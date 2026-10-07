"""Screen real per-case scalar lifetimes without changing sampler scratch storage."""

import json
from pathlib import Path

from tools.experiments import game_area_sampler_candidates as screen


def scoped_body(mask, early=True):
    body = screen.SELECTED if early else screen.SWITCH.replace(
        '(scratch.unk1B - 64) & 0xFF', 'scratch.unk1B - 64')
    if mask & 1:
        body = body.replace('    f32 width;\n', '')
    if (mask & 6) == 6:
        body = body.replace('    f32 distance;\n', '')
    for bit, case, scalar in ((0, 2, 'width'), (1, 0, 'distance'), (2, 1, 'distance')):
        if not mask & (1 << bit):
            continue
        label = '        case %d:\n' % case
        start = body.index(label)
        end = body.find('        case ', start + len(label))
        if end < 0:
            end = body.rindex('    }\n}')
        block = body[start + len(label):end]
        body = (body[:start] + label.rstrip() + ' {\n'
            + '            f32 %s;\n' % scalar + block
            + '        }\n' + body[end:])
    return body


def candidates():
    for early in (False, True):
        for mask in range(8):
            yield 'scalar-scope-%X-early%d' % (mask, early), scoped_body(mask, early)


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-area-sampler-lifetimes'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = screen.compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], record['frame'], record['differences'], flush=True)
    assert len(records) == 16
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
