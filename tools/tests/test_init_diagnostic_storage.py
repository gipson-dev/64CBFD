import struct
import unittest

from tools.tests import test_init_decompressor_retail_pages as retail
from tools.tests import test_init_decompressor_contract as contract
from tools.tests.test_init_decompressor_storage_boundaries import StorageAddressFixture


class DiagnosticAddressFixture(StorageAddressFixture):
    def execute(self, word):
        if word >> 26 == 0 and word & 63 == 32:
            rs, rt, rd = word >> 21 & 31, word >> 16 & 31, word >> 11 & 31
            result = self.signed(self.registers[rs]) + self.signed(self.registers[rt])
            if not -0x80000000 <= result <= 0x7FFFFFFF:
                raise AssertionError("diagnostic ADD would overflow")
            self.registers[rd] = result & 0xFFFFFFFF
            self.registers[0] = 0
        else:
            super().execute(word)


class InitDiagnosticStorageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        retail.InitDecompressorRetailPageTests.setUpClass.__func__(cls)

    def slice(self, first, last):
        entries = dict(contract.InitDecompressorContractTests.entries("func_10007DAC"))
        code = {pc: entries[pc] for pc in range(first, last, 4)}
        for pc, word in code.items():
            self.assertEqual(struct.unpack_from(">I", self.rom, pc - 0x10000000)[0], word)
        return code

    def placement(self, pool):
        fixture = DiagnosticAddressFixture(self.slice(0x10007ED8, 0x10007F04))
        fixture.put(0x8003BE74, pool, 4)
        fixture.reads, fixture.writes = [], []
        fixture.run(entry=0x10007ED8, stop_pc=0x10007F04, budget=32)
        return fixture

    def test_all_pool_alignment_residues_place_at_next_64k_boundary(self):
        for low in range(0, 0x10000, 0x2000):
            with self.subTest(low=hex(low)):
                pool = 0x00100000 + low
                fixture = self.placement(pool)
                self.assertEqual(fixture.registers[17], 0x80110000)
                self.assertEqual(fixture.registers[29], 0x80115958)
                self.assertEqual(fixture.writes, [])
                delta = (fixture.registers[17] & 0x0FFFFFFF) - pool
                self.assertGreaterEqual(delta, 0x2000)
                self.assertLessEqual(delta + 0x5958, 107 * 0x1000)

    def test_debugger_dma_arguments_use_overlay_not_static_workspace(self):
        fixture = self.placement(0x0012E000)
        fixture.code = self.slice(0x10007F1C, 0x10007F40)
        fixture.run(entry=0x10007F1C, stop_pc=0x10007F40, budget=32)
        self.assertEqual(fixture.registers[4:8], [0, 0x19EA88, 0x80130000, 0x4960])
        self.assertLess(fixture.registers[6] + fixture.registers[7], fixture.registers[29])
        self.assertGreater(fixture.registers[6], retail.WORKSPACE)
        self.assertEqual(fixture.writes, [])

    def test_debugger_tlb_arguments_map_two_64k_halves_of_overlay(self):
        fixture = self.placement(0x0012E000)
        fixture.code = self.slice(0x10007FC8, 0x10008000)
        fixture.run(entry=0x10007FC8, stop_pc=0x10008000, budget=32)
        self.assertEqual(fixture.registers[4:8], [15, 0x1E000, 0x16000000, 0x00130000])
        self.assertEqual(fixture.get(fixture.registers[29] + 16, 4), 0x00140000)
        self.assertEqual(fixture.get(fixture.registers[29] + 20, 4), 0xFFFFFFFF)
        self.assertEqual(fixture.writes, [(0x80135950, 4), (0x80135954, 4)])

    def test_zero_or_tiny_pool_does_not_back_diagnostic_overlay(self):
        fixture = self.placement(0)
        self.assertEqual(fixture.registers[17], 0x80010000)
        self.assertLess(fixture.registers[17], 0x800E9D10)
        pool = 0x0012E000
        fixture = self.placement(pool)
        needed = (fixture.registers[29] & 0x0FFFFFFF) - pool
        self.assertEqual(needed, 0x7958)
        self.assertGreater(needed, 8)
        self.assertGreater(needed, 0x1000)

    def test_local_signed_add_overflow_rejected(self):
        fixture = DiagnosticAddressFixture({})
        fixture.registers[1:3] = [0x7FFFFFFF, 1]
        with self.assertRaisesRegex(AssertionError, "overflow"):
            fixture.execute((1 << 21) | (2 << 16) | (3 << 11) | 32)


if __name__ == "__main__":
    unittest.main()
