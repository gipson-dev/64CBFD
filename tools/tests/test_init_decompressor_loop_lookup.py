import unittest

from tools.tests import test_init_decompressor_exception_mask as mask
from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_guest_fpr_shadow as shadow
from tools.tests import test_init_decompressor_shadow_corpus as corpus


class InitDecompressorLoopLookupTests(shadow.InitDecompressorGuestFprShadowTests):
    shadow_extra_flags = ("--loop-lookup",)
    test_compiled_images_do_not_write_cp0_status = (
        mask.InitDecompressorCompiledMaskedContextTests.test_compiled_images_do_not_write_cp0_status)
    test_masked_entry_success_and_early_failure = (
        mask.InitDecompressorCompiledMaskedContextTests.test_masked_entry_success_and_early_failure)
    test_masked_entry_representative_retail_pages = (
        mask.InitDecompressorCompiledMaskedContextTests.test_masked_entry_representative_retail_pages)

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4560, 408), ("o1", 5936, 336)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 320)

    def test_nested_lookup_path_is_exercised(self):
        receipt = self.receipts["packed-remaining", "o2g3"]
        units = receipt["call_graph"]
        # IDO emits lookup as the last unnamed helper before this public entry.
        index = next(i for i, unit in enumerate(units)
                     if unit["name"] == "init_decode_compressed")
        helper, compressed = units[index - 1], units[index]
        image = next(image for label, profile, image in self.adapter_images
                     if label == "packed-remaining" and profile == "o2g3")
        base = image.symbols["init_decode_compressed"] - compressed["entry"]
        entry, end = base + helper["entry"], base + compressed["entry"]
        backedges = []
        for pc in range(entry, end, 4):
            word = image.code[pc]
            if word >> 16 == 0x1000 and word & 0x8000:
                target = pc + 4 + ((word & 0xFFFF) - 0x10000) * 4
                if entry <= target < pc:
                    backedges.append(target)
        self.assertEqual(len(backedges), 1)
        _, start, last, _, output = self.pages[169]
        dma_size = (last - start + 15) & ~15
        fixture = self.fixture_type(image, self.rom[start:start + dma_size],
                                    exception.SR_FR | exception.SR_CU1 | 0xFF00)
        fixture.context()
        self.assertGreater(fixture.visits.get(entry, 0), 0)
        self.assertGreater(fixture.visits.get(backedges[0], 0), fixture.visits[entry])
        self.assertEqual(bytes(fixture.memory[fixture.OUTPUT + i]
                               for i in range(len(output))), output)
        print("loop lookup nested gate: page=169 calls=%d iterations=%d" %
              (fixture.visits[entry], fixture.visits[backedges[0]]), flush=True)


class InitDecompressorLoopLookupCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = ("--loop-lookup",)


if __name__ == "__main__":
    unittest.main()
