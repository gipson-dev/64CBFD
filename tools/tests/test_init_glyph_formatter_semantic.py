import json
import shutil
import struct
import subprocess
import unittest
from pathlib import Path

from tools import match_progress
from tools.tests import test_init_glyph_adapter as adapter
from tools.tests import test_init_glyph_formatters as formatters


class FormatterSemanticFixture(adapter.AdapterFixture):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_writes.append((0x800FFF00, 0x80100020))
        self.memory.update((address, 0xA5) for address in range(0x800FFF00, 0x80100020))

    def execute(self, word):
        # The C trial owns its frame and output cells; neither is retail output.
        op, rs = word >> 26, word >> 21 & 31
        offset = word & 65535
        offset = offset if offset < 32768 else offset - 65536
        address = (self.registers[rs] + offset) & 0xFFFFFFFF
        before = len(self.operations)
        super().execute(word)
        if op in (32, 35, 36, 37, 40, 41, 43) and 0x800FFF00 <= address < 0x80100020:
            del self.operations[before:]


class InitGlyphFormatterSemanticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        formatters.InitGlyphFormatterTests.setUpClass()
        cls.retail = formatters.InitGlyphFormatterTests.code
        root = Path(__file__).resolve().parents[2]
        cwd = root / 'conker'
        compiler = root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file():
            raise unittest.SkipTest('IDO is unavailable')
        for tool in ('mips-linux-gnu-ld', 'mips-linux-gnu-objcopy', 'mips-linux-gnu-objdump'):
            if shutil.which(tool) is None:
                raise unittest.SkipTest(tool + ' is unavailable')
        output = cwd / 'build/init-glyph-formatters-semantic'
        output.mkdir(parents=True, exist_ok=True)
        cls.images, cls.receipts = {}, {}
        for profile, flags in (('o2g3-no-unroll', ['-O2', '-g3', '-Wo,-loopunroll,0']),
                               ('o1', ['-O1']),
                               ('shared-o2g3-no-unroll', ['-O2', '-g3', '-Wo,-loopunroll,0', '-DGLYPH_SHARED_SETUP']),
                               ('shared-o1', ['-O1', '-DGLYPH_SHARED_SETUP'])):
            prefix = 'build/init-glyph-formatters-semantic/' + profile
            objects = []
            for name, source, options in (
                    ('formatters', 'init_glyph_formatters_semantic.c', flags),
                    ('writer', 'init_glyph_writer_semantic.c',
                     ['-O2', '-g3', '-Wo,-loopunroll,0', '-DGLYPH_LOW_PIXEL', '-DGLYPH_COUNTDOWN'])):
                obj = prefix + '-' + name + '.o'
                (cwd / obj).unlink(missing_ok=True)
                result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn',
                    '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
                    '-mips2', '-o32', *options, '-o', obj, '../tools/experiments/' + source],
                    cwd=cwd, capture_output=True, text=True)
                if result.returncode or result.stdout or result.stderr or not (cwd / obj).is_file():
                    raise AssertionError(result.stdout + result.stderr)
                objects.append(obj)
            elf, binary = prefix + '.elf', prefix + '.bin'
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-Ttext=0x10009000',
                            '-e', 'init_glyph_hex', '--defsym=D_8002AAE8=0x8002AAE8',
                            '--defsym=D_8002AC84=0x8002AC84', '-o', elf, *objects],
                           cwd=cwd, check=True, capture_output=True)
            subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', '.text', elf, binary],
                           cwd=cwd, check=True, capture_output=True)
            data = (cwd / binary).read_bytes()
            code = {0x10009000 + i * 4: word[0] for i, word in enumerate(struct.iter_unpack('>I', data))}
            words, _, addresses = match_progress.load_elf_functions(str(cwd / elf), 'mips-linux-gnu-objdump')
            if 'shared' in profile:
                # IDO omits the static symbol; pin its entry through both callers.
                if '_ftext' in words:
                    for caller in ('init_glyph_hex', 'init_glyph_string'):
                        call_index = next(i for i, word in enumerate(words[caller]) if word >> 26 == 3)
                        target = match_progress.jump_target(words[caller][call_index], addresses[caller] + call_index * 4)
                        if target != addresses['_ftext']:
                            raise AssertionError('unexpected shared setup call target')
                    words['init_glyph_destination'] = words.pop('_ftext')
            cls.images[profile] = (code, addresses)
            cls.receipts[profile] = {'allocated_text_bytes': len(data), 'functions': {
                name: {'slot_words': len(body), 'body_words': max(i for i, word in enumerate(body)
                   if word == 0x03E00008) + 2} for name, body in words.items()}}
        (output / 'measurements.json').write_text(json.dumps(cls.receipts, indent=2) + '\n')
        cls.depths = {}

    def compare(self, position, value=0, text=None, pointers=None, alias=None):
        original = 0x10007C74 if text is None else 0x10007CC4
        for profile, (code, addresses) in self.images.items():
            fixtures = []
            for compiled in (False, True):
                fixture = FormatterSemanticFixture(code if compiled else self.retail,
                    addresses['init_glyph_hex' if text is None else 'init_glyph_string']
                    if compiled else original, position, value, text)
                if pointers is not None:
                    fixture.allowed_writes = None
                    fixture.put(0x8002AAE8, pointers[0], 4)
                    fixture.put(0x8002AAEC, pointers[1], 4)
                if alias is not None:
                    address = fixture.DEST + 0x4A0 + alias
                    fixture.memory.update((address + i, byte) for i, byte in enumerate(text + b'\0'))
                    fixture.registers[5] = address
                fixture.registers[6] = 0x80100010
                fixture.run()
                fixtures.append(fixture)
            retail, trial = fixtures
            with self.subTest(profile=profile, position=position, value=value, text=text, alias=alias):
                self.assertEqual(trial.operations, retail.operations)
                self.assertEqual({address: value for address, value in trial.memory.items()
                                  if not 0x800FFF00 <= address < 0x80100020},
                                 {address: value for address, value in retail.memory.items()
                                  if not 0x800FFF00 <= address < 0x80100020})
                success = pointers is None or all(pointers)
                self.assertEqual(trial.registers[2], int(success))
                if success:
                    self.assertEqual(trial.get(0x80100010, 4), retail.registers[9])
                    if text is not None:
                        self.assertEqual(trial.get(0x80100014, 4), retail.registers[3])
                else:
                    self.assertEqual(trial.get(0x80100010, 8), 0xA5A5A5A5A5A5A5A5)
                for register in (*range(16, 24), 28, 29, 30, 31):
                    self.assertEqual(trial.registers[register], trial.before[register])
                self.depths[profile] = max(self.depths.get(profile, 0), 0x80100000 - trial.min_sp)

    def test_hex_positions_and_patterns(self):
        for position in (0, 31, 32, 63, 0x300):
            for value in (0, 0xFFFFFFFF, 0x12345678, 0x80000001):
                self.compare(position, value)

    def test_all_signed_bytes_and_strings(self):
        for byte in range(1, 256):
            self.compare(0, text=bytes([byte]))
        for text in (b'', b'0123456789ABCDEF', b' A@Z[az\x80\xff'):
            self.compare(32, text=text)

    def test_output_can_mutate_later_text_reads(self):
        for offset in (0, 2, 8, 14):
            self.compare(0, text=b'ABCD', alias=offset)

    def test_null_buffers_leave_result_cells_unwritten(self):
        for pointers in ((0, 0x80210000), (0x80200000, 0), (0, 0)):
            self.compare(0, value=0x12345678, pointers=pointers)
            self.compare(0, text=b'A', pointers=pointers)

    def test_shared_setup_linked_text_tradeoff(self):
        self.assertEqual(self.receipts['o2g3-no-unroll']['allocated_text_bytes'], 624)
        self.assertEqual(self.receipts['shared-o2g3-no-unroll']['allocated_text_bytes'], 608)
        self.assertEqual(self.receipts['o1']['allocated_text_bytes'], 704)
        self.assertEqual(self.receipts['shared-o1']['allocated_text_bytes'], 688)
        self.assertEqual(self.receipts['shared-o2g3-no-unroll']['functions']
                         ['init_glyph_destination']['body_words'], 29)

    @classmethod
    def tearDownClass(cls):
        output = Path(__file__).resolve().parents[2] / 'conker/build/init-glyph-formatters-semantic'
        (output / 'stack-depths.json').write_text(json.dumps(cls.depths, indent=2) + '\n')


if __name__ == '__main__':
    unittest.main()
