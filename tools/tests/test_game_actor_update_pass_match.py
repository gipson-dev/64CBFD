"""Actor-pass recovery; opaque phase contracts and a real connected dispatcher."""

import csv
import random
import re
import shutil
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_actor_update_pass_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests import test_game_actor_update_dispatch_match as dispatch
from tools.tests import test_game_table_range_loader as table

ENTRY, ACTORS, STRIDE = 0x1502BEE4, 0x800CC2D0, 0x32C
MASK, FIRST, LAST, GATE = 0x800C3E74, 0x800C3E90, 0x800C3E70, 0x800BEAC0
ZERO, UPDATE, POST, FINISH = 0x100226F0, 0x1502BD84, 0x1502F948, 0x15030468
COUNTS = {0x1503F964: 0, ZERO: 2, UPDATE: 2, 0x1502F3C8: 0,
          POST: 1, FINISH: 0, 0x1507C22C: 1, **dispatch.COUNTS}


def memory_case(active=None, links=None, masks=None, gate=0):
    memory = {table.STACK + i: 0xA5 for i in range(-0x400, 0x80)}
    memory.update({ACTORS + i: 0xA5 for i in range(-16, 26 * STRIDE + 16)})
    memory.update({dispatch.FLAGS + i: 0 for i in range(-16, 26 * 16 + 16)})
    for slot in range(26):
        for offset, value, size in ((0, (active or [0] * 26)[slot], 4),
                (0x65, (links or [0] * 26)[slot], 1), (0x274, (masks or [0] * 26)[slot], 1),
                (4, 0, 1), (5, 0, 1), (0xA4, 0, 1), (0x1C9, 0, 1),
                (0xF8, 0, 4), (0x260, 0, 4), (0x1D4, 0xDEADBEEF, 4)):
            dispatch.put(memory, ACTORS + slot * STRIDE + offset, value, size)
    for address, value, size in ((MASK, 0xDEADBEEF, 4), (FIRST, 255, 1),
                                 (LAST, 255, 1), (GATE, gate, 1)):
        dispatch.put(memory, address, value, size)
    return memory


def external_memory(memory):
    return {a: v for a, v in memory.items() if not table.STACK - 0x400 <= a < table.STACK + 0x80}


def external_events(model):
    events = []
    for event in model.events:
        if event[0] == 'CALL':
            if event[1] == ZERO:
                event = ('CALL', ZERO, ('private-depths', event[2][1]))
        elif table.STACK - 0x400 <= event[1] < table.STACK + 0x80:
            continue
        # Repeated nonvolatile field loads can merge without any intervening
        # externally visible event; callback boundaries must remain intact.
        if event[0] == 'R' and events and events[-1] == event:
            continue
        events.append(event)
    return events


class PassOracle(table.RangeOracle):
    def __init__(self, words, memory, phase=0, actions=None, connected=None):
        super().__init__(words, memory, (), phase, connected=connected, entry=ENTRY)
        self.actions = actions or {}

    def record_call(self, target):
        args = self.arguments(COUNTS[target])
        self.calls.append((target, *args))
        self.events.append(('CALL', target, args))

    def hook(self, target):
        if target == ZERO:
            address, length = self.r[4:6]
            assert length == 25
            for i in range(length):
                self.put(address + i, 0, 1)
        slot = (self.r[5] if target == UPDATE else
                (self.r[4] - ACTORS) // STRIDE if target == POST else -1)
        if target == 0x1503A08C:
            self.put(self.r[4] + 0x1D4, 0, 4)
        for address, value, size in self.actions.get((target, slot), ()):
            self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register


class GameActorUpdatePassMatchTests(unittest.TestCase):
    run_host = table.native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(shutil.which(n) is None
                for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-actor-update-pass-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        cls.other_record, cls.other = screen.compile_candidate(cls.root, cls.output, 'baseline', screen.BASELINE)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>176I', rom, 0x59394))
        cls.dispatcher = list(struct.unpack_from('>88I', rom, 0x59234))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = ('typedef unsigned char u8; typedef unsigned int u32; typedef int s32;\n'
                       'void bzero(void *, unsigned int);\n' + screen.DECLARATIONS + r'''
ActorUpdate58F80 D_800CC2D0[26];
u32 D_800C3E74;u8 D_800C3E90,D_800C3E70,D_800BEAC0;
static int logCount,log[64],mutation,error;
void bzero(void *value,unsigned int length) {unsigned int i;u8 *p=value;for(i=0;i<length;i++) p[i]=0;}
s32 func_1503F964(void) {log[logCount++]=100;return -1;}
void func_1502BD84(ActorUpdate58F80 *actor,s32 slot) {
    if(actor!=D_800CC2D0+slot || slot<0 || slot>=25) error=1;
    log[logCount++]=slot;
    actor->work=0;
    if(mutation==1 && slot==0) {D_800CC2D0[1].active=1;D_800CC2D0[1].predecessor=1;}
    if(mutation==2 && slot==0) D_800CC2D0[1].active=0;
    if(mutation==3 && slot==1) {D_800CC2D0[2].active=0;D_800CC2D0[2].predecessor=0;}
}
s32 func_1502F3C8(void) {log[logCount++]=101;if(mutation==4) D_800CC2D0[24].active=1;return -1;}
s32 func_1502F948(ActorUpdate58F80 *actor) {
    int slot=(int)(actor-D_800CC2D0);log[logCount++]=slot+200;
    if(mutation==5 && slot==0) D_800CC2D0[1].active=1;
    return -1;
}
s32 func_15030468(void) {log[logCount++]=102;if(mutation==6) D_800BEAC0=1;if(mutation==7) D_800BEAC0=0;return -1;}
s32 func_1507C22C(s32 mode) {log[logCount++]=103;if(mode) error=2;return -1;}
static void reference(void) {
    int i,j,n=0,depth[25]={0},queue[25],cursor,previous;
    func_1503F964();D_800C3E90=0;D_800C3E74=0;
    for(i=0;i<25;i++) if(D_800CC2D0[i].maskId)
        D_800C3E74 |= 1u << ((D_800CC2D0[i].maskId-1u)&31u);
    for(i=0;i<25;i++) if(D_800CC2D0[i].active) {
        if(!D_800CC2D0[i].predecessor) func_1502BD84(D_800CC2D0+i,i);
        else {
            cursor=i;
            while(D_800CC2D0[cursor].predecessor) {depth[i]=(depth[i]+1)&255;cursor=D_800CC2D0[cursor].predecessor-1;}
            if(depth[i]) {
                j=n;
                while(j>0 && depth[queue[j-1]]>depth[i]) {queue[j]=queue[j-1];j--;}
                queue[j]=i;n++;
            }
        }
    }
    for(i=0;i<n;i++) {previous=queue[i];func_1502BD84(D_800CC2D0+previous,previous);}
    func_1502F3C8();
    for(i=0;i<25;i++) if(D_800CC2D0[i].active) func_1502F948(D_800CC2D0+i);
    func_15030468();if(!D_800BEAC0) func_1507C22C(0);D_800C3E70=0;
}
static void reset(int pattern,int gate) {
    int i,j;u8 *p=(u8 *)D_800CC2D0;
    for(i=0;i<(int)sizeof(D_800CC2D0);i++) p[i]=0xA5;
    for(i=0;i<26;i++) {
        D_800CC2D0[i].active=(pattern&(1<<(i%10)))?-1:0;
        D_800CC2D0[i].predecessor=(u8)(i==0?0:(pattern+i)%(i+1));
        D_800CC2D0[i].maskId=(u8)(pattern*17+i*31);
        D_800CC2D0[i].work=-123;
    }
    if(mutation==1 || mutation==2 || mutation==5) {
        D_800CC2D0[0].active=1;D_800CC2D0[0].predecessor=0;
        D_800CC2D0[1].active=mutation==2;D_800CC2D0[1].predecessor=0;
    }
    if(mutation==3) {
        for(j=0;j<3;j++) {D_800CC2D0[j].active=1;D_800CC2D0[j].predecessor=(u8)j;}
    }
    D_800C3E74=0xDEADBEEF;D_800C3E90=D_800C3E70=255;D_800BEAC0=(u8)gate;
    logCount=error=0;
}
''' + screen.SELECTED + '\n')

    def models(self, memory, phase=0, actions=None, connected=False):
        connection = {0x1502BD84 + i * 4: w for i, w in enumerate(self.dispatcher)} if connected else None
        models = [PassOracle(w, memory, phase, actions, connection).run()
                  for w in (self.retail, self.words, self.other)]
        for model in models[1:]:
            self.assertEqual(external_memory(model.memory), external_memory(models[0].memory))
            self.assertEqual(external_events(model), external_events(models[0]))
        return models[0]

    def test_compiler_boundary_and_no_broad_normalization(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']),
                         (174, 0x88, 115))
        self.assertEqual(self.record['diagnostics'], '')
        source = (self.root / 'conker/src/game/generated_58F80.c').read_text()
        body = re.search(r'void func_1502BEE4\(void\) \{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body, screen.production_body())
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502BEE4'], ENTRY)
        self.assertEqual(functions['func_1502BEE4'], self.words)
        self.assertEqual(functions['func_1502BD84'], self.dispatcher)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            self.assertFalse(any(r['function'] == 'func_1502BEE4' for r in csv.DictReader(file)))

    def test_mask_all_byte_values_and_reserved_slot_exclusion(self):
        coverage = set()
        for value in range(256):
            masks = [value] * 25 + [255]
            model = self.models(memory_case(masks=masks), phase=(value & 1) * 8)
            expected = (1 << ((value - 1) & 31)) if value else 0
            self.assertEqual(model.get(MASK, 4), expected)
            self.assertFalse(any(a >= ACTORS + 25 * STRIDE and a < ACTORS + 26 * STRIDE for a, _, _ in model.reads))
            coverage.update(model.visits)
        self.assertIn(ENTRY, coverage)

    def test_random_acyclic_depths_stable_order_and_real_dispatcher(self):
        rng = random.Random(0x1502BEE4)
        coverage, count = set(), 0
        for case in range(256):
            permutation = list(range(26))
            rng.shuffle(permutation)
            links = [0] * 26
            for index, slot in enumerate(permutation):
                links[slot] = permutation[rng.randrange(index)] + 1 if index and rng.randrange(3) else 0
            active = [rng.choice((0, 1, -1)) for _ in range(26)]
            masks = [rng.randrange(256) for _ in range(26)]
            for connected in (False, True):
                model = self.models(memory_case(active, links, masks, case & 1), (case & 1) * 8, connected=connected)
                immediate, queue = [], []
                for slot in range(25):
                    if active[slot]:
                        if not links[slot]:
                            immediate.append(slot)
                        else:
                            depth, cursor = 0, slot
                            while links[cursor]:
                                depth += 1
                                cursor = links[cursor] - 1
                            queue.append((depth, slot))
                actual = [call[2] for call in model.calls if call[0] == UPDATE]
                self.assertEqual(actual, immediate + [slot for _, slot in sorted(queue)])
                self.assertEqual([call[1] for call in model.calls if call[0] == POST],
                                 [ACTORS + slot * STRIDE for slot in range(25) if active[slot]])
                coverage.update(model.visits)
                count += 1
        self.assertEqual(count, 512)
        self.assertEqual(set(range(ENTRY, ENTRY + 704, 4)) - coverage, set())

    def test_reserved_root_maximum_depth_and_inactive_predecessors(self):
        links = [i + 2 for i in range(25)] + [0]
        active = [1] * 25 + [0]
        model = self.models(memory_case(active, links), connected=True)
        self.assertEqual([c[2] for c in model.calls if c[0] == UPDATE], list(reversed(range(25))))
        self.assertIn((ACTORS + 25 * STRIDE + 0x65, 1, 0), model.reads)

    def test_live_callbacks_and_captured_queue_have_distinct_boundaries(self):
        active, links = [0] * 26, [0] * 26
        active[0] = 1
        actions = {(UPDATE, 0): ((ACTORS + STRIDE, 1, 4), (ACTORS + STRIDE + 0x65, 1, 1)),
                   (0x1502F3C8, -1): ((ACTORS + 24 * STRIDE, 1, 4),),
                   (POST, 0): ((ACTORS + STRIDE, 0, 4),),
                   (FINISH, -1): ((GATE, 1, 1),)}
        model = self.models(memory_case(active, links), actions=actions)
        self.assertEqual([c[2] for c in model.calls if c[0] == UPDATE], [0, 1])
        self.assertEqual([c[1] for c in model.calls if c[0] == POST], [ACTORS, ACTORS + 24 * STRIDE])
        self.assertNotIn((0x1507C22C, 0), model.calls)
        active[:3], links[:3] = [1, 1, 1], [0, 1, 2]
        actions = {(UPDATE, 1): ((ACTORS + 2 * STRIDE, 0, 4), (ACTORS + 2 * STRIDE + 0x65, 0, 1)),
                   (FINISH, -1): ((GATE, 0, 1),)}
        model = self.models(memory_case(active, links, gate=1), actions=actions)
        self.assertEqual([c[2] for c in model.calls if c[0] == UPDATE], [0, 1, 2])
        self.assertIn((0x1507C22C, 0), model.calls)

    def test_shift_and_activity_recheck_negative_controls(self):
        wrong_body = screen.SELECTED.replace('((actor->maskId + 31) & 31)', '(actor->maskId & 31)')
        _, wrong = screen.compile_candidate(self.root, self.output, 'wrong-mask', wrong_body)
        memory = memory_case(masks=[1] * 26)
        self.assertNotEqual(external_memory(PassOracle(self.retail, memory).run().memory),
                            external_memory(PassOracle(wrong, memory).run().memory))
        wrong_body = screen.SELECTED.replace(
            '            func_1502BD84(D_800CC2D0 + ordered[slot], ordered[slot]);',
            '            if (D_800CC2D0[ordered[slot]].active)\n'
            '                func_1502BD84(D_800CC2D0 + ordered[slot], ordered[slot]);')
        self.assertNotEqual(wrong_body, screen.SELECTED)
        _, wrong = screen.compile_candidate(self.root, self.output, 'wrong-recheck', wrong_body)
        memory = memory_case([1, 1, 1] + [0] * 23, [0, 1, 2] + [0] * 23)
        actions = {(UPDATE, 1): ((ACTORS + 2 * STRIDE, 0, 4),)}
        correct = PassOracle(self.retail, memory, actions=actions).run()
        altered = PassOracle(wrong, memory, actions=actions).run()
        self.assertNotEqual(correct.calls, altered.calls)

    def test_cycle_prefix_remains_unsanitized_not_a_completion_claim(self):
        memory = memory_case([1] + [0] * 25, [1] + [0] * 25)
        for words in (self.retail, self.words):
            model = PassOracle(words, memory)
            with self.assertRaisesRegex(AssertionError, 'instruction budget exhausted'):
                model.run()
            self.assertEqual([c[0] for c in model.calls], [0x1503F964, ZERO])
            values = [value for address, size, value in model.stores
                      if table.STACK - 0x88 <= address < table.STACK and size == 1]
            self.assertIn(255, values)
            self.assertTrue(any(a == 255 and b == 0 for a, b in zip(values, values[1:])))

    def test_post_checkpoint_local_storage_controls(self):
        forms = screen.followup_candidates()
        self.assertEqual(len(forms), 8)
        connection = {0x1502BD84 + i * 4: w for i, w in enumerate(self.dispatcher)}
        cases = [
            (memory_case([1] * 25 + [0], list(range(2, 27)) + [0]), None, connection),
            (memory_case([1, 1, 1] + [0] * 23, [0, 1, 2] + [0] * 23,
                         list(range(232, 258))), None, connection),
            (memory_case([1, 1, 1] + [0] * 23, [0, 1, 2] + [0] * 23),
             {(UPDATE, 1): ((ACTORS + 2 * STRIDE, 0, 4),)}, None),
            (memory_case([1] + [0] * 25),
             {(UPDATE, 0): ((ACTORS + STRIDE, 1, 4), (ACTORS + STRIDE + 0x65, 1, 1))}, None)]
        count = 0
        for name, body in forms:
            record, words = screen.compile_candidate(self.root, self.output, name, body)
            expected = (174, 0x88, 115) if name.startswith('register-') else (172, 0x80, 175)
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')
            for memory, actions, connected in cases:
                for phase in (0, 8):
                    original = PassOracle(self.retail, memory, phase, actions, connected).run()
                    model = PassOracle(words, memory, phase, actions, connected).run()
                    self.assertEqual(external_memory(model.memory), external_memory(original.memory))
                    self.assertEqual(external_events(model), external_events(original))
                    count += 1
        self.assertEqual(count, 64)

    def test_native_independent_stable_sort_reference_and_mutations(self):
        self.run_host(r'''
static ActorUpdate58F80 expected[26];static int savedLog[64];
int pattern,gate,i,n,cases=0;u32 mask;u8 finalGate;
if(sizeof(ActorUpdate58F80)!=0x32C || __builtin_offsetof(ActorUpdate58F80,predecessor)!=0x65
   || __builtin_offsetof(ActorUpdate58F80,maskId)!=0x274) return 1;
for(mutation=0;mutation<8;mutation++) for(pattern=0;pattern<1024;pattern++) for(gate=0;gate<2;gate++) {
    reset(pattern,gate);reference();n=logCount;mask=D_800C3E74;finalGate=D_800BEAC0;
    for(i=0;i<n;i++) savedLog[i]=log[i];
    for(i=0;i<26;i++) expected[i]=D_800CC2D0[i];
    reset(pattern,gate);func_1502BEE4();
    if(error || n!=logCount || mask!=D_800C3E74 || finalGate!=D_800BEAC0 || D_800C3E70 || D_800C3E90) return 2;
    for(i=0;i<n;i++) if(savedLog[i]!=log[i]) return 3;
    for(i=0;i<(int)sizeof(expected);i++) if(((u8 *)expected)[i]!=((u8 *)D_800CC2D0)[i]) return 4;
    cases++;
}
if(cases!=16384) return 5;
''')


if __name__ == '__main__':
    unittest.main()
