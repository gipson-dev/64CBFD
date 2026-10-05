"""Resource relocation register guards: bounded full-word traces, not hardware."""

import csv
import hashlib
import re
import shutil
import struct
import unittest
from pathlib import Path

from tools.experiments import game_offset_relocator_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_queued_segment_writer import SegmentQueueOracle


ENTRY = 0x1502B4A8
GUARDS = {
    0xA0: (0x000278C0, 0x000270C0),
    0xA4: (0x0005C0C0, 0x000578C0),
    0xA8: (0x03043021, 0x01E43021),
    0xAC: (0x008F1821, 0x008E1821),
    0xB8: (0x8C790004, 0x8C780004),
    0xC0: (0x03274824, 0x0307C824),
    0xC8: (0xAC690004, 0xAC790004),
    0xCC: (0x15200003, 0x17200003),
    0xD0: (0x00445821, 0x00445021),
    0xDC: (0xAC6B0000, 0xAC6A0000),
    0xE0: (0x8C6C000C, 0x8C6B000C),
    0xE8: (0x01876824, 0x01676024),
    0xF0: (0xAC6D000C, 0xAC6C000C),
    0xF4: (0x15A00003, 0x15800003),
    0xF8: (0x00447821, 0x00447021),
    0x104: (0xAC6F0008, 0xAC6E0008),
    0x110: (0x8C790004, 0x8C780004),
}


def source_body():
    return dict(screen.candidates())['named-tag-ResourceRelocationEntry57FA0']


class RelocationOracle(SegmentQueueOracle):
    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        if op == 0 and word & 63 == 36:
            self.r[word >> 11 & 31] = self.r[rs] & self.r[rt]
            self.r[0] = 0
        elif op == 11:
            immediate = word & 65535
            if immediate & 0x8000:
                immediate |= 0xFFFF0000
            self.r[rt] = int(self.r[rs] < immediate)
            self.r[0] = 0
        else:
            super().execute(word)


def memory_case(base, pairs):
    memory = {base + i: 0xA5 for i in range(-16, len(pairs) * 8 + 16)}
    for index, pair in enumerate(pairs):
        memory.update({base + index * 8 + i: byte for i, byte in enumerate(struct.pack('>II', *pair))})
    return memory


class GameOffsetRelocatorMatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(name) is None for name in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        output = cls.root / 'conker/build/game-offset-relocator-test'
        output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, output, 'typed-scan', source_body())
        cls.retail = list(struct.unpack_from('>72I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0x58958))
        cls.guarded = cls.raw[:]
        for offset, (expected, replacement) in GUARDS.items():
            if cls.guarded[offset // 4] != expected:
                raise AssertionError('compiled guard input changed')
            cls.guarded[offset // 4] = replacement

    def test_raw_slot_and_closed_allocation(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']),
                         (72, 0, 17))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(hashlib.sha256(struct.pack('>72I', *self.raw)).hexdigest(),
                         '1174f22c712142aeaec1cd146c214088942d94898c0a3d1a6a0a867ea121a96d')
        self.assertEqual({i * 4: (a, b) for i, (a, b) in enumerate(zip(self.raw, self.retail)) if a != b},
                         GUARDS)
        self.assertEqual(self.guarded, self.retail)
        self.assertEqual(hashlib.sha256(struct.pack('>72I', *self.guarded)).hexdigest(),
                         'a07f71a50c44c47daf0edd894105db8a482bf2e3ff105109148e8c807164944f')

    def test_baseline_and_oversize_scan_remain_reproducible_rejection_controls(self):
        output=self.root/'conker/build/game-offset-relocator-test'
        forms=dict(screen.candidates())
        self.assertEqual(forms['break'],screen.BASELINE)
        for name,body,differences in (('break',65,71),('while-post-increment',73,73)):
            record,words=screen.compile_candidate(self.root,output,name,forms[name])
            self.assertEqual((record['body_words'],record['frame'],record['real_differences']),
                             (body,0,differences))
            self.assertEqual(record['diagnostics'],'')
            if name=='break':
                self.assertEqual(hashlib.sha256(struct.pack('>72I',*words)).hexdigest(),
                                 'bcce58836363dffad7c081528b0be692fbdfc461a5cc8b71e9b3376e16b43262')

    def paired(self, base, count, pairs):
        memory = memory_case(base, pairs)
        models = [RelocationOracle(words, ENTRY, memory, (base, count)).run()
                  for words in (self.retail, self.raw, self.guarded)]
        expected = count if count else next(i + 1 for i, pair in enumerate(pairs) if pair[1] & 0x80000000)
        for model in models:
            self.assertEqual(model.r[2], expected & 0xFFFFFFFF)
            self.assertEqual(model.memory, models[0].memory)
            self.assertEqual(model.reads, models[0].reads)
            self.assertEqual(model.stores, models[0].stores)
        return models

    def test_three_way_fixed_and_auto_counts_cover_every_reachable_word(self):
        coverage = [set(), set(), set()]
        cases = 0
        offsets = (0, 1, 16, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFE, 0xFFFFFFFF)
        lengths = (0, 1, 0x0FFFFFFF, 0x10000000, 0x80000000, 0xFFFFFFFF)
        for base in (0x20000, 0x80020000, 0xFFFFFE00):
            for count in range(1, 18):
                for offset in offsets:
                    for length in lengths:
                        pairs = [(offset, length)] * count
                        models = self.paired(base, count, pairs)
                        for visited, model in zip(coverage, models):
                            visited.update(model.visits)
                        cases += 1
            for last in range(20):
                for offset in offsets:
                    for terminal in lengths:
                        pairs = [(offset, 0x10000001)] * (last + 1)
                        pairs[-1] = (offset, terminal | 0x80000000)
                        models = self.paired(base, 0, pairs)
                        for visited, model in zip(coverage, models):
                            visited.update(model.visits)
                        cases += 1
        for count in (-1, -2, -0x80000000):
            models = self.paired(0, count, [])
            for visited, model in zip(coverage, models):
                self.assertFalse(model.reads or model.stores)
                visited.update(model.visits)
            cases += 1
        # The odd-entry peel has a duplicated store after an unconditional branch.
        expected = set(range(ENTRY, ENTRY + 72 * 4, 4)) - {0x1502B538}
        self.assertEqual(coverage, [expected] * 3)
        self.assertEqual(cases, 4665)
        print('offset relocation:', cases, 'three-way cases, all 71 reachable words')

    def test_missing_any_guard_is_rejected(self):
        for offset in GUARDS:
            partial = self.guarded[:]
            partial[offset // 4] = self.raw[offset // 4]
            rejected = False
            for count, pairs in ((2, [(16, 1), (32, 1)]),
                                 (2, [(16, 0), (32, 1)]),
                                 (2, [(16, 1), (32, 0)]),
                                 (4, [(16, 1), (32, 1), (48, 0), (64, 1)]),
                                 (3, [(16, 0), (0xFFFFFFFF, 1), (32, 1)])):
                memory = memory_case(0x20000, pairs)
                reference = RelocationOracle(self.retail, ENTRY, memory, (0x20000, count)).run()
                try:
                    candidate = RelocationOracle(partial, ENTRY, memory, (0x20000, count)).run()
                    rejected |= (candidate.memory != reference.memory or candidate.reads != reference.reads
                                 or candidate.stores != reference.stores or candidate.r[2] != reference.r[2])
                except (AssertionError, KeyError):
                    rejected = True
            self.assertTrue(rejected, hex(offset))

    def test_mixed_records_have_independent_masked_lengths_and_wrapping_offsets(self):
        offsets = (0, 1, 16, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFE, 0xFFFFFFFF)
        lengths = (0, 1, 0x0FFFFFFF, 0x10000000, 0x80000000, 0xFFFFFFFF)
        cases=0
        base=0xFFFFFE00
        for count in range(1,33):
            for phase in range(7):
                for auto in (False,True):
                    pairs=[(offsets[(i+phase)%7], lengths[(i+phase)%6] & 0x7FFFFFFF)
                           for i in range(count)]
                    if auto:
                        pairs[-1]=(pairs[-1][0],pairs[-1][1]|0x80000000)
                    models=self.paired(base,0 if auto else count,pairs)
                    for model in models:
                        for i,(offset,length) in enumerate(pairs):
                            masked=length & 0x0FFFFFFF
                            relocated=0 if not masked or offset==0xFFFFFFFF else (base+offset)&0xFFFFFFFF
                            address=base+i*8
                            actual=bytes(model.memory[address+j] for j in range(8))
                            self.assertEqual(actual,struct.pack('>II',relocated,masked))
                    cases+=1
        self.assertEqual(cases,448)
        print('offset relocation mixed records:',cases,'three-way cases')

    def test_production_source_and_guard_rows_match_the_independent_fixture(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        body = re.search(r's32 func_1502B4A8\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body, source_body())
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = [row for row in csv.DictReader(stream) if row['function'] == 'func_1502B4A8']
        self.assertEqual({int(row['offset'], 0): (int(row['expected'], 0), int(row['replacement'], 0))
                         for row in rows}, GUARDS)
        self.assertEqual(len(rows), 17)
        for row in rows:
            self.assertEqual(row['filename'], 'game_57FA0')
            self.assertEqual((row['expected_relocations'], row['replacement_relocations']), ('-', '-'))
            self.assertEqual((row['insert_after'], row['omit']), ('', 'false'))
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                    'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502B4A8'], ENTRY)
        self.assertEqual(functions['func_1502B4A8'], self.retail)


if __name__ == '__main__':
    unittest.main()
