"""Qualify immutable entry-value lifetime trials, not production adoption."""

import hashlib
import json
import struct
import subprocess
import sys
import unittest
from pathlib import Path

from tools.tests import test_init_decompressor_distance_operation_local as distance
from tools.tests import test_init_decompressor_semantic as semantic


class EntryValueChecks:
    def test_packed_profile_size_reduction(self):
        for profile, text, bound, frame in (
                ('o2g3', 4336, 400, 64), ('o1', 5808, 360, 56)):
            receipt = self.receipts['packed-remaining', profile]
            self.assertEqual(receipt['text_bytes'], text)
            compressed = next(row for row in receipt['functions']
                              if row['function'] == 'init_decode_compressed')
            words = self.compressed_words[profile]
            self.assertEqual((compressed['public_unit_words'], compressed['frame_bytes']),
                             (words, frame))
            core = next(row for row in receipt['call_graph']
                        if row['name'] == 'init_decode_core')
            self.assertEqual(core['direct_call_frame_bound'], bound)
            core_function = next(row for row in receipt['functions']
                                 if row['function'] == 'init_decode_core')
            padding = {('o2g3', 118): 2, ('o2g3', 119): 1,
                       ('o1', 157): 3, ('o1', 158): 2}[profile, words]
            self.assertEqual(core_function['body_words'], 50 if profile == 'o2g3' else 86)
            self.assertEqual(core_function['slot_words'] - core_function['body_words'], padding)
            image = next(image for label, selected, image in self.adapter_images
                         if label == 'packed-remaining' and selected == profile)
            self.assertEqual(len(image.code) * 4, text + 176)
            self.assertGreater(len(image.code) * 4, 3984)

    def test_disabled_option_keeps_both_default_instruction_images(self):
        output = self.directory.name + '/packed-remaining-shadow'
        # Compare a fresh disabled-option shadow control with its banked instruction hashes.
        baseline = Path(output) / 'disabled-control'
        result = subprocess.run([sys.executable,
            str(self.root / 'tools/experiments/compile_init_decompressor.py'),
            '--output', str(baseline), *self.shape_flags['packed-remaining'],
            '--abi-fpr-shadow', *distance.InitDecompressorDistanceOperationLocalTests.shadow_extra_flags],
            capture_output=True, text=True, check=True)
        receipts = json.loads(result.stdout)
        expected = {
            'o2g3': (4336, '177d7344426bb233f32c0cfbc92f40e533e2f344889f473bee0540e7bafeb62d'),
            'o1': (5808, '8797fe0eef6f346ea9a90a36e0206b76f648ec3dd5026c7a7f1f6b75d2fb6755'),
        }
        for profile, (size, digest) in expected.items():
            data = (baseline / (profile + '.o')).read_bytes()
            header = struct.unpack_from('>16sHHIIIIIHHHHHH', data)
            sections = [struct.unpack_from('>10I', data, header[6] + i * header[11])
                        for i in range(header[12])]
            names = sections[header[13]]
            strings = data[names[4]:names[4] + names[5]]
            text, = [section for section in sections
                     if strings[section[0]:].split(b'\0', 1)[0] == b'.text']
            body = data[text[4]:text[4] + text[5]]
            self.assertEqual((len(body), hashlib.sha256(body).hexdigest()), (size, digest))
            self.assertEqual(receipts[profile]['text_bytes'], size)
            self.assertEqual((baseline / (profile + '.log')).read_text(), '')

    @classmethod
    def tearDownClass(cls):
        if not any(cls.maximum_depths.values()):
            return
        output = cls.root / 'conker/build/init-entry-value-local'
        output.mkdir(parents=True, exist_ok=True)
        report = {'mode': cls.mode, 'qualification': 'bounded-connected-fixtures-only',
                  'adapter_bytes': 176, 'retail_bytes': 3984,
                  'profiles': {profile: cls.receipts['packed-remaining', profile]
                               for profile in ('o2g3', 'o1')},
                  'maximum_depths': {'%s/%s' % key: value
                                     for key, value in cls.maximum_depths.items()}}
        (output / (cls.mode + '-qualification.json')).write_text(
            json.dumps(report, indent=2) + '\n')


class InitDecompressorBothEntryValuesTests(
        EntryValueChecks, distance.InitDecompressorDistanceOperationLocalTests):
    mode = 'both'
    compressed_words = {'o2g3': 118, 'o1': 158}
    shadow_extra_flags = (*distance.InitDecompressorDistanceOperationLocalTests.shadow_extra_flags,
                          '--entry-value-local', mode)


class InitDecompressorLiteralEntryValueTests(
        EntryValueChecks, distance.InitDecompressorDistanceOperationLocalTests):
    mode = 'literal'
    compressed_words = {'o2g3': 118, 'o1': 157}
    shadow_extra_flags = (*distance.InitDecompressorDistanceOperationLocalTests.shadow_extra_flags,
                          '--entry-value-local', mode)


class InitDecompressorDistanceEntryValueTests(
        EntryValueChecks, distance.InitDecompressorDistanceOperationLocalTests):
    mode = 'distance'
    compressed_words = {'o2g3': 119, 'o1': 158}
    shadow_extra_flags = (*distance.InitDecompressorDistanceOperationLocalTests.shadow_extra_flags,
                          '--entry-value-local', mode)


class InitDecompressorNativeEntryValueTests(semantic.InitDecompressorSemanticTests):
    compiler_flags = ('-DINIT_DECODE_ENTRY_VALUE_LOCAL=1',)


if __name__ == '__main__':
    unittest.main()
