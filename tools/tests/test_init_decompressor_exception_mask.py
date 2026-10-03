import struct
import unittest

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_guest_fpr_shadow as shadow
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_shadow_corpus as corpus


def status_write(word):
    return word >> 26 == 16 and word >> 21 & 31 == 4 and word >> 11 & 31 == 12


class InitDecompressorExceptionEntryMaskTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract.InitDecompressorContractTests.setUpClass()

    def test_actual_status_mask_prefix_and_wrapper_preserve_disabled_ie(self):
        prefix = {pc: word for pc, word in contract.InitDecompressorContractTests.entries(
                  "func_100071D0") if 0x100071EC <= pc < 0x10007200}
        self.assertEqual(len(prefix), 5)
        for cu1 in (False, True):
            for flags in range(4):
                incoming = exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF00 | flags
                for chunk, output in exception.InitDecompressorExceptionTests.chunks():
                    with self.subTest(cu1=cu1, flags=flags, chunk=chunk[:8]):
                        fixture = exception.ExceptionCoreFixture(chunk, incoming)
                        fixture.code.update(prefix)
                        fixture.registers[26] = 0x80037E40
                        fixture.run(entry=0x100071EC, stop_pc=0x10007200, budget=16)
                        masked = incoming & ~3
                        self.assertEqual(fixture.get(0x80037E40 + 0x118, 4), incoming)
                        self.assertEqual(fixture.status, masked)
                        self.assertEqual(fixture.status_writes, [masked])
                        fixture.status_writes.clear()
                        fixture.context()
                        self.assertEqual(fixture.status, masked)
                        self.assertTrue(all(value & 3 == 0 for value in fixture.status_writes))
                        self.assertEqual(fixture.status_writes,
                                         [masked] if cu1 else [masked | exception.SR_CU1, masked])
                        self.assertEqual(bytes(fixture.memory[fixture.OUTPUT + i]
                                               for i in range(len(output))), output)
                        self.assertEqual(fixture.get(0x80037E40 + 0x118, 4), incoming)

    def test_retail_tlbl_route_and_status_write_sites(self):
        handler = dict(contract.InitDecompressorContractTests.entries("func_100071D0"))
        wrapper = dict(contract.InitDecompressorContractTests.entries("func_10005C2C"))
        self.assertEqual([pc for pc, word in handler.items() if status_write(word)], [0x100071FC])
        self.assertEqual([pc for pc, word in wrapper.items() if status_write(word)],
                         [0x10005ED4, 0x10005F88])
        expected = {0x100071EC: 0x401B6000, 0x100071F0: 0xAF5B0118,
                    0x100071F4: 0x2401FFFC, 0x100071F8: 0x0361D824,
                    0x100071FC: 0x409B6000, 0x100073EC: 0x40086800,
                    0x100073FC: 0x3109007C, 0x10007400: 0x240A0008,
                    0x10007404: 0x112A00C0, 0x10007408: 0,
                    0x10007708: 0x0C00170B, 0x1000770C: 0}
        rom_path = contract.InitDecompressorContractTests.project / "conker.us.bin"
        rom = rom_path.read_bytes() if rom_path.exists() else None
        for pc, word in expected.items():
            self.assertEqual(handler[pc], word)
            if rom is not None:
                self.assertEqual(struct.unpack_from(">I", rom, pc - 0x10000000)[0], word)
        self.assertEqual(0x10007404 + 4 + (handler[0x10007404] & 0xFFFF) * 4, 0x10007708)
        calls = [pc for pc, word in handler.items()
                 if word >> 26 == 3 or (word >> 26 == 0 and word & 63 == 9)]
        self.assertEqual(min(calls), 0x100074A4)
        self.assertFalse(any(pc < 0x10007404 for pc in calls))

    def test_corpus_context_selector_is_explicit(self):
        self.assertEqual(corpus.context_status("generic"), 0x2400FF01)
        self.assertEqual(corpus.context_status("exception-masked"), 0x2400FF00)
        with self.assertRaisesRegex(ValueError, "Unknown shadow corpus context"):
            corpus.context_status("masked-maybe")


class InitDecompressorCompiledMaskedContextTests(unittest.TestCase):
    fixture_type = shadow.ShadowExceptionFixture
    compare_scratch_fprs = True
    compare = shadow.InitDecompressorGuestFprShadowTests.compare

    @classmethod
    def setUpClass(cls):
        shadow.InitDecompressorGuestFprShadowTests.setUpClass.__func__(cls)

    def test_compiled_images_do_not_write_cp0_status(self):
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile):
                self.assertFalse(any(status_write(word) for word in image.code.values()))

    def test_masked_entry_success_and_early_failure(self):
        cases = [*exception.InitDecompressorExceptionTests.chunks(),
                 (b"\x11\x72" + streams.InitDecompressorStreamTests().dynamic(overflow=True), b"")]
        for chunk, output in cases:
            for cu1 in (False, True):
                status = corpus.context_status("exception-masked")
                if not cu1:
                    status &= ~exception.SR_CU1
                self.compare(chunk, status,
                             expected_output=output, expected_result=len(output))

    def test_masked_entry_representative_retail_pages(self):
        for index in (0, 169, 506):
            _, start, end, _, output = self.pages[index]
            dma_size = (end - start + 15) & ~15
            for cu1 in (False, True):
                status = corpus.context_status("exception-masked")
                if not cu1:
                    status &= ~exception.SR_CU1
                self.compare(self.rom[start:start + dma_size], status,
                    expected_output=output, expected_result=len(output), dma_size=dma_size)


if __name__ == "__main__":
    unittest.main()
