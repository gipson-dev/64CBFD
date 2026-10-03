import json
import random
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.tests import test_init_decompressor_contract as contract
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture, GuestImage
from tools.tests.test_init_decompressor_tables import BuilderFixture


class InitDecompressorGuestInstructionTests(unittest.TestCase):
    @staticmethod
    def fixture():
        fixture = GuestBuilderFixture.__new__(GuestBuilderFixture)
        fixture.memory = {address: 0xA5 for address in range(0x1000, 0x1010)}
        fixture.registers = [0] * 32
        fixture.registers[29] = fixture.min_sp = 0x4000
        fixture.registers[31] = 0xDEAD0000
        fixture.readonly, fixture.allowed_writes = [], None
        fixture.reads, fixture.writes = [], []
        fixture.visits, fixture.capture, fixture.snapshots = {}, set(), {}
        return fixture

    def test_unaligned_store_pair_preserves_bytes_outside_each_offset(self):
        for offset in range(4):
            with self.subTest(offset=offset):
                fixture = self.fixture()
                fixture.registers[1:3] = [0x1004 + offset, 0x11223344]
                fixture.execute((42 << 26) | (1 << 21) | (2 << 16))
                fixture.execute((46 << 26) | (1 << 21) | (2 << 16) | 3)
                expected = bytearray(b"\xa5" * 16)
                expected[4 + offset:8 + offset] = b"\x11\x22\x33\x44"
                self.assertEqual(bytes(fixture.memory[address] for address in range(0x1000, 0x1010)),
                                 expected)

    def test_unsigned_immediate_comparison_sign_extends_then_compares_unsigned(self):
        for value, expected in ((0xFFFFFFFE, 1), (0xFFFFFFFF, 0)):
            fixture = self.fixture()
            fixture.registers[1] = value
            fixture.execute((11 << 26) | (1 << 21) | (2 << 16) | 0xFFFF)
            self.assertEqual(fixture.registers[2], expected)

    def test_unsigned_register_comparison_and_xor_immediate(self):
        fixture = self.fixture()
        fixture.registers[1:3] = [0xFFFFFFFF, 1]
        fixture.execute((1 << 21) | (2 << 16) | (3 << 11) | 43)
        self.assertEqual(fixture.registers[3], 0)
        fixture.execute((14 << 26) | (1 << 21) | (3 << 16) | 0xF0FF)
        self.assertEqual(fixture.registers[3], 0xFFFF0F00)

    def test_branch_likely_annuls_only_untaken_delay_store(self):
        for opcode in (4, 20):
            for taken in (False, True):
                with self.subTest(opcode=opcode, taken=taken):
                    fixture = self.fixture()
                    fixture.registers[1] = 0 if taken else 1
                    fixture.registers[2] = 0x1000
                    fixture.code = {0: (opcode << 26) | (1 << 21) | 3,
                                    4: (43 << 26) | (2 << 21),
                                    8: 0x03E00008, 12: 0, 16: 0x03E00008, 20: 0}
                    BuilderFixture.run(fixture, entry=0, budget=8)
                    self.assertEqual(fixture.get(0x1000, 4),
                                     0 if taken or opcode == 4 else 0xA5A5A5A5)

    def test_write_guards_and_truncated_image_are_rejected(self):
        fixture = self.fixture()
        fixture.readonly = [(0x1000, 0x1004)]
        with self.assertRaisesRegex(AssertionError, "read-only"):
            fixture.put(0x1003, 0, 2)
        fixture.readonly, fixture.allowed_writes = [], [(0x1004, 0x1008)]
        with self.assertRaisesRegex(AssertionError, "caller-owned"):
            fixture.put(0x1007, 0, 2)
        with self.assertRaises(ValueError):
            GuestImage(b"\x7fELF")


class InitDecompressorCompiledGuestBuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which("mips-linux-gnu-ld"):
            raise unittest.SkipTest("MIPS linker is unavailable")
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / "ido/ido5.3_recomp/cc").is_file():
            raise unittest.SkipTest("IDO compiler is unavailable")
        contract.InitDecompressorContractTests.setUpClass()
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.images = []
        cls.receipts = {}
        shapes = (("frame", ["--frame-backed"]),
                  ("aligned-end", ["--frame-backed", "--aligned-entry", "--bounded-builder-shifts",
                      "--no-unroll", "--bounded-length-scan", "--dynamic-cursor", "--builder-symbol-cursor"]),
                  ("packed-remaining", ["--frame-backed", "--packed-entry", "--bounded-builder-shifts",
                      "--no-unroll", "--bounded-length-scan", "--dynamic-cursor",
                      "--cache-builder", "counts-offsets", "--builder-symbol-cursor", "remaining"]))
        for label, flags in shapes:
            output = Path(cls.directory.name) / label
            result = subprocess.run([sys.executable,
                str(cls.root / "tools/experiments/compile_init_decompressor.py"),
                "--output", str(output), *flags], cwd=cls.root, capture_output=True, text=True, check=True)
            receipts = json.loads(result.stdout)
            if set(receipts) != {"o2g3", "o1"}:
                raise AssertionError("both guest compiler profiles are required")
            expected_text = {"frame": (5312, 5600), "aligned-end": (4192, 5408),
                             "packed-remaining": (4160, 5408)}[label]
            for profile, receipt in receipts.items():
                if receipt["text_bytes"] != expected_text[profile == "o1"]:
                    raise AssertionError("guest shape differs from the measured baseline")
                if (output / (profile + ".log")).read_text():
                    raise AssertionError("guest compile log is not empty")
                executable = output / (profile + ".elf")
                result = subprocess.run(["mips-linux-gnu-ld", "-Ttext", "0x10400000",
                    "-Tdata", "0x10500000", "-e", "init_decode_build", "-o", str(executable),
                    str(output / (profile + ".o"))], capture_output=True, text=True, check=True)
                if result.stdout or result.stderr:
                    raise AssertionError("guest link log is not empty")
                image = GuestImage(executable.read_bytes())
                sizes = image.symbols["init_decode_guest_sizes"]
                if bytes(image.memory[sizes + i] for i in range(8)) != b"\0\0\0\4\0\0\0\x28":
                    raise AssertionError("guest layout is not the frame-backed O32 layout")
                unit = next(unit for unit in receipt["call_graph"] if unit["name"] == "init_decode_build")
                cls.images.append((label, profile, image, unit["direct_call_frame_bound"]))
                cls.receipts[label, profile] = receipt

    def compare(self, lengths, bits=7, simple=None, allocated=0, bases=(), extras=()):
        reference = BuilderFixture(lengths, bits=bits, simple=simple, allocated=allocated,
                                   bases=bases, extras=extras)
        expected = reference.run()
        for label, profile, image, frame_bound in self.images:
            with self.subTest(shape=label, profile=profile, count=len(lengths), bits=bits):
                guest = GuestBuilderFixture(image, lengths, bits=bits, simple=simple,
                                            allocated=allocated, bases=bases, extras=extras)
                self.assertEqual(guest.run(), expected)
                self.assertEqual((guest.get(guest.ROOT, 2), guest.get(guest.BITS, 4),
                                  guest.get(guest.STATE + 28, 4)),
                                 (reference.get(reference.ROOT, 2), reference.get(reference.BITS, 4),
                                  reference.fprs[19]))
                self.assertEqual([guest.get(guest.STATE + offset, 4) for offset in range(0, 40, 4)
                                  if offset != 28],
                                 [0, 0, guest.WORKSPACE, 0, 0, 0, 0, guest.FRAME, guest.WORKSPACE])
                for address, value in reference.memory.items():
                    if reference.WORKSPACE <= address < reference.WORKSPACE + reference.fprs[19] * 4:
                        self.assertEqual(guest.memory[address], value, hex(address))
                self.assertEqual(bytes(guest.memory[guest.FRAME + i] for i in range(0x548)),
                                 bytes(reference.memory[reference.STACK + i] for i in range(0x548)))
                for register in (*range(16, 24), 28, 29, 30, 31):
                    self.assertEqual(guest.registers[register], guest.before[register])
                self.assertLessEqual(guest.STACK - guest.min_sp, frame_bound)
                workspace_end = guest.WORKSPACE + reference.fprs[19] * 4
                self.assertEqual(bytes(guest.memory[address] for address in
                                       range(workspace_end, workspace_end + 16)), b"\xa5" * 16)
                for first, last in ((guest.FRAME - 16, guest.FRAME),
                                    (guest.FRAME + 0xA44, guest.FRAME + 0xA88 + 16)):
                    self.assertEqual(bytes(guest.memory[address] for address in range(first, last)),
                                     b"\xa5" * (last - first))

    def test_small_empty_incomplete_and_oversubscribed_trees(self):
        for lengths, bits, allocated in (([], 7, 9), ([0] * 19, 7, 9), ([1, 1], 1, 0),
                ([2, 2], 2, 0), ([1], 7, 0), ([1, 2, 2], 1, 0), ([1, 2, 3, 3], 1, 11),
                ([1, 2, 3, 3], 2, 11), ([1, 1, 1], 1, 0), ([2] * 5, 2, 0)):
            self.compare(lengths, bits=bits, allocated=allocated)

    def test_full_capacity_and_explicit_base_extra_arguments(self):
        for lengths in ([0] * 288, [0] * 286 + [1, 1],
                        [8] * 144 + [9] * 112 + [7] * 24 + [8] * 8):
            self.compare(lengths, bits=9)
        self.compare([1, 2, 3, 3], bits=1, simple=2, bases=(32, 64), extras=(5, 7))

    def test_generated_complete_trees_and_depth_sixteen(self):
        for bits in (0, 1, 4, 7, 9):
            self.compare(list(range(1, 16)) + [16, 16], bits=bits)
        randomizer = random.Random(0x1000696C)
        for _ in range(12):
            lengths = [1, 1]
            for _ in range(randomizer.randrange(4, 60)):
                candidates = [index for index, length in enumerate(lengths) if length < 16]
                index = randomizer.choice(candidates)
                length = lengths.pop(index) + 1
                lengths.extend((length, length))
            randomizer.shuffle(lengths)
            self.compare(lengths, bits=randomizer.choice((0, 1, 4, 7, 9)))


if __name__ == "__main__":
    unittest.main()
