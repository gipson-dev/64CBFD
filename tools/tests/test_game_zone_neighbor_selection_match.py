"""Complete zone pass with connected retail visitor; opaque height/root lookup."""

import itertools
import csv
import math
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_zone_neighbor_selection_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_record_neighbor_visit_match import read, reference as visit_reference
from tools.tests.test_game_table_range_loader import STACK, native
from tools.tests.game_animation_timeline_oracle import bits, floating, signed


ENTRY = screen.ENTRY
GLOBAL, COUNT, START, ACTORS, NODES, MINIMUM = (screen.SYMBOLS[n] for n in
    ('D_800D23B0', 'D_8008FD8C', 'D_8008FD90', 'D_800CC2D0', 'D_800D2350', 'D_8009DA5C'))
STATE, TABLE, PRIVATE = 0x20000, 0x90000, STACK - 0x400
ALT_STATE, ALT_TABLE = 0x26000, 0xA0000
HEIGHT, ROOT, ZERO, VISITOR = (screen.SYMBOLS[n] for n in
    ('func_15085DA8', 'func_15085DF8', 'bzero', 'func_1508B2A8'))


def byte_signed(value):
    return value if value < 128 else value - 256


def case_memory(seed=0, count=4, start=0, zones=2, pattern=0, radius=0, bound=0):
    memory = {STACK + i: 0xA5 for i in range(-0x2000, 0x100)}
    for address, size in ((STATE, 0x1900), (ACTORS - 0x32C, 9 * 0x32C), (TABLE, 4096)):
        memory.update({address + i: 0xA5 for i in range(size)})
    for address, value, size in ((GLOBAL, STATE, 4), (NODES, TABLE, 4),
            (COUNT, count, 1), (START, start, 1), (MINIMUM, bits(1.0e10), 4),
            (STATE + 0x1745, zones, 1)):
        put(memory, address, value, size)
    for i in range(8):
        put(memory, STATE + 0x55C + i * 4, (-1, 10, -5, 0)[(pattern + i) % 4])
        put(memory, STATE + 0x5C + i * 4, 0x12345678 + i)
        x, y, z = ((i * 3 + seed) % 15 - 7, (0, -100, 200, -99.5, 199.5, math.nan)[bound], 0)
        if pattern == 4:
            x = math.nan
        for offset, value in ((0x14, x), (0x18, y), (0x1C, z)):
            put(memory, ACTORS + i * 0x32C + offset, bits(value))
    for i in range(8):
        point = STATE + 0x1748 + i * 12
        put(memory, point, (bits(-1.0), bits(0.0), bits(25.0), 0x7FC00000, 0x7F800000)[radius])
        put(memory, point + 4, i * 2 - 1, 2)
        put(memory, point + 6, 0, 2)
        put(memory, point + 8, 0, 2)
    for i in range(256):
        point = TABLE + i * 16
        put(memory, point, (i * 11 + seed * 3) % 101 - 50, 2)
        put(memory, point + 2, i * 127 - 16000, 2)
        put(memory, point + 4, (i * 7 + seed * 5) % 101 - 50, 2)
        put(memory, point + 7, (i * 13 + seed) & 255, 1)
        for edge in range(5):
            neighbor = ((seed * 7 + i * 3 + edge * 5) % 16
                        if i < 16 and (seed + i + edge) % 3 else 255)
            put(memory, point + 9 + edge, neighbor, 1)
    return memory


def wide_memory(amount=8, pattern=0, actor_x=2.0, phase_radius=25.0):
    memory = case_memory(count=4, zones=2, pattern=pattern, radius=2)
    candidates = (1, 2, 3, 8, 9, 10, 11, 16)[:amount]
    for i in range(256):
        for edge in range(5):
            put(memory, TABLE + i * 16 + 9 + edge, 255, 1)
    for identity in (0, 24):
        put(memory, TABLE + identity * 16, -1, 2)
        put(memory, TABLE + identity * 16 + 4, 0, 2)
    edges = candidates if amount <= 5 else (*candidates[:4], 24)
    for edge, identity in enumerate(edges):
        put(memory, TABLE + 9 + edge, identity, 1)
    if amount > 5:
        for edge, identity in enumerate(candidates[4:]):
            put(memory, TABLE + 24 * 16 + 9 + edge, identity, 1)
    for i, identity in enumerate(candidates):
        put(memory, TABLE + identity * 16, 6 + amount - i, 2)
        put(memory, TABLE + identity * 16 + 4, 0, 2)
    for i in range(4):
        put(memory, ACTORS + i * 0x32C + 0x14, bits(actor_x + i))
    for i in range(2):
        put(memory, STATE + 0x1748 + i * 12, bits(phase_radius))
        put(memory, STATE + 0x174C + i * 12, -1, 2)
    return memory


def external_writes(model):
    return [e for e in model.events if e[0] == 'W' and not STACK - 0x2000 <= e[1] < STACK + 0x100]


def external_memory(memory):
    return {a: b for a, b in memory.items() if not STACK - 0x2000 <= a < STACK + 0x100}


def f32(value):
    return floating(bits(value))


def mutation(memory, call, mode):
    actions = []
    if call == 0:
        if mode & 1:
            actions.append((COUNT, 2, 1))
        if mode & 2:
            actions.append((STATE + 0x1745, 1, 1))
        if mode & 4:
            actions.append((ACTORS + 0x32C + 0x14, bits(2.0), 4))
        if mode & 8:
            actions.append((MINIMUM, bits(0.0), 4))
        if mode & 16:
            actions.append((STATE + 0x55C, -1, 4))
        if mode & 32:
            actions.append((TABLE + 7, 201, 1))
        if mode & 64:
            actions.append((GLOBAL, ALT_STATE, 4))
        if mode & 128:
            actions.append((NODES, ALT_TABLE, 4))
    for address, value, size in actions:
        put(memory, address, value, size)
    return [('W', address, size, value & ((1 << (size * 8)) - 1)) for address, value, size in actions]


def reference(memory, roots=(0, 8), mode=0, inclusive=False, repeat=False, clear=False):
    memory, calls, writes = dict(memory), [], []
    lookup = 0

    def store(address, value, size=4):
        put(memory, address, value, size)
        writes.append(('W', address, size, value & ((1 << (size * 8)) - 1)))

    state = read(memory, GLOBAL, 4)
    selections = state + 0x55C
    zone = state + 0x1748
    i = 0
    while i < byte_signed(read(memory, COUNT, 1)):
        address = selections + i * 4
        if signed(read(memory, address, 4)) != -1:
            store(address, -2)
        i += 1
    i = 0
    while i < byte_signed(read(memory, read(memory, GLOBAL, 4) + 0x1745, 1)):
        threshold = read(memory, zone, 4)
        x, y, z = (float((v if v < 32768 else v - 65536))
                   for v in (read(memory, zone + offset, 2) for offset in (4, 6, 8)))
        ready, query = False, PRIVATE
        player = byte_signed(read(memory, START, 1))
        while player < byte_signed(read(memory, COUNT, 1)):
            actor = ACTORS + player * 0x32C
            height = f32(floating(read(memory, actor + 0x18, 4)) - y)
            if height < 200.0 and -100.0 < height:
                dx = f32(floating(read(memory, actor + 0x14, 4)) - x)
                dz = f32(floating(read(memory, actor + 0x1C, 4)) - z)
                distance = f32(f32(dx * dx) + f32(dz * dz))
                if distance < f32(floating(threshold) + 100.0):
                    best, minimum = 255, floating(read(memory, MINIMUM, 4))
                    if not ready or repeat:
                        put(memory, query + 8, threshold)
                        put(memory, query + 0x2C, 0, 2)
                        ready = True
                        calls.append((HEIGHT, bits(y)))
                        calls.append((ROOT, bits(x), bits(y), bits(z), 0, 17))
                        writes.extend(mutation(memory, lookup, mode))
                        root = roots[lookup % len(roots)] & 0xFFFFFFFF
                        lookup += 1
                        if root != 0xFFFFFFFF:
                            put(memory, query, bits(x))
                            put(memory, query + 4, bits(z))
                            calls.append((ZERO, 32))
                            for k in range(32):
                                put(memory, query + 0x36 + k, 0, 1)
                            calls.append((VISITOR, root & 255))
                            memory, events = visit_reference(memory, root, query)
                            calls.extend((VISITOR, e[2][0]) for e in events if e[0] == 'CALL')
                    nodes = read(memory, NODES, 4)
                    ax, az = (floating(read(memory, actor + offset, 4)) for offset in (0x14, 0x1C))
                    count = read(memory, query + 0x2C, 2)
                    count = count if count < 32768 else count - 65536
                    for j in range(max(0, count)):
                        identity = read(memory, query + 0x2E + j, 1)
                        point = nodes + identity * 16
                        nx, nz = (float(v if v < 32768 else v - 65536)
                                  for v in (read(memory, point + offset, 2) for offset in (0, 4)))
                        dx, dz = f32(nx - ax), f32(nz - az)
                        distance = f32(f32(dx * dx) + f32(dz * dz))
                        limit = floating(read(memory, query + 0xC + j * 4, 4))
                        accept = distance <= limit and distance <= minimum if inclusive else distance < limit and distance < minimum
                        if accept:
                            best, minimum = identity, distance
                    if best != 255:
                        point = read(memory, NODES, 4) + best * 16
                        address = selections + player * 4
                        if signed(read(memory, address, 4)) != -2:
                            store(read(memory, GLOBAL, 4) + player * 4 + 0x5C, 1)
                        store(address, read(memory, point + 7, 1))
            player += 1
        zone += 12
        i += 1
    i = 0
    while i < byte_signed(read(memory, COUNT, 1)):
        address = selections + i * 4
        if signed(read(memory, address, 4)) < 0:
            store(address, -1)
        i += 1
    if not clear:
        store(read(memory, GLOBAL, 4) + 0x1745, 0, 1)
    return memory, calls, writes


class ZoneOracle(TriangleOracle):
    def __init__(self, words, memory, visitor, phase=0, roots=(0, 8), mode=0):
        connected = {VISITOR + i * 4: w for i, w in enumerate(visitor)}
        super().__init__(words, memory, phase=phase, connected=connected, entry=ENTRY, arguments=())
        self.roots, self.mode, self.lookup = roots, mode, 0

    def execute(self, word):
        if word >> 26 == 32:
            rs, rt, immediate = word >> 21 & 31, word >> 16 & 31, word & 65535
            address = (self.r[rs] + (immediate if immediate < 32768 else immediate - 65536)) & 0xFFFFFFFF
            self.r[rt] = byte_signed(self.get(address, 1)) & 0xFFFFFFFF
            self.r[0] = 0
        else:
            super().execute(word)

    def record_call(self, target):
        if target == HEIGHT:
            args = (self.f[12],)
        elif target == ROOT:
            args = (self.f[12], self.f[14], self.r[6], self.r[7], self.get(self.r[29] + 0x10, 4))
        elif target == ZERO:
            self.assert_private(self.r[4], 32)
            args = (self.r[5],)
        else:
            assert target == VISITOR, hex(target)
            self.assert_private(self.r[5], 86)
            args = (self.r[4] & 255,)
        self.calls.append((target, *args))

    def assert_private(self, address, length):
        assert STACK - 0x2000 <= address and address + length <= self.before[29], (hex(address), length)

    def hook(self, target):
        result = 0
        if target == HEIGHT:
            result = 17
        elif target == ROOT:
            for _, address, size, value in mutation(dict(self.memory), self.lookup, self.mode):
                self.put(address, value, size)
            result = self.roots[self.lookup % len(self.roots)] & 0xFFFFFFFF
            self.lookup += 1
        else:
            assert target == ZERO and self.r[5] == 32
            for i in range(32):
                self.put(self.r[4] + i, 0, 1)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.r[2] = result


class GameZoneNeighborSelectionMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-zone-neighbor-selection-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        _, cls.baseline = screen.compile_candidate(cls.root, cls.output, 'baseline', screen.BASELINE)
        _, cls.checkpoint = screen.compile_candidate(cls.root, cls.output, 'checkpoint', screen.CHECKPOINT)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>369I', rom, 0xB88A8))
        cls.visitor = list(struct.unpack_from('>84I', rom, 0xB8758))
        cls.coverage, cls.visitor_coverage, cls.cases = set(), set(), 0
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def check_case(self, memory, phase=0, roots=(0, 8), mode=0):
        expected_memory, calls, writes = reference(memory, roots, mode)
        models = [ZoneOracle(words, memory, self.visitor, phase, roots, mode).run()
                  for words in (self.retail, self.words, self.baseline, self.checkpoint)]
        for model in models:
            self.assertEqual(model.calls, calls)
            self.assertEqual(external_writes(model), writes)
            self.assertEqual(external_memory(model.memory), external_memory(expected_memory))
        type(self).coverage.update(models[0].visits & set(range(ENTRY, ENTRY + 369 * 4, 4)))
        type(self).visitor_coverage.update(models[0].visits & set(range(VISITOR, VISITOR + 84 * 4, 4)))
        type(self).cases += 1
        return models[0]

    def test_bounded_connected_smoke_and_root_failure(self):
        for seed, roots, phase in itertools.product(range(4), ((0, 8), (-1,), (255,),
                                                             (256, 0x1234AB00), (-2, 255)), (0, 8)):
            self.check_case(case_memory(seed), phase, roots)

    def test_signed_queue_and_player_bounds(self):
        for count, start, zones, phase in itertools.product((-128, -1, 0, 1, 4, 8), (-1, 0, 1, 4, 8, 127),
                                                          (-128, -1, 0, 1, 4, 8), (0, 8)):
            self.check_case(case_memory(count=count, start=start, zones=zones), phase)

    def test_height_radial_unordered_and_selection_boundaries(self):
        for seed, pattern, radius, bound, phase in itertools.product(range(4), range(5), range(5), range(6), (0, 8)):
            self.check_case(case_memory(seed, pattern=pattern, radius=radius, bound=bound), phase)

    def test_lookup_mutations_of_future_work_and_publication(self):
        for seed, mode, roots, phase in itertools.product(range(4), range(64), ((0, 8), (-1, 0)), (0, 8)):
            self.check_case(case_memory(seed), phase, roots, mode)

    def test_every_candidate_count_remainder_and_four_way_scan(self):
        coverage, visitor_coverage = set(), set()
        for amount, pattern, actor_x, phase in itertools.product(range(1, 9), range(4),
                                                               (-1.0, 2.0, 6.0, 10.0), (0, 8)):
            model = self.check_case(wide_memory(amount, pattern, actor_x), phase, (0,))
            coverage.update(model.visits)
            visitor_coverage.update(model.visits)
        for count, zones, start, roots in ((0, 0, 0, (-1,)), (4, 0, 0, (-1,)),
                                           (4, 1, 8, (-1,)), (4, 1, 0, (-1,))):
            model = self.check_case(case_memory(count=count, zones=zones, start=start), roots=roots)
            coverage.update(model.visits)
        memory = wide_memory(8)
        for identity in (1, 2, 3, 8, 9, 10, 11, 16):
            put(memory, TABLE + identity * 16, 7, 2)
        model = self.check_case(memory, roots=(0,))
        coverage.update(model.visits)
        memory = wide_memory(6)
        put(memory, TABLE + 24 * 16 + 13, 0, 1)
        model = self.check_case(memory, roots=(0,))
        visitor_coverage.update(model.visits)
        self.assertTrue(set(range(ENTRY, ENTRY + 369 * 4, 4)) <= coverage,
                        sorted(set(range(ENTRY, ENTRY + 369 * 4, 4)) - coverage))
        self.assertEqual(visitor_coverage & set(range(VISITOR, VISITOR + 84 * 4, 4)),
                         set(range(VISITOR, VISITOR + 84 * 4, 4)))

    def test_mutated_global_bases_keep_original_selection_and_zone_cursors(self):
        for amount, mode, phase in itertools.product((1, 4, 8), (64, 128, 192), (0, 8)):
            memory = wide_memory(amount)
            memory.update({ALT_STATE + i: memory[STATE + i] for i in range(0x1900)})
            memory.update({ALT_TABLE + i: memory[TABLE + i] for i in range(4096)})
            put(memory, ALT_STATE + 0x1745, 1, 1)
            for i in range(256):
                put(memory, ALT_TABLE + i * 16 + 7, (i + 99) & 255, 1)
            self.check_case(memory, phase, (0,), mode)

    def test_strict_equal_candidate_distance_and_first_tie_winner(self):
        memory = wide_memory(2, pattern=0)
        put(memory, TABLE + 1 * 16, 7, 2)
        put(memory, TABLE + 2 * 16, 7, 2)
        put(memory, COUNT, 1, 1)
        put(memory, STATE + 0x1745, 1, 1)
        selected = self.check_case(memory, roots=(0,))
        self.assertEqual(read(selected.memory, STATE + 0x55C, 4), 13)
        equal = dict(memory)
        put(equal, ACTORS + 0x14, bits(-1.0))
        rejected = self.check_case(equal, roots=(0,))
        self.assertEqual(read(rejected.memory, STATE + 0x55C, 4), 0xFFFFFFFF)

    def test_minimum_unordered_and_signed_floating_bounds(self):
        for minimum, phase in itertools.product((0, bits(1.0), bits(25.0),
                                                0x7F800000, 0xFF800000, 0x7FC00000), (0, 8)):
            memory = wide_memory(8)
            put(memory, MINIMUM, minimum)
            self.check_case(memory, phase, (0,))

    def test_root_reuse_and_clear_queue_negative_controls_fail(self):
        for name, body in (
                ('repeat-query', screen.SELECTED.replace('if (!ready)', 'if (1)')),
                ('missing-queue-clear', screen.SELECTED.replace(
                    '    *(s8 *)((u8 *)D_800D23B0 + 0x1745) = 0;\n', '')),
                ('inclusive-distance', screen.SELECTED.replace('dz < context->distances[j]', 'dz <= context->distances[j]')
                    .replace('dz < *(f32 *)(distances', 'dz <= *(f32 *)(distances')
                    .replace('dz < minimum', 'dz <= minimum'))):
            self.assertNotEqual(body, screen.SELECTED)
            record, words = screen.compile_candidate(self.root, self.output, name, body)
            self.assertEqual(record['diagnostics'], '')
            memory = wide_memory(2, actor_x=-1.0) if name == 'inclusive-distance' else wide_memory()
            old = ZoneOracle(self.retail, memory, self.visitor, roots=(0,)).run()
            new = ZoneOracle(words, memory, self.visitor, roots=(0,)).run()
            self.assertNotEqual((new.calls, external_writes(new), external_memory(new.memory)),
                                (old.calls, external_writes(old), external_memory(old.memory)), name)

    def test_native_1424_complete_public_memory_footprints(self):
        rows = []
        for seed, count, start, zones, radius, root_mode in itertools.product(
                range(4), (0, 1, 4, 8), (0, 1, 4), (0, 1, 2), (0, 2, 3), range(3)):
            roots = ((0, 8), (-1,), (255,))[root_mode]
            expected, calls, _ = reference(case_memory(seed, count, start, zones, radius=radius), roots)
            digest = 2166136261
            for call in calls:
                for value in call:
                    digest = ((digest ^ value) * 16777619) & 0xFFFFFFFF
            words = [read(expected, STATE + offset + i * 4, 4) for offset in (0x55C, 0x5C) for i in range(8)]
            rows.append('{%s,0,0,0,0x%08X,{%s}}' % (','.join(map(str, (seed, count, start, zones, radius, root_mode))),
                        digest, ','.join('0x%08X' % word for word in words)))
        for amount, pattern, actor_x in itertools.product(range(1, 9), range(4), (-1.0, 2.0, 6.0, 10.0)):
            expected, calls, _ = reference(wide_memory(amount, pattern, actor_x), (0,))
            digest = 2166136261
            for call in calls:
                for value in call:
                    digest = ((digest ^ value) * 16777619) & 0xFFFFFFFF
            words = [read(expected, STATE + offset + i * 4, 4) for offset in (0x55C, 0x5C) for i in range(8)]
            rows.append('{0,4,0,2,2,3,%d,%d,0x%08X,0x%08X,{%s}}' %
                        (amount, pattern, bits(actor_x), digest,
                         ','.join('0x%08X' % word for word in words)))
        source = (self.root / 'conker/src/game/generated_B3020.c').read_text()
        visitor = re.search(r'void func_1508B2A8\([^;{]*\{\n.*?\n\}', source, re.S).group()
        body = re.search(r'void func_1508B3F8\([^;{]*\{\n.*?\n\}', source, re.S).group()
        self.assertEqual(body, screen.SELECTED)
        visitor = visitor.replace('void func_1508B2A8(', 'static void visitorBody(', 1)
        self.fixture = '''typedef unsigned char u8;typedef signed char s8;
typedef short s16;typedef int s32;typedef unsigned int u32;typedef float f32;
''' + screen.QUERY + '\n' + screen.DECLARATIONS + r'''
static union {u32 align;u8 bytes[0x1900];} state;
static union {u32 align;u8 bytes[4096];} nodes;
u8 D_800CC2D0[8*0x32C];s32 D_800D23B0;u8 *D_800D2350;
s8 D_8008FD8C,D_8008FD90;f32 D_8009DA5C;
static int lookup,rootMode;static u32 digest;
static f32 number(u32 word) {union {u32 u;f32 f;} v;v.u=word;return v.f;}
static u32 word(f32 value) {union {u32 u;f32 f;} v;v.f=value;return v.u;}
static void logWord(u32 value) {digest=(digest^value)*16777619;}
s32 func_15085DA8(f32 y) {logWord(0x15085DA8);logWord(word(y));return 17;}
s32 func_15085DF8(f32 x,f32 y,f32 z,s8 mode,s8 band) {
 logWord(0x15085DF8);logWord(word(x));logWord(word(y));logWord(word(z));
 logWord(mode);logWord(band);
 return rootMode==1?-1:rootMode==2?255:rootMode==3?0:(lookup++%2?8:0);
}
void bzero(void *pointer,int count) {u8 *out=pointer;int i;
 logWord(0x100226F0);logWord(count);for(i=0;i<count;i++) out[i]=0;
}
''' + visitor + r'''
void func_1508B2A8(u8 id,NeighborVisitQueryB3020 *query) {
 logWord(0x1508B2A8);logWord(id);visitorBody(id,query);
}
''' + body + r'''
static const struct {int seed,count,start,zones,radius,rootMode,amount,pattern;u32 actorX,digest,output[16];} cases[]={
''' + ',\n'.join(rows) + '\n};\n'
        self.run_host(r'''
static u8 expected[0x1900],oldNodes[4096],oldActors[8*0x32C];
static u32 radii[]={0xBF800000,0,0x41C80000,0x7FC00000,0x7F800000};
static int selections[]={-1,10,-5,0};
static int candidates[]={1,2,3,8,9,10,11,16};
int c,i,e,id,amount;u8 *p;
for(c=0;c<1424;c++) {
 for(i=0;i<0x1900;i++) state.bytes[i]=0xA5;
 for(i=0;i<4096;i++) nodes.bytes[i]=0xA5;
 for(i=0;i<8*0x32C;i++) D_800CC2D0[i]=0xA5;
 D_800D23B0=(s32)state.bytes;D_800D2350=nodes.bytes;
 D_8008FD8C=cases[c].count;D_8008FD90=cases[c].start;D_8009DA5C=1.0e10f;
 state.bytes[0x1745]=cases[c].zones;
 for(i=0;i<8;i++) {
  *(s32 *)(state.bytes+0x55C+i*4)=selections[(cases[c].pattern+i)%4];
  *(u32 *)(state.bytes+0x5C+i*4)=0x12345678+i;
  *(f32 *)(D_800CC2D0+i*0x32C+0x14)=cases[c].amount && i<4
      ? number(cases[c].actorX)+i : (i*3+cases[c].seed)%15-7;
  *(f32 *)(D_800CC2D0+i*0x32C+0x18)=0;
  *(f32 *)(D_800CC2D0+i*0x32C+0x1C)=0;
  p=state.bytes+0x1748+i*12;
  *(f32 *)p=number(radii[cases[c].radius]);
  *(s16 *)(p+4)=cases[c].amount && i<2 ? -1 : i*2-1;
  *(s16 *)(p+6)=0;*(s16 *)(p+8)=0;
 }
 for(i=0;i<256;i++) {
  p=nodes.bytes+i*16;*(s16 *)p=(i*11+cases[c].seed*3)%101-50;
  *(s16 *)(p+2)=i*127-16000;*(s16 *)(p+4)=(i*7+cases[c].seed*5)%101-50;
  p[7]=(i*13+cases[c].seed)&255;
  for(e=0;e<5;e++) p[9+e]=i<16 && (cases[c].seed+i+e)%3 ? (cases[c].seed*7+i*3+e*5)%16 : 255;
 }
 amount=cases[c].amount;
 if(amount) {
  for(i=0;i<256;i++) for(e=0;e<5;e++) nodes.bytes[i*16+9+e]=255;
  *(s16 *)nodes.bytes=-1;*(s16 *)(nodes.bytes+4)=0;
  *(s16 *)(nodes.bytes+24*16)=-1;*(s16 *)(nodes.bytes+24*16+4)=0;
  for(e=0;e<(amount<=5?amount:5);e++) nodes.bytes[9+e]=amount>5 && e==4 ? 24 : candidates[e];
  if(amount>5) for(e=0;e<amount-4;e++) nodes.bytes[24*16+9+e]=candidates[e+4];
  for(i=0;i<amount;i++) {
   id=candidates[i];*(s16 *)(nodes.bytes+id*16)=6+amount-i;*(s16 *)(nodes.bytes+id*16+4)=0;
  }
 }
 for(i=0;i<0x1900;i++) expected[i]=state.bytes[i];
 for(i=0;i<8;i++) {
  *(u32 *)(expected+0x55C+i*4)=cases[c].output[i];
  *(u32 *)(expected+0x5C+i*4)=cases[c].output[i+8];
 }
 expected[0x1745]=0;
 for(i=0;i<4096;i++) oldNodes[i]=nodes.bytes[i];
 for(i=0;i<8*0x32C;i++) oldActors[i]=D_800CC2D0[i];
 digest=2166136261;lookup=0;rootMode=cases[c].rootMode;
 func_1508B3F8();
 if(digest!=cases[c].digest) return 1;
 if(D_800D23B0!=(s32)state.bytes || D_800D2350!=nodes.bytes
    || D_8008FD8C!=cases[c].count || D_8008FD90!=cases[c].start
    || word(D_8009DA5C)!=word(1.0e10f)) return 2;
 for(i=0;i<0x1900;i++) if(state.bytes[i]!=expected[i]) return 3;
 for(i=0;i<4096;i++) if(nodes.bytes[i]!=oldNodes[i]) return 4;
 for(i=0;i<8*0x32C;i++) if(D_800CC2D0[i]!=oldActors[i]) return 5;
}
''')

    def test_compiler_inventory_complete_body_and_fitting_contract(self):
        forms = screen.candidates()
        self.assertEqual((len(forms), len(dict(forms))), (29, 29))
        self.assertEqual(screen.CHECKPOINT, dict(forms)['retail-byte-cursors'])
        self.assertEqual(screen.SELECTED, screen.retain_query_pointer(screen.CHECKPOINT))
        self.assertEqual((self.record['body_words'], self.record['frame'],
                          self.record['real_differences'], self.record['diagnostics']), (369, 0x140, 282, ''))
        self.assertEqual(len(self.words), 369)
        for name, expected in (('indexed', (249, 0x138, 333)),
                               ('explicit-four-candidates', (371, 0x140, 323)),
                               ('retail-remainder-z-reuse', (370, 0x140, 257))):
            record, _ = screen.compile_candidate(self.root, self.output, name, dict(forms)[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')

    def test_production_source_complete_padded_slot_and_unchanged_next_symbol(self):
        source = (self.root / 'conker/src/game/generated_B3020.c').read_text()
        body = re.search(r'void func_1508B3F8\([^;{]*\{\n.*?\n\}', source, re.S).group()
        self.assertEqual(body, screen.SELECTED)
        self.assertIn('void func_1508B3F8(void);', (self.root / 'conker/include/functions.h').read_text())
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                     'mips-linux-gnu-objdump')
        self.assertEqual(functions['func_1508B3F8'], self.words)
        self.assertEqual((addresses['func_1508B3F8'], addresses['func_1508B9BC']), (ENTRY, 0x1508B9BC))
        self.assertNotIn('__retail_overflow_func_1508B3F8', functions)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse(any(row['function'] == 'func_1508B3F8' for row in csv.DictReader(stream)))

    def test_lookup_body_now_matches_retail_instead_of_its_placeholder(self):
        from tools.experiments import game_root_neighbor_lookup_candidates as lookup

        record, words = lookup.compile_candidate(self.root, self.output, 'root-lookup', lookup.SELECTED)
        functions, _, _ = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                             'mips-linux-gnu-objdump')
        self.assertEqual((record['body_words'], record['frame'], record['real_differences']), (168, 0x80, 0))
        self.assertEqual(functions['func_15085DF8'], words)

    def test_branch_likely_sign_gates_annul_delay_when_not_taken(self):
        # Branch over an increment when taken; annul its delay when not taken.
        for opcode, value in itertools.product((22, 23), (0, 1, 0xFFFFFFFF, 0x80000000)):
            words = [(opcode << 26) | (4 << 21) | 2, 0x24A50001, 0x24A50002,
                     0x03E00008, 0]
            model = TriangleOracle(words, case_memory(), entry=ENTRY, arguments=(value, 10)).run()
            take = signed(value) <= 0 if opcode == 22 else signed(value) > 0
            self.assertEqual(model.r[5], 11 if take else 12)


if __name__ == '__main__':
    unittest.main()
