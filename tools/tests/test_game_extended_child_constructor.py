"""Actual extended constructor/resource helper; allocation and loaders are opaque fixtures."""

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


class GameExtendedChildConstructorTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.source = (cls.root / 'conker/src/game/generated_15F680.c').read_text()
        cls.constructor = re.search(r'void \*func_1513264C\([^;{}]+\) \{\n.*?\n\}', cls.source, re.S).group(0)
        cls.helper = re.search(r's32 func_151336A8\([^;{}]+\) \{\n.*?\n\}', cls.source, re.S).group(0)
        cls.wrapper = re.search(r'void \*func_15132A4C\([^;{}]+\) \{\n.*?\n\}', cls.source, re.S).group(0)
        cls.types = ('typedef unsigned char u8; typedef unsigned short u16; typedef short s16; '
                     'typedef int s32; typedef unsigned int u32; typedef float f32;\n'
                     '#define NULL ((void *)0)\n')
        cls.layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';',
                                         cls.source, re.S).group(0) for name in
            ('ExtendedResource15F680', 'ExtendedResourceNode15F680', 'ExtendedState15F680')) + '\n'
        cls.declarations = r'''
extern f32 D_800A3868;
extern s32 D_800A3880[], D_800DC63C, D_800DC640[], D_800BE9F0, D_80082FA0;
extern s16 D_800DC468[];
extern u8 D_800BE616;
extern ExtendedResourceNode15F680 *D_800DC460, *D_800DC464;
void *allocate_memory(s32, s32, s32, s32);
void func_10004074(void *);
void *func_15167A68(s32, s32, s32, s32, u8, u8);
void func_15168A9C(void *);
u8 *func_1515D480(s32);
u8 *func_1515D440(void);
ExtendedResource15F680 *func_1502B6BC(s32 *, s32, s32 *, s32, s32, s32);
void func_1510CE60(void *, s32, s32, s32, s32 *);
void func_15168E54(void *, void *);
s32 func_151336A8(s32, ExtendedResourceNode15F680 *, void *);
void *memcpy(void *, const void *, u32);
f32 sqrtf(f32);
'''
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        first, address, _, _ = load_game_data_layout(cls.root / 'conker')
        cls.table = struct.unpack_from('>236I', cls.rom, first + 0x800A3880 - address)
        cls.default = struct.unpack_from('>I', cls.rom, first + 0x800A3868 - address)[0]
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = cls.types + cls.layouts + cls.declarations + (
            'static const u32 retailTable[236]={' + ','.join('0x%Xu' % w for w in cls.table) + '};\n'
            'static const u32 retailDefault=0x%Xu;\n' % cls.default) + r'''
f32 D_800A3868;
s32 D_800A3880[236], D_800DC63C, D_800DC640[234], D_800BE9F0, D_80082FA0;
s16 D_800DC468[234];
u8 D_800BE616;
ExtendedResourceNode15F680 *D_800DC460, *D_800DC464;
static union { u32 alignment; u8 bytes[0x240]; } storage, descriptorStorage;
static u8 *result=storage.bytes+16, *descriptor=descriptorStorage.bytes+16;
static ExtendedState15F680 optional;
static ExtendedResourceNode15F680 nodes[102];
static ExtendedResource15F680 loaded[3];
static u32 data[3];
static u8 views[4][4], trailing[4];
static int allocations, nodeAllocations, loads, setups, attachments, copies, removals, frees;
static int viewCalls, tailCalls, error, failRecord, failNode, failLoad, mutate, mutateBound;
static int inChild, extraCopies;
static int expectedKind, expectedPool, expectedNodePool, expectedSize, expectedContext;
static int expectedResource, expectedValue, expectedSlot, expectedIndex, expectedRefs;
static f32 expectedLength;
static char trace[128];
static int traceLength;
static u32 bits(f32 value) { union { f32 f; u32 u; } word; word.f=value; return word.u; }
static f32 number(u32 value) { union { f32 f; u32 u; } word; word.u=value; return word.f; }
static void push(char c) { if(traceLength<127) trace[traceLength++]=c; else error=1; }
static int trace_is(const char *s) {
    int i=0;
    while(s[i]) { if(i>=traceLength || s[i]!=trace[i]) return 0; i++; }
    return i==traceLength;
}
static void reset(u32 flags, int index) {
    int i;
    descriptor=descriptorStorage.bytes+16;
    for(i=0;i<0x240;i++) { storage.bytes[i]=0xA5; descriptorStorage.bytes[i]=0x6B; }
    for(i=0;i<(int)sizeof(nodes);i++) ((u8 *)nodes)[i]=0xD7;
    for(i=0;i<234;i++) { D_800DC468[i]=0; D_800DC640[i]=0x2468; }
    for(i=0;i<236;i++) D_800A3880[i]=(s32)retailTable[i];
    for(i=0;i<3;i++) { loaded[i].data=&data[i]; data[i]=(u32)(0xABC0+i); }
    for(i=0;i<9;i++) optional.words[i]=0x12345000u+(u32)i;
    allocations=nodeAllocations=loads=setups=attachments=copies=removals=frees=0;
    viewCalls=tailCalls=error=failRecord=failNode=failLoad=mutate=mutateBound=inChild=extraCopies=0;
    traceLength=0;
    D_800DC460=D_800DC464=NULL;
    D_800DC63C=0; D_800BE9F0=0; D_800BE616=0; D_80082FA0=3;
    D_800A3868=number(retailDefault);
    *(u32 *)(descriptor+0x50)=flags; *(u16 *)(descriptor+0x56)=(u16)index;
    *(f32 *)(descriptor+0x34)=3; *(f32 *)(descriptor+0x38)=4; *(f32 *)(descriptor+0x3C)=12;
    expectedLength=13;
    expectedKind=(flags&0x4000)?0x48:0x19; expectedPool=(flags&0x400000)?2:1;
    expectedNodePool=expectedPool; expectedSize=0x18C; expectedContext=-123;
    expectedResource=3; expectedValue=255; expectedSlot=0xF3; expectedIndex=index;
    expectedRefs=1;
}
static int fences(void) {
    int i;
    for(i=0;i<16;i++) if(storage.bytes[i]!=0xA5 || storage.bytes[0x230+i]!=0xA5
        || descriptorStorage.bytes[i]!=0x6B || descriptorStorage.bytes[0x230+i]!=0x6B) return 1;
    return 0;
}
void *func_15167A68(s32 kind, s32 context, s32 size, s32 linked, u8 slot, u8 pool) {
    push('A'); allocations++;
    if(allocations!=1 || kind!=expectedKind || context!=expectedContext || size!=expectedSize
       || linked!=1 || slot!=expectedSlot || pool!=expectedPool || nodeAllocations || copies) error=2;
    if(mutate&1) {
        *(u16 *)(descriptor+0x56)=9; expectedIndex=9;
        *(u32 *)(descriptor+0x50)=0x500000; expectedNodePool=2;
        D_800DC63C=40;
    }
    return failRecord?NULL:result;
}
void *allocate_memory(s32 size, s32 tag, s32 mode, s32 pool) {
    push('N'); nodeAllocations++;
    if(size!=16 || tag!=1 || mode!=2 || pool!=expectedNodePool || allocations!=1 || copies) error=3;
    if(mutate&2) { *(u16 *)(descriptor+0x56)=10; expectedIndex=10; }
    return failNode?NULL:&nodes[0];
}
ExtendedResource15F680 *func_1502B6BC(s32 *a, s32 b, s32 *c, s32 d, s32 e, s32 f) {
    push('L'); loads++;
    if(b || d!=2 || e!=9 || f!=D_800A3880[expectedIndex] || !a || !c || a==c || copies) error=4;
    *a=123; *c=-456;
    if(mutate&4) { *(u16 *)(descriptor+0x56)=11; *(u32 *)(descriptor+0x50)=0x100000; }
    return failLoad?NULL:&loaded[0];
}
void func_1510CE60(void *a, s32 b, s32 c, s32 d, s32 *e) {
    push('S'); setups++;
    if(a!=loaded[0].data || b || c!=1 || d!=0x3E || e!=&D_800DC640[expectedIndex]
       || loads!=1 || copies || nodes[0].resource!=&loaded[0]) error=5;
    *e=0x1357;
    if(mutate&8) nodes[0].resource=&loaded[1];
    if(mutate&16) { D_800BE9F0=6; D_800BE616=1; D_800DC63C=90; }
}
void func_15168E54(void *a, void *b) {
    ExtendedResource15F680 *p=(mutate&8)?&loaded[1]:&loaded[0];
    push('T'); attachments++;
    if(a!=p->data || b!=p || setups!=1 || copies) error=6;
    if(mutate&32) { *(u16 *)(descriptor+0x56)=12; *(u32 *)(descriptor+0x50)=0x100000; }
}
void func_15168A9C(void *p) {
    push('R'); removals++;
    if(p!=result || copies || removals!=1 || frees || viewCalls || tailCalls) error=7;
}
void func_10004074(void *p) {
    push('F'); frees++;
    if(removals!=1 || copies || (frees==1 && p!=result)
       || (frees==2 && p!=&nodes[0]) || frees>2) error=8;
}
void *memcpy(void *destination, const void *source, u32 length) {
    u32 i;
    if(inChild && length==28) {
        push('E'); extraCopies++;
        if(destination!=result+0x170 || copies!=1 || tailCalls!=1 || removals || frees
           || ((u32)source>=(u32)descriptor && (u32)source<(u32)descriptor+124)) error=12;
        for(i=0;i<length;i++) ((u8 *)destination)[i]=((const u8 *)source)[i];
        return destination;
    }
    if(inChild) descriptor=(u8 *)source;
    push('C'); copies++;
    if(destination!=result+0x10 || source!=descriptor || length!=124
       || *(ExtendedResourceNode15F680 **)(result+0x8C)==NULL || removals || frees
       || D_800DC468[*(u16 *)(descriptor+0x56)]!=expectedRefs) error=9;
    for(i=0;i<length;i++) ((u8 *)destination)[i]=((const u8 *)source)[i];
    if(mutate&64) {
        *(f32 *)(descriptor+0x34)=6; *(f32 *)(descriptor+0x38)=8; *(f32 *)(descriptor+0x3C)=0;
        D_800DC63C=99; D_800A3868=-777; expectedLength=10;
    }
    return destination;
}
f32 sqrtf(f32 value) {
    f32 resultValue;
    __asm__("sqrtss %1, %0" : "=x"(resultValue) : "x"(value));
    return resultValue;
}
u8 *func_1515D480(s32 resource) {
    int i=viewCalls++;
    push('V');
    if(resource!=expectedResource || copies!=1 || i>3
       || *(s32 *)(result+0x168)!=expectedValue) error=10;
    if(mutateBound==1) D_80082FA0=(i==0)?3:1;
    if(mutateBound==2) D_80082FA0=0;
    if(mutate&128) *(u32 *)(result+0x60)=0xABCDEF01;
    return i<4?views[i]:NULL;
}
u8 *func_1515D440(void) {
    push('B'); tailCalls++;
    if(copies!=1 || tailCalls!=1 || *(s32 *)(result+0x14C)!=expectedResource) error=11;
    return trailing;
}
static int check_result(int statePresent, ExtendedResourceNode15F680 *node, int viewsExpected) {
    u8 golden[0x170];
    int i;
    for(i=0;i<0x170;i++) golden[i]=0xA5;
    for(i=0;i<124;i++) golden[0x10+i]=descriptor[i];
    *(ExtendedResourceNode15F680 **)(golden+0x8C)=node;
    *(f32 *)(golden+0x134)=*(f32 *)(golden+0x138)=*(f32 *)(golden+0x13C)=0;
    *(f32 *)(golden+0x140)=expectedLength;
    *(f32 *)(golden+0x144)=1;
    golden[0x148]=golden[0x149]=0;
    if(statePresent) { for(i=0;i<36;i++) golden[0x110+i]=((u8 *)&optional)[i]; }
    else {
        *(u32 *)(golden+0x130)=*(u32 *)(golden+0x128)=0;
        golden[0x12D]=golden[0x12C]=0;
        *(f32 *)(golden+0x110)=D_800A3868;
    }
    *(s32 *)(golden+0x14C)=expectedResource; *(s32 *)(golden+0x168)=expectedValue;
    golden[0x150]=0;
    for(i=0;i<4;i++) *(void **)(golden+0x154+i*4)=(i<viewsExpected)?views[i]:NULL;
    *(void **)(golden+0x164)=expectedResource?trailing:NULL;
    *(u32 *)(golden+0x60)&=~0x200000;
    for(i=0;i<0x170;i++) if(result[i]!=golden[i]) return i+1;
    for(i=0x170;i<0x220;i++) if(result[i]!=0xA5) return i+1;
    return fences();
}
''' + cls.helper + '\n' + cls.constructor + '\n' + cls.wrapper + '\n'

    def test_layout_complete_creation_and_default_holes(self):
        self.run_host(r'''
void *p;
if(sizeof(ExtendedResourceNode15F680)!=16 || sizeof(ExtendedState15F680)!=36
   || (u32)&nodes[0].id-(u32)&nodes[0]!=12) return 1;
reset(0x7049E8,7); p=func_15132A4C(descriptor,3,255,28,0xF3,-123);
if(p!=result || error || !trace_is("ANLSTCVVVVB") || check_result(0,&nodes[0],4)) return 2;
if(D_800DC63C!=1 || D_800DC468[7]!=1 || D_800DC460!=&nodes[0] || D_800DC464!=&nodes[0]
   || nodes[0].next || nodes[0].previous || nodes[0].id!=7 || nodes[0].retained!=1
   || nodes[0].reserved0F!=0xD7 || nodes[0].resource!=&loaded[0]) return 3;
''')

    def test_cap_precedes_descriptor_reads_and_all_callbacks(self):
        self.run_host(r'''
static s32 counts[]={301,302,0x7FFFFFFF}; int i;
for(i=0;i<3;i++) {
    reset(0,7); D_800DC63C=counts[i];
    if(func_1513264C(NULL,3,255,NULL,28,0xF3,-123) || traceLength || error || fences()) return 1;
}
for(i=-1;i<=300;i+=301) {
    reset(0,7); D_800DC63C=i;
    if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error
       || D_800DC63C!=i+1 || check_result(0,&nodes[0],4)) return 2;
}
reset(0,7); D_800DC63C=300;
if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error || D_800DC63C!=301) return 3;
''')

    def test_allocator_flags_argument_types_sizes_and_optional_state(self):
        self.run_host(r'''
static u32 flags[]={0,0x4000,0x400000,0x404000,0xFFFFFFFF};
static s32 sizes[]={-16,0,28,512}; int i,j;
for(i=0;i<5;i++) for(j=0;j<4;j++) {
    reset(flags[i],7); expectedSize=sizes[j]+0x170;
    expectedResource=0; expectedValue=(s32)0x80000001; expectedContext=(s32)0x87654321; expectedSlot=255;
    if(func_1513264C(descriptor,0,expectedValue,&optional,sizes[j],255,expectedContext)!=result
       || error || !trace_is("ANLSTC") || check_result(1,&nodes[0],0) || D_800DC63C!=1) return 1;
}
''')

    def test_failure_cleanup_orders_and_no_partial_success_writes(self):
        self.run_host(r'''
int phase,i;
for(phase=0;phase<3;phase++) {
    reset(0x704000,7); failRecord=phase==0; failNode=phase==1; failLoad=phase==2;
    if(func_15132A4C(descriptor,3,255,28,0xF3,-123) || error || copies || viewCalls || tailCalls
       || D_800DC63C || D_800DC468[7] || D_800DC460 || D_800DC464 || fences()) return 1;
    if(!trace_is(phase==0?"A":phase==1?"ANRF":"ANLRFF")) return 2;
    for(i=0;i<0x220;i++) if(result[i]!=0xA5) return 3;
    if(phase==2 && nodes[0].resource) return 4;
}
''')

    def test_new_node_prepend_preserves_old_tail_and_unrelated_nodes(self):
        self.run_host(r'''
reset(0,7);
nodes[1].next=&nodes[2]; nodes[1].previous=NULL;
nodes[2].next=NULL; nodes[2].previous=&nodes[1];
D_800DC460=&nodes[1]; D_800DC464=&nodes[2];
if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error || check_result(0,&nodes[0],4)) return 1;
if(D_800DC460!=&nodes[0] || D_800DC464!=&nodes[2] || nodes[0].next!=&nodes[1]
   || nodes[0].previous || nodes[1].previous!=&nodes[0] || nodes[1].next!=&nodes[2]
   || nodes[2].previous!=&nodes[1] || nodes[2].next) return 2;
''')

    def test_retention_flag_category_and_mode_truth_table(self):
        self.run_host(r'''
static s32 categories[]={-1,0,1,2,3,6,0x13,0x3B,0x3C};
static u8 modes[]={0,1,255}; int f,c,m;
for(f=0;f<2;f++) for(c=0;c<9;c++) for(m=0;m<3;m++) {
    int retained=f && modes[m]==0 && categories[c]!=2 && categories[c]!=6
        && categories[c]!=0x13 && categories[c]!=0x3B;
    reset(f?0x100000:0,7); D_800BE9F0=categories[c]; D_800BE616=modes[m];
    if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error
       || nodes[0].retained!=retained || check_result(0,&nodes[0],4)) return 1;
}
''')

    def test_reuse_signed_refcount_and_exact_hundred_hop_boundary(self):
        self.run_host(r'''
static s16 refs[]={-32768,-1,1,32767}; int position,r,i;
for(position=0;position<=100;position++) for(r=0;r<4;r++) {
    reset(0,7); D_800DC468[7]=refs[r]; expectedRefs=(s16)(refs[r]+1);
    for(i=0;i<102;i++) { nodes[i].id=8; nodes[i].next=&nodes[(i+1)%102]; }
    nodes[position].id=7; D_800DC460=&nodes[0]; D_800DC464=&nodes[101];
    if(position==100) {
        if(func_15132A4C(descriptor,3,255,28,0xF3,-123) || error || !trace_is("ARF")
           || D_800DC468[7]!=refs[r] || D_800DC63C || copies) return 1;
    } else {
        if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error
           || !trace_is("ACVVVVB") || check_result(0,&nodes[position],4)
           || D_800DC468[7]!=expectedRefs || D_800DC63C!=1) return 2;
    }
    if(nodeAllocations || loads || setups || attachments || D_800DC460!=&nodes[0]
       || D_800DC464!=&nodes[101] || fences()) return 3;
}
reset(0,7); D_800DC468[7]=1; nodes[0].id=8; nodes[0].next=&nodes[0]; D_800DC460=&nodes[0];
if(func_15132A4C(descriptor,3,255,28,0xF3,-123) || error || !trace_is("ARF")) return 4;
''')

    def test_live_descriptor_reload_across_allocators_and_loader_callbacks(self):
        self.run_host(r'''
reset(0,7); mutate=1|2|4|8|16|32;
if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error
   || !trace_is("ANLSTCVVVVB") || check_result(0,&nodes[0],4)) return 1;
if(D_800DC468[7] || D_800DC468[9] || D_800DC468[10] || D_800DC468[11]
   || D_800DC468[12]!=1 || nodes[0].id!=12 || nodes[0].retained || nodes[0].resource!=&loaded[1]
   || D_800DC640[10]!=0x1357 || D_800DC640[12]!=0x2468 || D_800DC63C!=91) return 2;
''')

    def test_reads_post_copy_norm_default_and_count_then_clears_live_result_flags(self):
        self.run_host(r'''
reset(0x7049E8,7); mutate=64|128;
if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error || D_800DC63C!=100
   || *(f32 *)(result+0x140)!=10 || *(f32 *)(result+0x110)!=-777
   || *(f32 *)(result+0x44)!=3 || *(f32 *)(result+0x48)!=4 || *(f32 *)(result+0x4C)!=12
   || *(u32 *)(result+0x60)!=(0xABCDEF01u&~0x200000u) || fences()) return 1;
''')

    def test_post_allocation_resource_reload_selects_reuse_instead_of_new_node(self):
        self.run_host(r'''
reset(0,7); mutate=1;
D_800DC468[9]=3; expectedRefs=4; nodes[1].id=9; nodes[1].next=NULL;
D_800DC460=D_800DC464=&nodes[1];
if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error
   || !trace_is("ACVVVVB") || check_result(0,&nodes[1],4) || D_800DC63C!=41
   || D_800DC468[7] || D_800DC468[9]!=4 || nodeAllocations || loads || setups || attachments) return 1;
''')

    def test_view_bound_reloaded_and_zero_resource_skips_all_view_callbacks(self):
        self.run_host(r'''
static s32 bounds[]={-3,-1,0,1,2,3}; int b;
for(b=0;b<6;b++) {
    int count=bounds[b]<0?0:bounds[b]+1;
    reset(0,7); D_80082FA0=bounds[b];
    if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error || viewCalls!=count
       || tailCalls!=1 || check_result(0,&nodes[0],count)) return 1;
}
reset(0,7); D_80082FA0=0; mutateBound=1;
if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error || viewCalls!=2
   || check_result(0,&nodes[0],2)) return 2;
reset(0,7); mutateBound=2;
if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=result || error || viewCalls!=1
   || check_result(0,&nodes[0],1)) return 3;
reset(0,7); expectedResource=0; D_80082FA0=0x7FFFFFFF;
if(func_15132A4C(descriptor,0,255,28,0xF3,-123)!=result || error || viewCalls || tailCalls
   || check_result(0,&nodes[0],0)) return 4;
''')

    def test_resource_helper_all_retail_ids_failure_and_post_setup_reload(self):
        self.run_host(r'''
int index;
for(index=0;index<234;index++) {
    reset(0,index);
    if(func_151336A8(index,&nodes[0],NULL)!=1 || error || !trace_is("LST")
       || nodes[0].resource!=&loaded[0] || D_800DC640[index]!=0x1357) return 1;
    reset(0,index); failLoad=1;
    if(func_151336A8(index,&nodes[0],(void *)1) || error || !trace_is("L") || nodes[0].resource) return 2;
}
reset(0,7); mutate=8;
if(func_151336A8(7,&nodes[0],NULL)!=1 || error || !trace_is("LST")
   || nodes[0].resource!=&loaded[1]) return 3;
''')

    def test_actual_child_wrapper_constructor_resource_helper_connection(self):
        source = (self.root / 'conker/src/game/generated_113D60.c').read_text()
        helpers = (self.root / 'conker/src/game_16EE20.c').read_text()
        child = re.search(r'void func_150E93DC\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        spherical = re.search(r'void func_151436B4\([^;{}]+\) \{\n.*?\n\}', helpers, re.S).group(0)
        layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';',
                                     source, re.S).group(0) for name in
            ('EventPayload113D60', 'WorldPosition113D60', 'EventPositionPayload113D60',
             'ExtendedChildEmissionDescriptor113D60'))
        connection = r'''
typedef struct { f32 x,y,z; } vertex;
''' + layouts + r'''
f32 D_800A13C8=27374, D_800A13CC=0.001f, D_800A13D0=351, D_800A13D4=423;
f32 D_800A13D8=-1401, D_800A13DC=-13687, D_800A13E0=-13687, D_800A13E4=6.2831855f;
f32 D_800BE9A4=1, D_800A12F4[1]={0.1f};
u8 D_800A12F0[1]={7};
static union { u32 alignment; u8 bytes[0x90]; } childRecord;
static int floats, integers, mathCalls;
f32 func_150ADA68(void) { floats++; return 0.5f; }
s32 func_150ADA20(void) { integers++; return 0x12345678; }
f32 cosf(f32 a) { mathCalls++; return a+1; }
f32 sinf(f32 a) { mathCalls++; return a-1; }
''' + spherical + '\n#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"\n' + child + '\n#pragma GCC diagnostic pop\n'
        original = self.fixture
        try:
            self.fixture += connection
            self.run_host(r'''
EventPositionPayload113D60 *payload=(EventPositionPayload113D60 *)(childRecord.bytes+0x28);
int phase,i;
for(phase=0;phase<4;phase++) {
    reset(0x49E8,7); inChild=1;
    for(i=0;i<0x90;i++) childRecord.bytes[i]=0;
    childRecord.bytes[0xC]=0xF3; childRecord.bytes[1]=0x91; expectedContext=0x91;
    payload->position.x=100; payload->position.y=200; payload->position.z=300;
    payload->parameters.field00=1.75f; payload->parameters.field04=0; payload->parameters.field08=0;
    failRecord=phase==1; failNode=phase==2; failLoad=phase==3; floats=integers=mathCalls=0;
    func_150E93DC(childRecord.bytes);
    if(error || floats!=11 || integers!=2 || mathCalls!=4 || payload->parameters.field08!=0.75f
       || fences()) return 1;
    if(phase==0) {
        if(!trace_is("ANLSTCVVVVBE") || extraCopies!=1 || copies!=1 || D_800DC63C!=1
           || D_800DC468[7]!=1 || nodes[0].id!=7 || *(void **)(result+0x8C)!=&nodes[0]
           || *(u32 *)(result+0x60)!=0x49E8 || *(f32 *)(result+0x140)!=0
           || *(f32 *)(result+0x144)!=1 || *(s32 *)(result+0x14C)!=3
           || *(s32 *)(result+0x168)!=255 || result[0x71]!=8) return 2;
    } else if(extraCopies || copies || D_800DC63C || D_800DC468[7]
              || !trace_is(phase==1?"A":phase==2?"ANRF":"ANLRFF")) return 3;
}
''')
        finally:
            self.fixture = original

    def test_retail_ownership_interfaces_no_guards_and_remaining_loader_gates(self):
        self.assertEqual(self.default, 0xC61C4000)
        self.assertEqual(self.table[-3:], (0, 0, 0))
        self.assertEqual(self.table[7], 0xC6)
        self.assertNotIn('memset', self.constructor)
        self.assertNotIn('bzero', self.constructor)
        for name, rom, size in (('func_1513264C', 0x15FAFC, 256), ('func_151336A8', 0x160B58, 46)):
            words = struct.unpack_from('>' + str(size) + 'I', self.rom, rom)
            self.assertEqual(words[0] & 0xFFFF, 0xFFB8 if size == 256 else 0xFFD0)
            with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as source:
                self.assertFalse(any(row['function'] == name for row in csv.DictReader(source)))
        for path, name in (('game_57FA0.c', 'func_1502B6BC'),
                           ('game/generated_139FC0.c', 'func_1510CE60'),
                           ('game_1944C0.c', 'func_15168E54')):
            text = (self.root / 'conker/src' / path).read_text()
            self.assertRegex(text, r's32 ' + name + r'\(\) \{\s*return 0;\s*\}')

    def test_fresh_ido_bodies_slots_and_exact_wrapper(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(n) is None for n in
                ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            self.skipTest('IDO/MIPS tools are unavailable')
        source, obj, elf, script = (self.path / ('constructor' + suffix) for suffix in ('.c', '.o', '.elf', '.ld'))
        source.write_text(self.types + self.layouts + self.declarations + '#pragma intrinsic(sqrtf)\n' +
                          self.constructor + '\n' + self.wrapper + '\n' + self.helper + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
            '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3',
            '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        compact, _, _ = match_progress.load_elf_functions(str(obj), 'mips-linux-gnu-objdump')
        sizes = {'func_1513264C': 256, 'func_15132A4C': 15, 'func_151336A8': 46}
        measured = {'func_1513264C': (255, 0x50, 184, '8b6d14c3eb1958344cb8b6b07419aa58f7f376269bb1717182d3f8f879ee046a'),
                    'func_151336A8': (45, 0x30, 9, 'b9bf8563bcb9f3774bccf5094ff9f8f46b47cc2de1d93c7b05e35831022fe287'),
                    'func_15132A4C': (15, 0x28, 0, 'ffae9cfd67fff9633201e9af3484a65b32dbb9f1c3222dd9170fe0fc8d43ceeb')}
        for name, size in sizes.items():
            body = compact[name]
            count = max(i for i, word in enumerate(body) if word == 0x03E00008) + 2
            self.assertEqual(count, measured[name][0])
            self.assertEqual(body[count:], [0] * (len(body) - count))
        # Link the compact input in its emitted order; each routine is then compared after relocation.
        script.write_text('SECTIONS { .text 0x1513264C : SUBALIGN(4) { *(.text) } }\n')
        targets = {name: int(name[2:], 16) for name in
            ('D_800A3868', 'D_800A3880', 'D_800DC63C', 'D_800DC640', 'D_800DC468', 'D_800BE9F0',
             'D_80082FA0', 'D_800BE616', 'D_800DC460', 'D_800DC464')}
        targets.update({name: int(name[5:], 16) for name in
            ('func_15167A68', 'func_15168A9C', 'func_1515D480', 'func_1515D440', 'func_1502B6BC',
             'func_1510CE60', 'func_15168E54', 'func_10004074')})
        targets.update({'allocate_memory': 0x10003C40, 'memcpy': 0x10022EC0})
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1513264C',
            *(f'--defsym={name}=0x{value:X}' for name, value in targets.items()), '-o', str(elf), str(obj)],
            check=True, capture_output=True)
        linked, _, _ = match_progress.load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        production, _, addresses = match_progress.load_elf_functions(
            str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        # Internal compact call targets differ from padded production. Normalize only those relocations
        # using the ELF's relocation records, never arbitrary instruction replacements.
        relocations = subprocess.run(['mips-linux-gnu-objdump', '-r', str(obj)],
                                    check=True, capture_output=True, text=True).stdout
        compact_addresses = match_progress.load_elf_functions(str(obj), 'mips-linux-gnu-objdump')[2]
        for name, size in sizes.items():
            body = list(linked[name][:measured[name][0]])
            start = compact_addresses[name]
            for offset, target in re.findall(r'^([0-9a-fA-F]+)\s+R_MIPS_26\s+(func_151336A8|func_1513264C)\s*$',
                                              relocations, re.M):
                index = (int(offset, 16) - start) // 4
                if 0 <= index < len(body):
                    body[index] = (body[index] & 0xFC000000) | ((int(target[5:], 16) >> 2) & 0x3FFFFFF)
            slot = body + [0] * (size-len(body))
            self.assertEqual(addresses[name], int(name[5:], 16))
            self.assertEqual(production[name], slot)
            self.assertEqual(0x10000-(body[0]&0xFFFF), measured[name][1])
            first = 0x2D4B0 + addresses[name] - 0x15000000
            retail = struct.unpack_from('>' + str(size) + 'I', self.rom, first)
            self.assertEqual(sum(a != b for a, b in zip(slot, retail)), measured[name][2])
            self.assertEqual(hashlib.sha256(struct.pack('>' + str(size) + 'I', *slot)).hexdigest(), measured[name][3])
        print('extended constructor:', {name: measured[name][:3] for name in measured})


if __name__ == '__main__':
    unittest.main()
