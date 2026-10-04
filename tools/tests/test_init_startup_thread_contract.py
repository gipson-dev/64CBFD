import hashlib
import struct
import unittest

from tools.experiments import audit_init_storage_literals as literals
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture


class StartupThreadFixture(GuestBuilderFixture):
    STACK = 0x80060000
    CREATE = 0x100037F0
    QUEUE = 0x8002BDFC

    def __init__(self, code, thread, argument=0):
        self.code = dict(code)
        # Stub only queue setup and interrupt-mask helpers; no hardware claim.
        self.code.update({0x10004470: 0x03E00008, 0x10004474: 0,
                          0x10022DC0: 0x24020055, 0x10022DC4: 0x03E00008,
                          0x10022DC8: 0, 0x10022DE0: 0x03E00008, 0x10022DE4: 0})
        self.registers = [(0xA5A50000 + index) & 0xFFFFFFFF for index in range(32)]
        self.registers[0] = 0
        self.registers[4] = argument
        self.registers[29] = self.STACK
        self.fprs = [0] * 32
        self.memory = dict.fromkeys(range(0x800318A0, 0x80032B30), 0xA5)
        self.memory.update(dict.fromkeys(range(self.STACK - 0x40, self.STACK + 0x40), 0xA5))
        self.readonly = []
        self.allowed_writes = [(thread, thread + 0x230),
                               (self.STACK - 0x40, self.STACK + 0x40),
                               (self.QUEUE, self.QUEUE + 4)]
        self.put(self.QUEUE, 0x80077770, 4)
        self.writes, self.reads, self.visits = [], [], {}
        self.capture, self.snapshots = {self.CREATE}, {}
        self.min_sp = self.STACK


class InitStartupThreadContractTests(unittest.TestCase):
    REGIONS = ((0x10AC, 0x10DC, "fb48d3f639678ca252c7dfcf5f6d3d2f647ee5c23e8b2ba2eb4d93b70ec3ce2f"),
               (0x10F8, 0x113C, "8317d6527d4e4391782d77eb1d817c86046ca484daf2dd32a4ea46a369d5e8d2"),
               (0x37F0, 0x38B8, "4fa02c8a7eefc1e0c6a772e9fcbb34f4d7f481cdaf4dadd41beffcf430116e15"))

    @classmethod
    def setUpClass(cls):
        path = literals.ROOT / "baserom.us.z64"
        if not path.is_file():
            raise unittest.SkipTest("local pristine retail ROM required")
        cls.rom = path.read_bytes()
        if hashlib.sha1(cls.rom).hexdigest() != literals.ROM_SHA1:
            raise AssertionError("retail ROM hash mismatch")
        cls.code = {}
        for first, last, digest in cls.REGIONS:
            data = cls.rom[first:last]
            if hashlib.sha256(data).hexdigest() != digest:
                raise AssertionError("startup/constructor words changed")
            cls.code.update((0x10000000 + offset, struct.unpack_from(">I", cls.rom, offset)[0])
                            for offset in range(first, last, 4))

    def fixture(self, second=False, argument=0):
        thread = 0x80031AE0 if second else 0x800318B0
        guest = StartupThreadFixture(self.code, thread, argument)
        entry, stop = (0x100010F8, 0x1000113C) if second else (0x100010AC, 0x100010DC)
        guest.run(entry=entry, stop_pc=stop, budget=256)
        self.assertEqual(guest.visits.get(guest.CREATE), 1)
        self.assertEqual(guest.visits.get(0x10003880), 1)
        self.assertEqual(guest.visits.get(0x1000389C), 1)
        return guest, thread

    def test_actual_call_arguments_include_delay_slot_and_stack_parameters(self):
        for second, argument in ((False, 0), (True, 0), (True, 1), (True, 0xDEADBEEF)):
            with self.subTest(second=second, argument=argument):
                guest, thread = self.fixture(second, argument)
                registers, _ = guest.snapshots[guest.CREATE]
                expected = [thread, 3 if second else 1,
                            0x10001194 if second else 0x100010F8,
                            argument if second else 0]
                self.assertEqual(registers[4:8], expected)
                self.assertEqual(guest.get(registers[29] + 0x10, 4),
                                 0x800318B0 if second else 0x8002D8B0)
                self.assertEqual(guest.get(registers[29] + 0x14, 4), 10 if second else 5)

    def test_constructor_publishes_signed_context_stack_and_argument(self):
        for second, argument in ((False, 0), (True, 1), (True, 0xDEADBEEF)):
            with self.subTest(second=second, argument=argument):
                guest, thread = self.fixture(second, argument)
                stack_top = 0x800318B0 if second else 0x8002D8B0
                self.assertEqual(guest.get(thread + 0xF0, 8), 0xFFFFFFFF00000000 | (stack_top - 16))
                signed_arg = argument | (0xFFFFFFFF00000000 if argument & 0x80000000 else 0)
                self.assertEqual(guest.get(thread + 0x38, 8), signed_arg)
                self.assertEqual(guest.get(thread + 0x11C, 4), 0x10001194 if second else 0x100010F8)
                self.assertEqual(guest.get(thread + 0x100, 8), 0x10007BF8)
                self.assertEqual(guest.get(thread + 0x118, 4), 0x0400FF03)
                self.assertEqual(guest.get(thread + 0x128, 4), 0x3F)
                self.assertEqual(guest.get(thread + 0x12C, 4), 0x01000800)
                self.assertEqual(guest.get(thread + 0x14, 4), 3 if second else 1)
                self.assertEqual(guest.get(thread + 4, 4), 10 if second else 5)
                self.assertEqual(guest.get(thread + 0x10, 2), 1)
                self.assertEqual(guest.get(thread + 0x12, 2), 0)
                self.assertEqual(guest.get(thread + 0x18, 4), 0)
                self.assertEqual(guest.get(thread + 0xC, 4), 0x80077770)
                self.assertEqual(guest.get(guest.QUEUE, 4), thread)

    def test_constructor_extent_and_private_gap_are_not_written(self):
        for second in (False, True):
            with self.subTest(second=second):
                guest, thread = self.fixture(second)
                context_writes = [(address, size) for address, size in guest.writes
                                  if thread <= address < thread + 0x230]
                self.assertEqual(max(address + size for address, size in context_writes), thread + 0x130)
                self.assertEqual(bytes(guest.memory[address] for address in range(thread + 0x130, thread + 0x230)),
                                 b"\xA5" * 0x100)
                first, last = 0x80031D10, 0x80032B1C
                self.assertEqual(bytes(guest.memory[address] for address in range(first, last)),
                                 b"\xA5" * (last - first))
                self.assertFalse(any(address < last and first < address + size for address, size in guest.writes))

    def test_constructor_restores_callee_register_and_call_stack(self):
        for second in (False, True):
            guest, _ = self.fixture(second)
            self.assertEqual(guest.registers[16], 0xA5A50010)
            self.assertEqual(guest.registers[29], guest.STACK - (0x20 if second else 0))
            self.assertEqual(guest.min_sp, guest.STACK - (0x40 if second else 0x20))

    def test_executed_store_crossing_thread_extent_is_rejected(self):
        for thread, entry, stop in ((0x800318B0, 0x100010AC, 0x100010DC),
                                    (0x80031AE0, 0x100010F8, 0x1000113C)):
            guest = StartupThreadFixture(self.code, thread)
            self.assertEqual(guest.code[0x10003874], 0xAE19012C)
            guest.code[0x10003874] = 0xAE190230
            with self.assertRaisesRegex(AssertionError, "guest write exceeds caller-owned buffers"):
                guest.run(entry=entry, stop_pc=stop, budget=256)


if __name__ == "__main__":
    unittest.main()
