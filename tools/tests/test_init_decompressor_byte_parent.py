import ctypes
import struct
import unittest

from tools.tests import test_init_decompressor_aligned_entry as aligned
from tools.tests import test_init_decompressor_bounded_shifts as bounded
from tools.tests import test_init_decompressor_combined_builder as combined
from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_tables as tables


BYTE_PARENT = ("-DINIT_DECODE_FRAME_BACKED", "-DINIT_DECODE_BYTE_PARENT")


class WrappedParentAddresses:
    def test_parent_lookup_with_wrapped_guest_workspace_labels(self):
        lengths = [1, 2, 3, 3]
        for address in (0, 0x20000, 0x800340E8, 0xFFFFFFC0, 0xFFFFFFFC):
            with self.subTest(address=hex(address)):
                model = tables.BuilderFixture(lengths, bits=1, allocated=11)
                expected_status = model.run()
                candidate = self.fixture_type(self.library)
                candidate.state.workspaceAddress = address
                candidate.state.allocated = 11
                values = (ctypes.c_uint32 * len(lengths))(*lengths)
                root, bits = ctypes.c_uint16(0xABCD), ctypes.c_uint32(1)
                self.assertEqual(self.library.init_decode_build(
                    ctypes.byref(candidate.state), values, len(lengths), len(lengths),
                    None, None, ctypes.byref(root), ctypes.byref(bits)), expected_status)
                self.assertEqual(root.value, model.get(model.ROOT, 2))
                self.assertEqual(bits.value, model.get(model.BITS, 4))
                self.assertEqual(candidate.state.allocated, model.fprs[19])
                expected_frame = bytearray(model.memory[model.STACK + i] for i in range(0xA88))
                written_tables = {a - model.STACK for a, size in model.writes
                                  if size == 4 and model.STACK + 0x44 <= a < model.STACK + 0x84}
                self.assertGreater(len(written_tables), 1)
                for offset in written_tables:
                    retail = struct.unpack_from(">I", expected_frame, offset)[0]
                    translated = (retail - model.WORKSPACE + address) & 0xFFFFFFFF
                    struct.pack_into(">I", expected_frame, offset, translated)
                self.assertEqual(frame.FrameFixture.frame_bytes(candidate.state), expected_frame)
                actual = b"".join(struct.pack(">BBH", e.operation, e.bits, e.value)
                                   for e in candidate.workspace[:candidate.state.allocated])
                for location, size in model.writes:
                    if model.WORKSPACE <= location < model.ROOT:
                        offset = location - model.WORKSPACE
                        self.assertEqual(actual[offset:offset + size],
                                         bytes(model.memory[location + i] for i in range(size)))


class InitDecompressorByteParentTests(WrappedParentAddresses,
                                     bounded.BuilderShiftBounds,
                                     frame.InitDecompressorFrameBackedTests):
    compiler_flags = BYTE_PARENT


class InitDecompressorAlignedByteParentTests(WrappedParentAddresses,
                                            aligned.EntryAlignmentChecks,
                                            bounded.BuilderShiftBounds,
                                            frame.InitDecompressorFrameBackedTests):
    compiler_flags = BYTE_PARENT + combined.ALIGNED_BOUNDED


class InitDecompressorPackedByteParentTests(WrappedParentAddresses,
                                           aligned.EntryAlignmentChecks,
                                           bounded.BuilderShiftBounds,
                                           frame.InitDecompressorFrameBackedTests):
    compiler_flags = BYTE_PARENT + combined.PACKED_BOUNDED


class InitDecompressorSanitizedByteParentTests(WrappedParentAddresses,
                                              aligned.EntryAlignmentChecks,
                                              bounded.BuilderShiftBounds,
                                              frame.InitDecompressorFrameBackedTests):
    compiler_flags = BYTE_PARENT + combined.PACKED_BOUNDED + (
        "-fsanitize=undefined", "-fno-sanitize-recover=undefined")


if __name__ == "__main__":
    unittest.main()
