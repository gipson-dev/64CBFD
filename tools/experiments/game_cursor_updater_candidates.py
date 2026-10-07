"""Screen fixed-point cursor modes without losing live alias-sensitive stores."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES as SDK_PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x1514401C, 0x1714CC, 98
FUNCTION = 'func_1514401C'
SYMBOLS = dict(D_800BE9E4=0x800BE9E4, D_80090B64=0x80090B64)
PROFILES = dict(SDK_PROFILES, o2g3nounroll=('-O2', '-g3', '-Wo,-loopunroll,0'))
DECLARATIONS = '''typedef struct { u8 count; u8 pad1[11]; } GameCursorLimit;
extern GameCursorLimit D_80090B64[];
extern s32 D_800BE9E4;
'''
PROTOTYPE = 's32 func_1514401C(u8 index, s32 *velocity, s32 *position, u8 flags);'
BASELINE = '''s32 func_1514401C(u8 index, s32 *velocity, s32 *position, u8 flags) {
    s32 result = 0;
    s32 limit;
    s32 value;

    limit = (D_80090B64[index].count << 16) - 1;
    value = (u32)*position + (u32)*velocity * (u32)D_800BE9E4;
    *position = value;
    if (value > limit) {
        if (flags & 1) {
            result = 1;
        } else if (flags & 2) {
            *velocity = 0;
            *position = limit;
        } else if (flags & 4) {
            *position = limit - value % limit;
            *velocity = 0U - (u32)*velocity;
        } else {
            do {
                value = (u32)value - (u32)limit;
                *position = value;
            } while (value > limit);
        }
    } else if (value < 0) {
        if (!(flags & 8)) {
            if (flags & 16) {
                *velocity = 0;
                *position = 0;
            } else if (flags & 4) {
                *position = (s32)(0U - (u32)value) % limit;
                *velocity = 0U - (u32)*velocity;
            } else {
                do {
                    value = (u32)value + (u32)limit;
                    *position = value;
                } while (value < 0);
            }
        }
    }
    return result;
}'''


def candidates():
    for layout, init, update, product in itertools.product(range(6), (False,True), (False,True), (False,True)):
        body = BASELINE
        declarations = ('    s32 result = 0;', '    s32 limit;', '    s32 value;')
        order = list(itertools.permutations(declarations))[layout]
        body = body.replace('\n'.join(declarations), '\n'.join(order))
        if init:
            body = body.replace('s32 result = 0;', 's32 result;').replace(
                '    limit = ', '    result = 0;\n    limit = ', 1)
        if update:
            body = body.replace('    value = (u32)*position + (u32)*velocity * (u32)D_800BE9E4;\n    *position = value;',
                '    *position = (u32)*position + (u32)*velocity * (u32)D_800BE9E4;\n    value = *position;')
        if product:
            body = body.replace('(u32)*velocity * (u32)D_800BE9E4', '*velocity * D_800BE9E4')
        yield 'decl%d-init%d-update%d-product%d' % (layout,init,update,product), body


def loop_candidates():
    for initial, upper, lower in itertools.product((False,True),repeat=3):
        body=BASELINE
        if initial:
            body=body.replace('    value = (u32)*position + (u32)*velocity * (u32)D_800BE9E4;\n    *position = value;',
                '    *position = (u32)*position + (u32)*velocity * (u32)D_800BE9E4;\n    value = *position;')
        for enabled,op in ((upper,'-'),(lower,'+')):
            if enabled:
                indent='                ' if op=='-' else '                    '
                old=indent+'value = (u32)value %s (u32)limit;\n'%op+indent+'*position = value;'
                assert old in body
                body=body.replace(old,indent+'*position = (u32)value %s (u32)limit;\n'%op+indent+'value = *position;')
        yield 'initial%d-upper%d-lower%d'%(initial,upper,lower),body


def flow_candidates():
    base=dict(loop_candidates())['initial1-upper1-lower1']
    old='''                do {
                    *position = (u32)value + (u32)limit;
                    value = *position;
                } while (value < 0);'''
    forms=(old,
        '''                while (value < 0) {
                    *position = (u32)value + (u32)limit;
                    value = *position;
                }''',
        '''                for (; value < 0; value = *position) {
                    *position = (u32)value + (u32)limit;
                }''',
        '''                do {
                    *position = (u32)value + (u32)limit;
                } while ((value = *position) < 0);''')
    assert old in base
    for kind,loop in itertools.product(('s32','u32','s16','u8'),range(4)):
        yield 'result-%s-lower%d'%(kind,loop),base.replace('s32 result = 0;',kind+' result = 0;').replace(old,forms[loop])


def shape_candidates():
    base=dict(loop_candidates())['initial1-upper1-lower1']
    limit_forms=('limit = (D_80090B64[index].count << 16) - 1;',
        'limit = D_80090B64[index].count;\n    limit = (limit << 16) - 1;',
        'limit = D_80090B64[index].count << 16;\n    limit--;',
        'limit = D_80090B64[index].count;\n    limit <<= 16;\n    limit--;')
    for form,upper,lower in itertools.product(range(4),(False,True),(False,True)):
        body=base.replace(limit_forms[0],limit_forms[form])
        for enabled,op in ((upper,'-'),(lower,'+')):
            if enabled:
                body=body.replace('*position = (u32)value %s (u32)limit;'%op,
                    '*position = (u32)*position %s (u32)limit;'%op)
        yield 'limit%d-upper%d-lower%d'%(form,upper,lower),body


def compound_candidates():
    base=dict(loop_candidates())['initial1-upper1-lower1']
    for initial,upper,lower,predicate in itertools.product((False,True),repeat=4):
        body=base
        if initial:
            body=body.replace('*position = (u32)*position + (u32)*velocity * (u32)D_800BE9E4;',
                '*position += (u32)*velocity * (u32)D_800BE9E4;')
        for enabled,op in ((upper,'-'),(lower,'+')):
            if enabled:
                body=body.replace('*position = (u32)value %s (u32)limit;'%op,
                    '*position %s= (u32)limit;'%op)
        if predicate:body=body.replace('while (value < 0);','while (*position < 0);')
        yield 'compound%d%d%d-predicate%d'%(initial,upper,lower,predicate),body


def signedness_candidates():
    base=dict(loop_candidates())['initial1-upper1-lower1']
    for value_unsigned,limit_unsigned,register in itertools.product((False,True),repeat=3):
        body=base
        if value_unsigned:
            body=body.replace('s32 value;', 'u32 value;').replace('if (value > limit)', 'if ((s32)value > limit)').replace(
                'value % limit', '(s32)value % limit').replace('while (value > limit)', 'while ((s32)value > limit)').replace(
                'value < 0', '(s32)value < 0')
        if limit_unsigned:
            body=body.replace('s32 limit;', 'u32 limit;').replace('> limit', '> (s32)limit').replace(
                '% limit', '% (s32)limit')
        if register:
            body=body.replace('    s32 limit;', '    register s32 limit;').replace('    s32 value;', '    register s32 value;').replace(
                '    u32 limit;', '    register u32 limit;').replace('    u32 value;', '    register u32 value;')
        yield 'unsigned-value%d-limit%d-register%d'%(value_unsigned,limit_unsigned,register),body


SELECTED = dict(loop_candidates())['initial1-upper1-lower1']


def temporary_candidates():
    for kind,initial,upper,lower in itertools.product(('s32','u32'),(False,True),(False,True),(False,True)):
        if not (initial or upper or lower):continue
        body=SELECTED.replace('    s32 value;', '    s32 value;\n    %s next;'%kind)
        if initial:
            body=body.replace('    *position = (u32)*position + (u32)*velocity * (u32)D_800BE9E4;',
                '    next = (u32)*position + (u32)*velocity * (u32)D_800BE9E4;\n    *position = next;')
        for enabled,op in ((upper,'-'),(lower,'+')):
            if enabled:
                indent='                ' if op=='-' else '                    '
                old=indent+'*position = (u32)value %s (u32)limit;'%op
                assert old in body
                body=body.replace(old,indent+'next = (u32)value %s (u32)limit;\n'%op+indent+'*position = next;')
        yield 'temporary-%s-%d%d%d'%(kind,initial,upper,lower),body


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source,obj,elf=(output/(name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n'+DECLARATIONS+body+'\n')
    result=subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    diagnostics=result.stdout+result.stderr
    if result.returncode or diagnostics:raise ValueError(diagnostics)
    script=output/'cursor.ld'
    script.write_text('SECTIONS { .text 0x1514401C : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',FUNCTION,
        *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()],'-o',str(elf),str(obj)],check=True,capture_output=True)
    _,functions,relocations=parse_object(obj)
    meta=functions[FUNCTION];data=sections(elf)['.text'][1]
    words=list(struct.unpack_from('>%dI'%(meta['size']//4),data,meta['value']))
    end=max(i for i,w in enumerate(words) if w==0x03E00008)+2
    assert not any(words[end:]);words=words[:end]
    retail=struct.unpack_from('>98I',(root/'conker/conker.us.bin').read_bytes(),ROM)
    frames=[(-w)&65535 for w in words if w&0xFFFF0000==0x27BD0000 and w&0x8000]
    return dict(name=name,profile=profile,body_words=end,frame=frames[0] if frames else 0,diagnostics=diagnostics,
        relocations=relocations,differences=sum(a!=b for a,b in itertools.zip_longest(words,retail,fillvalue=0))),words


def register_mask(word):
    """Keep the opcode, branch target, immediate and fixed register roles intact."""
    op, fn = word >> 26, word & 63
    if op == 0:
        return {0: 0x001FF800, 16: 0x0000F800, 18: 0x0000F800,
            25: 0x03FF0000, 26: 0x03FF0000,
            33: 0x03FFF800, 35: 0x03FFF800, 37: 0x03FFF800, 42: 0x03FFF800}.get(fn, 0)
    return {1: 0x03E00000, 4: 0x03FF0000, 5: 0x03FF0000, 20: 0x03FF0000,
        9: 0x03FF0000, 12: 0x03FF0000, 15: 0x001F0000,
        35: 0x001F0000, 36: 0x001F0000, 43: 0x001F0000}.get(op, 0)


def owner_guards():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-cursor-updater'; output.mkdir(exist_ok=True)
    record, words = compile_candidate(root, output, 'guard-source')
    retail = struct.unpack_from('>98I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    assert (record['body_words'], record['frame'], record['differences']) == (98, 0, 46)
    assert record['relocations'] == {0x18: [('R_MIPS_HI16', 'D_800BE9E4')],
        0x1C: [('R_MIPS_LO16', 'D_800BE9E4')], 0x34: [('R_MIPS_HI16', 'D_80090B64')],
        0x3C: [('R_MIPS_LO16', 'D_80090B64')]}
    raw, functions, _ = parse_object(output / 'guard-source.o')
    raw = struct.unpack_from('>98I', raw, functions[FUNCTION]['value'])
    rows = []
    for i, (a, b) in enumerate(zip(words, retail)):
        assert a & ~register_mask(a) == b & ~register_mask(a), hex(i * 4)
        if a == b:
            continue
        assert i * 4 not in record['relocations']
        rows.append(dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % (i * 4),
            expected='0x%08X' % raw[i], replacement='0x%08X' % b,
            expected_relocations='-', replacement_relocations='-',
            note='Normalize cursor updater closed temporary register allocation and commutative add order',
            insert_after='', insert_after_relocations='', omit='false'))
    return rows


def main():
    root=Path(__file__).resolve().parents[2]
    output=root/'conker/build/game-cursor-updater';output.mkdir(exist_ok=True)
    records=[]
    for name,body in candidates():
        record,_=compile_candidate(root,output,name,body)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for profile in PROFILES:
        record,_=compile_candidate(root,output,'selected-'+profile,SELECTED,profile)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for name,body in loop_candidates():
        record,_=compile_candidate(root,output,name,body)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for name,body in flow_candidates():
        record,_=compile_candidate(root,output,name,body)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for name,body in shape_candidates():
        record,_=compile_candidate(root,output,name,body)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for name,body in compound_candidates():
        record,_=compile_candidate(root,output,name,body)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for name,body in signedness_candidates():
        record,_=compile_candidate(root,output,name,body)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for name,body in temporary_candidates():
        record,_=compile_candidate(root,output,name,body)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__=='__main__':main()
