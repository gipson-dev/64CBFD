"""Cached quad full footprints, escaped cursor, and the actual matrix callee."""

import itertools
import csv
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_cached_quad_builder_candidates as screen
from tools.experiments.game_actor_triangle_transform_candidates import MATRIX_BODY
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests import test_game_random_curve_record as native
from tools.match_progress import load_elf_functions

ACTOR, BUFFER, ALTERNATE = 0x20000, 0x21000, 0x22000
BACKEND, COPY, ORIENT, MATRIX = (screen.SYMBOLS[n] for n in
    ('func_151D5D60', 'memcpy', 'func_150A8050', 'func_150A7960'))
WIDTHS = (0.0, -0.0, 1.25, -2.75, 32767.75, 65536.5)
HEIGHTS = (-1.5, 0.0, 2.5)


def half(value):
    value &= 65535
    return value-65536 if value&32768 else value


def external(memory):
    return {a:v for a,v in memory.items() if not STACK-0x600 <= a < STACK+0x100}


def matrix_values(pattern):
    value = [0.0]*16
    value[15] = 1.0
    for index, number in zip((0,1,2,4,5,6,8,9,10),
            ((1,0,0,0,1,0,0,0,1), (-1,0.5,1,2,0,-1,0,0,1),
             (0.25,2,-0.5,-3,1.5,0.75,2,-1,0.5))[pattern]):
        value[index] = float(number)
    return value


def memory_case(view, width, height):
    memory = {STACK+i:0xA5 for i in range(-0x600,0x100)}
    for base, size in ((ACTOR,0x180),(BUFFER,160),(ALTERNATE,160)):
        memory.update({base+i:(i*17+13)&255 for i in range(size)})
    for offset, value in zip((0x2C,0x30,0x34,0x38,0x3C,0x40,0x44,0x48),
            (width,height,10.5,-12.25,3.75,0.25,-0.5,1.0)):
        put(memory,ACTOR+offset,bits(value))
    put(memory,ACTOR+0x100+half(view)*4,BUFFER)
    return memory


def reference(memory, view, fresh, success, pattern, mutation, redirect):
    result = dict(memory)
    if not success:
        return result, 0
    first = BUFFER+0x40
    if fresh:
        for i in range(64):
            result[BUFFER+i] = result[ACTOR+0xC0+i]
        second = ALTERNATE if mutation else BUFFER
        if mutation:
            put(result,ACTOR+0x100+half(view)*4,ALTERNATE)
            put(result,ACTOR+0x2C,bits(-4.75))
        for i in range(64):
            result[second+64+i] = result[ACTOR+0xC0+i]
    width = floating(int.from_bytes(bytes(result[ACTOR+0x2C+i] for i in range(4)),'big'))
    height = floating(int.from_bytes(bytes(result[ACTOR+0x30+i] for i in range(4)),'big'))
    values = matrix_values(pattern)
    if mutation:
        put(result,ACTOR+0x34,bits(-7.5))
    values[12:15] = [floating(int.from_bytes(bytes(result[ACTOR+offset+i] for i in range(4)),'big'))
        for offset in (0x34,0x38,0x3C)]
    cursor = first
    for index, (x,y) in enumerate(((width,height),(-width,height),(-width,-height),(width,-height))):
        if redirect:
            cursor = ALTERNATE+index*16
        for axis in range(3):
            left = floating(bits(floating(bits(values[axis]*x))+floating(bits(values[axis+4]*y))))
            right = floating(bits(floating(bits(values[axis+8]*0.0))+values[axis+12]))
            coordinate = floating(bits(left+right))
            put(result,cursor+axis*2,int(coordinate),2)
        put(result,cursor+6,0,2)
        cursor += 16
    return result, first


class QuadOracle(TriangleOracle):
    def execute(self, word):
        if word>>26==17 and word>>21&31==16 and word&63==7:
            self.f[word>>6&31] = self.f[word>>11&31]^0x80000000
        else:
            super().execute(word)

    def __init__(self, words, memory, view, fresh, success, pattern, mutation, redirect, phase=0, connected=None):
        super().__init__(words,memory,entry=screen.ENTRY,arguments=(ACTOR,view),phase=phase,connected=connected)
        self.view, self.fresh, self.success = half(view),fresh,success
        self.pattern, self.mutation, self.redirect = pattern,mutation,redirect
        self.copies, self.matrix_calls = 0,0

    def record_call(self,target):
        args = self.arguments(7 if target==MATRIX else 5 if target==BACKEND else 4 if target==ORIENT else 3)
        if target==BACKEND:
            self.cursor_slot, self.fresh_slot = args[3:5]
            assert args[:3] == (ACTOR+0x100,self.view&0xFFFFFFFF,64), 'backend contract'
            self.calls.append((target,*args[:3],'cursor','fresh'))
        elif target==ORIENT:
            self.calls.append((target,'matrix',*args[1:]))
        elif target==MATRIX:
            self.calls.append((target,'matrix',*args[1:4],('point',self.matrix_calls)))
            assert args[5]==args[4]+4 and args[6]==args[4]+8
            if self.redirect:
                self.put(self.cursor_slot,ALTERNATE+self.matrix_calls*16,4)
            self.matrix_calls += 1
        else:
            assert target==COPY
            self.calls.append((target,*args))

    def hook(self,target):
        if target==BACKEND:
            self.put(self.cursor_slot,BUFFER+0x40 if self.success else 0,4)
            self.put(self.fresh_slot,self.fresh,1)
        elif target==COPY:
            destination, source, size = self.arguments(3)
            assert source==ACTOR+0xC0 and size==64
            for i in range(size):
                self.put(destination+i,self.get(source+i,1),1)
            self.copies += 1
            if self.mutation and self.copies==1:
                self.put(ACTOR+0x100+self.view*4,ALTERNATE,4)
                self.put(ACTOR+0x2C,bits(-4.75),4)
        elif target==ORIENT:
            matrix = self.r[4]
            for i,value in enumerate(matrix_values(self.pattern)):
                self.put(matrix+i*4,bits(value),4)
            if self.mutation:
                self.put(ACTOR+0x34,bits(-7.5),4)
        else:
            assert target==MATRIX
            super().hook(target)
            return
        for register in (1,2,3,*range(4,16),24,25):
            self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameCachedQuadBuilderMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-cached-quad-builder-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root,cls.output,'selected')
        rom = (cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>134I',rom,screen.ROM))
        cls.matrix = list(struct.unpack_from('>40I',rom,0xD4E10))
        cls.connected = {MATRIX+i*4:w for i,w in enumerate(cls.matrix)}
        cls.directory = tempfile.TemporaryDirectory();cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def test_compiler_shape_and_five_independent_scheduling_words(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],self.record['diagnostics']),
                         (134,0xD0,5,''))
        self.assertEqual(self.words[:45],self.retail[:45])
        self.assertEqual(self.words[50:],self.retail[50:])
        self.assertCountEqual(self.words[45:50],self.retail[45:50])
        self.assertEqual(self.words[45:50],[0x02402025,0xE7B40060,0xC624002C,0xE7A40058,0xC6260030])

    def test_production_complete_slot_source_and_only_five_schedule_guards(self):
        owner = (self.root/'conker/src/game_169510.c').read_text()
        self.assertIn(screen.SELECTED,owner)
        self.assertIn('Vtx *func_15140190(u8 *actor, s16 view);',owner)
        production = load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        self.assertEqual(production['func_15140190'],self.retail)
        self.assertEqual(production['func_150A7960'],self.matrix)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        guards = [r for r in rows if r['function']=='func_15140190']
        self.assertEqual((len(rows),len(guards)),(10760,5))
        normalized = list(self.words)
        for index,guard in enumerate(guards,45):
            self.assertEqual(guard['filename'],'game_169510')
            self.assertEqual(int(guard['offset'],16),index*4)
            self.assertEqual(int(guard['expected'],16),self.words[index])
            self.assertEqual(int(guard['replacement'],16),self.retail[index])
            self.assertEqual((guard['expected_relocations'],guard['replacement_relocations'],guard['omit']),('-','-','false'))
            self.assertEqual((guard['insert_after'],guard['insert_after_relocations']),('',''))
            normalized[index] = int(guard['replacement'],16)
        self.assertEqual(normalized,self.retail)

    def test_guest_actual_matrix_live_slot_copy_mutations_and_full_footprints(self):
        count, coverage = 0,set()
        for view,fresh,success,pattern,mutation,redirect,phase in itertools.product(
                (0,1,3,0x8000,0xFFFF,0x12340002),(0,1,255),(False,True),range(3),(False,True),(False,True),(0,8)):
            memory = memory_case(view,WIDTHS[count%len(WIDTHS)],HEIGHTS[count%len(HEIGHTS)])
            wanted, result = reference(memory,view,fresh,success,pattern,mutation,redirect)
            models = [QuadOracle(body,memory,view,fresh,success,pattern,mutation,redirect,phase,
                                 self.connected).run() for body in (self.words,self.retail)]
            for model in models:
                self.assertEqual(external(model.memory),external(wanted),(count,view))
                self.assertEqual(model.r[2],result)
                self.assertEqual((model.copies,model.matrix_calls),
                    (2 if success and fresh else 0,4 if success else 0))
                coverage.update(model.visits)
            self.assertEqual(models[0].calls,models[1].calls)
            self.assertEqual([e for e in models[0].events if not STACK-0x600<=e[1]<STACK+0x100],
                             [e for e in models[1].events if not STACK-0x600<=e[1]<STACK+0x100])
            count += 1
        self.assertEqual((count,len(coverage)),(864,174))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=count,bodies=2,covered_words=len(coverage)),indent=2)+'\n')

    def test_six_compiled_negative_controls_change_real_output(self):
        negatives = [('stub','Vtx *func_15140190(u8 *actor, s16 view) { return NULL; }'),
            ('lost-flags',screen.SELECTED.replace('        cursor->v.flag = 0;','')),
            ('three-corners',screen.SELECTED.replace('i < 4','i < 3')),
            ('wrong-size',screen.SELECTED.replace('view, 0x40,','view, 0x20,')),
            ('wrong-translation',screen.SELECTED.replace('matrix[3][1] = *(f32 *)(actor + 0x38);','matrix[3][1] = 0.0f;')),
            ('wrong-axis',screen.SELECTED.replace('cursor->v.ob[2] = (s32)point[2];','cursor->v.ob[2] = (s32)point[1];'))]
        memory = memory_case(0,1.25,2.5)
        wanted,result = reference(memory,0,0,True,1,False,False)
        for name,body in negatives:
            _,words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            try:
                model = QuadOracle(words,memory,0,0,True,1,False,False,connected=self.connected).run()
            except AssertionError as error:
                self.assertEqual(name,'wrong-size')
                self.assertEqual(str(error),'backend contract')
            else:
                self.assertTrue(model.r[2]!=result or external(model.memory)!=external(wanted),name)

    def test_twenty_four_compiler_controls(self):
        expected = {'selected':((134,208,5),(134,208,35),(160,168,160),(160,168,160)),
            'z-after-colors':((134,208,8),(134,208,38),(160,168,160),(160,168,160)),
            'named-point':((134,208,22),(134,208,36),(160,168,160),(160,168,160)),
            'outer-success':((130,208,97),(130,208,112),(156,168,156),(156,168,156)),
            'early-null':((132,208,108),(132,208,122),(158,168,158),(158,168,158)),
            'wide-counter':((132,216,130),(132,216,131),(159,176,159),(159,176,159))}
        count = 0
        for name,body in screen.candidates():
            for index,profile in enumerate(screen.PROFILES):
                record,_ = screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                self.assertEqual((record['body_words'],record['frame'],record['differences']),expected[name][index])
                self.assertEqual(record['diagnostics'],'');count += 1
        self.assertEqual(count,24)

    def test_native_caller_full_storage_and_all_signed_view_failures(self):
        self.fixture = '''typedef unsigned char u8;typedef short s16;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;typedef float f32;
typedef struct {struct {s16 ob[3];u16 flag;s16 tc[2];u8 cn[4];} v;} Vtx;
#define NULL ((void *)0)
'''+screen.DECLARATIONS+'''void *memcpy(void *,const void *,u32);
'''+screen.SELECTED+'\n'+MATRIX_BODY.replace('func_150A7960','semantic_matrix')+r'''
static union {u32 alignment;u8 bytes[0x180];} a;
static union {u32 alignment;u8 bytes[160];} b,c;
static u8 wantedA[0x180],wantedB[160],wantedC[160];
static int fresh,success,pattern,mutation,redirect,backend,copies,orients,matrices,error;
static s16 expectedView;
static Vtx **cursorSlot;
static f32 expectedWidth,expectedHeight;
static f32 widths[]={0,-0.0f,1.25f,-2.75f,32767.75f,65536.5f};
static f32 linear[3][9]={{1,0,0,0,1,0,0,0,1},{-1,0.5f,1,2,0,-1,0,0,1},{0.25f,2,-0.5f,-3,1.5f,0.75f,2,-1,0.5f}};
static void fill_matrix(f32 *m) {
    int i,j;for(i=0;i<16;i++) m[i]=0;
    m[15]=1;for(i=0;i<3;i++) for(j=0;j<3;j++) m[i*4+j]=linear[pattern][i*3+j];
}
__attribute__((noinline)) void func_151D5D60(void *slots,s16 view,s32 size,Vtx **cursor,u8 *flag) {
    if(backend++ || slots!=a.bytes+0x100 || view!=expectedView || size!=64) error=1;
    cursorSlot=cursor;*cursor=success?(Vtx *)(b.bytes+64):NULL;*flag=(u8)fresh;
}
void *memcpy(void *out,const void *input,u32 length) {
    u8 *dst=out;const u8 *src=input;u32 i;
    if(length!=64 || src!=a.bytes+0xC0 || dst!=(copies?((mutation?c.bytes:b.bytes)+64):b.bytes)) error=2;
    for(i=0;i<length;i++) dst[i]=src[i];
    if(copies++==0 && mutation) {
        *(u8 **)(a.bytes+0x100+expectedView*4)=c.bytes;*(f32 *)(a.bytes+0x2C)=-4.75f;
    }
    return out;
}
void func_150A8050(f32 matrix[4][4],f32 x,f32 y,f32 z) {
    if(orients++ || x!=0.25f || y!=-0.5f || z!=1) error=3;
    fill_matrix(&matrix[0][0]);if(mutation) *(f32 *)(a.bytes+0x34)=-7.5f;
}
void func_150A7960(f32 *matrix,f32 x,f32 y,f32 z,f32 *ox,f32 *oy,f32 *oz) {
    f32 px=matrices==1 || matrices==2?-expectedWidth:expectedWidth;
    f32 py=matrices>=2?-expectedHeight:expectedHeight;
    if(x!=px || y!=py || z!=0 || oy!=ox+1 || oz!=ox+2) error=4;
    if(redirect) *cursorSlot=(Vtx *)(c.bytes+matrices*16);
    matrices++;semantic_matrix(matrix,x,y,z,ox,oy,oz);
}
static void initialize(int view,int w) {
    int i;for(i=0;i<0x180;i++) a.bytes[i]=(u8)(i*17+13);
    for(i=0;i<160;i++) b.bytes[i]=c.bytes[i]=(u8)(i*17+13);
    *(f32 *)(a.bytes+0x2C)=widths[w];*(f32 *)(a.bytes+0x30)=2.5f;
    *(f32 *)(a.bytes+0x34)=10.5f;*(f32 *)(a.bytes+0x38)=-12.25f;*(f32 *)(a.bytes+0x3C)=3.75f;
    *(f32 *)(a.bytes+0x40)=0.25f;*(f32 *)(a.bytes+0x44)=-0.5f;*(f32 *)(a.bytes+0x48)=1;
    expectedView=(s16)view;backend=copies=orients=matrices=error=0;
    if(success) *(u8 **)(a.bytes+0x100+expectedView*4)=b.bytes;
    for(i=0;i<0x180;i++) wantedA[i]=a.bytes[i];
    for(i=0;i<160;i++) {wantedB[i]=b.bytes[i];wantedC[i]=c.bytes[i];}
    if(!success) return;
    if(fresh) {
        u8 *second=mutation?wantedC:wantedB;
        for(i=0;i<64;i++) wantedB[i]=wantedA[0xC0+i];
        if(mutation) {*(u8 **)(wantedA+0x100+expectedView*4)=c.bytes;*(f32 *)(wantedA+0x2C)=-4.75f;}
        for(i=0;i<64;i++) second[64+i]=wantedA[0xC0+i];
    }
    expectedWidth=*(f32 *)(wantedA+0x2C);expectedHeight=*(f32 *)(wantedA+0x30);
    if(mutation) *(f32 *)(wantedA+0x34)=-7.5f;
    for(i=0;i<4;i++) {
        int axis;f32 x=i==1 || i==2?-expectedWidth:expectedWidth,y=i>=2?-expectedHeight:expectedHeight;
        u8 *out=redirect?wantedC+i*16:wantedB+64+i*16;
        for(axis=0;axis<3;axis++) {
            f32 left=linear[pattern][axis]*x+linear[pattern][3+axis]*y;
            f32 right=linear[pattern][6+axis]*0.0f+*(f32 *)(wantedA+0x34+axis*4);
            *(s16 *)(out+axis*2)=(s32)(left+right);
        }
        *(u16 *)(out+6)=0;
    }
}
static int verify(Vtx *result) {
    int i;if(error || backend!=1 || result!=(success?(Vtx *)(b.bytes+64):NULL)) return 1;
    if(copies!=(success && fresh?2:0) || orients!=success || matrices!=(success?4:0)) return 2;
    for(i=0;i<0x180;i++) if(a.bytes[i]!=wantedA[i]) return 3;
    for(i=0;i<160;i++) if(b.bytes[i]!=wantedB[i] || c.bytes[i]!=wantedC[i]) return 4;
    return 0;
}
'''
        self.run_host(r'''
int v,w,f,s,p,m,r,count=0;
if(sizeof(void *)!=4 || sizeof(Vtx)!=16 || sizeof(s16)!=2) return 20;
for(v=0;v<3;v++) for(w=0;w<6;w++) for(f=0;f<2;f++) for(s=0;s<2;s++)
for(p=0;p<3;p++) for(m=0;m<2;m++) for(r=0;r<2;r++) {
    fresh=f;success=s;pattern=p;mutation=m;redirect=r;initialize(v,w);
    if(verify(func_15140190(a.bytes,(s16)v))) return 21;
    count++;
}
if(count!=864) return 22;
success=0;fresh=255;
for(v=0;v<65536;v++) {initialize(v,0);if(verify(func_15140190(a.bytes,(s16)v))) return 23;}
''')


if __name__=='__main__':
    unittest.main()
