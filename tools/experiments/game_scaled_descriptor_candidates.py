"""Screen a scaled 76-byte descriptor and its original position subrecord."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15142180, 0x16F630, 80
FUNCTION = 'func_15142180'
SYMBOLS = dict(D_800A5470=0x800A5470, D_800A5474=0x800A5474, func_15153F18=0x15153F18)
PROTOTYPE = 'void func_15142180(u8 slot, struct17 *source, s32 word, f32 width, f32 height);'
LAYOUT = '''typedef struct {
    s16 value0, value2, value4, value6;
    struct17 point;
    f32 value14, value18, value1C, value20, value24, value28;
    s16 value2C, value2E, value30, value32, value34, value36, value38, value3A;
    u8 slot, pad3D[3];
    f32 value40;
    s16 value44, value46;
    s32 word48;
} GameScaledDescriptor;
'''
LOCAL_DECLARATIONS = LAYOUT+'''extern f32 D_800A5470, D_800A5474;
void func_15153F18(GameScaledDescriptor *, struct17 *, s32, u8, s32);
'''
SELECTED = '''void func_15142180(u8 slot, struct17 *source, s32 word, f32 width, f32 height) {
    GameScaledDescriptor descriptor;
    descriptor.point = *source;
    descriptor.value14 = 2.5f * width;
    descriptor.value18 = 2 * width;
    descriptor.value1C = D_800A5470;
    descriptor.value20 = D_800A5474;
    descriptor.value2C = 3;
    descriptor.value2E = 3;
    descriptor.value2 = 255;
    descriptor.value4 = -25;
    descriptor.value6 = 10;
    descriptor.value30 = 3;
    descriptor.value24 = 3.0f * height;
    descriptor.value28 = 3.5f * height;
    descriptor.value0 = 0;
    descriptor.value32 = 1;
    descriptor.value34 = 9;
    descriptor.value36 = 15;
    descriptor.value38 = 180;
    descriptor.value3A = 75;
    descriptor.value44 = 12;
    descriptor.value46 = 21;
    descriptor.value40 = 0.0f;
    descriptor.word48 = word;
    descriptor.slot = slot;
    func_15153F18(&descriptor, &descriptor.point, 0, 255, 1);
}'''


def candidates():
    for aggregate, integer_two, late_header, constants_first in itertools.product((False, True), repeat=4):
        body = SELECTED
        if not aggregate:
            body = body.replace('    descriptor.point = *source;',
                '    descriptor.point.unk0 = source->unk0;\n    descriptor.point.unk4 = source->unk4;\n'
                '    descriptor.point.unk8 = source->unk8;')
        if not integer_two:
            body=body.replace('2 * width','2.0f * width')
        if not late_header:
            body=body.replace('    descriptor.value4 = -25;\n    descriptor.value6 = 10;\n','')
            body=body.replace('    descriptor.value14 =',
                '    descriptor.value4 = -25;\n    descriptor.value6 = 10;\n    descriptor.value14 =')
        if constants_first:
            lines = body.splitlines()
            fields = ('    descriptor.value1C = D_800A5470;', '    descriptor.value20 = D_800A5474;')
            lines = [line for line in lines if line not in fields]
            lines[2:2] = fields
            body = '\n'.join(lines)
        yield 'shape-%d%d%d%d' % (aggregate, integer_two, late_header, constants_first), body


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n#include "variables.h"\n'+LOCAL_DECLARATIONS+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout+result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output/'descriptor.ld'
    script.write_text('SECTIONS { .text 0x15142180 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocs = parse_object(obj)
    function = functions[FUNCTION]
    words = list(struct.unpack_from('>%dI'%(function['size']//4), sections(elf)['.text'][1], function['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    retail = struct.unpack_from('>80I', (root/'conker/conker.us.bin').read_bytes(), ROM)
    record = dict(name=name, profile=profile, body_words=end, object_words=function['size']//4,
        frame=frames[0] if frames else 0, diagnostics=diagnostics,
        differences=sum(a!=b for a,b in itertools.zip_longest(words,retail,fillvalue=0)), relocations=relocs)
    return record, words


def main():
    root=Path(__file__).resolve().parents[2]
    output=root/'conker/build/game-scaled-descriptor'
    output.mkdir(exist_ok=True)
    records=[]
    for name,body in candidates():
        for profile in PROFILES:
            record,_=compile_candidate(root,output,name+'-'+profile,body,profile)
            records.append(record)
            print(record['name'],record['body_words'],record['frame'],record['differences'],flush=True)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__=='__main__':
    main()
