import unittest

from tools.tests import test_init_decompressor_dynamic_repeat_fill as fill
from tools.tests import test_init_decompressor_core_owned_state as owned
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture


class InitDecompressorBuilderOffsetSumTests(fill.InitDecompressorDynamicRepeatFillTests):
    shadow_extra_flags = (*fill.InitDecompressorDynamicRepeatFillTests.shadow_extra_flags,
                          "--builder-offset-sum")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4432, 392), ("o1", 5856, 352)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            builder = next(row for row in receipt["functions"]
                           if row["function"] == "init_decode_build")
            self.assertEqual(builder["frame_bytes"], 200 if profile == "o2g3" else 120)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 304)

    def test_ordered_prefix_offsets_at_depth_boundaries(self):
        cases = ([1, 1], [1, 2, 3, 3], [0, 2, 2],
                 list(range(1, 16)) + [16, 16])
        for lengths in cases:
            maximum = max(lengths)
            counts = [lengths.count(width) for width in range(17)]
            expected = [(0x504 + width * 4, sum(counts[1:width]), 4)
                        for width in range(1, maximum + 1)]
            for label, profile, image in self.adapter_images:
                class OffsetFixture(GuestBuilderFixture):
                    def __init__(self, *args, **kwargs):
                        self.offset_writes = []
                        self.watch_offsets = False
                        super().__init__(*args, **kwargs)
                        self.watch_offsets = True

                    def put(self, address, value, size):
                        super().put(address, value, size)
                        if self.watch_offsets and self.FRAME + 0x504 <= address < self.FRAME + 0x548:
                            self.offset_writes.append((address - self.FRAME, value, size))

                with self.subTest(shape=label, profile=profile, maximum=maximum):
                    guest = OffsetFixture(image, lengths, bits=1)
                    guest.run()
                    self.assertEqual(guest.offset_writes[:maximum], expected)


class InitDecompressorBuilderOffsetSumCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorBuilderOffsetSumTests.shadow_extra_flags
    shadow_adapter_flags = owned.InitDecompressorCoreOwnedStateTests.shadow_adapter_flags
    fixture_type = owned.CoreOwnedStateFixture


if __name__ == "__main__":
    unittest.main()
