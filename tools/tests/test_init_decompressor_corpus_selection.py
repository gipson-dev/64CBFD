import contextlib
import io
import os
from types import SimpleNamespace
import unittest
from unittest import mock

from tools.tests import test_init_decompressor_shadow_corpus as corpus
from tools.tests import test_init_decompressor_guest_fpr_shadow as shadow


class InitDecompressorCorpusSelectionTests(unittest.TestCase):
    def test_setup_defaults_and_invalid_modes_before_compilation(self):
        compiled = []

        def compile_stub(cls):
            compiled.append(cls)
            cls.adapter_images = [("fake", str(i), None) for i in range(6)]

        selected = type("SelectedCorpus", (corpus.InitDecompressorShadowCorpusTests,), {})
        with mock.patch.object(shadow.InitDecompressorGuestFprShadowTests,
                               "setUpClass", classmethod(compile_stub)):
            with mock.patch.dict(os.environ, {}, clear=True):
                selected.setUpClass()
                self.assertEqual(selected.corpus_context, "generic")
                self.assertEqual(selected.corpus_statuses, [("set", 0x2400FF01)])
            with mock.patch.dict(os.environ, {"CONKER_INIT_SHADOW_CORPUS_CU1": "both",
                    "CONKER_INIT_SHADOW_CORPUS_CONTEXT": "exception-masked"}, clear=True):
                selected.setUpClass()
                self.assertEqual(selected.corpus_statuses,
                                 [("clear", 0x0400FF00), ("set", 0x2400FF00)])
            self.assertEqual(len(compiled), 2)
            for env in ({"CONKER_INIT_SHADOW_CORPUS_CU1": "maybe"},
                        {"CONKER_INIT_SHADOW_CORPUS_CONTEXT": "maybe"}):
                with mock.patch.dict(os.environ, env, clear=True):
                    with self.assertRaises(ValueError):
                        selected.setUpClass()
            self.assertEqual(len(compiled), 2)

    def test_dispatch_counts_statuses_and_mode_local_depths(self):
        # Synthetic page orchestration only; this test does not execute MIPS.
        for context in ("generic", "exception-masked"):
            for selection in ("set", "clear", "both"):
                with self.subTest(context=context, selection=selection):
                    case = corpus.InitDecompressorShadowCorpusTests(
                        "test_all_507_retail_pages_selected_cu1_modes")
                    case.corpus_context = context
                    case.corpus_modes = corpus.cu1_modes(selection)
                    case.corpus_statuses = [(mode, corpus.context_status(context, mode))
                                           for mode in case.corpus_modes]
                    case.pages = [(i, 0, 1, b"X", b"Q") for i in range(507)]
                    case.rom = b"X" + bytes(15)
                    case.image = bytes(0x2D4B0) + (b"Q" + bytes(4095)) * 507
                    case.adapter_images = [("fake", str(i), SimpleNamespace(code={0: 0}))
                                           for i in range(6)]
                    case.maximum_depths = {("fake", str(i)): 99 for i in range(6)}
                    calls = []

                    def compare(supplied, status, **kwargs):
                        self.assertEqual(supplied, case.rom)
                        self.assertEqual(kwargs, {"expected_output": b"Q",
                                                 "expected_result": 1, "dma_size": 16})
                        if len(calls) % 507 == 0:
                            self.assertEqual(set(case.maximum_depths.values()), {0})
                        for key in case.maximum_depths:
                            case.maximum_depths[key] = 10 + len(calls) // 507
                        calls.append(status)

                    case.compare = compare
                    output = io.StringIO()
                    with contextlib.redirect_stdout(output):
                        case.test_all_507_retail_pages_selected_cu1_modes()
                    self.assertEqual(calls, [status for _, status in case.corpus_statuses
                                             for _ in range(507)])
                    self.assertIn("runs=%d" % (len(calls) * 6), output.getvalue())
                    for mode in case.corpus_modes:
                        self.assertIn("CU1-%s corpus: pages=507/507" % mode, output.getvalue())
                        self.assertIn("cu1=%s pages=507" % mode, output.getvalue())


if __name__ == "__main__":
    unittest.main()
