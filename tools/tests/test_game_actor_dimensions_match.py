"""Direct actor-dimension query, sequential overlapping stores and finite float work."""

import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_actor_dimensions_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_actor_triangle_transform_match import put
from tools.tests.test_game_indexed_state_save_match import StateSaveOracle, external, events
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

ACTOR, OUTPUT = 0x20000, 0x20400
CASES = ((-32768, 32767, -32768, (1.0, 2.0, 3.0)),
         (32767, -32768, 32767, (-1.0, -2.0, -3.0)),
         (-1, 0, 1, (0.0, -0.0, 0.125)),
         (0, 1, -1, (-0.0, 16777216.0, -0.125)),
         (1, -1, 0, (0.5, -16777216.0, -0.5)),
         (100, -100, 100, (123.25, -321.5, 0.75)))
ALIASES = ((OUTPUT, OUTPUT+32, OUTPUT+36), (OUTPUT, OUTPUT+32, OUTPUT+32),
           (OUTPUT, OUTPUT, OUTPUT+4), (ACTOR+20, OUTPUT+32, OUTPUT+36),
           (OUTPUT, ACTOR+212, OUTPUT+36), (OUTPUT, OUTPUT+32, ACTOR+212),
           (OUTPUT, ACTOR+20, OUTPUT+36), (OUTPUT, OUTPUT+32, ACTOR+24),
           (ACTOR+208, OUTPUT+32, OUTPUT+36), (OUTPUT, OUTPUT, OUTPUT),
           (ACTOR+16, OUTPUT+32, OUTPUT+36), (OUTPUT, ACTOR+4, OUTPUT+36))


def memory_case(identity, case, offsets=(210, 212, 214)):
    memory = {STACK+i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({ACTOR+i: 0xA5 for i in range(0x440)})
    put(memory, ACTOR+4, identity, 1)
    for offset, value in zip(offsets, case[:3]):
        put(memory, ACTOR+offset, value & 65535, 2)
    for offset, value in zip((20, 24, 28), case[3]):
        put(memory, ACTOR+offset, bits(value))
    return memory


def reference(memory, outputs, offsets=(210, 212, 214)):
    memory, trace = dict(memory), []
    position, width, height = outputs
    def read(address, size):
        value = int.from_bytes(bytes(memory[address+i] for i in range(size)), 'big')
        trace.append(('R', address, size, value))
        return value
    def write(address, value):
        put(memory, address, value)
        trace.append(('W', address, 4, value))
    def half(offset):
        value = read(ACTOR+offset, 2)
        return value if value < 32768 else value-65536
    special = read(ACTOR+4, 1) < 187
    if special:
        write(width, bits(float(half(offsets[0]))))
        write(height, bits(float(half(offsets[1]))))
    else:
        write(width, bits(1.0))
        write(height, bits(1.0))
    write(position, read(ACTOR+20, 4))
    if special:
        offset = half(offsets[2])
        write(position+4, bits(floating(read(ACTOR+24, 4)) + float(offset)))
    else:
        write(position+4, read(ACTOR+24, 4))
    write(position+8, read(ACTOR+28, 4))
    return external(memory), trace


class DimensionOracle(StateSaveOracle):
    def __init__(self, words, memory, outputs, phase=0, entry=screen.ENTRY):
        super().__init__(words, memory, phase=phase)
        self.code = {entry+i*4: word for i, word in enumerate(words)}
        self.entry = entry
        self.r[4:8] = (ACTOR, *outputs)

    def record_call(self, target):
        raise AssertionError('dimension query unexpectedly calls a helper')


class GameActorDimensionsMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-actor-dimensions-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.retail = list(struct.unpack_from('>41I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        header = (cls.root / 'conker/include/structs.h').read_text()
        actor_prefix = re.search(r'struct struct127 \{.*?(?=    f32 unkDC;)', header, re.S).group() + '};'
        point = re.search(r'typedef struct \{[^{}]*\} struct17;', header).group()
        cls.fixture = ('typedef unsigned char u8;typedef signed char s8;typedef short s16;'
                       'typedef unsigned short u16;typedef int s32;typedef unsigned int u32;typedef float f32;\n'
                       + actor_prefix + '\ntypedef struct struct127 struct127;\n' + point + '\n'
                       + screen.SELECTED + r'''
static union {u32 aligned[272];u8 bytes[1088];} actual,expected;
static u32 word(f32 f) {union {u32 u;f32 f;} v;v.f=f;return v.u;}
static void store(u8 *p,int offset,u32 value) {*(u32 *)(p+offset)=value;}
static u32 load(u8 *p,int offset) {return *(u32 *)(p+offset);}
static s16 half(u8 *p,int offset) {return *(s16 *)(p+offset);}
static f32 number(u32 u) {union {u32 u;f32 f;} v;v.u=u;return v.f;}
static void independent(int p,int w,int h) {
    u8 *b=expected.bytes;
    int special=b[4]<187;
    if(special) {store(b,w,word((f32)half(b,210)));store(b,h,word((f32)half(b,212)));}
    else {store(b,w,0x3F800000);store(b,h,0x3F800000);}
    store(b,p,load(b,20));
    if(special) {s16 offset=half(b,214);volatile f32 y=number(load(b,24))+(f32)offset;store(b,p+4,word(y));}
    else store(b,p+4,load(b,24));
    store(b,p+8,load(b,28));
}
''')

    def test_direct_compiler_and_sixteen_controls(self):
        self.assertEqual(self.words, self.retail)
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (41, 0, 0))
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                with self.subTest(name=name, profile=profile):
                    record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                    count = 44 if name == 'cached-id' else 43
                    wanted = (count, 43) if profile.startswith('o1') else (41, 8 if name == 'reverse-add' else 0)
                    self.assertEqual((record['body_words'], record['differences']), wanted)
                    self.assertEqual(record['diagnostics'], '')

    def test_guest_ordered_traces_aliases_and_coverage(self):
        coverage, cases = set(), 0
        for identity, case, outputs, phase in itertools.product(range(256), CASES, ALIASES, (0, 8)):
            memory = memory_case(identity, case)
            wanted, trace = reference(memory, outputs)
            for words in (self.retail, self.words):
                model = DimensionOracle(words, memory, outputs, phase).run()
                self.assertEqual(external(model.memory), wanted)
                self.assertEqual(events(model), trace)
                self.assertEqual(model.calls, [])
                if words is self.retail:
                    coverage.update(model.visits)
            cases += 1
        unreachable = screen.ENTRY+0x14
        self.assertEqual(coverage, set(range(screen.ENTRY, screen.ENTRY+164, 4))-{unreachable})
        self.assertEqual(self.retail[1:6], [0x284100BB, 0x10200019, 0x240100FF, 0x50410018, 0x3C013F80])
        self.assertEqual(cases, 36864)
        (self.output / 'behavior.json').write_text(json.dumps(dict(guest_cases=cases, models=2,
            reachable_words=len(coverage), unreachable_word=hex(unreachable), native_cases=18432), indent=2)+'\n')

    def test_native_real_actor_prefix_and_full_footprints(self):
        cases = ','.join('{%s,{%s}}' % (','.join(str(v) for v in case[:3]),
                    ','.join('0x%08X' % bits(v) for v in case[3])) for case in CASES)
        aliases = ','.join('{%s}' % ','.join(str(a-ACTOR) for a in outputs) for outputs in ALIASES)
        self.run_host('static struct {s16 w,h,d;u32 xyz[3];} cases[]={'+cases+'};\n'
                      'static int aliases[][3]={'+aliases+'};\n'+r'''
int id,c,a,i,count=0;
struct127 *actor=(struct127 *)actual.bytes;
if((u8 *)&actor->id-actual.bytes!=4 || (u8 *)&actor->x_position-actual.bytes!=20
   || (u8 *)&actor->y_position-actual.bytes!=24 || (u8 *)&actor->z_position-actual.bytes!=28
   || (u8 *)&actor->unkD2-actual.bytes!=210 || (u8 *)&actor->unkD4-actual.bytes!=212
   || (u8 *)&actor->unkD6-actual.bytes!=214 || sizeof(struct17)!=12) return 1;
for(id=0;id<256;id++) for(c=0;c<6;c++) for(a=0;a<12;a++) {
    for(i=0;i<1088;i++) actual.bytes[i]=0xA5;
    actor->id=id;actor->unkD2=cases[c].w;actor->unkD4=cases[c].h;actor->unkD6=cases[c].d;
    actor->x_position=number(cases[c].xyz[0]);actor->y_position=number(cases[c].xyz[1]);
    actor->z_position=number(cases[c].xyz[2]);
    for(i=0;i<1088;i++) expected.bytes[i]=actual.bytes[i];
    independent(aliases[a][0],aliases[a][1],aliases[a][2]);
    func_1515C1A0(actor,(struct17 *)(actual.bytes+aliases[a][0]),
                 (f32 *)(actual.bytes+aliases[a][1]),(f32 *)(actual.bytes+aliases[a][2]));
    for(i=0;i<1088;i++) if(actual.bytes[i]!=expected.bytes[i]) return 2;
    count++;
}
if(count!=18432) return 3;
''')

    def test_negative_controls_detect_stub_threshold_sign_and_offset(self):
        negatives = {'stub': 'void func_1515C1A0(struct127 *a, struct17 *p, f32 *w, f32 *h) {}',
                     'threshold': screen.SELECTED.replace('< 0xBB', '< 0xBC'),
                     'unsigned': screen.SELECTED.replace('= arg0->unkD2;', '= (u16)arg0->unkD2;'),
                     'offset': screen.SELECTED.replace('arg0->y_position + arg0->unkD6', 'arg0->y_position')}
        for name, body in negatives.items():
            _, words = screen.compile_candidate(self.root, self.output, 'wrong-'+name, body)
            identity = 187 if name == 'threshold' else 0
            memory = memory_case(identity, CASES[0])
            expected, _ = reference(memory, ALIASES[0])
            self.assertNotEqual(external(DimensionOracle(words, memory, ALIASES[0]).run().memory), expected, name)

    def test_production_direct_slot_and_no_target_guards(self):
        linked, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1515C1A0'], screen.ENTRY)
        self.assertEqual(linked['func_1515C1A0'], self.retail)
        source = (self.root / 'conker/src/game/generated_188F90.c').read_text()
        self.assertIn(screen.SELECTED, source)
        self.assertNotIn('func_1515C1A0', (self.root / 'conker/retail_word_patches.us.csv').read_text())


if __name__ == '__main__':
    unittest.main()
