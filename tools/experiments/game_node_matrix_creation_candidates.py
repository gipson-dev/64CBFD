"""Recover matrix-backed creation and post-call homes in func_150335C8."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.experiments import game_node_transform_setup_candidates as setup
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x150335C8, 0x60A78, 113
FUNCTION = 'func_150335C8'
STUB = 's32 func_150335C8() {\n    return 0;\n}'
SYMBOLS = dict(func_15083568=0x15083568, guMtxL2F=0x151EFEB8, func_15048B10=0x15048B10,
    func_150A9B0C=0x150A9B0C, func_150A7A48=0x150A7A48, func_1503E5F8=0x1503E5F8,
    func_15030D54=0x15030D54)
DECLARATIONS = '''u8 *func_15083568(u8 *, s32, f32, s32);
void func_15048B10(f32 [4][4], f32 [4][4]);
void func_150A9B0C(f32 [4][4], f32, f32, f32, f32, f32, f32);
void func_150A7A48(f32 [4][4], f32 [4][4], f32 [4][4]);
void func_1503E5F8(f32 [4][4], f32 *, f32 *, f32 *, f32 *, f32 *, f32 *, f32 *, f32 *, f32 *);
void func_15030D54(u8 *, f32, f32, f32, f32, f32, f32);'''
SELECTED = '''u8 *func_150335C8(register u8 *node, u8 *actor, s32 kind, s32 index, s32 clear_flag, s32 zero_position) {
    u8 *created;
    f32 converted[4][4];
    f32 inverse[4][4];
    f32 transform[4][4];
    f32 combined[4][4];
    f32 position_x;
    f32 position_y;
    f32 position_z;
    f32 scale_x;
    f32 scale_y;
    f32 scale_z;
    f32 angle_x;
    f32 angle_y;
    f32 angle_z;

    if (*(Mtx **)(actor + 0x1D4) == 0) {
        return 0;
    }
    created = func_15083568(actor, kind, 1.0f, 0);
    if (created == 0) {
        return 0;
    }
    created[2] = index;
    *(f32 *)(created + 0x40) = *(f32 *)(node + 0x14C);
    if (clear_flag != 0) {
        created[0x16] &= ~4;
    } else {
        created[0x16] |= 4;
    }
    guMtxL2F(converted, *(Mtx **)(actor + 0x1D4) + index);
    func_15048B10(converted, inverse);
    func_150A9B0C(transform, *(f32 *)(node + 0xB8), *(f32 *)(node + 0x40),
        *(f32 *)(node + 0xC4), *(f32 *)(node + 0x14C), *(f32 *)(node + 0x150),
        *(f32 *)(node + 0x14C));
    transform[3][0] = *(f32 *)(node + 0x14);
    transform[3][1] = *(f32 *)(node + 0x18);
    transform[3][2] = *(f32 *)(node + 0x1C);
    transform[0][3] = 0.0f;
    transform[1][3] = 0.0f;
    transform[2][3] = 0.0f;
    transform[3][3] = 1.0f;
    func_150A7A48(transform, inverse, combined);
    func_1503E5F8(combined, &position_x, &position_y, &position_z,
        &angle_x, &angle_y, &angle_z, &scale_x, &scale_y, &scale_z);
    if (zero_position != 0) {
        position_z = 0.0f;
        position_y = 0.0f;
        position_x = 0.0f;
    }
    func_15030D54(created, position_x, position_y, position_z, angle_x, angle_y, angle_z);
    return created;
}'''
EARLY_RETURN = SELECTED
SELECTED = SELECTED.replace('    if (created == 0) {\n        return 0;\n    }\n',
    '    if (created != 0) {\n').replace('    return created;\n}', '        return created;\n    }\n    return 0;\n}')
opening, processing = SELECTED.split('    if (created != 0) {\n', 1)
processing, ending = processing.split('        return created;\n', 1)
SELECTED = opening+'    if (created != 0) {\n'+''.join('    '+line+'\n' for line in processing.splitlines())+'        return created;\n'+ending


def candidates():
    yield 'selected', SELECTED
    yield 'early-return', EARLY_RETURN
    yield 'ordinary-node', SELECTED.replace('register u8 *node', 'u8 *node')
    yield 'volatile-result', SELECTED.replace('    u8 *created;', '    u8 *volatile created;')
    yield 'negative-cached-bank', SELECTED.replace('    u8 *created;', '    u8 *created;\n    Mtx *bank;').replace(
        'if (*(Mtx **)(actor + 0x1D4) == 0)', 'if ((bank = *(Mtx **)(actor + 0x1D4)) == 0)').replace(
        'guMtxL2F(converted, *(Mtx **)(actor + 0x1D4) + index)', 'guMtxL2F(converted, bank + index)')
    yield 'negative-index-byte', SELECTED.replace('+ index);', '+ (u8)index);')
    yield 'negative-flag-direction', SELECTED.replace('if (clear_flag != 0)', 'if (clear_flag == 0)')
    yield 'negative-no-zero-position', SELECTED.replace('if (zero_position != 0)', 'if (0)')
    yield 'negative-reversed-matrices', SELECTED.replace('func_150A7A48(transform, inverse, combined)',
        'func_150A7A48(inverse, transform, combined)')


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
    script = out / 'matrix-creation.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % ENTRY)
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()],'-o',str(elf),str(obj)],check=True,capture_output=True)
    _, functions, relocs = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4), pools['.text'][1],meta['value']))
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
    parser.add_argument('--owner',action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-node-matrix-creation'
    if args.owner:
        out.mkdir(exist_ok=True)
        source = (root / 'conker/src/game/generated_5D2C0.c').read_text()
        source = source.replace(SELECTED,STUB).replace(setup.SELECTED,setup.STUB)
        source = source.replace(DECLARATIONS+'\n','',1).replace(setup.DECLARATION+'\n','',1)
        assert source.count(STUB) == 1
        source = source.replace(STUB,SELECTED).replace('#include <ultra64.h>\n',
            '#include <ultra64.h>\n'+DECLARATIONS+'\n'+setup.DECLARATION+'\n',1)
        source = source.replace(setup.STUB,setup.SELECTED)
        obj,warnings = compile_owner(root,out,source,'owner-selected')
        print(obj,warnings,flush=True)
        return
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
