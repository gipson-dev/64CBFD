import unittest

from tools.patch_generated_slice_ld import anchor_init_math_rodata


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


if __name__ == "__main__":
    unittest.main()
