import csv
import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameLowestHeightQueryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Reuse the 32-bit build harness and shared query layouts, not its tests.
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        match = re.search(r"s32 func_15045384\([^;{]*\{\n.*?\n\}", source, re.S)
        if match is None:
            raise AssertionError("lowest-height query definition was not found")
        prefix = cls.source.split("void func_1510F800", 1)[0].replace(
            "f32 D_80098D44 = -10000.0f;", "f32 D_80098D48 = 99999.8984375f;")
        suffix = cls.source[cls.source.index("static void initialize(void)"):].replace(
            "vertexIndex = 1;", "vertexIndex = 16;").replace("threshold = 0;", "threshold = 20;")
        cls.source = prefix + r'''
void func_1510F800(s32 mode) {
    if (mode != 3 || phase != 0 || output.height != D_80098D48) error = 1;
    phase = 1;
    if (mutation == 1) {
        query_position[0] = 1.75f; query_position[1] = 1.5f; query_position[2] = -2.75f;
    }
}
s32 func_150A4FA0(s32 x, s32 z) {
    if (phase != 1 || D_800DBE68 != -123 || D_800DBE6C != -123 ||
        D_800DBE70 != -123 || D_800DBE74 != -123) error = 2;
    query_x = x; query_z = z; phase = 2;
    if (mutation == 2) query_position[1] = 3;
    if (mutation == 3) output.height = 2;
    return candidate_count;
}
''' + match.group(0) + suffix

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_guest_layout_and_default_byte_offset(self):
        self.run_case(r'''
CHECK(sizeof(HeightCandidate71820) == 16 && sizeof(HeightResult71820) == 36);
CHECK(sizeof(QueryVertex71820) == 16 && sizeof(QueryTriangle71820) == 12);
initialize(); query_position[1] = 0;
CHECK(func_15045384(query_position, threshold, &output) == 1 && copied(0, 1));
CHECK(output.metadata == 0 && output.state == 4 && output.value == 0 && error == 0);
''')

    def test_early_rejection_changes_only_flag_bit_and_calls_nothing(self):
        self.run_case(r'''
s32 flag, byte; u8 before[36];
for (flag = 0; flag < 256; flag++) {
    initialize(); threshold = 9; output.flags = flag;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
    CHECK(func_15045384(query_position, threshold, &output) == 0 && phase == 0);
    CHECK(output.flags == (flag & ~2) && D_800DBE68 == -123);
    for (byte = 0; byte < 36; byte++) if (byte != 0x1C)
        CHECK(before[byte] == ((u8 *)&output)[byte]);
}
''')

    def test_lowest_eligible_candidate_first_tie_and_truncated_coordinates(self):
        self.run_case(r'''
initialize(); query_position[1] = 1.5f;
D_800D3300[2].fixedHeight = 2 * 256;
CHECK(func_15045384(query_position, threshold, &output) == 1 && error == 0);
CHECK(output.height == 2 && copied(1, 1) && output.flags == 0xA7);
CHECK(query_x == -12 && query_z == 23 && phase == 2);
''')

    def test_y_and_threshold_equality_are_inclusive(self):
        self.run_case(r'''
initialize(); query_position[1] = threshold = 3;
CHECK(func_15045384(query_position, threshold, &output) == 1);
CHECK(output.height == 3 && copied(2, 1) && error == 0);
''')

    def test_selected_above_threshold_still_publishes_and_sets_flags(self):
        self.run_case(r'''
s32 flag;
for (flag = 0; flag < 256; flag++) {
    initialize(); query_position[1] = 0; threshold = 0.5f; output.flags = flag;
    CHECK(func_15045384(query_position, threshold, &output) == 0 && error == 0);
    CHECK(output.height == 1 && output.flags == (flag | 6));
    CHECK(copied(0, 1) && output.metadata == 0 && output.state == 4 && output.value == 0);
}
''')

    def test_nonpositive_count_preserves_other_fields(self):
        self.run_case(r'''
s32 count, flag, byte; u8 before[36];
for (count = -5; count <= 0; count++) for (flag = 0; flag < 256; flag++) {
    initialize(); candidate_count = count; output.flags = flag;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
    CHECK(func_15045384(query_position, threshold, &output) == 0 && phase == 2 && error == 0);
    CHECK(output.height == D_80098D48 && output.flags == (flag & ~2));
    for (byte = 4; byte < 36; byte++) if (byte != 0x1C)
        CHECK(before[byte] == ((u8 *)&output)[byte]);
}
''')

    def test_no_eligible_height_and_strict_positive_sentinel(self):
        self.run_case(r'''
s32 i;
initialize();
CHECK(func_15045384(query_position, threshold, &output) == 0 && output.height == D_80098D48);
initialize(); query_position[1] = 0;
for (i = 0; i < 4; i++) D_800D3300[i].fixedHeight = i == 0 ? 25599974 : 25599976;
CHECK(func_15045384(query_position, threshold, &output) == 0 && output.height == D_80098D48);
''')

    def test_signed_fractional_height_and_non_record_byte_offset(self):
        self.run_case(r'''
s32 v; s16 *coords;
initialize(); query_position[1] = -3; threshold = 0; candidate_count = 1;
D_800D3300[0].fixedHeight = -385; D_800D3300[0].vertexIndex = 2;
for (v = 0; v < 3; v++) {
    coords = (s16 *)((u8 *)vertices[0][v] + 2);
    coords[0] = -32768 + v; coords[1] = 32767 - v; coords[2] = -12 + v;
}
CHECK(func_15045384(query_position, threshold, &output) == 1 && error == 0);
CHECK(output.height == -1.50390625f);
for (v = 0; v < 3; v++) {
    CHECK(output.vertices[v * 3] == -32768 + v);
    CHECK(output.vertices[v * 3 + 1] == 32767 - v);
    CHECK(output.vertices[v * 3 + 2] == -12 + v);
}
''')

    def test_positions_and_height_reloaded_after_callbacks(self):
        self.run_case(r'''
initialize(); mutation = 1;
CHECK(func_15045384(query_position, threshold, &output) == 1 && error == 0);
CHECK(query_x == 1 && query_z == -2 && output.height == 2 && copied(1, 1));
initialize(); mutation = 2;
CHECK(func_15045384(query_position, threshold, &output) == 1 && output.height == 3);
initialize(); query_position[1] = 0; mutation = 3;
CHECK(func_15045384(query_position, threshold, &output) == 1 && output.height == 1);
''')

    def test_nan_query_and_threshold_follow_ordered_comparisons(self):
        self.run_case(r'''
initialize(); query_position[1] = nan_value();
CHECK(func_15045384(query_position, threshold, &output) == 0 && phase == 2);
CHECK(output.height == D_80098D48);
initialize(); query_position[1] = 0; threshold = nan_value();
CHECK(func_15045384(query_position, threshold, &output) == 0 && copied(0, 1));
CHECK(output.flags == 0xA7 && output.state == 4);
''')

    def test_result_padding_and_surrounding_state_preserved(self):
        self.run_case(r'''
initialize(); query_position[1] = 0;
CHECK(func_15045384(query_position, threshold, &output) == 1);
CHECK((u16)output.pad16 == 0xA5A5 && output.pad1E == 0xA5A5);
CHECK(D_800DBE68 == -123 && D_800DBE6C == -123 && D_800DBE70 == -123 && D_800DBE74 == -123);
CHECK(D_800D3300[0].padC == 0x654321 && metadata[0] == 0x12340000);
''')

    def test_guard_sets_are_closed_and_strict(self):
        path = Path(__file__).resolve().parents[2] / "conker/retail_word_patches.us.csv"
        with path.open(newline="") as stream:
            rows = [row for row in csv.DictReader(stream)
                    if row["function"] == "func_15045384"]
        guards = {int(row["offset"], 0): (int(row["expected"], 0),
                                         int(row["replacement"], 0)) for row in rows}
        self.assertEqual(len(rows), 15)
        self.assertEqual(set(guards), {0x60, 0x84, 0x8C, 0x94, 0xCC, 0xE0,
                                      0xE4, 0xEC, 0xF0, 0x13C, 0x140, 0x144,
                                      0x148, 0x14C, 0x154})
        for row in rows:
            self.assertEqual(row["filename"], "generated_71820")
            self.assertEqual(row["expected_relocations"], "-")
            self.assertEqual(row["replacement_relocations"], "-")
            self.assertEqual(row["insert_after"], "")
            self.assertEqual(row["omit"], "false")
            self.assertNotEqual(row.get("allow_mismatch"), "true")
        self.assertEqual(guards[0x60], (0xAFA60024, 0xAFA60020))
        self.assertEqual(guards[0x84], (0x8FA60024, 0x8FA60020))
        for offset in (0x8C, 0x94, 0xCC, 0xE0, 0xE4, 0xEC, 0xF0):
            original, replacement = guards[offset]
            # Simultaneously rename count/index a0 <-> v1 in all operands.
            shifts = (21, 16, 11) if original >> 26 == 0 else (21, 16)
            renamed = original
            for shift in shifts:
                register = (original >> shift) & 31
                if register in (3, 4):
                    renamed = (renamed & ~(31 << shift)) | ((7 - register) << shift)
            self.assertEqual(renamed, replacement)
        expected_copy = {0x13C: (0x24630006, 0xA46E0004),
                         0x140: (0xA46EFFFE, 0x844F0002),
                         0x144: (0x844F0002, 0xA46F0006),
                         0x148: (0xA46F0000, 0x84580004),
                         0x14C: (0x84580004, 0xA4780008),
                         0x154: (0xA4780002, 0x24630006)}
        self.assertEqual({offset: guards[offset] for offset in expected_copy}, expected_copy)

    def test_copy_schedule_equivalence_with_overlapping_vertex_storage(self):
        raw = [0x844E0000, 0x24630006, 0xA46EFFFE, 0x844F0002,
               0xA46F0000, 0x84580004, 0x1486FFF5, 0xA4780002]
        retail = [0x844E0000, 0xA46E0004, 0x844F0002, 0xA46F0006,
                  0x84580004, 0xA4780008, 0x1486FFF5, 0x24630006]

        def execute(words, destination):
            memory = {address: (address * 7919) & 0xFFFF for address in range(64, 160, 2)}
            registers = [0] * 32
            registers[2], registers[3] = 100, destination
            accesses = []
            for word in words:
                opcode, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
                immediate = word & 0xFFFF
                if immediate >= 0x8000:
                    immediate -= 0x10000
                address = registers[rs] + immediate
                if opcode == 33:
                    value = memory[address]
                    registers[rt] = value if value < 0x8000 else value - 0x10000
                    accesses.append(("load", address, value))
                elif opcode == 41:
                    memory[address] = registers[rt] & 0xFFFF
                    accesses.append(("store", address, memory[address]))
                elif opcode == 9:
                    registers[rt] = address
                else:
                    self.assertEqual(word, 0x1486FFF5)
            return memory, registers, accesses

        for displacement in range(-12, 14, 2):
            self.assertEqual(execute(raw, 100 + displacement),
                             execute(retail, 100 + displacement))
