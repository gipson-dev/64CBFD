"""View-corner arithmetic, untouched storage, and actual constructor handoffs."""

import csv
import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_view_corner_initializer_candidates as screen
from tools.experiments import game_source_effect_constructor_candidates as constructor
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_source_effect_constructor_match as effect
from tools.tests import test_game_random_curve_record as native

OUTPUT = 0x20000
OFFSETS = (0x38, 8, 0x28, 0x18, 0x1A, 0xA, 0x3A, 0x2A)
DIMENSIONS = ((0, 0), (1, 65535), (65535, 1), (0x8000, 0x401))


def external(memory):
    return {a:v for a,v in memory.items() if not STACK-0x600 <= a < STACK+0x100}


def memory_case(index, width, height, output=OUTPUT):
    memory = {STACK+i:0xA5 for i in range(-0x600,0x100)}
    for base,length in ((screen.TABLE-16,12*256+32),(output-16,96)):
        memory.update({base+i:(i*17+13)&255 for i in range(length)})
    put(memory,screen.TABLE+index*12+6,width,2)
    put(memory,screen.TABLE+index*12+8,height,2)
    return memory


def reference(memory, output, index, variant):
    result = dict(memory)
    index &= 255
    if index != 255:
        address = screen.TABLE+index*12
        dimensions = [int.from_bytes(bytes(memory[address+offset+i] for i in range(2)),'big')
                      for offset in (6,8)]
        x,y = (((value-1)&65535)<<6 for value in dimensions)
        values = (x if variant&1 else 0,)*2+(0 if variant&1 else x,)*2
        values += (y if variant&2 else 0,)*2+(0 if variant&2 else y,)*2
        for offset,value in zip(OFFSETS,values):
            put(result,output+offset,value,2)
    return result


class GameViewCornerInitializerMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-view-corner-initializer-test'
        cls.output.mkdir(exist_ok=True)
        cls.record,cls.words = screen.compile_candidate(cls.root,cls.output,'selected')
        cls.retail = list(struct.unpack_from('>55I',(cls.root/'conker/conker.us.bin').read_bytes(),screen.ROM))
        cls.production = load_elf_functions(str(cls.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        cls.directory = tempfile.TemporaryDirectory();cls.addClassCleanup(cls.directory.cleanup);cls.path = Path(cls.directory.name)
        cls.global_body = dict(screen.candidates())['global-declaration']
        cls.fixture = ('typedef unsigned char u8;typedef unsigned short u16;typedef short s16;typedef int s32;\n'
            +cls.global_body+'\nViewDimensions169510 D_80090B60[256];\n'
            +'static union {s32 align;u8 data[96];} storage;\n')

    def test_direct_body_and_forty_compiler_controls(self):
        self.assertEqual(self.words,self.retail)
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],self.record['diagnostics']),(55,8,0,''))
        direct = ((55,8,0),(53,8,53),(65,16,65),(64,16,64))
        expected = {'repeated':((71,8,49),(69,8,67),(87,8,85),(86,8,86)),
            'shared-halfword':((63,8,42),(61,8,57),(68,8,67),(67,8,66)),
            'shared-word':((55,8,25),(53,8,53),(68,8,67),(67,8,66)),
            'record-pointer':direct,'coordinate-first':direct,'height-first':direct,
            'unsigned-coordinate':direct,'global-declaration':direct,
            'register-coordinate':((55,8,0),(53,8,53),(57,16,56),(56,16,56)),
            'address-abi':((50,0,55),(49,0,53),(73,16,73),(73,16,73))}
        count = 0
        for name,body in screen.candidates():
            for index,profile in enumerate(screen.PROFILES):
                record,_ = screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                self.assertEqual((record['body_words'],record['frame'],record['differences']),expected[name][index],(name,profile))
                self.assertEqual(record['diagnostics'],'');count += 1
        self.assertEqual(count,40)

    def test_full_guest_dimensions_variants_traces_and_all_words(self):
        cases,coverage = 0,set()
        for index,variant,(width,height) in itertools.product(range(256),(0,1,2,3,0x80,0xFD,0xFE,0xFF),DIMENSIONS):
            memory = memory_case(index,width,height)
            wanted = external(reference(memory,OUTPUT,index,variant));traces = []
            for body in (self.words,self.retail):
                model = TriangleOracle(body,memory,entry=screen.ENTRY,phase=index&8,
                    arguments=(OUTPUT,0xABCD0000|index,0xFEDC0000|variant)).run()
                self.assertEqual(external(model.memory),wanted);self.assertEqual(model.calls,[])
                traces.append([e for e in model.events if not STACK-0x600<=e[1]<STACK+0x100])
                coverage.update(model.visits)
            self.assertEqual(traces[0],traces[1]);cases += 1
        self.assertEqual((cases,len(coverage)),(8192,55))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases,bodies=2,covered_words=len(coverage)),indent=2)+'\n')

    def test_every_index_variant_byte_pair_with_high_incoming_bits(self):
        for index,variant in itertools.product(range(256),repeat=2):
            memory = memory_case(index,index*257,(255-index)*257)
            wanted = external(reference(memory,OUTPUT,index,variant))
            model = TriangleOracle(self.words,memory,entry=screen.ENTRY,phase=(variant&1)*8,
                arguments=(OUTPUT,0xABCD0000|index,0xFEDC0000|variant)).run()
            self.assertEqual(external(model.memory),wanted);self.assertEqual(model.calls,[])

    def test_no_access_sentinel_and_captured_dimensions_under_table_alias(self):
        for index,variant in itertools.product((255,0xABCD00FF,0xFFFFFFFF),(0,1,2,3,255)):
            memory = {STACK+i:0xA5 for i in range(-0x600,0x100)}
            for body in (self.words,self.retail):
                model = TriangleOracle(body,memory,entry=screen.ENTRY,arguments=(0xDEADC0DE,index,variant)).run()
                self.assertEqual(external(model.memory),{})
                self.assertEqual([e for e in model.events if not STACK-0x600<=e[1]<STACK+0x100],[])
        cases = 0
        for index,variant,(width,height),delta in itertools.product((0,1,254,255),range(4),DIMENSIONS,(-0x38,-8,0,8)):
            output = screen.TABLE+index*12+delta
            memory = memory_case(index,width,height,output)
            wanted = external(reference(memory,output,index,variant))
            for body in (self.words,self.retail):
                model = TriangleOracle(body,memory,entry=screen.ENTRY,arguments=(output,index,variant)).run()
                self.assertEqual(external(model.memory),wanted)
            cases += 1
        self.assertEqual(cases,256)

    def test_native_every_unsigned_dimension_and_all_byte_pairs(self):
        self.run_host(r'''
int dimension,variant,index,i;u8 expected[96];u16 x,y;
if(sizeof(ViewDimensions169510)!=12 || __builtin_offsetof(ViewDimensions169510,width)!=6
   || __builtin_offsetof(ViewDimensions169510,height)!=8 || sizeof(void *)!=4) return 1;
for(dimension=0;dimension<65536;dimension++) for(variant=0;variant<8;variant++) {
    static int offsets[8]={0x38,8,0x28,0x18,0x1A,0xA,0x3A,0x2A};
    index=dimension%255;
    D_80090B60[index].width=(u16)dimension;D_80090B60[index].height=(u16)(65535-dimension);
    for(i=0;i<96;i++) expected[i]=storage.data[i]=(u8)(i*17+13);
    x=(u16)(((u16)(dimension-1))<<6);y=(u16)(((u16)(65534-dimension))<<6);
    for(i=0;i<8;i++) {
        u16 value=i<4?((i<2)==!!(variant&1)?x:0):((i<6)==!!(variant&2)?y:0);
        expected[16+offsets[i]]=(u8)value;expected[17+offsets[i]]=(u8)(value>>8);
    }
    func_1513FFF4(storage.data+16,(u8)index,(u8)(0x80|variant));
    for(i=0;i<96;i++) if(storage.data[i]!=expected[i]) return 2;
}
for(index=0;index<256;index++) for(variant=0;variant<256;variant++) {
    static int offsets[8]={0x38,8,0x28,0x18,0x1A,0xA,0x3A,0x2A};
    D_80090B60[index].width=(u16)(index*257);D_80090B60[index].height=(u16)((255-index)*257);
    for(i=0;i<96;i++) expected[i]=storage.data[i]=(u8)(i*31+7);
    x=(u16)(((u16)(index*257-1))<<6);y=(u16)(((u16)((255-index)*257-1))<<6);
    if(index!=255) for(i=0;i<8;i++) {
        u16 value=i<4?((i<2)==!!(variant&1)?x:0):((i<6)==!!(variant&2)?y:0);
        expected[16+offsets[i]]=(u8)value;expected[17+offsets[i]]=(u8)(value>>8);
    }
    func_1513FFF4(storage.data+16,(u8)(0xABCD0000|index),(u8)(0xFEDC0000|variant));
    for(i=0;i<96;i++) if(storage.data[i]!=expected[i]) return 3;
}
func_1513FFF4((u8 *)0,255,255);
''')

    def test_actual_constructor_helper_guest_handoff(self):
        cases,coverage = 0,set()
        flags = (0,0x800000,0x2000000,0x82800000)
        for flag,fail,index,variant,mutation,plan,resource in itertools.product(flags,(False,True),(0,1,254,255),
            range(4),(False,True),((-1,),(3,),(0,2,2,1)),(0,3)):
            memory = effect.memory_case(flag,plan[0])
            table = memory_case(index,0,65535)
            memory.update({a:v for a,v in table.items() if screen.TABLE-16<=a<screen.TABLE+12*256+16})
            memory[effect.DESC] = index
            args = (effect.DESC,0x800A4AA0,39,0,0,23,variant,resource,255,4,255,0x80000000)
            actions = effect.actions_for(mutation);actions.pop('init',None)
            wanted,calls,result = effect.reference(memory,args,fail,plan,actions)
            if not fail:
                put(wanted,effect.ACTOR+0xC0,effect.word(memory,effect.ACTOR+0xC0))
                wanted = reference(wanted,effect.ACTOR+0xC0,0xB2 if mutation else index,variant)
            traces = []
            for helper,ctor in ((self.words,self.production['func_1513D2F0']),
                                (self.retail,list(struct.unpack_from('>114I',(self.root/'conker/conker.us.bin').read_bytes(),constructor.ROM)))):
                connected = {screen.ENTRY+i*4:w for i,w in enumerate(helper)}
                model = effect.ConstructorOracle(ctor,memory,args,fail,plan,actions,connected=connected).run()
                self.assertEqual((effect.external(model.memory),model.calls,model.r[2]),(wanted,calls,result))
                coverage.update(model.visits)
                traces.append([e for e in model.events if not STACK-0x600<=e[1]<STACK+0x100])
            self.assertEqual(traces[0],traces[1]);cases += 1
        self.assertEqual(cases,1536)
        self.assertEqual(coverage,set(range(screen.ENTRY,screen.ENTRY+220,4)) | set(range(constructor.ENTRY,constructor.ENTRY+456,4)))

    def test_native_actual_constructor_helper_complete_footprint(self):
        saved = self.fixture
        self.fixture = connected_native_fixture(self.global_body)
        self.addCleanup(setattr,self,'fixture',saved)
        self.run_host(r'''
int index,variant,f,i;u32 flags;void *result;
for(i=0;i<256;i++) {D_80090B60[i].width=(u16)(i*257);D_80090B60[i].height=(u16)((255-i)*257);}
for(index=0;index<256;index++) for(variant=0;variant<256;variant++) for(f=0;f<2;f++) {
    initialize(f,(index+variant)&1,(index^variant)%6);
    expectedKind=(u8)index;expectedMode=(u8)variant;expectedFirst=(u8)(index+variant);
    expectedSetup=(u8)(index-variant);expectedVariant=(u8)variant;expectedChannel=(u8)(index*17+variant);
    expectedResource=(index+variant)%3==0?0:((index+variant)%3==1?3:-1);
    expectedExtra=(s32)0x80000000+variant;expectedContext=(s32)0x87654321;expectedPayload=(index&1)?4:-0x110;
    flags=(index&1?0x800000:0)|(index&2?0x2000000:0)|(index&4?0x80000000:0);
    descriptor[0]=(u8)index;descriptorBefore[16]=(u8)index;store(descriptor+0x40,flags);expectedFlags=flags;
    result=func_1513D2F0(descriptor,expectedTable,expectedKind,expectedMode,expectedFirst,
        expectedSetup,expectedVariant,expectedResource,expectedExtra,expectedPayload,expectedChannel,expectedContext);
    if(result!=(f?NULL:actor) || verify()) return 1;
}
''')

    def test_compiled_negatives_detect_gate_dimensions_variant_and_store(self):
        variants = [('stub','void func_1513FFF4(u8 *out,u8 index,u8 variant) {}'),
            ('gate',screen.SELECTED.replace('index != 255','index < 254')),
            ('dimension',screen.SELECTED.replace('record->width - 1','record->width + 1')),
            ('variant',screen.SELECTED.replace('variant & 2','variant & 4')),
            ('scale',screen.SELECTED.replace('<< 6','<< 5')),
            ('store',screen.SELECTED.replace('out + 0x2A','out + 0x2C'))]
        for name,body in variants:
            _,words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            rejected = False
            for index,variant in itertools.product((0,254,255),range(8)):
                memory = memory_case(index,0x123,0x456)
                model = TriangleOracle(words,memory,entry=screen.ENTRY,arguments=(OUTPUT,index,variant)).run()
                if external(model.memory)!=external(reference(memory,OUTPUT,index,variant)):
                    rejected = True;break
            self.assertTrue(rejected,name)

    def test_installed_body_slot_retained_constructor_and_no_guards(self):
        owner = (self.root/'conker/src/game_169510.c').read_text()
        self.assertIn(screen.SELECTED,owner)
        self.assertIn('void func_1513FFF4(u8 *out, u8 index, u8 variant);',owner)
        self.assertNotIn('#pragma GLOBAL_ASM("asm/nonmatchings/game_169510/func_1513FFF4.s")',owner)
        self.assertEqual(self.production['func_1513FFF4'],self.retail)
        self.assertEqual(self.production['func_1513D2F0'],list(struct.unpack_from('>114I',
            (self.root/'conker/conker.us.bin').read_bytes(),constructor.ROM)))
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        self.assertEqual(len(guards),10738)
        self.assertFalse([row for row in guards if row['function']=='func_1513FFF4'])


def connected_native_fixture(body):
    fixture = effect.native_fixture()
    hook = re.search(r'void func_1513FFF4\([^;{}]+\) \{\n.*?\n\}',fixture,re.S).group(0)
    fixture = fixture.replace(hook,r'''void func_1513FFF4(u8 *helper,u8 index,u8 variant) {
    if(stage++!=3 || helper!=actor+0xC0 || index!=(mutation?0xB2:copied[0]) || variant!=expectedVariant) error=5;
    actual_view_initializer(helper,index,variant);
}''')
    fixture = fixture.replace('store(e+0xC0,0x12345678);',
        'reference_corners(e+0xC0,mutation?0xB2:copied[0],expectedVariant);')
    fixture = fixture.replace('''#define NULL ((void *)0)
''','''#define NULL ((void *)0)
'''+body.replace('func_1513FFF4','actual_view_initializer')+r'''
ViewDimensions169510 D_80090B60[256];
static void reference_corners(u8 *out,u8 index,u8 variant) {
    static int offsets[8]={0x38,8,0x28,0x18,0x1A,0xA,0x3A,0x2A};
    u8 *row=(u8 *)D_80090B60+index*12;u32 x,y;int i;
    if(index==255) return;
    x=((((u32)row[6]|(u32)row[7]<<8)-1)&65535)<<6;
    y=((((u32)row[8]|(u32)row[9]<<8)-1)&65535)<<6;
    for(i=0;i<8;i++) {
        u32 value=i<4?((i<2)==!!(variant&1)?x:0):((i<6)==!!(variant&2)?y:0);
        out[offsets[i]]=(u8)value;out[offsets[i]+1]=(u8)(value>>8);
    }
}
''')
    return fixture+'\n'+constructor.SELECTED+'\n'
