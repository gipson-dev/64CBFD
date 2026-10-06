"""Compiler-screen receipts and retained helper identity, not projection qualification."""

import re
import struct
import unittest
from pathlib import Path

from tools.experiments import game_projection_wrapper_candidates as screen
from tools.match_progress import load_elf_functions


class GameProjectionWrapperAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-projection-wrapper-audit'
        cls.output.mkdir(exist_ok=True)
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()

    def test_twenty_reproducible_compiler_controls(self):
        forms = screen.candidates()
        self.assertEqual(len(forms), 20)
        self.assertEqual(len({name for name, _ in forms}), 20)
        for index, (name, body) in enumerate(forms):
            with self.subTest(name=name):
                record, words = screen.compile_candidate(self.root, self.output, name, body)
                if index < 16:
                    count, differences = ((108, 104) if index & 9 == 9 else
                                          (105, 101) if index & 8 else
                                          (103, 95) if index & 1 else (101, 85))
                else:
                    count, differences = (102, 90) if index < 18 else (106, 94)
                self.assertEqual((record['body_words'], record['frame'], record['differences']),
                                 (count, 0x50, differences))
                self.assertFalse(record['exact'])
                self.assertEqual(record['diagnostics'], '')
                self.assertEqual(words[0], 0x27BDFFB0)

    def test_retained_matrix_trampoline_and_continuation(self):
        linked, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                  'mips-linux-gnu-objdump')
        for name, address, rom, count in (
                ('func_150A7960', 0x150A7960, 0xD4E10, 40),
                ('func_150A7A00', 0x150A7A00, 0xD4EB0, 5),
                ('func_150A7A14', 0x150A7A14, 0xD4EC4, 13)):
            with self.subTest(name=name):
                self.assertEqual(addresses[name], address)
                self.assertEqual(linked[name], list(struct.unpack_from('>%dI' % count, self.rom, rom)))
        self.assertEqual(linked['func_150A7A00'][0], 0x03E0C825)
        self.assertEqual(linked['func_150A7A14'][-2:], [0x03200008, 0xE5520000])

    def test_retail_frame_and_production_placeholder_remain_explicit(self):
        retail = struct.unpack_from('>101I', self.rom, screen.ROM)
        self.assertEqual(retail[0], 0x27BDFFB8)
        self.assertEqual(retail[-5:], (0x8FBF002C, 0x8FB00028, 0x27BD0048, 0x03E00008, 0))
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertRegex(source, r's32 func_15144CEC\(\)\s*\{\s*return 0;\s*\}')
        guards = (self.root / 'conker/retail_word_patches.us.csv').read_text()
        self.assertIsNone(re.search(r'^.*func_15144CEC.*$', guards, re.MULTILINE))


if __name__ == '__main__':
    unittest.main()
