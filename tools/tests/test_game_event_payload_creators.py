import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests import test_game_random_curve_record as curve


class GameEventPayloadCreatorTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_113D60.c').read_text()
        cls.bodies = {name: re.search(r'void ' + name + r'\(void\) \{\n.*?\n\}',
                                     source, re.S).group(0)
                      for name in ('func_150E8A80', 'func_150E90DC', 'func_150E8930')}
        cls.timer = re.search(r'void func_150E88C0\([^;{}]+\) \{\n.*?\n\}',
                              source, re.S).group(0)
        cls.layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';',
            source, re.S).group(0) for name in
            ('EventPair113D60', 'RandomPacket113D60', 'EventPayload113D60'))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = ('typedef signed char s8; typedef unsigned char u8; typedef short s16; '
                     'typedef unsigned short u16; typedef int s32; typedef unsigned int u32; '
                     'typedef float f32;\n#define NULL ((void *)0)\n')
        cls.declarations = '''
extern f32 D_800A137C, D_800A1380, D_800A13B0, D_800A13B4;
extern f32 D_800BE9A4, D_800A1378;
extern s32 D_80088A80[4];
extern u8 D_800BE9EB;
extern u8 *D_800DCDC4;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);
void func_15169260(void *, s32, s32, u8);
void func_15164F0C(u8, u8, s32, u8, s32);
s32 func_151D8868(void *, s32, s32, s32);
void func_10010F30(s32, u16, u8, s16, u8);
void func_150E8A80(void);
void func_150E90DC(void);
void func_150E8930(void);
'''
        cls.fixture = cls.types + cls.layouts + cls.declarations + r'''
f32 D_800A137C, D_800A1380, D_800A13B0, D_800A13B4;
f32 D_800BE9A4, D_800A1378;
s32 D_80088A80[4];
u8 D_800BE9EB, *D_800DCDC4;
static union { u32 alignment; u8 bytes[64]; } storage[2], timer;
static u8 head0[1], head1[1];
static u32 words[6], payload[2][3];
static int integers, floats, allocations, copies, pairCalls, eventCalls, packetCalls, sounds;
static int seen[2], copied[2], failures, mutations, firstMutation, secondClears;
static int error, connected, publication, watchTimer;
static char trace[32];
static int traceLength;
static u32 bits(f32 value) { union { f32 f; u32 u; } w; w.f=value; return w.u; }
static f32 number(u32 value) { union { f32 f; u32 u; } w; w.u=value; return w.f; }
static void push(char code) { if(traceLength<31) trace[traceLength++]=code; else error=1; }
static int trace_is(const char *expected) {
    int i=0;
    while(expected[i]) { if(i>=traceLength || trace[i]!=expected[i]) return 0; i++; }
    return i==traceLength;
}
static void change_constants(void) {
    D_800A137C=11; D_800A1380=22; D_800A13B0=33; D_800A13B4=44;
}
s32 func_150ADA20(void) {
    int i=integers++;
    push('I');
    if(i>=6 || (connected && (pairCalls!=1 || eventCalls!=1))) { error=2; return 0; }
    if(mutations&1) change_constants();
    return (s32)words[i];
}
void *func_15149130(s16 duration, s8 index, s8 kind, s8 source, u8 active,
                   u8 mode, s32 bytes, u8 slot, s32 context) {
    int k=kind==0x33?0:1;
    push(k?'B':'A'); allocations++; seen[k]++;
    if((kind!=0x33 && kind!=0x36) || seen[k]!=1 || !integers || copies>allocations
       || duration!=(s16)(words[integers-1]%(k?26u:41u)+(k?5:30))
       || index!=-1 || source!=-1 || active!=1 || mode || bytes!=12 || slot!=255 || context!=1) error=3;
    if(connected && (packetCalls!=1 || !D_800DCDC4 || sounds)) error=4;
    if(connected && k && firstMutation==2 && D_800DCDC4!=head1) error=5;
    if(mutations&2) change_constants();
    if(connected && !k && firstMutation==1) D_800DCDC4=NULL;
    if(connected && !k && firstMutation==2) D_800DCDC4=head1;
    if(connected && k && secondClears) D_800DCDC4=NULL;
    return failures&(1<<k)?NULL:storage[k].bytes;
}
void *memcpy(void *destination, const void *source, u32 bytes) {
    int k=destination==storage[0].bytes+0x28?0:1;
    u32 i;
    push('C'); copies++; copied[k]++;
    if(destination!=storage[k].bytes+0x28 || bytes!=12 || seen[k]!=1 || copied[k]!=1
       || failures&(1<<k) || *(const u32 *)source!=payload[k][0]
       || *((const u32 *)source+1)!=payload[k][1] || *((const u32 *)source+2)!=0) error=6;
    for(i=0;i<bytes;i++) ((u8 *)destination)[i]=((const u8 *)source)[i];
    return destination;
}
void func_15169260(void *data, s32 count, s32 payloadValue, u8 kind) {
    EventPair113D60 *p=data;
    push('P'); pairCalls++;
    if(!connected || pairCalls!=1 || integers || count!=2 || payloadValue || kind!=0x1B
       || p->first!=25 || p->second!=72 || data==(void *)D_80088A80) error=7;
    if(watchTimer && *(f32 *)(timer.bytes+0x28)!=301) error=8;
}
void func_15164F0C(u8 kind, u8 index, s32 payloadValue, u8 slot, s32 context) {
    push('E'); eventCalls++;
    if(pairCalls!=1 || eventCalls!=1 || integers || kind || index!=0xA5
       || payloadValue || slot!=255 || context!=1) error=9;
}
s32 func_151D8868(void *data, s32 a, s32 b, s32 c) {
    RandomPacket113D60 *p=data;
    push('T'); packetCalls++;
    if(packetCalls!=1 || integers!=2 || allocations || sounds || a || b!=255 || c!=1
       || p->kind!=1 || p->duration!=(s16)(words[0]%21+20) || p->mode!=1
       || p->count!=(u8)(words[1]%6+3) || p->index!=-1) error=10;
    if(publication>=0) D_800DCDC4=publication?head0:NULL;
    return -123;
}
void func_10010F30(s32 id, u16 volume, u8 pan, s16 offset, u8 flags) {
    int i=sounds++;
    push('S');
    if(i>=2 || packetCalls!=1 || integers!=3+allocations+i
       || id!=(i?0x4CD:0x4C8) || volume!=(i?0x5DC0:0x7FFF) || pan!=0x40 || flags
       || offset!=(s16)(0x200-(words[integers-1]&0x400))) error=11;
}
f32 func_150ADA68(void) { push('F'); floats++; return 0.5f; }
static void initialize(void) {
    int i,k;
    integers=floats=allocations=copies=pairCalls=eventCalls=packetCalls=sounds=0;
    failures=mutations=firstMutation=secondClears=error=connected=watchTimer=traceLength=0;
    publication=-1; D_800DCDC4=NULL; D_800BE9EB=0xA5;
    D_80088A80[0]=25; D_80088A80[1]=72; D_80088A80[2]=D_80088A80[3]=0;
    D_800BE9A4=2; D_800A1378=200;
    words[0]=0xFFFFFFFF; words[1]=0x80000001; words[2]=0x400;
    words[3]=0x80000000; words[4]=0x80000400; words[5]=0xFFFFFBFF;
    payload[0][0]=0x3400D959; payload[0][1]=0x34ABCC77; payload[0][2]=0;
    payload[1][0]=0x3456BF95; payload[1][1]=0x34210FB0; payload[1][2]=0;
    D_800A137C=number(payload[0][0]); D_800A1380=number(payload[0][1]);
    D_800A13B0=number(payload[1][0]); D_800A13B4=number(payload[1][1]);
    for(k=0;k<2;k++) {
        seen[k]=copied[k]=0;
        for(i=0;i<64;i++) storage[k].bytes[i]=0xA5;
    }
    for(i=0;i<64;i++) timer.bytes[i]=0x5A;
}
static void creator(int k) { if(k) func_150E90DC(); else func_150E8A80(); }
static int records_exact(int first, int second) {
    int k,i,called[2]; called[0]=first; called[1]=second;
    for(k=0;k<2;k++) {
        int success=called[k] && !(failures&(1<<k));
        if(seen[k]!=called[k] || copied[k]!=success) return 1;
        for(i=0;i<64;i++) {
            u8 expected=success && i>=0x28 && i<0x34?((u8 *)payload[k])[i-0x28]:0xA5;
            if(storage[k].bytes[i]!=expected) return 2;
        }
    }
    return 0;
}
static int connected_trace(int first, int second, int timerFired) {
    char expected[32];
    int n=0;
    if(timerFired) expected[n++]='F';
    expected[n++]='P'; expected[n++]='E'; expected[n++]='I'; expected[n++]='I'; expected[n++]='T';
    if(first) { expected[n++]='I'; expected[n++]='A'; if(!(failures&1)) expected[n++]='C'; }
    if(second) { expected[n++]='I'; expected[n++]='B'; if(!(failures&2)) expected[n++]='C'; }
    expected[n++]='I'; expected[n++]='S'; expected[n++]='I'; expected[n++]='S'; expected[n]=0;
    return trace_is(expected);
}
''' + '\n'.join(cls.bodies.values()) + '\n' + cls.timer + '\n'

    def test_unsigned_lifetime_residues_and_boundaries_with_record_fences(self):
        self.run_host(r'''
static u32 limits[]={0,1,25,26,40,41,0x7FFFFFFF,0x80000000,0x80000001,0xFFFFFFFE,0xFFFFFFFF};
int k,i;
for(k=0;k<2;k++) for(i=0;i<52;i++) {
    initialize(); words[0]=i<41?(u32)i:limits[i-41]; creator(k);
    if(error || integers!=1 || allocations!=1 || copies!=1 || records_exact(!k,k)
       || !trace_is(k?"IBC":"IAC")) return 1;
}
''')

    def test_allocation_failure_has_no_copy_or_output_write(self):
        self.run_host(r'''
int k,i;
for(k=0;k<2;k++) for(i=0;i<41;i++) {
    initialize(); words[0]=(u32)i; failures=1<<k; mutations=3; creator(k);
    if(error || integers!=1 || allocations!=1 || copies || records_exact(!k,k)
       || !trace_is(k?"IB":"IA")) return 1;
}
''')

    def test_float_payload_snapshot_precedes_rng_and_allocator_mutations(self):
        self.run_host(r'''
static u32 values[]={0,0x80000000,0x3F800000,0xBF800000,0x7FC12345,0x7F800000,0xFF800000};
int k,m,i;
for(k=0;k<2;k++) for(m=0;m<4;m++) for(i=0;i<7;i++) {
    initialize(); mutations=m;
    payload[k][0]=values[i]; payload[k][1]=values[(i+3)%7];
    if(k) { D_800A13B0=number(payload[k][0]); D_800A13B4=number(payload[k][1]); }
    else { D_800A137C=number(payload[k][0]); D_800A1380=number(payload[k][1]); }
    creator(k);
    if(error || integers!=1 || allocations!=1 || copies!=1 || records_exact(!k,k)) return 1;
}
''')

    def test_actual_dispatcher_creator_chain_head_publication_mutation_and_failures(self):
        self.run_host(r'''
int initial,published,mutation,failed,clears;
for(initial=0;initial<2;initial++) for(published=-1;published<2;published++)
for(mutation=0;mutation<3;mutation++) for(failed=0;failed<4;failed++) for(clears=0;clears<2;clears++) {
    int first=published<0?initial:published;
    int second=first && mutation!=1;
    initialize(); connected=1; D_800DCDC4=initial?head0:NULL;
    publication=published; firstMutation=mutation; failures=failed; secondClears=clears;
    func_150E8930();
    if(error || pairCalls!=1 || eventCalls!=1 || packetCalls!=1 || sounds!=2
       || integers!=4+first+second || allocations!=first+second
       || records_exact(first,second) || !connected_trace(first,second,0)) return 1;
    if(first && mutation==1 && D_800DCDC4) return 2;
    if(second && clears && D_800DCDC4) return 3;
    if(second && !clears && D_800DCDC4!=(mutation==2?head1:head0)) return 4;
}
''')

    def test_actual_timer_dispatcher_both_creators_and_sound_rng_positions(self):
        self.run_host(r'''
static u32 timers[]={0x41200000,0x40000000,0x3F800000,0x7FC00000,0x7F800000,0xFF800000};
int i,failed,j;
for(i=0;i<6;i++) for(failed=0;failed<4;failed++) {
    int fires=i==2 || i==5;
    initialize(); connected=1; D_800DCDC4=head0; failures=failed; watchTimer=fires;
    *(f32 *)(timer.bytes+0x28)=number(timers[i]); func_150E88C0(timer.bytes);
    if(fires) {
        if(error || floats!=1 || integers!=6 || allocations!=2 || sounds!=2
           || records_exact(1,1) || !connected_trace(1,1,1)
           || *(f32 *)(timer.bytes+0x28)!=301) return 1;
    } else if(error || floats || integers || allocations || sounds || traceLength
              || records_exact(0,0)) return 2;
    for(j=0;j<64;j++) if((j<0x28 || j>=0x2C) && timer.bytes[j]!=0x5A) return 3;
}
''')

    def test_retail_slots_literals_calls_and_absence_of_guards(self):
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        for address,start in ((0x150E8A80,0x115F30),(0x150E90DC,0x11658C)):
            words = struct.unpack_from('>39I',rom,start)
            self.assertEqual(words[:2],(0x27BDFFB8,0xAFBF002C))
            self.assertEqual(words[-4:],(0x8FBF002C,0x27BD0048,0x03E00008,0))
            calls=[((address+i*4+4)&0xF0000000)|((word&0x3FFFFFF)<<2)
                   for i,word in enumerate(words) if word>>26==3]
            self.assertEqual(calls,[0x150ADA20,0x15149130,0x10022EC0])
        self.assertEqual(struct.unpack_from('>2I',rom,0x245E3C),(0x3400D959,0x34ABCC77))
        self.assertEqual(struct.unpack_from('>2I',rom,0x245E70),(0x3456BF95,0x34210FB0))
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as source:
            rows=list(csv.DictReader(source))
        self.assertFalse(any(row['function'] in ('func_150E8A80','func_150E90DC') for row in rows))

    def test_ido_both_creators_direct_match_all_39_words(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(name) is None for name in
                ('mips-linux-gnu-ld','mips-linux-gnu-objcopy')):
            self.skipTest('IDO/MIPS tools are unavailable')
        targets={'D_800A137C':0x800A137C,'D_800A1380':0x800A1380,
                 'D_800A13B0':0x800A13B0,'D_800A13B4':0x800A13B4,
                 'func_150ADA20':0x150ADA20,'func_15149130':0x15149130,'memcpy':0x10022EC0}
        for name,address,start in (('func_150E8A80',0x150E8A80,0x115F30),
                                   ('func_150E90DC',0x150E90DC,0x11658C)):
            with self.subTest(function=name):
                source,obj,elf,binary,script=(self.path/(name+suffix)
                    for suffix in ('.c','.o','.elf','.bin','.ld'))
                source.write_text(self.types+self.layouts+self.declarations+self.bodies[name]+'\n')
                result=subprocess.run([str(compiler),'-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
                    '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32','-O2','-g3',
                    '-o',str(obj),str(source)],capture_output=True,text=True)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertEqual(result.stdout+result.stderr,'')
                script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n'%address)
                subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',name,
                    *(f'--defsym={symbol}=0x{value:X}' for symbol,value in targets.items()),
                    '-o',str(elf),str(obj)],check=True,capture_output=True)
                subprocess.run(['mips-linux-gnu-objcopy','-O','binary','-j','.text',str(elf),str(binary)],
                               check=True,capture_output=True)
                data=binary.read_bytes()
                words=list(struct.unpack('>'+'I'*(len(data)//4),data))
                count=max(i for i,word in enumerate(words) if word==0x03E00008)+2
                self.assertEqual(count,39)
                retail=(self.root/'conker/conker.us.bin').read_bytes()[start:start+156]
                expected=struct.unpack('>39I',retail)
                differences=[(i*4,'%08X'%actual,'%08X'%wanted)
                             for i,(actual,wanted) in enumerate(zip(words[:count],expected))
                             if actual!=wanted]
                self.assertEqual(differences,[])
                self.assertEqual(data[:count*4],retail)
                self.assertEqual(data[count*4:],bytes(len(data)-count*4))
                print(name,'direct words:',count,'sha256:',hashlib.sha256(data[:count*4]).hexdigest())


if __name__ == '__main__':
    unittest.main()
