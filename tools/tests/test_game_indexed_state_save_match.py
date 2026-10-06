"""Sequential indexed state saves, opaque mutation and connected bit selection."""

import csv
import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_indexed_state_save_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native


ENTRY, CALLBACK = screen.ENTRY, screen.CALLBACK
ACTOR, FIRST, END = 0x20000, 0x1FD00, 0x20B00
INDICES = (*range(21), -1, -2, -21, 21, 22, 43, 65, 128, -128, 0x80000000, 0x80000001)
GATES = (0, 1, 0x7FFF, 0x8000, 0xFFFE, 0xFFFF)
VALUES = (0, 0xFFFFFFFF, 0x80000000, 0x7FFFFFFF, 0x81234560)
MASKS = (*[1 << i for i in range(32)], 3, 0x80000001, 0xFFFFFFFE, 0x80008000, 0xFFFFFFFF)


def address(offset, index=0, scale=0):
    return (ACTOR + offset + index * scale) & 0xFFFFFFFF


def get(memory, location, size):
    return int.from_bytes(bytes(memory[location + i] for i in range(size)), 'big')


def external(memory):
    return {a: v for a, v in memory.items() if not STACK - 0x600 <= a < STACK + 0x100}


def memory_case(index=0, gate=0, pattern=0):
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({a: (a * 17 + pattern * 53) & 255 for a in range(FIRST, END)})
    put(memory, ACTOR, (0, 1, 0x7FFF, 0x8000, 0xFFFF)[pattern], 2)
    for offset, value in ((0x2C, 0x12345678), (0x84, 0x87654321), (0xDC, 0x80000001), (0x134, 0xFEDCBA98)):
        put(memory, ACTOR + offset, value ^ (pattern * 0x11111111))
    put(memory, ACTOR + 0x1B4, (0, 1, 0x7FFF, 0x8000, 0xFFFF)[pattern], 2)
    put(memory, ACTOR + 0x1E0, (0xFFFF, 0x8000, 0x7FFF, 1, 0)[pattern], 2)
    put(memory, address(0x20C, index, 2), gate, 2)
    return memory


def changes(index, mode):
    return [] if not mode else [(ACTOR, 0xFFFF, 2), (ACTOR + 0x2C, 0x87654321, 4)] if mode == 1 else [
        (address(0x20C, index, 2), 0, 2), (ACTOR + 0xDC, 0x55555555, 4),
        (ACTOR + 0x134, 0xAAAAAAAA, 4)] if mode == 2 else [
        (address(2, index, 2), 0xABCD, 2), (address(0x30, index, 4), 0x76543210, 4),
        (address(0x1B6, index, 2), 0x8000, 2)]


def reference(memory, index, arguments, mutation=0, connected=False):
    memory, events, calls = dict(memory), [], []

    def read(location, size):
        value = get(memory, location, size)
        events.append(('R', location, size, value))
        return value

    def write(location, value, size):
        put(memory, location, value, size)
        events.append(('W', location, size, value & ((1 << (size * 8)) - 1)))

    if read(address(0x20C, index, 2), 2):
        return external(memory), calls, events, 0
    write(address(2, index, 2), read(ACTOR, 2), 2)
    for source, destination in ((0x2C, 0x30), (0x84, 0x88), (0xDC, 0xE0), (0x134, 0x138)):
        write(address(destination, index, 4), read(ACTOR + source, 4), 4)
    for source, destination in ((0x1B4, 0x1B6), (0x1E0, 0x1E2)):
        write(address(destination, index, 2), read(ACTOR + source, 2), 2)
    for destination, value in zip((0x2C, 0xDC, 0x134), arguments):
        write(ACTOR + destination, value, 4)
    write(address(0x20C, index, 2), 1, 2)
    snapshot = bytes(memory[a] for a in range(FIRST, END))
    calls.append((CALLBACK, ACTOR, snapshot))
    events.append(('CALL', CALLBACK, ACTOR))
    if connected:
        mask = read(ACTOR + 0x2C, 4)
        assert mask
        write(ACTOR, (mask & -mask).bit_length() - 1, 2)
    else:
        for location, value, size in changes(index, mutation):
            write(location, value, size)
    return external(memory), calls, events, 1


class StateSaveOracle(TriangleOracle):
    def __init__(self, words, memory, index=0, arguments=(1, 2, 3), mutation=0, phase=0, callback=None):
        code = {CALLBACK + i * 4: word for i, word in enumerate(callback or [])}
        super().__init__(words, memory, entry=ENTRY, arguments=(ACTOR, *arguments, index & 0xFFFFFFFF),
                         phase=phase, connected=code)
        self.index, self.mutation = index, mutation

    def execute(self, word):
        if word >> 26 == 33:
            rs, rt, immediate = word >> 21 & 31, word >> 16 & 31, word & 65535
            location = (self.r[rs] + (immediate if immediate < 32768 else immediate - 65536)) & 0xFFFFFFFF
            value = self.get(location, 2)
            self.r[rt] = value if value < 0x8000 else value | 0xFFFF0000
        else:
            super().execute(word)

    def record_call(self, target):
        assert target == CALLBACK and self.r[4] == ACTOR
        snapshot = bytes(self.memory[a] for a in range(FIRST, END))
        self.calls.append((target, ACTOR, snapshot))
        self.events.append(('CALL', target, ACTOR))

    def hook(self, target):
        for location, value, size in changes(self.index, self.mutation):
            self.put(location, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]


def events(model):
    return [event for event in model.events if event[0] == 'CALL' or not
            STACK - 0x600 <= event[1] < STACK + 0x100]


class GameIndexedStateSaveMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-indexed-state-save-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.other_record, cls.other = screen.compile_candidate(cls.root, cls.output, 'no-debug', profile='o2')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>38I', rom, screen.ROM))
        cls.callback = list(struct.unpack_from('>14I', rom, 0x152844))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = screen.TYPES + r'''
static u32 storage[256],expected[256],snapshot[256];
static struct108 *actor;
static int calls,mode,index;
void func_15125394(struct108 *value) {
    int i;
    s16 *s=(s16 *)actor+index;
    s32 *w=(s32 *)actor+index;
    if(value!=actor) calls=99;
    calls++;
    for(i=0;i<256;i++) snapshot[i]=storage[i];
    if(mode==1) {actor->unk0=0xFFFF;actor->unk2C=(s32)0x87654321;}
    if(mode==2) {s[0x106]=0;actor->unkDC=0x55555555;actor->unk134=(s32)0xAAAAAAAA;}
    if(mode==3) {((u16 *)s)[1]=0xABCD;w[0xC]=0x76543210;s[0xDB]=(s16)0x8000;}
}
''' + screen.SELECTED + '\n'

    def compare(self, memory, index, arguments, mutation=0, phase=0, connected=False):
        wanted, calls, trace, result = reference(memory, index, arguments, mutation, connected)
        coverage = set()
        for words in (self.retail, self.words, self.other):
            model = StateSaveOracle(words, memory, index, arguments, mutation, phase,
                                    self.callback if connected else None).run()
            self.assertEqual(external(model.memory), wanted)
            self.assertEqual(model.calls, calls)
            self.assertEqual(events(model), trace)
            self.assertEqual(model.r[2], result)
            if words is self.retail:
                coverage.update(model.visits)
        return coverage

    def test_existing_profile_and_plain_o2_control(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['diagnostics']), (38, 0x18, 0, ''))
        self.assertEqual(self.words, self.retail)
        self.assertEqual((self.other_record['body_words'], self.other_record['frame'],
                          self.other_record['differences']), (38, 0x18, 2))

    def test_named_source_and_profile_inventory(self):
        expected = {'halfword-pointer': (38, 0), 'unsigned-slot': (38, 1),
                    'named-word-pointer': (38, 0), 'field-gate': (40, 34),
                    'explicit-byte-offset': (38, 0), 'register-index': (38, 0),
                    'early-return': (38, 30), 'direct-saved-id': (39, 30)}
        self.assertEqual((len(screen.candidates()), len(dict(screen.candidates()))), (8, 8))
        for name, body in screen.candidates():
            record, _ = screen.compile_candidate(self.root, self.output, name, body)
            self.assertEqual((record['body_words'], record['differences']), expected[name])
            self.assertEqual(record['diagnostics'], '')

    def test_indexed_slots_gate_bits_callbacks_and_sequential_overlaps(self):
        coverage, cases = set(), 0
        for index, gate, pattern, phase, mutation in itertools.product(INDICES, GATES, range(5), (0, 8), range(4)):
            value = VALUES[pattern]
            arguments = (value, value ^ 0x89ABCDEF, ((value << 7) | (value >> 25)) & 0xFFFFFFFF)
            coverage.update(self.compare(memory_case(index, gate, pattern), index, arguments, mutation, phase))
            cases += 1
        self.assertEqual(cases, 7680)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 152, 4)))
        (self.output / 'behavior.json').write_text(json.dumps(dict(cases=cases, models=3,
             wrapper_words=len(coverage), bounded_index_patterns=len(INDICES)), indent=2) + '\n')

    def test_connected_retail_bit_selector_all_positions_and_blocked_slots(self):
        coverage, cases = set(), 0
        for index, mask, gate, phase in itertools.product(INDICES, MASKS, (0, 0xFFFF), (0, 8)):
            coverage.update(self.compare(memory_case(index, gate), index, (mask, 0x80000000, 0x81234560),
                                         phase=phase, connected=True))
            cases += 1
        self.assertEqual(cases, 4736)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 152, 4)) | set(range(CALLBACK, CALLBACK + 56, 4)))
        (self.output / 'connected.json').write_text(json.dumps(dict(cases=cases, wrapper_words=38,
             retail_callback_words=14, nonzero_mask_patterns=len(MASKS)), indent=2) + '\n')

    def test_zero_mask_connected_prefix_preserves_writes_without_return(self):
        for index, phase in itertools.product((0, 20, 21), (0, 8)):
            memory = memory_case(index)
            wanted, calls, _, _ = reference(memory, index, (0, 0x80000000, 0x81234560))
            for words in (self.retail, self.words, self.other):
                model = StateSaveOracle(words, memory, index, (0, 0x80000000, 0x81234560),
                                        phase=phase, callback=self.callback)
                with self.assertRaisesRegex(AssertionError, 'instruction budget exhausted'):
                    model.run()
                self.assertEqual(external(model.memory), wanted)
                self.assertEqual(model.calls, calls)
                self.assertNotIn(CALLBACK + 0x2C, model.visits)
                self.assertNotIn(CALLBACK + 0x30, model.visits)


    def test_native_32bit_prefix_layout_full_footprint_and_callback_snapshot(self):
        self.run_host(r'''
u16 gates[]={0,1,0x7FFF,0x8000,0xFFFE,0xFFFF};
u16 halves[]={0,1,0x7FFF,0x8000,0xFFFF};
u32 values[]={0,0xFFFFFFFF,0x80000000,0x7FFFFFFF,0x81234560};
int g,p,m,i,result;
u8 *base,*copy;
actor=(struct108 *)(storage+64);base=(u8 *)actor;copy=(u8 *)(expected+64);
if(sizeof(void *)!=4 || (u8 *)&actor->unk2C-base!=0x2C || (u8 *)&actor->unk84-base!=0x84
 || (u8 *)&actor->unkDC-base!=0xDC || (u8 *)&actor->unk134-base!=0x134
 || (u8 *)&actor->unk1B4-base!=0x1B4 || (u8 *)&actor->unk1E0-base!=0x1E0
 || (u8 *)actor->unk20C-base!=0x20C) return 1;
for(index=0;index<21;index++) for(g=0;g<6;g++) for(p=0;p<5;p++) for(m=0;m<4;m++) {
    u32 a=values[p],b=a^0x89ABCDEF,c=(a<<7)|(a>>25);
    int offsets[]={0x2C,0x84,0xDC,0x134};
    int targets[]={0x30,0x88,0xE0,0x138};
    for(i=0;i<256;i++) storage[i]=0xA5A5A5A5^(i*0x10203u);
    actor->unk0=halves[p];actor->unk2C=0x12345678;actor->unk84=(s32)0x87654321;
    actor->unkDC=(s32)0x80000001;actor->unk134=(s32)0xFEDCBA98;
    actor->unk1B4=(s16)halves[p];actor->unk1E0=(s16)halves[4-p];actor->unk20C[index]=gates[g];
    for(i=0;i<256;i++) expected[i]=storage[i];
    if(!gates[g]) {
        *(u16 *)(copy+2+index*2)=*(u16 *)copy;
        for(i=0;i<4;i++) *(u32 *)(copy+targets[i]+index*4)=*(u32 *)(copy+offsets[i]);
        *(u16 *)(copy+0x1B6+index*2)=*(u16 *)(copy+0x1B4);
        *(u16 *)(copy+0x1E2+index*2)=*(u16 *)(copy+0x1E0);
        *(u32 *)(copy+0x2C)=a;*(u32 *)(copy+0xDC)=b;*(u32 *)(copy+0x134)=c;
        *(u16 *)(copy+0x20C+index*2)=1;
    }
    calls=0;mode=m;
    result=func_15123934(actor,(s32)a,(s32)b,(s32)c,index);
    if(result!=!gates[g] || calls!=!gates[g]) return 2;
    if(!gates[g]) {
        for(i=0;i<256;i++) if(snapshot[i]!=expected[i]) return 3;
        if(m==1) {*(u16 *)copy=0xFFFF;*(u32 *)(copy+0x2C)=0x87654321;}
        if(m==2) {*(u16 *)(copy+0x20C+index*2)=0;*(u32 *)(copy+0xDC)=0x55555555;*(u32 *)(copy+0x134)=0xAAAAAAAA;}
        if(m==3) {*(u16 *)(copy+2+index*2)=0xABCD;*(u32 *)(copy+0x30+index*4)=0x76543210;*(u16 *)(copy+0x1B6+index*2)=0x8000;}
    }
    for(i=0;i<256;i++) if(storage[i]!=expected[i]) return 4;
}
''')

    def test_wrong_stride_early_install_late_mark_and_old_stub_are_detected(self):
        forms = [('old-stub', 's32 func_15123934(struct108 *arg0,s32 a,s32 b,s32 c,s32 i) { return 0; }'),
                 ('wrong-stride', screen.SELECTED.replace('(s16 *) arg0 + arg4', '(s16 *) arg0 + arg4 * 2')),
                 ('early-install', screen.SELECTED.replace('        ((u16 *) slot16)[1] = arg0->unk0;',
                                                           '        arg0->unk2C = arg1;\n        ((u16 *) slot16)[1] = arg0->unk0;')),
                 ('late-mark', screen.SELECTED.replace('        slot16[0x106] = 1;\n        func_15125394(arg0);',
                                                       '        func_15125394(arg0);\n        slot16[0x106] = 1;'))]
        memory = memory_case(21)
        wanted = reference(memory, 21, (0x1234, 0x5678, 0x9ABC))
        for name, body in forms:
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            model = StateSaveOracle(words, memory, 21, (0x1234, 0x5678, 0x9ABC)).run()
            self.assertNotEqual((external(model.memory), model.calls, events(model), model.r[2]), wanted)

    def test_production_source_and_exact_unchanged_callback(self):
        source = (self.root / 'conker/src/game_14FF90.c').read_text()
        self.assertEqual(re.search(r'^s32 func_15123934\([^;{]+\) \{\n.*?\n\}', source, re.M | re.S).group(), screen.SELECTED)
        functions = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        self.assertEqual(functions['func_15123934'], self.retail)
        self.assertEqual(functions['func_15125394'], self.callback)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse(any(row['function'] == 'func_15123934' for row in csv.DictReader(stream)))
        self.assertNotIn('//     temp_v1 = &arg0[arg4];', source)


if __name__ == '__main__':
    unittest.main()
