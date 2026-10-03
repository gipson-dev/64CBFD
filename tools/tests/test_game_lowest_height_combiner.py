import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameLowestHeightCombinerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        layout = re.search(r"typedef struct HeightResult71820 \{\n.*?\n\} HeightResult71820;",
                           source, re.S)
        body = re.search(r"s32 func_150461D0\([^;{]*\{\n.*?\n\}", source, re.S)
        if layout is None or body is None:
            raise AssertionError("lowest-height combiner definition/layout is missing")
        cls.source = highest.TYPES + "typedef unsigned short u16;\n" + layout.group(0) + r'''
static f32 position[3], threshold, expected_bound;
static HeightResult71820 output, original, first_value, second_value;
static HeightResult71820 *first_pointer;
static s32 *primary_pointer, *secondary_pointer;
static s32 phase, error, mutation, first_return, second_return;
static u16 expected_selector;
static u32 bits(f32 value) {
    union { f32 value; u32 bits; } number;
    number.value = value; return number.bits;
}
static s32 same(const HeightResult71820 *a, const HeightResult71820 *b) {
    s32 i;
    for (i = 0; i < 36; i++) if (((const u8 *)a)[i] != ((const u8 *)b)[i]) return 0;
    return 1;
}
void func_15045714(f32 *p, u16 selector, s32 *primary, s32 *secondary) {
    if (phase != 0 || p != position || selector != expected_selector ||
        primary != secondary + 1) error = 1;
    *primary = 3; *secondary = 2;
    primary_pointer = primary; secondary_pointer = secondary; phase = 1;
    if (mutation == 1) {
        output.height = -999; output.flags = 0;
        position[1] = 999; threshold = -999;
    }
}
s32 func_15045880(f32 *p, f32 bound, s32 *count, HeightResult71820 *result) {
    if (phase != 1 || p != position || bits(bound) != bits(expected_bound) ||
        count != primary_pointer || *count != 3 || result == &output ||
        !same(result, &original)) error = 2;
    first_pointer = result; *result = first_value; phase = 2;
    if (mutation == 2) output = first_value;
    return first_return;
}
s32 func_15045D48(f32 *p, f32 bound, s32 *count, HeightResult71820 *result) {
    if (phase != 2 || p != position || bits(bound) != bits(expected_bound) ||
        count != secondary_pointer || *count != 2 || result == &output ||
        result == first_pointer || !same(result, &original)) error = 3;
    *result = second_value; phase = 3;
    if (mutation == 3) first_pointer->height = -99;
    return second_return;
}
''' + body.group(0) + r'''
static void fill(HeightResult71820 *result, u8 seed) {
    s32 i;
    for (i = 0; i < 36; i++) ((u8 *)result)[i] = seed + i * 7;
}
static void initialize(void) {
    fill(&output, 0xA5); original = output;
    fill(&first_value, 0x21); first_value.height = 12;
    fill(&second_value, 0x52); second_value.height = 15;
    position[0] = 1; position[1] = 10; position[2] = 2;
    threshold = expected_bound = 20;
    phase = error = mutation = 0; first_return = second_return = 1;
    expected_selector = 0xFFFF;
}
static f32 nan_value(void) {
    union { f32 value; u32 bits; } number;
    number.bits = 0x7FC00000; return number.value;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_early_rejection_preserves_all_other_bytes_and_skips_calls(self):
        self.run_case(r'''
s32 flag;
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = 9; output.flags = flag; original = output;
    original.flags &= ~2;
    CHECK(func_150461D0(position, expected_selector, threshold, &output) == 0);
    CHECK(phase == 0 && same(&output, &original));
}
''')

    def test_both_success_and_failure_choose_lower_with_second_on_ties(self):
        self.run_case(r'''
s32 accepted, ordering; HeightResult71820 expected;
for (accepted = 0; accepted < 2; accepted++) for (ordering = 0; ordering < 3; ordering++) {
    initialize(); first_return = second_return = accepted;
    first_value.height = ordering == 0 ? 12 : ordering == 1 ? 15 : 18;
    expected = ordering == 0 ? first_value : second_value;
    if (!accepted) expected.flags &= ~2;
    CHECK(func_150461D0(position, expected_selector, threshold, &output) == accepted);
    CHECK(phase == 3 && error == 0 && same(&output, &expected));
}
''')

    def test_single_success_overrides_height_order(self):
        self.run_case(r'''
s32 first; HeightResult71820 expected;
for (first = 0; first < 2; first++) {
    initialize(); first_return = first; second_return = !first;
    first_value.height = first ? 99 : -99;
    expected = first ? first_value : second_value;
    CHECK(func_150461D0(position, expected_selector, threshold, &output) == 1);
    CHECK(phase == 3 && error == 0 && same(&output, &expected));
}
''')

    def test_both_returns_are_truncated_to_low_byte(self):
        self.run_case(r'''
s32 i, j, a, b; HeightResult71820 expected;
s32 returns[] = {0, 1, 255, 256, 257, -1, -256, -255, 0x12340000, 0x12340001};
for (i = 0; i < 10; i++) for (j = 0; j < 10; j++) {
    initialize(); first_return = returns[i]; second_return = returns[j];
    a = (u8)first_return != 0; b = (u8)second_return != 0;
    expected = a || !b ? first_value : second_value;
    if (!a && !b) expected.flags &= ~2;
    CHECK(func_150461D0(position, expected_selector, threshold, &output) == (a || b));
    CHECK(phase == 3 && error == 0 && same(&output, &expected));
}
''')

    def test_unordered_heights_select_second_for_both_or_neither(self):
        self.run_case(r'''
s32 accepted, which; HeightResult71820 expected;
for (accepted = 0; accepted < 2; accepted++) for (which = 0; which < 3; which++) {
    initialize(); first_return = second_return = accepted;
    if (which != 1) first_value.height = nan_value();
    if (which != 0) second_value.height = nan_value();
    expected = second_value; if (!accepted) expected.flags &= ~2;
    CHECK(func_150461D0(position, expected_selector, threshold, &output) == accepted);
    CHECK(error == 0 && same(&output, &expected));
}
''')

    def test_equal_and_unordered_gate_proceed(self):
        self.run_case(r'''
s32 mode;
for (mode = 0; mode < 3; mode++) {
    initialize(); threshold = expected_bound = mode == 2 ? nan_value() : 10;
    if (mode == 1) position[1] = nan_value();
    CHECK(func_150461D0(position, expected_selector, threshold, &output) == 1);
    CHECK(phase == 3 && error == 0 && same(&output, &first_value));
}
''')

    def test_snapshots_precede_helper_mutations_and_bound_is_by_value(self):
        self.run_case(r'''
s32 mode;
for (mode = 1; mode <= 2; mode++) {
    initialize(); mutation = mode;
    CHECK(func_150461D0(position, expected_selector, threshold, &output) == 1);
    CHECK(phase == 3 && error == 0 && same(&output, &first_value));
}
''')

    def test_late_mutation_of_first_snapshot_is_observed(self):
        self.run_case(r'''
initialize(); mutation = 3; first_value.height = 99;
CHECK(func_150461D0(position, expected_selector, threshold, &output) == 1);
first_value.height = -99;
CHECK(phase == 3 && error == 0 && same(&output, &first_value));
''')

    def test_failed_fallback_clears_only_bit2_for_every_flag(self):
        self.run_case(r'''
s32 flag, choice; HeightResult71820 expected;
for (choice = 0; choice < 2; choice++) for (flag = 0; flag < 256; flag++) {
    initialize(); first_return = second_return = 0;
    first_value.flags = second_value.flags = flag;
    first_value.height = choice ? 99 : -99;
    expected = choice ? second_value : first_value; expected.flags &= ~2;
    CHECK(func_150461D0(position, expected_selector, threshold, &output) == 0);
    CHECK(error == 0 && same(&output, &expected));
}
''')

    def test_selector_range_and_signed_zero(self):
        self.run_case(r'''
s32 selector;
for (selector = 0; selector <= 65535; selector++) {
    initialize(); expected_selector = selector;
    position[1] = 0; threshold = expected_bound = -0.0f;
    CHECK(func_150461D0(position, (u16)selector, threshold, &output) == 1);
    CHECK(phase == 3 && error == 0 && same(&output, &first_value));
}
''')
