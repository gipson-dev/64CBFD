import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.progress import parse_file


class GameCollectorAssemblyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.project = cls.root / "conker"
        source = (cls.project / "src/game/generated_D0F20.c").read_text()
        cls.paths = re.findall(r'^#pragma GLOBAL_ASM\("([^"]+)"\)$', source, re.M)
        cls.source = source
        cls.fragments = [(cls.project / path).read_text() for path in cls.paths]
        cls.instructions = []
        for fragment in cls.fragments:
            cls.instructions.extend((int(address, 16), int(word, 16))
                                    for address, word in re.findall(
                                        r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+"
                                        r"([0-9A-Fa-f]{8})\s*\*/", fragment))

    def test_all_entry_labels_have_assembly_ownership(self):
        self.assertEqual(len(self.paths), 23)
        self.assertEqual(len(set(self.paths)), 23)
        self.assertNotIn("return 0", self.source)
        for path, fragment in zip(self.paths, self.fragments):
            self.assertRegex(fragment, r"(?m)^\s*glabel " + re.escape(Path(path).stem) + r"$")
        groups = ["func_150A3A70", "func_150A3FC4", "func_150A43E0", "func_150A44F0",
                  "func_150A4B04", "func_150A4FA0"]
        self.assertEqual(parse_file(str(self.project), "src/game/generated_D0F20", groups), [])

    def test_reference_words_cover_the_complete_retail_span(self):
        addresses = [address for address, _ in self.instructions]
        self.assertEqual(addresses, list(range(0x150A3A70, 0x150A50C0, 4)))
        expected = b"".join(struct.pack(">I", word) for _, word in self.instructions)
        self.assertEqual(len(expected), 5712)
        self.assertEqual(hashlib.sha256(expected).hexdigest(),
                         "1986046720a68f120f612d0de32520c4cb623fc396d13b46073add33be6de04f")

    def test_assembled_group_and_cross_body_branch_match_retail_words(self):
        for tool in ["mips-linux-gnu-as", "mips-linux-gnu-ld", "mips-linux-gnu-objcopy"]:
            if shutil.which(tool) is None:
                self.skipTest(tool + " is unavailable")
        assembly = ('.include "macro.inc"\n.section .text,"ax"\n.set noat\n'
                    '.set noreorder\n.set gp=64\n' + "\n".join(self.fragments))
        defined = {Path(path).stem for path in self.paths}
        externals = {name: int(address, 16) for name, address in re.findall(
            r"\b((?:func|D)_([0-9A-Fa-f]{8}))\b", assembly) if name not in defined}
        externals["allocate_memory"] = 0x10003C40
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            source = work / "collector.s"
            source.write_text(assembly)
            assembled = subprocess.run(
                ["mips-linux-gnu-as", "-EB", "-march=vr4300", "-mabi=32", "-I",
                 str(self.project / "include"), "-o", str(work / "collector.o"), str(source)],
                capture_output=True, text=True)
            self.assertEqual(assembled.returncode, 0, assembled.stderr)
            definitions = [argument for name, address in sorted(externals.items())
                           for argument in ["--defsym", f"{name}=0x{address:X}"]]
            linked = subprocess.run(
                ["mips-linux-gnu-ld", "-m", "elf32btsmip", "-Ttext", "0x150A3A70",
                 "-e", "func_150A3A70", *definitions, "-o", str(work / "collector.elf"),
                 str(work / "collector.o")], capture_output=True, text=True)
            self.assertEqual(linked.returncode, 0, linked.stderr)
            copied = subprocess.run(
                ["mips-linux-gnu-objcopy", "-O", "binary", "-j", ".text",
                 str(work / "collector.elf"), str(work / "collector.bin")],
                capture_output=True, text=True)
            self.assertEqual(copied.returncode, 0, copied.stderr)
            actual = (work / "collector.bin").read_bytes()
        expected = b"".join(struct.pack(">I", word) for _, word in self.instructions)
        self.assertEqual(actual, expected)
        instruction = struct.unpack_from(">I", actual, 8)[0]
        displacement = struct.unpack(">h", struct.pack(">H", instruction & 0xFFFF))[0]
        self.assertEqual(0x150A3A78 + 4 + displacement * 4, 0x150A4A94)
