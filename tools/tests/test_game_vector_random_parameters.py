import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests.test_game_row_destination_fill import START


class GameVectorRandomParameterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / "conker/src/game/generated_113D60.c").read_text()
        match = re.search(r"void func_150E70EC\(s32 arg0, s32 arg1, f32 \*vector, f32 \*output\) \{\n.*?\n\}", source, re.S)
        if match is None:
            raise AssertionError("vector random parameter definition missing")
        cls.body = match.group(0)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = "typedef int s32; typedef float f32;\n"
        cls.fixture = cls.types + r'''
f32 D_800A1310, D_800A1314, D_800A1318, D_800A131C, D_800A1320;
static f32 vector[3], output[10], samples[6], *active, angular[2][2], sqrtInput;
static int angleCalls, sampleCalls, sqrtCalls, error, mutate;
static f32 root(f32 value) {
    f32 result;
    __asm__("fsqrt" : "=t"(result) : "0"(value));
    return result;
}
f32 sqrtf(f32 value) { sqrtCalls++; sqrtInput=value; return root(value); }
f32 func_150484A0(f32 x, f32 y) {
    if(angleCalls>=2) { error=1; return 0; }
    if(sampleCalls!=(angleCalls ? 3 : 0)) error=2;
    angular[angleCalls][0]=x; angular[angleCalls][1]=y;
    angleCalls++;
    return angleCalls==1 ? x+y : x-y;
}
f32 func_150ADA68(void) {
    int index=sampleCalls;
    if(index>=6) { error=3; return 0; }
    if(angleCalls!=(index<3 ? 1 : 2)) error=4;
    if(index==0 && active[0]!=angular[0][0]+angular[0][1]) error=5;
    if(index==1 && active[2]!=samples[0]*D_800A1310) error=6;
    if(index==2 && active[4]!=samples[1]*D_800A1314) error=7;
    if(index==3 && active[1]!=angular[1][0]-angular[1][1]-D_800A1318) error=8;
    if(index==4 && active[3]!=samples[3]*D_800A131C) error=9;
    if(index==5 && active[5]!=samples[4]*D_800A1320) error=10;
    if(mutate && index==0) D_800A1310=10;
    if(mutate && index==2) {
        vector[0]=6; vector[1]=2; vector[2]=8;
        D_800A1318=3;
    }
    sampleCalls++;
    return samples[index];
}
static void initialize(void) {
    int i;
    vector[0]=3; vector[1]=6; vector[2]=4;
    for(i=0;i<10;i++) output[i]=-999;
    samples[0]=0.25f; samples[1]=0.5f; samples[2]=0.75f;
    samples[3]=-1; samples[4]=2; samples[5]=3;
    D_800A1310=2; D_800A1314=4; D_800A1318=1;
    D_800A131C=8; D_800A1320=16;
    angleCalls=sampleCalls=sqrtCalls=error=mutate=0;
    active=output+1;
}
''' + cls.body + "\n"

    def run_host(self, body):
        compiler = shutil.which("cc")
        if compiler is None:
            self.skipTest("host compiler is unavailable")
        source = self.path / (self._testMethodName + ".c")
        binary = source.with_suffix("")
        source.write_text(self.fixture + "int run(void) {\n" + body + "\nreturn 0;\n}\n" + START)
        result = subprocess.run([compiler, "-m32", "-O2", "-std=c99", "-fno-strict-aliasing",
            "-ffreestanding", "-nostdlib", "-static", "-fno-pie", "-no-pie",
            "-fno-stack-protector", "-ffp-contract=off", "-Wall", "-Wextra", "-Werror",
            "-Wno-unused-parameter", str(source), "-o", str(binary)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([str(binary)], capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, "vector random parameter fixture failed")

    def test_eight_outputs_six_samples_and_publication_order(self):
        self.run_host(r'''
initialize();
func_150E70EC(-1, (s32)0x80000000, vector, active);
if(error || angleCalls!=2 || sampleCalls!=6 || sqrtCalls!=1) return 1;
if(active[0]!=7 || active[1]!=-2 || active[2]!=0.5f || active[3]!=-8
   || active[4]!=2 || active[5]!=32 || active[6]!=0.375f || active[7]!=1.5f) return 2;
if(output[0]!=-999 || output[9]!=-999 || sqrtInput!=25) return 3;
if(vector[0]!=3 || vector[1]!=6 || vector[2]!=4) return 4;
''')

    def test_zero_vector_and_zero_samples(self):
        self.run_host(r'''
int i;
initialize();
for(i=0;i<3;i++) vector[i]=0;
for(i=0;i<6;i++) samples[i]=0;
func_150E70EC(0,0,vector,active);
for(i=0;i<8;i++) if(active[i]!=(i==1 ? -1 : 0)) return 1;
if(error || sqrtInput!=0 || sampleCalls!=6) return 2;
''')

    def test_callback_changes_are_read_at_the_original_time(self):
        self.run_host(r'''
initialize(); mutate=1;
func_150E70EC(123,456,vector,active);
if(error || active[2]!=2.5f || active[1]!=5 || sqrtInput!=100) return 1;
if(angular[0][0]!=3 || angular[0][1]!=4 || angular[1][0]!=10 || angular[1][1]!=2) return 2;
''')

    def test_overlapping_vector_reads_follow_first_output_stores(self):
        self.run_host(r'''
volatile f32 expected=root(49.25f);
expected=expected-6;
expected=expected-1;
initialize();
output[1]=3; output[2]=6; output[3]=4;
func_150E70EC(0,0,active,active);
if(error || sqrtInput!=49.25f || angular[1][1]!=6) return 1;
if(active[1]!=expected || active[0]!=7 || active[2]!=0.5f) return 2;
if(output[0]!=-999 || output[9]!=-999 || sampleCalls!=6) return 3;
''')

    def test_independent_ido_slot_matches_without_guards(self):
        compiler = self.root / "ido/ido5.3_recomp/cc"
        if not compiler.is_file():
            self.skipTest("IDO compiler is unavailable")
        for tool in ("mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(tool) is None:
                self.skipTest(tool + " is unavailable")
        source, obj = self.path / "parameters.c", self.path / "parameters.o"
        source.write_text(self.types + "extern f32 D_800A1310,D_800A1314,D_800A1318,D_800A131C,D_800A1320;\n"
            "f32 func_150ADA68(void); f32 func_150484A0(f32,f32); f32 sqrtf(f32);\n"
            "#pragma intrinsic(sqrtf)\n" + self.body + "\n")
        result = subprocess.run([str(compiler), "-c", "-32", "-G", "0", "-Xfullwarn",
            "-Xcpluscomm", "-signed", "-nostdinc", "-non_shared", "-Wab,-r4300_mul",
            "-mips2", "-o32", "-O2", "-g3", "-o", str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, "")
        elf, binary, script = (self.path / ("parameters"+suffix) for suffix in (".elf", ".bin", ".ld"))
        script.write_text("SECTIONS { .text 0x150E70EC : SUBALIGN(4) { *(.text) } }\n")
        globals_ = ("D_800A1310", "D_800A1314", "D_800A1318", "D_800A131C", "D_800A1320")
        subprocess.run(["mips-linux-gnu-ld", "-m", "elf32btsmip", "-T", str(script),
            "-e", "func_150E70EC", "--defsym=func_150ADA68=0x150ADA68",
            "--defsym=func_150484A0=0x150484A0",
            *("--defsym=%s=0x%s" % (name,name[2:]) for name in globals_),
            "-o", str(elf), str(obj)], check=True, capture_output=True, text=True)
        subprocess.run(["mips-linux-gnu-objcopy", "-O", "binary", "-j", ".text",
            str(elf), str(binary)], check=True, capture_output=True, text=True)
        data = binary.read_bytes()
        retail = (self.root / "conker/conker.us.bin").read_bytes()[0x11459C:0x114694]
        self.assertEqual(data[:248], retail)
        self.assertEqual(data[248:], bytes(len(data)-248))


if __name__ == "__main__":
    unittest.main()
