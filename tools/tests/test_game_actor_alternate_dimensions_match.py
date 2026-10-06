"""Alternate signed actor fields, exact slot padding and sequential output aliases."""

import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_actor_alternate_dimensions_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import bits
from tools.tests.test_game_actor_dimensions_match import ACTOR, OUTPUT, CASES, DimensionOracle, memory_case, reference
from tools.tests.test_game_indexed_state_save_match import external, events
from tools.tests import test_game_random_curve_record as native

OFFSETS = (228, 230, 232)
ALIASES = ((OUTPUT, OUTPUT+32, OUTPUT+36), (OUTPUT, OUTPUT+32, OUTPUT+32),
           (OUTPUT, OUTPUT, OUTPUT+4), (ACTOR+20, OUTPUT+32, OUTPUT+36),
           (OUTPUT, ACTOR+228, OUTPUT+36), (OUTPUT, OUTPUT+32, ACTOR+228),
           (OUTPUT, OUTPUT+32, ACTOR+232), (OUTPUT, ACTOR+20, OUTPUT+36),
           (OUTPUT, OUTPUT+32, ACTOR+24), (ACTOR+228, OUTPUT+32, OUTPUT+36),
           (ACTOR+232, OUTPUT+32, OUTPUT+36), (ACTOR+224, OUTPUT+32, OUTPUT+36),
           (OUTPUT, OUTPUT, OUTPUT), (OUTPUT, ACTOR+4, OUTPUT+36))


class GameActorAlternateDimensionsMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-actor-alternate-dimensions-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.retail = list(struct.unpack_from('>43I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        header = (cls.root / 'conker/include/structs.h').read_text()
        actor = re.search(r'struct struct127 \{.*?(?=    f32 unkEC;)', header, re.S).group()+'};'
        point = re.search(r'typedef struct \{[^{}]*\} struct17;', header).group()
        cls.fixture = ('typedef unsigned char u8;typedef signed char s8;typedef short s16;'
                       'typedef unsigned short u16;typedef int s32;typedef unsigned int u32;typedef float f32;\n'
                       +actor+'\ntypedef struct struct127 struct127;\n'+point+'\n'+screen.SELECTED+r'''
static union {u32 aligned[272];u8 bytes[1088];} actual,expected;
static u32 word(f32 f) {union {u32 u;f32 f;} v;v.f=f;return v.u;}
static void store(u8 *p,int offset,u32 value) {*(u32 *)(p+offset)=value;}
static u32 load(u8 *p,int offset) {return *(u32 *)(p+offset);}
static s16 half(u8 *p,int offset) {return *(s16 *)(p+offset);}
static f32 number(u32 u) {union {u32 u;f32 f;} v;v.u=u;return v.f;}
static void independent(int p,int w,int h) {
    u8 *b=expected.bytes;
    int special=b[4]<187;
    if(special) {store(b,w,word((f32)half(b,228)));store(b,h,word((f32)half(b,230)));}
    else {store(b,w,0x3F800000);store(b,h,0x3F800000);}
    store(b,p,load(b,20));
    if(special) {s16 offset=half(b,232);volatile f32 y=number(load(b,24))+(f32)offset;store(b,p+4,word(y));}
    else store(b,p+4,load(b,24));
    store(b,p+8,load(b,28));
}
''')

    def test_direct_body_padding_and_sixteen_compiler_controls(self):
        self.assertEqual(self.words, self.retail[:41])
        self.assertEqual(self.retail[41:], [0, 0])
        self.assertEqual((self.record['body_words'], self.record['padding_words'],
                          self.record['frame'], self.record['differences'], self.record['exact']), (41, 2, 0, 0, True))
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                with self.subTest(name=name, profile=profile):
                    record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                    wanted = ((44, 43) if name == 'cached-id' else (43, 42)) if profile.startswith('o1') else (
                        41, 8 if name == 'reverse-add' else 0)
                    self.assertEqual((record['body_words'], record['differences']), wanted)
                    self.assertEqual(record['diagnostics'], '')

    def test_guest_signed_fields_aliases_traces_and_reachable_coverage(self):
        coverage, cases = set(), 0
        for identity, case, outputs, phase in itertools.product(range(256), CASES, ALIASES, (0, 8)):
            memory = memory_case(identity, case, OFFSETS)
            wanted, trace = reference(memory, outputs, OFFSETS)
            for words in (self.retail, self.words):
                model = DimensionOracle(words, memory, outputs, phase, screen.ENTRY).run()
                self.assertEqual(external(model.memory), wanted)
                self.assertEqual(events(model), trace)
                self.assertEqual(model.calls, [])
                if words is self.retail:
                    coverage.update(model.visits)
            cases += 1
        unreachable = {screen.ENTRY+0x14, screen.ENTRY+164, screen.ENTRY+168}
        self.assertEqual(coverage, set(range(screen.ENTRY, screen.ENTRY+172, 4))-unreachable)
        self.assertEqual(self.retail[1:6], [0x284100BB, 0x10200019, 0x240100FF, 0x50410018, 0x3C013F80])
        self.assertEqual(self.retail[18], 0x849800E8)
        self.assertEqual(cases, 43008)
        (self.output / 'behavior.json').write_text(json.dumps(dict(guest_cases=cases, models=2,
            reachable_words=len(coverage), unreachable_words=[hex(a) for a in sorted(unreachable)],
            native_cases=21504), indent=2)+'\n')

    def test_native_real_prefix_signed_cast_and_full_storage(self):
        cases = ','.join('{%s,{%s}}' % (','.join(str(v) for v in case[:3]),
                    ','.join('0x%08X' % bits(v) for v in case[3])) for case in CASES)
        aliases = ','.join('{%s}' % ','.join(str(a-ACTOR) for a in outputs) for outputs in ALIASES)
        self.run_host('static struct {s16 w,h,d;u32 xyz[3];} cases[]={'+cases+'};\n'
                      'static int aliases[][3]={'+aliases+'};\n'+r'''
int id,c,a,i,count=0;
struct127 *actor=(struct127 *)actual.bytes;
if((u8 *)&actor->id-actual.bytes!=4 || (u8 *)&actor->x_position-actual.bytes!=20
   || (u8 *)&actor->y_position-actual.bytes!=24 || (u8 *)&actor->z_position-actual.bytes!=28
   || (u8 *)&actor->unkE4-actual.bytes!=228 || (u8 *)&actor->unkE6-actual.bytes!=230
   || (u8 *)&actor->unkE8-actual.bytes!=232 || sizeof(struct17)!=12) return 1;
for(id=0;id<256;id++) for(c=0;c<6;c++) for(a=0;a<14;a++) {
    for(i=0;i<1088;i++) actual.bytes[i]=0xA5;
    actor->id=id;actor->unkE4=cases[c].w;actor->unkE6=cases[c].h;actor->unkE8=(u16)cases[c].d;
    actor->x_position=number(cases[c].xyz[0]);actor->y_position=number(cases[c].xyz[1]);
    actor->z_position=number(cases[c].xyz[2]);
    for(i=0;i<1088;i++) expected.bytes[i]=actual.bytes[i];
    independent(aliases[a][0],aliases[a][1],aliases[a][2]);
    func_1515C244(actor,(struct17 *)(actual.bytes+aliases[a][0]),
                 (f32 *)(actual.bytes+aliases[a][1]),(f32 *)(actual.bytes+aliases[a][2]));
    for(i=0;i<1088;i++) if(actual.bytes[i]!=expected.bytes[i]) return 2;
    count++;
}
if(count!=21504) return 3;
''')

    def test_wrong_stub_threshold_unsigned_offset_and_cached_fields_are_detected(self):
        cached = '''void func_1515C244(struct127 *a, struct17 *p, f32 *w, f32 *h) {
    f32 width = a->unkE4, height = a->unkE6;
    f32 x = a->x_position, y = a->y_position, z = a->z_position;
    s16 offset = (s16)a->unkE8;
    if (a->id < 0xBB && a->id != 0xFF) {
        *w = width; *h = height; p->unk0 = x; p->unk4 = y + offset; p->unk8 = z;
    } else {
        *w = 1.0f; *h = 1.0f; p->unk0 = x; p->unk4 = y; p->unk8 = z;
    }
}'''
        negatives = {'stub': 'void func_1515C244(struct127 *a, struct17 *p, f32 *w, f32 *h) {}',
                     'threshold': screen.SELECTED.replace('< 0xBB', '< 0xBC'),
                     'unsigned-offset': screen.SELECTED.replace('(s16)arg0->unkE8', 'arg0->unkE8'),
                     'unsigned-dimension': screen.SELECTED.replace('= arg0->unkE4;', '= (u16)arg0->unkE4;'),
                     'cached': cached}
        for name, body in negatives.items():
            _, words = screen.compile_candidate(self.root, self.output, 'wrong-'+name, body)
            identity = 187 if name == 'threshold' else 0
            outputs = ALIASES[4] if name == 'cached' else ALIASES[0]
            memory = memory_case(identity, CASES[0], OFFSETS)
            wanted, _ = reference(memory, outputs, OFFSETS)
            model = DimensionOracle(words, memory, outputs, entry=screen.ENTRY).run()
            self.assertNotEqual(external(model.memory), wanted, name)

    def test_production_complete_slot_and_unsigned_shared_field_preserved(self):
        linked, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1515C244'], screen.ENTRY)
        self.assertEqual(linked['func_1515C244'], self.retail)
        source = (self.root / 'conker/src/game/generated_188F90.c').read_text()
        self.assertIn(screen.SELECTED, source)
        self.assertNotIn('func_1515C244', (self.root / 'conker/retail_word_patches.us.csv').read_text())
        self.assertRegex((self.root / 'conker/include/structs.h').read_text(), r'u16 unkE8;')


if __name__ == '__main__':
    unittest.main()
