"""Resource cache-installer source screening at fixed retail addresses."""

import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


LAYOUT = '''typedef struct AssetTableCache57FA0 {
    u32 address;
    u32 generation;
    u32 offset;
    u32 descriptor;
} AssetTableCache57FA0;'''

BASELINE = '''void func_1502AB04(s32 count, u32 *pairs, u32 generation, u32 address) {
    u32 i;

    if (count != 0) {
        bcopy(&D_800C3D68[count], D_800C3D68, (16 - count) * 16);
    }
    for (i = 16 - (u32)count; i < 16; i++) {
        D_800C3D68[i].offset = pairs[0];
        D_800C3D68[i].descriptor = pairs[1];
        D_800C3D68[i].address = address;
        D_800C3D68[i].generation = generation;
        pairs += 2;
        address += 8;
    }
}'''


def candidates():
    forms = [('baseline', BASELINE)]
    local_count=BASELINE.replace('(s32 count,','(s32 arg0,')
    local_count=local_count.replace('    u32 i;', '    s32 count;\n    u32 i;')
    local_count=local_count.replace('    if (count != 0)', '    count = arg0;\n    if (count != 0)')
    forms.append(('scalar-local-count',local_count))
    post = BASELINE.replace('pairs[0]', '*pairs++').replace('pairs[1]', '*pairs++')
    post = post.replace('        pairs += 2;\n', '')
    forms.append(('post-pairs', post))
    for tag in ('Pair', 'AssetTablePair57FA0', 'struct124'):
        decl = ('    typedef struct '+tag+' {\n'
                '        u32 offset;\n        u32 descriptor;\n    } '+tag+';\n')
        copy = BASELINE.replace('    u32 i;', decl+'    u32 i;')
        copy = copy.replace('        D_800C3D68[i].offset = pairs[0];\n'
                            '        D_800C3D68[i].descriptor = pairs[1];',
                            '        *('+tag+' *)&D_800C3D68[i].offset = *('+tag+' *)pairs;')
        forms.append(('pair-copy-'+tag,copy))
    for name,base in list(forms):
        forms.append((name+'-register-count',base.replace('(s32 count,','(register s32 count,')))
    for name,base in list(forms):
        for label,before,after in (
                ('signed-index','    u32 i;','    s32 i;'),
                ('register-index','    u32 i;','    register u32 i;'),
                ('copy-size','(16 - count) * 16','256 - count * 16'),
                ('unsigned-count','s32 count','u32 count'),
                ('no-index-cast','16 - (u32)count','16 - count')):
            forms.append((name+'-'+label,base.replace(before,after)))
    for name,base in list(forms):
        if '-register-count' in name or 'AssetTablePair57FA0' not in name or name.endswith('signed-index') or name.endswith('unsigned-count'):
            continue
        for label,kind in (('local-count','s32'),('register-local-count','register s32'),
                           ('unsigned-local-count','u32')):
            local=base.replace('(s32 count,','(s32 arg0,')
            local=re.sub(r'    ((?:register )?u32 i;)', '    '+kind+' count;\n    \\1', local)
            local=local.replace('    if (count != 0)', '    count = arg0;\n    if (count != 0)')
            forms.append((name+'-'+label,local))
        swapped=base.replace('        D_800C3D68[i].address = address;\n'
                             '        D_800C3D68[i].generation = generation;',
                             '        D_800C3D68[i].generation = generation;\n'
                             '        D_800C3D68[i].address = address;')
        forms.append((name+'-generation-first',swapped))
    base=dict(forms)['pair-copy-AssetTablePair57FA0-local-count']
    for label,before,after in (
            ('generation-first', '        D_800C3D68[i].address = address;\n'
                                 '        D_800C3D68[i].generation = generation;',
                                 '        D_800C3D68[i].generation = generation;\n'
                                 '        D_800C3D68[i].address = address;'),
            ('advance-address-first','        pairs += 2;\n        address += 8;',
                                     '        address += 8;\n        pairs += 2;'),
            ('advance-address-middle','        D_800C3D68[i].address = address;',
                                      '        D_800C3D68[i].address = address;\n        address += 8;'),
            ('post-address','        D_800C3D68[i].address = address;',
                            '        D_800C3D68[i].address = (address += 8) - 8;'),
            ('register-local-index','    u32 i;', '    register u32 i;'),
            ('count-before-type','    u32 i;','    u32 i;'),
            ('unsigned-index-first','    s32 count;\n    u32 i;', '    u32 i;\n    s32 count;')):
        candidate=base.replace(before,after)
        if label in ('advance-address-middle','post-address'):
            candidate=candidate.replace('        pairs += 2;\n        address += 8;', '        pairs += 2;')
        if label=='count-before-type':
            candidate=candidate.replace('    s32 count;\n','')
            candidate=candidate.replace('    typedef struct', '    s32 count;\n    typedef struct')
        forms.append(('local-'+label,candidate))
    for tag in ('Pair','struct124','ResourceDescriptor','Entry'):
        forms.append(('local-tag-'+tag,base.replace('AssetTablePair57FA0',tag)))
    typed=base.replace('    u32 i;', '    AssetTablePair57FA0 *input;\n    u32 i;')
    typed=typed.replace('    count = arg0;', '    input = (AssetTablePair57FA0 *)pairs;\n    count = arg0;')
    typed=typed.replace('*(AssetTablePair57FA0 *)pairs', '*input')
    typed=typed.replace('        pairs += 2;', '        input++;')
    forms.append(('local-typed-input',typed))
    entry=base.replace('    u32 i;', '    AssetTableCache57FA0 *entry;\n    u32 i;')
    entry=entry.replace('        *(AssetTablePair57FA0 *)&D_800C3D68[i].offset',
                        '        entry = &D_800C3D68[i];\n        *(AssetTablePair57FA0 *)&entry->offset')
    entry=entry.replace('D_800C3D68[i].address', 'entry->address').replace('D_800C3D68[i].generation','entry->generation')
    forms.append(('local-entry-view',entry))
    base=dict(forms)['local-generation-first']
    word=base.replace('        u32 offset;\n        u32 descriptor;', '        u32 value;')
    word=word.replace('        *(AssetTablePair57FA0 *)&D_800C3D68[i].offset = *(AssetTablePair57FA0 *)pairs;',
        '        *(AssetTablePair57FA0 *)&D_800C3D68[i].offset = *(AssetTablePair57FA0 *)pairs;\n'
        '        D_800C3D68[i].descriptor = pairs[1];')
    forms.append(('word-offset-scalar-descriptor',word))
    selected=word.replace('AssetTablePair57FA0','AssetTableWord57FA0')
    selected=selected.replace('        *(AssetTableWord57FA0 *)&D_800C3D68[i].offset =',
        '        /* Keep pair reads sequential when input overlaps the cache. */\n'
        '        *(AssetTableWord57FA0 *)&D_800C3D68[i].offset =')
    forms.append(('word-selected',selected))
    both=word.replace('        D_800C3D68[i].descriptor = pairs[1];',
                      '        *(AssetTablePair57FA0 *)&D_800C3D68[i].descriptor = *(AssetTablePair57FA0 *)&pairs[1];')
    forms.append(('word-both',both))
    cursor=word.replace('    u32 i;', '    AssetTableCache57FA0 *entry;\n    u32 i;')
    cursor=cursor.replace('        *(AssetTablePair57FA0 *)&D_800C3D68[i].offset',
                         '        entry = &D_800C3D68[i];\n        *(AssetTablePair57FA0 *)&entry->offset')
    cursor=cursor.replace('D_800C3D68[i].descriptor','entry->descriptor')
    cursor=cursor.replace('D_800C3D68[i].generation','entry->generation').replace('D_800C3D68[i].address','entry->address')
    forms.append(('word-entry-view',cursor))
    fields=base.replace('        *(AssetTablePair57FA0 *)&D_800C3D68[i].offset = *(AssetTablePair57FA0 *)pairs;',
                       '        ((AssetTablePair57FA0 *)&D_800C3D68[i].offset)->offset = pairs[0];\n'
                       '        ((AssetTablePair57FA0 *)&D_800C3D68[i].offset)->descriptor = pairs[1];')
    forms.append(('word-two-pair-fields',fields))
    mixed=word.replace('        D_800C3D68[i].descriptor = pairs[1];',
                      '        ((u32 *)&D_800C3D68[i].offset)[1] = pairs[1];')
    forms.append(('word-descriptor-offset-base',mixed))
    for label,kind,first,second in (
            ('u32','u32 *','*(AssetTablePair57FA0 *)destination','destination[1]'),
            ('word','AssetTablePair57FA0 *','*destination','((u32 *)destination)[1]')):
        local=word.replace('    u32 i;', '    '+kind+'destination;\n    u32 i;')
        local=local.replace('        *(AssetTablePair57FA0 *)&D_800C3D68[i].offset =',
            '        destination = ('+kind+')&D_800C3D68[i].offset;\n        '+first+' =')
        local=local.replace('D_800C3D68[i].descriptor',second)
        forms.append(('word-local-destination-'+label,local))
        volatile=local.replace('destination[1] = pairs[1]', 'destination[1] = *(volatile u32 *)&pairs[1]')
        forms.append(('word-local-destination-'+label+'-volatile-second',volatile))
    captured=word.replace('    u32 i;', '    u32 descriptor;\n    u32 i;')
    captured=captured.replace('        D_800C3D68[i].descriptor = pairs[1];',
                            '        descriptor = pairs[1];\n        D_800C3D68[i].descriptor = descriptor;')
    forms.append(('word-capture-descriptor',captured))
    for name,base in (('word',word),('scalar',BASELINE.replace('(s32 count,','(s32 arg0,')
            .replace('    u32 i;', '    s32 count;\n    u32 i;')
            .replace('    if (count != 0)', '    count = arg0;\n    if (count != 0)'))):
        for mask in range(1,8):
            body=base
            for bit,field in enumerate(('descriptor','address','generation')):
                if mask & (1<<bit):
                    body=body.replace('D_800C3D68[i].'+field, '*(volatile u32 *)&D_800C3D68[i].'+field)
            forms.append(('volatile-'+name+'-'+str(mask),body))
    alternate=word.replace('        D_800C3D68[i].generation = generation;\n'
                           '        D_800C3D68[i].address = address;',
                           '        D_800C3D68[i].address = address;\n'
                           '        D_800C3D68[i].generation = generation;')
    forms.append(('word-address-first',alternate))
    for label,before,after in (
            ('descriptor-pointer','    u32 i;', '    u32 *descriptor;\n    u32 i;'),
            ('descriptor-pointer-before-count','    s32 count;', '    u32 *descriptor;\n    s32 count;')):
        body=word.replace(before,after)
        body=body.replace('        D_800C3D68[i].descriptor = pairs[1];',
                          '        descriptor = &D_800C3D68[i].descriptor;\n        *descriptor = pairs[1];')
        forms.append(('word-'+label,body))
    return forms


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name+'.c')
    obj,elf = path.with_suffix('.o'),path.with_suffix('.elf')
    prefix = ('typedef int s32; typedef unsigned int u32;\n'+LAYOUT+'\n'
              'extern AssetTableCache57FA0 D_800C3D68[16];\n'
              'void bcopy(const void *,void *,int);\n')
    path.write_text(prefix+source+'\n')
    result = subprocess.run([str(root/'ido/ido5.3_recomp/cc'),'-c','-32','-G','0',
        '-Xfullwarn','-Xcpluscomm','-signed','-nostdinc','-non_shared','-Wab,-r4300_mul',
        '-mips2','-o32','-O2','-g3','-o',str(obj.relative_to(conker)),
        str(path.relative_to(conker))],cwd=conker,capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output/'slot.ld'
    script.write_text('SECTIONS { .text 0x1502AB04 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),
        '-e','func_1502AB04','--defsym=D_800C3D68=0x800C3D68',
        '--defsym=bcopy=0x10023A10','-o',str(elf),str(obj)],check=True,capture_output=True)
    functions,_,_=load_elf_functions(str(elf),'mips-linux-gnu-objdump')
    words=functions['func_1502AB04']
    size=max(i for i,word in enumerate(words) if word==0x03E00008)+2
    slot=words[:size]+[0]*max(0,97-size)
    retail=struct.unpack_from('>97I',(conker/'conker.us.bin').read_bytes(),0x57FB4)
    differences=[(i*4,f'{a:08X}',f'{b:08X}') for i,(a,b) in enumerate(zip(slot,retail)) if a!=b]
    record=dict(name=name,body_words=size,
                frame=(-words[0])&0xFFFF if words[0]>>16==0x27BD else 0,
                real_differences=len(differences)+max(0,size-97),differences=differences,
                diagnostics=result.stdout+result.stderr)
    return record,slot


def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix',default='')
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[2]
    production=(root/'conker/src/game_57FA0.c').read_text()
    assert re.search(r'void func_1502AB04\([^;{}]+\) \{\n.*?\n\}',production,re.S).group(0)==dict(candidates())['word-selected']
    assert re.search(r'typedef struct AssetTableCache57FA0 \{.*?\} AssetTableCache57FA0;',production,re.S).group(0)==LAYOUT
    output=root/'conker/build/game-cache-installer'
    output.mkdir(exist_ok=True)
    records=[]
    for name,source in candidates():
        if not name.startswith(args.prefix):
            continue
        record,_=compile_candidate(root,output,name,source)
        records.append(record)
        print(name,record['body_words'],hex(record['frame']),record['real_differences'],flush=True)
    report='screen.json' if not args.prefix else 'screen-'+args.prefix+'.json'
    (output/report).write_text(json.dumps(records,indent=2)+'\n')


if __name__=='__main__':
    main()
