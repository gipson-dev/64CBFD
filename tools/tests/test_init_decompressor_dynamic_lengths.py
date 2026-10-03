import unittest

from tools.tests import test_init_decompressor_aligned_entry as aligned
from tools.tests import test_init_decompressor_bounded_shifts as bounded
from tools.tests import test_init_decompressor_combined_builder as combined
from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_semantic as semantic


CACHE_LENGTHS = ("-DINIT_DECODE_CACHE_DYNAMIC_LENGTHS",)
FRAME = ("-DINIT_DECODE_FRAME_BACKED",)
CURSOR = ("-DINIT_DECODE_DYNAMIC_CURSOR",)


class InitDecompressorCachedDynamicLengthsTests(semantic.InitDecompressorSemanticTests):
    compiler_flags = CACHE_LENGTHS


class InitDecompressorFrameCachedDynamicLengthsTests(frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + CACHE_LENGTHS


class InitDecompressorAlignedCachedDynamicLengthsTests(aligned.EntryAlignmentChecks,
                                                      bounded.BuilderShiftBounds,
                                                      frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + combined.ALIGNED_BOUNDED + CACHE_LENGTHS


class InitDecompressorPackedCachedDynamicLengthsTests(aligned.EntryAlignmentChecks,
                                                     bounded.BuilderShiftBounds,
                                                     frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + CACHE_LENGTHS
                      + ("-DINIT_DECODE_CACHE_BUILDER=2",))


class InitDecompressorSanitizedCachedDynamicLengthsTests(aligned.EntryAlignmentChecks,
                                                        bounded.BuilderShiftBounds,
                                                        frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + CACHE_LENGTHS
                      + ("-DINIT_DECODE_CACHE_BUILDER=2", "-fsanitize=undefined",
                          "-fno-sanitize-recover=undefined"))


class InitDecompressorFrameDynamicCursorTests(frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + CURSOR


class InitDecompressorAlignedDynamicCursorTests(aligned.EntryAlignmentChecks,
                                               bounded.BuilderShiftBounds,
                                               frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + combined.ALIGNED_BOUNDED + CURSOR


class InitDecompressorPackedDynamicCursorTests(aligned.EntryAlignmentChecks,
                                              bounded.BuilderShiftBounds,
                                              frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + CURSOR
                      + ("-DINIT_DECODE_CACHE_BUILDER=2",))


class InitDecompressorCachedDynamicCursorTests(aligned.EntryAlignmentChecks,
                                              bounded.BuilderShiftBounds,
                                              frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + CURSOR + CACHE_LENGTHS
                      + ("-DINIT_DECODE_CACHE_BUILDER=2",))


class InitDecompressorSanitizedDynamicCursorTests(aligned.EntryAlignmentChecks,
                                                 bounded.BuilderShiftBounds,
                                                 frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + CURSOR + CACHE_LENGTHS
                      + ("-DINIT_DECODE_CACHE_BUILDER=2", "-fsanitize=undefined",
                          "-fno-sanitize-recover=undefined"))


if __name__ == "__main__":
    unittest.main()
