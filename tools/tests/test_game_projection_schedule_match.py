"""Fitting projection C, closed instruction inputs and guarded copied-owner checks."""

import csv
import itertools
import math
import random
import shutil
import struct
import subprocess
import sys
from collections import Counter

from tools.experiments import game_projection_schedule_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_projection_lifetime_recovery as recovery
from tools.tests.game_owner_pool import normalized_pools
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly

STUB = 's32 func_15144CEC() {\n    return 0;\n}'


def guarded(words, rows):
    result = list(words)
    for row in rows:
        i = int(row['offset'], 16) // 4
        replacement = int(row['replacement'], 16)
        if row['replacement_relocations'] != '-':
            replacement |= result[i] & 65535
        result[i] = replacement
    return result


def read_phases(model):
    phases, reads = [], Counter()
    for kind, address, size, value in model.events:
        if recovery.private(address):
            continue
        if kind == 'R':
            reads[(address, size, value)] += 1
        else:
            phases.append((reads, (kind, address, size, value)))
            reads = Counter()
    phases.append((reads, None))
    return phases


class OperandCode(dict):
    def __init__(self, model, remap=False):
        super().__init__(model.code)
        self.model, self.remap, self.trace = model, remap, {}

    def __getitem__(self, pc):
        word = super().__getitem__(pc)
        m = self.model
        op, rs, rt, rd, shift, fn = (word >> 26, word >> 21 & 31,
            word >> 16 & 31, word >> 11 & 31, word >> 6 & 31, word & 63)
        imm = word & 65535
        signed_imm = imm if imm < 32768 else imm - 65536
        if op == 0:
            if fn == 0: inputs = (m.r[rt], shift)
            elif fn in (33, 37): inputs = tuple(sorted((m.r[rs], m.r[rt])))
            elif fn == 35: inputs = (m.r[rs], m.r[rt])
            elif fn == 8: inputs = (m.r[rs],)
            else: raise AssertionError(('integer input trace', hex(word)))
            identity = (op, fn)
        elif op in (35, 36, 43, 49, 57):
            address = (m.r[rs] + signed_imm) & 0xFFFFFFFF
            size = 1 if op == 36 else 4
            value = m.f[rt] if op == 57 else m.r[rt] if op == 43 else recovery.peek(m.memory, address, size)
            inputs, identity = (address, size, value), (op,)
        elif op == 17:
            identity = (op, rs, fn if rs == 16 else None)
            if rs == 4: inputs = (m.r[rt],)
            elif rs == 8: inputs = (m.condition, rt, imm)
            elif rs == 16:
                inputs = (m.f[rd], m.f[rt])
                if fn in (0, 2, 50): inputs = tuple(sorted(inputs))
            else: raise AssertionError(('floating input trace', hex(word)))
        elif op in (2, 3):
            inputs, identity = (((pc + 4) & 0xF0000000) | ((word & 0x3FFFFFF) << 2),), (op,)
        elif op in (4, 5, 20, 21):
            inputs, identity = (*sorted((m.r[rs], m.r[rt])), imm), (op,)
        elif op == 9: inputs, identity = (m.r[rs], signed_imm), (op,)
        elif op == 15: inputs, identity = (imm,), (op,)
        else: raise AssertionError(('projection input trace', hex(word)))
        mapped = pc
        if self.remap and screen.ENTRY <= pc < screen.ENTRY + 404:
            mapped = screen.ENTRY + screen.SCHEDULE.get(pc - screen.ENTRY, pc - screen.ENTRY)
        assert mapped not in self.trace, ('duplicate instruction visit', hex(mapped))
        self.trace[mapped] = identity, inputs
        return word


class CallerOracle(recovery.ProjectionOracle):
    def record_call(self, target):
        if target == screen.ENTRY:
            self.calls.append((target, *self.arguments(6)))
        else:
            super().record_call(target)


class GameProjectionScheduleMatchTests(recovery.GameProjectionLifetimeRecoveryTests):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.fixture = cls.fixture.replace(recovery.screen.SELECTED, screen.SELECTED)
        cls.output = cls.root / 'conker/build/game-projection-schedule-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rows = screen.owner_guards()
        cls.normalized = guarded(cls.words, cls.rows)

    def pair(self, memory, args, actions=(), phase=0):
        models = super().pair(memory, args, actions, phase)
        normalized = recovery.ProjectionOracle(self.normalized, memory, args,
            self.connected, phase, actions).run()
        self.assertEqual(normalized.memory, models[0].memory)
        self.assertEqual(normalized.events, models[0].events)
        self.assertEqual(normalized.calls, models[0].calls)
        self.assertEqual(normalized.r, models[0].r)
        self.assertEqual(normalized.f, models[0].f)
        self.assertEqual(read_phases(models[1]), read_phases(models[0]))
        return models

    def test_compiler_receipts_preserve_explicit_nonmatch(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (101, 72, 37))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertFalse(self.record['exact'])
        self.assertEqual(self.normalized, self.retail)
        self.assertEqual(len(self.rows), 37)
        self.assertTrue(all(r['insert_after'] == '' and r['omit'] == 'false' for r in self.rows))
        self.assertEqual(set(screen.SCHEDULE.values()), set(screen.SCHEDULE))
        self.assertEqual(self.words[:17], self.retail[:17])
        self.assertEqual(self.words[-5:], self.retail[-5:])

    def test_instruction_inputs_close_every_register_and_schedule_guard(self):
        cases = 0
        for index, mask, layout, depth, phase in itertools.product(
                (0, 127, 128, 255), range(8), range(9), (0.0, 2.0, 6000.0), (0, 8)):
            memory, args, actions = recovery.fixture(index, mask, layout, depth=depth, phase=phase)
            traces = []
            for raw, words in ((False, self.retail), (True, self.words)):
                model = recovery.ProjectionOracle(words, memory, args, self.connected, phase, actions)
                model.code = OperandCode(model, raw)
                model.run()
                traces.append(model.code.trace)
            self.assertEqual(traces[0], traces[1])
            cases += 1
        self.assertEqual(cases, 1728)

    def test_varied_finite_coordinates_matrices_scales_and_rounding(self):
        rng = random.Random(screen.ENTRY)
        for _ in range(4096):
            index, mask, layout, phase = rng.randrange(256), rng.randrange(8), rng.randrange(9), rng.choice((0, 8))
            memory, args, actions = recovery.fixture(index, mask, layout, phase=phase)
            for i in range(3):
                value = math.ldexp(rng.randrange(-64, 65) / 8.0, rng.randrange(-8, 9))
                recovery.put(memory, recovery.POINT + i * 4, recovery.bits(value))
            for i in range(16):
                value = rng.randrange(-8, 9) / 8.0
                if i % 4 == 3:
                    value = rng.choice((0.0, 0.25, 2.0, 6000.0)) if i == 15 else 0.0
                recovery.put(memory, recovery.BANK + index * 64 + i * 4, recovery.bits(value))
            for offset in (12, 16, 52, 56):
                recovery.put(memory, recovery.VIEW + index * 384 + offset,
                    recovery.bits(rng.randrange(-256, 257) / 8.0))
            self.pair(memory, args, actions, phase)

    def test_real_w_store_overwrites_index_home_before_view_selection(self):
        for index, phase in itertools.product(range(256), (0, 8)):
            memory, args, _ = recovery.fixture(index, phase=phase, new_index=0)
            args = (*args[:3], recovery.STACK + phase + 0x14, *args[4:])
            retail, raw = self.pair(memory, args, phase=phase)
            self.assertEqual(recovery.peek(retail.memory, recovery.STACK + phase + 0x14), recovery.bits(2.0))
            self.assertEqual(retail.calls[0][1], recovery.BANK + index * 64)
            self.assertEqual(recovery.floating(recovery.peek(raw.memory, recovery.XY)), 18.0)
            self.assertEqual(recovery.floating(recovery.peek(raw.memory, recovery.XY + 4)), 25.0)

    def test_original_eleven_word_caller_setup_and_index_delay_store(self):
        caller, index_word = 0x150CE270, 0x80082FA4
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        words = list(struct.unpack_from('>11I', rom, 0xFB720))
        self.assertEqual(words[-2:], [0x0D45133B, 0xAFAB0014])
        # The real setup ends at the call's delay; return scaffolding is synthetic.
        words += [0x3C1FDEAD, 0x03E00008, 0]
        cases = 0
        for index, depth, phase in itertools.product(range(256), (0.0, 2.0, 6000.0), (0, 8)):
            memory, _, _ = recovery.fixture(index, depth=depth, phase=phase)
            sp = recovery.STACK + phase
            memory.update({index_word + i: 0xA5 for i in range(4)})
            recovery.put(memory, index_word, 0xA5AB0000 | index)
            recovery.put(memory, sp + 0x28, recovery.XY - 0x28)
            for i, value in enumerate((2.0, 3.0, 4.0)):
                recovery.put(memory, sp + 0x40 + i * 4, recovery.bits(value))
            args = (sp + 0x40, recovery.XY, sp + 0x3C, sp + 0x38,
                    sp + 0x34, 0xA5AB0000 | index)
            expected, _, helper_calls, status = recovery.reference(memory, args, phase=phase)
            models = []
            for wrapper in (self.retail, self.words, self.normalized):
                connected = dict(self.connected)
                connected.update(zip(range(screen.ENTRY, screen.ENTRY + 404, 4), wrapper))
                model = CallerOracle(words, memory, (0, 0, 0, 0), connected, phase)
                model.entry = caller
                model.code = dict(zip(range(caller, caller + len(words) * 4, 4), words))
                model.code.update(connected)
                model.run()
                self.assertEqual(model.r[2], status)
                self.assertEqual(model.calls, [(screen.ENTRY, *args), *helper_calls])
                self.assertEqual(recovery.external(model.memory), recovery.external(expected))
                for offset in (0x38, 0x3C):
                    self.assertEqual(recovery.peek(model.memory, sp + offset), recovery.peek(expected, sp + offset))
                if status:
                    self.assertEqual(recovery.peek(model.memory, sp + 0x34), recovery.peek(expected, sp + 0x34))
                self.assertEqual(recovery.peek(model.memory, sp + 0x14), args[5])
                models.append(model)
            self.assertEqual(models[0].memory, models[1].memory)
            self.assertEqual(models[0].events, models[2].events)
            self.assertEqual(read_phases(models[0]), read_phases(models[1]))
            cases += 1
        self.assertEqual(cases, 1536)

    def test_copied_owner_pool_neighbors_padding_relocations_and_stale_guards(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        baseline = source.replace(screen.SELECTED, STUB).replace(screen.DECLARATIONS + '\n', '')
        baseline = baseline.replace(screen.PROTOTYPE, 's32 func_15144CEC();')
        selected = baseline.replace('/* Generated placeholder declarations. */',
            screen.DECLARATIONS + '\n/* Generated placeholder declarations. */')
        selected = selected.replace('s32 func_15144CEC();', screen.PROTOTYPE).replace(STUB, screen.SELECTED)
        objects, warnings = [], []
        for name, body in (('baseline', baseline), ('selected', selected)):
            obj, warning = compile_owner(self.root, self.output, body, 'owner-' + name)
            warnings.append(warning)
            processed = self.output / ('owner-' + name + '-postprocessed.o')
            shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.output / ('owner-' + name + '.c')).relative_to(self.root / 'conker')),
                '--post-process', str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker',
                check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0], warnings[1])
        self.assertEqual(len(warnings[0]), 2)
        old_text, old_functions, old_rel = parse_object(objects[0])
        text, functions, rel = parse_object(objects[1])
        self.assertEqual(set(functions), set(old_functions))
        self.assertEqual(len(functions), 89)
        for name, f in functions.items():
            if name == screen.FUNCTION: continue
            old = old_functions[name]
            self.assertEqual(text[f['value']:f['value'] + f['size']],
                old_text[old['value']:old['value'] + old['size']], name)
            self.assertEqual({o - f['value']: r for o, r in rel.items() if f['value'] <= o < f['value'] + f['size']},
                {o - old['value']: r for o, r in old_rel.items() if old['value'] <= o < old['value'] + old['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        raw, standalone, raw_rel = parse_object(self.output / 'selected.o')
        f, g = functions[screen.FUNCTION], standalone[screen.FUNCTION]
        self.assertEqual(text[f['value']:f['value'] + 404], raw[g['value']:g['value'] + 404])
        self.assertEqual({o - f['value']: r for o, r in rel.items() if f['value'] <= o < f['value'] + 404}, raw_rel)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = [r for r in csv.DictReader(stream) if r['function'] != screen.FUNCTION] + self.rows
        path = self.output / 'guards.csv'

        def emit(items):
            with path.open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=list(items[0]))
                writer.writeheader(); writer.writerows(items)
            return emit_padded_assembly(objects[1], self.root / 'conker/retail_layout.us.txt',
                'game_16EE20', rodata_symbol='jtbl_800A5218_game', word_patches_path=path)

        assembly = emit(rows)
        begin = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), begin)
        end = assembly.index('\n', end)
        asm, obj, elf = (self.output / ('padded' + s) for s in ('.s', '.o', '.elf'))
        asm.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + assembly[begin:end + 1])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(asm)], check=True, capture_output=True)
        _, padded, padded_rel = parse_object(obj)
        self.assertEqual(padded[screen.FUNCTION]['size'], 404)
        self.assertEqual(padded_rel, self.record['relocations'])
        for alternate in (False, True):
            symbols = screen.SYMBOLS if not alternate else {n: (a + 0x1007E10) & 0xFFFFFFFF for n, a in screen.SYMBOLS.items()}
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T',
                str(self.output / 'projection-lifetime.ld'), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X' % item for item in symbols.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = self.retail.copy()
            for hi, lo, name in ((0x20, 0x24, 'D_800D9D10'), (0x98, 0x9C, 'D_800A56B0'),
                    (0xA8, 0xBC, 'D_800D9B20'), (0xDC, 0xE8, 'D_800BE628')):
                expected[hi // 4] = expected[hi // 4] & 0xFFFF0000 | ((symbols[name] + 0x8000) >> 16) & 65535
                expected[lo // 4] = expected[lo // 4] & 0xFFFF0000 | symbols[name] & 65535
            expected[0x8C // 4] = 0x0C000000 | (symbols['func_150A7A00'] >> 2 & 0x3FFFFFF)
            self.assertEqual(list(struct.unpack_from('>101I', recovery.screen.sections(elf)['.text'][1])), expected)
        for column, value, pattern in (('expected', '0x00000000', 'stale'),
                ('expected_relocations', 'R_MIPS_LO16:D_800BE628', 'stale relocations')):
            broken = [dict(r) for r in rows]
            broken[-1][column] = value
            with self.assertRaisesRegex(ValueError, pattern): emit(broken)

    def test_production_source_complete_slot_and_guards(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertNotIn(STUB, source)
        self.assertIn(screen.SELECTED, source)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual([r for r in rows if r['function'] == screen.FUNCTION], self.rows)


if __name__ == '__main__':
    import unittest
    unittest.main()
