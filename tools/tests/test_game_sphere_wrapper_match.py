"""Nine-position sphere wrapper with the complete original output-writing callee."""

import csv
import itertools
import math
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_sphere_wrapper_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.game_owner_pool import normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_projection_lifetime_recovery import put, peek
from tools.tests.test_game_table_range_loader import native, STACK
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly

ORIGIN, DIRECTION, CENTER, POINTS, DISTANCES = 0x20000, 0x21000, 0x22000, 0x24000, 0x28000
STUB = 's32 func_151451F0() {\n    return 0;\n}'
CENTERS = ((5.0, 0.0, 0.0), (-5.0, 0.0, 0.0), (0.0, 0.0, 0.0),
           (1.0, 0.0, 0.0), (5.0, 1.0, 0.0), (5.0, 2.0, 0.0),
           (0.25, 0.5, -0.25), (5.0, 0.25, 0.5), (-0.5, -0.25, 0.5))


def private(address):
    return STACK - 0x300 <= address < STACK + 0x100


def external(memory):
    return {a: b for a, b in memory.items() if not private(a)}


def fixture(center=CENTERS[0], radius=1.0, threshold=100.0, layout=0, phase=0):
    memory = {STACK + i: 0xA5 for i in range(-0x300, 0x100)}
    for base, length in ((ORIGIN, 32), (DIRECTION, 32), (CENTER, 32), (POINTS, 128), (DISTANCES, 32)):
        memory.update({base + i: 0xA5 for i in range(length)})
    for base, values in ((ORIGIN, (0.0, 0.0, 0.0)), (DIRECTION, (1.0, 0.0, 0.0)), (CENTER, center)):
        for i, value in enumerate(values):
            put(memory, base + i * 4, bits(value))
    first, second, distance0, distance1 = POINTS, POINTS + 64, DISTANCES, DISTANCES + 4
    if layout == 1: second = first
    if layout == 2: first = ORIGIN
    if layout == 3: second = ORIGIN
    if layout == 4: first = DIRECTION
    if layout == 5: second = DIRECTION
    if layout == 6: first = CENTER
    if layout == 7: distance0 = first
    if layout == 8: distance1 = first + 4
    if layout == 9: distance1 = distance0
    if layout == 10: first = second + 4
    if layout == 11: distance0 = DIRECTION
    if layout == 12: distance1 = ORIGIN + 8
    if layout == 13: distance0 = STACK + phase + 0x10
    if layout == 14:
        distance0 = STACK + phase + 0x1C
        memory.update({0x40800000 + i: 0xA5 for i in range(4)})
        put(memory, 0x40800000, bits(-1.0))
    if layout == 15:
        distance1 = STACK + phase + 0x20
        memory.update({0x40C00000 + i: 0xA5 for i in range(4)})
        put(memory, 0x40C00000, bits(-1.0))
    return memory, (ORIGIN, DIRECTION, CENTER, bits(radius), bits(threshold),
                    first, second, distance0, distance1)


class SphereOracle(TriangleOracle):
    def __init__(self, words, memory, args, connected, phase=0, entry=screen.ENTRY):
        super().__init__(words, memory, phase=phase, entry=entry, arguments=args, connected=connected)

    def execute(self, word):
        op, rs, rd, fd, fn = word >> 26, word >> 21 & 31, word >> 11 & 31, word >> 6 & 31, word & 63
        if op == 17 and rs == 16 and fn == 4:
            value = floating(self.f[rd])
            self.f[fd] = bits(math.sqrt(value) if value >= 0.0 else math.nan)
        elif op == 17 and rs == 16 and fn == 7:
            self.f[fd] = self.f[rd] ^ 0x80000000
        else:
            super().execute(word)

    def record_call(self, target):
        if target in (screen.ENTRY, screen.CALLEE):
            self.calls.append((target, *self.arguments(9 if target == screen.ENTRY else 8)))
        else:
            assert target == screen.DOT
            self.calls.append((target, self.r[4], self.r[5]))

    def hook(self, target):
        raise AssertionError(('unconnected sphere helper', hex(target)))


class BoundaryOracle(SphereOracle):
    """Seeded wrapper branch probes, separate from connected geometry evidence."""

    def __init__(self, words, memory, args, status, outputs, phase=0):
        super().__init__(words, memory, args, {}, phase)
        self.status, self.outputs = status, outputs

    def hook(self, target):
        assert target == screen.CALLEE
        args = self.arguments(8)
        for address, value in zip(args[6:], self.outputs):
            self.put(address, value, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.r[2] = self.status


def reference(memory, args, phase=0):
    memory = memory.copy()
    start, direction, center, radius, threshold, point0, point1, distance0, distance1 = args
    for i, word in enumerate(args[4:]):
        put(memory, STACK + phase + 0x10 + i * 4, word)
    writes = []

    def read(address):
        return floating(peek(memory, address))

    def rounded(value):
        return floating(bits(value))

    def multiply(a, b):
        return rounded(a * b)

    def add(a, b):
        return rounded(a + b)

    def store(address, value):
        word = bits(value)
        put(memory, address, word)
        if not private(address):
            writes.append(('W', address, 4, word))

    origin = [read(start + i * 4) for i in range(3)]
    copied_direction = [read(direction + i * 4) for i in range(3)]
    delta = [rounded(read(center + i * 4) - origin[i]) for i in range(3)]
    projection = add(add(multiply(delta[0], copied_direction[0]),
                         multiply(delta[1], copied_direction[1])), multiply(delta[2], copied_direction[2]))
    perpendicular = rounded(add(add(multiply(delta[0], delta[0]), multiply(delta[1], delta[1])),
                                multiply(delta[2], delta[2])) - multiply(projection, projection))
    radius_squared = multiply(floating(radius), floating(radius))
    helper_status = 0
    if not radius_squared < perpendicular:
        root = rounded(math.sqrt(rounded(radius_squared - perpendicular)))
        if projection < root:
            root = -root
        first, second = rounded(projection - root), add(projection, root)
        for i in range(3): store(point0 + i * 4, add(multiply(first, copied_direction[i]), origin[i]))
        store(distance0, first)
        for i in range(3): store(point1 + i * 4, add(multiply(second, copied_direction[i]), origin[i]))
        store(distance1, second)
        relative = [rounded(read(point0 + i * 4) - read(start + i * 4)) for i in range(3)]
        products = [multiply(relative[i], read(direction + i * 4)) for i in range(3)]
        helper_status = int(not add(add(products[0], products[1]), products[2]) < 0.0)
    status = 0
    if helper_status:
        first = read(peek(memory, STACK + phase + 0x1C))
        second_pointer = peek(memory, STACK + phase + 0x20)
        if first < 0.0 and read(second_pointer) < 0.0:
            status = 0
        elif first >= 0.0 and read(second_pointer) < 0.0:
            status = 1
        else:
            status = int(first < read(STACK + phase + 0x10))
    return memory, writes, status, helper_status


class GameSphereWrapperMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or shutil.which('mips-linux-gnu-ld') is None:
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-sphere-wrapper-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.callee_record, cls.callee_trial = screen.compile_candidate(cls.root, cls.output, 'callee',
            screen.CALLEE_BODY, function=screen.CALLEE_FUNCTION)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>53I', rom, screen.ROM))
        cls.callee = list(struct.unpack_from('>126I', rom, screen.CALLEE_ROM))
        cls.dot = list(struct.unpack_from('>13I', rom, screen.DOT_ROM))
        cls.connected = {}
        for entry, words in ((screen.CALLEE, cls.callee), (screen.DOT, cls.dot)):
            cls.connected.update(zip(range(entry, entry + len(words) * 4, 4), words))
        cls.coverage = set()
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = '''typedef unsigned int u32;typedef int s32;typedef float f32;
typedef struct {f32 unk0,unk4,unk8;} struct17;
typedef char pointer_size[sizeof(void *)==4?1:-1];
static u32 logs[8];static int helperStatus,calls;static f32 output0,output1;
static u32 word(f32 f) {union {f32 f;u32 u;} b;b.f=f;return b.u;}
static f32 number(u32 u) {union {f32 f;u32 u;} b;b.u=u;return b.f;}
s32 func_151452C4(struct17 *a,struct17 *b,struct17 *c,f32 r,
    struct17 *p,struct17 *q,f32 *x,f32 *y) {
    logs[0]=(u32)a;logs[1]=(u32)b;logs[2]=(u32)c;logs[3]=word(r);
    logs[4]=(u32)p;logs[5]=(u32)q;logs[6]=(u32)x;logs[7]=(u32)y;
    calls++;*x=output0;*y=output1;return helperStatus;
}
''' + screen.SELECTED + '\n'

    def pair(self, memory, args, phase=0):
        expected, writes, status, helper_status = reference(memory, args, phase)
        models = []
        for words in (self.retail, self.words):
            model = SphereOracle(words, memory, args, self.connected, phase).run()
            self.assertEqual(model.r[2], status)
            self.assertEqual(external(model.memory), external(expected))
            self.assertEqual([e for e in model.events if e[0] == 'W' and not private(e[1])], writes)
            self.assertEqual(model.calls[0], (screen.CALLEE, *args[:4], *args[5:]))
            self.assertEqual(len(model.calls), 1 if helper_status == 0 and not writes else 2)
            self.coverage.update(model.visits)
            models.append(model)
        self.assertEqual(models[0].memory, models[1].memory)
        self.assertEqual(models[0].events, models[1].events)
        self.assertEqual(models[0].calls, models[1].calls)
        for offset in (0x10, 0x1C, 0x20):
            self.assertEqual(peek(models[0].memory, STACK + phase + offset), peek(expected, STACK + phase + offset))
        return models

    def test_complete_direct_slot_and_profile_source_shape_controls(self):
        self.assertEqual(self.words, self.retail)
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (53, 40, 0))
        self.assertEqual(self.record['relocations'], {0x2C: [('R_MIPS_26', screen.CALLEE_FUNCTION)]})
        self.assertEqual(self.record['diagnostics'], '')
        expected = {'selected': ((53, 40, 0), (53, 40, 5), (69, 40, 63), (69, 40, 63)),
            'early-false': ((52, 40, 38), (52, 40, 43), (69, 40, 63), (69, 40, 63)),
            'cached-first': ((53, 40, 0), (53, 40, 5), (68, 48, 63), (68, 48, 63)),
            'threshold-home': ((54, 40, 18), (54, 40, 23), (69, 40, 63), (69, 40, 63)),
            'first-pointer-home': ((58, 40, 51), (58, 40, 52), (69, 40, 63), (69, 40, 61))}
        for name, body in screen.candidates():
            for profile, measurement in zip(screen.PROFILES, expected[name]):
                record, _ = screen.compile_candidate(self.root, self.output, name + '-' + profile, body, profile)
                self.assertEqual((record['body_words'], record['frame'], record['differences']), measurement)

    def test_connected_finite_geometry_aliases_bounds_and_full_storage(self):
        cases = 0
        for center, radius, threshold, layout, phase in itertools.product(
                CENTERS, (0.0, 0.25, 1.0, -1.0, 2.0, 8.0), (-10.0, -0.0, 0.0, 1.0, 4.0, 100.0), range(13), (0, 8)):
            memory, args = fixture(center, radius, threshold, layout, phase)
            self.pair(memory, args, phase)
            cases += 1
        self.assertEqual(cases, 8424)
        for entry, count in ((screen.CALLEE, 126), (screen.DOT, 13)):
            self.assertTrue(set(range(entry, entry + count * 4, 4)).issubset(self.coverage))

    def test_natural_scalar_stores_change_threshold_and_both_pointer_homes(self):
        expected = {13: 0, 14: 1, 15: 1}
        for layout, phase in itertools.product((13, 14, 15), (0, 8)):
            memory, args = fixture(threshold=100.0 if layout == 13 else 0.0, layout=layout, phase=phase)
            retail, _ = self.pair(memory, args, phase)
            self.assertEqual(retail.r[2], expected[layout])

    def test_false_callee_preserves_writes_and_wrapper_reads_outputs_lazily(self):
        memory, args = fixture(CENTERS[1])
        model, _ = self.pair(memory, args)
        self.assertEqual(model.r[2], 0)
        self.assertEqual(sum(e[0] == 'W' and not private(e[1]) for e in model.events), 8)
        self.assertNotIn(screen.ENTRY + 0x44, model.visits)
        memory, args = fixture((5.0, 8.0, 0.0))
        for base in (POINTS, POINTS + 64, DISTANCES):
            for i in range(12): memory.pop(base + i, None)
        self.pair(memory, args)
        self.assertEqual(self.record['body_words'], 53)

    def test_callee_trial_is_explicitly_uninstalled_and_retained_helpers_are_exact(self):
        self.assertEqual((self.callee_record['body_words'], self.callee_record['frame'],
                          self.callee_record['differences']), (128, 104, 106))
        production = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        self.assertEqual(production[screen.CALLEE_FUNCTION], self.callee)
        self.assertEqual(production['func_15144A74'], self.dot)
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        from tools.experiments import game_sphere_callee_allocation_candidates as allocation
        self.assertIn(allocation.SELECTED, source)
        self.assertNotIn(screen.CALLEE_BODY, source)

    def test_callee_c_trial_bounded_finite_external_aliases_not_private_layout(self):
        connected = {a: word for a, word in self.connected.items() if not screen.CALLEE <= a < screen.CALLEE + 504}
        connected.update(zip(range(screen.CALLEE, screen.CALLEE + len(self.callee_trial) * 4, 4), self.callee_trial))
        cases = 0
        for center, radius, layout, phase in itertools.product(CENTERS, (0.0, 0.25, 1.0, -1.0, 2.0, 8.0), range(13), (0, 8)):
            memory, args = fixture(center, radius, 4.0, layout, phase)
            expected, writes, status, _ = reference(memory, args, phase)
            model = SphereOracle(self.words, memory, args, connected, phase).run()
            self.assertEqual(model.r[2], status)
            self.assertEqual(external(model.memory), external(expected))
            self.assertEqual([e for e in model.events if e[0] == 'W' and not private(e[1])], writes)
            cases += 1
        self.assertEqual(cases, 1404)

    def test_missing_required_geometry_and_hit_output_fields_fail_closed(self):
        cases = 0
        for base, count in ((ORIGIN, 3), (DIRECTION, 3), (CENTER, 3),
                            (POINTS, 3), (POINTS + 64, 3), (DISTANCES, 2)):
            for i in range(count):
                memory, args = fixture()
                for byte in range(4): memory.pop(base + i * 4 + byte)
                for words in (self.retail, self.words):
                    with self.assertRaisesRegex(AssertionError, 'unmapped'):
                        SphereOracle(words, memory, args, self.connected).run()
                cases += 1
        self.assertEqual(cases, 17)

    def test_native_32_bit_nine_position_float_bits_aliases_and_return_paths(self):
        self.run_host(r'''
static u32 values[]={0xFF800000,0xBF800000,0x80000000,0,0x3F000000,
    0x3F800000,0x40800000,0x7F800000,0x7FC01234};
static struct17 a,b,c,p,q;static f32 storage[4];
int i,j,k,r,h,alias,n,cases=0,expected,result;f32 first,second,limit;u32 wanted[8];
for(h=0;h<2;h++)for(i=0;i<9;i++)for(j=0;j<9;j++)for(k=0;k<9;k++)for(r=0;r<9;r++)for(alias=0;alias<2;alias++) {
    output0=number(values[i]);output1=number(values[j]);limit=number(values[k]);
    storage[0]=storage[1]=number(0xA5A5A5A5);calls=0;helperStatus=h;
    first=alias?output1:output0;second=output1;
    expected=h && !((first<0 && second<0)) && ((first>=0 && second<0) || first<limit);
    wanted[0]=(u32)&a;wanted[1]=(u32)&b;wanted[2]=(u32)&c;wanted[3]=values[r];
    wanted[4]=(u32)&p;wanted[5]=(u32)&q;wanted[6]=(u32)storage;wanted[7]=(u32)(storage+(alias?0:1));
    result=func_151451F0(&a,&b,&c,number(values[r]),limit,&p,&q,storage,storage+(alias?0:1));
    if(result!=expected || calls!=1 || word(storage[0])!=word(first)
       || word(storage[alias?0:1])!=word(second))return 1;
    for(n=0;n<8;n++)if(logs[n]!=wanted[n])return 2;
    cases++;
}
if(cases!=26244)return 3;
''')

    def test_seeded_unordered_comparisons_lazy_reads_and_reachable_wrapper_words(self):
        values = (0xFF800000, 0xBF800000, 0x80000000, 0, 0x3F000000,
                  0x3F800000, 0x40800000, 0x7F800000, 0x7FC01234)
        coverage, cases = set(), 0
        for status, first, second, threshold, phase, alias in itertools.product(
                (0, 1), values, values, values, (0, 8), (0, 1)):
            memory, args = fixture(phase=phase)
            args = (*args[:4], threshold, *args[5:8], args[7] if alias else args[8])
            x, y, limit = floating(second if alias else first), floating(second), floating(threshold)
            expected = int(status and not (x < 0.0 and y < 0.0) and
                           ((x >= 0.0 and y < 0.0) or x < limit))
            models = [BoundaryOracle(words, memory, args, status, (first, second), phase).run()
                      for words in (self.retail, self.words)]
            for model in models:
                self.assertEqual(model.r[2], expected)
                self.assertEqual(model.calls, [(screen.CALLEE, *args[:4], *args[5:])])
                coverage.update(model.visits)
                if not status:
                    self.assertFalse(any(e[0] == 'R' and e[1] in args[7:] for e in model.events))
            self.assertEqual(models[0].memory, models[1].memory)
            self.assertEqual(models[0].events, models[1].events)
            cases += 1
        self.assertEqual(cases, 5832)
        expected = set(range(screen.ENTRY, screen.ENTRY + 212, 4)) - {screen.ENTRY + 0x74, screen.ENTRY + 0xA0}
        self.assertEqual(coverage, expected)
        self.assertEqual(self.words[0x74 // 4], self.retail[0x74 // 4])
        self.assertEqual(self.words[0xA0 // 4], self.retail[0xA0 // 4])

    def test_compiled_negative_controls_break_actual_returns_or_home_dependencies(self):
        cached_threshold = screen.SELECTED.replace('    if (func_',
            '    volatile f32 savedThreshold = arg4;\n    if (func_', 1).replace('*arg7 < arg4', '*arg7 < savedThreshold')
        cached_pointers = screen.SELECTED.replace('    if (func_',
            '    f32 *volatile saved7 = arg7;\n    f32 *volatile saved8 = arg8;\n    if (func_', 1)
        cached_pointers = cached_pointers.replace('*arg7 <', '*saved7 <').replace('*arg7 >=', '*saved7 >=').replace('*arg8 <', '*saved8 <')
        wrong_sign = screen.SELECTED.replace('*arg7 < 0.0f && *arg8 < 0.0f', '*arg7 < 0.0f || *arg8 < 0.0f')
        for name, body, center, threshold, layout in (
                ('cached-threshold', cached_threshold, CENTERS[0], 100.0, 13),
                ('cached-pointers', cached_pointers, CENTERS[0], 0.0, 14),
                ('wrong-sign', wrong_sign, CENTERS[2], 0.0, 0)):
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            memory, args = fixture(center, threshold=threshold, layout=layout)
            correct = SphereOracle(self.retail, memory, args, self.connected).run()
            # Oversized negative bodies must not collide with the fixed callee slot.
            wrong = SphereOracle(words, memory, args, self.connected, entry=0x15200000).run()
            self.assertNotEqual(correct.r[2], wrong.r[2], name)

    def test_both_original_caller_setups_include_their_argument_delay_stores(self):
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        cases = 0
        for kind, center, radius, threshold, phase in itertools.product(
                (0, 1), CENTERS, (0.0, 1.0, 8.0), (-1.0, 4.0, 100.0), (0, 8)):
            memory, _ = fixture(center, radius, threshold, phase=phase)
            sp = STACK + phase
            if kind == 0:
                entry, position, count = 0x151C893C, 0x1F5DEC, 14
                args = (sp + 0x88, DIRECTION, sp + 0x98, bits(radius), bits(threshold),
                        sp + 0x60, sp + 0x54, sp + 0x50, sp + 0x4C)
                put(memory, sp + 0x6C, bits(threshold))
                put(memory, sp + 0xA8, bits(radius))
            else:
                entry, position, count = 0x15145C00, 0x1730B0, 18
                args = (sp + 0x68, sp + 0x5C, sp + 0x50, bits(radius), bits(threshold),
                        POINTS, POINTS + 64, sp + 0x48, sp + 0x44)
                put(memory, sp + 0x94, POINTS)
                put(memory, sp + 0x98, POINTS + 64)
                put(memory, DISTANCES + 16, bits(radius))
                put(memory, sp + 0x50, bits(center[0]))
            for base, vector in ((args[0], (0.0, 0.0, 0.0)), (args[1], (1.0, 0.0, 0.0)), (args[2], center)):
                for i, value in enumerate(vector): put(memory, base + i * 4, bits(value))
            original = list(struct.unpack_from('>%dI' % count, rom, position))
            self.assertEqual(original[-2], 0x0D45147C)
            self.assertEqual(original[-1], 0xE7A80010 if kind == 0 else 0xAFAA0018)
            original += [0x3C1FDEAD, 0x03E00008, 0]
            expected, _, status, _ = reference(memory, args, phase)
            models = []
            for wrapper in (self.retail, self.words):
                connected = dict(self.connected)
                connected.update(zip(range(screen.ENTRY, screen.ENTRY + 212, 4), wrapper))
                model = SphereOracle(original, memory, (0, 0, 0, 0), connected, phase, entry)
                if kind == 0:
                    model.r[4] = sp + 0x88
                    model.r[16] = model.before[16] = DIRECTION
                else:
                    model.r[16] = model.before[16] = CENTER
                    model.r[25] = DISTANCES + 16
                    model.f[0], model.f[4], model.f[10] = bits(1.0), bits(center[1]), bits(threshold)
                model.run()
                self.assertEqual(model.r[2], status)
                self.assertEqual(model.calls[:2], [(screen.ENTRY, *args), (screen.CALLEE, *args[:4], *args[5:])])
                self.assertEqual(external(model.memory), external(expected))
                for base, count_words in ((args[5], 3), (args[6], 3), (args[7], 1), (args[8], 1)):
                    for i in range(count_words):
                        self.assertEqual(peek(model.memory, base + i * 4), peek(expected, base + i * 4))
                models.append(model)
            self.assertEqual(models[0].memory, models[1].memory)
            self.assertEqual(models[0].events, models[1].events)
            cases += 1
        self.assertEqual(cases, 324)

    def copied_owner(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        baseline = source.replace(screen.SELECTED, STUB).replace(screen.PROTOTYPE, 's32 func_151451F0();')
        selected = baseline.replace(STUB, screen.SELECTED).replace('s32 func_151451F0();', screen.PROTOTYPE)
        objects, warnings = [], []
        for name, body in (('baseline', baseline), ('selected', selected)):
            obj, warning = compile_owner(self.root, self.output, body, 'owner-' + name)
            warnings.append(warning)
            processed = self.output / ('owner-' + name + '-processed.o')
            shutil.copyfile(obj, processed)
            subprocess.run(['python3', str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.output / ('owner-' + name + '.c')).relative_to(self.root / 'conker')),
                '--post-process', str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker',
                check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0], warnings[1])
        self.assertEqual(len(warnings[0]), 2)
        old_text, old_functions, old_rel = parse_object(objects[0])
        text, functions, rel = parse_object(objects[1])
        self.assertEqual(set(functions), set(old_functions))
        self.assertEqual(len(functions), 89)
        for name, meta in functions.items():
            if name == screen.FUNCTION: continue
            old = old_functions[name]
            self.assertEqual(text[meta['value']:meta['value'] + meta['size']], old_text[old['value']:old['value'] + old['size']], name)
            self.assertEqual({o - meta['value']: r for o, r in rel.items() if meta['value'] <= o < meta['value'] + meta['size']},
                {o - old['value']: r for o, r in old_rel.items() if old['value'] <= o < old['value'] + old['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        meta = functions[screen.FUNCTION]
        self.assertEqual(list(struct.unpack_from('>53I', text, meta['value']))[0:11], self.words[0:11])
        _, standalone, raw_rel = parse_object(self.output / 'selected.o')
        raw = parse_object(self.output / 'selected.o')[0]
        self.assertEqual(text[meta['value']:meta['value'] + 212], raw[standalone[screen.FUNCTION]['value']:standalone[screen.FUNCTION]['value'] + 212])
        self.assertEqual({o - meta['value']: r for o, r in rel.items() if meta['value'] <= o < meta['value'] + 212}, raw_rel)
        return objects[1]

    def test_copied_owner_neighbors_pools_relocations_and_warnings(self):
        self.copied_owner()

    def test_actual_padder_complete_direct_slot_and_alternate_call_target(self):
        obj = self.copied_owner()
        assembly = emit_padded_assembly(obj, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=self.root / 'conker/retail_word_patches.us.csv')
        begin = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), begin)
        end = assembly.index('\n', end)
        asm, padded, elf = (self.output / ('padded' + suffix) for suffix in ('.s', '.o', '.elf'))
        asm.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + assembly[begin:end + 1])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(padded), str(asm)], check=True, capture_output=True)
        _, functions, relocations = parse_object(padded)
        self.assertEqual(functions[screen.FUNCTION]['size'], 212)
        self.assertEqual(relocations, self.record['relocations'])
        for target in (screen.CALLEE, screen.CALLEE + 0x100000):
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output / 'selected.ld'),
                '-e', screen.FUNCTION, '--defsym=%s=0x%X' % (screen.CALLEE_FUNCTION, target),
                '-o', str(elf), str(padded)], check=True, capture_output=True)
            expected = self.retail.copy()
            expected[11] = 0x0C000000 | (target >> 2 & 0x3FFFFFF)
            self.assertEqual(list(struct.unpack_from('>53I', screen.sections(elf)['.text'][1])), expected)

    def test_production_complete_direct_slot_typed_abi_and_no_new_guards(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.SELECTED, source)
        self.assertIn(screen.PROTOTYPE, source)
        self.assertNotIn(STUB, source)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        self.assertEqual(len(guards), 11006)
        self.assertFalse(any(g['function'] == screen.FUNCTION for g in guards))


if __name__ == '__main__':
    unittest.main()
