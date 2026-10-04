"""Real variadic path traversal/relocation C with explicit lookup/block-load boundaries."""

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
from tools.tests import test_game_extended_child_constructor as constructor


class GameVariadicResourceLoaderTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.source = (cls.root / 'conker/src/game_57FA0.c').read_text()
        cls.body = re.search(r'void \*func_1502B6BC\([^;{}]+\) \{\n.*?\n\}', cls.source, re.S).group(0)
        cls.relocator = re.search(r's32 func_1502B4A8\([^;{}]+\) \{\n.*?\n\}', cls.source, re.S).group(0)
        cls.types = ('typedef unsigned char u8; typedef int s32; typedef unsigned int u32;\n'
                     '#define NULL ((void *)0)\n')
        cls.declarations = r'''
extern u8 D_AB1950[];
s32 func_1502AC88(u32, s32, u32 *);
void *func_1502B350(u32, u32, s32 *);
s32 func_1502B4A8(u32 *, s32);
'''
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = '#include <stdarg.h>\n' + cls.types + cls.declarations + r'''
u8 D_AB1950[16];
static union { u32 words[160]; u8 bytes[640]; } storage;
static u32 *entries=storage.words+4;
static s32 sizeOutput, relocatedOutput, items[24], expectedCount, blockSize;
static u32 metadata[24], advances[24], expectedOffset, seenDescriptor;
static int lookups, blocks, relocations, consumed, error, failBlock, mutateSize;
static int expectedLookupCalls, mutateDescriptor, expectedFallback;
static s32 *sizePointer;
static u32 *lastMetadata;
static char trace[64];
static int traceLength;
static void push(char c) { if(traceLength<63) trace[traceLength++]=c; else error=1; }
static int trace_is(const char *s) {
    int i=0;
    while(s[i]) { if(i>=traceLength || trace[i]!=s[i]) return 0; i++; }
    return i==traceLength;
}
static void reset(void) {
    int i;
    for(i=0;i<160;i++) storage.words[i]=0xA5A5A5A5;
    for(i=0;i<24;i++) { items[i]=100+i; metadata[i]=0xF0000020u+(u32)i; advances[i]=8*(u32)(i+1); }
    sizeOutput=-99; relocatedOutput=-77; expectedCount=2; blockSize=32;
    expectedOffset=(u32)D_AB1950; seenDescriptor=0;
    lookups=blocks=relocations=consumed=error=failBlock=mutateSize=0;
    expectedLookupCalls=2; mutateDescriptor=expectedFallback=0; traceLength=0;
    sizePointer=&sizeOutput; lastMetadata=NULL;
    entries[0]=16; entries[1]=0x10000004; entries[2]=32; entries[3]=0x80000008;
}
static int fences(void) {
    int i;
    for(i=0;i<4;i++) if(storage.words[i]!=0xA5A5A5A5 || storage.words[156+i]!=0xA5A5A5A5) return 1;
    return 0;
}
s32 func_1502AC88(u32 offset, s32 item, u32 *descriptor) {
    int i=lookups++;
    push('Q');
    if(i>=expectedLookupCalls || offset!=expectedOffset || item!=items[i] || !descriptor
       || blocks || relocations || (i==0 && sizePointer && *sizePointer!=1)) error=2;
    *descriptor=metadata[i]; lastMetadata=descriptor;
    expectedOffset+=advances[i];
    if(mutateSize && sizePointer) *sizePointer=-123;
    return (s32)advances[i];
}
void *func_1502B350(u32 offset, u32 descriptor, s32 *size) {
    push('B'); blocks++;
    if(blocks!=1 || lookups!=expectedLookupCalls || offset!=expectedOffset || relocations
       || descriptor!=metadata[lookups-1] || !size || (sizePointer && size!=sizePointer)
       || *size!=(s32)(metadata[lookups-1]&0x0FFFFFFF)) error=3;
    if(!sizePointer) { sizePointer=size; expectedFallback=1; }
    seenDescriptor=descriptor;
    *size=blockSize;
    if(mutateDescriptor) *lastMetadata=0;
    return failBlock?NULL:entries;
}
''' + '#define func_1502B4A8 actual_relocation\n' + cls.relocator + '\n#undef func_1502B4A8\n' + r'''
s32 func_1502B4A8(u32 *data, s32 count) {
    push('R'); relocations++;
    if(blocks!=1 || relocations!=1 || data!=entries || count!=expectedCount || *sizePointer==0) error=4;
    return actual_relocation(data,count);
}
#undef va_arg
#define va_arg(path,type) (consumed++,__builtin_va_arg(path,type))
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
''' + cls.body + '\n#pragma GCC diagnostic pop\n'

    def test_complete_variadic_load_and_actual_relocation(self):
        self.run_host(r'''
reset();
if(func_1502B6BC(&sizeOutput,2,&relocatedOutput,2,items[0],items[1])!=entries
   || error || !trace_is("QQBR") || consumed!=2 || sizeOutput!=32 || relocatedOutput!=2
   || entries[0]!=(u32)entries+16 || entries[2]!=(u32)entries+32
   || entries[1]!=4 || entries[3]!=8 || fences()) return 1;
''')

    def test_many_depths_signed_components_and_wrapping_offsets(self):
        self.run_host(r'''
int depth;
for(depth=1;depth<=16;depth++) {
    reset(); expectedLookupCalls=depth;
    items[0]=(s32)0x80000000; items[1]=-1; items[2]=0x7FFFFFFF;
    advances[0]=0xFFFFFFF0; advances[1]=0x80000001;
    if(func_1502B6BC(&sizeOutput,2,&relocatedOutput,depth,
       items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],
       items[8],items[9],items[10],items[11],items[12],items[13],items[14],items[15])!=entries
       || error || lookups!=depth || consumed!=depth || blocks!=1 || relocations!=1
       || sizeOutput!=32 || relocatedOutput!=2 || seenDescriptor!=metadata[depth-1] || fences()) return 1;
}
''')

    def test_missing_component_stops_lookup_but_consumes_remaining_varargs(self):
        self.run_host(r'''
int missing;
for(missing=0;missing<4;missing++) {
    reset(); metadata[missing]=0xF0000000; expectedLookupCalls=missing+1;
    if(func_1502B6BC(&sizeOutput,2,&relocatedOutput,4,items[0],items[1],items[2],items[3])
       || error || lookups!=missing+1 || consumed!=4 || blocks || relocations
       || sizeOutput || relocatedOutput!=-77 || entries[0]!=16 || entries[1]!=0x10000004 || fences()) return 1;
}
''')

    def test_optional_size_and_relocation_outputs_and_aliasing(self):
        self.run_host(r'''
reset(); sizePointer=NULL;
if(func_1502B6BC(NULL,2,&relocatedOutput,2,items[0],items[1])!=entries
   || error || !expectedFallback || sizeOutput!=-99 || relocatedOutput!=2 || fences()) return 1;
reset();
if(func_1502B6BC(&sizeOutput,2,NULL,2,items[0],items[1])!=entries
   || error || relocatedOutput!=-77 || sizeOutput!=32) return 2;
reset(); sizePointer=NULL;
if(func_1502B6BC(NULL,2,NULL,2,items[0],items[1])!=entries || error || !expectedFallback) return 3;
reset();
if(func_1502B6BC(&sizeOutput,2,&sizeOutput,2,items[0],items[1])!=entries || error || sizeOutput!=2) return 4;
''')

    def test_block_pointer_and_post_load_size_are_independent_gates(self):
        self.run_host(r'''
int pointerNull,sizeZero;
for(pointerNull=0;pointerNull<2;pointerNull++) for(sizeZero=0;sizeZero<2;sizeZero++) {
    reset(); failBlock=pointerNull; blockSize=sizeZero?0:-123;
    if(func_1502B6BC(&sizeOutput,2,&relocatedOutput,2,items[0],items[1])!=(pointerNull?NULL:entries)
       || error || sizeOutput!=blockSize || relocatedOutput!=((!pointerNull && !sizeZero)?2:0)
       || relocations!=(!pointerNull && !sizeZero) || fences()) return 1;
    if((pointerNull || sizeZero) && (entries[0]!=16 || entries[1]!=0x10000004)) return 2;
}
''')

    def test_live_size_and_descriptor_reads_with_metadata_snapshot_at_block_call(self):
        self.run_host(r'''
reset(); mutateSize=mutateDescriptor=1;
if(func_1502B6BC(&sizeOutput,2,&relocatedOutput,2,items[0],items[1])!=entries || error
   || sizeOutput!=32 || relocatedOutput!=2 || seenDescriptor!=metadata[1] || fences()) return 1;
''')

    def test_relocator_fixed_counts_masks_sentinels_and_unsigned_addition(self):
        self.run_host(r'''
static u32 offsets[]={0,1,16,0x7FFFFFFF,0x80000000,0xFFFFFFFE,0xFFFFFFFF};
static u32 lengths[]={0,1,0x0FFFFFFF,0x10000000,0x80000000,0xFFFFFFFF};
int o,l,count,i;
for(o=0;o<7;o++) for(l=0;l<6;l++) for(count=1;count<=9;count++) {
    reset();
    for(i=0;i<128;i++) entries[i]=0xA5A5A5A5;
    for(i=0;i<count;i++) { entries[2*i]=offsets[o]; entries[2*i+1]=lengths[l]; }
    if(actual_relocation(entries,count)!=count) return 1;
    for(i=0;i<count;i++) {
        u32 length=lengths[l]&0x0FFFFFFF;
        u32 address=(offsets[o]==0xFFFFFFFF || !length)?0:offsets[o]+(u32)entries;
        if(entries[2*i]!=address || entries[2*i+1]!=length) return 2;
    }
    if(entries[count*2]!=0xA5A5A5A5 || fences()) return 3;
}
''')

    def test_relocator_auto_count_includes_terminal_entry_and_scans_before_writes(self):
        self.run_host(r'''
int last,i;
for(last=0;last<20;last++) {
    reset();
    for(i=0;i<128;i++) entries[i]=0xA5A5A5A5;
    for(i=0;i<=last;i++) { entries[2*i]=(u32)(i*8); entries[2*i+1]=0x10000001; }
    entries[2*last+1]|=0x80000000;
    if(actual_relocation(entries,0)!=last+1) return 1;
    for(i=0;i<=last;i++) if(entries[2*i]!=(u32)entries+(u32)(i*8) || entries[2*i+1]!=1) return 2;
    if(entries[2*(last+1)]!=0xA5A5A5A5 || fences()) return 3;
}
reset(); entries[0]=0xFFFFFFFF; entries[1]=0x80000000;
if(actual_relocation(entries,0)!=1 || entries[0] || entries[1]) return 4;
''')

    def test_relocator_negative_count_does_not_dereference_or_modify(self):
        self.run_host(r'''
static s32 counts[]={-1,-2,(s32)0x80000000}; int i;
for(i=0;i<3;i++) if(actual_relocation(NULL,counts[i])!=counts[i]) return 1;
reset(); expectedCount=-7;
if(func_1502B6BC(&sizeOutput,-7,&relocatedOutput,2,items[0],items[1])!=entries
   || error || relocatedOutput!=-7 || entries[0]!=16 || entries[1]!=0x10000004) return 2;
''')

    def test_retail_varargs_unspecified_zero_depth_and_no_guards(self):
        self.assertIn('va_arg(path, s32)', self.body)
        self.assertNotRegex(self.body, r'u32 descriptor\s*=')
        self.assertNotIn('depth <=', self.body)
        self.assertNotIn('depth >', self.body)
        self.assertNotIn('memset', self.body)
        self.assertIn('if (relocated != NULL)', self.body)
        self.assertEqual(struct.unpack_from('>I', self.rom, 0x58B6C)[0], 0x27BDFFB0)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] in ('func_1502B6BC','func_1502B4A8')
                                 for row in csv.DictReader(source)))
        self.assertIn('D_800C3D68[15] = saved;', self.source)
        self.assertIn('amount = func_10006240(compressed, result, D_8003809C);', self.source)

    def test_actual_resource_helper_consumes_relocated_header_and_output_counts(self):
        source=(self.root/'conker/src/game/generated_15F680.c').read_text()
        helper=re.search(r's32 func_151336A8\([^;{}]+\) \{\n.*?\n\}',source,re.S).group(0)
        layouts='\n'.join(re.search(r'typedef struct '+name+r' \{.*?\} '+name+';',source,re.S).group(0)
            for name in ('ExtendedResource15F680','ExtendedResourceNode15F680'))
        connection='typedef unsigned short u16;\n'+layouts+r'''
static ExtendedResourceNode15F680 node;
s32 D_800A3880[236], D_800DC640[234];
static int setupCalls, attachCalls, changeHeader;
static u8 replacement[4];
void func_1510CE60(void *data,s32 b,s32 c,s32 d,s32 *output) {
    push('S'); setupCalls++;
    if(data!=(u8 *)entries+16 || b || c!=1 || d!=0x3E || output!=D_800DC640+7
       || node.resource!=(void *)entries || blocks!=1 || relocations!=1) error=5;
    *output=333;
    if(changeHeader) node.resource->data=replacement;
}
void func_15168E54(void *data,void *resource) {
    push('T'); attachCalls++;
    if(resource!=entries || data!=(changeHeader?(void *)replacement:(void *)((u8 *)entries+16))
       || setupCalls!=1) error=6;
}
''' + helper+'\n'
        original=self.fixture
        try:
            self.fixture+=connection
            self.run_host(r'''
int fail,change;
for(fail=0;fail<2;fail++) for(change=0;change<2;change++) {
    reset(); sizePointer=NULL; expectedCount=0; items[0]=9; items[1]=D_800A3880[7]=0xC6;
    node.resource=(void *)1; setupCalls=attachCalls=0; changeHeader=change; failBlock=fail;
    if(func_151336A8(7,&node,NULL)!=(fail?0:1) || error || consumed!=2 || fences()) return 1;
    if(fail) {
        if(node.resource || setupCalls || attachCalls || !trace_is("QQB")) return 2;
    } else if(node.resource!=(void *)entries || setupCalls!=1 || attachCalls!=1
              || D_800DC640[7]!=333 || !trace_is("QQBRST")) return 3;
}
''')
        finally:
            self.fixture=original

    def test_actual_three_component_table_loader_and_two_component_lazy_loader(self):
        table_source=(self.root/'conker/src/game/generated_49D30.c').read_text()
        lazy_source=(self.root/'conker/src/game/generated_6A3D0.c').read_text()
        table=re.search(r's32 func_1501D1D4\([^;{}]+\) \{\n.*?\n\}',table_source,re.S).group(0)
        lazy=re.search(r's32 func_1503D774\([^;{}]+\) \{\n.*?\n\}',lazy_source,re.S).group(0)
        connection=r'''
typedef struct { u32 value; } struct124;
s32 D_800C3668[4];
struct124 *D_800D1C90[4];
''' +table+'\n'+lazy+'\n'
        original=self.fixture
        try:
            self.fixture+=connection
            self.run_host(r'''
reset(); sizePointer=NULL; expectedLookupCalls=3; expectedCount=0;
items[0]=6; items[1]=42; items[2]=-17; D_800C3668[1]=-99;
if(func_1501D1D4(42,-17,1)!=(s32)entries || error || consumed!=3
   || D_800C3668[1]!=(s32)entries || !trace_is("QQQBR")) return 1;
reset(); sizePointer=NULL; expectedLookupCalls=3; metadata[1]=0x80000000;
items[0]=6; items[1]=42; items[2]=-17; expectedLookupCalls=2;
if(func_1501D1D4(42,-17,1) || error || consumed!=3 || D_800C3668[1]) return 2;
reset(); sizePointer=NULL; items[0]=0x11; items[1]=2; expectedCount=2; D_800D1C90[2]=NULL;
if(func_1503D774(2,123) || error || consumed!=2 || D_800D1C90[2]!=(void *)((u8 *)entries+16)
   || !trace_is("QQBR")) return 3;
reset(); D_800D1C90[2]=(void *)1;
if(func_1503D774(2,123) || traceLength || D_800D1C90[2]!=(void *)1) return 4;
reset(); sizePointer=NULL; items[0]=0x11; items[1]=2; failBlock=1; D_800D1C90[2]=NULL;
if(func_1503D774(2,123)!=2 || error || D_800D1C90[2] || !trace_is("QQB")) return 5;
''')
        finally:
            self.fixture=original

    def test_actual_constructor_helper_loader_and_relocator_connected(self):
        class Connected(constructor.GameExtendedChildConstructorTests):
            pass
        Connected.setUpClass()
        self.addCleanup(Connected.doClassCleanups)
        fixture=Connected.fixture
        for pattern in (r'void \*func_1502B6BC\([^;{}]+\) \{\n.*?\n\}',
                        r'void func_1510CE60\([^;{}]+\) \{\n.*?\n\}',
                        r'void func_15168E54\([^;{}]+\) \{\n.*?\n\}'):
            fixture,count=re.subn(pattern,'',fixture,flags=re.S)
            self.assertEqual(count,1)
        fixture+=self.declarations+r'''
u8 D_AB1950[16];
static u32 resourceBlock[4];
static int lookupCalls, blockCalls, relocationCalls;
s32 func_1502AC88(u32 offset,s32 item,u32 *descriptor) {
    int i=lookupCalls++;
    push('Q');
    if(i>1 || item!=(i?0xC6:9) || offset!=(u32)D_AB1950+(u32)(i*8)) error=20;
    *descriptor=0x80000010;
    return 8;
}
void *func_1502B350(u32 offset,u32 descriptor,s32 *size) {
    push('D'); blockCalls++;
    if(offset!=(u32)D_AB1950+16 || descriptor!=0x80000010 || *size!=16 || lookupCalls!=2) error=21;
    *size=failLoad?0:16;
    return failLoad?NULL:resourceBlock;
}
void func_1510CE60(void *a,s32 b,s32 c,s32 d,s32 *e) {
    push('S'); setups++;
    if(a!=resourceBlock+2 || b || c!=1 || d!=0x3E || e!=&D_800DC640[7]
       || nodes[0].resource!=(void *)resourceBlock || copies || relocationCalls!=1) error=22;
    *e=1234;
}
void func_15168E54(void *a,void *b) {
    push('T'); attachments++;
    if(a!=resourceBlock+2 || b!=resourceBlock || setups!=1 || copies) error=23;
}
'''+'#define func_1502B4A8 connected_relocation\n'+self.relocator+'\n#undef func_1502B4A8\n'+r'''
s32 func_1502B4A8(u32 *data,s32 count) {
    push('R'); relocationCalls++;
    if(data!=resourceBlock || count!=0 || blockCalls!=1) error=24;
    return connected_relocation(data,count);
}
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
'''+self.body+'\n#pragma GCC diagnostic pop\n'
        original=self.fixture
        try:
            self.fixture=fixture
            self.run_host(r'''
int phase;
for(phase=0;phase<4;phase++) {
    reset(0x49E8,7); D_800A3880[7]=0xC6;
    lookupCalls=blockCalls=relocationCalls=0;
    resourceBlock[0]=8; resourceBlock[1]=0x80000004; resourceBlock[2]=0x13579BDF; resourceBlock[3]=0x2468;
    failRecord=phase==1; failNode=phase==2; failLoad=phase==3;
    if(func_15132A4C(descriptor,3,255,28,0xF3,-123)!=(phase?NULL:result) || error || fences()) return 1;
    if(!phase) {
        if(!trace_is("ANQQDRSTCVVVVB") || lookupCalls!=2 || blockCalls!=1 || relocationCalls!=1
           || nodes[0].resource!=(void *)resourceBlock || nodes[0].resource->data!=resourceBlock+2
           || D_800DC468[7]!=1 || D_800DC63C!=1 || D_800DC640[7]!=1234
           || check_result(0,&nodes[0],4) || resourceBlock[1]!=4) return 2;
    } else if(D_800DC63C || D_800DC468[7] || copies
              || !trace_is(phase==1?"A":phase==2?"ANRF":"ANQQDRFF")) return 3;
}
''')
        finally:
            self.fixture=original

    def test_fresh_ido_slots_and_preserved_exact_callers(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(n) is None for n in
                ('mips-linux-gnu-ld','mips-linux-gnu-objdump')):
            self.skipTest('IDO/MIPS tools are unavailable')
        source,obj,elf,script=(self.path/('loader'+suffix) for suffix in ('.c','.o','.elf','.ld'))
        source.write_text('#include "stdarg.h"\n'+self.types+self.declarations+self.relocator+'\n'+self.body+'\n')
        result=subprocess.run([str(compiler),'-c','-32','-G','0','-Xfullwarn','-Xcpluscomm','-signed',
            '-nostdinc','-non_shared','-Wab,-r4300_mul','-I',str(self.root/'conker/include/libc'),
            '-mips2','-o32','-O2','-g3','-o',str(obj),str(source)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(result.stdout+result.stderr,'')
        script.write_text('SECTIONS { .text 0x1502B4A8 : SUBALIGN(4) { *(.text) } }\n')
        targets={'D_AB1950':0xAB1950,'func_1502AC88':0x1502AC88,'func_1502B350':0x1502B350}
        subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e','func_1502B6BC',
            *(f'--defsym={name}=0x{value:X}' for name,value in targets.items()),'-o',str(elf),str(obj)],
            check=True,capture_output=True)
        fresh,_,_=match_progress.load_elf_functions(str(elf),'mips-linux-gnu-objdump')
        production,_,addresses=match_progress.load_elf_functions(
            str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        measured={'func_1502B6BC':(77,77,0x50,17,'88bc84ea5f8007358199c4f13b52e35d517419fd40230f9a25223139fe8bd1f5'),
                  'func_1502B4A8':(65,72,0,71,'bcce58836363dffad7c081528b0be692fbdfc461a5cc8b71e9b3376e16b43262')}
        for name,(body,size,frame,diffs,digest) in measured.items():
            words=fresh[name]
            count=max(i for i,w in enumerate(words) if w==0x03E00008)+2
            self.assertEqual(count,body)
            self.assertEqual(words[count:],[0]*(len(words)-count))
            slot=list(words[:count])+[0]*(size-count)
            self.assertEqual(production[name],slot)
            self.assertEqual(addresses[name],int(name[5:],16))
            self.assertEqual(0x10000-(slot[0]&0xFFFF) if slot[0]>>16==0x27BD else 0,frame)
            first=0x2D4B0+addresses[name]-0x15000000
            retail=struct.unpack_from('>'+str(size)+'I',self.rom,first)
            self.assertEqual(sum(a!=b for a,b in zip(slot,retail)),diffs)
            self.assertEqual(hashlib.sha256(struct.pack('>'+str(size)+'I',*slot)).hexdigest(),digest)
        for name,size in (('func_1501D1D4',33),('func_1503D774',36),('func_15002FB4',86)):
            first=0x2D4B0+addresses[name]-0x15000000
            self.assertEqual(struct.pack('>'+str(size)+'I',*production[name]),self.rom[first:first+size*4])
        print('variadic loader:',{name:value[:4] for name,value in measured.items()})


if __name__=='__main__':
    unittest.main()
