"""Qualify a size-neutral mask experiment, not production decoder adoption."""

import hashlib
import json
import struct
import subprocess
import sys
import unittest
from pathlib import Path

from tools.pad_generated_object import ELF_HEADER, SECTION_HEADER, read_c_string
from tools.tests import test_init_bitmap_unsigned_induction as bitmap
from tools.tests import test_init_decompressor_distance_operation_local as distance
from tools.tests import test_init_decompressor_semantic as semantic


def object_text(path):
    data = path.read_bytes()
    header = ELF_HEADER.unpack_from(data)
    if header[0][:7] != b'\x7fELF\x01\x02\x01' or header[2] != 8:
        raise AssertionError('expected big-endian ELF32 MIPS')
    sections = list(SECTION_HEADER.iter_unpack(
        data[header[6]:header[6] + header[11] * header[12]]))
    strings = sections[header[13]]
    names = data[strings[4]:strings[4] + strings[5]]
    section, = [section for section in sections
                if read_c_string(names, section[0]) == '.text']
    return data[section[4]:section[4] + section[5]]


class InitDecompressorComplementLowMaskTests(
        distance.InitDecompressorDistanceOperationLocalTests):
    shadow_extra_flags = (*distance.InitDecompressorDistanceOperationLocalTests.shadow_extra_flags,
                          '--complement-low-mask')

    def test_compiled_mask_all_shift_classes_and_high_width_bits(self):
        widths = [*range(256), 0x7FFFFFFF, 0x80000000, 0xFFFFFFFF]
        for label, profile, image in self.adapter_images:
            receipt = self.receipts[label, profile]
            builder = next(unit for unit in receipt['call_graph']
                           if unit['name'] == 'init_decode_build')
            base = image.symbols['init_decode_build'] - builder['entry']
            first = next(unit for unit in receipt['call_graph'] if unit['entry'] == 0)
            self.assertEqual((first['slot_words'], first['frame_bytes']),
                             (6 if profile == 'o2g3' else 5, 0))
            code = {pc: image.code[pc] for pc in range(base, base + first['slot_words'] * 4, 4)}
            for width in widths:
                with self.subTest(shape=label, profile=profile, width=width):
                    guest = bitmap.BitmapGuestFixture(code, {}, set())
                    guest.registers[4] = width
                    self.assertEqual(guest.run(entry=base, budget=8),
                                     (1 << (width & 31)) - 1)
                    self.assertEqual((guest.reads, guest.writes), ([], []))
                    for register in (*range(16, 24), 28, 29, 30, 31):
                        self.assertEqual(guest.registers[register], guest.before[register])

    def test_only_two_packed_words_change_and_disabled_images_stay_exact(self):
        output = Path(self.directory.name) / 'disabled-mask-control'
        result = subprocess.run([sys.executable,
            str(self.root / 'tools/experiments/compile_init_decompressor.py'),
            '--output', str(output), *self.shape_flags['packed-remaining'],
            '--abi-fpr-shadow',
            *distance.InitDecompressorDistanceOperationLocalTests.shadow_extra_flags],
            capture_output=True, text=True, check=True)
        receipts = json.loads(result.stdout)
        expected = {
            'o2g3': (4336, '177d7344426bb233f32c0cfbc92f40e533e2f344889f473bee0540e7bafeb62d',
                     {1: (0x240F0001, 0x240FFFFF), 3: (0x2442FFFF, 0x00401027)}),
            'o1': (5808, '8797fe0eef6f346ea9a90a36e0206b76f648ec3dd5026c7a7f1f6b75d2fb6755',
                   {1: (0x240F0001, 0x240FFFFF), 4: (0x2442FFFF, 0x00401027)}),
        }
        for profile, (size, digest, changes) in expected.items():
            control = object_text(output / (profile + '.o'))
            trial = object_text(Path(self.directory.name) /
                                'packed-remaining-shadow' / (profile + '.o'))
            self.assertEqual((len(control), hashlib.sha256(control).hexdigest()),
                             (size, digest))
            self.assertEqual((len(trial), receipts[profile]['text_bytes']), (size, size))
            differences = {index: (old[0], new[0]) for index, (old, new) in enumerate(
                zip(struct.iter_unpack('>I', control), struct.iter_unpack('>I', trial)))
                if old != new}
            self.assertEqual(differences, changes)
            self.assertEqual((output / (profile + '.log')).read_text(), '')

    def test_complete_packed_ledger_counts_helpers_and_adapter(self):
        for profile, named, helpers, total, builder, public, embedded in (
                ('o2g3', 1029, 55, 1084, 401, 333, [22, 46]),
                ('o1', 1395, 57, 1452, 560, 488, [27, 45])):
            receipt = self.receipts['packed-remaining', profile]
            ledger = receipt['retail_slot_ledger']
            self.assertEqual((ledger['c_named_slot_words'], ledger['c_helper_words'],
                              ledger['c_total_words'], ledger['retail_words']),
                             (named, helpers, total, 996))
            self.assertEqual(named + helpers, total)
            self.assertEqual(total * 4, receipt['text_bytes'])
            row = next(row for row in ledger['rows']
                       if row['c_function'] == 'init_decode_build')
            self.assertEqual((row['retail_slot_words'], row['c_slot_words'],
                              row['c_public_unit_words']), (293, builder, public))
            sizes = [unit['slot_words'] for unit in row['c_embedded_helpers']]
            self.assertEqual(sizes, embedded)
            self.assertEqual(public + sum(sizes), builder)
            image = next(image for label, selected, image in self.adapter_images
                         if label == 'packed-remaining' and selected == profile)
            self.assertEqual(len(image.code) * 4, total * 4 + 176)
            self.assertEqual(len(image.code) * 4 - 3984,
                             528 if profile == 'o2g3' else 2000)

    @classmethod
    def tearDownClass(cls):
        if not any(cls.maximum_depths.values()):
            return
        output = cls.root / 'conker/build/init-complement-low-mask-20261004'
        output.mkdir(parents=True, exist_ok=True)
        report = {'qualification': 'bounded-connected-fixtures-only; no size reduction',
                  'adapter_bytes': 176, 'retail_bytes': 3984,
                  'profiles': {profile: cls.receipts['packed-remaining', profile]
                               for profile in ('o2g3', 'o1')},
                  'maximum_depths': {'%s/%s' % key: value
                                     for key, value in cls.maximum_depths.items()}}
        (output / 'qualification.json').write_text(json.dumps(report, indent=2) + '\n')


class InitDecompressorNativeComplementLowMaskTests(semantic.InitDecompressorSemanticTests):
    compiler_flags = ('-DINIT_DECODE_COMPLEMENT_LOW_MASK',)


if __name__ == '__main__':
    unittest.main()
