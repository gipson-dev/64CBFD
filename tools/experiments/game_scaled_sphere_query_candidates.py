"""Recover the complete scaled-sphere caller; candidates are opt-in only."""

import itertools
import json
import struct
import subprocess
import sys
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS, FUNCTION = 0x15145AD8, 0x172F88, 110, 'func_15145AD8'
SYMBOLS = {'func_1515C1A0': 0x1515C1A0, 'func_15145128': 0x15145128,
           'func_151451F0': 0x151451F0}
PROTOTYPE = '''s32 func_15145AD8(struct17 *arg0, struct17 *arg1, struct127 *arg2,
    struct17 *arg3, struct17 *arg4, f32 *arg5, f32 *arg6, struct17 *arg7);'''
DECLARATIONS = '''void func_1515C1A0(struct127 *, struct17 *, f32 *, f32 *);
s32 func_15145128(struct17 *, struct17 *, f32 *, f32 *);
s32 func_151451F0(struct17 *, struct17 *, struct17 *, f32, f32,
    struct17 *, struct17 *, f32 *, f32 *);
'''
BASELINE = '''s32 func_15145AD8(struct17 *arg0, struct17 *arg1, struct127 *arg2,
    struct17 *arg3, struct17 *arg4, f32 *arg5, f32 *arg6, struct17 *arg7) {
    struct17 center;
    f32 radius;
    f32 height;
    struct17 origin;
    struct17 direction;
    struct17 scaledCenter;
    f32 length;
    f32 first;
    f32 second;
    f32 scale;
    f32 inverse;
    f32 reciprocal;

    if (arg5 != NULL) {
        arg5 = &radius;
    }
    if (arg6 != NULL) {
        arg6 = &height;
    }
    if (arg7 != NULL) {
        arg7 = &center;
    }
    func_1515C1A0(arg2, arg7, arg5, arg6);
    if (*arg6 == 0.0f) {
        return 0;
    }
    if (*arg5 == 0.0f) {
        return 0;
    }
    inverse = arg2->unkE0;
    scale = arg2->unkDC;
    origin.unk0 = arg0->unk0;
    origin.unk4 = arg0->unk4 * scale;
    origin.unk8 = arg0->unk8;
    direction.unk0 = arg1->unk0;
    direction.unk4 = arg1->unk4 * scale;
    direction.unk8 = arg1->unk8;
    if (func_15145128(&direction, &direction, &length, &reciprocal)) {
        scaledCenter.unk0 = arg7->unk0;
        scaledCenter.unk4 = arg7->unk4 * scale;
        scaledCenter.unk8 = arg7->unk8;
        if (func_151451F0(&origin, &direction, &scaledCenter, *arg5, length,
                arg3, arg4, &first, &second)) {
            arg3->unk4 *= inverse;
            arg4->unk4 *= inverse;
            return 1;
        } else {
            return 0;
        }
    } else {
        return 0;
    }
}'''


def flow_body(gates=0, final=0):
    body = BASELINE
    body = body.replace('''    if (func_15145128(&direction, &direction, &length, &reciprocal)) {''',
        '''    if (!func_15145128(&direction, &direction, &length, &reciprocal)) {
        return 0;
    }
    {''').replace('''    } else {
        return 0;
    }
}''', '    }\n}')
    if final:
        body = body.replace('''        if (func_151451F0(&origin, &direction, &scaledCenter, *arg5, length,
                arg3, arg4, &first, &second)) {''',
            '''        if (!func_151451F0(&origin, &direction, &scaledCenter, *arg5, length,
                arg3, arg4, &first, &second)) {
            return 0;
        }
        {''').replace('''        } else {
            return 0;
        }''', '        }')
    if gates == 1:
        body = body.replace('''    if (*arg5 == 0.0f) {
        return 0;
    }''', '    if (*arg5 != 0.0f) {').removesuffix('\n}') + '\n    }\n    return 0;\n}'
    elif gates == 2:
        body = body.replace('''    if (*arg6 == 0.0f) {
        return 0;
    }
    if (*arg5 == 0.0f) {''', '    if (*arg6 == 0.0f || *arg5 == 0.0f) {')
    return body


SELECTED = BASELINE[:BASELINE.index('    if (func_15145128')] + '''    if (!func_15145128(&direction, &direction, &length, &reciprocal)) {
        return 0;
    }
    scaledCenter.unk0 = arg7->unk0;
    scaledCenter.unk4 = arg7->unk4 * scale;
    scaledCenter.unk8 = arg7->unk8;
    if (!func_151451F0(&origin, &direction, &scaledCenter, *arg5, length,
            arg3, arg4, &first, &second)) {
        return 0;
    }
    arg3->unk4 *= inverse;
    arg4->unk4 *= inverse;
    return 1;
}'''


def local_layout(obj):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'ultralib/tools'))
    from libelf import ElfFile
    from mdebug import EcoffSt
    elf = ElfFile(Path(obj).read_bytes())
    for fdr in elf.find_section_by_name('.mdebug').fdrs:
        for pdr in fdr.pdrs:
            if pdr.name == FUNCTION:
                return dict(frame=pdr.frameoffset, entry_relative={
                    s.name: s.value - 0x100000000 if s.value & 0x80000000 else s.value
                    for s in pdr.symrs if s.st == EcoffSt.LOCAL})
    raise ValueError('Missing scaled query debug procedure')


def compile_candidate(root, out, name, body=SELECTED, profile='o2g3'):
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "structs.h"\n' + DECLARATIONS + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn',
        '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root,
        capture_output=True, text=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics or 'IDO compilation failed')
    script = out / (name + '.ld')
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % ENTRY)
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta = functions[FUNCTION]
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), sections(elf)['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>110I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frame = (-words[0]) & 65535 if words[0] & 0xFFFF0000 == 0x27BD0000 else 0
    return dict(name=name, profile=profile, body_words=end, frame=frame, diagnostics=diagnostics,
        relocations=relocations, exact=words == list(retail),
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def candidates():
    for combined, nested, reverse in itertools.product((False, True), repeat=3):
        body = BASELINE
        if combined:
            body = body.replace('''    if (*arg6 == 0.0f) {
        return 0;
    }
    if (*arg5 == 0.0f) {''', '    if (*arg6 == 0.0f || *arg5 == 0.0f) {')
        if not nested:
            body = body.replace('''    if (func_15145128(&direction, &direction, &length, &reciprocal)) {''',
                '''    if (!func_15145128(&direction, &direction, &length, &reciprocal)) {
        return 0;
    }
    {''').replace('''    } else {
        return 0;
    }
}''', '    }\n}')
        if reverse:
            body = body.replace('arg0->unk4 * scale', 'scale * arg0->unk4').replace(
                'arg1->unk4 * scale', 'scale * arg1->unk4').replace('arg7->unk4 * scale', 'scale * arg7->unk4')
        yield 'combined%d-nested%d-reverse%d' % (combined, nested, reverse), body
    for gates, final in itertools.product(range(3), (False, True)):
        yield 'flow-gate%d-final%d' % (gates, final), flow_body(gates, final)
    yield 'straight', SELECTED


def negatives():
    yield 'ordinary-null-fallback', SELECTED.replace('!= NULL', '== NULL')
    yield 'late-inverse', SELECTED.replace('    inverse = arg2->unkE0;\n', '').replace(
        'arg3->unk4 *= inverse;', 'inverse = arg2->unkE0;\n            arg3->unk4 *= inverse;')
    yield 'unscaled-direction', SELECTED.replace('arg1->unk4 * scale', 'arg1->unk4')
    yield 'missing-output-unscale', SELECTED.replace('    arg4->unk4 *= inverse;\n', '')


def fit_candidates():
    for mask in range(1, 8):
        body = SELECTED
        for flag, name in ((1, 'origin'), (2, 'direction'), (4, 'scaledCenter')):
            if not mask & flag:
                continue
            body = body.replace('    struct17 %s;' % name, '    union {struct17 point; f32 values[3];} %s;' % name)
            for axis, member in enumerate(('unk0', 'unk4', 'unk8')):
                body = body.replace(name + '.' + member, '%s.values[%d]' % (name, axis))
            body = body.replace('&' + name, '&' + name + '.point')
        yield 'storage%d' % mask, body
    for all_pointers, hint in itertools.product((False, True), repeat=2):
        qualifier = 'register ' if hint else ''
        declarations = '    %sstruct17 *normalized;\n' % qualifier
        assignment = '    normalized = &direction;\n'
        arguments = 'normalized, normalized, &length, &reciprocal'
        if all_pointers:
            declarations += '    %sf32 *normalLength;\n    %sf32 *normalReciprocal;\n' % (qualifier, qualifier)
            assignment += '    normalLength = &length;\n    normalReciprocal = &reciprocal;\n'
            arguments = 'normalized, normalized, normalLength, normalReciprocal'
        body = SELECTED.replace('    f32 reciprocal;\n', '    f32 reciprocal;\n' + declarations).replace(
            '    if (*arg5 == 0.0f)', assignment + '    if (*arg5 == 0.0f)').replace(
            'func_15145128(&direction, &direction, &length, &reciprocal)', 'func_15145128(' + arguments + ')')
        yield 'prepare-all%d-register%d' % (all_pointers, hint), body


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-scaled-sphere-query'
    out.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, out, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    for name, body in fit_candidates():
        record, _ = compile_candidate(root, out, name, body)
        records.append(record)
        print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')
    compile_candidate(root, out, 'selected')
    (out / 'local-layout.json').write_text(json.dumps(local_layout(out / 'selected.o'), indent=2) + '\n')


if __name__ == '__main__':
    main()
