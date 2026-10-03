import struct
import unittest
import zlib

from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_guest_builder as builder
from tools.tests.init_decompressor_guest_oracle import GuestStreamFixture


class InitDecompressorGuestSignedBranchTests(unittest.TestCase):
    def test_signed_regular_and_likely_branches_preserve_delay_semantics(self):
        for opcode, variants in ((1, (0, 1, 2, 3)), (6, (0,)), (7, (0,)),
                                 (22, (0,)), (23, (0,))):
            for variant in variants:
                for value in (0xFFFFFFFF, 0, 1):
                    with self.subTest(opcode=opcode, variant=variant, value=value):
                        fixture = builder.InitDecompressorGuestInstructionTests.fixture()
                        fixture.registers[1], fixture.registers[2] = value, 0x1000
                        signed = fixture.signed(value)
                        if opcode == 1:
                            taken = signed < 0 if variant in (0, 2) else signed >= 0
                            likely = variant in (2, 3)
                        else:
                            taken = signed <= 0 if opcode in (6, 22) else signed > 0
                            likely = opcode in (22, 23)
                        fixture.code = {0: (opcode << 26) | (1 << 21) | (variant << 16) | 3,
                                        4: (43 << 26) | (2 << 21),
                                        8: 0x03E00008, 12: 0, 16: 0x03E00008, 20: 0}
                        fixture.run(entry=0, budget=8)
                        self.assertGreater(fixture.visits.get(16 if taken else 8, 0), 0)
                        self.assertEqual(fixture.get(0x1000, 4),
                                         0 if taken or not likely else 0xA5A5A5A5)

    def test_arithmetic_shift_extends_sign_then_preserves_low_word(self):
        for value, shift, expected in ((0xFFFFFFF0, 2, 0xFFFFFFFC),
                                      (0x80000000, 31, 0xFFFFFFFF), (0x7FFFFFFF, 31, 0)):
            with self.subTest(value=value, shift=shift):
                fixture = builder.InitDecompressorGuestInstructionTests.fixture()
                fixture.registers[1] = value
                fixture.execute((1 << 16) | (3 << 11) | (shift << 6) | 3)
                self.assertEqual(fixture.registers[3], expected)


class InitDecompressorCompiledGuestStreamTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        builder.InitDecompressorCompiledGuestBuilderTests.setUpClass.__func__(cls)
        decoder.InitDecompressorDecoderTests.setUpClass()

    def compare(self, raw, expected=None, limit=0x70000000, core=False,
                alignment=0, workspace=None, gate=None):
        model = streams.StreamFixture(raw, limit=limit)
        frame_base = model.STACK - 0xA88 if core else model.STACK
        model.memory.update((frame_base + index, 0xA5) for index in range(0xA44))
        model.memory.update((address, 0xA5) for address in range(model.WORKSPACE, model.ROOT))
        if core:
            model.capture = {0x100062F0}
            status = model.core(False, alignment=alignment, workspace=workspace)
            registers, _ = model.snapshots[0x100062F0]
            self.assertEqual(registers[29], frame_base)
        else:
            status = model.stream()
            registers = model.registers
        for label, profile, image, _ in self.images:
            with self.subTest(shape=label, profile=profile, core=core, limit=limit):
                original_readonly = tuple(image.readonly)
                guest = GuestStreamFixture(image, raw, limit=limit)
                self.assertEqual(tuple(image.readonly), original_readonly)
                self.assertEqual(guest.fixed_table, bytes(model.memory.get(model.FIXED_BASE + i, 0xA5)
                                                         for i in range(658 * 4)))
                result = guest.core(alignment=alignment, workspace=workspace) if core else guest.stream()
                self.assertEqual(result, status)
                state = [guest.get(guest.STATE + index * 4, 4) for index in range(10)]
                active_workspace = model.WORKSPACE if workspace is None else workspace
                self.assertEqual(state, [registers[23], model.OUTPUT, active_workspace,
                    registers[28], registers[30], model.fprs[17], model.fprs[18], model.fprs[19],
                    guest.FRAME, active_workspace])
                if expected is not None:
                    self.assertEqual(bytes(guest.memory[guest.OUTPUT + i] for i in range(len(expected))),
                                     expected)
                    if not core and status == 0:
                        self.assertEqual(zlib.decompress(raw, -15), expected)
                changed = {current for address, size in (*model.writes, *guest.writes)
                           if model.OUTPUT <= address < model.INPUT or model.WORKSPACE <= address < model.ROOT
                           for current in range(address, address + size)}
                for current in changed:
                    self.assertEqual(guest.memory[current], model.memory.get(current, 0xA5), hex(current))
                self.assertEqual(bytes(guest.memory[guest.FRAME + i] for i in range(0xA44)),
                                 bytes(model.memory[frame_base + i] for i in range(0xA44)))
                for register in (*range(16, 24), 28, 29, 30, 31):
                    self.assertEqual(guest.registers[register], guest.before[register])
                unit = next(unit for unit in self.receipts[label, profile]["call_graph"]
                            if unit["name"] == ("init_decode_core" if core else "init_decode_stream"))
                self.assertLessEqual(guest.STACK - guest.min_sp, unit["direct_call_frame_bound"])
                for first, last in ((guest.FRAME - 16, guest.FRAME),
                                    (guest.FRAME + 0xA44, guest.FRAME + 0xA88 + 16),
                                    (guest.OUTPUT - 16, guest.OUTPUT)):
                    self.assertEqual(bytes(guest.memory[address] for address in range(first, last)),
                                     b"\xa5" * (last - first))
                gates = {gate: 1} if isinstance(gate, str) else gate or {}
                for name, minimum in gates.items():
                    self.assertGreaterEqual(guest.visits.get(image.symbols[name], 0), minimum)

    def test_stored_and_fixed_streams(self):
        for payload in (b"", b"Conker\0\xff", bytes(range(256))):
            stored = b"\x01" + struct.pack("<HH", len(payload), len(payload) ^ 0xFFFF) + payload
            self.compare(stored, expected=payload, gate="init_decode_stored")
            self.compare(decoder.InitDecompressorDecoderTests.encoded(payload), expected=payload,
                         gate="init_decode_compressed")
        self.compare(decoder.InitDecompressorDecoderTests.encoded([ord("A"), (258, 1)]),
                     expected=b"A" * 259, gate="init_decode_compressed")
        self.compare(decoder.InitDecompressorDecoderTests.encoded([ord("A"), (3, 2)]))

    def test_dynamic_and_partial_error_state(self):
        fixture = streams.InitDecompressorStreamTests()
        self.compare(fixture.dynamic(), expected=b"A", gate="init_decode_dynamic")
        for raw in (b"\x07", fixture.dynamic(overflow=True), fixture.dynamic(repeat_first=True),
                    decoder.InitDecompressorDecoderTests.encoded([ord("A"), 286], terminate=False)):
            self.compare(raw)
        stored = b"\x00" + struct.pack("<HH", 2, 0xFFFD) + b"XY"
        self.compare(stored + fixture.dynamic(overflow=True), expected=b"XY")

    def test_strict_limits(self):
        self.compare(b"\x01\x01\x00\xff\xffA")
        for limit in (0, 1, 2, 3, 4, 5):
            self.compare(b"\x01\x01\x00\xfe\xffA", limit=limit)
            self.compare(decoder.InitDecompressorDecoderTests.encoded([ord("A"), (3, 1)]), limit=limit)

    def test_core_headers_alignment_and_workspace_limit(self):
        dynamic = streams.InitDecompressorStreamTests().dynamic()
        for header in (b"\x11\x72", b"\x11\x73\0\0"):
            for alignment in range(4):
                for workspace in (0x20000, 0x42000):
                    self.compare(b"\xa5" * alignment + header + dynamic, expected=b"A", core=True,
                                 alignment=alignment, workspace=workspace, gate="init_decode_dynamic")
        self.compare(b"\x11\x72\x07", core=True)

    def test_generated_dynamic_mixed_blocks_and_core_partial_failure(self):
        for payload in (b"Conker dynamic block with repeated text " * 256, bytes(range(128)) * 64):
            encoder = zlib.compressobj(level=6, wbits=-15)
            raw = encoder.compress(payload) + encoder.flush()
            self.assertEqual(raw[0] >> 1 & 3, 2)
            self.compare(raw, expected=payload, gate="init_decode_dynamic")
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
        while len(bits.bits) & 7:
            bits.emit(0, 1)
        bits.emit(0, 16)
        bits.emit(0xFFFF, 16)
        dynamic = streams.InitDecompressorStreamTests()
        self.compare(bits.data() + dynamic.dynamic(), expected=b"XYBCA",
                     gate={"init_decode_stored": 2, "init_decode_compressed": 2, "init_decode_dynamic": 1})
        self.compare(b"\x11\x72" + stored + dynamic.dynamic(overflow=True), expected=b"XY", core=True)


if __name__ == "__main__":
    unittest.main()
