"""Recovered cursor phase, original homes and a strictly closed register cycle."""

import csv
import itertools
import json
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_point_list_transform_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_point_list_transform_audit as audit
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_point_transform_match import external_memory
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly


class GamePointListTransformMatchTests(unittest.TestCase):
    run_host = audit.GamePointListTransformAuditTests.run_host
    BODY = screen.SELECTED
    test_actual_native_32bit_phase_and_provider_mutation = audit.GamePointListTransformAuditTests.test_actual_32bit_c_every_translation_halfword_and_callback_mutation

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-point-list-match-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected', screen.SELECTED)
        cls.retail = list(struct.unpack_from('>57I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.normalized = screen.normalize(cls.words)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        helper = struct.unpack_from('>40I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0xD4E10)
        cls.connected = dict(zip(range(audit.TRANSFORM, audit.TRANSFORM + 160, 4), helper))

    def receipt(self, name, data):
        (self.out / (name + '.json')).write_text(json.dumps(data, indent=2) + '\n')

    def model(self, words, memory, args, **kwargs):
        return audit.PointListOracle(words, memory, args, **kwargs).run()

    def check_case(self, memory, args, **kwargs):
        wanted_args = list(args)
        mask = kwargs.get('home', 0)
        if mask & 1:
            wanted_args[1] += 4
        if mask & 2:
            wanted_args[2] += 4
        expected, calls = audit.reference(memory, wanted_args, kwargs.get('change', False))
        models = [self.model(words, memory, args, **kwargs) for words in (self.words, self.normalized, self.retail)]
        for model in models:
            self.assertEqual(external_memory(model.memory), external_memory(expected))
            self.assertEqual(model.calls, calls)
        public = lambda model: [event for event in model.events if not audit.STACK - 0x600 <= event[1] < audit.STACK + 0x140]
        self.assertEqual(public(models[0]), public(models[2]))
        self.assertEqual(public(models[1]), public(models[2]))
        self.assertEqual(models[0].memory, models[2].memory)
        self.assertEqual(models[1].memory, models[2].memory)
        return models

    def test_complete_cycle_two_prologue_permutations_and_all_guard_words(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (57, 0x88, 19))
        self.assertEqual(self.record['pool_bytes'], 0)
        self.assertEqual(self.normalized, self.retail)
        self.assertEqual(self.words[:2], self.retail[:2])
        self.assertEqual(self.words[50:], self.retail[50:])
        self.assertEqual({self.words[i] for i in (2, 8)}, {self.retail[i] for i in (2, 8)})
        raw, functions, rel = parse_object(self.out / 'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['size'], 228)
        self.assertEqual(rel, {0x38: [('R_MIPS_26', 'func_150A8050')], 0xB0: [('R_MIPS_26', 'func_150A7960')]})
        rows = screen.owner_guards()
        changes = [i * 4 for i, (a, b) in enumerate(zip(self.words, self.retail)) if a != b]
        self.assertEqual(changes, [int(row['offset'], 16) for row in rows])
        applied = self.words.copy()
        for row in rows:
            offset = int(row['offset'], 16)
            self.assertEqual(struct.unpack_from('>I', raw, offset)[0], int(row['expected'], 16))
            self.assertEqual(row['expected_relocations'], '-')
            self.assertEqual(row['replacement_relocations'], '-')
            self.assertNotIn(offset, rel)
            self.assertEqual((row['insert_after'], row['omit']), ('', 'false'))
            applied[offset // 4] = int(row['replacement'], 16)
        self.assertEqual(applied, self.retail)
        self.receipt('cycle', dict(words=57, frame=136, raw_differences=19, normalized_differences=0,
            cycle=[16, 17, 18], independent_swaps=[[2, 8], [4, 5]], changed_private_offsets=0,
            insertions=0, omissions=0, call_relocations_untouched=True))

    def test_complete_guest_calls_aliases_and_connected_original_point_helper(self):
        count, coverage, helper_coverage = 0, set(), set()
        for remaining, n, alias, change, phase in itertools.product(audit.COUNTS, range(16), range(3), (False, True), (0, 8)):
            memory, args = audit.fixture(remaining, n, alias)
            for model in self.check_case(memory, args, change=change, phase=phase):
                coverage.update(model.visits)
            count += 1
        self.assertEqual(coverage, set(range(screen.ENTRY, screen.ENTRY + 228, 4)))
        for remaining, n, alias, change, phase in itertools.product((1, 2, 4), range(16), range(3), (False, True), (0, 8)):
            memory, args = audit.fixture(remaining, n, alias)
            for model in self.check_case(memory, args, change=change, phase=phase, connected=self.connected):
                helper_coverage.update(model.visits & self.connected.keys())
            count += 1
        self.assertEqual(helper_coverage, set(self.connected))
        self.receipt('effects', dict(cases=count, guest=1344, connected=576, all_wrapper_and_helper_words=True,
            complete_memory_public_traces_calls_saved_state=True, rotation_provider_bounded=True,
            no_hardware_or_general_FCSR_claim=True))

    def test_each_list_home_readback_independently_and_both_stack_phases(self):
        count = 0
        for remaining, mask, n, alias, change, phase in itertools.product((0, 1, 2, 4), (1, 2, 3), range(16), range(3), (False, True), (0, 8)):
            memory, args = audit.fixture(remaining, n, alias)
            self.check_case(memory, args, home=mask, change=change, phase=phase, connected=self.connected)
            count += 1
        self.receipt('homes', dict(cases=count, each_incoming_list_and_both=True,
            raw_and_normalized_match_original=True, private_physical_homes_not_relocated=True,
            nonstandard_guest_ABI_probe_not_general_native_C_permission=True))

    def test_required_storage_fails_closed_and_nonpositive_counts_skip_lists(self):
        count = 0
        for remaining in (0, 2):
            required = [(audit.ACTOR + offset, size) for offset, size in ((0, 4), (4, 4), (8, 4), (16, 2), (18, 2), (20, 2))]
            if remaining:
                required += [(audit.INPUT, 4), (audit.OUTPUT, 4), (audit.POINTS, 4), (audit.RESULTS, 4)]
            for address, size in required:
                memory, args = audit.fixture(remaining)
                for byte in range(size):
                    del memory[address + byte]
                for words in (self.words, self.normalized, self.retail):
                    with self.assertRaises((AssertionError, KeyError)):
                        self.model(words, memory, args, connected=self.connected)
                count += 1
        for remaining in audit.COUNTS[:4]:
            memory, args = audit.fixture(remaining)
            for address in list(memory):
                if audit.INPUT - 16 <= address < audit.ALTERNATE + 272:
                    del memory[address]
            self.check_case(memory, args, connected=self.connected)
        self.receipt('unmapped', dict(required_cases=count, nonpositive_cases=4, fail_closed=True))

    def test_40_new_address_structure_phase_count_controls_and_effective_negatives(self):
        forms = [(name, body, screen.DECLARATIONS) for name, body in screen.address_candidates()]
        forms += list(screen.structured_candidates())
        forms += [(name, body, screen.DECLARATIONS) for name, body in itertools.chain(screen.phase_candidates(), screen.count_candidates())]
        self.assertEqual(len(forms), 40)
        records = []
        for name, body, declarations in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, declarations=declarations)
            self.assertEqual(record['pool_bytes'], 0)
            self.assertGreater(record['differences'], 0)
            for remaining, alias, change in itertools.product((-1, 0, 2), range(3), (False, True)):
                memory, args = audit.fixture(remaining, 7, alias)
                expected, calls = audit.reference(memory, args, change)
                model = self.model(words, memory, args, change=change)
                self.assertEqual((external_memory(model.memory), model.calls), (external_memory(expected), calls), name)
            records.append(record)
        lines = '\n'.join('    matrix[3][%d] = *(s16 *)(cursor + 0x%X);' % (i, 16 + i * 2) for i in range(3)) + '\n'
        negatives = dict(unsigned_translation=screen.SELECTED.replace('*(s16 *)', '*(u16 *)'),
            exact_one_count=screen.SELECTED.replace('count > 0', 'count == 1'),
            wrong_input_stride=screen.SELECTED.replace('cursor += 4;', 'cursor += 8;'),
            cached_first_source=screen.SELECTED.replace('    while (count > 0)', '    src = *(struct17 **)cursor;\n    while (count > 0)').replace('        src = *(struct17 **)cursor;\n', ''),
            wrong_output_list=screen.SELECTED.replace('output = destinations;', 'output = input;'),
            translation_before_provider=screen.SELECTED.replace(lines, '').replace('    func_150A8050(', lines + '    func_150A8050(', 1),
            legacy_saved_lists=screen.BASELINE)
        detected = {}
        for name, body in negatives.items():
            _, words = screen.compile_candidate(self.root, self.out, 'negative-' + name, body)
            changed = 0
            for n, alias, change in itertools.product(range(4), range(3), (False, True)):
                memory, args = audit.fixture(2, n, alias)
                expected, _ = audit.reference(memory, (args[0], args[1] + 4, args[2] + 4, args[3]), change)
                model = self.model(words, memory, args, change=change, home=3)
                changed += external_memory(model.memory) != external_memory(expected)
            self.assertGreater(changed, 0, name)
            detected[name] = changed
        self.receipt('controls', dict(count=40, measurements=records, bounded_candidate_executions=720,
            negatives=detected, every_negative_changes_public_storage=True))

    def test_copied_owner_actual_padder_and_independently_rebased_call_relocations(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        baseline = source.replace(screen.SELECTED, screen.BASELINE)
        self.assertEqual(baseline.count(screen.BASELINE), 1)
        objects, warnings = [], []
        for name, body in (('baseline', baseline), ('selected', baseline.replace(screen.BASELINE, screen.SELECTED))):
            obj, diagnostic = compile_owner(self.root, self.out, body, 'owner-' + name)
            warnings.append(diagnostic)
            processed = self.out / ('owner-' + name + '-postprocessed.o')
            shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.out / ('owner-' + name + '.c')).relative_to(self.root / 'conker')), '--post-process',
                str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker', check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0], warnings[1])
        self.assertEqual(len(warnings[0]), 2)
        old_text, old_functions, old_rel = parse_object(objects[0])
        text, functions, rel = parse_object(objects[1])
        self.assertEqual(set(functions), set(old_functions))
        self.assertEqual(len(functions), 89)
        for name, current in functions.items():
            if name == screen.FUNCTION:
                continue
            old = old_functions[name]
            self.assertEqual(text[current['value']:current['value'] + current['size']], old_text[old['value']:old['value'] + old['size']], name)
            self.assertEqual({o - current['value']: r for o, r in rel.items() if current['value'] <= o < current['value'] + current['size']},
                {o - old['value']: r for o, r in old_rel.items() if old['value'] <= o < old['value'] + old['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        target = functions[screen.FUNCTION]
        isolated = parse_object(self.out / 'selected.o')[0]
        self.assertEqual(target['size'], 228)
        self.assertEqual(text[target['value']:target['value'] + 228], isolated[:228])
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        additions = screen.owner_guards()
        path = self.root / 'conker/retail_word_patches.us.csv'
        if not any(row['function'] == screen.FUNCTION for row in guards):
            path = self.out / 'proposed-guards.csv'
            with path.open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=list(guards[0]), lineterminator='\n')
                writer.writeheader(); writer.writerows([*guards, *additions])
        else:
            self.assertEqual([row for row in guards if row['function'] == screen.FUNCTION], additions)
        assembly = emit_padded_assembly(objects[1], self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=path)
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        body = assembly[start:assembly.index('\n', end) + 1]
        self.assertEqual(len(re.findall(r'\.word 0x[0-9A-F]{8}', body)), 57)
        self.assertNotIn('__retail_overflow_' + screen.FUNCTION, assembly)
        padded_source, obj, elf = (self.out / ('padded' + suffix) for suffix in ('.s', '.o', '.elf'))
        padded_source.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + body)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(padded_source)], check=True, capture_output=True)
        _, symbols, mapped = parse_object(obj)
        self.assertEqual(symbols[screen.FUNCTION]['size'], 228)
        self.assertEqual(mapped, self.record['relocations'])
        for changed in (None, *screen.SYMBOLS):
            targets = {name: address + (0x1000000 if name == changed else 0) for name, address in screen.SYMBOLS.items()}
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'point-list.ld'), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X' % item for item in targets.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = self.retail.copy()
            for offset, entries in mapped.items():
                self.assertEqual(len(entries), 1)
                kind, name = entries[0]
                self.assertEqual(kind, 'R_MIPS_26')
                expected[offset // 4] = 0x0C000000 | (targets[name] >> 2 & 0x3FFFFFF)
            self.assertEqual(list(struct.unpack_from('>57I', screen.sections(elf)['.text'][1])), expected)
        self.receipt('owner', dict(functions=89, neighbors=88, warnings=2, padded_words=57,
            guards=19, raw_owner_equals_isolated=True, pools_unchanged=True, independent_call_rebases=2))

    def test_installed_source_complete_byte_exact_linked_slot_and_guard_history(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertEqual(source.count(screen.SELECTED), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertEqual(guards[-19:], screen.owner_guards())


if __name__ == '__main__':
    unittest.main()
