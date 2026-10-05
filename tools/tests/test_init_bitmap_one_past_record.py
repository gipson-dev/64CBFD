"""Qualify unsigned one-past sentinel fitting, not assembly owner adoption."""

import hashlib
import json
import shutil
import struct
import subprocess
import unittest

from tools.experiments.compile_init_bitmap_ordered import compile_shapes
from tools.tests import test_init_bitmap_assembly as bitmap
from tools.tests import test_init_bitmap_unsigned_induction as unsigned


class InitBitmapOnePastRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bitmap.InitBitmapAssemblyTests.setUpClass()
        cls.project = bitmap.InitBitmapAssemblyTests.project
        cls.source = cls.project.parent / 'tools/experiments/init_bitmap_ordered.c'
        cls.source_hash = hashlib.sha256(cls.source.read_bytes()).hexdigest()
        if not (cls.project.parent / 'ido/ido5.3_recomp/cc').is_file():
            raise unittest.SkipTest('IDO is unavailable')
        for tool in ('cc', 'mips-linux-gnu-ld', 'mips-linux-gnu-objcopy',
                     'mips-linux-gnu-objdump'):
            if shutil.which(tool) is None:
                raise unittest.SkipTest(tool + ' is unavailable')
        cls.measurements = compile_shapes((12, 23, 25, 26))
        cls.retail = dict(bitmap.InitBitmapAssemblyTests.entries)
        reference = b''.join(struct.pack('>I', cls.retail[pc]) for pc in sorted(cls.retail))
        if reference != (cls.project / 'conker.us.bin').read_bytes()[0x5BE0:0x5C2C]:
            raise AssertionError('bitmap assembly differs from pristine ROM')
        cls.images, cls.frames, cls.hashes = {}, {}, {}
        for row in cls.measurements:
            if row['shape'] not in (25, 26):
                continue
            name = 'shape%d-%s' % (row['shape'], row['profile'])
            data = (cls.project / ('build/init-bitmap-ordered/' + name + '.o.bin')).read_bytes()
            cls.images[name] = {unsigned.BitmapGuestFixture.ENTRY + index * 4: word[0]
                               for index, word in enumerate(struct.iter_unpack('>I', data))}
            cls.frames[name] = row['frame_bytes']
            cls.hashes[name] = hashlib.sha256(data).hexdigest()
        cls.pairs, cls.prefixes = 0, 0

    @classmethod
    def tearDownClass(cls):
        unchanged = hashlib.sha256(cls.source.read_bytes()).hexdigest() == cls.source_hash
        receipt = {'completed_pairs': cls.pairs, 'bounded_prefix_pairs': cls.prefixes,
                   'paired_corpus_complete': cls.pairs == 1098 and cls.prefixes == 18,
                   'source_unchanged': unchanged, 'source_sha256': cls.source_hash,
                   'image_sha256': cls.hashes, 'measurements': cls.measurements,
                   'qualification': 'bounded-instruction-model-only; no record provenance or adoption'}
        (cls.project / 'build/init-bitmap-ordered/one-past-record-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')
        if not unchanged:
            raise AssertionError('bitmap source changed during qualification')

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

    def test_zero_one_past_sentinel_completes_the_inclusive_range(self):
        for count in range(8):
            for start, extent in ((0xFFFFFFFC, 4), (0xFFFFFFFF, 1)):
                fixture = self.compare(start, 0xFFFFFFFF, count, extent)
                stores = [op for op in fixture.operations if op[0] == 'write']
                self.assertEqual([op[1] for op in stores[:extent]],
                                 list(range(start, 0x100000000)))
                self.assertEqual(fixture.memory[0xFFFFFFFF], (1 << count) - 1 if count else 255)

    def test_zero_start_zero_sentinel_preserves_nonempty_full_cycle_prefix(self):
        initial, allowed = self.configured(0, 0xFFFFFFFF, 0, 17)
        expected = unsigned.BitmapGuestFixture(self.retail, initial, allowed, prefix_limit=16)
        with self.assertRaises(unsigned.PrefixComplete):
            expected.run(budget=2000)
        for name, code in self.images.items():
            with self.subTest(image=name):
                actual = unsigned.BitmapGuestFixture(code, initial, allowed, prefix_limit=16)
                with self.assertRaises(unsigned.PrefixComplete):
                    actual.run(budget=2000)
                self.assertEqual(actual.operations, expected.operations)
                self.assertEqual(actual.byte_writes, 16)
                self.assertFalse(any(op[0] == 'read' and
                                     op[1] == bitmap.InitBitmapAssemblyTests.COUNT
                                     for op in actual.operations))
                type(self).prefixes += 1

    def test_zero_sentinel_early_exit_control_is_rejected(self):
        first = unsigned.BitmapGuestFixture.ENTRY
        original = self.images['shape26-o2g3-no-unroll']
        words = [original[pc] for pc in sorted(original)]
        insert, tail = 7, 10
        rewritten = []
        # Insert a false "zero sentinel means empty" guard and relocate local branches.
        for index, word in enumerate(words):
            if index == insert:
                rewritten.extend((0x10800000 | (tail + 2 - insert - 1), 0))
            if word >> 26 in (4, 5):
                offset = word & 0xFFFF
                offset = offset if offset < 0x8000 else offset - 0x10000
                target = index + 1 + offset
                target += 2 if target >= insert else 0
                origin = index + (2 if index >= insert else 0)
                word = (word & 0xFFFF0000) | ((target - origin - 1) & 0xFFFF)
            rewritten.append(word)
        mutant = {first + index * 4: word for index, word in enumerate(rewritten)}
        initial, allowed = self.configured(0xFFFFFFFC, 0xFFFFFFFF, 0, 4)
        expected = unsigned.BitmapGuestFixture(original, initial, allowed)
        actual = unsigned.BitmapGuestFixture(mutant, initial, allowed)
        expected.run()
        actual.run()
        self.assertEqual(expected.byte_writes, 4)
        self.assertEqual(actual.byte_writes, 0)
        self.assertNotEqual(actual.operations, expected.operations)
        self.assertNotEqual(actual.memory, expected.memory)

    def test_reversed_endpoint_read_control_is_rejected_despite_same_memory(self):
        first = unsigned.BitmapGuestFixture.ENTRY
        words = [self.retail[pc] for pc in sorted(self.retail)]
        reordered = [words[0], words[3], words[4], words[1], words[2], *words[5:]]
        mutant = {first + index * 4: word for index, word in enumerate(reordered)}
        initial, allowed = self.configured(0x80050000, 0x80050002, 19, 3)
        expected = unsigned.BitmapGuestFixture(self.retail, initial, allowed)
        actual = unsigned.BitmapGuestFixture(mutant, initial, allowed)
        expected.run()
        actual.run()
        self.assertEqual(actual.memory, expected.memory)
        self.assertNotEqual(actual.operations, expected.operations)
        self.assertEqual(actual.operations[:2], expected.operations[:2][::-1])
        self.assertEqual(actual.operations[2:], expected.operations[2:])

    def test_complete_measurements_remain_unmatched(self):
        expected = {(25, 'o2g3'): (36, 36, 144, 0),
                    (25, 'o2g3-no-unroll'): (23, 23, 96, 0),
                    (25, 'o1'): (36, 36, 144, 16),
                    (26, 'o2g3'): (32, 32, 128, 0),
                    (26, 'o2g3-no-unroll'): (19, 16, 80, 0),
                    (26, 'o1'): (33, 32, 144, 16)}
        self.assertEqual({(row['shape'], row['profile']):
                          (row['body_words'], row['different_positions'],
                           row['text_bytes'], row['frame_bytes'])
                          for row in self.measurements if row['shape'] in (25, 26)}, expected)
        for row in self.measurements:
            self.assertFalse(row['exact'])
            self.assertEqual(row['host_cases'], 79)
            self.assertFalse(row['host_return_checked'])
            self.assertEqual(row['text_bytes'], row['body_words'] * 4 + row['trailing_text_bytes'])
            name = 'shape%d-%s' % (row['shape'], row['profile'])
            self.assertEqual((self.project / ('build/init-bitmap-ordered/' + name + '.o.log'))
                             .read_text(), '')
            if row['shape'] in (23, 26):
                self.assertEqual(tuple(row['record_layout']), (16, 0, 8, 12, 2))
        self.assertIn('build/asm/init_5AB0.s.o(.text);', (self.project / 'conker.ld').read_text())

    def test_direct_back_edge_still_has_store_not_increment_in_delay(self):
        first = unsigned.BitmapGuestFixture.ENTRY
        code = self.images['shape26-o2g3-no-unroll']
        self.assertEqual([code[first + offset] for offset in range(24, 40, 4)],
                         [0x24640001, 0x24420001, 0x1444FFFE, 0xA046FFFF])
        self.assertFalse(any(word >> 26 == 0 and word & 63 == 38 for word in code.values()))
        self.assertEqual([self.retail[first + offset] for offset in range(20, 32, 4)],
                         [0xA0480000, 0x1443FFFE, 0x24420001])

    def test_grouped_view_reads_only_captured_fields_and_late_count(self):
        initial, allowed = self.configured(0x80050000, 0x80050002, 19, 3)
        expected_reads = [(0x8003BE70, 4), (0x8003BE7C, 4), (0x8003BE78, 2)]
        for name, code in self.images.items():
            with self.subTest(image=name):
                fixture = unsigned.BitmapGuestFixture(code, initial, allowed)
                fixture.run()
                self.assertEqual([(address, size) for kind, address, size, _ in fixture.operations
                                  if kind == 'read'], expected_reads)

    def test_all_old_host_guest_selections_keep_banked_preprocessing(self):
        digest = hashlib.sha256()
        for shape in range(1, 25):
            for host in (False, True):
                command = ['cc', '-E', '-P', '-x', 'c', '-DSHAPE=%d' % shape]
                if host:
                    command.append('-DHOST_TEST')
                text = subprocess.check_output(command + ['-'], input=self.source.read_bytes())
                digest.update(('%d/%d\n' % (shape, host)).encode())
                digest.update(text)
        self.assertEqual(digest.hexdigest(),
                         '65e378d5b7bb42e3ae991234d33e8714bab6787ab2364747e8516d84f1f21d19')


if __name__ == '__main__':
    unittest.main()
