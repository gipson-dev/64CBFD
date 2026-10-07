"""Four halfword outputs, exact stack-byte reads and preserved switch ownership."""

import csv
import itertools
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_output_mode_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.patch_generated_slice_ld import load_game_data_layout
from tools.pad_generated_object import parse_object
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read
from tools.tests.test_game_queued_segment_writer import STACK
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests import test_game_random_curve_record as native

OUTPUT, OBJECT = 0x24000, 0x25000
STUB = 's32 func_151441A4() {\n    return 0;\n}'
ALIASES = ((0,1,2,3),(0,0,2,3),(0,1,1,3),(0,1,2,0),
    (0,0,0,0),(3,2,1,0),(1,1,1,0),(0,1,0,1))
TARGETS = (0x151441F4,0x1514420C,0x151441D0,0x15144228,0x15144270)


def values(pattern):
    edges=(0,1,2,127,128,254,255,17)
    return tuple(edges[(pattern+i*(3 if pattern<8 else 5))%8] for i in range(9))


def fixture(mode=0,pattern=0,alias=0,phase=0,stack_alias=None,table=None):
    memory={STACK+i:(i*17+13)&255 for i in range(-0x100,0x100)}
    memory.update({OUTPUT+i:(i*31+7)&255 for i in range(32)})
    data=table if table is not None else struct.pack('>5I',*TARGETS)
    memory.update({screen.TABLE+i:b for i,b in enumerate(data)})
    inputs=values(pattern)
    # Word arguments carry poisoned high bits; only each big-endian low byte is live.
    words=tuple(0xABCD0000|v for v in (*inputs,mode))
    for i,word in enumerate(words):put(memory,STACK+phase+0x10+i*4,word)
    pointers=tuple(OUTPUT+i*2 for i in ALIASES[alias])
    if stack_alias is not None:
        offsets=((0x14,0x18,0x2C,0x34),(0x30,0x24,0x28,0x2C),
            (0x24,0x28,0x2C,0x30),(0x12,0x16,0x1A,0x36),
            (0x30,0x30,0x30,0x30),(0x36,0x16,0x1A,0x2E),
            (0x20,0x20,0x20,0x2C),(0x2C,0x24,0x28,0x10))[stack_alias]
        pointers=tuple(STACK+phase+i for i in offsets)
    return memory,(*pointers,*words)


def reference(memory,args,phase=0):
    after=memory.copy();trace=[];pointers=args[:4]
    def get(address,size=1):
        value=read(after,address,size);trace.append(('R',address,size,value));return value
    def store(address,value):
        put(after,address,value,2);trace.append(('W',address,2,value&65535))
    home=STACK+phase
    mode=get(home+0x37);scale=get(home+0x33);first=get(home+0x13)
    if mode<5:get(screen.TABLE+mode*4,4)
    if mode==0:
        store(pointers[3],0);value=get(pointers[3],2)
        for i in (2,1,0):store(pointers[i],value)
    elif mode==1:
        store(pointers[2],0);value=get(pointers[2],2)
        for i in (1,0):store(pointers[i],value)
        store(pointers[3],get(home+0x2F))
    elif mode==2:
        for i in range(4):store(pointers[i],get(home+0x23+i*4))
    else:
        if mode in (3,4):scale=get(home+0x33);first=get(home+0x13)
        store(pointers[0],first*scale>>8)
        for i in (1,2):store(pointers[i],get(home+0x13+i*4)*scale>>8)
        store(pointers[3],0)
    return after,trace


class OutputOracle(TriangleOracle):
    def __init__(self,words,memory,args,phase=0,entry=screen.ENTRY,connected=None):
        # Keep fixture argument homes authoritative, especially for unmapped-read tests.
        super().__init__(words,memory,arguments=args[:4],phase=phase,entry=entry,connected=connected)

    def record_call(self,target):
        assert target==screen.ENTRY
        self.calls.append((target,*self.arguments(14)))


class GameOutputModeMatchTests(unittest.TestCase):
    run_host=native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        cls.output=cls.root/'conker/build/game-output-mode-test';cls.output.mkdir(exist_ok=True)
        cls.record,cls.words=screen.compile_candidate(cls.root,cls.output,'selected')
        cls.rom=(cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail=list(struct.unpack_from('>86I',cls.rom,screen.ROM))
        address,data=screen.sections(cls.root/'conker/build/conker.us.elf')['.game_data']
        cls.original=data[screen.TABLE-address:screen.TABLE-address+20]
        start,vram,_,owners=load_game_data_layout(cls.root/'conker')
        assert cls.original==cls.rom[start+screen.TABLE-vram:start+screen.TABLE-vram+20]
        cls.table_owners=[o for o in owners if o['address']<screen.TABLE+20 and o['end']>screen.TABLE]
        cls.directory=tempfile.TemporaryDirectory();cls.addClassCleanup(cls.directory.cleanup);cls.path=Path(cls.directory.name)

    def receipt(self,name,report):(self.output/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')

    def test_complete_direct_slot_original_table_and_fourteen_argument_abi(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences']),(86,0,0))
        self.assertEqual(self.words,self.retail);self.assertEqual(self.record['diagnostics'],'')
        self.assertEqual(self.record['table'][:5],list(TARGETS));self.assertEqual(self.record['table'][5:],[0,0,0])
        self.assertEqual(self.original,struct.pack('>5I',*TARGETS));self.assertEqual(len(self.table_owners),1)
        self.assertEqual(self.record['relocations'],{0x18:[('R_MIPS_HI16','.rodata')],0x20:[('R_MIPS_LO16','.rodata')]})
        self.assertEqual(self.words[:3],[0x93AE0037,0x93A20033,0x93A80013])
        self.receipt('slot',dict(words=86,direct=True,frame=0,argument_positions=14,unused_argument=7,
            original_table_bytes=20,standalone_table_padding=12,table_owners=self.table_owners))

    def test_guest_all_mode_bytes_input_patterns_output_aliases_full_memory_and_trace(self):
        cases=0;coverage=[set(),set()]
        for mode,pattern,alias,phase in itertools.product(range(256),range(16),range(8),(0,8)):
            memory,args=fixture(mode,pattern,alias,phase);after,trace=reference(memory,args,phase)
            models=[]
            for i,words in enumerate((self.words,self.retail)):
                model=OutputOracle(words,memory,args,phase).run();self.assertEqual(model.memory,after)
                self.assertEqual(model.events,trace);self.assertEqual(model.calls,[])
                coverage[i].update(model.visits);models.append(model)
            self.assertEqual(models[0].r,models[1].r);cases+=1
        self.assertEqual([len(c) for c in coverage],[86,86])
        self.receipt('guest',dict(cases=cases,mode_bytes=256,patterns=16,output_alias_patterns=8,
            stack_phases=2,words_covered=86,full_memory=True,ordered_all_reads_writes=True,saved_state=True))

    def test_guest_live_stack_byte_overlaps_scale_snapshot_and_unused_slot(self):
        cases=0
        for mode,pattern,alias,phase in itertools.product(range(256),range(6),range(8),(0,8)):
            memory,args=fixture(mode,pattern,phase=phase,stack_alias=alias)
            after,trace=reference(memory,args,phase)
            for words in (self.words,self.retail):
                model=OutputOracle(words,memory,args,phase).run()
                self.assertEqual(model.memory,after);self.assertEqual(model.events,trace)
            cases+=1
        for mode in range(256):
            memory,args=fixture(mode)
            for i in range(4):del memory[STACK+0x1C+i]
            for words in (self.words,self.retail):OutputOracle(words,memory,args).run()
        self.receipt('stack-alias',dict(cases=cases,live_future_input_bytes=True,cached_scale_after_first_store=True,
            mode_snapshot=True,unused_argument_unmapped_modes=256,full_memory=True,ordered_trace=True,
            guest_argument_homes_not_portable_native_parameter_aliases=True))

    def test_unused_seventh_argument_all_byte_values_do_not_change_outputs_or_reads(self):
        self.assertEqual(len({values(i) for i in range(16)}),16)
        cases=0
        for mode,value,alias in itertools.product((0,1,2,3,4,5,255),range(256),(0,4)):
            memory,args=fixture(mode,3,alias);put(memory,STACK+0x1C,0x76543200|value)
            after,trace=reference(memory,args)
            for words in (self.words,self.retail):
                model=OutputOracle(words,memory,args).run()
                self.assertEqual(model.memory,after);self.assertEqual(model.events,trace)
                self.assertFalse(any(e[0]=='R' and STACK+0x1C<=e[1]<STACK+0x20 for e in model.events))
            cases+=1
        self.receipt('unused-input',dict(cases=cases,input_low_bytes=256,input_high_word_poison=True,
            all_switch_paths=True,output_aliases=True,no_unused_home_reads=True,distinct_patterns=16))

    def test_lazy_case_bytes_default_table_and_unmapped_required_reads(self):
        checks=0
        for mode in range(256):
            memory,args=fixture(mode)
            required={0x37,0x33,0x13}
            if mode==1:required.add(0x2F)
            elif mode==2:required.update((0x23,0x27,0x2B,0x2F))
            elif mode not in (0,1):required.update((0x17,0x1B))
            minimal={a:v for a,v in memory.items() if not STACK<=a<STACK+0x40 or a-STACK in required}
            if mode>=5:
                for i in range(20):del minimal[screen.TABLE+i]
            for words in (self.words,self.retail):OutputOracle(words,minimal,args).run()
            for offset in required:
                broken=minimal.copy();del broken[STACK+offset]
                for words in (self.words,self.retail):
                    with self.assertRaisesRegex(AssertionError,'unmapped'):OutputOracle(words,broken,args).run()
                checks+=1
        for mode in range(5):
            memory,args=fixture(mode);del memory[screen.TABLE+mode*4]
            with self.assertRaisesRegex(AssertionError,'unmapped'):OutputOracle(self.words,memory,args).run()
        memory,args=fixture(2);broken=list(args);broken[0]=0x12345678
        with self.assertRaisesRegex(AssertionError,'unmapped'):OutputOracle(self.words,memory,broken).run()
        self.receipt('reads',dict(mode_bytes=256,required_byte_negatives=checks,unused_home_bytes_unmapped=True,
            higher_modes_need_no_table=True,selected_table_and_outputs_fail_closed=True))

    def test_original_caller_four_outputs_ten_staged_bytes_and_delay_store(self):
        entry=0x1515BC10;fragment=list(struct.unpack_from('>25I',self.rom,0x1890C0))
        self.assertEqual(fragment[-2:],[0x0D451069,0xAFAE0034]);fragment += [0x8FBF0044,0x03E00008,0]
        cases=0
        for mode,pattern,phase in itertools.product(range(256),range(4),(0,8)):
            memory,_=fixture(mode,pattern,phase=phase)
            memory.update({OBJECT+i:0xA5 for i in range(64)})
            inputs=(*values(pattern),mode)
            for i,value in enumerate(inputs):put(memory,OBJECT+0x20+i,value,1)
            put(memory,STACK+phase+0x44,0xDEAD0000)
            staged=memory.copy()
            for i,value in enumerate(inputs):put(staged,STACK+phase+0x10+i*4,value)
            args=(*(STACK+phase+i for i in (0x70,0x6E,0x6C,0x6A)),*inputs)
            after,trace=reference(staged,args,phase)
            setup=[]
            for i,value in enumerate(inputs):
                setup.extend((('R',OBJECT+0x20+i,1,value),('W',STACK+phase+0x10+i*4,4,value)))
            expected=setup+trace+[('R',STACK+phase+0x44,4,0xDEAD0000)]
            for words in (self.words,self.retail):
                connected={screen.ENTRY+i*4:w for i,w in enumerate(words)}
                model=OutputOracle(fragment,memory,(),phase,entry,connected)
                model.r[16]=model.before[16]=OBJECT;model.run()
                self.assertEqual(model.calls,[(screen.ENTRY,*args)])
                self.assertEqual(model.memory,after);self.assertEqual(model.events,expected)
            cases+=1
        self.receipt('caller',dict(cases=cases,original_words=25,original_delay_argument13=True,
            original_four_pointer_setup_and_ten_byte_staging=True,full_memory=True,ordered_trace=True,
            earlier_context_and_return_seeded=True,whole_caller=False))

    def test_native_32_bit_all_modes_aliases_and_exhaustive_byte_products(self):
        self.fixture='typedef unsigned char u8;typedef short s16;typedef unsigned int u32;\n'+screen.SELECTED+r'''
static const int aliases[8][4]={{0,1,2,3},{0,0,2,3},{0,1,1,3},{0,1,2,0},
    {0,0,0,0},{3,2,1,0},{1,1,1,0},{0,1,0,1}};
static s16 words[16],expected[16];
static int check(u32 *v,int alias) {
    s16 *p[4];int i,mode=(u8)v[9],scale=(u8)v[8];
    for(i=0;i<16;i++)words[i]=expected[i]=(s16)(0xA500u+i);
    for(i=0;i<4;i++)p[i]=expected+aliases[alias][i];
    if(mode==0) {*p[3]=0;*p[2]=*p[3];*p[1]=*p[2];*p[0]=*p[1];}
    else if(mode==1) {*p[2]=0;*p[1]=*p[2];*p[0]=*p[1];*p[3]=(u8)v[7];}
    else if(mode==2) {for(i=0;i<4;i++)*p[i]=(u8)v[i+4];}
    else {for(i=0;i<3;i++)*p[i]=((u8)v[i]*scale)/256;*p[3]=0;}
    func_151441A4(words+aliases[alias][0],words+aliases[alias][1],words+aliases[alias][2],words+aliases[alias][3],
        v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9]);
    for(i=0;i<16;i++)if(words[i]!=expected[i])return 1;
    return 0;
}
'''
        self.run_host(r'''
static const u8 edge[8]={0,1,2,127,128,254,255,17};
static const u8 scaled[4]={3,4,5,255};u32 v[10];int m,p,a,i,x,s;
if(sizeof(void *)!=4 || sizeof(s16)!=2)return 1;
for(m=0;m<256;m++)for(p=0;p<16;p++)for(a=0;a<8;a++) {
    for(i=0;i<9;i++) { v[i]=0xABCD0000u|edge[(p+i*(p<8?3:5))%8]; }
    v[9]=0xABCD0000u|m;
    if(check(v,a))return 2;
}
for(x=0;x<256;x++)for(s=0;s<256;s++)for(m=0;m<4;m++)for(a=0;a<2;a++) {
    for(i=0;i<10;i++) { v[i]=0xABCD0080u; }
    v[0]=0xABCD0000u|x;v[8]=0xABCD0000u|s;v[9]=scaled[m];
    if(check(v,a?4:0))return 3;
}
''')
        self.receipt('native',dict(cases=557056,bits=32,all_mode_bytes=True,all_65536_byte_products=True,
            all_output_alias_patterns=True,typed_fourteen_input_calls=True,argument_conversion=True,
            guest_stack_home_aliases_not_claimed=True))

    def copied_owner(self):
        if hasattr(self.__class__,'copied'):return self.__class__.copied
        source=(self.root/'conker/src/game_16EE20.c').read_text()
        baseline=source.replace(screen.SELECTED,STUB).replace(screen.PROTOTYPE,'s32 func_151441A4();')
        self.assertIn(STUB,baseline)
        selected=baseline.replace('s32 func_151441A4();',screen.PROTOTYPE).replace(STUB,screen.SELECTED)
        objects=[];warnings=[]
        for name,body in (('baseline',baseline),('selected',selected)):
            obj,warning=compile_owner(self.root,self.output,body,'owner-'+name);warnings.append(warning)
            processed=self.output/('owner-'+name+'-postprocessed.o');shutil.copyfile(obj,processed)
            subprocess.run([sys.executable,str(self.root/'tools/asm-processor/asm_processor.py'),'-O2','-g3',
                str((self.output/('owner-'+name+'.c')).relative_to(self.root/'conker')),'--post-process',
                str(processed.relative_to(self.root/'conker')),'--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude','include/asm_processor_prelude.inc'],cwd=self.root/'conker',check=True,capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0],warnings[1]);self.assertEqual(len(warnings[0]),2)
        self.__class__.copied=objects;return objects

    def test_copied_owner_all_neighbors_prior_pool_and_appended_table(self):
        old,new=self.copied_owner();ot,of,orr=parse_object(old);text,functions,rel=parse_object(new)
        self.assertEqual(set(functions),set(of))
        for name,f in functions.items():
            if name==screen.FUNCTION:continue
            previous=of[name]
            self.assertEqual(text[f['value']:f['value']+f['size']],ot[previous['value']:previous['value']+previous['size']],name)
            self.assertEqual({o-f['value']:r for o,r in rel.items() if f['value']<=o<f['value']+f['size']},
                {o-previous['value']:r for o,r in orr.items() if previous['value']<=o<previous['value']+previous['size']},name)
        op,np=normalized_pools(old),normalized_pools(new)
        self.assertEqual(op['.data'],np['.data']);self.assertEqual(len(op['.rodata'][0]),624)
        self.assertEqual(len(np['.rodata'][0]),656);self.assertEqual(op['.rodata'][0],np['.rodata'][0][:624])
        self.assertEqual(op['.rodata'][1],tuple(i for i in np['.rodata'][1] if i[0]<624))
        appended=np['.rodata'][1][len(op['.rodata'][1]):]
        self.assertEqual(appended,tuple((624+i*4,screen.FUNCTION,t-screen.ENTRY) for i,t in enumerate(TARGETS)))
        self.assertEqual(np['.rodata'][0][624:],bytes(32))
        f=functions[screen.FUNCTION];raw=list(struct.unpack_from('>86I',text,f['value']))
        self.assertEqual(raw[0x20//4],0x8C2E0270);raw[0x20//4]-=624
        standalone,_,_=parse_object(self.output/'selected.o')
        self.assertEqual(raw,list(struct.unpack_from('>86I',standalone)))
        self.receipt('owner',dict(functions=89,unchanged_neighbors=88,warnings=2,new_warnings=0,
            previous_pool_bytes=624,new_pool_bytes=656,prior_normalized_pool_unchanged=True,
            appended_table_bytes=20,alignment_padding=12,table_addend=624,raw_target_identical_after_addend=True))

    def test_actual_owner_padder_retail_binding_alternate_carries_and_stale_guards(self):
        _,owner=self.copied_owner()
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:rows=list(csv.DictReader(stream))
        rows=[r for r in rows if r['function']!=screen.FUNCTION]+screen.owner_guards()
        path=self.output/'guards.csv'
        def emit(items):
            with path.open('w',newline='') as stream:
                writer=csv.DictWriter(stream,fieldnames=list(items[0]));writer.writeheader();writer.writerows(items)
            return emit_padded_assembly(owner,self.root/'conker/retail_layout.us.txt','game_16EE20',
                rodata_symbol='jtbl_800A5218_game',word_patches_path=path)
        assembly=emit(rows);begin=assembly.index('.type %s, @function'%screen.FUNCTION)
        end=assembly.index('.size %s, . - %s'%(screen.FUNCTION,screen.FUNCTION),begin);end=assembly.index('\n',end)
        source,obj,elf=(self.output/('padded'+suffix) for suffix in ('.s','.o','.elf'))
        source.write_text('.text\n.globl '+screen.FUNCTION+'\n'+assembly[begin:end+1])
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(obj),str(source)],check=True,capture_output=True)
        _,functions,rel=parse_object(obj);self.assertEqual(functions[screen.FUNCTION]['size'],344)
        self.assertEqual(rel,{0x18:[('R_MIPS_HI16',screen.ANCHOR)],0x20:[('R_MIPS_LO16',screen.ANCHOR)]})
        for address in (screen.TABLE,0x81237FFC,0x81248004):
            subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'output-mode.ld'),'-e',screen.FUNCTION,
                '--defsym=%s=0x%X'%(screen.ANCHOR,address),'-o',str(elf),str(obj)],check=True,capture_output=True)
            words=list(struct.unpack_from('>86I',screen.sections(elf)['.text'][1]))
            expected=self.retail.copy();expected[6]=expected[6]&0xFFFF0000|((address+0x8000)>>16)&65535
            expected[8]=expected[8]&0xFFFF0000|address&65535;self.assertEqual(words,expected)
        for field,value in (('expected','0x8C2E0274'),('expected_relocations','R_MIPS_LO16:D_800BE9E4')):
            broken=[dict(r) for r in rows];broken[-1][field]=value
            with self.assertRaisesRegex(ValueError,'stale'):emit(broken)
        self.receipt('padding',dict(words=86,guards=2,only_table_relocation_binding=True,
            alternate_carries=2,stale_words_and_relocations_fail=True,no_insertions_or_omissions=True))

    def test_profile_controls_and_compiled_negatives(self):
        controls=[]
        for profile in screen.PROFILES:
            record,words=screen.compile_candidate(self.root,self.output,'profile-'+profile,profile=profile);controls.append(record)
            table=struct.pack('>%dI'%len(record['table']),*record['table'])
            for mode,alias in itertools.product(range(256),(0,4)):
                memory,args=fixture(mode,3,alias,table=table);after,_=reference(memory,args)
                model=OutputOracle(words,memory,args).run()
                self.assertEqual({a:v for a,v in model.memory.items() if OUTPUT<=a<OUTPUT+32},
                    {a:v for a,v in after.items() if OUTPUT<=a<OUTPUT+32})
        forms={'full-mode':screen.SELECTED.replace('u8 mode','u32 mode'),
            'wrong-shift':screen.SELECTED.replace('>> 8','>> 7'),
            'wrong-direct':screen.SELECTED.replace('*out0 = direct0','*out0 = direct1'),
            'wrong-fourth':screen.SELECTED.replace('*out3 = direct3','*out3 = direct2'),
            'nonzero-scaled-fourth':screen.SELECTED.replace('*out3 = 0;','*out3 = scale;'),
            'zero-load-elision':screen.SELECTED.replace('*out3 = 0;\n        *out0 = *out1 = *out2 = *out3;',
                '*out3 = 0;\n        *out2 = 0;\n        *out1 = 0;\n        *out0 = 0;')}
        negatives={}
        for name,body in forms.items():
            self.assertNotEqual(body,screen.SELECTED);record,words=screen.compile_candidate(self.root,self.output,name,body)
            table=struct.pack('>%dI'%len(record['table']),*record['table']);detected=0
            for mode,alias in itertools.product(range(8),(0,4)):
                memory,args=fixture(mode,3,alias,table=table);after,trace=reference(memory,args)
                model=OutputOracle(words,memory,args).run()
                public=lambda events:[e for e in events if OUTPUT<=e[1]<OUTPUT+32]
                detected+=(any(model.memory[a]!=v for a,v in after.items() if OUTPUT<=a<OUTPUT+32)
                    or public(model.events)!=public(trace))
            self.assertGreater(detected,0,name);negatives[name]=detected
        self.receipt('controls',dict(profiles=controls,profile_mode_alias_cases=2048,
            negative_detections=negatives,zero_load_elision_detected_by_reads=True,alternative_stack_read_schedules_unqualified=True))

    def test_production_complete_source_slot_original_table_and_guard_history(self):
        self.assertIn(screen.SELECTED,(self.root/'conker/src/game_16EE20.c').read_text())
        functions,_,addresses=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY);self.assertEqual(functions[screen.FUNCTION],self.retail)
        address,data=screen.sections(self.root/'conker/build/conker.us.elf')['.game_data']
        self.assertEqual(data[screen.TABLE-address:screen.TABLE-address+20],self.original)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:guards=list(csv.DictReader(stream))
        digest=assert_guard_history(self,guards);self.assertEqual(guards[10912:],screen.owner_guards())
        self.receipt('production',dict(words=86,direct_words=True,guards=len(guards),new_table_guards=2,
            guard_sha256=digest,original_table_unchanged=True))


if __name__=='__main__': unittest.main()
