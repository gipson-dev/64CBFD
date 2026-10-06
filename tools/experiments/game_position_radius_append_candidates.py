"""Recover the signed-count append and its four fresh output-base reads."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BODY = '''void func_1508B20C(f32 x, f32 y, f32 z, f32 radius) {
    u8 *base;
    s32 index;

    base = (u8 *)D_800D23B0;
    if (base != NULL) {
        index = *(s8 *)(base + 0x1745);
        if (index < 8) {
            *(s8 *)(base + 0x1745) = index + 1;
            *(s16 *)((u8 *)D_800D23B0 + index * 12 + 0x174C) = (s16)(s32)x;
            *(s16 *)((u8 *)D_800D23B0 + index * 12 + 0x174E) = (s16)(s32)y;
            *(s16 *)((u8 *)D_800D23B0 + index * 12 + 0x1750) = (s16)(s32)z;
            *(f32 *)((u8 *)D_800D23B0 + index * 12 + 0x1748) = radius * radius;
        }
    }
}'''
PLACEHOLDER = '''s32 func_1508B20C() {
    return 0;
}'''


def replace(body, before, after, count=1):
    if body.count(before) != count:
        raise ValueError('position/radius anchor no longer binds: ' + before)
    return body.replace(before, after)


def candidates():
    forms = [('placeholder', PLACEHOLDER)]
    for access in ('ordinary', 'volatile', 'cached'):
        for kind in ('s32', 's8', 'u8'):
            for cast in ('word', 'half'):
                body = replace(BODY, '    s32 index;', '    ' + kind + ' index;')
                if access == 'volatile':
                    body = replace(body, '(u8 *)D_800D23B0 + index',
                                   '(u8 *)*(volatile s32 *)&D_800D23B0 + index', 4)
                elif access == 'cached':
                    body = replace(body, '(u8 *)D_800D23B0 + index', 'base + index', 4)
                if cast == 'half':
                    body = replace(body, '(s16)(s32)', '(s16)', 3)
                forms.append((f'{access}-{kind}-{cast}', body))
    for name, before, after in (
            ('unsigned-load-negative-control', 'index = *(s8 *)', 'index = *(u8 *)'),
            ('lower-bound-negative-control', 'if (index < 8)', 'if (index >= 0 && index < 8)'),
            ('wrong-stride-negative-control', 'index * 12', 'index * 8'),
            ('unsquared-negative-control', 'radius * radius', 'radius')):
        forms.append((name, BODY.replace(before, after)))
    for name, body in (
            ('index-declared-first', replace(BODY, '    u8 *base;\n    s32 index;', '    s32 index;\n    u8 *base;')),
            ('integer-base', replace(replace(BODY, '    u8 *base;', '    u32 base;'),
                                     'base = (u8 *)D_800D23B0;', 'base = (u32)D_800D23B0;')),
            ('unretained-base', replace(replace(BODY, '    u8 *base;\n', ''),
                                       '    base = (u8 *)D_800D23B0;\n', '').replace('base', '(u8 *)D_800D23B0')),
            ('cached-byte-offset', replace(BODY, '    s32 index;', '    s32 index;\n    s32 offset;')
             .replace('            *(s8 *)(base + 0x1745) = index + 1;',
                      '            *(s8 *)(base + 0x1745) = index + 1;\n            offset = index * 12;')
             .replace('index * 12 +', 'offset +')),
            ('literal-index-increment', replace(BODY, '*(s8 *)(base + 0x1745) = index + 1;',
                                               '(*(s8 *)(base + 0x1745))++;'))):
        forms.append((name, body))
    increment = dict(forms)['literal-index-increment']
    for name, body in (
            ('increment-byte-index', replace(increment, '    s32 index;', '    s8 index;')),
            ('increment-unsigned-word-index', replace(increment, '    s32 index;', '    u32 index;')),
            ('postincrement-capture', replace(increment, '(*(s8 *)(base + 0x1745))++;',
                                             'index = (*(s8 *)(base + 0x1745))++;')),
            ('inline-count-guard', replace(replace(increment, '        index = *(s8 *)(base + 0x1745);\n', ''),
                                          'if (index < 8)', 'if (*(s8 *)(base + 0x1745) < 8)')
             .replace('(*(s8 *)(base + 0x1745))++;', 'index = (*(s8 *)(base + 0x1745))++;')),
            ('increment-early-return', replace(replace(increment, '        if (index < 8) {',
                    '        if (index >= 8) {\n            return;\n        }\n        {'),
                    '    if (base != NULL) {', '    if (base == NULL) return;\n    {')),
            ('increment-preincrement-capture', replace(increment, '(*(s8 *)(base + 0x1745))++;',
                                                     'index = ++(*(s8 *)(base + 0x1745)) - 1;'))):
        forms.append((name, body))
    return forms


SELECTED = dict(candidates())['inline-count-guard']


def compile_candidate(root, output, name, body, no_unroll=False):
    conker = root / 'conker'
    source, obj, elf = [output / (name + suffix) for suffix in ('.c', '.o', '.elf')]
    source.write_text('#include <ultra64.h>\nextern s32 D_800D23B0;\n\n' + body + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', '-woff', '649,838']
    for include in ('.', 'include', 'include/2.0L', 'include/2.0L/PR', 'include/libc'):
        command += ['-I', include]
    command += ['-mips2', '-o32', '-O2', '-g3']
    if no_unroll:
        command += ['-Wo,-loopunroll,0']
    command += ['-o', str(obj.relative_to(conker)), str(source.relative_to(conker))]
    result = subprocess.run(command, cwd=conker, capture_output=True, text=True, check=True)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1508B20C : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1508B20C',
                    '--defsym=D_800D23B0=0x800D23B0', '-o', str(elf), str(obj)], capture_output=True, check=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1508B20C']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 39 - size)
    retail = list(struct.unpack_from('>39I', (conker / 'conker.us.bin').read_bytes(), 0xB86BC))
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, body_words=size, real_differences=len(differences) + max(0, size - 39),
                differences=differences, diagnostics=result.stdout + result.stderr), slot


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-position-radius-append'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
