"""Screen pointer versus O32 address-word cursors for the attachment walker."""

import json
import itertools
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


def main():
    root = Path(__file__).resolve().parents[2]
    conker = root / 'conker'
    output = conker / 'build/game-attachment-cursor'
    output.mkdir(exist_ok=True)
    source = (conker / 'src/game_1944C0.c').read_text()
    body = re.search(r'void func_15168E54\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
    for kind in ('s32', 'u32'):
        body = body.replace('    ' + kind + ' cur;', '    s8 *cur;')
        body = body.replace('    cur = (' + kind + ')arg0;', '    cur = arg0;')
        body = body.replace('*(volatile s8 *)(' + kind + ')cur', '*(volatile s8 *)cur')
        body = body.replace('    cur = (i << 3) + (' + kind + ')arg0;',
                            '    cur = (s8 *)((i << 3) + (s32)arg0);')
    body = body.replace('s32 opcode;', 's8 opcode;')
    variants = []
    for cursor in ('pointer', 's32', 'u32'):
        for opcode in ('s8', 's32'):
            candidate = body.replace('s8 opcode;', opcode + ' opcode;')
            if cursor != 'pointer':
                candidate = candidate.replace('s8 *cur;', cursor + ' cur;')
                candidate = candidate.replace('cur = arg0;', 'cur = (' + cursor + ')arg0;')
                candidate = candidate.replace('cur = (s8 *)((i << 3) + (s32)arg0);',
                                               'cur = (i << 3) + (' + cursor + ')arg0;')
            variants.append((cursor + '-' + opcode, candidate))
    for order in itertools.permutations(('s8 *cur;', 's32 i = 0;', 's8 opcode;')):
        candidate = body.replace('    s8 *cur;\n    s32 i = 0;\n    s8 opcode;',
                                 '\n'.join('    ' + line for line in order))
        variants.append(('order-' + '-'.join(line.split()[1].strip('*;') for line in order), candidate))
    variants.append(('declaration-init', body.replace('s8 *cur;', 's8 *cur = arg0;')
                     .replace('    cur = arg0;\n', '')))
    variants.append(('scoped-opcode', body.replace('    s8 opcode;\n', '')
                     .replace('        opcode = *(volatile s8 *)cur;',
                              '        s8 opcode = *(volatile s8 *)cur;', 1)))
    variants.append(('reverse-index-sum', body.replace('((i << 3) + (s32)arg0)',
                                                      '((s32)arg0 + (i << 3))')))
    for first in (False, True):
        for second in (False, True):
            candidate = body
            if first:
                candidate = candidate.replace('1 == opcode', 'opcode == 1')
            if second:
                candidate = candidate.replace('-0x24 == opcode', 'opcode == -0x24')
            variants.append(('comparison-' + str(int(first)) + str(int(second)), candidate))
    for name in ('cur', 'opcode', 'i'):
        variants.append(('register-' + name, re.sub(r'(^    )(s8|s32)( \*?' + name + r'\b)',
                                                  r'\1register \2\3', body, flags=re.M)))
    for access in ('(s8 *)((s32)arg0 + i * 8)', '(s8 *)arg0 + i * 8',
                   '(s8 *)arg0 + (i << 3)', '(s8 *)((s32)arg0 + (i << 3))'):
        variants.append(('cursor-expression-' + str(len(variants)),
                         body.replace('(s8 *)((i << 3) + (s32)arg0)', access)))
    variants.append(('signed-leaf-result', body))
    variants.append(('unsigned-leaf-result', body))
    for name, expression in (('xor-zero', '(opcode ^ 0)'), ('or-zero', '(opcode | 0)'),
                              ('add-zero', '(opcode + 0)'), ('sub-zero', '(opcode - 0)'),
                              ('wide-cast', '(s32)opcode')):
        candidate = body.replace('1 == opcode', '1 == ' + expression)
        candidate = candidate.replace('-0x24 == opcode', '-0x24 == ' + expression)
        candidate = candidate.replace('-0x21 != opcode', '-0x21 != ' + expression)
        variants.append((name, candidate))
    variants.append(('single-line', ' '.join(line.strip() for line in body.splitlines())))
    variants.append(('same-line-loop-update', body.replace(
        '            i++;\n            cur = (s8 *)((i << 3) + (s32)arg0);\n'
        '            opcode = *(volatile s8 *)cur;',
        '            i++; cur = (s8 *)((i << 3) + (s32)arg0); opcode = *(volatile s8 *)cur;')))
    variants.append(('gate-xor-zero', body.replace('if (*(volatile s8 *)cur != -0x21)',
                                                  'if ((*(volatile s8 *)cur != -0x21) ^ 0)')))
    types = ('typedef signed char s8; typedef unsigned char u8; typedef int s32; '
             'typedef unsigned int u32;\nvoid func_15168E34(s32 *, s32);\n')
    retail = list(struct.unpack_from('>45I', (conker / 'conker.us.bin').read_bytes(), 0x196304))
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x15168E54 : SUBALIGN(4) { *(.text) } }\n')
    records = []
    for name, candidate in variants:
        path = output / (name + '.c')
        obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
        declarations = types
        if name == 'signed-leaf-result':
            declarations = types.replace('void func_15168E34', 's32 func_15168E34')
        elif name == 'unsigned-leaf-result':
            declarations = types.replace('void func_15168E34', 'u32 func_15168E34')
        path.write_text(declarations + candidate + '\n')
        result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
            '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
            '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
            str(path.relative_to(conker))], cwd=conker, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stderr)
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
            '-e', 'func_15168E54', '--defsym=func_15168E34=0x15168E34',
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        words = functions['func_15168E54']
        size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        slot = words[:size] + [0] * max(0, 45 - size)
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
