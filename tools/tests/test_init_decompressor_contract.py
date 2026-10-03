import hashlib
import re
import struct
import unittest
import zlib
from pathlib import Path


class InitDecompressorContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project = Path(__file__).resolve().parents[2] / "conker"
        cls.source = (cls.project / "asm/init_5AB0.s").read_text()

    @classmethod
    def entries(cls, name):
        body = cls.source.split("glabel " + name + "\n", 1)[1].split(
            "endlabel " + name, 1)[0]
        return [(int(address, 16), int(word, 16)) for address, word in re.findall(
            r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+"
            r"([0-9A-Fa-f]{8})\s*\*/", body)]

    def stored(self, payload, produced=0, limit=0x10000, alignment=5,
               preload=0, complement=None, budget=2000000):
        # Only the original stored-block leaf is modeled, not a general MIPS CPU.
        code = dict(self.entries("func_10006828"))
        length = len(payload)
        complement = length ^ 0xFFFF if complement is None else complement
        data = struct.pack("<HH", length, complement) + payload
        reservoir = ((1 << alignment) - 1) | (
            int.from_bytes(data[:preload], "little") << alignment)
        self.assertLessEqual(alignment + preload * 8, 32)
        memory = {0x10000 + i: byte for i, byte in enumerate(data)}
        registers, fprs = [0] * 32, [0] * 32
        registers[23] = 0x10000 + preload
        registers[28], registers[30] = reservoir, alignment + preload * 8
        registers[31] = 0xDEAD0000
        fprs[16], fprs[17], fprs[18] = 0x40000, produced, limit
        reads, writes = [], []

        def signed(value):
            return value if value < 0x80000000 else value - 0x100000000

        def execute(word):
            op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
            rd, shift, fn = (word >> 11) & 31, (word >> 6) & 31, word & 63
            immediate = word & 0xFFFF
            displacement = immediate if immediate < 0x8000 else immediate - 0x10000
            address = (registers[rs] + displacement) & 0xFFFFFFFF
            if word == 0:
                pass
            elif op == 17 and rs in (0, 4):
                if rs == 0:
                    registers[rt] = fprs[rd]
                else:
                    fprs[rd] = registers[rt]
            elif op == 9:
                registers[rt] = registers[rs] + displacement
            elif op == 10:
                registers[rt] = int(signed(registers[rs]) < displacement)
            elif op == 12:
                registers[rt] = registers[rs] & immediate
            elif op == 36:
                registers[rt] = memory[address]
                reads.append(address)
            elif op == 40:
                memory[address] = registers[rt] & 0xFF
                writes.append((address, memory[address]))
            elif op == 0 and fn in (2, 4, 6, 33, 35, 37, 39, 42):
                left, right = registers[rs], registers[rt]
                operations = {
                    2: lambda: right >> shift,
                    4: lambda: right << (left & 31),
                    6: lambda: right >> (left & 31),
                    33: lambda: left + right,
                    35: lambda: left - right,
                    37: lambda: left | right,
                    39: lambda: ~(left | right),
                    42: lambda: int(signed(left) < signed(right)),
                }
                registers[rd] = operations[fn]()
            else:
                self.fail("Unsupported stored-block instruction %08X" % word)
            registers[:] = [value & 0xFFFFFFFF for value in registers]
            registers[0] = 0

        pc = 0x10006828
        for _ in range(budget):
            word = code[pc]
            op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
            if op in (4, 5, 21):
                take = registers[rs] == registers[rt]
                if op != 4:
                    take = not take
                offset = word & 0xFFFF
                offset = offset if offset < 0x8000 else offset - 0x10000
                if take or op != 21:
                    execute(code[pc + 4])
                pc = pc + 4 + offset * 4 if take else pc + 8
            elif word == 0x03E00008:
                execute(code[pc + 4])
                return registers, fprs, reads, writes
            else:
                execute(word)
                pc += 4
        self.fail("Stored-block instruction budget exhausted")

    def test_stored_leaf_complete_reference_slot(self):
        entries = self.entries("func_10006828")
        self.assertEqual([address for address, _ in entries],
                         list(range(0x10006828, 0x1000692C, 4)))
        data = b"".join(struct.pack(">I", word) for _, word in entries)
        self.assertEqual(hashlib.sha256(data).hexdigest(),
                         "f4f01aceaebcbe190ba42cc9519797ac3c96a94a17e3e7558801480cd5722cc4")
        rom = self.project / "conker.us.bin"
        if rom.exists():
            self.assertEqual(data, rom.read_bytes()[0x6828:0x692C])

    def test_byte_alignment_and_preloaded_reservoir(self):
        payload = bytes(range(64))
        for alignment in range(8):
            for preload in range(4):
                with self.subTest(alignment=alignment, preload=preload):
                    registers, fprs, reads, writes = self.stored(
                        payload, produced=7, alignment=alignment, preload=preload)
                    self.assertEqual(registers[2], 0)
                    self.assertEqual(fprs[17], 71)
                    self.assertEqual(reads, list(range(0x10000 + preload,
                                                     0x10000 + 4 + len(payload))))
                    self.assertEqual(writes, list(enumerate(payload, 0x40007)))
                    self.assertEqual((registers[28], registers[30]), (0, 0))

    def test_zero_length_still_checks_strict_limit(self):
        registers, fprs, _, writes = self.stored(b"", produced=7, limit=8)
        self.assertEqual((registers[2], fprs[17], writes), (0, 7, []))
        registers, fprs, _, writes = self.stored(b"", produced=7, limit=7)
        self.assertEqual((registers[2], fprs[17], writes), (1, 7, []))

    def test_limit_equality_and_excess_reject_before_output(self):
        for limit in (10, 11):
            registers, fprs, reads, writes = self.stored(b"abcd", produced=7,
                                                        limit=limit)
            self.assertEqual((registers[2], fprs[17], writes), (1, 7, []))
            self.assertEqual(reads, list(range(0x10000, 0x10004)))
        registers, fprs, _, writes = self.stored(b"abcd", produced=7, limit=12)
        self.assertEqual((registers[2], fprs[17], len(writes)), (0, 11, 4))

    def test_bad_complement_does_not_publish_or_write(self):
        registers, fprs, reads, writes = self.stored(b"abcd", produced=9,
                                                    complement=0)
        self.assertEqual((registers[2], fprs[17], writes), (1, 9, []))
        self.assertEqual(reads, list(range(0x10000, 0x10004)))
        # Its failure delay slot shifts the reservoir, but skips the bit-count update.
        self.assertEqual(registers[30], 16)

    def test_stored_payloads_against_zlib_raw_deflate_oracle(self):
        for length in (0, 1, 255, 256, 4096, 65535):
            payload = bytes((i * 37 + 11) & 0xFF for i in range(length))
            raw = b"\x01" + struct.pack("<HH", length, length ^ 0xFFFF) + payload
            self.assertEqual(zlib.decompress(raw, -15), payload)
            registers, fprs, _, writes = self.stored(payload)
            self.assertEqual(registers[2], 0)
            self.assertEqual(fprs[17], length)
            self.assertEqual(bytes(value for _, value in writes), payload)
            self.assertEqual([address for address, _ in writes],
                             list(range(0x40000, 0x40000 + length)))

    def test_shared_frame_and_integer_fpr_contract(self):
        entry = dict(self.entries("func_1000625C"))
        self.assertEqual(entry[0x1000625C], 0x27BDF578)  # Allocate 0xA88.
        self.assertEqual(entry[0x1000628C], 0x24970002)  # Input starts at +2.
        self.assertEqual(entry[0x100062AC], 0x26F70002)  # Non-1172 starts at +4.
        self.assertEqual(entry[0x10006290], 0x44858000)  # Output base in f16.
        self.assertEqual(entry[0x100062DC], 0x448A9000)  # Limit in f18.
        self.assertEqual(entry[0x100062EC], 0x44028800)  # Count in return delay.
        for name, slot in (("func_1000632C", 0xA6C),
                           ("func_10006380", 0xA68),
                           ("func_10006424", 0xA44),
                           ("func_1000692C", 0xA44)):
            self.assertEqual(self.entries(name)[0][1], 0xAFBF0000 | slot)
        builder = dict(self.entries("func_1000696C"))
        self.assertEqual(builder[0x10006970], 0x44901000)
        self.assertEqual(builder[0x10006998], 0x44139800)

    def test_fixed_wrapper_discards_decoder_status(self):
        words = [word for _, word in self.entries("func_1000692C")]
        self.assertEqual(words[10:], [0x0C001B80, 0, 0x8FB60A74,
                                     0x8FBF0A44, 0x03E00008, 0x24020000])


if __name__ == "__main__":
    unittest.main()
