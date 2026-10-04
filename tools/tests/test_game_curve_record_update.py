import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests import test_game_random_curve_record as curve


class GameCurveRecordUpdateTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_113D60.c').read_text()
        cls.body = re.search(r'void func_150E7C9C\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.builder = re.search(r'void \*func_150E7994\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.emitter = re.search(r's32 func_150E75A0\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';', source, re.S).group(0)
            for name in ('CurvePayload113D60', 'EmitterPosition113D60', 'EmitterDescriptor113D60', 'RandomPacket113D60'))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = ('typedef signed char s8; typedef unsigned char u8; typedef short s16; '
                     'typedef unsigned short u16; typedef int s32; typedef unsigned int u32; typedef float f32;\n'
                     '#define NULL ((void *)0)\n')
        cls.fixture = cls.types + cls.layouts + r'''
f32 D_800BE9A4;
static union { u32 alignment; u8 bytes[0x40100]; } storage;
static u8 *record=storage.bytes+16;
static CurvePayload113D60 *payload;
static f32 samples[2], seenPosition[4][2], seenScale[4], seenProgress[4];
static u32 words[2];
static s32 seen[4][10], soundPan[4];
static int floatCalls, integerCalls, emitCalls, soundCalls, error, mutation, stage;
static char trace[64];
static int traceLength;
static u32 bits(f32 value) { union { f32 f; u32 u; } word; word.f=value; return word.u; }
static f32 number(u32 value) { union { f32 f; u32 u; } word; word.u=value; return word.f; }
static void push(char value) { if(traceLength<63) trace[traceLength++]=value; else error=1; }
static int trace_is(const char *expected) {
    int i=0;
    while(expected[i]) { if(i>=traceLength || expected[i]!=trace[i]) return 0; i++; }
    return i==traceLength;
}
f32 func_150ADA68(void) {
    static f32 controls[4]={0,0.25f,0.75f,1};
    int i=floatCalls++;
    push('F');
    if(stage==0) { if(i>=4) { error=2; return 0; } return controls[i]; }
    if(i!=emitCalls*2+(i%2) || soundCalls!=emitCalls || integerCalls!=emitCalls*2+(i%2)*2) error=3;
    if(mutation==1 && i%2==0) {
        f32 *point=(f32 *)(record+0x38)+payload->cursor*2;
        point[0]=1000; point[1]=-1000;
        record[0xC]=0xD5; record[1]=0xFE; D_800BE9A4=-999;
    }
    return samples[i%2];
}
s32 func_150ADA20(void) {
    int i=integerCalls++;
    push('I');
    if(stage==0) return (s32)0xFFFFFFFF;
    if(i!=emitCalls*2+(i%2) || soundCalls!=emitCalls || floatCalls!=emitCalls*2+1) error=4;
    return (s32)words[i%2];
}
static s32 capture(f32 *position,f32 scale,s16 id,u8 flags,s32 duration,s32 opacity,
                   s32 size0,s32 size1,s32 *pair,s32 mode,u8 slot,s32 context) {
    int i=emitCalls++;
    push('E');
    if(i>=4 || floatCalls!=(i+1)*2 || integerCalls!=(i+1)*2 || soundCalls!=i
       || id!=300 || opacity!=255 || size0!=1 || size1!=255 || pair || mode) { error=5; return -1; }
    seenPosition[i][0]=position[0]; seenPosition[i][1]=position[1]; seenScale[i]=scale;
    seen[i][0]=flags; seen[i][1]=duration; seen[i][2]=slot; seen[i][3]=context;
    seen[i][4]=payload->cursor; seen[i][5]=payload->count; seenProgress[i]=payload->progress;
    if(mutation==2) { payload->progress=2.25f; payload->cursor=1; payload->count=2; }
    if(mutation==4) position[0]=32;
    return -123;
}
s32 func_150E75A0(f32 *position,f32 scale,s16 id,u8 flags,s32 duration,s32 opacity,
                   s32 size0,s32 size1,s32 *pair,s32 mode,u8 slot,s32 context) {
    return capture(position,scale,id,flags,duration,opacity,size0,size1,pair,mode,slot,context);
}
void func_10010F30(s32 id,u16 volume,u8 pan,s16 arg3,u8 arg4) {
    int i=soundCalls++;
    push('S');
    if(i>=4 || emitCalls!=i+1 || floatCalls!=(i+1)*2 || integerCalls!=(i+1)*2
       || id!=0x360 || volume!=0x7FFF || arg3 || arg4) { error=6; return; }
    soundPan[i]=pan;
    if(mutation==3) { payload->progress=0.5f; payload->cursor=1; payload->count=3; }
}
static void initialize(s16 count,s16 cursor,f32 progress,f32 rate,f32 delta) {
    u32 i;
    f32 *points;
    static f32 x[4]={-146,-50,50,146};
    for(i=0;i<sizeof(storage.bytes);i++) storage.bytes[i]=0x5A;
    record=storage.bytes+16; payload=(CurvePayload113D60 *)(record+0x28);
    record[1]=0xAB; record[0xC]=0xCD; *(s16 *)(record+0xE)=300;
    payload->value=rate; payload->progress=progress; payload->count=count; payload->cursor=cursor;
    D_800BE9A4=delta; points=(f32 *)(record+0x38);
    for(i=0;i<(u32)(count>0?count:0);i++) { points[i*2]=x[i%4]; points[i*2+1]=(f32)(i+1)*16; }
    samples[0]=0.25f; samples[1]=0.75f; words[0]=0x80000001; words[1]=0xFFFFFFFE;
    floatCalls=integerCalls=emitCalls=soundCalls=error=mutation=traceLength=0; stage=1;
}
''' + cls.body + '\n'

    def test_strict_progress_gate_and_signed_terminal_comparison(self):
        self.run_host(r'''
static f32 progress[]={-2,0,0.5f,1};
static s16 counts[]={2,2,0,-1,2}, cursors[]={0,2,0,0,3};
int i;
for(i=0;i<4;i++) {
    initialize(2,0,progress[i],0,1); func_150E7C9C(record);
    if(error || emitCalls || floatCalls || integerCalls || soundCalls || traceLength
       || payload->cursor || bits(payload->progress)!=bits(progress[i]) || *(s16 *)(record+0xE)!=300) return 1;
}
for(i=0;i<5;i++) {
    initialize(counts[i],cursors[i],0,0,1); func_150E7C9C(record);
    if(error || traceLength || payload->cursor!=cursors[i]) return 2;
    if(*(s16 *)(record+0xE)!=(cursors[i]>=counts[i]?-1:300)) return 3;
}
initialize(2,0,number(0x7FC00000),0,1); func_150E7C9C(record);
if(error || traceLength || payload->progress==payload->progress || *(s16 *)(record+0xE)!=300) return 4;
initialize(2,2,number(0x7F800000),0,1); func_150E7C9C(record);
if(error || traceLength || bits(payload->progress)!=0x7F800000 || *(s16 *)(record+0xE)!=-1) return 5;
''')

    def test_accumulation_flags_arguments_and_multiple_points(self):
        self.run_host(r'''
static f32 x[]={-146,-50,50,146};
int a,b,i;
for(a=0;a<2;a++) for(b=0;b<2;b++) {
    initialize(4,0,0.5f,1.25f,3); words[0]=0xFFFFFFFE + a; words[1]=0x80000000 + b;
    func_150E7C9C(record);
    if(error || emitCalls!=4 || soundCalls!=4 || floatCalls!=8 || integerCalls!=8
       || payload->cursor!=4 || payload->progress!=0.25f || *(s16 *)(record+0xE)!=-1) return 1;
    if(!trace_is("FIIFESFIIFESFIIFESFIIFES")) return 2;
    for(i=0;i<4;i++) {
        if(seenPosition[i][0]!=x[i] || seenPosition[i][1]!=(i+1)*16 || seenScale[i]!=33
           || seen[i][0]!=(a*4+b*2) || seen[i][1]!=118 || seen[i][2]!=0xCD || seen[i][3]!=0xAB
           || seen[i][4]!=i || seenProgress[i]!=4.25f-i
           || soundPan[i]!=(u8)(x[i]*0.4315068424f+64)) return 3;
    }
    for(i=0;i<16;i++) if(storage.bytes[i]!=0x5A || record[0x58+i]!=0x5A) return 4;
    for(i=0x34;i<0x38;i++) if(record[i]!=0x5A) return 5;
}
initialize(32767,32766,0,2,1); func_150E7C9C(record);
if(error || emitCalls!=1 || payload->cursor!=32767 || payload->progress!=1 || *(s16 *)(record+0xE)!=-1) return 6;
''')

    def test_fractional_casts_snapshot_and_post_callback_reloads(self):
        self.run_host(r'''
static f32 fractions[]={-1,0,0.125f,0.5f,1,2};
int i;
for(i=0;i<6;i++) {
    initialize(2,0,1.25f,0,1); samples[0]=fractions[i]; samples[1]=fractions[(i+1)%6];
    func_150E7C9C(record);
    if(error || emitCalls!=1 || seenScale[0]!=fractions[i]*12+30
       || seen[0][1]!=(s32)(u32)(fractions[(i+1)%6]*25+100) || payload->progress!=0.25f) return 1;
}
initialize(2,0,1.25f,0,1); mutation=1; func_150E7C9C(record);
if(error || seenPosition[0][0]!=-146 || seenPosition[0][1]!=16
   || seen[0][2]!=0xD5 || seen[0][3]!=0xFE || soundPan[0]!=(u8)(-146*0.4315068424f+64)) return 2;
initialize(3,0,1.25f,0,1); mutation=2; func_150E7C9C(record);
if(error || emitCalls!=1 || payload->progress!=1.25f || payload->cursor!=2
   || payload->count!=2 || *(s16 *)(record+0xE)!=-1) return 3;
initialize(3,0,1.25f,0,1); mutation=3; func_150E7C9C(record);
if(error || emitCalls!=1 || payload->progress!=-0.5f || payload->cursor!=2
   || payload->count!=3 || *(s16 *)(record+0xE)!=300) return 4;
initialize(2,0,1.25f,0,1); mutation=4; func_150E7C9C(record);
if(error || emitCalls!=1 || soundPan[0]!=(u8)(32*0.4315068424f+64)) return 5;
''')

    def connect_actual_emitter(self):
        fixture = re.sub(r's32 func_150E75A0\([^;{}]+\) \{.*?\n\}', self.emitter, self.fixture, count=1, flags=re.S)
        self.assertNotEqual(fixture, self.fixture)
        self.fixture = self.types + 'extern u8 D_80088A64; s32 func_1515548C(void *,s32,s32 *,s32,s32,u8,s32);\n' + fixture[len(self.types):] + r'''
u8 D_80088A64=0xA7;
s32 func_1515548C(void *data,s32 arg1,s32 *pair,s32 mode,s32 arg4,u8 slot,s32 context) {
    EmitterDescriptor113D60 *d=data;
    if(arg1 || arg4 || d->kind!=4 || d->tag!=0xA7 || d->scale[0]!=d->scale[1]
       || d->field1B!=255 || d->field1C!=230 || d->field1D!=190 || d->field24!=1) error=7;
    return capture((f32 *)&d->position,d->scale[0],d->id,(u8)d->flags,d->duration,d->opacity,
                   d->size0,d->size1,pair,mode,slot,context);
}
'''

    def test_actual_emitter_descriptor_copy_isolated_from_audio_position(self):
        self.connect_actual_emitter()
        self.run_host(r'''
initialize(2,0,1.25f,0,1); mutation=4; func_150E7C9C(record);
if(error || emitCalls!=1 || seen[0][0]!=(4|0x40) || seen[0][1]!=118
   || seenPosition[0][0]!=-146 || soundPan[0]!=(u8)(-146*0.4315068424f+64)
   || payload->cursor!=1 || !trace_is("FIIFES")) return 1;
''')

    def test_actual_builder_update_and_emitter_chain(self):
        self.connect_actual_emitter()
        self.fixture += r'''
s32 D_800BE9E8=2;
static u8 actors[3*0x9A0];
u8 *D_800DBFF0=actors;
void func_1512D748(void *actor,s32 arg1,s32 arg2) { if(actor!=actors+2*0x9A0 || arg1 || arg2!=1) error=8; }
s32 func_151D8868(void *data,s32 a,s32 b,s32 c) {
    RandomPacket113D60 *p=data;
    if(p->kind!=1 || p->duration!=(s16)(0xFFFFFFFFU%11+30) || p->count!=8 || p->mode!=1 || p->index!=-1
       || a || b!=255 || c) error=9;
    return -1;
}
void *func_151491F4(s16 a,s8 b,s8 c,u8 d,u8 e,s32 size,u8 slot,s32 context) {
    if(a!=300 || b!=-1 || c!=16 || d!=1 || e!=12 || size!=48 || slot!=0xCD || context!=0xAB) error=10;
    return record;
}
void *memcpy(void *destination,const void *source,u32 length) {
    u32 i;
    if(destination!=record+0x28 || length!=12) error=11;
    for(i=0;i<length;i++) ((u8 *)destination)[i]=((const u8 *)source)[i];
    return destination;
}
f32 func_15142B04(f32 p) { return p==1?1:0; }
f32 func_15142AC0(f32 p) { return p==0?1:0; }
f32 func_15142A80(f32 p) { return p==-1?1:0; }
f32 func_15142B44(f32 p) { return p==2?1:0; }
''' + self.builder + '\n'
        self.run_host(r'''
static f32 x[]={-146,-50,50,146}, y[]={-80,-40,40,80};
int i;
initialize(4,0,0,0,4.25f); stage=0;
if(func_150E7994(4,1,0xCD,0xAB)!=record || error || floatCalls!=4 || integerCalls!=1
   || payload->value!=1 || payload->progress || payload->cursor || payload->count!=4) return 1;
stage=1; floatCalls=integerCalls=traceLength=0; func_150E7C9C(record);
if(error || emitCalls!=4 || soundCalls!=4 || payload->cursor!=4 || payload->progress!=0.25f
   || *(s16 *)(record+0xE)!=-1 || !trace_is("FIIFESFIIFESFIIFESFIIFES")) return 2;
for(i=0;i<4;i++) if(seenPosition[i][0]!=x[i] || seenPosition[i][1]!=y[i] || seen[i][0]!=(4|0x40)) return 3;
''')

    def test_independent_ido_exact_body_and_single_literal_pool(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file():
            self.skipTest('IDO is unavailable')
        for tool in ('mips-linux-gnu-ld', 'mips-linux-gnu-objcopy'):
            if shutil.which(tool) is None:
                self.skipTest(tool + ' is unavailable')
        source, obj = self.path / 'update.c', self.path / 'update.o'
        source.write_text(self.types + self.layouts + '''
extern f32 D_800BE9A4; f32 func_150ADA68(void); s32 func_150ADA20(void);
s32 func_150E75A0(f32 *,f32,s16,u8,s32,s32,s32,s32,s32 *,s32,u8,s32);
void func_10010F30(s32,u16,u8,s16,u8);
''' + self.body + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm', '-signed',
            '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3',
            '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        elf, binary, pool, script = (self.path / ('update' + suffix) for suffix in ('.elf', '.bin', '.pool', '.ld'))
        script.write_text('SECTIONS { .text 0x150E7C9C : SUBALIGN(4) { *(.text) } '
                          '.rodata 0x800A1350 : SUBALIGN(4) { *(.rodata) *(.rdata) } }\n')
        targets = {'D_800BE9A4': 0x800BE9A4, 'func_150ADA68': 0x150ADA68, 'func_150ADA20': 0x150ADA20,
                   'func_150E75A0': 0x150E75A0, 'func_10010F30': 0x10010F30}
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_150E7C9C',
            *(f'--defsym={name}=0x{address:X}' for name, address in targets.items()), '-o', str(elf), str(obj)],
            check=True, capture_output=True)
        for section, path in (('.text', binary), ('.rodata', pool)):
            subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', section, str(elf), str(path)],
                           check=True, capture_output=True)
        words = list(struct.unpack('>' + 'I' * (binary.stat().st_size // 4), binary.read_bytes()))
        end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        retail = (self.root / 'conker/conker.us.bin').read_bytes()
        self.assertEqual(words[:end], list(struct.unpack('>212I', retail[0x11514C:0x11549C])))
        data = pool.read_bytes()
        self.assertEqual(data[:4], bytes.fromhex('3EDCEE77'))
        self.assertEqual(data[:4], retail[0x245E10:0x245E14])
        self.assertLessEqual(len(data), 16)
        self.assertTrue(all(byte == 0 for byte in data[4:]))


if __name__ == '__main__':
    unittest.main()
