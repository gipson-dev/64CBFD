"""Source-scope controls and real private-actor scale capture, not installation."""

import itertools
import json
import unittest

from tools.experiments import game_scaled_sphere_query_source_layout_candidates as screen
from tools.tests import test_game_scaled_sphere_query_recovery as recovery
from tools.tests import game_scaled_sphere_query_reference as reference
from tools.tests.game_animation_timeline_oracle import bits
from tools.tests.test_game_projection_lifetime_recovery import peek


def actor_fixture(offset=0x3C, phase=0, identity=186, layout=0, **kwargs):
    memory, args = recovery.fixture(phase=phase, identity=identity, layout=layout, **kwargs)
    actor = recovery.STACK + phase - 0x88 + offset - 0xDC
    memory.update({actor + i: memory[recovery.ACTOR + i] for i in range(0x440)})
    args = list(args)
    args[2] = actor
    if layout == 8:
        args[3] = actor + 0xDC
    return memory, args


class GameScaledSphereSourceLayoutTests(recovery.GameScaledSphereQueryRecoveryTests):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.old, cls.old_record = cls.words, cls.record
        cls.out = cls.root / 'conker/build/game-scaled-sphere-query-source-layout-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected', screen.SCALE_FIRST)
        assert cls.fixture.count(recovery.screen.SELECTED) == 1
        cls.fixture = cls.fixture.replace(recovery.screen.SELECTED, screen.SCALE_FIRST)
        assert cls.fixture.count(screen.SCALE_FIRST) == 1 and recovery.screen.SELECTED not in cls.fixture
        (cls.out / 'selected-record.json').write_text(json.dumps(cls.record, indent=2) + '\n')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def check_actor(self, memory, args, phase=0):
        snapshots, models = [], []
        for words in (self.retail, self.words):
            model = recovery.QueryOracle(words, memory, args, self.connected, phase)
            expected, writes, status, calls = reference.reference(memory, args, phase, snapshots,
                caller_saves=(model.before[16], model.before[31]))
            model.run()
            self.assertEqual(model.r[2], status)
            self.assertEqual(reference.external(model.memory), reference.external(expected))
            self.assertEqual([e for e in model.events if e[0] == 'W' and not reference.private(e[1])], writes)
            self.assertEqual(model.calls, calls)
            self.assertEqual(model.snapshots, snapshots)
            snapshots.clear()
            if words is self.retail:
                self.coverage.update(model.visits)
            models.append(model)
        return models

    def test_actor_scale_alias_counterexample_and_both_reads_before_inverse_spill(self):
        for phase in (0, 8):
            memory, args = actor_fixture(phase=phase, center=(5.0, 5.0, 0.0), radius=2,
                scale=(2.0, 0.5), direction=(10.0, 10.0, 0.0))
            frame = recovery.STACK + phase - 0x88
            original, improved = self.check_actor(memory, args, phase)
            old = recovery.QueryOracle(self.old, memory, args, self.connected, phase).run()
            for model in (original, improved, old):
                self.assertEqual(model.r[2], 1)
            for model in (original, improved):
                self.assertEqual(model.snapshots[0][1][2], bits(2.0))
                self.assertEqual(model.snapshots[0][1][15:17], (bits(-8531.0), bits(16.0)))
                self.assertEqual(tuple(peek(model.memory, pointer + 4) for pointer in args[3:5]),
                    (0x41427C98, 0xC009F25D))
                spill = next(i for i, event in enumerate(model.events) if event[:3] == ('W', frame + 0x3C, 4))
                captures = [event[1:] for event in model.events[:spill]
                    if event[0] == 'R' and event[1] in (args[2] + 0xDC, args[2] + 0xE0)]
                self.assertEqual(len(captures), 2)
                self.assertEqual(set(captures), {(args[2] + 0xDC, 4, bits(2.0)),
                    (args[2] + 0xE0, 4, bits(0.5))})
            self.assertEqual(old.snapshots[0][1][2], bits(0.5))
            self.assertEqual(tuple(peek(old.memory, pointer + 4) for pointer in args[3:5]),
                (0x409A7C98, 0xC014F92F))

    def test_private_actor_windows_preserve_the_complete_geometry_contract(self):
        count = 0
        for offset, phase, identity, layout, scale, center, direction in itertools.product(
                range(0x38, 0x80, 4), (0, 8), (186, 187), (0, 1, 8, 10), recovery.SCALES,
                ((5.0, 0.0, 0.0), (5.0, 5.0, 0.0), (-5.0, 0.0, 0.0)),
                ((10.0, 0.0, 0.0), (10.0, 10.0, 0.0), (0.0, 10.0, 0.0))):
            memory, args = actor_fixture(offset, phase, identity, layout,
                scale=scale, center=center, direction=direction)
            self.check_actor(memory, args, phase)
            count += 1
        self.assertEqual(count, 10368)

    def test_copied_owner_preserves_neighbors_but_padder_uses_overflow(self):
        self.check_copied_owner(screen.SCALE_FIRST)

    def test_zero_radius_does_not_read_removed_vectors_scales_or_points(self):
        memory, args = recovery.fixture(radius=0, height=2)
        for base, size in ((recovery.ORIGIN, 12), (recovery.DIRECTION, 12),
                (recovery.ACTOR + 0xDC, 8), (recovery.POINTS, 128)):
            for i in range(size):
                memory.pop(base + i, None)
        for model in self.check(memory, args):
            self.assertEqual(model.r[2], 0)
            self.assertEqual(len(model.calls), 1)
            self.assertEqual(model.calls[0][0], reference.DIMENSION)
            self.assertEqual(model.snapshots, [])

    def test_gate_storage_and_live_home_controls_do_not_fix_the_fit(self):
        records = []
        for name, body in screen.candidates():
            record, words = screen.compile_candidate(self.root, self.out, name, body)
            self.assertEqual(record['diagnostics'], '')
            self.assertFalse(record['exact'])
            expected = (113, 136, 76) if name in ('workspace-mask2', 'workspace-mask3', 'workspace-whole') else (
                (111, 136, 73) if name.startswith('scoped-') and name != 'scoped-tail0' else (111, 136, 72))
            self.assertEqual((record['body_words'], record['frame'], record['differences']), expected)
            if name.startswith(('volatile-', 'const-', 'same-line-')) or name in ('workspace-mask1', 'scoped-tail0'):
                self.assertEqual(words, self.old)
            if name.startswith('scoped-') and name != 'scoped-tail0':
                self.assertEqual(words[0xA0 // 4], 0x45000003)
                self.assertEqual(words[0x9C // 4], 0)
                self.assertEqual(sum(word >> 26 == 49 and word >> 21 & 31 == 8 and word & 65535 == 0xE0
                    for word in words), 1)
            record['layout'] = screen.local_layout(self.out / (name + '.o'))
            records.append(record)
        self.assertEqual(len(records), 39)
        (self.out / 'source-layout-records.json').write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    unittest.main()
