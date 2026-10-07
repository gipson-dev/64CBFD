"""Recover the sphere wrapper and its real output-writing dependency, opt-in only."""

import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x151451F0, 0x1726A0, 53
CALLEE, CALLEE_ROM, CALLEE_WORDS = 0x151452C4, 0x172774, 126
DOT, DOT_ROM, DOT_WORDS = 0x15144A74, 0x171F24, 13
FUNCTION, CALLEE_FUNCTION = 'func_151451F0', 'func_151452C4'
PROTOTYPE = '''s32 func_151451F0(struct17 *arg0, struct17 *arg1, struct17 *arg2,
    f32 arg3, f32 arg4, struct17 *arg5, struct17 *arg6, f32 *arg7, f32 *arg8);'''
DECLARATIONS = '''s32 func_151452C4(struct17 *arg0, struct17 *arg1, struct17 *arg2,
    f32 arg3, struct17 *arg4, struct17 *arg5, f32 *arg6, f32 *arg7);
f32 func_15144A74(f32 *arg0, f32 *arg1);
'''
SELECTED = '''s32 func_151451F0(struct17 *arg0, struct17 *arg1, struct17 *arg2,
    f32 arg3, f32 arg4, struct17 *arg5, struct17 *arg6, f32 *arg7, f32 *arg8) {
    if (func_151452C4(arg0, arg1, arg2, arg3, arg5, arg6, arg7, arg8)) {
        if (*arg7 < 0.0f && *arg8 < 0.0f) {
            return 0;
        }
        if (*arg7 >= 0.0f && *arg8 < 0.0f) {
            return 1;
        }
        if (*arg7 < arg4) {
            return 1;
        } else {
            return 0;
        }
    } else {
        return 0;
    }
}'''
CALLEE_BODY = '''s32 func_151452C4(struct17 *arg0, struct17 *arg1, struct17 *arg2,
    f32 arg3, struct17 *arg4, struct17 *arg5, f32 *arg6, f32 *arg7) {
    struct17 direction;
    struct17 origin;
    struct17 relative;
    f32 x;
    f32 y;
    f32 z;
    f32 projection;
    f32 radiusSquared;
    volatile f32 perpendicularSquared;
    f32 root;
    f32 first;
    f32 second;

    x = arg2->unk0 - arg0->unk0;
    y = arg2->unk4 - arg0->unk4;
    z = arg2->unk8 - arg0->unk8;
    direction = *arg1;
    origin = *arg0;
    projection = x * direction.unk0 + y * direction.unk4 + z * direction.unk8;
    radiusSquared = arg3 * arg3;
    perpendicularSquared = x * x + y * y + z * z - projection * projection;
    if (radiusSquared < perpendicularSquared) {
        return 0;
    }
    root = sqrtf(radiusSquared - perpendicularSquared);
    if (projection < root) {
        root = -root;
    }
    first = projection - root;
    second = projection + root;
    arg4->unk0 = first * direction.unk0 + origin.unk0;
    arg4->unk4 = first * direction.unk4 + origin.unk4;
    arg4->unk8 = first * direction.unk8 + origin.unk8;
    *arg6 = first;
    arg5->unk0 = second * direction.unk0 + origin.unk0;
    arg5->unk4 = second * direction.unk4 + origin.unk4;
    arg5->unk8 = second * direction.unk8 + origin.unk8;
    *arg7 = second;
    relative.unk0 = arg4->unk0 - arg0->unk0;
    relative.unk4 = arg4->unk4 - arg0->unk4;
    relative.unk8 = arg4->unk8 - arg0->unk8;
    if (func_15144A74((f32 *)&relative, (f32 *)arg1) < 0.0f) {
        return 0;
    }
    return 1;
}'''


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3', function=FUNCTION):
    source, obj, elf = (output / (name + suffix) for suffix in ('.c', '.o', '.elf'))
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
    entry, rom, count = (ENTRY, ROM, WORDS) if function == FUNCTION else (CALLEE, CALLEE_ROM, CALLEE_WORDS)
    script = output / (name + '.ld')
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
    symbols = {CALLEE_FUNCTION: CALLEE, 'func_15144A74': DOT}
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', function,
        *['--defsym=%s=0x%X' % item for item in symbols.items() if item[0] != function],
        '-o', str(elf), str(obj)], check=True, capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta = functions[function]
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), sections(elf)['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % count, (root / 'conker/conker.us.bin').read_bytes(), rom)
    frame = (-words[0]) & 65535 if words[0] & 0xFFFF0000 == 0x27BD0000 else 0
    return dict(name=name, function=function, profile=profile, body_words=end, frame=frame,
        diagnostics=diagnostics, relocations=relocations, exact=words == list(retail),
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def candidates():
    yield 'selected', SELECTED
    yield 'early-false', SELECTED.replace('    if (func_151452C4', '    if (!func_151452C4').replace(
        'arg7, arg8)) {', 'arg7, arg8)) {\n        return 0;\n    }\n    {').replace(
        '    } else {\n        return 0;\n    }\n}', '    }\n}')
    yield 'cached-first', SELECTED.replace('    if (func_', '    f32 first;\n\n    if (func_', 1).replace(
        'arg7, arg8)) {', 'arg7, arg8)) {\n        first = *arg7;').replace('*arg7 <', 'first <').replace('*arg7 >=', 'first >=')
    yield 'threshold-home', SELECTED.replace('f32 arg3, f32 arg4,', 'f32 arg3, volatile f32 arg4,')
    yield 'first-pointer-home', SELECTED.replace('f32 *arg7, f32 *arg8)', 'f32 *volatile arg7, f32 *volatile arg8)')


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-sphere-wrapper'
    output.mkdir(exist_ok=True)
    records = []
    forms = [(name, body, FUNCTION) for name, body in candidates()]
    forms.append(('callee', CALLEE_BODY, CALLEE_FUNCTION))
    for name, body, function in forms:
        for profile in PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile, function)
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (output / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
