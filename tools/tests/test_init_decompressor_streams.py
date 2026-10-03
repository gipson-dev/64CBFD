import hashlib
import struct
import unittest
import zlib

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests import test_init_decompressor_tables as tables


class StreamFixture(decoder.FixedDecoderFixture):
    def __init__(self, raw, limit=0x70000000):
        super().__init__(raw, limit=limit)
        for name in ("func_10006240", "func_1000625C", "func_1000632C", "func_10006380", "func_10006424",
                     "func_10006828", "func_1000696C"):
            self.code.update(contract.InitDecompressorContractTests.entries(name))
        for address, filename, symbol in (
                (0x8002C0E2, "2C0C0.rodata.s", "D_8002C0E2"),
                (0x8002C120, "2C120.rodata.s", "D_8002C120"),
                (0x8002C15C, "2C120.rodata.s", "D_8002C15C"),
                (0x8002C16F, "2C120.rodata.s", "D_8002C16F"),
                (0x8002C18E, "2C120.rodata.s", "D_8002C18E")):
            data = decoder.reference_data(filename, symbol)
            self.memory.update({address + i: byte for i, byte in enumerate(data)})
        self.registers[23] = self.INPUT
        self.registers[28], self.registers[30] = 0, 0
        self.visits = {}

    def stream(self):
        return self.run(entry=0x1000632C, budget=2000000)

    def core(self, wrapped, alignment=0, workspace=None):
        self.registers[4:7] = [self.INPUT + alignment, self.OUTPUT,
                               self.WORKSPACE if workspace is None else workspace]
        return self.run(entry=0x10006240 if wrapped else 0x1000625C,
                        budget=2000000)


class BitStream:
    def __init__(self):
        self.bits = []

    def emit(self, value, width):
        self.bits.extend((value >> i) & 1 for i in range(width))

    def data(self):
        return bytes(sum(bit << i for i, bit in enumerate(self.bits[offset:offset + 8]))
                     for offset in range(0, len(self.bits), 8))


class InitDecompressorStreamTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract.InitDecompressorContractTests.setUpClass.__func__(
            contract.InitDecompressorContractTests)

    def dynamic(self, repeat_first=False, overflow=False):
        bits = BitStream()
        bits.emit(5, 3)  # Final dynamic block.
        bits.emit(0, 5)  # 257 literal/length symbols.
        bits.emit(0, 5)  # One distance symbol.
        bits.emit(14, 4)  # Eighteen transmitted code-length lengths.
        order = decoder.reference_data("2C120.rodata.s", "D_8002C15C")
        lengths = [0] * 19
        for symbol, width in ((0, 2), (1, 2), (16, 2), (17, 3), (18, 3)):
            lengths[symbol] = width
        for symbol in order[:18]:
            bits.emit(lengths[symbol], 3)
        codes = {symbol: (code, width) for symbol, width, code in
                 tables.InitDecompressorTableTests.canonical(lengths)}

        def code(symbol, extra=0):
            bits.emit(*codes[symbol])
            if symbol >= 16:
                bits.emit(extra, {16: 2, 17: 3, 18: 7}[symbol])

        if overflow:
            code(0)
            code(18, 127)
            code(18, 127)
            return bits.data()
        if repeat_first:
            code(16, 0)  # Model repeats the initialized zero three times.
            code(18, 51)  # Another 62 zero lengths.
        else:
            code(0)
            code(16, 3)  # Six zero lengths.
            code(17, 7)  # Ten zero lengths.
            code(18, 37)  # Forty-eight zero lengths: total 65.
        code(1)  # Literal A.
        code(18, 127)
        code(18, 41)  # 190 zero lengths: through symbol 255.
        code(1)  # End-of-block symbol 256.
        code(1)  # Single distance code.
        bits.emit(0, 1)  # Literal A in the recovered two-symbol tree.
        bits.emit(1, 1)  # End-of-block.
        return bits.data()

    def assert_stream(self, raw, expected):
        self.assertEqual(zlib.decompress(raw, -15), expected)
        fixture = StreamFixture(raw)
        fixture.memory[fixture.OUTPUT + len(expected)] = 0xA5
        self.assertEqual(fixture.stream(), 0)
        self.assertEqual(fixture.output(), expected)
        self.assertEqual(fixture.memory[fixture.OUTPUT + len(expected)], 0xA5)
        self.assertEqual(fixture.registers[23], fixture.INPUT + len(raw))
        self.assertLess(fixture.registers[30], 8)
        return fixture

    def test_dynamic_reference_body(self):
        entries = contract.InitDecompressorContractTests.entries("func_10006424")
        data = b"".join(struct.pack(">I", word) for _, word in entries)
        self.assertEqual(len(data), 1028)
        self.assertEqual(hashlib.sha256(data).hexdigest(),
                         "40f835450a499e50052e1737edfade8b336c3add82f129da5a8b6de7600cba6a")
        rom = contract.InitDecompressorContractTests.project / "conker.us.bin"
        if rom.exists():
            self.assertEqual(data, rom.read_bytes()[0x6424:0x6828])

    def test_dynamic_repeat_symbols_and_generated_tables(self):
        fixture = self.assert_stream(self.dynamic(), b"A")
        for address in (0x10006630, 0x100066A8, 0x10006714):
            self.assertGreater(fixture.visits.get(address, 0), 0)
        self.assertEqual(fixture.visits.get(0x1000696C), 3)
        self.assertGreater(fixture.visits.get(0x10006E00, 0), 0)

    def test_zlib_generated_dynamic_blocks(self):
        for payload in ((b"Conker dynamic block with repeated text " * 256),
                        bytes(range(128)) * 64):
            encoder = zlib.compressobj(level=6, wbits=-15)
            raw = encoder.compress(payload) + encoder.flush()
            self.assertEqual((raw[0] >> 1) & 3, 2)
            self.assert_stream(raw, payload)

    def test_mixed_stored_fixed_dynamic_stream_and_cursor_rewind(self):
        fixed = decoder.InitDecompressorDecoderTests
        fixed.setUpClass.__func__(fixed)
        fixed_raw = fixed.encoded(b"BC")
        nonfinal = bytes([fixed_raw[0] & 0xFE]) + fixed_raw[1:]
        # A stored block aligns the following boundary and is independently encoded.
        stored = b"\x00" + struct.pack("<HH", 2, 0xFFFD) + b"XY"
        # Fixed bitstream ends within its last byte; append a byte-aligned empty
        # stored block header before using the final dynamic block.
        bits = BitStream()
        bits.bits = [(byte >> i) & 1 for byte in stored for i in range(8)]
        fixed_length = 3 + sum(fixed.codes[symbol][1] for symbol in (*b"BC", 256))
        bits.bits.extend((byte >> i) & 1 for byte in nonfinal for i in range(8))
        bits.bits = bits.bits[:len(stored) * 8 + fixed_length]
        bits.emit(0, 3)
        while len(bits.bits) & 7:
            bits.emit(0, 1)
        bits.emit(0, 16)
        bits.emit(0xFFFF, 16)
        raw = bits.data() + self.dynamic()
        fixture = self.assert_stream(raw, b"XYBCA")
        self.assertEqual(fixture.visits.get(0x10006380), 4)
        self.assertEqual(fixture.visits.get(0x10006828), 2)
        self.assertEqual(fixture.visits.get(0x1000692C), 1)
        self.assertEqual(fixture.visits.get(0x10006424), 1)

    def test_repeat_before_first_length_is_not_rejected_in_model(self):
        raw = self.dynamic(repeat_first=True)
        with self.assertRaises(zlib.error):
            zlib.decompress(raw, -15)
        fixture = StreamFixture(raw)
        self.assertEqual(fixture.stream(), 0)
        self.assertEqual(fixture.output(), b"A")

    def test_repeat_overflow_rejects_before_output(self):
        raw = self.dynamic(overflow=True)
        with self.assertRaises(zlib.error):
            zlib.decompress(raw, -15)
        fixture = StreamFixture(raw)
        self.assertEqual(fixture.stream(), 1)
        self.assertEqual(fixture.fprs[17], 0)
        self.assertFalse(any(fixture.OUTPUT <= address < fixture.INPUT
                             for address, _ in fixture.writes))

    def test_reserved_block_type_returns_two(self):
        fixture = StreamFixture(b"\x07")
        self.assertEqual(fixture.stream(), 2)
        self.assertEqual(fixture.fprs[17], 0)

    def test_core_header_skips_unaligned_input_and_saved_registers(self):
        raw = self.dynamic()
        for header in (b"\x11\x72", b"\x11\x73\0\0"):
            for alignment in range(4):
                for wrapped in (False, True):
                    fixture = StreamFixture(b"\xa5" * alignment + header + raw)
                    before = fixture.registers[:]
                    self.assertEqual(fixture.core(wrapped, alignment), 1)
                    self.assertEqual(fixture.output(), b"A")
                    self.assertEqual(fixture.fprs[18], fixture.INPUT + alignment - fixture.OUTPUT)
                    for register in (*range(16, 24), 28, 29, 30, 31):
                        self.assertEqual(fixture.registers[register], before[register])

    def test_core_error_returns_zero_without_output(self):
        for wrapped in (False, True):
            fixture = StreamFixture(b"\x11\x72\x07")
            self.assertEqual(fixture.core(wrapped), 0)
            self.assertEqual(fixture.fprs[17], 0)
            self.assertFalse(any(fixture.OUTPUT <= address < fixture.INPUT
                                 for address, _ in fixture.writes))

    def test_dynamic_header_count_bounds_reject_before_output(self):
        for literals, distances in ((30, 0), (31, 0), (0, 30), (0, 31)):
            bits = BitStream()
            bits.emit(5, 3)
            bits.emit(literals, 5)
            bits.emit(distances, 5)
            bits.emit(0, 4)
            fixture = StreamFixture(bits.data())
            self.assertEqual(fixture.stream(), 1)
            self.assertEqual(fixture.fprs[17], 0)
            self.assertNotIn(0x1000696C, fixture.visits)

    def test_core_workspace_limit_and_prior_block_error_side_effects(self):
        fixture = StreamFixture(b"\x11\x72" + self.dynamic())
        self.assertEqual(fixture.core(False, workspace=fixture.OUTPUT + 8192), 1)
        self.assertEqual(fixture.fprs[18], 8192)
        self.assertEqual(fixture.output(), b"A")
        # A good stored block publishes two bytes; a failing dynamic block then
        # makes the core return zero without undoing those already written bytes.
        stored = b"\x00" + struct.pack("<HH", 2, 0xFFFD) + b"XY"
        fixture = StreamFixture(b"\x11\x72" + stored + self.dynamic(overflow=True))
        self.assertEqual(fixture.core(True), 0)
        self.assertEqual(fixture.fprs[17], 2)
        self.assertEqual(fixture.output(), b"XY")


if __name__ == "__main__":
    unittest.main()
