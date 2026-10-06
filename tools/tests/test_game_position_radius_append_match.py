"""Direct leaf match and bounded actual caller prefix, not full caller/gameplay acceptance."""

import csv
import itertools
import math
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_position_radius_append_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put, external_writes
from tools.tests.test_game_actor_buffer_copy_match import CopyOracle
from tools.tests.test_game_table_range_loader import STACK, native
from tools.tests.game_animation_timeline_oracle import bits, floating


ENTRY, GLOBAL, BANK, ACTOR, ENABLE = 0x1508B20C, 0x800D23B0, 0x20000, 0x24000, 0x25000
PREFIX, CLOSURE = 0x150C3494, 0x150C3564
POINTS = ((1.75, -2.75, 3.5), (0.0, -0.0, 0.0), (32767.75, 32768.0, -32768.75),
          (65535.0, 65536.0, -65537.0), (2147483520.0, -2147483648.0, 16777217.0),
          (-1.875, 2.999, 0.0001220703125), (123456.75, -98765.125, 0.5),
          (-32769.0, 32769.0, 65534.5))
RADII = (0.0, -0.0, 900.0, -900.0, 2.5, -1.25, 0.1, 1e20)


def memory_case(count=0, present=True, bank=BANK, coordinates=POINTS[0], enabled=1):
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({bank + i: (i * 137 + 19) & 255 for i in range(-8, 0x1808)})
    memory.update({GLOBAL + i: 0xA5 for i in range(-8, 12)})
    memory.update({ACTOR + i: 0xA5 for i in range(0x40)})
    memory.update({ENABLE + i: 0xA5 for i in range(8)})
    put(memory, bank + 0x1745, count, 1)
    put(memory, GLOBAL, bank if present else 0)
    put(memory, ENABLE, enabled, 1)
    for i, value in enumerate(coordinates):
        put(memory, ACTOR + 0x14 + i * 4, bits(value))
    return memory


class AppendOracle(TriangleOracle):
    def __init__(self, words, memory, coordinates=POINTS[0], radius=RADII[0], phase=0, caller=None):
        args = (*map(bits, coordinates), bits(radius))
        connected = None if caller is None else {ENTRY + i * 4: w for i, w in enumerate(words)}
        super().__init__(words, memory, phase=phase, entry=ENTRY if caller is None else PREFIX,
                         arguments=args, connected=connected)
        self.f[12], self.f[14] = args[:2]
        if caller is not None:
            self.code = caller | connected
            self.r[29] -= 0x60
            self.put(self.r[29] + 0x28, self.before[16], 4)
            self.put(self.r[29] + 0x2C, self.before[31], 4)
            self.r[16], self.r[5] = ACTOR, ENABLE

    def execute(self, word):
        if word >> 26 == 32:
            CopyOracle.execute(self, word)
        else:
            super().execute(word)

    def record_call(self, target):
        assert target == ENTRY
        self.calls.append((target, self.f[12], self.f[14], self.r[6], self.r[7]))

    def hook(self, target):
        raise AssertionError(('unexpected opaque helper', target))


def expected_writes(memory, coordinates, radius):
    bank = int.from_bytes(bytes(memory[GLOBAL + i] for i in range(4)), 'big')
    if not bank:
        return []
    count = memory[bank + 0x1745]
    index = count if count < 128 else count - 256
    if index >= 8:
        return []
    words = [math.trunc(floating(bits(value))) & 65535 for value in coordinates]
    square = bits(floating(bits(radius)) * floating(bits(radius)))
    record = bank + 0x1748 + index * 12
    return [('W', bank + 0x1745, 1, (index + 1) & 255),
            *[('W', record + 4 + i * 2, 2, value) for i, value in enumerate(words)],
            ('W', record, 4, square)]


class GamePositionRadiusAppendMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-position-radius-append-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        _, cls.baseline = screen.compile_candidate(cls.root, cls.output, 'baseline', screen.PLACEHOLDER)
        forms = dict(screen.candidates())
        cls.negative = {name: screen.compile_candidate(cls.root, cls.output, name, forms[name])[1] for name in
                        ('cached-s32-word', 'unsigned-load-negative-control', 'lower-bound-negative-control',
                         'wrong-stride-negative-control', 'unsquared-negative-control',
                         'increment-unsigned-word-index')}
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>39I', rom, 0xB86BC))
        cls.production = load_elf_functions(str(cls.root / 'conker/build/conker.us.elf'),
                                           'mips-linux-gnu-objdump')[0]['func_1508B20C']
        cls.caller = {address: struct.unpack_from('>I', rom, address - 0x15000000 + 0x2D4B0)[0]
                      for address in (*range(PREFIX, PREFIX + 10 * 4, 4), *range(CLOSURE, CLOSURE + 4 * 4, 4))}
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        source = (cls.root / 'conker/src/game/generated_B3020.c').read_text()
        cls.body = re.search(r'void func_1508B20C\([^;{]*\{\n.*?\n\}', source, re.S).group(0)
        cls.fixture = '''typedef signed char s8;typedef unsigned char u8;typedef short s16;
typedef unsigned short u16;typedef int s32;typedef unsigned int u32;typedef float f32;
#define NULL ((void *)0)
s32 D_800D23B0;
''' + cls.body + r'''
static union {u32 align;u8 bytes[0x1804];} storage;
static u8 expected[0x1804];
static f32 points[8][3]={
 {1.75f,-2.75f,3.5f},{0.0f,-0.0f,0.0f},{32767.75f,32768.0f,-32768.75f},
 {65535.0f,65536.0f,-65537.0f},{2147483520.0f,-2147483648.0f,16777217.0f},
 {-1.875f,2.999f,0.0001220703125f},{123456.75f,-98765.125f,0.5f},
 {-32769.0f,32769.0f,65534.5f}};
static u16 halfwords[8][3]={
 {1,0xFFFE,3},{0,0,0},{0x7FFF,0x8000,0x8000},{0xFFFF,0,0xFFFF},
 {0xFF80,0,0},{0xFFFF,2,0},{0xE240,0x7E33,0},{0x7FFF,0x8001,0xFFFE}};
static u32 radii[8]={0,0x80000000,0x44610000,0xC4610000,0x40200000,0xBFA00000,0x3DCCCCCD,0x60AD78EC};
static u32 squares[8]={0,0,0x4945C100,0x4945C100,0x40C80000,0x3FC80000,0x3C23D70B,0x7F800000};
static f32 number(u32 value) {union {u32 u;f32 f;} v;v.u=value;return v.f;}
static void initialize(int count,int shift,int present) {
 int i;for(i=0;i<0x1804;i++) storage.bytes[i]=expected[i]=(u8)(i*137+19);
 storage.bytes[shift+0x1745]=expected[shift+0x1745]=(u8)count;
 D_800D23B0=present?(s32)(storage.bytes+shift):0;
}
static void predict(int count,int shift,int present,int point,int radius) {
 int index=count<128?count:count-256;
 if(present && index<8) {
  int i,record=shift+0x1748+index*12;
  expected[shift+0x1745]=(u8)(index+1);
  for(i=0;i<3;i++) *(u16 *)(expected+record+4+i*2)=halfwords[point][i];
  *(u32 *)(expected+record)=squares[radius];
 }
}
static int matches(void) {
 int i;for(i=0;i<0x1804;i++) if(storage.bytes[i]!=expected[i]) return 0;
 return 1;
}
'''

    def models(self, memory, coordinates=POINTS[0], radius=RADII[0], phase=0, caller=None):
        models = [AppendOracle(words, memory, coordinates, radius, phase, caller).run()
                  for words in (self.retail, self.words, self.production)]
        for model in models[1:]:
            self.assertEqual(model.events, models[0].events)
            self.assertEqual(model.memory, models[0].memory)
            self.assertEqual(model.calls, models[0].calls)
        return models[0]

    def test_direct_complete_slot_source_signature_and_existing_profile(self):
        self.assertEqual((self.record['body_words'], self.record['real_differences']), (39, 0))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.production, self.retail)
        self.assertEqual(self.body, screen.SELECTED)
        self.assertIn('void func_1508B20C(f32, f32, f32, f32);',
                      (self.root / 'conker/include/functions.h').read_text())
        record, words = screen.compile_candidate(self.root, self.output, 'existing-slice-profile',
                                                 screen.SELECTED, no_unroll=True)
        self.assertEqual((record['body_words'], record['real_differences'], record['diagnostics']), (39, 0, ''))
        self.assertEqual(words, self.retail)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse(any(r['function'] == 'func_1508B20C' for r in csv.DictReader(stream)))

    def test_control_inventory_and_fail_closed_anchors(self):
        forms = screen.candidates()
        self.assertEqual((len(forms), len(dict(forms))), (34, 34))
        self.assertEqual(dict(forms)['inline-count-guard'], screen.SELECTED)
        with self.assertRaises(ValueError):
            screen.replace(screen.BODY, 'missing anchor', 'replacement')
        with self.assertRaises(ValueError):
            screen.replace(screen.BODY, 'index * 12', 'index * 8', 3)
        for name, expected in (('placeholder', (3, 36)), ('ordinary-s32-word', (39, 15)),
                               ('literal-index-increment', (39, 5)), ('cached-s32-word', (31, 36)),
                               ('increment-byte-index', (41, 35))):
            record, _ = screen.compile_candidate(self.root, self.output, name, dict(forms)[name])
            self.assertEqual((record['body_words'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')

    def test_all_signed_count_bytes_coordinates_radii_phases_and_word_coverage(self):
        coverage, cases = set(), 0
        for count, pattern, phase, shift in itertools.product(range(256), range(8), (0, 8), (0, 4)):
            coordinates, radius = POINTS[pattern], RADII[pattern]
            memory = memory_case(count, bank=BANK + shift)
            model = self.models(memory, coordinates, radius, phase)
            self.assertEqual(external_writes(model), expected_writes(memory, coordinates, radius))
            reads = [(a, size) for a, size, _ in model.reads if a == GLOBAL]
            self.assertEqual(reads, [(GLOBAL, 4)] * (5 if count < 8 or count >= 128 else 1))
            self.assertEqual(sum(a == BANK + shift + 0x1745 for a, _, _ in model.reads), 1)
            self.assertEqual(model.f[20:], model.saved_f)
            coverage.update(model.visits)
            cases += 1
        self.assertEqual(cases, 8192)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 39 * 4, 4)))

    def test_null_base_does_not_dereference_count_or_convert_coordinates(self):
        for phase, pattern in itertools.product((0, 8), range(8)):
            memory = memory_case(present=False)
            # Invalid conversion inputs are permitted only on the path that never converts them.
            model = self.models(memory, (math.nan, math.inf, -math.inf), RADII[pattern], phase)
            self.assertEqual(external_writes(model), [])
            self.assertEqual([(a, s) for a, s, _ in model.reads], [(GLOBAL, 4)])
            self.assertNotIn(ENTRY + 0x2C, model.visits)

    def test_physical_global_aliases_prove_fresh_bases_and_store_order(self):
        for field, offset in (('x', 0x174C), ('z', 0x1750), ('radius', 0x1748)):
            for phase in (0, 8):
                bank = GLOBAL - offset
                memory = memory_case(bank=bank)
                new_bank = bank + 0x10000
                memory.update({new_bank + i: 0xA5 for i in range(-8, 0x1808)})
                coordinates = (-32754.0, 19.75, 21.5) if field == 'x' else (17.75, 19.75, -32754.0)
                model = self.models(memory, coordinates, 6.0, phase)
                writes = external_writes(model)
                self.assertEqual(writes[0], ('W', bank + 0x1745, 1, 1))
                bases = (bank, new_bank, new_bank, new_bank) if field == 'x' else (
                    bank, bank, bank, new_bank) if field == 'z' else (bank,) * 4
                expected = [('W', bases[i] + 0x174C + i * 2, 2,
                             math.trunc(floating(bits(coordinates[i]))) & 65535) for i in range(3)]
                expected.append(('W', bases[3] + 0x1748, 4, bits(36.0)))
                self.assertEqual(writes[1:], expected)
                self.assertEqual(sum(a == GLOBAL for a, _, _ in model.reads), 5)

    def test_negative_controls_reject_unsigned_count_cached_base_stride_and_square(self):
        for name, words in self.negative.items():
            memory = memory_case(count=255 if 'unsigned' in name or 'lower-bound' in name else 1)
            if 'cached' in name:
                bank = GLOBAL - 0x174C
                memory = memory_case(bank=bank)
                memory.update({bank + 0x10000 + i: 0xA5 for i in range(-8, 0x1808)})
            coordinates = (-32754.0, 19.75, 21.5)
            original = AppendOracle(self.retail, memory, coordinates, 6.0).run()
            altered = AppendOracle(words, memory, coordinates, 6.0).run()
            self.assertNotEqual(external_writes(altered), external_writes(original), name)
        self.assertNotEqual(external_writes(AppendOracle(self.baseline, memory_case(), radius=6.0).run()),
                            expected_writes(memory_case(), POINTS[0], 6.0))

    def test_bounded_actual_caller_setup_leaf_and_return_closure(self):
        cases, coverage = 0, set()
        for count, enabled, present, phase, pattern in itertools.product(
                (0, 1, 7, 8, 127, 128, 255), (0, 1, 255), (False, True), (0, 8), (0, 2, 7)):
            coordinates = POINTS[pattern]
            memory = memory_case(count, present, coordinates=coordinates, enabled=enabled)
            model = self.models(memory, coordinates, 900.0, phase, self.caller)
            self.assertEqual(model.calls, [(ENTRY, *map(bits, coordinates), bits(900.0))] if enabled else [])
            self.assertEqual(external_writes(model), expected_writes(memory, coordinates, 900.0) if enabled else [])
            coverage.update(model.visits)
            cases += 1
        self.assertEqual(cases, 252)
        self.assertTrue(set(self.caller) <= coverage)
        self.assertTrue(set(range(ENTRY, ENTRY + 39 * 4, 4)) <= coverage)

    def test_native_all_count_bytes_coordinate_patterns_radii_and_base_states(self):
        self.run_host(r'''
int c,p,r,s,present,cases=0;
if(sizeof(void *)!=4 || sizeof(s8)!=1 || sizeof(s16)!=2 || sizeof(f32)!=4) return 1;
for(c=0;c<256;c++) for(p=0;p<8;p++) for(r=0;r<8;r++) for(s=0;s<=4;s+=4) for(present=0;present<2;present++) {
 initialize(c,s,present);predict(c,s,present,p,r);
 func_1508B20C(points[p][0],points[p][1],points[p][2],number(radii[r]));
 if(!matches()) return 2;
 if(D_800D23B0!=(present?(s32)(storage.bytes+s):0)) return 3;
 cases++;
}
if(cases!=65536) return 4;
''')

    def test_native_repeated_appends_fill_eight_records_then_stop(self):
        self.run_host(r'''
int i;
initialize(0,0,1);
for(i=0;i<12;i++) {
 predict(i<8?i:8,0,1,i%8,(i+3)%8);
 func_1508B20C(points[i%8][0],points[i%8][1],points[i%8][2],number(radii[(i+3)%8]));
 if(!matches()) return 1;
 if(storage.bytes[0x1745]!=(i<8?i+1:8)) return 2;
}
''')


if __name__ == '__main__':
    unittest.main()
