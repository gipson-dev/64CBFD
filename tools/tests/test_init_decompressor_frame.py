import ctypes
import shutil
import struct
import subprocess
import unittest
import zlib
from pathlib import Path

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests import test_init_decompressor_semantic as semantic
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_tables as tables


class InitDecompressorFrameTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        semantic.InitDecompressorSemanticTests.setUpClass.__func__(cls)

    def compare_scratch(self, candidate, model, lengths=False):
        for field, offset, count in (("counts", 0, 17), ("sorted", 0x84, 288),
                                     ("offsets", 0x504, 17)):
            values = getattr(candidate.state, field)
            for index in range(count):
                self.assertEqual(values[index], model.get(model.STACK + offset + index * 4, 4),
                                 (field, index))
        written = {byte for address, size in model.writes
                   for byte in range(address, address + size)}
        for index in range(16):
            address = model.STACK + 0x44 + index * 4
            value = model.get(address, 4)
            # Retail stores physical workspace pointers; candidate stores indices.
            if address in written and value:
                self.assertGreaterEqual(value, model.WORKSPACE)
                self.assertEqual((value - model.WORKSPACE) & 3, 0)
                value = (value - model.WORKSPACE) // 4
            self.assertEqual(candidate.state.tables[index], value, ("tables", index))
        if lengths:
            for index in range(316):
                self.assertEqual(candidate.state.lengths[index],
                                 model.get(model.STACK + 0x548 + index * 4, 4),
                                 ("lengths", index))
        self.assertEqual(candidate.state.tables[16], 0xA5A5A5A5)
        self.assertEqual(list(candidate.state.lengths[316:]), [0xA5A5A5A5] * 4)

    def test_native_physical_frame_layout_and_fixed_overlay(self):
        compiler = shutil.which("cc")
        self.assertIsNotNone(compiler)
        directory = Path(self.directory.name)
        fixture, binary = directory / "frame.c", directory / "frame"
        header = Path(__file__).resolve().parents[1] / "experiments"
        fields = ("counts", "tables", "sorted", "offsets", "staging",
                  "staging.fixed.literalRoot", "staging.fixed.literalBits",
                  "staging.fixed.distanceRoot", "staging.fixed.distanceBits",
                  "literalRoot", "distanceRoot", "literalBits", "distanceBits",
                  "wrapperReturn", "savedS", "dispatcherReturn", "streamReturn",
                  "finalBlock", "savedWorkspace", "savedFp", "savedGp",
                  "entryReturn", "padA84")
        expected = (0, 0x44, 0x84, 0x504, 0x548, 0x9C8, 0x9CC, 0x9D0, 0x9D4,
                    0xA38, 0xA3A, 0xA3C, 0xA40, 0xA44, 0xA48, 0xA68, 0xA6C,
                    0xA70, 0xA74, 0xA78, 0xA7C, 0xA80, 0xA84)
        checks = "\n".join("if (offsetof(InitDecodeFrame, %s) != %d) return %d;" %
                           (name, value, index + 2)
                           for index, (name, value) in enumerate(zip(fields, expected)))
        fixture.write_text('#include <stddef.h>\n#include "init_decompressor_frame.h"\n'
                           'int main(void) {\n'
                           'if (sizeof(InitDecodeFrame) != 0xA88) return 1;\n' +
                           checks + '\nreturn 0;\n}\n')
        subprocess.run([compiler, "-std=c99", "-Wall", "-Wextra", "-Werror",
                        "-I", str(header), str(fixture), "-o", str(binary)],
                       check=True, capture_output=True, text=True)
        subprocess.run([str(binary)], check=True)

    def test_builder_frame_arrays_and_pointer_index_translation(self):
        for lengths, width, allocated in (([], 7, 9), ([0] * 19, 7, 9),
                                          ([1, 1], 1, 0), ([1, 2, 3, 3], 1, 11),
                                          ([2] * 5, 2, 0), ([1, 1, 1], 1, 0)):
            with self.subTest(lengths=lengths, width=width, allocated=allocated):
                model = tables.BuilderFixture(lengths, bits=width, allocated=allocated)
                candidate = semantic.SemanticFixture(self.library)
                candidate.state.allocated = allocated
                values = (ctypes.c_uint32 * len(lengths))(*lengths)
                root, bits = ctypes.c_uint16(0xABCD), ctypes.c_uint32(width)
                result = self.library.init_decode_build(ctypes.byref(candidate.state),
                    values, len(lengths), len(lengths), None, None,
                    ctypes.byref(root), ctypes.byref(bits))
                self.assertEqual(result, model.run())
                self.compare_scratch(candidate, model, lengths=True)

    def test_dynamic_stream_scratch_and_register_mapping(self):
        payload = b"Conker frame mapping with repeated output " * 64
        encoder = zlib.compressobj(level=6, wbits=-15)
        raws = (streams.InitDecompressorStreamTests().dynamic(),
                encoder.compress(payload) + encoder.flush())
        for raw in raws:
            with self.subTest(raw=raw[:8]):
                candidate, model = semantic.InitDecompressorSemanticTests.assert_model(
                    self, raw, scratch_pattern=0xA5)
                self.compare_scratch(candidate, model, lengths=True)
                self.assertEqual(candidate.state.output - ctypes.addressof(candidate.output), 16)
                self.assertEqual(model.fprs[16], model.OUTPUT)
                self.assertEqual(model.fprs[18], candidate.state.limit)
                self.assertEqual(model.registers[22], model.WORKSPACE)

    def test_partial_dynamic_error_preserves_scratch_mapping(self):
        raw = streams.InitDecompressorStreamTests().dynamic(overflow=True)
        candidate, model = semantic.InitDecompressorSemanticTests.assert_model(
            self, raw, scratch_pattern=0xA5)
        self.compare_scratch(candidate, model, lengths=True)

    def test_fixed_initializer_root_outputs_alias_length_tail(self):
        model = streams.StreamFixture(b"\x03")
        model.code.update(contract.InitDecompressorContractTests.entries("func_1000709C"))
        model.registers[31] = 0xDEAD0000
        before = model.registers[:]
        model.run(entry=0x1000709C)
        frame = model.STACK - 0xA88
        self.assertEqual([model.get(frame + offset, size) for offset, size in
                          ((0x9C8, 2), (0x9CC, 4), (0x9D0, 2), (0x9D4, 4))],
                         [1, 7, 626, 5])
        self.assertEqual(model.fprs[19], 658)
        self.assertEqual(model.registers[29], before[29])
        for index in range(16, 24):
            self.assertEqual(model.registers[index], before[index])
        # Initializer saves neither gp nor fp in memory; builder restores them via FPRs.
        self.assertEqual(model.registers[28], before[28])
        self.assertEqual(model.registers[30], before[30])
        self.assertFalse(any(frame + 0xA78 <= address < frame + 0xA80
                             for address, _ in model.writes))

    def test_outer_core_save_cells_and_distinct_nested_return_slots(self):
        raw = b"\x11\x72" + streams.InitDecompressorStreamTests().dynamic()
        model = streams.StreamFixture(raw)
        before = model.registers[:]
        self.assertEqual(model.core(True), 1)
        frame = model.STACK - 0x10 - 0xA88
        saved = (*range(16, 24), 30, 28, 31)
        offsets = (*range(0xA48, 0xA68, 4), 0xA78, 0xA7C, 0xA80)
        for register, offset in zip(saved, offsets):
            expected = 0x10006250 if register == 31 else before[register]
            self.assertEqual(model.get(frame + offset, 4), expected, register)
            self.assertEqual(model.registers[register], before[register], register)
        self.assertEqual([model.get(frame + offset, 4) for offset in (0xA44, 0xA68, 0xA6C)],
                         [0x100063DC, 0x10006348, 0x100062E8])
        self.assertEqual(model.get(frame + 0xA70, 4), 1)
        self.assertEqual(model.get(model.STACK - 0x10, 4), before[31])
        self.assertEqual(model.registers[29], before[29])

    def test_direct_init_call_ledger_has_no_external_internal_entry(self):
        rom = contract.InitDecompressorContractTests.project / "conker.us.bin"
        if not rom.exists():
            self.skipTest("pristine decompressed image unavailable")
        data = rom.read_bytes()
        calls = set()
        for offset in range(0x1000, 0x290D0, 4):
            word = struct.unpack_from(">I", data, offset)[0]
            if word >> 26 not in (2, 3):
                continue
            pc = 0x10000000 + offset
            target = ((pc + 4) & 0xF0000000) | ((word & 0x03FFFFFF) << 2)
            if 0x10006240 <= target < 0x100071C8 and not 0x6240 <= offset < 0x71C8:
                calls.add((offset, target))
        self.assertEqual(calls, {(0x1234, 0x1000709C), (0x1308, 0x10006240),
                                 (0x5F2C, 0x1000625C)})

    def test_exception_caller_fpr_save_restore_and_unconditional_delay(self):
        words = dict(contract.InitDecompressorContractTests.entries("func_10005C2C"))
        saved_fprs = (*range(12), *range(16, 20))
        for index, fpr in enumerate(saved_fprs):
            self.assertEqual(words[0x10005EE4 + index * 4],
                             (61 << 26) | (29 << 21) | (fpr << 16) | (index * 8))
            self.assertEqual(words[0x10005F44 + index * 4],
                             (53 << 26) | (29 << 21) | (fpr << 16) | (index * 8))
        self.assertEqual(words[0x10005EB4], 0x27BDFF78)  # Extra 0x88 frame.
        self.assertEqual(words[0x10005EC8], 0x14C00016)  # CU1 set skips FPR saves.
        self.assertEqual(words[0x10005F40], 0x14C00010)  # Ordinary BNE, not BNEL.
        self.assertEqual(words[0x10005F44], 0xD7A00000)  # f0 load always in delay slot.
        self.assertEqual(words[0x10005F84], 0x27BD0088)

    def test_core_stack_low_water_for_direct_and_wrapped_paths(self):
        for wrapped in (False, True):
            for raw in (b"\x11\x72\x07", b"\x11\x72\x01\0\0\xff\xff",
                        b"\x11\x72" + streams.InitDecompressorStreamTests().dynamic()):
                with self.subTest(wrapped=wrapped, raw=raw[:8]):
                    model = streams.StreamFixture(raw)
                    execute = model.execute
                    stack = [model.registers[29]]

                    def record(word):
                        execute(word)
                        stack.append(model.registers[29])

                    model.execute = record
                    model.core(wrapped)
                    self.assertEqual(model.STACK - min(stack), 0xA98 if wrapped else 0xA88)
                    self.assertEqual(stack[-1], model.STACK)


if __name__ == "__main__":
    unittest.main()
