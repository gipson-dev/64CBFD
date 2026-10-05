"""Resource table-range DMA and offset-fixup source screening at retail addresses."""

import json
import itertools
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = '''u32 *func_1502AF04(u32 base, void *buffer, u32 component, u32 count) {
    u32 address;
    u8 *aligned;
    u32 i;

    component *= 8;
    address = base + component;
    aligned = (u8 *)(((u32)buffer + 8) & ~0xF);
    func_10004514(address & ~0xF, aligned, ((address & 0xE) + count * 8 + 15) & ~0xF, 1);
    for (i = 0; i < count; i++) {
        ((u32 *)(aligned + (address & 0xF)))[i * 2] += base;
    }
    return (u32 *)(aligned + (address & 0xF));
}'''

PLACEHOLDER = '''s32 func_1502AF04() {
    return 0;
}'''


def candidates():
    forms = [('baseline', BASELINE)]
    local = BASELINE.replace('    component *= 8;\n    address = base + component;',
                             '    address = base + component * 8;')
    forms.append(('local-component', local))
    for label, body in list(forms):
        forms.append((label + '-signed-count', body.replace('u32 count)', 's32 count)')
                      .replace('    u32 i;', '    s32 i;')))
        forms.append((label + '-integer-buffer', body.replace('void *buffer', 'u32 buffer')
                      .replace('(u32)buffer', 'buffer')))
        forms.append((label + '-swapped-locals', body.replace('    u32 address;\n    u8 *aligned;',
                                                           '    u8 *aligned;\n    u32 address;')))
        forms.append((label + '-register-aligned', body.replace('    u8 *aligned;', '    register u8 *aligned;')))
    for label, body in list(forms):
        pairs = re.sub(r'    (u32|s32) i;', r'    \1 i;\n    u32 *pairs;', body)
        pairs = pairs.replace('    for (i =', '    pairs = (u32 *)(aligned + (address & 0xF));\n    for (i =')
        pairs = pairs.replace('((u32 *)(aligned + (address & 0xF)))[i * 2]', 'pairs[i * 2]')
        pairs = pairs.replace('return (u32 *)(aligned + (address & 0xF));', 'return pairs;')
        if pairs != body:
            forms.append((label + '-pairs-local', pairs))
    for label, body in list(forms):
        if label.endswith('-pairs-local'):
            continue
        entry = body.replace('    u32 address;',
            '    typedef struct TableRangePair57FA0 { u32 offset; u32 descriptor; } Entry;\n    u32 address;')
        entry = entry.replace('((u32 *)(aligned + (address & 0xF)))[i * 2]',
                              '((Entry *)(aligned + (address & 0xF)))[i].offset')
        forms.append((label + '-entry', entry))
    entry = dict(forms)['baseline-entry']
    integer_sum = entry.replace('aligned + (address & 0xF)', '(u32)aligned + (address & 0xF)')
    forms.append(('entry-integer-sum', integer_sum))
    for label, body in (('entry', entry), ('integer-sum', integer_sum)):
        for mask in range(1, 8):
            candidate = body
            for i, decl in enumerate(('u32 address;', 'u8 *aligned;', 'u32 i;')):
                if mask & (1 << i):
                    candidate = candidate.replace('    ' + decl, '    register ' + decl)
            forms.append((label + '-register-' + str(mask), candidate))
        original = '    u32 address;\n    u8 *aligned;\n    u32 i;'
        for index, order in enumerate(itertools.permutations(('u32 address;', 'u8 *aligned;', 'u32 i;'))):
            forms.append((label + '-layout-' + str(index),
                          body.replace(original, '\n'.join('    ' + decl for decl in order))))
    integer_aligned = integer_sum.replace('    u8 *aligned;', '    u32 aligned;')
    integer_aligned = integer_aligned.replace('aligned = (u8 *)(', 'aligned = (')
    integer_aligned = integer_aligned.replace('~0xF, aligned,', '~0xF, (void *)aligned,')
    forms.append(('entry-integer-aligned', integer_aligned))
    forms.append(('integer-sum-signed-index', integer_sum.replace('    u32 i;', '    s32 i;')))
    forms.append(('integer-sum-signed-address', integer_sum.replace('    u32 address;', '    s32 address;')))
    for kind in ('u8 *', 'u32 *', 'Entry *'):
        pointer = integer_sum.replace('    u32 address;', '    ' + kind + 'address;')
        pointer = pointer.replace('address = base + component;', 'address = (' + kind + ')(base + component);')
        pointer = pointer.replace('address &', '(u32)address &')
        forms.append(('integer-sum-address-' + kind.replace(' *', ''), pointer))
    for label, before, after in (
            ('combined-component', '    component *= 8;\n    address = base + component;',
             '    address = base + (component *= 8);'),
            ('shift-component', 'component *= 8;', 'component <<= 3;'),
            ('address-first-argument', 'func_10004514(address & ~0xF,',
             'func_10004514((address = base + component) & ~0xF,'),
            ('preincrement-index', 'i++)', '++i)'),
            ('explicit-offset-assignment', '[i].offset += base;', '[i].offset = ((Entry *)((u32)aligned + (address & 0xF)))[i].offset + base;')):
        forms.append(('integer-sum-' + label, integer_sum.replace(before, after)))
    for name in ('tableAddress', 'sp28', 'offset', 'rom', 'start'):
        forms.append(('integer-sum-name-' + name, re.sub(r'\baddress\b', name, integer_sum)))
    unsafe = dict(forms)['integer-sum-address-first-argument']
    # The first trial assigns address while another call argument reads it: reject it.
    safe = unsafe.replace('((address & 0xE)', '(((base + component) & 0xE)')
    forms.append(('argument-address-recomputed-length', safe))
    selected = safe.replace('    address = base + component;\n', '')
    selected = selected.replace('    func_10004514(',
        '    /* Keep the saved-address assignment independent of the length argument. */\n    func_10004514(')
    forms.append(('argument-address-no-early-assignment', selected))
    length_local = unsafe.replace('    u32 i;', '    u32 i;\n    u32 length;')
    length_local = length_local.replace('    func_10004514(',
        '    length = ((address & 0xE) + count * 8 + 15) & ~0xF;\n    func_10004514(')
    length_local = length_local.replace('aligned, ((address & 0xE) + count * 8 + 15) & ~0xF,', 'aligned, length,')
    forms.append(('argument-address-captured-length', length_local))
    forms.append(('placeholder', PLACEHOLDER))
    return forms


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    prefix = ('typedef int s32; typedef unsigned int u32; typedef unsigned char u8;\n'
              's32 func_10004514(u32, void *, u32, s32);\n')
    path.write_text(prefix + source + '\n')
    result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
        '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
        '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
        str(path.relative_to(conker))], cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502AF04 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
        '-e', 'func_1502AF04', '--defsym=func_10004514=0x10004514',
        '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502AF04']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 71 - size)
    retail = struct.unpack_from('>71I', (conker / 'conker.us.bin').read_bytes(), 0x583B4)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - 71),
                  differences=differences, diagnostics=result.stdout + result.stderr,
                  rejected_unsequenced_arguments=name=='integer-sum-address-first-argument')
    return record, slot


def main():
    root = Path(__file__).resolve().parents[2]
    production = re.search(r'u32 \*func_1502AF04\([^;{}]+\) \{\n.*?\n\}',
                           (root / 'conker/src/game_57FA0.c').read_text(), re.S).group(0)
    assert production == dict(candidates())['argument-address-no-early-assignment']
    output = root / 'conker/build/game-table-range'
    output.mkdir(exist_ok=True)
    records = []
    for name, source in candidates():
        record, _ = compile_candidate(root, output, name, source)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
