import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.progress import parse_file
from tools.tests import test_game_highest_height_query as highest


class GameEntityScanAssemblyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project = Path(__file__).resolve().parents[2] / "conker"
        cls.names = ["func_150A64B8", "func_150A6568", "func_150A66FC"]
        cls.fragments = [(cls.project / ("asm/nonmatchings/generated_D3040/" + name + ".s"))
                         .read_text() for name in cls.names]
        cls.instructions = [[(int(address, 16), int(word, 16))
                             for address, word in re.findall(
                                 r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+"
                                 r"([0-9A-Fa-f]{8})\s*\*/", fragment)]
                            for fragment in cls.fragments]
        cls.expected = [b"".join(struct.pack(">I", word) for _, word in entries)
                        for entries in (cls.instructions[0],
                                        cls.instructions[1] + cls.instructions[2])]

    def test_all_required_entries_are_assembly_and_inventory_is_not_c(self):
        source = (self.project / "src/game/generated_D3040.c").read_text()
        for name in self.names:
            self.assertIn('#pragma GLOBAL_ASM("asm/nonmatchings/generated_D3040/' + name + '.s")',
                          source)
            self.assertNotRegex(source, r"s32 " + name + r"\([^;{]*\{\s*return 0;")
        self.assertEqual(parse_file(str(self.project), "src/game/generated_D3040",
                                    ["func_150A6568"]), [])

    def test_reference_spans_and_output_stores_are_original(self):
        self.assertEqual([address for address, _ in self.instructions[0]],
                         list(range(0x150A64B8, 0x150A64C8, 4)))
        self.assertEqual([address for entries in self.instructions[1:] for address, _ in entries],
                         list(range(0x150A6568, 0x150A6760, 4)))
        self.assertEqual(hashlib.sha256(self.expected[0]).hexdigest(),
                         "f10e5e336e5fb76e6def91eb6fe9dbb0a6adb09eaa07aced495e21d6525df078")
        self.assertEqual(hashlib.sha256(self.expected[1]).hexdigest(),
                         "e4e19a59547819b91826d68e9ea9d3802c274fea1eaa43aa0e4cb50a5e0aa135")
        self.assertEqual(self.instructions[1][:2], [(0x150A6568, 0x00001025),
                                                   (0x150A656C, 0xACC00000)])
        self.assertIn((0x150A670C, 0xACD00000), self.instructions[2])

    def test_assembled_noncontiguous_spans_and_cross_entry_branches_match(self):
        for name in ("mips-linux-gnu-as", "mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(name) is None:
                self.skipTest(name + " is unavailable")
        assembly = ('.include "macro.inc"\n.set noat\n.set noreorder\n.set gp=64\n'
                    '.section .return,"ax"\n' + self.fragments[0] +
                    '\n.section .producer,"ax"\n' + "\n".join(self.fragments[1:]))
        externals = {name: int(address, 16) for name, address in re.findall(
            r"\b((?:func|D)_([0-9A-Fa-f]{8}))\b", assembly) if name not in self.names}
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            (work / "scan.s").write_text(assembly)
            (work / "scan.ld").write_text(
                "SECTIONS { .return 0x150A64B8 : { *(.return) } "
                ".producer 0x150A6568 : { *(.producer) } }")
            definitions = [argument for name, address in sorted(externals.items())
                           for argument in ("--defsym", f"{name}=0x{address:X}")]
            commands = [
                ["mips-linux-gnu-as", "-EB", "-march=vr4300", "-mabi=32", "-I",
                 str(self.project / "include"), "-o", str(work / "scan.o"), str(work / "scan.s")],
                ["mips-linux-gnu-ld", "-m", "elf32btsmip", "-T", str(work / "scan.ld"),
                 "-e", "func_150A6568", *definitions, "-o", str(work / "scan.elf"),
                 str(work / "scan.o")],
            ]
            for command in commands:
                result = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
            for index, section in enumerate((".return", ".producer")):
                output = work / (section[1:] + ".bin")
                result = subprocess.run(["mips-linux-gnu-objcopy", "-O", "binary", "-j", section,
                                         str(work / "scan.elf"), str(output)],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                actual = output.read_bytes()
                size = len(self.expected[index])
                self.assertEqual(actual[:size], self.expected[index])
                self.assertEqual(actual[size:], bytes(len(actual) - size))
                if index == 1:
                    for offset, target in ((0x10, 0x150A64C0), (0x19C, 0x150A6628)):
                        word = struct.unpack_from(">I", actual, offset)[0]
                        displacement = struct.unpack(">h", struct.pack(">H", word & 0xFFFF))[0]
                        self.assertEqual(0x150A6568 + offset + 4 + displacement * 4, target)


class GameEntityScanPointerContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        project = Path(__file__).resolve().parents[2] / "conker"
        snippets = []
        for path, name in (("src/game/generated_D3040.c", "func_150A6500"),
                           ("src/game/generated_71820.c", "func_15045714")):
            match = re.search(r"(?:s32|void) " + name + r"\([^;{]*\{\n.*?\n\}",
                              (project / path).read_text(), re.S)
            if match is None:
                raise AssertionError(name + " definition is missing")
            snippets.append(match.group(0))
        cls.source = highest.TYPES + "typedef unsigned short u16;\n" + r'''
static s32 *expected_secondary;
static s32 x_value, z_value, selector_value, calls, resets, error;
void func_1510F800(s32 mode) {
    if (mode != 2 || calls != 0) error = 2;
    resets++;
}
s32 func_150A6568(s32 x, s32 z, s32 *secondary, s32 selector,
                  s32 xEnd, s32 zEnd, s32 yMin, s32 yMax) {
    if (resets != 1 || secondary != expected_secondary || xEnd != x || zEnd != z ||
        yMin != -10000 || yMax != 20000) error = 1;
    x_value = x; z_value = z; selector_value = selector; calls++;
    *secondary = 13;
    return -2;
}
''' + "\n".join(snippets) + "\n" + r'''
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_real_wrappers_forward_pointer_bounds_and_publish_both_counts(self):
        self.run_case(r'''
s32 counts[4] = {0x1234, 0, 0, 0x5678};
f32 position[3] = {-12.75f, 99.0f, 23.75f};
expected_secondary = &counts[1];
func_15045714(position, 0xFFFF, &counts[2], &counts[1]);
CHECK(calls == 1 && error == 0 && x_value == -12 && z_value == 23 && selector_value == 65535);
CHECK(counts[0] == 0x1234 && counts[1] == 13 && counts[2] == -2 && counts[3] == 0x5678);
''')

    def test_primary_store_follows_secondary_store_when_outputs_alias(self):
        self.run_case(r'''
s32 count = 0;
f32 position[3] = {-32768.0f, 0, 32767.0f};
expected_secondary = &count;
func_15045714(position, 0, &count, &count);
CHECK(calls == 1 && error == 0 && x_value == -32768 && z_value == 32767);
CHECK(count == -2);
''')
