"""Match the pointer-list point transformer using real loop and record views."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x15145CD0, 0x173180, 57
FUNCTION = 'func_15145CD0'
SYMBOLS = dict(func_150A8050=0x150A8050, func_150A7960=0x150A7960)
DECLARATIONS = 'void func_150A7960(f32 matrix[4][4], f32 x, f32 y, f32 z, f32 *outX, f32 *outY, f32 *outZ);\n'
BASELINE = '''void func_15145CD0(u8 *arg0, struct17 **arg1, struct17 **arg2, s32 arg3) {
    f32 mtx[4][4];
    struct17 *src;
    struct17 *dst;

    func_150A8050(mtx, *(f32 *)(arg0 + 0), *(f32 *)(arg0 + 4), *(f32 *)(arg0 + 8));
    mtx[3][0] = *(s16 *)(arg0 + 0x10);
    mtx[3][1] = *(s16 *)(arg0 + 0x12);
    mtx[3][2] = *(s16 *)(arg0 + 0x14);

    while (arg3 > 0) {
        src = *arg1;
        dst = *arg2;
        func_150A7960(mtx, src->unk0, src->unk4, src->unk8, &dst->unk0, &dst->unk4, &dst->unk8);
        arg3--;
        arg1++;
        arg2++;
    }
}'''


def candidates():
    for loop, arrays in itertools.product(range(4), (False, True)):
        body = BASELINE
        if loop == 1:
            body = body.replace('    while (arg3 > 0) {', '    if (arg3 > 0) {\n        do {')
            body = body.replace('        arg2++;\n    }', '        arg2++;\n        } while (arg3 > 0);\n    }')
        elif loop == 2:
            body = body.replace('while (arg3 > 0)', 'for (; arg3 > 0; arg3--, arg1++, arg2++)')
            body = body.replace('        arg3--;\n        arg1++;\n        arg2++;\n', '')
        elif loop == 3:
            body = body.replace('        src = *arg1;\n        dst = *arg2;', '        src = *arg1++;\n        dst = *arg2++;')
            body = body.replace('        arg1++;\n        arg2++;\n', '')
        if arrays:
            body = body.replace('struct17 **arg1, struct17 **arg2', 'f32 **arg1, f32 **arg2')
            body = body.replace('struct17 *src;', 'f32 *src;').replace('struct17 *dst;', 'f32 *dst;')
            for i, field in enumerate(('unk0', 'unk4', 'unk8')):
                body = body.replace('src->' + field, 'src[%d]' % i).replace('&dst->' + field, '&dst[%d]' % i)
        yield 'loop%d-arrays%d' % (loop, arrays), body


def lifetime_candidates():
    for matrix_first, input_first, local_count in itertools.product((False, True), repeat=3):
        cursors = ('    struct17 **input;\n    struct17 **output;\n' if input_first else
            '    struct17 **output;\n    struct17 **input;\n')
        declarations = '    f32 mtx[4][4];\n' + cursors if matrix_first else cursors + '    f32 mtx[4][4];\n'
        if local_count:
            declarations += '    s32 remaining;\n'
        body = BASELINE.replace('    f32 mtx[4][4];\n', declarations)
        loop = body.index('    while (arg3 > 0)')
        body = body[:loop] + body[loop:].replace('arg1', 'input').replace('arg2', 'output')
        body = body[:loop] + '    input = arg1;\n    output = arg2;\n' + body[loop:]
        if local_count:
            body = body.replace('    while (arg3 > 0)', '    remaining = arg3;\n    while (remaining > 0)')
            body = body.replace('        arg3--;', '        remaining--;')
        yield 'lifetime-matrix%d-input%d-count%d' % (matrix_first, input_first, local_count), body


def readback_candidates():
    cursor_body = dict(lifetime_candidates())['lifetime-matrix1-input1-count0']
    for mask, early_output in itertools.product(range(4), (False, True)):
        body = cursor_body
        if mask & 1:
            body = body.replace('struct17 **arg1', 'struct17 ** volatile arg1')
        if mask & 2:
            body = body.replace('struct17 **arg2', 'struct17 ** volatile arg2')
        if early_output:
            body = body.replace('    output = arg2;\n', '')
            body = body.replace('    mtx[3][0]', '    output = arg2;\n    mtx[3][0]', 1)
        yield 'readback%d-early-output%d' % (mask, early_output), body


def compile_candidate(root, out, name, body=BASELINE, profile='o2g3'):
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n' + DECLARATIONS + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, text=True, capture_output=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'point-list.ld'
    script.write_text('SECTIONS { .text 0x15145CD0 : SUBALIGN(4) { *(.text) } }\n')
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
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        pool_bytes=len(pools.get('.rodata', (0, b''))[1]), diagnostics=diagnostics, relocations=rel,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-point-list-transform'
    out.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in PROFILES:
            record, _ = compile_candidate(root, out, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    for name, body in lifetime_candidates():
        record, _ = compile_candidate(root, out, name, body)
        records.append(record)
        print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    for name, body in readback_candidates():
        record, _ = compile_candidate(root, out, name, body)
        records.append(record)
        print(record['name'], record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
