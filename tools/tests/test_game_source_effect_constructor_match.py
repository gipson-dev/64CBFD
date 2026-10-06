"""Complete effect construction and real wrapper/constructor/consumer handoffs."""

import csv
import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_source_effect_constructor_candidates as screen
from tools.experiments import game_source_effect_packet_candidates as packet
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import signed
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

DESC, ACTOR, SOURCE = 0x22000, 0x21000, 0x20000
BOUND, DEFAULT = screen.SYMBOLS['D_80082FA0'], screen.SYMBOLS['D_800A5184']
ALLOC, COPY, ZERO, INIT, TABLE, VIEW, OWNER = (screen.SYMBOLS[n] for n in
    ('func_15167A68','memcpy','bzero','func_1513FFF4','func_151400D0','func_1515D480','func_1515D440'))
PLANS = ((-1,), (0,), (3,), (0,2,2,1), (3,0), (4,))


def word(memory, address):
    return int.from_bytes(bytes(memory[address+i] for i in range(4)), 'big')


def external(memory):
    return {a:v for a,v in memory.items() if not STACK-0x600 <= a < STACK+0x100}


def memory_case(flags=0, bound=0, padding=0xA5):
    memory = {STACK+i:padding for i in range(-0x600,0x100)}
    for base,length in ((DESC-16,120),(ACTOR-16,0x230),(SOURCE,64),(BOUND-16,36),(DEFAULT-16,36),(packet.TABLE-16,64)):
        memory.update({base+i:(i*17+13)&255 for i in range(length)})
    put(memory,DESC+0x40,flags);put(memory,BOUND,bound);put(memory,DEFAULT,0xC61C4000)
    for i,value in enumerate((0x3F800000,0xC0000000,0x40400000,0x40800000,0x40A00000,0x40C00000,0x42C80000,0xC3200000)):
        put(memory,SOURCE+i*4,value)
    return memory


def actions_for(mutation):
    if not mutation:
        return {}
    return {'allocate':((DESC,0xFE,1),(DESC+0x40,0xDEADBEEF,4)),
            'zero':((ACTOR+0x18,0xB2,1),(DEFAULT,0xBF800000,4)),
            'init':((DEFAULT,0xC0000000,4),),
            'table':((DEFAULT,0x3F000000,4),),
            'view':((ACTOR+0x9C,0xBAD,4),(DEFAULT,0xC0400000,4))}


def apply_actions(memory, actions, stage):
    for address,value,size in actions.get(stage,()):
        put(memory,address,value,size)


def reference(memory, arguments, fail=False, plan=(0,), actions=None, descriptor=DESC):
    actions = actions or {}
    result = dict(memory)
    _,table,kind,mode,first,setup,variant,resource,extra,payload,channel,context = arguments
    flags = word(result,descriptor+0x40)
    category = 0x56 if flags & 0x800000 else 0x49 if flags & 0x2000000 else 0x1C
    calls = [(ALLOC,category,context & 0xFFFFFFFF,(payload+0x110)&0xFFFFFFFF,1,channel & 255,2 if flags & 0x80000000 else 1)]
    apply_actions(result,actions,'allocate')
    if fail:
        return external(result),calls,0
    copied = bytes(result[descriptor+i] for i in range(88))
    calls.append((COPY,ACTOR+0x18,copied,88))
    for i,value in enumerate(copied):
        result[ACTOR+0x18+i] = value
    apply_actions(result,actions,'copy')
    for offset,value in ((0x70,kind),(0x71,mode),(0x72,first),(0x73,setup),(0x74,0)):
        put(result,ACTOR+offset,value,1)
    calls.append((ZERO,ACTOR+0x100,16))
    for i in range(16):
        result[ACTOR+0x100+i] = 0
    apply_actions(result,actions,'zero')
    calls.append((INIT,ACTOR+0xC0,result[ACTOR+0x18],variant & 255))
    put(result,ACTOR+0xC0,0x12345678)
    apply_actions(result,actions,'init')
    calls.append((TABLE,ACTOR+0xC0,table & 0xFFFFFFFF))
    put(result,ACTOR+0xC4,table)
    apply_actions(result,actions,'table')
    put(result,BOUND,plan[0])
    for offset,value in ((0x10,1),(0x14,0),(0x78,word(result,DEFAULT)),(0x98,0),(0x90,0),(0x9C,resource),(0xB8,extra)):
        put(result,ACTOR+offset,value)
    for offset in (0x94,0x95,0xA0):
        put(result,ACTOR+offset,0,1)
    for offset in range(0xA4,0xB8,4):
        put(result,ACTOR+offset,0)
    if resource & 0xFFFFFFFF:
        index = 0
        while index <= signed(word(result,BOUND)):
            assert index < 8
            calls.append((VIEW,resource & 0xFFFFFFFF))
            apply_actions(result,actions,'view')
            put(result,BOUND,plan[min(index+1,len(plan)-1)])
            put(result,ACTOR+0xA4+index*4,0x30000+index*16)
            index += 1
        calls.append((OWNER,))
        apply_actions(result,actions,'owner')
        put(result,ACTOR+0xB4,0x31000)
    return external(result),calls,ACTOR


class ConstructorOracle(TriangleOracle):
    def __init__(self,words,memory,arguments,fail=False,plan=(0,),actions=None,connected=None,entry=screen.ENTRY,phase=0):
        super().__init__(words,memory,entry=entry,arguments=arguments,connected=connected,phase=phase)
        self.fail,self.plan,self.actions = fail,plan,actions or {}
        self.view_calls,self.descriptor = 0,DESC

    def record_call(self,target):
        if target == screen.ENTRY:
            args = self.arguments(12);self.descriptor = args[0]
            call = (target,bytes(self.memory[args[0]+i] for i in range(88)),*args[1:])
        elif target == COPY:
            destination,source,size = self.r[4:7]
            if size == 88:
                assert source == self.descriptor and destination == ACTOR+0x18
            else:
                assert size == 4 and destination == ACTOR+0x110
            call = (target,destination,bytes(self.memory[source+i] for i in range(size)),size)
        elif target == ALLOC:
            call = (target,*self.arguments(6))
        elif target in (ZERO,INIT,TABLE):
            call = (target,*self.arguments(3 if target == INIT else 2))
        else:
            assert target in (VIEW,OWNER)
            call = (target,*self.arguments(1 if target == VIEW else 0))
        self.calls.append(call);self.events.append(('CALL',target,call[1:]))

    def hook(self,target):
        result = 0xFFFFFFFF
        if target == ALLOC:
            stage,result = 'allocate',0 if self.fail else ACTOR
        elif target == COPY:
            destination,source,size = self.r[4:7]
            for i in range(size):
                self.put(destination+i,self.get(source+i,1),1)
            stage,result = 'copy',destination
        elif target == ZERO:
            for i in range(self.r[5]):
                self.put(self.r[4]+i,0,1)
            stage = 'zero'
        elif target == INIT:
            self.put(self.r[4],0x12345678,4);stage = 'init'
        elif target == TABLE:
            self.put(self.r[4]+4,self.r[5],4);self.put(BOUND,self.plan[0],4);stage = 'table'
        elif target == VIEW:
            stage,result = 'view',0x30000+self.view_calls*16
            self.view_calls += 1
            self.put(BOUND,self.plan[min(self.view_calls,len(self.plan)-1)],4)
        else:
            assert target == OWNER
            stage,result = 'owner',0x31000
        for address,value,size in self.actions.get(stage,()):
            self.put(address,value,size)
        for register in (1,2,3,*range(4,16),24,25):
            self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]
        self.r[2] = result


def connected_wrapper_cases(test,wrapper,constructor):
    from tools.tests.test_game_source_effect_packet_match import packet_bytes
    connected = {screen.ENTRY+i*4:w for i,w in enumerate(constructor)}
    cases,coverage = 0,set()
    for mode,lifetime,channel,context,fail,plan in itertools.product((0,206,255),(-32768,-1,0,32767),
        (0,255),(0,0x80000000),(False,True),PLANS):
        memory = memory_case(bound=plan[0])
        expected_packet = packet_bytes(memory,mode,lifetime,0xA5)
        descriptor = STACK-88
        for i,value in enumerate(expected_packet):
            memory[descriptor+i] = value
        arguments = (descriptor,packet.TABLE,39,0,0,23,0,3,255,4,channel,context)
        wanted,calls,result = reference(memory,arguments,fail,plan,descriptor=descriptor)
        prefix = (screen.ENTRY,expected_packet,*arguments[1:])
        if result:
            payload = SOURCE.to_bytes(4,'big')
            calls.append((COPY,ACTOR+0x110,payload,4))
            for i,value in enumerate(payload):
                wanted[ACTOR+0x110+i] = value
        model = ConstructorOracle(wrapper,memory,(SOURCE,mode,lifetime,channel,context),fail,plan,
                                  connected=connected,entry=packet.ENTRY).run()
        test.assertEqual((external(model.memory),model.calls),(wanted,[prefix,*calls]))
        test.assertEqual(model.r[2],ACTOR+0x110 if result else 0)
        coverage.update(model.visits);cases += 1
    test.assertEqual(cases,576)
    constructor_coverage = set(range(screen.ENTRY,screen.ENTRY+456,4))
    constructor_coverage.difference_update(screen.ENTRY+i for i in (0x4C,0x50,0x60,0x64,0x70,0x74))
    test.assertEqual(coverage,set(range(packet.ENTRY,packet.ENTRY+384,4)) | constructor_coverage)


class GameSourceEffectConstructorMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-source-effect-constructor-test'
        cls.output.mkdir(exist_ok=True)
        cls.record,cls.words = screen.compile_candidate(cls.root,cls.output,'selected')
        cls.retail = list(struct.unpack_from('>114I',(cls.root/'conker/conker.us.bin').read_bytes(),screen.ROM))
        cls.production = load_elf_functions(str(cls.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        cls.directory = tempfile.TemporaryDirectory();cls.addClassCleanup(cls.directory.cleanup);cls.path = Path(cls.directory.name)
        consumer = re.search(r's32 func_1519EF04\([^;{}]+\) \{\n.*?\n\}',
            (cls.root/'conker/src/game/generated_1CBE20.c').read_text(),re.S).group(0)
        cls.fixture = native_fixture()+'\n'+screen.SELECTED+'\n'+packet.SELECTED+'\n'+consumer+'\n'

    def test_native_all_byte_pairs_failure_and_live_helper_footprint(self):
        self.run_host(r'''
int a,b,f;u32 flags;void *result;
if(sizeof(void *)!=4 || sizeof(Source1CBE20)!=32 || sizeof(SourceEffect1CBE20)!=88) return 1;
for(a=0;a<256;a++) for(b=0;b<256;b++) for(f=0;f<2;f++) {
    initialize(f,(a+b)&1,(a^b)%6);
    expectedKind=a;expectedMode=b;expectedFirst=(u8)(a+b);expectedSetup=(u8)(a-b);
    expectedVariant=(u8)(a^b);expectedChannel=(u8)(a*17+b);
    expectedResource=(a+b)%3==0?0:((a+b)%3==1?3:-1);
    expectedExtra=(s32)0x80000000+b;expectedContext=(s32)0x87654321;
    expectedPayload=(a&1)?4:-0x110;flags=0x045C0081 & ~0x82800000;
    flags|=(a&1)?0x800000:0;flags|=(a&2)?0x2000000:0;flags|=(a&4)?0x80000000:0;
    store(descriptor+0x40,flags);expectedFlags=flags;
    result=func_1513D2F0(descriptor,expectedTable,expectedKind,expectedMode,expectedFirst,
        expectedSetup,expectedVariant,expectedResource,expectedExtra,expectedPayload,expectedChannel,expectedContext);
    if(result!=(f?NULL:actor) || verify()) return 2;
}
''')

    def test_native_actual_wrapper_constructor_consumer_publication(self):
        self.run_host(r'''
static s16 lifetimes[]={-32768,-1,0,32767};
static s32 modes[]={0,206,255};int m,l,h,c,f,p,i;u8 beforeSource[32];
for(m=0;m<3;m++) for(l=0;l<4;l++) for(h=0;h<2;h++) for(c=0;c<2;c++) for(f=0;f<2;f++) for(p=0;p<6;p++) {
    initialize(f,0,p);connected=1;
    expectedKind=39;expectedMode=0;expectedFirst=0;expectedSetup=23;expectedVariant=0;
    expectedResource=3;expectedExtra=255;expectedPayload=4;expectedChannel=h?255:0;
    expectedContext=c?(s32)0x80000000:0;expectedFlags=0x045C0081;
    expectedTable=(s32)&D_800A4AA0;
    source.position.x=1.25f;source.position.y=-2.5f;source.position.z=4;
    source.vector.x=6;source.vector.y=-8;source.vector.z=12;source.width=100;source.height=-160;
    copy_bytes(beforeSource,(u8 *)&source,32);
    func_1519ED84(&source,modes[m],lifetimes[l],expectedChannel,expectedContext);
    if(verify()) return 3;
    for(i=0;i<32;i++) if(beforeSource[i]!=((u8 *)&source)[i]) return 4;
    if(!f) {
        SourceEffect1CBE20 *snapshot=(SourceEffect1CBE20 *)copied;
        if(snapshot->mode!=(u8)modes[m] || snapshot->field01 || snapshot->field02!=0x3B03
           || snapshot->lifetime!=lifetimes[l] || snapshot->flags!=0x045C0081
           || snapshot->width!=1000 || snapshot->height!=-1600
           || snapshot->position.x!=1.25f || snapshot->position.y!=-2.5f || snapshot->position.z!=4
           || snapshot->vector.x!=6 || snapshot->vector.y!=-8 || snapshot->vector.z!=12) return 5;
        source.position.x=-3;source.position.y=4;source.position.z=5;
        source.vector.x=6;source.vector.y=7;source.vector.z=8;source.width=9;source.height=-10;
        copy_bytes(beforeSource,(u8 *)&source,32);
        store(expected+16+0x2C,bits(90));store(expected+16+0x30,bits(-100));
        copy_bytes(expected+16+0x34,(u8 *)&source,12);
        copy_bytes(expected+16+0x40,(u8 *)&source+12,12);
        if(func_1519EF04(actor)!=1) return 6;
        for(i=0;i<0x230;i++) if(storage.bytes[i]!=expected[i]) return 7;
        for(i=0;i<32;i++) if(beforeSource[i]!=((u8 *)&source)[i]) return 8;
    }
}
''')

    def test_direct_body_and_ninety_seven_compiler_controls(self):
        self.assertEqual(self.words,self.retail)
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],self.record['diagnostics']),(114,56,0,''))
        common = ((113,56,81),(113,56,106),(150,56,149),(150,56,149))
        expected = {'field-order':common,'direct-schedule':((114,56,0),(114,56,33),(152,56,151),(152,56,151)),
            'narrow-category':((114,56,43),(114,56,67),(150,48,150),(150,48,150)),
            'wide-allocation-mode':common,'separate-mode':common,'typed-actor':common,
            'bit-allocation-mode':((114,56,23),(114,56,56),(152,56,151),(152,56,151)),
            'typed-bit-mode':((114,56,23),(114,56,56),(152,56,151),(152,56,151)),
            'typed-narrow-category':((114,56,43),(114,56,67),(150,48,150),(150,48,150)),
            'split-category':((112,56,93),(112,56,111),(148,56,147),(148,56,147)),
            'explicit-cursor':((113,56,81),(113,56,106),(153,56,152),(153,56,152)),
            'do-clear':((113,56,83),(113,56,108),(152,56,151),(152,56,151)),
            'direct-flags':((114,56,35),(114,56,48),(152,56,151),(152,56,151)),
            'unit-first':common,'resource-first':common,
            'default-first':((113,56,84),(113,56,109),(150,56,149),(150,56,149)),
            'byte-order':((114,56,20),(114,56,53),(152,56,151),(152,56,151)),
            'captured-default':((114,56,8),(114,56,41),(154,56,153),(154,56,153)),
            'combined-schedule':((114,56,5),(114,56,38),(154,56,153),(154,56,153)),
            'typed-combined':((114,56,5),(114,56,38),(154,56,153),(154,56,153)),
            'bound-pointer':((114,56,34),(114,56,64),(157,64,157),(157,64,157)),
            'register-bound':((114,56,34),(114,56,64),(157,72,157),(157,72,157))}
        count = 0
        for name,body in [*screen.candidates(),*screen.scheduling_candidates()]:
            for index,profile in enumerate(screen.PROFILES):
                record,_ = screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                self.assertEqual((record['body_words'],record['frame'],record['differences']),expected[name][index],(name,profile))
                self.assertEqual(record['diagnostics'],'');count += 1
        for (name,body),difference in zip(screen.default_candidates(),(7,4,7,8,9,10,2,5,0)):
            record,_ = screen.compile_candidate(self.root,self.output,name,body)
            self.assertEqual((record['body_words'],record['frame'],record['differences'],record['diagnostics']),(114,56,difference,''),name)
            count += 1
        self.assertEqual(count,97)

    def test_full_guest_contract_flags_failure_live_callbacks_and_all_words(self):
        cases,coverage = 0,set()
        for flag_bits,fail,context,phase,plan,resource,mutation,padding in itertools.product(range(8),(False,True),
            (0,0x80000000),(0,8),PLANS,(0,3,0xFFFFFFFF),(False,True),(0,0xA5,0x5A)):
            flags = 0x45C0081 & ~0x82800000
            flags |= (0x800000 if flag_bits & 1 else 0) | (0x2000000 if flag_bits & 2 else 0) | (0x80000000 if flag_bits & 4 else 0)
            memory = memory_case(flags,plan[0],padding)
            arguments = (DESC,packet.TABLE,0xABCD0027,0xFEDC0080,0x123400FF,0x76540117,0xFFFF0100,resource,0x80000000,4,0xABCDEFEE,context)
            wanted = reference(memory,arguments,fail,plan,actions_for(mutation))
            traces = []
            for words in (self.words,self.retail):
                model = ConstructorOracle(words,memory,arguments,fail,plan,actions_for(mutation),phase=phase)
                model.run()
                self.assertEqual((external(model.memory),model.calls,model.r[2]),wanted)
                traces.append([e for e in model.events if e[0]=='CALL' or not STACK-0x600<=e[1]<STACK+0x100])
                if words is self.retail:
                    coverage.update(model.visits)
            self.assertEqual(traces[0],traces[1]);cases += 1
        self.assertEqual(cases,6912)
        self.assertEqual(coverage,set(range(screen.ENTRY,screen.ENTRY+456,4)))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases,bodies=2,words=len(coverage),plans=PLANS),indent=2)+'\n')

    def test_every_byte_width_and_safe_payload_context_boundaries(self):
        cases = 0
        for byte,payload,phase in itertools.product(range(256),(0,4,-0x110,0x7FFFFEEF),(0,8)):
            memory = memory_case(0x82800000,3)
            args = (DESC,0xFFFFFFFF,0xABCD0000|byte,0xFEDC0000|byte,0x12340000|byte,0x56780000|byte,
                    0x9ABC0000|byte,-1,0xFFFFFFFF,payload,0xFFFF0000|byte,0x80000000)
            wanted = reference(memory,args,plan=(3,))
            model = ConstructorOracle(self.words,memory,args,plan=(3,),phase=phase)
            model.run();self.assertEqual((external(model.memory),model.calls,model.r[2]),wanted);cases += 1
        self.assertEqual(cases,2048)

    def test_default_float_raw_transport_after_helpers_before_view_mutation(self):
        patterns = (0xC61C4000,0,0x80000000,1,0x7F7FFFFF,0x7F800000,0xFF800000,0x7FC12345,0x7FA12345)
        for pattern,resource in itertools.product(patterns,(0,3)):
            memory = memory_case(bound=0)
            args = (DESC,packet.TABLE,39,0,0,23,0,resource,255,4,0,1)
            actions = {'table':((DEFAULT,pattern,4),),'view':((DEFAULT,0x12345678,4),)}
            wanted = reference(memory,args,plan=(0,),actions=actions)
            for words in (self.words,self.retail):
                model = ConstructorOracle(words,memory,args,plan=(0,),actions=actions).run()
                self.assertEqual((external(model.memory),model.calls,model.r[2]),wanted)
                self.assertEqual(word(model.memory,ACTOR+0x78),pattern)

    def test_actual_wrapper_constructor_guest_handoff(self):
        connected_wrapper_cases(self,self.production['func_1519ED84'],self.words)

    def test_compiled_negatives_detect_stub_wrong_category_live_bound_and_copy(self):
        negatives = [('stub','void *func_1513D2F0(void *d,s32 t,u8 k,u8 m,u8 a,u8 b,u8 c,s32 r,s32 e,s32 p,u8 h,s32 x) {return NULL;}'),
            ('category',screen.SELECTED.replace('category = 0x56','category = 0x49')),
            ('copy',screen.SELECTED.replace('descriptor, 0x58','descriptor, 0x54')),
            ('default',screen.SELECTED.replace('    *(f32 *)(result + 0x78) = D_800A5184;',
                '    *(f32 *)(result + 0x78) = 0.0f;')),
            ('clamp',screen.SELECTED.replace('i <= D_80082FA0','i < 4 && i <= D_80082FA0')),
            ('captured-bound',screen.SELECTED.replace('    s32 i;', '    s32 i;\n    s32 bound;').replace(
                '    if (resource != 0) {', '    bound = D_80082FA0;\n    if (resource != 0) {').replace('i <= D_80082FA0','i <= bound'))]
        memory = memory_case(0x82800000,bound=4)
        args = (DESC,packet.TABLE,39,0,0,23,0,3,255,4,255,1)
        for name,body in negatives:
            _,words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            plan = (0,2,2,1) if name == 'captured-bound' else (4,)
            wanted = reference(memory,args,plan=plan)
            try:
                model = ConstructorOracle(words,memory,args,plan=plan).run()
            except (AssertionError,KeyError):
                continue
            self.assertNotEqual((external(model.memory),model.calls,model.r[2]),wanted,name)

    def test_installed_direct_slot_body_no_guards_and_default_anchor(self):
        self.assertEqual(self.production['func_1513D2F0'],self.retail)
        self.assertIn(screen.SELECTED,(self.root/'conker/src/game_169510.c').read_text())
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(len(rows),10660)
        self.assertFalse([r for r in rows if r['function']=='func_1513D2F0'])


def native_fixture():
    return '''typedef unsigned char u8;typedef short s16;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;typedef float f32;
#define NULL ((void *)0)
'''+packet.LAYOUTS+'\n'+r'''
s32 D_80082FA0,D_800A4AA0;f32 D_800A5184;
static union {u32 alignment;u8 bytes[0x230];} storage,description;
static u8 *actor=storage.bytes+16,*descriptor=description.bytes+16;
static u8 expected[0x230],copied[88],descriptorBefore[0x230];
static Source1CBE20 source;
static u32 expectedFlags;static s32 expectedTable,expectedResource,expectedExtra,expectedPayload,expectedContext;
static u8 expectedKind,expectedMode,expectedFirst,expectedSetup,expectedVariant,expectedChannel;
static int fail,mutation,plan,connected,error,stage,views,published;
static int bounds[6][4]={{-1,-1,-1,-1},{0,0,0,0},{3,3,3,3},{0,2,2,1},{3,0,0,0},{4,4,4,4}};
static u8 handles[128],ownerHandle;
static u32 bits(f32 value) {union {f32 f;u32 u;} v;v.f=value;return v.u;}
static void store(u8 *address,u32 value) {u8 *p=(u8 *)&value;int i;for(i=0;i<4;i++) address[i]=p[i];}
static void copy_bytes(u8 *out,const u8 *in,int length) {int i;for(i=0;i<length;i++) out[i]=in[i];}
void *func_15167A68(s32 category,s32 context,s32 size,s32 one,u8 channel,u8 mode) {
    s32 wanted=expectedFlags&0x800000?0x56:expectedFlags&0x2000000?0x49:0x1C;
    if(stage++ || category!=wanted || context!=expectedContext || size!=expectedPayload+0x110
       || one!=1 || channel!=expectedChannel || mode!=(expectedFlags&0x80000000?2:1)) error=1;
    if(mutation) {descriptor[0]=0xFE;store(descriptor+0x40,0xDEADBEEF);}
    return fail?NULL:actor;
}
void *memcpy(void *out,const void *in,u32 length) {
    if(length==88) {
        if(stage++!=1 || out!=actor+0x18 || (!connected && in!=descriptor)) error=2;
        copy_bytes(copied,in,88);
    } else {
        if(!connected || fail || length!=4 || out!=actor+0x110 || *(Source1CBE20 *const *)in!=&source
           || stage!=5+(expectedResource!=0) || published++) error=3;
    }
    copy_bytes(out,in,length);return out;
}
void bzero(void *out,u32 length) {
    u32 i;
    if(stage++!=2 || out!=actor+0x100 || length!=16 || actor[0x70]!=expectedKind
       || actor[0x71]!=expectedMode || actor[0x72]!=expectedFirst || actor[0x73]!=expectedSetup || actor[0x74]) error=4;
    for(i=0;i<length;i++) ((u8 *)out)[i]=0;
    if(mutation) {actor[0x18]=0xB2;D_800A5184=-1;}
}
void func_1513FFF4(u8 *helper,u8 index,u8 variant) {
    int i;
    if(stage++!=3 || helper!=actor+0xC0 || index!=(mutation?0xB2:copied[0]) || variant!=expectedVariant) error=5;
    for(i=0;i<16;i++) if(actor[0x100+i]) error=6;
    store(helper,0x12345678);if(mutation) D_800A5184=-2;
}
void func_151400D0(u8 *helper,u8 *table) {
    if(stage++!=4 || helper!=actor+0xC0 || table!=(u8 *)expectedTable) error=7;
    store(helper+4,(u32)table);D_80082FA0=bounds[plan][0];
    if(mutation) D_800A5184=0.5f;
}
u8 *func_1515D480(s32 resource) {
    u8 *result=handles+views*16;
    if(stage!=5 || resource!=expectedResource || views>=5) error=8;
    if(mutation) {store(actor+0x9C,0xBAD);D_800A5184=-3;}
    views++;D_80082FA0=bounds[plan][views<4?views:3];return result;
}
u8 *func_1515D440(void) {
    if(stage++!=5 || expectedResource==0) error=9;
    return &ownerHandle;
}
static void initialize(int failure,int mutate,int boundPlan) {
    int i;
    fail=failure;mutation=mutate;plan=boundPlan;connected=error=stage=views=published=0;
    for(i=0;i<0x230;i++) {storage.bytes[i]=(u8)(i*17+13);description.bytes[i]=(u8)(i*31+7);}
    copy_bytes(expected,storage.bytes,0x230);copy_bytes(descriptorBefore,description.bytes,0x230);
    D_80082FA0=99;D_800A5184=-10000;D_800A4AA0=(s32)0xFEDCBA98;expectedTable=(s32)0xFEDCBA98;
}
static int verify(void) {
    int i,n=0,bound;u8 *e=expected+16;
    if(error || stage!=(fail?1:5+(expectedResource!=0))) return 1;
    if(!connected) {
        store(descriptorBefore+16+0x40,expectedFlags);
        if(mutation) {descriptorBefore[16]=0xFE;store(descriptorBefore+16+0x40,0xDEADBEEF);}
        for(i=0;i<0x230;i++) if(description.bytes[i]!=descriptorBefore[i]) return 2;
    }
    if(!fail) {
        copy_bytes(e+0x18,copied,88);if(mutation) e[0x18]=0xB2;
        e[0x70]=expectedKind;e[0x71]=expectedMode;e[0x72]=expectedFirst;e[0x73]=expectedSetup;e[0x74]=0;
        for(i=0;i<16;i++) e[0x100+i]=0;
        store(e+0xC0,0x12345678);store(e+0xC4,(u32)expectedTable);
        store(e+0x10,1);store(e+0x14,0);store(e+0x78,bits(mutation?0.5f:-10000));
        store(e+0x98,0);e[0x95]=e[0x94]=0;store(e+0x90,0);store(e+0x9C,(u32)expectedResource);
        store(e+0xB8,(u32)expectedExtra);e[0xA0]=0;
        for(i=0;i<5;i++) store(e+0xA4+i*4,0);
        bound=bounds[plan][0];
        if(expectedResource!=0) {
            while(n<=bound) {store(e+0xA4+n*4,(u32)(handles+n*16));n++;bound=bounds[plan][n<4?n:3];}
            store(e+0xB4,(u32)&ownerHandle);
            if(mutation && n) store(e+0x9C,0xBAD);
        }
        if(views!=n || D_80082FA0!=bound || bits(D_800A5184)!=bits(mutation?(n?-3:0.5f):-10000)) return 3;
        if(connected) {if(published!=1) return 4;store(e+0x110,(u32)&source);}
    } else if(views || published || D_80082FA0!=99 || D_800A5184!=-10000) return 5;
    for(i=0;i<0x230;i++) if(storage.bytes[i]!=expected[i]) return 6;
    return D_800A4AA0!=(s32)0xFEDCBA98;
}
'''
