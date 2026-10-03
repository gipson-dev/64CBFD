import ctypes
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class Vector(ctypes.Structure):
    _fields_ = [("x", ctypes.c_float), ("y", ctypes.c_float), ("z", ctypes.c_float)]


class GameVectorNormalizerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("cc")
        if compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game_16EE20.c").read_text()
        match = re.search(r"s32 func_15145128\([^\n]*\) \{\n.*?\n\}", source, re.S)
        if match is None:
            raise AssertionError("vector normalizer definition was not found")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        directory = Path(cls.directory.name)
        fixture = directory / "normalizer.c"
        fixture.write_text(
            "#include <math.h>\n#include <stddef.h>\n"
            "typedef float f32;\ntypedef int s32;\n"
            "typedef struct { f32 unk0, unk4, unk8; } struct17;\n" +
            match.group(0) + "\n"
        )
        library = directory / "normalizer.so"
        subprocess.run(
            [compiler, "-shared", "-fPIC", "-O2", "-std=c99",
             "-fno-fast-math", "-ffp-contract=off", str(fixture),
             "-o", str(library), "-lm"],
            check=True, capture_output=True, text=True,
        )
        cls.library = ctypes.CDLL(str(library))
        cls.normalize = cls.library.func_15145128
        cls.normalize.argtypes = [ctypes.POINTER(Vector), ctypes.POINTER(Vector),
                                  ctypes.POINTER(ctypes.c_float),
                                  ctypes.POINTER(ctypes.c_float)]
        cls.normalize.restype = ctypes.c_int

    def assertVector(self, vector, expected):
        for actual, value in zip((vector.x, vector.y, vector.z), expected):
            self.assertAlmostEqual(actual, value, places=6)

    def test_length_and_reciprocal_outputs(self):
        source, result = Vector(3, 4, 0), Vector()
        length, reciprocal = ctypes.c_float(), ctypes.c_float()
        self.assertEqual(self.normalize(ctypes.byref(source), ctypes.byref(result),
                         ctypes.byref(length), ctypes.byref(reciprocal)), 1)
        self.assertVector(result, (0.6, 0.8, 0))
        self.assertEqual(length.value, 5)
        self.assertAlmostEqual(reciprocal.value, 0.2, places=6)

    def test_zero_vector_preserves_all_outputs(self):
        source, result = Vector(), Vector(7, 8, 9)
        length, reciprocal = ctypes.c_float(11), ctypes.c_float(12)
        self.assertEqual(self.normalize(ctypes.byref(source), ctypes.byref(result),
                         ctypes.byref(length), ctypes.byref(reciprocal)), 0)
        self.assertVector(result, (7, 8, 9))
        self.assertEqual((length.value, reciprocal.value), (11, 12))

    def test_both_optional_outputs_omitted(self):
        source, result = Vector(-3, 0, 4), Vector()
        self.assertEqual(self.normalize(ctypes.byref(source), ctypes.byref(result),
                                        None, None), 1)
        self.assertVector(result, (-0.6, 0, 0.8))

    def test_length_only(self):
        source, result, length = Vector(0, 0, 2), Vector(), ctypes.c_float()
        self.assertEqual(self.normalize(ctypes.byref(source), ctypes.byref(result),
                                        ctypes.byref(length), None), 1)
        self.assertEqual(length.value, 2)
        self.assertVector(result, (0, 0, 1))

    def test_reciprocal_only(self):
        source, result, reciprocal = Vector(0, -2, 0), Vector(), ctypes.c_float()
        self.assertEqual(self.normalize(ctypes.byref(source), ctypes.byref(result),
                                        None, ctypes.byref(reciprocal)), 1)
        self.assertAlmostEqual(reciprocal.value, 0.5, places=6)
        self.assertVector(result, (0, -1, 0))

    def test_in_place_normalization(self):
        vector = Vector(3, 4, 0)
        self.assertEqual(self.normalize(ctypes.byref(vector), ctypes.byref(vector),
                                        None, None), 1)
        self.assertVector(vector, (0.6, 0.8, 0))

    def test_length_and_reciprocal_share_output(self):
        source, result, shared = Vector(3, 4, 0), Vector(), ctypes.c_float()
        self.assertEqual(self.normalize(ctypes.byref(source), ctypes.byref(result),
                                        ctypes.byref(shared), ctypes.byref(shared)), 1)
        self.assertAlmostEqual(shared.value, 0.2, places=6)
        self.assertVector(result, (0.6, 0.8, 0))

    def test_length_output_aliases_input_x(self):
        source, result = Vector(3, 4, 0), Vector()
        length = ctypes.cast(ctypes.byref(source), ctypes.POINTER(ctypes.c_float))
        self.assertEqual(self.normalize(ctypes.byref(source), ctypes.byref(result),
                                        length, None), 1)
        self.assertEqual(source.x, 5)
        self.assertVector(result, (1, 0.8, 0))

    def test_reciprocal_output_aliases_input_x(self):
        source, result = Vector(3, 4, 0), Vector()
        reciprocal = ctypes.cast(ctypes.byref(source), ctypes.POINTER(ctypes.c_float))
        self.assertEqual(self.normalize(ctypes.byref(source), ctypes.byref(result),
                                        None, reciprocal), 1)
        self.assertVector(result, (0.04, 0.8, 0))


if __name__ == "__main__":
    unittest.main()
