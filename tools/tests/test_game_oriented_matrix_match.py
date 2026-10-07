"""Direct oriented-builder fit, original private storage and typed caller gates."""

import csv
import itertools
import json
import math
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_oriented_matrix_lifetime_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_oriented_matrix_recovery as recovery
from tools.tests import test_game_random_curve_record as native
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly, fixed_payload

STACK, OUTPUT, ACTOR = recovery.STACK, recovery.OUTPUT, recovery.ACTOR
CALLER, CONVERT = recovery.CALLER, recovery.CONVERT
bits, floating, read, put = recovery.bits, recovery.floating, recovery.read, recovery.put


class PrivateOrientedOracle(recovery.OrientedOracle):
    """Finite CVT.W.S with default nearest/even only; no FCSR/hardware claim."""

    def execute(self, word):
        if word >> 26 == 17 and word >> 21 & 31 == 16 and word & 63 == 36:
            fs, fd = word >> 11 & 31, word >> 6 & 31
            value = floating(self.f[fs])
            assert math.isfinite(value) and -0x80000000 <= value <= 0x7FFFFFFF, ('unsupported conversion', value)
            result = round(value)
            assert -0x80000000 <= result <= 0x7FFFFFFF
            self.f[fd] = result & 0xFFFFFFFF
        else:
            super().execute(word)


class GameOrientedMatrixMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-oriented-matrix-match-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected', screen.SELECTED)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>142I', rom, screen.ROM))
        cls.caller = list(struct.unpack_from('>30I', rom, 0xE71C4))
        cls.converter = list(struct.unpack_from('>115I', rom, 0xD4C40))
        cls.inputs = list(recovery.cases())
        cls.fixture = recovery.native_fixture(cls.inputs).replace(screen.prior.SELECTED, screen.SELECTED)
        assert cls.fixture.count(screen.SELECTED) == 1
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def equal_effects(self, pair):
        for attr in ('memory', 'events', 'r', 'f', 'visits', 'calls'):
            self.assertEqual(getattr(pair[0], attr), getattr(pair[1], attr), attr)
        return pair

    def compare(self, args, phase=0, caller=False, fixed=False, mutation=False):
        memory = recovery.memory_case(args)
        values = recovery.reference(args)
        wanted = dict(memory)
        if mutation:
            for offset in recovery.OFFSETS:
                put(wanted, ACTOR + offset, 0xA5000000 + offset)
        payload = fixed_payload(values) if fixed else struct.pack('>16I', *values)
        wanted.update({args[0] + i: b for i, b in enumerate(payload)})
        connected = {}
        if caller:
            connected.update(zip(range(CALLER, CALLER + 120, 4), self.caller))
        if fixed:
            connected.update(zip(range(CONVERT, CONVERT + 460, 4), self.converter))
        models = []
        for words in (self.words, self.retail):
            model = recovery.OrientedOracle(words, memory, args, phase, connected, mutation)
            if caller:
                model.entry = CALLER
                model.r[4:8] = model.before[4:8] = [args[0], ACTOR, 0, 0]
            model.run()
            if caller:
                self.assertEqual(model.forwarded, args)
                self.assertEqual(model.r[2], 1)
            self.assertEqual(len(model.calls), 1)
            observed, destination, snapshot = model.calls[0]
            self.assertEqual((destination, snapshot), (args[0], recovery.external(memory)))
            for i, (a, b) in enumerate(zip(observed, values)):
                self.assertTrue(recovery.equal_word(a, b) if recovery.arithmetic_index(i) else a == b,
                    (i, hex(a), hex(b)))
            actual = recovery.external(model.memory)
            if not fixed:
                for i in range(16):
                    if recovery.arithmetic_index(i) and recovery.equal_word(read(actual, args[0] + i * 4), values[i]):
                        put(actual, args[0] + i * 4, values[i])
            self.assertEqual(actual, recovery.external(wanted))
            models.append(model)
        return self.equal_effects(models)

    def test_direct_slot_and_four_fitting_real_storage_orders(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (142, 184, 0))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.record['relocations'], {0x21C: [('R_MIPS_26', 'guMtxF2L')]})
        self.assertEqual(screen.local_layout(self.out / 'selected.o'), dict(frame=184, entry_relative=dict(
            matrix=-64, leftX=-68, direction=-80, leftZ=-84, up=-96, inverse=-100)))
        records, exact = [], []
        for name, body in screen.candidates():
            record, words = screen.compile_candidate(self.root, self.out, name, body)
            record['layout'] = screen.local_layout(self.out / (name + '.o'))
            self.assertEqual(record['diagnostics'], '')
            self.assertEqual(record['profile'], 'o2g3')
            if name.startswith('inplace-order-'):
                expected = (142, 184, 10 if name[len('inplace-order-')] == '1' else 27)
                self.assertEqual((record['body_words'], record['frame'], record['differences']), expected)
            if not record['differences']:
                self.assertEqual(words, self.retail)
                exact.append(name)
            records.append(record)
        self.assertEqual(len(records), 48)
        self.assertEqual(exact, ['scalar-left-order-' + order for order in ('20314', '21304', '20341', '21340')])
        self.receipt('controls', dict(measurements=records, exact=exact,
            matrix_first_reduces_differences_to=10, no_guard_or_profile_changes=True))

    def test_reference_backed_guest_aliases_float_edges_and_complete_private_effects(self):
        coverage, count = set(), 0
        for original, alias, phase, mutation in itertools.product(self.inputs, range(3), (0, 8), (False, True)):
            args = ((OUTPUT, ACTOR + 0x18, ACTOR + 0x20)[alias], *original[1:])
            for model in self.compare(args, phase, mutation=mutation):
                coverage.update(model.visits)
            count += 1
        self.assertEqual(count, 2448)
        self.assertEqual(coverage, set(range(screen.ENTRY, screen.ENTRY + 568, 4)))
        self.receipt('guest', dict(cases=count, all_words=142, independent_matrix_reference=True,
            full_memory_events_registers_equal=True, arithmetic_nan_reference='classification only'))

    def test_original_caller_builder_and_fixed_converter_all_words_exact_domain(self):
        coverage, count = set(), 0
        for delta, rows, column, alias, phase in itertools.product(((4, 0, 0), (-4, 0, 0), (0, 0, 4), (0, 0, -4)),
                ((0.5, 2), (-2, 0.25)), ((2, -0.5, 3), (-2, 0.25, -1), (0, 0, 0)), range(3), (0, 8)):
            start = (0.5, -2, 4)
            args = ((OUTPUT, ACTOR + 0x18, ACTOR + 0x20)[alias],
                *map(bits, (*rows, *column, *start, *[a + b for a, b in zip(start, delta)])))
            for model in self.compare(args, phase, caller=True, fixed=True):
                coverage.update(model.visits)
            count += 1
        expected = (set(range(screen.ENTRY, screen.ENTRY + 568, 4)) |
            set(range(CALLER, CALLER + 120, 4)) | set(range(CONVERT, CONVERT + 460, 4)))
        self.assertEqual(coverage, expected)
        self.assertEqual(count, 144)
        self.receipt('connected', dict(cases=count, caller_words=30, builder_words=142, converter_words=115,
            all_words=True, full_memory_events_registers_equal=True, domain='finite exact integral signed32 scaling'))

    def test_private_converter_source_destination_overlap_and_old_layout_negative(self):
        connected = dict(zip(range(CONVERT, CONVERT + 460, 4), self.converter))
        _, old = screen.compile_candidate(self.root, self.out, 'old-inplace', screen.BASELINE)
        records, changes = [], 0
        for offset, phase, rows, start in itertools.product(range(0x28, 0xB8, 4), (0, 8),
                ((1, 2), (2, 1)), ((0, 0, 0), (1, 2, 4))):
            output = STACK + phase - 184 + offset
            args = (output, *map(bits, (*rows, 1, 2, 4, *start, start[0], start[1], start[2] + 4)))
            memory = recovery.memory_case(args)
            pair = [PrivateOrientedOracle(words, memory, args, phase, connected).run()
                for words in (self.words, self.retail)]
            self.equal_effects(pair)
            legacy = PrivateOrientedOracle(old, memory, args, phase, connected).run()
            result = bytes(pair[0].memory[output + i] for i in range(64))
            different = result != bytes(legacy.memory[output + i] for i in range(64))
            changes += different
            records.append(dict(offset=offset, phase=phase, rows=rows, start=start, old_output_differs=different))
        self.assertEqual(len(records), 288)
        self.assertGreater(changes, 0)
        self.receipt('private-alias', dict(cases=len(records), old_output_differences=changes, cases_detail=records,
            full_memory_events_registers_equal=True, converter='finite default nearest/even bounded model'))

    def test_actual_native_32bit_typed_caller_and_complete_external_storage(self):
        self.run_host('int n,a,m,count=0;\nfor(n=0;n<204;n++)for(a=0;a<3;a++)for(m=0;m<2;m++){\n'
            'initialize(n,a,m);if(func_150B9D14(output,source)!=1 || check())return 20+error;count++;}\n'
            'if(count!=1224 || sizeof(Mtx)!=64 || sizeof(f32)!=4 || sizeof(void *)!=4)return 30;\n')
        self.receipt('native', dict(cases=1224, bits=32, selected_source_and_typed_caller=True,
            complete_external_storage=True, converter='bounded float payload capture', private_stack_aliases=False))

    def test_nine_compiled_semantic_negatives_change_known_results(self):
        args = (OUTPUT, *map(bits, (1, 2, 2, -0.5, 3, 7, -9, 11, 10, -7, 15)))
        expected = recovery.reference(args)
        source = screen.SELECTED
        forms = {'placeholder': screen.prior.PROTOTYPE[:-1] + ' { }',
            'missing-converter': source.replace('    guMtxF2L(matrix, output);', ''),
            'wrong-direction': source.replace('ex - sx', 'sx - ex'),
            'wrong-cross': source.replace('up.unk0 = -direction.unk4', 'up.unk0 = direction.unk4'),
            'missing-up-normalization': source.replace('up.unk8 * inverse *', 'up.unk8 *'),
            'wrong-row': source.replace('cy * row1', 'cy * row0'),
            'wrong-column': source.replace('leftX * cx', 'leftX * cy'),
            'view-translation': source.replace('matrix[3][0] = sx;', 'matrix[3][0] = -sx;'),
            'wrong-output': source.replace('matrix, output);', 'matrix, (Mtx *)((u8 *)output + 4));')}
        for name, body in forms.items():
            self.assertNotEqual(body, source)
            _, words = screen.compile_candidate(self.root, self.out, name, body)
            model = recovery.OrientedOracle(words, recovery.memory_case(args), args).run()
            changed = len(model.calls) != 1 or model.calls[0][1] != OUTPUT or any(
                not recovery.equal_word(a, b) for a, b in zip(model.calls[0][0], expected))
            self.assertTrue(changed, name)
        self.receipt('negatives', dict(count=9, result_or_call_changes=True))

    def copied_builder(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        stub = 's32 func_15142600() {\n    return 0;\n}'
        baseline = source.replace(screen.SELECTED, stub).replace(screen.prior.PROTOTYPE, 's32 func_15142600();')
        self.assertEqual(baseline.count(stub), 1)
        selected = baseline.replace(stub, screen.SELECTED).replace('s32 func_15142600();', screen.prior.PROTOTYPE)
        objects, warning_sets = [], []
        for name, body in (('baseline', baseline), ('selected', selected)):
            obj, warnings = compile_owner(self.root, self.out, body, 'builder-' + name)
            warning_sets.append(warnings)
            processed = self.out / ('builder-' + name + '-postprocessed.o')
            shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.out / ('builder-' + name + '.c')).relative_to(self.root / 'conker')), '--post-process',
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
            prior = old_functions[name]
            self.assertEqual(text[current['value']:current['value'] + current['size']],
                old_text[prior['value']:prior['value'] + prior['size']], name)
            self.assertEqual({o - current['value']: r for o, r in rel.items()
                if current['value'] <= o < current['value'] + current['size']},
                {o - prior['value']: r for o, r in old_rel.items()
                if prior['value'] <= o < prior['value'] + prior['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        target = functions[screen.FUNCTION]
        standalone, _, _ = parse_object(self.out / 'selected.o')
        self.assertEqual(target['size'], 568)
        self.assertEqual(text[target['value']:target['value'] + 568], standalone[:568])
        self.assertEqual({o - target['value']: r for o, r in rel.items()
            if target['value'] <= o < target['value'] + 568}, self.record['relocations'])
        self.receipt('builder-owner', dict(functions=89, neighbors=88, warnings=2, pools_unchanged=True))
        return objects[1]

    def test_copied_builder_real_padder_full_slot_and_converter_relocation(self):
        obj = self.copied_builder()
        assembly = emit_padded_assembly(obj, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=self.root / 'conker/retail_word_patches.us.csv')
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        body = assembly[start:assembly.index('\n', end) + 1]
        self.assertEqual(len(re.findall(r'\.word 0x[0-9A-F]{8}', body)), 142)
        self.assertNotIn('__retail_overflow_' + screen.FUNCTION, assembly)
        source, padded, elf = (self.out / ('padded' + suffix) for suffix in ('.s', '.o', '.elf'))
        source.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + body)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(padded), str(source)],
            check=True, capture_output=True)
        _, functions, relocations = parse_object(padded)
        self.assertEqual(functions[screen.FUNCTION]['size'], 568)
        self.assertEqual(relocations, self.record['relocations'])
        for address in (CONVERT, CONVERT + 0x1000000):
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'oriented.ld'),
                '-e', screen.FUNCTION, '--defsym=guMtxF2L=0x%X' % address,
                '-o', str(elf), str(padded)], check=True, capture_output=True)
            expected = self.retail.copy()
            expected[0x21C // 4] = 0x0C000000 | (address >> 2 & 0x3FFFFFF)
            self.assertEqual(list(struct.unpack_from('>142I', screen.prior.sections(elf)['.text'][1])), expected)

    def test_copied_typed_caller_is_raw_identical_in_all_eight_functions(self):
        source = (self.root / 'conker/src/game/generated_E5E90.c').read_text()
        baseline = source.replace(screen.prior.CALLER, screen.prior.LEGACY_CALLER).replace(
            screen.prior.PROTOTYPE, screen.prior.OLD_CALLER_PROTOTYPE)
        self.assertEqual(baseline.count(screen.prior.LEGACY_CALLER), 1)
        selected = baseline.replace(screen.prior.LEGACY_CALLER, screen.prior.CALLER).replace(
            screen.prior.OLD_CALLER_PROTOTYPE, screen.prior.PROTOTYPE)
        old, old_warnings = compile_owner(self.root, self.out, baseline, 'caller-baseline')
        new, warnings = compile_owner(self.root, self.out, selected, 'caller-selected')
        self.assertEqual(warnings, old_warnings)
        self.assertFalse(warnings)
        old_text, old_functions, old_rel = parse_object(old)
        text, functions, rel = parse_object(new)
        self.assertEqual(set(functions), set(old_functions))
        self.assertEqual(len(functions), 8)
        for name, current in functions.items():
            prior = old_functions[name]
            self.assertEqual(text[current['value']:current['value'] + current['size']],
                old_text[prior['value']:prior['value'] + prior['size']], name)
            self.assertEqual({o - current['value']: r for o, r in rel.items()
                if current['value'] <= o < current['value'] + current['size']},
                {o - prior['value']: r for o, r in old_rel.items()
                if prior['value'] <= o < prior['value'] + prior['size']}, name)
        self.assertEqual(normalized_pools(old), normalized_pools(new))
        caller = functions['func_150B9D14']
        self.assertEqual(caller['size'], 120)
        words = list(struct.unpack_from('>30I', text, caller['value']))
        self.assertEqual({o - caller['value']: r for o, r in rel.items()
            if caller['value'] <= o < caller['value'] + 120}, {0x58: [('R_MIPS_26', screen.FUNCTION)]})
        words[0x58 // 4] = 0x0C000000 | (screen.ENTRY >> 2 & 0x3FFFFFF)
        self.assertEqual(words, self.caller)
        self.receipt('caller-owner', dict(functions=8, all_raw_unchanged=True, warnings=0, caller_words=30))

    def test_mapped_inputs_private_matrix_and_destination_fail_closed(self):
        args = self.inputs[0]
        for address, caller in ((ACTOR + 0x18, True), (ACTOR + 0x40, True), (OUTPUT, False),
                (STACK - 184 + 0x78, False)):
            memory = recovery.memory_case(args)
            del memory[address]
            connected = dict(zip(range(CALLER, CALLER + 120, 4), self.caller)) if caller else {}
            for words in (self.words, self.retail):
                model = recovery.OrientedOracle(words, memory, args, connected=connected)
                if caller:
                    model.entry = CALLER
                    model.r[4:8] = model.before[4:8] = [OUTPUT, ACTOR, 0, 0]
                with self.assertRaisesRegex(AssertionError, 'unmapped'):
                    model.run()

    def test_installed_builder_typed_caller_exact_slots_and_unchanged_guard_history(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertEqual(source.count(screen.SELECTED), 1)
        self.assertEqual(source.count(screen.prior.PROTOTYPE), 1)
        caller = (self.root / 'conker/src/game/generated_E5E90.c').read_text()
        self.assertEqual(caller.count(screen.prior.CALLER), 1)
        self.assertEqual(caller.count(screen.prior.PROTOTYPE), 1)
        self.assertNotIn(screen.prior.OLD_CALLER_PROTOTYPE, caller)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        self.assertEqual(functions['func_150B9D14'], self.caller)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] in (screen.FUNCTION, 'func_150B9D14') for row in guards))


if __name__ == '__main__':
    unittest.main()
