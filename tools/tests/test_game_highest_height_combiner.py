import re
import unittest
from pathlib import Path

from tools.tests import test_game_lowest_height_combiner as lowest


class GameHighestHeightCombinerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lowest.GameLowestHeightCombinerTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        body = re.search(r"s32 func_15046460\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("highest-height combiner definition is missing")
        cls.source = re.sub(r"s32 func_150461D0\([^;{]*\{\n.*?\n\}",
                            lambda _: body.group(0), cls.source, count=1, flags=re.S)
        cls.source = cls.source.replace("func_15045880", "func_15045AE4")
        cls.source = cls.source.replace("func_15045D48", "func_15045F8C")
        cls.source = cls.source.replace("first_value.height = 12;", "first_value.height = 18;")
        cls.source = cls.source.replace("threshold = expected_bound = 20;",
                                        "threshold = expected_bound = 0;")
        cls.source = cls.source.replace("position[1] = 999; threshold = -999;",
                                        "position[1] = -999; threshold = 999;")
        cls.source = cls.source.replace("first_pointer->height = -99;",
                                        "first_pointer->height = 99;")

    run_case = lowest.GameLowestHeightCombinerTests.run_case

    def test_early_rejection_resets_state_value_and_only_flag_bit2(self):
        self.run_case(r'''
s32 flag;
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = 11; output.flags = flag; original = output;
    original.flags &= ~2; original.state = 0; original.value = 0;
    CHECK(func_15046460(position, expected_selector, threshold, &output) == 0);
    CHECK(phase == 0 && same(&output, &original));
}
''')

    def test_both_success_and_failure_choose_higher_with_second_on_ties(self):
        self.run_case(r'''
s32 accepted, ordering; HeightResult71820 expected;
for (accepted = 0; accepted < 2; accepted++) for (ordering = 0; ordering < 3; ordering++) {
    initialize(); first_return = second_return = accepted;
    first_value.height = ordering == 0 ? 18 : ordering == 1 ? 15 : 12;
    expected = ordering == 0 ? first_value : second_value;
    if (!accepted) expected.flags &= ~2;
    CHECK(func_15046460(position, expected_selector, threshold, &output) == accepted);
    CHECK(phase == 3 && error == 0 && same(&output, &expected));
}
''')

    def test_single_success_overrides_height_order(self):
        self.run_case(r'''
s32 first; HeightResult71820 expected;
for (first = 0; first < 2; first++) {
    initialize(); first_return = first; second_return = !first;
    first_value.height = first ? -99 : 99;
    expected = first ? first_value : second_value;
    CHECK(func_15046460(position, expected_selector, threshold, &output) == 1);
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
    CHECK(func_15046460(position, expected_selector, threshold, &output) == (a || b));
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
    CHECK(func_15046460(position, expected_selector, threshold, &output) == accepted);
    CHECK(error == 0 && same(&output, &expected));
}
''')

    def test_equal_and_unordered_gate_proceed(self):
        self.run_case(r'''
s32 mode;
for (mode = 0; mode < 3; mode++) {
    initialize(); threshold = expected_bound = mode == 2 ? nan_value() : 10;
    if (mode == 1) position[1] = nan_value();
    CHECK(func_15046460(position, expected_selector, threshold, &output) == 1);
    CHECK(phase == 3 && error == 0 && same(&output, &first_value));
}
''')

    def test_snapshots_precede_helper_mutations_and_bound_is_by_value(self):
        self.run_case(r'''
s32 mode;
for (mode = 1; mode <= 2; mode++) {
    initialize(); mutation = mode;
    CHECK(func_15046460(position, expected_selector, threshold, &output) == 1);
    CHECK(phase == 3 && error == 0 && same(&output, &first_value));
}
''')

    def test_late_mutation_of_first_snapshot_is_observed(self):
        self.run_case(r'''
initialize(); mutation = 3; first_value.height = -99;
CHECK(func_15046460(position, expected_selector, threshold, &output) == 1);
first_value.height = 99;
CHECK(phase == 3 && error == 0 && same(&output, &first_value));
''')

    def test_failed_fallback_retains_selected_state_value_and_padding(self):
        self.run_case(r'''
s32 flag, choice; HeightResult71820 expected;
for (choice = 0; choice < 2; choice++) for (flag = 0; flag < 256; flag++) {
    initialize(); first_return = second_return = 0;
    first_value.flags = second_value.flags = flag;
    first_value.height = choice ? -99 : 99;
    expected = choice ? second_value : first_value; expected.flags &= ~2;
    CHECK(func_15046460(position, expected_selector, threshold, &output) == 0);
    CHECK(error == 0 && same(&output, &expected));
    CHECK(output.state != 0 && output.value != 0);
}
''')

    def test_selector_range_and_signed_zero(self):
        self.run_case(r'''
s32 selector;
for (selector = 0; selector <= 65535; selector++) {
    initialize(); expected_selector = selector;
    position[1] = 0; threshold = expected_bound = -0.0f;
    CHECK(func_15046460(position, (u16)selector, threshold, &output) == 1);
    CHECK(phase == 3 && error == 0 && same(&output, &first_value));
}
''')
