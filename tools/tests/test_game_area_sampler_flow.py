"""Uninstalled sampler flow evidence; public contract only across different CFGs."""

import itertools
import json
import struct
import unittest
from pathlib import Path

from tools.experiments import game_area_sampler_flow_candidates as flow
from tools.tests import test_game_area_sampler_recovery as prior
from tools.tests.test_game_point_transform_match import external_memory, put


class GameAreaSamplerFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-area-sampler-flow-test'
        cls.out.mkdir(exist_ok=True)
        cls.forms = []
        for name, body in flow.candidates():
            record, words = flow.prior.compile_candidate(cls.root, cls.out, name, body)
            record['ra_reloads'] = words.count(0x8FBF001C)
            cls.forms.append((name, body, record, words))
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>254I', rom, flow.prior.ROM))
        address, data = flow.prior.sections(cls.root / 'conker/build/conker.us.elf')['.game_data']
        cls.table = struct.unpack_from('>65I', data, prior.TABLE - address)
        cls.scale = struct.unpack_from('>I', data, prior.SCALE - address)[0]

    def receipt(self, name, value):
        (self.out / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def test_all_fifty_four_forms_keep_one_reload_and_no_exact_slot(self):
        self.assertEqual(len(self.forms), 54)
        self.assertEqual(self.retail.count(0x8FBF001C), 3)
        for name, _, record, _ in self.forms:
            self.assertEqual(record['ra_reloads'], 1, name)
            self.assertEqual(record['frame'], 80, name)
            self.assertEqual(record['profile'], 'o2g3', name)
            self.assertEqual(record['diagnostics'], '', name)
            self.assertEqual(record['pool_bytes'], 0, name)
            self.assertGreater(record['differences'], 0, name)
        records = [record for _, _, record, _ in self.forms]
        self.assertTrue(any(record['body_words'] == 254 for record in records))
        self.receipt('controls', dict(measurements=records, count=54, retail_reloads=3,
            candidate_reloads=1, exact=0, matching_count_is_not_sufficient=True))

    def test_every_flow_form_preserves_all_modes_live_fields_aliases_and_callbacks(self):
        count = 0
        for mode, values, phase, alias, mutate, random in itertools.product(
                (0, 1, 2, 3, 252, 253, 254, 255), prior.HALVES, (0, 8), range(4),
                (False, True), (0, 0x812345FF, 0x80000000)):
            memory, args = prior.fixture(self.table, self.scale, mode, values, alias=alias)
            expected, calls, writes = prior.reference(memory, args, random=random, mutate=mutate)
            for name, _, _, words in self.forms:
                model = prior.AreaOracle(words, memory, args, phase, random=random, mutate=mutate).run()
                self.assertEqual(external_memory(model.memory), external_memory(expected), name)
                self.assertEqual(model.calls, calls, name)
                self.assertEqual(prior.writes(model), writes, name)
                count += 1
        self.assertEqual(count, 82944)
        self.receipt('guest', dict(candidate_executions=count, input_fixtures=count // 54, forms=54,
            independent_reference=True, private_frames_or_traces_equal=False,
            random='bounded full-word values, including INT_MIN; unsigned shifted subtraction'))

    def test_every_flow_form_preserves_both_unsigned_conversion_stages_and_restore(self):
        count = 0
        angles = (0.0, -0.0, 0.5, -0.5, -0.999, 90.0, 359.5, 2**31, 2**32 - 512,
            2**32, 2**33, -1.0, -2**32, prior.math.inf, -prior.math.inf, prior.math.nan)
        for angle, fcsr in itertools.product(angles, (0, 4, 0x800000)):
            memory, args = prior.fixture(self.table, self.scale, 2, angle=angle)
            put(memory, prior.SCALE, prior.bits(1.0))
            expected, calls, writes = prior.reference(memory, args)
            for name, _, _, words in self.forms:
                model = prior.AreaOracle(words, memory, args, fcsr=fcsr).run()
                self.assertEqual(external_memory(model.memory), external_memory(expected), name)
                self.assertEqual(model.calls, calls, name)
                self.assertEqual(prior.writes(model), writes, name)
                count += 1
        self.assertEqual(count, 2592)
        self.receipt('conversion', dict(candidate_executions=count, fixtures=48, forms=54,
            both_stages=True, control_state_restored=True, model='bounded truncation/invalid bit only'))

    def test_production_sampler_stays_a_placeholder_without_guards(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn('s32 func_151432BC() {\n    return 0;\n}', source)
        for _, body, _, _ in self.forms:
            self.assertNotIn(body, source)
        self.assertNotIn('func_151432BC,', (self.root / 'conker/retail_word_patches.us.csv').read_text())


if __name__ == '__main__':
    unittest.main()
