"""Direct table-range recovery, actual C fixtures and bounded connected guest traces."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_table_range_candidates as screen
from tools.tests import test_game_random_curve_record as native
from tools.tests import test_game_cached_lookup_match as lookup
from tools.tests import test_game_cache_installer_match as installer
from tools.tests.test_game_viewport_renderer import RendererOracle
from tools.tests.test_game_queued_segment_writer import SegmentQueueOracle, STACK
from tools.tests.game_animation_timeline_oracle import TimelineOracle
from tools.match_progress import load_elf_functions


ENTRY, DMA, BUFFER, WRAPPER = 0x1502AF04, 0x10004514, 0x20000, 0x1502B110


def source_body():
    return dict(screen.candidates())['argument-address-no-early-assignment']


def word_value(index, pattern):
    return ((0xFFFFFFE0, 0x80000000, 0x12340000)[pattern] + index * 19) & 0xFFFFFFFF


def memory_case(pattern=0):
    memory = {STACK + i: 0xA5 for i in range(-0x500, 0xC0)}
    memory.update({BUFFER + i: 0xA5 for i in range(-32, 544)})
    memory.update({lookup.CACHE + i: 0xA5 for i in range(-16, 272)})
    for i in range(64):
        lookup.put_word(memory, lookup.CACHE + i * 4, 0x90000000 + i * 17)
    lookup.put_word(memory, lookup.CLOCK, (0, 0xFFFFFFFF, 0x12345678)[pattern])
    return memory


class RangeOracle(RendererOracle):
    """Real range/connected instructions; DMA and SDK bcopy are bounded models."""

    def __init__(self, words, memory, arguments, phase=0, pattern=0, connected=None, entry=ENTRY):
        SegmentQueueOracle.__init__(self, words, entry, memory, arguments[:4])
        assert phase in (0, 8)
        self.r[29] = self.before[29] = STACK + phase
        for i, argument in enumerate(arguments[4:]):
            lookup.put_word(self.memory, STACK + phase + 0x10 + i * 4, argument)
        self.connected = connected or {}
        self.code.update(self.connected)
        self.calls, self.events, self.pattern = [], [], pattern
        self.owner = ENTRY

    def get(self, address, size):
        value = super().get(address, size)
        self.events.append(('R', address, size, value))
        return value

    def put(self, address, value, size):
        if self.recording:
            self.events.append(('W', address, size, value & ((1 << (size * 8)) - 1)))
        SegmentQueueOracle.put(self, address, value, size)

    def record_call(self, target):
        assert target in (DMA, lookup.COPY, lookup.INSTALL, lookup.ENTRY, ENTRY)
        args = tuple(self.r[4:7 if target == lookup.COPY else 8])
        self.calls.append((target, *args))
        self.events.append(('CALL', target, args))
        if target in (lookup.ENTRY, ENTRY):
            self.owner = target

    def hook(self, target):
        if target == DMA:
            source, destination, length, mode = self.r[4:8]
            assert source & 15 == 0 and destination & 15 == 0
            assert length & 15 == 0 and length <= 272 and mode == 1
            for i in range(length // 4):
                value = word_value(i, self.pattern)
                if self.owner == lookup.ENTRY:
                    value = 0x20 + (i // 2) * 0x20 if i % 2 == 0 else 0x80000010
                self.put(destination + i * 4, value, 4)
        else:
            assert target == lookup.COPY
            source, destination, length = self.r[4:7]
            assert destination == lookup.CACHE and length == 224
            for i in range(length):
                self.put(destination + i, self.get(source + i, 1), 1)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register


class GameTableRangeLoaderTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(n) is None for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-table-range-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', source_body())
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>71I', rom, 0x583B4))
        cls.wrapper = list(struct.unpack_from('>69I', rom, 0x585C0))
        _, raw_lookup = lookup.screen.compile_candidate(cls.root, cls.output, 'lookup', lookup.source_body())
        _, raw_cache = installer.screen.compile_candidate(cls.root, cls.output, 'cache', installer.source_body())
        cls.connected = {}
        for address, words in ((ENTRY, cls.words),
                (lookup.ENTRY, lookup.apply_linked_guards(raw_lookup)),
                (lookup.INSTALL, installer.apply_linked_guards(raw_cache))):
            cls.connected.update(zip(range(address, address + len(words) * 4, 4), words))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = r'''
typedef unsigned int u32; typedef int s32; typedef unsigned char u8;
static u8 storage[640] __attribute__((aligned(16)));
static u32 dmaAddress,dmaDestination,dmaLength,dmaMode; static int calls,pattern;
static u32 value(int i) {
    static u32 initial[]={0xFFFFFFE0,0x80000000,0x12340000};
    return initial[pattern]+(u32)i*19;
}
s32 func_10004514(u32 address,void *destination,u32 length,s32 mode) {
    u32 *out=destination; u32 i;
    dmaAddress=address; dmaDestination=(u32)destination; dmaLength=length; dmaMode=mode; calls++;
    if(length>272 || ((u32)destination&15)) return -1;
    for(i=0;i<length/4;i++) out[i]=value(i);
    return -1;
}
''' + source_body() + '\n'

    def test_direct_complete_slot_and_source_shape_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']),
                         (71, 0x40, 0))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(hashlib.sha256(struct.pack('>71I', *self.words)).hexdigest(),
                         'aefe486d405c79f8b2c99f848b7f96fddfb3de3b7f41985a940671bd70aa7ce5')
        for name, expected in (('baseline', (75, 0x40, 46)),
                               ('placeholder', (3, 0, 71)),
                               ('baseline-entry', (71, 0x40, 5)),
                               ('entry-integer-sum', (71, 0x40, 2)),
                               ('argument-address-captured-length', (71, 0x48, 9))):
            record, words = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')
            self.assertNotEqual(words, self.retail)

    def test_safe_argument_assignment_never_reads_the_written_local_in_other_arguments(self):
        forms = dict(screen.candidates())
        unsafe = forms['integer-sum-address-first-argument']
        self.assertIn('aligned, ((address & 0xE)', unsafe)
        selected_call = next(line for line in source_body().splitlines() if 'func_10004514(' in line)
        self.assertEqual(selected_call.count('address'), 1)
        self.assertIn('(address = base + component)', selected_call)
        self.assertIn('((base + component) & 0xE)', selected_call)
        record, words = screen.compile_candidate(self.root, self.output, 'safe-early-assignment',
                                                 forms['argument-address-recomputed-length'])
        self.assertEqual((record['body_words'], record['frame'], record['real_differences']), (71, 0x40, 0))
        self.assertEqual(words, self.words)

    def test_actual_c_alignment_count_zero_and_all_bounded_pair_offsets(self):
        self.run_host(r'''
static u32 roots[]={0x12340,0x12344,0x12348,0x1234C};
u8 expected[640]; int n,a,k,i,j,cases=0; u32 base,address,aligned,length,result;
for(pattern=0;pattern<3;pattern++) for(n=0;n<=32;n++) for(a=0;a<16;a++) for(k=0;k<4;k++) {
    for(i=0;i<640;i++) storage[i]=expected[i]=0xA5;
    calls=0; base=roots[k]; address=base+(u32)-2*8;
    aligned=((u32)(storage+32+a)+8)&~15u;
    length=((address&14)+(u32)n*8+15)&~15u;
    for(i=0;i<(int)(length/4);i++) ((u32 *)(expected+(aligned-(u32)storage)))[i]=value(i);
    result=aligned+(address&15);
    for(i=0;i<n;i++) ((u32 *)(expected+(result-(u32)storage)))[i*2]+=base;
    if((u32)func_1502AF04(base,storage+32+a,(u32)-2,(u32)n)!=result || calls!=1
       || dmaAddress!=(address&~15u) || dmaDestination!=aligned || dmaLength!=length || dmaMode!=1) return 1;
    for(j=0;j<640;j++) if(storage[j]!=expected[j]) return 2;
    cases++;
}
if(cases!=6336) return 3;
''')

    def test_actual_c_wrapping_address_and_offset_values_keep_high_source_bits(self):
        self.run_host(r'''
static u32 bases[]={0,0xFFFFFFFC,0x7FFFFFF8,0x80000000,0x12340,0x12340,0x12350};
static u32 parts[]={0xFFFFFFFF,1,1,0xFFFFFFFF,0x7FFFFFFF,0x80000000,0xFFFFFFFE};
int i,j; u32 address,*result;
for(pattern=0;pattern<3;pattern++) for(i=0;i<7;i++) {
    calls=0; address=bases[i]+parts[i]*8;
    result=func_1502AF04(bases[i],storage+40,parts[i],5);
    if((u32)result!=(((u32)(storage+40)+8)&~15u)+(address&15)
       || calls!=1 || dmaAddress!=(address&~15u) || dmaLength!=(((address&14)+40+15)&~15u)) return 1;
    for(j=0;j<5;j++) if(result[j*2]!=value((address&15)/4+j*2)+bases[i]
       || result[j*2+1]!=value((address&15)/4+j*2+1)) return 2;
}
''')

    def test_complete_instruction_corpus_against_independent_outputs(self):
        coverage = [set(), set()]
        cases = 0
        for pattern in range(3):
            for phase in (0, 8):
                for count in range(33):
                    for alignment in range(16):
                        for low in (0, 4, 8, 12):
                            base, component = 0xFFFFF000 + low, 0xFFFFFFFF
                            address = (base + component * 8) & 0xFFFFFFFF
                            destination = (BUFFER + alignment + 8) & ~15
                            length = ((address & 14) + count * 8 + 15) & ~15
                            result = destination + (address & 15)
                            memory = memory_case(pattern)
                            expected = memory.copy()
                            for i in range(length // 4):
                                lookup.put_word(expected, destination + i * 4, word_value(i, pattern))
                            for i in range(count):
                                lookup.put_word(expected, result + i * 8,
                                                word_value((address & 15) // 4 + i * 2, pattern) + base)
                            models = [RangeOracle(words, memory, (base, BUFFER + alignment, component, count),
                                                  phase, pattern).run() for words in (self.retail, self.words)]
                            reference = models[0]
                            for i, model in enumerate(models):
                                coverage[i].update(model.visits)
                                self.assertEqual(model.r[2], result)
                                self.assertEqual(model.calls, [(DMA, address & ~15, destination, length, 1)])
                                self.assertEqual({a: b for a, b in model.memory.items()
                                                  if not STACK - 0x500 <= a < STACK + 0xC0},
                                                 {a: b for a, b in expected.items()
                                                  if not STACK - 0x500 <= a < STACK + 0xC0})
                                self.assertEqual(model.memory, reference.memory)
                                self.assertEqual(model.events, reference.events)
                            cases += 1
        self.assertEqual(cases, 12672)
        self.assertEqual(coverage, [set(range(ENTRY, ENTRY + 284, 4))] * 2)
        print('table range loader:', cases, 'two-way cases with independent memory expectations; all 71 words')

    def test_retail_variadic_caller_connected_to_recovered_range_and_checked_lookup(self):
        cases = 0
        range_hits = set()
        for phase in (0, 8):
            for root in (0, 0x12340):
                for depth in (1, 2, 3):
                    for count in (0, 1, 2, 5, 16):
                        memory = memory_case(1)
                        args = (root, count, BUFFER + 8, depth, *([1] * depth))
                        model = RangeOracle(self.wrapper, memory, args, phase, 1,
                                            self.connected, WRAPPER).run()
                        calls = [call for call in model.calls if call[0] == ENTRY]
                        self.assertEqual(len(calls), 1)
                        self.assertEqual(calls[0][2:], (BUFFER + 8, 1, count))
                        resolved = 0xAB1950 if root == 0 else root
                        # Component one reads the second pair, whose offset is 0x40.
                        resolved += (depth - 1) * 0x40
                        self.assertEqual(calls[0][1], resolved)
                        destination = (BUFFER + 16) & ~15
                        address = resolved + 8
                        length = ((address & 14) + count * 8 + 15) & ~15
                        self.assertEqual(model.calls[-1], (DMA, address & ~15, destination, length, 1))
                        self.assertEqual(model.r[2], destination + (address & 15))
                        for i in range(count):
                            start = destination + (address & 15) + i * 8
                            self.assertEqual(TimelineOracle.get(model, start, 4),
                                             (word_value((address & 15) // 4 + i * 2, 1) + resolved) & 0xFFFFFFFF)
                        range_hits.update(v for v in model.visits if ENTRY <= v < ENTRY + 284)
                        cases += 1
        self.assertEqual(cases, 60)
        self.assertEqual(range_hits, set(range(ENTRY, ENTRY + 284, 4)))
        print('table range caller:', cases, 'connected retail-wrapper cases; recovered callee all 71 words')

    def test_production_source_relocations_and_guard_free_identity(self):
        production = (self.root / 'conker/src/game_57FA0.c').read_text()
        body = re.search(r'u32 \*func_1502AF04\([^;{}]+\) \{\n.*?\n\}', production, re.S).group(0)
        self.assertEqual(body, source_body())
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            self.assertFalse(any(r['function'] == 'func_1502AF04' for r in csv.DictReader(file)))
        output = subprocess.run(['mips-linux-gnu-objdump', '-r', str(self.output / 'selected.o')],
                                check=True, capture_output=True, text=True).stdout
        relocations = re.findall(r'(?m)^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\S+)\s*$', output)
        self.assertEqual(relocations, [('00000064', 'R_MIPS_26', 'func_10004514')])
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
                                                    'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502AF04'], ENTRY)
        self.assertEqual(functions['func_1502AF04'], self.words)


if __name__ == '__main__':
    unittest.main()
