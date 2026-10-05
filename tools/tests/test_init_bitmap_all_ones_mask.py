"""Qualify all-ones mask fitting without claiming a retail C replacement."""

import json
import shutil
import struct
import unittest

from tools.experiments.compile_init_bitmap_ordered import compile_shapes
from tools.tests import test_init_bitmap_assembly as bitmap
from tools.tests import test_init_bitmap_unsigned_induction as unsigned


class InitBitmapAllOnesMaskTests(unittest.TestCase):
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
        cls.measurements = compile_shapes((19, 21, 22))
        cls.retail = dict(bitmap.InitBitmapAssemblyTests.entries)
        reference = b''.join(struct.pack('>I', cls.retail[pc]) for pc in sorted(cls.retail))
        if reference != (cls.project / 'conker.us.bin').read_bytes()[0x5BE0:0x5C2C]:
            raise AssertionError('bitmap assembly differs from pristine ROM')
        cls.images, cls.frames = {}, {}
        for row in cls.measurements:
            if row['shape'] == 19:
                continue
            name = 'shape%d-%s' % (row['shape'], row['profile'])
            data = (cls.project / ('build/init-bitmap-ordered/' + name + '.o.bin')).read_bytes()
            cls.images[name] = {unsigned.BitmapGuestFixture.ENTRY + index * 4: word[0]
                               for index, word in enumerate(struct.iter_unpack('>I', data))}
            cls.frames[name] = row['frame_bytes']
        cls.pairs, cls.prefixes = 0, 0

    @classmethod
    def tearDownClass(cls):
        receipt = {'completed_pairs': cls.pairs, 'bounded_prefix_pairs': cls.prefixes,
                   'paired_corpus_complete': cls.pairs == 1002 and cls.prefixes == 12,
                   'measurements': cls.measurements,
                   'qualification': 'model-address-domain-only; all-ones mask fitting'}
        (cls.project / 'build/init-bitmap-ordered/all-ones-mask-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')
        print('all-ones bitmap receipt:', receipt)

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

    def test_complete_slot_fits_but_does_not_match_retail(self):
        expected = {(21, 'o2g3'): (19, 17, 0),
                    (21, 'o2g3-no-unroll'): (19, 17, 0),
                    (21, 'o1'): (32, 32, 24),
                    (22, 'o2g3'): (20, 19, 0),
                    (22, 'o2g3-no-unroll'): (20, 19, 0),
                    (22, 'o1'): (33, 33, 24)}
        self.assertEqual({(row['shape'], row['profile']):
                          (row['body_words'], row['different_positions'], row['frame_bytes'])
                          for row in self.measurements if row['shape'] != 19}, expected)
        self.assertTrue(all(not row['exact'] and row['host_cases'] == 79
                            and not row['host_return_checked'] for row in self.measurements))
        for row in self.measurements:
            if row['shape'] == 19:
                continue
            name = 'shape%d-%s' % (row['shape'], row['profile'])
            self.assertEqual(len(self.images[name]) * 4, row['text_bytes'])
            self.assertEqual(row['text_bytes'],
                             row['body_words'] * 4 + row['trailing_text_bytes'])
            if row['profile'] != 'o1':
                self.assertEqual((row['text_bytes'], row['trailing_text_bytes']),
                                 (80, 4 if row['shape'] == 21 else 0))
            else:
                self.assertEqual((row['text_bytes'], row['trailing_text_bytes']),
                                 (128, 0) if row['shape'] == 21 else (144, 12))
        self.assertIn('build/asm/init_5AB0.s.o(.text);',
                      (self.project / 'conker.ld').read_text())

    def test_all_ones_is_rematerialized_and_xor_loop_remains(self):
        first = unsigned.BitmapGuestFixture.ENTRY
        for profile in ('o2g3', 'o2g3-no-unroll'):
            code = self.images['shape21-' + profile]
            self.assertEqual([code[first + offset] for offset in range(16, 36, 4)],
                             [0x2405FFFF, 0x00641026, 0x24630001,
                              0x1440FFFD, 0xA065FFFF])
            self.assertEqual([code[first + offset] for offset in range(44, 68, 4)],
                             [0x240FFFFF, 0x306E0007, 0x11C00003,
                              0x01CF1004, 0x00401027, 0xA0820000])
            self.assertEqual([self.retail[first + offset] for offset in range(20, 32, 4)],
                             [0xA0480000, 0x1443FFFE, 0x24420001])

    def test_prior_right_shift_control_keeps_banked_extent(self):
        self.assertEqual({row['profile']: (row['body_words'], row['different_positions'],
                                         row['frame_bytes']) for row in self.measurements
                          if row['shape'] == 19},
                         {'o2g3': (20, 20, 0), 'o2g3-no-unroll': (20, 20, 0),
                          'o1': (33, 33, 24)})


if __name__ == '__main__':
    unittest.main()
