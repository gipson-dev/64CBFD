"""Direct retail caller fit, full guest effects and real owner/padder gates."""

import csv
import itertools
import json
import re
import struct
import subprocess

from tools.experiments import game_scaled_sphere_query_address_view_candidates as screen
from tools.experiments.game_actor_classifier_candidates import sections
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_scaled_sphere_query_source_layout as recovery
from tools.tests.game_owner_pool import assert_guard_history
from tools.tests.test_game_projection_lifetime_recovery import peek
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly


class GameScaledSphereQueryMatchTests(recovery.GameScaledSphereSourceLayoutTests):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.out = cls.root / 'conker/build/game-scaled-sphere-query-match-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected', screen.SELECTED)
        assert cls.fixture.count(screen.SCALE_FIRST) == 1
        cls.fixture = cls.fixture.replace(screen.SCALE_FIRST, screen.SELECTED)
        assert cls.fixture.count(screen.SELECTED) == 1 and screen.SCALE_FIRST not in cls.fixture
        (cls.out / 'selected-record.json').write_text(json.dumps(cls.record, indent=2) + '\n')

    def equal_guest(self, models):
        original, candidate = models
        self.assertEqual(candidate.memory, original.memory)
        self.assertEqual(candidate.events, original.events)
        self.assertEqual(candidate.r, original.r)
        self.assertEqual(candidate.f, original.f)
        self.assertEqual(candidate.visits, original.visits)
        self.assertEqual(candidate.calls, original.calls)
        self.assertEqual(candidate.snapshots, original.snapshots)
        return models

    def check(self, memory, args, phase=0):
        return self.equal_guest(super().check(memory, args, phase))

    def check_actor(self, memory, args, phase=0):
        return self.equal_guest(super().check_actor(memory, args, phase))

    def test_recovered_original_layout_and_uninstalled_oversized_fit(self):
        """The historical recovery gate now requires the complete direct fit."""
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (110, 136, 0))
        self.assertEqual(self.words, self.retail)
        self.assertTrue(self.record['exact'])
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.record['profile'], 'o2g3')
        self.assertEqual(screen.local_layout(self.out / 'selected.o'), dict(frame=136, entry_relative=dict(
            center=-12, radius=-16, height=-20, origin=-32, direction=-44, scaledCenter=-56,
            length=-60, first=-64, second=-68, scale=-72, inverse=-76, reciprocal=-80)))
        self.assertEqual(self.record['relocations'], {0x58: [('R_MIPS_26', 'func_1515C1A0')],
            0xFC: [('R_MIPS_26', 'func_15145128')], 0x168: [('R_MIPS_26', 'func_151451F0')]})
        memory, args = recovery.actor_fixture(center=(5.0, 5.0, 0.0),
            scale=(2.0, 0.5), direction=(10.0, 10.0, 0.0))
        for model in self.check_actor(memory, args):
            spill = next(i for i, e in enumerate(model.events) if e[:3] == ('W', model.caller_frame + 0x3C, 4))
            reads = [e[1] for e in model.events[:spill] if e[0] == 'R' and e[1] in (args[2] + 0xDC, args[2] + 0xE0)]
            self.assertEqual(reads, [args[2] + 0xE0, args[2] + 0xDC])

    def test_gate_storage_and_live_home_controls_do_not_fix_the_fit(self):
        """Pin the new controls, including three independently direct fits."""
        records, identical, exact = [], [], []
        _, capture_first = screen.compile_candidate(self.root, self.out, 'capture-first', screen.SCALE_FIRST)
        for name, body in screen.candidates():
            record, words = screen.compile_candidate(self.root, self.out, name, body)
            if name.startswith('nested'):
                expected = (110, 136, 0) if name.endswith('-normalizer') else (111, 136, 71)
            elif name == 'reciprocal-scope-height-gate':
                expected = (112, 136, 86)
            elif name == 'reciprocal-scope-normalizer':
                expected = (111, 136, 71)
            elif name.startswith('scope') or name == 'reciprocal-scope-capture':
                expected = (111, 136, 73)
            else:
                expected = (111, 136, 72)
            self.assertEqual((record['body_words'], record['frame'], record['differences']), expected, name)
            self.assertEqual(record['diagnostics'], '')
            self.assertEqual(record['profile'], 'o2g3')
            record['layout'] = screen.local_layout(self.out / (name + '.o'))
            self.assertEqual(record['layout'], screen.local_layout(self.out / 'selected.o'), name)
            if words == capture_first:
                identical.append(name)
            if record['exact']:
                self.assertEqual(words, self.retail)
                exact.append(name)
            records.append(record)
        self.assertEqual(len(records), 51)
        self.assertEqual(len(identical), 33)
        self.assertEqual(exact, ['nested%d-reciprocal-normalizer' % count for count in (3, 6, 9)])
        (self.out / 'address-view-records.json').write_text(json.dumps(records, indent=2) + '\n')

    def test_three_inverse_first_forms_are_effective_compiled_negatives(self):
        forms = dict(screen.candidates())
        for name, phase in itertools.product(('capture-scale-result', 'scope3-initialize-inverse',
                'scope9-initialize-inverse'), (0, 8)):
            _, words = screen.compile_candidate(self.root, self.out, name + '-negative', forms[name])
            memory, args = recovery.actor_fixture(phase=phase, center=(5.0, 5.0, 0.0),
                scale=(2.0, 0.5), direction=(10.0, 10.0, 0.0))
            original, _ = self.check_actor(memory, args, phase)
            wrong = recovery.recovery.QueryOracle(words, memory, args, self.connected, phase).run()
            self.assertEqual(wrong.r[2], original.r[2])
            self.assertEqual(wrong.r[2], 1)
            self.assertEqual(tuple(peek(wrong.memory, pointer + 4) for pointer in args[3:5]),
                (0x409A7C98, 0xC014F92F))
            self.assertNotEqual(wrong.events, original.events)

    def test_copied_owner_preserves_neighbors_but_padder_uses_overflow(self):
        """The actual padder must now emit the direct slot, never an overflow."""
        obj = self.check_copied_owner(screen.SELECTED, return_owner=True)
        assembly = emit_padded_assembly(obj, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=self.root / 'conker/retail_word_patches.us.csv')
        begin = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), begin)
        body = assembly[begin:assembly.index('\n', end) + 1]
        self.assertNotIn('__retail_overflow_' + screen.FUNCTION, assembly)
        self.assertEqual(len(re.findall(r'\.word 0x[0-9A-F]{8}', body)), 110)
        asm, padded, elf = (self.out / ('padded' + suffix) for suffix in ('.s', '.o', '.elf'))
        asm.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + body)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(padded), str(asm)],
            check=True, capture_output=True)
        _, functions, rel = parse_object(padded)
        self.assertEqual(functions[screen.FUNCTION]['size'], 440)
        self.assertEqual(rel, self.record['relocations'])
        symbols = recovery.recovery.screen.SYMBOLS
        for alternate in (None, *symbols):
            targets = {name: address + (0x100000 if name == alternate else 0) for name, address in symbols.items()}
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'selected.ld'),
                '-e', screen.FUNCTION, *['--defsym=%s=0x%X' % item for item in targets.items()],
                '-o', str(elf), str(padded)], check=True, capture_output=True)
            expected = self.retail.copy()
            for offset, relocations in self.record['relocations'].items():
                expected[offset // 4] = 0x0C000000 | (targets[relocations[0][1]] >> 2 & 0x3FFFFFF)
            self.assertEqual(list(struct.unpack_from('>110I', sections(elf)['.text'][1])), expected)
        (self.out / 'owner-padded.s').write_text(assembly)

    def test_production_source_slot_and_unchanged_guard_history(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertEqual(source.count(screen.SELECTED), 1)
        self.assertNotIn('s32 func_15145AD8() {\n    return 0;\n}', source)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertEqual(len(guards), 11006)
        self.assertEqual([row for row in guards if row['function'] == screen.FUNCTION], [])


if __name__ == '__main__':
    import unittest
    unittest.main()
