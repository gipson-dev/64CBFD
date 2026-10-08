"""Recover the two-table node action dispatcher without clearing retail V0."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15031A50, 0x5EF00, 113
FUNCTION, TABLE = 'func_15031A50', 0x80096F40
SYMBOLS = {'func_151001B4': 0x151001B4, 'func_15163BE8': 0x15163BE8,
    'func_150D3360': 0x150D3360, 'func_150D5440': 0x150D5440,
    'func_151BD828': 0x151BD828, 'func_151D74B0': 0x151D74B0,
    'func_150859AC': 0x150859AC, 'D_80090228': 0x80090228, 'D_8009022C': 0x8009022C}
DECLARATIONS = '''void func_151001B4(u8 *);
void func_15163BE8(u8 *, s32, s32);
void func_150D3360(u8 *, s32, s32);
void func_150D5440(u8 *, s32, s32);
void func_151BD828(u8 *, s32, s32);
void func_151D74B0(u8 *, s32, s32, s32, s32);
s32 func_150859AC(s32, s32);
extern s32 D_80090228;
extern s32 D_8009022C;'''
BASELINE = '''void func_15031A50(u8 *node, u8 *actor) {
    u8 *state;

    switch (node[1]) {
        case 0x37:
            func_151001B4(actor);
            break;
        case 0x5A:
            state = *(u8 **)(actor + 0x31C);
            if (state != 0) {
                *(u16 *)(state + 0x1A6) += 0xAA;
            }
            break;
        case 0x90:
            *(u32 *)(actor + 0x9C) |= 0x70;
            break;
        case 0x8F:
            *(u32 *)(actor + 0x9C) |= 0xE00;
            break;
        case 0x49:
            func_15163BE8(actor, 0xFF, 1);
            break;
        case 0x5D:
            func_150D3360(actor, 0xFF, 1);
            func_150D5440(actor, 0xFF, 1);
            break;
        case 0x3D:
            func_151BD828(actor, 0xFF, 1);
            break;
        case 0x1D:
            func_151D74B0(actor, 0, 2, 0xFF, 1);
            break;
        case 0x85:
        case 0x5E:
            *(u32 *)(actor + 0x9C) |= 0x6000;
            break;
        case 0x8D:
            if (func_150859AC(0, 6) < 100) {
                *(s16 *)(node + 0x18) = D_80090228;
            } else {
                *(s16 *)(node + 0x18) = D_8009022C;
            }
            break;
        case 0x82:
            func_151D74B0(actor, 6, -1, 0xFF, 1);
            break;
    }
}'''
SELECTED = BASELINE


def candidates():
    for kind, register, default in itertools.product(('inline', 's32', 'u32'), (False, True), (False, True)):
        body = BASELINE
        if kind != 'inline':
            body = body.replace('    u8 *state;', '    u8 *state;\n    %s action = node[1];' % kind)
            body = body.replace('switch (node[1])', 'switch (action)')
        if register:
            body = body.replace('u8 *node, u8 *actor', 'u8 *node, register u8 *actor')
        if default:
            body = body.replace('    }\n}', '        default:\n            break;\n    }\n}')
        yield '%s-register%d-default%d' % (kind, register, default), body


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3'):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+DECLARATIONS+'\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    if result.returncode or result.stdout or result.stderr:
        raise ValueError(result.stdout+result.stderr)
    script = out / 'node-action.ld'
    script.write_text('SECTIONS { .text 0x15031A50 : SUBALIGN(4) { *(.text) } '
        '.rodata 0x80096F40 : SUBALIGN(4) { *(.rodata) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocs = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>113I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    table_bytes = pools.get('.rodata', (TABLE, b''))[1]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics='', relocations=relocs, pool_bytes=len(table_bytes)), words, table_bytes


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-node-action'
    forms = [('profile-'+profile, SELECTED, profile) for profile in PROFILES] if args.profiles else (
        [(name, body, 'o2g3') for name, body in candidates()])
    records = []
    for name, body, profile in forms:
        record, _, _ = compile_candidate(root, out, name, body, profile)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], record['pool_bytes'], flush=True)
    (out / ('profiles.json' if args.profiles else 'measurements.json')).write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
