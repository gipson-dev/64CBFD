"""Recover the lighting descriptor's actor/global/position dispatch and nine-word ABI."""

import argparse
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = 0x151462C8, 0x173778, 124
FUNCTION = 'func_151462C8'
SYMBOLS = dict(func_1515E544=0x1515E544, func_1515D914=0x1515D914,
    D_800BE9C0=0x800BE9C0, D_800D9E10=0x800D9E10, D_800D9BD0=0x800D9BD0,
    D_800D9E20=0x800D9E20, D_800D9E21=0x800D9E21)
LAYOUT = '''typedef struct {
    s32 capacity;
    u8 count;
    u8 pad5[3];
    u8 *lights[4];
    u8 *ambient;
    s32 channels;
} GameLightingDescriptor;
'''
DECLARATIONS = LAYOUT + '''extern u8 D_800D9E21;
Gfx *func_1515E544(Gfx *, s32, u8, u8, u8 *);
Gfx *func_1515D914(Gfx *, s32, s32, s32, s32, s32, u8 *, s32,
    u8 *, u8 *, s32, u8 *, s32, u8 **);
'''
PROTOTYPE = '''Gfx *func_151462C8(Gfx *commands, GameLightingDescriptor *descriptor,
    u8 mode, u8 *actor, u8 slot, s16 index, struct17 *position, u8 flags, s32 extra);'''
SELECTED = '''Gfx *func_151462C8(Gfx *commands, GameLightingDescriptor *descriptor,
    u8 mode, u8 *actor, u8 slot, s16 index, struct17 *position, u8 flags, s32 extra) {
    u8 *lights = descriptor->lights[index];
    u8 *ambient;
    u32 selected;
    s32 direction;
    s32 environment;

    if (lights != 0 && (ambient = descriptor->ambient) != 0) {
        selected = mode;
        if (mode == 1U) {
            if (actor != 0) {
                if (*(s32 *)actor == 0 || actor[0x3B] != slot || actor[4] == 255 || actor[0x302] == 0) {
                    selected = 2;
                }
            } else {
                selected = 0;
            }
        }
        switch (selected) {
        case 1:
            commands = func_1515E544(commands, ((s32 *)(actor + 0x304))[index],
                actor[0x301], actor[0x302], *(u8 **)(actor + 0x314));
            break;
        case 2:
            commands = func_1515E544(commands, D_800D9E10[index], D_800D9E20,
                D_800D9E21, D_800D9BD0[index][D_800BE9C0]);
            break;
        case 0:
        default:
            if (flags & 1) {
                direction = 2;
            } else {
                direction = 0;
            }
            if (flags & 2) {
                environment = 16;
            } else {
                environment = 0;
            }
            commands = func_1515D914(commands, index, (s32)position->unk0,
                (s32)position->unk4, (s32)position->unk8, extra, lights, descriptor->capacity,
                ambient, &descriptor->count, descriptor->channels, 0, environment | 8 | direction, 0);
            break;
        }
    }
    return commands;
}'''
BASELINE = '''Gfx *func_151462C8(Gfx *commands, GameLightingDescriptor *descriptor,
    u8 mode, u8 *actor, u8 slot, s16 index, struct17 *position, u8 flags, s32 extra) {
    u8 *lights = descriptor->lights[index];
    u8 *ambient = descriptor->ambient;
    s32 selected = mode;
    s32 direction;
    s32 environment;

    if (lights == 0 || ambient == 0) {
        return commands;
    }
    if (mode == 1) {
        if (actor == 0) {
            selected = 0;
        } else if (*(s32 *)actor == 0 || actor[0x3B] != slot || actor[4] == 255 || actor[0x302] == 0) {
            selected = 2;
        }
    }
    switch (selected) {
    case 1:
        commands = func_1515E544(commands, ((s32 *)(actor + 0x304))[index],
            actor[0x301], actor[0x302], *(u8 **)(actor + 0x314));
        break;
    case 2:
        commands = func_1515E544(commands, D_800D9E10[index], D_800D9E20,
            D_800D9E21, D_800D9BD0[index][D_800BE9C0]);
        break;
    default:
        direction = 0;
        if (flags & 1) {
            direction = 2;
        }
        if (flags & 2) {
            environment = 16;
        } else {
            environment = 0;
        }
        commands = func_1515D914(commands, index, (s32)position->unk0,
            (s32)position->unk4, (s32)position->unk8, extra, lights, descriptor->capacity,
            ambient, &descriptor->count, descriptor->channels, 0, environment | 8 | direction, 0);
        break;
    }
    return commands;
}'''


def candidates():
    for mode_type, lazy_ambient, condition, returns in itertools.product(('s32', 'u8'), (False, True), range(3), (False, True)):
        body = BASELINE.replace('s32 selected = mode;', mode_type + ' selected = mode;')
        if lazy_ambient:
            body = body.replace('u8 *ambient = descriptor->ambient;', 'u8 *ambient;')
            body = body.replace('lights == 0 || ambient == 0', 'lights == 0 || (ambient = descriptor->ambient) == 0')
        if condition == 1:
            body = body.replace('*(s32 *)actor == 0 || actor[0x3B] != slot || actor[4] == 255 || actor[0x302] == 0',
                '!(*(s32 *)actor != 0 && actor[0x3B] == slot && actor[4] != 255 && actor[0x302] != 0)')
        if condition == 2:
            body = body.replace('if (actor == 0) {\n            selected = 0;\n        } else if',
                'if (actor != 0) {\n            if').replace('            selected = 2;\n        }',
                '                selected = 2;\n            }\n        } else {\n            selected = 0;\n        }')
        if returns:
            body = body.replace('        commands = func_', '        return func_').replace('        break;\n', '')
        yield 'mode%s-lazy%d-condition%d-returns%d' % (mode_type, lazy_ambient, condition, returns), body


def lifetime_candidates():
    forms = dict(candidates())
    for selected, zero_case, gates, condition, flags in itertools.product(range(3), (False, True), (False, True), range(3), (False, True)):
        body = forms['modeu8-lazy1-condition%d-returns0' % condition]
        if selected == 1:
            body = body.replace('u8 selected = mode;', 'u8 selected;')
            body = body.replace('    if (mode == 1)', '    selected = mode;\n    if (mode == 1)', 1)
        elif selected == 2:
            body = body.replace('    u8 selected = mode;\n', '').replace('selected', 'mode')
        if zero_case:
            body = body.replace('    default:\n', '    case 0:\n    default:\n')
        if gates:
            body = body.replace('if (lights == 0 || (ambient = descriptor->ambient) == 0) {\n        return commands;\n    }',
                'if (lights == 0) {\n        return commands;\n    }\n    ambient = descriptor->ambient;\n    if (ambient == 0) {\n        return commands;\n    }')
        if flags:
            body = body.replace('        direction = 0;\n        if (flags & 1) {\n            direction = 2;\n        }',
                '        if (flags & 1) {\n            direction = 2;\n        } else {\n            direction = 0;\n        }')
        yield 'lifetime-selected%d-zero%d-gates%d-condition%d-flags%d' % (selected, zero_case, gates, condition, flags), body


def dispatch_candidates():
    forms = dict(lifetime_candidates())
    for mode_type, selected, gates, flags in itertools.product(('s32', 'u8'), (False, True), (False, True), (False, True)):
        body = forms['lifetime-selected1-zero1-gates%d-condition2-flags%d' % (gates, flags)]
        body = body.replace('u8 selected;', mode_type + ' selected;')
        if selected:
            body = body.replace('    selected = mode;\n    if (mode == 1)', '    if (mode == 1)', 1)
            body = body.replace('            if (*(s32 *)actor', '            selected = 1;\n            if (*(s32 *)actor', 1)
            body = body.replace('            selected = 0;\n        }\n    }',
                '            selected = 0;\n        }\n    } else {\n        selected = mode;\n    }', 1)
        yield 'dispatch-type%s-branches%d-gates%d-flags%d' % (mode_type, selected, gates, flags), body


def guard_candidates():
    forms = dict(lifetime_candidates())
    for mode_type, condition, flags, zero_case, assigned in itertools.product(('s32', 'u8'), (0, 2),
            (False, True), (False, True), (False, True)):
        body = forms['lifetime-selected1-zero%d-gates0-condition%d-flags%d' % (zero_case, condition, flags)]
        body = body.replace('u8 selected;', mode_type + ' selected;')
        body = body.replace('    if (lights == 0 || (ambient = descriptor->ambient) == 0) {\n        return commands;\n    }',
            '    if (lights != 0 && (ambient = descriptor->ambient) != 0) {')
        body = body.replace('    return commands;\n}', '    }\n    return commands;\n}', 1)
        if assigned:
            body = body.replace('u8 *lights = descriptor->lights[index];', 'u8 *lights;')
            body = body.replace('if (lights != 0 &&', 'if ((lights = descriptor->lights[index]) != 0 &&', 1)
        yield 'guard-type%s-condition%d-flags%d-zero%d-assigned%d' % (mode_type, condition, flags, zero_case, assigned), body


def shape_candidates():
    forms = dict(guard_candidates())
    for mode_type, initialization, index_type, flags in itertools.product(
            ('s32', 'u32', 'u8'), range(3), ('formal', 's32', 's16', 'u16'), (False, True)):
        body = forms['guard-types32-condition2-flags%d-zero1-assigned0' % flags]
        body = body.replace('s32 selected;', mode_type + ' selected;')
        if initialization == 1:
            body = body.replace(mode_type + ' selected;', mode_type + ' selected = mode;')
            body = body.replace('    selected = mode;\n', '', 1)
        elif initialization == 2:
            body = body.replace('    ' + mode_type + ' selected;\n', '')
            body = body.replace('    selected = mode;', '    ' + mode_type + ' selected = mode;', 1)
        if index_type != 'formal':
            body = body.replace('    case 0:\n    default:\n',
                '    case 0:\n    default: {\n        ' + index_type + ' position_index = index;\n')
            body = body.replace('func_1515D914(commands, index,', 'func_1515D914(commands, position_index,')
            body = body.replace('        break;\n    }\n    }', '        break;\n    }\n    }\n    }', 1)
        yield 'shape-type%s-init%d-index%s-flags%d' % (mode_type, initialization, index_type, flags), body


def sharing_candidates():
    base = dict(shape_candidates())['shape-typeu32-init0-indexformal-flags1']
    for condition, switch, flag_type in itertools.product(range(4), range(2), ('formal', 'u32', 's32')):
        body = base
        body = body.replace('if (mode == 1)', ('if (mode == 1)', 'if ((u32)mode == 1)',
            'if (mode == 1U)', 'if (selected == 1)')[condition], 1)
        if switch:
            body = body.replace('switch (selected)', 'switch ((s32)selected)')
        if flag_type != 'formal':
            body = body.replace('    case 0:\n    default:\n',
                '    case 0:\n    default: {\n        ' + flag_type + ' position_flags = flags;\n')
            body = body.replace('flags &', 'position_flags &')
            body = body.replace('        break;\n    }\n    }', '        break;\n    }\n    }\n    }', 1)
        yield 'sharing-condition%d-switch%d-flags%s' % (condition, switch, flag_type), body


def normalize(words):
    assert len(words) == WORDS
    assert words[0x138 // 4:0x140 // 4] == [0x00004025, 0x87A5005E]
    result = list(words)
    result[0x138 // 4:0x140 // 4] = [0x87A5005E, 0x00004025]
    return result


def owner_guards():
    return [dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % offset,
        expected='0x%08X' % expected, replacement='0x%08X' % replacement,
        expected_relocations='-', replacement_relocations='-',
        note='Normalize independent lighting-dispatch index load and temporary initialization schedule',
        insert_after='', insert_after_relocations='', omit='false')
        for offset, expected, replacement in ((0x138, 0x00004025, 0x87A5005E),
                                             (0x13C, 0x87A5005E, 0x00004025))]


def compile_candidate(root, out, name, body=BASELINE, profile='o2g3', entry=ENTRY, symbols=None):
    out.mkdir(exist_ok=True)
    source, obj, elf = (out / (name + suffix) for suffix in ('.c', '.o', '.elf'))
    source.write_text('#include <ultra64.h>\n#include "functions.h"\n#include "variables.h"\n' + DECLARATIONS + body + '\n')
    result = subprocess.run(['ido/ido5.3_recomp/cc', '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
        '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32',
        '-I', 'conker/include', '-I', 'conker/include/2.0L', '-I', 'conker/include/2.0L/PR',
        '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32', *PROFILES[profile],
        '-o', str(obj.relative_to(root)), str(source.relative_to(root))], cwd=root, text=True, capture_output=True)
    diagnostics = result.stdout + result.stderr
    if result.returncode or diagnostics:
        raise ValueError(diagnostics)
    script = out / 'lighting.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in (symbols or SYMBOLS).items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocations = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size'] // 4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word) & 65535 for word in words if word & 0xFFFF0000 == 0x27BD0000 and word & 0x8000]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        pool_bytes=len(pools.get('.rodata', (0, b''))[1]), diagnostics=diagnostics, relocations=relocations,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0))), words


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profiles', action='store_true')
    parser.add_argument('--lifetime', action='store_true')
    parser.add_argument('--dispatch', action='store_true')
    parser.add_argument('--guard', action='store_true')
    parser.add_argument('--shape', action='store_true')
    parser.add_argument('--sharing', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-lighting-dispatch'
    out.mkdir(exist_ok=True)
    forms = [('profile-' + p, BASELINE, p) for p in PROFILES] if args.profiles else [(n, b, 'o2g3') for n, b in
        (sharing_candidates() if args.sharing else shape_candidates() if args.shape else guard_candidates() if args.guard else dispatch_candidates() if args.dispatch else lifetime_candidates() if args.lifetime else candidates())]
    records = []
    for name, body, profile in forms:
        record, _ = compile_candidate(root, out, name, body, profile)
        records.append(record)
        print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
    (out / ('profiles.json' if args.profiles else 'sharing.json' if args.sharing else 'shape.json' if args.shape else 'guard.json' if args.guard else 'dispatch.json' if args.dispatch else 'lifetime.json' if args.lifetime else 'measurements.json')).write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
