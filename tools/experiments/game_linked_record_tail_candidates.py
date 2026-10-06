"""Isolated linked-record volatile-store and backend tail-optimization controls."""

import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_record_neighbor_visit_candidates import replace


CHECKPOINT = '''void func_150E6FAC(f32 *output, u8 *actor) {
    void *node;
    u8 *record;
    f32 radius;
    s16 angle;
    f32 xOffset;
    f32 zOffset;

    if (func_1514ECE0(*(void **)(actor + 0x2F4), 0x16, &node)) {
        radius = func_150ADA68() * 100.0f + 80.0f;
        angle = func_150ADA20() & 0xFF;
        xOffset = func_151423D8((u8)(angle - 0x40));
        zOffset = func_151423D8((u8)angle);
        record = *(u8 **)((u8 *)node + 0x10);
        output[0] = (*(f32 *)(record + 0x38) * -80.0f + *(f32 *)(actor + 0x14)) + xOffset * radius;
        output[1] = (*(f32 *)(record + 0x3C) * -80.0f + *(f32 *)(actor + 0x18)) + 100.0f;
        output[2] = (*(f32 *)(record + 0x40) * -80.0f + *(f32 *)(actor + 0x1C)) + zOffset * radius;
    } else {
        output[0] = *(f32 *)(actor + 0x14);
        output[1] = *(f32 *)(actor + 0x18);
        output[2] = *(f32 *)(actor + 0x1C);
    }
}'''
TYPES = 'typedef unsigned char u8; typedef short s16; typedef int s32; typedef float f32;\n'
DECLARATIONS = ('s32 func_150ADA20(void); f32 func_150ADA68(void);\n'
                'f32 func_151423D8(u8); s32 func_1514ECE0(void *,s16,void **);\n')
SYMBOLS = (0x150ADA20, 0x150ADA68, 0x151423D8, 0x1514ECE0)
PROFILES = {'control': [], 'no-tail': ['-Wc,-notailopt'],
            'no-peep': ['-Wb,-nopeep'], 'no-tail-peep': ['-Wc,-notailopt', '-Wb,-nopeep']}
GUARDS = {0x28: (0x50400032, 0x50400033, None),
          0xE8: (0x10000007, 0xE6320008, None),
          0xEC: (0xE6320008, 0x10000008, 0x8FBF001C)}


def normalize(words, omitted=None):
    if len(words) != 71:
        raise ValueError('unexpected linked-record body length')
    result = []
    for index, word in enumerate(words):
        offset = index * 4
        if offset in GUARDS:
            expected, replacement, inserted = GUARDS[offset]
            if word != expected:
                raise ValueError('stale linked-record guard at ' + hex(offset))
            if offset != omitted:
                result.append(replacement)
                if inserted is not None:
                    result.append(inserted)
                continue
        result.append(word)
    return result


def candidates():
    forms = [('control', CHECKPOINT)]
    success = '        output[2] = (*(f32 *)(record + 0x40)'
    fallback = '        output[2] = *(f32 *)(actor + 0x1C);'
    for mask in (1, 2, 3):
        body = CHECKPOINT
        if mask & 1:
            body = replace(body, success, success.replace('output[2]', '((volatile f32 *)output)[2]'))
        if mask & 2:
            body = replace(body, fallback, fallback.replace('output[2]', '((volatile f32 *)output)[2]'))
        forms.append(('volatile-' + str(mask), body))
    return forms


def compile_candidate(root, output, name, body, flags=()):
    source, obj, elf, binary = (output / (name + suffix) for suffix in ('.c', '.o', '.elf', '.bin'))
    source.write_text(TYPES + DECLARATIONS + body + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
               '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared',
               '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3', *flags,
               '-o', str(obj.relative_to(root)), str(source.relative_to(root))]
    compiled = subprocess.run(command, cwd=root, capture_output=True, text=True)
    diagnostics = compiled.stdout + compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'position.ld'
    script.write_text('SECTIONS { .text 0x150E6FAC : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e',
                    'func_150E6FAC', *['--defsym=func_%08X=0x%08X' % (s, s) for s in SYMBOLS],
                    '-o', str(elf), str(obj)], capture_output=True, text=True, check=True)
    subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', '.text', str(elf), str(binary)],
                   capture_output=True, text=True, check=True)
    data = binary.read_bytes()
    words = list(struct.unpack('>%dI' % (len(data) // 4), data))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    if any(words[end:]):
        raise ValueError('nonzero instructions after final return')
    words = words[:end]
    retail = list(struct.unpack_from('>72I', (root / 'conker/conker.us.bin').read_bytes(), 0x11445C))
    slot = words + [0] * max(0, 72 - end)
    record = dict(name=name, body_words=end, frame=(-words[0]) & 65535,
                  differences=sum(a != b for a, b in zip(slot, retail)) + max(0, end - 72),
                  exact=words == retail, flags=list(flags), diagnostics=diagnostics,
                  differences_by_word=[(i, hex(slot[i]), hex(retail[i])) for i in range(72) if slot[i] != retail[i]])
    return record, words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-linked-record-tail'
    output.mkdir(exist_ok=True)
    report = []
    for name, body in candidates():
        for profile, flags in PROFILES.items():
            record, _ = compile_candidate(root, output, name + '-' + profile, body, flags)
            report.append(record)
            print(record['name'], record['body_words'], record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(report, indent=2) + '\n')


if __name__ == '__main__':
    main()
