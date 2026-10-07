"""Focused gate/storage scheduling controls; no production edits or guards."""

import itertools
import json
import re
from pathlib import Path

from tools.experiments import game_scaled_sphere_query_candidates as prior

ENTRY, ROM, WORDS, FUNCTION = prior.ENTRY, prior.ROM, prior.WORDS, prior.FUNCTION
compile_candidate = prior.compile_candidate
local_layout = prior.local_layout


def candidates():
    for left, right in itertools.product(range(3), repeat=2):
        body = prior.SELECTED
        for argument, form in ((6, left), (5, right)):
            expression = ('*arg%d == 0.0f' % argument, '!(*arg%d)' % argument,
                          '0.0f == *arg%d' % argument)[form]
            body = body.replace('*arg%d == 0.0f' % argument, expression)
        yield 'zero-left%d-right%d' % (left, right), body
    for outer, inner in itertools.product((False, True), repeat=2):
        body = prior.SELECTED
        for argument, wrap in ((5, inner), (6, outer)):
            if not wrap:
                continue
            gate = '    if (*arg%d == 0.0f) {\n        return 0;\n    }' % argument
            body = body.replace(gate, '    if (*arg%d != 0.0f) {' % argument)
            body = body.removesuffix('\n}') + '\n    } else {\n        return 0;\n    }\n}'
        yield 'nested-height%d-radius%d' % (outer, inner), body
    for union in (False, True):
        declaration = ('    union {struct {f32 inverse, scale;} named; f32 values[2];} scales;'
                       if union else '    struct {f32 inverse, scale;} scales;')
        access = ('scales.values[1]', 'scales.values[0]') if union else ('scales.scale', 'scales.inverse')
        body = prior.SELECTED.replace('    f32 scale;\n    f32 inverse;', declaration)
        for word, replacement in zip(('scale', 'inverse'), access):
            begin = body.index('\n\n')
            body = body[:begin] + re.sub(r'\b' + word + r'\b', replacement, body[begin:])
        yield 'scale-pair-union%d' % union, body
    for name in ('origin', 'direction', 'scaledCenter'):
        body = prior.SELECTED.replace('    struct17 %s;' % name, '    f32 %s[3];' % name)
        for axis, member in enumerate(('unk0', 'unk4', 'unk8')):
            body = body.replace(name + '.' + member, '%s[%d]' % (name, axis))
        body = body.replace('&' + name, '(struct17 *)' + name)
        yield 'array-' + name, body
    for argument in range(8):
        typename = 'struct127' if argument == 2 else 'f32' if argument in (5, 6) else 'struct17'
        body = prior.SELECTED.replace('%s *arg%d' % (typename, argument), '%s *volatile arg%d' % (typename, argument), 1)
        yield 'live-home%d' % argument, body
    for mask in (1, 2, 3, 15):
        body = prior.SELECTED
        cursor = 0
        for gate in range(4):
            offset = body.index('        return 0;', cursor)
            if mask & (1 << gate):
                body = body[:offset] + body[offset:].replace('        return 0;', '        goto failed;', 1)
            cursor = offset + 1
        body = body.removesuffix('\n}') + '\nfailed:\n    return 0;\n}'
        yield 'shared-failure%d' % mask, body


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-scaled-sphere-query-schedule'
    out.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, out, name, body)
        record['layout'] = local_layout(out / (name + '.o'))
        records.append(record)
        print(name, record['body_words'], record['frame'], record['differences'], record['layout']['entry_relative'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
