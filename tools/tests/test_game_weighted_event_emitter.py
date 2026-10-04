import csv
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests import test_game_random_curve_record as curve


class GameWeightedEventEmitterTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root/'conker/src/game/generated_113D60.c').read_text()
        cls.body = re.search(r'void func_150E8B1C\([^;{}]+\) \{\n.*?\n\}',source,re.S).group(0)
        cls.creator = re.search(r'void func_150E8A80\(void\) \{\n.*?\n\}',source,re.S).group(0)
        cls.layouts = '\n'.join(re.search(r'typedef struct '+name+r' \{.*?\} '+name+';',
            source,re.S).group(0) for name in ('EventPayload113D60','WorldPosition113D60',
                                              'EventPositionPayload113D60','EventWeightNode113D60'))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = ('typedef signed char s8; typedef unsigned char u8; typedef short s16; '
                     'typedef unsigned short u16; typedef int s32; typedef unsigned int u32; '
                     'typedef float f32;\n#define NULL ((void *)0)\n')
        cls.declarations = '''
extern f32 D_800A137C, D_800A1380, D_800A1384, D_800A1388, D_800A138C;
extern f32 D_800BE9A4, D_800DCD90;
extern s32 D_800BE9E8;
extern u8 *D_800DCDC4;
f32 func_150ADA68(void);
s32 func_150ADA20(void);
f32 *func_15144B34(s32);
void func_1514470C(void *, void *);
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);
'''
        cls.fixture = cls.types+cls.layouts+cls.declarations+r'''
f32 D_800A137C, D_800A1380, D_800A1384, D_800A1388, D_800A138C;
f32 D_800BE9A4, D_800DCD90;
s32 D_800BE9E8;
u8 *D_800DCDC4;
static union { u32 alignment; u8 bytes[64]; } record, children[8];
static EventWeightNode113D60 nodes[3];
static u8 descriptors[3][16];
static f32 origin[3], points[3][3], expectedPosition[3], fractions[16];
static u32 integers[16], expectedFirst, expectedSecond;
static u32 expectedChildren[8][6], expectedBase, expectedVariation;
static u8 expectedSlot, expectedContext;
static int floatCalls, integerCalls, originCalls, pointCalls, allocations, copies, creatorCalls;
static int selected[8], copied[8], error, failures, mutateInitial, mutateSelection, mutateConstants;
static int mutateOrigin, mutateProgress, mutateMetadata;
static char trace[64];
static int traceLength;
static u32 bits(f32 value) { union { f32 f; u32 u; } w; w.f=value; return w.u; }
static f32 number(u32 value) { union { f32 f; u32 u; } w; w.u=value; return w.f; }
static EventPayload113D60 *state(void) { return (EventPayload113D60 *)(record.bytes+0x28); }
static void push(char c) { if(traceLength<63) trace[traceLength++]=c; else error=1; }
static int trace_is(const char *s) {
    int i=0;
    while(s[i]) { if(i>=traceLength || trace[i]!=s[i]) return 0; i++; }
    return i==traceLength;
}
f32 *func_15144B34(s32 player) {
    push('O'); originCalls++;
    if(originCalls!=1 || floatCalls || player!=(s32)0x80000001) error=2;
    return origin;
}
f32 func_150ADA68(void) {
    int i=floatCalls++;
    push('F');
    if(i>=16 || originCalls!=1) { error=3; return 0; }
    if(!i && mutateInitial) {
        state()->field00=0.25f; state()->field04=0.5f; state()->field08=0.5f;
        expectedBase=bits(0.25f); expectedVariation=bits(0.5f);
        D_800BE9A4=0.5f; D_800DCD90=4; D_800BE9E8=77;
    }
    if(i && mutateSelection) {
        int k=i==1?1:0;
        D_800DCD90=i==1?8:2; nodes[k].weight=D_800DCD90;
        nodes[k].next=NULL; D_800DCDC4=(u8 *)&nodes[k];
    }
    if(i && mutateConstants) { D_800A1384=99; D_800A1388=100; D_800A138C=0; }
    return fractions[i];
}
s32 func_150ADA20(void) {
    int i=integerCalls++;
    push('I');
    if(i>=16) { error=4; return 0; }
    if(mutateMetadata) {
        record.bytes[0xC]=expectedSlot=0xC7; record.bytes[1]=expectedContext=0x81;
    }
    return (s32)integers[i];
}
void func_1514470C(void *descriptor, void *output) {
    int k=descriptor==descriptors[0]?0:descriptor==descriptors[1]?1:2, i;
    f32 *p=output;
    push('P');
    if(descriptor!=descriptors[k] || pointCalls>=8 || floatCalls!=pointCalls+2) error=5;
    selected[pointCalls++]=k;
    for(i=0;i<3;i++) p[i]=expectedPosition[i]=points[k][i];
    if(mutateOrigin && pointCalls==1) origin[0]=3;
}
void *func_15149130(s16 duration, s8 index, s8 kind, s8 source, u8 active,
                   u8 mode, s32 bytes, u8 slot, s32 context) {
    int i=allocations;
    if(kind==0x33) {
        push('G'); creatorCalls++;
        if(creatorCalls!=1 || originCalls || duration!=(s16)(integers[integerCalls-1]%41+30)
           || index!=-1 || source!=-1 || active!=1 || mode || bytes!=12 || slot!=255 || context!=1) error=6;
        record.bytes[0xC]=expectedSlot=slot; record.bytes[1]=expectedContext=(u8)context;
        return record.bytes;
    }
    push('A'); allocations++;
    if(i>=8 || kind!=0x34 || index!=-1 || source!=-1 || active!=1 || mode || bytes!=24
       || slot!=expectedSlot || context!=expectedContext
       || duration!=(s16)(integers[integerCalls-1]%13+5)) error=7;
    if(mutateProgress && i==0) state()->field08=3.5f;
    return failures&(1<<i)?NULL:children[i].bytes;
}
void *memcpy(void *destination, const void *source, u32 bytes) {
    const u32 *p=source;
    u32 i;
    push('C'); copies++;
    if(destination==record.bytes+0x28) {
        if(bytes!=12 || creatorCalls!=1 || p[0]!=bits(D_800A137C) || p[1]!=bits(D_800A1380) || p[2]) error=8;
        expectedBase=bits(D_800A137C); expectedVariation=bits(D_800A1380);
    } else {
        int k=allocations-1;
        if(k<0 || k>=8) { error=9; return destination; }
        copied[k]++;
        if(destination!=children[k].bytes+0x28 || bytes!=24 || copied[k]!=1 || failures&(1<<k)
           || p[0]!=bits(expectedPosition[0]) || p[1]!=bits(expectedPosition[1])
           || p[2]!=bits(expectedPosition[2]) || p[3]!=expectedFirst || p[4]!=expectedSecond || p[5]) error=10;
        for(i=0;i<3;i++) expectedChildren[k][i]=bits(expectedPosition[i]);
        expectedChildren[k][3]=expectedFirst; expectedChildren[k][4]=expectedSecond;
        expectedChildren[k][5]=0;
    }
    for(i=0;i<bytes;i++) ((u8 *)destination)[i]=((const u8 *)source)[i];
    return destination;
}
static void initialize(void) {
    int i,k;
    floatCalls=integerCalls=originCalls=pointCalls=allocations=copies=creatorCalls=error=traceLength=0;
    failures=mutateInitial=mutateSelection=mutateConstants=mutateOrigin=mutateProgress=mutateMetadata=0;
    D_800BE9E8=(s32)0x80000001; D_800BE9A4=1; D_800DCD90=10;
    D_800A137C=number(0x3400D959); D_800A1380=number(0x34ABCC77);
    D_800A1384=number(0x3F85F40A); D_800A1388=number(0x3EA25D8D); D_800A138C=4;
    expectedFirst=bits(D_800A1388); expectedSecond=bits(D_800A1384);
    for(i=0;i<64;i++) record.bytes[i]=0xA5;
    record.bytes[0xC]=expectedSlot=0xC3; record.bytes[1]=expectedContext=0x91;
    expectedBase=expectedVariation=0;
    state()->field00=state()->field04=0; state()->field08=0.5f;
    for(k=0;k<8;k++) { copied[k]=selected[k]=0; for(i=0;i<64;i++) children[k].bytes[i]=0xA5; }
    for(i=0;i<16;i++) { fractions[i]=0; integers[i]=(u32)i; }
    for(k=0;k<3;k++) {
        nodes[k].descriptor=descriptors[k]; nodes[k].field04=(s32)0xA5A5A5A5;
        nodes[k].weight=k?7:3; nodes[k].next=k?NULL:&nodes[1];
        for(i=0;i<3;i++) points[k][i]=0;
    }
    for(i=0;i<3;i++) origin[i]=0;
    D_800DCDC4=(u8 *)&nodes[0];
}
static int fences(void) {
    int i,k;
    if(record.bytes[0xC]!=expectedSlot || record.bytes[1]!=expectedContext
       || bits(state()->field00)!=expectedBase || bits(state()->field04)!=expectedVariation) return 3;
    for(i=0;i<64;i++) if(i!=1 && i!=0xC && (i<0x28 || i>=0x34) && record.bytes[i]!=0xA5) return 1;
    for(k=0;k<8;k++) for(i=0;i<64;i++) {
        u8 expected=copied[k] && i>=0x28 && i<0x40?((u8 *)expectedChildren[k])[i-0x28]:0xA5;
        if(children[k].bytes[i]!=expected) return 2;
    }
    return 0;
}
''' + cls.creator+'\n'+cls.body+'\n'

    def test_rate_order_strict_gate_and_nonfinite_no_head_paths(self):
        self.run_host(r'''
static u32 values[]={0,0x3E800000,0x3F000000,0x3F800000,0xBF800000,0x7FC12345,0x7F800000,0xFF800000};
static f32 progress[]={-1,0,0.5f,1};
int i,j;
for(i=0;i<8;i++) for(j=0;j<4;j++) {
    f32 expected;
    initialize(); D_800DCDC4=NULL; D_800BE9A4=0;
    state()->field00=0.25f; state()->field04=0.5f; state()->field08=progress[j];
    expectedBase=bits(0.25f); expectedVariation=bits(0.5f);
    fractions[0]=number(values[i]);
    expected=progress[j]+((0.25f+fractions[0]*0.5f)*0.0f)*10.0f;
    func_150E8B1C(record.bytes);
    if(error || originCalls!=1 || floatCalls!=1 || pointCalls || integerCalls || allocations || copies
       || !trace_is("OF") || fences()) return 1;
    if(expected==expected) { if(bits(state()->field08)!=bits(expected)) return 2; }
    else if(state()->field08==state()->field08) return 3;
}
''')

    def test_multi_hop_and_zero_weight_strict_boundary_selection(self):
        self.run_host(r'''
static f32 fractions0[]={0,0.2f,0.25f,0.5f,0.6f,1};
static f32 fractions1[]={0,0.1f,0.3f,0.30000004f,0.6f,1};
static int expected0[]={0,0,1,1,2,2}, expected1[]={0,1,1,2,2,2};
int mode,i;
for(mode=0;mode<2;mode++) for(i=0;i<6;i++) {
    initialize(); state()->field08=2;
    nodes[0].weight=mode?0:2; nodes[1].weight=3; nodes[2].weight=mode?7:5;
    nodes[0].next=&nodes[1]; nodes[1].next=&nodes[2]; nodes[2].next=NULL;
    fractions[1]=mode?fractions1[i]:fractions0[i];
    func_150E8B1C(record.bytes);
    if(error || pointCalls!=1 || selected[0]!=(mode?expected1[i]:expected0[i])
       || floatCalls!=2 || allocations!=1 || copies!=1 || state()->field08!=1 || fences()) return 1;
}
''')

    def test_weight_boundaries_unsigned_lifetimes_and_allocation_failure(self):
        self.run_host(r'''
static f32 targets[]={0,0.25f,0.3f,0.30000004f,0.9f,1,-1};
static u32 words[]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,0x7FFFFFFF,0x80000000,0xFFFFFFFF};
int i,j,failed;
for(i=0;i<8;i++) for(j=0;j<17;j++) for(failed=0;failed<2;failed++) {
    f32 target=i<7?targets[i]:number(0x7FC00000);
    int expected=3.0f<target*10.0f;
    initialize(); state()->field08=2; fractions[1]=target; integers[0]=words[j]; failures=failed;
    func_150E8B1C(record.bytes);
    if(error || pointCalls!=1 || selected[0]!=expected || floatCalls!=2 || integerCalls!=1
       || allocations!=1 || copies!=!failed || copied[0]!=!failed || state()->field08!=1
       || !trace_is(failed?"OFFPIA":"OFFPIAC") || fences()) return 1;
}
''')

    def test_strict_accumulator_and_distance_consumption(self):
        self.run_host(r'''
static f32 progress[]={1,1.125f,2,2.125f,3,3.125f,5};
static int counts[]={0,1,1,2,2,3,4};
static f32 distances[]={0,1.999f,2,2.001f};
int i,j,k;
for(i=0;i<7;i++) for(j=0;j<6;j++) {
    int near=j<2;
    initialize(); state()->field08=progress[i];
    points[0][0]=j<4?distances[j]:number(j==4?0x7FC00000:0x7F800000);
    func_150E8B1C(record.bytes);
    if(error || floatCalls!=counts[i]+1 || pointCalls!=counts[i]
       || integerCalls!=counts[i]*near || allocations!=counts[i]*near
       || copies!=counts[i]*near || state()->field08!=progress[i]-(f32)counts[i] || fences()) return 1;
    for(k=0;k<counts[i];k++) if(selected[k]!=0) return 2;
}
''')

    def test_rate_fields_are_loaded_after_initial_float_callback(self):
        self.run_host(r'''
initialize(); mutateInitial=1; fractions[0]=0.25f;
func_150E8B1C(record.bytes);
if(error || originCalls!=1 || floatCalls!=2 || pointCalls!=1 || allocations!=1 || copies!=1
   || state()->field00!=0.25f || state()->field04!=0.5f || state()->field08!=0.25f
   || D_800BE9E8!=77 || !trace_is("OFFPIAC") || fences()) return 1;
''')

    def test_each_selection_reloads_head_and_total_but_keeps_parameter_snapshot(self):
        self.run_host(r'''
initialize(); state()->field08=3; fractions[1]=fractions[2]=0.5f;
mutateSelection=mutateConstants=1;
func_150E8B1C(record.bytes);
if(error || floatCalls!=3 || pointCalls!=2 || selected[0]!=1 || selected[1]!=0
   || integerCalls!=2 || allocations!=2 || copies!=2 || state()->field08!=1
   || D_800DCDC4!=(u8 *)&nodes[0] || D_800DCD90!=2 || D_800A138C!=0
   || !trace_is("OFFPIACFPIAC") || fences()) return 1;
''')

    def test_origin_progress_and_metadata_reload_across_callbacks(self):
        self.run_host(r'''
int failed;
for(failed=0;failed<8;failed++) {
    initialize(); state()->field08=2; points[0][0]=3;
    mutateOrigin=mutateProgress=mutateMetadata=1; failures=failed;
    func_150E8B1C(record.bytes);
    if(error || pointCalls!=3 || floatCalls!=4 || integerCalls!=3 || allocations!=3
       || copies!=3-((failed&1)!=0)-((failed&2)!=0)-((failed&4)!=0)
       || state()->field08!=0.5f || record.bytes[0xC]!=0xC7 || record.bytes[1]!=0x81 || fences()) return 1;
}
''')

    def test_actual_creator_to_updater_payload_and_two_children(self):
        self.run_host(r'''
f32 expected;
EventWeightNode113D60 node;
EventPositionPayload113D60 payload;
if(sizeof(node)!=16 || sizeof(payload)!=24 || sizeof(EventPayload113D60)!=12
   || (u8 *)&node.weight-(u8 *)&node!=8 || (u8 *)&node.next-(u8 *)&node!=12
   || (u8 *)&payload.parameters-(u8 *)&payload!=12) return 2;
initialize(); D_800DCD90=10000000; nodes[0].weight=nodes[1].weight=5000000;
fractions[0]=0.5f; fractions[1]=0; fractions[2]=1;
func_150E8A80();
expected=((D_800A137C+0.5f*D_800A1380)*D_800BE9A4)*D_800DCD90;
expected-=1; expected-=1;
func_150E8B1C(record.bytes);
if(error || creatorCalls!=1 || floatCalls!=3 || pointCalls!=2 || selected[0]!=0 || selected[1]!=1
   || integerCalls!=3 || allocations!=2 || copies!=3 || bits(state()->field08)!=bits(expected)
   || !trace_is("IGCOFFPIACFPIAC") || fences()) return 1;
''')

    def test_retail_callback_mapping_position_pointer_and_literal_contracts(self):
        rom=(self.root/'conker/conker.us.bin').read_bytes()
        self.assertEqual(struct.unpack_from('>2I',rom,0x22F074),(0x150E8B1C,0x150E8D5C))
        self.assertEqual(0x8008A4E8+0x33*4,0x8008A5B4)
        self.assertEqual(struct.unpack_from('>3I',rom,0x245E44),(0x3F85F40A,0x3EA25D8D,0x4A45C100))
        helper=(self.root/'conker/asm/nonmatchings/game_16EE20/func_1514470C.s').read_text()
        self.assertIn('lh         $t7, 0x8($s0)',helper)
        self.assertIn('swc1       $f6, 0x8($s1)',helper)
        retail=rom[0x115FCC:0x11620C]
        self.assertEqual(len(retail),576)
        words=struct.unpack('>144I',retail)
        self.assertEqual(words[0],0x27BDFF38)
        self.assertEqual(words[-2:],(0x03E00008,0x27BD00C8))
        calls=[((0x150E8B1C+i*4+4)&0xF0000000)|((word&0x3FFFFFF)<<2)
               for i,word in enumerate(words) if word>>26==3]
        self.assertEqual(calls,[0x15144B34,0x150ADA68,0x150ADA68,0x1514470C,
                               0x150ADA20,0x15149130,0x10022EC0])
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(r['function']=='func_150E8B1C' for r in csv.DictReader(source)))

    def test_ido_complete_slot_footprint(self):
        compiler=self.root/'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(n) is None for n in
                ('mips-linux-gnu-ld','mips-linux-gnu-objcopy')):
            self.skipTest('IDO/MIPS tools are unavailable')
        source,obj,elf,binary,script=(self.path/('weighted'+s) for s in ('.c','.o','.elf','.bin','.ld'))
        source.write_text(self.types+self.layouts+self.declarations+self.body+'\n')
        result=subprocess.run([str(compiler),'-c','-32','-G','0','-Xfullwarn','-Xcpluscomm',
            '-signed','-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32','-O2','-g3',
            '-o',str(obj),str(source)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(result.stdout+result.stderr,'')
        script.write_text('SECTIONS { .text 0x150E8B1C : SUBALIGN(4) { *(.text) } }\n')
        targets={name:int(name[2:],16) for name in ('D_800BE9E8','D_800BE9A4','D_800DCD90',
                  'D_800DCDC4','D_800A1384','D_800A1388','D_800A138C')}
        targets.update({name:int(name[5:],16) for name in
            ('func_15144B34','func_150ADA68','func_1514470C','func_150ADA20','func_15149130')})
        targets['memcpy']=0x10022EC0
        subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e','func_150E8B1C',
            *(f'--defsym={name}=0x{value:X}' for name,value in targets.items()),
            '-o',str(elf),str(obj)],check=True,capture_output=True)
        subprocess.run(['mips-linux-gnu-objcopy','-O','binary','-j','.text',str(elf),str(binary)],
                       check=True,capture_output=True)
        data=binary.read_bytes(); words=struct.unpack('>'+'I'*(len(data)//4),data)
        count=max(i for i,word in enumerate(words) if word==0x03E00008)+2
        self.assertEqual(count,144)
        self.assertEqual(words[0],0x27BDFF38)
        self.assertEqual(data[count*4:],bytes(len(data)-count*4))
        retail=(self.root/'conker/conker.us.bin').read_bytes()[0x115FCC:0x11620C]
        padded=data[:count*4]+bytes(576-count*4)
        differences=sum(a!=b for a,b in zip(struct.unpack('>144I',padded),struct.unpack('>144I',retail)))
        self.assertEqual(differences,44)
        print('weighted emitter slot:',{'body_words':count,'slot_words':144,
              'frame_bytes':0x10000-(words[0]&0xFFFF),'different_words':differences})


if __name__ == '__main__':
    unittest.main()
