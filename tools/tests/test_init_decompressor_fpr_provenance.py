import json
import subprocess
import sys
import unittest
from pathlib import Path

from tools.tests import test_init_decompressor_decoder as decoder
from tools.tests import test_init_decompressor_exception as exception
from tools.tests import test_init_decompressor_guest_adapter as adapter
from tools.tests import test_init_decompressor_streams as streams
from tools.tests import test_init_decompressor_tables as tables
from tools.tests.init_decompressor_guest_oracle import GuestImage


class TrackingCode(dict):
    def __init__(self, fixture, code):
        super().__init__(code)
        self.fixture = fixture

    def __getitem__(self, pc):
        self.fixture.instruction_pc = pc
        return super().__getitem__(pc)


class FprProvenanceFixture(exception.ExceptionCoreFixture):
    def __init__(self, chunk, status):
        super().__init__(chunk, status)
        self.transfers, self.code_returns, self.length_completions = [], [], []
        self.capture.add(0x100062F0)
        self.code = TrackingCode(self, self.code)
        self.memory.update((self.WORKSPACE + i, 0xA5) for i in range(4096))

    def execute(self, word):
        if self.context_enabled and hasattr(self, "transfers"):
            pc = self.instruction_pc
            if word >> 26 == 17 and (word >> 21) & 31 == 4:
                source, destination = word >> 16 & 31, word >> 11 & 31
                self.transfers.append({"pc": pc, "source": source, "fpr": destination,
                                       "value": self.registers[source],
                                       "gprs": tuple(self.registers)})
            frame = self.registers[29]
            if pc == 0x10006548:
                self.code_returns.append({"bits": self.get(frame + 0xA3C, 4),
                                          "root": self.get(frame + 0xA38, 2)})
            if pc == 0x1000675C:
                total = self.registers[20]
                self.length_completions.append({"total": total,
                    "last": self.get(frame + 0x548 + (total - 1) * 4, 4),
                    "entry_index": self.registers[16], "symbol": self.registers[17],
                    "input": self.registers[23], "bits": self.registers[30],
                    "reservoir": self.registers[28]})
        super().execute(word)


class InitDecompressorFprProvenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        adapter.InitDecompressorCompiledGuestAdapterTests.setUpClass.__func__(cls)
        directory = Path(cls.directory.name)
        cls.seeded_images, cls.seeded_receipts = [], {}
        for label, flags in cls.shape_flags.items():
            output = directory / (label + "-seeded")
            result = subprocess.run([sys.executable,
                str(cls.root / "tools/experiments/compile_init_decompressor.py"),
                "--output", str(output), *flags, "--seed-distance-root"],
                capture_output=True, text=True, check=True)
            receipts = json.loads(result.stdout)
            if set(receipts) != {"o2g3", "o1"}:
                raise AssertionError("both seeded compiler profiles are required")
            for profile, receipt in receipts.items():
                if (output / (profile + ".log")).read_text():
                    raise AssertionError("seeded compiler log is not empty")
                executable = output / (profile + "-adapter.elf")
                result = subprocess.run(["mips-linux-gnu-ld", "-Ttext", "0x10400000",
                    "-Tdata", "0x10500000", "-e", "init_decode_build", "-o", str(executable),
                    str(output / (profile + ".o")), str(directory / "adapter.o")],
                    capture_output=True, text=True, check=True)
                if result.stdout or result.stderr:
                    raise AssertionError("seeded link log is not empty")
                cls.seeded_images.append((label, profile, GuestImage(executable.read_bytes())))
                cls.seeded_receipts[label, profile] = receipt

    @staticmethod
    def incomplete_literal_tree(repeats=False, sparse=False):
        bits = streams.BitStream()
        bits.emit(5, 3)
        bits.emit(0, 5)
        bits.emit(0, 5)
        bits.emit(14, 4)
        order = decoder.reference_data("2C120.rodata.s", "D_8002C15C")
        lengths = [0] * 19
        if sparse:
            lengths[0], lengths[2] = 1, 1
        else:
            lengths[9], lengths[16 if repeats else 18] = 1, 1
        for symbol in order[:18]:
            bits.emit(lengths[symbol], 3)
        codes = {symbol: (code, width) for symbol, width, code in
                 tables.InitDecompressorTableTests.canonical(lengths)}
        # Dense width-nine and sparse width-two trees both gate on retail's
        # incomplete-tree result before distance construction.
        if sparse:
            for _ in range(65):
                bits.emit(*codes[0])
            bits.emit(*codes[2])
            for _ in range(192):
                bits.emit(*codes[0])
        elif repeats:
            bits.emit(*codes[9])
            for extra in (*([3] * 42), 2):
                bits.emit(*codes[16])
                bits.emit(extra, 2)
        else:
            for _ in range(258):
                bits.emit(*codes[9])
        return bits.data()

    @staticmethod
    def after_fixed(dynamic):
        raw = decoder.InitDecompressorDecoderTests.encoded(b"BC")
        length = 3 + sum(decoder.InitDecompressorDecoderTests.codes[symbol][1]
                         for symbol in (*b"BC", 256))
        bits = streams.BitStream()
        bits.bits = [(byte >> i) & 1 for byte in raw for i in range(8)][:length]
        bits.bits[0] = 0
        bits.emit(0, 3)
        while len(bits.bits) % 8:
            bits.emit(0, 1)
        bits.emit(0, 16)
        bits.emit(0xFFFF, 16)
        bits.bits.extend((byte >> i) & 1 for byte in dynamic for i in range(8))
        return bits.data()

    def run_reference(self, raw, cu1=True):
        fixture = FprProvenanceFixture(b"\x11\x72" + raw,
            exception.SR_FR | (exception.SR_CU1 if cu1 else 0) | 0xFF01)
        fixture.context()
        return fixture

    def assert_builder_saves(self, fixture, expected_roles):
        saves = [row for row in fixture.transfers if 2 <= row["fpr"] <= 11]
        self.assertEqual(len(saves), len(expected_roles) * 10)
        groups = [saves[i:i + 10] for i in range(0, len(saves), 10)]
        for group, role in zip(groups, expected_roles):
            self.assertEqual([row["fpr"] for row in group], list(range(2, 12)))
            self.assertEqual([row["source"] for row in group], [*range(16, 24), 30, 28])
            self.assertEqual([row["pc"] for row in group], list(range(0x10006970, 0x10006998, 4)))
            self.assertEqual(group[0]["gprs"][31], role)
            for row in group:
                self.assertEqual(row["value"], row["gprs"][row["source"]])
        return groups

    def test_dynamic_builder_values_map_to_semantic_boundaries(self):
        raw = streams.InitDecompressorStreamTests().dynamic()
        for cu1 in (False, True):
            fixture = self.run_reference(raw, cu1)
            groups = self.assert_builder_saves(fixture, (0x10006548, 0x1000679C, 0x100067E0))
            count_writes = [row for row in fixture.transfers if row["fpr"] in (0, 1)]
            self.assertEqual([(row["pc"], row["fpr"], row["value"]) for row in count_writes],
                [(0x10006520, 0, 257), (0x10006524, 1, 1),
                 (0x1000676C, 0, 257), (0x10006770, 1, 1)])
            self.assertEqual(groups[0][0]["value"], fixture.initial_registers[16])
            self.assertEqual(groups[0][1]["value"], 19)
            code, lengths = fixture.code_returns[0], fixture.length_completions[0]
            for group in groups[1:]:
                self.assertEqual([row["value"] for row in group],
                    [lengths["entry_index"], lengths["symbol"], lengths["last"],
                     (1 << code["bits"]) - 1, lengths["total"], code["root"],
                     fixture.WORKSPACE, lengths["input"], lengths["bits"], lengths["reservoir"]])
            if cu1:
                for row in groups[-1]:
                    self.assertEqual(fixture.fpr_value(row["fpr"]), (row["value"], 0xFFFFFFFF))
                self.assertEqual(fixture.fpr_value(1), (1, 0xFFFFFFFF))
            else:
                self.assertEqual([fixture.fpr_value(i) for i in range(32)], fixture.initial_fprs)

    def test_fixed_history_changes_the_builder_s0_snapshot(self):
        raw = self.after_fixed(streams.InitDecompressorStreamTests().dynamic())
        fixture = self.run_reference(raw)
        groups = self.assert_builder_saves(fixture, (0x10006548, 0x1000679C, 0x100067E0))
        self.assertGreater(fixture.visits.get(0x10006E00, 0), 1)
        self.assertEqual(groups[0][0]["value"], 0x8002C0C0)
        self.assertEqual([group[0]["value"] for group in groups[1:]],
                         [fixture.length_completions[0]["entry_index"]] * 2)
        self.assertNotEqual(groups[0][0]["value"], fixture.initial_registers[16])
        self.assertEqual(fixture.fpr_value(2),
                         (fixture.length_completions[0]["entry_index"], 0xFFFFFFFF))

    def test_non_dynamic_blocks_do_not_touch_builder_scratch_fprs(self):
        raws = (b"\x01\x02\0\xfd\xffXY",
                decoder.InitDecompressorDecoderTests.encoded(b"BC"), b"\x07")
        for raw in raws:
            fixture = self.run_reference(raw)
            self.assertEqual([row for row in fixture.transfers if row["fpr"] < 12], [])
            for i in range(1, 12):
                self.assertEqual(fixture.fpr_value(i), fixture.initial_fprs[i])

    def test_repeat_overflow_leaves_only_the_code_builder_snapshot(self):
        fixture = self.run_reference(streams.InitDecompressorStreamTests().dynamic(overflow=True))
        groups = self.assert_builder_saves(fixture, (0x10006548,))
        self.assertEqual(fixture.length_completions, [])
        self.assertEqual([row["pc"] for row in fixture.transfers if row["fpr"] in (0, 1)],
                         [0x10006520, 0x10006524])
        for row in groups[0]:
            self.assertEqual(fixture.fpr_value(row["fpr"]), (row["value"], 0xFFFFFFFF))

    def test_literal_failure_root_seed_fix_matches_all_six_images(self):
        for repeats in (False, True):
            failed = self.incomplete_literal_tree(repeats)
            for raw in (failed, self.after_fixed(failed)):
                self.compare_literal_failure(raw, 2 if repeats else 1)

    def compare_literal_failure(self, raw, seed):
        reference = self.run_reference(raw, cu1=False)
        self.assert_builder_saves(reference, (0x10006548, 0x1000679C))
        self.assertEqual(reference.snapshots[0x10005F34][0][2], 0)
        frame = exception.CALLER_SP - 0xA88
        self.assertEqual(reference.get(frame + 0xA3A, 2), seed)
        for label, profile, image in self.adapter_images:
            with self.subTest(shape=label, profile=profile, seed=seed):
                guest = adapter.GuestExceptionFixture(image, b"\x11\x72" + raw,
                                                       exception.SR_FR | 0xFF01)
                guest.context()
                self.assertEqual(guest.snapshots[0x10005F34][0][2], 0)
                self.assertEqual(guest.registers, reference.registers)
                self.assertEqual([guest.fpr_value(i) for i in range(32)],
                                 [reference.fpr_value(i) for i in range(32)])
                different = [i for i in range(0xA44)
                             if guest.memory[frame + i] != reference.memory[frame + i]]
                self.assertEqual(different, [0xA3A, 0xA3B])
                self.assertEqual(guest.get(frame + 0xA3A, 2), 0xA5A5)
                print("literal failure root-seed gap: %s/%s retail=0x%04X C=0xA5A5" %
                      (label, profile, seed), flush=True)
        for label, profile, image in self.seeded_images:
            with self.subTest(shape=label, profile=profile, corrected_seed=seed):
                guest = adapter.GuestExceptionFixture(image, b"\x11\x72" + raw,
                                                       exception.SR_FR | 0xFF01)
                guest.context()
                self.assertEqual(guest.snapshots[0x10005F34][0][2], 0)
                self.assertEqual(guest.get(frame + 0xA3A, 2), seed)
                self.assertEqual(bytes(guest.memory[frame + i] for i in range(0xA44)),
                                 bytes(reference.memory[frame + i] for i in range(0xA44)))
                self.assertEqual(guest.registers, reference.registers)
                self.assertEqual([guest.fpr_value(i) for i in range(32)],
                                 [reference.fpr_value(i) for i in range(32)])
                core_registers, _ = reference.snapshots[0x100062F0]
                _, result_fprs = reference.snapshots[0x10005F34]
                self.assertEqual([guest.get(guest.adapter_state + i * 4, 4) for i in range(10)],
                    [core_registers[23], guest.OUTPUT, guest.WORKSPACE,
                     core_registers[28], core_registers[30], result_fprs[17], result_fprs[18],
                     result_fprs[19], frame, guest.WORKSPACE])
                changed = {current for address, size in (*reference.writes, *guest.writes)
                           if guest.WORKSPACE <= address < guest.WORKSPACE + 4096
                           or guest.OUTPUT <= address < guest.OUTPUT + guest.OUTPUT_CAPACITY
                           for current in range(address, address + size)}
                for current in changed:
                    self.assertEqual(guest.memory[current], reference.memory.get(current, 0xA5), hex(current))
                self.assertEqual(guest.status_writes, reference.status_writes)
                self.assertGreater(guest.visits.get(image.symbols["init_decode_core"], 0), 0)

    def test_sparse_tree_signed_stale_sorted_symbols_match_retail(self):
        raw = self.incomplete_literal_tree(sparse=True)
        reference = self.run_reference(raw, cu1=False)
        self.assert_builder_saves(reference, (0x10006548, 0x1000679C))
        self.assertEqual(reference.snapshots[0x10005F34][0][2], 0)
        self.assertEqual(reference.get(exception.CALLER_SP - 0xA88 + 0x84 + 8, 4), 0xA5A5A5A5)
        allocated = reference.snapshots[0x10005F34][1][19]
        self.assertTrue(any(reference.get(address, 1) == 16 and
                            reference.get(address + 2, 2) == 0xA5A5
                            for address in range(reference.WORKSPACE,
                                                 reference.WORKSPACE + allocated * 4, 4)))
        self.compare_literal_failure(raw, 1)

    compare = adapter.InitDecompressorCompiledGuestAdapterTests.compare

    def test_seeded_images_preserve_adapter_vectors_and_retail_pages(self):
        self.adapter_images = self.seeded_images
        self.receipts = self.seeded_receipts
        adapter.InitDecompressorCompiledGuestAdapterTests.test_cu1_clear_success_and_failure_contexts(self)
        adapter.InitDecompressorCompiledGuestAdapterTests.test_representative_retail_pages_through_context_adapter(self)

    def test_root_seed_requires_frame_backed_layout(self):
        output = Path(self.directory.name) / "rejected-layout"
        result = subprocess.run([sys.executable,
            str(self.root / "tools/experiments/compile_init_decompressor.py"),
            "--output", str(output), "--seed-distance-root"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--seed-distance-root requires --frame-backed", result.stderr)
        self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
