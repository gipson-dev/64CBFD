"""SDK-varargs optional-size loader screening, including incoming descriptor controls."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = '''void *func_1502B5C8(s32 *size, u32 depth, ...) {
    s32 *target;
    va_list path;
    s32 fallbackSize;
    s32 component;
    u32 base;
    u32 descriptor;
    void *result;

    target = &fallbackSize;
    if (size != NULL) {
        target = size;
    }
    *target = 1;
    base = (u32)D_AB1950;
    va_start(path, depth);
    if (depth != 0) {
        do {
            component = va_arg(path, s32);
            if (*target != 0) {
                base += func_1502AC88(base, component, &descriptor);
            }
            *target = descriptor & 0x0FFFFFFF;
        } while (--depth != 0);
    }
    va_end(path);
    if (*target != 0) {
        result = func_1502B350(base, descriptor, target);
    } else {
        result = NULL;
    }
    return result;
}'''

PLACEHOLDER = '''s32 func_1502B5C8() {
    return 0;
}'''


def candidates():
    forms = [('baseline', BASELINE), ('placeholder', PLACEHOLDER)]
    declarations = '    va_list path;\n    s32 fallbackSize;\n    s32 component;\n    u32 base;\n    u32 descriptor;'
    for index, order in enumerate(itertools.permutations(declarations.splitlines())):
        forms.append(('layout-' + str(index), BASELINE.replace(declarations, '\n'.join(order))))
    for name, before, after in (
            ('ternary-target', '    target = &fallbackSize;\n    if (size != NULL) {\n        target = size;\n    }',
             '    target = size != NULL ? size : &fallbackSize;'),
            ('inverted-target', '    target = &fallbackSize;\n    if (size != NULL) {\n        target = size;\n    }',
             '    target = size;\n    if (size == NULL) {\n        target = &fallbackSize;\n    }'),
            ('while-loop', '    if (depth != 0) {\n        do {', '    while (depth != 0) {'),
            ('result-default', '    if (*target != 0) {\n        result = func_1502B350(base, descriptor, target);\n    } else {\n        result = NULL;\n    }',
             '    result = NULL;\n    if (*target != 0) {\n        result = func_1502B350(base, descriptor, target);\n    }'),
            ('zero-descriptor', '    *target = 1;', '    descriptor = 0;\n    *target = 1;'),
            ('one-descriptor', '    *target = 1;', '    descriptor = 1;\n    *target = 1;')):
        body = BASELINE.replace(before, after)
        if name == 'while-loop':
            body = body.replace('        } while (--depth != 0);\n    }', '        depth--;\n    }')
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
    script.write_text('SECTIONS { .text 0x1502B5C8 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502B5C8',
        '--defsym=D_AB1950=0xAB1950', '--defsym=func_1502AC88=0x1502AC88',
        '--defsym=func_1502B350=0x1502B350', '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502B5C8']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 61 - size)
    retail = struct.unpack_from('>61I', (conker / 'conker.us.bin').read_bytes(), 0x58A78)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - 61),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    root = Path(__file__).resolve().parents[2]
    production = (root / 'conker/src/game_57FA0.c').read_text()
    body = re.search(r'void \*func_1502B5C8\([^;{}]+\) \{\n.*?\n\}', production, re.S).group(0)
    assert body == dict(candidates())['layout-6']
    output = root / 'conker/build/game-optional-size-loader'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
