"""Keep lifetime controls bounded and fail closed as their source anchors evolve."""

import re
import unittest
from pathlib import Path

from tools.experiments import game_actor_triangle_lifetime_candidates as lifetime
from tools.experiments import game_actor_triangle_transform_candidates as recovery


class GameActorTriangleLifetimeCandidateTests(unittest.TestCase):
    def test_inventory_preserves_one_transform_and_sdk_call(self):
        forms = lifetime.candidates()
        self.assertEqual(len(forms), 34)
        self.assertEqual(len({name for name, _ in forms}), 34)
        self.assertEqual(forms[0], ('checkpoint', recovery.SELECTED))
        for name, body in forms:
            with self.subTest(name=name):
                self.assertTrue(body.startswith('void func_1502F490('))
                self.assertEqual(body.count('func_150A7960('), 1)
                self.assertNotIn('return 0;', body)
                self.assertIn('*x +=', body)
                self.assertIn('*y +=', body)
                self.assertIn('*z +=', body)

    def test_source_rewriters_and_weight_modes_fail_closed(self):
        for transform in (lifetime.reuse, lifetime.scoped, lifetime.range_loop,
                          lifetime.edge_pointers, lifetime.direct_metadata,
                          lifetime.indexed_vertices, lifetime.phase_blocks,
                          lifetime.ternary_weights, lifetime.short_metadata):
            with self.subTest(transform=transform.__name__):
                with self.assertRaises(ValueError):
                    transform('void missing_source(void) {}')
        with self.assertRaises(ValueError):
            lifetime.nonzero_weights(recovery.SELECTED, 'unknown')

    def test_production_source_remains_the_qualified_checkpoint(self):
        root = Path(__file__).resolve().parents[2]
        source = (root / 'conker/src/game/generated_58F80.c').read_text()
        body = re.search(r'void func_1502F490\([^;{}]+\) \{\n.*?\n\}', source, re.S)
        self.assertIsNotNone(body)
        self.assertEqual(body.group(), recovery.SELECTED)


if __name__ == '__main__':
    unittest.main()
