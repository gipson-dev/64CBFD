import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path


class InitMmioAssemblyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project = Path(__file__).resolve().parents[2] / "conker"
        cls.source = cls.project / "asm/nonmatchings/init_38E0/func_100038E0.s"
        cls.assembly = cls.source.read_text()
        cls.entries = [(int(address, 16), int(word, 16))
                       for address, word in re.findall(
                           r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+"
                           r"([0-9A-Fa-f]{8})\s*\*/", cls.assembly)]
        cls.words = [word for _, word in cls.entries]
        cls.reference = b"".join(struct.pack(">I", word) for word in cls.words)

    def test_original_slot_and_assembly_ownership(self):
        self.assertEqual([address for address, _ in self.entries],
                         list(range(0x100038E0, 0x1000390C, 4)))
        self.assertEqual(hashlib.sha256(self.reference).hexdigest(),
                         "2afa60e885db40dd282ff0cf18ffe43a5716521c18c5c235975bcf8cb84d97f4")
        source = (self.project / "src/init_38E0.c").read_text()
        self.assertIn('#pragma GLOBAL_ASM("asm/nonmatchings/init_38E0/func_100038E0.s")',
                      source)
        self.assertEqual(self.words[-2:], [0x03E00008, 0])

    def test_only_three_ordered_stores_and_callee_register_preservation(self):
        # Decode only the original straight-line leaf; never execute host MMIO.
        for seed in (0xA5A5A5A5, 0xFFFFFFFF):
            registers = [(seed ^ index) & 0xFFFFFFFF for index in range(32)]
            registers[0] = 0
            before = registers[:]
            stores = []
            for word in self.words:
                opcode = word >> 26
                rs, rt = (word >> 21) & 31, (word >> 16) & 31
                immediate = word & 0xFFFF
                signed = immediate if immediate < 0x8000 else immediate - 0x10000
                if opcode == 15:
                    registers[rt] = immediate << 16
                elif opcode == 13:
                    registers[rt] = registers[rs] | immediate
                elif opcode == 9:
                    registers[rt] = (registers[rs] + signed) & 0xFFFFFFFF
                elif opcode in (41, 43):
                    size = 2 if opcode == 41 else 4
                    stores.append(((registers[rs] + signed) & 0xFFFFFFFF,
                                   size, registers[rt] & ((1 << (size * 8)) - 1)))
                else:
                    self.assertIn(word, (0, 0x03E00008))
                registers[0] = 0
            self.assertEqual(stores, [(0x80038070, 4, 0xBC000C02),
                                      (0x80038074, 2, 0x4040),
                                      (0xBC000C02, 2, 0x4040)])
            for index in (*range(16, 24), 28, 29, 30, 31):
                self.assertEqual(registers[index], before[index])

    def test_assembled_linked_bytes_equal_reference(self):
        for name in ("mips-linux-gnu-as", "mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(name) is None:
                self.skipTest(name + " is unavailable")
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            assembly = work / "mmio.s"
            assembly.write_text('.include "macro.inc"\n.section .text,"ax"\n'
                                '.set noat\n.set noreorder\n' + self.assembly)
            commands = [
                ["mips-linux-gnu-as", "-EB", "-march=vr4300", "-mabi=32", "-I",
                 str(self.project / "include"), "-o", str(work / "mmio.o"), str(assembly)],
                ["mips-linux-gnu-ld", "-m", "elf32btsmip", "-Ttext=0x100038E0",
                 "-e", "func_100038E0", "--defsym=D_80038070=0x80038070",
                 "--defsym=D_80038074=0x80038074", "-o", str(work / "mmio.elf"),
                 str(work / "mmio.o")],
                ["mips-linux-gnu-objcopy", "-O", "binary", "-j", ".text",
                 str(work / "mmio.elf"), str(work / "mmio.bin")],
            ]
            for command in commands:
                result = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
            actual = (work / "mmio.bin").read_bytes()
        self.assertEqual(actual[:44], self.reference)
        self.assertEqual(actual[44:], bytes(len(actual) - 44))
