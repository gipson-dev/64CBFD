import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameActorHeightResultBuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        layouts = []
        for name in ("HeightResult71820", "HeightCoordinates71820",
                     "HeightActor71820", "HeightEntity71820"):
            match = re.search(r"typedef struct " + name + r" \{\n.*?\n\} " + name + ";",
                              source, re.S)
            if match is None:
                raise AssertionError("missing actor/result layout: " + name)
            layouts.append(match.group(0))
        body = re.search(r"void func_1504715C\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("actor/result builder definition is missing")
        cls.source = highest.TYPES + "typedef unsigned short u16;\n" + \
            "\n".join(layouts) + r'''
static HeightActor71820 actor;
static HeightResult71820 output, before;
static HeightEntity71820 entities[65535];
HeightEntity71820 *D_800DBEF4 = entities;
static HeightResult71820 *active_result;
static s32 calls, error, mutation, helper_return, expected_index;
s32 func_15145C90(s32 index) {
    if (calls || index != expected_index || active_result->state != 2 ||
        active_result->flags != 6 ||
        active_result->value != (s32)&entities[index]) error = 1;
    calls++;
    if (mutation) {
        active_result->flags = mutation - 1;
        actor.entityIndex = 0; D_800DBEF4 = 0;
    }
    return helper_return;
}
''' + body.group(0) + r'''
static void initialize(void) {
    s32 i;
    for (i = 0; i < sizeof(actor); i++) ((u8 *)&actor)[i] = 0;
    for (i = 0; i < sizeof(output); i++) ((u8 *)&output)[i] = 0xA5;
    before = output;
    actor.x = -12.75f; actor.z = 23.75f; actor.height = -5.75f;
    actor.metadata = 0x12345678;
    for (i = 0; i < 9; i++) actor.vertices.values[i] = i * 137 - 1234;
    D_800DBEF4 = entities; active_result = &output;
    calls = error = mutation = helper_return = expected_index = 0;
}
static s32 preserved_padding(void) {
    return output.pad16 == before.pad16 && output.pad1E == before.pad1E;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_layout_offsets_and_coordinate_alignment(self):
        self.run_case(r'''
CHECK(sizeof(HeightCoordinates71820) == 18);
CHECK(__alignof__(HeightCoordinates71820) == 2);
CHECK(sizeof(HeightResult71820) == 36 && sizeof(HeightEntity71820) == 160);
CHECK(__builtin_offsetof(HeightActor71820, x) == 0x14);
CHECK(__builtin_offsetof(HeightActor71820, z) == 0x1C);
CHECK(__builtin_offsetof(HeightActor71820, flags) == 0xF8);
CHECK(__builtin_offsetof(HeightActor71820, height) == 0x180);
CHECK(__builtin_offsetof(HeightActor71820, metadata) == 0x184);
CHECK(__builtin_offsetof(HeightActor71820, vertices) == 0x18C);
CHECK(__builtin_offsetof(HeightActor71820, entityIndex) == 0x1A0);
''')

    def test_stored_vertices_metadata_and_padding(self):
        self.run_case(r'''
s32 i;
initialize(); func_1504715C(&output, &actor);
CHECK(output.height == actor.height && output.metadata == actor.metadata);
for (i = 0; i < 9; i++) CHECK(output.vertices[i] == actor.vertices.values[i]);
CHECK(output.flags == 7 && output.state == 1 && output.value == 0);
CHECK(calls == 0 && preserved_padding());
''')

    def test_synthetic_triangle_uses_truncation_and_exact_vertex_order(self):
        self.run_case(r'''
s32 i; s16 expected[] = {988, -5, 1023, -1012, -5, 23, 988, -5, -977};
initialize(); actor.flags = 0x200000; func_1504715C(&output, &actor);
for (i = 0; i < 9; i++) CHECK(output.vertices[i] == expected[i]);
CHECK(output.height == -5.75f && output.metadata == 0x12345678);
CHECK(output.flags == 7 && output.state == 1 && output.value == 0);
CHECK(calls == 0 && preserved_padding());
''')

    def test_only_bit21_selects_synthetic_vertices(self):
        self.run_case(r'''
s32 bit;
for (bit = 0; bit < 32; bit++) {
    initialize(); actor.flags = (u32)1 << bit; func_1504715C(&output, &actor);
    CHECK(output.vertices[0] == (bit == 21 ? 988 : -1234));
}
initialize(); actor.flags = ~0x200000u; func_1504715C(&output, &actor);
CHECK(output.vertices[0] == -1234);
''')

    def test_coordinate_halfword_wrapping(self):
        self.run_case(r'''
initialize(); actor.flags = 0x200000;
actor.x = 32767.75f; actor.height = -32769.75f; actor.z = -32768.75f;
func_1504715C(&output, &actor);
CHECK(output.vertices[0] == (s16)(32767 + 1000));
CHECK(output.vertices[3] == (s16)(32767 - 1000));
CHECK(output.vertices[1] == (s16)-32769 && output.vertices[4] == (s16)-32769);
CHECK(output.vertices[7] == (s16)-32769);
CHECK(output.vertices[2] == (s16)(-32768 + 1000));
CHECK(output.vertices[5] == (s16)-32768 && output.vertices[8] == (s16)(-32768 - 1000));
''')

    def test_all_entity_indices_publish_pointer_before_helper(self):
        self.run_case(r'''
s32 index;
for (index = 1; index <= 65535; index++) {
    initialize(); actor.entityIndex = index; expected_index = index - 1;
    helper_return = index & 1; func_1504715C(&output, &actor);
    CHECK(calls == 1 && error == 0 && output.state == 2);
    CHECK(output.value == (s32)&entities[index - 1]);
    CHECK(output.flags == (6 | helper_return) && preserved_padding());
}
''')

    def test_helper_truth_uses_raw_integer_not_low_byte(self):
        self.run_case(r'''
s32 i; s32 values[] = {0, 1, 255, 256, 257, -1, -256, 0x12340000};
for (i = 0; i < 8; i++) {
    initialize(); actor.entityIndex = 1; helper_return = values[i];
    func_1504715C(&output, &actor);
    CHECK(calls == 1 && error == 0 && output.flags == (6 | (values[i] != 0)));
}
''')

    def test_flags_are_reloaded_after_helper_mutation(self):
        self.run_case(r'''
s32 flag, accepted;
for (accepted = 0; accepted < 2; accepted++) for (flag = 0; flag < 256; flag++) {
    initialize(); actor.entityIndex = 1; mutation = flag + 1; helper_return = accepted;
    func_1504715C(&output, &actor);
    CHECK(calls == 1 && error == 0 && output.flags == (flag | accepted));
    CHECK(output.state == 2 && output.value == (s32)&entities[0]);
}
''')

    def test_stored_copy_preserves_surrounding_bytes(self):
        self.run_case(r'''
s32 i; union { u32 alignment; u8 bytes[44]; } storage;
HeightResult71820 *result = (HeightResult71820 *)(storage.bytes + 4);
initialize();
for (i = 0; i < 44; i++) storage.bytes[i] = 0xA5;
func_1504715C(result, &actor);
for (i = 0; i < 9; i++) CHECK(result->vertices[i] == actor.vertices.values[i]);
for (i = 0; i < 4; i++) CHECK(storage.bytes[i] == 0xA5 && storage.bytes[40 + i] == 0xA5);
''')

    def test_height_publication_precedes_aliased_flag_read(self):
        self.run_case(r'''
union { f32 value; u32 bits; } height;
HeightResult71820 *result;
initialize(); height.bits = 0x3FA00000; actor.height = height.value;
result = (HeightResult71820 *)((u8 *)&actor + 0xF8);
func_1504715C(result, &actor);
CHECK(result->vertices[0] == 988 && result->vertices[1] == 1);
CHECK(result->vertices[2] == 1023 && result->flags == 7);
''')

    def test_metadata_is_reloaded_after_aliased_vertex_writes(self):
        self.run_case(r'''
u32 expected; HeightResult71820 *result;
initialize(); actor.flags = 0x200000;
result = (HeightResult71820 *)((u8 *)&actor + 0x180);
func_1504715C(result, &actor);
expected = *(u32 *)result->vertices;
CHECK(result->metadata == expected && expected != 0x12345678);
CHECK(result->state == 1 && result->value == 0 && result->flags == 7);
''')

    def test_metadata_is_cached_before_aliased_flag_publication(self):
        self.run_case(r'''
HeightResult71820 *result;
initialize(); actor.flags = 0x200000;
result = (HeightResult71820 *)((u8 *)&actor + 0x168);
func_1504715C(result, &actor);
CHECK(result->metadata == 0x12345678 && result->flags == 7);
CHECK(result->state == 1 && result->value == 0);
''')
