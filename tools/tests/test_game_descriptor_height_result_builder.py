import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameDescriptorHeightResultBuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        layouts = []
        for name in ("HeightResult71820", "HeightCoordinates71820", "HeightDescriptor71820"):
            match = re.search(r"typedef struct " + name + r" \{\n.*?\n\} " + name + ";",
                              source, re.S)
            if match is None:
                raise AssertionError("missing descriptor/result layout: " + name)
            layouts.append(match.group(0))
        body = re.search(r"void func_150472C0\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("descriptor/result builder definition is missing")
        cls.source = highest.TYPES + "typedef unsigned short u16;\n" + \
            "\n".join(layouts) + body.group(0) + r'''
static HeightDescriptor71820 descriptor, saved_descriptor;
static HeightResult71820 output, before;
static void initialize(void) {
    s32 i;
    for (i = 0; i < sizeof(descriptor); i++) ((u8 *)&descriptor)[i] = i * 17 + 3;
    for (i = 0; i < sizeof(output); i++) ((u8 *)&output)[i] = 0xA5;
    descriptor.height = -12.75f; descriptor.metadata = 0x12345678;
    descriptor.value = -1234567; descriptor.state = 1;
    saved_descriptor = descriptor; before = output;
}
static s32 same_bytes(const void *a, const void *b, s32 count) {
    s32 i;
    for (i = 0; i < count; i++) if (((const u8 *)a)[i] != ((const u8 *)b)[i]) return 0;
    return 1;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_layout_offsets_and_coordinate_alignment(self):
        self.run_case(r'''
CHECK(sizeof(HeightCoordinates71820) == 18 && __alignof__(HeightCoordinates71820) == 2);
CHECK(sizeof(HeightDescriptor71820) == 0x64 && sizeof(HeightResult71820) == 36);
CHECK(__builtin_offsetof(HeightDescriptor71820, height) == 0xC);
CHECK(__builtin_offsetof(HeightDescriptor71820, vertices) == 0x44);
CHECK(__builtin_offsetof(HeightDescriptor71820, state) == 0x59);
CHECK(__builtin_offsetof(HeightDescriptor71820, value) == 0x5C);
CHECK(__builtin_offsetof(HeightDescriptor71820, metadata) == 0x60);
''')

    def test_all_state_values_and_complete_output_record(self):
        self.run_case(r'''
s32 state; HeightResult71820 expected;
for (state = 0; state < 256; state++) {
    initialize(); descriptor.state = state; saved_descriptor = descriptor;
    expected = before; expected.height = descriptor.height;
    *(HeightCoordinates71820 *)expected.vertices = descriptor.vertices;
    expected.metadata = descriptor.metadata; expected.value = descriptor.value;
    expected.flags = state == 1 ? 7 : 0; expected.state = state == 1;
    func_150472C0(&output, &descriptor);
    CHECK(same_bytes(&output, &expected, 36));
    CHECK(same_bytes(&descriptor, &saved_descriptor, sizeof(descriptor)));
}
''')

    def test_height_bits_including_nan_infinity_and_signed_zero(self):
        self.run_case(r'''
s32 i; u32 patterns[] = {0, 0x80000000, 0x7F800000, 0xFF800000, 0x7FC12345, 0xFFC54321};
union { f32 value; u32 bits; } number;
for (i = 0; i < 6; i++) {
    initialize(); number.bits = patterns[i]; descriptor.height = number.value;
    func_150472C0(&output, &descriptor); number.value = output.height;
    CHECK(number.bits == patterns[i]);
}
''')

    def test_full_halfword_vertex_values_and_padding_preservation(self):
        self.run_case(r'''
s32 value, i;
for (value = -32768; value <= 32767; value++) {
    initialize();
    for (i = 0; i < 9; i++) descriptor.vertices.values[i] = value + i;
    func_150472C0(&output, &descriptor);
    for (i = 0; i < 9; i++) CHECK(output.vertices[i] == descriptor.vertices.values[i]);
    CHECK(output.pad16 == before.pad16 && output.pad1E == before.pad1E);
}
''')

    def test_metadata_value_and_surrounding_bytes(self):
        self.run_case(r'''
s32 i; union { u32 alignment; u8 bytes[44]; } storage;
HeightResult71820 *result = (HeightResult71820 *)(storage.bytes + 4);
initialize(); descriptor.metadata = 0xFEDCBA98; descriptor.value = (s32)0x80000000;
for (i = 0; i < 44; i++) storage.bytes[i] = 0xA5;
func_150472C0(result, &descriptor);
CHECK(result->metadata == 0xFEDCBA98 && result->value == (s32)0x80000000);
for (i = 0; i < 4; i++) CHECK(storage.bytes[i] == 0xA5 && storage.bytes[40 + i] == 0xA5);
CHECK(result->pad16 == before.pad16 && result->pad1E == before.pad1E);
''')

    def test_state_is_read_after_aliased_metadata_publication(self):
        self.run_case(r'''
s32 state; HeightResult71820 *result = (HeightResult71820 *)((u8 *)&descriptor + 0x40);
for (state = 0; state < 256; state++) {
    initialize(); ((u8 *)&descriptor.metadata)[1] = state;
    func_150472C0(result, &descriptor);
    CHECK(result->flags == (state == 1 ? 7 : 0));
    CHECK(result->state == (state == 1));
}
''')

    def test_value_is_loaded_after_aliased_flag_and_state_stores(self):
        self.run_case(r'''
s32 state; HeightResult71820 *result = (HeightResult71820 *)((u8 *)&descriptor + 0x40);
for (state = 0; state < 2; state++) {
    initialize(); ((u8 *)&descriptor.metadata)[1] = state;
    func_150472C0(result, &descriptor);
    CHECK(result->value == descriptor.value);
    CHECK(((u8 *)&result->value)[0] == (state ? 7 : 0));
    CHECK(((u8 *)&result->value)[1] == state);
}
''')

    def test_source_retains_separate_state_read_after_flag_publication(self):
        body = self.source[self.source.index("void func_150472C0("):]
        flag_store = body.index("result->flags =")
        state_store = body.index("result->state =")
        value_store = body.index("result->value =")
        self.assertLess(flag_store, state_store)
        self.assertLess(state_store, value_store)
        self.assertIn("descriptor->state", body[state_store:value_store])
