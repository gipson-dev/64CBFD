"""Actual metadata/cache-maintenance C with bounded DMA, allocator and decoder mocks."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

from tools import match_progress
from tools.pad_generated_object import ELF_HEADER, SECTION_HEADER, read_c_string
from tools.tests import test_game_random_curve_record as curve


class GameTextureMetadataAndMaintenanceTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.metadata_source = (cls.root / 'conker/src/game_305D0.c').read_text()
        cls.cache_source = (cls.root / 'conker/src/game/generated_139FC0.c').read_text()
        cls.bodies = {}
        for name, kind, source in (
                ('func_15003570', 'void', cls.metadata_source),
                ('func_150034B4', 's32', cls.metadata_source),
                ('func_1510D404', 'void', cls.cache_source),
                ('func_1510D374', 's32', cls.cache_source),
                ('func_1510D0EC', 'u32', cls.cache_source),
                ('func_1510CE60', 's32', cls.cache_source),
                ('func_1510D608', 'void', cls.cache_source),
                ('func_1510D694', 'void', cls.cache_source),
                ('func_1510D630', 'void', cls.cache_source)):
            cls.bodies[name] = re.search(kind + ' ' + name + r'\([^;{}]+\) \{\n.*?\n\}',
                                         source, re.S).group(0)
        cls.types = ('typedef unsigned char u8; typedef signed char s8; typedef unsigned short u16; '
                     'typedef short s16; typedef unsigned int u32; typedef int s32;\n'
                     '#define NULL ((void *)0)\n')
        cls.prototypes = r'''
void *allocate_memory(s32,s32,s32,s32);
void *func_10003C6C(s32,s32,s32,s32,s32);
s32 func_10004514(s32,void *,u32,s32);
void func_10004074(void *);
s32 func_10006240(void *,void *,u32);
void func_150AD770(void);
s32 func_1510D374(s32);
u32 func_1510D0EC(s32,s32 *,s32,s32);
void func_1510D694(s32);
void func_1510D608(s32,s32);
'''
        cls.declarations = r'''
extern u16 D_80091D20[], D_800B87A0[];
extern u32 D_800B0E58[], D_8003809C;
extern s8 D_800BC448[];
extern u8 D_800D9F68[], D_800DBDBA, D_800D9F60, D_1A37E0;
extern s32 D_800D9F58, D_800D9F5C, D_800DBDBC, D_8003C8E0;
''' + cls.prototypes
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = cls.types + r'''
static u16 lengthStorage[7764],extentStorage[7764];
static u32 cacheStorage[7764];
static s8 stateStorage[7764];
static u8 activityStorage[7764];
#define D_80091D20 (lengthStorage+1)
#define D_800B87A0 (extentStorage+1)
#define D_800B0E58 (cacheStorage+1)
#define D_800BC448 (stateStorage+1)
#define D_800D9F68 (activityStorage+1)
u32 D_8003809C;
u8 D_800DBDBA,D_800D9F60,D_1A37E0 __attribute__((aligned(16)));
s32 D_800D9F58,D_800D9F5C,D_800DBDBC,D_8003C8E0,D_800BE9F0;
static union { u32 alignment; u8 bytes[48]; } headerStorage;
static u8 compressed[64];
static u32 expanded[32],staged[4],alternate[4],commands[8];
static s16 listStorage[7764];
enum { METADATA=1, RESOLVER=2, MAINTENANCE=3 };
static int phase,error,allocations,listAllocations,dmas,decodes,frees,diagnostics;
static int failHeader,mutateLength,mutateDecode,mutateFree,diagnosticStop;
static int expectedId,freeList,diagnosticCounter;
static u32 metadataCursor,resolverSource,resolverAmount;
static void *expectedFree[4],*expectedDestination[4];
static u32 expectedSource[4],expectedScratch[4];
static s32 expectedMarker[4],decoderResult;
static void stop(s32 code) {
    __asm__ volatile("int $0x80" :: "a"(1),"b"(code) : "memory");
    __builtin_unreachable();
}
static u16 length_for(int id) {
    static u16 lengths[5]={0,1,2,0x8000,0xFFFF};
    return lengths[id%5];
}
static u32 header_for(int id) { return 0xA5000000u ^ ((u32)id*0x010203u); }
static int fences(void) {
    return lengthStorage[0]==0xA5A5 && lengthStorage[7763]==0xA5A5
        && extentStorage[0]==0xA5A5 && extentStorage[7763]==0xA5A5
        && cacheStorage[0]==0xA5A5A5A5 && cacheStorage[7763]==0xA5A5A5A5
        && stateStorage[0]==(s8)0xA5 && stateStorage[7763]==(s8)0xA5
        && activityStorage[0]==0xA5 && activityStorage[7763]==0xA5;
}
static void reset(void) {
    int i;
    for(i=0;i<7764;i++) {
        lengthStorage[i]=extentStorage[i]=0xA5A5; cacheStorage[i]=0xA5A5A5A5;
        stateStorage[i]=(s8)0xA5; activityStorage[i]=0xA5; listStorage[i]=(s16)0xA5A5;
    }
    for(i=0;i<7762;i++) {
        D_80091D20[i]=length_for(i); D_800B87A0[i]=0x7777;
        D_800B0E58[i]=0xFFFFFFFF; D_800BC448[i]=0; D_800D9F68[i]=200;
    }
    for(i=0;i<48;i++) headerStorage.bytes[i]=0xA5;
    for(i=0;i<32;i++) expanded[i]=0xA5A5A5A5;
    for(i=0;i<8;i++) commands[i]=0;
    for(i=0;i<4;i++) {
        staged[i]=alternate[i]=0; expectedFree[i]=expectedDestination[i]=NULL;
        expectedSource[i]=expectedScratch[i]=0; expectedMarker[i]=-1;
    }
    phase=METADATA; error=allocations=listAllocations=dmas=decodes=frees=diagnostics=0;
    failHeader=mutateLength=mutateDecode=mutateFree=diagnosticStop=freeList=0;
    D_800D9F58=0xFFFF; D_800D9F5C=-1; D_800DBDBC=93; D_800D9F60=0;
    D_800DBDBA=0; D_800BE9F0=0; D_8003809C=0x12345678; D_8003C8E0=0;
    metadataCursor=(u32)&D_1A37E0; expectedId=5; decoderResult=0; diagnosticCounter=0;
}
void *allocate_memory(s32 size,s32 b,s32 c,s32 d) {
    if(phase==METADATA) {
        allocations++;
        if(size!=16 || b!=1 || c!=2 || d || allocations!=1 || dmas || frees) error=1;
        return failHeader?NULL:headerStorage.bytes+16;
    }
    listAllocations++;
    if(phase!=RESOLVER || size!=4 || b!=1 || c || d!=2 || listAllocations!=1) error=2;
    return listStorage;
}
void *func_10003C6C(s32 size,s32 b,s32 c,s32 d,s32 e) {
    allocations++;
    if(phase!=RESOLVER || b!=1 || e!=2 || allocations>2) error=3;
    if(allocations==1) {
        if((u32)size!=resolverAmount || c!=2 || d!=1 || D_800DBDBA!=5) error=4;
        return compressed;
    }
    if(size!=D_800B87A0[expectedId] || c!=1 || d || dmas!=1) error=5;
    D_8003809C=0x456789AB;
    return expanded;
}
s32 func_10004514(s32 source,void *destination,u32 amount,s32 mode) {
    int id=dmas++;
    if(phase==METADATA) {
        u8 *bytes=destination; u32 value=header_for(id); u32 skip=metadataCursor&1; int i;
        if(id>=7762 || (u32)source!=(metadataCursor&~1u) || amount!=16 || mode!=1
           || destination!=(failHeader?NULL:headerStorage.bytes+16) || allocations!=1 || frees) error=6;
        if(failHeader) stop(error?96:0);
        if(id && D_800B87A0[id-1]!=(u16)header_for(id-1)) error=7;
        if(D_800B87A0[id]!=0x7777) error=8;
        for(i=0;i<16;i++) bytes[i]=0xCC;
        bytes[skip]=value>>24; bytes[skip+1]=value>>16;
        bytes[skip+2]=value>>8; bytes[skip+3]=value;
        if(mutateLength) D_80091D20[id]=(u16)(id*17);
        metadataCursor+=D_80091D20[id];
    } else if(phase!=RESOLVER || id || (u32)source!=resolverSource || destination!=compressed
              || amount!=resolverAmount || mode!=1 || allocations!=1 || decodes || frees) error=9;
    return -123;
}
s32 func_10006240(void *source,void *destination,u32 scratch) {
    int index=decodes++;
    if(index>=4 || source!=(void *)expectedSource[index] || destination!=expectedDestination[index]
       || scratch!=expectedScratch[index]) error=10;
    if(phase==RESOLVER) {
        if(allocations!=2 || dmas!=1 || frees) error=11;
    } else if(phase==MAINTENANCE) {
        if(D_800DBDBC!=expectedMarker[index]) error=12;
        if(mutateDecode) {
            staged[0]=0x11112222; staged[1]=0x33334444;
            D_800B0E58[expectedId]=(u32)alternate;
            D_800BC448[expectedId]=0x63;
            D_800D9F58=1; D_800D9F5C=100; D_800BC448[100]=1;
            D_8003809C=0x98765432;
        }
    } else error=13;
    return decoderResult;
}
void func_10004074(void *pointer) {
    int index=frees++;
    if(phase==METADATA) {
        if(pointer!=headerStorage.bytes+16 || dmas!=7762 || frees!=1
           || D_800B87A0[7761]!=(u16)header_for(7761)) error=14;
    } else if(phase==RESOLVER) {
        if(pointer!=(freeList?(void *)listStorage:(void *)compressed)) error=15;
    } else if(phase==MAINTENANCE) {
        if(index>=4 || pointer!=expectedFree[index] || D_800DBDBC!=expectedMarker[index]) error=16;
        if(mutateFree && index==0) {
            D_800B0E58[expectedId]=0x13572468;
            D_800BC448[expectedId]=0x51;
            D_800BC448[expectedId+1]=1;
            D_800D9F58=1; D_800D9F5C=100; D_800BC448[100]=1;
        }
    } else error=17;
}
void func_150AD770(void) {
    diagnostics++;
    if(D_8003C8E0!=0x0C000046 || D_800D9F58!=0xFFFF || D_800D9F5C!=-1
       || D_800DBDBC!=93 || D_800DBDBA!=diagnosticCounter) error=18;
    if(diagnosticStop) stop(error?98:0);
    D_800D9F58=9; D_800D9F5C=11;
}
'''
        cls.fixture += cls.prototypes
        cls.fixture += '\n'.join(cls.bodies[n] for n in (
            'func_15003570', 'func_1510D404', 'func_1510D374', 'func_1510D0EC',
            'func_1510D608', 'func_1510D694', 'func_1510D630')) + '\n'
        cls.fixture += '#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored "-Wreturn-type"\n'
        cls.fixture += cls.bodies['func_150034B4'] + '\n#pragma GCC diagnostic pop\n'
        cls.fixture += '#pragma GCC diagnostic push\n#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"\n'
        cls.fixture += cls.bodies['func_1510CE60'] + '\n#pragma GCC diagnostic pop\n'

    def test_metadata_all_entries_endianness_truncation_alignment_and_fences(self):
        self.run_host(r'''
int i; reset(); D_800D9F58=8; D_800D9F5C=9; D_800DBDBA=5; D_800D9F60=1;
for(i=0;i<7762;i++) { D_800B0E58[i]=0x81230000+(u32)i; D_800BC448[i]=(s8)(i*7); D_800D9F68[i]=(u8)i; }
func_15003570();
if(error || allocations!=1 || dmas!=7762 || frees!=1 || decodes || !fences()
   || D_800D9F58!=8 || D_800D9F5C!=9 || D_800DBDBA!=5 || D_800D9F60!=1 || D_800DBDBC!=93) return 1;
for(i=0;i<7762;i++) if(D_800B87A0[i]!=(u16)header_for(i) || D_80091D20[i]!=length_for(i)
    || D_800B0E58[i]!=0x81230000+(u32)i || D_800BC448[i]!=(s8)(i*7) || D_800D9F68[i]!=(u8)i) return 2;
for(i=0;i<16;i++) if(headerStorage.bytes[i]!=0xA5 || headerStorage.bytes[i+32]!=0xA5) return 3;
''')

    def test_metadata_reads_compressed_lengths_fresh_after_each_dma(self):
        self.run_host(r'''
int i; reset(); mutateLength=1; func_15003570();
if(error || dmas!=7762 || frees!=1 || !fences()) return 1;
for(i=0;i<7762;i++) if(D_800B87A0[i]!=(u16)header_for(i) || D_80091D20[i]!=(u16)(i*17)) return 2;
''')

    def test_metadata_null_allocation_first_dma_prefix_only(self):
        self.run_host('reset(); failHeader=1; func_15003570(); return 99;')

    def test_cache_initializer_actual_body_preserves_other_tables_and_activity(self):
        self.run_host(r'''
static s32 modes[]={-1,0,1,2,49,50,51}; int m,i;
for(m=0;m<7;m++) {
    reset(); D_800BE9F0=modes[m]; D_800D9F60=17; D_800DBDBA=4;
    for(i=0;i<7762;i++) { D_800B0E58[i]=i; D_800BC448[i]=127; }
    func_150034B4();
    if(error || !fences() || D_800D9F58!=0xFFFF || D_800D9F5C!=-1
       || D_800D9F60!=(modes[m]==1 || modes[m]==50) || D_800DBDBA!=4 || D_800DBDBC!=93) return 1;
    for(i=0;i<7762;i++) if(D_800B0E58[i]!=0xFFFFFFFF || D_800BC448[i]
        || D_800D9F68[i]!=200 || D_80091D20[i]!=length_for(i) || D_800B87A0[i]!=0x7777) return 2;
}
''')

    def test_maintenance_no_work_counter_and_freeze_gates(self):
        self.run_host(r'''
int counter,freeze;
for(counter=0;counter<=255;counter++) for(freeze=0;freeze<2;freeze++) {
    reset(); phase=MAINTENANCE; D_800DBDBA=(u8)counter; D_800D9F60=(u8)freeze;
    D_800D9F58=5; D_800BC448[5]=3; func_1510D404();
    if(error || D_800DBDBA!=counter || D_800BC448[5]!=3 || D_800D9F58!=5 || D_800DBDBC!=93) return 1;
    D_800D9F5C=5; func_1510D404();
    if(error || frees || decodes || diagnostics || !fences()) return 2;
    if(!counter && freeze) {
        if(D_800BC448[5]!=3 || D_800D9F58!=5 || D_800D9F5C!=5 || D_800DBDBC!=93) return 3;
    } else if(D_800BC448[5]!=2 || D_800D9F58!=5 || D_800D9F5C!=5 || D_800DBDBC!=-2
              || D_800DBDBA!=(counter?counter-1:0)) return 4;
}
''')

    def test_maintenance_all_signed_byte_states_and_activity_untouched(self):
        self.run_host(r'''
int bits; s8 state; reset();
for(bits=0;bits<256;bits++) {
    reset(); phase=MAINTENANCE; state=(s8)bits;
    D_800D9F58=D_800D9F5C=5; D_800BC448[5]=state; D_800B0E58[5]=0x12345678;
    expectedFree[0]=(void *)0x12345678; expectedMarker[0]=5;
    if(state>=4 && (state&0x40)) {
        staged[0]=0xFFFFFFF0; staged[1]=0x20; D_800B0E58[5]=(u32)staged;
        expectedSource[0]=0x10; expectedDestination[0]=staged; expectedScratch[0]=D_8003809C;
        expectedFree[0]=(void *)0xFFFFFFF0; expectedMarker[0]=-1;
    }
    func_1510D404();
    if(error || diagnostics || !fences() || D_800D9F68[5]!=200 || D_800DBDBC!=-2) return 1;
    if(!state || (state>=4 && !(state&0x40))) {
        if(D_800BC448[5]!=state || frees || decodes || D_800D9F58!=0xFFFF || D_800D9F5C!=-1) return 2;
    } else if(state<4) {
        if(D_800BC448[5]!=(s8)(state-1) || decodes || frees!=(state==1)
           || (state==1 && D_800B0E58[5]!=0xFFFFFFFF)
           || D_800D9F58!=(state==1?0xFFFF:5) || D_800D9F5C!=(state==1?-1:5)) return 3;
    } else if(D_800BC448[5]!=(s8)(state&~0x40) || decodes!=1 || frees!=1
              || D_800B0E58[5]!=(u32)staged || D_800D9F58!=5 || D_800D9F5C!=5) return 4;
}
''')

    def test_expiry_callbacks_captured_scan_range_fresh_next_state_and_cache_overwrite(self):
        self.run_host(r'''
reset(); phase=MAINTENANCE; mutateFree=1; D_800D9F58=5; D_800D9F5C=6;
D_800BC448[5]=1; D_800B0E58[5]=0x12340000; D_800B0E58[6]=0x12340010;
expectedFree[0]=(void *)0x12340000; expectedFree[1]=(void *)0x12340010;
expectedMarker[0]=5; expectedMarker[1]=6;
func_1510D404();
if(error || frees!=2 || decodes || D_800B0E58[5]!=0xFFFFFFFF || D_800B0E58[6]!=0xFFFFFFFF
   || D_800BC448[5]!=0x51 || D_800BC448[6] || D_800BC448[100]!=1
   || D_800D9F58!=1 || D_800D9F5C!=100 || D_800DBDBC!=-2 || !fences()) return 1;
''')

    def test_staged_decode_captured_temporary_and_fresh_state_after_callbacks(self):
        self.run_host(r'''
static s32 results[]={0,-1,64}; int r;
for(r=0;r<3;r++) {
    reset(); phase=MAINTENANCE; mutateDecode=mutateFree=1; decoderResult=results[r];
    D_800D9F58=D_800D9F5C=5; D_800BC448[5]=0x40; D_800B0E58[5]=(u32)staged;
    staged[0]=0xFFFFFFF0; staged[1]=0x20;
    expectedSource[0]=0x10; expectedDestination[0]=staged; expectedScratch[0]=D_8003809C;
    expectedFree[0]=(void *)0xFFFFFFF0;
    func_1510D404();
    if(error || decodes!=1 || frees!=1 || D_800B0E58[5]!=0x13572468 || D_800BC448[5]!=0x11
       || D_800BC448[6]!=1 || D_800BC448[100]!=1 || D_800D9F58!=1 || D_800D9F5C!=100
       || D_800DBDBC!=-2 || !fences()) return 1;
}
''')

    def test_staged_callbacks_preserve_cache_replacement_without_free_mutation(self):
        self.run_host(r'''
reset(); phase=MAINTENANCE; mutateDecode=1; D_800D9F58=D_800D9F5C=5;
D_800BC448[5]=0x40; D_800B0E58[5]=(u32)staged; staged[0]=0x12345000; staged[1]=7;
expectedSource[0]=0x12345007; expectedDestination[0]=staged; expectedScratch[0]=D_8003809C;
expectedFree[0]=(void *)0x12345000;
func_1510D404();
if(error || D_800B0E58[5]!=(u32)alternate || D_800BC448[5]!=0x23 || decodes!=1 || frees!=1
   || D_800D9F58!=1 || D_800D9F5C!=100 || !fences()) return 1;
''')

    def test_next_staged_entry_reads_scratch_and_cache_fresh_after_callbacks(self):
        self.run_host(r'''
reset(); phase=MAINTENANCE; mutateDecode=1; D_800D9F58=5; D_800D9F5C=6;
D_800BC448[5]=D_800BC448[6]=0x40; D_800B0E58[5]=(u32)staged; D_800B0E58[6]=(u32)alternate;
staged[0]=0x11110000; staged[1]=3; alternate[0]=0x22220000; alternate[1]=11;
expectedSource[0]=0x11110003; expectedSource[1]=0x2222000B;
expectedDestination[0]=staged; expectedDestination[1]=alternate;
expectedScratch[0]=D_8003809C; expectedScratch[1]=0x98765432;
expectedFree[0]=(void *)0x11110000; expectedFree[1]=(void *)0x22220000;
func_1510D404();
if(error || decodes!=2 || frees!=2 || D_800B0E58[5]!=(u32)alternate
   || D_800BC448[5]!=0x63 || D_800BC448[6] || D_800BC448[100]!=1
   || D_800D9F58!=1 || D_800D9F5C!=100 || D_800DBDBC!=-2 || !fences()) return 1;
''')

    def test_complete_valid_scan_includes_both_endpoints_without_touching_fences(self):
        self.run_host(r'''
reset(); phase=MAINTENANCE; D_800D9F58=0; D_800D9F5C=7761;
D_800BC448[0]=2; D_800BC448[7761]=1; D_800B0E58[7761]=0x12347761;
expectedFree[0]=(void *)0x12347761; expectedMarker[0]=7761;
func_1510D404();
if(error || frees!=1 || decodes || D_800BC448[0]!=1 || D_800BC448[7761]
   || D_800B0E58[7761]!=0xFFFFFFFF || D_800D9F58 || D_800D9F5C
   || D_800DBDBC!=-2 || !fences()) return 1;
''')

    def test_maintenance_empty_ranges_and_diagnostic_return_fallthrough(self):
        self.run_host(r'''
reset(); phase=MAINTENANCE; D_800D9F58=7763; D_800D9F5C=7762; func_1510D404();
if(error || diagnostics || frees || decodes || D_800DBDBC!=-2 || D_800D9F58!=0xFFFF || D_800D9F5C!=-1) return 1;
reset(); phase=MAINTENANCE; D_800D9F58=7764; D_800D9F5C=7763;
D_800DBDBA=3; diagnosticCounter=2; func_1510D404();
if(error || diagnostics!=1 || frees || decodes || D_800DBDBC!=-2
   || D_800D9F58!=9 || D_800D9F5C!=11 || !fences()) return 2;
reset(); phase=MAINTENANCE; D_800D9F58=-1; D_800D9F5C=-2; func_1510D404();
if(error || diagnostics!=1 || D_800DBDBC!=-2 || !fences()) return 3;
''')

    def test_invalid_nonempty_range_diagnostic_prefix_only(self):
        self.run_host('reset(); phase=MAINTENANCE; D_800D9F58=-1; D_800D9F5C=0; '
                      'diagnosticStop=1; func_1510D404(); return 99;')

    def test_actual_metadata_initializer_setup_resolver_release_maintenance_lifecycle(self):
        self.run_host(r'''
int i,output,extent;
reset(); for(i=0;i<7762;i++) D_80091D20[i]=2;
func_15003570(); if(error || D_800B87A0[5]!=(u16)header_for(5)) return 1;
func_150034B4(); phase=RESOLVER; allocations=dmas=decodes=frees=0;
resolverSource=(u32)&D_1A37E0+10; resolverAmount=16;
expectedSource[0]=(u32)compressed; expectedDestination[0]=expanded; expectedScratch[0]=0x456789AB;
commands[0]=0; ((s8 *)commands)[0]=-3; commands[1]=5;
commands[2]=0; ((s8 *)commands)[8]=-0x21; commands[3]=0xA5A5A5A5;
if(!func_1510CE60(commands,0,1,62,&output) || error || output!=(s32)listStorage
   || listStorage[0]!=1 || listStorage[1]!=5 || listStorage[2]!=(s16)0xA5A5
   || allocations!=2 || dmas!=1 || decodes!=1 || frees!=1 || commands[1]!=(u32)expanded
   || D_800BC448[5]!=62 || D_800D9F68[5]!=1) return 2;
extent=-1;
if(func_1510D0EC(5,&extent,62,0)!=(u32)expanded || extent!=(u16)header_for(5)
   || allocations!=2 || dmas!=1 || decodes!=1 || error) return 3;
freeList=1; func_1510D630(listStorage);
if(error || frees!=2 || D_800BC448[5]!=3 || D_800D9F68[5]) return 4;
phase=MAINTENANCE; frees=decodes=0; D_800D9F60=1;
expectedFree[0]=expanded; expectedMarker[0]=5;
for(i=0;i<3;i++) { func_1510D404(); if(error || D_800BC448[5]!=2-i || D_800DBDBA!=4-i) return 5; }
if(frees!=1 || decodes || D_800B0E58[5]!=0xFFFFFFFF || D_800D9F58!=0xFFFF
   || D_800D9F5C!=-1 || D_800DBDBC!=-2 || !fences()) return 6;
''')

    def test_retail_contracts_widths_and_no_new_guards(self):
        config = yaml.safe_load((self.root / 'conker/conker.us.yaml').read_text())
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        self.assertEqual(hashlib.sha1(rom).hexdigest(), config['sha1'])
        words = struct.unpack_from('>62I', rom, 0x2D4B0 + 0x3570)
        code = dict(zip(range(0x15003570, 0x15003668, 4), words))
        self.assertEqual([code[pc] for pc in range(0x150035F8, 0x1500360C, 4)],
                         [0x90580000, 0x904F0003, 0x90490001, 0x904C0002, 0x964E0000])
        self.assertEqual(code[0x15003630], 0xA663FFFE)
        self.assertEqual(code[0x150035BC], 0x26B5C444)
        self.assertEqual(code[0x15003638], 0x02188021)
        self.assertEqual(0x800B87A0 + 7762 * 2, 0x800BC444)
        shared = (self.root / 'conker/include/variables.h').read_text()
        for name in ('D_80091D20', 'D_800B87A0'):
            self.assertRegex(shared, r'extern\s+u16\s+' + name + r'\[\];')
        self.assertIn('last >= 0x1E53', self.bodies['func_1510D404'])
        self.assertNotIn('if (buffer', self.bodies['func_15003570'])
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] in ('func_15003570', 'func_1510D404')
                                 for row in csv.DictReader(source)))

    def test_fresh_ido_slots_and_unchanged_initializer_startup_and_prior_recoveries(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(n) is None for n in
                                        ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            self.skipTest('IDO/MIPS tools are unavailable')
        source, obj, elf, script = (self.path / ('maintenance' + suffix)
                                    for suffix in ('.c', '.o', '.elf', '.ld'))
        names = ('func_15003570', 'func_1510D404')
        source.write_text(self.types + self.declarations + '\n'.join(self.bodies[n] for n in names) + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
            '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3',
            '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        script.write_text('SECTIONS { .text 0x15003570 : SUBALIGN(4) { *(.text) } }\n')
        targets = {name: int(name[2:], 16) for name in ('D_80091D20', 'D_800B87A0', 'D_800B0E58',
            'D_8003809C', 'D_800BC448', 'D_800D9F60', 'D_800DBDBA', 'D_800D9F58', 'D_800D9F5C',
            'D_800DBDBC', 'D_8003C8E0')}
        targets.update({'D_1A37E0': 0x1A37E0, 'allocate_memory': 0x10003C40,
                        'func_10004514': 0x10004514, 'func_10004074': 0x10004074,
                        'func_10006240': 0x10006240, 'func_150AD770': 0x150AD770})
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', names[0],
            *(f'--defsym={name}=0x{value:X}' for name, value in targets.items()), '-o', str(elf), str(obj)],
            check=True, capture_output=True)
        fresh, _, _ = match_progress.load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        production, _, addresses = match_progress.load_elf_functions(
            str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        measurements = {
            'func_15003570': (58, 62, 0x30, 54, '096cbdac52e624b1a23fd8f3f7430477801c27d22ab78fb3b57418a95138fb06'),
            'func_1510D404': (125, 129, 0x40, 119, 'eccdb2fdca0e14d179f3f0e7299448b7dd41135e17ae14d53922683f615ee991'),
        }
        for name, (body, size, frame, different, digest) in measurements.items():
            words = fresh[name]
            count = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
            self.assertEqual(count, body)
            self.assertEqual(words[count:], [0] * (len(words) - count))
            slot = words[:body] + [0] * (size - body)
            self.assertEqual(production[name], slot)
            self.assertEqual(addresses[name], int(name[5:], 16))
            self.assertEqual(0x10000 - (slot[0] & 0xFFFF), frame)
            first = 0x2D4B0 + addresses[name] - 0x15000000
            retail = struct.unpack_from('>' + str(size) + 'I', rom, first)
            self.assertEqual(sum(a != b for a, b in zip(slot, retail)), different)
            self.assertEqual(hashlib.sha256(struct.pack('>' + str(size) + 'I', *slot)).hexdigest(), digest)
        for name, size in (('func_150034B4', 47), ('func_15007830', 124),
                           ('func_1510D374', 36), ('func_15168E34', 8)):
            first = 0x2D4B0 + addresses[name] - 0x15000000
            self.assertEqual(struct.pack('>' + str(size) + 'I', *production[name]), rom[first:first + size * 4])
        print('metadata/maintenance:', {name: value[:4] for name, value in measurements.items()})

    def test_shared_header_rebuild_keeps_complete_init_debugger_and_game_data_exact(self):
        root = self.root / 'conker'
        config = yaml.safe_load((root / 'conker.us.yaml').read_text())
        rom = (root / 'conker.us.bin').read_bytes()
        data = (root / 'build/conker.us.elf').read_bytes()
        header = ELF_HEADER.unpack_from(data)
        self.assertEqual(header[0][:7], b'\x7fELF\x01\x02\x01')
        self.assertEqual(header[1:3], (2, 8))
        sections = list(SECTION_HEADER.iter_unpack(data[header[6]:header[6] + header[11] * header[12]]))
        strings = sections[header[13]]
        names = data[strings[4]:strings[4] + strings[5]]
        for name in ('init', 'init_data', 'debugger', 'game_data'):
            segment = next(s for s in config['segments'] if isinstance(s, dict) and s.get('name') == name)
            section, = [s for s in sections if read_c_string(names, s[0]) == '.' + name]
            body = data[section[4]:section[4] + section[5]]
            self.assertEqual(section[3], segment['vram'])
            self.assertEqual(body, rom[segment['start']:segment['start'] + len(body)], name)


if __name__ == '__main__':
    unittest.main()
