import struct
import unittest

from tools.tests import test_init_glyph_register_contract as glyph
from tools.tests import test_init_decompressor_contract as contract


class FormatterFixture(glyph.GlyphFixture):
    def __init__(self, code, entry, position, value=0, text=None, buffers=True):
        super().__init__(code, [0] * 8)
        self.image.entry = entry
        self.allowed_writes = None
        self.readonly = []
        for index in range(128 * 8):
            self.memory[self.FONT + index] = (index * 37 + 19) & 255
        self.put(0x8002AAE8, self.DEST if buffers else 0, 4)
        self.put(0x8002AAEC, self.SECOND if buffers else 0, 4)
        self.registers[4:6] = [position, value]
        if text is not None:
            self.registers[5] = 0x80300000
            self.memory.update((0x80300000 + i, byte) for i, byte in enumerate(text + b'\0'))
        self.before = self.registers[:]
        self.writes.clear()
        self.reads.clear()
        self.glyphs = []
        self.readonly = [(self.FONT, self.FONT + 128 * 8)]
        self.allowed_writes = [(self.DEST, self.DEST + 0x20000),
                               (self.SECOND, self.SECOND + 0x20000)]

    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        immediate = word & 65535
        offset = immediate if immediate < 32768 else immediate - 65536
        if op == 8 or (op == 0 and word & 63 == 34):
            result = (self.signed(self.registers[rs]) + offset if op == 8 else
                      self.signed(self.registers[rs]) - self.signed(self.registers[rt]))
            if not -0x80000000 <= result <= 0x7FFFFFFF:
                raise AssertionError('signed arithmetic overflow')
            destination = rt if op == 8 else word >> 11 & 31
            self.registers[destination] = result & 0xFFFFFFFF
        elif op == 32:
            address = (self.registers[rs] + offset) & 0xFFFFFFFF
            value = self.get(address, 1)
            self.registers[rt] = (value if value < 128 else value - 256) & 0xFFFFFFFF
            self.reads.append((address, 1))
        else:
            super().execute(word)
        self.registers[0] = 0

    def run(self, budget=50000):
        pc = self.image.entry
        for _ in range(budget):
            if pc == 0xDEAD0000:
                return
            if pc == 0x10007D28:
                self.glyphs.append((self.registers[9], self.registers[11]))
            word = self.code[pc]
            op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
            if op in (1, 4, 5, 20, 21):
                if op == 1:
                    if rt not in (0, 1):
                        raise AssertionError('unsupported REGIMM')
                    taken = (self.signed(self.registers[rs]) < 0) == (rt == 0)
                else:
                    taken = (self.registers[rs] == self.registers[rt]) == (op in (4, 20))
                offset = word & 65535
                offset = offset if offset < 32768 else offset - 65536
                if taken or op not in (20, 21):
                    self.execute(self.code[pc + 4])
                pc = pc + 4 + offset * 4 if taken else pc + 8
            elif op == 3:
                self.registers[31] = pc + 8
                self.execute(self.code[pc + 4])
                pc = ((pc + 4) & 0xF0000000) | ((word & 0x3FFFFFF) << 2)
            elif op == 0 and word & 63 in (8, 9):
                target = self.registers[rs]
                if word & 63 == 9:
                    self.registers[word >> 11 & 31] = pc + 8
                self.execute(self.code[pc + 4])
                pc = target
            else:
                self.execute(word)
                pc += 4
        raise AssertionError('formatter instruction budget exhausted')


class InitGlyphFormatterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract.InitDecompressorContractTests.setUpClass()
        cls.code = {}
        for name in ('__osCleanupThread', 'func_10007C74', 'func_10007CC4', 'func_10007D28'):
            cls.code.update(contract.InitDecompressorContractTests.entries(name))
        cls.rom = (contract.InitDecompressorContractTests.project / 'conker.us.bin').read_bytes()

    def test_connected_words_equal_retail(self):
        for pc, word in self.code.items():
            self.assertEqual(word, struct.unpack_from('>I', self.rom, pc - 0x10000000)[0])

    def verify_pixels(self, fixture):
        expected = []
        for cursor, index in fixture.glyphs:
            for row in range(8):
                byte = fixture.memory[fixture.FONT + index * 8 + row]
                for column in range(8):
                    pixel = 65535 if byte & (128 >> column) else 1
                    for displacement in (0, fixture.SECOND - fixture.DEST):
                        address = cursor + row * fixture.STRIDE + column * 2 + displacement
                        expected.append((address, 2))
                        self.assertEqual(fixture.get(address, 2), pixel)
        self.assertEqual(fixture.writes, expected)
        for register in (*range(16, 24), 28, 29, 30):
            self.assertEqual(fixture.registers[register], fixture.before[register])
        self.assertEqual(fixture.registers[5], 0xDEAD0000)

    def test_hex_nibbles_render_right_to_left(self):
        for position in (0, 31, 32, 63, 0x300):
            for value in (0, 0xFFFFFFFF, 0x12345678, 0x80000001):
                fixture = FormatterFixture(self.code, 0x10007C74, position, value)
                fixture.run()
                adjusted = position + 9
                cursor = fixture.DEST + (adjusted & 0xFFE0) * 146 + (adjusted & 31) * 16 + 0x4A0
                self.assertEqual(fixture.glyphs, [(cursor - 32 - i * 16, ((value >> (i * 4)) & 15) + 9)
                                                for i in range(8)])
                self.assertEqual(fixture.registers[2], cursor - 128)
                self.assertEqual(fixture.registers[4], position)
                self.verify_pixels(fixture)

    def test_all_nonzero_signed_character_bytes(self):
        for byte in range(1, 256):
            fixture = FormatterFixture(self.code, 0x10007CC4, 0, text=bytes([byte]))
            fixture.run()
            signed = byte if byte < 128 else byte - 256
            index = max(0, signed - (7 if signed >= 65 else 0) - 39)
            self.assertEqual(fixture.glyphs, [(fixture.DEST + 0x4A0, index)])
            self.verify_pixels(fixture)

    def test_empty_and_multicharacter_strings(self):
        for text in (b'', b'0123456789ABCDEF', b' A@Z[az\x80\xff'):
            fixture = FormatterFixture(self.code, 0x10007CC4, 32, text=text)
            fixture.run()
            cursor = fixture.DEST + 32 * 146 + 0x4A0
            self.assertEqual([dest for dest, _ in fixture.glyphs],
                             [cursor + i * 16 for i in range(len(text))])
            self.verify_pixels(fixture)

    def test_missing_destination_exits_through_original_ra(self):
        for entry in (0x10007C74, 0x10007CC4):
            for first, second in ((0, 0x80210000), (0x80200000, 0), (0, 0)):
                fixture = FormatterFixture(self.code, entry, 0, text=b'A')
                fixture.allowed_writes = None
                fixture.put(0x8002AAE8, first, 4)
                fixture.put(0x8002AAEC, second, 4)
                fixture.writes.clear()
                fixture.run()
                self.assertEqual(fixture.glyphs, [])
                self.assertEqual(fixture.writes, [])
                self.assertEqual(fixture.registers[31], 0xDEAD0000)


if __name__ == '__main__':
    unittest.main()
