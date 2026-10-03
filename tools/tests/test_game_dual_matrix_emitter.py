import ctypes
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


def sdk_macro(source, name):
    lines = source.splitlines()
    for index, line in enumerate(lines):
        if re.match(r"\s*#\s*define\s+" + re.escape(name) + r"(?:\s|\()", line):
            result = [line]
            while result[-1].rstrip().endswith("\\"):
                index += 1
                result.append(lines[index])
            return "\n".join(result) + "\n"
    raise AssertionError("SDK macro was not found: " + name)


class Gfx(ctypes.Structure):
    _fields_ = [("w0", ctypes.c_uint32), ("w1", ctypes.c_uint32)]


class GameDualMatrixEmitterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("cc")
        if compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        root = Path(__file__).resolve().parents[2]
        source = (root / "conker/src/game/generated_183640.c").read_text()
        match = re.search(r"Gfx \*func_15157FE8\([^\n]*\) \{\n.*?\n\}", source, re.S)
        if match is None:
            raise AssertionError("dual matrix emitter definition was not found")
        gbi = (root / "conker/include/2.0L/PR/gbi.h").read_text()
        mbi = (root / "conker/include/2.0L/PR/mbi.h").read_text()
        macros = sdk_macro(mbi, "_SHIFTL")
        for name in ("G_MTX", "G_MTX_PROJECTION", "G_MTX_LOAD", "G_MTX_MUL",
                     "G_MTX_NOPUSH", "G_MTX_PUSH", "gDma2p", "gSPMatrix"):
            macros += sdk_macro(gbi, name)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        directory = Path(cls.directory.name)
        fixture = directory / "matrix.c"
        fixture.write_text(
            "#include <stdint.h>\n"
            "typedef uint32_t u32; typedef uint8_t u8; typedef int32_t s32;\n"
            "typedef struct { struct { u32 w0, w1; } words; } Gfx;\n"
            "typedef struct { u8 bytes[64]; } Mtx;\n"
            "u8 D_800BE9C0; u8 *D_800BE628; u8 *D_800DC2A0[2];\n" +
            macros + match.group(0) + "\n"
        )
        library = directory / "matrix.so"
        subprocess.run(
            [compiler, "-shared", "-fPIC", "-O2", "-std=c99",
             str(fixture), "-o", str(library)],
            check=True, capture_output=True, text=True,
        )
        cls.library = ctypes.CDLL(str(library))
        cls.emit = cls.library.func_15157FE8
        cls.emit.argtypes = [ctypes.POINTER(Gfx), ctypes.c_int32,
                             ctypes.c_int32, ctypes.c_int32]
        cls.emit.restype = ctypes.POINTER(Gfx)

    def checkEmission(self, record, page, unused1=0, unused3=0):
        records = (ctypes.c_uint8 * (8 * 0x180))()
        matrices = [(ctypes.c_uint8 * (8 * 0x40))() for _ in range(2)]
        ctypes.c_void_p.in_dll(self.library, "D_800BE628").value = ctypes.addressof(records)
        ctypes.c_uint8.in_dll(self.library, "D_800BE9C0").value = page
        table = (ctypes.c_void_p * 2).in_dll(self.library, "D_800DC2A0")
        for index, matrix in enumerate(matrices):
            table[index] = ctypes.addressof(matrix)
        commands = (Gfx * 5)(*[Gfx(0x12345678, 0xABCDEF12) for _ in range(5)])
        start = ctypes.cast(ctypes.byref(commands, 8), ctypes.POINTER(Gfx))
        result = self.emit(start, unused1, record, unused3)
        self.assertEqual(ctypes.addressof(result.contents), ctypes.addressof(commands) + 24)
        self.assertEqual(commands[1].w0, 0xDA380007)
        self.assertEqual(commands[1].w1,
                         (ctypes.addressof(records) + record * 0x180 + page * 0x40 + 0x100) & 0xFFFFFFFF)
        self.assertEqual(commands[2].w0, 0xDA380005)
        self.assertEqual(commands[2].w1,
                         (ctypes.addressof(matrices[page]) + record * 0x40) & 0xFFFFFFFF)
        for index in (0, 3, 4):
            self.assertEqual((commands[index].w0, commands[index].w1),
                             (0x12345678, 0xABCDEF12))

    def test_first_record_first_page(self):
        self.checkEmission(0, 0)

    def test_indexed_record_second_page(self):
        self.checkEmission(3, 1)

    def test_unused_arguments_do_not_change_commands(self):
        self.checkEmission(7, 0, -123, 456)
        self.checkEmission(7, 1, 789, -987)


if __name__ == "__main__":
    unittest.main()
