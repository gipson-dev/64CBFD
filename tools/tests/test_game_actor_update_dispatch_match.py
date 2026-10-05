"""Direct dispatcher match; ABI-aware opaque callbacks, not gameplay acceptance."""

import csv
import hashlib
import itertools
import re
import shutil
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_actor_update_dispatch_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests import test_game_table_range_loader as table


ENTRY, ACTOR, FLAGS = 0x1502BD84, 0x100000, 0x800C666F
COUNTS = {0x1502DF38: 2, 0x1502C608: 1, 0x1502FBE8: 1, 0x1502E4C4: 1,
          0x1503A08C: 1, 0x150345E4: 1, 0x1503A830: 1, 0x1503DF48: 1,
          0x1502EEF4: 1, 0x1502F264: 1, 0x1502EAFC: 1, 0x150A4B04: 1, 0x1517AD00: 3}


def put(memory, address, value, size=4):
    memory.update({address + i: byte for i, byte in enumerate((value & ((1 << (size * 8)) - 1)).to_bytes(size, 'big'))})


def memory_case(state=0, identity=0, active=1, prepare=0, flags=0, optional=0, metadata=0, signal=0, slot=0):
    memory = {table.STACK + i: 0xA5 for i in range(-0x100, 0x80)}
    memory.update({ACTOR + i: 0xA5 for i in range(-16, 0x32C + 16)})
    memory.update({FLAGS + i: 0xA5 for i in range(-32, 26 * 16 + 16)})
    for offset, value, size in ((0, active, 4), (4, identity, 1), (5, state, 1), (0xA4, signal, 1),
            (0xF8, flags, 4), (0x134, 254, 1), (0x135, 255, 1), (0x1C9, prepare, 1),
            (0x1D4, 0xDEADBEEF, 4), (0x1FC, 0xA5, 1), (0x260, optional, 4)):
        put(memory, ACTOR + offset, value, size)
    put(memory, FLAGS + slot * 16, metadata, 1)
    return memory


class DispatchOracle(table.RangeOracle):
    def __init__(self, words, memory, slot=0, phase=0, work=0, actions=None):
        super().__init__(words, memory, (ACTOR, slot), phase, entry=ENTRY)
        self.work, self.actions = work, actions or {}

    def record_call(self, target):
        args = self.arguments(COUNTS[target])
        self.calls.append((target, *args))
        self.events.append(('CALL', target, args))

    def hook(self, target):
        if target == 0x1503A08C:
            self.put(ACTOR + 0x1D4, self.work, 4)
        for offset, value, size in self.actions.get(target, ()):
            self.put(ACTOR + offset, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register


class SlotPrefixBoundary(Exception):
    """Stop after the actual callee computes its actor pointer, before its loop."""


class SlotPrefixOracle(DispatchOracle):
    def hook(self, target):
        if target == 0x1502EEF4:
            for word in self.prefix:
                self.execute(word)
            raise SlotPrefixBoundary()
        super().hook(target)


class GameActorUpdateDispatchMatchTests(unittest.TestCase):
    run_host = table.native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(shutil.which(n) is None
                for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-actor-update-dispatch-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'baseline', screen.BASELINE)
        cls.shifted_record, cls.shifted = screen.compile_candidate(cls.root, cls.output, 'shifted', dict(screen.candidates())['shifted-flag'])
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>88I', rom, 0x59234))
        cls.slot_prefix = list(struct.unpack_from('>21I', rom, 0x5C3A4))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = ('typedef unsigned char u8; typedef unsigned int u32; typedef int s32;\n' + screen.DECLARATIONS + r'''
static ActorUpdate58F80 actor;u8 D_800C666F[26*16];
static s32 slot,workValue;static int actual[32],expected[32],count,wanted,error,mutation;
static void reset(int state,int id,int active,int prepare,int flag,int optional,int metadata,int signal) {
    int i;u8 *p=(u8 *)&actor;
    for(i=0;i<(int)sizeof(actor);i++) p[i]=0xA5;
    actor.state=(u8)state;actor.id=(u8)id;actor.active=active;actor.prepare=(u8)prepare;
    actor.flags=flag?0x4000:0;actor.optional=(u32)optional;actor.signal=(u8)signal;
    actor.eventA=254;actor.eventB=255;actor.work=-123;actor.status=0xA5;
    for(i=0;i<26*16;i++) D_800C666F[i]=0xA5;
    D_800C666F[slot*16]=(u8)metadata;count=wanted=error=mutation=0;
}
static void record(int target) {if(count>=32) error=1;else actual[count++]=target;}
static void checkSlot(s32 value) {if(value!=slot) error=2;}
static void checkActor(ActorUpdate58F80 *value) {if(value!=&actor) error=3;}
s32 func_1502DF38(s32 value,s32 mode) {checkSlot(value);record(1);if(mode!=(actor.state==5?1:0) || actor.work) error=4;return -123;}
s32 func_1502C608(s32 value) {checkSlot(value);record(2);if(actor.work) error=5;return -123;}
s32 func_1502FBE8(ActorUpdate58F80 *value) {checkActor(value);record(3);if(actor.work) error=6;return -123;}
s32 func_1502E4C4(s32 value) {checkSlot(value);record(4);return -123;}
s32 func_1503A08C(ActorUpdate58F80 *value) {checkActor(value);record(5);actor.work=workValue;return -123;}
s32 func_150345E4(s32 value) {checkSlot(value);record(6);return -123;}
s32 func_1503A830(ActorUpdate58F80 *value) {checkActor(value);record(7);return -123;}
s32 func_1503DF48(s32 value) {checkSlot(value);record(8);if(mutation==1) actor.active=0;return -123;}
s32 func_1502EEF4(s32 value) {checkSlot(value);record(9);return -123;}
s32 func_1502F264(s32 value) {checkSlot(value);record(10);if(mutation==2) {actor.active=0;actor.signal=1;}return -123;}
s32 func_1502EAFC(ActorUpdate58F80 *value) {checkActor(value);record(11);if(mutation==2) actor.flags=0x4000;return -123;}
s32 func_150A4B04(ActorUpdate58F80 *value) {checkActor(value);record(12);if(mutation==2) {actor.optional=1;actor.eventA=17;actor.eventB=93;}return -123;}
s32 func_1517AD00(s32 first,s32 second,s32 value) {
    checkSlot(value);record(13);if(first!=(mutation==2?17:254) || second!=(mutation==2?93:255)) error=7;return -123;
}
static void expect(int value) {expected[wanted++]=value;}
static int compare(void) {int i;if(error || count!=wanted) return 1;for(i=0;i<count;i++) if(actual[i]!=expected[i]) return 2;return 0;}
''' + screen.BASELINE + '\n')

    def models(self, memory, **case):
        models = [DispatchOracle(words, memory, **case).run() for words in (self.retail, self.words, self.shifted)]
        for model in models[1:]:
            self.assertEqual(model.memory, models[0].memory)
            self.assertEqual(model.calls, models[0].calls)
            self.assertEqual(model.stores, models[0].stores)
            # Stack reload scheduling differs; external reads/writes/calls must not.
            for field in ('events', 'reads'):
                def external(events):
                    return [e for e in events if e[0] == 'CALL' or not table.STACK - 0x100 <= e[1 if field == 'events' else 0] < table.STACK + 0x80]
                self.assertEqual(external(getattr(model, field)), external(getattr(models[0], field)))
        return models[0]

    def test_direct_frame_slot_production_identity_and_no_guards(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (88, 0x20, 0))
        self.assertEqual(self.words, self.retail)
        self.assertEqual((self.shifted_record['body_words'], self.shifted_record['frame'], self.shifted_record['real_differences']), (89, 0x20, 23))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.shifted_record['diagnostics'], '')
        self.assertEqual(len(screen.candidates()), 26)
        source = (self.root / 'conker/src/game/generated_58F80.c').read_text()
        body = re.search(r'void func_1502BD84\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body, screen.BASELINE)
        self.assertIn(screen.DECLARATIONS.strip(), source)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502BD84'], ENTRY)
        self.assertEqual(functions['func_1502BD84'], self.retail)
        self.assertEqual(hashlib.sha256(struct.pack('>88I', *self.words)).hexdigest(),
                         '0ce9ed73235a6dfd192422f224efe6d78bcb0b07a8cd2eb9bccb942370a9d9b6')
        caller = functions['func_1502BEE4']
        self.assertEqual(len(caller), 176)
        from tools.experiments import game_actor_update_pass_candidates as caller_screen
        _, recovered_caller = caller_screen.compile_candidate(self.root, self.output, 'recovered-caller', caller_screen.SELECTED)
        self.assertEqual(caller, recovered_caller)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            self.assertFalse(any(r['function'] == 'func_1502BD84' for r in csv.DictReader(file)))

    def test_omitted_slot_negative_control_is_not_an_equivalent_recovery(self):
        record, wrong = screen.compile_candidate(self.root, self.output, 'missing-slot', dict(screen.candidates())['wrong-omitted-slot-negative-control'])
        self.assertEqual((record['body_words'], record['frame'], record['real_differences']), (87, 0x20, 42))
        memory = memory_case(metadata=1, active=1)
        original = DispatchOracle(self.retail, memory).run()
        altered = DispatchOracle(wrong, memory).run()
        self.assertNotEqual(original.calls, altered.calls)
        self.assertIn((0x1502EEF4, 0), original.calls)
        self.assertIn((0x1502EEF4, 0xA5000004), altered.calls)

    def test_actual_slot_callee_prefix_consumes_and_indexes_the_argument(self):
        self.assertEqual(self.slot_prefix[2], 0x00809025)
        self.assertEqual(self.slot_prefix[-1], 0x01CF8021)
        count = 0
        for slot, phase, metadata, work in itertools.product((-1, 0, 1, 24), (0, 8), (0, 1), (0, 1, -1)):
            memory = memory_case(metadata=metadata, active=1, slot=slot)
            models = []
            for words in (self.retail, self.words):
                model = SlotPrefixOracle(words, memory, slot, phase, work)
                model.prefix = self.slot_prefix
                with self.assertRaises(SlotPrefixBoundary):
                    model.run()
                self.assertEqual(model.r[18], slot & 0xFFFFFFFF)
                self.assertEqual(model.r[16], (0x800CC2D0 + slot * 0x32C) & 0xFFFFFFFF)
                self.assertEqual(model.r[29], table.STACK + phase - 0x50)
                models.append(model)
            for field in ('memory', 'calls', 'events', 'reads', 'stores'):
                self.assertEqual(getattr(models[0], field), getattr(models[1], field))
            count += 1
        self.assertEqual(count, 48)

    def test_target_gate_work_and_optional_matrix(self):
        count, coverage = 0, set()
        for state, identity, prepare, active, flag, optional, metadata, work, signal in itertools.product(
                (0, 1, 2, 3, 4, 5, 6, 7, 255), (0, 255), (0, 1), (0, 1, -1), (0, 1), (0, 1), (0, 1), (0, 1, -1), (0, 1)):
            memory = memory_case(state, identity, active, prepare, flag * 0x4000, optional, metadata, signal=signal)
            model = self.models(memory, work=work)
            expected = []
            if state == 5:
                expected = [(0x1502DF38, 0, 1)]
            elif identity != 255 and state != 3:
                if state == 2:
                    expected = [(0x1502C608, 0)]
                else:
                    if prepare:
                        expected.append((0x1502FBE8, ACTOR))
                    expected += [(0x1502E4C4, 0), (0x1502DF38, 0, 0), (0x1503A08C, ACTOR)]
                    if work:
                        expected += [(0x150345E4, 0), (0x1503A830, ACTOR)]
                    if metadata:
                        expected.append((0x1503DF48, 0))
                    if active:
                        expected += [(0x1502EEF4, 0), (0x1502F264, 0)]
                        if signal:
                            expected.append((0x1502EAFC, ACTOR))
                        if flag:
                            expected.append((0x150A4B04, ACTOR))
                        if optional:
                            expected.append((0x1517AD00, 254, 255, 0))
            self.assertEqual(model.calls, expected)
            self.assertEqual(model.stores[3], (ACTOR + 0x1D4, 4, 0))
            coverage.update(model.visits)
            count += 1
        self.assertEqual(count, 5184)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 88 * 4, 4)) - {0x1502BDEC})

    def test_target_live_mutations_and_no_repeated_early_gates(self):
        memory = memory_case(prepare=1, active=1, metadata=1)
        actions = {0x1502FBE8: ((4, 255, 1), (5, 3, 1)),
                   0x150345E4: ((0x1D4, 0, 4),), 0x1503DF48: ((0, 0, 4),)}
        model = self.models(memory, work=1, actions=actions)
        self.assertEqual([c[0] for c in model.calls], [0x1502FBE8, 0x1502E4C4, 0x1502DF38, 0x1503A08C,
                                                        0x150345E4, 0x1503A830, 0x1503DF48])
        memory = memory_case(active=-1, signal=0)
        actions = {0x1502F264: ((0, 0, 4), (0xA4, 1, 1)),
                   0x1502EAFC: ((0xF8, 0x4000, 4),),
                   0x150A4B04: ((0x260, 1, 4), (0x134, 17, 1), (0x135, 93, 1))}
        model = self.models(memory, actions=actions)
        self.assertEqual([c[0] for c in model.calls], [0x1502E4C4, 0x1502DF38, 0x1503A08C,
                            0x1502EEF4, 0x1502F264, 0x1502EAFC, 0x150A4B04, 0x1517AD00])
        self.assertEqual(model.calls[-1], (0x1517AD00, 17, 93, 0))

    def test_target_slot_home_phases_and_signed_indices(self):
        for slot, phase in itertools.product((-1, 0, 1, 24), (0, 8)):
            model = self.models(memory_case(metadata=1, optional=1, slot=slot), slot=slot, phase=phase)
            self.assertEqual(model.calls[-1], (0x1517AD00, 254, 255, slot & 0xFFFFFFFF))
            self.assertIn((FLAGS + slot * 16, 1, 1), model.reads)
            self.assertEqual(model.memory[ACTOR + 0x1FC], 2)

    def test_semantically_wrong_work_comparison_has_a_counterexample(self):
        _, wrong = screen.compile_candidate(self.root, self.output, 'wrong-work', dict(screen.candidates())['wrong-work-one-negative-control'])
        memory = memory_case(active=0)
        correct = DispatchOracle(self.retail, memory, work=-1).run()
        altered = DispatchOracle(wrong, memory, work=-1).run()
        self.assertNotEqual(correct.calls, altered.calls)
        self.assertNotEqual(correct.memory[ACTOR + 0x1FC], altered.memory[ACTOR + 0x1FC])

    def test_native_all_state_bytes_and_callback_order(self):
        self.run_host(r'''
int st,id,prep,active,flag,opt,meta,w,i,cases=0,regular;static s32 workValues[]={0,1,-1};
if(sizeof(ActorUpdate58F80)!=0x32C || __builtin_offsetof(ActorUpdate58F80,work)!=0x1D4
   || __builtin_offsetof(ActorUpdate58F80,optional)!=0x260) return 1;
slot=24;
for(st=0;st<256;st++) for(id=0;id<2;id++) for(prep=0;prep<2;prep++) for(active=0;active<2;active++)
for(flag=0;flag<2;flag++) for(opt=0;opt<2;opt++) for(meta=0;meta<2;meta++) for(w=0;w<3;w++) {
    reset(st,id?255:0,active?-1:0,prep,flag,opt,meta,1);workValue=workValues[w];regular=0;
    if(st==5) expect(1);
    else if(!id && st!=3) {
        if(st==2) expect(2);
        else {
            regular=1;if(prep) expect(3);expect(4);expect(1);expect(5);
            if(workValue) {expect(6);expect(7);}if(meta) expect(8);
            if(active) {expect(9);expect(10);expect(11);if(flag) expect(12);if(opt) expect(13);}
        }
    }
    func_1502BD84(&actor,slot);
    if(compare() || actor.work!=(regular?workValue:0) || actor.status!=(regular && !workValue?2:0xA5)) return 2;
    for(i=0;i<26*16;i++) if(D_800C666F[i]!=(i==slot*16?meta:0xA5)) return 3;
    cases++;
}
if(cases!=49152) return 4;
''')

    def test_native_mutations_keep_later_reads_live(self):
        self.run_host(r'''
slot=1;reset(0,0,1,0,0,0,1,0);workValue=1;mutation=1;
expect(4);expect(1);expect(5);expect(6);expect(7);expect(8);
func_1502BD84(&actor,slot);if(compare() || actor.active || actor.status!=0xA5) return 1;
reset(0,0,1,0,0,0,0,0);workValue=0;mutation=2;
expect(4);expect(1);expect(5);expect(9);expect(10);expect(11);expect(12);expect(13);
func_1502BD84(&actor,slot);if(compare() || actor.active || actor.status!=2) return 2;
''')


if __name__ == '__main__':
    unittest.main()
