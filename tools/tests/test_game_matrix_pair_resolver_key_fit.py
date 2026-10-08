"""Qualified bank pointer-addition phase; the missing key move stays explicit."""

import csv
import itertools
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_matrix_pair_resolver_candidates as pair
from tools.experiments import game_matrix_pair_resolver_key_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.game_owner_pool import assert_guard_history


class GameMatrixPairResolverKeyFitTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host
    receipt = prior.GameMatrixPairResolverRecoveryTests.receipt
    compare = prior.GameMatrixPairResolverRecoveryTests.compare
    qualify_native_candidate = prior.GameMatrixPairResolverRecoveryTests.qualify_native_candidate
    test_all_routes_full_returns_public_reads_writes_and_recursion_coverage = (
        prior.GameMatrixPairResolverRecoveryTests.test_all_routes_full_returns_public_reads_writes_and_recursion_coverage)
    test_output_aliases_fields_page_and_each_other_preserve_store_order = (
        prior.GameMatrixPairResolverRecoveryTests.test_output_aliases_fields_page_and_each_other_preserve_store_order)
    test_original_lookup_connection_and_incoming_actor_secondary_home_mutations = (
        prior.GameMatrixPairResolverRecoveryTests.test_original_lookup_connection_and_incoming_actor_secondary_home_mutations)
    test_lazy_failed_routes_required_storage_and_unclamped_word_address_wrap = (
        prior.GameMatrixPairResolverRecoveryTests.test_lazy_failed_routes_required_storage_and_unclamped_word_address_wrap)
    test_actual_matrix_wrapper_connection_and_recursive_resolver_paths = (
        prior.GameMatrixPairResolverRecoveryTests.test_actual_matrix_wrapper_connection_and_recursive_resolver_paths)
    test_real_padder_preserves_complete_body_and_self_call_symbol_relocations = (
        prior.GameMatrixPairResolverRecoveryTests.test_real_padder_preserves_complete_body_and_self_call_symbol_relocations)

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-matrix-pair-key-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = pair.compile_candidate(cls.root, cls.out, 'selected', screen.SELECTED)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>85I', rom, pair.ROM))
        cls.lookup = dict(zip(range(prior.LOOKUP, prior.LOOKUP+28*4, 4), struct.unpack_from('>28I', rom, 0x5EE0C)))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def qualify_owner(self, candidate=screen.SELECTED):
        return prior.GameMatrixPairResolverRecoveryTests.qualify_owner(self, candidate)

    def test_canonical_node_bank_phase_and_still_missing_key_move(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (84, 32, 40))
        self.assertEqual((self.record['pool_bytes'], self.record['diagnostics']), (0, ''))
        self.assertEqual(self.words[:15], self.retail[:15])
        self.assertEqual(self.words[37:42], self.retail[37:42])
        self.assertEqual(self.words[-5:], self.retail[-5:])
        self.assertEqual(self.words[44], 0x9625001E)
        self.assertEqual(self.retail[44], 0x9622001E)
        self.assertEqual(self.retail[48], 0x00402825)
        self.assertNotIn(0x00402825, self.words)
        _, typed = pair.compile_candidate(self.root, self.out, 'typed-node-control', screen.NODE_SELECTED)
        self.assertEqual(self.words, typed)
        self.receipt('slot', dict(body_words=84, slot_words=85, frame=32, differences=40,
            node_bank_GP_cycle_directly_exact=True, complete_C=True, guards_added=0,
            key_A1_in_C_V0_then_A1_in_retail=True, missing_meaningful_word=True))

    def test_eighty_six_source_controls_ordinary_contract_without_claiming_all_aliases(self):
        forms = list(screen.candidates())
        self.assertEqual(len(forms), 86)
        records, executions = [], 0
        for name, body, declaration in forms:
            record, words = pair.compile_candidate(self.root, self.out, name, body, lookup_declaration=declaration)
            self.assertGreater(record['differences'], 0)
            self.assertEqual((record['pool_bytes'], record['diagnostics']), (0, ''))
            for kind, page, phase in itertools.product(range(8), range(2), (0, 8)):
                memory, args = prior.fixture(kind, page)
                reference = prior.PairReference(memory, phase)
                expected = reference.run(*args)
                model = prior.PairOracle(words, memory, args, phase).run()
                self.assertEqual((prior.external_memory(model.memory), model.calls, model.r[2]),
                    (prior.external_memory(reference.memory), reference.calls, expected), name)
                executions += 1
            records.append(record)
        self.receipt('controls', dict(forms=86, ordinary_executions=executions, exact=0,
            measurements=records, total_forms_with_previous=155,
            alias_home_fault_and_private_contract_not_claimed_for_all_controls=True))

    def test_native_complete_C_and_four_byte_typed_control_layout(self):
        checks = r'''
#define FIELD_OFFSET(field) __builtin_offsetof(MatrixPairNode,field)
typedef char node_layout[(sizeof(MatrixPairNode)==0x4C&&FIELD_OFFSET(slot)==2&&
    FIELD_OFFSET(key)==0x1E&&FIELD_OFFSET(offset)==0x20&&FIELD_OFFSET(bank)==0x34&&
    FIELD_OFFSET(attachment)==0x48)?1:-1];
'''
        self.qualify_native_candidate(screen.NODE_VIEW+screen.SELECTED+checks)

    def test_copied_owner_no_changed_neighbors_pools_relocations_or_warnings(self):
        self.qualify_owner(screen.SELECTED)

    def test_installed_variant_explicit_and_previous_guards_intact(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        installed = screen.SELECTED in source
        self.assertEqual(source.count(screen.SELECTED), int(installed))
        body = screen.SELECTED if installed else pair.SELECTED
        _, expected = pair.compile_candidate(self.root, self.out, 'installed-current', body)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
            'mips-linux-gnu-objdump')
        self.assertEqual((addresses[pair.FUNCTION], functions[pair.FUNCTION]), (pair.ENTRY, expected+[0]))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == pair.FUNCTION for row in guards))
        self.receipt('installed', dict(bank_phase_C_installed=installed, body_words=84, slot_words=85,
            frame=32, differences=sum(a != b for a, b in zip(expected+[0], self.retail)), guards_added=0))


if __name__ == '__main__':
    unittest.main()
