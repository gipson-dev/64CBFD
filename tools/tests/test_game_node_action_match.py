"""Complete two-table action dispatch, raw V0, call ABI and fixed table ownership."""

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

from tools.experiments import game_node_action_candidates as screen
from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.patch_generated_slice_ld import load_game_data_layout
from tools.tests import test_game_attachment_progress_match as progress
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.game_animation_timeline_oracle import signed
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read

NODE, ALT_NODE, ACTOR, STATE = 0x10000, 0x11000, 0x20000, 0x21000
LOW, HIGH = 0x80090228, 0x8009022C
ANCHOR = 'jtbl_80096F40_game'
STUB = 's32 func_15031A50() {\n    return 0;\n}'
RANDOM = screen.SYMBOLS['func_150859AC']
WIDTHS = {screen.SYMBOLS[n]: w for n, w in (('func_151001B4', 1), ('func_15163BE8', 3),
    ('func_150D3360', 3), ('func_150D5440', 3), ('func_151BD828', 3), ('func_151D74B0', 5), ('func_150859AC', 2))}
RESULTS = (0, 99, 100, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFF)
COUNTERS = (None, 0, 0xFF55, 0xFF56, 0xFFFF)
CALLS = {0x37: [('func_151001B4', ())], 0x49: [('func_15163BE8', (255, 1))],
    0x5D: [('func_150D3360', (255, 1)), ('func_150D5440', (255, 1))],
    0x3D: [('func_151BD828', (255, 1))], 0x1D: [('func_151D74B0', (0, 2, 255, 1))],
    0x82: [('func_151D74B0', (6, 0xFFFFFFFF, 255, 1))]}
MASKS = {0x90: 0x70, 0x8F: 0xE00, 0x85: 0x6000, 0x5E: 0x6000}


def fixture(pool, action, counter=0, phase=0):
    memory = {prior.STACK+i: 0xA5 for i in range(-0x100, 0x100)}
    for base, size in ((NODE, 0x40), (ALT_NODE, 0x40), (ACTOR, 0x340), (STATE, 0x1C0)):
        memory.update({base+i: 0xA5 for i in range(size)})
    memory.update({screen.TABLE+i: value for i, value in enumerate(pool)})
    put(memory, NODE+1, action, 1)
    put(memory, ACTOR+0x31C, 0 if counter is None else STATE)
    put(memory, STATE+0x1A6, counter or 0, 2)
    put(memory, ACTOR+0x9C, 0x80000001 if counter is None else counter)
    put(memory, LOW, 0xABCD1234)
    put(memory, HIGH, 0xDEAD8001)
    return memory


def mutations(mode, stack):
    return {0: [], 1: [(stack, ALT_NODE, 4)],
        2: [(LOW, 0xFFFF7FFF, 4), (HIGH, 0x12348000, 4)],
        3: [(NODE+1, 0, 1), (ACTOR+0x9C, 0x12345678, 4)]}[mode]


class ActionReference(progress.ProgressReference):
    def put(self, address, value, size=4):
        value &= (1 << (size*8))-1
        self.events.append(('W', address, size, value))
        assert all(address+i in self.memory for i in range(size)), ('unmapped store', address, size)
        put(self.memory, address, value, size)

    def call(self, name, arguments):
        target = screen.SYMBOLS[name]
        self.calls.append((target, *arguments))
        for address, value, size in mutations(self.mode, self.stack):
            self.put(address, value, size)
        return self.random if target == RANDOM else 0xBEEF0000+len(self.calls)

    def run(self, node, actor, random=0):
        self.random = random
        action = self.get(node+1, 1)
        if action >= 0x5F:
            if 0x82 <= action <= 0x90:
                self.get(screen.TABLE+(action-0x82)*4)
        elif action >= 0x1E and 0x37 <= action <= 0x5E:
            self.get(screen.TABLE+60+(action-0x37)*4)
        if action in CALLS:
            for name, rest in CALLS[action]:
                action_result = self.call(name, (actor, *rest))
            return action_result
        if action == 0x5A:
            state = self.get(actor+0x31C)
            if state:
                self.put(state+0x1A6, self.get(state+0x1A6, 2)+0xAA, 2)
            return state
        if action in MASKS:
            self.put(actor+0x9C, self.get(actor+0x9C)|MASKS[action])
        if action == 0x8D:
            self.put(self.stack, node)
            result = self.call('func_150859AC', (0, 6))
            node = self.get(self.stack)
            value = self.get(LOW if signed(result) < 100 else HIGH)
            self.put(node+0x18, value, 2)
            return result
        return action


class ActionOracle(TriangleOracle):
    def __init__(self, words, memory, args=(NODE, ACTOR), phase=0, mode=0, random=0):
        super().__init__(words, memory, entry=screen.ENTRY, arguments=args, phase=phase)
        self.stack, self.mode, self.random = prior.STACK+phase, mode, random

    def record_call(self, target):
        self.calls.append((target, *self.arguments(WIDTHS[target])))

    def hook(self, target):
        for address, value, size in mutations(self.mode, self.stack):
            self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.r[2] = self.random if target == RANDOM else 0xBEEF0000+len(self.calls)
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameNodeActionMatchTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-node-action-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words, cls.pool = screen.compile_candidate(cls.root, cls.out, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>113I', cls.rom, screen.ROM))
        start, base, _, owners = load_game_data_layout(cls.root / 'conker')
        cls.original_pool = cls.rom[start+screen.TABLE-base:start+screen.TABLE-base+220]
        cls.table_owner = [o for o in owners if o['address'] <= screen.TABLE < o['end']]
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def compare(self, memory, args=(NODE, ACTOR), phase=0, mode=0, random=0):
        reference = ActionReference(memory, phase, mode)
        expected = reference.run(*args, random)
        models = [ActionOracle(w, memory, args, phase, mode, random).run() for w in (self.words, self.retail)]
        for model in models:
            self.assertEqual((model.r[2], model.calls, prior.public(model.events), prior.external_memory(model.memory)),
                (expected, reference.calls, prior.public(reference.events), prior.external_memory(reference.memory)))
        self.assertEqual((models[0].r, models[0].f, models[0].events), (models[1].r, models[1].f, models[1].events))
        return models

    def test_direct_slot_and_complete_generated_table_targets(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (113, 40, 0))
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.pool, self.original_pool+bytes(4))
        self.assertEqual(self.table_owner[0]['input'], 'build/asm/data/23B8A0.rodata.s.o(.rodata)')
        self.assertEqual(self.record['diagnostics'], '')
        self.receipt('slot', dict(body_words=113, slot_words=113, frame=40, direct_differences=0,
            table_targets=55, generated_tail_alignment_bytes=4, original_data_owner_preserved=True, guards_added=0))

    def test_all_selectors_signed_random_boundary_wrap_mutations_and_word_coverage(self):
        seen, cases = set(), 0
        for action, random, counter, mode, phase in itertools.product(range(256), RESULTS, COUNTERS, range(4), (0, 8)):
            for model in self.compare(fixture(self.original_pool, action, counter), phase=phase, mode=mode, random=random):
                seen.update(model.visits)
            cases += 1
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+452, 4))-seen)
        self.assertEqual(missing, [])
        self.receipt('guest', dict(cases=cases, selector_bytes=256, signed_random_results=6, counters=5,
            callback_modes=4, SP_phases=2, missing_word_indices=missing,
            raw_V0_GP_FP_public_trace_and_memory_equal=True, all_saved_registers_checked=True,
            complete_callees_and_hardware_not_claimed=True))

    def test_lazy_default_null_state_required_storage_and_post_callback_home(self):
        for action in (0, 0x1E, 0x36, 0x5F, 0x81, 0x91, 0xFF):
            self.compare(fixture(self.original_pool, action), (NODE, 0))
        memory = fixture(self.original_pool, 0x5A, None)
        memory.pop(STATE+0x1A6)
        self.compare(memory)
        probes = [(fixture(self.original_pool, 0), (0, ACTOR), 0, None),
            (fixture(self.original_pool, 0x90), (NODE, 0), 0, None),
            (fixture(self.original_pool, 0x90), (NODE, ACTOR), 0, ACTOR+0x9C),
            (fixture(self.original_pool, 0x5A), (NODE, ACTOR), 0, ACTOR+0x31C),
            (fixture(self.original_pool, 0x5A), (NODE, ACTOR), 0, STATE+0x1A6),
            (fixture(self.original_pool, 0x8D), (NODE, ACTOR), 0, LOW),
            (fixture(self.original_pool, 0x8D), (NODE, ACTOR), 0, NODE+0x18),
            (fixture(self.original_pool, 0x8D), (NODE, ACTOR), 1, ALT_NODE+0x18),
            (fixture(self.original_pool, 0x82), (NODE, ACTOR), 0, screen.TABLE),
            (fixture(self.original_pool, 0x37), (NODE, ACTOR), 0, screen.TABLE+60)]
        for memory, args, mode, missing in probes:
            if missing is not None:
                memory.pop(missing)
            reference = ActionReference(memory, mode=mode)
            with self.assertRaises(AssertionError) as failure:
                reference.run(*args)
            for words in (self.words, self.retail):
                model = ActionOracle(words, memory, args, mode=mode)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args, failure.exception.args)
                self.assertEqual((prior.public(model.events), model.calls, prior.external_memory(model.memory)),
                    (prior.public(reference.events), reference.calls, prior.external_memory(reference.memory)))
        self.receipt('gates', dict(lazy_cases=8, required_faults=10, callback_partial_effects_preserved=True,
            random_callback_reloads_incoming_node_home=True, arbitrary_stack_aliases_not_claimed=True))

    def test_fifteen_source_profile_controls_and_effective_negatives(self):
        forms = [(n, b, 'o2g3') for n, b in screen.candidates()]
        forms += [('profile-'+p, screen.SELECTED, p) for p in PROFILES if p != 'o2g3']
        records, executions = [], 0
        for name, body, profile in forms:
            record, words, pool = screen.compile_candidate(self.root, self.out, name, body, profile)
            for action in range(256):
                memory = fixture(pool, action, 0xFFFF)
                reference = ActionReference(memory)
                reference.run(NODE, ACTOR, 100)
                model = ActionOracle(words, memory, random=100).run()
                self.assertEqual((model.calls, prior.external_memory(model.memory)),
                    (reference.calls, prior.external_memory(reference.memory)), name)
                executions += 1
            records.append(record)
        self.assertEqual(sum(not r['differences'] for r in records), 8)
        negatives = {'strict_boundary': (screen.SELECTED.replace('< 100', '<= 100'), 0x8D, 100),
            'unsigned_random': (screen.SELECTED.replace('func_150859AC(0, 6) <', '(u32)func_150859AC(0, 6) <'), 0x8D, 0xFFFFFFFF),
            'wrong_mask': (screen.SELECTED.replace('|= 0x70;', '|= 0x60;'), 0x90, 0),
            'omit_second_call': (screen.SELECTED.replace('            func_150D5440(actor, 0xFF, 1);\n', ''), 0x5D, 0)}
        for name, (body, action, random) in negatives.items():
            _, words, pool = screen.compile_candidate(self.root, self.out, 'negative-'+name, body)
            memory = fixture(pool, action, 0)
            reference = ActionReference(memory)
            expected = reference.run(NODE, ACTOR, random)
            model = ActionOracle(words, memory, random=random).run()
            self.assertNotEqual((model.r[2], model.calls, prior.external_memory(model.memory)),
                (expected, reference.calls, prior.external_memory(reference.memory)), name)
        self.receipt('controls', dict(forms=len(forms), ordinary_executions=executions, raw_exact_forms=8,
            measurements=records, effective_negatives=list(negatives), no_fault_accepted_as_success=True,
            all_control_raw_V0_read_order_homes_private_not_claimed=True))

    def test_native32_complete_void_C_public_effects_and_call_ABI(self):
        self.fixture = r'''typedef unsigned char u8;typedef unsigned short u16;typedef short s16;
typedef int s32;typedef unsigned int u32;
typedef union {u32 align;u8 b[0x340];} Storage;
typedef char pointer_width[(sizeof(void *)==4)?1:-1];
static Storage node,actor,state;static int mode,count;static u32 random_value,log[2][6];
s32 D_80090228,D_8009022C;
static void call(u32 target,u32 a,u32 b,u32 c,u32 d,u32 e){
    log[count][0]=target;log[count][1]=a;log[count][2]=b;log[count][3]=c;log[count][4]=d;log[count][5]=e;count++;
    if(mode&1){node.b[1]=0;*(u32 *)(actor.b+0x9C)=0x12345678;}
    if(mode&2){D_80090228=0xFFFF7FFF;D_8009022C=0x12348000;}
}
void func_151001B4(u8 *a){call(0x151001B4,(u32)a,0,0,0,0);}
void func_15163BE8(u8 *a,s32 b,s32 c){call(0x15163BE8,(u32)a,b,c,0,0);}
void func_150D3360(u8 *a,s32 b,s32 c){call(0x150D3360,(u32)a,b,c,0,0);}
void func_150D5440(u8 *a,s32 b,s32 c){call(0x150D5440,(u32)a,b,c,0,0);}
void func_151BD828(u8 *a,s32 b,s32 c){call(0x151BD828,(u32)a,b,c,0,0);}
void func_151D74B0(u8 *a,s32 b,s32 c,s32 d,s32 e){call(0x151D74B0,(u32)a,b,c,d,e);}
s32 func_150859AC(s32 a,s32 b){call(0x150859AC,a,b,0,0,0);return (s32)random_value;}
static void init(int action,u32 random,int counter,int kind){int i,j;count=0;mode=kind;random_value=random;
    for(i=0;i<0x340;i++)node.b[i]=actor.b[i]=state.b[i]=0xA5;
    for(i=0;i<2;i++)for(j=0;j<6;j++)log[i][j]=0;
    node.b[1]=action;*(u8 **)(actor.b+0x31C)=counter<0?0:state.b;
    *(u16 *)(state.b+0x1A6)=counter<0?0:counter;*(u32 *)(actor.b+0x9C)=counter<0?0x80000001:(u32)counter;
    D_80090228=0xABCD1234;D_8009022C=0xDEAD8001;
}
static void reference(u8 *n,u8 *a){int action=n[1];u8 *s;int result;
    if(action==0x5A){s=*(u8 **)(a+0x31C);if(s)*(u16 *)(s+0x1A6)+=0xAA;}
    else if(action==0x90||action==0x8F||action==0x85||action==0x5E)
        *(u32 *)(a+0x9C)|=action==0x90?0x70:action==0x8F?0xE00:0x6000;
    else if(action==0x37)call(0x151001B4,(u32)a,0,0,0,0);
    else if(action==0x49)call(0x15163BE8,(u32)a,255,1,0,0);
    else if(action==0x5D){call(0x150D3360,(u32)a,255,1,0,0);call(0x150D5440,(u32)a,255,1,0,0);}
    else if(action==0x3D)call(0x151BD828,(u32)a,255,1,0,0);
    else if(action==0x1D||action==0x82)call(0x151D74B0,(u32)a,action==0x1D?0:6,action==0x1D?2:0xFFFFFFFF,255,1);
    else if(action==0x8D){result=(s32)random_value;call(0x150859AC,0,6,0,0,0);
        *(s16 *)(n+0x18)=result<100?D_80090228:D_8009022C;}
}
''' + screen.SELECTED
        self.run_host(r'''
static u32 results[6]={0,99,100,0x7FFFFFFF,0x80000000,0xFFFFFFFF};static int counters[5]={-1,0,0xFF55,0xFF56,0xFFFF};
Storage saved[3];u32 savedlog[2][6];s32 low,high;int action,r,c,m,i,j,expectedCount;
for(action=0;action<256;action++)for(r=0;r<6;r++)for(c=0;c<5;c++)for(m=0;m<4;m++){
    init(action,results[r],counters[c],m);reference(node.b,actor.b);saved[0]=node;saved[1]=actor;saved[2]=state;
    low=D_80090228;high=D_8009022C;expectedCount=count;for(i=0;i<2;i++)for(j=0;j<6;j++)savedlog[i][j]=log[i][j];
    init(action,results[r],counters[c],m);func_15031A50(node.b,actor.b);
    if(count!=expectedCount||D_80090228!=low||D_8009022C!=high)return 1;
    for(i=0;i<0x340;i++)if(node.b[i]!=saved[0].b[i]||actor.b[i]!=saved[1].b[i]||state.b[i]!=saved[2].b[i])return 2;
    for(i=0;i<2;i++)for(j=0;j<6;j++)if(savedlog[i][j]!=log[i][j])return 3;
}
''')
        self.receipt('native', dict(cases=256*6*5*4, pointer_bytes=4, complete_actual_void_C=True,
            calls_ABI_all_object_bytes_and_globals_checked=True, defined_C_return_not_claimed=True,
            invalid_pointers_private_homes_full_callees_not_claimed=True))

    def qualify_owner(self):
        from tools.experiments import game_node_cleanup_candidates as cleanup
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        has_cleanup = cleanup.SELECTED in source
        if screen.SELECTED in source:
            source = source.replace(screen.SELECTED, STUB).replace(screen.DECLARATIONS+'\n', '', 1)
        self.assertEqual(source.count(STUB), 1)
        selected = source.replace(STUB, screen.SELECTED).replace('#include <ultra64.h>\n',
            '#include <ultra64.h>\n'+screen.DECLARATIONS+'\n', 1)
        objects = []
        for name, body in (('baseline', source), ('selected', selected)):
            obj, warnings = compile_owner(self.root, self.out, body, 'owner-'+name)
            self.assertEqual(warnings, [])
            processed = self.out / ('owner-'+name+'-postprocessed.o')
            shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.out / ('owner-'+name+'.c')).relative_to(self.root / 'conker')), '--post-process',
                str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker', check=True, capture_output=True)
            objects.append(processed)
        old_text, old_functions, old_rel = parse_object(objects[0])
        text, functions, rel = parse_object(objects[1])
        self.assertEqual(set(functions), set(old_functions))
        for name, current in functions.items():
            if name == screen.FUNCTION:
                continue
            previous = old_functions[name]
            expected_text = bytearray(old_text[previous['value']:previous['value']+previous['size']])
            if has_cleanup and name == cleanup.FUNCTION:
                # Removing this earlier dispatcher shifts the later pool by 55 entries.
                self.assertEqual(struct.unpack_from('>I', expected_text, 132)[0]&65535, 0)
                struct.pack_into('>I', expected_text, 132, struct.unpack_from('>I', expected_text, 132)[0]+220)
            self.assertEqual(text[current['value']:current['value']+current['size']],
                expected_text, name)
            self.assertEqual({o-current['value']: r for o, r in rel.items()
                if current['value'] <= o < current['value']+current['size']},
                {o-previous['value']: r for o, r in old_rel.items()
                if previous['value'] <= o < previous['value']+previous['size']}, name)
        before, after, target_pool = (normalized_pools(o) for o in (*objects, self.out / 'selected.o'))
        if has_cleanup:
            self.assertEqual(before['.data'], after['.data'])
            old_raw, old_ids = before['.rodata']
            new_raw, new_ids = after['.rodata']
            self.assertEqual((len(old_raw), len(new_raw)), (192, 416))
            self.assertEqual(new_raw[:220], target_pool['.rodata'][0][:220])
            self.assertEqual(tuple(i for i in new_ids if i[1] == screen.FUNCTION), target_pool['.rodata'][1])
            self.assertEqual(new_raw[220:], old_raw+bytes(4))
            self.assertEqual(tuple((o-220, n, v) for o, n, v in new_ids if n != screen.FUNCTION), old_ids)
        else:
            self.assertEqual(before, {'.rodata': None, '.data': None})
            self.assertEqual(after, target_pool)
        isolated_text, isolated, isolated_rel = parse_object(self.out / 'selected.o')
        target = functions[screen.FUNCTION]
        self.assertEqual(target['size'], isolated[screen.FUNCTION]['size'])
        self.assertEqual(text[target['value']:target['value']+452], isolated_text[:452])
        self.assertEqual({o-target['value']: r for o, r in rel.items()
            if target['value'] <= o < target['value']+452}, isolated_rel)
        self.receipt('owner', dict(functions=len(functions), unchanged_neighbors=len(functions)-1,
            target_isolated_equal=True, added_pool_only_target_owned=True, warnings=0,
            later_cleanup_pool_preserved=has_cleanup, expected_later_pool_addend_shift=220 if has_cleanup else 0))
        return objects[1]

    def test_copied_owner_and_real_padder_fixed_anchor_rebases(self):
        assembly = emit_padded_assembly(self.qualify_owner(), self.root / 'conker/asm/5D2C0.s',
            word_patches_path=self.root / 'conker/retail_word_patches.us.csv', filename='generated_5D2C0', rodata_symbol=ANCHOR)
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        end = assembly.index('\n', end)+1
        next_function = assembly.index('.type ', end)
        tail = assembly[end:next_function]
        self.assertNotIn('.space', tail)
        asm, obj = self.out / 'padded.s', self.out / 'padded.o'
        asm.write_text('.text\n.globl %s\n' % screen.FUNCTION+assembly[start:end])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(asm)], check=True, capture_output=True)
        text, functions, relocs = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'], 452)
        self.assertNotIn('.rodata', sections(obj))
        configurations = [(screen.ENTRY, screen.TABLE, None), (screen.ENTRY+0x01000004, screen.TABLE, None),
            (screen.ENTRY, 0x90007FFC, None)]
        configurations += [(screen.ENTRY, screen.TABLE, name) for name in screen.SYMBOLS]
        for entry, anchor, rebased in configurations:
            script, elf = self.out / 'padded.ld', self.out / ('rebased-%X-%X-%s.elf' % (entry, anchor, rebased))
            script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
            symbols = dict(screen.SYMBOLS, **{ANCHOR: anchor})
            if rebased:
                symbols[rebased] += 0x01008004
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X' % item for item in symbols.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
            linked = list(struct.unpack_from('>113I', sections(elf)['.text'][1]))
            expected = self.words.copy()
            for offset, entries in relocs.items():
                kind, name = entries[0]
                address = symbols[name]
                word = struct.unpack_from('>I', text, offset)[0]
                if kind == 'R_MIPS_26':
                    expected[offset//4] = word&0xFC000000 | address>>2&0x3FFFFFF
                else:
                    addend = 60 if offset in (92, 100) else 0
                    expected[offset//4] = word&0xFFFF0000 | (((address+addend+0x8000)>>16)&65535
                        if kind == 'R_MIPS_HI16' else (address+addend)&65535)
            self.assertEqual(linked, expected)
        self.receipt('padder', dict(body_bytes=452, slot_bytes=452, padding_words=0,
            original_anchor_and_two_table_addends=True, independently_rebased_symbols=10,
            carry_rebase_and_entry_rebase=True,
            generated_pool_not_linked_or_written_to_original_data=True))

    def test_installed_slot_or_previous_stub_and_guard_history(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        installed = screen.SELECTED in source
        self.assertEqual(source.count(screen.SELECTED if installed else STUB), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        expected = self.words if installed else [0x00001025, 0x03E00008]+[0]*111
        self.assertEqual((addresses[screen.FUNCTION], functions[screen.FUNCTION]), (screen.ENTRY, expected))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed', dict(C_installed=installed, byte_exact=installed, guards_added=0))


if __name__ == '__main__':
    unittest.main()
