import unittest

from tools.tests import test_init_decompressor_packed_header as header
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_exception as exception


class InitDecompressorStoredSharedLengthsTests(header.InitDecompressorPackedHeaderTests):
    shadow_extra_flags = (*header.InitDecompressorPackedHeaderTests.shadow_extra_flags,
                          "--stored-shared-lengths")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4480, 408), ("o1", 5888, 344)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 320)

    def test_bad_complement_preserves_pre_drop_bit_count(self):
        bad = b"\x11\x72\x01\x02\0\xff\xff"
        for cu1 in (False, True):
            self.compare(bad, exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF00,
                         expected_output=b"", expected_result=0, dma_size=len(bad))
        for label, profile, image in self.adapter_images:
            entry = image.symbols["init_decode_stored"]
            end = image.symbols["init_decode_fixed_tables"]
            stores = [(pc, word) for pc, word in image.code.items()
                      if entry <= pc < end and word >> 26 == 43
                      and word & 0xFFFF == 16 and (word >> 21) & 31 != 29]
            self.assertEqual(len(stores), 1)
            pc, word = stores[0]

            class RestoreFixture(self.fixture_type):
                def __init__(self, *args):
                    self.restore_snapshots = []
                    super().__init__(*args)

                def execute(self, instruction):
                    state = getattr(self, "adapter_state", None)
                    if instruction == word and state is not None:
                        base = self.registers[(instruction >> 21) & 31]
                        if (base + 16) & 0xFFFFFFFF == state + 16:
                            self.restore_snapshots.append(self.registers[:])
                    super().execute(instruction)

            for chunk, output, bits, active in (
                    (bad, b"", 16, True),
                    (b"\x11\x72\x01\x02\0\xfd\xffXY", b"XY", 0, False)):
                with self.subTest(shape=label, profile=profile, active=active):
                    guest = RestoreFixture(image, chunk,
                                           exception.SR_FR | exception.SR_CU1 | 0xFF00)
                    guest.context()
                    self.assertEqual(len(guest.restore_snapshots), int(active))
                    self.assertEqual(guest.get(guest.adapter_state + 16, 4), bits)
                    self.assertEqual(guest.get(guest.adapter_state + 12, 4), 0)
                    self.assertEqual(guest.get(guest.adapter_state, 4), guest.INPUT + len(chunk))
                    self.assertEqual(guest.get(guest.adapter_state + 20, 4), len(output))
                    self.assertEqual(bytes(guest.memory[guest.OUTPUT + i]
                                           for i in range(len(output))), output)
                    if active:
                        registers = guest.restore_snapshots[0]
                        self.assertEqual(registers[(word >> 21) & 31], guest.adapter_state)
                        self.assertEqual(registers[(word >> 16) & 31], 16)


class InitDecompressorStoredSharedLengthsCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorStoredSharedLengthsTests.shadow_extra_flags


if __name__ == "__main__":
    unittest.main()
