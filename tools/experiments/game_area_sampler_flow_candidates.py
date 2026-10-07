"""Measure sampler control-flow forms with the original live fields and scratch."""

import itertools
import json
from pathlib import Path

from tools.experiments import game_area_sampler_candidates as prior


def blocks():
    default, rest = prior.SELECTED.split('        default:\n', 1)[1].split('        case 2:\n')
    rectangle, rest = rest.split('        case 0:\n')
    circle0, circle1 = rest.split('        case 1:\n')
    circle1 = circle1.rsplit('    }\n}', 1)[0]
    return {3: default, 2: rectangle, 0: circle0, 1: circle1}


PREFIX = prior.SELECTED.split('    switch (', 1)[0]


def work(case):
    return blocks()[case].replace('            break;\n', '').replace('            return;\n', '')


def candidates():
    for order in itertools.permutations(range(4)):
        body = PREFIX + '    switch (source->flags & 3) {\n'
        for case in order:
            label = 'default' if case == 3 else 'case %d' % case
            body += '        %s:\n' % label + work(case) + '            return;\n'
        yield 'switch-order-' + ''.join(map(str, order)), body + '    }\n}'
    for order in itertools.permutations(range(3)):
        for chain in (False, True):
            body = PREFIX + '    s32 mode = source->flags & 3;\n'
            for i, case in enumerate(order):
                keyword = 'else if' if i and chain else 'if'
                body += '    %s (mode == %d) {\n' % (keyword, case) + work(case) + '        return;\n    } '
            body += ('else {\n' + work(3) + '    }\n' if chain else '\n' + work(3)) + '}'
            yield 'chain%d-order-%s' % (chain, ''.join(map(str, order))), body
    for singled in range(3):
        for first in (False, True):
            body = PREFIX + '    s32 mode = source->flags & 3;\n'
            if first:
                body += '    if (mode == %d) {\n' % singled + work(singled) + '        return;\n    }\n'
            body += '    switch (mode) {\n'
            for case in (3, 2, 0, 1):
                if case == singled:
                    continue
                label = 'default' if case == 3 else 'case %d' % case
                if case == 3 and not first:
                    body += '        default:\n            break;\n'
                else:
                    body += '        %s:\n' % label + work(case) + '            return;\n'
            body += '    }\n'
            if not first:
                body += '    if (mode == %d) {\n' % singled + work(singled) + '    } else {\n' + work(3) + '    }\n'
            yield 'split-case%d-first%d' % (singled, first), body + '}'
    for kind, keyword, shifted in itertools.product(('s32', 'u32', 'u8'), ('', 'register '), (False, True)):
        body = prior.SELECTED.replace('    f32 width;\n', '    f32 width;\n    %s%s angle;\n' % (keyword, kind))
        for field in ('unk1B', 'unkB'):
            body = body.replace('scratch.%s = func_150ADA20();' % field,
                'angle = func_150ADA20();\n            scratch.%s = angle;' % field)
            if shifted:
                expression = '(u32)angle - 64' if kind == 's32' else 'angle - 64'
                body = body.replace('func_151423D8(scratch.%s - 64)' % field, 'func_151423D8(%s)' % expression)
        yield 'rng-%s-register%d-shifted%d' % (kind, bool(keyword), shifted), body


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-area-sampler-flow'
    out.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = prior.compile_candidate(root, out, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
    assert len(records) == 54
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
