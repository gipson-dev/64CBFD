import unittest
import zlib

from tools.tests import test_init_decompressor_fixed_length_cursor as fixed
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_tables as tables
from tools.tests import test_init_decompressor_decoder as decoder


class InitDecompressorStreamFittingTests(fixed.InitDecompressorFixedLengthCursorTests):
    shadow_extra_flags = ("--loop-lookup", "--builder-histogram-cursor",
                          "--fixed-length-cursor", "--stream-masked-dispatch",
                          "--stream-byte-rewind")

    def test_byte_rewind_path_is_exercised(self):
        image = next(image for label, profile, image in self.adapter_images
                     if label == "packed-remaining" and profile == "o2g3")
        entry = image.symbols["init_decode_stream"]
        end = image.symbols["init_decode_core"]
        shifts = [(pc, word) for pc, word in image.code.items()
                  if entry <= pc < end and word >> 26 == 0
                  and word & 63 == 2 and (word >> 6) & 31 == 3]
        stores = [(pc, word) for pc, word in image.code.items()
                  if entry <= pc < end and word >> 26 == 43
                  and word & 0xFFFF == 0 and (word >> 21) & 31 != 29]
        self.assertEqual(len(shifts), 1)
        self.assertEqual(len(stores), 1)
        shift_pc, shift = shifts[0]
        store_pc, store = stores[0]
        guard_pc = shift_pc - 4
        subtract = image.code[store_pc - 4]
        # IDO places the count shift in the guard's ordinary branch delay slot.
        self.assertEqual(image.code[guard_pc] >> 26, 5)
        self.assertEqual(subtract >> 26, 0)
        self.assertEqual(subtract & 63, 35)
        self.assertEqual((subtract >> 11) & 31, (store >> 16) & 31)
        self.assertEqual((subtract >> 16) & 31, (shift >> 11) & 31)
        bits = streams.BitStream()
        bits.emit(5, 3)
        bits.emit(0, 5)
        bits.emit(0, 5)
        bits.emit(14, 4)
        code_lengths = [0] * 19
        code_lengths[0] = code_lengths[1] = 2
        code_lengths[9] = 1
        order = decoder.reference_data("2C120.rodata.s", "D_8002C15C")
        for symbol in order[:18]:
            bits.emit(code_lengths[symbol], 3)
        code_codes = {symbol: (code, width) for symbol, width, code in
                      tables.InitDecompressorTableTests.canonical(code_lengths)}
        literal_lengths = [9] * 256 + [1]
        for width in (*literal_lengths, 1):
            bits.emit(*code_codes[width])
        literal_codes = {symbol: (code, width) for symbol, width, code in
                         tables.InitDecompressorTableTests.canonical(literal_lengths)}
        bits.emit(*literal_codes[65])
        bits.emit(*literal_codes[256])
        raw = bits.data() + b"\0\0"
        self.assertEqual(zlib.decompress(raw, -15), b"A")
        chunk = b"\x11\x72" + raw
        for cu1 in (False, True):
            self.compare(chunk, exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF00,
                         expected_output=b"A", expected_result=1, dma_size=len(chunk))
        guest = self.fixture_type(image, chunk, exception.SR_FR | exception.SR_CU1 | 0xFF00)
        guest.capture.update((guard_pc, store_pc))
        guest.context()
        self.assertEqual(guest.visits.get(store_pc, 0), 1)
        before, _ = guest.snapshots[guard_pc]
        at_store, _ = guest.snapshots[store_pc]
        buffered = before[(shift >> 16) & 31]
        self.assertGreaterEqual(buffered, 8)
        state = at_store[(store >> 21) & 31]
        self.assertEqual(guest.get(state + 16, 4), buffered & 7)
        self.assertEqual(guest.get(state, 4), at_store[(store >> 16) & 31])
        self.assertEqual(at_store[(shift >> 11) & 31], buffered >> 3)
        self.assertEqual(guest.get(state, 4),
                         (at_store[(subtract >> 21) & 31] - (buffered >> 3)) & 0xFFFFFFFF)
        print("stream rewind gate: bits=%d unread=%d remaining=%d" %
              (buffered, buffered >> 3, buffered & 7), flush=True)

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4512, 408), ("o1", 5952, 344)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 320)


class InitDecompressorStreamFittingCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = ("--loop-lookup", "--builder-histogram-cursor",
                          "--fixed-length-cursor", "--stream-masked-dispatch",
                          "--stream-byte-rewind")


if __name__ == "__main__":
    unittest.main()
