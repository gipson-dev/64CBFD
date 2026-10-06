"""Scoped FPR lifetimes, live envelope inputs and unchecked period subtraction."""

import csv
import itertools
import json
import math
import re
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_piecewise_envelope_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_timed_interpolation_match import (
    ACTOR, TIME, InterpolationOracle, external, external_trace, memory_case as base_memory,
    number, put, read, rounded, rounded_bits,
)
from tools.tests import test_game_random_curve_record as native
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly
from pad_generated_object import parse_object

PATTERNS = (0, 0x80000000, 1, 0x80000001, 0x007FFFFF, 0x00800000,
            0x7F7FFFFF, 0xFF7FFFFF, 0x7F800000, 0xFF800000, 0x7FC12345, 0x7F812345)
FIELDS = (0x170, 0x174, 0x178, 0x17C, 0x180, 0x184, 0x188, 0x18C, 0x190, TIME)
CYCLES = ((0x44, 0x68, {4: 18, 18: 16, 16: 4}), (0x84, 0xA4, {4: 8, 8: 4}),
          (0x88, 0x90, {16: 18, 18: 16}), (0xAC, 0xB8, {4: 16, 16: 4}))
OFFSETS = (0x44, 0x48, 0x50, 0x58, 0x64, 0x68, 0x84, 0x88, 0x90, 0x94, 0x98, 0xAC, 0xB4)


def rewrite_registers(word, mapping):
    op, fmt = word >> 26, word >> 21 & 31
    fields = (16,) if op in (49, 57) else (16, 11, 6) if op == 17 and fmt == 16 else (11,) if op == 17 and fmt == 4 else ()
    for shift in fields:
        value = word >> shift & 31
        word = word & ~(31 << shift) | mapping.get(value, value) << shift
    return word


def normalize(words):
    derived = []
    for index, word in enumerate(words):
        offset = index*4
        for start, end, mapping in CYCLES:
            assert set(mapping) == set(mapping.values())
            if start <= offset <= end:
                word = rewrite_registers(word, mapping)
        if offset in (0x58, 0xA4, 0xB8):
            assert word >> 26 == 17 and word >> 21 & 31 == 16 and word & 63 in (0, 2)
            fs, ft = word >> 11 & 31, word >> 16 & 31
            word = word & ~((31 << 11) | (31 << 16)) | fs << 16 | ft << 11
        derived.append(word)
    return derived


class EnvelopeOracle(InterpolationOracle):
    def __init__(self, body, memory, actor, phase=0):
        super().__init__(body, memory, actor, (), 0, phase=phase)
        self.entry = screen.ENTRY
        self.code = {screen.ENTRY+i*4: word for i, word in enumerate(body)}

    def execute(self, word):
        if word >> 26 == 17 and word >> 21 & 31 == 16 and word & 63 == 62:
            self.condition = number_value(self.f[word >> 11 & 31]) <= number_value(self.f[word >> 16 & 31])
        else:
            super().execute(word)

    def record_call(self, target):
        raise AssertionError(('unexpected call', target))


def memory_case(elapsed, step, period, alias=0, amplitude=10, baseline=-2):
    memory, _ = base_memory()
    actor = (ACTOR, TIME-0x17C, TIME-0x158)[alias]
    if alias:
        memory.update({actor-16+i: (i*17+13)&255 for i in range(0x1E0)})
    for offset, value in ((0x158, 99), (0x170, 8), (0x174, baseline), (0x178, amplitude),
                          (0x17C, elapsed), (0x180, 1), (0x184, 2), (0x188, 3),
                          (0x18C, period), (0x190, 1)):
        put(memory, actor+offset, rounded_bits(value))
    put(memory, TIME, rounded_bits(step))
    return memory, actor


def arithmetic_output(memory, actor):
    elapsed = number(memory, actor+0x17C)
    return not (elapsed < number(memory, actor+0x180)) and (
        elapsed < number(memory, actor+0x184) or not (elapsed < number(memory, actor+0x188)))


def reference(memory, actor):
    memory = dict(memory)
    elapsed = number(memory, actor+0x17C)
    baseline = number(memory, actor+0x174)
    if elapsed < number(memory, actor+0x180):
        output = read(memory, actor+0x174)
    elif elapsed < number(memory, actor+0x184):
        factor = rounded(rounded(elapsed-number(memory, actor+0x180))*number(memory, actor+0x190))
        output = rounded_bits(baseline+rounded(number(memory, actor+0x178)*factor))
    elif elapsed < number(memory, actor+0x188):
        output = read(memory, actor+0x170)
    else:
        product = rounded(rounded(elapsed-number(memory, actor+0x188))*number(memory, actor+0x190))
        factor = rounded(1.0-product)
        output = rounded_bits(baseline+rounded(number(memory, actor+0x178)*factor))
    put(memory, actor+0x158, output)
    period = number(memory, actor+0x18C)
    elapsed = rounded(number(memory, actor+0x17C)+number(memory, TIME))
    put(memory, actor+0x17C, rounded_bits(elapsed))
    for _ in range(128):
        if not period < elapsed:
            return external(memory)
        elapsed = rounded(elapsed-period)
        put(memory, actor+0x17C, rounded_bits(elapsed))
    return None


def native_fixture(body):
    return r'''
typedef unsigned char u8; typedef unsigned int u32; typedef int s32; typedef float f32;
typedef struct { union { u32 align; u8 bytes[0x1E0]; } storage; f32 step; } State;
static State live, shadow;
static int alias, arithmetic;
static u8 *actor(State *s) { return s->storage.bytes+16; }
static f32 *timeStep(State *s) { return alias==1?(f32 *)(actor(s)+0x17C):
    alias==2?(f32 *)(actor(s)+0x158):&s->step; }
#define D_800BE9A4 (*timeStep(&live))
static u32 bits(f32 v) { union { u32 u; f32 f; } w; w.f=v; return w.u; }
static f32 number(u32 v) { union { u32 u; f32 f; } w; w.u=v; return w.f; }
static f32 load(State *s,int offset) { return *(f32 *)(actor(s)+offset); }
static void store(State *s,int offset,f32 value) { *(f32 *)(actor(s)+offset)=value; }
static int nanWord(u32 u) { return (u&0x7FFFFFFF)>0x7F800000; }
static void initialize(f32 elapsed,f32 step,f32 period,int useAlias,f32 amp,f32 baseline) {
    int i;
    alias=useAlias;
    for(i=0;i<0x1E0;i++) live.storage.bytes[i]=(u8)(i*17+13);
    store(&live,0x158,99); store(&live,0x170,8); store(&live,0x174,baseline); store(&live,0x178,amp);
    store(&live,0x17C,elapsed); store(&live,0x180,1); store(&live,0x184,2); store(&live,0x188,3);
    store(&live,0x18C,period); store(&live,0x190,1); *timeStep(&live)=step;
}
static int reference(void) {
    volatile f32 delta,factor,product,elapsed;
    f32 period;
    int i;
    for(i=0;i<0x1E0;i++) shadow.storage.bytes[i]=live.storage.bytes[i];
    shadow.step=live.step; arithmetic=0; elapsed=load(&shadow,0x17C);
    if(elapsed<load(&shadow,0x180)) store(&shadow,0x158,load(&shadow,0x174));
    else if(elapsed<load(&shadow,0x184)) {
        arithmetic=1; delta=elapsed-load(&shadow,0x180); factor=delta*load(&shadow,0x190);
        product=load(&shadow,0x178)*factor; store(&shadow,0x158,load(&shadow,0x174)+product);
    } else if(elapsed<load(&shadow,0x188)) store(&shadow,0x158,load(&shadow,0x170));
    else {
        arithmetic=1; delta=elapsed-load(&shadow,0x188); product=delta*load(&shadow,0x190);
        factor=1.0f-product; product=load(&shadow,0x178)*factor;
        store(&shadow,0x158,load(&shadow,0x174)+product);
    }
    period=load(&shadow,0x18C); elapsed=load(&shadow,0x17C)+*timeStep(&shadow);
    store(&shadow,0x17C,elapsed);
    for(i=0;i<128;i++) {
        if(!(period<elapsed)) return 1;
        elapsed=elapsed-period; store(&shadow,0x17C,elapsed);
    }
    return 0;
}
static int check(int classify) {
    int i;
    for(i=0;i<0x1E0;i++) {
        if(classify && (i==16+0x17C || (arithmetic && i==16+0x158))) {
            u32 a=bits(*(f32 *)(live.storage.bytes+i)), b=bits(*(f32 *)(shadow.storage.bytes+i));
            if(a!=b && !(nanWord(a)&&nanWord(b))) return 1;
            i+=3;
        } else if(live.storage.bytes[i]!=shadow.storage.bytes[i]) return 2;
    }
    if(bits(live.step)!=bits(shadow.step)) return 3;
    return 0;
}
''' + body + '\n'


class GamePiecewiseEnvelopeMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-piecewise-envelope-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.normalized = normalize(cls.raw)
        cls.retail = list(struct.unpack_from('>69I', (cls.root/'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        owner = (cls.root/'conker/src/game_16DC80.c').read_text()
        body = re.search(r's32 func_151415D4\(u8 \*actor\) \{\n.*?\n\}', owner, re.S)
        cls.fixture = native_fixture(body.group(0) if body else screen.SELECTED)

    def test_scoped_factor_shape_and_closed_fpr_lifetimes(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['diagnostics']), (69, 0, 13, ''))
        self.assertEqual(self.normalized, self.retail)
        self.assertEqual([i*4 for i, (a, b) in enumerate(zip(self.raw, self.retail)) if a != b], list(OFFSETS))
        for old, new in zip(self.raw, self.normalized):
            self.assertEqual(old >> 26, new >> 26)
            if old >> 26 == 17:
                self.assertEqual(old&63, new&63)
            else:
                self.assertEqual(old&65535, new&65535)
        self.assertEqual(self.raw[:17], self.retail[:17])
        self.assertEqual(self.raw[48:], self.retail[48:])

    def test_real_padder_guards_relocations_and_complete_slot(self):
        text, functions, relocations = parse_object(self.output/'selected.o')
        start = functions['func_151415D4']['value']
        raw = list(struct.unpack_from('>69I', text, start))
        fields = ('filename', 'function', 'offset', 'expected', 'replacement', 'expected_relocations',
                  'replacement_relocations', 'note', 'insert_after', 'insert_after_relocations', 'omit')
        with (self.output/'guards.csv').open('w', newline='') as stream:
            writer = csv.writer(stream); writer.writerow(fields)
            for offset in OFFSETS:
                self.assertNotIn(start+offset, relocations)
                writer.writerow(('game_16DC80', 'func_151415D4', '0x%X'%offset, '0x%08X'%raw[offset//4],
                    '0x%08X'%normalize(raw)[offset//4], '-', '-',
                    'Normalize envelope closed FPR lifetimes and commutative operands', '', '', 'false'))
        layout = self.output/'layout.csv'
        layout.write_text('version,section,filename,function,address,end\n'
                          'us,game,game_16DC80,func_151415D4,0x151415D4,0x151416E8\n')
        assembly = emit_padded_assembly(self.output/'selected.o', layout, 'game_16DC80',
                                       word_patches_path=self.output/'guards.csv')
        (self.output/'padded.s').write_text(assembly)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(self.output/'padded.o'),
                        str(self.output/'padded.s')], check=True, capture_output=True)
        _, padded_functions, padded_relocations = parse_object(self.output/'padded.o')
        self.assertEqual(padded_functions['func_151415D4']['size'], 276)
        self.assertEqual(padded_relocations, relocations)
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output/'envelope.ld'),
                        '-e', 'func_151415D4', *['--defsym=%s=0x%X'%item for item in screen.SYMBOLS.items()],
                        '-o', str(self.output/'padded.elf'), str(self.output/'padded.o')], check=True, capture_output=True)
        linked = load_elf_functions(str(self.output/'padded.elf'), 'mips-linux-gnu-objdump')[0]['func_151415D4']
        self.assertEqual(linked[:69], self.retail)
        self.assertFalse(any(linked[69:]))

    def test_guest_complete_storage_access_order_return_and_reachable_words(self):
        coverage = [set(), set(), set()]; count = 0
        for elapsed, step, period, alias, amp, baseline, phase in itertools.product(
                (-1, 0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5), (0, 0.25, 1, 4), (2, 4, 8),
                range(3), (0, 10, -4), (-2, 0, 5), (0, 8)):
            memory, actor = memory_case(elapsed, step, period, alias, amp, baseline)
            wanted = reference(memory, actor); self.assertIsNotNone(wanted)
            traces = []
            for index, body in enumerate((self.raw, self.normalized, self.retail)):
                model = EnvelopeOracle(body, memory, actor, phase).run()
                self.assertEqual(external(model.memory), wanted, (count, index))
                self.assertEqual(model.r[2], 1); self.assertFalse(model.calls)
                traces.append(external_trace(model)); coverage[index].update(model.visits)
            self.assertEqual(traces[0], traces[2]); self.assertEqual(traces[1], traces[2]); count += 1
        self.assertEqual(count, 6480)
        self.assertEqual([len(values) for values in coverage], [66, 66, 66])
        for visits in coverage:
            self.assertEqual(set(range(screen.ENTRY, screen.ENTRY+276, 4))-visits,
                             {0x15141600, 0x15141648, 0x15141668})

    def test_bounded_unchecked_period_loops(self):
        count = 0
        for period, elapsed in ((0, 4), (-1, 4), (float('-inf'), 4), (4, float('inf')),
                               (number_value(1), 4), (number_value(0x00800000), 4)):
            memory, actor = memory_case(elapsed, 0.25, period)
            self.assertIsNone(reference(memory, actor))
            for body in (self.raw, self.normalized, self.retail):
                model = EnvelopeOracle(body, memory, actor)
                with self.assertRaisesRegex(AssertionError, '^triangle instruction budget exhausted$'):
                    model.run()
                stores = [event for event in model.events if event[0] == 'W' and event[1] == actor+0x17C]
                self.assertEqual(len(stores), 9995); self.assertFalse(model.calls); count += 1
        self.assertEqual(count, 18)

    def test_native_actual_source_full_storage_and_live_timestep_aliases(self):
        self.run_host(r'''
static f32 times[]={-1,0,1,1.5f,2,2.5f,3,3.5f,4,5}, steps[]={0,0.25f,1,4};
static f32 periods[]={2,4,8}, amps[]={0,10,-4}, baselines[]={-2,0,5};
int a,b,c,d,e,f,count=0;
for(a=0;a<10;a++) for(b=0;b<4;b++) for(c=0;c<3;c++) for(d=0;d<3;d++)
for(e=0;e<3;e++) for(f=0;f<3;f++) {
    initialize(times[a],steps[b],periods[c],d,amps[e],baselines[f]);
    if(!reference() || func_151415D4(actor(&live))!=1 || check(0)) return 1;
    count++;
}
if(count!=3240) return 2;
''')

    def test_special_float_inputs_and_classified_arithmetic_only(self):
        accepted = 0; deferred = 0
        for elapsed, field, pattern in itertools.product((0.5, 2.5, 3.5), FIELDS, PATTERNS):
            memory, actor = memory_case(elapsed, 0.25, 4)
            put(memory, field if field == TIME else actor+field, pattern)
            wanted = reference(memory, actor)
            if wanted is None:
                deferred += 1; continue
            traces = []; outputs = []
            for body in (self.raw, self.normalized, self.retail):
                model = EnvelopeOracle(body, memory, actor).run()
                actual = external(model.memory)
                for offset in (0x17C, *((0x158,) if arithmetic_output(memory, actor) else ())):
                    address = actor+offset
                    if math.isnan(number(actual, address)) and math.isnan(number(wanted, address)):
                        put(actual, address, read(wanted, address))
                self.assertEqual(actual, wanted); self.assertEqual(model.r[2], 1)
                traces.append(external_trace(model)); outputs.append(external(model.memory))
            self.assertEqual(traces[1], traces[2]); self.assertEqual(outputs[1], outputs[2]); accepted += 1
        self.assertEqual(accepted+deferred, 360)
        self.run_host(r'''
static u32 patterns[]={0,0x80000000,1,0x80000001,0x007FFFFF,0x00800000,
    0x7F7FFFFF,0xFF7FFFFF,0x7F800000,0xFF800000,0x7FC12345,0x7F812345};
static int fields[]={0x170,0x174,0x178,0x17C,0x180,0x184,0x188,0x18C,0x190};
static f32 times[]={0.5f,2.5f,3.5f};
int a,b,c,count=0;
for(a=0;a<3;a++) for(b=0;b<10;b++) for(c=0;c<12;c++) {
    initialize(times[a],0.25f,4,0,10,-2);
    if(b==9) *timeStep(&live)=number(patterns[c]); else store(&live,fields[b],number(patterns[c]));
    if(!reference()) continue;
    if(func_151415D4(actor(&live))!=1 || check(1)) return 1;
    count++;
}
if(count!=EXPECTED) return 2;
'''.replace('EXPECTED', str(accepted)))
        (self.output/'special-floats.json').write_text(json.dumps(dict(accepted=accepted, deferred=deferred))+'\n')

    def test_compiler_scope_sum_and_profile_controls(self):
        records = []
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                self.assertEqual(record['diagnostics'], ''); self.assertFalse(record['exact']); records.append(record)
        self.assertEqual(len(records), 32)
        (self.output/'controls.json').write_text(json.dumps(records, indent=2)+'\n')

    def test_compiled_negative_semantics(self):
        controls = {
            'start-gate': screen.SELECTED.replace('< *(f32 *)(actor + 0x180)', '<= *(f32 *)(actor + 0x180)'),
            'end-gate': screen.SELECTED.replace('< *(f32 *)(runtime + 0x14)', '<= *(f32 *)(runtime + 0x14)'),
            'fall-gate': screen.SELECTED.replace('< *(f32 *)(runtime + 0x18)', '<= *(f32 *)(runtime + 0x18)'),
            'rise-scale': screen.SELECTED.replace('runtime + 0x20', 'runtime + 0x1C', 1),
            'fall-scale': screen.SELECTED.replace('1.0f -', '2.0f -'),
            'plateau': screen.SELECTED.replace('= *(f32 *)(runtime + 0);', '= *(f32 *)(runtime + 4);'),
            'wrap-gate': screen.SELECTED.replace('while (period <', 'while (period <='),
            'single-wrap': screen.SELECTED.replace('while (period <', 'if (period <'),
            'captured-step': screen.SELECTED.replace('    f32 period;', '    f32 period;\n    f32 step;').replace(
                '    runtime =', '    step = D_800BE9A4;\n    runtime =', 1).replace('+= D_800BE9A4;', '+= step;'),
            'wrong-return': screen.SELECTED.replace('return 1;', 'return 0;'),
            'stub': 's32 func_151415D4(u8 *actor) { return 0; }',
        }
        witnesses = []
        for name, body in controls.items():
            _, words = screen.compile_candidate(self.root, self.output, 'negative-'+name, body)
            differences = 0
            for elapsed, step, alias in itertools.product((1, 2, 3, 4, 9), (0, 0.25, 4), (0, 2)):
                memory, actor = memory_case(elapsed, step, 4)
                if alias:
                    memory, actor = memory_case(elapsed, step, 4, alias)
                wanted = reference(memory, actor)
                model = EnvelopeOracle(words, memory, actor).run()
                retail = EnvelopeOracle(self.retail, memory, actor).run()
                if external(model.memory) != wanted or model.r[2] != 1 or external_trace(model) != external_trace(retail):
                    differences += 1
            self.assertGreater(differences, 0, name)
            witnesses.append(dict(name=name, cases=30, differences=differences))
        (self.output/'negatives.json').write_text(json.dumps(witnesses, indent=2)+'\n')

    def test_production_source_complete_slot_and_guard_metadata(self):
        owner = (self.root/'conker/src/game_16DC80.c').read_text()
        self.assertIn(screen.SELECTED, owner)
        self.assertIn('s32 func_151415D4(u8 *actor);', owner)
        production = load_elf_functions(str(self.root/'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        self.assertEqual(production['func_151415D4'], self.retail)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        guards = [row for row in rows if row['function'] == 'func_151415D4']
        self.assertEqual((len(rows), len(guards)), (10760, 13))
        for row, offset in zip(guards, OFFSETS):
            self.assertEqual(int(row['offset'], 0), offset)
            self.assertEqual((int(row['expected'], 0), int(row['replacement'], 0)),
                             (self.raw[offset//4], self.normalized[offset//4]))
            self.assertEqual((row['filename'], row['expected_relocations'], row['replacement_relocations'],
                              row['insert_after'], row['insert_after_relocations'], row['omit']),
                             ('game_16DC80', '-', '-', '', '', 'false'))


def number_value(word):
    return struct.unpack('>f', struct.pack('>I', word))[0]


if __name__ == '__main__':
    unittest.main()
