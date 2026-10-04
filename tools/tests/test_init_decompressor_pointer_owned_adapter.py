import subprocess
import sys
import unittest

from tools.tests import test_init_decompressor_tight_adapter as tight


class PointerOwnedFixture(tight.InitDecompressorTightAdapterTests.fixture_type):
    CORE_FIELDS = (*tight.InitDecompressorTightAdapterTests.fixture_type.CORE_FIELDS, 0)

    def __init__(self, *args):
        self.fifth_fence = False
        self.fifth_initialized = False
        super().__init__(*args)
        # The fifth argument is no longer initialized or consumed by this core.
        super().put(self.adapter_state - 0x10, 0xCCBADBAD, 4)
        self.fifth_fence = True

    def get(self, address, size):
        if self.fifth_fence:
            field = self.adapter_state - 0x10
            if address < field + 4 and field < address + size and not self.fifth_initialized:
                raise AssertionError("fifth slot read before initialization")
        return super().get(address, size)

    def put(self, address, value, size):
        super().put(address, value, size)
        if self.fifth_fence:
            field = self.adapter_state - 0x10
            if address <= field and field + 4 <= address + size:
                self.fifth_initialized = True


class InitDecompressorPointerOwnedAdapterTests(tight.InitDecompressorTightAdapterTests):
    shadow_extra_flags = (*tight.InitDecompressorTightAdapterTests.shadow_extra_flags,
                          "--core-pointer-arguments")
    shadow_adapter_flags = (*tight.InitDecompressorTightAdapterTests.shadow_adapter_flags,
                            "--defsym", "INIT_DECODE_CORE_POINTER_ARGUMENTS=1")
    shadow_adapter_bytes = 176
    fixture_type = PointerOwnedFixture

    def test_packed_profile_size_reduction(self):
        for profile, text, bound in (("o2g3", 4384, 392), ("o1", 5792, 352)):
            receipt = self.receipts["packed-remaining", profile]
            self.assertEqual(receipt["text_bytes"], text)
            core = next(unit for unit in receipt["call_graph"]
                        if unit["name"] == "init_decode_core")
            self.assertEqual(core["direct_call_frame_bound"], bound)
            image = next(image for label, selected, image in self.adapter_images
                         if label == "packed-remaining" and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 176)
            code_end = max(image.code) + 4
            following = min(first for first, last in image.readonly if first >= code_end)
            self.assertEqual(following, code_end)

    def test_input_pointer_poison_and_omitted_stores(self):
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile):
                start = image.symbols["init_decode_retail_core_adapter"]
                end = image.symbols["init_decode_retail_core_adapter_end"]
                words = [image.code[pc] for pc in range(start, end, 4)]
                self.assertNotIn(0xAFA20010, words)
                self.assertNotIn(0xAFA40020, words)
                guest = self.fixture_type(image, b"\x11\x72\x01\0\0\xff\xff",
                                          0x0400FF00)
                with self.assertRaisesRegex(AssertionError, "core field read before initialization: 0"):
                    guest.get(guest.adapter_state, 4)
                guest.context()
                self.assertIn(0, guest.initialized_fields)
                for word, message in ((0x8C880000, "core field read before initialization: 0"),
                                      (0x8FA80010, "fifth slot read before initialization")):
                    broken = self.fixture_type(image, b"\x11\x72\x01\0\0\xff\xff",
                                               0x0400FF00)
                    # Executed early reads must fail before initialization.
                    broken.code[image.symbols["init_decode_core"]] = word
                    with self.assertRaisesRegex(AssertionError, message):
                        broken.context()

    def test_pointer_arguments_require_frame_backing(self):
        result = subprocess.run([sys.executable,
            str(self.root / "tools/experiments/compile_init_decompressor.py"),
            "--core-pointer-arguments"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--core-pointer-arguments requires --frame-backed", result.stderr)


class InitDecompressorPointerOwnedAdapterCorpusTests(tight.InitDecompressorTightAdapterCorpusTests):
    shadow_extra_flags = InitDecompressorPointerOwnedAdapterTests.shadow_extra_flags
    shadow_adapter_flags = InitDecompressorPointerOwnedAdapterTests.shadow_adapter_flags
    fixture_type = PointerOwnedFixture


if __name__ == "__main__":
    unittest.main()
