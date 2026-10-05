"""Fast orchestration checks, not execution evidence for the full corpus."""

import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from tools.tests import test_init_decompressor_builder_byte_level as byte_level
from tools.tests import test_init_decompressor_builder_byte_level_corpus as corpus
from tools.tests import test_init_decompressor_distance_operation_local as distance
from tools.tests import test_init_decompressor_live_stack_writes as live
from tools.tests import test_init_decompressor_pointer_owned_adapter as pointer


class InitDecompressorBuilderByteLevelCorpusSelectionTests(unittest.TestCase):
    def selected(self):
        return type('SelectedByteDepthCorpus',
                    (corpus.InitDecompressorBuilderByteLevelCorpusTests,), {})

    def test_candidate_flags_and_guarded_fixture_are_inherited(self):
        selected = self.selected()
        self.assertEqual(selected.shadow_extra_flags,
                         byte_level.InitDecompressorBuilderByteLevelTests.shadow_extra_flags)
        self.assertIn('--builder-byte-level', selected.shadow_extra_flags)
        self.assertIn('--core-pointer-arguments', selected.shadow_extra_flags)
        self.assertTrue(issubclass(selected.fixture_type, pointer.PointerOwnedFixture))
        self.assertTrue(issubclass(selected.fixture_type, live.LiveStackWriteFixture))

    def test_wrong_context_or_profile_is_rejected_before_object_access(self):
        for context, images, message in (
                ('generic', [('packed-remaining', 'o2g3', None)], 'exception-masked'),
                ('exception-masked', [('packed-remaining', 'o1', None)], 'selection'),
                ('exception-masked', [('frame', 'o2g3', None)], 'selection'),
                ('exception-masked', [('packed-remaining', 'o2g3', None)] * 2, 'selection')):
            with self.subTest(context=context, images=images):
                def setup(cls):
                    cls.corpus_context, cls.adapter_images = context, images

                with mock.patch.object(distance.InitDecompressorDistanceOperationLocalCorpusTests,
                        'setUpClass', classmethod(setup)), mock.patch.object(
                        corpus.mask, 'object_text') as read_object:
                    with self.assertRaisesRegex(ValueError, message):
                        self.selected().setUpClass()
                    read_object.assert_not_called()

    def test_wrong_instruction_hash_is_rejected(self):
        def setup(cls):
            cls.corpus_context = 'exception-masked'
            cls.adapter_images = [('packed-remaining', 'o2g3', None)]
            cls.root = Path(__file__).resolve().parents[2]
            cls.directory = SimpleNamespace(name='synthetic-corpus-directory')

        with mock.patch.object(distance.InitDecompressorDistanceOperationLocalCorpusTests,
                'setUpClass', classmethod(setup)), mock.patch.object(
                corpus.mask, 'object_text', return_value=b'not the banked instruction image'):
            with self.assertRaisesRegex(AssertionError, 'banked candidate'):
                self.selected().setUpClass()

    def test_collected_failure_cannot_mark_corpus_complete(self):
        for success in (False, True):
            with self.subTest(success=success):
                selected = self.selected()
                selected.corpus_modes = ('clear', 'set')
                selected.completed_runs = {'clear': 507, 'set': 507}
                selected.corpus_completed = False
                case = selected('test_all_507_retail_pages_selected_cu1_modes')
                case._outcome = SimpleNamespace(success=success)
                with mock.patch.object(
                        distance.InitDecompressorDistanceOperationLocalCorpusTests,
                        'test_all_507_retail_pages_selected_cu1_modes', return_value=None):
                    if success:
                        case.test_all_507_retail_pages_selected_cu1_modes()
                    else:
                        with self.assertRaisesRegex(AssertionError, 'corpus comparison failed'):
                            case.test_all_507_retail_pages_selected_cu1_modes()
                self.assertEqual(selected.corpus_completed, success)

    def test_completed_counts_require_successful_comparison(self):
        for success in (False, True):
            with self.subTest(success=success):
                selected = self.selected()
                selected.corpus_statuses = (('clear', 0x0400FF00),)
                selected.adapter_images = [('packed-remaining', 'o2g3', None)]
                selected.completed_runs = {'clear': 0}
                case = selected('test_all_507_retail_pages_selected_cu1_modes')
                case._outcome = SimpleNamespace(success=success)
                with mock.patch.object(
                        distance.InitDecompressorDistanceOperationLocalCorpusTests,
                        'compare', return_value=None):
                    case.compare(None, 0x0400FF00)
                self.assertEqual(selected.completed_runs, {'clear': int(success)})


if __name__ == '__main__':
    unittest.main()
