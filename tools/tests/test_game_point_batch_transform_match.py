"""Record strides, physical matrix lifetime and lazy incoming-source reload."""

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

from tools.experiments import game_point_batch_transform_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_point_list_transform_audit as points
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read, external_memory
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly

ACTOR, SOURCE, OUTPUT, STACK = points.ACTOR, points.POINTS, points.RESULTS, points.STACK
ROTATE, TRANSFORM = screen.SYMBOLS.values()


def fixture(count=2, n=0, alias=0):
    memory, _ = points.fixture(count, n)
    destination = (OUTPUT, SOURCE, SOURCE + 12, SOURCE + 4)[alias]
    return memory, (ACTOR, SOURCE, destination, count & 0xFFFFFFFF)


def mutations(args, change):
    if not change:
        return ()
    return tuple((args[0] + 16 + axis * 2, value, 2) for axis, value in enumerate((-32768, -1, 32767))) + tuple(
        (SOURCE + 12 + axis * 4, points.bits(-axis - 4.0), 4) for axis in range(3))


def reference(memory, args, change=False, home=0, phase=0):
    memory = dict(memory)
    actor, source, output, count = args
    put(memory, STACK + phase + 4, source)
    put(memory, STACK + phase + 8, output)
    calls = [(ROTATE, tuple(read(memory, actor + i * 4) for i in range(3)))]
    matrix = STACK + phase - 0x98 + 0x58
    for i, value in enumerate(points.provider()):
        put(memory, matrix + i * 4, value)
    for address, value, size in mutations(args, change):
        put(memory, address, value, size)
    for bit in (1, 2):
        if home & bit:
            put(memory, STACK + phase + bit * 4, args[bit] + 12)
    output = read(memory, STACK + phase + 8)
    for i in range(3):
        value = points.bits(points.matrix.half(read(memory, actor + 16 + i * 2, 2)))
        put(memory, matrix + 48 + i * 4, value)
    if points.signed(count) > 0:
        source = read(memory, STACK + phase + 4)
    for i in range(max(0, points.signed(count))):
        values = tuple(read(memory, matrix + j * 4) for j in range(16))
        coordinates = tuple(read(memory, source + i * 12 + axis * 4) for axis in range(3))
        outputs = tuple(output + i * 12 + axis * 4 for axis in range(3))
        calls.append((TRANSFORM, values, coordinates, outputs))
        for address, value in zip(outputs, points.transformed(values, coordinates)):
            put(memory, address, value)
    return memory, calls


class PointBatchOracle(TriangleOracle):
    record_call = points.PointListOracle.record_call

    def __init__(self, words, memory, args, change=False, phase=0, connected=None, home=0, drop_home=0):
        super().__init__(words, memory, entry=screen.ENTRY, arguments=args, phase=phase, connected=connected)
        self.args, self.change, self.phase, self.home, self.drop_home = args, change, phase, home, drop_home

    def hook(self, target):
        if target == ROTATE:
            for i, value in enumerate(points.provider()):
                self.put(self.matrix + i * 4, value, 4)
            for address, value, size in mutations(self.args, self.change):
                self.put(address, value, size)
            for bit in (1, 2):
                address = STACK + self.phase + bit * 4
                if self.home & bit:
                    self.put(address, self.args[bit] + 12, 4)
                if self.drop_home & bit:
                    for i in range(4):
                        del self.memory[address + i]
        else:
            assert target == TRANSFORM
            _, values, coordinates, outputs = self.calls[-1]
            for address, value in zip(outputs, points.transformed(values, coordinates)):
                self.put(address, value, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]


class GamePointBatchTransformMatchTests(unittest.TestCase):
    run_host = points.GamePointListTransformAuditTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-point-batch-transform-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected', screen.SELECTED)
        cls.retail = list(struct.unpack_from('>60I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.normalized = screen.normalize(cls.words)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        helper = struct.unpack_from('>40I', (cls.root / 'conker/conker.us.bin').read_bytes(), 0xD4E10)
        cls.connected = dict(zip(range(TRANSFORM, TRANSFORM + 160, 4), helper))

    def receipt(self, name, data):
        (self.out / (name + '.json')).write_text(json.dumps(data, indent=2) + '\n')

    def model(self, words, memory, args, **kwargs):
        return PointBatchOracle(words, memory, args, **kwargs).run()

    def check_case(self, memory, args, **kwargs):
        expected, calls = reference(memory, args, kwargs.get('change', False), kwargs.get('home', 0), kwargs.get('phase', 0))
        models = [self.model(words, memory, args, **kwargs) for words in (self.words, self.normalized, self.retail)]
        for model in models:
            self.assertEqual(external_memory(model.memory), external_memory(expected))
            self.assertEqual(model.calls, calls)
        public = lambda model: [event for event in model.events if not STACK - 0x600 <= event[1] < STACK + 0x140]
        for model in models[:2]:
            self.assertEqual(public(model), public(models[2]))
            self.assertEqual(model.memory, models[2].memory)
        return models

    def test_complete_closed_register_cycles_save_store_permutation_and_guard_words(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (60, 0x98, 17))
        self.assertEqual((self.record['pool_bytes'], self.record['diagnostics'], self.record['extra_flags']), (0, '', []))
        self.assertEqual(self.normalized, self.retail)
        self.assertEqual(self.words[:2], self.retail[:2])
        self.assertEqual(self.words[51:], self.retail[51:])
        self.assertEqual({self.words[i] for i in (2, 8, 9)}, {self.retail[i] for i in (2, 8, 9)})
        for i in (6, 11, 12, 19, 24, 29, 36):
            self.assertEqual(self.words[i], self.retail[i], ('private pointer, home, store or lazy source reload', i))
        raw, functions, rel = parse_object(self.out / 'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['size'], 240)
        self.assertEqual(rel, {0x40: [('R_MIPS_26', 'func_150A8050')], 0xAC: [('R_MIPS_26', 'func_150A7960')]})
        rows = screen.owner_guards()
        changes = [i * 4 for i, (a, b) in enumerate(zip(self.words, self.retail)) if a != b]
        self.assertEqual(changes, [int(row['offset'], 16) for row in rows])
        applied = self.words.copy()
        for row in rows:
            offset = int(row['offset'], 16)
            self.assertEqual(struct.unpack_from('>I', raw, offset)[0], int(row['expected'], 16))
            self.assertEqual((row['expected_relocations'], row['replacement_relocations']), ('-', '-'))
            self.assertEqual((row['insert_after'], row['omit']), ('', 'false'))
            self.assertNotIn(offset, rel)
            if offset not in (8, 0x20, 0x24):
                mask = 0x7FF if self.words[offset // 4] >> 26 == 0 else 0xFFFF
                self.assertEqual(self.words[offset // 4] & mask, int(row['replacement'], 16) & mask)
            applied[offset // 4] = int(row['replacement'], 16)
        self.assertEqual(applied, self.retail)
        self.receipt('cycles', dict(words=60, frame=152, raw_differences=17, normalized_differences=0,
            saved_cycle=[18, 19, 20], halfword_cycles=[[2, 15], [3, 24]], independent_stores=[2, 8, 9],
            private_offsets_or_FP_register_changes=0, insertions=0, omissions=0, untouched_call_relocations=2))

    def test_complete_guest_aliases_calls_and_connected_original_point_helper(self):
        coverage, helper_coverage = set(), set()
        for count, n, alias, change, phase in itertools.product(points.COUNTS, range(16), range(4), (False, True), (0, 8)):
            memory, args = fixture(count, n, alias)
            for model in self.check_case(memory, args, change=change, phase=phase):
                coverage.update(model.visits)
        self.assertEqual(coverage, set(range(screen.ENTRY, screen.ENTRY + 240, 4)))
        for count, n, alias, change, phase in itertools.product((1, 2, 4), range(16), range(4), (False, True), (0, 8)):
            memory, args = fixture(count, n, alias)
            for model in self.check_case(memory, args, change=change, phase=phase, connected=self.connected):
                helper_coverage.update(model.visits & self.connected.keys())
        self.assertEqual(helper_coverage, set(self.connected))
        self.receipt('effects', dict(guest=1792, connected=768, all_wrapper_and_helper_words=True,
            full_memory_public_traces_calls_saved_state=True, aliases=['separate', 'in-place', 'future-record', 'partial-record'],
            rotation_provider_bounded=True, no_general_FCSR_or_hardware_claim=True))

    def test_each_incoming_record_home_and_both_independently_at_both_stack_phases(self):
        for count, mask, n, alias, change, phase in itertools.product(points.COUNTS, (1, 2, 3), range(16), range(4), (False, True), (0, 8)):
            memory, args = fixture(count, n, alias)
            self.check_case(memory, args, home=mask, change=change, phase=phase, connected=self.connected)
        self.receipt('homes', dict(cases=5376, each_source_destination_and_both=True,
            raw_normalized_original_full_memory_identity=True, nonstandard_guest_ABI_not_native_C_permission=True))

    def test_required_storage_and_lazy_source_home_gate_fail_closed(self):
        removed = 0
        for count in (0, 2):
            required = [(ACTOR + offset, size) for offset, size in ((0, 4), (4, 4), (8, 4), (16, 2), (18, 2), (20, 2))]
            if count:
                required += [(base + axis * 4, 4) for base in (SOURCE, OUTPUT) for axis in range(3)]
            for address, size in required:
                memory, args = fixture(count)
                for byte in range(size):
                    del memory[address + byte]
                for words in (self.words, self.normalized, self.retail):
                    with self.assertRaises((AssertionError, KeyError)):
                        self.model(words, memory, args, connected=self.connected)
                removed += 1
        for count, drop, phase in itertools.product(points.COUNTS, (1, 2), (0, 8)):
            memory, args = fixture(count)
            if drop == 1 and count <= 0:
                self.check_case(memory, args, phase=phase, drop_home=drop, connected=self.connected)
            else:
                for words in (self.words, self.normalized, self.retail):
                    with self.assertRaises((AssertionError, KeyError)):
                        self.model(words, memory, args, phase=phase, drop_home=drop, connected=self.connected)
        for count in points.COUNTS[:4]:
            memory, args = fixture(count)
            for address in list(memory):
                if SOURCE - 16 <= address < points.ALTERNATE + 272:
                    del memory[address]
            self.check_case(memory, args, connected=self.connected)
        eager = dict(screen.storage_candidates())['storage-mask2-first0']
        _, eager_words = screen.compile_candidate(self.root, self.out, 'negative-eager-home', eager)
        memory, args = fixture(0)
        with self.assertRaises((AssertionError, KeyError)):
            self.model(eager_words, memory, args, drop_home=1)
        self.receipt('unmapped', dict(required_cases=removed, removed_home_cases=28, unused_record_cases=4,
            destination_home_always_required=True, source_home_only_positive=True, eager_home_negative_detected=True))

    def test_original_matrix_offset_with_descriptor_private_overlap_and_legacy_counterexamples(self):
        count, legacy_different, faults, legacy_missing_faults = 0, 0, 0, 0
        _, legacy = screen.compile_candidate(self.root, self.out, 'legacy-private', screen.BASELINE)
        for n, offset, remaining, change, phase in itertools.product(range(8), (0, 16, 32, 36, 40, 48), (0, 2), (False, True), (0, 8)):
            memory, args = fixture(remaining, n)
            descriptor = STACK + phase - 0x98 + 0x58 + offset
            for i in range(24):
                memory[descriptor + i] = memory[ACTOR + i]
            args = (descriptor, *args[1:])
            try:
                expected, _ = reference(memory, args, change, phase=phase)
            except KeyError:
                self.assertEqual((offset, remaining, change), (48, 2, True))
                for words in (self.words, self.normalized, self.retail):
                    with self.assertRaises((AssertionError, KeyError)):
                        self.model(words, memory, args, change=change, phase=phase, connected=self.connected)
                self.model(legacy, memory, args, change=change, phase=phase, connected=self.connected)
                faults += 1
                legacy_missing_faults += 1
                count += 1
                continue
            self.check_case(memory, args, change=change, phase=phase, connected=self.connected)
            old = self.model(legacy, memory, args, change=change, phase=phase, connected=self.connected)
            legacy_different += external_memory(old.memory) != external_memory(expected)
            count += 1
        self.assertGreater(legacy_different, 0)
        self.assertEqual(faults, 16)
        self.receipt('private', dict(cases=count, valid_cases=count-faults, fault_cases=faults,
            legacy_public_storage_counterexamples=legacy_different, legacy_missing_fault_cases=legacy_missing_faults,
            matrix_offset=88, actual_original_helper=True, full_memory_identity=True))

    def test_actual_native_32bit_all_translation_halfwords_provider_mutations_and_record_aliases(self):
        self.fixture = r'''typedef unsigned char u8;typedef short s16;typedef unsigned short u16;
typedef unsigned int u32;typedef int s32;typedef float f32;
typedef struct {f32 unk0,unk4,unk8;} struct17;
typedef union {u8 bytes[32];s16 halves[16];f32 words[8];} Descriptor;
typedef union {struct17 records[8];f32 words[24];} Records;
static Descriptor descriptor,expectedDescriptor;
static Records inputStore,outputStore;
static f32 expectedInput[24],expectedOutput[24];
static int mode,change,error,rotations,transforms;
static struct17 *destination;
static u32 word(f32 value){union {f32 f;u32 u;} v;v.f=value;return v.u;}
void func_150A8050(f32 matrix[4][4],f32 x,f32 y,f32 z){
    int i;rotations++;
    if(word(x)!=word(1.0f)||word(y)!=word(2.0f)||word(z)!=word(3.0f))error=1;
    for(i=0;i<16;i++)((f32 *)matrix)[i]=(f32)(i+1)*0.25f;
    if(change){
        descriptor.halves[8]=-32768;descriptor.halves[9]=-1;descriptor.halves[10]=32767;
        for(i=0;i<3;i++)inputStore.words[3+i]=(f32)(-i-4);
    }
}
void func_150A7960(f32 matrix[4][4],f32 x,f32 y,f32 z,f32 *outX,f32 *outY,f32 *outZ){
    int i,index=transforms*3,base=mode==2?3:mode==3?1:0;
    f32 values[3],*expected=mode?expectedInput:expectedOutput;
    f32 *actual=(f32 *)destination;
    for(i=0;i<16;i++){
        f32 wanted=i>=12&&i<=14?(f32)expectedDescriptor.halves[8+i-12]:(f32)(i+1)*0.25f;
        if(word(((f32 *)matrix)[i])!=word(wanted))error=2;
    }
    for(i=0;i<3;i++)values[i]=expectedInput[index+i];
    if(word(x)!=word(values[0])||word(y)!=word(values[1])||word(z)!=word(values[2]))error=3;
    if(outX!=actual+index||outY!=actual+index+1||outZ!=actual+index+2)error=4;
    for(i=0;i<3;i++)expected[base+index+i]=values[i];
    *outX=x;*outY=y;*outZ=z;transforms++;
}
static void initialize(u32 n,int alias,int mutation){
    int i;mode=alias;change=mutation;error=rotations=transforms=0;
    for(i=0;i<32;i++)descriptor.bytes[i]=0xA5;
    descriptor.words[0]=1.0f;descriptor.words[1]=2.0f;descriptor.words[2]=3.0f;
    for(i=0;i<3;i++)descriptor.halves[8+i]=(s16)(n*(u32)(2*i+1)+(u32)(i*13));
    for(i=0;i<32;i++)expectedDescriptor.bytes[i]=descriptor.bytes[i];
    for(i=0;i<24;i++){
        inputStore.words[i]=(f32)(i+1)*0.25f;outputStore.words[i]=-123.0f;
        expectedInput[i]=inputStore.words[i];expectedOutput[i]=outputStore.words[i];
    }
    destination=alias==0?outputStore.records:alias==1?inputStore.records:
        alias==2?inputStore.records+1:(struct17 *)(inputStore.words+1);
    if(change){
        expectedDescriptor.halves[8]=-32768;expectedDescriptor.halves[9]=-1;expectedDescriptor.halves[10]=32767;
        for(i=0;i<3;i++)expectedInput[3+i]=(f32)(-i-4);
    }
}
static int check(int count){
    int i;if(error||rotations!=1||transforms!=count)return 1;
    for(i=0;i<24;i++)if(word(inputStore.words[i])!=word(expectedInput[i])
        ||word(outputStore.words[i])!=word(expectedOutput[i]))return 2;
    for(i=0;i<32;i++)if(descriptor.bytes[i]!=expectedDescriptor.bytes[i])return 3;
    return 0;
}
''' + screen.SELECTED + '\n'
        self.run_host(r'''
u32 n;int alias,mutation,i;static s32 counts[]={(-2147483647-1),-3,-1,0};
for(n=0;n<65536;n++)for(alias=0;alias<4;alias++)for(mutation=0;mutation<2;mutation++){
    initialize(n,alias,mutation);
    func_15145DB4(descriptor.bytes,inputStore.records,destination,4);
    if(check(4))return 1;
}
for(i=0;i<4;i++)for(mutation=0;mutation<2;mutation++){
    initialize(7,0,mutation);
    func_15145DB4(descriptor.bytes,(struct17 *)0,destination,counts[i]);
    if(check(0))return 2;
}
''')
        self.receipt('native', dict(cases=524296, actual_32bit_C=True, every_halfword_each_translation_field=True,
            four_record_aliases=True, provider_mutations=True, all_records_and_descriptor_fences=True,
            nonpositive_null_source_cases=8, validating_copy_helper_not_full_SDK_or_64bit_host=True))

    def test_119_meaningful_controls_and_seven_public_storage_changing_negatives(self):
        forms = [(name, body, 'o2g3', ()) for name, body in screen.candidates()]
        forms += [(name, body, 'o2g3', ()) for name, body in screen.storage_candidates()]
        base = dict(screen.candidates())['phase1-early1-loop1-arrays0']
        forms += [('profile-' + profile, base, profile, ()) for profile in screen.PROFILES]
        forms += [('backend-' + flag, base, 'o2g3', ('-Wab,-' + flag,)) for flag in
            ('no_branch_target', 'noxbb', 'nobopt', 'noglobal', 'nopeep', 'noswpipe', 'O0', 'O1')]
        forms += [('backend-' + flag, base, 'o2g3', ('-Wc,-' + flag,)) for flag in ('notailopt', 'nooffsetopt')]
        forms += [(name, body, 'o2g3', ()) for name, body in screen.reload_candidates()]
        forms += [('reload-backend-noxbb', dict(screen.storage_candidates())['storage-mask2-first0'], 'o2g3', ('-Wab,-noxbb',))]
        forms += [(name, body, 'o2g3', ()) for name, body in screen.gate_candidates()]
        self.assertEqual(len(forms), 119)
        records = []
        for name, body, profile, flags in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile, flags)
            self.assertEqual(record['pool_bytes'], 0)
            self.assertGreater(record['differences'], 0)
            for count, alias, change in itertools.product((-1, 0, 2), range(4), (False, True)):
                memory, args = fixture(count, 7, alias)
                expected, calls = reference(memory, args, change)
                model = self.model(words, memory, args, change=change)
                self.assertEqual((external_memory(model.memory), model.calls), (external_memory(expected), calls), name)
            records.append(record)
        block = screen.SELECTED[screen.SELECTED.index('    matrix[3][0]'):screen.SELECTED.index('\n\n    /* Keep')]
        negatives = dict(unsigned_translation=screen.SELECTED.replace('*(s16 *)', '*(u16 *)'),
            exact_one_gate=screen.SELECTED.replace('count > 0) goto', 'count == 1) goto'),
            wrong_source_stride=screen.SELECTED.replace('cursor += 12;', 'cursor += 8;'),
            wrong_destination_stride=screen.SELECTED.replace('x += 3;', 'x += 1;'),
            stale_source=screen.SELECTED.replace('        cursor += 12;\n', ''),
            translation_before_provider=screen.SELECTED.replace(block, '').replace('    func_150A8050(', block + '\n    func_150A8050(', 1),
            legacy_saved_arguments=screen.BASELINE)
        detected = {}
        for name, body in negatives.items():
            _, words = screen.compile_candidate(self.root, self.out, 'negative-' + name, body)
            changed = 0
            for n, alias, change in itertools.product(range(4), range(4), (False, True)):
                memory, args = fixture(2, n, alias)
                expected, _ = reference(memory, args, change, home=3)
                model = self.model(words, memory, args, change=change, home=3)
                changed += external_memory(model.memory) != external_memory(expected)
            self.assertGreater(changed, 0, name)
            detected[name] = changed
        self.receipt('controls', dict(measurements=records, count=119, ordinary_candidate_executions=2856,
            negatives=detected, every_negative_changes_public_storage=True, raw_exact=0))

    def test_copied_owner_actual_padder_and_both_independently_rebased_calls(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        baseline = source.replace(screen.SELECTED, screen.BASELINE)
        self.assertEqual(baseline.count(screen.BASELINE), 1)
        objects, warnings = [], []
        for name, body in (('baseline', baseline), ('selected', baseline.replace(screen.BASELINE, screen.SELECTED))):
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
            self.assertEqual(text[current['value']:current['value'] + current['size']], old_text[old['value']:old['value'] + old['size']], name)
            self.assertEqual({o - current['value']: r for o, r in rel.items() if current['value'] <= o < current['value'] + current['size']},
                {o - old['value']: r for o, r in old_rel.items() if old['value'] <= o < old['value'] + old['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        target = functions[screen.FUNCTION]
        isolated = parse_object(self.out / 'selected.o')[0]
        self.assertEqual(target['size'], 240)
        self.assertEqual(text[target['value']:target['value'] + 240], isolated[:240])
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        additions = screen.owner_guards()
        path = self.root / 'conker/retail_word_patches.us.csv'
        if not any(row['function'] == screen.FUNCTION for row in guards):
            path = self.out / 'proposed-guards.csv'
            with path.open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=list(guards[0]), lineterminator='\n')
                writer.writeheader(); writer.writerows([*guards, *additions])
        else:
            self.assertEqual([row for row in guards if row['function'] == screen.FUNCTION], additions)
        assembly = emit_padded_assembly(objects[1], self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=path)
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        body = assembly[start:assembly.index('\n', end) + 1]
        self.assertEqual(len(re.findall(r'\.word 0x[0-9A-F]{8}', body)), 60)
        self.assertNotIn('__retail_overflow_' + screen.FUNCTION, assembly)
        padded_source, obj, elf = (self.out / ('padded' + suffix) for suffix in ('.s', '.o', '.elf'))
        padded_source.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + body)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(padded_source)], check=True, capture_output=True)
        _, symbols, mapped = parse_object(obj)
        self.assertEqual(symbols[screen.FUNCTION]['size'], 240)
        self.assertEqual(mapped, self.record['relocations'])
        for changed in (None, *screen.SYMBOLS):
            targets = {name: address + (0x1000000 if name == changed else 0) for name, address in screen.SYMBOLS.items()}
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'point-batch.ld'), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X' % item for item in targets.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = self.retail.copy()
            for offset, entries in mapped.items():
                self.assertEqual(len(entries), 1)
                kind, name = entries[0]
                self.assertEqual(kind, 'R_MIPS_26')
                expected[offset // 4] = 0x0C000000 | (targets[name] >> 2 & 0x3FFFFFF)
            self.assertEqual(list(struct.unpack_from('>60I', screen.sections(elf)['.text'][1])), expected)
        self.receipt('owner', dict(functions=89, neighbors=88, warnings=2, padded_words=60,
            guards=17, raw_owner_equals_isolated=True, pools_unchanged=True, independent_call_rebases=2))

    def test_installed_source_complete_byte_exact_slot_and_guard_history(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertEqual(source.count(screen.SELECTED), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertEqual(guards[11025:], screen.owner_guards())


if __name__ == '__main__':
    unittest.main()
