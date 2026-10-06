"""Recover the retail pair-clamp access trace without claiming a frame/byte match."""

import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_integer_pair_clamp_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import signed
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native


ENTRY = screen.ENTRY
BUFFER = 0x20000
VALUES = (0x80000000, 0xFFFFFF9C, 0xFFFFFFFF, 0, 1, 100, 0x7FFFFFFF, 0x40000000)
POINTERS = ((BUFFER + 4, BUFFER + 8), (BUFFER + 8, BUFFER + 4), (BUFFER + 4, BUFFER + 4))


def memory_case(pointers, a, b):
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({BUFFER + i: 0xA5 for i in range(24)})
    put(memory, pointers[0], a)
    put(memory, pointers[1], b)
    return memory


def external(memory):
    return {a: v for a, v in memory.items() if not STACK - 0x600 <= a < STACK + 0x100}


def reference(memory, pointers, lower, upper):
    memory, events = dict(memory), []
    lower, upper = sorted((signed(lower), signed(upper)))

    def read(address):
        value = int.from_bytes(bytes(memory[address + i] for i in range(4)), 'big')
        events.append(('R', address, 4, value))
        return value

    def write(address, value):
        value &= 0xFFFFFFFF
        put(memory, address, value)
        events.append(('W', address, 4, value))

    a, b = pointers
    right, left = read(b), read(a)
    if signed(right) < signed(left):
        difference = left ^ right
        write(a, difference)
        right = read(b) ^ difference
        write(b, right)
        left = read(a) ^ right
        write(a, left)
    if signed(left) < lower:
        write(a, lower)
    right = read(b)
    if upper < signed(right):
        write(b, upper)
    return external(memory), events


class PairOracle(TriangleOracle):
    def __init__(self, words, memory, pointers, lower, upper, phase=0):
        super().__init__(words, memory, entry=ENTRY, arguments=(*pointers, lower, upper), phase=phase)

    def execute(self, word):
        if word >> 26 == 0 and word & 63 == 38:
            rs, rt, rd = word >> 21 & 31, word >> 16 & 31, word >> 11 & 31
            self.r[rd] = self.r[rs] ^ self.r[rt]
            self.r[0] = 0
        else:
            super().execute(word)

    def record_call(self, target):
        raise AssertionError('pair clamp unexpectedly calls a helper')


def events(model):
    return [event for event in model.events if not STACK - 0x600 <= event[1] < STACK + 0x100]


class GameIntegerPairClampRecoveryTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-integer-pair-clamp-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.old_record, cls.old = screen.compile_candidate(cls.root, cls.output, 'baseline', screen.BASELINE)
        cls.retail = list(struct.unpack_from('>36I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = screen.TYPES + screen.SELECTED + '\n'

    def test_source_shape_and_nonmatching_length_are_explicit(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['diagnostics']), (29, 0, 36, ''))
        self.assertEqual((self.old_record['body_words'], self.old_record['frame'], self.old_record['differences']),
                         (24, 0, 36))
        self.assertFalse(self.record['exact'])
        self.assertNotEqual(self.words, self.retail)
        self.assertEqual(self.words[-2:], [0x03E00008, 0])

    def test_source_profile_inventory_is_bounded(self):
        forms = screen.candidates()
        self.assertEqual((len(forms), len(dict(forms))), (23, 23))
        for name, body in forms:
            record, _ = screen.compile_candidate(self.root, self.output, name, body)
            self.assertFalse(record['exact'])
            self.assertEqual(record['differences'], 36)
            self.assertEqual(record['frame'], 0)
            self.assertEqual(record['diagnostics'], '')

    def test_separate_parameter_and_local_register_hints_do_not_recover_frame(self):
        forms = screen.register_lifetimes()
        self.assertEqual((len(forms), len(dict(forms))), (64, 64))
        shapes, cases = {}, 0
        corners = ((100, 1, 0, 100, 0), (0x80000000, 0x7FFFFFFF, 0x7FFFFFFF, 0x80000000, 1),
                   (100, 100, 0, 1, 0), (0xFFFFFF9C, 0xFFFFFFFF, 0, 1, 0),
                   (100, 1, 0, 100, 2), (0x80000000, 0x7FFFFFFF, 0x80000000, 0x7FFFFFFF, 0))
        for name, body in forms:
            locals_mask = int(name[-1], 16)
            for profile in ('o2g3', 'o1g3'):
                record, words = screen.compile_candidate(self.root, self.output, name + '-' + profile, body, profile)
                self.assertFalse(record['exact'])
                self.assertEqual(record['diagnostics'], '')
                if profile == 'o2g3':
                    self.assertEqual(words, self.words)
                    self.assertEqual((record['body_words'], record['frame'], record['differences']), (29, 0, 36))
                else:
                    size = (50, 47, 46, 40)[locals_mask]
                    self.assertEqual((record['body_words'], record['frame'], record['differences']), (size, 0x20, size))
                key = (profile, locals_mask)
                if key in shapes:
                    self.assertEqual(words, shapes[key])
                else:
                    shapes[key] = words
                for a, b, lower, upper, mode in corners:
                    pointers = POINTERS[mode]
                    memory = memory_case(pointers, a, b)
                    wanted, trace = reference(memory, pointers, lower, upper)
                    for phase in (0, 8):
                        model = PairOracle(words, memory, pointers, lower, upper, phase).run()
                        self.assertEqual(external(model.memory), wanted)
                        self.assertEqual(events(model), trace)
                        self.assertEqual(model.calls, [])
                        cases += 1
        self.assertEqual(cases, 1536)

    def test_core_opcodes_delays_and_immediates_match_under_lifetime_renaming(self):
        renames = {3: {'rd': 5}, 4: {'rs': 5}, 5: {'rt': 5}, 6: {'rs': 16, 'rt': 3},
                   7: {'rs': 17, 'rt': 5}, 8: {'rs': 3, 'rt': 5}, 10: {'rs': 5, 'rt': 3, 'rd': 2},
                   11: {'rs': 17, 'rt': 2}, 12: {'rs': 16}, 13: {'rt': 2, 'rd': 4},
                   14: {'rs': 16, 'rt': 4}, 15: {'rs': 17}, 16: {'rt': 4, 'rd': 5},
                   17: {'rs': 17, 'rt': 5}, 18: {'rs': 5}, 20: {'rs': 16, 'rt': 25},
                   21: {'rs': 17}, 22: {'rs': 16, 'rt': 25}, 23: {'rt': 25}}
        core = self.words[:24]
        for index, changes in renames.items():
            word = core[index]
            for field, register in changes.items():
                shift = {'rs': 21, 'rt': 16, 'rd': 11}[field]
                word = (word & ~(31 << shift)) | register << shift
            core[index] = word
        self.assertEqual(core, self.retail[5:29])
        self.assertEqual(self.retail[:5], [0x27BDFFF0, 0xAFB1000C, 0xAFB00008, 0x00A08025, 0x00808825])
        self.assertNotEqual(self.words[24:], self.retail[29:])

    def test_complete_guest_access_trace_and_old_body_final_outputs(self):
        coverage, cases, old_trace_differences = set(), 0, 0
        for a, b, lower, upper, pointers, phase in itertools.product(VALUES, VALUES, VALUES, VALUES, POINTERS, (0, 8)):
            memory = memory_case(pointers, a, b)
            wanted, trace = reference(memory, pointers, lower, upper)
            for words in (self.retail, self.words):
                model = PairOracle(words, memory, pointers, lower, upper, phase).run()
                self.assertEqual(external(model.memory), wanted)
                self.assertEqual(events(model), trace)
                self.assertEqual(model.calls, [])
                if words is self.retail:
                    coverage.update(model.visits)
            old = PairOracle(self.old, memory, pointers, lower, upper, phase).run()
            self.assertEqual(external(old.memory), wanted)
            old_trace_differences += events(old) != trace
            cases += 1
        self.assertEqual(cases, 24576)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 144, 4)))
        self.assertEqual(old_trace_differences, 7168)
        (self.output / 'behavior.json').write_text(json.dumps(dict(cases=cases, models=3,
             retail_words=len(coverage), old_trace_differences=old_trace_differences,
             raw_body_words=29, byte_exact=False), indent=2) + '\n')

    def test_native_actual_c_signed_extrema_reverse_and_equal_pointers(self):
        self.run_host(r'''
static u32 values[]={0x80000000,0xFFFFFF9C,0xFFFFFFFF,0,1,100,0x7FFFFFFF,0x40000000};
u32 storage[6],expected[6];
int a,b,l,u,mode,i;
for(a=0;a<8;a++) for(b=0;b<8;b++) for(l=0;l<8;l++) for(u=0;u<8;u++) for(mode=0;mode<3;mode++) {
    int x=mode==1?2:1,y=mode==0?2:1;
    s32 low=(s32)values[l],high=(s32)values[u],left,right,temp;
    for(i=0;i<6;i++) storage[i]=0xA5A5A5A5;
    storage[x]=values[a];storage[y]=values[b];
    for(i=0;i<6;i++) expected[i]=storage[i];
    if(high<low) {temp=low;low=high;high=temp;}
    left=(s32)expected[x];right=(s32)expected[y];
    if(right<left) {expected[x]=(u32)right;expected[y]=(u32)left;left=right;}
    if(left<low) expected[x]=(u32)low;
    if(high<(s32)expected[y]) expected[y]=(u32)high;
    func_15143D18((s32 *)(storage+x),(s32 *)(storage+y),(s32)values[l],(s32)values[u]);
    for(i=0;i<6;i++) if(storage[i]!=expected[i]) return 1;
}
''')

    def test_original_temporary_swap_and_wrong_clamps_are_detected(self):
        pointers = POINTERS[0]
        memory = memory_case(pointers, 100, 1)
        wanted, trace = reference(memory, pointers, 0, 100)
        old = PairOracle(self.old, memory, pointers, 0, 100).run()
        self.assertEqual(external(old.memory), wanted)
        self.assertNotEqual(events(old), trace)
        for name, body, a, b, low, high in (
                ('no-xor-swap', screen.SELECTED.replace('    if (value1 < value0)', '    if (0)'), 100, 1, 0, 100),
                ('no-bound-swap', screen.SELECTED.replace('    if (arg3 < arg2)', '    if (0)'), 1, 100, 100, 0),
                ('clamp-both-ends', screen.SELECTED.replace('    if (arg3 < *ptr1)',
                   '    if (arg3 < *ptr0) { *ptr0 = arg3; }\n    if (arg3 < *ptr1)'), 100, 100, 0, 1)):
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            memory = memory_case(pointers, a, b)
            expected, _ = reference(memory, pointers, low, high)
            model = PairOracle(words, memory, pointers, low, high).run()
            self.assertNotEqual(external(model.memory), expected)

    def test_production_source_slot_padding_no_guards_and_unchanged_signature(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertEqual(re.search(r'^void func_15143D18\([^;{]+\) \{\n.*?\n\}', source, re.M | re.S).group(), screen.SELECTED)
        functions = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        self.assertEqual(functions['func_15143D18'], self.words + [0] * 7)
        self.assertNotIn(',func_15143D18,', (self.root / 'conker/retail_word_patches.us.csv').read_text())
        self.assertEqual(screen.SELECTED.splitlines()[0], screen.BASELINE.splitlines()[0])
        self.assertNotIn('func_15143D18(', (self.root / 'conker/include/functions.h').read_text())


if __name__ == '__main__':
    unittest.main()
