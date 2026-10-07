"""Recover record-batch source phases and three real destination cursors."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_point_list_transform_candidates import DECLARATIONS, SYMBOLS
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15145DB4, 0x173264, 60
FUNCTION = 'func_15145DB4'
BASELINE = '''void func_15145DB4(u8 *arg0, struct17 *arg1, struct17 *arg2, s32 arg3) {
    f32 mtx[4][4];

    func_150A8050(mtx, *(f32 *)(arg0 + 0), *(f32 *)(arg0 + 4), *(f32 *)(arg0 + 8));
    mtx[3][0] = *(s16 *)(arg0 + 0x10);
    mtx[3][1] = *(s16 *)(arg0 + 0x12);
    mtx[3][2] = *(s16 *)(arg0 + 0x14);

    while (arg3 > 0) {
        func_150A7960(mtx, arg1->unk0, arg1->unk4, arg1->unk8, &arg2->unk0, &arg2->unk4, &arg2->unk8);
        arg3--;
        arg1++;
        arg2++;
    }
}'''


def candidates():
    for phase, early, loop, arrays in itertools.product((False, True), (False, True), range(3), (False, True)):
        declaration = '    f32 *x;\n    f32 *y;\n    f32 *z;\n'
        if not phase:
            declaration += '    %s *source;\n' % ('f32' if arrays else 'struct17')
        body = BASELINE.replace('    f32 mtx[4][4];\n', '    f32 mtx[4][4];\n' + declaration)
        outputs = '    x = &arg2->unk0;\n    y = &arg2->unk4;\n    z = &arg2->unk8;\n'
        marker = '    mtx[3][0]' if early else '    while (arg3 > 0)'
        body = body.replace(marker, outputs + marker, 1)
        switch = 'arg0 = (u8 *)arg1;' if phase else 'source = %sarg1;' % ('(f32 *)' if arrays else '')
        if loop == 0:
            body = body.replace('    while (arg3 > 0)', '    %s\n    while (arg3 > 0)' % switch)
        elif loop == 1:
            body = body.replace('    while (arg3 > 0) {', '    if (arg3 > 0) {\n        %s\n        do {' % switch)
            body = body.replace('        arg2++;\n    }', '        arg2++;\n        } while (arg3 > 0);\n    }')
        else:
            body = body.replace('    while (arg3 > 0) {', '    if (arg3 > 0) {\n        %s\n        while (arg3 > 0) {' % switch)
            body = body.replace('        arg2++;\n    }', '        arg2++;\n        }\n    }')
        if phase:
            view = '((f32 *)arg0)' if arrays else '((struct17 *)arg0)'
            coordinates = ', '.join(view + ('[%d]' % axis if arrays else '->' + field)
                for axis, field in enumerate(('unk0', 'unk4', 'unk8')))
            update = 'arg0 += 12;'
        else:
            coordinates = ', '.join('source' + ('[%d]' % axis if arrays else '->' + field)
                for axis, field in enumerate(('unk0', 'unk4', 'unk8')))
            update = 'source += 3;' if arrays else 'source++;'
        body = body.replace('arg1->unk0, arg1->unk4, arg1->unk8, &arg2->unk0, &arg2->unk4, &arg2->unk8',
            coordinates + ', x, y, z')
        body = body.replace('        arg1++;\n        arg2++;', '        %s\n        x += 3;\n        y += 3;\n        z += 3;' % update)
        yield 'phase%d-early%d-loop%d-arrays%d' % (phase, early, loop, arrays), body


def storage_candidates():
    base = dict(candidates())['phase1-early1-loop1-arrays0']
    for mask, first in itertools.product(range(1, 16), (False, True)):
        body, declarations = base, ''
        if mask & 1:
            declarations += '    f32 rx, ry, rz;\n'
            line = '    func_150A8050(mtx, *(f32 *)(arg0 + 0), *(f32 *)(arg0 + 4), *(f32 *)(arg0 + 8));'
            body = body.replace(line, '    rx = *(f32 *)(arg0 + 0);\n    ry = *(f32 *)(arg0 + 4);\n'
                '    rz = *(f32 *)(arg0 + 8);\n    func_150A8050(mtx, rx, ry, rz);')
        if mask & 2:
            declarations += '    f32 tx, ty, tz;\n'
            for i, axis in enumerate('xyz'):
                line = '    mtx[3][%d] = *(s16 *)(arg0 + 0x%X);' % (i, 16 + i * 2)
                body = body.replace(line, '    t%s = *(s16 *)(arg0 + 0x%X);\n    mtx[3][%d] = t%s;' % (axis, 16 + i * 2, i, axis))
        if mask & 4:
            declarations += '    f32 px, py, pz;\n'
            body = body.replace('        func_150A7960(',
                '        px = ((struct17 *)arg0)->unk0;\n        py = ((struct17 *)arg0)->unk4;\n'
                '        pz = ((struct17 *)arg0)->unk8;\n        func_150A7960(', 1)
            body = body.replace('((struct17 *)arg0)->unk0, ((struct17 *)arg0)->unk4, ((struct17 *)arg0)->unk8', 'px, py, pz')
        if mask & 8:
            declarations += '    s32 remaining;\n'
            body = body.replace('    if (arg3 > 0)', '    remaining = arg3;\n    if (remaining > 0)')
            body = body.replace('        arg3--;', '        remaining--;').replace('while (arg3 > 0)', 'while (remaining > 0)')
        body = body.replace('    f32 mtx[4][4];\n', declarations + '    f32 mtx[4][4];\n' if first else
            '    f32 mtx[4][4];\n' + declarations)
        yield 'storage-mask%d-first%d' % (mask, first), body
    for order in itertools.permutations(range(3)):
        body = base
        declarations = ('    f32 *x;\n', '    f32 *y;\n', '    f32 *z;\n')
        body = body.replace(''.join(declarations), ''.join(declarations[i] for i in order))
        yield 'cursor-order-' + ''.join(map(str, order)), body


def reload_candidates():
    base = dict(storage_candidates())['storage-mask2-first0']
    for type_name, mask in itertools.product(('s16', 's32'), range(1, 8)):
        body = base.replace('    f32 tx, ty, tz;\n', ''.join('    %s t%s;\n' % (type_name, axis)
            for i, axis in enumerate('xyz') if mask >> i & 1))
        for i, axis in enumerate('xyz'):
            if not mask >> i & 1:
                body = body.replace('    t%s = *(s16 *)(arg0 + 0x%X);\n    mtx[3][%d] = t%s;' % (axis, 16 + i * 2, i, axis),
                    '    mtx[3][%d] = *(s16 *)(arg0 + 0x%X);' % (i, 16 + i * 2))
        yield 'integer-%s-mask%d' % (type_name, mask), body
    for source, descriptor in itertools.product(('plain', 'volatile', 'register'), ('plain', 'register')):
        body = base
        if source != 'plain':
            body = body.replace('struct17 *arg1', 'struct17 * volatile arg1' if source == 'volatile' else 'register struct17 *arg1')
        if descriptor == 'register':
            body = body.replace('u8 *arg0', 'register u8 *arg0')
        yield 'reload-source-%s-descriptor-%s' % (source, descriptor), body
    for style in range(4):
        body = base
        if style == 0:
            body = body.replace('    if (arg3 > 0) {\n', '    if (arg3 <= 0) return;\n    {\n')
        elif style == 1:
            body = body.replace('    if (arg3 > 0) {\n', '    if (arg3 <= 0) goto done;\n    {\n').replace('\n}', '\ndone:;\n}', 1)
        elif style == 2:
            body = body.replace('    if (arg3 > 0) {\n', '    if (arg3 > 0) goto loop;\n    return;\nloop:\n    {\n')
        else:
            body = body.replace('    if (arg3 > 0) {\n', '    if (arg3 <= 0) { return; } else {\n')
        yield 'reload-flow%d' % style, body


def gate_candidates():
    for name, source in reload_candidates():
        if not name.startswith('integer-'):
            continue
        body = source.replace('    if (arg3 > 0) {\n', '    if (arg3 > 0) goto loop;\n    return;\nloop:\n    {\n')
        yield 'gate-' + name, body
    bases = (dict(storage_candidates())['storage-mask2-first0'], dict(reload_candidates())['integer-s32-mask6'])
    for n, source in enumerate(bases):
        for style in range(3):
            body = source
            if style == 0:
                body = body.replace('        } while (arg3 > 0);\n    }', '        } while (arg3 > 0);\n    } else { return; }')
            elif style == 1:
                body = body.replace('    if (arg3 > 0) {\n', '    switch (arg3 > 0) {\n    case 1:\n    {\n')
                body = body.replace('        } while (arg3 > 0);\n    }', '        } while (arg3 > 0);\n    }\n    default: return;\n    }')
            else:
                body = body.replace('    if (arg3 > 0) {\n', '    while (arg3 > 0) {\n')
            yield 'gate-base%d-style%d' % (n, style), body


SELECTED = '''void func_15145DB4(u8 *cursor, struct17 *input, struct17 *destination, s32 count) {
    f32 matrix[4][4];
    s32 translationY;
    s32 translationZ;
    f32 *x;
    f32 *y;
    f32 *z;

    func_150A8050(matrix, *(f32 *)(cursor + 0), *(f32 *)(cursor + 4), *(f32 *)(cursor + 8));
    x = &destination->unk0;
    y = &destination->unk4;
    z = &destination->unk8;
    matrix[3][0] = *(s16 *)(cursor + 0x10);
    translationY = *(s16 *)(cursor + 0x12);
    matrix[3][1] = translationY;
    translationZ = *(s16 *)(cursor + 0x14);
    matrix[3][2] = translationZ;

    /* Keep the source reload on the positive-count path. */
    if (count > 0) goto transform;
    return;
transform:
    cursor = (u8 *)input;
    do {
        func_150A7960(matrix, ((struct17 *)cursor)->unk0, ((struct17 *)cursor)->unk4, ((struct17 *)cursor)->unk8, x, y, z);
        count--;
        cursor += 12;
        x += 3;
        y += 3;
        z += 3;
    } while (count > 0);
}'''


def normalize(words):
    """Close saved-register and two halfword-temporary cycles; preserve private layout."""
    assert len(words) == WORDS
    result = list(words)
    rename = {18: 19, 19: 20, 20: 18, 2: 15, 15: 2, 3: 24, 24: 3}
    for i in range(4, 51):
        word, op = result[i], result[i] >> 26
        fields = (21, 16, 11) if op == 0 else (16,) if op == 17 and word >> 21 & 31 == 4 else (
            (21, 16) if op in (6, 7, 9, 33, 35, 43) else ())
        for shift in fields:
            register = word >> shift & 31
            if register in rename:
                word = word & ~(31 << shift) | rename[register] << shift
        result[i] = word
    result[2], result[8], result[9] = words[9], words[2], words[8]
    return result


def owner_guards():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-point-batch-transform'
    out.mkdir(exist_ok=True)
    record, words = compile_candidate(root, out, 'guard-source', SELECTED)
    assert (record['body_words'], record['frame'], record['differences']) == (60, 0x98, 17)
    result = normalize(words)
    retail = list(struct.unpack_from('>60I', (root / 'conker/conker.us.bin').read_bytes(), ROM))
    assert result == retail
    raw, functions, rel = parse_object(out / 'guard-source.o')
    assert functions[FUNCTION]['size'] == 240
    assert rel == {0x40: [('R_MIPS_26', 'func_150A8050')], 0xAC: [('R_MIPS_26', 'func_150A7960')]}
    rows = []
    for i, (expected, replacement) in enumerate(zip(words, result)):
        if expected == replacement:
            continue
        assert i * 4 not in rel
        assert struct.unpack_from('>I', raw, i * 4)[0] == expected
        rows.append(dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % (i * 4),
            expected='0x%08X' % expected, replacement='0x%08X' % replacement,
            expected_relocations='-', replacement_relocations='-',
            note='Normalize point-batch closed register cycles and independent saved-register store schedule',
            insert_after='', insert_after_relocations='', omit='false'))
    assert len(rows) == 17
    return rows


def compile_candidate(root, out, name, body=BASELINE, profile='o2g3', extra_flags=()):
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n' + DECLARATIONS + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile], *extra_flags,
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, text=True, capture_output=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'point-batch.ld'
    script.write_text('SECTIONS { .text 0x15145DB4 : SUBALIGN(4) { *(.text) } }\n')
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, functions, rel = parse_object(obj)
    meta = functions[FUNCTION]
    pools = sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, extra_flags=list(extra_flags), body_words=end, frame=frames[0] if frames else 0,
        pool_bytes=len(pools.get('.rodata', (0, b''))[1]), diagnostics=diagnostics, relocations=rel,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--storage', action='store_true')
    parser.add_argument('--reload', action='store_true')
    parser.add_argument('--gate', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-point-batch-transform'
    out.mkdir(exist_ok=True)
    records = []
    if args.gate:
        forms = [(name, body, 'o2g3', ()) for name, body in gate_candidates()]
    elif args.reload:
        forms = [(name, body, 'o2g3', ()) for name, body in reload_candidates()]
        base = dict(storage_candidates())['storage-mask2-first0']
        forms += [('reload-backend-noxbb', base, 'o2g3', ('-Wab,-noxbb',))]
    elif args.storage:
        forms = [(name, body, 'o2g3', ()) for name, body in storage_candidates()]
        base = dict(candidates())['phase1-early1-loop1-arrays0']
        forms += [('profile-' + profile, base, profile, ()) for profile in PROFILES]
        forms += [('backend-' + flag, base, 'o2g3', ('-Wab,-' + flag,)) for flag in
            ('no_branch_target', 'noxbb', 'nobopt', 'noglobal', 'nopeep', 'noswpipe', 'O0', 'O1')]
        forms += [('backend-' + flag, base, 'o2g3', ('-Wc,-' + flag,)) for flag in ('notailopt', 'nooffsetopt')]
    else:
        forms = [(name, body, 'o2g3', ()) for name, body in [('baseline', BASELINE), *candidates()]]
    for name, body, profile, flags in forms:
        record, _ = compile_candidate(root, out, name, body, profile, flags)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
    filename = 'gate-measurements.json' if args.gate else 'reload-measurements.json' if args.reload else 'storage-measurements.json' if args.storage else 'measurements.json'
    (out / filename).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
