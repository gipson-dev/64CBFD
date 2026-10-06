"""Captured basis components, live translation aliases, and real buffer backend."""

import csv
import itertools
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_basis_quad_builder_candidates as screen
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_cached_quad_builder_match import half, external
from tools.tests import test_game_random_curve_record as native
from tools.match_progress import load_elf_functions

ACTOR, BUFFER, ALTERNATE, WIDTH, HEIGHT = 0x20000,0x21000,0x22000,0x23000,0x23100
BACKEND, COPY = screen.SYMBOLS['func_151D5D60'],screen.SYMBOLS['memcpy']
ALLOCATE, FLIP = 0x10003C40,0x800BE9C0
WRAPPER = 0x1513F4B0
LAYOUTS = ((WIDTH,HEIGHT),(WIDTH,WIDTH),(ACTOR+0x34,ACTOR+0x40))
OUTPUTS = (BUFFER+64,ACTOR+0x2C,ACTOR+0x34,WIDTH)


def read(memory,address,size=4):
    return int.from_bytes(bytes(memory[address+i] for i in range(size)),'big')


def number(memory,address):
    return floating(read(memory,address))


def round_float(value):
    return floating(bits(value))


def memory_case(view,slot=BUFFER,width=0.25,height=0.5):
    memory = {STACK+i:0xA5 for i in range(-0x600,0x100)}
    for base,size in ((ACTOR,0x180),(BUFFER,160),(ALTERNATE,160),(WIDTH,160),(HEIGHT,160)):
        memory.update({base+i:(i*17+13)&255 for i in range(size)})
    for offset,value in zip((0x2C,0x30,0x34,0x38,0x3C,0x40,0x44,0x48),
                            (width,height,128.5,136.75,144.25,0.25,-0.5,1.0)):
        put(memory,ACTOR+offset,bits(value))
    for base,values in ((WIDTH,(1.25,-0.75,2.0)),(HEIGHT,(0.25,0.75,-0.5))):
        for axis,value in enumerate(values):put(memory,base+axis*4,bits(value))
    put(memory,ACTOR+0x100+half(view)*4,slot)
    put(memory,FLIP,0,1)
    return memory


def mutate_first(memory,view):
    put(memory,ACTOR+0x100+half(view)*4,ALTERNATE)
    put(memory,ACTOR+0x2C,bits(0.125))
    put(memory,ACTOR+0x38,bits(140.75))
    put(memory,WIDTH,bits(0.75));put(memory,HEIGHT+8,bits(-0.25))


def reference(memory,view,width_axis,height_axis,first,fresh,mutation):
    result = dict(memory)
    if not first:return result,0
    cursor = first
    if fresh:
        for copy in range(2):
            destination = read(result,ACTOR+0x100+half(view)*4)+copy*64
            for i in range(64):result[destination+i]=result[ACTOR+0xC0+i]
            if mutation:
                if copy==0:mutate_first(result,view)
                else:
                    put(result,ACTOR+0x34,bits(129.25));cursor=ALTERNATE+64
    width,height = number(result,ACTOR+0x2C),number(result,ACTOR+0x30)
    scaled_width = [round_float(number(result,width_axis+i*4)*width) for i in range(3)]
    scaled_height = [round_float(number(result,height_axis+i*4)*height) for i in range(3)]
    for vertex,(width_sign,height_sign) in enumerate(((1,1),(-1,1),(-1,-1),(1,-1))):
        for axis in range(3):
            translation = number(result,ACTOR+0x34+axis*4)
            value = round_float(round_float(translation+width_sign*scaled_width[axis])+height_sign*scaled_height[axis])
            assert -2147483648<=value<2147483648, 'finite bounded conversion fixture'
            put(result,cursor+vertex*16+axis*2,int(value),2)
        put(result,cursor+vertex*16+6,0,2)
    return result,first


class BasisOracle(TriangleOracle):
    def __init__(self,words,memory,view,width_axis,height_axis,first,fresh,mutation,phase=0,
                 connected=None,outcome='opaque'):
        super().__init__(words,memory,entry=screen.ENTRY,
            arguments=(ACTOR,width_axis,height_axis,view),phase=phase,connected=connected)
        self.view,self.first,self.fresh,self.mutation = half(view),first,fresh,mutation
        self.width_axis,self.height_axis = width_axis,height_axis
        self.outcome,self.copies,self.allocations = outcome,0,0

    def record_call(self,target):
        if target==screen.ENTRY:
            args = self.arguments(4)
            assert args==(ACTOR,self.width_axis,self.height_axis,self.view&0xFFFFFFFF),'wrapper contract'
            self.calls.append((target,*args));return
        args = self.arguments(5 if target==BACKEND else 4 if target==ALLOCATE else 3)
        if target==BACKEND:
            assert args[:3]==(ACTOR+0x100,self.view&0xFFFFFFFF,64),'backend contract'
            self.cursor_slot,self.fresh_slot = args[3:5]
            self.calls.append((target,*args[:3],'cursor','fresh'))
        elif target==ALLOCATE:
            assert args==(128,1,2,1),'allocator contract'
            self.calls.append((target,*args))
        else:
            assert target==COPY
            assert args[1:]==(ACTOR+0xC0,64),'copy contract'
            self.calls.append((target,*args))

    def hook(self,target):
        if target==BACKEND:
            self.put(self.cursor_slot,self.first,4);self.put(self.fresh_slot,self.fresh,1)
        elif target==ALLOCATE:
            self.allocations += 1
            result = 0 if self.outcome=='failed' else BUFFER
            if self.mutation:
                self.put(FLIP,0 if self.get(FLIP,1) else 255,1)
                self.put(ACTOR+0x2C,bits(0.125),4)
        else:
            assert target==COPY
            destination,source,size = self.arguments(3)
            for i in range(size):self.put(destination+i,self.get(source+i,1),1)
            self.copies += 1
            if self.mutation:
                if self.copies==1:
                    for address,value in ((ACTOR+0x100+self.view*4,ALTERNATE),(ACTOR+0x2C,bits(0.125)),
                                          (ACTOR+0x38,bits(140.75)),(WIDTH,bits(0.75)),(HEIGHT+8,bits(-0.25))):
                        self.put(address,value,4)
                else:
                    self.put(ACTOR+0x34,bits(129.25),4);self.put(self.cursor_slot,ALTERNATE+64,4)
        for register in (1,2,3,*range(4,16),24,25):self.r[register]=0xA5000000+register
        self.f[:20]=[0xA5000000+i for i in range(20)]
        if target==ALLOCATE:self.r[2]=result


class GameBasisQuadBuilderMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-basis-quad-builder-test';cls.output.mkdir(exist_ok=True)
        cls.record,cls.words = screen.compile_candidate(cls.root,cls.output,'selected')
        rom = (cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>167I',rom,screen.ROM))
        cls.backend = list(struct.unpack_from('>52I',rom,0x203210))
        cls.connected = {BACKEND+i*4:w for i,w in enumerate(cls.backend)}
        cls.directory = tempfile.TemporaryDirectory();cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def test_complete_shape_and_two_independent_loads(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],self.record['diagnostics']),
                         (167,0x68,2,''))
        self.assertEqual(self.words[:41],self.retail[:41]);self.assertEqual(self.words[43:],self.retail[43:])
        self.assertEqual(self.words[41:43],[0xC600002C,0x8FA30070])
        self.assertEqual(self.words[41:43],list(reversed(self.retail[41:43])))

    def test_guest_full_footprints_aliases_live_copies_and_all_words(self):
        count,coverage = 0,set()
        for view,fresh,success,mutation,out,(width_axis,height_axis),phase in itertools.product(
                (0,1,3,0x8000,0xFFFF,0x12340002),(0,1,255),(False,True),(False,True),OUTPUTS,LAYOUTS,(0,8)):
            memory = memory_case(view)
            first = out if success else 0
            wanted,value = reference(memory,view,width_axis,height_axis,first,fresh,mutation)
            models = [BasisOracle(body,memory,view,width_axis,height_axis,first,fresh,mutation,phase).run()
                      for body in (self.words,self.retail)]
            for model in models:
                self.assertEqual(external(model.memory),external(wanted),(count,out,width_axis))
                self.assertEqual(model.r[2],value);self.assertEqual(model.copies,2 if success and fresh else 0)
                coverage.update(model.visits)
            self.assertEqual(models[0].calls,models[1].calls)
            self.assertEqual([e for e in models[0].events if not STACK-0x600<=e[1]<STACK+0x100],
                             [e for e in models[1].events if not STACK-0x600<=e[1]<STACK+0x100])
            count += 1
        self.assertEqual((count,len(coverage)),(1728,167))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=count,bodies=2,covered_words=len(coverage)),indent=2)+'\n')

    def test_connected_actual_backend_allocation_ping_pong_and_live_flag(self):
        count,coverage = 0,set()
        for view,outcome,flip,mutation,(width_axis,height_axis),phase in itertools.product(
                (0,3,0xFFFF),('existing','new','failed'),(0,1,255),(False,True),LAYOUTS,(0,8)):
            memory = memory_case(view,BUFFER if outcome=='existing' else 0);put(memory,FLIP,flip,1)
            backend_result = dict(memory)
            if outcome!='existing':
                put(backend_result,ACTOR+0x100+half(view)*4,0 if outcome=='failed' else BUFFER)
                if mutation:
                    put(backend_result,FLIP,0 if flip else 255,1);put(backend_result,ACTOR+0x2C,bits(0.125))
            first = 0 if outcome=='failed' else BUFFER+(0 if read(backend_result,FLIP,1) else 64)
            wanted,value = reference(backend_result,view,width_axis,height_axis,first,outcome=='new',mutation)
            models = [BasisOracle(body,memory,view,width_axis,height_axis,0,0,mutation,phase,
                                 self.connected,outcome).run() for body in (self.words,self.retail)]
            for model in models:
                self.assertEqual(external(model.memory),external(wanted),(count,outcome,flip))
                self.assertEqual(model.r[2],value);self.assertEqual(model.allocations,outcome!='existing')
                coverage.update(model.visits)
            self.assertEqual(models[0].calls,models[1].calls)
            self.assertEqual([e for e in models[0].events if not STACK-0x600<=e[1]<STACK+0x100],
                             [e for e in models[1].events if not STACK-0x600<=e[1]<STACK+0x100])
            count += 1
        self.assertEqual((count,len(coverage)),(324,218))
        self.assertNotIn(BACKEND+0x34,coverage)
        (self.output/'connected.json').write_text(json.dumps(dict(cases=count,bodies=2,covered_words=len(coverage),
            unreachable_optional_null_flag_store=hex(BACKEND+0x34)),indent=2)+'\n')

    def test_float_rounding_fractional_and_halfword_wrap(self):
        count = 0
        for width,height,translation,phase in itertools.product(
                (0.0,-0.0,0.25,-0.25,1.25,-2.75,32767.75,-32768.75,65536.5,-65536.5,16777216.0),
                (-1.5,0.0,2.5),(128.5,-0.5,16777216.0),(0,8)):
            memory = memory_case(0,width=width,height=height)
            for axis in range(3):put(memory,ACTOR+0x34+axis*4,bits(translation))
            wanted,value = reference(memory,0,WIDTH,HEIGHT,BUFFER+64,0,False)
            for body in (self.words,self.retail):
                model = BasisOracle(body,memory,0,WIDTH,HEIGHT,BUFFER+64,0,False,phase).run()
                self.assertEqual(external(model.memory),external(wanted));self.assertEqual(model.r[2],value)
            count += 1
        self.assertEqual(count,198)

    def test_actual_owner_wrapper_and_backend_embedded_basis_chain(self):
        rom = (self.root/'conker/conker.us.bin').read_bytes()
        wrapper = list(struct.unpack_from('>13I',rom,0x16C960))
        production = load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        self.assertEqual(production['func_1513F4B0'],wrapper)
        width_axis,height_axis = ACTOR+0x110,ACTOR+0x11C
        count,coverage = 0,set()
        for view,outcome,flip,mutation,phase in itertools.product(
                (0,3,0xFFFF,0x12340002),('existing','new','failed'),(0,1,255),(False,True),(0,8)):
            memory = memory_case(view,BUFFER if outcome=='existing' else 0);put(memory,FLIP,flip,1)
            for pointer,values in ((width_axis,(1.25,-0.75,2.0)),(height_axis,(0.25,0.75,-0.5))):
                for axis,value in enumerate(values):put(memory,pointer+axis*4,bits(value))
            backend_result = dict(memory)
            if outcome!='existing':
                put(backend_result,ACTOR+0x100+half(view)*4,0 if outcome=='failed' else BUFFER)
                if mutation:
                    put(backend_result,FLIP,0 if flip else 255,1);put(backend_result,ACTOR+0x2C,bits(0.125))
            first = 0 if outcome=='failed' else BUFFER+(0 if read(backend_result,FLIP,1) else 64)
            wanted,_ = reference(backend_result,view,width_axis,height_axis,first,outcome=='new',mutation)
            models = []
            for body in (self.words,self.retail):
                model = BasisOracle(body,memory,view,width_axis,height_axis,0,0,mutation,phase,self.connected,outcome)
                model.code.update({WRAPPER+i*4:w for i,w in enumerate(wrapper)})
                model.entry=WRAPPER;model.r[5]=view&0xFFFFFFFF
                model.run();models.append(model)
                self.assertEqual(external(model.memory),external(wanted));coverage.update(model.visits)
            self.assertEqual(models[0].calls,models[1].calls)
            self.assertEqual([e for e in models[0].events if not STACK-0x600<=e[1]<STACK+0x100],
                             [e for e in models[1].events if not STACK-0x600<=e[1]<STACK+0x100])
            count += 1
        self.assertEqual((count,len(coverage)),(144,231))

    def test_production_body_slot_caller_and_two_nonrelocating_guards(self):
        source = (self.root/'conker/src/game_169510.c').read_text()
        self.assertIn(screen.SELECTED,source)
        self.assertIn('Vtx *func_15140410(u8 *actor, f32 *widthAxis, f32 *heightAxis, s16 view);',source)
        self.assertIn('func_15140410((u8 *)arg0, (f32 *)((u8 *)arg0 + 0x110),',source)
        production = load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        self.assertEqual(production['func_15140410'],self.retail)
        self.assertEqual(production['func_151D5D60'],self.backend)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        guards = [r for r in rows if r['function']=='func_15140410']
        self.assertEqual((len(rows),len(guards)),(10747,2))
        normalized = list(self.words)
        for index,guard in enumerate(guards,41):
            self.assertEqual(guard['filename'],'game_169510');self.assertEqual(int(guard['offset'],16),index*4)
            self.assertEqual(int(guard['expected'],16),self.words[index]);self.assertEqual(int(guard['replacement'],16),self.retail[index])
            self.assertEqual((guard['expected_relocations'],guard['replacement_relocations'],guard['omit']),('-','-','false'))
            self.assertEqual((guard['insert_after'],guard['insert_after_relocations']),('',''))
            normalized[index]=int(guard['replacement'],16)
        self.assertEqual(normalized,self.retail)

    def test_twenty_four_compiler_controls(self):
        expected = {'selected':((167,104,2),(167,104,11),(210,72,209),(210,72,209)),
            'components-first':((167,104,8),(167,104,17),(210,72,209),(210,72,209)),
            'scalars':((167,112,31),(167,112,35),(208,80,208),(208,80,208)),
            'fresh-first':((167,104,4),(167,104,12),(210,72,209),(210,72,209)),
            'early-null':((165,104,148),(165,104,157),(208,72,206),(208,72,206)),
            'byte-output':((167,104,2),(167,104,11),(210,72,209),(210,72,209))}
        count = 0
        for name,body in screen.candidates():
            for index,profile in enumerate(screen.PROFILES):
                record,_ = screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                self.assertEqual((record['body_words'],record['frame'],record['differences']),expected[name][index])
                self.assertEqual(record['diagnostics'],'');count += 1
        self.assertEqual(count,24)

    def test_eight_compiled_negatives_detect_memory_return_and_backend_contract(self):
        eager = screen.SELECTED.replace('    u8 fresh;', '    f32 tx, ty, tz;\n    u8 fresh;').replace(
            '    wx =', '    tx = *(f32 *)(actor + 0x34);\n    ty = *(f32 *)(actor + 0x38);\n    tz = *(f32 *)(actor + 0x3C);\n    wx =')
        for offset,letter in ((0x34,'x'),(0x38,'y'),(0x3C,'z')):
            eager = eager.replace('((*(f32 *)(actor + 0x%X)'%offset,'((t'+letter)
        live = screen.SELECTED.replace('    f32 wx, wy, wz, hx, hy, hz;\n','')
        for letter,axis in zip('xyz',range(3)):
            for prefix,vector,offset in (('w','widthAxis',0x2C),('h','heightAxis',0x30)):
                statement = '    %s%s = *(f32 *)(actor + 0x%X) * %s[%d];\n'%(prefix,letter,offset,vector,axis)
                live = live.replace(statement,'')
                live = live.replace(prefix+letter+')','(*(f32 *)(actor + 0x%X) * %s[%d]))'%(offset,vector,axis))
        cached = screen.SELECTED.replace('        if (fresh) {','        if (fresh) {\n            u8 *buffer = *(u8 **)(actor + 0x100 + view * 4);').replace(
            'memcpy(*(u8 **)(actor + 0x100 + view * 4)', 'memcpy(buffer')
        negatives = [('stub','Vtx *func_15140410(u8 *actor, f32 *widthAxis, f32 *heightAxis, s16 view) { return NULL; }'),
            ('flags', '\n'.join(line for line in screen.SELECTED.splitlines() if '.v.flag = 0;' not in line)),
            ('grouped-add',screen.SELECTED.replace('((*(f32 *)(actor + 0x34) + wx) + hx)',
                                                 '(*(f32 *)(actor + 0x34) + (wx + hx))')),
            ('eager-translation',eager),('live-basis',live),('cached-slot',cached),
            ('changed-return',screen.SELECTED.replace('    return first;','    return cursor;')),
            ('wrong-size',screen.SELECTED.replace('view, 0x40,','view, 0x20,'))]
        cases = [(memory_case(0),WIDTH,HEIGHT,BUFFER+64,1,True),
                 (memory_case(0,width=4,height=2),WIDTH,HEIGHT,WIDTH,0,False),
                 (memory_case(0),ACTOR+0x34,ACTOR+0x40,ACTOR+0x34,0,False)]
        rounding = memory_case(0,width=1,height=1)
        for axis in range(3):
            put(rounding,ACTOR+0x34+axis*4,bits(16777216));put(rounding,WIDTH+axis*4,bits(1))
            put(rounding,HEIGHT+axis*4,bits(-16777216))
        cases.append((rounding,WIDTH,HEIGHT,BUFFER+64,0,False))
        for name,body in negatives:
            _,words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            found = False
            for memory,width_axis,height_axis,out,fresh,mutation in cases:
                wanted,value = reference(memory,0,width_axis,height_axis,out,fresh,mutation)
                try:model = BasisOracle(words,memory,0,width_axis,height_axis,out,fresh,mutation).run()
                except AssertionError as error:
                    self.assertEqual((name,str(error)),('wrong-size','backend contract'));found=True
                else:found = model.r[2]!=value or external(model.memory)!=external(wanted)
                if found:break
            self.assertTrue(found,name)

    def test_native_full_alias_storage_and_every_signed_view_null(self):
        self.fixture = '''typedef unsigned char u8;typedef short s16;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;typedef float f32;
typedef struct {struct {s16 ob[3];u16 flag;s16 tc[2];u8 cn[4];} v;} Vtx;
#define NULL ((void *)0)
'''+screen.DECLARATIONS+'''void *memcpy(void *,const void *,u32);
'''+screen.SELECTED+r'''
static union {u32 align;u8 bytes[0x180];} a;
static union {u32 align;u8 bytes[160];} b,c,w,h;
static u8 wantedA[0x180],wantedB[160],wantedC[160],wantedW[160],wantedH[160];
static u8 *bases[5],*wanted[5];
static u32 sizes[]={0x180,160,160,160,160};
static Vtx **cursorSlot;
static u8 *output,*widthVector,*heightVector;
static int fresh,success,mutation,copies,backend,error;
static s16 expectedView;
static u8 *mapped(u8 *pointer) {
    int i;u32 address=(u32)pointer;
    for(i=0;i<5;i++) if(address>=(u32)bases[i] && address<(u32)bases[i]+sizes[i])
        return wanted[i]+(address-(u32)bases[i]);
    error=9;return wantedA;
}
__attribute__((noinline)) void func_151D5D60(void *slots,s16 view,s32 size,Vtx **cursor,u8 *flag) {
    if(backend++ || slots!=a.bytes+0x100 || view!=expectedView || size!=64) error=1;
    cursorSlot=cursor;*cursor=success?(Vtx *)output:NULL;*flag=(u8)fresh;
}
void *memcpy(void *out,const void *input,u32 length) {
    u8 *dst=out;const u8 *src=input;u32 i;
    if(length!=64 || src!=a.bytes+0xC0 || dst!=(copies?((mutation?c.bytes:b.bytes)+64):b.bytes)) error=2;
    for(i=0;i<length;i++) dst[i]=src[i];
    copies++;
    if(mutation) {
        if(copies==1) {
            *(u8 **)(a.bytes+0x100+expectedView*4)=c.bytes;
            *(f32 *)(a.bytes+0x2C)=0.125f;*(f32 *)(a.bytes+0x38)=140.75f;
            *(f32 *)w.bytes=0.75f;*(f32 *)(h.bytes+8)=-0.25f;
        } else {
            *(f32 *)(a.bytes+0x34)=129.25f;*cursorSlot=(Vtx *)(c.bytes+64);
        }
    }
    return out;
}
static void initialize(int view,int which,int layout) {
    int i,j;u8 *outputs[4];u8 *widths[3],*heights[3];
    bases[0]=a.bytes;bases[1]=b.bytes;bases[2]=c.bytes;bases[3]=w.bytes;bases[4]=h.bytes;
    wanted[0]=wantedA;wanted[1]=wantedB;wanted[2]=wantedC;wanted[3]=wantedW;wanted[4]=wantedH;
    for(i=0;i<5;i++) for(j=0;j<(int)sizes[i];j++) bases[i][j]=(u8)(j*17+13);
    *(f32 *)(a.bytes+0x2C)=0.25f;*(f32 *)(a.bytes+0x30)=0.5f;
    *(f32 *)(a.bytes+0x34)=128.5f;*(f32 *)(a.bytes+0x38)=136.75f;*(f32 *)(a.bytes+0x3C)=144.25f;
    *(f32 *)(a.bytes+0x40)=0.25f;*(f32 *)(a.bytes+0x44)=-0.5f;*(f32 *)(a.bytes+0x48)=1;
    *(f32 *)w.bytes=1.25f;*(f32 *)(w.bytes+4)=-0.75f;*(f32 *)(w.bytes+8)=2;
    *(f32 *)h.bytes=0.25f;*(f32 *)(h.bytes+4)=0.75f;*(f32 *)(h.bytes+8)=-0.5f;
    expectedView=(s16)view;backend=copies=error=0;
    if(success) *(u8 **)(a.bytes+0x100+expectedView*4)=b.bytes;
    outputs[0]=b.bytes+64;outputs[1]=a.bytes+0x2C;outputs[2]=a.bytes+0x34;outputs[3]=w.bytes;
    widths[0]=widths[1]=w.bytes;widths[2]=a.bytes+0x34;
    heights[0]=h.bytes;heights[1]=w.bytes;heights[2]=a.bytes+0x40;
    output=outputs[which];widthVector=widths[layout];heightVector=heights[layout];
    for(i=0;i<5;i++) for(j=0;j<(int)sizes[i];j++) wanted[i][j]=bases[i][j];
}
static void compute_reference(void) {
    int copy,i,axis,vertex;f32 width,height,scaledW[3],scaledH[3];u8 *cursor=output;
    static s32 signW[]={1,-1,-1,1},signH[]={1,1,-1,-1};
    if(!success) return;
    if(fresh) {
        for(copy=0;copy<2;copy++) {
            u8 *destination=*(u8 **)(wantedA+0x100+expectedView*4)+copy*64;
            for(i=0;i<64;i++) mapped(destination)[i]=wantedA[0xC0+i];
            if(mutation) {
                if(copy==0) {
                    *(u8 **)(wantedA+0x100+expectedView*4)=c.bytes;
                    *(f32 *)(wantedA+0x2C)=0.125f;*(f32 *)(wantedA+0x38)=140.75f;
                    *(f32 *)wantedW=0.75f;*(f32 *)(wantedH+8)=-0.25f;
                } else {*(f32 *)(wantedA+0x34)=129.25f;cursor=c.bytes+64;}
            }
        }
    }
    width=*(f32 *)(wantedA+0x2C);height=*(f32 *)(wantedA+0x30);
    for(axis=0;axis<3;axis++) {
        scaledW[axis]=*(f32 *)mapped(widthVector+axis*4)*width;
        scaledH[axis]=*(f32 *)mapped(heightVector+axis*4)*height;
    }
    for(vertex=0;vertex<4;vertex++) {
        for(axis=0;axis<3;axis++) {
            f32 translation=*(f32 *)(wantedA+0x34+axis*4),left,result;
            left=signW[vertex]>0?translation+scaledW[axis]:translation-scaledW[axis];
            result=signH[vertex]>0?left+scaledH[axis]:left-scaledH[axis];
            *(s16 *)mapped(cursor+vertex*16+axis*2)=(s32)result;
        }
        *(u16 *)mapped(cursor+vertex*16+6)=0;
    }
}
static int verify(Vtx *result) {
    int i,j;if(error || backend!=1 || result!=(success?(Vtx *)output:NULL)) return 1;
    if(copies!=(success && fresh?2:0)) return 2;
    for(i=0;i<5;i++) for(j=0;j<(int)sizes[i];j++) if(bases[i][j]!=wanted[i][j]) return 3;
    return 0;
}
'''
        self.run_host(r'''
int v,f,s,m,o,l,count=0;static s32 views[]={0,2,3,65535};static s32 freshValues[]={0,1,255};
if(sizeof(void *)!=4 || sizeof(Vtx)!=16 || sizeof(s16)!=2 || sizeof(f32)!=4) return 20;
for(v=0;v<4;v++) for(f=0;f<3;f++) for(s=0;s<2;s++) for(m=0;m<2;m++) for(o=0;o<4;o++) for(l=0;l<3;l++) {
    fresh=freshValues[f];success=s;mutation=m;initialize(views[v],o,l);compute_reference();
    if(verify(func_15140410(a.bytes,(f32 *)widthVector,(f32 *)heightVector,(s16)views[v]))) return 21;
    count++;
}
if(count!=576) return 22;
success=0;fresh=255;
for(v=0;v<65536;v++) {
    initialize(v,0,0);compute_reference();
    if(verify(func_15140410(a.bytes,NULL,NULL,(s16)v))) return 23;
}
''')


if __name__=='__main__':
    unittest.main()
