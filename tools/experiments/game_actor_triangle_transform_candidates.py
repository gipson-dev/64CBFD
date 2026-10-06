"""Recover the complete actor triangle remapping, not just its table-null return."""

import json
import struct
import subprocess
from pathlib import Path

from tools.experiments import game_actor_buffer_copy_candidates as copy
from tools.match_progress import load_elf_functions

DECLARATIONS = copy.DECLARATIONS.split('extern u16', 1)[0] + '''
typedef struct ActorVertex58F80 {
    s16 x, y, z;
    u8 pad6[10];
} ActorVertex58F80;
typedef struct ActorRange58F80 {
    u32 start, count, matrix;
} ActorRange58F80;
extern u32 *D_800C6070[];
extern u8 *D_800D19A0[];
extern u16 D_800C5EF8[];
extern ActorRange58F80 *D_800C5C08[];
void func_150A7960(f32 *, f32, f32, f32, f32 *, f32 *, f32 *);
'''

BASELINE = '''void func_1502F490(ActorCopy58F80 *actor, f32 *x, f32 *y, f32 *z, s32 joint) {
    ActorVertex58F80 *vertices[3];
    u32 matrices[3];
    f32 points[2][3][3];
    f32 edgeA[2][3], edgeB[2][3];
    f32 relative[3], blend[3];
    u32 *offsets;
    u8 *base, *matrixBase;
    ActorRange58F80 *range;
    s32 id, count, i, j, pass, axis;
    u32 mask, bit;
    f32 denominator, weightA, weightB;

    id = actor->id;
    offsets = D_800C6070[id];
    if (offsets == NULL) {
        return;
    }
    base = D_800D19A0[id];
    for (i = 0; i != 3; i++) {
        vertices[i] = (ActorVertex58F80 *)(base + offsets[joint * 3 + i]);
    }
    count = D_800C5EF8[id];
    mask = 0;
    for (i = 0; ; i++) {
        if (i == count) {
            return;
        }
        for (j = 0; j != 3; j++) {
            bit = 1u << j;
            if ((mask & bit) == 0) {
                range = D_800C5C08[id] + i;
                if ((u32)vertices[j] >= range->start &&
                    (u32)vertices[j] < range->start + (range->count << 4)) {
                    matrices[j] = range->matrix;
                    mask |= bit;
                }
            }
        }
        if (mask == 7) {
            break;
        }
    }
    matrixBase = actor->buffer;
    if (matrixBase == NULL || actor->source == NULL) {
        return;
    }
    for (pass = 0; pass != 2; pass++) {
        if (pass != 0) {
            matrixBase = actor->source;
        }
        for (j = 0; j != 3; j++) {
            func_150A7960((f32 *)(matrixBase + (matrices[j] << 6)),
                         (f32)vertices[j]->x, (f32)vertices[j]->y, (f32)vertices[j]->z,
                         &points[pass][j][0], &points[pass][j][1], &points[pass][j][2]);
        }
    }
    for (pass = 0; pass != 2; pass++) {
        for (axis = 0; axis != 3; axis++) {
            edgeA[pass][axis] = points[pass][1][axis] - points[pass][0][axis];
            edgeB[pass][axis] = points[pass][2][axis] - points[pass][0][axis];
        }
    }
    relative[0] = *x - points[0][0][0];
    relative[1] = *y - points[0][0][1];
    relative[2] = *z - points[0][0][2];
    denominator = edgeA[0][0] * edgeB[0][2] - edgeB[0][0] * edgeA[0][2];
    if (denominator == 0.0f) {
        weightA = -100.0f;
    } else {
        weightA = (relative[0] * edgeB[0][2] - edgeB[0][0] * relative[2]) / denominator;
    }
    if (weightA < 0.0f || 1.0f < weightA) {
        return;
    }
    if (edgeB[0][2] == 0.0f) {
        weightB = -100.0f;
    } else {
        weightB = (relative[2] - weightA * edgeA[0][2]) / edgeB[0][2];
    }
    if (weightB < 0.0f || 1.0f < weightB) {
        return;
    }
    for (axis = 0; axis != 3; axis++) {
        blend[axis] = edgeB[1][axis] * weightB + weightA * edgeA[1][axis];
    }
    relative[1] = edgeB[0][1] * weightB + weightA * edgeA[0][1];
    *x += ((blend[0] + points[1][0][0]) - relative[0]) - points[0][0][0];
    *y += ((blend[1] + points[1][0][1]) - relative[1]) - points[0][0][1];
    *z += ((blend[2] + points[1][0][2]) - relative[2]) - points[0][0][2];
}'''


def flat_points(body):
    body = body.replace('points[2][3][3]', 'points[6][3]')
    for before, after in (('points[pass][j]', 'points[pass * 3 + j]'),
                          ('points[pass][1]', 'points[pass * 3 + 1]'),
                          ('points[pass][2]', 'points[pass * 3 + 2]'),
                          ('points[pass][0]', 'points[pass * 3]'),
                          ('points[0][0]', 'points[0]'), ('points[1][0]', 'points[3]')):
        body = body.replace(before, after)
    return body


POINTER_TRANSFORMS = '''    triangle = points;
    do {
        if (triangle == points + 3) {
            matrixBase = actor->source;
        }
        vertex = vertices;
        matrix = matrices;
        point = triangle;
        do {
            func_150A7960((f32 *)(matrixBase + (*matrix << 6)),
                         (f32)(*vertex)->x, (f32)(*vertex)->y, (f32)(*vertex)->z,
                         &(*point)[0], &(*point)[1], &(*point)[2]);
            vertex++;
            matrix++;
            point++;
        } while (matrix != matrices + 3);
        triangle += 3;
    } while (triangle != points + 6);
'''


def pointer_transforms(body):
    begin = body.index('    for (pass = 0; pass != 2; pass++) {')
    end = body.index('    for (pass = 0; pass != 2; pass++) {', begin + 1)
    return (body[:begin] + POINTER_TRANSFORMS + body[end:]).replace('    u32 *offsets;',
                '    ActorVertex58F80 **vertex;\n    u32 *matrix;\n    f32 (*point)[3], (*triangle)[3];\n    u32 *offsets;')


def candidates():
    forms = [('baseline', BASELINE)]
    for capacity in (4, 8):
        forms.append((f'vertex-capacity-{capacity}', BASELINE.replace('vertices[3]', f'vertices[{capacity}]', 1)))
    forms.append(('unsigned-id', BASELINE.replace('    s32 id, count, i, j, pass, axis;',
                                                 '    u32 id;\n    s32 count, i, j, pass, axis;')))
    forms.append(('separate-null-gates', BASELINE.replace('if (matrixBase == NULL || actor->source == NULL)',
                           'if (matrixBase == NULL)').replace('    for (pass = 0; pass != 2; pass++) {',
                           '    if (actor->source == NULL) {\n        return;\n    }\n    for (pass = 0; pass != 2; pass++) {', 1)))
    forms.append(('closed-end-negative-control', BASELINE.replace('(u32)vertices[j] < range->start',
                                                                   '(u32)vertices[j] <= range->start')))
    forms.append(('cached-source-negative-control', BASELINE.replace('    u8 *base, *matrixBase;',
                          '    u8 *base, *matrixBase, *source;').replace('    for (pass = 0; pass != 2; pass++) {',
                          '    source = actor->source;\n    for (pass = 0; pass != 2; pass++) {', 1)
                  .replace('            matrixBase = actor->source;', '            matrixBase = source;')))
    forms.append(('sum-weight-negative-control', BASELINE.replace('if (weightB < 0.0f || 1.0f < weightB)',
                                                                  'if (weightB < 0.0f || 1.0f < weightB || weightA + weightB > 1.0f)')))
    forms.append(('wrong-y-negative-control', BASELINE.replace('    relative[1] = edgeB[0][1] * weightB + weightA * edgeA[0][1];\n', '')))
    forms.append(('direct-x-negative-control', BASELINE.replace(
        '    *x += ((blend[0] + points[1][0][0]) - relative[0]) - points[0][0][0];',
        '    *x = blend[0] + points[1][0][0];')))
    flat = flat_points(BASELINE)
    pointers = pointer_transforms(flat)
    forms += [('flat-points', flat), ('pointer-transforms', pointers)]
    for capacity in (4, 8):
        forms.append((f'pointer-vertex-capacity-{capacity}', pointers.replace('vertices[3]', f'vertices[{capacity}]', 1)))
    loop = pointers.replace('    for (i = 0; ; i++) {', '    i = 0;\n    do {').replace(
        '        if (mask == 7) {\n            break;\n        }\n    }',
        '        i++;\n    } while (mask != 7);').replace('j != 3', 'j < 3')
    forms.append(('range-do-loop', loop))
    for name, body in (('pointer', pointers), ('range-do', loop)):
        registered = body
        for declaration in ('ActorVertex58F80 **vertex;', 'u32 *matrix;', 'f32 (*point)[3], (*triangle)[3];',
                            'u32 *offsets;', 'u8 *base, *matrixBase;', 'ActorRange58F80 *range;',
                            's32 id, count, i, j, pass, axis;', 'u32 mask, bit;', 'f32 denominator, weightA, weightB;'):
            registered = registered.replace('    ' + declaration, '    register ' + declaration)
        forms.append((name + '-register-locals', registered))
    return forms


SELECTED = dict(candidates())['pointer-transforms']

MATRIX_BODY = '''void func_150A7960(f32 *matrix, f32 x, f32 y, f32 z, f32 *outX, f32 *outY, f32 *outZ) {
    f32 resultX, resultY, resultZ;

    resultX = (matrix[0] * x + matrix[4] * y) + (matrix[8] * z + matrix[12]);
    resultY = (matrix[1] * x + matrix[5] * y) + (matrix[9] * z + matrix[13]);
    resultZ = (matrix[2] * x + matrix[6] * y) + (matrix[10] * z + matrix[14]);
    *outX = resultX;
    *outY = resultY;
    *outZ = resultZ;
}'''


def compile_candidate(root, output, name, body, function='func_1502F490'):
    conker = root / 'conker'
    path = output / (name + '.c')
    obj, elf = path.with_suffix('.o'), path.with_suffix('.elf')
    path.write_text('#include <ultra64.h>\n' + DECLARATIONS + '\n' + body + '\n')
    command = [str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn',
               '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', '-woff', '649,838']
    for include in ('.', 'include', 'include/2.0L', 'include/2.0L/PR', 'include/libc'):
        command += ['-I', include]
    command += ['-mips2', '-o32', '-O2', '-g3', '-o', str(obj.relative_to(conker)), str(path.relative_to(conker))]
    result = subprocess.run(command, cwd=conker, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    entry, rom_offset, capacity = ((0x1502F490, 0x5C940, 302) if function == 'func_1502F490'
                                   else (0x150A7960, 0xD4E10, 40))
    script = output / 'slot.ld'
    script.write_text(f'SECTIONS {{ .text 0x{entry:X} : SUBALIGN(4) {{ *(.text) }} .rodata 0x80094600 : {{ *(.rodata*) }} }}\n')
    definitions = dict(D_800C6070=0x800C6070, D_800D19A0=0x800D19A0,
                       D_800C5EF8=0x800C5EF8, D_800C5C08=0x800C5C08, func_150A7960=0x150A7960)
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', function,
                    *[f'--defsym={n}=0x{v:X}' for n, v in definitions.items() if n != function], '-o', str(elf), str(obj)],
                   check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0][function]
    size = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    slot = words[:size] + [0] * max(0, capacity - size)
    retail = struct.unpack_from(f'>{capacity}I', (conker / 'conker.us.bin').read_bytes(), rom_offset)
    differences = [(i * 4, f'{a:08X}', f'{b:08X}') for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word) & 0xFFFF for word in words[:20] if word >> 16 == 0x27BD]
    return dict(name=name, body_words=size, frame=frames[0] if frames else 0,
                real_differences=len(differences) + max(0, size - capacity), differences=differences,
                diagnostics=result.stdout + result.stderr), slot


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-triangle-transform'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    record, _ = compile_candidate(root, output, 'ordinary-matrix-control', MATRIX_BODY, 'func_150A7960')
    records.append(record)
    print(record['name'], record['body_words'], hex(record['frame']), record['real_differences'], flush=True)
    (output / 'screen.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
