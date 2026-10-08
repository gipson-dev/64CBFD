"""Pin recovered register phases without installing an incomplete source fit."""

import itertools
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_matrix_route_branch_candidates as branch
from tools.experiments import game_matrix_route_candidates as route
from tools.experiments import game_matrix_route_layout_candidates as layout
from tools.tests import test_game_matrix_route_layout_recovery as fitted
from tools.tests import test_game_matrix_route_recovery as prior
from tools.tests.test_game_point_transform_match import external_memory


class GameMatrixRouteBranchRecoveryTests(unittest.TestCase):
    run_host = prior.GameMatrixRouteRecoveryTests.run_host
    qualify_native_candidate = prior.GameMatrixRouteRecoveryTests.qualify_native_candidate
    qualify_copied_owner = prior.GameMatrixRouteRecoveryTests.qualify_copied_owner
    check_case = fitted.GameMatrixRouteLayoutRecoveryTests.check_case

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-matrix-route-branch-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = route.compile_candidate(cls.root, cls.out, 'selected', branch.SELECTED)
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

    def test_canonical_opening_loop_and_actual_private_layout_but_missing_word(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (119, 160, 74))
        self.assertEqual((self.record['pool_bytes'], self.record['diagnostics']), (0, ''))
        self.assertEqual(self.words[:17], self.retail[:17])
        self.assertEqual(self.words[0x168//4:0x1A8//4], self.retail[0x16C//4:0x1AC//4])
        self.assertEqual(self.words[-8:], self.retail[-8:])
        self.assertEqual(layout.private_offsets(self.words), dict(primary_offset=144, secondary_offset=140, matrix_offset=76))
        self.assertEqual(self.words[0x144//4:0x154//4], self.retail[0x148//4:0x158//4])
        self.receipt('slot', dict(body_words=119, retail_words=120, frame=160, differences=74,
            opening_exact_words=17, shifted_loop_exact_words=16, epilogue_exact_words=8,
            matrix_carrier='A1', actor_and_output_cursor='S2', node_and_input_cursor='S1',
            private_offsets=layout.private_offsets(self.words), candidate_installed=False,
            missing_word_not_replaced_by_alignment_nop=True, guards_added=0))

    def test_all_ninety_two_controls_compile_and_ordinary_effects_qualify(self):
        forms = [(name, body) for group in (branch.candidates, branch.phase_candidates,
            branch.key_candidates, branch.storage_candidates, branch.flow_candidates) for name, body in group()]
        self.assertEqual(len(forms), 92)
        self.assertEqual(len({name for name, _ in forms}), 92)
        records, executions = [], 0
        for name, body in forms:
            record, words = route.compile_candidate(self.root, self.out, name, body)
            self.assertGreater(record['differences'], 0)
            record.update(layout.private_offsets(words))
            record['debug'] = layout.debug_locals(self.out / (name + '.o'))
            for r, count in itertools.product(range(8), (-1, 0, 2)):
                memory, args = prior.fixture(r, count)
                expected, calls, result = prior.reference(memory, args)
                model = prior.MatrixRouteOracle(words, memory, args).run()
                self.assertEqual((external_memory(model.memory), model.calls, model.r[2]),
                    (external_memory(expected), calls, result), name)
                executions += 1
            records.append(record)
        self.receipt('controls', dict(count=92, executions=executions, exact=0, measurements=records,
            previous_controls=285, total_controls=377, ordinary_effects_only_for_all_forms=True,
            volatile_controls_not_original_source_evidence=True))

    def test_selected_all_routes_public_traces_homes_and_attachment_reread(self):
        fitted.GameMatrixRouteLayoutRecoveryTests.test_ordinary_public_traces_all_routes_homes_and_callback_attachment_reread(self)

    def test_selected_original_helpers_and_actual_private_arguments(self):
        fitted.GameMatrixRouteLayoutRecoveryTests.test_connected_actual_helpers_private_arguments_and_public_trace(self)

    def test_selected_closes_old_private_matrix_counterexamples(self):
        fitted.GameMatrixRouteLayoutRecoveryTests.test_old_sixteen_private_matrix_output_counterexamples_now_agree(self)

    def test_selected_additional_private_source_destination_and_resolver_overlaps(self):
        fitted.GameMatrixRouteLayoutRecoveryTests.test_additional_matrix_source_destination_and_resolver_output_overlaps(self)

    def test_selected_lazy_gates_faults_and_guest_wrapping_indices(self):
        prior.GameMatrixRouteRecoveryTests.test_lazy_gates_required_storage_and_unclamped_index(self)

    def test_selected_native_complete_C_actual_SDK_32bit(self):
        self.qualify_native_candidate(branch.SELECTED)

    def test_selected_copied_owner_neighbor_pool_and_warning_isolation(self):
        self.qualify_copied_owner(branch.SELECTED)
