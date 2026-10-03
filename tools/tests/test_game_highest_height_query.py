import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests.test_game_oriented_record_overlap import START, TYPES


class GameHighestHeightQueryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.compiler = shutil.which("cc")
        if cls.compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.flags = ["-m32", "-O2", "-std=c99", "-ffreestanding", "-nostdlib",
                     "-static", "-fno-pie", "-no-pie", "-fno-stack-protector",
                     "-fno-strict-aliasing", "-msse2", "-mfpmath=sse", "-ffp-contract=off"]
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
        layouts = []
        for name in ["QueryVertex71820", "QueryTriangle71820", "HeightCandidate71820",
                     "HeightResult71820"]:
            match = re.search(r"typedef struct " + name + r" \{\n.*?\n\} " + name + ";",
                              source, re.S)
            if match is None:
                raise AssertionError("height query layout was not found: " + name)
            layouts.append(match.group(0))
        body = re.search(r"s32 func_150450CC\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("height query definition was not found")
        cls.source = TYPES + "typedef unsigned short u16;\n#define NULL ((void *)0)\n" + \
                     "\n".join(layouts) + r'''
HeightCandidate71820 D_800D3300[4];
QueryTriangle71820 *D_800DBE3C;
u32 *D_800DBE5C;
f32 D_800DBE68, D_800DBE6C, D_800DBE70, D_800DBE74;
f32 D_80098D44 = -10000.0f;
static QueryTriangle71820 triangles[4];
static QueryVertex71820 vertices[4][3][2];
static u32 metadata[4];
static HeightResult71820 output;
static f32 query_position[3], threshold;
static s32 phase, error, mutation, query_x, query_z, candidate_count;
void func_1510F800(s32 mode) {
    if (mode != 0 || phase != 0 || output.height != -10000.0f) error = 1;
    phase = 1;
    if (mutation == 1) {
        query_position[0] = 1.75f; query_position[1] = 20; query_position[2] = -2.75f;
    }
}
s32 func_150A3A70(s32 x, s32 z) {
    if (phase != 1 || D_800DBE68 != query_position[0] ||
        D_800DBE6C != query_position[1] || D_800DBE70 != query_position[2] ||
        D_800DBE74 != threshold) error = 2;
    query_x = x; query_z = z; phase = 2;
    if (mutation == 2) query_position[1] = 2;
    if (mutation == 3) output.height = 6;
    return candidate_count;
}
''' + body.group(0) + r'''
static void initialize(void) {
    s32 t, v, index, byte;
    for (byte = 0; byte < 36; byte++) ((u8 *)&output)[byte] = 0xA5;
    for (t = 0; t < 4; t++) {
        for (v = 0; v < 3; v++) {
            triangles[t].vertices[v] = vertices[t][v];
            for (index = 0; index < 2; index++) {
                vertices[t][v][index].x = t * 100 + v * 10 + index;
                vertices[t][v][index].y = -t * 100 - v * 10 - index - 1;
                vertices[t][v][index].z = t * 200 + v * 20 + index;
            }
        }
        metadata[t] = 0x12340000 + t;
        D_800D3300[t].fixedHeight = (t + 1) * 256;
        D_800D3300[t].triangle = &triangles[t];
        D_800D3300[t].vertexIndex = 1;
        D_800D3300[t].padC = 0x654321;
    }
    D_800DBE3C = triangles; D_800DBE5C = metadata;
    query_position[0] = -12.75f; query_position[1] = 10; query_position[2] = 23.75f;
    threshold = 0; phase = error = mutation = 0; candidate_count = 4;
    D_800DBE68 = D_800DBE6C = D_800DBE70 = D_800DBE74 = -123;
}
static s32 copied(s32 t, s32 index) {
    s32 v;
    for (v = 0; v < 3; v++) {
        if (output.vertices[v * 3] != vertices[t][v][index].x ||
            output.vertices[v * 3 + 1] != vertices[t][v][index].y ||
            output.vertices[v * 3 + 2] != vertices[t][v][index].z) return 0;
    }
    return 1;
}
static f32 nan_value(void) {
    union { u32 bits; f32 value; } number;
    number.bits = 0x7FC00000; return number.value;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    def run_case(self, body):
        fixture = self.path / (self._testMethodName + ".c")
        binary = fixture.with_suffix("")
        fixture.write_text(self.source + "\nint run(void) {\n" + body +
                           "\nreturn 0;\n}\n" + START)
        compiled = subprocess.run([self.compiler, *self.flags, str(fixture), "-o", str(binary)],
                                  capture_output=True, text=True)
        self.assertEqual(compiled.returncode, 0, compiled.stderr)
        executed = subprocess.run([str(binary)], capture_output=True, timeout=5)
        self.assertEqual(executed.returncode, 0, "32-bit highest-height query fixture failed")

    def test_guest_layouts(self):
        self.run_case(r'''
CHECK(sizeof(QueryVertex71820) == 16 && sizeof(QueryTriangle71820) == 12);
CHECK(sizeof(HeightCandidate71820) == 16 && sizeof(HeightResult71820) == 36);
CHECK(__builtin_offsetof(HeightResult71820, vertices) == 4);
CHECK(__builtin_offsetof(HeightResult71820, metadata) == 0x18);
CHECK(__builtin_offsetof(HeightResult71820, flags) == 0x1C);
CHECK(__builtin_offsetof(HeightResult71820, state) == 0x1D);
CHECK(__builtin_offsetof(HeightResult71820, value) == 0x20);
''')

    def test_early_rejection_changes_only_bit_two_and_calls_nothing(self):
        self.run_case(r'''
s32 flag, byte; u8 before[36];
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = 11; output.flags = flag;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
    CHECK(func_150450CC(query_position, threshold, &output) == 0 && phase == 0);
    CHECK(output.flags == (flag & ~2) && D_800DBE68 == -123);
    for (byte = 0; byte < 36; byte++) if (byte != 0x1C)
        CHECK(before[byte] == ((u8 *)&output)[byte]);
}
''')

    def test_highest_eligible_candidate_and_first_equal_height(self):
        self.run_case(r'''
initialize(); D_800D3300[0].fixedHeight = 9 * 256;
D_800D3300[1].fixedHeight = 9 * 256;
D_800D3300[2].fixedHeight = 11 * 256;
CHECK(func_150450CC(query_position, threshold, &output) == 1 && error == 0);
CHECK(output.height == 9 && copied(0, 1) && output.metadata == metadata[0]);
CHECK(output.flags == 0xA7 && output.state == 1 && output.value == 0);
CHECK(query_x == -12 && query_z == 23 && phase == 2);
''')

    def test_candidate_at_query_y_and_threshold_equality_are_inclusive(self):
        self.run_case(r'''
initialize(); threshold = 10; D_800D3300[2].fixedHeight = 10 * 256;
CHECK(func_150450CC(query_position, threshold, &output) == 1);
CHECK(output.height == 10 && copied(2, 1) && error == 0);
''')

    def test_selected_below_threshold_still_publishes_and_sets_flags(self):
        self.run_case(r'''
s32 flag;
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = 5; output.flags = flag;
    CHECK(func_150450CC(query_position, threshold, &output) == 0 && error == 0);
    CHECK(output.height == 4 && output.flags == (flag | 7));
    CHECK(copied(3, 1) && output.metadata == metadata[3] && output.state == 1 && output.value == 0);
}
''')

    def test_nonpositive_count_preserves_other_output_fields(self):
        self.run_case(r'''
s32 count, byte; u8 before[36];
for (count = -5; count <= 0; count++) {
    initialize(); candidate_count = count;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
    CHECK(func_150450CC(query_position, threshold, &output) == 0 && error == 0 && phase == 2);
    CHECK(output.height == -10000 && output.flags == 0xA5);
    for (byte = 4; byte < 36; byte++) if (byte != 0x1C)
        CHECK(before[byte] == ((u8 *)&output)[byte]);
}
''')

    def test_no_eligible_height_and_strict_sentinel_bound(self):
        self.run_case(r'''
s32 i;
initialize();
for (i = 0; i < 4; i++) D_800D3300[i].fixedHeight = (i == 0 ? -10000 : -10001) * 256;
CHECK(func_150450CC(query_position, threshold, &output) == 0 && output.height == -10000);
initialize();
for (i = 0; i < 4; i++) D_800D3300[i].fixedHeight = 11 * 256;
CHECK(func_150450CC(query_position, threshold, &output) == 0 && output.height == -10000);
''')

    def test_fractional_signed_height_and_vertex_stride(self):
        self.run_case(r'''
initialize(); candidate_count = 1; threshold = -5;
D_800D3300[0].fixedHeight = -385; D_800D3300[0].vertexIndex = 0;
vertices[0][0][0].x = -32768; vertices[0][1][0].y = 32767;
CHECK(func_150450CC(query_position, threshold, &output) == 1 && error == 0);
CHECK(output.height == -1.50390625f && copied(0, 0));
''')

    def test_optional_metadata_and_signed_triangle_index(self):
        self.run_case(r'''
initialize(); D_800DBE5C = NULL; D_800DBE3C = NULL;
CHECK(func_150450CC(query_position, threshold, &output) == 1 && output.metadata == 0);
initialize(); candidate_count = 1; D_800DBE3C = &triangles[2]; D_800DBE5C = &metadata[2];
CHECK(func_150450CC(query_position, threshold, &output) == 1 && output.metadata == metadata[0]);
CHECK(error == 0);
''')

    def test_reset_and_collector_mutation_use_reloaded_data(self):
        self.run_case(r'''
initialize(); mutation = 1;
CHECK(func_150450CC(query_position, threshold, &output) == 1 && error == 0);
CHECK(query_x == 1 && query_z == -2 && D_800DBE6C == 20);
initialize(); mutation = 2;
CHECK(func_150450CC(query_position, threshold, &output) == 1 && output.height == 2 && copied(1, 1));
initialize(); mutation = 3;
CHECK(func_150450CC(query_position, threshold, &output) == 0 && output.height == 6);
CHECK(error == 0);
''')

    def test_padding_is_preserved_and_nan_comparisons_follow_retail(self):
        self.run_case(r'''
initialize();
CHECK(func_150450CC(query_position, threshold, &output) == 1);
CHECK(output.pad16 == (s16)0xA5A5 && output.pad1E == 0xA5A5);
initialize(); query_position[1] = nan_value();
CHECK(func_150450CC(query_position, threshold, &output) == 0 && phase == 2 && output.height == -10000);
initialize(); threshold = nan_value();
/* The context equality check itself is unordered for NaN; inspect the query result instead. */
CHECK(func_150450CC(query_position, threshold, &output) == 0 && phase == 2);
CHECK(output.height == 4 && output.flags == 0xA7 && copied(3, 1));
''')
