"""Recover the rotation/row-scaled matrix and start-point translation stores."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15142838, 0x16FCE8, 55
FUNCTION = 'func_15142838'
SYMBOLS = dict(func_150A8050=0x150A8050, guMtxF2L=0x150A7790)
PROTOTYPE = '''void func_15142838(Mtx *output, f32 row0, f32 row1, f32 rx, f32 ry, f32 rz,
    f32 tx, f32 ty, f32 tz);'''
SELECTED = '''void func_15142838(Mtx *output, f32 row0, f32 row1, f32 rx, f32 ry, f32 rz,
    f32 tx, f32 ty, f32 tz) {
    f32 matrix[4][4];
    func_150A8050(matrix, rx, ry, rz);
    matrix[3][0] = tx;
    matrix[3][1] = ty;
    matrix[3][2] = tz;
    matrix[0][0] *= row0;
    matrix[0][1] *= row0;
    matrix[0][2] *= row0;
    matrix[1][0] *= row1;
    matrix[1][1] *= row1;
    matrix[1][2] *= row1;
    matrix[2][0] *= row0;
    matrix[2][1] *= row0;
    matrix[2][2] *= row0;
    guMtxF2L(matrix, output);
}'''
OLD_CALLER_PROTOTYPE = 's32 func_15142838(void *, f32, f32, f32, f32, f32, f32, f32, f32);'
CALLER = '''s32 func_15133760(u8 *arg0, u8 *arg1) {
    func_15142838(
        (Mtx *)arg0,
        *(f32 *)(arg1 + 0x18),
        *(f32 *)(arg1 + 0x1C),
        *(f32 *)(arg1 + 0x20),
        *(f32 *)(arg1 + 0x24),
        *(f32 *)(arg1 + 0x28),
        *(f32 *)(arg1 + 0x38),
        *(f32 *)(arg1 + 0x3C),
        *(f32 *)(arg1 + 0x40)
    );
    return 1;
}'''
OLD_CALLER = CALLER.replace('(Mtx *)arg0,', 'arg0,')


def candidates():
    for translations_first, columns in itertools.product((False, True), repeat=2):
        body = SELECTED
        translations = '    matrix[3][0] = tx;\n    matrix[3][1] = ty;\n    matrix[3][2] = tz;\n'
        if not translations_first:
            body = body.replace(translations, '').replace('    guMtxF2L(', translations + '    guMtxF2L(')
        if columns:
            lines = [line for line in body.splitlines() if '*=' in line]
            for line in lines:
                body = body.replace(line + '\n', '')
            ordered = [next(line for line in lines if line.startswith('    matrix[%d][%d]' % (r, c))) for c in range(3) for r in range(3)]
            body = body.replace('    guMtxF2L(', '\n'.join(ordered) + '\n    guMtxF2L(')
        yield 'translation%d-columns%d' % (translations_first, columns), body


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
    script = output / 'row-matrix.ld'
    script.write_text('SECTIONS { .text 0x15142838 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
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


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-row-matrix'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record, flush=True)
    (output / 'maintained-measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
