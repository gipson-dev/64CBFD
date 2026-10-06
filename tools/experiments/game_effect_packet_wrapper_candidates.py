"""Recover the six-argument float-reference packet wrapper under the existing profile."""

import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_record_neighbor_visit_candidates import replace
from tools.match_progress import load_elf_functions


ENTRY, ROM, WORDS = 0x150C2804, 0xEFCB4, 37
TYPES = ('typedef unsigned char u8; typedef signed char s8; typedef short s16;\n'
         'typedef int s32; typedef unsigned int u32; typedef float f32;\n')
PACKET = '''typedef struct PacketEF410 {
    f32 *x;
    f32 *y;
    f32 *z;
    f32 parameter0;
    f32 parameter1;
    s16 delta;
    u8 flags;
    u8 byte17;
    u8 byte18;
    s8 sentinel;
} PacketEF410;'''
DECLARATIONS = ('extern f32 D_800A0280;\nextern f32 D_800A0284;\n'
                'void *func_15134908(void *, s32, u8, s32);\n')
SELECTED = '''void func_150C2804(f32 *x, f32 *y, f32 *z, s16 delta, u8 channel, s32 context) {
    PacketEF410 packet;

    packet.parameter0 = D_800A0280;
    packet.x = x;
    packet.y = y;
    packet.z = z;
    packet.parameter1 = D_800A0284;
    packet.delta = delta;
    packet.flags = 5;
    packet.byte17 = 6;
    packet.byte18 = 3;
    packet.sentinel = -1;
    func_15134908(&packet, 0, channel, context);
}'''
PROFILES = {'o2g3': ['-O2', '-g3'], 'o2': ['-O2'], 'o1g3': ['-O1', '-g3'], 'o1': ['-O1']}
SYMBOLS = {'D_800A0280': 0x800A0280, 'D_800A0284': 0x800A0284, 'func_15134908': 0x15134908}


def candidates():
    forms = [('retained-order', SELECTED)]
    assignments = SELECTED.split('\n\n', 1)[1].split('    func_15134908(', 1)[0].splitlines(keepends=True)
    original = ''.join(assignments)
    for name, order in (('field-order', (1, 2, 3, 0, 4, 5, 6, 7, 8, 9)),
                        ('flags-first', (6, 7, 8, 9, 0, 1, 2, 3, 4, 5)),
                        ('globals-first', (0, 4, 1, 2, 3, 5, 6, 7, 8, 9))):
        forms.append((name, replace(SELECTED, original, ''.join(assignments[i] for i in order))))
    forms.append(('wide-delta', replace(SELECTED, 's16 delta,', 's32 delta,')))
    forms.append(('pointer-return', replace(replace(SELECTED, 'void func_', 'void *func_'),
                                           '    func_15134908(', '    return func_15134908(')))
    return forms


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3', packet=PACKET):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text(TYPES + packet + '\n' + DECLARATIONS + body + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-mips2', '-o32', *PROFILES[profile], '-o', str(obj.relative_to(root)), str(source.relative_to(root))]
    compiled = subprocess.run(command, cwd=root, capture_output=True, text=True)
    diagnostics = compiled.stdout + compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'packet.ld'
    script.write_text('SECTIONS { .text 0x150C2804 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_150C2804',
                    *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
                   capture_output=True, text=True, check=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_150C2804']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    if any(words[end:]):
        raise ValueError('nonzero tail after return')
    words = words[:end]
    retail = list(struct.unpack_from('>37I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    slot = words + [0] * max(0, WORDS - end)
    differences = [(i * 4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, profile=profile, body_words=end, frame=(-words[0]) & 65535,
                differences=len(differences) + max(0, end - WORDS), different_words=differences,
                exact=words == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-effect-packet-wrapper'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
