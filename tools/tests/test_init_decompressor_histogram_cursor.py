import unittest

from tools.tests import test_init_decompressor_loop_lookup as lookup
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_guest_builder as builder


class InitDecompressorHistogramCursorTests(lookup.InitDecompressorLoopLookupTests):
    shadow_extra_flags = ("--loop-lookup", "--builder-histogram-cursor")

    def test_direct_builder_cursor_boundaries(self):
        self.images = [
            (label, profile, image, next(unit["direct_call_frame_bound"]
             for unit in self.receipts[label, profile]["call_graph"]
             if unit["name"] == "init_decode_build"))
            for label, profile, image in self.adapter_images
        ]
        cases = (([], 7, 9), ([0] * 19, 7, 9), ([1, 1], 1, 0),
                 ([2, 2], 2, 0), ([1], 7, 0), ([1, 2, 2], 1, 0),
                 ([1, 2, 3, 3], 1, 11), ([1, 2, 3, 3], 2, 11),
                 ([1, 1, 1], 1, 0), ([2] * 5, 2, 0),
                 ([0] * 288, 9, 0), ([0] * 286 + [1, 1], 9, 0),
                 ([8] * 144 + [9] * 112 + [7] * 24 + [8] * 8, 9, 0))
        for lengths, bits, allocated in cases:
            builder.InitDecompressorCompiledGuestBuilderTests.compare(
                self, lengths, bits=bits, allocated=allocated)
        for bits in (0, 1, 4, 7, 9):
            builder.InitDecompressorCompiledGuestBuilderTests.compare(
                self, list(range(1, 16)) + [16, 16], bits=bits)
        builder.InitDecompressorCompiledGuestBuilderTests.compare(
            self, [1, 2, 3, 3], bits=1, simple=2, bases=(32, 64), extras=(5, 7))

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4544, 408), ("o1", 5920, 344)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 320)


class InitDecompressorHistogramCursorCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = ("--loop-lookup", "--builder-histogram-cursor")


if __name__ == "__main__":
    unittest.main()
