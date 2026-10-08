"""Recover the six-float attachment record allocator used by matrix creation."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15030D54, 0x5E204, 45
FUNCTION = 'func_15030D54'
STUB = 's32 func_15030D54() {\n    return 0;\n}'
DECLARATION = 'void *allocate_memory(s32, s32, s32, s32);'
SELECTED = '''void func_15030D54(register u8 *node, f32 x, f32 y, f32 z, f32 angle_x, f32 angle_y, f32 angle_z) {
    u8 *values;

    values = allocate_memory(0x18, 1, 0, 2);
    *(u8 **)(node + 0x44) = values;
    if (values != 0) {
        *(f32 *)values = x;
        *(f32 *)(*(u8 **)(node + 0x44) + 4) = y;
        *(f32 *)(*(u8 **)(node + 0x44) + 8) = z;
        *(f32 *)(*(u8 **)(node + 0x44) + 0xC) = angle_x;
        *(f32 *)(*(u8 **)(node + 0x44) + 0x10) = angle_y;
        *(f32 *)(*(u8 **)(node + 0x44) + 0x14) = angle_z;
        if (*(u8 **)(node + 0x34) == 0) {
            *(u8 **)(node + 0x34) = allocate_memory(0x80, 1, 2, 2);
        }
    }
}'''
BASELINE = SELECTED
SELECTED = SELECTED.replace('*(f32 *)values = x;', '*(f32 *)*(u8 **)(node + 0x44) = x;')


def candidates():
    yield 'selected', SELECTED
    yield 'cached-first-store', BASELINE
    yield 'ordinary-node', SELECTED.replace('register u8 *node', 'u8 *node')
    yield 'early-return', SELECTED.replace('    if (values != 0) {\n', '    if (values == 0) { return; }\n    {\n')
    yield 'negative-cached-values', SELECTED.replace('*(u8 **)(node + 0x44) +', 'values +')
    yield 'negative-first-class', SELECTED.replace('0x18, 1, 0, 2', '0x18, 1, 2, 2')
    yield 'negative-second-size', SELECTED.replace('0x80, 1, 2, 2', '0x40, 1, 2, 2')
    yield 'negative-reverse-last', SELECTED.replace('= angle_y;', '= angle_z;').replace('= angle_z;\n        if', '= angle_y;\n        if')
    yield 'negative-always-bank', SELECTED.replace('if (*(u8 **)(node + 0x34) == 0)', 'if (1)')


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3'):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n'+DECLARATION+'\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    if result.returncode or result.stdout or result.stderr:
        raise ValueError(result.stdout+result.stderr)
    script = out / 'transform-setup.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % ENTRY)
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',FUNCTION,
        '--defsym=allocate_memory=0x10003C40','-o',str(elf),str(obj)],check=True,capture_output=True)
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
    out = root / 'conker/build/game-node-transform-setup'
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
