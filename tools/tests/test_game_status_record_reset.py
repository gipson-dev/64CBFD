import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests.test_game_row_destination_fill import START


class GameStatusRecordResetTests(unittest.TestCase):
    STORES = ((0x00, 4), (0x04, 4), (0x2B, 1), (0x20, 2),
              (0x3E, 1), (0x3F, 1), (0x41, 1), (0x43, 1),
              (0x44, 1), (0x10, 4), (0x2A, 1), (0x14, 4),
              (0x18, 4), (0x1C, 4), (0x0C, 4), (0x08, 4))

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / "conker/src/game/generated_20AE20.c").read_text()
        record = re.search(r"typedef struct \{\n    f32 unk0;.*?\n\} StatusReset20AE20;",
                           source, re.S)
        body = re.search(r"void func_151E5034\(void\) \{\n.*?\n\}", source, re.S)
        if record is None or body is None:
            raise AssertionError("status record reset production definition missing")
        cls.source = ("typedef unsigned char u8; typedef signed char s8;\n"
                      "typedef short s16; typedef float f32;\n"
                      "s8 *D_8008FDD4;\n" + record.group(0) + "\n" + body.group(0))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        assembly = (cls.root / "conker/asm/20AE20.s").read_text()
        slot = assembly.split("glabel func_151E5034\n", 1)[1].split(
            "glabel func_151E50C8", 1)[0]
        cls.entries = [(int(address, 16), int(word, 16)) for address, word in
                       re.findall(r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+"
                                  r"([0-9A-Fa-f]{8})\s*\*/", slot)]
        cls.reference = b"".join(struct.pack(">I", word) for _, word in cls.entries)

    def test_complete_retail_slot_and_ordered_pointer_reloads(self):
        self.assertEqual([address for address, _ in self.entries],
                         list(range(0x151E5034, 0x151E50C8, 4)))
        image = (self.root / "conker/conker.us.bin").read_bytes()
        offset = 0x2D4B0 + 0x1E5034
        self.assertEqual(self.reference, image[offset:offset + 148])
        words = [word for _, word in self.entries]
        self.assertEqual(words[:3], [0x3C028009, 0x44800000, 0x2442FDD4])
        for index, (offset, size) in enumerate(self.STORES):
            load, store = words[3 + index * 2:5 + index * 2]
            self.assertEqual(load >> 26, 35)
            self.assertEqual((load >> 21) & 31, 2)
            self.assertEqual(load & 0xFFFF, 0)
            self.assertEqual(store >> 26, {1: 40, 2: 41, 4: 57}[size])
            self.assertEqual((store >> 21) & 31, (load >> 16) & 31)
            self.assertEqual((store >> 16) & 31, 0)
            self.assertEqual(store & 0xFFFF, offset)
        self.assertEqual(words[-2:], [0x03E00008, 0])

    def run_host(self, extra):
        compiler = shutil.which("cc")
        if compiler is None:
            self.skipTest("host C compiler is unavailable")
        fixture = self.path / (self._testMethodName + ".c")
        fixture.write_text(self.source + "\n" + extra + "\n" + START)
        binary = fixture.with_suffix("")
        result = subprocess.run([compiler, "-m32", "-O2", "-std=c99",
            "-fno-strict-aliasing", "-ffreestanding", "-nostdlib", "-static",
            "-fno-pie", "-no-pie", "-fno-stack-protector", "-Wall", "-Wextra",
            "-Werror", str(fixture), "-o", str(binary)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([str(binary)], capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, "32-bit reset fixture failed")

    def test_record_layout(self):
        assertions = "\n".join(
            "typedef char offset_%X[__builtin_offsetof(StatusReset20AE20, unk%X) == 0x%X ? 1 : -1];"
            % (offset, offset, offset) for offset, _ in self.STORES)
        self.run_host(assertions + "\ntypedef char record_size[sizeof(StatusReset20AE20) == 0x48 ? 1 : -1];\n"
                      "int run(void) { return 0; }")

    def test_zero_bits_untouched_bytes_pointer_selection_and_repeat(self):
        ranges = ",".join("{%d,%d}" % row for row in self.STORES)
        self.run_host(r'''
static u8 first[0x58], second[0x58], savedFirst[0x58];
static int ranges[16][2] = {''' + ranges + r'''};
int run(void) {
    int seed, index, store, pass;
    for (seed = 0; seed < 256; seed += 85) {
        for (index = 0; index < 0x58; index++) {
            first[index] = seed;
            second[index] = seed ^ 0x5A;
        }
        D_8008FDD4 = (s8 *)(first + 4);
        for (pass = 0; pass < 2; pass++) {
            func_151E5034();
            if (D_8008FDD4 != (s8 *)(first + 4)) return 1;
            for (index = 0; index < 0x58; index++) {
                int expected = seed;
                for (store = 0; store < 16; store++) {
                    if (index >= ranges[store][0] + 4 &&
                        index < ranges[store][0] + ranges[store][1] + 4) expected = 0;
                }
                if (first[index] != expected || second[index] != (seed ^ 0x5A)) return 2;
            }
            for (store = 0; store < 16; store++) first[ranges[store][0] + 4] = 0xFF;
        }
        for (index = 0; index < 0x58; index++) savedFirst[index] = first[index];
        D_8008FDD4 = (s8 *)(second + 4);
        func_151E5034();
        if (D_8008FDD4 != (s8 *)(second + 4)) return 3;
        for (index = 0; index < 0x58; index++) {
            int expected = seed ^ 0x5A;
            for (store = 0; store < 16; store++) {
                if (index >= ranges[store][0] + 4 &&
                    index < ranges[store][0] + ranges[store][1] + 4) expected = 0;
            }
            if (second[index] != expected || first[index] != savedFirst[index]) return 4;
        }
    }
    return 0;
}
''')

    def test_independently_compiled_linked_slot_is_exact_without_guards(self):
        compiler = self.root / "ido/ido5.3_recomp/cc"
        if not compiler.is_file():
            self.skipTest("IDO compiler is unavailable")
        for name in ("mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(name) is None:
                self.skipTest(name + " is unavailable")
        source, obj = self.path / "reset.c", self.path / "reset.o"
        source.write_text(self.source.replace("s8 *D_8008FDD4;", "extern s8 *D_8008FDD4;") + "\n")
        result = subprocess.run([str(compiler), "-c", "-32", "-G", "0", "-Xfullwarn",
            "-Xcpluscomm", "-signed", "-nostdinc", "-non_shared", "-Wab,-r4300_mul",
            "-mips2", "-o32", "-O2", "-g3", "-o", str(obj), str(source)],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, "")
        elf, binary = self.path / "reset.elf", self.path / "reset.bin"
        script = self.path / "reset.ld"
        script.write_text("SECTIONS { .text 0x151E5034 : SUBALIGN(4) { *(.text) } }\n")
        subprocess.run(["mips-linux-gnu-ld", "-m", "elf32btsmip",
            "-T", str(script), "-e", "func_151E5034",
            "--defsym=D_8008FDD4=0x8008FDD4", "-o", str(elf), str(obj)],
            check=True, capture_output=True, text=True)
        subprocess.run(["mips-linux-gnu-objcopy", "-O", "binary", "-j", ".text",
            str(elf), str(binary)], check=True, capture_output=True, text=True)
        actual = binary.read_bytes()
        self.assertEqual(actual[:148], self.reference)
        self.assertEqual(actual[148:], bytes(len(actual) - 148))


if __name__ == "__main__":
    unittest.main()
