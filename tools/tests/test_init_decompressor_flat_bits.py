import unittest

from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_semantic as semantic


class InitDecompressorFlatBitsTests(semantic.InitDecompressorSemanticTests):
    compiler_flags = ("-DINIT_DECODE_FLAT_BITS",)


class InitDecompressorFrameFlatBitsTests(frame.InitDecompressorFrameBackedTests):
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED", "-DINIT_DECODE_FLAT_BITS")


if __name__ == "__main__":
    unittest.main()
