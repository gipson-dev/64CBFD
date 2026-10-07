"""Screen the point transform and its observable diagnostic status writes."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15143134, 0x1705E4, 98
FUNCTION = 'func_15143134'
PROTOTYPE = 'void func_15143134(f32 *point, f32 *output, u8 *matrix);'
SYMBOLS = dict(D_800DCA00=0x800DCA00, D_800DCA04=0x800DCA04,
    D_800DCA08=0x800DCA08, D_800DCA0C=0x800DCA0C, D_800DCA10=0x800DCA10,
    D_800C3E90=0x800C3E90, guMtxL2F=0x151EFEB8,
    func_150A7960=0x150A7960, func_15142314=0x15142314)
DECLARATIONS = '''extern volatile s32 D_800DCA00;
extern u8 *D_800DCA04;
extern f32 D_800DCA08, D_800DCA0C, D_800DCA10;
extern u8 D_800C3E90;
void func_150A7960(f32 matrix[4][4], f32 x, f32 y, f32 z,
    f32 *outputX, f32 *outputY, f32 *outputZ);
void func_15142314(u8 *matrix, s32 index, f32 *output);
'''
OWNER_DECLARATIONS = DECLARATIONS.split('extern u8 D_800C3E90;', 1)[0]
SELECTED = '''void func_15143134(f32 *point, f32 *output, u8 *matrix) {
    f32 converted[4][4];
    D_800DCA00 = 1;
    if (point != NULL && (point[0] != 0.0f || point[1] != 0.0f || point[2] != 0.0f)) {
        D_800DCA00 = 2;
        D_800DCA08 = point[0];
        D_800DCA0C = point[1];
        D_800DCA10 = point[2];
        if (D_800C3E90 != 0) {
            D_800DCA00 = 3;
            D_800DCA04 = matrix;
            guMtxL2F(converted, (Mtx *)matrix);
            func_150A7960(converted, point[0], point[1], point[2],
                &output[0], &output[1], &output[2]);
            D_800DCA00 = 4;
            D_800DCA00 = 0;
            return;
        } else {
            D_800DCA00 = 5;
            D_800DCA04 = matrix;
            func_150A7960((f32 (*)[4])matrix, point[0], point[1], point[2],
                &output[0], &output[1], &output[2]);
            D_800DCA00 = 6;
        }
    } else {
        D_800DCA00 = 7;
        func_15142314(matrix, 0, output);
        D_800DCA00 = 8;
    }
    D_800DCA00 = 0;
}'''


def owner_guards():
    changes = (
        (0x4, 0xAFB10028, 0xAFB30030, '-'),
        (0x8, 0x3C110000, 0x3C130000, 'R_MIPS_HI16:D_800DCA00'),
        (0xC, 0xAFB30030, 0xAFB2002C, '-'),
        (0x10, 0xAFB2002C, 0xAFB10028, '-'),
        (0x1C, 0x00A09025, 0x00A08825, '-'),
        (0x20, 0x00C09825, 0x00C09025, '-'),
        (0x24, 0x26310000, 0x26730000, 'R_MIPS_LO16:D_800DCA00'),
        (0x34, 0xAE2E0000, 0xAE6E0000, '-'),
        (0x50, 0xAE2F0000, 0xAE6F0000, '-'),
        (0x64, 0xAE2F0000, 0xAE6F0000, '-'),
        (0x7C, 0xAE2F0000, 0xAE6F0000, '-'),
        (0xB4, 0xAE390000, 0xAE790000, '-'),
        (0xBC, 0xAC330000, 0xAC320000, 'R_MIPS_LO16:D_800DCA04'),
        (0xC8, 0x02602825, 0x02402825, '-'),
        (0xD8, 0x26480004, 0x26280004, '-'),
        (0xDC, 0x26490008, 0x26290008, '-'),
        (0xE8, 0xAFB20010, 0xAFB10010, '-'),
        (0xF8, 0xAE2A0000, 0xAE6A0000, '-'),
        (0x100, 0xAE200000, 0xAE600000, '-'),
        (0x108, 0xAE2B0000, 0xAE6B0000, '-'),
        (0x110, 0xAC330000, 0xAC320000, 'R_MIPS_LO16:D_800DCA04'),
        (0x120, 0x264C0004, 0x262C0004, '-'),
        (0x124, 0x264D0008, 0x262D0008, '-'),
        (0x130, 0xAFB20010, 0xAFB10010, '-'),
        (0x138, 0x02602025, 0x02402025, '-'),
        (0x144, 0xAE2E0000, 0xAE6E0000, '-'),
        (0x14C, 0xAE2F0000, 0xAE6F0000, '-'),
        (0x150, 0x02602025, 0x02402025, '-'),
        (0x15C, 0x02403025, 0x02203025, '-'),
        (0x164, 0xAE380000, 0xAE780000, '-'),
        (0x168, 0xAE200000, 0xAE600000, '-'))
    return [dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % offset,
        expected='0x%08X' % expected, replacement='0x%08X' % replacement,
        expected_relocations=reloc, replacement_relocations=reloc,
        note='Normalize point transform closed saved-register cycle and independent save schedule',
        insert_after='', insert_after_relocations='', omit='false')
        for offset, expected, replacement, reloc in changes]


def candidates():
    for pointer, inverted in itertools.product((False, True), repeat=2):
        body = SELECTED
        if pointer:
            body = body.replace('    f32 converted[4][4];',
                '    f32 converted[4][4];\n    volatile s32 *status = &D_800DCA00;')
            body = body.replace('    D_800DCA00 =', '    *status =')
        if inverted:
            body = body.replace('point[0] != 0.0f || point[1] != 0.0f || point[2] != 0.0f',
                '!(point[0] == 0.0f && point[1] == 0.0f && point[2] == 0.0f)')
        yield 'pointer%d-inverted%d' % (pointer, inverted), body
    yield 'split-outer-clear', SELECTED.replace('            D_800DCA00 = 0;\n            return;\n', '').replace(
        '            D_800DCA00 = 6;\n        }', '            D_800DCA00 = 6;\n        }\n        D_800DCA00 = 0;').replace(
        '        D_800DCA00 = 8;\n    }\n    D_800DCA00 = 0;', '        D_800DCA00 = 8;\n        D_800DCA00 = 0;\n    }')
    yield 'goto-done', SELECTED.replace('            return;', '            goto done;').replace(
        '    D_800DCA00 = 0;\n}', '    D_800DCA00 = 0;\ndone:\n    ;\n}')
    for mask in range(8):
        body = SELECTED
        for bit, value in enumerate((4, 0, 6)):
            if mask & (1 << bit):
                body = body.replace('D_800DCA00 = %d;' % value, '*(volatile s32 *)&D_800DCA00 = %d;' % value)
        yield 'cast%d' % mask, body
    for shape in ('array', 'struct', 'register-args'):
        if shape == 'array':
            body = SELECTED.replace('D_800DCA00 =', 'D_800DCA00[0] =')
        elif shape == 'struct':
            body = SELECTED.replace('D_800DCA00 =', 'D_800DCA00.value =')
        else:
            body = SELECTED.replace('f32 *point, f32 *output, u8 *matrix)',
                'register f32 *point, register f32 *output, register u8 *matrix)')
        yield shape, body


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3', declarations=DECLARATIONS):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n' + declarations + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2',
        '-o32', '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I',
        'conker/include/2.0L/PR', '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2',
        '-D_MIPS_SZLONG=32', *PROFILES[profile], '-o', str(obj.relative_to(root)),
        str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'point.ld'
    script.write_text('SECTIONS { .text 0x15143134 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta = functions[FUNCTION]
    pools = sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:]); words = words[:end]
    retail = struct.unpack_from('>98I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, object_words=meta['size'] // 4,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics=diagnostics, frame=frames[0] if frames else 0,
        relocations=relocations, pool_bytes=len(pools.get('.rodata', (0, b''))[1])), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-point-transform'; output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for volatile in (True, False):
            declarations = DECLARATIONS if volatile else DECLARATIONS.replace('volatile ', '')
            if name == 'array':
                declarations = declarations.replace('s32 D_800DCA00;', 's32 D_800DCA00[];')
            elif name == 'struct':
                declarations = declarations.replace('extern volatile s32 D_800DCA00;',
                    'extern struct { volatile s32 value; } D_800DCA00;').replace(
                    'extern s32 D_800DCA00;', 'extern struct { s32 value; } D_800DCA00;')
            for profile in ('o2g3',):
                record, _ = compile_candidate(root, output,
                    name + '-volatile%d-' % volatile + profile, body, profile, declarations)
                records.append(record)
                print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
