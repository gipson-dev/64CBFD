import hashlib
import re
import struct
import unittest
from pathlib import Path


class InitBitmapAssemblyTests(unittest.TestCase):
    START = 0x8003BE70
    COUNT = 0x8003BE78
    END = 0x8003BE7C

    @classmethod
    def setUpClass(cls):
        cls.project = Path(__file__).resolve().parents[2] / "conker"
        source = (cls.project / "asm/init_5AB0.s").read_text()
        leaf = source.split("glabel func_10005BE0\n", 1)[1].split(
            "endlabel func_10005BE0", 1)[0]
        cls.entries = [(int(address, 16), int(word, 16))
                       for address, word in re.findall(
                           r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+"
                           r"([0-9A-Fa-f]{8})\s*\*/", leaf)]
        cls.words = [word for _, word in cls.entries]

    @staticmethod
    def put(memory, address, value, size):
        for index, byte in enumerate(value.to_bytes(size, "big")):
            memory[address + index] = byte

    def configured(self, start, end, count):
        memory = {}
        self.put(memory, self.START, start, 4)
        self.put(memory, self.END, end, 4)
        self.put(memory, self.COUNT, count & 0xFFFF, 2)
        return memory

    def run_leaf(self, memory, budget=50000, seed=0xA5A5A5A5):
        registers = [(seed ^ index) & 0xFFFFFFFF for index in range(32)]
        registers[0] = 0
        before = registers[:]
        reads, writes = [], []

        def execute(word):
            opcode = word >> 26
            rs, rt = (word >> 21) & 31, (word >> 16) & 31
            immediate = word & 0xFFFF
            signed = immediate if immediate < 0x8000 else immediate - 0x10000
            address = (registers[rs] + signed) & 0xFFFFFFFF
            if word == 0:
                pass
            elif opcode == 15:
                registers[rt] = immediate << 16
            elif opcode == 9:
                registers[rt] = (registers[rs] + signed) & 0xFFFFFFFF
            elif opcode == 12:
                registers[rt] = registers[rs] & immediate
            elif opcode in (33, 35):
                size = 2 if opcode == 33 else 4
                value = int.from_bytes(bytes(memory[address + i]
                                             for i in range(size)), "big")
                reads.append((address, size, value))
                if size == 2 and value & 0x8000:
                    value -= 0x10000
                registers[rt] = value & 0xFFFFFFFF
            elif opcode == 40:
                value = registers[rt] & 0xFF
                memory[address] = value
                writes.append((address, value))
            elif opcode == 0 and word & 63 == 4:
                rd = (word >> 11) & 31
                registers[rd] = (registers[rt] << (registers[rs] & 31)) & 0xFFFFFFFF
            else:
                self.fail("Unsupported bitmap instruction: %08X" % word)
            registers[0] = 0

        # Branch predicates use pre-delay registers; the delay instruction always runs.
        pc, steps, returned = 0, 0, False
        while steps < budget:
            word = self.words[pc]
            opcode = word >> 26
            if opcode in (4, 5):
                rs, rt = (word >> 21) & 31, (word >> 16) & 31
                equal = registers[rs] == registers[rt]
                take = equal if opcode == 4 else not equal
                offset = word & 0xFFFF
                offset = offset if offset < 0x8000 else offset - 0x10000
                execute(self.words[pc + 1])
                pc = pc + 1 + offset if take else pc + 2
                steps += 2
            elif word == 0x03E00008:
                execute(self.words[pc + 1])
                returned = True
                break
            else:
                execute(word)
                pc += 1
                steps += 1
        for index in (*range(16, 24), 28, 29, 30, 31):
            self.assertEqual(registers[index], before[index])
        return returned, registers, reads, writes

    def test_original_complete_slot(self):
        self.assertEqual([address for address, _ in self.entries],
                         list(range(0x10005BE0, 0x10005C2C, 4)))
        data = b"".join(struct.pack(">I", word) for word in self.words)
        self.assertEqual(hashlib.sha256(data).hexdigest(),
                         "fb041ca8620d0564873d0763acbed67a65f8b7ccfe4c5e175a7ef71631f12899")
        self.assertEqual(self.words[-2:], [0x03E00008, 0])

    def test_positive_counts_remainders_sentinels_and_repeat(self):
        for count in (*range(1, 65), 107, 235, 243, 251, 259, 267, 362, 32767):
            with self.subTest(count=count):
                start = 0x80050000
                size = (count + 7) >> 3
                end = start + size - 1
                memory = self.configured(start, end, count)
                memory.update({start + i: 0xA5 for i in range(-1, size + 1)})
                for _ in range(2):
                    returned, registers, reads, writes = self.run_leaf(memory)
                    self.assertTrue(returned)
                    self.assertEqual(registers[2], end + 1)
                    mask = (1 << (count & 7)) - 1 if count & 7 else 0xFF
                    self.assertEqual([memory[start + i] for i in range(size)],
                                     [0xFF] * (size - 1) + [mask])
                    self.assertEqual(memory[start - 1], 0xA5)
                    self.assertEqual(memory[end + 1], 0xA5)
                    self.assertEqual(reads, [(self.START, 4, start),
                                            (self.END, 4, end),
                                            (self.COUNT, 2, count)])
                    expected = [(start + i, 0xFF) for i in range(size)]
                    if count & 7:
                        expected.append((end, mask))
                    self.assertEqual(writes, expected)

    def test_zero_count_with_explicit_single_byte_endpoint_still_writes(self):
        start = 0x80050000
        memory = self.configured(start, start, 0)
        returned, registers, _, writes = self.run_leaf(memory)
        self.assertTrue(returned)
        self.assertEqual(writes, [(start, 0xFF)])
        self.assertEqual(registers[4], 0xFFFFFFFF)

    def test_zero_setup_endpoint_does_not_return_within_bounded_probe(self):
        start = 0x80050000
        memory = self.configured(start, start - 1, 0)
        returned, _, reads, writes = self.run_leaf(memory, budget=128)
        self.assertFalse(returned)
        self.assertGreater(len(writes), 1)
        self.assertEqual(writes[0], (start, 0xFF))
        self.assertNotIn(self.COUNT, [address for address, _, _ in reads])

    def test_signed_negative_count_uses_low_three_bits_after_fill(self):
        for count in (-32768, -8, -7, -1):
            with self.subTest(count=count):
                start = 0x80050000
                memory = self.configured(start, start, count)
                returned, _, _, writes = self.run_leaf(memory)
                self.assertTrue(returned)
                bits = count & 7
                self.assertEqual(writes, [(start, 0xFF)] +
                                 ([(start, (1 << bits) - 1)] if bits else []))

    def test_count_alias_is_reloaded_after_stores(self):
        memory = self.configured(self.COUNT, self.COUNT + 1, 8)
        returned, _, reads, writes = self.run_leaf(memory)
        self.assertTrue(returned)
        self.assertEqual(reads[-1], (self.COUNT, 2, 0xFFFF))
        self.assertEqual(writes, [(self.COUNT, 0xFF), (self.COUNT + 1, 0xFF),
                                  (self.COUNT + 1, 0x7F)])

    def test_endpoint_alias_uses_snapshot_not_overwritten_global(self):
        memory = self.configured(self.END, self.END + 3, 3)
        returned, _, reads, writes = self.run_leaf(memory)
        self.assertTrue(returned)
        self.assertEqual(reads[1], (self.END, 4, self.END + 3))
        self.assertEqual(writes, [(self.END + i, 0xFF) for i in range(4)] +
                                 [(self.END + 3, 7)])

    def test_direct_retail_resize_call_domain(self):
        rom_path = self.project / "conker.us.bin"
        if not rom_path.exists():
            self.skipTest("retail ROM is unavailable for caller-domain audit")
        rom = rom_path.read_bytes()
        self.assertEqual(hashlib.sha256(rom[0x34FEC:0x350D8]).hexdigest(),
                         "5abc9359b3204474a0b5f820ec61852aa816694a361643987f8f4e035970a3f5")
        calls = [offset for lo, hi in ((0x1000, 0x290D0), (0x2D4B0, 0x2275E0))
                 for offset in range(lo, hi, 4)
                 if struct.unpack_from(">I", rom, offset)[0] == 0x0C000531]
        self.assertEqual(calls, [0x350D0])
        table = struct.unpack_from(">45I", rom, 0x23A510)
        self.assertEqual(set(table), {0x15007B9C, 0x15007BE0, 0x15007C10})
        special = {index + 0x13 for index, target in enumerate(table)
                   if target == 0x15007B9C}
        self.assertEqual(special, {0x1A, 0x24, 0x2B, 0x2D, 0x30, 0x33, 0x34, 0x3F})
        # Pin the actual input-producing instructions, not merely derived arithmetic.
        expected = {0x35054: 0x24040103, 0x35058: 0x240400F3,
                    0x35068: 0x2484FFF8, 0x35078: 0x2484FFF8,
                    0x3508C: 0x24840008, 0x35098: 0x240400EB,
                    0x350B4: 0x81440011, 0x350BC: 0x248400EB,
                    0x350C8: 0x81640011, 0x350CC: 0x248400EB}
        for offset, word in expected.items():
            self.assertEqual(struct.unpack_from(">I", rom, offset)[0], word)
        counts = set(range(235 - 128, 235 + 128)) | {235, 243, 251, 259, 267}
        self.assertEqual((min(counts), max(counts)), (107, 362))
        self.assertTrue(all(0 < count <= 32767 for count in counts))


if __name__ == "__main__":
    unittest.main()
