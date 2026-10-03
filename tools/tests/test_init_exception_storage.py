import os
import struct
import tempfile
import unittest

from tools.experiments import qualify_init_exception_storage as storage
from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_retail_pages as pages


class InitExceptionStorageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract.InitDecompressorContractTests.setUpClass.__func__(
            contract.InitDecompressorContractTests)

    def test_retail_thread_context_extends_through_32_full_fprs(self):
        save = dict(contract.InitDecompressorContractTests.entries("func_100071D0"))
        restore = dict(contract.InitDecompressorContractTests.entries("func_10007A38"))
        for fpr in range(32):
            offset = 0x130 + fpr * 8
            self.assertEqual(save[0x1000736C + fpr * 4],
                             (61 << 26) | (26 << 21) | (fpr << 16) | offset)
            self.assertEqual(restore[0x10007B2C + fpr * 4],
                             (53 << 26) | (26 << 21) | (fpr << 16) | offset)
        self.assertEqual(0x130 + 32 * 8, 0x230)
        self.assertEqual(0x800318B0 + 0x230, 0x80031AE0)
        self.assertEqual(0x80031AE0 + 0x230, 0x80031D10)

    def test_current_sdk_guest_layout_receipt(self):
        compiler = storage.ROOT / "ido/ido5.3_recomp/cc"
        if os.name != "posix" or not compiler.exists():
            self.skipTest("The isolated guest layout probe requires WSL/IDO")
        with tempfile.TemporaryDirectory(prefix="init-thread-layout-") as directory:
            layout = storage.compile_layout(storage.Path(directory))
        self.assertEqual(layout, {
            "thread_bytes": 0x1B0, "context_offset": 0x20,
            "fp0_offset": 0x130, "fp30_offset": 0x1A8})

    def test_page_table_rounded_dma_meets_input_boundary(self):
        count = pages.PAGE_COUNT
        self.assertEqual(count, 507)
        dma = ((count + 2) * 4 + 15) & ~15
        self.assertEqual(dma, 0x800)
        self.assertEqual(0x80032B30 + dma, pages.INPUT)
        self.assertEqual(0x80032B30 + (count + 1) * 4, 0x80033320)
        image = contract.InitDecompressorContractTests.project / "conker.us.bin"
        if not image.exists():
            self.skipTest("Pristine startup words required")
        data = image.read_bytes()
        for offset, word in ((0x1354, 0x27392B30), (0x1358, 0x25E60002),
                             (0x1360, 0x0006C080), (0x1368, 0x2706000F),
                             (0x1378, 0x34D9000F), (0x1380, 0x3B26000F)):
            self.assertEqual(struct.unpack_from(">I", data, offset)[0], word)

    def test_known_thread_extent_and_gap_not_written_by_wrapper(self):
        start, end = 0x80031AE0, pages.CALLER_SP - 0xA88
        for chunk, _ in exception.InitDecompressorExceptionTests.chunks():
            for cu1 in (0, exception.SR_CU1):
                fixture = exception.ExceptionCoreFixture(chunk, exception.SR_FR | cu1)
                sentinel = bytes((index * 17 + 3) & 0xFF for index in range(end - start))
                fixture.memory.update({start + i: byte for i, byte in enumerate(sentinel)})
                fixture.context()
                self.assertEqual(bytes(fixture.memory[start + i]
                                       for i in range(len(sentinel))), sentinel)
                self.assertFalse(any(address < end and address + size > start
                                     for address, size in fixture.writes))
        self.assertEqual(end - 0x80031D10, 632)

    def test_observed_write_fence_accepts_exact_ends(self):
        low = pages.CALLER_SP - 0xA88
        storage.validate_observed_writes(
            [(low, 4), (pages.CALLER_SP - 4, 4), (pages.WORKSPACE, 4),
             (0x800354F4, 4), (0x80050000, 4), (0x8005000C, 4)], 0x80050000, 16)

    def test_observed_write_fence_rejects_crossings_and_input(self):
        for write in ((pages.CALLER_SP - 0xA88 - 1, 4), (pages.CALLER_SP - 1, 4),
                      (pages.INPUT, 4), (pages.WORKSPACE - 1, 4), (0x800354F7, 4),
                      (0x8005000D, 4), (pages.WORKSPACE, 0)):
            with self.subTest(write=write):
                with self.assertRaisesRegex(ValueError, "outside observed"):
                    storage.validate_observed_writes([write], 0x80050000, 16)


if __name__ == "__main__":
    unittest.main()
