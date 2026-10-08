"""Fit the fourth tile-size command updater from its complete retail slot."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15031E7C, 0x5F32C, 83
FUNCTION, SCALE = 'func_15031E7C', 0x800970DC
DECLARATIONS = 'extern f32 D_800970DC;'
SELECTED = '''s32 func_15031E7C(u8 *node, u8 *actor) {
    u8 *source;
    Gfx *commands;
    f32 factor;
    s32 index;
    s32 remaining;

    source = *(u8 **)(actor + 0x2D0);
    if (source == 0) {
        return 0;
    }
    commands = *(Gfx **)*(u8 **)(node + 0x24);
    if (commands == 0) {
        return 0;
    }
    if (*(u16 *)(actor + 0x84) == 0x55) {
        factor = 1.0f;
    } else if (*(u16 *)(actor + 0x84) == 0x56) {
        factor = 0.0f;
    } else if (0.0f <= *(f32 *)(source + 8) && *(f32 *)(source + 8) <= 120.0f) {
        factor = *(f32 *)(source + 8) * D_800970DC;
        factor = 1.0f - factor;
    } else {
        factor = 0.0f;
    }
    index = 0;
    remaining = 4;
    do {
        remaining--;
        while (*(s8 *)&commands[index] != (s8)G_SETTILESIZE) {
            index++;
        }
        if (remaining != 0) {
            index++;
        }
    } while (remaining != 0);
    commands[index].words.w0 = _SHIFTL(G_SETTILESIZE, 24, 8) | _SHIFTL(2, 12, 12) |
        ((s32)(25.0f * factor + 2.0f) & 0xFFF);
    return 0;
}'''


def candidates():
    for kind, registers, loop in itertools.product(('Gfx', 'bytes'), (False, True), ('countdown', 'for')):
        body = SELECTED
        if registers:
            body = body.replace('u8 *node, u8 *actor', 'register u8 *node, register u8 *actor')
        if kind == 'bytes':
            body = body.replace('Gfx *commands;', 'u8 *commands;').replace('*(Gfx **)', '*(u8 **)')
            body = body.replace('*(s8 *)&commands[index]', '*(s8 *)(commands + index * 8)')
            body = body.replace('commands[index].words.w0', '*(u32 *)(commands + index * 8)')
        if loop == 'for':
            body = body.replace('    remaining = 4;\n    do {\n        remaining--;',
                '    for (remaining = 4; remaining != 0;) {\n        remaining--;').replace(
                    '    } while (remaining != 0);', '    }')
        yield '%s-register%d-%s' % (kind, registers, loop), body
    yield 'single-expression-factor', SELECTED.replace(
        '        factor = *(f32 *)(source + 8) * D_800970DC;\n        factor = 1.0f - factor;',
        '        factor = 1.0f - *(f32 *)(source + 8) * D_800970DC;')


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3'):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name+suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n'+DECLARATIONS+'\n'+body+'\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    if result.returncode or result.stdout or result.stderr:
        raise ValueError(result.stdout+result.stderr)
    script = out / 'node-tile.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % ENTRY)
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        '--defsym=D_800970DC=0x800970DC', '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, functions, relocs = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics='', relocations=relocs, pool_bytes=sum(len(v[1]) for n, v in pools.items()
            if n in ('.rodata', '.data'))), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-node-tile'
    forms = [('profile-'+p, SELECTED, p) for p in PROFILES] if args.profiles else (
        [(name, body, 'o2g3') for name, body in candidates()])
    records = []
    for name, body, profile in forms:
        record, _ = compile_candidate(root, out, name, body, profile)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], record['pool_bytes'], flush=True)
    (out / ('profiles.json' if args.profiles else 'measurements.json')).write_text(json.dumps(records, indent=2)+'\n')


if __name__ == '__main__':
    main()
