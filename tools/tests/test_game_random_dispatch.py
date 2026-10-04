import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests import test_game_vector_random_parameters as vector_tests


class GameRandomDispatchTests(unittest.TestCase):
    run_host = vector_tests.GameVectorRandomParameterTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / "conker/src/game/generated_113D60.c").read_text()
        cls.body = re.search(r"void func_150E7290\(u8 index, u8 slot, s32 context\) \{\n.*?\n\}", source, re.S).group(0)
        cls.packet = re.search(r"typedef struct RandomPacket113D60 \{.*?\} RandomPacket113D60;", source, re.S).group(0)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = "typedef unsigned char u8; typedef signed char s8; typedef short s16; typedef unsigned short u16; typedef int s32; typedef unsigned int u32; typedef float f32;\n"
        cls.fixture = cls.types + cls.packet + r'''
f32 D_800A1340,D_800A1344,D_800A1348,D_800A134C;
s32 D_80088A5C[2];
static f32 samples[5],capturedPosition[2],capturedScale;
static u32 words[6];
static s32 captured[11];
static int floats,integers,positionCalls,alternateCalls,soundCalls,eventCalls,packetCalls,error,mutate;
static char trace[32]; static int traceCount;
static RandomPacket113D60 capturedPacket;
static void push(char code) { if(traceCount>=31) error=1; else trace[traceCount++]=code; }
int trace_equals(const char *expected) {
    int i=0;
    while(expected[i]) { if(i>=traceCount || trace[i]!=expected[i]) return 0; i++; }
    return i==traceCount;
}
f32 func_150ADA68(void) {
    int index=floats++;
    push('F');
    if(index>=5) { error=2; return 0; }
    if(mutate && index==1) { D_80088A5C[0]=99; D_80088A5C[1]=100; }
    return samples[index];
}
s32 func_150ADA20(void) {
    int index=integers++;
    push('I');
    if(index>=6) { error=3; return 0; }
    if(mutate && index==3) D_800A1348=4;
    return (s32)words[index];
}
static void capture(s16 id,u8 flags,s32 duration,s32 opacity,s32 size0,s32 size1,s32 *pair,s32 mode,u8 slot,s32 context) {
    captured[0]=id; captured[1]=flags; captured[2]=duration; captured[3]=opacity;
    captured[4]=size0; captured[5]=size1; captured[6]=pair[0]; captured[7]=pair[1];
    captured[8]=mode; captured[9]=slot; captured[10]=context;
}
s32 func_150E75A0(f32 *position,f32 scale,s16 id,u8 flags,s32 duration,s32 opacity,
                 s32 size0,s32 size1,s32 *pair,s32 mode,u8 slot,s32 context) {
    push('P'); positionCalls++;
    capturedPosition[0]=position[0]; capturedPosition[1]=position[1]; capturedScale=scale;
    capture(id,flags,duration,opacity,size0,size1,pair,mode,slot,context);
    return -1;
}
s32 func_150E76D0(f32 scale,s16 id,u8 flags,u8 duration,s32 opacity,s32 size0,
                 s32 size1,s32 *pair,s32 mode,u8 slot,s32 context) {
    push('A'); alternateCalls++; capturedScale=scale;
    capture(id,flags,duration,opacity,size0,size1,pair,mode,slot,context);
    return 0;
}
void func_10010F30(s32 id,unsigned short volume,u8 arg2,s16 arg3,u8 arg4) {
    push('S'); soundCalls++;
    if(id!=0x360 || volume!=0x7FFF || arg2 || arg3 || arg4) error=4;
}
void func_15164F0C(u8 kind,u8 index,s32 arg2,u8 slot,s32 context) {
    push('E'); eventCalls++;
    if(kind!=1 || index!=0x23 || arg2 || slot!=0xAB || context!=(s32)0x87654321) error=5;
}
s32 func_151D8868(void *input,s32 arg1,s32 arg2,s32 arg3) {
    RandomPacket113D60 *packet=input;
    push('T'); packetCalls++;
    capturedPacket.kind=packet->kind; capturedPacket.duration=packet->duration;
    capturedPacket.count=packet->count; capturedPacket.mode=packet->mode; capturedPacket.index=packet->index;
    if(arg1 || arg2!=255 || arg3) error=6;
    return -1;
}
void initialize(void) {
    int i;
    D_800A1340=0.125f; D_800A1344=0.75f; D_800A1348=D_800A134C=2;
    D_80088A5C[0]=4; D_80088A5C[1]=5;
    samples[0]=0.0625f; samples[1]=0.5f; samples[2]=0.25f; samples[3]=0.75f; samples[4]=0.5f;
    words[0]=0x80000000; words[1]=1; words[2]=0; words[3]=0xFFFFFFFF;
    words[4]=0x80000001; words[5]=0xFFFFFFFE;
    floats=integers=positionCalls=alternateCalls=soundCalls=eventCalls=packetCalls=error=mutate=traceCount=0;
    for(i=0;i<11;i++) captured[i]=-999;
}
int check_common(int tail) {
    if(error || soundCalls!=1 || eventCalls!=1 || packetCalls!=1) return 1;
    if(captured[0]!=(s16)(words[0]%201+500) || captured[3]!=255 || captured[4]!=64
       || captured[5]!=3 || captured[6]!=4 || captured[7]!=5 || captured[8]!=2
       || captured[9]!=0xAB || captured[10]!=(s32)0x87654321) return 2;
    if(capturedPacket.kind!=1 || capturedPacket.duration!=(s16)(words[tail]%26+25)
       || capturedPacket.count!=(u8)(words[tail+1]%6+3) || capturedPacket.mode!=1
       || capturedPacket.index!=-1) return 3;
    return 0;
}
''' + cls.body + "\n"

    def test_outer_gate_equal_above_and_nan_have_no_submissions(self):
        self.run_host(r'''
int i;
for(i=0;i<3;i++) {
    union { u32 word; f32 value; } nan;
    initialize(); nan.word=0x7FC00000;
    samples[0]=i==0 ? 0.125f : i==1 ? 1 : nan.value;
    func_150E7290(0x23,0xAB,(s32)0x87654321);
    if(error || floats!=1 || integers || positionCalls || alternateCalls || soundCalls || eventCalls || packetCalls) return 1;
    if(!trace_equals("F")) return 2;
}
''')

    def test_positioned_path_all_flags_unsigned_remainders_and_tail(self):
        self.run_host(r'''
int flags;
for(flags=0;flags<4;flags++) {
    initialize(); words[1]=(flags&1) ? 0xFFFFFFFF : 0x80000000;
    words[2]=(flags&2) ? 0x80000001 : 0xFFFFFFFE;
    func_150E7290(0x23,0xAB,(s32)0x87654321);
    if(check_common(4) || positionCalls!=1 || alternateCalls || floats!=5 || integers!=6) return 1;
    if(capturedPosition[0]!=-75 || capturedPosition[1]!=50 || capturedScale!=550) return 2;
    if(captured[1]!=(9 | ((flags&1)?2:0) | ((flags&2)?4:0)) || captured[2]!=(s32)(words[3]%26+100)) return 3;
    if(!trace_equals("FFFFFIIIIPSEIIT")) return 4;
}
''')

    def test_alternate_path_threshold_boundary_and_nan(self):
        self.run_host(r'''
int i;
for(i=0;i<3;i++) {
    union {u32 word;f32 value;} nan;
    initialize(); nan.word=0x7FC00000;
    samples[1]=i==0 ? 0.75f : i==1 ? 1 : nan.value;
    samples[2]=0.5f;
    func_150E7290(0x23,0xAB,(s32)0x87654321);
    if(check_common(2) || positionCalls || alternateCalls!=1 || floats!=3 || integers!=4) return 1;
    if(capturedScale!=400 || captured[1]!=9 || captured[2]!=(u8)(words[1]%26+100)) return 2;
    if(!trace_equals("FFFIIASEIIT")) return 3;
}
''')

    def test_pair_snapshot_and_scale_read_after_rng_callbacks(self):
        self.run_host(r'''
initialize(); mutate=1;
func_150E7290(0x23,0xAB,(s32)0x87654321);
if(check_common(4) || capturedScale!=1100 || D_80088A5C[0]!=99) return 1;
if(!trace_equals("FFFFFIIIIPSEIIT")) return 2;
''')

    def test_packet_layout_and_independent_ido_body_fit(self):
        self.run_host(r'''
if(sizeof(RandomPacket113D60)!=8 || __builtin_offsetof(RandomPacket113D60,duration)!=2
   || __builtin_offsetof(RandomPacket113D60,count)!=4 || __builtin_offsetof(RandomPacket113D60,mode)!=5
   || __builtin_offsetof(RandomPacket113D60,index)!=6) return 1;
''')
        compiler = self.root / "ido/ido5.3_recomp/cc"
        if not compiler.is_file():
            self.skipTest("IDO compiler is unavailable")
        for tool in ("mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(tool) is None:
                self.skipTest(tool + " is unavailable")
        original = (self.root / "conker/src/game/generated_113D60.c").read_text()
        prototypes = original[original.index("s32 func_150E75A0("):original.index("f32 func_150484A0(")]
        source, obj = self.path / "dispatch.c", self.path / "dispatch.o"
        source.write_text(self.types+self.packet+"\n"+prototypes+
            "extern f32 D_800A1340,D_800A1344,D_800A1348,D_800A134C; extern s32 D_80088A5C[2];\n"
            "f32 func_150ADA68(void); s32 func_150ADA20(void);\n"+self.body+"\n")
        result = subprocess.run([str(compiler),"-c","-32","-G","0","-Xfullwarn","-Xcpluscomm",
            "-signed","-nostdinc","-non_shared","-Wab,-r4300_mul","-mips2","-o32","-O2","-g3",
            "-o",str(obj),str(source)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(result.stdout+result.stderr,"")
        elf,binary,script=(self.path/("dispatch"+suffix) for suffix in (".elf",".bin",".ld"))
        script.write_text("SECTIONS { .text 0x150E7290 : SUBALIGN(4) { *(.text) } }\n")
        addresses = {name: int(name.split("_")[1],16) for name in
            ("func_150ADA68","func_150ADA20","func_150E75A0","func_150E76D0","func_10010F30",
             "func_15164F0C","func_151D8868","D_800A1340","D_800A1344","D_800A1348","D_800A134C","D_80088A5C")}
        subprocess.run(["mips-linux-gnu-ld","-m","elf32btsmip","-T",str(script),"-e","func_150E7290",
            *("--defsym=%s=0x%X"%(name,address) for name,address in addresses.items()),
            "-o",str(elf),str(obj)],check=True,capture_output=True,text=True)
        subprocess.run(["mips-linux-gnu-objcopy","-O","binary","-j",".text",str(elf),str(binary)],
                       check=True,capture_output=True,text=True)
        data=binary.read_bytes()
        words=struct.unpack(">"+"I"*(len(data)//4),data)
        end=max(i for i,word in enumerate(words) if word==0x03E00008)+2
        self.assertLessEqual(end,196)
        self.assertEqual(words[0],0x27BDFF98)
        callTargets={0x10000000 | ((word&0x3FFFFFF)<<2) for word in words[:end] if word>>26==3}
        self.assertEqual(callTargets,{value for name,value in addresses.items() if name.startswith("func_")})
        self.assertEqual(data[end*4:],bytes(len(data)-end*4))


if __name__ == "__main__":
    unittest.main()
