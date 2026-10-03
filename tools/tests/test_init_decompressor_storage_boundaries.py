import struct
import unittest

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_retail_pages as retail
from tools.tests import test_init_decompressor_tables as tables


class StorageAddressFixture(tables.BuilderFixture):
    """Bounded address arithmetic; CACHE records operands, not cache effects."""

    def __init__(self, code, input_address=None):
        super().__init__([])
        self.code = code
        self.cache_operands = []
        if input_address is not None:
            self.put(0x800354F8, input_address, 4)

    def execute(self, word):
        op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
        if op == 0 and word & 63 == 43:
            self.registers[(word >> 11) & 31] = int(
                self.registers[rs] < self.registers[rt])
            self.registers[0] = 0
        elif op == 14:
            self.registers[rt] = self.registers[rs] ^ (word & 0xFFFF)
            self.registers[0] = 0
        elif op == 47:
            base, operation = (word >> 21) & 31, (word >> 16) & 31
            offset = word & 0xFFFF
            if offset & 0x8000:
                offset -= 0x10000
            self.cache_operands.append((operation,
                (self.registers[base] + offset) & 0xFFFFFFFF))
        else:
            super().execute(word)


class InitDecompressorStorageBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        retail.InitDecompressorRetailPageTests.setUpClass.__func__(cls)

    def test_startup_page_table_transfer_ends_at_input_buffer(self):
        first, last = 0x10001318, 0x10001390
        expected = bytes.fromhex("""
            3C0E8003 25CE3330 25CF000F 3C0E1500 3C0D1520 25ADA130
            25CE0000 2403FFF0 01AE1023 01E3C024 24420FFF 3C018003
            3C198003 00027B02 AC3854F8 27392B30 25E60002 272B000F
            0006C080 3C098003 2706000F 252954FC 01632824 25EA0001
            34D9000F AD250000 3B26000F AFAA004C AFAA0028 26040004
        """)
        self.assertEqual(self.rom[first - 0x10000000:last - 0x10000000], expected)
        fixture = StorageAddressFixture({first + i * 4: word for i, (word,) in
                                         enumerate(struct.iter_unpack(">I", expected))})
        fixture.registers[16] = 0x42450
        fixture.run(entry=first, stop_pc=last, budget=64)
        self.assertEqual(fixture.get(0x800354F8, 4), retail.INPUT)
        table = fixture.get(0x800354FC, 4)
        self.assertEqual(table, 0x80032B30)
        self.assertEqual(fixture.registers[15], len(self.pages))
        self.assertEqual(fixture.registers[10], len(self.pages) + 1)
        self.assertEqual(fixture.registers[6], 2048)
        self.assertEqual(table + fixture.registers[6], retail.INPUT)
        self.assertEqual(retail.INPUT - (table + 4 * (len(self.pages) + 1)), 16)
        self.assertEqual(fixture.registers[4], 0x42454)
        self.assertEqual([address for address, _ in fixture.writes],
                         [0x800354F8, 0x800354FC, fixture.STACK + 0x4C, fixture.STACK + 0x28])

    def test_cache_loop_includes_endpoint_and_crosses_workspace(self):
        code = {pc: word for pc, word in contract.InitDecompressorContractTests.entries(
                "func_10005C2C") if 0x10005DEC <= pc < 0x10005E08}
        self.assertEqual(len(code), 7)
        for pc, word in code.items():
            self.assertEqual(struct.unpack_from(">I", self.rom, pc - 0x10000000)[0], word)
        fixture = StorageAddressFixture(code, retail.INPUT)
        fixture.run(entry=0x10005DEC, stop_pc=0x10005E08, budget=2048)
        self.assertEqual(fixture.cache_operands,
                         [(0x15, retail.INPUT + offset) for offset in range(0, 0x1001, 16)])
        self.assertEqual(len(fixture.cache_operands), 257)
        self.assertEqual(fixture.registers[8], retail.INPUT + 0x1010)
        self.assertEqual(fixture.writes, [])
        self.assertEqual(fixture.visits[0x10005DF8], 257)
        self.assertEqual(retail.INPUT + 0x1010 - retail.WORKSPACE, 600)
        maximum_dma = max((end - start + 15) & ~15
                          for _, start, end, _, _ in self.pages)
        self.assertEqual(maximum_dma, 3072)
        self.assertEqual(retail.WORKSPACE - retail.INPUT - maximum_dma, 440)
        print("storage boundary receipt: table=2048 dma_max=3072 dma_gap=440 "
              "cache_operands=257 cache_endpoint=0x80034330", flush=True)

    def test_local_unsigned_compare_and_xor_operations(self):
        fixture = StorageAddressFixture({})
        fixture.registers[8:10] = [0xFFFFFFF0, 1]
        fixture.execute(0x0109082B)
        self.assertEqual(fixture.registers[1], 0)
        fixture.registers[8:10] = [1, 0xFFFFFFF0]
        fixture.execute(0x0109082B)
        self.assertEqual(fixture.registers[1], 1)
        fixture.registers[25] = 0xABCDEF0F
        fixture.execute(0x3B26000F)
        self.assertEqual(fixture.registers[6], 0xABCDEF00)

    def test_output_page_index_uses_pool_not_static_workspace(self):
        code = {pc: word for pc, word in contract.InitDecompressorContractTests.entries(
                "func_10005C2C") if 0x10005CF4 <= pc < 0x10005D20}
        self.assertEqual(len(code), 11)
        for pc, word in code.items():
            self.assertEqual(struct.unpack_from(">I", self.rom, pc - 0x10000000)[0], word)
        pool, bitmap, count = 0x00100000, 0x80200000, 235
        for page in (0, 7, 8, count - 1):
            with self.subTest(page=page):
                fixture = StorageAddressFixture(code)
                address, bit = bitmap + page // 8, page & 7
                fixture.put(0x8003BE70, bitmap, 4)
                fixture.put(0x8003BE74, pool, 4)
                fixture.put(address, 0xFF, 1)
                fixture.registers[8:10] = [0xFF, address]
                fixture.registers[14:16] = [bit, 1 << bit]
                fixture.run(entry=0x10005CF4, stop_pc=0x10005D20, budget=32)
                self.assertEqual(fixture.registers[17], pool + page * 0x1000)
                self.assertLessEqual(fixture.registers[17] + 0x1000, pool + count * 0x1000)
                self.assertEqual(fixture.get(address, 1), 0xFF ^ (1 << bit))
                self.assertEqual(fixture.writes, [(address, 1)])


if __name__ == "__main__":
    unittest.main()
