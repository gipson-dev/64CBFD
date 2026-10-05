"""Full attachment-walker traces before/after guarded register renaming."""

import csv
import hashlib
import json
import shutil
import struct
import subprocess
import sys
import unittest
from pathlib import Path

from tools.match_progress import load_elf_functions
from tools.tests import test_game_queued_segment_writer as queue
from tools.tests.test_game_viewport_renderer import RendererOracle


ENTRY, LEAF = 0x15168E54, 0x15168E34


def case(opcode, subtype, word):
    memory = {queue.OUTPUT + i: 0xA5 for i in range(-8, 48)}
    memory.update({queue.STACK + i: 0xA5 for i in range(-0x80, 0x40)})
    for index, (op, kind, value) in enumerate(((opcode, subtype, word), (1, 14, 8),
                                              (0xDF, 0, 0x12345678), (1, 14, 0x1111))):
        data = bytes((op, 0xA5, 0xA5, kind)) + struct.pack('>I', value)
        memory.update({queue.OUTPUT + index * 8 + i: byte for i, byte in enumerate(data)})
    return memory


class AttachmentOracle(RendererOracle):
    def __init__(self, words, leaf, memory, base, mutation=0, opening=None):
        queue.SegmentQueueOracle.__init__(self, words, ENTRY, memory, (queue.OUTPUT, base))
        self.connected = dict(zip(range(LEAF, LEAF + len(leaf) * 4, 4), leaf)) if leaf else {}
        self.code.update(self.connected)
        self.calls, self.mutation, self.opening = [], mutation, opening
        self.opening_reads = 0

    def put(self, address, value, size):
        queue.SegmentQueueOracle.put(self, address, value, size)

    def get(self, address, size):
        value = RendererOracle.get(self, address, size)
        if address == queue.OUTPUT and size == 1:
            self.opening_reads += 1
            if self.opening_reads == 1 and self.opening is not None:
                self.put(address, self.opening, 1)
        return value

    def execute(self, word):
        if word >> 26 == 32:
            immediate = word & 65535
            immediate = immediate if immediate < 32768 else immediate - 65536
            address = (self.r[word >> 21 & 31] + immediate) & 0xFFFFFFFF
            value = self.get(address, 1)
            self.r[word >> 16 & 31] = (value if value < 128 else value - 256) & 0xFFFFFFFF
            self.r[0] = 0
        else:
            RendererOracle.execute(self, word)

    def record_call(self, target):
        assert target == LEAF
        self.calls.append((target, self.r[4], self.r[5]))

    def hook(self, target):
        assert target == LEAF
        value = self.get(self.r[4], 4)
        if not value & 0x0F000000:
            self.put(self.r[4], value + self.r[5], 4)
        if len(self.calls) == 1:
            if self.mutation == 1:
                self.put(queue.OUTPUT + 8, 0xDF, 1)
            elif self.mutation == 2:
                self.put(queue.OUTPUT + 8, 0xDC, 1)
                self.put(queue.OUTPUT + 11, 14, 1)
                self.put(queue.OUTPUT + 12, 0xFFFFF000, 4)
            elif self.mutation == 3:
                self.put(queue.OUTPUT + 8, 0, 1)
        for register in (2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register


class GameAttachmentCursorMatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(name) is None for name in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        result = subprocess.run([sys.executable, '-m', 'tools.experiments.game_attachment_cursor_candidates'],
            cwd=cls.root, capture_output=True, text=True, timeout=120)
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        cls.output = cls.root / 'conker/build/game-attachment-cursor'
        cls.records = json.loads((cls.output / 'screen.json').read_text())
        fresh, _, _ = load_elf_functions(str(cls.output / 'pointer-s8.elf'), 'mips-linux-gnu-objdump')
        cls.raw = fresh['func_15168E54'][:45]
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>45I', rom, 0x196304))
        cls.leaf = list(struct.unpack_from('>8I', rom, 0x1962E4))
        with (cls.root / 'conker/retail_word_patches.us.csv').open() as stream:
            cls.patches = [row for row in csv.DictReader(stream) if row['function'] == 'func_15168E54']
        cls.guarded = cls.raw[:]
        for row in cls.patches:
            index = int(row['offset'], 0) // 4
            if cls.guarded[index] != int(row['expected'], 0):
                raise AssertionError('compiled guard input changed')
            cls.guarded[index] = int(row['replacement'], 0)

    def test_screen_keeps_full_body_and_guards_are_only_the_nine_differences(self):
        self.assertEqual(len(self.records), 36)
        self.assertFalse(any(row['real_differences'] == 0 for row in self.records))
        self.assertEqual(hashlib.sha256(struct.pack('>45I', *self.raw)).hexdigest(),
                         '958dcb84bbf375ebdd6c9170744538d8a59afb5385c31977ab50158843aca792')
        differences = {i * 4: (a, b) for i, (a, b) in enumerate(zip(self.raw, self.retail)) if a != b}
        self.assertEqual(len(self.patches), 9)
        self.assertEqual({int(row['offset'], 0): (int(row['expected'], 0), int(row['replacement'], 0))
                          for row in self.patches}, differences)
        for row in self.patches:
            self.assertEqual(row['filename'], 'game_1944C0')
            self.assertEqual((row['expected_relocations'], row['replacement_relocations']), ('-', '-'))
            self.assertEqual((row['insert_after'], row['omit']), ('', 'false'))
        self.assertEqual(self.guarded, self.retail)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                    'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_15168E54'], ENTRY)
        self.assertEqual(functions['func_15168E54'], self.retail)

    def paired(self, memory, base, leaf=None, mutation=0, opening=None):
        models = [AttachmentOracle(words, leaf, memory, base, mutation, opening).run()
                  for words in (self.retail, self.raw, self.guarded)]
        first = models[0]
        for model in models[1:]:
            self.assertEqual(model.memory, first.memory)
            self.assertEqual(model.calls, first.calls)
            self.assertEqual(model.reads, first.reads)
            self.assertEqual(model.stores, first.stores)
        return models

    def test_connected_leaf_traces_cover_all_walker_and_leaf_words(self):
        coverage = [set(), set(), set()]
        pairs = 0
        for opcode in range(256):
            for subtype in (0, 13, 14, 15, 255):
                models = self.paired(case(opcode, subtype, 0x1000), 0xFFFFFFF0, self.leaf)
                for visited, model in zip(coverage, models):
                    visited.update(model.visits)
                pairs += 1
        words = (0, 1, 0xFFFFFFFF, 0x80000000, 0x10000000, 0x01000000, 0x0F000000)
        for word in words:
            for base in words:
                for opcode, subtype in ((1, 0), (0xDC, 14), (0xDC, 13)):
                    models = self.paired(case(opcode, subtype, word), base, self.leaf)
                    for visited, model in zip(coverage, models):
                        visited.update(model.visits)
                    pairs += 1
        expected = set(range(ENTRY, ENTRY + 45 * 4, 4)) | set(range(LEAF, LEAF + 8 * 4, 4))
        self.assertEqual(coverage, [expected] * 3)
        self.assertEqual(pairs, 1427)
        print('attachment connected traces:', pairs, 'three-way cases, full 45+8 word coverage')

    def test_opaque_leaf_clobbering_and_next_command_and_opening_reload_mutations(self):
        for mutation in range(4):
            models = self.paired(case(1, 0, 0x1000), 0xFFFFFFF0, mutation=mutation)
            self.assertEqual(len(models[0].calls), 1 if mutation in (1, 3) else 2)
        for before in (0, 1, 0xDC, 0xDF):
            for after in (0, 1, 0xDC, 0xDF):
                models = self.paired(case(before, 14, 0x1000), 16, opening=after)
                self.assertEqual(models[0].opening_reads, 1 if before == 0xDF else 2)

    def test_neighboring_leaves_and_walkers_keep_checkpoint_bytes(self):
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                    'mips-linux-gnu-objdump')
        checkpoints = {
            'func_15168B10': '68036065f0b70cec817bb2da07d8b64e74700ff8ba629f5b96d3fa63466b7a25',
            'func_15168E34': 'e067fd7c0707eda03e9b507c1b8105321b98faf2e5509d9a7d58e3effa1db57c',
            'func_15168F08': '87b6edb1eaa07348ff987b92fadfd41fe157af7bb3bd4bd60ee33b3b46bc764f',
            'func_15168F84': '3d1b60f9cb6b350c57087d1c39204e797a6a1c5e4504090a902159027a2f57a3',
        }
        for name, digest in checkpoints.items():
            self.assertEqual(addresses[name], int(name[5:], 16))
            words = functions[name]
            self.assertEqual(hashlib.sha256(struct.pack('>' + str(len(words)) + 'I', *words)).hexdigest(),
                             digest, name)

    def test_omitting_any_guard_breaks_the_closed_register_allocation(self):
        for row in self.patches:
            index = int(row['offset'], 0) // 4
            partial = self.guarded[:]
            partial[index] = self.raw[index]
            rejected = False
            for opcode, subtype in ((1, 0), (0xDC, 14)):
                memory = case(opcode, subtype, 0x1000)
                reference = AttachmentOracle(self.retail, None, memory, 16).run()
                try:
                    candidate = AttachmentOracle(partial, None, memory, 16).run()
                    rejected |= (candidate.memory != reference.memory or candidate.calls != reference.calls
                                 or candidate.reads != reference.reads or candidate.stores != reference.stores)
                except (AssertionError, KeyError):
                    rejected = True
            self.assertTrue(rejected, 'partial allocation unexpectedly accepted at ' + row['offset'])


if __name__ == '__main__':
    unittest.main()
