"""Screen private-array orders and explicit matrix-output cursor lifetimes."""

import json
import struct
from pathlib import Path

from tools.experiments import game_actor_triangle_transform_candidates as screen
from tools.tests import test_game_actor_triangle_transform_match as checks


OUTPUT_LOOP = '''    triangle = points;
    do {
        if (triangle == points + 3) {
            matrixBase = actor->source;
        }
        vertex = vertices;
        matrix = matrices;
        byteCursor = 0;
        outX = &triangle[0][0];
        outY = &triangle[0][1];
        outZ = &triangle[0][2];
        do {
            func_150A7960((f32 *)(matrixBase + (*matrix << 6)),
                         (f32)(*vertex)->x, (f32)(*vertex)->y, (f32)(*vertex)->z,
                         outX, outY, outZ);
            vertex++;
            matrix++;
            byteCursor += 12;
            outX += 3;
            outY += 3;
            outZ += 3;
        } while (byteCursor != 36);
        triangle += 3;
    } while (triangle != points + 6);
'''

ARRAYS = '''    ActorVertex58F80 *vertices[3];
    u32 matrices[3];
    f32 points[6][3];
    f32 edgeA[2][3], edgeB[2][3];
    f32 relative[3], blend[3];'''

ORDERS = {
    'reverse-retail-homes': '''    f32 relative[3];
    f32 blend[3];
    u32 matrices[3];
    ActorVertex58F80 *vertices[3];
    f32 points[6][3];
    f32 edgeA[2][3];
    f32 edgeB[2][3];''',
    'forward-retail-homes': '''    f32 edgeB[2][3];
    f32 edgeA[2][3];
    f32 points[6][3];
    ActorVertex58F80 *vertices[3];
    u32 matrices[3];
    f32 blend[3];
    f32 relative[3];''',
}


def candidates():
    begin = screen.SELECTED.index('    triangle = points;')
    end = screen.SELECTED.index('    for (pass = 0;', begin)
    cursors = (screen.SELECTED[:begin] + OUTPUT_LOOP + screen.SELECTED[end:]).replace(
        '    f32 (*point)[3], (*triangle)[3];',
        '    f32 (*triangle)[3];\n    f32 *outX, *outY, *outZ;\n    s32 byteCursor;')
    forms = [('checkpoint', screen.SELECTED), ('three-output-cursors', cursors)]
    for name, body in [('checkpoint', screen.SELECTED), ('output-cursors', cursors)]:
        for order, declarations in ORDERS.items():
            for capacity in (3, 8):
                changed = body.replace(ARRAYS, declarations.replace('vertices[3]', f'vertices[{capacity}]'))
                if changed == body:
                    raise ValueError('array declarations no longer bind to selected source')
                forms.append((f'{name}-{order}-capacity-{capacity}', changed))
    return forms


def qualify(words, retail):
    cases = 0
    for identity in (0, 7, 127, 255):
        for phase in (0, 8):
            for coordinate in ((1.0, 5.5, 1.0), (3.0, 5.5, 3.0), (-1.0, 5.5, 1.0)):
                memory = checks.memory_case(identity=identity, coordinate=coordinate)
                original = checks.TriangleOracle(retail, memory, phase).run()
                candidate = checks.TriangleOracle(words, memory, phase).run()
                if (checks.actor_pass.external_memory(original.memory) != checks.actor_pass.external_memory(candidate.memory)
                        or checks.external_writes(original) != checks.external_writes(candidate)
                        or original.calls != candidate.calls):
                    raise AssertionError(('bounded layout contract differs', identity, phase, coordinate))
                cases += 1
    return cases


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-triangle-layout'
    output.mkdir(exist_ok=True)
    retail = list(struct.unpack_from('>302I', (root / 'conker/conker.us.bin').read_bytes(), 0x5C940))
    records, baseline_words = [], None
    for name, body in candidates():
        record, words = screen.compile_candidate(root, output, name, body)
        if baseline_words is None:
            baseline_words = words
        record['same_as_checkpoint'] = words == baseline_words
        # Fitting forms receive bounded probes, not the complete production suite.
        record['bounded_guest_cases'] = qualify(words, retail) if record['body_words'] <= 302 else 0
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'],
              record['bounded_guest_cases'], 'unchanged' if record['same_as_checkpoint'] else 'different', flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
