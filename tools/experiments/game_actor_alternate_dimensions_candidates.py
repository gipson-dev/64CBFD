"""Recover the signed alternate actor query, including its two retail padding words."""

import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions
from tools.experiments.game_actor_dimensions_candidates import PROFILES

ENTRY, ROM, WORDS = 0x1515C244, 0x1896F4, 43
SELECTED = '''void func_1515C244(struct127 *arg0, struct17 *arg1, f32 *arg2, f32 *arg3) {
    if (arg0->id < 0xBB && arg0->id != 0xFF) {
        *arg2 = arg0->unkE4;
        *arg3 = arg0->unkE6;
        arg1->unk0 = arg0->x_position;
        arg1->unk4 = arg0->y_position + (s16)arg0->unkE8;
        arg1->unk8 = arg0->z_position;
    } else {
        *arg2 = 1.0f;
        *arg3 = 1.0f;
        arg1->unk0 = arg0->x_position;
        arg1->unk4 = arg0->y_position;
        arg1->unk8 = arg0->z_position;
    }
}'''


def candidates():
    return [('fields', SELECTED),
            ('cached-id', SELECTED.replace('    if (', '    s32 id = arg0->id;\n    if (', 1)
             .replace('arg0->id <', 'id <').replace('arg0->id !=', 'id !=')),
            ('reverse-add', SELECTED.replace('arg0->y_position + (s16)arg0->unkE8',
                                             '(s16)arg0->unkE8 + arg0->y_position')),
            ('early-return', SELECTED.replace('    } else {', '        return;\n    }\n    {'))]


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "structs.h"\n' + body + '\n')
    command = ['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
               '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
               '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
               '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32',
               *PROFILES[profile], '-o', str(obj.relative_to(root)), str(source.relative_to(root))]
    result = subprocess.run(command, cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'dimensions.ld'
    script.write_text('SECTIONS { .text 0x1515C244 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1515C244',
                    '-o', str(elf), str(obj)], check=True, capture_output=True, text=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_1515C244']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    if any(words[end:]):
        raise ValueError('nonzero return tail')
    words = words[:end]
    retail = list(struct.unpack_from('>43I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    slot = words + [0] * max(0, WORDS - end)
    different = [(i * 4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-(w & 65535)) & 65535 for w in words if w & 0xFFFF0000 == 0x27BD0000 and w & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=max(frames, default=0),
                padding_words=max(0, WORDS-end), differences=len(different)+max(0, end-WORDS),
                different_words=different, exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-alternate-dimensions'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name+'-'+profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], record['padding_words'], record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
