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


class GameRecordDispatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.compiler = shutil.which("cc")
        if cls.compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.flags = ["-m32", "-O2", "-std=c99", "-ffreestanding", "-nostdlib",
                     "-static", "-fno-pie", "-no-pie", "-fno-stack-protector"]
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
                  "conker/src/game_6D800.c").read_text()
        body = re.search(r"void func_15040CC8\(u8 \*arg0\) \{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("record dispatcher source was not found")
        cls.source = ("typedef unsigned char u8; typedef int s32;\n"
                      "void (*D_800844B0[256])(s32);\n"
                      "s32 D_800848B0; s32 func_1500390C(s32);\n" +
                      body.group(0) + "\n" + r'''
static u8 buffer[256], expected[256];
static s32 calls, error, mode, cleanup_calls, cleanup_arg, cleanup_at;
static s32 seen[30], kinds[30];
static u8 *base(void) { return buffer + 8 + 20 * 8; }
static void dispatch(s32 address, s32 kind) {
    u8 *record = (u8 *)address;
    if (calls >= 30) { error = 1; return; }
    if (record != buffer + 8 + calls * 8) error = 2;
    seen[calls] = address;
    kinds[calls] = kind;
    if (mode == 1 && calls == 0) D_800848B0 = 0;
    if (mode == 2 && calls == 29) D_800848B0 = -1234567;
    if (mode == 3 && calls == 0) {
        buffer[16] = expected[16] = 255;
    }
    if (mode == 4 && calls == 0) D_800844B0[129] = D_800844B0[255];
    calls++;
}
static void ordinary(s32 address) { dispatch(address, 0); }
static void alternate(s32 address) { dispatch(address, 1); }
s32 func_1500390C(s32 arg) {
    cleanup_calls++;
    cleanup_arg = arg;
    cleanup_at = calls;
    D_800848B0 = 0;
    return 99;
}
static void initialize(void) {
    s32 i;
    calls = error = mode = cleanup_calls = cleanup_arg = cleanup_at = 0;
    D_800848B0 = 0;
    for (i = 0; i < 256; i++) {
        buffer[i] = expected[i] = 0xA5;
        D_800844B0[i] = ordinary;
    }
    D_800844B0[255] = alternate;
    for (i = 0; i < 30; i++) buffer[8 + i * 8] = expected[8 + i * 8] = 128 + i;
}
static s32 matches(void) {
    s32 i;
    for (i = 0; i < 256; i++) if (buffer[i] != expected[i]) return 0;
    return 1;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
''')

    def run_case(self, body):
        fixture = self.path / (self._testMethodName + ".c")
        binary = fixture.with_suffix("")
        fixture.write_text(self.source + "\nint run(void) {\n" + body +
                           "\nreturn 0;\n}\n" + START)
        compiled = subprocess.run([self.compiler, *self.flags, str(fixture), "-o", str(binary)],
                                  capture_output=True, text=True)
        self.assertEqual(compiled.returncode, 0, compiled.stderr)
        executed = subprocess.run([str(binary)], capture_output=True, timeout=5)
        self.assertEqual(executed.returncode, 0, "32-bit record dispatcher fixture failed")

    def test_direct_addresses_cover_all_thirty_slots_in_order(self):
        self.run_case(r'''
s32 i;
CHECK(sizeof(void *) == 4 && sizeof(s32) == 4);
initialize();
func_15040CC8(base());
CHECK(calls == 30 && error == 0 && cleanup_calls == 0 && matches());
for (i = 0; i < 30; i++) CHECK(seen[i] == (s32)(buffer + 8 + i * 8));
''')

    def test_unsigned_selectors_include_zero_and_255(self):
        self.run_case(r'''
initialize();
buffer[8] = expected[8] = 0;
buffer[240] = expected[240] = 255;
func_15040CC8(base());
CHECK(calls == 30 && error == 0 && kinds[0] == 0 && kinds[29] == 1 && matches());
''')

    def test_cleanup_receives_global_after_all_callbacks(self):
        self.run_case(r'''
initialize();
D_800848B0 = -98765;
func_15040CC8(base());
CHECK(calls == 30 && error == 0 && matches());
CHECK(cleanup_calls == 1 && cleanup_arg == -98765 && cleanup_at == 30);
CHECK(D_800848B0 == 0);
''')

    def test_callback_can_clear_cleanup_global(self):
        self.run_case(r'''
initialize();
D_800848B0 = 42;
mode = 1;
func_15040CC8(base());
CHECK(calls == 30 && error == 0 && cleanup_calls == 0 && matches());
''')

    def test_last_callback_can_publish_cleanup_global(self):
        self.run_case(r'''
initialize();
mode = 2;
func_15040CC8(base());
CHECK(calls == 30 && error == 0 && matches());
CHECK(cleanup_calls == 1 && cleanup_arg == -1234567 && cleanup_at == 30);
''')

    def test_callback_mutation_of_future_selector_is_observed(self):
        self.run_case(r'''
initialize();
mode = 3;
func_15040CC8(base());
CHECK(calls == 30 && error == 0 && kinds[1] == 1 && matches());
''')

    def test_callback_mutation_of_table_entry_is_observed(self):
        self.run_case(r'''
initialize();
mode = 4;
func_15040CC8(base());
CHECK(calls == 30 && error == 0 && kinds[1] == 1 && matches());
''')

    def test_repeat_dispatch_restarts_at_first_record(self):
        self.run_case(r'''
initialize();
D_800848B0 = 42;
func_15040CC8(base());
CHECK(calls == 30 && error == 0 && cleanup_calls == 1);
calls = 0;
func_15040CC8(base());
CHECK(calls == 30 && error == 0 && cleanup_calls == 1 && matches());
CHECK(seen[0] == (s32)(buffer + 8) && seen[29] == (s32)(buffer + 240));
''')


if __name__ == "__main__":
    unittest.main()
