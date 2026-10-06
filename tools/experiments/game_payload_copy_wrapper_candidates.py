"""Bound the allocation/copy wrapper's success join and pointer return ABI."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x151407D0, 0x16DC80, 53
WRAPPER_ENTRY, WRAPPER_ROM, WRAPPER_WORDS = 0x1513D524, 0x16A9D4, 28
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SYMBOLS = {'func_1513D524': WRAPPER_ENTRY, 'memcpy': 0x10022EC0, 'D_800DC9F0': 0x800DC9F0}
DECLARATIONS = '''void *func_1513D524(void *,u8,u8,u8,u8,u8,s32,u8,s32);
extern s32 D_800DC9F0;
'''
SELECTED = '''u8 *func_151407D0(void *source, s32 size, u8 *descriptor, u8 kind, u8 mode,
                       u8 first, u8 variant, s8 selector, u8 channel, s32 context) {
    u8 *result;
    u8 *payload;
    descriptor[1] = 3;
    *(u32 *)(descriptor + 0x40) |= 0x40400000;
    result = func_1513D524(descriptor, kind, mode, first, 1, variant, size, channel, context);
    if (result != NULL) {
        payload = result + 0x110;
        memcpy(payload, source, size);
        *(s32 *)(payload + 0x44) = 0;
        payload[0x59] = selector;
        goto finalize;
    }
    return NULL;
finalize:
    if (result != NULL) {
        *(u32 *)&D_800DC9F0 += 1;
    }
    return result;
}'''
WRAPPER_DECLARATIONS = '''void *func_1513D2F0(void *,s32,u8,u8,u8,u8,u8,s32,s32,s32,u8,s32);
extern u8 D_800A4AA0[];
'''
WRAPPER = '''void *func_1513D524(void *descriptor, u8 kind, u8 mode, u8 first, u8 setup,
                         u8 variant, s32 size, u8 channel, s32 context) {
    return func_1513D2F0(descriptor, (s32)&D_800A4AA0, kind, mode, first, setup,
                        variant, 0, 0, size, channel, context);
}'''


def candidates():
    structured = SELECTED.replace('        goto finalize;\n    }\n    return NULL;\nfinalize:',
        '    } else {\n        return NULL;\n    }')
    early = structured.replace('    if (result != NULL) {\n        payload',
        '    if (result == NULL) { return NULL; }\n    {\n        payload').replace(
        '    } else {\n        return NULL;\n    }', '    }')
    captured = SELECTED.replace('    u8 *payload;', '    u8 *payload;\n    s8 choice;').replace(
        '        *(s32 *)(payload + 0x44) = 0;', '        choice = selector;\n        *(s32 *)(payload + 0x44) = 0;').replace(
        'payload[0x59] = selector', 'payload[0x59] = choice')
    typed = SELECTED.replace('u8 *payload', 'Payload16DC80 *payload').replace(
        'payload = result + 0x110', 'payload = (Payload16DC80 *)(result + 0x110)').replace(
        '*(s32 *)(payload + 0x44)', 'payload->zero').replace('payload[0x59]', 'payload->selector')
    layout = '''typedef struct Payload16DC80 {
    u8 prefix[0x44]; s32 zero; u8 gap[0x11]; s8 selector;
} Payload16DC80;
'''
    return [('success-join', SELECTED, DECLARATIONS), ('structured', structured, DECLARATIONS),
            ('early-null', early, DECLARATIONS), ('capture-selector', captured, DECLARATIONS),
            ('typed-payload', typed, DECLARATIONS+layout),
            ('volatile-counter', SELECTED.replace('*(u32 *)&D_800DC9F0',
                '*(volatile u32 *)&D_800DC9F0'), DECLARATIONS)]


def wrapper_candidates():
    word = WRAPPER.replace('void *descriptor', 's32 descriptor').replace(
        'func_1513D2F0(descriptor,', 'func_1513D2F0((void *)descriptor,')
    old = word.replace('void *func_', 'void func_').replace('    return func_', '    func_')
    byte = WRAPPER.replace('void *func_', 'u8 *func_').replace('void *descriptor', 'u8 *descriptor')
    return [('old-void', old), ('word-return', word), ('descriptor-return', WRAPPER), ('byte-return', byte)]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3', declarations=DECLARATIONS, wrapper=False):
    function, entry, rom, count = ('func_1513D524', WRAPPER_ENTRY, WRAPPER_ROM, WRAPPER_WORDS) if wrapper else (
        'func_151407D0', ENTRY, ROM, WORDS)
    symbols = {'func_1513D2F0': 0x1513D2F0, 'D_800A4AA0': 0x800A4AA0} if wrapper else SYMBOLS
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+declarations+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics: raise ValueError(diagnostics)
    script = output/(function+'.ld')
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n'%entry)
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', function,
        *['--defsym=%s=0x%X'%item for item in symbols.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0][function]
    end = max(i for i,word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:]); words = words[:end]
    retail = list(struct.unpack_from('>%dI'%count, (root/'conker/conker.us.bin').read_bytes(), rom))
    slot = words+[0]*max(0,count-end)
    differences = [(i*4,hex(a),hex(b)) for i,(a,b) in enumerate(zip(slot,retail)) if a != b]
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    return dict(name=name,profile=profile,body_words=end,frame=frames[0] if frames else 0,
        differences=len(differences)+max(0,end-count),different_words=differences,
        exact=slot==retail,diagnostics=diagnostics),words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-payload-copy-wrapper'; output.mkdir(exist_ok=True)
    records = []
    for name,body,declarations in candidates():
        for profile in PROFILES:
            record,_ = compile_candidate(root,output,name+'-'+profile,body,profile,declarations)
            records.append(record); print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    for name,body in wrapper_candidates():
        for profile in PROFILES:
            record,_ = compile_candidate(root,output,'wrapper-'+name+'-'+profile,body,profile,WRAPPER_DECLARATIONS,True)
            records.append(record); print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__ == '__main__':
    main()
