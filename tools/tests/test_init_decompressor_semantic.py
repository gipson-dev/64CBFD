import ctypes
import shutil
import struct
import subprocess
import tempfile
import unittest
import zlib
from pathlib import Path

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_tables as tables


class Entry(ctypes.Structure):
    _fields_ = [("operation", ctypes.c_uint8), ("bits", ctypes.c_uint8),
                ("value", ctypes.c_uint16)]


class State(ctypes.Structure):
    _fields_ = [("input", ctypes.c_void_p), ("output", ctypes.c_void_p),
                ("workspace", ctypes.POINTER(Entry)),
                ("reservoir", ctypes.c_uint32), ("bits", ctypes.c_int32),
                ("produced", ctypes.c_int32), ("limit", ctypes.c_int32),
                ("allocated", ctypes.c_uint32),
                ("counts", ctypes.c_uint32 * 17), ("tables", ctypes.c_uint32 * 17),
                ("sorted", ctypes.c_uint32 * 288), ("offsets", ctypes.c_uint32 * 17),
                ("lengths", ctypes.c_uint32 * 320)]


class SemanticFixture:
    @staticmethod
    def make_state():
        state = State()
        ctypes.memset(ctypes.byref(state), 0xA5, ctypes.sizeof(state))
        return state

    def __init__(self, library, raw=b"", limit=0x70000000):
        self.library = library
        self.input = ctypes.create_string_buffer(raw + b"\0" * 16)
        self.output = ctypes.create_string_buffer(b"\xa5" * 0x10020)
        self.workspace = (Entry * 16384)()
        ctypes.memset(self.workspace, 0xA5, ctypes.sizeof(self.workspace))
        self.state = self.make_state()
        self.state.input = ctypes.addressof(self.input)
        self.state.output = ctypes.addressof(self.output) + 16
        self.state.workspace = self.workspace
        self.state.reservoir = self.state.bits = self.state.produced = 0
        self.state.limit = limit
        self.state.allocated = 0

    def fixed(self):
        fixed = (Entry * 16384)()
        ctypes.memset(fixed, 0xA5, ctypes.sizeof(fixed))
        state = self.make_state()
        state.workspace = fixed
        state.reservoir = 0
        self.library.init_decode_fixed_tables(ctypes.byref(state))
        return fixed, state

    def stream(self):
        fixed, _ = self.fixed()
        status = self.library.init_decode_stream(ctypes.byref(self.state), fixed)
        return status

    def bytes(self, count=None):
        count = self.state.produced if count is None else count
        return self.output.raw[16:16 + count]


class InitDecompressorSemanticTests(unittest.TestCase):
    state_type = State
    fixture_type = SemanticFixture
    compiler_flags = ()

    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("cc")
        if compiler is None:
            raise unittest.SkipTest("host C compiler is unavailable")
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        path = Path(cls.directory.name) / "semantic.so"
        source = Path(__file__).resolve().parents[1] / "experiments/init_decompressor_semantic.c"
        result = subprocess.run([compiler, "-std=c99", "-O2", "-shared", "-fPIC", "-fwrapv",
                        "-Wall", "-Wextra", "-Werror", *getattr(cls, "compiler_flags", ()),
                        str(source), "-o", str(path)],
                       capture_output=True, text=True)
        if result.returncode:
            raise AssertionError(result.stderr)
        cls.library = ctypes.CDLL(str(path))
        state_type = ctypes.POINTER(getattr(cls, "state_type", State))
        cls.library.init_decode_build.argtypes = [state_type,
            ctypes.POINTER(ctypes.c_uint32), ctypes.c_uint32, ctypes.c_uint32,
            ctypes.POINTER(ctypes.c_uint16), ctypes.POINTER(ctypes.c_uint8),
            ctypes.POINTER(ctypes.c_uint16), ctypes.POINTER(ctypes.c_uint32)]
        cls.library.init_decode_compressed.argtypes = [state_type] + [ctypes.c_uint32] * 4
        cls.library.init_decode_stored.argtypes = [state_type]
        cls.library.init_decode_fixed_tables.argtypes = [state_type]
        cls.library.init_decode_stream.argtypes = [state_type, ctypes.POINTER(Entry)]
        cls.library.init_decode_core.argtypes = [state_type, ctypes.POINTER(Entry)] + [ctypes.c_uint32] * 3
        contract.InitDecompressorContractTests.setUpClass.__func__(
            contract.InitDecompressorContractTests)
        decoder.InitDecompressorDecoderTests.setUpClass.__func__(
            decoder.InitDecompressorDecoderTests)

    def assert_model(self, raw, expected=None, limit=0x70000000, scratch_pattern=None):
        model = streams.StreamFixture(raw, limit=limit)
        if scratch_pattern is not None:
            # Fixed-table fixture setup used this frame; reset only scratch so
            # candidate/model stream entries start with the same physical bytes.
            model.memory.update({model.STACK + i: scratch_pattern for i in range(0xA38)})
        model_status = model.stream()
        candidate = getattr(self, "fixture_type", SemanticFixture)(self.library, raw, limit)
        self.assertEqual(candidate.stream(), model_status)
        self.assertEqual(candidate.state.produced, model.fprs[17])
        self.assertEqual(candidate.state.reservoir, model.registers[28])
        self.assertEqual(candidate.state.bits, model.registers[30])
        self.assertEqual(candidate.state.input - ctypes.addressof(candidate.input),
                         model.registers[23] - model.INPUT)
        self.assertEqual(candidate.state.allocated, model.fprs[19])
        expected_output = bytearray(b"\xa5" * 0x10020)
        for address, value in model.memory.items():
            if model.OUTPUT - 16 <= address < model.INPUT:
                expected_output[16 + address - model.OUTPUT] = value
        self.assertEqual(candidate.output.raw[:-1], bytes(expected_output))
        for address, size in model.writes:
            if model.OUTPUT <= address < model.INPUT:
                self.assertEqual(size, 1)
                self.assertEqual(candidate.output.raw[16 + address - model.OUTPUT],
                                 model.memory[address])
            elif model.WORKSPACE <= address < model.ROOT:
                for current in range(address, address + size):
                    index, offset = divmod(current - model.WORKSPACE, 4)
                    entry = candidate.workspace[index]
                    encoded = bytes([entry.operation, entry.bits]) + struct.pack(">H", entry.value)
                    self.assertEqual(encoded[offset], model.memory[current])
        if expected is not None:
            self.assertEqual(candidate.bytes(), expected)
            self.assertEqual(zlib.decompress(raw, -15), expected)
        return candidate, model

    def test_fixed_table_allocation_and_all_written_bytes_match_model(self):
        candidate = self.fixture_type(self.library)
        fixed, state = candidate.fixed()
        model = decoder.FixedDecoderFixture(b"\x03")
        self.assertEqual(state.allocated, 658)
        for address, value in model.memory.items():
            if model.WORKSPACE <= address < model.WORKSPACE + 658 * 4:
                index, offset = divmod(address - model.WORKSPACE, 4)
                entry = fixed[index]
                encoded = bytes([entry.operation, entry.bits]) + struct.pack(">H", entry.value)
                self.assertEqual(encoded[offset], value, (index, offset))

    def test_builder_small_trees_and_narrow_root_layout_match(self):
        for lengths, bits, allocated in (([], 7, 0), ([0] * 19, 7, 0), ([1, 1], 1, 0),
                              ([2, 2], 2, 0), ([1], 7, 0), ([1, 2, 2], 1, 0),
                              ([1, 2, 3, 3], 1, 0), ([1, 2, 3, 3], 2, 0),
                              ([1, 1, 1], 1, 0), ([2] * 5, 2, 0),
                              ([1, 2, 2], 1, 11), ([1, 2, 3, 3], 1, 11)):
            model = tables.BuilderFixture(lengths, bits=bits, allocated=allocated)
            candidate = self.fixture_type(self.library)
            candidate.state.allocated = allocated
            values = (ctypes.c_uint32 * len(lengths))(*lengths)
            root, width = ctypes.c_uint16(0xABCD), ctypes.c_uint32(bits)
            status = self.library.init_decode_build(ctypes.byref(candidate.state),
                values, len(lengths), len(lengths), None, None,
                ctypes.byref(root), ctypes.byref(width))
            self.assertEqual(status, model.run())
            if lengths == [1, 1, 1]:
                self.assertEqual(status, 0)
            elif lengths == [2] * 5:
                self.assertEqual(status, 1)
            self.assertEqual((root.value, width.value, candidate.state.allocated),
                             (model.get(model.ROOT, 2), model.get(model.BITS, 4), model.fprs[19]))
            for address, value in model.memory.items():
                if model.WORKSPACE <= address < model.WORKSPACE + model.fprs[19] * 4:
                    index, offset = divmod(address - model.WORKSPACE, 4)
                    entry = candidate.workspace[index]
                    encoded = bytes([entry.operation, entry.bits]) + struct.pack(">H", entry.value)
                    self.assertEqual(encoded[offset], value, (lengths, bits, index, offset))

    def test_stored_and_fixed_complete_streams(self):
        fixed = decoder.InitDecompressorDecoderTests
        for payload in (b"", b"Conker\0\xff", bytes(range(256))):
            raw = b"\x01" + struct.pack("<HH", len(payload), len(payload) ^ 0xFFFF) + payload
            self.assert_model(raw, payload)
            self.assert_model(fixed.encoded(payload), payload)
        self.assert_model(fixed.encoded([ord("A"), (258, 1)]), b"A" * 259)

    def test_dynamic_repeats_and_zlib_generated_streams(self):
        fixture = streams.InitDecompressorStreamTests()
        self.assert_model(fixture.dynamic(), b"A")
        for payload in (b"Conker dynamic block with repeated text " * 256,
                        bytes(range(128)) * 64):
            encoder = zlib.compressobj(level=6, wbits=-15)
            raw = encoder.compress(payload) + encoder.flush()
            self.assert_model(raw, payload)

    def test_errors_partial_output_and_repeat_first_match_model(self):
        fixture = streams.InitDecompressorStreamTests()
        for raw in (b"\x07", fixture.dynamic(overflow=True),
                    fixture.dynamic(repeat_first=True),
                    decoder.InitDecompressorDecoderTests.encoded([ord("A"), 286], terminate=False)):
            self.assert_model(raw)
        stored = b"\x00" + struct.pack("<HH", 2, 0xFFFD) + b"XY"
        self.assert_model(stored + fixture.dynamic(overflow=True))

    def test_strict_stored_and_match_limits(self):
        fixed = decoder.InitDecompressorDecoderTests
        stored = b"\x01\x01\x00\xfe\xffA"
        for limit in (0, 1, 2, 3, 4, 5):
            self.assert_model(stored, limit=limit)
            self.assert_model(fixed.encoded([ord("A"), (3, 1)]), limit=limit)

    def test_core_header_alignment_limit_and_error_match_model(self):
        dynamic = streams.InitDecompressorStreamTests().dynamic()
        for header in (b"\x11\x72", b"\x11\x73\0\0"):
            for alignment in range(4):
                for workspace in (tables.BuilderFixture.WORKSPACE,
                                  decoder.FixedDecoderFixture.OUTPUT + 8192):
                    raw = b"\xa5" * alignment + header + dynamic
                    model = streams.StreamFixture(raw)
                    model.capture = {0x100062F0}
                    status = model.core(False, alignment, workspace)
                    candidate = self.fixture_type(self.library, raw)
                    candidate.state.input += alignment
                    fixed, _ = candidate.fixed()
                    result = self.library.init_decode_core(ctypes.byref(candidate.state), fixed,
                        model.INPUT + alignment, model.OUTPUT, workspace)
                    self.assertEqual(result, status)
                    self.assertEqual(candidate.bytes(), model.output())
                    self.assertEqual(candidate.state.limit, model.fprs[18])
                    # Core restores s7/gp/fp; compare explicit candidate state
                    # with the original state immediately before that epilogue.
                    registers, _ = model.snapshots[0x100062F0]
                    self.assertEqual(candidate.state.input - ctypes.addressof(candidate.input),
                                     registers[23] - model.INPUT)
                    self.assertEqual(candidate.state.reservoir, registers[28])
                    self.assertEqual(candidate.state.bits, registers[30])
        raw = b"\x11\x72\x07"
        model = streams.StreamFixture(raw)
        candidate = self.fixture_type(self.library, raw)
        fixed, _ = candidate.fixed()
        self.assertEqual(self.library.init_decode_core(ctypes.byref(candidate.state), fixed,
            model.INPUT, model.OUTPUT, model.WORKSPACE), model.core(True))
        self.assertEqual(candidate.state.produced, model.fprs[17])

    def test_mixed_blocks_and_dynamic_error_after_stored_output(self):
        dynamic = streams.InitDecompressorStreamTests().dynamic()
        stored = b"\x00" + struct.pack("<HH", 2, 0xFFFD) + b"XY"
        fixed = decoder.InitDecompressorDecoderTests.encoded(b"BC")
        bits = streams.BitStream()
        bits.bits = [(byte >> i) & 1 for byte in stored for i in range(8)]
        fixed_length = 3 + sum(decoder.InitDecompressorDecoderTests.codes[symbol][1]
                               for symbol in (*b"BC", 256))
        fixed = bytes([fixed[0] & 0xFE]) + fixed[1:]
        bits.bits.extend((byte >> i) & 1 for byte in fixed for i in range(8))
        bits.bits = bits.bits[:len(stored) * 8 + fixed_length]
        bits.emit(0, 3)
        while len(bits.bits) & 7: bits.emit(0, 1)
        bits.emit(0, 16)
        bits.emit(0xFFFF, 16)
        self.assert_model(bits.data() + dynamic, b"XYBCA")
        bad = streams.InitDecompressorStreamTests().dynamic(overflow=True)
        model = streams.StreamFixture(b"\x11\x72" + stored + bad)
        candidate = self.fixture_type(self.library, b"\x11\x72" + stored + bad)
        fixed, _ = candidate.fixed()
        self.assertEqual(self.library.init_decode_core(ctypes.byref(candidate.state), fixed,
            model.INPUT, model.OUTPUT, model.WORKSPACE), model.core(True))
        self.assertEqual(candidate.bytes(), b"XY")
        self.assertEqual(candidate.state.produced, 2)

    def test_direct_decoder_extra_classes_and_guarded_history_underflow(self):
        encoder = decoder.InitDecompressorDecoderTests
        for index in range(30):
            distance = encoder.distance_bases[index] + (1 << encoder.distance_extras[index]) - 1
            li = min(index, 28)
            length = encoder.bases[li] + (1 << encoder.extras[li]) - 1
            prefix = bytes((i * 17 + 3) & 0xFF for i in range(distance))
            raw = encoder.encoded([(length, distance, li)])
            model = decoder.FixedDecoderFixture(raw, prefix=prefix)
            status = model.decode()
            candidate = self.fixture_type(self.library, raw)
            ctypes.memmove(candidate.state.output, prefix, len(prefix))
            candidate.state.produced = len(prefix)
            candidate.state.input += 1
            candidate.state.reservoir, candidate.state.bits = raw[0] >> 3, 5
            fixed, _ = candidate.fixed()
            candidate.state.workspace = fixed
            self.assertEqual(self.library.init_decode_compressed(ctypes.byref(candidate.state),
                1, 626, 7, 5), status)
            self.assertEqual(candidate.bytes(), model.output())
            self.assertEqual(candidate.state.bits, model.registers[30])
            self.assertEqual(candidate.state.reservoir, model.registers[28])
        candidate, _ = self.assert_model(encoder.encoded([ord("A"), (3, 2)]))
        self.assertEqual(candidate.bytes(), b"A\xa5A\xa5")


if __name__ == "__main__":
    unittest.main()
