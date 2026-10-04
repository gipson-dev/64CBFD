import subprocess
import sys
import unittest

from tools.tests import test_init_decompressor_live_stack_writes as live
from tools.tests.test_init_decompressor_tables import BuilderFixture
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture


class InitDecompressorBuilderScanDeficitTests(live.InitDecompressorLiveStackWriteTests):
    shadow_extra_flags = (*live.InitDecompressorLiveStackWriteTests.shadow_extra_flags,
                          "--bounded-builder-shifts",
                          "--builder-scan-deficit")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound, words, frame in (
                ("o2g3", 4384, 392, 333, 200), ("o1", 5792, 352, 488, 120)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            builder = next(unit for unit in receipt["functions"]
                           if unit["function"] == "init_decode_build")
            self.assertEqual((builder["public_unit_words"], builder["frame_bytes"]),
                             (words, frame))
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 192)

    def test_scan_deficit_requires_bounded_shifts(self):
        result = subprocess.run([sys.executable,
            str(self.root / "tools/experiments/compile_init_decompressor.py"),
            "--builder-scan-deficit"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--builder-scan-deficit requires --bounded-builder-shifts",
                      result.stderr)

    def test_signed_deficit_matches_unsigned_scan_domain(self):
        # Scan buckets precede max, so none contains the rewritten max count.
        for slots in range(1, 65537):
            counts = {0, 1, 288, min(slots, 288), min(slots - 1, 288),
                      min(slots + 1, 288)}
            for count in counts:
                wrapped = (slots - count) & 0xFFFFFFFF
                signed = wrapped if wrapped < 0x80000000 else wrapped - 0x100000000
                self.assertEqual(signed <= 0, count >= slots)
                if count < slots:
                    self.assertEqual(wrapped, slots - count)

    def test_compiled_deficit_branch_is_executed(self):
        lengths = list(range(1, 16)) + [16, 16]
        reference = BuilderFixture(lengths, bits=7)
        expected = reference.run()
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile):
                unit = next(unit for unit in self.receipts[label, profile]["functions"]
                            if unit["function"] == "init_decode_build")
                start = image.symbols["init_decode_build"]
                end = start + unit["public_unit_words"] * 4
                branches = [pc for pc, word in image.code.items()
                            if start <= pc < end and word >> 26 in (6, 22)]
                self.assertEqual(len(branches), 1)
                guest = GuestBuilderFixture(image, lengths, bits=7)
                self.assertEqual(guest.run(), expected)
                self.assertGreater(guest.visits.get(branches[0], 0), 0)


class InitDecompressorBuilderScanDeficitCorpusTests(live.InitDecompressorLiveStackWriteCorpusTests):
    shadow_extra_flags = InitDecompressorBuilderScanDeficitTests.shadow_extra_flags


if __name__ == "__main__":
    unittest.main()
