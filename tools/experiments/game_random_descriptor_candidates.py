"""Screen the original random descriptor and sixteen-argument submit call."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15141F78, 0x16F428, 96
FUNCTION = 'func_15141F78'
SYMBOLS = dict(func_150ADA20=0x150ADA20, func_150ADA68=0x150ADA68,
               func_1513C650=0x1513C650)
PROTOTYPE = 'void func_15141F78(u8 slot, u8 *source, f32 scale, u8 tag, f32 *position, u8 mode);'
DECLARATIONS = '''typedef struct {
    s32 flags;
    s16 lifetime;
    u8 slot, kind;
    s32 zero8, zeroC;
    u8 random, value11, value12, value13, value14, value15, zero16, seven;
    s32 effect, sourceWord;
    u8 value20, pad21;
    s16 size, count;
} GameRandomDescriptor;
'''
SELECTED = '''void func_15141F78(u8 slot, u8 *source, f32 scale, u8 tag, f32 *position, u8 mode) {
    struct157 descriptor;
    f32 range;
    s32 enabled;
    descriptor.unk6 = slot;
    descriptor.unk7 = 0;
    descriptor.unk0 = 0x6F701;
    descriptor.unk4 = (u32)func_150ADA20() % 61U + 100;
    descriptor.unk8 = 0;
    descriptor.unkC = 0;
    descriptor.unk10 = (func_150ADA20() & 0x7F) + 128;
    descriptor.unk11 = 0xFF;
    descriptor.unk12 = 0xFF;
    descriptor.unk13 = 0xFF;
    descriptor.unk14 = 0xFF;
    descriptor.unk15 = 0xFF;
    descriptor.unk18 = 0x3B0002;
    descriptor.unk16 = 0;
    descriptor.unk17 = 7;
    descriptor.unk20 = 0xFF;
    descriptor.unk1C = *(s32 *)(source + 0x18);
    descriptor.unk22 = 0x28;
    descriptor.unk24 = 6;
    range = (func_150ADA68() * 5.0f + 10.0f) * scale;
    if (mode == 2) {
        enabled = 1;
    } else {
        enabled = 0;
    }
    func_1513C650((s32)&descriptor, 0, 0, (s32)(source + 4),
        position[0], *(f32 *)source, position[2], range, range,
        tag, enabled, 3, 1, 0, 255, 1);
}'''
UNSIGNED = SELECTED.replace('struct157 descriptor;', 'GameRandomDescriptor descriptor;')
for old, new in (('unk0', 'flags'), ('unk4', 'lifetime'), ('unk6', 'slot'), ('unk7', 'kind'),
    ('unk8', 'zero8'), ('unkC', 'zeroC'), ('unk10', 'random'), ('unk11', 'value11'),
    ('unk12', 'value12'), ('unk13', 'value13'), ('unk14', 'value14'), ('unk15', 'value15'),
    ('unk16', 'zero16'), ('unk17', 'seven'), ('unk18', 'effect'), ('unk1C', 'sourceWord'),
    ('unk20', 'value20'), ('unk22', 'size'), ('unk24', 'count')):
    UNSIGNED = UNSIGNED.replace('descriptor.'+old+' =', 'descriptor.'+new+' =')
SIGNED = SELECTED
SELECTED = UNSIGNED


def candidates():
    for unsigned, byte, conditional, swapped in itertools.product((False, True), repeat=4):
        body = SELECTED if unsigned else SIGNED
        if byte:
            body = body.replace('    s32 enabled;', '    u8 enabled;')
        if conditional:
            body = body.replace('    if (mode == 2) {\n        enabled = 1;\n    } else {\n        enabled = 0;\n    }',
                                '    enabled = mode == 2;')
        if swapped:
            descriptor = 'GameRandomDescriptor' if unsigned else 'struct157'
            body = body.replace('    '+descriptor+' descriptor;\n    f32 range;',
                                '    f32 range;\n    '+descriptor+' descriptor;')
        yield 'shape-%d%d%d%d' % (unsigned, byte, conditional, swapped), body


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n#include "variables.h"\n'+DECLARATIONS+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output/'descriptor.ld'
    script.write_text('SECTIONS { .text 0x15141F78 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocs = parse_object(obj)
    function = functions[FUNCTION]
    text = sections(elf)['.text'][1]
    words = list(struct.unpack_from('>%dI' % (function['size']//4), text, function['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    retail = struct.unpack_from('>96I', (root/'conker/conker.us.bin').read_bytes(), ROM)
    record = dict(name=name, profile=profile, body_words=end, object_words=function['size']//4,
        frame=frames[0] if frames else 0, diagnostics=diagnostics,
        differences=sum(a!=b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        relocations=relocs)
    return record, words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-random-descriptor'
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
