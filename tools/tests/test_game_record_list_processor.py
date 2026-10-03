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


class GameRecordListProcessorTests(unittest.TestCase):
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
        body = re.search(r"void func_15044A28\(void\) \{\n.*?\n\}", source, re.S)
        if record is None or body is None:
            raise AssertionError("record processor or layout was not found")
        cls.source = ("typedef unsigned char u8; typedef short s16; typedef int s32;\n"
                      "typedef unsigned int u32;\n#define NULL ((void *)0)\n" +
                      record.group(0) + "\n" + r'''
PositionScaleRecord71820 *D_800CBE00;
s32 D_800BE9E4;
s32 (*D_80085E80[256])(PositionScaleRecord71820 *);
void (*D_80085E8C[256])(void);
void func_100043B4(s32 *, u32);
''' + body.group(0) + "\n" + r'''
static PositionScaleRecord71820 nodes[4], *active;
static u8 expected[4][32];
static s32 primary_calls, secondary_calls, marks, error, mode, result, mark_mutation;
static s32 seen[16], kinds[16], marked[4], secondary_kind;
static PositionScaleRecord71820 *head_at_mark[4];
static void expect_half(s32 index, s32 offset, s32 value) {
    s16 stored = value;
    expected[index][offset] = ((u8 *)&stored)[0];
    expected[index][offset + 1] = ((u8 *)&stored)[1];
}
static void expect_pointer(s32 index, PositionScaleRecord71820 *pointer) {
    s32 i;
    for (i = 0; i < 4; i++) expected[index][i] = ((u8 *)&pointer)[i];
}
static s32 primary(PositionScaleRecord71820 *record, s32 kind) {
    s32 index = record - nodes;
    if (primary_calls >= 16 || index < 0 || index >= 4) { error = 1; return 0; }
    active = record;
    seen[primary_calls] = index; kinds[primary_calls] = kind; primary_calls++;
    if (index == 0) {
        if (mode == 1) record->selector = expected[0][13] = 255;
        if (mode == 2 || mode == 3) {
            record->lifetime = 0; expect_half(0, 4, 0);
        }
        if (mode == 3) { record->next = NULL; expect_pointer(0, NULL); }
        if (mode == 4) D_800BE9E4 = 4;
    }
    return result;
}
static s32 ordinary(PositionScaleRecord71820 *record) { return primary(record, 0); }
static s32 alternate(PositionScaleRecord71820 *record) { return primary(record, 255); }
static void completion(s32 kind) {
    secondary_calls++; secondary_kind = kind;
    if (mode == 5) {
        active->lifetime = 0;
        expect_half(active - nodes, 4, 0);
    }
}
static void ordinary_completion(void) { completion(0); }
static void alternate_completion(void) { completion(255); }
void func_100043B4(s32 *record, u32 release_mode) {
    s32 index = (PositionScaleRecord71820 *)record - nodes;
    if (marks >= 4 || index < 0 || index >= 4 || release_mode != 2) { error = 2; return; }
    marked[marks] = index; head_at_mark[marks] = D_800CBE00; marks++;
    if (mark_mutation) D_800BE9E4 = 5;
}
static void snapshot(void) {
    s32 i, j;
    for (i = 0; i < 4; i++) for (j = 0; j < 32; j++) expected[i][j] = ((u8 *)&nodes[i])[j];
}
static void initialize(s32 length) {
    s32 i, j;
    primary_calls = secondary_calls = marks = error = mode = result = mark_mutation = 0;
    secondary_kind = -1;
    D_800BE9E4 = 1; D_800CBE00 = length ? &nodes[0] : NULL;
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 32; j++) ((u8 *)&nodes[i])[j] = 0xA5;
        nodes[i].next = i + 1 < length ? &nodes[i + 1] : NULL;
        nodes[i].lifetime = -1; nodes[i].state = 0;
        nodes[i].type = nodes[i].selector = 1;
    }
    for (i = 0; i < 256; i++) {
        D_80085E80[i] = ordinary; D_80085E8C[i] = ordinary_completion;
    }
    D_80085E80[255] = alternate; D_80085E8C[255] = alternate_completion;
    snapshot();
}
static s32 matches(void) {
    s32 i, j;
    for (i = 0; i < 4; i++) for (j = 0; j < 32; j++)
        if (((u8 *)&nodes[i])[j] != expected[i][j]) return 0;
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
        self.assertEqual(executed.returncode, 0, "32-bit record list processor fixture failed")

    def test_empty_list_has_no_callbacks_or_writes(self):
        self.run_case(r'''
initialize(0); func_15044A28();
CHECK(primary_calls == 0 && secondary_calls == 0 && marks == 0 && error == 0 && matches());
''')

    def test_indefinite_lifetimes_dispatch_in_order_without_field_writes(self):
        self.run_case(r'''
s32 i;
initialize(4); func_15044A28();
CHECK(primary_calls == 4 && secondary_calls == 0 && marks == 0 && error == 0 && matches());
for (i = 0; i < 4; i++) CHECK(seen[i] == i);
CHECK(D_800CBE00 == &nodes[0]);
''')

    def test_nonzero_callback_result_dispatches_completion(self):
        self.run_case(r'''
initialize(1); result = -7; func_15044A28();
CHECK(primary_calls == 1 && secondary_calls == 1 && secondary_kind == 0);
CHECK(marks == 0 && error == 0 && matches());
''')

    def test_delay_reaching_zero_waits_until_next_pass(self):
        self.run_case(r'''
initialize(2); D_800BE9E4 = 2;
nodes[0].state = 5; nodes[0].lifetime = 10; nodes[1].state = 1; snapshot();
func_15044A28();
expected[0][14] = 3; expected[1][14] = 0; expect_half(0, 4, 8);
CHECK(primary_calls == 0 && marks == 0 && matches());
func_15044A28();
expected[0][14] = 1; expect_half(0, 4, 6);
CHECK(primary_calls == 1 && seen[0] == 1 && marks == 0 && error == 0 && matches());
''')

    def test_positive_lifetime_decrements_without_removal(self):
        self.run_case(r'''
initialize(1); D_800BE9E4 = 2; nodes[0].lifetime = 5; snapshot();
func_15044A28(); expect_half(0, 4, 3);
CHECK(primary_calls == 1 && marks == 0 && D_800CBE00 == &nodes[0] && matches());
''')

    def test_head_middle_and_tail_removal_preserve_retained_record(self):
        self.run_case(r'''
initialize(4); D_800BE9E4 = 2;
nodes[0].lifetime = 2; nodes[2].lifetime = 0; nodes[3].lifetime = 2; snapshot();
func_15044A28(); expect_pointer(1, NULL);
CHECK(primary_calls == 4 && marks == 3 && marked[0] == 0 && marked[1] == 2 && marked[2] == 3);
CHECK(head_at_mark[0] == &nodes[1] && D_800CBE00 == &nodes[1] && error == 0 && matches());
''')

    def test_consecutive_expired_records_clear_head_before_marking(self):
        self.run_case(r'''
s32 i;
initialize(4);
for (i = 0; i < 4; i++) nodes[i].lifetime = 1;
snapshot(); func_15044A28();
CHECK(marks == 4 && primary_calls == 4 && D_800CBE00 == NULL && error == 0 && matches());
for (i = 0; i < 4; i++) {
    CHECK(marked[i] == i);
    CHECK(head_at_mark[i] == (i < 3 ? &nodes[i + 1] : NULL));
}
''')

    def test_cached_next_traversal_survives_callback_link_mutation(self):
        self.run_case(r'''
initialize(3); mode = 3; func_15044A28();
CHECK(primary_calls == 3 && seen[0] == 0 && seen[1] == 1 && seen[2] == 2);
CHECK(marks == 1 && marked[0] == 0 && head_at_mark[0] == NULL && D_800CBE00 == NULL);
CHECK(error == 0 && matches());
''')

    def test_unsigned_type_and_post_callback_selector_reload(self):
        self.run_case(r'''
initialize(1); mode = 1; result = 1; nodes[0].type = 255; snapshot();
func_15044A28();
CHECK(primary_calls == 1 && kinds[0] == 255 && secondary_calls == 1 && secondary_kind == 255);
CHECK(marks == 0 && error == 0 && matches());
''')

    def test_primary_callback_lifetime_change_controls_removal(self):
        self.run_case(r'''
initialize(2); mode = 2; func_15044A28();
CHECK(primary_calls == 2 && marks == 1 && marked[0] == 0);
CHECK(head_at_mark[0] == &nodes[1] && D_800CBE00 == &nodes[1] && error == 0 && matches());
''')

    def test_tick_change_in_callback_is_used_for_lifetime_updates(self):
        self.run_case(r'''
initialize(2); mode = 4; nodes[0].lifetime = nodes[1].lifetime = 10; snapshot();
func_15044A28(); expect_half(0, 4, 6); expect_half(1, 4, 6);
CHECK(primary_calls == 2 && marks == 0 && D_800BE9E4 == 4 && error == 0 && matches());
''')

    def test_release_marker_tick_change_is_used_by_next_record(self):
        self.run_case(r'''
initialize(2); mark_mutation = 1;
nodes[0].lifetime = 1; nodes[1].lifetime = 7; nodes[1].state = 10; snapshot();
func_15044A28(); expected[1][14] = 5; expect_half(1, 4, 2);
CHECK(primary_calls == 1 && marks == 1 && D_800CBE00 == &nodes[1]);
CHECK(error == 0 && matches());
''')

    def test_negative_tick_updates_truncate_byte_and_halfword(self):
        self.run_case(r'''
initialize(1); D_800BE9E4 = -300;
nodes[0].state = 255; nodes[0].lifetime = 32767; snapshot();
func_15044A28(); expected[0][14] = 43; expect_half(0, 4, 33067);
CHECK(primary_calls == 0 && marks == 0 && error == 0 && matches());
''')

    def test_word_subtraction_wrap_matches_retail_signed_branch(self):
        self.run_case(r'''
initialize(1); D_800BE9E4 = -2147483647 - 1;
nodes[0].state = 1; nodes[0].lifetime = 1; snapshot();
func_15044A28(); expected[0][14] = 0;
CHECK(primary_calls == 0 && marks == 1 && D_800CBE00 == NULL && error == 0 && matches());
''')

    def test_completion_callback_lifetime_change_is_observed(self):
        self.run_case(r'''
initialize(1); mode = 5; result = 1; func_15044A28();
CHECK(primary_calls == 1 && secondary_calls == 1 && marks == 1 && marked[0] == 0);
CHECK(D_800CBE00 == NULL && error == 0 && matches());
''')


if __name__ == "__main__":
    unittest.main()
