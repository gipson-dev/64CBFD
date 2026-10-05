"""SDK-varargs table-address resolver source screening with retail relocations."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = '''u32 func_1502B020(u32 *size, u32 depth, ...) {
    va_list path;
    s32 component;
    u32 descriptor;
    u32 base;

    descriptor = 1;
    base = (u32)D_AB1950;
    va_start(path, depth);
    while (depth != 0) {
        component = va_arg(path, s32);
        if (descriptor != 0) {
            base += func_1502AC88(base, component, &descriptor);
        }
        depth--;
        descriptor &= 0x0FFFFFFF;
    }
    if (size != NULL) {
        *size = descriptor & 0x0FFFFFFF;
    }
    va_end(path);
    return descriptor != 0 ? base : 0;
}'''

PLACEHOLDER = '''s32 func_1502B020() {
    return 0;
}'''


def candidates():
    forms = [('baseline', BASELINE), ('placeholder', PLACEHOLDER)]
    declarations = '    va_list path;\n    s32 component;\n    u32 descriptor;\n    u32 base;'
    for index, order in enumerate(itertools.permutations(declarations.splitlines())):
        body = BASELINE.replace(declarations, '\n'.join(order))
        forms.append(('layout-' + str(index), body))
        forms.append(('layout-' + str(index) + '-store-order', body.replace(
            '        depth--;\n        descriptor &= 0x0FFFFFFF;',
            '        descriptor &= 0x0FFFFFFF;\n        depth--;')))
        early = body.replace('    return descriptor != 0 ? base : 0;',
            '    if (descriptor == 0) {\n        return 0;\n    }\n    return base;')
        forms.append(('layout-' + str(index) + '-early', early))
        forms.append(('layout-' + str(index) + '-early-store-order', early.replace(
            '        depth--;\n        descriptor &= 0x0FFFFFFF;',
            '        descriptor &= 0x0FFFFFFF;\n        depth--;')))
    for label, before, after in (
            ('return-if', '    return descriptor != 0 ? base : 0;',
             '    if (descriptor == 0) {\n        return 0;\n    }\n    return base;'),
            ('return-if-nonzero', '    return descriptor != 0 ? base : 0;',
             '    if (descriptor != 0) {\n        return base;\n    }\n    return 0;'),
            ('reverse-initialization', '    descriptor = 1;\n    base = (u32)D_AB1950;',
             '    base = (u32)D_AB1950;\n    descriptor = 1;'),
            ('predecrement', '        depth--;', '        --depth;'),
            ('unsigned-component', 's32 component;', 'u32 component;')):
        body = BASELINE.replace(before, after)
        if label == 'unsigned-component':
            body = body.replace('va_arg(path, s32)', 'va_arg(path, u32)')
            body = body.replace('base, component,', 'base, (s32)component,')
        forms.append((label, body))
    selected = dict(forms)['layout-1-early']
    for label, before, after in (
            ('predecrement', '        depth--;', '        --depth;'),
            ('comma-update', '        depth--;\n        descriptor &= 0x0FFFFFFF;',
             '        depth--, descriptor &= 0x0FFFFFFF;'),
            ('explicit-mask', 'descriptor &= 0x0FFFFFFF;', 'descriptor = descriptor & 0x0FFFFFFF;'),
            ('unsigned-component', 's32 component;', 'u32 component;')):
        body = selected.replace(before, after)
        if label == 'unsigned-component':
            body = body.replace('va_arg(path, s32)', 'va_arg(path, u32)')
            body = body.replace('base, component,', 'base, (s32)component,')
        forms.append(('selected-' + label, body))
    loop = selected.replace('    while (depth != 0) {', '    if (depth != 0) {\n        do {')
    loop = loop.replace('        depth--;\n        descriptor &= 0x0FFFFFFF;\n    }',
                        '        descriptor &= 0x0FFFFFFF;\n        } while (--depth != 0);\n    }')
    forms.append(('selected-do-while', loop))
    return forms


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    prefix = ('#include "stdarg.h"\ntypedef unsigned char u8; typedef int s32; typedef unsigned int u32;\n'
              '#define NULL ((void *)0)\nextern u8 D_AB1950[];\n'
              's32 func_1502AC88(u32,s32,u32 *);\n')
    path.write_text(prefix + source + '\n')
    result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
        '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
        '-I', 'include/libc', '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
        str(path.relative_to(conker))], cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502B020 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502B020',
        '--defsym=D_AB1950=0xAB1950', '--defsym=func_1502AC88=0x1502AC88',
        '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502B020']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 60 - size)
    retail = struct.unpack_from('>60I', (conker / 'conker.us.bin').read_bytes(), 0x584D0)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - 60),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    root = Path(__file__).resolve().parents[2]
    production = re.search(r'u32 func_1502B020\([^;{}]+\) \{\n.*?\n\}',
                           (root / 'conker/src/game_57FA0.c').read_text(), re.S).group(0)
    assert production == dict(candidates())['layout-1-early']
    output = root / 'conker/build/game-variadic-table-address'
    output.mkdir(exist_ok=True)
    records = []
    for name, source in candidates():
        record, _ = compile_candidate(root, output, name, source)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
