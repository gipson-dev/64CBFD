import ctypes
import random
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class Record(ctypes.Structure):
    _fields_ = [
        ("pad0", ctypes.c_uint8 * 0x1A), ("counter", ctypes.c_int16),
        ("pad1", ctypes.c_uint8 * 0xF), ("firstOutput", ctypes.c_uint8),
        ("secondOutput", ctypes.c_uint8), ("pad2", ctypes.c_uint8 * 0xB),
        ("firstValue", ctypes.c_float), ("secondValue", ctypes.c_float),
        ("pad3", ctypes.c_uint8 * 0x68), ("parameters", ctypes.c_int16 * 6),
    ]


class GameThresholdUpdateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("cc")
        if compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_1D0840.c").read_text()
        record = re.search(r"typedef struct \{\n    u8 pad0\[0x1A\];.*?\n\} UpdateRecord1D0840;",
                           source, re.S)
        body = re.search(r"s32 func_151A4900\(UpdateRecord1D0840 \*arg0, s32 arg1\) \{\n.*?\n\}",
                         source, re.S)
        if record is None or body is None:
            raise AssertionError("threshold update source was not found")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        directory = Path(cls.directory.name)
        fixture = directory / "threshold.c"
        fixture.write_text(
            "#include <stdint.h>\n#include <stddef.h>\n"
            "typedef uint8_t u8; typedef int16_t s16; typedef int32_t s32;\n"
            "typedef uint32_t u32; typedef float f32; s32 D_800BE9E4;\n" +
            record.group(0) + "\n" + body.group(0) + "\n" +
            "size_t recordOffset(int field) {\n"
            "switch (field) {\n"
            "case 0: return offsetof(UpdateRecord1D0840, counter);\n"
            "case 1: return offsetof(UpdateRecord1D0840, firstOutput);\n"
            "case 2: return offsetof(UpdateRecord1D0840, secondOutput);\n"
            "case 3: return offsetof(UpdateRecord1D0840, firstValue);\n"
            "case 4: return offsetof(UpdateRecord1D0840, secondValue);\n"
            "case 5: return offsetof(UpdateRecord1D0840, parameters);\n"
            "default: return sizeof(UpdateRecord1D0840); } }\n"
        )
        library = directory / "threshold.so"
        subprocess.run([compiler, "-shared", "-fPIC", "-O2", "-std=c99",
                        str(fixture), "-o", str(library)],
                       check=True, capture_output=True, text=True)
        cls.library = ctypes.CDLL(str(library))
        cls.update = cls.library.func_151A4900
        cls.update.argtypes = [ctypes.POINTER(Record), ctypes.c_int32]
        cls.update.restype = ctypes.c_int32
        cls.offset = cls.library.recordOffset
        cls.offset.argtypes = [ctypes.c_int]
        cls.offset.restype = ctypes.c_size_t

    def check_case(self, counter, first_limit=10, second_limit=10,
                   first_scale=3, second_scale=7, increment_scale=2,
                   global_scale=4, argument=0):
        actual = Record()
        ctypes.memset(ctypes.byref(actual), 0xA5, ctypes.sizeof(actual))
        actual.counter = counter
        actual.firstValue = 1.25
        actual.secondValue = -10.5
        actual.parameters[:] = (123, second_scale, first_limit, first_scale,
                                second_limit, increment_scale)
        expected = Record.from_buffer_copy(actual)
        if counter < first_limit:
            expected.firstOutput = (counter * first_scale) & 0xFF
        if counter < second_limit:
            product = ctypes.c_int32(increment_scale * global_scale).value
            increment = ctypes.c_float(product).value
            expected.firstValue = ctypes.c_float(expected.firstValue + increment).value
            expected.secondValue = ctypes.c_float(expected.secondValue + increment).value
        expected.secondOutput = (counter * second_scale) & 0xFF
        ctypes.c_int32.in_dll(self.library, "D_800BE9E4").value = global_scale
        self.assertEqual(self.update(ctypes.byref(actual), argument), 1)
        self.assertEqual(bytes(actual), bytes(expected))

    def test_actual_c_layout_matches_guest_offsets(self):
        offsets = (0x1A, 0x2B, 0x2C, 0x38, 0x3C, 0xA8, 0xB4)
        self.assertEqual(tuple(self.offset(i) for i in range(7)), offsets)
        self.assertEqual(ctypes.sizeof(Record), 0xB4)

    def test_strict_threshold_boundaries(self):
        for counter in (9, 10, 11):
            with self.subTest(counter=counter):
                self.check_case(counter)

    def test_thresholds_are_independent(self):
        for first_limit, second_limit in ((0, 20), (20, 0), (0, 0), (20, 20)):
            with self.subTest(first_limit=first_limit, second_limit=second_limit):
                self.check_case(10, first_limit=first_limit, second_limit=second_limit)

    def test_signed_counters_and_negative_scales(self):
        for counter in (-32768, -5, -1, 0, 32767):
            with self.subTest(counter=counter):
                self.check_case(counter, first_limit=-1, second_limit=1,
                                first_scale=-32768, second_scale=-7,
                                increment_scale=-3, global_scale=9)

    def test_integer_product_wraps_before_signed_float_conversion(self):
        for scale in (0x7FFFFFFF, -0x80000000, -0x7FFFFFFF):
            with self.subTest(scale=scale):
                self.check_case(1, increment_scale=3, global_scale=scale)

    def test_second_argument_is_ignored(self):
        for argument in (0, 1, -1, -0x80000000, 0x7FFFFFFF):
            with self.subTest(argument=argument):
                self.check_case(2, argument=argument)

    def test_deterministic_signed_parameter_sweep(self):
        rng = random.Random(0x151A4900)
        for case in range(256):
            values = [rng.randint(-32768, 32767) for _ in range(6)]
            with self.subTest(case=case):
                self.check_case(*values, global_scale=rng.randint(-0x80000000, 0x7FFFFFFF))


if __name__ == "__main__":
    unittest.main()
