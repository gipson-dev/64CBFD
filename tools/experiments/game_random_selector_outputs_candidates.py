"""Recover the seven-output RNG/selector wrapper without changing its retained helpers."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x1518E5D8, 0x1BBA88, 37
RANDOM, SELECTOR = 0x150ADA20, 0x151429E0
SYMBOLS = {'func_150ADA20': RANDOM, 'func_151429E0': SELECTOR}
PROFILES = {'o2g3': ('-O2','-g3'), 'o2': ('-O2',), 'o1g3': ('-O1','-g3'), 'o1': ('-O1',)}
DECLARATIONS = '''s32 func_150ADA20(void);
void func_151429E0(u8, u8 *, u8 *, u8 *);
'''
SELECTED = '''void func_1518E5D8(u8 *arg0, u8 *arg1, u8 *arg2, u8 *arg3, u8 *arg4, u8 *arg5, s16 *arg6) {
    s32 selector;

    if (func_150ADA20() & 1) {
        *arg1 |= 1;
    }
    *arg0 = 0x16;
    if (func_150ADA20() & 1) {
        selector = 3;
    } else {
        selector = 4;
    }
    func_151429E0(selector, arg2, arg3, arg4);
    *arg5 = 0xC8;
    *arg6 = 0x401;
}'''


def candidates():
    byte = SELECTED.replace('s32 selector;', 'u8 selector;')
    choice = '''    if (func_150ADA20() & 1) {
        selector = 3;
    } else {
        selector = 4;
    }'''
    return [('byte-selector',byte),
            ('ternary',byte.replace(choice,'    selector = (func_150ADA20() & 1) ? 3 : 4;')),
            ('wide-selector',SELECTED),
            ('direct-choice',byte.replace('    u8 selector;\n\n','').replace(choice+'\n','')
             .replace('func_151429E0(selector,','func_151429E0((func_150ADA20() & 1) ? 3 : 4,')),
            ('cached-first-random',byte.replace('    u8 selector;','    u8 selector;\n    s32 first = func_150ADA20();')
             .replace('if (func_150ADA20() & 1)','if (first & 1)',1)),
            ('volatile-first-pointers',byte.replace('u8 *arg0','u8 *volatile arg0')
             .replace('u8 *arg1','u8 *volatile arg1'))]


def compile_candidate(root,output,name,body=SELECTED,profile='o2g3'):
    source,obj,elf = (output / (name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n'+DECLARATIONS+body+'\n')
    command = ['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm','-signed',
               '-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
               '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
               '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',
               *PROFILES[profile],'-o',str(obj.relative_to(root)),str(source.relative_to(root))]
    result = subprocess.run(command,cwd=root,capture_output=True,text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'outputs.ld'
    script.write_text('SECTIONS { .text 0x1518E5D8 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e','func_1518E5D8',
                    *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()],'-o',str(elf),str(obj)],
                   check=True,capture_output=True,text=True)
    words = load_elf_functions(str(elf),'mips-linux-gnu-objdump')[0]['func_1518E5D8']
    end = max(i for i,word in enumerate(words) if word==0x03E00008)+2
    if any(words[end:]):
        raise ValueError('nonzero return tail')
    words = words[:end]
    retail = list(struct.unpack_from('>37I',(root / 'conker/conker.us.bin').read_bytes(),ROM))
    slot = words+[0]*max(0,WORDS-end)
    different = [(i*4,hex(a),hex(b)) for i,(a,b) in enumerate(zip(slot,retail)) if a!=b]
    frames = [(-(w&65535))&65535 for w in words if w&0xFFFF0000==0x27BD0000 and w&0x8000]
    return dict(name=name,profile=profile,body_words=end,frame=max(frames,default=0),
                differences=len(different)+max(0,end-WORDS),different_words=different,
                exact=slot==retail,diagnostics=diagnostics),words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-random-selector-outputs'
    output.mkdir(exist_ok=True)
    records = []
    for name,body in candidates():
        for profile in PROFILES:
            record,_ = compile_candidate(root,output,name+'-'+profile,body,profile)
            records.append(record)
            print(record['name'],record['body_words'],hex(record['frame']),record['differences'],flush=True)
    (output / 'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__ == '__main__':
    main()
