import csv
import struct
import unittest
from pathlib import Path

from tools.tests import test_init_diagnostic_storage as storage
from tools.tests import test_init_decompressor_contract as contract


class InitGlyphAdoptionBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        storage.InitDiagnosticStorageTests.setUpClass()
        cls.root = Path(__file__).resolve().parents[2]
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.code = dict(contract.InitDecompressorContractTests.entries('func_10007DAC'))
        with (cls.root / 'conker/progress.init.csv').open(newline='') as source:
            cls.inventory = list(csv.DictReader(source))

    def test_diagnostic_formatter_sites_have_two_stack_regimes(self):
        sites = []
        for pc, word in self.code.items():
            self.assertEqual(word, struct.unpack_from('>I', self.rom, pc - 0x10000000)[0])
            if word >> 26 == 3:
                target = ((pc + 4) & 0xF0000000) | ((word & 0x3FFFFFF) << 2)
                if target in (0x10007C74, 0x10007CC4):
                    sites.append(pc)
        self.assertEqual([pc for pc in sites if pc < 0x10007F00],
                         [0x10007E18, 0x10007E3C, 0x10007E4C, 0x10007E5C,
                          0x10007E6C, 0x10007E7C, 0x10007E8C, 0x10007EA0, 0x10007EC0])
        self.assertEqual([pc for pc in sites if pc > 0x10007F00],
                         [0x10007F0C, 0x10007F60, 0x10007FAC,
                          0x10008048, 0x1000805C, 0x100080E8])
        self.assertEqual(self.code[0x10007F00], 0x00B1E821)
        for pc, word in self.code.items():
            if pc >= 0x10007F00:
                continue
            op, rt, rd = word >> 26, word >> 16 & 31, word >> 11 & 31
            writes_sp = (op in (8, 9, 15, 35) and rt == 29) or (op == 0 and rd == 29)
            self.assertFalse(writes_sp, hex(pc))

    def test_adapter_overlay_frame_inside_successful_pool_but_not_dma(self):
        audit = storage.InitDiagnosticStorageTests()
        for low in range(0, 0x10000, 0x2000):
            pool = 0x00100000 + low
            fixture = audit.placement(pool)
            base, top = fixture.registers[17], fixture.registers[29]
            frame = top - 56
            self.assertEqual((top - base, frame - base), (0x5958, 0x5920))
            self.assertEqual(frame - (base + 0x4960), 0xFC0)
            for count in range(107, 363):
                physical_low, physical_high = frame & 0x0FFFFFFF, top & 0x0FFFFFFF
                self.assertGreaterEqual(physical_low, pool)
                self.assertLessEqual(physical_high, pool + count * 0x1000)
            self.assertEqual(fixture.writes, [])

    def test_experimental_c_address_is_occupied_production_code(self):
        first, last = 0x10009000, 0x10009080
        owners = [row for row in self.inventory
                  if int(row['offset']) < last and int(row['offset']) + int(row['length']) > first]
        self.assertEqual([(row['function'], int(row['offset']), int(row['length']), row['language'])
                          for row in owners], [('func_10008F90', 0x10008F90, 1084, 'c')])
        self.assertNotEqual(self.rom[0x9000:0x9080], bytes(128))

    def test_adapter_slot_has_no_adjacent_free_extension(self):
        rows = {row['function']: row for row in self.inventory}
        leaf, syscall, diagnostic = (rows[name] for name in
                                    ('func_10007D28', 'func_10007DA0', 'func_10007DAC'))
        self.assertEqual((int(leaf['offset']), int(leaf['length'])), (0x10007D28, 120))
        self.assertEqual((int(syscall['offset']), int(syscall['length'])), (0x10007DA0, 12))
        self.assertEqual(int(diagnostic['offset']), 0x10007DAC)


if __name__ == '__main__':
    unittest.main()
