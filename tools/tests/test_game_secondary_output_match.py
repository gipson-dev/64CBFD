"""Fourteen-mode leaf: direct slot, live homes, native values and linked ownership."""

import csv
import hashlib
import itertools
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_secondary_output_candidates as screen
from tools.experiments import game_output_mode_candidates as first
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.patch_generated_slice_ld import load_game_data_layout
from tools.pad_generated_object import parse_object
from tools.tests.game_owner_pool import normalized_pools
from tools.tests.test_game_output_mode_match import fixture as first_fixture, values, reference as first_reference
from tools.tests.test_game_output_mode_match import OUTPUT, OBJECT, ALIASES, OutputOracle
from tools.tests.test_game_point_transform_match import put, read
from tools.tests.test_game_queued_segment_writer import STACK
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests import test_game_random_curve_record as native

STUB = 's32 func_151442FC() {\n    return 0;\n}'


def fixture(mode=0,pattern=0,alias=0,phase=0,stack_alias=None,table=None):
    memory,args=first_fixture(mode,pattern,alias,phase,stack_alias)
    scale=(0,1,2,127,128,254,255,17)[(pattern*3+1)%8]
    put(memory,STACK+phase+0x30,0xABCD0000|scale)
    args=(*args[:12],0xABCD0000|scale,args[13])
    data=table if table is not None else struct.pack('>14I',*screen.TARGETS)
    memory.update({screen.TABLE+i:b for i,b in enumerate(data)})
    return memory,args


def reference(memory,args,phase=0):
    after=memory.copy();trace=[];pointers=args[:4];home=STACK+phase
    def get(address,size=1):
        value=read(after,address,size);trace.append(('R',address,size,value));return value
    def store(address,value):
        put(after,address,value,2);trace.append(('W',address,2,value&65535))
    mode=get(home+0x37);scale=get(home+0x33)
    if mode<14:get(screen.TABLE+mode*4,4)
    if mode==0:
        store(pointers[3],0);zero=get(pointers[3],2)
        for i in (2,1,0):store(pointers[i],zero)
    elif mode in (7,8,12):
        store(pointers[2],0);zero=get(pointers[2],2)
        for i in (1,0):store(pointers[i],zero)
        store(pointers[3],get(home+(0x1F if mode==8 else 0x2F)))
    elif mode in (2,3,6,10,11,13):
        base=0x23 if mode in (10,11) else 0x13
        for i in range(3):store(pointers[i],get(home+base+i*4))
        if mode==13:store(pointers[3],0)
        else:store(pointers[3],get(home+(0x2F if mode in (6,10) else 0x1F)))
    else:
        if mode in (1,4,5,9):scale=get(home+0x33)
        for i in (2,1,0):store(pointers[i],scale)
        if mode==1:store(pointers[3],0)
        elif mode==9:store(pointers[3],get(home+0x2F))
        else:
            direct=get(home+0x2F);value=get(home+0x1F)
            store(pointers[3],value*direct>>8)
    return after,trace


class SecondaryOracle(OutputOracle):
    def __init__(self,words,memory,args,phase=0,entry=screen.ENTRY,connected=None):
        super().__init__(words,memory,args,phase,entry,connected)

    def record_call(self,target):
        assert target in (screen.ENTRY,first.ENTRY)
        self.calls.append((target,*self.arguments(14)))


class GameSecondaryOutputMatchTests(unittest.TestCase):
    run_host=native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        cls.output=cls.root/'conker/build/game-secondary-output-test';cls.output.mkdir(exist_ok=True)
        cls.record,cls.words=screen.compile_candidate(cls.root,cls.output,'selected')
        cls.rom=(cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail=list(struct.unpack_from('>120I',cls.rom,screen.ROM))
        address,data=screen.sections(cls.root/'conker/build/conker.us.elf')['.game_data']
        cls.original=data[screen.TABLE-address:screen.TABLE-address+56]
        start,vram,_,owners=load_game_data_layout(cls.root/'conker')
        assert cls.original==cls.rom[start+screen.TABLE-vram:start+screen.TABLE-vram+56]
        cls.table_owners=[o for o in owners if o['address']<screen.TABLE+56 and o['end']>screen.TABLE]
        cls.directory=tempfile.TemporaryDirectory();cls.addClassCleanup(cls.directory.cleanup);cls.path=Path(cls.directory.name)

    def receipt(self,name,report):
        (self.output/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')

    def test_complete_direct_slot_original_table_fourteen_positions_and_shared_cases(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences']),(120,0,0))
        self.assertEqual(self.words,self.retail);self.assertEqual(self.record['diagnostics'],'')
        self.assertEqual(self.record['table'][:14],list(screen.TARGETS));self.assertEqual(self.record['table'][14:],[0,0])
        self.assertEqual(self.original,struct.pack('>14I',*screen.TARGETS));self.assertEqual(len(self.table_owners),1)
        self.assertEqual(self.record['relocations'],{0x14:[('R_MIPS_HI16','.rodata')],0x1C:[('R_MIPS_LO16','.rodata')]})
        self.assertEqual(self.words[:2],[0x93AE0037,0x93A20033])
        self.receipt('slot',dict(words=120,direct=True,frame=0,arguments=14,table_bytes=56,
            padding=8,shared_cases=((2,3),(7,12)),separate_product_cases=(4,5),table_owners=self.table_owners))

    def test_guest_all_mode_bytes_patterns_output_aliases_full_memory_trace_and_registers(self):
        cases=0;coverage=[set(),set()]
        for mode,pattern,alias,phase in itertools.product(range(256),range(16),range(8),(0,8)):
            memory,args=fixture(mode,pattern,alias,phase);after,trace=reference(memory,args,phase)
            models=[]
            for i,words in enumerate((self.words,self.retail)):
                model=SecondaryOracle(words,memory,args,phase).run()
                self.assertEqual(model.memory,after);self.assertEqual(model.events,trace);self.assertEqual(model.calls,[])
                coverage[i].update(model.visits);models.append(model)
            self.assertEqual(models[0].r,models[1].r);cases+=1
        self.assertEqual([len(c) for c in coverage],[120,120])
        self.receipt('guest',dict(cases=cases,mode_bytes=256,patterns=16,aliases=8,phases=2,
            words_covered=120,full_memory=True,ordered_trace=True,registers_and_saved_state=True))

    def test_guest_argument_home_overlap_cached_scale_live_fourth_product_read_order(self):
        cases=0
        for mode,pattern,alias,phase in itertools.product(range(256),range(6),range(8),(0,8)):
            memory,args=fixture(mode,pattern,phase=phase,stack_alias=alias);after,trace=reference(memory,args,phase)
            for words in (self.words,self.retail):
                model=SecondaryOracle(words,memory,args,phase).run()
                self.assertEqual(model.memory,after);self.assertEqual(model.events,trace)
            cases+=1
        self.receipt('stack-alias',dict(cases=cases,live_input3=True,cached_scale=True,
            direct3_before_input3=True,mode_snapshot=True,ordered_trace=True,full_memory=True))

    def test_minimal_mapped_inputs_default_without_table_and_required_reads_fail_closed(self):
        checks=0
        for mode in range(256):
            memory,args=fixture(mode);required={0x37,0x33}
            if mode in (2,3,6,10,11,13):
                required.update((0x23,0x27,0x2B) if mode in (10,11) else (0x13,0x17,0x1B))
                if mode!=13:required.add(0x2F if mode in (6,10) else 0x1F)
            elif mode in (7,8,9,12):required.add(0x1F if mode==8 else 0x2F)
            elif mode in (4,5) or mode>=14:required.update((0x1F,0x2F))
            minimal={a:v for a,v in memory.items() if not STACK<=a<STACK+0x40 or a-STACK in required}
            if mode>=14:
                for i in range(56):del minimal[screen.TABLE+i]
            for words in (self.words,self.retail):SecondaryOracle(words,minimal,args).run()
            for offset in required:
                broken=minimal.copy();del broken[STACK+offset]
                for words in (self.words,self.retail):
                    with self.assertRaisesRegex(AssertionError,'unmapped'):SecondaryOracle(words,broken,args).run()
                checks+=1
        for mode in range(14):
            memory,args=fixture(mode);del memory[screen.TABLE+mode*4]
            with self.assertRaisesRegex(AssertionError,'unmapped'):SecondaryOracle(self.words,memory,args).run()
        memory,args=fixture(2);bad=list(args);bad[3]=0x12345678
        with self.assertRaisesRegex(AssertionError,'unmapped'):SecondaryOracle(self.words,memory,bad).run()
        self.receipt('reads',dict(mode_bytes=256,required_byte_negatives=checks,default_table_unmapped=True,
            no_unconditional_input0_read=True,selected_table_and_output_fail_closed=True))

    def test_live_seventh_argument_every_byte_and_high_word_poison(self):
        cases=0
        for mode,value,alias in itertools.product((2,3,4,5,8,11,14,255),range(256),(0,4)):
            memory,args=fixture(mode,3,alias);put(memory,STACK+0x1C,0x76543200|value)
            after,trace=reference(memory,args)
            for words in (self.words,self.retail):
                model=SecondaryOracle(words,memory,args).run()
                self.assertEqual(model.memory,after);self.assertEqual(model.events,trace)
                self.assertTrue(any(e[0]=='R' and e[1]==STACK+0x1F for e in model.events))
            cases+=1
        self.assertEqual(len({values(i) for i in range(16)}),16)
        self.receipt('live-input',dict(cases=cases,input3_bytes=256,high_word_poison=True,all_live_paths=True))

    def test_original_two_output_calls_staging_delays_object_modes_and_full_trace(self):
        fragment=list(struct.unpack_from('>50I',self.rom,0x1890C0))
        self.assertEqual(fragment[23:25],[0x0D451069,0xAFAE0034])
        self.assertEqual(fragment[48:],[0x0D4510BF,0xAFAE0034])
        fragment += [0x8FBF0044,0x03E00008,0]
        first_words=first.compile_candidate(self.root,self.output,'first-leaf')[1]
        first_retail=list(struct.unpack_from('>86I',self.rom,first.ROM));cases=0
        for mode,first_mode,pattern,phase in itertools.product(range(256),(0,1,2,3,4,5,6,255),range(2),(0,8)):
            memory,_=fixture(mode,pattern,phase=phase)
            memory.update({OBJECT+i:0xA5 for i in range(64)})
            inputs=values(pattern)
            for i,value in enumerate((*inputs,first_mode,mode)):put(memory,OBJECT+0x20+i,value,1)
            put(memory,STACK+phase+0x44,0xDEAD0000)
            after=memory.copy();expected=[];calls=[]
            for target,staged_values,offsets,ref in (
                (first.ENTRY,(*inputs,first_mode),(0x70,0x6E,0x6C,0x6A),first_reference),
                (screen.ENTRY,(*inputs,mode),(0x68,0x66,0x64,0x62),reference)):
                for i,value in enumerate(staged_values):
                    source=OBJECT+0x20+i+(1 if target==screen.ENTRY and i==9 else 0)
                    put(after,STACK+phase+0x10+i*4,value)
                    expected.extend((('R',source,1,value),('W',STACK+phase+0x10+i*4,4,value)))
                args=(*(STACK+phase+i for i in offsets),*staged_values)
                after,trace=ref(after,args,phase);expected+=trace;calls.append((target,*args))
            expected.append(('R',STACK+phase+0x44,4,0xDEAD0000))
            for left,right in ((first_words,self.words),(first_retail,self.retail)):
                connected={first.ENTRY+i*4:w for i,w in enumerate(left)}
                connected.update({screen.ENTRY+i*4:w for i,w in enumerate(right)})
                model=SecondaryOracle(fragment,memory,(),phase,0x1515BC10,connected)
                model.r[16]=model.before[16]=OBJECT;model.run()
                self.assertEqual(model.calls,calls);self.assertEqual(model.memory,after);self.assertEqual(model.events,expected)
            cases+=1
        self.receipt('caller',dict(cases=cases,original_words=50,two_connected_leaves=True,
            first_mode_object_offset=0x29,second_mode_object_offset=0x2A,both_delay_stores=True,
            full_memory=True,ordered_trace=True,earlier_context_and_return_seeded=True,whole_caller=False))

    def test_native_32_bit_all_modes_aliases_and_all_product_pairs(self):
        self.fixture='typedef unsigned char u8;typedef short s16;typedef unsigned int u32;\n'+screen.SELECTED+r'''
static const int aliases[8][4]={{0,1,2,3},{0,0,2,3},{0,1,1,3},{0,1,2,0},
    {0,0,0,0},{3,2,1,0},{1,1,1,0},{0,1,0,1}};
static s16 words[16],expected[16];
static int check(u32 *v,int alias) {
    s16 *p[4];int i,mode=(u8)v[9],scale=(u8)v[8],base;
    for(i=0;i<16;i++)words[i]=expected[i]=(s16)(0xA500u+i);
    for(i=0;i<4;i++)p[i]=expected+aliases[alias][i];
    if(mode==0) {*p[3]=0;*p[2]=*p[3];*p[1]=*p[2];*p[0]=*p[1];}
    else if(mode==7 || mode==8 || mode==12) {
        *p[2]=0;*p[1]=*p[2];*p[0]=*p[1];*p[3]=(u8)v[mode==8?3:7];
    } else if(mode==2 || mode==3 || mode==6 || mode==10 || mode==11 || mode==13) {
        base=(mode==10 || mode==11)?4:0;
        for(i=0;i<3;i++)*p[i]=(u8)v[base+i];
        *p[3]=mode==13?0:(u8)v[(mode==6 || mode==10)?7:3];
    } else {
        *p[2]=scale;*p[1]=scale;*p[0]=scale;
        *p[3]=mode==1?0:mode==9?(u8)v[7]:((u8)v[3]*(u8)v[7])/256;
    }
    func_151442FC(words+aliases[alias][0],words+aliases[alias][1],words+aliases[alias][2],words+aliases[alias][3],
        v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9]);
    for(i=0;i<16;i++)if(words[i]!=expected[i])return 1;
    return 0;
}
'''
        self.run_host(r'''
static const u8 edge[8]={0,1,2,127,128,254,255,17};
static const u8 products[4]={4,5,14,255};u32 v[10];int m,p,a,i,x,y;
if(sizeof(void *)!=4 || sizeof(s16)!=2)return 1;
for(m=0;m<256;m++)for(p=0;p<16;p++)for(a=0;a<8;a++) {
    for(i=0;i<9;i++) { v[i]=0xABCD0000u|edge[(p+i*(p<8?3:5))%8]; }
    v[8]=0xABCD0000u|edge[(p*3+1)%8];
    v[9]=0xABCD0000u|m;if(check(v,a))return 2;
}
for(x=0;x<256;x++)for(y=0;y<256;y++)for(m=0;m<4;m++)for(a=0;a<2;a++) {
    for(i=0;i<10;i++) { v[i]=0xABCD0080u; }
    v[3]=0xABCD0000u|x;v[7]=0xABCD0000u|y;v[9]=products[m];
    if(check(v,a?4:0))return 3;
}
''')
        self.receipt('native',dict(cases=557056,bits=32,all_modes=True,output_aliases=8,
            product_pairs=65536,typed_fourteen_input_calls=True,guest_home_aliases_not_claimed=True))

    def copied_owner(self):
        if hasattr(self.__class__,'copied'):return self.__class__.copied
        source=(self.root/'conker/src/game_16EE20.c').read_text()
        baseline=source.replace(screen.SELECTED,STUB).replace(screen.PROTOTYPE,'s32 func_151442FC();')
        self.assertIn(STUB,baseline)
        selected=baseline.replace('s32 func_151442FC();',screen.PROTOTYPE).replace(STUB,screen.SELECTED)
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

    def test_copied_owner_neighbors_pool_payload_padding_and_exact_new_table(self):
        old,new=self.copied_owner();ot,of,orr=parse_object(old);text,functions,rel=parse_object(new)
        self.assertEqual(set(functions),set(of));self.assertEqual(len(functions),89)
        for name,f in functions.items():
            if name==screen.FUNCTION:continue
            previous=of[name]
            self.assertEqual(text[f['value']:f['value']+f['size']],ot[previous['value']:previous['value']+previous['size']],name)
            self.assertEqual({o-f['value']:r for o,r in rel.items() if f['value']<=o<f['value']+f['size']},
                {o-previous['value']:r for o,r in orr.items() if previous['value']<=o<previous['value']+previous['size']},name)
        op,np=normalized_pools(old),normalized_pools(new)
        self.assertEqual(op['.data'],np['.data']);self.assertEqual(len(op['.rodata'][0]),656)
        self.assertEqual(len(np['.rodata'][0]),704);self.assertEqual(op['.rodata'][0][:644],np['.rodata'][0][:644])
        self.assertEqual(op['.rodata'][0][644:],bytes(12));self.assertEqual(np['.rodata'][0][644:],bytes(60))
        self.assertEqual(op['.rodata'][1],tuple(i for i in np['.rodata'][1] if i[0]<644))
        self.assertEqual(np['.rodata'][1][len(op['.rodata'][1]):],
            tuple((644+i*4,screen.FUNCTION,t-screen.ENTRY) for i,t in enumerate(screen.TARGETS)))
        f=functions[screen.FUNCTION];raw=list(struct.unpack_from('>120I',text,f['value']))
        self.assertEqual(raw[7],0x8C2E0284);raw[7]-=644
        standalone,_,_=parse_object(self.output/'selected.o');self.assertEqual(raw,list(struct.unpack_from('>120I',standalone)))
        self.receipt('owner',dict(functions=89,unchanged_neighbors=88,warnings=2,payload_retained=644,
            previous_pool=656,new_pool=704,table_offset=644,table_bytes=56,padding=4))

    def test_actual_padder_original_binding_alternate_carries_and_stale_guards(self):
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
        _,functions,rel=parse_object(obj);self.assertEqual(functions[screen.FUNCTION]['size'],480)
        self.assertEqual(rel,{0x14:[('R_MIPS_HI16',screen.ANCHOR)],0x1C:[('R_MIPS_LO16',screen.ANCHOR)]})
        for address in (screen.TABLE,0x81237FFC,0x81248004):
            subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'secondary-output.ld'),'-e',screen.FUNCTION,
                '--defsym=%s=0x%X'%(screen.ANCHOR,address),'-o',str(elf),str(obj)],check=True,capture_output=True)
            words=list(struct.unpack_from('>120I',screen.sections(elf)['.text'][1]))
            expected=self.retail.copy();expected[5]=expected[5]&0xFFFF0000|((address+0x8000)>>16)&65535
            expected[7]=expected[7]&0xFFFF0000|address&65535;self.assertEqual(words,expected)
        for field,value in (('expected','0x8C2E0288'),('expected_relocations','R_MIPS_LO16:D_800BE9E4')):
            broken=[dict(r) for r in rows];broken[-1][field]=value
            with self.assertRaisesRegex(ValueError,'stale'):emit(broken)
        self.receipt('padding',dict(words=120,guards=2,only_table_binding=True,alternate_carries=2,
            stale_words_and_relocations_fail=True,no_insertions_or_omissions=True))

    def test_profile_controls_and_compiled_behavior_or_read_negatives(self):
        controls=[]
        for profile in screen.PROFILES:
            record,words=screen.compile_candidate(self.root,self.output,'profile-'+profile,profile=profile);controls.append(record)
            table=struct.pack('>%dI'%len(record['table']),*record['table'])
            for mode,alias in itertools.product(range(256),(0,4)):
                memory,args=fixture(mode,3,alias,table=table);after,_=reference(memory,args)
                model=SecondaryOracle(words,memory,args).run()
                self.assertEqual({a:v for a,v in model.memory.items() if OUTPUT<=a<OUTPUT+32},
                    {a:v for a,v in after.items() if OUTPUT<=a<OUTPUT+32})
        forms={'full-mode':screen.SELECTED.replace('u8 mode','u32 mode'),
            'wrong-shift':screen.SELECTED.replace('>> 8','>> 7'),
            'wrong-fourth':screen.SELECTED.replace('*out3 = input3','*out3 = input2'),
            'wrong-scale':screen.SELECTED.replace('*out2 = scale','*out2 = input0'),
            'wrong-direct':screen.SELECTED.replace('*out0 = direct0','*out0 = direct1'),
            'zero-load-elision':screen.SELECTED.replace('*out3 = 0;\n        *out0 = *out1 = *out2 = *out3;',
                '*out3 = 0;\n        *out2 = 0;\n        *out1 = 0;\n        *out0 = 0;')}
        negatives={}
        for name,body in forms.items():
            self.assertNotEqual(body,screen.SELECTED);record,words=screen.compile_candidate(self.root,self.output,name,body)
            table=struct.pack('>%dI'%len(record['table']),*record['table']);detected=0
            for mode,pattern,alias in itertools.product(range(16),(3,4,5,8),(0,4)):
                memory,args=fixture(mode,pattern,alias,table=table);after,trace=reference(memory,args)
                model=SecondaryOracle(words,memory,args).run()
                public=lambda events:[e for e in events if OUTPUT<=e[1]<OUTPUT+32]
                detected+=(any(model.memory[a]!=v for a,v in after.items() if OUTPUT<=a<OUTPUT+32)
                    or public(model.events)!=public(trace))
            self.assertGreater(detected,0,name);negatives[name]=detected
        self.receipt('controls',dict(profiles=controls,profile_cases=2048,negative_detections=negatives,
            zero_elision_detected_by_reads=True,alternative_stack_schedules_unqualified=True))

    def test_production_complete_slot_original_table_and_guard_history(self):
        self.assertIn(screen.SELECTED,(self.root/'conker/src/game_16EE20.c').read_text())
        functions,_,addresses=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY);self.assertEqual(functions[screen.FUNCTION],self.retail)
        address,data=screen.sections(self.root/'conker/build/conker.us.elf')['.game_data']
        self.assertEqual(data[screen.TABLE-address:screen.TABLE-address+56],self.original)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:guards=list(csv.DictReader(stream))
        self.assertEqual(guards[10914:],screen.owner_guards())
        digest=hashlib.sha256(json.dumps(guards[:10914],sort_keys=True,separators=(',',':')).encode()).hexdigest()
        self.assertEqual(digest,'f2d0df124fdbc693c980d574463aca4b495160acfc37374fea3d4ae3a2482446')
        self.assertEqual(len(guards),10916)
        self.receipt('production',dict(words=120,direct=True,guards=10916,new_guards=2,prior_guards_sha256=digest))


if __name__=='__main__':unittest.main()
