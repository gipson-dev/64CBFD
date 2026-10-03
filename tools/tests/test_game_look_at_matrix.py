import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameLookAtMatrixTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        body = re.search(r"void func_15047390\([^;{]*\{\n.*?\n\}", source, re.S)
        wrapper = re.search(r"void func_15047688\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None or wrapper is None:
            raise AssertionError("look-at matrix builder/wrapper is missing")
        cls.source = highest.TYPES + r'''
typedef struct { u32 words[16]; } Mtx;
static f32 matrix[4][4], captured[4][4], parameters[9], original_parameters[9];
static f32 roots[3], expected_roots[3];
f32 D_80098D60 = 0.001f, D_80098D64 = 0.001f, D_80098D68 = 0.001f;
static s32 phase, error, identity_mutation, matrix_mutation, forced_stage, constant_mutation;
static u32 forced_bits;
static Mtx fixed_output;
static f32 raw_sqrt(f32 value) {
    f32 result;
    __asm__("sqrtss %1, %0" : "=x"(result) : "x"(value));
    return result;
}
static f32 from_bits(u32 bits) {
    union { f32 value; u32 bits; } number;
    number.bits = bits; return number.value;
}
static u32 bits(f32 value) {
    union { f32 value; u32 bits; } number;
    number.value = value; return number.bits;
}
void guMtxIdentF(f32 mf[4][4]) {
    s32 i, j;
    if (phase != 0) error = 1;
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) mf[i][j] = i == j;
    phase = 1;
    if (identity_mutation) for (i = 0; i < 9; i++) parameters[i] = 999;
}
f32 sqrtf(f32 value) {
    s32 stage = phase - 1, i, j;
    if (stage < 0 || stage > 2) { error = 2; return 1; }
    roots[stage] = value; phase++;
    if (matrix_mutation) for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) matrix[i][j] = 99;
    if (stage == forced_stage) {
        if (constant_mutation) {
            if (stage == 0) D_80098D60 = 2;
            if (stage == 1) D_80098D64 = 3;
            if (stage == 2) D_80098D68 = 4;
        }
        return from_bits(forced_bits);
    }
    return raw_sqrt(value);
}
void guMtxF2L(f32 mf[4][4], Mtx *output) {
    s32 i, j;
    if (phase != 4 || output != &fixed_output) error = 3;
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) captured[i][j] = mf[i][j];
    phase = 5;
}
''' + body.group(0) + wrapper.group(0) + r'''
static f32 absolute(f32 value) { return value < 0 ? -value : value; }
static f32 reference_root(f32 squared, s32 stage) {
    expected_roots[stage] = squared;
    if (stage == forced_stage) return from_bits(forced_bits);
    return raw_sqrt(squared);
}
static void cross(const f32 a[3], const f32 b[3], f32 out[3]) {
    out[0] = a[1] * b[2] - a[2] * b[1];
    out[1] = a[2] * b[0] - a[0] * b[2];
    out[2] = a[0] * b[1] - a[1] * b[0];
}
static f32 dot(const f32 a[3], const f32 b[3]) {
    return (a[0] * b[0] + a[1] * b[1]) + a[2] * b[2];
}
static void reference(f32 expected[4][4]) {
    f32 axes[3][3], up[3], scale, length, fallback[3];
    s32 i, stage;
    fallback[0] = 0.001f; fallback[1] = 0.001f; fallback[2] = 0.001f;
    if (constant_mutation && forced_stage >= 0) fallback[forced_stage] = forced_stage + 2;
    for (i = 0; i < 3; i++) {
        axes[2][i] = original_parameters[i + 3] - original_parameters[i];
        up[i] = original_parameters[i + 6];
    }
    for (stage = 0; stage < 3; stage++) {
        f32 *axis = axes[stage == 0 ? 2 : stage == 1 ? 0 : 1];
        if (stage == 1) cross(up, axes[2], axes[0]);
        if (stage == 2) cross(axes[2], axes[0], axes[1]);
        length = reference_root(dot(axis, axis), stage);
        if (length == 0) length = fallback[stage];
        scale = (stage == 0 ? -1.0f : 1.0f) / length;
        for (i = 0; i < 3; i++) axis[i] *= scale;
    }
    for (stage = 0; stage < 3; stage++) {
        for (i = 0; i < 3; i++) expected[i][stage] = axes[stage][i];
        expected[3][stage] = -dot(original_parameters, axes[stage]);
        expected[stage][3] = 0;
    }
    expected[3][3] = 1;
}
static s32 equal_value(f32 a, f32 b) {
    if (a != a || b != b) return a != a && b != b;
    if ((bits(a) & 0x7FFFFFFF) == 0x7F800000 ||
        (bits(b) & 0x7FFFFFFF) == 0x7F800000) return bits(a) == bits(b);
    return absolute(a - b) <= 0.00001f * (1 + absolute(b));
}
static s32 matches(f32 mf[4][4]) {
    s32 i, j; f32 expected[4][4];
    reference(expected);
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++)
        if (!equal_value(mf[i][j], expected[i][j])) return 0;
    for (i = 0; i < 3; i++) if (!equal_value(roots[i], expected_roots[i])) return 0;
    return error == 0;
}
static void initialize(void) {
    s32 i, j; f32 values[] = {1, 2, 5, 0, 0, 0, 0, 1, 0};
    for (i = 0; i < 9; i++) parameters[i] = original_parameters[i] = values[i];
    for (i = 0; i < 4; i++) for (j = 0; j < 4; j++) matrix[i][j] = 99;
    phase = error = identity_mutation = matrix_mutation = constant_mutation = 0;
    forced_stage = -1; forced_bits = 0;
    D_80098D60 = D_80098D64 = D_80098D68 = 0.001f;
}
static void build(void) {
    s32 i;
    for (i = 0; i < 9; i++) original_parameters[i] = parameters[i];
    func_15047390(matrix, parameters[0], parameters[1], parameters[2],
                  parameters[3], parameters[4], parameters[5],
                  parameters[6], parameters[7], parameters[8]);
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_axis_aligned_camera_and_translation(self):
        self.run_case(r'''
initialize(); parameters[0] = parameters[1] = 0; build();
CHECK(phase == 4 && matches(matrix));
CHECK(matrix[0][0] == 1 && matrix[1][1] == 1 && matrix[2][2] == 1);
CHECK(matrix[3][0] == 0 && matrix[3][1] == 0 && matrix[3][2] == -5);
''')

    def test_general_cameras_match_independent_vector_reference(self):
        self.run_case(r'''
s32 case_number;
for (case_number = 1; case_number < 129; case_number++) {
    initialize(); parameters[0] = case_number * 0.25f;
    parameters[1] = case_number % 7 - 3.25f; parameters[2] = case_number % 11 + 1.5f;
    parameters[3] = -case_number * 0.5f; parameters[4] = case_number % 5 + 0.75f;
    parameters[5] = -case_number % 13 - 2.75f;
    parameters[6] = 0.25f; parameters[7] = 1; parameters[8] = -0.5f;
    build(); CHECK(phase == 4 && matches(matrix));
}
''')

    def test_basis_is_orthonormal_and_eye_transforms_to_origin(self):
        self.run_case(r'''
s32 i, j, k; f32 dot_product, transformed;
initialize(); build();
for (i = 0; i < 3; i++) {
    for (j = 0; j < 3; j++) {
        dot_product = 0;
        for (k = 0; k < 3; k++) dot_product += matrix[k][i] * matrix[k][j];
        CHECK(absolute(dot_product - (i == j)) < 0.00001f);
    }
    transformed = matrix[3][i];
    for (k = 0; k < 3; k++) transformed += original_parameters[k] * matrix[k][i];
    CHECK(absolute(transformed) < 0.00001f);
}
''')

    def test_degenerate_eye_and_target_produce_finite_zero_basis(self):
        self.run_case(r'''
s32 i, j;
initialize(); for (i = 0; i < 3; i++) parameters[i + 3] = parameters[i];
build(); CHECK(phase == 4 && matches(matrix));
for (i = 0; i < 4; i++) for (j = 0; j < 4; j++)
    CHECK(matrix[i][j] == (i == 3 && j == 3));
''')

    def test_zero_or_parallel_up_uses_right_and_up_fallbacks(self):
        self.run_case(r'''
s32 mode, i;
for (mode = 0; mode < 2; mode++) {
    initialize();
    for (i = 0; i < 3; i++) parameters[i + 6] = mode ? parameters[i + 3] - parameters[i] : 0;
    build(); CHECK(phase == 4 && matches(matrix));
    CHECK(roots[1] == 0 && roots[2] == 0);
}
''')

    def test_small_nonzero_length_is_not_replaced_by_epsilon(self):
        self.run_case(r'''
initialize(); parameters[0] = parameters[1] = 0; parameters[2] = 0.0000000001f;
build(); CHECK(phase == 4 && matches(matrix));
CHECK(matrix[2][2] > 0.999f && roots[0] > 0);
''')

    def test_each_zero_length_fallback_is_loaded_after_sqrt_call(self):
        self.run_case(r'''
s32 stage;
for (stage = 0; stage < 3; stage++) {
    initialize(); forced_stage = stage; constant_mutation = 1;
    build(); CHECK(phase == 4 && matches(matrix));
}
''')

    def test_negative_zero_sqrt_return_triggers_each_fallback(self):
        self.run_case(r'''
s32 stage;
for (stage = 0; stage < 3; stage++) {
    initialize(); forced_stage = stage; forced_bits = 0x80000000;
    build(); CHECK(phase == 4 && matches(matrix));
}
''')

    def test_nan_length_is_not_treated_as_zero(self):
        self.run_case(r'''
s32 stage;
for (stage = 0; stage < 3; stage++) {
    initialize(); forced_stage = stage; forced_bits = 0x7FC12345;
    build(); CHECK(phase == 4 && matches(matrix));
    CHECK(matrix[0][1] != matrix[0][1]);
}
''')

    def test_parameters_remain_by_value_across_identity_helper(self):
        self.run_case(r'''
initialize(); identity_mutation = 1; build();
CHECK(phase == 4 && parameters[0] == 999 && matches(matrix));
''')

    def test_final_matrix_overwrites_helper_mutations(self):
        self.run_case(r'''
initialize(); matrix_mutation = 1; build();
CHECK(phase == 4 && matches(matrix));
''')

    def test_fixed_matrix_wrapper_passes_complete_float_matrix(self):
        self.run_case(r'''
initialize();
func_15047688(&fixed_output, parameters[0], parameters[1], parameters[2],
              parameters[3], parameters[4], parameters[5],
              parameters[6], parameters[7], parameters[8]);
CHECK(phase == 5 && matches(captured));
''')
