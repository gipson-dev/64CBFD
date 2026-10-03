import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


START = r'''
/* A process entry has no call-pushed return address for the i386 C ABI. */
__attribute__((force_align_arg_pointer)) void _start(void) {
    int result = run();
    __asm__ volatile(".byte 0xcd,0x80" : : "a"(1), "b"(result) : "memory");
    __builtin_unreachable();
}
'''

TYPES = "typedef unsigned char u8; typedef short s16; typedef int s32;\n" \
        "typedef unsigned int u32; typedef float f32;\n"


class GameOrientedRecordOverlapTests(unittest.TestCase):
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
        root = Path(__file__).resolve().parents[2]
        source = (root / "conker/src/game/generated_71820.c").read_text()
        record = re.search(r"typedef struct PositionScaleRecord71820 \{\n.*?"
                           r"\n\} PositionScaleRecord71820;", source, re.S)
        body = re.search(r"s32 func_15044B78\([^;{]*\{\n.*?\n\}", source, re.S)
        position_wrapper = re.search(r"s32 func_15044CE4\([^;{]*\{\n.*?\n\}",
                                     source, re.S)
        wrapper_source = (root / "conker/src/game_75E60.c").read_text()
        wrapper = re.search(r"f32 func_15048A40\(u8 arg0\) \{\n.*?\n\}",
                            wrapper_source, re.S)
        if record is None or body is None or wrapper is None or position_wrapper is None:
            raise AssertionError("overlap layout, body, or float-return wrapper was not found")
        cls.wrapper = TYPES + r'''
static s32 calls, seen;
static f32 response;
f32 func_150489B0(u8 angle) { calls++; seen = angle; return response; }
''' + wrapper.group(0) + "\n"
        cls.source = TYPES + record.group(0) + "\n" + r'''
static union { u32 align; u8 bytes[0x320]; } player_storage;
static union { u32 align; u8 bytes[0x11C]; } dimensions, other_dimensions;
#define D_800CC2D0 player_storage.bytes
static PositionScaleRecord71820 record;
static s32 calls, seen[2], mutation;
static f32 first_basis, second_basis;
static void position(f32 x, f32 y, f32 z) {
    *(f32 *)(D_800CC2D0 + 0x14) = x;
    *(f32 *)(D_800CC2D0 + 0x18) = y;
    *(f32 *)(D_800CC2D0 + 0x1C) = z;
}
static void dimensions_set(s32 height, s32 z, s32 x) {
    *(s16 *)(dimensions.bytes + 0x114) = height;
    *(s16 *)(dimensions.bytes + 0x116) = z;
    *(s16 *)(dimensions.bytes + 0x118) = x;
}
f32 func_15048A40(u8 angle) {
    seen[calls++] = angle;
    if (mutation == 1 || mutation == 2) record.flags = 255;
    if (mutation == 2) {
        position(1000, 1000, 1000);
        dimensions_set(-1000, -1000, -1000);
        *(u8 **)(D_800CC2D0 + 0x31C) = other_dimensions.bytes;
        record.x = record.y = record.z = 1000;
    }
    return first_basis;
}
f32 func_150489B0(u8 angle) {
    seen[calls++] = angle;
    if (mutation == 3) record.scaleX = record.scaleY = record.scaleZ = 0;
    if (mutation == 4) record.scaleX = record.scaleY = record.scaleZ = 100;
    return second_basis;
}
f32 fabsf(f32 value) { return __builtin_fabsf(value); }
''' + body.group(0) + "\n" + r'''
static void initialize(void) {
    s32 i;
    for (i = 0; i < 0x320; i++) D_800CC2D0[i] = 0xA5;
    for (i = 0; i < 0x11C; i++) dimensions.bytes[i] = other_dimensions.bytes[i] = 0xA5;
    for (i = 0; i < 32; i++) ((u8 *)&record)[i] = 0xA5;
    *(u8 **)(D_800CC2D0 + 0x31C) = dimensions.bytes;
    position(0, -5, 0); dimensions_set(10, 2, 3);
    record.x = record.y = record.z = 0;
    record.scaleX = 7; record.scaleY = 8; record.scaleZ = 5; record.flags = 0;
    first_basis = 0; second_basis = 1; mutation = calls = 0;
}
static f32 nan_value(void) {
    union { u32 bits; f32 value; } number;
    number.bits = 0x7FC00000; return number.value;
}
static f32 float_bits(u32 bits) {
    union { u32 bits; f32 value; } number;
    number.bits = bits; return number.value;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''
        cls.integrated_source = cls.source + position_wrapper.group(0) + "\n"
        cls.position_wrapper_source = TYPES + record.group(0) + "\n" + r'''
static union { PositionScaleRecord71820 value; s16 halfwords[16]; } record_storage;
#define record record_storage.value
static s32 overlap_calls, overlap_result, error;
static s16 expected_x, expected_y, expected_z, expected_scale;
s32 func_15044B78(PositionScaleRecord71820 *argument) {
    overlap_calls++;
    if (argument != &record || argument->x != expected_x ||
        argument->y != expected_y || argument->z != expected_z ||
        argument->scaleX != expected_scale || argument->scaleY != expected_scale ||
        argument->scaleZ != expected_scale) error = 1;
    return overlap_result;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
''' + position_wrapper.group(0) + "\n"

    def run_case(self, body, source=None):
        fixture = self.path / (self._testMethodName + ".c")
        binary = fixture.with_suffix("")
        fixture.write_text((self.source if source is None else source) +
                           "\nint run(void) {\n" + body + "\nreturn 0;\n}\n" + START)
        compiled = subprocess.run([self.compiler, *self.flags, str(fixture), "-o", str(binary)],
                                  capture_output=True, text=True)
        self.assertEqual(compiled.returncode, 0, compiled.stderr)
        executed = subprocess.run([str(binary)], capture_output=True, timeout=5)
        self.assertEqual(executed.returncode, 0, "32-bit overlap fixture failed")

    def test_guest_record_layout(self):
        self.run_case(r'''
CHECK(sizeof(record) == 32 && sizeof(void *) == 4);
CHECK(__builtin_offsetof(PositionScaleRecord71820, x) == 6);
CHECK(__builtin_offsetof(PositionScaleRecord71820, scaleX) == 0x10);
CHECK(__builtin_offsetof(PositionScaleRecord71820, scaleY) == 0x12);
CHECK(__builtin_offsetof(PositionScaleRecord71820, scaleZ) == 0x14);
CHECK(__builtin_offsetof(PositionScaleRecord71820, flags) == 0x16);
''')

    def test_interior_overlap_has_no_field_writes(self):
        self.run_case(r'''
u8 before_record[32], before_player[0x320], before_dimensions[0x11C]; s32 i;
initialize();
for (i = 0; i < 32; i++) before_record[i] = ((u8 *)&record)[i];
for (i = 0; i < 0x320; i++) before_player[i] = D_800CC2D0[i];
for (i = 0; i < 0x11C; i++) before_dimensions[i] = dimensions.bytes[i];
CHECK(func_15044B78(&record) == 1 && calls == 2 && seen[0] == 0 && seen[1] == 0);
for (i = 0; i < 32; i++) CHECK(before_record[i] == ((u8 *)&record)[i]);
for (i = 0; i < 0x320; i++) CHECK(before_player[i] == D_800CC2D0[i]);
for (i = 0; i < 0x11C; i++) CHECK(before_dimensions[i] == dimensions.bytes[i]);
''')

    def test_strict_y_bound_on_both_sides(self):
        self.run_case(r'''
s32 side;
for (side = -1; side <= 1; side += 2) {
    initialize(); position(0, side * 10 - 5, 0);
    CHECK(func_15044B78(&record) == 0 && calls == 2);
    position(0, side * 9.5f - 5, 0); CHECK(func_15044B78(&record) == 1);
    position(0, side * 10.5f - 5, 0); CHECK(func_15044B78(&record) == 0);
}
''')

    def test_strict_rotated_z_bound_on_both_sides(self):
        self.run_case(r'''
s32 side;
for (side = -1; side <= 1; side += 2) {
    initialize(); position(side * 10, -5, 0); CHECK(func_15044B78(&record) == 0);
    position(side * 9.5f, -5, 0); CHECK(func_15044B78(&record) == 1);
    position(side * 10.5f, -5, 0); CHECK(func_15044B78(&record) == 0);
}
''')

    def test_strict_rotated_x_bound_on_both_sides(self):
        self.run_case(r'''
s32 side;
for (side = -1; side <= 1; side += 2) {
    initialize(); position(0, -5, side * 10); CHECK(func_15044B78(&record) == 0);
    position(0, -5, side * 9.5f); CHECK(func_15044B78(&record) == 1);
    position(0, -5, side * 10.5f); CHECK(func_15044B78(&record) == 0);
}
''')

    def test_nonzero_origin_and_basis_rotation(self):
        self.run_case(r'''
initialize(); record.x = -200; record.y = 123; record.z = 300;
record.scaleX = 2; record.scaleY = 20;
first_basis = 1; second_basis = 0;
position(-196, 118, 315); CHECK(func_15044B78(&record) == 1);
position(-195, 118, 315); CHECK(func_15044B78(&record) == 0);
first_basis = -1; position(-196, 118, 315); CHECK(func_15044B78(&record) == 1);
''')

    def test_odd_negative_height_uses_arithmetic_half(self):
        self.run_case(r'''
initialize(); dimensions_set(-3, 2, 3); record.scaleZ = 3;
position(0, 2, 0); CHECK(func_15044B78(&record) == 1);
position(0, 1, 0); CHECK(func_15044B78(&record) == 0);
dimensions_set(3, 2, 3); record.scaleZ = 0;
position(0, -1, 0); CHECK(func_15044B78(&record) == 1);
position(0, 0, 0); CHECK(func_15044B78(&record) == 0);
''')

    def test_both_basis_terms_contribute_with_retail_signs(self):
        self.run_case(r'''
initialize(); dimensions_set(10, 0, 0); position(4, -5, 1);
first_basis = 0.6f; second_basis = 0.8f;
record.scaleX = 4; record.scaleY = 3;
CHECK(func_15044B78(&record) == 1);
record.scaleX = 3; record.scaleY = 5;
CHECK(func_15044B78(&record) == 0);
''')

    def test_signed_dimension_extremes_and_record_extents(self):
        self.run_case(r'''
initialize(); dimensions_set(-32768, -32768, -32768);
record.scaleZ = 32767; record.scaleX = record.scaleY = 32767;
position(0, 16384, 0); CHECK(func_15044B78(&record) == 0);
dimensions_set(32767, 32767, 32767);
record.scaleX = record.scaleY = record.scaleZ = -32768;
position(0, -16383, 0); CHECK(func_15044B78(&record) == 0);
record.scaleX = record.scaleY = record.scaleZ = 32767;
CHECK(func_15044B78(&record) == 1);
''')

    def test_zero_and_negative_bounds_reject(self):
        self.run_case(r'''
initialize(); record.scaleZ = -5; CHECK(func_15044B78(&record) == 0);
initialize(); record.scaleY = -2; CHECK(func_15044B78(&record) == 0);
initialize(); record.scaleX = -3; CHECK(func_15044B78(&record) == 0);
initialize(); record.scaleX = -4; CHECK(func_15044B78(&record) == 0);
''')

    def test_angle_is_unsigned_and_reloaded_between_helpers(self):
        self.run_case(r'''
s32 angle;
for (angle = 0; angle < 256; angle++) {
    initialize(); record.flags = angle; mutation = 1;
    CHECK(func_15044B78(&record) == 1 && calls == 2);
    CHECK(seen[0] == angle && seen[1] == 255);
}
''')

    def test_position_and_dimensions_are_cached_before_helpers(self):
        self.run_case(r'''
initialize(); record.flags = 128; mutation = 2;
CHECK(func_15044B78(&record) == 1 && calls == 2);
CHECK(seen[0] == 128 && seen[1] == 255);
CHECK(record.x == 1000 && *(u8 **)(D_800CC2D0 + 0x31C) == other_dimensions.bytes);
''')

    def test_record_extents_reload_after_helpers(self):
        self.run_case(r'''
initialize(); position(4, -5, 4); mutation = 3;
CHECK(func_15044B78(&record) == 0 && calls == 2);
initialize(); record.scaleX = record.scaleY = record.scaleZ = -100;
mutation = 4; CHECK(func_15044B78(&record) == 1 && calls == 2);
''')

    def test_nan_and_infinite_coordinates_reject(self):
        self.run_case(r'''
s32 axis;
for (axis = 0; axis < 3; axis++) {
    initialize(); *(f32 *)(D_800CC2D0 + 0x14 + axis * 4) = nan_value();
    CHECK(func_15044B78(&record) == 0 && calls == 2);
    initialize(); *(f32 *)(D_800CC2D0 + 0x14 + axis * 4) = float_bits(0x7F800000);
    CHECK(func_15044B78(&record) == 0 && calls == 2);
}
initialize(); first_basis = nan_value(); CHECK(func_15044B78(&record) == 0);
''')

    def test_single_precision_adjacent_boundary_values(self):
        self.run_case(r'''
initialize(); position(float_bits(0x411FFFFF), -5, 0);
CHECK(func_15044B78(&record) == 1);
position(float_bits(0x41200000), -5, 0); CHECK(func_15044B78(&record) == 0);
position(float_bits(0x41200001), -5, 0); CHECK(func_15044B78(&record) == 0);
''')

    def test_shifted_wrapper_returns_float_for_every_angle(self):
        self.run_case(r'''
s32 angle;
for (angle = 0; angle < 256; angle++) {
    calls = 0; response = angle * 0.25f - 17.5f;
    if (func_15048A40((u8)angle) != response || calls != 1 ||
        seen != ((angle - 64) & 255)) return angle % 254 + 1;
}
''', source=self.wrapper)

    def test_position_wrapper_forwards_full_signed_result_after_stores(self):
        self.run_case(r'''
s16 coordinates[3] = {-32768, 32767, -123}, scale = -33;
s32 results[4] = {0, 1, -37, 1234567}, i;
record.position = coordinates; record.scale = &scale;
expected_x = -32768; expected_y = 32767; expected_z = -123; expected_scale = -1;
for (i = 0; i < 4; i++) {
    overlap_calls = error = 0; overlap_result = results[i];
    CHECK(func_15044CE4(&record) == results[i] && overlap_calls == 1 && error == 0);
}
''', source=self.position_wrapper_source)

    def test_position_wrapper_all_signed_halfword_scales_truncate_toward_zero(self):
        self.run_case(r'''
s16 coordinates[3] = {12, -15, 300}, scale;
s32 value;
record.position = coordinates; record.scale = &scale;
expected_x = 12; expected_y = -15; expected_z = 300; overlap_result = -7;
for (value = -32768; value <= 32767; value++) {
    scale = value;
    expected_scale = value < 0 ? -((-value) >> 5) : value >> 5;
    overlap_calls = error = 0;
    CHECK(func_15044CE4(&record) == -7 && overlap_calls == 1 && error == 0);
    CHECK(scale == value && coordinates[0] == 12 && coordinates[1] == -15 &&
          coordinates[2] == 300 && record.position == coordinates && record.scale == &scale);
}
''', source=self.position_wrapper_source)

    def test_position_wrapper_preserves_unrelated_record_and_input_bytes(self):
        self.run_case(r'''
u8 before[32]; s16 coordinates[3] = {-11, 22, -33}, scale = 1024; s32 i;
for (i = 0; i < 32; i++) ((u8 *)&record)[i] = 0xA5;
record.position = coordinates; record.scale = &scale;
for (i = 0; i < 32; i++) before[i] = ((u8 *)&record)[i];
expected_x = -11; expected_y = 22; expected_z = -33; expected_scale = 32;
overlap_result = 1; CHECK(func_15044CE4(&record) == 1 && error == 0);
for (i = 0; i < 32; i++) if (!(i >= 6 && i < 12) && !(i >= 16 && i < 22))
    CHECK(before[i] == ((u8 *)&record)[i]);
CHECK(coordinates[0] == -11 && coordinates[1] == 22 && coordinates[2] == -33 && scale == 1024);
''', source=self.position_wrapper_source)

    def test_position_wrapper_aliases_observe_sequential_coordinate_stores(self):
        self.run_case(r'''
/* Source starts one halfword before destination; stores change later loads. */
s16 scale = 64;
record.lifetime = -12; record.x = 100; record.y = 200; record.z = 300;
record.position = &record_storage.halfwords[2]; record.scale = &scale;
expected_x = expected_y = expected_z = -12; expected_scale = 2;
overlap_result = 1; CHECK(func_15044CE4(&record) == 1 && error == 0 && overlap_calls == 1);
CHECK(record.lifetime == -12 && scale == 64);
''', source=self.position_wrapper_source)

    def test_position_wrapper_reads_aliased_scale_after_coordinate_stores(self):
        self.run_case(r'''
s16 coordinates[3] = {10, -65, 30};
record.position = coordinates; record.scale = &record.y;
record.y = 32000;
expected_x = 10; expected_y = -65; expected_z = 30; expected_scale = -2;
overlap_result = -3; CHECK(func_15044CE4(&record) == -3 && error == 0);
CHECK(overlap_calls == 1 && record.scale == &record.y);
''', source=self.position_wrapper_source)

    def test_position_wrapper_calls_actual_overlap_for_inside_and_boundary(self):
        self.run_case(r'''
s16 coordinates[3] = {100, -20, -100}, scale = -33;
initialize(); record.position = coordinates; record.scale = &scale;
position(100, -25, -100);
CHECK(func_15044CE4(&record) == 1 && calls == 2);
CHECK(record.x == 100 && record.y == -20 && record.z == -100);
CHECK(record.scaleX == -1 && record.scaleY == -1 && record.scaleZ == -1);
position(101, -25, -100); CHECK(func_15044CE4(&record) == 0 && calls == 4);
scale = 0; CHECK(func_15044CE4(&record) == 1 && calls == 6);
scale = -64; position(100, -25, -100);
CHECK(func_15044CE4(&record) == 0 && calls == 8);
''', source=self.integrated_source)
