import json
import subprocess
import sys
import unittest
import zlib
from pathlib import Path

from tools.tests import test_init_decompressor_guest_adapter as adapter
from tools.tests import test_init_decompressor_fpr_provenance as provenance
from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests import test_init_decompressor_tables as tables


class ShadowExceptionFixture(adapter.GuestExceptionFixture):
    ADAPTER_EXTRA = 0x98
    NEIGHBOR_END = 0x80031D10

    def __init__(self, image, chunk, status):
        super().__init__(image, chunk, status)
        self.readonly.append((0x80031AE0, self.NEIGHBOR_END))
        self.allowed_writes[-1] = (self.NEIGHBOR_END, exception.CONTEXT_TOP + 4)


class InitDecompressorGuestFprShadowTests(unittest.TestCase):
    fixture_type = ShadowExceptionFixture
    compare_scratch_fprs = True
    compare = adapter.InitDecompressorCompiledGuestAdapterTests.compare

    @classmethod
    def setUpClass(cls):
        adapter.InitDecompressorCompiledGuestAdapterTests.setUpClass.__func__(cls)
        directory = Path(cls.directory.name)
        shadow_adapter = directory / "shadow-adapter.o"
        result = subprocess.run(["mips-linux-gnu-as", "-mips3", "-32", "--defsym",
            "INIT_DECODE_ABI_FPR_SHADOW=1", "-o", str(shadow_adapter),
            str(cls.root / "tools/experiments/init_decompressor_core_adapter.s")],
            capture_output=True, text=True, check=True)
        if result.stdout or result.stderr:
            raise AssertionError("shadow adapter assembly log is not empty")
        cls.adapter_images, cls.receipts, cls.maximum_depths = [], {}, {}
        for label, flags in cls.shape_flags.items():
            output = directory / (label + "-shadow")
            result = subprocess.run([sys.executable,
                str(cls.root / "tools/experiments/compile_init_decompressor.py"),
                "--output", str(output), *flags, "--abi-fpr-shadow",
                *getattr(cls, "shadow_extra_flags", ())],
                capture_output=True, text=True, check=True)
            receipts = json.loads(result.stdout)
            if set(receipts) != {"o2g3", "o1"}:
                raise AssertionError("both shadow profiles are required")
            for profile, receipt in receipts.items():
                if receipt["state_bytes"] != 116 or receipt["entry_bytes"] != 4:
                    raise AssertionError("shadow state/entry layout changed")
                if (output / (profile + ".log")).read_text():
                    raise AssertionError("shadow compiler log is not empty")
                executable = output / (profile + "-adapter.elf")
                result = subprocess.run(["mips-linux-gnu-ld", "-Ttext", "0x10400000",
                    "-Tdata", "0x10500000", "-e", "init_decode_build", "-o", str(executable),
                    str(output / (profile + ".o")), str(shadow_adapter)],
                    capture_output=True, text=True, check=True)
                if result.stdout or result.stderr:
                    raise AssertionError("shadow link log is not empty")
                image = adapter.GuestImage(executable.read_bytes())
                cls.adapter_images.append((label, profile, image))
                cls.receipts[label, profile] = receipt
                cls.maximum_depths[label, profile] = 0

    @staticmethod
    def dynamic_bits(distance_lengths=(1,), final=True):
        bits = streams.BitStream()
        bits.emit(4 | int(final), 3)
        bits.emit(0, 5)
        bits.emit(len(distance_lengths) - 1, 5)
        bits.emit(14, 4)
        lengths = [0] * 19
        lengths[0], lengths[1], lengths[2] = 1, 2, 2
        order = decoder.reference_data("2C120.rodata.s", "D_8002C15C")
        for symbol in order[:18]:
            bits.emit(lengths[symbol], 3)
        codes = {symbol: (code, width) for symbol, width, code in
                 tables.InitDecompressorTableTests.canonical(lengths)}
        literal_lengths = [0] * 257
        literal_lengths[65] = literal_lengths[256] = 1
        for width in (*literal_lengths, *distance_lengths):
            bits.emit(*codes[width])
        bits.emit(0, 1)
        bits.emit(1, 1)
        return bits

    def assert_builder_gate(self, raw, calls, output=b"", result=0):
        fixture = provenance.FprProvenanceFixture(b"\x11\x72" + raw,
            exception.SR_FR | exception.SR_CU1 | 0xFF01)
        fixture.capture.add(0x100067E0)
        fixture.context()
        self.assertEqual(fixture.visits.get(0x1000696C, 0), calls)
        registers, fprs = fixture.snapshots[0x10005F34]
        self.assertEqual(registers[2], result)
        self.assertEqual(fprs[17], len(output))
        self.assertEqual(bytes(fixture.memory[fixture.OUTPUT + i]
                               for i in range(len(output))), output)
        return fixture

    def test_distance_builder_failures_and_empty_tree(self):
        for distance_lengths, output, result in (((2, 2), b"", 0),
                                                  ((1, 1, 2), b"", 0),
                                                  ((1, 1, 1), b"A", 1),
                                                  ((0,), b"A", 1)):
            raw = self.dynamic_bits(distance_lengths).data()
            reference = self.assert_builder_gate(raw, 3, output, result)
            self.assertEqual(reference.snapshots[0x100067E0][0][2] != 0, result == 0)
            self.assertEqual(reference.visits.get(0x10006E00, 0), int(result != 0))
            for cu1 in (False, True):
                self.compare(b"\x11\x72" + raw,
                    exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF01,
                    expected_output=output, expected_result=result)

    def test_multiple_dynamic_blocks_and_retained_snapshot_errors(self):
        cases = []
        for ending, calls, output, result in (
                (self.dynamic_bits(), 6, b"AA", 2),
                (self.dynamic_bits((2, 2)), 6, b"A", 0)):
            prefix = self.dynamic_bits(final=False)
            prefix.bits.extend(ending.bits)
            cases.append((prefix.data(), calls, output, result))
        for ending, calls in ((streams.InitDecompressorStreamTests().dynamic(overflow=True), 4),
                               (b"\x07", 3)):
            prefix = self.dynamic_bits(final=False)
            prefix.bits.extend((byte >> i) & 1 for byte in ending for i in range(8))
            cases.append((prefix.data(), calls, b"A", 0))
        prefix = self.dynamic_bits(final=False)
        prefix.emit(5, 3)
        prefix.emit(30, 5)
        prefix.emit(0, 9)
        cases.append((prefix.data(), 3, b"A", 0))
        prefix = self.dynamic_bits(final=False)
        prefix.emit(0, 3)
        while len(prefix.bits) % 8:
            prefix.emit(0, 1)
        prefix.emit(2, 16)
        prefix.emit(0xFFFD, 16)
        for byte in b"XY":
            prefix.emit(byte, 8)
        prefix.bits.extend(self.dynamic_bits().bits)
        cases.append((prefix.data(), 6, b"AXYA", 4))
        fixed = decoder.InitDecompressorDecoderTests
        fixed_raw = fixed.encoded(b"BC")
        fixed_length = 3 + sum(fixed.codes[symbol][1] for symbol in (*b"BC", 256))
        for overflow in (False, True):
            prefix = self.dynamic_bits(final=False)
            fixed_bits = [(byte >> i) & 1 for byte in fixed_raw for i in range(8)][:fixed_length]
            fixed_bits[0] = 0
            prefix.bits.extend(fixed_bits)
            prefix.emit(0, 3)
            while len(prefix.bits) % 8:
                prefix.emit(0, 1)
            prefix.emit(0, 16)
            prefix.emit(0xFFFF, 16)
            ending = streams.InitDecompressorStreamTests().dynamic(overflow=True) if overflow else None
            prefix.bits.extend(((byte >> i) & 1 for byte in ending for i in range(8))
                               if overflow else self.dynamic_bits().bits)
            cases.append((prefix.data(), 4 if overflow else 6,
                          b"ABC" if overflow else b"ABCA", 0 if overflow else 4))
        for raw, calls, output, result in cases:
            self.assert_builder_gate(raw, calls, output, result)
            for cu1 in (False, True):
                self.compare(b"\x11\x72" + raw,
                    exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF01,
                    expected_output=output, expected_result=result)

    def test_shadow_requires_frame_backing(self):
        result = subprocess.run([sys.executable,
            str(self.root / "tools/experiments/compile_init_decompressor.py"),
            "--abi-fpr-shadow"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires --frame-backed", result.stderr)

    def test_neighbor_thread_redzone_rejects_writes(self):
        image = self.adapter_images[0][2]
        chunk = exception.InitDecompressorExceptionTests.chunks()[0][0]
        fixture = self.fixture_type(image, chunk, exception.SR_FR | exception.SR_CU1 | 0xFF01)
        with self.assertRaisesRegex(AssertionError, "read-only"):
            fixture.put(fixture.NEIGHBOR_END - 4, 0, 4)
        with self.assertRaisesRegex(AssertionError, "read-only"):
            fixture.put(fixture.NEIGHBOR_END - 2, 0, 4)

    def test_match_history_before_dynamic_success_and_early_failure(self):
        encoder = zlib.compressobj(wbits=-15, strategy=zlib.Z_FIXED)
        payload = b"ABCD" * 24
        prefix = encoder.compress(payload) + encoder.flush(zlib.Z_SYNC_FLUSH)
        self.assertEqual((prefix[0] >> 1) & 3, 1)
        dynamic = streams.InitDecompressorStreamTests().dynamic
        for overflow in (False, True):
            raw = prefix + dynamic(overflow=overflow)
            for cu1 in (False, True):
                self.compare(b"\x11\x72" + raw,
                    exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF01,
                    expected_output=payload if overflow else payload + b"A",
                    expected_result=0 if overflow else len(payload) + 1)

    def test_cu1_clear_contexts(self):
        adapter.InitDecompressorCompiledGuestAdapterTests.test_cu1_clear_success_and_failure_contexts(self)

    def test_cu1_set_contexts(self):
        status = exception.SR_FR | exception.SR_CU1 | 0xFF01
        for chunk, output in exception.InitDecompressorExceptionTests.chunks():
            self.compare(chunk, status, expected_output=output, expected_result=len(output))
        dynamic = streams.InitDecompressorStreamTests().dynamic
        for raw in (b"\x07", dynamic(overflow=True),
                    provenance.InitDecompressorFprProvenanceTests.after_fixed(dynamic()),
                    provenance.InitDecompressorFprProvenanceTests.after_fixed(dynamic(overflow=True)),
                    b"\x00\x01\0\xfe\xffZ\x07"):
            self.compare(b"\x11\x72" + raw, status)

    def test_incomplete_literal_trees_both_status_paths(self):
        maker = provenance.InitDecompressorFprProvenanceTests.incomplete_literal_tree
        after_fixed = provenance.InitDecompressorFprProvenanceTests.after_fixed
        for raw in (maker(), maker(repeats=True), maker(sparse=True),
                    after_fixed(maker()), after_fixed(maker(repeats=True))):
            for cu1 in (False, True):
                self.compare(b"\x11\x72" + raw,
                    exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF01)

    def test_retail_samples_both_status_paths_and_costs(self):
        for index in (0, 169, 506):
            _, start, end, _, output = self.pages[index]
            dma_size = (end - start + 15) & ~15
            for cu1 in (False, True):
                self.compare(self.rom[start:start + dma_size],
                    exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF01,
                    expected_output=output, expected_result=len(output), dma_size=dma_size)
        for label, profile, image in self.adapter_images:
            body = (image.symbols["init_decode_retail_core_adapter_end"] -
                    image.symbols["init_decode_retail_core_adapter"])
            self.assertEqual(body, 320)
            bound = next(unit["direct_call_frame_bound"] for unit in
                         self.receipts[label, profile]["call_graph"]
                         if unit["name"] == "init_decode_core")
            print("shadow receipt: %s/%s body=%d text=%d bound=%d observed=%d" %
                  (label, profile, body, len(image.code) * 4,
                   0xA88 + ShadowExceptionFixture.ADAPTER_EXTRA + bound,
                   self.maximum_depths[label, profile]), flush=True)


if __name__ == "__main__":
    unittest.main()
