"""Screen the source-backed 88-byte effect descriptor without installing it."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x1519ED84, 0x1CC234, 96
CONSTRUCTOR, COPY, TABLE = 0x1513D2F0, 0x10022EC0, 0x800A4AA0
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
LAYOUTS = '''typedef struct { f32 x, y, z; } Position1CBE20;
typedef struct {
    Position1CBE20 position;
    Position1CBE20 vector;
    f32 width;
    f32 height;
} Source1CBE20;
typedef struct {
    u8 mode;
    u8 field01;
    u16 field02;
    s16 lifetime;
    u8 pad06[2];
    u32 field08;
    u32 field0C;
    u8 field10;
    u8 field11;
    u8 field12;
    u8 field13;
    f32 width;
    f32 height;
    Position1CBE20 position;
    Position1CBE20 vector;
    f32 field34;
    f32 field38;
    f32 field3C;
    u32 flags;
    u8 field44;
    u8 field45;
    u8 field46;
    u8 field47;
    u32 field48;
    u8 field4C;
    u8 pad4D[3];
    u32 field50;
    s16 field54;
    s16 field56;
} SourceEffect1CBE20;'''
DECLARATIONS = '''extern s32 D_800A4AA0;
void *func_1513D2F0(void *, s32, u8, u8, u8, u8, u8, s32, s32, s32, u8, s32);
void *memcpy(void *, const void *, u32);
'''
BASELINE = '''void func_1519ED84(Source1CBE20 *source, s32 mode, s16 lifetime, u8 channel, s32 context) {
    SourceEffect1CBE20 packet;
    Source1CBE20 *savedSource;
    u8 *effect;

    savedSource = source;
    packet.field01 = 0;
    packet.field02 = 0x3B03;
    packet.field08 = 0;
    packet.field0C = 0;
    packet.field10 = 255;
    packet.field11 = 255;
    packet.field12 = 255;
    packet.field13 = 255;
    packet.mode = mode;
    packet.lifetime = lifetime;
    packet.width = source->width * 10.0f;
    packet.height = source->height * 10.0f;
    packet.position.x = source->position.x;
    packet.position.y = source->position.y;
    packet.position.z = source->position.z;
    packet.vector.x = source->vector.x;
    packet.vector.y = source->vector.y;
    packet.vector.z = source->vector.z;
    packet.field34 = 1.0f;
    packet.field38 = 1.0f;
    packet.field3C = 1.0f;
    packet.flags = 0x045C0081;
    packet.field44 = 255;
    packet.field45 = 255;
    packet.field46 = 0;
    packet.field47 = 7;
    packet.field48 = 0;
    packet.field4C = 255;
    packet.field50 = 0;
    packet.field54 = 1;
    packet.field56 = 255;
    effect = func_1513D2F0(&packet, (s32)&D_800A4AA0, 39, 0, 0, 23, 0, 3, 255, 4, channel, context);
    if (effect != NULL) {
        memcpy(effect + 0x110, &savedSource, sizeof(savedSource));
    }
}'''
SELECTED = BASELINE.replace('    packet.mode = mode;\n', '').replace('    packet.lifetime = lifetime;\n', '')
SELECTED = SELECTED.replace('    savedSource = source;', '    savedSource = source;\n    packet.mode = mode;').replace(
    '    packet.field02 = 0x3B03;', '    packet.field02 = 0x3B03;\n    packet.lifetime = lifetime;')


def candidates():
    body = BASELINE
    return [('field-order', body),
            ('header-order', SELECTED),
            ('narrow-mode', body.replace('s32 mode,', 'u8 mode,')),
            ('wide-lifetime', body.replace('s16 lifetime,', 's32 lifetime,')),
            ('wide-channel', body.replace('u8 channel,', 's32 channel,')),
            ('mode-first', body.replace('    packet.mode = mode;\n', '').replace(
                '    savedSource = source;', '    savedSource = source;\n    packet.mode = mode;')),
            ('unit-first', body.replace('    packet.field34 = 1.0f;\n    packet.field38 = 1.0f;\n'
                '    packet.field3C = 1.0f;\n', '').replace('    savedSource = source;',
                '    savedSource = source;\n    packet.field34 = 1.0f;\n    packet.field38 = 1.0f;\n    packet.field3C = 1.0f;')),
            ('vector-copy', body.replace('    packet.vector.x = source->vector.x;\n'
                '    packet.vector.y = source->vector.y;\n    packet.vector.z = source->vector.z;',
                '    packet.vector = source->vector;')),
            ('position-copy', body.replace('    packet.position.x = source->position.x;\n'
                '    packet.position.y = source->position.y;\n    packet.position.z = source->position.z;',
                '    packet.position = source->position;')),
            ('captured-factor', body.replace('    u8 *effect;', '    u8 *effect;\n    f32 factor = 10.0f;').replace(
                '* 10.0f;', '* factor;')),
            ('captured-unit', body.replace('    u8 *effect;', '    u8 *effect;\n    f32 unit = 1.0f;').replace(
                'packet.field34 = 1.0f;', 'packet.field34 = unit;').replace('packet.field38 = 1.0f;',
                'packet.field38 = unit;').replace('packet.field3C = 1.0f;', 'packet.field3C = unit;')),
            ('dimensions-first', body.replace('    packet.width = source->width * 10.0f;\n'
                '    packet.height = source->height * 10.0f;\n', '').replace('    savedSource = source;',
                '    savedSource = source;\n    packet.width = source->width * 10.0f;\n    packet.height = source->height * 10.0f;')),
            ('pointer-first', body.replace('    SourceEffect1CBE20 packet;\n    Source1CBE20 *savedSource;',
                '    Source1CBE20 *savedSource;\n    SourceEffect1CBE20 packet;'))]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+LAYOUTS+'\n'+DECLARATIONS+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output/'source-effect.ld'
    script.write_text('SECTIONS { .text 0x1519ED84 : SUBALIGN(4) { *(.text) } }\n')
    symbols = {'func_1513D2F0': CONSTRUCTOR, 'memcpy': COPY, 'D_800A4AA0': TABLE}
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1519ED84',
        *['--defsym=%s=0x%X'%item for item in symbols.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True, text=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1519ED84']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>96I', (root/'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    return dict(name=name, profile=profile, body_words=end, frame=(-words[0]) & 65535,
        differences=len(differences)+max(0, end-WORDS), different_words=differences,
        exact=slot == retail, diagnostics=diagnostics), words


def ordering_candidates():
    assignments = BASELINE.split('    savedSource = source;\n', 1)[1].split('    effect =', 1)[0].splitlines()
    for field in ('mode', 'lifetime', 'field4C', 'field54', 'field56'):
        line = next(a for a in assignments if a.startswith('    packet.'+field+' ='))
        without = [a for a in assignments if a != line]
        indices = range(11) if field in ('mode', 'lifetime') else range(23, len(without)+1)
        for index in indices:
            reordered = without[:index]+[line]+without[index:]
            body = BASELINE.replace('\n'.join(assignments), '\n'.join(reordered))
            yield field+'-at-'+str(index), body


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-source-effect-packet'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name+'-'+profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    for name, body in ordering_candidates():
        record, _ = compile_candidate(root, output, name, body)
        records.append(record)
        print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (output/'measurements.json').write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
