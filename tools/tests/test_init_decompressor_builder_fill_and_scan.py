import unittest

from tools.tests import test_init_decompressor_aligned_entry as aligned
from tools.tests import test_init_decompressor_bounded_shifts as bounded
from tools.tests import test_init_decompressor_combined_builder as combined
from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_semantic as semantic


LEAF = ("-DINIT_DECODE_CACHE_LEAF_TABLE",)
FRAME = ("-DINIT_DECODE_FRAME_BACKED",)


class InitDecompressorLeafTableTests(semantic.InitDecompressorSemanticTests):
    compiler_flags = LEAF


class InitDecompressorAlignedLeafTableTests(aligned.EntryAlignmentChecks,
                                           bounded.BuilderShiftBounds,
                                           frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + combined.ALIGNED_BOUNDED + LEAF + ("-DINIT_DECODE_DYNAMIC_CURSOR",)


class InitDecompressorPackedLeafTableTests(aligned.EntryAlignmentChecks,
                                          bounded.BuilderShiftBounds,
                                          frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + LEAF
                      + ("-DINIT_DECODE_DYNAMIC_CURSOR", "-DINIT_DECODE_CACHE_BUILDER=2"))


class InitDecompressorSanitizedLeafTableTests(aligned.EntryAlignmentChecks,
                                             bounded.BuilderShiftBounds,
                                             frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + LEAF
                      + ("-DINIT_DECODE_DYNAMIC_CURSOR", "-DINIT_DECODE_CACHE_BUILDER=2",
                         "-fsanitize=undefined", "-fno-sanitize-recover=undefined"))


class InitDecompressorBoundedLengthScanTests(semantic.InitDecompressorSemanticTests):
    compiler_flags = ("-DINIT_DECODE_BOUNDED_LENGTH_SCAN",)


class InitDecompressorAlignedLengthScanTests(aligned.EntryAlignmentChecks,
                                            bounded.BuilderShiftBounds,
                                            frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.ALIGNED_BOUNDED
                      + ("-DINIT_DECODE_DYNAMIC_CURSOR", "-DINIT_DECODE_BOUNDED_LENGTH_SCAN"))


class InitDecompressorPackedLengthScanTests(aligned.EntryAlignmentChecks,
                                           bounded.BuilderShiftBounds,
                                           frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED
                      + ("-DINIT_DECODE_DYNAMIC_CURSOR", "-DINIT_DECODE_CACHE_BUILDER=2",
                         "-DINIT_DECODE_BOUNDED_LENGTH_SCAN"))


class InitDecompressorSanitizedLengthScanTests(aligned.EntryAlignmentChecks,
                                              bounded.BuilderShiftBounds,
                                              frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED
                      + ("-DINIT_DECODE_DYNAMIC_CURSOR", "-DINIT_DECODE_CACHE_BUILDER=2",
                         "-DINIT_DECODE_BOUNDED_LENGTH_SCAN", "-fsanitize=undefined",
                         "-fno-sanitize-recover=undefined"))


if __name__ == "__main__":
    unittest.main()
