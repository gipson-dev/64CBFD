"""Qualify the closed linked-record tail transformation before counting a match."""

import csv
import itertools
import json
import re
import struct
import subprocess
import unittest
from pathlib import Path
from unittest import mock

from tools import pad_generated_object as pad
from tools.experiments import game_linked_record_tail_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK


ENTRY = 0x150E6FAC
ACTOR, NODE, RECORD, ALTERNATE, OUTPUT = 0x20000, 0x21000, 0x22000, 0x23000, 0x24000
LOOKUP, FRACTION, WORD, ANGULAR = 0x1514ECE0, 0x150ADA68, 0x150ADA20, 0x151423D8


def memory_case():
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
    for base, size in ((ACTOR, 0x300), (NODE, 0x20), (RECORD, 0x50), (ALTERNATE, 0x50), (OUTPUT, 20)):
        memory.update({base + i: 0xA5 for i in range(size)})
    put(memory, ACTOR + 0x2F4, 0x12345678)
    put(memory, NODE + 0x10, RECORD)
    for base, offsets, values in ((ACTOR, (0x14, 0x18, 0x1C), (10.0, 20.0, 30.0)),
                                 (RECORD, (0x38, 0x3C, 0x40), (0.25, -0.5, 1.0)),
                                 (ALTERNATE, (0x38, 0x3C, 0x40), (1.0, 2.0, 3.0))):
        for offset, value in zip(offsets, values):
            put(memory, base + offset, bits(value))
    return memory


def mutation(memory, index):
    put(memory, ACTOR + 0x14, bits(float(index * 10)))
    put(memory, NODE + 0x10, ALTERNATE)


def external(memory):
    return {a: v for a, v in memory.items() if not STACK - 0x600 <= a < STACK + 0x100}


class PositionOracle(TriangleOracle):
    def __init__(self, words, memory, found=1, random_word=0, fraction=0.5, mutate=0, output=OUTPUT + 4, phase=0):
        super().__init__(words, memory, entry=ENTRY, phase=phase, arguments=(output, ACTOR))
        self.found, self.random_word, self.fraction, self.mutate = found, random_word, fraction, mutate

    def record_call(self, target):
        index = len(self.calls)
        assert target == (LOOKUP, FRACTION, WORD, ANGULAR, ANGULAR)[index]
        if target == LOOKUP:
            node, key, result = self.r[4:7]
            assert node == 0x12345678 and key == 0x16
            assert result == self.before[29] - 4
            args = (node, key, 'private-node')
        elif target == ANGULAR:
            args = (self.r[4],)
            assert args == (((self.random_word - 64) if index == 3 else self.random_word) & 255,)
        else:
            args = ()
        self.calls.append((target, *args))
        self.events.append(('CALL', target, args))

    def hook(self, target):
        index = len(self.calls) - 1
        result_pointer = self.r[6]
        if self.mutate & (1 << index):
            mutation(self.memory, index + 1)
        if target == LOOKUP and self.found:
            self.put(result_pointer, NODE, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        if target == LOOKUP:
            self.r[2] = self.found & 0xFFFFFFFF
        elif target == FRACTION:
            self.f[0] = bits(self.fraction)
        elif target == WORD:
            self.r[2] = self.random_word & 0xFFFFFFFF
        else:
            self.f[0] = bits(0.5 if index == 3 else -0.25)


def reference(memory, found, random_word, fraction, mutate, output):
    memory = dict(memory)
    writes = []

    def read(address):
        return int.from_bytes(bytes(memory[address + i] for i in range(4)), 'big')

    def add(a, b):
        return bits(floating(a) + floating(b))

    def mul(a, b):
        return bits(floating(a) * floating(b))

    for index in range(5 if found else 1):
        if mutate & (1 << index):
            mutation(memory, index + 1)
    radius = add(mul(bits(fraction), bits(100.0)), bits(80.0))
    record = read(NODE + 0x10) if found else None
    for axis in range(3):
        coordinate = read(ACTOR + 0x14 + axis * 4)
        if found:
            coordinate = add(coordinate, mul(read(record + 0x38 + axis * 4), bits(-80.0)))
            coordinate = add(coordinate, bits(100.0) if axis == 1 else
                             mul(bits(0.5 if axis == 0 else -0.25), radius))
        put(memory, output + axis * 4, coordinate)
        writes.append(('W', output + axis * 4, 4, coordinate))
    return memory, writes


class GameLinkedRecordTailMatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-linked-record-tail-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, cls.output, 'checkpoint', screen.CHECKPOINT)
        cls.normalized = screen.normalize(cls.raw)
        cls.retail = list(struct.unpack_from('>72I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0x11445C))

    def test_complete_closed_tail_and_frozen_source(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (71, 0x38, 15))
        self.assertEqual(self.normalized, self.retail)
        self.assertEqual(self.raw[:10], self.retail[:10])
        self.assertEqual(self.raw[11:58], self.retail[11:58])
        self.assertEqual(self.raw[60:], self.retail[61:])
        self.assertEqual(self.normalized[58:61], [self.raw[59], 0x10000008, self.raw[66]])
        source = (self.root / 'conker/src/game/generated_113D60.c').read_text()
        self.assertEqual(re.search(r'void func_150E6FAC\([^;{]+\) \{\n.*?\n\}', source, re.S).group(), screen.CHECKPOINT)

    def test_independent_reference_both_paths_aliases_mutations_and_saved_state(self):
        coverage, cases = set(), 0
        for found, word, fraction, mutate, output, phase in itertools.product(
                (0, 1, -1), (0, 63, 64, 255, 256, -1, 0x80000040), (-1.0, 0.0, 0.5, 1.0, 2.0),
                (0, 1, 16, 31), (OUTPUT + 4, ACTOR + 0x18, RECORD + 0x3C, NODE + 0x10), (0, 8)):
            memory = memory_case()
            expected, writes = reference(memory, found, word, fraction, mutate, output)
            models = [PositionOracle(words, memory, found, word, fraction, mutate, output, phase).run()
                      for words in (self.retail, self.raw, self.normalized)]
            for model in models:
                self.assertEqual(external(model.memory), external(expected))
                self.assertEqual([e for e in model.events if e[0] == 'W' and e[1] >= ACTOR and e[1] < OUTPUT + 20], writes)
                self.assertEqual(model.calls, models[0].calls)
                self.assertEqual([e for e in model.events if e[0] == 'CALL' or
                                  e[0] == 'R' and not STACK - 0x600 <= e[1] < STACK + 0x100],
                                 [e for e in models[0].events if e[0] == 'CALL' or
                                  e[0] == 'R' and not STACK - 0x600 <= e[1] < STACK + 0x100])
            coverage.update(models[0].visits)
            cases += 1
        self.assertEqual(cases, 3360)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 288, 4)) - {ENTRY + 61 * 4})
        (self.output / 'behavior.json').write_text(json.dumps(dict(cases=cases, models=3,
             executed_words=len(coverage), always_unreachable_word=hex(ENTRY + 61 * 4)), indent=2) + '\n')

    def test_stale_and_each_incomplete_guard_has_a_control_flow_counterexample(self):
        for offset in screen.GUARDS:
            stale = self.raw[:]
            stale[offset // 4] ^= 1
            with self.assertRaisesRegex(ValueError, 'stale linked-record guard'):
                screen.normalize(stale)
            failed = False
            for found in (0, 1):
                try:
                    model = PositionOracle(screen.normalize(self.raw, omitted=offset), memory_case(), found=found).run()
                except (AssertionError, KeyError):
                    failed = True
                else:
                    wanted, _ = reference(memory_case(), found, 0, 0.5, 0, OUTPUT + 4)
                    failed |= external(model.memory) != external(wanted)
                    retail = PositionOracle(self.retail, memory_case(), found=found).run()
                    failed |= [e for e in model.events if e[0] == 'R' and ACTOR <= e[1] < OUTPUT + 20] != \
                              [e for e in retail.events if e[0] == 'R' and ACTOR <= e[1] < OUTPUT + 20]
            self.assertTrue(failed, hex(offset))

    def test_source_and_profile_inventory_boundaries(self):
        self.assertEqual((len(screen.candidates()), len(dict(screen.candidates()))), (4, 4))
        for name, body in screen.candidates():
            for profile, flags in screen.PROFILES.items():
                record, words = screen.compile_candidate(self.root, self.output, name + '-' + profile, body, flags)
                expected = (74, 52) if 'peep' in profile else (71, 15)
                self.assertEqual((record['body_words'], record['differences']), expected)
                self.assertEqual(record['diagnostics'], '')
                if 'peep' not in profile:
                    self.assertEqual(words, self.raw)

    def test_actual_emitter_rejects_stale_words_and_relocations(self):
        name = 'func_150E6FAC'
        patches = {(name, offset): dict(expected=expected, replacement=replacement,
                   expected_relocations=[], replacement_relocations=[], insert_after=inserted,
                   insert_after_relocations=[], omit=False)
                   for offset, (expected, replacement, inserted) in screen.GUARDS.items()}
        obj = self.output / 'checkpoint.o'
        text, functions, relocations = pad.parse_object(obj)
        start = functions[name]['value']
        with mock.patch.object(pad, 'parse_retail_slice', return_value=(ENTRY, ENTRY + 288, {name: ENTRY}, {})), \
                mock.patch.object(pad, 'load_word_patches', return_value=patches):
            emitted = pad.emit_padded_assembly(obj, self.root / 'conker/asm/113D60.s')
            self.assertEqual([int(w, 16) for w in re.findall(r'^\.word (0x[0-9A-F]+)$', emitted, re.M)],
                             screen.normalize(list(struct.unpack('>71I', text[start:start + 284]))))
            self.assertEqual(emitted.count('.word '), 72)
            assembly, padded, elf = (self.output / ('emitted' + suffix) for suffix in ('.s', '.o', '.elf'))
            assembly.write_text(emitted)
            subprocess.run(['mips-linux-gnu-as', '-EB', '-mtune=vr4300', '-march=vr4300', '-mabi=32',
                            '-o', str(padded), str(assembly)], capture_output=True, text=True, check=True)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output / 'position.ld'),
                            '-e', name, *['--defsym=func_%08X=0x%08X' % (s, s) for s in screen.SYMBOLS],
                            '-o', str(elf), str(padded)], capture_output=True, text=True, check=True)
            self.assertEqual(load_elf_functions(str(elf), 'mips-linux-gnu-objdump')[0][name], self.retail)
            for offset in screen.GUARDS:
                changed = bytearray(text)
                struct.pack_into('>I', changed, start + offset, screen.GUARDS[offset][0] ^ 1)
                with mock.patch.object(pad, 'parse_object', return_value=(bytes(changed), functions, relocations)):
                    with self.assertRaisesRegex(ValueError, 'stale word patch'):
                        pad.emit_padded_assembly(obj, self.root / 'conker/asm/113D60.s')
                shifted = dict(relocations)
                shifted[start + offset] = [('R_MIPS_HI16', 'D_800D2350')]
                with mock.patch.object(pad, 'parse_object', return_value=(text, functions, shifted)):
                    with self.assertRaisesRegex(ValueError, 'stale relocations'):
                        pad.emit_padded_assembly(obj, self.root / 'conker/asm/113D60.s')

    def test_production_guards_and_linked_slot(self):
        name = 'func_150E6FAC'
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = [r for r in csv.DictReader(stream) if r['function'] == name]
        self.assertEqual(len(rows), 3)
        for row in rows:
            offset = int(row['offset'], 0)
            expected, replacement, inserted = screen.GUARDS[offset]
            self.assertEqual((int(row['expected'], 0), int(row['replacement'], 0)), (expected, replacement))
            self.assertEqual(row['filename'], 'generated_113D60')
            self.assertEqual((row['expected_relocations'], row['replacement_relocations'], row['omit']), ('-', '-', 'false'))
            self.assertEqual(row['insert_after'], '' if inserted is None else '0x%08X' % inserted)
            self.assertEqual(row['insert_after_relocations'], '' if inserted is None else '-')
        functions = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        self.assertEqual(functions[name], self.retail)


if __name__ == '__main__':
    unittest.main()
