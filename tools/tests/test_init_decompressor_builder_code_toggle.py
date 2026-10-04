import unittest

from tools.tests import test_init_decompressor_builder_offset_sum as offsets
from tools.tests import test_init_decompressor_core_owned_state as owned
from tools.tests import test_init_decompressor_shadow_corpus as corpus


class InitDecompressorBuilderCodeToggleTests(offsets.InitDecompressorBuilderOffsetSumTests):
    shadow_extra_flags = (*offsets.InitDecompressorBuilderOffsetSumTests.shadow_extra_flags,
                          "--builder-code-toggle")

    def test_exhaustive_reversed_code_increment_widths(self):
        checked = 0
        for width in range(1, 17):
            for code in range(1 << width):
                original, mask = code, 1 << (width - 1)
                while original & mask:
                    original ^= mask
                    mask >>= 1
                original ^= mask
                original_mask = mask
                toggled, mask = code, 1 << (width - 1)
                while True:
                    toggled ^= mask
                    if toggled & mask:
                        break
                    mask >>= 1
                    if not mask:
                        break
                self.assertEqual((toggled, mask), (original, original_mask), (width, code))
                checked += 1
        self.assertEqual(checked, 131070)

    def test_packed_profile_size_reduction(self):
        for profile, text, bound, words, frame in (
                ("o2g3", 4432, 392, 338, 200), ("o1", 5840, 352, 496, 120)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            builder = next(row for row in receipt["functions"]
                           if row["function"] == "init_decode_build")
            self.assertEqual((builder["public_unit_words"], builder["frame_bytes"]),
                             (words, frame))
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 304)


class InitDecompressorBuilderCodeToggleCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorBuilderCodeToggleTests.shadow_extra_flags
    shadow_adapter_flags = owned.InitDecompressorCoreOwnedStateTests.shadow_adapter_flags
    fixture_type = owned.CoreOwnedStateFixture


if __name__ == "__main__":
    unittest.main()
