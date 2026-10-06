"""Recover the source-backed extended actor descriptor under the retail profile."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS, CONSTRUCTOR, COPY = 0x1519EB8C, 0x1CC03C, 102, 0x1513264C, 0x10022EC0
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
LAYOUTS = '''typedef struct { f32 x, y, z; } Position1CBE20;
typedef struct {
    Position1CBE20 position;
    Position1CBE20 vector;
    f32 width;
    f32 height;
} Source1CBE20;
typedef struct {
    f32 field00;
    f32 field04;
    f32 field08;
    f32 field0C;
    Position1CBE20 vector;
    f32 field1C;
    f32 field20;
    f32 field24;
    Position1CBE20 position;
    Position1CBE20 first;
    Position1CBE20 second;
    f32 field4C;
    u32 flags;
    s16 lifetime;
    u16 resource;
    u8 field58;
    u8 pad59[3];
    u32 field5C;
    u8 field60;
    u8 field61;
    u8 field62;
    u8 field63;
    u8 field64;
    u8 field65;
    u8 field66;
    u8 field67;
    u8 field68;
    u8 pad69;
    u8 field6A;
    u8 pad6B;
    u32 field6C;
    u8 field70;
    u8 pad71;
    s16 field72;
    s16 field74;
    u8 pad76[2];
    u32 field78;
} ActorDescriptor1CBE20;'''
DECLARATIONS = '''extern Position1CBE20 D_800A5480;
extern f32 D_800A8CD4;
struct ExtendedState15F680;
void *func_1513264C(u8 *, s32, s32, struct ExtendedState15F680 *, s32, u8, s32);
void *memcpy(void *, const void *, u32);
'''
SELECTED = '''void func_1519EB8C(Source1CBE20 *source, u16 resource, s16 lifetime, u8 channel, s32 context) {
    ActorDescriptor1CBE20 packet;
    Source1CBE20 *savedSource;
    u8 *actor;

    savedSource = source;
    packet.field00 = 1.0f;
    packet.field04 = 1.0f;
    packet.field08 = source->width * D_800A8CD4;
    packet.field0C = source->height * D_800A8CD4;
    packet.vector.x = source->vector.x;
    packet.vector.y = source->vector.y;
    packet.vector.z = source->vector.z;
    packet.field1C = 1.0f;
    packet.field20 = 1.0f;
    packet.field24 = 1.0f;
    packet.position.x = source->position.x;
    packet.position.y = source->position.y;
    packet.position.z = source->position.z;
    packet.first = D_800A5480;
    packet.second = D_800A5480;
    packet.field4C = 0.0f;
    packet.flags = 0x980;
    packet.lifetime = lifetime;
    packet.resource = resource;
    packet.field58 = 0;
    packet.field5C = 0;
    packet.field60 = 255;
    packet.field61 = 21;
    packet.field62 = 0;
    packet.field63 = 0;
    packet.field64 = 0;
    packet.field65 = 0;
    packet.field66 = 0;
    packet.field67 = 0;
    packet.field68 = 2;
    packet.field6A = 0;
    packet.field6C = 0;
    packet.field70 = 0;
    packet.field72 = 1;
    packet.field74 = 255;
    packet.field78 = 0;
    actor = func_1513264C((u8 *)&packet, 3, 255, NULL, 4, channel, context);
    if (actor != NULL) {
        memcpy(actor + 0x170, &savedSource, sizeof(savedSource));
    }
}'''


def candidates():
    pair = SELECTED.replace('    u8 *actor;', '    u8 *actor;\n    f32 unit = 1.0f;\n    f32 factor = D_800A8CD4;').replace(
        '= 1.0f;', '= unit;').replace('f32 unit = unit;', 'f32 unit = 1.0f;').replace('* D_800A8CD4;', '* factor;')
    pointers = SELECTED.replace('    u8 *actor;', '    u8 *actor;\n    f32 factor = D_800A8CD4;\n'
        '    Position1CBE20 *defaults = &D_800A5480;').replace('* D_800A8CD4;', '* factor;').replace(
        ' = D_800A5480;', ' = *defaults;')
    return [('field-order', SELECTED),
            ('size-after-scalars', SELECTED.replace('    packet.field4C = 0.0f;\n','').replace(
                '    packet.field78 = 0;', '    packet.field78 = 0;\n    packet.field4C = 0.0f;')),
            ('vector-copy', SELECTED.replace('    packet.vector.x = source->vector.x;\n'
                '    packet.vector.y = source->vector.y;\n    packet.vector.z = source->vector.z;',
                '    packet.vector = source->vector;')),
            ('position-copy', SELECTED.replace('    packet.position.x = source->position.x;\n'
                '    packet.position.y = source->position.y;\n    packet.position.z = source->position.z;',
                '    packet.position = source->position;')),
            ('wide-lifetime', SELECTED.replace('s16 lifetime,','s32 lifetime,')),
            ('wide-resource', SELECTED.replace('u16 resource,','s32 resource,')),
            ('captured-factor', SELECTED.replace('    u8 *actor;', '    u8 *actor;\n    f32 factor = D_800A8CD4;').replace(
                '* D_800A8CD4;', '* factor;')),
            ('factor-assignment', SELECTED.replace('    u8 *actor;', '    u8 *actor;\n    f32 factor;').replace(
                '    savedSource = source;', '    factor = D_800A8CD4;\n    savedSource = source;').replace(
                '* D_800A8CD4;', '* factor;')),
            ('captured-unit-factor', pair),
            ('register-unit-factor', pair.replace('    f32 unit =','    register f32 unit =').replace(
                '    f32 factor =','    register f32 factor =')),
            ('factor-and-default-address', pointers),
            ('unit-from-first-field', SELECTED.replace('packet.field04 = 1.0f;', 'packet.field04 = packet.field00;')),
            ('chained-unit-fields', SELECTED.replace('    packet.field00 = 1.0f;\n    packet.field04 = 1.0f;',
                '    packet.field04 = packet.field00 = 1.0f;')),
            ('dimensions-first', SELECTED.replace('    packet.field00 = 1.0f;\n    packet.field04 = 1.0f;\n','').replace(
                '    packet.vector.x =', '    packet.field00 = 1.0f;\n    packet.field04 = 1.0f;\n    packet.vector.x ='))]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output/(name+suffix) for suffix in ('.c','.o','.elf'))
    source.write_text('#include <ultra64.h>\n'+LAYOUTS+'\n'+DECLARATIONS+body+'\n')
    compiled = subprocess.run(['ido/ido5.3_recomp/cc','-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
        '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32',
        '-I','conker/include','-I','conker/include/2.0L','-I','conker/include/2.0L/PR',
        '-D_LANGUAGE_C','-D_FINALROM','-DF3DEX_GBI_2','-D_MIPS_SZLONG=32',*PROFILES[profile],
        '-o',str(obj.relative_to(root)),str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
    diagnostics = compiled.stdout+compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output/'source-packet.ld'
    script.write_text('SECTIONS { .text 0x1519EB8C : SUBALIGN(4) { *(.text) } }\n')
    symbols = {'func_1513264C': CONSTRUCTOR,'memcpy':COPY,'D_800A5480':0x800A5480,'D_800A8CD4':0x800A8CD4}
    subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e','func_1519EB8C',
        *['--defsym=%s=0x%X'%item for item in symbols.items()],'-o',str(elf),str(obj)],
        check=True,capture_output=True,text=True)
    words = load_elf_functions(str(elf),'mips-linux-gnu-objdump')[0]['func_1519EB8C']
    end = max(i for i,word in enumerate(words) if word==0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>102I',(root/'conker/conker.us.bin').read_bytes(),ROM))
    slot = words+[0]*max(0,WORDS-end)
    differences = [(i*4,hex(a),hex(b)) for i,(a,b) in enumerate(zip(slot,retail)) if a!=b]
    return dict(name=name,profile=profile,body_words=end,frame=(-words[0])&65535,
        differences=len(differences)+max(0,end-WORDS),different_words=differences,
        exact=slot==retail,diagnostics=diagnostics),words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-actor-source-packet'
    output.mkdir(exist_ok=True)
    records = []
    for name,body in candidates():
        for profile in PROFILES:
            record,_ = compile_candidate(root,output,name+'-'+profile,body,profile)
            records.append(record)
            print(record['name'],record['body_words'],hex(record['frame']),record['differences'],flush=True)
    (output/'measurements.json').write_text(json.dumps(records,indent=2)+'\n')


if __name__=='__main__':
    main()
