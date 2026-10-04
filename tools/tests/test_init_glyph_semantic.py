import json
import shutil
import struct
import subprocess
import unittest
from pathlib import Path

from tools.tests import test_init_glyph_register_contract as glyph


class SemanticFixture(glyph.GlyphFixture):
    def __init__(self, *args):
        super().__init__(*args)
        self.operations = []

    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        immediate = word & 65535
        offset = immediate if immediate < 32768 else immediate - 65536
        if op in (35, 36, 37, 40, 41, 43):
            address = (self.registers[rs] + offset) & 0xFFFFFFFF
            if not 0x800FFFC0 <= address < 0x80100010:
                size = {35: 4, 36: 1, 37: 2, 40: 1, 41: 2, 43: 4}[op]
                write = op in (40, 41, 43)
                value = self.registers[rt] & ((1 << (size * 8)) - 1) if write else self.get(address, size)
                self.operations.append(('write' if write else 'read', address, size, value))
        super().execute(word)


class InitGlyphSemanticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        glyph.InitGlyphRegisterContractTests.setUpClass()
        cls.retail = glyph.InitGlyphRegisterContractTests.code
        cls.root = Path(__file__).resolve().parents[2]
        compiler = cls.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file():
            raise unittest.SkipTest('IDO is unavailable')
        for tool in ('mips-linux-gnu-ld', 'mips-linux-gnu-objcopy'):
            if shutil.which(tool) is None:
                raise unittest.SkipTest(tool + ' is unavailable')
        cwd = cls.root / 'conker'
        output = cwd / 'build/init-glyph-semantic'
        output.mkdir(parents=True, exist_ok=True)
        cls.images, measurements = {}, []
        for profile, flags in (('o2g3', ['-O2', '-g3']),
                               ('o2g3-no-unroll', ['-O2', '-g3', '-Wo,-loopunroll,0']),
                               ('o1', ['-O1'])):
            prefix = 'build/init-glyph-semantic/' + profile
            obj, elf, binary = (prefix + suffix for suffix in ('.o', '.elf', '.bin'))
            (cwd / obj).unlink(missing_ok=True)
            result = subprocess.run([str(compiler), '-c', '-32', '-G', '0',
                '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared',
                '-Wab,-r4300_mul', '-mips2', '-o32', *flags, '-o', obj,
                '../tools/experiments/init_glyph_writer_semantic.c'],
                cwd=cwd, capture_output=True, text=True)
            if result.returncode or result.stdout or result.stderr or not (cwd / obj).is_file():
                raise AssertionError('glyph compile failed: ' + result.stdout + result.stderr)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip',
                            '-Ttext=0x10007D20', '-e', 'init_glyph_writer',
                            '-o', elf, obj], cwd=cwd, check=True, capture_output=True)
            subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', '.text',
                            elf, binary], cwd=cwd, check=True, capture_output=True)
            data = (cwd / binary).read_bytes()
            code = {0x10007D20 + i * 4: word[0] for i, word in
                    enumerate(struct.iter_unpack('>I', data))}
            cls.images[profile] = code
            last = max(pc for pc, word in code.items() if word == 0x03E00008) + 8
            measurements.append({'profile': profile, 'body_words': (last - 0x10007D20) // 4,
                                 'retail_words': 30, 'qualification': 'ordinary-ABI-trial'})
            disassembly = subprocess.check_output(['mips-linux-gnu-objdump', '-d', '-z', elf],
                                                  cwd=cwd, text=True)
            (cwd / (prefix + '.asm.txt')).write_text(disassembly)
        (output / 'measurements.json').write_text(json.dumps(measurements, indent=2) + '\n')

    def compare(self, rows, index=0, second_offset=0x10000, font_offset=None):
        for profile, code in self.images.items():
            fixtures = []
            for compiled in (False, True):
                fixture = SemanticFixture(code if compiled else self.retail, rows, index)
                fixture.readonly = []
                font = fixture.FONT if font_offset is None else fixture.DEST + font_offset
                fixture.memory.update((font + index * 8 + i, byte) for i, byte in enumerate(rows))
                fixture.registers[10:13] = [second_offset, index, font]
                fixture.registers[29] = fixture.before[29] = 0x80100000
                fixture.allowed_writes.append((0x800FFFC0, 0x80100010))
                fixture.memory.update((address, 0xA5) for address in range(0x800FFFC0, 0x80100010))
                if second_offset != 0x10000:
                    for row in range(8):
                        start = fixture.DEST + second_offset + row * fixture.STRIDE
                        fixture.allowed_writes.append((start, start + 16))
                        for address in range(start, start + 16):
                            fixture.memory.setdefault(address, 0xA5)
                if compiled:
                    fixture.image.entry = 0x10007D20
                    fixture.registers[4:8] = [fixture.DEST, second_offset, index, font]
                fixture.run(budget=10000)
                fixtures.append(fixture)
            retail, trial = fixtures
            with self.subTest(profile=profile, index=index, offset=second_offset, font=font_offset):
                def external(trace):
                    return [item for item in trace if not 0x800FFFC0 <= item[0] < 0x80100010]
                self.assertEqual(external(trial.writes), retail.writes)
                self.assertEqual(external(trial.reads), retail.reads)
                self.assertEqual(trial.operations, retail.operations)
                self.assertEqual({address: value for address, value in trial.memory.items()
                                  if not 0x800FFFC0 <= address < 0x80100010},
                                 {address: value for address, value in retail.memory.items()
                                  if not 0x800FFFC0 <= address < 0x80100010})
                self.assertEqual(trial.registers[2], retail.registers[9])
                for register in (*range(16, 24), 28, 29, 30, 31):
                    self.assertEqual(trial.registers[register], trial.before[register])

    def test_all_patterns_both_compiler_profiles(self):
        for byte in range(256):
            self.compare([(byte + row * 37) & 255 for row in range(8)], byte % 41)

    def test_overlapping_destinations(self):
        for offset in (0, 2, 8, 14):
            self.compare([0x80, 1, 0xAA, 0x55, 0, 255, 0x81, 0x18], second_offset=offset)

    def test_font_aliases_written_pixels_and_later_rows(self):
        for offset in (0, 2, 8, 14, 0x248, 0x24A):
            self.compare([0x81, 0x18, 0xAA, 0x55, 0, 255, 1, 0x80], font_offset=offset)


if __name__ == '__main__':
    unittest.main()
