import unittest
from pathlib import Path

from tools.experiments.compile_init_decompressor import retail_slot_ledger
from tools.tests import test_init_decompressor_contract as contract


class InitDecompressorSlotLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        contract.InitDecompressorContractTests.setUpClass()
        cls.source = Path(__file__).resolve().parents[2] / "conker/asm/init_5AB0.s"

    @staticmethod
    def measurements():
        sizes = {"init_decode_build": 413, "init_decode_compressed": 100,
                 "init_decode_stored": 55, "init_decode_fixed_tables": 82,
                 "init_decode_dynamic": 220, "init_decode_stream": 78,
                 "init_decode_core": 49}
        return [{"function": name, "slot_words": size,
                 "body_words": size if name != "init_decode_core" else 48}
                for name, size in sizes.items()]

    @staticmethod
    def jal_targets(name):
        return [((address + 4) & 0xF0000000) | ((word & 0x3FFFFFF) << 2)
                for address, word in contract.InitDecompressorContractTests.entries(name)
                if word >> 26 == 3]

    def test_dynamic_calls_builder_then_compressed_decoder(self):
        targets = self.jal_targets("func_10006424")
        self.assertEqual(targets.count(0x1000696C), 3)
        self.assertEqual(targets[-1], 0x10006E00)
        self.assertEqual(self.jal_targets("func_10006E00"), [])

    def test_fixed_wrapper_calls_compressed_decoder_and_forces_zero(self):
        self.assertEqual(self.jal_targets("func_1000692C"), [0x10006E00])
        self.assertEqual(contract.InitDecompressorContractTests.entries("func_1000692C")[-1][1],
                         0x24020000)

    def test_correct_roles_sizes_and_aggregate(self):
        report = retail_slot_ledger(self.measurements(), 4208, self.source)
        rows = {row["c_function"]: row for row in report["rows"]}
        dynamic = rows["init_decode_dynamic"]
        compressed = rows["init_decode_compressed"]
        self.assertEqual((dynamic["retail_entry"], dynamic["retail_slot_words"], dynamic["word_delta"]),
                         ("func_10006424", 257, -37))
        self.assertEqual((compressed["retail_entry"], compressed["retail_slot_words"], compressed["word_delta"]),
                         ("func_10006E00", 167, -67))
        self.assertEqual(rows["init_decode_build"]["word_delta"], 120)
        self.assertEqual((report["retail_words"], report["c_named_slot_words"],
                          report["c_helper_words"], report["c_total_words"], report["word_delta"]),
                         (996, 997, 55, 1052, 56))
        self.assertEqual(report["qualification"], "size-accounting-only")

    def test_fixed_alignment_and_merged_stream_are_in_slot_counts(self):
        report = retail_slot_ledger(self.measurements(), 4208, self.source)
        rows = {row["c_function"]: row for row in report["rows"]}
        self.assertEqual(rows["init_decode_stream"]["retail_slot_words"], 62)
        self.assertEqual(rows["init_decode_fixed_tables"]["retail_slot_words"], 77)
        self.assertEqual(len(contract.InitDecompressorContractTests.entries("func_1000709C")), 75)
        self.assertEqual([(row["role"], row["retail_slot_words"], row["distinct_c_entry"])
                          for row in report["retail_wrappers"]],
                         [("entry_wrapper", 7, False), ("fixed_decoder_wrapper", 16, False)])

    def test_duplicate_missing_and_unknown_functions_are_rejected(self):
        rows = self.measurements()
        for changed in (rows + [rows[0]], rows[1:],
                        rows + [{"function": "unknown", "slot_words": 1, "body_words": 1}]):
            with self.subTest(rows=changed), self.assertRaises(ValueError):
                retail_slot_ledger(changed, 4208, self.source)

    def test_invalid_text_and_body_sizes_are_rejected(self):
        for size in (-4, 4209, 4):
            with self.subTest(size=size), self.assertRaises(ValueError):
                retail_slot_ledger(self.measurements(), size, self.source)
        rows = self.measurements()
        rows[0]["body_words"] = rows[0]["slot_words"] + 1
        with self.assertRaises(ValueError):
            retail_slot_ledger(rows, 4208, self.source)


if __name__ == "__main__":
    unittest.main()
