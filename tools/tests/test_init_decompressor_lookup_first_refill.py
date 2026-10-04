import subprocess
import sys
import unittest

from tools.tests import test_init_decompressor_builder_allocation_table as allocation
from tools.tests import test_init_decompressor_core_owned_state as owned
from tools.tests import test_init_decompressor_shadow_corpus as corpus


class InitDecompressorLookupFirstRefillTests(allocation.InitDecompressorBuilderAllocationTableTests):
    shadow_extra_flags = (*allocation.InitDecompressorBuilderAllocationTableTests.shadow_extra_flags,
                          "--lookup-first-refill")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound, words, frame in (
                ("o2g3", 4384, 392, 333, 200), ("o1", 5824, 352, 496, 120)):
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

    def test_first_refill_requires_shared_loop(self):
        result = subprocess.run([sys.executable,
            str(self.root / "tools/experiments/compile_init_decompressor.py"),
            "--lookup-first-refill"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--lookup-first-refill requires --loop-lookup", result.stderr)


class InitDecompressorLookupFirstRefillCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorLookupFirstRefillTests.shadow_extra_flags
    shadow_adapter_flags = owned.InitDecompressorCoreOwnedStateTests.shadow_adapter_flags
    fixture_type = owned.CoreOwnedStateFixture


if __name__ == "__main__":
    unittest.main()
