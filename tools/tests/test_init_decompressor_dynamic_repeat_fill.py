import unittest
import zlib

from tools.tests import test_init_decompressor_simple_seed_combination as simple
from tools.tests import test_init_decompressor_dynamic_shared_repeats as repeats
from tools.tests import test_init_decompressor_core_owned_state as owned
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_tables as tables
from tools.tests import test_init_decompressor_decoder as decoder


class InitDecompressorDynamicRepeatFillTests(simple.InitDecompressorSimpleSeedCombinationTests):
    shadow_extra_flags = (*simple.InitDecompressorSimpleSeedCombinationTests.shadow_extra_flags,
                          "--dynamic-repeat-value")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4448, 392), ("o1", 5856, 352)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 304)

    @staticmethod
    def nonzero_repeat_stream():
        bits = streams.BitStream()
        bits.emit(5, 3)
        bits.emit(0, 5)
        bits.emit(0, 5)
        bits.emit(14, 4)
        lengths = [0] * 19
        lengths[0] = lengths[1] = 2
        lengths[3] = lengths[16] = lengths[17] = lengths[18] = 3
        order = decoder.reference_data("2C120.rodata.s", "D_8002C15C")
        for symbol in order[:18]:
            bits.emit(lengths[symbol], 3)
        codes = {symbol: (code, width) for symbol, width, code in
                 tables.InitDecompressorTableTests.canonical(lengths)}
        for symbol, extra in ((17, 0), (18, 51), (3, 0), (16, 0),
                              (18, 127), (18, 38), (1, 0), (1, 0)):
            bits.emit(*codes[symbol])
            if symbol >= 16:
                bits.emit(extra, {16: 2, 17: 3, 18: 7}[symbol])
        literal_lengths = [0] * 65 + [3] * 4 + [0] * 187 + [1]
        literal_codes = {symbol: (code, width) for symbol, width, code in
                         tables.InitDecompressorTableTests.canonical(literal_lengths)}
        bits.emit(*literal_codes[65])
        bits.emit(*literal_codes[256])
        return bits.data() + b"\0\0", lengths, literal_lengths + [1]

    def test_ordered_repeat_lengths_include_nonzero_previous_and_extremes(self):
        raw, code_lengths, decoded = self.nonzero_repeat_stream()
        for cu1 in (False, True):
            self.compare(b"\x11\x72" + raw,
                         exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF00,
                         expected_output=b"A", expected_result=1, dma_size=len(raw) + 2)
        zero_codes = [0] * 19
        zero_codes[0] = zero_codes[1] = zero_codes[16] = 2
        zero_codes[17] = zero_codes[18] = 3
        cases = ((repeats.InitDecompressorDynamicSharedRepeatsTests.repeat_stream(),
                  zero_codes, [0] * 65 + [1] + [0] * 190 + [1, 1]),
                 (raw, code_lengths, decoded))
        order = decoder.reference_data("2C120.rodata.s", "D_8002C15C")
        for raw, alphabet, decoded in cases:
            self.assertEqual(zlib.decompress(raw, -15), b"A")
            for label, profile, image in self.adapter_images:
                class LengthFixture(self.fixture_type):
                    def __init__(self, *args):
                        self.length_writes = []
                        self.watch_lengths = False
                        super().__init__(*args)
                        self.watch_lengths = True

                    def put(self, address, value, size):
                        super().put(address, value, size)
                        if self.watch_lengths:
                            if self.FRAME + 0x548 <= address < self.FRAME + 0x548 + 258 * 4:
                                self.length_writes.append((address, value, size))

                with self.subTest(shape=label, profile=profile, nonzero=3 in decoded):
                    guest = LengthFixture(image, b"\x11\x72" + raw,
                                          exception.SR_FR | exception.SR_CU1 | 0xFF00)
                    guest.context()
                    expected = [(guest.FRAME + 0x548 + symbol * 4, alphabet[symbol], 4)
                                for symbol in order]
                    expected += [(guest.FRAME + 0x548 + i * 4, value, 4)
                                 for i, value in enumerate(decoded)]
                    self.assertEqual(len(expected), 277)
                    self.assertEqual(guest.length_writes, expected)


class InitDecompressorDynamicRepeatFillCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorDynamicRepeatFillTests.shadow_extra_flags
    shadow_adapter_flags = owned.InitDecompressorCoreOwnedStateTests.shadow_adapter_flags
    fixture_type = owned.CoreOwnedStateFixture


if __name__ == "__main__":
    unittest.main()
