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


class GameOwnerEventTests(unittest.TestCase):
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
                  "conker/src/game/generated_1E73B0.c").read_text()
        body = re.search(r"void func_151BD21C\(u8 \*arg0, u8 \*arg1, u8 arg2\) \{\n.*?\n\}",
                         source, re.S)
        if body is None:
            raise AssertionError("owner event definition was not found")
        cls.source = ("typedef unsigned char u8; typedef unsigned short u16;\n"
                      "typedef int s32; typedef unsigned int u32;\n" +
                      body.group(0) + "\n" + r'''
static union { u32 alignment; u8 bytes[0xA0]; } record;
static union { u32 alignment; u8 bytes[0x10]; } target, event;
static u8 expectedRecord[0xA0], expectedTarget[0x10], originalEvent[0x10];
static void copy(u8 *to, const u8 *from, s32 size) {
    s32 i;
    for (i = 0; i < size; i++) to[i] = from[i];
}
static s32 equal(const u8 *left, const u8 *right, s32 size) {
    s32 i;
    for (i = 0; i < size; i++) if (left[i] != right[i]) return 0;
    return 1;
}
static void initialize(s32 owner, s32 first, s32 second) {
    s32 i;
    for (i = 0; i < 0xA0; i++) record.bytes[i] = 0xA5;
    for (i = 0; i < 0x10; i++) { target.bytes[i] = 0x5A; event.bytes[i] = 0xC3; }
    *(u8 **)(record.bytes + 0x98) = target.bytes;
    *(u16 *)(record.bytes + 0x1E) = 0x8101;
    record.bytes[0x30] = 0x77;
    *(s32 *)target.bytes = owner;
    target.bytes[4] = 0x21;
    *(s32 *)event.bytes = first;
    *(s32 *)(event.bytes + 4) = second;
    event.bytes[8] = 0x82;
    event.bytes[9] = 0x93;
}
static s32 check(u8 code) {
    s32 owner = *(s32 *)target.bytes;
    s32 first = *(s32 *)event.bytes;
    s32 second = *(s32 *)(event.bytes + 4);
    copy(expectedRecord, record.bytes, 0xA0);
    copy(expectedTarget, target.bytes, 0x10);
    copy(originalEvent, event.bytes, 0x10);
    if (code == 0 && (owner == first || target.bytes[4] == event.bytes[4])) {
        expectedRecord[0x30] = 0;
        *(u16 *)(expectedRecord + 0x1E) |= 8;
    }
    if (code == 0x2D && (owner == first || owner == second)) {
        *(s32 *)expectedTarget = owner == first ? second : first;
        expectedTarget[4] = owner == first ? event.bytes[9] : event.bytes[8];
    }
    func_151BD21C(record.bytes, event.bytes, code);
    return equal(record.bytes, expectedRecord, 0xA0) &&
           equal(target.bytes, expectedTarget, 0x10) &&
           equal(event.bytes, originalEvent, 0x10);
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
        self.assertEqual(executed.returncode, 0, "32-bit owner-event fixture failed")

    def test_zero_event_owner_match_preserves_other_flag_bits(self):
        self.run_case(r'''
CHECK(sizeof(void *) == 4 && sizeof(s32) == 4);
initialize(123, 123, 456);
CHECK(check(0));
CHECK(record.bytes[0x30] == 0 && *(u16 *)(record.bytes + 0x1E) == 0x8109);
''')

    def test_zero_event_selector_match_is_independent_of_owner(self):
        self.run_case(r'''
initialize(123, 456, 789);
event.bytes[4] = target.bytes[4];
CHECK(check(0));
CHECK(record.bytes[0x30] == 0 && *(u16 *)(record.bytes + 0x1E) == 0x8109);
''')

    def test_zero_event_nonmatch_is_unchanged(self):
        self.run_case(r'''
initialize(123, 456, 789);
CHECK(check(0));
CHECK(record.bytes[0x30] == 0x77 && *(u16 *)(record.bytes + 0x1E) == 0x8101);
''')

    def test_remap_forward_uses_second_owner_and_selector_nine(self):
        self.run_case(r'''
initialize(-123, -123, 456);
CHECK(check(0x2D));
CHECK(*(s32 *)target.bytes == 456 && target.bytes[4] == 0x93);
''')

    def test_remap_reverse_uses_first_owner_and_selector_eight(self):
        self.run_case(r'''
initialize(-456, 123, -456);
CHECK(check(0x2D));
CHECK(*(s32 *)target.bytes == 123 && target.bytes[4] == 0x82);
''')

    def test_remap_equal_endpoints_prefers_forward_arm(self):
        self.run_case(r'''
initialize(123, 123, 123);
CHECK(check(0x2D));
CHECK(*(s32 *)target.bytes == 123 && target.bytes[4] == 0x93);
''')

    def test_remap_nonmatch_and_other_event_codes_do_nothing(self):
        self.run_case(r'''
s32 code;
initialize(123, 456, 789);
CHECK(check(0x2D));
for (code = 1; code < 256; code++) {
    if (code == 0x2D) continue;
    initialize(123, 123, 123);
    CHECK(check((u8)code));
}
''')

    def test_event_and_target_aliasing_preserves_store_read_order(self):
        self.run_case(r'''
initialize(123, 123, 456);
*(u8 **)(record.bytes + 0x98) = event.bytes;
func_151BD21C(record.bytes, event.bytes, 0x2D);
CHECK(*(s32 *)event.bytes == 456 && event.bytes[4] == 0x93);
initialize(456, 123, 456);
*(u8 **)(record.bytes + 0x98) = event.bytes + 4;
func_151BD21C(record.bytes, event.bytes, 0x2D);
CHECK(*(s32 *)(event.bytes + 4) == 123 && event.bytes[8] == 0x82);
''')


if __name__ == "__main__":
    unittest.main()
