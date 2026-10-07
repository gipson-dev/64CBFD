"""Actor identity classification, original switch ownership and complete direct C."""

import csv
import itertools
import json
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from tools.tests.game_owner_pool import assert_guard_history

from tools.experiments import game_actor_classifier_candidates as screen
from tools.match_progress import load_elf_functions
from tools.patch_generated_slice_ld import load_game_data_layout
from tools.pad_generated_object import parse_object
from tools.tests.test_game_effect_dispatch_match import game_data
from tools.tests.test_game_payload_copy_wrapper_match import SignedByteOracle
from tools.tests.test_game_table_range_loader import STACK
from tools.tests.test_game_actor_triangle_transform_match import put
from tools.tests import test_game_random_curve_record as native

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly

ACTOR=0x21000


class GameActorClassifierMatchTests(unittest.TestCase):
    run_host=native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        cls.output=cls.root/'conker/build/game-actor-classifier-test';cls.output.mkdir(exist_ok=True)
        cls.record,cls.words,cls.pool=screen.compile_candidate(cls.root,cls.output,'selected')
        cls.rom=(cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail=list(struct.unpack_from('>45I',cls.rom,screen.ROM))
        data,base=game_data(cls.root/'conker/build/conker.us.elf')
        start,vram,_,owners=load_game_data_layout(cls.root/'conker')
        cls.original=data[screen.TABLE-base:screen.TABLE-base+536]
        assert cls.original==cls.rom[start+screen.TABLE-vram:start+screen.TABLE-vram+536]
        cls.table_owners=[owner for owner in owners if owner['address']<screen.TABLE+536 and owner['end']>screen.TABLE]
        cls.answers=[11]*256
        for first,count,offset in ((121,45,0),(0,89,180)):
            for identity,target in enumerate(struct.unpack_from('>%dI'%count,cls.original,offset),first):
                index=(target-screen.ENTRY)//4
                if target==0x15141CB4:answer=11
                else:
                    assert cls.retail[index]==0x03E00008
                    delay=cls.retail[index+1]
                    assert delay==0x00001025 or delay&0xFFFF0000==0x24020000
                    answer=0 if delay==0x00001025 else delay&65535
                cls.answers[identity]=answer
        cls.directory=tempfile.TemporaryDirectory();cls.addClassCleanup(cls.directory.cleanup)
        cls.path=Path(cls.directory.name)

    def memory(self,identity,alignment=0,poison=0xA5,pool=None):
        memory={STACK+i:poison for i in range(-0x600,0x100)}
        memory.update({ACTOR+i:poison for i in range(-16,64)})
        memory[ACTOR+alignment+4]=identity
        memory.update({screen.TABLE+i:value for i,value in enumerate(self.original if pool is None else pool)})
        return memory

    def model(self,words,memory,alignment=0,phase=0):
        return SignedByteOracle(words,memory,entry=screen.ENTRY,arguments=(ACTOR+alignment,),phase=phase).run()

    def test_thirty_two_controls_complete_direct_slot_and_all_table_targets(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences']),(45,0,0))
        self.assertEqual(self.words,self.retail)
        self.assertEqual(self.pool[:536],self.original);self.assertEqual(self.pool[536:],bytes(8))
        expected={identity:value for value,identities in screen.GROUPS.items() for identity in identities}
        self.assertEqual(self.answers,[expected.get(i,11) for i in range(256)])
        records=[]
        for name,body in screen.candidates():
            for profile in screen.PROFILES:
                record,words,pool=screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                self.assertEqual(record['diagnostics'],'');records.append(record)
                if record['differences']==0:
                    self.assertEqual(words,self.retail);self.assertEqual(pool[:536],self.original)
        self.assertEqual(sum(record['differences']==0 for record in records),8)
        (self.output/'controls.json').write_text(json.dumps(records,indent=2)+'\n')

    def test_actual_padder_preserves_words_and_both_relocation_addends(self):
        text,functions,relocations=parse_object(self.output/'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['value'],0)
        self.assertEqual(relocations,{0x1C:[('R_MIPS_HI16','.rodata')],0x24:[('R_MIPS_LO16','.rodata')],
            0x3C:[('R_MIPS_HI16','.rodata')],0x44:[('R_MIPS_LO16','.rodata')]})
        self.assertEqual(struct.unpack_from('>I',text,0x24)[0]&65535,0)
        self.assertEqual(struct.unpack_from('>I',text,0x44)[0]&65535,180)
        layout=self.output/'layout.csv'
        layout.write_text('version,section,filename,function,address,end\nus,game,game_16EE20,func_15141C0C,0x15141C0C,0x15141CC0\n')
        assembly=emit_padded_assembly(self.output/'selected.o',layout,'game_16EE20',rodata_symbol=screen.ANCHOR)
        (self.output/'padded.s').write_text(assembly)
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(self.output/'padded.o'),
            str(self.output/'padded.s')],check=True,capture_output=True)
        padded,symbols,mapped=parse_object(self.output/'padded.o')
        self.assertEqual(symbols[screen.FUNCTION]['size'],180)
        self.assertEqual(padded[:180],text[:180])
        self.assertNotIn('.rodata',screen.sections(self.output/'padded.o'))
        self.assertEqual(mapped,{offset:[(kind,screen.ANCHOR) for kind,_ in items] for offset,items in relocations.items()})
        for anchor in (screen.TABLE,0x90007FFC):
            elf=self.output/('padded-%X.elf'%anchor)
            subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'classifier.ld'),
                '-e',screen.FUNCTION,'--defsym=%s=0x%X'%(screen.ANCHOR,anchor),'-o',str(elf),str(self.output/'padded.o')],
                check=True,capture_output=True)
            words=list(struct.unpack_from('>45I',screen.sections(elf)['.text'][1]))
            for hi,lo,addend in ((0x1C,0x24,0),(0x3C,0x44,180)):
                address=anchor+addend
                self.assertEqual(words[hi//4]&65535,((address+0x8000)>>16)&65535)
                self.assertEqual(words[lo//4]&65535,address&65535)
            if anchor==screen.TABLE:self.assertEqual(words,self.retail)

    def test_guest_every_byte_alignment_poison_full_storage_and_exact_reads(self):
        coverage=[set(),set()];cases=0
        for identity,alignment,poison,phase in itertools.product(range(256),range(4),(0,0x55,0xA5,0xFF),(0,8)):
            memory=self.memory(identity,alignment,poison);models=[]
            for index,words in enumerate((self.words,self.retail)):
                model=self.model(words,memory,alignment,phase);models.append(model)
                self.assertEqual(model.r[2],self.answers[identity]);self.assertEqual(model.memory,memory)
                self.assertEqual(model.calls,[]);self.assertEqual(model.events[0],('R',ACTOR+alignment+4,1,identity))
                self.assertFalse([event for event in model.events if event[0]=='W'])
                coverage[index].update(model.visits)
            self.assertEqual(models[0].events,models[1].events);cases+=1
        self.assertEqual(cases,8192)
        self.assertEqual(coverage,[set(range(screen.ENTRY,screen.ENTRY+180,4))]*2)
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases,bodies=2,covered_words=[45,45]),indent=2)+'\n')

    def test_native_actual_source_every_identity_and_unaligned_record(self):
        owner=(self.root/'conker/src/game_16EE20.c').read_text()
        body=owner[owner.index(screen.SELECTED):owner.index(screen.SELECTED)+len(screen.SELECTED)] if screen.SELECTED in owner else screen.SELECTED
        answers=','.join(map(str,self.answers))
        self.fixture='typedef unsigned char u8;typedef int s32;\n'+body+'\nstatic int answers[256]={'+answers+'};\n'
        self.run_host(r'''
u8 bytes[48],before[48];int identity,alignment,poison,i,cases=0;
int poisons[]={0,0x55,0xA5,0xFF};
if(sizeof(void *)!=4 || sizeof(s32)!=4) return 80;
for(identity=0;identity<256;identity++) for(alignment=0;alignment<16;alignment++) for(poison=0;poison<4;poison++) {
    for(i=0;i<48;i++) bytes[i]=(u8)poisons[poison];
    bytes[16+alignment+4]=(u8)identity;
    for(i=0;i<48;i++) before[i]=bytes[i];
    if(func_15141C0C(bytes+16+alignment)!=answers[identity]) return 81;
    for(i=0;i<48;i++) if(bytes[i]!=before[i]) return 82;
    cases++;
}
if(cases!=16384) return 83;
''')
        (self.output/'native.json').write_text(json.dumps(dict(cases=16384,pointer_bytes=4,full_storage=True),indent=2)+'\n')

    def test_guest_minimal_actor_unmapped_byte_and_invalid_table_target(self):
        for identity in range(256):
            memory=self.memory(identity)
            for address in range(ACTOR-16,ACTOR+64):
                if address!=ACTOR+4:memory.pop(address)
            for words in (self.words,self.retail):self.assertEqual(self.model(words,memory).r[2],self.answers[identity])
        for words in (self.words,self.retail):
            memory=self.memory(121);del memory[ACTOR+4]
            with self.assertRaisesRegex(AssertionError,'unmapped read'):self.model(words,memory)
            memory=self.memory(121);put(memory,screen.TABLE,0x1BAD0000)
            with self.assertRaisesRegex(AssertionError,'unowned jump'):self.model(words,memory)

    def test_compiled_negative_bodies_change_returns_or_read_contract(self):
        negatives={'placeholder':'s32 func_15141C0C(u8 *actor) {return 0;}',
            'signed-byte':screen.SELECTED.replace('actor[4]','((signed char *)actor)[4]'),
            'wrong-field':screen.SELECTED.replace('actor[4]','actor[3]'),
            'missing-high-group':screen.SELECTED.replace('        case 0x96:\n',''),
            'wrong-default':screen.SELECTED.replace('return 11;','return 0;'),
            'wrong-category':screen.SELECTED.replace('return 6;','return 5;')}
        receipts=[]
        for name,body in negatives.items():
            _,words,pool=screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            differences=0
            for identity in range(256):
                model=self.model(words,self.memory(identity,pool=pool))
                differences+=model.r[2]!=self.answers[identity] or model.events[:1]!=[('R',ACTOR+4,1,identity)]
            self.assertGreater(differences,0,name);receipts.append(dict(name=name,cases=256,differences=differences))
        (self.output/'negatives.json').write_text(json.dumps(receipts,indent=2)+'\n')

    def test_connected_installed_dispatcher_with_compiled_classifier(self):
        from tools.tests.test_game_effect_dispatch_match import EffectOracle, memory_case, reference, CLASSIFY, MASK, CATEGORY, SEARCH, WORLD
        dispatcher=list(struct.unpack_from('>100I',self.rom,0x16EF2C));helpers={}
        for entry,offset,count in ((CLASSIFY,screen.ROM,45),(MASK,0x13CD7C,3),(CATEGORY,0x16F170,57),(SEARCH,0x17C190,23)):
            words=self.words if entry==CLASSIFY else struct.unpack_from('>%dI'%count,self.rom,offset)
            helpers.update({entry+i*4:word for i,word in enumerate(words)})
        data,base=game_data(self.root/'conker/build/conker.us.elf');cases=0
        for identity,selected,layout,mutation in itertools.product(range(256),(-1,0,20),(0,3),(0,15,32)):
            category=self.answers[identity]
            memory=memory_case(category,selected,-1,layout,0)
            memory.update({0x800A5218+i:data[0x800A5218-base+i] for i in range(0x258)})
            put(memory,WORLD,47);put(memory,ACTOR+4,identity,1)
            wanted=reference(memory,category,selected,mutation,0xFFFFFFFF,6)
            model=EffectOracle(dispatcher,memory,category,selected,mutation,0xFFFFFFFF,0,helpers).run()
            self.assertEqual((model.calls,{a:v for a,v in model.memory.items() if not STACK-0x600<=a<STACK+0x100}),
                (wanted[1],wanted[0]));cases+=1
        self.assertEqual(cases,4608)
        (self.output/'caller.json').write_text(json.dumps(dict(cases=cases,classifier_words=45,dispatcher_words=100),indent=2)+'\n')

    def test_production_source_slots_original_owners_and_unchanged_guards(self):
        owner=(self.root/'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.SELECTED,owner);self.assertEqual(owner.count(screen.PROTOTYPE),2)
        functions,_,addresses=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(functions[screen.FUNCTION],self.retail);self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY)
        self.assertEqual(functions['func_15141A7C'],list(struct.unpack_from('>100I',self.rom,0x16EF2C)))
        data,base=game_data(self.root/'conker/build/conker.us.elf')
        self.assertEqual(data[screen.TABLE-base:screen.TABLE-base+536],self.original)
        self.assertEqual(self.table_owners,[dict(rom=0x249CC0,address=0x800A5200,end=0x800A5480,
            section='.data',input='build/assets/249CC0.bin.o(.data)')])
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:rows=list(csv.DictReader(stream))
        assert_guard_history(self,rows);self.assertFalse([row for row in rows if row['function']==screen.FUNCTION])
        makefile=(self.root/'conker/Makefile').read_text()
        self.assertIn('game_16EE20.c.o: RETAIL_RODATA_SYMBOL := '+screen.ANCHOR,makefile)
        self.assertIn('game_16EE20.c.o: Makefile',makefile)


if __name__=='__main__':unittest.main()
