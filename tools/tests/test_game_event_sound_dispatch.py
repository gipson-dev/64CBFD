import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests import test_game_random_curve_record as curve


class GameEventSoundDispatchTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_113D60.c').read_text()
        cls.body = re.search(r'void func_150E8930\(void\) \{\n.*?\n\}', source, re.S).group(0)
        cls.timer = re.search(r'void func_150E88C0\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';',
            source, re.S).group(0) for name in ('EventPair113D60', 'RandomPacket113D60'))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = ('typedef signed char s8; typedef unsigned char u8; typedef short s16; '
                     'typedef unsigned short u16; typedef int s32; typedef unsigned int u32; '
                     'typedef float f32;\n#define NULL ((void *)0)\n')
        cls.declarations = '''
extern s32 D_80088A80[4];
extern u8 D_800BE9EB;
extern u8 *D_800DCDC4;
extern f32 D_800BE9A4, D_800A1378;
void func_15169260(void *, s32, s32, u8);
void func_15164F0C(u8, u8, s32, u8, s32);
s32 func_151D8868(void *, s32, s32, s32);
void func_150E8A80(void);
void func_150E90DC(void);
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_10010F30(s32, u16, u8, s16, u8);
'''
        cls.fixture = cls.types + cls.layouts + cls.declarations + r'''
s32 D_80088A80[4];
u8 D_800BE9EB;
u8 *D_800DCDC4;
f32 D_800BE9A4, D_800A1378;
static u8 head0[1], head1[1], record[64];
static u32 words[4];
static int integers, floats, pairCalls, eventCalls, packetCalls, firstCalls, secondCalls, soundCalls;
static int error, mutatePair, packetHead, firstMutation, secondClears;
static char trace[32];
static int traceLength, watchTimer;
static u32 bits(f32 value) { union { f32 f; u32 u; } w; w.f=value; return w.u; }
static f32 number(u32 value) { union { f32 f; u32 u; } w; w.u=value; return w.f; }
static void push(char code) { if(traceLength<31) trace[traceLength++]=code; else error=1; }
static int trace_is(const char *expected) {
    int i=0;
    while(expected[i]) { if(i>=traceLength || trace[i]!=expected[i]) return 0; i++; }
    return i==traceLength;
}
void func_15169260(void *data, s32 count, s32 payload, u8 kind) {
    EventPair113D60 *p=data;
    push('P'); pairCalls++;
    if(pairCalls!=1 || eventCalls || integers || count!=2 || payload || kind!=0x1B
       || p->first!=25 || p->second!=72 || data==(void *)D_80088A80) error=2;
    if(watchTimer && *(f32 *)(record+0x28)!=301) error=3;
    if(mutatePair) {
        D_80088A80[0]=777; D_80088A80[1]=888; D_800BE9EB=0xC7;
        if(p->first!=25 || p->second!=72) error=4;
        p->first=-9; p->second=-10;
        if(D_80088A80[0]!=777 || D_80088A80[1]!=888) error=5;
    }
}
void func_15164F0C(u8 kind, u8 index, s32 payload, u8 slot, s32 context) {
    push('E'); eventCalls++;
    if(pairCalls!=1 || eventCalls!=1 || integers || packetCalls || kind
       || index!=(mutatePair?0xC7:0xA5) || payload || slot!=255 || context!=1) error=6;
}
s32 func_150ADA20(void) {
    int i=integers++;
    push('I');
    if(i>=4 || pairCalls!=1 || eventCalls!=1) { error=7; return 0; }
    if((i<2 && packetCalls) || (i>=2 && (packetCalls!=1 || soundCalls!=i-2))) error=8;
    return (s32)words[i];
}
s32 func_151D8868(void *data, s32 a, s32 b, s32 c) {
    RandomPacket113D60 *p=data;
    push('T'); packetCalls++;
    if(packetCalls!=1 || integers!=2 || firstCalls || secondCalls || soundCalls
       || a || b!=255 || c!=1 || p->kind!=1 || p->duration!=(s16)(words[0]%21+20)
       || p->mode!=1 || p->count!=(u8)(words[1]%6+3) || p->index!=-1) error=9;
    if(packetHead>=0) D_800DCDC4=packetHead?head0:NULL;
    return -123;
}
void func_150E8A80(void) {
    push('A'); firstCalls++;
    if(firstCalls!=1 || !D_800DCDC4 || packetCalls!=1 || integers!=2 || secondCalls || soundCalls) error=10;
    if(firstMutation==1) D_800DCDC4=NULL;
    if(firstMutation==2) D_800DCDC4=head1;
}
void func_150E90DC(void) {
    push('B'); secondCalls++;
    if(firstCalls!=1 || secondCalls!=1 || !D_800DCDC4 || packetCalls!=1 || integers!=2 || soundCalls) error=11;
    if(firstMutation==2 && D_800DCDC4!=head1) error=12;
    if(secondClears) D_800DCDC4=NULL;
}
void func_10010F30(s32 id, u16 volume, u8 pan, s16 offset, u8 flags) {
    int i=soundCalls++;
    push('S');
    if(i>=2 || integers!=i+3 || packetCalls!=1 || id!=(i?0x4CD:0x4C8)
       || volume!=(i?0x5DC0:0x7FFF) || pan!=0x40 || flags
       || offset!=(s16)(0x200-(words[i+2]&0x400))) error=13;
}
f32 func_150ADA68(void) {
    push('F'); floats++;
    if(floats!=1 || pairCalls || integers) error=14;
    return 0.5f;
}
static void initialize(void) {
    int i;
    D_80088A80[0]=25; D_80088A80[1]=72; D_80088A80[2]=D_80088A80[3]=0;
    D_800BE9EB=0xA5; D_800DCDC4=NULL;
    words[0]=0xFFFFFFFF; words[1]=0x80000001; words[2]=0; words[3]=0xFFFFFFFF;
    integers=floats=pairCalls=eventCalls=packetCalls=firstCalls=secondCalls=soundCalls=0;
    error=mutatePair=firstMutation=secondClears=traceLength=watchTimer=0;
    packetHead=-1; D_800BE9A4=2; D_800A1378=200;
    for(i=0;i<64;i++) record[i]=0x5A;
}
static int complete(void) {
    return error || integers!=4 || pairCalls!=1 || eventCalls!=1 || packetCalls!=1 || soundCalls!=2;
}
''' + cls.body + '\n'

    def test_unsigned_packet_remainders_and_independent_sound_offsets(self):
        self.run_host(r'''
static u32 values[]={0,1,5,6,19,20,21,22,0x7FFFFFFF,0x80000000,0x80000001,0xFFFFFFFE,0xFFFFFFFF};
int a,b,flags;
for(a=0;a<13;a++) for(b=0;b<13;b++) for(flags=0;flags<4;flags++) {
    initialize(); words[0]=values[a]; words[1]=values[b];
    words[2]=(flags&1)?0xFFFFFFFF:0xFFFFFBFF;
    words[3]=(flags&2)?0x80000400:0x80000000;
    func_150E8930();
    if(complete() || firstCalls || secondCalls || !trace_is("PEIITISIS")) return 1;
}
''')

    def test_independent_list_gates_reload_after_first_callback(self):
        self.run_host(r'''
int mode, clears;
for(mode=0;mode<4;mode++) for(clears=0;clears<2;clears++) {
    initialize(); D_800DCDC4=mode?head0:NULL;
    firstMutation=mode==2?1:mode==3?2:0;
    secondClears=clears;
    func_150E8930();
    if(complete() || firstCalls!=(mode!=0) || secondCalls!=(mode==1 || mode==3)) return 1;
    if(!trace_is(mode==0?"PEIITISIS":mode==2?"PEIITAISIS":"PEIITABISIS")) return 2;
}
''')

    def test_pair_copy_and_post_submission_global_loads(self):
        self.run_host(r'''
int initial, published;
for(initial=0;initial<2;initial++) for(published=0;published<2;published++) {
    initialize(); mutatePair=1; D_800DCDC4=initial?head0:NULL; packetHead=published;
    func_150E8930();
    if(complete() || firstCalls!=published || secondCalls!=published
       || D_80088A80[0]!=777 || D_80088A80[1]!=888) return 1;
    if(!trace_is(published?"PEIITABISIS":"PEIITISIS")) return 2;
}
''')

    def test_actual_timer_caller_strict_gate_reset_and_record_fence(self):
        self.fixture += self.timer + '\n'
        self.run_host(r'''
static u32 timerWords[]={0x41200000,0x40000000,0x3F800000,0x7FC00000,0x7F800000,0xFF800000};
int i,j;
for(i=0;i<6;i++) {
    int fires=(i==2 || i==5);
    initialize(); *(f32 *)(record+0x28)=number(timerWords[i]); watchTimer=fires;
    func_150E88C0(record);
    if(fires) { if(complete() || floats!=1 || !trace_is("FPEIITISIS")) return 1; }
    else if(error || floats || integers || pairCalls || traceLength) return 2;
    if(i==0 && *(f32 *)(record+0x28)!=8) return 3;
    if(i==1 && *(f32 *)(record+0x28)!=0) return 4;
    if(fires && *(f32 *)(record+0x28)!=301) return 5;
    if(i==3 && *(f32 *)(record+0x28)==*(f32 *)(record+0x28)) return 6;
    for(j=0;j<64;j++) if((j<0x28 || j>=0x2C) && record[j]!=0x5A) return 7;
}
''')

    def test_retail_call_sequence_padding_and_caller_return(self):
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        retail = rom[0x115DE0:0x115F30]
        self.assertEqual(len(retail),336)
        calls = [((0x150E8930+i*4+4)&0xF0000000)|((word&0x3FFFFFF)<<2)
                 for i,(word,) in enumerate(struct.iter_unpack('>I',retail)) if word>>26==3]
        self.assertEqual(calls,[0x15169260,0x15164F0C,0x150ADA20,0x150ADA20,0x151D8868,
                               0x150E8A80,0x150E90DC,0x150ADA20,0x10010F30,0x150ADA20,0x10010F30])
        self.assertEqual(struct.unpack_from('>4I',rom,0xCAB98),
                         (0x0D43A24C,0,0x1000001E,0x8FA200C4))
        self.assertNotIn('packet.pad1',self.body)
        self.assertNotIn('packet.pad7',self.body)
        self.assertNotIn('arg0',self.body)
        self.assertEqual(struct.unpack_from('>4I',rom,0x22D540),(25,72,0,0))

    def test_ido_parent_and_timer_caller_direct_matches(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or shutil.which('mips-linux-gnu-ld') is None:
            self.skipTest('IDO/MIPS tools are unavailable')
        targets = {'D_80088A80':0x80088A80,'D_800BE9EB':0x800BE9EB,'D_800DCDC4':0x800DCDC4,
                   'D_800BE9A4':0x800BE9A4,'D_800A1378':0x800A1378,'func_15169260':0x15169260,
                   'func_15164F0C':0x15164F0C,'func_150ADA20':0x150ADA20,'func_151D8868':0x151D8868,
                   'func_150E8A80':0x150E8A80,'func_150E90DC':0x150E90DC,'func_10010F30':0x10010F30,
                   'func_150ADA68':0x150ADA68,'func_150E8930':0x150E8930}
        for name,body,address,start,end in (
                ('func_150E8930',self.body,0x150E8930,0x115DE0,0x115F30),
                ('func_150E88C0',self.timer,0x150E88C0,0x115D70,0x115DE0)):
            with self.subTest(function=name):
                source,obj,elf,binary,script=(self.path/(name+suffix)
                    for suffix in ('.c','.o','.elf','.bin','.ld'))
                source.write_text(self.types+self.layouts+self.declarations+
                                  'void func_150E8930(void);\n'+body+'\n')
                result=subprocess.run([str(compiler),'-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
                    '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32','-O2','-g3',
                    '-o',str(obj),str(source)],capture_output=True,text=True)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertEqual(result.stdout+result.stderr,'')
                script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n'%address)
                subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',name,
                    *(f'--defsym={symbol}=0x{value:X}' for symbol,value in targets.items() if symbol!=name),
                    '-o',str(elf),str(obj)],check=True,capture_output=True)
                subprocess.run(['mips-linux-gnu-objcopy','-O','binary','-j','.text',str(elf),str(binary)],
                               check=True,capture_output=True)
                words=list(struct.unpack('>'+'I'*(binary.stat().st_size//4),binary.read_bytes()))
                count=max(i for i,word in enumerate(words) if word==0x03E00008)+2
                body_bytes=binary.read_bytes()[:count*4]
                retail=(self.root/'conker/conker.us.bin').read_bytes()[start:end]
                self.assertEqual(body_bytes,retail)
                print(name,'direct words:',count,'sha256:',hashlib.sha256(body_bytes).hexdigest())


if __name__ == '__main__':
    unittest.main()
