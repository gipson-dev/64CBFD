"""Horizontal graph-edge crossings, including retail's last-fraction result."""

import csv
import itertools
import json
import math
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_graph_edge_crossing_candidates as screen
from tools.experiments import game_graph_edge_crossing_lifetimes as lifetimes
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_record_neighbor_visit_match import read
from tools.tests.test_game_root_neighbor_lookup_match import narrow, external, external_writes
from tools.tests.test_game_table_range_loader import STACK, native
from tools.tests.game_animation_timeline_oracle import bits, floating


ENTRY = screen.ENTRY
COUNT, GLOBAL, HEIGHT = (screen.SYMBOLS[n] for n in ('D_80087290', 'D_800D2350', 'func_15085DA8'))
TABLE, ALTERNATE = 0x90000, 0xA0000


def rounded(value):
    try:
        return floating(bits(value))
    except OverflowError:
        return math.copysign(math.inf, value)


def case_memory(points=((0, 0), (0, 10)), edges=(1,), count=1, band=0):
    memory = {STACK + i: 0xA5 for i in range(-0x2000, 0x100)}
    for base in (TABLE, ALTERNATE):
        memory.update({base + i: 0xA5 for i in range(512 * 16)})
        for i in range(512):
            pointer = base + i * 16
            for offset in (0, 2, 4):
                put(memory, pointer + offset, 0, 2)
            put(memory, pointer + 6, band, 1)
            put(memory, pointer + 14, 0, 1)
            for j in range(5):
                put(memory, pointer + 9 + j, 255, 1)
        for i, (x, z) in enumerate(points):
            put(memory, base + i * 16, x, 2)
            put(memory, base + i * 16 + 4, z, 2)
            put(memory, base + i * 16 + 14, 1, 1)
        for j, identity in enumerate(edges):
            put(memory, base + 9 + j, identity, 1)
    put(memory, COUNT, count, 2)
    put(memory, GLOBAL, TABLE)
    return memory


def mutations(mode):
    return [(address, value, size) for bit, address, value, size in (
        (1, COUNT, 0, 2), (2, COUNT, 2, 2), (4, GLOBAL, ALTERNATE, 4),
        (8, TABLE + 14, 0, 1), (16, ALTERNATE + 4, -10, 2)) if mode & bit]


def reference(initial, parameters=(-5.0, 2.75, 5.0, 10.0, 0.0), band=0, mutation=0):
    memory = dict(initial)
    x, y, z, dx, dz = map(rounded, parameters)
    for address, value, size in mutations(mutation):
        put(memory, address, value, size)
    count, table = narrow(read(memory, COUNT, 2), 16), read(memory, GLOBAL, 4)
    minimum, last, trace = 100.0, None, []
    mul = lambda a, b: rounded(a * b)
    add = lambda a, b: rounded(a + b)
    dot = lambda a, b, c, d: add(mul(a, b), mul(c, d))
    for i in range(max(0, count)):
        owner = table + i * 16
        if read(memory, owner + 14, 1) != 1 or read(memory, owner + 6, 1) != band:
            continue
        ax, az = (narrow(read(memory, owner + offset, 2), 16) for offset in (0, 4))
        for j in range(5):
            identity = read(memory, owner + j + 9, 1)
            if identity == 255 or identity <= i:
                continue
            target = table + identity * 16
            if read(memory, target + 14, 1) != 1:
                continue
            bx, bz = (narrow(read(memory, target + offset, 2), 16) for offset in (0, 4))
            normal = (float(bz - az), -float(bx - ax))
            plane = -dot(ax, normal[0], normal[1], az)
            left = add(dot(x, normal[0], z, normal[1]), plane)
            right = add(dot(add(x, dx), normal[0], add(z, dz), normal[1]), plane)
            if not ((right < 0 <= left) or (left < 0 <= right)):
                continue
            a, b = -left if left < 0 else left, -right if right < 0 else right
            last = rounded(a / add(a, b))
            tangent = (-normal[1], normal[0])
            plane = -dot(ax, tangent[0], tangent[1], az)
            crossing = add(dot(add(x, mul(last, dx)), tangent[0],
                               add(z, mul(last, dz)), tangent[1]), plane)
            extent = add(dot(bx, tangent[0], tangent[1], bz), plane)
            inside = (0 < extent and 0 < crossing <= extent) or (extent < 0 and extent <= crossing < 0)
            trace.append((i, j, identity, bits(last), inside))
            if inside and last < minimum:
                minimum = last
    result = mul(rounded(math.sqrt(add(mul(dx, dx), mul(dz, dz)))), last) if minimum <= 1 else -1.0
    return memory, [(HEIGHT, bits(y))], [('W', a, s, v & ((1 << (8*s))-1)) for a, v, s in mutations(mutation)], bits(result), trace


class EdgeOracle(TriangleOracle):
    def __init__(self, words, memory, parameters=(-5.0, 2.75, 5.0, 10.0, 0.0),
                 band=0, mutation=0, phase=0):
        super().__init__(words, memory, entry=ENTRY, phase=phase,
                         arguments=(0, 0, bits(parameters[2]), bits(parameters[3]), bits(parameters[4])))
        self.f[12], self.f[14] = bits(parameters[0]), bits(parameters[1])
        self.band, self.mutation = band, mutation

    def execute(self, word):
        op, rs, fs, fd, fn = word >> 26, word >> 21 & 31, word >> 11 & 31, word >> 6 & 31, word & 63
        if op == 17 and rs == 16 and fn == 7:
            self.f[fd] = self.f[fs] ^ 0x80000000
        elif op == 17 and rs == 16 and fn == 4:
            value = floating(self.f[fs])
            assert value >= 0 and math.isfinite(value)
            self.f[fd] = bits(math.sqrt(value))
        else:
            super().execute(word)

    def record_call(self, target):
        assert target == HEIGHT
        self.calls.append((target, self.f[12]))

    def hook(self, target):
        assert target == HEIGHT
        for address, value, size in mutations(self.mutation):
            self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.r[2] = self.band & 0xFFFFFFFF


class GameGraphEdgeCrossingMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-graph-edge-crossing-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        _, cls.baseline = screen.compile_candidate(cls.root, cls.output, 'baseline', screen.BASELINE)
        _, cls.checkpoint = screen.compile_candidate(cls.root, cls.output, 'checkpoint', lifetimes.CHECKPOINT)
        cls.retail = list(struct.unpack_from('>207I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0xB4244))
        cls.coverage, cls.cases = set(), 0
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def check_case(self, memory, parameters=(-5.0, 2.75, 5.0, 10.0, 0.0), band=0, mutation=0, phase=0):
        wanted, calls, writes, result, trace = reference(memory, parameters, band, mutation)
        for words in (self.retail, self.words, self.baseline, self.checkpoint):
            model = EdgeOracle(words, memory, parameters, band, mutation, phase).run()
            self.assertEqual(model.f[0], result, (parameters, band, trace))
            self.assertEqual(model.calls, calls)
            self.assertEqual(external_writes(model), writes)
            self.assertEqual(external(model.memory), external(wanted))
            if words is self.retail:
                type(self).coverage.update(model.visits)
        type(self).cases += 1
        return result, trace

    def test_orientations_endpoints_parallel_and_zero_motion(self):
        for points, x, z, dx, dz, phase in itertools.product(
                (((0, 0), (0, 10)), ((0, 10), (0, 0)), ((-10, -10), (10, 10)),
                 ((0, 0), (0, 0)), ((-32768, -32768), (32767, 32767))),
                (-10.0, -5.0, -0.0, 0.0, 5.0), (-1.0, -0.0, 0.0, 5.0, 10.0, 11.0),
                (-10.0, 0.0, 10.0), (0.0, 10.0), (0, 8)):
            self.check_case(case_memory(points), (x, 2.75, z, dx, dz), phase=phase)

    def test_last_fraction_not_minimum_and_later_rejected_crossing(self):
        for target, expected, inside in (((10, 10), 10.0, True), ((1, 2), 7.5, False)):
            for phase in (0, 8):
                result, trace = self.check_case(case_memory(((0, 0), (0, 10), target), (1, 2)), phase=phase)
                self.assertEqual(result, bits(expected))
                self.assertEqual([entry[-1] for entry in trace], [True, inside])
                self.assertEqual(trace[0][3], bits(0.5))
        result, _ = self.check_case(case_memory(((0, 0), (1, 2)), (1,)))
        self.assertEqual(result, bits(-1.0))

    def test_near_endpoint_excluded_far_endpoint_included_and_self_id_skipped(self):
        for z, result in ((0.0, -1.0), (10.0, 5.0)):
            actual, _ = self.check_case(case_memory(), (-5.0, 2.75, z, 10.0, 0.0))
            self.assertEqual(actual, bits(result))
        actual, _ = self.check_case(case_memory(edges=(0,)))
        self.assertEqual(actual, bits(-1.0))

    def test_local_negation_and_finite_sqrt_instruction_probes(self):
        for phase, word in itertools.product((0, 8), (0, 0x80000000, 0x3F800000,
                0xBF800000, 0x7F800000, 0xFF800000, 0x7FC12345, 0xFFC12345)):
            model = EdgeOracle([0x46000007, 0x03E00008, 0], case_memory(), phase=phase)
            model.f[0] = word
            model.run()
            self.assertEqual(model.f[0], word ^ 0x80000000)
        for phase, value in itertools.product((0, 8), (0.0, -0.0, 0.25, 1.0, 2.0, 9.0, 100000000.0)):
            model = EdgeOracle([0x46000004, 0x03E00008, 0], case_memory(), phase=phase)
            model.f[0] = bits(value)
            model.run()
            self.assertEqual(model.f[0], bits(math.sqrt(value)))

    def test_filters_full_band_and_signed_count(self):
        for count, band, flag, phase in itertools.product(
                (-32768, -1, 0, 1, 2), (-1, 0, 255, 256), (0, 1, 2, 255), (0, 8)):
            memory = case_memory(count=count, band=band)
            put(memory, TABLE + 14, flag, 1)
            if count <= 0:
                put(memory, GLOBAL, 0)
            self.check_case(memory, band=band, phase=phase)

    def test_all_five_edges_wide_ids_and_target_band_not_filtered(self):
        for slot, identity, target_flag, phase in itertools.product(range(5), (0, 1, 254, 255), (0, 1, 255), (0, 8)):
            memory = case_memory(edges=())
            put(memory, TABLE + 9 + slot, identity, 1)
            for offset, value, size in ((0, 0, 2), (4, 10, 2), (6, 123, 1), (14, target_flag, 1)):
                put(memory, TABLE + identity * 16 + offset, value, size)
            self.check_case(memory, phase=phase)
        memory = case_memory(count=2)
        put(memory, TABLE + 16 + 9, 0, 1)
        self.check_case(memory)

    def test_height_callback_clobbers_and_mutates_before_snapshots(self):
        for mutation, phase in itertools.product(range(32), (0, 8)):
            self.check_case(case_memory(), mutation=mutation, phase=phase)

    def test_unordered_coordinates_and_signed_zero(self):
        for index, value, phase in itertools.product((0, 2, 3, 4), (math.nan, -0.0, 0.0), (0, 8)):
            parameters = [-5.0, 2.75, 5.0, 10.0, 0.0]
            parameters[index] = value
            self.check_case(case_memory(), parameters, phase=phase)

    def test_negative_controls_minimum_result_and_narrowed_height(self):
        for name, body, memory, band in (
                ('minimum-result', screen.SELECTED.replace(' * fraction;', ' * minimum;'),
                 case_memory(((0, 0), (0, 10), (1, 2)), (1, 2)), 0),
                ('byte-band', screen.SELECTED.replace('    s32 band;', '    u8 band;'), case_memory(), 256)):
            self.assertNotEqual(body, screen.SELECTED)
            record, words = screen.compile_candidate(self.root, self.output, name, body)
            self.assertEqual(record['diagnostics'], '')
            self.assertNotEqual(EdgeOracle(words, memory, band=band).run().f[0],
                                EdgeOracle(self.retail, memory, band=band).run().f[0], name)

    def test_native_source_extracted_results_and_full_record_footprints(self):
        source = (self.root / 'conker/src/game/generated_B3020.c').read_text()
        body = re.search(r'f32 func_15086D94\([^;{]*\{\n.*?\n\}', source, re.S).group()
        self.assertEqual(body, screen.SELECTED)
        rows = []
        for x, z, dx, dz, target, band in itertools.product(
                (-5.0, 0.0, 5.0), (0.0, 5.0, 10.0, 11.0), (-10.0, 0.0, 10.0), (0.0, 10.0),
                ((10, 10), (1, 2)), (0, 256)):
            result = reference(case_memory(((0, 0), (0, 10), target), (1, 2)),
                               (x, 2.75, z, dx, dz), band)[3]
            rows.append('{%s,%d,%d,%d,0x%08X}' % (','.join(f'{v:.1f}f' for v in (x, z, dx, dz)),
                                                 *target, band, result))
        self.assertEqual(len(rows), 288)
        self.fixture = '''typedef unsigned char u8;typedef short s16;typedef int s32;
typedef unsigned int u32;typedef float f32;
''' + screen.DECLARATIONS + '''
static union {u32 align;u8 bytes[8192];} storage;
s16 D_80087290;u8 *D_800D2350;static s32 band,calls,error;
static u32 word(f32 v) {union {u32 u;f32 f;} n;n.f=v;return n.u;}
s32 func_15085DA8(f32 y) {calls++;if(word(y)!=word(2.75f)) error=1;return band;}
f32 sqrtf(f32 v) {f32 r;__asm__("sqrtss %1,%0":"=x"(r):"x"(v));return r;}
/* An accepted crossing assigns fraction before lowering the initially-100 minimum. */
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
''' + body + '''
#pragma GCC diagnostic pop
static const struct {f32 x,z,dx,dz;s32 bx,bz,band;u32 result;} cases[]={
''' + ',\n'.join(rows) + '\n};\n'
        self.run_host('''
static u8 before[8192];int c,i;u8 *p;
for(c=0;c<288;c++) {
 for(i=0;i<8192;i++) storage.bytes[i]=0xA5;
 for(i=0;i<512;i++) {
  p=storage.bytes+i*16;*(s16 *)p=0;*(s16 *)(p+2)=123;*(s16 *)(p+4)=0;
  p[6]=0;p[14]=0;p[9]=p[10]=p[11]=p[12]=p[13]=255;
 }
 storage.bytes[14]=storage.bytes[30]=storage.bytes[46]=1;
 *(s16 *)(storage.bytes+20)=10;
 *(s16 *)(storage.bytes+32)=cases[c].bx;*(s16 *)(storage.bytes+36)=cases[c].bz;
 storage.bytes[9]=1;storage.bytes[10]=2;
 for(i=0;i<8192;i++) before[i]=storage.bytes[i];
 D_80087290=1;D_800D2350=storage.bytes;band=cases[c].band;calls=error=0;
 if(word(func_15086D94(cases[c].x,2.75f,cases[c].z,cases[c].dx,cases[c].dz))!=cases[c].result) return 1;
 if(calls!=1 || error || D_80087290!=1 || D_800D2350!=storage.bytes) return 2;
 for(i=0;i<8192;i++) if(storage.bytes[i]!=before[i]) return 3;
}
''')

    def test_production_slot_and_guard_inventory(self):
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                     'mips-linux-gnu-objdump')
        self.assertEqual(functions['func_15086D94'], self.words + [0] * (207 - len(self.words)))
        self.assertEqual((addresses['func_15086D94'], addresses['func_150870D0']), (ENTRY, 0x150870D0))
        self.assertNotIn('__retail_overflow_func_15086D94', functions)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse(any(r['function'] == 'func_15086D94' for r in csv.DictReader(stream)))

    def test_compiler_inventory_and_nonmatching_boundary(self):
        forms = screen.candidates() + screen.lifetime_candidates() + screen.cursor_candidates() + screen.parameter_candidates()
        self.assertEqual((len(forms), len(dict(forms))), (39, 39))
        self.assertEqual(lifetimes.CHECKPOINT, dict(forms)['reused-side-values'])
        self.assertEqual(screen.SELECTED, lifetimes.SELECTED)
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences'],
                          self.record['diagnostics']), (207, 0x80, 102, ''))
        self.assertNotEqual(self.words, self.retail)

    def test_zz_record_coverage_receipt(self):
        missing = set(range(0x15087004, 0x15087028, 4))
        self.assertEqual(self.coverage, set(range(ENTRY, ENTRY + 207 * 4, 4)) - missing)
        (self.output / 'behavior.json').write_text(json.dumps(dict(
            cases=self.cases, models=4, retail_words_visited=len(self.coverage),
            missing=[hex(a) for a in range(ENTRY, ENTRY + 207 * 4, 4) if a not in self.coverage],
            selected=self.record), indent=2) + '\n')


if __name__ == '__main__':
    unittest.main()
