import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests import test_game_vector_random_parameters as vector_tests
from tools.tests import test_game_random_dispatch as dispatch_tests


class GamePositionedEmitterDescriptorTests(unittest.TestCase):
    run_host = vector_tests.GameVectorRandomParameterTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / "conker/src/game/generated_113D60.c").read_text()
        cls.body = re.search(r"s32 func_150E75A0\([^;{}]+\) \{\n.*?\n\}", source, re.S).group(0)
        cls.layouts = "\n".join(re.search(r"typedef struct " + name + r" \{.*?\} " + name + ";", source, re.S).group(0)
            for name in ("EmitterPosition113D60", "EmitterDescriptor113D60"))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = "typedef unsigned char u8; typedef short s16; typedef unsigned short u16; typedef int s32; typedef unsigned int u32; typedef float f32;\n"
        cls.fixture = cls.types + cls.layouts + r'''
u8 D_80088A64;
static EmitterDescriptor113D60 captured;
static f32 input[2];
static s32 pair[2],*capturedPair,args[6],result;
static int calls,mutate;
s32 func_1515548C(void *data,s32 arg1,s32 *choices,s32 mode,s32 arg4,u8 slot,s32 context) {
    EmitterDescriptor113D60 *d=data;
    calls++;
    captured.position=d->position; captured.scale[0]=d->scale[0]; captured.scale[1]=d->scale[1];
    captured.tag=d->tag; captured.id=d->id; captured.flags=d->flags;
    captured.size0=d->size0; captured.size1=d->size1; captured.kind=d->kind;
    captured.field1B=d->field1B; captured.field1C=d->field1C; captured.field1D=d->field1D;
    captured.duration=d->duration; captured.field1F=d->field1F;
    captured.field20=d->field20; captured.field21=d->field21; captured.field22=d->field22;
    captured.opacity=d->opacity; captured.field24=d->field24; captured.field28=d->field28;
    captured.field2C=d->field2C; captured.field30=d->field30; captured.field34=d->field34;
    captured.field38=d->field38; captured.field3C=d->field3C;
    captured.field40=d->field40; captured.field41=d->field41;
    capturedPair=choices; args[0]=arg1; args[1]=mode; args[2]=arg4; args[3]=slot; args[4]=context;
    if(mutate) { input[0]=99; input[1]=-99; D_80088A64=0; }
    return result;
}
void initialize(void) {
    input[0]=12.5f; input[1]=-25; pair[0]=4; pair[1]=5;
    D_80088A64=0xAB; calls=mutate=0; result=123;
}
int constants_match(void) {
    return captured.kind==4 && captured.field1B==255 && captured.field1C==230
        && captured.field1D==190 && captured.field1F==255 && captured.field20==255
        && captured.field21==255 && captured.field22==255 && captured.field24==1
        && captured.field28==0 && captured.field2C==0 && captured.field30==7
        && captured.field34==60 && captured.field38==128 && captured.field3C==32
        && captured.field40==0 && captured.field41==10;
}
''' + cls.body + "\n"

    def test_initialized_fields_and_submission_arguments(self):
        self.run_host(r'''
initialize();
if(func_150E75A0(input,2.5f,-123,0x85,0x123,0x456,0x18001,0xFFFF,pair,-7,0xCD,(s32)0x87654321)!=123) return 1;
if(calls!=1 || !constants_match() || capturedPair!=pair) return 2;
if(captured.position.x!=12.5f || captured.position.y!=-25 || captured.scale[0]!=2.5f || captured.scale[1]!=2.5f) return 3;
if(captured.tag!=0xAB || captured.id!=-123 || captured.flags!=0xC5 || captured.size0!=(s16)0x8001
   || captured.size1!=-1 || captured.duration!=0x23 || captured.opacity!=0x56) return 4;
if(args[0] || args[1]!=-7 || args[2] || args[3]!=0xCD || args[4]!=(s32)0x87654321) return 5;
if(input[0]!=12.5f || input[1]!=-25 || pair[0]!=4 || pair[1]!=5) return 6;
''')

    def test_return_values_and_narrowing_edges(self):
        self.run_host(r'''
static s32 results[]={0,1,-1,(s32)0x80000000};
static s32 values[]={0,-1,255,256,32767,32768,65535,65536};
int i,j;
for(i=0;i<4;i++) for(j=0;j<8;j++) {
    initialize(); result=results[i]; D_80088A64=(u8)values[j];
    if(func_150E75A0(input,-0.5f,(s16)values[j],(u8)values[j],values[j],values[j],values[j],values[j],0,0,0,0)!=result) return 1;
    if(captured.id!=(s16)values[j] || captured.flags!=((u8)values[j]|0x40)
       || captured.size0!=(s16)values[j] || captured.size1!=(s16)values[j]
       || captured.duration!=(u8)values[j] || captured.opacity!=(u8)values[j]
       || captured.tag!=(u8)values[j] || capturedPair || calls!=1 || !constants_match()) return 2;
}
''')

    def test_submission_observes_copies_before_mutating_sources(self):
        self.run_host(r'''
initialize(); mutate=1;
func_150E75A0(input,3,500,9,100,255,64,3,pair,2,7,8);
if(captured.position.x!=12.5f || captured.position.y!=-25 || captured.tag!=0xAB) return 1;
if(input[0]!=99 || input[1]!=-99 || D_80088A64!=0 || calls!=1) return 2;
''')

    def test_descriptor_extent_and_field_offsets(self):
        self.run_host(r'''
if(sizeof(EmitterPosition113D60)!=8 || sizeof(EmitterDescriptor113D60)!=0x58) return 1;
if(__builtin_offsetof(EmitterDescriptor113D60,scale)!=8 || __builtin_offsetof(EmitterDescriptor113D60,tag)!=0x10
   || __builtin_offsetof(EmitterDescriptor113D60,id)!=0x12 || __builtin_offsetof(EmitterDescriptor113D60,flags)!=0x14
   || __builtin_offsetof(EmitterDescriptor113D60,size0)!=0x16 || __builtin_offsetof(EmitterDescriptor113D60,size1)!=0x18
   || __builtin_offsetof(EmitterDescriptor113D60,kind)!=0x1A || __builtin_offsetof(EmitterDescriptor113D60,duration)!=0x1E
   || __builtin_offsetof(EmitterDescriptor113D60,opacity)!=0x23 || __builtin_offsetof(EmitterDescriptor113D60,field24)!=0x24
   || __builtin_offsetof(EmitterDescriptor113D60,field3C)!=0x3C || __builtin_offsetof(EmitterDescriptor113D60,field40)!=0x40
   || __builtin_offsetof(EmitterDescriptor113D60,reserved42)!=0x42) return 2;
''')

    def test_dispatcher_positioned_path_uses_actual_helper(self):
        case = dispatch_tests.GameRandomDispatchTests
        case.setUpClass()
        try:
            test = case("test_positioned_path_all_flags_unsigned_remainders_and_tail")
            fixture = re.sub(r"s32 func_150E75A0\([^;{}]+\) \{.*?\n\}", self.body, test.fixture, count=1, flags=re.S)
            self.assertNotEqual(fixture, test.fixture)
            submit = r'''
u8 D_80088A64;
s32 func_1515548C(void *data,s32 arg1,s32 *choices,s32 mode,s32 arg4,u8 slot,s32 context) {
    EmitterDescriptor113D60 *descriptor=data;
    push('P'); positionCalls++;
    capturedPosition[0]=descriptor->position.x; capturedPosition[1]=descriptor->position.y;
    capturedScale=descriptor->scale[0];
    if(arg1 || arg4 || descriptor->scale[1]!=capturedScale || descriptor->kind!=4
       || descriptor->tag!=0xA7 || descriptor->field24!=1) error=7;
    capture(descriptor->id,(u8)descriptor->flags,descriptor->duration,descriptor->opacity,
            descriptor->size0,descriptor->size1,choices,mode,slot,context);
    return -7;
}
'''
            declarations = "extern u8 D_80088A64; s32 func_1515548C(void *,s32,s32 *,s32,s32,u8,s32);\n"
            test.fixture = test.types + self.layouts + "\n" + declarations + fixture[len(test.types):] + submit
            test.run_host(r'''
initialize(); D_80088A64=0xA7;
func_150E7290(0x23,0xAB,(s32)0x87654321);
if(check_common(4) || positionCalls!=1 || captured[1]!=(9|2|0x40)) return 1;
if(capturedScale!=550 || capturedPosition[0]!=-75 || capturedPosition[1]!=50) return 2;
if(!trace_equals("FFFFFIIIIPSEIIT")) return 3;
''')
        finally:
            case.doClassCleanups()

    def test_independent_ido_body_fits_with_only_submission_call(self):
        compiler = self.root / "ido/ido5.3_recomp/cc"
        if not compiler.is_file():
            self.skipTest("IDO compiler is unavailable")
        for tool in ("mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(tool) is None:
                self.skipTest(tool + " is unavailable")
        source,obj=self.path/"emitter.c",self.path/"emitter.o"
        source.write_text(self.types+self.layouts+"\nextern u8 D_80088A64;\n"
            "s32 func_1515548C(void *,s32,s32 *,s32,s32,u8,s32);\n"+self.body+"\n")
        result=subprocess.run([str(compiler),"-c","-32","-G","0","-Xfullwarn","-Xcpluscomm",
            "-signed","-nostdinc","-non_shared","-Wab,-r4300_mul","-mips2","-o32","-O2","-g3",
            "-o",str(obj),str(source)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(result.stdout+result.stderr,"")
        elf,binary,script=(self.path/("emitter"+suffix) for suffix in (".elf",".bin",".ld"))
        script.write_text("SECTIONS { .text 0x150E75A0 : SUBALIGN(4) { *(.text) } }\n")
        subprocess.run(["mips-linux-gnu-ld","-m","elf32btsmip","-T",str(script),"-e","func_150E75A0",
            "--defsym=D_80088A64=0x80088A64","--defsym=func_1515548C=0x1515548C","-o",str(elf),str(obj)],
            check=True,capture_output=True,text=True)
        subprocess.run(["mips-linux-gnu-objcopy","-O","binary","-j",".text",str(elf),str(binary)],
                       check=True,capture_output=True,text=True)
        data=binary.read_bytes(); words=struct.unpack(">"+"I"*(len(data)//4),data)
        end=max(i for i,word in enumerate(words) if word==0x03E00008)+2
        self.assertLessEqual(end,76)
        self.assertEqual(words[0],0x27BDFF78)
        self.assertEqual([0x10000000|((word&0x3FFFFFF)<<2) for word in words[:end] if word>>26==3],[0x1515548C])
        self.assertEqual(data[end*4:],bytes(len(data)-end*4))


if __name__ == "__main__":
    unittest.main()
