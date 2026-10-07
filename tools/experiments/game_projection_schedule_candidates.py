"""Fit the projection wrapper while preserving pre-store coordinate snapshots."""

import itertools
import json
import struct
from pathlib import Path

from tools.experiments import game_projection_lifetime_candidates as lifetime
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS = lifetime.ENTRY, lifetime.ROM, lifetime.WORDS
FUNCTION, SYMBOLS, DECLARATIONS, PROTOTYPE = (
    lifetime.FUNCTION, lifetime.SYMBOLS, lifetime.DECLARATIONS, lifetime.PROTOTYPE)
SELECTED = '''s32 func_15144CEC(struct17 *arg0, f32 *arg1, f32 *arg2, f32 *arg3, f32 *arg4, volatile u8 arg5) {
    f32 localZ;
    f32 localW;
    f32 localReciprocal;
    f32 value;
    f32 yProduct;
    s32 offset;

    if (arg2 == NULL) {
        arg2 = &localZ;
    }
    if (arg3 == NULL) {
        arg3 = &localW;
    }
    offset = arg5;
    if (arg4 == NULL) {
        arg4 = &localReciprocal;
    }
    func_150A7A00((f32 (*)[4])((u8 *)D_800D9D10 + (offset << 6)),
                 arg0->unk0, arg0->unk4, arg0->unk8, arg1, arg1 + 1, arg2, arg3);
    value = *arg3;
    if (D_800A56B0 <= value || value <= D_800D9B20) {
        return 0;
    }
    if (value != 0.0f) {
        *arg4 = 1.0f / value;
    } else {
        return 0;
    }
    offset = arg5 * 0x180;
    value = *arg4 * (arg1[0] * (((struct140 *)((u8 *)D_800BE628 + offset))->unkC + 5.0f))
        + ((struct140 *)((u8 *)D_800BE628 + offset))->unk34;
    yProduct = arg1[1] * (((struct140 *)((u8 *)D_800BE628 + offset))->unk10 + 5.0f);
    arg1[0] = value;
    arg1[1] = ((struct140 *)((u8 *)D_800BE628 + offset))->unk38 - *arg4 * yProduct;
    return 1;
}'''

# Raw-PC -> retail-PC: the four independent pre-X-store operations.
SCHEDULE = {0x13C: 0x140, 0x140: 0x144, 0x144: 0x148, 0x148: 0x13C}


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    return lifetime.compile_candidate(root, output, name, body, profile)


def register_mask(word):
    op, rs, fn = word >> 26, word >> 21 & 31, word & 63
    if op == 0:
        return {0: 0x001FF800, 33: 0x03FFF800, 35: 0x03FFF800,
                37: 0x03FFF800}.get(fn, 0)
    if op == 17:
        if rs == 16 and fn in (0, 1, 2, 3, 50, 62):
            return 0x001FFFC0
        if rs == 4:
            return 0x001FF800
    return {5: 0x03FF0000, 9: 0x03FF0000, 15: 0x001F0000,
            35: 0x03FF0000, 36: 0x03FF0000, 43: 0x03FF0000,
            49: 0x03FF0000, 57: 0x03FF0000}.get(op, 0)


def owner_guards():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-projection-schedule'
    output.mkdir(exist_ok=True)
    record, words = compile_candidate(root, output, 'guard-source')
    assert (record['body_words'], record['frame'], record['differences']) == (101, 72, 37)
    retail = struct.unpack_from('>101I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    raw, functions, relocations = parse_object(output / 'guard-source.o')
    raw = struct.unpack_from('>101I', raw, functions[FUNCTION]['value'])
    assert relocations == {0x20: [('R_MIPS_HI16', 'D_800D9D10')],
        0x24: [('R_MIPS_LO16', 'D_800D9D10')], 0x8C: [('R_MIPS_26', 'func_150A7A00')],
        0x98: [('R_MIPS_HI16', 'D_800A56B0')], 0x9C: [('R_MIPS_LO16', 'D_800A56B0')],
        0xA8: [('R_MIPS_HI16', 'D_800D9B20')], 0xBC: [('R_MIPS_LO16', 'D_800D9B20')],
        0xDC: [('R_MIPS_HI16', 'D_800BE628')], 0xE8: [('R_MIPS_LO16', 'D_800BE628')]}
    for offset, word in enumerate(words):
        destination = SCHEDULE.get(offset * 4, offset * 4) // 4
        mask = register_mask(word)
        assert word & ~mask == retail[destination] & ~mask, hex(offset * 4)
    rows = []
    for i, (original, target) in enumerate(zip(words, retail)):
        if original == target:
            continue
        relocation = relocations.get(i * 4, [])
        replacement = target
        if relocation:
            assert i * 4 in (0xDC, 0xE8) and raw[i] & 65535 == 0
            replacement &= 0xFFFF0000
        metadata = ';'.join('%s:%s' % item for item in relocation) or '-'
        rows.append(dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % (i * 4),
            expected='0x%08X' % raw[i], replacement='0x%08X' % replacement,
            expected_relocations=metadata, replacement_relocations=metadata,
            note='Normalize projection wrapper closed temporary allocation and independent four-word capture schedule',
            insert_after='', insert_after_relocations='', omit='false'))
    assert len(rows) == 37
    return rows


def candidates():
    for order, addition, product in itertools.product((False, True), repeat=3):
        body = SELECTED
        if order:
            lines = body.splitlines()
            begin = next(i for i, line in enumerate(lines) if 'value = *arg4 *' in line)
            lines[begin:begin + 3] = [lines[begin + 2], *lines[begin:begin + 2]]
            body = '\n'.join(lines)
        if addition:
            body = body.replace('    value = *arg4 *',
                '    value = ((struct140 *)((u8 *)D_800BE628 + offset))->unk34 + *arg4 *')
            body = body.replace('\n        + ((struct140 *)((u8 *)D_800BE628 + offset))->unk34;', ';')
        if product:
            body = body.replace('*arg4 * yProduct', 'yProduct * *arg4')
        yield 'order%d-add%d-product%d' % (order, addition, product), body


def main():
    root = Path(__file__).resolve().parents[2]
    output = root / 'conker/build/game-projection-schedule'
    output.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        for profile in lifetime.PROFILES:
            record, _ = compile_candidate(root, output, name + '-' + profile, body, profile)
            records.append(record)
            print(record['name'], record['body_words'], record['frame'], record['differences'], flush=True)
    (output / 'schedule-measurements.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
