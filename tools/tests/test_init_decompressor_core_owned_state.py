import unittest

from tools.tests import test_init_decompressor_dynamic_shared_repeats as repeats
from tools.tests import test_init_decompressor_guest_fpr_shadow as shadow
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_exception as exception


class CoreOwnedStateFixture(shadow.ShadowExceptionFixture):
    CORE_FIELDS = (12, 16, 20, 24, 28, 36)

    def __init__(self, *args):
        self.watch_state = False
        super().__init__(*args)
        self.initialized_fields = set()
        for offset in self.CORE_FIELDS:
            super().put(self.adapter_state + offset, 0xCCFF0000 + offset, 4)
        self.watch_state = True

    def get(self, address, size):
        if self.watch_state:
            for offset in self.CORE_FIELDS:
                field = self.adapter_state + offset
                if address < field + 4 and field < address + size:
                    if offset not in self.initialized_fields:
                        raise AssertionError("core field read before initialization: %d" % offset)
        return super().get(address, size)

    def put(self, address, value, size):
        super().put(address, value, size)
        if self.watch_state and size == 4:
            offset = address - self.adapter_state
            if offset in self.CORE_FIELDS:
                self.initialized_fields.add(offset)


class InitDecompressorCoreOwnedStateTests(repeats.InitDecompressorDynamicSharedRepeatsTests):
    shadow_adapter_flags = ("--defsym", "INIT_DECODE_CORE_OWNS_STATE=1")
    shadow_adapter_bytes = 296
    fixture_type = CoreOwnedStateFixture

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4480, 400), ("o1", 5888, 352)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 304)

    def test_adapter_omits_six_initializers_and_poison_gate_is_active(self):
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile):
                entry = image.symbols["init_decode_retail_core_adapter"]
                end = image.symbols["init_decode_retail_core_adapter_end"]
                self.assertEqual(end - entry, 296)
                stores = [word & 0xFFFF for pc, word in image.code.items()
                          if entry <= pc < end and word >> 26 == 43
                          and (word >> 21) & 31 == 29]
                for offset in CoreOwnedStateFixture.CORE_FIELDS:
                    self.assertNotIn(0x20 + offset, stores)
                guest = self.fixture_type(image, b"\x11\x72\x01\0\0\xff\xff",
                                          exception.SR_FR | exception.SR_CU1 | 0xFF00)
                for offset in guest.CORE_FIELDS:
                    with self.assertRaisesRegex(AssertionError, "read before initialization"):
                        guest.get(guest.adapter_state + offset, 4)
                    self.assertEqual(bytes(guest.memory[guest.adapter_state + offset + i]
                                           for i in range(4)),
                                     (0xCCFF0000 + offset).to_bytes(4, "big"))
                guest.context()
                self.assertEqual(guest.initialized_fields, set(guest.CORE_FIELDS))


class InitDecompressorCoreOwnedStateCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = repeats.InitDecompressorDynamicSharedRepeatsTests.shadow_extra_flags
    shadow_adapter_flags = InitDecompressorCoreOwnedStateTests.shadow_adapter_flags
    fixture_type = CoreOwnedStateFixture


if __name__ == "__main__":
    unittest.main()
