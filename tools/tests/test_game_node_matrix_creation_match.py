"""Matrix creation ABI, live argument homes and connected six-float setup."""

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

from tools.experiments import game_node_matrix_creation_candidates as screen
from tools.experiments import game_node_transform_setup_candidates as setup
from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.tests import test_game_node_action_match as action
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read

NODE, ACTOR, ALT_ACTOR, CREATED = 0x10000, 0x20000, 0x21000, 0x30000
BANK, ALT_BANK, VALUES, EXTRA = 0x40000, 0x50000, 0x60000, 0x61000
ALLOCATE = 0x10003C40
CREATE, CONVERT, INVERT, BUILD, MULTIPLY, DECOMPOSE, ATTACH = (
    screen.SYMBOLS[name] for name in ('func_15083568','guMtxL2F','func_15048B10',
        'func_150A9B0C','func_150A7A48','func_1503E5F8','func_15030D54'))
WIDTHS = {CREATE:4, CONVERT:2, INVERT:2, BUILD:7, MULTIPLY:3, DECOMPOSE:10, ATTACH:7, ALLOCATE:4}
FLOATS = (0,0x80000000,1,0x80000001,0x00800000,0x80800000,0x3F800000,0xBF800000,
    0x7F7FFFFF,0xFF7FFFFF,0x7F800000,0xFF800000,0x7FC00001,0xFFC12345,0x7F800001)
INDICES = (0,1,2,255,256,0xFFFFFFFF,0x80000001)


def fixture(index=1, flags=0xA5, bank=True, value=0x3F800000, phase=0):
    memory = {prior.STACK+i:0xA5 for i in range(-0x600,0x140)}
    for base,length in ((NODE,0x200),(ACTOR,0x220),(ALT_ACTOR,0x220),
            (CREATED,0x100),(VALUES,64),(EXTRA,160)):
        memory.update({base+i:0xA5 for i in range(length)})
    for actor,matrix in ((ACTOR,BANK),(ALT_ACTOR,ALT_BANK)):
        put(memory,actor+0x1D4,matrix if bank else 0)
        for slot in set((0,1,index,0x101)):
            address = (matrix+slot*64)&0xFFFFFFFF
            for word in range(16):
                put(memory,address+word*4,(value+word*19)&0xFFFFFFFF)
    for offset in (0x14,0x18,0x1C,0x40,0xB8,0xC4,0x14C,0x150):
        put(memory,NODE+offset,value)
    put(memory,CREATED+0x16,flags,1)
    put(memory,CREATED+0x34,0)
    return memory


def mutations(target,mode,caller):
    if mode == 1 and target == CREATE:
        return [(caller+4,ALT_ACTOR,4),(caller+12,0x101,4),(NODE+0x14C,0xBF800000,4)]
    if mode == 2 and target == BUILD:
        return [(NODE+0x14,0x80000000,4),(NODE+0x18,0x7FC00001,4),(NODE+0x1C,1,4)]
    if mode == 3 and target == DECOMPOSE:
        return [(caller+20,1,4)]
    return []


def allocation_mutations(index,mode,caller,node):
    if index != 0:
        return []
    if mode == 1:
        return [(caller+4,0x80000000,4),(caller+16,0x7FC00001,4)]
    if mode == 2:
        return [(node+0x34,EXTRA,4)]
    if mode == 3:
        return [(node+0x34,0,4)]
    return []


def callback_effects(model,target,args,value):
    if target == CONVERT:
        data = [model.get(args[1]+i*4,4) for i in range(16)]
        for i,word in enumerate(data):
            model.put(args[0]+i*4,word,4)
    elif target == INVERT:
        data = [model.get(args[0]+i*4,4) for i in range(16)]
        for i,word in enumerate(reversed(data)):
            model.put(args[1]+i*4,word,4)
    elif target == BUILD:
        for i in range(16):
            model.put(args[0]+i*4,args[1+i%6],4)
    elif target == MULTIPLY:
        first = [model.get(args[0]+i*4,4) for i in range(16)]
        last = [model.get(args[1]+i*4,4) for i in range(16)]
        for i in range(16):
            model.put(args[2]+i*4,first[i]^last[15-i],4)
    elif target == DECOMPOSE:
        for i in range(16):
            model.get(args[0]+i*4,4)
        for i,address in enumerate(args[1:]):
            model.put(address,(value+i*0x10001)&0xFFFFFFFF,4)


class Reference(action.ActionReference):
    def __init__(self,memory,phase=0,mode=0,result=CREATED,value=0x3F800000,allocations=(VALUES,EXTRA)):
        super().__init__(memory,phase,mode)
        self.result,self.value,self.allocations = result,value,allocations
        self.caller,self.allocated = self.stack,0

    def call(self,target,args):
        self.calls.append((target,*args))
        callback_effects(self,target,args,self.value)
        for address,value,size in mutations(target,self.mode,self.caller):
            self.put(address,value,size)
        return self.result if target == CREATE else 0xBEEF0000+len(self.calls)

    def allocate(self,args,node,caller):
        self.calls.append((ALLOCATE,*args))
        for address,value,size in allocation_mutations(self.allocated,self.mode,caller,node):
            self.put(address,value,size)
        result = self.allocations[self.allocated]
        self.allocated += 1
        return result

    def attach(self,node,values,caller):
        for i,value in enumerate(values):
            self.put(caller+4+i*4,value)
        result = self.allocate((24,1,0,2),node,caller)
        self.put(node+0x44,result)
        if result:
            for i in range(6):
                destination = result if i == 0 else self.get(node+0x44)
                value = self.get(caller+4+i*4)
                self.put(destination+i*4,value)
            if self.get(node+0x34) == 0:
                result = self.allocate((128,1,2,2),node,caller)
                self.put(node+0x34,result)
        return result

    def run(self,args,connected=False):
        node,actor,kind,index,clear,zero = args
        for i,value in enumerate((actor,kind,index),1):
            self.put(self.caller+i*4,value)
        source_actor = self.get(self.caller+4)
        call_actor = self.get(self.caller+4)
        call_kind = self.get(self.caller+8)
        if self.get(source_actor+0x1D4) == 0:
            return 0
        created = self.call(CREATE,(call_actor,call_kind,0x3F800000,0))
        index = self.get(self.caller+12)
        frame = self.caller-0x168
        self.put(frame+0x164,created)
        if not created:
            return 0
        self.put(created+2,index,1)
        self.put(created+0x40,self.get(node+0x14C))
        clear = self.get(self.caller+16)
        flag = self.get(created+0x16,1)
        self.put(created+0x16,flag&~4 if clear else flag|4,1)
        actor = self.get(self.caller+4)
        bank = self.get(actor+0x1D4)
        converted,inverse,transform,combined = (frame+o for o in (0x124,0xE4,0xA4,0x64))
        self.call(CONVERT,(converted,(bank+index*64)&0xFFFFFFFF))
        self.call(INVERT,(converted,inverse))
        scale = self.get(node+0x14C)
        x,y,z = (self.get(node+o) for o in (0xB8,0x40,0xC4))
        vertical = self.get(node+0x150)
        self.call(BUILD,(transform,x,y,z,scale,vertical,scale))
        for offset,field in ((0x30,0x14),(0x34,0x18),(0x38,0x1C)):
            self.put(transform+offset,self.get(node+field))
        for offset in (0xC,0x1C,0x2C):
            self.put(transform+offset,0)
        self.put(transform+0x3C,0x3F800000)
        self.call(MULTIPLY,(transform,inverse,combined))
        destinations = tuple(frame+o for o in (0x60,0x5C,0x58,0x48,0x44,0x40,0x54,0x50,0x4C))
        self.call(DECOMPOSE,(combined,*destinations))
        if self.get(self.caller+20):
            for address in reversed(destinations[:3]):
                self.put(address,0)
        angles = tuple(self.get(a) for a in destinations[3:6])
        created = self.get(frame+0x164)
        position = tuple(self.get(a) for a in destinations[:3])
        self.call(ATTACH,(created,*position,*angles))
        if connected:
            self.attach(created,(*position,*angles),frame)
        return self.get(frame+0x164)


class CreationOracle(TriangleOracle):
    def __init__(self,words,memory,args,entry=screen.ENTRY,phase=0,mode=0,result=CREATED,
            value=0x3F800000,allocations=(VALUES,EXTRA),connected=None):
        super().__init__(words,memory,entry=entry,arguments=args,phase=phase)
        self.caller,self.mode,self.result,self.value = prior.STACK+phase,mode,result,value
        self.allocations,self.allocated,self.node = allocations,0,args[0]
        self.code.update(connected or {})

    def record_call(self,target):
        self.calls.append((target,*self.arguments(WIDTHS[target])))

    def hook(self,target):
        args = self.calls[-1][1:]
        if target == ALLOCATE:
            caller = self.caller if self.entry == setup.ENTRY else self.caller-0x168
            node = self.node if self.entry == setup.ENTRY else self.result
            for address,value,size in allocation_mutations(self.allocated,self.mode,caller,node):
                self.put(address,value,size)
            result = self.allocations[self.allocated]
            self.allocated += 1
        else:
            callback_effects(self,target,args,self.value)
            for address,value,size in mutations(target,self.mode,self.caller):
                self.put(address,value,size)
            result = self.result if target == CREATE else 0xBEEF0000+len(self.calls)
        for register in (1,2,3,*range(4,16),24,25):
            self.r[register] = 0xA5000000+register
        self.r[2] = result
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameNodeMatrixCreationMatchTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-node-matrix-creation-test'
        cls.out.mkdir(exist_ok=True)
        cls.record,cls.words = screen.compile_candidate(cls.root,cls.out,'selected')
        cls.setup_record,cls.setup_words = setup.compile_candidate(cls.root,cls.out,'setup-selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>113I',rom,screen.ROM))
        cls.setup_retail = list(struct.unpack_from('>45I',rom,setup.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self,name,value):
        (self.out / (name+'.json')).write_text(json.dumps(value,indent=2)+'\n')

    def compare(self,memory,args,phase=0,mode=0,result=CREATED,value=0x3F800000,
            allocations=(VALUES,EXTRA),connected=False):
        initial = dict(memory)
        for i,arg in enumerate(args[4:]):
            put(initial,prior.STACK+phase+16+i*4,arg)
        ref = Reference(initial,phase,mode,result,value,allocations)
        expected = ref.run(args,connected)
        models = []
        for words,callee in ((self.words,self.setup_words),(self.retail,self.setup_retail)):
            code = dict(zip(range(setup.ENTRY,setup.ENTRY+180,4),callee)) if connected else None
            model = CreationOracle(words,initial,args,phase=phase,mode=mode,result=result,value=value,
                allocations=allocations,connected=code).run()
            self.assertEqual((model.r[2],model.calls,prior.public(model.events),prior.external_memory(model.memory)),
                (expected,ref.calls,prior.public(ref.events),prior.external_memory(ref.memory)))
            models.append(model)
        self.assertEqual((models[0].r,models[0].f,models[0].events,models[0].memory),
            (models[1].r,models[1].f,models[1].events,models[1].memory))
        return models

    def test_01_both_direct_slots_frames_and_symbolic_calls(self):
        for record,words,retail,count,frame in ((self.record,self.words,self.retail,113,0x168),
                (self.setup_record,self.setup_words,self.setup_retail,45,0x20)):
            self.assertEqual((record['body_words'],record['frame'],record['differences'],record['pool_bytes']),
                (count,frame,0,0))
            self.assertEqual(words,retail)
            self.assertTrue(all(kind == 'R_MIPS_26' for entries in record['relocations'].values() for kind,_ in entries))
        self.receipt('slots',dict(caller_words=113,caller_frame=0x168,setup_words=45,setup_frame=0x20,
            raw_differences=0,guards_added=0,generated_data_bytes=0))

    def test_02_all_flag_bytes_signed_indices_home_mutations_float_patterns_and_coverage(self):
        seen,cases = set(),0
        for flags,clear,zero,result,phase in itertools.product(range(256),(0,1,0xFFFFFFFF),
                (0,1,0x80000000),(0,CREATED),(0,8)):
            for model in self.compare(fixture(flags=flags), (NODE,ACTOR,0x80000001,1,clear,zero),phase=phase,result=result):
                seen.update(model.visits)
            cases += 1
        for index,value,mode,phase in itertools.product(INDICES,FLOATS,range(4),(0,8)):
            for model in self.compare(fixture(index=index,value=value), (NODE,ACTOR,0xFFFFFFFF,index,1,0),
                    phase=phase,mode=mode,value=value):
                seen.update(model.visits)
            cases += 1
        for phase in (0,8):
            for model in self.compare(fixture(bank=False),(NODE,ACTOR,1,0,1,0),phase=phase):
                seen.update(model.visits)
            cases += 1
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY,screen.ENTRY+452,4))-seen)
        self.assertEqual(missing,[31])
        self.receipt('caller-guest',dict(cases=cases,flag_bytes=256,index_patterns=len(INDICES),
            float_patterns=len(FLOATS),callback_modes=4,SP_phases=2,missing_word_indices=missing,
            missing_only_unreachable_branch_likely_duplicate_loads=True,
            defined_return_call_ABI_public_trace_memory_and_complete_C_retail_GP_FP_equal=True,
            callback_matrix_bodies_are_controlled_not_complete_callees=True))

    def test_03_setup_allocation_failures_live_float_homes_aliases_and_complete_coverage(self):
        seen,cases = set(),0
        for value,bank,first,last,mode,phase in itertools.product(FLOATS,(0,EXTRA),(0,VALUES),
                (0,EXTRA),range(4),(0,8)):
            memory = fixture(value=value)
            put(memory,NODE+0x34,bank)
            args = (NODE,*((value+i*0x10001)&0xFFFFFFFF for i in range(6)))
            for i,arg in enumerate(args[4:]):
                put(memory,prior.STACK+phase+16+i*4,arg)
            ref = Reference(memory,phase,mode,allocations=(first,last))
            ref.attach(NODE,args[1:],prior.STACK+phase)
            models = [CreationOracle(words,memory,args,entry=setup.ENTRY,phase=phase,mode=mode,
                allocations=(first,last)).run() for words in (self.setup_words,self.setup_retail)]
            for model in models:
                seen.update(model.visits)
                self.assertEqual((model.calls,prior.public(model.events),prior.external_memory(model.memory)),
                    (ref.calls,prior.public(ref.events),prior.external_memory(ref.memory)))
            self.assertEqual((models[0].r,models[0].f,models[0].events,models[0].memory),
                (models[1].r,models[1].f,models[1].events,models[1].memory))
            cases += 1
        memory = fixture()
        put(memory,NODE+0x34,EXTRA)
        args = (NODE,0x3F800000,VALUES-8,0x40000000,0x40400000,0x40800000,0x40A00000)
        for i,arg in enumerate(args[4:]):
            put(memory,prior.STACK+16+i*4,arg)
        ref = Reference(memory,allocations=(NODE+0x40,EXTRA))
        ref.attach(NODE,args[1:],prior.STACK)
        for words in (self.setup_words,self.setup_retail):
            model = CreationOracle(words,memory,args,entry=setup.ENTRY,allocations=(NODE+0x40,EXTRA)).run()
            self.assertEqual((model.calls,prior.public(model.events),prior.external_memory(model.memory)),
                (ref.calls,prior.public(ref.events),prior.external_memory(ref.memory)))
        missing = sorted((pc-setup.ENTRY)//4 for pc in set(range(setup.ENTRY,setup.ENTRY+180,4))-seen)
        self.assertEqual(missing,[])
        self.receipt('setup-guest',dict(cases=cases+1,float_patterns=len(FLOATS),allocation_modes=4,
            SP_phases=2,alias_redirects_after_y_store=True,missing_word_indices=missing,
            allocation_failures_required_rereads_and_complete_C_retail_GP_FP_equal=True))

    def test_04_lazy_gates_required_fault_prefixes_and_connected_setup(self):
        cases = 0
        for value,clear,zero,first,last,phase in itertools.product(FLOATS,(0,1),(0,1),
                (0,VALUES),(0,EXTRA),(0,8)):
            self.compare(fixture(value=value),(NODE,ACTOR,0x17,1,clear,zero),phase=phase,value=value,
                allocations=(first,last),connected=True)
            cases += 1
        lazy = fixture(bank=False)
        for address in range(NODE,NODE+0x200):
            del lazy[address]
        self.compare(lazy,(NODE,ACTOR,1,0,1,0))
        lazy = fixture()
        for address in range(NODE,NODE+0x200):
            del lazy[address]
        self.compare(lazy,(NODE,ACTOR,1,0,1,0),result=0)
        fault_addresses = (ACTOR+0x1D4,CREATED+2,NODE+0x14C,CREATED+0x40,CREATED+0x16,
            BANK+64,NODE+0xB8,NODE+0x40,NODE+0xC4,NODE+0x150,NODE+0x14,NODE+0x18,NODE+0x1C)
        for address in fault_addresses:
            memory = fixture()
            put(memory,prior.STACK+16,1)
            put(memory,prior.STACK+20,0)
            del memory[address]
            args = (NODE,ACTOR,1,1,1,0)
            ref = Reference(memory)
            with self.assertRaises(AssertionError) as failure:
                ref.run(args)
            for words in (self.words,self.retail):
                model = CreationOracle(words,memory,args)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args,failure.exception.args)
                self.assertEqual((model.calls,prior.public(model.events),prior.external_memory(model.memory)),
                    (ref.calls,prior.public(ref.events),prior.external_memory(ref.memory)))
        setup_args = (NODE,0x3F800000,0x40000000,0x40400000,0x40800000,0x40A00000,0x40C00000)
        for missing in (NODE+0x44,VALUES,VALUES+4,VALUES+8,VALUES+0xC,VALUES+0x14,NODE+0x34):
            memory = fixture()
            for i,arg in enumerate(setup_args[4:]):
                put(memory,prior.STACK+16+i*4,arg)
            del memory[missing]
            ref = Reference(memory)
            with self.assertRaises(AssertionError) as failure:
                ref.attach(NODE,setup_args[1:],prior.STACK)
            for words in (self.setup_words,self.setup_retail):
                model = CreationOracle(words,memory,setup_args,entry=setup.ENTRY)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args,failure.exception.args)
                self.assertEqual((model.calls,prior.public(model.events),prior.external_memory(model.memory)),
                    (ref.calls,prior.public(ref.events),prior.external_memory(ref.memory)))
        memory = fixture()
        del memory[NODE+0x34]
        for address in range(VALUES,VALUES+64):
            del memory[address]
        for words in (self.setup_words,self.setup_retail):
            model = CreationOracle(words,memory,setup_args,entry=setup.ENTRY,allocations=(0,EXTRA)).run()
            self.assertEqual(model.calls,[(ALLOCATE,24,1,0,2)])
            self.assertEqual(read(model.memory,NODE+0x44),0)
        self.receipt('connected',dict(cases=cases,actual_C_and_retail_setup_words_connected=True,
            lazy_gates=3,required_faults=len(fault_addresses)+7,caller_faults=len(fault_addresses),setup_faults=7,
            ordered_prefixes_equal=True,
            allocation_wrapper_and_matrix_library_bodies_not_claimed=True))

    def test_05_profile_controls_and_effective_semantic_negatives(self):
        records,ordinary,negatives = [],0,0
        for module in (screen,setup):
            forms = [(n,b,'o2g3') for n,b in module.candidates()]
            forms += [('profile-'+p,module.SELECTED,p) for p in PROFILES if p != 'o2g3']
            for name,body,profile in forms:
                record,words = module.compile_candidate(self.root,self.out,module.FUNCTION+'-'+name,body,profile)
                records.append(record)
                caught = False
                for mode in (0,1,2,3):
                    memory = fixture(index=256)
                    if module is screen:
                        args = (NODE,ACTOR,0x17,256,1,1)
                        put(memory,prior.STACK+16,1)
                        put(memory,prior.STACK+20,1)
                        ref = Reference(memory,mode=mode)
                        expected = ref.run(args)
                        model = CreationOracle(words,memory,args,mode=mode if name.startswith('negative-') else 0)
                    else:
                        args = (NODE,0x3F800000,VALUES-8,0x40000000,0x40400000,0x40800000,0x40A00000)
                        put(memory,NODE+0x34,EXTRA)
                        for i,arg in enumerate(args[4:]):
                            put(memory,prior.STACK+16+i*4,arg)
                        allocations = (NODE+0x40,EXTRA)
                        ref = Reference(memory,mode=mode,allocations=allocations)
                        ref.attach(NODE,args[1:],prior.STACK)
                        expected = None
                        model = CreationOracle(words,memory,args,entry=setup.ENTRY,
                            mode=mode if name.startswith('negative-') else 0,allocations=allocations)
                    if not name.startswith('negative-') and mode:
                        continue
                    model.run()
                    expected_memory = prior.external_memory(ref.memory)
                    observed = (prior.external_memory(model.memory),model.calls)
                    required = (expected_memory,ref.calls)
                    # Control profiles have different private pointer layouts; compare public effects only.
                    if name.startswith('negative-'):
                        caught |= observed != required
                    else:
                        self.assertEqual(observed[0],required[0],(module.FUNCTION,name))
                        if expected is not None:
                            self.assertEqual(model.r[2],expected)
                        ordinary += 1
                if name.startswith('negative-'):
                    self.assertTrue(caught,(module.FUNCTION,name))
                    negatives += 1
        self.receipt('controls',dict(forms=len(records),ordinary_executions=ordinary,
            effective_negatives=negatives,measurements=records,all_profile_private_state_not_claimed=True))

    def test_06_copied_owner_two_targets_neighbors_padder_and_independent_call_rebases(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        for module in (screen,setup):
            if module.SELECTED in source:
                source = source.replace(module.SELECTED,module.STUB)
        source = source.replace(screen.DECLARATIONS+'\n','',1).replace(setup.DECLARATION+'\n','',1)
        selected = source.replace(screen.STUB,screen.SELECTED).replace(setup.STUB,setup.SELECTED).replace(
            '#include <ultra64.h>\n','#include <ultra64.h>\n'+screen.DECLARATIONS+'\n'+setup.DECLARATION+'\n',1)
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
            if name in (screen.FUNCTION,setup.FUNCTION):
                continue
            before = previous[name]
            self.assertEqual(text[function['value']:function['value']+function['size']],
                old[before['value']:before['value']+before['size']],name)
            self.assertEqual({o-function['value']:r for o,r in rel.items() if function['value'] <= o < function['value']+function['size']},
                {o-before['value']:r for o,r in old_rel.items() if before['value'] <= o < before['value']+before['size']},name)
        self.assertEqual(normalized_pools(objects[0]),normalized_pools(objects[1]))
        assembly = emit_padded_assembly(objects[1],self.root / 'conker/asm/5D2C0.s',
            word_patches_path=self.root / 'conker/retail_word_patches.us.csv',filename='generated_5D2C0',rodata_symbol=action.ANCHOR)
        for module,expected in ((screen,self.words),(setup,self.setup_words)):
            start = assembly.index('.type %s, @function' % module.FUNCTION)
            end = assembly.index('.size %s, . - %s' % (module.FUNCTION,module.FUNCTION),start)
            end = assembly.index('\n',end)+1
            self.assertNotIn('.space',assembly[end:assembly.find('.type ',end)])
            asm,obj = self.out / (module.FUNCTION+'-padded.s'),self.out / (module.FUNCTION+'-padded.o')
            asm.write_text('.text\n.set noreorder\n.globl %s\n' % module.FUNCTION+assembly[start:end])
            subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(obj),str(asm)],check=True,capture_output=True)
            _,functions,relocations = parse_object(obj)
            self.assertEqual(functions[module.FUNCTION]['size'],module.WORDS*4)
            self.assertNotIn('.rodata',sections(obj))
            symbols = screen.SYMBOLS if module is screen else dict(allocate_memory=ALLOCATE)
            for entry,delta in ((module.ENTRY,0),(module.ENTRY+0x01000004,0),(module.ENTRY,0x01000000)):
                script,elf = self.out / 'padded.ld',self.out / (module.FUNCTION+'-%X-%X.elf' % (entry,delta))
                script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
                subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',module.FUNCTION,
                    *['--defsym=%s=0x%X' % (name,address+delta) for name,address in symbols.items()],
                    '-o',str(elf),str(obj)],check=True,capture_output=True)
                rebased = list(struct.unpack_from('>%dI' % module.WORDS,sections(elf)['.text'][1]))
                required = expected.copy()
                for offset,entries in relocations.items():
                    self.assertEqual(len(entries),1)
                    kind,symbol = entries[0]
                    self.assertEqual(kind,'R_MIPS_26')
                    required[offset//4] = required[offset//4]&0xFC000000 | ((symbols[symbol]+delta)>>2)&0x3FFFFFF
                self.assertEqual(rebased,required)
        self.receipt('owner-padder',dict(functions=len(current),unchanged_neighbors=len(current)-2,
            pools_and_relative_relocations_unchanged=True,both_slots_no_padding_or_data=True,
            independent_entry_and_all_call_target_rebases=6,strict_diagnostics=0))

    def test_07_installed_or_previous_stubs_and_guard_history(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        functions,_,addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        installed = []
        for module,words in ((screen,self.words),(setup,self.setup_words)):
            present = module.SELECTED in source
            self.assertEqual(source.count(module.SELECTED if present else module.STUB),1)
            expected = words if present else [0x00001025,0x03E00008]+[0]*(module.WORDS-2)
            self.assertEqual((addresses[module.FUNCTION],functions[module.FUNCTION]),(module.ENTRY,expected))
            installed.append(present)
        self.assertEqual(installed[0],installed[1])
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self,guards)
        self.assertFalse(any(row['function'] in (screen.FUNCTION,setup.FUNCTION) for row in guards))
        self.receipt('installed',dict(both_installed=installed[0],guards_added=0))

    def test_08_actual_native32_connected_C_all_flag_bytes_and_input_canaries(self):
        patterns = ','.join('0x%X' % value for value in FLOATS)
        self.fixture = r'''typedef unsigned char u8;typedef int s32;typedef unsigned int u32;typedef float f32;
typedef union __attribute__((aligned(8))) {u32 words[16];unsigned long long align;} Mtx;
typedef union __attribute__((aligned(8))) {u32 align;u8 b[0x220];} Storage;
typedef union {u32 u;f32 f;} Float;
typedef char widths[(sizeof(void *)==4&&sizeof(Mtx)==64&&sizeof(f32)==4)?1:-1];
static Storage node,actor,created,values,extra;static Mtx bank[4];
static u32 value;static int mode,count,error,index,flags;static int calls[8];
static u32 bits(f32 f){Float v;v.f=f;return v.u;}
static void mark(int tag){if(count>=8){error=99;return;}calls[count++]=tag;}
u8 *func_15083568(u8 *a,s32 kind,f32 scale,s32 zero){
    mark(1);if(a!=actor.b||kind!=0x17||bits(scale)!=0x3F800000||zero)error=1;
    return mode&4?0:created.b;
}
void guMtxL2F(f32 out[4][4],Mtx *matrix){
    int i;mark(2);if(matrix!=bank+index)error=2;
    for(i=0;i<16;i++)((u32 *)out)[i]=matrix->words[i];
}
void func_15048B10(f32 in[4][4],f32 out[4][4]){
    int i;mark(3);for(i=0;i<16;i++)((u32 *)out)[i]=((u32 *)in)[15-i];
}
void func_150A9B0C(f32 out[4][4],f32 x,f32 y,f32 z,f32 sx,f32 sy,f32 sz){
    u32 args[6];int i;mark(4);args[0]=bits(x);args[1]=bits(y);args[2]=bits(z);
    args[3]=bits(sx);args[4]=bits(sy);args[5]=bits(sz);
    for(i=0;i<6;i++)if(args[i]!=value)error=3;
    for(i=0;i<16;i++)((u32 *)out)[i]=args[i%6];
}
void func_150A7A48(f32 in[4][4],f32 inverse[4][4],f32 out[4][4]){
    int i;mark(5);for(i=0;i<16;i++){
        u32 expected=i==15?0x3F800000:(i==3||i==7||i==11?0:value);
        if(((u32 *)in)[i]!=expected)error=4;
        if(((u32 *)inverse)[15-i]!=bank[index].words[i])error=5;
        ((u32 *)out)[i]=((u32 *)in)[i]^((u32 *)inverse)[15-i];
    }
}
void func_1503E5F8(f32 in[4][4],f32 *x,f32 *y,f32 *z,f32 *ax,f32 *ay,f32 *az,f32 *sx,f32 *sy,f32 *sz){
    f32 *out[9];int i;mark(6);out[0]=x;out[1]=y;out[2]=z;out[3]=ax;out[4]=ay;
    out[5]=az;out[6]=sx;out[7]=sy;out[8]=sz;
    for(i=0;i<16;i++){
        u32 expected=i==15?0x3F800000:(i==3||i==7||i==11?0:value);
        if(((u32 *)in)[i]!=(expected^bank[index].words[i]))error=6;
    }
    for(i=0;i<9;i++)*(u32 *)out[i]=value+(u32)i*0x10001;
}
void *allocate_memory(s32 amount,s32 a,s32 b,s32 c){
    int tag=count==6?7:8;mark(tag);if(a!=1||c!=2)error=7;
    if(tag==7){if(amount!=24||b!=0)error=8;return mode&8?0:values.b;}
    if(amount!=128||b!=2)error=9;
    return mode&16?0:extra.b;
}
''' + setup.SELECTED+'\n'+screen.SELECTED
        self.run_host('static u32 patterns[]={'+patterns+'};\n'+r'''
Storage old_node,old_actor,old_created,old_values,old_extra;Mtx old_bank[4];int i,j;u8 *result;
for(flags=0;flags<256;flags++)for(index=0;index<4;index++)for(mode=0;mode<64;mode++){
    value=patterns[flags%(sizeof(patterns)/sizeof(patterns[0]))];count=error=0;
    for(i=0;i<0x220;i++)node.b[i]=actor.b[i]=created.b[i]=values.b[i]=extra.b[i]=0xA5;
    for(i=0;i<4;i++)for(j=0;j<16;j++)bank[i].words[j]=value+(u32)j*19;
    *(Mtx **)(actor.b+0x1D4)=flags%17?bank:0;
    for(i=0;i<8;i++){static int offsets[8]={0x14,0x18,0x1C,0x40,0xB8,0xC4,0x14C,0x150};
        *(u32 *)(node.b+offsets[i])=value;}
    created.b[0x16]=(u8)flags;*(u8 **)(created.b+0x34)=mode&32?extra.b:0;
    old_node=node;old_actor=actor;old_created=created;old_values=values;old_extra=extra;
    for(i=0;i<4;i++)old_bank[i]=bank[i];
    result=func_150335C8(node.b,actor.b,0x17,index,mode&1,mode&2);
    if(!flags||flags%17==0){if(result||count||error)return 1;}
    else if(mode&4){if(result||count!=1||calls[0]!=1||error)return 2;}
    else{
        int expected_calls=(mode&8)||(mode&32)?7:8;
        if(result!=created.b||count!=expected_calls||error)return 3;
        for(i=0;i<count;i++)if(calls[i]!=i+1)return 4;
        old_created.b[2]=(u8)index;
        old_created.b[0x16]=(u8)(mode&1?flags&~4:flags|4);
        *(u32 *)(old_created.b+0x40)=value;
        *(u8 **)(old_created.b+0x44)=mode&8?0:values.b;
        if(!(mode&8)){
            for(i=0;i<6;i++)*(u32 *)(old_values.b+i*4)=i<3&&(mode&2)?0:value+(u32)i*0x10001;
            if(!(mode&32))*(u8 **)(old_created.b+0x34)=mode&16?0:extra.b;
        }
    }
    for(j=0;j<0x220;j++)if(node.b[j]!=old_node.b[j]||actor.b[j]!=old_actor.b[j]||
        created.b[j]!=old_created.b[j]||values.b[j]!=old_values.b[j]||extra.b[j]!=old_extra.b[j])return 5;
    for(i=0;i<4;i++)for(j=0;j<16;j++)if(bank[i].words[j]!=old_bank[i].words[j])return 6;
}
''')
        self.receipt('native',dict(cases=65536,pointer_bytes=4,Mtx_bytes=64,all_flag_bytes=256,
            both_complete_C_bodies_connected=True,creation_and_allocation_failures=True,
            optional_position_zero_and_existing_bank=True,all_object_bytes_and_input_canaries_checked=True,
            matrix_callbacks_controlled_not_complete_library_or_hardware=True))


if __name__ == '__main__':
    unittest.main()
