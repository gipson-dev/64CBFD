"""Bind the independent lifetime screen and retain the earlier source controls."""

import unittest
from pathlib import Path

from tools.experiments import game_zone_neighbor_selection_candidates as recovery
from tools.experiments import game_zone_neighbor_selection_lifetimes as lifetime


class GameZoneNeighborSelectionLifetimeTests(unittest.TestCase):
    def test_inventory_preserves_the_query_and_helper_contract(self):
        inventories = (lifetime.candidates(), lifetime.cursor_candidates(), lifetime.register_candidates())
        self.assertEqual(tuple(map(len, inventories)), (52, 16, 23))
        for forms in inventories:
            self.assertEqual(len(forms), len(dict(forms)))
            for name, body in forms:
                with self.subTest(name=name):
                    self.assertEqual(body.count('NeighborVisitQueryB3020 query;'), 1)
                    self.assertEqual(body.count('func_15085DA8('), 1)
                    self.assertEqual(body.count('func_15085DF8('), 1)
                    self.assertEqual(body.count('func_1508B2A8('), 1)
                    self.assertEqual(body.count('bzero('), 1)
                    self.assertEqual(body.count('ready = 0;'), 1)
                    self.assertEqual(body.count('ready = 1;'), 1)
                    self.assertEqual(body.count('best != 0xFF'), 1)
                    self.assertIn('    *(s8 *)((u8 *)D_800D23B0 + 0x1745) = 0;', body)
                    self.assertNotIn('volatile', body)
                    self.assertNotIn('padding', body)
        self.assertEqual(dict(inventories[0])['retail-byte-cursors-context-for-loads-early'],
                         recovery.SELECTED)

    def test_source_rewriters_fail_closed(self):
        for transform in (lifetime.context_pointer, lifetime.guarded_actor,
                          lifetime.cached_coordinates, lifetime.deferred_zone):
            with self.subTest(transform=transform.__name__):
                with self.assertRaises(ValueError):
                    transform('void missing_source(void) {}')

    def test_checkpoint_and_oversized_controls_remain_explicit(self):
        root = Path(__file__).resolve().parents[2]
        output = root / 'conker/build/game-zone-neighbor-lifetimes-test'
        output.mkdir(exist_ok=True)
        controls = dict(lifetime.cursor_candidates())
        for name, body, expected in (
                ('checkpoint', recovery.CHECKPOINT, (367, 0x140, 340)),
                ('selected', recovery.SELECTED, (369, 0x140, 282)),
                ('oversized-word', controls['cursor-direct-distances-context-word'], (370, 0x140, 237)),
                ('oversized-byte', controls['cursor-direct-distances-context-byte'], (370, 0x140, 233))):
            with self.subTest(name=name):
                record, words = recovery.compile_candidate(root, output, name, body)
                self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
                self.assertEqual(len(words), expected[0])
                self.assertEqual(record['diagnostics'], '')


if __name__ == '__main__':
    unittest.main()
