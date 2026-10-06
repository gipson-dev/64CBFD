"""Direct dispatcher match; callbacks and cleanup remain bounded opaque helpers."""

import csv
import itertools
import re
import struct
import unittest
from pathlib import Path

from tools.experiments import game_record_dispatch_induction_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_record_dispatch as native


ENTRY, TABLE, CLEANUP, FREE = screen.ENTRY, 0x800844B0, 0x800848B0, 0x1500390C
BUFFER, ORDINARY, ALTERNATE = 0x20000, 0x15100000, 0x15100004


def external(model):
    return [e for e in model.events if e[0] == 'CALL' or not STACK - 0x600 <= e[1] < STACK + 0x100]


def nonstack(memory):
    return {a: v for a, v in memory.items() if not STACK - 0x600 <= a < STACK + 0x100}


def memory_case(seed=0, cleanup=0, high=False):
    buffer = BUFFER if not high else 0x80020004
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({buffer + i: (i * 137 + 19) & 255 for i in range(-8, 248)})
    for selector in range(256):
        put(memory, TABLE + selector * 4, ALTERNATE if selector == 255 else ORDINARY)
    put(memory, CLEANUP, cleanup)
    for index in range(30):
        put(memory, buffer + index * 8, (seed + index * 137) & 255, 1)
    return memory, buffer


class DispatchOracle(TriangleOracle):
    def __init__(self, words, memory, buffer=BUFFER, phase=0, mode=0):
        super().__init__(words, memory, phase=phase, entry=ENTRY, arguments=(buffer + 160,))
        self.buffer, self.mode, self.dispatches, self.cleanups = buffer, mode, 0, 0

    def record_call(self, target):
        assert target in (ORDINARY, ALTERNATE, FREE), ('unexpected callback target', target)
        args = (self.r[4],)
        self.calls.append((target, *args))
        self.events.append(('CALL', target, args))

    def hook(self, target):
        if target == FREE:
            assert self.dispatches == 30
            self.cleanups += 1
            self.put(CLEANUP, 0, 4)
        else:
            assert self.r[4] == self.buffer + self.dispatches * 8
            index = self.dispatches
            if self.mode == 1 and index == 0:
                self.put(CLEANUP, 0, 4)
            if self.mode == 2 and index == 29:
                self.put(CLEANUP, 0xFFED2979, 4)
            if self.mode in (3, 6) and index == 0:
                self.put(self.buffer + 8, 255, 1)
            if self.mode in (4, 6) and index == 0:
                selector = self.memory[self.buffer + 8]
                self.put(TABLE + selector * 4, ALTERNATE, 4)
            if self.mode == 5:
                self.put(CLEANUP, 0 if index & 1 else index + 1, 4)
            if self.mode == 7 and index == 0:
                for future in range(1, 30):
                    self.put(self.buffer + future * 8, (future * 7) & 255, 1)
                    self.put(TABLE + ((future * 7) & 255) * 4, ALTERNATE, 4)
                self.put(CLEANUP, 0x80000000, 4)
            self.dispatches += 1
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]


class GameRecordDispatchMatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-record-dispatch-match-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        cls.old_record, cls.old_words = screen.compile_candidate(cls.root, cls.output, 'baseline', screen.BASELINE)
        cls.retail = list(struct.unpack_from('>38I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0x6E178))

    def test_selected_complete_direct_slot_frame_saves_and_no_divide(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['saved'],
                          self.record['real_differences'], self.record['diagnostics']),
                         (38, 0x28, [18, 17, 16], 0, ''))
        self.assertEqual(self.words, self.retail)
        self.assertFalse(any(w >> 26 == 0 and w & 63 in (26, 27) for w in self.words))
        self.assertEqual((self.old_record['body_words'], self.old_record['saved'],
                          self.old_record['real_differences']), (39, [19, 18, 17, 16], 30))

    def test_independent_declaration_and_increment_controls(self):
        forms = screen.candidates()
        self.assertEqual(len(forms), len(dict(forms)))
        self.assertEqual(len(forms), 45)
        with self.assertRaises(ValueError):
            screen.replace(screen.BASELINE, 'missing anchor', 'replacement')
        for name, expected in (('integer-record-only', (39, 30)),
                               ('division-increment', (39, 24)),
                               ('unsigned-biased-condition', (38, 25)),
                               ('negated-complement-increment', (40, 25))):
            record, words = screen.compile_candidate(self.root, self.output, name, dict(forms)[name])
            self.assertEqual((record['body_words'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')
            self.assertNotEqual(words, self.retail)

    def test_all_unsigned_selectors_cleanup_states_mutations_and_instruction_coverage(self):
        coverage, cases = set(), 0
        for seed, cleanup, mode, phase in itertools.product(range(256), (0, 0xFFFFFFFF, 0x80000000),
                                                           range(8), (0, 8)):
            memory, buffer = memory_case(seed, cleanup)
            models = [DispatchOracle(w, memory, buffer, phase, mode).run()
                      for w in (self.retail, self.words, self.old_words)]
            model = models[0]
            for other in models[1:]:
                self.assertEqual(external(other), external(model))
                self.assertEqual(nonstack(other.memory), nonstack(model.memory))
                self.assertEqual(other.calls, model.calls)
            callbacks = [c for c in model.calls if c[0] != FREE]
            self.assertEqual([c[1] for c in callbacks], [buffer + i * 8 for i in range(30)])
            for i, (target, _) in enumerate(callbacks):
                selector = (seed + i * 137) & 255
                expected = ALTERNATE if selector == 255 else ORDINARY
                if mode in (3, 6) and i == 1:
                    expected = ALTERNATE
                if mode in (4, 6) and i > 0:
                    changed = 255 if mode == 6 else (seed + 137) & 255
                    if selector == changed:
                        expected = ALTERNATE
                if mode == 7 and i > 0:
                    expected = ALTERNATE
                self.assertEqual(target, expected)
            wanted = 0 if mode in (1, 5) else 0xFFED2979 if mode == 2 else 0x80000000 if mode == 7 else cleanup
            self.assertEqual([c for c in model.calls if c[0] == FREE], [(FREE, wanted)] if wanted else [])
            self.assertEqual(sum(a == CLEANUP for a, _, _ in model.reads), 1)
            self.assertEqual(sum(TABLE <= a < TABLE + 1024 for a, _, _ in model.reads), 30)
            self.assertEqual(model.f[20:], model.saved_f)
            coverage.update(model.visits)
            cases += 1
        self.assertEqual(cases, 12288)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 38 * 4, 4)))

    def test_high_guest_record_addresses_and_repeated_dispatch(self):
        for seed, phase in itertools.product((0, 127, 255), (0, 8)):
            memory, buffer = memory_case(seed, 0xFFFFFFFF, high=True)
            for words in (self.retail, self.words, self.old_words):
                first = DispatchOracle(words, memory, buffer, phase).run()
                second = DispatchOracle(words, first.memory, buffer, phase).run()
                self.assertEqual(first.calls[-1], (FREE, 0xFFFFFFFF))
                self.assertEqual(len(second.calls), 30)
                self.assertEqual([c[1] for c in second.calls], [buffer + i * 8 for i in range(30)])

    def test_callback_mutation_controls_fail_the_reference_contract(self):
        for name, body in (
                ('signed-selector', screen.SELECTED.replace('*(u8 *)record', '*(s8 *)record')),
                ('wrong-stride', screen.SELECTED.replace('arg0 + i * 8', 'arg0 + i * 4')),
                ('miss-final-record', screen.SELECTED.replace('i < 10', 'i < 9')),
                ('missing-cleanup', screen.SELECTED.replace('func_1500390C(D_800848B0);', ''))):
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            memory, buffer = memory_case(128, 1)
            reference = DispatchOracle(self.retail, memory, buffer).run()
            try:
                altered = DispatchOracle(words, memory, buffer).run()
            except (AssertionError, KeyError):
                continue
            self.assertNotEqual(altered.calls, reference.calls, name)

    def test_native_selected_runs_existing_eight_semantic_cases(self):
        native.GameRecordDispatchTests.setUpClass()
        self.addCleanup(native.GameRecordDispatchTests.doClassCleanups)
        original = native.GameRecordDispatchTests.source
        body = re.search(r'void func_15040CC8\(u8 \*arg0\) \{\n.*?\n\}', original, re.S).group(0)
        self.assertEqual(original.count(body), 1)
        native.GameRecordDispatchTests.source = original.replace(body, screen.SELECTED, 1)
        try:
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(native.GameRecordDispatchTests)
            result = unittest.TestResult()
            suite.run(result)
            self.assertEqual(result.testsRun, 8)
            self.assertEqual((result.errors, result.failures, result.skipped), ([], [], []))
        finally:
            native.GameRecordDispatchTests.source = original

    def test_jalr_target_is_captured_before_link_register_write(self):
        memory, buffer = memory_case()
        words = [0x27BDFFE8, 0xAFBF0014, 0x3C1F1510, 0x37FF0000, 0x03E0F809,
                 0, 0x8FBF0014, 0x03E00008, 0x27BD0018]
        model = DispatchOracle(words, memory, buffer)
        model.r[4] = buffer
        model.run()
        self.assertEqual(model.calls, [(ORDINARY, buffer)])

    def test_production_source_and_slot_have_no_overflow_or_guards(self):
        source = (self.root / 'conker/src/game_6D800.c').read_text()
        body = re.search(r'void func_15040CC8\(u8 \*arg0\) \{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body.replace('    /* Inhibit pointer strength reduction without emitting a divide. */\n', ''),
                         screen.SELECTED)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                     'mips-linux-gnu-objdump')
        self.assertEqual(functions['func_15040CC8'], self.retail)
        self.assertNotIn('__retail_overflow_func_15040CC8', functions)
        self.assertEqual(addresses['func_15040D60'], 0x15040D60)
        self.assertIn('void func_15040CC8(u8 *arg0);', (self.root / 'conker/include/functions.h').read_text())
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse(any(r['function'] == 'func_15040CC8' for r in csv.DictReader(stream)))


if __name__ == '__main__':
    unittest.main()
