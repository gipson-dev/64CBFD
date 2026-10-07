"""Qualify uninstalled oriented-matrix candidates; do not claim byte matching."""

import itertools
import json
import math
import re
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_oriented_matrix_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.pad_generated_object import parse_object
from tools.tests import test_game_random_curve_record as native
from tools.tests import test_game_scaled_matrix_match as scaled
from tools.tests.test_game_timed_interpolation_match import InterpolationOracle, rounded_bits
from tools.tests.test_game_grid_channel_updater_match import STACK, external, put, read
from tools.tests.game_animation_timeline_oracle import bits, floating

CALLER, CONVERT = 0x150B9D14, 0x150A7790
ACTOR, OUTPUT = 0x20000, 0x24000
OFFSETS = (0x18, 0x1C, 0x2C, 0x30, 0x34, 0x38, 0x3C, 0x40, 0x20, 0x24, 0x28)


def fp(value):
    return floating(rounded_bits(value))


def divide(left, right):
    if right == 0:
        if left == 0 or math.isnan(left):
            return math.nan
        return math.copysign(math.inf, math.copysign(1, left) * math.copysign(1, right))
    return fp(left / right)


def root(value):
    return fp(math.sqrt(value)) if value >= 0 else math.nan


def reference(args):
    row0, row1, cx, cy, cz, sx, sy, sz, ex, ey, ez = map(floating, args[1:])
    dx, dy, dz = fp(ex - sx), fp(ey - sy), fp(ez - sz)
    inverse = divide(1, root(fp(fp(fp(dx * dx) + fp(dy * dy)) + fp(dz * dz))))
    x, y, z = fp(dx * inverse), fp(dy * inverse), fp(dz * inverse)
    lx, lz = z, -x
    inverse = divide(1, root(fp(fp(lx * lx) + fp(lz * lz))))
    lx, lz = fp(lx * inverse), fp(lz * inverse)
    ux = fp(y * lz)
    uy = fp(fp(z * lx) - fp(x * lz))
    uz = fp(-y * lx)
    inverse = divide(1, root(fp(fp(fp(ux * ux) + fp(uy * uy)) + fp(uz * uz))))
    values = [0] * 16
    for column, factor in enumerate((cx, cy, cz)):
        values[column] = rounded_bits(fp(fp((lx, 0, lz)[column] * factor) * row0)) if column != 1 else 0
        values[4 + column] = rounded_bits(fp(fp(fp((ux, uy, uz)[column] * inverse) * factor) * row1))
        values[8 + column] = rounded_bits(fp(fp((x, y, z)[column] * factor) * row0))
    values[12:15] = args[6:9]
    values[15] = bits(1)
    return tuple(values)


def cases():
    starts = ((7, -9, 11), (-0.0, 0, -0.0))
    deltas = ((0, 0, 4), (4, 0, 0), (-4, 0, 0), (0, 0, -4), (3, 2, 4),
              (-3, 7, -2), (0, 4, 0), (0, 0, 0))
    for rows, column, index in itertools.product(((1, 2), (-2, 0.25), (-0.0, 0)),
            ((2, -0.5, 3), (-2, 0.25, -1), (0, 0, 0)), range(8)):
        start = starts[index % 2]
        end = tuple(fp(a + b) for a, b in zip(start, deltas[index]))
        yield (OUTPUT, *map(bits, (*rows, *column, *start, *end)))
    for index, value in itertools.product(range(1, 12), scaled.PATTERNS):
        args = [OUTPUT, *map(bits, (1, 2, 2, -0.5, 3, 7, -9, 11, 10, -7, 15))]
        args[index] = value
        yield tuple(args)


def memory_case(args):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x100)}
    for base in (ACTOR, OUTPUT):
        memory.update({base + i: (i * 31 + 7) & 255 for i in range(-16, 256)})
    for offset, value in zip(OFFSETS, args[1:]):
        put(memory, ACTOR + offset, value)
    return memory


def equal_word(left, right):
    return left == right or math.isnan(floating(left)) and math.isnan(floating(right))


def arithmetic_index(index):
    return index < 12 and index % 4 < 3


class OrientedOracle(InterpolationOracle):
    def __init__(self, words, memory, args, phase=0, connected=None, mutation=False):
        super().__init__(words, memory, ACTOR, (), 0, phase=phase)
        self.entry = screen.ENTRY
        self.code = {screen.ENTRY + i * 4: word for i, word in enumerate(words)}
        self.code.update(connected or {})
        self.r[4:8] = self.before[4:8] = args[:4]
        for i, value in enumerate(args[4:]):
            put(self.memory, STACK + phase + 16 + i * 4, value)
        self.mutation = mutation

    def execute(self, word):
        if word >> 26 == 17 and word >> 21 & 31 == 16 and word & 63 in (3, 4, 7, 36):
            fs, ft, fd, fn = word >> 11 & 31, word >> 16 & 31, word >> 6 & 31, word & 63
            value = floating(self.f[fs])
            if fn == 7:
                self.f[fd] = self.f[fs] ^ 0x80000000
            elif fn == 36:
                assert math.isfinite(value) and value == int(value) and -0x80000000 <= value <= 0x7FFFFFFF
                self.f[fd] = int(value) & 0xFFFFFFFF
            else:
                self.f[fd] = rounded_bits(divide(value, floating(self.f[ft])) if fn == 3 else root(value))
        else:
            super().execute(word)

    def record_call(self, target):
        if target == screen.ENTRY:
            self.forwarded = self.arguments(12)
            return
        assert target == CONVERT
        matrix, output = self.arguments(2)
        values = tuple(self.get(matrix + i * 4, 4) for i in range(16))
        self.calls.append((values, output, external(self.memory)))

    def hook(self, target):
        assert target == CONVERT
        values, output, _ = self.calls[-1]
        if self.mutation:
            for offset in OFFSETS:
                self.put(ACTOR + offset, 0xA5000000 + offset, 4)
        for i, value in enumerate(values):
            self.put(output + i * 4, value, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]


def native_fixture(inputs):
    tables = ['static u32 inputs[][11] = {', *['{' + ','.join('0x%Xu' % v for v in a[1:]) + '},' for a in inputs], '};',
        'static u32 expectations[][16] = {', *['{' + ','.join('0x%Xu' % v for v in reference(a)) + '},' for a in inputs], '};']
    return r'''typedef unsigned char u8;typedef unsigned int u32;typedef int s32;typedef float f32;
typedef struct {f32 unk0,unk4,unk8;} struct17;
typedef struct {u32 words[16];} Mtx;
typedef union {u32 align;u8 bytes[384];} Bank;
static Bank live,wanted;static u8 *source;static Mtx *output;
static int current,change,stage,error;
static int offsets[11]={0x18,0x1C,0x2C,0x30,0x34,0x38,0x3C,0x40,0x20,0x24,0x28};
static u32 word(f32 value) {union {u32 u;f32 f;} w;w.f=value;return w.u;}
static int nanWord(u32 value) {return (value&0x7FFFFFFF)>0x7F800000;}
static int equal(u32 a,u32 b) {return a==b || (nanWord(a)&&nanWord(b));}
f32 sqrtf(f32 x) {f32 result;__asm__("sqrtss %1,%0":"=x"(result):"x"(x));return result;}
''' + '\n'.join(tables) + r'''
static void mutate(Bank *bank) {
    int i;if(!change)return;
    for(i=0;i<11;i++) *(u32 *)(bank->bytes+16+offsets[i])=0xA5000000u+offsets[i];
}
static void initialize(int n,int alias,int mutation) {
    int i,offset;current=n;change=mutation;stage=error=0;source=live.bytes+16;
    output=(Mtx *)(live.bytes+(alias==0?192:alias==1?40:48));
    for(i=0;i<384;i++)live.bytes[i]=(u8)(i*31+7);
    for(i=0;i<11;i++)*(u32 *)(source+offsets[i])=inputs[n][i];
    for(i=0;i<384;i++)wanted.bytes[i]=live.bytes[i];
    mutate(&wanted);offset=(u8 *)output-live.bytes;
    for(i=0;i<16;i++)*(u32 *)(wanted.bytes+offset+i*4)=expectations[n][i];
}
__attribute__((noinline)) void guMtxF2L(f32 matrix[4][4],Mtx *destination) {
    int i;if(stage++ || destination!=output)error=1;
    for(i=0;i<16;i++) {
        u32 value=word(((f32 *)matrix)[i]),expected=expectations[current][i];
        if(i<12 && i%4<3? !equal(value,expected):value!=expected)error=2;
    }
    mutate(&live);
    for(i=0;i<16;i++)destination->words[i]=word(((f32 *)matrix)[i]);
}
static int check(void) {
    int i,offset=(u8 *)output-live.bytes;
    if(error || stage!=1)return 1;
    for(i=0;i<384;i++) {
        if(i>=offset && i<offset+48 && (i-offset)%16<12 && (i-offset)%4==0) {
            if(!equal(*(u32 *)(live.bytes+i),*(u32 *)(wanted.bytes+i)))return 2;
            i+=3;
        } else if(live.bytes[i]!=wanted.bytes[i])return 3;
    }
    return 0;
}
''' + screen.SELECTED + '\n' + screen.CALLER + '\n'


class GameOrientedMatrixRecoveryTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-oriented-matrix-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.challenger_body = dict(screen.candidates())['up1-columns1-early0']
        cls.challenger_record, cls.challenger = screen.compile_candidate(cls.root, cls.output, 'challenger', cls.challenger_body)
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>142I', cls.rom, screen.ROM))
        cls.caller = list(struct.unpack_from('>30I', cls.rom, 0xE71C4))
        cls.converter = list(struct.unpack_from('>115I', cls.rom, 0xD4C40))
        cls.inputs = list(cases())
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = native_fixture(cls.inputs)

    def receipt(self, name, value):
        (self.output / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def compare(self, args, phase=0, caller=False, fixed=False, mutation=False):
        memory = memory_case(args)
        values = reference(args)
        wanted = dict(memory)
        if mutation:
            for offset in OFFSETS:
                put(wanted, ACTOR + offset, 0xA5000000 + offset)
        payload = scaled.fixed_payload(values) if fixed else struct.pack('>16I', *values)
        for i, value in enumerate(payload):
            wanted[args[0] + i] = value
        connected = {}
        if caller:
            connected.update({CALLER + i * 4: w for i, w in enumerate(self.caller)})
        if fixed:
            connected.update({CONVERT + i * 4: w for i, w in enumerate(self.converter)})
        models = []
        for words in (self.words, self.challenger, self.retail):
            model = OrientedOracle(words, memory, args, phase, connected, mutation)
            if caller:
                model.entry = CALLER
                model.r[4:8] = model.before[4:8] = [args[0], ACTOR, 0, 0]
                model.run()
                self.assertEqual(model.forwarded, args)
                self.assertEqual(model.r[2], 1)
            else:
                model.run()
            self.assertEqual(len(model.calls), 1)
            observed, destination, snapshot = model.calls[0]
            self.assertEqual((destination, snapshot), (args[0], external(memory)))
            for i, (a, b) in enumerate(zip(observed, values)):
                self.assertTrue(equal_word(a, b) if arithmetic_index(i) else a == b, (i, hex(a), hex(b)))
            actual = external(model.memory)
            if not fixed:
                for i in range(16):
                    if arithmetic_index(i) and equal_word(read(actual, args[0] + i * 4), values[i]):
                        put(actual, args[0] + i * 4, values[i])
            self.assertEqual(actual, external(wanted))
            models.append(model)
        return models

    def test_retail_length_frame_and_stack_only_challenger_are_not_matching(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (142, 0xB8, 84))
        self.assertEqual((self.challenger_record['body_words'], self.challenger_record['frame'], self.challenger_record['differences']), (142, 0xC8, 57))
        differences = []
        for i, (a, b) in enumerate(zip(self.challenger, self.retail)):
            if a == b:
                continue
            self.assertEqual(a >> 16, b >> 16)
            self.assertEqual(a >> 21 & 31, 29)
            self.assertIn(a >> 26, (9, 43, 49, 57))
            differences.append(i * 4)
        self.assertEqual(len(differences), 57)
        self.assertEqual(self.record['relocations'], {0x21C: [('R_MIPS_26', 'guMtxF2L')]})
        self.assertEqual(self.challenger_record['relocations'], self.record['relocations'])
        self.receipt('layout', dict(selected=self.record, challenger=self.challenger_record, stack_only_offsets=differences, installed=False, guards=0))

    def test_thirty_two_source_order_vector_and_sdk_profile_controls(self):
        records = []
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                record, _ = screen.compile_candidate(self.root, self.output, name + '-' + profile, body, profile)
                records.append(record)
        self.assertEqual(len(records), 32)
        self.assertFalse(any(r['differences'] == 0 for r in records))
        self.assertTrue(all(not r['diagnostics'] for r in records))
        selected = next(r for r in records if r['name'] == 'up0-columns1-early0-o2g3')
        self.assertEqual((selected['body_words'], selected['frame'], selected['differences']), (142, 0xB8, 84))
        self.receipt('controls', records)

    def test_actual_padder_preserves_uninstalled_slot_and_retargets_converter(self):
        text, functions, relocations = parse_object(self.output / 'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['size'], 568)
        layout = self.output / 'layout.csv'
        layout.write_text('version,section,filename,function,address,end\n'
            'us,game,game_16EE20,func_15142600,0x15142600,0x15142838\n')
        assembly = self.output / 'padded.s'
        assembly.write_text(scaled.emit_padded_assembly(self.output / 'selected.o', layout, 'game_16EE20'))
        obj = self.output / 'padded.o'
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(assembly)], check=True, capture_output=True)
        padded, symbols, mapped = parse_object(obj)
        self.assertEqual(symbols[screen.FUNCTION]['size'], 568)
        self.assertEqual(padded[:568], text[:568])
        self.assertEqual(mapped, relocations)
        for target in (CONVERT, CONVERT + 0x1000000):
            elf = self.output / ('padded-%X.elf' % target)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output / 'oriented.ld'),
                '-e', screen.FUNCTION, '--defsym=guMtxF2L=0x%X' % target, '-o', str(elf), str(obj)], check=True, capture_output=True)
            words = list(struct.unpack_from('>142I', screen.sections(elf)['.text'][1]))
            expected = list(self.words)
            expected[0x21C // 4] = 0x0C000000 | (target >> 2 & 0x3FFFFFF)
            self.assertEqual(words, expected)
        self.receipt('padding', dict(bytes=568, guards=0, retargeted_calls=1, installed=False))

    def test_guest_every_input_basis_sign_degenerate_float_edges_aliases_and_saved_state(self):
        coverage = [set(), set(), set()]
        count = 0
        for original, alias, phase, mutation in itertools.product(self.inputs, range(3), (0, 8), (False, True)):
            args = ((OUTPUT, ACTOR + 0x18, ACTOR + 0x20)[alias], *original[1:])
            for index, model in enumerate(self.compare(args, phase, mutation=mutation)):
                coverage[index].update(model.visits)
            count += 1
        self.assertEqual(count, 2448)
        self.assertEqual([len(c) for c in coverage], [142, 142, 142])
        self.receipt('guest', dict(cases=count, bodies=3, covered_words=[len(c) for c in coverage], external_storage=True, private_trace_identity=False, arithmetic_nan_classification=True, hardware_fcsr=False))

    def test_original_thirty_word_caller_and_complete_fixed_converter_exact_domain(self):
        coverage = [set(), set(), set()]
        count = 0
        for delta, rows, column, alias, phase in itertools.product(((4, 0, 0), (-4, 0, 0), (0, 0, 4), (0, 0, -4)),
                ((0.5, 2), (-2, 0.25)), ((2, -0.5, 3), (-2, 0.25, -1), (0, 0, 0)), range(3), (0, 8)):
            start = (0.5, -2, 4)
            args = ((OUTPUT, ACTOR + 0x18, ACTOR + 0x20)[alias], *map(bits, (*rows, *column, *start, *[a + b for a, b in zip(start, delta)])))
            for index, model in enumerate(self.compare(args, phase, caller=True, fixed=True)):
                coverage[index].update(model.visits)
            count += 1
        expected = set(range(screen.ENTRY, screen.ENTRY + 568, 4)) | set(range(CALLER, CALLER + 120, 4)) | set(range(CONVERT, CONVERT + 460, 4))
        self.assertEqual(coverage, [expected] * 3)
        self.assertEqual(count, 144)
        self.receipt('connected', dict(cases=count, bodies=3, caller_words=30, builder_words=142, converter_words=115, all_words=True, domain='finite exact integral signed32 after scaling', hardware_fcsr=False))

    def test_actual_32_bit_native_typed_caller_all_external_bytes_and_nan_classification(self):
        original = self.fixture
        try:
            for body in (screen.SELECTED, self.challenger_body):
                self.fixture = original.replace(screen.SELECTED, body)
                self.run_host('int n,a,m,count=0;\nfor(n=0;n<204;n++)for(a=0;a<3;a++)for(m=0;m<2;m++){\n'
                    'initialize(n,a,m);if(func_150B9D14(output,source)!=1 || check())return 20+error;count++;}\n'
                    'if(count!=1224 || sizeof(Mtx)!=64 || sizeof(f32)!=4)return 30;\n')
        finally:
            self.fixture = original
        self.receipt('native', dict(cases_per_body=1224, bodies=2, bits=32, actual_source=True, caller=True, external_storage=True, converter='bounded float payload capture', arithmetic_nan_classification=True))

    def test_native_integer_loads_under_float_prototype_change_known_outputs(self):
        caller = screen.CALLER
        for offset in ('0x18', '0x1C', '0x2C'):
            caller = caller.replace('*(f32 *)(source + ' + offset + ')', '*(s32 *)(source + ' + offset + ')')
        original = self.fixture
        self.fixture = original.replace(screen.CALLER, caller)
        try:
            self.run_host('initialize(0,1,1);if(func_150B9D14(output,source)!=1 || stage!=1 || !error)return 40;\n')
        finally:
            self.fixture = original

    def test_compiled_semantic_negatives_change_known_matrix_or_call(self):
        forms = {'placeholder': screen.PROTOTYPE[:-1] + ' { }',
            'missing-converter': screen.SELECTED.replace('    guMtxF2L(matrix, output);', ''),
            'wrong-direction': screen.SELECTED.replace('ex - sx', 'sx - ex'),
            'wrong-cross': screen.SELECTED.replace('up[2] = -direction.unk4', 'up[2] = direction.unk4'),
            'missing-up-normalization': screen.SELECTED.replace('up[0] * inverse *', 'up[0] *'),
            'wrong-row': screen.SELECTED.replace('cy * row1', 'cy * row0'),
            'wrong-column': screen.SELECTED.replace('left.x * cx', 'left.x * cy'),
            'view-translation': screen.SELECTED.replace('matrix[3][0] = sx;', 'matrix[3][0] = -sx;'),
            'wrong-output': screen.SELECTED.replace('matrix, output);', 'matrix, (Mtx *)((u8 *)output + 4));')}
        args = (OUTPUT, *map(bits, (1, 2, 2, -0.5, 3, 7, -9, 11, 10, -7, 15)))
        expected = reference(args)
        receipts = []
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            model = OrientedOracle(words, memory_case(args), args).run()
            changed = len(model.calls) != 1 or model.calls[0][1] != OUTPUT or any(
                not equal_word(a, b) for a, b in zip(model.calls[0][0], expected))
            self.assertTrue(changed, name)
            receipts.append(dict(name=name, valid_mapped_case=True, known_semantic_difference=True))
        self.receipt('negatives', receipts)

    def test_missing_source_private_matrix_or_destination_fails_mapped_memory_gate(self):
        args = next(iter(self.inputs))
        for address, caller in ((ACTOR + 0x18, True), (ACTOR + 0x40, True), (OUTPUT, False), (STACK - 0xB8 + 0x4C, False)):
            memory = memory_case(args)
            del memory[address]
            connected = {CALLER + i * 4: w for i, w in enumerate(self.caller)} if caller else {}
            model = OrientedOracle(self.words, memory, args, connected=connected)
            if caller:
                model.entry = CALLER
                model.r[4:8] = model.before[4:8] = [OUTPUT, ACTOR, 0, 0]
            with self.assertRaisesRegex(AssertionError, 'unmapped'):
                model.run()

    def test_copied_typed_caller_retains_all_raw_functions_pools_and_warnings(self):
        source = (self.root / 'conker/src/game/generated_E5E90.c').read_text()
        old = re.search(r's32 func_150B9D14\([^;{}]+\) \{\n.*?\n\}', source, re.S)
        self.assertIsNotNone(old)
        self.assertIn(screen.OLD_CALLER_PROTOTYPE, source)
        selected = source.replace(old.group(), screen.CALLER).replace(screen.OLD_CALLER_PROTOTYPE, screen.PROTOTYPE)
        original_object, original_warnings = compile_owner(self.root, self.output, source, 'caller-baseline')
        selected_object, warnings = compile_owner(self.root, self.output, selected, 'caller-selected')
        self.assertEqual(warnings, original_warnings)
        old_text, old_functions, old_relocations = parse_object(original_object)
        text, functions, relocations = parse_object(selected_object)
        self.assertEqual(set(functions), set(old_functions))
        for name, meta in functions.items():
            old_meta = old_functions[name]
            self.assertEqual(text[meta['value']:meta['value'] + meta['size']], old_text[old_meta['value']:old_meta['value'] + old_meta['size']], name)
            self.assertEqual({a - meta['value']: r for a, r in relocations.items() if meta['value'] <= a < meta['value'] + meta['size']},
                {a - old_meta['value']: r for a, r in old_relocations.items() if old_meta['value'] <= a < old_meta['value'] + old_meta['size']}, name)
        for section in ('.rodata', '.data'):
            self.assertEqual(screen.sections(original_object).get(section), screen.sections(selected_object).get(section))
        caller = functions['func_150B9D14']
        self.assertEqual(caller['size'], 120)
        caller_words = list(struct.unpack_from('>30I', text, caller['value']))
        self.assertEqual({a - caller['value']: r for a, r in relocations.items() if caller['value'] <= a < caller['value'] + 120},
            {0x58: [('R_MIPS_26', screen.FUNCTION)]})
        self.assertEqual(caller_words[0x58 // 4], 0x0C000000)
        caller_words[0x58 // 4] = 0x0C000000 | (screen.ENTRY >> 2 & 0x3FFFFFF)
        self.assertEqual(caller_words, self.caller)
        self.receipt('caller-owner', dict(functions=len(functions), warnings=len(warnings), raw_neighbors_unchanged=True,
            caller_retail_words=30, prototype_correction='copied owner only', installed=False))

    def test_copied_builder_preserves_neighbors_pools_warnings_and_standalone_candidates(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        stub = 's32 func_15142600() {\n    return 0;\n}'
        self.assertIn(stub, source)
        original_object, original_warnings = compile_owner(self.root, self.output, source, 'builder-baseline')
        old_text, old_functions, old_relocations = parse_object(original_object)
        receipts = []
        for variant, body in (('selected', screen.SELECTED), ('challenger', self.challenger_body)):
            selected = source.replace(stub, body).replace('s32 func_15142600();', screen.PROTOTYPE)
            obj, warnings = compile_owner(self.root, self.output, selected, 'builder-' + variant)
            self.assertEqual(warnings, original_warnings)
            text, functions, relocations = parse_object(obj)
            self.assertEqual(set(functions), set(old_functions))
            for name, meta in functions.items():
                if name == screen.FUNCTION:
                    continue
                old_meta = old_functions[name]
                self.assertEqual(text[meta['value']:meta['value'] + meta['size']], old_text[old_meta['value']:old_meta['value'] + old_meta['size']], name)
                self.assertEqual({a - meta['value']: r for a, r in relocations.items() if meta['value'] <= a < meta['value'] + meta['size']},
                    {a - old_meta['value']: r for a, r in old_relocations.items() if old_meta['value'] <= a < old_meta['value'] + old_meta['size']}, name)
            target = functions[screen.FUNCTION]
            standalone, standalone_functions, standalone_relocations = parse_object(self.output / (variant + '.o'))
            self.assertEqual(target['size'], standalone_functions[screen.FUNCTION]['size'])
            self.assertEqual(text[target['value']:target['value'] + target['size']], standalone[:target['size']])
            self.assertEqual({a - target['value']: r for a, r in relocations.items() if target['value'] <= a < target['value'] + target['size']}, standalone_relocations)
            for section in ('.rodata', '.data'):
                self.assertEqual(screen.sections(original_object).get(section), screen.sections(obj).get(section))
            receipts.append(dict(variant=variant, functions=len(functions), warnings=len(warnings), raw_neighbors_unchanged=True, installed=False))
        self.receipt('builder-owner', receipts)


if __name__ == '__main__':
    unittest.main()
