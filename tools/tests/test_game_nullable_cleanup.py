"""Typed cleanup fields: actual C callbacks and independent raw retail matching."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools import match_progress
from tools.tests import test_game_random_curve_record as curve


class GameNullableCleanupTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_1228D0.c').read_text()
        cls.body = re.search(r'void func_150F631C\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.types = ('typedef unsigned char u8; typedef unsigned int u32; '
                     'typedef struct struct102 struct102;\n#define NULL ((void *)0)\n')
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = cls.types + r'''
static union { u32 alignment; u8 bytes[0x60]; } storage;
static u8 *owner=storage.bytes+8;
static struct102 *expected[2], *replacement;
static int calls, error, mutate;
void func_1516972C(struct102 *value) {
    if(calls>=2 || value!=expected[calls]) error=1;
    calls++;
    if(mutate && calls==1) {
        *(struct102 **)(owner+0x30)=NULL;
        *(struct102 **)(owner+0x34)=replacement;
        owner[0x10]=0x19;
    }
}
static void reset(struct102 *first,struct102 *second) {
    int i;
    for(i=0;i<0x60;i++) storage.bytes[i]=0xA5;
    *(struct102 **)(owner+0x30)=first;
    *(struct102 **)(owner+0x34)=second;
    expected[0]=first?first:second; expected[1]=second;
    calls=error=mutate=0; replacement=NULL;
}
static int fences(void) {
    int i;
    for(i=0;i<0x60;i++) {
        if(i>=0x38 && i<0x40) continue;
        if(mutate && i==0x18) { if(storage.bytes[i]!=0x19) return 0; }
        else if(storage.bytes[i]!=0xA5) return 0;
    }
    return 1;
}
''' + cls.body + '\n'

    def test_nullable_pairs_forward_complete_pointer_values(self):
        self.run_host(r'''
u32 values[]={0,1,0x1000,0x7FFFFFFF,0x80000000,0x80001000,0xFFFFFFFF};
int i,j;
for(i=0;i<7;i++) for(j=0;j<7;j++) {
    reset((struct102 *)values[i],(struct102 *)values[j]);
    func_150F631C(owner);
    if(error || calls!=((i!=0)+(j!=0)) || !fences()) return 1;
    if((u32)*(struct102 **)(owner+0x30)!=values[i]
       || (u32)*(struct102 **)(owner+0x34)!=values[j]) return 2;
}
''')

    def test_first_callback_changes_second_field_before_its_read(self):
        self.run_host(r'''
u32 values[]={0,1,0x1000,0x7FFFFFFF,0x80000000,0x80001000,0xFFFFFFFF};
int i,j,k;
for(i=1;i<7;i++) for(j=0;j<7;j++) for(k=0;k<7;k++) {
    reset((struct102 *)values[i],(struct102 *)values[j]);
    mutate=1; replacement=(struct102 *)values[k]; expected[1]=replacement;
    func_150F631C(owner);
    if(error || calls!=1+(k!=0) || !fences()) return 1;
    if(*(struct102 **)(owner+0x30)!=NULL
       || *(struct102 **)(owner+0x34)!=replacement) return 2;
}
''')

    def compile_words(self, body, stem, allow_warnings=False):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(name) is None for name in
                                        ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            self.skipTest('IDO/MIPS tools are unavailable')
        source, obj, elf, script = (self.path / (stem + suffix)
                                   for suffix in ('.c', '.o', '.elf', '.ld'))
        source.write_text(self.types + 'void func_1516972C(struct102 *);\n' + body + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn',
            '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
            '-mips2', '-o32', '-O2', '-g3', '-o', str(obj), str(source)],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        if not allow_warnings:
            self.assertEqual(result.stdout + result.stderr, '')
        script.write_text('SECTIONS { .text 0x150F631C : SUBALIGN(4) { *(.text) } }\n')
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
            '-e', 'func_150F631C', '--defsym=func_1516972C=0x1516972C',
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        functions, _, addresses = match_progress.load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_150F631C'], 0x150F631C)
        words = functions['func_150F631C']
        self.assertEqual(len(words), 20)
        self.assertEqual(words[19:], [0])
        return words[:19]

    def test_fresh_typed_body_and_production_match_all_nineteen_words_without_guards(self):
        words = self.compile_words(self.body, 'typed')
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        retail = list(struct.unpack_from('>19I', rom, 0x1237CC))
        self.assertEqual(words, retail)
        packed = struct.pack('>19I', *words)
        self.assertEqual(hashlib.sha256(packed).hexdigest(),
                         '3d01686575967f832331b203dee11e677b94a8f8dc7ef88d6a270e2d887e1cdc')
        production, _, addresses = match_progress.load_elf_functions(
            str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_150F631C'], 0x150F631C)
        self.assertEqual(production['func_150F631C'], retail)
        with (self.root / 'conker/retail_word_patches.us.csv').open() as stream:
            self.assertFalse(any(row['function'] == 'func_150F631C'
                                 for row in csv.DictReader(stream)))

    def test_integer_field_control_reproduces_four_word_register_regression(self):
        body = self.body.replace('struct102 * volatile *', 'u32 volatile *')
        body = body.replace('struct102 **', 'u32 *').replace(' != NULL', ' != 0')
        words = self.compile_words(body, 'integer-control', allow_warnings=True)
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        retail = struct.unpack_from('>19I', rom, 0x1237CC)
        self.assertEqual([(i * 4, a, b) for i, (a, b) in enumerate(zip(words, retail)) if a != b],
                         [(0x14, 0x8CA20034, 0x8CA40034),
                          (0x28, 0x8CA20034, 0x8CA40034),
                          (0x2C, 0x50400004, 0x50800004),
                          (0x38, 0x00402025, 0x00000000)])

    def test_neighboring_functions_keep_checkpoint_bytes_and_addresses(self):
        production, _, addresses = match_progress.load_elf_functions(
            str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        checkpoints = {
            'func_150F6138': '4f7e855a3dea268b663493b36694680d393df2002defcc6c624874f2640b93ea',
            'func_150F6178': '5ea6f48e48b848b2b799158b83c0443ddd3e57f9f61cde7a2b8c5a68844977a1',
            'func_150F6368': 'b11adf8be22477fe9305e0aa04cb0c091eb13cd12fda833553df3bd715445e0d',
            'func_150F6394': 'f3098d8beb6292fad33020984967b604d647eb0248e64ef84fbdb4597011991b',
            'func_150F63C0': '8c5ab0dae97b7a7e9ba7881b0e70c785b97e0e6a7b2f73fd109b7547bc5af165',
            'func_150F6400': '44ea60cb98faef5a805992329730c97927692d4bc4cc04a065278c150970a0e0',
        }
        for name, digest in checkpoints.items():
            self.assertEqual(addresses[name], int(name[5:], 16))
            words = production[name]
            self.assertEqual(hashlib.sha256(struct.pack('>' + str(len(words)) + 'I', *words)).hexdigest(),
                             digest, name)


if __name__ == '__main__':
    unittest.main()
