"""Guarded word patches can move relocations with scheduled instructions."""

import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pad_c_object import emit_padded_assembly
from pad_generated_object import parse_object


class WordPatchRelocationTests(unittest.TestCase):
    def test_low_relocation_moves_with_scheduled_word(self):
        if not shutil.which("mips-linux-gnu-as"):
            self.skipTest("mips-linux-gnu-as required")

        with tempfile.TemporaryDirectory() as temp_name:
            work = Path(temp_name)
            (work / "compact.s").write_text(
                """
.section .text,"ax"
.set noreorder
.globl sample
.type sample,@function
sample:
lui $t4,%hi(target)
addiu $t4,$t4,%lo(target)
move $a3,$zero
jr $ra
nop
.size sample,.-sample
"""
            )
            (work / "layout.csv").write_text(
                "version,section,filename,function,address,end\n"
                "us,debugger,fixture,sample,0x16000000,0x16000014\n"
            )
            (work / "patches.csv").write_text(
                "filename,function,offset,expected,replacement,"
                "expected_relocations,replacement_relocations,note\n"
                "fixture,sample,0x4,0x258C0000,0x00003825,"
                "R_MIPS_LO16:target,-,move low load later\n"
                "fixture,sample,0x8,0x00003825,0x258C0000,-,"
                "R_MIPS_LO16:target,move low relocation later\n"
            )

            subprocess.run(
                [
                    "mips-linux-gnu-as",
                    "-EB",
                    "-march=vr4300",
                    "-o",
                    "compact.o",
                    "compact.s",
                ],
                cwd=work,
                check=True,
                capture_output=True,
            )
            padded = emit_padded_assembly(
                work / "compact.o",
                work / "layout.csv",
                "fixture",
                word_patches_path=work / "patches.csv",
            )
            (work / "padded.s").write_text(padded)
            subprocess.run(
                [
                    "mips-linux-gnu-as",
                    "-EB",
                    "-march=vr4300",
                    "-o",
                    "padded.o",
                    "padded.s",
                ],
                cwd=work,
                check=True,
                capture_output=True,
            )

            text, functions, relocations = parse_object(work / "padded.o")
            start = functions["sample"]["value"]
            self.assertEqual(struct.unpack_from(">I", text, start + 4)[0], 0x00003825)
            self.assertEqual(struct.unpack_from(">I", text, start + 8)[0], 0x258C0000)
            self.assertNotIn(start + 4, relocations)
            self.assertEqual(
                relocations[start + 8], [("R_MIPS_LO16", "target")]
            )


if __name__ == "__main__":
    unittest.main()
