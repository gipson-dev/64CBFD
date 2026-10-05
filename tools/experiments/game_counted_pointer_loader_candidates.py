"""SDK-varargs pointer-output/returned-size wrapper with retail stack dependencies."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = '''u32 func_1502B7F0(void **output, u32 depth, ...) {
    va_list path;
    s32 component;
    u32 base;
    u32 descriptor;
    s32 size;

    size = 1;
    base = (u32)D_AB1950;
    va_start(path, depth);
    while (depth != 0) {
        component = va_arg(path, s32);
        if (size != 0) {
            base += func_1502AC88(base, component, &descriptor);
        }
        depth--;
        size = descriptor & 0x0FFFFFFF;
    }
    if (size != 0) {
        *output = func_1502B350(base, descriptor, &size);
    } else {
        *output = NULL;
    }
    va_end(path);
    return (u32)size;
}'''

PLACEHOLDER = '''s32 func_1502B7F0(s32 *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    return 0;
}'''


def candidates():
    forms = [('baseline', BASELINE), ('placeholder', PLACEHOLDER)]
    declarations = '    va_list path;\n    s32 component;\n    u32 base;\n    u32 descriptor;\n    s32 size;'
    for index, order in enumerate(itertools.permutations(declarations.splitlines())):
        forms.append(('layout-' + str(index), BASELINE.replace(declarations, '\n'.join(order))))
    for name, before, after in (
            ('base-first', '    size = 1;\n    base = (u32)D_AB1950;', '    base = (u32)D_AB1950;\n    size = 1;'),
            ('size-before-depth', '        depth--;\n        size = descriptor & 0x0FFFFFFF;',
             '        size = descriptor & 0x0FFFFFFF;\n        depth--;'),
            ('unsigned-size', '    s32 size;', '    u32 size;'),
            ('zero-descriptor', '    size = 1;', '    descriptor = 0;\n    size = 1;'),
            ('one-descriptor', '    size = 1;', '    descriptor = 1;\n    size = 1;')):
        body = BASELINE.replace(before, after)
        if name == 'unsigned-size':
            body = body.replace('descriptor, &size)', 'descriptor, (s32 *)&size)')
        forms.append((name, body))
    selected = dict(forms)['layout-1']
    for name, before, after in (
            ('selected-size-first', '        depth--;\n        size = descriptor & 0x0FFFFFFF;',
             '        size = descriptor & 0x0FFFFFFF;\n        depth--;'),
            ('selected-depth-subtract', '        depth--;', '        depth = depth - 1;'),
            ('selected-for', '    while (depth != 0) {', '    for (; depth != 0; depth--) {'),
            ('selected-do', '    while (depth != 0) {', '    if (depth != 0) do {'),
            ('selected-comma', '        depth--;\n        size = descriptor & 0x0FFFFFFF;',
             '        depth--, size = descriptor & 0x0FFFFFFF;')):
        body = selected.replace(before, after)
        if name == 'selected-for':
            body = body.replace('        depth--;\n', '')
        if name == 'selected-do':
            body = body.replace('    }\n    if (size', '    } while (depth != 0);\n    if (size')
        forms.append((name, body))
    return forms


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    prefix = ('#include "stdarg.h"\ntypedef unsigned char u8; typedef int s32; typedef unsigned int u32;\n'
              '#define NULL ((void *)0)\nextern u8 D_AB1950[];\n'
              's32 func_1502AC88(u32,s32,u32 *); void *func_1502B350(u32,u32,s32 *);\n')
    path.write_text(prefix + source + '\n')
    result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
        '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
        '-I', 'include/libc', '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
        str(path.relative_to(conker))], cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502B7F0 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502B7F0',
        '--defsym=D_AB1950=0xAB1950', '--defsym=func_1502AC88=0x1502AC88',
        '--defsym=func_1502B350=0x1502B350', '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502B7F0']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 60 - size)
    retail = struct.unpack_from('>60I', (conker / 'conker.us.bin').read_bytes(), 0x58CA0)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - 60),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    root = Path(__file__).resolve().parents[2]
    source = (root / 'conker/src/game_57FA0.c').read_text()
    body = re.search(r'u32 func_1502B7F0\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
    assert body == dict(candidates())['selected-for']
    output = root / 'conker/build/game-counted-pointer-loader'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
