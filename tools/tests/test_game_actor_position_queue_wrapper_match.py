"""Signed argument homes, captured actor float bits and connected position queue."""

import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_actor_position_queue_wrapper_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_indexed_state_save_match import external, events
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

BASE, FLAG, COUNT, QUEUE = 0x800DBFF0, 0x800DDD1C, 0x8008CEB0, 0x800DDD28
ACTORS, ALTERNATE = 0x30000, 0x50000
INDICES = (0, 1, 3, -1, 255, 0x40000000, 0x80000000, 0x7FFFFFFF)
COORDINATES = ((0, 0, 0), (1, 2, 3), (0x7FFF, 0x8000, 0xFFFF),
               (0xFFFF8000, 0xFFFFFFFF, 0xFFFF7FFF), (0xABCD1234, 0xFEDC8001, 0x80008000),
               (0x80000000, 0x7FFFFFFF, 0x1234FFFF), (0x10000, 0x18000, 0x1FFFF),
               (0x76543210, 0x12345678, 0x87654321))
FLOATS = (0, 0x80000000, 0x3F800000, 0xBF800000, 0x3EAAAAAB, 0x7F800000, 0x7FC12345, 0x7F812345)
FLAGS = (0, 7, 8, 31, 127, 128, 248, 255)
COUNTS = (0, 1, 2, 3, 4, 255)


def field(index, base=ACTORS):
    return (base+index*0x9A0+0x380)&0xFFFFFFFF


def narrow(value):
    return (value&65535) | (0xFFFF0000 if value&32768 else 0)


def memory_case(index, value, flag, count=0, alias=None):
    memory = {STACK+i:0xA5 for i in range(-0x600,0x100)}
    memory.update({QUEUE+i:0xA5 for i in range(-16,64)})
    for address in (BASE, FLAG, COUNT, field(index), field(index,ALTERNATE),
                    (ACTORS+index*0x980+0x380)&0xFFFFFFFF, field(index)-4):
        memory.update({(address+i)&0xFFFFFFFF:0xA5 for i in range(4)})
    put(memory,BASE,ACTORS if alias is None else (alias-index*0x9A0-0x380)&0xFFFFFFFF)
    put(memory,FLAG,flag,1)
    put(memory,COUNT,count,1)
    put(memory,(ACTORS+index*0x980+0x380)&0xFFFFFFFF,0x40000000)
    put(memory,field(index)-4,0x3F000000)
    put(memory,field(index) if alias is None else alias,value)
    put(memory,field(index,ALTERNATE),0xC0000000)
    return memory


def mutations(index, mode, base=ACTORS):
    if mode == 1:
        return [(BASE,ALTERNATE,4),(FLAG,0x37,1),(field(index,base),0xC0000000,4)]
    if mode == 2:
        return [(COUNT,0xEE,1),(QUEUE,0xBEEF,2),(FLAG,0xFF,1),(field(index,base),0x3F000000,4)]
    return []


def reference(memory, arguments, mode=0, connected=False):
    memory,trace = dict(memory),[]
    def read(address,size):
        value = int.from_bytes(bytes(memory[(address+i)&0xFFFFFFFF] for i in range(size)),'big')
        trace.append(('R',address,size,value))
        return value
    def write(address,value,size):
        put(memory,address,value,size)
        trace.append(('W',address,size,value&((1<<(size*8))-1)))
    base = read(BASE,4)
    selector = read(FLAG,1)>>3
    duration = read(field(arguments[3],base),4)
    call = (screen.HELPER,*map(narrow,arguments[:3]),duration,*arguments[4:],selector)
    trace.append(('CALL',*call))
    if connected:
        count = read(COUNT,1)
        if count<3:
            entry = QUEUE+count*16
            for offset,value in zip((0,2,4),call[1:4]):
                write(entry+offset,value,2)
            write(entry+12,duration,4)
            write(COUNT,count+1,1)
            write(entry+8,arguments[4],2)
            write(entry+10,arguments[5],2)
            write(entry+6,selector,1)
        result = count
    else:
        for address,value,size in mutations(arguments[3],mode,base):
            write(address,value,size)
        result = (0,0xFFFFFFFF,0x81234567)[mode]
    return external(memory),trace,[call],result


class QueueOracle(TriangleOracle):
    def __init__(self,words,memory,arguments,phase=0,mode=0,helper=None):
        code = {screen.HELPER+i*4:word for i,word in enumerate(helper or [])}
        super().__init__(words,memory,entry=screen.ENTRY,arguments=arguments,phase=phase,connected=code)
        self.index,self.mode = arguments[3],mode
        self.base = int.from_bytes(bytes(memory[BASE+i] for i in range(4)),'big')

    def record_call(self,target):
        assert target == screen.HELPER
        call = (target,*self.arguments(7))
        self.calls.append(call)
        self.events.append(('CALL',*call))

    def hook(self,target):
        assert target == screen.HELPER
        for address,value,size in mutations(self.index,self.mode,self.base):
            self.put(address,value,size)
        for register in (1,2,3,*range(4,16),24,25):
            self.r[register] = 0xA5000000+register
        self.r[2] = (0,0xFFFFFFFF,0x81234567)[self.mode]
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameActorPositionQueueWrapperMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-actor-position-queue-wrapper-test'
        cls.output.mkdir(exist_ok=True)
        cls.record,cls.words = screen.compile_candidate(cls.root,cls.output,'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>37I',rom,screen.ROM))
        cls.helper = list(struct.unpack_from('>33I',rom,0x1AAA28))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        actor = re.search(r'struct struct108 \{.*?\n\};',
                          (cls.root / 'conker/include/structs.h').read_text(),re.S).group()
        source = (cls.root / 'conker/src/game/generated_1A89B0.c').read_text()
        record = re.search(r'typedef struct \{[^{}]*\} PositionQueueEntry;',source).group()
        helper = re.search(r'void func_1517D578\([^;{}]+\) \{.*?\n\}',source,re.S).group()
        cls.fixture = ('typedef unsigned char u8;typedef short s16;typedef unsigned short u16;'
                       'typedef int s32;typedef unsigned int u32;typedef float f32;\n'
                       'typedef struct struct150 struct150;typedef struct struct127 struct127;'
                       'typedef struct struct108 struct108;\n'+actor+'\n'+record+r'''
static struct108 actors[4],expectedActors[4];
static PositionQueueEntry expectedQueue[3];
PositionQueueEntry D_800DDD28[3];
struct108 *D_800DBFF0;
u8 D_800DDD1C,D_8008CEB0[1];
static int indexValue,mode,connected,calls,error;
static u32 expectedArguments[7];
static u32 word(f32 f) {union {u32 u;f32 f;} v;v.f=f;return v.u;}
static f32 number(u32 u) {union {u32 u;f32 f;} v;v.u=u;return v.f;}
'''+helper.replace('func_1517D578','queue_writer')+r'''
void func_1517D578(s16 x,s16 y,s16 z,f32 duration,s32 a,s32 b,u8 selector) {
    u32 values[7]={(u32)(s32)x,(u32)(s32)y,(u32)(s32)z,word(duration),(u32)a,(u32)b,selector};
    int i;
    calls++;
    for(i=0;i<7;i++) if(values[i]!=expectedArguments[i]) error=1;
    if(connected) {queue_writer(x,y,z,duration,a,b,selector);return;}
    if(mode==1) {D_800DBFF0=actors+1;D_800DDD1C=0x37;actors[indexValue].unk380=number(0xC0000000);}
    if(mode==2) {D_8008CEB0[0]=0xEE;D_800DDD28[0].unk0=(s16)0xBEEF;
        D_800DDD1C=0xFF;actors[indexValue].unk380=number(0x3F000000);}
}
'''+screen.SELECTED+'\n')

    def compare(self,memory,arguments,phase=0,mode=0,connected=False):
        wanted,trace,calls,result = reference(memory,arguments,mode,connected)
        coverage = set()
        for words in (self.retail,self.words):
            model = QueueOracle(words,memory,arguments,phase,mode,self.helper if connected else None).run()
            self.assertEqual(external(model.memory),wanted)
            self.assertEqual(events(model),trace)
            self.assertEqual(model.calls,calls)
            self.assertEqual(model.r[2],result)
            if words is self.retail:
                coverage.update(model.visits)
        return coverage

    def test_direct_body_and_thirty_two_compiler_controls(self):
        self.assertEqual(self.words,self.retail)
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences']),(37,0x28,0))
        expected = {'direct':((37,0x28,0),(36,0x28,35),(34,0x28,35)),
                    'coordinate-locals':((37,0x28,0),(36,0x28,35),(42,0x40,42)),
                    'wide-parameters':((34,0x28,35),(33,0x28,35),(34,0x28,35)),
                    'register-parameters':((37,0x28,0),(36,0x28,35),(34,0x28,35)),
                    'volatile-coordinates':((34,0x28,35),(34,0x28,35),(34,0x28,35)),
                    'volatile-index':((37,0x28,0),(37,0x28,28),(34,0x28,35)),
                    'byte-stride':((37,0x28,0),(36,0x28,35),(34,0x28,35)),
                    'cached-actor':((37,0x28,20),(36,0x28,36),(35,0x30,36))}
        for name,body in screen.candidates():
            for profile in screen.PROFILES:
                record,_ = screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                wanted = expected[name][0 if profile=='o2g3' else 1 if profile=='o2' else 2]
                self.assertEqual((record['body_words'],record['frame'],record['differences']),wanted,(name,profile))
                self.assertEqual(record['diagnostics'],'')

    def test_opaque_argument_homes_capture_mutations_and_full_traces(self):
        coverage,cases = set(),0
        for index,coordinates,value,flag,mode,phase in itertools.product(INDICES,COORDINATES,FLOATS,FLAGS,range(3),(0,8)):
            arguments = (*coordinates,index,0x87654321,0xFEDCBA98)
            coverage.update(self.compare(memory_case(index,value,flag),arguments,phase,mode))
            cases += 1
        self.assertEqual(cases,24576)
        self.assertEqual(coverage,set(range(screen.ENTRY,screen.ENTRY+148,4)))
        (self.output / 'opaque.json').write_text(json.dumps(dict(cases=cases,models=2,reachable_words=len(coverage)),indent=2)+'\n')

    def test_connected_queue_gate_order_raw_float_bits_and_aliases(self):
        coverage,cases = set(),0
        for index,coordinates,value,flag,count,phase in itertools.product(INDICES[:6],COORDINATES,FLOATS,FLAGS,COUNTS,(0,8)):
            arguments = (*coordinates,index,0xFFFF1234,0x8000ABCD)
            coverage.update(self.compare(memory_case(index,value,flag,count),arguments,phase,connected=True))
            cases += 1
        self.assertEqual(cases,36864)
        for byte,index,phase in itertools.product(range(256),(0,3),(0,8)):
            arguments = (*COORDINATES[byte%8],index,byte*0x1234567&0xFFFFFFFF,~byte&0xFFFFFFFF)
            coverage.update(self.compare(memory_case(index,FLOATS[byte%8],byte,byte),arguments,phase,connected=True))
            cases += 1
        for location,count,phase in itertools.product((QUEUE,QUEUE+12,QUEUE+16,QUEUE+28),COUNTS,(0,8)):
            arguments = (*COORDINATES[4],1,0x81234567,0xFEDCBA98)
            coverage.update(self.compare(memory_case(1,FLOATS[4],255,count,location),arguments,phase,connected=True))
            cases += 1
        self.assertEqual(cases,37936)
        self.assertEqual(coverage,set(range(screen.ENTRY,screen.ENTRY+148,4)) | set(range(screen.HELPER,screen.HELPER+132,4)))
        (self.output / 'connected.json').write_text(json.dumps(dict(cases=cases,models=2,
            wrapper_words=37,helper_words=33,all_count_and_flag_bytes=True),indent=2)+'\n')

    def run_native(self,connected):
        coordinates = ','.join('{'+','.join('0x%08X'%v for v in row)+'}' for row in COORDINATES)
        values = ','.join('0x%08X'%v for v in FLOATS)
        self.run_host('static u32 coordinates[][3]={'+coordinates+'};\nstatic u32 floats[]={'+values+'};\n'+
                      'connected=%d;\n'%connected+r'''
static u8 counts[]={0,1,2,3,4,255};
int n,c,f,k,q,i,countCases=0;
if(sizeof(struct108)!=0x9A0 || (u8 *)&actors[0].unk380-(u8 *)actors!=0x380 || sizeof(PositionQueueEntry)!=16) return 1;
for(n=0;n<4;n++) for(c=0;c<8;c++) for(f=0;f<8;f++) for(k=0;k<32;k++) for(q=0;q<(connected?6:1);q++) {
    u8 initialFlag=(u8)(k*8+c),initialCount=counts[q],expectedCount=initialCount,expectedFlag=initialFlag;
    struct108 *expectedBase=actors;
    PositionQueueEntry *entry;
    for(i=0;i<(int)sizeof(actors);i++) ((u8 *)actors)[i]=0xA5;
    for(i=0;i<(int)sizeof(D_800DDD28);i++) ((u8 *)D_800DDD28)[i]=0xA5;
    actors[n].unk380=number(floats[f]);
    for(i=0;i<(int)sizeof(actors);i++) ((u8 *)expectedActors)[i]=((u8 *)actors)[i];
    for(i=0;i<(int)sizeof(D_800DDD28);i++) ((u8 *)expectedQueue)[i]=((u8 *)D_800DDD28)[i];
    for(i=0;i<3;i++) expectedArguments[i]=(u32)(s32)(s16)(coordinates[c][i]&65535);
    expectedArguments[3]=floats[f];expectedArguments[4]=0x87654321;
    expectedArguments[5]=0xFEDCBA98;expectedArguments[6]=initialFlag>>3;
    mode=(n+c+f+k)%3;indexValue=n;calls=error=0;
    D_800DBFF0=actors;D_800DDD1C=initialFlag;D_8008CEB0[0]=initialCount;
    if(connected && initialCount<3) {
        entry=expectedQueue+initialCount;
        entry->unk0=(s16)expectedArguments[0];entry->unk2=(s16)expectedArguments[1];entry->unk4=(s16)expectedArguments[2];
        entry->unkC=number(floats[f]);expectedCount=initialCount+1;
        entry->unk8=(s16)0x4321;entry->unkA=(s16)0xBA98;entry->unk6=initialFlag>>3;
    }
    if(!connected && mode==1) {expectedBase=actors+1;expectedFlag=0x37;expectedActors[n].unk380=number(0xC0000000);}
    if(!connected && mode==2) {expectedCount=0xEE;expectedQueue[0].unk0=(s16)0xBEEF;
        expectedFlag=0xFF;expectedActors[n].unk380=number(0x3F000000);}
    func_1517D5FC((s16)coordinates[c][0],(s16)coordinates[c][1],(s16)coordinates[c][2],n,
                 (s32)0x87654321,(s32)0xFEDCBA98);
    if(error || calls!=1 || D_800DBFF0!=expectedBase || D_800DDD1C!=expectedFlag || D_8008CEB0[0]!=expectedCount) return 2;
    for(i=0;i<(int)sizeof(actors);i++) if(((u8 *)actors)[i]!=((u8 *)expectedActors)[i]) return 3;
    for(i=0;i<(int)sizeof(D_800DDD28);i++) if(((u8 *)D_800DDD28)[i]!=((u8 *)expectedQueue)[i]) return 4;
    countCases++;
}
if(countCases!=(connected?49152:8192)) return 5;
''')

    def test_native_opaque_actual_actor_layout_and_argument_capture(self):
        self.run_native(False)

    def test_native_connected_actual_writer_queue_and_full_actor_footprints(self):
        self.run_native(True)

    def test_stub_wrong_stride_field_selector_and_coordinate_are_detected(self):
        negatives = {'stub':'void func_1517D5FC(s16 a,s16 b,s16 c,s32 d,s32 e,s32 f) {}',
                     'stride':screen.SELECTED.replace('D_800DBFF0[arg3].unk380','*(f32 *)((u8 *)D_800DBFF0+arg3*0x980+0x380)'),
                     'field':screen.SELECTED.replace('.unk380','.unk37C'),
                     'selector':screen.SELECTED.replace('>> 3','>> 2'),
                     'coordinate':screen.SELECTED.replace('func_1517D578(arg0,','func_1517D578(arg0 + 1,')}
        arguments = (*COORDINATES[4],1,0x87654321,0xFEDCBA98)
        memory = memory_case(1,FLOATS[4],255)
        wanted,_,calls,_ = reference(memory,arguments)
        for name,body in negatives.items():
            _,words = screen.compile_candidate(self.root,self.output,'wrong-'+name,body)
            model = QueueOracle(words,memory,arguments).run()
            self.assertNotEqual(model.calls,calls,name)
            if name=='stub':
                self.assertEqual(external(model.memory),external(memory))

    def test_production_direct_wrapper_and_unchanged_complete_helper(self):
        linked,_,addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1517D5FC'],screen.ENTRY)
        self.assertEqual(linked['func_1517D5FC'],self.retail)
        self.assertEqual(linked['func_1517D578'],self.helper)
        self.assertIn(screen.SELECTED,(self.root / 'conker/src/game/generated_1A89B0.c').read_text())
        self.assertNotIn('func_1517D5FC',(self.root / 'conker/retail_word_patches.us.csv').read_text())


if __name__ == '__main__':
    unittest.main()
