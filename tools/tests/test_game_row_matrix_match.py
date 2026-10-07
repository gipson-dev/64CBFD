"""Row-scaled rotation matrix, live parameter homes and complete caller ABI."""

import csv
import hashlib
import itertools
import json
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_row_matrix_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_random_curve_record as native
from tools.tests import test_game_scaled_matrix_match as scaled
from tools.tests.test_game_timed_interpolation_match import rounded_bits
from tools.tests.test_game_grid_channel_updater_match import STACK, external, put
from tools.tests.game_animation_timeline_oracle import bits, floating

ROTATE, CONVERT, CALLER = 0x150A8050, 0x150A7790, 0x15133760
ACTOR, OUTPUT, ALTERNATE = 0x20000, 0x24000, 0x26000
OFFSETS = (0x18, 0x1C, 0x20, 0x24, 0x28, 0x38, 0x3C, 0x40)


def arguments(row0=1, row1=2, translation=0, alias=0):
    return ((OUTPUT, ACTOR + 0x18, ACTOR + 0x20)[alias],
        *map(bits, (row0, row1, 0.125, -0.25, 0.5, *scaled.TRANSLATIONS[translation])))


def memory_case(args):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x100)}
    for base in (ACTOR, OUTPUT, ALTERNATE):
        memory.update({base + i: (i * 31 + 7) & 255 for i in range(-16, 256)})
    for offset, value in zip(OFFSETS, args[1:]):
        put(memory, ACTOR + offset, value)
    return memory


def mutation_actions(args, enabled):
    return tuple((ACTOR + offset, 0xA5000000 + offset) for offset in OFFSETS) + ((args[0] + 8, 0x12345678),) if enabled else ()


def result_matrix(args, pattern):
    values = list(scaled.provider(pattern))
    for row in range(3):
        for column in range(3):
            index = row * 4 + column
            values[index] = rounded_bits(floating(values[index]) * floating(args[2 if row == 1 else 1]))
    values[12:15] = args[6:9]
    return tuple(values)


def reference(memory, args, pattern=0, mutation=False, home=None, fixed=False):
    memory = dict(memory)
    calls = [(ROTATE, args[3:6], external(memory))]
    for address, value in mutation_actions(args, mutation):
        put(memory, address, value)
    updated = list(args)
    if home is not None and home[0] not in (3, 4, 5):
        updated[home[0]] = home[1]
    values = result_matrix(updated, pattern)
    calls.append((CONVERT, values, updated[0], external(memory)))
    payload = scaled.fixed_payload(values) if fixed else struct.pack('>16I', *values)
    for i, value in enumerate(payload):
        memory[updated[0] + i] = value
    return external(memory), calls


class RowMatrixOracle(scaled.MatrixOracle):
    def __init__(self, words, memory, args, pattern=0, mutation=False, phase=0, home=None, connected=None):
        super().__init__(words, memory, args, pattern, mutation, phase, home, connected)
        self.entry = screen.ENTRY
        self.code = {screen.ENTRY + i * 4: word for i, word in enumerate(words)}
        self.code.update(connected or {})

    def record_call(self, target):
        if target == screen.ENTRY:
            self.forwarded = self.arguments(9)
        else:
            super().record_call(target)

    def hook(self, target):
        if target == ROTATE:
            for i, value in enumerate(scaled.provider(self.pattern)):
                self.put(self.matrix + i * 4, value, 4)
            for address, value in mutation_actions(self.args, self.change):
                self.put(address, value, 4)
            if self.home is not None:
                self.put(STACK + self.phase + self.home[0] * 4, self.home[1], 4)
            for register in (1, 2, 3, *range(4, 16), 24, 25):
                self.r[register] = 0xA5000000 + register
            self.f[:20] = [0xA5000000 + i for i in range(20)]
        else:
            super().hook(target)


def native_fixture():
    fixture = scaled.native_fixture()
    fixture = fixture.replace(scaled.screen.SELECTED, screen.SELECTED).replace(scaled.screen.CALLER, screen.CALLER)
    fixture = fixture.replace('input[11]', 'input[8]')
    fixture = fixture.replace('static int pattern,change,stage,error;',
        'static int pattern,change,stage,error;\nstatic int offsets[8]={0x18,0x1C,0x20,0x24,0x28,0x38,0x3C,0x40};')
    fixture = fixture.replace('for(i=0;i<11;i++) *(u32 *)(bank->bytes+40+i*4)=0xA5000000u+i;',
        'for(i=0;i<8;i++) *(u32 *)(bank->bytes+16+offsets[i])=0xA5000000u+offsets[i];')
    fixture = fixture.replace('for(i=0;i<11;i++) *(u32 *)(source+0x18+i*4)=input[i];',
        'for(i=0;i<8;i++) *(u32 *)(source+offsets[i])=input[i];')
    fixture = fixture.replace('volatile f32 factor=number(input[5+i%4])*number(input[i/4==1?1:0]);',
        'volatile f32 factor=number(input[i/4==1?1:0]);')
    fixture = fixture.replace('expected[12+i]=input[8+i];', 'expected[12+i]=input[5+i];')
    assert 'input[11]' not in fixture and scaled.screen.FUNCTION not in fixture
    return fixture


class GameRowMatrixMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-row-matrix-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>55I', cls.rom, screen.ROM))
        cls.caller = list(struct.unpack_from('>24I', cls.rom, 0x160C10))
        cls.converter = list(struct.unpack_from('>115I', cls.rom, 0xD4C40))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = native_fixture()

    def receipt(self, name, value):
        (self.output / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def compare(self, args, pattern=0, mutation=False, phase=0, home=None, caller=False, fixed=False):
        memory = memory_case(args)
        wanted, calls = reference(memory, args, pattern, mutation, home, fixed)
        connected = {}
        if caller:
            connected.update({CALLER + i * 4: word for i, word in enumerate(self.caller)})
        if fixed:
            connected.update({CONVERT + i * 4: word for i, word in enumerate(self.converter)})
        models = []
        for words in (self.words, self.retail):
            model = RowMatrixOracle(words, memory, args, pattern, mutation, phase, home, connected)
            if caller:
                model.entry = CALLER
                model.r[4:8] = model.before[4:8] = [args[0], ACTOR, 0, 0]
            model.run()
            self.assertEqual(external(model.memory), wanted)
            self.assertEqual(model.calls, calls)
            if caller:
                self.assertEqual(model.forwarded, args)
                self.assertEqual(model.r[2], 1)
            models.append(model)
        self.assertEqual(models[0].events, models[1].events)
        self.assertEqual(models[0].memory, models[1].memory)
        return models

    def test_sixteen_controls_and_complete_direct_slot_frame(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (55, 0x58, 0))
        self.assertEqual(self.words, self.retail)
        controls = []
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                record, _ = screen.compile_candidate(self.root, self.output, name + '-' + profile, body, profile)
                controls.append(record)
        self.assertEqual(len(controls), 16)
        self.assertEqual(sum(r['differences'] == 0 for r in controls), 1)
        self.assertTrue(all(not r['diagnostics'] for r in controls))
        self.receipt('controls', controls)

    def test_guest_scaling_translations_provider_mutations_aliases_and_saved_state(self):
        count = 0
        coverage = [set(), set()]
        for row0, row1, translation, pattern, alias, mutation, phase in itertools.product(
                scaled.ROWS0, scaled.ROWS1, range(3), range(3), range(3), (False, True), (0, 8)):
            for index, model in enumerate(self.compare(arguments(row0, row1, translation, alias), pattern, mutation, phase)):
                coverage[index].update(model.visits)
            count += 1
        self.assertEqual(count, 2160)
        self.assertEqual([len(c) for c in coverage], [55, 55])
        self.receipt('guest', dict(cases=count, bodies=2, covered_words=[55, 55], full_traces=True, full_memory=True, helpers='bounded rotation/payload models'))

    def test_guest_every_float_input_signed_zero_subnormal_overflow_inf_and_nan(self):
        count = 0
        for index, value, phase in itertools.product(range(1, 9), scaled.PATTERNS, (0, 8)):
            args = list(arguments(alias=index % 3))
            args[index] = value
            self.compare(tuple(args), index % 3, True, phase)
            count += 1
        self.assertEqual(count, 192)
        self.receipt('edges', dict(cases=count, all_eight_float_inputs=True, hardware_fcsr=False, native_nan_payload=False))

    def test_guest_live_parameter_homes_after_rotation(self):
        count = 0
        for index, phase, value in itertools.product(range(9), (0, 8), (bits(-0.5), bits(3))):
            home = (index, ALTERNATE if index == 0 else value)
            self.compare(arguments(), 1, True, phase, home)
            count += 1
        self.assertEqual(count, 36)
        self.receipt('homes', dict(cases=count, output_rows_translations_live=True, rotation_already_captured=True, native_private_home_claim=False))

    def test_complete_original_caller_and_converter_in_finite_exact_domain(self):
        count = 0
        coverage = [set(), set()]
        for row0, row1, translation, pattern, alias, mutation, phase in itertools.product(
                (0.5, -2), (0.25, 2), range(3), range(2), range(3), (False, True), (0, 8)):
            for index, model in enumerate(self.compare(arguments(row0, row1, translation, alias), pattern, mutation, phase, caller=True, fixed=True)):
                coverage[index].update(model.visits)
            count += 1
        expected = set(range(CALLER, CALLER + 96, 4)) | set(range(CONVERT, CONVERT + 460, 4)) | set(range(screen.ENTRY, screen.ENTRY + 220, 4))
        self.assertEqual(coverage, [expected, expected])
        self.assertEqual(count, 288)
        self.receipt('connected', dict(cases=count, caller_words=24, builder_words=55, converter_words=115, all_words=True, conversion='finite exact integral signed32 after scaling', rotation='bounded provider', hardware_fcsr=False))

    def test_actual_32_bit_native_caller_fields_aliases_and_special_float_bits(self):
        self.run_host(r'''
static f32 row0[]={0,-0.0f,0.5f,1,-2},row1[]={0,0.25f,2,-3};
static f32 translations[3][3]={{7,-9,11},{-0.0f,2.5f,-3.5f},{0,0,0}};
static u32 patterns[]={0,0x80000000u,1,0x80000001u,0x007FFFFF,0x00800000,
    0x7F7FFFFF,0xFF7FFFFFu,0x7F800000,0xFF800000u,0x7FC12345,0x7F812345};
int a,b,c,d,e,f,i,j,count=0;
for(a=0;a<5;a++)for(b=0;b<4;b++)for(c=0;c<3;c++)for(d=0;d<3;d++)for(e=0;e<3;e++)for(f=0;f<2;f++) {
    input[0]=word(row0[a]);input[1]=word(row1[b]);input[2]=word(0.125f);
    input[3]=word(-0.25f);input[4]=word(0.5f);
    for(i=0;i<3;i++)input[5+i]=word(translations[c][i]);
    initialize(d,f,e);
    if(func_15133760((u8 *)output,source)!=1 || check())return 20+error;
    count++;
}
if(count!=1080 || sizeof(Mtx)!=64 || sizeof(f32)!=4)return 30;
for(i=0;i<8;i++)for(j=0;j<12;j++) {
    for(a=0;a<8;a++)input[a]=word((a+1)*0.25f);
    input[i]=patterns[j];initialize(i%3,1,i%3);
    if(func_15133760((u8 *)output,source)!=1 || check())return 31+error;
    count++;
}
if(count!=1176)return 40;
''')
        self.receipt('native', dict(cases=1176, bits=32, actual_source=True, caller=True, external_storage=True, arithmetic_nan_classification=True, helpers='bounded rotation/payload models'))

    def test_actual_padder_preserves_extent_and_retargets_both_calls(self):
        text, functions, relocations = parse_object(self.output / 'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['size'], 220)
        self.assertEqual(text[220:224], bytes(4))
        self.assertEqual(relocations, {0x2C: [('R_MIPS_26', 'func_150A8050')], 0xC4: [('R_MIPS_26', 'guMtxF2L')]})
        layout = self.output / 'layout.csv'
        layout.write_text('version,section,filename,function,address,end\n'
            'us,game,game_16EE20,func_15142838,0x15142838,0x15142914\n')
        assembly = self.output / 'padded.s'
        assembly.write_text(scaled.emit_padded_assembly(self.output / 'selected.o', layout, 'game_16EE20'))
        obj = self.output / 'padded.o'
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(assembly)], check=True, capture_output=True)
        padded, symbols, mapped = parse_object(obj)
        self.assertEqual(symbols[screen.FUNCTION]['size'], 220)
        self.assertEqual(padded[:220], text[:220])
        self.assertEqual(mapped, relocations)
        for alternate in (False, True):
            targets = {name: address + (0x1000000 if alternate else 0) for name, address in screen.SYMBOLS.items()}
            elf = self.output / ('padded-%d.elf' % alternate)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output / 'row-matrix.ld'), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X' % item for item in targets.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
            words = list(struct.unpack_from('>55I', screen.sections(elf)['.text'][1]))
            expected = list(self.retail)
            for offset, name in ((0x2C, 'func_150A8050'), (0xC4, 'guMtxF2L')):
                expected[offset // 4] = 0x0C000000 | (targets[name] >> 2 & 0x3FFFFFF)
            self.assertEqual(words, expected)
        self.receipt('padding', dict(bytes=220, section_alignment_tail=4, guards=0, retargeted_calls=2))

    def test_missing_caller_source_provider_matrix_or_output_fails_strict_memory(self):
        args = arguments()
        for address, caller in ((ACTOR + 0x18, True), (ACTOR + 0x40, True), (OUTPUT, False), (STACK - 0x40, False)):
            memory = memory_case(args)
            del memory[address]
            connected = {CALLER + i * 4: word for i, word in enumerate(self.caller)} if caller else {}
            model = RowMatrixOracle(self.words, memory, args, connected=connected)
            if caller:
                model.entry = CALLER
                model.r[4:8] = model.before[4:8] = [OUTPUT, ACTOR, 0, 0]
            with self.assertRaisesRegex(AssertionError, 'unmapped'):
                model.run()

    def test_compiled_negatives_change_known_fields_or_call_sequence(self):
        translations = '    matrix[3][0] = tx;\n    matrix[3][1] = ty;\n    matrix[3][2] = tz;\n'
        forms = {'placeholder': screen.PROTOTYPE[:-1] + ' { }',
            'missing-provider': screen.SELECTED.replace('    func_150A8050(matrix, rx, ry, rz);', ''),
            'missing-converter': screen.SELECTED.replace('    guMtxF2L(matrix, output);', ''),
            'wrong-row': screen.SELECTED.replace('matrix[0][1] *= row0', 'matrix[0][1] *= row1'),
            'wrong-translation': screen.SELECTED.replace('matrix[3][2] = tz', 'matrix[3][2] = tx'),
            'wrong-rotation-inputs': screen.SELECTED.replace('matrix, rx, ry, rz', 'matrix, rz, ry, rx'),
            'wrong-output': screen.SELECTED.replace('matrix, output);', 'matrix, (Mtx *)((u8 *)output + 4));'),
            'premature-translation': screen.SELECTED.replace(translations, '').replace('    func_150A8050(', translations + '    func_150A8050('),
            'overwrite-provider-fields': screen.SELECTED.replace('    guMtxF2L(', '    matrix[0][3] = 0.0f;\n    guMtxF2L(')}
        receipts = []
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            differences = 0
            for pattern in range(3):
                args = arguments(-2, 0.25)
                memory = memory_case(args)
                wanted, calls = reference(memory, args, pattern, True)
                model = RowMatrixOracle(words, memory, args, pattern, True).run()
                differences += external(model.memory) != wanted or model.calls != calls
            self.assertGreater(differences, 0, name)
            receipts.append(dict(name=name, valid_mapped_cases=3, semantic_differences=differences))
        self.receipt('negatives', receipts)

    def test_copied_owners_retain_neighbors_pools_warnings_and_caller_words(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        stub = 's32 func_15142838() {\n    return 0;\n}'
        baseline = source.replace(screen.SELECTED, stub).replace(screen.PROTOTYPE, 's32 func_15142838();')
        self.assertIn(stub, baseline)
        selected = baseline.replace(stub, screen.SELECTED).replace('s32 func_15142838();', screen.PROTOTYPE)
        caller_source = (self.root / 'conker/src/game/generated_15F680.c').read_text()
        caller_baseline = caller_source.replace(screen.CALLER, screen.OLD_CALLER).replace(screen.PROTOTYPE, screen.OLD_CALLER_PROTOTYPE)
        self.assertIn(screen.OLD_CALLER, caller_baseline)
        caller_selected = caller_baseline.replace(screen.OLD_CALLER, screen.CALLER).replace(screen.OLD_CALLER_PROTOTYPE, screen.PROTOTYPE)
        receipts = []
        for prefix, old_source, new_source, target in (('builder', baseline, selected, screen.FUNCTION), ('caller', caller_baseline, caller_selected, None)):
            old, old_warnings = compile_owner(self.root, self.output, old_source, prefix + '-baseline')
            new, warnings = compile_owner(self.root, self.output, new_source, prefix + '-selected')
            self.assertEqual(warnings, old_warnings)
            old_text, old_functions, old_relocations = parse_object(old)
            text, functions, relocations = parse_object(new)
            self.assertEqual(set(functions), set(old_functions))
            for name, meta in functions.items():
                if name == target:
                    continue
                old_meta = old_functions[name]
                self.assertEqual(text[meta['value']:meta['value'] + meta['size']], old_text[old_meta['value']:old_meta['value'] + old_meta['size']], name)
                self.assertEqual({a - meta['value']: r for a, r in relocations.items() if meta['value'] <= a < meta['value'] + meta['size']},
                    {a - old_meta['value']: r for a, r in old_relocations.items() if old_meta['value'] <= a < old_meta['value'] + old_meta['size']}, name)
            if target:
                meta = functions[target]
                standalone, _, standalone_relocations = parse_object(self.output / 'selected.o')
                self.assertEqual(meta['size'], 220)
                self.assertEqual(text[meta['value']:meta['value'] + 220], standalone[:220])
                self.assertEqual({a - meta['value']: r for a, r in relocations.items() if meta['value'] <= a < meta['value'] + 220}, standalone_relocations)
            else:
                meta = functions['func_15133760']
                self.assertEqual(meta['size'], 96)
                words = list(struct.unpack_from('>24I', text, meta['value']))
                mapped = {a - meta['value']: r for a, r in relocations.items() if meta['value'] <= a < meta['value'] + 96}
                self.assertEqual(len(mapped), 1)
                offset, calls = next(iter(mapped.items()))
                self.assertEqual(calls, [('R_MIPS_26', screen.FUNCTION)])
                self.assertEqual(words[offset // 4], 0x0C000000)
                words[offset // 4] = 0x0C000000 | (screen.ENTRY >> 2 & 0x3FFFFFF)
                self.assertEqual(words, self.caller)
            for section in ('.rodata', '.data'):
                self.assertEqual(screen.sections(old).get(section), screen.sections(new).get(section))
            receipts.append(dict(owner=prefix, functions=len(functions), warnings=len(warnings), unchanged=len(functions) - (1 if target else 0)))
        self.receipt('owners', receipts)

    def test_production_sources_exact_target_caller_neighbors_and_unchanged_guards(self):
        owner = (self.root / 'conker/src/game_16EE20.c').read_text()
        caller = (self.root / 'conker/src/game/generated_15F680.c').read_text()
        self.assertIn(screen.SELECTED, owner)
        self.assertIn(screen.CALLER, caller)
        self.assertEqual(owner.count(screen.PROTOTYPE), 1)
        self.assertEqual(caller.count(screen.PROTOTYPE), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        self.assertEqual(functions['func_15133760'], self.caller)
        for name, rom, count in (('func_15141A7C', 0x16EF2C, 100), ('func_15141C0C', 0x16F0BC, 45),
                ('func_15141CC0', 0x16F170, 57), ('func_15141DA4', 0x16F254, 37), ('func_15141E38', 0x16F2E8, 80),
                ('func_15141F78', 0x16F428, 96), ('func_15142180', 0x16F630, 80), ('func_151424F4', 0x16F9A4, 67)):
            self.assertEqual(functions[name], list(struct.unpack_from('>%dI' % count, self.rom, rom)))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        self.assertEqual(len(guards), 10809)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        digest = hashlib.sha256(json.dumps(guards, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        self.assertEqual(digest, 'e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a')
        self.receipt('production', dict(words=55, direct=True, caller_words=24, guards=10809, guard_sha256=digest, exact_neighbors=8))


if __name__ == '__main__':
    unittest.main()
