import unittest

from tools.tests import test_init_decompressor_parent_ascent_cursor as ascent
from tools.tests import test_init_decompressor_core_owned_state as owned
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests.test_init_decompressor_tables import BuilderFixture
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture


class InitDecompressorBuilderAllocationTableTests(ascent.InitDecompressorParentAscentCursorTests):
    shadow_extra_flags = (*ascent.InitDecompressorParentAscentCursorTests.shadow_extra_flags,
                          "--builder-allocation-table")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound, words, frame in (
                ("o2g3", 4400, 392, 333, 200), ("o1", 5840, 352, 496, 120)):
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

    def test_ordered_allocation_commits_match_retail_counter(self):
        class RetailAllocations(BuilderFixture):
            def __init__(self, *args, **kwargs):
                self.allocation_updates = []
                super().__init__(*args, **kwargs)

            def execute(self, word):
                super().execute(word)
                if word == 0x26730001:
                    self.allocation_updates.append(self.registers[19])

        class GuestAllocations(GuestBuilderFixture):
            def __init__(self, *args, **kwargs):
                self.allocation_updates = []
                self.watch_allocations = False
                super().__init__(*args, **kwargs)
                self.watch_allocations = True

            def put(self, address, value, size):
                super().put(address, value, size)
                if self.watch_allocations and address == self.STATE + 28 and size == 4:
                    self.allocation_updates.append(value)

        for lengths in ([1, 2, 3, 3], list(range(1, 16)) + [16, 16]):
            reference = RetailAllocations(lengths, bits=1, allocated=11)
            self.assertEqual([pc for pc, word in reference.code.items() if word == 0x26730001],
                             [0x10006C38])
            expected = reference.run()
            self.assertGreater(len(reference.allocation_updates), 1)
            for label, profile, image in self.adapter_images:
                with self.subTest(shape=label, profile=profile, depth=max(lengths)):
                    guest = GuestAllocations(image, lengths, bits=1, allocated=11)
                    self.assertEqual(guest.run(), expected)
                    self.assertEqual(guest.allocation_updates, reference.allocation_updates)
                    self.assertEqual(guest.get(guest.STATE + 28, 4), reference.fprs[19])


class InitDecompressorBuilderAllocationTableCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorBuilderAllocationTableTests.shadow_extra_flags
    shadow_adapter_flags = owned.InitDecompressorCoreOwnedStateTests.shadow_adapter_flags
    fixture_type = owned.CoreOwnedStateFixture


if __name__ == "__main__":
    unittest.main()
