"""Qualify the basis recovery without replacing the still-exact original assembly."""

import csv
import itertools
import json
import math
import re
import shutil
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_vector_basis_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read, external_memory
from tools.tests import test_game_random_curve_record as native
from tools.tests.test_game_queued_segment_writer import STACK

CROSS, NORMALIZE = screen.SYMBOLS.values()
POINT, FIRST, SECOND = 0x20000, 0x20020, 0x20040
CALLER, FOLLOW = 0x1514FB98, 0x1514F8F8
ALIASES = ((FIRST, SECOND), (POINT, SECOND), (FIRST, POINT), (FIRST, FIRST),
           (POINT, POINT), (FIRST, FIRST + 4), (POINT + 4, SECOND), (FIRST, POINT + 4))
VALUES = (0, 0x80000000, bits(1), bits(-1), bits(2.5), bits(-3.5))


def fixture(coordinates, alias=0):
    memory = {POINT + i: (i * 17 + 9) & 255 for i in range(-16, 112)}
    memory.update({STACK + i: 0xA5 for i in range(-0x600, 0x100)})
    for axis, value in enumerate(coordinates):
        put(memory, POINT + axis * 4, value)
    return memory, (POINT, *ALIASES[alias])


def binary(left, right, operation):
    a, b = floating(left), floating(right)
    if operation == 'divide':
        value = a / b if b else (math.nan if not a else math.copysign(math.inf, a * math.copysign(1.0, b)))
    else:
        value = {'add': lambda: a + b, 'subtract': lambda: a - b, 'multiply': lambda: a * b}[operation]()
    return bits(value)


def reference(memory, args):
    memory, calls, writes = dict(memory), [], []
    point, first, second = args

    def store(address, value):
        put(memory, address, value)
        writes.append(('W', address, 4, value))

    values = [read(memory, point + i * 4) for i in range(3)]
    zeros = [i for i, word in enumerate(values) if floating(word) == 0.0]
    if len(zeros) == 3:
        return memory, 0, calls, writes
    if len(zeros) == 2:
        axis = next(i for i in range(3) if i not in zeros)
        a, b = ((1, 2), (0, 2), (0, 1))[axis]
        for i in range(3):
            if i != a:
                store(first + i * 4, 0)
        store(first + a * 4, bits(1))
        for i in range(3):
            if i != b:
                store(second + i * 4, 0)
        store(second + b * 4, bits(1))
    else:
        a, b = (2, 1) if zeros == [2] else (1, 2)
        store(first, bits(1))
        store(first + a * 4, bits(1))
        quotient = binary(read(memory, point + a * 4), read(memory, point + b * 4), 'divide')
        store(first + b * 4, binary(read(memory, point) ^ 0x80000000, quotient, 'subtract'))
        for left, right, destination in ((first, point, second), (second, point, first)):
            calls.append((CROSS, left, right, destination))
            for axis, (j, k) in enumerate(((1, 2), (2, 0), (0, 1))):
                positive = binary(read(memory, left + j * 4), read(memory, right + k * 4), 'multiply')
                negative = binary(read(memory, left + k * 4), read(memory, right + j * 4), 'multiply')
                store(destination + axis * 4, binary(positive, negative, 'subtract'))
        for destination in (first, second):
            calls.append((NORMALIZE, destination, destination, 'private-scales'))
            squares = [binary(read(memory, destination + i * 4), read(memory, destination + i * 4), 'multiply') for i in range(3)]
            squared = binary(binary(squares[0], squares[1], 'add'), squares[2], 'add')
            if floating(squared) != 0.0:
                reciprocal = binary(bits(1), bits(math.sqrt(floating(squared))), 'divide')
                for axis in range(3):
                    store(destination + axis * 4, binary(reciprocal, read(memory, destination + axis * 4), 'multiply'))
    return memory, 1, calls, writes


class BasisOracle(TriangleOracle):
    def __init__(self, words, memory, args, helpers, phase=0, entry=screen.ENTRY, scales=(0x40, 0x3C)):
        super().__init__(words, memory, entry=entry, arguments=args, phase=phase, connected=helpers)
        self.phase, self.scales, self.forward = phase, scales, []

    def execute(self, word):
        op, rs, fs, fd, fn = word >> 26, word >> 21 & 31, word >> 11 & 31, word >> 6 & 31, word & 63
        if op == 17 and rs == 16 and fn == 7:
            self.f[fd] = self.f[fs] ^ 0x80000000
        elif op == 17 and rs == 16 and fn == 4:
            value = floating(self.f[fs])
            assert value >= 0 or math.isnan(value)
            self.f[fd] = bits(math.sqrt(value))
        else:
            super().execute(word)

    def record_call(self, target):
        if target == screen.ENTRY:
            self.forward.append(self.arguments(3))
        elif target == CROSS:
            self.calls.append((target, *self.arguments(3)))
        elif target == NORMALIZE:
            source, destination, length, reciprocal = self.arguments(4)
            self.assert_scales(length, reciprocal)
            self.calls.append((target, source, destination, 'private-scales'))
        else:
            assert target == FOLLOW
            args = self.arguments(7)
            self.forward.append((target, *args[:2], tuple(read(self.memory, args[2] + i * 4) for i in range(3)),
                tuple(read(self.memory, args[3] + i * 4) for i in range(3)), *args[4:]))

    def assert_scales(self, length, reciprocal):
        assert (length, reciprocal) == tuple(self.r[29] + offset for offset in self.scales)

    def hook(self, target):
        assert target == FOLLOW
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]


def public_writes(model):
    return [e for e in model.events if e[0] == 'W' and not STACK - 0x600 <= e[1] < STACK + 0x100]


def scale_offsets(words):
    offsets = []
    for i, word in enumerate(words):
        if word >> 26 == 3 and ((screen.ENTRY + i * 4 + 4) & 0xF0000000 | (word & 0x3FFFFFF) << 2) == NORMALIZE:
            group = words[max(0, i - 10):i + 2]
            offsets.append(tuple(next(w & 65535 for w in reversed(group) if w & 0xFFFF0000 == opcode)
                for opcode in (0x27A60000, 0x27A70000)))
    assert offsets and all(pair == offsets[0] for pair in offsets)
    return offsets[0]


class GameVectorBasisRecoveryTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').exists() or any(shutil.which(n) is None for n in ('mips-linux-gnu-ld', 'cc')):
            raise unittest.SkipTest('IDO/MIPS/native tools unavailable')
        cls.output = cls.root / 'conker/build/game-vector-basis-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>148I', rom, screen.ROM))
        cls.helpers = {}
        for entry, offset, count in ((CROSS, 0x172564, 29), (NORMALIZE, 0x1725D8, 50)):
            cls.helpers.update(zip(range(entry, entry + count * 4, 4), struct.unpack_from('>%dI' % count, rom, offset)))
        cls.caller = list(struct.unpack_from('>25I', rom, 0x17D048))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        owner = (cls.root / 'conker/src/game_16EE20.c').read_text()
        cls.helper_bodies = '\n'.join(re.search(r'(?:s32|void) ' + name + r'\([^;{}]+\) \{\n.*?\n\}', owner, re.S).group(0)
            for name in screen.SYMBOLS)
        cls.fixture = '''typedef unsigned char u8; typedef unsigned int u32; typedef int s32; typedef float f32;
typedef struct { f32 unk0, unk4, unk8; } struct17;
#define NULL ((void *)0)
static f32 sqrtf(f32 value) { f32 result; __asm__("sqrtss %1,%0":"=x"(result):"x"(value));return result; }
static u32 storage[28];
''' + cls.helper_bodies + '\n' + screen.SELECTED + '\n'

    def model(self, words, memory, args, phase=0, entry=screen.ENTRY, extra=None):
        helpers = dict(self.helpers)
        helpers.update(extra or {})
        return BasisOracle(words, memory, args, helpers, phase, entry,
            scales=scale_offsets(words)).run()

    def test_ordinary_source_controls_and_profiles_remain_nonmatching(self):
        groups = (screen.candidates, screen.lifetime_candidates, screen.scalar_candidates,
                  screen.expression_candidates, screen.output_candidates, screen.vector_candidates,
                  screen.register_candidates, screen.coordinate_candidates, screen.workspace_candidates,
                  screen.seed_candidates)
        records, executions = [], 0
        coordinates = ((0, 0, 0), (bits(2), 0, 0), (0, bits(-2), 0), (0, 0, bits(2)),
            (0, bits(2), bits(3)), (bits(2), 0, bits(3)), (bits(2), bits(3), 0),
            (bits(2), bits(3), bits(4)), (0x80000000, bits(2), bits(3)),
            (bits(-3.5), bits(2.5), bits(-1)), (0, 0x80000000, 0), (bits(1), bits(-1), bits(1)))
        for name, body in itertools.chain.from_iterable(group() for group in groups):
            record, words = screen.compile_candidate(self.root, self.output, name, body)
            records.append(record)
            self.assertGreater(record['differences'], 0)
            self.assertEqual(record['diagnostics'], '')
            if name.startswith('expression-0.0-'):
                continue  # Double promotion is a measurement, not this single-precision oracle's contract.
            for point in coordinates:
                memory, args = fixture(point)
                expected, status, calls, writes = reference(memory, args)
                model = self.model(words, memory, args)
                self.assertEqual((external_memory(model.memory), model.r[2], model.calls),
                    (external_memory(expected), status, calls), name)
                executions += 1
        for profile, expected in zip(screen.PROFILES, ((142, 0x48, 116), (141, 0x48, 138), (217, 0x38, 214), (217, 0x38, 214))):
            record, _ = screen.compile_candidate(self.root, self.output, 'profile-' + profile, profile=profile)
            self.assertEqual((record['body_words'], record['frame'], record['differences']), expected)
            records.append(record)
        self.assertEqual((len(records), executions), (186, 2136))
        (self.output / 'measurements.json').write_text(json.dumps(dict(records=records,
            ordinary_public_executions=executions, installed=False), indent=2) + '\n')

    def test_compiled_semantic_negatives_have_actual_output_counterexamples(self):
        examples = ((bits(2), bits(3), bits(4)), (bits(2), 0, bits(3)),
                    (bits(2), bits(3), 0), (0, 0, 0))
        for name, body in screen.negative_candidates():
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            mismatches = []
            for point in examples:
                memory, args = fixture(point)
                expected, status, calls, writes = reference(memory, args)
                model = self.model(words, memory, args)
                if (external_memory(model.memory), model.r[2], model.calls, public_writes(model)) != (
                        external_memory(expected), status, calls, writes):
                    mismatches.append(point)
            self.assertTrue(mismatches, name)

    def test_private_output_overlap_pins_the_unrecovered_layout(self):
        for phase in (0, 8):
            memory, _ = fixture((bits(2), bits(3), bits(4)))
            args = (POINT, STACK + phase - 0x48 + 0x30, SECOND)
            models = [self.model(words, memory, args, phase) for words in (self.retail, self.words)]
            results = [tuple(read(model.memory, args[1] + axis * 4) for axis in range(3)) for model in models]
            self.assertNotEqual(*results)

    def test_measured_source_boundary_is_not_a_matching_conversion(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['pool_bytes'], self.record['diagnostics']), (144, 0x48, 93, 0, ''))
        self.assertEqual(list(self.record['relocations'].values()),
            [[('R_MIPS_26', 'func_151450B4')]] * 2 + [[('R_MIPS_26', 'func_15145128')]] * 2)
        self.assertNotEqual(self.words, self.retail)
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn('#pragma GLOBAL_ASM("asm/nonmatchings/game_16EE20/func_15146078.s")', source)
        self.assertNotIn(screen.SELECTED, source)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        linked, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual((addresses[screen.FUNCTION], linked[screen.FUNCTION]), (screen.ENTRY, self.retail))

    def test_finite_signed_zero_alias_corpus_with_actual_original_helpers(self):
        coverage = [set(), set()]
        cases = 0
        for coordinates, alias, phase in itertools.product(itertools.product(VALUES, repeat=3), range(8), (0, 8)):
            memory, args = fixture(coordinates, alias)
            expected, status, calls, writes = reference(memory, args)
            traces = []
            for i, words in enumerate((self.retail, self.words)):
                model = self.model(words, memory, args, phase)
                self.assertEqual((external_memory(model.memory), model.r[2], model.calls, public_writes(model)),
                    (external_memory(expected), status, calls, writes))
                coverage[i].update(model.visits)
                traces.append([e for e in model.events if not STACK - 0x600 <= e[1] < STACK + 0x100])
            self.assertEqual(traces[0], traces[1])
            cases += 1
        self.assertEqual(cases, 3456)
        self.assertEqual(set(range(screen.ENTRY, screen.ENTRY + 148 * 4, 4)) - coverage[0],
            {screen.ENTRY + offset for offset in (0x68, 0xBC, 0xE4, 0x10C, 0x110, 0x164)})
        self.assertEqual(set(self.helpers) - coverage[0],
            {NORMALIZE + offset for offset in (0xC, 0x10, 0x50, 0x74, 0x78, 0x7C, 0x80, 0x84, 0x88)})

    def test_early_private_byte_reads_are_real_but_publicly_dead(self):
        cases = 0
        coordinates = list(itertools.product((0, bits(2)), repeat=3))
        for words, offsets in ((self.retail, (0x45, 0x46)), (self.words, (0x3A, 0x39))):
            for point, phase, lane, value in itertools.product(coordinates, (0, 8), range(2), range(256)):
                memory, args = fixture(point)
                address = STACK + phase - 0x48 + offsets[lane]
                memory[address] = value
                expected, status, calls, writes = reference(memory, args)
                model = self.model(words, memory, args, phase)
                self.assertEqual((external_memory(model.memory), model.r[2], model.calls, public_writes(model)),
                    (external_memory(expected), status, calls, writes))
                cases += 1
            for point, phase in itertools.product(coordinates, (0, 8)):
                memory, args = fixture(point)
                model = self.model(words, memory, args, phase)
                reads = [e for e in model.events if e[0] == 'R' and e[2] == 1 and STACK - 0x600 <= e[1] < STACK + 0x100]
                expected_offsets = [] if not any(point) else [offsets[1] if point[0] == 0 else offsets[0]]
                self.assertEqual([e[1] - (STACK + phase - 0x48) for e in reads], expected_offsets)
                if reads:
                    del memory[reads[0][1]]
                    with self.assertRaisesRegex(AssertionError, 'unmapped read'):
                        self.model(words, memory, args, phase)
        self.assertEqual(cases, 16384)

    def test_zero_gate_accepts_null_unused_output_storage(self):
        for coordinates, phase in itertools.product(itertools.product((0, 0x80000000), repeat=3), (0, 8)):
            memory, _ = fixture(coordinates)
            for words in (self.retail, self.words):
                model = self.model(words, memory, (POINT, 0, 0), phase)
                self.assertEqual((model.r[2], model.calls, public_writes(model)), (0, [], []))

    def test_nonfinite_and_subnormal_patterns_preserve_zero_classification(self):
        patterns = (0, 0x80000000, 1, 0x80000001, 0x007FFFFF, 0x807FFFFF,
            0x00800000, 0x80800000, bits(1), bits(-1), 0x7F800000, 0xFF800000,
            0x7FC12345, 0xFFC12345, 0x7F812345, 0xFF812345)
        for pattern, axis, signs, phase in itertools.product(patterns, range(3),
                itertools.product((0, 0x80000000), repeat=2), (0, 8)):
            point = list(signs)
            point.insert(axis, pattern)
            memory, args = fixture(point)
            expected, status, calls, writes = reference(memory, args)
            for words in (self.retail, self.words):
                model = self.model(words, memory, args, phase)
                self.assertEqual((external_memory(model.memory), model.r[2], model.calls, public_writes(model)),
                    (external_memory(expected), status, calls, writes))
        for pattern, phase in itertools.product(patterns, (0, 8)):
            memory, args = fixture((pattern,) * 3)
            for words in (self.retail, self.words):
                model = self.model(words, memory, args, phase)
                zero = floating(pattern) == 0.0
                self.assertEqual((model.r[2], [call[0] for call in model.calls]),
                    (0, []) if zero else (1, [CROSS, CROSS, NORMALIZE, NORMALIZE]))

    def test_complete_original_caller_forwards_outputs_and_boolean_gate(self):
        coverage = set()
        for coordinates, phase in itertools.product(itertools.product(VALUES, repeat=3), (0, 8)):
            memory, _ = fixture(coordinates)
            put(memory, POINT + 12, bits(7.5))
            caller_sp = STACK + phase - 0x40
            args = (POINT, 0x123456A7, 0xCAFEBABE)
            outputs = (POINT, caller_sp + 0x34, caller_sp + 0x28)
            expected, status, calls, _ = reference(memory, outputs)
            forwards = []
            for words in (self.retail, self.words):
                connected = dict(self.helpers)
                connected.update(zip(range(screen.ENTRY, screen.ENTRY + len(words) * 4, 4), words))
                model = BasisOracle(self.caller, memory, args, connected, phase, CALLER,
                    (0x34, 0x30) if words is self.retail else (0x40, 0x3C)).run()
                coverage.update(model.visits)
                self.assertEqual(model.calls, calls)
                self.assertEqual(model.forward[0], outputs)
                wanted = [] if not status else [(FOLLOW, POINT + 16, POINT,
                    tuple(read(expected, outputs[1] + i * 4) for i in range(3)),
                    tuple(read(expected, outputs[2] + i * 4) for i in range(3)), bits(7.5), 0xA7, 0xCAFEBABE)]
                self.assertEqual(model.forward[1:], wanted)
                forwards.append(model.forward)
            self.assertEqual(*forwards)
        self.assertTrue(set(range(CALLER, CALLER + 100, 4)) <= coverage)

    def test_actual_32_bit_c_uses_recovered_helpers_and_preserves_storage_fences(self):
        records = []
        for coordinates, alias in itertools.product(itertools.product(VALUES, repeat=3), range(8)):
            memory, args = fixture(coordinates, alias)
            expected, status, _, _ = reference(memory, args)
            records.append('{%s,%s,%s,%s}' % (','.join(str((a - POINT + 16) // 4) for a in args), status,
                '{' + ','.join('0x%Xu' % read(memory, POINT - 16 + i * 4) for i in range(28)) + '}',
                '{' + ','.join('0x%Xu' % read(expected, POINT - 16 + i * 4) for i in range(28)) + '}'))
        self.fixture += '\nstatic const struct { int p,a,b,status;u32 initial[28],expected[28]; } cases[]={\n' + ',\n'.join(records) + '\n};\n'
        self.run_host('''int i,j;
for(i=0;i<1728;i++) {
    for(j=0;j<28;j++) storage[j]=cases[i].initial[j];
    if(func_15146078((f32 *)(storage+cases[i].p),(f32 *)(storage+cases[i].a),(f32 *)(storage+cases[i].b))!=cases[i].status) return 1;
    for(j=0;j<28;j++) if(storage[j]!=cases[i].expected[j]) return 2;
}
''')


if __name__ == '__main__':
    unittest.main()
