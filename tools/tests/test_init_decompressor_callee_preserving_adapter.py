import unittest

from tools.tests import test_init_decompressor_lookup_first_refill as refill
from tools.tests import test_init_decompressor_core_owned_state as owned
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_exception as exception


class CalleePreservingFixture(owned.CoreOwnedStateFixture):
    CALLEE_REGISTERS = (*range(16, 24), 28, 30)

    def __init__(self, image, chunk, status):
        super().__init__(image, chunk, status)
        self.adapter_entry = image.symbols["init_decode_retail_core_adapter"]
        end = image.symbols["init_decode_retail_core_adapter_end"]
        core = image.symbols["init_decode_core"]
        calls = [pc for pc, word in image.code.items()
                 if self.adapter_entry <= pc < end and word >> 26 == 3
                 and ((pc + 4) & 0xF0000000 | (word & 0x03FFFFFF) << 2) == core]
        if len(calls) != 1:
            raise AssertionError("one direct adapter-to-core call required")
        self.core_return = calls[0] + 8
        self.capture.add(self.core_return)

    def assert_callee_contract(self):
        incoming = self.snapshots[self.adapter_entry][0]
        returned = self.snapshots[self.core_return][0]
        for register in self.CALLEE_REGISTERS:
            if returned[register] != incoming[register]:
                raise AssertionError("core changed callee register %d" % register)

    def context(self):
        result = super().context()
        self.assert_callee_contract()
        return result


class InitDecompressorCalleePreservingAdapterTests(refill.InitDecompressorLookupFirstRefillTests):
    shadow_adapter_flags = (*owned.InitDecompressorCoreOwnedStateTests.shadow_adapter_flags,
                            "--defsym", "INIT_DECODE_CORE_PRESERVES_CALLEE=1")
    shadow_adapter_bytes = 256
    fixture_type = CalleePreservingFixture

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4384, 392), ("o1", 5824, 352)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 256)

    def test_removed_reloads_and_active_callee_receipt_guard(self):
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile):
                entry = image.symbols["init_decode_retail_core_adapter"]
                end = image.symbols["init_decode_retail_core_adapter_end"]
                words = [word for pc, word in image.code.items() if entry <= pc < end]
                for register in CalleePreservingFixture.CALLEE_REGISTERS:
                    self.assertFalse(any(word >> 26 == 35 and (word >> 21) & 31 == 29
                        and (word >> 16) & 31 == register for word in words))
                    self.assertTrue(any(word >> 26 == 43 and (word >> 21) & 31 == 29
                        and (word >> 16) & 31 == register for word in words))
                guest = self.fixture_type(image, b"\x11\x72\x01\0\0\xff\xff",
                    exception.SR_FR | 0xFF00)
                guest.context()
                core = image.symbols["init_decode_core"]
                returns = [pc for pc, word in image.code.items()
                           if core <= pc < entry and word == 0x03E00008]
                self.assertEqual(len(returns), 1)
                self.assertEqual(image.code[returns[0] + 4], 0)
                incoming = guest.snapshots[entry][0][16]
                corrupt = 0x1235 if incoming == 0x1234 else 0x1234
                broken = self.fixture_type(image, b"\x11\x72\x01\0\0\xff\xff",
                    exception.SR_FR | 0xFF00)
                broken.code[returns[0] + 4] = 0x34100000 | corrupt
                with self.assertRaisesRegex(AssertionError, "core changed callee register 16"):
                    broken.context()


class InitDecompressorCalleePreservingAdapterCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = refill.InitDecompressorLookupFirstRefillTests.shadow_extra_flags
    shadow_adapter_flags = InitDecompressorCalleePreservingAdapterTests.shadow_adapter_flags
    fixture_type = CalleePreservingFixture


if __name__ == "__main__":
    unittest.main()
