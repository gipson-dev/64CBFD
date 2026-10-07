"""Direct six-field cache, actual SDK packets and bounded native/guest effects."""

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

from tools.experiments import game_cached_primitive_color_candidates as screen
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

CACHE, LOD_CACHE, OUTPUT, SYNC = 0x800DD1C0, 0x800DD204, 0x20000, 0x24000
CACHES = tuple(screen.SYMBOLS.values())
LEGACY = '''Gfx *func_15142CF0(Gfx *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6, u8 *arg7) {
    if ((arg1 == D_800DD204) && (arg2 == D_800DD206) && (arg3 == D_800DD1C0) &&
        (arg4 == D_800DD1C2) && (arg5 == D_800DD1C4) && (arg6 == D_800DD1C6)) {
        return arg0;
    }

    if (*arg7 == 1) {
        gDPPipeSync(arg0++);
        *arg7 = 0;
    }

    arg0->words.w0 = 0xFA000000 | ((arg1 & 0xFF) << 8) | (arg2 & 0xFF);
    arg0->words.w1 = ((arg3 & 0xFF) << 24) | ((arg4 & 0xFF) << 16) | ((arg5 & 0xFF) << 8) | (arg6 & 0xFF);
    arg0++;

    D_800DD204 = arg1;
    D_800DD206 = arg2;
    D_800DD1C0 = arg3;
    D_800DD1C2 = arg4;
    D_800DD1C4 = arg5;
    D_800DD1C6 = arg6;
    return arg0;
}'''


def fields():
    for byte in range(256):
        yield (byte, 255 - byte, byte * 17 & 255, byte * 29 & 255,
            byte * 37 & 255, byte * 53 & 255)
    yield (-32768, -1, 32767, 128, -2, 256)
    yield (-0x80000000, 0x7FFFFFFF, 0x12345678, -2, 65536, -65535)
    yield (0x12340123, -65535, 65536, 32768, -32769, -65536)
    yield (1, 2, 3, 4, 5, 6)


def fixture(values, miss=6, flag=1, out=OUTPUT, sync=SYNC):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x100)}
    for base, size in ((CACHE - 8, 40), (LOD_CACHE - 8, 40), (OUTPUT - 8, 40), (SYNC - 8, 20)):
        memory.update({base + i: 0xA5 for i in range(size)})
    for i, (address, value) in enumerate(zip(CACHES, values)):
        put(memory, address, value + (i == miss), 2)
    put(memory, sync, flag, 1)
    return memory, (out, *[value & 0xFFFFFFFF for value in values], sync)


def reference(memory, args):
    memory, events = dict(memory), []
    output, *rest = args
    values, sync = rest[:6], rest[6]
    for address, value in zip(CACHES, values):
        cached = read(memory, address, 2)
        events.append(('R', address, 2, cached))
        if signed(value) != (cached if cached < 32768 else cached - 65536):
            break
    else:
        return memory, output, events
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
    store(output, 4, 0xFA000000 | (values[0] & 255) << 8 | values[1] & 255)
    store(output + 4, 4, sum((value & 255) << (24 - i * 8) for i, value in enumerate(values[2:])))
    output += 8
    for address, value in zip(CACHES, values):
        store(address, 2, value)
    return memory, output, events


def public_events(model):
    return [event for event in model.events if not STACK - 0x600 <= event[1] < STACK + 0x100]


class GameCachedPrimitiveColorMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-cached-primitive-color-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>77I', rom, screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        gbi = (cls.root / 'conker/include/2.0L/PR/gbi.h').read_text()
        mbi = (cls.root / 'conker/include/2.0L/PR/mbi.h').read_text()
        cls.macros = sdk_macro(mbi, '_SHIFTL')
        for name in ('G_SETPRIMCOLOR', 'G_RDPPIPESYNC', 'gDPSetPrimColor', 'gDPNoParam', 'gDPPipeSync'):
            cls.macros += sdk_macro(gbi, name)

    def receipt(self, name, value):
        (self.out / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def model(self, words, memory, args, phase=0):
        return TriangleOracle(words, memory, phase=phase, entry=screen.ENTRY, arguments=args).run()

    def test_full_direct_slot_frame_and_forty_eight_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (77, 8, 0))
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

    def test_all_six_field_bytes_full_signed_words_lazy_gates_aliases_and_complete_effects(self):
        coverage, count = set(), 0
        for values, miss, flag, out, sync, phase in itertools.product(fields(), range(7),
                (0, 1, 2, 255), (OUTPUT, CACHE, LOD_CACHE), (SYNC, OUTPUT, CACHE + 3, LOD_CACHE + 1), (0, 8)):
            memory, args = fixture(values, miss, flag, out, sync)
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
        self.assertEqual(count, 174720)
        self.assertEqual(coverage, set(range(screen.ENTRY, screen.ENTRY + 308, 4)))
        self.receipt('guest', dict(cases=count, all_words=77, independent_reference=True,
            full_memory_events_registers_equal=True, six_signed_halfword_caches=True, sync_only_when_one=True))

    def test_incoming_argument_homes_can_be_overwritten_after_values_are_loaded(self):
        count = 0
        for values, miss, flag, phase, alias in itertools.product(tuple(fields())[-4:], range(7),
                (0, 1, 2, 255), (0, 8), (False, True)):
            output = STACK + phase + 16
            sync = output + 8 if alias else SYNC
            memory, args = fixture(values, miss, flag, output, sync)
            for i, value in enumerate(args[4:]):
                put(memory, STACK + phase + 16 + i * 4, value)
            expected, result, _ = reference(memory, args)
            pair = [self.model(words, memory, args, phase) for words in (self.words, self.retail)]
            for model in pair:
                self.assertEqual(model.r[2], result)
                self.assertEqual(external_memory(model.memory), external_memory(expected))
                self.assertEqual([model.memory[output + i] for i in range(32)],
                    [expected[output + i] for i in range(32)])
            for attr in ('memory', 'events', 'r', 'f', 'calls', 'visits'):
                self.assertEqual(getattr(pair[0], attr), getattr(pair[1], attr), attr)
            count += 1
        self.assertEqual(count, 448)
        self.receipt('argument-homes', dict(cases=count, overwritten_homes=True,
            sync_alias_is_initialized_by_incoming_home=True, all_remaining_input_loads_precede_packet_writes=True))

    def test_cache_hit_skips_sync_output_and_required_bytes_fail_closed(self):
        values = (1, 2, 3, 4, 5, 6)
        memory, args = fixture(values, flag=1)
        for address in range(OUTPUT - 8, OUTPUT + 32):
            del memory[address]
        del memory[SYNC]
        for words in (self.words, self.retail):
            model = self.model(words, memory, args)
            self.assertEqual(model.r[2], OUTPUT)
            self.assertEqual(public_events(model), [('R', a, 2, v) for a, v in zip(CACHES, values)])
        for missing in (*CACHES, SYNC, OUTPUT):
            memory, args = fixture(values, miss=6 if missing in CACHES else 0)
            del memory[missing]
            for words in (self.words, self.retail):
                with self.assertRaises((AssertionError, KeyError)):
                    self.model(words, memory, args)

    def test_actual_native_32bit_sdk_macros_signed_fields_hits_and_sync_states(self):
        rows = ['{%s}' % ','.join('(s32)0x%Xu' % (v & 0xFFFFFFFF) for v in values) for values in fields()]
        self.fixture = '''typedef unsigned char u8;typedef short s16;typedef int s32;typedef unsigned int u32;
typedef struct {struct {u32 w0,w1;} words;} Gfx;
''' + self.macros + '\n'.join('s16 %s;' % name for name in screen.SYMBOLS) + '\n' + screen.SELECTED + '''
static const s32 values[260][6]={''' + ',\n'.join(rows) + '''};
static Gfx output[4];
static s16 *cache[6]={&D_800DD204,&D_800DD206,&D_800DD1C0,&D_800DD1C2,&D_800DD1C4,&D_800DD1C6};
'''
        self.run_host('''int n,miss,flag,i,changed,count=0;u8 sync;Gfx *result;u32 first,packed;
if(sizeof(void *)!=4 || sizeof(Gfx)!=8 || sizeof(s16)!=2)return 1;
for(n=0;n<260;n++)for(miss=0;miss<7;miss++)for(flag=0;flag<4;flag++){
    changed=0;packed=0;
    for(i=0;i<6;i++){
        *cache[i]=(s16)((u32)values[n][i]+(i==miss));
        changed|=values[n][i]!=*cache[i];
        if(i>=2)packed|=((u32)values[n][i]&255u)<<(24-(i-2)*8);
    }
    first=0xFA000000u|(((u32)values[n][0]&255u)<<8)|((u32)values[n][1]&255u);
    for(i=0;i<4;i++)output[i].words.w0=output[i].words.w1=0xA5A5A5A5u;
    sync=flag==3?255:flag;
    result=func_15142CF0(output,values[n][0],values[n][1],values[n][2],values[n][3],values[n][4],values[n][5],&sync);
    if(!changed){if(result!=output || sync!=(flag==3?255:flag))return 2;}
    else{
        if(result!=output+1+(flag==1) || sync!=(flag==1?0:flag==3?255:flag))return 3;
        if(flag==1 && (output[0].words.w0!=0xE7000000u || output[0].words.w1))return 4;
        if(output[flag==1].words.w0!=first || output[flag==1].words.w1!=packed)return 5;
        for(i=0;i<6;i++)if(*cache[i]!=(s16)values[n][i])return 6;
    }
    for(i=changed?1+(flag==1):0;i<4;i++)if(output[i].words.w0!=0xA5A5A5A5u || output[i].words.w1!=0xA5A5A5A5u)return 7;
    count++;
}
if(count!=7280)return 8;
''')
        self.receipt('native', dict(cases=7280, bits=32, real_sdk_macros=True, alias_scope='disjoint native storage'))

    def test_compiled_semantic_negatives_change_public_outputs_or_lazy_reads(self):
        forms = {'always-emit': screen.SELECTED.replace('minimumLod != D_800DD204', '1 || minimumLod != D_800DD204'),
            'sync-nonzero': screen.SELECTED.replace('*sync == 1', '*sync != 0'),
            'swapped-lod': screen.SELECTED.replace('output++, minimumLod, lodFraction, red', 'output++, lodFraction, minimumLod, red'),
            'swapped-colors': screen.SELECTED.replace('lodFraction, red, green, blue, alpha);', 'lodFraction, green, red, blue, alpha);'),
            'missing-clear': screen.SELECTED.replace('            *sync = 0;\n', ''),
            'unsigned-cache': screen.SELECTED,
            'missing-alpha-cache': screen.SELECTED.replace('        D_800DD1C6 = alpha;\n', '')}
        observed = {}
        for name, body in forms.items():
            declaration = screen.DECLARATIONS.replace('s16', 'u16') if name == 'unsigned-cache' else screen.DECLARATIONS
            _, words = screen.compile_candidate(self.root, self.out, name, body, declarations=declaration)
            changes = 0
            for values, miss, flag in itertools.product(((1, 2, 3, 4, 5, 6), (-1, -2, -3, -4, -5, -6)), range(7), (0, 1, 2)):
                memory, args = fixture(values, miss, flag)
                expected, result, events = reference(memory, args)
                actual = self.model(words, memory, args)
                changes += (external_memory(actual.memory), actual.r[2], public_events(actual)) != (
                    external_memory(expected), result, events)
            self.assertGreater(changes, 0, name)
            observed[name] = changes
        self.receipt('negatives', dict(count=7, detected=observed, private_layout_is_not_detection=True))

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
        self.assertEqual(target['size'], 308)
        self.assertEqual(text[target['value']:target['value'] + 308], isolated[:308])
        self.assertEqual({o - target['value']: r for o, r in rel.items() if target['value'] <= o < target['value'] + 308},
            self.record['relocations'])
        self.receipt('owner', dict(functions=89, neighbors=88, warnings=2, pools_unchanged=True))
        return objects[1]

    def test_copied_owner_real_padder_full_slot_and_six_independent_cache_relocations(self):
        obj = self.copied_owner()
        assembly = emit_padded_assembly(obj, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=self.root / 'conker/retail_word_patches.us.csv')
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        body = assembly[start:assembly.index('\n', end) + 1]
        self.assertEqual(len(re.findall(r'\.word 0x[0-9A-F]{8}', body)), 77)
        self.assertNotIn('__retail_overflow_' + screen.FUNCTION, assembly)
        source, padded, elf = (self.out / ('padded' + suffix) for suffix in ('.s', '.o', '.elf'))
        source.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + body)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(padded), str(source)], check=True, capture_output=True)
        _, functions, relocations = parse_object(padded)
        self.assertEqual(functions[screen.FUNCTION]['size'], 308)
        self.assertEqual(relocations, self.record['relocations'])
        entries = [entry for group in relocations.values() for entry in group]
        self.assertEqual({name for _, name in entries}, set(screen.SYMBOLS))
        for symbol in screen.SYMBOLS:
            self.assertEqual({kind for kind, name in entries if name == symbol},
                {'R_MIPS_HI16', 'R_MIPS_LO16'}, symbol)
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
            actual = list(struct.unpack_from('>77I', screen.sections(elf)['.text'][1]))
            self.assertEqual(actual, expected)
            if moved is not None:
                self.assertNotEqual(actual, self.retail, moved)

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
