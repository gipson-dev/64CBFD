"""Rejection controls for exact compiler output that narrows cache alias behavior."""

import hashlib
import re
import shutil
import struct
import unittest
from pathlib import Path

from tools.experiments import game_cache_installer_candidates as screen
from tools.tests import test_game_asset_table_lookup_and_block_load as asset
from tools.tests.test_game_queued_segment_writer import SegmentQueueOracle, STACK
from tools.tests.test_game_viewport_renderer import RendererOracle


ENTRY, CACHE, INPUT, COPY = 0x1502AB04, 0x800C3D68, 0x20000, 0x10023A10


class CacheInstallerOracle(RendererOracle):
    """Full routine with a bounded byte-copy callback, not the real SDK bcopy."""

    def __init__(self, words, memory, arguments):
        SegmentQueueOracle.__init__(self, words, ENTRY, memory, arguments)
        self.connected, self.calls = {}, []

    def put(self, address, value, size):
        SegmentQueueOracle.put(self, address, value, size)

    def record_call(self, target):
        assert target == COPY
        self.calls.append((target, *self.r[4:7]))

    def hook(self, target):
        assert target == COPY
        source, destination, length = self.r[4:7]
        assert destination == CACHE and 0 <= length <= 256
        for i in range(length):
            self.put(destination+i, self.get(source+i, 1), 1)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register


def memory_case(phase=0):
    memory={STACK+i:0xA5 for i in range(-0x80,0x40)}
    memory.update({CACHE+i:0xA5 for i in range(-16,272)})
    memory.update({INPUT+i:0xA5 for i in range(-16,144)})
    for i in range(64):
        value=(0x90000000+i*17+phase*0x13579B)&0xFFFFFFFF
        memory.update({CACHE+i*4+j:byte for j,byte in enumerate(struct.pack('>I',value))})
    for i in range(32):
        value=(0xF0000000+i*19+phase*0x2468AC)&0xFFFFFFFF
        memory.update({INPUT+i*4+j:byte for j,byte in enumerate(struct.pack('>I',value))})
    return memory


class GameCacheInstallerCandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        cls.forms=dict(screen.candidates())
        asset.GameAssetTableLookupAndBlockLoadTests.setUpClass()
        cls.addClassCleanup(asset.GameAssetTableLookupAndBlockLoadTests.directory.cleanup)
        cls.path=asset.GameAssetTableLookupAndBlockLoadTests.path
        cls.fixture=asset.GameAssetTableLookupAndBlockLoadTests.fixture
        cls.fixture+='\n'+screen.BASELINE.replace('func_1502AB04','baseline')+'\n'
        for label,form in (('pair_copy','local-generation-first'),
                           ('word_copy','word-offset-scalar-descriptor')):
            cls.fixture+=cls.forms[form].replace('func_1502AB04',label)+'\n'

    run_host=asset.GameAssetTableLookupAndBlockLoadTests.run_host

    def test_fresh_compiler_controls_reproduce_stack_lifetime_and_complete_slot(self):
        if not (self.root/'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(name) is None for name in ('mips-linux-gnu-ld','mips-linux-gnu-objdump')):
            self.skipTest('IDO/MIPS tools unavailable')
        output=self.root/'conker/build/game-cache-installer-test'
        output.mkdir(exist_ok=True)
        retail=list(struct.unpack_from('>97I',(self.root/'conker/conker.us.bin').read_bytes(),0x57FB4))
        for name,expected in (('baseline',(87,0x20,93)),
                ('scalar-local-count',(87,0x28,74)),
                ('pair-copy-AssetTablePair57FA0-local-count',(97,0x28,6)),
                ('local-generation-first',(97,0x28,0)),
                ('word-offset-scalar-descriptor',(97,0x28,41))):
            with self.subTest(name=name):
                record,words=screen.compile_candidate(self.root,output,name,self.forms[name])
                self.assertEqual((record['body_words'],record['frame'],record['real_differences']),expected)
                self.assertEqual(record['diagnostics'],'')
                if name=='baseline':
                    self.assertEqual(hashlib.sha256(struct.pack('>97I',*words)).hexdigest(),
                        '9411056ee2483732bfd3b404b7ab27b514a0af4c614b62c554dbe125f1b0719a')
                if name=='local-generation-first':
                    self.assertEqual(words,retail)
                if name=='scalar-local-count':
                    self.assertEqual(words[:19],retail[:19])
                    self.assertEqual(hashlib.sha256(struct.pack('>97I',*words)).hexdigest(),
                        '6acec640d1eb26a525a32a799d53abb2effeb9336ed73ec7fb4bc931e32ebad0')

    def test_exact_pair_assignment_is_rejected_for_partial_overlap(self):
        self.run_host(r'''
reset(); baseline(1,((u32 *)D_800C3D68)+61,41,0xFFFFFFF8);
if(error || D_800C3D68[15].offset!=115 || D_800C3D68[15].descriptor!=115) return 1;
reset(); pair_copy(1,((u32 *)D_800C3D68)+61,41,0xFFFFFFF8);
/* The two-word aggregate loads the descriptor before the offset store overwrites it. */
if(error || D_800C3D68[15].offset!=115 || D_800C3D68[15].descriptor!=215) return 2;
reset(); word_copy(1,((u32 *)D_800C3D68)+61,41,0xFFFFFFF8);
if(error || D_800C3D68[15].offset!=115 || D_800C3D68[15].descriptor!=115) return 3;
''')

    def test_word_copy_preserves_all_833_bounded_alias_cases(self):
        self.run_host(r'''
int n,k,i,cases=0; AssetTableCache57FA0 expected[16];
for(n=0;n<=16;n++) for(k=0;k<=64-2*n;k++) {
    reset(); baseline(n,(u32 *)D_800C3D68+k,41,0xFFFFFFF8);
    for(i=0;i<16;i++) expected[i]=D_800C3D68[i];
    reset(); word_copy(n,(u32 *)D_800C3D68+k,41,0xFFFFFFF8);
    if(error || copies!=(n!=0)) return 1;
    for(i=0;i<16;i++) if(!equal(D_800C3D68[i],expected[i])) return 2;
    cases++;
}
if(cases!=833) return 3;
''')

    def test_production_keeps_scalar_copy_and_original_qualification(self):
        source=(self.root/'conker/src/game_57FA0.c').read_text()
        body=re.search(r'void func_1502AB04\([^;{}]+\) \{\n.*?\n\}',source,re.S).group(0)
        self.assertEqual(body,self.forms['scalar-local-count'])

    def test_complete_retail_scalar_and_word_copy_traces_keep_live_alias_reads(self):
        if not (self.root/'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(name) is None for name in ('mips-linux-gnu-ld','mips-linux-gnu-objdump')):
            self.skipTest('IDO/MIPS tools unavailable')
        output=self.root/'conker/build/game-cache-installer-test'
        output.mkdir(exist_ok=True)
        retail=list(struct.unpack_from('>97I',(self.root/'conker/conker.us.bin').read_bytes(),0x57FB4))
        forms=[retail]
        for name in ('scalar-local-count','word-offset-scalar-descriptor'):
            _,words=screen.compile_candidate(self.root,output,name,self.forms[name])
            forms.append(words)
        coverage=[set(),set(),set()]
        cases=0
        for phase in range(3):
            memory=memory_case(phase)
            for count in range(17):
                pointers=[CACHE+i*4 for i in range(65-2*count)]
                pointers.append(INPUT if count else 0)
                for pointer in pointers:
                    args=(count,pointer,0xFFFFFFFF-phase,0xFFFFFFF8+phase)
                    models=[CacheInstallerOracle(words,memory,args).run() for words in forms]
                    for index,model in enumerate(models):
                        coverage[index].update(model.visits)
                        self.assertEqual(model.calls,models[0].calls)
                        self.assertEqual({a:v for a,v in model.memory.items() if not STACK-0x80<=a<STACK+0x40},
                                         {a:v for a,v in models[0].memory.items() if not STACK-0x80<=a<STACK+0x40})
                        self.assertEqual([r for r in model.reads if not STACK-0x80<=r[0]<STACK+0x40],
                                         [r for r in models[0].reads if not STACK-0x80<=r[0]<STACK+0x40])
                    cases+=1
        self.assertEqual(cases,2550)
        self.assertEqual([len(v) for v in coverage],[97,87,97])
        print('cache installer:',cases,'three-way traces; complete 97/87/97 word coverage')


if __name__=='__main__':
    unittest.main()
