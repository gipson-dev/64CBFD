"""Ordered output stores, selector palette aliases and the retained 64-bit RNG."""

import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.check_game_data_layout import load_section
from tools.experiments import game_random_selector_outputs_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_indexed_state_save_match import external, events
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

OUTPUT, TABLE, SEED = 0x20000, 0x8008A160, 0x800885B0
RANDOM_WORDS = (0, 1, 2, 3, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFE, 0xFFFFFFFF)
SEEDS = (0, 1, 2, 3, 0xFFFFFFFF, 0x100000000, 0x100000001, 0x1FFFFFFFF,
         0xFFFFFFFFFFFFFFFF, 0x123456789ABCDEF0, 0x8000000000000000, 0x8000000000000001)
NORMAL = tuple(OUTPUT+i for i in range(7))
LAYOUTS = [NORMAL, (OUTPUT,)*7]
for index, address in ((1, OUTPUT), (1, OUTPUT+7), (0, OUTPUT+2), (3, OUTPUT+2),
                       (2, TABLE+37), (2, TABLE+49), (3, TABLE+38), (3, TABLE+50),
                       (0, TABLE+36), (0, TABLE+48), (0, SEED+7), (1, SEED+3),
                       (2, SEED), (6, SEED+6)):
    layout = list(NORMAL)
    layout[index] = address
    LAYOUTS.append(tuple(layout))


def next_seed(value):
    mixed = ((value & 1) << 32) | ((value >> 1) & 0xFFFFFFFF)
    mixed ^= (value & 0xFFFFF) << 12
    return mixed ^ ((mixed >> 20) & 0xFFF)


def memory_case(seed, pattern, palette):
    memory = {STACK+i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({OUTPUT+i: (i*17+pattern*83)&255 for i in range(64)})
    memory.update({TABLE+i: value if not pattern else (i*29+pattern*71)&255
                   for i, value in enumerate(palette)})
    put(memory, SEED, seed, 8)
    return memory


def changes(arguments, call, mutation):
    if not mutation:
        return []
    return ([(arguments[1], 0x80, 1)] if call == 0 else
            [(arguments[0], 0xA7, 1)] if call == 1 else [(TABLE+37, 0xE3, 1), (TABLE+50, 0xC7, 1)])


def snapshot(memory):
    return bytes(memory[a] for a in (*range(OUTPUT, OUTPUT+64), *range(SEED, SEED+8), *range(TABLE, TABLE+60)))


def reference(memory, arguments, randoms, mode, mutation):
    memory, trace, calls = dict(memory), [], []
    number = 0
    def read(address, size):
        value = int.from_bytes(bytes(memory[address+i] for i in range(size)), 'big')
        trace.append(('R', address, size, value))
        return value
    def write(address, value, size):
        put(memory, address, value, size)
        trace.append(('W', address, size, value & ((1 << (size*8))-1)))
    def call(target, args=()):
        calls.append((target, *args, snapshot(memory)))
        trace.append(('CALL', target, *args))
    def random():
        nonlocal number
        call(screen.RANDOM)
        if mode == 2:
            value = next_seed(read(SEED, 8))
            write(SEED, value, 8)
        else:
            value = randoms[number]
            for address, word, size in changes(arguments, number, mutation):
                write(address, word, size)
        number += 1
        return value & 0xFFFFFFFF
    result = random()
    if result & 1:
        write(arguments[1], read(arguments[1], 1) | 1, 1)
    write(arguments[0], 0x16, 1)
    result = random()
    selector = 3 if result & 1 else 4
    call(screen.SELECTOR, (selector, *arguments[2:5]))
    if mode:
        result = random()
        row = TABLE+selector*12+(result&3)*3
        for i in range(3):
            write(arguments[i+2], read(row+i, 1), 1)
    else:
        for pointer, value in zip(arguments[2:5], (0x31, 0x52, 0x73)):
            write(pointer, value, 1)
        result = 0x81234567
    write(arguments[5], 0xC8, 1)
    write(arguments[6], 0x401, 2)
    return external(memory), trace, calls, result


class RandomOutputsOracle(TriangleOracle):
    def __init__(self, words, memory, arguments, randoms, mode=0, mutation=0, phase=0, selector=(), random=()):
        code = {screen.SELECTOR+i*4: word for i, word in enumerate(selector if mode else ())}
        code.update({screen.RANDOM+i*4: word for i, word in enumerate(random if mode == 2 else ())})
        super().__init__(words, memory, entry=screen.ENTRY, arguments=arguments, phase=phase, connected=code)
        self.outputs, self.randoms, self.mutation, self.number = arguments, randoms, mutation, 0

    def execute(self, word):
        op, rs, rt, rd, shift, fn = word >> 26, word >> 21 & 31, word >> 16 & 31, word >> 11 & 31, word >> 6 & 31, word & 63
        mask = (1 << 64)-1
        if op in (55, 63):
            immediate = word & 65535
            address = (self.r[rs]+(immediate if immediate < 32768 else immediate-65536)) & 0xFFFFFFFF
            assert address % 8 == 0
            if op == 55:
                self.r[rt] = self.get(address, 8)
            else:
                self.put(address, self.r[rt], 8)
        elif op == 0 and fn in (37, 38, 56, 58, 60, 62, 63):
            value = self.r[rt] & mask
            if fn in (37, 38):
                value = self.r[rs] | self.r[rt] if fn == 37 else self.r[rs] ^ self.r[rt]
            elif fn in (56, 60):
                value <<= shift+(32 if fn == 60 else 0)
            elif fn in (58, 62):
                value >>= shift+(32 if fn == 62 else 0)
            else:
                value = (value if value < 1 << 63 else value-(1 << 64)) >> (shift+32)
            self.r[rd] = value & mask
        else:
            # The shared low-word runner masks every register after an instruction.
            # Preserve untouched 64-bit RNG temporaries across ordinary operations.
            before = self.r[:]
            super().execute(word)
            destination = (rt if op in (9, 12, 13, 15, 33, 35, 36, 37) else
                           rd if op == 0 and fn in (0, 2, 3, 33, 35, 36, 42, 43) else None)
            for i, value in enumerate(before):
                if i != destination and value > 0xFFFFFFFF:
                    self.r[i] = value
        self.r[0] = 0

    def record_call(self, target):
        assert target in (screen.RANDOM, screen.SELECTOR)
        args = self.arguments(4) if target == screen.SELECTOR else ()
        self.calls.append((target, *args, snapshot(self.memory)))
        self.events.append(('CALL', target, *args))

    def hook(self, target):
        if target == screen.RANDOM:
            value = self.randoms[self.number]
            for address, word, size in changes(self.outputs, self.number, self.mutation):
                self.put(address, word, size)
            self.number += 1
        else:
            assert target == screen.SELECTOR
            for pointer, value in zip(self.arguments(4)[1:], (0x31, 0x52, 0x73)):
                self.put(pointer, value, 1)
            value = 0x81234567
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.r[2] = value
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameRandomSelectorOutputsMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-random-selector-outputs-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>37I', rom, screen.ROM))
        cls.selector = list(struct.unpack_from('>31I', rom, 0x16FE90))
        cls.random = list(struct.unpack_from('>18I', rom, 0xDAED0))
        cls.palette = rom[0x2275E0+TABLE-0x80082B20:0x2275E0+TABLE-0x80082B20+60]
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        helper = re.search(r'void func_151429E0\([^;{}]+\) \{.*?\n\}',
                          (cls.root / 'conker/src/game_16EE20.c').read_text(), re.S).group()
        cls.fixture = '''typedef unsigned char u8;typedef short s16;typedef int s32;
typedef unsigned int u32;typedef unsigned long long u64;
static union {u64 align;u8 b[256];} actual,expected;
#define D_8008A160 (actual.b+128)
static int mode,mutation,number,calls,expectedCalls,error;
static u32 randoms[3],targets[4],wantedTargets[4],args[4][4],wantedArgs[4][4];
static u8 snapshots[4][256],wantedSnapshots[4][256];
static int offsets[7];
static u64 next(u64 s) {u64 t=((s&1)<<32)|((s>>1)&0xFFFFFFFF);t^=(s&0xFFFFF)<<12;return t^((t>>20)&0xFFF);}
static void capture(int want,u32 target,u32 a,u32 b,u32 c,u32 d) {
    int i,n=want?expectedCalls++:calls++;u32 *v=want?wantedArgs[n]:args[n];
    if(n>=4) {error=1;return;}
    (want?wantedTargets:targets)[n]=target;v[0]=a;v[1]=b;v[2]=c;v[3]=d;
    for(i=0;i<256;i++) (want?wantedSnapshots:snapshots)[n][i]=(want?expected.b:actual.b)[i];
}
static void mutate(u8 *p,int n) {
    if(!mutation) return;
    if(n==0) p[offsets[1]]=0x80;
    if(n==1) p[offsets[0]]=0xA7;
    if(n==2) {p[128+37]=0xE3;p[128+50]=0xC7;}
}
static u32 draw(int want) {
    u8 *p=want?expected.b:actual.b;u32 value;
    capture(want,1,0,0,0,0);
    if(mode==2) {u64 value64=next(*(u64 *)(p+80));*(u64 *)(p+80)=value64;value=(u32)value64;}
    else {value=randoms[number];mutate(p,number);}
    number++;return value;
}
s32 func_150ADA20(void) {return (s32)draw(0);}
''' + helper.replace('func_151429E0', 'selector_impl') + '''
void func_151429E0(u8 selector,u8 *a,u8 *b,u8 *c) {
    capture(0,2,selector,(u32)(a-actual.b),(u32)(b-actual.b),(u32)(c-actual.b));
    if(mode) selector_impl(selector,a,b,c);
    else {*a=0x31;*b=0x52;*c=0x73;}
}
static void reference(void) {
    u8 *p=expected.b;u32 r;int selector,row,i;
    r=draw(1);if(r&1) p[offsets[1]]|=1;
    p[offsets[0]]=0x16;r=draw(1);selector=(r&1)?3:4;
    capture(1,2,selector,offsets[2],offsets[3],offsets[4]);
    if(mode) {r=draw(1);row=128+selector*12+(r&3)*3;for(i=0;i<3;i++) p[offsets[i+2]]=p[row+i];}
    else {p[offsets[2]]=0x31;p[offsets[3]]=0x52;p[offsets[4]]=0x73;}
    p[offsets[5]]=0xC8;*(s16 *)(p+offsets[6])=0x401;
}
''' + screen.SELECTED + '\n'

    def compare(self, seed, layout, randoms=(0, 0, 0), mode=0, mutation=0, phase=0, pattern=0):
        memory = memory_case(seed, pattern, self.palette)
        wanted, trace, calls, result = reference(memory, layout, randoms, mode, mutation)
        coverage = set()
        for words in (self.retail, self.words):
            model = RandomOutputsOracle(words, memory, layout, randoms, mode, mutation, phase, self.selector, self.random).run()
            self.assertEqual(external(model.memory), wanted)
            self.assertEqual(events(model), trace)
            self.assertEqual(model.calls, calls)
            self.assertEqual(model.r[2] & 0xFFFFFFFF, result)
            coverage.update(model.visits)
        return coverage

    def test_direct_body_and_twenty_four_compiler_controls(self):
        self.assertEqual(self.words, self.retail)
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (37, 0x18, 0))
        expected = {'byte-selector': ((36,24,15),(36,24,32),(42,32,38),(41,32,39)),
                    'ternary': ((36,24,15),(36,24,32),(42,32,38),(41,32,39)),
                    'wide-selector': ((37,24,0),(37,24,31),(42,32,38),(41,32,39)),
                    'direct-choice': ((37,24,0),(37,24,31),(42,40,42),(41,40,39)),
                    'cached-first-random': ((36,24,15),(36,24,32),(44,32,41),(43,32,42)),
                    'volatile-first-pointers': ((37,24,16),(37,24,22),(44,40,44),(43,40,41))}
        for name, body in screen.candidates():
            for i, profile in enumerate(screen.PROFILES):
                record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                self.assertEqual((record['body_words'], record['frame'], record['differences']), expected[name][i])
                self.assertEqual(record['diagnostics'], '')

    def test_opaque_and_connected_selector_order_aliases_and_call_snapshots(self):
        for mode in (0, 1):
            coverage, cases = set(), 0
            for first, second, third, layout, mutation, phase in itertools.product(
                    RANDOM_WORDS, RANDOM_WORDS, range(4) if mode else (0,), LAYOUTS, (0, 1), (0, 8)):
                coverage.update(self.compare(SEEDS[9], layout, (first, second, third), mode, mutation, phase, cases%3))
                cases += 1
            self.assertEqual(cases, 16384 if mode else 4096)
            wanted = set(range(screen.ENTRY, screen.ENTRY+148, 4))
            if mode:
                wanted.update(range(screen.SELECTOR, screen.SELECTOR+124, 4))
            self.assertEqual(coverage, wanted)
            (self.output / ('connected-selector.json' if mode else 'opaque.json')).write_text(
                json.dumps(dict(cases=cases, models=2, reachable_words=len(coverage)), indent=2)+'\n')

    def test_complete_handwritten_rng_carries_state_aliases_and_all_words(self):
        coverage, cases = set(), 0
        for seed, layout, phase in itertools.product(SEEDS, LAYOUTS, (0, 8)):
            coverage.update(self.compare(seed, layout, mode=2, phase=phase, pattern=cases%3))
            cases += 1
        for seed, phase in itertools.product(range(4096), (0, 8)):
            coverage.update(self.compare(seed, NORMAL, mode=2, phase=phase))
            cases += 1
        self.assertEqual(cases, 8576)
        self.assertEqual(coverage, set(range(screen.ENTRY, screen.ENTRY+148, 4)) |
                         set(range(screen.SELECTOR, screen.SELECTOR+124, 4)) |
                         set(range(screen.RANDOM, screen.RANDOM+72, 4)))
        (self.output / 'connected-rng.json').write_text(json.dumps(dict(cases=cases, models=2,
            wrapper_words=37, selector_words=31, rng_words=18, reachable_words=len(coverage)), indent=2)+'\n')

    def test_native_actual_wrapper_selector_and_independent_state_model(self):
        def offset(a):
            return a-OUTPUT if a < OUTPUT+64 else a-SEED+80 if SEED <= a < SEED+8 else a-TABLE+128
        layouts = ','.join('{'+','.join(str(offset(a)) for a in row)+'}' for row in LAYOUTS)
        palette = ','.join(str(v) for v in self.palette)
        seeds = ','.join('0x%016XULL'%v for v in SEEDS)
        words = ','.join('0x%08XU'%v for v in RANDOM_WORDS)
        self.run_host('static int layouts[][7]={'+layouts+'};static u8 palette[]={'+palette+'};'
                      'static u64 seeds[]={'+seeds+'};static u32 values[]={'+words+'};\n'+r'''
int m,a,b,t,l,k,i,j,n,count=0;
if(sizeof(void *)!=4 || sizeof(s16)!=2) return 1;
for(m=0;m<3;m++) for(a=0;a<(m==2?4108:8);a++) for(b=0;b<(m==2?1:8);b++)
for(t=0;t<(m==1?4:1);t++) for(l=0;l<(m==2 && a>=12?1:16);l++) for(k=0;k<(m==2?1:2);k++) {
    mode=m;mutation=k;randoms[0]=values[a%8];randoms[1]=values[b];randoms[2]=t;
    for(i=0;i<256;i++) actual.b[i]=(u8)(i*17+count*83);
    for(i=0;i<60;i++) actual.b[128+i]=palette[i];
    *(u64 *)(actual.b+80)=(m==2 && a>=12)?(u64)(a-12):seeds[a%12];
    for(i=0;i<7;i++) offsets[i]=layouts[l][i];
    for(i=0;i<256;i++) expected.b[i]=actual.b[i];
    calls=expectedCalls=error=number=0;reference();number=0;
    func_1518E5D8(actual.b+offsets[0],actual.b+offsets[1],actual.b+offsets[2],actual.b+offsets[3],
                  actual.b+offsets[4],actual.b+offsets[5],(s16 *)(actual.b+offsets[6]));
    n=mode?4:3;if(error || calls!=n || expectedCalls!=n) return 2;
    for(i=0;i<256;i++) if(actual.b[i]!=expected.b[i]) return 3;
    for(i=0;i<n;i++) {
        if(targets[i]!=wantedTargets[i]) return 4;
        for(j=0;j<4;j++) if(args[i][j]!=wantedArgs[i][j]) return 5;
        for(j=0;j<256;j++) if(snapshots[i][j]!=wantedSnapshots[i][j]) return 6;
    }
    count++;
}
if(count!=14528) return 7;
''')

    def test_stub_wrong_bit_selector_and_store_order_are_detected(self):
        forms = {'stub': 'void func_1518E5D8(u8 *a,u8 *b,u8 *c,u8 *d,u8 *e,u8 *f,s16 *g) {}',
                 'bit': screen.SELECTED.replace('& 1', '& 2', 1),
                 'selector': screen.SELECTED.replace('selector = 3;', 'selector = 4;'),
                 'flag': screen.SELECTED.replace('*arg1 |= 1;', '*arg1 |= 2;'),
                 'status-order': screen.SELECTED.replace('    *arg0 = 0x16;\n', '').replace('    if (func_150ADA20() & 1)', '    *arg0 = 0x16;\n    if (func_150ADA20() & 1)', 1),
                 'tail-order': screen.SELECTED.replace('    *arg5 = 0xC8;\n    *arg6 = 0x401;', '    *arg6 = 0x401;\n    *arg5 = 0xC8;')}
        layout = (OUTPUT,)*7
        memory = memory_case(1, 1, self.palette)
        wanted = reference(memory, layout, (1, 1, 2), 1, 1)
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root, self.output, 'wrong-'+name, body)
            model = RandomOutputsOracle(words, memory, layout, (1, 1, 2), 1, 1, selector=self.selector).run()
            self.assertNotEqual((external(model.memory), events(model), model.calls, model.r[2]&0xFFFFFFFF), wanted, name)
        wrong = list(self.random)
        wrong[2] = (wrong[2]&~63)|56
        model = RandomOutputsOracle(self.retail, memory_case(1, 0, self.palette), NORMAL, (), 2,
                                    selector=self.selector, random=wrong).run()
        self.assertNotEqual(external(model.memory), reference(memory_case(1, 0, self.palette), NORMAL, (), 2, 0)[0])

    def test_production_direct_wrapper_retained_helpers_and_palette(self):
        linked, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1518E5D8'], screen.ENTRY)
        self.assertEqual(linked['func_1518E5D8'], self.retail)
        self.assertEqual(linked['func_151429E0'], self.selector)
        self.assertEqual(linked['func_150ADA20'], self.random)
        self.assertIn(screen.SELECTED, (self.root / 'conker/src/game/generated_1BA1D0.c').read_text())
        self.assertNotIn('func_1518E5D8', (self.root / 'conker/retail_word_patches.us.csv').read_text())
        address, data = load_section(self.root / 'conker/build/conker.us.elf', '.game_data')
        self.assertEqual(data[TABLE-address:TABLE-address+60], self.palette)


if __name__ == '__main__':
    unittest.main()
