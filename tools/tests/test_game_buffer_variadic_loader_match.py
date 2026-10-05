"""Direct SDK-varargs wrapper match; incoming stack seeds qualify target code only."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_buffer_variadic_loader_candidates as screen
from tools.tests import test_game_buffer_resource_loader as buffer
from tools.tests import test_game_cached_lookup_match as lookup
from tools.tests import test_game_cache_installer_match as installer
from tools.tests import test_game_variadic_table_range_match as paths
from tools.match_progress import load_elf_functions


ENTRY, GAME_CALLER, BZERO = 0x1502B8E0, 0x1500ABA0, 0x100226F0
SEEDS = (0, 1, 0x80000010, 0x10000010, 0x90000011, 0xF0000000, 0xFFFFFFFF)


def source_body():
    return dict(screen.candidates())['selected-gate-first']


class BoundaryOracle(buffer.BufferOracle):
    """Lookup writes are optional here; descriptor seeds are physical mapped bytes."""

    def __init__(self, words, memory, arguments, phase=0, case=None):
        super().__init__(words, memory, arguments, phase, case, entry=ENTRY)

    def hook(self, target):
        if target == lookup.ENTRY:
            index = self.lookups - 1
            if not self.case.get('unwritten'):
                descriptor = self.case.get('descriptor', 0xF0000010) + index
                self.put(self.r[6], 0xF0000000 if index == self.case.get('missing', -1) else descriptor, 4)
            result = 0xFFFFFFF0 if self.case.get('wrap') and index == 0 else 8 * (index + 1)
        else:
            assert target == buffer.ENTRY
            result = self.case.get('result', 0xFFFFFFFF)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result & 0xFFFFFFFF


class CallerOracle(buffer.BufferOracle):
    """Full Game caller instructions, with SDK bzero as a bounded byte-write hook."""

    def record_call(self, target):
        if target in (ENTRY, BZERO):
            call = (target, *self.r[4:8 if target == ENTRY else 6])
            self.calls.append(call)
            self.events.append(('CALL', *call))
        else:
            super().record_call(target)

    def hook(self, target):
        if target != BZERO:
            return super().hook(target)
        destination, length = self.r[4:6]
        assert (destination, length) in ((0x800BE4A0, 60), (0x800DDA90, 240), (0x800DD478, 1560))
        for i in range(length):
            self.put(destination + i, 0, 1)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register


class GameBufferVariadicLoaderMatchTests(unittest.TestCase):
    run_host = buffer.GameBufferResourceLoaderTests.run_host
    assert_models_equal = buffer.GameBufferResourceLoaderTests.assert_models_equal

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(n) is None for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-buffer-variadic-loader-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', source_body())
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>53I', cls.rom, 0x58D90))
        cls.caller = list(struct.unpack_from('>29I', cls.rom, 0x38050))
        cls.connected = {}
        _, loader = buffer.screen.compile_candidate(cls.root, cls.output, 'loader', buffer.source_body())
        _, raw_lookup = lookup.screen.compile_candidate(cls.root, cls.output, 'lookup', lookup.source_body())
        _, raw_cache = installer.screen.compile_candidate(cls.root, cls.output, 'cache', installer.source_body())
        for address, words in ((buffer.ENTRY, loader),
                (lookup.ENTRY, lookup.apply_linked_guards(raw_lookup)),
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
static u32 storage[64], metadata[16], advances[16], expectedBase, cap, result, depth;
static s32 items[16];
static int lookups,loads,consumed,error,expectedLookups,missing;
static void *expectedBuffer;
static u32 *lastDescriptor;
static void reset(u32 count,int absent,int pattern,u32 flags,u32 limit) {
    int i;depth=count;missing=absent;cap=limit;result=pattern==2?0:0xFFFFFFFF;
    lookups=loads=consumed=error=0;lastDescriptor=NULL;expectedBase=(u32)D_AB1950;
    expectedLookups=absent<0?(int)count:absent+1;expectedBuffer=storage+4;
    for(i=0;i<64;i++) storage[i]=0xA5A5A5A5;
    for(i=0;i<16;i++) {
        items[i]=pattern==2?1:i+1;advances[i]=(u32)(8*(i+1));metadata[i]=flags|((u32)i+1);
    }
    if(pattern==1) {
        items[0]=-1;items[1]=(s32)0x80000000;items[2]=0x7FFFFFFF;
        advances[0]=0xFFFFFFF0;advances[1]=0x80000001;
    }
    if(absent>=0) metadata[absent]=0xF0000000;
}
s32 func_1502AC88(u32 base,s32 item,u32 *descriptor) {
    int i=lookups++;
    if(i>=expectedLookups || base!=expectedBase || item!=items[i] || loads
       || (lastDescriptor && descriptor!=lastDescriptor)) error=1;
    *descriptor=metadata[i];lastDescriptor=descriptor;expectedBase+=advances[i];
    return (s32)advances[i];
}
u32 func_1502B224(u32 base,void *out,u32 descriptor,u32 limit) {
    loads++;
    if(loads!=1 || lookups!=expectedLookups || base!=expectedBase || out!=expectedBuffer
       || descriptor!=metadata[depth-1] || limit!=cap) error=2;
    *(u32 *)out=0xC0FFEE00;return result;
}
#undef va_arg
#define va_arg(path,type) (consumed++,__builtin_va_arg(path,type))
/* Native cases below always execute a descriptor-writing lookup first. */
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wmaybe-uninitialized"
''' + source_body() + '\n#pragma GCC diagnostic pop\n'

    def test_direct_body_frame_and_compiler_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (53, 0x48, 0))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(hashlib.sha256(struct.pack('>53I', *self.words)).hexdigest(),
                         '2212c3662f9ec8a1cd54a8a6b594e65e25d31294efb74d9580842c5901633fbd')
        self.assertEqual(len(screen.candidates()), 133)
        for name, expected in (('placeholder', (3, 0, 53)), ('baseline', (53, 0x48, 5)),
                ('layout-1', (53, 0x48, 2)), ('gate-first', (53, 0x48, 3)),
                ('selected-zero-descriptor', (54, 0x48, 41)), ('selected-one-descriptor', (55, 0x48, 44))):
            record, _ = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected)
            self.assertEqual(record['diagnostics'], '')

    def test_native_positive_depth_signed_components_flags_caps_and_full_consumption(self):
        self.run_host(r'''
static u32 caps[]={0,1,0xFFFFFFFF};int d,absent,pattern,flag,c,cases=0,i;u32 actual;
for(pattern=0;pattern<3;pattern++) for(d=1;d<=16;d++) for(absent=-1;absent<d;absent++)
for(flag=0;flag<16;flag++) for(c=0;c<3;c++) {
    reset((u32)d,absent,pattern,(u32)flag<<28,caps[c]);
    actual=func_1502B8E0(expectedBuffer,cap,depth,
        items[0],items[1],items[2],items[3],items[4],items[5],items[6],items[7],
        items[8],items[9],items[10],items[11],items[12],items[13],items[14],items[15]);
    if(error || consumed!=d || lookups!=expectedLookups || loads!=(absent<0)
       || actual!=(absent<0?result:0) || storage[4]!=(absent<0?0xC0FFEE00:0xA5A5A5A5)) return 1;
    for(i=0;i<64;i++) if(i!=4 && storage[i]!=0xA5A5A5A5) return 2;
    cases++;
}
if(cases!=21888) return 3;
''')

    def test_native_missing_path_does_not_touch_null_buffer(self):
        self.run_host(r'''
reset(4,0,1,0xF0000000,0xFFFFFFFF);expectedBuffer=NULL;
if(func_1502B8E0(NULL,cap,4,items[0],items[1],items[2],items[3])
   || error || consumed!=4 || lookups!=1 || loads || storage[4]!=0xA5A5A5A5) return 1;
''')

    def test_target_boundary_full_memory_events_seed_and_argument_reads(self):
        cases, coverage = 0, [set(), set()]
        for pattern in range(3):
            items = paths.components(pattern)
            for depth in range(9):
                for missing in range(-2, depth):
                    for phase in (0, 8):
                        for seed in SEEDS:
                            memory = buffer.memory_case()
                            lookup.put_word(memory, buffer.table.STACK + phase - 0x14, seed)
                            args = (buffer.table.BUFFER + 8, 15, depth, *items)
                            case = dict(unwritten=missing == -2, missing=missing, wrap=pattern == 1,
                                        result=0 if pattern == 2 else 0xFFFFFFFF)
                            models = [BoundaryOracle(words, memory, args, phase, case).run()
                                      for words in (self.retail, self.words)]
                            reference = models[0]
                            expectedLookups = (0 if depth == 0 else 1 if missing == -2 and not seed & 0x0FFFFFFF
                                               else missing + 1 if missing >= 0 else depth)
                            self.assertEqual(reference.lookups, expectedLookups)
                            loader = [call for call in reference.calls if call[0] == buffer.ENTRY]
                            loads = depth == 0 or missing < 0 and (missing != -2 or seed & 0x0FFFFFFF != 0)
                            self.assertEqual(len(loader), int(loads))
                            self.assertEqual(reference.r[2], case['result'] if loads else 0)
                            if loads:
                                base = 0xAB1950
                                for i in range(expectedLookups):
                                    base = (base + (0xFFFFFFF0 if pattern == 1 and i == 0 else 8 * (i + 1))) & 0xFFFFFFFF
                                descriptor = seed if depth == 0 or missing == -2 else 0xF0000010 + depth - 1
                                self.assertEqual(loader, [(buffer.ENTRY, base, buffer.table.BUFFER + 8, descriptor, 15)])
                            self.assertEqual([address for address, size, _ in reference.reads if size == 4
                                and buffer.table.STACK + phase + 0xC <= address < buffer.table.STACK + phase + 0x4C],
                                [buffer.table.STACK + phase + 0xC + i * 4 for i in range(depth)])
                            if missing == -2 or depth == 0:
                                self.assertFalse(any(address == buffer.table.STACK + phase - 0x14
                                    for address, _, _ in reference.stores))
                            for i, model in enumerate(models):
                                coverage[i].update(model.visits)
                                self.assert_models_equal(model, reference)
                            cases += 1
        self.assertEqual(cases, 2268)
        self.assertEqual(coverage, [set(range(ENTRY, ENTRY + 212, 4))] * 2)
        print('buffer variadic wrapper:', cases, 'two-way boundary cases; all 53 words, physical descriptor seeds')

    def test_descriptor_initializers_fail_zero_depth_seed_witness(self):
        memory = buffer.memory_case()
        lookup.put_word(memory, buffer.table.STACK - 0x14, 0x90000011)
        args = (buffer.table.BUFFER + 8, 15, 0, 99)
        retail = BoundaryOracle(self.retail, memory, args).run()
        for name in ('selected-zero-descriptor', 'selected-one-descriptor'):
            _, words = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            actual = BoundaryOracle(words, memory, args).run()
            self.assertNotEqual(actual.calls, retail.calls)
            self.assertNotEqual(actual.memory, retail.memory)
            self.assertEqual(retail.calls, [(buffer.ENTRY, 0xAB1950, buffer.table.BUFFER + 8, 0x90000011, 15)])

    def test_connected_actual_cache_lookup_and_buffer_loader(self):
        cases = 0
        for phase in (0, 8):
            for depth in range(1, 6):
                for missing in range(-1, depth):
                    for descriptor in (0x80000010, 0x10000010, 0x90000011):
                        for cap in (0, 1, 15, 16, 17):
                            case = dict(lookupDescriptor=descriptor, missing=missing, decoded=32, mutation=True)
                            args = (buffer.table.BUFFER + 8, cap, depth, *([1] * depth))
                            models = [buffer.BufferOracle(words, buffer.memory_case(), args, phase, case,
                                                          self.connected, ENTRY).run()
                                      for words in (self.retail, self.words)]
                            self.assert_models_equal(models[1], models[0])
                            self.assertEqual(models[0].lookups, depth if missing < 0 else missing + 1)
                            calls = [call for call in models[0].calls if call[0] == buffer.ENTRY]
                            self.assertEqual(calls, [] if missing >= 0 else [
                                (buffer.ENTRY, 0xAB1950 + depth * 0x40, buffer.table.BUFFER + 8, descriptor, cap)])
                            expected = 0 if missing >= 0 else 32 if descriptor & 0x70000000 == 0x10000000 else buffer.amount_for(descriptor, cap)
                            self.assertEqual(models[0].r[2], expected)
                            cases += 1
        self.assertEqual(cases, 600)
        print('buffer variadic wrapper:', cases, 'connected actual lookup/cache/loader cases')

    def test_connected_zero_depth_target_incoming_seeds(self):
        for phase in (0, 8):
            for seed in SEEDS:
                memory = buffer.memory_case()
                lookup.put_word(memory, buffer.table.STACK + phase - 0x14, seed)
                args = (buffer.table.BUFFER + 8, 0, 0, 99)
                models = [buffer.BufferOracle(words, memory, args, phase, dict(decoded=32), self.connected, ENTRY).run()
                          for words in (self.retail, self.words)]
                self.assert_models_equal(models[1], models[0])
                self.assertEqual(models[0].lookups, 0)
                self.assertIn((buffer.ENTRY, 0xAB1950, buffer.table.BUFFER + 8, seed, 0), models[0].calls)
                self.assertEqual(models[0].r[2], 32 if seed & 0x70000000 == 0x10000000 else buffer.amount_for(seed, 0))

    def test_connected_allocation_failure_and_real_syscall_prefix(self):
        cases = 0
        self.assertEqual(struct.unpack_from('>I', self.rom, 0xDAC20)[0], 0x0000000C)
        for phase in (0, 8):
            for depth in (1, 3):
                args = (buffer.table.BUFFER + 8, 15, depth, *([1] * depth))
                failure = dict(lookupDescriptor=0x90000011, failure=True, mutation=True)
                models = [buffer.BufferOracle(words, buffer.memory_case(), args, phase, failure, self.connected, ENTRY).run()
                          for words in (self.retail, self.words)]
                self.assert_models_equal(models[1], models[0])
                self.assertEqual(models[0].r[2], 0)
                self.assertEqual(models[0].calls[-1], (buffer.ALLOC, 15, 1, 2, 2))
                self.assertFalse(any(call[0] in (buffer.DECODE, buffer.ERROR, buffer.FREE) for call in models[0].calls))
                for decoded in (0, 0xFFFFFFFF):
                    case = dict(lookupDescriptor=0x90000011, decoded=decoded, mutation=True)
                    models = [buffer.StopOnTrapOracle(words, buffer.memory_case(), args, phase, case, self.connected, ENTRY)
                              for words in (self.retail, self.words)]
                    for model in models:
                        with self.assertRaises(buffer.TrapBoundary):
                            model.run()
                        self.assertEqual(model.calls[-1], (buffer.ERROR,))
                        self.assertFalse(any(call[0] == buffer.FREE for call in model.calls))
                        self.assertEqual(model.r[17], decoded)
                        self.assertEqual(model.r[31], buffer.ENTRY + 0xE8)
                        self.assertEqual(model.peek(buffer.ERROR_WORD, 4), 0x0C000036)
                    self.assert_models_equal(models[1], models[0])
                    cases += 1
        self.assertEqual(cases, 8)
        print('buffer variadic wrapper:', cases, 'connected mismatch prefixes stop at original syscall boundary')

    def test_full_game_caller_and_same_physical_descriptor_cell(self):
        cases = 0
        for phase in (0, 8):
            for component in (1, 2, 3):
                for missing in range(-1, 3):
                    for descriptor in (0x80000011, 0x90000011):
                        memory = buffer.memory_case()
                        for address, length in ((0x800BE4A0, 64), (0x800DDA90, 240), (0x800DD478, 1560)):
                            memory.update({address + i: 0xA5 for i in range(-16, length + 16)})
                        case = dict(lookupDescriptor=descriptor, missing=missing, decoded=32)
                        models = []
                        for words in (self.retail, self.words):
                            code = self.connected.copy()
                            code.update(zip(range(ENTRY, ENTRY + 212, 4), words))
                            models.append(CallerOracle(self.caller, memory, (component,), phase, case, code, GAME_CALLER).run())
                        self.assert_models_equal(models[1], models[0])
                        model = models[0]
                        self.assertTrue(set(range(GAME_CALLER, GAME_CALLER + 116, 4)) <= model.visits)
                        self.assertIn((ENTRY, 0x800BE4A0, 60, 3, 12), model.calls)
                        self.assertEqual([call[2] for call in model.calls if call[0] == lookup.ENTRY],
                                         [12, component, 10][:3 if missing < 0 else missing + 1])
                        self.assertEqual({call[3] for call in model.calls if call[0] == lookup.ENTRY},
                                         {buffer.table.STACK + phase - 0x34})
                        self.assertEqual([call for call in model.calls if call[0] == BZERO],
                                         [(BZERO, 0x800BE4A0, 60), (BZERO, 0x800DDA90, 240), (BZERO, 0x800DD478, 1560)])
                        for address, length in ((0x800DDA90, 240), (0x800DD478, 1560)):
                            self.assertEqual(bytes(model.memory[address + i] for i in range(length)), bytes(length))
                        # The two cleared arrays are adjacent, so fence their combined extent.
                        self.assertEqual(model.memory[0x800DD477], 0xA5)
                        self.assertEqual(model.memory[0x800DDB80], 0xA5)
                        cases += 1
        self.assertEqual(cases, 48)
        print('buffer variadic wrapper:', cases, 'full 29-word Game caller cases; caller-entry SP-0x34 descriptor')

    def test_production_source_complete_linked_slots_and_caller_frames(self):
        source = (self.root / 'conker/src/game_57FA0.c').read_text()
        self.assertEqual(re.search(r'u32 func_1502B8E0\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0), source_body())
        self.assertNotRegex(source_body(), r'descriptor\s*=')
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        for name, offset, count, frame in (('func_1502B8E0', 0x58D90, 53, 0x48),
                ('func_1500ABA0', 0x38050, 29, 0x20), ('func_10008180', 0x8180, 214, 0xF0)):
            self.assertEqual(addresses[name], int(name[5:], 16))
            self.assertEqual(functions[name], list(struct.unpack_from('>' + str(count) + 'I', self.rom, offset)))
            self.assertEqual(functions[name][0], 0x27BD0000 | ((-frame) & 0xFFFF))
        prototype = 'u32 func_1502B8E0(void *buffer, u32 cap, u32 depth, ...);'
        for file in ('game_57FA0.c', 'game_36680.c', 'init_8180.c'):
            self.assertIn(prototype, (self.root / 'conker/src' / file).read_text())
        print('buffer variadic wrapper complete hash:', hashlib.sha256(struct.pack('>53I', *self.words)).hexdigest())

    def test_unlinked_relocations_and_no_word_guards(self):
        output = subprocess.run(['mips-linux-gnu-objdump', '-r', str(self.output / 'selected.o')],
                                check=True, capture_output=True, text=True).stdout
        actual = {int(o, 16): (kind, symbol) for o, kind, symbol in re.findall(
            r'(?m)^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\S+)\s*$', output)}
        self.assertEqual(actual, {0x2C: ('R_MIPS_HI16', 'D_AB1950'), 0x34: ('R_MIPS_LO16', 'D_AB1950'),
                                 0x70: ('R_MIPS_26', 'func_1502AC88'), 0xA4: ('R_MIPS_26', 'func_1502B224')})
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            self.assertFalse(any(r['function'] == 'func_1502B8E0' for r in csv.DictReader(file)))


if __name__ == '__main__':
    unittest.main()
