"""Block-loader direct IDO match and reproducible source-shape controls."""

import csv
import hashlib
import re
import shutil
import struct
import unittest
from pathlib import Path

from tools.experiments import game_block_loader_candidates as screen
from tools.match_progress import load_elf_functions


class GameBlockLoaderDirectMatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(name) is None for name in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-block-loader-test'
        cls.output.mkdir(exist_ok=True)
        cls.forms = dict(screen.candidates())
        cls.source = re.search(r'void \*func_1502B350\([^;{}]+\) \{\n.*?\n\}',
                              (cls.root / 'conker/src/game_57FA0.c').read_text(), re.S).group(0)
        cls.record, cls.words = screen.compile_candidate(
            cls.root, cls.output, 'production', cls.source, 'o2g3')
        cls.retail = list(struct.unpack_from('>86I',
            (cls.root / 'conker/conker.us.bin').read_bytes(), 0x58800))

    def test_complete_slot_emits_directly_from_default_profile(self):
        self.assertEqual(self.source, self.forms['nested-one-size-no-register'])
        self.assertEqual((self.record['body_words'], self.record['frame'],
                          self.record['real_differences']), (86, 0x30, 0))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(hashlib.sha256(struct.pack('>86I', *self.words)).hexdigest(),
                         'f176b2891cb5a8aa6f60461047ea78f4b4e7958fcaef18fb41b9d0c1ccdc31ae')

    def test_baseline_and_separate_size_remain_rejection_controls(self):
        for name, expected in (('baseline', (77, 0x38, 78)),
                               ('nested-no-register', (86, 0x38, 22))):
            with self.subTest(name=name):
                record, words = screen.compile_candidate(
                    self.root, self.output, name, self.forms[name], 'o2g3')
                self.assertEqual((record['body_words'], record['frame'],
                                  record['real_differences']), expected)
                self.assertEqual(record['diagnostics'], '')
                self.assertNotEqual(words, self.retail)
                if name == 'baseline':
                    self.assertEqual(hashlib.sha256(struct.pack('>86I', *words)).hexdigest(),
                        '17346d32c5e8ee8010b24eaf718d6d34eb9a1e802ee61ec8f2f226d3d3825ab4')

    def test_register_hint_is_not_needed_for_the_match(self):
        record, words = screen.compile_candidate(
            self.root, self.output, 'register-result', self.forms['nested-one-size'], 'o2g3')
        self.assertEqual(record['diagnostics'], '')
        self.assertEqual((record['body_words'], record['frame'],
                          record['real_differences']), (86, 0x30, 0))
        self.assertEqual(words, self.words)

    def test_production_slot_and_resource_neighbors_stay_exact(self):
        functions, _, addresses = load_elf_functions(
            str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502B350'], 0x1502B350)
        self.assertEqual(functions['func_1502B350'], self.words)
        for name, size, digest in (
                ('func_1502B4A8', 72, 'a07f71a50c44c47daf0edd894105db8a482bf2e3ff105109148e8c807164944f'),
                ('func_1502B6BC', 77, '40ead79430624c623749d0a0b9319470f3c925d306da179f6eb908c4828b3fe1')):
            self.assertEqual(len(functions[name]), size)
            self.assertEqual(hashlib.sha256(struct.pack('>'+str(size)+'I', *functions[name])).hexdigest(),
                             digest)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] == 'func_1502B350' for row in csv.DictReader(source)))


if __name__ == '__main__':
    unittest.main()
