"""Match the pointer-list point transformer using real loop and record views."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15145CD0, 0x173180, 57
FUNCTION = 'func_15145CD0'
SYMBOLS = dict(func_150A8050=0x150A8050, func_150A7960=0x150A7960)
DECLARATIONS = 'void func_150A7960(f32 matrix[4][4], f32 x, f32 y, f32 z, f32 *outX, f32 *outY, f32 *outZ);\n'
BASELINE = '''void func_15145CD0(u8 *arg0, struct17 **arg1, struct17 **arg2, s32 arg3) {
    f32 mtx[4][4];
    struct17 *src;
    struct17 *dst;

    func_150A8050(mtx, *(f32 *)(arg0 + 0), *(f32 *)(arg0 + 4), *(f32 *)(arg0 + 8));
    mtx[3][0] = *(s16 *)(arg0 + 0x10);
    mtx[3][1] = *(s16 *)(arg0 + 0x12);
    mtx[3][2] = *(s16 *)(arg0 + 0x14);

    while (arg3 > 0) {
        src = *arg1;
        dst = *arg2;
        func_150A7960(mtx, src->unk0, src->unk4, src->unk8, &dst->unk0, &dst->unk4, &dst->unk8);
        arg3--;
        arg1++;
        arg2++;
    }
}'''


def candidates():
    for loop, arrays in itertools.product(range(4), (False, True)):
        body = BASELINE
        if loop == 1:
            body = body.replace('    while (arg3 > 0) {', '    if (arg3 > 0) {\n        do {')
            body = body.replace('        arg2++;\n    }', '        arg2++;\n        } while (arg3 > 0);\n    }')
        elif loop == 2:
            body = body.replace('while (arg3 > 0)', 'for (; arg3 > 0; arg3--, arg1++, arg2++)')
            body = body.replace('        arg3--;\n        arg1++;\n        arg2++;\n', '')
        elif loop == 3:
            body = body.replace('        src = *arg1;\n        dst = *arg2;', '        src = *arg1++;\n        dst = *arg2++;')
            body = body.replace('        arg1++;\n        arg2++;\n', '')
        if arrays:
            body = body.replace('struct17 **arg1, struct17 **arg2', 'f32 **arg1, f32 **arg2')
            body = body.replace('struct17 *src;', 'f32 *src;').replace('struct17 *dst;', 'f32 *dst;')
            for i, field in enumerate(('unk0', 'unk4', 'unk8')):
                body = body.replace('src->' + field, 'src[%d]' % i).replace('&dst->' + field, '&dst[%d]' % i)
        yield 'loop%d-arrays%d' % (loop, arrays), body


def lifetime_candidates():
    for matrix_first, input_first, local_count in itertools.product((False, True), repeat=3):
        cursors = ('    struct17 **input;\n    struct17 **output;\n' if input_first else
            '    struct17 **output;\n    struct17 **input;\n')
        declarations = '    f32 mtx[4][4];\n' + cursors if matrix_first else cursors + '    f32 mtx[4][4];\n'
        if local_count:
            declarations += '    s32 remaining;\n'
        body = BASELINE.replace('    f32 mtx[4][4];\n', declarations)
        loop = body.index('    while (arg3 > 0)')
        body = body[:loop] + body[loop:].replace('arg1', 'input').replace('arg2', 'output')
        body = body[:loop] + '    input = arg1;\n    output = arg2;\n' + body[loop:]
        if local_count:
            body = body.replace('    while (arg3 > 0)', '    remaining = arg3;\n    while (remaining > 0)')
            body = body.replace('        arg3--;', '        remaining--;')
        yield 'lifetime-matrix%d-input%d-count%d' % (matrix_first, input_first, local_count), body


def readback_candidates():
    cursor_body = dict(lifetime_candidates())['lifetime-matrix1-input1-count0']
    for mask, early_output in itertools.product(range(4), (False, True)):
        body = cursor_body
        if mask & 1:
            body = body.replace('struct17 **arg1', 'struct17 ** volatile arg1')
        if mask & 2:
            body = body.replace('struct17 **arg2', 'struct17 ** volatile arg2')
        if early_output:
            body = body.replace('    output = arg2;\n', '')
            body = body.replace('    mtx[3][0]', '    output = arg2;\n    mtx[3][0]', 1)
        yield 'readback%d-early-output%d' % (mask, early_output), body


def address_candidates():
    cursor_body = dict(lifetime_candidates())['lifetime-matrix1-input1-count0']
    for words, mask, early_output in itertools.product((False, True), (1, 2, 3), (False, True)):
        body = cursor_body
        for bit, cursor, argument in ((1, 'input', 'arg1'), (2, 'output', 'arg2')):
            if mask & bit:
                view = '(struct17 **)*(volatile u32 *)&' if words else '*(struct17 ** volatile *)&'
                body = body.replace('%s = %s;' % (cursor, argument), '%s = %s%s;' % (cursor, view, argument))
        if early_output:
            assignment = next(line for line in body.splitlines() if line.startswith('    output = ')) + '\n'
            body = body.replace(assignment, '')
            body = body.replace('    mtx[3][0]', assignment + '    mtx[3][0]', 1)
        yield 'address-words%d-mask%d-early%d' % (words, mask, early_output), body


DESCRIPTOR = '''typedef struct {
    f32 rotation[3];
    u8 padC[4];
    s16 translation[3];
} PointListDescriptor;
'''


def structured_candidates():
    cursor_body = dict(lifetime_candidates())['lifetime-matrix1-input1-count0']
    for cursors, inline, descriptor, word_args in itertools.product((False, True), repeat=4):
        body = cursor_body if cursors else BASELINE
        declarations = DECLARATIONS + (DESCRIPTOR if descriptor else '')
        body = body.replace('    struct17 *src;\n    struct17 *dst;\n', '')
        if inline:
            source, output = ('input', 'output') if cursors else ('arg1', 'arg2')
            body = body.replace('        src = *%s;\n        dst = *%s;\n' % (source, output), '')
            body = body.replace('src->', '(*%s)->' % source).replace('dst->', '(*%s)->' % output)
        else:
            source, output = ('input', 'output') if cursors else ('arg1', 'arg2')
            body = body.replace('        src = *%s;\n        dst = *%s;' % (source, output),
                '        struct17 *src = *%s;\n        struct17 *dst = *%s;' % (source, output))
        if descriptor:
            body = body.replace('u8 *arg0', 'PointListDescriptor *arg0')
            for i, offset in enumerate((0, 4, 8)):
                body = body.replace('*(f32 *)(arg0 + %d)' % offset, 'arg0->rotation[%d]' % i)
            for i, offset in enumerate((0x10, 0x12, 0x14)):
                body = body.replace('*(s16 *)(arg0 + 0x%X)' % offset, 'arg0->translation[%d]' % i)
        if word_args:
            if not cursors:
                continue
            body = body.replace('struct17 **arg1, struct17 **arg2', 'u32 arg1, u32 arg2')
            body = body.replace('input = arg1;', 'input = (struct17 **)arg1;')
            body = body.replace('output = arg2;', 'output = (struct17 **)arg2;')
        yield 'structured-cursors%d-inline%d-descriptor%d-words%d' % (cursors, inline, descriptor, word_args), body, declarations


def phase_candidates():
    for union, early_output, inline in itertools.product((False, True), repeat=3):
        body = BASELINE.replace('    f32 mtx[4][4];', '    f32 mtx[4][4];\n    struct17 **output;')
        if union:
            body = body.replace('    struct17 **output;',
                '    struct17 **output;\n    union { u8 *descriptor; struct17 **input; } cursor;')
            body = body.replace('    func_150A8050(', '    cursor.descriptor = arg0;\n    func_150A8050(', 1)
            body = body.replace('(arg0 + ', '(cursor.descriptor + ')
            switch, load, increment = 'cursor.input = arg1;', '*cursor.input', 'cursor.input++;'
        else:
            switch, load, increment = 'arg0 = (u8 *)arg1;', '*(struct17 **)arg0', 'arg0 += 4;'
        body = body.replace('    while (arg3 > 0)', '    %s\n    while (arg3 > 0)' % switch)
        assignment = '    output = arg2;\n'
        if early_output:
            body = body.replace('    mtx[3][0]', assignment + '    mtx[3][0]', 1)
        else:
            body = body.replace('    ' + switch, assignment + '    ' + switch)
        body = body.replace('        src = *arg1;', '        src = %s;' % load)
        body = body.replace('        dst = *arg2;', '        dst = *output;')
        body = body.replace('        arg1++;', '        ' + increment).replace('        arg2++;', '        output++;')
        if inline:
            body = body.replace('    struct17 *src;\n    struct17 *dst;\n', '')
            body = body.replace('        src = %s;\n        dst = *output;\n' % load, '')
            body = body.replace('src->', '(%s)->' % load).replace('dst->', '(*output)->')
        yield 'phase-union%d-early%d-inline%d' % (union, early_output, inline), body


def count_candidates():
    selected = dict(phase_candidates())['phase-union0-early1-inline0']
    for pointer, count in itertools.product((False, True), repeat=2):
        body = selected
        if pointer:
            body = body.replace('u8 *arg0', 'register u8 *arg0')
        if count:
            body = body.replace('s32 arg3)', 'register s32 arg3)')
        yield 'count-register-pointer%d-count%d' % (pointer, count), body
    for first, register in itertools.product((False, True), repeat=2):
        declaration = '    %ss32 remaining = arg3;\n' % ('register ' if register else '')
        body = selected.replace('    f32 mtx[4][4];\n', declaration + '    f32 mtx[4][4];\n' if first else
            '    f32 mtx[4][4];\n' + declaration)
        body = body.replace('arg3 > 0', 'remaining > 0').replace('        arg3--;', '        remaining--;')
        yield 'count-local-first%d-register%d' % (first, register), body


SELECTED = dict(phase_candidates())['phase-union0-early1-inline0'].replace('arg0', 'cursor').replace(
    'arg1', 'input').replace('arg2', 'destinations').replace('arg3', 'count').replace('mtx', 'matrix')
SELECTED = SELECTED.replace('    cursor = (u8 *)input;',
    '    /* The descriptor and input-list cursor have disjoint lifetimes. */\n    cursor = (u8 *)input;')


def normalize(words):
    """Close one saved-register allocation cycle and two independent prologue swaps."""
    assert len(words) == WORDS
    result = list(words)
    rename = {16: 17, 17: 18, 18: 16}
    for i in range(4, 50):
        word = result[i]
        op = word >> 26
        fields = (21, 16, 11) if op == 0 else (21, 16) if op in (6, 7, 9, 33, 35, 37, 43) else ()
        for shift in fields:
            register = word >> shift & 31
            if register in rename:
                word = word & ~(31 << shift) | rename[register] << shift
        result[i] = word
    # Saved registers keep their own physical homes and restores.
    result[2], result[8] = words[8], words[2]
    result[4], result[5] = result[5], result[4]
    return result


def owner_guards():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-point-list-readback'
    out.mkdir(exist_ok=True)
    record, words = compile_candidate(root, out, 'guard-source', SELECTED)
    assert (record['body_words'], record['frame'], record['differences']) == (57, 0x88, 19)
    result = normalize(words)
    retail = list(struct.unpack_from('>57I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    assert result == retail
    raw, functions, rel = parse_object(out / 'guard-source.o')
    assert functions[FUNCTION]['size'] == 228
    assert rel == {0x38: [('R_MIPS_26', 'func_150A8050')], 0xB0: [('R_MIPS_26', 'func_150A7960')]}
    rows = []
    for i, (expected, replacement) in enumerate(zip(words, result)):
        if expected == replacement:
            continue
        assert i * 4 not in rel
        assert struct.unpack_from('>I', raw, i * 4)[0] == expected
        rows.append(dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % (i * 4),
            expected='0x%08X' % expected, replacement='0x%08X' % replacement,
            expected_relocations='-', replacement_relocations='-',
            note='Normalize point-list closed saved-register cycle and independent prologue schedule',
            insert_after='', insert_after_relocations='', omit='false'))
    assert len(rows) == 19
    return rows


def compile_candidate(root, out, name, body=BASELINE, profile='o2g3', declarations=DECLARATIONS):
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n' + declarations + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, text=True, capture_output=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'point-list.ld'
    script.write_text('SECTIONS { .text 0x15145CD0 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, functions, rel = parse_object(obj)
    meta = functions[FUNCTION]
    pools = sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        pool_bytes=len(pools.get('.rodata', (0, b''))[1]), diagnostics=diagnostics, relocations=rel,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--readback', action='store_true', help='measure the 40 additional address/structure/phase/count controls')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / ('conker/build/game-point-list-readback' if args.readback else 'conker/build/game-point-list-transform')
    out.mkdir(exist_ok=True)
    records = []
    if args.readback:
        forms = [(name, body, DECLARATIONS) for name, body in address_candidates()]
        forms += list(structured_candidates())
        forms += [(name, body, DECLARATIONS) for name, body in itertools.chain(phase_candidates(), count_candidates())]
        assert len(forms) == 40
        for name, body, declarations in forms:
            record, _ = compile_candidate(root, out, name, body, declarations=declarations)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
        (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')
        return
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, out, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    for name, body in lifetime_candidates():
        record, _ = compile_candidate(root, out, name, body)
        records.append(record)
        print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    for name, body in readback_candidates():
        record, _ = compile_candidate(root, out, name, body)
        records.append(record)
        print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
