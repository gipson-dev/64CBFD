import unittest

from tools.tests import test_init_decompressor_histogram_cursor as histogram
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture


class FixedLengthWriteFixture(GuestBuilderFixture):
    def __init__(self, image):
        self.length_writes = []
        super().__init__(image, [])

    def put(self, address, value, size):
        super().put(address, value, size)
        if self.FRAME + 0x548 <= address < self.FRAME + 0x9C8:
            self.length_writes.append((address, value, size))


class InitDecompressorFixedLengthCursorTests(histogram.InitDecompressorHistogramCursorTests):
    shadow_extra_flags = ("--loop-lookup", "--builder-histogram-cursor",
                          "--fixed-length-cursor")

    def test_fixed_initializer_ordered_lengths_and_complete_table(self):
        lengths = [8] * 144 + [9] * 112 + [7] * 24 + [8] * 8
        reference = decoder.FixedDecoderFixture(b"\x03")
        expected_table = bytes(reference.memory.get(reference.FIXED_BASE + i, 0xA5)
                               for i in range(658 * 4))
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile):
                guest = FixedLengthWriteFixture(image)
                guest.registers[4] = guest.STATE
                before = guest.registers[:]
                guest.run(entry=image.symbols["init_decode_fixed_tables"], budget=2000000)
                expected_writes = [
                    (guest.FRAME + 0x548 + i * 4, value, 4)
                    for i, value in enumerate(lengths)
                ] + [(guest.FRAME + 0x548 + i * 4, 5, 4) for i in range(30)]
                self.assertEqual(guest.length_writes, expected_writes)
                self.assertEqual([guest.get(guest.FRAME + 0x548 + i * 4, 4)
                                  for i in range(288)], [5] * 30 + lengths[30:])
                self.assertEqual(guest.get(guest.STATE + 28, 4), 658)
                self.assertEqual([guest.get(guest.FRAME + offset, size) for offset, size in
                                  ((0x9C8, 2), (0x9CC, 4), (0x9D0, 2), (0x9D4, 4))],
                                 [1, 7, 626, 5])
                self.assertEqual(bytes(guest.memory[guest.WORKSPACE + i]
                                       for i in range(658 * 4)), expected_table)
                self.assertEqual(bytes(guest.memory[guest.WORKSPACE + 658 * 4 + i]
                                       for i in range(16)), b"\xa5" * 16)
                self.assertEqual(bytes(guest.memory[guest.FRAME + i]
                                       for i in range(0xA44, 0xA88 + 16)), b"\xa5" * 84)
                for register in (*range(16, 24), 28, 29, 30, 31):
                    self.assertEqual(guest.registers[register], before[register])
                bound = next(unit["direct_call_frame_bound"]
                             for unit in self.receipts[label, profile]["call_graph"]
                             if unit["name"] == "init_decode_fixed_tables")
                self.assertLessEqual(guest.STACK - guest.min_sp, bound)

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4528, 408), ("o1", 5968, 344)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 320)


class InitDecompressorFixedLengthCursorCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = ("--loop-lookup", "--builder-histogram-cursor",
                          "--fixed-length-cursor")


if __name__ == "__main__":
    unittest.main()
