"""Direct leaf match, ordinal boundaries, lazy reads and connected resolver."""

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

from tools.experiments import game_matrix_parent_lookup_candidates as screen
from tools.experiments import game_matrix_pair_resolver_candidates as pair
from tools.experiments import game_matrix_pair_resolver_key_candidates as key
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.experiments.game_actor_classifier_candidates import sections
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools

ACTOR, NODES = 0x10000, 0x20000
KEYS = (0x80000000, 0xFFFFFFFF, 0, 1, 37, 255, 256, 65535)
ORDINALS = (0, 1, 2, 3, 4, 0x7FFFFFFF, 0x80000000, 0xFFFFFFFF)
ENTRIES = ((3, 37), (255, 37), (3, 255), (3, 37), (0, 37), (3, 37), (1, 0))
ASM = '#pragma GLOBAL_ASM("asm/nonmatchings/generated_5D2C0/func_1503195C.s")'


def fixture(group=3, length=7, rotation=0):
    memory = {ACTOR+0x3B: group}
    put(memory, screen.HEAD, NODES if length else 0)
    for i in range(length):
        node = NODES+i*0x60
        identity, key_value = ENTRIES[(i+rotation) % len(ENTRIES)]
        memory[node], memory[node+6] = identity, key_value
        put(memory, node+0x54, node+0x60 if i+1 < length else 0)
    return memory


class LookupReference:
    def __init__(self, memory):
        self.memory, self.events = dict(memory), []

    def get(self, address, size):
        address &= 0xFFFFFFFF
        assert all(address+i in self.memory for i in range(size)), ('unmapped read', address, size)
        value = read(self.memory, address, size)
        self.events.append(('R', address, size, value))
        return value

    def run(self, actor, key_value, ordinal):
        group = self.get(actor+0x3B, 1)
        if not group:
            return 0
        node = self.get(screen.HEAD, 4)
        while node:
            identity = self.get(node, 1)
            next_node = self.get(node+0x54, 4)
            if group == identity and key_value == self.get(node+6, 1):
                if ordinal == 0:
                    return node
                ordinal = (ordinal-1)&0xFFFFFFFF
            node = next_node
        return 0


class GameMatrixParentLookupMatchTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-matrix-parent-lookup-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>28I', rom, screen.ROM))
        cls.resolver_record, cls.resolver = pair.compile_candidate(cls.root, cls.out, 'resolver', key.SELECTED)
        cls.retail_resolver = list(struct.unpack_from('>85I', rom, pair.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def model(self, words, memory, args, phase=0):
        return TriangleOracle(words, memory, entry=screen.ENTRY, arguments=args, phase=phase)

    def compare(self, memory, args, phase=0, words=None):
        reference = LookupReference(memory)
        expected = reference.run(*args)
        models = [self.model(body, memory, args, phase).run() for body in (words or self.words, self.retail)]
        for model in models:
            self.assertEqual((model.r[2], model.events, model.calls), (expected, reference.events, []))
            self.assertTrue(all(model.memory[address] == value for address, value in memory.items()))
            self.assertFalse(any(event[0] == 'W' for event in model.events))
        self.assertEqual(models[0].r, models[1].r)
        return models

    def test_all_twenty_eight_words_direct_and_zero_frame(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (28, 0, 0))
        self.assertEqual((self.record['diagnostics'], self.record['pool_bytes']), ('', 0))
        self.assertEqual(self.words, self.retail)
        self.assertEqual(len(self.record['relocations']), 2)
        self.receipt('slot', dict(body_words=28, slot_words=28, bytes=112, frame=0,
            direct_word_differences=0, guards_added=0, default_o2g3_profile=True))

    def test_all_byte_groups_keys_full_word_ordinals_and_loop_coverage(self):
        cases, coverage = 0, set()
        for group, key_value, ordinal, length, rotation, phase in itertools.product(
                (0, 1, 3, 255), KEYS, ORDINALS, (0, 1, 4, 7), range(3), (0, 8)):
            memory = fixture(group, length, rotation)
            for model in self.compare(memory, (ACTOR, key_value, ordinal), phase):
                coverage.update(model.visits)
            cases += 1
        for value, ordinal in itertools.product(range(256), (0, 1)):
            self.compare(fixture(value), (ACTOR, 37, ordinal))
            self.compare(fixture(3), (ACTOR, value, ordinal))
            cases += 2
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+112, 4))-coverage)
        self.assertEqual(missing, [22])
        self.receipt('guest', dict(cases=cases, missing_word_indices=missing,
            unreachable_duplicate_move_only=True, all_byte_groups_and_keys=True,
            high_and_negative_argument_bits_not_truncated=True, both_SP_phases=True,
            no_writes_or_calls=True, saved_registers_SP_GP_RA_checked=True))

    def test_lazy_reads_required_next_word_and_invalid_actor_have_no_added_gates(self):
        models = self.compare({ACTOR+0x3B: 0}, (ACTOR, 37, 0))
        self.assertEqual(models[0].events, [('R', ACTOR+0x3B, 1, 0)])
        self.compare(fixture(3, 0), (ACTOR, 37, 0))
        probes = [(fixture(), (0, 37, 0), None),
            (fixture(), (ACTOR, 37, 0), ACTOR+0x3B),
            (fixture(), (ACTOR, 37, 0), screen.HEAD),
            (fixture(), (ACTOR, 37, 0), NODES),
            (fixture(), (ACTOR, 37, 0), NODES+0x54),
            (fixture(), (ACTOR, 37, 0), NODES+6),
            (fixture(), (ACTOR, 37, 1), NODES+0x60),
            (fixture(), (ACTOR, 37, 1), NODES+0x60+0x54),
            (fixture(), (ACTOR, 37, 1), NODES+3*0x60+6)]
        for memory, args, missing in probes:
            if missing is not None:
                memory.pop(missing)
            reference = LookupReference(memory)
            with self.assertRaises(AssertionError) as failure:
                reference.run(*args)
            for words in (self.words, self.retail):
                model = self.model(words, memory, args)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args, failure.exception.args)
                self.assertEqual(model.events, reference.events)
                self.assertTrue(all(model.memory[address] == value for address, value in memory.items()))
        self.receipt('gates', dict(lazy_cases=2, required_read_faults=len(probes),
            next_pointer_required_even_for_first_return=True, no_actor_null_gate=True,
            no_head_access_for_zero_actor_group=True, bounded_acyclic_fixtures_only=True))

    def test_source_and_profile_controls_preserve_ordinary_behavior(self):
        forms = [(name, body, 'o2g3') for name, body in screen.candidates()]
        bodies = dict(screen.candidates())
        forms += [(name+'-'+profile, bodies[name], profile) for name, profile in itertools.product(
            ('u32-u32-separate-nested', 'flow-current-continue-post0'), ('o2', 'o1g3', 'o1'))]
        self.assertEqual(len(forms), 58)
        executions, exact, records = 0, [], []
        for name, body, profile in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile)
            for group, key_value, ordinal, phase in itertools.product((0, 3, 255), (37, 256), (0, 1, 3, 0xFFFFFFFF), (0, 8)):
                memory = fixture(group)
                memory.update({prior.STACK+i: 0xA5 for i in range(-0x100, 0x100)})
                reference = LookupReference(memory)
                expected = reference.run(ACTOR, key_value, ordinal)
                model = self.model(words, memory, (ACTOR, key_value, ordinal), phase).run()
                self.assertEqual(model.r[2], expected, name)
                self.assertEqual(prior.external_memory(model.memory), prior.external_memory(memory), name)
                executions += 1
            if record['differences'] == 0:
                exact.append(name)
            records.append(record)
        self.assertEqual(exact, ['combined-inverse1-advance1'])
        self.receipt('controls', dict(forms=len(forms), ordinary_executions=executions, raw_exact=exact,
            measurements=records, required_read_order_and_private_stack_not_claimed_for_all_controls=True))

    def test_native_32bit_complete_C_valid_objects_and_unsigned_ordinal(self):
        self.fixture = r'''typedef unsigned char u8;typedef unsigned int u32;typedef int s32;
typedef union {u32 alignment;u8 bytes[0x60];} Node;
typedef char pointer_width[(sizeof(void *)==4)?1:-1];
static Node nodes[7];static u8 actor[0x40];u8 *D_800C3EE0;
static u32 groups[7]={3,255,3,3,0,3,1},keys[7]={37,37,255,37,37,37,0};
static void init(int length,int rotation){int i,j;
    for(i=0;i<7;i++){for(j=0;j<0x60;j++)nodes[i].bytes[j]=0xA5;
        nodes[i].bytes[0]=groups[(i+rotation)%7];nodes[i].bytes[6]=keys[(i+rotation)%7];
        *(u8 **)(nodes[i].bytes+0x54)=i+1<length?nodes[i+1].bytes:0;
    }D_800C3EE0=length?nodes[0].bytes:0;
}
static s32 reference(u8 *a,s32 key,u32 ordinal){u8 *cur;
    if(a[0x3B]==0)return 0;
    for(cur=D_800C3EE0;cur;cur=*(u8 **)(cur+0x54)){
        if(cur[0]==a[0x3B]&&cur[6]==key){if(ordinal==0)return (s32)cur;ordinal--;}
    }return 0;
}
''' + screen.SELECTED+'\n'
        self.run_host(r'''
int group,key,index,length,rotation,i,j;static u32 ordinals[8]={0,1,2,3,4,0x7FFFFFFF,0x80000000,0xFFFFFFFF};
static s32 extraKeys[4]={-1,(s32)0x80000000,256,65535};s32 expected,actual;Node saved[7];
for(rotation=0;rotation<3;rotation++)for(length=0;length<=7;length++){
    init(length,rotation);for(i=0;i<7;i++)saved[i]=nodes[i];
    for(group=0;group<256;group++)for(key=0;key<260;key++)for(index=0;index<8;index++){
        s32 value=key<256?key:extraKeys[key-256];actor[0x3B]=group;
        expected=reference(actor,value,ordinals[index]);
        actual=func_1503195C(actor,value,ordinals[index]);if(actual!=expected)return 1;
    }
    for(i=0;i<7;i++)for(j=0;j<0x60;j++)if(nodes[i].bytes[j]!=saved[i].bytes[j])return 2;
}
actor[0x3B]=0;D_800C3EE0=(u8 *)1;if(func_1503195C(actor,37,0))return 3;
''')
        self.receipt('native', dict(cases=3*8*256*260*8, lazy_cases=1, pointer_bytes=4,
            actual_complete_C=True, valid_node_objects=True, unsigned_ordinal_wrap_defined=True,
            native_fault_or_private_contract_not_claimed=True))

    def test_actual_recursive_resolver_connection_with_C_and_retail_lookup(self):
        executions = 0
        for kind, page, phase in itertools.product(range(8), range(2), (0, 8)):
            memory, args = prior.fixture(kind, page)
            reference = prior.PairReference(memory, phase)
            expected = reference.run(*args)
            models = []
            for resolver, lookup in itertools.product((self.resolver, self.retail_resolver), (self.words, self.retail)):
                connected = dict(zip(range(screen.ENTRY, screen.ENTRY+112, 4), lookup))
                model = prior.PairOracle(resolver, memory, args, phase, connected=connected).run()
                self.assertEqual((prior.external_memory(model.memory), model.calls, model.r[2]),
                    (prior.external_memory(reference.memory), reference.calls, expected))
                models.append(model)
                executions += 1
            self.assertTrue(all(prior.public(model.events) == prior.public(models[0].events) for model in models))
        self.receipt('connected', dict(cases=32, executions=executions, four_C_retail_combinations=True,
            actual_28_word_lookup=True, actual_recursive_resolver=True,
            four_parent_chain=True, full_wrapper_private_contract_not_claimed=True))

    def test_effective_compiled_key_predicate_and_mismatch_ordinal_negatives(self):
        forms = dict(truncated_key=screen.SELECTED.replace('key == current[6]', '(u8)key == current[6]'),
            either_predicate=screen.SELECTED.replace('group == current[0] && key == current[6]',
                'group == current[0] || key == current[6]'),
            decrement_on_mismatch=screen.SELECTED.replace('            } else {\n                current = next;',
                '            } else {\n                ordinal--;\n                current = next;'))
        args = dict(truncated_key=(ACTOR, 256, 0), either_predicate=(ACTOR, 255, 0),
            decrement_on_mismatch=(ACTOR, 37, 2))
        for name, body in forms.items():
            self.assertNotEqual(body, screen.SELECTED)
            _, words = screen.compile_candidate(self.root, self.out, 'negative-'+name, body)
            memory = fixture(1 if name == 'truncated_key' else 3)
            expected = LookupReference(memory).run(*args[name])
            actual = self.model(words, memory, args[name]).run()
            self.assertNotEqual(actual.r[2], expected, name)
        self.receipt('negatives', dict(compiled_effective_return_negatives=list(forms),
            no_fault_accepted_as_behavioral_difference=True))

    def qualify_owner(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        if screen.SELECTED in source:
            self.assertEqual(source.count(screen.SELECTED), 1)
            source = source.replace(screen.SELECTED, ASM)
        self.assertEqual(source.count(ASM), 1)
        objects = []
        for name, body in (('baseline', source), ('selected', source.replace(ASM, screen.SELECTED))):
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
            previous = old_functions[name]
            self.assertEqual(current['size'], previous['size'], name)
            self.assertEqual(text[current['value']:current['value']+current['size']],
                old_text[previous['value']:previous['value']+previous['size']], name)
            self.assertEqual({o-current['value']: r for o, r in rel.items()
                if current['value'] <= o < current['value']+current['size']},
                {o-previous['value']: r for o, r in old_rel.items()
                if previous['value'] <= o < previous['value']+previous['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        standalone, isolated, isolated_rel = parse_object(self.out / 'selected.o')
        target = functions[screen.FUNCTION]
        self.assertEqual(target['size'], isolated[screen.FUNCTION]['size'])
        self.assertEqual(text[target['value']:target['value']+112], standalone[:112])
        self.assertEqual({o-target['value']: r for o, r in rel.items()
            if target['value'] <= o < target['value']+112}, isolated_rel)
        self.receipt('owner', dict(functions=len(functions), unchanged_neighbors=len(functions)-1,
            target_and_neighbors_identical_to_asm=True, pools_and_relocations_equal=True, warnings=0))
        return objects[1]

    def test_copied_owner_all_function_bytes_pools_relocations_and_warnings_unchanged(self):
        self.qualify_owner()

    def test_real_generated_padder_keeps_leaf_size_and_rebases_head_HI_LO(self):
        owner = self.qualify_owner()
        assembly = emit_padded_assembly(owner, self.root / 'conker/asm/5D2C0.s',
            word_patches_path=self.root / 'conker/retail_word_patches.us.csv', filename='generated_5D2C0')
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        end = assembly.index('\n', end)+1
        next_function = assembly.index('.globl ', end)
        self.assertFalse(assembly[end:next_function].strip())
        asm, obj = self.out / 'padded.s', self.out / 'padded.o'
        asm.write_text('.text\n.globl %s\n' % screen.FUNCTION+assembly[start:next_function])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(asm)], check=True, capture_output=True)
        _, functions, relocs = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'], 112)
        self.assertEqual(relocs, parse_object(self.out / 'selected.o')[2])
        for address in (screen.HEAD, screen.HEAD+0x01008004):
            elf = self.out / ('head-%X.elf' % address)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'parent-lookup.ld'),
                '-e', screen.FUNCTION, '--defsym=D_800C3EE0=0x%X' % address, '-o', str(elf), str(obj)],
                check=True, capture_output=True)
            expected = self.words.copy()
            expected[1] = expected[1]&0xFFFF0000 | (address+0x8000)>>16&65535
            expected[6] = expected[6]&0xFFFF0000 | address&65535
            self.assertEqual(list(struct.unpack_from('>28I', sections(elf)['.text'][1])), expected)
        self.receipt('padder', dict(body_bytes=112, slot_bytes=112, extra_padding_words=0,
            symbolic_head_HI_LO_relocations=2, original_and_carry_rebased_link_exact=True))

    def test_installed_slot_and_all_existing_guards(self):
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual((addresses[screen.FUNCTION], functions[screen.FUNCTION]), (screen.ENTRY, self.words))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed', dict(exact=True, guards_added=0,
            C_source_installed=screen.SELECTED in (self.root / 'conker/src/game/generated_5D2C0.c').read_text()))


if __name__ == '__main__':
    unittest.main()
