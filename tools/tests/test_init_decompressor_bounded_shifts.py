import ctypes
import random
import struct
import unittest

from tools.tests import test_init_decompressor_frame_backed as frame
from tools.tests import test_init_decompressor_semantic as semantic
from tools.tests import test_init_decompressor_tables as tables


class BuilderShiftBounds:
    def test_generated_complete_trees_and_runtime_shift_counts(self):
        randomizer = random.Random(0x1000696C)
        cases = [(list(range(1, 16)) + [16, 16], width) for width in (0, 1, 4, 7, 9)]
        for index in range(24):
            maximum = 6 if index % 6 == 0 else 16
            lengths = [1, 1]
            for _ in range(8 + index * 3):
                candidates = [i for i, length in enumerate(lengths) if length < maximum]
                if not candidates:
                    break
                leaf = randomizer.choice(candidates)
                depth = lengths[leaf] + 1
                lengths[leaf:leaf + 1] = [depth, depth]
            randomizer.shuffle(lengths)
            cases.append((lengths, 31 if maximum == 6 else (1, 4, 7, 9)[index % 4]))
        shifts = []
        for lengths, width in cases:
            with self.subTest(count=len(lengths), width=width, maximum=max(lengths)):
                model = tables.BuilderFixture(lengths, bits=width)
                execute = model.execute

                def record(word):
                    if word >> 26 == 0 and word & 63 in (4, 6):
                        shift = model.registers[(word >> 21) & 31]
                        self.assertLess(shift, 32)
                        shifts.append(shift)
                    execute(word)

                model.execute = record
                result = model.run(budget=1000000)
                candidate = self.fixture_type(self.library)
                values = (ctypes.c_uint32 * len(lengths))(*lengths)
                root, bits = ctypes.c_uint16(0xABCD), ctypes.c_uint32(width)
                self.assertEqual(self.library.init_decode_build(
                    ctypes.byref(candidate.state), values, len(lengths), len(lengths),
                    None, None, ctypes.byref(root), ctypes.byref(bits)), result)
                self.assertEqual(root.value, model.get(model.ROOT, 2))
                self.assertEqual(bits.value, model.get(model.BITS, 4))
                self.assertEqual(candidate.state.allocated, model.fprs[19])
                actual = b"".join(struct.pack(">BBH", entry.operation, entry.bits, entry.value)
                                   for entry in candidate.workspace[:candidate.state.allocated])
                for address, size in model.writes:
                    if model.WORKSPACE <= address < model.ROOT:
                        offset = address - model.WORKSPACE
                        expected = bytes(model.memory[address + i] for i in range(size))
                        self.assertEqual(actual[offset:offset + size], expected)
        self.assertGreaterEqual(max(shifts), 15)


class InitDecompressorBoundedShiftsTests(BuilderShiftBounds,
                                        semantic.InitDecompressorSemanticTests):
    compiler_flags = ("-DINIT_DECODE_BOUNDED_BUILDER_SHIFTS",)


class InitDecompressorFrameBoundedShiftsTests(BuilderShiftBounds,
                                             frame.InitDecompressorFrameBackedTests):
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED", "-DINIT_DECODE_BOUNDED_BUILDER_SHIFTS")


class InitDecompressorSanitizedShiftsTests(BuilderShiftBounds,
                                          semantic.InitDecompressorSemanticTests):
    compiler_flags = ("-DINIT_DECODE_BOUNDED_BUILDER_SHIFTS",
                      "-fsanitize=undefined", "-fno-sanitize-recover=undefined")


if __name__ == "__main__":
    unittest.main()
