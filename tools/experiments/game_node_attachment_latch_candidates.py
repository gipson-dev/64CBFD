"""Recover the actor attachment-state latch and its activation/deactivation gates."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15033838, 0x60CE8, 100
FUNCTION = 'func_15033838'
STUB = 's32 func_15033838() {\n    return 0;\n}'
DECLARATIONS = 'void func_151026BC(u8 *, s32, s32, s32, s32, s32);\nvoid func_151027E8(u8 *);'
SELECTED = '''s32 func_15033838(u8 *node, u8 *actor) {
    s32 valid;
    s32 mode;
    u8 *attached;

    valid = 0;
    if (node[6] == 0x16) {
        mode = 4;
        if (*(u16 *)(actor + 0x84) == 0x165) {
            valid = 1;
        }
    } else if (node[6] == 0x89) {
        mode = 6;
        if (*(u16 *)(actor + 0x84) == 0x221 ||
            *(u16 *)(actor + 0x84) == 0x223 ||
            *(u16 *)(actor + 0x84) == 0x31B) {
            if ((*(u8 **)(actor + 0x31C))[0x198] == 2) {
                valid = 1;
            }
        }
    } else {
        mode = 5;
        if (*(u16 *)(actor + 0x84) == 0x157) {
            valid = 1;
        }
    }
    if (*(s32 *)(node + 0x38) == 0) {
        if (valid != 0) {
            attached = *(u8 **)(actor + 0x31C);
            if ((attached[0x197] != 0 || mode == 6) &&
                (*(u16 *)(attached + 0x8A) & 0x2000) == 0x2000 &&
                *(u16 *)(attached + 0x19E) == 0) {
                *(s32 *)(node + 0x38) = 1;
                func_151026BC(actor, -1, mode, 1, 255, 1);
            }
        }
    } else {
        if (valid != 0) {
            attached = *(u8 **)(actor + 0x31C);
            if ((*(u16 *)(attached + 0x8A) & 0x2000) != 0 &&
                (attached[0x197] != 0 || mode == 6)) {
                return 0;
            }
        }
        *(s32 *)(node + 0x38) = 0;
        func_151027E8(actor);
    }
    return 0;
}'''

EARLY_RETURN = SELECTED
SELECTED = SELECTED.replace('''            if ((*(u16 *)(attached + 0x8A) & 0x2000) != 0 &&
                (attached[0x197] != 0 || mode == 6)) {
                return 0;
            }''', '''            if ((*(u16 *)(attached + 0x8A) & 0x2000) != 0) {
                if (attached[0x197] != 0) {
                    goto done;
                }
                if (mode == 6) {
                    goto done;
                }
            }''').replace('    return 0;\n}', 'done:\n    return 0;\n}')


def candidates():
    yield 'selected', SELECTED
    yield 'nested-early-return', EARLY_RETURN
    yield 'register-node', SELECTED.replace('u8 *node,', 'register u8 *node,')
    yield 'register-actor', SELECTED.replace('u8 *actor)', 'register u8 *actor)')
    yield 'register-both', SELECTED.replace('u8 *node, u8 *actor)', 'register u8 *node, register u8 *actor)')
    yield 'nonzero-bit', SELECTED.replace('& 0x2000) == 0x2000', '& 0x2000) != 0')
    yield 'negative-wrong-action', SELECTED.replace('node[6] == 0x89', 'node[6] == 0x88')
    yield 'signed-type', SELECTED.replace('*(u16 *)(actor + 0x84)', '*(s16 *)(actor + 0x84)')
    yield 'negative-counter-on-hold', SELECTED.replace('& 0x2000) != 0)',
        '& 0x2000) != 0 && *(u16 *)(attached + 0x19E) == 0)')
    yield 'negative-mode-no-bypass', SELECTED.replace('attached[0x197] != 0 || mode == 6', 'attached[0x197] != 0')
    yield 'negative-swapped-enable', SELECTED.replace('actor, -1, mode, 1, 255, 1', 'actor, -1, mode, 255, 1, 1')
    yield 'negative-late-clear', SELECTED.replace('        *(s32 *)(node + 0x38) = 0;\n        func_151027E8(actor);',
        '        func_151027E8(actor);\n        *(s32 *)(node + 0x38) = 0;')
    yield 'negative-late-enable', SELECTED.replace('                *(s32 *)(node + 0x38) = 1;\n                func_151026BC(actor, -1, mode, 1, 255, 1);',
        '                func_151026BC(actor, -1, mode, 1, 255, 1);\n                *(s32 *)(node + 0x38) = 1;')
    yield 'negative-byte-counter', SELECTED.replace('*(u16 *)(attached + 0x19E)', 'attached[0x19E]')
    yield 'negative-wrong-mode', SELECTED.replace('mode = 6;', 'mode = 5;')


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3'):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n'+DECLARATIONS+'\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    if result.returncode or result.stdout or result.stderr:
        raise ValueError(result.stdout+result.stderr)
    script = out / 'attachment-latch.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % ENTRY)
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',FUNCTION,
        '--defsym=func_151026BC=0x151026BC','--defsym=func_151027E8=0x151027E8',
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
    out = root / 'conker/build/game-node-attachment-latch'
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
