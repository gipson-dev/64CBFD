import re
import unittest
from pathlib import Path

from tools.tests import test_game_highest_height_query as highest


class GameCachedHeightDispatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        highest.GameHighestHeightQueryTests.setUpClass.__func__(cls)
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        layout = re.search(r"typedef struct HeightResult71820 \{\n.*?\n\} HeightResult71820;",
                           source, re.S)
        bodies = []
        for name in ["func_15045780", "func_15047004", "func_15045800"]:
            body = re.search(r"s32 " + name + r"\([^;{]*\{\n.*?\n\}", source, re.S)
            if body is None:
                raise AssertionError("cached height definition is missing: " + name)
            bodies.append(body.group(0))
        if layout is None:
            raise AssertionError("height result layout is missing")
        cls.source = highest.TYPES + "typedef unsigned short u16;\n#define NULL ((void *)0)\n" + \
                     layout.group(0) + r'''
static f32 position[3], threshold, cached_height;
static HeightResult71820 output;
static s32 geometry_calls, producer_calls, query_calls, error, mutation;
static s32 geometry_return, query_return;
static u16 expected_selector;
static s32 *secondary_pointer;
static u32 bits(f32 value) {
    union { f32 value; u32 bits; } number;
    number.value = value; return number.bits;
}
static f32 from_bits(u32 value) {
    union { f32 value; u32 bits; } number;
    number.bits = value; return number.value;
}
s32 func_150A3FC4(f32 x, f32 z, void *triangle, s16 *vertices, f32 *height) {
    if (geometry_calls || producer_calls || query_calls || x != position[0] ||
        z != position[2] || triangle != NULL || vertices != output.vertices) error = 1;
    geometry_calls++;
    *height = cached_height;
    if (mutation == 1) { position[1] = 20; output.flags = 0x80; }
    if (mutation == 2) { position[1] = -10; output.flags = 0x82; }
    if (mutation == 3) { position[0] = -12.75f; position[2] = 23.75f; output.metadata = 123; }
    return geometry_return;
}
void func_15045714(f32 *p, u16 selector, s32 *primary, s32 *secondary) {
    if (producer_calls || query_calls || p != position || selector != expected_selector ||
        primary != secondary + 1) error = 2;
    if (mutation == 3 && (p[0] != -12.75f || p[2] != 23.75f || output.metadata != 123)) error = 3;
    *secondary = 2; *primary = 3; secondary_pointer = secondary; producer_calls++;
}
s32 func_15045F8C(f32 *p, f32 bound, s32 *counts, HeightResult71820 *result) {
    if (producer_calls != 1 || query_calls || p != position || bits(bound) != bits(threshold) ||
        counts != secondary_pointer || counts[0] != 2 || counts[1] != 3 ||
        result != &output) error = 4;
    query_calls++; result->metadata = 0x12345678; return query_return;
}
''' + "\n".join(bodies) + r'''
static void initialize(void) {
    s32 byte;
    for (byte = 0; byte < 36; byte++) ((u8 *)&output)[byte] = 0xA5;
    position[0] = 1; position[1] = 10; position[2] = 2; threshold = 0; cached_height = 5;
    geometry_calls = producer_calls = query_calls = error = mutation = 0;
    geometry_return = query_return = 1; expected_selector = 0xFFFF;
}
static s32 cache_only_changed_height_and_flags(u8 *before) {
    s32 byte;
    for (byte = 4; byte < 36; byte++) if (byte != 0x1C)
        if (before[byte] != ((u8 *)&output)[byte]) return 0;
    return 1;
}
static void snapshot(u8 *before) {
    s32 byte;
    for (byte = 0; byte < 36; byte++) before[byte] = ((u8 *)&output)[byte];
}
static s32 unchanged(u8 *before) {
    s32 byte;
    for (byte = 0; byte < 36; byte++)
        if (before[byte] != ((u8 *)&output)[byte]) return 0;
    return 1;
}
#define CHECK(condition) do { if (!(condition)) return __LINE__ % 254 + 1; } while (0)
'''

    run_case = highest.GameHighestHeightQueryTests.run_case

    def test_guest_layout(self):
        self.run_case(r'''
CHECK(sizeof(HeightResult71820) == 36);
CHECK(__builtin_offsetof(HeightResult71820, vertices) == 4);
CHECK(__builtin_offsetof(HeightResult71820, flags) == 0x1C);
''')

    def test_disabled_cache_never_calls_geometry_or_changes_result(self):
        self.run_case(r'''
s32 flag; u8 before[36];
for (flag = 0; flag < 256; flag++) if (!(flag & 4)) {
    initialize(); output.flags = flag; snapshot(before);
    CHECK(func_15047004(position, threshold, &output) == 0);
    CHECK(!geometry_calls && !producer_calls && !query_calls && unchanged(before));
}
''')

    def test_missing_triangle_leaves_every_enabled_flag_and_result_byte(self):
        self.run_case(r'''
s32 flag; u8 before[36];
for (flag = 0; flag < 256; flag++) if (flag & 4) {
    initialize(); output.flags = flag; geometry_return = 0; snapshot(before);
    CHECK(func_15047004(position, threshold, &output) == 0);
    CHECK(geometry_calls == 1 && !producer_calls && !query_calls && !error && unchanged(before));
}
''')

    def test_cache_acceptance_only_publishes_height_and_sets_bit2(self):
        self.run_case(r'''
s32 flag; u8 before[36];
for (flag = 0; flag < 256; flag++) if (flag & 4) {
    initialize(); output.flags = flag; snapshot(before);
    CHECK(func_15047004(position, threshold, &output) == 2);
    CHECK(geometry_calls == 1 && !error && output.height == cached_height);
    CHECK(output.flags == (flag | 2) && cache_only_changed_height_and_flags(before));
}
''')

    def test_out_of_range_or_nan_height_returns_one_without_publication(self):
        self.run_case(r'''
s32 kind; u8 before[36];
for (kind = 0; kind < 5; kind++) {
    initialize(); output.flags = 6;
    if (kind == 0) threshold = 6;
    if (kind == 1) cached_height = 11;
    if (kind == 2) threshold = from_bits(0x7FC00000);
    if (kind == 3) cached_height = from_bits(0x7FC00000);
    if (kind == 4) position[1] = from_bits(0x7FC00000);
    snapshot(before);
    CHECK(func_15047004(position, threshold, &output) == 1);
    CHECK(geometry_calls == 1 && !error && unchanged(before));
}
''')

    def test_inclusive_bounds_signed_zero_and_infinity(self):
        self.run_case(r'''
s32 kind;
for (kind = 0; kind < 5; kind++) {
    initialize();
    if (kind == 0) threshold = cached_height;
    if (kind == 1) position[1] = cached_height;
    if (kind == 2) { threshold = 0; cached_height = from_bits(0x80000000); position[1] = 0; }
    if (kind == 3) { threshold = from_bits(0x7F800000); cached_height = threshold; position[1] = threshold; }
    if (kind == 4) { threshold = from_bits(0xFF800000); cached_height = threshold; position[1] = threshold; }
    CHECK(func_15047004(position, threshold, &output) == 2);
    CHECK(bits(output.height) == bits(cached_height) && !error);
}
''')

    def test_helper_mutations_reload_y_and_flags_without_rechecking_cache_gate(self):
        self.run_case(r'''
initialize(); output.flags = 4; position[1] = 0; mutation = 1;
CHECK(func_15047004(position, threshold, &output) == 2);
CHECK(output.flags == 0x82 && output.height == 5 && !error);
initialize(); output.flags = 4; mutation = 2;
CHECK(func_15047004(position, threshold, &output) == 1);
CHECK(output.flags == 0x82 && !error);
''')

    def test_position_can_alias_result_height_during_publication(self):
        self.run_case(r'''
f32 *aliased;
initialize(); aliased = (f32 *)&output;
aliased[0] = 1; aliased[1] = 10; aliased[2] = 2;
/* The mock checks against position, so mirror only its argument values. */
position[0] = 1; position[2] = 2;
CHECK(func_15047004(aliased, output.height, &output) == 2);
CHECK(output.height == 5 && (output.flags & 2) && !error);
''')

    def test_dispatch_maps_cached_statuses_without_fallback(self):
        self.run_case(r'''
initialize(); output.flags = 4;
CHECK(func_15045800(position, expected_selector, threshold, &output) == 1);
CHECK(geometry_calls == 1 && !producer_calls && !query_calls && !error);
initialize(); output.flags = 6; threshold = 6;
CHECK(func_15045800(position, expected_selector, threshold, &output) == 0);
CHECK(geometry_calls == 1 && !producer_calls && !query_calls && output.flags == 6 && !error);
''')

    def test_missing_cache_dispatch_forwards_raw_fallback_returns(self):
        self.run_case(r'''
s32 i; s32 values[] = {-9, 0, 1, 17, 0x12345678};
for (i = 0; i < 5; i++) {
    initialize(); output.flags = 4; geometry_return = 0; query_return = values[i];
    CHECK(func_15045800(position, expected_selector, threshold, &output) == values[i]);
    CHECK(geometry_calls == 1 && producer_calls == 1 && query_calls == 1 && !error);
}
''')

    def test_disabled_cache_dispatch_preserves_all_halfword_selectors(self):
        self.run_case(r'''
s32 selector;
for (selector = 0; selector <= 65535; selector++) {
    initialize(); output.flags = 2; expected_selector = selector; threshold = from_bits(0x80000000);
    CHECK(func_15045800(position, (u16)selector, threshold, &output) == 1);
    CHECK(!geometry_calls && producer_calls == 1 && query_calls == 1 && !error);
}
''')

    def test_failed_geometry_mutations_reach_fallback_and_early_reject(self):
        self.run_case(r'''
initialize(); geometry_return = 0; mutation = 3;
CHECK(func_15045800(position, expected_selector, threshold, &output) == 1);
CHECK(geometry_calls == 1 && producer_calls == 1 && query_calls == 1 && !error);
initialize(); geometry_return = 0; mutation = 2;
CHECK(func_15045800(position, expected_selector, threshold, &output) == 0);
CHECK(geometry_calls == 1 && !producer_calls && !query_calls && output.flags == 0x80 && !error);
''')
