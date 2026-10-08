"""Node cleanup semantics, packet lifetime, exact slot and shared pool ownership."""

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

from tools.experiments import game_node_cleanup_candidates as screen
from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.patch_generated_slice_ld import load_game_data_layout
from tools.tests import test_game_node_action_match as action
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read

NODE, ALT_NODE, ACTOR, ALT_ACTOR, STATE = 0x10000, 0x11000, 0x20000, 0x22000, 0x24000
LOOKUP, REGISTER = screen.SYMBOLS['func_15083E90'], screen.SYMBOLS['func_1000FD38']
PACKETS = {screen.SYMBOLS[n]: i for n, i in (('func_151616D0', 2), ('func_15147D64', 0), ('func_151494E0', 0))}
WIDTHS = {v: 1 for v in screen.SYMBOLS.values()}
WIDTHS.update({REGISTER: 3, screen.SYMBOLS['func_151616D0']: 3,
    screen.SYMBOLS['func_15147D64']: 2, screen.SYMBOLS['func_151494E0']: 2})
STUB = 's32 func_15031C14() {\n    return 0;\n}'
ANCHOR, POOL_OFFSET = 'jtbl_80096F40_game', 220
COUNTERS, KEYS = (None, 0, 0xA9, 0xAA, 0xFFFF), (0, 0x16, 0x63, 0x89)


def fixture(pool, selector=0, key=0, counter=0):
    memory = {prior.STACK+i: 0xA5 for i in range(-0x100, 0x100)}
    memory.update({screen.TABLE+i: v for i, v in enumerate(pool)})
    for node in (NODE, ALT_NODE):
        put(memory, node, 7, 1)
        put(memory, node+1, selector, 1)
        put(memory, node+6, key, 1)
    for actor in (ACTOR, ALT_ACTOR):
        put(memory, actor+0x3B, 0xEF, 1)
        put(memory, actor+0x9C, 0xFFFFFFFF)
        put(memory, actor+0x31C, STATE if counter is not None else 0)
    put(memory, STATE+0x1A6, counter or 0, 2)
    return memory


def mutations(mode, target, stack):
    if mode == 4 and target == LOOKUP:
        return [(stack, ALT_NODE, 4)]
    if target == LOOKUP:
        return []
    if mode == 1:
        return [(NODE+1, 0x37, 1), (NODE+6, 0x89, 1)]
    if mode == 2:
        return [(stack, ALT_NODE, 4), (ALT_NODE+1, 0, 1), (ALT_NODE+6, 0x16, 1)]
    if mode == 3:
        changes = [(stack-4, ALT_ACTOR, 4)]
        if target == screen.SYMBOLS['func_15147D64']:
            changes += [(stack-28, stack-12, 4), (stack-12, ALT_ACTOR, 4), (stack-8, 0xE1, 1)]
        return changes
    return []


class CleanupReference(action.ActionReference):
    def call(self, name, arguments):
        target = screen.SYMBOLS[name]
        packet = arguments[PACKETS[target]] if target in PACKETS else None
        contents = (self.get(packet, 4), self.get(packet+4, 1)) if packet is not None else ()
        self.calls.append((target, *arguments, *contents))
        for address, value, size in mutations(self.mode, target, self.stack):
            self.put(address, value, size)
        return self.resolved if target == LOOKUP else 0xBEEF0000+len(self.calls)

    def run(self, node=NODE, resolved=ACTOR):
        self.resolved = resolved
        self.put(self.stack, node)
        result = self.call('func_15083E90', (self.get(node, 1),))
        self.put(self.stack-4, result)
        if not result:
            return result
        node = self.get(self.stack)
        selector = self.get(node+1, 1)
        if 0x37 <= selector <= 0x66:
            self.get(screen.TABLE+(selector-0x37)*4)
        if selector == 0x5A:
            state = self.get(result+0x31C)
            if state:
                self.put(state+0x1A6, self.get(state+0x1A6, 2)-0xAA, 2)
        elif selector in (0x90, 0x8F, 0x85, 0x5E):
            mask = 0x70 if selector == 0x90 else 0xE00 if selector == 0x8F else 0x6000
            self.put(result+0x9C, self.get(result+0x9C)&~mask)
        elif selector in (0x37, 0x4B, 0x4C):
            result = self.call('func_1000FD38', (screen.SYMBOLS['func_15033BDC'], node, self.get(self.stack-4)))
            node = self.get(self.stack)
            if self.get(node+1, 1) == 0x37:
                result = self.call('func_15100180', (self.get(self.stack-4),))
            node = self.get(self.stack)
        elif selector in (0x49, 0x5D):
            actor = self.get(self.stack-4)
            packet = self.stack-(12 if selector == 0x49 else 20)
            self.put(packet, actor)
            group = self.get(actor+0x3B, 1)
            if selector == 0x5D:
                self.put(self.stack-28, packet)
            self.put(packet+4, group, 1)
            if selector == 0x49:
                result = self.call('func_151616D0', (0x10, 0x29, packet))
            else:
                result = self.call('func_15147D64', (packet, 0x2E))
                result = self.call('func_151494E0', (self.get(self.stack-28), 0x2F))
            node = self.get(self.stack)
        elif selector in (0x3D, 0x1A, 0x1B, 0x5F, 0x65, 0x66, 0x1D, 0x82):
            callee = 'func_151BD7F4' if selector == 0x3D else 'func_151D747C' if selector in (0x1D, 0x82) else 'func_151D4668'
            result = self.call(callee, (self.get(self.stack-4),))
            node = self.get(self.stack)
        if self.get(node+6, 1) in (0x16, 0x63, 0x89):
            result = self.call('func_151027E8', (self.get(self.stack-4),))
            result = self.call('func_151D4668', (self.get(self.stack-4),))
        return result


class CleanupOracle(TriangleOracle):
    def __init__(self, words, memory, node=NODE, resolved=ACTOR, phase=0, mode=0):
        super().__init__(words, memory, entry=screen.ENTRY, arguments=(node,), phase=phase)
        self.stack, self.mode, self.resolved = prior.STACK+phase, mode, resolved

    def record_call(self, target):
        args = self.arguments(WIDTHS[target])
        packet = args[PACKETS[target]] if target in PACKETS else None
        contents = (self.get(packet, 4), self.get(packet+4, 1)) if packet is not None else ()
        self.calls.append((target, *args, *contents))

    def hook(self, target):
        for address, value, size in mutations(self.mode, target, self.stack):
            self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.r[2] = self.resolved if target == LOOKUP else 0xBEEF0000+len(self.calls)
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameNodeCleanupMatchTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-node-cleanup-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words, cls.pool = screen.compile_candidate(cls.root, cls.out, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>134I', cls.rom, screen.ROM))
        start, base, _, owners = load_game_data_layout(cls.root / 'conker')
        cls.original_pool = cls.rom[start+screen.TABLE-base:start+screen.TABLE-base+192]
        cls.table_owner = next(o for o in owners if o['address'] <= screen.TABLE < o['end'])
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def compare(self, memory, node=NODE, resolved=ACTOR, phase=0, mode=0):
        reference = CleanupReference(memory, phase, mode)
        expected = reference.run(node, resolved)
        models = [CleanupOracle(w, memory, node, resolved, phase, mode).run() for w in (self.words, self.retail)]
        for model in models:
            self.assertEqual((model.r[2], model.calls, prior.public(model.events), prior.external_memory(model.memory)),
                (expected, reference.calls, prior.public(reference.events), prior.external_memory(reference.memory)))
        self.assertEqual((models[0].r, models[0].f, models[0].events), (models[1].r, models[1].f, models[1].events))
        return models

    def test_direct_slot_and_complete_table(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (134, 56, 0))
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.pool, self.original_pool)
        self.assertEqual(self.table_owner['input'], 'build/asm/data/23B8A0.rodata.s.o(.rodata)')
        self.receipt('slot', dict(body_words=134, slot_words=134, frame=56, direct_differences=0,
            table_targets=48, guards_added=0, volatile_home_is_matching_annotation_not_original_source_claim=True))

    def test_all_selectors_cleanup_keys_wrap_callbacks_homes_and_coverage(self):
        seen, cases = set(), 0
        for selector, key, counter, mode, phase in itertools.product(range(256), KEYS, COUNTERS, range(5), (0, 8)):
            for model in self.compare(fixture(self.pool, selector, key, counter), phase=phase, mode=mode):
                seen.update(model.visits)
            cases += 1
        for selector, key in itertools.product(range(256), KEYS):
            self.compare(fixture(self.pool, selector, key), resolved=0)
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+536, 4))-seen)
        self.assertEqual(missing, [55])
        self.receipt('guest', dict(cases=cases, null_actor_cases=1024, selector_bytes=256, cleanup_keys=4,
            counter_states=5, callback_modes=5, SP_phases=2, missing_word_indices=missing,
            missing_only_unreachable_duplicate_load=True, GP_FP_V0_events_and_memory_equal=True,
            private_packet_pointer_and_cached_actor_redirection_checked=True, complete_callees_not_claimed=True))

    def test_lazy_null_actor_and_required_storage_fault_prefixes(self):
        memory = fixture(self.pool)
        del memory[NODE+1], memory[NODE+6]
        self.compare(memory, resolved=0)
        probes = ((0, NODE), (0, NODE+1), (0, NODE+6), (0x90, ACTOR+0x9C),
            (0x5A, ACTOR+0x31C), (0x5A, STATE+0x1A6), (0x49, ACTOR+0x3B),
            (0x5D, ACTOR+0x3B), (0x37, screen.TABLE))
        for selector, missing in probes:
            memory = fixture(self.pool, selector)
            del memory[missing]
            reference = CleanupReference(memory)
            with self.assertRaises(AssertionError) as failure:
                reference.run()
            for words in (self.words, self.retail):
                model = CleanupOracle(words, memory)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args, failure.exception.args)
                self.assertEqual((model.calls, prior.public(model.events), prior.external_memory(model.memory)),
                    (reference.calls, prior.public(reference.events), prior.external_memory(reference.memory)))
        self.receipt('gates', dict(lazy_null_actor_cases=1, required_faults=len(probes), ordered_fault_prefixes_equal=True))

    def test_source_profile_controls_and_effective_semantic_negatives(self):
        forms = [(n, b, 'o2g3') for n, b in screen.candidates()]
        forms += [('profile-'+p, screen.SELECTED, p) for p in PROFILES if p != 'o2g3']
        records = []
        for name, body, profile in forms:
            record, words, pool = screen.compile_candidate(self.root, self.out, name, body, profile)
            for selector in range(256):
                memory = fixture(pool, selector, 0x89, 0xFFFF)
                reference = CleanupReference(memory)
                expected = reference.run()
                model = CleanupOracle(words, memory).run()
                # Control frames differ, so compare packet contents, not their private addresses.
                def calls(c):
                    return [tuple(v for i, v in enumerate(row) if row[0] not in PACKETS or i != PACKETS[row[0]]+1) for row in c]
                self.assertEqual((calls(model.calls), prior.external_memory(model.memory)),
                    (calls(reference.calls), prior.external_memory(reference.memory)), name)
            records.append(record)
        for name, body, selector in (
                ('wrong-counter-direction', screen.SELECTED.replace('-= 0xAA', '+= 0xAA'), 0x5A),
                ('wrong-flag-direction', screen.SELECTED.replace('&= ~0x70', '|= 0x70'), 0x90),
                ('missing-cleanup-key', screen.SELECTED.replace('        case 0x89:\n', ''), 0),
                ('wrong-paired-event', screen.SELECTED.replace('packet, 0x2F', 'packet, 0x2E'), 0x5D)):
            _, words, pool = screen.compile_candidate(self.root, self.out, name, body)
            memory = fixture(pool, selector, 0x89, 0)
            reference = CleanupReference(memory)
            reference.run()
            model = CleanupOracle(words, memory).run()
            self.assertNotEqual((model.calls, prior.external_memory(model.memory)),
                (reference.calls, prior.external_memory(reference.memory)), name)
        self.receipt('controls', dict(forms=len(forms), ordinary_executions=len(forms)*256,
            raw_exact_forms=sum(r['differences'] == 0 for r in records), measurements=records,
            effective_semantic_negatives=4, private_homes_not_claimed_for_control_forms=True))

    def test_native32_complete_C_public_effects_and_packet_mutation(self):
        self.fixture = '''typedef unsigned char u8;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;
typedef union {u32 align;u8 b[0x340];} Storage;
typedef char pointer_width[(sizeof(void *)==4)?1:-1];
''' + screen.DECLARATIONS + r'''
typedef char packet_size[(sizeof(NodeCleanupPacket)==8)?1:-1];
typedef char packet_group[(__builtin_offsetof(NodeCleanupPacket,group)==4)?1:-1];
static Storage node,actor,state;static int mode,count,is_null;static u32 log[6][6];
static void call(u32 target,u32 a,u32 b,u32 c,NodeCleanupPacket *p){
    log[count][0]=target;log[count][1]=a;log[count][2]=b;log[count][3]=c;
    log[count][4]=p?(u32)p->actor:0;log[count][5]=p?p->group:0;count++;
    if(target==0x15083E90)return;
    if(mode==1){node.b[1]=0x37;node.b[6]=0x89;}
    if(mode==2&&p){p->group=0xE1;p->actor=state.b;}
}
u8 *func_15083E90(s32 a){call(0x15083E90,a,0,0,0);return is_null?0:actor.b;}
s32 func_15033BDC(){return 0;}
void func_1000FD38(s32 (*a)(),u8 *b,u8 *c){call(0x1000FD38,(u32)a,(u32)b,(u32)c,0);}
void func_15100180(u8 *a){call(0x15100180,(u32)a,0,0,0);}
void func_151616D0(s32 a,s32 b,NodeCleanupPacket *p){call(0x151616D0,a,b,0,p);}
void func_15147D64(NodeCleanupPacket *p,s32 b){call(0x15147D64,0,b,0,p);}
void func_151494E0(NodeCleanupPacket *p,s32 b){call(0x151494E0,0,b,0,p);}
void func_151BD7F4(u8 *a){call(0x151BD7F4,(u32)a,0,0,0);}
void func_151D4668(u8 *a){call(0x151D4668,(u32)a,0,0,0);}
void func_151D747C(u8 *a){call(0x151D747C,(u32)a,0,0,0);}
void func_151027E8(u8 *a){call(0x151027E8,(u32)a,0,0,0);}
static void init(int action,int key,int counter,int kind,int null_actor){int i,j;count=0;mode=kind;is_null=null_actor;
    for(i=0;i<0x340;i++)node.b[i]=actor.b[i]=state.b[i]=0xA5;
    for(i=0;i<6;i++)for(j=0;j<6;j++)log[i][j]=0;
    node.b[0]=7;node.b[1]=action;node.b[6]=key;actor.b[0x3B]=0xEF;
    *(u8 **)(actor.b+0x31C)=counter<0?0:state.b;*(u16 *)(state.b+0x1A6)=counter<0?0:counter;
    *(u32 *)(actor.b+0x9C)=0xFFFFFFFF;
}
static void reference(u8 *n){u8 *a=func_15083E90(n[0]),*s;int action;NodeCleanupPacket p;
    if(!a)return;
    action=n[1];
    if(action==0x5A){s=*(u8 **)(a+0x31C);if(s)*(u16 *)(s+0x1A6)-=0xAA;}
    else if(action==0x90||action==0x8F||action==0x85||action==0x5E)
        *(u32 *)(a+0x9C)&=~(action==0x90?0x70:action==0x8F?0xE00:0x6000);
    else if(action==0x37||action==0x4B||action==0x4C){func_1000FD38(func_15033BDC,n,a);if(n[1]==0x37)func_15100180(a);}
    else if(action==0x49||action==0x5D){p.actor=a;p.group=a[0x3B];
        if(action==0x49)func_151616D0(0x10,0x29,&p);
        else{func_15147D64(&p,0x2E);func_151494E0(&p,0x2F);}}
    else if(action==0x3D)func_151BD7F4(a);
    else if(action==0x1D||action==0x82)func_151D747C(a);
    else if(action==0x1A||action==0x1B||action==0x5F||action==0x65||action==0x66)func_151D4668(a);
    if(n[6]==0x16||n[6]==0x63||n[6]==0x89){func_151027E8(a);func_151D4668(a);}
}
''' + screen.SELECTED
        self.run_host(r'''
static int keys[4]={0,0x16,0x63,0x89},counters[5]={-1,0,0xA9,0xAA,0xFFFF};
Storage saved[3];u32 savedlog[6][6];int action,k,c,m,n,i,j,expected_count;
for(action=0;action<256;action++)for(k=0;k<4;k++)for(c=0;c<5;c++)for(m=0;m<3;m++)for(n=0;n<2;n++){
    init(action,keys[k],counters[c],m,n);reference(node.b);saved[0]=node;saved[1]=actor;saved[2]=state;
    expected_count=count;for(i=0;i<6;i++)for(j=0;j<6;j++)savedlog[i][j]=log[i][j];
    init(action,keys[k],counters[c],m,n);func_15031C14(node.b);
    if(count!=expected_count)return 1;
    for(i=0;i<0x340;i++)if(node.b[i]!=saved[0].b[i]||actor.b[i]!=saved[1].b[i]||state.b[i]!=saved[2].b[i])return 2;
    for(i=0;i<6;i++)for(j=0;j<6;j++)if(log[i][j]!=savedlog[i][j])return 3;
}
''')
        self.receipt('native', dict(cases=256*4*5*3*2, pointer_bytes=4, packet_bytes=8, packet_group_offset=4,
            complete_actual_void_C=True, callback_mutated_packet_reused=True, all_object_bytes_and_call_ABI_checked=True,
            defined_C_return_guest_private_homes_full_callees_and_hardware_not_claimed=True))

    def qualify_owner(self):
        from tools.experiments import game_node_selection_candidates as selection
        from tools.tests.game_owner_pool import rebind_selection_neighbor

        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        has_selection = selection.SELECTED in source
        if screen.SELECTED in source:
            source = source.replace(screen.SELECTED, STUB).replace(screen.DECLARATIONS+'\n', '', 1)
        self.assertEqual(source.count(STUB), 1)
        selected = source.replace(STUB, screen.SELECTED).replace('#include <ultra64.h>\n',
            '#include <ultra64.h>\n'+screen.DECLARATIONS+'\n', 1)
        # The later effect caller still needs these when cleanup is replaced by its stub.
        shared = 's32 func_15033BDC();\nvoid func_1000FD38(s32 (*)(), u8 *, u8 *);\n'
        source = source.replace('#include <ultra64.h>\n', '#include <ultra64.h>\n'+shared, 1)
        self.assertEqual(source.count(shared), 1)
        self.assertEqual(selected.count(shared), 1)
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
            expected_text = old_text[previous['value']:previous['value']+previous['size']]
            if has_selection and name == selection.FUNCTION:
                expected_text = rebind_selection_neighbor(self,expected_text,*objects,220)
            self.assertEqual(text[current['value']:current['value']+current['size']],
                expected_text, name)
            self.assertEqual({o-current['value']: r for o, r in rel.items() if current['value'] <= o < current['value']+current['size']},
                {o-previous['value']: r for o, r in old_rel.items() if previous['value'] <= o < previous['value']+previous['size']}, name)
        before, after, isolated = (normalized_pools(o) for o in (*objects, self.out / 'selected.o'))
        self.assertEqual(before['.data'], after['.data'])
        old_raw, old_ids = before['.rodata']
        new_raw, new_ids = after['.rodata']
        old_end = 220+(2696 if has_selection else 0)
        new_end = old_end+192
        self.assertEqual((len(old_raw),len(new_raw)),((old_end+15)//16*16,(new_end+15)//16*16))
        self.assertEqual(old_raw[old_end:],bytes(len(old_raw)-old_end))
        self.assertEqual(new_raw[:220], old_raw[:220])
        self.assertEqual(new_raw[412:new_end],old_raw[220:old_end])
        self.assertEqual(tuple((o-(192 if o>=412 else 0),n,v) for o,n,v in new_ids
            if n != screen.FUNCTION),old_ids)
        self.assertEqual(tuple((o-220, n, v) for o, n, v in new_ids if n == screen.FUNCTION), isolated['.rodata'][1])
        self.assertEqual(new_raw[220:412], isolated['.rodata'][0])
        self.assertEqual(new_raw[new_end:],bytes(len(new_raw)-new_end))
        target = functions[screen.FUNCTION]
        isolated_text, _, isolated_rel = parse_object(self.out / 'selected.o')
        expected_text = bytearray(isolated_text[:536])
        self.assertEqual(isolated_rel[132], [('R_MIPS_LO16', '.rodata')])
        table_load = struct.unpack_from('>I', expected_text, 132)[0]
        self.assertEqual(table_load&65535, 0)
        struct.pack_into('>I', expected_text, 132, table_load+POOL_OFFSET)
        self.assertEqual(text[target['value']:target['value']+536], expected_text)
        target_rel = {o-target['value']: r for o, r in rel.items() if target['value'] <= o < target['value']+536}
        self.assertEqual(target_rel, isolated_rel)
        self.receipt('owner', dict(functions=len(functions), unchanged_neighbors=len(functions)-1,
            existing_pool_targets_preserved=len(old_ids),added_targets=48,generated_pool_bytes=len(new_raw),
            retained_selection_table_targets=674 if has_selection else 0,
            checked_selection_LO_addend_shifts=7 if has_selection else 0,
            cleanup_pool_addend=220,end_alignment_bytes=len(new_raw)-new_end,strict_diagnostics=0))
        return objects[1]

    def test_copied_owner_padder_fixed_pool_offset_and_symbol_rebases(self):
        assembly = emit_padded_assembly(self.qualify_owner(), self.root / 'conker/asm/5D2C0.s',
            word_patches_path=self.root / 'conker/retail_word_patches.us.csv', filename='generated_5D2C0', rodata_symbol=ANCHOR)
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        end = assembly.index('\n', end)+1
        self.assertNotIn('.space', assembly[end:assembly.index('.type ', end)])
        asm, obj = self.out / 'padded.s', self.out / 'padded.o'
        asm.write_text('.text\n.globl %s\n' % screen.FUNCTION+assembly[start:end])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(asm)], check=True, capture_output=True)
        text, functions, relocs = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'], 536)
        self.assertNotIn('.rodata', sections(obj))
        configurations = [(screen.ENTRY, action.screen.TABLE, None), (screen.ENTRY+0x01000004, action.screen.TABLE, None),
            (screen.ENTRY, 0x90007FFC, None)]
        configurations += [(screen.ENTRY, action.screen.TABLE, name) for name in screen.SYMBOLS]
        for entry, anchor, rebased in configurations:
            script, elf = self.out / 'padded.ld', self.out / ('rebased-%X-%X-%s.elf' % (entry, anchor, rebased))
            script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
            symbols = dict(screen.SYMBOLS, **{ANCHOR: anchor})
            if rebased:
                symbols[rebased] += 0x01008004
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X' % item for item in symbols.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = self.words.copy()
            for offset, entries in relocs.items():
                kind, name = entries[0]
                address = symbols[name]+(220 if name == ANCHOR else 0)
                word = struct.unpack_from('>I', text, offset)[0]
                expected[offset//4] = (word&0xFC000000 | address>>2&0x3FFFFFF) if kind == 'R_MIPS_26' else (
                    word&0xFFFF0000 | (((address+0x8000)>>16)&65535 if kind == 'R_MIPS_HI16' else address&65535))
            self.assertEqual(list(struct.unpack_from('>134I', sections(elf)['.text'][1])), expected)
        self.receipt('padder', dict(body_bytes=536, slot_bytes=536, padding_words=0, fixed_pool_offset=220,
            independently_rebased_symbols=len(screen.SYMBOLS)+1, carry_and_entry_rebases=True,
            generated_pool_not_linked_or_written_to_original_data=True))

    def test_installed_slot_or_previous_stub_and_guard_history(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        installed = screen.SELECTED in source
        self.assertEqual(source.count(screen.SELECTED if installed else STUB), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        expected = self.words if installed else [0x00001025, 0x03E00008]+[0]*132
        self.assertEqual((addresses[screen.FUNCTION], functions[screen.FUNCTION]), (screen.ENTRY, expected))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed', dict(C_installed=installed, byte_exact=installed, guards_added=0))


if __name__ == '__main__':
    unittest.main()
