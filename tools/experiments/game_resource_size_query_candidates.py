"""SDK-varargs size query with the retail stack-aligned compressed header."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = '''u32 func_1502B9B4(u32 depth, ...) {
    va_list path;
    s32 component;
    u32 base;
    u32 descriptor;
    u32 size;
    u32 storage[6];
    u32 *header;

    base = (u32)D_AB1950;
    size = 1;
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
        size = ((descriptor & 0x0FFFFFFF) + 1) & ~1U;
        if ((descriptor & 0x70000000) == 0x10000000) {
            header = storage;
            if ((u32)header & 8) {
                header = storage + 2;
            }
            func_10004514(base, header, 16, 1);
            size = header[0];
        }
    }
    va_end(path);
    return size;
}'''

PLACEHOLDER = '''s32 func_1502B9B4() {
    return 0;
}'''


def candidates():
    forms = [('baseline', BASELINE), ('placeholder', PLACEHOLDER)]
    for kind, decl in (('u32', 'u32 storage[6];'), ('u64', 'u64 storage[3];'),
                       ('u8', 'u8 storage[24];')):
        body = BASELINE.replace('u32 storage[6];', decl)
        if kind != 'u32':
            body = body.replace('header = storage;', 'header = (u32 *)storage;')
            body = body.replace('header = storage + 2;', 'header = (u32 *)((u8 *)storage + 8);')
        forms.append(('buffer-' + kind, body))
    declarations = '    va_list path;\n    s32 component;\n    u32 base;\n    u32 descriptor;\n    u32 size;'
    for index, order in enumerate(itertools.permutations(declarations.splitlines())):
        forms.append(('layout-' + str(index), BASELINE.replace(declarations, '\n'.join(order))))
    for name, before, after in (
            ('size-first', '    base = (u32)D_AB1950;\n    size = 1;', '    size = 1;\n    base = (u32)D_AB1950;'),
            ('size-before-depth', '        depth--;\n        size = descriptor & 0x0FFFFFFF;', '        size = descriptor & 0x0FFFFFFF;\n        depth--;'),
            ('zero-descriptor', '    size = 1;', '    descriptor = 0;\n    size = 1;'),
            ('one-descriptor', '    size = 1;', '    descriptor = 1;\n    size = 1;')):
        forms.append((name, BASELINE.replace(before, after)))
    selected = dict(forms)['layout-1'].replace('u32 storage[6];', 'u64 storage[3];')
    selected = selected.replace('header = storage;', 'header = (u32 *)storage;')
    selected = selected.replace('header = storage + 2;', 'header = (u32 *)((u8 *)storage + 8);')
    forms.append(('selected-u64', selected))
    for name, before, after in (
            ('size-first', '    base = (u32)D_AB1950;\n    size = 1;', '    size = 1;\n    base = (u32)D_AB1950;'),
            ('comma-init', '    base = (u32)D_AB1950;\n    size = 1;', '    base = (u32)D_AB1950, size = 1;'),
            ('register-base', '    u32 base;', '    register u32 base;'),
            ('register-size', '    u32 size;', '    register u32 size;'),
            ('zero-descriptor', '    size = 1;', '    descriptor = 0;\n    size = 1;'),
            ('one-descriptor', '    size = 1;', '    descriptor = 1;\n    size = 1;')):
        forms.append(('selected-' + name, selected.replace(before, after)))
    return forms


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    prefix = ('#include "stdarg.h"\ntypedef unsigned char u8; typedef int s32; typedef unsigned int u32;\n'
              'typedef unsigned long long u64;\nextern u8 D_AB1950[];\n'
              's32 func_1502AC88(u32,s32,u32 *); s32 func_10004514(u32,void *,u32,s32);\n')
    path.write_text(prefix + source + '\n')
    result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
        '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
        '-I', 'include/libc', '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
        str(path.relative_to(conker))], cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502B9B4 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502B9B4',
        '--defsym=D_AB1950=0xAB1950', '--defsym=func_1502AC88=0x1502AC88',
        '--defsym=func_10004514=0x10004514', '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502B9B4']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 71 - size)
    retail = struct.unpack_from('>71I', (conker / 'conker.us.bin').read_bytes(), 0x58E64)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - 71),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    root = Path(__file__).resolve().parents[2]
    production = (root / 'conker/src/game_57FA0.c').read_text()
    body = re.search(r'u32 func_1502B9B4\([^;{}]+\) \{\n.*?\n\}', production, re.S).group(0)
    assert body == dict(candidates())['selected-size-first']
    output = root / 'conker/build/game-resource-size-query'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
