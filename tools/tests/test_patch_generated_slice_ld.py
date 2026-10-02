import unittest

from tools.patch_generated_slice_ld import (
    anchor_init_math_rodata,
    restore_init_audio_data_order,
)


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


if __name__ == "__main__":
    unittest.main()
