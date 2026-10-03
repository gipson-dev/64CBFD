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


class GameCommonRecordAllocatorTests(unittest.TestCase):
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
        allocator = re.search(r"PositionScaleRecord71820 \*func_15044964\(s32 size,"
                              r"[^;{]*\{\n.*?\n\}",
                              source, re.S)
        constructor = re.search(r"PositionScaleRecord71820 \*func_150448D0\(s32 arg0,.*?\n\}",
                                source, re.S)
        if record is None or allocator is None or constructor is None:
            raise AssertionError("common record source or constructor was not found")
        cls.source = ("typedef unsigned char u8; typedef short s16; typedef int s32;\n"
                      "typedef unsigned int u32;\n#define NULL ((void *)0)\n" +
                      record.group(0) + "\n" + r'''
PositionScaleRecord71820 *D_800CBE00;
static PositionScaleRecord71820 candidate, second_candidate, nodes[4];
static PositionScaleRecord71820 *allocation_result;
static u8 expected[32], second_expected[32], node_expected[4][32];
static s32 calls, fail, mutate_head, arguments[4];
static s16 positions[3], scales[3];
s32 allocate_memory(s32 size, s32 mode, s32 arg2, s32 arg3) {
    calls++;
    arguments[0] = size; arguments[1] = mode; arguments[2] = arg2; arguments[3] = arg3;
    if (mutate_head) D_800CBE00 = &nodes[0];
    return fail ? 0 : (s32)allocation_result;
}
''' + allocator.group(0) + "\n" + constructor.group(0) + "\n" + r'''
static void initialize(s32 length) {
    s32 i, j;
    calls = fail = mutate_head = 0;
    allocation_result = &candidate;
    D_800CBE00 = length ? &nodes[0] : NULL;
    for (i = 0; i < 32; i++) {
        ((u8 *)&candidate)[i] = expected[i] = 0xA5;
        ((u8 *)&second_candidate)[i] = second_expected[i] = 0xA5;
    }
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 32; j++) ((u8 *)&nodes[i])[j] = 0xA5;
        nodes[i].next = i + 1 < length ? &nodes[i + 1] : NULL;
        for (j = 0; j < 32; j++) node_expected[i][j] = ((u8 *)&nodes[i])[j];
    }
}
static void expect_half(u8 *bytes, s32 offset, s32 value) {
    s16 stored = value;
    bytes[offset] = ((u8 *)&stored)[0]; bytes[offset + 1] = ((u8 *)&stored)[1];
}
static void expect_pointer(u8 *bytes, s32 offset, void *pointer) {
    s32 i;
    for (i = 0; i < 4; i++) bytes[offset + i] = ((u8 *)&pointer)[i];
}
static void expect_header(u8 *bytes, s32 type, s32 owner, s32 state,
                          s32 selector, s32 x, s32 y, s32 z) {
    expect_pointer(bytes, 0, NULL);
    expect_half(bytes, 4, owner); expect_half(bytes, 6, x);
    expect_half(bytes, 8, y); expect_half(bytes, 10, z);
    bytes[12] = type; bytes[13] = selector; bytes[14] = state;
}
static s32 matches(PositionScaleRecord71820 *record, u8 *bytes) {
    s32 i;
    for (i = 0; i < 32; i++) if (((u8 *)record)[i] != bytes[i]) return 0;
    return 1;
}
static s32 nodes_match(void) {
    s32 i;
    for (i = 0; i < 4; i++) if (!matches(&nodes[i], node_expected[i])) return 0;
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
        self.assertEqual(executed.returncode, 0, "32-bit common record allocator fixture failed")

    def test_guest_common_header_offsets(self):
        self.run_case(r'''
CHECK(sizeof(void *) == 4 && sizeof(PositionScaleRecord71820) == 32);
CHECK(__builtin_offsetof(PositionScaleRecord71820, next) == 0);
CHECK(__builtin_offsetof(PositionScaleRecord71820, lifetime) == 4);
CHECK(__builtin_offsetof(PositionScaleRecord71820, x) == 6);
CHECK(__builtin_offsetof(PositionScaleRecord71820, y) == 8);
CHECK(__builtin_offsetof(PositionScaleRecord71820, z) == 10);
CHECK(__builtin_offsetof(PositionScaleRecord71820, type) == 12);
CHECK(__builtin_offsetof(PositionScaleRecord71820, selector) == 13);
CHECK(__builtin_offsetof(PositionScaleRecord71820, state) == 14);
CHECK(__builtin_offsetof(PositionScaleRecord71820, padF) == 15);
''')

    def test_failure_on_empty_list_has_no_record_or_list_writes(self):
        self.run_case(r'''
initialize(0); fail = 1;
CHECK(func_15044964(-123, 7, 8, 9, 10, 11, 12, 13) == NULL);
CHECK(calls == 1 && D_800CBE00 == NULL && matches(&candidate, expected) && nodes_match());
CHECK(arguments[0] == -123 && arguments[1] == 1 && arguments[2] == 0 && arguments[3] == 0);
''')

    def test_failure_preserves_existing_chain(self):
        self.run_case(r'''
initialize(4); fail = 1;
CHECK(func_15044964(0x30, 1, 2, 3, 4, 5, 6, 7) == NULL);
CHECK(calls == 1 && D_800CBE00 == &nodes[0] && nodes_match());
CHECK(matches(&candidate, expected));
''')

    def test_empty_list_publishes_identity_and_only_initializes_header(self):
        self.run_case(r'''
initialize(0);
CHECK(func_15044964(0x20, 0x1234, 0x12345678, -1, 0x133,
                   2147483647, -2147483647 - 1, -32769) == &candidate);
expect_header(expected, 0x1234, 0x12345678, -1, 0x133,
              2147483647, -2147483647 - 1, -32769);
CHECK(D_800CBE00 == &candidate && matches(&candidate, expected) && nodes_match());
CHECK(arguments[0] == 0x20 && arguments[1] == 1 && arguments[2] == 0 && arguments[3] == 0);
''')

    def test_one_node_append_preserves_head_and_prior_payload(self):
        self.run_case(r'''
initialize(1);
CHECK(func_15044964(0x20, 1, -2, 3, 4, 5, 6, 7) == &candidate);
expect_header(expected, 1, -2, 3, 4, 5, 6, 7);
expect_pointer(node_expected[0], 0, &candidate);
CHECK(D_800CBE00 == &nodes[0] && nodes_match() && matches(&candidate, expected));
''')

    def test_multi_node_append_changes_only_tail_link(self):
        self.run_case(r'''
initialize(4);
CHECK(func_15044964(0x20, 1, 2, 3, 4, 5, 6, 7) == &candidate);
expect_header(expected, 1, 2, 3, 4, 5, 6, 7);
expect_pointer(node_expected[3], 0, &candidate);
CHECK(D_800CBE00 == &nodes[0] && nodes_match() && matches(&candidate, expected));
''')

    def test_allocation_side_effect_on_head_is_observed(self):
        self.run_case(r'''
initialize(1); D_800CBE00 = NULL; mutate_head = 1;
CHECK(func_15044964(0x20, 1, 2, 3, 4, 5, 6, 7) == &candidate);
expect_header(expected, 1, 2, 3, 4, 5, 6, 7);
expect_pointer(node_expected[0], 0, &candidate);
CHECK(D_800CBE00 == &nodes[0] && nodes_match() && matches(&candidate, expected));
''')

    def test_repeated_allocations_append_distinct_records(self):
        self.run_case(r'''
initialize(0);
CHECK(func_15044964(0x20, 1, 2, 3, 4, 5, 6, 7) == &candidate);
allocation_result = &second_candidate;
CHECK(func_15044964(0x20, 8, 9, 10, 11, 12, 13, 14) == &second_candidate);
expect_header(expected, 1, 2, 3, 4, 5, 6, 7);
expect_pointer(expected, 0, &second_candidate);
expect_header(second_expected, 8, 9, 10, 11, 12, 13, 14);
CHECK(calls == 2 && D_800CBE00 == &candidate);
CHECK(matches(&candidate, expected) && matches(&second_candidate, second_expected) && nodes_match());
''')

    def test_constructor_and_real_common_allocator_integrate(self):
        self.run_case(r'''
initialize(1);
CHECK(func_150448D0(-2, 0x123, 0x456, -7, 8, 9, 0x17F, positions, scales) == &candidate);
expect_header(expected, 1, -2, 0x123, 0x456, 0, 0, 0);
expect_half(expected, 0x10, -7); expect_half(expected, 0x12, 8); expect_half(expected, 0x14, 9);
expected[0x16] = 0x7F;
expect_pointer(expected, 0x18, positions); expect_pointer(expected, 0x1C, scales);
expect_pointer(node_expected[0], 0, &candidate);
CHECK(calls == 1 && arguments[0] == 0x20 && arguments[1] == 1);
CHECK(arguments[2] == 0 && arguments[3] == 0 && D_800CBE00 == &nodes[0]);
CHECK(nodes_match() && matches(&candidate, expected));
''')

    def test_constructor_failure_through_real_common_allocator(self):
        self.run_case(r'''
initialize(4); fail = 1;
CHECK(func_150448D0(1, 2, 3, 4, 5, 6, 7, positions, scales) == NULL);
CHECK(calls == 1 && D_800CBE00 == &nodes[0] && nodes_match() && matches(&candidate, expected));
''')


if __name__ == "__main__":
    unittest.main()
