"""Recover the signed-coordinate actor-to-position-queue wrapper."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS, HELPER = 0x1517D5FC, 0x1AAAAC, 37, 0x1517D578
SYMBOLS = {'D_800DBFF0': 0x800DBFF0, 'D_800DDD1C': 0x800DDD1C, 'func_1517D578': HELPER}
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
DECLARATIONS = '''extern struct108 *D_800DBFF0;
extern u8 D_800DDD1C;
void func_1517D578(s16, s16, s16, f32, s32, s32, u8);
'''
SELECTED = '''void func_1517D5FC(s16 arg0, s16 arg1, s16 arg2, s32 arg3, s32 arg4, s32 arg5) {
    func_1517D578(arg0, arg1, arg2, D_800DBFF0[arg3].unk380,
                 arg4, arg5, D_800DDD1C >> 3);
}'''


def candidates():
    forms = [('direct', SELECTED)]
    forms.append(('coordinate-locals', SELECTED.replace('    func_1517D578',
        '    register s16 x = arg0;\n    register s16 y = arg1;\n    register s16 z = arg2;\n    func_1517D578')
        .replace('func_1517D578(arg0, arg1, arg2,', 'func_1517D578(x, y, z,')))
    forms.append(('wide-parameters', SELECTED.replace('s16 arg', 's32 arg')
                  .replace('func_1517D578(arg0, arg1, arg2,', 'func_1517D578((s16)arg0, (s16)arg1, (s16)arg2,')))
    forms.append(('register-parameters', SELECTED.replace('s16 arg', 'register s16 arg')))
    forms.append(('volatile-coordinates', SELECTED.replace('s16 arg', 'volatile s16 arg')))
    forms.append(('volatile-index', SELECTED.replace('s32 arg3', 'volatile s32 arg3')))
    forms.append(('byte-stride', SELECTED.replace('D_800DBFF0[arg3].unk380',
                                                '*(f32 *)((u8 *)D_800DBFF0 + arg3 * 0x9A0 + 0x380)')))
    forms.append(('cached-actor', SELECTED.replace('    func_1517D578',
        '    struct108 *actor = &D_800DBFF0[arg3];\n    func_1517D578').replace('D_800DBFF0[arg3].unk380', 'actor->unk380')))
    return forms


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "structs.h"\n'+DECLARATIONS+body+'\n')
    command = ['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
               '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
               '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
               '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',
               *PROFILES[profile],'-o',str(obj.relative_to(root)),str(source.relative_to(root))]
    result = subprocess.run(command,cwd=root,capture_output=True,text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'queue.ld'
    script.write_text('SECTIONS { .text 0x1517D5FC : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e','func_1517D5FC',
                    *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()],'-o',str(elf),str(obj)],
                   check=True,capture_output=True,text=True)
    words = load_elf_functions(str(elf),'mips-linux-gnu-objdump')[0]['func_1517D5FC']
    end = max(i for i,word in enumerate(words) if word == 0x03E00008)+2
    if any(words[end:]):
        raise ValueError('nonzero return tail')
    words = words[:end]
    retail = list(struct.unpack_from('>37I',(root / 'conker/conker.us.bin').read_bytes(),ROM))
    slot = words+[0]*max(0,WORDS-end)
    different = [(i*4,hex(a),hex(b)) for i,(a,b) in enumerate(zip(slot,retail)) if a!=b]
    frames = [(-(w&65535))&65535 for w in words if w&0xFFFF0000 == 0x27BD0000 and w&0x8000]
    return dict(name=name,profile=profile,body_words=end,frame=max(frames,default=0),
                differences=len(different)+max(0,end-WORDS),different_words=different,
                exact=slot==retail,diagnostics=diagnostics),words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-position-queue-wrapper'
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
