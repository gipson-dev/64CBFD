"""Qualify the unchecked grid/channel pass and its closed register cycles."""

import itertools
import csv
import json
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_grid_channel_updater_candidates as screen
from tools.match_progress import load_elf_functions, load_segments
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly
from pad_generated_object import parse_object
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

ENTRY, ROOT, INDEX, BOUND = screen.ENTRY, 0x800DCE50, 0x800A5168, 0x80082FA0
WIDTH, HEIGHT, POINTER = 0x800BE620, 0x800BE624, 0x800BE9C4
REGISTER_MAP = {2: 4, 4: 3, 3: 2, 6: 7, 7: 10, 10: 8, 8: 6}


def normalize(words):
    result = []
    for word in words:
        op = word >> 26
        fields = (21, 16, 11) if op == 0 else (21,) if op == 1 else (21, 16)
        for shift in fields:
            register = word >> shift & 31
            word = word & ~(31 << shift) | REGISTER_MAP.get(register, register) << shift
        result.append(word)
    result[12:19] = result[13:19]+result[12:13]
    return result


def read(memory, address, size=4):
    return int.from_bytes(bytes(memory[address+i] for i in range(size)), 'big')


def signed(value):
    return value if value < 0x80000000 else value-0x100000000


def external(memory):
    return {a: v for a, v in memory.items() if not STACK-0x600 <= a < STACK+0x100}


def memory_case(bound, width, height, pattern, alias, empty):
    memory = {STACK+i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({ROOT+i: 0 for i in range(0x340)})
    nodes = [0x20000+i*0x200 for i in range(16)]
    if alias == 1:
        nodes[0] = BOUND-0x15C
    grid = nodes[0]+0x15C if alias == 2 else 0x50000
    for address, length in ((INDEX-16, 48), (BOUND-16, 36), (WIDTH-16, 40),
                            (POINTER-16, 36), (grid-16, 112)):
        memory.update({address+i: (i*13+7)&255 for i in range(length)})
    for number, node in enumerate(nodes):
        memory.update({node+i: (i*17+13)&255 for i in range(0x1C0)})
        put(memory, node+8, nodes[number+1] if number % 2 == 0 else 0)
        flags = (0, 0x2000, 0x2010, (0, 0x10, 0x2000, 0x2010)[number % 4])[pattern]
        put(memory, node+0x58, flags)
        points = ((0, 0), (width-1, height-1), (-1, 0), (width, 0),
                  (0, -1), (0, height), (width-1, 0), (0, height-1))
        for channel in range(4):
            x, y = points[(number+channel) % 8]
            put(memory, node+0x134+channel*4, x&0xFFFFFFFF)
            put(memory, node+0x144+channel*4, y&0xFFFFFFFF)
    for i in range(width*height):
        put(memory, grid+i*2, (i*71+0x8000)&65535, 2)
    for bucket, column in enumerate((0, 28, 86, 103)):
        put(memory, INDEX+bucket*4, column)
        for row in range(2):
            put(memory, ROOT+row*0x1A0+column*4, 0 if empty else nodes[(row*4+bucket)*2])
    for address, value in ((BOUND, bound&0xFFFFFFFF), (WIDTH, width),
                            (HEIGHT, height), (POINTER, grid)):
        put(memory, address, value)
    return memory


def reference(memory):
    memory = dict(memory)
    for row in range(2):
        for bucket in range(4):
            node = read(memory, ROOT+row*0x1A0+read(memory, INDEX+bucket*4)*4)
            seen = set()
            while node:
                assert node not in seen
                seen.add(node)
                flags = read(memory, node+0x58)
                if flags&0x2000:
                    for offset in (0x162, 0x160, 0x15E, 0x15C):
                        put(memory, node+offset, 0, 2)
                    if flags&0x10:
                        channel = 0
                        while channel <= signed(read(memory, BOUND)):
                            x = signed(read(memory, node+0x134+channel*4))
                            width = signed(read(memory, WIDTH)) if x >= 0 else 0
                            value = 0x7FFF
                            if 0 <= x < width:
                                y = signed(read(memory, node+0x144+channel*4))
                                if 0 <= y < signed(read(memory, HEIGHT)):
                                    value = read(memory, read(memory, POINTER)+(y*width+x)*2, 2)
                            put(memory, node+0x15C+channel*2, value, 2)
                            channel = (channel+1)&255
                            assert channel <= 4
                node = read(memory, node+8)
    return external(memory)


class GridOracle(TriangleOracle):
    def get(self, address, size):
        assert all(address+i in self.memory for i in range(size)), ('unmapped read', address, size)
        return super().get(address, size)

    def put(self, address, value, size):
        if self.recording:
            assert all(address+i in self.memory for i in range(size)), ('unmapped write', address, size)
        super().put(address, value, size)


class GameGridChannelUpdaterMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root/'ido/ido5.3_recomp/cc').exists() or any(shutil.which(name) is None
                for name in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root/'conker/build/game-grid-channel-updater-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.normalized = normalize(cls.raw)
        cls.retail = list(struct.unpack_from('>96I', (cls.root/'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = native_fixture()

    def test_closed_register_cycles_and_independent_address_schedule(self):
        self.assertEqual(self.record['body_words'], 96)
        self.assertEqual(self.record['frame'], 24)
        self.assertEqual(self.record['differences'], 43)
        self.assertEqual(set(REGISTER_MAP), set(REGISTER_MAP.values()))
        self.assertEqual(self.normalized, self.retail)
        # No branch, instruction insertion, opcode or arithmetic-constant rewrite.
        for old, new in zip(self.raw, [*self.normalized[:12], self.normalized[18],
                                      *self.normalized[12:18], *self.normalized[19:]]):
            self.assertEqual(old >> 26, new >> 26)
            if old >> 26:
                self.assertEqual(old&65535, new&65535)
            else:
                self.assertEqual(old&2047, new&2047)

    def test_guest_storage_ordered_accesses_saved_state_and_normalized_return(self):
        coverage = [set(), set(), set()]
        cases = 0
        for bound, width, height, pattern, alias, empty, phase in itertools.product(
                (-1, 0, 1, 3), (1, 3, 7), (1, 2, 5), range(4), range(3), (False, True), (0, 8)):
            memory = memory_case(bound, width, height, pattern, alias, empty)
            wanted = reference(memory)
            models = [GridOracle(body, memory, entry=ENTRY, arguments=(), phase=phase).run()
                      for body in (self.raw, self.normalized, self.retail)]
            traces = []
            for i, model in enumerate(models):
                self.assertEqual(external(model.memory), wanted, (cases, i))
                self.assertFalse(model.calls)
                coverage[i].update(model.visits)
                traces.append([event for event in model.events if not STACK-0x600 <= event[1] < STACK+0x100])
            self.assertEqual(traces[0], traces[2], cases)
            self.assertEqual(traces[1], traces[2], cases)
            self.assertEqual(models[0].r[2], 0x800DD190)
            self.assertEqual(models[1].r[2], 4)
            self.assertEqual(models[2].r[2], 4)
            cases += 1
        self.assertEqual(cases, 1728)
        self.assertEqual([len(words) for words in coverage], [95, 95, 95])
        self.assertNotIn(ENTRY+0x120, coverage[2])

    def test_real_padder_relocation_schedule_and_complete_linked_slot(self):
        text, functions, relocations = parse_object(self.output/'selected.o')
        start = functions['func_151412BC']['value']
        fields = ('filename', 'function', 'offset', 'expected', 'replacement', 'expected_relocations',
                  'replacement_relocations', 'note', 'insert_after', 'insert_after_relocations', 'omit')
        moved = {12: 18, **{i: i-1 for i in range(13, 19)}}
        target_relocations = {moved.get((a-start)//4, (a-start)//4)*4: items
                              for a, items in relocations.items()}
        target_bytes = normalize(list(struct.unpack_from('>96I', text, start)))
        self.guard_rows = []
        with (self.output/'guards.csv').open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            for i, (old, new) in enumerate(zip(struct.unpack_from('>96I', text, start), target_bytes)):
                if old == new:
                    continue
                encoding = lambda items: ';'.join('%s:%s'%item for item in items) or '-'
                row = dict(zip(fields, ('game_16DC80', 'func_151412BC', '0x%X'%(i*4),
                    '0x%08X'%old, '0x%08X'%new, encoding(relocations.get(start+i*4, [])),
                    encoding(target_relocations.get(i*4, [])),
                    'Normalize grid updater closed register cycles and independent address setup', '', '', 'false')))
                self.guard_rows.append(row)
                writer.writerow(row)
        self.assertEqual(len(self.guard_rows), 43)
        layout = self.output/'layout.csv'
        layout.write_text('version,section,filename,function,address,end\n'
                          'us,game,game_16DC80,func_151412BC,0x151412BC,0x1514143C\n')
        assembly = emit_padded_assembly(self.output/'selected.o', layout, 'game_16DC80',
                                       word_patches_path=self.output/'guards.csv')
        (self.output/'padded.s').write_text(assembly)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(self.output/'padded.o'),
                        str(self.output/'padded.s')], check=True, capture_output=True)
        _, padded_functions, padded_relocations = parse_object(self.output/'padded.o')
        self.assertEqual(padded_functions['func_151412BC']['size'], 384)
        self.assertEqual(padded_relocations, target_relocations)
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output/'grid-channel.ld'),
                        '-e', 'func_151412BC', *['--defsym=%s=0x%X'%item for item in screen.SYMBOLS.items()],
                        '-o', str(self.output/'padded.elf'), str(self.output/'padded.o')], check=True, capture_output=True)
        linked = load_elf_functions(str(self.output/'padded.elf'), 'mips-linux-gnu-objdump')[0]['func_151412BC']
        self.assertEqual(linked, self.retail)

    def test_signed_bounds_and_live_byte_wrap_without_native_invalid_access(self):
        for bound, phase in itertools.product((-0x80000000, -1, 0, 127, 128, 254), (0, 8)):
            memory = memory_case(bound, 1, 1, 2, 0, True)
            node = 0x20000
            memory.update({node+i: 0xFF for i in range(0x580)})
            put(memory, node+8, 0)
            put(memory, node+0x58, 0x2010)
            put(memory, ROOT, node)
            put(memory, WIDTH, 0)
            models = [GridOracle(body, memory, entry=ENTRY, arguments=(), phase=phase).run()
                      for body in (self.raw, self.normalized, self.retail)]
            for model in models:
                stores = [e for e in model.events if e[0] == 'W' and node+0x15C <= e[1] < node+0x35C]
                self.assertEqual(len(stores), 4+max(0, bound+1))
                self.assertEqual(external(model.memory), external(models[2].memory))
        memory = memory_case(255, 1, 1, 2, 0, True)
        memory.update({0x20000+i: 0xFF for i in range(0x580)})
        put(memory, 0x20008, 0)
        put(memory, 0x20058, 0x2010)
        put(memory, ROOT, 0x20000)
        put(memory, WIDTH, 0)
        for body in (self.raw, self.normalized, self.retail):
            model = GridOracle(body, memory, entry=ENTRY, arguments=())
            with self.assertRaisesRegex(AssertionError, 'instruction budget exhausted'):
                model.run()
            first = [e for e in model.events if e[0] == 'W' and e[1] == 0x2015C]
            self.assertGreater(len(first), 2)
            self.assertFalse(any(e[0] == 'R' and e[1] == 0x20008 for e in model.events))

    def test_native_actual_body_complete_storage_aliases_and_bounds(self):
        self.run_host(r'''
int b,w,h,p,a,e,n,i;
static s32 bounds[]={-1,0,1,3};
static s32 widths[]={1,3,7},heights[]={1,2,5};
if(sizeof(void *)!=4) return 1;
for(b=0;b<4;b++) for(w=0;w<3;w++) for(h=0;h<3;h++)
for(p=0;p<4;p++) for(a=0;a<3;a++) for(e=0;e<2;e++) {
    prepare(bounds[b],widths[w],heights[h],p,a,e);
    expected_pass(a);
    func_151412BC();
    for(n=0;n<16;n++) for(i=0;i<0x1C0;i++) if(nodes[n].bytes[i]!=wanted[n].bytes[i]) return 2;
    for(i=0;i<56;i++) if(grid[i]!=wantedGrid[i]) return 3;
    if(*boundPointer!=expectedBound || D_800BE620!=widths[w] || D_800BE624!=heights[h]) return 4;
    for(i=0;i<0x340;i++) if(rows.bytes[i]!=rowsBefore[i]) return 5;
}
''')

    def test_semantic_and_access_order_negative_controls(self):
        sources = {
            'wrong-enable': screen.SELECTED.replace('flags & 0x2000', 'flags & 0x1000'),
            'wrong-channel-enable': screen.SELECTED.replace('flags & 0x10', 'flags & 0x20'),
            'wrong-clear': screen.SELECTED.replace('node + 0x162', 'node + 0x164'),
            'wrong-payload': screen.SELECTED.replace('node + 0x110', 'node + 0x108'),
            'wrong-sentinel': screen.SELECTED.replace('= 0x7FFF', '= 0xFFFF'),
            'wrong-grid': screen.SELECTED.replace('y * D_800BE620 + x]', 'y * D_800BE620 + x + 1]'),
            'missing-clear': screen.SELECTED.replace('*(s16 *)(node + 0x160) = 0;', ''),
            'clear-order': screen.SELECTED.replace('node + 0x162', 'node + 0xFFFF').replace(
                'node + 0x15C', 'node + 0x162').replace('node + 0xFFFF', 'node + 0x15C'),
            'captured-bound': screen.SELECTED.replace('    u32 flags;', '    u32 flags;\n    s32 bound;').replace(
                '    row =', '    bound = D_80082FA0;\n    row =').replace('channel <= D_80082FA0', 'channel <= bound'),
            'eager-y': screen.SELECTED.replace('                                    if (x',
                '                                    y = *(s32 *)(payload + 0x34 + channel * 4);\n                                    if (x').replace(
                    '(y = *(s32 *)(payload + 0x34 + channel * 4)) >= 0', 'y >= 0')}
        for name, source in sources.items():
            _, words = screen.compile_candidate(self.root, self.output, name, source)
            distinguished = False
            for bound, pattern, alias in itertools.product((0, 3), (1, 2, 3), range(3)):
                memory = memory_case(bound, 3, 2, pattern, alias, False)
                retail = GridOracle(self.retail, memory, entry=ENTRY, arguments=()).run()
                candidate = GridOracle(words, memory, entry=ENTRY, arguments=())
                try:
                    candidate.run()
                except AssertionError as error:
                    self.assertTrue('unmapped' in str(error), (name, error))
                    distinguished = True
                    break
                trace = lambda model: [event for event in model.events if not STACK-0x600 <= event[1] < STACK+0x100]
                if external(candidate.memory) != external(retail.memory) or trace(candidate) != trace(retail):
                    distinguished = True
                    break
            self.assertTrue(distinguished, name)

    def test_owner_local_global_interpretation_without_header_changes(self):
        record, words = screen.compile_candidate(self.root, self.output, 'owner-control',
            screen.OWNER_BODY, declarations='#include "variables.h"\n')
        self.assertEqual(words, self.raw)
        self.assertEqual((record['body_words'], record['frame'], record['differences']), (96, 24, 43))

    def test_persistent_declaration_and_loop_compiler_controls(self):
        records = []
        for name, body in itertools.chain(screen.candidates(), screen.loop_candidates()):
            for profile in screen.PROFILES:
                record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                records.append(record)
        self.assertEqual(len(records), 144)
        self.assertTrue(all(record['diagnostics'] == '' for record in records))
        selected = [record for record in records if record['name'] == 'byte-payload-s32-bottom-assignment-o2g3']
        self.assertEqual([(record['body_words'], record['frame'], record['differences']) for record in selected],
                         [(96, 24, 43)])
        (self.output/'measurements.json').write_text(json.dumps(records, indent=2)+'\n')

    def test_production_complete_slot_source_and_guard_metadata(self):
        owner = (self.root/'conker/src/game_16DC80.c').read_text()
        body = re.search(r'void func_151412BC\(void\) \{\n.*?\n\}', owner, re.S).group(0)
        self.assertEqual(body.split(), screen.OWNER_BODY.split())
        self.assertIn('void func_151412BC(void);', owner)
        self.assertNotIn('s32 func_151412BC', owner)
        production = load_elf_functions(str(self.root/'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        self.assertEqual(production['func_151412BC'], self.retail)
        # Scan pristine slots: the caller itself is still a C placeholder in the ELF.
        jal = 0x0C000000 | ((ENTRY >> 2)&0x3FFFFFF)
        rom = (self.root/'conker/conker.us.bin').read_bytes()
        segments = load_segments('us', str(self.root/'conker/progress.csv'))
        callers, retail_slots = [], {}
        with (self.root/'conker/retail_layout.us.txt').open(newline='') as stream:
            for row in csv.DictReader(stream):
                start, end = int(row['address'], 0), int(row['end'], 0)
                vram, offset = segments[row['section']]
                words = list(struct.unpack_from('>%dI'%((end-start)//4), rom, start-vram+offset))
                retail_slots[row['function']] = words
                callers.extend((row['function'], i) for i, word in enumerate(words) if word == jal)
        self.assertEqual(callers, [('func_1501878C', 37)])
        self.assertEqual(retail_slots['func_1501878C'][39], 0x3C02800C)
        text, functions, relocations = parse_object(self.output/'selected.o')
        start = functions['func_151412BC']['value']
        raw = list(struct.unpack_from('>96I', text, start))
        normalized = normalize(raw)
        movement = {12: 18, **{i: i-1 for i in range(13, 19)}}
        new_relocations = {movement.get((a-start)//4, (a-start)//4)*4: items
                           for a, items in relocations.items()}
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        guards = [row for row in rows if row['function'] == 'func_151412BC']
        self.assertEqual((len(rows), len(guards)), (10809, 43))
        self.assertEqual([int(row['offset'], 0) for row in guards],
                         [i*4 for i, pair in enumerate(zip(raw, normalized)) if pair[0] != pair[1]])
        encoding = lambda items: ';'.join('%s:%s'%item for item in items) or '-'
        for row in guards:
            offset = int(row['offset'], 0)
            self.assertEqual(row['filename'], 'game_16DC80')
            self.assertEqual(int(row['expected'], 0), raw[offset//4])
            self.assertEqual(int(row['replacement'], 0), normalized[offset//4])
            self.assertEqual(row['expected_relocations'], encoding(relocations.get(start+offset, [])))
            self.assertEqual(row['replacement_relocations'], encoding(new_relocations.get(offset, [])))
            self.assertEqual((row['insert_after'], row['insert_after_relocations'], row['omit']), ('', '', 'false'))


def native_fixture():
    return '''typedef unsigned char u8; typedef short s16; typedef unsigned short u16;
typedef int s32; typedef unsigned int u32;
#define NULL ((void *)0)
''' + r'''
static union {u32 align;u8 bytes[0x344];} rows;
static union {u32 align;u8 bytes[0x1C0];} nodes[16],wanted[16];
static u8 rowsBefore[0x340];
static u16 grid[56],wantedGrid[56];
static s32 boundValue,*boundPointer,expectedBound;
s32 D_800A5168[4],D_800BE620,D_800BE624;
u16 *D_800BE9C4;
#define D_800DCE50 rows.bytes
#define D_800DD190 (*(rows.bytes+0x340))
#define D_80082FA0 (*boundPointer)
static u32 load(u8 *p) {return *(u32 *)p;}
static void store(u8 *p,u32 v) {*(u32 *)p=v;}
static s32 live_expected_bound(int alias) {
    return alias==1?(s32)load(wanted[0].bytes+0x15C):expectedBound;
}
static void expected_pass(int alias) {
    int row,bucket,n,c;
    for(row=0;row<2;row++) for(bucket=0;bucket<4;bucket++) {
        if(!load(rows.bytes+row*0x1A0+D_800A5168[bucket]*4)) continue;
        for(n=(row*4+bucket)*2;n<(row*4+bucket)*2+2;n++) {
            u8 *node=wanted[n].bytes;
            u32 flags=load(node+0x58);
            if(!(flags&0x2000)) continue;
            for(c=3;c>=0;c--) *(u16 *)(node+0x15C+c*2)=0;
            if(!(flags&0x10)) continue;
            for(c=0;c<=live_expected_bound(alias);c++) {
                s32 x=(s32)load(node+0x134+c*4),y;
                u16 value=0x7FFF;
                if(x>=0 && x<D_800BE620) {
                    y=(s32)load(node+0x144+c*4);
                    if(y>=0 && y<D_800BE624) {
                        u16 *g=alias==2?(u16 *)(wanted[0].bytes+0x15C):wantedGrid;
                        value=g[y*D_800BE620+x];
                    }
                }
                *(u16 *)(node+0x15C+c*2)=value;
            }
        }
    }
    expectedBound=live_expected_bound(alias);
}
static void prepare(s32 bound,s32 width,s32 height,int pattern,int alias,int empty) {
    static int columns[]={0,28,86,103};
    int n,c,i,row;
    for(i=0;i<0x344;i++) rows.bytes[i]=0;
    boundValue=bound;expectedBound=bound;D_800BE620=width;D_800BE624=height;
    boundPointer=alias==1?(s32 *)(nodes[0].bytes+0x15C):&boundValue;
    D_800BE9C4=alias==2?(u16 *)(nodes[0].bytes+0x15C):grid;
    for(n=0;n<16;n++) {
        u8 *node=nodes[n].bytes;
        static u32 flags[]={0,0x2000,0x2010,0};
        static u32 mixed[]={0,0x10,0x2000,0x2010};
        for(i=0;i<0x1C0;i++) node[i]=(u8)(i*17+13);
        store(node+8,n%2==0?(u32)nodes[n+1].bytes:0);
        store(node+0x58,pattern==3?mixed[n%4]:flags[pattern]);
        for(c=0;c<4;c++) {
            s32 xs[]={0,width-1,-1,width,0,0,width-1,0};
            s32 ys[]={0,height-1,0,0,-1,height,0,height-1};
            store(node+0x134+c*4,(u32)xs[(n+c)%8]);
            store(node+0x144+c*4,(u32)ys[(n+c)%8]);
        }
    }
    for(i=0;i<56;i++) grid[i]=wantedGrid[i]=(u16)(i*71+0x8000);
    if(alias==2) for(i=0;i<width*height;i++) D_800BE9C4[i]=grid[i];
    *boundPointer=bound;
    for(c=0;c<4;c++) {
        D_800A5168[c]=columns[c];
        for(row=0;row<2;row++) store(rows.bytes+row*0x1A0+columns[c]*4,
            empty?0:(u32)nodes[(row*4+c)*2].bytes);
    }
    for(n=0;n<16;n++) for(i=0;i<0x1C0;i++) wanted[n].bytes[i]=nodes[n].bytes[i];
    for(i=0;i<0x340;i++) rowsBefore[i]=rows.bytes[i];
}
''' + screen.OWNER_BODY+'\n'


if __name__ == '__main__':
    unittest.main()
