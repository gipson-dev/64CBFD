"""Raw resource-handoff schedule and the old pointer-allocation controls."""

import hashlib
import json
import re
import shutil
import struct
import subprocess
import sys
import unittest
from pathlib import Path

from tools.match_progress import load_elf_functions


class GameResourceHelperScheduleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(name) is None for name in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools are unavailable')
        result = subprocess.run([sys.executable, '-m',
            'tools.experiments.game_resource_helper_schedule_candidates'], cwd=cls.root,
            capture_output=True, text=True, timeout=120)
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        cls.output = cls.root / 'conker/build/game-resource-helper-schedule'
        cls.records = json.loads((cls.output / 'screen.json').read_text())

    def test_cast_screen_matches_both_word_forms_and_rejects_old_schedule(self):
        self.assertEqual(len(self.records), 19)
        self.assertEqual(len({row['name'] for row in self.records}), 19)
        by_name = {row['name']: row for row in self.records}
        for name, size, different in (('baseline', 45, 9), ('typed-top', 45, 11),
                                     ('char-cast', 45, 9), ('volatile-node', 46, 4)):
            row = by_name[name]
            self.assertEqual((row['body_words'], row['frame'], row['real_differences']),
                             (size, 0x30, different))
        matches = [row for row in self.records if row['real_differences'] == 0]
        self.assertEqual([row['name'] for row in matches], ['signed-cast', 'unsigned-cast'])
        for row in matches:
            self.assertEqual((row['body_words'], row['frame'], row['diagnostics']), (46, 0x30, ''))

    def test_unmodified_unsigned_candidate_and_production_match_entire_retail_slot(self):
        candidate = (self.output / 'unsigned-cast.c').read_text()
        source = (self.root / 'conker/src/game/generated_15F680.c').read_text()
        body = re.search(r's32 func_151336A8\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        body = body.replace('    /* Retail passes the resource address through a 32-bit word. */\n', '')
        self.assertEqual(candidate[candidate.index('s32 func_151336A8'):].strip(), body)
        fresh, _, addresses = load_elf_functions(str(self.output / 'unsigned-cast.elf'),
                                                'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_151336A8'], 0x151336A8)
        words = fresh['func_151336A8']
        self.assertEqual(words[46:], [0] * (len(words) - 46))
        packed = struct.pack('>46I', *words[:46])
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        self.assertEqual(packed, rom[0x160B58:0x160C10])
        self.assertEqual(hashlib.sha256(packed).hexdigest(),
                         'bcc5a75d799670a4fe870c852b34ab2a2162245941d52b98e5ba20e301106322')
        production, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                     'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_151336A8'], 0x151336A8)
        self.assertEqual(production['func_151336A8'], words[:46])

    def test_constructor_wrapper_and_adjacent_slots_keep_checkpoint_bytes(self):
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                    'mips-linux-gnu-objdump')
        checkpoints = {
            'func_1513264C': '8b6d14c3eb1958344cb8b6b07419aa58f7f376269bb1717182d3f8f879ee046a',
            'func_15132A4C': 'ffae9cfd67fff9633201e9af3484a65b32dbb9f1c3222dd9170fe0fc8d43ceeb',
            'func_15133510': '212f7aca0a9183382226942e0dfc15bbfd4c9606b7db86d79fa4b59e84d5381a',
            'func_15133588': 'e39ca4f5e490a2fe9630acb96522eeb348c560d69820cf5da6dd9f26e83d5073',
            'func_15133760': '2f32a09575c94a5c410e4972036f77aa1e3f26d4f43cbe8b57f824663f5b4809',
        }
        for name, digest in checkpoints.items():
            self.assertEqual(addresses[name], int(name[5:], 16))
            words = functions[name]
            self.assertEqual(hashlib.sha256(struct.pack('>' + str(len(words)) + 'I', *words)).hexdigest(),
                             digest, name)


if __name__ == '__main__':
    unittest.main()
