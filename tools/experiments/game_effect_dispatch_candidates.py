"""Screen live effect dispatch with the actual SDK declarations; never install edits."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.pad_generated_object import ELF_HEADER, SECTION_HEADER, parse_object, read_c_string

ENTRY, ROM, WORDS = 0x15141A7C, 0x16EF2C, 100
FUNCTION = 'func_15141A7C'
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SYMBOLS = dict(func_15141C0C=0x15141C0C, func_1510F8CC=0x1510F8CC,
    func_15141CC0=0x15141CC0, func_15141E38=0x15141E38, func_1514ECE0=0x1514ECE0,
    D_800BE616=0x800BE616, D_8008A084=0x8008A084, D_8008A0B4=0x8008A0B4)
# Keep the typed helper declarations synchronized with the production owner.
LOCAL_DECLARATIONS = '''typedef s32 (*GameEffectClassifier)(s32, u8 *);
typedef void (*GameEffectCallback)(u8 *, s32, s32);
typedef struct { GameEffectCallback callback; s32 count; } GameEffectEntry;
s32 func_15141C0C(u8 *actor);
s32 func_1510F8CC(s32);
s32 func_15141CC0(s32 context);
void func_15141E38(u8 *actor, s32 index);
s32 func_1514ECE0(u8 *, s16, u8 **);
'''
DECLARATIONS = '#include "functions.h"\n#include "variables.h"\n' + LOCAL_DECLARATIONS
PROTOTYPE = 'void func_15141A7C(u8 *actor, s32 context);'
SELECTED = '''void func_15141A7C(u8 *actor, s32 context) {
    s32 category;
    s32 selected;
    u8 *node;
    u8 *record;
    if (D_800BE616 == 0) {
        category = func_15141C0C(actor);
        if (((GameEffectClassifier *)D_8008A084)[category] != NULL) {
            {
                s32 classified = func_15141CC0(func_1510F8CC(*(s32 *)(actor + 0x184)));
                selected = ((GameEffectClassifier *)D_8008A084)[category](classified, actor);
            }
            if ((selected != -1) && (((GameEffectEntry *)D_8008A0B4)[selected].callback != NULL)) {
                if (((GameEffectEntry *)D_8008A0B4)[selected].count > 0) {
                    func_15141E38(actor, selected);
                } else {
                    ((GameEffectEntry *)D_8008A0B4)[selected].callback(actor, context, 0);
                }
            }
        }
        node = *(u8 **)(actor + 0x2F4);
        while (func_1514ECE0(node, 0x1A, &node)) {
            record = *(u8 **)(node + 0x10);
            if (((GameEffectEntry *)D_8008A0B4)[*(volatile s32 *)(record + 0x28)].callback != NULL) {
                ((GameEffectEntry *)D_8008A0B4)[*(volatile s32 *)(record + 0x28)].callback(actor, context, *(s16 *)(record + 0xE));
            }
            *(u8 *volatile *)&node = *(u8 **)(node + 0x14);
        }
    }
}'''


def candidates():
    forms = []
    for selector_live, cursor_live, do_loop in itertools.product((False, True), repeat=3):
        body = SELECTED
        if not selector_live:
            body = body.replace('*(volatile s32 *)(record + 0x28)', '*(s32 *)(record + 0x28)')
        if not cursor_live:
            body = body.replace('*(u8 *volatile *)&node =', 'node =')
        if do_loop:
            body = body.replace('        while (func_1514ECE0(node, 0x1A, &node)) {',
                '        if (func_1514ECE0(node, 0x1A, &node)) { do {').replace(
                '            *(u8 *volatile *)&node = *(u8 **)(node + 0x14);\n        }',
                '            *(u8 *volatile *)&node = *(u8 **)(node + 0x14);\n        } while (func_1514ECE0(node, 0x1A, &node)); }').replace(
                '            node = *(u8 **)(node + 0x14);\n        }',
                '            node = *(u8 **)(node + 0x14);\n        } while (func_1514ECE0(node, 0x1A, &node)); }')
        forms.append(('shape-%d%d%d' % (selector_live, cursor_live, do_loop), body))
    return forms


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n' + DECLARATIONS + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'effect-dispatch.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % ENTRY)
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    # Absolute helper symbols can split objdump output inside an overlong control.
    _, symbols, _ = parse_object(obj)
    data = elf.read_bytes(); header = ELF_HEADER.unpack_from(data)
    sections = [SECTION_HEADER.unpack_from(data, header[6] + i * header[11]) for i in range(header[12])]
    names = sections[header[13]]; strings = data[names[4]:names[4] + names[5]]
    text = next(section for section in sections if read_c_string(strings, section[0]) == '.text')
    start, length = symbols[FUNCTION]['value'], symbols[FUNCTION]['size']
    words = list(struct.unpack_from('>%dI' % (length // 4), data, text[4] + start))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    slot = words[:end] + [0] * max(0, WORDS - end)
    retail = list(struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM))
    differences = [(i * 4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word) & 65535 for word in slot if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, slot_words=len(slot), frame=frames[0] if frames else 0,
        differences=len(differences) + max(0, end - WORDS), different_words=differences,
        exact=slot == retail, diagnostics=diagnostics), slot


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-effect-dispatch'; output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
