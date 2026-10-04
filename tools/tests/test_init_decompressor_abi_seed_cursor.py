import subprocess
import sys
import unittest

from tools.tests import test_init_decompressor_core_owned_state as owned
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_exception as exception


class InitDecompressorAbiSeedCursorTests(owned.InitDecompressorCoreOwnedStateTests):
    shadow_extra_flags = (*owned.InitDecompressorCoreOwnedStateTests.shadow_extra_flags,
                          "--abi-seed-cursor")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4480, 392), ("o1", 5904, 352)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 304)

    def test_seed_copies_six_ordered_saved_register_words(self):
        for label, profile, image in self.adapter_images:
            class SeedFixture(self.fixture_type):
                def __init__(self, *args):
                    self.seed_reads, self.seed_writes = [], []
                    self.watch_seed = False
                    super().__init__(*args)
                    self.watch_seed = True

                def get(self, address, size):
                    value = super().get(address, size)
                    if self.watch_seed and len(self.seed_reads) < 6:
                        if self.FRAME + 0xA48 <= address < self.FRAME + 0xA60:
                            self.seed_reads.append((address, value, size))
                    return value

                def put(self, address, value, size):
                    super().put(address, value, size)
                    if self.watch_seed and len(self.seed_writes) < 6:
                        if self.adapter_state + 40 <= address < self.adapter_state + 64:
                            self.seed_writes.append((address, value, size))

            with self.subTest(shape=label, profile=profile):
                guest = SeedFixture(image, b"\x11\x72\x01\0\0\xff\xff",
                                    exception.SR_FR | exception.SR_CU1 | 0xFF00)
                guest.context()
                self.assertEqual(len(guest.seed_reads), 6)
                self.assertEqual(guest.seed_reads, [
                    (guest.FRAME + 0xA48 + 4 * i, value, 4)
                    for i, (_, value, _) in enumerate(guest.seed_reads)])
                self.assertEqual(guest.seed_writes, [
                    (guest.adapter_state + 40 + 4 * i, value, 4)
                    for i, (_, value, _) in enumerate(guest.seed_reads)])

    def test_seed_cursor_requires_shadow(self):
        result = subprocess.run([sys.executable,
            str(self.root / "tools/experiments/compile_init_decompressor.py"),
            "--abi-seed-cursor"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--abi-seed-cursor requires --abi-fpr-shadow", result.stderr)


class InitDecompressorAbiSeedCursorCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorAbiSeedCursorTests.shadow_extra_flags
    shadow_adapter_flags = owned.InitDecompressorCoreOwnedStateTests.shadow_adapter_flags
    fixture_type = owned.CoreOwnedStateFixture


if __name__ == "__main__":
    unittest.main()
