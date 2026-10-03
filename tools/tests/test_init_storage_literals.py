import hashlib
import struct
import unittest

from tools.experiments import audit_init_storage_literals as literals
from tools.tests.init_decompressor_guest_oracle import GuestBuilderFixture


class InitStorageLiteralTests(unittest.TestCase):
    def scan(self, *words, low=0x80031AE0, high=0x80035504):
        return literals.literal_pairs(b"".join(struct.pack(">I", word) for word in words),
                                      0x10001000, low, high)

    def test_signed_low_half_and_memory_direction(self):
        rows = self.scan(0x3C088004, 0x8D093400, 0x3C088003, 0xAD093400)
        self.assertEqual([(row["kind"], row["address"]) for row in rows],
                         [("store", 0x80033400)])
        rows = self.scan(0x3C088004, 0x8D098000, low=0x80037FFF, high=0x80038004)
        self.assertEqual(rows[0]["address"], 0x80038000)
        self.assertEqual(rows[0]["kind"], "load")

    def test_addiu_and_ori_materializers_allow_different_destination(self):
        rows = self.scan(0x3C088003, 0x25043400, 0x3C088003, 0x35043400)
        self.assertEqual([row["address"] for row in rows], [0x80033400] * 2)
        self.assertEqual([row["kind"] for row in rows], ["address"] * 2)

    def test_boundary_crossing_and_exclusive_high(self):
        rows = self.scan(0x3C088003, 0xAD091ADC, 0x3C088003, 0xAD091ADC,
                         low=0x80031ADE, high=0x80031AE0)
        self.assertEqual(len(rows), 2)
        self.assertEqual(self.scan(0x3C088003, 0xAD095504), [])

    def test_nonadjacent_mismatched_and_zero_register_pairs_are_not_claimed(self):
        self.assertEqual(self.scan(0x3C088003, 0, 0x25083400), [])
        self.assertEqual(self.scan(0x3C088003, 0x25293400), [])
        self.assertEqual(self.scan(0x3C008003, 0x24083400), [])
        self.assertEqual(self.scan(0x3C088003, 0x25003400), [])

    def test_bad_input_and_wrong_rom_rejected(self):
        with self.assertRaises(ValueError):
            literals.literal_pairs(b"x", 0)
        with self.assertRaises(ValueError):
            literals.literal_pairs(b"", 1)
        with self.assertRaises(ValueError):
            literals.audit(b"not a retail ROM")

    def test_retail_reference_census_and_expected_decoder_materializers(self):
        path = literals.ROOT / "baserom.us.z64"
        if not path.is_file():
            self.skipTest("local retail ROM required")
        report = literals.audit(path.read_bytes())
        rows = report["references"]
        addresses = {(row["use_pc"], row["address"]) for row in rows}
        self.assertIn((0x10005E20, 0x80032B18), addresses)
        self.assertIn((0x10005F28, 0x800340E8), addresses)
        self.assertIn((0x10006014, 0x80032B18), addresses)
        print("storage literal census: " + ", ".join(
            "%s=%d" % (name, sum(row["section"] == name for row in rows))
            for name in ("Init", "Game", "Debugger")))

    def test_startup_clear_call_covers_enclosing_bss_not_individual_reservations(self):
        path = literals.ROOT / "baserom.us.z64"
        if not path.is_file():
            self.skipTest("local retail ROM required")
        data = path.read_bytes()
        self.assertEqual(hashlib.sha1(data).hexdigest(), literals.ROM_SHA1)
        words = [word for (word,) in struct.iter_unpack(">I", data[0x1050:0x1070])]
        self.assertEqual(words, [0x27BDFFE0, 0x3C048003, 0x2484D4B0, 0xAFBF001C,
                                 0x3C0E8004, 0x25CE3B40, 0x0C0089BC, 0x01C42823])
        fixture = GuestBuilderFixture.__new__(GuestBuilderFixture)
        fixture.registers, fixture.memory = [0] * 32, {}
        fixture.registers[29] = fixture.min_sp = 0x10000
        fixture.readonly, fixture.allowed_writes = [], None
        fixture.writes, fixture.reads = [], []
        for word in (*words[:6], words[7]):
            fixture.execute(word)
        self.assertEqual(fixture.registers[4:6], [0x8002D4B0, 0x16690])
        self.assertEqual(fixture.registers[4] + fixture.registers[5], 0x80043B40)
        self.assertLessEqual(fixture.registers[4], literals.LOW)
        self.assertGreaterEqual(fixture.registers[4] + fixture.registers[5], literals.HIGH)


class InitBlockLocalStorageTests(unittest.TestCase):
    def scan(self, *words):
        return literals.block_local_literals(b"".join(struct.pack(">I", word) for word in words),
                                            0x10001000)

    def test_scheduled_pair_copy_and_indirect_store_have_definition_chain(self):
        rows = self.scan(0x3C088003, 0x240B0007, 0x25083400,
                         0x01004825, 0xAD2B0004)
        store = rows[-1]
        self.assertEqual((store["kind"], store["address"]), ("store", 0x80033404))
        self.assertEqual(store["definition_pcs"], [0x10001000, 0x10001008, 0x1000100C])

    def test_loaded_pointer_is_unknown_and_does_not_create_following_store(self):
        rows = self.scan(0x3C088003, 0x25083400, 0x8D080000, 0xAD000004)
        self.assertEqual([(row["kind"], row["address"]) for row in rows],
                         [("address", 0x80033400), ("load", 0x80033400)])

    def test_call_keeps_delay_slot_candidate_but_clears_following_values(self):
        rows = self.scan(0x3C088003, 0x25083400, 0x0C004000, 0xAD090000, 0xAD090004)
        self.assertEqual([row["use_pc"] for row in rows if row["kind"] == "store"],
                         [0x1000100C])

    def test_branch_target_discards_incoming_constants(self):
        rows = self.scan(0x3C088003, 0x25083400, 0x10000002, 0,
                         0x3C088003, 0xAD093400)
        self.assertFalse(any(row["kind"] == "store" for row in rows))

    def test_unknown_opcode_discards_all_constants(self):
        rows = self.scan(0x3C088003, 0x25083400, 0x42000018, 0xAD090000)
        self.assertFalse(any(row["kind"] == "store" for row in rows))

    def test_addi_overflow_does_not_propagate_a_trapping_result(self):
        rows = self.scan(0x3C087FFF, 0x3508FFFF, 0x21083500, 0xAD090000)
        self.assertEqual(rows, [])

    def test_retail_scheduled_publications_and_context_stores_are_found(self):
        path = literals.ROOT / "baserom.us.z64"
        if not path.is_file():
            self.skipTest("local retail ROM required")
        report = literals.audit(path.read_bytes(), block_local=True)
        rows = report["block_local_references"]
        stores = {(row["use_pc"], row["address"]) for row in rows if row["kind"] == "store"}
        self.assertIn((0x10001350, 0x800354F8), stores)
        self.assertIn((0x1000137C, 0x800354FC), stores)
        self.assertIn((0x10005E24, 0x80032B18), stores)
        self.assertIn((0x10005E30, 0x80032A98), stores)
        self.assertEqual(report["references"], literals.audit(path.read_bytes())["references"])
        print("block-local storage census: " + ", ".join(
            "%s=%d" % (name, sum(row["section"] == name for row in rows))
            for name in ("Init", "Game", "Debugger")))


if __name__ == "__main__":
    unittest.main()
