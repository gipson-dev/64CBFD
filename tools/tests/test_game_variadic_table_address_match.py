"""Variadic table-address recovery, independent loop stores and connected cache."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_variadic_table_address_candidates as screen
from tools.tests import test_game_table_range_loader as table
from tools.tests import test_game_cached_lookup_match as lookup
from tools.tests import test_game_cache_installer_match as installer
from tools.tests import test_game_variadic_table_range_match as wrapper
from tools.tests import test_game_random_curve_record as native
from tools.match_progress import load_elf_functions


ENTRY = 0x1502B020
GUARDS = {0x94: (0xAFA80038, 0xAFA5004C), 0x9C: (0xAFA5004C, 0xAFA80038)}


def source_body():
    return dict(screen.candidates())['layout-1-early']


def apply_linked_guards(words, omitted=None):
    result = words[:]
    for offset, (expected, replacement) in GUARDS.items():
        assert result[offset // 4] == expected
        if offset != omitted:
            result[offset // 4] = replacement
    return result


class AddressOracle(table.RangeOracle):
    def __init__(self, words, memory, arguments, phase=0, pattern=0, missing=-1, connected=None):
        super().__init__(words, memory, arguments, phase, pattern, connected, ENTRY)
        self.missing, self.lookups = missing, 0

    def record_call(self, target):
        if self.connected:
            super().record_call(target)
            if target == lookup.ENTRY:
                self.lookups += 1
        else:
            assert target == lookup.ENTRY
            self.calls.append((target, *self.r[4:7]))
            self.events.append(('CALL', *self.calls[-1]))

    def hook(self, target):
        if self.connected:
            if target == table.DMA:
                source, destination, length, mode = self.r[4:8]
                assert source & 15 == 0 and destination & 15 == 0
                assert length & 15 == 0 and length <= 272 and mode == 1
                for i in range(length // 4):
                    self.put(destination + i * 4,
                        (0xF0000000 if self.lookups - 1 == self.missing else 0xF0000010)
                        if i % 2 else 0x20 + (i // 2) * 0x20, 4)
                for register in (1, 2, 3, *range(4, 16), 24, 25):
                    self.r[register] = 0xA5000000 + register
            else:
                super().hook(target)
            return
        assert target == lookup.ENTRY
        i = self.lookups
        self.lookups += 1
        if self.missing != -2:
            self.put(self.r[6], 0xF0000000 if i == self.missing else 0xF0000010 + i, 4)
        result = 0xFFFFFFF0 if self.pattern == 1 and i == 0 else 8 * (i + 1)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result & 0xFFFFFFFF


CALLER = 0x1001263C
COMMANDS = (0x151F2D6C, 0x151F2DFC, 0x151F2E4C, 0x151F2960)


class InitCallerOracle(AddressOracle):
    """Actual Init caller/lookup/cache code; sound commands remain opaque hooks."""

    def __init__(self, caller, wrapper_words, memory, arguments, phase, connected, missing):
        code = connected.copy()
        code.update(zip(range(ENTRY, ENTRY + 240, 4), wrapper_words))
        super().__init__(caller, memory, arguments, phase, connected=code, missing=missing)
        self.entry = CALLER
        self.code = dict(zip(range(CALLER, CALLER + len(caller) * 4, 4), caller))
        self.code.update(code)

    def record_call(self, target):
        if target == ENTRY or target in COMMANDS:
            self.calls.append((target, *(self.r[4:8] if target == ENTRY else self.r[4:6])))
            self.events.append(('CALL', *self.calls[-1]))
        else:
            super().record_call(target)

    def hook(self, target):
        if target in COMMANDS:
            for register in (1, 2, 3, *range(4, 16), 24, 25):
                self.r[register] = 0xA5000000 + register
        else:
            super().hook(target)


class GameVariadicTableAddressMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(n) is None for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-variadic-table-address-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, cls.output, 'selected', source_body())
        cls.guarded = apply_linked_guards(cls.raw)
        cls.retail = list(struct.unpack_from('>60I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0x584D0))
        _, raw_lookup = lookup.screen.compile_candidate(cls.root, cls.output, 'lookup', lookup.source_body())
        _, raw_cache = installer.screen.compile_candidate(cls.root, cls.output, 'cache', installer.source_body())
        cls.connected = {}
        for address, words in ((lookup.ENTRY, lookup.apply_linked_guards(raw_lookup)),
                (lookup.INSTALL, installer.apply_linked_guards(raw_cache))):
            cls.connected.update(zip(range(address, address + len(words) * 4, 4), words))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = 'typedef unsigned char u8; typedef int s32; typedef unsigned int u32;\n#define NULL ((void *)0)\n'
        cls.sdk = (cls.root / 'conker/include/libc/stdarg.h').read_text()
        cls.fixture = cls.sdk + '\n' + cls.types + r'''
u8 D_AB1950[16] __attribute__((aligned(16)));
static s32 items[16]; static u32 advances[16],metadata[16];
static u32 expectedBase,expectedDepth,*lastDescriptor,output[16];
static int lookups,consumed,error,expectedLookups,missing;
static void reset(u32 depth,int absent,int phase) {
    int i; missing=absent; expectedDepth=depth; expectedBase=(u32)D_AB1950;
    lookups=consumed=error=0;lastDescriptor=NULL;
    expectedLookups=absent>=0?absent+1:(int)depth;
    for(i=0;i<16;i++) {
        items[i]=phase==2?1:i+1; advances[i]=(u32)(8*(i+1));
        metadata[i]=0xF0000010u+(u32)i;output[i]=0xA5A5A5A5;
    }
    if(phase==1) { items[0]=-1;items[1]=(s32)0x80000000;items[2]=0x7FFFFFFF;advances[0]=0xFFFFFFF0; }
    if(absent>=0) metadata[absent]=0xF0000000;
}
s32 func_1502AC88(u32 base,s32 component,u32 *descriptor) {
    int i=lookups++;
    if(i>=expectedLookups || base!=expectedBase || component!=items[i]
       || (lastDescriptor && descriptor!=lastDescriptor)
       || *descriptor!=(i==0 || missing==-2?1:metadata[i-1]&0x0FFFFFFF)) error=1;
    lastDescriptor=descriptor;
    if(missing!=-2) *descriptor=metadata[i];
    expectedBase+=advances[i];return (s32)advances[i];
}
#undef va_arg
#define va_arg(path,type) (consumed++,__builtin_va_arg(path,type))
''' + source_body() + '\n'

    def assert_windows_equal(self, actual, reference, wrapper_frame=0):
        a, b = wrapper.read_windows(actual), wrapper.read_windows(reference)
        self.assertEqual(len(a), len(b))
        for (stores, event), (expected, following) in zip(a, b):
            self.assertEqual(event, following)
            if stores != expected:
                self.assertEqual(sorted(stores), sorted(expected))
                self.assertEqual(len(stores), 2)
                sp = actual.before[29] - wrapper_frame
                self.assertEqual({(address, size) for address, size, _ in stores}, {(sp - 16, 4), (sp + 4, 4)})

    def test_complete_raw_guarded_slots_and_compiler_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (60, 0x48, 2))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.guarded, self.retail)
        self.assertEqual(hashlib.sha256(struct.pack('>60I', *self.raw)).hexdigest(),
                         '541e2e7d512cda3d590e0773c06ab103954e1a87fbe38ab1e63a2ac1f835c8c3')
        self.assertEqual(hashlib.sha256(struct.pack('>60I', *self.retail)).hexdigest(),
                         'b13bf05cd069a03869466184bab0f54b0fb2557bb744f1d334034496776b7844')
        self.assertEqual({i * 4 for i, (a, b) in enumerate(zip(self.raw, self.retail)) if a != b}, set(GUARDS))
        for name, expected in (('placeholder', (3, 0, 60)), ('baseline', (61, 0x48, 17)),
                ('layout-1', (61, 0x48, 11)), ('return-if', (60, 0x48, 8)),
                ('selected-do-while', (60, 0x48, 2))):
            record, _ = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')

    def test_native_depth_descriptor_consumption_and_optional_output(self):
        self.run_host(r'''
int depth,absent,phase,slot,i,cases=0;u32 result,expectedSize,*out;
for(phase=0;phase<3;phase++) for(depth=0;depth<=16;depth++)
for(absent=-2;absent<depth;absent++) for(slot=-1;slot<3;slot++) {
    reset(depth,absent,phase);out=slot<0?NULL:output+slot;
    result=func_1502B020(out,depth,items[0],items[1],items[2],items[3],items[4],items[5],
        items[6],items[7],items[8],items[9],items[10],items[11],items[12],items[13],items[14],items[15]);
    expectedSize=absent>=0?0:(depth && absent!=-2?metadata[depth-1]&0x0FFFFFFF:1);
    if(error || consumed!=depth || lookups!=expectedLookups || result!=(expectedSize?expectedBase:0)) return 1;
    for(i=0;i<16;i++) if(output[i]!=(i==slot?expectedSize:0xA5A5A5A5)) return 2;
    cases++;
}
if(cases!=2040) return 3;
reset(0,-1,0);
if(func_1502B020(NULL,0)!=(u32)D_AB1950 || consumed || lookups) return 4;
''')

    def test_boundary_memory_events_outputs_and_all_words(self):
        coverage, cases = [set(), set(), set()], 0
        for pattern in range(3):
            items = wrapper.components(pattern)
            for depth in range(17):
                for missing in range(-2, depth):
                    for phase in (0, 8):
                        for out in (0, table.BUFFER + 8, table.STACK + phase + 0x80, table.STACK + phase + 8):
                            args = (out, depth, *items)
                            models = [AddressOracle(words, table.memory_case(pattern), args, phase, pattern, missing).run()
                                      for words in (self.retail, self.raw, self.guarded)]
                            reference = models[0]
                            calls = missing + 1 if missing >= 0 else depth
                            size = 0 if missing >= 0 else (1 if depth == 0 or missing == -2 else 0x10 + depth - 1)
                            base = (0xAB1950 + sum(0xFFFFFFF0 if pattern == 1 and i == 0 else 8 * (i + 1)
                                    for i in range(calls))) & 0xFFFFFFFF
                            self.assertEqual(reference.lookups, calls)
                            self.assertEqual(reference.r[2], base if size else 0)
                            self.assertEqual([a for a, n, _ in reference.reads if n == 4
                                and table.STACK + phase + 8 <= a < table.STACK + phase + 0x48],
                                [table.STACK + phase + 8 + i * 4 for i in range(depth)])
                            if out:
                                self.assertEqual(int.from_bytes(bytes(reference.memory[out + i] for i in range(4)), 'big'), size)
                                store = ('W', out, 4, size)
                                self.assertIn(store, reference.events)
                                last_store = len(reference.events) - 1 - reference.events[::-1].index(store)
                                self.assertEqual(reference.events[last_store + 1], ('R', table.STACK + phase - 16, 4, size))
                            for i, model in enumerate(models):
                                coverage[i].update(model.visits)
                                self.assertEqual(model.memory, reference.memory)
                                self.assertEqual(model.calls, reference.calls)
                                self.assertEqual(model.reads, reference.reads)
                                self.assertEqual(model.r[2], reference.r[2])
                                self.assert_windows_equal(model, reference)
                            self.assertEqual(models[2].events, reference.events)
                            cases += 1
        self.assertEqual(cases, 4080)
        self.assertEqual(coverage, [set(range(ENTRY, ENTRY + 240, 4))] * 3)
        print('variadic table address:', cases, 'three-way boundary cases; all 60 words and output-before-reread')

    def test_each_omitted_guard_is_rejected(self):
        args = (table.BUFFER + 8, 3, 1, 2, 3)
        reference = AddressOracle(self.retail, table.memory_case(), args, missing=0).run()
        for offset in GUARDS:
            try:
                partial = AddressOracle(apply_linked_guards(self.raw, offset), table.memory_case(), args, missing=0).run()
                rejected = partial.memory != reference.memory or partial.events != reference.events
            except (AssertionError, KeyError):
                rejected = True
            self.assertTrue(rejected, hex(offset))

    def test_actual_lookup_cache_connected_output_aliases(self):
        cases, coverage = 0, [set(), set(), set()]
        for phase in (0, 8):
            for depth in (0, 1, 2, 3, 5, 16):
                for out in (0, table.BUFFER + 8, table.STACK + phase + 0x80,
                        table.STACK + phase + 8, lookup.CLOCK, lookup.CACHE, lookup.CACHE + 248):
                    args = (out, depth, *([1] * max(depth, 2)))
                    models = [AddressOracle(words, table.memory_case(1), args, phase, 1, connected=self.connected).run()
                              for words in (self.retail, self.raw, self.guarded)]
                    reference = models[0]
                    self.assertEqual(reference.lookups, depth)
                    self.assertEqual(reference.r[2], 0xAB1950 + depth * 0x40)
                    if out:
                        self.assertEqual(int.from_bytes(bytes(reference.memory[out + i] for i in range(4)), 'big'), 16 if depth else 1)
                    for i, model in enumerate(models):
                        coverage[i].update(model.visits)
                        self.assertEqual(model.memory, reference.memory)
                        self.assertEqual(model.calls, reference.calls)
                        self.assertEqual(model.reads, reference.reads)
                        self.assertEqual(model.r[2], reference.r[2])
                        self.assert_windows_equal(model, reference)
                    self.assertEqual(models[2].events, reference.events)
                    cases += 1
        self.assertEqual(cases, 84)
        self.assertTrue(all(set(range(ENTRY, ENTRY + 240, 4)) - {ENTRY + 0xD0, ENTRY + 0xD4} <= v for v in coverage))
        print('variadic table address:', cases, 'three-way actual lookup/cache cases; cache/clock and caller-home outputs')

    def test_connected_hit_miss_descriptor_gates_and_output_aliases(self):
        cases, coverage = 0, [set(), set(), set()]
        for phase in (0, 8):
            for depth in range(1, 6):
                for missing in range(-1, depth):
                    for hit in (False, True):
                        for out in (0, table.BUFFER + 8, lookup.CLOCK, lookup.CACHE + 252,
                                    table.STACK + phase + 0x80):
                            memory = table.memory_case(1)
                            if hit:
                                for offset, value in ((0, 0x80AB1958), (4, 0xFFFFFFFF),
                                        (8, 0x40), (12, 0xF0000000 if missing == 0 else 0xF0000010)):
                                    lookup.put_word(memory, lookup.CACHE + 240 + offset, value)
                            args = (out, depth, *([1] * max(depth, 2)))
                            models = [AddressOracle(words, memory, args, phase, 1, missing, self.connected).run()
                                      for words in (self.retail, self.raw, self.guarded)]
                            reference = models[0]
                            calls = depth if missing < 0 else missing + 1
                            self.assertEqual(reference.lookups, calls)
                            self.assertEqual(sum(c[0] == table.DMA for c in reference.calls), calls - int(hit))
                            self.assertEqual(reference.r[2], 0xAB1950 + depth * 0x40 if missing < 0 else 0)
                            if out:
                                self.assertEqual(int.from_bytes(bytes(reference.memory[out + i] for i in range(4)), 'big'),
                                                 16 if missing < 0 else 0)
                            for i, model in enumerate(models):
                                coverage[i].update(model.visits)
                                self.assertEqual(model.memory, reference.memory)
                                self.assertEqual(model.calls, reference.calls)
                                self.assertEqual(model.reads, reference.reads)
                                self.assertEqual(model.r[2], reference.r[2])
                                self.assert_windows_equal(model, reference)
                            self.assertEqual(models[2].events, reference.events)
                            cases += 1
        self.assertEqual(cases, 400)
        self.assertTrue(all(set(range(ENTRY, ENTRY + 240, 4)) - {ENTRY + 0xA4, ENTRY + 0xA8} <= v for v in coverage))
        print('variadic table address:', cases, 'three-way connected hit/miss cases; every missing-descriptor position')

    def test_retail_init_sound_caller_with_actual_source_callees(self):
        caller = list(struct.unpack_from('>43I', (self.root / 'conker/conker.us.bin').read_bytes(), 0x1263C))
        self.assertEqual(caller[:2], [0x27BDFFE0, 0xAFBF0014])
        cases, visits = 0, set()
        for phase in (0, 8):
            for component in (0, 1, 0xD2, 0xFFFFFFFF):
                for missing in (-1, 0, 1):
                    memory = table.memory_case(1)
                    memory.update({0x800427F4 + i: 0xA5 for i in range(2)})
                    models = [InitCallerOracle(caller, words, memory, (component, 0x1234, 0x5678),
                              phase, self.connected, missing).run() for words in (self.retail, self.raw, self.guarded)]
                    reference = models[0]
                    calls = [c for c in reference.calls if c[0] in COMMANDS]
                    self.assertEqual(reference.lookups, 2 if missing < 0 else missing + 1)
                    self.assertEqual(int.from_bytes(bytes(reference.memory[0x800427F4 + i] for i in range(2)), 'big'), component & 0xFFFF)
                    size = int.from_bytes(bytes(reference.memory[table.STACK + phase - 8 + i] for i in range(4)), 'big')
                    self.assertEqual(size, 16 if missing < 0 else 0)
                    self.assertEqual(calls, [] if missing >= 0 else [
                        (COMMANDS[0], 0x1234, 0), (COMMANDS[1], 0x5678, 1),
                        (COMMANDS[2], 0 if component == 0xD2 else 10, 0 if component == 0xD2 else 11000),
                        (COMMANDS[3], 0xAB1950 + 0x20 + (0x20 if component % 2 == 0 else 0x40), 16)])
                    for model in models:
                        visits.update(model.visits)
                        self.assertEqual(model.memory, reference.memory)
                        self.assertEqual(model.calls, reference.calls)
                        self.assertEqual(model.reads, reference.reads)
                        self.assertEqual(model.r[2], reference.r[2])
                        self.assert_windows_equal(model, reference, 0x20)
                    self.assertEqual(models[2].events, reference.events)
                    cases += 1
        self.assertEqual(cases, 24)
        # This likely delay slot needs nonzero address with zero size, which the resolver never returns.
        self.assertEqual(set(range(CALLER, CALLER + 172, 4)) - visits, {CALLER + 0x4C})
        print('variadic table address:', cases, 'three-way actual Init sound-caller cases; 42/43 caller words reachable')

    def test_native_actual_cache_lookup_connected_missing_and_hits(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        layout = re.search(r'typedef struct AssetTableCache57FA0 \{.*?\} AssetTableCache57FA0;', source, re.S).group(0)
        cache = re.search(r'void func_1502AB04\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        actual_lookup = re.search(r's32 func_1502AC88\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        original = self.fixture
        self.fixture = self.sdk + '\n' + self.types + layout + r'''
u8 D_AB1950[16] __attribute__((aligned(16)));
AssetTableCache57FA0 D_800C3D68[16];u32 D_800C3D60;
static int dmas,copies,missing;
void bcopy(void *source,void *destination,s32 length) {
    u8 *s=source,*d=destination;int i;copies++;for(i=0;i<length;i++) d[i]=s[i];
}
s32 func_10004514(u32 address,void *destination,u32 length,s32 mode) {
    u32 *out=destination,i;int absent=dmas++==missing;(void)address;(void)mode;
    for(i=0;i<length/4;i++) out[i]=i%2?(absent?0xF0000000:0xF0000010):0x20+(i/2)*0x20;
    return -1;
}
''' + cache + '\n' + actual_lookup + '\n' + source_body() + '\n'
        try:
            self.run_host(r'''
int depth,slot,i,cases=0;u32 output,result,*out,expected;
for(depth=0;depth<=5;depth++) for(missing=-1;missing<depth;missing++) for(slot=0;slot<4;slot++) {
    for(i=0;i<16;i++) { D_800C3D68[i].address=0x90000000+i*8;D_800C3D68[i].generation=0;
        D_800C3D68[i].offset=0;D_800C3D68[i].descriptor=0; }
    D_800C3D60=0xFFFFFFFF;dmas=copies=0;output=0xA5A5A5A5;
    out=slot==0?NULL:slot==1?&output:slot==2?&D_800C3D60:&D_800C3D68[15].offset;
    result=func_1502B020(out,depth,1,1,1,1,1);
    expected=missing>=0?0:(depth?16:1);
    if(result!=(expected?(u32)D_AB1950+(u32)depth*0x40:0)
       || dmas!=(missing>=0?missing+1:depth) || copies!=dmas || (out && *out!=expected)) return 1;
    if(slot<2) {
        result=func_1502B020(out,depth,1,1,1,1,1);
        if(result!=(expected?(u32)D_AB1950+(u32)depth*0x40:0)
           || dmas!=(missing>=0?missing+1:depth) || copies!=dmas || (out && *out!=expected)) return 2;
    }
    cases++;
}
if(cases!=84) return 3;
''')
        finally:
            self.fixture = original

    def test_unlinked_sdk_relocations_and_final_output_read(self):
        functions, _, _ = load_elf_functions(str(self.output / 'selected.o'), 'mips-linux-gnu-objdump')
        for offset, (expected, _) in GUARDS.items():
            self.assertEqual(functions['func_1502B020'][offset // 4], expected)
        output = subprocess.run(['mips-linux-gnu-objdump', '-r', str(self.output / 'selected.o')],
                                check=True, capture_output=True, text=True).stdout
        actual = {int(o, 16): (kind, symbol) for o, kind, symbol in re.findall(
            r'(?m)^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\S+)\s*$', output)}
        self.assertEqual(actual, {0x30: ('R_MIPS_HI16', 'D_AB1950'), 0x38: ('R_MIPS_LO16', 'D_AB1950'),
                                 0x78: ('R_MIPS_26', 'func_1502AC88')})
        self.assertFalse(set(GUARDS) & set(actual))
        self.assertEqual(self.raw[0xB8 // 4:0xC0 // 4], [0xAD2B0000, 0x8FAC0038])

    def test_init_caller_declarations_and_full_linked_slots_remain_retail(self):
        for filename in ('init_8180.c', 'init_12560.c'):
            source = (self.root / 'conker/src' / filename).read_text()
            self.assertIn('u32 func_1502B020(u32 *size, u32 depth, ...);', source)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        for name, words in (('func_10008180', 214), ('func_1001263C', 43)):
            retail = list(struct.unpack_from('>' + str(words) + 'I', rom, addresses[name] - 0x10000000))
            self.assertEqual(functions[name], retail)
        self.assertIn('    u32 sp18;', (self.root / 'conker/src/init_12560.c').read_text())

    def test_production_source_rows_and_complete_linked_identity(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        body = re.search(r'u32 func_1502B020\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body, source_body())
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            rows = [r for r in csv.DictReader(file) if r['function'] == 'func_1502B020']
        self.assertEqual(len(rows), 2)
        self.assertEqual({int(r['offset'], 0): (int(r['expected'], 0), int(r['replacement'], 0)) for r in rows}, GUARDS)
        for row in rows:
            self.assertEqual((row['filename'], row['expected_relocations'], row['replacement_relocations'],
                              row['insert_after'], row['omit']), ('game_57FA0', '-', '-', '', 'false'))
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502B020'], ENTRY)
        self.assertEqual(functions['func_1502B020'], self.retail)
        print('variadic table address hashes:', hashlib.sha256(struct.pack('>60I', *self.raw)).hexdigest(),
              hashlib.sha256(struct.pack('>60I', *self.retail)).hexdigest())


if __name__ == '__main__':
    unittest.main()
