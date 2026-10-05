"""Reproduce the source-only frame screen and protect the surrounding slots."""

import hashlib
import json
import shutil
import struct
import subprocess
import sys
import unittest
from pathlib import Path

from tools.match_progress import load_elf_functions


class GameImmediateReleaseFrameTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(name) is None for name in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools are unavailable')
        result = subprocess.run([sys.executable, '-m',
            'tools.experiments.game_immediate_release_frame_candidates'], cwd=cls.root,
            capture_output=True, text=True, timeout=120)
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        cls.output = cls.root / 'conker/build/game-immediate-release-frame'
        cls.records = json.loads((cls.output / 'screen.json').read_text())

    def test_screen_reproduces_old_frame_and_unmodified_exact_candidate(self):
        self.assertEqual(len(self.records), 51)
        self.assertEqual(len({row['name'] for row in self.records}), 51)
        baseline = next(row for row in self.records if row['name'] == 'baseline')
        self.assertEqual((baseline['body_words'], baseline['frame'], baseline['real_differences']),
                         (46, 0x38, 4))
        self.assertEqual(baseline['differences'],
            [[0, '27BDFFC8', '27BDFFD8'], [0x68, 'AFA50038', 'AFA50028'],
             [0x6C, '8FA50038', '8FA50028'], [0xAC, '27BD0038', '27BD0028']])
        matches = [row for row in self.records if row['real_differences'] == 0]
        self.assertEqual([row['name'] for row in matches], ['inline-priority-inline-activity-both'])
        self.assertEqual((matches[0]['body_words'], matches[0]['frame']), (46, 0x28))
        self.assertEqual(matches[0]['diagnostics'], '')
        candidate = (self.output / (matches[0]['name'] + '.c')).read_text()
        source = (self.root / 'conker/src/game/generated_139FC0.c').read_text()
        body = candidate[candidate.index('void func_1510D7AC'):].strip()
        self.assertIn(body, source)

    def test_frame_shrinking_alone_does_not_prove_a_match(self):
        by_name = {row['name']: row for row in self.records}
        for name, frame, different in (('inline-count-cache', 0x30, 4),
                                        ('inline-activity-both', 0x28, 6),
                                        ('inline-priority-inline-count-cache', 0x28, 6)):
            row = by_name[name]
            self.assertEqual((row['body_words'], row['frame'], row['real_differences']),
                             (46, frame, different))

    def test_neighboring_maintenance_and_queue_slots_keep_bytes_and_addresses(self):
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                    'mips-linux-gnu-objdump')
        checkpoints = {
            'func_1510D694': '14b2c699b48bf4376cc3f16817191178ab21579419ba72f7755cf4ee0895d309',
            'func_1510D720': '291ebfdf97818a363db055caf102d3c63d6c9470df7db1bc76e7479705857527',
            'func_1510D864': 'e81b7668246b58e182518ea12697cbf47014a01b764ea1a2dc2f1e8ce2d55a31',
            'func_1510D874': '5ca5af947408d6055c1fdf4ce2c517d915c75c052975430b17056b22969beffb',
            'func_1510D8C0': 'f3a227545fc8d35dd017430e12f6fd1da0512c5746e400423358eee3a9566feb',
        }
        for name, digest in checkpoints.items():
            self.assertEqual(addresses[name], int(name[5:], 16))
            words = functions[name]
            self.assertEqual(hashlib.sha256(struct.pack('>' + str(len(words)) + 'I', *words)).hexdigest(),
                             digest, name)


if __name__ == '__main__':
    unittest.main()
