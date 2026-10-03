import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameEntityHeightWrapperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        layout = re.search(r"typedef struct HeightResult71820 \{\n.*?\n\} HeightResult71820;",
                           source, re.S)
        body = re.search(r"s32 func_15045780\([^;{]*\{\n.*?\n\}", source, re.S)
        if layout is None or body is None:
            raise AssertionError("entity height wrapper definition/layout is missing")
        cls.source = highest.TYPES + "typedef unsigned short u16;\n" + layout.group(0) + r'''
static f32 position[3], threshold;
static HeightResult71820 output;
static s32 phase, error, mutation, query_return;
static u16 expected_selector;
static s32 *secondary_pointer;
static u32 bits(f32 value) {
    union { f32 value; u32 bits; } number;
    number.value = value; return number.bits;
}
void func_15045714(f32 *p, u16 selector, s32 *primary, s32 *secondary) {
    if (phase != 0 || p != position || selector != expected_selector ||
        primary != secondary + 1) error = 1;
    *secondary = 2; *primary = 3; secondary_pointer = secondary; phase = 1;
    if (mutation) {
        position[0] = -12.75f; position[1] = -100; position[2] = 23.75f;
        output.height = 77; output.flags = 0x7F;
    }
}
s32 func_15045F8C(f32 *p, f32 bound, s32 *counts, HeightResult71820 *result) {
    if (phase != 1 || p != position || bits(bound) != bits(threshold) ||
        counts != secondary_pointer || counts[0] != 2 || counts[1] != 3 ||
        result != &output) error = 2;
    if (mutation && (p[1] != -100 || result->height != 77 || result->flags != 0x7F)) error = 3;
    result->metadata = 0x12345678; phase = 2; return query_return;
}
''' + body.group(0) + r'''
static void initialize(void) {
    s32 byte;
    for (byte = 0; byte < 36; byte++) ((u8 *)&output)[byte] = 0xA5;
    position[0] = 1; position[1] = 10; position[2] = 2; threshold = 0;
    phase = error = mutation = 0; query_return = 1; expected_selector = 0xFFFF;
}
static f32 nan_value(void) {
    union { f32 value; u32 bits; } number;
    number.bits = 0x7FC00000; return number.value;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_early_rejection_only_clears_bit2_for_every_flag(self):
        self.run_case(r'''
s32 flag, byte; u8 before[36];
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = 11; output.flags = flag;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
    CHECK(func_15045780(position, expected_selector, threshold, &output) == 0);
    CHECK(phase == 0 && output.flags == (flag & ~2));
    for (byte = 0; byte < 36; byte++) if (byte != 0x1C)
        CHECK(before[byte] == ((u8 *)&output)[byte]);
}
''')

    def test_equal_bound_and_raw_integer_return_forwarding(self):
        self.run_case(r'''
s32 i; s32 returns[] = {-9, 0, 1, 17, 0x12345678};
for (i = 0; i < 5; i++) {
    initialize(); threshold = 10; query_return = returns[i];
    CHECK(func_15045780(position, expected_selector, threshold, &output) == returns[i]);
    CHECK(phase == 2 && error == 0 && output.metadata == 0x12345678);
    CHECK(output.flags == 0xA5 && output.state == 0xA5);
}
''')

    def test_positions_and_result_mutations_visible_without_retesting_gate(self):
        self.run_case(r'''
initialize(); mutation = 1; threshold = 5;
CHECK(func_15045780(position, expected_selector, threshold, &output) == 1);
CHECK(phase == 2 && error == 0 && position[1] < threshold);
CHECK(output.height == 77 && output.flags == 0x7F);
''')

    def test_nan_y_and_bound_do_not_trigger_early_rejection(self):
        self.run_case(r'''
initialize(); position[1] = nan_value();
CHECK(func_15045780(position, expected_selector, threshold, &output) == 1 && phase == 2 && error == 0);
initialize(); threshold = nan_value();
CHECK(func_15045780(position, expected_selector, threshold, &output) == 1 && phase == 2 && error == 0);
''')

    def test_selector_halfword_range_and_signed_zero_bound(self):
        self.run_case(r'''
s32 selector;
for (selector = 0; selector <= 65535; selector++) {
    initialize(); expected_selector = selector; position[1] = 0; threshold = -0.0f;
    CHECK(func_15045780(position, (u16)selector, threshold, &output) == 1);
    CHECK(phase == 2 && error == 0);
}
''')
