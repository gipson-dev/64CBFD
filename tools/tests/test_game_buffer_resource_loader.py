"""Direct caller-buffer loader recovery; SDK/decoder/error hooks are bounded models."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_buffer_resource_loader_candidates as screen
from tools.tests import test_game_table_range_loader as table
from tools.tests import test_game_cached_lookup_match as lookup
from tools.tests import test_game_cache_installer_match as installer
from tools.tests import test_game_random_curve_record as native
from tools.match_progress import load_elf_functions


ENTRY, ALLOC, DECODE, FREE, ERROR = 0x1502B224, 0x10003C40, 0x10006240, 0x10004074, 0x150AD770
TEMP, SCRATCH, ERROR_WORD, WRAPPER = 0x30000, 0x8003809C, 0x8003C8E0, 0x1502B8E0
LENGTHS = (0, 1, 2, 3, 15, 16, 17, 0x0FFFFFFE, 0x0FFFFFFF)
CAPS = (0, 1, 2, 15, 16, 17, 31, 0xFFFFFFFF)


def source_body():
    return dict(screen.candidates())['layout-1']


def amount_for(descriptor, cap):
    amount = descriptor & 0x0FFFFFFF
    amount += amount % 2
    return min(amount, cap) if cap else amount


def memory_case():
    memory = table.memory_case(1)
    memory.update({TEMP + i: 0xA5 for i in range(256)})
    for address, value in ((TEMP, 0x80000020), (SCRATCH, 0x1234), (ERROR_WORD, 0xA5A5A5A5)):
        for i, byte in enumerate(struct.pack('>I', value)):
            memory[address + i] = byte
    return memory


class BufferOracle(table.RangeOracle):
    """Real instructions; allocation/decoder/error control is modeled, not reimplemented."""

    def __init__(self, words, memory, arguments, phase=0, case=None, connected=None, entry=ENTRY):
        super().__init__(words, memory, arguments, phase, 1, connected, entry)
        self.case = case or {}
        self.lookups = 0
        self.owner = ENTRY

    def record_call(self, target):
        counts = {ALLOC: 4, table.DMA: 4, DECODE: 3, FREE: 1, ERROR: 0,
                  lookup.ENTRY: 3, lookup.INSTALL: 4, lookup.COPY: 3, ENTRY: 4}
        assert target in counts, hex(target)
        call = (target, *self.r[4:4 + counts[target]])
        self.calls.append(call)
        self.events.append(('CALL', *call))
        if target in (lookup.ENTRY, ENTRY):
            self.owner = target
        if target == lookup.ENTRY:
            self.lookups += 1

    def hook(self, target):
        result = 0xA5000002
        if target == ALLOC:
            assert self.r[5:8] == [1, 2, 2]
            result = 0 if self.case.get('failure') else TEMP
            if not self.case.get('failure'):
                self.put(TEMP, self.case.get('header', 0x80000020), 4)
            if self.case.get('mutation'):
                self.put(SCRATCH, 0x4567, 4)
        elif target == table.DMA:
            address, destination, length, mode = self.r[4:8]
            assert mode == 1 and length % 16 == 0
            if self.owner == lookup.ENTRY:
                assert destination & 15 == 0 and length <= 32
                descriptor = self.case.get('lookupDescriptor', 0x80000010)
                if self.lookups - 1 == self.case.get('missing', -1):
                    descriptor = 0xF0000000
                for i in range(length // 4):
                    self.put(destination + i * 4, descriptor if i % 2 else 0x20 + (i // 2) * 0x20, 4)
            else:
                # Large lengths qualify call arguments only; they do not simulate large transfers.
                if length <= 64:
                    for i in range(length // 4):
                        self.put(destination + i * 4, 0xCA000000 + i, 4)
                    if destination == TEMP and length:
                        self.put(TEMP, self.case.get('header', 0x80000020), 4)
                if self.case.get('mutation'):
                    self.put(SCRATCH, 0x5678, 4)
            result = 0xFFFFFFFF
        elif target == DECODE:
            assert self.r[4] == TEMP
            assert self.r[6] == self.peek(SCRATCH, 4)
            self.put(TEMP, 0xDEADBEEF, 4)
            self.put(self.r[5], 0xAABBCCDD, 4)
            if self.case.get('mutation'):
                self.put(SCRATCH, 0x6789, 4)
            result = self.case.get('decoded', 32)
        elif target == ERROR:
            assert self.peek(ERROR_WORD, 4) == 0x0C000036
            if self.case.get('mutation'):
                self.put(ERROR_WORD, 0x0BADBEEF, 4)
                self.put(TEMP, 0xFFFFFFFF, 4)
        elif target == FREE:
            assert self.r[4] == TEMP
            if self.case.get('mutation'):
                self.put(SCRATCH, 0x789A, 4)
                self.put(TEMP + 4, 0xC0FFEE00, 4)
        else:
            assert target == lookup.COPY
            source, destination, length = self.r[4:7]
            assert destination == lookup.CACHE and length == 224
            for i in range(length):
                self.put(destination + i, self.get(source + i, 1), 1)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result & 0xFFFFFFFF


class TrapBoundary(Exception):
    """Stop before entering the real syscall helper; do not emulate trap recovery."""


class StopOnTrapOracle(BufferOracle):
    def hook(self, target):
        if target == ERROR:
            assert self.peek(ERROR_WORD, 4) == 0x0C000036
            raise TrapBoundary()
        super().hook(target)


class GameBufferResourceLoaderTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(n) is None for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-buffer-resource-loader-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', source_body())
        cls.retail = list(struct.unpack_from('>75I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0x586D4))
        cls.wrapper = list(struct.unpack_from('>53I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0x58D90))
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
        cls.fixture = cls.types + r'''
u32 D_8003809C; s32 D_8003C8E0;
static u32 temporary[64] __attribute__((aligned(16))),destination[64] __attribute__((aligned(16)));
static u32 descriptor,cap,expectedAmount,header,decodedResult,*buffer;
static int allocations,dmas,decodes,errors,frees,failure,error,traceLength,mutation;
static char trace[8];
static void push(char c) { if(traceLength<8) trace[traceLength++]=c;else error=1; }
static int trace_is(const char *s) { int i=0;while(s[i]) {if(i>=traceLength || trace[i]!=s[i])return 0;i++;}return i==traceLength; }
static void reset(u32 desc,u32 limit,int phase) {
    int i;descriptor=desc;cap=limit;expectedAmount=desc&0x0FFFFFFF;
    if(expectedAmount%2) expectedAmount++;
    if(limit && limit<expectedAmount) expectedAmount=limit;
    allocations=dmas=decodes=errors=frees=error=traceLength=0;
    failure=phase==1;mutation=1;header=0x80000020;decodedResult=phase==2?0:phase==3?0xFFFFFFFF:32;
    D_8003809C=0x1234;D_8003C8E0=(s32)0xA5A5A5A5;buffer=destination;
    for(i=0;i<64;i++) temporary[i]=destination[i]=0xA5A5A5A5;
    temporary[0]=header;
}
void *allocate_memory(s32 amount,s32 a,s32 b,s32 c) {
    push('A');allocations++;
    if((u32)amount!=expectedAmount || a!=1 || b!=2 || c!=2 || allocations!=1 || dmas || decodes || frees) error=2;
    if(mutation) D_8003809C=0x4567;
    return failure?NULL:temporary;
}
s32 func_10004514(u32 address,void *out,u32 length,s32 mode) {
    u32 *words=out,i;int compressed=(descriptor&0x70000000)==0x10000000;
    push('D');dmas++;
    if(address!=0x12340 || length!=((expectedAmount+15)&~15u) || mode!=1 || dmas!=1
       || out!=(compressed?(void *)temporary:(void *)buffer) || decodes || frees) error=3;
    if(length<=64) for(i=0;i<length/4;i++) words[i]=0xCA000000+i;
    if(compressed && length) temporary[0]=header;
    if(mutation) D_8003809C=0x5678;
    return -1;
}
s32 func_10006240(void *source,void *out,u32 scratch) {
    push('Z');decodes++;
    if(source!=temporary || out!=buffer || scratch!=(mutation?0x5678:0x1234) || allocations!=1
       || dmas!=1 || decodes!=1 || frees || temporary[0]!=header) error=4;
    temporary[0]=0xDEADBEEF;*(u32 *)out=0xAABBCCDD;
    if(mutation) D_8003809C=0x6789;
    return (s32)decodedResult;
}
void func_150AD770(void) {
    push('E');errors++;
    if((u32)D_8003C8E0!=0x0C000036 || decodes!=1 || frees || errors!=1) error=5;
    if(mutation) { D_8003C8E0=(s32)0x0BADBEEF;temporary[0]=0xFFFFFFFF; }
}
void func_10004074(void *source) {
    push('F');frees++;
    if(source!=temporary || frees!=1 || decodes!=1 || errors!=(decodedResult!=(header&0x7FFFFFFF))) error=6;
    if(mutation) { D_8003809C=0x789A;temporary[1]=0xC0FFEE00; }
}
''' + source_body() + '\n'

    def assert_models_equal(self, actual, retail):
        self.assertEqual(actual.memory, retail.memory)
        self.assertEqual(actual.calls, retail.calls)
        self.assertEqual(actual.events, retail.events)
        self.assertEqual(actual.reads, retail.reads)
        self.assertEqual(actual.stores, retail.stores)
        self.assertEqual(actual.r[2], retail.r[2])

    def test_direct_complete_body_frame_and_compiler_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (75, 0x30, 0))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(hashlib.sha256(struct.pack('>75I', *self.words)).hexdigest(),
                         'a19404b10321ccddb4e281f6712c201be4aa66052e2021d3e48082b8740257d1')
        for name, expected in (('placeholder', (3, 0, 75)), ('baseline', (75, 0x28, 10)),
                ('layout-2', (75, 0x28, 8)), ('layout-4', (75, 0x30, 0)), ('raw-first', (75, 0x28, 52))):
            record, words = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')
            self.assertEqual(words == self.words, name == 'layout-4')

    def test_native_all_flags_caps_and_decoder_results(self):
        self.run_host(r'''
static u32 lengths[]={0,1,2,3,15,16,17,31,0x0FFFFFFE,0x0FFFFFFF};
static u32 caps[]={0,1,2,15,16,17,31,0xFFFFFFFF};
int flag,n,c,phase,compressed,cases=0,i;u32 result,length;
for(flag=0;flag<16;flag++) for(n=0;n<10;n++) for(c=0;c<8;c++) for(phase=0;phase<4;phase++) {
    reset(((u32)flag<<28)|lengths[n],caps[c],phase);compressed=(flag&7)==1;
    result=func_1502B224(0x12340,buffer,descriptor,cap);
    if(error || result!=(compressed?(failure?0:decodedResult):expectedAmount)) return 1;
    if(allocations!=compressed || dmas!=(compressed && failure?0:1) || decodes!=(compressed && !failure)
       || frees!=decodes || errors!=(decodes && decodedResult!=32)) return 2;
    if(!trace_is(compressed?(failure?"A":decodedResult==32?"ADZF":"ADZEF"):"D")) return 3;
    if(!compressed) {
        length=(expectedAmount+15)&~15u;
        for(i=0;i<64;i++) if(destination[i]!=(length<=64 && (u32)i<length/4?0xCA000000+(u32)i:0xA5A5A5A5)) return 4;
    }
    cases++;
}
if(cases!=5120) return 5;
''')

    def test_native_header_limits_captured_size_and_cleanup_callbacks(self):
        self.run_host(r'''
static u32 headers[]={0,1,32,0x80000020,0x7FFFFFFF,0xFFFFFFFF,0x80000000,1000000};
static u32 results[]={0,1,32,0xFFFFFFFF,0x80000000,0x7FFFFFFF,1000000};
int h,r,alias,cases=0;u32 result;
for(h=0;h<8;h++) for(r=0;r<7;r++) for(alias=0;alias<2;alias++) {
    reset(0x90000011,15,0);header=headers[h];temporary[0]=header;decodedResult=results[r];
    if(alias) buffer=temporary;
    result=func_1502B224(0x12340,buffer,descriptor,cap);
    if(error || result!=decodedResult || errors!=(decodedResult!=(header&0x7FFFFFFF))
       || allocations!=1 || dmas!=1 || decodes!=1 || frees!=1
       || !trace_is(errors?"ADZEF":"ADZF") || D_8003809C!=0x789A) return 1;
    cases++;
}
if(cases!=112) return 2;
''')

    def test_native_failed_allocation_never_reads_null_destination(self):
        self.run_host(r'''
reset(0x10000011,1,1);buffer=NULL;
if(func_1502B224(0x12340,NULL,descriptor,cap) || error || allocations!=1 || dmas || decodes || errors || frees
   || !trace_is("A") || destination[0]!=0xA5A5A5A5) return 1;
''')

    def test_boundary_complete_memory_ordered_events_and_all_words(self):
        coverage, cases = [set(), set()], 0
        for flag in range(16):
            for length in LENGTHS:
                descriptor = flag << 28 | length
                for cap in CAPS:
                    for phase in (0, 8):
                        for scenario in range(3):
                            case = dict(failure=scenario == 1, header=0x80000020,
                                        decoded=32 if scenario == 0 else 0xFFFFFFFF, mutation=True)
                            args = (0x12340, table.BUFFER + 8, descriptor, cap)
                            models = [BufferOracle(words, memory_case(), args, phase, case).run()
                                      for words in (self.retail, self.words)]
                            retail = models[0]
                            amount = amount_for(descriptor, cap)
                            compressed = flag & 7 == 1
                            expected = 0 if compressed and case['failure'] else case['decoded'] if compressed else amount
                            self.assertEqual(retail.r[2], expected)
                            expected_calls = ([(ALLOC, amount, 1, 2, 2)] if compressed else [])
                            if not compressed or not case['failure']:
                                expected_calls += [(table.DMA, 0x12340, TEMP if compressed else table.BUFFER + 8,
                                                    (amount + 15) & ~15, 1)]
                                if compressed:
                                    expected_calls += [(DECODE, TEMP, table.BUFFER + 8, 0x5678)]
                                    if case['decoded'] != 32:
                                        expected_calls += [(ERROR,)]
                                    expected_calls += [(FREE, TEMP)]
                            self.assertEqual(retail.calls, expected_calls)
                            for i, model in enumerate(models):
                                coverage[i].update(model.visits)
                                self.assert_models_equal(model, retail)
                            cases += 1
        self.assertEqual(cases, 6912)
        self.assertEqual(coverage, [set(range(ENTRY, ENTRY + 300, 4))] * 2)
        print('buffer resource loader:', cases, 'two-way boundary cases; all 75 words')

    def test_decoder_destination_aliases_and_live_scratch(self):
        for phase in (0, 8):
            for buffer in (table.BUFFER + 8, TEMP, table.STACK + phase + 0x80, ERROR_WORD, SCRATCH):
                for header in (0, 0x80000020, 0xFFFFFFFF):
                    for decoded in (0, 32, 0xFFFFFFFF, 0x80000000):
                        args = (0x12344, buffer, 0x90000011, 15)
                        case = dict(header=header, decoded=decoded, mutation=True)
                        models = [BufferOracle(words, memory_case(), args, phase, case).run()
                                  for words in (self.retail, self.words)]
                        self.assert_models_equal(models[1], models[0])
                        self.assertEqual(models[0].r[2], decoded)
                        self.assertEqual(sum(c[0] == ERROR for c in models[0].calls), int(decoded != header & 0x7FFFFFFF))
                        self.assertIn((DECODE, TEMP, buffer, 0x5678), models[0].calls)

    def test_mismatch_stops_at_real_syscall_boundary_before_cleanup(self):
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        self.assertEqual(struct.unpack_from('>I', rom, 0xDAC20)[0], 0x0000000C)
        cases = 0
        for phase in (0, 8):
            for buffer in (table.BUFFER + 8, TEMP):
                for header in (0, 0x80000020, 0xFFFFFFFF):
                    for decoded in (0, 32, 0xFFFFFFFF, 0x80000000):
                        if decoded == header & 0x7FFFFFFF:
                            continue
                        args = (0x12340, buffer, 0x10000011, 15)
                        case = dict(header=header, decoded=decoded, mutation=True)
                        models = [StopOnTrapOracle(words, memory_case(), args, phase, case)
                                  for words in (self.retail, self.words)]
                        for model in models:
                            with self.assertRaises(TrapBoundary):
                                model.run()
                            self.assertEqual(model.calls[-1], (ERROR,))
                            self.assertFalse(any(c[0] == FREE for c in model.calls))
                            self.assertEqual(model.r[17], decoded)
                            self.assertEqual(model.r[31], ENTRY + 0xE8)
                            self.assertEqual(model.peek(ERROR_WORD, 4), 0x0C000036)
                        self.assert_models_equal(models[1], models[0])
                        cases += 1
        self.assertEqual(cases, 40)
        print('buffer resource loader:', cases, 'two-way mismatch prefixes stop at handwritten syscall boundary')

    def test_retail_variadic_caller_with_actual_lookup_cache_and_loader(self):
        cases, coverage = 0, [set(), set()]
        for phase in (0, 8):
            for depth in range(1, 6):
                for missing in range(-1, depth):
                    for descriptor in (0x80000010, 0x10000010, 0x90000011):
                        for cap in (0, 1, 15, 16, 17):
                            case = dict(lookupDescriptor=descriptor, missing=missing, decoded=32, mutation=True)
                            args = (table.BUFFER + 8, cap, depth, *([1] * depth))
                            models = []
                            for words in (self.retail, self.words):
                                connected = self.connected.copy()
                                connected.update(zip(range(ENTRY, ENTRY + 300, 4), words))
                                models.append(BufferOracle(self.wrapper, memory_case(), args, phase,
                                                          case, connected, WRAPPER).run())
                            self.assert_models_equal(models[1], models[0])
                            retail = models[0]
                            self.assertEqual(retail.lookups, depth if missing < 0 else missing + 1)
                            loader_calls = [c for c in retail.calls if c[0] == ENTRY]
                            self.assertEqual(loader_calls, [] if missing >= 0 else [
                                (ENTRY, 0xAB1950 + depth * 0x40, table.BUFFER + 8, descriptor, cap)])
                            expected = 0 if missing >= 0 else 32 if descriptor & 0x70000000 == 0x10000000 else amount_for(descriptor, cap)
                            self.assertEqual(retail.r[2], expected)
                            for i, model in enumerate(models):
                                coverage[i].update(model.visits)
                            cases += 1
        self.assertEqual(cases, 600)
        self.assertTrue(all(set(range(WRAPPER, WRAPPER + 212, 4)) <= visits for visits in coverage))
        print('buffer resource loader:', cases, 'connected retail SDK-varargs caller/actual cache/lookup cases')

    def test_zero_depth_retail_caller_preserves_incoming_descriptor_seed(self):
        for phase in (0, 8):
            for seed in (0, 1, 0x10000010, 0x90000011, 0xFFFFFFFF):
                memory = memory_case()
                lookup.put_word(memory, table.STACK + phase - 0x14, seed)
                args = (table.BUFFER + 8, 0, 0, 0xA5A5A5A5)
                models = []
                for words in (self.retail, self.words):
                    connected = self.connected.copy()
                    connected.update(zip(range(ENTRY, ENTRY + 300, 4), words))
                    models.append(BufferOracle(self.wrapper, memory, args, phase,
                                              dict(decoded=32), connected, WRAPPER).run())
                self.assert_models_equal(models[1], models[0])
                self.assertEqual(models[0].lookups, 0)
                self.assertIn((ENTRY, 0xAB1950, table.BUFFER + 8, seed, 0), models[0].calls)
                self.assertEqual(models[0].r[2], 32 if seed & 0x70000000 == 0x10000000 else amount_for(seed, 0))

    def test_unlinked_relocations_and_no_word_guards(self):
        output = subprocess.run(['mips-linux-gnu-objdump', '-r', str(self.output / 'selected.o')],
                                check=True, capture_output=True, text=True).stdout
        actual = {int(o, 16): (kind, symbol) for o, kind, symbol in re.findall(
            r'(?m)^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\S+)\s*$', output)}
        self.assertEqual(actual, {0x68: ('R_MIPS_26', 'allocate_memory'), 0x98: ('R_MIPS_26', 'func_10004514'),
            0xAC: ('R_MIPS_HI16', 'D_8003809C'), 0xB8: ('R_MIPS_LO16', 'D_8003809C'),
            0xC0: ('R_MIPS_26', 'func_10006240'), 0xDC: ('R_MIPS_HI16', 'D_8003C8E0'),
            0xE0: ('R_MIPS_26', 'func_150AD770'), 0xE4: ('R_MIPS_LO16', 'D_8003C8E0'),
            0xE8: ('R_MIPS_26', 'func_10004074'), 0x10C: ('R_MIPS_26', 'func_10004514')})
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            self.assertFalse(any(r['function'] == 'func_1502B224' for r in csv.DictReader(file)))

    def test_production_source_and_complete_linked_identity(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        self.assertEqual(re.search(r'u32 func_1502B224\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0), source_body())
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502B224'], ENTRY)
        self.assertEqual(functions['func_1502B224'], self.retail)
        print('buffer resource loader complete hash:', hashlib.sha256(struct.pack('>75I', *self.words)).hexdigest())


if __name__ == '__main__':
    unittest.main()
