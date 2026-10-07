"""Recover fixed/float translation extraction and the original repeated address."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15142314, 0x16F7C4, 49
FUNCTION = 'func_15142314'
FLAG = 0x800C3E90
DECLARATIONS = 'extern u8 D_800C3E90;\n'
ADDRESS = 'selected = (u8 *)((u32)matrix + ((u32)index << 6));'
LOW_FIRST_BODY = '''void func_15142314(u8 *matrix, s32 index, f32 *output) {
    u8 *selected;
    f32 scale = 1.0f / 65536.0f;
    if (D_800C3E90 != 0) {
        selected = (u8 *)((u32)matrix + ((u32)index << 6));
        output[0] = ((f32)*(s16 *)(selected + 0x38) + (f32)(*(s16 *)(selected + 0x18) * 65536)) * scale;
        output[1] = ((f32)*(s16 *)(selected + 0x3A) + (f32)(*(s16 *)(selected + 0x1A) * 65536)) * scale;
        output[2] = ((f32)*(s16 *)(selected + 0x3C) + (f32)(*(s16 *)(selected + 0x1C) * 65536)) * scale;
    } else {
        selected = (u8 *)((u32)matrix + ((u32)index << 6));
        output[0] = *(f32 *)(selected + 0x30);
        output[1] = *(f32 *)(selected + 0x34);
        output[2] = *(f32 *)(selected + 0x38);
    }
}'''


def candidates():
    for repeated, low_first, shifted, scale_local in itertools.product((False, True), repeat=4):
        body = LOW_FIRST_BODY
        if not repeated:
            body = body.replace('        ' + ADDRESS + '\n', '')
            body = body.replace('    u8 *selected;', '    u8 *' + ADDRESS)
        for high, low in ((0x18, 0x38), (0x1A, 0x3A), (0x1C, 0x3C)):
            upper = '(f32)(*(s16 *)(selected + 0x%X) * 65536)' % high
            lower = '(f32)*(s16 *)(selected + 0x%X)' % low
            if shifted:
                replacement = '(f32)(s32)((u32)(s32)*(s16 *)(selected + 0x%X) << 16)' % high
                body = body.replace(upper, replacement)
                upper = replacement
            if not low_first:
                body = body.replace(lower + ' + ' + upper, upper + ' + ' + lower)
        if not scale_local:
            body = body.replace('    f32 scale = 1.0f / 65536.0f;\n', '').replace(' * scale;', ' * (1.0f / 65536.0f);')
        yield 'repeated%d-lowfirst%d-shift%d-scale%d' % (repeated, low_first, shifted, scale_local), body


SELECTED = dict(candidates())['repeated1-lowfirst0-shift0-scale1']


def flow_candidates():
    for shape, repeated, left, local in itertools.product(range(6), (False, True), (False, True), (False, True)):
        prefix = 'void func_15142314(u8 *matrix, s32 index, f32 *output) {\n    u8 *selected;\n'
        if local:
            prefix += '    f32 scale = 1.0f / 65536.0f;\n'
        factor = 'scale' if local else '(1.0f / 65536.0f)'
        fixed = '        ' + ADDRESS + '\n'
        floating = fixed
        for i, (high, low) in enumerate(((0x18, 0x38), (0x1A, 0x3A), (0x1C, 0x3C))):
            value = '((f32)(*(s16 *)(selected + 0x%X) * 65536) + (f32)*(s16 *)(selected + 0x%X))' % (high, low)
            value = '%s * %s' % ((factor, value) if left else (value, factor))
            fixed += '        output[%d] = %s;\n' % (i, value)
            floating += '        output[%d] = *(f32 *)(selected + 0x%X);\n' % (i, 0x30 + i * 4)
        if not repeated:
            prefix = prefix.replace('    u8 *selected;', '    u8 *' + ADDRESS)
            fixed, floating = (block.replace('        ' + ADDRESS + '\n', '') for block in (fixed, floating))
        if shape == 0:
            body = '    if (D_800C3E90 != 0) {\n' + fixed + '    } else {\n' + floating + '    }\n'
        elif shape == 1:
            body = '    if (D_800C3E90 == 0) {\n' + floating + '        return;\n    }\n' + fixed
        elif shape == 2:
            body = '    if (D_800C3E90 != 0) {\n' + fixed + '        return;\n    }\n' + floating
        elif shape == 3:
            body = '    if (D_800C3E90 == 0) {\n' + floating + '    } else {\n' + fixed + '    }\n'
        elif shape == 4:
            body = '    if (D_800C3E90 == 0) {\n        goto floating;\n    }\n' + fixed + '    return;\nfloating:\n' + floating
        else:
            body = '    switch (D_800C3E90) {\n    case 0:\n' + floating + '        return;\n    default:\n' + fixed + '        return;\n    }\n'
        yield 'flow%d-repeated%d-left%d-local%d' % (shape, repeated, left, local), prefix + body + '}'


def temporary_candidates():
    for kind, register, repeated, left in itertools.product(range(3), (False, True), (False, True), (False, True)):
        body = SELECTED
        if not repeated:
            body = body.replace('        ' + ADDRESS + '\n', '')
            body = body.replace('    u8 *selected;', '    u8 *' + ADDRESS)
        declaration = '    f32 high, low;\n' if kind < 2 else '    f32 value;\n'
        body = body.replace('    f32 scale', declaration + '    f32 scale')
        if register:
            body = body.replace('    f32 scale', '    register f32 scale')
        for i, (high, low) in enumerate(((0x18, 0x38), (0x1A, 0x3A), (0x1C, 0x3C))):
            upper = '(f32)(*(s16 *)(selected + 0x%X) * 65536)' % high
            lower = '(f32)*(s16 *)(selected + 0x%X)' % low
            line = '        output[%d] = (%s + %s) * scale;' % (i, upper, lower)
            if kind < 2:
                statements = ['        high = %s;' % upper, '        low = %s;' % lower]
                if kind == 1:
                    statements.reverse()
                result = '(high + low)'
            else:
                statements = ['        value = %s + %s;' % (upper, lower)]
                result = 'value'
            expression = 'scale * %s' % result if left else '%s * scale' % result
            statements.append('        output[%d] = %s;' % (i, expression))
            assert line in body
            body = body.replace(line, '\n'.join(statements))
        yield 'temporary%d-register%d-repeated%d-left%d' % (kind, register, repeated, left), body


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3', declarations=DECLARATIONS, isa='mips2'):
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n' + declarations + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-' + isa, '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, text=True, capture_output=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'translation.ld'
    script.write_text('SECTIONS { .text 0x15142314 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        '--defsym=D_800C3E90=0x%X' % FLAG, '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, functions, rel = parse_object(obj)
    meta = functions[FUNCTION]
    pools = sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, body_words=end, profile=profile, isa=isa, frame=frames[0] if frames else 0,
        pool_bytes=len(pools.get('.rodata', (0, b''))[1]),
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics=diagnostics, relocations=rel), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--flow', action='store_true', help='measure the 48 additional O2/g3 flow forms')
    modes.add_argument('--access', action='store_true', help='measure the 16 ISA/access qualifier controls')
    modes.add_argument('--temporaries', action='store_true', help='measure 24 real O2/g3 scalar-temporary forms')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-matrix-translation'
    out.mkdir(exist_ok=True)
    records = []
    if args.access:
        chosen = dict(candidates())['repeated1-lowfirst0-shift0-scale1']
        for isa, profile, volatile in itertools.product(('mips1', 'mips2'), ('o2g3', 'o2'), range(4)):
            body, declarations = chosen, DECLARATIONS
            if volatile & 1:
                body = body.replace('f32 *output)', 'volatile f32 *output)')
            if volatile & 2:
                declarations = declarations.replace('extern u8 ', 'extern volatile u8 ')
            name = 'access%d-%s-%s' % (volatile, isa, profile)
            record, _ = compile_candidate(root, out, name, body, profile, declarations, isa)
            records.append(record)
            print(name, record['body_words'], record['differences'], flush=True)
        (out / 'access-measurements.json').write_text(json.dumps(records, indent=2) + '\n')
        return
    forms = temporary_candidates() if args.temporaries else flow_candidates() if args.flow else candidates()
    for name, body in forms:
        for profile in (('o2g3',) if args.flow or args.temporaries else PROFILES):
            record, _ = compile_candidate(root, out, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    filename = 'temporary-measurements.json' if args.temporaries else 'flow-measurements.json' if args.flow else 'measurements.json'
    (out / filename).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
