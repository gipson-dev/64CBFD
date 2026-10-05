"""SDK-varargs caller-buffer wrapper screen, retaining the original descriptor seed."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = '''u32 func_1502B8E0(void *buffer, u32 cap, u32 depth, ...) {
    va_list path;
    s32 component;
    u32 base;
    u32 descriptor;
    u32 gate;

    base = (u32)D_AB1950;
    gate = 1;
    va_start(path, depth);
    while (depth != 0) {
        component = va_arg(path, s32);
        if (gate != 0) {
            base += func_1502AC88(base, component, &descriptor);
        }
        depth--;
        gate = descriptor & 0x0FFFFFFF;
    }
    if (gate != 0) {
        gate = func_1502B224(base, buffer, descriptor, cap);
    }
    va_end(path);
    return gate;
}'''

PLACEHOLDER = '''s32 func_1502B8E0() {
    return 0;
}'''


def candidates():
    forms = [('baseline', BASELINE), ('placeholder', PLACEHOLDER)]
    declarations = '    va_list path;\n    s32 component;\n    u32 base;\n    u32 descriptor;\n    u32 gate;'
    for index, order in enumerate(itertools.permutations(declarations.splitlines())):
        forms.append(('layout-' + str(index), BASELINE.replace(declarations, '\n'.join(order))))
    forms.append(('descriptor-zero', BASELINE.replace('    base = (u32)D_AB1950;',
                                                    '    descriptor = 0;\n    base = (u32)D_AB1950;')))
    forms.append(('descriptor-one', BASELINE.replace('    base = (u32)D_AB1950;',
                                                   '    descriptor = 1;\n    base = (u32)D_AB1950;')))
    forms.append(('gate-first', BASELINE.replace('    base = (u32)D_AB1950;\n    gate = 1;',
                                               '    gate = 1;\n    base = (u32)D_AB1950;')))
    forms.append(('gate-before-depth', BASELINE.replace('        depth--;\n        gate = descriptor & 0x0FFFFFFF;',
                                                      '        gate = descriptor & 0x0FFFFFFF;\n        depth--;')))
    selected = dict(forms)['layout-1']
    for label, before, after in (
            ('gate-first', '    base = (u32)D_AB1950;\n    gate = 1;',
             '    gate = 1;\n    base = (u32)D_AB1950;'),
            ('register-base', '    u32 base;', '    register u32 base;'),
            ('register-gate', '    u32 gate;', '    register u32 gate;'),
            ('comma-initialization', '    base = (u32)D_AB1950;\n    gate = 1;',
             '    base = (u32)D_AB1950, gate = 1;'),
            ('gate-before-depth', '        depth--;\n        gate = descriptor & 0x0FFFFFFF;',
             '        gate = descriptor & 0x0FFFFFFF;\n        depth--;'),
            ('zero-descriptor', '    base = (u32)D_AB1950;', '    descriptor = 0;\n    base = (u32)D_AB1950;'),
            ('one-descriptor', '    base = (u32)D_AB1950;', '    descriptor = 1;\n    base = (u32)D_AB1950;')):
        forms.append(('selected-' + label, selected.replace(before, after)))
    return forms


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    prefix = ('#include "stdarg.h"\ntypedef unsigned char u8; typedef int s32; typedef unsigned int u32;\n'
              '#define NULL ((void *)0)\nextern u8 D_AB1950[];\n'
              's32 func_1502AC88(u32,s32,u32 *); u32 func_1502B224(u32,void *,u32,u32);\n')
    path.write_text(prefix + source + '\n')
    result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
        '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
        '-I', 'include/libc', '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
        str(path.relative_to(conker))], cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502B8E0 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502B8E0',
        '--defsym=D_AB1950=0xAB1950', '--defsym=func_1502AC88=0x1502AC88',
        '--defsym=func_1502B224=0x1502B224', '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502B8E0']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 53 - size)
    retail = struct.unpack_from('>53I', (conker / 'conker.us.bin').read_bytes(), 0x58D90)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - 53),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    root = Path(__file__).resolve().parents[2]
    production = (root / 'conker/src/game_57FA0.c').read_text()
    body = re.search(r'u32 func_1502B8E0\([^;{}]+\) \{\n.*?\n\}', production, re.S).group(0)
    assert body == dict(candidates())['selected-gate-first']
    output = root / 'conker/build/game-buffer-variadic-loader'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
