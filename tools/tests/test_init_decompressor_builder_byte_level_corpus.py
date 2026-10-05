"""Opt-in full masked corpus for the banked byte-depth packed O2 candidate."""

import hashlib
import json
import unittest
from pathlib import Path

from tools.tests import test_init_decompressor_builder_byte_level as byte_level
from tools.tests import test_init_decompressor_complement_low_mask as mask
from tools.tests import test_init_decompressor_distance_operation_local as distance


class InitDecompressorBuilderByteLevelCorpusTests(
        distance.InitDecompressorDistanceOperationLocalCorpusTests):
    shadow_extra_flags = byte_level.InitDecompressorBuilderByteLevelTests.shadow_extra_flags

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        if cls.corpus_context != 'exception-masked':
            raise ValueError('byte-depth qualification requires exception-masked context')
        if [(label, profile) for label, profile, _ in cls.adapter_images] != [
                ('packed-remaining', 'o2g3')]:
            raise ValueError('byte-depth qualification requires packed-remaining/o2g3 selection')
        cls.source_paths = tuple(cls.root / path for path in (
            'tools/experiments/init_decompressor_semantic.c',
            'tools/experiments/init_decompressor_core_adapter.s',
            'tools/experiments/compile_init_decompressor.py',
            'tools/tests/test_init_decompressor_builder_byte_level.py',
            'tools/tests/test_init_decompressor_builder_byte_level_corpus.py',
            'tools/tests/test_init_decompressor_shadow_corpus.py',
            'tools/tests/test_init_decompressor_pointer_owned_adapter.py',
            'tools/tests/test_init_decompressor_live_stack_writes.py'))
        cls.source_hashes = cls.hash_sources()
        body = mask.object_text(Path(cls.directory.name) / 'packed-remaining-shadow/o2g3.o')
        cls.object_hash = hashlib.sha256(body).hexdigest()
        if cls.object_hash != 'dce986104060637a90746c3c16c711b2bd792ee835c699c87a13904fb173082a':
            raise AssertionError('byte-depth packed instruction image differs from the banked candidate')
        receipt = cls.receipts['packed-remaining', 'o2g3']
        _, _, image = cls.adapter_images[0]
        adapter_bytes = (image.symbols['init_decode_retail_core_adapter_end'] -
                         image.symbols['init_decode_retail_core_adapter'])
        if (len(body), receipt['text_bytes'], adapter_bytes, len(image.code) * 4) != (
                4320, 4320, 176, 4496):
            raise AssertionError('byte-depth complete allocation changed')
        cls.completed_runs = {mode: 0 for mode in cls.corpus_modes}
        cls.corpus_completed = False
        print('byte-depth corpus gate: hash=%s text=4320 adapter=176 executable=4496' %
              cls.object_hash, flush=True)

    @classmethod
    def hash_sources(cls):
        return {str(path.relative_to(cls.root)): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in cls.source_paths}

    def compare(self, chunk, status, **kwargs):
        super().compare(chunk, status, **kwargs)
        if self._outcome.success:
            mode = next(mode for mode, expected in self.corpus_statuses if expected == status)
            type(self).completed_runs[mode] += len(self.adapter_images)

    def test_all_507_retail_pages_selected_cu1_modes(self):
        super().test_all_507_retail_pages_selected_cu1_modes()
        self.assertTrue(self._outcome.success, 'corpus comparison failed')
        self.assertEqual(type(self).completed_runs,
                         {mode: 507 for mode in self.corpus_modes})
        type(self).corpus_completed = True

    @classmethod
    def tearDownClass(cls):
        after = cls.hash_sources()
        unchanged = after == cls.source_hashes
        output = cls.root / 'conker/build/init-byte-depth-corpus-20261005' / (
            cls.corpus_context + '-' + '-'.join(cls.corpus_modes))
        output.mkdir(parents=True, exist_ok=True)
        depth = cls.maximum_depths['packed-remaining', 'o2g3']
        report = {'qualification': 'masked-guarded-instruction-model-only; no adoption',
            'complete': cls.corpus_completed and unchanged,
            'context': cls.corpus_context, 'statuses': dict(cls.corpus_statuses),
            'paired_runs': cls.completed_runs, 'profile': 'packed-remaining/o2g3',
            'c_text_bytes': 4320, 'adapter_bytes': 176, 'executable_bytes': 4496,
            'retail_bytes': 3984, 'object_sha256': cls.object_hash,
            'maximum_stack_descent': depth, 'source_hashes_before': cls.source_hashes,
            'source_hashes_after': after, 'source_hashes_unchanged': unchanged,
            'compiler_receipt': cls.receipts['packed-remaining', 'o2g3']}
        (output / 'qualification.json').write_text(json.dumps(report, indent=2) + '\n')
        if not unchanged:
            raise AssertionError('corpus source/adapter/guard hashes changed during qualification')


if __name__ == '__main__':
    unittest.main()
