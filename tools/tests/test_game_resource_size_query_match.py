"""Direct size query; incoming descriptor seeds are target-only qualification."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_resource_size_query_candidates as screen
from tools.tests import test_game_optional_size_loader_match as optional
from tools.match_progress import load_elf_functions


buffer, lookup, installer = optional.buffer, optional.lookup, optional.installer
ENTRY, CALLER, LOAD, RESOLVE = 0x1502B9B4, 0x10008180, 0x1502B8E0, 0x1502B020
DMA = buffer.table.DMA
SEEDS = optional.SEEDS + (0x10000000, 0x90000000)
HEADERS = (0, 0x80000001, 0xFFFFFFFF)
LENGTHS = (0, 1, 16, 17, 0x0FFFFFFE, 0x0FFFFFFF)


def source_body():
    return dict(screen.candidates())['selected-size-first']


def header_address(home):
    first = home - 0x30
    return first + (8 if first & 8 else 0)


def memory_case():
    return buffer.memory_case()


class BoundaryOracle(buffer.table.RangeOracle):
    """Retail instructions with descriptor-writing/retaining lookup and DMA hooks."""

    def __init__(self, words, memory, arguments, phase=0, case=None):
        super().__init__(words, memory, arguments, phase, entry=ENTRY)
        self.case, self.lookups = case or {}, 0
        self.home = buffer.table.STACK + phase

    def record_call(self, target):
        assert target in (lookup.ENTRY, DMA)
        count = 3 if target == lookup.ENTRY else 4
        call = (target, *self.r[4:4 + count])
        self.calls.append(call)
        self.events.append(('CALL', *call))

    def hook(self, target):
        if target == lookup.ENTRY:
            index = self.lookups
            self.lookups += 1
            if not self.case.get('unwritten'):
                descriptor = self.case.get('descriptor', 0x80000010) + index
                self.put(self.r[6], 0xF0000000 if index == self.case.get('missing', -1) else descriptor, 4)
            result = 0xFFFFFFF0 if self.case.get('wrap') and index == 0 else 8 * (index + 1)
        else:
            assert self.r[5] == header_address(self.home) and self.r[5] & 15 == 0
            assert self.r[6:8] == [16, 1]
            for i in range(4):
                self.put(self.r[5] + i * 4, self.case.get('header', 0xFFFFFFFF) if i == 0 else 0xCA000000 + i, 4)
            if self.case.get('mutation'):
                self.put(self.home - 0x14, 0, 4)
            result = self.case.get('dmaReturn', 0xDEADBEEF)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result & 0xFFFFFFFF


class BankLoadBoundary(Exception):
    """Stop before the bank load; allocator/audio/runtime acceptance is separate."""


class ConnectedOracle(buffer.BufferOracle):
    """Actual cache/lookup/query instructions; Init setup and allocation are opaque."""

    def __init__(self, words, memory, arguments, phase=0, case=None, connected=None, entry=ENTRY):
        super().__init__(words, memory, arguments, phase, case, connected, entry)
        self.home = buffer.table.STACK + phase if entry == ENTRY else None
        self.headers = 0

    def record_call(self, target):
        count = {ENTRY: 1, CALLER: 0, LOAD: 4, RESOLVE: 4,
                 0x10012820: 3, 0x10008F90: 3}.get(target)
        if count is None:
            super().record_call(target)
        else:
            call = (target, *self.r[4:4 + count])
            self.calls.append(call)
            self.events.append(('CALL', *call))
            if target == ENTRY:
                self.home = self.r[29]

    def hook(self, target):
        if target == DMA and self.home is not None and self.r[5] == header_address(self.home):
            assert self.r[5] & 15 == 0 and self.r[6:8] == [16, 1]
            self.headers += 1
            for i in range(4):
                self.put(self.r[5] + i * 4, self.case.get('header', 0xFFFFFFFF) if i == 0 else 0xCA000000 + i, 4)
            if self.case.get('mutation'):
                self.put(self.home - 0x14, 0, 4)
            result = self.case.get('dmaReturn', 0xDEADBEEF)
        elif target == LOAD:
            raise BankLoadBoundary()
        elif target in (RESOLVE, 0x10012820, 0x10008F90, buffer.ALLOC):
            if target == RESOLVE:
                assert self.r[4:8] == [0, 2, 0x17, 2]
            if target == buffer.ALLOC:
                assert self.r[5:8] == [0xFF, 2, 0]
            result = buffer.table.BUFFER
        else:
            super().hook(target)
            return
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result & 0xFFFFFFFF


class GameResourceSizeQueryMatchTests(unittest.TestCase):
    run_host = buffer.GameBufferResourceLoaderTests.run_host
    assert_models_equal = buffer.GameBufferResourceLoaderTests.assert_models_equal

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(n) is None for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-resource-size-query-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', source_body())
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>71I', cls.rom, 0x58E64))
        cls.caller = list(struct.unpack_from('>214I', cls.rom, 0x8180))
        _, raw_lookup = lookup.screen.compile_candidate(cls.root, cls.output, 'lookup', lookup.source_body())
        _, raw_cache = installer.screen.compile_candidate(cls.root, cls.output, 'cache', installer.source_body())
        cls.connected = {}
        for address, words in ((lookup.ENTRY, lookup.apply_linked_guards(raw_lookup)),
                               (lookup.INSTALL, installer.apply_linked_guards(raw_cache))):
            cls.connected.update(zip(range(address, address + len(words) * 4, 4), words))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.sdk = (cls.root / 'conker/include/libc/stdarg.h').read_text()
        # GCC's i386 u64 alignment differs from MIPS o32; make that ABI premise explicit.
        cls.types = 'typedef unsigned char u8; typedef int s32; typedef unsigned int u32;\ntypedef unsigned long long u64 __attribute__((aligned(8)));\n'
        cls.fixture = cls.sdk + '\n' + cls.types + r'''
u8 D_AB1950[16] __attribute__((aligned(16)));
static s32 items[16];static u32 metadata[16],advances[16],expectedBase,depth,headerWord,*lastDescriptor;
static int lookups,dmas,consumed,error,missing,mutation;
static void reset(u32 count,int absent,int pattern,u32 flags) {
    int i;depth=count;missing=absent;lookups=dmas=consumed=error=mutation=0;lastDescriptor=(void *)0;
    expectedBase=(u32)D_AB1950;headerWord=pattern==2?0:pattern==1?0xFFFFFFFF:0x80000001;
    for(i=0;i<16;i++) {items[i]=pattern==2?1:i+1;advances[i]=(u32)(8*(i+1));metadata[i]=flags|((u32)i+1);}
    if(pattern==1) {items[0]=-1;items[1]=(s32)0x80000000;items[2]=0x7FFFFFFF;advances[0]=0xFFFFFFF0;}
    if(absent>=0) metadata[absent]=0xF0000000;
}
s32 func_1502AC88(u32 base,s32 item,u32 *descriptor) {
    int i=lookups++;
    if(base!=expectedBase || item!=items[i] || dmas || i>=(missing<0?(int)depth:missing+1)
       || (lastDescriptor && lastDescriptor!=descriptor)) error=1;
    *descriptor=metadata[i];lastDescriptor=descriptor;expectedBase+=advances[i];return (s32)advances[i];
}
s32 func_10004514(u32 base,void *out,u32 length,s32 mode) {
    u32 *words=out;int i;dmas++;
    if(base!=expectedBase || dmas!=1 || ((u32)out&15) || length!=16 || mode!=1
       || lookups!=(int)depth || consumed!=(int)depth) error=2;
    for(i=0;i<4;i++) words[i]=i?0xCA000000+(u32)i:headerWord;
    if(mutation) *lastDescriptor=0;
    return -123;
}
#undef va_arg
#define va_arg(path,type) (consumed++,__builtin_va_arg(path,type))
/* Native cases always write the descriptor before reading it. */
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
''' + source_body() + '\n#pragma GCC diagnostic pop\n'

    def test_direct_body_frame_slot_controls_and_no_guards(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (69, 0x68, 0))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(len(screen.candidates()), 136)
        for name, expected in (('placeholder', (3, 0, 69)), ('baseline', (69, 0x68, 7)),
                               ('layout-1', (69, 0x68, 4)), ('buffer-u64', (69, 0x68, 5)),
                               ('selected-u64', (69, 0x68, 2)), ('selected-comma-init', (69, 0x68, 2)),
                               ('selected-zero-descriptor', (71, 0x68, 58)), ('selected-one-descriptor', (71, 0x68, 58))):
            record, _ = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')
        self.assertEqual(self.words[-2:], [0, 0])
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            self.assertFalse(any(r['function'] == 'func_1502B9B4' for r in csv.DictReader(file)))

    def test_native_positive_depth_flags_missing_and_all_component_consumption(self):
        self.run_host(r'''
int d,absent,pattern,flag,cases=0,compressed;u32 result,expected;
for(pattern=0;pattern<3;pattern++) for(d=1;d<=16;d++) for(absent=-1;absent<d;absent++)
for(flag=0;flag<16;flag++) {
    reset((u32)d,absent,pattern,(u32)flag<<28);mutation=1;
    result=func_1502B9B4(depth,items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],
                       items[8],items[9],items[10],items[11],items[12],items[13],items[14],items[15]);
    compressed=(flag&7)==1;expected=absent>=0?0:compressed?headerWord:(((u32)d+1)&~1u);
    if(error || result!=expected || consumed!=d || lookups!=(absent<0?d:absent+1)
       || dmas!=(absent<0 && compressed)) return 1;
    cases++;
}
if(cases!=7296) return 2;
''')

    def test_target_boundary_seeds_rounding_header_reload_and_full_coverage(self):
        cases, coverage = 0, [set(), set()]
        for depth in range(7):
            for missing in range(-2, depth):
                for phase in (0, 8):
                    for seed in SEEDS:
                        for descriptor in (0x80000010, 0x10000010, 0x90000011):
                            for header in HEADERS:
                                memory = memory_case()
                                home = buffer.table.STACK + phase
                                lookup.put_word(memory, home - 0x14, seed)
                                case = dict(unwritten=missing == -2, missing=missing, wrap=True,
                                            descriptor=descriptor, header=header, mutation=True)
                                models = [BoundaryOracle(words, memory, (depth, -1, 0x80000000, 3, 4, 5, 6), phase, case).run()
                                          for words in (self.retail, self.words)]
                                self.assert_models_equal(models[1], models[0])
                                reference = models[0]
                                expected = 0 if depth == 0 else 1 if missing == -2 and not seed & 0x0FFFFFFF else missing + 1 if missing >= 0 else depth
                                self.assertEqual(reference.lookups, expected)
                                active = depth == 0 or missing < 0 and (missing != -2 or seed & 0x0FFFFFFF != 0)
                                final = seed if depth == 0 or missing == -2 else descriptor + depth - 1
                                compressed = active and final & 0x70000000 == 0x10000000
                                result = 0 if not active else header if compressed else ((final & 0x0FFFFFFF) + 1) & ~1
                                self.assertEqual(reference.r[2], result)
                                base = (0xAB1950 + (0xFFFFFFF0 if expected else 0) + sum(8 * (i + 1) for i in range(1, expected))) & 0xFFFFFFFF
                                calls = [call for call in reference.calls if call[0] == DMA]
                                self.assertEqual(calls, [(DMA, base, header_address(home), 16, 1)] if compressed else [])
                                if compressed:
                                    self.assertEqual(reference.peek(header_address(home), 4), header)
                                for i, model in enumerate(models):
                                    coverage[i].update(model.visits)
                                cases += 1
        self.assertEqual(cases, 5670)
        self.assertEqual(coverage, [set(range(ENTRY, ENTRY + 276, 4))] * 2)
        print('resource size query:', cases, 'target boundary cases; all 69 body words, both header choices and original seeds')

    def test_live_header_load_ignores_dma_return_and_mutated_descriptor(self):
        for phase in (0, 8):
            for header in HEADERS:
                for dmaReturn in (0, 1, 0xFFFFFFFF):
                    case = dict(descriptor=0x90000011, header=header, dmaReturn=dmaReturn, mutation=True)
                    models = [BoundaryOracle(words, memory_case(), (1, 1, 2), phase, case).run()
                              for words in (self.retail, self.words)]
                    self.assert_models_equal(models[1], models[0])
                    self.assertEqual(models[0].r[2], header)
                    self.assertEqual(models[0].peek(buffer.table.STACK + phase - 0x14, 4), 0)
        stale = self.words[:]
        self.assertEqual(stale[0xEC // 4], 0x8E030000)
        stale[0xEC // 4] = 0x00401825
        case = dict(descriptor=0x90000011, header=0x80000001, dmaReturn=0xFFFFFFFF)
        reference = BoundaryOracle(self.retail, memory_case(), (1, 1, 2), case=case).run()
        actual = BoundaryOracle(stale, memory_case(), (1, 1, 2), case=case).run()
        self.assertNotEqual(actual.r[2], reference.r[2])

    def test_zero_depth_initializers_and_wrong_buffer_layout_fail_physical_witnesses(self):
        memory = memory_case()
        lookup.put_word(memory, buffer.table.STACK - 0x14, 0x90000011)
        reference = BoundaryOracle(self.retail, memory, (0, 1, 2)).run()
        for name in ('selected-zero-descriptor', 'selected-one-descriptor'):
            _, words = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            actual = BoundaryOracle(words, memory, (0, 1, 2)).run()
            self.assertNotEqual(actual.calls, reference.calls)
            self.assertNotEqual(actual.memory, reference.memory)
        _, wrong = screen.compile_candidate(self.root, self.output, 'wrong-buffer', dict(screen.candidates())['layout-1'])
        with self.assertRaises(AssertionError):
            BoundaryOracle(wrong, memory, (0, 1, 2)).run()

    def test_connected_actual_cache_lookup_raw_lengths_compressed_headers_and_missing(self):
        cases = 0
        for phase in (0, 8):
            for depth in range(1, 4):
                for missing in range(-1, depth):
                    for flags in (0x80000000, 0x10000000, 0x90000000):
                        for length in LENGTHS:
                            for header in HEADERS:
                                descriptor = flags | length
                                case = dict(lookupDescriptor=descriptor, missing=missing, header=header, mutation=True)
                                models = [ConnectedOracle(words, memory_case(), (depth, *([1] * depth)), phase, case, self.connected).run()
                                          for words in (self.retail, self.words)]
                                self.assert_models_equal(models[1], models[0])
                                active = length != 0 and missing < 0
                                compressed = active and flags & 0x70000000 == 0x10000000
                                self.assertEqual(models[0].r[2], 0 if not active else header if compressed else length + (length & 1))
                                self.assertEqual(models[0].headers, int(compressed))
                                self.assertEqual(models[0].lookups, 1 if length == 0 else depth if missing < 0 else missing + 1)
                                self.assertTrue(all(call[0] in (lookup.ENTRY, lookup.INSTALL, lookup.COPY, DMA) for call in models[0].calls))
                                cases += 1
        self.assertEqual(cases, 972)
        print('resource size query:', cases, 'connected actual lookup/cache cases; rounded raw lengths and unmasked headers')

    def test_connected_zero_depth_compressed_zero_length_still_reads_header(self):
        for phase in (0, 8):
            for seed in SEEDS:
                for header in HEADERS:
                    memory = memory_case()
                    home = buffer.table.STACK + phase
                    lookup.put_word(memory, home - 0x14, seed)
                    case = dict(header=header, mutation=True)
                    models = [ConnectedOracle(words, memory, (0, 1, 2), phase, case, self.connected).run()
                              for words in (self.retail, self.words)]
                    self.assert_models_equal(models[1], models[0])
                    compressed = seed & 0x70000000 == 0x10000000
                    self.assertEqual(models[0].lookups, 0)
                    self.assertEqual(models[0].headers, int(compressed))
                    self.assertEqual(models[0].r[2], header if compressed else ((seed & 0x0FFFFFFF) + 1) & ~1)

    def test_init_audio_prefix_preserves_query_count_allocation_and_bank_load_arguments(self):
        cases, visits = 0, [set(), set()]
        for phase in (0, 8):
            for missing in (-1, 0, 1):
                for descriptor in (0x80000010, 0x80000011, 0x10000010, 0x90000011):
                    for header in HEADERS:
                        case = dict(lookupDescriptor=descriptor, missing=missing, header=header)
                        models = []
                        for words in (self.retail, self.words):
                            code = self.connected.copy()
                            code.update(zip(range(ENTRY, ENTRY + 284, 4), words))
                            model = ConnectedOracle(self.caller, memory_case(), (), phase, case, code, CALLER)
                            with self.assertRaises(BankLoadBoundary):
                                model.run()
                            models.append(model)
                        self.assert_models_equal(models[1], models[0])
                        reference = models[0]
                        compressed = descriptor & 0x70000000 == 0x10000000
                        size = 0 if missing >= 0 else header if compressed else (descriptor & 0x0FFFFFFF) + (descriptor & 1)
                        self.assertIn((ENTRY, 2), reference.calls)
                        self.assertIn((buffer.ALLOC, size, 0xFF, 2, 0), reference.calls)
                        self.assertEqual(reference.calls[-1], (LOAD, buffer.table.BUFFER, size, 2, 0x17))
                        self.assertEqual(reference.peek(buffer.table.STACK + phase - 0xF0 + 0x10, 4), 0)
                        self.assertEqual(reference.r[29], buffer.table.STACK + phase - 0xF0)
                        self.assertEqual(reference.r[16], size)
                        self.assertEqual([call[2] for call in reference.calls if call[0] == lookup.ENTRY], [0x17, 0][:2 if missing < 0 else missing + 1])
                        for call in reference.calls:
                            if call[0] == lookup.ENTRY:
                                self.assertEqual(call[3], buffer.table.STACK + phase - 0x104)
                            if call[0] == DMA and call[2] == header_address(buffer.table.STACK + phase - 0xF0):
                                self.assertEqual(call[3:], (16, 1))
                        for i, model in enumerate(models):
                            visits[i].update(model.visits)
                        cases += 1
        self.assertEqual(cases, 72)
        self.assertTrue(all(set(range(CALLER, 0x10008288, 4)) <= v for v in visits))
        print('resource size query:', cases, 'actual Init caller prefixes; first 66 words, stop before bank load')

    def test_native_connected_actual_cache_lookup_hit_miss_and_size_query(self):
        original = self.fixture
        try:
            self.fixture = self.sdk + '\n' + self.types + r'''
u8 D_AB1950[16] __attribute__((aligned(16)));
typedef struct AssetTableCache57FA0 {u32 address,generation,offset,descriptor;} AssetTableCache57FA0;
AssetTableCache57FA0 D_800C3D68[16];u32 D_800C3D60;
static u32 descriptor,headerWord,root;static int dmas,copies,error,hit;
static void reset(int cached,u32 desc,u32 header) {
    int i;root=(u32)D_AB1950;hit=cached;descriptor=desc;headerWord=header;dmas=copies=error=0;
    D_800C3D60=0;
    for(i=0;i<16;i++) {D_800C3D68[i].address=0;D_800C3D68[i].generation=0;D_800C3D68[i].offset=0;D_800C3D68[i].descriptor=0;}
    if(hit) {D_800C3D68[15].address=(root+8)|0x80000000;D_800C3D68[15].offset=0x20;D_800C3D68[15].descriptor=desc;}
}
void bcopy(void *source,void *destination,s32 length) {
    int i;u8 *s=source,*d=destination;copies++;
    if(destination!=D_800C3D68 || length!=224) error=1;
    for(i=0;i<length;i++) d[i]=s[i];
}
s32 func_10004514(u32 address,void *out,u32 length,s32 mode) {
    int i;u32 *words=out;dmas++;
    if((u32)out&15 || mode!=1) error=2;
    if(!hit && dmas==1) {
        if(address!=root || length!=32) error=3;
        for(i=0;i<8;i++) words[i]=i&1?descriptor:0x10+(u32)(i/2)*0x10;
    } else {
        if(address!=root+0x20 || length!=16 || (descriptor&0x70000000)!=0x10000000) error=4;
        for(i=0;i<4;i++) words[i]=i?0xCA000000+(u32)i:headerWord;
    }
    return -123;
}
''' + installer.source_body() + '\n' + lookup.source_body() + r'''
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
''' + source_body() + '\n#pragma GCC diagnostic pop\n'
            self.run_host(r'''
int cached,flag,length,h,cases=0;u32 headers[3]={0,0x80000001,0xFFFFFFFF},result,expected;
for(cached=0;cached<2;cached++) for(flag=0;flag<16;flag++) for(length=0;length<4;length++) for(h=0;h<3;h++) {
    reset(cached,((u32)flag<<28)|(u32)length,headers[h]);
    result=func_1502B9B4(1,1);
    expected=length==0?0:(flag&7)==1?headers[h]:((u32)length+1)&~1u;
    if(error || result!=expected || copies!=!cached || dmas!=!cached+(length!=0 && (flag&7)==1)) return 1;
    cases++;
}
if(cases!=384) return 2;
''')
        finally:
            self.fixture = original

    def test_production_body_prototypes_and_complete_init_caller_slot(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        self.assertEqual(re.search(r'u32 func_1502B9B4\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0), source_body())
        self.assertNotRegex(source_body(), r'descriptor\s*=')
        prototype = 'u32 func_1502B9B4(u32 depth, ...);'
        self.assertIn(prototype, source)
        self.assertIn(prototype, (self.root / 'conker/src/init_8180.c').read_text())
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        for name, expected, address in (('func_1502B9B4', self.retail, ENTRY), ('func_10008180', self.caller, CALLER)):
            self.assertEqual(addresses[name], address)
            self.assertEqual(functions[name], expected)
        self.assertEqual(self.caller[0], 0x27BDFF10)
        self.assertEqual(hashlib.sha256(struct.pack('>214I', *self.caller)).hexdigest(),
                         'e5edcb6039f9b8e816dacd1dea8996ed458a81fa7a68f9f342ef13de781a5dbf')

    def test_unlinked_relocations(self):
        output = subprocess.run(['mips-linux-gnu-objdump', '-r', str(self.output / 'selected.o')],
                                check=True, capture_output=True, text=True).stdout
        actual = {int(o, 16): (kind, symbol) for o, kind, symbol in re.findall(
            r'(?m)^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\S+)\s*$', output)}
        self.assertEqual(actual, {0x2C: ('R_MIPS_HI16', 'D_AB1950'), 0x34: ('R_MIPS_LO16', 'D_AB1950'),
                                 0x70: ('R_MIPS_26', 'func_1502AC88'), 0xE4: ('R_MIPS_26', 'func_10004514')})


if __name__ == '__main__':
    unittest.main()
