import re
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


class TableLoopFixture(StorageAddressFixture):
    def __init__(self, code, raw, address, count):
        self.write_interval = None
        super().__init__(code)
        self.table, self.payload = address, raw
        self.memory.update((address + i, byte) for i, byte in enumerate(raw))
        self.put(0x800354FC, address, 4)
        self.put(self.STACK + 0x28, count, 4)
        self.put(self.STACK + 0x4C, count, 4)
        self.registers[16] = 0x42450
        self.reads, self.writes = [], []
        self.write_interval = (address, address + count * 4)

    def put(self, address, value, size):
        if self.write_interval is not None:
            first, last = self.write_interval
            if not first <= address <= address + size <= last:
                raise AssertionError("table decode write exceeds declared word count")
        super().put(address, value, size)


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

    def table_loop_code(self):
        source = (contract.InitDecompressorContractTests.project /
                  "asm/nonmatchings/init_1050/func_10001194.s").read_text()
        entries = {int(pc, 16): int(word, 16) for pc, word in re.findall(
            r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+([0-9A-Fa-f]{8})\s*\*/", source)}
        code = {pc: entries[pc] for pc in range(0x10001398, 0x100013E4, 4)}
        self.assertEqual(len(code), 19)
        for pc, word in code.items():
            self.assertEqual(struct.unpack_from(">I", self.rom, pc - 0x10000000)[0], word)
        return code

    def test_all_retail_page_table_offsets_decode_without_tail_or_input_writes(self):
        table, count = 0x80032B30, len(self.pages) + 1
        self.assertEqual(count, 508)
        raw = self.rom[0x42454:0x42454 + 2048] + b"\xA5" * 16
        fixture = TableLoopFixture(self.table_loop_code(), raw, table, count)
        fixture.run(entry=0x10001398, stop_pc=0x100013E4, budget=8192)
        expected = [page[1] for page in self.pages] + [self.pages[-1][2]]
        self.assertEqual([fixture.get(table + i * 4, 4) for i in range(count)], expected)
        self.assertEqual(fixture.writes, [(table + i * 4, 4) for i in range(count)])
        self.assertEqual(fixture.reads.count((0x800354FC, 4)), count)
        self.assertEqual(fixture.visits[0x100013BC], count)
        self.assertEqual(fixture.visits[0x100013DC], count)
        self.assertEqual(fixture.registers[3:5], [count, count * 4])
        self.assertEqual(fixture.get(0x800354FC, 4), table)
        self.assertEqual(bytes(fixture.memory[table + i] for i in range(count * 4, len(raw))),
                         raw[count * 4:])
        self.assertEqual(table + count * 4, 0x80033320)
        self.assertEqual(table + 2048, retail.INPUT)

    def test_table_loop_loaded_pointer_and_cursor_on_relocated_small_fixtures(self):
        code = self.table_loop_code()
        for address in (0x80032B30, 0x81000000):
            for count in (1, 2, 17):
                with self.subTest(address=hex(address), count=count):
                    values = [0x42480 + i * 0x20 for i in range(count)]
                    raw = b"".join(struct.pack(">I", (value - 0x42450) ^ 0x8039CCCA)
                                   for value in values) + b"\xA5" * 16
                    fixture = TableLoopFixture(code, raw, address, count)
                    fixture.run(entry=0x10001398, stop_pc=0x100013E4, budget=256)
                    self.assertEqual([fixture.get(address + i * 4, 4) for i in range(count)], values)
                    self.assertEqual(fixture.writes, [(address + i * 4, 4) for i in range(count)])
                    self.assertEqual(bytes(fixture.memory[address + count * 4 + i]
                                           for i in range(16)), b"\xA5" * 16)

    def test_zero_table_count_skips_pointer_dereference_and_all_writes(self):
        fixture = TableLoopFixture(self.table_loop_code(), b"\xA5" * 16, 0x80032B30, 0)
        fixture.run(entry=0x10001398, stop_pc=0x100013E4, budget=16)
        self.assertEqual(fixture.writes, [])
        self.assertNotIn((0x800354FC, 4), fixture.reads)
        self.assertNotIn(0x100013BC, fixture.visits)


if __name__ == "__main__":
    unittest.main()
