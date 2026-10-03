import struct
import subprocess
import unittest
from pathlib import Path

from tools.tests import test_init_decompressor_guest_builder as builder
from tools.tests import test_init_decompressor_contract as contract
from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_guest_fpr_shadow as shadow
from tools.tests.init_decompressor_guest_oracle import GuestImage


class InitDecompressorContextLayoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        builder.InitDecompressorCompiledGuestBuilderTests.setUpClass.__func__(cls)

    def test_guest_thread_layout_and_neighbor_boundary(self):
        directory = Path(self.directory.name)
        for profile, flags in (("o2g3", ["-O2", "-g3"]), ("o1", ["-O1"])):
            with self.subTest(profile=profile):
                obj = directory / (profile + "-context.o")
                result = subprocess.run([str(self.root / "ido/ido5.3_recomp/cc"),
                    "-c", "-32", "-G", "0", "-Xfullwarn", "-Xcpluscomm", "-signed",
                    "-nostdinc", "-non_shared", "-Wab,-r4300_mul", "-mips2", "-o32",
                    "-D_LANGUAGE_C", "-D_FINALROM", "-DF3DEX_GBI_2", "-D_MIPS_SZLONG=32",
                    "-woff", "649,838", "-Iinclude/2.0L", "-Iinclude/libc", *flags,
                    "-o", str(obj), str(self.root / "tools/experiments/init_decompressor_context_layout.c")],
                    cwd=self.root / "conker", capture_output=True, text=True, check=True)
                self.assertEqual(result.stdout + result.stderr, "")
                executable = directory / (profile + "-context.elf")
                result = subprocess.run(["mips-linux-gnu-ld", "-Ttext", "0x10400000",
                    "-Tdata", "0x10500000", "-e", "init_decode_build", "-o", str(executable),
                    str(directory / "frame" / (profile + ".o")), str(obj)],
                    capture_output=True, text=True, check=True)
                self.assertEqual(result.stdout + result.stderr, "")
                image = GuestImage(executable.read_bytes())
                address = image.symbols["init_decode_context_layout"]
                values = struct.unpack(">10I", bytes(image.memory[address + i] for i in range(40)))
                self.assertEqual(values, (4, 4, 0x190, 0x1B0, 0x20, 0xF0, 0x130, 8, 0x230, 0x130))
                self.assertEqual(0x80031AE0 + values[3], 0x80031C90)
                self.assertEqual(shadow.ShadowExceptionFixture.NEIGHBOR_END,
                                 0x80031AE0 + values[8])
                print("guest context layout: %s SDK_thread=%d retail_storage=%d neighbor_end=0x80031D10" %
                      (profile, values[3], values[8]), flush=True)

    def test_retail_context_stack_instructions_and_symbol_addresses(self):
        words = dict(contract.InitDecompressorContractTests.entries("func_10005C2C"))
        for address, expected in ((0x10005E1C, 0x3C048003),
                                  (0x10005E20, 0x24842B18),
                                  (0x10005E24, 0xAC9D0000),
                                  (0x10005E28, 0x249D0000),
                                  (0x10005E2C, 0x27BDFF80),
                                  (0x10005EB4, 0x27BDFF78)):
            self.assertEqual(words[address], expected)
        self.assertEqual(exception.CALLER_SP, 0x80032B18 - 0x80 - 0x88)
        symbols = (self.root / "conker/undefined_syms_auto.txt").read_text()
        self.assertIn("D_80031AE0 = 0x80031AE0;", symbols)
        self.assertIn("D_800318B0 = 0x800318B0;", symbols)
        self.assertIn("D_80032B18 = 0x80032B18;", symbols)
        self.assertEqual(0x80031AE0 - 0x800318B0, 0x230)
        self.assertEqual(0x80032B18 - shadow.ShadowExceptionFixture.NEIGHBOR_END, 3592)

    def test_retail_fr1_saver_and_restore_require_32_fpr_slots(self):
        saves = dict(contract.InitDecompressorContractTests.entries("func_100071D0"))
        restores = dict(contract.InitDecompressorContractTests.entries("func_10007A38"))
        rom_path = contract.InitDecompressorContractTests.project / "conker.us.bin"
        rom = rom_path.read_bytes() if rom_path.exists() else None
        for index in range(32):
            offset = 0x130 + index * 8
            self.assertEqual(saves[0x1000736C + index * 4],
                             (61 << 26) | (26 << 21) | (index << 16) | offset)
            self.assertEqual(restores[0x10007B2C + index * 4],
                             (53 << 26) | (26 << 21) | (index << 16) | offset)
            if rom is not None:
                for address, words in ((0x1000736C + index * 4, saves),
                                       (0x10007B2C + index * 4, restores)):
                    self.assertEqual(struct.unpack_from(">I", rom, address - 0x10000000)[0],
                                     words[address])
        self.assertEqual(0x130 + 32 * 8, 0x230)
        self.assertEqual(shadow.ShadowExceptionFixture.NEIGHBOR_END, 0x80031AE0 + 0x230)


if __name__ == "__main__":
    unittest.main()
