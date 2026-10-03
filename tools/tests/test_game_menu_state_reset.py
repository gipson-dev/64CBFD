import ctypes
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class GameMenuStateResetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("cc")
        if compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_20AE20.c").read_text()
        body = re.search(r"void func_151DE85C\(void\) \{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("menu state reset definition was not found")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        directory = Path(cls.directory.name)
        fixture = directory / "menu_reset.c"
        fixture.write_text("#include <stdint.h>\n"
                           "typedef uint8_t u8; typedef int8_t s8; typedef int32_t s32;\n" + r'''
u8 D_800D2E40, D_800E0B94, D_8008FD80, D_8008FE28, D_8008FDA4;
s8 *D_8008FDD4, *replacement;
s32 calls, mutate;
s32 arguments[5], observed[5];
void func_1501C730(s32 first, s32 second, s32 third, s32 fourth, s32 fifth) {
    calls++;
    arguments[0] = first; arguments[1] = second; arguments[2] = third;
    arguments[3] = fourth; arguments[4] = fifth;
    observed[0] = D_800D2E40; observed[1] = D_800E0B94;
    observed[2] = D_8008FD80; observed[3] = D_8008FE28; observed[4] = D_8008FDA4;
    if (mutate) {
        D_800D2E40 = 0x66;
        D_800E0B94 = D_8008FD80 = D_8008FE28 = D_8008FDA4 = 0x77;
        D_8008FDD4 = replacement;
    }
}
''' + body.group(0) + "\n")
        library = directory / "menu_reset.so"
        subprocess.run([compiler, "-shared", "-fPIC", "-O2", "-std=c99",
                        str(fixture), "-o", str(library)],
                       check=True, capture_output=True, text=True)
        cls.library = ctypes.CDLL(str(library))
        cls.reset = cls.library.func_151DE85C
        cls.reset.argtypes = []
        cls.reset.restype = None

    def setUp(self):
        self.actor = (ctypes.c_uint8 * 0x50)(*([0xA5] * 0x50))
        self.other = (ctypes.c_uint8 * 0x50)(*([0x5A] * 0x50))
        self.globals = [ctypes.c_uint8.in_dll(self.library, name) for name in
                        ("D_800D2E40", "D_800E0B94", "D_8008FD80", "D_8008FE28", "D_8008FDA4")]
        for value, initial in zip(self.globals, (0xFF, 0x31, 0x42, 0x53, 0x64)):
            value.value = initial
        ctypes.c_int32.in_dll(self.library, "calls").value = 0
        ctypes.c_int32.in_dll(self.library, "mutate").value = 0
        ctypes.c_void_p.in_dll(self.library, "D_8008FDD4").value = ctypes.addressof(self.actor)
        ctypes.c_void_p.in_dll(self.library, "replacement").value = ctypes.addressof(self.other)

    def expected_actor(self, fill):
        expected = bytearray([fill] * 0x50)
        expected[0x3E] = 0
        expected[0x2B] = expected[0x2C] = 5
        return bytes(expected)

    def test_gate_is_cleared_before_exact_external_call(self):
        self.reset()
        self.assertEqual(ctypes.c_int32.in_dll(self.library, "calls").value, 1)
        self.assertEqual(tuple((ctypes.c_int32 * 5).in_dll(self.library, "arguments")),
                         (6, 0x1D, 0, 0, 1))
        self.assertEqual(tuple((ctypes.c_int32 * 5).in_dll(self.library, "observed")),
                         (0, 0x31, 0x42, 0x53, 0x64))

    def test_final_global_state_bytes(self):
        self.reset()
        self.assertEqual(tuple(value.value for value in self.globals), (0, 3, 1, 2, 0))

    def test_only_three_object_bytes_are_changed(self):
        self.reset()
        self.assertEqual(bytes(self.actor), self.expected_actor(0xA5))
        self.assertEqual(bytes(self.other), bytes([0x5A] * 0x50))

    def test_external_call_mutation_uses_new_pointer_and_is_overwritten(self):
        ctypes.c_int32.in_dll(self.library, "mutate").value = 1
        self.reset()
        self.assertEqual(tuple(value.value for value in self.globals), (0x66, 3, 1, 2, 0))
        self.assertEqual(bytes(self.actor), bytes([0xA5] * 0x50))
        self.assertEqual(bytes(self.other), self.expected_actor(0x5A))

    def test_repeated_reset_reapplies_state_and_resubmits_call(self):
        self.reset()
        self.actor[0x2B] = 0x80
        self.actor[0x2C] = 0xFF
        self.actor[0x3E] = 0x11
        for value in self.globals:
            value.value = 0xEE
        self.reset()
        self.assertEqual(ctypes.c_int32.in_dll(self.library, "calls").value, 2)
        self.assertEqual(tuple(value.value for value in self.globals), (0, 3, 1, 2, 0))
        self.assertEqual(bytes(self.actor), self.expected_actor(0xA5))


if __name__ == "__main__":
    unittest.main()
