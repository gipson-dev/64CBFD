"""Keep source-only scope/plane/operand screens bounded and fail closed."""

import unittest
from unittest.mock import patch

from tools.experiments import game_graph_edge_crossing_lifetimes as previous
from tools.experiments import game_graph_edge_crossing_scopes as screen


class GameGraphEdgeCrossingScopeTests(unittest.TestCase):
    def test_frozen_checkpoint_and_named_inventory(self):
        self.assertEqual(screen.CHECKPOINT, previous.SELECTED)
        counts = {'scopes': 15, 'planes': 14, 'aggregates': 8, 'sums': 32, 'products': 32}
        names = []
        for mode, make_forms in screen.SCREENS.items():
            forms = make_forms()
            self.assertEqual(len(forms), counts[mode])
            self.assertEqual(len(dict(forms)), len(forms))
            names.extend(name for name, _ in forms)
        self.assertEqual((len(names), len(set(names))), (101, 101))

    def test_product_rewriter_preserves_identifier_boundaries(self):
        forms = dict(screen.operand_candidates(True))
        query = forms['products-1']
        self.assertIn('start = nx * x + nz * z + constant;', query)
        self.assertIn('constant = -(ax * nx + nz * az);', query)
        self.assertIn('a = cross_x * nx + cross_z * nz + constant;', query)
        plane = forms['products-16']
        self.assertEqual(plane.count('nx * ax'), 2)
        self.assertIn('start = x * nx + z * nz + constant;', plane)
        with patch.object(screen, 'CHECKPOINT', screen.CHECKPOINT.replace('x * nx', 'x / nx')):
            with self.assertRaisesRegex(ValueError, 'operand-product anchor'):
                screen.operand_candidates(True)

    def test_plane_and_aggregate_rewriters_protect_declarations_and_inputs(self):
        body = screen.separate(screen.CHECKPOINT, constant=True, normal=True, distances=True)
        self.assertIn('tangent_x = -nz;', body)
        self.assertIn('tangent_z = nx;', body)
        self.assertIn('crossing_distance = cross_x * tangent_x', body)
        self.assertIn('a / (a + b)', body)
        body = screen.aggregate(screen.CHECKPOINT, ('nx', 'nz', 'constant'), 'plane')
        self.assertIn('struct { f32 nx; f32 nz; f32 constant; } plane;', body)
        self.assertIn('plane.nx = ', body)
        self.assertNotIn('plane-aggregate-declaration', body)
        with self.assertRaises(ValueError):
            screen.scope('void missing(void) {}', ('nx',))
        with self.assertRaises(ValueError):
            screen.aggregate('void missing(void) {}', ('nx', 'nz'), 'plane')


if __name__ == '__main__':
    unittest.main()
