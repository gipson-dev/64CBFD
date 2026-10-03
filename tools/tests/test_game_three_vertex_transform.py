import csv
import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameThreeVertexTransformTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        layout = re.search(r"typedef struct QueryVertex71820 \{\n.*?\n\} "
                           r"QueryVertex71820;", source, re.S)
        body = re.search(r"void func_1504452C\([^;{]*\{\n.*?\n\}", source, re.S)
        if layout is None or body is None:
            raise AssertionError("three-vertex transform/layout is missing")
        cls.source = highest.TYPES + layout.group(0) + body.group(0) + r'''
static QueryVertex71820 records[3][3], *pointers[3];
static struct { u32 before[4]; f32 values[3][3]; u32 after[4]; } output;
static u8 saved[sizeof(records)];
static f32 sine, cosine, origin[3];
static s32 offset;
static u32 bits(f32 value) {
    union { f32 value; u32 bits; } number;
    number.value = value; return number.bits;
}
static f32 from_bits(u32 value) {
    union { f32 value; u32 bits; } number;
    number.bits = value; return number.value;
}
static s32 equal(f32 a, f32 b) {
    if (a != a || b != b) return a != a && b != b;
    return bits(a) == bits(b);
}
static void initialize(void) {
    s32 i, j;
    for (i = 0; i < sizeof(records); i++) ((u8 *)records)[i] = 0xA5;
    for (i = 0; i < 3; i++) {
        pointers[i] = &records[i][0];
        for (j = 0; j < 3; j++) {
            records[i][j].x = 10 + i * 100 + j * 20;
            records[i][j].y = -20 - i * 200 - j * 30;
            records[i][j].z = 30 + i * 300 + j * 40;
        }
        for (j = 0; j < 3; j++) output.values[i][j] = 999;
    }
    for (i = 0; i < 4; i++) output.before[i] = output.after[i] = 0xDEADBEEF;
    sine = 0; cosine = 1; origin[0] = origin[1] = origin[2] = 0; offset = 0;
}
static void transform(void) {
    s32 i;
    for (i = 0; i < sizeof(records); i++) saved[i] = ((u8 *)records)[i];
    func_1504452C(pointers, output.values, sine, cosine,
                 origin[0], origin[1], origin[2], offset);
}
static s32 matches(void) {
    s32 i; f32 x, y, z, expected_x, expected_z;
    QueryVertex71820 *v;
    for (i = 0; i < 3; i++) {
        v = (QueryVertex71820 *)((u8 *)pointers[i] + offset);
        x = (f32)v->x - origin[0]; y = (f32)v->y - origin[1];
        z = (f32)v->z - origin[2];
        expected_x = cosine * x + sine * z;
        expected_z = cosine * z - sine * x;
        if (!equal(output.values[i][0], expected_x) ||
            !equal(output.values[i][1], y) ||
            !equal(output.values[i][2], expected_z)) return 0;
    }
    for (i = 0; i < sizeof(records); i++)
        if (((u8 *)records)[i] != saved[i]) return 0;
    for (i = 0; i < 4; i++)
        if (output.before[i] != 0xDEADBEEF || output.after[i] != 0xDEADBEEF) return 0;
    return 1;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_identity_copies_exactly_three_signed_coordinates(self):
        self.run_case(r'''
initialize(); transform(); CHECK(matches());
CHECK(output.values[0][0] == 10 && output.values[1][1] == -220);
CHECK(output.values[2][2] == 630);
''')

    def test_quarter_turn_and_fractional_origin(self):
        self.run_case(r'''
initialize(); sine = 1; cosine = 0;
origin[0] = 1.25f; origin[1] = -2.5f; origin[2] = 3.75f;
transform(); CHECK(matches());
CHECK(output.values[0][0] == 26.25f && output.values[0][2] == -8.75f);
CHECK(output.values[0][1] == -17.5f);
''')

    def test_positive_byte_offset_selects_second_record(self):
        self.run_case(r'''
initialize(); offset = 16; transform(); CHECK(matches());
CHECK(output.values[0][0] == 30 && output.values[0][1] == -50);
''')

    def test_negative_byte_offset_within_each_allocation(self):
        self.run_case(r'''
s32 i; initialize(); for (i = 0; i < 3; i++) pointers[i] = &records[i][1];
offset = -16; transform(); CHECK(matches() && output.values[0][0] == 10);
''')

    def test_signed_halfword_extremes_are_not_unsigned_or_clamped(self):
        self.run_case(r'''
initialize(); records[0][0].x = -32768; records[0][0].y = 32767;
records[0][0].z = -1; transform(); CHECK(matches());
CHECK(output.values[0][0] == -32768 && output.values[0][1] == 32767);
CHECK(output.values[0][2] == -1);
''')

    def test_independent_pointer_order_and_repeated_vertices(self):
        self.run_case(r'''
initialize(); pointers[0] = &records[2][2]; pointers[1] = &records[0][1];
pointers[2] = pointers[0]; transform(); CHECK(matches());
CHECK(output.values[0][0] == output.values[2][0]);
CHECK(output.values[1][0] == 30);
''')

    def test_coefficients_are_used_without_normalization(self):
        self.run_case(r'''
initialize(); sine = -2; cosine = 3; transform(); CHECK(matches());
CHECK(output.values[0][0] == -30 && output.values[0][2] == 110);
''')

    def test_general_coefficients_and_origins(self):
        self.run_case(r'''
s32 trial; for (trial = 0; trial < 128; trial++) {
    initialize(); sine = trial * 0.03125f - 2; cosine = trial * -0.015625f + 1;
    origin[0] = trial * 0.125f; origin[1] = trial * -0.25f;
    origin[2] = trial * 0.0625f; offset = (trial % 3) * 16;
    transform(); CHECK(matches());
}
''')

    def test_nan_coefficients_propagate_without_changing_y(self):
        self.run_case(r'''
initialize(); sine = from_bits(0x7FC12345); transform(); CHECK(matches());
CHECK(output.values[0][0] != output.values[0][0]);
CHECK(output.values[0][2] != output.values[0][2]);
CHECK(output.values[0][1] == -20);
''')

    def test_vertex_at_origin_produces_zero(self):
        self.run_case(r'''
initialize(); origin[0] = 10; origin[1] = -20; origin[2] = 30;
sine = -0.5f; cosine = 0.75f; transform(); CHECK(matches());
CHECK(output.values[0][0] == 0 && output.values[0][1] == 0 && output.values[0][2] == 0);
''')

    def test_guards_only_close_register_cycles_and_swap_independent_loads(self):
        root = Path(__file__).resolve().parents[2]
        assembly = (root / "conker/asm/71820.s").read_text()
        body = re.search(r"glabel func_1504452C\n.*?endlabel func_1504452C",
                         assembly, re.S).group(0)
        retail = [int(word, 16) for word in re.findall(
            r"/\*\s*[0-9A-F]+\s+[0-9A-F]{8}\s+([0-9A-F]{8})\s*\*/", body)]
        with (root / "conker/retail_word_patches.us.csv").open(newline="") as stream:
            guards = [row for row in csv.DictReader(stream)
                      if row["filename"] == "generated_71820"
                      and row["function"] == "func_1504452C"]
        self.assertEqual(len(guards), 20)
        self.assertEqual(len({row["offset"] for row in guards}), 20)
        raw = retail[:]
        for row in guards:
            index = int(row["offset"], 0) // 4
            self.assertEqual(int(row["replacement"], 0), retail[index])
            self.assertEqual(row["expected_relocations"], "-")
            self.assertEqual(row["replacement_relocations"], "-")
            self.assertEqual(row["omit"], "false")
            self.assertFalse(row["insert_after"])
            raw[index] = int(row["expected"], 0)

        def rename(word):
            opcode = word >> 26
            gpr = {24: 25, 25: 24}
            fpr = {12: 16, 16: 12, 14: 18, 18: 14}

            def field(shift, mapping):
                nonlocal word
                value = (word >> shift) & 31
                word = (word & ~(31 << shift)) | (mapping.get(value, value) << shift)

            if opcode == 33:
                field(16, gpr)
            elif opcode in (49, 57):
                field(16, fpr)
            elif opcode == 17:
                fmt = (word >> 21) & 31
                if fmt == 4:
                    field(16, gpr)
                    field(11, fpr)
                elif fmt in (16, 20):
                    field(16, fpr)
                    field(11, fpr)
                    field(6, fpr)
            return word

        normalized = [rename(word) for word in raw]
        self.assertEqual(normalized[9], 0xC7AE002C)
        self.assertEqual(normalized[10], 0xC7B20030)
        normalized[9], normalized[10] = normalized[10], normalized[9]
        self.assertEqual(normalized, retail)


if __name__ == "__main__":
    unittest.main()
