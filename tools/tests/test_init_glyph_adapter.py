import json
import shutil
import struct
import subprocess
import unittest
from pathlib import Path

from tools.tests import test_init_glyph_formatters as formatters


class AdapterFixture(formatters.FormatterFixture):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.registers[29] = self.before[29] = 0x80100000
        self.min_sp = self.registers[29]
        self.allowed_writes.append((0x800FFFC8, 0x80100000))
        self.memory.update((address, 0xA5) for address in range(0x800FFFC0, 0x80100008))
        self.operations = []

    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        immediate = word & 65535
        offset = immediate if immediate < 32768 else immediate - 65536
        if op in (32, 35, 36, 37, 40, 41, 43):
            address = (self.registers[rs] + offset) & 0xFFFFFFFF
            if not 0x800FFFC8 <= address < 0x80100000:
                size = {32: 1, 35: 4, 36: 1, 37: 2, 40: 1, 41: 2, 43: 4}[op]
                write = op in (40, 41, 43)
                value = self.registers[rt] & ((1 << (size * 8)) - 1) if write else self.get(address, size)
                self.operations.append(('write' if write else 'read', address, size, value))
        super().execute(word)
        self.min_sp = min(self.min_sp, self.registers[29])


class InitGlyphAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        formatters.InitGlyphFormatterTests.setUpClass()
        cls.retail = formatters.InitGlyphFormatterTests.code
        cls.root = Path(__file__).resolve().parents[2]
        cwd = cls.root / 'conker'
        compiler = cls.root / 'ido/ido5.3_recomp/cc'
        for tool in ('mips-linux-gnu-as', 'mips-linux-gnu-ld', 'mips-linux-gnu-objcopy'):
            if shutil.which(tool) is None:
                raise unittest.SkipTest(tool + ' is unavailable')
        if not compiler.is_file():
            raise unittest.SkipTest('IDO is unavailable')
        output = cwd / 'build/init-glyph-adapter'
        output.mkdir(parents=True, exist_ok=True)
        prefix = 'build/init-glyph-adapter/'
        (output / 'writer.o').unlink(missing_ok=True)
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn',
            '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
            '-mips2', '-o32', '-O2', '-g3', '-Wo,-loopunroll,0', '-DGLYPH_LOW_PIXEL',
            '-DGLYPH_COUNTDOWN', '-o', prefix + 'writer.o',
            '../tools/experiments/init_glyph_writer_semantic.c'], cwd=cwd,
            capture_output=True, text=True)
        if result.returncode or result.stdout or result.stderr:
            raise AssertionError(result.stdout + result.stderr)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-mabi=32',
                        '-o', prefix + 'adapter.o', '../tools/experiments/init_glyph_writer_adapter.s'],
                       cwd=cwd, check=True, capture_output=True)
        (output / 'adapter.ld').write_text('SECTIONS { .adapter 0x10007D28 : SUBALIGN(4) '
            '{ *(.text.glyph_adapter) } .text 0x10009000 : { *(.text) } }\n')
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', prefix + 'adapter.ld',
                        '-e', 'init_glyph_writer_adapter', '-o', prefix + 'adapter.elf',
                        prefix + 'adapter.o', prefix + 'writer.o'], cwd=cwd,
                       check=True, capture_output=True)
        cls.candidate = dict(cls.retail)
        cls.sizes = {}
        for section, address in (('.adapter', 0x10007D28), ('.text', 0x10009000)):
            filename = prefix + section[1:] + '.bin'
            subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', section,
                            prefix + 'adapter.elf', filename], cwd=cwd, check=True, capture_output=True)
            data = (cwd / filename).read_bytes()
            cls.sizes[section] = len(data)
            cls.candidate.update((address + i * 4, word[0]) for i, word in
                                 enumerate(struct.iter_unpack('>I', data)))
        (output / 'measurements.json').write_text(json.dumps(cls.sizes, indent=2) + '\n')

    def compare(self, entry, position, value=0, text=None, buffers=True):
        fixtures = []
        for code in (self.retail, self.candidate):
            fixture = AdapterFixture(code, entry, position, value, text, buffers)
            fixture.run()
            fixtures.append(fixture)
        retail, candidate = fixtures
        self.assertEqual(candidate.glyphs, retail.glyphs)
        self.assertEqual(candidate.operations, retail.operations)
        self.assertEqual({address: value for address, value in candidate.memory.items()
                          if not 0x800FFFC8 <= address < 0x80100000},
                         {address: value for address, value in retail.memory.items()
                          if not 0x800FFFC8 <= address < 0x80100000})
        for register in (2, 3, 4, 5, 8, 9, 10, 12, 25, 26, 27, 28, 29, 30, 31, *range(16, 24)):
            self.assertEqual(candidate.registers[register], retail.registers[register])
        self.assertEqual(candidate.min_sp, 0x800FFFC8 if candidate.glyphs else 0x80100000)

    def test_adapter_extent_and_total_allocated_text(self):
        self.assertEqual(self.sizes, {'.adapter': 120, '.text': 128})
        self.assertEqual(sum(self.sizes.values()), 248)

    def test_hex_connected_live_registers(self):
        for position in (0, 31, 32, 63, 0x300):
            for value in (0, 0xFFFFFFFF, 0x12345678, 0x80000001):
                self.compare(0x10007C74, position, value)

    def test_all_signed_character_bytes(self):
        for byte in range(1, 256):
            self.compare(0x10007CC4, 0, text=bytes([byte]))

    def test_empty_and_multicharacter_continuation(self):
        for text in (b'', b'0123456789ABCDEF', b' A@Z[az\x80\xff'):
            self.compare(0x10007CC4, 32, text=text)

    def test_missing_buffers_skip_adapter_and_stack(self):
        for entry in (0x10007C74, 0x10007CC4):
            self.compare(entry, 0, text=b'A', buffers=False)

    def test_direct_leaf_preserves_all_required_registers(self):
        for index in (0, 9, 24, 40, 81):
            fixtures = []
            for code in (self.retail, self.candidate):
                fixture = AdapterFixture(code, 0x10007D28, 0)
                fixture.registers[11] = index
                fixture.run()
                fixtures.append(fixture)
            retail, candidate = fixtures
            clobbered = {1, 6, 7, 9, 11, 13, 14, 15, 24}
            for register in set(range(32)) - clobbered:
                self.assertEqual(candidate.registers[register], retail.registers[register])
            self.assertEqual(candidate.registers[6:8], [0, 0])
            self.assertEqual(candidate.registers[9], retail.registers[9])
            self.assertEqual(candidate.operations, retail.operations)

    def test_stack_fence_rejects_below_frame_and_caller_stack(self):
        fixture = AdapterFixture(self.candidate, 0x10007C74, 0)
        for address in (0x800FFFC4, 0x80100000):
            with self.assertRaisesRegex(AssertionError, 'caller-owned'):
                fixture.put(address, 0, 4)


if __name__ == '__main__':
    unittest.main()
