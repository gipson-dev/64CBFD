"""Screen byte-indexed view-corner initialization at fixed retail anchors."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS, TABLE = 0x1513FFF4, 0x16D4A4, 55, 0x80090B60
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SELECTED = '''void func_1513FFF4(u8 *out, u8 index, u8 variant) {
    typedef struct {
        u8 prefix[6];
        u16 width;
        u16 height;
        u8 tail[2];
    } ViewDimensions169510;
    extern ViewDimensions169510 D_80090B60[];
    ViewDimensions169510 *record;
    u16 width, height;
    s32 coordinate;

    if (index != 255) {
        record = &D_80090B60[index];
        width = record->width - 1;
        height = record->height - 1;
        coordinate = (variant & 1) ? width << 6 : 0;
        *(s16 *)(out + 0x38) = coordinate;
        *(s16 *)(out + 0x08) = coordinate;
        coordinate = (variant & 1) ? 0 : width << 6;
        *(s16 *)(out + 0x28) = coordinate;
        *(s16 *)(out + 0x18) = coordinate;
        coordinate = (variant & 2) ? height << 6 : 0;
        *(s16 *)(out + 0x1A) = coordinate;
        *(s16 *)(out + 0x0A) = coordinate;
        coordinate = (variant & 2) ? 0 : height << 6;
        *(s16 *)(out + 0x3A) = coordinate;
        *(s16 *)(out + 0x2A) = coordinate;
    }
}'''


def candidates():
    repeated = SELECTED.replace('    ViewDimensions169510 *record;\n', '').replace('    s32 coordinate;\n', '').replace(
        '        record = &D_80090B60[index];\n', '').replace('record->width', 'D_80090B60[index].width').replace(
        'record->height', 'D_80090B60[index].height')
    for expression, offsets in (('(variant & 1) ? width << 6 : 0', (0x38, 8)),
                               ('(variant & 1) ? 0 : width << 6', (0x28, 0x18)),
                               ('(variant & 2) ? height << 6 : 0', (0x1A, 0xA)),
                               ('(variant & 2) ? 0 : height << 6', (0x3A, 0x2A))):
        repeated = repeated.replace('        coordinate = '+expression+';\n', '')
        for offset in offsets:
            repeated = repeated.replace('*(s16 *)(out + 0x%02X) = coordinate;'%offset,
                                        ('*(s16 *)(out + 0x%02X) = '%offset)+expression+';')
    no_pointer = SELECTED.replace('    ViewDimensions169510 *record;\n', '').replace(
        '        record = &D_80090B60[index];\n', '').replace('record->width', 'D_80090B60[index].width').replace(
        'record->height', 'D_80090B60[index].height')
    declaration = SELECTED[SELECTED.index('    typedef struct'):SELECTED.index('    ViewDimensions169510 *record;')]
    global_type = declaration.replace('    ', '')+'\n'+SELECTED.replace(declaration, '')
    return [('repeated', repeated), ('shared-halfword', no_pointer.replace('s32 coordinate;', 's16 coordinate;')),
            ('shared-word', no_pointer), ('record-pointer', SELECTED),
            ('coordinate-first', SELECTED.replace('    ViewDimensions169510 *record;\n    u16 width, height;\n    s32 coordinate;',
                '    s32 coordinate;\n    u16 width, height;\n    ViewDimensions169510 *record;')),
            ('height-first', SELECTED.replace('u16 width, height;', 'u16 height, width;')),
            ('unsigned-coordinate', SELECTED.replace('s32 coordinate;', 'u32 coordinate;')),
            ('register-coordinate', SELECTED.replace('s32 coordinate;', 'register s32 coordinate;')),
            ('address-abi', SELECTED.replace('u8 *out, u8 index', 's32 address, u8 index').replace(
                '    ViewDimensions169510 *record;', '    u8 *out = (u8 *)address;\n    ViewDimensions169510 *record;')),
            ('global-declaration', global_type)]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output/'view-corners.ld'
    script.write_text('SECTIONS { .text 0x1513FFF4 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1513FFF4',
                    '--defsym=D_80090B60=0x80090B60', '-o', str(elf), str(obj)], check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1513FFF4']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>55I', (root/'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word)&65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        differences=len(differences)+max(0, end-WORDS), different_words=differences,
        exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-view-corner-initializer'
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
