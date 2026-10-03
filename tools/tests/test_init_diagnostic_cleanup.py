import struct
import unittest
from types import SimpleNamespace

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_retail_pages as retail
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture


class DiagnosticCleanupFixture(GuestBuilderFixture):
    TABLE, BITMAP = 0x80043B40, 0x80200000
    STATIC_LOW, STATIC_HIGH = 0x80031AE0, 0x80035504
    MARKERS = {0x4D: "unmap", 0x8D: "format", 0xCD: "writeback"}

    def __init__(self, code, count, result):
        self.code, self.image = dict(code), SimpleNamespace(entry=0x10008078)
        self.memory = {}
        self.readonly, self.allowed_writes = [], None
        self.registers = [0] * 32
        self.registers[2:4] = [result, 0x12345678]
        self.registers[29] = self.min_sp = 0x80135958
        self.fprs = [0] * 32
        self.reads, self.writes, self.visits = [], [], {}
        self.capture, self.snapshots = set(), {}
        self.calls, self.cache_operands = [], []
        self.count, self.bitmap_bytes = count, (count + 7) // 8
        self.memory.update((address, 0xA5) for address in
                           range(self.STATIC_LOW, self.STATIC_HIGH))
        self.memory.update((address, 0xA5) for address in
                           range(self.TABLE - 16, self.TABLE + 0xFE0 + 16))
        self.memory.update((address, 0xA5) for address in
                           range(self.BITMAP - 16, self.BITMAP + self.bitmap_bytes + 16))
        for address, value, size in ((0x8003BE70, self.BITMAP, 4),
                                     (0x8003BE74, 0x0012E000, 4),
                                     (0x8003BE78, count, 2),
                                     (0x8003BE7C, self.BITMAP + self.bitmap_bytes - 1, 4),
                                     (0x8003C8F8, 0x100077A4, 4),
                                     (0x8003C8FC, 0x80032A10, 4),
                                     (0x8002AE34, 0x220, 4)):
            self.put(address, value, size)
        for address, marker in ((0x100262D0, 0x4D), (0x10007CC4, 0x8D),
                                (0x10024F10, 0xCD)):
            self.code.update({address: marker, address + 4: 0x03E00008, address + 8: 0})
        self.allowed_writes = [(self.TABLE, self.TABLE + 0xFE0),
                               (self.BITMAP, self.BITMAP + self.bitmap_bytes),
                               (0x8003C8F8, 0x8003C8FC), (0x8002AE34, 0x8002AE38)]

    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        immediate = word & 0xFFFF
        offset = immediate if immediate < 0x8000 else immediate - 0x10000
        if word in self.MARKERS:
            self.calls.append((self.MARKERS[word], self.registers[4], self.registers[5]))
        elif op == 47:
            self.cache_operands.append((rt, (self.registers[rs] + offset) & 0xFFFFFFFF))
        elif op == 8:
            result = self.signed(self.registers[rs]) + offset
            if not -0x80000000 <= result <= 0x7FFFFFFF:
                raise AssertionError("cleanup ADDI would overflow")
            self.registers[rt] = result & 0xFFFFFFFF
        elif op == 33:
            address = (self.registers[rs] + offset) & 0xFFFFFFFF
            value = self.get(address, 2)
            self.registers[rt] = (value if value < 0x8000 else value - 0x10000) & 0xFFFFFFFF
            self.reads.append((address, 2))
        else:
            super().execute(word)
        self.registers[0] = 0


class InitDiagnosticCleanupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        retail.InitDecompressorRetailPageTests.setUpClass.__func__(cls)
        entries = dict(contract.InitDecompressorContractTests.entries("func_10007DAC"))
        entries.update(contract.InitDecompressorContractTests.entries("func_10005BE0"))
        cls.code = {}
        clear_words = bytes.fromhex(
            "3C0E8004 25C53B40 24A40FE0 24A50004 00A4082B 1420FFFD ACA0FFFC 03E00008 00000000")
        if cls.rom[0x1420:0x1444] != clear_words:
            raise AssertionError("software page-table clear differs from retail")
        cls.code.update((0x10001420 + i * 4, word) for i, (word,) in
                        enumerate(struct.iter_unpack(">I", clear_words)))
        for first, last in ((0x10008078, 0x10008118), (0x10005BE0, 0x10005C2C)):
            for pc in range(first, last, 4):
                word = entries[pc]
                if struct.unpack_from(">I", cls.rom, pc - 0x10000000)[0] != word:
                    raise AssertionError("diagnostic cleanup differs from retail")
                cls.code[pc] = word

    def qualify(self, count, result):
        fixture = DiagnosticCleanupFixture(self.code, count, result)
        fixture.run(stop_pc=0x10008110, budget=20000)
        self.assertEqual([call[1] for call in fixture.calls if call[0] == "unmap"], list(range(2, 32)))
        self.assertEqual([call[0] for call in fixture.calls], ["unmap"] * 30 + ["format", "writeback"])
        self.assertEqual(fixture.calls[-2], ("format", 0x300, 0x8002ADEC))
        self.assertEqual(fixture.cache_operands, [(0, address) for address in range(0x80000000, 0x80004001, 32)])
        self.assertEqual(len(fixture.cache_operands), 513)
        self.assertEqual([write for write in fixture.writes if fixture.TABLE <= write[0] < fixture.TABLE + 0xFE0],
                         [(fixture.TABLE + i * 4, 4) for i in range(1016)])
        self.assertEqual(bytes(fixture.memory[fixture.TABLE + i] for i in range(0xFE0)), bytes(0xFE0))
        for first in (fixture.TABLE - 16, fixture.TABLE + 0xFE0,
                      fixture.BITMAP - 16, fixture.BITMAP + fixture.bitmap_bytes):
            self.assertEqual(bytes(fixture.memory[first + i] for i in range(16)), b"\xA5" * 16)
        expected = bytearray(b"\xFF" * fixture.bitmap_bytes)
        if count & 7:
            expected[-1] = (1 << (count & 7)) - 1
        self.assertEqual(bytes(fixture.memory[fixture.BITMAP + i] for i in range(fixture.bitmap_bytes)), expected)
        self.assertEqual(bytes(fixture.memory[address] for address in
                               range(fixture.STATIC_LOW, fixture.STATIC_HIGH)),
                         b"\xA5" * (fixture.STATIC_HIGH - fixture.STATIC_LOW))
        self.assertEqual(fixture.get(0x8002AE34, 4), 0)
        self.assertEqual(fixture.get(0x8003BE74, 4), 0x0012E000)
        self.assertEqual(fixture.registers[29], 0x80032A10)
        self.assertEqual(fixture.registers[18], 0x12345678)
        self.assertEqual(fixture.registers[31], 0x10007760 if result else 0x100077A4)
        return fixture

    def test_return_result_selects_continuation_after_real_page_state_cleanup(self):
        for count in (107, 235, 362):
            for result in (0, 1):
                with self.subTest(count=count, result=result):
                    self.qualify(count, result)

    def test_nonzero_result_is_not_limited_to_one_and_full_bitmap_byte_case(self):
        self.qualify(112, 0xFFFFFFFF)

    def test_all_partial_bitmap_byte_masks(self):
        for count in range(112, 120):
            with self.subTest(count=count):
                self.qualify(count, 0)

    def test_write_fence_rejects_static_decoder_storage_and_guard_bytes(self):
        fixture = DiagnosticCleanupFixture(self.code, 235, 0)
        for address in (fixture.STATIC_LOW, fixture.TABLE - 4,
                        fixture.TABLE + 0xFE0, fixture.BITMAP + fixture.bitmap_bytes):
            with self.assertRaisesRegex(AssertionError, "caller-owned"):
                fixture.put(address, 0, 4)


if __name__ == "__main__":
    unittest.main()
