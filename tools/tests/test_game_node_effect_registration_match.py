"""Effect handle lifecycle, finite coordinate narrowing and symbolic owner preservation."""

import csv
import itertools
import json
import math
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_node_effect_registration_candidates as screen
from tools.experiments import game_node_tile_scroll_candidates as scroll_screen
from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.tests import test_game_node_action_match as action
from tools.tests import test_game_node_tile_match as tile
from tools.tests import test_game_node_tile_scroll_match as scroll
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read

NODE, ACTOR = tile.NODE, tile.ACTOR
MODE, FREEZE = screen.SYMBOLS['D_800C35EA'], screen.SYMBOLS['D_800BEA0C']
SCROLL, UNREGISTER, CREATE, CALLBACK = (screen.SYMBOLS[n] for n in (
    'func_150334B8','func_1000FD38','func_1000FA64','func_15033BDC'))
ADDED_DECLARATIONS = 'extern u8 D_800BEA0C;\n'+screen.ALLOCATOR
HANDLES = (0, 1, 0xFF, 0x100, 0xFFFF, 0x80000000, 0x80000001, 0xFFFFFFFF)
RESULTS = (0, 1, 0x7FFF, 0x8000, 0xFFFE, 0xFFFF)
COORDINATES = (0, 0x80000000, 1, 0x80000001, bits(-1.75), bits(1.75),
    bits(-32768.75), bits(-32768), bits(32767.75), bits(32768), bits(-32769),
    bits(65535.75), bits(65536), bits(-65536.75), bits(2147483520), bits(-2147483648))


def fixture(mode=0, freeze=0, handle=0, coordinates=(bits(1.75), bits(-2.75), bits(32767.75)), selector=0):
    memory = scroll.fixture(selector=selector)
    memory.update({ACTOR+i:0xA5 for i in range(0x40)})
    put(memory,NODE+0x3C,handle)
    put(memory,MODE,mode,1)
    put(memory,FREEZE,freeze,1)
    for axis,value in enumerate(coordinates):
        put(memory,ACTOR+0x14+axis*4,value)
    return memory


def mutations(target, mode, node, actor, stack):
    if target == SCROLL:
        return {0: [], 1: [(MODE,1,1)],
            2: [(MODE,0,1),(FREEZE,0,1),(node+0x3C,0,4)],
            3: [(MODE,2,1),(FREEZE,0,1),(node+0x3C,0,4),(actor+0x14,bits(-17.75),4)],
            4: [], 5: [], 6: [(stack,0,4),(stack+4,0,4)]}[mode]
    if target == UNREGISTER and mode == 4:
        return [(node+0x3C,0x12345678,4),(FREEZE,0,1)]
    if target == CREATE and mode == 5:
        return [(node+0x3C,0x76543210,4),(stack,0,4),(stack+4,0,4)]
    return []


def narrowed(word):
    value = floating(word)
    assert math.isfinite(value) and -0x80000000 <= math.trunc(value) < 0x80000000
    low = math.trunc(value)&65535
    return (low if low < 32768 else low-65536)&0xFFFFFFFF


class EffectReference(action.ActionReference):
    def call(self,target,arguments,node,actor):
        self.calls.append((target,*arguments))
        if target != SCROLL:
            self.observed.append((target,self.get(node+0x3C)))
        if target == SCROLL and self.connected:
            saved_stack = self.stack
            self.stack -= 64
            scroll.ScrollReference.run(self,node,actor)
            self.stack = saved_stack
        for address,value,size in mutations(target,self.mode,node,actor,self.stack):
            self.put(address,value,size)
        return self.result if target == CREATE else 0xBEEF1234

    def run(self,node=NODE,actor=ACTOR,result=0,connected=False):
        self.result,self.connected,self.observed = result,connected,[]
        self.call(SCROLL,(node,actor),node,actor)
        if self.get(MODE,1) == 1:
            return 0
        if self.get(FREEZE,1):
            if self.get(node+0x3C):
                self.call(UNREGISTER,(CALLBACK,node,actor),node,actor)
            self.put(node+0x3C,0)
        elif not self.get(node+0x3C):
            xyz = tuple(narrowed(self.get(actor+0x14+i*4)) for i in range(3))
            handle = self.call(CREATE,(0x448,*xyz,32000,1000,500,CALLBACK,node,actor,0,0),node,actor)
            self.put(node+0x3C,handle|0x80000000)
        return 0


class EffectOracle(tile.TileOracle):
    def __init__(self,words,memory,args=(NODE,ACTOR),phase=0,mode=0,result=0,connected=None):
        TriangleOracle.__init__(self,words,memory,entry=screen.ENTRY,arguments=args,phase=phase,connected=connected)
        self.node,self.actor = args
        self.stack,self.mode,self.result = prior.STACK+phase,mode,result
        self.observed = []

    def record_call(self,target):
        self.calls.append((target,*self.arguments({SCROLL:2,UNREGISTER:3,CREATE:12}[target])))

    def hook(self,target):
        if target != SCROLL:
            self.observed.append((target,self.get(self.node+0x3C,4)))
        for address,value,size in mutations(target,self.mode,self.node,self.actor,self.stack):
            self.put(address,value,size)
        for register in (1,2,3,*range(4,16),24,25):
            self.r[register] = 0xA5000000+register
        self.r[2] = self.result if target == CREATE else 0xBEEF1234
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameNodeEffectRegistrationMatchTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-node-effect-registration-test'
        cls.out.mkdir(exist_ok=True)
        cls.record,cls.words = screen.compile_candidate(cls.root,cls.out,'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>68I',rom,screen.ROM))
        _,cls.scroll_words = scroll_screen.compile_candidate(cls.root,cls.out,'scroll-selected')
        cls.scroll_retail = list(struct.unpack_from('>68I',rom,scroll_screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self,name,value):
        (self.out / (name+'.json')).write_text(json.dumps(value,indent=2)+'\n')

    def compare(self,memory,args=(NODE,ACTOR),phase=0,mode=0,result=0,connected=False):
        reference = EffectReference(memory,phase,mode)
        expected = reference.run(*args,result,connected)
        models = []
        for body,helper in ((self.words,self.scroll_words),(self.retail,self.scroll_retail)):
            code = {SCROLL+i*4:word for i,word in enumerate(helper)} if connected else None
            model = EffectOracle(body,memory,args,phase,mode,result,code).run()
            self.assertEqual((model.r[2],model.calls,model.observed,prior.public(model.events),prior.external_memory(model.memory)),
                (expected,reference.calls,reference.observed,prior.public(reference.events),prior.external_memory(reference.memory)))
            models.append(model)
        self.assertEqual((models[0].r,models[0].f,models[0].events,models[0].memory),
            (models[1].r,models[1].f,models[1].events,models[1].memory))
        return models

    def test_01_complete_direct_slot_frame_and_symbolic_ownership(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],
            self.record['pool_bytes'],self.record['diagnostics']),(68,64,0,0,''))
        self.assertEqual(self.words,self.retail)
        relocations = [entry for entries in self.record['relocations'].values() for entry in entries]
        self.assertEqual(set(symbol for _,symbol in relocations),set(screen.SYMBOLS))
        self.assertEqual(sum(kind == 'R_MIPS_26' for kind,_ in relocations),3)
        self.assertEqual(sum(kind == 'R_MIPS_HI16' for kind,_ in relocations),4)
        self.assertEqual(sum(kind == 'R_MIPS_LO16' for kind,_ in relocations),4)
        self.receipt('slot',dict(words=68,frame=64,differences=0,generated_data_bytes=0,
            guards_added=0,padding_words=0,symbolic_call_relocations=3,symbolic_HI_LO_pairs=4))

    def test_02_all_global_bytes_handle_results_mutations_and_finite_coordinates(self):
        seen,globals_cases,gates,coordinates = set(),0,0,0
        for value,axis,handle,phase in itertools.product(range(256),('mode','freeze'),(0,0x80000001),(0,8)):
            for model in self.compare(fixture(handle=handle,**{axis:value}),phase=phase,result=0xFFFF):
                seen.update(model.visits)
            globals_cases += 1
        for global_mode,freeze,handle,result,mode,phase in itertools.product(
                (0,1,2,255),(0,1,255),HANDLES,RESULTS,range(7),(0,8)):
            for model in self.compare(fixture(global_mode,freeze,handle),phase=phase,mode=mode,result=result):
                seen.update(model.visits)
            gates += 1
        for words in itertools.product(COORDINATES,repeat=3):
            for model in self.compare(fixture(coordinates=words),result=0x1234):
                seen.update(model.visits)
            coordinates += 1
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY,screen.ENTRY+272,4))-seen)
        self.assertEqual(missing,[27])
        self.receipt('guest',dict(cases=globals_cases+gates+coordinates,global_axis_cases=globals_cases,
            gate_cases=gates,coordinate_cases=coordinates,each_global_all_256_bytes=True,
            handle_patterns=len(HANDLES),legal_u16_results=len(RESULTS),mutation_modes=7,SP_phases=2,
            finite_binary32_patterns=len(COORDINATES),missing_word_indices=missing,
            low_signed_halfword_after_finite_int32_truncation=True,
            independent_reference_public_effects_and_full_C_retail_GP_FP_traces_equal=True,
            invalid_FP_conversions_FCSR_and_full_callee_library_not_claimed=True))

    def test_03_connected_tile_scroll_precedes_global_gates_and_handle_lifecycle(self):
        cases = 0
        for selector,global_mode,freeze,handle,result,layout,phase in itertools.product(
                (0,0x37),(0,1,2),(0,1),(0,0x80000001),(0,0xFFFF),tile.LAYOUTS,(0,8)):
            memory = fixture(global_mode,freeze,handle,selector=selector)
            commands = scroll.fixture(selector=selector,s=0,t=91,end_s=62,end_t=62,layout=layout)
            for address in range(tile.COMMANDS,tile.COMMANDS+320):
                memory[address] = commands[address]
            self.compare(memory,phase=phase,result=result,connected=True)
            cases += 1
        lazy = fixture(mode=1,selector=0x37)
        put(lazy,tile.CONTAINER,0)
        del lazy[FREEZE],lazy[NODE+0x3C],lazy[ACTOR+0x14]
        self.compare(lazy,(NODE,0),connected=True)
        fault_addresses = (NODE+1,NODE+0x24,tile.CONTAINER,tile.COMMANDS,
            tile.COMMANDS+24,tile.COMMANDS+28)
        for missing in fault_addresses:
            memory = fixture(mode=1,selector=0x37)
            del memory[missing]
            reference = EffectReference(memory)
            with self.assertRaises(AssertionError) as failure:
                reference.run(connected=True)
            for body,helper in ((self.words,self.scroll_words),(self.retail,self.scroll_retail)):
                connected = {SCROLL+i*4:word for i,word in enumerate(helper)}
                model = EffectOracle(body,memory,connected=connected)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args,failure.exception.args)
                self.assertEqual((model.calls,prior.public(model.events),prior.external_memory(model.memory)),
                    (reference.calls,prior.public(reference.events),prior.external_memory(reference.memory)))
                self.assertEqual(model.calls,[(SCROLL,NODE,ACTOR)])
                self.assertFalse(any(event[1] in (MODE,FREEZE) for event in model.events))
        self.receipt('connected',dict(cases=cases,actual_C_and_retail_tile_scroll_connected=True,
            initial_scroll_runs_even_mode1_or_frozen=True,all_six_scan_layouts=True,
            null_command_lazy_case=1,helper_fault_prefixes=len(fault_addresses),
            malformed_scroll_faults_before_mode_or_freeze_read=True,
            complete_unregistration_allocator_and_callback_bodies_not_claimed=True))

    def test_04_lazy_storage_fault_prefixes_and_valid_aliases(self):
        lazy = []
        memory = fixture(mode=1)
        del memory[FREEZE],memory[NODE+0x3C],memory[ACTOR+0x14]
        lazy.append((memory,(NODE,0)))
        memory = fixture(freeze=1,handle=1)
        del memory[ACTOR+0x14]
        lazy.append((memory,(NODE,0)))
        memory = fixture(handle=1)
        del memory[ACTOR+0x14]
        lazy.append((memory,(NODE,0)))
        for memory,args in lazy:
            self.compare(memory,args)
        aliases = []
        memory = fixture()
        aliases.append((memory,(NODE,NODE)))
        for axis,value in enumerate((bits(-1.75),bits(2.75),bits(17.5))):
            put(memory,NODE+0x14+axis*4,value)
        memory = fixture()
        put(memory,ACTOR+0x3C,0)
        aliases.append((memory,(ACTOR,ACTOR)))
        memory = fixture()
        put(memory,MODE-0x3C+0x3C,0)
        put(memory,MODE,0,1)
        aliases.append((memory,(MODE-0x3C,ACTOR)))
        for memory,args in aliases:
            self.compare(memory,args)
        faults = []
        for missing in (MODE,FREEZE,NODE+0x3C,ACTOR+0x14,ACTOR+0x18,ACTOR+0x1C):
            memory = fixture()
            del memory[missing]
            faults.append((memory,(NODE,ACTOR)))
        faults.append((fixture(),(0,ACTOR)))
        faults.append((fixture(),(NODE,0)))
        for memory,args in faults:
            reference = EffectReference(memory)
            with self.assertRaises(AssertionError) as failure:
                reference.run(*args)
            for words in (self.words,self.retail):
                model = EffectOracle(words,memory,args)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args,failure.exception.args)
                self.assertEqual((model.calls,prior.public(model.events),prior.external_memory(model.memory)),
                    (reference.calls,prior.public(reference.events),prior.external_memory(reference.memory)))
        self.receipt('gates',dict(lazy_cases=len(lazy),aliases=len(aliases),fault_prefixes=len(faults),
            modeled_scroll_call_precedes_every_required_read=True,
            callback_handle_observation_and_post_callback_overwrite=True,arbitrary_private_aliases_not_claimed=True))

    def test_05_profiles_and_effective_semantic_negatives(self):
        memories = [fixture(mode=m,freeze=f,handle=h,coordinates=coords) for m,f,h,coords in (
            (0,0,0,(bits(-17.75),bits(2.75),bits(32768))),
            (2,0,0,(bits(1),bits(-2),bits(3))),
            (0,1,1,(bits(1),bits(2),bits(3))),
            (0,0,0x80000000,(bits(1),bits(2),bits(3))))]
        records,ordinary,negatives = [],0,0
        forms = [(n,b,'o2g3') for n,b in screen.candidates()]
        forms += [('profile-'+p,screen.SELECTED,p) for p in PROFILES if p != 'o2g3']
        for name,body,profile in forms:
            record,words = screen.compile_candidate(self.root,self.out,name,body,profile)
            records.append(record)
            caught = False
            for memory in memories:
                if not name.startswith('negative-') and any(not -32768 <= math.trunc(
                        floating(read(memory,ACTOR+0x14+i*4))) <= 32767 for i in range(3)):
                    continue
                reference = EffectReference(memory)
                expected = reference.run(result=0x1234)
                model = EffectOracle(words,memory,result=0x1234).run()
                observed = (model.r[2],model.calls,model.observed,prior.external_memory(model.memory))
                required = (expected,reference.calls,reference.observed,prior.external_memory(reference.memory))
                if name.startswith('negative-'):
                    caught |= observed != required
                else:
                    self.assertEqual(observed,required,name)
                    ordinary += 1
            if name.startswith('negative-'):
                self.assertTrue(caught,name)
                negatives += 1
        self.receipt('controls',dict(forms=len(records),ordinary_executions=ordinary,
            effective_semantic_negatives=negatives,measurements=records,
            implicit_narrowing_control_is_not_a_negative=True,ordinary_defined_float_to_s16_range_only=True,
            alternate_private_traces_not_claimed=True))

    def test_06_actual_native32_complete_C_all_handle_results_and_canaries(self):
        self.fixture = r'''typedef unsigned char u8;typedef unsigned short u16;typedef short s16;
typedef int s32;typedef unsigned int u32;typedef float f32;
typedef union __attribute__((aligned(8))) {u32 align;u8 b[0x40];} Storage;
typedef char widths[(sizeof(void *)==4&&sizeof(s16)==2&&sizeof(f32)==4)?1:-1];
static Storage node,actor;u8 D_800C35EA,D_800BEA0C;
static u16 result;static int count,error,mutation,want_mode;static int calls[3];
static s16 expected_xyz[3];static u32 observed;
static u8 seen_results[65536],seen_coordinates[65536];
s32 func_15033BDC(){return 0;}
s32 func_150334B8(u8 *n,u8 *a){calls[count++]=1;if(n!=node.b||a!=actor.b)error=1;
    if(mutation==1)D_800C35EA=1;
    return -1;
}
void func_1000FD38(s32 (*callback)(),u8 *n,u8 *a){calls[count++]=2;
    if(callback!=func_15033BDC||n!=node.b||a!=actor.b)error=2;
    observed=*(u32 *)(node.b+0x3C);*(u32 *)(node.b+0x3C)=0x12345678;
}
u16 func_1000FA64(u16 effect,s16 x,s16 y,s16 z,s32 amount,u16 rate,s16 limit,s32 callback,
    void *n,s32 a,s32 extra,s32 tail){calls[count++]=3;
    if(effect!=0x448||x!=expected_xyz[0]||y!=expected_xyz[1]||z!=expected_xyz[2]||
        amount!=32000||rate!=1000||limit!=500||callback!=(s32)func_15033BDC||
        n!=node.b||a!=(s32)actor.b||extra||tail)error=3;
    seen_results[result]=1;seen_coordinates[(u16)x]=1;
    observed=*(u32 *)(node.b+0x3C);*(u32 *)(node.b+0x3C)=0x76543210;return result;
}
''' + screen.SELECTED
        self.run_host(r'''
static u32 handles[4]={0,1,0x80000000,0xFFFFFFFF};
Storage old_node,old_actor;u32 expected;int v,i,l,g,f,callback;f32 value;
for(v=0;v<65536;v++)for(l=0;l<4;l++)for(g=0;g<3;g++)for(f=0;f<2;f++){
    for(i=0;i<0x40;i++)node.b[i]=actor.b[i]=0xA5;
    expected_xyz[0]=(s16)(v-32768);expected_xyz[1]=(s16)(32767-v);expected_xyz[2]=17;
    for(i=0;i<3;i++){value=(f32)expected_xyz[i]+(expected_xyz[i]<0?-0.25f:0.25f);
        *(f32 *)(actor.b+0x14+i*4)=value;}
    *(u32 *)(node.b+0x3C)=handles[l];D_800C35EA=g;D_800BEA0C=f;
    result=(u16)v;mutation=l==3?1:0;count=error=0;observed=0;
    want_mode=mutation==1?1:g;
    callback=want_mode==1?0:f?(handles[l]?2:0):handles[l]?0:3;
    expected=want_mode==1?handles[l]:f?0:handles[l]?handles[l]:((u32)result|0x80000000);
    old_node=node;old_actor=actor;
    if(func_150339C8(node.b,actor.b)!=0||error||count!=(callback?2:1)||calls[0]!=1)return 1;
    if(callback&&(calls[1]!=callback||observed!=(callback==2?handles[l]:0)))return 2;
    *(u32 *)(old_node.b+0x3C)=expected;
    for(i=0;i<0x40;i++)if(node.b[i]!=old_node.b[i]||actor.b[i]!=old_actor.b[i])return 3;
}
for(v=0;v<65536;v++)if(!seen_results[v]||!seen_coordinates[v])return 4;
''')
        self.receipt('native',dict(cases=1572864,actual_complete_C=True,pointer_bytes=4,
            all_u16_results_observed_in_create=65536,all_signed16_coordinates_observed_in_create=65536,
            all_input_canaries_and_callback_ABI_checked=True,post_callback_handle_overwrite=True,
            axes_correlated=True,outside_defined_float_to_s16_native_range_not_claimed=True,
            scroll_and_original_allocator_are_controlled_hooks=True))

    def test_07_copied_owner_padder_and_symbol_carry_rebases(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        if screen.SELECTED in source:
            source = source.replace(screen.SELECTED,screen.STUB).replace(ADDED_DECLARATIONS+'\n','',1)
        self.assertEqual(source.count(screen.STUB),1)
        selected = source.replace(screen.STUB,screen.SELECTED).replace('#include <ultra64.h>\n',
            '#include <ultra64.h>\n'+ADDED_DECLARATIONS+'\n',1)
        objects = []
        for name,body in (('baseline',source),('selected',selected)):
            obj,warnings = compile_owner(self.root,self.out,body,'owner-'+name)
            self.assertEqual(warnings,[])
            processed = self.out / ('owner-'+name+'-postprocessed.o')
            shutil.copyfile(obj,processed)
            subprocess.run([sys.executable,str(self.root / 'tools/asm-processor/asm_processor.py'),'-O2','-g3',
                str((self.out / ('owner-'+name+'.c')).relative_to(self.root / 'conker')),'--post-process',
                str(processed.relative_to(self.root / 'conker')),'--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude','include/asm_processor_prelude.inc'],cwd=self.root / 'conker',check=True,capture_output=True)
            objects.append(processed)
        old,previous,old_rel = parse_object(objects[0])
        text,current,rel = parse_object(objects[1])
        self.assertEqual(current.keys(),previous.keys())
        for name,function in current.items():
            if name == screen.FUNCTION:
                continue
            before = previous[name]
            self.assertEqual(text[function['value']:function['value']+function['size']],
                old[before['value']:before['value']+before['size']],name)
            self.assertEqual({o-function['value']:r for o,r in rel.items() if function['value'] <= o < function['value']+function['size']},
                {o-before['value']:r for o,r in old_rel.items() if before['value'] <= o < before['value']+before['size']},name)
        self.assertEqual(normalized_pools(objects[0]),normalized_pools(objects[1]))
        target = current[screen.FUNCTION]
        isolated,_,isolated_rel = parse_object(self.out / 'selected.o')
        self.assertEqual(text[target['value']:target['value']+272],isolated[:272])
        self.assertEqual({o-target['value']:r for o,r in rel.items() if target['value'] <= o < target['value']+272},isolated_rel)
        assembly = emit_padded_assembly(objects[1],self.root / 'conker/asm/5D2C0.s',
            word_patches_path=self.root / 'conker/retail_word_patches.us.csv',filename='generated_5D2C0',rodata_symbol=action.ANCHOR)
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION,screen.FUNCTION),start)
        end = assembly.index('\n',end)+1
        self.assertNotIn('.space',assembly[end:assembly.find('.type ',end)])
        asm,obj = self.out / 'padded.s',self.out / 'padded.o'
        asm.write_text('.text\n.set noreorder\n.globl %s\n' % screen.FUNCTION+assembly[start:end])
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(obj),str(asm)],check=True,capture_output=True)
        _,functions,relocations = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'],272)
        self.assertEqual(relocations,isolated_rel)
        self.assertNotIn('.rodata',sections(obj))
        bindings = [(screen.ENTRY,dict(screen.SYMBOLS)),(screen.ENTRY+0x01000004,dict(screen.SYMBOLS))]
        for name in screen.SYMBOLS:
            symbols = dict(screen.SYMBOLS)
            symbols[name] += 0x8004 if name.startswith('D_') or name == 'func_15033BDC' else 0x01000000
            bindings.append((screen.ENTRY,symbols))
        for index,(entry,symbols) in enumerate(bindings):
            script,elf = self.out / 'padded.ld',self.out / ('rebased-%d.elf' % index)
            script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
            subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',screen.FUNCTION,
                *['--defsym=%s=0x%X' % item for item in symbols.items()],'-o',str(elf),str(obj)],check=True,capture_output=True)
            required = self.words.copy()
            for offset,entries in relocations.items():
                self.assertEqual(len(entries),1)
                kind,symbol = entries[0]
                address = symbols[symbol]
                word = required[offset//4]
                required[offset//4] = word&0xFC000000 | (address>>2)&0x3FFFFFF if kind == 'R_MIPS_26' else (
                    word&0xFFFF0000 | ((address+0x8000)>>16)&65535 if kind == 'R_MIPS_HI16' else word&0xFFFF0000 | address&65535)
                self.assertIn(kind,('R_MIPS_26','R_MIPS_HI16','R_MIPS_LO16'))
            self.assertEqual(list(struct.unpack_from('>68I',sections(elf)['.text'][1])),required)
        self.receipt('owner-padder',dict(functions=len(current),unchanged_neighbors=len(current)-1,
            pools_and_relative_relocations_unchanged=True,strict_diagnostics=0,
            slot_no_padding_or_generated_data=True,independent_entry_symbol_links=len(bindings),
            all_six_symbols_rebased_independently=True,signed_LO_carry_cases=3))

    def test_08_installed_or_previous_stub_and_guard_history(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        installed = screen.SELECTED in source
        self.assertEqual(source.count(screen.SELECTED if installed else screen.STUB),1)
        functions,_,addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        expected = self.words if installed else [0x00001025,0x03E00008]+[0]*66
        self.assertEqual((addresses[screen.FUNCTION],functions[screen.FUNCTION]),(screen.ENTRY,expected))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self,guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed',dict(installed=installed,byte_exact=installed,guards_added=0))


if __name__ == '__main__':
    unittest.main()
