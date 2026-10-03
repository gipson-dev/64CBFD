import ctypes
import shutil
import struct
import subprocess
import sys
import unittest
from pathlib import Path

from tools.tests import test_init_decompressor_aligned_entry as aligned
from tools.tests import test_init_decompressor_bounded_shifts as bounded
from tools.tests import test_init_decompressor_combined_builder as combined
from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_semantic as semantic


CURSOR = ("-DINIT_DECODE_BUILDER_SYMBOL_CURSOR",)
FRAME = ("-DINIT_DECODE_FRAME_BACKED",)
SCAN = ("-DINIT_DECODE_BOUNDED_LENGTH_SCAN", "-DINIT_DECODE_DYNAMIC_CURSOR")


class SymbolCapacityChecks:
    def test_full_288_cell_sorted_capacity_and_all_zero_return(self):
        for lengths in ([0] * 288, [0] * 286 + [1, 1],
                        [8] * 144 + [9] * 112 + [7] * 24 + [8] * 8):
            with self.subTest(lengths=lengths):
                model = semantic.tables.BuilderFixture(lengths, bits=9)
                candidate = self.fixture_type(self.library)
                values = (ctypes.c_uint32 * 288)(*lengths)
                root, width = ctypes.c_uint16(0xABCD), ctypes.c_uint32(9)
                result = self.library.init_decode_build(ctypes.byref(candidate.state),
                    values, 288, 288, None, None, ctypes.byref(root), ctypes.byref(width))
                self.assertEqual(result, model.run())
                self.assertEqual((root.value, width.value, candidate.state.allocated),
                                 (model.get(model.ROOT, 2), model.get(model.BITS, 4), model.fprs[19]))
                for address, value in model.memory.items():
                    if model.WORKSPACE <= address < model.WORKSPACE + model.fprs[19] * 4:
                        index, offset = divmod(address - model.WORKSPACE, 4)
                        entry = candidate.workspace[index]
                        encoded = bytes([entry.operation, entry.bits]) + struct.pack(">H", entry.value)
                        self.assertEqual(encoded[offset], value, (index, offset))


class InitDecompressorBuilderSymbolCursorTests(SymbolCapacityChecks,
                                               semantic.InitDecompressorSemanticTests):
    compiler_flags = CURSOR


class InitDecompressorAlignedSymbolCursorTests(SymbolCapacityChecks, aligned.EntryAlignmentChecks,
                                              bounded.BuilderShiftBounds,
                                              frame.InitDecompressorFrameBackedTests):
    compiler_flags = FRAME + combined.ALIGNED_BOUNDED + SCAN + CURSOR


class InitDecompressorPackedSymbolCursorTests(SymbolCapacityChecks, aligned.EntryAlignmentChecks,
                                             bounded.BuilderShiftBounds,
                                             frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + SCAN + CURSOR
                      + ("-DINIT_DECODE_CACHE_BUILDER=2",))


class InitDecompressorSanitizedSymbolCursorTests(SymbolCapacityChecks, aligned.EntryAlignmentChecks,
                                                bounded.BuilderShiftBounds,
                                                frame.InitDecompressorFrameBackedTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + SCAN + CURSOR
                      + ("-DINIT_DECODE_CACHE_BUILDER=2", "-fsanitize=undefined",
                         "-fno-sanitize-recover=undefined"))


class InitDecompressorRemainingSymbolCursorTests(InitDecompressorBuilderSymbolCursorTests):
    compiler_flags = ("-DINIT_DECODE_BUILDER_SYMBOL_CURSOR=2",)


class InitDecompressorAlignedRemainingCursorTests(InitDecompressorAlignedSymbolCursorTests):
    compiler_flags = (FRAME + combined.ALIGNED_BOUNDED + SCAN
                      + ("-DINIT_DECODE_BUILDER_SYMBOL_CURSOR=2",))


class InitDecompressorPackedRemainingCursorTests(InitDecompressorPackedSymbolCursorTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + SCAN
                      + ("-DINIT_DECODE_BUILDER_SYMBOL_CURSOR=2", "-DINIT_DECODE_CACHE_BUILDER=2"))


class InitDecompressorSanitizedRemainingCursorTests(InitDecompressorSanitizedSymbolCursorTests):
    compiler_flags = (FRAME + combined.PACKED_BOUNDED + SCAN
                      + ("-DINIT_DECODE_BUILDER_SYMBOL_CURSOR=2", "-DINIT_DECODE_CACHE_BUILDER=2",
                         "-fsanitize=undefined", "-fno-sanitize-recover=undefined"))


class InitDecompressorSymbolCursorGuardTests(unittest.TestCase):
    def test_unknown_source_modes_are_rejected(self):
        compiler = shutil.which("cc")
        if compiler is None:
            self.skipTest("host C compiler is unavailable")
        source = Path(__file__).resolve().parents[1] / "experiments/init_decompressor_semantic.c"
        for mode in (-1, 0, 3):
            with self.subTest(mode=mode):
                result = subprocess.run([compiler, "-std=c99", "-fsyntax-only",
                    "-DINIT_DECODE_BUILDER_SYMBOL_CURSOR=%d" % mode, str(source)],
                    capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Unsupported builder symbol cursor mode", result.stderr)

    def test_unknown_cli_mode_is_rejected_before_compilation(self):
        driver = Path(__file__).resolve().parents[1] / "experiments/compile_init_decompressor.py"
        result = subprocess.run([sys.executable, str(driver), "--builder-symbol-cursor", "invalid"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)


if __name__ == "__main__":
    unittest.main()
