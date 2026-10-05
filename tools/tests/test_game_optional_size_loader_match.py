"""Direct optional-size SDK wrapper match; unwritten seeds are target-only evidence."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_optional_size_loader_candidates as screen
from tools.tests import test_game_buffer_resource_loader as buffer
from tools.tests import test_game_cached_lookup_match as lookup
from tools.tests import test_game_cache_installer_match as installer
from tools.tests import test_game_block_loader_direct_match as block
from tools.tests import test_game_variadic_table_range_match as paths
from tools.tests import test_game_asset_table_lookup_and_block_load as assets
from tools.match_progress import load_elf_functions


ENTRY, BLOCK, EXPANDED, CALLER, FOLLOWUP = 0x1502B5C8, 0x1502B350, 0x40000, 0x15085B70, 0x15085BE8
SIZE = buffer.table.BUFFER + 512
SEEDS = (0, 1, 0x80000010, 0x10000010, 0x90000011, 0xF0000000, 0xFFFFFFFF)


def source_body():
    return dict(screen.candidates())['layout-6']


def memory_case():
    memory = buffer.memory_case()
    memory.update({EXPANDED + i: 0xA5 for i in range(-16, 272)})
    for address in (0x80087290, 0x80087294, 0x800D2350):
        memory.update({address + i: 0xA5 for i in range(-4, 8)})
    return memory


class BoundaryOracle(buffer.table.RangeOracle):
    """Opaque lookup/block calls allow precise incoming-slot and live-output witnesses."""

    def __init__(self, words, memory, arguments, phase=0, case=None):
        super().__init__(words, memory, arguments, phase, entry=ENTRY)
        self.case, self.lookups = case or {}, 0

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
            if 'mutateSize' in self.case:
                self.put(self.case['size'], self.case['mutateSize'], 4)
            result = 0xFFFFFFF0 if self.case.get('wrap') and index == 0 else 8 * (index + 1)
        else:
            self.put(self.r[6], self.case.get('loadedSize', 0xFFFFFFFF), 4)
            result = self.case.get('pointer', EXPANDED)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result & 0xFFFFFFFF


class BlockOracle(buffer.BufferOracle):
    """Actual cache/lookup/block instructions with bounded two-allocation SDK hooks."""

    def __init__(self, words, memory, arguments, phase=0, case=None, connected=None, entry=ENTRY):
        super().__init__(words, memory, arguments, phase, case, connected, entry)
        self.allocations, self.sizeTarget = 0, None

    def record_call(self, target):
        if target in (BLOCK, ENTRY, FOLLOWUP):
            count = 3 if target == BLOCK else 4 if target == ENTRY else 0
            call = (target, *self.r[4:4 + count])
            self.calls.append(call)
            self.events.append(('CALL', *call))
            if target == BLOCK:
                self.owner, self.sizeTarget = BLOCK, self.r[6]
        else:
            super().record_call(target)

    def hook(self, target):
        if target == buffer.ALLOC:
            assert self.r[5:8] == [1, 2, 2]
            self.allocations += 1
            assert self.allocations <= 2
            result = 0 if self.allocations == self.case.get('failure', 0) else buffer.TEMP if self.allocations == 1 else EXPANDED
            if self.allocations == 1 and result:
                self.put(buffer.TEMP, self.case.get('header', 0x80000020), 4)
            if self.case.get('mutation'):
                self.put(buffer.SCRATCH, 0x4567 if self.allocations == 1 else 0x6789, 4)
                if self.allocations == 2:
                    self.put(self.sizeTarget, 0xDEAD0001, 4)
        elif target == FOLLOWUP:
            result = 0x12345678
        else:
            super().hook(target)
            if target == buffer.FREE and self.case.get('mutation'):
                self.put(self.sizeTarget, 0xDEAD0002, 4)
            return
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result


class GameOptionalSizeLoaderMatchTests(unittest.TestCase):
    run_host = buffer.GameBufferResourceLoaderTests.run_host
    assert_models_equal = buffer.GameBufferResourceLoaderTests.assert_models_equal

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(n) is None for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-optional-size-loader-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', source_body())
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>61I', cls.rom, 0x58A78))
        cls.caller = list(struct.unpack_from('>30I', cls.rom, 0xB3020))
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
        sdk = (cls.root / 'conker/include/libc/stdarg.h').read_text()
        cls.fixture = sdk + '\n' + r'''
typedef unsigned char u8; typedef int s32; typedef unsigned int u32;
#define NULL ((void *)0)
u8 D_AB1950[16] __attribute__((aligned(16)));
static s32 output,items[16],*sizePointer;
static u32 storage[64],metadata[16],advances[16],expectedBase,depth,*lastDescriptor;
static s32 finalSize;
static int lookups,loads,consumed,error,expectedLookups,missing,mutateOutput,nullPointer;
static void reset(u32 count,int absent,int pattern,u32 flags,int optional) {
    int i;depth=count;missing=absent;lookups=loads=consumed=error=0;lastDescriptor=NULL;
    expectedBase=(u32)D_AB1950;expectedLookups=absent<0?(int)count:absent+1;
    output=-99;sizePointer=optional?NULL:&output;finalSize=pattern==2?0:-123;
    mutateOutput=0;nullPointer=pattern==1;
    for(i=0;i<64;i++) storage[i]=0xA5A5A5A5;
    for(i=0;i<16;i++) { items[i]=pattern==2?1:i+1;advances[i]=(u32)(8*(i+1));metadata[i]=flags|((u32)i+1); }
    if(pattern==1) { items[0]=-1;items[1]=(s32)0x80000000;items[2]=0x7FFFFFFF;advances[0]=0xFFFFFFF0; }
    if(absent>=0) metadata[absent]=0xF0000000;
}
s32 func_1502AC88(u32 base,s32 item,u32 *descriptor) {
    int i=lookups++;
    if(i>=expectedLookups || base!=expectedBase || item!=items[i] || loads
       || (lastDescriptor && descriptor!=lastDescriptor)
       || (sizePointer && (u32)*sizePointer!=(i?metadata[i-1]&0x0FFFFFFF:1))) error=1;
    *descriptor=metadata[i];lastDescriptor=descriptor;expectedBase+=advances[i];
    if(mutateOutput && sizePointer) *sizePointer=-333;
    return (s32)advances[i];
}
void *func_1502B350(u32 base,u32 descriptor,s32 *size) {
    loads++;
    if(loads!=1 || lookups!=expectedLookups || base!=expectedBase || descriptor!=metadata[depth-1]
       || !size || (sizePointer && size!=sizePointer) || (u32)*size!=(descriptor&0x0FFFFFFF)) error=2;
    *size=finalSize;return nullPointer?NULL:storage+4;
}
#undef va_arg
#define va_arg(path,type) (consumed++,__builtin_va_arg(path,type))
/* Native cases always perform a descriptor-writing lookup before a descriptor read. */
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
''' + source_body() + '\n#pragma GCC diagnostic pop\n'

    def test_direct_complete_body_frame_hash_and_source_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (61, 0x50, 0))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(hashlib.sha256(struct.pack('>61I', *self.words)).hexdigest(),
                         '3e5a7f5d2eb6e43e30fefad7ef24f5cb4f7880de2bb8040cf05e4c437e8f0568')
        self.assertEqual(len(screen.candidates()), 128)
        for name, expected in (('placeholder', (3, 0, 61)), ('baseline', (61, 0x50, 1)),
                ('layout-12', (61, 0x50, 0)), ('ternary-target', (62, 0x50, 51)),
                ('zero-descriptor', (62, 0x50, 49)), ('one-descriptor', (63, 0x50, 49))):
            record, words = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')
            self.assertEqual(words == self.retail, name == 'layout-12')

    def test_native_positive_depth_optional_size_flags_and_argument_consumption(self):
        self.run_host(r'''
int d,absent,pattern,flag,optional,cases=0,i;void *actual;
for(pattern=0;pattern<3;pattern++) for(d=1;d<=16;d++) for(absent=-1;absent<d;absent++)
for(flag=0;flag<16;flag++) for(optional=0;optional<2;optional++) {
    reset((u32)d,absent,pattern,(u32)flag<<28,optional);
    actual=func_1502B5C8(sizePointer,depth,
        items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],
        items[8],items[9],items[10],items[11],items[12],items[13],items[14],items[15]);
    if(error || consumed!=d || lookups!=expectedLookups || loads!=(absent<0)
       || actual!=(absent<0 && !nullPointer?storage+4:NULL)
       || output!=(optional?-99:absent<0?finalSize:0)) return 1;
    for(i=0;i<64;i++) if(storage[i]!=0xA5A5A5A5) return 2;
    cases++;
}
if(cases!=14592) return 3;
''')

    def test_native_lookup_output_mutation_is_overwritten_and_final_pointer_independent(self):
        self.run_host(r'''
int pointerNull,sizeZero;
for(pointerNull=0;pointerNull<2;pointerNull++) for(sizeZero=0;sizeZero<2;sizeZero++) {
    reset(3,-1,0,0x90000000,0);mutateOutput=1;nullPointer=pointerNull;finalSize=sizeZero?0:-123;
    if(func_1502B5C8(&output,3,items[0],items[1],items[2])!=(pointerNull?NULL:storage+4)
       || error || output!=finalSize || consumed!=3 || lookups!=3 || loads!=1) return 1;
}
''')

    def test_target_boundary_seeds_full_memory_events_and_live_outputs(self):
        cases, coverage = 0, [set(), set()]
        for pattern in range(3):
            for depth in range(7):
                for missing in range(-2, depth):
                    for phase in (0, 8):
                        for seed in SEEDS:
                            for optional in (False, True):
                                memory = memory_case()
                                lookup.put_word(memory, buffer.table.STACK + phase - 0x18, seed)
                                target = buffer.table.STACK + phase - 0x10 if optional else SIZE
                                args = (0 if optional else SIZE, depth, *paths.components(pattern))
                                case = dict(unwritten=missing == -2, missing=missing, wrap=pattern == 1,
                                            loadedSize=0 if pattern == 2 else 0xFFFFFFFF,
                                            pointer=0 if pattern == 1 else EXPANDED)
                                models = [BoundaryOracle(words, memory, args, phase, case).run()
                                          for words in (self.retail, self.words)]
                                reference = models[0]
                                expected = 0 if depth == 0 else 1 if missing == -2 and not seed & 0x0FFFFFFF else missing + 1 if missing >= 0 else depth
                                self.assertEqual(reference.lookups, expected)
                                loads = depth == 0 or missing < 0 and (missing != -2 or seed & 0x0FFFFFFF != 0)
                                loader = [call for call in reference.calls if call[0] == BLOCK]
                                self.assertEqual(len(loader), int(loads))
                                self.assertEqual(reference.r[2], case['pointer'] if loads else 0)
                                self.assertEqual(reference.peek(target, 4), case['loadedSize'] if loads else 0)
                                if loads:
                                    base = 0xAB1950
                                    for i in range(expected):
                                        base = (base + (0xFFFFFFF0 if pattern == 1 and i == 0 else 8 * (i + 1))) & 0xFFFFFFFF
                                    descriptor = seed if depth == 0 or missing == -2 else 0xF0000010 + depth - 1
                                    self.assertEqual(loader, [(BLOCK, base, descriptor, target)])
                                for i, model in enumerate(models):
                                    coverage[i].update(model.visits)
                                    self.assert_models_equal(model, reference)
                                cases += 1
        self.assertEqual(cases, 2940)
        self.assertEqual(coverage, [set(range(ENTRY, ENTRY + 244, 4))] * 2)
        print('optional size wrapper:', cases, 'two-way target boundary cases; all 61 words, physical descriptor/fallback')

    def test_output_alias_to_descriptor_changes_full_loader_descriptor(self):
        for phase in (0, 8):
            for depth in (0, 1, 3):
                target = buffer.table.STACK + phase - 0x18
                memory = memory_case()
                lookup.put_word(memory, target, 0x90000011)
                args = (target, depth, 1, 2, 3)
                models = [BoundaryOracle(words, memory, args, phase).run() for words in (self.retail, self.words)]
                self.assert_models_equal(models[1], models[0])
                call = next(call for call in models[0].calls if call[0] == BLOCK)
                self.assertEqual(call[2], 1 if depth == 0 else 0x10 + depth - 1)
                self.assertEqual(call[3], target)
                self.assertEqual(models[0].peek(target, 4), 0xFFFFFFFF)
                # Initial output-one and loop output masks really store to the descriptor cell.
                self.assertIn((target, 4, 1), models[0].stores)

    def test_caller_argument_home_alias_keeps_retail_consumed_component_changes(self):
        for phase in (0, 8):
            target = buffer.table.STACK + phase + 4
            case = dict(descriptor=0xF0000001)
            models = [BoundaryOracle(words, memory_case(), (target, 3, 41, 42, 43), phase, case).run()
                      for words in (self.retail, self.words)]
            self.assert_models_equal(models[1], models[0])
            self.assertEqual(models[0].lookups, 1)
            self.assertEqual(models[0].r[2], 0)
            self.assertFalse(any(call[0] == BLOCK for call in models[0].calls))
            self.assertEqual(models[0].peek(target, 4), 0)
            for displacement in (8, 12, 16):
                target = buffer.table.STACK + phase + displacement
                args = (target, 3, 41, 42, 43)
                models = [BoundaryOracle(words, memory_case(), args, phase).run() for words in (self.retail, self.words)]
                self.assert_models_equal(models[1], models[0])
                components = [call[2] for call in models[0].calls if call[0] == lookup.ENTRY]
                self.assertEqual(components, {8: [1, 42, 43], 12: [41, 16, 43], 16: [41, 42, 17]}[displacement])
                self.assertEqual(models[0].peek(target, 4), 0xFFFFFFFF)

    def test_stale_final_descriptor_read_fails_output_alias_witness(self):
        stale = self.words[:]
        self.assertEqual(stale[0xB0 // 4], 0x8FA50038)
        stale[0xB0 // 4] = 0x01002825
        target = buffer.table.STACK - 0x18
        args = (target, 1, 1, 2)
        reference = BoundaryOracle(self.retail, memory_case(), args).run()
        actual = BoundaryOracle(stale, memory_case(), args).run()
        self.assertEqual(reference.calls[-1][2], 0x10)
        self.assertEqual(actual.calls[-1][2], 0xF0000010)
        self.assertNotEqual(actual.calls, reference.calls)

    def test_descriptor_initializer_controls_fail_incoming_seed_witness(self):
        memory = memory_case()
        lookup.put_word(memory, buffer.table.STACK - 0x18, 0x90000011)
        args = (SIZE, 0, 1, 2)
        retail = BoundaryOracle(self.retail, memory, args).run()
        for name in ('zero-descriptor', 'one-descriptor'):
            _, words = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            actual = BoundaryOracle(words, memory, args).run()
            self.assertNotEqual(actual.calls, retail.calls)
            self.assertNotEqual(actual.memory, retail.memory)
        self.assertEqual(retail.calls, [(BLOCK, 0xAB1950, 0x90000011, SIZE)])

    def test_connected_actual_lookup_cache_block_flags_failures_and_sizes(self):
        cases = 0
        for phase in (0, 8):
            for depth in range(1, 4):
                for missing in range(-1, depth):
                    for descriptor in (0x80000010, 0x10000010, 0x90000011):
                        for optional in (False, True):
                            for failure in (0, 1, 2):
                                case = dict(lookupDescriptor=descriptor, missing=missing, failure=failure,
                                            decoded=32, mutation=True)
                                args = (0 if optional else SIZE, depth, *([1] * depth))
                                models = [BlockOracle(words, memory_case(), args, phase, case, self.connected).run()
                                          for words in (self.retail, self.words)]
                                self.assert_models_equal(models[1], models[0])
                                reference = models[0]
                                target = buffer.table.STACK + phase - 0x10 if optional else SIZE
                                compressed = descriptor & 0x70000000 == 0x10000000
                                count = (descriptor & 0x0FFFFFFF) + (descriptor & 1)
                                expectedPointer = 0 if missing >= 0 or failure == 1 or compressed and failure == 2 else EXPANDED if compressed else buffer.TEMP
                                expectedSize = (0 if missing >= 0 or compressed and failure == 2 else descriptor & 0x0FFFFFFF
                                                if failure == 1 else count if not compressed else 32)
                                self.assertEqual(reference.r[2], expectedPointer)
                                self.assertEqual(reference.peek(target, 4), expectedSize)
                                self.assertEqual(reference.lookups, depth if missing < 0 else missing + 1)
                                self.assertEqual(reference.allocations, 0 if missing >= 0 else 1 if failure == 1 or not compressed else 2)
                                self.assertEqual(any(call[0] == buffer.FREE for call in reference.calls), missing < 0 and compressed and failure != 1)
                                cases += 1
        self.assertEqual(cases, 324)
        print('optional size wrapper:', cases, 'connected actual cache/lookup/block cases; both allocation failures')

    def test_connected_output_aliases_cache_clock_and_live_scratch(self):
        cases = 0
        for phase in (0, 8):
            for depth in (1, 3):
                for target in (lookup.CLOCK, buffer.SCRATCH, lookup.CACHE + 15 * 16 + 8):
                    for descriptor in (0x80000010, 0x90000011):
                        for failure in (0, 1, 2):
                            case = dict(lookupDescriptor=descriptor, failure=failure, decoded=32, mutation=True)
                            args = (target, depth, *([1] * depth))
                            models = [BlockOracle(words, memory_case(), args, phase, case, self.connected).run()
                                      for words in (self.retail, self.words)]
                            self.assert_models_equal(models[1], models[0])
                            self.assertEqual(models[0].lookups, depth)
                            calls = [call for call in models[0].calls if call[0] == BLOCK]
                            self.assertEqual(calls, [(BLOCK, 0xAB1950 + depth * 0x40, descriptor, target)])
                            expected = descriptor & 0x0FFFFFFF if failure == 1 else 0 if failure == 2 and descriptor == 0x90000011 else 32 if descriptor == 0x90000011 else 16
                            if target == buffer.SCRATCH and failure == 1:
                                expected = 0x4567
                            self.assertEqual(models[0].peek(target, 4), expected)
                            cases += 1
        self.assertEqual(cases, 72)
        print('optional size wrapper:', cases, 'connected output aliases to actual cache, clock and scratch')

    def test_connected_zero_depth_original_seed_and_allocation_failure_output(self):
        for phase in (0, 8):
            for seed in SEEDS:
                for optional in (False, True):
                    for failure in (0, 1):
                        memory = memory_case()
                        lookup.put_word(memory, buffer.table.STACK + phase - 0x18, seed)
                        args = (0 if optional else SIZE, 0, 1, 2)
                        models = [BlockOracle(words, memory, args, phase, dict(failure=failure, decoded=32), self.connected).run()
                                  for words in (self.retail, self.words)]
                        self.assert_models_equal(models[1], models[0])
                        target = buffer.table.STACK + phase - 0x10 if optional else SIZE
                        self.assertEqual(models[0].lookups, 0)
                        self.assertIn((BLOCK, 0xAB1950, seed, target), models[0].calls)
                        if failure:
                            self.assertEqual(models[0].r[2], 0)
                            self.assertEqual(models[0].peek(target, 4), 1)

    def test_full_game_caller_preserves_physical_fallback_and_followup_boundary(self):
        cases, coverage = 0, [set(), set()]
        for phase in (0, 8):
            for component in (1, 2, 3):
                for missing in range(-1, 2):
                    for descriptor in (0x80000010, 0x90000011):
                        for failure in (0, 1, 2):
                            case = dict(lookupDescriptor=descriptor, missing=missing, failure=failure, decoded=32)
                            models = []
                            for words in (self.retail, self.words):
                                code = self.connected.copy()
                                code.update(zip(range(ENTRY, ENTRY + 244, 4), words))
                                models.append(BlockOracle(self.caller, memory_case(), (component,), phase, case, code, CALLER).run())
                            self.assert_models_equal(models[1], models[0])
                            reference = models[0]
                            self.assertIn((ENTRY, 0, 2, 0x19, component), reference.calls)
                            for call in reference.calls:
                                if call[0] == lookup.ENTRY:
                                    self.assertEqual(call[3], buffer.table.STACK + phase - 0x30)
                                if call[0] == BLOCK:
                                    self.assertEqual(call[3], buffer.table.STACK + phase - 0x28)
                            self.assertEqual(reference.calls[-1], (FOLLOWUP,))
                            self.assertEqual(reference.r[2], 0x12345678)
                            loaded = missing < 0 and failure != 1 and not (descriptor & 0x70000000 == 0x10000000 and failure == 2)
                            pointer = EXPANDED if descriptor & 0x70000000 == 0x10000000 else buffer.TEMP
                            self.assertEqual(reference.peek(0x800D2350, 4), pointer + 4 if loaded else 0)
                            self.assertEqual(reference.peek(0x80087290, 2), reference.peek(pointer, 2) if loaded else 0)
                            self.assertEqual(reference.peek(0x80087294, 2), reference.peek(pointer + 2, 2) if loaded else 0)
                            for i, model in enumerate(models):
                                coverage[i].update(model.visits)
                            cases += 1
        self.assertEqual(cases, 108)
        self.assertTrue(all(set(range(CALLER, CALLER + 120, 4)) <= visits for visits in coverage))
        print('optional size wrapper:', cases, 'full 30-word caller cases; physical descriptor/fallback at SP-0x30/SP-0x28')

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
s32 size;u32 root=(u32)D_AB1950;int hit,optional,failure;
for(hit=0;hit<2;hit++) for(optional=0;optional<2;optional++) for(failure=0;failure<2;failure++) {
    reset();connected=1;expectedAddress=(root+8)&0x7FFFFFF0;connectedAddress=root+0x20;
    expectedLength=32;descriptor=0x80000010;failAllocation=failure;
    if(hit) { D_800C3D68[15].address=(root+8)|0x80000000;D_800C3D68[15].offset=0x20;
              D_800C3D68[15].descriptor=descriptor;dmaPhase=1; }
    size=-99;
    if(func_1502B5C8(optional?NULL:&size,1,1)!=(failure?NULL:compressed)
       || error || size!=(optional?-99:16) || allocations!=1 || decodes || frees
       || dmas!=(hit?0:1)+(failure?0:1) || copies!=!hit) return 1;
}
''')
        finally:
            self.fixture = original

    def test_production_body_and_all_six_complete_caller_slots(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        self.assertEqual(re.search(r'void \*func_1502B5C8\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0), source_body())
        self.assertNotRegex(source_body(), r'descriptor\s*=')
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        measured = [('func_1502B5C8', 61, 0x50, '3e5a7f5d2eb6e43e30fefad7ef24f5cb4f7880de2bb8040cf05e4c437e8f0568'),
            ('func_151D2AB0', 39, 0x20, '567ca1536ad5aae6e9cfb1d12f76799610e30d8f29f5b62b8f1f391674ad2428'),
            ('func_1509B8FC', 21, 0x20, '213e09c4c5a89cd47ee384637e0a864b78202411e86095581bc99dda4fdddd70'),
            ('func_15017578', 26, 0x28, '4043b1c317629655f606f67279f4d896b66d5dc7b293961de2e2b12b942c1d69'),
            ('func_151F2960', 146, 0x18, '817a4892fe725a27d02014723e552204e36a8c7393d904d69916231557f9582f'),
            ('func_15085B70', 30, 0x18, '420680f426f2b1f2b80d4d03a344b7ca8de125e0cc9067820c2464ec5e5d5a19'),
            ('func_150025FC', 50, 0x28, '236873814d601a42059f592b8f0918bdeaee8639d78de7272340396b1a617633')]
        for name, count, frame, digest in measured:
            words = functions[name]
            self.assertEqual(addresses[name], int(name[5:], 16))
            self.assertEqual(len(words), count)
            self.assertEqual(words[0], 0x27BD0000 | ((-frame) & 0xFFFF))
            self.assertEqual(hashlib.sha256(struct.pack('>' + str(count) + 'I', *words)).hexdigest(), digest)
            offset = 0x2D4B0 + addresses[name] - 0x15000000
            self.assertEqual(words, list(struct.unpack_from('>' + str(count) + 'I', self.rom, offset)))
        prototype = 'void *func_1502B5C8(s32 *size, u32 depth, ...);'
        for file in ('game_57FA0.c', 'game_2DF70.c', 'game_1FFF60.c', 'game_447B0.c',
                     'game_C8950.c', 'game/generated_B3020.c', 'libultra/audio/game_21FC90.c'):
            self.assertIn(prototype, (self.root / 'conker/src' / file).read_text())

    def test_unlinked_relocations_and_no_word_guards(self):
        output = subprocess.run(['mips-linux-gnu-objdump', '-r', str(self.output / 'selected.o')],
                                check=True, capture_output=True, text=True).stdout
        actual = {int(o, 16): (kind, symbol) for o, kind, symbol in re.findall(
            r'(?m)^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\S+)\s*$', output)}
        self.assertEqual(actual, {0x44: ('R_MIPS_HI16', 'D_AB1950'), 0x48: ('R_MIPS_LO16', 'D_AB1950'),
                                 0x80: ('R_MIPS_26', 'func_1502AC88'), 0xBC: ('R_MIPS_26', 'func_1502B350')})
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            self.assertFalse(any(r['function'] == 'func_1502B5C8' for r in csv.DictReader(file)))


if __name__ == '__main__':
    unittest.main()
