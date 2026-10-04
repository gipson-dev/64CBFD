import unittest

from tools.tests import test_init_decompressor_pointer_owned_adapter as pointer
from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_streams as streams


class InitDecompressorDynamicOrderCursorTests(pointer.InitDecompressorPointerOwnedAdapterTests):
    shadow_extra_flags = (*pointer.InitDecompressorPointerOwnedAdapterTests.shadow_extra_flags,
                          "--dynamic-order-cursor")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound, words in (("o2g3", 4352, 400, 247),
                                            ("o1", 5808, 360, 313)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            dynamic = next(unit for unit in receipt["functions"]
                           if unit["function"] == "init_decode_dynamic")
            self.assertEqual((dynamic["public_unit_words"], dynamic["frame_bytes"]),
                             (words, 112 if profile == "o2g3" else 120))
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 176)
            code_end = max(image.code) + 4
            following = min(first for first, last in image.readonly if first >= code_end)
            self.assertEqual(following, code_end)

    def test_all_transmitted_counts_preserve_ordered_initialization(self):
        order = decoder.reference_data("2C120.rodata.s", "D_8002C15C")
        self.assertEqual(sorted(order), list(range(19)))
        for transmitted in range(4, 20):
            bits = streams.BitStream()
            bits.emit(5, 3)
            bits.emit(0, 5)
            bits.emit(0, 5)
            bits.emit(transmitted - 4, 4)
            values = [(index * 3 + 1) & 7 for index in range(transmitted)]
            for value in values:
                bits.emit(value, 3)
            chunk = b"\x11\x72" + bits.data() + b"\0\0"
            for label, profile, image in self.adapter_images:
                for cu1 in (0, exception.SR_CU1):
                    with self.subTest(transmitted=transmitted, shape=label,
                                      profile=profile, cu1=cu1):
                        class LengthFixture(self.fixture_type):
                            def __init__(self, *args):
                                self.length_writes = []
                                self.watch_lengths = False
                                super().__init__(*args)
                                self.watch_lengths = True

                            def put(self, address, value, size):
                                super().put(address, value, size)
                                if self.watch_lengths and self.FRAME + 0x548 <= address < self.FRAME + 0x594:
                                    self.length_writes.append((address, value, size))

                        guest = LengthFixture(image, chunk, exception.SR_FR | cu1 | 0xFF00)
                        builder = image.symbols["init_decode_build"]
                        guest.run(entry=exception.ENTRY, stop_pc=builder, budget=10000)
                        self.assertGreater(guest.visits.get(image.symbols["init_decode_dynamic"], 0), 0)
                        self.assertEqual(guest.registers[6], 19)
                        expected = [(guest.FRAME + 0x548 + symbol * 4,
                                     values[index] if index < transmitted else 0, 4)
                                    for index, symbol in enumerate(order)]
                        self.assertEqual(guest.length_writes, expected)


class InitDecompressorDynamicOrderCursorCorpusTests(pointer.InitDecompressorPointerOwnedAdapterCorpusTests):
    shadow_extra_flags = InitDecompressorDynamicOrderCursorTests.shadow_extra_flags


if __name__ == "__main__":
    unittest.main()
