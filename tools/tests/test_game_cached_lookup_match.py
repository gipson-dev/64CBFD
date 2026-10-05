"""Cached lookup guards with connected installer code and bounded DMA/copy hooks."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import unittest
from pathlib import Path

from tools.experiments import game_cached_lookup_candidates as screen
from tools.tests import test_game_cache_installer_match as installer
from tools.tests import test_game_asset_table_lookup_and_block_load as asset
from tools.tests.test_game_queued_segment_writer import SegmentQueueOracle, STACK
from tools.tests.test_game_viewport_renderer import RendererOracle
from tools.tests.game_animation_timeline_oracle import TimelineOracle
from tools.match_progress import load_elf_functions


ENTRY, CACHE, CLOCK, OUTPUT = 0x1502AC88, 0x800C3D68, 0x800C3D60, 0x20000
INSTALL, DMA, COPY = 0x1502AB04, 0x10004514, 0x10023A10
GUARDS = {
    0x200: (0x27AA006F, 0x27AB0068),
    0x204: (0x320C000E, 0x320A000E),
    0x208: (0x258D001F, 0x254C001F),
    0x20C: (0x01422824, 0x01622824),
    0x224: (0x01A23024, 0x01823024),
    0x230: (0x8FAF0034, 0x8FAD0034),
    0x238: (0x8FAB00A8, 0x8FB900A8),
    0x23C: (0x01CF2821, 0x01AE2821),
    0x240: (0x8CB80000, 0x8CAF0000),
    0x24C: (0xAFB80058, 0xAFAF0058),
    0x250: (0x8CB90004, 0x8CB80004),
    0x258: (0xAD790000, 0xAF380000),
}


def source_body():
    return dict(screen.candidates())['ordered-locals']


def apply_linked_guards(words, omitted=None):
    result = words[:]
    for offset, (expected, replacement) in GUARDS.items():
        assert result[offset // 4] == expected
        if offset != omitted:
            result[offset // 4] = replacement
    return result


def put_word(memory, address, value):
    memory.update({address + i: byte for i, byte in enumerate(struct.pack('>I', value & 0xFFFFFFFF))})


def memory_case(pattern, address, hit=None):
    memory = {STACK + i: 0xA5 for i in range(-0x180, 0xC0)}
    memory.update({CACHE + i: 0xA5 for i in range(-16, 272)})
    memory.update({OUTPUT + i: 0xA5 for i in range(-16, 20)})
    for i in range(64):
        put_word(memory, CACHE + i * 4, 0x90000000 + i * 17 + pattern * 0x13579B)
    put_word(memory, CLOCK, (0, 0xFFFFFFFF, 0x12345678)[pattern])
    if hit is not None:
        put_word(memory, CACHE + hit * 16, address)
        put_word(memory, CACHE + 15 * 16, address)
    return memory


class LookupOracle(RendererOracle):
    """Execute the full lookup and guarded installer; SDK calls remain models."""

    def __init__(self, words, cache_words, memory, arguments, stack_phase=0, mutation=0):
        SegmentQueueOracle.__init__(self, words, ENTRY, memory, arguments)
        assert stack_phase in (0, 8)
        self.r[29] = self.before[29] = STACK + stack_phase
        self.connected = dict(zip(range(INSTALL, INSTALL + len(cache_words) * 4, 4), cache_words))
        self.code.update(self.connected)
        self.calls, self.events, self.mutation = [], [], mutation

    def get(self, address, size):
        value = super().get(address, size)
        self.events.append(('R', address, size, value))
        return value

    def put(self, address, value, size):
        if self.recording:
            self.events.append(('W', address, size, value & ((1 << (size * 8)) - 1)))
        SegmentQueueOracle.put(self, address, value, size)

    def record_call(self, target):
        assert target in (DMA, INSTALL, COPY)
        args = tuple(self.r[4:7 if target == COPY else 8])
        self.calls.append((target, *args))
        self.events.append(('CALL', target, args, TimelineOracle.get(self, CLOCK, 4)))

    def hook(self, target):
        if target == DMA:
            source, destination, length, mode = self.r[4:8]
            assert source & 15 == 0 and destination & 15 == 0
            assert length in (16, 32) and mode == 1
            for i in range(length // 4):
                self.put(destination + i * 4, 0xF0000000 + i * 19, 4)
            if self.mutation:
                self.put(CLOCK, (0, 123, 0xFFFFFFFF)[self.mutation], 4)
            if self.mutation == 2:
                # A callback-created hit must not restart the already-missed scan.
                self.put(CACHE, self.r[16], 4)
        else:
            assert target == COPY
            source, destination, length = self.r[4:7]
            assert destination == CACHE and length == 224
            for i in range(length):
                self.put(destination + i, self.get(source + i, 1), 1)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register


class GameCachedLookupMatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(n) is None for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-cached-lookup-match-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, cls.output, 'selected', source_body())
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>159I', rom, 0x58138))
        cls.guarded = apply_linked_guards(cls.raw)
        _, raw_cache = installer.screen.compile_candidate(cls.root, cls.output, 'installer', installer.source_body())
        cls.cache = installer.apply_linked_guards(raw_cache)
        assert cls.cache == list(struct.unpack_from('>97I', rom, 0x57FB4))

    def models(self, memory, args, phase=0, mutation=0):
        return [LookupOracle(words, self.cache, memory, args, phase, mutation).run()
                for words in (self.retail, self.raw, self.guarded)]

    def test_complete_raw_slot_and_checked_guard_result(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']),
                         (159, 0xA0, 12))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(hashlib.sha256(struct.pack('>159I', *self.raw)).hexdigest(),
                         '741808c2f0dd29cfa36ed21f352da41403212510d5803172ed14cdbbba767a35')
        self.assertEqual(hashlib.sha256(struct.pack('>159I', *self.retail)).hexdigest(),
                         '78b570cec704115f1ab2f832a78373a1e6e0038b65735e868197083d96e37b05')
        self.assertEqual({i * 4 for i, (a, b) in enumerate(zip(self.raw, self.retail)) if a != b}, set(GUARDS))
        self.assertEqual(self.raw[:128], self.retail[:128])
        self.assertEqual(self.guarded, self.retail)
        for stack in (STACK, STACK + 8):
            frame = stack - 0xA0
            self.assertEqual((frame + 0x6F) & ~15, (frame + 0x68) & ~15)
        self.assertNotEqual((STACK + 1 + 0x6F) & ~15, (STACK + 1 + 0x68) & ~15)

    def test_three_way_connected_aliases_live_clock_and_stack_phases(self):
        coverage = [set(), set(), set()]
        cases = 0
        outputs = [OUTPUT, CLOCK] + [CACHE + i * 4 for i in range(64)]
        for pattern in range(3):
            for stack in (0, 8):
                for hit in list(range(16)) + [None]:
                    lows = (0,) if hit is not None else (0, 4, 8, 12)
                    mutations = (0,) if hit is not None else (0, 1, 2)
                    for low in lows:
                        address = 0x80012340 + low
                        memory = memory_case(pattern, address, hit)
                        for output in outputs:
                            for mutation in mutations:
                                models = self.models(memory, (0x12350 + low, -2, output), stack, mutation)
                                reference = models[0]
                                for i, model in enumerate(models):
                                    coverage[i].update(model.visits)
                                    self.assertEqual(model.memory, reference.memory)
                                    self.assertEqual(model.events, reference.events)
                                    self.assertEqual(model.calls, reference.calls)
                                    self.assertEqual(model.r[2], reference.r[2])
                                cases += 1
        expected = set(range(ENTRY, ENTRY + 159 * 4, 4)) - {ENTRY + 0x1E0}
        expected.update(range(INSTALL, INSTALL + 0xBC, 4))
        expected.update(range(INSTALL + 0x16C, INSTALL + 97 * 4, 4))
        self.assertEqual(coverage, [expected] * 3)
        self.assertEqual(cases, 11088)
        print('cached lookup guards:', cases, 'three-way connected cases; 158/159 lookup and 53/97 installer words')

    def test_every_omitted_guard_is_rejected(self):
        for offset in GUARDS:
            partial = apply_linked_guards(self.raw, offset)
            rejected = False
            for stack in (0, 8):
                for low in (0, 4, 8, 12):
                    for output in (OUTPUT, CLOCK, CACHE + 240):
                        memory = memory_case(1, 0x80012340 + low)
                        args = (0x12340 + low, 0, output)
                        reference = LookupOracle(self.retail, self.cache, memory, args, stack, 1).run()
                        try:
                            model = LookupOracle(partial, self.cache, memory, args, stack, 1).run()
                            rejected = (model.memory != reference.memory or model.events != reference.events
                                        or model.r[2] != reference.r[2] or model.calls != reference.calls)
                        except (AssertionError, KeyError):
                            rejected = True
                        if rejected:
                            break
                    if rejected:
                        break
                if rejected:
                    break
            self.assertTrue(rejected, hex(offset))

    def test_wrapping_address_arithmetic_and_signed_components(self):
        vectors = ((0, -1), (0xFFFFFFFC, 1), (0x7FFFFFF8, 1),
                   (0x80000000, -1), (0x12340, 0x7FFFFFFF),
                   (0x12340, -0x80000000), (0x12350, -2))
        for base, component in vectors:
            address = ((base + (component & 0xFFFFFFFF) * 8) & 0xFFFFFFFF) | 0x80000000
            for stack in (0, 8):
                models = self.models(memory_case(2, address), (base, component, OUTPUT), stack, 2)
                reference = models[0]
                self.assertEqual(reference.calls[0],
                                 (DMA, address & 0x7FFFFFF0, reference.calls[0][2],
                                  ((address & 0xE) + 0x1F) & ~15, 1))
                self.assertEqual(reference.calls[1][0:2], (INSTALL, 2))
                self.assertEqual(reference.calls[1][-1], address)
                for model in models:
                    self.assertEqual(model.memory, reference.memory)
                    self.assertEqual(model.events, reference.events)
                    self.assertEqual(model.r[2], reference.r[2])

    def test_unlinked_inputs_have_no_guarded_relocations(self):
        functions, _, _ = load_elf_functions(str(self.output / 'selected.o'), 'mips-linux-gnu-objdump')
        for offset, (expected, _) in GUARDS.items():
            self.assertEqual(functions['func_1502AC88'][offset // 4], expected)
        output = subprocess.run(['mips-linux-gnu-objdump', '-r', str(self.output / 'selected.o')],
                                check=True, capture_output=True, text=True).stdout
        relocations = {int(o, 16): (kind, symbol) for o, kind, symbol in re.findall(
            r'(?m)^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\S+)\s*$', output)}
        self.assertFalse(set(GUARDS) & set(relocations))
        self.assertEqual({symbol for _, symbol in relocations.values()},
                         {'D_800C3D68', 'D_800C3D60', 'func_10004514', 'func_1502AB04'})

    def test_native_selected_hit_output_alias_matrix(self):
        asset.GameAssetTableLookupAndBlockLoadTests.setUpClass()
        self.addCleanup(asset.GameAssetTableLookupAndBlockLoadTests.directory.cleanup)
        self.path = asset.GameAssetTableLookupAndBlockLoadTests.path
        fixture = asset.GameAssetTableLookupAndBlockLoadTests.fixture
        old = asset.GameAssetTableLookupAndBlockLoadTests.bodies[1]
        self.fixture = fixture.replace(old, source_body())
        asset.GameAssetTableLookupAndBlockLoadTests.run_host(self, r'''
int hit,k,i,cases=0; u32 *out,expectedReturn,expectedClock; AssetTableCache57FA0 before[16],expect[16];
for(hit=0;hit<16;hit++) for(k=0;k<66;k++) {
    reset(); D_800C3D68[hit].address=0x80012340; D_800C3D68[15].address=0x80012340;
    for(i=0;i<16;i++) before[i]=expect[i]=D_800C3D68[i];
    for(i=hit;i<15;i++) expect[i]=before[i+1];
    expect[15]=before[hit]; expect[15].generation=D_800C3D60;
    expectedClock=D_800C3D60; expectedReturn=expect[15].offset;
    out=k<64?(u32 *)D_800C3D68+k:k==64?&D_800C3D60:(u32 *)&output;
    if(k<64) ((u32 *)expect)[k]=before[hit].descriptor;
    if(k==64) expectedClock=before[hit].descriptor;
    if(k==62) expectedReturn=before[hit].descriptor;
    if((u32)func_1502AC88(0x12350,-2,out)!=expectedReturn || error || copies || dmas
       || D_800C3D60!=expectedClock) return 1;
    for(i=0;i<16;i++) if(!equal(D_800C3D68[i],expect[i])) return 2;
    cases++;
}
if(cases!=1056) return 3;
''')

    def test_production_source_rows_and_complete_identity(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        body = re.search(r's32 func_1502AC88\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body, source_body())
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            rows = [row for row in csv.DictReader(file) if row['function'] == 'func_1502AC88']
        self.assertEqual(len(rows), 12)
        self.assertEqual({int(r['offset'], 0): (int(r['expected'], 0), int(r['replacement'], 0)) for r in rows}, GUARDS)
        for row in rows:
            self.assertEqual((row['filename'], row['expected_relocations'], row['replacement_relocations'],
                              row['insert_after'], row['omit']), ('game_57FA0', '-', '-', '', 'false'))
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                    'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502AC88'], ENTRY)
        self.assertEqual(functions['func_1502AC88'], self.retail)


if __name__ == '__main__':
    unittest.main()
