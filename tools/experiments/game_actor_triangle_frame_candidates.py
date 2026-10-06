"""Measure phase-local homes against the recovered triangle array layout."""

import argparse
import json
import struct
from pathlib import Path

from tools.experiments import game_actor_triangle_transform_candidates as screen
from tools.experiments import game_actor_triangle_home_candidates as home
from tools.experiments import game_actor_triangle_lifetime_candidates as lifetime


CHECKPOINT = dict(home.candidates())['weights-counters-retail-cut-10']
PHASES = (
    ('range', ('offsets', 'base', 'range', 'id', 'count', 'i', 'j', 'mask', 'bit')),
    ('sdk', ('vertex', 'matrix', 'point', 'triangle', 'matrixBase')),
    ('weights', ('pass', 'axis', 'denominator', 'weightA', 'weightB')),
)


def scoped_homes(body, phases, cut=None):
    if body != CHECKPOINT:
        raise ValueError('triangle private-home checkpoint no longer binds')
    if any(name not in dict(PHASES) for name in phases) or len(set(phases)) != len(phases):
        raise ValueError('unknown or repeated triangle phase')
    signature, contents = body.split('\n', 1)
    start = contents.index('    id = actor->id;')
    matrix = contents.index('    matrixBase = actor->buffer;')
    edges = contents.index('    for (pass = 0;')
    commands = (contents[start:matrix], contents[matrix:edges], contents[edges:contents.rindex('}')])
    header = contents[:start]
    moved = {variable for name, variables in PHASES if name in phases for variable in variables}
    for variable, declaration in home.SCALARS:
        if variable in moved:
            line = '    ' + declaration + '\n'
            if header.count(line) != 1:
                raise ValueError('phase declaration no longer binds: ' + variable)
            header = header.replace(line, '')
    if cut is not None:
        gap_names = ('pass', 'axis', 'denominator', 'weightA', 'weightB')
        gap = [declaration for name, declaration in home.SCALARS if name not in moved and name in gap_names]
        remaining = [declaration for name, declaration in home.SCALARS if name not in moved and name not in gap_names]
        header = ''.join('    ' + line + '\n' for line in
                         remaining[:cut] + home.ARRAYS['retail'][:3] + gap +
                         home.ARRAYS['retail'][3:] + remaining[cut:]) + '\n'
    result = signature + '\n' + header
    for (name, variables), block in zip(PHASES, commands):
        if name not in phases:
            result += block
            continue
        declarations = ''.join('        ' + declaration + '\n' for variable, declaration in home.SCALARS if variable in variables)
        result += '    {\n' + declarations + ''.join('    ' + line for line in block.splitlines(True)) + '    }\n'
    return result + '}'


def candidates():
    forms = [('checkpoint', CHECKPOINT)]
    for mask in range(1, 8):
        phases = tuple(name for index, (name, _) in enumerate(PHASES) if mask & (1 << index))
        label = '-'.join(phases)
        forms.append((label + '-checkpoint-order', scoped_homes(CHECKPOINT, phases)))
        for cut in (0, 5, 10):
            forms.append((label + '-cut-' + str(cut), scoped_homes(CHECKPOINT, phases, cut)))
    return forms


def reuse_bodies():
    reused = lifetime.reuse(screen.RECOVERY)
    names = ('vertex', 'matrix', 'point', 'triangle', 'base', 'range',
             'id', 'count', 'i', 'j', 'mask', 'weightA', 'weightB')
    direct = lifetime.direct_metadata(reused, True, True, False)
    aliased = lifetime.replace(reused, '    ActorRange58F80 *range;\n', '')
    aliased = lifetime.replace(aliased, '                range = D_800C5C08[id] + i;',
                               '                point = (f32 (*)[3])(D_800C5C08[id] + i);')
    for field in ('start', 'count', 'matrix'):
        aliased = aliased.replace('range->' + field, '((ActorRange58F80 *)point)->' + field)
    aliased = lifetime.direct_metadata(aliased, True, True, False)
    return (
        ('reused', reused, names),
        ('direct-id-count', direct, tuple(name for name in names if name not in ('id', 'count'))),
        ('direct-id-count-range', lifetime.direct_metadata(reused),
         tuple(name for name in names if name not in ('id', 'count', 'range'))),
        ('range-point-home', aliased, tuple(name for name in names if name not in ('id', 'count', 'range'))),
    )


def reuse_candidates():
    forms = []
    for label, body, variables in reuse_bodies():
        for range_style in ('for', 'do'):
            loop = body if range_style == 'for' else lifetime.range_loop(body)
            for bound in ('equal', 'less'):
                changed = loop if bound == 'equal' else loop.replace('triangle != points + 6', 'triangle < points + 6')
                signature, rest = changed.split('\n', 1)
                _, commands = rest.split('\n\n', 1)
                gap_names = ('vertex', 'matrix', 'point', 'triangle', 'base')
                gap = [declaration for name, declaration in home.SCALARS if name in gap_names]
                remaining = [declaration for name, declaration in home.SCALARS if name in variables and name not in gap_names]
                for cut in (0, 2, 4):
                    declarations = remaining[:cut] + home.ARRAYS['retail'][:3] + gap + home.ARRAYS['retail'][3:] + remaining[cut:]
                    header = ''.join('    ' + declaration + '\n' for declaration in declarations)
                    result = signature + '\n' + header + '\n' + commands
                    forms.append((f'{label}-{range_style}-{bound}-cut-{cut}', result))
    return forms


def lifetime_trace(words, frame):
    checks = lifetime.layout.checks
    stack = checks.table.STACK - frame

    class Trace(checks.TriangleOracle):
        def __init__(self):
            self.id_reads = self.count_reads = 0
            self.private_y = {'relative': [], 'blend': []}
            super().__init__(words, checks.memory_case())

        def get(self, address, size):
            if self.matrix_calls == 0:
                if (address, size) == (checks.ACTOR + 4, 1):
                    self.id_reads += 1
                if (address, size) == (checks.COUNT_TABLE + 14, 2):
                    self.count_reads += 1
            return super().get(address, size)

        def put(self, address, value, size):
            for name, offset in (('relative', 0x130), ('blend', 0x124)):
                if (address, size) == (stack + offset, 4):
                    self.private_y[name].append(checks.floating(value))
            return super().put(address, value, size)

    trace = Trace().run()
    return dict(pre_sdk_id_reads=trace.id_reads, pre_sdk_count_reads=trace.count_reads,
                private_y=trace.private_y)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reuse', action='store_true', help='combine reduced local counts and phase-dead pointer reuse')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-triangle-frame'
    output.mkdir(exist_ok=True)
    reference = (root / 'conker/conker.us.bin').read_bytes()
    retail = list(struct.unpack_from('>302I', reference, 0x5C940))
    matrix = list(struct.unpack_from('>40I', reference, 0xD4E10))
    records = []
    for name, body in (reuse_candidates() if args.reuse else candidates()):
        record, words = screen.compile_candidate(root, output, name, body)
        record['home_offsets'] = home.homes(words, record['frame'])
        record['bounded_guest_cases'] = lifetime.qualify(words, retail, matrix) if record['body_words'] <= 302 else 0
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'],
              record['home_offsets'], flush=True)
    (output / ('reuse-screen.json' if args.reuse else 'screen.json')).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
