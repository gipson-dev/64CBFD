"""Screen meaningful paired geometry locals and counted graph-edge lifetimes."""

import argparse
import itertools
import json
import re
from pathlib import Path

from tools.experiments import game_graph_edge_crossing_candidates as recovery
from tools.experiments.game_record_neighbor_visit_candidates import replace


CHECKPOINT = dict(recovery.candidates())['reused-side-values']
PAIRS = (
    (('nx', 'nz'), 'normal', ('x', 'z')),
    (('ax', 'az'), 'owner', ('x', 'z')),
    (('start', 'end'), 'side', ('start', 'end')),
    (('a', 'b'), 'absolute', ('start', 'end')),
    (('minimum', 'fraction'), 'hit', ('minimum', 'fraction')),
)


def pair(body, names, label, fields, array=False):
    declarations = ['    f32 ' + name + ';\n' for name in names]
    for declaration in declarations:
        if body.count(declaration) != 1:
            raise ValueError('missing paired float declaration: ' + declaration.strip())
    if array:
        declaration = '    f32 ' + label + '[2];\n'
        values = [label + '[0]', label + '[1]']
    else:
        declaration = '    struct { f32 ' + fields[0] + '; f32 ' + fields[1] + '; } ' + label + ';\n'
        values = [label + '.' + field for field in fields]
    marker = '    /* paired-local-declaration */\n'
    if marker in body:
        raise ValueError('paired declaration marker already present')
    body = replace(body, declarations[0], marker)
    body = replace(body, declarations[1], '')
    # Both members are semantic scalars; no extra padding or address escape is added.
    pattern = r'\b(' + '|'.join(names) + r')\b'
    translations = dict(zip(names, values))
    body = re.sub(pattern, lambda match: translations[match.group()], body)
    return replace(body, marker, declaration)


def layouts():
    forms = []
    for base_name, base in (
            ('baseline', recovery.BASELINE),
            ('side-reuse', CHECKPOINT),
            ('edge-cursor', dict(recovery.cursor_candidates())['edge-cursor']),
            ('side-copies', dict(recovery.cursor_candidates())['edge-cursor-side-copies'])):
        choices = PAIRS if base_name != 'side-reuse' else tuple(p for p in PAIRS if p[0] != ('a', 'b'))
        for array, entries in itertools.product((False, True),
                [(p,) for p in choices] + [choices[:2], choices[:3]]):
            body = base
            for names, label, fields in entries:
                body = pair(body, names, label, fields, array)
            name = base_name + '-' + ('arrays' if array else 'pairs') + '-' + '-'.join(p[1] for p in entries)
            forms.append((name, body))
    return forms


def loops():
    forms = []
    for name, base in [('baseline', recovery.BASELINE), ('side-reuse', CHECKPOINT),
                       ('edge-cursor', dict(recovery.cursor_candidates())['edge-cursor']),
                       ('side-copies', dict(recovery.cursor_candidates())['edge-cursor-side-copies'])]:
        for unsigned in (False, True):
            body = base
            if unsigned:
                body = replace(body, '    s32 i;', '    u32 i;')
            body = replace(body, '    if (count > 0) {\n        nodes = D_800D2350;\n'
                           '        for (i = 0; i < count; i++) {',
                           '    nodes = D_800D2350;\n    {\n        for (i = 0; i < count; i++) {')
            forms.append((name + '-single-count-gate' + ('-unsigned-control' if unsigned else ''), body))
        indexed = base.replace('i * 16', '(i << 4)').replace('id * 16', '(id << 4)')
        indexed = replace(indexed, '    if (count > 0) {\n        nodes = D_800D2350;\n'
                          '        for (i = 0; i < count; i++) {',
                          '    i = 0;\n    if (i < count) {\n        nodes = D_800D2350;\n        do {')
        indexed = replace(indexed, '        }\n    }\n    if (minimum',
                          '            i++;\n        } while (i < count);\n    }\n    if (minimum')
        forms.append((name + '-indexed-do-while', indexed))
        forms.append((name + '-indexed-do-while-reloaded-count', replace(indexed,
                      'while (i < count)', 'while (i < D_80087290)')))
    return forms


def side_lifetimes():
    forms = []
    for name, base in [('baseline', recovery.BASELINE),
                       ('edge-cursor', dict(recovery.cursor_candidates())['edge-cursor']),
                       ('side-copies', dict(recovery.cursor_candidates())['edge-cursor-side-copies'])]:
        early = replace(base, '                            a = start;\n', '')
        early = replace(early, '                            end = (x + dx)',
                        '                            a = start;\n                            end = (x + dx)')
        forms.append((name + '-early-start-copy', early))
        for suffix, before, after in (
                ('copy-tangent', 'constant = -(ax * nx + swap * az);', 'constant = -(ax * nx + nz * az);'),
                ('sentinel-first', 'id != 255', '255 != id'),
                ('minimum-pair', None, None)):
            body = pair(early, *PAIRS[-1]) if suffix == 'minimum-pair' else replace(early, before, after)
            forms.append((name + '-early-start-copy-' + suffix, body))
        for selected_name, loop in loops():
            if not selected_name.startswith(name + '-') or 'unsigned' in selected_name:
                continue
            loop = replace(loop, '                            a = start;\n', '')
            loop = replace(loop, '                            end = (x + dx)',
                           '                            a = start;\n                            end = (x + dx)')
            forms.append((selected_name + '-early-start-copy', loop))
    return forms


def coordinate_candidates():
    forms = []
    bases = [('baseline', recovery.BASELINE), ('side-reuse', CHECKPOINT),
             ('edge-cursor', dict(recovery.cursor_candidates())['edge-cursor']),
             ('side-copies', dict(recovery.cursor_candidates())['edge-cursor-side-copies']),
             ('early-edge', dict(side_lifetimes())['edge-cursor-early-start-copy'])]
    for name, base in bases:
        for owners, kind in itertools.product((False, True), ('s16', 's32')):
            body = base
            body = replace(body, '    s32 id;', '    s32 id;\n    ' + kind + ' bx;\n    ' + kind + ' bz;')
            if owners:
                body = replace(body, '    s32 id;', '    s32 id;\n    ' + kind + ' ox;\n    ' + kind + ' oz;')
            before = '                            nx = (f32)(*(s16 *)(second + 4) - *(s16 *)(first + 4));\n'
            assignments = '                            bz = *(s16 *)(second + 4);\n'
            if owners:
                assignments += '                            oz = *(s16 *)(first + 4);\n'
                assignments += '                            ox = *(s16 *)(first + 0);\n'
            assignments += '                            bx = *(s16 *)(second + 0);\n'
            body = replace(body, before, assignments + before)
            # Rewrite uses only after the loads, leaving each record load intact.
            prefix, calculations = body.split(before, 1)
            calculations = before + calculations
            calculations = calculations.replace('*(s16 *)(second + 0)', 'bx').replace('*(s16 *)(second + 4)', 'bz')
            if owners:
                calculations = calculations.replace('*(s16 *)(first + 0)', 'ox').replace('*(s16 *)(first + 4)', 'oz')
            body = prefix + calculations
            label = name + '-' + ('all' if owners else 'target') + '-coordinates-' + kind
            forms.append((label, body))
            forms.append((label + '-paired-minimum', pair(body, *PAIRS[-1])))
    return forms


def register_candidates():
    base = dict(side_lifetimes())['side-copies-indexed-do-while-reloaded-count-early-start-copy']
    forms = [('indexed-side-lifetime', base)]
    for hints in [('nx',), ('nz',), ('start',), ('end',), ('a',), ('b',), ('ax',), ('az',),
                  ('minimum',), ('fraction',), ('nx', 'nz'), ('a', 'b'), ('start', 'end'),
                  ('nx', 'nz', 'a', 'b'), ('minimum', 'fraction'), ('ax', 'az'),
                  ('count',), ('i',), ('j',), ('id',), ('first',), ('second',), ('cursor',),
                  ('nx', 'nz', 'start', 'end', 'a', 'b')]:
        body = base
        for variable in hints:
            declaration = re.search(r'^    (?:f32|s32|u8 \*)[^\n]*\b' + variable + r';$', body, re.M)
            if declaration is None:
                raise ValueError('missing register declaration: ' + variable)
            body = replace(body, declaration.group(), declaration.group().replace('    ', '    register ', 1))
        forms.append(('register-' + '-'.join(hints), body))
    forms.append(('indexed-side-lifetime-paired-hit', pair(base, *PAIRS[-1])))
    return forms


def declaration_candidates():
    base = dict(side_lifetimes())['side-copies-indexed-do-while-reloaded-count-early-start-copy']
    groups = ('    f32 nx;\n    f32 nz;\n', '    f32 ax;\n    f32 az;\n',
              '    f32 start;\n    f32 end;\n', '    f32 a;\n    f32 b;\n')
    forms = []
    for order in itertools.permutations(range(4)):
        body = base
        for group in groups:
            body = replace(body, group, '')
        body = replace(body, '    f32 swap;', ''.join(groups[i] for i in order) + '    f32 swap;')
        forms.append(('float-order-' + ''.join(map(str, order)), body))
    for mask in range(1, 8):
        body = base
        for bit, group in enumerate((groups[0], groups[2], groups[3])):
            if mask & (1 << bit):
                body = replace(body, group, ''.join(reversed(group.splitlines(keepends=True))))
        forms.append(('float-member-order-' + str(mask), body))
    return forms


def parameter_candidates():
    base = dict(side_lifetimes())['side-copies-indexed-do-while-reloaded-count-early-start-copy']
    forms = []
    for variables in (('nx',), ('nz',), ('nx', 'nz')):
        body = base
        if 'nx' in variables:
            body = replace(body, '    f32 nx;\n', '    f32 query_x;\n')
            body = replace(body, '    band = func_15085DA8(y);',
                           '    query_x = x;\n    band = func_15085DA8(y);')
            prefix, calculations = body.split('                            nx = ', 1)
            calculations = '                            nx = ' + calculations
            calculations = re.sub(r'\bx\b', 'query_x', calculations)
            body = prefix + calculations
            body = re.sub(r'\bnx\b', 'x', body)
        if 'nz' in variables:
            body = replace(body, '    f32 nz;\n', '')
            body = re.sub(r'\bnz\b', 'y', body)
        for initialize in (False, True):
            candidate = body
            if initialize:
                assignments = ''.join('    ' + ('x' if v == 'nx' else 'y') + ' = 0.0f;\n' for v in variables)
                candidate = replace(candidate, '    count = D_80087290;', assignments + '    count = D_80087290;')
            forms.append(('parameter-' + '-'.join(variables) + ('-initialized' if initialize else ''), candidate))
    return forms


def geometry_candidates():
    base = dict(side_lifetimes())['side-copies-indexed-do-while-reloaded-count-early-start-copy']
    forms = []
    groups = (
        ('end_x', 'end_z',
         '                            end = (x + dx) * nx + (z + dz) * nz + constant;',
         '                            end_x = x + dx;\n                            end_z = z + dz;\n'
         '                            end = end_x * nx + end_z * nz + constant;'),
        ('cross_x', 'cross_z',
         '                                a = (x + fraction * dx) * nx +\n'
         '                                        (z + fraction * dz) * nz + constant;',
         '                                cross_x = x + fraction * dx;\n'
         '                                cross_z = z + fraction * dz;\n'
         '                                a = cross_x * nx + cross_z * nz + constant;'),
        ('target_x', 'target_z',
         '                                b = (f32)*(s16 *)(second + 0) * nx +\n'
         '                                      nz * (f32)*(s16 *)(second + 4) + constant;',
         '                                target_x = (f32)*(s16 *)(second + 0);\n'
         '                                target_z = (f32)*(s16 *)(second + 4);\n'
         '                                b = target_x * nx + nz * target_z + constant;'),
        ('tangent_x', 'tangent_z',
         '                                swap = nx;\n                                nx = -nz;\n                                nz = swap;',
         '                                tangent_x = -nz;\n                                tangent_z = nx;\n'
         '                                swap = nx;\n                                nx = tangent_x;\n                                nz = tangent_z;'),
    )
    for mask in range(1, 16):
        body = base
        labels = []
        for bit, (first, second, before, after) in enumerate(groups):
            if mask & (1 << bit):
                body = replace(body, '    f32 swap;', '    f32 ' + first + ';\n    f32 ' + second + ';\n    f32 swap;')
                body = replace(body, before, after)
                labels.append(first.split('_')[0])
        forms.append(('geometry-' + '-'.join(labels), body))
    return forms


SCREENS = {'layouts': layouts, 'loops': loops, 'sides': side_lifetimes,
           'coordinates': coordinate_candidates, 'registers': register_candidates,
           'declarations': declaration_candidates, 'parameters': parameter_candidates,
           'geometry': geometry_candidates}
SELECTED = dict(geometry_candidates())['geometry-cross']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    for mode in SCREENS:
        if mode != 'layouts':
            group.add_argument('--' + mode, action='store_const', const=mode, dest='mode')
    parser.set_defaults(mode='layouts')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-graph-edge-lifetimes'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in SCREENS[args.mode]():
        record, _ = recovery.compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']),
              record['real_differences'], record['diagnostics'], flush=True)
    (output / (args.mode + '.json')).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
