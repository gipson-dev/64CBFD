"""Direct pointer/count wrapper; indeterminate descriptor seeds are target-only."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_counted_pointer_loader_candidates as screen
from tools.tests import test_game_optional_size_loader_match as optional
from tools.tests import test_game_asset_table_lookup_and_block_load as assets
from tools.tests.game_animation_timeline_oracle import bits
from tools.match_progress import load_elf_functions


buffer, lookup, installer, block = optional.buffer, optional.lookup, optional.installer, optional.block
ENTRY, BLOCK, CALLER = 0x1502B7F0, optional.BLOCK, 0x15016690
OUTPUT, REDIRECT, SCENE, FALLBACK = buffer.table.BUFFER + 512, buffer.table.BUFFER + 516, 0x50000, 0x60000
EXPANDED = 0x70000
GLOBAL, SCENE_GLOBAL = 0x800D212C, 0x800D20FC


def source_body():
    return dict(screen.candidates())['selected-for']


def memory_case(scene=False):
    memory = optional.memory_case()
    for address, length in ((GLOBAL - 16, 40), (SCENE_GLOBAL - 4, 12),
                            (SCENE - 16, 64), (FALLBACK - 16, 56), (EXPANDED - 16, 288)):
        memory.update({address + i: 0xA5 for i in range(length)})
    lookup.put_word(memory, SCENE_GLOBAL, SCENE if scene else 0)
    for address, value in ((SCENE + 6, -32768), (SCENE + 8, 32767), (SCENE + 10, -123)):
        data = (value & 0xFFFF).to_bytes(2, 'big')
        memory.update({address + i: byte for i, byte in enumerate(data)})
    memory[SCENE + 12] = 0xE7
    return memory


class BoundaryOracle(buffer.table.RangeOracle):
    """Only SDK lookup/block calls are opaque; output rereads execute on target."""

    def __init__(self, words, memory, arguments, phase=0, case=None):
        super().__init__(words, memory, arguments, phase, entry=ENTRY)
        self.case, self.lookups = case or {}, 0
        self.home = buffer.table.STACK + phase

    def record_call(self, target):
        assert target in (lookup.ENTRY, BLOCK)
        call = (target, *self.r[4:7])
        self.calls.append(call)
        self.events.append(('CALL', *call))

    def hook(self, target):
        if target == lookup.ENTRY:
            index = self.lookups
            self.lookups += 1
            if not self.case.get('unwritten'):
                descriptor = self.case.get('descriptor', 0xF0000010) + index
                self.put(self.r[6], 0xF0000000 if index == self.case.get('missing', -1) else descriptor, 4)
            result = 0xFFFFFFF0 if self.case.get('wrap') and index == 0 else 8 * (index + 1)
        else:
            self.put(self.r[6], self.case.get('loadedSize', 0xFFFFFFFF), 4)
            if self.case.get('redirect'):
                self.put(self.home, REDIRECT, 4)
            result = self.case.get('pointer', EXPANDED)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result & 0xFFFFFFFF


class ConnectedOracle(optional.BlockOracle):
    """Actual cache, lookup and block bodies plus the caller's bounded allocator."""

    def __init__(self, words, memory, arguments, phase=0, case=None, connected=None, entry=ENTRY):
        super().__init__(words, memory, arguments, phase, case, connected, entry)
        self.fallbacks = 0

    def record_call(self, target):
        if target == ENTRY:
            call = (target, *self.r[4:8])
            self.calls.append(call)
            self.events.append(('CALL', *call))
        else:
            super().record_call(target)

    def hook(self, target):
        if target == buffer.ALLOC and self.r[5:8] == [1, 0, 0]:
            assert self.r[4] == 24
            self.fallbacks += 1
            assert self.fallbacks == 1
            for register in (1, 2, 3, *range(4, 16), 24, 25):
                self.r[register] = 0xA5000000 + register
            self.r[2] = FALLBACK
        else:
            super().hook(target)
            if target == buffer.ALLOC and self.r[2] == optional.EXPANDED:
                self.r[2] = EXPANDED

    def execute(self, word):
        if word >> 26 == 0 and word & 63 == 27:
            # Retail caller uses divu; qualify only its nonzero divisor, low-word quotient.
            rs, rt = (word >> 21) & 31, (word >> 16) & 31
            assert self.r[rt] != 0
            self.lo = (self.r[rs] & 0xFFFFFFFF) // (self.r[rt] & 0xFFFFFFFF)
        else:
            super().execute(word)


class GameCountedPointerLoaderMatchTests(unittest.TestCase):
    run_host = buffer.GameBufferResourceLoaderTests.run_host
    assert_models_equal = buffer.GameBufferResourceLoaderTests.assert_models_equal

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(n) is None for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-counted-pointer-loader-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', source_body())
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>60I', cls.rom, 0x58CA0))
        cls.caller = list(struct.unpack_from('>112I', cls.rom, 0x43B40))
        _, loader = block.screen.compile_candidate(cls.root, cls.output, 'block',
            dict(block.screen.candidates())['nested-one-size-no-register'], 'o2g3')
        _, raw_lookup = lookup.screen.compile_candidate(cls.root, cls.output, 'lookup', lookup.source_body())
        _, raw_cache = installer.screen.compile_candidate(cls.root, cls.output, 'cache', installer.source_body())
        cls.connected = {}
        for address, words in ((BLOCK, loader), (lookup.ENTRY, lookup.apply_linked_guards(raw_lookup)),
                               (lookup.INSTALL, installer.apply_linked_guards(raw_cache))):
            cls.connected.update(zip(range(address, address + len(words) * 4, 4), words))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = (cls.root / 'conker/include/libc/stdarg.h').read_text() + r'''
typedef unsigned char u8; typedef int s32; typedef unsigned int u32;
#define NULL ((void *)0)
u8 D_AB1950[16] __attribute__((aligned(16)));
static u32 storage[64],metadata[16],advances[16],expectedBase,depth;
static s32 items[16],finalSize;
static void *output;
static int lookups,loads,consumed,error,missing,nullPointer;
static void reset(u32 count,int absent,int pattern,u32 flags) {
    int i;depth=count;missing=absent;lookups=loads=consumed=error=0;
    expectedBase=(u32)D_AB1950;output=storage;finalSize=pattern==2?0:-123;
    nullPointer=pattern==1;
    for(i=0;i<64;i++) storage[i]=0xA5A5A5A5;
    for(i=0;i<16;i++) {items[i]=pattern==2?1:i+1;advances[i]=(u32)(8*(i+1));metadata[i]=flags|((u32)i+1);}
    if(pattern==1) {items[0]=-1;items[1]=(s32)0x80000000;items[2]=0x7FFFFFFF;advances[0]=0xFFFFFFF0;}
    if(absent>=0) metadata[absent]=0xF0000000;
}
s32 func_1502AC88(u32 base,s32 item,u32 *descriptor) {
    int i=lookups++;
    if(base!=expectedBase || item!=items[i] || loads || output!=storage
       || i>=(missing<0?(int)depth:missing+1)) error=1;
    *descriptor=metadata[i];expectedBase+=advances[i];return (s32)advances[i];
}
void *func_1502B350(u32 base,u32 descriptor,s32 *size) {
    loads++;
    if(loads!=1 || lookups!=(int)depth || base!=expectedBase || descriptor!=metadata[depth-1]
       || (u32)*size!=(descriptor&0x0FFFFFFF) || output!=storage) error=2;
    *size=finalSize;return nullPointer?NULL:storage+4;
}
#undef va_arg
#define va_arg(path,type) (consumed++,__builtin_va_arg(path,type))
/* Native cases always write the descriptor before reading it. */
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
''' + source_body() + '\n#pragma GCC diagnostic pop\n'

    def test_direct_body_frame_controls_and_no_guards(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (60, 0x48, 0))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(hashlib.sha256(struct.pack('>60I', *self.words)).hexdigest(),
                         'e88dfdc70feb02075b447f087746999e1077f259047c8f4c20482f6be3f156f6')
        self.assertEqual(len(screen.candidates()), 132)
        for name, expected in (('placeholder', (7, 0, 60)), ('baseline', (60, 0x48, 10)),
                               ('layout-1', (60, 0x48, 2)), ('selected-size-first', (60, 0x48, 2)),
                               ('zero-descriptor', (61, 0x48, 48)), ('one-descriptor', (62, 0x48, 50))):
            record, _ = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            self.assertFalse(any(r['function'] == 'func_1502B7F0' for r in csv.DictReader(file)))

    def test_native_positive_depth_flags_missing_paths_and_independent_results(self):
        self.run_host(r'''
int d,absent,pattern,flag,cases=0,i;u32 result;
for(pattern=0;pattern<3;pattern++) for(d=1;d<=16;d++) for(absent=-1;absent<d;absent++)
for(flag=0;flag<16;flag++) {
    reset((u32)d,absent,pattern,(u32)flag<<28);
    result=func_1502B7F0(&output,depth,
        items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],
        items[8],items[9],items[10],items[11],items[12],items[13],items[14],items[15]);
    if(error || consumed!=d || lookups!=(absent<0?d:absent+1) || loads!=(absent<0)
       || output!=(absent<0 && !nullPointer?storage+4:NULL)
       || result!=(absent<0?(u32)finalSize:0)) return 1;
    for(i=0;i<64;i++) if(storage[i]!=0xA5A5A5A5) return 2;
    cases++;
}
if(cases!=7296) return 3;
''')

    def test_target_boundary_incoming_seeds_full_memory_and_coverage(self):
        cases, coverage = 0, [set(), set()]
        for depth in range(7):
            for missing in range(-2, depth):
                for phase in (0, 8):
                    for seed in optional.SEEDS:
                        for pointer, size in ((0, 0xFFFFFFFF), (EXPANDED, 0), (EXPANDED, 0x80000001)):
                            memory = memory_case()
                            lookup.put_word(memory, buffer.table.STACK + phase - 0x14, seed)
                            case = dict(unwritten=missing == -2, missing=missing, wrap=True, pointer=pointer, loadedSize=size)
                            models = [BoundaryOracle(words, memory, (OUTPUT, depth, -1, 0x80000000, 3, 4, 5, 6), phase, case).run()
                                      for words in (self.retail, self.words)]
                            self.assert_models_equal(models[1], models[0])
                            reference = models[0]
                            expected = 0 if depth == 0 else 1 if missing == -2 and not seed & 0x0FFFFFFF else missing + 1 if missing >= 0 else depth
                            self.assertEqual(reference.lookups, expected)
                            loads = depth == 0 or missing < 0 and (missing != -2 or seed & 0x0FFFFFFF != 0)
                            self.assertEqual(reference.r[2], size if loads else 0)
                            self.assertEqual(reference.peek(OUTPUT, 4), pointer if loads else 0)
                            calls = [call for call in reference.calls if call[0] == BLOCK]
                            descriptor = seed if depth == 0 or missing == -2 else 0xF0000010 + depth - 1
                            base = (0xAB1950 + (0xFFFFFFF0 if expected else 0) + sum(8 * (i + 1) for i in range(1, expected))) & 0xFFFFFFFF
                            self.assertEqual(calls, [(BLOCK, base, descriptor, buffer.table.STACK + phase - 0x10)] if loads else [])
                            for i, model in enumerate(models):
                                coverage[i].update(model.visits)
                            cases += 1
        self.assertEqual(cases, 1470)
        self.assertEqual(coverage, [set(range(ENTRY, ENTRY + 240, 4))] * 2)
        print('counted pointer wrapper:', cases, 'target boundary cases; all 60 words, original unwritten seeds')

    def test_output_aliases_private_size_descriptor_and_argument_homes(self):
        cases = 0
        for phase in (0, 8):
            for depth in (0, 1, 3):
                for displacement in (-0x14, -0x10, 0, 4, 8, 12, 16):
                    for missing in (-1, 0):
                        target = buffer.table.STACK + phase + displacement
                        memory = memory_case()
                        lookup.put_word(memory, buffer.table.STACK + phase - 0x14, 0x90000011)
                        models = [BoundaryOracle(words, memory, (target, depth, 41, 42, 43), phase, dict(missing=missing)).run()
                                  for words in (self.retail, self.words)]
                        self.assert_models_equal(models[1], models[0])
                        loads = depth == 0 or missing < 0
                        pointer = EXPANDED if loads else 0
                        self.assertEqual(models[0].peek(target, 4), pointer)
                        self.assertEqual(models[0].r[2], pointer if displacement == -0x10 else 0xFFFFFFFF if loads else 0)
                        self.assertEqual([call[2] for call in models[0].calls if call[0] == lookup.ENTRY], [41, 42, 43][:depth] if missing < 0 else [41][:min(depth, 1)])
                        cases += 1
        self.assertEqual(cases, 84)
        print('counted pointer wrapper:', cases, 'physical output aliases; pointer store precedes returned-size reload')

    def test_post_block_output_home_reread_and_stale_load_negative_control(self):
        for phase in (0, 8):
            models = [BoundaryOracle(words, memory_case(), (OUTPUT, 2, 1, 2), phase, dict(redirect=True)).run()
                      for words in (self.retail, self.words)]
            self.assert_models_equal(models[1], models[0])
            self.assertEqual(models[0].peek(OUTPUT, 4), 0xA5A5A5A5)
            self.assertEqual(models[0].peek(REDIRECT, 4), EXPANDED)
            stale = self.words[:]
            self.assertEqual(stale[0xBC // 4], 0x8FAA0048)
            # Replace the real reread with the original argument pointer.
            stale[0xBC // 4] = 0x3C0A0000 | (OUTPUT >> 16)
            stale[0xC4 // 4] = 0xAD420000 | (OUTPUT & 0xFFFF)
            actual = BoundaryOracle(stale, memory_case(), (OUTPUT, 2, 1, 2), phase, dict(redirect=True)).run()
            self.assertNotEqual(actual.memory, models[0].memory)

    def test_descriptor_initializers_fail_zero_depth_seed_witness(self):
        memory = memory_case()
        lookup.put_word(memory, buffer.table.STACK - 0x14, 0x90000011)
        reference = BoundaryOracle(self.retail, memory, (OUTPUT, 0, 1, 2)).run()
        for name in ('zero-descriptor', 'one-descriptor'):
            _, words = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            actual = BoundaryOracle(words, memory, (OUTPUT, 0, 1, 2)).run()
            self.assertNotEqual(actual.calls, reference.calls)
            self.assertNotEqual(actual.memory, reference.memory)
        self.assertEqual(reference.calls, [(BLOCK, 0xAB1950, 0x90000011, buffer.table.STACK - 0x10)])

    def test_connected_actual_lookup_cache_block_failures_and_sizes(self):
        cases = 0
        for phase in (0, 8):
            for depth in range(1, 4):
                for missing in range(-1, depth):
                    for descriptor in (0x80000010, 0x10000010, 0x90000011):
                        for failure in (0, 1, 2):
                            case = dict(lookupDescriptor=descriptor, missing=missing, failure=failure, decoded=32, mutation=True)
                            models = [ConnectedOracle(words, memory_case(), (OUTPUT, depth, *([1] * depth)), phase, case, self.connected).run()
                                      for words in (self.retail, self.words)]
                            self.assert_models_equal(models[1], models[0])
                            compressed = descriptor & 0x70000000 == 0x10000000
                            pointer = 0 if missing >= 0 or failure == 1 or compressed and failure == 2 else EXPANDED if compressed else buffer.TEMP
                            size = 0 if missing >= 0 or compressed and failure == 2 else descriptor & 0x0FFFFFFF if failure == 1 else 32 if compressed else (descriptor & 0x0FFFFFFF) + (descriptor & 1)
                            self.assertEqual(models[0].r[2], size)
                            self.assertEqual(models[0].peek(OUTPUT, 4), pointer)
                            self.assertEqual(models[0].lookups, depth if missing < 0 else missing + 1)
                            self.assertEqual(models[0].allocations, 0 if missing >= 0 else 1 if failure == 1 or not compressed else 2)
                            cases += 1
        self.assertEqual(cases, 162)
        print('counted pointer wrapper:', cases, 'connected actual cache/lookup/block cases; independent size/pointer failures')

    def test_connected_zero_depth_seeds_and_first_allocation_failure_size_one(self):
        for phase in (0, 8):
            for seed in optional.SEEDS:
                for failure in (0, 1):
                    memory = memory_case()
                    lookup.put_word(memory, buffer.table.STACK + phase - 0x14, seed)
                    models = [ConnectedOracle(words, memory, (OUTPUT, 0, 1, 2), phase, dict(failure=failure), self.connected).run()
                              for words in (self.retail, self.words)]
                    self.assert_models_equal(models[1], models[0])
                    self.assertEqual(models[0].lookups, 0)
                    self.assertIn((BLOCK, 0xAB1950, seed, buffer.table.STACK + phase - 0x10), models[0].calls)
                    if failure:
                        self.assertEqual(models[0].r[2], 1)
                        self.assertEqual(models[0].peek(OUTPUT, 4), 0)

    def test_connected_pointer_output_aliases_live_cache_clock_and_scratch(self):
        cases = 0
        for phase in (0, 8):
            for depth in (1, 3):
                for target in (lookup.CLOCK, buffer.SCRATCH, lookup.CACHE + 15 * 16 + 8):
                    for descriptor in (0x80000010, 0x90000011):
                        for failure in (0, 1, 2):
                            case = dict(lookupDescriptor=descriptor, failure=failure, decoded=32, mutation=True)
                            models = [ConnectedOracle(words, memory_case(), (target, depth, *([1] * depth)), phase, case, self.connected).run()
                                      for words in (self.retail, self.words)]
                            self.assert_models_equal(models[1], models[0])
                            compressed = descriptor == 0x90000011
                            pointer = 0 if failure == 1 or compressed and failure == 2 else EXPANDED if compressed else buffer.TEMP
                            size = descriptor & 0x0FFFFFFF if failure == 1 else 0 if compressed and failure == 2 else 32 if compressed else 16
                            self.assertEqual(models[0].peek(target, 4), pointer)
                            self.assertEqual(models[0].r[2], size)
                            self.assertEqual(models[0].lookups, depth)
                            cases += 1
        self.assertEqual(cases, 72)
        print('counted pointer wrapper:', cases, 'connected pointer outputs aliasing actual cache, clock and scratch')

    def caller_model(self, words, case, phase=0, scene=False, component=1):
        code = self.connected.copy()
        code.update(zip(range(ENTRY, ENTRY + 240, 4), words))
        return ConnectedOracle(self.caller, memory_case(scene), (component,), phase, case, code, CALLER).run()

    def assert_fallback_record(self, model, scene):
        expected = (-32768, 32767, -123) if scene else (3600, -3200, -2200)
        for offset, value in zip((0, 2, 4), expected):
            self.assertEqual(model.peek(FALLBACK + offset, 2), value & 0xFFFF)
        for offset, value in zip((8, 12, 16), (-32668.0, 32867.0, -123.0) if scene else (1000.0,) * 3):
            self.assertEqual(model.peek(FALLBACK + offset, 4), bits(value))
        for offset, value in ((6, 0), (7, 0xE7 if scene else 0), (21, 0)):
            self.assertEqual(model.peek(FALLBACK + offset, 1), value)
        for offset in (20, 22, 23, -1, 24):
            self.assertEqual(model.peek(FALLBACK + offset, 1), 0xA5)

    def test_full_caller_unsigned_division_and_fallback_records(self):
        cases, visits = 0, [set(), set()]
        self.assertEqual(self.caller[(0x150166D8 - CALLER) // 4], 0x0041001B)
        for phase in (0, 8):
            for scene in (False, True):
                for component in (1, 2, 3):
                    for missing in range(-1, 3):
                        for descriptor in (0x80000010, 0x80000030, 0x90000011):
                            for failure in (0, 1, 2):
                                case = dict(lookupDescriptor=descriptor, missing=missing, failure=failure, decoded=32)
                                models = [self.caller_model(words, case, phase, scene, component) for words in (self.retail, self.words)]
                                self.assert_models_equal(models[1], models[0])
                                reference = models[0]
                                self.assertIn((ENTRY, GLOBAL, 3, 12, component), reference.calls)
                                components = [call[2] for call in reference.calls if call[0] == lookup.ENTRY]
                                self.assertEqual(components, [12, component, 6][:3 if missing < 0 else missing + 1])
                                for call in reference.calls:
                                    if call[0] == lookup.ENTRY:
                                        self.assertEqual(call[3], buffer.table.STACK + phase - 0x3C)
                                    if call[0] == BLOCK:
                                        self.assertEqual(call[3], buffer.table.STACK + phase - 0x38)
                                compressed = descriptor == 0x90000011
                                size = 0 if missing >= 0 or compressed and failure == 2 else descriptor & 0x0FFFFFFF if failure == 1 else 32 if compressed else descriptor & 0x0FFFFFFF
                                quotient = size // 24
                                fallback = quotient == 0
                                pointer = 0 if failure == 1 else EXPANDED if compressed else buffer.TEMP
                                self.assertEqual(reference.fallbacks, int(fallback))
                                self.assertEqual(reference.peek(GLOBAL - 12, 4), 0xFFFFFFFF)
                                self.assertEqual(reference.peek(GLOBAL - 8, 4), 0xFFFFFFFF)
                                self.assertEqual(reference.peek(GLOBAL - 4, 4), quotient or 1)
                                self.assertEqual(reference.peek(GLOBAL, 4), FALLBACK if fallback else pointer)
                                if fallback:
                                    self.assert_fallback_record(reference, scene)
                                for i, model in enumerate(models):
                                    visits[i].update(model.visits)
                                cases += 1
        self.assertEqual(cases, 432)
        reachable = set(range(CALLER, 0x15016844, 4)) - {0x150167D0}
        self.assertTrue(all(reachable <= v for v in visits))
        self.assertTrue(all(0x150167D0 not in v for v in visits))
        print('counted pointer wrapper:', cases, 'full 112-word caller cases; 108 reachable words, original unsigned division')

    def test_caller_high_bit_counts_use_unsigned_division(self):
        class CountOracle(ConnectedOracle):
            def hook(self, target):
                if target == ENTRY:
                    self.put(self.r[4], self.case['pointer'], 4)
                    for register in (1, 2, 3, *range(4, 16), 24, 25):
                        self.r[register] = 0xA5000000 + register
                    self.r[2] = self.case['count']
                else:
                    super().hook(target)
        for count in (0, 1, 23, 24, 25, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFF):
            for pointer in (0, EXPANDED):
                model = CountOracle(self.caller, memory_case(), (2,), case=dict(count=count, pointer=pointer), entry=CALLER).run()
                quotient = count // 24
                self.assertEqual(model.peek(GLOBAL - 4, 4), quotient or 1)
                self.assertEqual(model.fallbacks, int(quotient == 0))
                self.assertEqual(model.peek(GLOBAL, 4), pointer if quotient else FALLBACK)

    def test_native_connected_actual_lookup_cache_and_block_source(self):
        class Connected(assets.GameAssetTableLookupAndBlockLoadTests):
            pass
        Connected.setUpClass()
        self.addCleanup(Connected.doClassCleanups)
        original = self.fixture
        try:
            self.fixture = (self.root / 'conker/include/libc/stdarg.h').read_text() + '\n' + Connected.fixture + r'''
u8 D_AB1950[16] __attribute__((aligned(16)));
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
''' + source_body() + '\n#pragma GCC diagnostic pop\n'
            self.run_host(r'''
void *output;u32 size,root=(u32)D_AB1950;int hit,failure;
for(hit=0;hit<2;hit++) for(failure=0;failure<2;failure++) {
    reset();connected=1;expectedAddress=(root+8)&0x7FFFFFF0;connectedAddress=root+0x20;
    expectedLength=32;descriptor=0x80000010;failAllocation=failure;
    if(hit) {D_800C3D68[15].address=(root+8)|0x80000000;D_800C3D68[15].offset=0x20;
             D_800C3D68[15].descriptor=descriptor;dmaPhase=1;}
    output=compressed+4;size=func_1502B7F0(&output,1,1);
    if(size!=16 || output!=(failure?NULL:compressed) || error || allocations!=1 || decodes || frees
       || dmas!=(hit?0:1)+(failure?0:1) || copies!=!hit) return 1;
}
''')
        finally:
            self.fixture = original

    def test_production_body_prototype_and_complete_caller_slot(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        self.assertEqual(re.search(r'u32 func_1502B7F0\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0), source_body())
        self.assertNotRegex(source_body(), r'descriptor\s*=')
        self.assertIn('u32 func_1502B7F0(void **output, u32 depth, ...);',
                      (self.root / 'conker/include/functions.h').read_text())
        self.assertIn('func_1502B7F0((void **)&D_800D212C, 3, 12, arg0, 6) / 24U',
                      (self.root / 'conker/src/game/done/game_43B20.c').read_text())
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        for name, expected, address in (('func_1502B7F0', self.retail, ENTRY), ('func_15016690', self.caller, CALLER)):
            self.assertEqual(addresses[name], address)
            self.assertEqual(functions[name], expected)
        self.assertEqual(hashlib.sha256(struct.pack('>112I', *functions['func_15016690'])).hexdigest(),
                         '723d1caa2c30b4efcba8eab56eb2533207c0dd09cf358d5b9227e14ed0a19804')

    def test_unlinked_relocations(self):
        output = subprocess.run(['mips-linux-gnu-objdump', '-r', str(self.output / 'selected.o')],
                                check=True, capture_output=True, text=True).stdout
        actual = {int(o, 16): (kind, symbol) for o, kind, symbol in re.findall(
            r'(?m)^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\S+)\s*$', output)}
        self.assertEqual(actual, {0x30: ('R_MIPS_HI16', 'D_AB1950'), 0x38: ('R_MIPS_LO16', 'D_AB1950'),
                                 0x78: ('R_MIPS_26', 'func_1502AC88'), 0xB4: ('R_MIPS_26', 'func_1502B350')})


if __name__ == '__main__':
    unittest.main()
