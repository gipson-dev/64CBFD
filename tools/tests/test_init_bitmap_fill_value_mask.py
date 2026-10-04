"""Qualify the isolated right-shift fill-value trial, not production adoption."""

import json
import shutil
import struct
import unittest

from tools.experiments.compile_init_bitmap_ordered import compile_shapes
from tools.tests import test_init_bitmap_assembly as bitmap
from tools.tests import test_init_bitmap_unsigned_induction as unsigned


class InitBitmapFillValueMaskTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bitmap.InitBitmapAssemblyTests.setUpClass()
        cls.project = bitmap.InitBitmapAssemblyTests.project
        if not (cls.project.parent / 'ido/ido5.3_recomp/cc').is_file():
            raise unittest.SkipTest('IDO is unavailable')
        for tool in ('cc', 'mips-linux-gnu-ld', 'mips-linux-gnu-objcopy',
                     'mips-linux-gnu-objdump'):
            if shutil.which(tool) is None:
                raise unittest.SkipTest(tool + ' is unavailable')
        cls.measurements = compile_shapes((19,))
        cls.retail = dict(bitmap.InitBitmapAssemblyTests.entries)
        reference = b''.join(struct.pack('>I', cls.retail[pc]) for pc in sorted(cls.retail))
        if reference != (cls.project / 'conker.us.bin').read_bytes()[0x5BE0:0x5C2C]:
            raise AssertionError('bitmap assembly differs from pristine ROM')
        cls.images, cls.frames = {}, {}
        for row in cls.measurements:
            name = 'shape19-' + row['profile']
            data = (cls.project / ('build/init-bitmap-ordered/' + name + '.o.bin')).read_bytes()
            cls.images[name] = {unsigned.BitmapGuestFixture.ENTRY + index * 4: word[0]
                               for index, word in enumerate(struct.iter_unpack('>I', data))}
            cls.frames[name] = row['frame_bytes']
        cls.pairs, cls.prefixes = 0, 0

    @classmethod
    def tearDownClass(cls):
        receipt = {'completed_pairs': cls.pairs, 'bounded_prefix_pairs': cls.prefixes,
                   'paired_corpus_complete': cls.pairs == 501 and cls.prefixes == 6,
                   'measurements': cls.measurements,
                   'qualification': 'model-address-domain-only; right-shift mask trial'}
        (cls.project / 'build/init-bitmap-ordered/fill-value-mask-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')
        print('fill-value mask bitmap receipt:', receipt)

    configured = unsigned.InitBitmapUnsignedInductionTests.configured
    compare = unsigned.InitBitmapUnsignedInductionTests.compare
    test_bounded_counts_remainders_sentinels_and_repeat = (
        unsigned.InitBitmapUnsignedInductionTests.test_bounded_counts_remainders_sentinels_and_repeat)
    test_start_end_and_count_storage_aliases = (
        unsigned.InitBitmapUnsignedInductionTests.test_start_end_and_count_storage_aliases)
    test_unsigned_wraparound_in_model_not_real_hardware = (
        unsigned.InitBitmapUnsignedInductionTests.test_unsigned_wraparound_in_model_not_real_hardware)
    test_reversed_endpoints_preserve_bounded_fill_prefix = (
        unsigned.InitBitmapUnsignedInductionTests.test_reversed_endpoints_preserve_bounded_fill_prefix)
    test_output_fence_rejects_writes_outside_owned_bytes = (
        unsigned.InitBitmapUnsignedInductionTests.test_output_fence_rejects_writes_outside_owned_bytes)
    test_alias_oracle_rejects_hoisted_count_load = (
        unsigned.InitBitmapUnsignedInductionTests.test_alias_oracle_rejects_hoisted_count_load)

    def test_complete_slots_remain_rejected_without_production_edits(self):
        self.assertEqual({row['profile']: (row['body_words'], row['different_positions'],
                                         row['frame_bytes']) for row in self.measurements},
                         {'o2g3': (20, 20, 0), 'o2g3-no-unroll': (20, 20, 0),
                          'o1': (33, 33, 24)})
        self.assertTrue(all(not row['exact'] and row['host_cases'] == 79
                            and not row['host_return_checked'] for row in self.measurements))
        self.assertIn('build/asm/init_5AB0.s.o(.text);',
                      (self.project / 'conker.ld').read_text())

    def test_fill_constant_is_rematerialized_and_xor_survives(self):
        first = unsigned.BitmapGuestFixture.ENTRY
        for profile in ('o2g3', 'o2g3-no-unroll'):
            with self.subTest(profile=profile):
                code = self.images['shape19-' + profile]
                words = [code[first + offset] for offset in range(0, 80, 4)]
                self.assertEqual(words[4:9], [0x240500FF, 0x00641026, 0x24630001,
                                             0x1440FFFD, 0xA065FFFF])
                self.assertEqual(words[11:18], [0x240F0008, 0x241900FF, 0x306E0007,
                                               0x11C00003, 0x01EEC023, 0x03191006,
                                               0xA0820000])
                self.assertEqual(words[-2:], [0x03E00008, 0])


if __name__ == '__main__':
    unittest.main()
