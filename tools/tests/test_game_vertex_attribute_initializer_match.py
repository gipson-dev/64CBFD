"""Alias-sensitive vertex attributes and the actual constructor/two-helper chain."""

import csv
import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_vertex_attribute_initializer_candidates as screen
from tools.experiments import game_source_effect_constructor_candidates as constructor
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native
from tools.tests import test_game_source_effect_constructor_match as effect
from tools.tests import test_game_view_corner_initializer_match as corners

BUFFER, INPUT = 0x20000, 0x20100
DELTAS = (-64,-48,-32,-24,-16,-12,-10,-8,-6,-4,-2,0,2,4,8,16,32,48,64)
PATTERNS = (-32768,-1,0,1,127,128,255,256,32767,0x8001,0xFF00,0x7F00)


def external(memory):
    return {a:v for a,v in memory.items() if not STACK-0x600 <= a < STACK+0x100}


def memory_case(seed):
    memory = {STACK+i:0xA5 for i in range(-0x600,0x100)}
    memory.update({BUFFER+i:(i*17+13)&255 for i in range(0x300)})
    for i in range(20):
        put(memory,INPUT+i*2,seed+i*7919,2)
    return memory


def reference(memory, output, source):
    result = dict(memory);events = []
    def load(address):
        value = int.from_bytes(bytes(result[address+i] for i in range(2)),'big')
        events.append(('R',address,2,value));return value
    def store(address,value,size):
        put(result,address,value,size)
        events.append(('W',address,size,value&((1<<(size*8))-1)))
    for index in range(4):
        out,src = output+index*16,source+index*10
        store(out+6,load(src+8),2)
        for component in range(3):
            store(out+12+component,load(src+component*2),1)
        alpha = load(src+6)
        store(out+6,0,2);store(out+15,alpha,1)
    return result,events


class GameVertexAttributeInitializerMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-vertex-attribute-initializer-test'
        cls.output.mkdir(exist_ok=True)
        cls.record,cls.words = screen.compile_candidate(cls.root,cls.output,'selected')
        cls.retail = list(struct.unpack_from('>48I',(cls.root/'conker/conker.us.bin').read_bytes(),screen.ROM))
        cls.production = load_elf_functions(str(cls.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        cls.directory = tempfile.TemporaryDirectory();cls.addClassCleanup(cls.directory.cleanup);cls.path = Path(cls.directory.name)
        cls.fixture = '''typedef unsigned char u8;typedef unsigned short u16;typedef short s16;typedef int s32;
'''+screen.SELECTED+r'''
static union {s32 alignment;u8 data[320];} storage;
static u16 read_half(u8 *p) {return (u16)((u16)p[0]|(u16)p[1]<<8);}
static void write_half(u8 *p,u16 value) {p[0]=(u8)value;p[1]=(u8)(value>>8);}
'''

    def test_direct_body_and_twenty_four_compiler_controls(self):
        self.assertEqual(self.words,self.retail)
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],self.record['diagnostics']),(48,0,0,''))
        expected = {'named-alpha':((48,0,32),(47,0,33),(24,8,47),(24,8,47)),
            'vertices':((48,0,33),(47,0,34),(24,8,47),(24,8,47)),
            'direct-colors':((48,0,0),(47,0,2),(22,8,47),(22,8,47)),
            'direct-vertices':((48,0,4),(47,0,6),(22,8,47),(22,8,47)),
            'short-alpha':((48,0,32),(47,0,33),(24,8,47),(24,8,47)),
            'indexed':((32,0,47),(32,0,47),(60,8,60),(60,8,60))}
        count = 0
        for name,body in screen.candidates():
            for index,profile in enumerate(screen.PROFILES):
                record,_ = screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                self.assertEqual((record['body_words'],record['frame'],record['differences']),expected[name][index],(name,profile))
                self.assertEqual(record['diagnostics'],'');count += 1
        self.assertEqual(count,24)

    def test_guest_full_signed_colors_aliases_intermediate_traces_and_all_words(self):
        cases,coverage = 0,set()
        for seed,delta,phase in itertools.product(PATTERNS,DELTAS,(0,8)):
            memory = memory_case(seed)
            wanted,events = reference(memory,INPUT+delta,INPUT)
            for body in (self.words,self.retail):
                model = TriangleOracle(body,memory,entry=screen.ENTRY,arguments=(INPUT+delta,INPUT),phase=phase).run()
                self.assertEqual(external(model.memory),external(wanted))
                self.assertEqual([e for e in model.events if not STACK-0x600<=e[1]<STACK+0x100],events)
                self.assertEqual(model.calls,[]);coverage.update(model.visits)
            cases += 1
        self.assertEqual((cases,len(coverage)),(456,48))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases,bodies=2,covered_words=len(coverage)),indent=2)+'\n')

    def test_every_halfword_bit_pattern_and_alias_phase(self):
        for value in range(65536):
            memory = memory_case(value);output = INPUT+DELTAS[value%len(DELTAS)]
            wanted,events = reference(memory,output,INPUT)
            model = TriangleOracle(self.words,memory,entry=screen.ENTRY,arguments=(output,INPUT),phase=(value&1)*8).run()
            self.assertEqual(external(model.memory),external(wanted))
            self.assertEqual([e for e in model.events if not STACK-0x600<=e[1]<STACK+0x100],events)

    def test_native_every_halfword_overlap_disjoint_and_whole_storage(self):
        self.run_host(r'''
static int deltas[9]={-64,-32,-16,-8,0,8,16,32,64};
int value,mode,i,j,offset;u8 expected[320];
if(sizeof(s16)!=2 || sizeof(u8)!=1 || sizeof(void *)!=4) return 1;
for(value=0;value<65536;value++) for(mode=0;mode<2;mode++) {
    offset=128+(mode?64:deltas[value%9]);
    for(i=0;i<320;i++) storage.data[i]=(u8)(i*17+13);
    for(i=0;i<20;i++) write_half(storage.data+128+i*2,(u16)(value+i*7919));
    for(i=0;i<320;i++) expected[i]=storage.data[i];
    for(i=0;i<4;i++) {
        u8 *out=expected+offset+i*16,*in=expected+128+i*10;u16 alpha;
        write_half(out+6,read_half(in+8));
        for(j=0;j<3;j++) out[12+j]=(u8)read_half(in+j*2);
        alpha=read_half(in+6);write_half(out+6,0);out[15]=(u8)alpha;
    }
    func_151400D0(storage.data+offset,storage.data+128);
    for(i=0;i<320;i++) if(storage.data[i]!=expected[i]) return 2;
}
''')

    def test_actual_constructor_and_both_helpers_guest_handoff(self):
        cases,coverage = 0,set()
        rom = (self.root/'conker/conker.us.bin').read_bytes()
        retail_ctor = list(struct.unpack_from('>114I',rom,constructor.ROM))
        retail_corner = list(struct.unpack_from('>55I',rom,corners.screen.ROM))
        for flag,fail,index,variant,mutation,plan,resource,alias in itertools.product((0,0x800000,0x2000000,0x82800000),
            (False,True),(0,1,254,255),range(4),(False,True),((-1,),(3,),(0,2,2,1)),(0,3),(False,True)):
            memory = effect.memory_case(flag,plan[0]);memory[effect.DESC] = index
            table = corners.memory_case(index,0,65535)
            memory.update({a:v for a,v in table.items() if corners.screen.TABLE-16<=a<corners.screen.TABLE+12*256+16})
            source = effect.ACTOR+0xC0 if alias else 0x800A4AA0
            args = (effect.DESC,source,39,0,0,23,variant,resource,255,4,255,0x80000000)
            actions = effect.actions_for(mutation)
            actions.pop('init',None);actions.pop('table',None)
            wanted,calls,result = effect.reference(memory,args,fail,plan,actions)
            if not fail:
                for offset in (0xC0,0xC4):
                    put(wanted,effect.ACTOR+offset,effect.word(memory,effect.ACTOR+offset))
                wanted = corners.reference(wanted,effect.ACTOR+0xC0,0xB2 if mutation else index,variant)
                wanted,_ = reference(wanted,effect.ACTOR+0xC0,source)
            traces = []
            for ctor,corner,attributes in ((self.production['func_1513D2F0'],self.production['func_1513FFF4'],self.words),
                                           (retail_ctor,retail_corner,self.retail)):
                connected = {corners.screen.ENTRY+i*4:w for i,w in enumerate(corner)}
                connected.update({screen.ENTRY+i*4:w for i,w in enumerate(attributes)})
                model = effect.ConstructorOracle(ctor,memory,args,fail,plan,actions,connected=connected).run()
                self.assertEqual((effect.external(model.memory),model.calls,model.r[2]),(wanted,calls,result))
                coverage.update(model.visits)
                traces.append([e for e in model.events if not STACK-0x600<=e[1]<STACK+0x100])
            self.assertEqual(traces[0],traces[1]);cases += 1
        self.assertEqual(cases,3072)
        self.assertEqual(coverage,set(range(constructor.ENTRY,constructor.ENTRY+456,4)) |
            set(range(corners.screen.ENTRY,corners.screen.ENTRY+220,4)) | set(range(screen.ENTRY,screen.ENTRY+192,4)))

    def test_native_actual_constructor_and_both_helpers_complete_footprint(self):
        saved = self.fixture;self.fixture = connected_native_fixture()
        self.addCleanup(setattr,self,'fixture',saved)
        self.run_host(r'''
int index,variant,f,i;u32 flags;void *result;u8 before[64];
for(i=0;i<256;i++) {D_80090B60[i].width=(u16)(i*257);D_80090B60[i].height=(u16)((255-i)*257);}
for(index=0;index<256;index++) for(variant=0;variant<256;variant++) for(f=0;f<2;f++) {
    initialize(f,(index+variant)&1,(index^variant)%6);D_80082FA0=bounds[plan][0];
    expectedKind=(u8)index;expectedMode=(u8)variant;expectedFirst=(u8)(index+variant);
    expectedSetup=(u8)(index-variant);expectedVariant=(u8)variant;expectedChannel=(u8)(index*17+variant);
    expectedResource=(index+variant)%3==0?0:((index+variant)%3==1?3:-1);
    expectedExtra=(s32)0x80000000+variant;expectedContext=(s32)0x87654321;expectedPayload=(index&1)?4:-0x110;
    for(i=0;i<64;i++) attributes.bytes[i]=(u8)(i*31+7);
    for(i=0;i<20;i++) write_half(attributes.bytes+16+i*2,(u16)(index*257+variant*7919+i*17));
    copy_bytes(before,attributes.bytes,64);expectedTable=(s32)(attributes.bytes+16);
    flags=(index&1?0x800000:0)|(index&2?0x2000000:0)|(index&4?0x80000000:0);
    descriptor[0]=(u8)index;descriptorBefore[16]=(u8)index;store(descriptor+0x40,flags);expectedFlags=flags;
    result=func_1513D2F0(descriptor,expectedTable,expectedKind,expectedMode,expectedFirst,
        expectedSetup,expectedVariant,expectedResource,expectedExtra,expectedPayload,expectedChannel,expectedContext);
    if(result!=(f?NULL:actor) || verify()) return 1;
    for(i=0;i<64;i++) if(attributes.bytes[i]!=before[i]) return 2;
}
''')

    def test_compiled_negatives_detect_transient_flags_order_strides_and_stores(self):
        variants = [('stub','void func_151400D0(u8 *out,u8 *input) {}'),
            ('initial-flags',screen.SELECTED.replace('        *(u16 *)(out + 6) = *(u16 *)(input + 8);\n','')),
            ('clear-order',screen.SELECTED.replace('        out[15] = *(s16 *)(input + 6);\n        *(u16 *)(out + 6) = 0;',
                '        *(u16 *)(out + 6) = 0;\n        out[15] = *(s16 *)(input + 6);')),
            ('stride',screen.SELECTED.replace('input += 10','input += 8')),
            ('count',screen.SELECTED.replace('i < 4','i < 3')),
            ('store',screen.SELECTED.replace('out[14]','out[13]'))]
        for name,body in variants:
            _,words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            rejected = False
            for seed,delta in itertools.product(PATTERNS,DELTAS):
                memory = memory_case(seed);wanted,events = reference(memory,INPUT+delta,INPUT)
                model = TriangleOracle(words,memory,entry=screen.ENTRY,arguments=(INPUT+delta,INPUT)).run()
                if external(model.memory)!=external(wanted):
                    rejected = True;break
            self.assertTrue(rejected,name)

    def test_installed_body_slot_abi_retained_chain_and_no_guards(self):
        owner = (self.root/'conker/src/game_169510.c').read_text()
        self.assertIn(screen.SELECTED,owner)
        self.assertIn('void func_151400D0(u8 *out, u8 *input);',owner)
        self.assertNotIn('#pragma GLOBAL_ASM("asm/nonmatchings/game_169510/func_151400D0.s")',owner)
        self.assertEqual(self.production['func_151400D0'],self.retail)
        rom = (self.root/'conker/conker.us.bin').read_bytes()
        self.assertEqual(self.production['func_1513D2F0'],list(struct.unpack_from('>114I',rom,constructor.ROM)))
        self.assertEqual(self.production['func_1513FFF4'],list(struct.unpack_from('>55I',rom,corners.screen.ROM)))
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        self.assertEqual(len(guards),10685)
        self.assertFalse([row for row in guards if row['function']=='func_151400D0'])


def connected_native_fixture():
    fixture = corners.connected_native_fixture(dict(corners.screen.candidates())['global-declaration'])
    hook = re.search(r'void func_151400D0\([^;{}]+\) \{\n.*?\n\}',fixture,re.S).group(0)
    fixture = fixture.replace(hook,r'''void func_151400D0(u8 *helper,u8 *table) {
    if(stage++!=4 || helper!=actor+0xC0 || table!=(u8 *)expectedTable) error=7;
    actual_vertex_initializer(helper,table);
}''')
    fixture = fixture.replace('store(e+0xC4,(u32)expectedTable);','reference_attributes(e+0xC0,(u8 *)expectedTable);')
    fixture = fixture.replace('bits(mutation?0.5f:-10000)','bits(mutation?-1.0f:-10000)')
    fixture = fixture.replace('bits(mutation?(n?-3:0.5f):-10000)','bits(mutation?(n?-3:-1.0f):-10000)')
    fixture = fixture.replace('D_80082FA0!=99','D_80082FA0!=bounds[plan][0]')
    fixture = fixture.replace('#define NULL ((void *)0)\n','#define NULL ((void *)0)\n'+screen.SELECTED.replace(
        'func_151400D0','actual_vertex_initializer')+r'''
static union {u32 alignment;u8 bytes[64];} attributes;
static u16 read_half(u8 *p) {return (u16)((u16)p[0]|(u16)p[1]<<8);}
static void write_half(u8 *p,u16 value) {p[0]=(u8)value;p[1]=(u8)(value>>8);}
static void reference_attributes(u8 *out,u8 *input) {
    int i,j;
    for(i=0;i<4;i++) {
        u8 *vertex=out+i*16,*row=input+i*10;u16 alpha;
        write_half(vertex+6,read_half(row+8));
        for(j=0;j<3;j++) vertex[12+j]=(u8)read_half(row+j*2);
        alpha=read_half(row+6);write_half(vertex+6,0);vertex[15]=(u8)alpha;
    }
}
''')
    return fixture
