"""Qualify preincrement cursor scheduling separately from production adoption."""

import json
import shutil
import struct
import unittest

from tools.experiments.compile_init_bitmap_ordered import compile_shapes
from tools.tests import test_init_bitmap_assembly as bitmap
from tools.tests import test_init_bitmap_unsigned_induction as unsigned


class InitBitmapPreincrementTests(unittest.TestCase):
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
        cls.measurements = compile_shapes((20,))
        cls.retail = dict(bitmap.InitBitmapAssemblyTests.entries)
        reference = b''.join(struct.pack('>I', cls.retail[pc]) for pc in sorted(cls.retail))
        if reference != (cls.project / 'conker.us.bin').read_bytes()[0x5BE0:0x5C2C]:
            raise AssertionError('bitmap assembly differs from pristine ROM')
        cls.images, cls.frames = {}, {}
        for row in cls.measurements:
            name = 'shape20-' + row['profile']
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
                   'qualification': 'model-address-domain-only; preincrement cursor trial'}
        (cls.project / 'build/init-bitmap-ordered/preincrement-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')
        print('preincrement bitmap receipt:', receipt)

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
                         {'o2g3': (32, 32, 0), 'o2g3-no-unroll': (20, 20, 0),
                          'o1': (32, 32, 16)})
        self.assertTrue(all(not row['exact'] and row['host_cases'] == 79
                            and not row['host_return_checked'] for row in self.measurements))
        self.assertIn('build/asm/init_5AB0.s.o(.text);',
                      (self.project / 'conker.ld').read_text())

    def test_direct_endpoint_branch_still_has_wrong_delay_and_extra_bias(self):
        first = unsigned.BitmapGuestFixture.ENTRY
        code = self.images['shape20-o2g3-no-unroll']
        self.assertEqual([code[first + offset] for offset in range(20, 36, 4)],
                         [0x2442FFFF, 0x24420001, 0x1443FFFE, 0xA0440000])
        self.assertEqual([self.retail[first + offset] for offset in range(20, 32, 4)],
                         [0xA0480000, 0x1443FFFE, 0x24420001])


if __name__ == '__main__':
    unittest.main()
