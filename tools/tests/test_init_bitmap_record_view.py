"""Qualify isolated grouped bitmap reads, not original-type or adoption proof."""

import json
import shutil
import struct
import unittest

from tools.experiments.compile_init_bitmap_ordered import compile_shapes
from tools.tests import test_init_bitmap_assembly as bitmap
from tools.tests import test_init_bitmap_unsigned_induction as unsigned


class InitBitmapRecordViewTests(unittest.TestCase):
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
        cls.measurements = compile_shapes((12, 23, 24))
        cls.retail = dict(bitmap.InitBitmapAssemblyTests.entries)
        reference = b''.join(struct.pack('>I', cls.retail[pc]) for pc in sorted(cls.retail))
        if reference != (cls.project / 'conker.us.bin').read_bytes()[0x5BE0:0x5C2C]:
            raise AssertionError('bitmap assembly differs from pristine ROM')
        cls.images, cls.frames = {}, {}
        for row in cls.measurements:
            if row['shape'] == 12:
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
                   'qualification': 'bounded-model-only; no original record-type or adoption proof'}
        (cls.project / 'build/init-bitmap-ordered/record-view-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')

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

    def test_complete_sizes_still_do_not_match_retail(self):
        expected = {(23, 'o2g3'): (19, 17, 80, 0),
                    (23, 'o2g3-no-unroll'): (19, 17, 80, 0),
                    (23, 'o1'): (31, 31, 128, 16),
                    (24, 'o2g3'): (19, 17, 80, 0),
                    (24, 'o2g3-no-unroll'): (19, 17, 80, 0),
                    (24, 'o1'): (32, 32, 128, 24)}
        self.assertEqual({(row['shape'], row['profile']):
                          (row['body_words'], row['different_positions'],
                           row['text_bytes'], row['frame_bytes'])
                          for row in self.measurements if row['shape'] != 12}, expected)
        for row in self.measurements:
            self.assertFalse(row['exact'])
            self.assertEqual(row['host_cases'], 79)
            self.assertFalse(row['host_return_checked'])
            self.assertEqual(row['text_bytes'], row['body_words'] * 4 + row['trailing_text_bytes'])
            if row['shape'] != 12:
                self.assertEqual(tuple(row['record_layout']), (16, 0, 8, 12, 2))
                name = 'shape%d-%s' % (row['shape'], row['profile'])
                self.assertEqual(len(self.images[name]) * 4, row['text_bytes'])
        self.assertIn('build/asm/init_5AB0.s.o(.text);',
                      (self.project / 'conker.ld').read_text())

    def test_record_layout_reads_and_optimized_views(self):
        first = unsigned.BitmapGuestFixture.ENTRY
        for profile in ('o2g3', 'o2g3-no-unroll'):
            code = self.images['shape23-' + profile]
            self.assertEqual(code, self.images['shape24-' + profile])
            self.assertEqual([code[first + offset] for offset in range(0, 16, 4)],
                             [0x3C058004, 0x24A5BE70, 0x8CA20000, 0x8CA3000C])
            self.assertEqual(code[first + 36], 0x84A20008)
            self.assertEqual([code[first + offset] for offset in range(20, 36, 4)],
                             [0x00432026, 0x24420001, 0x1480FFFD, 0xA046FFFF])
            self.assertEqual(code[first + 56], 0x004FC004)
        initial, allowed = self.configured(0x80050000, 0x80050002, 19, 3)
        expected_reads = [(0x8003BE70, 4), (0x8003BE7C, 4), (0x8003BE78, 2)]
        for name, code in self.images.items():
            with self.subTest(image=name):
                fixture = unsigned.BitmapGuestFixture(code, initial, allowed)
                fixture.run()
                self.assertEqual([(address, size) for kind, address, size, _ in fixture.operations
                                  if kind == 'read'], expected_reads)

    def test_read_oracle_detects_reserved_field_access(self):
        first = unsigned.BitmapGuestFixture.ENTRY
        original = self.images['shape23-o2g3']
        mutant = dict(original)
        mutant[first + 72] = 0x8CA80004  # lw t0,4(a1) in the return delay slot.
        initial, allowed = self.configured(0x80050000, 0x80050000, 3, 1)
        initial.update({address: 0x5A for address in range(0x8003BE74, 0x8003BE78)})
        expected = unsigned.BitmapGuestFixture(original, initial, allowed)
        actual = unsigned.BitmapGuestFixture(mutant, initial, allowed)
        expected.run()
        actual.run()
        self.assertEqual(actual.memory, expected.memory)
        self.assertEqual(actual.operations, expected.operations +
                         [('read', 0x8003BE74, 4, 0x5A5A5A5A)])

    def test_unsigned_scalar_control_keeps_banked_extent(self):
        self.assertEqual({row['profile']: (row['body_words'], row['different_positions'],
                                         row['text_bytes'], row['frame_bytes'])
                          for row in self.measurements if row['shape'] == 12},
                         {'o2g3': (20, 19, 80, 0), 'o2g3-no-unroll': (20, 19, 80, 0),
                          'o1': (31, 31, 128, 16)})


if __name__ == '__main__':
    unittest.main()
