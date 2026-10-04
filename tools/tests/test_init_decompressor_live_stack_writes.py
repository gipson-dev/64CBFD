import unittest

from tools.tests import test_init_decompressor_direct_fpr_adapter as direct
from tools.tests import test_init_decompressor_callee_preserving_adapter as callee
from tools.tests import test_init_decompressor_exception as exception


class LiveStackWriteFixture(callee.CalleePreservingFixture):
    """Live-SP write fence, not proof of the retail stack reservation."""

    def __init__(self, *args):
        self.live_stack_fence = False
        super().__init__(*args)

    def execute(self, word):
        super().execute(word)
        # Retail first saves the incoming SP, then switches to its private stack.
        if word == 0x249D0000:
            if self.registers[29] != exception.CONTEXT_TOP:
                raise AssertionError("unexpected private stack switch")
            self.live_stack_fence = True

    def put(self, address, value, size):
        if self.live_stack_fence:
            first, last = self.NEIGHBOR_END, exception.CONTEXT_TOP + 4
            if address < last and first < address + size:
                if address < self.registers[29]:
                    raise AssertionError("stack write below live SP")
        super().put(address, value, size)


class InitDecompressorLiveStackWriteTests(direct.InitDecompressorDirectFprAdapterTests):
    fixture_type = LiveStackWriteFixture

    def test_live_sp_fence_and_executed_below_frame_store(self):
        chunk = b"\x11\x72\x01\0\0\xff\xff"
        for label, profile, image in self.adapter_images:
            for cu1 in (0, exception.SR_CU1):
                with self.subTest(shape=label, profile=profile, cu1=cu1):
                    status = exception.SR_FR | 0xFF00 | cu1
                    guest = self.fixture_type(image, chunk, status)
                    self.assertFalse(guest.live_stack_fence)
                    guest.context()
                    self.assertTrue(guest.live_stack_fence)
                    entry = image.symbols["init_decode_retail_core_adapter"]
                    end = image.symbols["init_decode_retail_core_adapter_end"]
                    stores = [pc for pc, word in image.code.items()
                              if entry <= pc < end and word == 0xAFB00A48]
                    self.assertEqual(len(stores), 1)
                    broken = self.fixture_type(image, chunk, status)
                    # This store crosses live SP but stays above the neighbor fence.
                    self.assertGreater(broken.STACK - 0xA88 - 4, broken.NEIGHBOR_END)
                    broken.code[stores[0]] = 0xAFB0FFFC
                    with self.assertRaisesRegex(AssertionError, "stack write below live SP"):
                        broken.context()

    def test_live_sp_fence_exact_boundary_and_crossing(self):
        image = self.adapter_images[0][2]
        guest = self.fixture_type(image, b"\x11\x72\x01\0\0\xff\xff",
                                  exception.SR_FR | 0xFF00)
        guest.registers[29] = guest.FRAME
        guest.live_stack_fence = True
        guest.put(guest.FRAME, 0x12345678, 4)
        guest.put(guest.FRAME + 4, 0x12345678, 4)
        for address, size in ((guest.FRAME - 4, 4), (guest.FRAME - 1, 4)):
            with self.assertRaisesRegex(AssertionError, "stack write below live SP"):
                guest.put(address, 0, size)
        guest.put(guest.OUTPUT, 0x42, 1)


class InitDecompressorLiveStackWriteCorpusTests(direct.InitDecompressorDirectFprAdapterCorpusTests):
    fixture_type = LiveStackWriteFixture


if __name__ == "__main__":
    unittest.main()
