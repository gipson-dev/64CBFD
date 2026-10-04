"""Recovered callback/wrapper/spherical C; the constructor is an opaque fixture."""

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


class GameExtendedChildEmissionTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_113D60.c').read_text()
        helper = (cls.root / 'conker/src/game_16EE20.c').read_text()
        wrapper = (cls.root / 'conker/src/game/generated_15F680.c').read_text()
        header = (cls.root / 'conker/include/structs.h').read_text()
        cls.body = re.search(r'void func_150E93DC\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.parent = re.search(r'void func_150E9178\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.spherical = re.search(r'void func_151436B4\([^;{}]+\) \{\n.*?\n\}', helper, re.S).group(0)
        cls.wrapper = re.search(r'void \*func_15132A4C\([^;{}]+\) \{\n.*?\n\}', wrapper, re.S).group(0)
        vertex = re.search(r'typedef struct \{\s*f32 x;\s*f32 y;\s*f32 z;\s*\} vertex;', header).group(0)
        cls.types = ('typedef unsigned char u8; typedef signed char s8; typedef short s16; '
                     'typedef unsigned short u16; typedef int s32; typedef unsigned int u32; '
                     'typedef float f32;\n#define NULL ((void *)0)\n') + vertex + '\n'
        cls.layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';',
                                         source, re.S).group(0) for name in
            ('EventPayload113D60', 'WorldPosition113D60', 'EventPositionPayload113D60',
             'ExtendedEventPositionPayload113D60', 'EventWeightNode113D60',
             'ExtendedChildEmissionDescriptor113D60'))
        cls.constants = [f'D_800A{address:04X}' for address in range(0x13C8, 0x13E8, 4)]
        cls.declarations = 'extern f32 ' + ','.join(cls.constants) + ';\n' + r'''
extern f32 D_800BE9A4, D_800A12F4[];
extern u8 D_800A12F0[];
s32 func_150ADA20(void);
f32 func_150ADA68(void);
f32 cosf(f32);
f32 sinf(f32);
void func_151436B4(f32, f32, f32, vertex *);
void *func_15132A4C(void *, s32, s32, s32, u8, s32);
void *func_1513264C(void *, s32, s32, void *, s32, u8, s32);
void *memcpy(void *, const void *, u32);
'''
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        first, address, _, _ = load_game_data_layout(cls.root / 'conker')
        cls.literals = struct.unpack_from('>8I', cls.rom, first + 0x800A13C8 - address)
        cls.resource = cls.rom[first + 0x800A12F0 - address]
        cls.table_word = struct.unpack_from('>I', cls.rom, first + 0x800A12F4 - address)[0]
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = cls.types + cls.layouts + cls.declarations + (
            'static const u32 literalWords[8]={' + ','.join('0x%08Xu' % w for w in cls.literals) + '};\n'
            'f32 ' + ','.join(cls.constants) + ';\n'
            + ('static const u32 tableWord=0x%08Xu;\n' % cls.table_word)
            + ('static const u8 retailResource=%d;\n' % cls.resource)) + r'''
f32 D_800BE9A4, D_800A12F4[4];
u8 D_800A12F0[4];
static union { u32 alignment; u8 bytes[0x90]; } record;
static union { u32 alignment; u8 bytes[0x1B0]; } results[8];
static ExtendedChildEmissionDescriptor113D60 snapshots[8], *lastDescriptor;
static f32 samples[96], expectedPosition[3], expectedSize, expected4C, expected40, expected48;
static f32 expectedSpread, expectedScale, expectedPeriod, expected34;
static u32 expectedFlags, expected00;
static u8 expectedSlot, expectedContext, expectedResource, expected60;
static int floatCalls, integerCalls, mathCalls, submissions, copies, error, failures;
static int mutateInitial, mutateLive, mutatePosition, mutateMetadata, mutateDescriptor;
static int mutateSubmitProgress, mutateCopyProgress, inParent, parentFloats, parentIntegers;
static int parentCopies, parentAllocations, parentPoints;
static char trace[256];
static int traceLength;
static u32 bits(f32 x) { union { f32 f; u32 u; } v; v.f=x; return v.u; }
static f32 number(u32 x) { union { f32 f; u32 u; } v; v.u=x; return v.f; }
static EventPositionPayload113D60 *state(void) { return (EventPositionPayload113D60 *)(record.bytes+0x28); }
static void push(char c) { if(traceLength<255) trace[traceLength++]=c; else error=1; }
static int trace_is(const char *s) {
    int i=0;
    while(s[i]) { if(i>=traceLength || trace[i]!=s[i]) return 0; i++; }
    return i==traceLength;
}
f32 func_150ADA68(void) {
    int i, phase;
    if(inParent) { parentFloats++; return 0; }
    i=floatCalls++; push('F');
    if(i>=96) { error=2; return 0; }
    if(!i) {
        if(mutateInitial) {
            state()->parameters.field00=0.5f; state()->parameters.field04=0.5f;
            state()->parameters.field08=0.875f; D_800BE9A4=0.5f;
            D_800A13C8=3; D_800A13CC=4;
        }
        expectedSpread=D_800A13C8; expectedScale=D_800A13CC;
        return samples[i];
    }
    phase=(i-1)%10+1;
    if(mutateLive) { D_800A13C8=99; D_800A13CC=100; }
    if(phase==1) {
        if(mutateLive) { D_800A13D0=2; D_800A12F4[0]=0.25f; }
        expectedSize=((samples[i]*D_800A13D0+400.0f)*D_800A12F4[0])*expectedScale;
    }
    if(phase==5) {
        if(mutateLive) { D_800A13D4=5; D_800A13D8=6; }
        expected4C=(samples[i]*D_800A13D4+D_800A13D8)*expectedScale;
    }
    if(phase==6) {
        if(mutateLive) D_800A13DC=7;
        expected40=(samples[i]*expectedSpread+D_800A13DC)*expectedScale;
    }
    if(phase==7) {
        if(mutateLive) D_800A13E0=8;
        expected48=(samples[i]*expectedSpread+D_800A13E0)*expectedScale;
    }
    if(phase==10) {
        if(mutateLive) D_800A13E4=2.0f+(f32)((i-1)/10);
        expectedPeriod=D_800A13E4;
    }
    return samples[i];
}
s32 func_150ADA20(void) {
    int i;
    if(inParent) { parentIntegers++; return -1; }
    i=integerCalls++; push('I');
    if(mutateLive && !(i&1)) D_800A12F0[0]=(u8)(0xD0+i);
    if(!(i&1)) expectedResource=D_800A12F0[0];
    return i&1 ? (s32)0x80000000u : -1;
}
static f32 math(f32 angle, int sine) {
    int i=mathCalls++, phase=i%4, k=i/4;
    static f32 values[4]={0.5f,0.25f,1,-0.5f};
    f32 radius=samples[10*k+10]*50.0f;
    push(sine?'S':'C');
    if(sine!=(phase&1) || floatCalls!=1+10*(k+1)
       || bits(angle)!=bits(samples[10*k+(phase<2?8:9)]*expectedPeriod)) error=3;
    if(phase==3) {
        if(mutatePosition) { state()->position.x=1000; state()->position.y=2000; state()->position.z=3000; }
        if(mutateMetadata) { record.bytes[0xC]=expectedSlot=0xC7; record.bytes[1]=expectedContext=0x81; }
        expectedPosition[0]=(radius*values[2])*values[1]+state()->position.x;
        expectedPosition[1]=-radius*values[3]+state()->position.y;
        expectedPosition[2]=(radius*values[2])*values[0]+state()->position.z;
    }
    return values[phase];
}
f32 cosf(f32 angle) { return math(angle,0); }
f32 sinf(f32 angle) { return math(angle,1); }
void *func_1513264C(void *input, s32 resource, s32 value, void *optional,
                    s32 payloadBytes, u8 slot, s32 context) {
    ExtendedChildEmissionDescriptor113D60 *d=input;
    int i=submissions++, j;
    push('A');
    if(i>=8) { error=4; state()->parameters.field08=1; return NULL; }
    if(resource!=3 || value!=255 || optional || payloadBytes!=28
       || slot!=expectedSlot || context!=expectedContext
       || floatCalls!=1+10*(i+1) || integerCalls!=2*(i+1) || mathCalls!=4*(i+1)
       || bits(d->field00)!=expected00 || d->field04!=1 || d->field1C!=1 || d->field20!=1 || d->field24!=1
       || bits(d->field08)!=bits(expectedSize) || bits(d->field0C)!=bits(expectedSize)
       || bits(d->field10)!=bits(samples[10*i+2]*360.0f)
       || bits(d->field14)!=bits(samples[10*i+3]*360.0f)
       || bits(d->field18)!=bits(samples[10*i+4]*360.0f)
       || bits(d->field4C)!=bits(expected4C) || bits(d->field40)!=bits(expected40)
       || bits(d->field48)!=bits(expected48) || bits(d->field44)
       || bits(d->field34)!=bits(expected34) || bits(d->field38) || bits(d->field3C)
       || bits(d->position.x)!=bits(expectedPosition[0]) || bits(d->position.y)!=bits(expectedPosition[1])
       || bits(d->position.z)!=bits(expectedPosition[2]) || d->flags!=expectedFlags
       || d->field54!=100 || d->resource!=expectedResource || d->field58 || d->field5C
       || d->field60!=expected60 || d->field61!=8 || d->field62 || d->field63 || d->field64 || d->field65
       || d->field66 || d->field67 || d->field68!=2 || d->field6A!=2 || d->field6C || d->field70
       || d->field72!=1 || d->field74!=255) error=5;
    snapshots[i]=*d; lastDescriptor=d;
    if(!(failures&(1<<i))) for(j=0;j<124;j++) results[i].bytes[0x10+j]=((u8 *)d)[j];
    if(mutateSubmitProgress && !i) state()->parameters.field08=2.25f;
    if(mutateDescriptor && !i) {
        d->field00=9; expected00=bits(9); d->field34=expected34=11;
        d->flags=expectedFlags=0x12345678; d->field60=expected60=42;
        d->field54=-1; d->resource=0; d->field61=99; d->field08=-1;
    }
    return failures&(1<<i)?NULL:results[i].bytes;
}
void *memcpy(void *destination, const void *source, u32 length) {
    u32 i;
    if(inParent) {
        parentCopies++;
        if(destination!=record.bytes+0x28 || length!=60) error=6;
    } else {
        int k=submissions-1;
        push('M'); copies++;
        if(k<0 || k>=8 || destination!=results[k].bytes+0x170 || length!=28 || failures&(1<<k)) error=7;
        if(lastDescriptor && (u32)source >= (u32)lastDescriptor
           && (u32)source < (u32)lastDescriptor+124) error=8;
        if(mutateCopyProgress && copies==1) state()->parameters.field08=3.125f;
    }
    /* Forward opaque bytes; never assert a value for retail's uninitialized payload. */
    for(i=0;i<length;i++) ((u8 *)destination)[i]=((const u8 *)source)[i];
    return destination;
}
static void initialize(void) {
    int i,j;
    f32 *globals[8]={&D_800A13C8,&D_800A13CC,&D_800A13D0,&D_800A13D4,
                    &D_800A13D8,&D_800A13DC,&D_800A13E0,&D_800A13E4};
    for(i=0;i<8;i++) *globals[i]=number(literalWords[i]);
    D_800A12F0[0]=expectedResource=retailResource;
    for(i=1;i<4;i++) D_800A12F0[i]=(u8)(100+i);
    D_800A12F4[0]=number(tableWord); D_800A12F4[1]=99; D_800A12F4[2]=98; D_800A12F4[3]=97;
    for(i=0;i<0x90;i++) record.bytes[i]=0xA5;
    for(i=0;i<8;i++) for(j=0;j<0x1B0;j++) results[i].bytes[j]=0xA5;
    for(i=0;i<96;i++) samples[i]=0;
    for(i=0;i<8;i++) for(j=1;j<=10;j++) samples[10*i+j]=(f32)j/16.0f;
    record.bytes[0xC]=expectedSlot=0xC3; record.bytes[1]=expectedContext=0x91;
    state()->position.x=-100; state()->position.y=200; state()->position.z=-300;
    state()->parameters.field00=state()->parameters.field04=0; state()->parameters.field08=1.125f;
    D_800BE9A4=1; expectedSpread=D_800A13C8; expectedScale=D_800A13CC;
    expectedPeriod=D_800A13E4; expected00=0; expected34=0; expectedFlags=0x49E8; expected60=255;
    floatCalls=integerCalls=mathCalls=submissions=copies=error=failures=traceLength=0;
    mutateInitial=mutateLive=mutatePosition=mutateMetadata=mutateDescriptor=0;
    mutateSubmitProgress=mutateCopyProgress=inParent=0;
    parentFloats=parentIntegers=parentCopies=parentAllocations=parentPoints=0;
    lastDescriptor=NULL;
}
static int fences(void) {
    int i,k;
    for(i=0;i<0x90;i++) if(i!=1 && i!=0xC && (i<0x28 || i>=0x64) && record.bytes[i]!=0xA5) return 1;
    for(k=0;k<8;k++) for(i=0;i<0x1B0;i++) {
        if(k<submissions && !(failures&(1<<k)) && i>=0x10 && i<0x8C) continue;
        if(k<submissions && !(failures&(1<<k)) && i>=0x170 && i<0x18C) continue;
        if(results[k].bytes[i]!=0xA5) return 2;
    }
    return 0;
}
''' + cls.spherical + '\n' + cls.wrapper + '\n' + (
            '#pragma GCC diagnostic push\n'
            '#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"\n'
            + cls.body + '\n#pragma GCC diagnostic pop\n')

    def test_layout_and_complete_emission(self):
        self.run_host(r'''
ExtendedChildEmissionDescriptor113D60 d;
if(sizeof(d)!=124 || (u8 *)&d.position-(u8 *)&d!=0x28 || (u8 *)&d.flags-(u8 *)&d!=0x50
   || (u8 *)&d.resource-(u8 *)&d!=0x56 || (u8 *)&d.field60-(u8 *)&d!=0x60
   || (u8 *)&d.field72-(u8 *)&d!=0x72 || (u8 *)&d.reserved76-(u8 *)&d!=0x76) return 1;
initialize(); func_150E93DC(record.bytes);
if(error || submissions!=1 || copies!=1 || floatCalls!=11 || integerCalls!=2 || mathCalls!=4
   || state()->parameters.field08!=0.125f || !trace_is("FIFFFFFIFFFFFCSCSAM") || fences()) return 2;
''')

    def test_strict_progress_and_failures_consume_all_rng_calls(self):
        self.run_host(r'''
static f32 values[]={-1,0,0.5f,1,1.125f,2,2.125f,3,3.125f,5};
static int counts[]={0,0,0,0,1,1,2,2,3,4};
int i,failed,k,success;
for(i=0;i<10;i++) for(failed=0;failed<16;failed++) {
    initialize(); state()->parameters.field08=values[i]; failures=failed; success=0;
    for(k=0;k<counts[i];k++) success+=!(failed&(1<<k));
    func_150E93DC(record.bytes);
    if(error || submissions!=counts[i] || copies!=success || floatCalls!=1+10*counts[i]
       || integerCalls!=2*counts[i] || mathCalls!=4*counts[i]
       || state()->parameters.field08!=values[i]-(f32)counts[i] || fences()) return 1;
}
''')

    def test_initial_rng_reads_rates_and_snapshot_globals_after_callback(self):
        self.run_host(r'''
initialize(); mutateInitial=1; samples[0]=0.5f;
func_150E93DC(record.bytes);
if(error || submissions!=1 || copies!=1 || state()->parameters.field08!=0.25f
   || expectedSpread!=3 || expectedScale!=4 || fences()) return 1;
''')

    def test_live_fields_period_and_resource_but_captured_spread_scale(self):
        self.run_host(r'''
initialize(); state()->parameters.field08=3.125f; mutateLive=1;
func_150E93DC(record.bytes);
if(error || submissions!=3 || copies!=3 || D_800A13C8!=99 || D_800A13CC!=100
   || bits(expectedSpread)!=literalWords[0] || bits(expectedScale)!=literalWords[1]
   || snapshots[0].resource!=0xD0 || snapshots[2].resource!=0xD4 || expectedPeriod!=4 || fences()) return 1;
''')

    def test_first_table_entry_reused_without_advancing_index(self):
        self.run_host(r'''
initialize(); state()->parameters.field08=4.125f;
func_150E93DC(record.bytes);
if(error || submissions!=4 || snapshots[0].field08!=snapshots[3].field08 || fences()) return 1;
''')

    def test_position_and_metadata_read_after_actual_spherical_helper(self):
        self.run_host(r'''
initialize(); mutatePosition=mutateMetadata=1;
func_150E93DC(record.bytes);
if(error || submissions!=1 || snapshots[0].position.x!=1007.8125f
   || snapshots[0].position.y!=2015.625f || snapshots[0].position.z!=3015.625f
   || record.bytes[0xC]!=0xC7 || record.bytes[1]!=0x81 || fences()) return 1;
''')

    def test_constant_descriptor_fields_persist_and_dynamic_fields_reset(self):
        self.run_host(r'''
initialize(); state()->parameters.field08=3.125f; mutateDescriptor=1;
func_150E93DC(record.bytes);
if(error || submissions!=3 || snapshots[0].flags!=0x49E8 || snapshots[1].flags!=0x12345678
   || snapshots[2].field00!=9 || snapshots[2].field34!=11 || snapshots[2].field60!=42
   || snapshots[1].field54!=100 || snapshots[2].field61!=8 || fences()) return 1;
''')

    def test_progress_reloaded_after_constructor_and_copy_even_on_failure(self):
        self.run_host(r'''
int failed;
for(failed=0;failed<2;failed++) {
    initialize(); mutateSubmitProgress=1; failures=failed;
    func_150E93DC(record.bytes);
    if(error || submissions!=2 || copies!=2-failed || state()->parameters.field08!=0.25f || fences()) return 1;
}
initialize(); mutateCopyProgress=1;
func_150E93DC(record.bytes);
if(error || submissions!=3 || copies!=3 || state()->parameters.field08!=0.125f || fences()) return 2;
''')

    def test_unclamped_signed_samples_and_unsigned_resource_byte(self):
        self.run_host(r'''
static f32 values[]={-2,-1,0,0.25f,1,2};
int i,j;
for(i=0;i<6;i++) for(j=0;j<6;j++) {
    initialize(); samples[1]=values[i]; samples[10]=values[j];
    D_800A12F0[0]=0xFF; func_150E93DC(record.bytes);
    if(error || snapshots[0].resource!=255 || submissions!=1 || copies!=1 || fences()) return 1;
}
''')

    def test_nonfinite_initial_rates_stop_at_strict_gate(self):
        self.run_host(r'''
static u32 words[]={0x7FC01234,0xFFC01234,0xFF800000};
int i;
for(i=0;i<3;i++) {
    initialize(); state()->parameters.field00=number(words[i]);
    func_150E93DC(record.bytes);
    if(error || floatCalls!=1 || integerCalls || mathCalls || submissions || copies || fences()) return 1;
}
''')

    def test_actual_extended_parent_payload_is_consumed_by_child(self):
        connection = r'''
f32 D_800A13B8=2, D_800A13BC=0.25f, D_800A13C0=0.5f, D_800A13C4=1000000;
f32 D_800DCD90=1;
s32 D_800BE9E8;
static int object;
static union { u32 alignment; u8 bytes[0x50]; } parentRecord;
static EventWeightNode113D60 node={&object,0,1,NULL};
u8 *D_800DCDC4=(u8 *)&node;
f32 *func_15144B34(s32 player) { static f32 origin[3]={-100,200,-300}; return origin; }
void func_1514470C(void *descriptor, void *position) {
    WorldPosition113D60 *p=position; parentPoints++;
    if(descriptor!=&object) error=9;
    p->x=-100; p->y=200; p->z=-300;
}
void *func_15149130(s16 duration, s8 a, s8 code, s8 c, u8 d, u8 e, s32 bytes, u8 slot, s32 context) {
    parentAllocations++;
    if(duration!=13 || a!=-1 || code!=0x37 || c!=-1 || d!=1 || e || bytes!=60
       || slot!=0xC3 || context!=0x91) error=10;
    return record.bytes;
}
''' + self.parent + '\n'
        original = self.fixture
        try:
            self.fixture += connection
            self.run_host(r'''
EventPayload113D60 *parentState=(EventPayload113D60 *)(parentRecord.bytes+0x28);
initialize(); parentRecord.bytes[0xC]=0xC3; parentRecord.bytes[1]=0x91;
parentState->field00=parentState->field04=0; parentState->field08=1.125f;
inParent=1; func_150E9178(parentRecord.bytes); inParent=0;
if(error || parentFloats!=2 || parentIntegers!=1 || parentPoints!=1 || parentAllocations!=1
   || parentCopies!=1 || state()->position.x!=-100 || state()->parameters.field00!=0.5f
   || state()->parameters.field04!=0.25f || state()->parameters.field08!=0) return 1;
D_800BE9A4=3; samples[0]=0.5f; func_150E93DC(record.bytes);
if(error || submissions!=1 || copies!=1 || state()->parameters.field08!=0.875f || fences()) return 2;
''')
        finally:
            self.fixture = original

    def test_retail_contract_unspecified_bytes_and_no_word_guards(self):
        words = struct.unpack('>208I', self.rom[0x11688C:0x116BCC])
        self.assertEqual(words[0], 0x27BDFED8)
        self.assertEqual(words[-2:], (0x03E00008, 0x27BD0128))
        first, address, _, _ = load_game_data_layout(self.root / 'conker')
        self.assertEqual(struct.unpack_from('>I', self.rom, first + 0x8008A4E8 + 0x37*4 - address)[0],
                         0x150E93DC)
        self.assertNotIn('memset', self.body)
        self.assertNotIn('reserved', self.body)
        self.assertNotRegex(self.body, r'extra\s*\[[^]]+\]\s*=')
        self.assertNotRegex(self.body, r'extra\s*\[[^]]+\]\s*=[^;]+;')
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] in ('func_150E93DC', 'func_15132A4C')
                                 for row in csv.DictReader(source)))
        constructor = (self.root / 'conker/src/game/generated_15F680.c').read_text()
        self.assertRegex(constructor, r'void \*func_1513264C\(u8 \*descriptor,')
        self.assertIn('result = func_15167A68(', constructor)

    def test_fresh_ido_fitting_production_identity_and_exact_helpers(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(n) is None for n in
                ('mips-linux-gnu-ld', 'mips-linux-gnu-objcopy', 'mips-linux-gnu-objdump')):
            self.skipTest('IDO/MIPS tools are unavailable')
        source, obj, elf, binary, script = (self.path / ('child' + suffix)
                                           for suffix in ('.c', '.o', '.elf', '.bin', '.ld'))
        source.write_text(self.types + self.layouts + self.declarations + self.body + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
            '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3',
            '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        script.write_text('SECTIONS { .text 0x150E93DC : SUBALIGN(4) { *(.text) } }\n')
        targets = {name: int(name[2:], 16) for name in (*self.constants, 'D_800A12F0', 'D_800A12F4', 'D_800BE9A4')}
        targets.update({name: int(name[5:], 16) for name in
                        ('func_150ADA68', 'func_150ADA20', 'func_151436B4', 'func_15132A4C')})
        targets['memcpy'] = 0x10022EC0
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_150E93DC',
            *(f'--defsym={name}=0x{value:X}' for name, value in targets.items()),
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', '.text', str(elf), str(binary)],
                       check=True, capture_output=True)
        data = binary.read_bytes()
        words = struct.unpack('>' + 'I' * (len(data) // 4), data)
        count = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        self.assertEqual(count, 206)
        self.assertEqual(0x10000 - (words[0] & 0xFFFF), 0x138)
        self.assertEqual(data[count*4:], bytes(len(data)-count*4))
        slot = words[:count] + (0,) * (208-count)
        retail = struct.unpack('>208I', self.rom[0x11688C:0x116BCC])
        self.assertEqual(sum(a != b for a, b in zip(slot, retail)), 200)
        self.assertEqual(hashlib.sha256(struct.pack('>208I', *slot)).hexdigest(),
                         'e8fa58f879c32cea6d5b1df01d0b0c91d0f274c66e39e380121db942aec4a0cc')
        production = self.root / 'conker/build/conker.us.elf'
        self.assertTrue(production.is_file(), 'production relink is required')
        linked, _, addresses = match_progress.load_elf_functions(str(production), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_150E93DC'], 0x150E93DC)
        self.assertEqual(tuple(linked['func_150E93DC']), slot)
        for name, size in (('func_15132A4C', 15), ('func_151436B4', 34), ('func_15144B34', 13),
                           ('func_151423D8', 27), ('func_150E90DC', 39), ('func_150E8A80', 39)):
            with self.subTest(function=name):
                first = 0x2D4B0 + addresses[name] - 0x15000000
                self.assertEqual(len(linked[name]), size)
                self.assertEqual(struct.pack('>' + 'I' * size, *linked[name]), self.rom[first:first+size*4])
        print('extended child slot:', {'body_words': 206, 'slot_words': 208, 'frame_bytes': 0x138,
              'different_words': 200, 'constructor_fixture': 'opaque; actual constructor tested separately'})


if __name__ == '__main__':
    unittest.main()
