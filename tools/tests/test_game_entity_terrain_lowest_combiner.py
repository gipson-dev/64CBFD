import re
from pathlib import Path

from tools.tests import test_game_lowest_height_combiner as lowest


class GameEntityTerrainLowestCombinerTests(lowest.GameLowestHeightCombinerTests):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        body = re.search(r"s32 func_150466F8\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("entity/terrain lowest combiner definition is missing")
        # Keep the shared result fixture, but use the actual two-call interface/body.
        prefix = cls.source[:cls.source.index("void func_15045714(")]
        suffix = cls.source[cls.source.index("static void fill("):]
        cls.source = prefix + r'''
s32 func_150461D0(f32 *p, u16 selector, f32 bound, HeightResult71820 *result) {
    if (phase != 0 || p != position || selector != expected_selector ||
        bits(bound) != bits(expected_bound) || result == &output ||
        !same(result, &original)) error = 1;
    first_pointer = result;
    if (mutation == 1) {
        output.height = -999; output.flags = 0;
        position[1] = 999; threshold = -999;
    }
    *result = first_value; phase = 2;
    if (mutation == 2) output = first_value;
    return first_return;
}
s32 func_15044ED0(f32 *p, f32 bound, HeightResult71820 *result) {
    if (phase != 2 || p != position || bits(bound) != bits(expected_bound) ||
        result == &output || result == first_pointer || !same(result, &original)) error = 2;
    *result = second_value; phase = 3;
    if (mutation == 3) first_pointer->height = -99;
    return second_return;
}
''' + body.group(0) + suffix

    def run_case(self, body):
        super().run_case(body.replace("func_150461D0(", "func_150466F8("))

    def test_successful_selection_preserves_every_flag_value(self):
        self.run_case(r'''
s32 flag, choice; HeightResult71820 expected;
for (choice = 0; choice < 2; choice++) for (flag = 0; flag < 256; flag++) {
    initialize(); first_value.flags = second_value.flags = flag;
    first_value.height = choice ? 99 : -99;
    expected = choice ? second_value : first_value;
    CHECK(func_150466F8(position, expected_selector, threshold, &output) == 1);
    CHECK(phase == 3 && error == 0 && same(&output, &expected));
}
''')

    def test_infinite_heights_and_signed_zero_ties(self):
        self.run_case(r'''
s32 mode, accepted; HeightResult71820 expected;
union { f32 value; u32 bits; } infinity;
infinity.bits = 0x7F800000;
for (accepted = 0; accepted < 2; accepted++) for (mode = 0; mode < 4; mode++) {
    initialize(); first_return = second_return = accepted;
    if (mode == 0) { first_value.height = -infinity.value; second_value.height = infinity.value; }
    if (mode == 1) { first_value.height = infinity.value; second_value.height = -infinity.value; }
    if (mode == 2) { first_value.height = -0.0f; second_value.height = 0.0f; }
    if (mode == 3) { first_value.height = 0.0f; second_value.height = -0.0f; }
    expected = mode == 0 ? first_value : second_value;
    if (!accepted) expected.flags &= ~2;
    CHECK(func_150466F8(position, expected_selector, threshold, &output) == accepted);
    CHECK(phase == 3 && error == 0 && same(&output, &expected));
}
''')
