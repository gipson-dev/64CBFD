"""Screen cached texture submission while preserving the retail self-write."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15142E24, 0x1702D4, 102
FUNCTION = 'func_15142E24'
SYMBOLS = dict(func_1514306C=0x1514306C, func_15094FE8=0x15094FE8,
    D_800DD1B0=0x800DD1B0, D_800DD208=0x800DD208, D_800DD20C=0x800DD20C,
    D_800DD210=0x800DD210, D_800DD214=0x800DD214,
    D_800BE9F0=0x800BE9F0, D_800BE616=0x800BE616)
DECLARATIONS = '''typedef struct {
    u32 unk0;
    u8 unk4, pad5;
    u16 unk6, unk8;
    u8 unkA, unkB;
} GameTextureSource;
extern s32 D_800DD1B0, D_800DD208, D_800DD20C, D_800DD210;
extern u8 *D_800DD214;
extern s32 D_800BE9F0;
extern u8 D_800BE616;
s32 func_1514306C(GameTextureSource *source, s32 index, s32 subindex, u8 kind);
s32 func_15094FE8(s32, GameTextureSource *, s32, u8 *, s32, s32, s32, s32, s32, s32, s32);
'''
PROTOTYPE = '''Gfx *func_15142E24(Gfx *output, GameTextureSource *source, s32 packed, s32 width,
    s32 height, s32 value, s32 index, u8 kind, u8 *attachment, u8 *sync, s32 flags);'''
SELECTED = '''Gfx *func_15142E24(Gfx *output, GameTextureSource *source, s32 packed, s32 width,
    s32 height, s32 value, s32 index, u8 kind, u8 *attachment, u8 *sync, s32 flags) {
    s32 image = func_1514306C(source, index, packed >> 16, kind);
    if (image != D_800DD1B0 || width != D_800DD208 ||
        height != D_800DD20C || value != D_800DD210 || attachment != D_800DD214) {
        if (*sync == 1) {
            *sync = 0;
        }
        if (D_800BE9F0 == 0x18 || D_800BE9F0 == 0x13 || D_800BE9F0 == 6 ||
            D_800BE9F0 == 0x3B || D_800BE9F0 == 2 || D_800BE616 != 0) {
            flags = 3;
        }
        output = (Gfx *)func_15094FE8((s32)output, source, packed >> 8, attachment, 0, 0, 0,
            width, height, value, flags);
        D_800DD1B0 = image;
        D_800DD208 = width;
        D_800DD20C = height;
        D_800DD210 = value;
        *(u8 *volatile *)&D_800DD214 = *(u8 *volatile *)&D_800DD214;
    }
    return output;
}'''


def candidates():
    for equal_return, captured_world, volatile_world in itertools.product((False, True), repeat=3):
        body = SELECTED
        if equal_return:
            condition = ('    if (image != D_800DD1B0 || width != D_800DD208 ||\n'
                '        height != D_800DD20C || value != D_800DD210 || attachment != D_800DD214) {')
            body = body.replace(condition, '    if (image == D_800DD1B0 && width == D_800DD208 &&\n'
                '        height == D_800DD20C && value == D_800DD210 && attachment == D_800DD214) {\n'
                '        return output;\n    }\n    {')
        if captured_world:
            body = body.replace('    s32 image =', '    s32 world;\n    s32 image =', 1)
            body = body.replace('        if (D_800BE9F0 ==', '        world = D_800BE9F0;\n        if (world ==', 1)
            body = body.replace('|| D_800BE9F0 ==', '|| world ==')
        if volatile_world:
            body = body.replace('D_800BE9F0', '*(volatile s32 *)&D_800BE9F0')
        yield 'early%d-world%d-live%d' % (equal_return, captured_world, volatile_world), body


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n' + DECLARATIONS + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2',
        '-o32', '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I',
        'conker/include/2.0L/PR', '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2',
        '-D_MIPS_SZLONG=32', *PROFILES[profile], '-o', str(obj.relative_to(root)),
        str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = output / 'texture-cache.ld'
    script.write_text('SECTIONS { .text 0x15142E24 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta = functions[FUNCTION]
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), sections(elf)['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, object_words=meta['size'] // 4,
        frame=frames[0] if frames else 0, diagnostics=diagnostics, relocations=relocations,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-texture-cache'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (output / 'maintained-measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
