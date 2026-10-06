"""Measure private homes while interleaving scalar and array declarations."""

import argparse
import json
import struct
from pathlib import Path

from tools.experiments import game_actor_triangle_transform_candidates as screen
from tools.experiments import game_actor_triangle_lifetime_candidates as lifetime
from tools.experiments import game_actor_triangle_layout_candidates as layout


SCALARS = [
    ('vertex', 'ActorVertex58F80 **vertex;'), ('matrix', 'u32 *matrix;'),
    ('point', 'f32 (*point)[3];'), ('triangle', 'f32 (*triangle)[3];'),
    ('offsets', 'u32 *offsets;'), ('base', 'u8 *base;'), ('matrixBase', 'u8 *matrixBase;'),
    ('range', 'ActorRange58F80 *range;'), ('id', 's32 id;'), ('count', 's32 count;'),
    ('i', 's32 i;'), ('j', 's32 j;'), ('pass', 's32 pass;'), ('axis', 's32 axis;'),
    ('mask', 'u32 mask;'), ('bit', 'u32 bit;'),
    ('denominator', 'f32 denominator;'), ('weightA', 'f32 weightA;'), ('weightB', 'f32 weightB;'),
]

ARRAYS = {
    'retail': ['f32 relative[3];', 'f32 blend[3];', 'u32 matrices[3];',
               'ActorVertex58F80 *vertices[3];', 'f32 points[6][3];',
               'f32 edgeA[2][3];', 'f32 edgeB[2][3];'],
    'checkpoint': ['ActorVertex58F80 *vertices[3];', 'u32 matrices[3];',
                   'f32 points[6][3];', 'f32 edgeA[2][3];', 'f32 edgeB[2][3];',
                   'f32 relative[3];', 'f32 blend[3];'],
}


def candidates():
    forms = [('checkpoint', screen.RECOVERY)]
    signature, commands = screen.RECOVERY.split('    id = actor->id;', 1)
    signature = signature[:signature.index('\n')]
    for group, names in (
            ('weights-counters', ('denominator', 'weightA', 'weightB', 'pass', 'axis')),
            ('range-counters', ('id', 'count', 'i', 'j', 'mask'))):
        gap = [declaration for name, declaration in SCALARS if name in names]
        remaining = [declaration for name, declaration in SCALARS if name not in names]
        for cut in (0, 5, 8, 10, 12, 14):
            for order, arrays in ARRAYS.items():
                header = remaining[:cut] + arrays[:3] + gap + arrays[3:] + remaining[cut:]
                body = signature + '\n' + ''.join('    ' + line + '\n' for line in header)
                body += '\n    id = actor->id;' + commands
                forms.append((f'{group}-{order}-cut-{cut}', body))
    return forms


def loop_candidates():
    base = dict(candidates())['weights-counters-retail-cut-10']
    forms = [('retail-homes', base), ('retail-homes-range-do', lifetime.range_loop(base))]
    forms.append(('retail-homes-range-less', base.replace('j != 3', 'j < 3')))
    for range_style in ('for', 'do'):
        for outer in ('equal', 'less'):
            body = screen.RECOVERY if range_style == 'for' else lifetime.range_loop(screen.RECOVERY)
            begin = body.index('    triangle = points;')
            end = body.index('    for (pass = 0;', begin)
            body = body[:begin] + layout.OUTPUT_LOOP + body[end:]
            if outer == 'less':
                body = body.replace('triangle != points + 6', 'triangle < points + 6')
            signature, commands = body.split('    id = actor->id;', 1)
            signature = signature[:signature.index('\n')]
            scalars = [(name, declaration) for name, declaration in SCALARS if name != 'point']
            scalars += [('outX', 'f32 *outX;'), ('outY', 'f32 *outY;'), ('outZ', 'f32 *outZ;'),
                        ('byteCursor', 's32 byteCursor;')]
            gap_names = ('denominator', 'weightA', 'weightB', 'pass', 'axis')
            gap = [declaration for name, declaration in scalars if name in gap_names]
            remaining = [declaration for name, declaration in scalars if name not in gap_names]
            for cut in (12, 14):
                header = remaining[:cut] + ARRAYS['retail'][:3] + gap + ARRAYS['retail'][3:] + remaining[cut:]
                changed = signature + '\n' + ''.join('    ' + line + '\n' for line in header)
                changed += '\n    id = actor->id;' + commands
                forms.append((f'cursors-{range_style}-{outer}-cut-{cut}', changed))
    return forms


def homes(words, frame):
    checks = lifetime.layout.checks

    class HomeOracle(checks.TriangleOracle):
        def record_call(self, target):
            if target == checks.MATRIX:
                self.point_homes.append(self.arguments(7)[4])
            super().record_call(target)

    model = HomeOracle(words, checks.memory_case())
    model.point_homes = []
    model.run()
    bottom = checks.table.STACK - frame

    def find(values):
        result = []
        for offset in range(0x50, frame - len(values) * 4 + 1, 4):
            if [model.peek(bottom + offset + i * 4, 4) for i in range(len(values))] == values:
                result.append(offset)
        return result

    return dict(vertices=find([checks.VERTICES + i * 16 for i in range(3)]),
                matrices=find([0, 1, 2]),
                points=[address - bottom for address in model.point_homes],
                edgeA=find(list(map(checks.bits, (4, 2, 0, 4, 2, 0)))),
                edgeB=find(list(map(checks.bits, (0, 3, 4, 0, 3, 4)))),
                relative_blend=find(list(map(checks.bits, (1, 1.25, 1)))))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--loops', action='store_true', help='screen loop controls against the recovered homes')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-triangle-homes'
    output.mkdir(exist_ok=True)
    reference = (root / 'conker/conker.us.bin').read_bytes()
    retail = list(struct.unpack_from('>302I', reference, 0x5C940))
    matrix = list(struct.unpack_from('>40I', reference, 0xD4E10))
    records = []
    print('retail homes', homes(retail, 0x138), flush=True)
    for name, body in (loop_candidates() if args.loops else candidates()):
        record, words = screen.compile_candidate(root, output, name, body)
        record['home_offsets'] = homes(words, record['frame'])
        record['bounded_guest_cases'] = lifetime.qualify(words, retail, matrix) if record['body_words'] <= 302 else 0
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'],
              record['home_offsets'], flush=True)
    (output / ('loop-screen.json' if args.loops else 'screen.json')).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
