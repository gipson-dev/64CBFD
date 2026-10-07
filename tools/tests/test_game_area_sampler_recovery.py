"""Uninstalled area-sampler C recovery; bounded conversions are not FCSR emulation."""

import csv
import itertools
import json
import math
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_area_sampler_candidates as screen
from tools.experiments import game_area_sampler_lifetime_candidates as lifetimes
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.pad_generated_object import parse_object
from tools.tests.game_owner_pool import normalized_pools, assert_guard_history
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read, external_memory
from tools.tests.test_game_queued_segment_writer import STACK
from tools.tests import test_game_random_curve_record as native

SOURCE, OUTPUT, TABLE, SCALE = 0x20000, 0x24000, 0x8009A220, 0x800A5644
INTEGER, RANDOM, ANGLE = 0x150ADA20, 0x150ADA68, 0x151423D8
HALVES = ((7, 11, -13, 17, 19, 23), (-32768, 32767, -1, -32768, 32767, -1),
          (32767, -32768, 0, 32767, -32768, 32767), (0, 0, 0, 0, 0, 0))


def half(memory, offset):
    value = read(memory, SOURCE + offset, 2)
    return value if value < 32768 else value - 65536


def rounded(value):
    return floating(bits(value))


def converted_angle(value):
    """Retail's fallback result for this bounded, nontrapping conversion model."""
    if not math.isfinite(value): return 255
    integer = math.trunc(value)
    return integer & 255 if 0 <= integer < 2**32 else 255


def angle_value(memory, angle):
    angle &= 255
    index = 64 - (angle & 63) if angle & 64 else angle & 63
    value = read(memory, TABLE + index * 4)
    return value if (angle & 192) in (0, 192) else value ^ 0x80000000


def mutation(memory, call, enabled):
    if enabled:
        put(memory, SOURCE + 6, -17 - call, 2)
        put(memory, SOURCE + 8, 23 + call, 2)
        put(memory, SOURCE + 10, -29 - call, 2)
        put(memory, SOURCE + 0x15, 3, 1)


def fixture(table, scale, mode=0, values=HALVES[0], angle=90.0, alias=0):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x140)}
    for base, length in ((SOURCE, 64), (OUTPUT, 32)):
        memory.update({base + i: 0xA5 for i in range(length)})
    for i, value in enumerate(values): put(memory, SOURCE + i * 2, value, 2)
    put(memory, SOURCE + 0x10, bits(angle))
    put(memory, SOURCE + 0x15, mode, 1)
    for i, word in enumerate(table): put(memory, TABLE + i * 4, word)
    put(memory, SCALE, scale)
    outputs = ((OUTPUT, OUTPUT + 4, OUTPUT + 8, OUTPUT + 12),
               (OUTPUT, OUTPUT, OUTPUT, OUTPUT),
               (SOURCE, SOURCE + 4, SOURCE + 8, SOURCE + 12),
               (OUTPUT, SOURCE, SOURCE + 4, SOURCE + 8))[alias]
    return memory, (SOURCE, *outputs)


def reference(memory, args, random=0x812345FF, samples=(0.25, 0.75), mutate=False):
    memory, calls, writes = memory.copy(), [], []
    mode = read(memory, SOURCE + 0x15, 1) & 3
    sample_index = 0

    def callback(target, argument=None):
        nonlocal sample_index
        calls.append((target, argument))
        if target == INTEGER: result = random
        elif target == ANGLE: result = floating(angle_value(memory, argument))
        else:
            result = samples[sample_index]; sample_index += 1
        mutation(memory, len(calls), mutate)
        return result

    def store(index, value):
        word = bits(value)
        put(memory, args[index + 1], word)
        writes.append(('W', args[index + 1], 4, word))

    if mode == 3:
        store(0, half(memory, 0)); store(1, half(memory, 4))
    else:
        if mode == 2:
            angle = converted_angle(rounded(floating(read(memory, SOURCE + 0x10)) * floating(read(memory, SCALE))))
        else: angle = callback(INTEGER) & 255
        shifted = callback(ANGLE, (angle - 64) & 255)
        direct = callback(ANGLE, angle)
        if mode == 2:
            first = callback(RANDOM)
            radius = half(memory, 6)
            distance = rounded(rounded(first * rounded(2.0 * radius)) + float(-radius))
            second = callback(RANDOM)
            width = half(memory, 10)
            width = rounded(rounded(second * rounded(2.0 * width)) + float(-width))
            store(0, rounded(float(half(memory, 0)) + rounded(rounded(distance * direct) + rounded(width * shifted))))
            store(1, rounded(float(half(memory, 4)) + rounded(rounded(width * direct) - rounded(distance * shifted))))
        else:
            distance = rounded(callback(RANDOM) * float(half(memory, 6)))
            store(0, rounded(float(half(memory, 0)) + rounded(distance * direct)))
            store(1, rounded(float(half(memory, 4)) - rounded(distance * shifted)))
    store(2, half(memory, 2) + half(memory, 8))
    store(3, half(memory, 2) - half(memory, 8) if mode in (1, 3) else half(memory, 2))
    return memory, calls, writes


class AreaOracle(TriangleOracle):
    def __init__(self, words, memory, args, phase=0, random=0x812345FF, samples=(0.25, 0.75),
                 mutate=False, fcsr=0, connected=None, entry=screen.ENTRY):
        super().__init__(words, memory, phase=phase, entry=entry, arguments=args, connected=connected)
        self.random, self.samples, self.sample_index = random, samples, 0
        self.mutate, self.fcsr, self.initial_fcsr = mutate, fcsr, fcsr

    def execute(self, word):
        op, rs, rt, rd, dest, fn = word >> 26, word >> 21 & 31, word >> 16 & 31, word >> 11 & 31, word >> 6 & 31, word & 63
        if op == 17 and rs in (2, 6):
            assert rd == 31
            if rs == 2: self.r[rt] = self.fcsr
            else: self.fcsr = self.r[rt]
        elif op == 17 and rs == 16 and fn == 36:
            assert self.fcsr & 3 == 1, 'conversion must request truncation'
            value = floating(self.f[rd])
            if not math.isfinite(value) or not -(2**31) <= value < 2**31:
                self.fcsr |= 0x40
                self.f[dest] = 0x80000000
            else: self.f[dest] = math.trunc(value) & 0xFFFFFFFF
        elif op == 17 and rs == 16 and fn == 7:
            self.f[dest] = self.f[rd] ^ 0x80000000
        else: super().execute(word)
        self.r[0] = 0

    def record_call(self, target):
        if target == screen.ENTRY:
            self.forwarded = self.arguments(5)
            return
        assert target in (INTEGER, RANDOM, ANGLE)
        assert self.fcsr == self.initial_fcsr, ('conversion control state leaked', target)
        argument = self.r[4] & 255 if target == ANGLE else None
        self.calls.append((target, argument))
        mutation(self.memory, len(self.calls), self.mutate)

    def hook(self, target):
        if target == ANGLE: value = angle_value(self.memory, self.r[4])
        elif target == RANDOM:
            value = bits(self.samples[self.sample_index]); self.sample_index += 1
        else: value = self.random
        for register in (1, 2, 3, *range(4, 16), 24, 25): self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        if target == INTEGER: self.r[2] = value
        else: self.f[0] = value

    def run(self):
        result = super().run()
        assert self.fcsr == self.initial_fcsr
        return result


def writes(model):
    return [event for event in model.events if event[0] == 'W' and not STACK - 0x600 <= event[1] < STACK + 0x140]


class GameAreaSamplerRecoveryTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-area-sampler-test'; cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>254I', cls.rom, screen.ROM))
        address, data = screen.sections(cls.root / 'conker/build/conker.us.elf')['.game_data']
        cls.table = struct.unpack_from('>65I', data, TABLE - address)
        cls.scale = struct.unpack_from('>I', data, SCALE - address)[0]
        cls.angle_words = struct.unpack_from('>27I', cls.rom, 0x16F888)
        cls.connected = dict(zip(range(ANGLE, ANGLE + 108, 4), cls.angle_words))
        cls.directory = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, data):
        (self.output / (name + '.json')).write_text(json.dumps(data, indent=2) + '\n')

    def test_candidate_remains_uninstalled_and_two_words_short(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (252, 80, 109))
        self.assertEqual(self.record['pool_bytes'], 0)
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn('s32 func_151432BC() {\n    return 0;\n}', source)
        self.assertNotIn(screen.SELECTED, source)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        digest = assert_guard_history(self, guards)
        self.receipt('status', dict(candidate_words=252, retail_words=254, frame=80, raw_differences=109,
            installed=False, target_guards=0, guard_count=len(guards), guard_sha256=digest))

    def test_profile_and_storage_controls_do_not_close_the_match(self):
        records = []
        for profile in screen.PROFILES:
            record, _ = screen.compile_candidate(self.root, self.output, 'profile-' + profile, profile=profile)
            records.append(record)
        for name, body, declaration in screen.storage_candidates():
            record, _ = screen.compile_candidate(self.root, self.output, 'storage-' + name, body, declarations=declaration)
            records.append(record)
        self.assertTrue(all(record['differences'] for record in records))
        integer = next(r for r in records if r['name'] == 'storage-int-scale')
        self.assertEqual((integer['body_words'], integer['frame'], integer['differences']), (254, 80, 158))
        self.receipt('controls', dict(measurements=records, installed_profile_change=False))

    def test_scalar_case_lifetimes_preserve_the_same_short_body(self):
        records = []
        forms = list(lifetimes.candidates())
        self.assertEqual(len(forms), 16)
        self.assertEqual(len({body for _, body in forms}), 16)
        for name, body in forms:
            record, words = screen.compile_candidate(self.root, self.output, name, body)
            self.assertEqual((record['body_words'], record['frame'], record['differences']), (252, 80, 109), name)
            self.assertEqual(words, self.words, name)
            self.assertEqual(record['relocations'], self.record['relocations'], name)
            self.assertEqual(record['diagnostics'], '')
            self.assertEqual(record['profile'], 'o2g3')
            records.append(record)
        self.receipt('scalar-lifetimes', dict(controls=16, new_scoped_controls=14,
            all_raw_words_identical=True, measurements=records))

    def test_four_modes_signed_fields_aliases_mutations_and_preserved_state(self):
        coverage, count = [set(), set()], 0
        for mode, values, phase, alias, mutate, random in itertools.product(
                (0, 1, 2, 3, 252, 253, 254, 255), HALVES, (0, 8), range(4), (False, True), (0, 0x812345FF)):
            memory, args = fixture(self.table, self.scale, mode, values, alias=alias)
            expected, calls, output_writes = reference(memory, args, random=random, mutate=mutate)
            for i, words in enumerate((self.words, self.retail)):
                model = AreaOracle(words, memory, args, phase, random=random, mutate=mutate).run()
                self.assertEqual(external_memory(model.memory), external_memory(expected), (mode, values, alias, mutate))
                self.assertEqual(model.calls, calls)
                self.assertEqual(writes(model), output_writes)
                coverage[i].update(model.visits)
            count += 1
        self.receipt('guest', dict(cases=count, candidate_covered_words=len(coverage[0]), retail_covered_words=len(coverage[1]),
            independent_reference=True, external_memory_and_writes=True, aliases=4,
            private_traces_equal=False, rng='bounded sequence', fcsr='bounded truncation only'))

    def test_unsigned_conversion_first_second_failure_paths_and_restore(self):
        coverage = [set(), set()]
        angles = (0.0, -0.0, 0.5, -0.5, -0.999, 90.0, 359.5, 2**31, 2**32 - 512, 2**32,
                  2**33, -1.0, -2**32, math.inf, -math.inf, math.nan)
        for angle, fcsr in itertools.product(angles, (0, 4, 0x800000)):
            memory, args = fixture(self.table, self.scale, 2, angle=angle)
            # Unit conversion controls use an exact multiplier to reach both integer stages.
            put(memory, SCALE, bits(1.0))
            expected, calls, output_writes = reference(memory, args)
            for i, words in enumerate((self.words, self.retail)):
                model = AreaOracle(words, memory, args, fcsr=fcsr).run()
                self.assertEqual(external_memory(model.memory), external_memory(expected))
                self.assertEqual(model.calls, calls)
                self.assertEqual(writes(model), output_writes)
                coverage[i].update(model.visits)
        self.assertNotIn(0x151433F0, coverage[1])
        self.assertTrue(set(range(0x15143388, 0x15143410, 4)) - {0x151433F0} <= coverage[1])
        for mode in (0, 1, 3):
            memory, args = fixture(self.table, self.scale, mode)
            for i, words in enumerate((self.words, self.retail)):
                coverage[i].update(AreaOracle(words, memory, args).run().visits)
        for words, visited in zip((self.words, self.retail), coverage):
            self.assertEqual(visited, set(range(screen.ENTRY, screen.ENTRY + len(words) * 4, 4)) - {0x151433F0})
        self.receipt('conversion', dict(cases=48, additional_mode_cases=3, covered_words=[251, 253], original_unreachable_word='151433F0',
            both_conversion_stages=True, restore_before_callbacks=True, native_invalid_casts=False,
            boundary='bounded control-register/invalid-bit model, not hardware exceptions or general rounding'))

    def test_original_angle_helper_full_quadrant_table_connection(self):
        self.assertEqual((self.table[0], self.table[64]), (bits(1.0), bits(0.0)))
        coverage, count = set(), 0
        for angle, mode, phase in itertools.product(range(256), (0, 1, 2), (0, 8)):
            memory, args = fixture(self.table, self.scale, mode, angle=float(angle))
            put(memory, SCALE, bits(1.0))
            expected, calls, output_writes = reference(memory, args, random=0xABCD0000 | angle)
            for words in (self.words, self.retail):
                model = AreaOracle(words, memory, args, phase, random=0xABCD0000 | angle, connected=self.connected).run()
                self.assertEqual(external_memory(model.memory), external_memory(expected))
                self.assertEqual(model.calls, calls)
                self.assertEqual(writes(model), output_writes)
                coverage.update(model.visits)
            count += 1
        self.assertTrue(set(range(ANGLE, ANGLE + 108, 4)) <= coverage)
        self.receipt('connected-angle', dict(cases=count, angle_helper_words=27, all_helper_words=True,
            rng='bounded sequence', table_words=65, table_source='linked exact Game data'))

    def test_complete_original_descriptor_caller_and_angle_helper(self):
        entry, offset, length, actor = 0x151A8F1C, 0x1D63CC, 20, 0x28000
        caller = struct.unpack_from('>20I', self.rom, offset)
        assembly = (self.root / 'conker/asm/1D4E00.s').read_text().split(
            'glabel func_151A8F1C\n', 1)[1].split('endlabel func_151A8F1C', 1)[0]
        original = [int(w, 16) for w in re.findall(r'/\* [0-9A-F]+ [0-9A-F]+ ([0-9A-F]{8}) \*/', assembly)]
        self.assertEqual(list(caller), original)
        coverage, count = set(), 0
        for mode, values, phase, mutate in itertools.product(range(4), HALVES, (0, 8), (False, True)):
            memory, _ = fixture(self.table, self.scale, mode, values)
            memory.update({actor + i: 0xA5 for i in range(64)})
            put(memory, actor + 0x2C, SOURCE)
            args = (actor, OUTPUT, OUTPUT + 16, OUTPUT + 20)
            forwarded = (SOURCE, OUTPUT, OUTPUT + 8, OUTPUT + 16, OUTPUT + 20)
            expected, calls, output_writes = reference(memory, forwarded, mutate=mutate)
            put(expected, OUTPUT + 4, read(expected, OUTPUT + 16))
            output_writes.append(('W', OUTPUT + 4, 4, read(expected, OUTPUT + 16)))
            for words in (self.words, self.retail):
                connected = dict(self.connected)
                connected.update(zip(range(screen.ENTRY, screen.ENTRY + len(words) * 4, 4), words))
                model = AreaOracle(caller, memory, args, phase, mutate=mutate, connected=connected, entry=entry).run()
                self.assertEqual(model.forwarded, forwarded)
                self.assertEqual(external_memory(model.memory), external_memory(expected))
                self.assertEqual(model.calls, calls)
                self.assertEqual(writes(model), output_writes)
                coverage.update(model.visits)
            count += 1
        self.assertTrue(set(range(entry, entry + length * 4, 4)) <= coverage)
        self.receipt('connected-caller', dict(cases=count, caller_words=20, complete_original_caller=True,
            entry='151A8F1C', original_angle_helper=True, rng='bounded sequence'))

    def test_required_bytes_fail_closed_and_default_avoids_helpers(self):
        for mode, missing in ((3, SOURCE), (0, OUTPUT), (1, SOURCE + 6), (2, SCALE), (2, SOURCE + 0x10)):
            memory, args = fixture(self.table, self.scale, mode)
            del memory[missing]
            with self.assertRaises((KeyError, AssertionError)): AreaOracle(self.words, memory, args).run()
        memory, args = fixture(self.table, self.scale, 3)
        for address in (*range(TABLE, TABLE + 260), *range(SCALE, SCALE + 4), *range(SOURCE + 0x10, SOURCE + 0x14)):
            del memory[address]
        self.assertEqual(AreaOracle(self.words, memory, args).run().calls, [])

    def test_compiled_negative_controls_change_external_contract(self):
        bodies = {
            'zero': 'void func_151432BC(GameAreaSampleDescriptor *source, f32 *x, f32 *z, f32 *top, f32 *bottom) {}',
            'signed-conversion': screen.SELECTED.replace('(u32)(source->angle', '(s32)(source->angle'),
            'wrong-shifted-angle': screen.SELECTED.replace('scratch.unk2F - 64', 'scratch.unk2F'),
            'wrong-bottom': screen.SELECTED.replace('*bottom = source->y;', '*bottom = source->y - source->height;'),
            'unsigned-fields': screen.SELECTED,
            'wrong-span': screen.SELECTED.replace('2.0f * source->radius', '1.0f * source->radius'),
        }
        cases = [fixture(self.table, self.scale, mode, HALVES[1], angle=angle)
                 for mode, angle in itertools.product(range(4), (float(2**31 + 256), -90.0))]
        detections = {}
        for name, body in bodies.items():
            declaration = screen.DECLARATIONS.replace('s16 x,', 'u16 x,') if name == 'unsigned-fields' else screen.DECLARATIONS
            _, words = screen.compile_candidate(self.root, self.output, 'negative-' + name, body, declarations=declaration)
            differences = 0
            for memory, args in cases:
                expected = AreaOracle(self.words, memory, args).run()
                model = AreaOracle(words, memory, args).run()
                differences += (external_memory(model.memory), model.calls, writes(model)) != (
                    external_memory(expected.memory), expected.calls, writes(expected))
            self.assertGreater(differences, 0, name)
            detections[name] = differences
        self.receipt('negative', dict(controls=detections, detection='external memory, outputs or helper calls only'))

    def test_actual_native_32_bit_typed_caller_finite_unsigned_domain(self):
        helper = (self.root / 'conker/src/game_16EE20.c').read_text().split('f32 func_151423D8(u8 arg0) {', 1)[1].split('\n}', 1)[0]
        rows = []
        for mode, values, angle, mutate, alias in itertools.product(range(4), HALVES,
                (0.0, 90.0, 359.5, float(2**31)), (False, True), (0, 1)):
            memory, args = fixture(self.table, self.scale, mode, values, angle, alias)
            expected, calls, _ = reference(memory, args, mutate=mutate)
            rows.append('{%d,{%s},0x%X,%d,%d,{%s},%d}' % (mode, ','.join(map(str, values)), bits(angle), mutate, alias,
                ','.join('0x%X' % read(expected, address) for address in args[1:]), len(calls)))
        self.fixture = '''typedef unsigned char u8;typedef short s16;typedef unsigned short u16;
typedef unsigned int u32;typedef int s32;typedef float f32;
''' + screen.DECLARATIONS + '''typedef struct {
    f32 unk0,unk4;u8 pad8[3],unkB,padC[4];f32 unk10,unk14;u8 pad18[3],unk1B,pad1C[4];
    f32 unk20,unk24,unk28;u8 pad2C[3],unk2F;
} struct209;
static GameAreaSampleDescriptor descriptor;
static int calls,mutationEnabled,sampleIndex,error;
static f32 out[4];
static u32 word(f32 value) {union {f32 f;u32 u;} v;v.f=value;return v.u;}
static f32 fromWord(u32 value) {union {f32 f;u32 u;} v;v.u=value;return v.f;}
static void change(void) {
    calls++;
    if(mutationEnabled) {descriptor.radius=-17-calls;descriptor.height=23+calls;descriptor.width=-29-calls;descriptor.flags=3;}
}
static f32 D_800A5644;
static f32 D_8009A220[65];
s32 func_150ADA20(void) {change();return (s32)0x812345FFu;}
f32 func_150ADA68(void) {f32 v=sampleIndex++?0.75f:0.25f;change();return v;}
static f32 angleReference(u8 arg0) {''' + helper + '''
}
f32 func_151423D8(u8 arg0) {f32 v=angleReference(arg0);change();return v;}
''' + screen.SELECTED + '''
static const u32 table[65]={''' + ','.join('0x%X' % w for w in self.table) + '''};
static const struct {int mode;s16 halves[6];u32 angle;int mutation,alias;u32 expected[4];int calls;} cases[]={
''' + ',\n'.join(rows) + '\n};\n'
        self.run_host('''int i,j;f32 *p[4];
if(sizeof(void *)!=4 || sizeof(GameAreaSampleDescriptor)!=24 || sizeof(struct209)!=48
   || (u32)&descriptor.angle-(u32)&descriptor!=16 || (u32)&descriptor.flags-(u32)&descriptor!=21)return 1;
for(i=0;i<65;i++)D_8009A220[i]=fromWord(table[i]);
D_800A5644=fromWord(0x%X);
for(i=0;i<(int)(sizeof(cases)/sizeof(cases[0]));i++) {
    descriptor.x=cases[i].halves[0];descriptor.y=cases[i].halves[1];descriptor.z=cases[i].halves[2];
    descriptor.radius=cases[i].halves[3];descriptor.height=cases[i].halves[4];descriptor.width=cases[i].halves[5];
    descriptor.flags=cases[i].mode;descriptor.angle=fromWord(cases[i].angle);
    calls=sampleIndex=error=0;mutationEnabled=cases[i].mutation;
    for(j=0;j<4;j++)p[j]=out+(cases[i].alias?0:j);
    func_151432BC(&descriptor,p[0],p[1],p[2],p[3]);
    if(calls!=cases[i].calls)return 2;
    for(j=0;j<4;j++)if(word(*p[j])!=cases[i].expected[j])return 3;
}
''' % self.scale)
        self.receipt('native', dict(cases=len(rows), bits=32, typed_descriptor=True, actual_angle_c_body=True,
            finite_nonnegative_unsigned_casts=True, output_aliases=True, callbacks='bounded deterministic RNG/mutations'))

    def test_copied_owner_target_neighbors_warnings_and_pool_ownership(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        stub = 's32 func_151432BC() {\n    return 0;\n}'
        self.assertEqual(source.count(stub), 1)
        selected = source.replace('/* Generated placeholder declarations. */',
            screen.DECLARATIONS + '\n/* Generated placeholder declarations. */').replace(
            's32 func_151432BC();', screen.PROTOTYPE).replace(stub, screen.SELECTED)
        self.assertIn(screen.DECLARATIONS, selected)
        objects, warnings = [], []
        for name, body in (('baseline', source), ('selected', selected)):
            obj, warning = compile_owner(self.root, self.output, body, 'owner-' + name)
            warnings.append(warning)
            processed = self.output / ('owner-' + name + '-postprocessed.o'); shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.output / ('owner-' + name + '.c')).relative_to(self.root / 'conker')),
                '--post-process', str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker', check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0], warnings[1]); self.assertEqual(len(warnings[0]), 2)
        old_text, old_functions, old_relocs = parse_object(objects[0])
        text, functions, relocs = parse_object(objects[1])
        self.assertEqual(set(old_functions), set(functions))
        for name, function in functions.items():
            if name == screen.FUNCTION: continue
            old = old_functions[name]
            self.assertEqual(text[function['value']:function['value'] + function['size']], old_text[old['value']:old['value'] + old['size']], name)
            self.assertEqual({o - function['value']: r for o, r in relocs.items() if function['value'] <= o < function['value'] + function['size']},
                {o - old['value']: r for o, r in old_relocs.items() if old['value'] <= o < old['value'] + old['size']}, name)
        standalone, standalone_functions, standalone_relocs = parse_object(self.output / 'selected.o')
        target = functions[screen.FUNCTION]; size = standalone_functions[screen.FUNCTION]['size']
        self.assertEqual(text[target['value']:target['value'] + target['size']], standalone[:size])
        self.assertEqual({o - target['value']: r for o, r in relocs.items() if target['value'] <= o < target['value'] + target['size']}, standalone_relocs)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        self.receipt('owner', dict(functions=len(functions), unchanged=len(functions)-1, warnings=2,
            target_identical_to_standalone=True, pool_bytes=len(screen.sections(objects[1])['.rodata'][1]), normalized_pools_equal=True))


if __name__ == '__main__': unittest.main()
