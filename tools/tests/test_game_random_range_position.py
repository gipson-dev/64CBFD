import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests.test_game_row_destination_fill import START


class GameRandomRangePositionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / "conker/src/game/generated_113D60.c").read_text()
        body = re.search(r"void func_150E6F18\(f32 \*output\) \{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("random range position definition missing")
        cls.body = body.group(0)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = "typedef unsigned int u32; typedef int s32; typedef float f32;\n"
        cls.fixture = cls.types + r'''
static f32 records[6][14], replacement[6], output[7];
f32 *D_80088A44[6];
static u32 randomWord;
static f32 fraction;
static int phase, randomCalls, fractionCalls, mutate;
s32 func_150ADA20(void) {
    if (phase != 0) phase = 99;
    else phase = 1;
    randomCalls++;
    return (s32)randomWord;
}
f32 func_150ADA68(void) {
    int index;
    if (phase != 1) phase = 99;
    else phase = 2;
    fractionCalls++;
    if (mutate) {
        f32 *selected = D_80088A44[randomWord % 6];
        selected[0]=100; selected[1]=-100; selected[2]=20;
        selected[3]=108; selected[4]=-84; selected[5]=52;
        for (index=0; index<6; index++) D_80088A44[index]=replacement;
    }
    return fraction;
}
static void initialize(void) {
    int index, field;
    for (index=0; index<6; index++) {
        D_80088A44[index] = &records[index][2];
        for (field=0; field<14; field++) records[index][field]=-999;
        records[index][2]=index*100-10; records[index][3]=index*100+20;
        records[index][4]=index*100-30; records[index][5]=index*100-2;
        records[index][6]=index*100+4; records[index][7]=index*100+2;
    }
    for (index=0; index<6; index++) replacement[index]=1000+index;
    for (index=0; index<7; index++) output[index]=-999;
    phase=randomCalls=fractionCalls=mutate=0;
}
''' + cls.body + "\n"

    def run_host(self, body):
        compiler = shutil.which("cc")
        if compiler is None:
            self.skipTest("host C compiler is unavailable")
        source = self.path / (self._testMethodName + ".c")
        binary = source.with_suffix("")
        source.write_text(self.fixture + "\nint run(void) {\n" + body + "\nreturn 0;\n}\n" + START)
        result = subprocess.run([compiler, "-m32", "-O2", "-std=c99", "-fno-strict-aliasing",
            "-ffreestanding", "-nostdlib", "-static", "-fno-pie", "-no-pie",
            "-fno-stack-protector", "-ffp-contract=off", "-Wall", "-Wextra", "-Werror",
            str(source), "-o", str(binary)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([str(binary)], capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, "32-bit random range fixture failed")

    def test_unsigned_selection_fraction_samples_and_output_sentinels(self):
        self.run_host(r'''
u32 words[] = {0,1,2,3,4,5,6,7,8,9,10,11,0x80000000u,0x80000001u,0xFFFFFFFEu,0xFFFFFFFFu};
int selected[] = {0,1,2,3,4,5,0,1,2,3,4,5,2,3,2,3};
f32 fractions[] = {-1,0,0.25f,0.5f,1,2};
int word, sample, field, record;
for (word=0; word<16; word++) {
    for (sample=0; sample<6; sample++) {
        f32 before[6][14];
        initialize(); randomWord=words[word]; fraction=fractions[sample];
        for (record=0; record<6; record++) for (field=0; field<14; field++)
            before[record][field]=records[record][field];
        func_150E6F18(output+2);
        if (phase!=2 || randomCalls!=1 || fractionCalls!=1) return 1;
        for (field=0; field<3; field++) {
            f32 *range=before[selected[word]]+2;
            f32 expected=range[field]+(range[field+3]-range[field])*fraction;
            if (output[field+2]!=expected) return 2;
        }
        if (output[0]!=-999 || output[1]!=-999 || output[5]!=-999 || output[6]!=-999) return 3;
        for (record=0; record<6; record++) for (field=0; field<14; field++)
            if (records[record][field]!=before[record][field]) return 4;
    }
}
''')

    def test_selected_pointer_is_captured_but_fields_are_read_after_fraction_call(self):
        self.run_host(r'''
initialize(); randomWord=4; fraction=0.25f; mutate=1;
func_150E6F18(output+2);
if (phase!=2 || randomCalls!=1 || fractionCalls!=1) return 1;
if (output[2]!=102 || output[3]!=-96 || output[4]!=28) return 2;
if (D_80088A44[4]!=replacement || records[4][2]!=100) return 3;
''')

    def test_overlapping_output_preserves_sequential_axis_access(self):
        self.run_host(r'''
int selected, shift, field, axis;
for (selected=0; selected<6; selected++) {
    for (shift=-1; shift<=5; shift++) {
        f32 expected[14];
        initialize(); randomWord=selected; fraction=0.5f;
        for (field=0; field<14; field++) expected[field]=records[selected][field];
        for (axis=0; axis<3; axis++)
            expected[2+shift+axis]=expected[2+axis]+(expected[5+axis]-expected[2+axis])*fraction;
        func_150E6F18(records[selected]+2+shift);
        for (field=0; field<14; field++) if (records[selected][field]!=expected[field]) return 1;
        if (phase!=2 || randomCalls!=1 || fractionCalls!=1) return 2;
    }
}
''')

    def test_independent_ido_slot_matches_without_guards(self):
        compiler = self.root / "ido/ido5.3_recomp/cc"
        if not compiler.is_file():
            self.skipTest("IDO compiler is unavailable")
        for tool in ("mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(tool) is None:
                self.skipTest(tool + " is unavailable")
        source, obj = self.path / "range.c", self.path / "range.o"
        source.write_text(self.types + "extern f32 *D_80088A44[6];\n"
            "s32 func_150ADA20(void); f32 func_150ADA68(void);\n" + self.body + "\n")
        result = subprocess.run([str(compiler), "-c", "-32", "-G", "0", "-Xfullwarn",
            "-Xcpluscomm", "-signed", "-nostdinc", "-non_shared", "-Wab,-r4300_mul",
            "-mips2", "-o32", "-O2", "-g3", "-o", str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, "")
        elf, binary, script = (self.path / ("range"+suffix) for suffix in (".elf", ".bin", ".ld"))
        script.write_text("SECTIONS { .text 0x150E6F18 : SUBALIGN(4) { *(.text) } }\n")
        subprocess.run(["mips-linux-gnu-ld", "-m", "elf32btsmip", "-T", str(script),
            "-e", "func_150E6F18", "--defsym=D_80088A44=0x80088A44",
            "--defsym=func_150ADA20=0x150ADA20", "--defsym=func_150ADA68=0x150ADA68",
            "-o", str(elf), str(obj)], check=True, capture_output=True, text=True)
        subprocess.run(["mips-linux-gnu-objcopy", "-O", "binary", "-j", ".text",
            str(elf), str(binary)], check=True, capture_output=True, text=True)
        actual = binary.read_bytes()
        reference = (self.root / "conker/conker.us.bin").read_bytes()[0x1143C8:0x11445C]
        self.assertEqual(actual[:148], reference)
        self.assertEqual(actual[148:], bytes(len(actual)-148))


if __name__ == "__main__":
    unittest.main()
