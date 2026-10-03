import hashlib
import struct
import unittest
import zlib
from pathlib import Path

from tools.tests import test_init_decompressor_contract as contract
from tools.tests.test_init_decompressor_streams import StreamFixture


ROM_SHA1 = "4cbadd3c4e0729dec46af64ad018050eada4f47a"
PAGE_COUNT = (0x1FA130 + 0xFFF) // 0x1000
INPUT = 0x80033330
WORKSPACE = 0x800340E8
CALLER_SP = 0x80032B18 - 0x80 - 0x88


def retail_pages(rom):
    if hashlib.sha1(rom).hexdigest() != ROM_SHA1:
        raise ValueError("Expected the original US retail ROM")
    base = 0x42450
    offsets = [(struct.unpack_from(">I", rom, base + 4 + i * 4)[0]
                ^ 0x8039CCCA) + base for i in range(PAGE_COUNT + 1)]
    if any(a >= b for a, b in zip(offsets, offsets[1:])):
        raise ValueError("Non-increasing retail page offsets")
    pages = []
    for index, (start, end) in enumerate(zip(offsets, offsets[1:])):
        chunk = rom[start:end]
        size = struct.unpack_from(">I", chunk)[0]
        decoder = zlib.decompressobj(-15)
        output = decoder.decompress(chunk[4:]) + decoder.flush()
        if not decoder.eof or len(output) != size:
            raise ValueError("Invalid retail page length or stream")
        pages.append((index, start, end, chunk, output))
    return pages


class InitDecompressorRetailPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract.InitDecompressorContractTests.setUpClass.__func__(
            contract.InitDecompressorContractTests)
        root = Path(__file__).resolve().parents[2]
        rom_path = root / "baserom.us.z64"
        image_path = root / "conker/conker.us.bin"
        if not rom_path.exists() or not image_path.exists():
            raise unittest.SkipTest("Local retail ROM and decompressed image required")
        cls.rom = rom_path.read_bytes()
        cls.image = image_path.read_bytes()
        cls.pages = retail_pages(cls.rom)

    def test_all_page_outputs_and_dma_separation(self):
        self.assertEqual(len(self.pages), 507)
        maximum = 0
        for index, start, end, chunk, output in self.pages:
            with self.subTest(page=index):
                offset = 0x2D4B0 + index * 0x1000
                self.assertEqual(output, self.image[offset:offset + len(output)])
                dma_size = (end - start + 15) & ~15
                maximum = max(maximum, dma_size)
                self.assertLessEqual(INPUT + dma_size, WORKSPACE)
        self.assertEqual(maximum, 3072)
        self.assertEqual(WORKSPACE - INPUT - maximum, 440)
        self.assertEqual(len(self.pages[-1][4]), 304)

    def test_wrong_rom_rejected(self):
        with self.assertRaisesRegex(ValueError, "original US"):
            retail_pages(b"not a retail ROM")

    def test_retained_core_at_exception_addresses(self):
        # Bootstrap fixed tables independently, then place only the core call
        # at the handler's addresses; CP0, DMA and full FPR context are excluded.
        largest = max(self.pages, key=lambda page: page[2] - page[1])[0]
        for index in (0, largest, PAGE_COUNT - 1):
            with self.subTest(page=index):
                _, start, end, chunk, expected = self.pages[index]
                fixture = StreamFixture(chunk)
                fixture.INPUT, fixture.OUTPUT = INPUT, 0x80050000
                fixture.WORKSPACE = WORKSPACE
                fixture.registers[29] = CALLER_SP
                for address in range(CALLER_SP - 0xA88, CALLER_SP):
                    fixture.memory[address] = 0xA5
                dma_size = (end - start + 15) & ~15
                fixture.memory.update({INPUT + i: byte for i, byte in
                                       enumerate(self.rom[start:start + dma_size])})
                fixture.reads, fixture.writes = [], []
                self.assertEqual(fixture.core(wrapped=False), len(expected))
                self.assertEqual(fixture.output(), expected)
                self.assertEqual(fixture.registers[29], CALLER_SP)
                self.assertFalse(any(INPUT <= address < INPUT + dma_size
                                     for address, _ in fixture.writes))
                scratch = [(address, size) for address, size in fixture.writes
                           if WORKSPACE <= address < fixture.OUTPUT]
                self.assertEqual(bool(scratch), index != PAGE_COUNT - 1)
                span = max((a + n - WORKSPACE for a, n in scratch), default=0)
                self.assertEqual(span, {0: 3416, 169: 3276, 506: 0}[index])
                # Observed writes are not an inferred allocation capacity.
                if scratch:
                    self.assertLess(max(a + n for a, n in scratch), 0x800354F8)


if __name__ == "__main__":
    unittest.main()
