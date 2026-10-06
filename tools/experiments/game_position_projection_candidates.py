"""Screen the position projection and its typed caller without installing edits."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x1514182C, 0x16ECDC, 63
CALLER_ENTRY, CALLER_ROM, CALLER_WORDS = 0x15141928, 0x16EDD8, 18
PROFILES = {'o2g3': ('-O2','-g3'), 'o2': ('-O2',), 'o1g3': ('-O1','-g3'), 'o1': ('-O1',)}
SYMBOLS = {'func_150A8050': 0x150A8050, 'func_150A7960': 0x150A7960}
DECLARATIONS = '''#include "functions.h"
void func_150A7960(f32 *, f32, f32, f32, f32 *, f32 *, f32 *);
'''
PROTOTYPE = 'void func_1514182C(u8 *actor, f32 *origin, f32 height, f32 scale, f32 angleX, f32 angleZ);'
SELECTED = '''void func_1514182C(u8 *actor, f32 *origin, f32 height, f32 scale, f32 angleX, f32 angleZ) {
    f32 dx, dy, dz;
    f32 matrix[4][4];
    func_150A8050(matrix, angleX, 0.0f, angleZ);
    matrix[3][0] = origin[0];
    matrix[3][1] = origin[1];
    matrix[3][2] = origin[2];
    func_150A7960((f32 *)matrix, 0.0f, height, 0.0f,
        (f32 *)(actor + 0x34), (f32 *)(actor + 0x38), (f32 *)(actor + 0x3C));
    dx = (*(f32 *)(actor + 0x34) - origin[0]) * scale;
    dy = (*(f32 *)(actor + 0x38) - origin[1]) * scale;
    dz = (*(f32 *)(actor + 0x3C) - origin[2]) * scale;
    *(f32 *)(actor + 0x40) = *(f32 *)(actor + 0x34) + dx * 500.0f;
    *(f32 *)(actor + 0x44) = *(f32 *)(actor + 0x38) + dy * 500.0f;
    *(f32 *)(actor + 0x48) = *(f32 *)(actor + 0x3C) + dz * 500.0f;
}'''
CALLER = '''s32 func_15141928(void *arg0) {
    void *temp_v0 = *(void **)((u8 *)arg0 + 0x178);
    func_1514182C((u8 *)arg0, (f32 *)((u8 *)arg0 + 0x17C),
        *(f32 *)((u8 *)arg0 + 0x170), *(f32 *)((u8 *)arg0 + 0x174),
        *(f32 *)temp_v0, *(f32 *)((u8 *)temp_v0 + 8));
    return 1;
}'''


def candidates():
    records = []
    for matrix_scoped, products_scoped, product_first in itertools.product((False,True),repeat=3):
        body = SELECTED
        if matrix_scoped:
            body = body.replace('    f32 matrix[4][4];\n','').replace('    func_150A8050(',
                '    {\n    f32 matrix[4][4];\n    func_150A8050(',1).replace('    dx =','    }\n    dx =',1)
        if products_scoped:
            body = body.replace('    f32 dx, dy, dz;\n','').replace('    dx =','    {\n    f32 dx, dy, dz;\n    dx =',1)
            end = body.rfind('}')
            body = body[:end]+'    }\n'+body[end:]
        if product_first:
            for axis,index in zip(('x','y','z'),range(3)):
                position = '*(f32 *)(actor + 0x%X)'%(0x34+index*4)
                body = body.replace(position+' + d'+axis+' * 500.0f','d'+axis+' * 500.0f + '+position)
        records.append(('shape-%d%d%d'%(matrix_scoped,products_scoped,product_first),body))
    return records


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3', caller=False):
    entry,rom,length,function = (CALLER_ENTRY,CALLER_ROM,CALLER_WORDS,'func_15141928') if caller else (ENTRY,ROM,WORDS,'func_1514182C')
    declarations = DECLARATIONS+(PROTOTYPE+'\n' if caller else '')
    symbols = {'func_1514182C':ENTRY} if caller else SYMBOLS
    source,obj,elf = (output/(name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n'+declarations+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics: raise ValueError(diagnostics)
    script = output/(function+'.ld')
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n'%entry)
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',function,
                    *['--defsym=%s=0x%X'%item for item in symbols.items()],'-o',str(elf),str(obj)],
                   check=True,capture_output=True)
    words = load_elf_functions(str(elf),'mips-linux-gnu-objdump')[0][function]
    end = max(i for i,word in enumerate(words) if word==0x03E00008)+2
    assert not any(words[end:])
    slot = words[:end]+[0]*max(0,length-end)
    retail = list(struct.unpack_from('>%dI'%length,(root/'conker/conker.us.bin').read_bytes(),rom))
    differences = [(i*4,hex(a),hex(b)) for i,(a,b) in enumerate(zip(slot,retail)) if a!=b]
    frames = [(-word)&65535 for word in slot if word&0xFFFF0000==0x27BD0000 and word&0x8000]
    return dict(name=name,profile=profile,body_words=end,slot_words=len(slot),frame=frames[0] if frames else 0,
                differences=len(differences)+max(0,end-length),different_words=differences,
                exact=slot==retail,diagnostics=diagnostics),slot


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-position-projection'; output.mkdir(exist_ok=True)
    records = []
    for name,body in candidates():
        for profile in PROFILES:
            record,_ = compile_candidate(root,output,name+'-'+profile,body,profile)
            records.append(record)
            print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for profile in PROFILES:
        record,_ = compile_candidate(root,output,'caller-'+profile,CALLER,profile,caller=True)
        records.append(record)
        print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__=='__main__': main()
