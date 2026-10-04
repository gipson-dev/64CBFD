"""Actual texture resolver/setup/attachment C, with bounded allocator/DMA/decoder fixtures."""

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
from tools.tests import test_game_random_curve_record as curve


class GameTextureResourceSetupTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        cls.source=(cls.root/'conker/src/game/generated_139FC0.c').read_text()
        cls.attach_source=(cls.root/'conker/src/game_1944C0.c').read_text()
        cls.bodies={}
        for name,kind,source in (
                ('func_1510CE60','s32',cls.source),('func_1510D0EC','u32',cls.source),
                ('func_1510D374','s32',cls.source),('func_1510D630','void',cls.source),
                ('func_1510D608','void',cls.source),('func_1510D694','void',cls.source),
                ('func_15168E34','void',cls.attach_source),('func_15168E54','void',cls.attach_source)):
            cls.bodies[name]=re.search(kind+' '+name+r'\([^;{}]+\) \{\n.*?\n\}',source,re.S).group(0)
        cls.types=('typedef unsigned char u8; typedef signed char s8; typedef unsigned short u16; '
                   'typedef short s16; typedef int s32; typedef unsigned int u32;\n'
                   '#define NULL ((void *)0)\n')
        cls.declarations=r'''
extern u16 D_80091D20[], D_800B87A0[];
extern u32 D_800B0E58[], D_8003809C;
extern s8 D_800BC448[];
extern u8 D_800D9F68[], D_800DBDBA, D_1A37E0;
extern s32 D_800D9F58, D_800D9F5C;
void *allocate_memory(s32,s32,s32,s32);
void *func_10003C6C(s32,s32,s32,s32,s32);
s32 func_10004514(s32,void *,u32,s32);
void func_10004074(void *);
s32 func_10006240(void *,void *,u32);
u32 func_1510D0EC(s32,s32 *,s32,s32);
s32 func_1510D374(s32);
void func_1510D694(s32);
void func_1510D608(s32,s32);
void func_15168E34(s32 *,s32);
'''
        cls.directory=tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path=Path(cls.directory.name)
        cls.fixture=cls.types+cls.declarations+r'''
u16 D_80091D20[7762],D_800B87A0[7762];
u32 D_800B0E58[7762],D_8003809C;
s8 D_800BC448[7762];
u8 D_800D9F68[7762],D_800DBDBA,D_1A37E0 __attribute__((aligned(16)));
s32 D_800D9F58,D_800D9F5C;
static u32 compressed[32],expanded[32],commands[40];
static s16 listStorage[7764];
static int allocations,listAllocations,dmas,decodes,frees,error,failAllocation,failList;
static int expectedId,mutateDma,mutateDecode,mutateFree,freeList;
static s32 seenListBytes;
static s32 extent,output,decoderResult;
static u32 expectedSource,expectedAmount,expectedSize,expectedSkip;
static s32 *extentPointer;
static char trace[64]; static int traceLength;
static void push(char c) { if(traceLength<64) trace[traceLength++]=c; else error=1; }
static int trace_is(const char *s) {
    int i=0; while(s[i]) { if(i>=traceLength || s[i]!=trace[i]) return 0; i++; }
    return i==traceLength;
}
static void reset(void) {
    int i;
    for(i=0;i<7762;i++) { D_80091D20[i]=0; D_800B87A0[i]=0;
        D_800B0E58[i]=0xFFFFFFFF; D_800BC448[i]=0; D_800D9F68[i]=0; }
    for(i=0;i<40;i++) commands[i]=0xA5A5A5A5;
    for(i=0;i<7764;i++) listStorage[i]=(s16)0xA5A5;
    allocations=listAllocations=dmas=decodes=frees=error=failAllocation=failList=0;
    mutateDma=mutateDecode=mutateFree=freeList=0; traceLength=0;
    seenListBytes=0;
    D_800D9F58=7762; D_800D9F5C=-1; D_800DBDBA=0; D_8003809C=0x1234;
    expectedId=1; D_80091D20[1]=17; D_800B87A0[1]=64;
    expectedSource=(u32)&D_1A37E0; expectedSkip=0; expectedAmount=32; expectedSize=64;
    extent=-99; output=-77; extentPointer=&extent; decoderResult=64;
}
static void command(int index,s8 opcode,u8 subtype,u32 word) {
    commands[index*2]=0; ((s8 *)commands)[index*8]=opcode;
    ((u8 *)commands)[index*8+3]=subtype; commands[index*2+1]=word;
}
static void cached(int id,u32 address,u16 size) {
    D_80091D20[id]=1; D_800B0E58[id]=address; D_800B87A0[id]=size;
}
void *allocate_memory(s32 length,s32 b,s32 c,s32 d) {
    push('L'); listAllocations++;
    seenListBytes=length;
    if(length<2 || length>15538 || b!=1 || c || d!=2 || listAllocations>1) error=2;
    return failList?NULL:listStorage;
}
void *func_10003C6C(s32 length,s32 b,s32 c,s32 d,s32 e) {
    push('A'); allocations++;
    if(b!=1 || e!=2 || allocations>2) error=3;
    if(allocations==1) {
        if((u32)length!=expectedAmount || c!=2 || d!=1 || D_800DBDBA!=5) error=4;
    } else {
        if((u32)length!=expectedSize || c!=1 || d || dmas!=1) error=5;
        D_8003809C=0x5678;
    }
    return allocations==failAllocation?NULL:allocations==1?(void *)compressed:(void *)expanded;
}
s32 func_10004514(s32 source,void *destination,u32 length,s32 mode) {
    push('D'); dmas++;
    if((u32)source!=expectedSource || destination!=compressed || length!=expectedAmount || mode!=1
       || allocations!=1 || decodes || frees) error=6;
    if(mutateDma) { D_800B87A0[expectedId]=96; expectedSize=96; }
    return -1;
}
s32 func_10006240(void *source,void *destination,u32 scratch) {
    push('Z'); decodes++;
    if(source!=(u8 *)compressed+expectedSkip || destination!=expanded || scratch!=0x5678
       || allocations!=2 || dmas!=1 || frees) error=7;
    if(mutateDecode) { D_800B87A0[expectedId]=112; D_800D9F68[expectedId]=200; }
    return decoderResult;
}
void func_10004074(void *pointer) {
    push('F'); frees++;
    if(pointer!=(freeList?(void *)listStorage:(void *)compressed)) error=8;
    if(mutateFree) { D_800B87A0[expectedId]=128; *extentPointer=-123; }
}
'''+cls.bodies['func_1510D374']+'\n'+cls.bodies['func_1510D0EC']+r'''
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
'''+cls.bodies['func_1510CE60']+'\n#pragma GCC diagnostic pop\n'+ '\n'.join(
            cls.bodies[n] for n in ('func_15168E34','func_15168E54','func_1510D608','func_1510D694','func_1510D630'))+'\n'

    def test_resolver_invalid_ids_update_range_without_table_or_output_access(self):
        self.run_host(r'''
static s32 ids[]={-1,(s32)0x80000000,7762,0x7FFFFFFF}; int i;
for(i=0;i<4;i++) {
    reset(); if(func_1510D0EC(ids[i],&extent,63,1)!=0x80000000 || extent!=-99
        || allocations || dmas || frees || error || D_800DBDBA) return 1;
    if(D_800D9F58!=(ids[i]<7762?ids[i]:7762) || D_800D9F5C!=(ids[i]>-1?ids[i]:-1)) return 2;
}
''')

    def test_zero_size_overwrites_cache_but_still_publishes_extent_and_activity(self):
        self.run_host(r'''
reset(); D_80091D20[1]=0; D_800B0E58[1]=0x12345678; D_800D9F68[1]=254;
if(func_1510D0EC(1,&extent,63,-1)!=0x80000000 || extent!=64 || allocations || error
   || D_800B0E58[1]!=0x80000000 || D_800BC448[1]!=63 || D_800D9F68[1]!=255) return 1;
if(func_1510D0EC(1,NULL,0,1)!=0x80000000 || D_800D9F68[1]!=255 || error) return 2;
''')

    def test_cached_signed_priority_truncation_and_saturating_activity(self):
        self.run_host(r'''
static s32 priorities[]={-129,-128,-1,0,62,63,127,128,255};
static s32 states[]={-128,-1,0,62,127}; int p,s,count;
for(p=0;p<9;p++) for(s=0;s<5;s++) for(count=0;count<=255;count+=51) {
    reset(); cached(7761,0x81234567,0xFFFF); D_800BC448[7761]=(s8)states[s];
    D_800D9F68[7761]=(u8)count;
    if(func_1510D0EC(7761,&extent,priorities[p],1)!=0x81234567 || extent!=65535 || error
       || D_800BC448[7761]!=(s8)(states[s]<priorities[p]?priorities[p]:states[s])
       || D_800D9F68[7761]!=(count<255?count+1:255) || allocations || D_800DBDBA) return 1;
}
''')

    def test_miss_alignment_both_allocation_flags_and_no_decoder_result_gate(self):
        self.run_host(r'''
int odd,size; static s32 results[]={0,-1,64}; int r;
for(odd=0;odd<2;odd++) for(size=1;size<=33;size++) for(r=0;r<3;r++) {
    reset(); D_80091D20[0]=(u16)odd; D_80091D20[1]=(u16)size;
    expectedSkip=(u32)odd; expectedAmount=((u32)size+(u32)odd+1)&~1u;
    expectedAmount=(expectedAmount+15)&~15u; decoderResult=results[r];
    if(func_1510D0EC(1,&extent,63,1)!=(u32)expanded || error || extent!=64
       || D_800BC448[1]!=62 || D_800D9F68[1]!=1 || D_800B0E58[1]!=(u32)expanded
       || !trace_is("ADAZF")) return 1;
}
''')

    def test_allocation_failures_leave_extent_cache_state_and_activity_untouched(self):
        self.run_host(r'''
int fail;
for(fail=1;fail<=2;fail++) {
    reset(); failAllocation=fail; D_800BC448[1]=7; D_800D9F68[1]=9;
    if(func_1510D0EC(1,&extent,63,1)!=0x80000000 || error || extent!=-99
       || D_800B0E58[1]!=0xFFFFFFFF || D_800BC448[1]!=7 || D_800D9F68[1]!=9
       || D_800DBDBA!=5 || frees!=(fail==2) || decodes
       || !trace_is(fail==1?"A":"ADAF")) return 1;
}
''')

    def test_fresh_table_scratch_and_output_reads_across_callbacks(self):
        self.run_host(r'''
reset(); mutateDma=mutateDecode=mutateFree=1; D_800D9F68[1]=250;
if(func_1510D0EC(1,&extent,5,1)!=(u32)expanded || error || extent!=128
   || D_800D9F68[1]!=1 || D_800BC448[1]!=5 || !trace_is("ADAZF")) return 1;
reset(); cached(1,0x81234567,73);
if(func_1510D0EC(1,(s32 *)&D_800B0E58[1],0,0)!=73 || D_800B0E58[1]!=73 || error) return 2;
''')

    def test_empty_setup_optional_tracking_and_cleanup_failure_independent_of_success(self):
        self.run_host(r'''
reset(); command(0,-0x21,0,0); commands[2]=123;
if(!func_1510CE60(commands,0,1,62,NULL) || allocations || listAllocations || error || commands[2]!=123) return 1;
if(!func_1510CE60(commands,0,1,62,&output) || output!=(s32)listStorage || listStorage[0]
   || listStorage[1]!=(s16)0xA5A5 || seenListBytes!=2 || !trace_is("L") || error) return 2;
reset(); command(0,-0x21,0,0); failList=1;
if(!func_1510CE60(commands,0,1,62,&output) || output || error) return 3;
''')

    def test_setup_unique_sorted_cleanup_ids_and_actual_countdown_release(self):
        self.run_host(r'''
reset(); cached(1,0x81001000,512); cached(9,0x81009000,256); cached(11,0x8100B000,800);
command(0,-3,0,9); command(1,-3,0,1); command(2,-3,0,9); command(3,-3,0,11); command(4,-0x21,0,0);
if(!func_1510CE60(commands,0,1,62,&output) || error || output!=(s32)listStorage
   || listStorage[0]!=3 || listStorage[1]!=1 || listStorage[2]!=9 || listStorage[3]!=11
   || listStorage[4]!=(s16)0xA5A5 || D_800D9F68[9]!=2 || D_800D9F68[1]!=1
   || commands[1]!=0x81009000 || commands[3]!=0x81001000 || commands[5]!=0x81009000
   || commands[7]!=0x8100B000 || seenListBytes!=8 || allocations || !trace_is("L")) return 1;
freeList=1; func_1510D630(listStorage);
if(error || D_800D9F68[1] || D_800D9F68[11] || D_800D9F68[9]!=1
   || D_800BC448[1]!=3 || D_800BC448[11]!=3 || D_800BC448[9]!=62 || !trace_is("LF")) return 2;
''')

    def test_setup_all_valid_ids_fill_bitmap_and_complete_sorted_list(self):
        self.run_host(r'''
u32 many[15526]; int i;
reset();
for(i=0;i<7762;i++) {
    cached(i,0x81000000+(u32)i*8,64); many[i*2]=0; ((s8 *)many)[i*8]=-3; many[i*2+1]=(u32)i;
}
many[15524]=0; ((s8 *)many)[7762*8]=-0x21; many[15525]=0xA5A5A5A5;
if(!func_1510CE60(many,0,1,62,&output) || error || output!=(s32)listStorage
   || seenListBytes!=15526 || listStorage[0]!=7762 || listStorage[7763]!=(s16)0xA5A5
   || D_800D9F58 || D_800D9F5C!=7761 || allocations || !trace_is("L")) return 1;
for(i=0;i<7762;i++) if(listStorage[i+1]!=i || D_800D9F68[i]!=1
    || many[i*2+1]!=0x81000000+(u32)i*8) return 2;
''')

    def test_setup_adjustments_filters_and_previous_result_for_tagged_commands(self):
        self.run_host(r'''
int only,tag;
for(only=0;only<2;only++) for(tag=0;tag<256;tag++) {
    u32 raw=((u32)tag<<24)|9; reset(); cached(1,0x81001000,800); cached(9,0x81009000,800);
    command(0,-3,0,1); command(1,-3,0,raw); command(2,1,0,9); command(3,-0x21,0,0);
    if(!func_1510CE60(commands,only,1,62,NULL) || error || listAllocations || allocations
       || commands[1]!=0x81001000 || commands[3]!=(tag?raw:0x81009000)
       || commands[5]!=9 || D_800D9F68[9]!=(tag?0:1)) return 1;
}
for(tag=0;tag<4;tag++) {
    u32 expected=0xFFFFFF80; reset(); cached(1,expected,800);
    command(0,-3,0,((u32)tag<<22)|1); command(1,-0x21,0,0);
    if(tag&1) expected+=800-512; else if(tag&2) expected+=800-32;
    if(!func_1510CE60(commands,0,1,62,NULL) || commands[1]!=expected || error) return 2;
}
''')

    def test_setup_resolver_failure_still_tracks_and_preserves_previous_extent(self):
        self.run_host(r'''
reset(); cached(9,0x81009000,800); failAllocation=1;
command(0,-3,0,9); command(1,-3,0,0x400001); command(2,-0x21,0,0);
if(func_1510CE60(commands,0,1,62,&output) || error || commands[3]!=0x80000000+800-512
   || listStorage[0]!=2 || listStorage[1]!=1 || listStorage[2]!=9
   || D_800D9F68[9]!=1 || D_800D9F68[1] || !trace_is("AL")) return 1;
reset(); command(0,-3,0,1); command(1,-0x21,0,0); failAllocation=failList=1;
if(func_1510CE60(commands,0,1,62,&output) || output || commands[1]!=0x80000000
   || error || !trace_is("AL")) return 2;
''')

    def test_setup_zero_retain_optional_list_and_aliased_output(self):
        self.run_host(r'''
reset(); cached(1,0x81001000,800); command(0,-3,0,1); command(1,-0x21,0,0);
if(!func_1510CE60(commands,0,0,-1,(s32 *)&commands[1]) || error || D_800D9F68[1]
   || D_800BC448[1] || commands[1]!=(u32)listStorage || listStorage[0]!=1 || listStorage[1]!=1) return 1;
''')

    def test_attachment_selected_commands_and_segment_gate_use_actual_leaf(self):
        self.run_host(r'''
static u32 words[]={0,1,0xFFFFFFFF,0x80000000,0x10000000,0x01000000,0x0F000000};
int i;
for(i=0;i<7;i++) {
    u32 expected=(words[i]&0x0F000000)?words[i]:words[i]+0xFFFFFFF0;
    reset(); command(0,1,0,words[i]); command(1,-0x24,14,words[i]);
    command(2,-0x24,13,words[i]); command(3,-3,14,words[i]); command(4,-0x21,0,words[i]);
    command(5,1,0,words[i]);
    func_15168E54(commands,(void *)0xFFFFFFF0);
    if(error || commands[1]!=expected || commands[3]!=expected || commands[5]!=words[i]
       || commands[7]!=words[i] || commands[9]!=words[i] || commands[11]!=words[i] || traceLength) return 1;
}
reset(); command(0,-0x21,0,0); command(1,1,0,1); func_15168E54(commands,NULL);
if(commands[3]!=1 || error) return 2;
''')

    def test_actual_resource_helper_setup_resolver_and_attachment_connection(self):
        source=(self.root/'conker/src/game/generated_15F680.c').read_text()
        helper=re.search(r's32 func_151336A8\([^;{}]+\) \{\n.*?\n\}',source,re.S).group(0)
        layouts='\n'.join(re.search(r'typedef struct '+name+r' \{.*?\} '+name+';',source,re.S).group(0)
                          for name in ('ExtendedResource15F680','ExtendedResourceNode15F680'))
        original=self.fixture
        try:
            self.fixture+='#include <stdarg.h>\n'+layouts+r'''
s32 D_800A3880[236],D_800DC640[234];
static ExtendedResource15F680 resource;
static ExtendedResourceNode15F680 node;
static int failLoad;
void *func_1502B6BC(s32 *size,s32 count,s32 *relocated,s32 depth,...) {
    va_list path; int a,b;
    va_start(path,depth); a=va_arg(path,s32); b=va_arg(path,s32); va_end(path);
    push('H');
    if(!size || count || !relocated || depth!=2 || a!=9 || b!=0xC6) error=9;
    *size=16; *relocated=1;
    return failLoad?NULL:&resource;
}
'''+helper+'\n'
            self.run_host(r'''
int phase;
for(phase=0;phase<4;phase++) {
    reset(); failLoad=phase==1; failList=phase==3; D_800A3880[7]=0xC6; D_800DC640[7]=-77;
    cached(1,0x81001000,800); command(0,-3,0,1); command(1,1,0,8); command(2,-0x21,0,0);
    resource.data=commands; node.resource=(void *)1;
    if(phase==2) D_80091D20[1]=0;
    if(func_151336A8(7,&node,NULL)!=(phase==1?0:1) || error) return 1;
    if(phase==1) { if(node.resource || D_800DC640[7]!=-77 || !trace_is("H")) return 2; }
    else if(node.resource!=&resource || commands[1]!=(phase==2?0x80000000:0x81001000)
       || commands[3]!=(u32)&resource+8 || D_800DC640[7]!=(phase==3?0:(s32)listStorage)
       || D_800D9F68[1]!=1 || seenListBytes!=4 || !trace_is("HL")) return 3;
}
''')
        finally:
            self.fixture=original

    def test_unspecified_scratch_and_no_new_guards_are_explicit(self):
        self.assertRegex(self.bodies['func_1510CE60'],r'\bu32 address;')
        self.assertRegex(self.bodies['func_1510CE60'],r'\bs32 extent;')
        self.assertNotRegex(self.bodies['func_1510CE60'],r'(?:address|extent)\s*=\s*0;')
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] in ('func_1510CE60','func_1510D0EC','func_15168E54')
                                 for row in csv.DictReader(source)))

    def test_fresh_ido_complete_slots_and_exact_prefix_and_adjustment_leaves(self):
        compiler=self.root/'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(n) is None for n in ('mips-linux-gnu-ld','mips-linux-gnu-objdump')):
            self.skipTest('IDO/MIPS tools are unavailable')
        source,obj,elf,script=(self.path/('texture'+suffix) for suffix in ('.c','.o','.elf','.ld'))
        names=('func_1510CE60','func_1510D0EC','func_15168E54')
        source.write_text(self.types+self.declarations+'\n'.join(self.bodies[n] for n in names)+'\n')
        result=subprocess.run([str(compiler),'-c','-32','-G','0','-Xfullwarn','-Xcpluscomm','-signed',
            '-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32','-O2','-g3',
            '-o',str(obj),str(source)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(result.stdout+result.stderr,'')
        script.write_text('SECTIONS { .text 0x1510CE60 : SUBALIGN(4) { *(.text) } }\n')
        targets={'D_80091D20':0x80091D20,'D_800B87A0':0x800B87A0,'D_800B0E58':0x800B0E58,
                 'D_8003809C':0x8003809C,'D_800BC448':0x800BC448,'D_800D9F68':0x800D9F68,
                 'D_800DBDBA':0x800DBDBA,'D_800D9F58':0x800D9F58,'D_800D9F5C':0x800D9F5C,
                 'allocate_memory':0x10003C40,'func_10003C6C':0x10003C6C,'func_10004514':0x10004514,
                 'func_10004074':0x10004074,'func_10006240':0x10006240,
                 'func_1510D374':0x1510D374,'func_15168E34':0x15168E34}
        subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e','func_1510CE60',
            *(f'--defsym={name}=0x{value:X}' for name,value in targets.items()),'-o',str(elf),str(obj)],
            check=True,capture_output=True)
        fresh,_,addresses=match_progress.load_elf_functions(str(elf),'mips-linux-gnu-objdump')
        production,_,placed=match_progress.load_elf_functions(str(self.root/'conker/build/conker.us.elf'),
                                                              'mips-linux-gnu-objdump')
        relocations=subprocess.run(['mips-linux-gnu-objdump','-r',str(obj)],check=True,capture_output=True,text=True).stdout
        offsets=[int(offset,16) for offset in re.findall(r'(?m)^([0-9a-f]+)\s+R_MIPS_26\s+func_1510D0EC\s*$',relocations)]
        self.assertEqual(len(offsets),1)
        measured={'func_1510CE60':(152,163,0x430,159,'6ab58d90d8e1815a475fb86e64aa89b31da2a19f6f4e531c96dd158e6b98395c'),
                  'func_1510D0EC':(155,162,0x50,142,'1fde6b630576ea95a7e990c9402eb31491b7271ff8acd7ec181ad3b42b9100c9'),
                  'func_15168E54':(45,45,0x38,9,'958dcb84bbf375ebdd6c9170744538d8a59afb5385c31977ab50158843aca792')}
        rom=(self.root/'conker/conker.us.bin').read_bytes()
        for name,(body,size,frame,diffs,digest) in measured.items():
            words=fresh[name][:]
            for offset in offsets:
                absolute=0x1510CE60+offset
                if addresses[name]<=absolute<addresses[name]+len(words)*4:
                    index=(absolute-addresses[name])//4
                    self.assertEqual(words[index]>>26,3)
                    words[index]=(3<<26)|((0x1510D0EC>>2)&0x3FFFFFF)
            count=max(i for i,w in enumerate(words) if w==0x03E00008)+2
            self.assertEqual(count,body)
            self.assertEqual(words[count:],[0]*(len(words)-count))
            slot=words[:count]+[0]*(size-count)
            self.assertEqual(production[name],slot)
            self.assertEqual(placed[name],int(name[5:],16))
            self.assertEqual(0x10000-(slot[0]&0xFFFF),frame)
            first=0x2D4B0+placed[name]-0x15000000
            retail=struct.unpack_from('>'+str(size)+'I',rom,first)
            self.assertEqual(sum(a!=b for a,b in zip(slot,retail)),diffs)
            self.assertEqual(hashlib.sha256(struct.pack('>'+str(size)+'I',*slot)).hexdigest(),digest)
        for name,size in (('func_1510D374',36),('func_15168E34',8)):
            first=0x2D4B0+placed[name]-0x15000000
            self.assertEqual(struct.pack('>'+str(size)+'I',*production[name]),rom[first:first+size*4])
        print('texture setup/resolver/attachment:',{name:value[:4] for name,value in measured.items()})


if __name__=='__main__':
    unittest.main()
