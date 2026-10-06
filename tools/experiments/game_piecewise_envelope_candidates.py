"""Screen scoped envelope factors without installing source or word guards."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.match_progress import load_elf_functions

ENTRY, ROM, WORDS = 0x151415D4, 0x16EA84, 69
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
SYMBOLS = {'D_800BE9A4': 0x800BE9A4}
DECLARATIONS = 'extern f32 D_800BE9A4;\n'
SELECTED = '''s32 func_151415D4(u8 *actor) {
    u8 *runtime;
    f32 period;
    runtime = actor + 0x170;
    if (*(f32 *)(actor + 0x17C) < *(f32 *)(actor + 0x180)) {
        *(f32 *)(actor + 0x158) = *(f32 *)(runtime + 4);
    } else if (*(f32 *)(runtime + 0xC) < *(f32 *)(runtime + 0x14)) {
        f32 factor;
        factor = (*(f32 *)(runtime + 0xC) - *(f32 *)(runtime + 0x10)) * *(f32 *)(runtime + 0x20);
        *(f32 *)(actor + 0x158) = *(f32 *)(runtime + 8) * factor + *(f32 *)(runtime + 4);
    } else if (*(f32 *)(runtime + 0xC) < *(f32 *)(runtime + 0x18)) {
        *(f32 *)(actor + 0x158) = *(f32 *)(runtime + 0);
    } else {
        f32 factor;
        factor = 1.0f - (*(f32 *)(runtime + 0xC) - *(f32 *)(runtime + 0x18)) * *(f32 *)(runtime + 0x20);
        *(f32 *)(actor + 0x158) = *(f32 *)(runtime + 4) + *(f32 *)(runtime + 8) * factor;
    }
    period = *(f32 *)(runtime + 0x1C);
    *(f32 *)(runtime + 0xC) += D_800BE9A4;
    while (period < *(f32 *)(runtime + 0xC)) {
        *(f32 *)(runtime + 0xC) -= period;
    }
    return 1;
}'''


def candidates():
    records = []
    for scoped, rise_first, fall_first in itertools.product((False, True), repeat=3):
        body = SELECTED
        if not scoped:
            body = body.replace('        f32 factor;\n', '').replace('    f32 period;', '    f32 period;\n    f32 factor;')
        if not rise_first:
            body = body.replace('*(f32 *)(runtime + 8) * factor + *(f32 *)(runtime + 4)',
                                '*(f32 *)(runtime + 4) + *(f32 *)(runtime + 8) * factor')
        if fall_first:
            prefix, suffix = body.split('    } else {')
            suffix = suffix.replace('*(f32 *)(runtime + 4) + *(f32 *)(runtime + 8) * factor',
                                    '*(f32 *)(runtime + 8) * factor + *(f32 *)(runtime + 4)')
            body = prefix+'    } else {'+suffix
        records.append(('shape-%d%d%d'%(scoped, rise_first, fall_first), body))
    return records


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
    script = output/'envelope.ld'
    script.write_text('SECTIONS { .text 0x151415D4 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_151415D4',
                    *['--defsym=%s=0x%X'%item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
                   check=True, capture_output=True)
    words = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0]['func_151415D4']
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = list(struct.unpack_from('>69I', (root/'conker/conker.us.bin').read_bytes(), ROM))
    slot = words+[0]*max(0, WORDS-end)
    differences = [(i*4, hex(a), hex(b)) for i, (a, b) in enumerate(zip(slot, retail)) if a != b]
    frames = [(-word)&65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
                differences=len(differences)+max(0, end-WORDS), different_words=differences,
                exact=slot == retail, diagnostics=diagnostics), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root/'conker/build/game-piecewise-envelope'
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
