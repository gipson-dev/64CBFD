"""Point-transform diagnostics, typed C ABI and bounded original-helper execution."""

import csv
import itertools
import json
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_point_transform_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests.game_owner_pool import normalized_pools, assert_guard_history
from tools.tests import test_game_random_curve_record as native
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, external_writes
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests.game_animation_timeline_oracle import bits, floating, signed
from tools.tests.test_game_queued_segment_writer import STACK

POINT, OUTPUT, MATRIX = 0x20000, 0x24000, 0x28000
STATUS, DIAGNOSTIC, FLAG = 0x800DCA00, 0x800DCA04, 0x800C3E90
CONVERT, TRANSFORM, TRANSLATE = 0x151EFEB8, 0x150A7960, 0x15142314
PATTERNS = (0, 0x80000000, 1, 0x80000001, 0x007FFFFF, 0x00800000,
    0x3F800000, 0xBF800000, 0x7F7FFFFF, 0x7F800000, 0xFF800000, 0x7FC12345)


def put(memory, address, value, size=4):
    for i in range(size):
        memory[address + i] = (value >> ((size - i - 1) * 8)) & 255


def read(memory, address, size=4):
    return int.from_bytes(bytes(memory[address + i] for i in range(size)), 'big')


def external(events):
    return [e for e in events if e[0] not in ('R', 'W') or not
        STACK - 0x600 <= e[1] < STACK + 0x140]


def external_memory(memory):
    return {a: v for a, v in memory.items() if not STACK - 0x600 <= a < STACK + 0x140}


def fixture(flag=0, axis=0, pattern=0x3F800000, null=False, alias=0):
    args = (0 if null else (POINT, STATUS + 8, STATUS)[alias % 3],
        (OUTPUT, POINT, STATUS + 8)[alias // 3], MATRIX)
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x140)}
    for base, size in ((POINT, 64), (OUTPUT, 64), (MATRIX, 80), (STATUS - 4, 32), (FLAG, 1)):
        memory.update({base + i: 0xA5 for i in range(size)})
    put(memory, STATUS, 0x11223344)
    put(memory, DIAGNOSTIC, 0x55667788)
    for i in range(3):
        put(memory, STATUS + 8 + i * 4, 0x87654321 + i)
    values = [0.0] * 16
    for i in (0, 5, 10, 15): values[i] = 0.5
    values[12:15] = [3.25, -4.5, 5.75]
    if flag:
        integers = [int(v * 65536) & 0xFFFFFFFF for v in values]
        payload = struct.pack('>32H', *[v >> 16 for v in integers], *[v & 65535 for v in integers])
    else:
        payload = struct.pack('>16I', *[bits(v) for v in values])
    memory.update({MATRIX + i: b for i, b in enumerate(payload)})
    if args[0]:
        for i in range(3): put(memory, args[0] + i * 4, pattern if i == axis else 0)
    put(memory, FLAG, flag, 1)
    return memory, args


class PointOracle(TriangleOracle):
    def __init__(self, words, memory, args, phase=0, connected=None, mutate=False, entry=screen.ENTRY):
        super().__init__(words, memory, phase=phase, entry=entry, arguments=args, connected=connected)
        self.input_args, self.mutate = args, mutate

    def record_call(self, target):
        if target == screen.ENTRY:
            args = self.arguments(3)
            self.calls.append((target, *args))
            return
        count = {CONVERT: 2, TRANSFORM: 7, TRANSLATE: 3}[target]
        args = self.arguments(count)
        status = self.peek(STATUS, 4)
        expected_status = (3 if target == CONVERT else 7 if target == TRANSLATE else
            bits(7.0) if self.mutate and self.input_args[0] == STATUS and self.peek(FLAG, 1) else
            3 if self.peek(FLAG, 1) else 5)
        assert status == expected_status, ('helper status', target, status)
        if target == TRANSFORM:
            assert args[5] == args[4] + 4 and args[6] == args[4] + 8, ('output tuple', args[4:])
        if target == TRANSLATE: assert args[1] == 0, ('translation index', args[1])
        self.calls.append((target, args, status))
        self.events.append(('CALL', target, args, status))

    def hook(self, target):
        if target == CONVERT:
            destination, source = self.arguments(2)
            for i in range(16):
                integer = self.get(source + i * 2, 2) << 16 | self.get(source + 32 + i * 2, 2)
                self.put(destination + i * 4, bits(floating(bits(float(signed(integer)))) / 65536.0), 4)
            if self.mutate:
                for i, value in enumerate((7.0, -8.0, 9.0)):
                    self.put(self.input_args[0] + i * 4, bits(value), 4)
        elif target == TRANSFORM:
            matrix, x, y, z, *outputs = self.arguments(7)
            x, y, z = map(floating, (x, y, z))
            values = [floating(self.get(matrix + i * 4, 4)) for i in range(16)]
            result = [bits(floating(bits(floating(bits(values[i] * x)) + floating(bits(values[i + 4] * y))))
                + floating(bits(floating(bits(values[i + 8] * z)) + values[i + 12]))) for i in range(3)]
            for address, value in zip(outputs, result): self.put(address, value, 4)
        else:
            assert target == TRANSLATE
            matrix, _, output = self.arguments(3)
            for i in range(3):
                if self.get(FLAG, 1):
                    high, low = self.get(matrix + 0x18 + i * 2, 2), self.get(matrix + 0x38 + i * 2, 2)
                    high = high if high < 32768 else high - 65536
                    low = low if low < 32768 else low - 65536
                    value = bits(floating(bits(float(high << 16) + float(low))) * (1.0 / 65536.0))
                else:
                    value = self.get(matrix + 0x30 + i * 4, 4)
                self.put(output + i * 4, value, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25): self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]


class GamePointTransformMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-point-transform-test'; cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>98I', cls.rom, screen.ROM))
        cls.directory = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, data):
        (self.output / (name + '.json')).write_text(json.dumps(data, indent=2) + '\n')

    def model(self, words, memory, args, phase=0, **kwargs):
        return PointOracle(words, memory, args, phase, **kwargs).run()

    def test_complete_slot_closed_register_cycle_and_profile_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (98, 0x78, 31))
        self.assertEqual(self.record['pool_bytes'], 0)
        text, functions, relocs = parse_object(self.output / 'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['size'], 392)
        changed = [i * 4 for i, (a, b) in enumerate(zip(self.words, self.retail)) if a != b]
        self.assertEqual(changed, [int(r['offset'], 16) for r in screen.owner_guards()])
        patched = list(self.words)
        for row in screen.owner_guards():
            offset = int(row['offset'], 16)
            self.assertEqual(struct.unpack_from('>I', text, offset)[0], int(row['expected'], 16))
            expected_reloc = ';'.join(k + ':' + n for k, n in relocs.get(offset, ())) or '-'
            self.assertEqual(row['expected_relocations'], expected_reloc)
            self.assertEqual(row['replacement_relocations'], expected_reloc)
            patched[offset // 4] = int(row['replacement'], 16) | (
                self.words[offset // 4] & 65535 if offset in relocs else 0)
        self.assertEqual(patched, self.retail)
        # The three initial saved-register stores only change their independent order.
        self.assertEqual(set(self.words[i] for i in (1, 3, 4)), set(self.retail[i] for i in (1, 3, 4)))
        rename = {17: 19, 18: 17, 19: 18}
        for i in range(5, 90):
            word = self.words[i]; op = word >> 26
            fields = (21, 16, 11) if op == 0 else (16,) if op == 15 else (21,) if op in (49, 57) else (21, 16) if op != 17 else ()
            for shift in fields:
                value = word >> shift & 31
                if value in rename: word = word & ~(31 << shift) | rename[value] << shift
            self.assertEqual(word, self.retail[i], hex(i * 4))
        records = []
        for profile in screen.PROFILES:
            record, _ = screen.compile_candidate(self.root, self.output, 'profile-' + profile, profile=profile)
            records.append(record)
        self.receipt('slot', dict(words=98, frame=120, raw_differences=31, normalized_differences=0,
            guards=31, profiles=records, insertions=0, omissions=0, closed_cycle=[17, 19, 18]))

    def test_bounded_guest_null_zero_nonzero_diagnostics_aliases_and_rereads(self):
        count, coverage = 0, [set(), set()]
        for flag, axis, pattern, phase, alias in itertools.product((0, 1, 255), range(3), PATTERNS, (0, 8), range(9)):
            memory, args = fixture(flag, axis, pattern, alias=alias)
            models = [self.model(words, memory, args, phase, mutate=bool(count % 2)) for words in (self.words, self.retail)]
            self.assertEqual(models[0].memory, models[1].memory)
            self.assertEqual(external(models[0].events), external(models[1].events))
            self.assertEqual(models[0].calls, models[1].calls)
            self.assertEqual(read(models[0].memory, STATUS), 0)
            for i, model in enumerate(models): coverage[i].update(model.visits)
            count += 1
        for flag, phase in itertools.product((0, 1, 255), (0, 8)):
            memory, args = fixture(flag, null=True)
            del memory[POINT]
            models = [self.model(words, memory, args, phase) for words in (self.words, self.retail)]
            self.assertEqual(models[0].memory, models[1].memory)
            self.assertEqual(external(models[0].events), external(models[1].events))
            self.assertEqual([e[3] for e in external_writes(models[0]) if e[1] == STATUS], [1, 7, 8, 0])
            self.assertEqual(read(models[0].memory, DIAGNOSTIC), 0x55667788)
            for i, model in enumerate(models): coverage[i].update(model.visits)
            count += 1
        self.assertEqual([len(c) for c in coverage], [98, 98])
        self.receipt('guest', dict(cases=count, covered_words=[98, 98], full_memory=True,
            external_traces=True, aliases=9, mutations='bounded guMtxL2F hook', fcsr='not modeled'))

    def test_status_sequences_and_fixed_conversion_input_reload(self):
        for flag, null, zero in itertools.product((0, 1, 255), (False, True), (False, True)):
            memory, args = fixture(flag, pattern=0 if zero else bits(2.0), null=null)
            model = self.model(self.words, memory, args, mutate=True)
            expected = [1, 7, 8, 0] if null or zero else [1, 2, 3, 4, 0] if flag else [1, 2, 5, 6, 0]
            self.assertEqual([e[3] for e in external_writes(model) if e[1] == STATUS], expected)
            if flag and not null and not zero:
                transform = next(c for c in model.calls if c[0] == TRANSFORM)
                self.assertEqual(transform[1][1:4], tuple(map(bits, (7.0, -8.0, 9.0))))
                self.assertEqual(read(model.memory, STATUS + 8), bits(2.0))

    def test_connected_original_sdk_matrix_and_translation_helpers(self):
        helpers = {CONVERT: (0x21D368, 46), TRANSFORM: (0xD4E10, 40), TRANSLATE: (0x16F7C4, 49)}
        connected = {}
        for address, (offset, length) in helpers.items():
            connected.update(zip(range(address, address + length * 4, 4), struct.unpack_from('>%dI' % length, self.rom, offset)))
        count, coverage = 0, set()
        for flag, axis, pattern, phase, null in itertools.product((0, 1, 255), range(3),
                (0, 0x80000000, bits(1.0), bits(-2.5), bits(0.25)), (0, 8), (False, True)):
            memory, args = fixture(flag, axis, pattern, null)
            models = [self.model(words, memory, args, phase, connected=connected) for words in (self.words, self.retail)]
            hooked = self.model(self.retail, memory, args, phase)
            self.assertEqual(models[0].memory, models[1].memory)
            self.assertEqual(external(models[0].events), external(models[1].events))
            self.assertEqual(models[0].calls, models[1].calls)
            for i in range(3): self.assertEqual(read(models[0].memory, args[1] + i * 4), read(hooked.memory, args[1] + i * 4))
            coverage.update(models[0].visits); count += 1
        self.assertTrue(set(range(TRANSFORM, TRANSFORM + 160, 4)) <= coverage)
        self.assertTrue(set(range(CONVERT, CONVERT + 180, 4)) <= coverage)
        self.assertTrue(set(range(TRANSLATE, TRANSLATE + 196, 4)) <= coverage)
        self.receipt('connected', dict(cases=count, sdk_slot_words=46, sdk_executed_words=45,
            transform_words=40, translation_words=49, original_helpers=True,
            full_memory=True, finite_exact_fixed_domain=True, fcsr='not modeled'))

    def test_mapped_memory_fail_closed_and_lazy_point_reads(self):
        for flag, missing in ((0, POINT), (0, STATUS), (0, DIAGNOSTIC), (0, FLAG), (1, MATRIX), (0, OUTPUT)):
            memory, args = fixture(flag)
            del memory[missing]
            with self.assertRaisesRegex(AssertionError, 'unmapped'):
                self.model(self.words, memory, args)
        memory, args = fixture(0, pattern=bits(1.0))
        # The helper rereads all three nonzero-path coordinates, even after a short-circuit gate.
        del memory[POINT + 8]
        with self.assertRaisesRegex(AssertionError, 'unmapped'):
            self.model(self.words, memory, args)

    def test_actual_native_32_bit_typed_caller_and_sdk_conversion(self):
        sdk = (self.root / 'conker/src/libultra/gu/mtxutil2.c').read_text().split('void guMtxL2F', 1)[1]
        self.fixture = '''typedef unsigned char u8;typedef int s32;typedef unsigned int u32;typedef float f32;
typedef union { s32 m[4][4]; double alignment; } Mtx;
#define NULL ((void *)0)
void guMtxL2F(f32 matrix[4][4],Mtx *fixed);
''' + screen.DECLARATIONS + '''
volatile s32 D_800DCA00;u8 *D_800DCA04;f32 D_800DCA08,D_800DCA0C,D_800DCA10;u8 D_800C3E90;
static f32 point[3],output[3];
static union { Mtx fixed;f32 floating[16]; } buffer;
static int error,convertCalls,transformCalls,translationCalls,mutate;
static u32 asBits(f32 f) { union {f32 f;u32 u;} v;v.f=f;return v.u; }
void sdkMtxL2F''' + sdk + '''
void guMtxL2F(f32 matrix[4][4],Mtx *fixed) {
    if(D_800DCA00!=3 || fixed!=&buffer.fixed || D_800DCA04!=(u8 *)&buffer || transformCalls || translationCalls) error=1;
    convertCalls++;sdkMtxL2F(matrix,fixed);
    if(mutate) {point[0]=7.0f;point[1]=-8.0f;point[2]=9.0f;}
}
void func_150A7960(f32 matrix[4][4],f32 x,f32 y,f32 z,f32 *ox,f32 *oy,f32 *oz) {
    f32 *v=&matrix[0][0],result[3];int i;
    if(D_800DCA00!=(D_800C3E90?3:5) || D_800DCA04!=(u8 *)&buffer || translationCalls
       || oy!=ox+1 || oz!=ox+2 || (D_800C3E90?convertCalls!=1:convertCalls!=0)) error=2;
    transformCalls++;
    for(i=0;i<3;i++)result[i]=(v[i]*x+v[i+4]*y)+(v[i+8]*z+v[i+12]);
    *ox=result[0];*oy=result[1];*oz=result[2];
}
void func_15142314(u8 *matrix,s32 index,f32 *out) {
    if(D_800DCA00!=7 || matrix!=(u8 *)&buffer || index || convertCalls || transformCalls) error=3;
    translationCalls++;
    out[0]=3;out[1]=-4;out[2]=5;
}
''' + screen.SELECTED + '\n'
        self.run_host(r'''
static u8 flags[]={0,1,255};
int f,n,z,axis,alias,change,i,count=0;f32 input[3],want[3],*out;
u32 saved[16],*words=(u32 *)&buffer.fixed;
for(f=0;f<3;f++)for(n=0;n<2;n++)for(z=0;z<2;z++)for(axis=0;axis<3;axis++)for(alias=0;alias<2;alias++)for(change=0;change<2;change++) {
    error=convertCalls=transformCalls=translationCalls=0;mutate=change;D_800C3E90=flags[f];
    D_800DCA00=99;D_800DCA04=(u8 *)0x12345678;
    D_800DCA08=11;D_800DCA0C=12;D_800DCA10=13;
    for(i=0;i<3;i++)point[i]=input[i]=(!z && i==axis)?2.5f:0.0f;
    for(i=0;i<16;i++)buffer.floating[i]=0;
    if(!flags[f]) {
        for(i=0;i<4;i++)buffer.floating[i*5]=0.5f;
        buffer.floating[12]=3;buffer.floating[13]=-4;buffer.floating[14]=5;
    } else {
        s32 packed[16];
        for(i=0;i<16;i++)packed[i]=(i==0 || i==5 || i==10 || i==15)?32768:0;
        packed[12]=3*65536;packed[13]=-4*65536;packed[14]=5*65536;
        for(i=0;i<8;i++) {
            words[i]=((u32)packed[i*2]&0xFFFF0000u)|((u32)packed[i*2+1]>>16);
            words[i+8]=((u32)packed[i*2]<<16)|((u32)packed[i*2+1]&0xFFFFu);
        }
    }
    for(i=0;i<16;i++)saved[i]=words[i];
    for(i=0;i<3;i++)want[i]=(i==0?3.0f:i==1?-4.0f:5.0f)+((n || z)?0.0f:0.5f*(flags[f] && change?(i==0?7.0f:i==1?-8.0f:9.0f):input[i]));
    out=alias?point:output;
    func_15143134(n?NULL:point,out,(u8 *)&buffer);
    if(error || D_800DCA00 || sizeof(void *)!=4 || sizeof(Mtx)!=64)return 1;
    for(i=0;i<3;i++)if(asBits(out[i])!=asBits(want[i]))return 2;
    for(i=0;i<16;i++)if(words[i]!=saved[i])return 3;
    if(n || z) {
        if(translationCalls!=1 || convertCalls || transformCalls || D_800DCA04!=(u8 *)0x12345678
           || D_800DCA08!=11 || D_800DCA0C!=12 || D_800DCA10!=13)return 4;
    } else {
        if(transformCalls!=1 || translationCalls || convertCalls!=(flags[f]?1:0)
           || D_800DCA08!=input[0] || D_800DCA0C!=input[1] || D_800DCA10!=input[2])return 5;
    }
    count++;
}
if(count!=144)return 6;
''')
        self.receipt('native', dict(cases=144, bits=32, typed_caller=True, actual_sdk_body=True,
            translation='bounded helper', transform='separate rounded C arithmetic', readonly_matrix=True,
            aliases='output/input', fcsr='not modeled'))

    def test_original_caller_call_delay_pairs_forward_three_inputs_and_return(self):
        pair_word = 0x0C000000 | screen.ENTRY >> 2 & 0x3FFFFFF
        pairs = []
        pattern = re.compile(r'/\* [0-9A-F]+ ([0-9A-F]+) ([0-9A-F]{8}) \*/')
        for path in sorted((self.root / 'conker/asm/nonmatchings').rglob('*.s')):
            instructions = [(int(a, 16), int(w, 16)) for a, w in pattern.findall(path.read_text())]
            for i, (address, word) in enumerate(instructions[:-1]):
                if word == pair_word:
                    self.assertEqual(instructions[i + 1][0], address + 4)
                    pairs.append((str(path.relative_to(self.root)), address, word, instructions[i + 1][1]))
        self.assertGreaterEqual(len(pairs), 30)
        count = 0
        for path, address, call, delay in pairs:
            for flag, phase in itertools.product((0, 1, 255), (0, 8)):
                memory, args = fixture(flag)
                seed = {r: 0x100000 + r * 0x1000 for r in range(1, 29)}
                for base in seed.values():
                    memory.update({base + i: 0xA5 for i in range(-0x100, 0xA00)})
                    for i in range(-0x100, 0xA00, 4): put(memory, base + i, MATRIX)
                seed.update({4: POINT, 5: OUTPUT, 6: MATRIX})
                probe = PointOracle([], memory, args, phase)
                for r, value in seed.items(): probe.r[r] = probe.before[r] = value
                probe.execute(delay)
                forwarded = tuple(probe.r[4:7])
                for base in forwarded:
                    memory.update({base + i: 0xA5 for i in range(80)})
                for i in range(3): put(memory, forwarded[0] + i * 4, bits(i + 1.0))
                original_matrix, _ = fixture(flag)
                for i in range(64): memory[forwarded[2] + i] = original_matrix[MATRIX + i]
                models = []
                for words in (self.words, self.retail):
                    connected = dict(zip(range(screen.ENTRY, screen.ENTRY + 392, 4), words))
                    model = PointOracle([call, delay, 0x3C1FDEAD, 0x03E00008, 0], memory, args,
                        phase, connected=connected, entry=address)
                    for r, value in seed.items(): model.r[r] = model.before[r] = value
                    model.run()
                    self.assertEqual(model.calls[0], (screen.ENTRY, *forwarded), path)
                    models.append(model)
                self.assertEqual(models[0].memory, models[1].memory, path)
                self.assertEqual(external(models[0].events), external(models[1].events), path)
                count += 1
        self.receipt('caller-pairs', dict(pairs=len(pairs), cases=count, three_inputs=True,
            fourth_input='unused', full_memory=True, external_traces=True,
            boundary='original call/delay words, seeded registers and synthetic return; not complete callers',
            sites=[dict(path=p, address='0x%X' % a, delay='0x%08X' % d) for p, a, _, d in pairs]))

    def copied_owner(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        pragma = '#pragma GLOBAL_ASM("asm/nonmatchings/game_16EE20/func_15143134.s")'
        baseline = source.replace(screen.SELECTED, pragma).replace(screen.PROTOTYPE, 's32 func_15143134();')
        baseline = baseline.replace(screen.OWNER_DECLARATIONS + '\n', '')
        self.assertIn(pragma, baseline)
        selected = baseline.replace('/* Generated placeholder declarations. */',
            screen.OWNER_DECLARATIONS + '\n/* Generated placeholder declarations. */').replace(
            pragma, screen.SELECTED).replace('s32 func_15143134();', screen.PROTOTYPE)
        objects = []
        for name, body in (('baseline', baseline), ('selected', selected)):
            obj, warnings = compile_owner(self.root, self.output, body, 'owner-' + name)
            self.assertEqual(len(warnings), 2)
            objects.append((obj, warnings))
        self.assertEqual(objects[0][1], objects[1][1])
        text, functions, relocs = parse_object(objects[1][0])
        target = functions[screen.FUNCTION]
        standalone, _, standalone_relocs = parse_object(self.output / 'selected.o')
        self.assertEqual(text[target['value']:target['value'] + 392], standalone[:392])
        self.assertEqual({o - target['value']: r for o, r in relocs.items()
            if target['value'] <= o < target['value'] + 392}, standalone_relocs)
        result = []
        for name, (obj, _) in zip(('baseline', 'selected'), objects):
            processed = self.output / ('owner-' + name + '-postprocessed.o'); shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.output / ('owner-' + name + '.c')).relative_to(self.root / 'conker')),
                '--post-process', str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker', check=True, capture_output=True)
            result.append(processed)
        return result

    def test_copied_owner_complete_neighbors_and_pool_ownership(self):
        old, new = self.copied_owner()
        old_text, old_functions, old_relocs = parse_object(old)
        text, functions, relocs = parse_object(new)
        self.assertEqual(set(old_functions), set(functions))
        for name, f in functions.items():
            if name == screen.FUNCTION: continue
            previous = old_functions[name]
            self.assertEqual(text[f['value']:f['value'] + f['size']],
                old_text[previous['value']:previous['value'] + previous['size']], name)
            self.assertEqual({o - f['value']: r for o, r in relocs.items() if f['value'] <= o < f['value'] + f['size']},
                {o - previous['value']: r for o, r in old_relocs.items()
                    if previous['value'] <= o < previous['value'] + previous['size']}, name)
        self.assertEqual(normalized_pools(old), normalized_pools(new))
        self.assertEqual(len(screen.sections(new)['.rodata'][1]), 704)
        self.receipt('owner', dict(functions=len(functions), unchanged=len(functions) - 1,
            warnings=2, new_warnings=0, pool_bytes=704, normalized_pools_equal=True))

    def test_actual_owner_padder_guard_metadata_and_alternate_relocations(self):
        _, owner = self.copied_owner()
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream: rows = list(csv.DictReader(stream))
        rows = [r for r in rows if r['function'] != screen.FUNCTION] + screen.owner_guards()
        guard_path = self.output / 'owner-guards.csv'

        def emit(items):
            with guard_path.open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=list(items[0])); writer.writeheader(); writer.writerows(items)
            return emit_padded_assembly(owner, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
                rodata_symbol='jtbl_800A5218_game', word_patches_path=guard_path)

        assembly = emit(rows)
        begin = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), begin)
        end = assembly.index('\n', end)
        source, obj = (self.output / ('padded' + suffix) for suffix in ('.s', '.o'))
        source.write_text('.text\n.globl %s\n' % screen.FUNCTION + assembly[begin:end + 1])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(source)], check=True, capture_output=True)
        _, functions, relocs = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'], 392)
        original_text, _, original_relocs = parse_object(self.output / 'selected.o')
        self.assertEqual(relocs, original_relocs)
        for alternate in (False, True):
            targets = screen.SYMBOLS if not alternate else {n: (0x15208004 + i * 0x10000 if n in
                ('guMtxL2F', 'func_150A7960', 'func_15142314') else 0x90018004 + i * 0x10000)
                for i, n in enumerate(screen.SYMBOLS)}
            elf = self.output / ('padded-%d.elf' % alternate)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output / 'point.ld'), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X' % item for item in targets.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
            words = list(struct.unpack_from('>98I', screen.sections(elf)['.text'][1]))
            expected = list(self.retail)
            for offset, values in relocs.items():
                self.assertEqual(len(values), 1)
                kind, name = values[0]; address = targets[name]
                if kind == 'R_MIPS_26': expected[offset // 4] = expected[offset // 4] & 0xFC000000 | address >> 2 & 0x3FFFFFF
                else:
                    self.assertEqual(struct.unpack_from('>I', original_text, offset)[0] & 65535, 0)
                    expected[offset // 4] = expected[offset // 4] & 0xFFFF0000 | (
                        (address + 0x8000) >> 16 & 65535 if kind == 'R_MIPS_HI16' else address & 65535)
            self.assertEqual(words, expected)
        for field, value, index in (('expected', '0xAE200004', -1),
                ('expected_relocations', 'R_MIPS_HI16:D_800DCA04', -30)):
            altered = [dict(r) for r in rows]; altered[index][field] = value
            with self.assertRaisesRegex(ValueError, 'stale'): emit(altered)
        self.receipt('padding', dict(words=98, guards=31, metadata_unchanged=True,
            alternate_carries=True, alternate_helpers=True, stale_word=True, stale_relocation=True))

    def test_compiled_negative_controls_change_outputs_status_or_call_contract(self):
        forms = {
            'zero-stub': screen.PROTOTYPE[:-1] + ' {}',
            'wrong-zero-gate': screen.SELECTED.replace('point[2] != 0.0f', 'point[2] == 0.0f'),
            'wrong-diagnostic': screen.SELECTED.replace('D_800DCA0C = point[1]', 'D_800DCA0C = point[0]'),
            'wrong-final-status': screen.SELECTED.replace('D_800DCA00 = 0;', 'D_800DCA00 = 9;'),
            'wrong-translation-index': screen.SELECTED.replace('func_15142314(matrix, 0, output)', 'func_15142314(matrix, 1, output)'),
            'wrong-output': screen.SELECTED.replace('&output[2]', '&output[1]')}
        report = []
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            changes = 0
            for flag, axis, pattern in itertools.product((0, 1), range(3), (0, bits(2.0))):
                memory, args = fixture(flag, axis, pattern)
                expected = self.model(self.retail, memory, args)
                try:
                    model = self.model(words, memory, args)
                    changes += (external_memory(model.memory), external(model.events), model.calls) != (
                        external_memory(expected.memory), external(expected.events), expected.calls)
                except AssertionError as error:
                    self.assertTrue(any(gate in str(error) for gate in
                        ('helper status', 'unmapped', 'output tuple', 'translation index')), str(error))
                    changes += 1
            self.assertGreater(changes, 0, name)
            report.append(dict(name=name, mapped_cases=12, changes=changes))
        self.receipt('negatives', report)

    def test_production_source_slot_and_guard_history(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.SELECTED, source)
        self.assertEqual(source.count(screen.PROTOTYPE), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream: guards = list(csv.DictReader(stream))
        digest = assert_guard_history(self, guards)
        self.assertEqual(guards[10811:10842], screen.owner_guards())
        self.receipt('production', dict(words=98, guards=len(guards), guard_sha256=digest, byte_exact=True))


if __name__ == '__main__': unittest.main()
