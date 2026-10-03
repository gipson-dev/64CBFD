import hashlib
import re
import struct
import unittest
from pathlib import Path
from types import SimpleNamespace

from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture
from tools.tests import test_init_decompressor_retail_pages as retail


class FaultRouteFixture(GuestBuilderFixture):
    THREAD = 0x80031AE0

    def __init__(self, code, cause, diagnostic_flags=0):
        self.code = code
        self.image = SimpleNamespace(entry=0x100073EC)
        self.memory = {}
        self.readonly, self.allowed_writes = [], None
        self.registers = [0] * 32
        self.registers[26] = self.THREAD
        self.registers[29] = self.min_sp = 0x80032A10
        self.fprs = [0] * 32
        self.reads, self.writes, self.visits = [], [], {}
        self.capture, self.snapshots = set(), {}
        self.cp0 = {13: cause, 8: 0xDEADBEEF}
        for address, value, size in ((self.THREAD + 0x11C, 0x150AD770, 4),
                                     (self.THREAD + 0x10, 4, 2),
                                     (self.THREAD + 0x12, 0, 2),
                                     (0x800E9D00, diagnostic_flags, 4),
                                     (0x80042970, 0, 4)):
            self.put(address, value, size)
        self.allowed_writes = [(self.THREAD, self.THREAD + 0x230),
                               (0x8002BE04, 0x8002BE08),
                               (0x8003C8F8, 0x8003C900)]
        self.writes.clear()

    def execute(self, word):
        if word >> 26 == 16:
            rs, rt, rd = word >> 21 & 31, word >> 16 & 31, word >> 11 & 31
            if rs != 0 or rd not in self.cp0 or word & 0x7FF:
                raise AssertionError("only seeded Cause/BadVAddr reads are modeled")
            self.registers[rt] = self.cp0[rd]
            self.registers[0] = 0
        else:
            super().execute(word)


class InitSyscallFaultRouteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = Path(__file__).resolve().parents[2]
        rom = root / "baserom.us.z64"
        if not rom.is_file():
            raise unittest.SkipTest("local retail ROM required")
        data = rom.read_bytes()
        if hashlib.sha1(data).hexdigest() != retail.ROM_SHA1:
            raise AssertionError("expected original US retail ROM")
        source = (root / "conker/asm/init_5AB0.s").read_text()
        entries = {int(pc, 16): int(word, 16) for pc, word in re.findall(
            r"/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+([0-9A-Fa-f]{8})\s*\*/", source)}
        cls.code = {}
        for first, last in ((0x100073EC, 0x1000743C), (0x1000777C, 0x1000787C),
                            (0x10007DAC, 0x10007DD4), (0x10008108, 0x10008118)):
            for pc in range(first, last, 4):
                word = entries[pc]
                if struct.unpack_from(">I", data, pc - 0x10000000)[0] != word:
                    raise AssertionError("fault-route assembly differs from retail")
                cls.code[pc] = word

    def test_syscall_cause_routes_to_fault_with_pending_and_bd_bits(self):
        for flags in (0, 0xFF00, 0x80000000, 0x8000FF00):
            with self.subTest(flags=hex(flags)):
                fixture = FaultRouteFixture(self.code, 0x20 | flags)
                fixture.run(stop_pc=0x1000777C, budget=64)
                self.assertEqual(fixture.get(fixture.THREAD + 0x120, 4), 0x20 | flags)
                self.assertEqual(fixture.get(fixture.THREAD + 0x10, 2), 2)
                self.assertEqual(fixture.registers[9], 0x20)
                self.assertIn(0x10007434, fixture.visits)
                self.assertNotIn(0x1000743C, fixture.visits)

    def test_dispatch_distinguishes_tlb_break_and_interrupt_routes(self):
        for cause, target in ((8, 0x10007708), (12, 0x10007718),
                              (0x24, 0x10007720), (0x2C, 0x1000787C),
                              (0, 0x1000743C)):
            with self.subTest(cause=cause):
                fixture = FaultRouteFixture(self.code, cause)
                fixture.run(stop_pc=target, budget=64)
                self.assertEqual(fixture.registers[9], cause)

    def test_disabled_diagnostics_fault_notification_then_scheduler_boundary(self):
        fixture = FaultRouteFixture(self.code, 0x20)
        fixture.run(stop_pc=0x10007DAC, budget=96)
        self.assertEqual(fixture.get(0x8002BE04, 4), fixture.THREAD)
        self.assertEqual(fixture.get(fixture.THREAD + 0x10, 2), 1)
        self.assertEqual(fixture.get(fixture.THREAD + 0x12, 2), 2)
        self.assertEqual(fixture.get(fixture.THREAD + 0x124, 4), 0xDEADBEEF)
        self.assertEqual(fixture.get(fixture.THREAD + 0x11C, 4), 0x150AD770)
        fixture.run(entry=0x10007DAC, stop_pc=0x100077A4, budget=64)
        self.assertEqual(fixture.get(0x8003C8F8, 4), 0x100077A4)
        self.assertEqual(fixture.get(0x8003C8FC, 4), 0x80032A10)
        self.assertNotIn(0x10007DD4, fixture.visits)
        # Stop before JR s2; assert its target instead of widening the CPU model.
        fixture.run(entry=0x100077A4, stop_pc=0x10007874, budget=64)
        self.assertEqual(fixture.registers[4], 0x60)
        self.assertEqual(fixture.registers[18], 0x100077B0)
        self.assertNotIn(0x100077D4, fixture.visits)
        fixture.run(entry=fixture.registers[18], stop_pc=0x10007A38, budget=8)
        self.assertEqual(fixture.get(fixture.THREAD + 0x10, 2), 1)
        self.assertEqual(fixture.get(fixture.THREAD + 0x11C, 4), 0x150AD770)

    def test_enabled_diagnostics_enters_diagnostic_body(self):
        fixture = FaultRouteFixture(self.code, 0x20, diagnostic_flags=0x2000)
        fixture.run(stop_pc=0x10007DAC, budget=96)
        fixture.run(entry=0x10007DAC, stop_pc=0x10007DD4, budget=32)
        self.assertNotIn(0x10008108, fixture.visits)
        self.assertEqual(fixture.registers[9], 0x2000)


if __name__ == "__main__":
    unittest.main()
