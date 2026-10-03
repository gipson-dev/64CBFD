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


class ShadowExceptionFixture(adapter.GuestExceptionFixture):
    ADAPTER_EXTRA = 0x98


class InitDecompressorGuestFprShadowTests(unittest.TestCase):
    fixture_type = ShadowExceptionFixture
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
                "--output", str(output), *flags, "--abi-fpr-shadow"],
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

    def test_shadow_requires_frame_backing(self):
        result = subprocess.run([sys.executable,
            str(self.root / "tools/experiments/compile_init_decompressor.py"),
            "--abi-fpr-shadow"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires --frame-backed", result.stderr)

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
