import unittest

from tools.tests import test_init_decompressor_aligned_entry as aligned
from tools.tests import test_init_decompressor_bounded_shifts as bounded
from tools.tests import test_init_decompressor_combined_builder as combined
from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_semantic as semantic


CACHE_WORKSPACE = ("-DINIT_DECODE_CACHE_WORKSPACE",)


class InitDecompressorCachedWorkspaceTests(bounded.BuilderShiftBounds,
                                          semantic.InitDecompressorSemanticTests):
    compiler_flags = CACHE_WORKSPACE


class InitDecompressorFrameCachedWorkspaceTests(bounded.BuilderShiftBounds,
                                               frame.InitDecompressorFrameBackedTests):
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED",) + CACHE_WORKSPACE


class InitDecompressorFrameAlignedCachedWorkspaceTests(aligned.EntryAlignmentChecks,
                                                      bounded.BuilderShiftBounds,
                                                      frame.InitDecompressorFrameBackedTests):
    compiler_flags = (("-DINIT_DECODE_FRAME_BACKED",) + combined.ALIGNED_BOUNDED
                      + CACHE_WORKSPACE)


class InitDecompressorFramePackedCachedWorkspaceTests(aligned.EntryAlignmentChecks,
                                                     bounded.BuilderShiftBounds,
                                                     frame.InitDecompressorFrameBackedTests):
    compiler_flags = (("-DINIT_DECODE_FRAME_BACKED",) + combined.PACKED_BOUNDED
                      + CACHE_WORKSPACE)


class InitDecompressorSanitizedCachedWorkspaceTests(aligned.EntryAlignmentChecks,
                                                   bounded.BuilderShiftBounds,
                                                   frame.InitDecompressorFrameBackedTests):
    compiler_flags = (("-DINIT_DECODE_FRAME_BACKED",) + combined.PACKED_BOUNDED
                      + CACHE_WORKSPACE + ("-fsanitize=undefined",
                                            "-fno-sanitize-recover=undefined"))


if __name__ == "__main__":
    unittest.main()
