"""Direct actor copy match, live allocator mutations and bounded SDK connections."""

import csv
import itertools
import re
import shutil
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_actor_buffer_copy_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests import test_game_actor_update_pass_match as actor_pass
from tools.tests import test_game_table_range_loader as table

ENTRY, ALLOCATE, CORE, COPY = 0x1502F948, 0x10003C40, 0x10003C6C, 0x10023A10
ACTOR, SIZES, ARENA = actor_pass.ACTORS, 0x800C4ED0, 0x20000


def put(memory, address, value, size=4):
    actor_pass.dispatch.put(memory, address, value, size)


def memory_case(flags=0x4000, state=1, source=ARENA + 32, buffer=0, identity=7, units=2):
    memory = {table.STACK + i: 0xA5 for i in range(-0x400, 0x80)}
    memory.update({ACTOR + i: 0xA5 for i in range(-16, 0x32C + 16)})
    memory.update({SIZES + i: 0 for i in range(512)})
    memory.update({ARENA + i: (i * 137 + 19) & 255 for i in range(-16, 2048)})
    for offset, value, size in ((4, identity, 1), (0xF8, flags, 4),
            (0x264, state, 4), (0x1D4, source, 4), (0x1D8, buffer, 4)):
        put(memory, ACTOR + offset, value, size)
    put(memory, SIZES + identity * 2, units, 2)
    return memory


class CopyOracle(table.RangeOracle):
    def __init__(self, words, memory, phase=0, result=ARENA + 1024, actions=(), connected=None):
        super().__init__(words, memory, (ACTOR,), phase, connected=connected, entry=ENTRY)
        self.result, self.actions = result, actions

    def execute(self, word):
        op, rs, rt, rd = word >> 26, word >> 21 & 31, word >> 16 & 31, word >> 11 & 31
        if op == 32:
            immediate = word & 65535
            address = (self.r[rs] + (immediate if immediate < 32768 else immediate - 65536)) & 0xFFFFFFFF
            value = self.get(address, 1)
            self.r[rt] = (value if value < 128 else value - 256) & 0xFFFFFFFF
        elif op == 0 and word & 63 == 32:
            signed = lambda v: v if v < 0x80000000 else v - 0x100000000
            value = signed(self.r[rs]) + signed(self.r[rt])
            assert -0x80000000 <= value < 0x80000000, 'SDK ADD overflow outside qualified domain'
            self.r[rd] = value & 0xFFFFFFFF
        else:
            super().execute(word)
        self.r[0] = 0

    def record_call(self, target):
        count = {ALLOCATE: 4, CORE: 5, COPY: 3}[target]
        args = self.arguments(count)
        self.calls.append((target, *args))
        self.events.append(('CALL', target, args))

    def hook(self, target):
        if target in (ALLOCATE, CORE):
            for address, value, size in self.actions:
                self.put(address, value, size)
        else:
            assert target == COPY
            source, destination, length = self.arguments(3)
            assert length <= 256
            snapshot = [self.get(source + i, 1) for i in range(length)]
            for i, value in enumerate(snapshot):
                self.put(destination + i, value, 1)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        if target in (ALLOCATE, CORE):
            self.r[2] = self.result


class GameActorBufferCopyMatchTests(unittest.TestCase):
    run_host = table.native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').exists() or any(shutil.which(n) is None
                for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-actor-buffer-copy-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        forms = dict(screen.candidates())
        cls.control_record, cls.control = screen.compile_candidate(cls.root, cls.output, 'byte-id', forms['byte-id'])
        cls.negative = {name: screen.compile_candidate(cls.root, cls.output, name, body)[1]
                        for name, body in forms.items() if 'negative-control' in name}
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>45I', rom, 0x5CDF8))
        cls.production = load_elf_functions(str(cls.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        cls.wrapper, cls.sdk = cls.production['allocate_memory'], cls.production['bcopy']
        cls.connected = {ALLOCATE + i * 4: word for i, word in enumerate(cls.wrapper)}
        cls.connected.update({COPY + i * 4: word for i, word in enumerate(cls.sdk)})
        cls.coverage, cls.sdk_coverage, cls.cases = set(), set(), 0
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = ('''typedef unsigned char u8;typedef unsigned short u16;
typedef unsigned int u32;typedef int s32;
#define NULL ((void *)0)
void bcopy(const void *,void *,int);
''' + screen.DECLARATIONS + r'''
u16 D_800C4ED0[256];
static ActorCopy58F80 actor;
static u8 arena[2048];
static u32 log[2][5];
static int count,mode,error,recordOnly;
static void *result;
s32 allocate_memory(s32 size,s32 a,s32 b,s32 c) {
    if(count>=2) {error=1;return 0;}
    log[count][0]=1;log[count][1]=(u32)size;log[count][2]=(u32)a;
    log[count][3]=(u32)b;log[count++][4]=(u32)c;
    if(mode&1) actor.id^=255;
    if(mode&2) D_800C4ED0[actor.id^((mode&1)?255:0)]=3;
    if(mode&4) actor.source=arena+512;
    if(mode&8) actor.buffer=arena+768;
    if(mode&16) {actor.flags=0;actor.copyState=0;}
    return (s32)result;
}
void bcopy(const void *s,void *d,int length) {
    int i;u8 bytes[256];
    if(count>=2) {error=2;return;}
    log[count][0]=2;log[count][1]=(u32)s;log[count][2]=(u32)d;
    log[count++][3]=(u32)length;
    if(recordOnly) return;
    if(length<0 || length>256) {error=3;return;}
    for(i=0;i<length;i++) bytes[i]=((const u8 *)s)[i];
    for(i=0;i<length;i++) ((u8 *)d)[i]=bytes[i];
}
static void reset(int id,int units,int existing,int mutation,int fail) {
    int i;u8 *p=(u8 *)&actor;
    for(i=0;i<(int)sizeof(actor);i++) p[i]=0xA5;
    for(i=0;i<2048;i++) arena[i]=(u8)(i*137+19);
    for(i=0;i<256;i++) D_800C4ED0[i]=0;
    for(i=0;i<10;i++) ((u32 *)log)[i]=0;
    actor.id=(u8)id;actor.flags=0x4000;actor.copyState=1;
    actor.source=arena+32;actor.buffer=existing?arena+1024:NULL;
    D_800C4ED0[id]=(u16)units;mode=mutation;result=fail?NULL:arena+1024;
    count=error=recordOnly=0;
}
static void reference(void) {
    int savedId;
    if(!(actor.flags&0x4000)) return;
    if(!actor.copyState) return;
    if(!actor.source) return;
    savedId=actor.id;
    if(!actor.buffer) {
        void *allocated=(void *)allocate_memory((s32)D_800C4ED0[savedId]*64,1,1,2);
        actor.buffer=allocated;
        if(!allocated) return;
    }
    bcopy(actor.source,actor.buffer,(int)D_800C4ED0[savedId]*64);
}
''' + screen.SELECTED + '\n')

    def models(self, memory, phase=0, result=ARENA + 1024, actions=(), connected=None):
        models = [CopyOracle(words, memory, phase, result, actions, connected).run()
                  for words in (self.retail, self.words, self.control)]
        for model in models[1:]:
            self.assertEqual(actor_pass.external_memory(model.memory), actor_pass.external_memory(models[0].memory))
            self.assertEqual(actor_pass.external_events(model), actor_pass.external_events(models[0]))
        type(self).cases += 1
        type(self).coverage.update(models[0].visits)
        type(self).sdk_coverage.update(a for a in models[0].visits if COPY <= a < COPY + len(self.sdk) * 4)
        return models[0]

    def test_direct_compiler_match_and_production_identity(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (45, 0x28, 0))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.production['func_1502F948'], self.retail)
        self.assertEqual(self.control_record['real_differences'], 2)
        source = (self.root / 'conker/src/game/generated_58F80.c').read_text()
        self.assertEqual(re.search(r'void func_1502F948\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(), screen.SELECTED)
        layout = re.search(r'typedef struct ActorCopy58F80 \{.*?\} ActorCopy58F80;', source, re.S).group()
        self.assertIn(layout, screen.DECLARATIONS)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse(any(row['function'] == 'func_1502F948' for row in csv.DictReader(stream)))

    def test_gates_all_identity_bytes_and_unsigned_size_argument(self):
        for identity, flags, state, source, existing, phase in itertools.product(
                range(256), (0, 0x4000, 0xFFFFFFFF), (0, 0x80000000),
                (0, ARENA + 32), (0, ARENA + 1024), (0, 8)):
            model = self.models(memory_case(flags, state, source, existing, identity, 0), phase)
            enabled = bool(flags & 0x4000 and state and source)
            self.assertEqual(len(model.calls), (1 if existing else 2) if enabled else 0)
            if enabled:
                self.assertEqual(model.calls[-1], (COPY, source, existing or ARENA + 1024, 0))
        for units, phase in itertools.product((0x7FFF, 0x8000, 0xFFFF), (0, 8)):
            model = self.models(memory_case(units=units), phase, result=0)
            self.assertEqual(model.calls, [(ALLOCATE, units << 6, 1, 1, 2)])
            self.assertEqual(model.peek(ACTOR + 0x1D8, 4), 0)

    def test_gate_short_circuit_does_not_read_later_fields(self):
        for flags, state, source, absent in ((0, 1, 1, (0x264, 0x1D4)),
                (0x4000, 0, 1, (0x1D4,)), (0x4000, 1, 0, (4, 0x1D8))):
            memory = memory_case(flags=flags, state=state, source=source)
            for offset in absent:
                for i in range(1 if offset == 4 else 4):
                    del memory[ACTOR + offset + i]
            self.assertFalse(self.models(memory).calls)

    def test_cached_identity_and_fresh_post_allocation_fields(self):
        for identity, mode, failed, phase in itertools.product((0, 1, 127, 128, 255), range(32), (False, True), (0, 8)):
            actions = []
            if mode & 1:
                actions.append((ACTOR + 4, identity ^ 255, 1))
            if mode & 2:
                actions.append((SIZES + identity * 2, 3, 2))
            if mode & 4:
                actions.append((ACTOR + 0x1D4, ARENA + 512, 4))
            if mode & 8:
                actions.append((ACTOR + 0x1D8, ARENA + 768, 4))
            if mode & 16:
                actions += [(ACTOR + 0xF8, 0, 4), (ACTOR + 0x264, 0, 4)]
            model = self.models(memory_case(identity=identity), phase, 0 if failed else ARENA + 1024, actions)
            self.assertEqual(model.calls[0], (ALLOCATE, 128, 1, 1, 2))
            self.assertEqual(model.peek(ACTOR + 0x1D8, 4), 0 if failed else ARENA + 1024)
            self.assertEqual(len(model.calls), 1 if failed else 2)
            if not failed:
                self.assertEqual(model.calls[-1], (COPY, ARENA + (512 if mode & 4 else 32), ARENA + 1024, 192 if mode & 2 else 128))

    def test_actual_allocator_wrapper_and_sdk_overlap_alignment(self):
        self.assertEqual(len(self.wrapper), 11)
        self.assertEqual(len(self.sdk), 196)
        for source_offset, delta, units, phase in itertools.product(range(8), (0, 1, 7, -1, -7, 512), range(5), (0, 8)):
            source = ARENA + 32 + source_offset
            destination = source + delta
            memory = memory_case(source=source, units=units)
            expected = memory.copy()
            snapshot = [memory[source + i] for i in range(units * 64)]
            for i, value in enumerate(snapshot):
                expected[destination + i] = value
            put(expected, ACTOR + 0x1D8, destination)
            model = self.models(memory, phase, destination, connected=self.connected)
            self.assertEqual(actor_pass.external_memory(model.memory), actor_pass.external_memory(expected))
            self.assertEqual(model.calls, [(ALLOCATE, units * 64, 1, 1, 2),
                                          (CORE, units * 64, 1, 1, 0, 2), (COPY, source, destination, units * 64)])

    def test_connected_allocator_mutations_and_failure(self):
        for failed, phase in itertools.product((False, True), (0, 8)):
            actions = ((ACTOR + 4, 9, 1), (SIZES + 14, 3, 2),
                       (ACTOR + 0x1D4, ARENA + 512, 4), (ACTOR + 0x1D8, ARENA + 768, 4))
            model = self.models(memory_case(), phase, 0 if failed else ARENA + 1024, actions, self.connected)
            self.assertEqual(model.calls[:2], [(ALLOCATE, 128, 1, 1, 2), (CORE, 128, 1, 1, 0, 2)])
            self.assertEqual(model.peek(ACTOR + 0x1D8, 4), 0 if failed else ARENA + 1024)
            if not failed:
                self.assertEqual(model.calls[-1], (COPY, ARENA + 512, ARENA + 1024, 192))

    def test_existing_buffer_skips_allocation_and_keeps_copy(self):
        for identity, units, phase in itertools.product((0, 127, 128, 255), range(5), (0, 8)):
            model = self.models(memory_case(buffer=ARENA + 1024, identity=identity, units=units), phase, connected=self.connected)
            self.assertEqual(model.calls, [(COPY, ARENA + 32, ARENA + 1024, units * 64)])

    def test_negative_controls_are_semantically_detected(self):
        cases = (( 'missing-state-negative-control', memory_case(state=0), ()),
                 ('reloaded-id-negative-control', memory_case(), ((ACTOR + 4, 9, 1),)),
                 ('cached-size-negative-control', memory_case(), ((SIZES + 14, 3, 2),)))
        for name, memory, actions in cases:
            actual = CopyOracle(self.retail, memory, actions=actions).run()
            wrong = CopyOracle(self.negative[name], memory, actions=actions).run()
            self.assertNotEqual(actual.calls, wrong.calls, name)

    def test_native_layout_and_unsigned_halfword_abi(self):
        self.run_host(r'''
if(sizeof(actor)!=0x32C || (u8 *)&actor.id-(u8 *)&actor!=4
   || (u8 *)&actor.flags-(u8 *)&actor!=0xF8
   || (u8 *)&actor.source-(u8 *)&actor!=0x1D4
   || (u8 *)&actor.buffer-(u8 *)&actor!=0x1D8
   || (u8 *)&actor.copyState-(u8 *)&actor!=0x264) return 1;
reset(255,65535,0,0,1);recordOnly=1;func_1502F948(&actor);
if(error || count!=1 || log[0][1]!=4194240 || log[0][2]!=1 || log[0][3]!=1 || log[0][4]!=2 || actor.buffer) return 2;
reset(128,32768,1,0,0);recordOnly=1;func_1502F948(&actor);
if(error || count!=1 || log[0][0]!=2 || log[0][3]!=2097152) return 3;
''')

    def test_native_gates_preserve_ineligible_actor_and_storage(self):
        self.run_host(r'''
static u32 flags[]={0,1,0x3FFF,0x4000,0x4001,0x80000000,0xFFFFBFFF,0xFFFFFFFF};
static u8 saved[0x32C];int f,state,source,existing,id,i,enabled;
for(f=0;f<8;f++) for(state=0;state<2;state++) for(source=0;source<2;source++)
for(existing=0;existing<2;existing++) for(id=0;id<256;id++) {
    reset(id,0,existing,0,0);actor.flags=flags[f];actor.copyState=state?0x80000000:0;
    if(!source) actor.source=NULL;
    for(i=0;i<0x32C;i++) saved[i]=((u8 *)&actor)[i];
    enabled=(flags[f]&0x4000) && state && source;
    func_1502F948(&actor);
    if(error || count!=(enabled?(existing?1:2):0)) return 1;
    if(!enabled) for(i=0;i<0x32C;i++) if(saved[i]!=((u8 *)&actor)[i]) return 2;
    for(i=0;i<2048;i++) if(arena[i]!=(u8)(i*137+19)) return 3;
}
''')

    def test_native_independent_reference_whole_record_arena_and_calls(self):
        self.run_host(r'''
static u8 savedActor[0x32C],savedArena[2048];static u16 savedSizes[256];
static u32 savedLog[2][5];int id,units,existing,mutation,fail,i,savedCount;
for(id=0;id<256;id++) for(units=0;units<5;units++) for(existing=0;existing<2;existing++)
for(mutation=0;mutation<32;mutation++) for(fail=0;fail<2;fail++) {
    reset(id,units,existing,mutation,fail);reference();if(error) return 1;
    savedCount=count;
    for(i=0;i<0x32C;i++) savedActor[i]=((u8 *)&actor)[i];
    for(i=0;i<2048;i++) savedArena[i]=arena[i];
    for(i=0;i<256;i++) savedSizes[i]=D_800C4ED0[i];
    for(i=0;i<10;i++) ((u32 *)savedLog)[i]=((u32 *)log)[i];
    reset(id,units,existing,mutation,fail);func_1502F948(&actor);
    if(error || count!=savedCount) return 2;
    for(i=0;i<0x32C;i++) if(savedActor[i]!=((u8 *)&actor)[i]) return 3;
    for(i=0;i<2048;i++) if(savedArena[i]!=arena[i]) return 4;
    for(i=0;i<256;i++) if(savedSizes[i]!=D_800C4ED0[i]) return 5;
    for(i=0;i<10;i++) if(((u32 *)savedLog)[i]!=((u32 *)log)[i]) return 6;
}
''')

    @classmethod
    def tearDownClass(cls):
        print('actor buffer copy:', cls.cases, 'three-way cases;',
              len(cls.coverage & set(range(ENTRY, ENTRY + 180, 4))), '/45 retail words;',
              len(cls.sdk_coverage), '/196 connected SDK words')


if __name__ == '__main__':
    unittest.main()
