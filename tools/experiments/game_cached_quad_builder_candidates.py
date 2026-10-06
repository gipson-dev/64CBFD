"""Bound the cached quad builder's control flow and local-allocation choices."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x15140190, 0x16D640, 134
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SYMBOLS = {'func_151D5D60': 0x151D5D60, 'func_150A8050': 0x150A8050,
           'func_150A7960': 0x150A7960, 'memcpy': 0x10022EC0}
DECLARATIONS = '''void func_151D5D60(void *, s16, s32, Vtx **, u8 *);
void func_150A8050(f32 [4][4], f32, f32, f32);
void func_150A7960(f32 *, f32, f32, f32, f32 *, f32 *, f32 *);
'''
SELECTED = '''Vtx *func_15140190(u8 *actor, s16 view) {
    Vtx *cursor;
    Vtx *first;
    f32 matrix[4][4];
    f32 points[4][3];
    u8 i;
    u8 fresh;
    func_151D5D60(actor + 0x100, view, 0x40, &cursor, &fresh);
    first = cursor;
    if (cursor != NULL) {
        if (fresh) {
            memcpy(*(u8 **)(actor + 0x100 + view * 4), actor + 0xC0, 0x40);
            memcpy(*(u8 **)(actor + 0x100 + view * 4) + 0x40, actor + 0xC0, 0x40);
        }
    } else {
        return NULL;
    }
    points[0][2] = 0.0f;
    points[0][0] = *(f32 *)(actor + 0x2C);
    points[0][1] = *(f32 *)(actor + 0x30);
    points[1][0] = -*(f32 *)(actor + 0x2C);
    points[1][1] = *(f32 *)(actor + 0x30);
    points[1][2] = 0.0f;
    points[2][0] = -*(f32 *)(actor + 0x2C);
    points[2][1] = -*(f32 *)(actor + 0x30);
    points[2][2] = 0.0f;
    points[3][0] = *(f32 *)(actor + 0x2C);
    points[3][1] = -*(f32 *)(actor + 0x30);
    points[3][2] = 0.0f;
    func_150A8050(matrix, *(f32 *)(actor + 0x40), *(f32 *)(actor + 0x44), *(f32 *)(actor + 0x48));
    matrix[3][0] = *(f32 *)(actor + 0x34);
    matrix[3][1] = *(f32 *)(actor + 0x38);
    matrix[3][2] = *(f32 *)(actor + 0x3C);
    for (i = 0; i < 4; i++) {
        f32 *point = points[i];
        func_150A7960((f32 *)matrix, point[0], point[1], 0.0f,
                     &point[0], &point[1], &point[2]);
        cursor->v.ob[0] = (s32)point[0];
        cursor->v.ob[1] = (s32)point[1];
        cursor->v.ob[2] = (s32)point[2];
        cursor->v.flag = 0;
        cursor++;
    }
    return first;
}'''


def candidates():
    outer = SELECTED.replace('    } else {\n        return NULL;\n    }', '').replace(
        '    return first;', '    }\n    return first;')
    early = SELECTED.replace('    if (cursor != NULL) {\n', '    if (cursor == NULL) { return NULL; }\n').replace(
        '    } else {\n        return NULL;\n    }', '')
    named = SELECTED.replace('    u8 i;', '    f32 *point;\n    u8 i;').replace(
        '        f32 *point = points[i];', '        point = points[i];')
    return [('selected', SELECTED), ('z-after-colors', SELECTED.replace('    points[0][2] = 0.0f;\n','').replace(
        '    points[1][0]', '    points[0][2] = 0.0f;\n    points[1][0]', 1)),
        ('named-point', named), ('outer-success', outer), ('early-null', early),
        ('wide-counter', SELECTED.replace('    u8 i;', '    s32 i;'))]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+DECLARATIONS+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output/'cached-quad.ld'
    script.write_text('SECTIONS { .text 0x15140190 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_15140190',
        *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_15140190']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>134I', (root/'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word)&65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        differences=len(differences)+max(0, end-WORDS), different_words=differences,
        exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-cached-quad-builder'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name+'-'+profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (output/'measurements.json').write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
