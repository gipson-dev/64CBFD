"""Recover the node effect handle's tile-scroll, freeze and registration lifecycle."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x150339C8, 0x60E78, 68
FUNCTION = 'func_150339C8'
STUB = 's32 func_150339C8() {\n    return 0;\n}'
SYMBOLS = {name:int(name[5:],16) for name in ('func_150334B8','func_15033BDC','func_1000FD38','func_1000FA64')}
SYMBOLS.update(D_800C35EA=0x800C35EA,D_800BEA0C=0x800BEA0C)
ALLOCATOR = 'u16 func_1000FA64(u16, s16, s16, s16, s32, u16, s16, s32, void *, s32, s32, s32);'
DECLARATIONS = '''s32 func_150334B8(u8 *, u8 *);
s32 func_15033BDC();
void func_1000FD38(s32 (*)(), u8 *, u8 *);
extern u8 D_800C35EA;
extern u8 D_800BEA0C;
''' + ALLOCATOR
SELECTED = '''s32 func_150339C8(u8 *node, u8 *actor) {
    func_150334B8(node, actor);
    if (D_800C35EA != 1) {
        if (D_800BEA0C != 0) {
            if (*(u32 *)(node + 0x3C) != 0) {
                func_1000FD38(func_15033BDC, node, actor);
            }
            *(u32 *)(node + 0x3C) = 0;
        } else if (*(u32 *)(node + 0x3C) == 0) {
            *(u32 *)(node + 0x3C) = func_1000FA64(0x448,
                (s16)*(f32 *)(actor + 0x14), (s16)*(f32 *)(actor + 0x18),
                (s16)*(f32 *)(actor + 0x1C), 32000, 1000, 500,
                (s32)func_15033BDC, node, (s32)actor, 0, 0) | 0x80000000;
        }
    }
    return 0;
}'''


def candidates():
    yield 'selected', SELECTED
    yield 'register-node', SELECTED.replace('u8 *node,', 'register u8 *node,')
    yield 'register-actor', SELECTED.replace('u8 *actor)', 'register u8 *actor)')
    yield 'register-both', SELECTED.replace('u8 *node, u8 *actor)', 'register u8 *node, register u8 *actor)')
    yield 'early-mode-return', SELECTED.replace('    if (D_800C35EA != 1) {',
        '    if (D_800C35EA == 1) { return 0; }\n    {')
    yield 'negative-skip-scroll', SELECTED.replace('    func_150334B8(node, actor);\n', '')
    yield 'negative-wrong-mode-gate', SELECTED.replace('D_800C35EA != 1', 'D_800C35EA == 0')
    yield 'negative-no-handle-bit', SELECTED.replace(' | 0x80000000', '')
    yield 'negative-byte-handle', SELECTED.replace('*(u32 *)(node + 0x3C)', 'node[0x3C]')
    yield 'negative-clear-before-unregister', SELECTED.replace('                func_1000FD38(func_15033BDC, node, actor);',
        '                *(u32 *)(node + 0x3C) = 0;\n                func_1000FD38(func_15033BDC, node, actor);')
    yield 'implicit-coordinate-narrowing', SELECTED.replace('(s16)*(f32 *)', '(s32)*(f32 *)')
    yield 'negative-integer-coordinate-bits', SELECTED.replace('(s16)*(f32 *)', '(s16)*(s32 *)')
    yield 'negative-reversed-coordinates', SELECTED.replace('actor + 0x14', 'actor + 0x20').replace(
        'actor + 0x1C', 'actor + 0x14').replace('actor + 0x20', 'actor + 0x1C')
    yield 'negative-wrong-effect', SELECTED.replace('func_1000FA64(0x448,', 'func_1000FA64(0x447,')
    yield 'negative-swapped-rate', SELECTED.replace('32000, 1000, 500', '32000, 500, 1000')


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3', declarations=DECLARATIONS):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n'+declarations+'\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    if result.returncode or result.stdout or result.stderr:
        raise ValueError(result.stdout+result.stderr)
    script = out / 'effect-registration.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % ENTRY)
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()],
        '-o',str(elf),str(obj)],check=True,capture_output=True)
    _, functions, relocs = parse_object(obj)
    meta,pools = functions[FUNCTION],sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4),pools['.text'][1],meta['value']))
    end = max(i for i,word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS,(root / 'conker/conker.us.bin').read_bytes(),ROM)
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    return dict(name=name,profile=profile,body_words=end,frame=frames[0] if frames else 0,
        differences=sum(a!=b for a,b in itertools.zip_longest(words,retail,fillvalue=0)),
        diagnostics='',relocations=relocs,pool_bytes=sum(len(v[1]) for n,v in pools.items()
            if n in ('.rodata','.data'))),words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles',action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-node-effect-registration'
    forms = [('profile-'+p,SELECTED,p) for p in PROFILES] if args.profiles else (
        [(name,body,'o2g3') for name,body in candidates()])
    records = []
    for name,body,profile in forms:
        record,_ = compile_candidate(root,out,name,body,profile)
        records.append(record)
        print(name,record['body_words'],hex(record['frame']),record['differences'],flush=True)
    (out / ('profiles.json' if args.profiles else 'measurements.json')).write_text(json.dumps(records,indent=2)+'\n')


if __name__ == '__main__':
    main()
