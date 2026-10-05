"""Qualify opt-in byte-depth fitting; production entry and stack gates remain."""

import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path

from tools.tests import test_init_decompressor_complement_low_mask as mask
from tools.tests import test_init_decompressor_distance_operation_local as distance
from tools.tests import test_init_decompressor_semantic as semantic
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture
from tools.tests.test_init_decompressor_tables import BuilderFixture


class InitDecompressorBuilderByteLevelTests(
        distance.InitDecompressorDistanceOperationLocalTests):
    shadow_extra_flags = (*distance.InitDecompressorDistanceOperationLocalTests.shadow_extra_flags,
                          '--builder-byte-level')

    def test_packed_profile_size_reduction(self):
        for profile, text, bound, region, public, frame, compressed, digest in (
                ('o2g3', 4320, 400, 398, 330, 200, 119,
                 'dce986104060637a90746c3c16c711b2bd792ee835c699c87a13904fb173082a'),
                ('o1', 5792, 360, 556, 484, 120, 157,
                 'fff009d0196e62e0cbf661ac1398edf62d02c8943a8032171889b02999567394')):
            receipt = self.receipts['packed-remaining', profile]
            self.assertEqual(receipt['text_bytes'], text)
            builder = next(row for row in receipt['functions']
                           if row['function'] == 'init_decode_build')
            self.assertEqual((builder['slot_words'], builder['public_unit_words'],
                              builder['frame_bytes']), (region, public, frame))
            embedded = [row['slot_words'] for row in builder['embedded_helpers']]
            self.assertEqual(embedded, [22, 46] if profile == 'o2g3' else [27, 45])
            self.assertEqual(public + sum(embedded), region)
            core = next(row for row in receipt['call_graph']
                        if row['name'] == 'init_decode_core')
            self.assertEqual(core['direct_call_frame_bound'], bound)
            row = next(row for row in receipt['functions']
                       if row['function'] == 'init_decode_compressed')
            self.assertEqual(row['public_unit_words'], compressed)
            image = next(image for label, selected, image in self.adapter_images
                         if label == 'packed-remaining' and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 176)
            self.assertGreater(len(image.code) * 4, 3984)
            body = mask.object_text(Path(self.directory.name) /
                                    'packed-remaining-shadow' / (profile + '.o'))
            self.assertEqual(hashlib.sha256(body).hexdigest(), digest)

    def test_disabled_option_keeps_banked_packed_instruction_images(self):
        output = Path(self.directory.name) / 'disabled-byte-level-control'
        result = subprocess.run([sys.executable,
            str(self.root / 'tools/experiments/compile_init_decompressor.py'),
            '--output', str(output), *self.shape_flags['packed-remaining'],
            '--abi-fpr-shadow',
            *distance.InitDecompressorDistanceOperationLocalTests.shadow_extra_flags],
            capture_output=True, text=True, check=True)
        receipts = json.loads(result.stdout)
        for profile, size, digest in (
                ('o2g3', 4336, '177d7344426bb233f32c0cfbc92f40e533e2f344889f473bee0540e7bafeb62d'),
                ('o1', 5808, '8797fe0eef6f346ea9a90a36e0206b76f648ec3dd5026c7a7f1f6b75d2fb6755')):
            body = mask.object_text(output / (profile + '.o'))
            self.assertEqual((len(body), hashlib.sha256(body).hexdigest()), (size, digest))
            self.assertEqual(receipts[profile]['text_bytes'], size)
            self.assertEqual((output / (profile + '.log')).read_text(), '')

    def test_ordered_depth_table_publications_match_retail(self):
        class RetailDepthFixture(BuilderFixture):
            def __init__(self, *args, **kwargs):
                self.depth_writes = []
                self.watch = False
                super().__init__(*args, **kwargs)
                self.watch = True

            def put(self, address, value, size):
                super().put(address, value, size)
                first = self.STACK + 0x44
                if self.watch and first <= address < first + 0x40:
                    self.depth_writes.append((address - first, value, size))

        class CandidateDepthFixture(GuestBuilderFixture):
            def __init__(self, *args, **kwargs):
                self.depth_writes = []
                self.watch = False
                super().__init__(*args, **kwargs)
                self.watch = True

            def put(self, address, value, size):
                super().put(address, value, size)
                first = self.FRAME + 0x44
                if self.watch and first <= address < first + 0x40:
                    self.depth_writes.append((address - first, value, size))

        for lengths in ([1, 2, 3, 3], list(range(1, 16)) + [16, 16]):
            for width in (1, 4, 9):
                reference = RetailDepthFixture(lengths, bits=width, allocated=11)
                expected = reference.run()
                self.assertGreater(len(reference.depth_writes), 1)
                for label, profile, image in self.adapter_images:
                    with self.subTest(shape=label, profile=profile,
                                      depth=max(lengths), width=width):
                        guest = CandidateDepthFixture(image, lengths, bits=width, allocated=11)
                        self.assertEqual(guest.run(), expected)
                        self.assertEqual(guest.depth_writes, reference.depth_writes)
                        for offset, _, size in guest.depth_writes:
                            self.assertEqual((offset & 3, size), (0, 4))

    @classmethod
    def tearDownClass(cls):
        if not any(cls.maximum_depths.values()):
            return
        output = cls.root / 'conker/build/init-builder-byte-level-20261004'
        output.mkdir(parents=True, exist_ok=True)
        report = {'qualification': 'bounded-connected-fixtures-only; opt-in fitting',
                  'adapter_bytes': 176, 'retail_bytes': 3984,
                  'profiles': {profile: cls.receipts['packed-remaining', profile]
                               for profile in ('o2g3', 'o1')},
                  'maximum_depths': {'%s/%s' % key: value
                                     for key, value in cls.maximum_depths.items()}}
        (output / 'qualification.json').write_text(json.dumps(report, indent=2) + '\n')


class InitDecompressorNativeBuilderByteLevelTests(semantic.InitDecompressorSemanticTests):
    compiler_flags = ('-DINIT_DECODE_BUILDER_BYTE_LEVEL',)


if __name__ == '__main__':
    unittest.main()
