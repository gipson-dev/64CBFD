import hashlib
import struct
import unittest
from pathlib import Path
from types import SimpleNamespace

from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture
from tools.tests import test_init_decompressor_retail_pages as retail


class DebuggerEntryFixture(GuestBuilderFixture):
    SP, THREAD = 0x80135958, 0x80031AE0

    def __init__(self, code, disabled=0, framebuffers=(0x80350000, 0x80370000)):
        self.code, self.image = code, SimpleNamespace(entry=0x16000B14)
        self.memory = {address: 0xA5 for address in range(self.SP - 96, self.SP + 20)}
        self.readonly, self.allowed_writes = [], None
        self.registers = [0x5A000000 + i for i in range(32)]
        self.registers[0] = 0
        self.registers[4], self.registers[29], self.registers[31] = self.THREAD, self.SP, 0xDEAD0000
        self.before, self.min_sp = self.registers[:], self.SP
        self.fprs = [0] * 32
        self.reads, self.writes, self.visits = [], [], {}
        self.capture, self.snapshots = set(), {}
        for address, value, size in ((0x8002AC5C, disabled, 1),
                                     (0x8002AAE8, framebuffers[0], 4),
                                     (0x8002AAEC, framebuffers[1], 4),
                                     (0x16003888, 0xA5, 1),
                                     (0x16003AF0, 1, 4), (0x160038A4, 1, 1),
                                     (self.THREAD + 0x10, 1, 2),
                                     (self.THREAD + 0x12, 2, 2),
                                     (self.THREAD + 0x11C, 0x150AD770, 4),
                                     (self.THREAD + 0x120, 0x20, 4)):
            self.put(address, value, size)
        self.allowed_writes = [(self.SP - 80, self.SP + 4),
                               (0x8002AAE8, 0x8002AAF0), (0x16003888, 0x16003889),
                               (self.THREAD + 0x10, self.THREAD + 0x14),
                               (self.THREAD + 0x11C, self.THREAD + 0x120)]
        self.writes.clear()


class InitDebuggerEntryContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[2]
        path = root / "baserom.us.z64"
        if not path.is_file():
            raise unittest.SkipTest("local retail ROM required")
        rom = path.read_bytes()
        if hashlib.sha1(rom).hexdigest() != retail.ROM_SHA1:
            raise AssertionError("expected original US retail ROM")
        first, last = 0xB14, 0xF8C
        raw = rom[0x19EA88 + first:0x19EA88 + last]
        if len(raw) != 0x478:
            raise AssertionError("incomplete retail debugger function")
        cls.code = {0x16000000 + first + i * 4: word for i, (word,) in
                    enumerate(struct.iter_unpack(">I", raw))}
        if cls.code[0x16000B14] != 0x27BDFFB0 or cls.code[0x16000F88] != 0x27BD0050:
            raise AssertionError("retail debugger frame differs")

    def assert_restored(self, fixture):
        for register in (*range(16, 24), 28, 29, 30, 31):
            self.assertEqual(fixture.registers[register], fixture.before[register])
        self.assertEqual(fixture.min_sp, fixture.SP - 80)
        self.assertEqual(bytes(fixture.memory[fixture.SP - 96 + i] for i in range(16)), b"\xA5" * 16)
        self.assertEqual(bytes(fixture.memory[fixture.SP + 4 + i] for i in range(16)), b"\xA5" * 16)
        self.assertEqual(fixture.get(fixture.SP, 4), fixture.THREAD)
        self.assertEqual((fixture.SP - 80) - (0x80130000 + 0x4960), 0xFA8)

    def test_disabled_entry_returns_zero_without_framebuffer_or_flag_reset(self):
        fixture = DebuggerEntryFixture(self.code, disabled=1)
        self.assertEqual(fixture.run(budget=128), 0)
        self.assertEqual(fixture.get(0x16003888, 1), 0xA5)
        self.assertEqual(fixture.get(0x8002AAE8, 4), 0x80350000)
        self.assertEqual(fixture.get(0x8002AAEC, 4), 0x80370000)
        self.assertNotIn(0x16000B9C, fixture.visits)
        self.assert_restored(fixture)

    def test_missing_either_framebuffer_sets_both_fallbacks_and_returns_zero(self):
        for framebuffers in ((0, 0x80370000), (0x80350000, 0), (0, 0)):
            with self.subTest(framebuffers=framebuffers):
                fixture = DebuggerEntryFixture(self.code, framebuffers=framebuffers)
                self.assertEqual(fixture.run(budget=128), 0)
                self.assertEqual(fixture.get(0x16003888, 1), 0)
                self.assertEqual(fixture.get(0x8002AAE8, 4), 0x80350000)
                self.assertEqual(fixture.get(0x8002AAEC, 4), 0x80350000)
                self.assertNotIn(0x16000B9C, fixture.visits)
                self.assert_restored(fixture)

    def test_ready_framebuffers_reach_first_helper_boundary_with_bounded_frame(self):
        fixture = DebuggerEntryFixture(self.code)
        fixture.run(stop_pc=0x16000B9C, budget=64)
        self.assertEqual(fixture.registers[29], fixture.SP - 80)
        self.assertEqual(fixture.get(0x16003888, 1), 0)
        self.assertEqual(fixture.get(fixture.SP - 80 + 0x3C, 4), 0xDEAD0000)

    def test_seeded_footer_selects_runnable_syscall_skip_or_no_resume(self):
        cases = ((0, 0x20, 1, 0x150AD770, 1, 4, 0, 0x150AD770),
                 (1, 0x20, 1, 0x150AD770, 0, 1, 2, 0x150AD770),
                 (1, 0x20, 0, 0x10007DA0, 1, 1, 2, 0x10007DA4),
                 (1, 0x24, 0, 0x150AD770, 0, 1, 2, 0x150AD770))
        for mapping, cause, fatal, pc, result, state, flags, end_pc in cases:
            with self.subTest(mapping=mapping, cause=cause, fatal=fatal):
                fixture = DebuggerEntryFixture(self.code)
                fixture.run(stop_pc=0x16000B9C, budget=64)
                # UI/TLB scan is not executed; these are explicit footer premises.
                fixture.allowed_writes = None
                fixture.put(0x16003AF0, mapping, 4)
                fixture.put(0x160038A4, fatal, 1)
                fixture.put(fixture.THREAD + 0x120, cause, 4)
                fixture.put(fixture.THREAD + 0x11C, pc, 4)
                fixture.allowed_writes = [(fixture.THREAD + 0x10, fixture.THREAD + 0x14),
                                          (fixture.THREAD + 0x11C, fixture.THREAD + 0x120)]
                self.assertEqual(fixture.run(entry=0x16000F00, budget=128), result)
                self.assertEqual(fixture.get(fixture.THREAD + 0x10, 2), state)
                self.assertEqual(fixture.get(fixture.THREAD + 0x12, 2), flags)
                self.assertEqual(fixture.get(fixture.THREAD + 0x11C, 4), end_pc)
                self.assert_restored(fixture)


if __name__ == "__main__":
    unittest.main()
