"""Screen source lifetimes without changing the recovered query layout."""

import argparse
import itertools
import json
import re
from pathlib import Path

from tools.experiments import game_zone_neighbor_selection_candidates as baseline


def context_pointer(body, flags=False):
    return baseline.retain_query_pointer(body, flags)


def guarded_actor(body):
    opening = ('        for (player = D_8008FD90, actor = D_800CC2D0 + player * 0x32C;\n'
               '             player < D_8008FD8C; player++, actor += 0x32C) {')
    body = baseline.replace(body, opening,
                            '        player = D_8008FD90;\n'
                            '        if (player < D_8008FD8C) {\n'
                            '            actor = D_800CC2D0 + player * 0x32C;\n'
                            '            do {')
    return baseline.replace(body, '        }\n    }\n    for (i = 0; i < D_8008FD8C;',
                            '                player++;\n'
                            '                actor += 0x32C;\n'
                            '            } while (player < D_8008FD8C);\n'
                            '        }\n    }\n    for (i = 0; i < D_8008FD8C;')


def cached_coordinates(body):
    body = baseline.replace(body, '    f32 minimum;',
                            '    f32 minimum;\n    f32 actorX;\n    f32 actorZ;')
    body = baseline.replace(body, '                        nodes = D_800D2350;',
                            '                        nodes = D_800D2350;\n'
                            '                        actorX = *(f32 *)(actor + 0x14);\n'
                            '                        actorZ = *(f32 *)(actor + 0x1C);')
    return body.replace('- *(f32 *)(actor + 0x14)', '- actorX').replace(
        '- *(f32 *)(actor + 0x1C)', '- actorZ')


def deferred_zone(body):
    # Derive from the cached selection pointer, not a freshly loaded global.
    body = baseline.replace(body, '    zone = (u8 *)D_800D23B0 + 0x1748;\n', '')
    return baseline.replace(body,
        '    for (i = 0; i < *(s8 *)((u8 *)D_800D23B0 + 0x1745); i++, zone += 12)',
        '    for (i = 0, zone = (u8 *)selections + 0x11EC;\n'
        '         i < *(s8 *)((u8 *)D_800D23B0 + 0x1745); i++, zone += 12)')


def candidates():
    frozen = dict(baseline.candidates())
    forms = []
    for source, pointer, guarded, cached, deferred in itertools.product(
            ('retail-byte-cursors', 'retail-remainder-z-reuse'),
            ('object', 'context', 'flags'), (False, True), (False, True), (False, True)):
        body = frozen[source]
        if pointer != 'object':
            body = context_pointer(body, pointer == 'flags')
        if guarded:
            body = guarded_actor(body)
        if cached:
            body = cached_coordinates(body)
        if deferred:
            body = deferred_zone(body)
        name = '-'.join((source, pointer, 'guard' if guarded else 'for',
                         'cached' if cached else 'loads', 'deferred' if deferred else 'early'))
        forms.append((name, body))
    for name, body in list(forms):
        if '-flags-guard-cached-' in name:
            # Preserve byte narrowing even when the expression is held as a word.
            narrowed = re.sub(r'best = ([^;]+);', lambda m:
                             m[0] if m[1] == '0xFF' else 'best = (u8)(%s);' % m[1], body)
            forms.append((name + '-byte-best', narrowed.replace('    s32 best;', '    u8 best;')))
    return forms


def cursor_candidates():
    original = dict(baseline.candidates())['retail-remainder-z-reuse']
    forms = []
    for ids, distances, pointer, byte_best in itertools.product(
            (False, True), (False, True), (False, True), (False, True)):
        body = original
        if ids:
            body = body.replace('ids = query.ids + j;', 'ids = (u8 *)&query + j;')
            body = re.sub(r'ids\[([0-3])\]', lambda m: 'ids[%d]' % (int(m[1]) + 46), body)
        if distances:
            body = body.replace('distances = query.distances + j;',
                                'distances = (f32 *)((u8 *)&query + j * 4);')
            body = body.replace('end = query.distances + query.count;',
                                'end = (f32 *)((u8 *)&query + query.count * 4);')
            body = re.sub(r'distances\[([0-3])\]',
                          lambda m: 'distances[%d]' % (int(m[1]) + 3), body)
        if pointer:
            body = context_pointer(body)
        if byte_best:
            body = body.replace('    s32 best;', '    u8 best;')
        name = 'cursor-%s-%s-%s-%s' % ('ids' if ids else 'direct',
                                     'distances' if distances else 'direct',
                                     'context' if pointer else 'object',
                                     'byte' if byte_best else 'word')
        forms.append((name, body))
    return forms


def register_candidates():
    controls = dict(cursor_candidates())
    forms = []
    declarations = ('    s32 i;', '    s32 best;', '    s32 j;',
                    '    u8 *zone;', '    s32 *selections;',
                    '    NeighborVisitQueryB3020 *context;',
                    '    s32 ready;', '    u8 *nodes;',
                    '    u8 *ids;', '    f32 *distances;', '    f32 *end;')
    for source in ('cursor-direct-direct-object-word',
                   'cursor-direct-distances-context-word'):
        body = controls[source]
        for number, declaration in enumerate(declarations):
            if declaration in body:
                forms.append((source + '-register-%d' % number,
                              baseline.replace(body, declaration,
                                               declaration.replace('    ', '    register ', 1))))
        forms.append((source + '-register-scalars',
                      re.sub(r'^    (s32|f32|u8 \*)', r'    register \1', body, flags=re.M)))
    return forms


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--cursors', action='store_true')
    group.add_argument('--registers', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-zone-neighbor-lifetimes'
    output.mkdir(exist_ok=True)
    records = []
    mode = 'registers' if args.registers else 'cursors' if args.cursors else 'screen'
    forms = {'registers': register_candidates, 'cursors': cursor_candidates,
             'screen': candidates}[mode]()
    for name, body in forms:
        record, _ = baseline.compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']),
              record['real_differences'], flush=True)
    (output / (mode + '.json')).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
