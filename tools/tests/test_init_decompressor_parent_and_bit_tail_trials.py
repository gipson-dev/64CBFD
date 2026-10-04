"""Qualify isolated fitting trials; neither replaces the production decoder."""

import subprocess
import sys
import unittest

from tools.tests import test_init_decompressor_aligned_entry as aligned
from tools.tests import test_init_decompressor_distance_operation_local as distance
from tools.tests import test_init_decompressor_semantic as semantic
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture
from tools.tests.test_init_decompressor_tables import BuilderFixture


class InitDecompressorPackedParentTests(distance.InitDecompressorDistanceOperationLocalTests):
    shadow_extra_flags = (*distance.InitDecompressorDistanceOperationLocalTests.shadow_extra_flags,
                          "--packed-parent")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound, words, frame in (
                ("o2g3", 4352, 400, 337, 200), ("o1", 5808, 360, 489, 120)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["entry_layout"], [4, 4, 0, 1, 2])
            builder = next(row for row in receipt["functions"]
                           if row["function"] == "init_decode_build")
            self.assertEqual((builder["public_unit_words"], builder["frame_bytes"]),
                             (words, frame))
            core = next(row for row in receipt["call_graph"]
                        if row["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 176)
            self.assertGreater(len(image.code) * 4, 3984)

    def test_parent_word_stores_preserve_all_retail_table_bytes(self):
        for lengths, bits in (([1, 2, 3, 3], 1),
                              (list(range(1, 16)) + [16, 16], 1)):
            reference = BuilderFixture(lengths, bits=bits, allocated=11)
            expected = reference.run()
            parents = {address for address, size in reference.writes
                       if size == 1 and reference.WORKSPACE <= address < reference.ROOT
                       and address & 3 == 0}
            self.assertGreater(len(parents), 0)
            end = reference.WORKSPACE + reference.fprs[19] * 4
            for label, profile, image in self.adapter_images:
                with self.subTest(shape=label, profile=profile, depth=max(lengths)):
                    guest = GuestBuilderFixture(image, lengths, bits=bits, allocated=11)
                    self.assertEqual(guest.run(), expected)
                    word_stores = {address for address, size in guest.writes if size == 4}
                    self.assertTrue(parents <= word_stores)
                    for address, value in reference.memory.items():
                        if reference.WORKSPACE <= address < end:
                            self.assertEqual(guest.memory[address], value, hex(address))
                    self.assertEqual(bytes(guest.memory[end + i] for i in range(16)),
                                     b"\xa5" * 16)


class InitDecompressorInlineBitTailTests(distance.InitDecompressorDistanceOperationLocalTests):
    shadow_extra_flags = (*distance.InitDecompressorDistanceOperationLocalTests.shadow_extra_flags,
                          "--inline-bit-tail")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound, core_words, helper_words in (
                ("o2g3", 4368, 400, 53, 61), ("o1", 5840, 360, 89, 65)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["retail_slot_ledger"]["c_helper_words"], helper_words)
            core = next(row for row in receipt["call_graph"]
                        if row["name"] == "init_decode_core")
            self.assertEqual((core["slot_words"], core["direct_call_frame_bound"]),
                             (core_words, bound))
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 176)
            self.assertGreater(len(image.code) * 4, 3984)

    def test_alternative_bit_shapes_are_rejected_together(self):
        result = subprocess.run([sys.executable,
            str(self.root / "tools/experiments/compile_init_decompressor.py"),
            "--inline-bit-tail", "--flat-bits"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("alternative take_bits shapes", result.stderr)


class InitDecompressorNativePackedParentTests(aligned.EntryAlignmentChecks,
                                              semantic.InitDecompressorSemanticTests):
    compiler_flags = ("-DINIT_DECODE_ALIGNED_ENTRY", "-DINIT_DECODE_PACKED_PARENT")


if __name__ == "__main__":
    unittest.main()
