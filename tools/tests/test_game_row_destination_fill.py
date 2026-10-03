import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


START = r'''
void _start(void) {
    int result = run();
    __asm__ volatile(".byte 0xcd,0x80" : : "a"(1), "b"(result) : "memory");
    __builtin_unreachable();
}
'''


class GameRowDestinationFillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.compiler = shutil.which("cc")
        if cls.compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.flags = ["-m32", "-O2", "-std=c99", "-fno-strict-aliasing",
                     "-ffreestanding", "-nostdlib", "-static", "-fno-pie",
                     "-no-pie", "-fno-stack-protector"]
        probe = cls.path / "probe.c"
        probe.write_text("int run(void) { return 0; }\n" + START)
        result = subprocess.run([cls.compiler, *cls.flags, str(probe), "-o",
                                 str(cls.path / "probe")], capture_output=True, text=True)
        if result.returncode:
            raise unittest.SkipTest("freestanding 32-bit compiler support is unavailable")
        try:
            result = subprocess.run([str(cls.path / "probe")], capture_output=True, timeout=5)
        except OSError as error:
            raise unittest.SkipTest("32-bit host execution is unavailable") from error
        if result.returncode:
            raise unittest.SkipTest("32-bit host execution probe failed")
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_49D30.c").read_text()
        body = re.search(r"void func_1501CDC0\(s32 index\) \{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("row destination fill definition was not found")
        cls.source = ("typedef unsigned char u8; typedef int s32;\n"
                      "typedef unsigned int u32;\n"
                      "u8 D_800C363A[3];\n"
                      "u8 *D_800C3960[3][30] __attribute__((aligned(256)));\n" +
                      body.group(0) + "\n" + r'''
static u8 buffers[3][30][24];
static void initialize(void) {
    s32 row, slot, byte;
    for (row = 0; row < 3; row++) {
        D_800C363A[row] = 0;
        for (slot = 0; slot < 30; slot++) {
            D_800C3960[row][slot] = &buffers[row][slot][4];
            for (byte = 0; byte < 24; byte++) buffers[row][slot][byte] = 0xA5;
        }
    }
}
static s32 verify(s32 selectedRow, s32 active) {
    s32 row, slot, byte;
    for (row = 0; row < 3; row++) {
        for (slot = 0; slot < 30; slot++) {
            if (D_800C3960[row][slot] != &buffers[row][slot][4]) return 0;
            for (byte = 0; byte < 24; byte++) {
                u8 expected = row == selectedRow && slot < active && byte >= 4 && byte < 20
                              ? 0xFF : 0xA5;
                if (buffers[row][slot][byte] != expected) return 0;
            }
        }
    }
    return 1;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
''')

    def run_case(self, body):
        fixture = self.path / (self._testMethodName + ".c")
        binary = fixture.with_suffix("")
        fixture.write_text(self.source + "\nint run(void) {\n" + body + "\nreturn 0;\n}\n" + START)
        compiled = subprocess.run([self.compiler, *self.flags, str(fixture), "-o", str(binary)],
                                  capture_output=True, text=True)
        self.assertEqual(compiled.returncode, 0, compiled.stderr)
        executed = subprocess.run([str(binary)], capture_output=True, timeout=5)
        self.assertEqual(executed.returncode, 0, "32-bit row-fill fixture failed")

    def test_zero_count_skips_even_null_destinations(self):
        self.run_case(r'''
initialize();
D_800C3960[1][0] = (u8 *)0;
func_1501CDC0(1);
D_800C3960[1][0] = &buffers[1][0][4];
CHECK(verify(1, 0));
''')

    def test_single_destination_has_exact_sixteen_byte_bounds(self):
        self.run_case(r'''
initialize(); D_800C363A[0] = 1;
func_1501CDC0(0);
CHECK(verify(0, 1));
''')

    def test_selected_row_uses_guest_pointer_stride(self):
        self.run_case(r'''
CHECK(sizeof(void *) == 4 && sizeof(D_800C3960[0]) == 120);
initialize(); D_800C363A[0] = 2; D_800C363A[1] = 3; D_800C363A[2] = 4;
func_1501CDC0(1);
CHECK(verify(1, 3));
CHECK(D_800C363A[0] == 2 && D_800C363A[1] == 3 && D_800C363A[2] == 4);
''')

    def test_all_thirty_destination_slots(self):
        self.run_case(r'''
initialize(); D_800C363A[2] = 30;
func_1501CDC0(2);
CHECK(verify(2, 30));
''')

    def test_duplicate_destinations_and_repeated_fill(self):
        self.run_case(r'''
initialize(); D_800C363A[0] = 3;
D_800C3960[0][1] = D_800C3960[0][2] = D_800C3960[0][0];
func_1501CDC0(0); func_1501CDC0(0);
D_800C3960[0][1] = &buffers[0][1][4];
D_800C3960[0][2] = &buffers[0][2][4];
CHECK(verify(0, 1));
''')

    def test_pointer_is_reloaded_between_individual_stores(self):
        self.run_case(r'''
s32 byte;
u8 *table = (u8 *)D_800C3960;
CHECK(((u32)table & 255) == 0 && sizeof(D_800C3960) > 0x10E);
initialize(); D_800C363A[0] = 1;
D_800C3960[0][0] = table;
func_1501CDC0(0);
CHECK(D_800C3960[0][0] == table + 255);
for (byte = 0x100; byte <= 0x10E; byte++) CHECK(table[byte] == 0xFF);
for (byte = 0; byte < 24; byte++) CHECK(buffers[0][0][byte] == 0xA5);
''')


if __name__ == "__main__":
    unittest.main()
