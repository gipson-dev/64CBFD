"""Source-backed actor packet; ordered guest traces and actual constructor C."""

import csv
import itertools
import json
import re
import struct
import subprocess
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from tools.experiments import game_actor_source_packet_candidates as screen
from tools.match_progress import load_elf_functions
from tools.patch_generated_slice_ld import load_game_data_layout
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native
from tools.tests import test_game_extended_child_constructor as constructor

SOURCE, ACTOR, DEFAULT, FACTOR = 0x20000, 0x21000, 0x800A5480, 0x800A8CD4
HOLES = (0x59,0x5A,0x5B,0x69,0x6B,0x71,0x76,0x77)
ARGUMENTS = ((0,0,0),(1,1,1),(0xABCD7FFF,0xFEDC8000,0x12340080),
             (0xABCD8000,0xFEDC7FFF,0x123400FF),(0xABCDFFFF,0xFEDCFFFF,0x12340100),
             (0xFFFFFFFF,0x80000000,0xFFFFFFFF),(0x1234ABCD,0x76543210,0xABCDEFEE),(232,-53,255))


def target_guards(root):
    with (root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
        return [r for r in csv.DictReader(stream) if r['function']=='func_1519EB8C']


def relocated(word, specification):
    if specification=='-':
        return word
    kind,name = specification.split(':')
    address = int(name[2:],16)
    value = (address+0x8000)>>16 if kind=='R_MIPS_HI16' else address & 65535
    return word | value


def guarded(root, words):
    result = list(words)
    for row in target_guards(root):
        index = int(row['offset'],0)//4
        expected = relocated(int(row['expected'],0),row['expected_relocations'])
        assert result[index]==expected,(index,hex(result[index]),hex(expected))
        result[index] = relocated(int(row['replacement'],0),row['replacement_relocations'])
    return result


def external(memory):
    return {a:v for a,v in memory.items() if not STACK-0x600 <= a < STACK+0x100}


def memory_case(pattern=0,padding=0xA5):
    memory = {STACK+i:padding for i in range(-0x600,0x100)}
    for base in (SOURCE-0x180,ACTOR-16):
        memory.update({base+i:(i*17+13)&255 for i in range(0x380)})
    memory.update({DEFAULT+i:0xA5 for i in range(-16,28)})
    memory.update({FACTOR+i:0xA5 for i in range(-4,8)})
    values = ((1.25,-2.5,4.0,6.0,-8.0,12.0,100.0,-160.0),
              (-0.0,0.0,-20.0,-6.0,8.0,-12.0,-0.0,0.0),
              (17.0,31.0,-13.0,0.0,-0.0,1.0,0.125,-0.25))[pattern]
    for i,value in enumerate(values):
        put(memory,SOURCE+i*4,bits(value))
    for i,value in enumerate((3.0,4.0,12.0)):
        put(memory,DEFAULT+i*4,bits(value))
    put(memory,FACTOR,0x3DCCCCCD)
    return memory


def word(memory,address):
    return int.from_bytes(bytes(memory[address+i] for i in range(4)),'big')


def packet_bytes(memory,resource,lifetime,padding):
    packet = bytearray([padding]*124)
    def store(offset,value,size=4):
        packet[offset:offset+size] = (value & ((1<<(8*size))-1)).to_bytes(size,'big')
    for offset in (0,4,0x1C,0x20,0x24):
        store(offset,0x3F800000)
    for offset,input_offset in ((8,0x18),(12,0x1C)):
        store(offset,bits(floating(word(memory,SOURCE+input_offset))*floating(word(memory,FACTOR))))
    for offset,input_offset in ((0x10,12),(0x14,16),(0x18,20),(0x28,0),(0x2C,4),(0x30,8)):
        store(offset,word(memory,SOURCE+input_offset))
    for offset in (0x34,0x40):
        packet[offset:offset+12] = bytes(memory[DEFAULT+i] for i in range(12))
    for offset,value in ((0x4C,0),(0x50,0x980),(0x5C,0),(0x6C,0),(0x78,0)):
        store(offset,value)
    for offset,value in ((0x54,lifetime),(0x56,resource),(0x72,1),(0x74,255)):
        store(offset,value,2)
    for offset,value in ((0x58,0),(0x60,255),(0x61,21),*( (i,0) for i in range(0x62,0x68)),
                         (0x68,2),(0x6A,0),(0x70,0)):
        store(offset,value,1)
    return bytes(packet)


class SourcePacketOracle(TriangleOracle):
    def __init__(self,words,memory,resource=0,lifetime=0,channel=0,context=0,phase=0,
                 result=ACTOR,mutation=False):
        super().__init__(words,memory,entry=screen.ENTRY,phase=phase,
            arguments=(SOURCE,resource & 0xFFFFFFFF,lifetime & 0xFFFFFFFF,channel & 0xFFFFFFFF,context & 0xFFFFFFFF))
        self.result,self.mutation = result,mutation

    def record_call(self,target):
        if target==screen.CONSTRUCTOR:
            packet,resource,value,state,size,channel,context = self.arguments(7)
            assert packet==self.before[29]-124
            snapshot = bytes(self.memory[packet+i] for i in range(124))
            call = (target,snapshot,resource,value,state,size,channel,context)
        else:
            assert target==screen.COPY
            destination,source,size = self.r[4:7]
            assert source==self.before[29]-128 and size==4
            call = (target,destination,self.peek(source,4),size)
        self.calls.append(call)
        self.events.append(('CALL',target,call[1:]))

    def hook(self,target):
        if target==screen.CONSTRUCTOR:
            if self.mutation:
                for address in (SOURCE,DEFAULT,DEFAULT+4,DEFAULT+8,FACTOR,self.r[4]+0x50):
                    self.put(address,0x12345678,4)
            result = self.result
        else:
            destination,source,size = self.r[4:7]
            for i in range(size):
                self.put(destination+i,self.get(source+i,1),1)
            result = destination
        for register in (1,2,3,*range(4,16),24,25):
            self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]
        self.r[2] = result


class GameActorSourcePacketMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-actor-source-packet-test'
        cls.output.mkdir(exist_ok=True)
        cls.record,cls.raw = screen.compile_candidate(cls.root,cls.output,'selected')
        cls.words = guarded(cls.root,cls.raw)
        cls.retail = list(struct.unpack_from('>102I',(cls.root/'conker/conker.us.bin').read_bytes(),screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = ('''typedef unsigned char u8;typedef short s16;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;typedef float f32;
#define NULL ((void *)0)
''' + screen.LAYOUTS+'\n'+r'''
Position1CBE20 D_800A5480;f32 D_800A8CD4;
static union {u32 align;u8 bytes[0x230];} storage;
static Source1CBE20 source;
static u32 sourceWords[8],defaultWords[3];
static s32 expectedContext;static u16 expectedResource;static s16 expectedLifetime;
static u8 expectedChannel;static int calls,copies,error,fail,mutation;
static u32 word(f32 f) {union {f32 f;u32 u;} v;v.f=f;return v.u;}
static f32 number(u32 u) {union {f32 f;u32 u;} v;v.u=u;return v.f;}
void *func_1513264C(void *data,s32 resource,s32 value,void *state,s32 size,u8 channel,s32 context) {
    ActorDescriptor1CBE20 *p=data;calls++;
    if(resource!=3 || value!=255 || state || size!=4 || channel!=expectedChannel || context!=expectedContext) error=1;
    if(p->field00!=1 || p->field04!=1 || p->field1C!=1 || p->field20!=1 || p->field24!=1
       || word(p->field08)!=word(number(sourceWords[6])*D_800A8CD4)
       || word(p->field0C)!=word(number(sourceWords[7])*D_800A8CD4)) error=2;
    if(word(p->position.x)!=sourceWords[0] || word(p->position.y)!=sourceWords[1] || word(p->position.z)!=sourceWords[2]
       || word(p->vector.x)!=sourceWords[3] || word(p->vector.y)!=sourceWords[4] || word(p->vector.z)!=sourceWords[5]) error=3;
    if(word(p->first.x)!=defaultWords[0] || word(p->first.y)!=defaultWords[1] || word(p->first.z)!=defaultWords[2]
       || word(p->second.x)!=defaultWords[0] || word(p->second.y)!=defaultWords[1] || word(p->second.z)!=defaultWords[2]) error=4;
    if(word(p->field4C) || p->flags!=0x980 || p->lifetime!=expectedLifetime || p->resource!=expectedResource
       || p->field58 || p->field5C || p->field60!=255 || p->field61!=21 || p->field62 || p->field63
       || p->field64 || p->field65 || p->field66 || p->field67 || p->field68!=2 || p->field6A
       || p->field6C || p->field70 || p->field72!=1 || p->field74!=255 || p->field78) error=5;
    if(mutation) {source.position.x=number(0x12345678);D_800A5480.x=D_800A5480.y=D_800A5480.z=number(0x12345678);
        D_800A8CD4=number(0x12345678);p->flags=0;}
    return fail?NULL:storage.bytes+16;
}
void *memcpy(void *destination,const void *input,u32 size) {
    const u8 *p=input;u32 i;copies++;
    if(destination!=storage.bytes+16+0x170 || size!=4 || *(Source1CBE20 *const *)input!=&source) error=6;
    for(i=0;i<size;i++) ((u8 *)destination)[i]=p[i];
    return destination;
}
''' + screen.SELECTED+'\n')

    def test_compiler_controls_closed_schedule_and_relocation_guards(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],
                          self.record['diagnostics']),(102,0xB8,14,''))
        self.assertEqual(self.words,self.retail)
        rows = target_guards(self.root)
        self.assertEqual([int(r['offset'],0) for r in rows],list(range(8,64,4)))
        self.assertEqual(Counter(self.raw[:16]),Counter(self.retail[:16]))
        self.assertEqual(self.raw[16:],self.retail[16:])
        self.assertEqual(Counter((r['expected'],r['expected_relocations']) for r in rows),
                         Counter((r['replacement'],r['replacement_relocations']) for r in rows))
        relocations = subprocess.check_output(['mips-linux-gnu-objdump','-r',str(self.output/'selected.o')],text=True)
        actual = {int(a,16):f'{kind}:{name}' for a,kind,name in re.findall(r'^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\w+)\s*$',relocations,re.M)}
        for row in rows:
            self.assertEqual(actual.get(int(row['offset'],0),'-'),row['expected_relocations'])
            self.assertEqual((row['filename'],row['omit'],row['insert_after']),('generated_1CBE20','false',''))
        wrong = self.raw.copy();wrong[2]^=1
        with self.assertRaises(AssertionError):
            guarded(self.root,wrong)
        expected = {
            'field-order':((102,184,14),(101,184,95),(111,176,111),(111,176,110)),
            'size-after-scalars':((102,184,14),(101,184,95),(111,176,111),(111,176,110)),
            'vector-copy':((103,184,90),(102,184,72),(113,176,113),(113,176,112)),
            'position-copy':((103,184,90),(102,184,72),(112,176,112),(112,176,111)),
            'wide-lifetime':((102,184,15),(101,184,95),(111,176,111),(111,176,110)),
            'wide-resource':((102,184,15),(101,184,95),(111,176,111),(111,176,110)),
            'captured-factor':((102,184,14),(101,184,95),(111,176,111),(111,176,111)),
            'factor-assignment':((102,184,14),(101,184,95),(111,176,111),(111,176,111)),
            'captured-unit-factor':((102,192,56),(101,192,97),(108,184,107),(108,184,106)),
            'register-unit-factor':((102,192,56),(101,192,97),(109,200,109),(109,200,109)),
            'factor-and-default-address':((102,192,56),(101,192,97),(111,184,109),(111,184,109)),
            'unit-from-first-field':((102,184,14),(101,184,95),(110,176,109),(110,176,107)),
            'chained-unit-fields':((102,184,14),(101,184,95),(110,176,109),(110,176,107)),
            'dimensions-first':((102,184,29),(101,184,97),(110,176,109),(110,176,109))}
        self.assertEqual(len(screen.candidates()),14)
        for name,body in screen.candidates():
            for i,profile in enumerate(screen.PROFILES):
                record,_ = screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                self.assertEqual((record['body_words'],record['frame'],record['differences']),expected[name][i])
                self.assertEqual(record['diagnostics'],'')

    def test_guest_packets_padding_aliases_external_traces_and_lifetimes(self):
        cases,coverage = 0,set()
        for args,context,phase,padding,mutation,result,pattern in itertools.product(ARGUMENTS,
            (0,-1,0x80000000,0x7FFFFFFF),(0,8),(0,0xA5,0x5A),(False,True),(0,ACTOR,SOURCE-0x170),range(3)):
            resource,lifetime,channel = args
            memory = memory_case(pattern,padding)
            wanted = dict(memory)
            calls = [(screen.CONSTRUCTOR,packet_bytes(memory,resource,lifetime,padding),3,255,0,4,channel&255,context&0xFFFFFFFF)]
            if mutation:
                for address in (SOURCE,DEFAULT,DEFAULT+4,DEFAULT+8,FACTOR):
                    put(wanted,address,0x12345678)
            if result:
                calls.append((screen.COPY,result+0x170,SOURCE,4));put(wanted,result+0x170,SOURCE)
            traces = []
            for words in (self.raw,self.words,self.retail):
                model = SourcePacketOracle(words,memory,resource,lifetime,channel,context,phase,result,mutation).run()
                self.assertEqual(model.calls,calls)
                self.assertEqual(external(model.memory),external(wanted))
                self.assertEqual(model.r[2],result+0x170 if result else 0)
                traces.append([e for e in model.events if e[0]=='CALL' or not STACK-0x600<=e[1]<STACK+0x100])
                if words is self.retail:
                    coverage.update(model.visits)
            self.assertEqual(traces[0],traces[1]);self.assertEqual(traces[1],traces[2])
            cases += 1
        self.assertEqual(cases,3456)
        self.assertEqual(coverage,set(range(screen.ENTRY,screen.ENTRY+408,4)))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases,bodies=3,words=len(coverage),holes=list(HOLES)),indent=2)+'\n')

    def test_all_halfwords_and_channel_bytes_with_high_incoming_bits(self):
        memory = memory_case()
        for value in range(65536):
            model = SourcePacketOracle(self.words,memory,resource=0xABCD0000|value,lifetime=0xFEDC0000|value,
                channel=0x12340000|(value&255),context=0x80000000,phase=8*(value&1)).run()
            self.assertEqual(model.calls,[(screen.CONSTRUCTOR,packet_bytes(memory,value,value,0xA5),3,255,0,4,value&255,0x80000000),
                (screen.COPY,ACTOR+0x170,SOURCE,4)])
            wanted = dict(memory);put(wanted,ACTOR+0x170,SOURCE)
            self.assertEqual(external(model.memory),external(wanted))

    def test_single_precision_boundaries_and_raw_coordinate_default_transport(self):
        sizes = (0,0x80000000,1,0x007FFFFF,0x00800000,0x3F800001,0x7F7FFFFF,0xFF7FFFFF)
        transported = (0x7FA12345,0x7FC54321,0x7F800000,0xFF800000,0x80000000,1,0x7F7FFFFF,0)
        cases = 0
        for width,height,factor,phase in itertools.product(sizes,sizes,(0x3DCCCCCD,0,0xBF000000),(0,8)):
            memory = memory_case()
            put(memory,SOURCE+24,width);put(memory,SOURCE+28,height);put(memory,FACTOR,factor)
            for i in range(6):
                put(memory,SOURCE+i*4,transported[(sizes.index(width)+i)%8])
            for i in range(3):
                put(memory,DEFAULT+i*4,transported[(sizes.index(height)+i)%8])
            wanted = packet_bytes(memory,7,-53,0xA5)
            for words in (self.raw,self.words,self.retail):
                model = SourcePacketOracle(words,memory,7,-53,255,0,phase).run()
                self.assertEqual(model.calls[0],(screen.CONSTRUCTOR,wanted,3,255,0,4,255,0))
            cases += 1
        self.assertEqual(cases,384)

    def test_native_opaque_typed_layout_all_halfwords_and_full_storage(self):
        self.run_host(r'''
u32 value;int f,i;u8 before[32];ActorDescriptor1CBE20 p;
if(sizeof(source)!=32 || sizeof(p)!=124 || sizeof(void *)!=4 || (u8 *)&p.vector-(u8 *)&p!=16
   || (u8 *)&p.position-(u8 *)&p!=40 || (u8 *)&p.first-(u8 *)&p!=52 || (u8 *)&p.second-(u8 *)&p!=64
   || (u8 *)&p.flags-(u8 *)&p!=80 || (u8 *)&p.lifetime-(u8 *)&p!=84 || (u8 *)&p.resource-(u8 *)&p!=86
   || (u8 *)&p.field78-(u8 *)&p!=120) return 1;
for(value=0;value<65536;value++) for(f=0;f<2;f++) {
    for(i=0;i<8;i++) sourceWords[i]=word((f32)(i+1)*(value&1?-2:3));
    for(i=0;i<32;i++) ((u8 *)&source)[i]=((u8 *)sourceWords)[i];
    for(i=0;i<32;i++) before[i]=((u8 *)&source)[i];
    defaultWords[0]=word(3);defaultWords[1]=word(4);defaultWords[2]=word(12);
    D_800A5480.x=3;D_800A5480.y=4;D_800A5480.z=12;D_800A8CD4=number(0x3DCCCCCD);
    for(i=0;i<0x230;i++) storage.bytes[i]=0xA5;
    expectedResource=(u16)value;expectedLifetime=(s16)value;expectedChannel=value&255;
    expectedContext=value&1?(s32)0x80000000:0x7FFFFFFF;
    fail=f;mutation=value&1;calls=copies=error=0;
    func_1519EB8C(&source,expectedResource,expectedLifetime,expectedChannel,expectedContext);
    if(calls!=1 || copies!=!f || error) return 2;
    for(i=0;i<0x230;i++) {
        u8 expected=!f && i>=16+0x170 && i<16+0x174?((u8 *)&(Source1CBE20 *){&source})[i-16-0x170]:0xA5;
        if(storage.bytes[i]!=expected) return 3;
    }
    for(i=0;i<32;i++) {
        u8 expected=mutation && i<4?((u8 *)&(u32){0x12345678})[i]:before[i];
        if(((u8 *)&source)[i]!=expected) return 4;
    }
    if(word(D_800A5480.x)!=(mutation?0x12345678:defaultWords[0])
       || word(D_800A5480.y)!=(mutation?0x12345678:defaultWords[1])
       || word(D_800A5480.z)!=(mutation?0x12345678:defaultWords[2])
       || word(D_800A8CD4)!=(mutation?0x12345678:0x3DCCCCCD)) return 5;
}
return 0;
''')

    def test_native_actual_constructor_success_and_each_allocation_failure(self):
        harness = type('SourcePacketConstructorHarness',(constructor.GameExtendedChildConstructorTests,),{})
        harness.setUpClass()
        self.addCleanup(harness.doClassCleanups)
        original = self.fixture
        fixture = harness.fixture.replace('    if(inChild && length==28) {',r'''
    if(inChild && length==4) {
        push('E');extraCopies++;
        if(destination!=result+0x170 || *(void *const *)source!=expectedSource || copies!=1
           || tailCalls!=1 || removals || frees) error=12;
        for(i=0;i<4;i++) ((u8 *)destination)[i]=((const u8 *)source)[i];
        for(i=0;i<124;i++) capturedDescriptor.bytes[i]=descriptor[i];
        descriptor=capturedDescriptor.bytes;
        return destination;
    }
    if(inChild && length==28) {''')
        fixture = fixture.replace('void *memcpy(void *destination,', 'static void *expectedSource;\n'
            'static union {u32 alignment;u8 bytes[124];} capturedDescriptor;\nvoid *memcpy(void *destination,')
        fixture += '\n'+screen.LAYOUTS+'\nPosition1CBE20 D_800A5480;f32 D_800A8CD4;\n'+screen.SELECTED+'\n'
        self.fixture = fixture
        try:
            self.run_host(r'''
Source1CBE20 input;int phase,id,life,slot,i;u8 before[32];
for(phase=0;phase<4;phase++) for(id=0;id<3;id++) for(life=0;life<4;life++) for(slot=0;slot<4;slot++) {
    int index=id==0?0:id==1?7:232;
    reset(0x980,index);inChild=1;expectedSize=0x174;
    expectedSource=&input;expectedLength=13;expectedContext=-123;expectedSlot=slot*85;
    failRecord=phase==1;failNode=phase==2;failLoad=phase==3;
    input.position.x=100;input.position.y=-200;input.position.z=300;
    input.vector.x=4;input.vector.y=5;input.vector.z=6;input.width=100;input.height=-160;
    for(i=0;i<32;i++) before[i]=((u8 *)&input)[i];
    D_800A5480.x=3;D_800A5480.y=4;D_800A5480.z=12;D_800A8CD4=number(0x3DCCCCCD);
    func_1519EB8C(&input,(u16)index,(s16)(life==0?-32768:life==1?-1:life==2?0:32767),expectedSlot,-123);
    if(error || fences()) return 1;
    for(i=0;i<32;i++) if(((u8 *)&input)[i]!=before[i]) return 2;
    if(phase==0) {
        if(!trace_is("ANLSTCVVVVBE") || extraCopies!=1 || D_800DC63C!=1 || D_800DC468[index]!=1
           || *(void **)(result+0x170)!=&input || *(u32 *)(result+0x60)!=0x980
           || *(u16 *)(result+0x66)!=index || *(f32 *)(result+0x18)!=10
           || *(f32 *)(result+0x1C)!=-16 || *(f32 *)(result+0x140)!=13) return 3;
        *(void **)(result+0x170)=(void *)0xA5A5A5A5;
        if(check_result(0,&nodes[0],4)) return 4;
    } else if(extraCopies || copies || D_800DC63C || D_800DC468[index]
              || !trace_is(phase==1?"A":phase==2?"ANRF":"ANLRFF")) return 5;
}
return 0;
''')
        finally:
            self.fixture = original

    def test_stub_wrong_flags_size_payload_channel_and_padding_are_detected(self):
        negatives = [('stub','void func_1519EB8C(Source1CBE20 *s,u16 r,s16 l,u8 c,s32 x) {}'),
            ('flags',screen.SELECTED.replace('packet.flags = 0x980','packet.flags = 0')),
            ('size',screen.SELECTED.replace('NULL, 4, channel','NULL, 0, channel')),
            ('pointer',screen.SELECTED.replace('&savedSource, sizeof(savedSource)','savedSource, sizeof(savedSource)')),
            ('channel',screen.SELECTED.replace('4, channel, context','4, channel + 1, context')),
            ('padding',screen.SELECTED.replace('    packet.field78 = 0;','    packet.field78 = 0;\n    packet.pad69 = 0;'))]
        memory = memory_case()
        wanted = [(screen.CONSTRUCTOR,packet_bytes(memory,7,-53,0xA5),3,255,0,4,255,0),
                  (screen.COPY,ACTOR+0x170,SOURCE,4)]
        for name,body in negatives:
            _,words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            try:
                model = SourcePacketOracle(words,memory,resource=7,lifetime=-53,channel=255).run()
            except AssertionError:
                continue
            self.assertNotEqual(model.calls,wanted,name)

    def test_production_complete_slot_guard_count_and_retained_constructor(self):
        functions = load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        self.assertEqual(functions['func_1519EB8C'],self.retail)
        source = (self.root/'conker/src/game/generated_1CBE20.c').read_text()
        self.assertIn(screen.LAYOUTS.split('\n',1)[1],source)
        self.assertIn(screen.SELECTED,source)
        self.assertEqual(len(target_guards(self.root)),14)
        snapshot = json.loads((self.root/'conker/build/game-effect-configuration-packet-test/after.json').read_text())
        import hashlib
        for name in ('func_1513264C','func_151336A8','memcpy'):
            self.assertEqual(hashlib.sha256(struct.pack('>%dI'%len(functions[name]),*functions[name])).hexdigest(),
                             snapshot['slots'][name]['sha256'])
        first,address,_,_ = load_game_data_layout(self.root/'conker')
        rom = (self.root/'conker/conker.us.bin').read_bytes()
        self.assertEqual(struct.unpack_from('>I',rom,first+FACTOR-address)[0],0x3DCCCCCD)
