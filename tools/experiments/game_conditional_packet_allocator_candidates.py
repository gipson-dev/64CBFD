"""Screen the conditional object/byte packet allocator without normalizing words."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x1519E6BC, 0x1CBB6C, 38
CLEANUP, ALLOCATOR, COPY, SLOT = 0x1519E688, 0x151491F4, 0x10022EC0, 0x800E0920
SYMBOLS = dict(func_1519E688=CLEANUP, func_151491F4=ALLOCATOR, memcpy=COPY, D_800E0920=SLOT)
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
PACKET = '''typedef struct {
    u8 *object;
    u8 code;
    s32 reserved;
} Packet1CA420;'''
DECLARATIONS = '''extern u8 *D_800E0920;
void func_1519E688(void);
struct260 *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);
'''
SELECTED = '''void func_1519E6BC(u8 *arg0) {
    Packet1CA420 packet;

    func_1519E688();
    if (D_800E0920 == NULL) {
        packet.reserved = 0;
        packet.object = arg0;
        packet.code = arg0[0x3B];
        D_800E0920 = (u8 *)func_151491F4(0x12C, -1, 9, 0, 4, 12, 0xFF, 0);
        if (D_800E0920 != NULL) {
            memcpy(D_800E0920 + 0x28, &packet, sizeof(packet));
        }
    }
}'''


def candidates():
    return [('reserved-first', SELECTED),
            ('field-order', SELECTED.replace('        packet.reserved = 0;\n', '').replace(
                '        packet.code = arg0[0x3B];', '        packet.code = arg0[0x3B];\n        packet.reserved = 0;')),
            ('allocation-local', SELECTED.replace('    Packet1CA420 packet;', '    Packet1CA420 packet;\n    u8 *result;').replace(
                '        D_800E0920 = (u8 *)', '        result = (u8 *)').replace(
                '        if (D_800E0920 != NULL)', '        D_800E0920 = result;\n        if (result != NULL)').replace(
                'memcpy(D_800E0920 +', 'memcpy(result +')),
            ('unused-local', SELECTED.replace('    Packet1CA420 packet;', '    Packet1CA420 packet;\n    u8 *result;')),
            ('early-return', SELECTED.replace('    if (D_800E0920 == NULL) {', '    if (D_800E0920 != NULL) {\n        return;\n    }\n    {')),
            ('explicit-copy-size', SELECTED.replace('sizeof(packet)', '12'))]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3', packet=PACKET):
    source, obj, elf = (output / (name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "structs.h"\n'+packet+'\n'+DECLARATIONS+body+'\n')
    compiled = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = compiled.stdout+compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'packet.ld'
    script.write_text('SECTIONS { .text 0x1519E6BC : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1519E6BC',
                    *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
                   check=True, capture_output=True, text=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1519E6BC']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>38I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=max(frames, default=0),
                differences=len(differences)+max(0, end-WORDS), different_words=differences,
                exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-conditional-packet-allocator'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name+'-'+profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
