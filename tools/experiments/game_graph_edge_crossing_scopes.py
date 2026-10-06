"""Recover graph-edge calculation scopes and separate plane-value lifetimes."""

import argparse
import hashlib
import itertools
import json
import re
import struct
from pathlib import Path

from tools.experiments import game_graph_edge_crossing_candidates as recovery
from tools.experiments import game_graph_edge_crossing_lifetimes as previous
from tools.experiments.game_record_neighbor_visit_candidates import replace
from tools.match_progress import load_elf_functions


CHECKPOINT = previous.SELECTED
EDGE = '                        if (second[14] == 1) {\n'
CROSSING = '                                if (end < 0.0f) {'
GROUPS = (('nx', 'nz'), ('ax', 'az'), ('constant',), ('start', 'end'),
          ('a', 'b'), ('cross_x', 'cross_z'), ('swap',))


def scope(body, variables, target=EDGE):
    indent = ' ' * (28 if target == EDGE else 32)
    declarations = []
    for variable in variables:
        declaration = '    f32 ' + variable + ';\n'
        body = replace(body, declaration, '')
        declarations.append(indent + declaration.strip() + '\n')
    if target == EDGE:
        return replace(body, target, target + ''.join(declarations))
    return replace(body, target, ''.join(declarations) + target)


def scopes():
    forms = [('edge-scope-' + '-'.join(group), scope(CHECKPOINT, group)) for group in GROUPS]
    all_variables = tuple(itertools.chain.from_iterable(GROUPS))
    forms.append(('edge-scope-all', scope(CHECKPOINT, all_variables)))
    for groups in ((GROUPS[0], GROUPS[2]), (GROUPS[3], GROUPS[4]),
                   GROUPS[:3], GROUPS[3:]):
        variables = tuple(itertools.chain.from_iterable(groups))
        forms.append(('edge-scope-' + '-'.join(variables), scope(CHECKPOINT, variables)))
    for variables in (('cross_x', 'cross_z'), ('swap',), ('cross_x', 'cross_z', 'swap')):
        forms.append(('cross-scope-' + '-'.join(variables), scope(CHECKPOINT, variables, CROSSING)))
    return forms


def separate(body, *, constant=False, normal=False, distances=False, nested=False):
    prefix, crossing = body.split('                                swap = nx;\n', 1)
    crossing = '                                swap = nx;\n' + crossing
    declarations = []
    if normal:
        declarations += ['    f32 tangent_x;\n', '    f32 tangent_z;\n']
        crossing = replace(crossing, '                                swap = nx;\n'
                           '                                nx = -nz;\n                                nz = swap;',
                           '                                tangent_x = -nz;\n                                tangent_z = nx;')
        crossing = re.sub(r'\bnx\b', 'tangent_x', crossing)
        crossing = re.sub(r'\bnz\b', 'tangent_z', crossing)
        # The normal must be read before the new tangent values are assigned.
        crossing = replace(crossing, 'tangent_x = -tangent_z;\n                                tangent_z = tangent_x;',
                           'tangent_x = -nz;\n                                tangent_z = nx;')
        crossing = crossing.replace('swap * az', 'tangent_z * az')
        prefix = replace(prefix, '    f32 swap;\n', '')
    if constant:
        declarations += ['    f32 tangent_constant;\n']
        crossing = re.sub(r'\bconstant\b', 'tangent_constant', crossing)
    if distances:
        declarations += ['    f32 crossing_distance;\n', '    f32 target_distance;\n']
        before, projected = crossing.split('                                cross_x = ', 1)
        projected = '                                cross_x = ' + projected
        projected = re.sub(r'\ba\b', 'crossing_distance', projected)
        projected = re.sub(r'\bb\b', 'target_distance', projected)
        crossing = before + projected
    body = prefix + crossing
    if nested:
        declarations = [line.replace('    ', '                                ', 1) for line in declarations]
        body = replace(body, CROSSING, ''.join(declarations) + CROSSING)
    else:
        body = replace(body, '    band = func_15085DA8(y);', ''.join(declarations) + '\n    band = func_15085DA8(y);')
    return body


def planes():
    forms = []
    for constant, normal, distances, nested in itertools.product((False, True), repeat=4):
        if not any((constant, normal, distances)):
            continue
        body = separate(CHECKPOINT, constant=constant, normal=normal, distances=distances, nested=nested)
        labels = [label for enabled, label in ((constant, 'constant'), (normal, 'normal'),
                  (distances, 'distances'), (nested, 'nested')) if enabled]
        forms.append(('separate-' + '-'.join(labels), body))
    return forms


def aggregate(body, variables, label, array=False):
    marker = '    /* plane-aggregate-declaration */\n'
    body = replace(body, '    f32 ' + variables[0] + ';\n', marker)
    for variable in variables[1:]:
        body = replace(body, '    f32 ' + variable + ';\n', '')
    if array:
        declaration = '    f32 ' + label + '[' + str(len(variables)) + '];\n'
        translations = {v: label + '[' + str(i) + ']' for i, v in enumerate(variables)}
    else:
        declaration = '    struct { ' + ' '.join('f32 ' + v + ';' for v in variables) + ' } ' + label + ';\n'
        translations = {v: label + '.' + v for v in variables}
    body = re.sub(r'\b(' + '|'.join(variables) + r')\b', lambda m: translations[m.group()], body)
    return replace(body, marker, declaration)


def aggregates():
    forms = []
    for variables, label in ((('nx', 'nz', 'constant'), 'plane'),
                             (('ax', 'az', 'nx', 'nz'), 'edge'),
                             (('start', 'end', 'a', 'b'), 'sides'),
                             (('cross_x', 'cross_z', 'swap'), 'crossing')):
        for array in (False, True):
            body = aggregate(CHECKPOINT, variables, label, array)
            forms.append((label + ('-array' if array else '-struct'), body))
    return forms


def operand_candidates(products=False):
    sums = (
        (('x * nx + z * nz', 'z * nz + x * nx'),),
        (('(x + dx) * nx + (z + dz) * nz', '(z + dz) * nz + (x + dx) * nx'),),
        (('cross_x * nx + cross_z * nz', 'cross_z * nz + cross_x * nx'),),
        (('(f32)*(s16 *)(second + 0) * nx +\n                                      nz * (f32)*(s16 *)(second + 4)',
          'nz * (f32)*(s16 *)(second + 4) +\n                                      (f32)*(s16 *)(second + 0) * nx'),),
        (('ax * nx + nz * az', 'nz * az + ax * nx'),
         ('ax * nx + swap * az', 'swap * az + ax * nx')),
    )
    multiplications = (
        (('x * nx', 'nx * x'), ('z * nz', 'nz * z')),
        (('(x + dx) * nx', 'nx * (x + dx)'), ('(z + dz) * nz', 'nz * (z + dz)')),
        (('cross_x * nx', 'nx * cross_x'), ('cross_z * nz', 'nz * cross_z')),
        (('(f32)*(s16 *)(second + 0) * nx', 'nx * (f32)*(s16 *)(second + 0)'),
         ('nz * (f32)*(s16 *)(second + 4)', '(f32)*(s16 *)(second + 4) * nz')),
        (('ax * nx', 'nx * ax'), ('nz * az', 'az * nz'), ('swap * az', 'az * swap')),
    )
    forms = []
    for mask in range(32):
        body = CHECKPOINT
        for bit, changes in enumerate(multiplications if products else sums):
            if mask & (1 << bit):
                for before, after in changes:
                    if products:
                        pattern = r'(?<![A-Za-z0-9_])' + re.escape(before) + r'(?![A-Za-z0-9_])'
                        body, matches = re.subn(pattern, lambda _: after, body)
                        expected = 2 if before == 'ax * nx' else 1
                        if matches != expected:
                            raise ValueError('operand-product anchor no longer binds: ' + before)
                    else:
                        body = replace(body, before, after)
        forms.append((('products-' if products else 'sums-') + str(mask), body))
    return forms


SCREENS = {'scopes': scopes, 'planes': planes, 'aggregates': aggregates,
           'sums': operand_candidates, 'products': lambda: operand_candidates(True)}


def verify_checkpoint(root):
    functions, _, addresses = load_elf_functions(str(root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
    current = {name: dict(address=addresses[name], words=len(words),
               sha256=hashlib.sha256(struct.pack('>%dI' % len(words), *words)).hexdigest())
               for name, words in functions.items()}
    expected = json.loads((root / 'conker/build/game-graph-edge-lifetime-test/after-slots.json').read_text())
    if current != expected:
        raise ValueError('live ELF differs from the 5a2ef56a checkpoint receipt')
    print('Verified live checkpoint:', len(current), 'slots; target', current['func_15086D94']['sha256'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--planes', action='store_const', const='planes', dest='mode')
    group.add_argument('--aggregates', action='store_const', const='aggregates', dest='mode')
    group.add_argument('--sums', action='store_const', const='sums', dest='mode')
    group.add_argument('--products', action='store_const', const='products', dest='mode')
    group.add_argument('--verify-checkpoint', action='store_true')
    parser.set_defaults(mode='scopes')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    if args.verify_checkpoint:
        verify_checkpoint(root)
        return
    output = root / 'conker/build/game-graph-edge-scopes'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in SCREENS[args.mode]():
        record, _ = recovery.compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], record['diagnostics'], flush=True)
    (output / (args.mode + '.json')).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
