"""Matcher disassembly parsing keeps local jump targets in their function."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from match_progress import parse_elf_disassembly


class ElfDisassemblyTests(unittest.TestCase):
    def test_local_label_does_not_split_function(self):
        funcs, symbols, addresses = parse_elf_disassembly("""
1502db20 <func_1502DB20>:
1502db20: 2881003c  slti at,a0,60
1502db24: 14200009  bnez at,1502db4c
1502db54 <.L1502DB54_game_data>:
1502db54: 00047840  sll t7,a0,0x1
1502db58: 3c02800c  lui v0,0x800c
1502db84 <func_1502DB84>:
1502db84: 03e00008  jr ra
""")
        self.assertEqual(
            funcs["func_1502DB20"],
            [0x2881003C, 0x14200009, 0x00047840, 0x3C02800C],
        )
        self.assertEqual(funcs["func_1502DB84"], [0x03E00008])
        self.assertEqual(symbols[0x1502DB54], ".L1502DB54_game_data")
        self.assertNotIn(".L1502DB54_game_data", addresses)


if __name__ == "__main__":
    unittest.main()
