import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameReflectionLookAtMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        root = Path(__file__).resolve().parents[2]
        source = (root / "conker/src/game/generated_71820.c").read_text()
        body = re.search(r"void func_15047700\([^;{]*\{\n.*?\n\}", source, re.S)
        wrapper = re.search(r"void func_15047B80\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None or wrapper is None:
            raise AssertionError("reflection matrix builder/wrapper is missing")
        header = (root / "conker/include/2.0L/PR/gu.h").read_text()
        macros = "\n".join(re.findall(r"^#define\s+(?:MIN|FTOFRAC8)\([^\n]+",
                                      header, re.M))
        cls.source = highest.TYPES + macros + r'''
typedef union {
    struct { u8 col[3]; char pad1; u8 colc[3]; char pad2;
             signed char dir[3]; char pad3; } l;
    long long force_structure_alignment[2];
} Light;
typedef struct { Light l[2]; } LookAt;
typedef struct { u32 words[16]; } Mtx;
typedef char check_light_size[sizeof(Light) == 16 ? 1 : -1];
typedef char check_lookat_size[sizeof(LookAt) == 32 ? 1 : -1];
static f32 matrix[4][4], captured[4][4], parameters[9], original[9];
static LookAt lights;
static Mtx fixed;
static s32 identity_calls, roots, converted, error, mutate;
static f32 raw_sqrt(f32 value) {
    f32 result;
    __asm__("sqrtss %1, %0" : "=x"(result) : "x"(value));
    return result;
}
f32 sqrtf(f32 value) { roots++; return raw_sqrt(value); }
void guMtxIdentF(f32 mf[4][4]) {
    s32 i, j;
    if (identity_calls != 0) error = 1;
    identity_calls++;
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) mf[i][j] = i == j;
    if (mutate) for (i = 0; i < 9; i++) parameters[i] = 999;
}
void guMtxF2L(f32 mf[4][4], Mtx *output) {
    s32 i, j;
    if (identity_calls != 1 || output != &fixed || lights.l[1].l.col[1] != 128)
        error = 2;
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) captured[i][j] = mf[i][j];
    converted++;
}
''' + body.group(0) + wrapper.group(0) + r'''
static f32 dot(f32 a[3], f32 b[3]) {
    return (a[0] * b[0] + a[1] * b[1]) + a[2] * b[2];
}
static void cross(f32 a[3], f32 b[3], f32 out[3]) {
    out[0] = a[1] * b[2] - a[2] * b[1];
    out[1] = a[2] * b[0] - a[0] * b[2];
    out[2] = a[0] * b[1] - a[1] * b[0];
}
static u8 direction(f32 value) {
    f32 scaled = value * 128;
    if (!(scaled < 127)) scaled = 127;
    return (u8)(s32)scaled;
}
static void reference(f32 expected[4][4], u8 bytes[32]) {
    f32 axes[3][3], input_up[3], length, scale;
    s32 i, j;
    for (i = 0; i < 3; i++) {
        axes[2][i] = original[i + 3] - original[i];
        input_up[i] = original[i + 6];
    }
    if (original[3] == original[0] && axes[2][1] == 0 && axes[2][2] == 0) {
        axes[2][0] = axes[2][1] = 0; axes[2][2] = 1;
    }
    scale = -1.0f / raw_sqrt(dot(axes[2], axes[2]));
    for (i = 0; i < 3; i++) axes[2][i] *= scale;
    cross(input_up, axes[2], axes[0]);
    for (j = 0; j < 2; j++) {
        if (j == 1) cross(axes[2], axes[0], axes[1]);
        length = dot(axes[j], axes[j]);
        if (length == 0) {
            for (i = 0; i < 3; i++) axes[j][i] = i == j;
        } else {
            scale = 1.0f / raw_sqrt(length);
            for (i = 0; i < 3; i++) axes[j][i] *= scale;
        }
    }
    for (j = 0; j < 3; j++) {
        for (i = 0; i < 3; i++) expected[i][j] = axes[j][i];
        expected[3][j] = -dot(original, axes[j]);
        expected[j][3] = 0;
    }
    expected[3][3] = 1;
    for (i = 0; i < 32; i++) bytes[i] = 0xA5;
    for (j = 0; j < 2; j++) {
        for (i = 0; i < 8; i++) bytes[j * 16 + i] = 0;
        for (i = 0; i < 3; i++) bytes[j * 16 + 8 + i] = direction(axes[j][i]);
    }
    bytes[17] = bytes[21] = 128;
}
static f32 absolute(f32 value) { return value < 0 ? -value : value; }
static u32 bits(f32 value) {
    union { f32 value; u32 bits; } number;
    number.value = value; return number.bits;
}
static f32 from_bits(u32 value) {
    union { f32 value; u32 bits; } number;
    number.bits = value; return number.value;
}
static s32 equal(f32 a, f32 b) {
    if (a != a || b != b) return a != a && b != b;
    if ((bits(a) & 0x7FFFFFFF) == 0x7F800000 ||
        (bits(b) & 0x7FFFFFFF) == 0x7F800000) return bits(a) == bits(b);
    return absolute(a - b) <= 0.00001f * (1 + absolute(b));
}
static s32 matches(f32 mf[4][4]) {
    f32 expected[4][4]; u8 bytes[32]; s32 i, j;
    reference(expected, bytes);
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++)
        if (!equal(mf[i][j], expected[i][j])) return 0;
    for (i = 0; i < 32; i++) if (((u8 *)&lights)[i] != bytes[i]) return 0;
    return error == 0 && identity_calls == 1;
}
static void initialize(void) {
    s32 i, j; f32 values[] = {1, 2, 5, 0, 0, 0, 0, 1, 0};
    for (i = 0; i < 9; i++) parameters[i] = original[i] = values[i];
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) matrix[i][j] = 99;
    for (i = 0; i < 32; i++) ((u8 *)&lights)[i] = 0xA5;
    identity_calls = roots = converted = error = mutate = 0;
}
static void build(void) {
    s32 i;
    for (i = 0; i < 9; i++) original[i] = parameters[i];
    func_15047700(matrix, &lights, parameters[0], parameters[1], parameters[2],
                 parameters[3], parameters[4], parameters[5],
                 parameters[6], parameters[7], parameters[8]);
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_axis_aligned_camera(self):
        self.run_case(r'''
initialize(); parameters[0] = parameters[1] = 0; build();
CHECK(matches(matrix) && roots == 3);
CHECK(matrix[0][0] == 1 && matrix[1][1] == 1 && matrix[2][2] == 1);
CHECK(matrix[3][2] == -5 && lights.l[0].l.dir[0] == 127);
''')

    def test_general_cameras_against_vector_reference(self):
        self.run_case(r'''
s32 trial;
for (trial = 0; trial < 128; trial++) {
    initialize(); parameters[0] = trial * 0.17f - 10;
    parameters[1] = trial * -0.11f + 20; parameters[2] = trial * 0.07f + 2;
    parameters[3] = -4; parameters[4] = 3; parameters[5] = -8;
    parameters[6] = 0.2f; parameters[7] = 1; parameters[8] = -0.3f;
    build(); CHECK(matches(matrix));
}
''')

    def test_eye_maps_to_origin_and_basis_is_orthonormal(self):
        self.run_case(r'''
s32 i, j, k; f32 sum;
initialize(); build(); CHECK(matches(matrix));
for (j = 0; j < 3; j++) {
    sum = matrix[3][j];
    for (i = 0; i < 3; i++) sum += parameters[i] * matrix[i][j];
    CHECK(absolute(sum) < 0.00001f);
    for (k = 0; k < 3; k++) {
        sum = 0; for (i = 0; i < 3; i++) sum += matrix[i][j] * matrix[i][k];
        CHECK(absolute(sum - (j == k)) < 0.00001f);
    }
}
''')

    def test_coincident_eye_and_target(self):
        self.run_case(r'''
s32 i; initialize();
for (i = 0; i < 3; i++) parameters[i + 3] = parameters[i];
build(); CHECK(matches(matrix));
CHECK(matrix[0][0] == -1 && matrix[1][1] == 1 && matrix[2][2] == -1);
CHECK(lights.l[0].l.dir[0] == -128 && lights.l[1].l.dir[1] == 127);
''')

    def test_zero_x_difference_does_not_trigger_coincidence_alone(self):
        self.run_case(r'''
initialize(); parameters[0] = parameters[3] = 0;
parameters[2] = parameters[5] = 0; parameters[1] = 3; parameters[4] = 0;
build(); CHECK(matches(matrix) && matrix[1][2] == 1 && matrix[2][2] == 0);
''')

    def test_zero_up_uses_right_fallback(self):
        self.run_case(r'''
initialize(); parameters[6] = parameters[7] = parameters[8] = 0;
build(); CHECK(matches(matrix) && roots == 2);
CHECK(matrix[0][0] == 1 && matrix[1][0] == 0 && matrix[2][0] == 0);
''')

    def test_parallel_up_uses_right_fallback(self):
        self.run_case(r'''
initialize(); parameters[0] = parameters[1] = 0;
parameters[6] = parameters[7] = 0; parameters[8] = 1;
build(); CHECK(matches(matrix) && roots == 2 && matrix[0][0] == 1);
''')

    def test_parallel_x_look_uses_both_axis_fallbacks(self):
        self.run_case(r'''
initialize(); parameters[0] = 5; parameters[1] = parameters[2] = 0;
parameters[6] = 1; parameters[7] = parameters[8] = 0;
build(); CHECK(matches(matrix) && roots == 1);
CHECK(matrix[0][0] == 1 && matrix[1][1] == 1 && matrix[0][2] == 1);
''')

    def test_nonzero_right_with_underflowed_squared_length_uses_fallback(self):
        self.run_case(r'''
initialize(); parameters[0] = parameters[1] = 0;
parameters[7] = -1.0e-30f; build(); CHECK(matches(matrix) && roots == 2);
CHECK(matrix[0][0] == 1);
''')

    def test_direction_truncation_colors_and_untouched_padding(self):
        self.run_case(r'''
s32 i; initialize(); build(); CHECK(matches(matrix));
CHECK(lights.l[0].l.dir[0] == 125 && lights.l[0].l.dir[2] == -25);
for (i = 11; i < 16; i++) {
    CHECK(((u8 *)&lights)[i] == 0xA5 && ((u8 *)&lights)[i + 16] == 0xA5);
}
CHECK(lights.l[1].l.col[1] == 128 && lights.l[1].l.colc[1] == 128);
''')

    def test_negative_zero_coincidence(self):
        self.run_case(r'''
initialize(); parameters[0] = parameters[1] = parameters[2] = 0;
parameters[3] = parameters[4] = parameters[5] = from_bits(0x80000000);
build(); CHECK(matches(matrix) && matrix[2][2] == -1);
''')

    def test_nan_does_not_take_zero_fallback_and_direction_clamps(self):
        self.run_case(r'''
s32 i; initialize(); parameters[3] = from_bits(0x7FC12345);
build(); CHECK(matches(matrix) && roots == 3);
CHECK(matrix[0][0] != matrix[0][0] && matrix[0][2] != matrix[0][2]);
for (i = 0; i < 3; i++)
    CHECK(lights.l[0].l.dir[i] == 127 && lights.l[1].l.dir[i] == 127);
''')

    def test_parameters_survive_identity_helper_mutation(self):
        self.run_case(r'''
initialize(); mutate = 1; build(); CHECK(matches(matrix));
CHECK(parameters[0] == 999 && original[0] == 1);
''')

    def test_fixed_matrix_wrapper_handoff(self):
        self.run_case(r'''
initialize();
func_15047B80(&fixed, &lights, parameters[0], parameters[1], parameters[2],
             parameters[3], parameters[4], parameters[5],
             parameters[6], parameters[7], parameters[8]);
CHECK(converted == 1 && matches(captured));
''')


if __name__ == "__main__":
    unittest.main()
