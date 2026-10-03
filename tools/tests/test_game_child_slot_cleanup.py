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


class GameChildSlotCleanupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.compiler = shutil.which("cc")
        if cls.compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        # Guest record access overlays typed slots on a byte-addressed buffer.
        cls.flags = ["-m32", "-O2", "-std=c99", "-fno-strict-aliasing", "-ffreestanding", "-nostdlib",
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
                  "conker/src/game/generated_1DD500.c").read_text()
        slot = re.search(r"typedef struct \{\n    void \*child;.*?\n\} CleanupSlot1DD500;",
                         source, re.S)
        body = re.search(r"void func_151B1918\(u8 \*arg0\) \{\n.*?\n\}", source, re.S)
        if slot is None or body is None:
            raise AssertionError("child-slot cleanup source was not found")
        cls.source = ("typedef unsigned char u8; typedef int s32;\n"
                      "typedef unsigned int u32; typedef float f32;\n"
                      "#define NULL ((void *)0)\n"
                      "void func_1516972C(void *);\n" + slot.group(0) + "\n" +
                      body.group(0) + "\n" + r'''
static union { u32 alignment; u8 bytes[0xC0]; } record;
static u8 expected[0xC0];
static s32 owners[11], calls, error, mode;
static void *seen[11];
static CleanupSlot1DD500 *slots(void) {
    return (CleanupSlot1DD500 *)(record.bytes + 0x34);
}
static void initialize(u32 mask) {
    s32 i;
    calls = error = mode = 0;
    for (i = 0; i < 0xC0; i++) record.bytes[i] = expected[i] = 0xA5;
    for (i = 0; i < 11; i++) {
        slots()[i].child = (mask & (1U << i)) ? &owners[i] : NULL;
        slots()[i].first = 100 + i;
        slots()[i].second = 200 + i;
    }
    for (i = 0x30; i < 0xB8; i++) expected[i] = 0;
    for (i = 0xB8; i < 0xBC; i++) expected[i] = 0;
}
static s32 matches(void) {
    s32 i;
    for (i = 0; i < 0xC0; i++) {
        if (record.bytes[i] != expected[i]) return 0;
    }
    return 1;
}
void func_1516972C(void *child) {
    s32 i;
    if (calls >= 11) { error = 1; return; }
    seen[calls] = child;
    if (*(s32 *)(record.bytes + 0x30) != 0 ||
        *(u32 *)(record.bytes + 0xB8) != 0) error = 2;
    if (mode == 1) {
        if (slots()[calls].child != child ||
            slots()[calls].first != 100 + calls ||
            slots()[calls].second != 200 + calls) error = 3;
        for (i = 0; i < calls; i++) {
            if (slots()[i].child || slots()[i].first || slots()[i].second) error = 4;
        }
    }
    if (mode == 2 && calls == 0) {
        slots()[0].child = &owners[10];
        slots()[0].first = 777;
        slots()[0].second = 888;
        slots()[1].child = &owners[1];
        record.bytes[0x2C] = expected[0x2C] = 42;
    }
    calls++;
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
        self.assertEqual(executed.returncode, 0, "32-bit cleanup fixture failed")

    def test_actual_slot_layout_uses_guest_word_width(self):
        self.run_case(r'''
CHECK(sizeof(void *) == 4 && sizeof(s32) == 4);
CHECK(sizeof(CleanupSlot1DD500) == 12);
CHECK(__builtin_offsetof(CleanupSlot1DD500, first) == 4);
CHECK(__builtin_offsetof(CleanupSlot1DD500, second) == 8);
''')

    def test_empty_slots_still_clear_all_words(self):
        self.run_case(r'''
initialize(0);
func_151B1918(record.bytes);
CHECK(calls == 0 && error == 0 && matches());
''')

    def test_all_children_release_in_order_before_slot_clear(self):
        self.run_case(r'''
s32 i;
initialize(0x7FF);
mode = 1;
func_151B1918(record.bytes);
CHECK(calls == 11 && error == 0 && matches());
for (i = 0; i < 11; i++) CHECK(seen[i] == &owners[i]);
''')

    def test_sparse_children_include_first_and_last_slots(self):
        self.run_case(r'''
initialize((1U << 0) | (1U << 5) | (1U << 10));
func_151B1918(record.bytes);
CHECK(calls == 3 && error == 0 && matches());
CHECK(seen[0] == &owners[0] && seen[1] == &owners[5] && seen[2] == &owners[10]);
''')

    def test_duplicate_children_are_not_deduplicated(self):
        self.run_case(r'''
initialize(7);
slots()[1].child = slots()[2].child = slots()[0].child;
func_151B1918(record.bytes);
CHECK(calls == 3 && error == 0 && matches());
CHECK(seen[0] == &owners[0] && seen[1] == &owners[0] && seen[2] == &owners[0]);
''')

    def test_callback_mutation_is_observed_then_current_slot_cleared(self):
        self.run_case(r'''
initialize(1);
mode = 2;
func_151B1918(record.bytes);
CHECK(calls == 2 && error == 0 && matches());
CHECK(seen[0] == &owners[0] && seen[1] == &owners[1]);
''')

    def test_repeated_cleanup_does_not_release_again(self):
        self.run_case(r'''
initialize(0x7FF);
func_151B1918(record.bytes);
func_151B1918(record.bytes);
CHECK(calls == 11 && error == 0 && matches());
''')


if __name__ == "__main__":
    unittest.main()
