import json
import shutil
import struct
import unittest

from tools.experiments.compile_init_bitmap_ordered import compile_shapes
from tools.tests import test_init_bitmap_assembly as bitmap
from tools.tests import test_init_bitmap_unsigned_induction as unsigned


class InitBitmapExitEdgeTests(unittest.TestCase):
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
        cls.measurements = compile_shapes((1, 14, 15))
        cls.retail = dict(bitmap.InitBitmapAssemblyTests.entries)
        retail = b''.join(struct.pack('>I', cls.retail[pc]) for pc in sorted(cls.retail))
        if retail != (cls.project / 'conker.us.bin').read_bytes()[0x5BE0:0x5C2C]:
            raise AssertionError('bitmap assembly differs from pristine ROM')
        cls.images, cls.frames = {}, {}
        for row in cls.measurements:
            if row['shape'] == 1:
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
                   'qualification': 'model-address-domain-only; void-return trials'}
        (cls.project / 'build/init-bitmap-ordered/exit-edge-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')
        print('exit-edge bitmap receipt:', receipt)

    # Run the established trace, alias, wrap, stack and rejecting controls on
    # these independently compiled images; never credit the old trial images.
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

    def test_full_slot_footprints_reject_both_shapes(self):
        expected = {(1, 'o2g3'): (20, 0), (1, 'o2g3-no-unroll'): (20, 0),
                    (1, 'o1'): (31, 16), (14, 'o2g3'): (34, 0),
                    (14, 'o2g3-no-unroll'): (22, 0), (14, 'o1'): (35, 16),
                    (15, 'o2g3'): (20, 0), (15, 'o2g3-no-unroll'): (20, 0),
                    (15, 'o1'): (32, 16)}
        self.assertEqual({(row['shape'], row['profile']):
                          (row['body_words'], row['frame_bytes'])
                          for row in self.measurements}, expected)
        self.assertTrue(all(not row['exact'] and row['host_cases'] == 79
                            and not row['host_return_checked'] for row in self.measurements))
        self.assertIn('build/asm/init_5AB0.s.o(.text);',
                      (self.project / 'conker.ld').read_text())

    def test_backedge_loop_removes_xor_but_keeps_entry_jump(self):
        for profile in ('o2g3', 'o2g3-no-unroll'):
            code = self.images['shape15-' + profile]
            words = [code[pc] for pc in sorted(code)][:20]
            self.assertFalse(any(word >> 26 == 0 and word & 63 == 38 for word in words))
            self.assertEqual(words[4:9], [0x10000002, 0x240400FF, 0x24420001,
                                         0x1443FFFE, 0xA0440000])
            data = (self.project / ('build/init-bitmap-ordered/shape1-' +
                                   profile + '.o.bin')).read_bytes()
            control = [word[0] for word in struct.iter_unpack('>I', data[:80])]
            self.assertEqual(words[:4], control[:4])
            self.assertEqual(words[9:], control[9:])


if __name__ == '__main__':
    unittest.main()
