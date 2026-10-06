"""Screen actor identity switches against the retail code and fixed table pool."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.pad_generated_object import ELF_HEADER, SECTION_HEADER, parse_object, read_c_string

ENTRY, ROM, WORDS = 0x15141C0C, 0x16F0BC, 45
FUNCTION = 'func_15141C0C'
TABLE = 0x800A5218
ANCHOR = 'jtbl_800A5218_game'
PROTOTYPE = 's32 func_15141C0C(u8 *actor);'
PROFILES = {'o2g3': ('-O2', '-g3'), 'o2': ('-O2',), 'o1g3': ('-O1', '-g3'), 'o1': ('-O1',)}
GROUPS = {10: (121,), 9: (33,), 8: (123,), 0: (0, 1, 2, 3, 4, 150),
    1: (16, 145), 2: (43,), 5: (84,), 6: (54, 83, 165), 7: (88,), 3: (69,), 4: (75,)}
SELECTED = '''s32 func_15141C0C(u8 *actor) {
    s32 identity = actor[4];
    switch (identity) {
        case 0x79:
            return 10;
        case 0x21:
            return 9;
        case 0x7B:
            return 8;
        case 0x0:
        case 0x1:
        case 0x2:
        case 0x3:
        case 0x4:
        case 0x96:
            return 0;
        case 0x10:
        case 0x91:
            return 1;
        case 0x2B:
            return 2;
        case 0x54:
            return 5;
        case 0x36:
        case 0x53:
        case 0xA5:
            return 6;
        case 0x58:
            return 7;
        case 0x45:
            return 3;
        case 0x4B:
            return 4;
    }
    return 11;
}'''


def sections(path):
    data = path.read_bytes(); header = ELF_HEADER.unpack_from(data)
    headers = [SECTION_HEADER.unpack_from(data, header[6] + i * header[11]) for i in range(header[12])]
    names = headers[header[13]]; strings = data[names[4]:names[4] + names[5]]
    return {read_c_string(strings, item[0]): (item[3], data[item[4]:item[4] + item[5]])
            for item in headers if item[1] != 8}


def candidates():
    for kind, default in itertools.product(('inline', 's32', 'u32', 'u8'), (False, True)):
        body = SELECTED
        if kind == 'inline':
            body = body.replace('    s32 identity = actor[4];\n', '').replace('switch (identity)', 'switch (actor[4])')
        else:
            body = body.replace('s32 identity =', kind + ' identity =')
        if default:
            body = body.replace('    }\n    return 11;', '        default:\n            return 11;\n    }')
        yield '%s-%d' % (kind, default), body


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n#include "variables.h"\n' + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics: raise ValueError(diagnostics)
    script = output / 'classifier.ld'
    script.write_text('SECTIONS { .text 0x15141C0C : SUBALIGN(4) { *(.text) } '
        '.rodata 0x800A5218 : SUBALIGN(4) { *(.rodata) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, symbols, relocations = parse_object(obj)
    pools = sections(elf); text = pools['.text'][1]
    start, size = symbols[FUNCTION]['value'], symbols[FUNCTION]['size']
    words = list(struct.unpack_from('>%dI' % (size // 4), text, start))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:]); words = words[:end]
    table_bytes = pools.get('.rodata', (TABLE, b''))[1]
    retail = list(struct.unpack_from('>45I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    record = dict(name=name, profile=profile, body_words=end, object_words=size // 4,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics=diagnostics, frame=frames[0] if frames else 0, rodata_bytes=len(table_bytes), relocations=relocations)
    return record, words, table_bytes


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-actor-classifier'; output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__': main()
