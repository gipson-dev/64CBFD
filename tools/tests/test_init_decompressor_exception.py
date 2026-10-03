import struct
import unittest

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_streams as streams
from tools.tests.test_init_decompressor_retail_pages import (
    CALLER_SP, INPUT, WORKSPACE,
)


SR_FR = 0x04000000
SR_CU1 = 0x20000000
SAVED_FPRS = (*range(12), *range(16, 20))
CONTEXT_TOP = 0x80032B18
ENTRY = 0x10005E1C
STOP = 0x1000601C


class ExceptionCoreFixture(streams.StreamFixture):
    """FR=1 architectural-value model, not a pipeline/CP0 emulator."""

    def __init__(self, chunk, status, stale_f0=0xABCDEF0187654321):
        if not status & SR_FR:
            raise ValueError("Only FR=1 context is qualified")
        self.context_enabled = False
        super().__init__(chunk)
        self.code.update({pc: word for pc, word in
                          contract.InitDecompressorContractTests.entries(
                              "func_10005C2C") if ENTRY <= pc < STOP})
        self.INPUT, self.OUTPUT, self.WORKSPACE = INPUT, 0x80050000, WORKSPACE
        self.registers[17] = self.OUTPUT & 0x1FFFFFFF
        self.registers[29] = 0x80070000
        self.status = status
        self.initial_status = status
        self.status_writes = []
        self.high = [0xC0010000 + index for index in range(32)]
        self.fprs = [0xDEAD0000 + index for index in range(32)]
        self.initial_fprs = [self.fpr_value(index) for index in range(32)]
        self.initial_registers = self.registers[:]
        self.memory.update({INPUT + i: byte for i, byte in
                           enumerate(chunk + b"\0" * 16)})
        self.memory.update({address: 0xA5 for address in
                           range(CALLER_SP - 0xA88, CONTEXT_TOP + 4)})
        self.put(CALLER_SP, stale_f0, 8)
        self.put(0x800354F8, INPUT, 4)
        self.reads, self.writes = [], []
        self.fpr_loads, self.fpr_stores, self.fpr_moves = [], [], []
        self.stack_low = self.registers[29]
        self.capture = {0x1000625C, 0x10005F34}
        self.context_enabled = True

    def fpr_value(self, index):
        high = self.high[index]
        value = self.fprs[index] | (0 if high is None else high << 32)
        return value, 0xFFFFFFFF if high is None else 0xFFFFFFFFFFFFFFFF

    def execute(self, word):
        if not self.context_enabled:
            return super().execute(word)
        op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
        rd = (word >> 11) & 31
        if op == 16:
            if rd != 12 or rs not in (0, 4) or word & 0x7FF:
                raise AssertionError("Only CP0 Status moves are qualified")
            if rs == 0:
                self.registers[rt] = self.status
            else:
                status = self.registers[rt]
                if not status & SR_FR:
                    raise AssertionError("FR=0 transition is not qualified")
                self.status = status
                self.status_writes.append(status)
        elif op in (17, 53, 61):
            if not self.status & SR_CU1:
                raise AssertionError("COP1 access with CU1 disabled")
            if op == 17:
                if rs not in (0, 4):
                    raise AssertionError("Only MFC1/MTC1 are qualified")
                super().execute(word)
                if rs == 4:
                    # VR4300 MTC1 defines the low word, not its FR=1 upper half.
                    self.high[rd] = None
                    self.fpr_moves.append(rd)
            else:
                offset = word & 0xFFFF
                offset = offset if offset < 0x8000 else offset - 0x10000
                address = (self.registers[rs] + offset) & 0xFFFFFFFF
                if address & 7:
                    raise AssertionError("Unaligned FPR doubleword transfer")
                if op == 61:
                    value, mask = self.fpr_value(rt)
                    if mask != 0xFFFFFFFFFFFFFFFF:
                        raise AssertionError("Unknown FPR high word cannot be saved")
                    self.put(address, value, 8)
                    self.writes.append((address, 8))
                    self.fpr_stores.append((rt, address))
                else:
                    value = self.get(address, 8)
                    self.high[rt], self.fprs[rt] = value >> 32, value & 0xFFFFFFFF
                    self.reads.append((address, 8))
                    self.fpr_loads.append((rt, address))
        else:
            super().execute(word)
        self.stack_low = min(self.stack_low, self.registers[29])

    def context(self):
        return self.run(entry=ENTRY, stop_pc=STOP, budget=2000000)


class InitDecompressorExceptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract.InitDecompressorContractTests.setUpClass.__func__(
            contract.InitDecompressorContractTests)

    def test_wrapper_words_are_complete_and_retail_exact(self):
        entries = [(pc, word) for pc, word in
                   contract.InitDecompressorContractTests.entries("func_10005C2C")
                   if ENTRY <= pc < STOP]
        self.assertEqual([pc for pc, _ in entries], list(range(ENTRY, STOP, 4)))
        image = contract.InitDecompressorContractTests.project / "conker.us.bin"
        if not image.exists():
            self.skipTest("Pristine decompressed image required")
        self.assertEqual(b"".join(struct.pack(">I", word) for _, word in entries),
                         image.read_bytes()[ENTRY - 0x10000000:STOP - 0x10000000])

    @staticmethod
    def chunks():
        return ((struct.pack(">I", 2) + b"\x01\x02\0\xfd\xffXY", b"XY"),
                (b"\x11\x72" + streams.InitDecompressorStreamTests().dynamic(), b"A"))

    def assert_gpr_context(self, fixture):
        for index in (*range(1, 4), *range(5, 32)):
            self.assertEqual(fixture.registers[index],
                             fixture.initial_registers[index], index)
        # a0 is already replaced before its save and is reused for final SP load.
        self.assertEqual(fixture.registers[4], CONTEXT_TOP)
        self.assertEqual(fixture.get(CONTEXT_TOP, 4),
                         fixture.initial_registers[29])
        self.assertEqual(fixture.stack_low, CALLER_SP - 0xA88)
        self.assertEqual(fixture.status, fixture.initial_status)

    def test_cu1_clear_saves_and_restores_full_fprs(self):
        for chunk, expected in self.chunks():
            with self.subTest(chunk=chunk[:6]):
                fixture = ExceptionCoreFixture(chunk, SR_FR | 0xFF01)
                fixture.context()
                self.assertEqual(bytes(fixture.memory[fixture.OUTPUT + i]
                                       for i in range(len(expected))), expected)
                self.assertEqual([fixture.fpr_value(i) for i in range(32)],
                                 fixture.initial_fprs)
                cells = [(fpr, CALLER_SP + index * 8)
                         for index, fpr in enumerate(SAVED_FPRS)]
                self.assertEqual(fixture.fpr_stores, cells)
                self.assertEqual(fixture.fpr_loads, cells)
                for fpr, address in cells:
                    self.assertEqual(fixture.get(address, 8),
                                     fixture.initial_fprs[fpr][0])
                self.assertEqual(fixture.status_writes,
                                 [fixture.initial_status | SR_CU1,
                                  fixture.initial_status])
                self.assert_gpr_context(fixture)

    def test_cu1_set_unconditional_f0_load_uses_stale_slot(self):
        for stale in (0xABCDEF0187654321, 0x123456789ABCDEF0):
            fixture = ExceptionCoreFixture(self.chunks()[1][0],
                                           SR_FR | SR_CU1 | 0xFF01, stale)
            fixture.context()
            self.assertEqual(fixture.fpr_stores, [])
            self.assertEqual(fixture.fpr_loads, [(0, CALLER_SP)])
            self.assertEqual(fixture.fpr_value(0), (stale, 0xFFFFFFFFFFFFFFFF))
            self.assertFalse(any(address <= CALLER_SP < address + size
                                 for address, size in fixture.writes))
            for index in set(fixture.fpr_moves) - {0}:
                self.assertEqual(fixture.fpr_value(index)[1], 0xFFFFFFFF)
            for index in set(range(32)) - set(fixture.fpr_moves) - {0}:
                self.assertEqual(fixture.fpr_value(index), fixture.initial_fprs[index])
            self.assertEqual(fixture.status_writes, [fixture.initial_status])
            self.assert_gpr_context(fixture)

    def test_core_arguments_and_result_before_gpr_restore(self):
        fixture = ExceptionCoreFixture(self.chunks()[1][0], SR_FR)
        fixture.context()
        registers, _ = fixture.snapshots[0x1000625C]
        self.assertEqual(registers[4:7], [INPUT, fixture.OUTPUT, WORKSPACE])
        self.assertEqual(registers[29], CALLER_SP)
        registers, fprs = fixture.snapshots[0x10005F34]
        self.assertEqual(registers[2], 1)
        self.assertEqual(fprs[17], 1)
        self.assertEqual(registers[29], CALLER_SP)

    def test_fr0_is_explicitly_rejected(self):
        for status in (0, SR_CU1):
            with self.assertRaisesRegex(ValueError, "FR=1"):
                ExceptionCoreFixture(self.chunks()[0][0], status)

    def test_failure_paths_restore_context_without_output(self):
        raws = (b"\x11\x72\x07",
                b"\x11\x72" + streams.InitDecompressorStreamTests().dynamic(
                    overflow=True))
        for raw in raws:
            for cu1 in (0, SR_CU1):
                with self.subTest(raw=raw[:6], cu1=cu1):
                    fixture = ExceptionCoreFixture(raw, SR_FR | cu1)
                    fixture.context()
                    registers, fprs = fixture.snapshots[0x10005F34]
                    self.assertEqual(registers[2], 0)
                    self.assertEqual(fprs[17], 0)
                    self.assertFalse(any(fixture.OUTPUT <= address <
                                         fixture.OUTPUT + 0x1000
                                         for address, _ in fixture.writes))
                    if not cu1:
                        self.assertEqual([fixture.fpr_value(i) for i in range(32)],
                                         fixture.initial_fprs)
                    self.assert_gpr_context(fixture)

    def test_cop1_disabled_and_unaligned_access_rejected(self):
        fixture = ExceptionCoreFixture(self.chunks()[0][0], SR_FR)
        with self.assertRaisesRegex(AssertionError, "CU1 disabled"):
            fixture.execute(0x44858000)
        fixture.status |= SR_CU1
        fixture.registers[29] = CALLER_SP + 1
        with self.assertRaisesRegex(AssertionError, "Unaligned"):
            fixture.execute(0xF7A00000)

    def test_mtc1_high_word_is_unknown_until_full_reload(self):
        fixture = ExceptionCoreFixture(self.chunks()[0][0], SR_FR | SR_CU1)
        fixture.registers[29] = CALLER_SP
        fixture.registers[5] = 0x12345678
        fixture.execute(0x44858000)
        self.assertEqual(fixture.fpr_value(16), (0x12345678, 0xFFFFFFFF))
        with self.assertRaisesRegex(AssertionError, "Unknown FPR"):
            fixture.execute(0xF7B00000)
        fixture.put(CALLER_SP, 0xAABBCCDD11223344, 8)
        fixture.execute(0xD7B00000)
        self.assertEqual(fixture.fpr_value(16),
                         (0xAABBCCDD11223344, 0xFFFFFFFFFFFFFFFF))


if __name__ == "__main__":
    unittest.main()
