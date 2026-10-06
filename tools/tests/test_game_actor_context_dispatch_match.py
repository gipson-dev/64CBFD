"""Context dispatcher allocation closure; actual helper implementations stay opaque."""

import csv
import itertools
import re
import struct
import unittest
from pathlib import Path
from unittest import mock

from tools.experiments import game_actor_context_pointer_candidates as screen
from tools import pad_generated_object as pad
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put, external_writes
from tools.tests.game_animation_timeline_oracle import bits
from tools.tests.test_game_table_range_loader import STACK


ENTRY, ACTOR = 0x15044380, 0x20000
PREPARE, SWITCH, FIRST, SECOND = 0x15044660, 0x1510F800, 0x150AB1F0, 0x150AC3E4
CURRENT, ENABLE, ELIGIBLE = 0x800CBDD3, 0x80089120, 0x800DBE62
LOW, HIGH = 0x800CBDF4, 0x800CBDF8
XYZ = tuple(map(bits, (1.25, -7.5, 3.75)))
VALUES = (0x7FFFFFFF, 0x80000000, 0xFFFFFFFF, 0x12345678)
SELECTED = 'pointers-1-before-sum-first'
GUARDS = {
    0x068: (0x0000B825, 0x0000B025),
    0x084: (0x3C16800E, 0x3C15800E),
    0x088: (0x26D6BE62, 0x26B5BE62),
    0x094: (0x24150003, 0x8FB70078),
    0x098: (0x24140001, 0x24140003),
    0x09C: (0x8FB30078, 0x24130001),
    0x0A8: (0x568F0014, 0x566F0014),
    0x0B0: (0x16150005, 0x16140005),
    0x0D0: (0x92C80000, 0x92A80000),
    0x0F0: (0xAFB30010, 0xAFB70010),
    0x0F4: (0x0057B821, 0x02C2B021),
    0x11C: (0x568A000D, 0x566A000D),
    0x12C: (0x92CB0000, 0x92AB0000),
    0x154: (0x1615FFF0, 0x1614FFF0),
    0x16C: (0x02E01025, 0x02C01025),
}


def guarded(words, omitted=None):
    words = words[:]
    for offset, (expected, replacement) in GUARDS.items():
        assert words[offset // 4] == expected, ('stale context guard', offset)
        if offset != omitted:
            words[offset // 4] = replacement
    return words


def rename(word):
    cycle = {23: 22, 22: 21, 21: 20, 20: 19, 19: 23}
    op = word >> 26
    if op in (2, 3):
        return word
    if op == 17:
        # Only MFC1/MTC1 use a general register in the RT field.
        fields = (16,) if word >> 21 & 31 in (0, 4) else ()
    elif op in (49, 53, 57, 61):
        fields = (21,)
    elif op == 0:
        fields = (21, 16, 11)
    else:
        fields = (21, 16)
    for shift in fields:
        register = word >> shift & 31
        word = word & ~(31 << shift) | cycle.get(register, register) << shift
    return word


class ContextOracle(TriangleOracle):
    def __init__(self, words, enable=(1, 1, 1, 1), eligibility=(1, 1, 1, 1),
                 flags=0, second=0, phase=0, mode=0x81234567, mutation=0):
        memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
        memory.update({ACTOR + i: 0xA5 for i in range(-8, 0x280)})
        for base in (CURRENT, ENABLE, ELIGIBLE, LOW, HIGH):
            memory.update({base + i: 0xA5 for i in range(-4, 12)})
        put(memory, ACTOR + 0xF8, flags)
        put(memory, CURRENT, 0xAB, 1)
        put(memory, ELIGIBLE, 0, 1)
        for i, value in enumerate(enable):
            put(memory, ENABLE + i, value, 1)
        super().__init__(words, memory, phase=phase, entry=ENTRY,
                         arguments=(*XYZ, ACTOR, mode, second))
        self.f[12], self.f[14] = XYZ[:2]
        self.eligibility, self.mutation, self.current = eligibility, mutation, -1

    def record_call(self, target):
        if target == PREPARE:
            args = (self.r[4], *self.r[5:8])
            assert args == (ACTOR, *XYZ)
            assert self.get(ACTOR + 0x275, 1) == 0
            assert self.get(LOW, 4) == self.get(HIGH, 4) == bits(-32768.0)
        elif target == SWITCH:
            args = (self.r[4],)
            assert args[0] in range(4)
        else:
            assert target in (FIRST, SECOND)
            args = (self.f[12], self.f[14], self.r[6], self.r[7],
                    self.get(self.r[29] + 0x10, 4))
            assert args[:4] == (*XYZ, ACTOR)
            assert self.get(ELIGIBLE, 1) != 0
        self.calls.append((target, self.current, *args))

    def hook(self, target):
        result = 0
        if target == PREPARE:
            if self.mutation == 1:
                self.put(CURRENT, 0xE7, 1)
            if self.mutation == 3:
                self.put(ACTOR + 0xF8, 0, 4)
            if self.mutation == 4:
                self.put(LOW, bits(123.0), 4)
                self.put(HIGH, bits(456.0), 4)
        elif target == SWITCH:
            self.current = self.r[4]
            self.put(CURRENT, self.current, 1)
            self.put(ELIGIBLE, self.eligibility[self.current], 1)
        elif target == FIRST:
            result = VALUES[self.current]
            if self.mutation == 2 and self.current == 2:
                self.put(ENABLE + 1, 1, 1)
                self.put(ENABLE, 2, 1)
                self.put(CURRENT, 0xFA, 1)
            if self.mutation == 5:
                self.put(ACTOR + 0xF8, self.get(ACTOR + 0xF8, 4) | 0x200, 4)
        else:
            assert target == SECOND
            self.put(CURRENT, 0xEF, 1)
            result = 0xDEADBEEF
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result
        self.f[:20] = [0xA5000000 + i for i in range(20)]


class GameActorContextDispatchMatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-actor-context-match-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.output, 'selected', dict(screen.candidates())[SELECTED])
        cls.baseline_record, cls.baseline = screen.compile_candidate(cls.output, 'checkpoint', screen.BASELINE)
        cls.retail = list(struct.unpack_from('>107I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0x71830))
        cls.words = guarded(cls.raw)

    def models(self, **case):
        models = [ContextOracle(words, **case).run() for words in (self.retail, self.raw, self.baseline)]
        for model in models[1:]:
            self.assertEqual(model.calls, models[0].calls)
            self.assertEqual(external_writes(model), external_writes(models[0]))
            reads = lambda m: [e for e in m.events if e[0] == 'R' and not STACK - 0x600 <= e[1] < STACK + 0x100]
            self.assertEqual(reads(model), reads(models[0]))
            self.assertEqual(model.r[2], models[0].r[2])
        return models[0]

    def test_frozen_inventory_selected_source_and_fail_closed_anchors(self):
        forms = screen.candidates()
        self.assertEqual((len(forms), len(dict(forms))), (19, 19))
        self.assertEqual(forms[0], ('checkpoint', screen.BASELINE))
        source = screen.SOURCE.read_text()
        body = re.search(r's32 func_15044380\([^;{]*\{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body, dict(forms)[SELECTED])
        self.assertNotRegex(screen.PREAMBLE, r'void func_1510F800\(')
        with self.assertRaises(ValueError):
            screen.candidates(screen.BASELINE.replace('s32 total;', 'u32 total;'))
        with self.assertRaises(ValueError):
            screen.candidates(screen.BASELINE.replace('for (context = 3;', 'for (context = 2;'))

    def test_raw_frame_homes_and_exact_production_slot(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']),
                         (107, 0x68, 15))
        self.assertEqual((self.baseline_record['body_words'], self.baseline_record['frame'],
                          self.baseline_record['real_differences']), (107, 0x60, 20))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        functions = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        self.assertEqual(functions['func_15044380'], self.retail)
        for offset in (0, 4, 0xC, 0x10, 0x14, *range(0x2C, 0x4C, 4), 0xA0,
                       0x104, 0x164, *range(0x174, 0x1AC, 4)):
            self.assertEqual(self.raw[offset // 4], self.retail[offset // 4], hex(offset))

    def test_complete_register_cycle_schedule_and_commutative_add(self):
        normalized = self.raw[:]
        # Saves/restores preserve all five registers individually; rename only their active lifetimes.
        for i in range(0x68 // 4, 0x170 // 4):
            normalized[i] = rename(normalized[i])
        a, b, c = normalized[0x94 // 4:0xA0 // 4]
        normalized[0x94 // 4:0xA0 // 4] = [c, a, b]
        self.assertEqual((a, b, c), (0x24140003, 0x24130001, 0x8FB70078))
        word = normalized[0xF4 // 4]
        self.assertEqual(word, 0x0056B021)
        normalized[0xF4 // 4] = word & ~((31 << 21) | (31 << 16)) | (22 << 21) | (2 << 16)
        self.assertEqual(normalized, self.retail)
        changed = {i * 4 for i, (a, b) in enumerate(zip(self.raw, self.retail)) if a != b}
        self.assertEqual(changed, set(GUARDS))

    def test_csv_object_words_relocations_and_no_insertion(self):
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = [r for r in csv.DictReader(stream) if r['function'] == 'func_15044380']
        self.assertEqual(len(rows), 15)
        obj = self.output / 'selected.o'
        text, functions, relocations = pad.parse_object(obj)
        start = functions['func_15044380']['value']
        raw = list(struct.unpack_from('>107I', text, start))
        self.assertEqual({int(r['offset'], 0) for r in rows}, set(GUARDS))
        for row in rows:
            offset = int(row['offset'], 0)
            self.assertEqual(row['filename'], 'generated_71820')
            self.assertEqual(int(row['expected'], 0), raw[offset // 4])
            self.assertEqual(pad.parse_relocation_spec(row['expected_relocations']),
                             relocations.get(start + offset, []))
            self.assertEqual(row['replacement_relocations'], row['expected_relocations'])
            expected = GUARDS[offset][1]
            if offset in (0x84, 0x88):
                expected &= 0xFFFF0000
            self.assertEqual(int(row['replacement'], 0), expected)
            self.assertEqual((row['insert_after'], row['insert_after_relocations'], row['omit']), ('', '', 'false'))

    def test_actual_guard_emitter_rejects_changed_relocations(self):
        obj = self.output / 'selected.o'
        text, functions, relocations = pad.parse_object(obj)
        name = 'func_15044380'
        start = functions[name]['value']
        patches = {key: value for key, value in pad.load_word_patches(
            self.root / 'conker/retail_word_patches.us.csv', 'generated_71820').items() if key[0] == name}
        retail = (ENTRY, ENTRY + 107 * 4, {name: ENTRY}, {})
        with mock.patch.object(pad, 'parse_retail_slice', return_value=retail), \
                mock.patch.object(pad, 'load_word_patches', return_value=patches):
            emitted = pad.emit_padded_assembly(obj, self.root / 'conker/asm/71820.s')
            self.assertEqual(emitted.count('.word '), 107)
            for offset in (0x84, 0x88):
                for changed in ([], [(relocations[start + offset][0][0], 'D_80089120')]):
                    stale = dict(relocations)
                    stale[start + offset] = changed
                    with mock.patch.object(pad, 'parse_object', return_value=(text, functions, stale)):
                        with self.assertRaisesRegex(ValueError, 'stale relocations'):
                            pad.emit_padded_assembly(obj, self.root / 'conker/asm/71820.s')

    def test_guards_reject_stale_words_and_incomplete_cycles(self):
        for offset in GUARDS:
            changed = self.raw[:]
            changed[offset // 4] ^= 1
            with self.assertRaisesRegex(AssertionError, 'stale context guard'):
                guarded(changed)
            self.assertNotEqual(guarded(self.raw, omitted=offset), self.retail)

    def test_each_omitted_cycle_word_has_a_behavioral_counterexample(self):
        cases = [dict(enable=(1, 1, 1, 1), second=-1), dict(enable=(1, 1, 1, 1), flags=0x200),
                 dict(enable=(0, 1, 0, 1), second=-1)]
        for offset in GUARDS:
            rejected = False
            for case in cases:
                retail = ContextOracle(self.retail, **case).run()
                try:
                    altered = ContextOracle(guarded(self.raw, omitted=offset), **case).run()
                    rejected |= (altered.calls != retail.calls or external_writes(altered) != external_writes(retail)
                                 or altered.r[2] != retail.r[2])
                except (AssertionError, KeyError):
                    rejected = True
            self.assertTrue(rejected, hex(offset))

    def test_three_way_all_enable_bytes_gates_passes_and_complete_coverage(self):
        coverage, cases = set(), 0
        for enable, second, flags, eligibility in itertools.product(
                itertools.product((0, 1, 2, 255), repeat=4), (0, 1, -1), (0, 0x200),
                ((0, 0, 0, 0), (1, 1, 1, 1), (2, 0, 255, 0), (0, 255, 0, 2))):
            first = [i for i in (3, 2, 1, 0) if enable[i] == 1 and (i != 3 or not flags & 0x200)]
            second_contexts = [i for i in range(3) if second and enable[i] == 1]
            mode = 0x81234567 if cases & 1 else 0x7FFFFFFF
            model = self.models(enable=enable, second=second, flags=flags, eligibility=eligibility,
                                mode=mode, phase=8 if cases & 1 else 0)
            self.assertEqual([c[2] for c in model.calls if c[0] == SWITCH], first + second_contexts + [0])
            self.assertEqual([c[1] for c in model.calls if c[0] == FIRST], [i for i in first if eligibility[i]])
            self.assertEqual([c[1] for c in model.calls if c[0] == SECOND], [i for i in second_contexts if eligibility[i]])
            self.assertEqual(model.r[2], sum(VALUES[i] for i in first if eligibility[i]) & 0xFFFFFFFF)
            self.assertEqual(model.get(CURRENT, 1), 0xAB)
            for call in model.calls:
                if call[0] in (FIRST, SECOND):
                    self.assertEqual(call[-1], mode if call[0] == FIRST else 0)
            coverage.update(model.visits)
            cases += 1
        self.assertEqual(cases, 6144)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 107 * 4, 4)))

    def test_three_way_helper_mutations_and_post_prepare_context_save(self):
        cases = 0
        for mutation, flags, second, phase in itertools.product(range(1, 6), (0, 0x200), (0, -1), (0, 8)):
            model = self.models(mutation=mutation, flags=flags, second=second, phase=phase,
                                enable=(1, 0, 1, 1) if mutation == 2 else (1, 1, 1, 1))
            self.assertEqual(model.get(CURRENT, 1), 0xE7 if mutation == 1 else 0xAB)
            if mutation == 2:
                self.assertIn(1, [c[1] for c in model.calls if c[0] == FIRST])
                self.assertNotIn(0, [c[1] for c in model.calls if c[0] == FIRST])
            if mutation == 3:
                self.assertEqual(len([c for c in model.calls if c[0] == FIRST]), 4)
            if mutation == 4:
                self.assertEqual((model.get(LOW, 4), model.get(HIGH, 4)), (bits(123.0), bits(456.0)))
            cases += 1
        self.assertEqual(cases, 40)


if __name__ == '__main__':
    unittest.main()
