"""Bind the recovered private homes to both source and the live linked slot."""

import shutil
import struct
import unittest
from pathlib import Path

from tools.experiments import game_actor_triangle_home_candidates as home
from tools.experiments import game_actor_triangle_transform_candidates as screen
from tools.match_progress import load_elf_functions


class GameActorTriangleHomeCandidateTests(unittest.TestCase):
    def test_inventories_bind_to_frozen_recovery_and_selected_body(self):
        forms, loops = home.candidates(), home.loop_candidates()
        self.assertEqual((len(forms), len(loops)), (25, 11))
        self.assertEqual(len({name for name, _ in forms}), 25)
        self.assertEqual(len({name for name, _ in loops}), 11)
        self.assertEqual(forms[0], ('checkpoint', screen.RECOVERY))
        self.assertEqual(dict(forms)['weights-counters-retail-cut-10'], screen.HOME_RECOVERY)
        commands = screen.RECOVERY.split('    id = actor->id;', 1)[1]
        for name, body in forms:
            with self.subTest(name=name):
                self.assertEqual(body.split('    id = actor->id;', 1)[1], commands)
                self.assertEqual(body.count('func_150A7960('), 1)
                self.assertIn('ActorVertex58F80 *vertices[3];', body)
                self.assertIn('f32 points[6][3];', body)

    def test_home_rewriter_fails_closed_on_missing_or_changed_declarations(self):
        with self.assertRaises(ValueError):
            screen.retail_home_body('void missing_source(void) {}')
        with self.assertRaises(ValueError):
            screen.retail_home_body(screen.RECOVERY.replace('    u32 *matrix;', '    u8 *matrix;'))

    def test_live_private_arrays_have_all_retail_homes(self):
        if shutil.which('mips-linux-gnu-objdump') is None:
            self.skipTest('MIPS objdump unavailable')
        root = Path(__file__).resolve().parents[2]
        retail = list(struct.unpack_from('>302I', (root / 'conker/conker.us.bin').read_bytes(), 0x5C940))
        production = load_elf_functions(str(root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]['func_1502F490']
        expected = dict(vertices=[0xF4], matrices=[0x114],
                        points=[0xAC, 0xB8, 0xC4, 0xD0, 0xDC, 0xE8],
                        edgeA=[0x94], edgeB=[0x7C], relative_blend=[0x120, 0x12C])
        self.assertEqual(home.homes(retail, 0x138), expected)
        self.assertEqual(production[0], 0x27BDFEC0)
        self.assertEqual(home.homes(production, 0x140), expected)


if __name__ == '__main__':
    unittest.main()
