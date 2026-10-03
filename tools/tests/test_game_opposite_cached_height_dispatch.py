import re
import unittest
from pathlib import Path

from tools.tests import test_game_cached_height_dispatch as cached


class GameOppositeCachedHeightDispatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cached.GameCachedHeightDispatchTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        bodies = []
        for name in ["func_150470B0", "func_1504530C", "func_15046C00"]:
            body = re.search(r"s32 " + name + r"\([^;{]*\{\n.*?\n\}", source, re.S)
            if body is None:
                raise AssertionError("opposite-bound height definition is missing: " + name)
            bodies.append(body.group(0))
        cls.source += r'''
static s32 fallback_calls, fallback_kind, fallback_return;
s32 func_15044ED0(f32 *p, f32 bound, HeightResult71820 *result) {
    if (fallback_calls || p != position || bits(bound) != bits(threshold) || result != &output)
        error = 5;
    fallback_calls++; fallback_kind = 3;
    result->metadata = 0x12345678;
    return fallback_return;
}
s32 func_150466F8(f32 *p, u16 selector, f32 bound, HeightResult71820 *result) {
    if (fallback_calls || p != position || bits(bound) != bits(threshold) || result != &output ||
        selector != expected_selector) error = 6;
    if (mutation == 3 && (p[0] != -12.75f || p[2] != 23.75f || result->metadata != 123)) error = 7;
    fallback_calls++; fallback_kind = 4;
    result->metadata = 0x12345678;
    return fallback_return;
}
''' + "\n".join(bodies) + r'''
static void initialize_opposite(void) {
    initialize(); threshold = 10; position[1] = 0;
    fallback_calls = fallback_kind = 0; fallback_return = 1;
}
'''

    run_case = cached.GameCachedHeightDispatchTests.run_case

    def test_disabled_cache_preserves_all_flags_and_result_bytes(self):
        self.run_case(r'''
s32 flag; u8 before[36];
for (flag = 0; flag < 256; flag++) if (!(flag & 4)) {
    initialize_opposite(); output.flags = flag; snapshot(before);
    CHECK(func_150470B0(position, threshold, &output) == 0);
    CHECK(!geometry_calls && !fallback_calls && unchanged(before));
}
''')

    def test_missing_triangle_returns_zero_without_publication(self):
        self.run_case(r'''
s32 flag; u8 before[36];
for (flag = 0; flag < 256; flag++) if (flag & 4) {
    initialize_opposite(); output.flags = flag; geometry_return = 0; snapshot(before);
    CHECK(func_150470B0(position, threshold, &output) == 0);
    CHECK(geometry_calls == 1 && !error && unchanged(before));
}
''')

    def test_acceptance_sets_only_bit2_and_height_for_every_enabled_flag(self):
        self.run_case(r'''
s32 flag; u8 before[36];
for (flag = 0; flag < 256; flag++) if (flag & 4) {
    initialize_opposite(); output.flags = flag; geometry_return = (flag & 8) ? -9 : 17;
    snapshot(before);
    CHECK(func_150470B0(position, threshold, &output) == 2);
    CHECK(geometry_calls == 1 && !error && output.height == 5 && output.flags == (flag | 2));
    CHECK(cache_only_changed_height_and_flags(before));
}
''')

    def test_rejection_and_nan_do_not_clear_existing_success_bit(self):
        self.run_case(r'''
s32 kind; u8 before[36];
for (kind = 0; kind < 5; kind++) {
    initialize_opposite(); output.flags = 6;
    if (kind == 0) threshold = 4;
    if (kind == 1) position[1] = 6;
    if (kind == 2) threshold = from_bits(0x7FC00000);
    if (kind == 3) cached_height = from_bits(0x7FC00000);
    if (kind == 4) position[1] = from_bits(0x7FC00000);
    snapshot(before);
    CHECK(func_150470B0(position, threshold, &output) == 1);
    CHECK(geometry_calls == 1 && !error && unchanged(before));
}
''')

    def test_inclusive_bounds_signed_zero_and_infinities(self):
        self.run_case(r'''
s32 kind;
for (kind = 0; kind < 5; kind++) {
    initialize_opposite();
    if (kind == 0) threshold = cached_height;
    if (kind == 1) position[1] = cached_height;
    if (kind == 2) { threshold = 0; position[1] = 0; cached_height = from_bits(0x80000000); }
    if (kind == 3) { threshold = from_bits(0x7F800000); position[1] = threshold; cached_height = threshold; }
    if (kind == 4) { threshold = from_bits(0xFF800000); position[1] = threshold; cached_height = threshold; }
    CHECK(func_150470B0(position, threshold, &output) == 2);
    CHECK(bits(output.height) == bits(cached_height) && !error);
}
''')

    def test_helper_reloads_y_and_flags_without_rechecking_initial_gate(self):
        self.run_case(r'''
initialize_opposite(); output.flags = 4; mutation = 1;
CHECK(func_150470B0(position, threshold, &output) == 1);
CHECK(output.flags == 0x80 && !error);
initialize_opposite(); output.flags = 4; mutation = 2;
CHECK(func_150470B0(position, threshold, &output) == 2);
CHECK(output.flags == 0x82 && output.height == 5 && !error);
''')

    def test_position_alias_and_bound_passed_by_value(self):
        self.run_case(r'''
f32 *aliased;
initialize_opposite(); aliased = (f32 *)&output;
aliased[0] = 10; aliased[1] = 0; aliased[2] = 2;
position[0] = 10; position[2] = 2;
CHECK(func_150470B0(aliased, output.height, &output) == 2);
CHECK(output.height == 5 && output.flags == 0xA7 && !error);
''')

    def test_both_dispatch_wrappers_map_cached_statuses_without_fallback(self):
        self.run_case(r'''
s32 wrapper, rejection, result;
for (wrapper = 0; wrapper < 2; wrapper++) for (rejection = 0; rejection < 2; rejection++) {
    initialize_opposite(); output.flags = 6;
    if (rejection) position[1] = 6;
    result = wrapper ? func_15046C00(position, expected_selector, threshold, &output) :
                       func_1504530C(position, threshold, &output);
    CHECK(result == !rejection && geometry_calls == 1 && !fallback_calls && !error);
    CHECK(output.flags == 6);
}
''')

    def test_both_missing_cache_paths_forward_raw_integer_fallback_returns(self):
        self.run_case(r'''
s32 wrapper, missing, i, result; s32 values[] = {-9, 0, 1, 17, 0x12345678};
for (wrapper = 0; wrapper < 2; wrapper++) for (missing = 0; missing < 2; missing++)
for (i = 0; i < 5; i++) {
    initialize_opposite(); output.flags = missing ? 4 : 2; geometry_return = 0;
    fallback_return = values[i];
    result = wrapper ? func_15046C00(position, expected_selector, threshold, &output) :
                       func_1504530C(position, threshold, &output);
    CHECK(result == values[i] && geometry_calls == missing && fallback_calls == 1 && !error);
    CHECK(fallback_kind == (wrapper ? 4 : 3) && output.metadata == 0x12345678);
}
''')

    def test_four_argument_fallback_preserves_all_selectors_and_signed_zero(self):
        self.run_case(r'''
s32 selector;
for (selector = 0; selector <= 65535; selector++) {
    initialize_opposite(); output.flags = 2; expected_selector = selector;
    threshold = from_bits(0x80000000);
    CHECK(func_15046C00(position, (u16)selector, threshold, &output) == 1);
    CHECK(!geometry_calls && fallback_calls == 1 && fallback_kind == 4 && !error);
}
''')

    def test_geometry_failure_mutations_are_visible_to_four_argument_fallback(self):
        self.run_case(r'''
initialize_opposite(); geometry_return = 0; mutation = 3;
CHECK(func_15046C00(position, expected_selector, threshold, &output) == 1);
CHECK(geometry_calls == 1 && fallback_calls == 1 && fallback_kind == 4 && !error);
''')
