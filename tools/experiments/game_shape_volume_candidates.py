"""Recover the 56-word descriptor measure without changing retail data or profiles."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x1514462C, 0x171ADC, 56
SYMBOLS = {'D_800A5698': 0x800A5698, 'D_800A569C': 0x800A569C}
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SELECTED = '''f32 func_1514462C(struct134 *arg0) {
    f32 ret;
    u8 *record = (u8 *)arg0;

    switch (record[0x15] & 3) {
        case 2:
            /* Wrap the integer product before converting it to float. */
            ret = (s32)((u32)*(s16 *)(record + 8) * (u32)*(s16 *)(record + 0xA) * (u32)*(s16 *)(record + 6));
            break;
        case 0:
            ret = *(s16 *)(record + 8) * (*(s16 *)(record + 6) * *(s16 *)(record + 6) * D_800A5698);
            break;
        case 1: {
            f32 radius = *(s16 *)(record + 6);
            ret = radius * D_800A569C * radius * radius;
            break;
        }
        default:
            ret = 1.0f;
            break;
    }

    return ret;
}'''


def candidates():
    original = '(u32)*(s16 *)(record + 8) * (u32)*(s16 *)(record + 0xA) * (u32)*(s16 *)(record + 6)'
    cylinder = '*(s16 *)(record + 8) * (*(s16 *)(record + 6) * *(s16 *)(record + 6) * D_800A5698)'
    forms = []
    for order in itertools.permutations(('6', '8', '0xA')):
        box = ' * '.join('(u32)*(s16 *)(record + %s)' % offset for offset in order)
        for reverse in (False, True):
            body = SELECTED.replace(original, box)
            if reverse:
                body = body.replace(cylinder, '(*(s16 *)(record + 6) * *(s16 *)(record + 6) * D_800A5698) * *(s16 *)(record + 8)')
            forms.append(('box-' + '-'.join(order) + '-cylinder-' + ('right' if reverse else 'left'), body))
    return forms


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "structs.h"\n'
                      'extern f32 D_800A5698, D_800A569C;\n' + body + '\n')
    command = ['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
               '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
               '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32',
               *PROFILES[profile], '-o', str(obj.relative_to(root)), str(source.relative_to(root))]
    compiled = subprocess.run(command, cwd=root, capture_output=True, text=True)
    diagnostics = compiled.stdout + compiled.stderr
    if compiled.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'volume.ld'
    script.write_text('SECTIONS { .text 0x1514462C : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1514462C',
                    *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
                   check=True, capture_output=True, text=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1514462C']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    if any(words[end:]):
        raise ValueError('nonzero tail after return')
    words = words[:end]
    retail = list(struct.unpack_from('>56I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    slot = words + [0] * max(0, WORDS - end)
    different = [(i * 4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-(w & 65535)) & 65535 for w in words if w & 0xFFFF0000 == 0x27BD0000 and w & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=max(frames, default=0),
                differences=len(different) + max(0, end - WORDS), different_words=different,
                exact=words == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-shape-volume'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
            records.append(record)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
