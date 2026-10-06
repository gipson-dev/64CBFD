"""Bind the frame screen, frozen controls, and selected typed reuse body."""

import shutil
import struct
import unittest
from pathlib import Path

from tools.experiments import game_actor_triangle_frame_candidates as frame
from tools.experiments import game_actor_triangle_home_candidates as home
from tools.experiments import game_actor_triangle_transform_candidates as screen
from tools.match_progress import load_elf_functions


class GameActorTriangleFrameCandidateTests(unittest.TestCase):
    def test_inventories_and_selected_body(self):
        scopes, reused = frame.candidates(), frame.reuse_candidates()
        self.assertEqual((len(scopes), len(reused)), (29, 48))
        self.assertEqual(len({name for name, _ in scopes + reused}), 77)
        self.assertEqual(scopes[0], ('checkpoint', screen.HOME_RECOVERY))
        self.assertEqual(dict(reused)['direct-id-count-for-less-cut-2'], screen.SELECTED)
        for name, body in scopes + reused:
            with self.subTest(name=name):
                self.assertEqual(body.count('func_150A7960('), 1)
                self.assertIn('ActorVertex58F80 *vertices[3];', body)
                self.assertIn('f32 points[6][3];', body)
                self.assertEqual(body.count('= -100.0f;'), 2)
                self.assertNotIn('weightA + weightB', body)

    def test_scope_controls_preserve_operation_sequence(self):
        declarations = {declaration for _, declaration in home.SCALARS}

        def operations(body):
            commands = body[body.index('id = actor->id;'):]
            return [line.strip() for line in commands.splitlines()
                    if line.strip() and line.strip() not in declarations | {'{', '}'}]

        expected = operations(frame.CHECKPOINT)
        for name, body in frame.candidates():
            with self.subTest(name=name):
                self.assertEqual(operations(body), expected)

    def test_rewriters_fail_closed(self):
        with self.assertRaises(ValueError):
            frame.scoped_homes(frame.CHECKPOINT.replace('s32 count;', 'u32 count;'), ('range',))
        with self.assertRaises(ValueError):
            frame.scoped_homes(frame.CHECKPOINT, ('unknown',))
        with self.assertRaises(ValueError):
            frame.scoped_homes(frame.CHECKPOINT, ('sdk', 'sdk'))
        with self.assertRaises(ValueError):
            screen.reduced_frame_body(screen.RECOVERY.replace('vertices[3]', 'vertices[8]', 1))

    def test_selected_source_is_typed_reuse_without_pointer_punning(self):
        root = Path(__file__).resolve().parents[2]
        self.assertEqual((root / 'conker/src/game/generated_58F80.c').read_text().count(screen.SELECTED), 1)
        self.assertNotIn('((ActorRange58F80 *)point)', screen.SELECTED)
        self.assertNotIn('s32 id', screen.SELECTED)
        self.assertNotIn('s32 count', screen.SELECTED)
        self.assertIn('ActorRange58F80 *range;', screen.SELECTED)
        self.assertIn('i == D_800C5EF8[actor->id]', screen.SELECTED)
        self.assertIn('triangle < points + 6', screen.SELECTED)

    def test_live_read_mismatch_and_private_array_identity_are_explicit(self):
        if shutil.which('mips-linux-gnu-objdump') is None:
            self.skipTest('MIPS objdump unavailable')
        root = Path(__file__).resolve().parents[2]
        retail = list(struct.unpack_from('>302I', (root / 'conker/conker.us.bin').read_bytes(), 0x5C940))
        production = load_elf_functions(str(root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]['func_1502F490']
        original = frame.lifetime_trace(retail, 0x138)
        installed = frame.lifetime_trace(production, 0x140)
        self.assertEqual((original['pre_sdk_id_reads'], original['pre_sdk_count_reads']), (1, 1))
        self.assertEqual((installed['pre_sdk_id_reads'], installed['pre_sdk_count_reads']), (10, 3))
        self.assertEqual(original['private_y'], {'relative': [5.5, 1.25], 'blend': [1.25]})
        self.assertEqual(installed['private_y'], original['private_y'])


if __name__ == '__main__':
    unittest.main()
