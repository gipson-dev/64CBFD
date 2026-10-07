"""Pool comparison must preserve targets and literal bytes while rebasing PCs."""

import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests.game_owner_pool import normalized_pools


class GameOwnerPoolTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name)
        self.number = 0

    def make_object(self, shift=0, target=4, literal=0x12345678, relocation=True, unsupported=False):
        self.number += 1
        source, obj = (self.path / ('owner%d%s' % (self.number, suffix)) for suffix in ('.s', '.o'))
        value = 'target+%d' % target if relocation else str(target)
        source.write_text('.text\n.space %d\n.type target,@function\ntarget:\n'
            '.word 0,0,0,0\n.size target,.-target\n.section .rodata\n.word %d\n' % (shift, literal)
            + ('.reloc .,R_MIPS_26,target\n.word 0\n' if unsupported else '.word %s\n' % value))
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(source)],
            check=True, capture_output=True)
        return obj

    def test_relocated_target_rebases_but_preserves_function_relative_identity(self):
        self.assertEqual(normalized_pools(self.make_object()), normalized_pools(self.make_object(shift=16)))

    def test_wrong_relative_target_literal_or_removed_relocation_is_detected(self):
        original = normalized_pools(self.make_object())
        for obj in (self.make_object(shift=16, target=8), self.make_object(literal=0x12345679),
                self.make_object(relocation=False)):
            self.assertNotEqual(original, normalized_pools(obj))

    def test_unsupported_relocation_and_unowned_target_fail_closed(self):
        for obj in (self.make_object(unsupported=True), self.make_object(target=32)):
            with self.assertRaises(ValueError):
                normalized_pools(obj)


if __name__ == '__main__':
    unittest.main()
