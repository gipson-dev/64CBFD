"""Recover zero-axis selection and ordered basis construction from retail C shapes."""

import argparse
import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15146078, 0x173528, 148
FUNCTION = 'func_15146078'
SYMBOLS = dict(func_151450B4=0x151450B4, func_15145128=0x15145128)
DECLARATIONS = 's32 func_15145128(struct17 *, struct17 *, f32 *, f32 *);\n'
PROTOTYPE = 's32 func_15146078(f32 *point, f32 *first, f32 *second);'
BASELINE = '''s32 func_15146078(f32 *point, f32 *first, f32 *second) {
    f32 length;
    f32 reciprocal;
    u8 zeroCount = 0;
    u8 zeroAxis;
    u8 nonzeroAxis;
    s32 firstAxis = 1;
    s32 secondAxis = 2;

    if (point[0] == 0.0f && point[1] == 0.0f && point[2] == 0.0f) {
        return 0;
    }
    if (point[0] == 0.0f) {
        zeroCount++;
        zeroAxis = 0;
    } else {
        nonzeroAxis = 0;
    }
    if (point[1] == 0.0f) {
        zeroCount++;
        zeroAxis = 1;
    } else {
        nonzeroAxis = 1;
    }
    if (point[2] == 0.0f) {
        zeroCount++;
        zeroAxis = 2;
    } else {
        nonzeroAxis = 2;
    }

    if (zeroCount == 2) {
        switch (nonzeroAxis) {
        case 0:
            first[0] = first[2] = 0.0f;
            first[1] = 1.0f;
            second[0] = second[1] = 0.0f;
            second[2] = 1.0f;
            break;
        case 1:
            first[1] = first[2] = 0.0f;
            first[0] = 1.0f;
            second[0] = second[1] = 0.0f;
            second[2] = 1.0f;
            break;
        case 2:
            first[1] = first[2] = 0.0f;
            first[0] = 1.0f;
            second[0] = second[2] = 0.0f;
            second[1] = 1.0f;
            break;
        }
    } else {
        if (zeroCount == 1 && zeroAxis == 2) {
            firstAxis = 2;
            secondAxis = 1;
        }
        first[0] = first[firstAxis] = 1.0f;
        first[secondAxis] = -point[0] - point[firstAxis] / point[secondAxis];
        func_151450B4((struct17 *)first, (struct17 *)point, (struct17 *)second);
        func_151450B4((struct17 *)second, (struct17 *)point, (struct17 *)first);
        func_15145128((struct17 *)first, (struct17 *)first, &length, &reciprocal);
        func_15145128((struct17 *)second, (struct17 *)second, &length, &reciprocal);
    }
    return 1;
}'''


def candidates():
    for count_type, axis_type, initial, declaration_order, stores in itertools.product(
            ('u8', 's32'), ('u8', 's32'), (False, True), (False, True), (False, True)):
        body = BASELINE.replace('u8 zeroCount', count_type + ' zeroCount').replace('u8 zeroAxis', axis_type + ' zeroAxis')
        body = body.replace('u8 nonzeroAxis', axis_type + ' nonzeroAxis')
        if initial:
            body = body.replace('zeroAxis;', 'zeroAxis = 0;').replace('nonzeroAxis;', 'nonzeroAxis = 0;')
        if declaration_order:
            body = body.replace('    f32 length;\n    f32 reciprocal;\n', '').replace(
                '    s32 secondAxis = 2;\n', '    s32 secondAxis = 2;\n    f32 length;\n    f32 reciprocal;\n')
        if stores:
            for destination in ('first', 'second'):
                for a, b in ((0, 1), (0, 2), (1, 2)):
                    body = body.replace('%s[%d] = %s[%d] = 0.0f;' % (destination, a, destination, b),
                        '%s[%d] = 0.0f;\n            %s[%d] = 0.0f;' % (destination, a, destination, b))
            body = body.replace('first[0] = first[firstAxis] = 1.0f;', 'first[0] = 1.0f;\n        first[firstAxis] = 1.0f;')
        yield 'count%s-axis%s-init%d-order%d-stores%d' % (
            count_type, axis_type, initial, declaration_order, stores), body


def lifetime_candidates():
    for cached, placement, returns, explicit_stores in itertools.product((False, True), range(3), (False, True), (False, True)):
        body = dict(candidates())['countu8-axisu8-init0-order0-stores%d' % explicit_stores]
        if cached:
            body = body.replace('    f32 length;', '    f32 x;\n    f32 length;', 1)
            body = body.replace('if (point[0] == 0.0f &&', 'if ((x = point[0]) == 0.0f &&', 1)
            body = body.replace('    if (point[0] == 0.0f) {', '    if (x == 0.0f) {', 1)
        if placement:
            body = body.replace('u8 zeroCount = 0;', 'u8 zeroCount;')
            body = body.replace('    if (point[0] == 0.0f) {', '    zeroCount = 0;\n    if (point[0] == 0.0f) {', 1) if not cached else (
                body.replace('    if (x == 0.0f) {', '    zeroCount = 0;\n    if (x == 0.0f) {', 1))
            if placement == 2:
                body = body.replace('s32 firstAxis = 1;', 's32 firstAxis;').replace('s32 secondAxis = 2;', 's32 secondAxis;')
                body = body.replace('    if (point[1] == 0.0f) {', '    firstAxis = 1;\n    if (point[1] == 0.0f) {', 1)
                body = body.replace('        if (zeroCount == 1', '        secondAxis = 2;\n        if (zeroCount == 1', 1)
        if returns:
            body = body.replace('            break;', '            return 1;')
        yield 'lifetime-cached%d-placement%d-returns%d-stores%d' % (cached, placement, returns, explicit_stores), body


def scalar_candidates():
    base = dict(lifetime_candidates())['lifetime-cached1-placement2-returns1-stores1']
    declarations = '    f32 x;\n    f32 length;\n    f32 reciprocal;\n    u8 zeroCount;\n    u8 zeroAxis;\n    u8 nonzeroAxis;\n    s32 firstAxis;\n    s32 secondAxis;\n'
    layouts = {
        'original': declarations,
        'outputs-last': '    u8 nonzeroAxis;\n    u8 zeroAxis;\n    u8 zeroCount;\n    f32 x;\n    s32 firstAxis;\n    s32 secondAxis;\n    f32 length;\n    f32 reciprocal;\n',
        'indices-first': '    u8 nonzeroAxis;\n    u8 zeroAxis;\n    u8 zeroCount;\n    s32 firstAxis;\n    s32 secondAxis;\n    f32 x;\n    f32 length;\n    f32 reciprocal;\n',
    }
    for assignment, zero_first, layout in itertools.product((False, True), (False, True), layouts):
        body = base.replace(declarations, layouts[layout])
        if assignment:
            body = body.replace('    if ((x = point[0]) == 0.0f &&', '    x = point[0];\n    if (x == 0.0f &&', 1)
        if zero_first:
            body = body.replace('(x = point[0]) == 0.0f', '0.0f == (x = point[0])')
            body = body.replace('x == 0.0f', '0.0f == x')
            body = body.replace('point[1] == 0.0f', '0.0f == point[1]')
            body = body.replace('point[2] == 0.0f', '0.0f == point[2]')
        yield 'scalar-assignment%d-zero%d-%s' % (assignment, zero_first, layout), body


def expression_candidates():
    base = dict(lifetime_candidates())['lifetime-cached1-placement2-returns1-stores1']
    for literal, vector_input, cached in itertools.product(('0', '0.0', '0.0f'), (False, True), (False, True)):
        body = base.replace('0.0f', literal)
        if not cached:
            body = body.replace('    f32 x;\n', '').replace('(x = point[0])', 'point[0]').replace('if (x ==', 'if (point[0] ==')
        if vector_input:
            body = body.replace('f32 *point', 'struct17 *point')
            for index, member in enumerate(('unk0', 'unk4', 'unk8')):
                body = body.replace('point[%d]' % index, 'point->' + member)
            body = body.replace('point[firstAxis]', '((f32 *)point)[firstAxis]')
            body = body.replace('point[secondAxis]', '((f32 *)point)[secondAxis]')
        yield 'expression-%s-vector%d-cached%d' % (literal, vector_input, cached), body


def output_candidates():
    base = dict(lifetime_candidates())['lifetime-cached1-placement2-returns1-stores1']
    for pair, gate, names in itertools.product((False, True), range(3), (False, True)):
        body = base
        if pair:
            body = body.replace('    f32 length;\n    f32 reciprocal;', '    f32 scales[2];')
            body = body.replace('&length, &reciprocal', '&scales[1], &scales[0]')
        if gate == 1:
            body = body.replace('    if ((x = point[0]) == 0.0f && point[1] == 0.0f && point[2] == 0.0f)',
                '    if (!((x = point[0]) != 0.0f || point[1] != 0.0f || point[2] != 0.0f))')
        if gate == 2:
            body = body.replace('    if ((x = point[0]) == 0.0f && point[1] == 0.0f && point[2] == 0.0f)',
                '    if (!(x = point[0]) && !point[1] && !point[2])')
        if names:
            mapping = dict(point='arg0', first='arg1', second='arg2', x='var_f0', length='var_f4',
                reciprocal='var_f8', zeroCount='var_v0', zeroAxis='var_a2', nonzeroAxis='var_a0',
                firstAxis='var_t0', secondAxis='var_t1', scales='var_sp30')
            body = re.sub(r'\b(' + '|'.join(mapping) + r')\b', lambda m: mapping[m[0]], body)
        yield 'output-pair%d-gate%d-names%d' % (pair, gate, names), body


SELECTED = dict(lifetime_candidates())['lifetime-cached1-placement2-returns1-stores1']


def vector_candidates():
    for cached, returns, scope, chained in itertools.product((False, True), repeat=4):
        body = dict(lifetime_candidates())['lifetime-cached%d-placement2-returns%d-stores%d' % (cached, returns, not chained)]
        for destination in ('point', 'first', 'second'):
            body = body.replace('f32 *' + destination, 'struct17 *' + destination)
            for index, member in enumerate(('unk0', 'unk4', 'unk8')):
                body = body.replace('%s[%d]' % (destination, index), destination + '->' + member)
            body = body.replace(destination + '[firstAxis]', '((f32 *)%s)[firstAxis]' % destination)
            body = body.replace(destination + '[secondAxis]', '((f32 *)%s)[secondAxis]' % destination)
        if scope:
            for index in range(3):
                body = body.replace('        case %d:\n' % index, '        case %d: {\n' % index)
            body = body.replace('            return 1;\n', '            return 1;\n        }\n') if returns else body.replace('            break;\n', '            break;\n        }\n')
        yield 'vector-cached%d-returns%d-scope%d-chained%d' % (cached, returns, scope, chained), body


def negative_candidates():
    yield 'negative-corrected-plane-formula', SELECTED.replace('-point[0] - point[firstAxis] / point[secondAxis]',
        '-(point[0] + point[firstAxis]) / point[secondAxis]')
    yield 'negative-axis-swap-gate', SELECTED.replace('zeroAxis == 2', 'zeroAxis == 1')
    yield 'negative-cross-order', SELECTED.replace('((struct17 *)second, (struct17 *)point, (struct17 *)first)',
        '((struct17 *)point, (struct17 *)second, (struct17 *)first)')
    yield 'negative-second-normalization-omitted', SELECTED.replace(
        '        func_15145128((struct17 *)second, (struct17 *)second, &length, &reciprocal);\n', '')
    yield 'negative-zero-return', SELECTED.replace('        return 0;', '        return 1;', 1)


def register_candidates():
    for declaration, initialized in itertools.product(('f32', 'register f32', 'volatile f32'), (False, True)):
        body = SELECTED.replace('    f32 x;', '    %s x%s;' % (declaration, ' = point[0]' if initialized else ''))
        if initialized:
            body = body.replace('(x = point[0])', 'x')
        yield 'register-%s-init%d' % (declaration.replace(' ', '-'), initialized), body


def coordinate_candidates():
    for cached_y, cached_z, quotient, nested, initialize in itertools.product((False, True), repeat=5):
        body = SELECTED
        if nested:
            body = body.replace('    if ((x = point[0]) == 0.0f && point[1] == 0.0f && point[2] == 0.0f) {\n        return 0;\n    }',
                '    if ((x = point[0]) == 0.0f) {\n        if (point[1] == 0.0f) {\n            if (point[2] == 0.0f) {\n                return 0;\n            }\n        }\n    }')
        if initialize:
            body = body.replace('    f32 x;', '    f32 x = point[0];').replace('(x = point[0])', 'x')
        for cached, axis, name in ((cached_y, 1, 'y'), (cached_z, 2, 'z')):
            if cached:
                body = body.replace('    f32 length;', '    f32 %s;\n    f32 length;' % name, 1)
                position = body.index('    zeroCount = 0;')
                body = body[:position] + body[position:].replace('if (point[%d] == 0.0f)' % axis,
                    'if ((%s = point[%d]) == 0.0f)' % (name, axis), 1)
        if quotient:
            body = body.replace('    f32 length;', '    f32 quotient;\n    f32 length;', 1)
            body = body.replace('        first[secondAxis] = -point[0] - point[firstAxis] / point[secondAxis];',
                '        quotient = point[firstAxis] / point[secondAxis];\n        first[secondAxis] = -point[0] - quotient;')
        yield 'coordinate-y%d-z%d-quotient%d-nested%d-init%d' % (cached_y, cached_z, quotient, nested, initialize), body


def workspace_candidates():
    for reverse_axes, reverse_indices, placement in itertools.product((False, True), (False, True), range(3)):
        axes = ['zeroCount', 'zeroAxis', 'nonzeroAxis']
        indices = ['firstAxis', 'secondAxis']
        if reverse_axes:
            axes.reverse()
        if reverse_indices:
            indices.reverse()
        groups = [ [('f32', 'reciprocal'), ('f32', 'length')],
                   [('s32', name) for name in indices], [('f32', 'x')], [('u8', name) for name in axes] ]
        if placement == 1:
            groups = [groups[3], groups[2], groups[1], groups[0]]
        if placement == 2:
            groups = [groups[2], groups[3], groups[0], groups[1]]
        fields = list(itertools.chain.from_iterable(groups))
        body = SELECTED
        for kind, name in fields:
            body = body.replace('    %s %s;\n' % (kind, name), '')
        mapping = {name: 'work.' + name for kind, name in fields}
        body = re.sub(r'\b(' + '|'.join(mapping) + r')\b', lambda m: mapping[m[0]], body)
        declaration = '    struct {\n' + ''.join('        %s %s;\n' % field for field in fields) + '    } work;\n'
        body = body.replace('second) {\n', 'second) {\n' + declaration, 1)
        yield 'workspace-axes%d-indices%d-placement%d' % (reverse_axes, reverse_indices, placement), body


def seed_candidates():
    for refresh_x, operand_y, operand_z, quotient in itertools.product(range(3), (False, True), (False, True), (False, True)):
        body = SELECTED
        statements = []
        numerator, denominator, x = 'point[firstAxis]', 'point[secondAxis]', 'point[0]'
        for cached, axis, name in ((operand_y, 'firstAxis', 'y'), (operand_z, 'secondAxis', 'z')):
            if cached:
                body = body.replace('    f32 length;', '    f32 %s;\n    f32 length;' % name, 1)
                statements.append('        %s = point[%s];' % (name, axis))
                if name == 'y':
                    numerator = name
                else:
                    denominator = name
        if refresh_x == 1:
            statements.append('        x = point[0];')
            x = 'x'
        elif refresh_x == 2:
            x = '(x = point[0])'
        division = numerator + ' / ' + denominator
        if quotient:
            body = body.replace('    f32 length;', '    f32 quotient;\n    f32 length;', 1)
            statements.append('        quotient = %s;' % division)
            division = 'quotient'
        statements.append('        first[secondAxis] = -%s - %s;' % (x, division))
        body = body.replace('        first[secondAxis] = -point[0] - point[firstAxis] / point[secondAxis];', '\n'.join(statements))
        yield 'seed-refresh%d-y%d-z%d-quotient%d' % (refresh_x, operand_y, operand_z, quotient), body


def compile_candidate(root, out, name, body=BASELINE, profile='o2g3', extra_flags=()):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n' + DECLARATIONS + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile], *extra_flags,
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, text=True, capture_output=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'basis.ld'
    script.write_text('SECTIONS { .text 0x15146078 : SUBALIGN(4) { *(.text) } }\n')
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
    groups = dict(primary=candidates, lifetime=lifetime_candidates, scalars=scalar_candidates,
        expressions=expression_candidates, outputs=output_candidates, vectors=vector_candidates,
        registers=register_candidates, coordinates=coordinate_candidates, workspace=workspace_candidates,
        seed=seed_candidates)
    parser.add_argument('--group', choices=(*groups, 'profiles'), default='primary')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-vector-basis'
    out.mkdir(exist_ok=True)
    forms = [('profile-' + p, BASELINE, p) for p in PROFILES] if args.group == 'profiles' else [
        (name, body, 'o2g3') for name, body in groups[args.group]()]
    records = []
    for name, body, profile in forms:
        record, _ = compile_candidate(root, out, name, body, profile)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
    filename = args.group + '.json'
    (out / filename).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
