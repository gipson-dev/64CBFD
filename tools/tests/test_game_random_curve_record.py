import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests.test_game_row_destination_fill import START


class GameRandomCurveRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_113D60.c').read_text()
        cls.body = re.search(r'void \*func_150E7994\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';', source, re.S).group(0)
            for name in ('EmitterPosition113D60', 'RandomPacket113D60', 'CurvePayload113D60'))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = ('typedef signed char s8; typedef unsigned char u8; typedef short s16; '
                     'typedef int s32; typedef unsigned int u32; typedef float f32;\n'
                     '#define NULL ((void *)0)\n')
        cls.fixture = cls.types + cls.layouts + r'''
s32 D_800BE9E8;
u8 *D_800DBFF0;
static union { u32 alignment; u8 bytes[0x40100]; } storage;
static u8 actors[4*0x9A0];
static u8 *record=storage.bytes+16;
static u32 randomWord;
static f32 samples[4], weights[8], expectedParameter, expectedStep, expectedValue;
static s16 expectedCount;
static u8 expectedSlot;
static s32 expectedContext;
static int actorCalls, integerCalls, packetCalls, allocatorCalls, copyCalls;
static int floatCalls, weightCalls, failAllocation, error, mutateGlobals;
static u32 bits(f32 value) { union { f32 f; u32 u; } word; word.f=value; return word.u; }
static f32 number(u32 value) { union { f32 f; u32 u; } word; word.u=value; return word.f; }
static f32 coordinate(int axis) {
    int base=axis?4:0;
    f32 p0=axis?samples[0]*160.0f-80.0f:-146.0f;
    f32 p1=axis?samples[1]*160.0f-80.0f:-50.0f;
    f32 p2=axis?samples[2]*160.0f-80.0f:50.0f;
    f32 p3=axis?samples[3]*160.0f-80.0f:146.0f;
    f32 a=weights[base+2]*p0, b=weights[base+1]*p1;
    f32 c=weights[base]*p2, d=weights[base+3]*p3;
    return d+((a+b)+c);
}
void func_1512D748(void *actor,s32 arg1,s32 arg2) {
    if(actor!=actors+2*0x9A0 || arg1 || arg2!=1 || integerCalls || packetCalls || allocatorCalls) error=1;
    actorCalls++;
    if(mutateGlobals) { D_800BE9E8=0; D_800DBFF0=actors+0x9A0; }
}
s32 func_150ADA20(void) {
    if(actorCalls!=1 || integerCalls || packetCalls || allocatorCalls) error=2;
    integerCalls++;
    return (s32)randomWord;
}
s32 func_151D8868(void *data,s32 arg1,s32 arg2,s32 arg3) {
    RandomPacket113D60 *packet=data;
    if(actorCalls!=1 || integerCalls!=1 || packetCalls || allocatorCalls
       || packet->kind!=1 || packet->duration!=(s16)(randomWord%11+30)
       || packet->count!=8 || packet->mode!=1 || packet->index!=-1
       || arg1 || arg2!=255 || arg3) error=3;
    packetCalls++;
    return -123;
}
void *func_151491F4(s16 arg0,s8 arg1,s8 arg2,u8 arg3,u8 arg4,s32 size,u8 slot,s32 context) {
    if(actorCalls!=1 || integerCalls!=1 || packetCalls!=1 || allocatorCalls || copyCalls
       || arg0!=300 || arg1!=-1 || arg2!=16 || arg3!=1 || arg4!=12
       || size!=expectedCount*8+16 || slot!=expectedSlot || context!=expectedContext) error=4;
    allocatorCalls++;
    return failAllocation?NULL:record;
}
void *memcpy(void *destination,const void *source,u32 length) {
    const CurvePayload113D60 *payload=source;
    u32 i;
    if(destination!=record+0x28 || length!=12 || allocatorCalls!=1 || copyCalls || floatCalls || weightCalls
       || bits(payload->value)!=bits(expectedValue) || bits(payload->progress)!=0
       || payload->count!=expectedCount || payload->cursor) error=5;
    copyCalls++;
    for(i=0;i<length;i++) ((u8 *)destination)[i]=((const u8 *)source)[i];
    return destination;
}
f32 func_150ADA68(void) {
    int index=floatCalls++;
    CurvePayload113D60 *payload=(CurvePayload113D60 *)(record+0x28);
    if(index>=4 || copyCalls!=1 || weightCalls || bits(payload->value)!=bits(expectedValue)
       || bits(payload->progress)!=0 || payload->count!=expectedCount || payload->cursor) { error=6; return 0; }
    return samples[index];
}
static f32 weight(int kind,f32 parameter) {
    static int sequence[4]={2,1,0,3};
    int index=weightCalls%8, point=weightCalls/8;
    EmitterPosition113D60 *output=(EmitterPosition113D60 *)(record+0x38);
    if(floatCalls!=4 || point>=expectedCount || kind!=sequence[index%4]
       || bits(parameter)!=bits(expectedParameter)) error=7;
    if(index<4 && (bits(output[point].x)!=0xA5A5A5A5 || bits(output[point].y)!=0xA5A5A5A5)) error=8;
    if(index>=4 && (bits(output[point].x)!=bits(coordinate(0)) || bits(output[point].y)!=0xA5A5A5A5)) error=9;
    if(point && (bits(output[point-1].x)!=bits(coordinate(0)) || bits(output[point-1].y)!=bits(coordinate(1)))) error=10;
    weightCalls++;
    if(index==7) expectedParameter+=expectedStep;
    return weights[index];
}
f32 func_15142B04(f32 parameter) { return weight(2,parameter); }
f32 func_15142AC0(f32 parameter) { return weight(1,parameter); }
f32 func_15142A80(f32 parameter) { return weight(0,parameter); }
f32 func_15142B44(f32 parameter) { return weight(3,parameter); }
static void initialize(s16 count,int fail) {
    u32 i;
    for(i=0;i<sizeof(storage.bytes);i++) storage.bytes[i]=0xA5;
    record=storage.bytes+16; D_800DBFF0=actors; D_800BE9E8=2;
    expectedCount=count; expectedSlot=0xCD; expectedContext=(s32)0x87654321;
    expectedValue=number(0x80000000); expectedParameter=-1.0f;
    expectedStep=count>=2?3.0f/(count-1):0;
    samples[0]=0; samples[1]=0.25f; samples[2]=0.75f; samples[3]=1;
    weights[0]=0.125f; weights[1]=-2; weights[2]=3; weights[3]=0.5f;
    weights[4]=1.5f; weights[5]=0.25f; weights[6]=-1; weights[7]=2;
    actorCalls=integerCalls=packetCalls=allocatorCalls=copyCalls=floatCalls=weightCalls=error=mutateGlobals=0;
    failAllocation=fail; randomWord=0xFFFFFFFF;
}
static int check_success(void) {
    int i;
    EmitterPosition113D60 *output=(EmitterPosition113D60 *)(record+0x38);
    if(error || actorCalls!=1 || integerCalls!=1 || packetCalls!=1 || allocatorCalls!=1
       || copyCalls!=1 || floatCalls!=4 || weightCalls!=8*expectedCount) return 1;
    for(i=0;i<expectedCount;i++)
        if(bits(output[i].x)!=bits(coordinate(0)) || bits(output[i].y)!=bits(coordinate(1))) return 2;
    for(i=0;i<16+0x28;i++) if(storage.bytes[i]!=0xA5) return 3;
    for(i=0x34;i<0x38;i++) if(record[i]!=0xA5) return 4;
    for(i=0;i<16;i++) if(record[0x38+expectedCount*8+i]!=0xA5) return 5;
    return 0;
}
''' + cls.body + '\n'

    def run_host(self, body):
        compiler = shutil.which('cc')
        if compiler is None:
            self.skipTest('host compiler is unavailable')
        source = self.path / (self._testMethodName + '.c')
        binary = source.with_suffix('')
        source.write_text(self.fixture + 'int run(void) {\n' + body + '\nreturn 0;\n}\n' + START)
        result = subprocess.run([compiler, '-m32', '-O2', '-std=c99', '-fno-strict-aliasing',
            '-msse2', '-mfpmath=sse', '-mstackrealign', '-ffreestanding', '-nostdlib', '-static', '-fno-pie', '-no-pie',
            '-fno-stack-protector', '-ffp-contract=off', '-Wall', '-Wextra', '-Werror',
            '-Wno-unused-parameter', '-Wno-unused-function', str(source), '-o', str(binary)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([str(binary)], capture_output=True, timeout=10)
        self.assertEqual(result.returncode, 0, 'random curve record fixture failed')

    def test_signed_count_gate_has_no_callbacks_or_global_dereference(self):
        self.run_host(r'''
static s32 counts[]={-32768,-255,-1,0,1,32768,65535,65536,65537};
int i,j;
for(i=0;i<9;i++) {
    initialize((s16)counts[i],0); D_800DBFF0=NULL; D_800BE9E8=(s32)0x80000000;
    if(func_150E7994((s16)counts[i],expectedValue,expectedSlot,expectedContext)!=NULL) return 1;
    if(error || actorCalls || integerCalls || packetCalls || allocatorCalls || copyCalls || floatCalls || weightCalls) return 2;
    for(j=0;j<128;j++) if(storage.bytes[j]!=0xA5) return 3;
}
''')

    def test_allocation_failure_preserves_packet_and_stops_before_copy_and_samples(self):
        self.run_host(r'''
static s16 counts[]={2,4,6,32767};
static u32 words[]={0,1,10,11,0x80000000,0xFFFFFFFE,0xFFFFFFFF};
int i,j,k;
for(i=0;i<4;i++) for(j=0;j<7;j++) {
    initialize(counts[i],1); randomWord=words[j]; mutateGlobals=1;
    if(func_150E7994(expectedCount,expectedValue,expectedSlot,expectedContext)!=NULL) return 1;
    if(error || actorCalls!=1 || integerCalls!=1 || packetCalls!=1 || allocatorCalls!=1
       || copyCalls || floatCalls || weightCalls) return 2;
    for(k=0;k<128;k++) if(storage.bytes[k]!=0xA5) return 3;
}
''')

    def test_point_counts_payload_and_per_coordinate_store_order(self):
        self.run_host(r'''
static s16 counts[]={2,3,4,5,6,7,31,127,256,32767};
int i;
for(i=0;i<10;i++) {
    initialize(counts[i],0); mutateGlobals=1;
    if(func_150E7994(expectedCount,expectedValue,expectedSlot,expectedContext)!=record) return 1;
    if(check_success()) return 2;
}
''')

    def test_float_samples_rounding_unsigned_remainder_and_argument_narrowing(self):
        self.run_host(r'''
static f32 fractions[]={-1,0,0.125f,0.5f,1,2};
static u32 words[]={0,10,11,0x80000000,0xFFFFFFFF};
static s32 slots[]={-1,0,255,256,65535,65536};
int i,j;
for(i=0;i<6;i++) for(j=0;j<5;j++) {
    initialize(4,0); randomWord=words[j]; expectedSlot=(u8)slots[i]; expectedValue=fractions[i];
    samples[0]=fractions[i]; samples[1]=fractions[(i+1)%6];
    samples[2]=fractions[(i+2)%6]; samples[3]=fractions[(i+3)%6];
    weights[0]=number(0x4B800001); weights[1]=-number(0x4B800000);
    weights[2]=0.125f; weights[3]=-0.25f;
    if(func_150E7994((s16)65540,expectedValue,(u8)slots[i],expectedContext)!=record) return 1;
    if(check_success()) return 2;
}
''')

    def test_metadata_extent_offsets_and_independent_ido_contract(self):
        self.run_host(r'''
if(sizeof(CurvePayload113D60)!=12 || sizeof(EmitterPosition113D60)!=8 || sizeof(RandomPacket113D60)!=8) return 1;
if(__builtin_offsetof(CurvePayload113D60,progress)!=4 || __builtin_offsetof(CurvePayload113D60,count)!=8
   || __builtin_offsetof(CurvePayload113D60,cursor)!=10) return 2;
''')
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file():
            self.skipTest('IDO is unavailable')
        for tool in ('mips-linux-gnu-ld', 'mips-linux-gnu-objcopy'):
            if shutil.which(tool) is None:
                self.skipTest(tool + ' is unavailable')
        declarations = '''
extern s32 D_800BE9E8; extern u8 *D_800DBFF0;
void func_1512D748(void *,s32,s32); s32 func_150ADA20(void); f32 func_150ADA68(void);
s32 func_151D8868(void *,s32,s32,s32);
void *func_151491F4(s16,s8,s8,u8,u8,s32,u8,s32); void *memcpy(void *,const void *,u32);
f32 func_15142B04(f32); f32 func_15142AC0(f32); f32 func_15142A80(f32); f32 func_15142B44(f32);
'''
        source, obj = self.path / 'curve.c', self.path / 'curve.o'
        source.write_text(self.types + self.layouts + '\n' + declarations + self.body + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
            '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3',
            '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        elf, binary, script = (self.path / ('curve' + suffix) for suffix in ('.elf', '.bin', '.ld'))
        script.write_text('SECTIONS { .text 0x150E7994 : SUBALIGN(4) { *(.text) } }\n')
        targets = {'D_800BE9E8': 0x800BE9E8, 'D_800DBFF0': 0x800DBFF0,
            'func_1512D748': 0x1512D748, 'func_150ADA20': 0x150ADA20, 'func_150ADA68': 0x150ADA68,
            'func_151D8868': 0x151D8868, 'func_151491F4': 0x151491F4, 'memcpy': 0x10022EC0,
            'func_15142B04': 0x15142B04, 'func_15142AC0': 0x15142AC0,
            'func_15142A80': 0x15142A80, 'func_15142B44': 0x15142B44}
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_150E7994',
            *(f'--defsym={name}=0x{address:X}' for name, address in targets.items()),
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', '.text', str(elf), str(binary)],
            check=True, capture_output=True)
        words = list(struct.unpack('>' + 'I' * (binary.stat().st_size // 4), binary.read_bytes()))
        end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        self.assertLessEqual(end, 194)
        self.assertEqual(words[0], 0x27BDFF38)
        self.assertEqual(words[end-1], 0x27BD00C8)
        calls = [0x10000000 | ((word & 0x3FFFFFF) << 2) for word in words[:end] if word >> 26 == 3]
        expected = [0x1512D748, 0x150ADA20, 0x151D8868, 0x151491F4, 0x10022EC0]
        expected += [0x150ADA68] * 4
        expected += [0x15142B04, 0x15142AC0, 0x15142A80, 0x15142B44] * 2
        self.assertEqual(calls, expected)
        retail = (self.root / 'conker/conker.us.bin').read_bytes()[0x114E44:0x11514C]
        self.assertEqual(words[:end], list(struct.unpack('>194I', retail)))


if __name__ == '__main__':
    unittest.main()
