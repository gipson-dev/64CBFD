import re
import struct
import unittest

from tools.tests import test_game_actor_dimension_helper as dimensions
from tools.tests.game_animation_timeline_oracle import TimelineOracle, bits, floating


class GameAnimationTimelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dimensions.GameActorDimensionHelperTests.setUpClass.__func__(cls)
        source = (cls.project / "src/game/generated_A9260.c").read_text()
        layouts = [match.group(0) for match in re.finditer(
            r"typedef struct \{\n.*?\n\} (\w+);", source, re.S)
                   if match.group(1) == "AnimationTimelineA9260"]
        body = re.search(r"void func_1507BDB0\([^;{]*\{\n.*?\n\}", source, re.S)
        if len(layouts) != 1 or body is None:
            raise AssertionError("production timeline recovery missing")
        cls.source += "\n#undef actor\n" + layouts[0] + r'''
f32 D_800BE9A4;
s32 D_800BE9E4;
u8 D_800BEA0C, D_800C3E78, context_flags[4], D_800C365E[4];
#define D_800C35EA context_flags[0]
struct127 *D_800D154C;
static AnimationTimelineA9260 timeline;
static s32 event_count, event_kind[3], event_actor[3], event_mode[3], mutation;
static u32 event_frame[3], helper_results[2];
static s32 helper_count;
static void word(void *p, u32 value) { *(u32 *)p = value; }
static void mutate(s32 callback) {
    if (callback && mutation == 1) { timeline.sequence = 2; timeline.frame = 4.5f; timeline.end = 20; }
    if (callback && mutation == 2) { timeline.end = 5; timeline.flags = 0; D_800CC2D0[2].unkF4 = 0; }
    if (!callback && mutation == 3) { timeline.rate = -1; timeline.end = 20; }
    if (!callback && mutation == 4 && helper_count == 2) timeline.frame = 6.25f;
    if (callback && mutation == 5) D_800D154C = &D_800CC2D0[1];
    if (callback && mutation == 6) { timeline.sequence = 0; timeline.frame = 4.5f; }
}
static void timeline_callback(void) {
    event_kind[event_count] = 1; event_actor[event_count] = 0;
    event_frame[event_count] = 0; event_mode[event_count++] = 0;
    mutate(1);
}
f32 func_1506AD30(struct127 *p, f32 frame, s32 mode) {
    u32 result = helper_results[helper_count++];
    event_kind[event_count] = 0; event_actor[event_count] = p - D_800CC2D0;
    event_frame[event_count] = *(u32 *)&frame; event_mode[event_count++] = mode;
    mutate(0);
    return *(f32 *)&result;
}
''' + body.group(0) + r'''
static void setup_timeline(void) {
    u32 i;
    initialize();
    for (i = 0; i < sizeof(timeline); i++) ((u8 *)&timeline)[i] = 0xA5;
    for (i = 0; i < sizeof(struct127); i++) ((u8 *)&D_800CC2D0[2])[i] = 0xA5;
    timeline.callback = 0; timeline.flags = 0; timeline.frame = 2; timeline.rate = 1;
    timeline.end = 10; timeline.start = 1; timeline.sequence = 1;
    timeline.decrement = 1; timeline.timer = 0;
    D_800CC2D0[2].unkF4 = 0; D_800CC2D0[2].unk1FC = 0xA5;
    D_800CC2D0[2].unk1FD = 0; D_800CC2D0[2].unk76 = 0xFF80;
    D_800BE9A4 = 1; D_800BE9E4 = 1; D_800BEA0C = 0;
    D_800D154C = D_800CC2D0; D_800C3E78 = 0xAA;
    for (i = 0; i < 4; i++) { context_flags[i] = 0; D_800C365E[i] = 0; }
    event_count = helper_count = mutation = 0;
    helper_results[0] = helper_results[1] = 0;
}
static s32 equal_word(u32 left, u32 right) {
    return left == right || (((left & 0x7FFFFFFF) > 0x7F800000) &&
                            ((right & 0x7FFFFFFF) > 0x7F800000));
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = dimensions.GameActorDimensionHelperTests.run_case

    @staticmethod
    def native_bytes(model, address, size, fields):
        result = bytearray(model.memory[address + i] for i in range(size))
        for offset, length in fields:
            result[offset:offset + length] = result[offset:offset + length][::-1]
        return result

    def assert_cases(self, cases):
        generated = []
        for case in cases:
            with self.subTest(case=case):
                model = TimelineOracle(case).run()
                state = self.native_bytes(model, model.STATE, 0x40,
                    [(4, 2), *[(i, 4) for i in range(8, 0x2C, 4)], (0x3A, 2), (0x3C, 2)])
                actor = self.native_bytes(model, model.ACTOR, 0x32C,
                    [(0x76, 2), (0x78, 2), (0x7A, 2), (0xB4, 4), (0xF4, 4),
                     (0x10C, 2), (0x1C4, 4), (0x21C, 2)])
                code = ["{", "setup_timeline();"]
                for name, default in (("frame", 2), ("rate", 1), ("end", 10), ("start", 1)):
                    code.append("word(&timeline.%s, 0x%08Xu);" % (name, bits(case.get(name, default))))
                for name, default in (("flags", 0), ("sequence", 1), ("timer", 0), ("decrement", 1)):
                    code.append("timeline.%s = %d;" % (name, case.get(name, default)))
                code += ["timeline.callback = %s;" % ("timeline_callback" if case.get("callback") else "0"),
                         "mutation = %d;" % case.get("mutation", 0),
                         "word(&D_800BE9A4, 0x%08Xu);" % bits(case.get("time", 1)),
                         "D_800BE9E4 = 0x%08Xu;" % (case.get("ticks", 1) & 0xFFFFFFFF),
                         "D_800BEA0C = %d;" % case.get("freeze", 0),
                         "D_800CC2D0[2].unkF4 = 0x%08Xu;" % (case.get("actor_flags", 0) & 0xFFFFFFFF),
                         "D_800CC2D0[2].unk1FC = %d;" % case.get("actor_bits", 0xA5),
                         "D_800CC2D0[2].unk1FD = %d;" % case.get("turn", 0),
                         "D_800CC2D0[2].unk76 = %d;" % case.get("angle", 0xFF80)]
                for i in range(4):
                    code += ["context_flags[%d] = %d;" % (i, case.get("modes", [0] * 4)[i]),
                             "D_800C365E[%d] = %d;" % (i, case.get("enable", [0] * 4)[i])]
                for i, value in enumerate(case.get("results", [0, 0])):
                    code.append("helper_results[%d] = 0x%08Xu;" % (i, bits(value)))
                code.append("func_1507BDB0((struct197 *)&timeline, %s, %s, %d);" % (
                    "*(f32 *)&(u32){0x%08Xu}" % bits(case.get("step", 1)),
                    "&D_800CC2D0[2]" if case.get("actor", True) else "0", case.get("mode", 0)))
                code.append("CHECK(event_count == %d);" % len(model.events))
                for i, (kind, pointer, frame, mode) in enumerate(model.events):
                    code.append("CHECK(event_kind[%d] == %d && event_actor[%d] == %d && "
                                "equal_word(event_frame[%d], 0x%08Xu) && event_mode[%d] == %d);" % (
                                    i, kind, i, (pointer - model.ACTORS) // 0x32C if kind == 0 else 0,
                                    i, frame, i, mode))
                code += ["CHECK(D_800C3E78 == %d);" % model.get(model.SLOT, 1),
                         "CHECK(D_800D154C == &D_800CC2D0[%d]);" % (
                             (model.get(model.CURRENT, 4) - model.ACTORS) // 0x32C),
                         "CHECK(timeline.callback == %s);" % (
                             "timeline_callback" if case.get("callback") else "0")]
                for name, data, pointer, begin, float_offset in (
                    ("state", state, "&timeline", 4, 8),
                    ("record", actor, "&D_800CC2D0[2]", 0, 0xB4)):
                    code.append("{ u8 expected[] = {%s}; u32 i;" % ",".join(str(byte) for byte in data))
                    code.append("CHECK(equal_word(*(u32 *)((u8 *)%s + %d), 0x%08Xu));" % (
                        pointer, float_offset, int.from_bytes(data[float_offset:float_offset + 4], "little")))
                    code.append("for (i = %d; i < sizeof(expected); i++) {" % begin)
                    code.append("if (i < %d || i >= %d) CHECK(((u8 *)%s)[i] == expected[i]);" % (
                        float_offset, float_offset + 4, pointer))
                    code += ["}}", ""]
                code.append("}")
                generated += code
        self.run_case("\n".join(generated) + "\nreturn 0;\n")

    def test_layout_and_original_word_slot(self):
        self.run_case(r'''
CHECK(sizeof(AnimationTimelineA9260) == 0x40);
CHECK(__builtin_offsetof(AnimationTimelineA9260, callback) == 0);
CHECK(__builtin_offsetof(AnimationTimelineA9260, flags) == 4);
CHECK(__builtin_offsetof(AnimationTimelineA9260, frame) == 8);
CHECK(__builtin_offsetof(AnimationTimelineA9260, rate) == 0x10);
CHECK(__builtin_offsetof(AnimationTimelineA9260, end) == 0x18);
CHECK(__builtin_offsetof(AnimationTimelineA9260, start) == 0x20);
CHECK(__builtin_offsetof(AnimationTimelineA9260, sequence) == 0x28);
CHECK(__builtin_offsetof(AnimationTimelineA9260, decrement) == 0x3A);
CHECK(__builtin_offsetof(AnimationTimelineA9260, timer) == 0x3C);
return 0;
''')
        model = TimelineOracle({})
        self.assertEqual(len(model.code), 287)
        original = b"".join(struct.pack(">I", word) for _, word in sorted(model.code.items()))
        retail = (self.project / "conker.us.bin").read_bytes()[0xA9260:0xA96DC]
        self.assertEqual(original, retail)
        self.assertEqual(len(original), 1148)

    def test_inactive_sequence_no_side_effects(self):
        self.assert_cases([{"sequence": 0, "callback": True, "timer": 123},
                           {"sequence": 0, "actor": False, "freeze": 1}])

    def test_time_scaling_cap_override_freeze_and_standalone(self):
        self.assert_cases([{"time": time, "step": 3} for time in (0, 0.5, 1.5, 2, 3, -1)] +
                          [{"time": 0.5, "step": 20}, {"modes": [1, 0, 0, 0], "time": 0.5},
                           {"modes": [2, 0, 0, 0], "time": 3}, {"freeze": 1, "step": 20},
                           {"actor": False, "time": 0.5, "step": 3},
                           {"actor": False, "step": 20},
                           {"freeze": 1, "results": [10, 0]}])

    def test_forward_wrap_and_reverse_wrap_boundaries(self):
        self.assert_cases([{"frame": frame} for frame in (8, 8.5, 9, 10, 20)] +
                          [{"rate": -1, "frame": frame} for frame in (3, 2, 1, 0, -10)] +
                          [{"actor": False, "rate": -1, "frame": 1},
                           {"actor": False, "frame": 9}])

    def test_forward_flag_clamp_reset_and_negative_floor(self):
        self.assert_cases([{"actor_flags": flag, "frame": frame}
                           for flag in (2, 4, 8, 10, 14) for frame in (8, 9, 10)] +
                          [{"flags": 0x8000, "frame": 8},
                           {"actor": False, "flags": 0x8000, "frame": 9},
                           {"flags": 0x8000, "end": 0, "start": -5, "frame": -2},
                           {"flags": 0x8000, "end": 0, "start": -5, "frame": -1}])

    def test_turn_rotation_wrap_and_motion_reset(self):
        self.assert_cases([{"turn": turn, "frame": 8, "actor_flags": flag}
                           for turn in (1, 128, 255) for flag in (0, 4, 8)] +
                          [{"turn": 1, "frame": 7.5, "actor_flags": 4}])

    def test_callback_crossing_suppression_and_sequence_change(self):
        self.assert_cases([{"callback": True, "frame": frame} for frame in (7, 8, 9)] +
                          [{"callback": True, "frame": 8, "mutation": mutation}
                           for mutation in (1, 2, 5, 6)] +
                          [{"callback": True, "frame": 8, "actor_flags": 8},
                           {"callback": True, "frame": 8, "modes": [1, 0, 0, 0]},
                           {"callback": True, "frame": 8, "mutation": 2, "actor_flags": 4},
                           {"callback": True, "frame": 8, "mutation": 2, "flags": 0x8000},
                           {"callback": True, "frame": 8, "step": 2, "mutation": 5},
                           {"callback": True, "frame": 8, "actor": False, "mutation": 1},
                           {"callback": True, "frame": 8, "actor": False}])

    def test_helper_gates_return_values_and_reload_after_second_call(self):
        self.assert_cases([{"modes": [mode, 0, 0, 0], "enable": [enabled, 0, 0, 0]}
                           for mode in (0, 1, 2) for enabled in (0, 1)] +
                          [{"results": [result, 0]} for result in (0, -0.0, 5, 10, -3)] +
                          [{"mode": 1, "modes": [0, 1, 0, 0]},
                           {"mode": 1, "modes": [0, 1, 0, 0], "enable": [0, 1, 0, 0]},
                           {"mutation": 3}, {"frame": 9, "mutation": 4}])

    def test_timer_signed_halfword_and_low_word_wrap(self):
        self.assert_cases([{"timer": timer, "decrement": decrement, "ticks": ticks}
                           for timer, decrement, ticks in ((0, 1, 1), (-1, 1, 1),
                               (1, 1, 1), (1, 2, 3), (32767, -32768, 0x7FFFFFFF),
                               (123, -1, -1), (32767, 32767, 0xFFFFFFFF))])

    def test_signed_zero_nan_and_infinity_classification(self):
        self.assert_cases([{"step": -0.0, "frame": -0.0, "start": -10},
                           {"rate": -0.0, "frame": -0.0, "start": -10},
                           {"rate": float("nan")}, {"time": float("nan")},
                           {"end": float("nan")}, {"frame": float("nan")},
                           {"step": float("inf")}, {"rate": -float("inf")},
                           {"results": [floating(0x7FC12345), 0]}])


if __name__ == "__main__":
    unittest.main()
