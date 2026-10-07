"""Actor health/callback gates and the original partially initialized packet."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15143E94, 0x171344, 98
FUNCTION = 'func_15143E94'
SYMBOLS = dict(D_80082FA0=0x80082FA0, D_800CC2D0=0x800CC2D0,
    D_800BE9E8=0x800BE9E8, D_800DBFF0=0x800DBFF0, func_150A29C8=0x150A29C8,
    func_1512D748=0x1512D748, func_150ADA20=0x150ADA20, func_151D8868=0x151D8868)
DECLARATIONS = '''typedef struct {
    u8 kind, pad1;
    s16 duration;
    u8 count, mode;
    s8 index;
    u8 pad7;
} GameGatedPacket;
typedef struct { u8 pad0[0x1CA]; u8 health; u8 pad1CB[0x161]; } GameGatedActor;
typedef struct { u8 bytes[0x9A0]; } GameGatedContext;
extern s32 D_80082FA0, D_800BE9E8;
extern GameGatedActor D_800CC2D0[];
extern GameGatedContext *D_800DBFF0;
s32 func_150A29C8(s32, s32);
void func_1512D748(GameGatedContext *, s32, s32);
s32 func_150ADA20(void);
void *func_151D8868(void *, s32, s32, s32);
'''
PROTOTYPE = 'u8 func_15143E94(s32 command, s32 flags);'
BASELINE = '''u8 func_15143E94(s32 command, s32 flags) {
    GameGatedPacket packet;
    u8 result = 0;
    s8 count;
    s8 index;
    s32 active;
    s32 ready;

    count = D_80082FA0 + 1;
    index = 0;
    active = 0;
    while (index < count && active == 0) {
        if (D_800CC2D0[index].health != 0) {
            active = 1;
        } else {
            index++;
        }
    }
    if (active != 0) {
        index = 0;
        ready = 0;
        while (index < count && ready == 0) {
            if (func_150A29C8(index, flags) == 0) {
                ready = 1;
            } else {
                index++;
            }
        }
        if (ready != 0) {
            func_1512D748(&D_800DBFF0[D_800BE9E8], command, 1);
            packet.kind = 1;
            packet.duration = (func_150ADA20() & 0xF) + 20;
            packet.count = (func_150ADA20() & 3) + 4;
            packet.index = -1;
            packet.mode = 1;
            func_151D8868(&packet, 0, 255, 0);
            result = 1;
        }
    }
    return result;
}'''
SELECTED = BASELINE.replace('    GameGatedPacket packet;\n    u8 result = 0;\n    s8 count;\n    s8 index;\n    s32 active;\n    s32 ready;',
    '    u8 result = 0;\n    s8 count;\n    s8 index;\n    s16 active;\n    s16 ready;\n    GameGatedPacket packet;').replace(
    'index < count && active == 0', 'active == 0 && index < count').replace(
    'index < count && ready == 0', 'ready == 0 && index < count').replace(
    'D_80082FA0 + 1', '(u32)D_80082FA0 + 1')
OWNER_INCLUDE = '''#define func_150A29C8 func_150A29C8_legacy_narrow_signature
#include "functions.h"
#undef func_150A29C8'''
OWNER_DECLARATIONS = DECLARATIONS[:DECLARATIONS.index('typedef struct { u8 pad0')] + '''s32 func_150A29C8(s32, s32);
void *func_151D8868(void *, s32, s32, s32);
'''


def storage_candidates():
    old = '    u8 result = 0;\n    s8 count;\n    s8 index;\n    s16 active;\n    s16 ready;\n    GameGatedPacket packet;'
    groups = ('    GameGatedPacket packet;', '    u8 result = 0;',
        '    s8 count;\n    s8 index;', '    s16 active;\n    s16 ready;')
    for i, order in enumerate(itertools.permutations(groups)):
        for late in (False, True):
            body = SELECTED.replace(old, '\n'.join(order))
            if late:
                body = body.replace('u8 result = 0;', 'u8 result;').replace(
                    '    count = ', '    result = 0;\n    count = ', 1)
            yield 'short-%02d-%d' % (i, late), body


def candidates():
    for gate_order, local_order, ready_type, flags_type in itertools.product((False,True),repeat=4):
        body=BASELINE
        if gate_order:
            body=body.replace('index < count && active == 0','active == 0 && index < count').replace(
                'index < count && ready == 0','ready == 0 && index < count')
        if local_order:
            body=body.replace('    GameGatedPacket packet;\n    u8 result = 0;',
                '    u8 result = 0;\n    GameGatedPacket packet;')
        if ready_type: body=body.replace('s32 active;', 'u8 active;').replace('s32 ready;', 'u8 ready;')
        if flags_type: body=body.replace('s32 flags)', 'u16 flags)')
        yield 'g%d-l%d-r%d-f%d'%(gate_order,local_order,ready_type,flags_type),body


def compile_candidate(root,output,name,body=SELECTED,profile='o2g3',declarations=DECLARATIONS):
    source,obj,elf=(output/(name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n'+declarations+body+'\n')
    result=subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    diagnostics=result.stdout+result.stderr
    if result.returncode or diagnostics:raise ValueError(diagnostics)
    script=output/'packet.ld'
    script.write_text('SECTIONS { .text 0x15143E94 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',FUNCTION,
        *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()],'-o',str(elf),str(obj)],check=True,capture_output=True)
    _,functions,relocations=parse_object(obj)
    meta=functions[FUNCTION];pools=sections(elf)
    words=list(struct.unpack_from('>%dI'%(meta['size']//4),pools['.text'][1],meta['value']))
    end=max(i for i,w in enumerate(words) if w==0x03E00008)+2
    assert not any(words[end:]);words=words[:end]
    retail=struct.unpack_from('>98I',(root/'conker/conker.us.bin').read_bytes(),ROM)
    frames=[(-word)&65535 for word in words if word&0xFFFF0000==0x27BD0000 and word&0x8000]
    frame=frames[0] if frames else 0
    return dict(name=name,profile=profile,body_words=end,frame=frame,diagnostics=diagnostics,
        relocations=relocations,differences=sum(a!=b for a,b in itertools.zip_longest(words,retail,fillvalue=0))),words


def schedule_tokens(words):
    """Compare operations with branch PCs normalized to their actual destination."""
    result = []
    for i in range(8, 20):
        word = words[i]
        if word >> 26 == 6:
            offset = word & 65535
            offset = offset if offset < 32768 else offset - 65536
            result.append(('blez', word >> 21 & 31, ENTRY + i * 4 + 4 + offset * 4))
        else:
            result.append(('word', word))
    return sorted(result)


def owner_guards():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-gated-packet'; output.mkdir(exist_ok=True)
    record, words = compile_candidate(root, output, 'guard-source')
    retail = list(struct.unpack_from('>98I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    assert (record['body_words'], record['frame'], record['differences']) == (98, 56, 11)
    assert schedule_tokens(words) == schedule_tokens(retail)
    text, functions, relocs = parse_object(output / 'guard-source.o')
    start = functions[FUNCTION]['value']
    raw = list(struct.unpack_from('>98I', text, start))
    old_rel = {o - start: r for o, r in relocs.items()}
    new_rel = {0x24: [('R_MIPS_HI16', 'D_80082FA0')], 0x28: [('R_MIPS_LO16', 'D_80082FA0')],
        0x48: [('R_MIPS_HI16', 'D_800CC2D0')], 0x4C: [('R_MIPS_LO16', 'D_800CC2D0')]}
    rows = []
    for i, (a, b) in enumerate(zip(words, retail)):
        if a == b:
            continue
        offset = i * 4
        assert 0x20 <= offset <= 0x4C
        replacement = b & 0xFFFF0000 if offset in new_rel else b
        encode = lambda rs: ';'.join('%s:%s' % r for r in rs) or '-'
        rows.append(dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % offset,
            expected='0x%08X' % raw[i], replacement='0x%08X' % replacement,
            expected_relocations=encode(old_rel.get(offset, [])), replacement_relocations=encode(new_rel.get(offset, [])),
            note='Normalize actor gated packet opening initialization schedule', insert_after='',
            insert_after_relocations='', omit='false'))
    return rows


def main():
    root=Path(__file__).resolve().parents[2]
    output=root/'conker/build/game-actor-gated-packet';output.mkdir(exist_ok=True)
    records=[]
    for name,body in candidates():
        for profile in PROFILES:
            record,_=compile_candidate(root,output,name+'-'+profile,body,profile)
            records.append(record)
            print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for name,body in storage_candidates():
        record,_=compile_candidate(root,output,name,body)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for profile in PROFILES:
        record,_=compile_candidate(root,output,'selected-'+profile,SELECTED,profile)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__=='__main__':main()
