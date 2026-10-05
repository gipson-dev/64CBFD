"""Full light-selector candidate, including explicit non-adoption controls."""

import hashlib
import itertools
import json
import math
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

from tools import match_progress
from tools.pad_generated_object import parse_object
from tools.tests.test_game_dual_matrix_emitter import sdk_macro
from tools.tests.test_game_random_curve_record import START
from tools.tests import test_game_palette_updater as palette
from tools.tests import test_game_queued_segment_writer as queue
from tools.tests import test_game_viewport_renderer as renderer
from tools.tests.game_animation_timeline_oracle import TimelineOracle, bits, floating


ENTRY = 0x1515D914
HEAD = 0x800DCD78
PAGE = 0x800BE9C0
NODES = 0x60000
LIGHTS = 0x70000
AMBIENT = 0x80000
COUNT = 0x81000
HISTORY = 0x82000
SELECTED = 0x83000
POSITIONS = 0x84000
SPECS = {0x1515E278: 7, 0x1515E43C: 8, 0x1515EC78: 7}
PROFILES = {'o2': ['-O2', '-g3'], 'o1': ['-O1'],
            'o2-no-unroll': ['-O2', '-g3', '-Wo,-loopunroll,0']}


def case(nodes=(), slot=0, capacity=4, flags=4, channels=2, page=0,
         history=True, count=True, selected=True, coordinates=(0, 0, 0)):
    memory = {queue.OUTPUT + i: 0xA5 for i in range(0x1010)}
    memory.update({queue.STACK + i: 0xA5 for i in range(-0x500, 0x80)})
    memory.update({NODES + i: 0xA5 for i in range(0x40 * (len(nodes) + 1))})
    for first, size in ((LIGHTS, 2 * 11 * 48 + 32), (AMBIENT, 48), (COUNT, 16),
                        (HISTORY, 16), (SELECTED, 48), (POSITIONS, 256),
                        (renderer.ACTORS, 4 * 0x9A0), (0x800DCD30, 16), (0x800DCD40, 48)):
        memory.update({first + i: 0xA5 for i in range(size)})
    for address, value, size in ((HEAD, NODES if nodes else 0, 4), (PAGE, page, 1),
                                 (renderer.BASE, renderer.ACTORS, 4)):
        palette.put(memory, address, value, size)
    for row in range(4):
        for index, value in enumerate((3.0, 4.0, 0.0)):
            palette.put(memory, renderer.ACTORS + row * 0x9A0 + 0x2BC + index * 4, bits(value), 4)
            palette.put(memory, renderer.ACTORS + row * 0x9A0 + 0x2F8 + index * 4, bits(0.0), 4)
        for index, value in enumerate((0x80, 0x7F, 0xFF)):
            palette.put(memory, 0x800DCD30 + row * 3 + index, value, 1)
    for index, node in enumerate(nodes):
        address = NODES + index * 0x40
        values = ((0, address + 0x40 if index + 1 < len(nodes) else 0, 4),
                  (4, node.get('type', 0), 1), (8, node.get('channels', 2), 1),
                  (9, node.get('disabled', 0), 1), (0xA, node.get('excluded', 0), 1),
                  (0xC, node.get('selected', 0), 1), (0x2F, node.get('radius', 255), 1))
        for offset, value, size in values:
            palette.put(memory, address + offset, value, size)
        if 'pointer' in node:
            position = POSITIONS + index * 12
            palette.put(memory, address + 0xE, 0x8000, 2)
            palette.put(memory, address + 0x10, position >> 16, 2)
            palette.put(memory, address + 0x12, position & 65535, 2)
            for component, value in enumerate(node['pointer']):
                palette.put(memory, position + component * 4, bits(value), 4)
        else:
            for component, value in enumerate(node.get('position', (index * 10, 0, 0))):
                palette.put(memory, address + 0xE + component * 2, value, 2)
    args = (queue.OUTPUT, slot, *coordinates, 0, LIGHTS, capacity, AMBIENT,
            COUNT if count else 0, channels, HISTORY if history else 0, flags,
            SELECTED if selected else 0)
    return memory, args


class LightSelectorOracle(renderer.RendererOracle):
    def __init__(self, words, memory, arguments, mutation=0, ambient=(1, 128, 255),
                 secondary=(255, 128, 1), environment=(1, 128, 255), alphas=(255, 128)):
        queue.SegmentQueueOracle.__init__(self, words, ENTRY, memory, arguments[:4])
        for index, value in enumerate(arguments[4:], 4):
            palette.put(self.memory, queue.STACK + index * 4, value, 4)
        self.events, self.connected, self.global_stores = [], {}, []
        self.mutation, self.slot, self.condition = mutation, arguments[1], False
        self.ambient, self.secondary, self.environment, self.alphas = ambient, secondary, environment, alphas
        self.callback_reads = []

    def put(self, address, value, size):
        if self.recording:
            assert (queue.STACK - 0x500 <= address < queue.STACK + 0x80
                    or queue.OUTPUT <= address < queue.OUTPUT + 0x1000
                    or LIGHTS <= address < LIGHTS + 2 * 11 * 48
                    or AMBIENT <= address < AMBIENT + 7
                    or COUNT <= address < COUNT + 1
                    or HISTORY <= address < HISTORY + 3
                    or SELECTED <= address < SELECTED + 44
                    or NODES <= address < NODES + 0x40 * 17), ('light-selector output fence', address, size)
        queue.SegmentQueueOracle.put(self, address, value, size)

    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        fn, rd, fd = word & 63, word >> 11 & 31, word >> 6 & 31
        if op == 17 and rs == 16 and fn in (3, 4):
            left, right = floating(self.f[rd]), floating(self.f[rt])
            value = math.sqrt(left) if fn == 4 else left / right
            self.f[fd] = bits(value)
        elif op == 32:
            value = self.get((self.r[rs] + ((word & 65535) if word & 0x8000 == 0 else (word & 65535) - 65536)) & 0xFFFFFFFF, 1)
            self.r[rt] = (value if value < 128 else value - 256) & 0xFFFFFFFF
        else:
            super().execute(word)

    def record_call(self, target):
        args = self.arguments(SPECS[target])
        if target == 0x1515E278:
            normalized = args[:4] + args[5:]
        elif target == 0x1515E43C:
            normalized = args[:4]
        else:
            normalized = args
        self.events.append((target, normalized))

    def hook(self, target):
        args = self.arguments(SPECS[target])
        if target == 0x1515E278:
            for i, value in enumerate(self.ambient):
                self.put(args[4] + i, value, 1)
            if self.mutation == 1:
                palette.put(self.memory, PAGE, 1, 1)
        elif target == 0x1515E43C:
            for i in range(3):
                self.put(args[4] + i, self.secondary[i], 1)
                self.put(args[5] + i, self.environment[i], 1)
            self.put(args[6], self.alphas[0], 1)
            self.put(args[7], self.alphas[1], 1)
        else:
            node, slot, data, x, y, z, flags = args
            self.callback_reads.append((node, self.peek(node + 0xC, 1), self.peek(PAGE, 1)))
            for i, value in enumerate((slot & 255, 0x19, 0xF2)):
                self.put(data + i, value, 1)
                self.put(data + i + 4, value, 1)
            if self.mutation == 2:
                palette.put(self.memory, PAGE, 1 - self.peek(PAGE, 1), 1)
            if self.mutation == 3:
                palette.put(self.memory, node + 4, 1, 1)
                palette.put(self.memory, HEAD, 0, 4)
        for register in (2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]


class GameLightSelectorCandidateTests(unittest.TestCase):
    test_complete_init_debugger_and_game_data_remain_exact = (
        queue.GameQueuedSegmentWriterTests.test_complete_init_debugger_and_game_data_remain_exact)

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.project = cls.root / 'conker'
        for tool in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump', 'cc'):
            if shutil.which(tool) is None:
                raise unittest.SkipTest(tool + ' unavailable')
        cls.source = cls.root / 'tools/experiments/game_light_selector_candidate.c'
        cls.source_hash = hashlib.sha256(cls.source.read_bytes()).hexdigest()
        cls.output = cls.project / 'build/game-light-selector-candidate'
        cls.output.mkdir(parents=True, exist_ok=True)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.rom = (cls.project / 'conker.us.bin').read_bytes()
        config = yaml.safe_load((cls.project / 'conker.us.yaml').read_text())
        assert hashlib.sha1(cls.rom).hexdigest() == config['sha1']
        cls.retail = list(struct.unpack_from('>601I', cls.rom, 0x18ADC4))
        cls.renderer_retail = list(struct.unpack_from('>356I', cls.rom, 0x138E80))
        data = next(segment for segment in config['segments']
                    if isinstance(segment, dict) and segment.get('name') == 'game_data')
        cls.renderer_table = struct.unpack_from('>35I', cls.rom,
            data['start'] + 0x800A2C2C - data['vram'])
        cls.production, _, _ = match_progress.load_elf_functions(
            str(cls.project / 'build/conker.us.elf'), 'mips-linux-gnu-objdump')
        cls.compiled, cls.measurements, cls.pairs, cls.completed = {}, {}, {}, set()
        cls.native_cases, cls.initial_distance_pairs, cls.caller_frame_pairs = 0, 0, 0
        for profile, flags in PROFILES.items():
            out = cls.output / profile
            out.mkdir(exist_ok=True)
            source, obj, elf, script = [out / ('candidate' + suffix) for suffix in ('.c', '.o', '.elf', '.ld')]
            shutil.copyfile(cls.source, source)
            obj.unlink(missing_ok=True)
            result = subprocess.run([str(cls.root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
                '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
                '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32',
                '-I', 'include', '-I', 'include/2.0L', '-I', 'include/2.0L/PR', '-I', 'include/libc',
                *flags, '-mips2', '-o32', '-o', str(obj.relative_to(cls.project)),
                str(source.relative_to(cls.project))], cwd=cls.project, capture_output=True, text=True)
            assert result.returncode == 0, result.stdout + result.stderr
            diagnostics = result.stdout + result.stderr
            (out / 'compiler.log').write_text(diagnostics)
            script.write_text('SECTIONS { .text 0x1515D914 : SUBALIGN(4) { *(.text) } }\n')
            args = ['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
                    '-T', 'undefined_syms.us.txt', '-T', 'undefined_syms_auto.txt',
                    '-e', 'func_1515D914', '-o', str(elf), str(obj)]
            args += ['--defsym=func_%08X=0x%08X' % (address, address) for address in SPECS]
            result = subprocess.run(args, cwd=cls.project, capture_output=True, text=True)
            assert result.returncode == 0, result.stdout + result.stderr
            functions, _, addresses = match_progress.load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
            assert addresses['func_1515D914'] == ENTRY
            words = functions['func_1515D914']
            text, symbols, _ = parse_object(str(obj))
            cls.compiled[profile], cls.pairs[profile] = words, 0
            cls.measurements[profile] = {'body_bytes': symbols['func_1515D914']['size'],
                'complete_text_bytes': len(text), 'retail_slot_bytes': 2404,
                'frame': (-words[0]) & 65535,
                'compiler_diagnostics': diagnostics,
                'instruction_sha256': hashlib.sha256(struct.pack('>' + str(len(words)) + 'I', *words)).hexdigest()}
        cls.coverage = {profile: set() for profile in (*PROFILES, 'retail')}

    def tearDown(self):
        if self._outcome.success:
            type(self).completed.add(self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        unchanged = cls.source_hash == hashlib.sha256(cls.source.read_bytes()).hexdigest()
        receipt = {'measurements': cls.measurements, 'pairs': cls.pairs,
                   'native_cases': cls.native_cases, 'initial_distance_pairs': cls.initial_distance_pairs,
                   'caller_frame_pairs': cls.caller_frame_pairs,
                   'completed_checks': sorted(cls.completed),
                   'candidate_source_sha256': cls.source_hash, 'candidate_source_unchanged': unchanged,
                   'complete_module_corpus': (unchanged and cls.completed == set(
                       unittest.defaultTestLoader.getTestCaseNames(cls))
                       and cls.pairs == {profile: 17410 for profile in PROFILES}
                       and cls.native_cases == 192 and cls.initial_distance_pairs == 168
                       and cls.caller_frame_pairs == 12),
                   'coverage': {profile: {'visited_words': len(addresses),
                       'unvisited_body_addresses': [hex(ENTRY + index * 4) for index in range(
                           601 if profile == 'retail' else cls.measurements[profile]['body_bytes'] // 4)
                           if ENTRY + index * 4 not in addresses]}
                       for profile, addresses in cls.coverage.items()},
                   'adopted': False,
                   'qualification': 'finite light products and pinned stack seed; no-unroll fits but connected caller-frame witness diverges'}
        (cls.output / 'qualification.json').write_text(json.dumps(receipt, indent=2) + '\n')
        print('light selector candidate:', cls.measurements, 'pairs:', cls.pairs)

    def compare(self, memory, args, **kwargs):
        expected = LightSelectorOracle(self.retail, memory, args, **kwargs).run()
        for profile, words in self.compiled.items():
            actual = LightSelectorOracle(words, memory, args, **kwargs).run()
            self.assertEqual(actual.events, expected.events)
            self.assertEqual(actual.callback_reads, expected.callback_reads)
            self.assertEqual(actual.r[2], expected.r[2])
            visible = lambda fixture: {a: v for a, v in fixture.memory.items()
                                       if not queue.STACK - 0x500 <= a < queue.STACK + 0x80}
            left, right = visible(actual), visible(expected)
            differences = [(hex(a), left.get(a), right.get(a)) for a in left.keys() | right.keys()
                           if left.get(a) != right.get(a)]
            self.assertEqual(differences[:16], [], profile)
            type(self).pairs[profile] += 1
            type(self).coverage[profile].update(actual.visits)
        type(self).coverage['retail'].update(expected.visits)
        return expected

    def test_empty_list_capacity_and_flag_products(self):
        for capacity, flags, slot, page in itertools.product(range(0, 12), range(64), range(4), range(2)):
            self.compare(*case(capacity=capacity, flags=flags, slot=slot, page=page))

    def test_positional_lists_rank_filter_ties_and_all_capacities(self):
        lists = [[], [{'position': (10, 0, 0)}],
                 [{'position': (v, 0, 0)} for v in (30, 10, 20, 10, -10, 0, 40, 5)],
                 [{'pointer': (1.75, -2.75, 3.5)}, {'position': (1, -2, 3)}],
                 [{'position': (100, 0, 0), 'disabled': 1}, {'position': (200, 0, 0), 'channels': 4},
                  {'position': (300, 0, 0), 'excluded': 1}, {'position': (400, 0, 0), 'radius': 0},
                  {'position': (500, 0, 0), 'channels': 3}, {'position': (600, 0, 0)}]]
        for nodes, capacity, flags, slot, page in itertools.product(lists, range(0, 12),
                                                                    (0, 1, 2, 4, 8, 0x20, 0x25, 0x3F),
                                                                    range(4), range(2)):
            self.compare(*case(nodes, slot=slot, capacity=capacity, flags=flags, page=page))

    def test_optional_outputs_and_mutating_light_callbacks(self):
        for slot, capacity, flags, history, count, selected, mutation in itertools.product(
                range(4), (0, 1, 2, 3, 4, 11), (0, 2, 4, 8, 0x20, 0x3F),
                range(2), range(2), range(2), range(4)):
            self.compare(*case([{'position': (i, 0, 0)} for i in range(6)], slot=slot,
                               capacity=capacity, flags=flags, history=history, count=count, selected=selected),
                         mutation=mutation)

    def test_defined_mixed_nodes_keep_carried_distance_and_stable_ties(self):
        for types, flags, capacity in itertools.product(((0, 1, 0, 1), (0, 1, 1, 0), (0, 0, 1, 1)),
                                                        (0, 4, 0x20), range(2, 12)):
            nodes = [{'type': value, 'position': (index * 10, 0, 0)} for index, value in enumerate(types)]
            self.compare(*case(nodes, flags=flags, capacity=capacity))

    def test_zero_and_finite_actor_vectors_preserve_query_truncation(self):
        for vector, slot, capacity, flags, coordinates, page in itertools.product(
                ((0.0, 0.0, 0.0), (-3.0, 0.0, 0.0), (1.0, 2.0, 2.0)), range(4),
                (0, 1, 2, 11), (1, 3, 5, 0x21, 0x3F),
                ((0, 0, 0), (32767, -32768, 65536), (65537, -65537, 3),
                 (-123456, 123456, -98765)), range(2)):
            memory, args = case([{'position': (1, 2, 3)}, {'position': (10, 20, 30)}],
                               slot=slot, capacity=capacity, flags=flags,
                               coordinates=coordinates, page=page)
            for index, value in enumerate(vector):
                palette.put(memory, renderer.ACTORS + slot * 0x9A0 + 0x2BC + index * 4,
                            bits(value), 4)
            self.compare(memory, args)

    def test_signed_wrapping_distances_and_preselected_channel_gate(self):
        patterns = ([{'position': (32767, -32768, 32767)},
                     {'position': (-32767, 32767, -32768)}],
                    [{'pointer': (2147483520.0, -2147483520.0, 32767.0)}],
                    [{'position': (32767, 32767, 32767)}, {'type': 1}],
                    [{'position': (3, 4, 5), 'channels': 3, 'selected': 15},
                     {'position': (3, 4, 5), 'channels': 3, 'selected': 0}])
        for nodes, capacity, flags, slot, page in itertools.product(
                patterns, (0, 1, 2, 3, 11), (0, 4, 0x20, 0x24), range(4), range(2)):
            self.compare(*case(nodes, capacity=capacity, flags=flags, slot=slot,
                               page=page, coordinates=(-32768, 32767, -32768)))

    def test_first_directional_distance_uses_exact_caller_stack_word(self):
        for poison, slot, page, capacity in itertools.product(
                (0, 1, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFF, 0xA5A5A5A5, 0x5A5A5A5A),
                range(4), range(2), (2, 3, 11)):
            memory, args = case([{'type': 1}, {'type': 1}], slot=slot, page=page, capacity=capacity)
            seed = queue.STACK - 0x84
            palette.put(memory, seed, poison, 4)
            self.compare(memory, args)
            for words in (self.retail, *self.compiled.values()):
                fixture = LightSelectorOracle(words, memory, args).run()
                self.assertEqual(next(value for address, size, value in fixture.reads
                                      if address == seed and size == 4), poison)
            type(self).initial_distance_pairs += 1

    def test_zero_initialization_control_changes_retail_directional_selection(self):
        memory, args = case([{'type': 1}, {'type': 1}], capacity=3)
        palette.put(memory, queue.STACK - 0x84, 0x7FFFFFFF, 4)
        expected = LightSelectorOracle(self.retail, memory, args).run()
        words = self.retail.copy()
        index = (0x1515DC80 - ENTRY) // 4
        self.assertEqual(words[index], 0x8FAB00B4)
        words[index] = 0x00005825
        mutant = LightSelectorOracle(words, memory, args).run()
        self.assertEqual(expected.peek(COUNT, 1), 1)
        self.assertEqual(mutant.peek(COUNT, 1), 3)
        self.assertNotEqual(mutant.r[2], expected.r[2])

    def test_connected_caller_frame_witness_blocks_directional_adoption(self):
        class Child(LightSelectorOracle):
            def __init__(self, words, memory, args):
                self.ranges = [(queue.STACK - 0x500, queue.STACK + 0x80),
                    (queue.OUTPUT, queue.OUTPUT + 0x1000), (LIGHTS, LIGHTS + 1056),
                    (NODES, NODES + 0x440), (args[8], args[8] + 7),
                    (args[9], args[9] + 1), (args[13], args[13] + 44)]
                super().__init__(words, memory, args)

            def put(self, address, value, size):
                if self.recording:
                    assert any(first <= address and address + size <= last
                               for first, last in self.ranges), ('connected light fence', address, size)
                queue.SegmentQueueOracle.put(self, address, value, size)

        class Parent(renderer.RendererOracle):
            def __init__(self, words, child, memory, table):
                self.child_words = child
                self.light = None
                super().__init__(words, memory, 0, table)

            def hook(self, target):
                if target != ENTRY:
                    return super().hook(target)
                args = self.arguments(14)
                child = Child(self.child_words, self.memory, args)
                # Preserve the actual caller SP/argument cells, not standalone fixture SP.
                child.memory, child.r, child.f = self.memory.copy(), self.r.copy(), self.f.copy()
                return_address = child.r[31]
                child.r[31] = 0xDEAD0000
                child.before = child.r.copy()
                child.seed = child.r[29] - 0x84
                child.run()
                self.light = child
                self.memory, self.r, self.f = child.memory, child.r.copy(), child.f.copy()
                self.r[31] = return_address

        caller = self.production['func_1510B9D0']
        self.assertEqual(((-self.renderer_retail[0]) & 65535, (-caller[0]) & 65535),
                         (0x98, 0xB8))
        for first_type, reverse in itertools.product((0, 1), (False, True)):
            memory, _ = case([{'type': first_type, 'channels': 1}, {'type': 1, 'channels': 1}])
            memory.update(renderer.case())
            memory.update({0x800D9E28 + index: 0xA5 for index in range(44)})
            old_seed, new_seed = (1, 0x7FFFFFFF) if reverse else (0x7FFFFFFF, 1)
            for address, value, size in ((renderer.VALUE, LIGHTS, 4), (0x800D9E20, 3, 1),
                    (queue.STACK - 0x98 - 0x84, old_seed, 4),
                    (queue.STACK - 0xB8 - 0x84, new_seed, 4)):
                palette.put(memory, address, value, size)
            for index, value in enumerate((3.0, 4.0, 0.0)):
                palette.put(memory, renderer.ACTORS + 0x2BC + index * 4, bits(value), 4)
            expected = Parent(self.renderer_retail, self.retail, memory, self.renderer_table).run()
            for profile, words in self.compiled.items():
                with self.subTest(profile=profile, first_type=first_type, reverse=reverse):
                    actual = Parent(caller, words, memory, self.renderer_table).run()
                    self.assertEqual(expected.light.seed, queue.STACK - 0x11C)
                    self.assertEqual(actual.light.seed, queue.STACK - 0x13C)
                    self.assertEqual(expected.light.seed - actual.light.seed, 32)
                    if first_type:
                        self.assertIn((expected.light.seed, 4, old_seed), expected.light.reads)
                        self.assertIn((actual.light.seed, 4, new_seed), actual.light.reads)
                        self.assertEqual((expected.peek(0x800D9E21, 1), actual.peek(0x800D9E21, 1)),
                                         (3, 1) if reverse else (1, 3))
                        self.assertEqual(abs(expected.r[2] - actual.r[2]), 16)
                        self.assertNotEqual(expected.peek(NODES + 0xC, 1),
                                            actual.peek(NODES + 0xC, 1))
                    else:
                        self.assertEqual(expected.peek(0x800D9E21, 1), 3)
                        self.assertEqual(actual.peek(0x800D9E21, 1), 3)
                        self.assertEqual(actual.r[2], expected.r[2])
                        visible = lambda fixture: {address: value for address, value in fixture.memory.items()
                                                   if not queue.STACK - 0x500 <= address < queue.STACK + 0x80}
                        self.assertEqual(visible(actual), visible(expected))
                    type(self).caller_frame_pairs += 1

    def test_native_retail_derived_full_candidate_outputs(self):
        patterns = ([{'position': (v, 0, 0)} for v in (30, 10, 20, 10, -10, 0, 40, 5)],
                    [{'type': value, 'position': (index * 10 + 15, 0, 0)}
                     for index, value in enumerate((0, 1, 0, 1))],
                    [{'pointer': (1.75, -2.75, 3.5)}, {'position': (1, -2, 3)}])
        records = []
        for pattern, capacity, flags in itertools.product(range(3), (0, 1, 2, 3, 4, 7, 10, 11),
                                                           (0, 1, 2, 4, 8, 0x20, 0x25, 0x3F)):
            slot, page = len(records) % 4, len(records) // 4 % 2
            memory, args = case(patterns[pattern], slot=slot, page=page, capacity=capacity, flags=flags)
            result = LightSelectorOracle(self.retail, memory, args).run()
            packets = (result.r[2] - queue.OUTPUT) // 8
            commands = []
            for index in range(packets):
                w0, w1 = result.peek(queue.OUTPUT + index * 8, 4), result.peek(queue.OUTPUT + index * 8 + 4, 4)
                kind = 1 if LIGHTS <= w1 < LIGHTS + 2 * 11 * 48 else 2 if w1 == AMBIENT else 3 if w1 == 0x800DCD40 else 0
                commands.append((w0, kind, w1 - LIGHTS if kind == 1 else w1 if kind == 0 else 0))
            records.append((pattern, capacity, flags, slot, page, packets, result.peek(COUNT, 1),
                            [result.peek(LIGHTS + i, 1) for i in range(1056)],
                            [result.peek(AMBIENT + i, 1) for i in range(8)],
                            [result.peek(HISTORY + i, 1) for i in range(3)],
                            [result.peek(SELECTED + i * 4, 4) for i in range(11)],
                            [result.peek(NODES + i * 0x40 + 0xC, 1) for i in range(len(patterns[pattern]))],
                            commands))
        def array(values):
            return '{' + ','.join(str(value) for value in values) + '}'
        initializers = []
        for pattern, capacity, flags, slot, page, packets, count, lights, ambient, history, selected, masks, commands in records:
            converted = [0xFFFFFFFF if value == 0xA5A5A5A5 else
                         0xFFFFFFFE if value == 0 else (value - NODES) // 0x40 for value in selected]
            fields = [str(v) for v in (pattern, capacity, flags, slot, page, packets, count)]
            fields += [array(lights), array(ambient), array(history), array(converted), array(masks),
                       '{' + ','.join(array(packet) for packet in commands) + '}']
            initializers.append('{' + ','.join(fields) + '}')
        gbi = (self.project / 'include/2.0L/PR/gbi.h').read_text()
        mbi = (self.project / 'include/2.0L/PR/mbi.h').read_text()
        macros = sdk_macro(mbi, '_SHIFTL')
        for name in ('G_MOVEWORD', 'G_MW_NUMLIGHT', 'G_MWO_NUMLIGHT', 'gDma1p', 'gMoveWd',
                     'G_MOVEMEM', 'G_MV_LIGHT', 'gDma2p'):
            macros += sdk_macro(gbi, name)
        body = re.search(r'Gfx \*func_1515D914\([^{}]+\) \{\n.*?\n\}', self.source.read_text(), re.S).group(0)
        fixture = r'''
typedef unsigned char u8; typedef signed char s8; typedef short s16;
typedef unsigned short u16; typedef int s32; typedef unsigned int u32; typedef float f32;
typedef struct { struct { u32 w0,w1; } words; } Gfx;
''' + macros + r'''
static u8 nodes[8][64], lightStorage[1088], ambient[48], history[16], actors[4*0x9A0];
static f32 positions[3]; static Gfx commands[32]; static u8 *outputs[11];
u8 *D_800DCD78,*D_800DBFF0=actors,D_800BE9C0;
s8 D_800DCD30[12]; u8 D_800DCD40[48]; static u8 count;
void func_1515E278(s32 x,s32 y,s32 z,s32 channels,u8 *out,s32 mode,s32 flags) {
    out[0]=1; out[1]=128; out[2]=255;
}
void func_1515E43C(s32 x,s32 y,s32 z,s32 channels,u8 *first,u8 *second,u8 *a,u8 *b) {
    first[0]=255;first[1]=128;first[2]=1;second[0]=1;second[1]=128;second[2]=255;*a=255;*b=128;
}
void func_1515EC78(u8 *node,s32 slot,u8 *data,s32 x,s32 y,s32 z,s32 flags) {
    data[0]=data[4]=(u8)slot;data[1]=data[5]=0x19;data[2]=data[6]=0xF2;
}
#define sqrtf __builtin_sqrtf
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
#pragma GCC diagnostic ignored "-Wuninitialized"
''' + body + r'''
#pragma GCC diagnostic pop
struct Packet { u32 w0,kind,value; };
struct Case { s32 pattern,capacity,flags,slot,page,packets,count;
    u8 lights[1056],ambient[8],history[3];u32 selected[11];u8 masks[8];struct Packet command[16]; };
static const struct Case cases[]={
''' + ',\n'.join(initializers) + r'''
};
int run(void) {
    static const int offsets[]={30,10,20,10,-10,0,40,5};
    int c,i,j,n; const struct Case *sample; Gfx *end; u32 expected;
    for(c=0;c<192;c++) {
        sample=&cases[c]; n=sample->pattern==0?8:sample->pattern==1?4:2;
        for(i=0;i<1088;i++) lightStorage[i]=0xA5;
        for(i=0;i<48;i++) ambient[i]=0xA5;
        for(i=0;i<16;i++) history[i]=0xA5;
        for(i=0;i<11;i++) outputs[i]=(u8 *)0xA5A5A5A5;
        for(i=0;i<32;i++) commands[i].words.w0=commands[i].words.w1=0xA5A5A5A5;
        for(i=0;i<4;i++) for(j=0;j<3;j++) {
            *(f32 *)(actors+i*0x9A0+0x2BC+j*4)=j==0?3.0f:j==1?4.0f:0.0f;
            *(f32 *)(actors+i*0x9A0+0x2F8+j*4)=0;
            D_800DCD30[i*3+j]=(s8)(j==0?0x80:j==1?0x7F:0xFF);
        }
        for(i=0;i<n;i++) {
            for(j=0;j<64;j++) nodes[i][j]=0xA5;
            *(u8 **)nodes[i]=i+1<n?nodes[i+1]:0;
            nodes[i][4]=sample->pattern==1?(i&1):0;nodes[i][8]=2;nodes[i][9]=nodes[i][10]=nodes[i][12]=0;
            nodes[i][0x2F]=255;
            *(s16 *)(nodes[i]+14)=sample->pattern==0?offsets[i]:sample->pattern==1?i*10+15:1;
            *(s16 *)(nodes[i]+16)=sample->pattern==2?-2:0;
            *(s16 *)(nodes[i]+18)=sample->pattern==2?3:0;
        }
        if(sample->pattern==2) {
            positions[0]=1.75f;positions[1]=-2.75f;positions[2]=3.5f;
            *(s16 *)(nodes[0]+14)=-32768;
            *(u16 *)(nodes[0]+16)=(u32)positions>>16;
            *(u16 *)(nodes[0]+18)=(u32)positions;
        }
        count=0xA5;D_800DCD78=nodes[0];D_800BE9C0=sample->page;
        end=func_1515D914(commands+1,sample->slot,0,0,0,0,lightStorage+16,sample->capacity,
                         ambient,&count,2,history,sample->flags,outputs);
        if(end!=commands+1+sample->packets||count!=sample->count) return 1;
        for(i=0;i<1056;i++) if(lightStorage[i+16]!=sample->lights[i]) return 2;
        for(i=0;i<16;i++) if(lightStorage[i]!=0xA5||lightStorage[1072+i]!=0xA5) return 3;
        for(i=0;i<8;i++) if(ambient[i]!=sample->ambient[i]) return 4;
        for(i=0;i<3;i++) if(history[i]!=sample->history[i]) return 5;
        for(i=0;i<11;i++) {
            expected=sample->selected[i];
            expected=expected==0xFFFFFFFF?0xA5A5A5A5:expected==0xFFFFFFFE?0:(u32)nodes[expected];
            if((u32)outputs[i]!=expected) return 6;
        }
        for(i=0;i<n;i++) if(nodes[i][12]!=sample->masks[i]) return 7;
        for(i=0;i<sample->packets;i++) {
            const struct Packet *p=&sample->command[i];
            expected=p->kind==1?(u32)(lightStorage+16+p->value):p->kind==2?(u32)ambient:
                     p->kind==3?(u32)D_800DCD40:p->value;
            if(commands[i+1].words.w0!=p->w0||commands[i+1].words.w1!=expected) return 8;
        }
        if(commands[0].words.w0!=0xA5A5A5A5||end->words.w0!=0xA5A5A5A5) return 9;
    }
    return 0;
}
''' + START
        source = self.path / 'native.c'
        binary = self.path / 'native'
        source.write_text(fixture)
        result = subprocess.run(['cc', '-m32', '-O2', '-std=c99', '-fno-strict-aliasing', '-fno-math-errno',
            '-msse2', '-mfpmath=sse', '-mstackrealign', '-ffreestanding', '-nostdlib', '-static', '-fno-pie',
            '-no-pie', '-fno-stack-protector', '-ffp-contract=off', '-Wall', '-Wextra', '-Werror',
            '-Wno-unused-parameter', str(source), '-o', str(binary)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([str(binary)], capture_output=True, timeout=10)
        self.assertEqual(result.returncode, 0, 'retail-derived native candidate mismatch')
        type(self).native_cases += 192

    def test_profile_extents_and_instruction_identities(self):
        expected = {'o2': (2444, 2448, 344,
                          'be6bbb5a8e4181391a0436cbcfd74bbf079302e2541957c12be4ce03c5957f68'),
                    'o1': (2900, 2912, 272,
                          'd7d69b72a577328f17e6c68e0e2ecd5c80d1f852558f8e2e1aeded62fc34e4e0'),
                    'o2-no-unroll': (2212, 2224, 344,
                          '6176b7f3d6b6a18e6f047028631f598df1beb926fe333475feeae6b4f422d4cc')}
        self.assertEqual({profile: (row['body_bytes'], row['complete_text_bytes'],
                                   row['frame'], row['instruction_sha256'])
                          for profile, row in self.measurements.items()}, expected)
        self.assertTrue(all(not row['compiler_diagnostics'] for row in self.measurements.values()))
        self.assertLess(self.measurements['o2-no-unroll']['complete_text_bytes'], 2404)
        self.assertGreater(self.measurements['o2']['body_bytes'], 2404)
        self.assertNotEqual(self.measurements['o2-no-unroll']['frame'], 0x138)

    def test_retail_duplicate_words_have_no_reachable_entry(self):
        targets = set()
        indirect = []
        for index, word in enumerate(self.retail):
            pc = ENTRY + index * 4
            op, rs = word >> 26, word >> 21 & 31
            if op in (1, 4, 5, 6, 7, 20, 21) or op == 17 and rs == 8:
                immediate = word & 65535
                offset = immediate if immediate < 32768 else immediate - 65536
                targets.add(pc + 4 + offset * 4)
            elif op in (2, 3):
                targets.add((pc + 4 & 0xF0000000) | ((word & 0x3FFFFFF) << 2))
            elif op == 0 and word & 63 in (8, 9):
                indirect.append(pc)
        self.assertEqual(indirect, [0x1515E270])
        for address, expected in ((0x1515DC50, 0x8FAE0144), (0x1515E078, 0xA0C00004)):
            index = (address - ENTRY) // 4
            self.assertEqual(self.retail[index], expected)
            self.assertNotIn(address, targets)
            self.assertEqual(self.retail[index - 2] >> 16, 0x1000)
            self.assertNotEqual(address - 4 + (self.retail[index - 2] & 65535) * 4, address)

    def test_production_owner_is_not_replaced(self):
        source = (self.project / 'src/game/generated_18A8F0.c').read_text()
        self.assertIn('s32 func_1515D914() {\n    return 0;\n}', source)
        words = self.production['func_1515D914']
        self.assertEqual(len(words), 601)
        self.assertEqual(words[:3], [0x00001025, 0x03E00008, 0])
        self.assertIn('s32 distance;', self.source.read_text())
        self.assertNotIn('s32 distance =', self.source.read_text())


if __name__ == '__main__':
    unittest.main()
