"""Recover the cached environment-color leaf using the actual SDK command macros."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15142C10, 0x1700C0, 56
FUNCTION = 'func_15142C10'
SYMBOLS = dict(D_800DD1C8=0x800DD1C8, D_800DD1CA=0x800DD1CA,
    D_800DD1CC=0x800DD1CC, D_800DD1CE=0x800DD1CE)
DECLARATIONS = '\n'.join('extern s16 %s;' % name for name in SYMBOLS) + '\n'
PROTOTYPE = 'Gfx *func_15142C10(Gfx *output, s32 red, s32 green, s32 blue, s32 alpha, u8 *sync);'
SELECTED = '''Gfx *func_15142C10(Gfx *output, s32 red, s32 green, s32 blue, s32 alpha, u8 *sync) {
    if (red != D_800DD1C8 || green != D_800DD1CA || blue != D_800DD1CC || alpha != D_800DD1CE) {
        if (*sync == 1) {
            gDPPipeSync(output++);
            *sync = 0;
        }
        gDPSetEnvColor(output++, red, green, blue, alpha);
        D_800DD1C8 = red;
        D_800DD1CA = green;
        D_800DD1CC = blue;
        D_800DD1CE = alpha;
    }
    return output;
}'''


def candidates():
    for positive, cursor, command in itertools.product((False, True), (False, True), ('sdk', 'packet', 'direct')):
        body = SELECTED
        if not positive:
            body = body.replace('    if (red != D_800DD1C8 || green != D_800DD1CA || blue != D_800DD1CC || alpha != D_800DD1CE) {',
                '    if (red == D_800DD1C8 && green == D_800DD1CA && blue == D_800DD1CC && alpha == D_800DD1CE) {\n'
                '        return output;\n    }\n    {')
        if cursor:
            body = body.replace('    if (red', '    Gfx *cursor = output;\n    if (red', 1)
            body = body.replace('output++', 'cursor++').replace('return output;', 'return cursor;')
        pointer = 'cursor' if cursor else 'output'
        if command != 'sdk':
            target = pointer if command == 'direct' else 'packet'
            emitted = ('        {\n            Gfx *packet = %s++;\n' % pointer if command == 'packet' else '')
            emitted += '        %s->words.w0 = 0xFB000000;\n' % target
            emitted += '        %s->words.w1 = ((u32)red << 24) | ((u32)(green & 255) << 16) | ((u32)(blue & 255) << 8) | (alpha & 255);\n' % target
            emitted += '        }' if command == 'packet' else '        %s++;' % pointer
            body = body.replace('        gDPSetEnvColor(%s++, red, green, blue, alpha);' % pointer, emitted)
        yield 'positive%d-cursor%d-%s' % (positive, cursor, command), body


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3', declarations=DECLARATIONS):
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n' + declarations + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, text=True, capture_output=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'color.ld'
    script.write_text('SECTIONS { .text 0x15142C10 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, functions, rel = parse_object(obj)
    meta = functions[FUNCTION]
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), sections(elf)['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>56I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, body_words=end, profile=profile, frame=frames[0] if frames else 0,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics=diagnostics, relocations=rel), words


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-cached-environment-color'
    out.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, out, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
