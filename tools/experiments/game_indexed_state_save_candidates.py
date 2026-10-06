"""Recover the indexed state-save pass using the real actor/header definitions."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


ENTRY, ROM, WORDS = 0x15123934, 0x150DE4, 38
CALLBACK = 0x15125394
SELECTED = '''s32 func_15123934(struct108 *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    s16 *slot16;

    slot16 = (s16 *) arg0 + arg4;
    if (slot16[0x106] == 0) {
        ((u16 *) slot16)[1] = arg0->unk0;
        ((s32 *) arg0 + arg4)[0xC] = arg0->unk2C;
        ((s32 *) arg0 + arg4)[0x22] = arg0->unk84;
        ((s32 *) arg0 + arg4)[0x38] = arg0->unkDC;
        ((s32 *) arg0 + arg4)[0x4E] = arg0->unk134;
        slot16[0xDB] = arg0->unk1B4;
        slot16[0xF1] = arg0->unk1E0;
        arg0->unk2C = arg1;
        arg0->unkDC = arg2;
        arg0->unk134 = arg3;
        slot16[0x106] = 1;
        func_15125394(arg0);
        return 1;
    }
    return 0;
}'''
PROFILES = {'o2g3': ['-O2', '-g3'], 'o2': ['-O2'], 'o1g3': ['-O1', '-g3'], 'o1': ['-O1']}
TYPES = '''typedef unsigned char u8; typedef unsigned short u16; typedef short s16;
typedef int s32; typedef unsigned int u32;
typedef struct struct108 {
    u16 unk0;
    u16 unk2[21];
    s32 unk2C;
    u8 pad30[0x54];
    s32 unk84;
    u8 pad88[0x54];
    s32 unkDC;
    u8 padE0[0x54];
    s32 unk134;
    u8 pad138[0x7C];
    s16 unk1B4;
    u8 pad1B6[0x2A];
    s16 unk1E0;
    u8 pad1E2[0x2A];
    s16 unk20C[21];
} struct108;
'''


def candidates():
    forms = [('halfword-pointer', SELECTED)]
    forms.append(('unsigned-slot', SELECTED.replace('s16 *slot16;', 'u16 *slot16;')
                  .replace('slot16 = (s16 *)', 'slot16 = (u16 *)')))
    forms.append(('named-word-pointer', SELECTED.replace('    s16 *slot16;', '    s16 *slot16;\n    s32 *slot32;')
                  .replace('        ((u16 *) slot16)[1] = arg0->unk0;',
                           '        ((u16 *) slot16)[1] = arg0->unk0;\n        slot32 = (s32 *) arg0 + arg4;')
                  .replace('((s32 *) arg0 + arg4)', 'slot32')))
    forms.append(('field-gate', SELECTED.replace('slot16[0x106] == 0', 'arg0->unk20C[arg4] == 0')))
    forms.append(('explicit-byte-offset', SELECTED.replace('(s16 *) arg0 + arg4',
                                                         '(s16 *) ((u8 *) arg0 + arg4 * 2)')
                  .replace('((s32 *) arg0 + arg4)', '((s32 *) ((u8 *) arg0 + arg4 * 4))')))
    forms.append(('register-index', SELECTED.replace('s32 arg4)', 'register s32 arg4)')))
    forms.append(('early-return', SELECTED.replace('    if (slot16[0x106] == 0) {',
                                                  '    if (slot16[0x106] != 0) { return 0; }\n    {')
                  .replace('    }\n    return 0;\n}', '    }\n}')))
    forms.append(('direct-saved-id', SELECTED.replace('((u16 *) slot16)[1]', 'arg0->unk2[arg4]')))
    return forms


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n' + body + '\n')
    includes = ['.', 'include', 'include/2.0L', 'include/2.0L/PR', 'include/libc',
                'src/libultra/os', 'src/libultra/audio', 'src/libultra/io']
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32',
               '-woff', '649,838', *[flag for path in includes for flag in ('-I', path)],
               '-mips2', '-o32', *PROFILES[profile], '-o', str(obj.relative_to(root / 'conker')),
               str(source.relative_to(root / 'conker'))]
    compiled = subprocess.run(command, cwd=root / 'conker', capture_output=True, text=True)
    diagnostics = compiled.stdout + compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'save.ld'
    script.write_text('SECTIONS { .text 0x15123934 : SUBALIGN(4) { *(.text) } }\n')
    linked = subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_15123934',
                    '--defsym=func_15125394=0x15125394', '-o', str(elf), str(obj)],
                   capture_output=True, text=True)
    if linked.returncode:
        raise ValueError(linked.stdout + linked.stderr)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_15123934']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    if any(words[end:]):
        raise ValueError('nonzero tail after return')
    words = words[:end]
    retail = list(struct.unpack_from('>38I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    slot = words + [0] * max(0, WORDS - end)
    differences = [(i * 4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, profile=profile, body_words=end, frame=(-words[0]) & 65535,
                differences=len(differences) + max(0, end - WORDS), different_words=differences,
                exact=words == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-indexed-state-save'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
