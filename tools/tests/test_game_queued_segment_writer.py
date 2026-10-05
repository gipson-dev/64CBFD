"""Actual SDK C and bounded big-endian instruction traces, not hardware acceptance."""

import csv
import hashlib
import json
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

from tools import match_progress
from tools.tests.game_animation_timeline_oracle import TimelineOracle, signed
from tools.tests.test_game_dual_matrix_emitter import sdk_macro
from tools.tests import test_game_random_curve_record as curve
from tools.tests import test_game_texture_metadata_and_maintenance as texture


COUNT = 0x800D9ED0
QUEUE = 0x800D9ED8
OUTPUT = 0x20000
STACK = 0x40000
PRIMITIVE = 0x800D9B68
ENVIRONMENT = 0x800D9B78


def memory_case(count, entries, capacity=8):
    memory = {address: 0xA5 for address in range(COUNT - 8, QUEUE + capacity * 16 + 8)}
    memory.update({OUTPUT + i: 0xA5 for i in range(0x1010)})
    memory.update({STACK + i: 0xA5 for i in range(0x20)})
    memory[COUNT] = count
    for index, (key, first, second, segment1, segment2) in enumerate(entries):
        data = struct.pack('>III', key & 0xFFFFFFFF, first & 0xFFFFFFFF, second & 0xFFFFFFFF)
        data += bytes((segment1 & 255, segment2 & 255, 0xA5, 0xA5))
        memory.update({QUEUE + index * 16 + i: value for i, value in enumerate(data)})
    return memory


def palette_case(memory):
    memory = memory.copy()
    memory.update({address: 0xA5 for address in range(PRIMITIVE - 16, ENVIRONMENT + 60)})
    for index in range(12):
        memory[PRIMITIVE + index] = (0x31 + index * 17) & 255
        memory[ENVIRONMENT + index] = (0x93 + index * 29) & 255
    return memory


class SegmentQueueOracle(TimelineOracle):
    """Reuse the low-word oracle for these leaf routines and their delay slots only."""

    def __init__(self, words, entry, memory, arguments):
        self.code = dict(zip(range(entry, entry + len(words) * 4, 4), words))
        self.entry = entry
        self.memory = memory.copy()
        self.r = [0x5A000000 + i for i in range(32)]
        self.r[0] = 0
        for index, argument in enumerate(arguments[:4]):
            self.r[4 + index] = argument & 0xFFFFFFFF
        self.r[29], self.r[31] = STACK, 0xDEAD0000
        self.before = self.r[:]
        self.f, self.lo = [0] * 32, 0
        self.visits, self.writes, self.reads, self.stores = set(), [], [], []
        self.recording = False
        if len(arguments) > 4:
            self.put(STACK + 0x10, arguments[4], 4)
        self.recording = True

    def get(self, address, size):
        value = super().get(address, size)
        self.reads.append((address, size, value))
        return value

    def put(self, address, value, size):
        if self.recording:
            assert all(address + i in self.memory for i in range(size)), ('unmapped store', address, size)
            self.stores.append((address, size, value & ((1 << (8 * size)) - 1)))
        super().put(address, value, size)

    def execute(self, word):
        op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
        if op == 0 and word & 63 == 42:
            self.r[(word >> 11) & 31] = int(signed(self.r[rs]) < signed(self.r[rt]))
            self.r[0] = 0
        elif op == 10:
            imm = word & 0xFFFF
            self.r[rt] = int(signed(self.r[rs]) < (imm if imm < 0x8000 else imm - 0x10000))
            self.r[0] = 0
        else:
            super().execute(word)

    def run(self):
        pc = self.entry
        for _ in range(20000):
            self.visits.add(pc)
            word = self.code[pc]
            op, rs, rt = word >> 26, (word >> 21) & 31, (word >> 16) & 31
            if op in (4, 5, 6, 20, 21):
                imm = word & 0xFFFF
                offset = imm if imm < 0x8000 else imm - 0x10000
                take = signed(self.r[rs]) <= 0 if op == 6 else self.r[rs] == self.r[rt]
                if op in (5, 21):
                    take = not take
                if take or op not in (20, 21):
                    self.visits.add(pc + 4)
                    self.execute(self.code[pc + 4])
                pc = pc + 4 + offset * 4 if take else pc + 8
            elif op == 0 and word & 63 == 8:
                target = self.r[rs]
                self.visits.add(pc + 4)
                self.execute(self.code[pc + 4])
                assert target == 0xDEAD0000, ('unexpected jump', target)
                for index in (*range(16, 24), 28, 29, 30, 31):
                    assert self.r[index] == self.before[index], ('callee-saved register', index)
                return self
            else:
                self.execute(word)
                pc += 4
        raise AssertionError('segment queue instruction budget exhausted')


class GameQueuedSegmentWriterTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host
    test_complete_init_debugger_and_game_data_remain_exact = (
        texture.GameTextureMetadataAndMaintenanceTests.test_shared_header_rebuild_keeps_complete_init_debugger_and_game_data_exact)

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_139FC0.c').read_text()
        cls.names = ('func_1510D864', 'func_1510D874', 'func_1510D8C0', 'func_1510CDB8')
        cls.paired = dict.fromkeys(cls.names, 0)
        cls.prefix_pairs, cls.native_color_cases = 0, 0
        cls.bodies = {name: re.search(r'(?:void|Gfx \*)\s*' + name + r'\([^;{}]+\) \{\n.*?\n\}',
                                     source, re.S).group(0) for name in cls.names}
        cls.types = ('typedef unsigned char u8; typedef unsigned int u32; typedef int s32;\n'
                     'typedef struct { struct { u32 w0,w1; } words; } Gfx;\n')
        gbi = (cls.root / 'conker/include/2.0L/PR/gbi.h').read_text()
        mbi = (cls.root / 'conker/include/2.0L/PR/mbi.h').read_text()
        cls.macros = sdk_macro(mbi, '_SHIFTL')
        for name in ('G_MOVEWORD', 'G_MW_SEGMENT', 'gDma1p', 'gMoveWd', 'gSPSegment',
                     'G_SETPRIMCOLOR', 'G_SETENVCOLOR', 'gDPSetColor', 'DPRGBColor',
                     'gDPSetPrimColor', 'gDPSetEnvColor'):
            cls.macros += sdk_macro(gbi, name)
        cls.declarations = ('extern u8 D_800D9ED0, D_800D9ED8[];\n'
                            'extern u8 D_800D9B68[4][3], D_800D9B78[4][3];\n')
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = cls.types + cls.macros + r'''
static union { u32 alignment; u8 bytes[152]; } storage;
static union { u32 alignment; u8 bytes[48]; } palettes;
#define D_800D9ED0 storage.bytes[8]
#define D_800D9ED8 (storage.bytes+16)
#define D_800D9B68 ((u8 (*)[3])(palettes.bytes+8))
#define D_800D9B78 ((u8 (*)[3])(palettes.bytes+24))
static Gfx commands[18];
static void reset(void) {
    int i;
    for(i=0;i<152;i++) storage.bytes[i]=0xA5;
    for(i=0;i<48;i++) palettes.bytes[i]=0xA5;
    for(i=0;i<12;i++) { palettes.bytes[8+i]=(u8)(0x31+i*17); palettes.bytes[24+i]=(u8)(0x93+i*29); }
    for(i=0;i<18;i++) { commands[i].words.w0=0xA5A5A5A5; commands[i].words.w1=0xA5A5A5A5; }
    D_800D9ED0=0;
}
static int fences(void) {
    int i;
    for(i=0;i<8;i++) if(storage.bytes[i]!=0xA5 || storage.bytes[144+i]!=0xA5) return 0;
    for(i=9;i<16;i++) if(storage.bytes[i]!=0xA5) return 0;
    for(i=0;i<8;i++) if(palettes.bytes[i]!=0xA5) return 0;
    for(i=20;i<24;i++) if(palettes.bytes[i]!=0xA5) return 0;
    for(i=36;i<48;i++) if(palettes.bytes[i]!=0xA5) return 0;
    return commands[0].words.w0==0xA5A5A5A5 && commands[0].words.w1==0xA5A5A5A5
        && commands[17].words.w0==0xA5A5A5A5 && commands[17].words.w1==0xA5A5A5A5;
}
''' + '\n'.join(cls.bodies[name] for name in cls.names) + '\n'
        cls.production, _, cls.addresses = match_progress.load_elf_functions(
            str(cls.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        config = yaml.safe_load((cls.root / 'conker/conker.us.yaml').read_text())
        assert hashlib.sha1(cls.rom).hexdigest() == config['sha1']
        cls.retail = {name: list(struct.unpack_from('>' + str(size) + 'I', cls.rom,
                     0x2D4B0 + int(name[5:], 16) - 0x15000000))
                      for name, size in zip(cls.names, (4, 19, 44, 42))}

    @classmethod
    def tearDownClass(cls):
        receipt = {'completed_pairs': sum(cls.paired.values()), 'pairs_by_function': cls.paired,
                   'invalid_index_prefix_pairs': cls.prefix_pairs,
                   'native_color_cases': cls.native_color_cases,
                   'complete_module_corpus': (sum(cls.paired.values()) == 1710
                                              and cls.prefix_pairs == 3
                                              and cls.native_color_cases == 262144),
                   'qualification': 'bounded low-word big-endian model; no hardware/render acceptance'}
        (cls.root / 'conker/build/game-queued-segment-color-qualification.json').write_text(
            json.dumps(receipt, indent=2) + '\n')
        print('queued segment/color qualification:', receipt)

    def compare(self, memory, arguments, name='func_1510D8C0'):
        address = int(name[5:], 16)
        retail = SegmentQueueOracle(self.retail[name], address, memory, arguments).run()
        actual = SegmentQueueOracle(self.production[name], address, memory, arguments).run()
        self.assertEqual(actual.memory, retail.memory)
        self.assertEqual(actual.reads, retail.reads)
        self.assertEqual(actual.stores, retail.stores)
        if name in ('func_1510D8C0', 'func_1510CDB8'):
            self.assertEqual(actual.r[2], retail.r[2])
        actual.retail_visits = retail.visits
        type(self).paired[name] += 1
        return actual

    def test_native_sdk_commands_and_actual_queue_workflow(self):
        self.run_host(r'''
int i,written=0; Gfx *end;
reset(); D_800D9ED0=7; func_1510D864();
if(D_800D9ED0 || storage.bytes[16]!=0xA5) return 1;
for(i=0;i<8;i++) func_1510D874(i%2?-1:3,0x81230000+(u32)i,i%3?0xFFFFFFFF:0,128+i,255-i);
if(D_800D9ED0!=8 || !fences()) return 2;
end=func_1510D8C0(commands+1,-1);
for(i=1;i<8;i+=2) {
    if(commands[1+written].words.w0!=(0xDB060000u|((128u+i)*4))
       || commands[1+written].words.w1!=0x81230000u+(u32)i) return 3;
    written++;
    if(i%3) {
        if(commands[1+written].words.w0!=(0xDB060000u|((255u-i)*4))
           || commands[1+written].words.w1!=0xFFFFFFFF) return 4;
        written++;
    }
}
if(end!=commands+1+written || D_800D9ED0!=8 || !fences()) return 5;
for(i=1+written;i<17;i++) if(commands[i].words.w0!=0xA5A5A5A5 || commands[i].words.w1!=0xA5A5A5A5) return 6;
if(func_1510D8C0(end,0x12345678)!=end || !fences()) return 7;
''')

    def test_native_append_all_count_bytes_capacity_and_segment_truncation(self):
        self.run_host(r'''
int count,i;
for(count=0;count<256;count++) {
    reset(); D_800D9ED0=(u8)count;
    func_1510D874((s32)0x80000000,0,0xFFFFFFFF,-1,256+count);
    if(D_800D9ED0!=(count<8?count+1:count) || !fences()) return 1;
    for(i=0;i<128;i++) {
        if(count<8 && i>=count*16 && i<count*16+14) continue;
        if(D_800D9ED8[i]!=0xA5) return 2;
    }
    if(count<8) {
        u8 *slot=D_800D9ED8+count*16;
        if(*(u32 *)slot!=0x80000000 || *(u32 *)(slot+4) || *(u32 *)(slot+8)!=0xFFFFFFFF
           || slot[12]!=255 || slot[13]!=(u8)count) return 3;
    }
}
''')

    def test_big_endian_actual_reset_append_and_writer_connection(self):
        memory = memory_case(7, [(0xA5A5A5A5,) * 5 for _ in range(8)])
        before = memory.copy()
        result = self.compare(memory, [], 'func_1510D864')
        self.assertEqual(result.memory[COUNT], 0)
        self.assertEqual({a: v for a, v in result.memory.items() if a != COUNT},
                         {a: v for a, v in before.items() if a != COUNT})
        for index in range(9):
            args = [index % 2, 0x81230000 + index, 0 if index % 3 == 0 else 0xFFFFFFFF, 128 + index, 255 - index]
            previous = result.memory.copy()
            previous.update({STACK + 0x10 + i: value for i, value in
                             enumerate(struct.pack('>I', args[4]))})
            result = self.compare(previous, args, 'func_1510D874')
            self.assertEqual(result.memory[COUNT], min(index + 1, 8))
            if index < 8:
                self.assertEqual([(a, s) for a, s, _ in result.stores],
                                 [(QUEUE + index * 16 + offset, size) for offset, size in
                                  ((0, 4), (4, 4), (8, 4), (12, 1))] +
                                 [(COUNT, 1), (QUEUE + index * 16 + 13, 1)])
            else:
                self.assertEqual(result.memory, previous)
                self.assertFalse(result.stores)
        memory = result.memory
        result = self.compare(memory, [OUTPUT + 8, 1])
        self.assertEqual(result.r[2], OUTPUT + 8 + (2 + 1 + 2 + 2) * 8)
        self.assertEqual(result.memory[COUNT], 8)
        self.assertEqual([v for a, s, v in result.stores if a % 8 == 4],
                         [0x81230001, 0xFFFFFFFF, 0x81230003, 0x81230005,
                          0xFFFFFFFF, 0x81230007, 0xFFFFFFFF])

    def test_empty_queue_keeps_arbitrary_cursor_and_never_reads_entries(self):
        for cursor in (0, OUTPUT + 8, 0xFFFFFFF8):
            with self.subTest(cursor=cursor):
                memory = memory_case(0, [])
                result = self.compare(memory, [cursor, 0x80000000])
                self.assertEqual(result.memory, memory)
                self.assertEqual(result.r[2], cursor)
                self.assertEqual(result.reads, [(COUNT, 1, 0)])
                self.assertFalse(result.stores)

    def test_all_segment_bytes_full_addresses_sparse_keys_and_optional_commands(self):
        empty = self.compare(memory_case(0, []), [OUTPUT, 0])
        actual_visits, retail_visits = empty.visits.copy(), empty.retail_visits.copy()
        for segment in range(256):
            for second in (0, 0xFFFFFFFF):
                memory = memory_case(3, [(0x80000000, 0, second, segment, 255 - segment),
                    (0xFFFFFFFF, 0x12345678, 0x89ABCDEF, 1, 2),
                    (0x80000000, 0xE1234567, 0, 255, 0)])
                result = self.compare(memory, [OUTPUT + 8, 0x80000000])
                actual_visits.update(result.visits)
                retail_visits.update(result.retail_visits)
                values = [v for _, _, v in result.stores]
                expected = [0xDB060000 | segment * 4, 0]
                if second:
                    expected += [0xDB060000 | (255 - segment) * 4, second]
                expected += [0xDB0603FC, 0xE1234567]
                self.assertEqual(values, expected)
                self.assertEqual(result.r[2], OUTPUT + 8 + len(expected) * 4)
                self.assertEqual(result.memory[COUNT], 3)
                self.assertEqual([(a, s, v) for a, s, v in result.reads if a == COUNT],
                                 [(COUNT, 1, 3)] * 3)
        self.assertEqual(actual_visits, set(range(0x1510D8C0, 0x1510D8C0 + 40 * 4, 4)))
        self.assertEqual(retail_visits, set(range(0x1510D8C0, 0x1510D8C0 + 41 * 4, 4)))

    def test_unsigned_count_is_not_clamped_in_extended_mapped_fixture(self):
        entries = [(2, 0, 0, 0, 0)] * 255
        for count in range(256):
            result = self.compare(memory_case(count, entries, capacity=255), [OUTPUT, 1])
            self.assertFalse(result.stores)
            self.assertEqual(result.r[2], OUTPUT)
            self.assertEqual(result.reads, [(COUNT, 1, count)] +
                             [(QUEUE + index * 16, 4, 2) for index in range(count)])

    def test_big_endian_queue_output_aliases_preserve_fresh_load_and_store_order(self):
        entries = [(1, 0x12AB5678, 0xABCDEF01, 2, 0xE7), (1, 0, 0, 255, 128),
                   (0xDB060008, 0x89ABCDEF, 1, 3, 4)] + [(2, 0, 0, 0, 0)] * 5
        for count in range(1, 9):
            for offset in range(0, 112, 8):
                with self.subTest(count=count, offset=offset):
                    self.compare(memory_case(count, entries, capacity=16), [QUEUE + offset, 1])
        result = self.compare(memory_case(1, entries), [QUEUE, 1])
        self.assertEqual([v for _, _, v in result.stores],
                         [0xDB060008, 0x12AB5678, 0xDB06039C, 0xDB06039C])
        self.assertEqual([v for a, s, v in result.reads if a == QUEUE + 8 and s == 4],
                         [0xABCDEF01, 0xDB06039C])
        result = self.compare(memory_case(1, entries), [QUEUE + 8, 1])
        self.assertEqual([v for _, _, v in result.stores],
                         [0xDB060008, 0x12AB5678, 0xDB0602AC, 0xDB060008])

    def test_count_output_alias_refreshes_to_219_in_extended_fixture_only(self):
        entries = [(1, 0x12345678, 0, 2, 3)] + [(2, 0, 0, 0, 0)] * 254
        result = self.compare(memory_case(1, entries, capacity=255), [COUNT, 1])
        self.assertEqual(result.memory[COUNT], 0xDB)
        self.assertEqual(result.r[2], COUNT + 8)
        self.assertEqual([v for a, s, v in result.reads if a == COUNT], [1, 219])
        self.assertEqual([a for a, s, _ in result.reads if s == 4 and (a - QUEUE) % 16 == 0],
                         [QUEUE + index * 16 for index in range(219)])

    def test_native_color_all_rows_and_exhaustive_alpha_byte_pairs(self):
        self.run_host(r'''
int row,a,b,i; u32 primitive,environment; Gfx *end;
for(row=0;row<4;row++) {
    reset();
    primitive=((u32)(u8)(0x31+(row*3)*17)<<24)
        | ((u32)(u8)(0x31+(row*3+1)*17)<<16) | ((u32)(u8)(0x31+(row*3+2)*17)<<8);
    environment=((u32)(u8)(0x93+(row*3)*29)<<24)
        | ((u32)(u8)(0x93+(row*3+1)*29)<<16) | ((u32)(u8)(0x93+(row*3+2)*29)<<8);
    for(a=0;a<256;a++) for(b=0;b<256;b++) {
        end=func_1510CDB8(commands+1,(s32)(0xFEDCBA00u|(u32)a),(s32)(0x80000000u|(u32)b),row);
        if(end!=commands+3 || commands[1].words.w0!=0xFA00F200
           || commands[1].words.w1!=(primitive|(u32)a) || commands[2].words.w0!=0xFB000000
           || commands[2].words.w1!=(environment|(u32)b) || D_800D9ED0 || !fences()) return 1;
    }
    for(i=0;i<12;i++) if(palettes.bytes[8+i]!=(u8)(0x31+i*17)
        || palettes.bytes[24+i]!=(u8)(0x93+i*29)) return 2;
    for(i=0;i<128;i++) if(D_800D9ED8[i]!=0xA5) return 3;
    for(i=3;i<17;i++) if(commands[i].words.w0!=0xA5A5A5A5 || commands[i].words.w1!=0xA5A5A5A5) return 4;
}
''')
        type(self).native_color_cases = 4 * 256 * 256

    def test_native_actual_color_then_queue_writer_connection(self):
        self.run_host(r'''
int i; Gfx *colorEnd,*end;
reset();
func_1510D874(-1,0x12345678,0xFEDCBA98,2,3);
func_1510D874(-1,0,0,255,128);
colorEnd=func_1510CDB8(commands+1,-1,0x12345678,3);
end=func_1510D8C0(colorEnd,-1);
if(colorEnd!=commands+3 || end!=commands+6 || D_800D9ED0!=2 || !fences()) return 1;
if(commands[1].words.w0!=0xFA00F200 || commands[1].words.w1!=0xCADBECFF
   || commands[2].words.w0!=0xFB000000 || commands[2].words.w1!=0x98B5D278
   || commands[3].words.w0!=0xDB060008 || commands[3].words.w1!=0x12345678
   || commands[4].words.w0!=0xDB06000C || commands[4].words.w1!=0xFEDCBA98
   || commands[5].words.w0!=0xDB0603FC || commands[5].words.w1) return 2;
for(i=6;i<17;i++) if(commands[i].words.w0!=0xA5A5A5A5 || commands[i].words.w1!=0xA5A5A5A5) return 3;
for(i=0;i<12;i++) if(palettes.bytes[8+i]!=(u8)(0x31+i*17)
    || palettes.bytes[24+i]!=(u8)(0x93+i*29)) return 4;
if(func_1510D8C0(end,9)!=end || !fences()) return 5;
''')

    def test_big_endian_color_rows_alpha_edges_ordered_accesses_and_body_coverage(self):
        alphas = (-0x80000000, -257, -256, -1, 0, 1, 127, 128, 255,
                  256, 257, 0x7FFFFFFF, 0x12345678)
        visits, retail_visits = set(), set()
        cursor = OUTPUT + 8
        for row in range(4):
            for primitive_alpha in alphas:
                for environment_alpha in alphas:
                    memory = palette_case(memory_case(0, []))
                    result = self.compare(memory, [cursor, primitive_alpha, environment_alpha, row],
                                          'func_1510CDB8')
                    primitive = sum(memory[PRIMITIVE + row * 3 + channel] << (24 - channel * 8)
                                    for channel in range(3)) | (primitive_alpha & 255)
                    environment = sum(memory[ENVIRONMENT + row * 3 + channel] << (24 - channel * 8)
                                      for channel in range(3)) | (environment_alpha & 255)
                    expected = (0xFA00F200, primitive, 0xFB000000, environment)
                    self.assertEqual(result.stores, [(cursor + index * 4, 4, value)
                                                     for index, value in enumerate(expected)])
                    self.assertEqual(result.reads, [(base + row * 3 + channel, 1,
                                                    memory[base + row * 3 + channel])
                                                   for base in (PRIMITIVE, ENVIRONMENT)
                                                   for channel in (2, 0, 1)])
                    self.assertEqual(result.r[2], cursor + 16)
                    self.assertEqual({a: v for a, v in result.memory.items() if not cursor <= a < cursor + 16},
                                     {a: v for a, v in memory.items() if not cursor <= a < cursor + 16})
                    visits.update(result.visits)
                    retail_visits.update(result.retail_visits)
        expected_visits = set(range(0x1510CDB8, 0x1510CE60, 4))
        self.assertEqual(visits, expected_visits)
        self.assertEqual(retail_visits, expected_visits)

    def test_big_endian_color_palette_output_aliases_keep_header_before_rgb_reads(self):
        for row in range(4):
            for offset in (-8, 0, 8, 16, 24, 32, 40):
                for alphas in ((-1, 0x12345678), (256, -257), (0x80000000, 0x7FFFFFFF)):
                    with self.subTest(row=row, offset=offset, alphas=alphas):
                        result = self.compare(palette_case(memory_case(0, [])),
                                              [PRIMITIVE + offset, *alphas, row], 'func_1510CDB8')
                        self.assertEqual(result.r[2], PRIMITIVE + offset + 16)
        for offset, expected in ((0, (0xFA00F200, 0xFA00F2AA, 0xFB000000, 0x93B0CDBB)),
                                 (8, (0xFA00F200, 0x314253AA, 0xFB000000, 0xFB0000BB))):
            result = self.compare(palette_case(memory_case(0, [])),
                                  [PRIMITIVE + offset, 0xAA, 0xBB, 0], 'func_1510CDB8')
            self.assertEqual([value for _, _, value in result.stores], list(expected))

    def test_big_endian_color_writer_chain_normal_and_queue_output_alias(self):
        cursor = OUTPUT + 8
        for row in range(4):
            for count in (0, 1, 8):
                for key in (1, 0xFFFFFFFF):
                    entries = [(key, 0x81230000 + index, 0 if index % 2 else 0xFEDCBA98,
                                128 + index, 255 - index) for index in range(8)]
                    memory = palette_case(memory_case(count, entries))
                    color = self.compare(memory, [cursor, 17, 330, row], 'func_1510CDB8')
                    result = self.compare(color.memory, [color.r[2], key])
                    expected = []
                    for _, first, second, segment1, segment2 in entries[:count]:
                        expected += [0xDB060000 | segment1 * 4, first]
                        if second:
                            expected += [0xDB060000 | segment2 * 4, second]
                    self.assertEqual([value for _, _, value in result.stores], expected)
                    self.assertEqual(result.r[2], cursor + 16 + len(expected) * 4)
                    self.assertEqual(result.memory[COUNT], count)
                    self.assertEqual([result.memory[cursor + index] for index in range(16)],
                                     [color.memory[cursor + index] for index in range(16)])
                    self.assertEqual({a: v for a, v in result.memory.items() if not cursor <= a < result.r[2]},
                                     {a: v for a, v in memory.items() if not cursor <= a < result.r[2]})
        entries = [(1, 0x12345678, 0xFEDCBA98, 2, 3), (1, 0, 0, 4, 5)]
        color = self.compare(palette_case(memory_case(2, entries)),
                             [QUEUE, 0xAA, 0xBB, 0], 'func_1510CDB8')
        result = self.compare(color.memory, [color.r[2], 0xFA00F200])
        self.assertEqual([value for _, _, value in color.stores],
                         [0xFA00F200, 0x314253AA, 0xFB000000, 0x93B0CDBB])
        self.assertEqual(result.stores, [(QUEUE + offset, 4, value) for offset, value in
                         ((16, 0xDB06024C), (20, 0x314253AA), (24, 0xDB0602C0), (28, 0xFB000000))])
        self.assertEqual(result.r[2], QUEUE + 32)
        self.assertEqual(result.memory[COUNT], 2)

    def test_invalid_palette_indices_qualify_only_unmapped_read_prefix(self):
        name, cursor = 'func_1510CDB8', OUTPUT + 8
        for row in (-512, 4096, 0x80000000):
            memory = palette_case(memory_case(0, []))
            runs = [SegmentQueueOracle(words, 0x1510CDB8, memory, [cursor, -1, 256, row])
                    for words in (self.retail[name], self.production[name])]
            for result in runs:
                with self.assertRaises(KeyError):
                    result.run()
                self.assertEqual(result.stores, [(cursor, 4, 0xFA00F200)])
                self.assertFalse(result.reads)
                self.assertEqual([result.memory[cursor + index] for index in range(4, 16)], [0xA5] * 12)
            self.assertEqual(runs[0].memory, runs[1].memory)
            self.assertEqual(runs[0].stores, runs[1].stores)
            self.assertEqual(runs[0].reads, runs[1].reads)
            type(self).prefix_pairs += 1

    def test_fresh_ido_identity_retail_reference_exact_queue_helpers_and_no_guards(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or shutil.which('mips-linux-gnu-ld') is None:
            self.skipTest('IDO/MIPS tools unavailable')
        source, obj, elf, script = (self.path / ('segments' + suffix) for suffix in ('.c', '.o', '.elf', '.ld'))
        source.write_text(self.types + self.declarations + self.macros +
                          '\n'.join(self.bodies[name] for name in self.names) + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
            '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3',
            '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        script.write_text('SECTIONS { .text 0x1510D864 : SUBALIGN(4) { *(.text) } }\n')
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', self.names[0],
            '--defsym=D_800D9ED0=0x800D9ED0', '--defsym=D_800D9ED8=0x800D9ED8',
            '--defsym=D_800D9B68=0x800D9B68', '--defsym=D_800D9B78=0x800D9B78',
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        fresh, _, _ = match_progress.load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        measurements = {'func_1510D864': (4, 4, 0, 'e81b7668246b58e182518ea12697cbf47014a01b764ea1a2dc2f1e8ce2d55a31'),
                        'func_1510D874': (19, 19, 0, '5ca5af947408d6055c1fdf4ce2c517d915c75c052975430b17056b22969beffb'),
                        'func_1510D8C0': (40, 44, 38, 'f3a227545fc8d35dd017430e12f6fd1da0512c5746e400423358eee3a9566feb'),
                        'func_1510CDB8': (42, 42, 0, 'a1b386a82d28205880c5f04ac0e29057a9f2836f6b607d682b106490da0c2bc4')}
        assembly = (self.root / 'conker/asm/139FC0.s').read_text()
        for name, (body, size, different, digest) in measurements.items():
            words = fresh[name]
            length = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
            self.assertEqual(length, body)
            self.assertEqual(words[body:], [0] * (len(words) - body))
            slot = words[:body] + [0] * (size - body)
            self.assertEqual(self.production[name], slot)
            self.assertEqual(self.addresses[name], int(name[5:], 16))
            self.assertEqual(sum(a != b for a, b in zip(slot, self.retail[name])), different)
            self.assertEqual(hashlib.sha256(struct.pack('>' + str(size) + 'I', *slot)).hexdigest(), digest)
            block = assembly.split('glabel ' + name + '\n', 1)[1].split('endlabel ' + name, 1)[0]
            asm_words = [int(word, 16) for word in re.findall(r'/\*\s*\w+\s+\w+\s+(\w{8})\s*\*/', block)]
            self.assertEqual(asm_words + [0] * (size - len(asm_words)), self.retail[name])
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] in ('func_1510D8C0', 'func_1510CDB8')
                                 for row in csv.DictReader(source)))
        print('queued segment writer: body 40 / slot 44, frameless, 38 raw differences; helpers exact')
        print('palette color emitter: body/slot 42, frameless, raw-exact; no guards')


if __name__ == '__main__':
    unittest.main()
