"""Actual SDK helper and bounded command traces, not complete renderer acceptance."""

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
from tools.tests import test_game_queued_segment_writer as queue
from tools.tests import test_game_random_curve_record as curve
from tools.tests.test_game_dual_matrix_emitter import sdk_macro


ENTRY = 0x1510B7B4
BASE = 0x800BE628
PAGE = 0x800BE9C0
TABLE = 0x800DC2A0
RECORDS = 0x80050000
IDENTITY = 0x80089470


def case(slot=0, page=0, normalize=0x1234, output=queue.OUTPUT):
    memory = {address: 0xA5 for address in range(output - 8, output + 104)}
    memory.update({queue.STACK + offset: 0xA5 for offset in range(32)})
    memory.update({RECORDS + offset: 0xA5 for offset in range(4 * 0x180)})
    for address, value, size in ((BASE, RECORDS, 4), (PAGE, page, 1),
                                 (TABLE, 0x80060000, 4), (TABLE + 4, 0x80070000, 4),
                                 (RECORDS + (slot & 3) * 0x180 + 0xB8, normalize, 2)):
        for index, byte in enumerate(value.to_bytes(size, 'big')):
            memory[address + index] = byte
    if output == PAGE - 76:
        for index, byte in enumerate((0x80080000).to_bytes(4, 'big')):
            memory[TABLE + 128 * 4 + index] = byte
    return memory


class ViewportOracle(queue.SegmentQueueOracle):
    def __init__(self, words, entry, memory, arguments):
        self.output = arguments[0]
        super().__init__(words, entry, memory, arguments)

    def get(self, address, size):
        assert all(address + i in self.memory for i in range(size)), ('unmapped read', address, size)
        return super().get(address, size)

    def put(self, address, value, size):
        if self.recording:
            assert size == 4 and self.output <= address < self.output + 96, (
                'display-list output fence', address, size)
        super().put(address, value, size)


class GameViewportCommandHelperTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host
    test_complete_init_debugger_and_game_data_remain_exact = (
        queue.GameQueuedSegmentWriterTests.test_complete_init_debugger_and_game_data_remain_exact)

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        for tool in ('cc', 'mips-linux-gnu-ld', 'mips-linux-gnu-objcopy', 'mips-linux-gnu-objdump'):
            if shutil.which(tool) is None:
                raise unittest.SkipTest(tool + ' is unavailable')
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file():
            raise unittest.SkipTest('IDO is unavailable')
        source = (cls.root / 'conker/src/game/generated_138520.c').read_text()
        cls.body = re.search(r'Gfx \*func_1510B7B4\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        color_source = (cls.root / 'conker/src/game/generated_139FC0.c').read_text()
        color = re.search(r'Gfx \*func_1510CDB8\([^;{}]+\) \{\n.*?\n\}', color_source, re.S).group(0)
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
                     'G_SETPRIMCOLOR', 'G_SETENVCOLOR', 'gDPSetPrimColor', 'gDPSetEnvColor'):
            macros += sdk_macro(gbi, name)
        cls.types = ('typedef unsigned char u8; typedef unsigned short u16; '
                     'typedef unsigned int u32; typedef int s32;\n'
                     'typedef struct { struct { u32 w0,w1; } words; } Gfx;\n'
                     'typedef struct { u8 bytes[64]; } Mtx;\n')
        cls.fixture = cls.types + macros + r'''
static u8 records[4*0x180], matrices[2][4*0x40];
u8 D_80089470[64], D_800BE9C0, *D_800BE628=records;
u8 *D_800DC2A0[2]={matrices[0],matrices[1]};
u8 D_800D9B68[4][3], D_800D9B78[4][3];
static Gfx commands[18];
static const u32 words0[12]={0xE7000000,0xF9000000,0xDA380003,0xDB0E0000,
    0xDB040004,0xDB04000C,0xDB040014,0xDB04001C,0xD9EFFFFF,
    0xDA380007,0xDA380005,0xEF082C3F};
static void reset(int slot,int page,u16 normalize) {
    int i;
    D_800BE9C0=(u8)page;
    *(u16 *)(records+slot*0x180+0xB8)=normalize;
    for(i=0;i<18;i++) commands[i].words.w0=commands[i].words.w1=0xA5A5A5A5;
}
static int check(int slot,int page,u16 normalize,Gfx *end) {
    u32 words1[12]={0,1,(u32)D_80089470,0,3,3,0xFFFD,0xFFFD,0,0,0,0x552230};
    int i;
    words1[3]=normalize;
    words1[9]=(u32)records+slot*0x180+page*0x40+0x100;
    words1[10]=(u32)matrices[page]+slot*0x40;
    if(end!=commands+13) return 0;
    for(i=0;i<12;i++) if(commands[i+1].words.w0!=words0[i]
        ||commands[i+1].words.w1!=words1[i]) return 0;
    for(i=0;i<18;i++) if((i==0||i>=13)&&(commands[i].words.w0!=0xA5A5A5A5
        ||commands[i].words.w1!=0xA5A5A5A5)) return 0;
    return *(u16 *)(records+slot*0x180+0xB8)==normalize && D_800BE9C0==page;
}
''' + cls.body + '\n' + color + '\n'
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.production, _, cls.addresses = match_progress.load_elf_functions(
            str(cls.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        config = yaml.safe_load((cls.root / 'conker/conker.us.yaml').read_text())
        assert hashlib.sha1(rom).hexdigest() == config['sha1']
        cls.retail = list(struct.unpack_from('>105I', rom, 0x138C64))
        cls.pairs, cls.prefixes, cls.native = 0, 0, 0
        cls.coverage, cls.retail_coverage = set(), set()
        cls.completed_checks = set()

    def tearDown(self):
        if self._outcome.success:
            type(self).completed_checks.add(self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        (cls.root / 'conker/build/game-viewport-command-helper-qualification.json').write_text(
            json.dumps({'completed_pairs': cls.pairs, 'invalid_prefix_pairs': cls.prefixes,
                        'native_cases': cls.native,
                        'complete_module_corpus': (cls.pairs == 97 and cls.prefixes == 3
                                                   and cls.native == 65600
                                                   and cls.completed_checks == set(
                                                       unittest.defaultTestLoader.getTestCaseNames(cls))),
                        'completed_checks': sorted(cls.completed_checks),
                        'qualification': 'bounded low-word model; no complete renderer/pixel acceptance'},
                       indent=2) + '\n')

    def compare(self, memory, output, slot):
        expected = ViewportOracle(self.retail, ENTRY, memory, (output, slot)).run()
        actual = ViewportOracle(self.production['func_1510B7B4'], ENTRY,
                                memory, (output, slot)).run()
        self.assertEqual(actual.memory, expected.memory)
        self.assertEqual(actual.reads, expected.reads)
        self.assertEqual(actual.stores, expected.stores)
        self.assertEqual(actual.r[2], (output + 96) & 0xFFFFFFFF)
        self.assertEqual(actual.r[2], expected.r[2])
        self.assertEqual([(address, size) for address, size, _ in actual.stores],
                         [(address, size) for address, size, _ in expected.stores])
        type(self).coverage.update(actual.visits)
        type(self).retail_coverage.update(expected.visits)
        type(self).pairs += 1
        return actual

    def test_native_every_unsigned_normalization_value(self):
        self.run_host(r'''
u32 normalize;
for(normalize=0;normalize<65536;normalize++) {
    reset(0,0,(u16)normalize);
    if(!check(0,0,(u16)normalize,func_1510B7B4(commands+1,0))) return 1;
}
''')
        type(self).native += 65536

    def test_native_slots_pages_packets_and_cursor(self):
        self.run_host(r'''
static const u16 values[]={0,1,0x7FFF,0x8000,0xFFFF,0x1234,0xABCD};
int slot,page,i;
for(slot=0;slot<4;slot++) for(page=0;page<2;page++) for(i=0;i<7;i++) {
    reset(slot,page,values[i]);
    if(!check(slot,page,values[i],func_1510B7B4(commands+1,slot))) return 1;
}
''')
        type(self).native += 56

    def test_native_actual_helper_and_color_cursor_connection(self):
        self.run_host(r'''
int slot,page; Gfx *end;
for(slot=0;slot<4;slot++) for(page=0;page<2;page++) {
    reset(slot,page,0x8001);
    D_800D9B68[slot][0]=1;D_800D9B68[slot][1]=2;D_800D9B68[slot][2]=3;
    D_800D9B78[slot][0]=4;D_800D9B78[slot][1]=5;D_800D9B78[slot][2]=6;
    end=func_1510B7B4(commands+1,slot);
    if(!check(slot,page,0x8001,end)) return 1;
    end=func_1510CDB8(end,255,255,slot);
    if(end!=commands+15 || commands[13].words.w0!=0xFA00F200
        ||commands[13].words.w1!=0x010203FF ||commands[14].words.w0!=0xFB000000
        ||commands[14].words.w1!=0x040506FF) return 2;
    if(commands[15].words.w0!=0xA5A5A5A5 ||commands[0].words.w1!=0xA5A5A5A5) return 3;
}
''')
        type(self).native += 8

    def test_paired_all_slots_pages_and_normalization_boundaries(self):
        for slot in range(4):
            for page in range(2):
                for normalize in (0, 1, 0x7FFF, 0x8000, 0xFFFF, 0x1234, 0xABCD):
                    with self.subTest(slot=slot, page=page, normalize=normalize):
                        self.compare(case(slot, page, normalize), queue.OUTPUT, slot)

    def test_paired_low_word_wrapping_indices_in_model_only(self):
        for slot in (0x20000000, 0x40000000, 0x80000000, 0xE0000000):
            for page in range(2):
                with self.subTest(slot=slot, page=page):
                    self.compare(case(0, page, 0x8001), queue.OUTPUT, slot)

    def test_paired_selector_and_matrix_table_output_aliases(self):
        for output in (PAGE - 12, TABLE - 84, PAGE - 76, BASE - 68):
            for slot in range(4):
                for page in range(2):
                    with self.subTest(output=output, slot=slot, page=page):
                        self.compare(case(slot, page, 0x8001, output), output, slot)

    def test_cached_page_control_is_rejected_by_late_alias(self):
        class CachedPageOracle(ViewportOracle):
            saved_page = None

            def get(self, address, size):
                value = super().get(address, size)
                if address == PAGE:
                    if self.saved_page is None:
                        self.saved_page = value
                    return self.saved_page
                return value

        output = PAGE - 76
        memory = case(0, 0, 0x8001, output)
        words = self.production['func_1510B7B4']
        expected = ViewportOracle(words, ENTRY, memory, (output, 0)).run()
        mutant = CachedPageOracle(words, ENTRY, memory, (output, 0)).run()
        self.assertEqual([value for address, _, value in expected.reads if address == PAGE], [0, 128])
        self.assertNotEqual(mutant.memory, expected.memory)
        self.assertNotEqual(mutant.stores, expected.stores)

    def test_output_fence_rejects_unowned_and_wrong_width_stores(self):
        fixture = ViewportOracle(self.retail, ENTRY, case(), (queue.OUTPUT, 0))
        for address, size in ((queue.OUTPUT - 4, 4), (queue.OUTPUT + 96, 4),
                              (queue.OUTPUT, 2), (BASE, 4)):
            with self.assertRaisesRegex(AssertionError, 'output fence'):
                fixture.put(address, 0, size)

    def test_fresh_source_compile_reproduces_production_body(self):
        project = self.root / 'conker'
        source, obj, elf, binary = [self.path / ('independent' + suffix)
                                    for suffix in ('.c', '.o', '.elf', '.bin')]
        source.write_text('#include <ultra64.h>\nextern u8 *D_800BE628;\n'
                          'extern u8 D_80089470[], D_800BE9C0;\n'
                          'extern u8 *D_800DC2A0[];\n' + self.body + '\n')
        result = subprocess.run([str(self.root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
            '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
            '-D_LANGUAGE_C', '-D_FINALROM', '-DF3DEX_GBI_2', '-D_MIPS_SZLONG=32',
            '-I', 'include', '-I', 'include/2.0L', '-I', 'include/2.0L/PR', '-I', 'include/libc',
            '-O2', '-g3', '-mips2', '-o32', '-o', str(obj), str(source)],
            cwd=project, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        script = self.path / 'independent.ld'
        script.write_text('SECTIONS { .text 0x1510B7B4 : SUBALIGN(4) { *(.text) } }\n')
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
            '-e', 'func_1510B7B4', '--defsym=D_800BE628=0x800BE628',
            '--defsym=D_800BE9C0=0x800BE9C0', '--defsym=D_800DC2A0=0x800DC2A0',
            '--defsym=D_80089470=0x80089470', '-o', str(elf), str(obj)], check=True)
        subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '--only-section=.text',
                        str(elf), str(binary)], check=True)
        emitted, _, addresses = match_progress.load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        actual = emitted['func_1510B7B4']
        production = self.production['func_1510B7B4']
        end = max(index for index, word in enumerate(actual) if word == 0x03E00008) + 2
        self.assertEqual(addresses['func_1510B7B4'], ENTRY)
        self.assertEqual(actual[:end], production[:end])
        self.assertFalse(any(actual[end:]))
        self.assertFalse(any(production[end:]))

    def test_invalid_slot_and_page_prefixes_do_not_invent_guards(self):
        for slot, page in ((-1, 0), (4, 0), (0, 2)):
            memory = case(0, page)
            expected = ViewportOracle(self.retail, ENTRY, memory, (queue.OUTPUT, slot))
            actual = ViewportOracle(self.production['func_1510B7B4'], ENTRY,
                                    memory, (queue.OUTPUT, slot))
            with self.subTest(slot=slot, page=page):
                for fixture in (expected, actual):
                    with self.assertRaisesRegex(AssertionError, 'unmapped'):
                        fixture.run()
                self.assertEqual(actual.memory, expected.memory)
                self.assertEqual(actual.stores, expected.stores)
                self.assertEqual(actual.reads, expected.reads)
                type(self).prefixes += 1

    def test_source_slot_and_reachable_instruction_contract(self):
        words = self.production['func_1510B7B4']
        self.assertEqual(len(words), 105)
        self.assertEqual(self.addresses['func_1510B7B4'], ENTRY)
        self.assertFalse(any(word >> 16 == 0x27BD for word in words))
        self.assertFalse(any(word >> 26 == 3 for word in words))
        self.assertIn('gSPClipRatio(arg0++, FRUSTRATIO_3)', self.body)
        self.assertIn('gSPClearGeometryMode(arg0++, G_LOD)', self.body)
        patches = (self.root / 'conker/retail_word_patches.us.csv').read_text()
        self.assertNotIn(',func_1510B7B4,', patches)
        self.compare(case(), queue.OUTPUT, 0)
        end = max(index for index, word in enumerate(words) if word == 0x03E00008) + 2
        self.assertEqual(end, 103)
        self.assertEqual(sum(a != b for a, b in zip(words, self.retail)), 104)
        self.assertEqual(hashlib.sha256(struct.pack('>105I', *words)).hexdigest(),
                         '3f8226f75dae50f3e03d73ed53ac6f6bedabbe5b831946646c59856150c4247a')
        self.assertEqual(self.coverage, set(range(ENTRY, ENTRY + end * 4, 4)))
        self.assertEqual(self.retail_coverage, set(range(ENTRY, ENTRY + 105 * 4, 4)))


if __name__ == '__main__':
    unittest.main()
