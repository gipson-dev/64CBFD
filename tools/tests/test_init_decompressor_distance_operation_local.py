import unittest
import zlib

from tools.tests import test_init_decompressor_dynamic_order_cursor as order
from tools.tests import test_init_decompressor_exception as exception


class InitDecompressorDistanceOperationLocalTests(order.InitDecompressorDynamicOrderCursorTests):
    shadow_extra_flags = (*order.InitDecompressorDynamicOrderCursorTests.shadow_extra_flags,
                          "--distance-operation-local")

    def test_backreference_table_storage_is_stable_during_decode(self):
        encoder = zlib.compressobj(wbits=-15, strategy=zlib.Z_FIXED)
        payload = b"ABCD" * 24
        chunk = b"\x11\x72" + encoder.compress(payload) + encoder.flush()
        for label, profile, image in self.adapter_images:
            for cu1 in (0, exception.SR_CU1):
                with self.subTest(shape=label, profile=profile, cu1=cu1):
                    class StableTableFixture(self.fixture_type):
                        def __init__(self, *args):
                            self.decoding = False
                            self.distance_publications = 0
                            self.builder_visits = self.compressed_visits = 0
                            super().__init__(*args)

                        def execute(self, word):
                            builders = self.visits.get(image.symbols["init_decode_build"], 0)
                            compressed = self.visits.get(image.symbols["init_decode_compressed"], 0)
                            if builders != self.builder_visits:
                                self.decoding = False
                                self.builder_visits = builders
                            if compressed != self.compressed_visits:
                                self.decoding = True
                                self.compressed_visits = compressed
                            super().execute(word)

                        def put(self, address, value, size):
                            if self.decoding:
                                if address < self.WORKSPACE + 4096 and self.WORKSPACE < address + size:
                                    raise AssertionError("table write during compressed decode")
                                if address == self.adapter_state + 52 and size == 4:
                                    self.distance_publications += 1
                            super().put(address, value, size)

                    guest = StableTableFixture(image, chunk, exception.SR_FR | cu1 | 0xFF01)
                    self.assertLessEqual(guest.adapter_state + 116, guest.WORKSPACE)
                    guest.context()
                    self.assertGreater(guest.visits.get(image.symbols["init_decode_compressed"], 0), 0)
                    self.assertGreater(guest.distance_publications, 0)
                    self.assertEqual(bytes(guest.memory[guest.OUTPUT + index]
                                           for index in range(len(payload))), payload)
                    with self.assertRaisesRegex(AssertionError, "table write during compressed decode"):
                        guest.put(guest.WORKSPACE, 0, 1)

    def test_packed_profile_size_reduction(self):
        for profile, text, bound, words, frame in (
                ("o2g3", 4336, 400, 119, 64), ("o1", 5808, 360, 157, 56)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            compressed = next(unit for unit in receipt["functions"]
                              if unit["function"] == "init_decode_compressed")
            self.assertEqual((compressed["public_unit_words"], compressed["frame_bytes"]),
                             (words, frame))
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 176)
            code_end = max(image.code) + 4
            following = min(first for first, last in image.readonly if first >= code_end)
            self.assertEqual(following, code_end)


class InitDecompressorDistanceOperationLocalCorpusTests(order.InitDecompressorDynamicOrderCursorCorpusTests):
    shadow_extra_flags = InitDecompressorDistanceOperationLocalTests.shadow_extra_flags


if __name__ == "__main__":
    unittest.main()
