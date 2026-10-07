"""Uninstalled sphere-intersection controls; equal length/frame is not a match."""

import itertools
import json
from pathlib import Path

from tools.experiments import game_sphere_wrapper_candidates as prior

ENTRY, ROM, WORDS = prior.CALLEE, prior.CALLEE_ROM, prior.CALLEE_WORDS
FUNCTION = prior.CALLEE_FUNCTION
DOT, DOT_ROM, DOT_WORDS = prior.DOT, prior.DOT_ROM, prior.DOT_WORDS
DECLARATIONS = prior.DECLARATIONS


def signed_root(body):
    body = body.replace('    f32 root;', '    f32 root;\n    f32 signedRoot;')
    body = body.replace('    if (projection < root)', '    signedRoot = root;\n    if (projection < root)')
    body = body.replace('        root = -root;', '        signedRoot = -root;')
    return body.replace('first = projection - root;', 'first = projection - signedRoot;').replace(
        'second = projection + root;', 'second = projection + signedRoot;')


def union_body(mask=1, member_address=False, separate_root=False):
    body = prior.CALLEE_BODY.replace('volatile f32 perpendicularSquared;', 'f32 perpendicularSquared;')
    for i, name in enumerate(('direction', 'origin', 'relative')):
        if mask & 1 << i:
            body = body.replace('struct17 ' + name + ';', 'union {struct17 point; f32 values[3];} ' + name + ';')
            if name in ('direction', 'origin'):
                body = body.replace('    ' + name + ' =', '    ' + name + '.point =')
            for offset in (0, 4, 8):
                body = body.replace(name + '.unk%d' % offset, name + '.values[%d]' % (offset // 4))
            if name == 'relative':
                body = body.replace('(f32 *)&relative', 'relative.values')
    if member_address and not mask & 4:
        body = body.replace('(f32 *)&relative', '&relative.unk0')
    return signed_root(body) if separate_root else body


SELECTED = union_body()


def storage_candidates():
    # Array overlays are compiler controls, not qualified production replacements.
    for mask, radius_parameter, separate_root in itertools.product(range(8), (False, True), (False, True)):
        body = prior.CALLEE_BODY.replace('volatile f32 perpendicularSquared;', 'f32 perpendicularSquared;')
        for i, name in enumerate(('direction', 'origin', 'relative')):
            if mask & 1 << i:
                body = body.replace('struct17 ' + name + ';', 'f32 ' + name + '[3];')
                for offset in (0, 4, 8):
                    body = body.replace(name + '.unk%d' % offset, name + '[%d]' % (offset // 4))
                if name in ('direction', 'origin'):
                    body = body.replace('    ' + name + ' =', '    *(struct17 *)' + name + ' =')
                else:
                    body = body.replace('(f32 *)&relative', 'relative')
        if radius_parameter:
            body = body.replace('    f32 radiusSquared;\n', '').replace('radiusSquared', 'arg3')
        if separate_root:
            body = signed_root(body)
        yield 'storage%d-radius%d-root%d' % (mask, radius_parameter, separate_root), body


def candidates():
    yield from storage_candidates()
    for mask, member_address, separate_root in itertools.product(range(8), (False, True), (False, True)):
        yield 'union%d-member%d-root%d' % (mask, member_address, separate_root), union_body(mask, member_address, separate_root)


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    return prior.compile_candidate(root, output, name, body, profile, FUNCTION)


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-sphere-callee'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], record['frame'], record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
