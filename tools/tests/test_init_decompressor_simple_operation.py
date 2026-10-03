import unittest

from tools.tests import test_init_decompressor_histogram_cursor as histogram
from tools.tests import test_init_decompressor_shadow_corpus as corpus


class InitDecompressorSimpleOperationTests(histogram.InitDecompressorHistogramCursorTests):
    shadow_extra_flags = ("--loop-lookup", "--builder-histogram-cursor",
                          "--builder-simple-operation")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4544, 408), ("o1", 5904, 344)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 320)


class InitDecompressorSimpleOperationCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = ("--loop-lookup", "--builder-histogram-cursor",
                          "--builder-simple-operation")


if __name__ == "__main__":
    unittest.main()
