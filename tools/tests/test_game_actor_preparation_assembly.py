import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path


class GameActorPreparationAssemblyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project = Path(__file__).resolve().parents[2] / "conker"
        cls.assembly = (cls.project /
                        "asm/nonmatchings/generated_71820/func_15044660.s").read_text()
        cls.entries = [(int(address, 16), int(word, 16))
                       for address, word in re.findall(
                           r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+"
                           r"([0-9A-Fa-f]{8})\s*\*/", cls.assembly)]
        cls.words = [word for _, word in cls.entries]
        cls.reference = b"".join(struct.pack(">I", word) for word in cls.words)

    def test_complete_retail_slot_and_void_interface(self):
        self.assertEqual([address for address, _ in self.entries],
                         list(range(0x15044660, 0x150448D0, 4)))
        self.assertEqual(hashlib.sha256(self.reference).hexdigest(),
                         "d5a49547ad263ec4f509c34c0a8eb7a5c415a0bb90a84c7ef5a297c0693d8c6d")
        source = (self.project / "src/game/generated_71820.c").read_text()
        self.assertIn("void func_15044660(void *actor, f32 x, f32 y, f32 z);", source)
        self.assertIn('#pragma GLOBAL_ASM("asm/nonmatchings/generated_71820/'
                      'func_15044660.s")', source)
        self.assertNotRegex(source, r"s32 func_15044660\(")
        self.assertEqual(self.words[-4:], [0x8FBF0014, 0x27BD0030, 0x03E00008, 0])

    def test_special_branch_retains_uninitialized_stack_index_read(self):
        instructions = dict(self.entries)
        self.assertEqual(instructions[0x150446CC], 0x8FA70020)
        self.assertEqual(instructions[0x150446EC], 0x00E1001A)
        self.assertEqual(instructions[0x15044700], 0x00003812)
        self.assertEqual(instructions[0x150447FC], 0x04E00013)
        # This proves the routine itself does not initialize sp+0x20;
        # it does not establish reachability or the external stack value.
        writes_to_slot = [word for word in self.words
                          if word >> 26 in (40, 41, 43, 49, 57, 61)
                          and (word >> 21) & 31 == 29
                          and word & 0xFFFF == 0x20]
        self.assertEqual(writes_to_slot, [])
        self.assertEqual(self.words[5:8], [0x27A5002E, 0x27A6002C, 0x27A7002A])

    def test_independently_assembled_linked_bytes(self):
        for name in ("mips-linux-gnu-as", "mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(name) is None:
                self.skipTest(name + " is unavailable")
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            assembly = work / "actor.s"
            assembly.write_text('.include "macro.inc"\n.section .text,"ax"\n'
                                '.set noat\n.set noreorder\n' + self.assembly)
            symbols = {"func_1507C3E0": 0x1507C3E0, "D_800CBDD8": 0x800CBDD8,
                       "D_800CBDDC": 0x800CBDDC, "D_800CC2D0": 0x800CC2D0,
                       "D_8008FD8C": 0x8008FD8C}
            commands = [
                ["mips-linux-gnu-as", "-EB", "-march=vr4300", "-mabi=32", "-I",
                 str(self.project / "include"), "-o", str(work / "actor.o"), str(assembly)],
                ["mips-linux-gnu-ld", "-m", "elf32btsmip", "-Ttext=0x15044660",
                 "-e", "func_15044660", *["--defsym=" + name + "=" + hex(address)
                                          for name, address in symbols.items()],
                 "-o", str(work / "actor.elf"), str(work / "actor.o")],
                ["mips-linux-gnu-objcopy", "-O", "binary", "-j", ".text",
                 str(work / "actor.elf"), str(work / "actor.bin")],
            ]
            for command in commands:
                result = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
            actual = (work / "actor.bin").read_bytes()
        self.assertEqual(actual[:624], self.reference)
        self.assertEqual(actual[624:], bytes(len(actual) - 624))


if __name__ == "__main__":
    unittest.main()
