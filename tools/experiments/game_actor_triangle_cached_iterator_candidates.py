"""Screen cached metadata and the retail SDK counter/output-cursor lifetimes."""

import argparse
import json
import struct
from pathlib import Path

from tools.experiments import game_actor_triangle_transform_candidates as screen
from tools.experiments import game_actor_triangle_home_candidates as home
from tools.experiments import game_actor_triangle_frame_candidates as frame
from tools.experiments import game_actor_triangle_lifetime_candidates as lifetime


CHECKPOINT = screen.reduced_frame_body(screen.RECOVERY)
SDK_LOOP = '''    triangle = points;
    do {
        if (triangle == points + 3) {
            base = actor->source;
        }
        matrix = matrices;
        vertex = vertices;
        byteCursor = 0;
        outX = &triangle[0][0];
        outY = &triangle[0][1];
        outZ = &triangle[0][2];
        do {
            func_150A7960((f32 *)(base + (*matrix << 6)),
                         (f32)(*vertex)->x, (f32)(*vertex)->y, (f32)(*vertex)->z,
                         outX, outY, outZ);
            byteCursor += 12;
            matrix++;
            vertex++;
            outX += 3;
            outY += 3;
            outZ += 3;
        } while (byteCursor != 36);
        triangle += 3;
    } while (triangle < points + 6);
'''


def recipes():
    reused = lifetime.reuse(screen.RECOVERY)
    names = ('vertex', 'matrix', 'point', 'triangle', 'base', 'range',
             'id', 'count', 'i', 'j', 'mask', 'weightA', 'weightB')
    forms = []
    for sdk in ('point', 'xyz-counter', 'xyz-i', 'xyz-id'):
        for range_style in ('for', 'do'):
            for inner in ('equal', 'less'):
                for outer in ('equal', 'less'):
                    body = reused if range_style == 'for' else lifetime.range_loop(reused)
                    body = body.replace('j < 3', 'j != 3')
                    if inner == 'less':
                        body = body.replace('j != 3', 'j < 3')
                    if outer == 'less':
                        body = body.replace('i != 2', 'i < 2')
                    body = body.replace('triangle != points + 6', 'triangle < points + 6')
                    variables = list(names)
                    if sdk != 'point':
                        begin = body.index('    triangle = points;')
                        end = body.index('    for (i = 0; i', begin)
                        loop = SDK_LOOP
                        if sdk in ('xyz-i', 'xyz-id'):
                            loop = loop.replace('byteCursor', 'i' if sdk == 'xyz-i' else 'id')
                        else:
                            variables.append('byteCursor')
                        body = body[:begin] + loop + body[end:]
                        variables.remove('point')
                        variables += ['outX', 'outY', 'outZ']
                    forms.append((f'{sdk}-{range_style}-inner-{inner}-edge-{outer}', body, tuple(variables)))
    return forms


def isolate(body, names, mask):
    if mask not in range(8):
        raise ValueError('unknown cached iterator isolation mask')
    signature, rest = body.split('\n', 1)
    old_header, commands = rest.split('\n\n', 1)
    variables, label = list(names), []
    if mask & 1:
        for before, after in (
                ('matrix = D_800C6070[id];', 'offsets = D_800C6070[id];'),
                ('if (matrix == NULL)', 'if (offsets == NULL)'),
                ('base + matrix[joint * 3 + i]', 'base + offsets[joint * 3 + i]')):
            commands = lifetime.replace(commands, before, after)
        variables.append('offsets')
        label.append('offsets')
    if mask & 2:
        begin = commands.index('    base = actor->buffer;')
        commands = commands[:begin] + commands[begin:].replace('base', 'matrixBase')
        variables.append('matrixBase')
        label.append('base')
    if mask & 4:
        end = commands.index('    if (weightA < 0.0f')
        commands = commands[:end].replace('weightB', 'denominator') + commands[end:]
        variables.append('denominator')
        label.append('denominator')
    return '-'.join(label) or 'reused', signature + '\n' + old_header + '\n\n' + commands, tuple(variables)


def isolated_recipes():
    forms = []
    originals = {name: (body, variables) for name, body, variables in recipes()}
    for sdk in ('xyz-counter', 'xyz-id'):
        original, names = originals[sdk + '-for-inner-less-edge-equal']
        for mask in range(1, 8):
            label, body, variables = isolate(original, names, mask)
            forms.append((sdk + '-separate-' + label, body, variables))
    return forms


def mixed_recipes():
    forms = []
    originals = {name: (body, variables) for name, body, variables in recipes()}
    for sdk in ('xyz-counter', 'xyz-id'):
        for range_style in ('for', 'do'):
            for outer in ('equal', 'less'):
                original, names = originals[f'{sdk}-{range_style}-inner-less-edge-{outer}']
                begin = original.index('    for (i = 0; i ' + ('!= 2' if outer == 'equal' else '< 2'))
                mixed = original[:begin] + original[begin:].replace('j < 3', 'j != 3')
                for mask in range(4):
                    label, body, variables = isolate(mixed, names, mask)
                    forms.append((f'{sdk}-{range_style}-mixed-edge-{outer}-' + label, body, variables))
    return forms


def declarations(body, variables, cut):
    if not 0 <= cut <= len(variables) - 5:
        raise ValueError('private-home declaration cut exceeds available locals')
    recipe = next((candidate for _, candidate, names in recipes() + isolated_recipes() + mixed_recipes()
                   if (candidate, names) == (body, variables)), None)
    if recipe is None:
        raise ValueError('cached iterator recipe no longer binds')
    signature, rest = body.split('\n', 1)
    _, commands = rest.split('\n\n', 1)
    scalars = dict(home.SCALARS)
    scalars.update(outX='f32 *outX;', outY='f32 *outY;', outZ='f32 *outZ;', byteCursor='s32 byteCursor;')
    gap = ('vertex', 'matrix', 'point', 'triangle', 'base') if 'point' in variables else (
        'vertex', 'matrix', 'outX', 'outY', 'outZ')
    remaining = [name for name in variables if name not in gap]
    header = ([scalars[name] for name in remaining[:cut]] + home.ARRAYS['retail'][:3] +
              [scalars[name] for name in gap] + home.ARRAYS['retail'][3:] +
              [scalars[name] for name in remaining[cut:]])
    return signature + '\n' + ''.join('    ' + line + '\n' for line in header) + '\n' + commands


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--isolated', action='store_true', help='separate early pointer and determinant definitions')
    mode.add_argument('--mixed', action='store_true', help='use retail distinct range/edge inner bounds')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-triangle-cached-iterators'
    output.mkdir(exist_ok=True)
    reference = (root / 'conker/conker.us.bin').read_bytes()
    retail = list(struct.unpack_from('>302I', reference, 0x5C940))
    matrix = list(struct.unpack_from('>40I', reference, 0xD4E10))
    records = []
    expected_homes = home.homes(retail, 0x138)
    forms = isolated_recipes() if args.isolated else mixed_recipes() if args.mixed else recipes()
    for name, body, variables in forms:
        first, _ = screen.compile_candidate(root, output, name + '-unplaced', declarations(body, variables, 0))
        cut = (first['frame'] - 0x138) // 4
        if not 0 <= cut <= len(variables) - 5:
            raise ValueError(('frame cannot recover retail homes without added locals', name, first['frame']))
        record, words = screen.compile_candidate(root, output, name, declarations(body, variables, cut))
        record['placement_cut'] = cut
        record['unplaced_frame'] = first['frame']
        record['unplaced_diagnostics'] = first['diagnostics']
        record['home_offsets'] = home.homes(words, record['frame'])
        record['homes_match_retail'] = record['home_offsets'] == expected_homes
        record['lifetime_trace'] = frame.lifetime_trace(words, record['frame'])
        record['bounded_guest_cases'] = lifetime.qualify(words, retail, matrix) if record['body_words'] <= 302 else 0
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'],
              record['placement_cut'], record['lifetime_trace'], flush=True)
    filename = 'isolated-screen.json' if args.isolated else 'mixed-screen.json' if args.mixed else 'screen.json'
    (output / filename).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
