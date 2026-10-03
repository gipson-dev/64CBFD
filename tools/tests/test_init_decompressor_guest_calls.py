import struct
import unittest

from tools.experiments.compile_init_decompressor import analyze_guest_calls


class InitDecompressorGuestCallTests(unittest.TestCase):
    @staticmethod
    def text(*words):
        return struct.pack(">%dI" % len(words), *words)

    def test_unnamed_helpers_are_included_in_nested_frame_bound(self):
        text = self.text(0x27BDFFF0, 0x0C000006, 0, 0x27BD0010, 0x03E00008, 0,
                         0x27BDFFE0, 0x0C00000C, 0, 0x27BD0020, 0x03E00008, 0,
                         0x03E00008, 0)
        units = analyze_guest_calls(text, {0: "root"}, {4: 24, 28: 48})
        self.assertEqual([(unit["name"], unit["frame_bytes"],
                           unit["direct_call_frame_bound"]) for unit in units],
                         [("root", 16, 48), ("local_0018", 32, 32), ("local_0030", 0, 0)])

    def test_unresolved_call_and_indirect_call_are_rejected(self):
        for word in (0x0C000000, 0x0320F809):
            with self.subTest(word=hex(word)), self.assertRaises(ValueError):
                analyze_guest_calls(self.text(word, 0), {0: "root"}, {})

    def test_recursive_call_graph_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "recursive"):
            analyze_guest_calls(self.text(0x0C000000, 0), {0: "root"}, {0: 0})

    def test_nonword_target_and_text_length_are_rejected(self):
        for text, targets in ((self.text(0x0C000000, 0), {0: 1}), (b"\0", {})):
            with self.subTest(text=text, targets=targets), self.assertRaises(ValueError):
                analyze_guest_calls(text, {0: "root"}, targets)

    def test_multiple_allocations_and_absolute_tail_transfer_are_rejected(self):
        for text in (self.text(0x27BDFFF0, 0x27BDFFE0), self.text(0x08000000, 0)):
            with self.subTest(text=text), self.assertRaises(ValueError):
                analyze_guest_calls(text, {0: "root"}, {})

    def test_word_store_forms_are_counted_from_opcodes(self):
        text = self.text(0xAC880000, 0xA8880000, 0xB8880003, 0xAC880004,
                         0x03E00008, 0)
        unit = analyze_guest_calls(text, {0: "root"}, {})[0]
        self.assertEqual(unit["word_store_forms"], {"sw": 2, "swl": 1, "swr": 1})


if __name__ == "__main__":
    unittest.main()
