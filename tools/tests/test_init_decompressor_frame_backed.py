import ctypes
import struct
import unittest

from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests import test_init_decompressor_semantic as semantic
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_tables as tables


class FrameState(ctypes.Structure):
    _fields_ = semantic.State._fields_[:8] + [
        ("frame", ctypes.POINTER(ctypes.c_uint32)), ("workspaceAddress", ctypes.c_uint32)]


class FrameFixture(semantic.SemanticFixture):
    @staticmethod
    def make_state():
        state = FrameState()
        ctypes.memset(ctypes.byref(state), 0xA5, ctypes.sizeof(state))
        state.storage = (ctypes.c_uint32 * (0xA88 // 4 + 8))()
        ctypes.memset(state.storage, 0xA5, ctypes.sizeof(state.storage))
        state.frame = ctypes.cast(ctypes.byref(state.storage, 16), ctypes.POINTER(ctypes.c_uint32))
        state.workspaceAddress = tables.BuilderFixture.WORKSPACE
        return state

    @staticmethod
    def frame_bytes(state, fixed=False):
        # Native halfwords at dynamic/fixed root cells need separate BE encoding.
        words = ctypes.string_at(state.frame, 0xA88)
        result = bytearray(b"".join(struct.pack(">I", value)
                                    for value in struct.unpack("=674I", words)))
        for offset in ((0x9C8, 0x9D0, 0xA38) if fixed else (0xA38,)):
            result[offset:offset + 4] = struct.pack(">2H", *struct.unpack_from("=2H", words, offset))
        return bytes(result)


class InitDecompressorFrameBackedTests(semantic.InitDecompressorSemanticTests):
    state_type = FrameState
    fixture_type = FrameFixture
    compiler_flags = ("-DINIT_DECODE_FRAME_BACKED",)

    def compare_frame(self, state, model, start=0, end=0xA38):
        expected = bytes(model.memory[model.STACK + offset] for offset in range(start, end))
        self.assertEqual(FrameFixture.frame_bytes(state)[start:end], expected)
        self.assertEqual(bytes(ctypes.string_at(state.storage, 16)), b"\xa5" * 16)
        self.assertEqual(bytes(ctypes.string_at(ctypes.byref(state.storage, 16 + 0xA88), 16)),
                         b"\xa5" * 16)
        # This candidate has no original entry adapter and must not occupy save cells.
        self.assertEqual(FrameFixture.frame_bytes(state)[0xA44:], b"\xa5" * (0xA88 - 0xA44))

    def test_physical_builder_scratch_including_workspace_addresses(self):
        for lengths, width, allocated in (([], 7, 9), ([0] * 19, 7, 9),
                                          ([1, 1], 1, 0), ([1, 2, 3, 3], 1, 11),
                                          ([1, 1, 1], 1, 0), ([2] * 5, 2, 0)):
            with self.subTest(lengths=lengths, width=width, allocated=allocated):
                model = tables.BuilderFixture(lengths, bits=width, allocated=allocated)
                candidate = FrameFixture(self.library)
                candidate.state.allocated = allocated
                values = (ctypes.c_uint32 * len(lengths))(*lengths)
                root, bits = ctypes.c_uint16(0xABCD), ctypes.c_uint32(width)
                status = self.library.init_decode_build(ctypes.byref(candidate.state),
                    values, len(lengths), len(lengths), None, None,
                    ctypes.byref(root), ctypes.byref(bits))
                self.assertEqual(status, model.run())
                self.compare_frame(candidate.state, model)

    def test_dynamic_frame_bytes_and_error_lifetimes(self):
        fixture = streams.InitDecompressorStreamTests()
        for raw in (fixture.dynamic(), fixture.dynamic(overflow=True),
                    fixture.dynamic(repeat_first=True)):
            with self.subTest(raw=raw[:8]):
                candidate, model = self.assert_model(raw, scratch_pattern=0xA5)
                self.compare_frame(candidate.state, model)
                # Root/width outputs are native halfwords/words, serialized above.
                self.assertEqual(FrameFixture.frame_bytes(candidate.state)[0xA38:0xA44],
                                 bytes(model.memory[model.STACK + i] for i in range(0xA38, 0xA44)))

    def test_fixed_initializer_reuses_root_cells_in_length_tail(self):
        model = streams.StreamFixture(b"\x03")
        model.code.update(contract.InitDecompressorContractTests.entries("func_1000709C"))
        model.registers[31] = 0xDEAD0000
        model.run(entry=0x1000709C)
        candidate = FrameFixture(self.library)
        candidate.state.workspaceAddress = 0x8003BE90
        self.library.init_decode_fixed_tables(ctypes.byref(candidate.state))
        frame = model.STACK - 0xA88
        # Initializer reused a new frame; compare all bytes it wrote in scratch.
        actual = FrameFixture.frame_bytes(candidate.state, fixed=True)
        for address, size in model.writes:
            if frame <= address < frame + 0xA38:
                self.assertEqual(actual[address - frame:address - frame + size],
                                 bytes(model.memory[address + i] for i in range(size)),
                                 hex(address - frame))
        self.assertEqual(candidate.state.allocated, 658)
        self.assertEqual(actual[0xA44:], b"\xa5" * (0xA88 - 0xA44))

    def test_maximum_connected_length_domain_fits_316_cells(self):
        bits = streams.BitStream()
        bits.emit(5, 3)
        bits.emit(29, 5)  # 286 literal/length cells.
        bits.emit(29, 5)  # 30 distance cells.
        bits.emit(14, 4)
        order = decoder.reference_data("2C120.rodata.s", "D_8002C15C")
        for symbol in order[:18]:
            bits.emit(1 if symbol in (0, 1) else 0, 3)
        lengths = [0] * 316
        for index in (65, 256, 286, 287):
            lengths[index] = 1
        for length in lengths:
            bits.emit(length, 1)
        bits.emit(0, 1)  # A.
        bits.emit(1, 1)  # End of block.
        candidate, model = self.assert_model(bits.data(), b"A", scratch_pattern=0xA5)
        self.compare_frame(candidate.state, model)
        self.assertEqual(FrameFixture.frame_bytes(candidate.state)[0xA38:0xA44],
                         bytes(model.memory[model.STACK + i] for i in range(0xA38, 0xA44)))

    def test_guest_workspace_base_translation_is_not_native_pointer_truncation(self):
        for base in (0x20000, 0x8003BE90, 0x807FD000):
            with self.subTest(base=hex(base)):
                model = tables.BuilderFixture([1, 2, 3, 3], bits=1, allocated=11)
                model.registers[22] = base
                model.WORKSPACE = base
                candidate = FrameFixture(self.library)
                candidate.state.workspaceAddress = base
                candidate.state.allocated = 11
                values = (ctypes.c_uint32 * 4)(1, 2, 3, 3)
                root, bits = ctypes.c_uint16(0xABCD), ctypes.c_uint32(1)
                result = self.library.init_decode_build(ctypes.byref(candidate.state),
                    values, 4, 4, None, None, ctypes.byref(root), ctypes.byref(bits))
                self.assertEqual(result, model.run())
                self.assertEqual((root.value, bits.value, candidate.state.allocated),
                                 (model.get(model.ROOT, 2), model.get(model.BITS, 4), model.fprs[19]))
                self.compare_frame(candidate.state, model)
                for address, size in model.writes:
                    if base <= address < base + model.fprs[19] * 4:
                        for byte in range(address, address + size):
                            index, offset = divmod(byte - base, 4)
                            entry = candidate.workspace[index]
                            encoded = bytes([entry.operation, entry.bits]) + struct.pack(">H", entry.value)
                            self.assertEqual(encoded[offset], model.memory[byte])


if __name__ == "__main__":
    unittest.main()
