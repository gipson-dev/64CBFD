"""Timed random targets, live sampling and the saved runtime-pointer lifetime."""

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

from tools.experiments import game_timed_interpolation_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_grid_channel_updater_match import GridOracle, STACK, external, read, put
from tools.tests import test_game_random_curve_record as native
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly
from pad_generated_object import parse_object

ENTRY, TIME, FLOAT, INTEGER = screen.ENTRY, 0x800BE9A4, 0x150ADA68, 0x150ADA20
ACTOR, ALTERNATE, SECOND = 0x20000, 0x23000, 0x24000
STACK_WORDS = (0x58, 0x64, 0x6C, 0x70, 0x94, 0x98)
FLOAT_WORDS = (0x4C, 0x84, 0xAC)


def normalize(words):
    result = list(words)
    for offset in STACK_WORDS:
        word = result[offset//4]
        assert word >> 26 in (35, 43) and word >> 21&31 == 29 and word&65535 == 0x20
        result[offset//4] = word&0xFFFF0000 | 0x24
    for offset in FLOAT_WORDS:
        word = result[offset//4]
        assert word >> 26 == 17 and word >> 21&31 == 16 and word&63 in (0, 2)
        fs, ft = word >> 11&31, word >> 16&31
        result[offset//4] = word&~((31<<11)|(31<<16)) | fs<<16 | ft<<11
    return result


def rounded_bits(value):
    try:
        return bits(value)
    except OverflowError:
        return 0xFF800000 if value < 0 else 0x7F800000


def rounded(value):
    return floating(rounded_bits(value))


def number(memory, address):
    return floating(read(memory, address))


def mutate(memory, actor, stage, enabled):
    if not enabled:
        return
    for offset, value in ((0x158, 10.0+stage), (0x170, 1.0+stage), (0x174, -3.0-stage),
                          (0x178, 12.0+stage), (0x17C, 21.0+stage), (0x180, 8.0+stage),
                          (0x184, 4.0+stage), (0x188, 0.75)):
        put(memory, actor+offset, bits(value))
    put(memory, TIME, bits(-2.0-stage))


def snapshot(memory, actor):
    return bytes(memory[actor+i] for i in range(0x110, 0x18C)), read(memory, TIME)


def memory_case(timer=-1.0, step=0.25, alias=False):
    actor = TIME-0x180 if alias else ACTOR
    memory = {STACK+i: 0xA5 for i in range(-0x600, 0x100)}
    for base, length in ((actor-16, 0x1E0), (TIME-16, 48), (ALTERNATE-16, 80), (SECOND-16, 80)):
        memory.update({base+i: (i*17+13)&255 for i in range(length)})
    for offset, value in ((0x158, 3.0), (0x170, 2.0), (0x174, -4.0), (0x178, 9.0),
                          (0x17C, 5.0), (0x180, timer), (0x184, 2.5), (0x188, 0.125)):
        put(memory, actor+offset, bits(value))
    for base, sign in ((ALTERNATE, 1), (SECOND, -1)):
        for offset, value in ((0, 11), (4, -7), (8, 19), (12, 23), (16, 31), (20, 5), (24, 0.5)):
            put(memory, base+offset, bits(value*sign))
    put(memory, TIME, bits(step))
    return memory, actor


def reference(memory, actor, samples, integer, mutation=False, redirects=(0, 0)):
    memory = dict(memory)
    calls = []
    timer = rounded(number(memory, actor+0x180)-number(memory, TIME))
    put(memory, actor+0x180, rounded_bits(timer))
    if timer < 0:
        calls.append((FLOAT, snapshot(memory, actor), None))
        mutate(memory, actor, 1, mutation)
        put(memory, actor+0x180, rounded_bits(samples[0]*number(memory, actor+0x184)))
        calls.append((INTEGER, snapshot(memory, actor), actor+0x170))
        mutate(memory, actor, 2, mutation)
        runtime = redirects[0] or actor+0x170
        calls.append((FLOAT, snapshot(memory, actor), runtime))
        mutate(memory, actor, 3, mutation)
        runtime = redirects[1] or runtime
        low_offset, high_offset = (4, 0) if integer&3 else (0, 8)
        low = number(memory, runtime+low_offset)
        delta = rounded(number(memory, runtime+high_offset)-low)
        put(memory, runtime+12, rounded_bits(rounded(samples[1]*delta)+low))
    current = number(memory, actor+0x158)
    delta = rounded(number(memory, actor+0x17C)-current)
    put(memory, actor+0x158, rounded_bits(current+rounded(delta*number(memory, actor+0x188))))
    return external(memory), calls


class InterpolationOracle(GridOracle):
    def __init__(self, words, memory, actor, samples, integer, mutation=False, phase=0,
                 home=0x20, redirects=(0, 0)):
        super().__init__(words, memory, entry=ENTRY, arguments=(actor,), phase=phase)
        self.actor, self.samples, self.integer, self.mutation = actor, samples, integer, mutation
        self.stage, self.float_calls = 0, 0
        self.home, self.redirects = STACK+phase-0x30+home, redirects

    def execute(self, word):
        if word >> 26 == 17 and word >> 21&31 == 16 and word&63 in (0, 1, 2):
            fs, ft, fd, fn = word >> 11&31, word >> 16&31, word >> 6&31, word&63
            left, right = floating(self.f[fs]), floating(self.f[ft])
            value = (lambda: left+right, lambda: left-right, lambda: left*right)[fn]()
            self.f[fd] = rounded_bits(value)
        else:
            super().execute(word)

    def record_call(self, target):
        assert target in (FLOAT, INTEGER)
        call = (target, snapshot(self.memory, self.actor), self.r[3] if self.stage else None)
        self.calls.append(call)
        self.events.append(('CALL', target, call[1:]))

    def hook(self, target):
        self.stage += 1
        mutate(self.memory, self.actor, self.stage, self.mutation)
        if self.stage in (2, 3) and self.redirects[self.stage-2]:
            self.put(self.home, self.redirects[self.stage-2], 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]
        if target == FLOAT:
            self.f[0] = rounded_bits(self.samples[self.float_calls])
            self.float_calls += 1
        else:
            self.r[2] = self.integer


def external_trace(model):
    return [event for event in model.events if not STACK-0x600 <= event[1] < STACK+0x100]


def native_fixture(body):
    return r'''
typedef unsigned char u8; typedef unsigned int u32; typedef int s32; typedef float f32;
typedef struct { union { u32 align; u8 bytes[0x1E0]; } storage; f32 step; } State;
static State live, shadow;
static u8 expected[3][0x1E0];
static u32 expectedStep[3], samples[2], randomWord;
static int alias, mutation, stage, expectedCalls, error;
static u8 *actor(State *s) { return s->storage.bytes+16; }
static f32 *timeStep(State *s) { return alias?(f32 *)(actor(s)+0x180):&s->step; }
#define D_800BE9A4 (*timeStep(&live))
static u32 bits(f32 v) { union { u32 u; f32 f; } w; w.f=v; return w.u; }
static f32 number(u32 v) { union { u32 u; f32 f; } w; w.u=v; return w.f; }
static f32 load(State *s,int offset) { return *(f32 *)(actor(s)+offset); }
static void store(State *s,int offset,f32 value) { *(f32 *)(actor(s)+offset)=value; }
static int nanWord(u32 u) { return (u&0x7FFFFFFF)>0x7F800000; }
static void mutateState(State *s,int n) {
    if(!mutation) return;
    store(s,0x158,10.0f+n); store(s,0x170,1.0f+n); store(s,0x174,-3.0f-n);
    store(s,0x178,12.0f+n); store(s,0x17C,21.0f+n); store(s,0x180,8.0f+n);
    store(s,0x184,4.0f+n); store(s,0x188,0.75f); *timeStep(s)=-2.0f-n;
}
static void capture(int n) {
    int i;
    for(i=0;i<0x1E0;i++) expected[n][i]=shadow.storage.bytes[i];
    expectedStep[n]=bits(*timeStep(&shadow));
}
static void callback(void) {
    int i;
    if(stage>=expectedCalls) { error=1; return; }
    for(i=0;i<0x1E0;i++) if(live.storage.bytes[i]!=expected[stage][i]) error=2;
    if(bits(*timeStep(&live))!=expectedStep[stage]) error=3;
    mutateState(&live,++stage);
}
__attribute__((noinline)) f32 func_150ADA68(void) {
    int n=stage;
    if(n!=0 && n!=2) error=4;
    callback(); return number(samples[n==0?0:1]);
}
__attribute__((noinline)) s32 func_150ADA20(void) {
    if(stage!=1) error=5;
    callback(); return (s32)randomWord;
}
static void initialize(u32 timer,u32 step,int useAlias,int change) {
    int i;
    alias=useAlias; mutation=change; stage=expectedCalls=error=0;
    for(i=0;i<0x1E0;i++) live.storage.bytes[i]=(u8)(i*17+13);
    store(&live,0x158,3); store(&live,0x170,2); store(&live,0x174,-4); store(&live,0x178,9);
    store(&live,0x17C,5); store(&live,0x180,number(timer)); store(&live,0x184,2.5f);
    store(&live,0x188,0.125f); *timeStep(&live)=number(step);
}
static void reference(void) {
    volatile f32 timer,delta,product;
    f32 low,high;
    int i;
    for(i=0;i<0x1E0;i++) shadow.storage.bytes[i]=live.storage.bytes[i];
    shadow.step=live.step;
    timer=load(&shadow,0x180)-*timeStep(&shadow); store(&shadow,0x180,timer);
    if(timer<0) {
        expectedCalls=3; capture(0); mutateState(&shadow,1);
        product=number(samples[0])*load(&shadow,0x184); store(&shadow,0x180,product);
        capture(1); mutateState(&shadow,2); capture(2); mutateState(&shadow,3);
        low=load(&shadow,randomWord&3?0x174:0x170);
        high=load(&shadow,randomWord&3?0x170:0x178);
        delta=high-low; product=number(samples[1])*delta;
        store(&shadow,0x17C,product+low);
    }
    delta=load(&shadow,0x17C)-load(&shadow,0x158);
    product=delta*load(&shadow,0x188);
    store(&shadow,0x158,load(&shadow,0x158)+product);
}
static int check(int classify) {
    int i,j;
    if(error || stage!=expectedCalls) return 1;
    for(i=0;i<0x1E0;i++) {
        if(classify && (i==16+0x158 || i==16+0x180 || (expectedCalls && i==16+0x17C))) {
            u32 a=bits(*(f32 *)(live.storage.bytes+i)), b=bits(*(f32 *)(shadow.storage.bytes+i));
            if(a!=b && !(nanWord(a)&&nanWord(b))) return 2;
            i+=3;
        } else if(live.storage.bytes[i]!=shadow.storage.bytes[i]) return 3;
    }
    if(bits(live.step)!=bits(shadow.step)) return 4;
    for(j=0;j<3;j++) for(i=0;i<0x1E0;i++) expected[j][i]=0;
    return 0;
}
''' + body + '\n'


class GameTimedInterpolationMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-timed-interpolation-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.normalized = normalize(cls.raw)
        cls.retail = list(struct.unpack_from('>59I', (cls.root/'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        owner = (cls.root/'conker/src/game_16DC80.c').read_text()
        cls.body = re.search(r's32 func_15141478\([^;{}]+\) \{\n.*?\n\}', owner, re.S).group(0)
        cls.fixture = native_fixture(cls.body)

    def test_derived_private_slot_and_commutative_operands_complete_slot(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['diagnostics']), (59, 48, 9, ''))
        self.assertEqual(self.normalized, self.retail)
        self.assertEqual([i*4 for i, pair in enumerate(zip(self.raw, self.retail)) if pair[0] != pair[1]],
                         sorted((*STACK_WORDS, *FLOAT_WORDS)))
        for old, new in zip(self.raw, self.normalized):
            self.assertEqual(old >> 26, new >> 26)
        text, functions, relocations = parse_object(self.output/'selected.o')
        start = functions['func_15141478']['value']
        raw = list(struct.unpack_from('>59I', text, start))
        fields = ('filename', 'function', 'offset', 'expected', 'replacement', 'expected_relocations',
                  'replacement_relocations', 'note', 'insert_after', 'insert_after_relocations', 'omit')
        with (self.output/'guards.csv').open('w', newline='') as stream:
            writer = csv.writer(stream)
            writer.writerow(fields)
            for offset in sorted((*STACK_WORDS, *FLOAT_WORDS)):
                self.assertNotIn(start+offset, relocations)
                writer.writerow(('game_16DC80', 'func_15141478', hex(offset), '0x%08X'%raw[offset//4],
                    '0x%08X'%normalize(raw)[offset//4], '-', '-',
                    'Normalize timed interpolation private pointer slot and commutative FP operands', '', '', 'false'))
        layout = self.output/'layout.csv'
        layout.write_text('version,section,filename,function,address,end\n'
                          'us,game,game_16DC80,func_15141478,0x15141478,0x15141564\n')
        assembly = emit_padded_assembly(self.output/'selected.o', layout, 'game_16DC80',
                                       word_patches_path=self.output/'guards.csv')
        (self.output/'padded.s').write_text(assembly)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(self.output/'padded.o'),
                        str(self.output/'padded.s')], check=True, capture_output=True)
        _, padded_functions, padded_relocations = parse_object(self.output/'padded.o')
        self.assertEqual(padded_functions['func_15141478']['size'], 236)
        self.assertEqual(padded_relocations, relocations)
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output/'interpolation.ld'),
                        '-e', 'func_15141478', *['--defsym=%s=0x%X'%item for item in screen.SYMBOLS.items()],
                        '-o', str(self.output/'padded.elf'), str(self.output/'padded.o')], check=True, capture_output=True)
        linked = load_elf_functions(str(self.output/'padded.elf'), 'mips-linux-gnu-objdump')[0]['func_15141478']
        self.assertEqual(linked[:59], self.retail)
        self.assertFalse(any(linked[59:]))

    def test_guest_complete_storage_calls_access_order_return_and_every_word(self):
        coverage = [set(), set(), set()]
        count = 0
        for timer, step, first, second, integer, mutation, alias, phase in itertools.product(
                (-1.0, -0.0, 0.0, 0.25, 1.0), (0.0, 0.25, 0.5), (0.0, 0.25, 1.0),
                (0.0, 0.25, 1.0), (0, 1, 2, 3, 4, 5, 0x80000000, 0xFFFFFFFF),
                (False, True), (False, True), (0, 8)):
            memory, actor = memory_case(timer, step, alias)
            samples = (first, second)
            wanted = reference(memory, actor, samples, integer, mutation)
            traces = []
            for i, (body, home) in enumerate(((self.raw, 0x20), (self.normalized, 0x24), (self.retail, 0x24))):
                model = InterpolationOracle(body, memory, actor, samples, integer, mutation, phase, home).run()
                self.assertEqual((external(model.memory), model.calls), wanted, (count, i))
                self.assertEqual(model.r[2], 1)
                coverage[i].update(model.visits)
                traces.append(external_trace(model))
            self.assertEqual(traces[0], traces[2])
            self.assertEqual(traces[1], traces[2])
            count += 1
        self.assertEqual(count, 8640)
        self.assertEqual([len(words) for words in coverage], [59, 59, 59])
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=count, bodies=3, covered_words=59))+'\n')

    def test_private_pointer_redirection_across_both_random_callbacks(self):
        count = 0
        for earlier, later, integer, sample, mutation, phase in itertools.product(
                (0, ALTERNATE, SECOND), (0, ALTERNATE, SECOND), (0, 1, 3, 0xFFFFFFFF),
                (0.0, 0.25, 1.0), (False, True), (0, 8)):
            memory, actor = memory_case()
            redirects = (earlier, later)
            samples = (sample, 1-sample)
            wanted = reference(memory, actor, samples, integer, mutation, redirects)
            for body, home in ((self.raw, 0x20), (self.normalized, 0x24), (self.retail, 0x24)):
                model = InterpolationOracle(body, memory, actor, samples, integer, mutation, phase, home, redirects).run()
                self.assertEqual((external(model.memory), model.calls), wanted)
                self.assertEqual(model.r[2], 1)
            count += 1
        self.assertEqual(count, 432)

    def test_native_actual_body_whole_storage_and_callback_live_reads(self):
        self.run_host(r'''
static f32 timers[]={-1,-0.0f,0,0.25f,1}, steps[]={0,0.25f,0.5f}, fractions[]={0,0.25f,1};
static u32 words[]={0,1,2,3,4,5,0x80000000,0xFFFFFFFF};
int a,b,c,d,e,f,g,count=0;
for(a=0;a<5;a++) for(b=0;b<3;b++) for(c=0;c<3;c++) for(d=0;d<3;d++)
for(e=0;e<8;e++) for(f=0;f<2;f++) for(g=0;g<2;g++) {
    initialize(bits(timers[a]),bits(steps[b]),g,f); samples[0]=bits(fractions[c]);
    samples[1]=bits(fractions[d]); randomWord=words[e]; reference();
    if(func_15141478(actor(&live))!=1 || check(0)) return 1;
    count++;
}
if(count!=4320) return 2;
''')

    def test_special_float_raw_inputs_and_classified_arithmetic_outputs(self):
        patterns = (0, 0x80000000, 1, 0x80000001, 0x007FFFFF, 0x00800000,
                    0x7F7FFFFF, 0xFF7FFFFF, 0x7F800000, 0xFF800000, 0x7FC12345, 0x7F812345)
        locations = (TIME, 0x158, 0x170, 0x174, 0x178, 0x17C, 0x180, 0x184, 0x188)
        count = 0
        for location, pattern, integer, phase in itertools.product(locations, patterns, (0, 1), (0, 8)):
            memory, actor = memory_case()
            put(memory, location if location == TIME else actor+location, pattern)
            samples = (0.25, 0.75)
            models = [InterpolationOracle(body, memory, actor, samples, integer, phase=phase, home=home).run()
                      for body, home in ((self.raw, 0x20), (self.normalized, 0x24), (self.retail, 0x24))]
            self.assertEqual(external(models[1].memory), external(models[2].memory))
            self.assertEqual(external_trace(models[1]), external_trace(models[2]))
            wanted, calls = reference(memory, actor, samples, integer)
            for model in models:
                actual = external(model.memory)
                for offset in (0x158, 0x180, *((0x17C,) if calls else ())):
                    address = actor+offset
                    if math.isnan(number(actual, address)) and math.isnan(number(wanted, address)):
                        put(actual, address, read(wanted, address))
                self.assertEqual(actual, wanted)
                self.assertEqual([call[0] for call in model.calls], [call[0] for call in calls])
                self.assertEqual(model.r[2], 1)
            count += 1
        self.assertEqual(count, 432)
        self.run_host(r'''
static u32 patterns[]={0,0x80000000,1,0x80000001,0x007FFFFF,0x00800000,
    0x7F7FFFFF,0xFF7FFFFF,0x7F800000,0xFF800000,0x7FC12345,0x7F812345};
static int offsets[]={0x158,0x170,0x174,0x178,0x17C,0x180,0x184,0x188};
int a,b,c;
for(a=0;a<9;a++) for(b=0;b<12;b++) for(c=0;c<2;c++) {
    initialize(bits(-1.0f),bits(0.25f),0,0);
    if(a==8) *timeStep(&live)=number(patterns[b]); else store(&live,offsets[a],number(patterns[b]));
    samples[0]=bits(0.25f); samples[1]=bits(0.75f); randomWord=c; reference();
    if(func_15141478(actor(&live))!=1 || check(1)) return 1;
}
for(a=0;a<12;a++) for(b=0;b<12;b++) for(c=0;c<2;c++) {
    initialize(bits(-1.0f),bits(0.25f),0,0);
    samples[0]=patterns[a]; samples[1]=patterns[b]; randomWord=c; reference();
    if(func_15141478(actor(&live))!=1 || check(1)) return 2;
}
''')

    def test_special_random_samples_in_guest_model(self):
        patterns = (0, 0x80000000, 1, 0x80000001, 0x007FFFFF, 0x00800000,
                    0x7F7FFFFF, 0xFF7FFFFF, 0x7F800000, 0xFF800000, 0x7FC12345, 0x7F812345)
        count = 0
        for first, second, integer, phase in itertools.product(patterns, patterns, (0, 1), (0, 8)):
            memory, actor = memory_case()
            samples = (floating(first), floating(second))
            wanted, calls = reference(memory, actor, samples, integer)
            models = [InterpolationOracle(body, memory, actor, samples, integer, phase=phase, home=home).run()
                      for body, home in ((self.raw, 0x20), (self.normalized, 0x24), (self.retail, 0x24))]
            self.assertEqual(external(models[1].memory), external(models[2].memory))
            self.assertEqual(external_trace(models[1]), external_trace(models[2]))
            for model in models:
                actual = external(model.memory)
                for offset in (0x158, 0x180, *((0x17C,) if calls else ())):
                    address = actor+offset
                    if math.isnan(number(actual, address)) and math.isnan(number(wanted, address)):
                        put(actual, address, read(wanted, address))
                self.assertEqual(actual, wanted)
                self.assertEqual([call[0] for call in model.calls], [call[0] for call in calls])
                self.assertEqual(model.r[2], 1)
            count += 1
        self.assertEqual(count, 576)

    def test_production_source_complete_slot_and_guard_metadata(self):
        self.assertEqual(self.body, screen.SELECTED)
        owner = (self.root/'conker/src/game_16DC80.c').read_text()
        self.assertIn('s32 func_15141478(u8 *actor);', owner)
        self.assertNotIn('s32 func_15141478();', owner)
        linked, _, addresses = load_elf_functions(str(self.root/'conker/build/conker.us.elf'),
                                                 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_15141478'], ENTRY)
        self.assertEqual(linked['func_15141478'], self.retail)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        guards = [row for row in rows if row['function'] == 'func_15141478']
        self.assertEqual((len(rows), len(guards)), (10760, 9))
        self.assertEqual([int(row['offset'], 0) for row in guards], sorted((*STACK_WORDS, *FLOAT_WORDS)))
        for row in guards:
            offset = int(row['offset'], 0)//4
            self.assertEqual((int(row['expected'], 0), int(row['replacement'], 0)),
                             (self.raw[offset], self.normalized[offset]))
            self.assertEqual((row['filename'], row['expected_relocations'], row['replacement_relocations'],
                              row['insert_after'], row['insert_after_relocations'], row['omit']),
                             ('game_16DC80', '-', '-', '', '', 'false'))

    def test_compiler_profile_and_source_shape_controls(self):
        records = []
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                self.assertEqual(record['diagnostics'], '')
                self.assertFalse(record['exact'])
                records.append(record)
        self.assertEqual(len(records), 32)
        (self.output/'controls.json').write_text(json.dumps(records, indent=2)+'\n')

    def test_compiled_negative_semantics_are_observably_different(self):
        controls = {
            'zero-expiry': screen.SELECTED.replace('< 0.0f', '<= 0.0f'),
            'wrong-mask': screen.SELECTED.replace('& 3', '& 1'),
            'reset-scale': screen.SELECTED.replace('runtime + 0x14', 'runtime + 0x18'),
            'wrong-endpoint': screen.SELECTED.replace('runtime + 8', 'runtime + 4'),
            'missing-sample': screen.SELECTED.replace('            sample = func_150ADA68();', '            sample = 0.0f;'),
            'wrong-smoothing': screen.SELECTED.replace('runtime + 0x18', 'runtime + 0x14'),
            'wrong-return': screen.SELECTED.replace('return 1;', 'return 0;'),
            'stub': 's32 func_15141478(u8 *actor) { return 0; }',
            'captured-scale': screen.SELECTED.replace('    f32 sample;', '    f32 sample;\n    f32 scale;').replace(
                '        sample = func_150ADA68();',
                '        scale = *(f32 *)(runtime + 0x14);\n        sample = func_150ADA68();', 1).replace(
                'sample * *(f32 *)(runtime + 0x14)', 'sample * scale'),
            'captured-endpoints': screen.SELECTED.replace('    f32 sample;', '    f32 sample;\n    f32 low;\n    f32 high;').replace(
                '            sample = func_150ADA68();\n            *(f32 *)(runtime + 0xC) = sample * (*(f32 *)(runtime + 0) - *(f32 *)(runtime + 4)) + *(f32 *)(runtime + 4);',
                '            low = *(f32 *)(runtime + 4);\n            high = *(f32 *)(runtime + 0);\n'
                '            sample = func_150ADA68();\n            *(f32 *)(runtime + 0xC) = sample * (high - low) + low;'),
        }
        witnessed = []
        for name, body in controls.items():
            _, words = screen.compile_candidate(self.root, self.output, 'negative-'+name, body)
            differences = 0
            for timer, integer, mutation in itertools.product((0.25, -1.0), (0, 2), (False, True)):
                memory, actor = memory_case(timer)
                wanted = reference(memory, actor, (0.25, 0.75), integer, mutation)
                model = InterpolationOracle(words, memory, actor, (0.25, 0.75), integer, mutation).run()
                if (external(model.memory), model.calls) != wanted or model.r[2] != 1:
                    differences += 1
            self.assertGreater(differences, 0, name)
            witnessed.append(dict(name=name, cases=8, differences=differences))
        (self.output/'negatives.json').write_text(json.dumps(witnessed, indent=2)+'\n')


if __name__ == '__main__':
    unittest.main()
