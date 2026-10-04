import subprocess
import unittest
from pathlib import Path

from tools.tests import test_init_decompressor_builder_scan_deficit as scan


class InitDecompressorTightAdapterTests(scan.InitDecompressorBuilderScanDeficitTests):
    shadow_adapter_flags = (*scan.InitDecompressorBuilderScanDeficitTests.shadow_adapter_flags,
                            "--defsym", "INIT_DECODE_TIGHT_ADAPTER=1")
    shadow_adapter_bytes = 184

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4384, 392), ("o1", 5792, 352)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 184)

    def test_saved_return_address_in_snapshot_branch_delay_slot(self):
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile):
                start = image.symbols["init_decode_retail_core_adapter"]
                end = image.symbols["init_decode_retail_core_adapter_end"]
                self.assertEqual(end - start, self.shadow_adapter_bytes)
                words = [image.code[pc] for pc in range(start, end, 4)]
                branches = [i for i, word in enumerate(words)
                            if word >> 26 == 4]
                self.assertEqual(len(branches), 1)
                self.assertEqual(words[branches[0] + 1], 0x8FBF0B18)
                self.assertEqual(words[-2:], [0x03E00008, 0x27BD0B20])
                self.assertNotIn(0x27BD0098, words)

    def test_tight_adapter_rejects_missing_contracts(self):
        cases = (([], "tight adapter requires ABI FPR shadow"),
                 (["--defsym", "INIT_DECODE_ABI_FPR_SHADOW=1"],
                  "tight adapter requires callee-preserving core"))
        for index, (flags, message) in enumerate(cases):
            with self.subTest(contract=message):
                result = subprocess.run(["mips-linux-gnu-as", "-mips3", "-32",
                    "--defsym", "INIT_DECODE_TIGHT_ADAPTER=1", *flags,
                    "-o", str(Path(self.directory.name) / ("invalid-tight-%d.o" % index)),
                    str(self.root / "tools/experiments/init_decompressor_core_adapter.s")],
                    capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(message, result.stderr)


class InitDecompressorTightAdapterCorpusTests(scan.InitDecompressorBuilderScanDeficitCorpusTests):
    shadow_adapter_flags = InitDecompressorTightAdapterTests.shadow_adapter_flags


if __name__ == "__main__":
    unittest.main()
