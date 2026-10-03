import ctypes
import unittest

from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_semantic as semantic


class EntryAlignmentChecks:
    def test_native_entry_layout_and_actual_workspace_alignment(self):
        layout = (ctypes.c_uint32 * 5).in_dll(self.library, "init_decode_entry_layout")
        self.assertEqual(list(layout), [4, 4, 0, 1, 2])
        candidate = self.fixture_type(self.library)
        fixed, _ = candidate.fixed()
        self.assertEqual(ctypes.addressof(candidate.workspace) & 3, 0)
        self.assertEqual(ctypes.addressof(fixed) & 3, 0)


class InitDecompressorAlignedEntryTests(EntryAlignmentChecks,
                                        semantic.InitDecompressorSemanticTests):
    compiler_flags = ("-DINIT_DECODE_ALIGNED_ENTRY",)


class InitDecompressorFrameAlignedEntryTests(EntryAlignmentChecks,
                                             frame.InitDecompressorFrameBackedTests):
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED", "-DINIT_DECODE_ALIGNED_ENTRY")


class InitDecompressorPackedEntryTests(EntryAlignmentChecks,
                                       semantic.InitDecompressorSemanticTests):
    compiler_flags = ("-DINIT_DECODE_ALIGNED_ENTRY", "-DINIT_DECODE_PACKED_ENTRY")


class InitDecompressorFramePackedEntryTests(EntryAlignmentChecks,
                                            frame.InitDecompressorFrameBackedTests):
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED", "-DINIT_DECODE_ALIGNED_ENTRY",
                      "-DINIT_DECODE_PACKED_ENTRY")


if __name__ == "__main__":
    unittest.main()
