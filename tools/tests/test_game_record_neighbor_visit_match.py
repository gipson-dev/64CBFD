"""Recursive visitor recovery and closed temporary lifetimes, not gameplay acceptance."""

import csv
import itertools
import math
import re
import struct
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.experiments import game_record_neighbor_visit_candidates as screen
from tools import pad_generated_object as pad
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK, native
from tools.tests.game_animation_timeline_oracle import bits, floating


ENTRY, GLOBAL, NODES, QUERY = screen.ENTRY, 0x800D2350, 0x90000, 0x30000
GUARDS = {0x30: (0x024F1021, 0x024F1821), 0x34: (0x90580036, 0x90780036),
          0x48: (0xA04A0036, 0xA06A0036), 0xF8: (0x308200FF, 0x308300FF),
          0xFC: (0x000258C3, 0x000358C3), 0x108: (0x304E0003, 0x306E0003)}
THRESHOLDS = (0, bits(25.0), 0x7F800000, 0x7FC00000)


def guarded(words, omitted=None):
    result = words[:]
    for offset, (expected, replacement) in GUARDS.items():
        assert result[offset // 4] == expected, ('stale visitor guard', offset)
        if offset != omitted:
            result[offset // 4] = replacement
    return result


def read(memory, address, size):
    return int.from_bytes(bytes(memory[address + i] for i in range(size)), 'big')


def signed_half(value):
    return value if value < 32768 else value - 65536


def graph_memory(seed=0, count=0, threshold=0, preset=0, query=QUERY, nodes=NODES):
    memory = {STACK + i: 0xA5 for i in range(-0x2000, 0x100)}
    memory.update({nodes + i: 0xA5 for i in range(256 * 16)})
    memory.update({query + i: 0xA5 for i in range(-16, 0x70)})
    put(memory, GLOBAL, nodes)
    for identity in range(256):
        point = nodes + identity * 16
        put(memory, point, (identity * 11 + seed * 3) % 101 - 50, 2)
        put(memory, point + 2, identity * 127 - 16000, 2)
        put(memory, point + 4, (identity * 7 + seed * 5) % 101 - 50, 2)
        for edge in range(5):
            neighbor = ((seed * 7 + identity * 3 + edge * 5) % 16
                        if identity < 16 and (seed + identity + edge) % 3 else 255)
            put(memory, point + 9 + edge, neighbor, 1)
    put(memory, query, bits(1.25))
    put(memory, query + 4, bits(-2.75))
    put(memory, query + 8, threshold)
    put(memory, query + 0x2C, count, 2)
    for offset in range(32):
        put(memory, query + 0x36 + offset, preset, 1)
    return memory


def leaf_memory(identity, count, profile):
    memory = graph_memory(count=count)
    x, z, qx, qz, threshold = (
        (3, 4, 0.0, 0.0, bits(24.0)), (3, 4, 0.0, 0.0, bits(25.0)),
        (-32768, 32767, 1.25, -2.75, bits(-1.0)), (0, 0, 0.0, -0.0, bits(-1.0)),
        (3, 4, math.inf, 0.0, 0x7F800000), (3, 4, math.nan, 0.0, 0),
        (3, 4, 0.0, 0.0, 0x7FC00000), (3, 4, 0.0, 0.0, 0xFF800000))[profile]
    point = NODES + identity * 16
    put(memory, point, x, 2)
    put(memory, point + 4, z, 2)
    for edge in range(5):
        put(memory, point + 9 + edge, 255, 1)
    put(memory, QUERY, bits(qx))
    put(memory, QUERY + 4, bits(qz))
    put(memory, QUERY + 8, threshold)
    # Map every possible payload address after an aliasing negative-count byte store.
    index = signed_half(count & 65535)
    for address in (QUERY + index + 0x2E, QUERY + index * 4 + 0xC):
        for i in range(-4, 8):
            memory.setdefault(address + i, 0xA5)
    if index in (-2, -1):
        changed = (identity << 8 | 254) if index == -2 else (0xFF00 | identity)
        address = QUERY + signed_half(changed) * 4 + 0xC
        for i in range(-4, 8):
            memory.setdefault(address + i, 0xA5)
    return memory


def reference(memory, identity, query=QUERY, mask=3, cached_count=False):
    memory, events = dict(memory), []

    def store(address, value, size):
        put(memory, address, value, size)
        events.append(('W', address, size, value & ((1 << (size * 8)) - 1)))

    def visit(identity, depth):
        assert depth < 256
        identity &= 255
        flag = query + 0x36 + (identity >> 3)
        store(flag, read(memory, flag, 1) | 1 << (identity & mask), 1)
        point = read(memory, GLOBAL, 4) + identity * 16
        x = floating(bits(float(signed_half(read(memory, point, 2))) - floating(read(memory, query, 4))))
        z = floating(bits(float(signed_half(read(memory, point + 4, 2))) - floating(read(memory, query + 4, 4))))
        distance = bits(floating(bits(x * x)) + floating(bits(z * z)))
        if floating(read(memory, query + 8, 4)) < floating(distance):
            count = signed_half(read(memory, query + 0x2C, 2))
            if count < 8:
                store(query + count + 0x2E, identity, 1)
                index = count if cached_count else signed_half(read(memory, query + 0x2C, 2))
                store(query + index * 4 + 0xC, distance, 4)
                index = count if cached_count else signed_half(read(memory, query + 0x2C, 2))
                store(query + 0x2C, index + 1, 2)
        else:
            for edge in range(5):
                neighbor = read(memory, point + 9 + edge, 1)
                if neighbor != 255 and not read(memory, query + 0x36 + (neighbor >> 3), 1) & (1 << (neighbor & mask)):
                    events.append(('CALL', ENTRY, (neighbor, query)))
                    visit(neighbor, depth + 1)

    visit(identity, 0)
    return memory, events


def external(events):
    return [e for e in events if e[0] == 'CALL' or not STACK - 0x2000 <= e[1] < STACK + 0x100]


class VisitorOracle(TriangleOracle):
    def __init__(self, words, memory, identity=0, phase=0, query=QUERY):
        super().__init__(words, memory, phase=phase, entry=ENTRY, arguments=(identity, query))
        self.query = query

    def record_call(self, target):
        assert target == ENTRY and self.r[5] == self.query
        self.calls.append((target, self.r[4], self.r[5]))
        self.events.append(('CALL', target, (self.r[4], self.r[5])))

    def hook(self, target):
        raise AssertionError(('unexpected opaque helper', target))


class GameRecordNeighborVisitMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-record-neighbor-visit-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        cls.retail = list(struct.unpack_from('>84I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0xB8758))
        cls.guarded = guarded(cls.raw)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def check_case(self, memory, identity, phase=0, query=QUERY):
        models = [VisitorOracle(words, memory, identity, phase, query).run()
                  for words in (self.retail, self.raw, self.guarded)]
        expected_memory, expected_events = reference(memory, identity, query)
        model = models[0]
        for other in models[1:]:
            self.assertEqual(external(other.events), external(model.events))
            self.assertEqual(other.memory, model.memory)
            self.assertEqual(other.calls, model.calls)
        self.assertEqual(external([e for e in model.events if e[0] != 'R']), expected_events)
        self.assertEqual({a: v for a, v in model.memory.items() if not STACK - 0x2000 <= a < STACK + 0x100},
                         {a: v for a, v in expected_memory.items() if not STACK - 0x2000 <= a < STACK + 0x100})
        return model

    def test_complete_frame_slot_and_two_closed_temporary_lifetimes(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['saved'],
                          self.record['real_differences'], self.record['diagnostics']),
                         (84, 0x30, [18, 20, 19, 17, 16], 6, ''))
        self.assertEqual(self.guarded, self.retail)
        normalized = self.raw[:]
        for first, end in ((0x30, 0x4C), (0xF8, 0x10C)):
            for offset in range(first, end, 4):
                word = normalized[offset // 4]
                fields = (21, 16, 11) if word >> 26 == 0 else (21, 16)
                for shift in fields:
                    if word >> shift & 31 == 2:
                        word = word & ~(31 << shift) | (3 << shift)
                normalized[offset // 4] = word
        self.assertEqual(normalized, self.retail)
        self.assertEqual({i * 4 for i, (a, b) in enumerate(zip(self.raw, self.retail)) if a != b}, set(GUARDS))

    def test_control_inventory_and_fail_closed_source_anchors(self):
        forms = screen.candidates()
        self.assertEqual((len(forms), len(dict(forms))), (24, 24))
        self.assertEqual(dict(forms)['typed-query-late-index'], screen.SELECTED)
        with self.assertRaises(ValueError):
            screen.replace(screen.BASELINE, 'missing source anchor', 'replacement')
        for name, expected in (('raw-byte-walk', (82, 57)), ('walker', (83, 29)),
                               ('walker-late-byte-index', (84, 7)), ('opaque-query-local', (84, 28))):
            record, _ = screen.compile_candidate(self.root, self.output, name, dict(forms)[name])
            self.assertEqual((record['body_words'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')

    def test_wrong_mask_missing_mark_wrong_plane_and_cached_count_controls_fail(self):
        cached = screen.replace(screen.SELECTED, '    f32 z;', '    f32 z;\n    s16 cachedCount;')
        cached = screen.replace(cached, '        if (query->count < 8)',
                                '        cachedCount = query->count;\n        if (cachedCount < 8)')
        cached = cached.replace('[query->count + 0x2E]', '[cachedCount + 0x2E]')
        cached = cached.replace('query->count * 4', 'cachedCount * 4')
        cached = screen.replace(cached, '(query->count)++;', 'query->count = cachedCount + 1;')
        for name, body, memory, identity in (
                ('wrong-mask', screen.SELECTED.replace('& 3', '& 7'), graph_memory(threshold=0x7F800000), 0),
                ('missing-mark', screen.replace(screen.SELECTED, '    query->visited[id >> 3] |= 1 << (id & 3);\n', ''),
                 leaf_memory(0, 0, 0), 0),
                ('wrong-plane', screen.replace(screen.SELECTED, '(node + 4)', '(node + 2)'), leaf_memory(0, 0, 1), 0),
                ('cached-count', cached, leaf_memory(1, -1, 0), 1)):
            record, words = screen.compile_candidate(self.root, self.output, name, body)
            self.assertEqual(record['diagnostics'], '')
            reference_model = VisitorOracle(self.retail, memory, identity).run()
            try:
                altered = VisitorOracle(words, memory, identity).run()
            except (AssertionError, KeyError):
                continue
            self.assertNotEqual(external(altered.events), external(reference_model.events), name)

    def test_strict_boundary_and_unordered_predicate_negative_controls_fail(self):
        for name, predicate, profile in (('inclusive-boundary', 'query->threshold <= z', 1),
                                          ('unordered-inverse', '!(query->threshold >= z)', 6)):
            body = screen.replace(screen.SELECTED, 'query->threshold < z', predicate)
            record, words = screen.compile_candidate(self.root, self.output, name, body)
            self.assertEqual(record['diagnostics'], '')
            memory = leaf_memory(0, 0, profile)
            original = VisitorOracle(self.retail, memory).run()
            altered = VisitorOracle(words, memory).run()
            self.assertNotEqual(external(altered.events), external(original.events))

    def test_all_entry_bytes_thresholds_capacity_and_upper_argument_bits(self):
        coverage = set()
        for identity, profile, phase in itertools.product(range(256), range(8), (0, 8)):
            count = (0, 7, 8, -1, -2, -32768, 32767, -256)[profile]
            model = self.check_case(leaf_memory(identity, count, profile), 0x1234AB00 | identity, phase)
            coverage.update(model.visits)
        self.leaf_coverage = coverage
        self.assertTrue(set(range(ENTRY, ENTRY + 0xEC, 4)) <= coverage)

    def test_recursive_graphs_cycles_collisions_and_full_instruction_coverage(self):
        coverage, cases = set(), 0
        for seed, identity, threshold, count, preset, phase in itertools.product(
                range(16), (0, 4, 128, 255), THRESHOLDS, (0, 7, 8), (0, 0xA5, 255), (0, 8)):
            model = self.check_case(graph_memory(seed, count, threshold, preset), identity, phase)
            coverage.update(model.visits)
            cases += 1
        self.assertEqual(cases, 4608)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 84 * 4, 4)))

    def test_retail_three_bit_bank_four_bit_mask_collision_and_count_aliases(self):
        memory = graph_memory(threshold=0x7F800000)
        for edge, neighbor in enumerate((4, 8, 255, 0, 8)):
            put(memory, NODES + 9 + edge, neighbor, 1)
        model = self.check_case(memory, 0)
        self.assertNotIn((ENTRY, 4, QUERY), model.calls)
        _, corrected = reference(memory, 0, mask=7)
        self.assertNotEqual(external([e for e in model.events if e[0] != 'R']), corrected)
        for identity, count, phase in itertools.product((0, 1, 127, 128, 255), (-2, -1), (0, 8)):
            memory = leaf_memory(identity, count, 0)
            model = self.check_case(memory, identity, phase)
            _, cached = reference(memory, identity, cached_count=True)
            if identity != 255:
                self.assertNotEqual(external([e for e in model.events if e[0] != 'R']), cached)
            else:
                self.assertEqual(external([e for e in model.events if e[0] != 'R']), cached)

    def test_signed_count_extremes_on_the_append_path(self):
        for identity, count, phase in itertools.product((0, 1, 127, 128, 254, 255),
                (-32768, -257, -256, -2, -1, 0, 1, 7, 8, 32767), (0, 8)):
            self.check_case(leaf_memory(identity, count, 0), identity, phase)

    def test_physical_visited_global_alias_reloads_and_cached_parent_walk(self):
        query = GLOBAL - 0x36
        memory = graph_memory(threshold=0x7F800000, query=query, nodes=0x80020000)
        # Marking nodes 0/8/16 changes successive bytes of the global table pointer.
        banks = (0x81020000, 0x81030000, 0x81030100)
        for bank in banks:
            for offset in range(4096):
                memory.setdefault(bank + offset, 0xA5)
        put(memory, GLOBAL, 0x80020000)
        for bank, identity in zip(banks, (0, 8, 16)):
            point = bank + identity * 16
            put(memory, point, 0, 2)
            put(memory, point + 4, 0, 2)
            for edge in range(5):
                put(memory, point + 9 + edge, 255, 1)
        put(memory, banks[0] + 9, 8, 1)
        put(memory, banks[0] + 10, 16, 1)
        for phase in (0, 8):
            model = self.check_case(memory, 0, phase, query)
            self.assertEqual(model.calls, [(ENTRY, 8, query), (ENTRY, 16, query)])
            self.assertEqual([value for a, size, value in model.reads if a == GLOBAL and size == 4], list(banks))

    def test_stale_guards_and_each_incomplete_lifetime_have_counterexamples(self):
        for offset in GUARDS:
            stale = self.raw[:]
            stale[offset // 4] ^= 1
            with self.assertRaisesRegex(AssertionError, 'stale visitor guard'):
                guarded(stale)
            failed = False
            for seed in range(16):
                memory = graph_memory(seed, threshold=0x7F800000)
                reference_model = VisitorOracle(self.retail, memory).run()
                try:
                    altered = VisitorOracle(guarded(self.raw, omitted=offset), memory).run()
                    failed |= external(altered.events) != external(reference_model.events)
                except (AssertionError, KeyError):
                    failed = True
                if failed:
                    break
            self.assertTrue(failed, hex(offset))

    def test_actual_guard_emitter_binds_words_and_empty_relocations(self):
        obj = self.output / 'selected.o'
        text, functions, relocations = pad.parse_object(obj)
        name = 'func_1508B2A8'
        start = functions[name]['value']
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = [r for r in csv.DictReader(stream) if r['function'] == name]
        self.assertEqual(len(rows), 6)
        for row in rows:
            offset = int(row['offset'], 0)
            self.assertEqual((int(row['expected'], 0), int(row['replacement'], 0)), GUARDS[offset])
            self.assertEqual(row['filename'], 'generated_B3020')
            self.assertEqual((row['expected_relocations'], row['replacement_relocations'],
                              row['insert_after'], row['insert_after_relocations'], row['omit']), ('-', '-', '', '', 'false'))
            self.assertEqual(relocations.get(start + offset, []), [])
        patches = pad.load_word_patches(self.root / 'conker/retail_word_patches.us.csv', 'generated_B3020')
        patches = {k: v for k, v in patches.items() if k[0] == name}
        with mock.patch.object(pad, 'parse_retail_slice', return_value=(ENTRY, ENTRY + 336, {name: ENTRY}, {})), \
                mock.patch.object(pad, 'load_word_patches', return_value=patches):
            self.assertEqual(pad.emit_padded_assembly(obj, self.root / 'conker/asm/B3020.s').count('.word '), 84)
            for offset in GUARDS:
                changed = bytearray(text)
                word = struct.unpack_from('>I', changed, start + offset)[0] ^ 1
                struct.pack_into('>I', changed, start + offset, word)
                with mock.patch.object(pad, 'parse_object', return_value=(bytes(changed), functions, relocations)):
                    with self.assertRaisesRegex(ValueError, 'stale word patch'):
                        pad.emit_padded_assembly(obj, self.root / 'conker/asm/B3020.s')
                shifted = dict(relocations)
                shifted[start + offset] = [('R_MIPS_HI16', 'D_800D2350')]
                with mock.patch.object(pad, 'parse_object', return_value=(text, functions, shifted)):
                    with self.assertRaisesRegex(ValueError, 'stale relocations'):
                        pad.emit_padded_assembly(obj, self.root / 'conker/asm/B3020.s')

    def test_native_query_layout_and_2304_reference_graph_footprints(self):
        rows = []
        for seed, identity, threshold, count, preset in itertools.product(
                range(16), (0, 4, 128, 255), THRESHOLDS, (0, 7, 8), (0, 0xA5, 255)):
            expected, _ = reference(graph_memory(seed, count, threshold, preset), identity)
            data = [expected[QUERY + i] for i in range(88)]
            for first in range(0, 44, 4):
                data[first:first + 4] = reversed(data[first:first + 4])
            data[44:46] = reversed(data[44:46])
            rows.append('{%d,%d,%d,0x%08X,%d,{%s}}' % (seed, identity, count, threshold, preset, ','.join(map(str, data))))
        source = (self.root / 'conker/src/game/generated_B3020.c').read_text()
        body = re.search(r'void func_1508B2A8\([^;{]*\{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body, screen.SELECTED)
        self.fixture = '''typedef unsigned char u8;typedef short s16;typedef int s32;
typedef unsigned int u32;typedef float f32;
''' + screen.QUERY + '\nu8 *D_800D2350;\n' + body + r'''
static union {u32 alignment;u8 bytes[4096];} nodes;
static union {u32 alignment;u8 bytes[96];} query;
static f32 number(u32 word) {union {u32 u;f32 f;} value;value.u=word;return value.f;}
static const struct {int seed,id,count;u32 threshold;int preset;u8 expected[88];} cases[]={
''' + ',\n'.join(rows) + '\n};\n'
        self.run_host(r'''
int c,i,e;
NeighborVisitQueryB3020 *q=(NeighborVisitQueryB3020 *)query.bytes;
if(sizeof(*q)!=88 || (u8 *)&q->count-query.bytes!=0x2C || q->visited-query.bytes!=0x36
   || q->ids-query.bytes!=0x2E || (u8 *)q->distances-query.bytes!=0xC) return 1;
for(c=0;c<2304;c++) {
 for(i=0;i<4096;i++) nodes.bytes[i]=0xA5;
 for(i=0;i<256;i++) {
  *(s16 *)(nodes.bytes+i*16)=(i*11+cases[c].seed*3)%101-50;
  *(s16 *)(nodes.bytes+i*16+2)=i*127-16000;
  *(s16 *)(nodes.bytes+i*16+4)=(i*7+cases[c].seed*5)%101-50;
  for(e=0;e<5;e++) nodes.bytes[i*16+9+e]=i<16 && (cases[c].seed+i+e)%3
       ? (cases[c].seed*7+i*3+e*5)%16 : 255;
 }
 for(i=0;i<96;i++) query.bytes[i]=0xA5;
 q->x=1.25f;q->z=-2.75f;q->threshold=number(cases[c].threshold);q->count=cases[c].count;
 for(i=0;i<32;i++) q->visited[i]=cases[c].preset;
 D_800D2350=nodes.bytes;func_1508B2A8(cases[c].id,q);
 if(D_800D2350!=nodes.bytes) return 6;
 for(i=0;i<88;i++) if(query.bytes[i]!=cases[c].expected[i]) return 2;
 for(i=88;i<96;i++) if(query.bytes[i]!=0xA5) return 3;
 for(i=0;i<256;i++) {
  if(*(s16 *)(nodes.bytes+i*16)!=(i*11+cases[c].seed*3)%101-50
     || *(s16 *)(nodes.bytes+i*16+2)!=i*127-16000
     || *(s16 *)(nodes.bytes+i*16+4)!=(i*7+cases[c].seed*5)%101-50) return 4;
  for(e=0;e<5;e++) if(nodes.bytes[i*16+9+e]!=(i<16 && (cases[c].seed+i+e)%3
      ? (cases[c].seed*7+i*3+e*5)%16 : 255)) return 5;
  for(e=6;e<16;e++) if((e<9 || e>13) && nodes.bytes[i*16+e]!=0xA5) return 7;
 }
}
''')

    def test_production_source_slot_prototype_and_existing_profile(self):
        source = (self.root / 'conker/src/game/generated_B3020.c').read_text()
        body = re.search(r'void func_1508B2A8\([^;{]*\{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body, screen.SELECTED)
        self.assertIn(screen.QUERY, source)
        header = (self.root / 'conker/include/functions.h').read_text()
        self.assertIn('struct NeighborVisitQueryB3020;', header)
        self.assertIn('void func_1508B2A8(u8, struct NeighborVisitQueryB3020 *);', header)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                     'mips-linux-gnu-objdump')
        self.assertEqual(functions['func_1508B2A8'], self.retail)
        self.assertEqual(addresses['func_1508B3F8'], 0x1508B3F8)
        self.assertNotIn('__retail_overflow_func_1508B2A8', functions)
        record, words = screen.compile_candidate(self.root, self.output, 'default-profile', screen.SELECTED,
                                                 no_unroll=False)
        self.assertEqual((record['body_words'], record['real_differences'], record['diagnostics']), (84, 6, ''))
        self.assertEqual(words, self.raw)


if __name__ == '__main__':
    unittest.main()
