"""Screen the actor-event callback and payload tail without installing edits."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x151416E8, 0x16EB98, 55
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SYMBOLS = {'D_8008A02C': 0x8008A02C, 'func_1516972C': 0x1516972C}
DECLARATIONS = '''#include "functions.h"
#include "variables.h"
typedef void (*ActorEventCallback16DC80)(u8 *, u8 *, u8);
extern ActorEventCallback16DC80 D_8008A02C[];
'''
SELECTED = '''void func_151416E8(u8 *actor, u8 *event, u8 command) {
    u8 *payload;
    if (D_8008A02C[*(volatile u8 *)(actor + 0x168)] != NULL) {
        D_8008A02C[*(volatile u8 *)(actor + 0x168)](actor, event, command);
    }
    if (command == 0x22 || command == 0x24 || command == 0x25) {
        /* Retain the retail payload base using unsigned N64 address arithmetic. */
        payload = (u8 *)((u32)actor - (u32)-0x110);
        if (event[0] == payload[0x58]) {
            switch (command) {
                case 0x22: func_1516972C((struct102 *)actor); break;
                case 0x24: *(s8 *)(payload + 0x59) = -1; break;
                case 0x25: *(s8 *)(payload + 0x59) = 2; break;
            }
        }
    }
}'''


def candidates():
    selected = SELECTED
    return [
        ('selected', selected),
        ('pointer-addition', selected.replace('(u8 *)((u32)actor - (u32)-0x110)', 'actor + 0x110')),
        ('signed-pointer-subtraction', selected.replace('(u8 *)((u32)actor - (u32)-0x110)', 'actor - (s32)-0x110')),
        ('unsigned-hex-subtraction', selected.replace('(u32)-0x110', '0xFFFFFEF0U')),
        ('ordinary-selector', selected.replace('*(volatile u8 *)(actor + 0x168)', 'actor[0x168]')),
        ('unsigned-status', selected.replace('*(s8 *)(payload + 0x59)', 'payload[0x59]')),
        ('reverse-comparison', selected.replace('event[0] == payload[0x58]', 'payload[0x58] == event[0]')),
        ('if-chain', selected.replace('''            switch (command) {
                case 0x22: func_1516972C((struct102 *)actor); break;
                case 0x24: *(s8 *)(payload + 0x59) = -1; break;
                case 0x25: *(s8 *)(payload + 0x59) = 2; break;
            }''', '''            if (command == 0x22) {
                func_1516972C((struct102 *)actor);
            } else if (command == 0x24) {
                *(s8 *)(payload + 0x59) = -1;
            } else if (command == 0x25) {
                *(s8 *)(payload + 0x59) = 2;
            }''')),
    ]


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
    script = output/'event.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n'%ENTRY)
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_151416E8',
                    *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
                   check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_151416E8']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>%dI'%WORDS, (root/'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word)&65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
                differences=len(differences)+max(0, end-WORDS), different_words=differences,
                exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-actor-event-dispatch'
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
