"""Screen world/context classification against the original N64 slot and pool."""

import itertools
import json
import re
import struct
import subprocess
import sys
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15141CC0, 0x16F170, 57
FUNCTION = 'func_15141CC0'
TABLE, WORLD = 0x800A5430, 0x800BE9F0
ANCHOR, POOL_OFFSET = 'jtbl_800A5218_game', 0x218
PROTOTYPE = 's32 func_15141CC0(s32 context);'
SELECTED = '''s32 func_15141CC0(s32 context) {
    s32 world = D_800BE9F0;
    if (world == 47) {
        return 6;
    }
    if (world == 66) {
        return 7;
    }
    if (world == 39) {
        return 8;
    }
    if (world == 25) {
        return 5;
    }
    switch (context) {
        case 10:
            return 0;
        case 7:
            return 2;
        case 11:
            return 1;
        case 15:
            return 3;
        case 2:
        case 8:
        case 12:
            if (world == 2) {
                return 7;
            }
            return 4;
        case 5:
            if (world == 20) {
                return 5;
            }
            return 9;
        case 0:
            return 9;
    }
    return 9;
}'''


def candidates():
    for local, default in itertools.product((False, True), (False, True)):
        body = SELECTED
        if not local:
            body = body.replace('    s32 world = D_800BE9F0;\n', '').replace('world ==', 'D_800BE9F0 ==')
        if default:
            body = body.replace('    }\n    return 9;', '        default:\n            return 9;\n    }')
        yield 'local%d-default%d' % (local, default), body


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n#include "variables.h"\n' + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'classifier.ld'
    script.write_text('SECTIONS { .text 0x15141CC0 : SUBALIGN(4) { *(.text) } '
        '.rodata 0x800A5430 : SUBALIGN(4) { *(.rodata) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        '--defsym=D_800BE9F0=0x800BE9F0', '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, symbols, relocations = parse_object(obj)
    pools = sections(elf); text = pools['.text'][1]
    start, size = symbols[FUNCTION]['value'], symbols[FUNCTION]['size']
    words = list(struct.unpack_from('>%dI' % (size // 4), text, start))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:]); words = words[:end]
    retail = struct.unpack_from('>57I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    record = dict(name=name, profile=profile, body_words=end, object_words=size // 4,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics=diagnostics, frame=frames[0] if frames else 0, relocations=relocations)
    return record, words, pools.get('.rodata', (TABLE, b''))[1]


def compile_owner(root, output, source, name):
    """Use the production preprocessing/profile and retain warning locations by statement."""
    raw, processed, obj = (output / (name + suffix) for suffix in ('.c', '-processed.c', '.o'))
    raw.write_text(source)
    result = subprocess.run([sys.executable, str(root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
        str(raw.relative_to(root / 'conker'))], cwd=root / 'conker', capture_output=True, text=True, check=True)
    assert not result.stderr; processed.write_text(result.stdout)
    includes = ['.', 'include', 'include/2.0L', 'include/2.0L/PR', 'include/libc',
                'src/libultra/os', 'src/libultra/audio', 'src/libultra/io']
    result = subprocess.run([str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2',
        '-D_MIPS_SZLONG=32', '-woff', '649,838', *[f for p in includes for f in ('-I', p)], '-O2', '-g3',
        '-mips2', '-o32', '-o', str(obj.relative_to(root / 'conker')), str(processed.relative_to(root / 'conker'))],
        cwd=root / 'conker', capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    assert not result.returncode, diagnostics
    (output / (name + '-diagnostics.txt')).write_text(diagnostics)
    warnings = re.findall(r'cfe: Warning (\d+): [^\n]+\n([^\n]+)\n([^\n]+)\n', diagnostics)
    assert len(warnings) == diagnostics.count('cfe: Warning')
    return obj, warnings


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-context-classifier'; output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__': main()
