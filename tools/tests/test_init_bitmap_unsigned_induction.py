import json
import shutil
import struct
import unittest
from pathlib import Path
from types import SimpleNamespace

from tools.experiments.compile_init_bitmap_ordered import compile_shapes
from tools.tests import test_init_bitmap_assembly as bitmap
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture
from tools.tests.test_init_decompressor_tables import BuilderFixture


class PrefixComplete(Exception):
    pass


class BitmapGuestFixture(GuestBuilderFixture):
    ENTRY = 0x10005BE0
    STACK = 0x80100000

    def __init__(self, code, memory, allowed_bytes, prefix_limit=None):
        self.image = SimpleNamespace(entry=self.ENTRY)
        self.code = code
        self.memory = dict(memory)
        self.memory.update((self.STACK + offset, 0xA5) for offset in range(-64, 16))
        self.registers = [0xA5A50000 + index for index in range(32)]
        self.registers[0] = 0
        self.registers[29] = self.STACK
        self.registers[31] = 0xDEAD0000
        self.before = self.registers[:]
        self.fprs = [0] * 32
        self.min_sp = self.STACK
        self.reads, self.writes, self.operations = [], [], []
        self.capture, self.snapshots, self.visits = set(), {}, {}
        self.allowed_bytes = set(allowed_bytes)
        self.prefix_limit = prefix_limit
        self.byte_writes = 0

    def private(self, address, size):
        return self.STACK - 64 <= address and address + size <= self.STACK + 16

    def put(self, address, value, size):
        if not self.private(address, size):
            if size != 1 or address not in self.allowed_bytes:
                raise AssertionError('bitmap store exceeds fixture output fence')
            if self.prefix_limit is not None and self.byte_writes == self.prefix_limit:
                raise PrefixComplete()
            self.byte_writes += 1
        # Reuse the byte writer, not the decoder's frame/workspace fences.
        BuilderFixture.put(self, address, value, size)

    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        offset = word & 0xFFFF
        offset = offset if offset < 0x8000 else offset - 0x10000
        address = (self.registers[rs] + offset) & 0xFFFFFFFF
        sizes = {33: 2, 35: 4, 40: 1, 43: 4}
        operation = None
        if op in sizes and not self.private(address, sizes[op]):
            size = sizes[op]
            write = op in (40, 43)
            value = (self.registers[rt] & ((1 << (8 * size)) - 1)
                     if write else self.get(address, size))
            operation = ('write' if write else 'read', address, size, value)
        if op == 33:
            value = self.get(address, 2)
            self.registers[rt] = (value if value < 0x8000 else value - 0x10000) & 0xFFFFFFFF
            self.reads.append((address, 2))
            self.registers[0] = 0
        else:
            super().execute(word)
        if operation is not None:
            self.operations.append(operation)


class InitBitmapUnsignedInductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bitmap.InitBitmapAssemblyTests.setUpClass()
        cls.project = bitmap.InitBitmapAssemblyTests.project
        compiler = cls.project.parent / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file():
            raise unittest.SkipTest('IDO is unavailable')
        for tool in ('cc', 'mips-linux-gnu-ld', 'mips-linux-gnu-objcopy',
                     'mips-linux-gnu-objdump'):
            if shutil.which(tool) is None:
                raise unittest.SkipTest(tool + ' is unavailable')
        cls.measurements = compile_shapes((1, 12, 13))
        cls.retail = dict(bitmap.InitBitmapAssemblyTests.entries)
        rom = (cls.project / 'conker.us.bin').read_bytes()
        if b''.join(struct.pack('>I', cls.retail[pc]) for pc in sorted(cls.retail)) != rom[0x5BE0:0x5C2C]:
            raise AssertionError('bitmap assembly differs from pristine ROM')
        cls.images, cls.frames = {}, {}
        for row in cls.measurements:
            if row['shape'] == 1:
                continue
            name = 'shape%d-%s' % (row['shape'], row['profile'])
            data = (cls.project / ('build/init-bitmap-ordered/' + name + '.o.bin')).read_bytes()
            cls.images[name] = {BitmapGuestFixture.ENTRY + index * 4: word[0]
                               for index, word in enumerate(struct.iter_unpack('>I', data))}
            cls.frames[name] = row['frame_bytes']
        cls.pairs, cls.prefixes = 0, 0

    @classmethod
    def tearDownClass(cls):
        receipt = {'completed_pairs': cls.pairs, 'bounded_prefix_pairs': cls.prefixes,
                   'paired_corpus_complete': cls.pairs == 1002 and cls.prefixes == 12,
                   'qualification': 'model-address-domain-only; not hardware acceptance'}
        (cls.project / 'build/init-bitmap-ordered/unsigned-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')
        print('unsigned bitmap receipt:', receipt)

    def configured(self, start, end, count, extent):
        memory = {}
        for address, value, size in ((bitmap.InitBitmapAssemblyTests.START, start, 4),
                                     (bitmap.InitBitmapAssemblyTests.END, end, 4),
                                     (bitmap.InitBitmapAssemblyTests.COUNT, count & 0xFFFF, 2)):
            bitmap.InitBitmapAssemblyTests.put(memory, address, value, size)
        allowed = {(start + offset) & 0xFFFFFFFF for offset in range(extent)}
        for offset in range(-1, extent + 1):
            memory.setdefault((start + offset) & 0xFFFFFFFF, 0xA5)
        return memory, allowed

    def compare(self, start, end, count, extent, repeats=1):
        initial, allowed = self.configured(start, end, count, extent)
        expected = BitmapGuestFixture(self.retail, initial, allowed)
        controls = {name: BitmapGuestFixture(code, initial, allowed)
                    for name, code in self.images.items()}
        for _ in range(repeats):
            expected.operations.clear()
            expected.run(budget=100000)
            for name, actual in controls.items():
                with self.subTest(image=name, start=start, end=end, count=count):
                    actual.operations.clear()
                    actual.run(budget=100000)
                    self.assertEqual(actual.operations, expected.operations)
                    external = lambda fixture: {address: value for address, value in fixture.memory.items()
                                                if not fixture.private(address, 1)}
                    self.assertEqual(external(actual), external(expected))
                    for register in (*range(16, 24), 28, 29, 30, 31):
                        self.assertEqual(actual.registers[register], actual.before[register])
                    self.assertEqual(actual.min_sp, actual.STACK - self.frames[name])
                    type(self).pairs += 1
        return expected

    def test_bounded_counts_remainders_sentinels_and_repeat(self):
        counts = [*range(1, 65), 0, -32768, -8, -7, -1,
                  107, 235, 243, 251, 259, 267, 362, 32767]
        for count in counts:
            size = (count + 7) >> 3 if count > 0 else 1
            self.compare(0x80050000, 0x80050000 + size - 1, count, size, repeats=2)

    def test_start_end_and_count_storage_aliases(self):
        for address, size in ((bitmap.InitBitmapAssemblyTests.START, 4),
                              (bitmap.InitBitmapAssemblyTests.END, 4),
                              (bitmap.InitBitmapAssemblyTests.COUNT, 2),
                              (bitmap.InitBitmapAssemblyTests.COUNT, 1),
                              (bitmap.InitBitmapAssemblyTests.COUNT + 1, 1)):
            self.compare(address, address + size - 1, 3, size)

    def test_unsigned_wraparound_in_model_not_real_hardware(self):
        for count in range(8):
            fixture = self.compare(0xFFFFFFFC, 3, count, 8)
            writes = [operation[1] for operation in fixture.operations if operation[0] == 'write']
            self.assertEqual(writes[:8], [0xFFFFFFFC, 0xFFFFFFFD, 0xFFFFFFFE, 0xFFFFFFFF,
                                          0, 1, 2, 3])

    def test_reversed_endpoints_preserve_bounded_fill_prefix(self):
        for start in (0x80050000, 0xFFFFFFF8):
            initial, allowed = self.configured(start, (start - 1) & 0xFFFFFFFF, 0, 17)
            expected = BitmapGuestFixture(self.retail, initial, allowed, prefix_limit=16)
            with self.assertRaises(PrefixComplete):
                expected.run(budget=2000)
            for name, code in self.images.items():
                with self.subTest(image=name, start=start):
                    actual = BitmapGuestFixture(code, initial, allowed, prefix_limit=16)
                    with self.assertRaises(PrefixComplete):
                        actual.run(budget=2000)
                    self.assertEqual(actual.operations, expected.operations)
                    self.assertFalse(any(operation[0] == 'read' and
                                         operation[1] == bitmap.InitBitmapAssemblyTests.COUNT
                                         for operation in actual.operations))
                    self.assertEqual(actual.byte_writes, 16)
                    type(self).prefixes += 1

    def test_output_fence_rejects_writes_outside_owned_bytes(self):
        initial, allowed = self.configured(0x80050000, 0x80050000, 0, 1)
        fixture = BitmapGuestFixture(self.retail, initial, allowed)
        for address, size in ((0x8004FFFF, 1), (0x80050001, 1),
                              (bitmap.InitBitmapAssemblyTests.START, 4)):
            with self.assertRaises(AssertionError):
                fixture.put(address, 0, size)

    def test_complete_slots_remain_rejected_without_production_edits(self):
        expected = {(12, 'o2g3'): 20, (12, 'o2g3-no-unroll'): 20, (12, 'o1'): 31,
                    (13, 'o2g3'): 22, (13, 'o2g3-no-unroll'): 22, (13, 'o1'): 34}
        self.assertEqual({(row['shape'], row['profile']): row['body_words']
                          for row in self.measurements if row['shape'] != 1}, expected)
        self.assertTrue(all(not row['exact'] for row in self.measurements))
        self.assertTrue(all(row['host_cases'] == 79 for row in self.measurements))
        self.assertIn('build/asm/init_5AB0.s.o(.text);',
                      (self.project / 'conker.ld').read_text())

    def test_unsigned_equality_is_control_byte_identical(self):
        output = self.project / 'build/init-bitmap-ordered'
        for profile in ('o2g3', 'o2g3-no-unroll', 'o1'):
            self.assertEqual((output / ('shape1-' + profile + '.o.bin')).read_bytes(),
                             (output / ('shape12-' + profile + '.o.bin')).read_bytes())

    def test_alias_oracle_rejects_hoisted_count_load(self):
        words = [self.retail[pc] for pc in sorted(self.retail)]
        # Keep the local back edge intact, but move the count read before filling.
        hoisted = words[:5] + words[8:10] + words[5:8] + words[10:]
        code = {BitmapGuestFixture.ENTRY + index * 4: word for index, word in enumerate(hoisted)}
        count = bitmap.InitBitmapAssemblyTests.COUNT
        initial, allowed = self.configured(count, count + 1, 3, 2)
        expected = BitmapGuestFixture(self.retail, initial, allowed)
        mutant = BitmapGuestFixture(code, initial, allowed)
        expected.run()
        mutant.run()
        self.assertNotEqual(mutant.operations, expected.operations)
        self.assertEqual(expected.memory[count + 1], 0x7F)
        self.assertEqual(mutant.memory[count + 1], 7)


if __name__ == '__main__':
    unittest.main()
