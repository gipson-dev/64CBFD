"""Measure scale accesses and source-line scheduling under the existing profile."""

import itertools
import json
import re
from pathlib import Path

from tools.experiments import game_scaled_sphere_query_candidates as prior

ENTRY, ROM, WORDS, FUNCTION = prior.ENTRY, prior.ROM, prior.WORDS, prior.FUNCTION
compile_candidate = prior.compile_candidate
local_layout = prior.local_layout
SCALE_FIRST = prior.SELECTED.replace('    inverse = arg2->unkE0;\n    scale = arg2->unkDC;',
    '    scale = arg2->unkDC;\n    inverse = arg2->unkE0;')


def scoped_body(count=3, initialize_inverse=False):
    body = prior.SELECTED
    declarations = body[body.index('    struct17 origin;'):body.index('\n\n')].splitlines()
    moving = declarations[-count:] if count else []
    for declaration in moving:
        body = body.replace(declaration + '\n', '')
    begin = body.index('    inverse =')
    inner = body[begin:].removesuffix('\n}')
    if initialize_inverse:
        moving = [line.replace('f32 inverse;', 'f32 inverse = arg2->unkE0;') for line in moving]
        inner = inner.replace('    inverse = arg2->unkE0;\n', '')
    return body[:begin] + '    {\n' + '\n'.join(moving) + '\n' + inner + '\n    }\n}'


def workspace_body(mask=3, whole=False):
    body = prior.SELECTED
    vectors = ('origin', 'direction', 'scaledCenter')
    scalars = ('length', 'first', 'second', 'scale', 'inverse', 'reciprocal')
    for names, typename in ((vectors if mask & 1 else (), 'struct17'), (scalars if mask & 2 else (), 'f32')):
        for name in names:
            body = body.replace('    %s %s;\n' % (typename, name), '')
    vector_record = 'struct17 scaledCenter, direction, origin;'
    scalar_record = 'f32 reciprocal, inverse, scale, second, first, length;'
    if whole:
        body = body.replace('    f32 height;\n', '    f32 height;\n' +
            '    struct {%s %s} work;\n' % (scalar_record, vector_record))
    else:
        if mask & 1:
            body = body.replace('    f32 height;\n', '    f32 height;\n' +
                '    struct {%s} points;\n' % vector_record)
        if mask & 2:
            begin = body.index('\n\n')
            body = body[:begin] + '\n    struct {%s} values;' % scalar_record + body[begin:]
    begin = body.index('\n\n')
    code = body[begin:]
    for names, flag, prefix in ((vectors, 1, 'points'), (scalars, 2, 'values')):
        if mask & flag:
            for name in names:
                code = re.sub(r'\b' + name + r'\b', ('work' if whole else prefix) + '.' + name, code)
    return body[:begin] + code


def candidates():
    for mask, qualifier in itertools.product(range(1, 4), ('volatile', 'const')):
        body = prior.SELECTED
        for flag, member in ((1, 'unkE0'), (2, 'unkDC')):
            if mask & flag:
                body = body.replace('arg2->' + member,
                    '*(%s f32 *)&arg2->%s' % (qualifier, member))
        yield '%s-scale-mask%d' % (qualifier, mask), body
    regions = {
        'height-gate': ('    if (*arg6 == 0.0f)', '    if (*arg5 == 0.0f)'),
        'radius-gate': ('    if (*arg5 == 0.0f)', '    inverse ='),
        'scales': ('    inverse =', '    origin.unk0 ='),
        'origin': ('    origin.unk0 =', '    direction.unk0 ='),
        'direction': ('    direction.unk0 =', '    if (!func_15145128'),
        'vectors': ('    origin.unk0 =', '    if (!func_15145128'),
        'scales-vectors': ('    inverse =', '    if (!func_15145128'),
        'radius-scales': ('    if (*arg5 == 0.0f)', '    origin.unk0 ='),
        'radius-scales-vectors': ('    if (*arg5 == 0.0f)', '    if (!func_15145128'),
        'normalize-gate': ('    if (!func_15145128', '    scaledCenter.unk0 ='),
        'center': ('    scaledCenter.unk0 =', '    if (!func_151451F0'),
        'wrapper-gate': ('    if (!func_151451F0', '    arg3->unk4 *='),
        'success': ('    inverse =', None),
        'both-gates-success': ('    if (*arg6 == 0.0f)', None),
        'body': ('    if (arg5 != NULL)', None),
    }
    for name, (start, finish) in regions.items():
        body = prior.SELECTED
        begin = body.index(start)
        end = body.index(finish, begin) if finish is not None else body.rindex('\n}')
        body = body[:begin] + '    ' + ' '.join(body[begin:end].split()) + '\n' + body[end:]
        yield 'same-line-' + name, body
    for mask in (1, 2, 3):
        yield 'workspace-mask%d' % mask, workspace_body(mask)
    yield 'workspace-whole', workspace_body(whole=True)
    for count in range(10):
        yield 'scoped-tail%d' % count, scoped_body(count)
    for count in (3, 9):
        yield 'scoped-inverse-initializer%d' % count, scoped_body(count, initialize_inverse=True)
    yield 'capture-scale-first', SCALE_FIRST
    yield 'scoped-scale-first', scoped_body().replace(
        '    inverse = arg2->unkE0;\n    scale = arg2->unkDC;',
        '    scale = arg2->unkDC;\n    inverse = arg2->unkE0;')


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-scaled-sphere-query-source-layout'
    out.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, out, name, body)
        record['layout'] = local_layout(out / (name + '.o'))
        records.append(record)
        print(name, record['body_words'], record['frame'], record['differences'],
              record['layout']['entry_relative'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
