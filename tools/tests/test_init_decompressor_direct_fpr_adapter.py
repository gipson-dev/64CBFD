import unittest

from tools.tests import test_init_decompressor_callee_preserving_adapter as callee
from tools.tests import test_init_decompressor_exception as exception


class InitDecompressorDirectFprAdapterTests(callee.InitDecompressorCalleePreservingAdapterTests):
    shadow_adapter_flags = (*callee.InitDecompressorCalleePreservingAdapterTests.shadow_adapter_flags,
                            "--defsym", "INIT_DECODE_DIRECT_FPR_LOADS=1")
    shadow_adapter_bytes = 192

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4384, 392), ("o1", 5824, 352)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 192)

    def test_direct_load_instruction_and_execution_order(self):
        for label, profile, image in self.adapter_images:
            entry = image.symbols["init_decode_retail_core_adapter"]
            end = image.symbols["init_decode_retail_core_adapter_end"]
            words = [word for pc, word in image.code.items() if entry <= pc < end]
            self.assertEqual(sum(word >> 26 == 49 for word in words), 16)
            self.assertFalse(any(word >> 26 == 17 and (word >> 21) & 31 == 4
                                 for word in words))
            for cu1 in (0, exception.SR_CU1):
                for chunk, dirty in ((b"\x11\x72\x01\0\0\xff\xff", False),
                                     (b"\x11\x72" + self.dynamic_bits().data(), True)):
                    with self.subTest(shape=label, profile=profile, cu1=cu1, dirty=dirty):
                        guest = self.fixture_type(image, chunk, exception.SR_FR | 0xFF00 | cu1)
                        guest.context()
                        state = guest.snapshots[guest.core_return][0][29]
                        expected = [(i, state + 0x60 + i * 4) for i in range(12)] if dirty else []
                        expected += [(16, state + 0x24), (17, state + 0x34),
                                     (18, state + 0x38), (19, state + 0x3C)]
                        self.assertEqual(guest.fpr_word_loads, expected)


class InitDecompressorDirectFprAdapterCorpusTests(callee.InitDecompressorCalleePreservingAdapterCorpusTests):
    shadow_adapter_flags = InitDecompressorDirectFprAdapterTests.shadow_adapter_flags


class Fr1WordLoadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        exception.InitDecompressorExceptionTests.setUpClass()

    def test_word_load_and_rejection_boundaries(self):
        guest = exception.ExceptionCoreFixture(b"\x11\x72\x01\0\0\xff\xff",
                                              exception.SR_FR | exception.SR_CU1)
        guest.registers[8] = 0x80040004
        guest.put(0x80040000, 0x89ABCDEF, 4)
        before = guest.registers[:]
        word = (49 << 26) | (8 << 21) | (3 << 16) | 0xFFFC
        self.assertTrue(guest.execute_context_transfer(word))
        self.assertEqual(guest.fpr_value(3), (0x89ABCDEF, 0xFFFFFFFF))
        self.assertEqual(guest.registers, before)
        self.assertEqual(guest.reads, [(0x80040000, 4)])
        self.assertEqual(guest.fpr_word_loads, [(3, 0x80040000)])
        self.assertEqual(guest.fpr_loads, [])
        with self.assertRaisesRegex(AssertionError, "Unaligned FPR word"):
            guest.execute_context_transfer(word + 1)
        guest.status = exception.SR_FR
        with self.assertRaisesRegex(AssertionError, "CU1 disabled"):
            guest.execute_context_transfer(word)


if __name__ == "__main__":
    unittest.main()
