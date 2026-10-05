"""Qualify emitted MMIO record views in a model, never on host hardware."""

import json
import shutil
import struct
import unittest
from tools.experiments.compile_init_mmio_record import compile_trials
from tools.tests import test_init_mmio_assembly as retail
from tools.tests.test_init_decompressor_tables import BuilderFixture


class MmioFixture(BuilderFixture):
    ENTRY = 0x100038E0
    STACK = 0x80100000
    STORES = {(0x80038070, 4), (0x80038074, 2), (0xBC000C02, 2)}

    def __init__(self, code, seed):
        self.code = code
        self.memory = {self.STACK + offset: 0xA5 for offset in range(-64, 16)}
        self.memory.update({address: seed & 0xFF
                            for address in range(0x8003806C, 0x8003807C)})
        self.memory.update({address: seed & 0xFF
                            for address in range(0xBC000C00, 0xBC000C08)})
        self.registers = [(seed ^ index) & 0xFFFFFFFF for index in range(32)]
        self.registers[0], self.registers[29], self.registers[31] = 0, self.STACK, 0xDEAD0000
        self.before = self.registers[:]
        self.fprs = [0] * 32
        self.reads, self.writes, self.operations = [], [], []
        self.capture, self.snapshots, self.visits = set(), {}, {}
        self.min_sp = self.STACK

    def private(self, address, size):
        return self.STACK - 64 <= address and address + size <= self.STACK + 16

    def put(self, address, value, size):
        if not self.private(address, size):
            if (address, size) not in self.STORES:
                raise AssertionError('MMIO store exceeds address/width fence')
            self.operations.append(('write', address, size, value & ((1 << (size * 8)) - 1)))
        super().put(address, value, size)

    def get(self, address, size):
        value = super().get(address, size)
        if not self.private(address, size):
            self.operations.append(('read', address, size, value))
        return value

    def execute(self, word):
        super().execute(word)
        self.min_sp = min(self.min_sp, self.registers[29])

    def run(self):
        return super().run(budget=200, entry=self.ENTRY)

    def external(self):
        return {address: value for address, value in self.memory.items()
                if not self.private(address, 1)}


class InitMmioRecordTests(unittest.TestCase):
    EXPECTED = [('write', 0x80038070, 4, 0xBC000C02),
                ('write', 0x80038074, 2, 0x4040),
                ('write', 0xBC000C02, 2, 0x4040)]

    @classmethod
    def setUpClass(cls):
        retail.InitMmioAssemblyTests.setUpClass()
        cls.project = retail.InitMmioAssemblyTests.project
        if not (cls.project.parent / 'ido/ido5.3_recomp/cc').is_file():
            raise unittest.SkipTest('IDO is unavailable')
        for tool in ('mips-linux-gnu-ld', 'mips-linux-gnu-objcopy', 'mips-linux-gnu-objdump'):
            if shutil.which(tool) is None:
                raise unittest.SkipTest(tool + ' is unavailable')
        cls.retail = dict(retail.InitMmioAssemblyTests.entries)
        reference = b''.join(struct.pack('>I', cls.retail[pc]) for pc in sorted(cls.retail))
        if reference != (cls.project / 'conker.us.bin').read_bytes()[0x38E0:0x390C]:
            raise AssertionError('MMIO assembly differs from pristine ROM')
        cls.measurements = compile_trials()
        cls.output = cls.project / 'build/init-mmio-record-20261004'
        cls.images, cls.binaries = {}, {}
        for row in cls.measurements:
            key = row['shape'], row['profile']
            data = (cls.output / ('shape%d-%s.bin' % key)).read_bytes()
            cls.binaries[key] = data
            cls.images[key] = {MmioFixture.ENTRY + index * 4: word[0]
                               for index, word in enumerate(struct.iter_unpack('>I', data))}
        cls.pairs = 0

    @classmethod
    def tearDownClass(cls):
        (cls.output / 'qualification.json').write_text(json.dumps({
            'qualification': 'bounded-instruction-model-only; no host MMIO',
            'paired_traces': cls.pairs, 'expected_paired_traces': 60,
            'measurements': cls.measurements}, indent=2) + '\n')

    def test_complete_ordered_accesses_and_saved_registers(self):
        for seed in (0, 0xA5A5A5A5, 0xFFFFFFFF, 0x80000000, 0x12345678):
            reference = MmioFixture(self.retail, seed)
            reference.run()
            self.assertEqual(reference.operations, self.EXPECTED)
            for row in self.measurements:
                key = row['shape'], row['profile']
                with self.subTest(shape=key[0], profile=key[1], seed=seed):
                    guest = MmioFixture(self.images[key], seed)
                    guest.run()
                    self.assertEqual(guest.operations, reference.operations)
                    self.assertEqual(guest.external(), reference.external())
                    self.assertEqual(guest.min_sp, guest.STACK - row['frame_bytes'])
                    for register in (*range(16, 24), 28, 29, 30, 31):
                        self.assertEqual(guest.registers[register], guest.before[register])
                    type(self).pairs += 1

    def test_complete_allocations_still_do_not_match_retail(self):
        expected = {(1, 'o2g3'): (13, 13, 64, 0), (1, 'o2'): (12, 12, 48, 0),
                    (1, 'o1'): (13, 13, 64, 0), (1, 'o1g3'): (14, 14, 64, 0),
                    (2, 'o2g3'): (11, 9, 48, 0), (2, 'o2'): (10, 11, 48, 0),
                    (2, 'o1'): (11, 8, 48, 0), (2, 'o1g3'): (12, 10, 48, 0),
                    (3, 'o2g3'): (11, 9, 48, 0), (3, 'o2'): (10, 11, 48, 0),
                    (3, 'o1'): (17, 17, 80, 8), (3, 'o1g3'): (17, 17, 80, 8)}
        self.assertEqual({(row['shape'], row['profile']):
                          (row['body_words'], row['different_positions'],
                           row['text_bytes'], row['frame_bytes'])
                          for row in self.measurements}, expected)
        for row in self.measurements:
            data = self.binaries[row['shape'], row['profile']]
            self.assertFalse(row['exact'])
            self.assertEqual(len(data), row['text_bytes'])
            self.assertEqual(len(data) - row['body_words'] * 4, row['trailing_text_bytes'])
            self.assertFalse(any(data[row['body_words'] * 4:]))

    def test_record_layout_offsets_and_no_padding_store(self):
        for row in self.measurements:
            self.assertEqual(tuple(row['record_layout']), (8, 0, 4))
        self.assertEqual(self.EXPECTED[1][1] - self.EXPECTED[0][1], 4)
        source = (self.project / 'src/init_38E0.c').read_text()
        self.assertIn('#pragma GLOBAL_ASM("asm/nonmatchings/init_38E0/func_100038E0.s")', source)
        self.assertEqual(set(MmioFixture.STORES), {(address, size)
                         for _, address, size, _ in self.EXPECTED})

    def test_record_views_have_identical_optimized_instruction_images(self):
        for profile in ('o2g3', 'o2'):
            self.assertEqual(self.binaries[2, profile], self.binaries[3, profile])
        first = MmioFixture.ENTRY
        code = self.images[2, 'o2g3']
        self.assertEqual([code[first + offset] for offset in range(0, 8, 4)],
                         [0x3C028004, 0x24428070])
        self.assertEqual([code[first + offset] for offset in range(20, 36, 4)],
                         [0xAC4E0000, 0xA4430004, 0x3C0FBC00, 0xA5E30C02])

    def test_return_delay_store_is_executed(self):
        for key in ((2, 'o2'), (2, 'o1'), (3, 'o1')):
            row = next(row for row in self.measurements if (row['shape'], row['profile']) == key)
            first = MmioFixture.ENTRY
            code = self.images[key]
            self.assertEqual(code[first + (row['body_words'] - 2) * 4], 0x03E00008)
            self.assertEqual(code[first + (row['body_words'] - 1) * 4] >> 26, 41)
            guest = MmioFixture(code, 0xA5A5A5A5)
            guest.run()
            self.assertEqual(guest.operations[-1], self.EXPECTED[-1])

    def test_oracle_rejects_store_reordering_with_identical_final_memory(self):
        words = [self.retail[pc] for pc in sorted(self.retail)]
        reordered = words[:5] + words[7:9] + words[5:7] + words[9:]
        code = {MmioFixture.ENTRY + index * 4: word for index, word in enumerate(reordered)}
        reference, mutant = MmioFixture(self.retail, 0), MmioFixture(code, 0)
        reference.run()
        mutant.run()
        self.assertEqual(mutant.external(), reference.external())
        self.assertNotEqual(mutant.operations, reference.operations)

    def test_oracle_reports_an_extra_hardware_read(self):
        words = [self.retail[pc] for pc in sorted(self.retail)]
        extra = words[:9] + [0x94480000] + words[9:]  # lhu t0,0(v0)
        code = {MmioFixture.ENTRY + index * 4: word for index, word in enumerate(extra)}
        guest = MmioFixture(code, 0)
        guest.run()
        self.assertEqual(guest.operations, self.EXPECTED + [('read', 0xBC000C02, 2, 0x4040)])

    def test_output_fence_rejects_wrong_width_and_padding_writes(self):
        guest = MmioFixture(self.retail, 0)
        for address, size in ((0x80038074, 4), (0x80038076, 2), (0xBC000C02, 4)):
            with self.assertRaisesRegex(AssertionError, 'address/width fence'):
                guest.put(address, 0, size)

    def test_compiler_logs_are_empty(self):
        for row in self.measurements:
            self.assertEqual((self.output / ('shape%d-%s.log' %
                (row['shape'], row['profile']))).read_text(), '')


if __name__ == '__main__':
    unittest.main()
