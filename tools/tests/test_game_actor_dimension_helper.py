import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests.test_game_oriented_record_overlap import START, TYPES


class GameActorDimensionHelperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.compiler = shutil.which("cc")
        if cls.compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.flags = ["-m32", "-O2", "-std=c99", "-ffreestanding", "-nostdlib",
                     "-static", "-fno-pie", "-no-pie", "-fno-stack-protector",
                     "-fno-strict-aliasing", "-msse2", "-mfpmath=sse", "-ffp-contract=off"]
        probe = cls.path / "probe.c"
        probe.write_text("int run(void) { return 0; }\n" + START)
        result = subprocess.run([cls.compiler, *cls.flags, str(probe), "-o",
                                 str(cls.path / "probe")], capture_output=True, text=True)
        if result.returncode:
            raise unittest.SkipTest("freestanding 32-bit compiler support is unavailable")
        try:
            result = subprocess.run([str(cls.path / "probe")], timeout=5)
        except OSError as error:
            raise unittest.SkipTest("32-bit host execution is unavailable") from error
        if result.returncode:
            raise unittest.SkipTest("32-bit host execution probe failed")
        cls.project = Path(__file__).resolve().parents[2] / "conker"
        source = (cls.project / "src/game/generated_A9260.c").read_text()
        shared = (cls.project / "include/structs.h").read_text()
        actor = re.search(r"struct struct127 \{\n.*?\n\};", shared, re.S)
        if actor is None:
            raise AssertionError("production actor layout was not found")
        forward = sorted(set(re.findall(r"\bstruct\d+\b", actor.group(0))) -
                         {"struct126", "struct127"})
        layouts = [match.group(0) for match in re.finditer(
            r"typedef struct \{\n.*?\n\} Dimension\w+A9260;", source, re.S)]
        if len(layouts) != 2:
            raise AssertionError("dimension views were not found")
        bodies = []
        for name in ("func_1507C3E0", "func_1507C370"):
            match = re.search(r"void " + name + r"\([^;{]*\{\n.*?\n\}", source, re.S)
            if match is None:
                raise AssertionError("production function not found: " + name)
            bodies.append(match.group(0))
        cls.source = TYPES + "typedef signed char s8; typedef unsigned short u16;\n" + \
            "#define NULL 0\ntypedef struct struct127 struct127;\n" + \
            "\n".join("typedef struct " + name + " " + name + ";" for name in forward) + r'''
typedef struct {
    u8 pad0[0x114];
    u16 unk114, unk116, unk118;
} struct126;
''' + actor.group(0) + "\n" + "\n".join(layouts) + r'''
f32 D_8009B688 = 257.0f;
u8 D_800BE616;
u8 D_800B85A4[256 * 0x32C];
struct127 D_800CC2D0[26];
s8 D_8008FD8C;
static DimensionStateA9260 state;
static DimensionCameraA9260 camera;
static u16 output[3];
#define actor D_800CC2D0[0]
''' + "\n".join(bodies) + r'''
static void clear_bytes(void *p, u32 size) {
    u32 i;
    for (i = 0; i < size; i++) ((u8 *)p)[i] = 0;
}
static void initialize(void) {
    clear_bytes(D_800CC2D0, sizeof(D_800CC2D0));
    clear_bytes(&state, sizeof(state));
    clear_bytes(&camera, sizeof(camera));
    clear_bytes(D_800B85A4, sizeof(D_800B85A4));
    actor.interaction_state = 1;
    actor.id = 1;
    actor.xz_scale = actor.y_scale = 1.0f;
    actor.unkE4 = 17;
    actor.unkE6 = 21;
    D_800BE616 = 0;
    D_8009B688 = 257.0f;
    D_8008FD8C = 1;
    output[0] = output[1] = output[2] = 0xA5A5;
}
static void dimensions(void) {
    func_1507C3E0(&actor, &output[0], &output[1], &output[2]);
}
static s32 equal(u16 height, u16 baseRadius, u16 radius) {
    return output[0] == height && output[1] == baseRadius && output[2] == radius;
}
'''

    def run_case(self, body):
        fixture = self.path / "dimensions.c"
        binary = self.path / "dimensions"
        fixture.write_text(self.source + "\nint run(void) {\n" + body + "\n}\n" + START)
        result = subprocess.run([self.compiler, *self.flags, str(fixture), "-o", str(binary)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([str(binary)], capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, result.stderr.decode())

    def test_production_and_local_view_offsets(self):
        self.run_case(r'''
#define OFFSET(type, field) __builtin_offsetof(type, field)
    if (sizeof(struct127) != 0x32C || OFFSET(struct127, camera) != 0x318 ||
        OFFSET(struct127, unk31C) != 0x31C || OFFSET(struct127, xz_scale) != 0x14C ||
        OFFSET(struct127, y_scale) != 0x150 || OFFSET(struct127, unk13C) != 0x13C) return 1;
    if (OFFSET(DimensionStateA9260, unk4) != 4 ||
        OFFSET(DimensionStateA9260, unk17) != 0x17 ||
        OFFSET(DimensionStateA9260, unk4E) != 0x4E ||
        OFFSET(DimensionStateA9260, unk4F) != 0x4F ||
        OFFSET(DimensionStateA9260, unk197) != 0x197 ||
        OFFSET(DimensionStateA9260, unk1A6) != 0x1A6 ||
        OFFSET(DimensionStateA9260, unk1B3) != 0x1B3) return 2;
    if (OFFSET(DimensionCameraA9260, unk73C) != 0x73C ||
        OFFSET(DimensionCameraA9260, unk95C) != 0x95C ||
        OFFSET(DimensionCameraA9260, unk960) != 0x960) return 3;
    return 0;
''')

    def test_all_subtypes_against_retail_jump_tables(self):
        rom_path = self.project / "conker.us.bin"
        if not rom_path.exists():
            self.skipTest("retail ROM is unavailable for jump-table oracle")
        rom = rom_path.read_bytes()
        targets = [0x1507C7A4] * 256
        for address, first, count in ((0x8009B4A0, 0x75, 70),
                                      (0x8009B5B8, 0x25, 47), (0x8009B674, 0, 5)):
            offset = 0x2275E0 + address - 0x80082B20
            targets[first:first + count] = struct.unpack_from(
                ">" + str(count) + "I", rom, offset)
        self.assertEqual(set(targets), {0x1507C574, 0x1507C6D4, 0x1507C6F0,
                                       0x1507C70C, 0x1507C728, 0x1507C744,
                                       0x1507C760, 0x1507C7A4})
        table = ",".join("0x%08X" % target for target in targets)
        self.run_case("static u32 targets[256] = {" + table + "};\n" + r'''
    s32 id, mode;
    u16 height, radius;
    for (mode = 0; mode < 2; mode++) {
        for (id = 0; id < 256; id++) {
            initialize(); actor.id = id; D_800BE616 = mode;
            actor.xz_scale = 2.0f; actor.y_scale = 3.0f;
            switch (targets[id]) {
                case 0x1507C574: height = 540; radius = 120; break;
                case 0x1507C6D4: height = 210; radius = 180; break;
                case 0x1507C6F0: height = 771; radius = 180; break;
                case 0x1507C70C: height = 60; radius = 45; break;
                case 0x1507C728: height = 90; radius = 30; break;
                case 0x1507C744: height = 60; radius = 30; break;
                case 0x1507C760: height = mode ? 900 : 750;
                    radius = mode ? 300 : 180; break;
                default: height = 42; radius = 17; break;
            }
            dimensions();
            if (!equal(height, radius, radius)) return 1;
        }
    }
    return 0;
''')

    def test_early_type_priority_and_scale_bypass(self):
        self.run_case(r'''
    s32 types[] = {0, 0x2D, 4, 0x2C};
    u16 heights[] = {180, 23, 126, 160}, radii[] = {60, 12, 51, 80};
    s32 i;
    for (i = 0; i < 4; i++) {
        initialize(); actor.interaction_state = types[i]; actor.unk5 = 5;
        actor.xz_scale = 2.0f; actor.y_scale = 3.0f;
        actor.unk13C = 255; D_800B85A4[255 * 0x32C] = 0x13;
        actor.camera = (struct108 *)&camera;
        camera.unk95C = 12.75f; camera.unk960 = 23.75f;
        dimensions(); if (!equal(heights[i], radii[i], radii[i])) return 1;
    }
    initialize(); actor.unk5 = 5; actor.id = 0x53;
    actor.xz_scale = 5; actor.y_scale = 7;
    dimensions(); if (!equal(42, 17, 17)) return 2;
    initialize(); actor.interaction_state = 0x2E; actor.id = 0x36;
    dimensions(); if (!equal(257, 90, 90)) return 3;
    return 0;
''')

    def test_signed_halfword_dimensions(self):
        self.run_case(r'''
    initialize(); actor.interaction_state = 4; actor.unkE4 = -7; actor.unkE6 = -11;
    dimensions(); if (!equal((u16)-66, (u16)-21, (u16)-21)) return 1;
    actor.interaction_state = 1; actor.id = 5;
    dimensions(); if (!equal((u16)-22, (u16)-7, (u16)-7)) return 2;
    actor.unk5 = 5;
    dimensions(); if (!equal((u16)-22, (u16)-7, (u16)-7)) return 3;
    return 0;
''')

    def test_state_mode_precedence_over_water_and_extra_height(self):
        self.run_case(r'''
    initialize(); actor.unk31C = (struct126 *)&state;
    state.unk4 = -1; state.unk17 = 1; state.unk1A6 = 123; actor.in_water = 1;
    dimensions(); if (!equal(80, 60, 60)) return 1;
    state.unk4 = 0;
    dimensions(); if (!equal(300, 70, 70)) return 2;
    state.unk17 = 0;
    dimensions(); if (!equal(180, 90, 90)) return 3;
    actor.in_water = 0;
    dimensions(); if (!equal(303, 60, 60)) return 4;
    return 0;
''')

    def test_each_widening_trigger_and_null_camera(self):
        self.run_case(r'''
    initialize(); actor.unk31C = (struct126 *)&state;
    dimensions(); if (!equal(180, 60, 60)) return 1;
    actor.camera = (struct108 *)&camera; camera.unk73C = -1;
    dimensions(); if (!equal(180, 120, 120)) return 2;
    camera.unk73C = 0; state.unk197 = 1;
    dimensions(); if (!equal(180, 120, 120)) return 3;
    state.unk197 = 0; state.unk1B3 = 1;
    dimensions(); if (!equal(180, 120, 120)) return 4;
    state.unk17 = 1;
    dimensions(); if (!equal(300, 70, 70)) return 5;
    return 0;
''')

    def test_extra_height_is_unsigned_halfword(self):
        self.run_case(r'''
    initialize(); actor.unk31C = (struct126 *)&state; state.unk1A6 = 65535;
    dimensions(); if (!equal(179, 60, 60)) return 1;
    return 0;
''')

    def test_locomotion_override_threshold_and_low_nibble(self):
        self.run_case(r'''
    union { u32 bits; f32 value; } nan = {0x7FC00000};
    initialize(); actor.unk31C = (struct126 *)&state;
    state.unk4 = 1; state.unk4E = 0xF1;
    actor.xz_velocity = 39.999f;
    dimensions(); if (!equal(500, 110, 110)) return 1;
    actor.xz_velocity = 40.0f;
    dimensions(); if (!equal(80, 60, 60)) return 2;
    actor.xz_velocity = nan.value;
    dimensions(); if (!equal(80, 60, 60)) return 3;
    actor.xz_velocity = -1; state.unk4F = 1;
    dimensions(); if (!equal(80, 60, 60)) return 4;
    state.unk4F = 0; state.unk4E = 2;
    dimensions(); if (!equal(80, 60, 60)) return 5;
    return 0;
''')

    def test_scaled_attachment_preserves_distinct_base_radius(self):
        self.run_case(r'''
    initialize(); actor.id = 0x25; actor.unk13C = 101;
    D_800B85A4[101 * 0x32C] = 0x13;
    actor.xz_scale = 2; actor.y_scale = 3;
    dimensions(); if (!equal(1110, 180, 660)) return 1;
    return 0;
''')

    def test_unscaled_attachment_and_default_record(self):
        self.run_case(r'''
    initialize(); actor.id = 0xAC; actor.unk13C = 255;
    D_800B85A4[255 * 0x32C] = 0x13;
    actor.xz_scale = 2; actor.y_scale = 3;
    dimensions(); if (!equal(390, 30, 270)) return 1;
    actor.id = 5;
    dimensions(); if (!equal(342, 17, 257)) return 2;
    return 0;
''')

    def test_attachment_threshold_and_type_gate(self):
        self.run_case(r'''
    initialize(); actor.id = 0x25; actor.unk13C = 100;
    D_800B85A4[100 * 0x32C] = 0x13;
    dimensions(); if (!equal(70, 90, 90)) return 1;
    actor.unk13C = 101; D_800B85A4[101 * 0x32C] = 0x12;
    dimensions(); if (!equal(70, 90, 90)) return 2;
    D_800B85A4[101 * 0x32C] = 0x13;
    dimensions(); if (!equal(170, 90, 210)) return 3;
    return 0;
''')

    def test_null_outputs_and_alias_publication_order(self):
        self.run_case(r'''
    s32 mask; u16 shared;
    initialize(); actor.id = 0x25; actor.unk13C = 101;
    D_800B85A4[101 * 0x32C] = 0x13;
    for (mask = 0; mask < 8; mask++) {
        output[0] = output[1] = output[2] = 0xA5A5;
        func_1507C3E0(&actor, mask & 1 ? &output[0] : NULL,
                     mask & 2 ? &output[1] : NULL, mask & 4 ? &output[2] : NULL);
        if (output[0] != (mask & 1 ? 170 : 0xA5A5) ||
            output[1] != (mask & 2 ? 90 : 0xA5A5) ||
            output[2] != (mask & 4 ? 210 : 0xA5A5)) return 1;
    }
    shared = 0; func_1507C3E0(&actor, &shared, &shared, &shared);
    if (shared != 210) return 2;
    func_1507C3E0(&actor, &shared, &shared, NULL);
    if (shared != 90) return 3;
    return 0;
''')

    def test_fractional_negative_scaling_and_low_halfword_wrap(self):
        self.run_case(r'''
    initialize(); actor.id = 0x25; actor.xz_scale = -0.125f; actor.y_scale = -0.125f;
    dimensions(); if (!equal((u16)-8, (u16)-11, (u16)-11)) return 1;
    actor.xz_scale = 1000.0f; actor.y_scale = 1000.0f;
    dimensions(); if (!equal((u16)70000, (u16)90000, (u16)90000)) return 2;
    return 0;
''')

    def test_height_constant_is_loaded_not_hardcoded(self):
        self.run_case(r'''
    initialize(); actor.id = 0x36; D_8009B688 = 123.75f; actor.y_scale = 2;
    dimensions(); if (!equal(247, 90, 90)) return 1;
    return 0;
''')

    def test_real_refresh_wrapper_skips_null_and_obeys_count(self):
        self.run_case(r'''
    DimensionStateA9260 other;
    struct126 *first = (struct126 *)&state, *last = (struct126 *)&other;
    initialize(); clear_bytes(&other, sizeof(other));
    actor.unk31C = first;
    D_800CC2D0[1].interaction_state = 0;
    D_800CC2D0[2].interaction_state = 0;
    D_800CC2D0[2].unk31C = last;
    first->unk114 = first->unk116 = first->unk118 = 0xA5A5;
    last->unk114 = last->unk116 = last->unk118 = 0xA5A5;
    D_8008FD8C = 2; func_1507C370();
    if (first->unk114 != 180 || first->unk116 != 60 || first->unk118 != 60) return 1;
    if (last->unk114 != 0xA5A5 || last->unk116 != 0xA5A5 || last->unk118 != 0xA5A5) return 2;
    D_8008FD8C = 3; func_1507C370();
    if (last->unk114 != 180 || last->unk116 != 60 || last->unk118 != 60) return 3;
    return 0;
''')

    def test_real_refresh_wrapper_nonpositive_count(self):
        self.run_case(r'''
    struct126 *outputs = (struct126 *)&state;
    initialize(); actor.unk31C = outputs;
    outputs->unk114 = outputs->unk116 = outputs->unk118 = 0xA5A5;
    D_8008FD8C = 0; func_1507C370();
    D_8008FD8C = -1; func_1507C370();
    if (outputs->unk114 != 0xA5A5 || outputs->unk116 != 0xA5A5 ||
        outputs->unk118 != 0xA5A5) return 1;
    return 0;
''')


if __name__ == "__main__":
    unittest.main()
