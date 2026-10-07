"""Recover the dual fixed/float matrix point-list wrapper and its lazy reads."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_point_list_transform_candidates import DECLARATIONS as POINT_DECLARATIONS
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15145EA4, 0x173354, 117
FUNCTION = 'func_15145EA4'
SYMBOLS = dict(guMtxL2F=0x151EFEB8, func_150A7960=0x150A7960,
    func_15142314=0x15142314, D_800C3E90=0x800C3E90)
DECLARATIONS = POINT_DECLARATIONS + '''void func_15142314(u8 *matrix, s32 index, f32 *output);
extern u8 D_800C3E90;
'''


def source(loop=0, condition=0, arrays=False, inverse=False):
    point_type = 'f32' if arrays else 'struct17'
    src = ['point[%d]' % i if arrays else 'point->' + field
        for i, field in enumerate(('unk0', 'unk4', 'unk8'))]
    dst = ['&destination[%d]' % i if arrays else '&destination->' + field
        for i, field in enumerate(('unk0', 'unk4', 'unk8'))]
    nonzero = 'point != 0 && (%s != 0.0f || %s != 0.0f || %s != 0.0f)' % tuple(src)
    zero = 'point == 0 || (%s == 0.0f && %s == 0.0f && %s == 0.0f)' % tuple(src)
    coordinates = list(src)
    declaration = ''
    if condition >= 2:
        declaration = '    f32 x;\n'
        nonzero = nonzero.replace(src[0] + ' !=', '(x = %s) !=' % src[0])
        zero = zero.replace(src[0] + ' ==', '(x = %s) ==' % src[0])
        coordinates[0] = 'x'
    predicate = zero if condition % 2 else nonzero
    fallback = 'func_15142314(matrix, 0, (f32 *)*destinations);'

    def block(transform_matrix):
        transform = ('destination = *destinations;\n'
            '                func_150A7960(%s, %s, %s);') % (
                transform_matrix, ', '.join(coordinates), ', '.join(dst))
        first, second = (fallback, transform) if condition % 2 else (transform, fallback)
        body = ('''            point = *input;
            if (%s) {
                %s
            } else {
                %s
            }
            count--;
            input++;
            destinations++;''') % (predicate, first, second)
        if loop == 0:
            return '        while (count > 0) {\n' + body + '\n        }\n'
        if loop == 1:
            return '        if (count > 0) {\n            do {\n' + body + '\n            } while (count > 0);\n        }\n'
        if loop == 2:
            return ('        for (; count > 0; count--, input++, destinations++) {\n' +
                body.replace('            count--;\n            input++;\n            destinations++;', '') + '\n        }\n')
        return '        if (count <= 0) return;\n        do {\n' + body + '\n        } while (count > 0);\n'

    fixed = '        guMtxL2F(converted, (Mtx *)matrix);\n' + block('converted')
    floating = block('(f32 (*)[4])matrix')
    first, second = (floating, fixed) if inverse else (fixed, floating)
    return ('''void func_15145EA4(%s **input, %s **destinations, u8 *matrix, s32 count) {
    f32 converted[4][4];
    %s *point;
    %s *destination;
%s
    if (D_800C3E90 %s 0) {
%s    } else {
%s    }
}''') % (point_type, point_type, point_type, point_type, declaration,
        '==' if inverse else '!=', first, second)


BASELINE = source()

PROTOTYPE = 'void func_15145EA4(struct17 **inputArgument, struct17 **destinationArgument, u8 *matrix, s32 count);'
SELECTED = '''void func_15145EA4(struct17 **inputArgument, struct17 **destinationArgument, u8 *matrix, s32 count) {
    f32 x;
    f32 converted[4][4];
    struct17 **input;
    struct17 **destinations;
    struct17 *point;
    struct17 *destination;

    if (D_800C3E90 != 0) {
        guMtxL2F(converted, (Mtx *)matrix);
        if (count > 0) {
            input = inputArgument;
            destinations = destinationArgument;
            do {
                point = *input;
                if (point != 0 && ((x = point->unk0) != 0.0f || point->unk4 != 0.0f || point->unk8 != 0.0f)) {
                    destination = *destinations;
                    func_150A7960(converted, x, point->unk4, point->unk8, &destination->unk0, &destination->unk4, &destination->unk8);
                } else {
                    func_15142314(matrix, 0, (f32 *)*destinations);
                }
                count--;
                input++;
                destinations++;
            } while (count > 0);
        }
    } else {
        if (count > 0) {
            input = inputArgument;
            destinations = destinationArgument;
            do {
                point = *input;
                if (point != 0 && ((x = point->unk0) != 0.0f || point->unk4 != 0.0f || point->unk8 != 0.0f)) {
                    destination = *destinations;
                    func_150A7960((f32 (*)[4])matrix, x, point->unk4, point->unk8, &destination->unk0, &destination->unk4, &destination->unk8);
                } else {
                    func_15142314(matrix, 0, (f32 *)*destinations);
                }
                count--;
                input++;
                destinations++;
            } while (count > 0);
        }
    }
}'''


def normalize(words):
    """Close one GP cycle and save permutation; commute two equality operands."""
    assert len(words) == WORDS
    result = list(words)
    rename = {17: 18, 18: 17}
    for i in range(3, 109):
        if i == 7:
            continue
        word, op = result[i], result[i] >> 26
        fields = (21, 16, 11) if op == 0 else (21, 16) if op in (6, 7, 9, 35, 43) else ()
        for shift in fields:
            register = word >> shift & 31
            if register in rename:
                word = word & ~(31 << shift) | rename[register] << shift
        result[i] = word
    result[2], result[7] = words[7], words[2]
    for i in (30, 75):
        word = result[i]
        assert word == 0x46140032
        fs, ft = word >> 11 & 31, word >> 16 & 31
        result[i] = word & ~((31 << 11) | (31 << 16)) | fs << 16 | ft << 11
    return result


def owner_guards():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-matrix-list-transform'
    record, words = compile_candidate(root, out, 'guard-source', SELECTED)
    assert (record['body_words'], record['frame'], record['differences']) == (117, 0xA0, 19)
    retail = list(struct.unpack_from('>117I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    result = normalize(words)
    assert result == retail
    raw, functions, rel = parse_object(out / 'guard-source.o')
    assert functions[FUNCTION]['size'] == 468
    assert rel == {0x30: [('R_MIPS_HI16', 'D_800C3E90')], 0x34: [('R_MIPS_LO16', 'D_800C3E90')],
        0x48: [('R_MIPS_26', 'guMtxL2F')], 0xD4: [('R_MIPS_26', 'func_150A7960')],
        0xE4: [('R_MIPS_26', 'func_15142314')], 0x188: [('R_MIPS_26', 'func_150A7960')],
        0x198: [('R_MIPS_26', 'func_15142314')]}
    rows = []
    for i, (expected, replacement) in enumerate(zip(words, result)):
        if expected == replacement:
            continue
        assert i * 4 not in rel and struct.unpack_from('>I', raw, i * 4)[0] == expected
        rows.append(dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % (i * 4),
            expected='0x%08X' % expected, replacement='0x%08X' % replacement,
            expected_relocations='-', replacement_relocations='-',
            note='Normalize matrix-list closed GP cycle, independent save order and equality operand order',
            insert_after='', insert_after_relocations='', omit='false'))
    assert len(rows) == 19
    return rows


def candidates():
    for loop, condition, arrays, inverse in itertools.product(range(4), range(4), (False, True), (False, True)):
        yield 'loop%d-condition%d-arrays%d-inverse%d' % (loop, condition, arrays, inverse), source(loop, condition, arrays, inverse)


def lifetime_candidates():
    for mask, matrix_first, placement, local_count in itertools.product(range(1, 4), (False, True), range(4), (False, True)):
        body = source(loop=1)
        declarations = ''
        assignments = []
        for bit, name, argument in ((1, 'input', 'inputArgument'), (2, 'destinations', 'destinationArgument')):
            if mask & bit:
                body = body.replace('struct17 **' + name + ',', 'struct17 **' + argument + ',', 1)
                declarations += '    struct17 **%s;\n' % name
                assignments.append((name, '        %s = %s;\n' % (name, argument)))
        matrix = '    f32 converted[4][4];\n'
        body = body.replace(matrix, matrix + declarations if matrix_first else declarations + matrix, 1)
        if local_count:
            body = body.replace('s32 count)', 's32 countArgument)')
            body = body.replace('    struct17 *point;', '    s32 count = countArgument;\n    struct17 *point;')
        if placement == 0:
            body = body.replace('        if (count > 0)', ''.join(line for _, line in assignments) + '        if (count > 0)')
        elif placement == 1:
            body = body.replace('        if (count > 0) {\n', ''.join(line for name, line in assignments if name == 'input') +
                '        if (count > 0) {\n' + ''.join(line for name, line in assignments if name == 'destinations'))
        elif placement == 2:
            body = body.replace('        if (count > 0) {\n', '        if (count > 0) {\n' + ''.join(line for _, line in assignments))
        else:
            for n in range(2):
                body = body.replace('        if (count > 0) {\n', '        if (count > 0) goto transform%d;\n'
                    '        return;\ntransform%d:\n        {\n' % (n, n) + ''.join(line for _, line in assignments), 1)
        yield 'lifetime-mask%d-matrix%d-placement%d-count%d' % (mask, matrix_first, placement, local_count), body


def view_candidates():
    base = dict(lifetime_candidates())['lifetime-mask3-matrix1-placement2-count0']
    for inline, scoped, order, arrays in itertools.product(range(4), (False, True), (False, True), (False, True)):
        body = base
        if inline & 1:
            body = body.replace('    struct17 *point;\n', '').replace('            point = *input;\n', '')
            body = body.replace('point !=', '*input !=').replace('point->', '(*input)->')
        elif scoped:
            body = body.replace('    struct17 *point;\n', '').replace('            point = *input;', '            struct17 *point = *input;')
        if inline & 2:
            body = body.replace('    struct17 *destination;\n', '').replace('                destination = *destinations;\n', '')
            body = body.replace('destination->', '(*destinations)->')
        elif scoped:
            body = body.replace('    struct17 *destination;\n', '').replace('                destination = *destinations;',
                '                struct17 *destination = *destinations;')
        if order:
            cursors = '    struct17 **input;\n    struct17 **destinations;\n'
            body = body.replace('    f32 converted[4][4];\n' + cursors, cursors + '    f32 converted[4][4];\n')
        if arrays:
            body = body.replace('struct17', 'f32')
            for i, field in enumerate(('unk0', 'unk4', 'unk8')):
                body = body.replace('->' + field, '[%d]' % i)
        yield 'view-inline%d-scoped%d-order%d-arrays%d' % (inline, scoped, order, arrays), body


def scalar_candidates():
    for inline, mask, declarations_first in itertools.product((0, 2), range(1, 8), (False, True)):
        body = dict(view_candidates())['view-inline%d-scoped0-order0-arrays0' % inline]
        declarations = ''.join('    f32 %s;\n' % axis for i, axis in enumerate('xyz') if mask >> i & 1)
        matrix = '    f32 converted[4][4];\n'
        body = body.replace(matrix, declarations + matrix if declarations_first else matrix + declarations, 1)
        for i, (axis, field) in enumerate(zip('xyz', ('unk0', 'unk4', 'unk8'))):
            if mask >> i & 1:
                body = body.replace('point->' + field + ' !=', '(%s = point->%s) !=' % (axis, field))
                if i == 0:
                    body = body.replace('converted, point->' + field, 'converted, ' + axis)
                    body = body.replace('(f32 (*)[4])matrix, point->' + field, '(f32 (*)[4])matrix, ' + axis)
        yield 'scalar-inline%d-mask%d-first%d' % (inline, mask, declarations_first), body


def comparison_candidates():
    base = dict(scalar_candidates())['scalar-inline0-mask1-first1']
    for style in range(6):
        body = base
        if style == 1:
            body = body.replace('(x = point->unk0) != 0.0f', '0.0f != (x = point->unk0)')
        elif style == 2:
            body = body.replace('            if (point != 0 && ((x = point->unk0)',
                '            if (point != 0) x = point->unk0;\n            if (point != 0 && (x')
        elif style == 3:
            body = body.replace('(x = point->unk0) != 0.0f', '!((x = point->unk0) == 0.0f)')
        elif style >= 4:
            body = body.replace('(x = point->unk0) != 0.0f', 'point->unk0 != 0.0f')
            if style == 4:
                body = body.replace('converted, x,', 'converted, (x = point->unk0),').replace(
                    '(f32 (*)[4])matrix, x,', '(f32 (*)[4])matrix, (x = point->unk0),')
            else:
                body = body.replace('                destination = *destinations;',
                    '                x = point->unk0;\n                destination = *destinations;')
        yield 'comparison%d' % style, body


def compile_candidate(root, out, name, body=BASELINE, profile='o2g3', extra_flags=()):
    out.mkdir(exist_ok=True)
    c_file, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    c_file.write_text('#include <ultra64.h>\n#include "functions.h"\n' + DECLARATIONS + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile], *extra_flags,
        '-o', str(obj.relative_to(root)), str(c_file.relative_to(root))], cwd=root, text=True, capture_output=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'matrix-list.ld'
    script.write_text('SECTIONS { .text 0x15145EA4 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, rel = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, extra_flags=list(extra_flags), body_words=end,
        frame=frames[0] if frames else 0, pool_bytes=len(pools.get('.rodata', (0, b''))[1]),
        diagnostics=diagnostics, relocations=rel,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles', action='store_true')
    parser.add_argument('--lifetime', action='store_true')
    parser.add_argument('--views', action='store_true')
    parser.add_argument('--scalars', action='store_true')
    parser.add_argument('--comparisons', action='store_true')
    parser.add_argument('--guards', action='store_true')
    args = parser.parse_args()
    if args.guards:
        print(json.dumps(owner_guards(), indent=2))
        return
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-matrix-list-transform'
    out.mkdir(exist_ok=True)
    forms = [('profile-' + p, BASELINE, p, ()) for p in PROFILES] if args.profiles else [
        (name, body, 'o2g3', ()) for name, body in (
            comparison_candidates() if args.comparisons else scalar_candidates() if args.scalars else view_candidates() if args.views else
            lifetime_candidates() if args.lifetime else candidates())]
    records = []
    for name, body, profile, flags in forms:
        record, _ = compile_candidate(root, out, name, body, profile, flags)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
    filename = 'profiles.json' if args.profiles else 'comparisons.json' if args.comparisons else 'scalars.json' if args.scalars else 'views.json' if args.views else 'lifetime.json' if args.lifetime else 'measurements.json'
    (out / filename).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
