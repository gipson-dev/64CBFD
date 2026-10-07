"""Dual matrix routes, lazy point gates, ABI homes and original connected helpers."""

import csv
import itertools
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_matrix_list_transform_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_matrix_translation_recovery as translation
from tools.tests import test_game_point_list_transform_audit as points
from tools.tests.game_animation_timeline_oracle import bits, floating, signed
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read, external_memory, PATTERNS
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly

CONVERT, TRANSFORM, TRANSLATE, FLAG = screen.SYMBOLS.values()
INPUT, OUTPUT, POINTS, RESULTS, ALTERNATE = points.INPUT, points.OUTPUT, points.POINTS, points.RESULTS, points.ALTERNATE
MATRIX, STACK = 0x28000, points.STACK
COUNTS = points.COUNTS
FLOATS = (*PATTERNS, 0xFFC12345, 0x7F812345, 0x00800001, 0x80800001)


def fixture(flag=1, count=2, n=0, mode=0, alias=0):
    memory, _ = points.fixture(count, n)
    memory.update({MATRIX + i: (i * 19 + 5) & 255 for i in range(-16, 160)})
    memory[FLAG] = flag
    values = [bits((i + 1) / 4.0) for i in range(16)]
    if flag:
        integers = [int(floating(word) * 65536) & 0xFFFFFFFF for word in values]
        for i, value in enumerate(integers):
            put(memory, MATRIX + i * 2, value >> 16, 2)
            put(memory, MATRIX + 32 + i * 2, value, 2)
    else:
        for i, value in enumerate(values):
            put(memory, MATRIX + i * 4, value)
    for i in range(8):
        null = mode == 2 and i % 2 == 0 or mode == 3
        source = 0 if null else POINTS + i * 12
        for axis in range(3):
            word = FLOATS[(n + i * 3 + axis) % len(FLOATS)] if mode == 0 else (
                FLOATS[n] if mode == 1 and axis == n % 3 else 0x80000000 if (i + axis) % 2 else 0)
            put(memory, POINTS + i * 12 + axis * 4, word)
            put(memory, ALTERNATE + i * 12 + axis * 4, bits(-i - axis - 1.0))
        destination = (RESULTS + i * 12, POINTS + i * 12, POINTS + (i + 1) * 12, MATRIX + 48)[alias]
        put(memory, INPUT + i * 4, source)
        put(memory, OUTPUT + i * 4, destination)
    return memory, (INPUT, OUTPUT, MATRIX, count & 0xFFFFFFFF)


def convert(memory, destination, source):
    for i in range(16):
        integer = read(memory, source + i * 2, 2) << 16 | read(memory, source + 32 + i * 2, 2)
        put(memory, destination + i * 4, bits(floating(bits(float(signed(integer)))) / 65536.0))


def changes(memory, args, mutate, home, phase):
    if mutate:
        put(memory, INPUT + 4, ALTERNATE)
        put(memory, OUTPUT + 4, ALTERNATE + 128)
        for axis in range(3):
            put(memory, POINTS + axis * 4, bits(axis + 7.0))
    for bit, index in ((1, 0), (2, 1)):
        if home & bit:
            put(memory, STACK + phase + index * 4, args[index] + 4)


def reference(memory, args, mutate=False, home=0, phase=0):
    memory, calls = dict(memory), []
    source, destination, matrix, count = args
    put(memory, STACK + phase, source)
    put(memory, STACK + phase + 4, destination)
    fixed = bool(read(memory, FLAG, 1))
    converted = STACK + phase - 0xA0 + 0x5C
    if fixed:
        calls.append((CONVERT, matrix))
        convert(memory, converted, matrix)
        changes(memory, args, mutate, home, phase)
    # The retail BLEZ delay reloads the source home even for unused lists.
    source = read(memory, STACK + phase)
    if signed(count) > 0:
        destination = read(memory, STACK + phase + 4)
    for i in range(max(0, signed(count))):
        point = read(memory, source + i * 4)
        nonzero = point != 0 and any(floating(read(memory, point + axis * 4)) != 0.0 for axis in range(3))
        output = read(memory, destination + i * 4)
        if nonzero:
            selected = converted if fixed else matrix
            values = tuple(read(memory, selected + j * 4) for j in range(16))
            coordinates = tuple(read(memory, point + axis * 4) for axis in range(3))
            outputs = tuple(output + axis * 4 for axis in range(3))
            calls.append((TRANSFORM, values, coordinates, outputs))
            for address, value in zip(outputs, points.transformed(values, coordinates)):
                put(memory, address, value)
        else:
            calls.append((TRANSLATE, matrix, 0, output))
            memory, _ = translation.reference(memory, (matrix, 0, output))
    return memory, calls


class MatrixListOracle(TriangleOracle):
    def __init__(self, words, memory, args, phase=0, connected=None, mutate=False, home=0, drop_home=0, entry=screen.ENTRY):
        super().__init__(words, memory, entry=entry, arguments=args, phase=phase, connected=connected)
        self.args, self.phase, self.mutate = args, phase, mutate
        self.home, self.drop_home = home, drop_home

    def record_call(self, target):
        if target == screen.ENTRY:
            self.calls.append((target, *self.arguments(4)))
        elif target == CONVERT:
            self.private_matrix, source = self.arguments(2)
            self.calls.append((target, source))
        elif target == TRANSFORM:
            matrix, x, y, z, *outputs = self.arguments(7)
            assert outputs[1] == outputs[0] + 4 and outputs[2] == outputs[0] + 8, 'output tuple'
            self.calls.append((target, tuple(read(self.memory, matrix + i * 4) for i in range(16)),
                (x, y, z), tuple(outputs)))
        else:
            assert target == TRANSLATE
            args = self.arguments(3)
            self.calls.append((target, *args))

    def hook(self, target):
        if target == CONVERT:
            # Use traced reads/writes, preserving SDK's sequential overlap effects.
            destination, source = self.arguments(2)
            for pair in range(8):
                ai, af = source + pair * 4, source + 32 + pair * 4
                first = self.get(ai, 4) & 0xFFFF0000 | self.get(af, 4) >> 16 & 65535
                second = self.get(ai, 4) << 16 & 0xFFFF0000 | self.get(af, 4) & 65535
                for lane, value in enumerate((first, second)):
                    self.put(destination + pair * 8 + lane * 4, bits(floating(bits(float(signed(value)))) / 65536.0), 4)
            changed = dict(self.memory)
            changes(changed, self.args, self.mutate, self.home, self.phase)
            for address, value in changed.items():
                if value != self.memory.get(address):
                    self.put(address, value, 1)
            for bit, index in ((1, 0), (2, 1)):
                if self.drop_home & bit:
                    for i in range(4):
                        del self.memory[STACK + self.phase + index * 4 + i]
        elif target == TRANSFORM:
            _, values, coordinates, outputs = self.calls[-1]
            for address, value in zip(outputs, points.transformed(values, coordinates)):
                self.put(address, value, 4)
        else:
            assert target == TRANSLATE
            _, matrix, index, output = self.calls[-1]
            _, events = translation.reference(self.memory, (matrix, index, output))
            for action, address, size, value in events:
                if action == 'R':
                    assert self.get(address, size) == value
                else:
                    self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]


class GameMatrixListTransformMatchTests(unittest.TestCase):
    run_host = points.GamePointListTransformAuditTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-matrix-list-transform-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected', screen.SELECTED)
        cls.normalized = screen.normalize(cls.words)
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>117I', cls.rom, screen.ROM))
        cls.connected = {}
        for entry, offset, length in ((CONVERT, 0x21D368, 46), (TRANSFORM, 0xD4E10, 40), (TRANSLATE, 0x16F7C4, 49)):
            cls.connected.update(zip(range(entry, entry + length * 4, 4), struct.unpack_from('>%dI' % length, cls.rom, offset)))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def model(self, words, memory, args, **kwargs):
        return MatrixListOracle(words, memory, args, **kwargs).run()

    def check_case(self, memory, args, **kwargs):
        reference_kwargs = {k: v for k, v in kwargs.items() if k in ('phase', 'mutate', 'home')}
        expected, calls = reference(memory, args, **reference_kwargs)
        models = [self.model(words, memory, args, **kwargs) for words in (self.words, self.normalized, self.retail)]
        for model in models:
            self.assertEqual(external_memory(model.memory), external_memory(expected))
            self.assertEqual(model.calls, calls)
        self.assertEqual(models[0].memory, models[1].memory)
        self.assertEqual(models[1].memory, models[2].memory)
        public = lambda model: [event for event in model.events if not STACK - 0x600 <= event[1] < STACK + 0x140]
        self.assertEqual(public(models[0]), public(models[1]))
        self.assertEqual(public(models[1]), public(models[2]))
        return models

    def test_complete_slot_original_frame_homes_matrix_and_closed_normalization(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (117, 0xA0, 19))
        self.assertEqual(self.record['pool_bytes'], 0)
        self.assertEqual(self.normalized, self.retail)
        self.assertEqual(self.words[0], 0x27BDFF60)
        self.assertEqual(self.words[10:12], [0xAFA400A0, 0xAFA500A4])
        self.assertEqual(self.words[14], 0x27B4005C)
        self.assertEqual(self.words[9], 0xF7B40028)
        self.assertEqual(self.words[23], 0x8FB000A4)
        self.assertEqual(self.words[68], 0x8FB000A4)
        self.assertEqual(self.words[21] & 65535, 0xA0)
        self.assertEqual(self.words[66] & 65535, 0xA0)
        self.assertEqual(self.words[109:], self.retail[109:])
        self.assertEqual({self.words[i] for i in (2, 7)}, {self.retail[i] for i in (2, 7)})
        for i, (raw, retail) in enumerate(zip(self.words, self.retail)):
            if i in (2, 7):
                continue
            self.assertEqual(raw >> 26, retail >> 26, i)
            if i in (30, 75):
                self.assertEqual(raw & 0xFFE007FF, retail & 0xFFE007FF)
                self.assertEqual(sorted((raw >> 11 & 31, raw >> 16 & 31)), [0, 20])
            else:
                mask = 0x7FF if raw >> 26 == 0 else 65535
                self.assertEqual(raw & mask, retail & mask, i)
        rows = screen.owner_guards()
        raw, functions, rel = parse_object(self.out / 'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['size'], 468)
        self.assertEqual(len(rows), 19)
        self.assertEqual([int(row['offset'], 16) for row in rows],
            [i * 4 for i, (a, b) in enumerate(zip(self.words, self.retail)) if a != b])
        for row in rows:
            offset = int(row['offset'], 16)
            self.assertNotIn(offset, rel)
            self.assertEqual(struct.unpack_from('>I', raw, offset)[0], int(row['expected'], 16))
            self.assertEqual(row['insert_after'], '')
            self.assertEqual(row['omit'], 'false')
        self.receipt('slot', dict(words=117, frame=160, matrix_offset=92, guards=19,
            GP_cycle=[17, 18], equality_operand_commutations=2, private_offsets_unchanged=True,
            relocations=rel, insertions=0, omissions=0))

    def test_guest_all_paths_float_edges_aliases_mutations_and_complete_word_coverage(self):
        cases, coverage = 0, [set(), set(), set()]
        for flag, count, n, mode, alias, phase in itertools.product((0, 1, 255), COUNTS,
                range(16), range(4), range(4), (0, 8)):
            memory, args = fixture(flag, count, n, mode, alias)
            models = self.check_case(memory, args, phase=phase, mutate=bool(n % 2))
            for visited, model in zip(coverage, models):
                visited.update(model.visits)
            cases += 1
        expected = set(range(screen.ENTRY, screen.ENTRY + 468, 4))
        self.assertEqual(coverage, [expected] * 3)
        self.receipt('guest', dict(cases=cases, all_wrapper_words=117, full_memory_and_public_reads_writes_calls=True,
            signed_zero_subnormal_infinity_quiet_and_signaling_NaN_bits=True, general_FCSR=False))

    def test_connected_original_sdk_point_and_translation_helpers(self):
        cases, coverage = 0, set()
        for flag, count, n, mode, alias, phase in itertools.product((0, 1, 255), (1, 2, 4),
                (0, 1, 6, 7), range(4), range(4), (0, 8)):
            memory, args = fixture(flag, count, n, mode, alias)
            for model in self.check_case(memory, args, phase=phase, connected=self.connected):
                coverage.update(model.visits)
            cases += 1
        self.assertTrue(set(range(CONVERT, CONVERT + 45 * 4, 4)) <= coverage)
        self.assertTrue(set(range(TRANSFORM, TRANSFORM + 40 * 4, 4)) <= coverage)
        self.assertTrue(set(range(TRANSLATE, TRANSLATE + 49 * 4, 4)) <= coverage)
        caller_entry, caller_words, caller_cases = 0x15135424, struct.unpack_from('>23I', self.rom, 0x1628D4), 0
        for flag, n, mode, phase in itertools.product((0, 1, 255), (0, 6, 7), range(4), (0, 8)):
            memory, _ = fixture(flag, 2, n, mode)
            caller_args = (MATRIX, read(memory, INPUT), read(memory, INPUT + 4),
                read(memory, OUTPUT), read(memory, OUTPUT + 4))
            target_args = (STACK + phase - 8, STACK + phase - 16, MATRIX, 2)
            expected_memory = dict(memory)
            for address, value in zip((target_args[0], target_args[0] + 4, target_args[1], target_args[1] + 4),
                    caller_args[1:]):
                put(expected_memory, address, value)
            expected_memory, expected_calls = reference(expected_memory, target_args, phase=phase - 40)
            models = []
            for words in (self.words, self.normalized, self.retail):
                connected = {**self.connected, **dict(zip(range(screen.ENTRY, screen.ENTRY + 468, 4), words))}
                model = self.model(caller_words, memory, caller_args, entry=caller_entry, phase=phase, connected=connected)
                self.assertEqual(model.calls[0], (screen.ENTRY, *target_args))
                self.assertEqual(model.calls[1:], expected_calls)
                self.assertEqual(external_memory(model.memory), external_memory(expected_memory))
                models.append(model)
            self.assertEqual(models[0].memory, models[1].memory)
            self.assertEqual(models[1].memory, models[2].memory)
            caller_cases += 1
        self.receipt('connected', dict(cases=cases, original_converter_slot_words=46,
            executed_converter_body_words=45, point_words=40, translation_words=49, full_memory=True,
            original_complete_caller_words=23, complete_caller_cases=caller_cases, forwarded_inputs_and_return=True,
            converter_mutation_hook_not_applied_to_connected_SDK=True, no_hardware_FCSR_claim=True))

    def test_equality_operand_order_and_private_matrix_point_overlaps(self):
        memory, args = fixture()
        model = MatrixListOracle(self.words, memory, args)
        patterns = [*FLOATS, *(((n << 16) | (n ^ 65535)) for n in range(65536))]
        for word, zero in itertools.product(patterns, (0, 0x80000000)):
            model.f[0], model.f[20] = word, zero
            before = list(model.f)
            model.execute(self.words[30])
            raw_condition = model.condition
            model.execute(self.retail[30])
            self.assertEqual(raw_condition, model.condition)
            self.assertEqual(model.f, before)
        cases = 0
        for flag, count, n, source_offset, output_offset, phase in itertools.product((0, 1, 255),
                (0, 2), range(4), (None, 0, 16, 32, 48), (None, 0, 16, 32, 48), (0, 8)):
            memory, args = fixture(flag, count, n, 1)
            matrix = STACK + phase - 0xA0 + 0x5C
            for i in range(2):
                if source_offset is not None:
                    put(memory, INPUT + i * 4, matrix + source_offset)
                if output_offset is not None:
                    put(memory, OUTPUT + i * 4, matrix + output_offset)
            self.check_case(memory, args, phase=phase, connected=self.connected)
            cases += 1
        self.receipt('private', dict(equality_bit_patterns=len(patterns), equality_cases=len(patterns)*2,
            unchanged_FP_bits=True, private_overlap_cases=cases, full_memory=True, actual_original_helpers=True,
            matrix_offset=92, no_private_offset_normalization=True, FCSR_flags_traps_and_rounding_modes_not_modeled=True))

    def test_incoming_home_readbacks_required_storage_and_nonpositive_lazy_lists(self):
        cases = 0
        for count, n, alias, home, phase in itertools.product(COUNTS, range(8), range(4), (1, 2, 3), (0, 8)):
            memory, args = fixture(1, count, n, 1, alias)
            self.check_case(memory, args, phase=phase, mutate=True, home=home)
            cases += 1
        removed = 0
        for count, drop, phase in itertools.product(COUNTS, (1, 2, 3), (0, 8)):
            memory, args = fixture(1, count)
            for words in (self.words, self.normalized, self.retail):
                if drop & 1 or signed(count) > 0:
                    with self.assertRaises((AssertionError, KeyError)):
                        self.model(words, memory, args, phase=phase, drop_home=drop)
                else:
                    self.model(words, memory, args, phase=phase, drop_home=drop)
            removed += 1
        unused = 0
        for flag, count in itertools.product((0, 1, 255), COUNTS[:4]):
            memory, args = fixture(flag, count)
            for address in list(memory):
                if INPUT - 16 <= address < ALTERNATE + 272:
                    del memory[address]
            self.check_case(memory, (0, 0, MATRIX, args[3]), connected=self.connected)
            unused += 1
        required = 0
        for flag, missing in ((0, FLAG), (1, MATRIX), (0, INPUT), (0, OUTPUT),
                (0, POINTS), (0, POINTS + 4), (0, POINTS + 8), (0, RESULTS)):
            memory, args = fixture(flag, 1, 6, 1)
            del memory[missing]
            for words in (self.words, self.normalized, self.retail):
                with self.assertRaises((AssertionError, KeyError)):
                    self.model(words, memory, args, connected=self.connected)
            required += 1
        self.receipt('homes', dict(readback_cases=cases, removed_home_cases=removed,
            unused_null_list_cases=unused, required_storage_cases=required,
            source_home_always_required_after_conversion=True, destination_home_positive_only=True))

    def test_source_forms_profiles_and_effective_public_storage_negatives(self):
        forms = [(n, b, 'o2g3') for group in (screen.candidates, screen.lifetime_candidates,
            screen.view_candidates, screen.scalar_candidates, screen.comparison_candidates) for n, b in group()]
        forms += [('profile-' + profile, screen.BASELINE, profile) for profile in screen.PROFILES]
        self.assertEqual(len(forms), 182)
        records = []
        for name, body, profile in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile)
            self.assertGreater(record['differences'], 0)
            self.assertEqual(record['pool_bytes'], 0)
            for flag, count, mode in itertools.product((0, 1), (-1, 0, 2), (0, 2)):
                memory, args = fixture(flag, count, 6, mode)
                expected, calls = reference(memory, args)
                model = self.model(words, memory, args)
                self.assertEqual((external_memory(model.memory), model.calls), (external_memory(expected), calls), name)
            records.append(record)
        negatives = dict(wrong_flag_gate=screen.SELECTED.replace('D_800C3E90 != 0', 'D_800C3E90 == 0'),
            wrong_count_gate=screen.SELECTED.replace('count > 0', 'count == 1'),
            wrong_source_stride=screen.SELECTED.replace('input++;', 'input += 2;'),
            wrong_destination_stride=screen.SELECTED.replace('destinations++;', 'destinations += 2;'),
            wrong_zero_gate=screen.SELECTED.replace('point->unk8 != 0.0f', 'point->unk8 == 0.0f'),
            wrong_translation_index=screen.SELECTED.replace('matrix, 0, (f32 *)', 'matrix, 1, (f32 *)'),
            wrong_matrix_route=screen.SELECTED.replace('func_150A7960(converted,', 'func_150A7960((f32 (*)[4])matrix,'),
            cached_argument_homes=screen.BASELINE)
        detected = {}
        for name, body in negatives.items():
            _, words = screen.compile_candidate(self.root, self.out, 'negative-' + name, body)
            changed = 0
            for flag, mode, n in itertools.product((0, 1), (0, 1, 2, 3), (0, 6, 7)):
                memory, args = fixture(flag, 2, n, mode)
                expected, _ = reference(memory, args, mutate=True, home=3)
                model = self.model(words, memory, args, mutate=True, home=3)
                changed += external_memory(model.memory) != external_memory(expected)
            self.assertGreater(changed, 0, name)
            detected[name] = changed
        self.receipt('controls', dict(measurements=records, count=182, candidate_executions=2184,
            raw_exact=0, negatives=detected, all_negatives_detected=True))

    def test_actual_native_32bit_sdk_conversion_count_point_modes_and_sequential_aliases(self):
        sdk = (self.root / 'conker/src/libultra/gu/mtxutil2.c').read_text().split('void guMtxL2F', 1)[1]
        self.fixture = r'''typedef unsigned char u8;typedef int s32;typedef unsigned int u32;typedef float f32;
typedef struct {f32 unk0,unk4,unk8;} struct17;
typedef union {s32 m[4][4];double alignment;} Mtx;
typedef union {Mtx fixed;f32 floating[16];u32 words[16];} Matrix;
void guMtxL2F(f32 matrix[4][4],Mtx *fixed);
''' + screen.DECLARATIONS + r'''
u8 D_800C3E90;
static Matrix matrix;static struct17 inputStore[8],outputStore[8],expectedInput[8],expectedOutput[8];
static struct17 *inputs[8],*outputs[8];static int error,conversions,transforms,translations,index,mode,alias;
static f32 values[16];static u32 matrixBefore[16];
static u32 word(f32 f){union{f32 f;u32 u;}v;v.f=f;return v.u;}
void sdkMtxL2F''' + sdk + r'''
void guMtxL2F(f32 output[4][4],Mtx *source){
    if(source!=&matrix.fixed||transforms||translations)error=1;
    conversions++;sdkMtxL2F(output,source);
}
static int nonzero(int i){
    return mode!=3 && !(mode==2 && i%2==0) &&
        (expectedInput[i].unk0!=0.0f||expectedInput[i].unk4!=0.0f||expectedInput[i].unk8!=0.0f);
}
static void expectedTransform(f32 x,f32 y,f32 z,f32 *out){
    int i;for(i=0;i<3;i++)out[i]=(values[i]*x+values[i+4]*y)+(values[i+8]*z+values[i+12]);
}
void func_150A7960(f32 m[4][4],f32 x,f32 y,f32 z,f32 *ox,f32 *oy,f32 *oz){
    f32 result[3];struct17 *actual=outputs[index];int i;
    if(!nonzero(index)||ox!=&actual->unk0||oy!=&actual->unk4||oz!=&actual->unk8 ||
       word(x)!=word(expectedInput[index].unk0)||word(y)!=word(expectedInput[index].unk4)||
       word(z)!=word(expectedInput[index].unk8)||conversions!=(D_800C3E90?1:0))error=2;
    for(i=0;i<16;i++)if(word(((f32 *)m)[i])!=word(values[i]))error=3;
    expectedTransform(x,y,z,result);
    {struct17 *expected=alias?expectedInput+index+(alias==2):expectedOutput+index;
    expected->unk0=result[0];expected->unk4=result[1];expected->unk8=result[2];}
    *ox=result[0];*oy=result[1];*oz=result[2];transforms++;index++;
}
void func_15142314(u8 *m,s32 offset,f32 *out){
    struct17 *actual=outputs[index],*expected=alias?expectedInput+index+(alias==2):expectedOutput+index;
    if(nonzero(index)||m!=(u8 *)&matrix||offset||out!=&actual->unk0||conversions!=(D_800C3E90?1:0))error=4;
    expected->unk0=out[0]=values[12];expected->unk4=out[1]=values[13];expected->unk8=out[2]=values[14];
    translations++;index++;
}
static void initialize(u32 n,int fixed,int route,int overlap){
    int i,a;u32 packed[16];mode=route;alias=overlap;D_800C3E90=fixed?(u8)(n%255+1):0;
    error=conversions=transforms=translations=index=0;
    for(i=0;i<16;i++){packed[i]=((n*(u32)(2*i+1)+(u32)i*13)<<16)|
        ((n*(u32)(17+i*12)+3u)&65535u);
        values[i]=(f32)(s32)packed[i]/65536.0f;}
    for(i=0;i<8;i++){
        if(fixed){matrix.words[i]=(packed[i*2]&0xFFFF0000u)|(packed[i*2+1]>>16);
            matrix.words[i+8]=(packed[i*2]<<16)|(packed[i*2+1]&65535u);}
        else{matrix.floating[i*2]=values[i*2];matrix.floating[i*2+1]=values[i*2+1];}
    }
    for(i=0;i<16;i++)matrixBefore[i]=matrix.words[i];
    for(i=0;i<8;i++){
        for(a=0;a<3;a++){((f32 *)&inputStore[i])[a]=(mode==0||(mode==1&&a==(int)(n%3)))?(f32)(i+a+1)*0.25f:0.0f;
            ((f32 *)&outputStore[i])[a]=-123.0f;}
        expectedInput[i]=inputStore[i];expectedOutput[i]=outputStore[i];
        inputs[i]=(mode==3||(mode==2&&i%2==0))?(struct17 *)0:inputStore+i;
        outputs[i]=alias?inputStore+i+(alias==2):outputStore+i;
    }
}
static int check(int count){
    int i,a;if(error||conversions!=(D_800C3E90?1:0)||transforms+translations!=count||index!=count||sizeof(void *)!=4)return 1;
    for(i=0;i<8;i++)for(a=0;a<3;a++)if(word(((f32 *)&inputStore[i])[a])!=word(((f32 *)&expectedInput[i])[a])||
        word(((f32 *)&outputStore[i])[a])!=word(((f32 *)&expectedOutput[i])[a]))return 2;
    for(i=0;i<16;i++)if(matrix.words[i]!=matrixBefore[i])return 3;
    return 0;
}
''' + screen.SELECTED + '\n'
        self.run_host(r'''
u32 n;int fixed,route,overlap,i;static s32 counts[]={(-2147483647-1),-3,-1,0};
for(n=0;n<65536;n++)for(fixed=0;fixed<2;fixed++)for(route=0;route<4;route++)for(overlap=0;overlap<3;overlap++){
    initialize(n,fixed,route,overlap);
    func_15145EA4(inputs,outputs,(u8 *)&matrix,4);
    if(check(4))return 1;
}
for(fixed=0;fixed<2;fixed++)for(i=0;i<4;i++){
    initialize(7,fixed,0,0);
    func_15145EA4((struct17 **)0,(struct17 **)0,(u8 *)&matrix,counts[i]);
    if(check(0))return 2;
}
''')
        self.receipt('native', dict(cases=1572872, bits=32, actual_SDK_conversion=True,
            count_and_point_routes=True, all_255_nonzero_flags=True, sequential_point_output_aliases=True,
            every_high_and_low_halfword_each_of_16_fixed_fields=True, correlated_not_cartesian_matrix_domain=True,
            complete_records_and_matrix_fences=True, native_transform_and_translation_are_bounded_hooks=True,
            general_FCSR_and_64bit_port_acceptance=False))

    def test_copied_owner_padder_neighbors_and_independent_relocations(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        old = '/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15145EA4.s. */\ns32 func_15145EA4() {\n    return 0;\n}'
        if screen.SELECTED in source:
            source = source.replace(screen.SELECTED, old).replace(screen.PROTOTYPE, 's32 func_15145EA4();')
        self.assertIn(old, source)
        selected = source.replace(old, screen.SELECTED).replace('s32 func_15145EA4();', screen.PROTOTYPE)
        objects, warnings = [], []
        for name, body in (('baseline', source), ('selected', selected)):
            obj, diagnostic = compile_owner(self.root, self.out, body, 'owner-' + name)
            warnings.append(diagnostic)
            processed = self.out / ('owner-' + name + '-postprocessed.o')
            shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.out / ('owner-' + name + '.c')).relative_to(self.root / 'conker')), '--post-process',
                str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker', check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0], warnings[1])
        self.assertEqual(len(warnings[0]), 2)
        old_text, old_functions, old_rel = parse_object(objects[0])
        text, functions, rel = parse_object(objects[1])
        self.assertEqual(set(functions), set(old_functions))
        self.assertEqual(len(functions), 89)
        for name, current in functions.items():
            if name == screen.FUNCTION:
                continue
            previous = old_functions[name]
            self.assertEqual(text[current['value']:current['value'] + current['size']],
                old_text[previous['value']:previous['value'] + previous['size']], name)
            self.assertEqual({o - current['value']: r for o, r in rel.items() if current['value'] <= o < current['value'] + current['size']},
                {o - previous['value']: r for o, r in old_rel.items() if previous['value'] <= o < previous['value'] + previous['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        target = functions[screen.FUNCTION]
        standalone, _, relocs = parse_object(self.out / 'selected.o')
        self.assertEqual(text[target['value']:target['value'] + 468], standalone[:468])
        self.assertEqual({o - target['value']: r for o, r in rel.items() if target['value'] <= o < target['value'] + 468}, relocs)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = [row for row in csv.DictReader(stream) if row['function'] != screen.FUNCTION]
        guards += screen.owner_guards()
        guard_path = self.out / 'guards.csv'
        with guard_path.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(guards[0]))
            writer.writeheader()
            writer.writerows(guards)
        assembly = emit_padded_assembly(objects[1], self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=guard_path)
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        end = assembly.index('\n', end) + 1
        asm, obj = self.out / 'padded.s', self.out / 'padded.o'
        asm.write_text('.text\n.globl %s\n' % screen.FUNCTION + assembly[start:end])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(asm)], check=True, capture_output=True)
        _, padded_functions, padded_relocs = parse_object(obj)
        self.assertEqual(padded_functions[screen.FUNCTION]['size'], 468)
        self.assertEqual(padded_relocs, relocs)
        for rebased in (None, *screen.SYMBOLS):
            targets = dict(screen.SYMBOLS)
            if rebased:
                targets[rebased] += 0x01008004
            elf = self.out / ('rebased-%s.elf' % rebased)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'matrix-list.ld'),
                '-e', screen.FUNCTION, *['--defsym=%s=0x%X' % item for item in targets.items()],
                '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = list(self.retail)
            for offset, relocations in relocs.items():
                kind, name = relocations[0]
                address = targets[name]
                expected[offset // 4] = (expected[offset // 4] & 0xFC000000 | address >> 2 & 0x3FFFFFF) if kind == 'R_MIPS_26' else (
                    expected[offset // 4] & 0xFFFF0000 | ((address + 0x8000) >> 16 & 65535 if kind == 'R_MIPS_HI16' else address & 65535))
            self.assertEqual(list(struct.unpack_from('>117I', screen.sections(elf)['.text'][1])), expected)
        self.receipt('owner', dict(functions=89, unchanged_neighbors=88, warnings=2, new_warnings=0,
            normalized_pools_equal=True, actual_padder_words=117, independently_rebased_symbols=4,
            retained_all_seven_relocations=True))

    def test_installed_complete_slot_and_guard_history(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.SELECTED, source)
        self.assertEqual(source.count(screen.PROTOTYPE), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertEqual(guards[11042:], screen.owner_guards())


if __name__ == '__main__':
    unittest.main()
