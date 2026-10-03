import shutil
import struct
import subprocess
import unittest
from pathlib import Path

from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_guest_builder as builder
from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests import test_init_decompressor_retail_pages as retail
from tools.tests import test_init_decompressor_streams as streams
from tools.tests.init_decompressor_guest_oracle import GuestImage, GuestStreamFixture


class GuestExceptionFixture(exception.Fr1ContextTransfers, GuestStreamFixture):
    INPUT = exception.INPUT
    OUTPUT = 0x80050000
    WORKSPACE = exception.WORKSPACE
    WORKSPACE_CAPACITY = 4096
    STACK = 0x10000
    FRAME = exception.CALLER_SP - 0xA88
    ADAPTER_EXTRA = 0x48

    def __init__(self, image, chunk, status):
        if not status & exception.SR_FR:
            raise ValueError("Only FR=1 context is qualified")
        self.context_enabled = False
        super().__init__(image, chunk)
        self.STACK = exception.CALLER_SP
        seed = exception.ExceptionCoreFixture(chunk, status)
        self.code = dict(image.code)
        wrapper = {pc: word for pc, word in
                   exception.contract.InitDecompressorContractTests.entries("func_10005C2C")
                   if exception.ENTRY <= pc < exception.STOP}
        if wrapper[0x10005F2C] != 0x0C001897:
            raise AssertionError("retail core call changed")
        target = image.symbols["init_decode_retail_core_adapter"]
        if target >> 28 != 1 or target & 3:
            raise AssertionError("adapter is outside the retail JAL region")
        wrapper[0x10005F2C] = 0x0C000000 | ((target >> 2) & 0x03FFFFFF)
        self.code.update(wrapper)
        self.readonly.append((exception.ENTRY, exception.STOP))
        self.allowed_writes.append((self.STACK - 4096, exception.CONTEXT_TOP + 4))
        self.memory.update((address, 0xA5) for address in
                           range(self.STACK - 4096, exception.CONTEXT_TOP + 4))
        self.memory.update((address, seed.memory[address]) for address in
                           range(self.FRAME, exception.CONTEXT_TOP + 4))
        self.memory.update((self.WORKSPACE + i, 0xA5) for i in range(4096))
        self.memory.update((0x800354F8 + i, seed.memory[0x800354F8 + i]) for i in range(4))
        self.registers = seed.initial_registers[:]
        self.high, self.fprs = seed.high[:], seed.fprs[:]
        self.status = self.initial_status = status
        self.initial_registers = self.registers[:]
        self.initial_fprs = [self.fpr_value(i) for i in range(32)]
        self.status_writes = []
        self.fpr_loads, self.fpr_stores, self.fpr_moves = [], [], []
        self.reads, self.writes, self.visits = [], [], {}
        self.min_sp = self.stack_low = self.registers[29]
        self.capture = {target, 0x10005F34}
        self.snapshots = {}
        self.adapter_state = self.FRAME - self.ADAPTER_EXTRA + 0x20
        self.context_enabled = True

    def execute(self, word):
        if not self.context_enabled:
            return super().execute(word)
        if not self.execute_context_transfer(word):
            super().execute(word)
        self.stack_low = min(self.stack_low, self.registers[29])

    def context(self):
        return self.run(entry=exception.ENTRY, stop_pc=exception.STOP, budget=2000000)


class InitDecompressorCompiledGuestAdapterTests(unittest.TestCase):
    fixture_type = GuestExceptionFixture
    @classmethod
    def setUpClass(cls):
        if not shutil.which("mips-linux-gnu-as"):
            raise unittest.SkipTest("MIPS assembler is unavailable")
        builder.InitDecompressorCompiledGuestBuilderTests.setUpClass.__func__(cls)
        retail.InitDecompressorRetailPageTests.setUpClass.__func__(cls)
        decoder.InitDecompressorDecoderTests.setUpClass()
        directory = Path(cls.directory.name)
        adapter = directory / "adapter.o"
        result = subprocess.run(["mips-linux-gnu-as", "-mips3", "-32", "-o", str(adapter),
            str(cls.root / "tools/experiments/init_decompressor_core_adapter.s")],
            capture_output=True, text=True, check=True)
        if result.stdout or result.stderr:
            raise AssertionError("adapter assembly log is not empty")
        cls.adapter_images = []
        cls.maximum_depths = {}
        for label, profile, _, _ in cls.images:
            executable = directory / label / (profile + "-adapter.elf")
            result = subprocess.run(["mips-linux-gnu-ld", "-Ttext", "0x10400000",
                "-Tdata", "0x10500000", "-e", "init_decode_build", "-o", str(executable),
                str(directory / label / (profile + ".o")), str(adapter)],
                capture_output=True, text=True, check=True)
            if result.stdout or result.stderr:
                raise AssertionError("adapter link log is not empty")
            image = GuestImage(executable.read_bytes())
            cls.adapter_images.append((label, profile, image))
            cls.maximum_depths[label, profile] = 0

    def compare(self, chunk, status=exception.SR_FR | 0xFF01,
                expected_output=None, expected_result=None, dma_size=None):
        reference = exception.ExceptionCoreFixture(chunk, status)
        reference.memory.update((reference.WORKSPACE + i, 0xA5) for i in range(4096))
        reference.capture.add(0x100062F0)
        reference.context()
        result_registers, result_fprs = reference.snapshots[0x10005F34]
        if expected_result is not None:
            self.assertEqual(result_registers[2], expected_result)
        if expected_output is not None:
            self.assertEqual(result_fprs[17], len(expected_output))
            self.assertEqual(bytes(reference.memory[reference.OUTPUT + i]
                                   for i in range(len(expected_output))), expected_output)
        core_registers, _ = reference.snapshots[0x100062F0]
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile, chunk=chunk[:8]):
                fixture_type = getattr(self, "fixture_type", GuestExceptionFixture)
                guest = fixture_type(image, chunk, status)
                guest.context()
                registers, fprs = guest.snapshots[0x10005F34]
                self.assertEqual(registers[2], result_registers[2])
                self.assertEqual(fprs[16:20], result_fprs[16:20])
                self.assertEqual(guest.registers, reference.registers)
                self.assertEqual(guest.status, reference.status)
                self.assertEqual(guest.status_writes, reference.status_writes)
                self.assertEqual([guest.fpr_value(i) for i in range(32)],
                                 [reference.fpr_value(i) for i in range(32)])
                self.assertEqual(guest.fpr_stores, reference.fpr_stores)
                self.assertEqual(guest.fpr_loads, reference.fpr_loads)
                self.assertEqual([guest.get(guest.adapter_state + i * 4, 4) for i in range(10)],
                    [core_registers[23], guest.OUTPUT, guest.WORKSPACE,
                     core_registers[28], core_registers[30], result_fprs[17],
                     result_fprs[18], result_fprs[19], guest.FRAME, guest.WORKSPACE])
                self.assertEqual(bytes(guest.memory[guest.FRAME + i] for i in range(0xA44)),
                                 bytes(reference.memory[guest.FRAME + i] for i in range(0xA44)))
                changed = {current for address, size in (*reference.writes, *guest.writes)
                           if guest.OUTPUT <= address < guest.OUTPUT + guest.OUTPUT_CAPACITY
                           or guest.WORKSPACE <= address < guest.WORKSPACE + 4096
                           for current in range(address, address + size)}
                for current in changed:
                    self.assertEqual(guest.memory[current], reference.memory.get(current, 0xA5), hex(current))
                cells = range(guest.STACK, exception.CONTEXT_TOP + 4)
                self.assertEqual(bytes(guest.memory[address] for address in cells),
                                 bytes(reference.memory[address] for address in cells))
                bound = next(unit["direct_call_frame_bound"] for unit in
                             self.receipts[label, profile]["call_graph"]
                             if unit["name"] == "init_decode_core")
                self.assertLessEqual(guest.STACK - guest.min_sp, 0xA88 + guest.ADAPTER_EXTRA + bound)
                self.maximum_depths[label, profile] = max(self.maximum_depths[label, profile],
                                                         guest.STACK - guest.min_sp)
                if dma_size is not None:
                    reads = [address + size - guest.INPUT for address, size in guest.reads
                             if guest.INPUT <= address < guest.WORKSPACE]
                    self.assertLessEqual(max(reads, default=0), dma_size)
                self.assertGreater(guest.visits.get(image.symbols["init_decode_retail_core_adapter"], 0), 0)
                self.assertGreater(guest.visits.get(image.symbols["init_decode_core"], 0), 0)
                self.assertNotIn(0x1000625C, guest.visits)

    def test_cu1_clear_success_and_failure_contexts(self):
        cases = [(chunk, output, len(output)) for chunk, output in
                 exception.InitDecompressorExceptionTests.chunks()]
        dynamic = streams.InitDecompressorStreamTests().dynamic
        cases.extend(((b"\x11\x72\x07", b"", 0),
                      (b"\x11\x72" + dynamic(overflow=True), b"", 0),
                      (struct.pack(">I", 2) + b"\x01\x02\0\0\0XY", b"", 0),
                      (b"\x11\x72\x00\x01\0\xfe\xffZ\x07", b"Z", 0),
                      (b"\x11\x72" + decoder.InitDecompressorDecoderTests.encoded(b"Conker"),
                       b"Conker", 6)))
        for chunk, output, result in cases:
            self.compare(chunk, expected_output=output, expected_result=result)

    def test_cu1_set_scratch_fprs_remain_an_explicit_gap(self):
        chunk = exception.InitDecompressorExceptionTests.chunks()[1][0]
        status = exception.SR_FR | exception.SR_CU1 | 0xFF01
        reference = exception.ExceptionCoreFixture(chunk, status)
        reference.context()
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile):
                guest = GuestExceptionFixture(image, chunk, status)
                guest.context()
                self.assertEqual(guest.registers, reference.registers)
                self.assertEqual(guest.fpr_stores, [])
                self.assertEqual(guest.fpr_loads, [(0, guest.STACK)])
                self.assertEqual(guest.fpr_value(0), reference.fpr_value(0))
                self.assertEqual(guest.status, reference.status)
                self.assertEqual(guest.status_writes, reference.status_writes)
                for i in (*range(12, 16), *range(16, 32)):
                    self.assertEqual(guest.fpr_value(i), reference.fpr_value(i))
                different = [i for i in range(1, 12)
                             if guest.fpr_value(i) != reference.fpr_value(i)]
                self.assertTrue(different, "CU1-set compatibility must not be claimed")
                print("adapter CU1-set gap: %s/%s fprs=%s" %
                      (label, profile, different), flush=True)

    def test_representative_retail_pages_through_context_adapter(self):
        for index in (0, 169, 506):
            _, start, end, _, output = self.pages[index]
            dma_size = (end - start + 15) & ~15
            self.compare(self.rom[start:start + dma_size], expected_output=output,
                         expected_result=len(output), dma_size=dma_size)
        for label, profile, image in self.adapter_images:
            adapter_bytes = (image.symbols["init_decode_retail_core_adapter_end"] -
                             image.symbols["init_decode_retail_core_adapter"])
            self.assertGreater(adapter_bytes, 0)
            self.assertEqual(adapter_bytes % 4, 0)
            text_bytes = len(image.code) * 4
            bound = next(unit["direct_call_frame_bound"] for unit in
                         self.receipts[label, profile]["call_graph"]
                         if unit["name"] == "init_decode_core")
            print("adapter receipt: %s/%s body=%d text=%d bound=%d observed=%d" %
                  (label, profile, adapter_bytes, text_bytes, 0xA88 + 0x48 + bound,
                   self.maximum_depths[label, profile]), flush=True)


if __name__ == "__main__":
    unittest.main()
