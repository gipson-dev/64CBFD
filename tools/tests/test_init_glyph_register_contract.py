import re
import struct
import unittest
from pathlib import Path
from types import SimpleNamespace

from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture
from tools.tests import test_init_decompressor_contract as contract


class GlyphFixture(GuestBuilderFixture):
    DEST = 0x80200000
    SECOND = 0x80210000
    FONT = 0x8002AC84
    STRIDE = 0x248

    def __init__(self, code, rows, glyph=0):
        super().__init__(SimpleNamespace(code=code, memory={}, readonly=[],
                                         entry=0x10007D28), [])
        self.allowed_writes = None
        for base in (self.DEST, self.SECOND):
            self.memory.update((base + offset, 0xA5)
                               for offset in range(-16, 8 * self.STRIDE + 16))
        self.memory.update((self.FONT + glyph * 8 + index, byte)
                           for index, byte in enumerate(rows))
        self.registers = [(0xA5A50000 + index) for index in range(32)]
        self.registers[0] = 0
        self.registers[9:13] = [self.DEST, self.SECOND - self.DEST,
                                glyph, self.FONT]
        self.registers[31] = 0xDEAD0000
        self.before = self.registers[:]
        self.min_sp = self.registers[29]
        self.writes.clear()
        self.reads.clear()
        self.allowed_writes = [(base + row * self.STRIDE,
                                base + row * self.STRIDE + 16)
                               for base in (self.DEST, self.SECOND)
                               for row in range(8)]
        self.readonly = [(self.FONT + glyph * 8, self.FONT + glyph * 8 + 8)]


class InitGlyphRegisterContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract.InitDecompressorContractTests.setUpClass()
        project = Path(__file__).resolve().parents[2] / 'conker'
        source = (project / 'asm/init_5AB0.s').read_text()
        leaf = source.split('glabel func_10007D28\n', 1)[1].split(
            'endlabel func_10007D28', 1)[0]
        cls.code = {int(address, 16): int(word, 16) for address, word in
                    re.findall(r'/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+'
                               r'([0-9A-Fa-f]{8})\s*\*/', leaf)}
        cls.rom = (project / 'conker.us.bin').read_bytes()

    def test_complete_retail_slot(self):
        self.assertEqual(sorted(self.code), list(range(0x10007D28, 0x10007DA0, 4)))
        self.assertEqual(b''.join(struct.pack('>I', self.code[pc])
                                  for pc in sorted(self.code)),
                         self.rom[0x7D28:0x7DA0])

    def qualify(self, rows, glyph):
        fixture = GlyphFixture(self.code, rows, glyph)
        fixture.run(budget=5000)
        expected = []
        for row, byte in enumerate(rows):
            for column in range(8):
                pixel = 0xFFFF if byte & (0x80 >> column) else 1
                for base in (fixture.DEST, fixture.SECOND):
                    address = base + row * fixture.STRIDE + column * 2
                    expected.append((address, 2))
                    self.assertEqual(fixture.get(address, 2), pixel)
        self.assertEqual(fixture.writes, expected)
        self.assertEqual(len(fixture.writes), 128)
        for base in (fixture.DEST, fixture.SECOND):
            for row in range(8):
                self.assertEqual(fixture.get(base + row * fixture.STRIDE - 2, 2), 0xA5A5)
                self.assertEqual(fixture.get(base + row * fixture.STRIDE + 16, 2), 0xA5A5)
        self.assertEqual(fixture.registers[9], fixture.DEST + 16)
        changed = {1, 6, 7, 9, 11, 13, 14, 15, 24}
        for index in set(range(32)) - changed:
            self.assertEqual(fixture.registers[index], fixture.before[index])
        self.assertEqual(fixture.registers[14], fixture.FONT + glyph * 8 + 8)
        self.assertEqual(fixture.registers[6:8], [0, 0])
        return fixture

    def test_all_byte_patterns_and_nonzero_glyph_offsets(self):
        for byte in range(256):
            with self.subTest(byte=byte):
                self.qualify([(byte + row * 37) & 255 for row in range(8)], byte % 41)

    def test_uniform_and_alternating_rows(self):
        for byte in (0, 0xFF, 0xAA, 0x55, 0x80, 1):
            self.qualify([byte] * 8, 9)

    def test_write_fence_rejects_row_gaps_and_font(self):
        fixture = GlyphFixture(self.code, [0] * 8)
        for address in (fixture.DEST - 2, fixture.DEST + 16,
                        fixture.SECOND + 16, fixture.FONT):
            with self.assertRaises(AssertionError):
                fixture.put(address, 0, 2)


if __name__ == '__main__':
    unittest.main()
