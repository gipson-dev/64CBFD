import unittest

from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_semantic as semantic


class InitDecompressorCachedBuilderTests(semantic.InitDecompressorSemanticTests):
    compiler_flags = ("-DINIT_DECODE_CACHE_BUILDER",)


class InitDecompressorFrameCachedBuilderTests(frame.InitDecompressorFrameBackedTests):
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED", "-DINIT_DECODE_CACHE_BUILDER")


class InitDecompressorCountsOffsetsTests(semantic.InitDecompressorSemanticTests):
    compiler_flags = ("-DINIT_DECODE_CACHE_BUILDER=2",)


class InitDecompressorFrameCountsOffsetsTests(frame.InitDecompressorFrameBackedTests):
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED", "-DINIT_DECODE_CACHE_BUILDER=2")


if __name__ == "__main__":
    unittest.main()
