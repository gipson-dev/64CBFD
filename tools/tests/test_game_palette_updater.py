"""Actual palette C and bounded retail traces, not FCSR or renderer acceptance."""

import csv
import hashlib
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
from tools.tests import test_game_queued_segment_writer as queue
from tools.tests import test_game_random_curve_record as curve
from tools.tests.game_animation_timeline_oracle import TimelineOracle, bits, floating, signed
from tools.tests.test_game_dual_matrix_emitter import sdk_macro


PHASE = 0x800D9E70
INCREMENT = 0x800D9E88
AMPLITUDE = 0x800D9E98
CURRENT = 0x800D9EA8
DEFAULT = 0x800D9EB4
TARGET = 0x800D9EB8
BASE = 0x800DBFF0
TICKS = 0x800BE9E4
ACTORS = 0x100000
ENTRY = 0x1510CB10
TRIG = 0x150489B0


def put(memory, address, value, size):
    memory.update({address + i: byte for i, byte in
                   enumerate((value & ((1 << (size * 8)) - 1)).to_bytes(size, 'big'))})


def updater_case(row, custom=True, ticks=1, count=0, entries=()):
    memory = queue.memory_case(count, entries)
    memory.update({a: 0xA5 for a in range(queue.PRIMITIVE - 16, TARGET + 20)})
    memory.update({a: 0xA5 for a in range(ACTORS - 16, ACTORS + 4 * 0x9A0 + 16)})
    memory.update({a: 0xA5 for a in range(queue.STACK - 0x80, queue.STACK + 0x20)})
    put(memory, BASE, ACTORS, 4)
    put(memory, TICKS, ticks, 4)
    for slot in range(4):
        put(memory, ACTORS + slot * 0x9A0 + 0x5F0, 1, 4)
        for channel in range(3):
            put(memory, PHASE + slot * 6 + channel * 2, (channel + 1) * 16, 2)
            put(memory, INCREMENT + slot * 3 + channel, channel + 1, 1)
            put(memory, AMPLITUDE + slot * 3 + channel, (17, 128, 255)[channel], 1)
            put(memory, CURRENT + slot * 3 + channel, (0, 127, 255)[channel], 1)
            put(memory, TARGET + slot * 3 + channel, (1, 128, 254)[channel], 1)
            put(memory, queue.PRIMITIVE + slot * 3 + channel, (0, 127, 255)[channel], 1)
            put(memory, queue.ENVIRONMENT + slot * 3 + channel, (255, 128, 0)[channel], 1)
    for channel, value in enumerate((0, 128, 255)):
        put(memory, DEFAULT + channel, value, 1)
    if not custom:
        put(memory, TARGET + row * 3, 0, 1)
    return memory


class PaletteUpdaterOracle(queue.SegmentQueueOracle):
    """Extend the existing low-word leaf oracle for finite palette arithmetic."""

    def __init__(self, words, memory, row, samples, mutation=0):
        super().__init__(words, ENTRY, memory, [row])
        self.row, self.samples, self.mutation = row, samples, mutation
        self.events = []

    def peek(self, address, size):
        return TimelineOracle.get(self, address, size)

    def hook(self, target):
        assert target == TRIG, ('unexpected palette callback', target)
        index = len(self.events)
        assert index < 3 and 0 <= self.r[4] <= 255
        snapshot = tuple(self.peek(base + self.row * 3 + i, 1)
                         for base in (CURRENT, TARGET, queue.PRIMITIVE, queue.ENVIRONMENT, AMPLITUDE, INCREMENT)
                         for i in range(3))
        phases = tuple(self.peek(PHASE + self.row * 6 + i * 2, 2) for i in range(3))
        self.events.append((self.r[4], snapshot, phases, self.peek(TICKS, 4)))
        if index == 0:
            row = self.row
            if self.mutation == 1:
                self.put(TICKS, 100, 4)
                self.put(BASE, 0, 4)
                self.put(TARGET + row * 3, 0 if self.peek(TARGET + row * 3, 1) else 255, 1)
            elif self.mutation == 2:
                self.put(CURRENT + row * 3, 7, 1)
                self.put(CURRENT + row * 3 + 1, 50, 1)
                self.put(TARGET + row * 3 + 1, 51, 1)
                self.put(DEFAULT + 1, 99, 1)
            elif self.mutation == 3:
                self.put(PHASE + row * 6, 0xFFFE, 2)
                self.put(INCREMENT + row * 3, 253, 1)
                self.put(AMPLITUDE + row * 3, 250, 1)
            elif self.mutation == 4:
                self.put(queue.PRIMITIVE + row * 3, 200, 1)
                self.put(queue.ENVIRONMENT + row * 3, 255, 1)
            elif self.mutation == 5:
                self.put(PHASE + row * 6 + 2, 0xFFF0, 2)
                self.put(INCREMENT + row * 3 + 1, 255, 1)
                self.put(AMPLITUDE + row * 3 + 1, 40, 1)
            elif self.mutation == 6:
                self.put(ACTORS + row * 0x9A0 + 0x5F0, 0, 4)
                self.put(TARGET + row * 3 + 2, 0, 1)
        for register in (2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.f[0] = bits(self.samples[index])

    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        rd, shift, fn = word >> 11 & 31, word >> 6 & 31, word & 63
        if op == 0 and fn in (2, 3):
            value = signed(self.r[rt]) if fn == 3 else self.r[rt]
            self.r[rd] = (value >> shift) & 0xFFFFFFFF
            self.r[0] = 0
        elif op == 17 and rs == 20 and fn == 32:
            self.f[shift] = bits(signed(self.f[rd]))
        elif op == 17 and rs == 16 and fn == 13:
            value = math.trunc(floating(self.f[rd]))
            assert -0x80000000 <= value < 0x80000000, 'outside qualified signed conversion'
            self.f[shift] = value & 0xFFFFFFFF
        else:
            super().execute(word)

    def run(self):
        pc = ENTRY
        for _ in range(4000):
            self.visits.add(pc)
            word = self.code[pc]
            op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
            immediate = word & 65535
            offset = immediate if immediate < 32768 else immediate - 65536
            if op in (1, 4, 5, 6, 7, 20, 21):
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
                target = ((pc + 4) & 0xF0000000) | ((word & 0x3FFFFFF) << 2)
                self.r[31] = pc + 8
                self.visits.add(pc + 4)
                self.execute(self.code[pc + 4])
                self.hook(target)
                pc += 8
            elif op == 0 and word & 63 == 8:
                target = self.r[rs]
                self.visits.add(pc + 4)
                self.execute(self.code[pc + 4])
                assert target == 0xDEAD0000
                for register in (*range(16, 24), 28, 29, 30, 31):
                    assert self.r[register] == self.before[register], ('saved register', register)
                return self
            else:
                self.execute(word)
                pc += 4
        raise AssertionError('palette instruction budget exhausted')


class GamePaletteUpdaterTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host
    leaf_compare = queue.GameQueuedSegmentWriterTests.compare
    test_complete_init_debugger_and_game_data_remain_exact = (
        queue.GameQueuedSegmentWriterTests.test_complete_init_debugger_and_game_data_remain_exact)

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_139FC0.c').read_text()
        cls.names = ('func_1510CB10', 'func_1510CDB8', 'func_1510D8C0', 'func_1510D864', 'func_1510D874')
        cls.bodies = {name: re.search(r'(?:void|Gfx \*)\s*' + name + r'\([^;{}]+\) \{\n.*?\n\}',
                                     source, re.S).group(0) for name in cls.names}
        cls.paired, cls.prefix_pairs = dict.fromkeys(cls.names, 0), 0
        cls.native_cases = {}
        cls.types = ('typedef unsigned char u8; typedef unsigned short u16; typedef unsigned int u32;\n'
                     'typedef int s32; typedef float f32;\n'
                     'typedef struct { struct { u32 w0,w1; } words; } Gfx;\n')
        cls.declarations = ('extern u8 *D_800DBFF0; extern s32 D_800BE9E4;\n'
                            'extern u16 D_800D9E70[4][3]; extern u8 D_800D9EB4[3];\n'
                            'extern u8 D_800D9B68[4][3], D_800D9B78[4][3], D_800D9E88[4][3],\n'
                            'D_800D9E98[4][3], D_800D9EA8[4][3], D_800D9EB8[4][3];\n'
                            'f32 func_150489B0(u8);\n')
        gbi = (cls.root / 'conker/include/2.0L/PR/gbi.h').read_text()
        mbi = (cls.root / 'conker/include/2.0L/PR/mbi.h').read_text()
        macros = sdk_macro(mbi, '_SHIFTL')
        for name in ('G_MOVEWORD', 'G_MW_SEGMENT', 'gDma1p', 'gMoveWd', 'gSPSegment',
                     'G_SETPRIMCOLOR', 'G_SETENVCOLOR', 'gDPSetColor', 'DPRGBColor',
                     'gDPSetPrimColor', 'gDPSetEnvColor'):
            macros += sdk_macro(gbi, name)
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        config = yaml.safe_load((cls.root / 'conker/conker.us.yaml').read_text())
        assert hashlib.sha1(cls.rom).hexdigest() == config['sha1']
        segment = next(s for s in config['segments'] if isinstance(s, dict) and s.get('name') == 'game_data')
        table_offset = segment['start'] + 0x8009A220 - segment['vram']
        table = struct.unpack_from('>65f', cls.rom, table_offset)
        assert all(math.isfinite(value) and -1 <= value <= 1 for value in table)
        cls.table_bits = [bits(value) for value in table]
        initializer = ','.join(value.hex() + 'f' for value in table)
        trig_source = (cls.root / 'conker/src/game_75E60.c').read_text()
        trig = re.search(r'f32 func_150489B0\([^;{}]+\) \{\n.*?\n\}', trig_source, re.S).group(0)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = cls.types + macros + 'static const f32 quarter[65]={' + initializer + '};\n' + r'''
static union { u32 alignment; u8 bytes[0x400]; } paletteStorage;
static union { u32 alignment; u8 bytes[4*0x9A0+32]; } actorStorage;
static union { u32 alignment; u8 bytes[152]; } queueStorage;
#define D_800D9B68 ((u8 (*)[3])(paletteStorage.bytes+16))
#define D_800D9B78 ((u8 (*)[3])(paletteStorage.bytes+32))
#define D_800D9E70 ((u16 (*)[3])(paletteStorage.bytes+0x318))
#define D_800D9E88 ((u8 (*)[3])(paletteStorage.bytes+0x330))
#define D_800D9E98 ((u8 (*)[3])(paletteStorage.bytes+0x340))
#define D_800D9EA8 ((u8 (*)[3])(paletteStorage.bytes+0x350))
#define D_800D9EB4 (paletteStorage.bytes+0x35C)
#define D_800D9EB8 ((u8 (*)[3])(paletteStorage.bytes+0x360))
#define D_800D9ED0 queueStorage.bytes[8]
#define D_800D9ED8 (queueStorage.bytes+16)
u8 *D_800DBFF0;
s32 D_800BE9E4;
static Gfx commands[20];
static f32 samples[3], trigStorage[449];
static int row, calls, error, mutation, actualTrig;
static u8 angles[3], captured[3];
#define D_8009A020 (trigStorage+16)
#define D_8009A220 (trigStorage+144)
#define D_8009A420 (trigStorage+272)
#define D_8009A620 (trigStorage+400)
#define func_150489B0 actual_trig
''' + trig + '\n#undef func_150489B0\n' + r'''
f32 func_150489B0(u8 angle) {
    int index=calls++;
    if(index>=3) { error=1; return 0; }
    angles[index]=angle; captured[index]=D_800D9EA8[row][index];
    if(mutation && index==0) {
        D_800BE9E4=100; D_800DBFF0=0; D_800D9EB8[row][0]=0;
        D_800D9EA8[row][0]=7; D_800D9EA8[row][1]=50;
        D_800D9EB8[row][1]=51; D_800D9EB4[1]=99;
        D_800D9E70[row][0]=0xFFFE; D_800D9E88[row][0]=253;
        D_800D9E98[row][0]=250; D_800D9E98[row][1]=40;
        D_800D9B68[row][0]=200; D_800D9B78[row][0]=255;
    }
    return actualTrig ? actual_trig(angle) : samples[index];
}
static void initialize(int selected,s32 ticks) {
    int i,j;
    for(i=0;i<65;i++) trigStorage[144+i]=quarter[i];
    for(i=0;i<0x400;i++) paletteStorage.bytes[i]=0xA5;
    for(i=0;i<4*0x9A0+32;i++) actorStorage.bytes[i]=0xA5;
    for(i=0;i<152;i++) queueStorage.bytes[i]=0xA5;
    for(i=0;i<20;i++) { commands[i].words.w0=0xA5A5A5A5; commands[i].words.w1=0xA5A5A5A5; }
    D_800DBFF0=actorStorage.bytes+16; D_800BE9E4=ticks; row=selected;
    D_800D9ED0=0; calls=error=mutation=actualTrig=0;
    for(i=0;i<4;i++) {
        *(u32 *)(actorStorage.bytes+16+i*0x9A0+0x5F0)=1;
        for(j=0;j<3;j++) {
            D_800D9E70[i][j]=(u16)((j+1)*16); D_800D9E88[i][j]=(u8)(j+1);
            D_800D9E98[i][j]=17; D_800D9EA8[i][j]=100; D_800D9EB8[i][j]=130;
            D_800D9B68[i][j]=10; D_800D9B78[i][j]=20; samples[j]=0;
        }
    }
    D_800D9EB4[0]=D_800D9EB4[1]=D_800D9EB4[2]=127;
}
static int fences(void) {
    int i;
    for(i=0;i<16;i++) if(paletteStorage.bytes[i]!=0xA5 || paletteStorage.bytes[0x36C+i]!=0xA5
        || actorStorage.bytes[i]!=0xA5 || actorStorage.bytes[16+4*0x9A0+i]!=0xA5) return 0;
    for(i=0;i<8;i++) if(queueStorage.bytes[i]!=0xA5 || queueStorage.bytes[144+i]!=0xA5) return 0;
    return commands[0].words.w0==0xA5A5A5A5 && commands[19].words.w0==0xA5A5A5A5;
}
static f32 expected_trig(u8 angle) {
    int index=angle<=64?angle:angle<=128?128-angle:angle<=192?angle-128:256-angle;
    f32 value=trigStorage[144+index];
    return angle>64 && angle<=192 ? -value : value;
}
''' + '\n'.join(
            cls.bodies[name] for name in cls.names) + '\n'
        cls.production, _, cls.addresses = match_progress.load_elf_functions(
            str(cls.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        cls.retail = {name: list(struct.unpack_from('>' + str(size) + 'I', cls.rom,
                      0x2D4B0 + int(name[5:], 16) - 0x15000000))
                      for name, size in zip(cls.names, (170, 42, 44, 4, 19))}

    @classmethod
    def tearDownClass(cls):
        receipt = {'completed_pairs': sum(cls.paired.values()), 'pairs_by_function': cls.paired,
                   'invalid_index_prefix_pairs': cls.prefix_pairs, 'native_cases': cls.native_cases,
                   'complete_module_corpus': (sum(cls.paired.values()) == 1251
                                              and cls.prefix_pairs == 3
                                              and sum(cls.native_cases.values()) == 398353),
                   'qualification': 'finite palette products; bounded low-word model, no FCSR/hardware acceptance'}
        (cls.root / 'conker/build/game-palette-updater-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')
        print('palette updater qualification:', receipt)

    def compare(self, memory, row, samples=(0, 0, 0), mutation=0):
        runs = [PaletteUpdaterOracle(words, memory, row, samples, mutation).run()
                for words in (self.retail['func_1510CB10'], self.production['func_1510CB10'])]
        actual, retail = runs[1], runs[0]
        external = lambda a: not queue.STACK - 0x80 <= a < queue.STACK + 0x20
        self.assertEqual({a: v for a, v in actual.memory.items() if external(a)},
                         {a: v for a, v in retail.memory.items() if external(a)})
        self.assertEqual([store for store in actual.stores if external(store[0])],
                         [store for store in retail.stores if external(store[0])])
        self.assertEqual(actual.events, retail.events)
        actual.retail_visits = retail.visits
        type(self).paired['func_1510CB10'] += 1
        return actual

    def test_native_disabled_flags_preserve_every_palette_byte(self):
        self.run_host(r'''
static u32 flags[]={0,2,0x80000000,0xFFFFFFFE};
u8 before[0x400]; int i,j,k;
for(i=0;i<4;i++) for(j=0;j<4;j++) {
    initialize(i,-1);
    *(u32 *)(actorStorage.bytes+16+i*0x9A0+0x5F0)=flags[j];
    for(k=0;k<0x400;k++) before[k]=paletteStorage.bytes[k];
    func_1510CB10(i);
    if(calls || error || !fences()) return 1;
    for(k=0;k<0x400;k++) if(before[k]!=paletteStorage.bytes[k]) return 2;
}
''')
        type(self).native_cases['disabled_flags'] = 16

    def test_native_all_current_target_bytes_and_signed_step_shapes(self):
        self.run_host(r'''
static s32 ticks[]={-1,1,128};
int a,b,t,j; s32 step,value,difference,magnitude,adjustment; u8 primitive,environment;
for(t=0;t<3;t++) for(a=0;a<256;a++) for(b=0;b<256;b++) {
    initialize(1,ticks[t]);
    for(j=0;j<3;j++) { D_800D9EA8[1][j]=(u8)a; D_800D9EB8[1][j]=(u8)b; D_800D9EB4[j]=(u8)b; }
    step=(s32)((u32)ticks[t]<<1); value=a; difference=b-a;
    magnitude=difference<0?-difference:difference;
    if(difference) value=magnitude<step?b:(s32)((u32)a+(difference<0?0u-(u32)step:(u32)step));
    adjustment=(s32)((u32)value-127);
    primitive=adjustment>=0?(u8)(10u+(u32)adjustment):10;
    environment=adjustment<0?(u8)(20u-(u32)adjustment):20;
    if(primitive>=128) primitive=127;
    if(environment>=128) environment=127;
    func_1510CB10(1);
    if(calls!=3 || error || D_800D9EB8[1][0] || !fences()) return 1;
    for(j=0;j<3;j++) if(D_800D9EA8[1][j]!=(u8)value
        || D_800D9B68[1][j]!=primitive || D_800D9B78[1][j]!=environment) return 2;
}
''')
        type(self).native_cases['current_target_step'] = 3 * 256 * 256

    def test_native_all_color_bytes_wrap_before_clamp_not_saturating_addition(self):
        self.run_host(r'''
static f32 values[]={-0.5f,0,0.5f};
int p,e,v,j; s32 adjustment; u8 primitive,environment;
for(v=0;v<3;v++) for(p=0;p<256;p++) for(e=0;e<256;e++) {
    initialize(2,0);
    for(j=0;j<3;j++) {
        D_800D9EA8[2][j]=D_800D9EB8[2][j]=127; D_800D9E98[2][j]=255;
        D_800D9B68[2][j]=(u8)p; D_800D9B78[2][j]=(u8)e; samples[j]=values[v];
    }
    adjustment=v==0?-127:v==1?0:127;
    primitive=adjustment>=0?(u8)((u32)p+(u32)adjustment):(u8)p;
    environment=adjustment<0?(u8)((u32)e-(u32)adjustment):(u8)e;
    if(primitive>=128) primitive=127;
    if(environment>=128) environment=127;
    func_1510CB10(2);
    if(calls!=3 || error || !fences()) return 1;
    for(j=0;j<3;j++) if(D_800D9B68[2][j]!=primitive || D_800D9B78[2][j]!=environment) return 2;
}
''')
        type(self).native_cases['color_wrap_clamp'] = 3 * 256 * 256

    def test_native_callback_captures_and_late_table_reloads(self):
        self.run_host(r'''
initialize(3,1); mutation=1; samples[1]=0.5f;
func_1510CB10(3);
if(calls!=3 || error || !fences() || D_800DBFF0 || D_800BE9E4!=100 || D_800D9EB8[3][0]) return 1;
if(captured[0]!=102 || captured[1]!=51 || captured[2]!=102
   || angles[0]!=1 || angles[1]!=2 || angles[2]!=3) return 2;
if(D_800D9EA8[3][0]!=7 || D_800D9EA8[3][1]!=51 || D_800D9EA8[3][2]!=102) return 3;
if(D_800D9B68[3][0]!=127 || D_800D9B78[3][0]!=24
   || D_800D9B68[3][1]!=10 || D_800D9B78[3][1]!=76
   || D_800D9B68[3][2]!=10 || D_800D9B78[3][2]!=45) return 4;
if(D_800D9E70[3][0]!=251 || D_800D9E70[3][1]!=34 || D_800D9E70[3][2]!=51) return 5;
''')
        type(self).native_cases['callback_mutation'] = 1

    def test_native_actual_trig_updater_color_and_queue_writer_connection(self):
        self.run_host(r'''
static u8 amplitudes[]={0,1,127,128,255};
int slot,angle,a,j; s32 adjustment; u8 primitive,environment; u32 rgbp,rgbe; Gfx *end;
for(j=0;j<449;j++) trigStorage[j]=0;
for(j=0;j<65;j++) trigStorage[144+j]=quarter[j];
for(slot=0;slot<4;slot++) for(angle=0;angle<256;angle++) for(a=0;a<5;a++) {
    initialize(slot,0); actualTrig=1;
    for(j=0;j<3;j++) {
        D_800D9EA8[slot][j]=D_800D9EB8[slot][j]=127;
        D_800D9E70[slot][j]=(u16)(angle<<4); D_800D9E88[slot][j]=13;
        D_800D9E98[slot][j]=amplitudes[a];
    }
    func_1510D874(-1,0x12345678,0xFEDCBA98,128,255);
    adjustment=(s32)(expected_trig((u8)angle)*(f32)amplitudes[a]);
    primitive=adjustment>=0?(u8)(10u+(u32)adjustment):10;
    environment=adjustment<0?(u8)(20u-(u32)adjustment):20;
    if(primitive>=128) primitive=127;
    if(environment>=128) environment=127;
    func_1510CB10(slot);
    end=func_1510D8C0(func_1510CDB8(commands+1,-1,0x12345678,slot),-1);
    rgbp=(u32)primitive*0x01010100u|255u; rgbe=(u32)environment*0x01010100u|0x78u;
    if(calls!=3 || error || end!=commands+5 || D_800D9ED0!=1 || !fences()) return 1;
    if(commands[1].words.w0!=0xFA00F200 || commands[1].words.w1!=rgbp
       || commands[2].words.w0!=0xFB000000 || commands[2].words.w1!=rgbe
       || commands[3].words.w0!=0xDB060200 || commands[3].words.w1!=0x12345678
       || commands[4].words.w0!=0xDB0603FC || commands[4].words.w1!=0xFEDCBA98) return 2;
    for(j=0;j<3;j++) if(angles[j]!=(u8)angle || D_800D9E70[slot][j]!=((angle*16+13)&4095)
        || D_800D9B68[slot][j]!=primitive || D_800D9B78[slot][j]!=environment) return 3;
}
''')
        type(self).native_cases['actual_trig_color_writer'] = 4 * 256 * 5

    def test_big_endian_disabled_gate_does_not_read_ticks_or_palette_tables(self):
        for row in range(4):
            for flags in (0, 2, 0x80000000, 0xFFFFFFFE):
                memory = updater_case(row)
                put(memory, ACTORS + row * 0x9A0 + 0x5F0, flags, 4)
                memory = {a: v for a, v in memory.items()
                          if not queue.PRIMITIVE - 16 <= a < TARGET + 20
                          and not TICKS <= a < TICKS + 4}
                result = self.compare(memory, row)
                self.assertFalse(result.events)
                self.assertEqual([store for store in result.stores if store[0] >= 0x80000000], [])

    def test_big_endian_rows_selectors_signed_steps_and_finite_products(self):
        samples = ((-1, 0, 1), (0.5, -0.5, 0.125), (0.99999, -0.99999, 2))
        for row in range(4):
            for custom in (False, True):
                for ticks in (-2, 0, 1, 2, 128, 0x7FFFFFFF, -0x80000000, 0x40000000):
                    for phase in (0, 4095, 65535):
                        for values in samples:
                            memory = updater_case(row, custom, ticks)
                            for channel in range(3):
                                put(memory, PHASE + row * 6 + channel * 2, phase, 2)
                            result = self.compare(memory, row, values)
                            self.assertEqual(len(result.events), 3)
                            self.assertEqual([event[0] for event in result.events], [(phase >> 4) & 255] * 3)
                            self.assertEqual(result.memory[TARGET + row * 3], 0)

    def test_big_endian_callback_mutations_preserve_capture_and_reload_contracts(self):
        for row in range(4):
            for custom in (False, True):
                for mutation in range(1, 7):
                    for values in ((-1, 0, 1), (0.5, -0.5, 0.125), (0, 1, -1)):
                        self.compare(updater_case(row, custom), row, values, mutation)

    def test_big_endian_complete_reachable_instruction_coverage(self):
        actual_visits, retail_visits = set(), set()
        memory = updater_case(0)
        put(memory, ACTORS + 0x5F0, 0, 4)
        results = [self.compare(memory, 0)]
        for custom in (False, True):
            for ticks in (-2, 0, 1, 128):
                for samples in ((-1, 0, 1), (0.5, -0.5, 0.125)):
                    results.append(self.compare(updater_case(0, custom, ticks), 0, samples))
        for result in results:
            actual_visits.update(result.visits)
            retail_visits.update(result.retail_visits)
        # Unsigned-byte correction paths and branch-over duplicate instructions cannot execute.
        self.assertEqual(set(range(ENTRY, ENTRY + 168 * 4, 4)) - actual_visits,
                         {0x1510CC8C, 0x1510CCC8, 0x1510CCCC, 0x1510CCD0, 0x1510CCD4, 0x1510CD14})
        self.assertEqual(set(range(ENTRY, ENTRY + 170 * 4, 4)) - retail_visits,
                         {0x1510CC94, 0x1510CCD0, 0x1510CCD4, 0x1510CCD8, 0x1510CCDC, 0x1510CD1C})

    def test_big_endian_phase_double_store_wrap_and_default_on_repeat(self):
        for row in range(4):
            for phase in (0, 15, 16, 255, 256, 4094, 4095, 4096, 65534, 65535):
                for increment in (0, 1, 15, 16, 127, 128, 255):
                    memory = updater_case(row)
                    for channel in range(3):
                        put(memory, PHASE + row * 6 + channel * 2, phase, 2)
                        put(memory, INCREMENT + row * 3 + channel, increment, 1)
                    result = self.compare(memory, row)
                    self.assertEqual([(a, s, v) for a, s, v in result.stores
                                      if PHASE + row * 6 <= a < PHASE + row * 6 + 6],
                                     [(PHASE + row * 6 + channel * 2, 2, value)
                                      for channel in range(3) for value in
                                      ((phase + increment) & 65535, (phase + increment) & 4095)])
        memory = updater_case(0, True, 128)
        for channel in range(3):
            put(memory, TARGET + channel, 20 + channel, 1)
            put(memory, DEFAULT + channel, 90 + channel, 1)
        first = self.compare(memory, 0)
        second = self.compare(first.memory, 0)
        self.assertEqual([first.memory[CURRENT + i] for i in range(3)], [20, 21, 22])
        self.assertEqual([second.memory[CURRENT + i] for i in range(3)], [90, 91, 92])

    def test_big_endian_actual_updater_color_writer_repeated_connection(self):
        for row in range(4):
            for count in (0, 1, 8):
                for key in (1, 0xFFFFFFFF):
                    entries = [(key, 0x81230000 + i, 0 if i % 2 else 0xFEDCBA98, 128 + i, 255 - i)
                               for i in range(8)]
                    memory = updater_case(row, count=count, entries=entries)
                    for frame in range(3):
                        updated = self.compare(memory, row, (-1, 0, 1))
                        color = self.leaf_compare(updated.memory, [queue.OUTPUT + 8, -1, frame, row],
                                                  'func_1510CDB8')
                        result = self.leaf_compare(color.memory, [color.r[2], key], 'func_1510D8C0')
                        self.assertEqual(result.r[2], queue.OUTPUT + 24 + (count + (count + 1) // 2) * 8)
                        self.assertEqual(result.memory[queue.COUNT], count)
                        self.assertEqual([value for _, _, value in color.stores],
                            [0xFA00F200, sum(updated.memory[queue.PRIMITIVE + row * 3 + i] << (24 - i * 8)
                                            for i in range(3)) | 255,
                             0xFB000000, sum(updated.memory[queue.ENVIRONMENT + row * 3 + i] << (24 - i * 8)
                                            for i in range(3)) | frame])
                        memory = result.memory

    def test_invalid_slot_indices_qualify_unmapped_flag_read_prefix_only(self):
        for row in (-1, 4, 4096):
            memory = updater_case(0)
            runs = [PaletteUpdaterOracle(words, memory, row, (0, 0, 0))
                    for words in (self.retail['func_1510CB10'], self.production['func_1510CB10'])]
            for result in runs:
                with self.assertRaises(KeyError):
                    result.run()
                self.assertFalse(result.events)
                self.assertFalse([store for store in result.stores if store[0] >= 0x80000000])
            type(self).prefix_pairs += 1

    def test_fresh_ido_identity_frame_retail_slot_and_no_guards(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or shutil.which('mips-linux-gnu-ld') is None:
            self.skipTest('IDO/MIPS tools unavailable')
        source, obj, elf, script = (self.path / ('palette' + suffix) for suffix in ('.c', '.o', '.elf', '.ld'))
        source.write_text(self.types + self.declarations + self.bodies['func_1510CB10'] + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
            '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3',
            '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        script.write_text('SECTIONS { .text 0x1510CB10 : SUBALIGN(4) { *(.text) } }\n')
        definitions = {name: address for name, address in
                       (('D_800DBFF0', BASE), ('D_800BE9E4', TICKS), ('D_800D9E70', PHASE),
                        ('D_800D9E88', INCREMENT), ('D_800D9E98', AMPLITUDE), ('D_800D9EA8', CURRENT),
                        ('D_800D9EB4', DEFAULT), ('D_800D9EB8', TARGET),
                        ('D_800D9B68', queue.PRIMITIVE), ('D_800D9B78', queue.ENVIRONMENT),
                        ('func_150489B0', TRIG))}
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1510CB10',
            *['--defsym=%s=0x%X' % pair for pair in definitions.items()],
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        fresh, _, _ = match_progress.load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        words = fresh['func_1510CB10']
        body = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        self.assertEqual(body, 168)
        self.assertEqual(words[body:], [0] * (len(words) - body))
        slot = words[:body] + [0] * (170 - body)
        self.assertEqual(self.production['func_1510CB10'], slot)
        self.assertEqual(self.addresses['func_1510CB10'], ENTRY)
        self.assertEqual(slot[0], 0x27BDFF98)
        self.assertEqual(sum(a != b for a, b in zip(slot, self.retail['func_1510CB10'])), 135)
        self.assertEqual(hashlib.sha256(struct.pack('>170I', *slot)).hexdigest(),
                         '0954376ea7ac52711bb8b9ccc922eb10c0a8cdb8164cb1d84caea013461922e4')
        self.assertEqual([word for word in slot if word >> 26 == 3],
                         [(3 << 26) | ((TRIG >> 2) & 0x3FFFFFF)])
        assembly = (self.root / 'conker/asm/139FC0.s').read_text()
        block = assembly.split('glabel func_1510CB10\n', 1)[1].split('endlabel func_1510CB10', 1)[0]
        self.assertEqual([int(word, 16) for word in re.findall(r'/\*\s*\w+\s*\w+\s+(\w{8})\s*\*/', block)],
                         self.retail['func_1510CB10'])
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] == 'func_1510CB10' for row in csv.DictReader(source)))
        print('palette updater: body 168 / slot 170, frame 0x68, 135 raw differences; no guards')


if __name__ == '__main__':
    unittest.main()
