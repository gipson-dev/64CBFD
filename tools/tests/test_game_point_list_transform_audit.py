"""Bounded public effects and the still-open pointer-list saved-register lifetime."""

import csv
import itertools
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_point_list_transform_candidates as screen
from tools.experiments import game_matrix_translation_candidates as translation
from tools.experiments import game_matrix_translation_schedule_candidates as schedule
from tools.match_progress import load_elf_functions
from tools.tests import test_game_matrix_translation_recovery as matrix
from tools.tests import test_game_random_curve_record as native
from tools.tests.game_animation_timeline_oracle import bits, floating, signed
from tools.tests.game_owner_pool import assert_guard_history
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read, external_memory
from tools.tests.test_game_queued_segment_writer import STACK

ACTOR, INPUT, OUTPUT, POINTS, RESULTS, ALTERNATE = 0x20000, 0x22000, 0x23000, 0x24000, 0x25000, 0x26000
ROTATE, TRANSFORM = screen.SYMBOLS.values()
COUNTS = (-0x80000000, -3, -1, 0, 1, 2, 4)


def provider():
    return tuple(bits((i + 1) / 4.0) for i in range(16))


def halves(n):
    return tuple(matrix.half(n * (2 * axis + 1) + axis * 13) for axis in range(3))


def mutations(change):
    if not change:
        return ()
    return ((ACTOR + 0x10, -32768, 2), (ACTOR + 0x12, -1, 2), (ACTOR + 0x14, 32767, 2),
        (INPUT + 4, ALTERNATE, 4), (OUTPUT + 4, ALTERNATE + 128, 4))


def fixture(count=2, n=0, alias=0):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x140)}
    for base in (ACTOR, INPUT, OUTPUT, POINTS, RESULTS, ALTERNATE):
        memory.update({base + i: (i * 31 + 7) & 255 for i in range(-16, 272)})
    for i, value in enumerate(matrix.float_words(n)):
        put(memory, ACTOR + i * 4, value)
    for i, value in enumerate(halves(n)):
        put(memory, ACTOR + 0x10 + i * 2, value, 2)
    for i in range(8):
        for axis in range(3):
            put(memory, POINTS + i * 12 + axis * 4, bits((i * 3 + axis + 1) / 4.0))
            put(memory, ALTERNATE + i * 12 + axis * 4, bits(-i - axis / 4.0 - 1))
        destination = RESULTS + i * 12 if alias == 0 else POINTS + (i + (alias == 2)) * 12
        put(memory, INPUT + i * 4, POINTS + i * 12)
        put(memory, OUTPUT + i * 4, destination)
    return memory, (ACTOR, INPUT, OUTPUT, count & 0xFFFFFFFF)


def transformed(values, coordinates):
    coordinates = tuple(map(floating, coordinates))
    values = tuple(map(floating, values))
    result = []
    for i in range(3):
        first = floating(bits(values[i] * coordinates[0]))
        second = floating(bits(values[i + 4] * coordinates[1]))
        third = floating(bits(values[i + 8] * coordinates[2]))
        left = floating(bits(first + second))
        right = floating(bits(third + values[i + 12]))
        result.append(bits(left + right))
    return tuple(result)


def reference(memory, args, change=False):
    memory = dict(memory)
    actor, input_list, output_list, count = args
    calls = [(ROTATE, tuple(read(memory, actor + i * 4) for i in range(3)))]
    for address, value, size in mutations(change):
        put(memory, address, value, size)
    values = list(provider())
    values[12:15] = (bits(matrix.half(read(memory, actor + 0x10 + i * 2, 2))) for i in range(3))
    for i in range(max(0, signed(count))):
        source = read(memory, input_list + i * 4)
        destination = read(memory, output_list + i * 4)
        coordinates = tuple(read(memory, source + axis * 4) for axis in range(3))
        outputs = tuple(destination + axis * 4 for axis in range(3))
        calls.append((TRANSFORM, tuple(values), coordinates, outputs))
        for address, value in zip(outputs, transformed(values, coordinates)):
            put(memory, address, value)
    return memory, calls


class PointListOracle(TriangleOracle):
    def __init__(self, words, memory, args, change=False, phase=0, connected=None, home=False):
        super().__init__(words, memory, entry=screen.ENTRY, arguments=args, phase=phase, connected=connected)
        self.change, self.phase, self.home = change, phase, home

    def record_call(self, target):
        if target == ROTATE:
            args = self.arguments(4)
            self.matrix = args[0]
            self.calls.append((target, args[1:]))
        else:
            assert target == TRANSFORM
            args = self.arguments(7)
            self.calls.append((target, tuple(read(self.memory, args[0] + i * 4) for i in range(16)), args[1:4], args[4:]))

    def hook(self, target):
        if target == ROTATE:
            for i, value in enumerate(provider()):
                self.put(self.matrix + i * 4, value, 4)
            for address, value, size in mutations(self.change):
                self.put(address, value, size)
            mask = 3 if self.home is True else self.home
            if mask & 1:
                self.put(STACK + self.phase + 4, INPUT + 4, 4)
            if mask & 2:
                self.put(STACK + self.phase + 8, OUTPUT + 4, 4)
        else:
            _, values, coordinates, outputs = self.calls[-1]
            for address, value in zip(outputs, transformed(values, coordinates)):
                self.put(address, value, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]


class GamePointListTransformAuditTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host
    BODY = screen.BASELINE

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-point-list-transform-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'baseline')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>57I', cls.rom, screen.ROM))
        helper = struct.unpack_from('>40I', cls.rom, 0xD4E10)
        cls.connected = dict(zip(range(TRANSFORM, TRANSFORM + 160, 4), helper))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def model(self, words, memory, args, **kwargs):
        return PointListOracle(words, memory, args, **kwargs).run()

    def check_case(self, memory, args, **kwargs):
        expected, calls = reference(memory, args, kwargs.get('change', False))
        models = [self.model(words, memory, args, **kwargs) for words in (self.words, self.retail)]
        for model in models:
            self.assertEqual(external_memory(model.memory), external_memory(expected))
            self.assertEqual(model.calls, calls)
        public = lambda model: [event for event in model.events if not STACK - 0x600 <= event[1] < STACK + 0x140]
        self.assertEqual(public(models[0]), public(models[1]))
        return models

    def test_signed_count_post_provider_reads_and_sequential_point_aliases(self):
        count, coverage = 0, [set(), set()]
        for remaining, n, alias, change, phase in itertools.product(COUNTS, range(16), range(3), (False, True), (0, 8)):
            memory, args = fixture(remaining, n, alias)
            for covered, model in zip(coverage, self.check_case(memory, args, change=change, phase=phase)):
                covered.update(model.visits)
            count += 1
        self.assertEqual(coverage[0], set(range(screen.ENTRY, screen.ENTRY + 228, 4)))
        self.assertEqual(coverage[1], coverage[0])
        self.receipt('effects', dict(cases=count, raw_words=57, raw_differences=46, full_word_coverage=True,
            complete_public_memory_calls_and_trace=True, provider_and_transform_are_bounded_hooks=True))

    def test_connected_original_point_helper_and_nonpositive_count_without_lists(self):
        count, coverage = 0, set()
        for remaining, n, alias, change, phase in itertools.product((1, 2, 4), range(16), range(3), (False, True), (0, 8)):
            memory, args = fixture(remaining, n, alias)
            models = self.check_case(memory, args, change=change, phase=phase, connected=self.connected)
            for model in models:
                coverage.update(model.visits & self.connected.keys())
            count += 1
        for remaining in COUNTS[:4]:
            memory, args = fixture(remaining)
            for address in list(memory):
                if INPUT - 16 <= address < ALTERNATE + 272:
                    del memory[address]
            self.check_case(memory, args, connected=self.connected)
        self.assertEqual(coverage, set(self.connected))
        self.receipt('connected', dict(cases=count + 4, original_helper_words=40, independent_final_storage=True,
            provider_remains_bounded_hook=True, no_hardware_or_general_FCSR_claim=True))

    def test_required_descriptor_lists_points_and_outputs_fail_closed(self):
        count = 0
        for remaining in (0, 2):
            required = [(ACTOR + offset, size) for offset, size in ((0, 4), (4, 4), (8, 4), (0x10, 2), (0x12, 2), (0x14, 2))]
            if remaining:
                required += [(INPUT, 4), (OUTPUT, 4), (POINTS, 4), (RESULTS, 4)]
            for address, size in required:
                memory, args = fixture(remaining)
                for byte in range(size):
                    del memory[address + byte]
                for words in (self.words, self.retail):
                    with self.assertRaises((AssertionError, KeyError)):
                        self.model(words, memory, args, connected=self.connected)
                count += 1
        self.receipt('unmapped', dict(cases=count, fail_closed=True, unused_lists_covered_by_connected_gate=True))

    def test_actual_32bit_c_every_translation_halfword_and_callback_mutation(self):
        self.fixture = r'''typedef unsigned char u8;typedef short s16;typedef int s32;
typedef unsigned int u32;typedef float f32;
typedef struct {f32 unk0,unk4,unk8;} struct17;
typedef char PointerSize[(sizeof(void *)==4)?1:-1];
typedef union {u32 align;u8 bytes[64];} Descriptor;
static Descriptor descriptor;
static struct17 input[5],output[5],*sources[4],*destinations[4];
static u32 expectedAngles[3],matrixWords[16];static s16 expectedHalf[3];
static int rotations,transforms,error,change;
static u32 word(f32 value){union{u32 u;f32 f;} v;v.f=value;return v.u;}
static f32 number(u32 value){union{u32 u;f32 f;} v;v.u=value;return v.f;}
__attribute__((noinline)) void func_150A8050(f32 matrix[4][4],f32 x,f32 y,f32 z){
    int i;
    if(rotations++ || transforms || word(x)!=expectedAngles[0] || word(y)!=expectedAngles[1] || word(z)!=expectedAngles[2])error=1;
    for(i=0;i<16;i++) ((f32 *)matrix)[i]=number(matrixWords[i]);
    if(change){
        for(i=0;i<3;i++) *(s16 *)(descriptor.bytes+16+i*2)=expectedHalf[i];
        sources[1]=input+4;destinations[1]=output+4;
    }
}
__attribute__((noinline)) void func_150A7960(f32 matrix[4][4],f32 x,f32 y,f32 z,f32 *ox,f32 *oy,f32 *oz){
    int i,n=transforms++;struct17 *source=sources[n],*destination=destinations[n];
    if(rotations!=1 || n>=4 || word(x)!=word(source->unk0) || word(y)!=word(source->unk4)
       || word(z)!=word(source->unk8) || ox!=&destination->unk0 || oy!=&destination->unk4 || oz!=&destination->unk8)error=2;
    for(i=0;i<16;i++) if(word(((f32 *)matrix)[i])!=(i>=12&&i<15?word((f32)expectedHalf[i-12]):matrixWords[i]))error=3;
    *ox=x;*oy=y;*oz=z;
}
static void initialize(u32 n,int mode){
    int i;rotations=transforms=error=0;change=mode;
    for(i=0;i<64;i++)descriptor.bytes[i]=(u8)(i*17+13);
    for(i=0;i<3;i++){
        expectedAngles[i]=0x3F000000u+(n+i*13)%0x1000000u;
        *(u32 *)(descriptor.bytes+i*4)=expectedAngles[i];
        expectedHalf[i]=(s16)(n*(2*i+1)+i*13);
        *(s16 *)(descriptor.bytes+16+i*2)=change?7:expectedHalf[i];
    }
    for(i=0;i<16;i++)matrixWords[i]=word((f32)(i+1)/4);
    for(i=0;i<5;i++){
        input[i].unk0=(f32)i+0.25f;input[i].unk4=(f32)i-2;input[i].unk8=(f32)i+3;
        output[i].unk0=output[i].unk4=output[i].unk8=-123;
        if(i<4){sources[i]=input+i;destinations[i]=output+i;}
    }
}
''' + self.BODY + '\n'
        self.run_host(r'''
u32 n;int mode,i,j;static s32 counts[]={(-2147483647-1),-3,-1,0};
for(n=0;n<65536;n++)for(mode=0;mode<2;mode++){
    initialize(n,mode);func_15145CD0(descriptor.bytes,sources,destinations,4);
    if(error || rotations!=1 || transforms!=4)return 1;
    for(i=0;i<4;i++)if(word(destinations[i]->unk0)!=word(sources[i]->unk0)
        || word(destinations[i]->unk4)!=word(sources[i]->unk4) || word(destinations[i]->unk8)!=word(sources[i]->unk8))return 2;
    for(j=0;j<64;j++)if(!((j<12)||(j>=16&&j<22)) && descriptor.bytes[j]!=(u8)(j*17+13))return 3;
    for(i=0;i<5;i++){
        int written=i<4?(i!=1 || !mode):mode;
        if(word(input[i].unk0)!=word((f32)i+0.25f) || word(input[i].unk4)!=word((f32)i-2)
            || word(input[i].unk8)!=word((f32)i+3))return 5;
        if(word(output[i].unk0)!=word(written?input[i].unk0:-123.0f)
            || word(output[i].unk4)!=word(written?input[i].unk4:-123.0f)
            || word(output[i].unk8)!=word(written?input[i].unk8:-123.0f))return 6;
    }
}
for(i=0;i<4;i++){
    initialize(7,1);func_15145CD0(descriptor.bytes,(struct17 **)0,(struct17 **)0,counts[i]);
    if(error || rotations!=1 || transforms)return 4;
}
''')
        self.receipt('native', dict(cases=131076, actual_32bit_C=True, every_halfword_in_each_translation_field=True,
            provider_mutation=True, transform_is_validating_copy_hook=True, not_cartesian_domain=True))

    def test_historical_callback_argument_home_mismatch_remains_reproduced(self):
        detected = 0
        for phase in (0, 8):
            memory, args = fixture(1)
            raw, original = [self.model(words, memory, args, home=True, phase=phase) for words in (self.words, self.retail)]
            self.assertNotEqual(raw.calls, original.calls)
            self.assertNotEqual(external_memory(raw.memory), external_memory(original.memory))
            self.assertEqual(raw.calls[1][2], tuple(read(memory, POINTS + axis * 4) for axis in range(3)))
            self.assertEqual(original.calls[1][2], tuple(read(memory, POINTS + 12 + axis * 4) for axis in range(3)))
            self.assertEqual(raw.calls[1][3], tuple(RESULTS + axis * 4 for axis in range(3)))
            self.assertEqual(original.calls[1][3], tuple(RESULTS + 12 + axis * 4 for axis in range(3)))
            detected += 1
        self.receipt('argument-homes', dict(cases=detected, historical_C_still_differs=True,
            original_reads_spilled_lists_after_provider=True, full_ABI_home_acceptance_not_claimed=True))

    def test_five_compiled_negatives_change_public_storage(self):
        lines = '\n'.join('    mtx[3][%d] = *(s16 *)(arg0 + 0x%X);' % (i, 0x10 + i * 2) for i in range(3)) + '\n'
        forms = dict(unsigned_translation=screen.BASELINE.replace('*(s16 *)', '*(u16 *)'),
            exact_one_count=screen.BASELINE.replace('arg3 > 0', 'arg3 == 1'),
            wrong_input_stride=screen.BASELINE.replace('arg1++;', 'arg1 += 2;'),
            cached_first_source=screen.BASELINE.replace('    while (arg3 > 0)', '    src = *arg1;\n    while (arg3 > 0)').replace('        src = *arg1;\n', ''),
            translation_before_provider=screen.BASELINE.replace(lines, '').replace('    func_150A8050(', lines + '    func_150A8050(', 1))
        detected = {}
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root, self.out, 'negative-' + name, body)
            changed = 0
            for n, alias, change in itertools.product(range(4), range(3), (False, True)):
                memory, args = fixture(2, n, alias)
                expected, _ = reference(memory, args, change)
                model = self.model(words, memory, args, change=change)
                changed += external_memory(model.memory) != external_memory(expected)
            self.assertGreater(changed, 0, name)
            detected[name] = changed
        self.receipt('negatives', dict(count=5, public_storage_changes=detected))

    def test_48_real_loop_lifetime_and_readback_measurements_remain_nonmatching(self):
        records = []
        forms = [(name + '-' + p, body, p) for name, body in screen.candidates() for p in screen.PROFILES]
        forms += [(name, body, 'o2g3') for name, body in itertools.chain(screen.lifetime_candidates(), screen.readback_candidates())]
        self.assertEqual(len(forms), 48)
        for name, body, profile in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile)
            self.assertGreater(record['differences'], 0, name)
            self.assertEqual(record['pool_bytes'], 0, name)
            for count, alias, change in itertools.product((-1, 0, 2), range(3), (False, True)):
                memory, args = fixture(count, 7, alias)
                expected, calls = reference(memory, args, change)
                model = self.model(words, memory, args, change=change)
                self.assertEqual((external_memory(model.memory), model.calls), (external_memory(expected), calls), name)
            records.append(record)
        self.receipt('controls', dict(count=48, measurements=records, public_effect_cases=864, exact=0))

    def test_26_matrix_view_and_backend_controls_do_not_resolve_translation_schedule(self):
        records = []
        forms = [*schedule.typed_candidates(), *schedule.backend_candidates()]
        self.assertEqual(len(forms), 26)
        for name, body, declarations, flags in forms:
            record, words = translation.compile_candidate(self.root, self.out, name, body, declarations=declarations, extra_flags=flags)
            self.assertGreater(record['differences'], 0, name)
            self.assertEqual(record['pool_bytes'], 0, name)
            for flag, n, alias in itertools.product((0, 1, 255), range(4), (None, 0x18)):
                memory, args = matrix.fixture(flag, matrix.edge_pairs(n), matrix.float_words(n), alias=alias)
                expected, events = matrix.reference(memory, args)
                model = TriangleOracle(words, memory, entry=translation.ENTRY, arguments=args).run()
                self.assertEqual(external_memory(model.memory), external_memory(expected), name)
                self.assertEqual([e for e in matrix.public_events(model) if e[0] == 'W'], [e for e in events if e[0] == 'W'], name)
            records.append(record)
        self.assertEqual([(r['body_words'], r['differences']) for r in records[:16]], [(49, 34)] * 16)
        self.receipt('translation-controls', dict(count=26, measurements=records, public_effect_cases=624,
            exact=0, production_profile_unchanged=True, all_public_read_order_identity=False))

    def test_historical_baseline_and_current_installed_match_with_guard_history(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertEqual(source.count(screen.BASELINE), 0)
        self.assertEqual(source.count(screen.SELECTED), 1)
        self.assertEqual(source.count(translation.SELECTED), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (57, 0x88, 46))
        selected, selected_words = screen.compile_candidate(self.root, self.out, 'point-list-production', screen.SELECTED)
        self.assertEqual((selected['body_words'], selected['frame'], selected['differences']), (57, 0x88, 19))
        self.assertEqual(functions[screen.FUNCTION], screen.normalize(selected_words))
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        record, words = translation.compile_candidate(self.root, self.out, 'translation-production')
        self.assertEqual((record['body_words'], record['differences']), (49, 34))
        self.assertEqual(functions[translation.FUNCTION], words)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertEqual([row for row in guards if row['function'] == screen.FUNCTION], screen.owner_guards())
        self.assertFalse(any(row['function'] == translation.FUNCTION for row in guards))


if __name__ == '__main__':
    unittest.main()
