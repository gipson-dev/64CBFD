import struct
import unittest

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_retail_pages as retail
from tools.tests import test_init_decompressor_storage_boundaries as boundaries


class PagePoolSetupFixture(boundaries.StorageAddressFixture):
    """Retail setup words with synthetic allocator returns and CP0 receipts."""

    def __init__(self, requested, previous, pool_returns, bitmap_return=0x800E9D1C):
        super().__init__(dict(contract.InitDecompressorContractTests.entries("func_10005B04")))
        self.pool_returns = iter(pool_returns)
        self.bitmap_return = bitmap_return
        self.allocations, self.cp0_writes = [], []
        self.put(0x8003BE78, previous, 2)
        self.put(0x8003BE74, 0x00120000, 4)
        self.put(0x8003BE70, 0x800E9D1C, 4)
        self.put(0x8003BE7C, 0x800E9D39, 4)
        self.registers[4] = requested
        self.code.update({0x10003C6C: 0x0000000D, 0x10003C70: 0x03E00008,
                          0x10003C74: 0, 0x10003C40: 0x0000004D,
                          0x10003C44: 0x03E00008, 0x10003C48: 0})

    def execute(self, word):
        op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
        if word in (0x0000000D, 0x0000004D):
            args = tuple(self.registers[4:8])
            if word == 0x0000000D:
                args += (self.get(self.registers[29] + 0x10, 4),)
                self.allocations.append(("pool", args))
                self.registers[2] = next(self.pool_returns, 0)
            else:
                self.allocations.append(("bitmap", args))
                self.registers[2] = self.bitmap_return
        elif op == 16 and rs == 4 and not word & 0x7FF:
            register = (word >> 11) & 31
            if register not in (4, 6):
                raise AssertionError("Only setup Context/Wired writes are recorded")
            self.cp0_writes.append((register, self.registers[rt]))
        elif op == 33:
            offset = word & 0xFFFF
            if offset & 0x8000:
                offset -= 0x10000
            value = self.get((self.registers[rs] + offset) & 0xFFFFFFFF, 2)
            self.registers[rt] = value if value < 0x8000 else value | 0xFFFF0000
        elif op == 0 and word & 63 == 3:
            value = self.signed(self.registers[rt]) >> ((word >> 6) & 31)
            self.registers[(word >> 11) & 31] = value & 0xFFFFFFFF
        else:
            super().execute(word)
        self.registers[0] = 0

    def setup(self, budget=1000):
        return self.run(entry=0x10005B04, budget=budget)


class InitPagePoolSetupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        retail.InitDecompressorRetailPageTests.setUpClass.__func__(cls)

    def test_setup_slot_matches_retail(self):
        words = contract.InitDecompressorContractTests.entries("func_10005B04")
        self.assertEqual([pc for pc, _ in words], list(range(0x10005B04, 0x10005BE0, 4)))
        self.assertEqual(b"".join(struct.pack(">I", word) for _, word in words),
                         self.rom[0x5B04:0x5BE0])

    def assert_return_contract(self, fixture, before):
        self.assertEqual(fixture.registers[16:24], before[16:24])
        self.assertEqual(fixture.registers[28:32], before[28:32])
        self.assertEqual(fixture.cp0_writes, [(4, 0), (6, 2)])
        self.assertEqual(fixture.get(0x8003BE80, 2), 0x1FC)
        self.assertEqual(fixture.get(0x8003BE82, 2), 0x3FF)

    def test_requested_pool_success(self):
        fixture = PagePoolSetupFixture(235, 107, [0x80300000])
        before = fixture.registers[:]
        fixture.setup()
        self.assertEqual(fixture.allocations,
                         [("pool", (235 << 12, 0xFF, 4, 1, 2)),
                          ("bitmap", (30, 0xFF, 0, 0))])
        self.assertEqual(fixture.get(0x8003BE78, 2), 235)
        self.assertEqual(fixture.get(0x8003BE74, 4), 0x00300000)
        self.assertEqual(fixture.get(0x8003BE7C, 4), 0x800E9D1C + 29)
        self.assert_return_contract(fixture, before)

    def test_failure_reallocates_previous_count(self):
        fixture = PagePoolSetupFixture(362, 235, [0, 0x80300000])
        before = fixture.registers[:]
        fixture.setup()
        self.assertEqual(fixture.allocations,
                         [("pool", (362 << 12, 0xFF, 4, 1, 2)),
                          ("pool", (235 << 12, 0xFF, 4, 1, 2)),
                          ("bitmap", (30, 0xFF, 0, 0))])
        self.assertEqual(fixture.get(0x8003BE78, 2), 235)
        self.assertEqual(fixture.get(0x8003BE74, 4), 0x00300000)
        self.assert_return_contract(fixture, before)

    def test_repeated_pool_failure_has_no_bounded_return(self):
        fixture = PagePoolSetupFixture(362, 235, [])
        with self.assertRaisesRegex(AssertionError, "instruction budget exhausted"):
            fixture.setup(budget=256)
        self.assertGreater(len(fixture.allocations), 2)
        self.assertEqual(fixture.allocations[0], ("pool", (362 << 12, 0xFF, 4, 1, 2)))
        self.assertTrue(all(call == ("pool", (235 << 12, 0xFF, 4, 1, 2))
                            for call in fixture.allocations[1:]))
        self.assertEqual(fixture.get(0x8003BE74, 4), 0x00120000)

    def test_zero_previous_count_fallback_then_bitmap_clear(self):
        fixture = PagePoolSetupFixture(235, 0, [0, 0x80300000])
        fixture.setup()
        self.assertEqual(fixture.allocations,
                         [("pool", (235 << 12, 0xFF, 4, 1, 2)),
                          ("pool", (0, 0xFF, 4, 1, 2)),
                          ("bitmap", (0, 0xFF, 0, 0))])
        self.assertEqual(fixture.get(0x8003BE78, 2), 0)
        start = fixture.get(0x8003BE70, 4)
        self.assertEqual(fixture.get(0x8003BE7C, 4), start - 1)
        fixture.code.update(contract.InitDecompressorContractTests.entries("func_10005BE0"))
        fixture.writes.clear()
        with self.assertRaisesRegex(AssertionError, "instruction budget exhausted"):
            fixture.run(entry=0x10005BE0, budget=128)
        self.assertEqual(fixture.writes[0], (start, 1))
        self.assertEqual(fixture.get(start, 1), 0xFF)

    def test_bitmap_zero_return_is_published_if_callee_returns(self):
        fixture = PagePoolSetupFixture(235, 107, [0x80300000], bitmap_return=0)
        fixture.setup()
        self.assertEqual(fixture.get(0x8003BE70, 4), 0)
        self.assertEqual(fixture.get(0x8003BE7C, 4), 29)

    def test_previous_count_is_loaded_signed(self):
        fixture = PagePoolSetupFixture(235, 0xFFFF, [0, 0x80300000])
        before = fixture.registers[:]
        fixture.setup()
        self.assertEqual(fixture.allocations,
                         [("pool", (235 << 12, 0xFF, 4, 1, 2)),
                          ("pool", (0xFFFFF000, 0xFF, 4, 1, 2)),
                          ("bitmap", (0, 0xFF, 0, 0))])
        self.assertEqual(fixture.get(0x8003BE78, 2), 0xFFFF)
        self.assert_return_contract(fixture, before)


if __name__ == "__main__":
    unittest.main()
