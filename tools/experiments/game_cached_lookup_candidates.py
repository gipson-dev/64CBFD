"""Cached resource-lookup source and stack-layout screening at retail addresses."""

import json
import re
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_cache_installer_candidates import LAYOUT
from tools.match_progress import load_elf_functions


BASELINE = '''s32 func_1502AC88(u32 arg0, s32 arg1, u32 *arg2) {
    AssetTableCache57FA0 saved;
    u8 storage[0x40];
    u8 *aligned;
    u32 *pairs;
    u32 address;
    u32 offset;
    u32 i;
    u32 j;

    address = (arg0 + (u32)arg1 * 8) | 0x80000000;
    for (i = 0; i < 16; i++) {
        if (D_800C3D68[i].address == address) {
            saved = D_800C3D68[i];
            for (j = i; j < 15; j++) {
                D_800C3D68[j] = D_800C3D68[j + 1];
            }
            D_800C3D68[15] = saved;
            D_800C3D68[15].generation = D_800C3D60;
            *arg2 = D_800C3D68[15].descriptor;
            return D_800C3D68[15].offset;
        }
    }
    D_800C3D60++;
    aligned = (u8 *)(((u32)storage + 15) & ~0xF);
    func_10004514(address & 0x7FFFFFF0, aligned, ((address & 0xE) + 0x1F) & ~0xF, 1);
    pairs = (u32 *)(aligned + (address & 0xF));
    offset = pairs[0];
    *arg2 = pairs[1];
    func_1502AB04(2, pairs, D_800C3D60, address);
    return offset;
}'''


def candidates():
    split=BASELINE.replace('    address = (arg0 + (u32)arg1 * 8) | 0x80000000;',
        '    address = arg0;\n    address += (u32)arg1 * 8;\n    address |= 0x80000000;')
    forms=[('baseline',BASELINE),('split-address',split)]
    declarations={'saved':'AssetTableCache57FA0 saved;', 'storage':'u8 storage[0x40];',
                  'aligned':'u8 *aligned;', 'pairs':'u32 *pairs;', 'address':'u32 address;',
                  'offset':'u32 offset;', 'i':'u32 i;', 'j':'u32 j;'}
    original='\n'.join('    '+v for v in declarations.values())
    orders=(('storage','saved','aligned','pairs','address','offset','i','j'),
            ('storage','aligned','offset','address','i','j','saved','pairs'),
            ('storage','pairs','offset','address','i','j','saved','aligned'),
            ('storage','offset','aligned','pairs','address','saved','i','j'),
            ('storage','address','offset','i','j','aligned','saved','pairs'),
            ('storage','i','offset','j','address','pairs','saved','aligned'),
            ('i','j','address','storage','aligned','pairs','offset','saved'),
            ('aligned','saved','offset','storage','pairs','address','i','j'))
    for index,order in enumerate(orders):
        forms.append(('layout-'+str(index),split.replace(original,
            '\n'.join('    '+declarations[k] for k in order))))
    for name,body in list(forms):
        forms.append((name+'-align8',body.replace('(u32)storage + 15','(u32)storage + 8')))
    for name,body in list(forms):
        param=body.replace('(u32 arg0,','(u32 address,').replace('    u32 address;\n','')
        param=param.replace('    address = arg0;\n','')
        param=param.replace('    address = (arg0 + (u32)arg1 * 8) | 0x80000000;',
                            '    address += (u32)arg1 * 8;\n    address |= 0x80000000;')
        forms.append(('parameter-'+name,param))
    base=dict(forms)['parameter-layout-1']
    base=base.replace('    AssetTableCache57FA0 saved;\n    u32 *pairs;',
                      '    u32 *pairs;\n    AssetTableCache57FA0 saved;')
    forms.append(('ordered-locals',base))
    for label,before,after in (
            ('signed-offset','    u32 offset;','    s32 offset;'),
            ('integer-pair-sum','pairs = (u32 *)(aligned + (address & 0xF));',
                                 'pairs = (u32 *)((u32)aligned + (address & 0xF));'),
            ('register-aligned','    u8 *aligned;','    register u8 *aligned;'),
            ('register-pairs','    u32 *pairs;','    register u32 *pairs;'),
            ('preincrement-clock','    D_800C3D60++;','    ++D_800C3D60;'),
            ('clock-add','    D_800C3D60++;','    D_800C3D60 += 1;'),
            ('masked-shift','(u32)arg1 * 8','((u32)arg1 << 3)'),
            ('signed-shift','(u32)arg1 * 8','(arg1 << 3)'),
            ('array-align8','(u32)storage + 15','(u32)storage + 8'),
            ('signed-pairs','    u32 *pairs;', '    s32 *pairs;')):
        candidate=base.replace(before,after)
        if label=='signed-pairs':
            candidate=candidate.replace('pairs = (u32 *)','pairs = (s32 *)')
            candidate=candidate.replace('func_1502AB04(2, pairs,','func_1502AB04(2, (u32 *)pairs,')
        forms.append(('ordered-'+label,candidate))
    number=base.replace('    u8 *aligned;', '    u32 aligned;')
    number=number.replace('aligned = (u8 *)(', 'aligned = (')
    number=number.replace('0x7FFFFFF0, aligned,','0x7FFFFFF0, (void *)aligned,')
    forms.append(('ordered-integer-aligned',number))
    for label,body in list(forms):
        if label.startswith('ordered-') and not label.endswith('align8'):
            forms.append((label+'-align8',body.replace('(u32)storage + 15','(u32)storage + 8')))
    for label,before,after in (
            ('aligned-advance','pairs = (u32 *)(aligned + (address & 0xF));',
                               'aligned += address & 0xF;\n    pairs = (u32 *)aligned;'),
            ('pair-advance','pairs = (u32 *)(aligned + (address & 0xF));',
                            'pairs = (u32 *)aligned;\n    pairs = (u32 *)((u8 *)pairs + (address & 0xF));'),
            ('dereference-offset','offset = pairs[0];','offset = *pairs;'),
            ('dereference-output','*arg2 = pairs[1];','*arg2 = *(pairs + 1);'),
            ('signed-output','*arg2 = pairs[1];','*(s32 *)arg2 = (s32)pairs[1];'),
            ('sum-first','aligned + (address & 0xF)','(address & 0xF) + aligned'),
            ('buffer-u32','u8 storage[0x40];','u32 storage[16];'),
            ('buffer-u64','u8 storage[0x40];','u64 storage[8];')):
        forms.append(('expression-'+label,base.replace(before,after)))
    return forms


def compile_candidate(root, output, name, source):
    conker=root/'conker'
    path=output/(name+'.c')
    obj,elf=path.with_suffix('.o'),path.with_suffix('.elf')
    prefix=('typedef int s32; typedef unsigned int u32; typedef unsigned char u8;\n'
            'typedef unsigned long long u64;\n'+LAYOUT+'\n'
            'extern AssetTableCache57FA0 D_800C3D68[16]; extern u32 D_800C3D60;\n'
            's32 func_10004514(u32,void *,u32,s32);\n'
            'void func_1502AB04(s32,u32 *,u32,u32);\n')
    path.write_text(prefix+source+'\n')
    result=subprocess.run([str(root/'ido/ido5.3_recomp/cc'),'-c','-32','-G','0',
        '-Xfullwarn','-Xcpluscomm','-signed','-nostdinc','-non_shared','-Wab,-r4300_mul',
        '-mips2','-o32','-O2','-g3','-o',str(obj.relative_to(conker)),
        str(path.relative_to(conker))],cwd=conker,capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script=output/'slot.ld'
    script.write_text('SECTIONS { .text 0x1502AC88 : SUBALIGN(4) { *(.text) } }\n')
    targets={'D_800C3D68':0x800C3D68,'D_800C3D60':0x800C3D60,
             'func_10004514':0x10004514,'func_1502AB04':0x1502AB04}
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),
        '-e','func_1502AC88',*(f'--defsym={k}=0x{v:X}' for k,v in targets.items()),
        '-o',str(elf),str(obj)],check=True,capture_output=True)
    functions,_,_=load_elf_functions(str(elf),'mips-linux-gnu-objdump')
    words=functions['func_1502AC88']
    size=max(i for i,word in enumerate(words) if word==0x03E00008)+2
    slot=words[:size]+[0]*max(0,159-size)
    retail=struct.unpack_from('>159I',(conker/'conker.us.bin').read_bytes(),0x58138)
    differences=[(i*4,f'{a:08X}',f'{b:08X}') for i,(a,b) in enumerate(zip(slot,retail)) if a!=b]
    record=dict(name=name,body_words=size,
                frame=(-words[0])&0xFFFF if words[0]>>16==0x27BD else 0,
                real_differences=len(differences)+max(0,size-159),differences=differences,
                stack_addresses=[(i*4,w&0xFFFF) for i,w in enumerate(words[:size])
                    if w>>26==9 and w>>21&31==29 and w>>16&31!=29],
                diagnostics=result.stdout+result.stderr)
    return record,slot


def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix',default='')
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[2]
    production=re.search(r's32 func_1502AC88\([^;{}]+\) \{\n.*?\n\}',
        (root/'conker/src/game_57FA0.c').read_text(),re.S).group(0)
    assert production==dict(candidates())['ordered-locals']
    output=root/'conker/build/game-cached-lookup'
    output.mkdir(exist_ok=True)
    records=[]
    for name,source in candidates():
        if not name.startswith(args.prefix):
            continue
        record,_=compile_candidate(root,output,name,source)
        records.append(record)
        print(name,record['body_words'],hex(record['frame']),record['real_differences'],
              [(hex(a),hex(b)) for a,b in record['stack_addresses']],flush=True)
    report='screen.json' if not args.prefix else 'screen-'+args.prefix+'.json'
    (output/report).write_text(json.dumps(records,indent=2)+'\n')


if __name__=='__main__':
    main()
