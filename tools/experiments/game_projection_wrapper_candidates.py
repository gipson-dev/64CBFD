"""Recover the six-argument projection wrapper and its four-component helper ABI."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x15144CEC, 0x17219C, 101
SYMBOLS = {'func_150A7A00': 0x150A7A00, 'D_800D9D10': 0x800D9D10,
           'D_800BE628': 0x800BE628, 'D_800A56B0': 0x800A56B0, 'D_800D9B20': 0x800D9B20}
DECLARATIONS = '''extern s32 D_800D9D10[];
extern s32 D_800BE628;
extern f32 D_800A56B0, D_800D9B20;
void func_150A7A00(f32 matrix[4][4], f32 x, f32 y, f32 z, f32 *outX, f32 *outY, f32 *outZ, f32 *outW);
'''
SELECTED = '''s32 func_15144CEC(struct17 *arg0, f32 *arg1, f32 *arg2, f32 *arg3, f32 *arg4, u8 arg5) {
    f32 localZ;
    f32 localW;
    f32 localReciprocal;
    f32 depth;
    f32 xProduct;
    f32 yProduct;
    struct140 *view;

    if (arg2 == NULL) {
        arg2 = &localZ;
    }
    if (arg3 == NULL) {
        arg3 = &localW;
    }
    if (arg4 == NULL) {
        arg4 = &localReciprocal;
    }
    func_150A7A00((f32 (*)[4])((u8 *)D_800D9D10 + (arg5 << 6)),
                 arg0->unk0, arg0->unk4, arg0->unk8, arg1, arg1 + 1, arg2, arg3);
    depth = *arg3;
    if (D_800A56B0 <= depth || depth <= D_800D9B20) {
        return 0;
    }
    if (depth == 0.0f) {
        return 0;
    }
    *arg4 = 1.0f / depth;
    view = (struct140 *)((u8 *)D_800BE628 + arg5 * 0x180);
    xProduct = arg1[0] * (view->unkC + 5.0f);
    yProduct = arg1[1] * (view->unk10 + 5.0f);
    arg1[0] = *arg4 * xProduct + view->unk34;
    view = (struct140 *)((u8 *)D_800BE628 + arg5 * 0x180);
    arg1[1] = view->unk38 - *arg4 * yProduct;
    return 1;
}'''
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}


def candidates():
    forms = []
    parameters = ('struct17 *arg0', 'f32 *arg2', 'f32 *arg3', 'f32 *arg4')
    for mask in range(16):
        body = SELECTED
        for index, parameter in enumerate(parameters):
            if mask & 1 << index:
                body = body.replace(parameter, parameter.replace('*', '*volatile '), 1)
        forms.append(('pointer-homes-%x' % mask, body))
    uncached = SELECTED.replace('    f32 depth;\n', '').replace('    depth = *arg3;\n', '').replace('depth', '*arg3')
    grouped = uncached.replace('''    if (*arg3 == 0.0f) {
        return 0;
    }
    *arg4''', '''    if (*arg3 != 0.0f) {
    *arg4''').replace('    return 1;\n}', '    return 1;\n    }\n    return 0;\n}')
    lifetimes = [('uncached-depth', uncached), ('nonzero-body', grouped)]
    forms.extend(lifetimes)
    forms.extend((name + '-live-index', body.replace('u8 arg5)', 'volatile u8 arg5)'))
                 for name, body in lifetimes)
    return forms


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "structs.h"\n' + DECLARATIONS + body + '\n')
    command = ['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm', '-signed',
               '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
               '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32',
               *PROFILES[profile], '-o', str(obj.relative_to(root)), str(source.relative_to(root))]
    compiled = subprocess.run(command, cwd=root, capture_output=True, text=True)
    diagnostics = compiled.stdout + compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'projection.ld'
    script.write_text('SECTIONS { .text 0x15144CEC : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_15144CEC',
                    *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
                   check=True, capture_output=True, text=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_15144CEC']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    if any(words[end:]):
        raise ValueError('nonzero tail after return')
    words = words[:end]
    retail = list(struct.unpack_from('>101I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    slot = words + [0] * max(0, WORDS - end)
    differences = [(i * 4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-(w & 65535)) & 65535 for w in words if w & 0xFFFF0000 == 0x27BD0000 and w & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=max(frames, default=0),
                differences=len(differences) + max(0, end - WORDS), different_words=differences,
                exact=words == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-projection-wrapper'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
