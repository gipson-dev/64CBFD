import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests.test_game_row_destination_fill import START


class GameLinkedRecordPositionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / "conker/src/game/generated_113D60.c").read_text()
        match = re.search(r"void func_150E6FAC\(f32 \*output, u8 \*actor\) \{\n.*?\n\}", source, re.S)
        if match is None:
            raise AssertionError("linked record position definition missing")
        cls.body = match.group(0)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = "typedef unsigned char u8; typedef short s16; typedef int s32; typedef float f32;\n"
        cls.fixture = cls.types + r'''
static union { unsigned int align; u8 bytes[0x300]; } actorStorage;
static union { unsigned int align; u8 bytes[0x20]; } nodeStorage;
static f32 record[20], replacement[20], output[5];
static s32 found, randomWord;
static f32 fraction;
static int phase, lookupCalls, floatCalls, randomCalls, trigCalls, mutate;
static u8 angles[2];
s32 func_1514ECE0(void *node, s16 key, void **result) {
    lookupCalls++;
    if (phase != 0 || node != (void *)0x12345678 || key != 0x16) phase=99;
    else phase=1;
    if (found) *result=nodeStorage.bytes;
    return found;
}
f32 func_150ADA68(void) {
    floatCalls++;
    if (phase != 1) phase=99; else phase=2;
    return fraction;
}
s32 func_150ADA20(void) {
    randomCalls++;
    if (phase != 2) phase=99; else phase=3;
    return randomWord;
}
f32 func_151423D8(u8 angle) {
    if (trigCalls >= 2) { phase=99; return 0; }
    angles[trigCalls]=angle;
    if (phase != 3+trigCalls) phase=99; else phase++;
    trigCalls++;
    if (mutate && trigCalls==2) {
        *(f32 *)(actorStorage.bytes+0x14)=50;
        replacement[14]=1; replacement[15]=2; replacement[16]=3;
        *(void **)(nodeStorage.bytes+0x10)=replacement;
    }
    return trigCalls==1 ? 0.5f : -0.25f;
}
static void initialize(void) {
    int i;
    for (i=0;i<0x300;i++) actorStorage.bytes[i]=0;
    for (i=0;i<20;i++) record[i]=replacement[i]=0;
    *(void **)(actorStorage.bytes+0x2F4)=(void *)0x12345678;
    *(void **)(nodeStorage.bytes+0x10)=record;
    *(f32 *)(actorStorage.bytes+0x14)=10;
    *(f32 *)(actorStorage.bytes+0x18)=20;
    *(f32 *)(actorStorage.bytes+0x1C)=30;
    record[14]=0.25f; record[15]=-0.5f; record[16]=1;
    for(i=0;i<5;i++) output[i]=-999;
    phase=lookupCalls=floatCalls=randomCalls=trigCalls=mutate=0;
    found=1; fraction=0.5f; randomWord=0;
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
            str(source), "-o", str(binary)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([str(binary)], capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, "linked record fixture failed")

    def test_failed_lookup_copies_coordinates_without_rng(self):
        self.run_host(r'''
initialize(); found=0;
func_150E6FAC(output+1, actorStorage.bytes);
if(output[1]!=10 || output[2]!=20 || output[3]!=30) return 1;
if(output[0]!=-999 || output[4]!=-999) return 2;
if(phase!=1 || lookupCalls!=1 || floatCalls || randomCalls || trigCalls) return 3;
''')

    def test_radius_angles_call_order_and_output_sentinels(self):
        self.run_host(r'''
static s32 words[]={0,63,64,255,256,-1,(s32)0x80000040};
static f32 fractions[]={-1,0,0.5f,1,2};
int i,j;
for(i=0;i<7;i++) for(j=0;j<5;j++) {
    f32 radius;
    initialize(); randomWord=words[i]; fraction=fractions[j];
    radius=fraction*100+80;
    func_150E6FAC(output+1, actorStorage.bytes);
    if(output[1]!=-10+0.5f*radius || output[2]!=160 || output[3]!=-50-0.25f*radius) return 1;
    if(angles[0]!=(u8)((words[i]&255)-64) || angles[1]!=(u8)words[i]) return 2;
    if(phase!=5 || lookupCalls!=1 || floatCalls!=1 || randomCalls!=1 || trigCalls!=2) return 3;
    if(output[0]!=-999 || output[4]!=-999) return 4;
}
''')

    def test_record_pointer_and_coordinates_are_read_after_callbacks(self):
        self.run_host(r'''
initialize(); mutate=1;
func_150E6FAC(output+1, actorStorage.bytes);
if(output[1]!=35 || output[2]!=-40 || output[3]!=-242.5f) return 1;
if(phase!=5 || trigCalls!=2) return 2;
''')

    def test_overlapping_output_preserves_sequential_reads(self):
        self.run_host(r'''
initialize(); found=0;
func_150E6FAC((f32 *)(actorStorage.bytes+0x18), actorStorage.bytes);
if(*(f32 *)(actorStorage.bytes+0x18)!=10 || *(f32 *)(actorStorage.bytes+0x1C)!=10
   || *(f32 *)(actorStorage.bytes+0x20)!=10) return 1;
initialize();
func_150E6FAC(record+15, actorStorage.bytes);
if(record[15]!=55 || record[16]!=-4280 || record[17]!=342397.5f) return 2;
if(phase!=5) return 3;
''')

    def test_independent_ido_body_fits_retail_slot(self):
        compiler = self.root / "ido/ido5.3_recomp/cc"
        if not compiler.is_file():
            self.skipTest("IDO compiler is unavailable")
        for tool in ("mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(tool) is None:
                self.skipTest(tool + " is unavailable")
        source, obj = self.path / "position.c", self.path / "position.o"
        source.write_text(self.types + "s32 func_150ADA20(void); f32 func_150ADA68(void);\n"
            "f32 func_151423D8(u8); s32 func_1514ECE0(void *,s16,void **);\n" + self.body + "\n")
        result = subprocess.run([str(compiler), "-c", "-32", "-G", "0", "-Xfullwarn",
            "-Xcpluscomm", "-signed", "-nostdinc", "-non_shared", "-Wab,-r4300_mul",
            "-mips2", "-o32", "-O2", "-g3", "-o", str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, "")
        elf, binary, script = (self.path / ("position"+suffix) for suffix in (".elf", ".bin", ".ld"))
        script.write_text("SECTIONS { .text 0x150E6FAC : SUBALIGN(4) { *(.text) } }\n")
        subprocess.run(["mips-linux-gnu-ld", "-m", "elf32btsmip", "-T", str(script),
            "-e", "func_150E6FAC", "--defsym=func_150ADA20=0x150ADA20",
            "--defsym=func_150ADA68=0x150ADA68", "--defsym=func_151423D8=0x151423D8",
            "--defsym=func_1514ECE0=0x1514ECE0", "-o", str(elf), str(obj)],
            check=True, capture_output=True, text=True)
        subprocess.run(["mips-linux-gnu-objcopy", "-O", "binary", "-j", ".text",
            str(elf), str(binary)], check=True, capture_output=True, text=True)
        data = binary.read_bytes()
        words = list(struct.unpack(">" + "I"*(len(data)//4), data))
        end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        self.assertLessEqual(end, 72)
        self.assertEqual(words[0], 0x27BDFFC8)
        calls = [word for word in words[:end] if word >> 26 == 3]
        self.assertEqual(calls, [(3 << 26) | ((address >> 2) & 0x3FFFFFF)
            for address in (0x1514ECE0, 0x150ADA68, 0x150ADA20, 0x151423D8, 0x151423D8)])
        self.assertEqual(data[end*4:], bytes(len(data)-end*4))


if __name__ == "__main__":
    unittest.main()
