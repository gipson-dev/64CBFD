import csv
import re
import struct
import unittest

from tools.tests import test_game_actor_dimension_helper as dimensions


class GameActorStepDispatcherTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dimensions.GameActorDimensionHelperTests.setUpClass.__func__(cls)
        source = (cls.project / "src/game/generated_A9260.c").read_text()
        body = re.search(r"void func_1507C22C\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("production actor-step dispatcher not found")
        cls.source += r'''
#undef actor
u8 D_800C3638;
s32 D_800C3654;
#define D_800D121C D_800CC2D0[25].interaction_state
static s32 predicate_calls[26], update_calls[26], predicate_result[26];
static s32 order[52], events, mutation, error, expected_mode;
static struct197 *observed_state[26];
static u32 observed_step[26];
static s32 actor_index(struct127 *p) { return p - D_800CC2D0; }
s32 func_150229E4(struct127 *p) {
    s32 i = actor_index(p);
    if (i < 0 || i >= 25) { error = 1; return 0; }
    predicate_calls[i]++; order[events++] = i * 2;
    if (mutation == 1) { p->unk2D0 = (struct197 *)0x12345678; p->unk48 = -7.5f; }
    if (mutation == 2) p->unk2D0 = 0;
    if (mutation == 3) p->unk2FA = 0;
    return predicate_result[i];
}
s32 func_1507BDB0(struct197 *state, s32 step_bits, struct127 *p, s32 mode) {
    s32 i = actor_index(p);
    if (i < 0 || i >= 25 || mode != expected_mode) { error = 2; return 0; }
    update_calls[i]++; order[events++] = i * 2 + 1;
    observed_state[i] = state; observed_step[i] = step_bits;
    if (mutation == 4) { D_800C3638 = 1; *(u8 *)&D_800C3654 = 0; }
    if (mutation == 5 && i == 0) D_800CC2D0[1].interaction_state = 0;
    return -123;
}
''' + body.group(0) + r'''
static void setup_dispatch(void) {
    s32 i;
    initialize();
    clear_bytes(predicate_calls, sizeof(predicate_calls));
    clear_bytes(update_calls, sizeof(update_calls));
    clear_bytes(observed_state, sizeof(observed_state));
    clear_bytes(observed_step, sizeof(observed_step));
    events = mutation = error = expected_mode = 0;
    D_800C3638 = 0; D_800C3654 = 0;
    for (i = 0; i < 26; i++) {
        D_800CC2D0[i].interaction_state = 1;
        D_800CC2D0[i].unk5 = 4;
        D_800CC2D0[i].unk2D0 = (struct197 *)(0x12340000 + i * 4);
        D_800CC2D0[i].unk2FA = 1;
        D_800CC2D0[i].unk48 = 0.25f + i;
        predicate_result[i] = 1;
    }
}
static void dispatch(s32 mode) { expected_mode = mode; func_1507C22C(mode); }
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = dimensions.GameActorDimensionHelperTests.run_case

    def test_layout_offsets(self):
        self.run_case(r'''
CHECK(sizeof(struct127) == 0x32C);
CHECK(__builtin_offsetof(struct127, interaction_state) == 0);
CHECK(__builtin_offsetof(struct127, unk5) == 5);
CHECK(__builtin_offsetof(struct127, unk48) == 0x48);
CHECK(__builtin_offsetof(struct127, unk25C) == 0x25C);
CHECK(__builtin_offsetof(struct127, unk2D0) == 0x2D0);
CHECK(__builtin_offsetof(struct127, unk2FA) == 0x2FA);
return 0;
''')

    def test_exact_25_record_range_order_arguments_and_repeat(self):
        self.run_case(r'''
s32 i; setup_dispatch(); dispatch(0);
CHECK(events == 25 && error == 0);
for (i = 0; i < 25; i++) {
    CHECK(order[i] == i * 2 + 1 && update_calls[i] == 1 && predicate_calls[i] == 0);
    CHECK(observed_state[i] == D_800CC2D0[i].unk2D0);
    CHECK(observed_step[i] == *(u32 *)&D_800CC2D0[i].unk48);
}
CHECK(update_calls[25] == 0 && predicate_calls[25] == 0);
events = 0; dispatch(0); CHECK(events == 25 && error == 0);
for (i = 0; i < 25; i++) CHECK(update_calls[i] == 2);
return 0;
''')

    def test_gate_truth_table_and_short_circuit_calls(self):
        self.run_case(r'''
s32 active, disabled, mode, type, gate, override, result;
for (active = 0; active <= 1; active++)
for (disabled = 0; disabled <= 1; disabled++)
for (mode = 0; mode <= 1; mode++)
for (type = 3; type <= 5; type++)
for (gate = 0; gate <= 1; gate++)
for (override = 0; override <= 1; override++)
for (result = 0; result <= 1; result++) {
    s32 eligible = active && !disabled && (!mode || type == 4);
    s32 predicate = eligible && gate && !override;
    setup_dispatch();
    D_800CC2D0[0].interaction_state = active;
    D_800CC2D0[0].unk25C = disabled ? 0x200 : 0;
    D_800CC2D0[0].unk5 = type;
    D_800C3638 = gate; *(u8 *)&D_800C3654 = override;
    predicate_result[0] = result;
    dispatch(mode);
    CHECK(predicate_calls[0] == predicate);
    CHECK(update_calls[0] == (eligible && (!predicate || result)));
    CHECK(error == 0);
}
return 0;
''')

    def test_nested_pointer_and_enable_byte_gate_after_predicate(self):
        self.run_case(r'''
setup_dispatch(); D_800C3638 = 1; D_800CC2D0[0].unk2D0 = 0; dispatch(0);
CHECK(predicate_calls[0] == 1 && update_calls[0] == 0 && error == 0);
setup_dispatch(); D_800C3638 = 1; D_800CC2D0[0].unk2FA = 0; dispatch(0);
CHECK(predicate_calls[0] == 1 && update_calls[0] == 0 && error == 0);
setup_dispatch(); D_800CC2D0[0].unk2FA = 255; dispatch(0);
CHECK(update_calls[0] == 1 && error == 0);
return 0;
''')

    def test_override_reads_only_first_addressed_byte(self):
        self.run_case(r'''
setup_dispatch(); D_800C3638 = 255;
((u8 *)&D_800C3654)[0] = 0;
((u8 *)&D_800C3654)[1] = 255;
((u8 *)&D_800C3654)[2] = 255;
((u8 *)&D_800C3654)[3] = 255;
predicate_result[0] = 0; dispatch(0);
CHECK(predicate_calls[0] == 1 && update_calls[0] == 0 && error == 0);
setup_dispatch(); D_800C3638 = 255; *(u8 *)&D_800C3654 = 128;
predicate_result[0] = 0; dispatch(0);
CHECK(predicate_calls[0] == 0 && update_calls[0] == 1 && error == 0);
return 0;
''')

    def test_callback_mutates_current_nested_pointer_step_and_enable(self):
        self.run_case(r'''
setup_dispatch(); D_800C3638 = 1; mutation = 1; dispatch(0);
CHECK(observed_state[0] == (struct197 *)0x12345678);
CHECK(observed_step[0] == 0xC0F00000 && error == 0);
setup_dispatch(); D_800C3638 = 1; mutation = 2; dispatch(0);
CHECK(predicate_calls[0] == 1 && update_calls[0] == 0 && error == 0);
setup_dispatch(); D_800C3638 = 1; mutation = 3; dispatch(0);
CHECK(predicate_calls[0] == 1 && update_calls[0] == 0 && error == 0);
return 0;
''')

    def test_update_mutates_gate_and_next_actor(self):
        self.run_case(r'''
setup_dispatch(); mutation = 4; predicate_result[1] = 0; dispatch(0);
CHECK(predicate_calls[0] == 0 && update_calls[0] == 1);
CHECK(predicate_calls[1] == 1 && update_calls[1] == 0 && error == 0);
setup_dispatch(); mutation = 5; dispatch(0);
CHECK(update_calls[0] == 1 && update_calls[1] == 0 && update_calls[2] == 1);
CHECK(error == 0);
return 0;
''')

    def test_non_boolean_modes_signed_active_and_other_flag_bits(self):
        self.run_case(r'''
s32 i; setup_dispatch();
for (i = 0; i < 25; i++) {
    D_800CC2D0[i].interaction_state = -1;
    D_800CC2D0[i].unk25C = 0xFFFFFDFF;
}
dispatch(-123); CHECK(events == 25 && error == 0);
setup_dispatch(); D_800CC2D0[0].unk5 = 255; dispatch(0x7FFFFFFF);
CHECK(update_calls[0] == 0 && update_calls[1] == 1 && error == 0);
return 0;
''')

    def test_float_argument_bits_and_caller_does_not_mutate_records(self):
        self.run_case(r'''
u8 before[sizeof(D_800CC2D0)]; s32 i;
setup_dispatch();
*(u32 *)&D_800CC2D0[0].unk48 = 0x7FC12345;
*(u32 *)&D_800CC2D0[1].unk48 = 0x80000000;
for (i = 0; i < sizeof(before); i++) before[i] = ((u8 *)D_800CC2D0)[i];
dispatch(0);
CHECK(observed_step[0] == 0x7FC12345 && observed_step[1] == 0x80000000);
for (i = 0; i < sizeof(before); i++) CHECK(before[i] == ((u8 *)D_800CC2D0)[i]);
CHECK(error == 0); return 0;
''')

    def test_complete_guard_proof_is_address_setup_permutation_only(self):
        reference = (self.project / "asm/A9260.s").read_text().split(
            "glabel func_1507C22C\n", 1)[1].split("endlabel func_1507C22C", 1)[0]
        retail = [int(word, 16) for word in re.findall(
            r"/\*\s*[0-9A-Fa-f]+\s+[0-9A-Fa-f]{8}\s+([0-9A-Fa-f]{8})\s*\*/", reference)]
        with (self.project / "retail_word_patches.us.csv").open(newline="") as file:
            guards = [row for row in csv.DictReader(file)
                      if row["function"] == "func_1507C22C"]
        self.assertEqual(len(retail), 62)
        self.assertEqual([int(row["offset"], 0) for row in guards], list(range(0x28, 0x44, 4)))
        addresses = {"D_800CC2D0": 0x800CC2D0, "D_800D121C": 0x800D121C,
                     "D_800C3638": 0x800C3638, "D_800C3654": 0x800C3654}

        def relocated(word, relocation):
            kind, symbol = relocation.split(":")
            address = addresses[symbol]
            value = ((address + 0x8000) >> 16) if kind == "R_MIPS_HI16" else address
            self.assertIn(kind, ("R_MIPS_HI16", "R_MIPS_LO16"))
            return word | (value & 0xFFFF)

        original = retail[:]
        pairs = []
        for row in guards:
            self.assertEqual(row["filename"], "generated_A9260")
            self.assertEqual(row["omit"], "false")
            self.assertEqual(row["insert_after"], "")
            self.assertEqual(row["insert_after_relocations"], "")
            index = int(row["offset"], 0) // 4
            expected = relocated(int(row["expected"], 0), row["expected_relocations"])
            replacement = relocated(int(row["replacement"], 0), row["replacement_relocations"])
            self.assertEqual(replacement, retail[index])
            original[index] = expected
            pairs.append(((int(row["expected"], 0), row["expected_relocations"]),
                          (int(row["replacement"], 0), row["replacement_relocations"])))
        self.assertCountEqual([pair[0] for pair in pairs], [pair[1] for pair in pairs])

        def execute_setup(words):
            regs = [0xA5A5A5A5] * 32
            for word in words:
                opcode, rs, rt, imm = word >> 26, (word >> 21) & 31, (word >> 16) & 31, word & 0xFFFF
                if opcode == 15:
                    regs[rt] = imm << 16
                else:
                    self.assertEqual(opcode, 9)
                    self.assertEqual(rs, rt)
                    regs[rt] = (regs[rs] + (imm if imm < 0x8000 else imm - 0x10000)) & 0xFFFFFFFF
            return regs

        self.assertEqual(execute_setup(original[9:17]), execute_setup(retail[9:17]))
        self.assertEqual(original[:10], retail[:10])
        self.assertEqual(original[17:], retail[17:])
        self.assertEqual(len(b"".join(struct.pack(">I", word) for word in original)), 248)


if __name__ == "__main__":
    unittest.main()
