"""Caller-buffer resource-loader source screen with fixed retail relocations."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = '''u32 func_1502B224(u32 address, void *buffer, u32 descriptor, u32 cap) {
    u32 amount;
    u32 expanded;
    void *compressed;

    amount = ((descriptor & 0x0FFFFFFF) + 1) & ~1;
    if (cap != 0 && cap < amount) {
        amount = cap;
    }
    if ((descriptor & 0x70000000) == 0x10000000) {
        compressed = allocate_memory(amount, 1, 2, 2);
        if (compressed == NULL) {
            return 0;
        }
        func_10004514(address, compressed, (amount + 15) & ~0xF, 1);
        expanded = *(u32 *)compressed & 0x7FFFFFFF;
        amount = func_10006240(compressed, buffer, D_8003809C);
        if (amount != expanded) {
            D_8003C8E0 = 0x0C000036;
            func_150AD770();
        }
        func_10004074(compressed);
    } else {
        func_10004514(address, buffer, (amount + 15) & ~0xF, 1);
    }
    return amount;
}'''

PLACEHOLDER = '''s32 func_1502B224() {
    return 0;
}'''


def candidates():
    forms = [('baseline', BASELINE), ('placeholder', PLACEHOLDER)]
    declarations = '    u32 amount;\n    u32 expanded;\n    void *compressed;'
    for index, order in enumerate(itertools.permutations(declarations.splitlines())):
        forms.append(('layout-' + str(index), BASELINE.replace(declarations, '\n'.join(order))))
    for mask in range(1, 8):
        body = BASELINE
        for i, declaration in enumerate(declarations.splitlines()):
            if mask & (1 << i):
                body = body.replace(declaration, declaration.replace('    ', '    register ', 1))
        forms.append(('register-' + str(mask), body))
    for label, before, after in (
            ('nested-cap', '    if (cap != 0 && cap < amount) {\n        amount = cap;\n    }',
             '    if (cap != 0) {\n        if (cap < amount) {\n            amount = cap;\n        }\n    }'),
            ('reverse-cap', 'cap < amount', 'amount > cap'),
            ('cap-ternary', '    if (cap != 0 && cap < amount) {\n        amount = cap;\n    }',
             '    amount = cap != 0 && cap < amount ? cap : amount;'),
            ('allocation-condition', '        compressed = allocate_memory(amount, 1, 2, 2);\n        if (compressed == NULL)',
             '        if ((compressed = allocate_memory(amount, 1, 2, 2)) == NULL)'),
            ('signed-size', '    u32 expanded;', '    s32 expanded;'),
            ('error-constant-u', '0x0C000036;', '0x0C000036u;')):
        body = BASELINE.replace(before, after)
        if label == 'signed-size':
            body = body.replace('amount != expanded', 'amount != (u32)expanded')
        forms.append((label, body))
    raw_first = BASELINE.replace('    if ((descriptor & 0x70000000) == 0x10000000) {',
        '    if ((descriptor & 0x70000000) != 0x10000000) {\n'
        '        func_10004514(address, buffer, (amount + 15) & ~0xF, 1);\n    } else {')
    raw_first = raw_first.replace('    } else {\n        func_10004514(address, buffer, (amount + 15) & ~0xF, 1);\n    }\n', '    }\n')
    forms.append(('raw-first', raw_first))
    return forms


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    prefix = ('typedef int s32; typedef unsigned int u32;\n#define NULL ((void *)0)\n'
              'void *allocate_memory(s32,s32,s32,s32);\n'
              's32 func_10004514(u32,void *,u32,s32);\n'
              's32 func_10006240(void *,void *,u32); void func_10004074(void *);\n'
              'extern u32 D_8003809C; extern s32 D_8003C8E0; void func_150AD770(void);\n')
    path.write_text(prefix + source + '\n')
    result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
        '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
        '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)), str(path.relative_to(conker))],
        cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502B224 : SUBALIGN(4) { *(.text) } }\n')
    targets = {'allocate_memory': 0x10003C40, 'func_10004514': 0x10004514,
               'func_10006240': 0x10006240, 'func_10004074': 0x10004074,
               'D_8003809C': 0x8003809C, 'D_8003C8E0': 0x8003C8E0, 'func_150AD770': 0x150AD770}
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1502B224',
        *(f'--defsym={k}=0x{v:X}' for k, v in targets.items()), '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502B224']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 75 - size)
    retail = struct.unpack_from('>75I', (conker / 'conker.us.bin').read_bytes(), 0x586D4)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - 75),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    root = Path(__file__).resolve().parents[2]
    production = re.search(r'u32 func_1502B224\([^;{}]+\) \{\n.*?\n\}',
                           (root / 'conker/src/game_57FA0.c').read_text(), re.S).group(0)
    assert production == dict(candidates())['layout-1']
    output = root / 'conker/build/game-buffer-resource-loader'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
