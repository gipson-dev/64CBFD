"""Recover the fourteen-mode four-halfword output leaf."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x151442FC, 0x1717AC, 120
FUNCTION = 'func_151442FC'
TABLE, ANCHOR = 0x800A565C, 'jtbl_800A565C_game'
TARGETS = (0x15144368, 0x15144380, 0x15144324, 0x15144324, 0x151443D0,
    0x151443FC, 0x15144428, 0x15144398, 0x151443B4, 0x15144494,
    0x1514444C, 0x15144470, 0x15144398, 0x15144348)
PROTOTYPE = '''void func_151442FC(s16 *out0, s16 *out1, s16 *out2, s16 *out3,
    u8 input0, u8 input1, u8 input2, u8 input3,
    u8 direct0, u8 direct1, u8 direct2, u8 direct3, u8 scale, u8 mode);'''
SCALE = '        *out0 = *out1 = *out2 = scale;'
PRODUCT = '        *out3 = (input3 * direct3) >> 8;'
FIRST = '''        *out0 = input0;
        *out1 = input1;
        *out2 = input2;'''
DIRECT = '''        *out0 = direct0;
        *out1 = direct1;
        *out2 = direct2;'''
ZERO = '''        *out2 = 0;
        *out0 = *out1 = *out2;'''
CASES = {
    2: FIRST + '\n        *out3 = input3;',
    13: FIRST + '\n        *out3 = 0;',
    0: '''        *out3 = 0;
        *out0 = *out1 = *out2 = *out3;''',
    1: SCALE + '\n        *out3 = 0;',
    7: ZERO + '\n        *out3 = direct3;',
    8: ZERO + '\n        *out3 = input3;',
    4: SCALE + '\n' + PRODUCT,
    5: SCALE + '\n' + PRODUCT,
    6: FIRST + '\n        *out3 = direct3;',
    10: DIRECT + '\n        *out3 = direct3;',
    11: DIRECT + '\n        *out3 = input3;',
    9: SCALE + '\n        *out3 = direct3;',
}


def make_body(order=(2,13,0,1,7,8,4,5,6,10,11,9), chained=True,
              reverse_product=False, shared_product=False):
    body = PROTOTYPE[:-1] + ' {\n    switch (mode) {\n'
    for mode in order:
        if shared_product and mode == 4:
            body += '    case 4:\n'
            continue
        block = CASES[mode]
        if not chained:
            block = block.replace(SCALE, '        *out2 = scale;\n        *out1 = scale;\n        *out0 = scale;')
            block = block.replace('*out0 = *out1 = *out2 = *out3;',
                '*out2 = *out3;\n        *out1 = *out2;\n        *out0 = *out1;')
            block = block.replace('*out0 = *out1 = *out2;',
                '*out1 = *out2;\n        *out0 = *out1;')
        if reverse_product: block = block.replace('input3 * direct3', 'direct3 * input3')
        labels = ('    case 2:\n    case 3:\n' if mode == 2 else
            '    case 7:\n    case 12:\n' if mode == 7 else '    case %d:\n' % mode)
        body += labels + block + '\n        break;\n'
    block = SCALE + '\n' + PRODUCT
    if not chained: block = block.replace(SCALE, '        *out2 = scale;\n        *out1 = scale;\n        *out0 = scale;')
    if reverse_product: block = block.replace('input3 * direct3', 'direct3 * input3')
    return body + '    default:\n' + block + '\n        break;\n    }\n}'


SELECTED = make_body()


def candidates():
    orders = ((2,13,0,1,7,8,4,5,6,10,11,9), (0,1,2,4,5,6,7,8,9,10,11,13),
        (2,13,0,1,7,8,4,5,6,9,10,11))
    for i, order in enumerate(orders):
        for chained, reverse, shared in itertools.product((False,True), repeat=3):
            yield 'order%d-chain%d-reverse%d-shared%d' % (i,chained,reverse,shared), make_body(order,chained,reverse,shared)


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n' + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics: raise ValueError(diagnostics)
    script = output / 'secondary-output.ld'
    script.write_text('SECTIONS { .text 0x151442FC : SUBALIGN(4) { *(.text) } .rodata 0x800A565C : SUBALIGN(4) { *(.rodata) } }\n')
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',FUNCTION,
        '-o',str(elf),str(obj)],check=True,capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta = functions[FUNCTION]; pools = sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4),pools['.text'][1],meta['value']))
    end = max(i for i,w in enumerate(words) if w == 0x03E00008) + 2
    assert not any(words[end:]); words = words[:end]
    retail = struct.unpack_from('>120I',(root/'conker/conker.us.bin').read_bytes(),ROM)
    frames = [(-w)&65535 for w in words if w&0xFFFF0000 == 0x27BD0000 and w&0x8000]
    table = list(struct.unpack('>%dI' % (len(pools['.rodata'][1])//4),pools['.rodata'][1])) if '.rodata' in pools else []
    return dict(name=name,profile=profile,body_words=end,frame=frames[0] if frames else 0,
        diagnostics=diagnostics,relocations=relocations,table=table,
        differences=sum(a!=b for a,b in itertools.zip_longest(words,retail,fillvalue=0))),words


def owner_guards():
    return [dict(filename='game_16EE20',function=FUNCTION,offset='0x%X'%offset,
        expected='0x%08X'%expected,replacement='0x%08X'%replacement,
        expected_relocations=kind+':.rodata',replacement_relocations=kind+':'+ANCHOR,
        note='Bind secondary output switch to its preserved retail jump table',
        insert_after='',insert_after_relocations='',omit='false')
        for offset,expected,replacement,kind in (
            (0x14,0x3C010000,0x3C010000,'R_MIPS_HI16'),
            (0x1C,0x8C2E0284,0x8C2E0000,'R_MIPS_LO16'))]


def main():
    root=Path(__file__).resolve().parents[2]
    output=root/'conker/build/game-secondary-output';output.mkdir(exist_ok=True)
    records=[]
    for name,body in candidates():
        for profile in PROFILES:
            record,_=compile_candidate(root,output,name+'-'+profile,body,profile)
            records.append(record)
            print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__=='__main__': main()
