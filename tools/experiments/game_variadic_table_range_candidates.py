"""SDK-varargs table-range wrapper source screening with fixed retail relocations."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = '''u32 *func_1502B110(u32 base, u32 count, void *buffer, u32 depth, ...) {
    u32 *result;
    u32 descriptor;
    va_list path;
    s32 component;

    descriptor = 1;
    result = NULL;
    if (base == 0) {
        base = (u32)D_AB1950;
    }
    va_start(path, depth);
    while (depth >= 2) {
        component = va_arg(path, s32);
        if (descriptor != 0) {
            base += func_1502AC88(base, component, &descriptor);
        }
        depth--;
        descriptor &= 0x0FFFFFFF;
    }
    component = va_arg(path, s32);
    if (descriptor != 0) {
        result = func_1502AF04(base, buffer, (u32)component, count);
    }
    va_end(path);
    return result;
}'''

PLACEHOLDER = '''s32 func_1502B110() {
    return 0;
}'''


def candidates():
    forms = [('baseline', BASELINE), ('placeholder', PLACEHOLDER)]
    for name, body in (('baseline', BASELINE),
            ('unsigned-component', BASELINE.replace('s32 component;', 'u32 component;')
             .replace('va_arg(path, s32)', 'va_arg(path, u32)')
             .replace('base, component,', 'base, (s32)component,'))):
        if name != 'baseline':
            forms.append((name, body))
        original = '    u32 *result;\n    u32 descriptor;\n    va_list path;\n    s32 component;'
        if name == 'unsigned-component':
            original = original.replace('s32 component;', 'u32 component;')
        decls = original.splitlines()
        for index, order in enumerate(itertools.permutations(decls)):
            forms.append((name + '-layout-' + str(index), body.replace(original, '\n'.join(order))))
        for label, before, after in (
                ('strict-depth', 'while (depth >= 2)', 'while (depth > 1)'),
                ('condition-decrement', '        depth--;\n        descriptor &= 0x0FFFFFFF;\n    }',
                 '        descriptor &= 0x0FFFFFFF;\n        depth--;\n    }'),
                ('initialization-reversed', '    descriptor = 1;\n    result = NULL;',
                 '    result = NULL;\n    descriptor = 1;'),
                ('late-result', '    result = NULL;\n', ''),
                ('integer-result', '    u32 *result;', '    u32 result;')):
            candidate = body.replace(before, after)
            if label == 'late-result':
                candidate = candidate.replace('    if (descriptor != 0) {\n        result =',
                                               '    result = NULL;\n    if (descriptor != 0) {\n        result =')
            if label == 'integer-result':
                candidate = candidate.replace('result = NULL;', 'result = 0;')
                candidate = candidate.replace('result = func_1502AF04(', 'result = (u32)func_1502AF04(')
                candidate = candidate.replace('return result;', 'return (u32 *)result;')
            forms.append((name + '-' + label, candidate))
    selected = dict(forms)['baseline-layout-17']
    for label, before, after in (
            ('descriptor-first', '        depth--;\n        descriptor &= 0x0FFFFFFF;',
             '        descriptor &= 0x0FFFFFFF;\n        depth--;'),
            ('predecrement', '        depth--;', '        --depth;'),
            ('explicit-descriptor', 'descriptor &= 0x0FFFFFFF;', 'descriptor = descriptor & 0x0FFFFFFF;'),
            ('comma-update', '        depth--;\n        descriptor &= 0x0FFFFFFF;',
             '        depth--, descriptor &= 0x0FFFFFFF;')):
        forms.append(('selected-' + label, selected.replace(before, after)))
    loop = selected.replace('    while (depth >= 2) {', '    if (depth >= 2) {\n        do {')
    loop = loop.replace('        depth--;\n        descriptor &= 0x0FFFFFFF;\n    }',
                        '        descriptor &= 0x0FFFFFFF;\n        } while (--depth >= 2);\n    }')
    forms.append(('selected-do-while', loop))
    forms.append(('selected-do-while-greater', loop.replace('--depth >= 2', '--depth > 1')))
    return forms


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    prefix = ('#include "stdarg.h"\ntypedef unsigned char u8; typedef int s32; typedef unsigned int u32;\n'
              '#define NULL ((void *)0)\nextern u8 D_AB1950[];\n'
              's32 func_1502AC88(u32,s32,u32 *); u32 *func_1502AF04(u32,void *,u32,u32);\n')
    path.write_text(prefix + source + '\n')
    result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
        '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
        '-I', 'include/libc', '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
        str(path.relative_to(conker))], cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502B110 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502B110',
        '--defsym=D_AB1950=0xAB1950', '--defsym=func_1502AC88=0x1502AC88',
        '--defsym=func_1502AF04=0x1502AF04', '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502B110']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 69 - size)
    retail = struct.unpack_from('>69I', (conker / 'conker.us.bin').read_bytes(), 0x585C0)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - 69),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    root = Path(__file__).resolve().parents[2]
    production = re.search(r'u32 \*func_1502B110\([^;{}]+\) \{\n.*?\n\}',
                           (root / 'conker/src/game_57FA0.c').read_text(), re.S).group(0)
    assert production == dict(candidates())['baseline-layout-17']
    output = root / 'conker/build/game-variadic-table-range'
    output.mkdir(exist_ok=True)
    records = []
    for name, source in candidates():
        record, _ = compile_candidate(root, output, name, source)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
