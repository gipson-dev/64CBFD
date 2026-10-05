"""Actual cache/lookup/block C; DMA, allocation and decoder remain bounded fixtures."""

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


class GameAssetTableLookupAndBlockLoadTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.source = (cls.root / 'conker/src/game_57FA0.c').read_text()
        cls.layout = re.search(r'typedef struct AssetTableCache57FA0 \{.*?\} AssetTableCache57FA0;',
                               cls.source, re.S).group(0)
        cls.bodies = [re.search(pattern, cls.source, re.S).group(0) for pattern in (
            r'void func_1502AB04\([^;{}]+\) \{\n.*?\n\}',
            r's32 func_1502AC88\([^;{}]+\) \{\n.*?\n\}',
            r'void \*func_1502B350\([^;{}]+\) \{\n.*?\n\}')]
        cls.types = ('typedef unsigned char u8; typedef int s32; typedef unsigned int u32;\n'
                     '#define NULL ((void *)0)\n' + cls.layout + '\n')
        cls.declarations = r'''
extern AssetTableCache57FA0 D_800C3D68[16];
extern u32 D_800C3D60, D_8003809C;
void bcopy(void *, void *, s32);
s32 func_10004514(u32, void *, u32, s32);
void *allocate_memory(s32, s32, s32, s32);
void func_10004074(void *);
s32 func_10006240(void *, void *, u32);
'''
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = cls.types + cls.declarations + r'''
AssetTableCache57FA0 D_800C3D68[16], before[16];
u32 D_800C3D60, D_8003809C;
static u32 pairs[32], dmaWords[8], compressed[16], expanded[16];
static int copies, dmas, allocations, frees, decodes, error, failAllocation, lookupMode;
static int mutateClock, mutateFree, connected, dmaPhase;
static u32 expectedAddress, expectedLength, expectedGeneration, expandedSize, descriptor;
static u32 connectedAddress;
static s32 output, decoderResult;
static s32 *outputPointer;
static char trace[32]; static int traceLength;
static void push(char c) { if(traceLength<32) trace[traceLength++]=c; else error=1; }
static int trace_is(const char *s) {
    int i=0; while(s[i]) { if(i>=traceLength || trace[i]!=s[i]) return 0; i++; }
    return i==traceLength;
}
static int equal(AssetTableCache57FA0 a, AssetTableCache57FA0 b) {
    return a.address==b.address && a.generation==b.generation && a.offset==b.offset && a.descriptor==b.descriptor;
}
static void reset(void) {
    int i;
    for(i=0;i<16;i++) {
        D_800C3D68[i].address=0x90000000+(u32)i*8;
        D_800C3D68[i].generation=100+(u32)i;
        D_800C3D68[i].offset=200+(u32)i;
        D_800C3D68[i].descriptor=300+(u32)i;
        before[i]=D_800C3D68[i]; compressed[i]=expanded[i]=0xA5A5A5A5;
        pairs[2*i]=0x80000000+(u32)i; pairs[2*i+1]=0xF0000000+(u32)i;
    }
    for(i=0;i<8;i++) dmaWords[i]=1000+(u32)i;
    D_800C3D60=77; D_8003809C=0x1234;
    copies=dmas=allocations=frees=decodes=error=failAllocation=mutateClock=mutateFree=connected=dmaPhase=0;
    lookupMode=0; expectedAddress=0x12340; expectedLength=16; expectedGeneration=78;
    expandedSize=48; descriptor=0x1000000F; output=-99; outputPointer=&output;
    decoderResult=24; traceLength=0;
}
void bcopy(void *source, void *destination, s32 length) {
    u8 *s=source,*d=destination; int i;
    push('C'); copies++;
    if(destination!=D_800C3D68 || length<0 || length>256) error=2;
    for(i=0;i<length;i++) d[i]=s[i];
}
void *allocate_memory(s32 length,s32 b,s32 c,s32 d) {
    push('A'); allocations++;
    if(b!=1 || c!=2 || d!=2 || allocations>2) error=3;
    if(allocations==1) {
        if((u32)length!=(((descriptor&0x0FFFFFFF)+1)&~1u)) error=4;
        if(connected) { expectedAddress=connectedAddress; expectedLength=16; }
    } else {
        if((u32)length!=expandedSize || (u32)*outputPointer!=expandedSize || dmas!=1 || frees) error=5;
        D_8003809C=0x5678;
    }
    if(allocations==failAllocation) return NULL;
    return allocations==1?(void *)compressed:(void *)expanded;
}
s32 func_10004514(u32 address,void *destination,u32 length,s32 mode) {
    u32 *words=destination; int i;
    push('D'); dmas++;
    if(address!=expectedAddress || length!=expectedLength || mode!=1) error=6;
    if(lookupMode) {
        if(((u32)destination&15) || D_800C3D60!=expectedGeneration || allocations) error=7;
        for(i=0;i<(int)(length/4);i++) words[i]=dmaWords[i];
        if(mutateClock) D_800C3D60=123;
    } else if(connected && dmaPhase++==0) {
        if(((u32)destination&15) || length!=32) error=8;
        for(i=0;i<8;i++) words[i]=0;
        words[2]=0x20; words[3]=0x80000010; words[4]=0x40; words[5]=0x80000010;
    } else {
        if(destination!=compressed || allocations!=1 || decodes || frees) error=9;
        compressed[0]=expandedSize|0x80000000;
        if(connected) { compressed[0]=8; compressed[1]=0x80000004; }
    }
    return -1;
}
s32 func_10006240(void *source,void *destination,u32 scratch) {
    push('Z'); decodes++;
    if(source!=compressed || destination!=expanded || scratch!=0x5678 || allocations!=2 || frees
       || (u32)*outputPointer!=expandedSize) error=10;
    return decoderResult;
}
void func_10004074(void *pointer) {
    push('F'); frees++;
    if(pointer!=compressed || frees!=1) error=11;
    if(mutateFree) *outputPointer=-333;
}
''' + '\n'.join(cls.bodies) + '\n'

    def test_cache_installs_every_supported_count_and_zero_is_noop(self):
        self.run_host(r'''
int n,i;
for(n=0;n<=16;n++) {
    reset(); func_1502AB04(n,n?pairs:NULL,0xFFFFFFFF,0xFFFFFFF8);
    if(error || copies!=(n!=0) || allocations || dmas) return 1;
    for(i=0;i<16-n;i++) if(!equal(D_800C3D68[i],before[i+n])) return 2;
    for(i=16-n;i<16;i++) {
        int j=i-(16-n); AssetTableCache57FA0 a=D_800C3D68[i];
        if(a.address!=0xFFFFFFF8+(u32)j*8 || a.generation!=0xFFFFFFFF
           || a.offset!=pairs[2*j] || a.descriptor!=pairs[2*j+1]) return 3;
    }
}
''')

    def test_cache_shift_precedes_reading_aliased_input_pairs(self):
        self.run_host(r'''
reset(); func_1502AB04(2,&D_800C3D68[0].offset,41,0x80001234);
if(error || copies!=1 || D_800C3D68[14].offset!=before[2].offset
   || D_800C3D68[14].descriptor!=before[2].descriptor
   || D_800C3D68[15].offset!=before[3].address
   || D_800C3D68[15].descriptor!=before[3].generation) return 1;
''')

    def test_cache_all_bounded_word_aligned_input_aliases_keep_sequential_reads(self):
        self.run_host(r'''
int n,k,i,j,cases=0; u32 expected[64];
for(n=0;n<=16;n++) for(k=0;k<=64-2*n;k++) {
    u32 address=0xFFFFFFF8;
    reset();
    for(i=0;i<64;i++) expected[i]=((u32 *)D_800C3D68)[i];
    if(n) for(i=0;i<(16-n)*4;i++) expected[i]=expected[i+n*4];
    for(i=16-n,j=k;i<16;i++,j+=2) {
        expected[i*4+2]=expected[j];
        expected[i*4+3]=expected[j+1];
        expected[i*4]=address;
        expected[i*4+1]=41;
        address+=8;
    }
    func_1502AB04(n,(u32 *)D_800C3D68+k,41,0xFFFFFFF8);
    if(error || copies!=(n!=0) || allocations || dmas) return 1;
    for(i=0;i<64;i++) if(((u32 *)D_800C3D68)[i]!=expected[i]) return 2;
    cases++;
}
if(cases!=833) return 3;
''')

    def test_hit_all_positions_and_duplicate_first_match(self):
        self.run_host(r'''
int hit,i;
for(hit=0;hit<16;hit++) {
    reset(); D_800C3D68[hit].address=0x80012340; before[hit]=D_800C3D68[hit];
    if(hit<15) { D_800C3D68[15].address=0x80012340; before[15]=D_800C3D68[15]; }
    if((u32)func_1502AC88(0x12350,-2,(u32 *)&output)!=before[hit].offset
       || (u32)output!=before[hit].descriptor || error || copies || dmas || D_800C3D60!=77) return 1;
    for(i=0;i<15;i++) if(!equal(D_800C3D68[i],before[i+(i>=hit)])) return 2;
    before[hit].generation=77;
    if(!equal(D_800C3D68[15],before[hit])) return 3;
}
''')

    def test_hit_output_alias_observes_post_store_return_read(self):
        self.run_host(r'''
reset(); D_800C3D68[3].address=0x80012340;
if((u32)func_1502AC88(0x12340,0,&D_800C3D68[15].offset)!=303
   || D_800C3D68[15].offset!=303 || dmas || copies || error) return 1;
reset(); D_800C3D68[3].address=0x80012340;
if((u32)func_1502AC88(0x12340,0,&D_800C3D60)!=203 || D_800C3D60!=303
   || D_800C3D68[15].generation!=77 || error) return 2;
''')

    def test_miss_alignment_pair_selection_generation_and_neighbor_hit(self):
        self.run_host(r'''
int low,i;
for(low=0;low<16;low+=4) {
    reset(); lookupMode=1; expectedLength=low?32:16;
    if((u32)func_1502AC88(0x12340+(u32)low,0,(u32 *)&output)!=dmaWords[low/4]
       || (u32)output!=dmaWords[low/4+1] || error || dmas!=1 || copies!=1 || D_800C3D60!=78) return 1;
    for(i=0;i<14;i++) if(!equal(D_800C3D68[i],before[i+2])) return 2;
    if(D_800C3D68[14].address!=0x80012340+(u32)low || D_800C3D68[15].address!=0x80012348+(u32)low
       || D_800C3D68[15].offset!=dmaWords[low/4+2] || D_800C3D68[14].generation!=78) return 3;
    if((u32)func_1502AC88(0x12340+(u32)low,1,(u32 *)&output)!=dmaWords[low/4+2]
       || (u32)output!=dmaWords[low/4+3] || dmas!=1 || copies!=1 || error) return 4;
}
''')

    def test_miss_clock_wrap_live_dma_mutation_and_output_alias(self):
        self.run_host(r'''
reset(); lookupMode=1; D_800C3D60=0xFFFFFFFF; expectedGeneration=0; mutateClock=1;
if((u32)func_1502AC88(0x12350,-2,(u32 *)&output)!=1000 || error || D_800C3D60!=123
   || D_800C3D68[14].generation!=123 || D_800C3D68[15].generation!=123) return 1;
reset(); lookupMode=1;
if((u32)func_1502AC88(0x12340,0,&D_800C3D60)!=1000 || error || D_800C3D60!=1001
   || D_800C3D68[14].generation!=1001 || D_800C3D68[15].generation!=1001) return 2;
reset(); lookupMode=1;
if((u32)func_1502AC88(0x12340,0,&D_800C3D68[15].offset)!=1000 || error
   || D_800C3D68[13].offset!=1001 || D_800C3D68[15].offset!=1002) return 3;
''')

    def test_plain_modes_even_allocation_and_separate_dma_rounding(self):
        self.run_host(r'''
int flag,i; static u32 lengths[]={0,1,2,15,16,17,0x0FFFFFFE,0x0FFFFFFF};
for(flag=0;flag<16;flag++) if((flag&7)!=1) for(i=0;i<8;i++) {
    u32 amount; reset(); descriptor=((u32)flag<<28)|lengths[i];
    amount=((descriptor&0x0FFFFFFF)+1)&~1u; expectedLength=(amount+15)&~15u;
    if(func_1502B350(expectedAddress,descriptor,&output)!=compressed || error || (u32)output!=amount
       || allocations!=1 || dmas!=1 || frees || decodes || !trace_is("AD")) return 1;
}
''')

    def test_first_allocation_failure_keeps_output_untouched(self):
        self.run_host(r'''
reset(); failAllocation=1;
if(func_1502B350(expectedAddress,descriptor,&output) || output!=-99 || error
   || allocations!=1 || dmas || frees || decodes || !trace_is("A")) return 1;
''')

    def test_compressed_header_limits_and_cleanup_store_order(self):
        self.run_host(r'''
static u32 sizes[]={0,1,999999,1000000,0x7FFFFFFF}; int i;
for(i=0;i<5;i++) {
    int valid=sizes[i]>0 && sizes[i]<1000000;
    reset(); expandedSize=sizes[i]; mutateFree=1;
    if(func_1502B350(expectedAddress,descriptor,&output)!=(valid?(void *)expanded:NULL)
       || output!=(valid?24:0) || error || allocations!=(valid?2:1) || dmas!=1 || frees!=1
       || decodes!=valid || !trace_is(valid?"ADAZF":"ADF")) return 1;
}
''')

    def test_second_allocation_failure_and_decoder_zero_or_negative_result(self):
        self.run_host(r'''
static s32 results[]={0,-1,(s32)0x80000000,48}; int i;
reset(); failAllocation=2; mutateFree=1;
if(func_1502B350(expectedAddress,descriptor,&output) || output || error || allocations!=2
   || decodes || frees!=1 || !trace_is("ADAF")) return 1;
for(i=0;i<4;i++) {
    reset(); descriptor=0x9000000F; decoderResult=results[i]; mutateFree=1;
    if(func_1502B350(expectedAddress,descriptor,&output)!=expanded || error || output!=results[i]
       || frees!=1 || !trace_is("ADAZF")) return 2;
}
''')

    def test_compressed_output_aliases_header_without_losing_captured_size(self):
        self.run_host(r'''
reset(); outputPointer=(s32 *)compressed;
if(func_1502B350(expectedAddress,descriptor,outputPointer)!=expanded || error
   || compressed[0]!=24 || output!=-99 || !trace_is("ADAZF")) return 1;
''')

    def test_connected_actual_lookup_block_variadic_loader_and_relocator(self):
        loader=re.search(r'void \*func_1502B6BC\([^;{}]+\) \{\n.*?\n\}',self.source,re.S).group(0)
        relocator=re.search(r's32 func_1502B4A8\([^;{}]+\) \{\n.*?\n\}',self.source,re.S).group(0)
        original=self.fixture
        try:
            self.fixture='#include <stdarg.h>\n'+self.fixture+'u8 D_AB1950[16];\n'+relocator+r'''
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
'''+loader+'\n#pragma GCC diagnostic pop\n'
            self.run_host(r'''
s32 size,relocated; u32 root=(u32)D_AB1950; int phase;
for(phase=0;phase<2;phase++) {
    reset(); connected=1; expectedAddress=(root+8)&0x7FFFFFF0;
    connectedAddress=root+0x20;
    expectedLength=32; descriptor=0x80000010;
    /* Root table symbols on this host are 16-aligned; key component 1 selects pair at +8. */
    if(root&15) return 1;
    if(phase) { D_800C3D68[15].address=(root+8)|0x80000000; D_800C3D68[15].offset=0x20;
               D_800C3D68[15].descriptor=descriptor; dmaPhase=1; }
    size=-99; relocated=-77;
    if(func_1502B6BC(&size,0,&relocated,1,1)!=compressed || error || size!=16 || relocated!=1
       || compressed[0]!=(u32)compressed+8 || compressed[1]!=4 || allocations!=1
       || dmas!=(phase?1:2) || copies!=(phase?0:1) || frees || decodes) return 2;
}
''')
        finally:
            self.fixture=original

    def test_lookup_and_block_have_no_guards_and_retained_alias_is_one_cache(self):
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] in ('func_1502AC88','func_1502B350')
                                 for row in csv.DictReader(source)))
        self.assertNotIn('D_800C3E58',self.source)
        symbols=(self.root/'conker/undefined_syms_auto.txt').read_text()
        self.assertRegex(symbols,r'D_800C3D68\s*=\s*0x800C3D68;')
        self.assertRegex(symbols,r'D_800C3E58\s*=\s*0x800C3E58;')

    def test_fresh_ido_bodies_fit_and_match_production_with_only_call_relocations(self):
        compiler=self.root/'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(n) is None for n in ('mips-linux-gnu-ld','mips-linux-gnu-objdump')):
            self.skipTest('IDO/MIPS tools are unavailable')
        source,obj,elf,script=(self.path/('cache'+suffix) for suffix in ('.c','.o','.elf','.ld'))
        source.write_text(self.types+self.declarations+'\n'.join(self.bodies)+'\n')
        result=subprocess.run([str(compiler),'-c','-32','-G','0','-Xfullwarn','-Xcpluscomm','-signed',
            '-nostdinc','-non_shared','-Wab,-r4300_mul','-mips2','-o32','-O2','-g3',
            '-o',str(obj),str(source)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(result.stdout+result.stderr,'')
        script.write_text('SECTIONS { .text 0x1502AB04 : SUBALIGN(4) { *(.text) } }\n')
        targets={'D_800C3D68':0x800C3D68,'D_800C3D60':0x800C3D60,'D_8003809C':0x8003809C,
                 'bcopy':0x10023A10,'allocate_memory':0x10003C40,'func_10004514':0x10004514,
                 'func_10004074':0x10004074,'func_10006240':0x10006240}
        subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e','func_1502AB04',
            *(f'--defsym={name}=0x{value:X}' for name,value in targets.items()),'-o',str(elf),str(obj)],
            check=True,capture_output=True)
        fresh,_,addresses=match_progress.load_elf_functions(str(elf),'mips-linux-gnu-objdump')
        production,_,placed=match_progress.load_elf_functions(str(self.root/'conker/build/conker.us.elf'),
                                                              'mips-linux-gnu-objdump')
        relocations=subprocess.run(['mips-linux-gnu-objdump','-r',str(obj)],check=True,capture_output=True,text=True).stdout
        call_offsets=[int(offset,16) for offset in re.findall(r'(?m)^([0-9a-f]+)\s+R_MIPS_26\s+func_1502AB04\s*$',relocations)]
        self.assertEqual(len(call_offsets),1)
        measured={'func_1502AB04':(97,97,0x28,41,'a6bca817be8a9ee74df0bc7e91206bd401525478a5f4c39ffb832a9eed82a9bf'),
                  'func_1502AC88':(158,159,0xA0,156,'1bb0909b45c22e6029c8100583e55835d0cea88a3a28efe38ba65524a7f2ca28'),
                  'func_1502B350':(86,86,0x30,0,'f176b2891cb5a8aa6f60461047ea78f4b4e7958fcaef18fb41b9d0c1ccdc31ae')}
        rom=(self.root/'conker/conker.us.bin').read_bytes()
        for name,(body,size,frame,diffs,digest) in measured.items():
            words=fresh[name][:]
            for offset in call_offsets:
                absolute=0x1502AB04+offset
                if addresses[name]<=absolute<addresses[name]+len(words)*4:
                    index=(absolute-addresses[name])//4
                    self.assertEqual(words[index]>>26,3)
                    words[index]=(3<<26)|((0x1502AB04>>2)&0x3FFFFFF)
            count=max(i for i,w in enumerate(words) if w==0x03E00008)+2
            self.assertEqual(count,body)
            self.assertEqual(words[count:],[0]*(len(words)-count))
            slot=words[:count]+[0]*(size-count)
            if name=='func_1502AB04':
                from tools.tests.test_game_cache_installer_match import apply_linked_guards
                self.assertEqual(production[name],apply_linked_guards(slot))
            else:
                self.assertEqual(production[name],slot)
            self.assertEqual(placed[name],int(name[5:],16))
            self.assertEqual(0x10000-(slot[0]&0xFFFF),frame)
            first=0x2D4B0+placed[name]-0x15000000
            retail=struct.unpack_from('>'+str(size)+'I',rom,first)
            self.assertEqual(sum(a!=b for a,b in zip(slot,retail)),diffs)
            self.assertEqual(hashlib.sha256(struct.pack('>'+str(size)+'I',*slot)).hexdigest(),digest)
        print('asset cache/lookup/block:',{name:value[:4] for name,value in measured.items()})


if __name__=='__main__':
    unittest.main()
