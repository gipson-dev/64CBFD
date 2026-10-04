import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests import test_game_vector_random_parameters as vector_tests


class GameFixedRandomParameterTests(unittest.TestCase):
    run_host = vector_tests.GameVectorRandomParameterTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / "conker/src/game/generated_113D60.c").read_text()
        match = re.search(r"void func_150E71E4\(s32 arg0, s32 arg1, f32 \*vector, f32 \*output\) \{\n.*?\n\}", source, re.S)
        if match is None:
            raise AssertionError("fixed random parameter definition missing")
        cls.body = match.group(0)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = "typedef int s32; typedef float f32;\n"
        cls.fixture = cls.types + r'''
f32 D_800A1324,D_800A1328,D_800A132C,D_800A1330,D_800A1334,D_800A1338,D_800A133C;
static f32 vector[3],output[10],samples[4],*active,angleX,angleZ;
static int angleCalls,sampleCalls,error,mutate;
f32 func_150484A0(f32 x,f32 z) {
    if(angleCalls || sampleCalls) error=1;
    angleCalls++; angleX=x; angleZ=z;
    if(mutate) { vector[0]=99; vector[2]=-99; }
    return x-z;
}
f32 func_150ADA68(void) {
    int index=sampleCalls;
    if(index>=4) { error=2; return 0; }
    if(angleCalls!=1 || active[0]!=angleX-angleZ || active[2]!=D_800A1324) error=3;
    if(index>=1 && active[4]!=samples[0]*D_800A1328) error=4;
    if(index>=2 && (active[6]!=samples[1]*D_800A132C || active[1]!=D_800A1330
                   || active[3]!=D_800A1334)) error=5;
    if(index==3 && active[5]!=samples[2]*D_800A1338) error=6;
    if(mutate && index==0) D_800A1328=12;
    if(mutate && index==1) { D_800A1330=-9; D_800A1334=11; }
    if(mutate && index==2) D_800A1338=20;
    sampleCalls++;
    return samples[index];
}
static void initialize(void) {
    int i;
    vector[0]=3; vector[1]=6; vector[2]=4;
    for(i=0;i<10;i++) output[i]=-999;
    samples[0]=0.25f; samples[1]=-1; samples[2]=2; samples[3]=0.5f;
    D_800A1324=3; D_800A1328=4; D_800A132C=8; D_800A1330=-5;
    D_800A1334=7; D_800A1338=16; D_800A133C=32;
    angleCalls=sampleCalls=error=mutate=0;
    active=output+1;
}
''' + cls.body + "\n"

    def test_fixed_fields_samples_publication_and_unused_arguments(self):
        self.run_host(r'''
initialize();
func_150E71E4(-1,(s32)0x80000000,vector,active);
if(error || angleCalls!=1 || sampleCalls!=4) return 1;
if(active[0]!=-1 || active[1]!=-5 || active[2]!=3 || active[3]!=7
   || active[4]!=1 || active[5]!=32 || active[6]!=-8 || active[7]!=16) return 2;
if(output[0]!=-999 || output[9]!=-999 || vector[1]!=6) return 3;
''')

    def test_zero_samples_preserve_fixed_fields(self):
        self.run_host(r'''
int i;
initialize();
for(i=0;i<4;i++) samples[i]=0;
func_150E71E4(0,0,vector,active);
if(error || active[1]!=-5 || active[2]!=3 || active[3]!=7) return 1;
for(i=4;i<8;i++) if(active[i]!=0) return 2;
if(sampleCalls!=4) return 3;
''')

    def test_callbacks_mutate_later_global_reads(self):
        self.run_host(r'''
initialize(); mutate=1;
func_150E71E4(1,2,vector,active);
if(error || active[0]!=-1 || active[4]!=3 || active[1]!=-9 || active[3]!=11 || active[5]!=40) return 1;
if(angleX!=3 || angleZ!=4 || vector[0]!=99 || vector[2]!=-99 || sampleCalls!=4) return 2;
''')

    def test_overlapping_input_is_not_reread_after_angle_call(self):
        self.run_host(r'''
initialize();
active[0]=3; active[1]=6; active[2]=4;
func_150E71E4(0,0,active,active);
if(error || angleX!=3 || angleZ!=4 || active[0]!=-1 || active[2]!=3) return 1;
if(active[1]!=-5 || output[0]!=-999 || output[9]!=-999 || sampleCalls!=4) return 2;
''')

    def test_independent_ido_slot_matches_without_guards(self):
        compiler = self.root / "ido/ido5.3_recomp/cc"
        if not compiler.is_file():
            self.skipTest("IDO compiler is unavailable")
        for tool in ("mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(tool) is None:
                self.skipTest(tool + " is unavailable")
        source,obj=self.path/"fixed.c",self.path/"fixed.o"
        globals_=("D_800A1324","D_800A1328","D_800A132C","D_800A1330",
                  "D_800A1334","D_800A1338","D_800A133C")
        source.write_text(self.types+"extern f32 "+",".join(globals_)+";\n"
            "f32 func_150ADA68(void); f32 func_150484A0(f32,f32);\n"+self.body+"\n")
        result=subprocess.run([str(compiler),"-c","-32","-G","0","-Xfullwarn",
            "-Xcpluscomm","-signed","-nostdinc","-non_shared","-Wab,-r4300_mul",
            "-mips2","-o32","-O2","-g3","-o",str(obj),str(source)],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(result.stdout+result.stderr,"")
        elf,binary,script=(self.path/("fixed"+suffix) for suffix in (".elf",".bin",".ld"))
        script.write_text("SECTIONS { .text 0x150E71E4 : SUBALIGN(4) { *(.text) } }\n")
        subprocess.run(["mips-linux-gnu-ld","-m","elf32btsmip","-T",str(script),
            "-e","func_150E71E4","--defsym=func_150ADA68=0x150ADA68",
            "--defsym=func_150484A0=0x150484A0",
            *("--defsym=%s=0x%s"%(name,name[2:]) for name in globals_),
            "-o",str(elf),str(obj)],check=True,capture_output=True,text=True)
        subprocess.run(["mips-linux-gnu-objcopy","-O","binary","-j",".text",str(elf),str(binary)],
                       check=True,capture_output=True,text=True)
        data=binary.read_bytes()
        retail=(self.root/"conker/conker.us.bin").read_bytes()[0x114694:0x114740]
        self.assertEqual(data[:172],retail)
        self.assertEqual(data[172:],bytes(len(data)-172))


if __name__ == "__main__":
    unittest.main()
