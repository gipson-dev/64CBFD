"""Recover retail local allocation; guard only proven register/schedule words."""

import itertools
import json
import struct
import sys
from pathlib import Path

from tools.experiments import game_sphere_callee_candidates as prior
from tools.experiments.game_projection_schedule_candidates import register_mask as base_mask
from tools.pad_generated_object import parse_object

ENTRY, ROM, WORDS, FUNCTION = prior.ENTRY, prior.ROM, prior.WORDS, prior.FUNCTION
DOT = prior.DOT
ASSEMBLY = '#pragma GLOBAL_ASM("asm/nonmatchings/game_16EE20/func_151452C4.s")'


def allocation_body(mask=1, early=True, relative_last=True, perp_last=False):
    body = prior.union_body(mask)
    begin, end = body.index('    ', body.index('{') + 1), body.index('\n\n')
    declarations = body[begin:end].splitlines()
    vectors, coordinates, scalars = declarations[:3], declarations[3:6], declarations[6:]
    if perp_last:
        perpendicular = next(d for d in scalars if 'perpendicularSquared;' in d)
        scalars = [d for d in scalars if d != perpendicular] + [perpendicular]
    reordered = (coordinates if early else []) + (vectors[:2] if relative_last else vectors) + (
        [] if early else coordinates) + scalars + ([vectors[2]] if relative_last else [])
    return body[:begin] + '\n'.join(reordered) + body[end:]


SELECTED = allocation_body()
# The independent relative address moves past point writes; two final loads swap.
SCHEDULE = {0x114: 0x198, 0x198: 0x190,
            **{offset: offset - 4 for offset in range(0x118, 0x194, 4)}}


def local_layout(obj):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'ultralib/tools'))
    from libelf import ElfFile
    from mdebug import EcoffSt
    elf = ElfFile(Path(obj).read_bytes())
    for fdr in elf.find_section_by_name('.mdebug').fdrs:
        for pdr in fdr.pdrs:
            if pdr.name == FUNCTION:
                offsets = {sym.name: sym.value - 0x100000000 if sym.value & 0x80000000 else sym.value
                           for sym in pdr.symrs if sym.st == EcoffSt.LOCAL}
                return dict(frame=pdr.frameoffset, entry_relative=offsets)
    raise ValueError('Missing sphere callee debug procedure')


def compile_candidate(root, output, name, body=SELECTED, profile='o2g3'):
    return prior.compile_candidate(root, output, name, body, profile)


def register_mask(word):
    if word >> 26 == 17 and word >> 21 & 31 == 16 and word & 63 in (4, 6, 7, 60):
        return 0x001FFFC0
    return base_mask(word)


def owner_guards():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-sphere-callee-allocation-match'
    out.mkdir(exist_ok=True)
    record, words = compile_candidate(root, out, 'guard-source')
    assert (record['body_words'], record['frame'], record['differences']) == (126, 112, 53)
    assert record['relocations'] == {0x1C0: [('R_MIPS_26', 'func_15144A74')]}
    layout = local_layout(out / 'guard-source.o')
    assert layout['frame'] == 112
    assert {k: layout['entry_relative'][k] for k in ('direction', 'origin', 'relative')} == {
        'direction': -24, 'origin': -36, 'relative': -72}
    assert set(SCHEDULE) == set(SCHEDULE.values())
    retail = struct.unpack_from('>126I', (root / 'conker/conker.us.bin').read_bytes(), ROM)
    raw, functions, relocations = parse_object(out / 'guard-source.o')
    raw = struct.unpack_from('>126I', raw, functions[FUNCTION]['value'])
    for i, word in enumerate(words):
        target = retail[SCHEDULE.get(i * 4, i * 4) // 4]
        mask = register_mask(word)
        assert word & ~mask == target & ~mask, hex(i * 4)
    rows = []
    for i, (word, target) in enumerate(zip(words, retail)):
        if word == target:
            continue
        assert i * 4 not in relocations
        rows.append(dict(filename='game_16EE20', function=FUNCTION, offset='0x%X' % (i * 4),
            expected='0x%08X' % raw[i], replacement='0x%08X' % target,
            expected_relocations='-', replacement_relocations='-',
            note='Normalize sphere callee closed FP allocation and independent relative-address schedule',
            insert_after='', insert_after_relocations='', omit='false'))
    assert len(rows) == 53
    return rows


def candidates():
    for options in itertools.product((0, 1, 3, 7), (False, True), (False, True), (False, True)):
        yield 'mask%d-early%d-last%d-perp%d' % options, allocation_body(*options)


def main():
    root = Path(__file__).resolve().parents[2]
    out = root / 'conker/build/game-sphere-callee-allocation-match'
    out.mkdir(exist_ok=True)
    records = []
    for name, body in candidates():
        record, _ = compile_candidate(root, out, name, body)
        records.append(record)
        print(name, record['body_words'], record['frame'], record['differences'], flush=True)
    (out / 'measurements.json').write_text(json.dumps(records, indent=2) + '\n')
    (out / 'guards.json').write_text(json.dumps(owner_guards(), indent=2) + '\n')
    (out / 'local-layout.json').write_text(json.dumps(local_layout(out / 'guard-source.o'), indent=2) + '\n')


if __name__ == '__main__':
    main()
