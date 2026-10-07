"""Retain the recovered real frame and ABI while keeping branch fitting open."""

import csv
import itertools
import json
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_matrix_route_layout_candidates as fit
from tools.experiments import game_matrix_route_candidates as route
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_matrix_route_recovery as prior
from tools.tests.test_game_point_transform_match import external_memory, put
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests.game_owner_pool import assert_guard_history


class GameMatrixRouteLayoutRecoveryTests(unittest.TestCase):
    run_host = prior.GameMatrixRouteRecoveryTests.run_host
    qualify_native_candidate = prior.GameMatrixRouteRecoveryTests.qualify_native_candidate
    qualify_copied_owner = prior.GameMatrixRouteRecoveryTests.qualify_copied_owner

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-matrix-route-layout-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = route.compile_candidate(cls.root, cls.out, 'selected', fit.SELECTED)
        cls.old_record, cls.old_words = route.compile_candidate(cls.root, cls.out, 'old-selected', route.SELECTED)
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>120I', cls.rom, route.ROM))
        cls.connected = {}
        for entry, offset, length in ((prior.LOOKUP, 0x5EE0C, 28), (prior.RESOLVE, 0x5E520, 85),
                (prior.CONVERT, 0x21D368, 46), (prior.POINT, 0xD4E10, 40), (prior.LIST, 0x173354, 117),
                (prior.matrix_list.TRANSLATE, 0x16F7C4, 49)):
            cls.connected.update(zip(range(entry, entry + length * 4, 4),
                struct.unpack_from('>%dI' % length, cls.rom, offset)))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def check_case(self, memory, args, **kwargs):
        expected, calls, result = prior.reference(memory, args,
            **{k: v for k, v in kwargs.items() if k in ('phase', 'home', 'mutate')})
        models = [prior.MatrixRouteOracle(words, memory, args, **kwargs).run()
            for words in (self.words, self.retail)]
        for model in models:
            self.assertEqual((external_memory(model.memory), model.calls, model.r[2]),
                (external_memory(expected), calls, result))
        self.assertEqual(models[0].private_matrices, models[1].private_matrices)
        self.assertEqual(models[0].private_outputs, models[1].private_outputs)
        public = lambda model: [e for e in model.events if not prior.STACK-0x600 <= e[1] < prior.STACK+0x140]
        self.assertEqual(public(models[0]), public(models[1]))
        return models

    def test_full_body_frame_real_private_offsets_and_not_yet_matching(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (120, 0xA0, 60))
        self.assertEqual((self.record['pool_bytes'], self.record['diagnostics']), (0, ''))
        self.assertEqual(fit.private_offsets(self.words), dict(primary_offset=0x90, secondary_offset=0x8C, matrix_offset=0x4C))
        layout = fit.debug_locals(self.out / 'selected.o')
        self.assertEqual(layout['frame'], 0xA0)
        self.assertEqual({k: layout['locals'][k]['value'] for k in ('converted', 'lookupMatrix', 'other')},
            dict(converted=-84, lookupMatrix=-16, other=-20))
        self.assertEqual(self.words[0], self.retail[0])
        self.assertEqual(self.words[-8:], self.retail[-8:])
        self.assertEqual(len(self.words), len(self.retail))
        self.assertNotEqual(self.words, self.retail)
        self.receipt('slot', dict(words=120, frame=160, differences=60,
            private_offsets=fit.private_offsets(self.words), debug=layout, actual_complete_body=True,
            alignment_nop_not_counted=True, guards_added=0, raw_exact=False))

    def test_ordinary_public_traces_all_routes_homes_and_callback_attachment_reread(self):
        cases = 0
        for r, count, page, index, alias, phase in itertools.product(range(8), prior.COUNTS,
                (0, 1), (-1, 0, 2), range(3), (0, 8)):
            memory, args = prior.fixture(r, count, page, index, alias)
            self.check_case(memory, args, phase=phase)
            cases += 1
        homes = 0
        for r, count, home, phase in itertools.product(range(4), prior.COUNTS, range(1, 8), (0, 8)):
            memory, args = prior.fixture(r, count)
            self.check_case(memory, args, phase=phase, home=home)
            homes += 1
        mutations = 0
        for r, count, phase in itertools.product((1, 2), prior.COUNTS, (0, 8)):
            memory, args = prior.fixture(r, count)
            self.check_case(memory, args, phase=phase, mutate=True)
            mutations += 1
        self.receipt('guest', dict(cases=cases, homes=homes, attachment_rereads=mutations,
            actual_private_argument_addresses=True, public_reads_writes_and_calls=True,
            full_return_word=True, caller_saved_GP_FP_clobbered=True, full_stack_memory_not_claimed=True))

    def test_connected_actual_helpers_private_arguments_and_public_trace(self):
        cases = 0
        for r, count, page, index, alias, phase in itertools.product(range(8), (-1, 0, 2),
                (0, 1), (-1, 0, 2), range(3), (0, 8)):
            memory, args = prior.fixture(r, count, page, index, alias)
            self.check_case(memory, args, phase=phase, connected=self.connected)
            cases += 1
        self.receipt('connected', dict(cases=cases, original_instructions=True,
            private_argument_addresses_equal=True, public_trace_equal=True,
            complete_callee_coverage=False, full_stack_memory_not_claimed=True))

    def test_old_sixteen_private_matrix_output_counterexamples_now_agree(self):
        cases, old_differences = 0, 0
        for offset, count, phase in itertools.product((0, 16, 32, 48), (1, 2), (0, 8)):
            memory, args = prior.fixture(count=count)
            for i in range(count):
                put(memory, prior.INPUT+i*4, prior.STACK+phase-0xA0+0x4C+offset)
            models = [prior.MatrixRouteOracle(words, memory, args, phase=phase, connected=self.connected).run()
                for words in (self.old_words, self.words, self.retail)]
            old_differences += external_memory(models[0].memory) != external_memory(models[2].memory)
            self.assertEqual(external_memory(models[1].memory), external_memory(models[2].memory))
            self.assertEqual(models[1].calls, models[2].calls)
            self.assertEqual(models[1].private_matrices, models[2].private_matrices)
            cases += 1
        self.assertEqual((cases, old_differences), (16, 16))
        self.receipt('old-overlaps', dict(cases=16, old_output_differences=16,
            new_output_differences=0, actual_original_helpers=True, no_offset_normalization=True))

    def test_additional_matrix_source_destination_and_resolver_output_overlaps(self):
        cases = 0
        for r, source_offset, output_offset, count, phase in itertools.product((0, 1, 2, 3),
                (None, 0, 16, 32, 48, 64, 68), (None, 0, 16, 32, 48), (0, 2), (0, 8)):
            memory, args = prior.fixture(r, count)
            base = prior.STACK+phase-0xA0+0x4C
            for i in range(count):
                if source_offset is not None:
                    put(memory, prior.INPUT+i*4, base+source_offset)
                if output_offset is not None:
                    put(memory, prior.OUTPUT+i*4, base+output_offset)
            models = [prior.MatrixRouteOracle(words, memory, args, phase=phase, connected=self.connected).run()
                for words in (self.words, self.retail)]
            self.assertEqual(external_memory(models[0].memory), external_memory(models[1].memory))
            self.assertEqual(models[0].calls, models[1].calls)
            self.assertEqual(models[0].private_matrices, models[1].private_matrices)
            self.assertEqual(models[0].private_outputs, models[1].private_outputs)
            cases += 1
        self.receipt('private', dict(cases=cases, matrix_source_destination_and_primary_secondary_aliases=True,
            actual_original_helpers=True, public_outputs_and_calls_equal=True,
            full_stack_memory_not_claimed=True, no_offset_patch=True))

    def test_new_source_controls_no_instruction_guard_and_no_exact_fit(self):
        forms = [(n, b) for group in (fit.topology_candidates, fit.storage_candidates,
            fit.parameter_candidates, fit.indexed_candidates, fit.pointer_phase_candidates,
            fit.output_phase_candidates) for n, b in group()]
        self.assertEqual(len(forms), 77)
        records, executions = [], 0
        for name, body in forms:
            record, words = route.compile_candidate(self.root, self.out, name, body)
            self.assertGreater(record['differences'], 0)
            record.update(fit.private_offsets(words))
            record['debug'] = fit.debug_locals(self.out / (name+'.o'))
            for r, count in itertools.product(range(8), (-1, 0, 2)):
                memory, args = prior.fixture(r, count)
                expected, calls, result = prior.reference(memory, args)
                model = prior.MatrixRouteOracle(words, memory, args).run()
                self.assertEqual((external_memory(model.memory), model.calls, model.r[2]),
                    (external_memory(expected), calls, result), name)
                executions += 1
            records.append(record)
        self.receipt('controls', dict(count=len(forms), executions=executions, exact=0,
            measurements=records, original_corpus=208, total_controls=285,
            private_and_home_equivalence_not_claimed_for_all_controls=True))

    def test_native_complete_candidate_32bit_actual_sdk(self):
        self.qualify_native_candidate(fit.SELECTED)

    def test_copied_owner_only_target_changes_pools_and_warning_statements_unchanged(self):
        self.qualify_copied_owner(fit.SELECTED)

    def test_lazy_gates_required_storage_and_wrapping_index_contract(self):
        prior.GameMatrixRouteRecoveryTests.test_lazy_gates_required_storage_and_unclamped_index(self)

    def test_compiled_semantic_negatives_detect_actual_public_outputs(self):
        negatives = dict(wrong_flag=fit.SELECTED.replace('attachment[0x3F6] == 0', 'attachment[0x3F6] != 0'),
            wrong_page=fit.SELECTED.replace('[D_800BE9C0]', '[0]'),
            wrong_index=fit.SELECTED.replace(' + index;', ' + 0;'),
            wrong_key=fit.SELECTED.replace('actor, *(u16 *)(descriptor + 0x1E), 0', 'actor, 38, 0'),
            wrong_count=fit.SELECTED.replace('count > 0', 'count == 1'),
            wrong_stride=fit.SELECTED.replace('input++;', 'input += 2;'))
        detected = {}
        for name, body in negatives.items():
            self.assertNotEqual(body, fit.SELECTED)
            _, words = route.compile_candidate(self.root, self.out, 'negative-'+name, body)
            differences = 0
            for r in range(4):
                memory, args = prior.fixture(r, 2, 1, 2)
                expected, _, result = prior.reference(memory, args)
                model = prior.MatrixRouteOracle(words, memory, args).run()
                differences += (external_memory(model.memory), model.r[2]) != (external_memory(expected), result)
            self.assertGreater(differences, 0, name)
            detected[name] = differences
        self.receipt('negatives', dict(actual_output_detections=detected, unexpected_fault_not_accepted=True))

    def test_actual_padder_preserves_raw_body_and_all_relocations_without_new_guards(self):
        self.qualify_copied_owner(fit.SELECTED)
        owner = self.out / 'owner-selected-postprocessed.o'
        assembly = emit_padded_assembly(owner, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=self.root / 'conker/retail_word_patches.us.csv')
        start = assembly.index('.type %s, @function' % route.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (route.FUNCTION, route.FUNCTION), start)
        end = assembly.index('\n', end)+1
        asm, obj = self.out / 'padded.s', self.out / 'padded.o'
        asm.write_text('.text\n.globl %s\n' % route.FUNCTION+assembly[start:end])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(asm)], check=True, capture_output=True)
        _, functions, relocs = parse_object(obj)
        self.assertEqual(functions[route.FUNCTION]['size'], 480)
        self.assertEqual(relocs, parse_object(self.out / 'selected.o')[2])
        self.assertEqual(len(relocs), 9)
        for rebased in (None, *route.SYMBOLS):
            targets = dict(route.SYMBOLS)
            if rebased:
                targets[rebased] += 0x01008004
            elf = self.out / ('rebased-%s.elf' % rebased)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'matrix-route.ld'),
                '-e', route.FUNCTION, *['--defsym=%s=0x%X' % item for item in targets.items()],
                '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = list(self.words)
            for offset, entries in relocs.items():
                kind, name = entries[0]
                address = targets[name]
                expected[offset//4] = (expected[offset//4] & 0xFC000000 | address >> 2 & 0x3FFFFFF) if kind == 'R_MIPS_26' else (
                    expected[offset//4] & 0xFFFF0000 | ((address+0x8000) >> 16 & 65535 if kind == 'R_MIPS_HI16' else address & 65535))
            self.assertEqual(list(struct.unpack_from('>120I', route.sections(elf)['.text'][1])), expected)
        self.receipt('padder', dict(words=120, relocations=9, independent_symbols=6,
            guards_added=0, insertions=0, omissions=0, preserves_raw_nonmatching_body=True))

    def test_installed_complete_nonmatching_body_and_previous_guard_history(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertEqual(source.count(fit.SELECTED), 1)
        self.assertEqual(source.count(route.PROTOTYPE), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual((addresses[route.FUNCTION], functions[route.FUNCTION]), (route.ENTRY, self.words))
        self.assertEqual(sum(a != b for a, b in zip(functions[route.FUNCTION], self.retail)), 60)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == route.FUNCTION for row in guards))
        self.receipt('installed', dict(words=120, frame=160, differences=60, complete_C=True,
            exact=False, guards_added=0, incoming_ABI_words=6))
