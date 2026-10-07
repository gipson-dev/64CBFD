"""Bounded semantic recovery; private-frame mismatch forbids installation."""

import csv
import itertools
import shutil
import struct
import unittest
from pathlib import Path

from tools.experiments import game_sphere_callee_candidates as screen
from tools.experiments import game_sphere_wrapper_candidates as prior
from tools.match_progress import load_elf_functions
from tools.tests.test_game_sphere_wrapper_match import (
    CENTERS, DIRECTION, DISTANCES, ORIGIN, POINTS, STACK, SphereOracle,
    bits, external, fixture, floating, peek, private, put, reference,
)


class GameSphereCalleeRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or shutil.which('mips-linux-gnu-ld') is None:
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-sphere-callee-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.trial = screen.compile_candidate(cls.root, cls.output, 'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>126I', rom, screen.ROM))
        cls.wrapper = list(struct.unpack_from('>53I', rom, prior.ROM))
        cls.dot = list(struct.unpack_from('>13I', rom, screen.DOT_ROM))

    def execute(self, words, memory, args, phase=0):
        connected = dict(zip(range(screen.ENTRY, screen.ENTRY + len(words) * 4, 4), words))
        connected.update(zip(range(screen.DOT, screen.DOT + len(self.dot) * 4, 4), self.dot))
        return SphereOracle(self.wrapper, memory, args, connected, phase).run()

    def pair(self, memory, args, phase=0):
        expected, writes, status, _ = reference(memory, args, phase)
        result = []
        for words in (self.retail, self.trial):
            model = self.execute(words, memory, args, phase)
            self.assertEqual(model.r[2], status)
            self.assertEqual(external(model.memory), external(expected))
            self.assertEqual([e for e in model.events if e[0] == 'W' and not private(e[1])], writes)
            self.assertEqual(model.calls[0], (screen.ENTRY, *args[:4], *args[5:]))
            result.append(model)
        return result

    def test_selected_fit_and_reproducible_storage_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (126, 112, 60))
        self.assertEqual(self.record['relocations'], {0x1C0: [('R_MIPS_26', 'func_15144A74')]})
        self.assertEqual(self.record['diagnostics'], '')
        self.assertFalse(self.record['exact'])
        controls = dict(screen.candidates())
        self.assertEqual(len(controls), 64)
        self.assertEqual(controls['union1-member0-root0'], screen.SELECTED)
        expected = {'union0-member0-root0': (126, 104, 80),
                    'union0-member0-root1': (126, 112, 74),
                    'union1-member0-root1': (126, 112, 61),
                    'storage1-radius0-root0': (126, 112, 60),
                    'storage1-radius1-root0': (126, 104, 82)}
        for name, wanted in expected.items():
            record, _ = screen.compile_candidate(self.root, self.output, name, controls[name])
            self.assertEqual((record['body_words'], record['frame'], record['differences']), wanted)

    def test_finite_external_aliases_complete_storage_and_original_word_coverage(self):
        count, coverage = 0, set()
        for center, radius, layout, phase in itertools.product(
                CENTERS, (0.0, 0.25, 1.0, -1.0, 2.0, 8.0), range(13), (0, 8)):
            memory, args = fixture(center, radius, 4.0, layout, phase)
            models = self.pair(memory, args, phase)
            coverage.update(models[0].visits)
            count += 1
        self.assertEqual(count, 1404)
        for entry, words in ((screen.ENTRY, self.retail), (screen.DOT, self.dot)):
            self.assertTrue(set(range(entry, entry + len(words) * 4, 4)).issubset(coverage))

    def test_nonzero_origins_and_three_axis_directions(self):
        origins = ((1.0, -2.0, 0.5), (-0.25, 0.5, -1.0))
        directions = ((0.0, 1.0, 0.0), (0.0, 0.0, -1.0), (0.5, -0.5, 0.5))
        count = 0
        for origin, direction, center, radius, layout, phase in itertools.product(
                origins, directions, (CENTERS[0], CENTERS[2], CENTERS[6]), (0.25, 2.0, 8.0), range(13), (0, 8)):
            memory, args = fixture(center, radius, 4.0, layout, phase)
            for base, values in ((ORIGIN, origin), (DIRECTION, direction)):
                for i, value in enumerate(values):
                    put(memory, base + i * 4, bits(value))
            self.pair(memory, args, phase)
            count += 1
        self.assertEqual(count, 1404)

    def test_private_direction_slot_alias_is_a_measured_installation_blocker(self):
        for phase in (0, 8):
            memory, args = fixture(phase=phase)
            frame = STACK + phase - 0x28 - 0x70
            args = (*args[:5], frame + 0x58, *args[6:])
            retail = self.execute(self.retail, memory, args, phase)
            trial = self.execute(self.trial, memory, args, phase)
            self.assertEqual(floating(peek(retail.memory, POINTS + 64)), 24.0)
            self.assertEqual(floating(peek(trial.memory, POINTS + 64)), 10.0)
            self.assertNotEqual(external(retail.memory), external(trial.memory))
            self.assertEqual(retail.calls[-1], (screen.DOT, frame + 0x28, DIRECTION))
            self.assertEqual(trial.calls[-1], (screen.DOT, frame + 0x4C, DIRECTION))

    def test_miss_does_not_touch_unmapped_outputs(self):
        memory, args = fixture((5.0, 8.0, 0.0))
        for base, length in ((POINTS, 128), (DISTANCES, 32)):
            for byte in range(length):
                memory.pop(base + byte)
        models = self.pair(memory, args)
        self.assertTrue(all(model.r[2] == 0 and len(model.calls) == 1 for model in models))

    def test_compiled_stale_origin_and_direction_negatives_change_results(self):
        origin_body = screen.SELECTED
        for offset in (0, 4, 8):
            origin_body = origin_body.replace('arg4->unk%d - arg0->unk%d' % (offset, offset),
                                              'arg4->unk%d - origin.unk%d' % (offset, offset))
        direction_body = screen.SELECTED.replace('(f32 *)arg1) < 0.0f', 'direction.values) < 0.0f')
        for name, body, layout in (('stale-origin', origin_body, 2), ('stale-direction', direction_body, 4)):
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            memory, args = fixture(CENTERS[1], layout=layout)
            helper_args = (*args[:4], *args[5:])
            connected = dict(zip(range(screen.DOT, screen.DOT + len(self.dot) * 4, 4), self.dot))
            good = SphereOracle(self.retail, memory, helper_args, connected, entry=screen.ENTRY).run()
            bad = SphereOracle(words, memory, helper_args, connected, entry=screen.ENTRY).run()
            self.assertEqual((good.r[2], bad.r[2]), (1, 0), name)

    def test_production_retains_original_words_with_new_allocation_body(self):
        production = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        self.assertEqual(production[screen.FUNCTION], self.retail)
        self.assertEqual(production[prior.FUNCTION], self.wrapper)
        self.assertEqual(production['func_15144A74'], self.dot)
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        from tools.experiments import game_sphere_callee_allocation_candidates as allocation
        self.assertIn(allocation.SELECTED, source)
        self.assertNotIn(screen.SELECTED, source)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        self.assertEqual([row for row in guards if row['function'] == screen.FUNCTION], allocation.owner_guards())


if __name__ == '__main__':
    unittest.main()
