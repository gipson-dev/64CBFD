import unittest

from tools.tests import test_init_decompressor_aligned_entry as aligned
from tools.tests import test_init_decompressor_bounded_shifts as bounded
from tools.tests import test_init_decompressor_combined_builder as combined
from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_semantic as semantic


CACHE_CODE = ("-DINIT_DECODE_CACHE_DYNAMIC_CODE",)
FRAME_CURSOR = ("-DINIT_DECODE_FRAME_BACKED", "-DINIT_DECODE_DYNAMIC_CURSOR")
MASK_ONLY = ("-DINIT_DECODE_CACHE_DYNAMIC_CODE=2",)
INLINE_MASK = ("-DINIT_DECODE_CACHE_DYNAMIC_CODE=3",)
SANITIZE = ("-fsanitize=undefined", "-fno-sanitize-recover=undefined")


class InitDecompressorCachedDynamicCodeTests(semantic.InitDecompressorSemanticTests):
    compiler_flags = CACHE_CODE


class InitDecompressorFrameCachedDynamicCodeTests(frame.InitDecompressorFrameBackedTests):
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED",) + CACHE_CODE


class InitDecompressorAlignedCachedDynamicCodeTests(aligned.EntryAlignmentChecks,
                                                   bounded.BuilderShiftBounds,
                                                   frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME_CURSOR + combined.ALIGNED_BOUNDED + CACHE_CODE


class InitDecompressorPackedCachedDynamicCodeTests(aligned.EntryAlignmentChecks,
                                                  bounded.BuilderShiftBounds,
                                                  frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME_CURSOR + combined.PACKED_BOUNDED + CACHE_CODE
                      + ("-DINIT_DECODE_CACHE_BUILDER=2",))


class InitDecompressorSanitizedCachedDynamicCodeTests(aligned.EntryAlignmentChecks,
                                                     bounded.BuilderShiftBounds,
                                                     frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME_CURSOR + combined.PACKED_BOUNDED + CACHE_CODE
                      + ("-DINIT_DECODE_CACHE_BUILDER=2", "-fsanitize=undefined",
                          "-fno-sanitize-recover=undefined"))


class InitDecompressorAlignedMaskOnlyTests(aligned.EntryAlignmentChecks,
                                          bounded.BuilderShiftBounds,
                                          frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME_CURSOR + combined.ALIGNED_BOUNDED + MASK_ONLY


class InitDecompressorPackedMaskOnlyTests(aligned.EntryAlignmentChecks,
                                         bounded.BuilderShiftBounds,
                                         frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME_CURSOR + combined.PACKED_BOUNDED + MASK_ONLY
                      + ("-DINIT_DECODE_CACHE_BUILDER=2",))


class InitDecompressorSanitizedMaskOnlyTests(aligned.EntryAlignmentChecks,
                                            bounded.BuilderShiftBounds,
                                            frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME_CURSOR + combined.PACKED_BOUNDED + MASK_ONLY
                      + ("-DINIT_DECODE_CACHE_BUILDER=2",) + SANITIZE)


class InitDecompressorAlignedInlineMaskTests(aligned.EntryAlignmentChecks,
                                            bounded.BuilderShiftBounds,
                                            frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME_CURSOR + combined.ALIGNED_BOUNDED + INLINE_MASK


class InitDecompressorPackedInlineMaskTests(aligned.EntryAlignmentChecks,
                                           bounded.BuilderShiftBounds,
                                           frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME_CURSOR + combined.PACKED_BOUNDED + INLINE_MASK
                      + ("-DINIT_DECODE_CACHE_BUILDER=2",))


class InitDecompressorSanitizedInlineMaskTests(aligned.EntryAlignmentChecks,
                                              bounded.BuilderShiftBounds,
                                              frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME_CURSOR + combined.PACKED_BOUNDED + INLINE_MASK
                      + ("-DINIT_DECODE_CACHE_BUILDER=2",) + SANITIZE)


if __name__ == "__main__":
    unittest.main()
