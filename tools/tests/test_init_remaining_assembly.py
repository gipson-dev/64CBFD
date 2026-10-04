"""Audit retained Init ownership and the existing linked artifact, not C adoption."""

import csv
import hashlib
import re
import struct
import unittest
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from tools.check_game_data_layout import audit_layout, load_section
from tools.pad_generated_object import ELF_HEADER, SECTION_HEADER, read_c_string


SMALL = {'func_100038E0', 'func_10005BE0'}
DECODER = {'func_10006240', 'func_1000625C', 'func_1000632C',
           'func_10006380', 'func_10006424', 'func_10006828',
           'func_1000692C', 'func_1000696C', 'func_10006E00', 'func_1000709C'}
DIAGNOSTIC = {'__osCleanupThread', 'func_10007C74', 'func_10007CC4',
              'func_10007D28', 'func_10007DAC'}
RETAIN = {'func_10001000', 'func_10005AB0', 'func_10005B04',
          'func_10005C2C', 'func_100061F8', 'func_100071D0',
          'func_100077B8', 'func_100079D8', 'func_10007A24',
          'func_10007A38', 'func_10007DA0', 'osMapTLBRdb', 'bzero',
          '__osSetSR', '__osGetSR', '__osSetFpcCsr', 'osInvalICache',
          'osInvalDCache', '__osDisableInt', '__osRestoreInt', 'bcopy',
          'osWritebackDCache', 'osGetCount', 'osSetIntMask',
          'osWritebackDCacheAll', 'osUnmapTLB', 'osMapTLB', 'sqrtf',
          '__osProbeTLB', '__osSetCompare'}


class InitRemainingAssemblyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.project = Path(__file__).resolve().parents[2] / 'conker'
        with (cls.project / 'progress.init.csv').open(newline='') as source:
            cls.inventory = list(csv.DictReader(source))
        cls.rows = [row for row in cls.inventory if row['language'] == 'asm']
        cls.config = yaml.safe_load((cls.project / 'conker.us.yaml').read_text())
        cls.rom = (cls.project / 'conker.us.bin').read_bytes()
        cls.init = next(segment for segment in cls.config['segments']
                        if isinstance(segment, dict) and segment.get('name') == 'init')
        cls.sources = defaultdict(list)
        for path in (cls.project / 'src').rglob('*.c'):
            cls.sources[path.stem].append(path)

    def owner(self, row):
        direct = [segment for segment in self.init['subsegments']
                  if isinstance(segment, list) and len(segment) >= 3
                  and segment[1] == 'asm'
                  and Path(segment[2]).name == row['filename']]
        if direct:
            self.assertEqual(len(direct), 1)
            path = self.project / ('asm/' + direct[0][2] + '.s')
            self.assertTrue(path.is_file(), str(path))
            return path
        owners = []
        for source in self.sources[row['filename']]:
            for name in re.findall(r'#pragma\s+GLOBAL_ASM\("([^"]+)"\)',
                                   source.read_text()):
                path = self.project / name
                self.assertTrue(path.is_file(), str(path))
                if re.search(r'^glabel\s+' + re.escape(row['function']) + r'\s*$',
                             path.read_text(), re.MULTILINE):
                    owners.append(path)
        self.assertEqual(len(owners), 1, row['function'])
        return owners[0]

    def test_inventory_is_complete_contiguous_and_unchanged(self):
        self.assertEqual(len(self.inventory), 539)
        self.assertEqual(len({row['function'] for row in self.inventory}), 539)
        self.assertEqual(Counter(row['language'] for row in self.inventory),
                         {'c': 492, 'asm': 47})
        cursor = self.init['vram']
        totals = Counter()
        for row in sorted(self.inventory, key=lambda row: int(row['offset'])):
            self.assertEqual((row['version'], row['section']), ('us', 'init'))
            first, size = int(row['offset']), int(row['length'])
            self.assertEqual(first, cursor, row['function'])
            self.assertGreater(size, 0)
            self.assertEqual((first | size) & 3, 0)
            cursor += size
            totals[row['language']] += size
        self.assertEqual((cursor, dict(totals)),
                         (0x100290D0, {'asm': 12252, 'c': 151796}))

    def test_every_remaining_entry_has_an_explicit_decision_group(self):
        groups = (SMALL, DECODER, DIAGNOSTIC, RETAIN)
        self.assertEqual(sum(map(len, groups)), len(set().union(*groups)))
        self.assertEqual({row['function'] for row in self.rows}, set().union(*groups))
        expected = ((2, 120), (10, 3984), (5, 1308), (30, 6840))
        for names, measurement in zip(groups, expected):
            selected = [row for row in self.rows if row['function'] in names]
            self.assertEqual((len(selected), sum(int(row['length']) for row in selected)),
                             measurement)

    def test_pristine_reference_checksum(self):
        self.assertEqual(hashlib.sha1(self.rom).hexdigest(), self.config['sha1'])

    def test_all_assembly_owners_and_recorded_instruction_bytes(self):
        for row in self.rows:
            with self.subTest(function=row['function']):
                source = self.owner(row).read_text()
                self.assertRegex(source, r'(?m)^glabel\s+' +
                                 re.escape(row['function']) + r'\s*$')
                first, size = int(row['offset']), int(row['length'])
                entries = [(int(pc, 16), int(word, 16)) for pc, word in
                           re.findall(r'/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+'
                                      r'([0-9A-Fa-f]{8})\s*\*/', source)
                           if first <= int(pc, 16) < first + size]
                self.assertTrue(entries, row['function'])
                self.assertEqual(len(entries), len({pc for pc, _ in entries}))
                for pc, word in entries:
                    rom = self.init['start'] + pc - self.init['vram']
                    self.assertEqual(struct.unpack_from('>I', self.rom, rom)[0], word,
                                     hex(pc))

    def linked_init(self):
        elf = self.project / 'build/conker.us.elf'
        if not elf.is_file():
            self.skipTest('build/conker.us.elf is required for existing-artifact audit')
        data = elf.read_bytes()
        header = ELF_HEADER.unpack_from(data)
        self.assertEqual(header[0][:7], b'\x7fELF\x01\x02\x01')
        self.assertEqual(header[1:3], (2, 8))
        self.assertEqual(header[11], SECTION_HEADER.size)
        sections = list(SECTION_HEADER.iter_unpack(
            data[header[6]:header[6] + header[11] * header[12]]))
        self.assertEqual(len(sections), header[12])
        strings = sections[header[13]]
        names = data[strings[4]:strings[4] + strings[5]]
        found = [section for section in sections
                 if read_c_string(names, section[0]) == '.init']
        self.assertEqual(len(found), 1)
        section, = found
        self.assertEqual((section[1], section[2] & 6, section[3], section[5]),
                         (1, 6, 0x10001000, 164048))
        body = data[section[4]:section[4] + section[5]]
        self.assertEqual(len(body), section[5])
        return body

    def test_existing_linked_init_code_and_all_47_raw_slots(self):
        body = self.linked_init()
        self.assertEqual(body, self.rom[0x1000:0x290D0])
        self.assertEqual(hashlib.sha256(body).hexdigest(),
                         '34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf')
        for row in self.rows:
            first, size = int(row['offset']) - 0x10001000, int(row['length'])
            with self.subTest(function=row['function']):
                self.assertEqual(body[first:first + size],
                                 self.rom[first + 0x1000:first + 0x1000 + size])

    def test_existing_linked_init_data(self):
        self.linked_init()
        address, body = load_section(self.project / 'build/conker.us.elf', '.init_data')
        self.assertEqual((address, len(body)), (0x800290D0, 17376))
        self.assertEqual(body, self.rom[0x290D0:0x2D4B0])
        self.assertEqual(hashlib.sha256(body).hexdigest(),
                         'a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239')

    def test_existing_linked_game_data_remains_exact(self):
        self.linked_init()
        report = audit_layout(self.project / 'build/conker.us.elf', self.project)
        self.assertTrue(report['exact'], report)
        self.assertEqual((report['bytes'], report['owner_count']), (189088, 720))


if __name__ == '__main__':
    unittest.main()
