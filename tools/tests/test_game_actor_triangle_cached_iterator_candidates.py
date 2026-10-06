"""Rejected cached-read controls must retain real array homes and bounded scope."""

import struct
import unittest
from pathlib import Path

from tools.experiments import game_actor_triangle_cached_iterator_candidates as cached
from tools.experiments import game_actor_triangle_transform_candidates as screen
from tools.experiments import game_actor_triangle_home_candidates as home
from tools.experiments import game_actor_triangle_frame_candidates as frame
from tools.experiments import game_actor_triangle_lifetime_candidates as lifetime


class GameActorTriangleCachedIteratorTests(unittest.TestCase):
    def test_frozen_inventories_and_original_capacities(self):
        groups = (cached.recipes(), cached.isolated_recipes(), cached.mixed_recipes())
        self.assertEqual(tuple(map(len, groups)), (32, 14, 32))
        forms = sum((list(group) for group in groups), [])
        self.assertEqual(len({name for name, _, _ in forms}), 78)
        self.assertEqual(cached.CHECKPOINT, screen.SELECTED)
        for name, body, variables in forms:
            with self.subTest(name=name):
                placed = cached.declarations(body, variables, 0)
                self.assertIn('ActorVertex58F80 *vertices[3];', placed)
                self.assertIn('f32 points[6][3];', placed)
                self.assertIn('id = actor->id;', placed)
                self.assertIn('count = D_800C5EF8[id];', placed)
                self.assertEqual(placed.count('func_150A7960('), 1)
                self.assertEqual(placed.count('= -100.0f;'), 2)
                self.assertNotIn('weightA + weightB', placed)

    def test_rewriters_fail_closed(self):
        _, body, variables = cached.recipes()[0]
        for cut in (-1, len(variables)):
            with self.assertRaises(ValueError):
                cached.declarations(body, variables, cut)
        with self.assertRaises(ValueError):
            cached.declarations(body.replace('id = actor->id;', 'id = 0;'), variables, 0)
        with self.assertRaises(ValueError):
            cached.isolate(body, variables, 8)
        with self.assertRaises(ValueError):
            cached.isolate(body.replace('matrix = D_800C6070[id];', 'matrix = NULL;'), variables, 1)

    def test_mixed_bounds_are_distinct_per_phase(self):
        for name, body, _ in cached.mixed_recipes():
            begin = body.index('    triangle = points;')
            self.assertIn('j < 3', body[:begin], name)
            self.assertNotIn('j != 3', body[:begin], name)
            self.assertIn('j != 3', body[begin:], name)
            self.assertNotIn('j < 3', body[begin:], name)

    def test_representative_compiler_receipts_and_cached_reads(self):
        root = Path(__file__).resolve().parents[2]
        output = root / 'conker/build/game-actor-triangle-cached-test'
        output.mkdir(exist_ok=True)
        rom = (root / 'conker/conker.us.bin').read_bytes()
        retail = list(struct.unpack_from('>302I', rom, 0x5C940))
        matrix = list(struct.unpack_from('>40I', rom, 0xD4E10))
        forms = {name: (body, variables) for name, body, variables in
                 cached.recipes() + cached.isolated_recipes() + cached.mixed_recipes()}
        for name, cut, expected in (
                ('xyz-counter-for-inner-less-edge-equal', 8, (302, 0x158, 204)),
                ('xyz-counter-separate-offsets-base', 10, (302, 0x160, 199)),
                ('xyz-counter-do-mixed-edge-equal-offsets-base', 10, (306, 0x160, 281))):
            with self.subTest(name=name):
                body, variables = forms[name]
                record, words = screen.compile_candidate(root, output, name,
                                                         cached.declarations(body, variables, cut))
                self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
                self.assertEqual(record['diagnostics'], '')
                self.assertEqual(home.homes(words, record['frame']), home.homes(retail, 0x138))
                self.assertEqual(frame.lifetime_trace(words, record['frame']),
                                 frame.lifetime_trace(retail, 0x138))
                if record['body_words'] <= 302:
                    self.assertEqual(lifetime.qualify(words, retail, matrix), 66)


if __name__ == '__main__':
    unittest.main()
