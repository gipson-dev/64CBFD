import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameEntityHeightQueryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        entity = re.search(r"typedef struct HeightEntity71820 \{\n.*?\n\} HeightEntity71820;",
                           source, re.S)
        body = re.search(r"s32 func_15045F8C\([^;{]*\{\n.*?\n\}", source, re.S)
        if entity is None or body is None:
            raise AssertionError("entity height query definition/layout is missing")
        prefix = cls.source.split("void func_1510F800", 1)[0].replace(
            "D_80098D44", "D_80098D5C")
        suffix = cls.source[cls.source.index("static void initialize(void)"):].replace(
            "static void initialize(void)", "static void initialize_base(void)")
        cls.source = prefix + entity.group(0) + r'''
static HeightEntity71820 entities[4];
HeightEntity71820 *D_800DBEF4 = entities;
u8 D_800D3830[256];
static s32 input[2];
static HeightResult71820 *active_result;
void func_150A44F0(s32 value, void *scratch, s32 mode) {
    if (phase != 0 || value != input[0] || scratch != D_800D3830 || mode != 0 ||
        active_result->height != -10000) error = 1;
    phase = 1;
    if (mutation == 1) {
        input[0] = 77; query_position[0] = 1.75f; query_position[2] = -2.75f;
    }
}
s32 func_150A43E0(s32 x, s32 z, s32 value, void *scratch) {
    if (phase != 1 || value != input[0] || scratch != D_800D3830) error = 2;
    query_x = x; query_z = z; phase = 2;
    if (mutation == 2) query_position[1] = 2;
    if (mutation == 3) active_result->height = 6;
    return candidate_count;
}
''' + body.group(0) + suffix + r'''
static void initialize(void) {
    s32 t, byte;
    initialize_base(); active_result = &output;
    input[0] = 3; input[1] = 0x76543210;
    for (t = 0; t < 4; t++) {
        for (byte = 0; byte < 160; byte++) ((u8 *)&entities[t])[byte] = 0xA5;
        entities[t].metadata = 0x87650000 + t;
        entities[t].metadataTable = 0;
        entities[t].firstTriangle = 0;
        entities[t].flags = t == 2 ? 0x80 : 0;
        D_800D3300[t].vertexIndex = 16;
        D_800D3300[t].padC = t;
    }
    D_800DBEF4 = entities;
}
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_entity_layout_and_default_metadata(self):
        self.run_case(r'''
CHECK(sizeof(HeightEntity71820) == 0xA0);
CHECK(__builtin_offsetof(HeightEntity71820, metadata) == 0x40);
CHECK(__builtin_offsetof(HeightEntity71820, metadataTable) == 0x44);
CHECK(__builtin_offsetof(HeightEntity71820, firstTriangle) == 0x58);
CHECK(__builtin_offsetof(HeightEntity71820, flags) == 0x6F);
initialize();
CHECK(func_15045F8C(query_position, threshold, input, &output) == 1 && error == 0);
CHECK(output.height == 4 && copied(3, 1) && output.metadata == entities[3].metadata);
CHECK(output.value == (s32)&entities[3] && output.state == 3);
CHECK(query_x == -12 && query_z == 23 && input[1] == 0x76543210);
''')

    def test_highest_eligible_first_tie_and_inclusive_boundaries(self):
        self.run_case(r'''
initialize(); D_800D3300[0].fixedHeight = D_800D3300[1].fixedHeight = 9 * 256;
D_800D3300[2].fixedHeight = 11 * 256;
CHECK(func_15045F8C(query_position, threshold, input, &output) == 1 && copied(0, 1));
initialize(); query_position[1] = threshold = 3;
CHECK(func_15045F8C(query_position, threshold, input, &output) == 1 && copied(2, 1));
''')

    def test_no_early_threshold_rejection_and_selected_failure_still_publishes(self):
        self.run_case(r'''
s32 flag;
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = 11; output.flags = flag;
    CHECK(func_15045F8C(query_position, threshold, input, &output) == 0 && phase == 2 && error == 0);
    CHECK(output.height == 4 && copied(3, 1) && output.flags == (flag | 6));
    CHECK(output.value == (s32)&entities[3] && output.state == 3);
}
''')

    def test_nonpositive_counts_preserve_other_fields_all_flags(self):
        self.run_case(r'''
s32 count, flag, byte; u8 before[36];
for (count = -3; count <= 0; count++) for (flag = 0; flag < 256; flag++) {
    initialize(); candidate_count = count; output.flags = flag;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
    CHECK(func_15045F8C(query_position, threshold, input, &output) == 0 && phase == 2);
    CHECK(output.height == -10000 && output.flags == (flag & ~2));
    for (byte = 4; byte < 36; byte++) if (byte != 0x1C)
        CHECK(before[byte] == ((u8 *)&output)[byte]);
}
''')

    def test_strict_sentinel_and_no_eligible_candidate(self):
        self.run_case(r'''
s32 i;
initialize();
for (i = 0; i < 4; i++) D_800D3300[i].fixedHeight = (i ? -10001 : -10000) * 256;
CHECK(func_15045F8C(query_position, threshold, input, &output) == 0 && output.height == -10000);
initialize(); query_position[1] = 0;
CHECK(func_15045F8C(query_position, threshold, input, &output) == 0 && output.height == -10000);
''')

    def test_entity_flag_bit7_controls_result_bit0_without_clearing_existing_bits(self):
        self.run_case(r'''
s32 flag, entity_flag;
for (flag = 0; flag < 256; flag++) for (entity_flag = 0; entity_flag < 256; entity_flag++) {
    initialize(); output.flags = flag; entities[3].flags = entity_flag;
    CHECK(func_15045F8C(query_position, threshold, input, &output) == 1);
    CHECK(output.flags == (flag | 6 | ((entity_flag & 0x80) ? 1 : 0)));
}
''')

    def test_metadata_table_relative_triangle_and_unsigned_base_index(self):
        self.run_case(r'''
static u32 wide_metadata[32772];
initialize(); entities[3].metadataTable = metadata; entities[3].firstTriangle = 2;
CHECK(func_15045F8C(query_position, threshold, input, &output) == 1);
CHECK(output.metadata == metadata[1]);
initialize(); candidate_count = 1; entities[0].metadataTable = &metadata[3];
entities[0].firstTriangle = 1; D_800DBE3C = &triangles[1];
CHECK(func_15045F8C(query_position, threshold, input, &output) == 1 && output.metadata == metadata[1]);
initialize(); candidate_count = 1; wide_metadata[1] = metadata[1];
entities[0].metadataTable = &wide_metadata[32769];
entities[0].firstTriangle = 32768;
CHECK(func_15045F8C(query_position, threshold, input, &output) == 1 && output.metadata == metadata[1]);
''')

    def test_copy_caches_triangle_but_reloads_entity_index_after_overlapping_stores(self):
        self.run_case(r'''
s32 v;
initialize(); candidate_count = 2; D_800D3300[1].fixedHeight = 5 * 256;
entities[0].metadataTable = metadata;
for (v = 0; v < 3; v++) {
    vertices[1][v][1].x = vertices[1][v][1].y = vertices[1][v][1].z = 0;
}
active_result = (HeightResult71820 *)((u8 *)&D_800D3300[1] - 4);
CHECK(func_15045F8C(query_position, threshold, input, active_result) == 1 && error == 0);
CHECK(active_result->height == 5 && active_result->metadata == metadata[1]);
CHECK(active_result->value == (s32)&entities[0]);
CHECK(D_800D3300[1].triangle == 0 && D_800D3300[1].padC == 0);
''')

    def test_reload_input_positions_and_height_after_helpers(self):
        self.run_case(r'''
initialize(); mutation = 1;
CHECK(func_15045F8C(query_position, threshold, input, &output) == 1 && error == 0);
CHECK(query_x == 1 && query_z == -2 && input[0] == 77 && input[1] == 0x76543210);
initialize(); mutation = 2;
CHECK(func_15045F8C(query_position, threshold, input, &output) == 1 && output.height == 2);
initialize(); mutation = 3;
CHECK(func_15045F8C(query_position, threshold, input, &output) == 0 && output.height == 6);
''')

    def test_entity_address_is_published_before_metadata_table_load(self):
        self.run_case(r'''
initialize(); candidate_count = 1;
active_result = (HeightResult71820 *)((u8 *)&entities[0] + 0x24);
CHECK(entities[0].metadataTable == 0);
CHECK(func_15045F8C(query_position, threshold, input, active_result) == 1 && error == 0);
CHECK(entities[0].metadataTable == (u32 *)&entities[0]);
CHECK(active_result->metadata == 0xA5A5A5A5);
CHECK(active_result->value == (s32)&entities[0]);
''')

    def test_signed_fractional_height_and_negative_byte_offset(self):
        self.run_case(r'''
s32 v;
initialize(); candidate_count = 1; threshold = -3;
D_800D3300[0].fixedHeight = -385; D_800D3300[0].vertexIndex = -16;
for (v = 0; v < 3; v++) triangles[0].vertices[v] = &vertices[0][v][1];
CHECK(func_15045F8C(query_position, threshold, input, &output) == 1);
CHECK(output.height == -1.50390625f && copied(0, 0));
''')

    def test_nan_predicates_and_padding_preserved(self):
        self.run_case(r'''
initialize(); query_position[1] = nan_value();
CHECK(func_15045F8C(query_position, threshold, input, &output) == 0 && phase == 2 && output.height == -10000);
initialize(); threshold = nan_value();
CHECK(func_15045F8C(query_position, threshold, input, &output) == 0 && copied(3, 1));
CHECK(output.flags == 0xA7 && output.state == 3 && output.value == (s32)&entities[3]);
CHECK((u16)output.pad16 == 0xA5A5 && output.pad1E == 0xA5A5);
''')
