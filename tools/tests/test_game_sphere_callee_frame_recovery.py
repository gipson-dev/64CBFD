"""Full retained/trial frame footprints and naturally overwritten helper homes."""

import itertools
import shutil
import struct
import unittest
from pathlib import Path

from tools.experiments import game_sphere_callee_candidates as screen
from tools.experiments import game_sphere_callee_layout_candidates as controls
from tools.tests import game_sphere_frame_reference as frame_reference
from tools.tests.test_game_sphere_wrapper_match import (
    CENTERS, POINTS, STACK, SphereOracle, bits, external, fixture, floating, peek,
)


class GameSphereCalleeFrameRecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or shutil.which('mips-linux-gnu-ld') is None:
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.out = cls.root / 'conker/build/game-sphere-callee-frame-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.trial = screen.compile_candidate(cls.root, cls.out, 'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>126I', rom, screen.ROM))
        dot = list(struct.unpack_from('>13I', rom, screen.DOT_ROM))
        cls.connected = dict(zip(range(screen.DOT, screen.DOT + len(dot) * 4, 4), dot))

    def check(self, memory, args, phase=0):
        models = []
        for words, layout in ((self.retail, frame_reference.RETAIL), (self.trial, frame_reference.TRIAL)):
            expected, writes, status, dot = frame_reference.reference(memory, args, phase, layout)
            model = SphereOracle(words, memory, args, self.connected, phase, entry=screen.ENTRY).run()
            self.assertEqual(model.r[2], status)
            self.assertEqual(model.memory, expected)
            self.assertEqual([e for e in model.events if e[0] == 'W'], writes)
            self.assertEqual(model.calls, [] if dot is None else [(screen.DOT, *dot)])
            models.append(model)
        return models

    def test_external_aliases_now_include_complete_private_memory_and_write_order(self):
        count = 0
        for center, radius, layout, phase in itertools.product(
                CENTERS, (0.0, 0.25, 1.0, -1.0, 2.0, 8.0), range(13), (0, 8)):
            memory, args = fixture(center, radius, 4.0, layout, phase)
            models = self.check(memory, (*args[:4], *args[5:]), phase)
            self.assertEqual(external(models[0].memory), external(models[1].memory))
            count += 1
        self.assertEqual(count, 1404)

    def test_private_output_windows_and_incoming_homes_have_layout_specific_results(self):
        offsets = (*range(0x1C, 0x70, 4), 0x70, 0x7C, 0x80, 0x84, 0x88, 0x8C)
        self.assertEqual(len(offsets), 27)
        count, different = 0, 0
        for offset, output, center, radius, phase in itertools.product(
                offsets, range(4), (CENTERS[0], CENTERS[1], CENTERS[5]), (1.0, 2.0), (0, 8)):
            memory, wrapper_args = fixture(center, radius, phase=phase)
            for number in (0.0, *range(3, 8), *range(-7, -2)):
                memory.update({bits(number) + i: 0xA5 for i in range(16)})
            args = list((*wrapper_args[:4], *wrapper_args[5:]))
            args[4 + output] = STACK + phase - 0x70 + offset
            models = self.check(memory, args, phase)
            different += external(models[0].memory) != external(models[1].memory)
            count += 1
        self.assertEqual(count, 1296)
        self.assertGreater(different, 0)

    def test_original_counterexample_is_explained_by_live_private_copy_reads(self):
        memory, wrapper_args = fixture()
        args = list((*wrapper_args[:4], *wrapper_args[5:]))
        args[4] = STACK - 0x70 + 0x58
        original, trial = self.check(memory, args)
        self.assertEqual(floating(peek(original.memory, POINTS + 64)), 24.0)
        self.assertEqual(floating(peek(trial.memory, POINTS + 64)), 10.0)
        self.assertNotEqual(floating(peek(original.memory, POINTS + 64)), 6.0)

    def test_late_distance_pointer_home_and_early_point_pointer_lifetimes(self):
        memory, wrapper_args = fixture()
        args = list((*wrapper_args[:4], *wrapper_args[5:]))
        args[4] = STACK + 0x14
        for address in (0, bits(4.0)):
            memory.update({address + i: 0xA5 for i in range(16)})
        models = self.check(memory, args)
        for model in models:
            self.assertEqual(floating(peek(model.memory, POINTS + 64)), 6.0)
            self.assertEqual(floating(peek(model.memory, 0)), 6.0)
            self.assertEqual([event for event in model.events if event[0] == 'W' and event[1] == 0],
                             [('W', 0, 4, bits(4.0)), ('W', 0, 4, bits(6.0))])

    def test_missing_private_snapshot_and_late_scalar_target_fail_closed(self):
        for words, layout in ((self.retail, frame_reference.RETAIL), (self.trial, frame_reference.TRIAL)):
            for address in (STACK - 0x70 + layout.direction, STACK + 0x18):
                memory, wrapper_args = fixture()
                args = list((*wrapper_args[:4], *wrapper_args[5:]))
                if address == STACK + 0x18:
                    args[4] = address
                    address = bits(4.0)
                    memory.update({i: 0xA5 for i in range(16)})
                for i in range(4):
                    memory.pop(address + i, None)
                with self.assertRaisesRegex(AssertionError, 'unmapped'):
                    SphereOracle(words, memory, args, self.connected, entry=screen.ENTRY).run()

    def test_meaningful_layout_controls_do_not_recover_the_private_slots(self):
        candidates = {n: (b, p) for n, b, p in controls.candidates()}
        self.assertEqual(len(candidates), 48)
        expected = {'workspace-r0-c0-g0-u0': (139, 96, 124),
                    'workspace-r0-c1-g1-u1': (144, 96, 137),
                    'types-c2-s1-g0': (126, 112, 60),
                    'types-c3-s2-g2': (132, 120, 128),
                    'initialized-u1-o2g3': (126, 112, 60),
                    'initialized-u1-o2': (126, 112, 80)}
        for name, wanted in expected.items():
            body, profile = candidates[name]
            record, _ = screen.compile_candidate(self.root, self.out, name, body, profile)
            self.assertEqual((record['body_words'], record['frame'], record['differences']), wanted)


if __name__ == '__main__':
    unittest.main()
