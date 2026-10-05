"""Source-only scan and indexed-loop screening for the resource relocator."""

import json
import itertools
import re
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions


BASELINE = r'''s32 func_1502B4A8(u32 *entries, s32 count) {
    u32 *cursor;
    u32 base;
    s32 i;

    if (count == 0) {
        cursor = entries;
        do {
            count++;
            if (cursor[1] & 0x80000000) {
                break;
            }
            cursor += 2;
        } while (1);
    }
    base = (u32)entries;
    for (i = 0; i < count; i++) {
        entries[i * 2 + 1] &= 0x0FFFFFFF;
        if (entries[i * 2] == 0xFFFFFFFF || entries[i * 2 + 1] == 0) {
            entries[i * 2] = 0;
        } else {
            entries[i * 2] += base;
        }
    }
    return count;
}'''


def candidates():
    scan = '''        cursor = entries;
        do {
            count++;
            if (cursor[1] & 0x80000000) {
                break;
            }
            cursor += 2;
        } while (1);'''
    variants = []
    for name, replacement in (
            ('break', scan),
            ('boolean', '''        cursor = entries + count * 2;
        do {
            scanning = (cursor[1] & 0x80000000) == 0;
            count++;
            cursor += 2;
        } while (scanning);'''),
            ('post-index', '''        do {
            scanning = (entries[count * 2 + 1] & 0x80000000) == 0;
            count++;
        } while (scanning);'''),
            ('while-flag', '''        cursor = entries + count * 2;
        scanning = 1;
        while (scanning) {
            scanning = (cursor[1] & 0x80000000) == 0;
            count++;
            cursor += 2;
        }'''),
            ('while-done', '''        cursor = entries + count * 2;
        scanning = 0;
        while (!scanning) {
            scanning = (cursor[1] & 0x80000000) != 0;
            count++;
            cursor += 2;
        }'''),
            ('for-flag', '''        cursor = entries + count * 2;
        for (scanning = 1; scanning; count++) {
            scanning = (cursor[1] & 0x80000000) == 0;
            cursor += 2;
        }'''),
            ('while-index-flag', '''        scanning = 1;
        while (scanning) {
            scanning = (entries[count * 2 + 1] & 0x80000000) == 0;
            count++;
        }'''),
            ('while-index', '''        while ((entries[count * 2 + 1] & 0x80000000) == 0) {
            count++;
        }
        count++;'''),
            ('while-post-increment', '''        while ((entries[count++ * 2 + 1] & 0x80000000) == 0) {
        }'''),
            ('while-local-index', '''        i = count;
        while ((entries[i++ * 2 + 1] & 0x80000000) == 0) {
        }
        count = i;'''),
            ('peeled-boolean', '''        cursor = entries + count * 2;
        scanning = (cursor[1] & 0x80000000) == 0;
        cursor += 2;
        count++;
        while (scanning) {
            scanning = (cursor[1] & 0x80000000) == 0;
            count++;
            cursor += 2;
        }'''),
            ('peeled-index-cursor', '''        scanning = (entries[count * 2 + 1] & 0x80000000) == 0;
        count++;
        cursor = entries + count * 2;
        while (scanning) {
            scanning = (cursor[1] & 0x80000000) == 0;
            count++;
            cursor += 2;
        }'''),
            ('peeled-index-cursor-address', '''        scanning = (entries[count * 2 + 1] & 0x80000000) == 0;
        count++;
        cursor = (u32 *)((u32)entries + (u32)count * 8);
        while (scanning) {
            scanning = (cursor[1] & 0x80000000) == 0;
            count++;
            cursor += 2;
        }'''),
            ('while-assigned-boolean', '''        cursor = (u32 *)((u32)entries + (u32)count * 8);
        while ((scanning = (cursor[1] & 0x80000000) == 0)) {
            count++;
            cursor += 2;
        }
        count++;'''),
            ('while-boolean-pointer-condition', '''        cursor = (u32 *)((u32)entries + (u32)count * 8);
        while ((scanning = (cursor[1] & 0x80000000) == 0, cursor += 2, scanning)) {
            count++;
        }
        count++;'''),
            ('while-post-boolean', '''        while (!(entries[count++ * 2 + 1] & 0x80000000)) {
        }'''),
            ('while-comma', '''        while ((scanning = (entries[count * 2 + 1] & 0x80000000) == 0,
                count++, scanning)) {
        }'''),
            ('while-comma-increment', '''        while ((scanning = (entries[count * 2 + 1] & 0x80000000) == 0,
                ++count, scanning)) {
        }'''),
            ('while-comma-not', '''        while ((scanning = entries[count * 2 + 1] & 0x80000000,
                count++, !scanning)) {
        }'''),
            ('while-pointer-comma', '''        cursor = entries + count * 2;
        while ((scanning = (cursor[1] & 0x80000000) == 0,
                count++, cursor += 2, scanning)) {
        }'''),
            ('while-pointer-comma-not', '''        cursor = entries + count * 2;
        while ((scanning = cursor[1] & 0x80000000,
                count++, cursor += 2, !scanning)) {
        }'''),
            ('while-pointer-comma-advance-first', '''        cursor = entries + count * 2;
        while ((scanning = (cursor[1] & 0x80000000) == 0,
                cursor += 2, count++, scanning)) {
        }'''),
            ('while-post-pointer', '''        cursor = entries + count * 2;
        while ((cursor[1] & 0x80000000) == 0) {
            count++;
            cursor += 2;
        }
        count++;''')):
        base = BASELINE.replace(scan, replacement)
        if 'scanning' in replacement:
            base = base.replace('    s32 i;', '    s32 i;\n    s32 scanning;')
        for capture in (False, True):
            body = base
            if capture:
                body = body.replace('    s32 i;', '    u32 offset;\n    s32 i;')
                body = body.replace('        entries[i * 2 + 1] &=',
                                    '        offset = entries[i * 2];\n        entries[i * 2 + 1] &=')
                body = body.replace('if (entries[i * 2] ==', 'if (offset ==')
                body = body.replace('entries[i * 2] += base;', 'entries[i * 2] = offset + base;')
            for inline_base in (False, True):
                candidate = body
                if inline_base:
                    candidate = candidate.replace('    u32 base;\n', '').replace('    base = (u32)entries;\n', '')
                    candidate = candidate.replace(' + base;', ' + (u32)entries;').replace(' += base;', ' += (u32)entries;')
                variants.append((name + ('-capture' if capture else '') +
                                 ('-inline-base' if inline_base else ''), candidate))
    bases = dict(variants)
    for name in ('while-post-increment', 'peeled-boolean', 'while-pointer-comma', 'boolean'):
        body = bases[name]
        variants.append((name + '-register-count', body.replace('s32 count)', 'register s32 count)')))
        for type_ in ('u32', 'register s32', 'unsigned char'):
            if 's32 scanning;' in body:
                variants.append((name + '-flag-' + type_.replace(' ', '-'),
                                 body.replace('s32 scanning;', type_ + ' scanning;')))
        variants.append((name + '-unsigned-index', body.replace('count * 2', '(u32)count * 2')
                         .replace('count++ * 2', '(u32)count++ * 2')))
        variants.append((name + '-unsigned-increment', body.replace('count++;', 'count = (u32)count + 1;')
                         .replace('count++,', 'count = (u32)count + 1,')))
        variants.append((name + '-unsigned-formal', body.replace('s32 count)', 'u32 count)')
                         .replace('i < count;', 'i < (s32)count;')))
        if '        cursor = entries + count * 2;' in body:
            variants.append((name + '-scoped-address', body.replace('cursor = entries + count * 2;',
                'cursor = (u32 *)((u32)entries + (u32)count * 8);')))
            candidate = body.replace('        cursor = entries + count * 2;',
                '        cursor = (u32 *)((u32)entries + base);')
            candidate = candidate.replace('    if (count == 0) {',
                '    base = (u32)count * 8;\n    if (count == 0) {')
            variants.append((name + '-hoisted-scale', candidate))
            for label, expression in (
                    ('pointer', 'entries + count * 2'),
                    ('address', '(u32 *)((u32)entries + (u32)count * 8)')):
                candidate = body.replace('        cursor = entries + count * 2;\n', '')
                candidate = candidate.replace('    if (count == 0) {',
                    '    cursor = ' + expression + ';\n    if (count == 0) {')
                variants.append((name + '-hoisted-' + label, candidate))
    for name, body in list(variants):
        if name in ('peeled-boolean-scoped-address', 'peeled-boolean-hoisted-address',
                    'peeled-boolean-hoisted-scale', 'boolean-scoped-address',
                    'while-pointer-comma-scoped-address'):
            candidate = body.replace('    u32 *cursor;', '    u32 cursor;')
            candidate = candidate.replace('cursor = (u32 *)(', 'cursor = (')
            candidate = candidate.replace('cursor[1]', '*(u32 *)(cursor + 4)')
            candidate = candidate.replace('cursor += 2;', 'cursor += 8;')
            variants.append(('address-cursor-' + name, candidate))
    base = dict(variants)['peeled-boolean-scoped-address']
    old = '    u32 *cursor;\n    u32 base;\n    s32 i;\n    s32 scanning;'
    for order in itertools.permutations(('u32 *cursor;', 'u32 base;', 's32 i;', 's32 scanning;')):
        variants.append(('declarations-' + '-'.join(x.split()[-1].strip('*;') for x in order),
                         base.replace(old, '\n'.join('    ' + x for x in order))))
    for name, body in list(variants):
        if name in ('break', 'boolean', 'post-index', 'while-index', 'while-post-increment',
                    'peeled-boolean-scoped-address', 'peeled-boolean-hoisted-scale',
                    'while-pointer-comma-scoped-address', 'while-assigned-boolean'):
            candidate = body.replace('    u32 *cursor;',
                '    typedef struct { u32 offset; u32 length; } Entry;\n'
                '    Entry *records;\n    Entry *cursor;')
            candidate = candidate.replace('    if (count == 0) {',
                '    records = (Entry *)entries;\n    if (count == 0) {')
            candidate = candidate.replace('cursor = entries;', 'cursor = records;')
            candidate = candidate.replace('cursor = entries + count * 2;', 'cursor = records + count;')
            candidate = candidate.replace('cursor = (u32 *)(', 'cursor = (Entry *)(')
            candidate = candidate.replace('cursor[1]', 'cursor->length').replace('cursor += 2;', 'cursor++;')
            candidate = candidate.replace('entries[count * 2 + 1]', 'records[count].length')
            candidate = candidate.replace('entries[count++ * 2 + 1]', 'records[count++].length')
            candidate = candidate.replace('entries[i * 2 + 1]', 'records[i].length')
            candidate = candidate.replace('entries[i * 2]', 'records[i].offset')
            variants.append(('record-view-' + name, candidate))
    for name, body in list(variants):
        if name in ('record-view-while-post-increment', 'record-view-while-index'):
            candidate = body.replace('records[i].length', 'entries[i * 2 + 1]')
            candidate = candidate.replace('records[i].offset', 'entries[i * 2]')
            variants.append(('typed-scan-' + name.removeprefix('record-view-'), candidate))
    body = dict(variants)['typed-scan-while-post-increment']
    variants.append(('typed-scan-scoped-records', body.replace('    records = (Entry *)entries;\n', '')
                     .replace('    if (count == 0) {', '    if (count == 0) {\n        records = (Entry *)entries;')))
    candidate = body.replace('    Entry *records;\n', '').replace('    records = (Entry *)entries;\n', '')
    candidate = candidate.replace('records[count++].length', '((Entry *)entries)[count++].length')
    variants.append(('typed-scan-inline-records', candidate))
    variants.append(('typed-scan-inline-records-no-cursor', candidate.replace('    Entry *cursor;\n', '')))
    base = variants[-1][1]
    for name, before, after in (
            ('double-first', 'i * 2', '2 * i'),
            ('shift-index', 'i * 2', '(i << 1)'),
            ('reverse-bound', 'i < count', 'count > i'),
            ('preincrement', 'i++)', '++i)'),
            ('register-index', '    s32 i;', '    register s32 i;'),
            ('unsigned-index', '    s32 i;', '    u32 i;'),
            ('capture-offset', '        entries[i * 2 + 1] &=',
             '        offset = entries[i * 2];\n        entries[i * 2 + 1] &=')):
        body = base.replace(before, after)
        if name == 'unsigned-index':
            body = body.replace('i < count', '(s32)i < count')
        if name == 'capture-offset':
            body = body.replace('    s32 i;', '    s32 i;\n    u32 offset;')
            body = body.replace('if (entries[i * 2] ==', 'if (offset ==')
            body = body.replace('entries[i * 2] += base;', 'entries[i * 2] = offset + base;')
        variants.append(('bulk-' + name, body))
    candidate = base.replace('    for (i = 0; i < count; i++) {',
        '    if (count > 0) {\n    for (i = 0; i != count; i++) {')
    candidate = candidate.replace('    return count;', '    }\n    return count;')
    variants.append(('bulk-gated-not-equal', candidate))
    candidate = base.replace('    u32 base;', '    u32 *cursor;\n    u32 base;')
    candidate = candidate.replace('    for (i = 0; i < count; i++) {',
                                  '    for (i = 0; i < count; i++) {\n        cursor = entries + i * 2;')
    candidate = candidate.replace('entries[i * 2 + 1]', 'cursor[1]').replace('entries[i * 2]', 'cursor[0]')
    variants.append(('bulk-local-cursor', candidate))
    variants.append(('bulk-local-cursor-address', candidate.replace('cursor = entries + i * 2;',
                    'cursor = (u32 *)((u32)entries + (u32)i * 8);')))
    for name in ('Entry', 'ResourceRelocationEntry57FA0', 'ResourceEntry', 'struct124'):
        variants.append(('named-tag-' + name, base.replace('typedef struct {', 'typedef struct ' + name + ' {')))
    return variants


def compile_candidate(root, output, name, source):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    path.write_text('typedef int s32; typedef unsigned int u32;\n' + source + '\n')
    result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
        '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
        '-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)),
        str(path.relative_to(conker))], cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    script = output / 'slot.ld'
    script.write_text('SECTIONS { .text 0x1502B4A8 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
        '-e', 'func_1502B4A8', '-o', str(elf), str(obj)], check=True, capture_output=True)
    functions, _, _ = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
    words = functions['func_1502B4A8']
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, 72 - size)
    retail = struct.unpack_from('>72I', (conker / 'conker.us.bin').read_bytes(), 0x58958)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}')
                   for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    record = dict(name=name, body_words=size,
                  frame=(-words[0]) & 0xFFFF if words[0] >> 16 == 0x27BD else 0,
                  real_differences=len(differences) + max(0, size - len(retail)),
                  differences=differences, diagnostics=result.stdout + result.stderr)
    return record, slot


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix', default='')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    production = re.search(r's32 func_1502B4A8\([^;{}]+\) \{\n.*?\n\}',
        (root / 'conker/src/game_57FA0.c').read_text(), re.S).group(0)
    assert production == dict(candidates())['named-tag-ResourceRelocationEntry57FA0']
    output = root / 'conker/build/game-offset-relocator'
    output.mkdir(exist_ok=True)
    records = []
    for name, candidate in candidates():
        if not name.startswith(args.prefix):
            continue
        record, _ = compile_candidate(root, output, name, candidate)
        records.append(record)
        print(name, record['body_words'], record['frame'], record['real_differences'], flush=True)
    report = 'screen.json' if not args.prefix else 'screen-' + args.prefix + '.json'
    (output / report).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
