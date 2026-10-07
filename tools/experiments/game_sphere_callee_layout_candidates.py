"""Meaningful workspace/type/initializer controls; never install private patches."""

import itertools
import json
import re
from pathlib import Path

from tools.experiments import game_sphere_callee_candidates as prior
from tools.experiments import game_sphere_wrapper_candidates as wrapper

SCALARS = ('projection', 'radiusSquared', 'perpendicularSquared', 'root', 'first', 'second')


def workspace_body(reverse=False, coordinate_struct=False, grouped=False, union_direction=False):
    body = wrapper.CALLEE_BODY.replace('volatile f32 perpendicularSquared;', 'f32 perpendicularSquared;')
    fields = ['struct17 relative;'] + ['f32 ' + s + ';' for s in reversed(SCALARS)] + [
        'struct17 origin;', 'union {struct17 point; f32 values[3];} direction;' if union_direction else 'struct17 direction;']
    if coordinate_struct:
        fields.append('struct17 delta;')
    else:
        fields.extend('f32 ' + s + ';' for s in ('z', 'y', 'x'))
    if reverse:
        fields.reverse()
    names = ['direction', 'origin', 'relative', *SCALARS]
    if grouped:
        names.extend(('x', 'y', 'z'))
    else:
        fields = [f for f in fields if f not in ('struct17 delta;', 'f32 x;', 'f32 y;', 'f32 z;')]
    begin, end = body.index('    struct17 direction;'), body.index('\n\n    x =')
    declaration = '    struct {\n        ' + '\n        '.join(fields) + '\n    } work;'
    if not grouped:
        declaration += '\n    f32 x;\n    f32 y;\n    f32 z;'
    tail = body[end:]
    for name in names:
        target = 'work.' + name
        if coordinate_struct and name in ('x', 'y', 'z'):
            target = 'work.delta.unk%d' % (('x', 'y', 'z').index(name) * 4)
        tail = re.sub(r'\b' + name + r'\b', target, tail)
    if union_direction:
        tail = tail.replace('work.direction =', 'work.direction.point =')
        for offset in (0, 4, 8):
            tail = tail.replace('work.direction.unk%d' % offset, 'work.direction.values[%d]' % (offset // 4))
    return body[:begin] + declaration + tail


def type_body(coords=0, scalar_type=0, scalar_group=0):
    body = prior.SELECTED
    if coords:
        declarations = ('struct17 delta;', 'union {struct17 point; f32 values[3];} delta;',
                        'union {struct17 point; f32 values[3];} delta;')
        body = body.replace('f32 x;\n    f32 y;\n    f32 z;', declarations[coords - 1])
        for i, name in enumerate(('x', 'y', 'z')):
            target = 'delta.unk%d' % (i * 4) if coords == 1 else (
                'delta.point.unk%d' % (i * 4) if coords == 2 else 'delta.values[%d]' % i)
            body = re.sub(r'\b' + name + r'\b', target, body)
    chosen = SCALARS if scalar_group == 0 else (('projection', 'perpendicularSquared') if scalar_group == 1 else ('root', 'first', 'second'))
    if scalar_type:
        for name in chosen:
            body = body.replace('f32 ' + name + ';', ('union' if scalar_type == 1 else 'struct') + ' {f32 value;} ' + name + ';')
        split = body.index('\n\n')
        head, tail = body[:split], body[split:]
        for name in chosen:
            tail = re.sub(r'\b' + name + r'\b', name + '.value', tail)
        body = head + tail
    return body


def initialized_coordinates(union_direction=True):
    body = prior.SELECTED if union_direction else wrapper.CALLEE_BODY.replace('volatile f32 perpendicularSquared;', 'f32 perpendicularSquared;')
    expressions = ['arg2->unk%d - arg0->unk%d' % (o, o) for o in (0, 4, 8)]
    declaration = '\n    '.join('f32 %s = %s;' % pair for pair in zip(('x', 'y', 'z'), expressions))
    body = body.replace('f32 x;\n    f32 y;\n    f32 z;', declaration)
    for name, expression in zip(('x', 'y', 'z'), expressions):
        body = body.replace('    %s = %s;\n' % (name, expression), '')
    return body


def candidates():
    for options in itertools.product((False, True), repeat=4):
        yield 'workspace-r%d-c%d-g%d-u%d' % options, workspace_body(*options), 'o2g3'
    for coords, scalar_type, group in itertools.product(range(4), range(3), range(3)):
        if scalar_type == 0 and group != 0:
            continue
        yield 'types-c%d-s%d-g%d' % (coords, scalar_type, group), type_body(coords, scalar_type, group), 'o2g3'
    for union_direction, profile in itertools.product((False, True), ('o2g3', 'o2')):
        yield 'initialized-u%d-%s' % (union_direction, profile), initialized_coordinates(union_direction), profile


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-sphere-callee-layout-controls'
    out.mkdir(exist_ok=True)
    records = []
    for name, body, profile in candidates():
        record, _ = prior.compile_candidate(root, out, name, body, profile)
        records.append(record)
        print(name, record['body_words'], record['frame'], record['differences'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
