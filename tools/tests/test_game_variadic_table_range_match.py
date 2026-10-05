"""SDK-varargs wrapper recovery with checked independent loop stores and real callees."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_variadic_table_range_candidates as screen
from tools.tests import test_game_table_range_loader as table
from tools.tests import test_game_cached_lookup_match as lookup
from tools.tests import test_game_cache_installer_match as installer
from tools.tests import test_game_random_curve_record as native
from tools.tests.game_animation_timeline_oracle import TimelineOracle
from tools.match_progress import load_elf_functions


ENTRY = 0x1502B110
GUARDS = {0xAC: (0xAFA8003C, 0xAFA70054), 0xB4: (0xAFA70054, 0xAFA8003C)}


def source_body():
    return dict(screen.candidates())['baseline-layout-17']


def apply_linked_guards(words, omitted=None):
    result = words[:]
    for offset, (expected, replacement) in GUARDS.items():
        assert result[offset // 4] == expected
        if offset != omitted:
            result[offset // 4] = replacement
    return result


def components(pattern):
    if pattern == 0:
        return list(range(1, 17))
    if pattern == 1:
        return [0xFFFFFFFF, 0x80000000, 0x7FFFFFFF] + list(range(4, 17))
    return [1] * 16


class BoundaryOracle(table.RangeOracle):
    """Lookup/range boundaries are modeled here; connected tests below execute them."""

    def __init__(self, words, memory, arguments, phase=0, pattern=0, missing=-1):
        super().__init__(words, memory, arguments, phase, pattern, entry=ENTRY)
        self.missing, self.lookups = missing, 0

    def record_call(self, target):
        assert target in (lookup.ENTRY, table.ENTRY)
        self.calls.append((target, *(self.r[4:8] if target == table.ENTRY else self.r[4:7])))
        self.events.append(('CALL', *self.calls[-1]))

    def hook(self, target):
        if target == lookup.ENTRY:
            i = self.lookups
            self.lookups += 1
            if self.missing != -2:
                self.put(self.r[6], 0xF0000000 if i == self.missing else 0xF0000010 + i, 4)
            result = (0xFFFFFFF0 if self.pattern == 1 and i == 0 else 8 * (i + 1))
        else:
            assert target == table.ENTRY
            result = 0 if self.pattern == 2 else self.r[5] + 4
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result & 0xFFFFFFFF


def read_windows(model):
    windows, stores = [], []
    for event in model.events + [('END',)]:
        if event[0] == 'W':
            stores.append(event[1:])
        else:
            windows.append((tuple(stores), event))
            stores = []
    return windows


class GameVariadicTableRangeMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(n) is None for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-variadic-table-range-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, cls.output, 'selected', source_body())
        cls.guarded = apply_linked_guards(cls.raw)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>69I', rom, 0x585C0))
        cls.connected = {}
        _, range_words = table.screen.compile_candidate(cls.root, cls.output, 'range', table.source_body())
        _, raw_lookup = lookup.screen.compile_candidate(cls.root, cls.output, 'lookup', lookup.source_body())
        _, raw_cache = installer.screen.compile_candidate(cls.root, cls.output, 'cache', installer.source_body())
        for address, words in ((table.ENTRY, range_words),
                (lookup.ENTRY, lookup.apply_linked_guards(raw_lookup)),
                (lookup.INSTALL, installer.apply_linked_guards(raw_cache))):
            cls.connected.update(zip(range(address, address + len(words) * 4, 4), words))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = ('typedef unsigned char u8; typedef int s32; typedef unsigned int u32;\n'
                     '#define NULL ((void *)0)\n')
        cls.sdk = (cls.root / 'conker/include/libc/stdarg.h').read_text()
        cls.fixture = cls.sdk + '\n' + cls.types + r'''
u8 D_AB1950[16] __attribute__((aligned(16)));
static u8 storage[640] __attribute__((aligned(16)));
static s32 items[16]; static u32 advances[16],metadata[16];
static u32 expectedBase,expectedCount,expectedDepth,*lastDescriptor;
static int lookups,ranges,consumed,error,expectedLookups,missing,pattern,nullResult;
static void *expectedBuffer;
static void reset(u32 root,u32 count,u32 depth,int absent,int phase) {
    int i; missing=absent; pattern=phase; expectedCount=count; expectedDepth=depth;
    expectedBase=root?root:(u32)D_AB1950; expectedBuffer=storage+32;
    lookups=ranges=consumed=error=0; lastDescriptor=NULL; nullResult=phase==2;
    expectedLookups=depth>=2?(int)depth-1:0;
    if(absent>=0 && absent<expectedLookups) expectedLookups=absent+1;
    for(i=0;i<16;i++) {
        items[i]=phase==2?1:i+1; advances[i]=(u32)(8*(i+1)); metadata[i]=0xF0000010u+(u32)i;
    }
    if(phase==1) { items[0]=-1; items[1]=(s32)0x80000000; items[2]=0x7FFFFFFF; advances[0]=0xFFFFFFF0; }
    if(absent>=0) metadata[absent]=0xF0000000;
}
s32 func_1502AC88(u32 base,s32 component,u32 *descriptor) {
    int i=lookups++;
    if(i>=expectedLookups || base!=expectedBase || component!=items[i] || ranges
       || (lastDescriptor && descriptor!=lastDescriptor)
       || *descriptor!=(i==0 || missing==-2?1:metadata[i-1]&0x0FFFFFFF)) error=1;
    lastDescriptor=descriptor;
    if(missing!=-2) *descriptor=metadata[i];
    expectedBase+=advances[i];
    return (s32)advances[i];
}
u32 *func_1502AF04(u32 base,void *buffer,u32 component,u32 count) {
    ranges++;
    if(ranges!=1 || lookups!=expectedLookups || base!=expectedBase || count!=expectedCount
       || buffer!=expectedBuffer || component!=(u32)items[expectedDepth>=2?expectedDepth-1:0]) error=2;
    return nullResult?NULL:(u32 *)((u8 *)buffer+4);
}
#undef va_arg
#define va_arg(path,type) (consumed++,__builtin_va_arg(path,type))
''' + source_body() + '\n'

    def assert_windows_equal(self, actual, reference):
        a, b = read_windows(actual), read_windows(reference)
        self.assertEqual(len(a), len(b))
        for (stores, event), (expected, following) in zip(a, b):
            self.assertEqual(event, following)
            if stores != expected:
                self.assertEqual(sorted(stores), sorted(expected))
                self.assertEqual(len(stores), 2)
                sp = actual.before[29]
                self.assertEqual({(address, size) for address, size, _ in stores}, {(sp - 12, 4), (sp + 12, 4)})
                occupied = set()
                for address, size, _ in stores:
                    addresses = set(range(address, address + size))
                    self.assertFalse(occupied & addresses)
                    occupied.update(addresses)

    def test_full_raw_frame_and_guarded_slot_with_source_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (69, 0x48, 2))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(hashlib.sha256(struct.pack('>69I', *self.raw)).hexdigest(),
                         'b249fec226d56f27cdf2471a0a1b283cacde2654b3befa32a1bf03364511f08d')
        self.assertEqual(hashlib.sha256(struct.pack('>69I', *self.retail)).hexdigest(),
                         'd2a96c6abbb8424685a7350199fa6fb7e1c2d6ef9c4b3c3fd7004f41ec548a4f')
        self.assertEqual({i * 4 for i, (a, b) in enumerate(zip(self.raw, self.retail)) if a != b}, set(GUARDS))
        self.assertEqual(self.guarded, self.retail)
        for name, expected in (('placeholder', (3, 0, 69)), ('baseline', (69, 0x48, 10)),
                               ('baseline-layout-2', (69, 0x48, 5)), ('selected-do-while', (69, 0x48, 2))):
            record, _ = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')

    def test_native_argument_consumption_and_descriptor_gate_matrix(self):
        self.run_host(r'''
static u32 roots[]={0,0x12340,0xFFFFFFF8},counts[]={0,5,0xFFFFFFFF};
int depth,absent,phase,root,cases=0; u32 *result;
for(phase=0;phase<3;phase++) for(root=0;root<3;root++) for(depth=0;depth<=16;depth++)
for(absent=-2;absent<(depth>=2?depth-1:0);absent++) {
    reset(roots[root],counts[phase],depth,absent,phase);
    result=func_1502B110(roots[root],counts[phase],expectedBuffer,(u32)depth,
        items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],
        items[8],items[9],items[10],items[11],items[12],items[13],items[14],items[15]);
    if(error || consumed!=(depth?depth:1) || lookups!=expectedLookups
       || ranges!=(absent<0) || result!=(absent>=0 || nullResult?NULL:(u32 *)((u8 *)expectedBuffer+4))) return 1;
    cases++;
}
if(cases!=1386) return 2;
''')

    def test_native_unwritten_descriptor_and_skipped_null_buffer(self):
        self.run_host(r'''
reset(0xFFFFFFF8,0xFFFFFFFF,3,-2,0);
if(func_1502B110(0xFFFFFFF8,0xFFFFFFFF,expectedBuffer,3,items[0],items[1],items[2])
   !=(u32 *)((u8 *)expectedBuffer+4) || error || consumed!=3 || lookups!=2 || ranges!=1) return 1;
reset(0,16,4,0,0); expectedBuffer=NULL;
if(func_1502B110(0,16,NULL,4,items[0],items[1],items[2],items[3])
   || error || consumed!=4 || lookups!=1 || ranges) return 2;
''')

    def test_boundary_three_way_complete_memory_and_independent_store_windows(self):
        coverage = [set(), set(), set()]
        cases = 0
        for pattern in range(3):
            items = components(pattern)
            for root in (0, 0x12340, 0xFFFFFFF8):
                for depth in range(17):
                    for missing in range(-2, max(depth - 1, 0)):
                        for phase in (0, 8):
                            for count in (0, 5, 0xFFFFFFFF):
                                memory = table.memory_case(pattern)
                                args = (root, count, table.BUFFER + 8, depth, *items)
                                models = [BoundaryOracle(words, memory, args, phase, pattern, missing).run()
                                          for words in (self.retail, self.raw, self.guarded)]
                                reference = models[0]
                                expected_lookups = min(missing + 1, max(depth - 1, 0)) if missing >= 0 else max(depth - 1, 0)
                                self.assertEqual(reference.lookups, expected_lookups)
                                self.assertEqual(sum(c[0] == table.ENTRY for c in reference.calls), int(missing < 0))
                                self.assertEqual([a for a, size, _ in reference.reads if size == 4
                                                  and table.STACK + phase + 0x10 <= a < table.STACK + phase + 0x50],
                                                 [table.STACK + phase + 0x10 + i * 4 for i in range(max(depth, 1))])
                                for i, model in enumerate(models):
                                    coverage[i].update(model.visits)
                                    self.assertEqual(model.memory, reference.memory)
                                    self.assertEqual(model.calls, reference.calls)
                                    self.assertEqual(model.reads, reference.reads)
                                    self.assertEqual(model.r[2], reference.r[2])
                                    self.assert_windows_equal(model, reference)
                                self.assertEqual(models[2].events, reference.events)
                                cases += 1
        self.assertEqual(cases, 8316)
        self.assertEqual(coverage, [set(range(ENTRY, ENTRY + 276, 4))] * 3)
        print('variadic table range:', cases, 'three-way boundary cases; all 69 words and independent loop stores')

    def test_each_omitted_guard_is_rejected(self):
        memory = table.memory_case()
        args = (0x12340, 5, table.BUFFER + 8, 3, 1, 2, 3)
        for offset in GUARDS:
            reference = BoundaryOracle(self.retail, memory, args, missing=0).run()
            try:
                partial = BoundaryOracle(apply_linked_guards(self.raw, offset), memory, args, missing=0).run()
                rejected = partial.memory != reference.memory or partial.events != reference.events
            except (AssertionError, KeyError):
                rejected = True
            self.assertTrue(rejected, hex(offset))

    def test_connected_three_way_lookup_range_cache_cases(self):
        cases, coverage = 0, [set(), set(), set()]
        for phase in (0, 8):
            for root in (0, 0x12340):
                for depth in (0, 1, 2, 3, 5):
                    for count in (0, 1, 2, 5, 16):
                        for caller_buffer in (False, True):
                            memory = table.memory_case(1)
                            memory.update({table.STACK + i: 0xA5 for i in range(0xC0, 0x200)})
                            buffer = table.STACK + phase + 0x80 if caller_buffer else table.BUFFER + 8
                            args = (root, count, buffer, depth, *([1] * max(depth, 1)))
                            models = [table.RangeOracle(words, memory, args, phase, 1, self.connected, ENTRY).run()
                                      for words in (self.retail, self.raw, self.guarded)]
                            reference = models[0]
                            resolved = (0xAB1950 if root == 0 else root) + max(depth - 1, 0) * 0x40
                            range_call = next(c for c in reference.calls if c[0] == table.ENTRY)
                            self.assertEqual(range_call, (table.ENTRY, resolved, buffer, 1, count))
                            self.assertEqual(reference.r[2], ((buffer + 8) & ~15) + ((resolved + 8) & 15))
                            for i, model in enumerate(models):
                                coverage[i].update(model.visits)
                                self.assertEqual(model.memory, reference.memory)
                                self.assertEqual(model.calls, reference.calls)
                                self.assertEqual(model.reads, reference.reads)
                                self.assertEqual(model.r[2], reference.r[2])
                                self.assert_windows_equal(model, reference)
                            self.assertEqual(models[2].events, reference.events)
                            cases += 1
        self.assertEqual(cases, 200)
        wrapper = set(range(ENTRY, ENTRY + 276, 4))
        range_body = set(range(table.ENTRY, table.ENTRY + 284, 4))
        for visits in coverage:
            self.assertTrue(wrapper | range_body <= visits)
        print('variadic table range:', cases, 'three-way actual lookup/cache/range cases; caller-owned stack buffers included')

    def test_native_actual_resource_helpers_connected(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        layout = re.search(r'typedef struct AssetTableCache57FA0 \{.*?\} AssetTableCache57FA0;', source, re.S).group(0)
        cache = re.search(r'void func_1502AB04\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        actual_lookup = re.search(r's32 func_1502AC88\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        actual_range = re.search(r'u32 \*func_1502AF04\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        original = self.fixture
        self.fixture = self.sdk + '\n' + self.types + layout + r'''
u8 D_AB1950[16] __attribute__((aligned(16)));
AssetTableCache57FA0 D_800C3D68[16]; u32 D_800C3D60;
static u8 storage[640] __attribute__((aligned(16)));
static int owner,rangeCalls,dmas,lookupDmas,copies,missing;
static u32 rangeBase;
void bcopy(void *source,void *destination,s32 length) {
    u8 *s=source,*d=destination; int i; copies++;
    for(i=0;i<length;i++) d[i]=s[i];
}
s32 func_10004514(u32 address,void *destination,u32 length,s32 mode) {
    u32 *out=destination,i; int absent=lookupDmas==missing; (void)address;(void)mode; dmas++;
    for(i=0;i<length/4;i++) out[i]=owner?0x80000000+i*19:
        (i%2?(absent?0xF0000000:0xF0000010):0x20+(i/2)*0x20);
    if(!owner) lookupDmas++;
    return -1;
}
''' + cache + '\n' + actual_lookup + '\n' + actual_range.replace('func_1502AF04', 'actual_range') + r'''
u32 *func_1502AF04(u32 base,void *buffer,u32 component,u32 count) {
    u32 *result; rangeCalls++;rangeBase=base;owner=1;
    result=actual_range(base,buffer,component,count);owner=0;return result;
}
''' + source_body() + '\n'
        try:
            self.run_host(r'''
int root,depth,n,i,cases=0; u32 base,*result,address,aligned;
for(root=0;root<2;root++) for(depth=0;depth<=5;depth++) for(n=0;n<=16;n++)
for(missing=-1;missing<(depth>=2?depth-1:0);missing++) {
    for(i=0;i<16;i++) { D_800C3D68[i].address=0x90000000+i*8;D_800C3D68[i].generation=0;
        D_800C3D68[i].offset=0;D_800C3D68[i].descriptor=0; }
    D_800C3D60=0xFFFFFFFF;owner=rangeCalls=dmas=lookupDmas=copies=0;
    base=root?0x12340:0;
    result=func_1502B110(base,n,storage+40,depth,1,1,1,1,1);
    if(lookupDmas!=(missing>=0?missing+1:(depth>=2?depth-1:0)) || copies!=lookupDmas) return 1;
    if(missing>=0) { if(result || rangeCalls || dmas!=lookupDmas) return 2; }
    else {
        base=(root?0x12340:(u32)D_AB1950)+(depth>=2?(u32)(depth-1)*0x40:0);
        address=base+8;aligned=((u32)(storage+40)+8)&~15u;
        if(rangeCalls!=1 || rangeBase!=base || dmas!=lookupDmas+1 || (u32)result!=aligned+(address&15)) return 3;
        for(i=0;i<n;i++) if(result[i*2]!=0x80000000+((address&15)/4+(u32)i*2)*19+base
           || result[i*2+1]!=0x80000000+((address&15)/4+(u32)i*2+1)*19) return 4;
    }
    cases++;
}
if(cases!=544) return 5;
''')
        finally:
            self.fixture = original

    def test_unlinked_inputs_and_preserved_sdk_relocations(self):
        functions, _, _ = load_elf_functions(str(self.output / 'selected.o'), 'mips-linux-gnu-objdump')
        for offset, (expected, _) in GUARDS.items():
            self.assertEqual(functions['func_1502B110'][offset // 4], expected)
        output = subprocess.run(['mips-linux-gnu-objdump', '-r', str(self.output / 'selected.o')],
                                check=True, capture_output=True, text=True).stdout
        actual = {int(o, 16): (kind, symbol) for o, kind, symbol in re.findall(
            r'(?m)^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\S+)\s*$', output)}
        self.assertEqual(actual, {0x40: ('R_MIPS_HI16', 'D_AB1950'), 0x44: ('R_MIPS_LO16', 'D_AB1950'),
                                 0x8C: ('R_MIPS_26', 'func_1502AC88'), 0xE0: ('R_MIPS_26', 'func_1502AF04')})
        self.assertFalse(set(GUARDS) & set(actual))

    def test_production_source_rows_and_complete_linked_identity(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        body = re.search(r'u32 \*func_1502B110\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body, source_body())
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            rows = [r for r in csv.DictReader(file) if r['function'] == 'func_1502B110']
        self.assertEqual(len(rows), 2)
        self.assertEqual({int(r['offset'], 0): (int(r['expected'], 0), int(r['replacement'], 0)) for r in rows}, GUARDS)
        for row in rows:
            self.assertEqual((row['filename'], row['expected_relocations'], row['replacement_relocations'],
                              row['insert_after'], row['omit']), ('game_57FA0', '-', '-', '', 'false'))
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                    'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502B110'], ENTRY)
        self.assertEqual(functions['func_1502B110'], self.retail)


if __name__ == '__main__':
    unittest.main()
