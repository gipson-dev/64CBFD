"""Fit the node cleanup dispatcher and its two private callback packets."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15031C14, 0x5F0C4, 134
FUNCTION, TABLE = 'func_15031C14', 0x8009701C
SYMBOLS = {name: int(name[5:], 16) for name in (
    'func_15083E90', 'func_15033BDC', 'func_1000FD38', 'func_15100180',
    'func_151616D0', 'func_15147D64', 'func_151494E0', 'func_151BD7F4',
    'func_151D4668', 'func_151D747C', 'func_151027E8')}
DECLARATIONS = '''typedef struct {
    u8 *actor;
    u8 group;
} NodeCleanupPacket;
u8 *func_15083E90(s32);
s32 func_15033BDC();
void func_1000FD38(s32 (*)(), u8 *, u8 *);
void func_15100180(u8 *);
void func_151616D0(s32, s32, NodeCleanupPacket *);
void func_15147D64(NodeCleanupPacket *, s32);
void func_151494E0(NodeCleanupPacket *, s32);
void func_151BD7F4(u8 *);
void func_151D4668(u8 *);
void func_151D747C(u8 *);
void func_151027E8(u8 *);'''
SELECTED = '''void func_15031C14(u8 *node) {
    u8 *actor;
    NodeCleanupPacket first;
    NodeCleanupPacket second;
    u8 *state;
    /* Preserve the retail private pointer home across the paired callbacks. */
    NodeCleanupPacket *volatile packet;

    actor = func_15083E90(node[0]);
    if (actor == 0) {
        return;
    }
    switch (node[1]) {
        case 0x5A:
            state = *(u8 **)(actor + 0x31C);
            if (state != 0) {
                *(u16 *)(state + 0x1A6) -= 0xAA;
            }
            break;
        case 0x90:
            *(u32 *)(actor + 0x9C) &= ~0x70;
            break;
        case 0x8F:
            *(u32 *)(actor + 0x9C) &= ~0xE00;
            break;
        case 0x37:
        case 0x4B:
        case 0x4C:
            func_1000FD38(func_15033BDC, node, actor);
            if (node[1] == 0x37) {
                func_15100180(actor);
            }
            break;
        case 0x49:
            first.actor = actor;
            first.group = actor[0x3B];
            func_151616D0(0x10, 0x29, &first);
            break;
        case 0x5D:
            second.actor = actor;
            second.group = actor[0x3B];
            packet = &second;
            func_15147D64(&second, 0x2E);
            func_151494E0(packet, 0x2F);
            break;
        case 0x3D:
            func_151BD7F4(actor);
            break;
        case 0x1A:
        case 0x1B:
        case 0x5F:
        case 0x65:
        case 0x66:
            func_151D4668(actor);
            break;
        case 0x1D:
        case 0x82:
            func_151D747C(actor);
            break;
        case 0x85:
        case 0x5E:
            *(u32 *)(actor + 0x9C) &= ~0x6000;
            break;
    }
    switch (node[6]) {
        case 0x16:
        case 0x63:
        case 0x89:
            func_151027E8(actor);
            func_151D4668(actor);
    }
}'''


def candidates():
    for actor_register, order, cleanup in itertools.product((False, True), (False, True), ('if', 'switch')):
        body = SELECTED
        if actor_register:
            body = body.replace('    u8 *actor;', '    register u8 *actor;')
        if order:
            body = body.replace('    NodeCleanupPacket first;\n    NodeCleanupPacket second;',
                '    NodeCleanupPacket second;\n    NodeCleanupPacket first;')
        if cleanup == 'if':
            body = body.replace('    switch (node[6]) {\n        case 0x16:\n        case 0x63:\n        case 0x89:',
                '    if (node[6] == 0x16 || node[6] == 0x63 || node[6] == 0x89) {')
        yield 'register%d-reverse%d-%s' % (actor_register, order, cleanup), body
    yield 'recompute-packet', SELECTED.replace('NodeCleanupPacket *volatile packet;', 'NodeCleanupPacket *packet;')
    yield 'volatile-first-argument', SELECTED.replace('func_15147D64(&second,', 'func_15147D64(packet,')


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3', declarations=DECLARATIONS):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+declarations+'\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    if result.returncode or result.stdout or result.stderr:
        raise ValueError(result.stdout+result.stderr)
    script = out / 'node-cleanup.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } '
        '.rodata 0x%X : SUBALIGN(4) { *(.rodata) } }\n' % (ENTRY, TABLE))
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocs = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
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
    out = root / 'conker/build/game-node-cleanup'
    forms = [('profile-'+p, SELECTED, p) for p in PROFILES] if args.profiles else (
        [(name, body, 'o2g3') for name, body in candidates()])
    records = []
    for name, body, profile in forms:
        record, _, _ = compile_candidate(root, out, name, body, profile)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], record['pool_bytes'], flush=True)
    (out / ('profiles.json' if args.profiles else 'measurements.json')).write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
