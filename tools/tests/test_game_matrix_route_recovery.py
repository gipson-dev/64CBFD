"""Four routing paths, lazy ABI homes and the still-open private-frame boundary."""

import csv
import itertools
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_matrix_route_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_matrix_list_transform_match as matrix_list
from tools.tests import test_game_point_list_transform_audit as points
from tools.tests import test_game_random_curve_record as native
from tools.tests.game_animation_timeline_oracle import bits, signed
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read, external_memory

LOOKUP, RESOLVE, LIST, CONVERT, POINT, PAGE = screen.SYMBOLS.values()
ACTOR, DESCRIPTOR, ATTACHMENT, NODE = 0x10000, 0x11000, 0x12000, 0x13000
INPUT, OUTPUT, SOURCES, RESULTS, ALTERNATE = 0x20000, 0x21000, 0x22000, 0x23000, 0x24000
BANK, SECONDARY, DESCRIPTOR_BANK = 0x28000, 0x2A000, 0x2C000
HEAD, STACK = 0x800C3EE0, points.STACK
COUNTS = (-0x80000000, -1, 0, 1, 2, 4)


def fixture(route=0, count=2, page=0, index=0, alias=0, pattern=0):
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x140)}
    for base, size in ((ACTOR, 0x200), (DESCRIPTOR, 0x60), (ATTACHMENT, 0x410),
            (NODE, 0x60), (INPUT, 32), (OUTPUT, 32), (SOURCES, 108), (RESULTS, 108),
            (ALTERNATE, 108), (BANK - 64, 512), (SECONDARY, 512), (DESCRIPTOR_BANK, 512)):
        memory.update({base + i: 0 for i in range(size)})
    put(memory, ACTOR + 0x1D4, BANK)
    put(memory, ACTOR + 0x3B, 3, 1)
    put(memory, PAGE, page, 1)
    put(memory, matrix_list.FLAG, 1, 1)
    put(memory, HEAD, NODE)
    put(memory, NODE, 3, 1)
    put(memory, NODE + 6, 37, 1)
    put(memory, NODE + 0x54, 0)
    put(memory, DESCRIPTOR + 2, 2, 1)
    put(memory, DESCRIPTOR + 0x20, 1, 2)
    put(memory, ATTACHMENT + 0x3F6, 1, 1)
    for matrix_page in range(2):
        put(memory, ATTACHMENT + 0x3E8 + matrix_page * 4, BANK + matrix_page * 64)
        put(memory, ATTACHMENT + 0x3E0 + matrix_page * 4, SECONDARY + matrix_page * 64)
    # 0 attachment, 1 resolved attachment, 2 resolved bank, 3 descriptor bank,
    # 4 delegated actor bank, 5 null selected matrix, 6 lookup fail, 7 resolve fail.
    if route in (0, 5):
        put(memory, DESCRIPTOR + 0x48, ATTACHMENT)
        if route == 5:
            put(memory, ATTACHMENT + 0x3E8 + page * 4, 0)
            index = 0
    elif route in (1, 2, 6, 7):
        put(memory, DESCRIPTOR + 0x1E, 37, 2)
        put(memory, NODE + 0x48, ATTACHMENT if route in (1, 7) else 0)
        put(memory, NODE + 0x34, DESCRIPTOR_BANK if route == 2 else 0)
        if route == 6:
            put(memory, NODE + 6, 38, 1)
        if route == 7:
            put(memory, ATTACHMENT + 0x3F6, 0, 1)
    elif route == 3:
        put(memory, DESCRIPTOR + 0x34, DESCRIPTOR_BANK)
    for base in (BANK - 64, BANK, BANK + 64, BANK + 128, BANK + 192,
            DESCRIPTOR_BANK, DESCRIPTOR_BANK + page * 64):
        values = [((i * 7 + pattern * 3 + (base - BANK) // 64 * 5) % 17 - 8) / 8 for i in range(16)]
        for i, value in enumerate(values):
            integer = int(value * 65536) & 0xFFFFFFFF
            put(memory, base + i * 2, integer >> 16, 2)
            put(memory, base + 32 + i * 2, integer, 2)
    for i in range(8):
        put(memory, INPUT + i * 4, SOURCES + i * 12)
        put(memory, OUTPUT + i * 4, (RESULTS + i * 12, SOURCES + i * 12,
            SOURCES + (i + 1) * 12)[alias])
        for axis in range(3):
            value = (-3.5, 0.0, 2.25, -0.0, 8.0, 0.5)[(pattern + i * 3 + axis) % 6]
            put(memory, SOURCES + i * 12 + axis * 4, bits(value))
            put(memory, ALTERNATE + i * 12 + axis * 4, bits(axis + i + 7.0))
    return memory, (ACTOR, DESCRIPTOR, index & 0xFFFFFFFF, INPUT, OUTPUT, count & 0xFFFFFFFF)


def lookup(memory, actor, key, ordinal=0):
    slot = read(memory, actor + 0x3B, 1)
    if not slot:
        return 0
    node = read(memory, HEAD)
    while node:
        if read(memory, node, 1) == slot and read(memory, node + 6, 1) == key:
            if ordinal == 0:
                return node
            ordinal -= 1
        node = read(memory, node + 0x54)
    return 0


def resolve(memory, node, actor, depth=0):
    assert depth < 4, 'fixture resolver recursion bound'
    attachment = read(memory, node + 0x48)
    if attachment:
        if not read(memory, attachment + 0x3F6, 1):
            return None
        page = read(memory, PAGE, 1)
        return (read(memory, attachment + 0x3E8 + page * 4),
            read(memory, attachment + 0x3E0 + page * 4))
    bank = read(memory, node + 0x34)
    actor_bank = read(memory, actor + 0x1D4)
    if bank:
        return bank + read(memory, PAGE, 1) * 64, actor_bank + read(memory, node + 2, 1) * 64
    key = read(memory, node + 0x1E, 2)
    if key:
        parent = lookup(memory, actor, key)
        result = resolve(memory, parent, actor, depth + 1) if parent else None
        return (result[0] + read(memory, node + 0x20, 2) * 64, result[1]) if result else None
    selected = actor_bank + read(memory, node + 2, 1) * 64
    return selected, selected


def change_homes(memory, args, phase, home):
    for mask, address, value in ((1, STACK + phase + 12, INPUT + 4),
            (2, STACK + phase + 16, OUTPUT + 4), (4, STACK + phase + 20, 1)):
        if home & mask:
            put(memory, address, value)


def reference(memory, args, phase=0, home=0, mutate=False):
    memory, calls = dict(memory), []
    actor, descriptor, index, inputs, outputs, count = args
    if not actor or not descriptor or not read(memory, actor + 0x1D4):
        return memory, calls, 0
    bank, attachment = read(memory, actor + 0x1D4), read(memory, descriptor + 0x48)
    if attachment:
        if not read(memory, attachment + 0x3F6, 1):
            return memory, calls, 0
        selected = (read(memory, attachment + 0x3E8 + read(memory, PAGE, 1) * 4) + index * 64) & 0xFFFFFFFF
    elif read(memory, descriptor + 0x1E, 2):
        key = read(memory, descriptor + 0x1E, 2)
        calls.append((LOOKUP, actor, key, 0))
        node = lookup(memory, actor, key)
        if not node:
            return memory, calls, 0
        calls.append((RESOLVE, node, actor))
        result = resolve(memory, node, actor)
        if result is None:
            return memory, calls, 0
        if mutate:
            put(memory, node + 0x48, 0 if read(memory, node + 0x48) else ATTACHMENT)
        selected = result[0]
        if read(memory, node + 0x48):
            selected += read(memory, descriptor + 0x20, 2) * 64
    elif read(memory, descriptor + 0x34):
        selected = read(memory, descriptor + 0x34) + read(memory, PAGE, 1) * 64
    else:
        selected = bank + read(memory, descriptor + 2, 1) * 64
        calls.append((LIST, inputs, outputs, selected, count))
        memory, nested = matrix_list.reference(memory, (inputs, outputs, selected, count), phase=phase - 0xA0)
        return memory, calls + nested, 1
    if not selected:
        return memory, calls, 0
    private = STACK + phase - 0xA0 + 0x4C
    calls.append((CONVERT, selected))
    matrix_list.convert(memory, private, selected)
    change_homes(memory, args, phase, home)
    inputs = INPUT + 4 if home & 1 else inputs
    outputs = OUTPUT + 4 if home & 2 else outputs
    count = 1 if home & 4 else signed(count)
    for i in range(max(0, count)):
        source, destination = read(memory, inputs + i * 4), read(memory, outputs + i * 4)
        values = tuple(read(memory, private + j * 4) for j in range(16))
        coordinates = tuple(read(memory, source + axis * 4) for axis in range(3))
        addresses = tuple(destination + axis * 4 for axis in range(3))
        calls.append((POINT, values, coordinates, addresses))
        for address, value in zip(addresses, points.transformed(values, coordinates)):
            put(memory, address, value)
    return memory, calls, 1


class MatrixRouteOracle(TriangleOracle):
    def __init__(self, words, memory, args, phase=0, home=0, mutate=False, connected=None):
        super().__init__(words, memory, entry=screen.ENTRY, arguments=args, phase=phase, connected=connected)
        self.args, self.phase, self.home, self.mutate = args, phase, home, mutate
        self.private_outputs, self.private_matrices = [], []

    def record_call(self, target):
        if target == LOOKUP:
            self.calls.append((target, *self.arguments(3)))
        elif target == RESOLVE:
            node, actor, primary, other = self.arguments(4)
            self.private_outputs.append((primary, other))
            self.calls.append((target, node, actor))
        elif target == LIST:
            self.calls.append((target, *self.arguments(4)))
        elif target == CONVERT:
            destination, source = self.arguments(2)
            self.private_matrices.append(destination)
            self.calls.append((target, source))
        elif target == POINT:
            matrix, x, y, z, *outputs = self.arguments(7)
            assert outputs[1] == outputs[0] + 4 and outputs[2] == outputs[0] + 8
            self.calls.append((target, tuple(read(self.memory, matrix + i * 4) for i in range(16)),
                (x, y, z), tuple(outputs)))
        else:
            assert target == matrix_list.TRANSLATE
            self.calls.append((target, *self.arguments(3)))

    def hook(self, target):
        result = 0
        if target == LOOKUP:
            result = lookup(self.memory, *self.arguments(3))
        elif target == RESOLVE:
            node, actor, primary, other = self.arguments(4)
            resolved = resolve(self.memory, node, actor)
            if resolved is not None:
                self.put(primary, resolved[0], 4)
                self.put(other, resolved[1], 4)
                result = 1
                if self.mutate:
                    self.put(node + 0x48, 0 if self.get(node + 0x48, 4) else ATTACHMENT, 4)
        elif target == CONVERT:
            destination, source = self.arguments(2)
            changed = dict(self.memory)
            matrix_list.convert(changed, destination, source)
            change_homes(changed, self.args, self.phase, self.home)
            for address, value in changed.items():
                if value != self.memory.get(address):
                    self.put(address, value, 1)
        elif target == POINT:
            _, values, coordinates, outputs = self.calls[-1]
            for address, value in zip(outputs, points.transformed(values, coordinates)):
                self.put(address, value, 4)
        elif target == LIST:
            args = self.arguments(4)
            changed, nested = matrix_list.reference(self.memory, args, phase=self.phase - 0xA0)
            self.calls.extend(nested)
            for address, value in changed.items():
                if value != self.memory.get(address):
                    self.put(address, value, 1)
        else:
            assert target == matrix_list.TRANSLATE
            changed, _ = matrix_list.translation.reference(self.memory, self.arguments(3))
            for address, value in changed.items():
                if value != self.memory.get(address):
                    self.put(address, value, 1)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.r[2] = result


class GameMatrixRouteRecoveryTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-matrix-route-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected', screen.SELECTED)
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>120I', cls.rom, screen.ROM))
        cls.connected = {}
        for entry, offset, length in ((LOOKUP, 0x5EE0C, 28), (RESOLVE, 0x5E520, 85),
                (CONVERT, 0x21D368, 46), (POINT, 0xD4E10, 40), (LIST, 0x173354, 117),
                (matrix_list.TRANSLATE, 0x16F7C4, 49)):
            cls.connected.update(zip(range(entry, entry + length * 4, 4),
                struct.unpack_from('>%dI' % length, cls.rom, offset)))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def check_case(self, memory, args, **kwargs):
        expected, calls, result = reference(memory, args,
            **{k: v for k, v in kwargs.items() if k in ('phase', 'home', 'mutate')})
        models = [MatrixRouteOracle(words, memory, args, **kwargs).run() for words in (self.words, self.retail)]
        for model in models:
            self.assertEqual(external_memory(model.memory), external_memory(expected))
            self.assertEqual(model.r[2], result)
            self.assertEqual(model.calls, calls)
        return models

    def test_complete_source_still_open_and_installed_placeholder_unchanged(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (119, 0xA8, 58))
        self.assertEqual((self.record['pool_bytes'], self.record['diagnostics']), (0, ''))
        self.assertEqual(self.words[0], 0x27BDFF58)
        self.assertIn(0x27B40068, self.words)
        self.assertIn(0x27B4004C, self.retail)
        self.assertEqual(self.words[1:9], self.retail[1:9])
        self.assertEqual(self.words[0x16C//4:0x1AC//4], self.retail[0x16C//4:0x1AC//4])
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], [0x00001025, 0x03E00008, 0] + [0] * 117)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn('s32 func_1514654C() {\n    return 0;\n}', source)
        self.receipt('slot', dict(retail_words=120, candidate_words=119, retail_frame=160,
            candidate_frame=168, differences=58, raw_exact=False, original_is_reference_only=True,
            installed_placeholder_body_words=3,
            candidate_installed=False, guards_added=0, matrix_private_offsets=[104, 76]))

    def test_all_four_routes_failures_signed_counts_aliases_and_home_mutation(self):
        cases, coverage = 0, [set(), set()]
        for route, count, page, index, alias, pattern, phase in itertools.product(range(8), COUNTS,
                (0, 1), (-1, 0, 2), range(3), range(4), (0, 8)):
            memory, args = fixture(route, count, page, index, alias, pattern)
            for covered, model in zip(coverage, self.check_case(memory, args, phase=phase)):
                covered.update(model.visits)
            cases += 1
        for gate in ('actor', 'descriptor', 'actor_bank', 'attachment_flag'):
            memory, args = fixture()
            if gate == 'actor':
                args = (0, *args[1:])
            elif gate == 'descriptor':
                args = (args[0], 0, *args[2:])
            else:
                put(memory, ACTOR + 0x1D4 if gate == 'actor_bank' else ATTACHMENT + 0x3F6,
                    0, 4 if gate == 'actor_bank' else 1)
            for covered, model in zip(coverage, self.check_case(memory, args)):
                covered.update(model.visits)
            cases += 1
        homes = 0
        for route, count, home, phase in itertools.product(range(4), COUNTS, range(1, 8), (0, 8)):
            memory, args = fixture(route, count)
            self.check_case(memory, args, phase=phase, home=home)
            homes += 1
        mutation = 0
        for route, count, phase in itertools.product((1, 2), COUNTS, (0, 8)):
            memory, args = fixture(route, count)
            self.check_case(memory, args, phase=phase, mutate=True)
            mutation += 1
        for covered, words, unreachable in zip(coverage, (self.words, self.retail),
                ((0x4C, 0x8C, 0xD8, 0x100, 0x124), (0x4C, 0x8C, 0xD8, 0x128))):
            self.assertEqual(set(range(screen.ENTRY, screen.ENTRY + len(words) * 4, 4)) - covered,
                {screen.ENTRY + offset for offset in unreachable})
        self.receipt('guest', dict(cases=cases, home_cases=homes, post_resolver_attachment_cases=mutation,
            candidate_words_covered=len(coverage[0]), retail_words_covered=len(coverage[1]),
            comparison='public memory, normalized calls and full return word', full_stack_equivalence=False,
            caller_saved_GP_FP_clobbered=True))

    def test_connected_original_lookup_resolver_sdk_point_list_and_translation(self):
        cases, visited = 0, set()
        for route, count, page, index, alias, phase in itertools.product(range(8), (-1, 0, 2),
                (0, 1), (-1, 0, 2), range(3), (0, 8)):
            memory, args = fixture(route, count, page, index, alias)
            for model in self.check_case(memory, args, phase=phase, connected=self.connected):
                visited.update(model.visits)
            cases += 1
        for phase in (0, 8):
            memory, args = fixture(4)
            put(memory, INPUT, 0)
            for axis in range(3):
                put(memory, SOURCES + 12 + axis * 4, 0x80000000 if axis & 1 else 0)
            for model in self.check_case(memory, args, phase=phase, connected=self.connected):
                visited.update(model.visits)
            cases += 1
        helpers = {hex(entry): sum(entry <= pc < entry + length * 4 for pc in visited)
            for entry, length in ((LOOKUP, 28), (RESOLVE, 85), (CONVERT, 45), (POINT, 40),
                (LIST, 117), (matrix_list.TRANSLATE, 49))}
        self.assertTrue(all(helpers.values()), helpers)
        recursive = 0
        for parent_kind, phase in itertools.product(('actor_bank', 'descriptor_bank', 'attachment'), (0, 8)):
            memory, args = fixture(2)
            parent = NODE + 0x80
            memory.update({parent + i: 0 for i in range(0x60)})
            put(memory, NODE + 0x34, 0)
            put(memory, NODE + 0x1E, 38, 2)
            put(memory, NODE + 0x20, 1, 2)
            put(memory, NODE + 0x54, parent)
            put(memory, parent, 3, 1)
            put(memory, parent + 6, 38, 1)
            put(memory, parent + 2, 1, 1)
            put(memory, parent + 0x34, DESCRIPTOR_BANK if parent_kind == 'descriptor_bank' else 0)
            put(memory, parent + 0x48, ATTACHMENT if parent_kind == 'attachment' else 0)
            expected, _, result = reference(memory, args, phase=phase)
            models = [MatrixRouteOracle(words, memory, args, phase=phase, connected=self.connected).run()
                for words in (self.words, self.retail)]
            for model in models:
                self.assertEqual(external_memory(model.memory), external_memory(expected))
                self.assertEqual(model.r[2], result)
                self.assertEqual(sum(call[0] == RESOLVE for call in model.calls), 2)
                self.assertEqual(sum(call[0] == LOOKUP for call in model.calls), 2)
                visited.update(model.visits)
            self.assertEqual(models[0].calls, models[1].calls)
            recursive += 1
        helpers = {hex(entry): sum(entry <= pc < entry + length * 4 for pc in visited)
            for entry, length in ((LOOKUP, 28), (RESOLVE, 85), (CONVERT, 45), (POINT, 40),
                (LIST, 117), (matrix_list.TRANSLATE, 49))}
        self.receipt('connected', dict(cases=cases, helper_words_visited=helpers,
            acyclic_recursive_resolver_cases=recursive,
            original_instructions=True, full_stack_equivalence=False, hardware_FCSR=False,
            production_resolver_is_still_placeholder=True))

    def test_lazy_gates_required_storage_and_unclamped_index(self):
        lazy = 0
        memory, args = fixture()
        for altered in ((0, 0, *args[2:]), (ACTOR, 0, *args[2:])):
            absent = {a: v for a, v in memory.items() if not ACTOR <= a < NODE + 0x60}
            self.check_case(absent, altered)
            lazy += 1
        for count in COUNTS[:3]:
            memory, args = fixture(count=count)
            absent = {a: v for a, v in memory.items() if not INPUT <= a < ALTERNATE + 108}
            self.check_case(absent, (*args[:3], 0, 0, args[5]), connected=self.connected)
            lazy += 1
        required = 0
        for missing in (ACTOR + 0x1D4, DESCRIPTOR + 0x48, ATTACHMENT + 0x3F6, PAGE,
                ATTACHMENT + 0x3E8, BANK, INPUT, OUTPUT, SOURCES, SOURCES + 4, SOURCES + 8, RESULTS):
            memory, args = fixture(count=1)
            del memory[missing]
            for words in (self.words, self.retail):
                with self.assertRaises((AssertionError, KeyError)):
                    MatrixRouteOracle(words, memory, args, connected=self.connected).run()
            required += 1
        wrapped = 0
        for index in (0x7FFFFFFF, 0x80000000, 0x02000000, 0xFFFFFFFF):
            memory, args = fixture(count=1)
            selected = (BANK + index * 64) & 0xFFFFFFFF
            for i in range(64):
                memory[selected + i] = memory[BANK + i]
            self.check_case(memory, (*args[:2], index, *args[3:]), connected=self.connected)
            wrapped += 1
        self.receipt('gates', dict(lazy_cases=lazy, required_storage_faults=required,
            guest_only_wrapping_indices=wrapped, no_clamp=True))

    def test_private_overlap_counterexamples_prevent_word_guard_installation(self):
        cases, changed, offsets = 0, 0, []
        for source_offset, count, phase in itertools.product((0, 16, 32, 48), (1, 2), (0, 8)):
            memory, args = fixture(count=count)
            for i in range(count):
                put(memory, INPUT + i * 4, STACK + phase - 0xA0 + 0x4C + source_offset)
            models = [MatrixRouteOracle(words, memory, args, phase=phase, connected=self.connected).run()
                for words in (self.words, self.retail)]
            changed += external_memory(models[0].memory) != external_memory(models[1].memory)
            offsets.append([model.private_matrices[0] - (STACK + phase) for model in models])
            cases += 1
        self.assertGreater(changed, 0)
        self.assertEqual({tuple(pair) for pair in offsets}, {(-0x40, -0x54)})
        self.receipt('private', dict(cases=cases, observed_public_output_counterexamples=changed,
            absolute_matrix_offsets_from_entry_sp=[-64, -84], raw_candidate_not_fully_equivalent=True,
            normalization_permitted=False, production_placeholder_unchanged=True))

    def test_source_and_profile_corpus_and_output_detected_negatives(self):
        forms = [(n, b, 'o2g3') for group in (screen.candidates, screen.lifetime_candidates,
            screen.branch_candidates, screen.register_candidates, screen.phase_candidates,
            screen.layout_candidates, screen.route_candidates) for n, b in group()]
        forms += [('profile-' + p, screen.BASELINE, p) for p in screen.PROFILES]
        self.assertEqual(len(forms), 208)
        records, executions = [], 0
        for name, body, profile in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile)
            self.assertGreater(record['differences'], 0)
            self.assertEqual((record['pool_bytes'], record['diagnostics']), (0, ''))
            for route, count in itertools.product(range(8), (-1, 0, 2)):
                memory, args = fixture(route, count)
                expected, calls, result = reference(memory, args)
                model = MatrixRouteOracle(words, memory, args).run()
                self.assertEqual((external_memory(model.memory), model.calls, model.r[2]),
                    (external_memory(expected), calls, result), name)
                executions += 1
            records.append(record)
        negatives = dict(wrong_attachment_flag=screen.SELECTED.replace('attachment[0x3F6] == 0', 'attachment[0x3F6] != 0'),
            wrong_page=screen.SELECTED.replace('[D_800BE9C0]', '[0]'),
            wrong_index=screen.SELECTED.replace(' + index;', ' + 0;'),
            wrong_lookup_key=screen.SELECTED.replace('actor, *(u16 *)(descriptor + 0x1E), 0', 'actor, 38, 0'),
            wrong_count=screen.SELECTED.replace('count > 0', 'count == 1'),
            wrong_source_stride=screen.SELECTED.replace('input++;', 'input += 2;'))
        detected = {}
        for name, body in negatives.items():
            self.assertNotEqual(body, screen.SELECTED, name)
            _, words = screen.compile_candidate(self.root, self.out, 'negative-' + name, body)
            differences = 0
            for route in range(4):
                memory, args = fixture(route, 2, 1, 2)
                expected, _, result = reference(memory, args)
                model = MatrixRouteOracle(words, memory, args).run()
                differences += (external_memory(model.memory), model.r[2]) != (external_memory(expected), result)
            self.assertGreater(differences, 0, name)
            detected[name] = differences
        self.receipt('controls', dict(count=len(forms), executions=executions,
            exact=0, measurements=records, negative_output_detections=detected,
            ABI_home_mutations_not_claimed_for_every_source_form=True))

    def test_native_32bit_actual_sdk_conversion_and_typed_six_word_wrapper(self):
        sdk = (self.root / 'conker/src/libultra/gu/mtxutil2.c').read_text().split('void guMtxL2F', 1)[1]
        self.fixture = r'''typedef unsigned char u8;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;typedef float f32;
typedef union {s32 m[4][4];double alignment;} Mtx;
typedef struct {f32 unk0,unk4,unk8;} struct17;
typedef struct {u8 pad[0x1D4];void *unk1D4;} struct127;
typedef struct {u8 bytes[0x60];} struct126;
typedef union {u32 alignment;u8 bytes[0x410];} Storage;
typedef char pointer_width[(sizeof(void *)==4)?1:-1];
void guMtxL2F(f32 [4][4],Mtx *);
struct126 *func_1503195C(struct127 *,s32,s32);
''' + screen.DECLARATIONS + r'''
u8 D_800BE9C0;
static Storage descriptor,attachment;static struct127 actor;static struct126 node;
static Mtx matrices[6],otherBank[4];static Mtx *selected,*resolved;
static struct17 source[9],result[9],expectedSource[9],expectedResult[9];
static struct17 *input[8],*output[8];static f32 expectedMatrix[4][4];
static int route,alias,error,lookups,resolves,conversions,transforms,lists;
static u32 word(f32 f){union{f32 f;u32 u;}v;v.f=f;return v.u;}
void sdkMtxL2F''' + sdk + r'''
struct126 *func_1503195C(struct127 *a,s32 key,s32 ordinal){
    if(a!=&actor||key!=37||ordinal||resolves||conversions||transforms||lists)error=1;
    lookups++;return route==6?0:&node;
}
s32 func_15031070(struct126 *n,struct127 *a,Mtx **primary,Mtx **other){
    if(n!=&node||a!=&actor||lookups!=1||resolves||conversions||transforms||lists||primary==other)error=2;
    resolves++;if(route==7)return 0;*primary=resolved;*other=matrices;return 1;
}
void guMtxL2F(f32 matrix[4][4],Mtx *fixed){
    if(fixed!=selected||conversions||transforms||lists)error=3;
    conversions++;sdkMtxL2F(matrix,fixed);
}
static void transform(f32 m[4][4],f32 x,f32 y,f32 z,struct17 *out){
    f32 *v=(f32 *)m;out->unk0=(v[0]*x+v[4]*y)+(v[8]*z+v[12]);
    out->unk4=(v[1]*x+v[5]*y)+(v[9]*z+v[13]);
    out->unk8=(v[2]*x+v[6]*y)+(v[10]*z+v[14]);
}
void func_150A7960(f32 m[4][4],f32 x,f32 y,f32 z,f32 *ox,f32 *oy,f32 *oz){
    int i;struct17 out;
    if(conversions!=1||lists||oy!=ox+1||oz!=ox+2)error=4;
    for(i=0;i<16;i++)if(word(((f32 *)m)[i])!=word(((f32 *)expectedMatrix)[i]))error=5;
    transform(m,x,y,z,&out);*ox=out.unk0;*oy=out.unk4;*oz=out.unk8;transforms++;
}
void func_15145EA4(struct17 **inputs,struct17 **outputs,u8 *bank,s32 count){
    int i;f32 m[4][4];
    if(route!=4||inputs!=input||outputs!=output||bank!=(u8 *)selected||lookups||resolves||conversions||lists)error=6;
    lists++;sdkMtxL2F(m,(Mtx *)bank);
    for(i=0;i<count;i++)transform(m,inputs[i]->unk0,inputs[i]->unk4,inputs[i]->unk8,outputs[i]);
}
static void init(int r,int page,int index,int n,int a,int pattern){
    int i,j,k;u32 first,second;Storage *d=&descriptor;
    route=r;alias=a;error=lookups=resolves=conversions=transforms=lists=0;
    for(i=0;i<(int)sizeof(Storage);i++)d->bytes[i]=attachment.bytes[i]=0;
    for(i=0;i<0x60;i++)node.bytes[i]=0;
    D_800BE9C0=page;actor.unk1D4=matrices+1;
    for(k=0;k<10;k++)for(i=0;i<8;i++){
        Mtx *m=k<6?matrices+k:otherBank+k-6;
        first=(u32)((((i*2+pattern+k*5)%17)-8)*8192);
        second=(u32)((((i*2+1+pattern+k*5)%17)-8)*8192);
        ((u32 *)m)[i]=(first&0xFFFF0000)|(second>>16);
        ((u32 *)m)[i+8]=(first<<16)|(second&65535);
    }
    *(u8 **)(d->bytes+0x48)=r==0||r==5?attachment.bytes:0;
    attachment.bytes[0x3F6]=1;((Mtx **)(attachment.bytes+0x3E8))[page]=matrices+1+page;
    *(u16 *)(d->bytes+0x1E)=r==1||r==2||r==6||r==7?37:0;
    *(u16 *)(d->bytes+0x20)=1;d->bytes[2]=2;
    *(Mtx **)(d->bytes+0x34)=r==3?otherBank:0;
    *(u8 **)(node.bytes+0x48)=r==1?attachment.bytes:0;
    resolved=r==1?matrices+1+page:otherBank+page;
    selected=r==0?matrices+1+page+index:r==1?resolved+1:r==2?resolved:r==3?otherBank+page:matrices+3;
    if(r==5){((Mtx **)(attachment.bytes+0x3E8))[page]=0;selected=0;}
    if(selected)sdkMtxL2F(expectedMatrix,selected);
    for(i=0;i<9;i++){
        f32 *s=(f32 *)(source+i),*out=(f32 *)(result+i);
        for(j=0;j<3;j++){s[j]=(f32)((i*3+j+pattern)%9-4)/4;out[j]=-123.5f;}
        expectedSource[i]=source[i];expectedResult[i]=result[i];
        if(i<8){input[i]=source+i;output[i]=a?source+i+(a==2):result+i;}
    }
    if(r<5)for(i=0;i<n;i++){
        struct17 *s=expectedSource+i,*out=a?expectedSource+i+(a==2):expectedResult+i;
        transform(expectedMatrix,s->unk0,s->unk4,s->unk8,out);
    }
}
''' + screen.SELECTED + '\n'
        self.run_host(r'''
int r,p,i,n,a,k,j,res;static int counts[]={-2147483647-1,-1,0,1,2,4};
for(r=0;r<8;r++)for(p=0;p<2;p++)for(i=-1;i<=2;i++)for(n=0;n<6;n++)for(a=0;a<3;a++)for(k=0;k<8;k++){
    init(r,p,i,counts[n],a,k);
    res=func_1514654C(&actor,descriptor.bytes,r==5?0:i,input,output,counts[n]);
    if(error||res!=(r<5))return 1;
    if(lookups!=(r==1||r==2||r==6||r==7)||resolves!=(r==1||r==2||r==7))return 2;
    if(conversions!=(r<4)||lists!=(r==4)||transforms!=(r<4&&counts[n]>0?counts[n]:0))return 3;
    for(j=0;j<27;j++)if(word(((f32 *)source)[j])!=word(((f32 *)expectedSource)[j])||
        word(((f32 *)result)[j])!=word(((f32 *)expectedResult)[j]))return 4;
}
init(0,0,0,2,0,0);
if(func_1514654C(0,0,0,0,0,2)||conversions||lookups||resolves||transforms||lists)return 5;
if(func_1514654C(&actor,0,0,0,0,2)||conversions||lookups||resolves||transforms||lists)return 6;
actor.unk1D4=0;
if(func_1514654C(&actor,descriptor.bytes,0,0,0,2)||conversions||lookups||resolves||transforms||lists)return 7;
''')
        self.receipt('native', dict(cases=8*2*4*6*3*8, lazy_cases=3, pointer_bytes=4,
            actual_complete_candidate_C=True, actual_SDK_converter_C=True,
            other_helpers='bounded validating native callbacks', finite_coordinates=True,
            candidate_private_frame_not_installed=True))

    def test_copied_owner_only_target_changes_and_no_new_pools_or_warnings(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        stub = 's32 func_1514654C() {\n    return 0;\n}'
        self.assertEqual(source.count(stub), 1)
        selected = source.replace(stub, screen.SELECTED).replace('s32 func_1514654C();',
            screen.DECLARATIONS + screen.PROTOTYPE)
        objects, warnings = [], []
        for name, body in (('baseline', source), ('selected', selected)):
            obj, diagnostic = compile_owner(self.root, self.out, body, 'owner-' + name)
            warnings.append([(item[0], item[2]) for item in diagnostic])
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
            previous = old_functions[name]
            self.assertEqual(text[current['value']:current['value'] + current['size']],
                old_text[previous['value']:previous['value'] + previous['size']], name)
            self.assertEqual({o - current['value']: r for o, r in rel.items() if current['value'] <= o < current['value'] + current['size']},
                {o - previous['value']: r for o, r in old_rel.items() if previous['value'] <= o < previous['value'] + previous['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        target = functions[screen.FUNCTION]
        standalone, isolated_functions, isolated_rel = parse_object(self.out / 'selected.o')
        size = isolated_functions[screen.FUNCTION]['size']
        self.assertEqual(target['size'], size)
        self.assertEqual(text[target['value']:target['value'] + size], standalone[:size])
        self.assertEqual({o - target['value']: r for o, r in rel.items() if target['value'] <= o < target['value'] + size}, isolated_rel)
        self.receipt('owner', dict(functions=89, unchanged_neighbors=88, warnings=2,
            normalized_pools_equal=True, target_matches_isolated=True, object_words=size//4,
            meaningful_body_words=119, no_production_edit=True))
