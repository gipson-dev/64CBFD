"""Attachment latch gates, ordered public accesses, callback ABI and owner isolation."""

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

from tools.experiments import game_node_attachment_latch_candidates as screen
from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.tests import test_game_node_action_match as action
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read

NODE, ACTOR, ATTACHED = 0x10000, 0x20000, 0x21000
ENABLE, DISABLE = 0x151026BC, 0x151027E8
DECLARATION = screen.DECLARATIONS.splitlines()[0]
TYPES = (0, 0x156, 0x157, 0x158, 0x164, 0x165, 0x166, 0x220, 0x221,
    0x222, 0x223, 0x224, 0x31A, 0x31B, 0x31C, 0x8000, 0xFFFF)
FLAGS = (0, 1, 0x1FFF, 0x2000, 0x2001, 0x7FFF, 0x8000, 0xFFFF)
LATCHES = (0, 1, 0x80000000, 0xFFFFFFFF)


def fixture(selector=0x16, kind=0x165, latch=0, active=1, subtype=2, flags=0x2000, counter=0):
    memory = {prior.STACK+i: 0xA5 for i in range(-0x100, 0x140)}
    for base, size in ((NODE, 0x40), (ACTOR, 0x340), (ATTACHED, 0x1C0)):
        memory.update({base+i: 0xA5 for i in range(size)})
    for address, value, size in ((NODE+6, selector, 1), (NODE+0x38, latch, 4),
            (ACTOR+0x84, kind, 2), (ACTOR+0x31C, ATTACHED, 4),
            (ATTACHED+0x197, active, 1), (ATTACHED+0x198, subtype, 1),
            (ATTACHED+0x8A, flags, 2), (ATTACHED+0x19E, counter, 2)):
        put(memory, address, value, size)
    return memory


def mutations(mode, stack, node):
    return {0: [], 1: [(node+0x38, 0x13579BDF, 4)],
        2: [(stack, 0, 4), (stack+4, 0, 4)],
        3: [(ACTOR+0x31C, 0, 4), (ATTACHED+0x8A, 0, 2), (node+6, 0, 1)]}[mode]


class LatchReference(action.ActionReference):
    def call(self, target, arguments, node):
        self.calls.append((target, *arguments))
        self.observed.append(self.get(node+0x38))
        for address, value, size in mutations(self.mode, self.stack, node):
            self.put(address, value, size)

    def run(self, node=NODE, actor=ACTOR):
        self.observed = []
        self.put(self.stack, node)
        self.put(self.stack+4, actor)
        selector = self.get(node+6, 1)
        kind = self.get(actor+0x84, 2)
        if selector == 0x16:
            mode, valid = 4, kind == 0x165
        elif selector == 0x89:
            mode, valid = 6, False
            if kind in (0x221, 0x223, 0x31B):
                valid = self.get(self.get(actor+0x31C)+0x198, 1) == 2
        else:
            mode, valid = 5, kind == 0x157
        latch = self.get(node+0x38)
        if not latch:
            if valid:
                attached = self.get(actor+0x31C)
                if self.get(attached+0x197, 1) or mode == 6:
                    if self.get(attached+0x8A, 2)&0x2000:
                        if not self.get(attached+0x19E, 2):
                            self.put(node+0x38, 1)
                            self.call(ENABLE, (self.get(self.stack+4), 0xFFFFFFFF, mode, 1, 255, 1), node)
        else:
            if valid:
                attached = self.get(actor+0x31C)
                if self.get(attached+0x8A, 2)&0x2000:
                    if self.get(attached+0x197, 1) or mode == 6:
                        return 0
            self.put(node+0x38, 0)
            self.call(DISABLE, (self.get(self.stack+4),), node)
        return 0


class LatchOracle(TriangleOracle):
    def __init__(self, words, memory, args=(NODE, ACTOR), phase=0, mode=0):
        super().__init__(words, memory, entry=screen.ENTRY, arguments=args, phase=phase)
        self.node, self.stack, self.mode = args[0], prior.STACK+phase, mode
        self.observed = []

    def record_call(self, target):
        assert target in (ENABLE, DISABLE)
        self.calls.append((target, *self.arguments(6 if target == ENABLE else 1)))

    def hook(self, target):
        self.observed.append(self.get(self.node+0x38, 4))
        for address, value, size in mutations(self.mode, self.stack, self.node):
            self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameNodeAttachmentLatchMatchTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-node-attachment-latch-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        cls.retail = list(struct.unpack_from('>100I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def compare(self, memory, args=(NODE, ACTOR), phase=0, mode=0):
        reference = LatchReference(memory, phase, mode)
        expected = reference.run(*args)
        models = [LatchOracle(w, memory, args, phase, mode).run() for w in (self.words, self.retail)]
        for model in models:
            self.assertEqual((model.r[2], model.calls, model.observed, prior.public(model.events), prior.external_memory(model.memory)),
                (expected, reference.calls, reference.observed, prior.public(reference.events), prior.external_memory(reference.memory)))
            for offset in (0, 4):
                self.assertEqual(read(model.memory, prior.STACK+phase+offset), read(reference.memory, prior.STACK+phase+offset))
        self.assertEqual((models[0].r, models[0].f, models[0].events, models[0].memory),
            (models[1].r, models[1].f, models[1].events, models[1].memory))
        return models

    def test_01_direct_complete_slot_frame_and_symbolic_calls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
            self.record['pool_bytes'], self.record['diagnostics']), (100, 32, 0, 0, ''))
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.record['relocations'], {296: [('R_MIPS_26', 'func_151026BC')],
            372: [('R_MIPS_26', 'func_151027E8')]})
        self.receipt('slot', dict(words=100, frame=32, differences=0, padding_words=0,
            guards_added=0, generated_data_bytes=0, symbolic_calls=2, standard_o2g3_profile=True))

    def test_02_all_selectors_type_boundaries_gates_callback_mutations_and_word_coverage(self):
        seen, selectors, gates, bytes_seen = set(), 0, 0, 0
        for selector, kind, latch, phase in itertools.product(range(256), TYPES, (0, 1), (0, 8)):
            for model in self.compare(fixture(selector, kind, latch), phase=phase):
                seen.update(model.visits)
            selectors += 1
        for selector, kind in ((0x16, 0x165), (0x89, 0x221), (0, 0x157)):
            for flag, count, active, latch, mode, phase in itertools.product(
                    FLAGS, (0, 1, 0xFF, 0x100, 0xFFFF), (0, 1, 0x80, 0xFF), LATCHES, range(4), (0, 8)):
                for model in self.compare(fixture(selector, kind, latch, active, flags=flag, counter=count), phase=phase, mode=mode):
                    seen.update(model.visits)
                gates += 1
        for value, axis, latch in itertools.product(range(256), ('active', 'subtype'), (0, 1)):
            for model in self.compare(fixture(0x89, 0x31B, latch, **{axis:value})):
                seen.update(model.visits)
            bytes_seen += 1
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+400, 4))-seen)
        self.assertEqual(missing, [19])
        self.receipt('guest', dict(cases=selectors+gates+bytes_seen, selector_cases=selectors,
            gate_cases=gates, byte_axis_cases=bytes_seen, selector_bytes=256, actor_type_boundaries=len(TYPES),
            active_and_subtype_all_256_bytes=True, all_nonzero_latch_patterns=True,
            SP_phases=2, callback_mutation_modes=4, missing_word_indices=missing,
            public_access_order_memory_return_and_call_ABI_equal=True,
            full_GP_FP_trace_memory_equal_C_vs_retail=True, saved_registers_checked=True,
            full_callback_libraries_and_gameplay_not_claimed=True))

    def test_03_lazy_fields_fault_prefixes_aliases_and_callback_latch_order(self):
        lazy = []
        memory = fixture(kind=0)
        for address in range(ACTOR+0x31C, ACTOR+0x320):
            del memory[address]
        lazy.append(memory)
        memory = fixture(active=0)
        del memory[ATTACHED+0x8A]
        del memory[ATTACHED+0x19E]
        lazy.append(memory)
        memory = fixture(flags=0)
        del memory[ATTACHED+0x19E]
        lazy.append(memory)
        memory = fixture(latch=1, flags=0)
        del memory[ATTACHED+0x197]
        del memory[ATTACHED+0x19E]
        lazy.append(memory)
        memory = fixture(latch=1, counter=0xFFFF)
        del memory[ATTACHED+0x19E]
        lazy.append(memory)
        memory = fixture(0x89, 0x220)
        del memory[ACTOR+0x31C]
        lazy.append(memory)
        for memory in lazy:
            self.compare(memory)
        aliases = []
        memory = fixture()
        put(memory, ACTOR+6, 0x16, 1)
        put(memory, ACTOR+0x38, 0)
        aliases.append((memory, (ACTOR, ACTOR)))
        memory = fixture()
        put(memory, ACTOR+0x31C, ACTOR)
        put(memory, ACTOR+0x197, 1, 1)
        put(memory, ACTOR+0x8A, 0x2000, 2)
        put(memory, ACTOR+0x19E, 0, 2)
        aliases.append((memory, (NODE, ACTOR)))
        memory = fixture()
        memory.update({NODE+i:memory.get(NODE+i, 0xA5) for i in range(0x1C0)})
        put(memory, ACTOR+0x31C, NODE)
        put(memory, NODE+0x197, 1, 1)
        put(memory, NODE+0x8A, 0x2000, 2)
        put(memory, NODE+0x19E, 0, 2)
        aliases.append((memory, (NODE, ACTOR)))
        memory = fixture(latch=1, kind=0)
        home_node = prior.STACK-0x34
        put(memory, home_node+6, 0x16, 1)
        aliases.append((memory, (home_node, ACTOR)))
        for memory, args in aliases:
            self.compare(memory, args)
        faults = []
        for selector, kind, latch in ((0x16, 0x165, 0), (0x89, 0x221, 0), (0x16, 0x165, 1)):
            for address in (NODE+6, ACTOR+0x84, NODE+0x38, ACTOR+0x31C, ATTACHED+0x197, ATTACHED+0x8A):
                memory = fixture(selector, kind, latch)
                del memory[address]
                faults.append((memory, (NODE, ACTOR)))
        for address, selector, kind in ((ATTACHED+0x198, 0x89, 0x221), (ATTACHED+0x19E, 0x16, 0x165)):
            memory = fixture(selector, kind)
            del memory[address]
            faults.append((memory, (NODE, ACTOR)))
        memory = fixture()
        put(memory, ACTOR+0x31C, 0)
        faults.append((memory, (NODE, ACTOR)))
        faults.extend(((fixture(), (0, ACTOR)), (fixture(), (NODE, 0))))
        for memory, args in faults:
            reference = LatchReference(memory)
            with self.assertRaises(AssertionError) as failure:
                reference.run(*args)
            for words in (self.words, self.retail):
                model = LatchOracle(words, memory, args)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args, failure.exception.args)
                self.assertEqual((model.calls, prior.public(model.events), prior.external_memory(model.memory)),
                    (reference.calls, prior.public(reference.events), prior.external_memory(reference.memory)))
        self.receipt('gates', dict(lazy_cases=len(lazy), aliases=len(aliases), required_fault_prefixes=len(faults),
            no_added_null_attachment_gate=True, latch_written_before_callbacks=True,
            callback_mutated_latch_preserved=True, clear_reloads_actor_home_after_alias_store=True))

    def test_04_source_profiles_and_effective_semantic_negatives(self):
        memories = [fixture(selector=s, kind=k, latch=l, active=a, counter=c) for s,k,l,a,c in (
            (0x16,0x165,0,1,0), (0x16,0x165,1,1,1), (0x89,0x221,0,0,0),
            (0x89,0x31B,1,0,1), (0x89,0x165,1,1,0), (0,0x157,0,1,1),
            (0x16,0x165,0,1,0x100), (0,0x157,1,0,0))]
        records, ordinary, negatives = [], 0, 0
        forms = [(n,b,'o2g3') for n,b in screen.candidates()]
        forms += [('profile-'+p,screen.SELECTED,p) for p in PROFILES if p != 'o2g3']
        for name,body,profile in forms:
            record,words = screen.compile_candidate(self.root,self.out,name,body,profile)
            records.append(record)
            caught = False
            for memory in memories:
                reference = LatchReference(memory)
                expected = reference.run()
                model = LatchOracle(words,memory).run()
                observed = (model.r[2], model.calls, model.observed, prior.external_memory(model.memory))
                required = (expected, reference.calls, reference.observed, prior.external_memory(reference.memory))
                if name.startswith('negative-'):
                    caught |= observed != required
                else:
                    self.assertEqual(observed, required, name)
                    ordinary += 1
            if name.startswith('negative-'):
                self.assertTrue(caught, name)
                negatives += 1
        self.receipt('controls', dict(forms=len(records), ordinary_executions=ordinary,
            effective_semantic_negatives=negatives, measurements=records,
            alternate_control_private_frames_and_full_access_traces_not_claimed=True))

    def test_05_actual_native32_all_unsigned_types_and_public_canaries(self):
        self.fixture = r'''typedef unsigned char u8;typedef unsigned short u16;typedef int s32;typedef unsigned int u32;
typedef union __attribute__((aligned(8))) {u32 align;u8 b[0x340];} Storage;
typedef char widths[(sizeof(void *)==4&&sizeof(u16)==2)?1:-1];
static Storage node,actor,attached;static int count,error,seen_mode,mutate;static u32 observed;
void func_151026BC(u8 *a,s32 minus,s32 mode,s32 one,s32 max,s32 tail){
    count=1;seen_mode=mode;observed=*(u32 *)(node.b+0x38);
    if(a!=actor.b||minus!=-1||one!=1||max!=255||tail!=1)error=1;
    if(mutate)*(u32 *)(node.b+0x38)=0x13579BDF;
}
void func_151027E8(u8 *a){count=2;observed=*(u32 *)(node.b+0x38);if(a!=actor.b)error=2;
    if(mutate)*(u32 *)(node.b+0x38)=0x13579BDF;
}
''' + screen.SELECTED + r'''
static int check_case(int selector,int kind,u32 latch,int active,int subtype,int flag,int counter,int mutation){
    Storage old_node,old_actor,old_attached;u32 expected;int i,mode,valid,want;
    for(i=0;i<0x340;i++)node.b[i]=actor.b[i]=attached.b[i]=0xA5;
    mode=selector==0x16?4:selector==0x89?6:5;node.b[6]=selector;
    *(u16 *)(actor.b+0x84)=kind;*(u8 **)(actor.b+0x31C)=attached.b;
    *(u32 *)(node.b+0x38)=latch;
    attached.b[0x197]=active;attached.b[0x198]=subtype;
    *(u16 *)(attached.b+0x8A)=flag;*(u16 *)(attached.b+0x19E)=counter;
    valid=selector==0x16?kind==0x165:selector==0x89?((kind==0x221||kind==0x223||kind==0x31B)&&subtype==2):kind==0x157;
    want=latch?(valid&&(flag&0x2000)&&(active||mode==6)?0:2):
        (valid&&(active||mode==6)&&(flag&0x2000)&&counter==0?1:0);
    expected=want==1?1:want==2?0:latch;mutate=mutation;
    old_node=node;old_actor=actor;old_attached=attached;count=error=seen_mode=0;observed=0xA5A5A5A5;
    if(func_15033838(node.b,actor.b)!=0||error||count!=want)return 1;
    if(want&&(observed!=expected||(want==1&&seen_mode!=mode)))return 2;
    if(want&&mutate)expected=0x13579BDF;
    *(u32 *)(old_node.b+0x38)=expected;
    for(i=0;i<0x340;i++)if(node.b[i]!=old_node.b[i]||actor.b[i]!=old_actor.b[i]||attached.b[i]!=old_attached.b[i])return 3;
    return 0;
}
'''
        self.run_host(r'''
static int selectors[3]={0x16,0x89,0};static int kinds[3]={0x165,0x221,0x157};
static int flags[8]={0,1,0x1FFF,0x2000,0x2001,0x7FFF,0x8000,0xFFFF};
static int counters[5]={0,1,0xFF,0x100,0xFFFF};static int actives[4]={0,1,0x80,0xFF};
static u32 latches[4]={0,1,0x80000000,0xFFFFFFFF};
int axis,kind,l,f,c,a,m,v,result;
for(axis=0;axis<3;axis++)for(kind=0;kind<65536;kind++)for(l=0;l<4;l++){
    result=check_case(selectors[axis],kind,latches[l],kind&1,(kind>>1)&3,
        kind&4?0xFFFF:0,kind&8?0x100:0,(kind>>4)&1);
    if(result)return result;
}
for(axis=0;axis<3;axis++)for(f=0;f<8;f++)for(c=0;c<5;c++)for(a=0;a<4;a++)for(l=0;l<4;l++)for(m=0;m<2;m++){
    result=check_case(selectors[axis],kinds[axis],latches[l],actives[a],2,flags[f],counters[c],m);
    if(result)return 10+result;
}
for(v=0;v<256;v++)for(l=0;l<4;l++)for(m=0;m<2;m++){
    result=check_case(0x89,0x31B,latches[l],0,v,0x2000,0,m);
    if(result)return 20+result;
    result=check_case(0x89,0x223,latches[l],v,2,0x2000,0,m);
    if(result)return 30+result;
}
''')
        self.receipt('native', dict(cases=794368, type_sweep_cases=786432, independent_gate_cases=3840,
            byte_axis_cases=4096, all_unsigned_actor_types=65536, action_classes=3,
            latch_patterns=4, actual_complete_C=True, pointer_bytes=4, all_input_canaries_checked=True,
            callback_arguments_and_pre_callback_latch_checked=True, type_sweep_axes_correlated=True,
            independent_gate_grid_and_mode6_activation=True, hardware_not_claimed=True))

    def test_06_copied_owner_padder_and_independent_symbol_rebases(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        if screen.SELECTED in source:
            source = source.replace(screen.SELECTED,screen.STUB).replace(DECLARATION+'\n','',1)
        self.assertEqual(source.count(screen.STUB),1)
        selected = source.replace(screen.STUB,screen.SELECTED).replace('#include <ultra64.h>\n',
            '#include <ultra64.h>\n'+DECLARATION+'\n',1)
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
        self.assertEqual(text[target['value']:target['value']+400],isolated[:400])
        self.assertEqual({o-target['value']:r for o,r in rel.items() if target['value'] <= o < target['value']+400},isolated_rel)
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
        self.assertEqual(functions[screen.FUNCTION]['size'],400)
        self.assertEqual(relocations,isolated_rel)
        self.assertNotIn('.rodata',sections(obj))
        symbols = dict(func_151026BC=ENABLE,func_151027E8=DISABLE)
        for entry,delta in ((screen.ENTRY,0),(screen.ENTRY+0x01000004,0),(screen.ENTRY,0x01000000)):
            script,elf = self.out / 'padded.ld',self.out / ('rebased-%X-%X.elf' % (entry,delta))
            script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
            subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',screen.FUNCTION,
                *['--defsym=%s=0x%X' % (name,address+delta) for name,address in symbols.items()],
                '-o',str(elf),str(obj)],check=True,capture_output=True)
            required = self.words.copy()
            for offset,entries in relocations.items():
                kind,symbol = entries[0]
                self.assertEqual((len(entries),kind),(1,'R_MIPS_26'))
                required[offset//4] = required[offset//4]&0xFC000000 | ((symbols[symbol]+delta)>>2)&0x3FFFFFF
            self.assertEqual(list(struct.unpack_from('>100I',sections(elf)['.text'][1])),required)
        self.receipt('owner-padder',dict(functions=len(current),unchanged_neighbors=len(current)-1,
            pools_relative_relocations_unchanged=True, strict_diagnostics=0,
            slot_no_padding_or_data=True, independent_entry_and_call_rebases=3))

    def test_07_installed_or_previous_stub_and_guard_history(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        installed = screen.SELECTED in source
        self.assertEqual(source.count(screen.SELECTED if installed else screen.STUB),1)
        functions,_,addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        expected = self.words if installed else [0x00001025,0x03E00008]+[0]*98
        self.assertEqual((addresses[screen.FUNCTION],functions[screen.FUNCTION]),(screen.ENTRY,expected))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self,guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed',dict(installed=installed,byte_exact=installed,guards_added=0))


if __name__ == '__main__':
    unittest.main()
