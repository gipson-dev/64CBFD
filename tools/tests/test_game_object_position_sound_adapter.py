import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests.test_game_row_destination_fill import START


class GameObjectPositionSoundAdapterTests(unittest.TestCase):
    TYPES = "typedef unsigned char u8; typedef unsigned short u16;\ntypedef short s16; typedef int s32; typedef float f32;\n"

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        game = (cls.root / "conker/src/game/generated_CBDB0.c").read_text()
        init = (cls.root / "conker/src/init_EB00.c").read_text()
        cls.game = re.search(r"s32 func_1509F6E8\([^\n]*\) \{\n.*?\n\}", game, re.S)
        cls.init = re.search(r"u16 func_10010F88\([^\n]*\) \{\n.*?\n\}", init, re.S)
        if cls.game is None or cls.init is None:
            raise AssertionError("recovered Game/Init sound adapter definitions missing")
        cls.game, cls.init = cls.game.group(0), cls.init.group(0)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def run_host(self, source):
        compiler = shutil.which("cc")
        if compiler is None:
            self.skipTest("host C compiler is unavailable")
        fixture = self.path / (self._testMethodName + ".c")
        binary = fixture.with_suffix("")
        fixture.write_text(self.TYPES + source + "\n" + START)
        result = subprocess.run([compiler, "-m32", "-O2", "-std=c99",
            "-fno-strict-aliasing", "-ffreestanding", "-nostdlib", "-static",
            "-fno-pie", "-no-pie", "-fno-stack-protector", "-Wall", "-Wextra",
            "-Werror", str(fixture), "-o", str(binary)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([str(binary)], capture_output=True, timeout=5)
        self.assertEqual(result.returncode, 0, "32-bit sound adapter fixture failed")

    def game_fixture(self):
        return r'''
static s32 lookupResult, lookupCalls, lookupArgument, soundCalls, soundResult;
static s32 received[10];
s32 func_1505EEF4(s32 index) {
    lookupCalls++;
    lookupArgument = index;
    return lookupResult;
}
s32 func_10010F88(s32 a, s32 b, s32 c, s32 d, s32 e,
                  s32 f, s32 g, s32 h, s32 i, s32 j) {
    soundCalls++;
    received[0]=a; received[1]=b; received[2]=c; received[3]=d; received[4]=e;
    received[5]=f; received[6]=g; received[7]=h; received[8]=i; received[9]=j;
    return soundResult;
}
''' + self.game + "\n"

    def test_failed_lookup_returns_zero_without_sound_submission(self):
        self.run_host(self.game_fixture() + r'''
int run(void) {
    lookupResult = 0;
    soundResult = 0xFFFF;
    if (func_1509F6E8(-1, 0x12345678, 0xFFFF, -2, -3) != 0) return 1;
    if (lookupCalls != 1 || lookupArgument != 0x12345678 || soundCalls != 0) return 2;
    return 0;
}
''')

    def test_coordinates_full_call_words_and_return_handle(self):
        self.run_host(self.game_fixture() + r'''
static u8 object[0x40] __attribute__((aligned(4)));
int run(void) {
    struct { f32 x,y,z; s32 ix,iy,iz; } cases[] = {
        {-0.0f,-1.9f,1.9f,0,-1,1},
        {125.75f,-64.75f,0.75f,125,-64,0},
        {32768.75f,-32769.75f,65535.5f,32768,-32769,65535},
        {2147483520.0f,-2147483648.0f,0.75f,2147483520,(-2147483647-1),0}
    };
    s32 results[] = {0,1,0x7FFF,0x8000,0xFFFF};
    s32 index, result;
    lookupResult = (s32)object;
    for (index = 0; index < 4; index++) {
        *(f32 *)(object+0x14)=cases[index].x;
        *(f32 *)(object+0x18)=cases[index].y;
        *(f32 *)(object+0x1C)=cases[index].z;
        for (result = 0; result < 5; result++) {
            soundResult = results[result];
            if (func_1509F6E8((s32)0xDEADBEEFu, -123, 0xFEDC,
                             (s32)0x87654321u, 0x12345678) != soundResult) return 1;
            if (lookupArgument != -123 || lookupCalls != index*5+result+1 ||
                soundCalls != lookupCalls) return 2;
            if (received[0] != (s32)0xDEADBEEFu || received[1] != 0xFEDC ||
                received[2] || received[3] || received[4]) return 3;
            if (received[5] != cases[index].ix || received[6] != cases[index].iy ||
                received[7] != cases[index].iz) return 4;
            if (received[8] != (s32)0x87654321u || received[9] != 0x12345678) return 5;
        }
    }
    return 0;
}
''')

    def test_init_return_contract_and_narrow_argument_forwarding(self):
        header = (self.root / "conker/include/functions.h").read_text()
        self.assertRegex(header, r"\bu16 func_10010F88\(")
        self.run_host(r'''
static s32 received[11], calls;
static u16 handle;
u16 func_10010E78(u16 a, s32 b, u16 c, s16 d, u8 e, s32 f,
                  s16 g, s16 h, s16 i, s16 j, s16 k) {
    calls++;
    received[0]=a; received[1]=b; received[2]=c; received[3]=d; received[4]=e;
    received[5]=f; received[6]=g; received[7]=h; received[8]=i; received[9]=j; received[10]=k;
    return handle;
}
''' + self.init + r'''
int run(void) {
    s32 results[] = {0,1,0x7FFF,0x8000,0xFFFF};
    s32 index;
    for (index = 0; index < 5; index++) {
        handle = results[index];
        if (func_10010F88(-123, 0xFEDC, -32768, 0xFE, (s32)0xDEADBEEFu,
                          32767, -32768, -1, 1234, -1234) != results[index]) return 1;
        if (calls != index+1 || received[0] || received[1] != -123 ||
            received[2] != 0xFEDC || received[3] != -32768 || received[4] != 0xFE ||
            received[5] != (s32)0xDEADBEEFu || received[6] != 32767 ||
            received[7] != -32768 || received[8] != -1 || received[9] != 1234 ||
            received[10] != -1234) return 2;
    }
    return 0;
}
''')

    def test_independent_game_and_init_slots_match_without_guards(self):
        compiler = self.root / "ido/ido5.3_recomp/cc"
        if not compiler.is_file():
            self.skipTest("IDO compiler is unavailable")
        for tool in ("mips-linux-gnu-ld", "mips-linux-gnu-objcopy"):
            if shutil.which(tool) is None:
                self.skipTest(tool + " is unavailable")
        image = (self.root / "conker/conker.us.bin").read_bytes()
        prototypes = "u16 func_10010E78(u16,s32,u16,s16,u8,s32,s16,s16,s16,s16,s16);\n"
        for name, body, prefix, address, offset, length, symbols in (
                ("func_1509F6E8", self.game, "s32 func_1505EEF4(); s32 func_10010F88();\n",
                 0x1509F6E8, 0xCCB98, 148,
                 ("func_1505EEF4=0x1505EEF4", "func_10010F88=0x10010F88")),
                ("func_10010F88", self.init, prototypes, 0x10010F88, 0x10F88, 116,
                 ("func_10010E78=0x10010E78",))):
            with self.subTest(function=name):
                source, obj = self.path / (name+".c"), self.path / (name+".o")
                source.write_text(self.TYPES + prefix + body + "\n")
                result = subprocess.run([str(compiler), "-c", "-32", "-G", "0",
                    "-Xfullwarn", "-Xcpluscomm", "-signed", "-nostdinc", "-non_shared",
                    "-Wab,-r4300_mul", "-mips2", "-o32", "-O2", "-g3",
                    "-o", str(obj), str(source)], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout + result.stderr, "")
                elf, binary, script = (self.path / (name+suffix) for suffix in (".elf", ".bin", ".ld"))
                script.write_text("SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n" % address)
                args = ["mips-linux-gnu-ld", "-m", "elf32btsmip", "-T", str(script), "-e", name]
                for symbol in symbols:
                    args.append("--defsym="+symbol)
                subprocess.run([*args, "-o", str(elf), str(obj)], check=True, capture_output=True, text=True)
                subprocess.run(["mips-linux-gnu-objcopy", "-O", "binary", "-j", ".text",
                    str(elf), str(binary)], check=True, capture_output=True, text=True)
                actual = binary.read_bytes()
                self.assertEqual(actual[:length], image[offset:offset+length])
                self.assertEqual(actual[length:], bytes(len(actual)-length))


if __name__ == "__main__":
    unittest.main()
