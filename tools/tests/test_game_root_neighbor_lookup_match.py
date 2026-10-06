"""Direct nearest-node lookup match, with the ray helper kept opaque."""

import csv
import itertools
import math
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_root_neighbor_lookup_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_record_neighbor_visit_match import read
from tools.tests.test_game_table_range_loader import STACK, native
from tools.tests.game_animation_timeline_oracle import bits, floating, signed


ENTRY = screen.ENTRY
COUNT, SEED, GLOBAL, RESULT, LIMIT, RAY = (screen.SYMBOLS[name] for name in
    ('D_80087290', 'D_8008729C', 'D_800D2350', 'D_800D2354', 'D_8009D9CC', 'func_15086D94'))
TABLE, ALTERNATE = 0x90000, 0xA0000


def narrow(value, size):
    value &= (1 << size) - 1
    return value - (1 << size) if value & (1 << (size - 1)) else value


def case_memory(seed=255, count=4, pattern=0):
    memory = {STACK + i: 0xA5 for i in range(-0x2000, 0x100)}
    for base in (TABLE, ALTERNATE):
        memory.update({base + i: 0xA5 for i in range(512 * 16)})
        for i in range(512):
            point = base + i * 16
            for offset, value in ((0, (i * 7 + pattern * 5) % 51 - 25),
                                  (2, (i * 3 + pattern) % 31 - 15),
                                  (4, (i * 11 + pattern * 7) % 61 - 30)):
                put(memory, point + offset, value, 2)
            put(memory, point + 6, i % 3, 1)
            put(memory, point + 14, i % 2, 1)
    for address, value, size in ((COUNT, count, 2), (SEED, seed, 1), (GLOBAL, TABLE, 4),
                                 (RESULT, 0x12345678, 4), (LIMIT, bits(100000000.0), 4)):
        put(memory, address, value, size)
    return memory


def external(memory):
    return {address: value for address, value in memory.items()
            if not STACK - 0x2000 <= address < STACK + 0x100}


def external_writes(model):
    return [event for event in model.events if event[0] == 'W'
            and not STACK - 0x2000 <= event[1] < STACK + 0x100]


def mutations(mode):
    entries = ((1, COUNT, 0, 2), (2, COUNT, 6, 2), (4, GLOBAL, ALTERNATE, 4),
               (8, TABLE + 16, 30000, 2), (16, SEED, 7, 1),
               (32, LIMIT, bits(-1.0), 4), (64, RESULT, 0xABCDEF01, 4),
               (128, TABLE + 16 + 6, 2, 1), (256, TABLE + 16 + 14, 1, 1),
               (512, TABLE, -30000, 2))
    return [(address, value, size) for bit, address, value, size in entries if mode & bit]


def reference(initial, coordinates=(0.0, 0.0, 0.0), mode=0, band=-1,
              responses=(-1.0,), mutation=0):
    memory, calls, writes = dict(initial), [], []
    x, y, z = [floating(bits(value)) for value in coordinates]
    mode, band = narrow(mode, 8), narrow(band, 8)
    minimum = floating(read(memory, LIMIT, 4))

    def store(address, value, size):
        value &= (1 << (size * 8)) - 1
        put(memory, address, value, size)
        writes.append(('W', address, size, value))

    def coordinates_at(identity):
        pointer = read(memory, GLOBAL, 4) + identity * 16
        return [floating(bits(narrow(read(memory, pointer + offset, 2), 16) - axis))
                for offset, axis in zip((0, 2, 4), (x, y, z))]

    def distance_of(delta):
        squares = [floating(bits(value * value)) for value in delta]
        return floating(bits(floating(bits(squares[0] + squares[1])) + squares[2]))

    def ray(delta):
        index = len(calls)
        calls.append((RAY, bits(x), bits(y), bits(z), bits(delta[0]), bits(delta[2])))
        if not index:
            for address, value, size in mutations(mutation):
                store(address, value, size)
        return floating(bits(responses[index % len(responses)])) < 0.0

    seed = read(memory, SEED, 1)
    if seed != 255:
        delta = coordinates_at(seed)
        if mode or ray(delta):
            minimum = floating(bits(distance_of(delta) + 10.0))
        store(SEED, 255, 1)
    best, identity = 255, 0
    while identity < narrow(read(memory, COUNT, 2), 16):
        pointer = read(memory, GLOBAL, 4) + identity * 16
        if (read(memory, pointer + 6, 1) == band or band == -1) and (
                read(memory, pointer + 14, 1) == mode or mode == -1):
            delta = coordinates_at(identity)
            distance = distance_of(delta)
            if distance < minimum and (mode or ray(delta)):
                minimum, best = distance, identity
        identity += 1
    assert math.isfinite(minimum) and minimum >= 0
    store(RESULT, math.trunc(floating(bits(math.sqrt(minimum)))), 4)
    return memory, calls, writes, best


class RootOracle(TriangleOracle):
    def __init__(self, words, memory, coordinates=(0.0, 0.0, 0.0), mode=0, band=-1,
                 responses=(-1.0,), mutation=0, phase=0):
        super().__init__(words, memory, entry=ENTRY, phase=phase,
                         arguments=(0, 0, bits(coordinates[2]), mode, band))
        self.f[12], self.f[14] = bits(coordinates[0]), bits(coordinates[1])
        self.responses, self.mutation = responses, mutation

    def execute(self, word):
        op, rs, rt, rd, fd, fn = word >> 26, word >> 21 & 31, word >> 16 & 31, word >> 11 & 31, word >> 6 & 31, word & 63
        if op == 32:
            offset = narrow(word, 16)
            self.r[rt] = narrow(self.get((self.r[rs] + offset) & 0xFFFFFFFF, 1), 8) & 0xFFFFFFFF
        elif op == 17 and rs == 16 and fn == 4:
            value = floating(self.f[rd])
            assert math.isfinite(value) and value >= 0
            self.f[fd] = bits(math.sqrt(value))
        elif op == 17 and rs == 16 and fn == 13:
            value = floating(self.f[rd])
            assert math.isfinite(value) and -2147483648 <= value < 2147483648
            self.f[fd] = math.trunc(value) & 0xFFFFFFFF
        else:
            super().execute(word)

    def record_call(self, target):
        assert target == RAY
        self.calls.append((target, self.f[12], self.f[14], self.r[6], self.r[7],
                           self.get(self.r[29] + 16, 4)))

    def hook(self, target):
        assert target == RAY
        if len(self.calls) == 1:
            for address, value, size in mutations(self.mutation):
                self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.f[0] = bits(self.responses[(len(self.calls) - 1) % len(self.responses)])


class GameRootNeighborLookupMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-root-neighbor-lookup-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        _, cls.baseline = screen.compile_candidate(cls.root, cls.output, 'baseline', screen.BASELINE)
        cls.retail = list(struct.unpack_from('>168I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0xB32A8))
        cls.coverage, cls.cases = set(), 0
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def check_case(self, memory, coordinates=(0.0, 0.0, 0.0), mode=0, band=-1,
                   responses=(-1.0,), mutation=0, phase=0):
        wanted, calls, writes, result = reference(memory, coordinates, mode, band, responses, mutation)
        for words in (self.retail, self.words, self.baseline):
            model = RootOracle(words, memory, coordinates, mode, band, responses, mutation, phase).run()
            self.assertEqual(model.r[2], result)
            self.assertEqual(model.calls, calls)
            self.assertEqual(external_writes(model), writes)
            self.assertEqual(external(model.memory), external(wanted))
            if words is self.retail:
                type(self).coverage.update(model.visits)
        type(self).cases += 1
        return wanted, result

    def test_bounded_filters_cached_seeds_and_ray_results(self):
        for seed, count, mode, band, response, phase in itertools.product(
                (255, 0, 2, 254), (0, 1, 4, 8), (-1, 0, 1, 2), (-1, 0, 1, 2),
                (-1.0, 0.0, 1.0), (0, 8)):
            self.check_case(case_memory(seed, count, pattern=count % 4),
                            (1.25, -2.75, 3.5), mode, band, (response,), phase=phase)

    def test_signed_byte_arguments_and_signed_count(self):
        for count, mode, band, phase in itertools.product(
                (-32768, -1, 0, 1, 8), (-129, -128, 127, 128, 255, 256, 0x1234AB00),
                (-129, -128, 127, 128, 255, 256, 0x1234ABFF), (0, 8)):
            self.check_case(case_memory(255, count), mode=mode, band=band, phase=phase)

    def test_helper_mutations_keep_saved_distances_and_refresh_future_globals(self):
        modes = (*range(64), 64, 128, 256, 512, 127, 255, 511, 1023)
        for mutation, seed, responses, phase in itertools.product(
                modes, (255, 0), ((-1.0,), (0.0,), (-1.0, 0.0, 1.0)), (0, 8)):
            self.check_case(case_memory(seed, 4), mode=0, band=-1,
                            responses=responses, mutation=mutation, phase=phase)

    def test_cached_bound_is_not_a_winner_and_has_ten_unit_slack(self):
        memory = case_memory(0, 0)
        for offset in (0, 2, 4):
            put(memory, TABLE + offset, 0, 2)
        wanted, result = self.check_case(memory, mode=-1)
        self.assertEqual((result, read(wanted, RESULT, 4), read(wanted, SEED, 1)), (255, 3, 255))
        put(memory, COUNT, 1, 2)
        wanted, result = self.check_case(memory, mode=-1)
        self.assertEqual((result, read(wanted, RESULT, 4)), (0, 0))

    def test_equal_distances_keep_first_and_wide_ids_are_not_narrowed(self):
        for count, winner, phase in itertools.product((255, 256, 257, 512), (0, 254, 255, 256, 511), (0, 8)):
            if winner >= count:
                continue
            memory = case_memory(255, count)
            for i in range(count):
                for offset in (0, 2, 4):
                    put(memory, TABLE + i * 16 + offset, 100, 2)
            for offset in (0, 2, 4):
                put(memory, TABLE + winner * 16 + offset, 0, 2)
            wanted, result = self.check_case(memory, mode=-1, phase=phase)
            self.assertEqual((result, read(wanted, RESULT, 4)), (winner, 0))
        memory = case_memory(255, 2)
        for i in range(2):
            for offset in (0, 2, 4):
                put(memory, TABLE + i * 16 + offset, 0, 2)
        self.assertEqual(self.check_case(memory, mode=-1)[1], 0)

    def test_unordered_and_signed_zero_ray_results(self):
        for response, phase in itertools.product((math.nan, math.inf, -math.inf, -0.0, 0.0), (0, 8)):
            self.check_case(case_memory(0, 8), responses=(response,), phase=phase)
        for coordinate, phase in itertools.product((math.nan, math.inf, -math.inf), (0, 8)):
            self.check_case(case_memory(255, 4), (coordinate, 0.0, 0.0), mode=-1, phase=phase)

    def test_unsigned_record_fields_do_not_match_negative_signed_filters(self):
        for field, mode, band, phase in itertools.product(
                (0, 127, 128, 255), (-1, -128, 127, 128, 255, 256),
                (-1, -128, 127, 128, 255, 256), (0, 8)):
            memory = case_memory(255, 1)
            put(memory, TABLE + 6, field, 1)
            put(memory, TABLE + 14, field, 1)
            self.check_case(memory, mode=mode, band=band, phase=phase)

    def test_finite_minimum_distance_gates_and_guarded_empty_table(self):
        for minimum, coordinate, phase in itertools.product(
                (0.0, 1.0, 10.0, 100000000.0),
                ((0.0, 0.0, 0.0), (0.5, 0.5, 0.5), (-32768.0, 32767.0, -1.0),
                 (math.nan, 0.0, 0.0), (math.inf, 0.0, 0.0)), (0, 8)):
            memory = case_memory(255, 4)
            put(memory, LIMIT, bits(minimum))
            self.check_case(memory, coordinate, mode=-1, phase=phase)
        for phase in (0, 8):
            memory = case_memory(0, 0)
            for offset, value in ((0, -32768), (2, 32767), (4, -32768)):
                put(memory, TABLE + offset, value, 2)
            self.check_case(memory, mode=-1, phase=phase)
        for count, phase in itertools.product((-32768, -1, 0, -2), (0, 8)):
            memory = case_memory(255, count)
            put(memory, GLOBAL, 0)
            self.check_case(memory, phase=phase)

    def test_native_1536_full_record_and_global_footprints(self):
        rows = []
        for seed, count, mode, band, pattern, response in itertools.product(
                (255, 0, 2, 254), (0, 1, 4, 8), (-1, 0, 1, 2), (-1, 0, 1, 2),
                (0, 3), (-1.0, 0.0, 1.0)):
            wanted, calls, _, result = reference(case_memory(seed, count, pattern),
                (1.25, -2.75, 3.5), mode, band, (response,))
            digest = 2166136261
            for call in calls:
                for value in call:
                    digest = ((digest ^ value) * 16777619) & 0xFFFFFFFF
            rows.append('{%s,0x%08X,%d,%d,0x%08X}' % (
                ','.join(map(str, (seed, count, mode, band, pattern))), bits(response), result,
                read(wanted, RESULT, 4), digest))
        self.assertEqual(len(rows), 1536)
        source = (self.root / 'conker/src/game/generated_B3020.c').read_text()
        body = re.search(r's32 func_15085DF8\([^;{]*\{\n.*?\n\}', source, re.S).group()
        self.assertEqual(body, screen.SELECTED)
        self.fixture = '''typedef unsigned char u8;typedef signed char s8;
typedef short s16;typedef int s32;typedef unsigned int u32;typedef float f32;
''' + screen.DECLARATIONS + r'''
static union {u32 align;u8 bytes[8192];} storage;
s16 D_80087290;u8 D_8008729C;u8 *D_800D2350;s32 D_800D2354;f32 D_8009D9CC;
static u32 digest,response;
static f32 number(u32 word) {union {u32 u;f32 f;} v;v.u=word;return v.f;}
static u32 word(f32 value) {union {u32 u;f32 f;} v;v.f=value;return v.u;}
f32 sqrtf(f32 value) {f32 result;__asm__("sqrtss %1,%0":"=x"(result):"x"(value));return result;}
static void logWord(u32 value) {digest=(digest^value)*16777619;}
f32 func_15086D94(f32 x,f32 y,f32 z,f32 dx,f32 dz) {
 logWord(0x15086D94);logWord(word(x));logWord(word(y));logWord(word(z));
 logWord(word(dx));logWord(word(dz));return number(response);
}
''' + body + r'''
static const struct {int seed,count,mode,band,pattern;u32 response;int result,distance;u32 digest;} cases[]={
''' + ',\n'.join(rows) + '\n};\n'
        self.run_host(r'''
static u8 before[8192];int c,i;u8 *p;
for(c=0;c<1536;c++) {
 for(i=0;i<8192;i++) storage.bytes[i]=0xA5;
 for(i=0;i<512;i++) {
  p=storage.bytes+i*16;
  *(s16 *)(p+0)=(i*7+cases[c].pattern*5)%51-25;
  *(s16 *)(p+2)=(i*3+cases[c].pattern)%31-15;
  *(s16 *)(p+4)=(i*11+cases[c].pattern*7)%61-30;
  p[6]=i%3;p[14]=i%2;
 }
 for(i=0;i<8192;i++) before[i]=storage.bytes[i];
 D_80087290=cases[c].count;D_8008729C=cases[c].seed;D_800D2350=storage.bytes;
 D_800D2354=0x12345678;D_8009D9CC=100000000.0f;
 digest=2166136261;response=cases[c].response;
 if(func_15085DF8(1.25f,-2.75f,3.5f,cases[c].mode,cases[c].band)!=cases[c].result) return 1;
 if(digest!=cases[c].digest || D_800D2354!=cases[c].distance || D_8008729C!=255) return 2;
 if(D_80087290!=cases[c].count || D_800D2350!=storage.bytes || word(D_8009D9CC)!=0x4CBEBC20) return 3;
 for(i=0;i<8192;i++) if(before[i]!=storage.bytes[i]) return 4;
}
''')

    def test_negative_controls_reject_seed_reuse_ties_and_byte_winners(self):
        for name, body, memory in (
                ('missing-seed-clear', screen.SELECTED.replace('        D_8008729C = 0xFF;\n', ''), case_memory(0, 4)),
                ('inclusive-distance', screen.SELECTED.replace('distance < minimum', 'distance <= minimum'), case_memory(255, 2)),
                ('narrowed-winner', screen.SELECTED.replace('best = i;', 'best = (u8)i;'), case_memory(255, 257))):
            self.assertNotEqual(body, screen.SELECTED)
            if name == 'inclusive-distance':
                for i in (0, 1):
                    for offset in (0, 2, 4):
                        put(memory, TABLE + i * 16 + offset, 0, 2)
            if name == 'narrowed-winner':
                for i in range(257):
                    for offset in (0, 2, 4):
                        put(memory, TABLE + i * 16 + offset, 100 if i != 256 else 0, 2)
            record, words = screen.compile_candidate(self.root, self.output, name, body)
            self.assertEqual(record['diagnostics'], '')
            wanted = RootOracle(self.retail, memory, mode=-1).run()
            control = RootOracle(words, memory, mode=-1).run()
            self.assertNotEqual((control.r[2], control.calls, external(control.memory)),
                                (wanted.r[2], wanted.calls, external(wanted.memory)), name)

    def test_zz_reachable_word_coverage_and_annulled_retail_delays(self):
        # These second checks cannot be taken after the first check accepted nonzero.
        unreachable = {0x15085EC4, 0x15085FEC}
        self.assertEqual(self.coverage & set(range(ENTRY, ENTRY + 168 * 4, 4)),
                         set(range(ENTRY, ENTRY + 168 * 4, 4)) - unreachable)

    def test_compiler_inventory_and_complete_direct_match(self):
        forms = screen.candidates()
        self.assertEqual((len(forms), len(dict(forms))), (35, 35))
        self.assertEqual(screen.SELECTED, dict(forms)['inline-node-addresses'])
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences'],
                          self.record['diagnostics']), (168, 0x80, 0, ''))
        self.assertEqual(self.words, self.retail)
        for name, expected in (('signed-byte-arguments', (171, 0x90, 168)),
                               ('word-shift', (168, 0x88, 10))):
            record, _ = screen.compile_candidate(self.root, self.output, name, dict(forms)[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')
        with self.assertRaises(ValueError):
            screen.inline_nodes('void missing_source(void) {}')

    def test_production_slot_and_ray_placeholder_abi(self):
        source = (self.root / 'conker/src/game/generated_B3020.c').read_text()
        body = re.search(r's32 func_15085DF8\([^;{]*\{\n.*?\n\}', source, re.S).group()
        self.assertEqual(body, screen.SELECTED)
        self.assertIn('f32 func_15086D94(f32 x, f32 y, f32 z, f32 dx, f32 dz) {\n    return 0.0f;\n}', source)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                     'mips-linux-gnu-objdump')
        self.assertEqual(functions['func_15085DF8'], self.retail)
        self.assertEqual((addresses['func_15085DF8'], addresses['func_15086098']), (ENTRY, 0x15086098))
        self.assertNotIn('__retail_overflow_func_15085DF8', functions)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse(any(row['function'] == 'func_15085DF8' for row in csv.DictReader(stream)))

    def test_ray_placeholder_has_float_result_and_four_argument_homes(self):
        functions, _, _ = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                             'mips-linux-gnu-objdump')
        prefix = [0xE7AC0000, 0xE7AE0004, 0xAFA60008, 0xAFA7000C,
                  0x44800000, 0, 0x03E00008, 0]
        self.assertEqual(functions['func_15086D94'], prefix + [0] * (207 - len(prefix)))
        for phase in (0, 8):
            model = TriangleOracle(prefix, case_memory(), phase=phase, entry=RAY,
                arguments=(0, 0, bits(3.5), bits(-4.25), bits(5.75)))
            model.f[12], model.f[14] = bits(1.25), bits(-2.75)
            model.run()
            self.assertEqual(model.f[0], 0)
            self.assertEqual([event for event in model.events if event[0] == 'W'],
                [('W', STACK + phase, 4, bits(1.25)), ('W', STACK + phase + 4, 4, bits(-2.75)),
                 ('W', STACK + phase + 8, 4, bits(3.5)), ('W', STACK + phase + 12, 4, bits(-4.25))])

    def test_finite_sqrt_and_truncate_instruction_probes(self):
        words = [0x46000004, 0x4600010D, 0x03E00008, 0]
        for value, phase in itertools.product((0.0, -0.0, 0.25, 1.0, 2.0, 3.0, 9.0, 10.0,
                                               100000000.0, 16777216.0, 16777215.0, 2147483647.0), (0, 8)):
            model = RootOracle(words, case_memory(), phase=phase)
            model.f[0] = bits(value)
            model.run()
            expected = bits(math.sqrt(floating(bits(value))))
            self.assertEqual((model.f[0], model.f[4]), (expected, math.trunc(floating(expected))))


if __name__ == '__main__':
    unittest.main()
