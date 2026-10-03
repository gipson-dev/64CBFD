import ctypes
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class GameTimedCallbackRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("cc")
        if compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_185560.c").read_text()
        match = re.search(r"void func_15158224\(u8 \*arg0\) \{\n.*?\n\}", source, re.S)
        if match is None:
            raise AssertionError("timed callback record definition was not found")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        directory = Path(cls.directory.name)
        fixture = directory / "callback.c"
        fixture.write_text(
            "#include <stdint.h>\n"
            "typedef uint8_t u8; typedef int8_t s8;\n"
            "typedef int16_t s16; typedef int32_t s32;\n" + r"""
s32 D_800BE9E4;
u8 *currentRecord, *releasedRecord;
s32 callbackCalls, releaseCalls, callbackResult, callbackSlot, observedTimer, mutate;
static s32 callback(s32 slot) {
    callbackCalls++;
    callbackSlot = slot;
    observedTimer = *(s16 *)(currentRecord + 0x14);
    if (mutate) {
        currentRecord[0x10] ^= 0x80;
        currentRecord[0x12] = 0xFF;
    }
    return callbackResult;
}
static s32 first(void) { return callback(0); }
static s32 second(void) { return callback(1); }
s32 (*D_8008AE00[])() = { first, second };
void func_1516972C(u8 *record) {
    releaseCalls++;
    releasedRecord = record;
}
""" + match.group(0) + "\n"
        )
        library = directory / "callback.so"
        subprocess.run(
            [compiler, "-shared", "-fPIC", "-O2", "-std=c99",
             str(fixture), "-o", str(library)],
            check=True, capture_output=True, text=True,
        )
        cls.library = ctypes.CDLL(str(library))
        cls.update = cls.library.func_15158224
        cls.update.argtypes = [ctypes.POINTER(ctypes.c_uint8)]
        cls.update.restype = None

    def integer(self, name):
        return ctypes.c_int32.in_dll(self.library, name)

    def setUp(self):
        self.record = (ctypes.c_uint8 * 32)(*([0xA5] * 32))
        self.record[0x10] = 0
        self.record[0x11] = 0
        self.record[0x12] = 0xFF
        self.timer = ctypes.c_int16.from_buffer(self.record, 0x14)
        self.timer.value = 100
        for name in ("callbackCalls", "releaseCalls", "callbackSlot", "observedTimer", "mutate"):
            self.integer(name).value = 0
        self.integer("callbackResult").value = 1
        self.integer("D_800BE9E4").value = 1
        ctypes.c_void_p.in_dll(self.library, "currentRecord").value = ctypes.addressof(self.record)
        ctypes.c_void_p.in_dll(self.library, "releasedRecord").value = None

    def assertReleaseCount(self, count):
        self.assertEqual(self.integer("releaseCalls").value, count)
        address = ctypes.c_void_p.in_dll(self.library, "releasedRecord").value
        self.assertEqual(address, ctypes.addressof(self.record) if count else None)

    def test_disabled_timer_preserves_record_and_dispatches(self):
        self.record[0x10] = 2
        self.record[0x12] = 0
        self.timer.value = -10
        self.integer("callbackResult").value = -7
        before = bytes(self.record)
        self.update(self.record)
        self.assertEqual(bytes(self.record), before)
        self.assertEqual(self.integer("callbackCalls").value, 1)
        self.assertReleaseCount(0)

    def test_sentinel_skips_callback_and_release(self):
        self.update(self.record)
        self.assertEqual(self.integer("callbackCalls").value, 0)
        self.assertReleaseCount(0)

    def test_expired_timer_skips_callback_and_releases_once(self):
        self.record[0x10] = 1
        self.record[0x12] = 0
        self.timer.value = 0
        self.update(self.record)
        self.assertEqual(self.timer.value, -1)
        self.assertEqual(self.integer("callbackCalls").value, 0)
        self.assertReleaseCount(1)

    def test_zero_timer_after_update_is_not_expired(self):
        self.record[0x10] = 1
        self.record[0x12] = 0
        self.timer.value = 1
        self.update(self.record)
        self.assertEqual(self.timer.value, 0)
        self.assertEqual(self.integer("observedTimer").value, 0)
        self.assertEqual(self.integer("callbackCalls").value, 1)
        self.assertReleaseCount(0)

    def test_callback_failure_releases_once(self):
        self.record[0x12] = 0
        self.integer("callbackResult").value = 0
        self.update(self.record)
        self.assertEqual(self.integer("callbackCalls").value, 1)
        self.assertReleaseCount(1)

    def test_signed_halfword_wrap_is_checked_after_store(self):
        for timer, delta, expected, removed in ((32767, -1, -32768, 1),
                                                 (-32768, 1, 32767, 0)):
            with self.subTest(timer=timer, delta=delta):
                self.setUp()
                self.record[0x10] = 1
                self.timer.value = timer
                self.integer("D_800BE9E4").value = delta
                self.update(self.record)
                self.assertEqual(self.timer.value, expected)
                self.assertReleaseCount(removed)

    def test_callback_mutation_keeps_original_release_argument(self):
        self.record[0x12] = 0
        self.integer("callbackResult").value = 0
        self.integer("mutate").value = 1
        self.update(self.record)
        self.assertEqual(self.record[0x10], 0x80)
        self.assertEqual(self.record[0x12], 0xFF)
        self.assertReleaseCount(1)

    def test_selector_uses_offset_12_not_neighbor(self):
        self.record[0x11] = 0
        self.record[0x12] = 1
        self.update(self.record)
        self.assertEqual(self.integer("callbackSlot").value, 1)
        self.assertEqual(self.integer("callbackCalls").value, 1)
        self.assertReleaseCount(0)


if __name__ == "__main__":
    unittest.main()
