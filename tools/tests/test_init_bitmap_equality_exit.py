import json
import shutil
import struct
import unittest

from tools.experiments.compile_init_bitmap_ordered import compile_shapes
from tools.tests import test_init_bitmap_assembly as bitmap
from tools.tests import test_init_bitmap_unsigned_induction as unsigned


class InitBitmapEqualityExitTests(unittest.TestCase):
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
        cls.measurements = compile_shapes((16, 17))
        cls.retail = dict(bitmap.InitBitmapAssemblyTests.entries)
        retail = b''.join(struct.pack('>I', cls.retail[pc]) for pc in sorted(cls.retail))
        if retail != (cls.project / 'conker.us.bin').read_bytes()[0x5BE0:0x5C2C]:
            raise AssertionError('bitmap assembly differs from pristine ROM')
        cls.images, cls.frames = {}, {}
        for row in cls.measurements:
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
                   'qualification': 'model-address-domain-only; equality-exit trials'}
        (cls.project / 'build/init-bitmap-ordered/equality-exit-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')
        print('equality-exit bitmap receipt:', receipt)

    # Run the established alias/wrap/stack oracle on freshly compiled images.
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

    def test_complete_slots_and_original_owner_remain_rejected(self):
        expected = {(shape, profile): (21, differences, 0)
                    for shape, differences in ((16, 20), (17, 19))
                    for profile in ('o2g3', 'o2g3-no-unroll')}
        expected.update({(shape, 'o1'): (31, 31, 16) for shape in (16, 17)})
        self.assertEqual({(row['shape'], row['profile']):
                          (row['body_words'], row['different_positions'], row['frame_bytes'])
                          for row in self.measurements}, expected)
        self.assertTrue(all(not row['exact'] and row['host_cases'] == 79
                            and not row['host_return_checked'] for row in self.measurements))
        self.assertIn('build/asm/init_5AB0.s.o(.text);',
                      (self.project / 'conker.ld').read_text())

    def test_equality_exit_removes_xor_but_adds_backedge_and_second_return(self):
        first = unsigned.BitmapGuestFixture.ENTRY
        for shape, store in ((16, 0xA0480000), (17, 0xA0680000)):
            for profile in ('o2g3', 'o2g3-no-unroll'):
                with self.subTest(shape=shape, profile=profile):
                    code = self.images['shape%d-%s' % (shape, profile)]
                    words = [code[first + offset] for offset in range(0, 84, 4)]
                    self.assertFalse(any(word >> 26 == 0 and word & 63 == 38
                                         for word in words))
                    self.assertEqual(words[5:7], [0x1443000B, 0xA0440000])
                    self.assertEqual(words[15:], [0x03E00008, store, 0x1000FFF3,
                                                 0x24420001, 0x03E00008, 0])


if __name__ == '__main__':
    unittest.main()
