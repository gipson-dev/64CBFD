"""Bind the graph-edge lifetime screen to the frozen and improved source bodies."""

import hashlib
import struct
import unittest
from pathlib import Path

from tools.experiments import game_graph_edge_crossing_candidates as recovery
from tools.experiments import game_graph_edge_crossing_lifetimes as screen


class GameGraphEdgeCrossingLifetimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-graph-edge-lifetime-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = recovery.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        cls.old_record, cls.old_words = recovery.compile_candidate(cls.root, cls.output, 'checkpoint', screen.CHECKPOINT)
        cls.retail = list(struct.unpack_from('>207I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0xB4244))

    def test_screen_inventory_is_unique_and_checkpoint_remains_frozen(self):
        counts = {'layouts': 54, 'loops': 16, 'sides': 21, 'coordinates': 40,
                  'registers': 26, 'declarations': 31, 'parameters': 6, 'geometry': 15}
        names = []
        for mode, make_forms in screen.SCREENS.items():
            forms = make_forms()
            self.assertEqual(len(forms), counts[mode], mode)
            self.assertEqual(len(dict(forms)), len(forms), mode)
            names.extend(name for name, _ in forms)
        self.assertEqual((len(names), len(set(names))), (209, 209))
        self.assertEqual(screen.CHECKPOINT, dict(recovery.candidates())['reused-side-values'])
        self.assertEqual(recovery.SELECTED, screen.SELECTED)
        self.assertEqual(screen.SELECTED, dict(screen.geometry_candidates())['geometry-cross'])

    def test_complete_fitting_body_and_preserved_checkpoint_hash(self):
        self.assertEqual((self.record['body_words'], self.record['frame'],
                          self.record['real_differences'], self.record['diagnostics']), (207, 0x80, 102, ''))
        self.assertEqual((self.old_record['body_words'], self.old_record['frame'],
                          self.old_record['real_differences'], self.old_record['diagnostics']), (206, 0x78, 151, ''))
        old_slot = self.old_words + [0]
        self.assertEqual(hashlib.sha256(struct.pack('>207I', *old_slot)).hexdigest(),
                         '3bc4ecb9798225dd2b6f8cf921ec1bcd68467b62c38920374c373baf7087d1ad')
        self.assertEqual(self.words[-2:], [0x03E00008, 0x27BD0080])
        self.assertNotEqual(self.words, self.retail)

    def test_saved_register_prefix_and_complete_outer_loop_emit_directly(self):
        self.assertEqual(self.words[1:11], self.retail[1:11])
        self.assertEqual(self.words[0x2A8 // 4:0x2C4 // 4], self.retail[0x2A8 // 4:0x2C4 // 4])
        self.assertEqual([(i, w) for i, w in enumerate(self.words)
                          if w >> 26 == 33 and w & 65535 == 0x7290], [(16, 0x86317290)])
        self.assertIn('while (i < D_80087290)', screen.SELECTED)

    def test_pair_rewriter_preserves_member_declarations_and_rejects_missing_input(self):
        body = screen.pair(recovery.BASELINE, ('start', 'end'), 'side', ('start', 'end'))
        self.assertIn('struct { f32 start; f32 end; } side;', body)
        self.assertIn('side.start = x * nx', body)
        self.assertNotIn('paired-local-declaration', body)
        with self.assertRaises(ValueError):
            screen.pair('void missing(void) {}', ('start', 'end'), 'side', ('start', 'end'))


if __name__ == '__main__':
    unittest.main()
