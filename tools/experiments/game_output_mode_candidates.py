"""Recover the four halfword outputs and fourteen-position stack-byte ABI."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x151441A4, 0x171654, 86
FUNCTION = 'func_151441A4'
TABLE, ANCHOR = 0x800A5648, 'jtbl_800A5648_game'
PROTOTYPE = '''void func_151441A4(s16 *out0, s16 *out1, s16 *out2, s16 *out3,
    u8 input0, u8 input1, u8 input2, u8 input3,
    u8 direct0, u8 direct1, u8 direct2, u8 direct3, u8 scale, u8 mode);'''
SCALED = '''        *out0 = (input0 * scale) >> 8;
        *out1 = (input1 * scale) >> 8;
        *out2 = (input2 * scale) >> 8;
        *out3 = 0;'''
CASES = {
    2: '''        *out0 = direct0;
        *out1 = direct1;
        *out2 = direct2;
        *out3 = direct3;''',
    0: '''        *out3 = 0;
        *out0 = *out1 = *out2 = *out3;''',
    1: '''        *out2 = 0;
        *out0 = *out1 = *out2;
        *out3 = direct3;''',
    3: SCALED, 4: SCALED,
}


def make_body(order=(2, 0, 1, 3, 4), chained=True, unsigned_product=False, shared=False):
    body = PROTOTYPE[:-1] + ' {\n    switch (mode) {\n'
    for mode in order:
        if shared and mode == 3:
            body += '    case 3:\n'
            continue
        block = CASES[mode]
        if not chained and mode == 0:
            block = '        *out3 = 0;\n        *out2 = *out3;\n        *out1 = *out2;\n        *out0 = *out1;'
        if not chained and mode == 1:
            block = '        *out2 = 0;\n        *out1 = *out2;\n        *out0 = *out1;\n        *out3 = direct3;'
        if unsigned_product:
            for i in range(3): block = block.replace('input%d * scale' % i, '(u32)input%d * scale' % i)
        body += '    case %d:\n%s\n        break;\n' % (mode, block)
    block = SCALED
    if unsigned_product:
        for i in range(3): block = block.replace('input%d * scale' % i, '(u32)input%d * scale' % i)
    body += '    default:\n%s\n        break;\n    }\n}' % block
    return body


SELECTED = make_body()


def candidates():
    for order, chained, unsigned_product, shared in itertools.product(
            ((2,0,1,3,4), (0,1,2,3,4), (2,1,0,3,4)), (False,True), (False,True), (False,True)):
        yield 'order%s-chain%d-unsigned%d-shared%d' % (''.join(map(str,order)),chained,unsigned_product,shared), make_body(
            order,chained,unsigned_product,shared)


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
    script = output / 'output-mode.ld'
    script.write_text('SECTIONS { .text 0x151441A4 : SUBALIGN(4) { *(.text) } .rodata 0x800A5648 : SUBALIGN(4) { *(.rodata) } }\n')
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',FUNCTION,
        '-o',str(elf),str(obj)],check=True,capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta = functions[FUNCTION]; pools = sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4),pools['.text'][1],meta['value']))
    end = max(i for i,w in enumerate(words) if w == 0x03E00008) + 2
    assert not any(words[end:]); words = words[:end]
    retail = struct.unpack_from('>86I',(root/'conker/conker.us.bin').read_bytes(),ROM)
    frames = [(-w)&65535 for w in words if w&0xFFFF0000 == 0x27BD0000 and w&0x8000]
    table = list(struct.unpack('>%dI' % (len(pools['.rodata'][1])//4),pools['.rodata'][1])) if '.rodata' in pools else []
    return dict(name=name,profile=profile,body_words=end,frame=frames[0] if frames else 0,
        diagnostics=diagnostics,relocations=relocations,table=table,
        differences=sum(a!=b for a,b in itertools.zip_longest(words,retail,fillvalue=0))),words


def owner_guards():
    return [dict(filename='game_16EE20',function=FUNCTION,offset='0x%X'%offset,
        expected='0x%08X'%expected,replacement='0x%08X'%replacement,
        expected_relocations=kind+':.rodata',replacement_relocations=kind+':'+ANCHOR,
        note='Bind output mode switch to its preserved retail jump table',
        insert_after='',insert_after_relocations='',omit='false')
        for offset,expected,replacement,kind in (
            (0x18,0x3C010000,0x3C010000,'R_MIPS_HI16'),
            (0x20,0x8C2E0270,0x8C2E0000,'R_MIPS_LO16'))]


def main():
    root=Path(__file__).resolve().parents[2]
    output=root/'conker/build/game-output-mode';output.mkdir(exist_ok=True)
    records=[]
    for name,body in candidates():
        for profile in PROFILES:
            record,_=compile_candidate(root,output,name+'-'+profile,body,profile)
            records.append(record)
            print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__=='__main__': main()
