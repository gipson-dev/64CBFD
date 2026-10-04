"""Actual recovered child/wrapper/spherical C; SDK math and allocation are fixtures."""

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


class GameChildEmissionCallbackTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_113D60.c').read_text()
        helper = (cls.root / 'conker/src/game_16EE20.c').read_text()
        wrapper = (cls.root / 'conker/src/game/generated_15D730.c').read_text()
        header = (cls.root / 'conker/include/structs.h').read_text()
        cls.body = re.search(r'void func_150E8D5C\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.weighted = re.search(r'void func_150E8B1C\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.spherical = re.search(r'void func_151436B4\([^;{}]+\) \{\n.*?\n\}', helper, re.S).group(0)
        cls.wrapper = re.search(r'void \*func_15130374\([^;{}]+\) \{\n.*?\n\}', wrapper, re.S).group(0)
        cls.vertex = re.search(r'typedef struct \{\s*f32 x;\s*f32 y;\s*f32 z;\s*\} vertex;', header).group(0)
        cls.types = ('typedef unsigned char u8; typedef signed char s8; typedef short s16; '
                     'typedef int s32; typedef unsigned int u32; typedef float f32;\n'
                     '#define NULL ((void *)0)\n') + cls.vertex + '\n'
        cls.layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';',
                                         source, re.S).group(0) for name in
            ('EventPayload113D60', 'WorldPosition113D60', 'EventPositionPayload113D60',
             'EventWeightNode113D60', 'ChildEmissionDescriptor113D60'))
        cls.constants = [f'D_800A{address:04X}' for address in range(0x1390, 0x13B0, 4)]
        cls.declarations = ('extern f32 ' + ','.join(cls.constants) + ';\n' + '''
extern f32 D_800BE9A4;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
f32 cosf(f32);
f32 sinf(f32);
void func_151436B4(f32, f32, f32, vertex *);
void *func_15130374(void *, u8, s32, u8, s32);
void *func_15130280(void *, u8, void *, s32, u8, s32);
void *memcpy(void *, const void *, u32);
''')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        first, address, _, _ = load_game_data_layout(cls.root / 'conker')
        cls.literal_words = struct.unpack_from('>8I', cls.rom, first + 0x800A1390 - address)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = cls.types + cls.layouts + cls.declarations + (
            'static const u32 literalWords[8]={' + ','.join('0x%08Xu' % w for w in cls.literal_words) + '};\n'
            'f32 ' + ','.join(cls.constants) + ';\n') + r'''
f32 D_800BE9A4;
static union { u32 alignment; u8 bytes[80]; } record;
static union { u32 alignment; u8 bytes[0xC0]; } results[8];
static ChildEmissionDescriptor113D60 snapshots[8], *lastDescriptor;
static f32 samples[64], mathArguments[32], expectedPosition[3];
static u32 integers[32], expectedFlags, expectedField00, expectedBonus;
static f32 expectedPeriod, expectedScale, expected24, expected4C;
static u8 expectedField17, expectedSlot, expectedContext;
static int floatCalls, integerCalls, mathCalls, submissions, copies, error, failures;
static int mutateInitial, mutateConstants, mutatePosition, mutateMetadata;
static int mutateSubmitProgress, mutateCopyProgress, mutateDescriptor, mutateFlags;
static int flagsOverride, inWeighted, weightedFloats, weightedIntegers, weightedPoints, weightedAllocations;
static char trace[256];
static int traceLength;
static u32 bits(f32 value) { union { f32 f; u32 u; } v; v.f=value; return v.u; }
static f32 number(u32 value) { union { f32 f; u32 u; } v; v.u=value; return v.f; }
static EventPositionPayload113D60 *state(void) { return (EventPositionPayload113D60 *)(record.bytes+0x28); }
static void push(char c) { if(traceLength<255) trace[traceLength++]=c; else error=1; }
static int trace_is(const char *s) {
    int i=0;
    while(s[i]) { if(i>=traceLength || trace[i]!=s[i]) return 0; i++; }
    return i==traceLength;
}
f32 func_150ADA68(void) {
    int i, phase;
    if(inWeighted) { weightedFloats++; return 0; }
    i=floatCalls++; push('F');
    if(i>=64) { error=2; return 0; }
    if(!i) {
        if(mutateInitial) {
            state()->parameters.field00=0.5f; state()->parameters.field04=0.5f;
            state()->parameters.field08=0.875f; D_800BE9A4=0.5f;
            D_800A1390=3; D_800A1394=4;
            expectedBonus=bits(3); expectedPeriod=4;
        }
        return samples[i];
    }
    phase=(i-1)%6+1;
    if(mutateConstants) { D_800A1390=99; D_800A1394=100; }
    if(phase==1) expectedScale=samples[i]*59.0f+80.0f;
    if(phase==2) {
        flagsOverride=0;
        if(mutateConstants) { D_800A1398=2; D_800A139C=3; D_800A13A0=4; }
        expected24=(samples[i]*D_800A1398+D_800A139C)*D_800A13A0;
    }
    if(phase==6) {
        if(mutateConstants) { D_800A13A4=5; D_800A13A8=6; D_800A13AC=7; }
        if(mutateMetadata) {
            record.bytes[0xC]=expectedSlot=0xC7; record.bytes[1]=expectedContext=0x81;
        }
        if(mutatePosition) { state()->position.x=9000; state()->position.y=8000; state()->position.z=7000; }
        expected4C=(samples[i]*D_800A13A4+D_800A13A8)*D_800A13AC;
    }
    return samples[i];
}
s32 func_150ADA20(void) {
    int i;
    if(inWeighted) { weightedIntegers++; return -1; }
    i=integerCalls++; push('I');
    if(i>=32) { error=3; return 0; }
    if(mutateFlags && lastDescriptor && i%4==2) {
        if(lastDescriptor->flags & 0xC0) error=4;
        lastDescriptor->flags=expectedFlags=0x12340080; flagsOverride=1;
    }
    if(mutateFlags && lastDescriptor && i%4==3) {
        lastDescriptor->flags|=4; expectedFlags|=4;
    }
    return (s32)integers[i];
}
static f32 math(f32 angle, int sine) {
    int i=mathCalls++, phase=i%4, k=i/4;
    f32 radius=samples[6*k+5]*20.0f;
    static f32 values[4]={0.5f,0.25f,1,-0.5f};
    push(sine?'S':'C');
    if(i>=32 || sine!=(phase&1) || floatCalls!=6*k+6
       || bits(angle)!=bits(samples[6*k+(phase<2?3:4)]*expectedPeriod)) error=5;
    if(i<32) mathArguments[i]=angle;
    if(phase==3) {
        if(mutatePosition) { state()->position.x=1000; state()->position.y=2000; state()->position.z=3000; }
        expectedPosition[0]=(radius*values[2])*values[1]+state()->position.x;
        expectedPosition[1]=-radius*values[3]+state()->position.y;
        expectedPosition[2]=(radius*values[2])*values[0]+state()->position.z;
    }
    return values[phase];
}
f32 cosf(f32 angle) { return math(angle,0); }
f32 sinf(f32 angle) { return math(angle,1); }
void *func_15130280(void *input, u8 mode, void *optional, s32 payloadBytes, u8 slot, s32 context) {
    ChildEmissionDescriptor113D60 *d=input;
    int i=submissions++, j;
    u32 flagBits;
    push('A');
    if(i>=8) { error=6; state()->parameters.field08=1; return NULL; }
    flagBits=(integers[4*i+2]&1?0x80:0)|(integers[4*i+3]&1?0x40:0);
    if(!flagsOverride) expectedFlags&=~0xC0;
    expectedFlags|=flagBits;
    if(mode || optional || payloadBytes!=4 || slot!=expectedSlot || context!=expectedContext
       || floatCalls!=1+6*(i+1) || integerCalls!=4*(i+1) || mathCalls!=4*(i+1)
       || d->field00!=expectedField00 || d->field04 || d->field08!=0xE01
       || d->field0A!=(s16)((integers[4*i]&15)+40) || d->field22!=d->field0A
       || d->field0C || d->field10 || d->field14!=15 || d->field15!=17 || d->field16!=5
       || d->field17!=expectedField17 || d->field18!=0x44 || d->field19!=0x3C || d->field1A!=0x27
       || d->field1B!=integers[4*i+1]%119+100 || d->field1C!=255 || d->field1D!=0x16
       || d->field1E!=30 || d->field20!=8 || bits(d->field24)!=bits(expected24)
       || bits(d->field28)!=bits(expectedScale) || bits(d->field2C)!=bits(expectedScale)
       || bits(d->position.x)!=bits(expectedPosition[0]) || bits(d->position.y)!=bits(expectedPosition[1])
       || bits(d->position.z)!=bits(expectedPosition[2]) || bits(d->field4C)!=bits(expected4C)
       || bits(d->field3C) || bits(d->field40) || bits(d->field44) || bits(d->field48)
       || bits(d->field50) || bits(d->field54) || d->flags!=expectedFlags
       || d->field60!=3 || d->field61!=3 || d->field62!=0x1A || d->field63!=255) error=7;
    snapshots[i]=*d;
    lastDescriptor=d;
    if(mutateSubmitProgress && !i) state()->parameters.field08=2.25f;
    if(!(failures&(1<<i))) {
        /* Model the retained core's full descriptor copy; holes stay unspecified. */
        for(j=0;j<0x70;j++) results[i].bytes[0x10+j]=((u8 *)d)[j];
    }
    if(mutateDescriptor && !i) {
        d->field00=expectedField00=0x12345678; d->field17=expectedField17=42;
        d->field14=99; d->field28=-1; d->flags=expectedFlags=0xABCDFFFF;
    }
    return failures&(1<<i)?NULL:results[i].bytes;
}
void *memcpy(void *destination, const void *source, u32 length) {
    u32 i;
    if(inWeighted) {
        if(destination!=record.bytes+0x28 || length!=24) error=8;
    } else {
        int k=submissions-1;
        push('M'); copies++;
        if(k<0 || k>=8 || destination!=results[k].bytes+0xA8 || length!=4
           || bits(*(const f32 *)source)!=expectedBonus || failures&(1<<k)) error=9;
        if(mutateCopyProgress && copies==1) state()->parameters.field08=3.125f;
    }
    for(i=0;i<length;i++) ((u8 *)destination)[i]=((const u8 *)source)[i];
    return destination;
}
static void initialize(void) {
    int i,j;
    f32 *globals[8]={&D_800A1390,&D_800A1394,&D_800A1398,&D_800A139C,
                    &D_800A13A0,&D_800A13A4,&D_800A13A8,&D_800A13AC};
    for(i=0;i<8;i++) *globals[i]=number(literalWords[i]);
    for(i=0;i<80;i++) record.bytes[i]=0xA5;
    for(i=0;i<8;i++) for(j=0;j<0xC0;j++) results[i].bytes[j]=0xA5;
    for(i=0;i<64;i++) samples[i]=0;
    for(i=0;i<32;i++) integers[i]=i;
    for(i=0;i<8;i++) {
        samples[6*i+1]=0.25f; samples[6*i+2]=0.5f; samples[6*i+3]=0.125f;
        samples[6*i+4]=0.75f; samples[6*i+5]=0.5f; samples[6*i+6]=0.25f;
    }
    record.bytes[0xC]=expectedSlot=0xC3; record.bytes[1]=expectedContext=0x91;
    state()->position.x=-100; state()->position.y=200; state()->position.z=-300;
    state()->parameters.field00=state()->parameters.field04=0; state()->parameters.field08=1.125f;
    D_800BE9A4=1;
    expectedFlags=0x801E05; expectedField00=0x200005; expectedField17=255;
    expectedBonus=bits(D_800A1390); expectedPeriod=D_800A1394;
    floatCalls=integerCalls=mathCalls=submissions=copies=error=failures=traceLength=0;
    mutateInitial=mutateConstants=mutatePosition=mutateMetadata=0;
    mutateSubmitProgress=mutateCopyProgress=mutateDescriptor=mutateFlags=flagsOverride=0;
    inWeighted=weightedFloats=weightedIntegers=weightedPoints=weightedAllocations=0;
    lastDescriptor=NULL;
}
static int fences(void) {
    int i,k;
    for(i=0;i<80;i++) if(i!=1 && i!=0xC && (i<0x28 || i>=0x40) && record.bytes[i]!=0xA5) return 1;
    for(k=0;k<8;k++) for(i=0;i<0xC0;i++) {
        if(k<submissions && !(failures&(1<<k)) && i>=0x10 && i<0x80) continue;
        if(k<submissions && !(failures&(1<<k)) && i>=0xA8 && i<0xAC) {
            if(results[k].bytes[i]!=((u8 *)&expectedBonus)[i-0xA8]) return 2;
        } else if(results[k].bytes[i]!=0xA5) return 3;
    }
    return 0;
}
''' + cls.spherical + '\n' + cls.wrapper + '\n' + cls.body + '\n'

    def test_layout_and_one_complete_successful_emission(self):
        self.run_host(r'''
ChildEmissionDescriptor113D60 d;
EventPositionPayload113D60 p;
if(sizeof(d)!=0x70 || (u8 *)&d.position-(u8 *)&d!=0x30
   || (u8 *)&d.flags-(u8 *)&d!=0x58 || (u8 *)&d.field60-(u8 *)&d!=0x60
   || sizeof(p)!=24 || (u8 *)&p.parameters-(u8 *)&p!=12) return 1;
initialize(); func_150E8D5C(record.bytes);
if(error || submissions!=1 || copies!=1 || floatCalls!=7 || integerCalls!=4 || mathCalls!=4
   || state()->parameters.field08!=0.125f || !trace_is("FIIFFIIFFFCSCSFAM") || fences()) return 2;
''')

    def test_unsigned_rng_residues_and_all_four_flag_combinations(self):
        self.run_host(r'''
static u32 words[]={0,1,15,16,118,119,120,0x7FFFFFFF,0x80000000,0xFFFFFFFE,0xFFFFFFFF};
int i,j,flags;
for(i=0;i<11;i++) for(j=0;j<11;j++) for(flags=0;flags<4;flags++) {
    initialize(); integers[0]=words[i]; integers[1]=words[j];
    integers[2]=0xFFFFFFFEu|(flags&1); integers[3]=0x80000000u|((flags>>1)&1);
    func_150E8D5C(record.bytes);
    if(error || submissions!=1 || copies!=1 || fences()) return 1;
}
''')

    def test_unclamped_signed_scale_and_radius_samples(self):
        self.run_host(r'''
static f32 values[]={-2,-1,0,0.25f,1,2};
int i,j;
for(i=0;i<6;i++) for(j=0;j<6;j++) {
    initialize(); samples[1]=values[i]; samples[5]=values[j];
    func_150E8D5C(record.bytes);
    if(error || submissions!=1 || copies!=1 || fences()) return 1;
}
''')

    def test_strict_accumulator_repeats_and_failed_allocations_still_consume(self):
        self.run_host(r'''
static f32 progress[]={-1,0,0.5f,1,1.125f,2,2.125f,3,3.125f,5};
static int counts[]={0,0,0,0,1,1,2,2,3,4};
int i,failed,success,k;
for(i=0;i<10;i++) for(failed=0;failed<16;failed++) {
    initialize(); state()->parameters.field08=progress[i]; failures=failed; success=0;
    for(k=0;k<counts[i];k++) success+=!(failed&(1<<k));
    func_150E8D5C(record.bytes);
    if(error || submissions!=counts[i] || copies!=success || floatCalls!=1+6*counts[i]
       || integerCalls!=4*counts[i] || mathCalls!=4*counts[i]
       || state()->parameters.field08!=progress[i]-(f32)counts[i] || fences()) return 1;
}
''')

    def test_initial_rng_mutations_are_observed_before_rate_and_snapshots(self):
        self.run_host(r'''
initialize(); mutateInitial=1; samples[0]=0.5f;
func_150E8D5C(record.bytes);
if(error || submissions!=1 || copies!=1 || state()->parameters.field08!=0.25f
   || state()->parameters.field00!=0.5f || state()->parameters.field04!=0.5f
   || expectedBonus!=bits(3) || expectedPeriod!=4 || fences()) return 1;
''')

    def test_per_sample_globals_live_but_bonus_and_period_captured(self):
        self.run_host(r'''
initialize(); state()->parameters.field08=3.125f; mutateConstants=1;
func_150E8D5C(record.bytes);
if(error || submissions!=3 || copies!=3 || D_800A1390!=99 || D_800A1394!=100
   || expectedBonus!=literalWords[0] || bits(expectedPeriod)!=literalWords[1]
   || state()->parameters.field08!=0.125f || fences()) return 1;
''')

    def test_parent_position_after_math_and_metadata_after_last_sample(self):
        self.run_host(r'''
initialize(); mutatePosition=mutateMetadata=1;
func_150E8D5C(record.bytes);
if(error || submissions!=1 || snapshots[0].position.x!=1002.5f
   || snapshots[0].position.y!=2005 || snapshots[0].position.z!=3005
   || state()->position.x!=9000 || record.bytes[0xC]!=0xC7 || record.bytes[1]!=0x81 || fences()) return 1;
''')

    def test_descriptor_constants_persist_but_per_loop_fields_reset(self):
        self.run_host(r'''
initialize(); state()->parameters.field08=3.125f; mutateDescriptor=mutateFlags=1;
func_150E8D5C(record.bytes);
if(error || submissions!=3 || copies!=3 || snapshots[0].field00!=0x200005
   || snapshots[1].field00!=0x12345678 || snapshots[2].field17!=42
   || snapshots[1].field14!=15 || snapshots[2].field28<0 || fences()) return 1;
''')

    def test_progress_reloaded_after_submit_or_bonus_copy_even_on_failure(self):
        self.run_host(r'''
int failed;
for(failed=0;failed<2;failed++) {
    initialize(); mutateSubmitProgress=1; failures=failed;
    func_150E8D5C(record.bytes);
    if(error || submissions!=2 || copies!=2-failed || state()->parameters.field08!=0.25f || fences()) return 1;
}
initialize(); mutateCopyProgress=1;
func_150E8D5C(record.bytes);
if(error || submissions!=3 || copies!=3 || state()->parameters.field08!=0.125f || fences()) return 2;
''')

    def test_nonfinite_rates_stop_at_strict_gate_without_extra_callbacks(self):
        self.run_host(r'''
static u32 words[]={0x7FC12345,0x7F800000,0xFF800000};
int i;
for(i=0;i<3;i++) {
    initialize(); samples[0]=number(words[i]); D_800BE9A4=0;
    state()->parameters.field00=0.25f; state()->parameters.field04=0.5f;
    func_150E8D5C(record.bytes);
    if(error || floatCalls!=1 || integerCalls || mathCalls || submissions || copies
       || state()->parameters.field08==state()->parameters.field08 || !trace_is("F") || fences()) return 1;
}
initialize(); state()->parameters.field00=0.25f; state()->parameters.field04=0.5f;
state()->parameters.field08=0.875f; D_800BE9A4=0.25f; samples[0]=0.5f;
func_150E8D5C(record.bytes);
if(error || submissions || floatCalls!=1 || state()->parameters.field08!=1 || fences()) return 2;
''')

    def test_actual_weighted_parent_payload_flows_into_actual_child(self):
        connection = r'''
f32 D_800A1384, D_800A1388, D_800A138C, D_800DCD90;
s32 D_800BE9E8;
u8 *D_800DCDC4;
static f32 origin[3];
f32 *func_15144B34(s32 player) { if(player!=7) error=20; return origin; }
void func_1514470C(void *descriptor, void *output) {
    f32 *p=output;
    if(descriptor!=origin) error=21;
    weightedPoints++; p[0]=p[1]=p[2]=0;
}
void *func_15149130(s16 duration, s8 index, s8 kind, s8 source, u8 active,
                   u8 mode, s32 size, u8 slot, s32 context) {
    weightedAllocations++;
    if(duration!=(s16)(0xFFFFFFFFu%13+5) || index!=-1 || kind!=0x34 || source!=-1 || active!=1 || mode || size!=24
       || slot!=expectedSlot || context!=expectedContext) error=22;
    return record.bytes;
}
''' + self.weighted + '\n'
        original = self.fixture
        try:
            self.fixture += connection
            self.run_host(r'''
union { u32 alignment; u8 bytes[64]; } parent;
EventPayload113D60 *p=(EventPayload113D60 *)(parent.bytes+0x28);
EventWeightNode113D60 node;
int i;
initialize(); for(i=0;i<64;i++) parent.bytes[i]=0xA5;
parent.bytes[0xC]=expectedSlot; parent.bytes[1]=expectedContext;
p->field00=p->field04=0; p->field08=1.125f;
origin[0]=origin[1]=origin[2]=0; D_800BE9E8=7;
D_800DCD90=1; D_800A138C=100; D_800A1388=1.25f; D_800A1384=0;
node.descriptor=origin; node.weight=1; node.next=NULL; D_800DCDC4=(u8 *)&node;
inWeighted=1; func_150E8B1C(parent.bytes); inWeighted=0;
if(error || weightedFloats!=2 || weightedIntegers!=1 || weightedPoints!=1 || weightedAllocations!=1
   || p->field08!=0.125f || state()->parameters.field00!=1.25f
   || state()->parameters.field04 || state()->parameters.field08) return 1;
func_150E8D5C(record.bytes);
if(error || submissions!=1 || copies!=1 || floatCalls!=7 || integerCalls!=4
   || state()->parameters.field08!=0.25f || fences()) return 2;
''')
        finally:
            self.fixture = original

    def test_retail_callback_literals_reserved_holes_and_no_instruction_guards(self):
        self.assertEqual(struct.unpack_from('>2I', self.rom, 0x22F074), (0x150E8B1C, 0x150E8D5C))
        words = struct.unpack('>224I', self.rom[0x11620C:0x11658C])
        self.assertEqual(words[0], 0x27BDFEF8)
        self.assertIn(0x3C01426C, words)
        self.assertNotIn('memset', self.body)
        self.assertNotIn('reserved5C', self.body)
        self.assertNotIn('reserved64', self.body)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] == 'func_150E8D5C' for row in csv.DictReader(source)))

    def test_fresh_ido_body_and_linked_constructor_wrappers(self):
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
        script.write_text('SECTIONS { .text 0x150E8D5C : SUBALIGN(4) { *(.text) } }\n')
        targets = {name: int(name[2:], 16) for name in self.constants}
        targets.update({'D_800BE9A4': 0x800BE9A4, 'func_150ADA68': 0x150ADA68,
                        'func_150ADA20': 0x150ADA20, 'func_151436B4': 0x151436B4,
                        'func_15130374': 0x15130374, 'memcpy': 0x10022EC0})
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_150E8D5C',
            *(f'--defsym={name}=0x{value:X}' for name, value in targets.items()),
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', '.text', str(elf), str(binary)],
                       check=True, capture_output=True)
        data = binary.read_bytes()
        words = struct.unpack('>' + 'I' * (len(data) // 4), data)
        count = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        self.assertEqual(count, 219)
        self.assertEqual(0x10000 - (words[0] & 0xFFFF), 0x120)
        padded = words[:count] + (0,) * (224 - count)
        retail = struct.unpack('>224I', self.rom[0x11620C:0x11658C])
        self.assertEqual(sum(a != b for a, b in zip(padded, retail)), 213)
        production = self.root / 'conker/build/conker.us.elf'
        self.assertTrue(production.is_file(), 'production relink is required')
        linked, _, addresses = match_progress.load_elf_functions(str(production), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_150E8D5C'], 0x150E8D5C)
        self.assertEqual(tuple(linked['func_150E8D5C']), padded)
        self.assertEqual(hashlib.sha256(struct.pack('>224I', *padded)).hexdigest(),
                         '5804b8b394d8f1474e6e974134cb15f9c9db4a9c56f63df710ec7a71087a2f34')
        for name, count in (('func_15130280', 61), ('func_15130374', 18), ('func_151303BC', 12),
                            ('func_151436B4', 34), ('func_150E8A80', 39), ('func_150E90DC', 39)):
            with self.subTest(function=name):
                self.assertEqual(len(linked[name]), count)
                first = 0x2D4B0 + addresses[name] - 0x15000000
                self.assertEqual(struct.pack('>' + 'I' * count, *linked[name]), self.rom[first:first+4*count])
        print('child emission slot:', {'body_words': 219, 'slot_words': 224,
              'frame_bytes': 0x120, 'different_words': 213})


if __name__ == '__main__':
    unittest.main()
