import os
import unittest

from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_guest_fpr_shadow as shadow


@unittest.skipUnless(os.environ.get("CONKER_INIT_SHADOW_CORPUS") == "1",
                     "Opt-in compiled shadow corpus")
class InitDecompressorShadowCorpusTests(unittest.TestCase):
    fixture_type = shadow.ShadowExceptionFixture
    compare_scratch_fprs = True
    compare = shadow.InitDecompressorGuestFprShadowTests.compare

    @classmethod
    def setUpClass(cls):
        shadow.InitDecompressorGuestFprShadowTests.setUpClass.__func__(cls)
        if len(cls.adapter_images) != 6:
            raise AssertionError("six freshly compiled shadow images required")
        selected = os.environ.get("CONKER_INIT_SHADOW_CORPUS_PROFILE")
        if selected:
            cls.adapter_images = [row for row in cls.adapter_images
                                  if "%s/%s" % row[:2] == selected]
            if len(cls.adapter_images) != 1:
                raise ValueError("Unknown shadow corpus profile: " + selected)

    def test_all_507_retail_pages_cu1_set(self):
        self.assertEqual(len(self.pages), 507)
        completed = 0
        for index, start, end, chunk, output in self.pages:
            with self.subTest(page=index):
                dma_size = (end - start + 15) & ~15
                supplied = self.rom[start:start + dma_size]
                self.assertEqual(supplied[:len(chunk)], chunk)
                offset = 0x2D4B0 + index * 0x1000
                self.assertEqual(output, self.image[offset:offset + len(output)])
                self.compare(supplied, exception.SR_FR | exception.SR_CU1 | 0xFF01,
                    expected_output=output, expected_result=len(output), dma_size=dma_size)
                completed += len(self.adapter_images)
            if (index + 1) % 16 == 0 or index == 506:
                print("shadow CU1-set corpus: pages=%d/507 runs=%d/%d" %
                      (index + 1, completed, 507 * len(self.adapter_images)), flush=True)
        self.assertEqual(completed, 507 * len(self.adapter_images))
        for label, profile, image in self.adapter_images:
            depth = self.maximum_depths[label, profile]
            low = exception.CALLER_SP - depth
            self.assertGreaterEqual(low, self.fixture_type.NEIGHBOR_END)
            print("shadow corpus terminal: %s/%s pages=507 text=%d depth=%d low=0x%08X margin=%d" %
                  (label, profile, len(image.code) * 4, depth, low,
                   low - self.fixture_type.NEIGHBOR_END), flush=True)


if __name__ == "__main__":
    unittest.main()
