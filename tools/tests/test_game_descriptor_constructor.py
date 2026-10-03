import ctypes
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


class GameDescriptorConstructorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("cc")
        if compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        root = Path(__file__).resolve().parents[2]
        source = (root / "conker/src/game_1FFF60.c").read_text()
        body = re.search(r"struct224 \*func_151D2F00\(void \* volatile arg0, s32 volatile arg1, "
                         r"u8 volatile arg2, s32 volatile arg3\) \{\n.*?\n\}", source, re.S)
        header = (root / "conker/include/structs.h").read_text()
        record = re.search(r"struct struct224 \{\n.*?\n\};", header, re.S)
        if body is None or record is None:
            raise AssertionError("descriptor constructor or shared record declaration was not found")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        directory = Path(cls.directory.name)
        fixture = directory / "constructor.c"
        fixture.write_text("#include <stddef.h>\n#include <stdint.h>\n"
                           "typedef uint8_t u8; typedef int16_t s16; typedef int32_t s32;\n"
                           "typedef struct struct224 struct224;\n" + record.group(0) + "\n" + r'''
struct224 candidate;
s32 failAllocation, allocationCalls, copyCalls, arguments[6];
void *copyDestination;
const void *copySource;
size_t copyLength;
struct224 *func_15167A68(s32 type, s32 owner, s32 size, s32 mode, u8 selector, u8 enabled) {
    allocationCalls++;
    arguments[0] = type; arguments[1] = owner; arguments[2] = size;
    arguments[3] = mode; arguments[4] = selector; arguments[5] = enabled;
    return failAllocation ? NULL : &candidate;
}
static void *mockCopy(void *destination, const void *source, size_t length) {
    size_t i;
    copyCalls++;
    copyDestination = destination; copySource = source; copyLength = length;
    for (i = 0; i < length; i++) ((u8 *)destination)[i] = ((const u8 *)source)[i];
    return destination;
}
#define memcpy mockCopy
''' + body.group(0) + "\n" + r'''
size_t recordSize(void) { return sizeof(struct224); }
size_t recordOffset(s32 field) {
    switch (field) {
    case 0: return offsetof(struct224, unk10);
    case 1: return offsetof(struct224, unk20);
    case 2: return offsetof(struct224, unk24);
    default: return offsetof(struct224, unk28);
    }
}
''')
        library = directory / "constructor.so"
        subprocess.run([compiler, "-shared", "-fPIC", "-O2", "-std=c99",
                        "-fno-strict-aliasing", str(fixture), "-o", str(library)],
                       check=True, capture_output=True, text=True)
        cls.library = ctypes.CDLL(str(library))
        cls.construct = cls.library.func_151D2F00
        cls.construct.argtypes = [ctypes.c_void_p, ctypes.c_int32, ctypes.c_uint8, ctypes.c_int32]
        cls.construct.restype = ctypes.c_void_p
        cls.library.recordSize.restype = ctypes.c_size_t
        cls.size = cls.library.recordSize()
        cls.library.recordOffset.argtypes = [ctypes.c_int32]
        cls.library.recordOffset.restype = ctypes.c_size_t

    def integer(self, name):
        return ctypes.c_int32.in_dll(self.library, name)

    def setUp(self):
        self.candidate = (ctypes.c_uint8 * self.size).in_dll(self.library, "candidate")
        ctypes.memset(ctypes.addressof(self.candidate), 0xA5, self.size)
        self.source = (ctypes.c_uint8 * 16)(*range(16))
        for name in ("failAllocation", "allocationCalls", "copyCalls"):
            self.integer(name).value = 0

    def check_success(self, flags=0xFF, payload_size=0x60, selector=0x91, owner=-7):
        self.source[8] = flags
        original_source = bytes(self.source)
        result = self.construct(ctypes.addressof(self.source), payload_size, selector, owner)
        self.assertEqual(result, ctypes.addressof(self.candidate))
        self.assertEqual(self.integer("allocationCalls").value, 1)
        self.assertEqual(self.integer("copyCalls").value, 1)
        self.assertEqual(tuple((ctypes.c_int32 * 6).in_dll(self.library, "arguments")),
                         (0x3E, owner, payload_size + 0x30, 1, selector & 0xFF, 1))
        self.assertEqual(ctypes.c_void_p.in_dll(self.library, "copyDestination").value,
                         ctypes.addressof(self.candidate) + 0x10)
        self.assertEqual(ctypes.c_void_p.in_dll(self.library, "copySource").value,
                         ctypes.addressof(self.source))
        self.assertEqual(ctypes.c_size_t.in_dll(self.library, "copyLength").value, 16)
        expected = bytearray([0xA5] * self.size)
        expected[0x10:0x20] = original_source
        expected[0x18] &= 0xFD
        expected[0x20:0x22] = bytes(2)
        expected[0x24:0x2C] = bytes(8)
        self.assertEqual(bytes(self.candidate), bytes(expected))
        self.assertEqual(bytes(self.source), original_source)

    def test_shared_record_offsets_match_constructor_accesses(self):
        self.assertEqual(tuple(self.library.recordOffset(i) for i in range(4)),
                         (0x10, 0x20, 0x24, 0x28))

    def test_allocation_failure_skips_copy_and_all_writes(self):
        self.integer("failAllocation").value = 1
        self.assertIsNone(self.construct(None, 0x60, 0xFE, -9))
        self.assertEqual(self.integer("allocationCalls").value, 1)
        self.assertEqual(self.integer("copyCalls").value, 0)
        self.assertEqual(bytes(self.candidate), bytes([0xA5] * self.size))

    def test_descriptor_copy_and_bookkeeping_reset(self):
        self.check_success()

    def test_only_flag_bit_two_is_cleared_for_every_byte(self):
        for flags in range(256):
            with self.subTest(flags=flags):
                self.setUp()
                self.check_success(flags=flags)

    def test_allocator_arguments_preserve_signed_values_and_byte_selector(self):
        for size, selector, owner in ((0, 0, 0), (-0x30, 255, -1),
                                      (0x1234, 128, 0x7FFFFFFF), (7, 257, -0x80000000)):
            with self.subTest(size=size, selector=selector, owner=owner):
                self.setUp()
                self.check_success(payload_size=size, selector=selector, owner=owner)


if __name__ == "__main__":
    unittest.main()
