import hashlib
import re
import struct
import unittest

from tools.tests import test_init_decompressor_contract as contract


class BuilderFixture:
    STACK = 0x10000
    LENGTHS = 0x12000
    WORKSPACE = 0x20000
    ROOT = 0x30000
    BITS = 0x30004
    BASES = 0x31000
    EXTRAS = 0x32000

    def __init__(self, lengths, bits=7, simple=None, allocated=0,
                 bases=(), extras=()):
        self.code = dict(contract.InitDecompressorContractTests.entries(
            "func_1000696C"))
        self.memory = {self.STACK + i: 0xA5 for i in range(0xA88)}
        self.writes = []
        self.reads = []
        self.visits = {}
        self.capture = set()
        self.snapshots = {}
        self.registers = [(0x5A000000 + i) for i in range(32)]
        self.registers[0] = 0
        self.fprs = [0] * 32
        self.fprs[19] = allocated
        for i, length in enumerate(lengths):
            self.put(self.LENGTHS + i * 4, length, 4)
        for i, base in enumerate(bases):
            self.put(self.BASES + i * 2, base, 2)
        for i, extra in enumerate(extras):
            self.put(self.EXTRAS + i, extra, 1)
        self.put(self.ROOT, 0xABCD, 2)
        self.put(self.BITS, bits, 4)
        for register, value in {4: self.LENGTHS, 5: len(lengths),
                                6: len(lengths) if simple is None else simple,
                                7: self.BASES, 15: self.EXTRAS,
                                24: self.ROOT, 25: self.BITS,
                                22: self.WORKSPACE, 29: self.STACK,
                                31: 0xDEAD0000}.items():
            self.registers[register] = value
        self.before = self.registers[:]

    def put(self, address, value, size):
        for i, byte in enumerate((value & ((1 << (size * 8)) - 1)).to_bytes(
                size, "big")):
            self.memory[address + i] = byte

    def get(self, address, size):
        return int.from_bytes(bytes(self.memory[address + i]
                                    for i in range(size)), "big")

    @staticmethod
    def signed(value):
        return value if value < 0x80000000 else value - 0x100000000

    def execute(self, word):
        r = self.registers
        op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
        rd, shift, fn = (word >> 11) & 31, (word >> 6) & 31, word & 63
        immediate = word & 0xFFFF
        signed = immediate if immediate < 0x8000 else immediate - 0x10000
        address = (r[rs] + signed) & 0xFFFFFFFF
        if word == 0:
            pass
        elif op == 17 and rs in (0, 4):
            if rs == 0:
                r[rt] = self.fprs[rd]
            else:
                self.fprs[rd] = r[rt]
        elif op == 9:
            r[rt] = r[rs] + signed
        elif op == 12:
            r[rt] = r[rs] & immediate
        elif op == 13:
            r[rt] = r[rs] | immediate
        elif op == 15:
            r[rt] = immediate << 16
        elif op in (34, 38):
            aligned, offset = address & ~3, address & 3
            if op == 34:
                size = 4 - offset
                mask = (1 << (offset * 8)) - 1
                r[rt] = (r[rt] & mask) | (self.get(address, size) << (offset * 8))
                self.reads.append((address, size))
            else:
                size = offset + 1
                mask = (1 << (size * 8)) - 1
                r[rt] = (r[rt] & ~mask) | self.get(aligned, size)
                self.reads.append((aligned, size))
        elif op in (35, 36, 37):
            size = {35: 4, 36: 1, 37: 2}[op]
            r[rt] = self.get(address, size)
            self.reads.append((address, size))
        elif op in (40, 41, 43, 63):
            size = {40: 1, 41: 2, 43: 4, 63: 8}[op]
            if op == 63 and rt != 0:
                raise AssertionError("Only zero doubleword stores are modeled")
            self.put(address, r[rt], size)
            self.writes.append((address, size))
        elif op == 10:
            r[rt] = int(self.signed(r[rs]) < signed)
        elif op == 0 and fn in (0, 2, 4, 6, 33, 35, 36, 37, 38, 39, 42):
            left, right = r[rs], r[rt]
            operations = {0: lambda: right << shift,
                          2: lambda: right >> shift,
                          4: lambda: right << (left & 31),
                          6: lambda: right >> (left & 31),
                          33: lambda: left + right,
                          35: lambda: left - right,
                          36: lambda: left & right,
                          37: lambda: left | right,
                          38: lambda: left ^ right,
                          39: lambda: ~(left | right),
                          42: lambda: int(self.signed(left) < self.signed(right))}
            r[rd] = operations[fn]()
        else:
            raise AssertionError("Unsupported builder word %08X" % word)
        r[:] = [value & 0xFFFFFFFF for value in r]
        r[0] = 0

    def run(self, budget=200000, entry=0x1000696C):
        # Shared low-word model for the builder and connected decoder only.
        pc = entry
        for _ in range(budget):
            if pc in self.capture:
                self.snapshots[pc] = (self.registers[:], self.fprs[:])
            self.visits[pc] = self.visits.get(pc, 0) + 1
            word = self.code[pc]
            op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
            if op in (1, 23):
                if op == 1 and rt != 0:
                    raise AssertionError("Only BLTZ is modeled for REGIMM")
                take = (self.signed(self.registers[rs]) < 0 if op == 1 else
                        self.signed(self.registers[rs]) > 0)
                immediate = word & 0xFFFF
                offset = immediate if immediate < 0x8000 else immediate - 0x10000
                if take or op == 1:
                    self.execute(self.code[pc + 4])
                pc = pc + 4 + offset * 4 if take else pc + 8
            elif op in (4, 5, 20, 21):
                take = self.registers[rs] == self.registers[rt]
                if op in (5, 21):
                    take = not take
                immediate = word & 0xFFFF
                offset = immediate if immediate < 0x8000 else immediate - 0x10000
                if take or op in (4, 5):
                    self.execute(self.code[pc + 4])
                pc = pc + 4 + offset * 4 if take else pc + 8
            elif op in (2, 3):
                if op == 3:
                    self.registers[31] = pc + 8
                self.execute(self.code[pc + 4])
                pc = ((pc + 4) & 0xF0000000) | ((word & 0x3FFFFFF) << 2)
            elif word == 0x03E00008:
                target = self.registers[31]
                self.execute(self.code[pc + 4])
                if target == 0xDEAD0000:
                    return self.registers[2]
                pc = target
            else:
                self.execute(word)
                pc += 4
        raise AssertionError("Decompressor fixture instruction budget exhausted")

    def lookup(self, code):
        index, width = self.get(self.ROOT, 2), self.get(self.BITS, 4)
        consumed = 0
        for _ in range(17):
            address = self.WORKSPACE + 4 * (index + (code & ((1 << width) - 1)))
            operation, bits = self.get(address, 1), self.get(address + 1, 1)
            value = self.get(address + 2, 2)
            consumed += bits
            if operation <= 16 or operation == 99:
                return operation, consumed, value
            code >>= bits
            index, width = value, operation - 16
        raise AssertionError("Table lookup exceeded maximum depth")


class InitDecompressorTableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract.InitDecompressorContractTests.setUpClass.__func__(
            contract.InitDecompressorContractTests)

    @staticmethod
    def canonical(lengths):
        # Independent canonical-code assignment, then reverse for reservoir lookup.
        counts = [lengths.count(bits) for bits in range(17)]
        counts[0] = 0
        next_code, code = [0] * 17, 0
        for bits in range(1, 17):
            code = (code + counts[bits - 1]) << 1
            next_code[bits] = code
        for symbol, bits in enumerate(lengths):
            if bits:
                code = next_code[bits]
                next_code[bits] += 1
                reversed_code = int(format(code, "0%db" % bits)[::-1], 2)
                yield symbol, bits, reversed_code

    def assert_saved(self, fixture):
        for register in (*range(16, 24), 28, 29, 30, 31):
            self.assertEqual(fixture.registers[register], fixture.before[register])

    def test_full_builder_reference_body(self):
        entries = contract.InitDecompressorContractTests.entries("func_1000696C")
        self.assertEqual([address for address, _ in entries],
                         list(range(0x1000696C, 0x10006E00, 4)))
        data = b"".join(struct.pack(">I", word) for _, word in entries)
        self.assertEqual(hashlib.sha256(data).hexdigest(),
                         "671a7926edb4a0b13a0fda7de90eb090cd9211b8f364aef7f6950d915b3b8b5f")
        rom = contract.InitDecompressorContractTests.project / "conker.us.bin"
        if rom.exists():
            self.assertEqual(data, rom.read_bytes()[0x696C:0x6E00])

    def test_no_symbols_returns_one_without_outputs(self):
        fixture = BuilderFixture([], allocated=9)
        self.assertEqual(fixture.run(), 1)
        self.assertEqual(fixture.get(fixture.ROOT, 2), 0xABCD)
        self.assertEqual(fixture.get(fixture.BITS, 4), 7)
        self.assertEqual(fixture.fprs[19], 9)
        self.assertEqual(fixture.writes, [])
        self.assert_saved(fixture)

    def test_all_zero_lengths_publish_empty_outputs(self):
        fixture = BuilderFixture([0] * 19, allocated=9)
        self.assertEqual(fixture.run(), 0)
        self.assertEqual(fixture.get(fixture.ROOT, 2), 0)
        self.assertEqual(fixture.get(fixture.BITS, 4), 0)
        self.assertEqual(fixture.fprs[19], 9)
        self.assert_saved(fixture)

    def test_complete_literal_trees_and_root_clamping(self):
        for lengths in ([1, 1], [2] * 4, [1, 2, 2],
                        [0, 1, 0, 2, 2]):
            for requested in (0, 1, 2, 7, 16):
                with self.subTest(lengths=lengths, requested=requested):
                    fixture = BuilderFixture(list(lengths), bits=requested)
                    self.assertEqual(fixture.run(), 0)
                    self.assertEqual(fixture.get(fixture.BITS, 4),
                                     min(max(requested, min(x for x in lengths if x)),
                                         max(lengths)))
                    for symbol, bits, code in self.canonical(list(lengths)):
                        self.assertEqual(fixture.lookup(code), (16, bits, symbol))
                    self.assert_saved(fixture)

    def test_incomplete_tree_status_and_invalid_entries(self):
        fixture = BuilderFixture([2, 2], bits=2)
        self.assertEqual(fixture.run(), 1)
        self.assertEqual(fixture.lookup(0), (16, 2, 0))
        self.assertEqual(fixture.lookup(2), (16, 2, 1))
        self.assertEqual(fixture.lookup(1)[0], 99)
        self.assertEqual(fixture.lookup(3)[0], 99)
        single = BuilderFixture([1], bits=7)
        self.assertEqual(single.run(), 0)
        self.assertEqual(single.lookup(0), (16, 1, 0))
        self.assertEqual(single.lookup(1)[0], 99)

    def test_workspace_allocation_append_and_subtable_links(self):
        fixture = BuilderFixture([1, 2, 2], bits=1, allocated=11)
        self.assertEqual(fixture.run(), 0)
        self.assertEqual(fixture.get(fixture.ROOT, 2), 12)
        self.assertGreater(fixture.fprs[19], 14)
        self.assertTrue(all(address >= fixture.WORKSPACE + 44
                            for address, _ in fixture.writes
                            if fixture.WORKSPACE <= address < fixture.ROOT))
        for symbol, bits, code in self.canonical([1, 2, 2]):
            self.assertEqual(fixture.lookup(code), (16, bits, symbol))
        self.assert_saved(fixture)

    def test_narrow_multilevel_tree_has_model_observed_unwritten_lookup(self):
        fixture = BuilderFixture([1, 2, 3, 3], bits=1)
        self.assertEqual(fixture.run(), 0)
        self.assertEqual(fixture.get(fixture.WORKSPACE + 8, 1), 18)
        self.assertEqual(fixture.get(fixture.WORKSPACE + 10, 2), 6)
        for symbol, bits, code in list(self.canonical([1, 2, 3, 3]))[:3]:
            self.assertEqual(fixture.lookup(code), (16, bits, symbol))
        self.assertNotIn(fixture.WORKSPACE + 4 * 9, fixture.memory)
        with self.assertRaises(KeyError):
            fixture.lookup(7)
        for requested in (2, 7):
            fixture = BuilderFixture([1, 2, 3, 3], bits=requested)
            self.assertEqual(fixture.run(), 0)
            for symbol, bits, code in self.canonical([1, 2, 3, 3]):
                self.assertEqual(fixture.lookup(code), (16, bits, symbol))

    def test_fixed_length_alphabet_operation_and_extra_tables(self):
        project = contract.InitDecompressorContractTests.project
        lengths = [8] * 144 + [9] * 112 + [7] * 24 + [8] * 8
        base_source = (project / "asm/data/2C0C0.rodata.s").read_text()
        base_body = base_source.split("dlabel D_8002C0E2\n", 1)[1]
        bases = [int(value, 16) for value in re.findall(r"\.short 0x([0-9A-F]+)", base_body)]
        extra_source = (project / "asm/data/2C120.rodata.s").read_text()
        extra_body = extra_source.split("dlabel D_8002C16F\n", 1)[1].split(
            "enddlabel D_8002C16F", 1)[0]
        extras = [int(value, 16) for value in re.findall(r"\.byte 0x([0-9A-F]+)", extra_body)]
        self.assertEqual((len(bases), len(extras)), (31, 31))
        fixture = BuilderFixture(lengths, bits=7, simple=257, bases=bases, extras=extras)
        self.assertEqual(fixture.run(), 0)
        self.assertEqual((fixture.get(fixture.ROOT, 2), fixture.fprs[19]), (1, 625))
        for symbol, bits, code in self.canonical(lengths):
            expected = ((16, bits, symbol) if symbol < 256 else
                        (15, bits, 256) if symbol == 256 else
                        (extras[symbol - 257], bits, bases[symbol - 257]))
            self.assertEqual(fixture.lookup(code), expected)
        self.assert_saved(fixture)

    def test_fixed_distance_table_incomplete_status_is_expected(self):
        project = contract.InitDecompressorContractTests.project
        source = (project / "asm/data/2C120.rodata.s").read_text()
        body = source.split("dlabel D_8002C120\n", 1)[1].split(
            "enddlabel D_8002C120", 1)[0]
        words = [int(value, 16) for value in re.findall(r"\.word 0x([0-9A-F]+)", body)]
        bases = [half for word in words for half in (word >> 16, word & 0xFFFF)]
        body = source.split("dlabel D_8002C18E\n", 1)[1].split(
            "enddlabel D_8002C18E", 1)[0]
        extras = [int(value, 16) for value in re.findall(r"\.byte 0x([0-9A-F]+)", body)]
        self.assertEqual((len(bases), len(extras)), (30, 34))
        fixture = BuilderFixture([5] * 30, bits=5, simple=0, bases=bases,
                                 extras=extras, allocated=625)
        self.assertEqual(fixture.run(), 1)
        self.assertEqual((fixture.get(fixture.ROOT, 2), fixture.fprs[19]), (626, 658))
        self.assertEqual(0x8003BE90 + fixture.get(fixture.ROOT, 2) * 4, 0x8003C858)
        for symbol, bits, code in self.canonical([5] * 30):
            self.assertEqual(fixture.lookup(code), (extras[symbol], bits, bases[symbol]))
        self.assertEqual(fixture.lookup(15)[0], 99)
        self.assertEqual(fixture.lookup(31)[0], 99)
        self.assert_saved(fixture)


if __name__ == "__main__":
    unittest.main()
