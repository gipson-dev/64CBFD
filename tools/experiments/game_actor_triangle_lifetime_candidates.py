"""Screen phase-local lifetimes and dead temporary reuse in triangle remapping."""

import json
import struct
from pathlib import Path

from tools.experiments import game_actor_triangle_transform_candidates as screen
from tools.experiments import game_actor_triangle_layout_candidates as layout


def replace(body, before, after):
    if before not in body:
        raise ValueError('candidate replacement no longer binds: ' + before)
    return body.replace(before, after)


def reuse(body):
    body = replace(body, 's32 id, count, i, j, pass, axis;', 's32 id, count, i, j;')
    body = replace(body, 'for (pass = 0; pass != 2; pass++)', 'for (i = 0; i != 2; i++)')
    body = replace(body, 'for (axis = 0; axis != 3; axis++)', 'for (j = 0; j != 3; j++)')
    body = body.replace('[pass]', '[i]').replace('pass * 3', 'i * 3').replace('[axis]', '[j]')
    body = replace(body, 'u8 *base, *matrixBase;', 'u8 *base;')
    body = body.replace('matrixBase', 'base')
    body = replace(body, 'u32 mask, bit;', 'u32 mask;')
    body = replace(body, '            bit = 1u << j;\n', '')
    body = replace(body, '(mask & bit)', '(mask & (1u << j))')
    body = replace(body, 'mask |= bit;', 'mask |= 1u << j;')
    body = replace(body, 'f32 denominator, weightA, weightB;', 'f32 weightA, weightB;')
    body = body.replace('denominator', 'weightB')
    body = replace(body, '    u32 *matrix;\n    f32 (*point)[3], (*triangle)[3];\n    u32 *offsets;',
                   '    u32 *matrix;\n    f32 (*point)[3], (*triangle)[3];')
    body = body.replace('offsets', 'matrix')
    return body


def scoped(body):
    declarations = '''        u32 *offsets;
        u8 *base;
        ActorRange58F80 *range;
        s32 id, count, i, j;
        u32 mask, bit;
'''
    for line in ('    u32 *offsets;\n', '    u8 *base, *matrixBase;\n',
                 '    ActorRange58F80 *range;\n', '    s32 id, count, i, j, pass, axis;\n', '    u32 mask, bit;\n'):
        body = replace(body, line, '')
    begin = body.index('    id = actor->id;')
    end = body.index('    matrixBase = actor->buffer;')
    block = body[begin:end]
    body = body[:begin] + '    {\n' + declarations + ''.join('    ' + line for line in block.splitlines(True)) + '    }\n' + body[end:]
    body = replace(body, '    ActorVertex58F80 **vertex;\n', '    s32 pass, axis;\n    u8 *matrixBase;\n    ActorVertex58F80 **vertex;\n')
    return body


def range_loop(body):
    body = replace(body, '    for (i = 0; ; i++) {', '    i = 0;\n    do {')
    return replace(body, '        if (mask == 7) {\n            break;\n        }\n    }',
                   '        i++;\n    } while (mask != 7);').replace('j != 3', 'j < 3')


def edge_pointers(body):
    begin = body.index('    for (i = 0; i != 2; i++) {')
    end = body.index('    relative[0]', begin)
    block = '''    triangle = points;
    a = edgeA;
    b = edgeB;
    do {
        outA = *a;
        outB = *b;
        for (j = 0; j != 3; j++) {
            *outA++ = triangle[1][j] - triangle[0][j];
            *outB++ = triangle[2][j] - triangle[0][j];
        }
        triangle += 3;
        a++;
        b++;
    } while (b != edgeB + 2);
'''
    body = body[:begin] + block + body[end:]
    return replace(body, '    u32 *matrix;', '    f32 (*a)[3], (*b)[3];\n    f32 *outA, *outB;\n    u32 *matrix;')


def direct_metadata(body, remove_id=True, remove_count=True, remove_range=True):
    if remove_id:
        body = replace(body, '    id = actor->id;\n', '').replace('[id]', '[actor->id]')
    if remove_count:
        identity = 'actor->id' if remove_id else 'id'
        body = replace(body, f'    count = D_800C5EF8[{identity}];\n', '')
        body = replace(body, 'i == count', f'i == D_800C5EF8[{identity}]')
    if remove_range:
        identity = 'actor->id' if remove_id else 'id'
        body = replace(body, '    ActorRange58F80 *range;\n', '')
        body = replace(body, f'                range = D_800C5C08[{identity}] + i;\n', '')
        for field in ('start', 'count', 'matrix'):
            body = body.replace('range->' + field, f'D_800C5C08[{identity}][i].{field}')
    variables = [v for v in ('id', 'count', 'i', 'j') if not
                 (v == 'id' and remove_id or v == 'count' and remove_count)]
    return replace(body, '    s32 id, count, i, j;', '    s32 ' + ', '.join(variables) + ';')


def indexed_vertices(body):
    body = replace(body, '    ActorVertex58F80 **vertex;\n', '')
    body = replace(body, '        vertex = vertices;\n', '')
    body = replace(body, '            vertex++;\n', '')
    return body.replace('(*vertex)', 'vertices[matrix - matrices]')


def phase_blocks(body):
    declarations_end = body.index('    ActorVertex58F80 **vertex;')
    range_start = body.index('    id = actor->id;')
    matrix_start = body.index('    matrixBase = actor->buffer;')
    edges_start = body.index('    for (pass = 0;')
    blocks = [
        ('''        u32 *offsets;
        u8 *base;
        ActorRange58F80 *range;
        s32 id, count, i, j;
        u32 mask, bit;
''', body[range_start:matrix_start]),
        ('''        ActorVertex58F80 **vertex;
        u32 *matrix;
        f32 (*point)[3], (*triangle)[3];
        u8 *matrixBase;
''', body[matrix_start:edges_start]),
        ('''        s32 pass, axis;
        f32 denominator, weightA, weightB;
''', body[edges_start:-1]),
    ]
    result = body[:declarations_end]
    for declarations, contents in blocks:
        result += '    {\n' + declarations + ''.join('    ' + line for line in contents.splitlines(True)) + '    }\n'
    return result + '}'


def ternary_weights(body):
    body = replace(body, '''    if (denominator == 0.0f) {
        weightA = -100.0f;
    } else {
        weightA = (relative[0] * edgeB[0][2] - edgeB[0][0] * relative[2]) / denominator;
    }''', '''    weightA = denominator == 0.0f ? -100.0f :
        (relative[0] * edgeB[0][2] - edgeB[0][0] * relative[2]) / denominator;''')
    return replace(body, '''    if (edgeB[0][2] == 0.0f) {
        weightB = -100.0f;
    } else {
        weightB = (relative[2] - weightA * edgeA[0][2]) / edgeB[0][2];
    }''', '''    weightB = edgeB[0][2] == 0.0f ? -100.0f :
        (relative[2] - weightA * edgeA[0][2]) / edgeB[0][2];''')


def short_metadata(body):
    body = replace(body, '    s32 id, count, i, j, pass, axis;',
                   '    u8 id;\n    u16 count;\n    s32 i, j, pass, axis;')
    return body


def nonzero_weights(body, mode):
    if mode not in ('if', 'ternary', 'truthy', 'initialized'):
        raise ValueError('unknown weight selection mode: ' + mode)
    for value, target, formula in (
            ('denominator', 'weightA', '(relative[0] * edgeB[0][2] - edgeB[0][0] * relative[2]) / denominator'),
            ('edgeB[0][2]', 'weightB', '(relative[2] - weightA * edgeA[0][2]) / edgeB[0][2]')):
        before = f'''    if ({value} == 0.0f) {{
        {target} = -100.0f;
    }} else {{
        {target} = {formula};
    }}'''
        if mode == 'if':
            after = f'''    if ({value} != 0.0f) {{
        {target} = {formula};
    }} else {{
        {target} = -100.0f;
    }}'''
        elif mode in ('ternary', 'truthy'):
            condition = value + ' != 0.0f' if mode == 'ternary' else value
            after = f'    {target} = {condition} ? {formula} : -100.0f;'
        else:
            after = f'''    {target} = -100.0f;
    if ({value} != 0.0f) {{
        {target} = {formula};
    }}'''
        body = replace(body, before, after)
    return body


def candidates():
    reused = reuse(screen.SELECTED)
    scoped_body = scoped(screen.SELECTED)
    forms = [('checkpoint', screen.SELECTED), ('phase-scopes', scoped_body), ('reused-temporaries', reused)]
    forms.append(('scopes-range-do', scoped(range_loop(screen.SELECTED))))
    forms.append(('reused-range-do', range_loop(reused)))
    forms.append(('reused-edge-pointers', edge_pointers(reused)))
    forms.append(('reused-range-do-edge-pointers', edge_pointers(range_loop(reused))))
    for name, body in forms[2:].copy():
        forms.append((name + '-vertex-capacity-8', body.replace('vertices[3]', 'vertices[8]', 1)))
    for remove_id, remove_count, remove_range in ((True, False, False), (False, True, False),
            (False, False, True), (True, True, False), (True, True, True)):
        label = 'direct-' + '-'.join(n for n, yes in zip(('id', 'count', 'range'),
                                                       (remove_id, remove_count, remove_range)) if yes)
        changed = direct_metadata(reused, remove_id, remove_count, remove_range)
        forms.append((label, changed))
    direct = direct_metadata(reused)
    forms.append(('direct-metadata-indexed-vertices', indexed_vertices(direct)))
    forms.append(('direct-metadata-range-do-indexed-vertices', indexed_vertices(range_loop(direct))))
    for label, body in [('all-phase-blocks', phase_blocks(screen.SELECTED)),
                        ('all-phase-blocks-range-do', phase_blocks(range_loop(screen.SELECTED)))]:
        forms.append((label, body))
        forms.append((label + '-vertex-capacity-8', body.replace('vertices[3]', 'vertices[8]', 1)))
    ternary = ternary_weights(screen.SELECTED)
    cursors = dict(layout.candidates())['three-output-cursors']
    for label, body in [('ternary-weights', ternary), ('ternary-range-do', range_loop(ternary)),
                        ('short-metadata', short_metadata(screen.SELECTED)),
                        ('output-cursors-less-bound', cursors.replace('triangle != points + 6', 'triangle < points + 6')),
                        ('checkpoint-less-bound', screen.SELECTED.replace('triangle != points + 6', 'triangle < points + 6')),
                        ('output-cursors-ternary', ternary_weights(cursors)),
                        ('reused-ternary', reuse(ternary))]:
        forms.append((label, body))
    for mode in ('if', 'ternary', 'truthy', 'initialized'):
        forms.append(('nonzero-weights-' + mode, nonzero_weights(screen.SELECTED, mode)))
    return forms


def qualify(words, retail, matrix):
    checks = layout.checks
    connected = {checks.MATRIX + i * 4: word for i, word in enumerate(matrix)}
    cases = 0

    def compare(memory, phase=0, joint=0, actions=None, outputs=None):
        nonlocal cases
        calls = None if actions else connected
        original = checks.TriangleOracle(retail, memory, phase, joint, actions, calls, outputs).run()
        candidate = checks.TriangleOracle(words, memory, phase, joint, actions, calls, outputs).run()
        if (checks.actor_pass.external_memory(original.memory) != checks.actor_pass.external_memory(candidate.memory)
                or checks.external_writes(original) != checks.external_writes(candidate)
                or original.calls != candidate.calls):
            raise AssertionError(('lifetime contract differs', cases, phase, joint))
        cases += 1

    for identity in (0, 7, 127, 255):
        for phase in (0, 8):
            for coordinate in ((1.0, 5.5, 1.0), (3.0, 5.5, 3.0), (-1.0, 5.5, 1.0)):
                compare(checks.memory_case(identity=identity, coordinate=coordinate), phase)
    for variant in (0, 1):
        memory = checks.memory_case()
        fields = ((4, 2), (8, 0), (16, 2), (20, 2)) if variant == 0 else (
            (12, checks.VERTICES), (16, 3), (20, 1))
        for offset, value in fields:
            checks.put(memory, checks.RANGES + offset, value)
        for offset in range(24, 36):
            del memory[checks.RANGES + offset]
        for phase in (0, 8):
            compare(memory, phase)
    mutations = ({0: ((checks.ACTOR + 0x1D8, checks.ALTERNATE, 4),)},
                 {0: ((checks.ACTOR + 0x1D4, checks.ALTERNATE, 4),)},
                 {0: ((checks.ACTOR + 4, 99, 1), (checks.COUNT_TABLE + 14, 0, 2))},
                 {0: ((checks.VERTICES + 16, 8, 2), (checks.VERTICES + 18, -32768, 2))},
                 {2: ((checks.ACTOR + 0x1D4, checks.ALTERNATE, 4),)},
                 {3: ((checks.ACTOR + 0x1D4, checks.ALTERNATE, 4),)},
                 {5: ((checks.OUTPUT, checks.bits(3.0), 4), (checks.OUTPUT + 4, checks.bits(-4.5), 4))})
    for actions in mutations:
        for phase in (0, 8):
            compare(checks.memory_case(), phase, actions=actions)
    for mode in range(5):
        memory = checks.memory_case()
        if mode == 0:
            checks.put(memory, checks.OFFSET_TABLE + 28, 0)
            for i in range(4):
                del memory[checks.ACTOR + 0x1D8 + i]
        elif mode in (1, 2):
            checks.put(memory, checks.COUNT_TABLE + 14, 0 if mode == 1 else 2, 2)
        elif mode == 3:
            checks.put(memory, checks.ACTOR + 0x1D8, 0)
            for i in range(4):
                del memory[checks.ACTOR + 0x1D4 + i]
        else:
            checks.put(memory, checks.ACTOR + 0x1D4, 0)
        compare(memory)
    for vertices in (((0, 0, 0), (4, 2, 0), (8, 3, 0)),
                     ((0, 0, 0), (0, 2, 4), (4, 3, 0)),
                     ((-32768, -1, -32768), (32767, 32767, -32768), (-32768, -32768, 32767))):
        for phase in (0, 8):
            compare(checks.memory_case(vertices=vertices), phase)
    for offsets in ((0, 0, 0), (0, 0, 8), (0, 4, 0), (0, 4, 4)):
        compare(checks.memory_case(), outputs=tuple(checks.OUTPUT + o for o in offsets))
    compare(checks.memory_case(vertices=((0, 0, 0), (32, 2, 0), (0, 3, 4)),
                              coordinate=(100000008.0, 5.5, 1.0),
                              translations=((100000000.0, 0, 0), (10, 20, 30), (-3, -4, -5))))
    for joint in (0x8000, 0xFFFF):
        for phase in (0, 8):
            compare(checks.memory_case(joint=joint), phase, joint)
    for count in (0x8000, 0xFFFF):
        for phase in (0, 8):
            memory = checks.memory_case()
            checks.put(memory, checks.COUNT_TABLE + 14, count, 2)
            compare(memory, phase)
    return cases


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-triangle-lifetime'
    output.mkdir(exist_ok=True)
    reference = (root / 'conker/conker.us.bin').read_bytes()
    retail = list(struct.unpack_from('>302I', reference, 0x5C940))
    matrix = list(struct.unpack_from('>40I', reference, 0xD4E10))
    records = []
    for name, body in candidates():
        record, words = screen.compile_candidate(root, output, name, body)
        record['bounded_guest_cases'] = qualify(words, retail, matrix) if record['body_words'] <= 302 else 0
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'],
              record['bounded_guest_cases'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
