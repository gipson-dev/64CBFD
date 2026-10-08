"""Recover the attachment setup gate and end-minus-one progress predicate."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x1503327C, 0x6072C, 43
FUNCTION, SETUP = 'func_1503327C', 0x1503F5B8
DECLARATION = 'void func_1503F5B8(u8 *, s32, s32, f32, f32, s32);'
BASELINE = '''s32 func_1503327C(u8 *node, u8 *actor) {
    u8 *attachment;

    attachment = *(u8 **)(node + 0x48);
    if (attachment == 0) {
        return 0;
    }
    if ((*(u16 *)(attachment + 4) & 0x8000) != 0x8000) {
        func_1503F5B8(attachment, 0, 0, 1.0f, 0.0f, 1);
        attachment = *(u8 **)(node + 0x48);
    }
    if (*(f32 *)(attachment + 0x18) - 1.0f <= *(f32 *)(attachment + 8)) {
        return 1;
    }
    return 0;
}'''


def candidates():
    for comparison, mask, boolean, register in itertools.product(
            ('end-first', 'current-first'), ('full', 'zero'), (False, True), (False, True)):
        body = BASELINE
        if comparison == 'current-first':
            body = body.replace('*(f32 *)(attachment + 0x18) - 1.0f <= *(f32 *)(attachment + 8)',
                '*(f32 *)(attachment + 8) >= *(f32 *)(attachment + 0x18) - 1.0f')
        if mask == 'zero':
            body = body.replace('& 0x8000) != 0x8000', '& 0x8000) == 0')
        if boolean:
            condition = body.split('    if (*(f32 *)', 1)[1].split(') {\n', 1)[0]
            body = body.split('    if (*(f32 *)', 1)[0]+'    return *(f32 *)'+condition+';\n}'
        if register:
            body = body.replace('    u8 *attachment;', '    register u8 *attachment;')
        yield '%s-mask%s-boolean%d-register%d' % (comparison, mask, boolean, register), body


SELECTED = BASELINE


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3'):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+DECLARATION+'\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'attachment-progress.ld'
    script.write_text('SECTIONS { .text 0x1503327C : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        '--defsym=func_1503F5B8=0x1503F5B8', '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, functions, relocs = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>43I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics=diagnostics, relocations=relocs, pool_bytes=len(pools.get('.rodata', (0, b''))[1])), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-attachment-progress'
    forms = [('profile-'+profile, SELECTED, profile) for profile in PROFILES] if args.profiles else (
        [(name, body, 'o2g3') for name, body in candidates()])
    records = []
    for name, body, profile in forms:
        record, _ = compile_candidate(root, out, name, body, profile)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (out / ('profiles.json' if args.profiles else 'measurements.json')).write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
