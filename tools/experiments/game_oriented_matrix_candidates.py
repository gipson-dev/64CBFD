"""Screen the two-point oriented matrix without rewriting its retail frame."""

import itertools
import json
import re
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15142600, 0x16FAB0, 142
FUNCTION = 'func_15142600'
SYMBOLS = {'guMtxF2L': 0x150A7790}
PROTOTYPE = '''void func_15142600(Mtx *output, f32 row0, f32 row1, f32 cx, f32 cy, f32 cz,
    f32 sx, f32 sy, f32 sz, f32 ex, f32 ey, f32 ez);'''
SELECTED = '''typedef struct { f32 x, z; } OrientedHorizontal;
void func_15142600(Mtx *output, f32 row0, f32 row1, f32 cx, f32 cy, f32 cz,
    f32 sx, f32 sy, f32 sz, f32 ex, f32 ey, f32 ez) {
    f32 dx, dy, dz;
    struct17 direction;
    OrientedHorizontal left;
    f32 up[3];
    f32 matrix[4][4];
    f32 inverse;
    dx = ex - sx;
    dy = ey - sy;
    dz = ez - sz;
    inverse = 1.0f / sqrtf(dx * dx + dy * dy + dz * dz);
    direction.unk0 = dx * inverse;
    direction.unk4 = dy * inverse;
    direction.unk8 = dz * inverse;
    left.x = direction.unk8;
    left.z = -direction.unk0;
    inverse = 1.0f / sqrtf(left.x * left.x + left.z * left.z);
    left.x *= inverse;
    left.z *= inverse;
    up[0] = direction.unk4 * left.z;
    up[1] = direction.unk8 * left.x - direction.unk0 * left.z;
    up[2] = -direction.unk4 * left.x;
    inverse = 1.0f / sqrtf(up[0] * up[0] + up[1] * up[1] + up[2] * up[2]);
    matrix[0][0] = left.x * cx * row0;
    matrix[1][0] = up[0] * inverse * cx * row1;
    matrix[2][0] = direction.unk0 * cx * row0;
    matrix[3][0] = sx;
    matrix[0][1] = 0.0f;
    matrix[1][1] = up[1] * inverse * cy * row1;
    matrix[2][1] = direction.unk4 * cy * row0;
    matrix[3][1] = sy;
    matrix[0][2] = left.z * cz * row0;
    matrix[1][2] = up[2] * inverse * cz * row1;
    matrix[2][2] = direction.unk8 * cz * row0;
    matrix[3][2] = sz;
    matrix[0][3] = 0.0f;
    matrix[1][3] = 0.0f;
    matrix[2][3] = 0.0f;
    matrix[3][3] = 1.0f;
    guMtxF2L(matrix, output);
}'''
OLD_CALLER_PROTOTYPE = 's32 func_15142600(s32, s32, s32, s32, f32, f32, f32, f32, f32, f32, f32, f32);'
CALLER = '''s32 func_150B9D14(Mtx *output, u8 *source) {
    func_15142600(output,
                  *(f32 *)(source + 0x18),
                  *(f32 *)(source + 0x1C),
                  *(f32 *)(source + 0x2C),
                  *(f32 *)(source + 0x30),
                  *(f32 *)(source + 0x34),
                  *(f32 *)(source + 0x38),
                  *(f32 *)(source + 0x3C),
                  *(f32 *)(source + 0x40),
                  *(f32 *)(source + 0x20),
                  *(f32 *)(source + 0x24),
                  *(f32 *)(source + 0x28));
    return 1;
}'''
LEGACY_CALLER = '''s32 func_150B9D14(s32 arg0, u8 *arg1) {
    func_15142600(arg0, *(s32 *) (arg1 + 0x18), *(s32 *) (arg1 + 0x1C),
                   *(s32 *) (arg1 + 0x2C), *(f32 *) (arg1 + 0x30),
                   *(f32 *) (arg1 + 0x34), *(f32 *) (arg1 + 0x38),
                   *(f32 *) (arg1 + 0x3C), *(f32 *) (arg1 + 0x40),
                   *(f32 *) (arg1 + 0x20), *(f32 *) (arg1 + 0x24),
                   *(f32 *) (arg1 + 0x28));
    return 1;
}'''


def candidates():
    for up_struct, columns, early in itertools.product((False, True), repeat=3):
        body = SELECTED
        if not columns:
            lines = [line for line in body.splitlines() if line.startswith('    matrix[')]
            start, end = body.index(lines[0]), body.index('    guMtxF2L(')
            body = body[:start] + '\n'.join(sorted(lines)) + '\n' + body[end:]
        if early:
            line = '    matrix[0][0] = left.x * cx * row0;\n'
            body = body.replace(line, '').replace('    inverse = 1.0f / sqrtf(up[0]',
                line + '    inverse = 1.0f / sqrtf(up[0]')
        if up_struct:
            body = body.replace('    f32 up[3];', '    struct17 up;')
            for i, field in enumerate(('unk8', 'unk4', 'unk0')):
                body = body.replace('up[%d]' % i, 'up.' + field)
        yield 'up%d-columns%d-early%d' % (up_struct, columns, early), body


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n' + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2',
        '-o32', '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I',
        'conker/include/2.0L/PR', '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2',
        '-D_MIPS_SZLONG=32', *PROFILES[profile], '-o', str(obj.relative_to(root)),
        str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'oriented.ld'
    script.write_text('SECTIONS { .text 0x15142600 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e',
        FUNCTION, *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o',
        str(elf), str(obj)], check=True, capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta = functions[FUNCTION]
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), sections(elf)['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, object_words=meta['size'] // 4,
        frame=frames[0] if frames else 0, diagnostics=diagnostics, relocations=relocations,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def layout_candidates():
    base = dict(candidates())['up1-columns1-early0']
    declarations = ('    struct17 direction;\n', '    OrientedHorizontal left;\n',
                    '    struct17 up;\n', '    f32 matrix[4][4];\n')
    for late_direction, reverse_direction, capture_start in itertools.product((False, True), repeat=3):
        body = base
        if late_direction:
            for declaration in declarations:
                body = body.replace(declaration, '')
            body = body.replace('    f32 dx, dy, dz;\n',
                '    f32 dx, dy, dz;\n' + ''.join(declarations[i] for i in (1, 3, 0, 2)))
        if reverse_direction:
            body = body.replace('direction.unk0', 'direction.TEMP').replace(
                'direction.unk8', 'direction.unk0').replace('direction.TEMP', 'direction.unk8')
        if capture_start:
            body = body.replace('    dx =', '    f32 px, py, pz;\n'
                '    px = sx;\n    py = sy;\n    pz = sz;\n    dx =', 1)
            for index, axis in enumerate('xyz'):
                body = body.replace('e%s - s%s' % (axis, axis), 'e%s - p%s' % (axis, axis)).replace(
                    'matrix[3][%d] = s%s;' % (index, axis), 'matrix[3][%d] = p%s;' % (index, axis))
        yield 'layout%d-reverse%d-capture%d' % (late_direction, reverse_direction, capture_start), body


def inplace_candidates():
    layouts = dict(layout_candidates())
    for point_left, direction_inplace, up_inplace, capture in itertools.product((False, True), repeat=4):
        body = layouts['layout1-reverse1-capture%d' % capture]
        if point_left:
            body = body.replace('    OrientedHorizontal left;', '    struct17 left;')
            body = body.replace('left.x', 'left.unk0').replace('left.z', 'left.unk8')
        if direction_inplace:
            body = body.replace('    f32 dx, dy, dz;\n', '')
            for old, field in zip(('dx', 'dy', 'dz'), ('unk8', 'unk4', 'unk0')):
                body = body.replace('    direction.%s = %s * inverse;\n' % (field, old),
                    '    direction.%s *= inverse;\n' % field)
                body = re.sub(r'\b' + old + r'\b', 'direction.' + field, body)
        if up_inplace:
            assignments = ''.join('    up.%s *= inverse;\n' % field for field in ('unk8', 'unk4', 'unk0'))
            body = body.replace('    matrix[0][0]', assignments + '    matrix[0][0]', 1)
            for field in ('unk8', 'unk4', 'unk0'):
                body = body.replace('up.%s * inverse *' % field, 'up.%s *' % field)
        yield 'inplace%d%d%d%d' % (point_left, direction_inplace, up_inplace, capture), body


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-oriented-matrix'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in itertools.chain(candidates(), layout_candidates(), inplace_candidates()):
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record, flush=True)
    (output / 'maintained-measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
