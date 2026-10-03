import csv
import re
import struct
import unittest
from pathlib import Path

from tools.tests import test_game_actor_dimension_helper as dimensions


class GameNestedFloatCopyClampTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dimensions.GameActorDimensionHelperTests.setUpClass.__func__(cls)
        shared = (cls.project / "include/structs.h").read_text()
        layouts = [match.group(0) for match in re.finditer(
            r"typedef struct \{\n.*?\n\} (\w+);", shared, re.S)
                   if match.group(1) == "struct197"]
        if len(layouts) != 1:
            raise AssertionError("production nested layout was not found")
        cls.source = cls.source.replace("typedef struct struct197 struct197;", layouts[0])
        source = (cls.project / "src/game/generated_A9260.c").read_text()
        body = re.search(r"void func_1507C324\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("production copy/clamp definition was not found")
        cls.source += "\n" + body.group(0) + r'''
static struct197 destinationState, sourceState;
static void setup_copy(void) {
    initialize();
    clear_bytes(&destinationState, sizeof(destinationState));
    clear_bytes(&sourceState, sizeof(sourceState));
    actor.unk2D0 = &destinationState;
    D_800CC2D0[1].unk2D0 = &sourceState;
    sourceState.unk8 = 4;
    destinationState.unk8 = -123;
    destinationState.unk18 = 10;
}
static void copy_clamp(void) { func_1507C324(&actor, &D_800CC2D0[1]); }
static void set_bits(f32 *value, u32 bits) { *(u32 *)value = bits; }
static u32 bits(f32 *value) { return *(u32 *)value; }
'''

    run_case = dimensions.GameActorDimensionHelperTests.run_case

    def test_nested_layout_offsets(self):
        self.run_case(r'''
    if (__builtin_offsetof(struct127, unk2D0) != 0x2D0 ||
        __builtin_offsetof(struct197, unk8) != 8 ||
        __builtin_offsetof(struct197, unk18) != 0x18) return 1;
    return 0;
''')

    def test_null_destination_nested_pointer(self):
        self.run_case(r'''
    setup_copy(); actor.unk2D0 = NULL; copy_clamp();
    if (destinationState.unk8 != -123 || sourceState.unk8 != 4) return 1;
    return 0;
''')

    def test_null_source_nested_pointer(self):
        self.run_case(r'''
    setup_copy(); D_800CC2D0[1].unk2D0 = NULL; copy_clamp();
    if (destinationState.unk8 != -123 || sourceState.unk8 != 4) return 1;
    actor.unk2D0 = NULL; copy_clamp();
    if (destinationState.unk8 != -123) return 2;
    return 0;
''')

    def test_copy_below_limit(self):
        self.run_case(r'''
    setup_copy(); copy_clamp();
    if (destinationState.unk8 != 4 || sourceState.unk8 != 4 ||
        destinationState.unk18 != 10) return 1;
    return 0;
''')

    def test_equal_and_above_limit_clamp(self):
        self.run_case(r'''
    setup_copy(); sourceState.unk8 = 9; copy_clamp();
    if (destinationState.unk8 != 9) return 1;
    sourceState.unk8 = 100; copy_clamp();
    if (destinationState.unk8 != 9 || sourceState.unk8 != 100) return 2;
    copy_clamp(); if (destinationState.unk8 != 9) return 3;
    return 0;
''')

    def test_negative_limit_and_fractional_subtraction(self):
        self.run_case(r'''
    setup_copy(); destinationState.unk18 = -3.25f; sourceState.unk8 = -1;
    copy_clamp(); if (destinationState.unk8 != -4.25f) return 1;
    sourceState.unk8 = -7.75f;
    copy_clamp(); if (destinationState.unk8 != -7.75f) return 2;
    return 0;
''')

    def test_shared_nested_state_and_actor_alias(self):
        self.run_case(r'''
    setup_copy(); D_800CC2D0[1].unk2D0 = &destinationState;
    destinationState.unk8 = 12; copy_clamp();
    if (destinationState.unk8 != 9) return 1;
    destinationState.unk8 = 3;
    func_1507C324(&actor, &actor);
    if (destinationState.unk8 != 3) return 2;
    destinationState.unk8 = 15;
    func_1507C324(&actor, &actor);
    if (destinationState.unk8 != 9) return 3;
    return 0;
''')

    def test_captured_source_pointer_survives_overlapping_output(self):
        self.run_case(r'''
    struct197 *overlap;
    setup_copy();
    overlap = (struct197 *)((u8 *)&D_800CC2D0[1] + 0x2C8);
    actor.unk2D0 = overlap;
    overlap->unk18 = 10;
    copy_clamp();
    if (overlap->unk8 != 4 || (u32)D_800CC2D0[1].unk2D0 != 0x40800000) return 1;
    return 0;
''')

    def test_nan_source_payload_is_copied_without_clamp(self):
        self.run_case(r'''
    setup_copy(); set_bits(&sourceState.unk8, 0x7FC12345);
    copy_clamp();
    if (bits(&destinationState.unk8) != 0x7FC12345 ||
        bits(&sourceState.unk8) != 0x7FC12345) return 1;
    return 0;
''')

    def test_nan_limit_does_not_replace_finite_copy(self):
        self.run_case(r'''
    setup_copy(); set_bits(&destinationState.unk18, 0x7FCABCDE);
    copy_clamp();
    if (destinationState.unk8 != 4 || bits(&destinationState.unk18) != 0x7FCABCDE) return 1;
    return 0;
''')

    def test_infinities(self):
        self.run_case(r'''
    setup_copy(); set_bits(&sourceState.unk8, 0x7F800000);
    copy_clamp(); if (destinationState.unk8 != 9) return 1;
    set_bits(&sourceState.unk8, 0xFF800000);
    copy_clamp(); if (bits(&destinationState.unk8) != 0xFF800000) return 2;
    sourceState.unk8 = 4; set_bits(&destinationState.unk18, 0x7F800000);
    copy_clamp(); if (destinationState.unk8 != 4) return 3;
    set_bits(&destinationState.unk18, 0xFF800000);
    copy_clamp(); if (bits(&destinationState.unk8) != 0xFF800000) return 4;
    return 0;
''')

    def test_equality_clamp_preserves_retail_signed_zero_result(self):
        self.run_case(r'''
    setup_copy(); destinationState.unk18 = 1; set_bits(&sourceState.unk8, 0x80000000);
    copy_clamp(); if (bits(&destinationState.unk8) != 0) return 1;
    destinationState.unk18 = 10;
    copy_clamp(); if (bits(&destinationState.unk8) != 0x80000000) return 2;
    return 0;
''')

    def test_only_destination_value_bytes_change(self):
        self.run_case(r'''
    struct197 before, sourceBefore;
    u32 i;
    setup_copy();
    for (i = 0; i < sizeof(destinationState); i++) ((u8 *)&destinationState)[i] = 0xA5;
    destinationState.unk18 = 10;
    before = destinationState; sourceBefore = sourceState;
    copy_clamp();
    for (i = 0; i < sizeof(destinationState); i++) {
        if ((i < 8 || i >= 12) && ((u8 *)&destinationState)[i] != ((u8 *)&before)[i]) return 1;
        if (((u8 *)&sourceState)[i] != ((u8 *)&sourceBefore)[i]) return 2;
    }
    if (destinationState.unk8 != 4) return 3;
    return 0;
''')

    def test_guards_are_only_one_closed_fpr_permutation(self):
        assembly = (self.project / "asm/nonmatchings/generated_A9260/func_1507C324.s").read_text()
        reference = [int(word, 16) for word in re.findall(
            r"/\*\s*[0-9A-Fa-f]+\s+[0-9A-Fa-f]{8}\s+([0-9A-Fa-f]{8})\s*\*/", assembly)]
        self.assertEqual(len(reference), 19)
        with (self.project / "retail_word_patches.us.csv").open(newline="") as stream:
            rows = [row for row in csv.DictReader(stream)
                    if row["function"] == "func_1507C324"]
        self.assertEqual(len(rows), 8)
        self.assertEqual({int(row["offset"], 0) for row in rows},
                         {0x18, 0x1C, 0x20, 0x24, 0x28, 0x2C, 0x30, 0x40})
        compiled = reference[:]
        for row in rows:
            self.assertEqual(row["filename"], "generated_A9260")
            self.assertEqual(row["expected_relocations"], "-")
            self.assertEqual(row["replacement_relocations"], "-")
            self.assertFalse(row["insert_after"])
            self.assertEqual(row["omit"], "false")
            index = int(row["offset"], 0) // 4
            self.assertEqual(int(row["replacement"], 0), reference[index])
            compiled[index] = int(row["expected"], 0)
        rename = {0: 4, 4: 8, 8: 2, 2: 6, 6: 10, 10: 12, 12: 0}
        self.assertEqual(set(rename), set(rename.values()))

        def field(word, shift):
            register = (word >> shift) & 31
            return (word & ~(31 << shift)) | (rename.get(register, register) << shift)

        normalized = []
        for word in compiled:
            opcode, rs = word >> 26, (word >> 21) & 31
            if opcode in (49, 57):
                word = field(word, 16)
            elif opcode == 17 and rs == 4:
                word = field(word, 11)
            elif opcode == 17 and rs == 16:
                word = field(field(word, 16), 11)
                if word & 63 == 1:
                    word = field(word, 6)
            normalized.append(word)
        self.assertEqual(normalized, reference)
        self.assertEqual(compiled[-2:], [0x03E00008, 0])
        self.assertEqual(struct.pack(">19I", *normalized), struct.pack(">19I", *reference))


if __name__ == "__main__":
    unittest.main()
