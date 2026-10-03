import hashlib
import re
import struct
import unittest
import zlib

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_tables as tables


def reference_data(filename, symbol):
    project = contract.InitDecompressorContractTests.project
    source = (project / ("asm/data/" + filename)).read_text()
    body = source.split("dlabel " + symbol + "\n", 1)[1].split(
        "enddlabel " + symbol, 1)[0]
    sizes = {"byte": 1, "short": 2, "word": 4}
    return b"".join(int(value, 16).to_bytes(sizes[kind], "big")
                    for kind, value in re.findall(
                        r"\.(byte|short|word) 0x([0-9A-Fa-f]+)", body))


class FixedDecoderFixture(tables.BuilderFixture):
    OUTPUT = 0x40000
    INPUT = 0x50000
    FIXED_BASE = 0x8003BE90

    def __init__(self, raw, prefix=b"", limit=0x70000000):
        bases = struct.unpack(">31H", reference_data("2C0C0.rodata.s", "D_8002C0E2"))
        extras = reference_data("2C120.rodata.s", "D_8002C16F")
        lengths = [8] * 144 + [9] * 112 + [7] * 24 + [8] * 8
        super().__init__(lengths, bits=7, simple=257, bases=bases, extras=extras)
        if self.run() != 0:
            raise AssertionError("Fixed literal table build failed")
        distance = tables.BuilderFixture(
            [5] * 30, bits=5, simple=0, allocated=self.fprs[19],
            bases=struct.unpack(">30H", reference_data("2C120.rodata.s", "D_8002C120")),
            extras=reference_data("2C120.rodata.s", "D_8002C18E"))
        if distance.run() != 1:
            raise AssertionError("Fixed distance incomplete-table status changed")
        self.memory.update({address: value for address, value in distance.memory.items()
                            if self.WORKSPACE <= address < self.ROOT})
        # The fixed wrapper uses absolute retail workspace pointers.
        self.memory.update({self.FIXED_BASE + address - self.WORKSPACE: value
                            for address, value in list(self.memory.items())
                            if self.WORKSPACE <= address < self.ROOT})
        self.code = dict(contract.InitDecompressorContractTests.entries("func_10006E00"))
        self.code.update(contract.InitDecompressorContractTests.entries("func_1000692C"))
        masks = reference_data("2C0C0.rodata.s", "D_8002C0C0")
        self.memory.update({0x8002C0C0 + i: value for i, value in enumerate(masks)})
        self.memory.update({self.INPUT + i: value for i, value in enumerate(raw + b"\0" * 16)})
        self.memory.update({self.OUTPUT + i: value for i, value in enumerate(prefix)})
        self.memory[self.OUTPUT - 1] = 0xA5
        self.registers[4:8] = [self.WORKSPACE + 4, self.WORKSPACE + 626 * 4, 7, 5]
        self.registers[22] = self.WORKSPACE
        self.registers[23] = self.INPUT + 1
        self.registers[28], self.registers[30] = raw[0] >> 3, 5
        self.registers[31] = 0xDEAD0000
        self.fprs[16:19] = [self.OUTPUT, len(prefix), limit]
        self.reads, self.writes = [], []

    def decode(self, wrapper=False):
        return self.run(entry=0x1000692C if wrapper else 0x10006E00)

    def output(self):
        return bytes(self.memory[self.OUTPUT + i] for i in range(self.fprs[17]))


class InitDecompressorDecoderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract.InitDecompressorContractTests.setUpClass.__func__(
            contract.InitDecompressorContractTests)
        cls.lengths = [8] * 144 + [9] * 112 + [7] * 24 + [8] * 8
        cls.codes = {symbol: (code, bits) for symbol, bits, code in
                     tables.InitDecompressorTableTests.canonical(cls.lengths)}
        cls.distance_codes = {symbol: (code, bits) for symbol, bits, code in
                              tables.InitDecompressorTableTests.canonical([5] * 32)}
        cls.bases = struct.unpack(">31H", reference_data("2C0C0.rodata.s", "D_8002C0E2"))
        cls.extras = reference_data("2C120.rodata.s", "D_8002C16F")
        cls.distance_bases = struct.unpack(">30H", reference_data("2C120.rodata.s", "D_8002C120"))
        cls.distance_extras = reference_data("2C120.rodata.s", "D_8002C18E")

    @classmethod
    def encoded(cls, tokens, terminate=True):
        bits = [1, 1, 0]  # Final fixed-Huffman block header, low bit first.

        def emit(value, width):
            bits.extend((value >> i) & 1 for i in range(width))

        for token in tokens:
            if isinstance(token, int):
                emit(*cls.codes[token])
                continue
            length, distance = token[:2]
            li = (token[2] if len(token) == 3 else
                  max(index for index in range(29)
                      if cls.bases[index] <= length <=
                      cls.bases[index] + (1 << cls.extras[index]) - 1))
            emit(*cls.codes[257 + li])
            emit(length - cls.bases[li], cls.extras[li])
            di = max(index for index in range(30)
                     if cls.distance_bases[index] <= distance <=
                     cls.distance_bases[index] + (1 << cls.distance_extras[index]) - 1)
            emit(*cls.distance_codes[di])
            emit(distance - cls.distance_bases[di], cls.distance_extras[di])
        if terminate:
            emit(*cls.codes[256])
        return bytes(sum(bit << i for i, bit in enumerate(bits[offset:offset + 8]))
                     for offset in range(0, len(bits), 8))

    def assert_valid(self, raw, expected):
        self.assertEqual(zlib.decompress(raw, -15), expected)
        for wrapper in (False, True):
            fixture = FixedDecoderFixture(raw)
            fixture.memory[fixture.OUTPUT + len(expected)] = 0xA5
            self.assertEqual(fixture.decode(wrapper), 0)
            self.assertEqual(fixture.output(), expected)
            self.assertEqual(fixture.memory[fixture.OUTPUT - 1], 0xA5)
            self.assertEqual(fixture.memory[fixture.OUTPUT + len(expected)], 0xA5)

    def test_complete_decoder_body_matches_reference(self):
        entries = contract.InitDecompressorContractTests.entries("func_10006E00")
        self.assertEqual([address for address, _ in entries],
                         list(range(0x10006E00, 0x1000709C, 4)))
        data = b"".join(struct.pack(">I", word) for _, word in entries)
        self.assertEqual(hashlib.sha256(data).hexdigest(),
                         "9991b45e6425503146d321b1a31b8a114c5932e8c029101ea0942c42c06d4895")
        rom = contract.InitDecompressorContractTests.project / "conker.us.bin"
        if rom.exists():
            self.assertEqual(data, rom.read_bytes()[0x6E00:0x709C])

    def test_empty_and_every_literal_against_zlib(self):
        for payload in (b"", bytes(range(256)), b"Conker fixed table\0\xff"):
            self.assert_valid(self.encoded(payload), payload)

    def test_overlapping_distance_one_and_three(self):
        self.assert_valid(self.encoded([ord("A"), (258, 1)]), b"A" * 259)
        self.assert_valid(self.encoded([*b"abc", (258, 3)]), b"abc" * 87)

    def test_zlib_generated_fixed_blocks(self):
        for payload in (b"A" * 2048, b"Conker fixed block\0" * 96,
                        bytes(range(64)) * 32):
            encoder = zlib.compressobj(level=6, wbits=-15, strategy=zlib.Z_FIXED)
            raw = encoder.compress(payload) + encoder.flush()
            self.assertEqual((raw[0] >> 1) & 3, 1)
            self.assert_valid(raw, payload)

    def test_all_length_and_distance_extra_bit_classes(self):
        prefix = bytes((i * 17 + 3) & 0xFF for i in range(32768))
        for index in range(30):
            distance = self.distance_bases[index] + (1 << self.distance_extras[index]) - 1
            li = min(index, 28)
            length = self.bases[li] + (1 << self.extras[li]) - 1
            history = prefix[:distance]
            raw = self.encoded([*history, (length, distance, li)])
            expected = bytearray(history)
            for _ in range(length):
                expected.append(expected[-distance])
            self.assertEqual(zlib.decompress(raw, -15), bytes(expected))
            # Start at this block with preceding output already in the history window.
            for wrapper in (False, True):
                fixture = FixedDecoderFixture(self.encoded([(length, distance, li)]),
                                              prefix=history)
                self.assertEqual(fixture.decode(wrapper), 0)
                self.assertEqual(fixture.output(), bytes(expected))
                self.assertEqual([(address, size) for address, size in fixture.writes
                                  if fixture.OUTPUT <= address < fixture.INPUT],
                                 [(fixture.OUTPUT + len(history) + i, 1)
                                  for i in range(length)])

    def test_literal_path_ignores_limit_and_publishes_at_end(self):
        raw = self.encoded(b"abcd")
        fixture = FixedDecoderFixture(raw, limit=1)
        self.assertEqual(fixture.decode(), 0)
        self.assertEqual(fixture.output(), b"abcd")

    def test_match_limit_equality_rejects_without_publishing_partial_count(self):
        raw = self.encoded([ord("A"), (3, 1)])
        for limit in (3, 4):
            fixture = FixedDecoderFixture(raw, limit=limit)
            self.assertEqual(fixture.decode(), 1)
            self.assertEqual(fixture.fprs[17], 0)
            self.assertEqual(fixture.writes, [(fixture.OUTPUT, 1)])
            self.assertEqual(fixture.memory[fixture.OUTPUT], ord("A"))
        fixture = FixedDecoderFixture(raw, limit=5)
        self.assertEqual(fixture.decode(), 0)
        self.assertEqual(fixture.output(), b"AAAA")

    def test_reserved_symbol_errors_and_wrapper_discards_status(self):
        for symbol in (286, 287):
            raw = self.encoded([ord("A"), symbol], terminate=False)
            direct = FixedDecoderFixture(raw)
            self.assertEqual(direct.decode(), 1)
            self.assertEqual(direct.fprs[17], 0)
            wrapped = FixedDecoderFixture(raw)
            self.assertEqual(wrapped.decode(wrapper=True), 0)
            self.assertEqual(wrapped.fprs[17], 0)
            self.assertEqual(wrapped.memory[wrapped.OUTPUT], ord("A"))
            self.assertEqual(wrapped.registers[22], wrapped.WORKSPACE)

    def test_reserved_distance_codes_fail_without_count_publication(self):
        for symbol in (30, 31):
            fields = [(3, 3), self.codes[ord("A")], self.codes[257],
                      self.distance_codes[symbol], self.codes[256]]
            bits = [((value >> i) & 1) for value, width in fields for i in range(width)]
            raw = bytes(sum(bit << i for i, bit in enumerate(bits[offset:offset + 8]))
                        for offset in range(0, len(bits), 8))
            with self.assertRaises(zlib.error):
                zlib.decompress(raw, -15)
            fixture = FixedDecoderFixture(raw)
            self.assertEqual(fixture.decode(), 1)
            self.assertEqual(fixture.fprs[17], 0)
            self.assertEqual(fixture.writes, [(fixture.OUTPUT, 1)])

    def test_distance_before_output_is_not_validated_in_model(self):
        raw = self.encoded([ord("A"), (3, 2)])
        with self.assertRaises(zlib.error):
            zlib.decompress(raw, -15)
        fixture = FixedDecoderFixture(raw)
        self.assertEqual(fixture.decode(), 0)
        self.assertEqual(fixture.output(), b"A\xa5A\xa5")
        self.assertIn((fixture.OUTPUT - 1, 1), fixture.reads)


if __name__ == "__main__":
    unittest.main()
