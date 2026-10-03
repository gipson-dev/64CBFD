import unittest

from tools.tests import test_init_decompressor_guest_builder as builder
from tools.tests import test_init_decompressor_retail_pages as retail
from tools.tests.init_decompressor_guest_oracle import GuestStreamFixture
from tools.tests.test_init_decompressor_streams import StreamFixture


class GuestRetailPageFixture(GuestStreamFixture):
    INPUT = retail.INPUT
    OUTPUT = 0x80050000
    WORKSPACE = retail.WORKSPACE
    WORKSPACE_CAPACITY = 0x1000
    STACK = retail.CALLER_SP


class InitDecompressorCompiledGuestRetailPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        builder.InitDecompressorCompiledGuestBuilderTests.setUpClass.__func__(cls)
        retail.InitDecompressorRetailPageTests.setUpClass.__func__(cls)

    def test_representative_pages_with_explicit_capacities(self):
        for index in (0, 169, 506):
            _, start, end, chunk, expected = self.pages[index]
            dma_size = (end - start + 15) & ~15
            supplied = self.rom[start:start + dma_size]
            self.assertEqual(supplied[:len(chunk)], chunk)
            for label, profile, image, _ in self.images:
                with self.subTest(page=index, shape=label, profile=profile):
                    guest = GuestRetailPageFixture(image, supplied)
                    self.assertEqual(guest.WORKSPACE_CAPACITY, 4096)
                    self.assertEqual(guest.OUTPUT_CAPACITY, 65536)
                    self.assertEqual(guest.core(), len(expected))
                    self.assertEqual(bytes(guest.memory[guest.OUTPUT + i]
                                           for i in range(len(expected))), expected)
                    for first, last in ((guest.WORKSPACE - 16, guest.WORKSPACE),
                                        (guest.WORKSPACE + 4096, guest.WORKSPACE + 4112)):
                        self.assertEqual(bytes(guest.memory[address] for address in range(first, last)),
                                         b"\xa5" * (last - first))
                    reads = [address + size - retail.INPUT for address, size in guest.reads
                             if retail.INPUT <= address < retail.WORKSPACE]
                    self.assertLessEqual(max(reads, default=0), dma_size)

    def test_all_507_pages_through_six_compiled_guest_cores(self):
        self.assertEqual(len(self.pages), 507)
        self.assertEqual(len(self.images), 6)
        completed, maximum_workspace, maximum_read, maximum_dma = 0, 0, 0, 0
        for index, start, end, chunk, expected in self.pages:
            offset = 0x2D4B0 + index * 0x1000
            self.assertEqual(expected, self.image[offset:offset + len(expected)])
            dma_size = (end - start + 15) & ~15
            supplied = self.rom[start:start + dma_size]
            self.assertEqual(supplied[:len(chunk)], chunk)
            maximum_dma = max(maximum_dma, dma_size)
            reference = StreamFixture(chunk)
            reference.INPUT, reference.OUTPUT = retail.INPUT, GuestRetailPageFixture.OUTPUT
            reference.WORKSPACE = retail.WORKSPACE
            reference.registers[29] = retail.CALLER_SP
            reference_frame = retail.CALLER_SP - 0xA88
            reference.memory.update((reference_frame + i, 0xA5) for i in range(0xA88))
            reference.memory.update((retail.WORKSPACE + i, 0xA5) for i in range(0x1000))
            reference.memory.update((retail.INPUT + i, value) for i, value in
                                    enumerate(supplied + b"\0" * 16))
            reference.reads, reference.writes = [], []
            reference.capture = {0x100062F0}
            self.assertEqual(reference.core(False), len(expected))
            self.assertEqual(reference.output(), expected)
            registers, _ = reference.snapshots[0x100062F0]
            self.assertEqual(registers[29], reference_frame)
            for label, profile, image, _ in self.images:
                with self.subTest(page=index, shape=label, profile=profile):
                    readonly = tuple(image.readonly)
                    guest = GuestRetailPageFixture(image, supplied)
                    self.assertEqual(tuple(image.readonly), readonly)
                    self.assertEqual(guest.fixed_table, bytes(reference.memory.get(reference.FIXED_BASE + i, 0xA5)
                                                             for i in range(658 * 4)))
                    self.assertEqual(guest.core(), len(expected))
                    self.assertEqual([guest.get(guest.STATE + i * 4, 4) for i in range(10)],
                        [registers[23], reference.OUTPUT, retail.WORKSPACE, registers[28], registers[30],
                         reference.fprs[17], reference.fprs[18], reference.fprs[19], guest.FRAME, retail.WORKSPACE])
                    self.assertEqual(bytes(guest.memory[guest.OUTPUT + i] for i in range(len(expected))), expected)
                    self.assertEqual(bytes(guest.memory[guest.OUTPUT + i] for i in
                                           range(len(expected), guest.OUTPUT_CAPACITY + 16)),
                                     b"\xa5" * (guest.OUTPUT_CAPACITY + 16 - len(expected)))
                    self.assertEqual(bytes(guest.memory[guest.INPUT + i] for i in range(dma_size)), supplied)
                    self.assertEqual(bytes(guest.memory[guest.FRAME + i] for i in range(0xA44)),
                                     bytes(reference.memory[reference_frame + i] for i in range(0xA44)))
                    changed = {current for address, size in (*reference.writes, *guest.writes)
                               if retail.WORKSPACE <= address < retail.WORKSPACE + 0x1000
                               for current in range(address, address + size)}
                    for current in changed:
                        self.assertEqual(guest.memory[current], reference.memory.get(current, 0xA5), hex(current))
                    for register in (*range(16, 24), 28, 29, 30, 31):
                        self.assertEqual(guest.registers[register], guest.before[register])
                    unit = next(unit for unit in self.receipts[label, profile]["call_graph"]
                                if unit["name"] == "init_decode_core")
                    self.assertLessEqual(guest.STACK - guest.min_sp, unit["direct_call_frame_bound"])
                    for first, last in ((guest.FRAME - 16, guest.FRAME),
                                        (guest.FRAME + 0xA44, guest.FRAME + 0xA88 + 16),
                                        (guest.OUTPUT - 16, guest.OUTPUT),
                                        (guest.WORKSPACE - 16, guest.WORKSPACE),
                                        (guest.WORKSPACE + 0x1000, guest.WORKSPACE + 0x1010)):
                        self.assertEqual(bytes(guest.memory[address] for address in range(first, last)),
                                         b"\xa5" * (last - first))
                    reads = [address + size - retail.INPUT for address, size in guest.reads
                             if retail.INPUT <= address < retail.WORKSPACE]
                    self.assertLessEqual(max(reads, default=0), dma_size)
                    maximum_read = max(maximum_read, max(reads, default=0))
                    span = max((address + size - retail.WORKSPACE for address, size in guest.writes
                                if retail.WORKSPACE <= address < retail.WORKSPACE + 0x1000), default=0)
                    maximum_workspace = max(maximum_workspace, span)
                    self.assertGreater(guest.visits.get(image.symbols["init_decode_core"], 0), 0)
                    self.assertGreater(guest.visits.get(image.symbols["init_decode_stream"], 0), 0)
                    completed += 1
            if (index + 1) % 32 == 0 or index == 506:
                print("guest retail pages: %d/507; compiled runs: %d/3042" % (index + 1, completed), flush=True)
        self.assertEqual(completed, 3042)
        self.assertEqual(maximum_workspace, 3564)
        self.assertEqual(maximum_dma, 3072)
        print("guest retail terminal: runs=%d max_workspace=%d max_input_read=%d max_dma=%d" %
              (completed, maximum_workspace, maximum_read, maximum_dma), flush=True)


if __name__ == "__main__":
    unittest.main()
