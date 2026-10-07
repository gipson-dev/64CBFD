"""Original translation arithmetic, wrapped ABI addresses and sequential aliases."""

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

from tools.experiments import game_matrix_translation_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests.game_animation_timeline_oracle import bits
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read, external_memory
from tools.tests.test_game_queued_segment_writer import STACK
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests import test_game_random_curve_record as native

MATRIX, OUTPUT, POINT, STATUS = 0x28000, 0x20000, 0x26000, 0x800DCA00
PARENT, PARENT_ROM = 0x15143134, 0x1705E4
INDICES = (0, 1, -1, 2, -2, 0x7FFFFFFF, -0x80000000, 0x02000000, -0x02000001, 0x40000001)
ALIASES = (None, -4, 0x18, 0x1C, 0x30, 0x34, 0x38, 0x3C)
HALVES = ((-32768, -32768), (-32768, -1), (-32768, 0), (-32768, 32767),
    (-32767, 32767), (-1, -32768), (-1, -1), (-1, 32767), (0, -1), (0, 0),
    (0, 1), (0, 32767), (1, -32768), (1, 32767), (32767, -32768), (32767, 32767))
FLOATS = (0, 0x80000000, 1, 0x80000001, 0x007FFFFF, 0x00800000, 0x3F800000,
    0xBF800000, 0x7F7FFFFF, 0x7F800000, 0xFF800000, 0x7FC12345, 0xFFC12345,
    0x7F812345, 0x00800001, 0x80800001)
LEGACY = '''void func_15142314(u8 *arg0, s32 arg1, f32 *arg2) {
    u8 *ptr = arg0 + (arg1 << 6);
    f32 scale = 1.0f / 65536.0f;

    if (D_800C3E90 != 0) {
        arg2[0] = (f32)(((*(s16 *)(ptr + 0x18)) << 16) + *(s16 *)(ptr + 0x38)) * scale;
        arg2[1] = (f32)(((*(s16 *)(ptr + 0x1A)) << 16) + *(s16 *)(ptr + 0x3A)) * scale;
        arg2[2] = (f32)(((*(s16 *)(ptr + 0x1C)) << 16) + *(s16 *)(ptr + 0x3C)) * scale;
    } else {
        arg2[0] = *(f32 *)(ptr + 0x30);
        arg2[1] = *(f32 *)(ptr + 0x34);
        arg2[2] = *(f32 *)(ptr + 0x38);
    }
}'''


def half(value):
    value &= 65535
    return value if value < 32768 else value - 65536


def pairs(index):
    return tuple((half(index * (2 * axis + 1)), half(index * (17 + axis * 12) + 3)) for axis in range(3))


def edge_pairs(index):
    return tuple(HALVES[(index + axis * 5) % len(HALVES)] for axis in range(3))


def float_words(index):
    return tuple(FLOATS[(index + axis * 5) % len(FLOATS)] for axis in range(3))


def fixture(flag=1, values=None, floats=None, index=0, alias=None, selected=MATRIX, output=None):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x140)}
    for base, size in ((selected - 80, 192), (OUTPUT - 16, 48),
            (screen.FLAG - 4, 24), (POINT - 8, 32), (STATUS - 4, 32)):
        memory.update({(base + i) & 0xFFFFFFFF: 0xA5 for i in range(size)})
    if flag:
        for axis, (high, low) in enumerate(values or edge_pairs(0)):
            put(memory, (selected + 0x18 + axis * 2) & 0xFFFFFFFF, high, 2)
            put(memory, (selected + 0x38 + axis * 2) & 0xFFFFFFFF, low, 2)
    else:
        for axis, word in enumerate(floats or float_words(0)):
            put(memory, (selected + 0x30 + axis * 4) & 0xFFFFFFFF, word)
    put(memory, screen.FLAG, flag, 1)
    output = output if output is not None else OUTPUT if alias is None else (selected + alias) & 0xFFFFFFFF
    base = (selected - ((index & 0xFFFFFFFF) << 6)) & 0xFFFFFFFF
    return memory, (base, index & 0xFFFFFFFF, output)


def reference(memory, args):
    memory, events = dict(memory), []
    base, index, output = args
    selected = (base + (index << 6)) & 0xFFFFFFFF
    flag = read(memory, screen.FLAG, 1)
    events.append(('R', screen.FLAG, 1, flag))
    for axis in range(3):
        if flag:
            high_address, low_address = ((selected + offset + axis * 2) & 0xFFFFFFFF for offset in (0x18, 0x38))
            high, low = read(memory, high_address, 2), read(memory, low_address, 2)
            events.extend((('R', high_address, 2, high), ('R', low_address, 2, low)))
            # The exact integer numerator and power-of-two scale give the RNE bits independently.
            value = bits((half(high) * 65536 + half(low)) / 65536.0)
        else:
            address = (selected + 0x30 + axis * 4) & 0xFFFFFFFF
            value = read(memory, address)
            events.append(('R', address, 4, value))
        address = (output + axis * 4) & 0xFFFFFFFF
        events.append(('W', address, 4, value))
        put(memory, address, value)
    return memory, events


def public_events(model):
    return [event for event in model.events if not STACK - 0x600 <= event[1] < STACK + 0x140]


class ConnectedTranslationOracle(TriangleOracle):
    def record_call(self, target):
        assert target == screen.ENTRY
        self.calls.append((target, *self.arguments(3)))


class GameMatrixTranslationRecoveryTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-matrix-translation-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>49I', rom, screen.ROM))
        cls.parent = list(struct.unpack_from('>98I', rom, PARENT_ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def model(self, words, memory, args, phase=0):
        return TriangleOracle(words, memory, phase=phase, entry=screen.ENTRY, arguments=args).run()

    def check_case(self, memory, args, phase=0, coverage=None):
        expected, events = reference(memory, args)
        pair = [self.model(words, memory, args, phase) for words in (self.words, self.retail)]
        for model in pair:
            self.assertEqual(external_memory(model.memory), external_memory(expected))
            self.assertEqual(public_events(model), events)
            self.assertEqual(model.calls, [])
            if coverage is not None:
                coverage.update(model.visits)
        self.assertEqual(pair[0].memory, pair[1].memory)
        return pair

    def test_every_signed_halfword_in_each_field_and_all_nonzero_flag_bytes(self):
        coverage, flags = set(), set()
        for n in range(65536):
            flag = n % 255 + 1
            flags.add(flag)
            memory, args = fixture(flag, pairs(n), index=INDICES[n % 10],
                selected=0xFFFFFFC0 if n & 4 else MATRIX)
            self.check_case(memory, args, n % 2 * 8, coverage)
        self.assertEqual(flags, set(range(1, 256)))
        self.assertEqual(coverage, set(range(screen.ENTRY, screen.ENTRY + 164, 4)))
        self.receipt('halves', dict(cases=65536, every_halfword_per_field=True,
            all_nonzero_flag_bytes=True, independent_exact_numerator_reference=True,
            cartesian_six_field_domain=False, model='binary32 round-to-nearest-even; no general FCSR'))

    def test_edges_float_bit_copies_wrapped_indices_and_sequential_input_output_aliases(self):
        count, coverage = 0, set()
        for flag, n, index, alias, selected, phase in itertools.product((1, 128, 255), range(16),
                INDICES, ALIASES, (MATRIX, 0xFFFFFFC0), (0, 8)):
            memory, args = fixture(flag, edge_pairs(n), index=index, alias=alias, selected=selected)
            self.check_case(memory, args, phase, coverage)
            count += 1
        fixed = count
        for n, index, alias, selected, phase in itertools.product(range(16), INDICES, ALIASES,
                (MATRIX, 0xFFFFFFC0), (0, 8)):
            memory, args = fixture(0, floats=float_words(n), index=index, alias=alias, selected=selected)
            self.check_case(memory, args, phase, coverage)
            count += 1
        self.assertEqual((fixed, count - fixed), (15360, 5120))
        self.assertEqual(coverage, set(range(screen.ENTRY, screen.ENTRY + 196, 4)))
        for flag, n, phase in itertools.product((0, 1, 255), range(16), (0, 8)):
            memory, args = fixture(flag, edge_pairs(n), float_words(n), output=screen.FLAG)
            self.check_case(memory, args, phase)
            count += 1
        self.assertEqual(count, 20576)
        self.receipt('aliases', dict(cases=count, fixed_matrix_aliases=15360, float_matrix_aliases=5120,
            flag_output_aliases=96, all_words=49, preserved_state=True,
            signed_zero_subnormal_infinity_quiet_and_signaling_nan_copies=True))

    def test_actual_native_32bit_body_with_wrapped_indices_and_complete_alias_storage(self):
        floats = ','.join('0x%Xu' % value for value in FLOATS)
        indices = ','.join('(s32)0x%Xu' % (value & 0xFFFFFFFF) for value in INDICES)
        self.fixture = '''typedef unsigned char u8;typedef short s16;typedef int s32;typedef unsigned int u32;typedef float f32;
u8 D_800C3E90;
''' + screen.SELECTED + '''
static union {double align;u8 bytes[96];} actual,want;
static union {double align;u8 bytes[32];} output,wantOutput;
static const u32 floatWords[16]={''' + floats + '''};
static const s32 indices[10]={''' + indices + '''};
static const int aliases[8]={-1000,-4,0x18,0x1C,0x30,0x34,0x38,0x3C};
static s16 half(u32 v){v&=65535u;return (s16)(v<32768u?(s32)v:(s32)v-65536);}
static u32 bits(f32 f){union{f32 f;u32 u;}v;v.f=f;return v.u;}
static void reference(u8 *matrix,f32 *destination){int i;
    for(i=0;i<3;i++){
        if(D_800C3E90){
            double numerator=(double)*(s16 *)(matrix+0x18+i*2)*65536.0+(double)*(s16 *)(matrix+0x38+i*2);
            destination[i]=(f32)(numerator/65536.0);
        }else{
            *(u32 *)&destination[i]=*(u32 *)(matrix+0x30+i*4);
        }
    }
}
'''
        self.run_host('''int n,a,i,mode,index,count=0;u8 *selected,*base;f32 *out,*expected;
if(sizeof(void *)!=4 || sizeof(s32)!=4 || sizeof(s16)!=2)return 1;
for(mode=0;mode<2;mode++)for(n=0;n<(mode?16:65536);n++)for(a=0;a<(mode?80:1);a++){
    index=mode?a/8:n%10;
    D_800C3E90=mode?0:(u8)(n%255+1);
    for(i=0;i<96;i++)actual.bytes[i]=0xA5;
    for(i=0;i<32;i++)output.bytes[i]=0xA5;
    selected=actual.bytes+16;
    for(i=0;i<3;i++){
        if(mode)*(u32 *)(selected+0x30+i*4)=floatWords[(n+i*5)%16];
        else{
            *(s16 *)(selected+0x18+i*2)=half((u32)n*(2*i+1));
            *(s16 *)(selected+0x38+i*2)=half((u32)n*(17+i*12)+3);
        }
    }
    for(i=0;i<96;i++)want.bytes[i]=actual.bytes[i];
    for(i=0;i<32;i++)wantOutput.bytes[i]=output.bytes[i];
    i=mode?a%8:n%8;
    out=(f32 *)(i?selected+aliases[i]:output.bytes+8);
    expected=(f32 *)(i?want.bytes+16+aliases[i]:wantOutput.bytes+8);
    base=(u8 *)((u32)selected-((u32)indices[index]<<6));
    reference(want.bytes+16,expected);
    func_15142314(base,indices[index],out);
    for(i=0;i<96;i++)if(actual.bytes[i]!=want.bytes[i])return 2;
    for(i=0;i<32;i++)if(output.bytes[i]!=wantOutput.bytes[i])return 3;
    count++;
}
if(count!=66816)return 4;
''')
        self.receipt('native', dict(cases=66816, bits=32, original_typed_signature=True,
            full_storage_checked=True, native_little_endian_alias_reference=True,
            reference='independent exact double numerator; bitwise float-mode copies'))

    def test_complete_original_parent_on_null_and_zero_routes_connects_both_translation_bodies(self):
        count = 0
        for flag, n, point_mode, phase, out in itertools.product((0, 1, 255), range(16), range(3),
                (0, 8), (OUTPUT, MATRIX + 0x18, STATUS, POINT)):
            memory, args = fixture(flag, edge_pairs(n), float_words(n), output=out)
            point = 0 if point_mode == 0 else POINT
            for axis in range(3):
                put(memory, POINT + axis * 4, 0x80000000 if point_mode == 2 else 0)
            expected = dict(memory)
            put(expected, STATUS, 7)
            expected, _ = reference(expected, args)
            put(expected, STATUS, 0)
            pair = []
            for words in (self.words, self.retail):
                connected = {screen.ENTRY + i * 4: word for i, word in enumerate(words)}
                model = ConnectedTranslationOracle(self.parent, memory, phase=phase, entry=PARENT,
                    arguments=(point, out, args[0]), connected=connected).run()
                self.assertEqual(external_memory(model.memory), external_memory(expected))
                self.assertEqual(model.calls, [(screen.ENTRY, args[0], 0, out)])
                pair.append(model)
            for attr in ('memory', 'events', 'calls'):
                self.assertEqual(getattr(pair[0], attr), getattr(pair[1], attr), attr)
            count += 1
        self.assertEqual(count, 1152)
        self.receipt('parent', dict(cases=count, complete_parent_execution=True,
            scope='null/positive-zero/negative-zero routes only', original_parent_words=98))

    def test_required_reads_fail_closed_and_unused_fields_are_not_read(self):
        for flag in (0, 1, 255):
            memory, args = fixture(flag)
            required = [screen.FLAG, OUTPUT]
            required += [MATRIX + offset + axis * (2 if flag else 4)
                for axis in range(3) for offset in ((0x18, 0x38) if flag else (0x30,))]
            for missing in required:
                broken = dict(memory)
                del broken[missing]
                for words in (self.words, self.retail):
                    with self.assertRaises((AssertionError, KeyError)):
                        self.model(words, broken, args)
            unused = MATRIX + (0x30 if flag else 0x18)
            del memory[unused]
            self.check_case(memory, args)

    def test_effective_compiled_negatives_expose_overflow_signed_low_alias_or_gate_errors(self):
        snapshot = screen.SELECTED.replace('    f32 scale', '    f32 values[3];\n    f32 scale')
        for axis in range(3):
            snapshot = snapshot.replace('        output[%d] =' % axis, '        values[%d] =' % axis, 1)
        marker = '    } else {\n'
        snapshot = snapshot.replace(marker, '        output[0] = values[0];\n        output[1] = values[1];\n        output[2] = values[2];\n' + marker, 1)
        forms = dict(legacy_integer_sum=LEGACY, unsigned_low=screen.SELECTED,
            wrong_stride=screen.SELECTED.replace('index << 6', 'index << 5'),
            flag_only_one=screen.SELECTED.replace('D_800C3E90 != 0', 'D_800C3E90 == 1'),
            wrong_scale=screen.SELECTED.replace('65536.0f', '32768.0f'),
            snapshot_inputs=snapshot, missing_z=screen.SELECTED.replace(
                '        output[2] = ((f32)(*(s16 *)(selected + 0x1C) * 65536) + (f32)*(s16 *)(selected + 0x3C)) * scale;\n', ''))
        for offset in (0x38, 0x3A, 0x3C):
            forms['unsigned_low'] = forms['unsigned_low'].replace('(s16 *)(selected + 0x%X)' % offset,
                '(u16 *)(selected + 0x%X)' % offset)
        detected = {}
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root, self.out, name, body)
            changes = storage_changes = 0
            for flag, n, index, alias in itertools.product((0, 1, 255), range(16), (0, 1), ALIASES):
                memory, args = fixture(flag, edge_pairs(n), float_words(n), index, alias)
                expected, events = reference(memory, args)
                model = self.model(words, memory, args)
                storage_changes += external_memory(model.memory) != external_memory(expected)
                changes += (external_memory(model.memory), public_events(model)) != (external_memory(expected), events)
            self.assertGreater(changes, 0, name)
            self.assertGreater(storage_changes, 0, name)
            if name == 'legacy_integer_sum':
                memory, args = fixture(1, ((-32768, -1),) * 3)
                expected, _ = reference(memory, args)
                legacy = self.model(words, memory, args)
                for axis in range(3):
                    self.assertEqual(read(expected, OUTPUT + axis * 4), 0xC7000000)
                    self.assertEqual(read(legacy.memory, OUTPUT + axis * 4), 0x47000000)
            detected[name] = dict(effects_or_traces=changes, public_storage=storage_changes)
        self.receipt('negatives', dict(count=7, detected=detected,
            legacy_is_compiled_guest_evidence_not_native_undefined_behavior=True))

    def test_complete_slot_and_all_152_source_controls_remain_nonmatching(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (49, 0, 34))
        self.assertEqual(self.record['pool_bytes'], 0)
        records = []
        forms = [(name + '-' + p, body, p, screen.DECLARATIONS, 'mips2')
            for name, body in screen.candidates() for p in screen.PROFILES]
        forms += [(name, body, 'o2g3', screen.DECLARATIONS, 'mips2')
            for name, body in [*screen.flow_candidates(), *screen.temporary_candidates()]]
        for isa, p, volatile in itertools.product(('mips1', 'mips2'), ('o2g3', 'o2'), range(4)):
            body, declaration = screen.SELECTED, screen.DECLARATIONS
            if volatile & 1:
                body = body.replace('f32 *output)', 'volatile f32 *output)')
            if volatile & 2:
                declaration = declaration.replace('extern u8 ', 'extern volatile u8 ')
            forms.append(('access%d-%s-%s' % (volatile, isa, p), body, p, declaration, isa))
        self.assertEqual(len(forms), 152)
        for name, body, profile, declaration, isa in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile, declaration, isa)
            self.assertEqual(record['diagnostics'], '', name)
            self.assertEqual(record['pool_bytes'], 0, name)
            self.assertGreater(record['differences'], 0, name)
            for flag, n, alias in itertools.product((0, 1, 255), range(4), (None, 0x18)):
                memory, args = fixture(flag, edge_pairs(n), float_words(n), alias=alias)
                expected, events = reference(memory, args)
                model = self.model(words, memory, args, n % 2 * 8)
                self.assertEqual(external_memory(model.memory), external_memory(expected), name)
                self.assertEqual([e for e in public_events(model) if e[0] == 'W'],
                    [e for e in events if e[0] == 'W'], name)
            records.append(record)
        self.receipt('controls', dict(measurements=records, count=152, exact=0,
            bounded_public_effect_qualification=3648, all_public_read_order_identity=False))

    def test_copied_owner_actual_padder_retains_complete_unguarded_body_and_flag_relocation(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        baseline = source.replace(screen.SELECTED, LEGACY)
        self.assertEqual(baseline.count(LEGACY), 1)
        objects, warnings = [], []
        for name, body in (('baseline', baseline), ('selected', baseline.replace(LEGACY, screen.SELECTED))):
            obj, diagnostic = compile_owner(self.root, self.out, body, 'owner-' + name)
            warnings.append(diagnostic)
            processed = self.out / ('owner-' + name + '-postprocessed.o')
            shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.out / ('owner-' + name + '.c')).relative_to(self.root / 'conker')), '--post-process',
                str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker', check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0], warnings[1])
        self.assertEqual(len(warnings[0]), 2)
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
        self.assertEqual(target['size'], 196)
        self.assertEqual(text[target['value']:target['value'] + 196], isolated[:196])
        assembly = emit_padded_assembly(objects[1], self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=self.root / 'conker/retail_word_patches.us.csv')
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        body = assembly[start:assembly.index('\n', end) + 1]
        self.assertEqual(len(re.findall(r'\.word 0x[0-9A-F]{8}', body)), 49)
        self.assertNotIn('__retail_overflow_' + screen.FUNCTION, assembly)
        source, obj, elf = (self.out / ('padded' + suffix) for suffix in ('.s', '.o', '.elf'))
        source.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + body)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(source)], check=True, capture_output=True)
        _, functions, rel = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'], 196)
        self.assertEqual(rel, self.record['relocations'])
        self.assertEqual({e for group in rel.values() for e in group},
            {('R_MIPS_HI16', 'D_800C3E90'), ('R_MIPS_LO16', 'D_800C3E90')})
        for delta in (0, 0x18000):
            flag = screen.FLAG + delta
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'translation.ld'),
                '-e', screen.FUNCTION, '--defsym=D_800C3E90=0x%X' % flag, '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = self.words.copy()
            for offset, entries in rel.items():
                for kind, _ in entries:
                    value = (flag + 0x8000) >> 16 if kind == 'R_MIPS_HI16' else flag
                    expected[offset // 4] = expected[offset // 4] & 0xFFFF0000 | value & 65535
            actual = list(struct.unpack_from('>49I', screen.sections(elf)['.text'][1]))
            self.assertEqual(actual, expected)
            if delta:
                self.assertNotEqual(actual, self.words)
        self.receipt('owner', dict(functions=89, neighbors=88, warnings=2,
            pools_unchanged=True, padded_words=49, relocated_flag=True, guards=0))

    def test_installed_source_complete_linked_slot_and_unchanged_guard_history(self):
        self.assertEqual((self.root / 'conker/src/game_16EE20.c').read_text().count(screen.SELECTED), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(functions[screen.FUNCTION], self.words)
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(sum(a != b for a, b in zip(functions[screen.FUNCTION], self.retail)), 34)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))


if __name__ == '__main__':
    unittest.main()
