import csv
import re
import unittest
from pathlib import Path

from tools.tests import test_game_lowest_height_query as lowest


class GameContext3HighestHeightQueryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        lowest.GameLowestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        body = re.search(r"s32 func_1504554C\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("context-3 highest-height definition was not found")
        cls.source = re.sub(r"s32 func_15045384\([^;{]*\{\n.*?\n\}",
                            lambda _: body.group(0), cls.source, flags=re.S)
        cls.source = cls.source.replace("D_80098D48", "D_80098D4C").replace(
            "99999.8984375f", "-10000.0f").replace("threshold = 20;", "threshold = 0;")

    run_case = lowest.GameLowestHeightQueryTests.run_case

    def test_layout_byte_offset_and_state4_publication(self):
        self.run_case(r'''
CHECK(sizeof(HeightCandidate71820) == 16 && sizeof(HeightResult71820) == 36);
CHECK(sizeof(QueryVertex71820) == 16 && sizeof(QueryTriangle71820) == 12);
initialize();
CHECK(func_1504554C(query_position, threshold, &output) == 1 && copied(3, 1));
CHECK(output.height == 4 && output.metadata == 0 && output.state == 4 && output.value == 0);
CHECK(error == 0 && query_x == -12 && query_z == 23);
''')

    def test_early_rejection_all_flags_preserves_other_bytes_and_calls_nothing(self):
        self.run_case(r'''
s32 flag, byte; u8 before[36];
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = 11; output.flags = flag;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
    CHECK(func_1504554C(query_position, threshold, &output) == 0 && phase == 0);
    CHECK(output.flags == (flag & ~2));
    for (byte = 0; byte < 36; byte++) if (byte != 0x1C)
        CHECK(before[byte] == ((u8 *)&output)[byte]);
}
''')

    def test_highest_eligible_candidate_and_first_tie(self):
        self.run_case(r'''
initialize(); D_800D3300[0].fixedHeight = D_800D3300[1].fixedHeight = 9 * 256;
D_800D3300[2].fixedHeight = 11 * 256;
CHECK(func_1504554C(query_position, threshold, &output) == 1);
CHECK(output.height == 9 && copied(0, 1) && error == 0);
''')

    def test_y_and_threshold_equalities_are_inclusive(self):
        self.run_case(r'''
initialize(); query_position[1] = threshold = 3;
CHECK(func_1504554C(query_position, threshold, &output) == 1);
CHECK(output.height == 3 && copied(2, 1));
''')

    def test_selected_below_threshold_publishes_flags6_and_returns_zero(self):
        self.run_case(r'''
s32 flag;
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = 5; output.flags = flag;
    CHECK(func_1504554C(query_position, threshold, &output) == 0 && error == 0);
    CHECK(output.height == 4 && output.flags == (flag | 6));
    CHECK(copied(3, 1) && output.metadata == 0 && output.state == 4 && output.value == 0);
}
''')

    def test_nonpositive_count_all_flags_preserves_non_result_fields(self):
        self.run_case(r'''
s32 count, flag, byte; u8 before[36];
for (count = -5; count <= 0; count++) for (flag = 0; flag < 256; flag++) {
    initialize(); candidate_count = count; output.flags = flag;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
    CHECK(func_1504554C(query_position, threshold, &output) == 0 && phase == 2 && error == 0);
    CHECK(output.height == -10000 && output.flags == (flag & ~2));
    for (byte = 4; byte < 36; byte++) if (byte != 0x1C)
        CHECK(before[byte] == ((u8 *)&output)[byte]);
}
''')

    def test_no_eligible_candidate_and_strict_negative_sentinel(self):
        self.run_case(r'''
s32 i;
initialize();
for (i = 0; i < 4; i++) D_800D3300[i].fixedHeight = 11 * 256;
CHECK(func_1504554C(query_position, threshold, &output) == 0 && output.height == -10000);
initialize();
for (i = 0; i < 4; i++) D_800D3300[i].fixedHeight = (i == 0 ? -10000 : -10001) * 256;
CHECK(func_1504554C(query_position, threshold, &output) == 0 && output.height == -10000);
''')

    def test_signed_fractional_height_and_non_record_offset(self):
        self.run_case(r'''
s32 v; s16 *coords;
initialize(); threshold = -3; candidate_count = 1;
D_800D3300[0].fixedHeight = -385; D_800D3300[0].vertexIndex = 2;
for (v = 0; v < 3; v++) {
    coords = (s16 *)((u8 *)vertices[0][v] + 2);
    coords[0] = -32768 + v; coords[1] = 32767 - v; coords[2] = -12 + v;
}
CHECK(func_1504554C(query_position, threshold, &output) == 1 && error == 0);
CHECK(output.height == -1.50390625f);
for (v = 0; v < 3; v++) {
    CHECK(output.vertices[v * 3] == -32768 + v);
    CHECK(output.vertices[v * 3 + 1] == 32767 - v);
    CHECK(output.vertices[v * 3 + 2] == -12 + v);
}
''')

    def test_signed_negative_vertex_byte_offset(self):
        self.run_case(r'''
s32 v;
initialize(); candidate_count = 1; D_800D3300[0].vertexIndex = -16;
for (v = 0; v < 3; v++) triangles[0].vertices[v] = &vertices[0][v][1];
CHECK(func_1504554C(query_position, threshold, &output) == 1 && copied(0, 0));
''')

    def test_callback_mutations_use_reloaded_position_and_result_height(self):
        self.run_case(r'''
initialize(); mutation = 1;
CHECK(func_1504554C(query_position, threshold, &output) == 1 && error == 0);
CHECK(query_x == 1 && query_z == -2 && output.height == 1 && copied(0, 1));
initialize(); mutation = 2;
CHECK(func_1504554C(query_position, threshold, &output) == 1 && output.height == 3);
initialize(); mutation = 3;
CHECK(func_1504554C(query_position, threshold, &output) == 1 && output.height == 4);
''')

    def test_nan_predicates(self):
        self.run_case(r'''
initialize(); query_position[1] = nan_value();
CHECK(func_1504554C(query_position, threshold, &output) == 0 && phase == 2);
CHECK(output.height == -10000);
initialize(); threshold = nan_value();
CHECK(func_1504554C(query_position, threshold, &output) == 0 && copied(3, 1));
CHECK(output.flags == 0xA7 && output.state == 4);
''')

    def test_padding_and_context0_globals_untouched(self):
        self.run_case(r'''
initialize();
CHECK(func_1504554C(query_position, threshold, &output) == 1);
CHECK((u16)output.pad16 == 0xA5A5 && output.pad1E == 0xA5A5);
CHECK(D_800DBE68 == -123 && D_800DBE6C == -123 && D_800DBE70 == -123 && D_800DBE74 == -123);
CHECK(metadata[3] == 0x12340003 && D_800D3300[3].padC == 0x654321);
''')

    def test_guards_equal_the_proven_context3_normalization(self):
        path = Path(__file__).resolve().parents[2] / "conker/retail_word_patches.us.csv"
        with path.open(newline="") as stream:
            rows = list(csv.DictReader(stream))
        old = [row for row in rows if row["function"] == "func_15045384"]
        new = [row for row in rows if row["function"] == "func_1504554C"]
        self.assertEqual(len(new), 15)
        fields = ("filename", "offset", "expected", "replacement",
                  "expected_relocations", "replacement_relocations",
                  "insert_after", "insert_after_relocations", "omit")
        self.assertEqual([tuple(row[field] for field in fields) for row in new],
                         [tuple(row[field] for field in fields) for row in old])
        for row in new:
            self.assertNotEqual(row.get("allow_mismatch"), "true")
