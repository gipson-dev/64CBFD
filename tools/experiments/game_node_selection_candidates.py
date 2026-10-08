"""Recover the complete attachment-selection dispatcher without installing it."""

import argparse
import hashlib
import itertools
import json
import struct
import subprocess
from pathlib import Path

from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.pad_generated_object import parse_object
from tools.tests.game_owner_pool import normalized_pools

ENTRY, ROM, WORDS = 0x15031FC8, 0x5F478, 1148
FUNCTION, TABLE = 'func_15031FC8', 0x800970E0
STUB = 's32 func_15031FC8() {\n    return 0;\n}'
SYMBOLS = {'func_1503F5B8': 0x1503F5B8, 'func_1505E060': 0x1505E060,
    'D_800902D0': 0x800902D0, 'D_800902D4': 0x800902D4}
DECLARATIONS = '''void func_1503F5B8(u8 *, s32, s32, f32, f32, s32);
void func_1505E060(u8 *);
extern s32 D_800902D0;
extern s32 D_800902D4;'''
MODEL_CHOICES = ((0x6, 7), (0x26, 15), (0x27, 15), (0x1, 3), (0x2A, 3),
    (0x0, 5), (0x3, 6), (0x7, 2), (0xA, 4), (0xF, 8), (0x1E, 8),
    (0x13, 13), (0x4, 9), (0x5, 10), (0x10, 11), (0x8, 16),
    (0x14, 14), (0x15, 14), (0x50, 19), (0x51, 20))
JOINT_CHOICES = ((0x14, 3), (0x15, 4), (0x16, 5), (0x17, 6), (0x18, 7),
    (0x1A, 8), (0x1B, 9), (0x1C, 10), (0x1D, 11), (0x1E, 12), (0x1F, 13),
    (0x20, 14), (0x21, 15), (0x22, 16), (0x23, 17))
# Ordered semantic case/value pairs, including retail's distinct equal-value cases.
BROAD_CHOICES = (
    (0xB9, 1), (0xAE, 2), (0xDA, 3), (0x104, 4), (0x107, 5), (0x10B, 6),
    (0x11E, 7), (0x11F, 8), (0x134, 9), (0x135, 10), (0x136, 11),
    (0x13B, 13), (0x13C, 14), (0x145, 15), (0x146, 16), (0x141, 17),
    (0x147, 18), (0x14B, 22), (0x14A, 21), (0x149, 20), (0x148, 19), (0x151, 24),
    (0x17F, 26), (0x180, 27), (0x181, 28), (0x182, 29), (0x186, 30),
    (0x187, 31), (0x189, 32), (0x18C, 33), (0x18D, 34), (0x18E, 35),
    (0x1A0, 36), (0x1A3, 37), (0x1B3, 38), (0x1B4, 39), (0x1B5, 40),
    (0x1B6, 41), (0x1B7, 42), (0x1B8, 43), (0x1BD, 44), (0x1BE, 45),
    (0x1BF, 46), (0x1C0, 47), (0x1C1, 48), (0x1C2, 49), (0x1C3, 50),
    (0x1C4, 51), (0x1C5, 52), (0x1C6, 53), (0x1C7, 54), (0x1C8, 55),
    (0x1C9, 56), (0x1CA, 57), (0x1D1, 58), (0x1D2, 59), (0x1D3, 60),
    (0x1D5, 61), (0x1D9, 62), (0x1DA, 63), (0x1DB, 64), (0x1E3, 65),
    (0x1E4, 66), (0x1E5, 67), (0x1E6, 68), (0x1E7, 69), (0x1E8, 71),
    (0x1E9, 68), (0x1F0, 72), (0x1F1, 73), (0x1F2, 74), (0x201, 75),
    (0x202, 77), (0x203, 78), (0x204, 79), (0x200, 80), (0x205, 81),
    (0x208, 82), (0x209, 83), (0x20A, 84), (0x20B, 85), (0x20C, 86),
    (0x211, 87), (0x212, 88), (0x216, 89), (0x217, 90), (0x218, 91),
    (0x219, 92), (0x21A, 93), (0x21B, 94), (0xA8, 95), (0x1FD, 76),
    (0x228, 98), (0x22E, 99), (0x22F, 100), (0x232, 97), (0x220, 96),
    (0x23A, 101), (0x23B, 102), (0x24D, 110), (0x21C, 111), (0x241, 112),
    (0x23C, 103), (0x24B, 109), (0x24A, 108), (0x249, 107), (0x248, 106),
    (0x246, 105), (0x245, 104), (0x25C, 113), (0x25D, 114), (0x25E, 115),
    (0x260, 116), (0x266, 119), (0x267, 120), (0x268, 121), (0x26A, 122),
    (0x26B, 123), (0x26C, 124), (0x26D, 125), (0x275, 126), (0x1D6, 127),
    (0x1D7, 134), (0x1D8, 133), (0x276, 128), (0x277, 129), (0x278, 130),
    (0x265, 118), (0x27F, 131), (0x280, 132), (0x281, 135), (0x282, 136),
    (0x290, 137), (0x291, 138), (0x292, 139), (0x293, 140), (0x294, 141),
    (0x295, 142), (0x298, 143), (0x29A, 144), (0x29B, 145), (0x29C, 146),
    (0x29D, 147), (0x2A9, 148), (0x2AA, 149), (0x2AC, 150), (0x2AD, 151),
    (0x2AE, 152), (0x2AF, 153), (0x2B0, 154), (0x2B2, 155), (0x2B3, 156),
    (0x2B4, 157), (0x2B5, 158), (0x2B6, 159), (0x2B8, 160), (0x2B9, 161),
    (0x2BA, 162), (0x2BB, 163), (0x2BC, 164), (0x2BD, 165), (0x2BE, 166),
    (0x2BF, 167), (0x2C0, 168), (0x2C1, 169), (0x2C4, 170), (0x2CF, 171),
    (0x2DA, 172), (0x2DB, 173), (0x2DD, 174), (0x2DC, 175), (0x2D9, 176),
    (0x2DF, 177), (0x2E0, 178), (0x2E1, 179), (0x2E2, 180), (0x2E3, 181),
    (0x2EC, 182), (0x2ED, 183), (0x2EE, 184), (0x2EF, 185), (0x2F0, 186),
    (0x2F1, 187), (0x2F8, 188), (0x2F9, 189), (0x301, 190), (0x304, 191),
    (0x305, 192), (0x306, 193), (0x307, 194), (0x308, 195), (0x309, 196),
    (0x30A, 197), (0x30B, 198), (0x30C, 199), (0x30D, 200), (0x30E, 201),
    (0x30F, 202), (0x314, 203), (0x315, 204), (0x316, 205), (0x317, 206),
    (0x318, 207), (0x319, 208), (0x31C, 209), (0x31D, 210), (0x31E, 211),
    (0x320, 212), (0x31F, 213), (0x321, 214), (0x322, 215), (0x323, 216),
    (0x324, 217), (0x326, 218), (0x327, 219), (0x328, 220), (0x32B, 221),
    (0x32C, 222), (0x32D, 223), (0x32E, 224), (0x32F, 225), (0x330, 226),
    (0x331, 227), (0x332, 228), (0x333, 229), (0x334, 230), (0x335, 231),
    (0x345, 232), (0x347, 234), (0x348, 235), (0x349, 236), (0x34A, 237),
    (0x34B, 238), (0x34C, 239), (0x34D, 240), (0x240, 233))


def choice_cases(pairs, indent):
    result = []
    for index, (key, value) in enumerate(pairs):
        shared = pairs is MODEL_CHOICES and index+1 < len(pairs) and value in (3, 8, 15) and pairs[index+1][1] == value
        result.append('%scase 0x%X:%s' % (indent, key, '' if shared else ' choice = 0x%X; break;' % value))
    return '\n'.join(result)


SELECTED = '''s32 func_15031FC8(u8 *node, u8 *actor) {
    u8 *source;
    u8 *attachment;
    u8 *initial;
    s32 choice;
    s32 copy_state;
    s32 old_flags;
    s32 model;
    s32 type;
    f32 limit;

    source = *(u8 **)(actor + 0x2D0);
    initial = *(u8 **)(node + 0x48);
    choice = -1;
    copy_state = 1;
    if (initial == 0) {
        return 0;
    }
    old_flags = *(u16 *)(initial + 4) & ~0x8000;
    model = actor[4];
    type = *(u16 *)(actor + 0x84);
    switch (model) {
        case 0x58:
            if (node[1] == 0x9B) {
                node[2] = 0x12;
            }
            switch (type) {
                case 0x27: choice = 3; break;
                case 0x28: choice = 4; break;
                case 2: choice = 1; break;
                case 3: choice = 0; break;
                default:
                    choice = 0;
                    if (node[1] == 0x9B) {
                        choice = 3;
                    }
                    break;
            }
            break;
        case 0x5B:
            choice = 0;
            break;
        case 0x5A:
        case 0x74:
        case 0x7A:
            if (*(s32 *)(actor + 0x2E8) != 0) {
                *(s16 *)(node + 0x18) = D_800902D4;
            } else {
                *(s16 *)(node + 0x18) = D_800902D0;
            }
            switch (type) {
@MODEL@
                default: choice = 6; break;
            }
            break;
        default:
            switch (node[1]) {
                case 0x9E:
                    node[2] = 9;
                    *(u16 *)(node + 0x1E) = 0x41;
                    *(u16 *)(node + 0x20) = 1;
                    switch (type) {
                        case 0x1D6: choice = 1; break;
                        case 0x1D7: choice = 2; node[2] = 0x13; break;
                        case 0x257: choice = 4; node[2] = 0x13; break;
                        case 0x275: choice = 5; node[2] = 0x13; break;
                        case 0x1D8: choice = 3; break;
                    }
                    copy_state = 0;
                    if (node[2] == 0x13) {
                        *(u16 *)(node + 0x1E) = 0;
                    }
                    break;
                case 0x9B:
                    choice = 0;
                    if (actor[5] == 5) {
                        node[2] = 0;
                    } else if (model == 0x8B) {
                        node[2] = 6;
                        switch (type) {
                            case 0xC: choice = 6; break;
                            case 0x13: choice = 7; break;
                        }
                    } else {
                        node[2] = 9;
                        switch (type) {
                            case 0x22E: choice = 5; break;
                            case 0x1B7: choice = 1; break;
                            case 0x1B8: choice = 2; break;
                        }
                    }
                    break;
                case 0x9F:
                    choice = 0;
                    if (actor[5] == 5) {
                        node[2] = 0;
                    } else if (model == 0xB5) {
                        node[2] = 0x12;
                        switch (type) {
                            case 0x34: choice = 1; break;
                            case 0x35: choice = 2; break;
                            case 0x36: choice = 3; break;
                            case 0x37: choice = 4; break;
                        }
                    } else {
                        node[2] = 9;
                    }
                    break;
                case 0x9C:
                    choice = 8;
                    break;
                case 0x9D:
                    choice = 0;
                    if (actor[5] == 5) {
                        node[2] = 0;
                    } else if (model == 0x8B) {
                        node[2] = 6;
                        switch (type) {
                            case 0x13:
                            case 0x20: choice = 4; break;
                            case 0x22: choice = 3; break;
                        }
                    } else {
                        node[2] = 9;
                        switch (type) {
                            case 0x21C: choice = 1; break;
                            case 0x241: choice = 2; break;
                        }
                    }
                    break;
                case 0x9A:
                    switch (model) {
                        case 0x87:
                            node[2] = 0x12;
                            switch (type) {
                                case 1: choice = 1; break;
                                case 5: choice = 2; break;
                                default: choice = 0; break;
                            }
                            break;
                        case 0x99:
                            node[2] = 0x15;
                            switch (type) {
@JOINT@
                                default: choice = 0; break;
                            }
                            break;
                    }
                    break;
                case 0x8D:
                    switch (type) {
                        case 0x323: choice = 1; break;
                        case 0x324: choice = 2; break;
                        default: choice = 0; break;
                    }
                    break;
                case 0x8E:
                    switch (type) {
                        case 0xB4: choice = 0; break;
                        case 0xB6: choice = 1; break;
                        case 0xB5: choice = 2; break;
                        case 0xDD: choice = 3; break;
                        case 0xDE: choice = 3; break;
                        default: return 1;
                    }
                    break;
                case 0x8F:
                case 0x90:
                    switch (type) {
@BROAD@
                        default: choice = 0; break;
                    }
                    break;
                case 0x83:
                    switch (type) {
                        case 0x5E: choice = 0; break;
                        case 0x5F:
                        case 0xFA: choice = 1; break;
                        case 0x60: choice = 2; break;
                        case 0xB3: choice = 3; break;
                        default: return 1;
                    }
                    break;
                case 0x85:
                    switch (type) {
                        case 0x13E: choice = 5; break;
                        case 0x13F: choice = 4; break;
                        case 0x7C: choice = 2; break;
                        default: choice = 0.0f < *(f32 *)(actor + 0x3C) ? 1 : 0; break;
                    }
                    break;
                case 0x88:
                    switch (type) {
                        case 0x11: choice = 0; break;
                        case 0x26: choice = 1; break;
                        default: choice = 2; break;
                    }
                    break;
                case 0x98:
                    if (model == 0x8B) {
                        choice = 5;
                        node[2] = 6;
                    } else {
                        switch (type) {
                            case 0x12C: choice = 0; break;
                            case 0x12D: choice = 3; break;
                            case 0x142: choice = 4; break;
                            case 0x12E:
                            case 0x358: choice = 2; break;
                            case 0x2AA: choice = 6; break;
                            default: return 1;
                        }
                    }
                    break;
                case 0x87:
                    switch (type) {
                        case 0x172: choice = 0; break;
                        case 0x174: choice = 2; break;
                        case 0x17A: choice = 3; break;
                        case 0x171:
                        case 0x173: choice = 1; break;
                        default: return 1;
                    }
                    break;
                case 0x89:
                    if (actor[5] == 5) {
                        choice = 3;
                        node[2] = 0;
                    } else {
                        switch (type) {
                            case 0x49: choice = 0; node[2] = 9; break;
                            case 0x47: choice = 1; node[2] = 9; break;
                            case 0x81: choice = 2; node[2] = 0x13; break;
                            default: return 1;
                        }
                    }
                    break;
                case 0x91:
                    if (actor[5] == 5) {
                        node[2] = 0;
                        choice = *(f32 *)(actor + 0x24) == 0.0f ? 3 : 0;
                    } else {
                        node[2] = 0xE;
                        switch (type) {
                            case 0x12: choice = 2; break;
                            case 0x10: choice = 1; break;
                            default: choice = 4; break;
                        }
                    }
                    break;
            }
            break;
    }
    if (choice != -1) {
        func_1503F5B8(*(u8 **)(node + 0x48), 0, choice, 0.0f, 0.0f, 1);
    }
    if (source != 0) {
        attachment = *(u8 **)(node + 0x48);
        if (choice == old_flags && *(s16 *)(source + 0x3C) == 0x3FF) {
            func_1505E060(attachment);
            attachment = *(u8 **)(node + 0x48);
        }
        *(f32 *)(attachment + 8) = *(f32 *)(source + 8);
        attachment = *(u8 **)(node + 0x48);
        if (copy_state != 0) {
            if (*(s8 *)(attachment + 0x39) != 0 || attachment[0x215] == 0) {
                *(s16 *)(attachment + 0x3A) = *(s16 *)(source + 0x3A);
                *(s16 *)(*(u8 **)(node + 0x48) + 0x3C) = *(s16 *)(source + 0x3C);
                attachment = *(u8 **)(node + 0x48);
            }
        }
        limit = *(f32 *)(attachment + 0x18) - 1.0f;
        if (limit <= *(f32 *)(attachment + 8)) {
            *(f32 *)(attachment + 8) = limit;
        }
    }
    return 0;
}'''.replace('@MODEL@', choice_cases(MODEL_CHOICES, '                ')).replace(
    '@JOINT@', choice_cases(JOINT_CHOICES, '                                ')).replace(
    '@BROAD@', choice_cases(BROAD_CHOICES, '                        '))


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
    script = out / 'node-selection.ld'
    script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } '
        '.rodata 0x%X : SUBALIGN(4) { *(.rodata) } }\n' % (ENTRY, TABLE))
    subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', FUNCTION,
        *['--defsym=%s=0x%X' % item for item in SYMBOLS.items()], '-o', str(elf), str(obj)],
        check=True, capture_output=True)
    _, functions, relocs = parse_object(obj)
    meta, pools = functions[FUNCTION], sections(elf)
    words = list(struct.unpack_from('>%dI' % (meta['size']//4), pools['.text'][1], meta['value']))
    end = max(i for i, word in enumerate(words) if word == 0x03E00008)+2
    assert not any(words[end:])
    words = words[:end]
    retail = struct.unpack_from('>%dI' % WORDS, (root / 'conker/conker.us.bin').read_bytes(), ROM)
    frames = [(-word)&65535 for word in words if word&0xFFFF0000 == 0x27BD0000 and word&0x8000]
    pool = pools.get('.rodata', (TABLE, b''))[1]
    return dict(name=name, profile=profile, body_words=end, frame=frames[0] if frames else 0,
        differences=sum(a != b for a, b in itertools.zip_longest(words, retail, fillvalue=0)),
        diagnostics='', relocations=relocs, pool_bytes=len(pool)), words, pool


def candidates():
    yield 'shared-initial-pointer', SELECTED.replace('    u8 *initial;\n', '').replace('initial', 'attachment')
    yield 'literal-low-mask', SELECTED.replace('& ~0x8000', '& 0x7FFF')
    yield 'register-locals', SELECTED.replace('    s32 ', '    register s32 ').replace('    u8 *', '    register u8 *')
    yield 'negative-missing-choice', SELECTED.replace('case 0x34D: choice = 0xF0;', 'case 0x34D: choice = 0xEF;')
    yield 'negative-always-copy-state', SELECTED.replace('                    copy_state = 0;', '                    copy_state = 1;')
    yield 'negative-skip-reset', SELECTED.replace('choice == old_flags &&', 'choice != old_flags &&')
    yield 'negative-strict-clamp', SELECTED.replace('if (limit <=', 'if (limit <')
    yield 'negative-no-postsetup-reload', SELECTED.replace('attachment = *(u8 **)(node + 0x48);\n        if (choice',
        'attachment = initial;\n        if (choice')


def measure_owner(root, out):
    original = (root / 'conker/src/game/generated_5D2C0.c').read_text()
    assert original.count(STUB) == 1
    candidate = original.replace(STUB, SELECTED).replace('extern f32 D_800970DC;',
        'extern f32 D_800970DC;\n'+DECLARATIONS)
    old, warnings = compile_owner(root, out, original, 'owner-stub')
    assert not warnings
    new, warnings = compile_owner(root, out, candidate, 'owner-candidate')
    assert not warnings
    old_text, old_functions, old_relocs = parse_object(old)
    text, functions, relocs = parse_object(new)
    assert functions.keys() == old_functions.keys()
    for name, current in functions.items():
        if name == FUNCTION:
            continue
        previous = old_functions[name]
        assert text[current['value']:current['value']+current['size']] == old_text[
            previous['value']:previous['value']+previous['size']], name
        assert {o-current['value']:r for o,r in relocs.items() if current['value'] <= o < current['value']+current['size']} == {
            o-previous['value']:r for o,r in old_relocs.items() if previous['value'] <= o < previous['value']+previous['size']}, name
    old_pool, new_pool = normalized_pools(old), normalized_pools(new)
    target = functions[FUNCTION]
    compile_candidate(root, out, 'owner-isolated')
    isolated_text, isolated_funcs, isolated_relocs = parse_object(out / 'owner-isolated.o')
    size = isolated_funcs[FUNCTION]['size']
    target_relocs = {o-target['value']:r for o,r in relocs.items() if target['value'] <= o < target['value']+target['size']}
    table_loads = []
    for offset, items in target_relocs.items():
        if items == [('R_MIPS_LO16', '.rodata')]:
            table_loads.append(dict(text_offset=offset, pool_addend=struct.unpack_from('>I', text, target['value']+offset)[0]&65535))
    assert target_relocs == isolated_relocs
    expected = bytearray(isolated_text[:size])
    for table in table_loads:
        offset = table['text_offset']
        word = struct.unpack_from('>I', expected, offset)[0]
        assert table['pool_addend'] == (word&65535)+412
        struct.pack_into('>I', expected, offset, word+412)
    assert bytes(expected) == text[target['value']:target['value']+target['size']]
    isolated_pool = normalized_pools(out / 'owner-isolated.o')['.rodata']
    assert tuple((location-412, name, offset) for location,name,offset in new_pool['.rodata'][1] if location >= 412) == isolated_pool[1]
    return dict(functions=len(functions), neighbors_unchanged=len(functions)-1, strict_diagnostics=0,
        isolated_object_bytes=size, owner_object_bytes=target['size'],
        isolated_text_equals_owner=text[target['value']:target['value']+target['size']] == isolated_text[:size],
        isolated_text_differs_only_seven_checked_pool_addends=True, target_pool_identities_match_isolated=True,
        old_pool_bytes=len(sections(old).get('.rodata', (0,b''))[1]),
        new_pool_bytes=len(sections(new).get('.rodata', (0,b''))[1]),
        old_pool_identities=old_pool['.rodata'][1], new_pool_identities=new_pool['.rodata'][1],
        old_useful_pool_preserved=old_pool['.rodata'][0][:412] == new_pool['.rodata'][0][:412] and
            old_pool['.rodata'][1] == tuple(i for i in new_pool['.rodata'][1] if i[0] < 412),
        old_raw_pool_sha256=hashlib.sha256(old_pool['.rodata'][0]).hexdigest(),
        new_raw_pool_sha256=hashlib.sha256(new_pool['.rodata'][0]).hexdigest(), table_loads=table_loads,
        original_first_table_owner_offset=416, fixed_anchor_binding_not_installed=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--owner', action='store_true')
    parser.add_argument('--controls', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-node-selection'
    records = []
    for profile in PROFILES:
        record, _, _ = compile_candidate(root, out, 'profile-'+profile, profile=profile)
        records.append(record)
        print(profile, record['body_words'], hex(record['frame']), record['differences'], record['pool_bytes'], flush=True)
    (out / 'profiles.json').write_text(json.dumps(records, indent=2)+'\n')
    if args.controls:
        controls = []
        for name, body in candidates():
            record, _, _ = compile_candidate(root, out, name, body)
            controls.append(record)
            print(name, record['body_words'], hex(record['frame']), record['differences'], flush=True)
        (out / 'controls.json').write_text(json.dumps(controls, indent=2)+'\n')
    if args.owner:
        record = measure_owner(root, out)
        (out / 'owner.json').write_text(json.dumps(record, indent=2)+'\n')
        print(json.dumps({k:v for k,v in record.items() if not k.endswith('_identities')}, indent=2))


if __name__ == '__main__':
    main()
