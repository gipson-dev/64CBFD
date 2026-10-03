import unittest

from tools.tests import test_init_decompressor_aligned_entry as aligned
from tools.tests import test_init_decompressor_bounded_shifts as bounded
from tools.tests import test_init_decompressor_combined_builder as combined
from tools.tests import test_init_decompressor_frame_backed as frame


FRAME = ("-DINIT_DECODE_FRAME_BACKED",)
LOCAL = ("-DINIT_DECODE_LOCAL_ALLOCATED",)


class InitDecompressorAlignedCachedOffsetsTests(aligned.EntryAlignmentChecks,
                                               bounded.BuilderShiftBounds,
                                               frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + combined.ALIGNED_BOUNDED + ("-DINIT_DECODE_CACHE_BUILDER=2",)


class InitDecompressorPackedCachedOffsetsTests(aligned.EntryAlignmentChecks,
                                              bounded.BuilderShiftBounds,
                                              frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + combined.PACKED_BOUNDED + ("-DINIT_DECODE_CACHE_BUILDER=2",)


class InitDecompressorPackedCachedAllTests(aligned.EntryAlignmentChecks,
                                          bounded.BuilderShiftBounds,
                                          frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + combined.PACKED_BOUNDED + ("-DINIT_DECODE_CACHE_BUILDER=1",)


class InitDecompressorAlignedLocalAllocationTests(aligned.EntryAlignmentChecks,
                                                 bounded.BuilderShiftBounds,
                                                 frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + combined.ALIGNED_BOUNDED + LOCAL


class InitDecompressorPackedLocalAllocationTests(aligned.EntryAlignmentChecks,
                                                bounded.BuilderShiftBounds,
                                                frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + combined.PACKED_BOUNDED + LOCAL


class InitDecompressorSanitizedLocalAllocationTests(aligned.EntryAlignmentChecks,
                                                   bounded.BuilderShiftBounds,
                                                   frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + combined.PACKED_BOUNDED + LOCAL + (
        "-fsanitize=undefined", "-fno-sanitize-recover=undefined")


if __name__ == "__main__":
    unittest.main()
