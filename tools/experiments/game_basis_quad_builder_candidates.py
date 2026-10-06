"""Bound the basis-vector quad builder's scalar lifetimes and scheduling."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x15140410, 0x16D8C0, 167
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SYMBOLS = {'func_151D5D60': 0x151D5D60, 'memcpy': 0x10022EC0}
DECLARATIONS = 'void func_151D5D60(void *, s16, s32, Vtx **, u8 *);\n'
SELECTED = '''Vtx *func_15140410(u8 *actor, f32 *widthAxis, f32 *heightAxis, s16 view) {
    Vtx *cursor;
    Vtx *first;
    f32 wx, wy, wz, hx, hy, hz;
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
    wx = *(f32 *)(actor + 0x2C) * widthAxis[0];
    wy = *(f32 *)(actor + 0x2C) * widthAxis[1];
    wz = *(f32 *)(actor + 0x2C) * widthAxis[2];
    hx = *(f32 *)(actor + 0x30) * heightAxis[0];
    hy = *(f32 *)(actor + 0x30) * heightAxis[1];
    hz = *(f32 *)(actor + 0x30) * heightAxis[2];
    cursor[0].v.ob[0] = (s32)((*(f32 *)(actor + 0x34) + wx) + hx);
    cursor[0].v.ob[1] = (s32)((*(f32 *)(actor + 0x38) + wy) + hy);
    cursor[0].v.ob[2] = (s32)((*(f32 *)(actor + 0x3C) + wz) + hz);
    cursor[0].v.flag = 0;
    cursor[1].v.ob[0] = (s32)((*(f32 *)(actor + 0x34) - wx) + hx);
    cursor[1].v.ob[1] = (s32)((*(f32 *)(actor + 0x38) - wy) + hy);
    cursor[1].v.ob[2] = (s32)((*(f32 *)(actor + 0x3C) - wz) + hz);
    cursor[1].v.flag = 0;
    cursor[2].v.ob[0] = (s32)((*(f32 *)(actor + 0x34) - wx) - hx);
    cursor[2].v.ob[1] = (s32)((*(f32 *)(actor + 0x38) - wy) - hy);
    cursor[2].v.ob[2] = (s32)((*(f32 *)(actor + 0x3C) - wz) - hz);
    cursor[2].v.flag = 0;
    cursor[3].v.ob[0] = (s32)((*(f32 *)(actor + 0x34) + wx) - hx);
    cursor[3].v.ob[1] = (s32)((*(f32 *)(actor + 0x38) + wy) - hy);
    cursor[3].v.ob[2] = (s32)((*(f32 *)(actor + 0x3C) + wz) - hz);
    cursor[3].v.flag = 0;
    return first;
}'''


def candidates():
    components_first = SELECTED
    for vector,offset in (('widthAxis',0x2C),('heightAxis',0x30)):
        for axis in range(3):
            load = '*(f32 *)(actor + 0x%X)'%offset
            components_first = components_first.replace('%s * %s[%d]'%(load,vector,axis),
                                                         '%s[%d] * %s'%(vector,axis,load))
    scalars = SELECTED.replace('    f32 wx,', '    f32 width;\n    f32 height;\n    f32 wx,').replace(
        '    wx =', '    width = *(f32 *)(actor + 0x2C);\n    wx =').replace(
        '    hx =', '    height = *(f32 *)(actor + 0x30);\n    hx =')
    scalars = scalars.replace('= *(f32 *)(actor + 0x2C) *', '= width *').replace(
        '= *(f32 *)(actor + 0x30) *', '= height *')
    early = SELECTED.replace('    if (cursor != NULL) {\n', '    if (cursor == NULL) { return NULL; }\n').replace(
        '    } else {\n        return NULL;\n    }', '')
    byte = SELECTED.replace('    Vtx *cursor;', '    u8 *cursor;').replace(
        '&cursor, &fresh', '(Vtx **)&cursor, &fresh').replace('    first = cursor;', '    first = (Vtx *)cursor;')
    for vertex in range(4):
        for axis in range(3):
            byte = byte.replace('cursor[%d].v.ob[%d]'%(vertex,axis), '*(s16 *)(cursor + 0x%X)'%(vertex*16+axis*2))
        byte = byte.replace('cursor[%d].v.flag'%vertex, '*(u16 *)(cursor + 0x%X)'%(vertex*16+6))
    return [('selected',SELECTED),('components-first',components_first),('scalars',scalars),
        ('fresh-first',SELECTED.replace('    u8 fresh;\n','').replace('    f32 wx,', '    u8 fresh;\n    f32 wx,')),
        ('early-null',early),('byte-output',byte)]


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
    script = output/'basis-quad.ld'
    script.write_text('SECTIONS { .text 0x15140410 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_15140410',
        *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_15140410']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>167I', (root/'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word)&65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        differences=len(differences)+max(0, end-WORDS), different_words=differences,
        exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-basis-quad-builder'
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
