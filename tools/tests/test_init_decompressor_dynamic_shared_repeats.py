import unittest
import zlib

from tools.tests import test_init_decompressor_stored_shared_lengths as stored
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_tables as tables
from tools.tests import test_init_decompressor_decoder as decoder


class InitDecompressorDynamicSharedRepeatsTests(stored.InitDecompressorStoredSharedLengthsTests):
    shadow_extra_flags = (*stored.InitDecompressorStoredSharedLengthsTests.shadow_extra_flags,
                          "--dynamic-shared-repeats")

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
            self.assertEqual(len(image.code) * 4, text + 320)

    @staticmethod
    def repeat_stream(overflow=None):
        bits = streams.BitStream()
        bits.emit(5, 3)
        bits.emit(0, 5)
        bits.emit(0, 5)
        bits.emit(14, 4)
        lengths = [0] * 19
        lengths[0] = lengths[1] = lengths[16] = 2
        lengths[17] = lengths[18] = 3
        order = decoder.reference_data("2C120.rodata.s", "D_8002C15C")
        for symbol in order[:18]:
            bits.emit(lengths[symbol], 3)
        codes = {symbol: (code, width) for symbol, width, code in
                 tables.InitDecompressorTableTests.canonical(lengths)}

        def emit(symbol, extra=0):
            bits.emit(*codes[symbol])
            if symbol >= 16:
                bits.emit(extra, {16: 2, 17: 3, 18: 7}[symbol])

        # 65 zeros, literal A, 190 zeros, EOB, then one distance length.
        for symbol, extra in ((0, 0), (16, 0), (17, 0), (18, 47),
                              (1, 0), (18, 127), (18, 41), (1, 0)):
            emit(symbol, extra)
        emit(1 if overflow is None else overflow)
        if overflow is None:
            bits.emit(0, 1)
            bits.emit(1, 1)
        return bits.data() + b"\0\0"

    def test_repeat_widths_and_each_overflow_path(self):
        for overflow in (None, 16, 17, 18):
            raw = self.repeat_stream(overflow)
            output = b"A" if overflow is None else b""
            if overflow is None:
                self.assertEqual(zlib.decompress(raw, -15), output)
            chunk = b"\x11\x72" + raw
            for cu1 in (False, True):
                self.compare(chunk, exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF00,
                             expected_output=output, expected_result=len(output), dma_size=len(chunk))
            for label, profile, image in self.adapter_images:
                entry = image.symbols["init_decode_dynamic"]
                end = image.symbols["init_decode_stream"]
                calls = [(pc, word) for pc, word in image.code.items()
                         if entry <= pc < end and word >> 26 == 3]
                first_pc, take_word = min(calls)
                take_calls = sorted(pc for pc, word in calls if word == take_word)
                self.assertEqual(len(take_calls), 3)
                self.assertEqual(take_calls[0], first_pc)
                repeat_return = take_calls[-1] + 8
                target = ((first_pc + 4) & 0xF0000000) | ((take_word & 0x3FFFFFF) << 2)
                first_word = image.code[target]

                class RepeatFixture(self.fixture_type):
                    def __init__(self, *args):
                        self.repeat_widths = []
                        super().__init__(*args)

                    def execute(self, instruction):
                        if instruction == first_word and self.registers[31] == repeat_return:
                            self.repeat_widths.append(self.registers[5])
                        super().execute(instruction)

                with self.subTest(shape=label, profile=profile, overflow=overflow):
                    guest = RepeatFixture(image, chunk, exception.SR_FR | exception.SR_CU1 | 0xFF00)
                    guest.context()
                    widths = [2, 3, 7, 7, 7]
                    if overflow is not None:
                        widths.append({16: 2, 17: 3, 18: 7}[overflow])
                    self.assertEqual(guest.repeat_widths, widths)


class InitDecompressorDynamicSharedRepeatsCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorDynamicSharedRepeatsTests.shadow_extra_flags


if __name__ == "__main__":
    unittest.main()
