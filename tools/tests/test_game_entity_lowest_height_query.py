import re
import struct
import unittest
from pathlib import Path

from tools.tests import test_game_entity_height_query as entity


class GameEntityLowestHeightQueryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        entity.GameEntityHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        body = re.search(r"s32 func_15045880\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("entity lowest-height query definition is missing")
        cls.source = re.sub(r"s32 func_15045F8C\([^;{]*\{\n.*?\n\}",
                            lambda _: body.group(0), cls.source, flags=re.S)
        cls.source = cls.source.replace("D_80098D5C", "D_80098D50").replace(
            "D_800D3830", "D_800D37E0").replace("-10000.0f", "99999.8984375f").replace(
            "-10000", "99999.8984375f")
        cls.source = cls.source.replace("active_result->height = 6;", "active_result->height = 0.5f;")
        cls.source = cls.source.replace("entities[4]", "entities[8]").replace(
            "HeightEntity71820 *D_800DBEF4 = entities;", r'''
static union {
    HeightResult71820 result;
    struct { u8 pad[0x20]; HeightEntity71820 *base; } fields;
} base_alias;
#define D_800DBEF4 base_alias.fields.base
''')
        cls.source = cls.source.replace("static void initialize(void)",
                                        "static void initialize_entities(void)") + r'''
static void initialize(void) {
    initialize_entities(); query_position[1] = 0; threshold = 10;
}
'''

    run_case = entity.GameEntityHeightQueryTests.run_case

    def test_layout_default_metadata_and_exact_sentinel_bits(self):
        self.run_case(r'''
union { f32 value; u32 bits; } sentinel;
sentinel.value = D_80098D50;
CHECK(sentinel.bits == 0x47C34FF3 && sizeof(HeightEntity71820) == 160);
initialize();
CHECK(func_15045880(query_position, threshold, input, &output) == 1 && !error);
CHECK(output.height == 1 && copied(0, 1) && output.metadata == entities[0].metadata);
CHECK(output.value == (s32)&entities[0] && output.state == 2);
CHECK(query_x == -12 && query_z == 23 && input[1] == 0x76543210);
''')

    def test_retail_sentinel(self):
        rom = Path(__file__).resolve().parents[2] / "conker/conker.us.bin"
        if not rom.exists():
            self.skipTest("retail ROM is unavailable")
        self.assertEqual(struct.unpack_from(">I", rom.read_bytes(), 0x23D810)[0], 0x47C34FF3)

    def test_lowest_eligible_first_tie_and_inclusive_bounds(self):
        self.run_case(r'''
initialize(); D_800D3300[0].fixedHeight = D_800D3300[1].fixedHeight = 3 * 256;
D_800D3300[2].fixedHeight = 4 * 256;
CHECK(func_15045880(query_position, threshold, input, &output) == 1 && copied(0, 1));
initialize(); query_position[1] = threshold = 3;
CHECK(func_15045880(query_position, threshold, input, &output) == 1 && copied(2, 1));
''')

    def test_no_early_threshold_gate_and_selected_failure_still_publishes(self):
        self.run_case(r'''
s32 flag;
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = -1; output.flags = flag;
    CHECK(func_15045880(query_position, threshold, input, &output) == 0 && phase == 2 && !error);
    CHECK(output.height == 1 && copied(0, 1) && output.flags == (flag | 6));
    CHECK(output.value == (s32)&entities[0] && output.state == 2);
}
''')

    def test_nonpositive_counts_only_change_height_and_clear_bit2(self):
        self.run_case(r'''
s32 count, flag, byte; u8 before[36];
for (count = -3; count <= 0; count++) for (flag = 0; flag < 256; flag++) {
    initialize(); candidate_count = count; output.flags = flag;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
    CHECK(func_15045880(query_position, threshold, input, &output) == 0 && phase == 2 && !error);
    CHECK(output.height == D_80098D50 && output.flags == (flag & ~2));
    for (byte = 4; byte < 36; byte++) if (byte != 0x1C)
        CHECK(before[byte] == ((u8 *)&output)[byte]);
}
''')

    def test_strict_sentinel_and_no_eligible_candidates(self):
        self.run_case(r'''
s32 i;
initialize();
for (i = 0; i < 4; i++) D_800D3300[i].fixedHeight = (s32)(D_80098D50 * 256) + i * 256;
CHECK(func_15045880(query_position, threshold, input, &output) == 0 && output.height == D_80098D50);
initialize(); query_position[1] = 5;
CHECK(func_15045880(query_position, threshold, input, &output) == 0 && output.height == D_80098D50);
''')

    def test_entity_flag_bit7_and_all_result_flag_combinations(self):
        self.run_case(r'''
s32 flag, entity_flag;
for (flag = 0; flag < 256; flag++) for (entity_flag = 0; entity_flag < 256; entity_flag++) {
    initialize(); output.flags = flag; entities[0].flags = entity_flag;
    CHECK(func_15045880(query_position, threshold, input, &output) == 1);
    CHECK(output.flags == (flag | 6 | ((entity_flag & 0x80) ? 1 : 0)));
}
''')

    def test_metadata_table_relative_triangle_and_unsigned_base(self):
        self.run_case(r'''
static u32 wide_metadata[32772];
initialize(); query_position[1] = 4; entities[3].metadataTable = metadata; entities[3].firstTriangle = 2;
CHECK(func_15045880(query_position, threshold, input, &output) == 1 && output.metadata == metadata[1]);
initialize(); candidate_count = 1; entities[0].metadataTable = &metadata[3];
entities[0].firstTriangle = 1; D_800DBE3C = &triangles[1];
CHECK(func_15045880(query_position, threshold, input, &output) == 1 && output.metadata == metadata[1]);
initialize(); candidate_count = 1; wide_metadata[1] = metadata[1];
entities[0].metadataTable = &wide_metadata[32769]; entities[0].firstTriangle = 32768;
CHECK(func_15045880(query_position, threshold, input, &output) == 1 && output.metadata == metadata[1]);
''')

    def test_copy_caches_triangle_but_reloads_entity_index(self):
        self.run_case(r'''
s32 v;
initialize(); candidate_count = 2;
D_800D3300[0].fixedHeight = 9 * 256; D_800D3300[1].fixedHeight = 5 * 256;
entities[0].metadataTable = metadata;
for (v = 0; v < 3; v++) vertices[1][v][1].x = vertices[1][v][1].y = vertices[1][v][1].z = 0;
active_result = (HeightResult71820 *)((u8 *)&D_800D3300[1] - 4);
CHECK(func_15045880(query_position, threshold, input, active_result) == 1 && !error);
CHECK(active_result->height == 5 && active_result->metadata == metadata[1]);
CHECK(active_result->value == (s32)&entities[0]);
CHECK(D_800D3300[1].triangle == 0 && D_800D3300[1].padC == 0);
''')

    def test_reload_input_positions_and_height_after_helpers(self):
        self.run_case(r'''
initialize(); mutation = 1;
CHECK(func_15045880(query_position, threshold, input, &output) == 1 && !error);
CHECK(query_x == 1 && query_z == -2 && input[0] == 77 && input[1] == 0x76543210);
initialize(); mutation = 2;
CHECK(func_15045880(query_position, threshold, input, &output) == 1 && output.height == 2);
initialize(); mutation = 3;
CHECK(func_15045880(query_position, threshold, input, &output) == 0 && output.height == 0.5f);
''')

    def test_entity_address_publication_precedes_metadata_table_load(self):
        self.run_case(r'''
initialize(); candidate_count = 1;
active_result = (HeightResult71820 *)((u8 *)&entities[0] + 0x24);
CHECK(entities[0].metadataTable == 0);
CHECK(func_15045880(query_position, threshold, input, active_result) == 1 && !error);
CHECK(entities[0].metadataTable == (u32 *)&entities[0]);
CHECK(active_result->metadata == 0xA5A5A5A5 && active_result->value == (s32)&entities[0]);
''')

    def test_entity_index_reloaded_after_flag_publication(self):
        self.run_case(r'''
s32 v;
initialize(); candidate_count = 2; D_800D3300[1].padC = 0;
entities[0].flags = 0; entities[6].flags = 0x80;
for (v = 0; v < 3; v++) vertices[1][v][1].x = vertices[1][v][1].y = vertices[1][v][1].z = 0;
active_result = (HeightResult71820 *)&D_800D3300[0];
CHECK(func_15045880(query_position, threshold, input, active_result) == 1 && !error);
CHECK(active_result->value == (s32)&entities[0] && active_result->metadata == entities[0].metadata);
CHECK(active_result->flags == 7 && active_result->state == 2);
''')

    def test_entity_table_base_reloaded_after_result_value_publication(self):
        self.run_case(r'''
s32 byte;
initialize(); candidate_count = 2;
D_800D3300[0].fixedHeight = 9 * 256; D_800D3300[1].fixedHeight = 3 * 256;
active_result = &base_alias.result;
for (byte = 0; byte < 36; byte++) ((u8 *)active_result)[byte] = 0;
D_800DBEF4 = entities;
CHECK(func_15045880(query_position, threshold, input, active_result) == 1 && !error);
CHECK(D_800DBEF4 == &entities[1] && active_result->value == (s32)&entities[1]);
CHECK(active_result->metadata == entities[1].metadata);
CHECK(active_result->flags == 7 && active_result->state == 2);
''')

    def test_signed_fractional_height_and_negative_vertex_byte_offset(self):
        self.run_case(r'''
s32 v;
initialize(); candidate_count = 1; query_position[1] = -2; threshold = 0;
D_800D3300[0].fixedHeight = -385; D_800D3300[0].vertexIndex = -16;
for (v = 0; v < 3; v++) triangles[0].vertices[v] = &vertices[0][v][1];
CHECK(func_15045880(query_position, threshold, input, &output) == 1);
CHECK(output.height == -1.50390625f && copied(0, 0));
''')

    def test_nan_predicates_and_padding_preserved(self):
        self.run_case(r'''
initialize(); query_position[1] = nan_value();
CHECK(func_15045880(query_position, threshold, input, &output) == 0 && phase == 2 && output.height == D_80098D50);
initialize(); threshold = nan_value();
CHECK(func_15045880(query_position, threshold, input, &output) == 0 && copied(0, 1));
CHECK(output.flags == 0xA7 && output.state == 2 && output.value == (s32)&entities[0]);
CHECK((u16)output.pad16 == 0xA5A5 && output.pad1E == 0xA5A5);
''')
