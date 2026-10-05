"""Full cache-installer guards with live alias reads and commuting-store checks."""

import csv
import hashlib
import re
import shutil
import struct
import subprocess
import unittest
from pathlib import Path

from tools.experiments import game_cache_installer_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_cache_installer_candidates import CacheInstallerOracle, ENTRY, CACHE, INPUT, memory_case


GUARDS = {
    0x94: (0x8E0DFFFC, 0x8E0CFFFC),
    0x98: (0xAC470000, 0x24420010),
    0x9C: (0x24E70008, 0x24630010),
    0xA0: (0xAC510004, 0xAC6CFFF4),
    0xA4: (0x24420010, 0xAC47FFF0),
    0xA8: (0x24630010, 0x24E70008),
    0xB0: (0xAC4DFFFC, 0xAC51FFF4),
    0xB8: (0x3C0F0000, 0x3C0E0000),
    0xBC: (0x25EF0000, 0x25CE0000),
    0xC0: (0x00087100, 0x00086900),
    0xC4: (0x01CF1021, 0x01AE1021),
    0xF0: (0x8E0AFFE4, 0x8E18FFE4),
    0xF4: (0xAC510004, 0x24420040),
    0xF8: (0xAC470000, 0x24630040),
    0xFC: (0xAC4A000C, 0xAC78FFC4),
    0x100: (0x8E01FFE8, 0xAC51FFC4),
    0x104: (0x24E70008, 0xAC47FFC0),
    0x108: (0x24420040, 0x8E01FFE8),
    0x10C: (0xACA10000, 0x24E70008),
    0x110: (0x8E0DFFEC, 0x24A50040),
    0x114: (0xAC47FFD0, 0xACA1FFC0),
    0x118: (0xAC51FFD4, 0x8E0AFFEC),
    0x11C: (0xAC4DFFDC, 0x24C60040),
    0x120: (0x8E01FFF0, 0xACAAFFC4),
    0x124: (0x24E70008, 0xAC47FFD0),
    0x128: (0x24630040, 0xAC51FFD4),
    0x12C: (0xACC10000, 0x8E01FFF0),
    0x130: (0x8E18FFF4, 0x24E70008),
    0x134: (0xAC47FFE0, 0xACC1FFC0),
    0x138: (0xAC51FFE4, 0x8E0CFFF4),
    0x13C: (0xAC58FFEC, 0xACCCFFC4),
    0x140: (0x8E01FFF8, 0xAC47FFE0),
    0x144: (0x24E70008, 0xAC51FFE4),
    0x148: (0x24A50040, 0x8E01FFF8),
    0x14C: (0xAC81FFC0, 0x24E70008),
    0x150: (0x8E0BFFFC, 0xAC81FFC0),
    0x154: (0xAC47FFF0, 0x8E0EFFFC),
    0x158: (0x24E70008, 0xAC8EFFC4),
    0x15C: (0xAC51FFF4, 0xAC47FFF0),
    0x160: (0x24C60040, 0x24E70008),
    0x168: (0xAC4BFFFC, 0xAC51FFF4),
}


def source_body():
    return dict(screen.candidates())['word-selected']


def apply_linked_guards(words, omitted=None):
    result=words[:]
    for offset,(expected,replacement) in GUARDS.items():
        index=offset//4
        if offset in (0xB8,0xBC):
            assert result[index]&0xFFFF0000==expected
            replacement|=result[index]&0xFFFF
        else:
            assert result[index]==expected
        if offset!=omitted:
            result[index]=replacement
    return result


class SchedulingOracle(CacheInstallerOracle):
    def __init__(self, words, memory, arguments):
        self.events=[]
        super().__init__(words,memory,arguments)

    def get(self, address, size):
        value=super().get(address,size)
        self.events.append(('R',address,size,value))
        return value

    def put(self, address, value, size):
        if self.recording:
            self.events.append(('W',address,size,value&((1<<(size*8))-1)))
        super().put(address,value,size)

    def read_windows(self):
        windows,stores=[],[]
        for event in self.events+[('END',)]:
            if event[0]=='W':
                stores.append(event[1:])
                continue
            occupied=set()
            for address,size,_ in stores:
                addresses=set(range(address,address+size))
                assert not occupied&addresses, 'stores within a read window overlap'
                occupied.update(addresses)
            windows.append((tuple(sorted(stores)),event))
            stores=[]
        return windows


class GameCacheInstallerMatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        if not (cls.root/'ido/ido5.3_recomp/cc').is_file() or any(
                shutil.which(name) is None for name in ('mips-linux-gnu-ld','mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output=cls.root/'conker/build/game-cache-installer-match-test'
        cls.output.mkdir(exist_ok=True)
        cls.record,cls.raw=screen.compile_candidate(cls.root,cls.output,'selected',source_body())
        cls.retail=list(struct.unpack_from('>97I',(cls.root/'conker/conker.us.bin').read_bytes(),0x57FB4))
        cls.guarded=apply_linked_guards(cls.raw)

    def test_complete_raw_slot_and_checked_guard_result(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['real_differences']),
                         (97,0x28,41))
        self.assertEqual(self.record['diagnostics'],'')
        self.assertEqual(hashlib.sha256(struct.pack('>97I',*self.raw)).hexdigest(),
                         'a6bca817be8a9ee74df0bc7e91206bd401525478a5f4c39ffb832a9eed82a9bf')
        self.assertEqual(len(GUARDS),41)
        self.assertEqual({i*4 for i,(a,b) in enumerate(zip(self.raw,self.retail)) if a!=b},set(GUARDS))
        self.assertEqual(self.raw[:37],self.retail[:37])
        self.assertEqual(self.raw[-6:],self.retail[-6:])
        controls=lambda words: {i:word for i,word in enumerate(words)
            if word>>26 in (1,2,3,4,5,6,7,20,21) or word>>26==0 and word&63 in (8,9)}
        self.assertEqual(controls(self.raw),controls(self.retail))
        self.assertEqual(self.guarded,self.retail)

    def test_three_way_live_reads_and_independent_store_windows(self):
        coverage=[set(),set(),set()]
        cases=0
        for phase in range(3):
            memory=memory_case(phase)
            for count in range(17):
                pointers=[CACHE+i*4 for i in range(65-2*count)]
                pointers.append(INPUT if count else 0)
                for pointer in pointers:
                    args=(count,pointer,0xFFFFFFFF-phase,0xFFFFFFF8+phase)
                    models=[SchedulingOracle(words,memory,args).run()
                            for words in (self.retail,self.raw,self.guarded)]
                    reference=models[0]
                    windows=reference.read_windows()
                    for index,model in enumerate(models):
                        coverage[index].update(model.visits)
                        self.assertEqual(model.memory,reference.memory)
                        self.assertEqual(model.calls,reference.calls)
                        self.assertEqual(model.reads,reference.reads)
                        self.assertEqual(model.read_windows(),windows)
                    self.assertEqual(models[2].stores,reference.stores)
                    cases+=1
        self.assertEqual(cases,2550)
        self.assertEqual([len(v) for v in coverage],[97,97,97])
        print('cache installer guards:',cases,'three-way cases; independent stores between identical reads')

    def test_every_omitted_guard_breaks_the_closed_schedule(self):
        for offset in GUARDS:
            partial=apply_linked_guards(self.raw,offset)
            rejected=False
            for count in (1,2,3,4,7,8,16):
                for pointer in (INPUT,CACHE,CACHE+(64-2*count)*4):
                    memory=memory_case(1)
                    args=(count,pointer,0xFFFFFFFF,0xFFFFFFF8)
                    reference=SchedulingOracle(self.retail,memory,args).run()
                    try:
                        actual=SchedulingOracle(partial,memory,args).run()
                        rejected=(actual.memory!=reference.memory or actual.reads!=reference.reads
                                  or actual.calls!=reference.calls or actual.read_windows()!=reference.read_windows())
                    except (AssertionError,KeyError):
                        rejected=True
                    if rejected:
                        break
                if rejected:
                    break
            self.assertTrue(rejected,hex(offset))

    def test_unlinked_guard_inputs_and_preserved_address_relocations(self):
        functions,_,_=load_elf_functions(str(self.output/'selected.o'),'mips-linux-gnu-objdump')
        for offset,(expected,_) in GUARDS.items():
            self.assertEqual(functions['func_1502AB04'][offset//4],expected)
        relocations=subprocess.run(['mips-linux-gnu-objdump','-r',str(self.output/'selected.o')],
                                   check=True,capture_output=True,text=True).stdout
        actual={int(offset,16):(kind,symbol) for offset,kind,symbol in re.findall(
            r'(?m)^([0-9a-f]+)\s+(R_MIPS_\w+)\s+(\S+)\s*$',relocations)}
        self.assertEqual(actual,{0x24:('R_MIPS_HI16','D_800C3D68'),
            0x2C:('R_MIPS_LO16','D_800C3D68'),0x40:('R_MIPS_26','bcopy'),
            0x70:('R_MIPS_HI16','D_800C3D68'),0x74:('R_MIPS_LO16','D_800C3D68'),
            0xB8:('R_MIPS_HI16','D_800C3D68'),0xBC:('R_MIPS_LO16','D_800C3D68'),
            0xC8:('R_MIPS_HI16','D_800C3D68'),0xCC:('R_MIPS_LO16','D_800C3D68')})

    def test_production_source_rows_and_full_linked_identity(self):
        source=(self.root/'conker/src/game_57FA0.c').read_text()
        body=re.search(r'void func_1502AB04\([^;{}]+\) \{\n.*?\n\}',source,re.S).group(0)
        self.assertEqual(body,source_body())
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as source:
            rows=[row for row in csv.DictReader(source) if row['function']=='func_1502AB04']
        self.assertEqual(len(rows),41)
        self.assertEqual({int(r['offset'],0):(int(r['expected'],0),int(r['replacement'],0)) for r in rows},GUARDS)
        for row in rows:
            offset=int(row['offset'],0)
            relocation={0xB8:'R_MIPS_HI16:D_800C3D68',0xBC:'R_MIPS_LO16:D_800C3D68'}.get(offset,'-')
            self.assertEqual((row['expected_relocations'],row['replacement_relocations']),(relocation,relocation))
            self.assertEqual(row['filename'],'game_57FA0')
            self.assertEqual((row['insert_after'],row['omit']),('','false'))
        functions,_,addresses=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),
                                               'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502AB04'],ENTRY)
        self.assertEqual(functions['func_1502AB04'],self.retail)


if __name__=='__main__':
    unittest.main()
