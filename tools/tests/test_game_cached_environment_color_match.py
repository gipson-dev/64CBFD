"""Direct SDK color leaf, lazy cache/sync gates and bounded native/guest aliases."""

import csv
import itertools
import json
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_cached_environment_color_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests.game_animation_timeline_oracle import signed
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_dual_matrix_emitter import sdk_macro
from tools.tests.test_game_point_transform_match import put, read, external_memory
from tools.tests.test_game_queued_segment_writer import STACK
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests import test_game_random_curve_record as native

CACHE, OUTPUT, SYNC = 0x800DD1C8, 0x20000, 0x24000
LEGACY = '''Gfx *func_15142C10(Gfx *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, u8 *arg5) {
    if ((arg1 == D_800DD1C8) && (arg2 == D_800DD1CA) && (arg3 == D_800DD1CC) && (arg4 == D_800DD1CE)) {
        return arg0;
    }

    if (*arg5 == 1) {
        gDPPipeSync(arg0++);
        *arg5 = 0;
    }

    arg0->words.w0 = 0xFB000000;
    arg0->words.w1 = ((arg1 & 0xFF) << 24) | ((arg2 & 0xFF) << 16) | ((arg3 & 0xFF) << 8) | (arg4 & 0xFF);
    arg0++;

    D_800DD1C8 = arg1;
    D_800DD1CA = arg2;
    D_800DD1CC = arg3;
    D_800DD1CE = arg4;
    return arg0;
}'''


def colors():
    for byte in range(256):
        yield (byte, 255 - byte, byte * 17 & 255, byte * 29 & 255)
    yield (-32768, -1, 32767, 128)
    yield (-0x80000000, 0x7FFFFFFF, 0x12345678, -2)
    yield (0x12340123, -65535, 65536, 32768)
    yield (1, 2, 3, 4)


def fixture(channels, miss=4, flag=1, out=OUTPUT, sync=SYNC):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x100)}
    for base, size in ((CACHE - 8, 40), (OUTPUT - 8, 40), (SYNC - 8, 20)):
        memory.update({base + i: 0xA5 for i in range(size)})
    for i, channel in enumerate(channels):
        put(memory, CACHE + i * 2, channel + (i == miss), 2)
    put(memory, sync, flag, 1)
    return memory, (out, *[channel & 0xFFFFFFFF for channel in channels], sync)


def reference(memory, args):
    memory, events = dict(memory), []
    output, *rest = args
    channels, sync = rest[:4], rest[4]
    changed = False
    for i, channel in enumerate(channels):
        value = read(memory, CACHE + i * 2, 2)
        events.append(('R', CACHE + i * 2, 2, value))
        cached = value if value < 32768 else value - 65536
        if signed(channel) != cached:
            changed = True
            break
    if changed:
        flag = read(memory, sync, 1)
        events.append(('R', sync, 1, flag))

        def store(address, size, value):
            value &= (1 << (size * 8)) - 1
            events.append(('W', address, size, value))
            put(memory, address, value, size)

        if flag == 1:
            store(output, 4, 0xE7000000)
            store(output + 4, 4, 0)
            output += 8
            store(sync, 1, 0)
        store(output, 4, 0xFB000000)
        packed = sum((channel & 255) << (24 - i * 8) for i, channel in enumerate(channels))
        store(output + 4, 4, packed)
        output += 8
        for i, channel in enumerate(channels):
            store(CACHE + i * 2, 2, channel)
    return memory, output, events


def public_events(model):
    return [event for event in model.events if not STACK - 0x600 <= event[1] < STACK + 0x100]


class GameCachedEnvironmentColorMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-cached-environment-color-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>56I', rom, screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        gbi = (cls.root / 'conker/include/2.0L/PR/gbi.h').read_text()
        mbi = (cls.root / 'conker/include/2.0L/PR/mbi.h').read_text()
        cls.macros = sdk_macro(mbi, '_SHIFTL')
        for name in ('G_SETENVCOLOR', 'G_RDPPIPESYNC', 'gDPSetColor', 'DPRGBColor',
                'gDPSetEnvColor', 'gDPNoParam', 'gDPPipeSync'):
            cls.macros += sdk_macro(gbi, name)

    def receipt(self, name, value):
        (self.out / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def model(self, words, memory, args, phase=0):
        return TriangleOracle(words, memory, phase=phase, entry=screen.ENTRY, arguments=args).run()

    def test_full_direct_slot_frame_and_forty_eight_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (56, 8, 0))
        self.assertEqual(self.words, self.retail)
        records, exact = [], []
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                record, words = screen.compile_candidate(self.root, self.out, name + '-' + profile, body, profile)
                self.assertEqual(record['diagnostics'], '')
                if not record['differences']:
                    self.assertEqual(words, self.retail)
                    exact.append(record['name'])
                records.append(record)
        self.assertEqual(len(records), 48)
        self.assertEqual(exact, ['positive1-cursor0-sdk-o2g3'])
        self.receipt('controls', dict(measurements=records, exact=exact, sdk_macros=True, guards=0))

    def test_all_channel_bytes_signed_words_lazy_gates_aliases_and_complete_guest_effects(self):
        coverage, count = set(), 0
        for channels, miss, flag, out, sync, phase in itertools.product(colors(), range(5),
                (0, 1, 2, 255), (OUTPUT, CACHE), (SYNC, OUTPUT, CACHE + 3), (0, 8)):
            memory, args = fixture(channels, miss, flag, out, sync)
            expected, result, events = reference(memory, args)
            pair = [self.model(words, memory, args, phase) for words in (self.words, self.retail)]
            for model in pair:
                self.assertEqual(external_memory(model.memory), external_memory(expected))
                self.assertEqual(model.r[2], result)
                self.assertEqual(public_events(model), events)
                self.assertEqual(model.calls, [])
                coverage.update(model.visits)
            for attr in ('memory', 'events', 'r', 'f', 'calls', 'visits'):
                self.assertEqual(getattr(pair[0], attr), getattr(pair[1], attr), attr)
            count += 1
        self.assertEqual(count, 62400)
        self.assertEqual(coverage, set(range(screen.ENTRY, screen.ENTRY + 224, 4)))
        self.receipt('guest', dict(cases=count, all_words=56, independent_reference=True,
            full_memory_events_registers_equal=True, cache_is_signed_halfword=True, sync_only_when_one=True))

    def test_cache_hit_skips_sync_output_and_later_cache_reads_fail_closed(self):
        channels = (1, 2, 3, 4)
        memory, args = fixture(channels, flag=1)
        for address in range(OUTPUT - 8, OUTPUT + 32):
            del memory[address]
        del memory[SYNC]
        for words in (self.words, self.retail):
            model = self.model(words, memory, args)
            self.assertEqual(model.r[2], OUTPUT)
            self.assertEqual(public_events(model), [('R', CACHE + i * 2, 2, c) for i, c in enumerate(channels)])
        for missing in (CACHE, SYNC, OUTPUT):
            memory, args = fixture(channels, miss=0)
            del memory[missing]
            for words in (self.words, self.retail):
                with self.assertRaises((AssertionError, KeyError)):
                    self.model(words, memory, args)

    def test_actual_native_32bit_sdk_macros_signed_channels_hits_and_sync_states(self):
        rows = ['{%s}' % ','.join('(s32)0x%Xu' % (c & 0xFFFFFFFF) for c in channels) for channels in colors()]
        self.fixture = '''typedef unsigned char u8;typedef short s16;typedef int s32;typedef unsigned int u32;
typedef struct {struct {u32 w0,w1;} words;} Gfx;
''' + self.macros + '\n'.join('s16 %s;' % name for name in screen.SYMBOLS) + '\n' + screen.SELECTED + '''
static const s32 colors[260][4]={''' + ',\n'.join(rows) + '''};
static Gfx output[4];
static s16 *cache[4]={&D_800DD1C8,&D_800DD1CA,&D_800DD1CC,&D_800DD1CE};
'''
        self.run_host('''int n,miss,flag,i,changed,count=0;u8 sync;Gfx *result;u32 packed;
if(sizeof(void *)!=4 || sizeof(Gfx)!=8 || sizeof(s16)!=2)return 1;
for(n=0;n<260;n++)for(miss=0;miss<5;miss++)for(flag=0;flag<4;flag++){
    changed=0;packed=0;
    for(i=0;i<4;i++){
        *cache[i]=(s16)((u32)colors[n][i]+(i==miss));
        changed|=colors[n][i]!=*cache[i];
        packed|=((u32)colors[n][i]&255u)<<(24-i*8);
        output[i].words.w0=output[i].words.w1=0xA5A5A5A5u;
    }
    sync=flag==3?255:flag;
    result=func_15142C10(output,colors[n][0],colors[n][1],colors[n][2],colors[n][3],&sync);
    if(!changed){if(result!=output || sync!=(flag==3?255:flag))return 2;}
    else{
        if(result!=output+1+(flag==1) || sync!=(flag==1?0:flag==3?255:flag))return 3;
        if(flag==1 && (output[0].words.w0!=0xE7000000u || output[0].words.w1))return 4;
        if(output[flag==1].words.w0!=0xFB000000u || output[flag==1].words.w1!=packed)return 5;
        for(i=0;i<4;i++)if(*cache[i]!=(s16)colors[n][i])return 6;
    }
    for(i=changed?1+(flag==1):0;i<4;i++)if(output[i].words.w0!=0xA5A5A5A5u || output[i].words.w1!=0xA5A5A5A5u)return 7;
    count++;
}
if(count!=5200)return 8;
''')
        self.receipt('native', dict(cases=5200, bits=32, real_sdk_macros=True, alias_scope='disjoint native storage'))

    def test_compiled_semantic_negatives_change_public_outputs_or_lazy_reads(self):
        forms = {'always-emit': screen.SELECTED.replace('red != D_800DD1C8', '1 || red != D_800DD1C8'),
            'sync-nonzero': screen.SELECTED.replace('*sync == 1', '*sync != 0'),
            'wrong-opcode': screen.SELECTED.replace('gDPSetEnvColor', 'gDPSetBlendColor'),
            'swapped-colors': screen.SELECTED.replace('output++, red, green, blue, alpha', 'output++, green, red, blue, alpha'),
            'missing-clear': screen.SELECTED.replace('            *sync = 0;\n', ''),
            'unsigned-cache': screen.SELECTED}
        observed = {}
        for name, body in forms.items():
            declaration = screen.DECLARATIONS
            if name == 'unsigned-cache':
                declaration = declaration.replace('s16', 'u16')
            _, words = screen.compile_candidate(self.root, self.out, name, body, declarations=declaration)
            changes = 0
            for channels, miss, flag in itertools.product(((1, 2, 3, 4), (-1, -2, -3, -4)), range(5), (0, 1, 2)):
                memory, args = fixture(channels, miss, flag)
                expected, result, events = reference(memory, args)
                actual = self.model(words, memory, args)
                changes += (external_memory(actual.memory), actual.r[2], public_events(actual)) != (
                    external_memory(expected), result, events)
            self.assertGreater(changes, 0, name)
            observed[name] = changes
        self.receipt('negatives', dict(count=6, detected=observed, private_layout_is_not_detection=True))

    def copied_owner(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        baseline = source.replace(screen.SELECTED, LEGACY)
        self.assertEqual(baseline.count(LEGACY), 1)
        selected = baseline.replace(LEGACY, screen.SELECTED)
        objects, warning_sets = [], []
        for name, body in (('baseline', baseline), ('selected', selected)):
            obj, warnings = compile_owner(self.root, self.out, body, 'owner-' + name)
            warning_sets.append(warnings)
            processed = self.out / ('owner-' + name + '-postprocessed.o')
            shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.out / ('owner-' + name + '.c')).relative_to(self.root / 'conker')), '--post-process',
                str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker', check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warning_sets[0], warning_sets[1])
        self.assertEqual(len(warning_sets[1]), 2)
        old_text, old_functions, old_rel = parse_object(objects[0])
        text, functions, rel = parse_object(objects[1])
        self.assertEqual(set(functions), set(old_functions))
        self.assertEqual(len(functions), 89)
        for name, current in functions.items():
            if name == screen.FUNCTION:
                continue
            old = old_functions[name]
            self.assertEqual(text[current['value']:current['value'] + current['size']],
                old_text[old['value']:old['value'] + old['size']], name)
            self.assertEqual({o - current['value']: r for o, r in rel.items() if current['value'] <= o < current['value'] + current['size']},
                {o - old['value']: r for o, r in old_rel.items() if old['value'] <= o < old['value'] + old['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        target = functions[screen.FUNCTION]
        isolated, _, _ = parse_object(self.out / 'selected.o')
        self.assertEqual(target['size'], 224)
        self.assertEqual(text[target['value']:target['value'] + 224], isolated[:224])
        self.assertEqual({o - target['value']: r for o, r in rel.items() if target['value'] <= o < target['value'] + 224},
            self.record['relocations'])
        self.receipt('owner', dict(functions=89, neighbors=88, warnings=2, pools_unchanged=True))
        return objects[1]

    def test_copied_owner_real_padder_full_slot_and_independent_cache_relocations(self):
        obj = self.copied_owner()
        assembly = emit_padded_assembly(obj, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=self.root / 'conker/retail_word_patches.us.csv')
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        body = assembly[start:assembly.index('\n', end) + 1]
        self.assertEqual(len(re.findall(r'\.word 0x[0-9A-F]{8}', body)), 56)
        self.assertNotIn('__retail_overflow_' + screen.FUNCTION, assembly)
        source, padded, elf = (self.out / ('padded' + suffix) for suffix in ('.s', '.o', '.elf'))
        source.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + body)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(padded), str(source)], check=True, capture_output=True)
        _, functions, relocations = parse_object(padded)
        self.assertEqual(functions[screen.FUNCTION]['size'], 224)
        self.assertEqual(relocations, self.record['relocations'])
        for moved in (None, *screen.SYMBOLS):
            addresses = {name: address + (0x18000 if name == moved else 0) for name, address in screen.SYMBOLS.items()}
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'color.ld'), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X' % pair for pair in addresses.items()], '-o', str(elf), str(padded)], check=True, capture_output=True)
            expected = self.retail.copy()
            for offset, entries in self.record['relocations'].items():
                for kind, name in entries:
                    self.assertIn(kind, ('R_MIPS_HI16', 'R_MIPS_LO16'))
                    value = ((addresses[name] + 0x8000) >> 16) if kind == 'R_MIPS_HI16' else addresses[name]
                    expected[offset // 4] = expected[offset // 4] & 0xFFFF0000 | value & 0xFFFF
            actual = list(struct.unpack_from('>56I', screen.sections(elf)['.text'][1]))
            self.assertEqual(actual, expected)

    def test_installed_direct_source_linked_slot_and_unchanged_guard_history(self):
        self.assertEqual((self.root / 'conker/src/game_16EE20.c').read_text().count(screen.SELECTED), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))


if __name__ == '__main__':
    unittest.main()
