"""Screen signed descriptor sampling and the original unsigned angle conversion."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x151432BC, 0x17076C, 254
FUNCTION = 'func_151432BC'
SYMBOLS = dict(func_150ADA20=0x150ADA20, func_150ADA68=0x150ADA68,
    func_151423D8=0x151423D8, D_800A5644=0x800A5644)
DECLARATIONS = '''typedef struct {
    s16 x, y, z, radius, height, width;
    u8 padC[4];
    f32 angle;
    u8 pad14, flags;
} GameAreaSampleDescriptor;
'''
PROTOTYPE = 'void func_151432BC(GameAreaSampleDescriptor *source, f32 *x, f32 *z, f32 *top, f32 *bottom);'
BASELINE = '''void func_151432BC(GameAreaSampleDescriptor *source, f32 *x, f32 *z, f32 *top, f32 *bottom) {
    struct209 scratch;
    f32 distance;
    f32 width;
    s32 mode;
    mode = source->flags & 3;
    if (mode == 0) {
        scratch.unk1B = func_150ADA20();
        scratch.unk14 = func_151423D8((scratch.unk1B - 64) & 0xFF);
        scratch.unk10 = func_151423D8(scratch.unk1B);
        distance = func_150ADA68() * source->radius;
        *x = source->x + distance * scratch.unk10;
        *z = source->z - distance * scratch.unk14;
        *top = source->y + source->height;
        *bottom = source->y;
    } else if (mode != 1) {
        if (mode == 2) {
            scratch.unk2F = (u32)(source->angle * D_800A5644);
            scratch.unk28 = func_151423D8(scratch.unk2F - 64);
            scratch.unk24 = func_151423D8(scratch.unk2F);
            scratch.unk20 = func_150ADA68() * (2.0f * source->radius) + (f32)-source->radius;
            width = func_150ADA68() * (2.0f * source->width) + (f32)-source->width;
            *x = source->x + (scratch.unk20 * scratch.unk24 + width * scratch.unk28);
            *z = source->z + (width * scratch.unk24 - scratch.unk20 * scratch.unk28);
            *top = source->y + source->height;
            *bottom = source->y;
        } else {
            *x = source->x;
            *z = source->z;
            *top = source->y + source->height;
            *bottom = source->y - source->height;
        }
    } else {
        scratch.unkB = func_150ADA20();
        scratch.unk4 = func_151423D8(scratch.unkB - 64);
        scratch.unk0 = func_151423D8(scratch.unkB);
        distance = func_150ADA68() * source->radius;
        *x = source->x + distance * scratch.unk0;
        *z = source->z - distance * scratch.unk4;
        *top = source->y + source->height;
        *bottom = source->y - source->height;
    }
}'''

SWITCH = '''void func_151432BC(GameAreaSampleDescriptor *source, f32 *x, f32 *z, f32 *top, f32 *bottom) {
    struct209 scratch;
    f32 distance;
    f32 width;
    switch (source->flags & 3) {
        default:
            *x = source->x;
            *z = source->z;
            *top = source->y + source->height;
            *bottom = source->y - source->height;
            break;
        case 2:
            scratch.unk2F = (u32)(source->angle * D_800A5644);
            scratch.unk28 = func_151423D8(scratch.unk2F - 64);
            scratch.unk24 = func_151423D8(scratch.unk2F);
            scratch.unk20 = func_150ADA68() * (2.0f * source->radius) + (f32)-source->radius;
            width = func_150ADA68() * (2.0f * source->width) + (f32)-source->width;
            *x = source->x + (scratch.unk20 * scratch.unk24 + width * scratch.unk28);
            *z = source->z + (width * scratch.unk24 - scratch.unk20 * scratch.unk28);
            *top = source->y + source->height;
            *bottom = source->y;
            break;
        case 0:
            scratch.unk1B = func_150ADA20();
            scratch.unk14 = func_151423D8((scratch.unk1B - 64) & 0xFF);
            scratch.unk10 = func_151423D8(scratch.unk1B);
            distance = func_150ADA68() * source->radius;
            *x = source->x + distance * scratch.unk10;
            *z = source->z - distance * scratch.unk14;
            *top = source->y + source->height;
            *bottom = source->y;
            break;
        case 1:
            scratch.unkB = func_150ADA20();
            scratch.unk4 = func_151423D8(scratch.unkB - 64);
            scratch.unk0 = func_151423D8(scratch.unkB);
            distance = func_150ADA68() * source->radius;
            *x = source->x + distance * scratch.unk0;
            *z = source->z - distance * scratch.unk4;
            *top = source->y + source->height;
            *bottom = source->y - source->height;
            break;
    }
}'''
EARLY = SWITCH.replace('(scratch.unk1B - 64) & 0xFF', 'scratch.unk1B - 64').replace(
    '            *bottom = source->y;\n            break;', '            *bottom = source->y;\n            return;')
TEMP = EARLY.replace('    f32 width;', '    f32 width;\n    f32 tangent;').replace(
    '            *x = source->x + (scratch.unk20 * scratch.unk24 + width * scratch.unk28);',
    '            tangent = width * scratch.unk24;\n'
    '            *x = source->x + (scratch.unk20 * scratch.unk24 + width * scratch.unk28);').replace(
    '*z = source->z + (width * scratch.unk24 - scratch.unk20 * scratch.unk28);',
    '*z = source->z + (tangent - scratch.unk20 * scratch.unk28);')
SELECTED = EARLY


def goto_body(common=False, local=False):
    parts = EARLY.split('        default:\n', 1)[1]
    default, parts = parts.split('        case 2:\n')
    rectangle, parts = parts.split('        case 0:\n')
    circle0, circle1 = parts.split('        case 1:\n')
    circle1 = circle1.rsplit('    }\n}', 1)[0]
    blocks = [default, rectangle, circle0, circle1]
    blocks = [block.replace('            break;\n', '').replace('            return;\n', '') for block in blocks]
    body = EARLY.split('    switch (', 1)[0]
    mode = 'mode' if local else '(source->flags & 3)'
    if local: body += '    s32 mode = source->flags & 3;\n'
    body += '    if (%s == 0) goto circle0;\n    if (%s == 1) goto circle1;\n    if (%s == 2) goto rectangle;\n' % (mode, mode, mode)
    for i, (label, block) in enumerate(zip(('', 'rectangle', 'circle0', 'circle1'), blocks)):
        if label: body += label + ':\n'
        body += block + ('    goto done;\n' if common or i == 0 else '    return;\n')
    return body + 'done:\n    return;\n}'


def candidates():
    for doubles, mode_byte, order, masks in itertools.product((False, True), repeat=4):
        body = BASELINE
        if doubles:
            for field in ('radius', 'width'):
                body = body.replace('2.0f * source->' + field,
                    '(f32)source->%s + (f32)source->%s' % (field, field))
        if mode_byte: body = body.replace('s32 mode;', 'u8 mode;')
        if order:
            body = body.replace('    struct209 scratch;\n    f32 distance;\n    f32 width;',
                '    f32 distance;\n    f32 width;\n    struct209 scratch;')
        if masks: body = body.replace('(scratch.unk1B - 64) & 0xFF', 'scratch.unk1B - 64')
        yield 'double%d-byte%d-order%d-mask%d' % (doubles, mode_byte, order, masks), body
    for local, masks in itertools.product((False, True), repeat=2):
        body = SWITCH
        if local:
            body = body.replace('    switch (source->flags & 3)',
                '    s32 mode = source->flags & 3;\n    switch (mode)')
        if masks:
            body = body.replace('(scratch.unk1B - 64) & 0xFF', 'scratch.unk1B - 64')
        yield 'switch-local%d-mask%d' % (local, masks), body
    yield 'switch-early', EARLY
    yield 'switch-tangent', TEMP
    for common, local in itertools.product((False, True), repeat=2):
        yield 'goto-common%d-local%d' % (common, local), goto_body(common, local)
    for kind in ('s32', 'u32', 'u8'):
        for temp in (False, True):
            body = TEMP if temp else EARLY
            body = body.replace('    f32 width;', '    f32 width;\n    %s random;' % kind)
            for field in ('unk1B', 'unkB'):
                body = body.replace('scratch.%s = func_150ADA20();' % field,
                    'random = func_150ADA20();\n            scratch.%s = random;' % field)
                body = body.replace('func_151423D8(scratch.%s - 64)' % field, 'func_151423D8(random - 64)')
            yield 'random-%s-tangent%d' % (kind, temp), body


def storage_candidates():
    yield 'sample', SELECTED.replace('    f32 width;', '    f32 width;\n    f32 sample;').replace(
        'distance = func_150ADA68() * source->radius;',
        'sample = func_150ADA68();\n            distance = sample * source->radius;'), DECLARATIONS
    yield 'signed-flags', SELECTED, DECLARATIONS.replace('u8 pad14, flags;', 'u8 pad14; s8 flags;')
    yield 'volatile-scratch', SELECTED.replace('struct209 scratch;', 'volatile struct209 scratch;'), DECLARATIONS
    yield 'volatile-angle', SELECTED.replace('struct209 scratch;', 'GameAreaScratch scratch;'), DECLARATIONS + '''typedef struct {
    f32 unk0, unk4; u8 pad8[3]; volatile u8 unkB; u8 padC[4];
    f32 unk10, unk14; u8 pad18[3]; volatile u8 unk1B; u8 pad1C[4];
    f32 unk20, unk24, unk28; u8 pad2C[3]; volatile u8 unk2F;
} GameAreaScratch;
'''
    yield 'int-scale', SELECTED.replace('2.0f * source->radius', '2 * source->radius').replace(
        '2.0f * source->width', '2 * source->width'), DECLARATIONS
    yield 'explicit-cast', SELECTED.replace('source->radius;', '(f32)source->radius;'), DECLARATIONS


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3', declarations=DECLARATIONS):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n#include "variables.h"\n' + declarations + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2',
        '-o32', '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I',
        'conker/include/2.0L/PR', '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2',
        '-D_MIPS_SZLONG=32', *PROFILES[profile], '-o', str(obj.relative_to(root)),
        str(source.relative_to(root))], cwd=root, capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics: raise ValueError(diagnostics)
    script = output / 'sampler.ld'
    script.write_text('SECTIONS { .text 0x151432BC : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta = functions[FUNCTION]
    pools = sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:]); words = words[:end]
    retail = struct.unpack_from('>254I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, object_words=meta['size'] // 4,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics=diagnostics, frame=frames[0] if frames else 0, relocations=relocations,
        pool_bytes=len(pools.get('.rodata', (0, b''))[1])), words


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-area-sampler'; output.mkdir(exist_ok=True)
    records = []
    shapes = [(name, body, DECLARATIONS) for name, body in candidates()] + list(storage_candidates())
    for name, body, declarations in shapes:
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile, declarations)
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__': main()
