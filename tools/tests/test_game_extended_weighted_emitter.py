"""Recovered code-0x36 emitter; opaque SDK boundaries and bounded actual helpers."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools import match_progress
from tools.patch_generated_slice_ld import load_game_data_layout
from tools.tests import test_game_random_curve_record as curve


class GameExtendedWeightedEmitterTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_113D60.c').read_text()
        cls.body = re.search(r'void func_150E9178\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.creator = re.search(r'void func_150E90DC\(void\) \{\n.*?\n\}', source, re.S).group(0)
        cls.layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';',
                                         source, re.S).group(0) for name in
            ('EventPayload113D60', 'WorldPosition113D60', 'EventPositionPayload113D60',
             'ExtendedEventPositionPayload113D60', 'EventWeightNode113D60'))
        cls.types = ('typedef unsigned char u8; typedef signed char s8; typedef short s16; '
                     'typedef int s32; typedef unsigned int u32; typedef float f32;\n'
                     'typedef struct { f32 x,y,z; } vertex;\n#define NULL ((void *)0)\n')
        cls.declarations = '''
extern f32 D_800A13B0, D_800A13B4, D_800A13B8, D_800A13BC, D_800A13C0, D_800A13C4;
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
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        first, address, _, _ = load_game_data_layout(cls.root / 'conker')
        cls.literal_words = struct.unpack_from('>6I', cls.rom, first + 0x800A13B0 - address)
        cls.table_words = struct.unpack_from('>65I', cls.rom, first + 0x8009A220 - address)
        cls.fixture = cls.types + cls.layouts + cls.declarations + (
            'static const u32 literalWords[6]={' + ','.join('0x%08Xu' % w for w in cls.literal_words) + '};\n'
        ) + r'''
f32 D_800A13B0, D_800A13B4, D_800A13B8, D_800A13BC, D_800A13C0, D_800A13C4;
f32 D_800BE9A4, D_800DCD90;
s32 D_800BE9E8;
u8 *D_800DCDC4;
static union { u32 alignment; u8 bytes[64]; } record;
static union { u32 alignment; u8 bytes[112]; } children[8];
static EventWeightNode113D60 nodes[3];
static u8 descriptors[3][64];
static f32 origin[3], points[3][3], expectedPosition[3], samples[64];
static u32 integers[32], expectedFirst, expectedSecond, expectedParameter;
static u32 expectedBase, expectedVariation;
static u8 expectedSlot, expectedContext;
static int originCalls, floatCalls, selectionCalls, pointCalls, integerCalls, allocations, copies, creatorCalls;
static int error, failures, selected[8], copied[8], mutateInitial, mutateSelection, mutateConstants;
static int mutateOrigin, mutateProgress, mutateCopyProgress, mutateMetadata, poisonPayload, inPoint;
static void (*actualWriter)(void *, void *);
static char trace[256];
static int traceLength;
static u32 bits(f32 value) { union { f32 f; u32 u; } v; v.f=value; return v.u; }
static f32 number(u32 value) { union { f32 f; u32 u; } v; v.u=value; return v.f; }
static EventPayload113D60 *state(void) { return (EventPayload113D60 *)(record.bytes+0x28); }
static void push(char c) { if(traceLength<255) trace[traceLength++]=c; else error=1; }
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
    if(i>=64 || originCalls!=1) { error=3; return 0; }
    if(!i && mutateInitial) {
        state()->field00=0.25f; state()->field04=0.5f; state()->field08=0.5f;
        expectedBase=bits(0.25f); expectedVariation=bits(0.5f);
        D_800BE9A4=0.5f; D_800DCD90=4; D_800BE9E8=77;
    }
    if(i && !inPoint) {
        selectionCalls++;
        if(mutateSelection) {
            int k=selectionCalls==1?1:0;
            D_800DCD90=selectionCalls==1?8:2; nodes[k].weight=D_800DCD90;
            nodes[k].next=NULL; D_800DCDC4=(u8 *)&nodes[k];
        }
        if(mutateConstants) { D_800A13B8=99; D_800A13BC=100; D_800A13C0=101; D_800A13C4=0; }
    }
    return samples[i];
}
s32 func_150ADA20(void) {
    int i=integerCalls++;
    push('I');
    if(i>=32) { error=4; return 0; }
    if(mutateMetadata && !inPoint) {
        record.bytes[0xC]=expectedSlot=0xC7; record.bytes[1]=expectedContext=0x81;
    }
    return (s32)integers[i];
}
void func_1514470C(void *descriptor, void *output) {
    int k=descriptor==descriptors[0]?0:descriptor==descriptors[1]?1:2, i;
    f32 *p=output;
    push('P');
    if(descriptor!=descriptors[k] || pointCalls>=8 || selectionCalls!=pointCalls+1) error=5;
    selected[pointCalls++]=k;
    for(i=0;i<3;i++) expectedPosition[i]=points[k][i];
    if(actualWriter) {
        inPoint=1; actualWriter(descriptor,output); inPoint=0;
    } else for(i=0;i<3;i++) p[i]=points[k][i];
    if(poisonPayload) {
        ExtendedEventPositionPayload113D60 *child=output;
        /* Opaque-boundary mutation proves subsequent resets and hole forwarding. */
        child->payload.parameters.field00=child->payload.parameters.field04=-1;
        child->payload.parameters.field08=child->field18=-1;
        child->field30=child->field38=-1; child->field34=child->field35=255;
        for(i=0;i<0x14;i++) child->reserved1C[i]=(u8)(0x80+i);
        child->reserved36[0]=0xD6; child->reserved36[1]=0xD7;
    }
    if(mutateOrigin && pointCalls==1) origin[0]=3;
}
void *func_15149130(s16 duration, s8 index, s8 kind, s8 source, u8 active,
                   u8 mode, s32 size, u8 slot, s32 context) {
    int i=allocations;
    if(kind==0x36) {
        push('G'); creatorCalls++;
        if(creatorCalls!=1 || originCalls || duration!=(s16)(integers[integerCalls-1]%26+5)
           || index!=-1 || source!=-1 || active!=1 || mode || size!=12 || slot!=255 || context!=1) error=6;
        record.bytes[0xC]=expectedSlot=slot; record.bytes[1]=expectedContext=(u8)context;
        return record.bytes;
    }
    push('A'); allocations++;
    if(i>=8 || kind!=0x37 || index!=-1 || source!=-1 || active!=1 || mode || size!=60
       || slot!=expectedSlot || context!=expectedContext || selectionCalls!=pointCalls
       || duration!=(s16)(integers[integerCalls-1]%13+5)) error=7;
    if(i>=8) { state()->field08=1; return NULL; }
    if(mutateProgress && i==0) state()->field08=3.5f;
    return failures&(1<<i)?NULL:children[i].bytes;
}
void *memcpy(void *destination, const void *source, u32 size) {
    const ExtendedEventPositionPayload113D60 *p=source;
    u32 j;
    push('C'); copies++;
    if(destination==record.bytes+0x28) {
        const EventPayload113D60 *initial=source;
        if(size!=12 || creatorCalls!=1 || bits(initial->field00)!=bits(D_800A13B0)
           || bits(initial->field04)!=bits(D_800A13B4) || bits(initial->field08)) error=8;
        expectedBase=bits(D_800A13B0); expectedVariation=bits(D_800A13B4);
    } else {
        int k=allocations-1, i;
        if(k<0 || k>=8) { error=9; return destination; }
        copied[k]++;
        if(destination!=children[k].bytes+0x28 || size!=60 || copied[k]!=1 || failures&(1<<k)
           || bits(p->payload.position.x)!=bits(expectedPosition[0])
           || bits(p->payload.position.y)!=bits(expectedPosition[1])
           || bits(p->payload.position.z)!=bits(expectedPosition[2])
           || bits(p->payload.parameters.field00)!=expectedFirst
           || bits(p->payload.parameters.field04)!=expectedSecond || bits(p->payload.parameters.field08)
           || bits(p->field18)!=expectedParameter || p->field30 || p->field34 || p->field35 || p->field38) error=10;
        if(poisonPayload) {
            for(i=0;i<0x14;i++) if(p->reserved1C[i]!=(u8)(0x80+i)) error=11;
            if(p->reserved36[0]!=0xD6 || p->reserved36[1]!=0xD7) error=11;
        }
        if(mutateCopyProgress && k==0) state()->field08=2.125f;
    }
    for(j=0;j<size;j++) ((u8 *)destination)[j]=((const u8 *)source)[j];
    return destination;
}
static void initialize(void) {
    int i,k;
    f32 *globals[6]={&D_800A13B0,&D_800A13B4,&D_800A13B8,&D_800A13BC,&D_800A13C0,&D_800A13C4};
    for(i=0;i<6;i++) *globals[i]=number(literalWords[i]);
    originCalls=floatCalls=selectionCalls=pointCalls=integerCalls=allocations=copies=creatorCalls=error=traceLength=0;
    failures=mutateInitial=mutateSelection=mutateConstants=mutateOrigin=mutateProgress=0;
    mutateCopyProgress=mutateMetadata=poisonPayload=inPoint=0; actualWriter=NULL;
    D_800BE9E8=(s32)0x80000001; D_800BE9A4=1; D_800DCD90=10; D_800A13C4=4;
    expectedFirst=bits(D_800A13C0); expectedSecond=bits(D_800A13BC); expectedParameter=bits(D_800A13B8);
    for(i=0;i<64;i++) { record.bytes[i]=0xA5; samples[i]=0; }
    for(i=0;i<32;i++) integers[i]=i;
    record.bytes[0xC]=expectedSlot=0xC3; record.bytes[1]=expectedContext=0x91;
    expectedBase=expectedVariation=0; state()->field00=state()->field04=0; state()->field08=0.5f;
    for(k=0;k<8;k++) { copied[k]=selected[k]=0; for(i=0;i<112;i++) children[k].bytes[i]=0xA5; }
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
       || bits(state()->field00)!=expectedBase || bits(state()->field04)!=expectedVariation) return 1;
    for(i=0;i<64;i++) if(i!=1 && i!=0xC && (i<0x28 || i>=0x34) && record.bytes[i]!=0xA5) return 2;
    for(k=0;k<8;k++) for(i=0;i<112;i++) {
        /* Undefined retail holes are copied, but their initial values are not asserted. */
        if(copied[k] && i>=0x28 && i<0x64) continue;
        if(children[k].bytes[i]!=0xA5) return 3;
    }
    return 0;
}
''' + cls.creator + '\n' + cls.body + '\n'

    def test_payload_layout_complete_copy_and_tail_resets(self):
        self.run_host(r'''
ExtendedEventPositionPayload113D60 p;
if(sizeof(p)!=60 || (u8 *)&p.payload-(u8 *)&p || (u8 *)&p.field18-(u8 *)&p!=0x18
   || (u8 *)&p.reserved1C-(u8 *)&p!=0x1C || (u8 *)&p.field30-(u8 *)&p!=0x30
   || (u8 *)&p.field34-(u8 *)&p!=0x34 || (u8 *)&p.field35-(u8 *)&p!=0x35
   || (u8 *)&p.reserved36-(u8 *)&p!=0x36 || (u8 *)&p.field38-(u8 *)&p!=0x38) return 1;
initialize(); state()->field08=3.125f; poisonPayload=1;
func_150E9178(record.bytes);
if(error || pointCalls!=3 || floatCalls!=4 || allocations!=3 || copies!=3
   || state()->field08!=0.125f || !trace_is("OFFPIACFPIACFPIAC") || fences()) return 2;
''')

    def test_rate_order_strict_gate_and_bounded_nonfinite_no_head_paths(self):
        self.run_host(r'''
static u32 values[]={0,0x3E800000,0x3F000000,0x3F800000,0xBF800000,0x7FC12345,0x7F800000,0xFF800000};
static f32 progress[]={-1,0,0.5f,1};
int i,j;
for(i=0;i<8;i++) for(j=0;j<4;j++) {
    f32 expected;
    initialize(); D_800DCDC4=NULL; D_800BE9A4=0;
    state()->field00=0.25f; state()->field04=0.5f; state()->field08=progress[j];
    expectedBase=bits(0.25f); expectedVariation=bits(0.5f); samples[0]=number(values[i]);
    expected=progress[j]+((0.25f+samples[0]*0.5f)*0.0f)*10.0f;
    func_150E9178(record.bytes);
    if(error || originCalls!=1 || floatCalls!=1 || pointCalls || integerCalls || allocations || copies
       || !trace_is("OF") || fences()) return 1;
    if(expected==expected) { if(bits(state()->field08)!=bits(expected)) return 2; }
    else if(state()->field08==state()->field08) return 3;
}
''')

    def test_multihop_weight_boundaries_and_zero_weight_nodes(self):
        self.run_host(r'''
static f32 samples0[]={0,0.2f,0.25f,0.5f,0.6f,1};
static f32 samples1[]={0,0.1f,0.3f,0.30000004f,0.6f,1};
static int expected0[]={0,0,1,1,2,2}, expected1[]={0,1,1,2,2,2};
int mode,i;
for(mode=0;mode<2;mode++) for(i=0;i<6;i++) {
    initialize(); state()->field08=2;
    nodes[0].weight=mode?0:2; nodes[1].weight=3; nodes[2].weight=mode?7:5;
    nodes[0].next=&nodes[1]; nodes[1].next=&nodes[2]; nodes[2].next=NULL;
    samples[1]=mode?samples1[i]:samples0[i];
    func_150E9178(record.bytes);
    if(error || pointCalls!=1 || selected[0]!=(mode?expected1[i]:expected0[i]) || floatCalls!=2
       || allocations!=1 || copies!=1 || state()->field08!=1 || fences()) return 1;
}
''')

    def test_unsigned_lifetime_residues_and_allocation_failures(self):
        self.run_host(r'''
static f32 targets[]={0,0.25f,0.3f,0.30000004f,0.9f,1,-1};
static u32 words[]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,0x7FFFFFFF,0x80000000,0xFFFFFFFF};
int i,j,failed;
for(i=0;i<8;i++) for(j=0;j<17;j++) for(failed=0;failed<2;failed++) {
    f32 target=i<7?targets[i]:number(0x7FC00000);
    int expected=3.0f<target*10.0f;
    initialize(); state()->field08=2; samples[1]=target; integers[0]=words[j]; failures=failed;
    func_150E9178(record.bytes);
    if(error || pointCalls!=1 || selected[0]!=expected || floatCalls!=2 || integerCalls!=1
       || allocations!=1 || copies!=!failed || state()->field08!=1
       || !trace_is(failed?"OFFPIA":"OFFPIAC") || fences()) return 1;
}
''')

    def test_accumulator_and_distance_strictness_with_culled_consumption(self):
        self.run_host(r'''
static f32 progress[]={1,1.125f,2,2.125f,3,3.125f,5};
static int counts[]={0,1,1,2,2,3,4};
static f32 distances[]={0,1.999f,2,2.001f};
int i,j;
for(i=0;i<7;i++) for(j=0;j<6;j++) {
    int near=j<2;
    initialize(); state()->field08=progress[i];
    points[0][0]=j<4?distances[j]:number(j==4?0x7FC00000:0x7F800000);
    func_150E9178(record.bytes);
    if(error || floatCalls!=counts[i]+1 || pointCalls!=counts[i] || integerCalls!=counts[i]*near
       || allocations!=counts[i]*near || copies!=counts[i]*near
       || state()->field08!=progress[i]-(f32)counts[i] || fences()) return 1;
}
''')

    def test_initial_rate_reads_and_live_head_weight_with_captured_payload_constants(self):
        self.run_host(r'''
initialize(); mutateInitial=1; samples[0]=0.25f;
func_150E9178(record.bytes);
if(error || originCalls!=1 || pointCalls!=1 || allocations!=1 || copies!=1
   || state()->field08!=0.25f || D_800BE9E8!=77 || fences()) return 1;
initialize(); state()->field08=3; samples[1]=samples[2]=0.5f;
mutateSelection=mutateConstants=1;
func_150E9178(record.bytes);
if(error || floatCalls!=3 || pointCalls!=2 || selected[0]!=1 || selected[1]!=0
   || integerCalls!=2 || allocations!=2 || copies!=2 || state()->field08!=1
   || D_800DCDC4!=(u8 *)&nodes[0] || D_800DCD90!=2 || D_800A13C4!=0 || fences()) return 2;
''')

    def test_origin_metadata_and_progress_reloads_across_callbacks(self):
        self.run_host(r'''
int failed;
for(failed=0;failed<8;failed++) {
    initialize(); state()->field08=2; points[0][0]=3;
    mutateOrigin=mutateProgress=mutateMetadata=1; failures=failed;
    func_150E9178(record.bytes);
    if(error || originCalls!=1 || pointCalls!=3 || floatCalls!=4 || integerCalls!=3 || allocations!=3
       || copies!=3-((failed&1)!=0)-((failed&2)!=0)-((failed&4)!=0)
       || state()->field08!=0.5f || record.bytes[0xC]!=0xC7 || record.bytes[1]!=0x81 || fences()) return 1;
}
initialize(); state()->field08=2; mutateCopyProgress=1;
func_150E9178(record.bytes);
if(error || pointCalls!=2 || allocations!=2 || copies!=2 || state()->field08!=0.125f || fences()) return 2;
''')

    def test_actual_creator_to_extended_updater_payload(self):
        self.run_host(r'''
initialize(); D_800A13B0=0.5f; D_800A13B4=0.25f; D_800BE9A4=0.5f;
D_800DCD90=8; nodes[0].weight=3; nodes[1].weight=5;
samples[0]=0.5f; samples[1]=0; samples[2]=1;
func_150E90DC(); func_150E9178(record.bytes);
if(error || creatorCalls!=1 || floatCalls!=3 || pointCalls!=2 || selected[0]!=0 || selected[1]!=1
   || integerCalls!=3 || allocations!=2 || copies!=3 || state()->field08!=0.5f
   || !trace_is("IGCOFFPIACFPIAC") || fences()) return 1;
''')

    def test_actual_position_writer_all_modes_through_extended_emitter(self):
        helper = (self.root / 'conker/src/game_16EE20.c').read_text()
        def body(name, result):
            return re.search(result + ' ' + name + r'\([^;{}]+\) \{\n.*?\n\}', helper, re.S).group(0)
        writer = body('func_1514470C', 'void').replace('void func_1514470C(', 'static void real_position_writer(', 1)
        connection = ('static const u32 tableWords[65]={' + ','.join('0x%08Xu' % w for w in self.table_words) + '};\n') + r'''
f32 D_800A56A0, D_8009A220[65];
static int mathCalls;
f32 cosf(f32 angle) { push('C'); mathCalls++; return 1; }
f32 sinf(f32 angle) { push('S'); mathCalls++; return 0; }
f32 func_151423D8(u8);
void func_151436B4(f32, f32, f32, vertex *);
''' + body('func_151423D8', 'f32') + '\n' + body('func_151436B4', 'void') + '\n' + writer + '\n'
        original = self.fixture
        try:
            self.fixture += connection
            self.run_host(r'''
static f32 x[]={-100,-100,-104,-100}, y[]={206,200,206,200}, z[]={-298,-294,-298,-300};
static int floats[]={4,5,5,2}, ints[]={2,1,1,1};
int mode,failed,i;
for(mode=0;mode<4;mode++) for(failed=0;failed<3;failed++) {
    u8 *d=descriptors[0];
    initialize(); actualWriter=real_position_writer; state()->field08=1.125f; mathCalls=0;
    D_800A13C4=failed==2?1:3240000;
    for(i=0;i<65;i++) D_8009A220[i]=number(tableWords[i]);
    D_800A56A0=number(0x40C90FDB);
    for(i=0;i<64;i++) d[i]=0;
    *(s16 *)(d+0)=-100; *(s16 *)(d+2)=200; *(s16 *)(d+4)=-300;
    *(s16 *)(d+6)=8; *(s16 *)(d+8)=12; *(s16 *)(d+0xA)=4;
    *(f32 *)(d+0x24)=0; *(f32 *)(d+0x28)=1; *(f32 *)(d+0x2C)=0; *(f32 *)(d+0x30)=1;
    d[0x15]=(u8)mode;
    points[0][0]=x[mode]; points[0][1]=y[mode]; points[0][2]=z[mode];
    samples[2]=0.25f; samples[3]=0.5f; samples[4]=0.75f;
    integers[0]=0x80000000; integers[1]=0xFFFFFFFF; failures=failed==1;
    func_150E9178(record.bytes);
    if(error || originCalls!=1 || pointCalls!=1 || selectionCalls!=1 || floatCalls!=floats[mode]
       || integerCalls!=ints[mode]-(failed==2) || allocations!=(failed!=2) || copies!=!failed
       || mathCalls!=(mode==1?4:0) || state()->field08!=0.125f || fences()) return 1;
}
''')
        finally:
            self.fixture = original

    def test_retail_slot_callback_mapping_and_no_instruction_guards(self):
        words = struct.unpack('>153I', self.rom[0x116628:0x11688C])
        self.assertEqual(words[0], 0x27BDFF10)
        self.assertEqual(words[-2:], (0x03E00008, 0x27BD00F0))
        first, address, _, _ = load_game_data_layout(self.root / 'conker')
        self.assertEqual(struct.unpack_from('>2I', self.rom, first + 0x8008A4E8 + 0x36*4 - address),
                         (0x150E9178, 0x150E93DC))
        self.assertNotIn('memset', self.body)
        self.assertNotIn('reserved1C', self.body)
        self.assertNotIn('reserved36', self.body)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] == 'func_150E9178' for row in csv.DictReader(source)))

    def test_fresh_ido_size_and_production_identity_preserve_exact_neighbors(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(n) is None for n in
                ('mips-linux-gnu-ld', 'mips-linux-gnu-objcopy', 'mips-linux-gnu-objdump')):
            self.skipTest('IDO/MIPS tools are unavailable')
        source, obj, elf, binary, script = (self.path / ('extended' + suffix)
                                           for suffix in ('.c', '.o', '.elf', '.bin', '.ld'))
        source.write_text(self.types + self.layouts + self.declarations + self.body + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
            '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3',
            '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        script.write_text('SECTIONS { .text 0x150E9178 : SUBALIGN(4) { *(.text) } }\n')
        targets = {name: int(name[2:], 16) for name in
                   ('D_800BE9E8', 'D_800BE9A4', 'D_800DCD90', 'D_800DCDC4',
                    'D_800A13B8', 'D_800A13BC', 'D_800A13C0', 'D_800A13C4')}
        targets.update({name: int(name[5:], 16) for name in
                        ('func_15144B34', 'func_150ADA68', 'func_1514470C', 'func_150ADA20', 'func_15149130')})
        targets['memcpy'] = 0x10022EC0
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_150E9178',
            *(f'--defsym={name}=0x{value:X}' for name, value in targets.items()),
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', '.text', str(elf), str(binary)],
                       check=True, capture_output=True)
        data = binary.read_bytes()
        words = struct.unpack('>' + 'I' * (len(data) // 4), data)
        count = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        self.assertEqual(count, 153)
        self.assertEqual(0x10000 - (words[0] & 0xFFFF), 0xF8)
        self.assertEqual(data[count*4:], bytes(len(data)-count*4))
        body = words[:count]
        retail = struct.unpack('>153I', self.rom[0x116628:0x11688C])
        self.assertEqual(sum(a != b for a, b in zip(body, retail)), 54)
        self.assertEqual(hashlib.sha256(data[:count*4]).hexdigest(),
                         'ef319998a5e6c55e5fa3e2808e82e710c7c49d01dfaef2bb0fd50ff886ec8b24')
        production = self.root / 'conker/build/conker.us.elf'
        self.assertTrue(production.is_file(), 'production relink is required')
        linked, _, addresses = match_progress.load_elf_functions(str(production), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_150E9178'], 0x150E9178)
        self.assertEqual(tuple(linked['func_150E9178']), body)
        for name, count in (('func_150E90DC', 39), ('func_150E8A80', 39), ('func_151436B4', 34),
                            ('func_151423D8', 27), ('func_15144B34', 13)):
            with self.subTest(function=name):
                first = 0x2D4B0 + addresses[name] - 0x15000000
                self.assertEqual(len(linked[name]), count)
                self.assertEqual(struct.pack('>' + 'I' * count, *linked[name]), self.rom[first:first+count*4])
        print('extended weighted emitter slot:', {'body_words': 153, 'slot_words': 153,
              'frame_bytes': 0xF8, 'different_words': 54})


if __name__ == '__main__':
    unittest.main()
