"""Bounded address/operand views for the corrected full caller, not installation."""

import json
from pathlib import Path

from tools.experiments import game_scaled_sphere_query_source_layout_candidates as prior

ENTRY, ROM, WORDS, FUNCTION = prior.ENTRY, prior.ROM, prior.WORDS, prior.FUNCTION
compile_candidate, local_layout = prior.compile_candidate, prior.local_layout
SCALE_FIRST = prior.SCALE_FIRST
PROTOTYPE, DECLARATIONS = prior.prior.PROTOTYPE, prior.prior.DECLARATIONS
OWNER_DECLARATIONS = 'void func_1515C1A0(struct127 *, struct17 *, f32 *, f32 *);\n'
SELECTED = '''s32 func_15145AD8(struct17 *arg0, struct17 *arg1, struct127 *arg2,
    struct17 *arg3, struct17 *arg4, f32 *arg5, f32 *arg6, struct17 *arg7) {
    struct17 center;
    f32 radius;
    f32 height;
    struct17 origin;
    struct17 direction;
    struct17 scaledCenter;
    f32 length;
    f32 first;
    f32 second;

    if (arg5 != NULL) {
        arg5 = &radius;
    }
    if (arg6 != NULL) {
        arg6 = &height;
    }
    if (arg7 != NULL) {
        arg7 = &center;
    }
    func_1515C1A0(arg2, arg7, arg5, arg6);
    if (*arg6 == 0.0f) {
        return 0;
    }
    if (*arg5 == 0.0f) {
        return 0;
    }
    {
        f32 scale;
        f32 inverse;

        scale = arg2->unkDC;
        inverse = arg2->unkE0;
        origin.unk0 = arg0->unk0;
        origin.unk4 = arg0->unk4 * scale;
        origin.unk8 = arg0->unk8;
        direction.unk0 = arg1->unk0;
        direction.unk4 = arg1->unk4 * scale;
        direction.unk8 = arg1->unk8;
        {
            f32 reciprocal;

            if (!func_15145128(&direction, &direction, &length, &reciprocal)) {
                return 0;
            }
            scaledCenter.unk0 = arg7->unk0;
            scaledCenter.unk4 = arg7->unk4 * scale;
            scaledCenter.unk8 = arg7->unk8;
            if (!func_151451F0(&origin, &direction, &scaledCenter, *arg5, length,
                    arg3, arg4, &first, &second)) {
                return 0;
            }
            arg3->unk4 *= inverse;
            arg4->unk4 *= inverse;
            return 1;
        }
    }
}'''


def candidates():
    for mask in range(1, 8):
        body = SCALE_FIRST
        for flag, argument in ((1, 0), (2, 1), (4, 7)):
            if not mask & flag:
                continue
            body = body.replace('struct17 *arg%d' % argument, 'f32 *arg%d' % argument, 1)
            for axis, member in enumerate(('unk0', 'unk4', 'unk8')):
                body = body.replace('arg%d->%s' % (argument, member), 'arg%d[%d]' % (argument, axis))
        if mask & 4:
            body = body.replace('arg7 = &center;', 'arg7 = (f32 *)&center;').replace(
                'func_1515C1A0(arg2, arg7,', 'func_1515C1A0(arg2, (struct17 *)arg7,')
        yield 'argument-array-mask%d' % mask, body
    for mask in range(1, 8):
        body = SCALE_FIRST
        for flag, name in ((1, 'origin'), (2, 'direction'), (4, 'scaledCenter')):
            if not mask & flag:
                continue
            for axis, member in enumerate(('unk0', 'unk4', 'unk8')):
                body = body.replace(name + '.' + member, '((f32 *)&%s)[%d]' % (name, axis))
        yield 'local-member-view-mask%d' % mask, body
    for mask in range(1, 8):
        body = SCALE_FIRST
        for flag, argument in ((1, 0), (2, 1), (4, 7)):
            if mask & flag:
                body = body.replace('arg%d->unk4 * scale' % argument, 'scale * arg%d->unk4' % argument)
        yield 'multiply-order-mask%d' % mask, body
    capture = '    scale = arg2->unkDC;\n    inverse = arg2->unkE0;'
    for name, expression in (
            ('comma', 'scale = arg2->unkDC, inverse = arg2->unkE0;'),
            ('parenthesized', '(scale = arg2->unkDC, inverse = arg2->unkE0);'),
            ('inverse-result', 'inverse = (scale = arg2->unkDC, arg2->unkE0);'),
            ('scale-result', 'scale = (inverse = arg2->unkE0, arg2->unkDC);')):
        yield 'capture-' + name, SCALE_FIRST.replace(capture, '    ' + expression)
    for mask in (1, 2, 3):
        body = SCALE_FIRST
        for flag, name in ((1, 'scale'), (2, 'inverse')):
            if mask & flag:
                body = body.replace('    f32 %s;' % name, '    register f32 %s;' % name)
        yield 'scalar-register-mask%d' % mask, body
    for name, addresses in (
            ('members', ('(struct17 *)&direction.unk0', '&length', '&reciprocal')),
            ('first-elements', ('(struct17 *)&((f32 *)&direction)[0]', '&length', '&reciprocal')),
            ('byte-view', ('(struct17 *)(u8 *)&direction', '&length', '&reciprocal')),
            ('scalar-first-members', ('&direction', '(f32 *)&length', '(f32 *)&reciprocal'))):
        point, length, reciprocal = addresses
        yield 'normalizer-address-' + name, SCALE_FIRST.replace(
            'func_15145128(&direction, &direction, &length, &reciprocal)',
            'func_15145128(%s, %s, %s, %s)' % (point, point, length, reciprocal))
    for count in (3, 9):
        scoped = prior.scoped_body(count).replace(
            '    inverse = arg2->unkE0;\n    scale = arg2->unkDC;', capture)
        for initializer in ('scale', 'inverse'):
            member = 'unkDC' if initializer == 'scale' else 'unkE0'
            body = scoped.replace('f32 %s;' % initializer, 'f32 %s = arg2->%s;' % (initializer, member)).replace(
                '    %s = arg2->%s;\n' % (initializer, member), '')
            yield 'scope%d-initialize-%s' % (count, initializer), body
    for name, begin in (('height-gate', '    if (*arg6 =='),
            ('radius-gate', '    if (*arg5 =='), ('capture', '    scale ='),
            ('origin', '    origin.unk0 ='), ('direction', '    direction.unk0 ='),
            ('normalizer', '    if (!func_15145128')):
        body = SCALE_FIRST.replace('    f32 reciprocal;\n', '')
        position = body.index(begin)
        body = body[:position] + '    {\n    f32 reciprocal;\n' + body[position:]
        yield 'reciprocal-scope-' + name, body.removesuffix('\n}') + '\n    }\n}'
    for count in (3, 6, 9):
        for name, begin in (('origin', '    origin.unk0 ='),
                ('direction', '    direction.unk0 ='), ('normalizer', '    if (!func_15145128')):
            body = prior.scoped_body(count).replace(
                '    inverse = arg2->unkE0;\n    scale = arg2->unkDC;', capture).replace(
                '    f32 reciprocal;\n', '')
            position = body.index(begin)
            body = body[:position] + '    {\n    f32 reciprocal;\n' + body[position:]
            yield 'nested%d-reciprocal-%s' % (count, name), body.removesuffix('\n}') + '\n    }\n}'


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-scaled-sphere-query-address-view'
    out.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, out, name, body)
        record['layout'] = local_layout(out / (name + '.o'))
        records.append(record)
        print(name, record['body_words'], record['frame'], record['differences'],
              record['layout']['entry_relative'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')
    record, _ = compile_candidate(root, out, 'selected', SELECTED)
    record['layout'] = local_layout(out / 'selected.o')
    (out / 'selected-record.json').write_text(json.dumps(record, indent=2) + '\n')


if __name__ == '__main__':
    main()
