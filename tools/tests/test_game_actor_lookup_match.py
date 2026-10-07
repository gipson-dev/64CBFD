"""Direct actor lookup match, lazy validity reads and original connected search."""

import csv
import hashlib
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

from tools.experiments import game_actor_lookup_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests import test_game_random_curve_record as native
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests.test_game_queued_segment_writer import STACK

LOOKUP, CANDIDATE, FOUND = 0x15083E90, 0x20000, 0x22000
ACTORS, STRIDE = 0x800CC2D0, 0x32C
HEADER_OVERRIDE = '#define func_15083E90 func_15083E90_legacy_word_signature\n'
HEADER_END = '#undef func_15083E90\n' + screen.DECLARATIONS


def put(memory, address, value, size=4):
    memory.update({address + i: b for i, b in enumerate(
        (value & ((1 << (8 * size)) - 1)).to_bytes(size, 'big'))})


def read(memory, address, size=4):
    return int.from_bytes(bytes(memory[address + i] for i in range(size)), 'big')


def fixture(slot, kind=2, valid=1, found=FOUND, found_valid=1):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x100, 0x100)}
    for base in (CANDIDATE, FOUND):
        memory.update({base + i: (i * 31 + 7) & 255 for i in range(0x200)})
    put(memory, CANDIDATE, 0 if kind == 1 else 0x80000000)
    put(memory, CANDIDATE + 0x3B, (slot + (kind == 3)) & 255, 1)
    put(memory, CANDIDATE + 0x1D4, valid)
    put(memory, FOUND + 0x1D4, found_valid)
    return memory, (slot | 0xABCD0000, 0 if kind == 0 else CANDIDATE)


def external_events(model):
    return [e for e in model.events if e[0] == 'CALL' or not STACK - 0x100 <= e[1] < STACK + 0x100]


def reference(memory, args, found=FOUND, mutation=None):
    memory, events = dict(memory), []
    slot, candidate = args[0] & 255, args[1]

    def load(address, size=4):
        value = read(memory, address, size)
        events.append(('R', address, size, value))
        return value

    if slot == 255:
        return candidate if load(candidate + 0x1D4) else 0, memory, events, []
    if candidate and load(candidate) and slot == load(candidate + 0x3B, 1):
        return candidate if load(candidate + 0x1D4) else 0, memory, events, []
    calls = [(LOOKUP, slot)]
    events.append(('CALL', LOOKUP, (slot,)))
    if mutation is not None:
        put(memory, found + 0x1D4, mutation)
        events.append(('W', found + 0x1D4, 4, mutation))
    return found if found and load(found + 0x1D4) else 0, memory, events, calls


class LookupOracle(TriangleOracle):
    def __init__(self, words, memory, args, phase=0, found=FOUND, mutation=None, connected=None):
        super().__init__(words, memory, phase=phase, entry=screen.ENTRY, arguments=args, connected=connected)
        self.found, self.mutation = found, mutation

    def record_call(self, target):
        assert target == LOOKUP
        args = (self.r[4],)
        self.calls.append((target, *args))
        self.events.append(('CALL', target, args))

    def hook(self, target):
        assert target == LOOKUP and self.r[4] <= 255
        if self.mutation is not None:
            self.put(self.found + 0x1D4, self.mutation, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.r[2] = self.found


class GameActorLookupMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-actor-lookup-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>44I', cls.rom, screen.ROM))
        cls.lookup = list(struct.unpack_from('>72I', cls.rom, 0xB1340))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, data):
        (self.out / (name + '.json')).write_text(json.dumps(data, indent=2) + '\n')

    def models(self, memory, args, **kwargs):
        pair = [LookupOracle(words, memory, args, **kwargs).run() for words in (self.words, self.retail)]
        for attr in ('memory', 'events', 'r', 'f', 'visits', 'calls'):
            self.assertEqual(getattr(pair[0], attr), getattr(pair[1], attr), attr)
        return pair

    def test_complete_direct_slot_and_word_vs_byte_abi_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (44, 24, 0))
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.record['pool_bytes'], 0)
        self.assertEqual(self.record['relocations'], {0x78: [('R_MIPS_26', 'func_15083E90')]})
        # The connected retail callee itself preserves then narrows its incoming word.
        self.assertEqual(self.lookup[:3], [0xAFA40000, 0x308E00FF, 0x01C02025])
        records = []
        for name, body in screen.candidates():
            for abi, declaration in (('word', screen.LEGACY_DECLARATIONS), ('byte', screen.DECLARATIONS)):
                record, words = screen.compile_candidate(self.root, self.out, name + '-' + abi, body,
                    declarations=declaration)
                record['lookup_abi'] = abi
                if not record['differences']:
                    self.assertEqual(words, self.retail)
                    self.assertEqual(abi, 'byte')
                records.append(record)
        self.assertEqual(len(records), 62)
        self.assertTrue(all(r['differences'] for r in records if r['lookup_abi'] == 'word'))
        self.receipt('controls', dict(measurements=records,
            direct_matches=sum(not r['differences'] for r in records)))

    def test_every_slot_lazy_gate_full_memory_and_ordered_events(self):
        coverage, count = set(), 0
        for slot, kind, valid, found, found_valid, phase in itertools.product(
                range(256), range(4), (0, 0xFFFFFFFF), (0, FOUND, CANDIDATE), (0, 0x80000000), (0, 8)):
            if slot == 255 and kind == 0:
                continue
            memory, args = fixture(slot, kind, valid, found, found_valid)
            answer, after, events, calls = reference(memory, args, found)
            for model in self.models(memory, args, phase=phase, found=found):
                self.assertEqual(model.r[2], answer)
                self.assertEqual(external_events(model), events)
                self.assertEqual(model.calls, calls)
                self.assertEqual({a: b for a, b in model.memory.items() if not STACK - 0x100 <= a < STACK + 0x100},
                    {a: b for a, b in after.items() if not STACK - 0x100 <= a < STACK + 0x100})
                coverage.update(model.visits)
            count += 1
        self.assertEqual(count, 24552)
        self.assertEqual(set(range(screen.ENTRY, screen.ENTRY + 176, 4)) - coverage, {screen.ENTRY + 0x9C})
        self.receipt('guest', dict(cases=count, words_covered=43, unreachable_word='151424E0',
            independent_reference=True, full_memory_registers_events_equal=True, helper='bounded model'))

    def test_lookup_return_validity_is_live_after_callback_and_may_alias_candidate(self):
        count = 0
        for found, mutation, phase in itertools.product((CANDIDATE, FOUND), (0, 0xFFFFFFFF), (0, 8)):
            memory, args = fixture(7, kind=3, valid=0x80000000, found=found)
            answer, after, events, calls = reference(memory, args, found, mutation)
            for model in self.models(memory, args, found=found, mutation=mutation, phase=phase):
                self.assertEqual(model.r[2], answer)
                self.assertEqual(external_events(model), events)
                self.assertEqual(model.calls, calls)
                self.assertEqual(read(model.memory, found + 0x1D4), read(after, found + 0x1D4))
            count += 1
        self.receipt('callbacks', dict(cases=count, post_callback_validity=True, result_may_alias_candidate=True))

    def test_unmapped_required_bytes_fail_closed_and_unused_fields_are_lazy(self):
        for slot, kind, missing, fails in ((255, 2, CANDIDATE, False),
                (7, 1, CANDIDATE + 0x3B, False), (7, 2, CANDIDATE + 0x1D4, True),
                (7, 3, FOUND + 0x1D4, True), (255, 2, CANDIDATE + 0x1D4, True)):
            memory, args = fixture(slot, kind)
            del memory[missing]
            if fails:
                for words in (self.words, self.retail):
                    with self.assertRaisesRegex(AssertionError, 'unmapped'):
                        LookupOracle(words, memory, args).run()
            else:
                self.models(memory, args)
        memory, args = fixture(255, kind=0)
        for words in (self.words, self.retail):
            with self.assertRaisesRegex(AssertionError, 'unmapped'):
                LookupOracle(words, memory, args).run()

    def test_complete_original_lookup_search_all_slots_and_scan_positions(self):
        connected = dict(zip(range(LOOKUP, LOOKUP + 288, 4), self.lookup))
        coverage, count = set(), 0
        for slot, hit, active, valid, phase in itertools.product(
                range(26), (0, 1, 2, 3, 4, 5, 6, 25), (False, True), (0, 0xFFFFFFFF), (0, 8)):
            memory, args = fixture(slot, kind=0)
            memory.update({ACTORS + i: 0xA5 for i in range(26 * STRIDE)})
            for index in range(26):
                put(memory, ACTORS + index * STRIDE, 0x80000000 if active else 0)
                put(memory, ACTORS + index * STRIDE + 0x3B, slot if index == hit - 1 else (slot + 1) & 255, 1)
                put(memory, ACTORS + index * STRIDE + 0x1D4, valid)
            wanted = ACTORS + (hit - 1) * STRIDE if slot and hit and active and valid else 0
            for model in self.models(memory, args, phase=phase, connected=connected):
                self.assertEqual(model.r[2], wanted, (slot, hit, active, valid))
                self.assertEqual(model.calls, [(LOOKUP, slot)])
                self.assertFalse(any(e[0] == 'W' and not STACK - 0x100 <= e[1] < STACK + 0x100 for e in model.events))
                coverage.update(model.visits)
            count += 1
        helper_missing = set(range(LOOKUP, LOOKUP + 288, 4)) - coverage
        self.assertEqual(helper_missing, {0x15083F08, 0x15083F2C, 0x15083F50, 0x15083F74})
        targets = set()
        for index, word in enumerate(self.lookup):
            if word >> 26 in (4, 5, 20, 21):
                imm = word & 65535
                offset = imm if imm < 32768 else imm - 65536
                targets.add(LOOKUP + index * 4 + 4 + offset * 4)
        for address in helper_missing:
            index = (address - LOOKUP) // 4
            self.assertEqual(self.lookup[index - 2], 0x03E00008)
            self.assertEqual(self.lookup[index - 1], 0x00601025)
            self.assertNotIn(address, targets)
        self.assertEqual(count, 1664)
        self.receipt('connected', dict(cases=count, original_helper_words=72, reachable_helper_words=68,
            unreachable_return_tail_loads=sorted(helper_missing),
            independent_scan_result=True, full_memory_registers_events_equal=True,
            helper_source_still_placeholder=True))

    def test_actual_native_32_bit_typed_caller_with_all_byte_slots(self):
        self.fixture = '''typedef unsigned char u8;typedef unsigned int u32;typedef int s32;
#define NULL ((void *)0)
static union {u32 alignment;u8 bytes[512];} candidate,foundRecord;
static u8 *lookupResult;static int calls;static u32 calledSlot;
u8 *func_15083E90(u8 slot) {calls++;calledSlot=slot;return lookupResult;}
''' + screen.SELECTED + '\n'
        self.run_host(r'''
int slot,kind,valid,found,foundValid,i,count=0,wantCalls;u8 *arg,*want;u8 saved[1024];
for(slot=0;slot<256;slot++)for(kind=0;kind<4;kind++)for(valid=0;valid<2;valid++)
for(found=0;found<3;found++)for(foundValid=0;foundValid<2;foundValid++) {
    if(slot==255 && kind==0)continue;
    for(i=0;i<512;i++){candidate.bytes[i]=(u8)(i*31+7);foundRecord.bytes[i]=(u8)(i*17+13);}
    *(u32 *)candidate.bytes=kind==1?0:0x80000000u;
    candidate.bytes[0x3B]=(u8)(slot+(kind==3));
    *(u32 *)(candidate.bytes+0x1D4)=valid?0xFFFFFFFFu:0;
    *(u32 *)(foundRecord.bytes+0x1D4)=foundValid?0x80000000u:0;
    for(i=0;i<512;i++){saved[i]=candidate.bytes[i];saved[i+512]=foundRecord.bytes[i];}
    arg=kind==0?NULL:candidate.bytes;
    lookupResult=found==0?NULL:found==1?foundRecord.bytes:candidate.bytes;
    wantCalls=slot!=255 && kind!=2;
    want=wantCalls?lookupResult:arg;
    if(want && !*(u32 *)(want+0x1D4))want=NULL;
    calls=0;calledSlot=0xFFFFFFFFu;
    if(func_15142444((u8)(0xABCD0000u|(u32)slot),arg)!=want)return 1;
    if(calls!=wantCalls || (calls && calledSlot!=(u32)slot))return 2;
    for(i=0;i<512;i++)if(saved[i]!=candidate.bytes[i] || saved[i+512]!=foundRecord.bytes[i])return 3;
    count++;
}
if(count!=12276 || sizeof(void *)!=4)return 4;
''')
        self.receipt('native', dict(cases=12276, bits=32, typed_byte_caller=True,
            complete_readonly_records=True, lookup='bounded C model, not recovered helper source'))

    def test_effective_compiled_negatives_change_results_or_lazy_reads(self):
        forms = {
            'full-selector': screen.SELECTED.replace('u8 arg0', 'u32 arg0'),
            'wrong-sentinel': screen.SELECTED.replace('arg0 == 0xFF', 'arg0 == 0xFE'),
            'ignore-live-word': screen.SELECTED.replace('(*(s32 *)arg1 != 0)', '1'),
            'wrong-identity': screen.SELECTED.replace('arg1[0x3B]', 'arg1[0x3A]'),
            'wrong-validity': screen.SELECTED.replace('+ 0x1D4', '+ 0x1D8'),
            'ignore-found-validity': screen.SELECTED.replace('*(s32 *)(found + 0x1D4) != 0', '1'),
        }
        cases = [(255, 3, 1, FOUND, 0), (7, 1, 1, FOUND, 0), (7, 2, 0, FOUND, 1), (7, 3, 1, FOUND, 0)]
        changes = {}
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root, self.out, name, body)
            changes[name] = 0
            for slot, kind, valid, found, found_valid in cases:
                memory, args = fixture(slot, kind, valid, found, found_valid)
                answer, _, events, calls = reference(memory, args, found)
                model = LookupOracle(words, memory, args, found=found).run()
                changes[name] += (model.r[2], external_events(model), model.calls) != (answer, events, calls)
            self.assertGreater(changes[name], 0, name)
        self.receipt('negatives', changes)

    def copied_owner(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        baseline = source.replace(HEADER_OVERRIDE, '').replace(HEADER_END, '').replace(screen.SELECTED, screen.BASELINE)
        self.assertEqual(baseline.count(screen.BASELINE), 1)
        selected = baseline.replace('#include "functions.h"\n',
            HEADER_OVERRIDE + '#include "functions.h"\n' + HEADER_END)
        selected = selected.replace(screen.BASELINE, screen.SELECTED)
        old, old_warnings = compile_owner(self.root, self.out, baseline, 'owner-baseline')
        new, warnings = compile_owner(self.root, self.out, selected, 'owner-selected')
        self.assertEqual(warnings, old_warnings)
        self.assertEqual(len(warnings), 2)
        processed = []
        for name, obj in (('owner-baseline', old), ('owner-selected', new)):
            final = self.out / (name + '-postprocessed.o')
            shutil.copyfile(obj, final)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'),
                '-O2', '-g3', str((self.out / (name + '.c')).relative_to(self.root / 'conker')),
                '--post-process', str(final.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker',
                check=True, capture_output=True)
            processed.append(final)
        old, new = processed
        old_text, old_functions, old_relocations = parse_object(old)
        text, functions, relocations = parse_object(new)
        self.assertEqual(set(functions), set(old_functions))
        self.assertEqual(len(functions), 89)
        for name, current in functions.items():
            if name == screen.FUNCTION:
                continue
            prior = old_functions[name]
            self.assertEqual(text[current['value']:current['value'] + current['size']],
                old_text[prior['value']:prior['value'] + prior['size']], name)
            self.assertEqual({o - current['value']: r for o, r in relocations.items()
                if current['value'] <= o < current['value'] + current['size']},
                {o - prior['value']: r for o, r in old_relocations.items()
                if prior['value'] <= o < prior['value'] + prior['size']}, name)
        self.assertEqual(normalized_pools(old), normalized_pools(new))
        target = functions[screen.FUNCTION]
        self.assertEqual(target['size'], 176)
        standalone, _, _ = parse_object(self.out / 'selected.o')
        self.assertEqual(text[target['value']:target['value'] + 176], standalone[:176])
        self.assertEqual({o - target['value']: r for o, r in relocations.items()
            if target['value'] <= o < target['value'] + 176}, self.record['relocations'])
        self.receipt('owner', dict(functions=89, unchanged_neighbors=88, warnings=2, normalized_pools_unchanged=True))
        return new

    def test_copied_owner_and_actual_padder_retain_direct_slot_and_rebase_helper(self):
        owner = self.copied_owner()
        assembly = emit_padded_assembly(owner, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=self.root / 'conker/retail_word_patches.us.csv')
        begin = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), begin)
        body = assembly[begin:assembly.index('\n', end) + 1]
        self.assertEqual(len(re.findall(r'\.word 0x[0-9A-F]{8}', body)), 44)
        self.assertNotIn('__retail_overflow_' + screen.FUNCTION, assembly)
        source, obj, elf = (self.out / ('padded' + suffix) for suffix in ('.s', '.o', '.elf'))
        source.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + body)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(source)],
            check=True, capture_output=True)
        _, functions, relocations = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'], 176)
        self.assertEqual(relocations, self.record['relocations'])
        for address in (LOOKUP, LOOKUP + 0x100000):
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'lookup.ld'),
                '-e', screen.FUNCTION, '--defsym=func_15083E90=0x%X' % address,
                '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = self.retail.copy()
            expected[0x78 // 4] = 0x0C000000 | (address >> 2 & 0x3FFFFFF)
            self.assertEqual(list(struct.unpack_from('>44I', screen.sections(elf)['.text'][1])), expected)

    def test_installed_source_linked_target_and_unchanged_guards(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertEqual(source.count(screen.SELECTED), 1)
        self.assertEqual(source.count(HEADER_OVERRIDE), 1)
        self.assertEqual(source.count(HEADER_END), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))

    def test_removed_overflow_only_rebases_the_following_trampoline(self):
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertNotIn('__retail_overflow_' + screen.FUNCTION, functions)
        tail, caller = '__retail_overflow_func_151F2E88', 'func_151F2E88'
        self.assertEqual(addresses[tail], 0x15F00D94)
        self.assertEqual(len(functions[tail]), 739)
        self.assertEqual(hashlib.sha256(struct.pack('>739I', *functions[tail])).hexdigest(),
            '1a0a94032d9d1709e7c3c9c45f8819a1179338695d0bced6c8bbc7c823b218bd')
        self.assertEqual(functions[caller][0], 0x08000000 | (addresses[tail] >> 2 & 0x3FFFFFF))
        self.assertEqual(len(functions[caller]), 727)
        self.assertFalse(any(functions[caller][1:]))
        baseline = functions[caller].copy()
        baseline[0] = 0x08000000 | (0x15F00E4C >> 2 & 0x3FFFFFF)
        self.assertEqual(hashlib.sha256(struct.pack('>727I', *baseline)).hexdigest(),
            '1c4222c729a12e92c7acbc5195c941dd84640b33f468a106517f8656b86877e0')


if __name__ == '__main__':
    unittest.main()
