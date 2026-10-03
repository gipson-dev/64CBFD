import ctypes
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class Destination(ctypes.Structure):
    _fields_ = [("prefix", ctypes.c_uint8 * 14), ("x", ctypes.c_int16),
                ("y", ctypes.c_int16), ("z", ctypes.c_int16),
                ("suffix", ctypes.c_uint8 * 4)]


class Record(ctypes.Structure):
    _fields_ = [("destination", ctypes.POINTER(Destination)),
                ("x", ctypes.POINTER(ctypes.c_float)),
                ("y", ctypes.POINTER(ctypes.c_float)),
                ("z", ctypes.c_ssize_t), ("selector", ctypes.c_int8)]


class GamePositionPublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("cc")
        if compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game_18D770.c").read_text()
        match = re.search(r"s32 func_15163504\(struct225 \*arg0\) \{\n.*?\n\}", source, re.S)
        if match is None:
            raise AssertionError("position publication definition was not found")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        directory = Path(cls.directory.name)
        fixture = directory / "publication.c"
        # Host-native pointer fields model the guest payload, not its byte layout.
        fixture.write_text("#include <stdint.h>\n" + r"""
typedef uint8_t u8; typedef int8_t s8; typedef int16_t s16;
typedef int32_t s32; typedef float f32;
typedef struct {
    u8 prefix[14]; s16 unkE, unk10, unk12; u8 suffix[4];
} struct226;
typedef struct {
    struct226 *unk14; f32 *unk18, *unk1C; intptr_t unk20; s8 unk24;
} struct225;
struct226 *currentDestination;
s32 callbackCalls, callbackSlot, callbackResult, mutate, observed[3];
static s32 callback(s32 slot) {
    callbackCalls++;
    callbackSlot = slot;
    observed[0] = currentDestination->unkE;
    observed[1] = currentDestination->unk10;
    observed[2] = currentDestination->unk12;
    if (mutate) currentDestination->unkE = 77;
    return callbackResult;
}
static s32 first(void) { return callback(0); }
static s32 second(void) { return callback(1); }
s32 (*D_8008B36C[])(void) = { first, second };
""" + match.group(0) + "\n")
        library = directory / "publication.so"
        subprocess.run(
            [compiler, "-shared", "-fPIC", "-O2", "-std=c99",
             str(fixture), "-o", str(library)],
            check=True, capture_output=True, text=True,
        )
        cls.library = ctypes.CDLL(str(library))
        cls.publish = cls.library.func_15163504
        cls.publish.argtypes = [ctypes.POINTER(Record)]
        cls.publish.restype = ctypes.c_int32

    def integer(self, name):
        return ctypes.c_int32.in_dll(self.library, name)

    def setUp(self):
        self.destination = Destination()
        ctypes.memset(ctypes.byref(self.destination), 0xA5, ctypes.sizeof(self.destination))
        self.sources = [(ctypes.c_float * 3)(value, 99, -99)
                        for value in (1.9, -2.7, 3.4)]
        self.record = Record(ctypes.pointer(self.destination), self.sources[0],
                             self.sources[1], ctypes.addressof(self.sources[2]), -1)
        for name in ("callbackCalls", "mutate"):
            self.integer(name).value = 0
        self.integer("callbackSlot").value = -1
        self.integer("callbackResult").value = 1
        ctypes.c_void_p.in_dll(self.library, "currentDestination").value = ctypes.addressof(self.destination)

    def assertCoordinates(self, expected):
        self.assertEqual((self.destination.x, self.destination.y, self.destination.z), expected)
        self.assertEqual(bytes(self.destination.prefix), bytes([0xA5] * 14))
        self.assertEqual(bytes(self.destination.suffix), bytes([0xA5] * 4))

    def test_independent_sources_truncate_toward_zero(self):
        self.assertEqual(self.publish(ctypes.byref(self.record)), 1)
        self.assertCoordinates((1, -2, 3))

    def test_sentinel_publishes_without_callback(self):
        self.publish(ctypes.byref(self.record))
        self.assertCoordinates((1, -2, 3))
        self.assertEqual(self.integer("callbackCalls").value, 0)

    def test_callback_observes_all_coordinates_and_returns_result(self):
        self.record.selector = 1
        self.integer("callbackResult").value = 5
        self.assertEqual(self.publish(ctypes.byref(self.record)), 5)
        self.assertEqual(self.integer("callbackCalls").value, 1)
        self.assertEqual(self.integer("callbackSlot").value, 1)
        self.assertEqual(tuple((ctypes.c_int32 * 3).in_dll(self.library, "observed")), (1, -2, 3))

    def test_zero_callback_result_is_propagated(self):
        self.record.selector = 0
        self.integer("callbackResult").value = 0
        self.assertEqual(self.publish(ctypes.byref(self.record)), 0)
        self.assertEqual(self.integer("callbackCalls").value, 1)

    def test_callback_mutation_and_negative_result_are_preserved(self):
        self.record.selector = 0
        self.integer("callbackResult").value = -7
        self.integer("mutate").value = 1
        self.assertEqual(self.publish(ctypes.byref(self.record)), -7)
        self.assertCoordinates((77, -2, 3))

    def test_truncated_words_narrow_to_halfwords(self):
        for source, value in zip(self.sources, (32768, 65535, -32769)):
            source[0] = value
        self.assertEqual(self.publish(ctypes.byref(self.record)), 1)
        self.assertCoordinates((-32768, -1, 32767))


if __name__ == "__main__":
    unittest.main()
