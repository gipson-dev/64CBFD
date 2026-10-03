import unittest

from tools.tests import test_init_decompressor_aligned_entry as aligned
from tools.tests import test_init_decompressor_bounded_shifts as bounded
from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_semantic as semantic


ALIGNED_BOUNDED = ("-DINIT_DECODE_ALIGNED_ENTRY",
                   "-DINIT_DECODE_BOUNDED_BUILDER_SHIFTS")
PACKED_BOUNDED = ALIGNED_BOUNDED + ("-DINIT_DECODE_PACKED_ENTRY",)


class InitDecompressorAlignedBoundedTests(aligned.EntryAlignmentChecks,
                                         bounded.BuilderShiftBounds,
                                         semantic.InitDecompressorSemanticTests):
    compiler_flags = ALIGNED_BOUNDED


class InitDecompressorFrameAlignedBoundedTests(aligned.EntryAlignmentChecks,
                                              bounded.BuilderShiftBounds,
                                              frame.InitDecompressorFrameBackedTests):
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED",) + ALIGNED_BOUNDED


class InitDecompressorPackedBoundedTests(aligned.EntryAlignmentChecks,
                                        bounded.BuilderShiftBounds,
                                        semantic.InitDecompressorSemanticTests):
    compiler_flags = PACKED_BOUNDED


class InitDecompressorFramePackedBoundedTests(aligned.EntryAlignmentChecks,
                                             bounded.BuilderShiftBounds,
                                             frame.InitDecompressorFrameBackedTests):
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED",) + PACKED_BOUNDED


class InitDecompressorSanitizedPackedBoundedTests(aligned.EntryAlignmentChecks,
                                                 bounded.BuilderShiftBounds,
                                                 semantic.InitDecompressorSemanticTests):
    compiler_flags = PACKED_BOUNDED + ("-fsanitize=undefined",
                                      "-fno-sanitize-recover=undefined")


if __name__ == "__main__":
    unittest.main()
