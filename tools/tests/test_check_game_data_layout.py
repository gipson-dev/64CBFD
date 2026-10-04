import copy
import hashlib
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.check_game_data_layout import audit_layout, compare_layout, load_section
from tools.pad_generated_object import ELF_HEADER, SECTION_HEADER
from tools.patch_generated_slice_ld import load_game_data_layout


def section_elf(address, payload):
    names = b'\0.shstrtab\0.game_data\0'
    names_offset = ELF_HEADER.size + 3 * SECTION_HEADER.size
    payload_offset = names_offset + len(names)
    header = ELF_HEADER.pack(b'\x7fELF\x01\x02\x01' + bytes(9), 2, 8, 1,
                             0, 0, ELF_HEADER.size, 0, ELF_HEADER.size, 0, 0,
                             SECTION_HEADER.size, 3, 1)
    sections = [bytes(SECTION_HEADER.size),
                SECTION_HEADER.pack(1, 3, 0, 0, names_offset, len(names), 0, 0, 1, 0),
                SECTION_HEADER.pack(11, 1, 3, address, payload_offset, len(payload), 0, 0, 4, 0)]
    return header + b''.join(sections) + names + payload


class CheckGameDataLayoutTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.project = Path(self.temporary.name)
        self.reference = bytes(range(64))
        (self.project / 'conker.us.bin').write_bytes(self.reference)
        self.config = {'sha1': hashlib.sha1(self.reference).hexdigest(), 'segments': [
            {'name': 'game_data', 'start': 0x20, 'vram': 0x80000000,
             'subsegments': [[0x20, 'data'], [0x30, 'rodata']]}, [0x40]]}
        (self.project / 'conker.us.yaml').write_text(yaml.safe_dump(self.config))
        self.layout = load_game_data_layout(self.project)
        self.elf = self.project / 'data.elf'
        self.elf.write_bytes(section_elf(0x80000000, self.reference[0x20:0x40]))

    def test_complete_section_address_length_bytes_and_owner_count(self):
        address, data = load_section(self.elf, '.game_data')
        self.assertEqual((address, data), (0x80000000, self.reference[0x20:0x40]))
        report = audit_layout(self.elf, self.project)
        self.assertTrue(report['exact'])
        self.assertEqual((report['bytes'], report['different_bytes'], report['owner_count']),
                         (32, 0, 2))

    def test_differences_missing_tail_and_wrong_address_reject(self):
        expected = self.reference[0x20:0x40]
        mutated = bytes([expected[0] ^ 1]) + expected[1:16] + bytes([expected[16] ^ 1]) + expected[17:]
        report = compare_layout(0x80000000, mutated, self.reference, self.layout)
        self.assertFalse(report['exact'])
        self.assertEqual((report['different_bytes'], report['different_owner_count']), (2, 2))
        self.assertEqual([owner['different_bytes'] for owner in report['different_owners']], [1, 1])
        short = compare_layout(0x80000000, expected[:-4], self.reference, self.layout)
        self.assertFalse(short['exact'])
        self.assertEqual(short['different_bytes'], 4)
        self.assertEqual(short['different_owners'][0]['rom'], 0x30)
        shifted = compare_layout(0x80000004, expected, self.reference, self.layout)
        self.assertFalse(shifted['exact'])

    def test_reference_checksum_and_truncation_fail_closed(self):
        (self.project / 'conker.us.bin').write_bytes(bytes(64))
        with self.assertRaisesRegex(ValueError, 'checksum'):
            audit_layout(self.elf, self.project)
        with self.assertRaisesRegex(ValueError, 'does not cover'):
            compare_layout(0x80000000, bytes(32), bytes(63), self.layout)

    def test_invalid_elf_header_ranges_sections_and_duplicates_fail_closed(self):
        original = self.elf.read_bytes()
        variants = [original[:20], original[:-1]]
        for offset, value, format in ((18, 3, '>H'), (32, 0xFFFFFFF0, '>I'),
                                      (50, 3, '>H'),
                                      (ELF_HEADER.size + 2 * SECTION_HEADER.size + 8, 7, '>I'),
                                      (ELF_HEADER.size + SECTION_HEADER.size, 11, '>I')):
            mutant = bytearray(original)
            struct.pack_into(format, mutant, offset, value)
            variants.append(mutant)
        for data in variants:
            self.elf.write_bytes(data)
            with self.subTest(data=data[:52]), self.assertRaises(ValueError):
                load_section(self.elf, '.game_data')

    def test_cli_exit_code_and_display_limit_do_not_reduce_comparison(self):
        tool = Path(__file__).resolve().parents[1] / 'check_game_data_layout.py'
        command = [sys.executable, str(tool), str(self.elf), '--project-dir',
                   str(self.project), '--limit', '0']
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)['exact'])
        self.elf.write_bytes(section_elf(0x80000000, bytes(32)))
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual((report['different_bytes'], report['different_owner_count']), (32, 2))
        self.assertEqual(report['different_owners'], [])

    def test_restored_pool_assembly_and_no_padding_table_equal_retail(self):
        for tool in ('mips-linux-gnu-as', 'mips-linux-gnu-objcopy'):
            if shutil.which(tool) is None:
                self.skipTest(tool + ' is unavailable')
        project = Path(__file__).resolve().parents[2] / 'conker'
        reference = (project / 'conker.us.bin').read_bytes()
        spans = ((0x23D870, 0x23D880, 'rodata'), (0x23D880, 0x23D890, 'rodata'),
                 (0x23D890, 0x23D8A0, 'rodata'), (0x23D8A0, 0x23D8C0, 'rodata'),
                 (0x236578, 0x2365B0, 'data'))
        for first, last, section in spans:
            source = project / ('asm/data/%X.%s.s' % (first, section))
            obj, binary = self.project / 'pool.o', self.project / 'pool.bin'
            command = ['mips-linux-gnu-as', '-EB', '-march=vr4300', '-mabi=32',
                       '-I', str(project / 'include'), '-o', str(obj), str(source)]
            if section == 'data':
                command.insert(1, '-no-pad-sections')
            subprocess.run(command, check=True)
            subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '--only-section=.' + section,
                            str(obj), str(binary)], check=True)
            self.assertEqual(binary.read_bytes(), reference[first:last])
        # The omitted flag must reproduce the exact eight-byte padding failure.
        command.remove('-no-pad-sections')
        subprocess.run(command, check=True)
        subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '--only-section=.data',
                        str(obj), str(binary)], check=True)
        self.assertEqual(binary.read_bytes(), reference[0x236578:0x2365B0] + bytes(8))

    def test_fresh_yaml_extraction_recreates_pools_without_manual_generated_files(self):
        for tool in ('mips-linux-gnu-as', 'mips-linux-gnu-objcopy'):
            if shutil.which(tool) is None:
                self.skipTest(tool + ' is unavailable')
        root = Path(__file__).resolve().parents[2]
        config = yaml.safe_load((root / 'conker/conker.us.yaml').read_text())
        segment = copy.deepcopy(next(segment for segment in config['segments']
                                     if isinstance(segment, dict) and segment.get('name') == 'game_data'))
        first, last = segment['start'], 0x255880
        reference = (root / 'conker/conker.us.bin').read_bytes()
        directory = self.project / 'fresh-extraction'
        directory.mkdir()
        (directory / 'retail-data.bin').write_bytes(reference[first:last])
        segment['start'] = 0
        for entry in segment['subsegments']:
            # Rebase the disposable ROM while preserving production owner filenames.
            if len(entry) == 2:
                entry.append('%X' % entry[0])
            entry[0] -= first
        options = copy.deepcopy(config['options'])
        options.update({'base_path': str(directory), 'target_path': 'retail-data.bin',
                        'basename': 'data-proof', 'symbol_addrs_path': [],
                        'generated_c_preamble': ''})
        manifest = directory / 'proof.yaml'
        manifest.write_text(yaml.safe_dump({'options': options,
                                           'segments': [segment, [last - first]]}, sort_keys=False))
        result = subprocess.run([sys.executable, str(root / 'tools/n64splat/split.py'),
                                 str(manifest), '--skip-version-check'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for first, last, kind in ((0x23D870, 0x23D880, 'rodata'),
                                  (0x23D880, 0x23D890, 'rodata'),
                                  (0x23D890, 0x23D8A0, 'rodata'),
                                  (0x23D8A0, 0x23D8C0, 'rodata'),
                                  (0x236578, 0x2365B0, 'data')):
            sources = list(directory.rglob('%X.%s.s' % (first, kind)))
            self.assertEqual(len(sources), 1)
            obj, binary = directory / 'pool.o', directory / 'pool.bin'
            command = ['mips-linux-gnu-as', '-EB', '-march=vr4300', '-mabi=32',
                       '-I', str(root / 'conker/include'), '-o', str(obj), str(sources[0])]
            if kind == 'data':
                command.insert(1, '-no-pad-sections')
            subprocess.run(command, check=True)
            subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '--only-section=.' + kind,
                            str(obj), str(binary)], check=True)
            self.assertEqual(binary.read_bytes(), reference[first:last])


if __name__ == '__main__':
    unittest.main()
