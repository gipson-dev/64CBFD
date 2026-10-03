import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameActorContextDispatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        layout = re.search(r"typedef struct ContextActor71820 \{\n.*?\n\} "
                           r"ContextActor71820;", source, re.S)
        body = re.search(r"s32 func_15044380\([^;{]*\{\n.*?\n\}", source, re.S)
        if layout is None or body is None:
            raise AssertionError("actor/context dispatcher or actor layout missing")
        cls.source = highest.TYPES + layout.group(0) + r'''
f32 D_800CBDF4, D_800CBDF8;
u8 D_800CBDD3, D_80089120[4], D_800DBE62;
static ContextActor71820 actor;
static u8 original_actor[sizeof(actor)], eligibility[4];
static s32 values[4], event_type[32], event_context[32], event_mode[32];
static s32 event_count, current, error, mutation, expected_mode;
static f32 parameters[3];
static void record(s32 type, s32 context, s32 mode) {
    event_type[event_count] = type; event_context[event_count] = context;
    event_mode[event_count++] = mode;
}
void func_15044660(void *input, f32 x, f32 y, f32 z) {
    if (input != &actor || actor.state != 0 || D_800CBDF4 != -32768 ||
        D_800CBDF8 != -32768 || x != 1.25f || y != -7.5f || z != 3.75f)
        error = 1;
    record(0, -1, 0);
    if (mutation == 1) D_800CBDD3 = 0xE7;
    if (mutation == 3) actor.flags = 0;
    if (mutation == 4) {
        parameters[0] = parameters[1] = parameters[2] = 999;
        D_800CBDF4 = 123; D_800CBDF8 = 456;
    }
}
void func_1510F800(s32 context) {
    record(1, context, 0); current = context;
    D_800CBDD3 = context; D_800DBE62 = eligibility[context];
}
s32 func_150AB1F0(f32 x, f32 y, f32 z, void *input, s32 mode) {
    if (input != &actor || x != 1.25f || y != -7.5f || z != 3.75f ||
        mode != expected_mode || D_800DBE62 == 0) error = 2;
    record(2, current, mode);
    if (mutation == 2 && current == 2) {
        D_80089120[1] = 1; D_80089120[0] = 2;
        D_800CBDD3 = 0xFA;
    }
    if (mutation == 5) actor.flags |= 0x200;
    return values[current];
}
void func_150AC3E4(f32 x, f32 y, f32 z, void *input, s32 mode) {
    if (input != &actor || x != 1.25f || y != -7.5f || z != 3.75f ||
        mode != 0 || D_800DBE62 == 0) error = 3;
    record(3, current, mode);
    D_800CBDD3 = 0xEF;
}
''' + body.group(0) + r'''
static void initialize(void) {
    s32 i;
    for (i = 0; i < sizeof(actor); i++) ((u8 *)&actor)[i] = 0xA5;
    actor.flags = 0;
    for (i = 0; i < sizeof(actor); i++) original_actor[i] = ((u8 *)&actor)[i];
    for (i = 0; i < 4; i++) {
        D_80089120[i] = eligibility[i] = 1; values[i] = 10 + i;
    }
    parameters[0] = 1.25f; parameters[1] = -7.5f; parameters[2] = 3.75f;
    D_800CBDF4 = D_800CBDF8 = 99; D_800CBDD3 = 0xAB;
    D_800DBE62 = 0; current = -1; event_count = error = mutation = 0;
    expected_mode = -123;
}
static s32 dispatch(s32 second) {
    return func_15044380(parameters[0], parameters[1], parameters[2],
                         &actor, expected_mode, second);
}
static s32 count(s32 type) {
    s32 i, result = 0;
    for (i = 0; i < event_count; i++) result += event_type[i] == type;
    return result;
}
static s32 event(s32 index, s32 type, s32 context) {
    return event_type[index] == type && event_context[index] == context;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_descending_pass_order_sum_and_final_reset(self):
        self.run_case(r'''
s32 i; initialize(); CHECK(dispatch(0) == 46 && error == 0);
CHECK(event_count == 10 && event(0, 0, -1));
for (i = 0; i < 4; i++) {
    CHECK(event(1 + i * 2, 1, 3 - i));
    CHECK(event(2 + i * 2, 2, 3 - i));
}
CHECK(event(9, 1, 0) && current == 0 && D_800CBDD3 == 0xAB);
''')

    def test_optional_ascending_pass_excludes_context_three(self):
        self.run_case(r'''
s32 i; initialize(); CHECK(dispatch(1) == 46 && error == 0);
CHECK(event_count == 16 && count(2) == 4 && count(3) == 3);
for (i = 0; i < 3; i++) {
    CHECK(event(9 + i * 2, 1, i) && event(10 + i * 2, 3, i));
    CHECK(event_mode[10 + i * 2] == 0);
}
CHECK(event(15, 1, 0) && D_800CBDD3 == 0xAB);
''')

    def test_negative_second_pass_flag_is_enabled(self):
        self.run_case(r'''
initialize(); CHECK(dispatch(-1) == 46 && count(3) == 3 && error == 0);
''')

    def test_enable_bytes_require_exactly_one(self):
        self.run_case(r'''
initialize(); D_80089120[3] = 2; D_80089120[2] = 255; D_80089120[1] = 0;
CHECK(dispatch(1) == 10 && error == 0);
CHECK(event_count == 6 && count(2) == 1 && count(3) == 1);
CHECK(event(1, 1, 0) && event(2, 2, 0) && event(3, 1, 0) && event(4, 3, 0));
''')

    def test_flag_excludes_only_descending_context_three(self):
        self.run_case(r'''
initialize(); actor.flags = 0x200; CHECK(dispatch(1) == 33 && error == 0);
CHECK(count(2) == 3 && count(3) == 3 && event_count == 14);
CHECK(event(1, 1, 2) && event(2, 2, 2));
''')

    def test_preparation_changes_are_seen_before_exclusion(self):
        self.run_case(r'''
initialize(); actor.flags = 0x200; mutation = 3;
CHECK(dispatch(0) == 46 && count(2) == 4 && error == 0);
''')

    def test_eligibility_is_read_after_each_context_switch(self):
        self.run_case(r'''
initialize(); eligibility[3] = 0; eligibility[1] = 0; eligibility[2] = 2;
CHECK(dispatch(1) == 22 && count(2) == 2 && count(3) == 2 && error == 0);
CHECK(count(1) == 8 && D_800CBDD3 == 0xAB);
''')

    def test_no_enabled_contexts_still_prepare_and_reset(self):
        self.run_case(r'''
s32 i; initialize(); for (i = 0; i < 4; i++) D_80089120[i] = 0;
CHECK(dispatch(1) == 0 && error == 0 && event_count == 2);
CHECK(event(0, 0, -1) && event(1, 1, 0) && D_800CBDD3 == 0xAB);
''')

    def test_saved_context_is_captured_after_preparation(self):
        self.run_case(r'''
initialize(); mutation = 1;
CHECK(dispatch(1) == 46 && D_800CBDD3 == 0xE7 && current == 0 && error == 0);
''')

    def test_later_enable_mutations_are_observed(self):
        self.run_case(r'''
initialize(); mutation = 2; D_80089120[1] = 0;
CHECK(dispatch(1) == 36 && error == 0);
CHECK(count(2) == 3 && count(3) == 2 && D_800CBDD3 == 0xAB);
CHECK(event(5, 1, 1) && event(6, 2, 1));
''')

    def test_late_exclusion_flag_does_not_skip_lower_contexts(self):
        self.run_case(r'''
initialize(); mutation = 5;
CHECK(dispatch(1) == 46 && count(2) == 4 && count(3) == 3 && error == 0);
''')

    def test_by_value_arguments_and_no_post_preparation_sentinel_reset(self):
        self.run_case(r'''
initialize(); mutation = 4;
CHECK(dispatch(1) == 46 && error == 0 && parameters[0] == 999);
CHECK(D_800CBDF4 == 123 && D_800CBDF8 == 456);
''')

    def test_result_accumulation_retains_low_32_bits(self):
        self.run_case(r'''
initialize(); values[3] = 0x7FFFFFFF; values[2] = 1;
values[1] = -7; values[0] = -1;
CHECK((u32)dispatch(1) == 0x7FFFFFF8u && error == 0);
''')

    def test_actor_layout_and_only_state_byte_cleared(self):
        self.run_case(r'''
s32 i; initialize(); CHECK((u8 *)&actor.flags - (u8 *)&actor == 0xF8);
CHECK((u8 *)&actor.state - (u8 *)&actor == 0x275);
CHECK(dispatch(0) == 46 && error == 0);
for (i = 0; i < sizeof(actor); i++)
    CHECK(((u8 *)&actor)[i] == (i == 0x275 ? 0 : original_actor[i]));
''')


if __name__ == "__main__":
    unittest.main()
