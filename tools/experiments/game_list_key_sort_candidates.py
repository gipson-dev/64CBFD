"""Bound the list-key sorter's captured successor and live link repairs."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS, TABLE = 0x151406AC, 0x16DB5C, 73, 0x800DCE50
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
DECLARATIONS = '''typedef struct SortNode169510 {
    u8 prefix[4];
    struct SortNode169510 *prev;
    struct SortNode169510 *next;
    u8 padC[0xC];
    u8 kind;
    u8 pad19[7];
    s32 value;
    u8 tail[0xEC];
} SortNode169510;
extern u8 D_800DCE50[];
'''
SELECTED = '''s32 func_151406AC(s32 token, u32 column, u32 row, s16 bypass) {
    SortNode169510 dummy;
    SortNode169510 **slot;
    SortNode169510 *head;
    SortNode169510 *current;
    SortNode169510 *previous;
    SortNode169510 *next;
    SortNode169510 *temporary;
    s32 key;
    s32 otherKey;
    if (bypass != 0) {
        return token;
    }
    slot = (SortNode169510 **)(D_800DCE50 + row * 0x1A0 + column * 4);
    head = *slot;
    dummy.kind = 0;
    dummy.value = 0;
    dummy.next = head;
    head->prev = &dummy;
    if (head != NULL) {
        current = head->next;
        while (current != NULL) {
            previous = current->prev;
            temporary = current->next;
            next = temporary;
            key = (current->kind << 8) + (current->value >> 16);
            head = previous;
            while (head != NULL) {
                otherKey = (head->kind << 8) + (head->value >> 16);
                if (key >= otherKey) {
                    if (head != previous) {
                        previous->next = temporary;
                        temporary = current->next;
                        if (temporary != NULL) {
                            temporary->prev = current->prev;
                        }
                        temporary = head->next;
                        current->next = temporary;
                        if (temporary != NULL) {
                            temporary->prev = current;
                        }
                        current->prev = head;
                        head->next = current;
                    }
                    break;
                }
                head = head->prev;
            }
            current = next;
        }
    }
    *slot = dummy.next;
    dummy.next->prev = NULL;
    return token;
}'''


def candidates():
    inner = SELECTED.replace('            head = previous;\n            while (head != NULL) {',
        '            for (head = previous; head != NULL; head = head->prev) {').replace('                head = head->prev;\n','')
    outer = SELECTED.replace('        current = head->next;\n        while (current != NULL) {',
        '        for (current = head->next; current != NULL; current = next) {').replace('            current = next;\n','')
    scoped = SELECTED
    for declaration in ('    SortNode169510 *previous;', '    SortNode169510 *next;',
                        '    SortNode169510 *temporary;', '    s32 key;', '    s32 otherKey;'):
        scoped = scoped.replace(declaration+'\n','').replace('        while (current != NULL) {',
            '        while (current != NULL) {\n        '+declaration)
    next_local = SELECTED.replace('    SortNode169510 *next;\n','').replace('        while (current != NULL) {',
        '        while (current != NULL) {\n            SortNode169510 *next;')
    return [('selected',SELECTED,DECLARATIONS),('inner-for',inner,DECLARATIONS),
            ('outer-for',outer,DECLARATIONS),('loop-local',scoped,DECLARATIONS),
            ('next-local',next_local,DECLARATIONS),('small-node',SELECTED,DECLARATIONS.replace('0xEC','0x0C'))]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3', declarations=DECLARATIONS):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n'+declarations+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:raise ValueError(diagnostics)
    script = output/'list-sort.ld'
    script.write_text('SECTIONS { .text 0x151406AC : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e','func_151406AC',
        '--defsym=D_800DCE50=0x800DCE50','-o',str(elf),str(obj)],check=True,capture_output=True)
    words = load_elf_functions(str(elf),'mips-linux-gnu-objdump')[0]['func_151406AC']
    end = max(i for i,w in enumerate(words) if w==0x03E00008)+2
    assert not any(words[end:]);words=words[:end]
    retail = list(struct.unpack_from('>73I',(root/'conker/conker.us.bin').read_bytes(),ROM))
    padded = words+[0]*max(0,WORDS-end)
    differences = [(i*4,hex(a),hex(b)) for i,(a,b) in enumerate(zip(padded,retail)) if a!=b]
    frame = [(-w)&65535 for w in words if w&0xFFFF0000==0x27BD0000 and w&0x8000]
    return dict(name=name,profile=profile,body_words=end,frame=frame[0] if frame else 0,
        differences=len(differences)+max(0,end-WORDS),different_words=differences,
        exact=padded==retail,diagnostics=diagnostics),words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-list-key-sort';output.mkdir(exist_ok=True)
    records = []
    for name,body,declarations in candidates():
        for profile in PROFILES:
            record,_ = compile_candidate(root,output,name+'-'+profile,body,profile,declarations)
            records.append(record)
            print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(records[0]['different_words']))


if __name__=='__main__':
    main()
