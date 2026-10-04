import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

from tools.patch_generated_slice_ld import (
    anchor_init_math_rodata,
    restore_init_audio_data_order,
    load_game_data_layout,
    restore_game_data_order,
)
from tools.check_game_data_layout import load_section


class InitMathRodataTests(unittest.TestCase):
    def test_anchor_precedes_original_constant_owner(self):
        text = (
            "        build/asm/data/2C830.rodata.s.o(.rodata);\n"
            "        build/asm/data/2C850.rodata.s.o(.rodata);\n"
            "        build/asm/data/2C920.rodata.s.o(.rodata);\n"
        )
        expected = text.replace(
            "        build/asm/data/2C850.rodata.s.o(.rodata);",
            "        . = ABSOLUTE(0x8002C850);\n"
            "        build/asm/data/2C850.rodata.s.o(.rodata);",
        )
        self.assertEqual(anchor_init_math_rodata(text), expected)

    def test_unrelated_layout_is_unchanged(self):
        text = "        build/asm/data/2C830.rodata.s.o(.rodata);\n"
        self.assertEqual(anchor_init_math_rodata(text), text)


class InitAudioDataOrderTests(unittest.TestCase):
    def make_layout(self):
        owners = [
            "assets/2C250.bin.o(.data)",
            "assets/2C460.bin.o(.data)",
            "assets/2C6B0.bin.o(.data)",
            "assets/2C7A0.bin.o(.data)",
            "asm/data/2C0C0.rodata.s.o(.rodata)",
            "asm/data/2C120.rodata.s.o(.rodata)",
            "asm/data/2C1B0.rodata.s.o(.rodata)",
            "asm/data/2C200.rodata.s.o(.rodata)",
            "asm/data/2C240.rodata.s.o(.rodata)",
            "src/libultra/audio/init_128D0.c.o(.rodata)",
            "asm/data/2C750.rodata.s.o(.rodata)",
            "src/libultra/audio/cents2ratio.c.o(.rodata)",
            "asm/data/2C770.rodata.s.o(.rodata)",
            "src/libultra/audio/init_1D900.c.o(.rodata)",
        ]
        return (
            "        init_data_DATA_START = .;\n" +
            "".join(f"        build/{owner};\n" for owner in owners) +
            "        init_data_RODATA_END = .;\n"
        )

    def test_retail_interleaving_and_anchors(self):
        result = restore_init_audio_data_order(self.make_layout())
        ordered = [
            "2C0C0.rodata", "2C120.rodata", "2C1B0.rodata", "2C200.rodata",
            "2C240.rodata", "2C250.bin", "init_128D0.c", "0x8002C460",
            "2C460.bin", "2C6B0.bin", "2C750.rodata", "cents2ratio.c",
            "0x8002C770", "2C770.rodata", "init_1D900.c", "0x8002C7A0",
            "2C7A0.bin",
        ]
        positions = [result.index(name) for name in ordered]
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(result.count("build/"), 14)

    def test_missing_owner_is_rejected(self):
        text = self.make_layout().replace(
            "        build/assets/2C460.bin.o(.data);\n", ""
        )
        with self.assertRaisesRegex(ValueError, "expected one Init data owner"):
            restore_init_audio_data_order(text)

    def test_unrelated_layout_is_unchanged(self):
        text = "        build/asm/data/2C830.rodata.s.o(.rodata);\n"
        self.assertEqual(restore_init_audio_data_order(text), text)


class GameDataOrderTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.project = Path(self.temporary.name)
        self.entries = [[0x1000, 'data'], [0x1010, 'rodata', 'first'],
                        [0x1020, '.rodata', 'sdk/math'], [0x1030, 'bin'],
                        [0x1038, 'data'], [0x1040, 'rodata']]
        self.config = {'segments': [{'name': 'game_data', 'start': 0x1000,
                                    'vram': 0x80001000, 'subsegments': self.entries},
                                   {'name': 'debugger', 'start': 0x1050}]}
        self.write_config()

    def write_config(self):
        (self.project / 'conker.us.yaml').write_text(yaml.safe_dump(self.config))

    def make_layout(self):
        owners = load_game_data_layout(self.project)[3]
        grouped = sorted(owners, key=lambda owner: owner['section'])
        return ('/* before */\ngame_data_ROM_START = 0;\n'
                '    .game_data 0x80001000 : AT(game_data_ROM_START) SUBALIGN(16)\n    {\n'
                '        game_data_DATA_START = .;\n' +
                ''.join('        ' + owner['input'] + ';\n' for owner in grouped) +
                '        game_data_RODATA_END = .;\n    }\n/* after */\n')

    def test_all_owner_kinds_addresses_and_retail_interleaving(self):
        _, _, _, owners = load_game_data_layout(self.project)
        self.assertEqual([owner['address'] for owner in owners],
                         [0x80001000, 0x80001010, 0x80001020,
                          0x80001030, 0x80001038, 0x80001040])
        self.assertEqual([owner['input'] for owner in owners],
                         ['build/asm/data/1000.data.s.o(.data)',
                          'build/asm/data/first.rodata.s.o(.rodata)',
                          'build/src/sdk/math.c.o(.rodata)',
                          'build/assets/1030.bin.o(.data)',
                          'build/asm/data/1038.data.s.o(.data)',
                          'build/asm/data/1040.rodata.s.o(.rodata)'])
        result = restore_game_data_order(self.make_layout(), self.project)
        positions = [result.index(owner['input'] + ';') for owner in owners]
        self.assertEqual(positions, sorted(positions))
        self.assertIn('SUBALIGN(4)', result)
        self.assertIn('. = ABSOLUTE(0x80001038);', result)
        self.assertIn('. = ABSOLUTE(0x80001050);', result)
        self.assertEqual(result.count('ASSERT('), len(owners))
        self.assertEqual(result.count('game_data_DATA_END = .;'), 1)

    def test_idempotent_and_unrelated_layout_preserved(self):
        original = self.make_layout()
        result = restore_game_data_order(original, self.project)
        self.assertEqual(restore_game_data_order(result, self.project), result)
        self.assertTrue(result.startswith('/* before */\ngame_data_ROM_START = 0;\n'))
        self.assertTrue(result.endswith('/* after */\n'))
        unrelated = '.init_data 0x800290D0 : SUBALIGN(16) { }\n'
        self.assertEqual(restore_game_data_order(unrelated, self.project), unrelated)

    def test_missing_extra_and_duplicate_linker_owners_fail_closed(self):
        original = self.make_layout()
        owner = '        build/asm/data/1000.data.s.o(.data);\n'
        for text in (original.replace(owner, ''), original.replace(owner, owner * 2),
                     original.replace(owner, owner + '        build/extra.o(.bss);\n'),
                     original.replace(owner, owner + '        KEEP(build/extra.o(.data));\n'),
                     original.replace(owner, owner + '        *(.data);\n')):
            with self.subTest(text=text), self.assertRaisesRegex(ValueError, 'owners differ'):
                restore_game_data_order(text, self.project)

    def test_wrong_base_and_duplicate_markers_fail_closed(self):
        original = self.make_layout()
        for text in (original.replace('0x80001000', '0x80001004'),
                     original.replace('game_data_DATA_START = .;',
                                      'game_data_DATA_START = .;\n        game_data_DATA_START = .;')):
            with self.subTest(text=text), self.assertRaises(ValueError):
                restore_game_data_order(text, self.project)

    def test_invalid_yaml_entries_and_boundaries_are_rejected(self):
        bad_entries = ([], [[0x1000]], [[0x1000, 'data', 'x', 'extra']],
                       [[0x1000, 'data'], [0x1000, 'rodata']],
                       [[0x1004, 'rodata']], [[0x1001, 'data']],
                       [[0x1000, 'bss']], [[0x1000, '.rodata']],
                       [[0x1000, 'data', '../escape']],
                       [[0x1000, 'rodata', 'x'], [0x1010, 'rodata', 'x']])
        for entries in bad_entries:
            self.config['segments'][0]['subsegments'] = entries
            self.write_config()
            with self.subTest(entries=entries), self.assertRaises(ValueError):
                load_game_data_layout(self.project)
        self.config['segments'][0]['subsegments'] = self.entries
        for end in (0x1000, 0x1040, None, True):
            self.config['segments'][1]['start'] = end
            self.write_config()
            with self.subTest(end=end), self.assertRaises(ValueError):
                load_game_data_layout(self.project)

    def test_current_manifest_is_complete_and_contains_fixed_coefficient_owner(self):
        project = Path(__file__).resolve().parents[2] / 'conker'
        start, vram, end, owners = load_game_data_layout(project)
        self.assertEqual((start, vram, end, len(owners)),
                         (0x2275E0, 0x80082B20, 0x255880, 720))
        coefficient, = [owner for owner in owners if owner['rom'] == 0x245C90]
        self.assertEqual(coefficient['address'] + 0x180, 0x800A1350)
        pools = [owner for owner in owners if 0x23D870 <= owner['rom'] < 0x23D8C0]
        self.assertEqual(len(pools), 4)
        self.assertTrue(all('/asm/data/' in owner['input'] for owner in pools))
        self.assertEqual(sum(owner['end'] - owner['address'] for owner in pools), 80)

    def test_stale_generated_c_pool_selectors_are_repaired(self):
        project = Path(__file__).resolve().parents[2] / 'conker'
        original = (project / 'conker.ld').read_text()
        repaired = restore_game_data_order(original, project)
        for source, address in (('libultra/gu/guPerspectiveF', '23D870'),
                                ('libultra/gu/guRotateF', '23D880'),
                                ('game/done/game_75810', '23D890'),
                                ('game/done/game_75950', '23D8A0')):
            original = original.replace('build/asm/data/' + address + '.rodata.s.o(.rodata);',
                                        'build/src/' + source + '.c.o(.rodata);')
        self.assertEqual(restore_game_data_order(original, project), repaired)

    def link_fixture(self, overflow=False):
        for tool in ('mips-linux-gnu-as', 'mips-linux-gnu-ld'):
            if shutil.which(tool) is None:
                self.skipTest(tool + ' is unavailable')
        owners = load_game_data_layout(self.project)[3]
        for index, owner in enumerate(owners):
            target = self.project / owner['input'].split('(')[0]
            target.parent.mkdir(parents=True, exist_ok=True)
            source = target.with_suffix('.fixture.s')
            size = owner['end'] - owner['address']
            if overflow and owner['rom'] == 0x1038:
                size += 1
            source.write_text('.section ' + owner['section'] + ',"a' +
                              ('w' if owner['section'] == '.data' else '') + '"\n' +
                              '.space %d, %d\n' % (size, index + 1))
            subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-mabi=32',
                            '-no-pad-sections', '-o', str(target), str(source)], check=True)
        script = self.project / 'layout.ld'
        script.write_text('SECTIONS {\n' + restore_game_data_order(self.make_layout(), self.project) +
                          '/DISCARD/ : { *(.text) *(.bss) *(.reginfo) *(.MIPS.abiflags) *(.pdr) }\n}\n')
        result = subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
                                 '-o', 'layout.elf'], cwd=self.project, capture_output=True, text=True)
        return result, owners

    def test_real_linker_interleaving_including_eight_byte_boundary(self):
        result, owners = self.link_fixture()
        self.assertEqual(result.returncode, 0, result.stderr)
        address, data = load_section(self.project / 'layout.elf', '.game_data')
        self.assertEqual(address, 0x80001000)
        self.assertEqual(data, b''.join(bytes([index + 1]) * (owner['end'] - owner['address'])
                                        for index, owner in enumerate(owners)))

    def test_real_linker_rejects_owner_overflow(self):
        result, _ = self.link_fixture(overflow=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue('cannot move location counter backwards' in result.stderr or
                        'exceeds retail span' in result.stderr, result.stderr)


if __name__ == "__main__":
    unittest.main()
