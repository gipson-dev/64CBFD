import unittest
from pathlib import Path
from unittest import mock

from tools.tests import test_init_decompressor_stream_fitting as stream
from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_guest_builder as builder
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests.init_decompressor_guest_oracle import GuestStreamFixture
from tools.experiments import compile_init_decompressor as compiler


class ShadowCoreFixture(GuestStreamFixture):
    def __init__(self, image, raw):
        super().__init__(image, raw)
        self.allowed_writes.remove((self.STATE, self.STATE + 40))
        self.allowed_writes.append((self.STATE, self.STATE + 116))
        self.memory.update((self.STATE + i, 0xA5) for i in range(40, 116))


class InitDecompressorPackedHeaderTests(stream.InitDecompressorStreamFittingTests):
    shadow_extra_flags = (*stream.InitDecompressorStreamFittingTests.shadow_extra_flags,
                          "--packed-header")

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4480, 408), ("o1", 5920, 344)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            self.assertEqual(receipt["state_bytes"], 116)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 320)

    def test_header_layout_and_compiled_unaligned_load_pair(self):
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile):
                self.assertEqual(self.receipts[label, profile]["header_layout"], [4, 1])
                entry = image.symbols["init_decode_core"]
                words = [image.code[entry + i * 4] for i in range(24)]
                left = [word for word in words if word >> 26 == 34]
                right = [word for word in words if word >> 26 == 38]
                self.assertEqual(len(left), 1)
                self.assertEqual(len(right), 1)
                self.assertEqual(left[0] & 0xFFFF, 0)
                self.assertEqual(right[0] & 0xFFFF, 3)
                self.assertEqual(left[0] >> 16 & 0x3FF, right[0] >> 16 & 0x3FF)

    def test_nonpacked_header_layout_is_rejected(self):
        original = compiler.struct.unpack_from

        def ignored_packing(fmt, *args):
            values = original(fmt, *args)
            return (4, 4) if fmt == ">2I" and values == (4, 1) else values

        obj = Path(self.directory.name) / "packed-remaining-shadow/o2g3.o"
        with mock.patch.object(compiler.struct, "unpack_from", side_effect=ignored_packing):
            with self.assertRaisesRegex(ValueError, "packed header.*byte alignment"):
                compiler.inspect_object(obj)

    def test_unaligned_load_pair_reads_exact_header_bytes(self):
        for alignment in range(4):
            fixture = builder.InitDecompressorGuestInstructionTests.fixture()
            address = 0x1004 + alignment
            fixture.put(address, 0x1172AABB, 4)
            fixture.registers[1:3] = [address, 0xC0DEC0DE]
            fixture.execute((34 << 26) | (1 << 21) | (2 << 16))
            fixture.execute((38 << 26) | (1 << 21) | (2 << 16) | 3)
            self.assertEqual(fixture.registers[2], 0x1172AABB)
            touched = {first + i for first, size in fixture.reads for i in range(size)}
            self.assertEqual(touched, set(range(address, address + 4)))

    def test_both_header_formats_at_all_input_alignments(self):
        payload = b"Packed"
        encoded = decoder.InitDecompressorDecoderTests.encoded(payload)
        for header in (b"\x11\x72", b"\x11\x73\0\0"):
            for alignment in range(4):
                raw = b"\xa5" * alignment + header + encoded
                reference = streams.StreamFixture(raw)
                frame = reference.STACK - 0xA88
                reference.memory.update((frame + i, 0xA5) for i in range(0xA44))
                reference.memory.update((reference.WORKSPACE + i, 0xA5)
                                        for i in range(reference.ROOT - reference.WORKSPACE))
                reference.capture.add(0x100062F0)
                expected = reference.core(False, alignment=alignment)
                registers, fprs = reference.snapshots[0x100062F0]
                self.assertEqual(expected, len(payload))
                for label, profile, image in self.adapter_images:
                    with self.subTest(shape=label, profile=profile, header=header, alignment=alignment):
                        guest = ShadowCoreFixture(image, raw)
                        self.assertEqual(guest.core(alignment=alignment), expected)
                        self.assertEqual(bytes(guest.memory[guest.OUTPUT + i]
                                               for i in range(len(payload))), payload)
                        self.assertEqual([guest.get(guest.STATE + i * 4, 4) for i in range(10)],
                            [registers[23], guest.OUTPUT, guest.WORKSPACE, registers[28],
                             registers[30], fprs[17], fprs[18], fprs[19], guest.FRAME, guest.WORKSPACE])
                        self.assertEqual(bytes(guest.memory[guest.FRAME + i] for i in range(0xA44)),
                                         bytes(reference.memory[frame + i] for i in range(0xA44)))
                        for register in (*range(16, 24), 28, 29, 30, 31):
                            self.assertEqual(guest.registers[register], guest.before[register])


class InitDecompressorPackedHeaderCorpusTests(corpus.InitDecompressorShadowCorpusTests):
    shadow_extra_flags = InitDecompressorPackedHeaderTests.shadow_extra_flags


if __name__ == "__main__":
    unittest.main()
