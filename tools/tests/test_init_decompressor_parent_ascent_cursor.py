import unittest

from tools.tests import test_init_decompressor_builder_code_toggle as toggle
from tools.tests import test_init_decompressor_core_owned_state as owned
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture


class InitDecompressorParentAscentCursorTests(toggle.InitDecompressorBuilderCodeToggleTests):
    shadow_extra_flags = (*toggle.InitDecompressorBuilderCodeToggleTests.shadow_extra_flags,
                          "--parent-ascent-cursor")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound, words, frame in (
                ("o2g3", 4416, 392, 336, 200), ("o1", 5840, 352, 497, 120)):
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

    def test_parent_offsets_descend_to_root_without_underflow(self):
        for lengths in ([1, 2, 3, 3], list(range(1, 16)) + [16, 16]):
            for label, profile, image in self.adapter_images:
                class AscentFixture(GuestBuilderFixture):
                    def __init__(self, *args, **kwargs):
                        self.offset_reads = []
                        self.watch_offsets = False
                        super().__init__(*args, **kwargs)
                        self.watch_offsets = True

                    def get(self, address, size):
                        if self.watch_offsets and size == 4 and address == self.FRAME + 0x500:
                            raise AssertionError("parent read below offset root")
                        value = super().get(address, size)
                        if self.watch_offsets and size == 4:
                            if self.FRAME + 0x504 <= address < self.FRAME + 0x548:
                                self.offset_reads.append((address, value))
                        return value

                with self.subTest(shape=label, profile=profile, depth=max(lengths)):
                    guest = AscentFixture(image, lengths, bits=1)
                    guest.run()
                    root = guest.FRAME + 0x504
                    self.assertIn((root, 0), guest.offset_reads)
                    self.assertTrue(any(left[0] == root + 4 and right == (root, 0)
                                        for left, right in zip(guest.offset_reads,
                                                               guest.offset_reads[1:])))
                    with self.assertRaisesRegex(AssertionError, "below offset root"):
                        guest.get(root - 4, 4)


class InitDecompressorParentAscentCursorCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorParentAscentCursorTests.shadow_extra_flags
    shadow_adapter_flags = owned.InitDecompressorCoreOwnedStateTests.shadow_adapter_flags
    fixture_type = owned.CoreOwnedStateFixture


if __name__ == "__main__":
    unittest.main()
