import unittest

from tools.tests import test_init_decompressor_abi_seed_cursor as seed
from tools.tests import test_init_decompressor_core_owned_state as owned
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_guest_builder as builder
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture


class InitDecompressorSimpleSeedCombinationTests(seed.InitDecompressorAbiSeedCursorTests):
    shadow_extra_flags = (*seed.InitDecompressorAbiSeedCursorTests.shadow_extra_flags,
                          "--builder-simple-operation")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4464, 392), ("o1", 5888, 352)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 304)

    def test_simple_symbol_boundary_and_signed_stale_word(self):
        self.images = [
            (label, profile, image, next(unit["direct_call_frame_bound"]
             for unit in self.receipts[label, profile]["call_graph"]
             if unit["name"] == "init_decode_build"))
            for label, profile, image in self.adapter_images
        ]
        cases = (([0] * 254 + [1, 1], 1, 257, ((16, 254), (16, 255))),
                 ([0] * 255 + [1, 1], 1, 257, ((16, 255), (15, 256))),
                 ([0, 2, 2], 2, 3, ((16, 1), (16, 0xA5A5), (16, 2), (99, 0xA5A5))))
        for lengths, bits, simple, expected in cases:
            builder.InitDecompressorCompiledGuestBuilderTests.compare(
                self, lengths, bits=bits, simple=simple)
            for label, profile, image, _ in self.images:
                with self.subTest(shape=label, profile=profile, count=len(lengths)):
                    guest = GuestBuilderFixture(image, lengths, bits=bits, simple=simple)
                    guest.run()
                    root = guest.get(guest.ROOT, 2)
                    entries = [(guest.get(guest.WORKSPACE + (root + i) * 4, 1),
                                guest.get(guest.WORKSPACE + (root + i) * 4 + 2, 2))
                               for i in range(len(expected))]
                    self.assertEqual(entries, list(expected))


class InitDecompressorSimpleSeedCombinationCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorSimpleSeedCombinationTests.shadow_extra_flags
    shadow_adapter_flags = owned.InitDecompressorCoreOwnedStateTests.shadow_adapter_flags
    fixture_type = owned.CoreOwnedStateFixture


if __name__ == "__main__":
    unittest.main()
