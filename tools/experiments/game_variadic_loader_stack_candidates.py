"""Source-only nullable-output and stack-layout screening for the full loader."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = r'''void *func_1502B6BC(s32 *size, s32 count, s32 *relocated, s32 depth, ...) {
    va_list path;
    s32 fallbackSize;
    /* Retail leaves this undefined for zero depth or an unwritten lookup result. */
    u32 descriptor;
    u32 offset;
    s32 component;
    void *result;

    if (size == NULL) {
        size = &fallbackSize;
    }
    *size = 1;
    offset = (u32)D_AB1950;
    va_start(path, depth);
    if (depth != 0) {
        do {
            component = va_arg(path, s32);
            if (*size != 0) {
                offset += func_1502AC88(offset, component, &descriptor);
            }
            *size = descriptor & 0x0FFFFFFF;
        } while (--depth != 0);
    }
    va_end(path);
    if (*size != 0) {
        result = func_1502B350(offset, descriptor, size);
        if (*size != 0 && result != NULL) {
            count = func_1502B4A8(result, count);
        } else {
            count = 0;
        }
        if (relocated != NULL) {
            *relocated = count;
        }
    } else {
        result = NULL;
    }
    return result;
}'''


def candidates():
    """Keep the pre-match source fixed so screens survive production adoption."""
    body = BASELINE
    selection = '    if (size == NULL) {\n        size = &fallbackSize;\n    }'
    variants = [('baseline', body)]
    for name, expression in (('ternary-null', 'size == NULL ? &fallbackSize : size'),
                             ('ternary-nonnull', 'size != NULL ? size : &fallbackSize')):
        variants.append((name, body.replace(selection, '    size = ' + expression + ';')))
    for name, selection_body in (
            ('separate-if', '    if (size == NULL) {\n        target = &fallbackSize;\n'
             '    } else {\n        target = size;\n    }'),
            ('separate-ternary', '    target = size == NULL ? &fallbackSize : size;')):
        candidate = body.replace('    va_list path;', '    s32 *target;\n    va_list path;')
        candidate = candidate.replace(selection, selection_body)
        candidate = candidate.replace('*size = 1;', '*target = 1;')
        candidate = candidate.replace('if (*size', 'if (*target').replace('*size = descriptor', '*target = descriptor')
        candidate = candidate.replace('descriptor, size)', 'descriptor, target)')
        variants.append((name, candidate))
    separate = variants[-2][1]
    reversed_selection = ('    if (size != NULL) {\n        target = size;\n'
                          '    } else {\n        target = &fallbackSize;\n    }')
    variants.append(('separate-if-nonnull', separate.replace(
        '    if (size == NULL) {\n        target = &fallbackSize;\n'
        '    } else {\n        target = size;\n    }', reversed_selection)))
    variants.append(('separate-default', separate.replace(
        '    if (size == NULL) {\n        target = &fallbackSize;\n'
        '    } else {\n        target = size;\n    }',
        '    target = &fallbackSize;\n    if (size != NULL) {\n        target = size;\n    }')))
    for name, base in list(variants):
        if name in ('baseline', 'separate-if-nonnull', 'separate-default'):
            candidate = base.replace('    void *result;\n', '')
            candidate = candidate.replace('result = func_1502B350(', 'offset = (u32)func_1502B350(')
            candidate = candidate.replace('result != NULL', 'offset != 0')
            candidate = candidate.replace('func_1502B4A8(result, count)', 'func_1502B4A8((u32 *)offset, count)')
            candidate = candidate.replace('result = NULL;', 'offset = 0;').replace('return result;', 'return (void *)offset;')
            variants.append((name + '-reuse-offset', candidate))
    old = ('    va_list path;\n    s32 fallbackSize;\n'
           '    /* Retail leaves this undefined for zero depth or an unwritten lookup result. */\n'
           '    u32 descriptor;')
    locals_ = ('va_list path;', 's32 fallbackSize;', 'u32 descriptor;')
    bases = list(variants)
    for name, base in bases:
        for order in itertools.permutations(locals_):
            candidate = base.replace(old, '\n'.join('    ' + local for local in order))
            variants.append((name + '-order-' + '-'.join(local.split()[1].strip(';') for local in order), candidate))
    for name, base in bases:
        candidate = base.replace('    s32 component;\n', '')
        candidate = candidate.replace('        do {\n            component = va_arg(path, s32);',
                                     '        do {\n            s32 component = va_arg(path, s32);')
        variants.append((name + '-scoped-component', candidate))
    default = dict(bases)['separate-default']
    for name, local in (('offset', 'u32 offset;'), ('component', 's32 component;'),
                        ('result', 'void *result;')):
        candidate = default.replace('    u32 descriptor;', '    SWAP_LOCAL;')
        candidate = candidate.replace('    ' + local, '    u32 descriptor;')
        candidate = candidate.replace('    SWAP_LOCAL;', '    ' + local)
        comment = '    /* Retail leaves this undefined for zero depth or an unwritten lookup result. */\n'
        candidate = candidate.replace(comment, '')
        candidate = candidate.replace('    u32 descriptor;', comment + '    u32 descriptor;')
        variants.append(('separate-default-swap-descriptor-' + name, candidate))
    return variants


def main():
    root = Path(__file__).resolve().parents[2]
    conker = root / 'conker'
    output = conker / 'build/game-variadic-loader-stack'
    output.mkdir(exist_ok=True)
    source = (conker / 'src/game_57FA0.c').read_text()
    production = re.search(r'void \*func_1502B6BC\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
    variants = candidates()
    assert production == dict(variants)['separate-default-swap-descriptor-component']
    types = ('#include "stdarg.h"\ntypedef unsigned char u8; typedef int s32; '
             'typedef unsigned int u32;\n#define NULL ((void *)0)\n'
             'extern u8 D_AB1950[]; s32 func_1502AC88(u32,s32,u32 *);\n'
             'void *func_1502B350(u32,u32,s32 *); s32 func_1502B4A8(u32 *,s32);\n')
    retail = list(struct.unpack_from('>77I', (conker / 'conker.us.bin').read_bytes(), 0x58B6C))
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502B6BC : SUBALIGN(4) { *(.text) } }\n')
    records = []
    for name, candidate in variants:
        path = output / (name + '.c')
        obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
        path.write_text(types + candidate + '\n')
        result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
            '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
            '-I', 'include/libc', '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
            str(path.relative_to(conker))], cwd=conker, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stderr)
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
            '-e', 'func_1502B6BC', '--defsym=D_AB1950=0xAB1950',
            '--defsym=func_1502AC88=0x1502AC88', '--defsym=func_1502B350=0x1502B350',
            '--defsym=func_1502B4A8=0x1502B4A8', '-o', str(elf), str(obj)], check=True, capture_output=True)
        functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        words = functions['func_1502B6BC']
        size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        slot = words[:size] + [0] * max(0, 77 - size)
        differences = [(i * 4, f'{a:08X}', f'{b:08X}')
                       for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
        record = dict(name=name, body_words=size, frame=(-words[0]) & 0xFFFF,
                      real_differences=len(differences) + max(0, size - len(retail)),
                      differences=differences, diagnostics=result.stdout + result.stderr)
        records.append(record)
        print(name, size, hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
