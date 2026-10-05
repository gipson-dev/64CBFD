"""Complete renderer control flow against retail; external callbacks are bounded models."""

import hashlib
import itertools
import json
import math
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

from tools import match_progress
from tools.tests import test_game_palette_updater as palette
from tools.tests import test_game_queued_segment_writer as queue
from tools.tests import test_game_random_curve_record as curve
from tools.tests.test_game_dual_matrix_emitter import sdk_macro
from tools.tests.game_animation_timeline_oracle import TimelineOracle, bits, floating, signed


ENTRY = 0x1510B9D0
BASE = 0x800DBFF0
ACTORS = 0x100000
PAGE = 0x800BE9C0
FLAG = 0x800BEBA0
CATEGORY = 0x800BE9F0
VALUE = 0x800D9E10
PRIMARY = 0x800B0E00
SECOND = PRIMARY + 4
THIRD = PRIMARY + 8
SPECS = {
    0x1510B7B4: (2, 0), 0x1510CB10: (1, None), 0x1510CDB8: (4, 0),
    0x151733D8: (2, 0), 0x150C8600: (1, 0), 0x15100464: (1, 0),
    0x150DFBD0: (1, 0), 0x150CF5E8: (1, 0), 0x150D765C: (1, 0),
    0x1510F800: (1, None), 0x1515D914: (14, 0), 0x150A5378: (6, 1),
    0x1512E5F0: (2, 0), 0x1515E544: (5, 0), 0x151742EC: (2, 0),
}
LEAVES = {'func_1510B7B4': 105, 'func_1510CB10': 170, 'func_1510CDB8': 42,
          'func_151733D8': 3}


def case(slot=0, page=0, category=0, mode=0, enabled=0, mask=0,
         draw=0, special=0, second=0, third=0, effect=0, no_light=0, coords=None):
    memory = palette.updater_case(slot)
    memory.update({queue.STACK + i: 0xA5 for i in range(-0x300, 0x40)})
    memory.update({0x80050000 + i: 0xA5 for i in range(4 * 0x180)})
    memory.update({0x800D9B90 + i: 0xA5 for i in range(0x260)})
    values = ((BASE, ACTORS, 4), (PAGE, page, 1), (FLAG, 0xA5, 1),
              (CATEGORY, category, 4), (0x800C35EA, mode, 1), (0x800C3662, enabled, 1),
              (0x800D18A0, mask, 2), (0x800BEAAA, draw, 1), (0x800DBE62, special, 1),
              (0x800DCD7C, no_light, 4), (PRIMARY, 0x12345678, 4),
              (SECOND, 0x23456780 if second else 0, 4),
              (THIRD, 0x34567890 if third else 0, 4), (0x800D9E20, 254, 1),
              (0x800D9E21, 253, 1), (0x800BE628, 0x80050000, 4),
              (0x800DC2A0, 0x80060000, 4), (0x800DC2A4, 0x80070000, 4))
    for address, value, size in values:
        palette.put(memory, address, value, size)
    for row in range(4):
        palette.put(memory, VALUE + row * 4, 0x12340000 + row, 4)
        palette.put(memory, ACTORS + row * 0x9A0 + 0x8B8, effect, 1)
        palette.put(memory, ACTORS + row * 0x9A0 + 0x84, 8 if effect else 0, 4)
        for index, value in enumerate(coords or (1.75, -2.75, 3.5)):
            palette.put(memory, ACTORS + row * 0x9A0 + 0x2F8 + index * 4, bits(value), 4)
        palette.put(memory, 0x80050000 + row * 0x180 + 0xB8, 0x8001, 2)
    return memory


class RendererOracle(palette.PaletteUpdaterOracle):
    def __init__(self, words, memory, slot, table, connected=None, mutation=0):
        queue.SegmentQueueOracle.__init__(self, words, ENTRY, memory, (queue.OUTPUT, slot))
        self.events, self.mutation, self.slot = [], mutation, slot & 0xFFFF
        self.global_stores = []
        self.calls, self.connected = [], connected or {}
        self.code.update(self.connected)
        for index, word in enumerate(table):
            palette.put(self.memory, 0x800A2C2C + index * 4, word, 4)

    def peek(self, address, size):
        assert all(address + i in self.memory for i in range(size)), ('unmapped read', address, size)
        return TimelineOracle.get(self, address, size)

    def get(self, address, size):
        self.peek(address, size)
        return queue.SegmentQueueOracle.get(self, address, size)

    def put(self, address, value, size):
        if self.recording:
            assert (queue.STACK - 0x300 <= address < queue.STACK + 0x40
                    or queue.OUTPUT <= address < queue.OUTPUT + 0x1000
                    or address == FLAG
                    or (self.connected and queue.PRIMITIVE <= address < palette.TARGET + 16)), (
                        'renderer output fence', address, size)
            if address == FLAG:
                self.global_stores.append((address, size, value & 255))
        queue.SegmentQueueOracle.put(self, address, value, size)

    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        fn, rd = word & 63, word >> 11 & 31
        if op == 0 and fn == 4:
            self.r[rd] = self.r[rt] << (self.r[rs] & 31) & 0xFFFFFFFF
        elif op == 0 and fn == 36:
            self.r[rd] = self.r[rs] & self.r[rt]
        elif op == 0 and fn == 43:
            self.r[rd] = int(self.r[rs] < self.r[rt])
        elif op == 11:
            immediate = word & 65535
            if immediate & 0x8000:
                immediate |= 0xFFFF0000
            self.r[rt] = int(self.r[rs] < immediate)
        elif op == 14:
            self.r[rt] = self.r[rs] ^ (word & 65535)
        else:
            super().execute(word)
        self.r[0] = 0

    def arguments(self, count):
        return tuple(self.r[4 + i] if i < 4 else self.peek(self.r[29] + i * 4, 4)
                     for i in range(count))

    def record_call(self, target):
        if target == palette.TRIG:
            self.events.append((target, (self.r[4],)))
            return
        count, _ = SPECS[target]
        args = self.arguments(count)
        self.events.append((target, args, self.peek(FLAG, 1), self.peek(PAGE, 1),
                            self.peek(BASE, 4), self.peek(VALUE + (self.slot & 3) * 4, 4)))

    def hook(self, target):
        result = 0xA5000002
        if target == palette.TRIG:
            self.f[0] = bits(0.25)
        else:
            _, cursor = SPECS[target]
            args = self.arguments(SPECS[target][0])
            if cursor is not None:
                output = args[cursor]
                self.put(output, target, 4)
                self.put(output + 4, 0xCA110000 | len(self.events), 4)
                result = output + 8
            row = self.slot & 3
            if self.mutation == 1 and target == 0x1510B7B4:
                palette.put(self.memory, 0x800D18A0, 1 << row, 2)
                palette.put(self.memory, 0x800C35EA, 1, 1)
                palette.put(self.memory, 0x800C3662, 1, 1)
            if self.mutation == 2 and target == 0x1515D914:
                palette.put(self.memory, BASE, ACTORS + 0x9A0, 4)
                palette.put(self.memory, ACTORS + row * 0x9A0 + 0x8B8, 1, 1)
                palette.put(self.memory, ACTORS + row * 0x9A0 + 0x84, 8, 4)
            if self.mutation == 3 and target == 0x1510F800:
                palette.put(self.memory, BASE, ACTORS + 0x9A0, 4)
                palette.put(self.memory, PAGE, 1, 1)
                for index, value in enumerate((15.75, -16.75, 17.5)):
                    palette.put(self.memory, ACTORS + (row + 1) * 0x9A0 + 0x2F8 + index * 4,
                                bits(value), 4)
            if self.mutation == 4 and target == 0x1515E544:
                palette.put(self.memory, THIRD, 0x34567890, 4)
            if self.mutation == 5 and target == 0x1515D914:
                palette.put(self.memory, CATEGORY, 5, 4)
            if self.mutation == 6 and target == 0x151733D8:
                palette.put(self.memory, SECOND, 0x23456780, 4)
            if self.mutation == 7 and target == 0x1515D914:
                palette.put(self.memory, VALUE + row * 4, 0x87654321, 4)
                palette.put(self.memory, 0x800D9E20, 252, 1)
                palette.put(self.memory, 0x800D9E21, 251, 1)
                palette.put(self.memory, PAGE, 1, 1)
            if self.mutation == 8 and target == 0x1510B7B4:
                palette.put(self.memory, 0x800D18A0, 0, 2)
                palette.put(self.memory, 0x800C35EA, 0, 1)
                palette.put(self.memory, 0x800C3662, 0, 1)
        for register in (2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        if target == palette.TRIG:
            self.f[0] = bits(0.25)
        self.r[2] = result

    def run(self):
        pc = self.entry
        for _ in range(20000):
            self.visits.add(pc)
            word = self.code[pc]
            op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
            if op == 17 and rs == 8:
                assert rt in (0, 1, 2, 3), ('unsupported floating branch', rt)
                immediate = word & 65535
                offset = immediate if immediate < 32768 else immediate - 65536
                take = self.condition == bool(rt & 1)
                if take or not rt & 2:
                    self.visits.add(pc + 4)
                    self.execute(self.code[pc + 4])
                pc = pc + 4 + offset * 4 if take else pc + 8
            elif op in (1, 4, 5, 6, 7, 20, 21):
                immediate = word & 65535
                offset = immediate if immediate < 32768 else immediate - 65536
                if op == 1:
                    assert rt in (0, 1, 2, 3)
                    take = signed(self.r[rs]) >= 0 if rt & 1 else signed(self.r[rs]) < 0
                    likely = bool(rt & 2)
                else:
                    take = (signed(self.r[rs]) <= 0 if op == 6 else
                            signed(self.r[rs]) > 0 if op == 7 else self.r[rs] == self.r[rt])
                    if op in (5, 21):
                        take = not take
                    likely = op in (20, 21)
                if take or not likely:
                    self.visits.add(pc + 4)
                    self.execute(self.code[pc + 4])
                pc = pc + 4 + offset * 4 if take else pc + 8
            elif op == 3:
                target = (pc + 4 & 0xF0000000) | ((word & 0x3FFFFFF) << 2)
                self.r[31] = pc + 8
                self.visits.add(pc + 4)
                self.execute(self.code[pc + 4])
                self.record_call(target)
                if target in self.connected:
                    pc = target
                else:
                    self.hook(target)
                    pc += 8
            elif op == 0 and word & 63 == 8:
                target = self.r[rs]
                self.visits.add(pc + 4)
                self.execute(self.code[pc + 4])
                if target == 0xDEAD0000:
                    for register in (*range(16, 24), 28, 29, 30, 31):
                        assert self.r[register] == self.before[register], ('saved register', register)
                    return self
                assert target in self.code, ('unowned jump', target)
                pc = target
            else:
                self.execute(word)
                pc += 4
        raise AssertionError('renderer instruction budget exhausted')


class GameViewportRendererTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host
    test_complete_init_debugger_and_game_data_remain_exact = (
        queue.GameQueuedSegmentWriterTests.test_complete_init_debugger_and_game_data_remain_exact)

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if shutil.which('mips-linux-gnu-objdump') is None:
            raise unittest.SkipTest('MIPS tools unavailable')
        source = (cls.root / 'conker/src/game/generated_138520.c').read_text()
        cls.body = re.search(r'Gfx \*func_1510B9D0\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.declarations = source.split('/* Non-matching placeholders', 1)[0]
        cls.production, _, cls.addresses = match_progress.load_elf_functions(
            str(cls.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        config = yaml.safe_load((cls.root / 'conker/conker.us.yaml').read_text())
        assert hashlib.sha1(cls.rom).hexdigest() == config['sha1']
        data = next(s for s in config['segments'] if isinstance(s, dict) and s.get('name') == 'game_data')
        cls.table = struct.unpack_from('>35I', cls.rom, data['start'] + 0x800A2C2C - data['vram'])
        cls.retail = list(struct.unpack_from('>356I', cls.rom, 0x138E80))
        cls.pairs, cls.connected_pairs, cls.prefixes = 0, 0, 0
        cls.coverage, cls.retail_coverage, cls.completed = set(), set(), set()
        cls.native_cases = 0
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        gbi = (cls.root / 'conker/include/2.0L/PR/gbi.h').read_text()
        mbi = (cls.root / 'conker/include/2.0L/PR/mbi.h').read_text()
        macros = sdk_macro(mbi, '_SHIFTL')
        for name in ('G_RDPPIPESYNC', 'gDPNoParam', 'gDPPipeSync', 'G_SETBLENDCOLOR',
                     'gDPSetColor', 'DPRGBColor', 'gDPSetBlendColor', 'G_MTX',
                     'G_MTX_MODELVIEW', 'G_MTX_PROJECTION', 'G_MTX_LOAD', 'G_MTX_MUL',
                     'G_MTX_NOPUSH', 'G_MTX_PUSH', 'gDma2p', 'gSPMatrix', 'G_MOVEWORD',
                     'G_MW_PERSPNORM', 'G_MW_CLIP', 'G_MWO_CLIP_RNX', 'G_MWO_CLIP_RNY',
                     'G_MWO_CLIP_RPX', 'G_MWO_CLIP_RPY', 'FR_NEG_FRUSTRATIO_3',
                     'FR_POS_FRUSTRATIO_3', 'gDma1p', 'gMoveWd', 'gSPPerspNormalize',
                     'gSPClipRatio', 'G_GEOMETRYMODE', 'G_LOD', 'gSPGeometryMode',
                     'gSPClearGeometryMode', 'G_RDPSETOTHERMODE', 'gDPSetOtherMode',
                     'G_SETPRIMCOLOR', 'G_SETENVCOLOR', 'gDPSetPrimColor', 'gDPSetEnvColor',
                     'G_MOVEMEM', 'G_MV_LIGHT', 'G_MVO_LOOKATX', 'gSPLookAtX', 'gSPLight',
                     'G_DL', 'G_DL_PUSH', 'gSPDisplayList'):
            macros += sdk_macro(gbi, name)
        helper = re.search(r'Gfx \*func_1510B7B4\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        color = re.search(r'Gfx \*func_1510CDB8\([^;{}]+\) \{\n.*?\n\}',
                          (cls.root / 'conker/src/game/generated_139FC0.c').read_text(), re.S).group(0)
        cls.fixture = '''typedef unsigned char u8; typedef unsigned short u16;
typedef short s16; typedef unsigned int u32; typedef int s32; typedef float f32;
typedef struct { struct { u32 w0,w1; } words; } Gfx;
typedef struct { u8 bytes[64]; } Mtx; typedef struct { u8 bytes[16]; } Light;
''' + macros + r'''
static u8 records[4*0x180], matrices[2][4*0x40], actors[4*0x9A0];
u8 *D_800BE628=records, *D_800DBFF0=actors;
u8 D_80089470[64], D_800BE9C0, *D_800DC2A0[2]={matrices[0],matrices[1]};
u8 D_800C35EA,D_800C3662,D_800BEBA0,D_800BEAAA,D_800DBE62;
u16 D_800D18A0; s32 D_800BE9F0,D_800DCD7C;
u8 D_800D9B90[64],D_800D9BD0[64],D_800D9C10[256];
s32 D_800D9E10[4]; u8 D_800D9E20,D_800D9E21,D_800D9E28[8];
u8 D_800D9B68[4][3],D_800D9B78[4][3];
Gfx *D_800B0E00,*D_800B0E04,*D_800B0E08;
static Gfx commands[128];
static u32 events[24]; static int count,error,selected;
static void event(u32 target) { if(count>=24) error=1; else events[count++]=target; }
static Gfx *packet(Gfx *p,u32 target) { event(target); p->words.w0=target; p->words.w1=0xCA110000; return p+1; }
void func_1510CB10(s16 slot) { if(slot!=selected) error=1; event(0x1510CB10); }
Gfx *func_151733D8(Gfx *p,s32 mode) { if(mode!=1) error=1; return p; }
Gfx *func_150C8600(Gfx *p) { return packet(p,0x150C8600); }
Gfx *func_15100464(Gfx *p) { return packet(p,0x15100464); }
Gfx *func_150DFBD0(Gfx *p) { return packet(p,0x150DFBD0); }
Gfx *func_150CF5E8(Gfx *p) { return packet(p,0x150CF5E8); }
Gfx *func_150D765C(Gfx *p) { return packet(p,0x150D765C); }
void func_1510F800(s32 value) { if(value) error=1; event(0x1510F800); }
Gfx *func_1515D914(Gfx *p,s32 slot,s32 x,s32 y,s32 z,s32 zero,s32 value,
                  s32 byte,u8 *light,u8 *other,s32 one,s32 zero2,s32 mode,u8 *tail) {
    if(slot!=selected||x!=1||y!=-2||z!=3||zero||value!=0x12340000+selected
       ||byte!=254||light!=D_800D9BD0+selected*16+D_800BE9C0*8||other!=&D_800D9E21
       ||one!=1||zero2||mode!=0x25||tail!=D_800D9E28) error=1;
    return packet(p,0x1515D914);
}
Gfx *func_150A5378(Gfx *dl,Gfx *p,u8 *matrix,s32 a,s32 b,u32 mask) {
    if(dl!=D_800B0E00||matrix!=D_800D9C10+selected*64||a||b||mask!=(1U<<selected)) error=1;
    return packet(p,0x150A5378);
}
Gfx *func_1512E5F0(Gfx *p,u8 *actor) {
    if(actor!=actors+selected*0x9A0||D_800BEBA0!=0) error=1;
    return packet(p,0x1512E5F0);
}
Gfx *func_1515E544(Gfx *p,s32 value,s32 byte,s32 other,u8 *light) {
    if(value!=0x12340000+selected||byte!=254||other!=253
       ||light!=D_800D9BD0+selected*16+D_800BE9C0*8) error=1;
    return packet(p,0x1515E544);
}
Gfx *func_151742EC(Gfx *p,s16 slot) { if(slot!=selected) error=1; return packet(p,0x151742EC); }
static void initialize(int slot,int page,int category,int draw,int special,int second,int third,int effect,int suppressed) {
    int i; selected=slot; count=error=0;
    D_800DBFF0=actors; D_800BE9C0=page; D_800BE9F0=category;
    D_800BEAAA=draw; D_800DBE62=special; D_800D18A0=suppressed?(1U<<slot):0;
    D_800C35EA=D_800C3662=D_800DCD7C=0; D_800BEBA0=0xA5;
    D_800B0E00=(Gfx *)0x12345678; D_800B0E04=second?(Gfx *)0x23456780:0;
    D_800B0E08=third?(Gfx *)0x34567890:0; D_800D9E20=254; D_800D9E21=253;
    for(i=0;i<128;i++) commands[i].words.w0=commands[i].words.w1=0xA5A5A5A5;
    for(i=0;i<4;i++) {
        D_800D9E10[i]=0x12340000+i;
        *(u16 *)(records+i*0x180+0xB8)=0x8001;
        *(f32 *)(actors+i*0x9A0+0x2F8)=1.75f;
        *(f32 *)(actors+i*0x9A0+0x2FC)=-2.75f;
        *(f32 *)(actors+i*0x9A0+0x300)=3.5f;
        actors[i*0x9A0+0x8B8]=effect; *(u32 *)(actors+i*0x9A0+0x84)=effect?8:0;
    }
}
''' + helper + '\n' + color + '\n' + cls.body + '\n'

    def tearDown(self):
        if self._outcome.success:
            type(self).completed.add(self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        receipt = {'completed_pairs': cls.pairs, 'connected_pairs': cls.connected_pairs,
                   'native_cases': cls.native_cases,
                   'invalid_prefix_pairs': cls.prefixes, 'completed_checks': sorted(cls.completed),
                   'renderer_retail_words_reached': len(cls.retail_coverage),
                   'renderer_c_words_reached': len(cls.coverage),
                   'complete_module_corpus': (cls.completed == set(
                       unittest.defaultTestLoader.getTestCaseNames(cls)) and cls.pairs == 5379
                       and cls.connected_pairs == 96 and cls.native_cases == 4608 and cls.prefixes == 4),
                   'qualification': 'complete renderer control flow; bounded callbacks, no pixel acceptance'}
        (cls.root / 'conker/build/game-viewport-renderer-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')

    def compare(self, memory, slot=0, mutation=0, connected=False):
        retail_code, production_code = {}, {}
        if connected:
            for name, size in LEAVES.items():
                entry = int(name[5:], 16)
                words = struct.unpack_from('>' + str(size) + 'I', self.rom, 0x2D4B0 + entry - 0x15000000)
                retail_code.update(zip(range(entry, entry + size * 4, 4), words))
                production_code.update(zip(range(entry, entry + len(self.production[name]) * 4, 4),
                                           self.production[name]))
        expected = RendererOracle(self.retail, memory, slot, self.table, retail_code, mutation).run()
        actual = RendererOracle(self.production['func_1510B9D0'], memory, slot,
                                self.table, production_code, mutation).run()
        self.assertEqual(actual.events, expected.events)
        self.assertEqual(actual.r[2], expected.r[2])
        self.assertEqual(actual.global_stores, expected.global_stores)
        visible = lambda fixture: {a: v for a, v in fixture.memory.items()
                                   if not queue.STACK - 0x300 <= a < queue.STACK + 0x40}
        left, right = visible(actual), visible(expected)
        differences = [(hex(a), left.get(a), right.get(a)) for a in left.keys() | right.keys()
                       if left.get(a) != right.get(a)]
        self.assertEqual(differences[:16], [], 'first visible byte differences')
        type(self).coverage.update(pc for pc in actual.visits if ENTRY <= pc < ENTRY + 356 * 4)
        type(self).retail_coverage.update(pc for pc in expected.visits if ENTRY <= pc < ENTRY + 356 * 4)
        type(self).pairs += 1
        type(self).connected_pairs += int(connected)
        return actual, expected

    def test_categories_slots_pages_and_all_optional_passes(self):
        for slot, page, category, draw, special, second, third, effect, no_light in itertools.product(
                range(4), range(2), (0, 5, 0x13, 0x14, 0x1A, 0x32, 0x33, 0x35, 0x36),
                range(2), range(2), range(2), range(2), range(2), range(2)):
            with self.subTest(slot=slot, page=page, category=category, draw=draw,
                              special=special, second=second, third=third, effect=effect, no_light=no_light):
                self.compare(case(slot, page, category, draw=draw, special=special,
                                  second=second, third=third, effect=effect, no_light=no_light), slot)

    def test_every_category_byte_and_switch_table_provenance(self):
        targets = {0x13: 0x1510BB6C, 0x14: 0x1510BB4C, 0x1A: 0x1510BB5C,
                   0x33: 0x1510BB8C, 0x35: 0x1510BB7C}
        self.assertEqual(list(self.table), [targets.get(i, 0x1510BB98) for i in range(0x13, 0x36)])
        for category in (*range(256), -1, -2147483648, 2147483647):
            self.compare(case(category=category))

    def test_suppression_modes_and_per_slot_mask_capture(self):
        for slot, mode, enabled, mask in itertools.product(range(4), (0, 1, 2, 255),
                                                          (0, 1, 255), (0, 1, 2, 4, 8, 15, 65535)):
            actual, _ = self.compare(case(slot=slot, category=0x35, mode=mode, enabled=enabled,
                                          mask=mask, draw=1, special=1, second=1, third=1, effect=1), slot)
            suppressed = mode == 1 and enabled != 0 or mask & (1 << slot)
            self.assertEqual(any(event[0] == 0x1515E544 for event in actual.events), not suppressed)

    def test_callbacks_mutate_captured_and_reloaded_state(self):
        for slot, mutation in itertools.product(range(3), range(1, 9)):
            actual, _ = self.compare(case(slot=slot, category=0x35, draw=1, special=1,
                                          mask=1 << slot if mutation == 8 else 0), slot, mutation)
            events = actual.events
            if mutation == 1:
                self.assertTrue(any(event[0] == 0x1515E544 for event in events))
            if mutation == 2:
                self.assertEqual(next(e[1][1] for e in events if e[0] == 0x1512E5F0),
                                 ACTORS + slot * 0x9A0)
            if mutation == 3:
                args = next(e[1] for e in events if e[0] == 0x1515D914)
                self.assertEqual(args[2:5], (15, (-16) & 0xFFFFFFFF, 17))
                self.assertEqual(args[8], 0x800D9BD0 + slot * 16 + 8)
            if mutation == 7:
                args = next(e[1] for e in events if e[0] == 0x1515E544)
                self.assertEqual(args[1:], (0x87654321, 252, 251, 0x800D9BD0 + slot * 16 + 8))
            if mutation == 8:
                self.assertFalse(any(event[0] == 0x1515E544 for event in events))

    def test_effect_byte_and_flag_gates_are_independent(self):
        for slot, byte, flags in itertools.product(range(4), (0, 1, 255), (0, 1, 8, 0xFFFFFFFF)):
            memory = case(slot=slot, draw=1, special=1)
            palette.put(memory, ACTORS + slot * 0x9A0 + 0x8B8, byte, 1)
            palette.put(memory, ACTORS + slot * 0x9A0 + 0x84, flags, 4)
            actual, _ = self.compare(memory, slot)
            self.assertEqual(any(event[0] == 0x1512E5F0 for event in actual.events),
                             byte != 0 and bool(flags & 8))

    def test_connected_actual_helper_updater_color_and_identity(self):
        for slot, page, category, draw, special in itertools.product(range(4), range(2),
                                                                     (0, 0x13, 0x35), range(2), range(2)):
            self.compare(case(slot, page, category, draw=draw, special=special,
                              second=1, third=1, effect=1), slot, connected=True)

    def test_native_actual_helper_color_and_complete_renderer_control(self):
        self.run_host(r'''
static const int categories[]={0,5,0x13,0x14,0x1A,0x32,0x33,0x35,0x36};
int slot,page,c,draw,special,second,third,effect,suppressed,i,n,packets;
u32 expected[24],category; Gfx *end;
for(slot=0;slot<4;slot++) for(page=0;page<2;page++) for(c=0;c<9;c++)
for(draw=0;draw<2;draw++) for(special=0;special<2;special++)
for(second=0;second<2;second++) for(third=0;third<2;third++)
for(effect=0;effect<2;effect++) for(suppressed=0;suppressed<2;suppressed++) {
    category=categories[c]; n=0; packets=18;
    initialize(slot,page,category,draw,special,second,third,effect,suppressed);
    expected[n++]=0x1510CB10;
    if(!suppressed) {
        u32 callback=category==0x14?0x150C8600:category==0x1A?0x15100464:
            category==0x13?0x150DFBD0:category==0x35?0x150CF5E8:
            category==0x33?0x150D765C:0;
        if(callback) { expected[n++]=callback; packets++; }
    }
    expected[n++]=0x1510F800; expected[n++]=0x1515D914; packets++;
    if(!suppressed) {
        if(category!=5) {
            if(draw) {
                packets++;
                if(special) {
                    if(category!=0x14&&category!=0x33&&category!=0x32) expected[n++]=0x150A5378;
                    packets++;
                    if(second) {
                        packets+=4;
                        if(category==0x35) { expected[n++]=0x150CF5E8; packets++; }
                    }
                    if(effect) { expected[n++]=0x1512E5F0; packets+=2; }
                } else packets++;
            } else packets++;
        }
        expected[n++]=0x1515E544; packets++;
        if(third) packets+=4;
    }
    expected[n++]=0x151742EC; packets+=2;
    end=func_1510B9D0(commands+1,(s16)slot);
    if(error||count!=n||end!=commands+1+packets) return 1;
    for(i=0;i<n;i++) if(events[i]!=expected[i]) return 2;
    if(commands[13].words.w0!=0xDC08000A||commands[14].words.w0!=0xDC08060A
       ||commands[13].words.w1!=(u32)(D_800D9B90+page*32)
       ||commands[14].words.w1!=(u32)(D_800D9B90+page*32+16)) return 3;
    if(end[-1].words.w0!=0xE7000000||end[-1].words.w1!=0
       ||commands[0].words.w0!=0xA5A5A5A5||end->words.w0!=0xA5A5A5A5) return 4;
    if(D_800BEBA0!=(suppressed||category==5||!draw||!special?1:0)) return 5;
}
''')
        type(self).native_cases += 4608

    def test_signed_halfword_interface_and_coordinate_truncation(self):
        for raw in (0x10000, 0x10001, 0xFFFF0002, 0xABCD0003):
            row = raw & 3
            self.compare(case(slot=row), raw)
        for coords in ((0.0, -0.0, -0.5), (-1.75, 0.75, 8388607.5),
                       (-2147483648.0, 2147483520.0, -123.875)):
            actual, _ = self.compare(case(coords=coords))
            args = next(e[1] for e in actual.events if e[0] == 0x1515D914)
            self.assertEqual(args[2:5], tuple(math.trunc(floating(bits(x))) & 0xFFFFFFFF for x in coords))

    def test_invalid_slot_prefixes_keep_original_side_effects(self):
        for raw in (-1, 4, 0x8000, 0x7FFF):
            memory = case()
            expected = RendererOracle(self.retail, memory, raw, self.table)
            actual = RendererOracle(self.production['func_1510B9D0'], memory, raw, self.table)
            for fixture in (expected, actual):
                with self.assertRaisesRegex(AssertionError, 'unmapped read'):
                    fixture.run()
            self.assertEqual(actual.events, expected.events)
            self.assertEqual(actual.global_stores, expected.global_stores)
            self.assertEqual(actual.r[2], expected.r[2])
            type(self).prefixes += 1

    def test_output_fence_rejects_unowned_writes(self):
        fixture = RendererOracle(self.retail, case(), 0, self.table)
        for address in (queue.OUTPUT - 4, queue.OUTPUT + 0x1000, PRIMARY, BASE):
            with self.assertRaisesRegex(AssertionError, 'output fence'):
                fixture.put(address, 0, 4)

    def test_fresh_source_compile_reproduces_linked_body(self):
        source, obj, elf = [self.path / ('independent' + suffix) for suffix in ('.c', '.o', '.elf')]
        source.write_text(self.declarations + '\nextern Gfx *func_1510B7B4(Gfx *, s32);\n' + self.body + '\n')
        result = subprocess.run([str(self.root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
            '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
            '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32',
            '-I', 'include', '-I', 'include/2.0L', '-I', 'include/2.0L/PR', '-I', 'include/libc',
            '-O2', '-g3', '-mips2', '-o32', '-o', str(obj), str(source)],
            cwd=self.root / 'conker', capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        script = self.path / 'independent.ld'
        script.write_text('SECTIONS { .text 0x1510B9D0 : SUBALIGN(4) { *(.text) } }\n')
        args = ['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
                '-T', 'undefined_syms.us.txt', '-T', 'undefined_syms_auto.txt',
                '-e', 'func_1510B9D0', '-o', str(elf), str(obj)]
        args += ['--defsym=func_%08X=0x%08X' % (address, address) for address in SPECS]
        result = subprocess.run(args, cwd=self.root / 'conker', capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        functions, _, addresses = match_progress.load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        words = functions['func_1510B9D0']
        self.assertEqual(addresses['func_1510B9D0'], ENTRY)
        self.assertEqual(words[:347], self.production['func_1510B9D0'][:347])
        self.assertFalse(any(words[347:]))

    def test_source_and_slot_contract(self):
        words = self.production['func_1510B9D0']
        self.assertEqual(len(words), 356)
        self.assertEqual(self.addresses['func_1510B9D0'], ENTRY)
        self.assertIn('Gfx *func_1510B9D0(Gfx *arg0, s16 arg1)', self.body)
        self.assertIn('u8 *actor = D_800DBFF0 + offset', self.body)
        self.assertNotIn(',func_1510B9D0,', (self.root / 'conker/retail_word_patches.us.csv').read_text())
        self.assertEqual(max(i for i, word in enumerate(words) if word == 0x03E00008) + 2, 347)
        self.assertFalse(any(words[347:]))
        self.assertEqual(words[0], 0x27BDFF48)
        self.assertEqual(sum(a != b for a, b in zip(words, self.retail)), 343)
        self.assertEqual(hashlib.sha256(struct.pack('>356I', *words)).hexdigest(),
                         '8ee7028e5868defa0388d7b4ec082af1bb41d711f9a0a6433b86c7a0afc7d01f')
        self.assertFalse(any(word >> 26 == 0 and word & 63 == 8 and word >> 21 & 31 != 31
                             for word in words))
        self.assertIn('Gfx *func_1510B9D0(Gfx *arg0, s16 arg1);',
                      (self.root / 'conker/include/functions.h').read_text())
        self.assertIn('(s32) func_1510B9D0((Gfx *) temp_s0, arg1)',
                      (self.root / 'conker/src/game_45B80.c').read_text())
        for name, expected in (
                ('func_15019464', 'dabbc7a11a875291b6fab2f75d2aaa046833d372ec228b7e2327a687b77cdac8'),
                ('func_1510B7B4', '3f8226f75dae50f3e03d73ed53ac6f6bedabbe5b831946646c59856150c4247a'),
                ('func_1510B32C', '1d1156abe599b3f2474a382805b158a19073bd10f6a273c4e72de1927b0bc317'),
                ('func_1510B958', '3b4951f5cfb30124cdb1616129dd0a5550a80c40c8f3b0d5ec6c649fe7b399fc')):
            slot = self.production[name]
            self.assertEqual(hashlib.sha256(struct.pack('>' + str(len(slot)) + 'I', *slot)).hexdigest(), expected)
        self.compare(case())

    def test_z_reachable_words_exclude_proven_dead_paths_and_padding(self):
        all_c = set(range(ENTRY, ENTRY + 347 * 4, 4))
        self.assertEqual(all_c - self.coverage, {0x1510BB48, 0x1510BB64, 0x1510BB80, 0x1510BB9C})
        all_retail = set(range(ENTRY, ENTRY + 356 * 4, 4))
        self.assertEqual(all_retail - self.retail_coverage, set(range(0x1510BE60, 0x1510BE98, 4)))


if __name__ == '__main__':
    unittest.main()
