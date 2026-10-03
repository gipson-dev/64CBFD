import re
import struct
import unittest
from pathlib import Path

from tools.tests import test_game_entity_lowest_height_query as lowest


class GameContext2HighestHeightQueryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lowest.GameEntityLowestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        body = re.search(r"s32 func_15045AE4\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("context-2 highest-height definition is missing")
        cls.source = re.sub(r"s32 func_15045880\([^;{]*\{\n.*?\n\}",
                            lambda _: body.group(0), cls.source, flags=re.S)
        cls.source = cls.source.replace("D_80098D50", "D_80098D54").replace(
            "99999.8984375f", "-10000.0f").replace(
            "active_result->height = 0.5f;", "active_result->height = 6;").replace(
            "initialize_entities(); query_position[1] = 0; threshold = 10;",
            "initialize_entities(); query_position[1] = 10; threshold = 0;")

    run_case = lowest.GameEntityLowestHeightQueryTests.run_case

    def test_layout_sentinel_default_metadata_and_state2(self):
        self.run_case(r'''
union { f32 value; u32 bits; } sentinel;
sentinel.value = D_80098D54;
CHECK(sentinel.bits == 0xC61C4000 && sizeof(HeightEntity71820) == 160);
initialize();
CHECK(func_15045AE4(query_position, threshold, input, &output) == 1 && !error);
CHECK(output.height == 4 && copied(3, 1) && output.metadata == entities[3].metadata);
CHECK(output.value == (s32)&entities[3] && output.state == 2);
CHECK(query_x == -12 && query_z == 23 && input[1] == 0x76543210);
''')

    def test_retail_sentinel(self):
        rom = Path(__file__).resolve().parents[2] / "conker/conker.us.bin"
        if not rom.exists():
            self.skipTest("retail ROM is unavailable")
        self.assertEqual(struct.unpack_from(">I", rom.read_bytes(), 0x23D814)[0], 0xC61C4000)

    def test_highest_eligible_first_tie_and_inclusive_boundaries(self):
        self.run_case(r'''
initialize(); D_800D3300[0].fixedHeight = D_800D3300[1].fixedHeight = 9 * 256;
D_800D3300[2].fixedHeight = 11 * 256;
CHECK(func_15045AE4(query_position, threshold, input, &output) == 1 && copied(0, 1));
initialize(); query_position[1] = threshold = 3;
CHECK(func_15045AE4(query_position, threshold, input, &output) == 1 && copied(2, 1));
''')

    def test_selected_failure_still_publishes_without_early_bound_gate(self):
        self.run_case(r'''
s32 flag;
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = 11; output.flags = flag;
    CHECK(func_15045AE4(query_position, threshold, input, &output) == 0 && phase == 2 && !error);
    CHECK(output.height == 4 && copied(3, 1) && output.flags == (flag | 6));
    CHECK(output.value == (s32)&entities[3] && output.state == 2);
}
''')

    def test_nonpositive_counts_only_change_height_and_clear_bit2(self):
        self.run_case(r'''
s32 count, flag, byte; u8 before[36];
for (count = -3; count <= 0; count++) for (flag = 0; flag < 256; flag++) {
    initialize(); candidate_count = count; output.flags = flag;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
    CHECK(func_15045AE4(query_position, threshold, input, &output) == 0 && phase == 2 && !error);
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
CHECK(func_15045AE4(query_position, threshold, input, &output) == 0 && output.height == -10000);
initialize(); query_position[1] = 0;
CHECK(func_15045AE4(query_position, threshold, input, &output) == 0 && output.height == -10000);
''')

    def test_entity_flag_bit7_and_all_result_flag_combinations(self):
        self.run_case(r'''
s32 flag, entity_flag;
for (flag = 0; flag < 256; flag++) for (entity_flag = 0; entity_flag < 256; entity_flag++) {
    initialize(); output.flags = flag; entities[3].flags = entity_flag;
    CHECK(func_15045AE4(query_position, threshold, input, &output) == 1);
    CHECK(output.flags == (flag | 6 | ((entity_flag & 0x80) ? 1 : 0)));
}
''')

    def test_relative_metadata_index_with_unsigned_first_triangle(self):
        self.run_case(r'''
static u32 wide_metadata[32772];
initialize(); entities[3].metadataTable = metadata; entities[3].firstTriangle = 2;
CHECK(func_15045AE4(query_position, threshold, input, &output) == 1 && output.metadata == metadata[1]);
initialize(); candidate_count = 1; entities[0].metadataTable = &metadata[3];
entities[0].firstTriangle = 1; D_800DBE3C = &triangles[1];
CHECK(func_15045AE4(query_position, threshold, input, &output) == 1 && output.metadata == metadata[1]);
initialize(); candidate_count = 1; wide_metadata[1] = metadata[1];
entities[0].metadataTable = &wide_metadata[32769]; entities[0].firstTriangle = 32768;
CHECK(func_15045AE4(query_position, threshold, input, &output) == 1 && output.metadata == metadata[1]);
''')

    def test_cached_triangle_and_entity_index_reload_after_vertex_copies(self):
        self.run_case(r'''
s32 v;
initialize(); candidate_count = 2; D_800D3300[1].fixedHeight = 5 * 256;
entities[0].metadataTable = metadata;
for (v = 0; v < 3; v++) vertices[1][v][1].x = vertices[1][v][1].y = vertices[1][v][1].z = 0;
active_result = (HeightResult71820 *)((u8 *)&D_800D3300[1] - 4);
CHECK(func_15045AE4(query_position, threshold, input, active_result) == 1 && !error);
CHECK(active_result->height == 5 && active_result->metadata == metadata[1]);
CHECK(active_result->value == (s32)&entities[0]);
CHECK(D_800D3300[1].triangle == 0 && D_800D3300[1].padC == 0);
''')

    def test_helper_input_position_and_height_reloads(self):
        self.run_case(r'''
initialize(); mutation = 1;
CHECK(func_15045AE4(query_position, threshold, input, &output) == 1 && !error);
CHECK(query_x == 1 && query_z == -2 && input[0] == 77 && input[1] == 0x76543210);
initialize(); mutation = 2;
CHECK(func_15045AE4(query_position, threshold, input, &output) == 1 && output.height == 2);
initialize(); mutation = 3;
CHECK(func_15045AE4(query_position, threshold, input, &output) == 0 && output.height == 6);
''')

    def test_value_publication_precedes_metadata_table_load(self):
        self.run_case(r'''
initialize(); candidate_count = 1;
active_result = (HeightResult71820 *)((u8 *)&entities[0] + 0x24);
CHECK(entities[0].metadataTable == 0);
CHECK(func_15045AE4(query_position, threshold, input, active_result) == 1 && !error);
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
CHECK(func_15045AE4(query_position, threshold, input, active_result) == 1 && !error);
CHECK(active_result->value == (s32)&entities[0] && active_result->metadata == entities[0].metadata);
CHECK(active_result->flags == 7 && active_result->state == 2);
''')

    def test_entity_base_reloaded_after_value_publication(self):
        self.run_case(r'''
s32 byte;
initialize(); candidate_count = 2; D_800D3300[1].fixedHeight = 3 * 256;
active_result = &base_alias.result;
for (byte = 0; byte < 36; byte++) ((u8 *)active_result)[byte] = 0;
D_800DBEF4 = entities;
CHECK(func_15045AE4(query_position, threshold, input, active_result) == 1 && !error);
CHECK(D_800DBEF4 == &entities[1] && active_result->value == (s32)&entities[1]);
CHECK(active_result->metadata == entities[1].metadata && active_result->flags == 7 && active_result->state == 2);
''')

    def test_negative_fractional_height_and_signed_vertex_byte_offset(self):
        self.run_case(r'''
s32 v;
initialize(); candidate_count = 1; threshold = -3;
D_800D3300[0].fixedHeight = -385; D_800D3300[0].vertexIndex = -16;
for (v = 0; v < 3; v++) triangles[0].vertices[v] = &vertices[0][v][1];
CHECK(func_15045AE4(query_position, threshold, input, &output) == 1);
CHECK(output.height == -1.50390625f && copied(0, 0));
''')

    def test_nan_predicates_and_padding_preservation(self):
        self.run_case(r'''
initialize(); query_position[1] = nan_value();
CHECK(func_15045AE4(query_position, threshold, input, &output) == 0 && phase == 2 && output.height == -10000);
initialize(); threshold = nan_value();
CHECK(func_15045AE4(query_position, threshold, input, &output) == 0 && copied(3, 1));
CHECK(output.flags == 0xA7 && output.state == 2 && output.value == (s32)&entities[3]);
CHECK((u16)output.pad16 == 0xA5A5 && output.pad1E == 0xA5A5);
''')
