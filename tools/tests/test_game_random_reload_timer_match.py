"""Bounded timer/callback qualification, including the retail divide-zero trap."""

import csv
import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_random_reload_timer_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import signed
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native


ENTRY = screen.ENTRY
OBJECT, STEP = 0x20000, 0x800BE9E4
DISPATCH, RANDOM = 0x150D278C, 0x150ADA20
FLAGS = (0, 1, 2, 3, 0x7E, 0x80, 0xFE, 0xFF)
TIMERS = (0, 1, 7, 0x7FFFFFFF, 0x80000000, 0x80000001, 0xFFFFFFFE, 0xFFFFFFFF)
STEPS = (0, 1, 2, 7, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFF)
RANGES = (0, 1, 7, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFE)
BASES = (0, 1, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFF)
RANDOMS = (0, 1, 2, 7, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFE, 0xFFFFFFFF)


def memory_case(flag=1, timer=0, step=1, base=0, limit=7):
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({OBJECT + i: 0xA5 for i in range(-16, 144)})
    put(memory, OBJECT + 1, 0xFE, 1)
    put(memory, OBJECT + 0xC, 0x81, 1)
    put(memory, OBJECT + 0x78, flag, 1)
    for offset, value in ((0x28, 0x81234560), (0x2C, base), (0x30, limit), (0x34, timer), (0x38, 0xABCDEF01)):
        put(memory, OBJECT + offset, value)
    put(memory, STEP, step)
    return memory


def read(memory, address, size=4):
    return int.from_bytes(bytes(memory[address + i] for i in range(size)), 'big')


def external(memory):
    return {a: v for a, v in memory.items() if not STACK - 0x600 <= a < STACK + 0x100}


def actions(mode):
    changed = [(OBJECT + 0x2C, 0xFFFFFFFC, 4), (OBJECT + 0x30, 3, 4),
               (OBJECT + 0x28, 0x12345678, 4), (OBJECT + 0x34, 0x76543210, 4),
               (OBJECT + 0xC, 0x22, 1), (OBJECT + 1, 0x33, 1),
               (OBJECT + 0x78, 0, 1), (STEP, 99, 4)]
    return {} if not mode else {DISPATCH: changed} if mode == 1 else {RANDOM: changed} if mode == 2 else {
        DISPATCH: changed, RANDOM: [(OBJECT + 0x2C, 0x80000000, 4), (OBJECT + 0x30, 1, 4)]}


def reference(memory, random_word, mutations):
    memory = dict(memory)
    calls, writes = [], []
    trap = False
    if read(memory, OBJECT + 0x78, 1) & 1:
        timer = (read(memory, OBJECT + 0x34) - read(memory, STEP)) & 0xFFFFFFFF
        put(memory, OBJECT + 0x34, timer)
        writes.append((OBJECT + 0x34, 4, timer))
        if signed(timer) < 0:
            calls.append((DISPATCH, read(memory, OBJECT + 0x28), OBJECT + 0x38,
                          read(memory, OBJECT + 0xC, 1), read(memory, OBJECT + 1, 1)))
            for target in (DISPATCH, RANDOM):
                if target == RANDOM:
                    calls.append((RANDOM,))
                for address, value, size in mutations.get(target, ()):
                    put(memory, address, value, size)
                    writes.append((address, size, value & ((1 << (size * 8)) - 1)))
            divisor = (read(memory, OBJECT + 0x30) + 1) & 0xFFFFFFFF
            trap = divisor == 0
            if not trap:
                timer = (random_word % divisor + read(memory, OBJECT + 0x2C)) & 0xFFFFFFFF
                put(memory, OBJECT + 0x34, timer)
                writes.append((OBJECT + 0x34, 4, timer))
    return external(memory), calls, writes, trap


class DivideZeroTrap(Exception):
    pass


class TimerOracle(TriangleOracle):
    """Extend the existing guest runner only for this leaf's DIVU/MFHI/BREAK."""

    def __init__(self, words, memory, random_word=0, mutations=None, phase=0):
        super().__init__(words, memory, entry=ENTRY, arguments=(OBJECT,), phase=phase)
        self.random_word, self.mutations = random_word, mutations or {}
        self.hi = self.lo = 0

    def execute(self, word):
        op, rs, rt, rd, fn = word >> 26, word >> 21 & 31, word >> 16 & 31, word >> 11 & 31, word & 63
        if op == 0 and fn == 27:
            numerator, denominator = self.r[rs], self.r[rt]
            self.lo, self.hi = divmod(numerator, denominator) if denominator else (0xFFFFFFFF, numerator)
        elif op == 0 and fn == 16:
            self.r[rd] = self.hi
        elif word == 0x0007000D:
            raise DivideZeroTrap('retail break 7')
        else:
            super().execute(word)

    def record_call(self, target):
        assert target in (DISPATCH, RANDOM)
        self.calls.append((target, *self.arguments(4)) if target == DISPATCH else (target,))
        self.events.append(('CALL', target))

    def hook(self, target):
        for address, value, size in self.mutations.get(target, ()):
            self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.r[2] = self.random_word if target == RANDOM else 0x98765432


def writes(model):
    return [event[1:] for event in model.events if event[0] == 'W'
            and not STACK - 0x600 <= event[1] < STACK + 0x100]


class GameRandomReloadTimerMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-random-reload-timer-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'typed', screen.RECORD_TYPE + screen.DIRECT)
        _, cls.other = screen.compile_candidate(cls.root, cls.output, 'array')
        cls.retail = list(struct.unpack_from('>39I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = screen.TYPES + screen.RECORD_TYPE + r'''
s32 D_800BE9E4;
static u32 storage[40], expected[40], randomWord;
static int mode,callCount,error;
static u32 arguments[4];
static u8 *object;
static void mutation(int target) {
    ReloadRecord *r=(ReloadRecord *)(object+0x28);
    if((mode==1 && target==0) || (mode==2 && target==1) || (mode==3 && target==0)) {
        r->base=0xFFFFFFFC;r->range=3;r->command=0x12345678;r->timer=0x76543210;
        object[0xC]=0x22;object[1]=0x33;object[0x78]=0;D_800BE9E4=99;
    }
    if(mode==3 && target==1) {r->base=0x80000000;r->range=1;}
}
s32 func_150D278C(u32 command,void *parameters,int channel,int identity) {
    if(callCount++!=0) error=1;
    arguments[0]=command;arguments[1]=(u32)parameters;arguments[2]=channel;arguments[3]=identity;
    mutation(0);return (s32)0x98765432;
}
s32 func_150ADA20(void) {
    if(callCount++!=1) error=2;
    mutation(1);return (s32)randomWord;
}
''' + screen.DIRECT + '\n'

    def check_case(self, memory, random_word=0, mutations=None, phase=0):
        mutations = mutations or {}
        expected, calls, stores, trap = reference(memory, random_word, mutations)
        coverage = set()
        for words in (self.retail, self.words, self.other):
            model = TimerOracle(words, memory, random_word, mutations, phase)
            caught = False
            try:
                model.run()
            except DivideZeroTrap:
                caught = True
            self.assertEqual(caught, trap)
            self.assertEqual(external(model.memory), expected)
            self.assertEqual(model.calls, calls)
            self.assertEqual(writes(model), stores)
            enabled = bool(read(memory, OBJECT + 0x78, 1) & 1)
            self.assertEqual(sum(event[0] == 'R' and event[1] == STEP for event in model.events), int(enabled))
            if calls:
                first_call = next(i for i, event in enumerate(model.events) if event[0] == 'CALL')
                timer_store = next(i for i, event in enumerate(model.events)
                                   if event[0] == 'W' and event[1] == OBJECT + 0x34)
                self.assertLess(timer_store, first_call)
                random_call = next(i for i, event in enumerate(model.events) if event[:2] == ('CALL', RANDOM))
                for offset in (0x2C, 0x30):
                    field_reads = [i for i, event in enumerate(model.events)
                                   if event[0] == 'R' and event[1] == OBJECT + offset]
                    self.assertEqual(len(field_reads), 1)
                    self.assertGreater(field_reads[0], random_call)
            if words is self.retail:
                coverage.update(model.visits)
        return coverage

    def test_existing_profile_direct_match_and_typed_record_frame(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['diagnostics']), (39, 0x20, 0, ''))
        self.assertEqual(self.words, self.retail)
        self.assertEqual((len(self.other), (-self.other[0]) & 65535,
                          sum(a != b for a, b in zip(self.other, self.retail))), (39, 0x28, 14))

    def test_named_compiler_controls(self):
        forms = screen.candidates()
        self.assertEqual((len(forms), len(dict(forms))), (19, 19))
        expected = {'unsigned-record': (39, 0x28, 14), 'signed-record': (39, 0x28, 14),
                    'explicit-store': (39, 0x28, 14), 'early-exit': (40, 0x28, 36),
                    'signed-modulo': (45, 0x28, 25), 'separate-pointer-assignment': (39, 0x28, 14),
                    'register-pointer': (39, 0x28, 14), 'void-argument': (39, 0x28, 12),
                    'reverse-addends': (39, 0x28, 7), 'signed-count': (39, 0x28, 14),
                    'scope-pointer': (39, 0x30, 36), 'named-random': (39, 0x28, 14),
                    'register-random': (39, 0x28, 14), 'typed-record': (39, 0x20, 0),
                    'typed-record-reversed': (39, 0x20, 0), 'void-return-declaration': (39, 0x28, 7),
                    'no-public-return': (39, 0x28, 7), 'volatile-pointer': (47, 0x20, 42),
                    'volatile-object': (41, 0x20, 38)}
        for name, body in forms:
            record, _ = screen.compile_candidate(self.root, self.output, name, body)
            self.assertEqual((record['body_words'], record['frame'], record['differences']), expected[name])
            self.assertEqual(record['diagnostics'], '')

    def test_flags_signed_threshold_and_wrapped_subtraction(self):
        coverage = set()
        for flag, timer, step, phase in itertools.product(FLAGS, TIMERS, STEPS, (0, 8)):
            coverage.update(self.check_case(memory_case(flag, timer, step), phase=phase))
        self.assertEqual(len(FLAGS) * len(TIMERS) * len(STEPS) * 2, 896)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 156, 4)) - {ENTRY + 0x84})

    def test_unsigned_rng_ranges_wrapping_base_and_post_callback_reads(self):
        cases = 0
        for limit, base, word, mode, phase in itertools.product(RANGES, BASES, RANDOMS, range(4), (0, 8)):
            self.check_case(memory_case(base=base, limit=limit), word, actions(mode), phase)
            cases += 1
        self.assertEqual(cases, 1920)
        (self.output / 'behavior.json').write_text(json.dumps(dict(gate_cases=896, reload_cases=cases,
             models=3, reachable_nontrap_words=38), indent=2) + '\n')

    def test_zero_divisor_break_after_callbacks_before_reload_store(self):
        coverage = set()
        for word, phase, target in itertools.product(RANDOMS, (0, 8), (None, DISPATCH, RANDOM)):
            memory = memory_case(limit=0xFFFFFFFF if target is None else 7)
            mutations = {} if target is None else {target: [(OBJECT + 0x30, 0xFFFFFFFF, 4)]}
            coverage.update(self.check_case(memory, word, mutations, phase))
        self.assertIn(ENTRY + 0x84, coverage)
        self.assertEqual(len(RANDOMS) * 2 * 3, 48)

    def test_native_32bit_record_layout_and_complete_memory_footprint(self):
        self.run_host(r'''
u32 flags[]={0,1,2,3,0x7E,0x80,0xFE,0xFF};
u32 timers[]={0,1,7,0x7FFFFFFF,0x80000000,0x80000001,0xFFFFFFFE,0xFFFFFFFF};
u32 steps[]={0,1,2,7,0x7FFFFFFF,0x80000000,0xFFFFFFFF};
u32 ranges[]={0,1,7,0x7FFFFFFF,0x80000000,0xFFFFFFFE};
u32 bases[]={0,1,0x7FFFFFFF,0x80000000,0xFFFFFFFF};
u32 words[]={0,1,2,7,0x7FFFFFFF,0x80000000,0xFFFFFFFE,0xFFFFFFFF};
int pass,a,b,c,m,i;
ReloadRecord *r;
object=(u8 *)(storage+4);r=(ReloadRecord *)(object+0x28);
if(sizeof(void *)!=4 || (u8 *)&r->timer-(u8 *)r!=12 || r->parameters-(u8 *)r!=16) return 1;
for(pass=0;pass<2;pass++) for(a=0;a<(pass?6:8);a++) for(b=0;b<(pass?5:8);b++)
for(c=0;c<(pass?8:7);c++) for(m=0;m<(pass?4:1);m++) {
    u32 newTimer,expectedBase,expectedRange;
    int fired;
    for(i=0;i<40;i++) storage[i]=0xA5A5A5A5;
    object[0x78]=pass?1:flags[a];object[0xC]=0x81;object[1]=0xFE;
    r->command=0x81234560;r->base=pass?bases[b]:0;r->range=pass?ranges[a]:7;
    r->timer=pass?0:timers[b];D_800BE9E4=(s32)(pass?1:steps[c]);
    randomWord=pass?words[c]:0;mode=m;callCount=error=0;
    for(i=0;i<40;i++) expected[i]=storage[i];
    newTimer=r->timer-(u32)D_800BE9E4;
    fired=(object[0x78]&1) && (s32)newTimer<0;
    if(object[0x78]&1) expected[(0x10+0x34)/4]=newTimer;
    if(fired) {
        expectedBase=r->base;expectedRange=r->range;
        if(mode) {
            ReloadRecord *e=(ReloadRecord *)((u8 *)(expected+4)+0x28);
            u8 *o=(u8 *)(expected+4);
            e->base=0xFFFFFFFC;e->range=3;e->command=0x12345678;e->timer=0x76543210;
            o[0xC]=0x22;o[1]=0x33;o[0x78]=0;
            expectedBase=0xFFFFFFFC;expectedRange=3;
            if(mode==3) {e->base=0x80000000;e->range=1;expectedBase=e->base;expectedRange=e->range;}
        }
        expected[(0x10+0x34)/4]=randomWord%(expectedRange+1)+expectedBase;
    }
    func_150D26F0(object);
    if(error || callCount!=(fired?2:0)) return 2;
    if(fired && (arguments[0]!=0x81234560 || arguments[1]!=(u32)(object+0x38)
       || arguments[2]!=0x81 || arguments[3]!=0xFE)) return 3;
    for(i=0;i<40;i++) if(storage[i]!=expected[i]) return 4;
    if(fired && mode && D_800BE9E4!=99) return 5;
}
''')

    def test_missing_dispatch_and_pre_callback_capture_are_detected(self):
        bodies = [('placeholder', 's32 func_150D26F0(void) { return 0; }'),
                  ('wrong-flag', screen.RECORD_TYPE + screen.DIRECT.replace('object[0x78] & 1', 'object[0x78] & 2')),
                  ('early-fields', screen.RECORD_TYPE + screen.DIRECT
                   .replace('        if ((s32) record->timer < 0) {',
                            '        if ((s32) record->timer < 0) {\n            u32 base = record->base;\n            u32 range = record->range;')
                   .replace('(record->range + 1) + record->base', '(range + 1) + base'))]
        memory, mutation = memory_case(base=0, limit=7), actions(2)
        expected = reference(memory, 0xFFFFFFFF, mutation)
        for name, body in bodies:
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            model = TimerOracle(words, memory, 0xFFFFFFFF, mutation).run()
            self.assertNotEqual((external(model.memory), model.calls, writes(model)), expected[:3])

    def test_production_source_slot_global_and_no_guards(self):
        source = (self.root / 'conker/src/game/generated_FFBA0.c').read_text()
        self.assertIn(screen.RECORD_TYPE.rstrip(), source)
        self.assertEqual(re.search(r'void func_150D26F0\([^;{]+\) \{\n.*?\n\}', source, re.S).group(), screen.DIRECT)
        functions = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        self.assertEqual(functions['func_150D26F0'], self.retail)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse(any(row['function'] == 'func_150D26F0' for row in csv.DictReader(stream)))
        self.assertEqual(self.words[4], 0x3C08800C)
        self.assertEqual(self.words[11], 0x8D08E9E4)


if __name__ == '__main__':
    unittest.main()
