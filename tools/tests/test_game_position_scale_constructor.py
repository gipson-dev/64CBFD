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


class GamePositionScaleConstructorTests(unittest.TestCase):
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
                  "conker/src/game/generated_71820.c").read_text()
        record = re.search(r"typedef struct PositionScaleRecord71820 \{\n.*?"
                           r"\n\} PositionScaleRecord71820;", source, re.S)
        body = re.search(r"PositionScaleRecord71820 \*func_150448D0\(s32 arg0,.*?\n\}",
                         source, re.S)
        if record is None or body is None:
            raise AssertionError("position/scale constructor or record layout was not found")
        cls.source = ("typedef unsigned char u8; typedef short s16; typedef int s32;\n"
                      "typedef unsigned int u32;\n#define NULL ((void *)0)\n" +
                      record.group(0) + "\n" + r'''
static PositionScaleRecord71820 candidate;
static u8 expected[32];
static s32 calls, fail, mutate, arguments[8];
static s16 positions[3], scales[3], other_positions[3], other_scales[3];
PositionScaleRecord71820 *func_15044964(s32 size, s32 type, s32 arg2, s32 arg3,
                                       s32 arg4, s32 x, s32 y, s32 z) {
    calls++;
    arguments[0] = size; arguments[1] = type; arguments[2] = arg2;
    arguments[3] = arg3; arguments[4] = arg4; arguments[5] = x;
    arguments[6] = y; arguments[7] = z;
    if (mutate) {
        ((u8 *)&candidate)[3] = expected[3] = 0x37;
        ((u8 *)&candidate)[12] = expected[12] = 1;
    }
    return fail ? NULL : &candidate;
}
''' + body.group(0) + "\n" + r'''
static void initialize(void) {
    s32 i;
    calls = fail = mutate = 0;
    for (i = 0; i < 32; i++) ((u8 *)&candidate)[i] = expected[i] = 0xA5;
}
static void expect_half(s32 offset, s32 value) {
    s16 stored = value;
    u8 *bytes = (u8 *)&stored;
    expected[offset] = bytes[0]; expected[offset + 1] = bytes[1];
}
static void expect_word(s32 offset, void *value) {
    u8 *bytes = (u8 *)&value;
    s32 i;
    for (i = 0; i < 4; i++) expected[offset + i] = bytes[i];
}
static void expect_fields(s32 x, s32 y, s32 z, s32 flags, s16 *position, s16 *scale) {
    expect_half(0x10, x); expect_half(0x12, y); expect_half(0x14, z);
    expected[0x16] = flags;
    expect_word(0x18, position); expect_word(0x1C, scale);
}
static s32 matches(void) {
    s32 i;
    for (i = 0; i < 32; i++) if (((u8 *)&candidate)[i] != expected[i]) return 0;
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
        self.assertEqual(executed.returncode, 0, "32-bit position/scale constructor fixture failed")

    def test_guest_layout_matches_all_constructor_offsets(self):
        self.run_case(r'''
CHECK(sizeof(void *) == 4 && sizeof(s32) == 4);
CHECK(sizeof(PositionScaleRecord71820) == 0x20);
CHECK(__builtin_offsetof(PositionScaleRecord71820, scaleX) == 0x10);
CHECK(__builtin_offsetof(PositionScaleRecord71820, scaleY) == 0x12);
CHECK(__builtin_offsetof(PositionScaleRecord71820, scaleZ) == 0x14);
CHECK(__builtin_offsetof(PositionScaleRecord71820, flags) == 0x16);
CHECK(__builtin_offsetof(PositionScaleRecord71820, position) == 0x18);
CHECK(__builtin_offsetof(PositionScaleRecord71820, scale) == 0x1C);
''')

    def test_allocation_failure_returns_null_without_field_writes(self):
        self.run_case(r'''
initialize(); fail = 1;
CHECK(func_150448D0(-1, -2, -3, 4, 5, 6, 7, NULL, NULL) == NULL);
CHECK(calls == 1 && matches());
CHECK(arguments[0] == 0x20 && arguments[1] == 1);
CHECK(arguments[2] == -1 && arguments[3] == -2 && arguments[4] == -3);
CHECK(arguments[5] == 0 && arguments[6] == 0 && arguments[7] == 0);
''')

    def test_signed_forwarding_and_exact_field_write_bounds(self):
        self.run_case(r'''
initialize();
CHECK(func_150448D0(-2147483647 - 1, 2147483647, -123, -4, 5, 6, 0xA9,
                    positions, scales) == &candidate);
CHECK(calls == 1 && arguments[2] == (-2147483647 - 1));
CHECK(arguments[3] == 2147483647 && arguments[4] == -123);
CHECK(arguments[0] == 0x20 && arguments[1] == 1);
CHECK(arguments[5] == 0 && arguments[6] == 0 && arguments[7] == 0);
expect_fields(-4, 5, 6, 0xA9, positions, scales);
CHECK(matches());
''')

    def test_halfword_inputs_keep_only_low_sixteen_bits(self):
        self.run_case(r'''
s32 i;
s32 values[6] = {0, -1, 32767, 32768, 0x12345678, -2147483647 - 1};
for (i = 0; i < 6; i++) {
    initialize();
    CHECK(func_150448D0(1, 2, 3, values[i], values[(i + 1) % 6],
                       values[(i + 2) % 6], 0, positions, scales) == &candidate);
    expect_fields(values[i], values[(i + 1) % 6], values[(i + 2) % 6], 0,
                  positions, scales);
    CHECK(matches());
}
''')

    def test_flags_keep_only_low_byte_for_all_selectors(self):
        self.run_case(r'''
s32 i;
for (i = 0; i < 256; i++) {
    initialize();
    CHECK(func_150448D0(1, 2, 3, 4, 5, 6, 0x123400 + i,
                       positions, scales) == &candidate);
    expect_fields(4, 5, 6, i, positions, scales);
    CHECK(matches());
}
initialize();
CHECK(func_150448D0(1, 2, 3, 4, 5, 6, -1, NULL, NULL) == &candidate);
expect_fields(4, 5, 6, 255, NULL, NULL);
CHECK(matches());
''')

    def test_allocator_initialized_bytes_are_preserved(self):
        self.run_case(r'''
initialize(); mutate = 1;
CHECK(func_150448D0(1, 2, 3, 4, 5, 6, 7, positions, scales) == &candidate);
expect_fields(4, 5, 6, 7, positions, scales);
CHECK(matches());
''')

    def test_repeat_construction_updates_fields_and_pointer_identity(self):
        self.run_case(r'''
initialize();
CHECK(func_150448D0(1, 2, 3, 4, 5, 6, 7, positions, scales) == &candidate);
CHECK(func_150448D0(-8, -9, -10, -11, -12, -13, 0xEE,
                   other_positions, other_scales) == &candidate);
expect_fields(-11, -12, -13, 0xEE, other_positions, other_scales);
CHECK(calls == 2 && matches());
CHECK(arguments[2] == -8 && arguments[3] == -9 && arguments[4] == -10);
''')


if __name__ == "__main__":
    unittest.main()
