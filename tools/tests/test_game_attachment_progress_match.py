"""Attachment setup ABI, post-call homes/rereads and single-precision boundary."""

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

from tools.experiments import game_attachment_progress_candidates as screen
from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools

NODE, ALT_NODE, ATTACHMENT, ALT_ATTACHMENT = 0x10000, 0x11000, 0x20000, 0x21000
FLAGS = (0, 1, 0x7FFF, 0x8000, 0x8001, 0xFFFF)
FLOATS = (0, 0x80000000, 0xBF800000, 0x3F800000, 0x3F7FFFFF, 0x3F800001,
    0x40000000, 0x40400000, 0x40800000, 0x40A00000, 0x40A00001, 0x407FFFFF,
    0xC0800000, 0xC0A00000, 0x4B800000, 0x4B800001, 0x7F7FFFFF, 0xFF7FFFFF,
    0x7F800000, 0xFF800000, 0x7FC00001, 0xFFC12345, 1, 0x80000001, 0x00800000)
MODES = (0, 1, 2, 3, 4, 7)
STUB = 's32 func_1503327C() {\n    return 0;\n}'


def fixture(flags=0, current=0, end=0x40800000, attached=ATTACHMENT):
    memory = {prior.STACK+i: 0xA5 for i in range(-0x100, 0x100)}
    put(memory, NODE+0x48, attached)
    put(memory, ALT_NODE+0x48, ALT_ATTACHMENT)
    for address, cur, limit in ((attached or ATTACHMENT, current, end),
            (ALT_ATTACHMENT, 0x41200000, 0x40800000)):
        put(memory, address+4, flags, 2)
        put(memory, address+8, cur)
        put(memory, address+0x18, limit)
    return memory


def actions(mode, node, attached, stack):
    return {0: [], 1: [(node+0x48, ALT_ATTACHMENT)],
        2: [(stack, ALT_NODE)],
        3: [(attached+8, 0x41200000), (attached+0x18, 0x40800000)],
        4: [(stack+4, 0xFFFFFFFF)], 5: [(node+0x48, 0)], 6: [(stack, 0)],
        7: [(node+0x48, 0), (stack, ALT_NODE)]}[mode]


class ProgressReference:
    def __init__(self, memory, phase=0, mode=0):
        self.memory, self.events, self.calls = dict(memory), [], []
        self.stack, self.mode = prior.STACK+phase, mode

    def get(self, address, size=4):
        address &= 0xFFFFFFFF
        assert all(address+i in self.memory for i in range(size)), ('unmapped read', address, size)
        value = read(self.memory, address, size)
        self.events.append(('R', address, size, value))
        return value

    def put(self, address, value):
        self.events.append(('W', address, 4, value&0xFFFFFFFF))
        assert all(address+i in self.memory for i in range(4)), ('unmapped store', address, 4)
        put(self.memory, address, value&0xFFFFFFFF)

    def run(self, node, actor):
        self.put(self.stack, node)
        self.put(self.stack+4, actor)
        attached = self.get(node+0x48)
        if not attached:
            return 0
        if self.get(attached+4, 2)&0x8000 != 0x8000:
            self.calls.append((screen.SETUP, attached, 0, 0, 0x3F800000, 0, 1))
            for address, value in actions(self.mode, node, attached, self.stack):
                self.put(address, value)
            node = self.get(self.stack)
            attached = self.get(node+0x48)
        end = self.get(attached+0x18)
        current = self.get(attached+8)
        threshold = floating(bits(floating(end)-1.0))
        return int(threshold <= floating(current))


class ProgressOracle(TriangleOracle):
    def __init__(self, words, memory, args, phase=0, mode=0):
        super().__init__(words, memory, entry=screen.ENTRY, arguments=args, phase=phase)
        self.node, self.stack, self.mode = args[0], prior.STACK+phase, mode

    def record_call(self, target):
        assert target == screen.SETUP
        arguments = self.arguments(6)
        assert arguments[1:] == (0, 0, 0x3F800000, 0, 1), arguments
        self.calls.append((target, *arguments))

    def hook(self, target):
        assert target == screen.SETUP
        for address, value in actions(self.mode, self.node, self.calls[-1][1], self.stack):
            self.put(address, value, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]
        self.condition = True


class GameAttachmentProgressMatchTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-attachment-progress-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        cls.retail = list(struct.unpack_from('>43I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def compare(self, memory, args=(NODE, 0), phase=0, mode=0, words=None):
        reference = ProgressReference(memory, phase, mode)
        expected = reference.run(*args)
        models = [ProgressOracle(body, memory, args, phase, mode).run() for body in (words or self.words, self.retail)]
        for model in models:
            self.assertEqual((model.r[2], model.calls, prior.public(model.events), prior.external_memory(model.memory)),
                (expected, reference.calls, prior.public(reference.events), prior.external_memory(reference.memory)))
            self.assertEqual(read(model.memory, prior.STACK+phase), read(reference.memory, prior.STACK+phase))
            self.assertEqual(read(model.memory, prior.STACK+phase+4), read(reference.memory, prior.STACK+phase+4))
        self.assertEqual((models[0].r, models[0].f), (models[1].r, models[1].f))
        self.assertEqual(models[0].events, models[1].events)
        return models

    def test_complete_direct_slot_frame_and_standard_profile(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (43, 40, 0))
        self.assertEqual((self.record['diagnostics'], self.record['pool_bytes']), ('', 0))
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.record['relocations'], {88: [('R_MIPS_26', 'func_1503F5B8')]})
        self.receipt('slot', dict(body_words=43, slot_words=43, frame=40, direct_differences=0,
            default_o2g3_profile=True, guards_added=0, argument_homes_and_reload_direct=True))

    def test_flags_float_boundaries_NaNs_setup_mutations_and_word_coverage(self):
        cases, seen = 0, set()
        for flag, current, end, mode, phase in itertools.product(FLAGS, FLOATS, FLOATS, MODES, (0, 8)):
            models = self.compare(fixture(flag, current, end), phase=phase, mode=mode)
            for model in models:
                seen.update(model.visits)
            cases += 1
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+172, 4))-seen)
        self.assertEqual(missing, [9, 10, 11])
        for phase in (0, 8):
            for model in self.compare(fixture(attached=0), phase=phase):
                seen.update(model.visits)
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+172, 4))-seen)
        self.assertEqual(missing, [11])
        self.receipt('guest', dict(cases=cases, absent_attachment_cases=2,
            float_bit_patterns=len(FLOATS), flags=len(FLAGS), callback_modes=len(MODES),
            missing_word_indices=missing, unreachable_branch_likely_duplicate_only=True,
            ordered_public_reads_writes_and_setup_6word_ABI=True, both_SP_phases=True,
            home_reload_after_callback=True, saved_SP_GP_RA_and_FP_checked=True,
            FCSR_exception_state_and_full_setup_callee_not_claimed=True))

    def test_unused_actor_words_and_self_attached_node_alias(self):
        cases = 0
        for attached, actor, flag, phase, mode in itertools.product((ATTACHMENT, NODE),
                (0, NODE, ALT_NODE, 0xFFFFFFFF), (0, 0x8000), (0, 8), (0, 1, 3, 4)):
            self.compare(fixture(flag, attached=attached), (NODE, actor), phase, mode)
            cases += 1
        self.receipt('aliases', dict(cases=cases, second_argument_copied_not_dereferenced=True,
            self_attached_node_valid=True, argument_home_mutation=True,
            full_arbitrary_stack_alias_contract_not_claimed=True))

    def test_lazy_absence_required_reads_and_no_post_setup_null_gate(self):
        memory = fixture(attached=0)
        for address in (ATTACHMENT+4, ATTACHMENT+8, ATTACHMENT+0x18):
            memory.pop(address)
        models = self.compare(memory, (NODE, 0xFFFFFFFF))
        self.assertEqual(prior.public(models[0].events), [('R', NODE+0x48, 4, 0)])
        probes = [(fixture(), (0, 0), 0, None),
            (fixture(), (NODE, 0), 0, NODE+0x48),
            (fixture(), (NODE, 0), 0, ATTACHMENT+4),
            (fixture(0x8000), (NODE, 0), 0, ATTACHMENT+0x18),
            (fixture(0x8000), (NODE, 0), 0, ATTACHMENT+8),
            (fixture(), (NODE, 0), 1, ALT_ATTACHMENT+0x18),
            (fixture(), (NODE, 0), 1, ALT_ATTACHMENT+8),
            (fixture(), (NODE, 0), 2, ALT_NODE+0x48),
            (fixture(), (NODE, 0), 5, None), (fixture(), (NODE, 0), 6, None)]
        for memory, args, mode, missing in probes:
            if missing is not None:
                memory.pop(missing)
            reference = ProgressReference(memory, mode=mode)
            with self.assertRaises(AssertionError) as failure:
                reference.run(*args)
            for words in (self.words, self.retail):
                model = ProgressOracle(words, memory, args, mode=mode)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args, failure.exception.args)
                self.assertEqual((prior.public(model.events), model.calls, prior.external_memory(model.memory)),
                    (prior.public(reference.events), reference.calls, prior.external_memory(reference.memory)))
        self.receipt('gates', dict(lazy_cases=1, required_faults=len(probes),
            no_node_null_or_post_setup_attachment_null_gate=True, partial_setup_effects_preserved=True))

    def test_nineteen_source_profile_controls_preserve_ordinary_results(self):
        forms = [(name, body, 'o2g3') for name, body in screen.candidates()]
        forms += [('profile-'+profile, screen.SELECTED, profile) for profile in PROFILES if profile != 'o2g3']
        records, exact, executions = [], [], 0
        for name, body, profile in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile)
            for flag, current, end, mode in itertools.product((0, 0x8000),
                    (0, 0x41200000, 0x7FC00001), (0x40800000, 0x7F800000), (0, 1, 3)):
                memory = fixture(flag, current, end)
                reference = ProgressReference(memory, mode=mode)
                expected = reference.run(NODE, 0)
                model = ProgressOracle(words, memory, (NODE, 0), mode=mode).run()
                self.assertEqual((model.r[2], model.calls, prior.external_memory(model.memory)),
                    (expected, reference.calls, prior.external_memory(reference.memory)), name)
                executions += 1
            records.append(record)
            if not record['differences']:
                exact.append(name)
        self.assertEqual(len(forms), 19)
        self.assertEqual(len(exact), 4)
        self.receipt('controls', dict(forms=19, ordinary_executions=executions, raw_exact=exact,
            measurements=records, homes_faults_read_order_and_private_not_claimed_for_all_controls=True))

    def test_compiled_reread_threshold_and_setup_bit_negatives_are_effective(self):
        forms = dict(cached_attachment=screen.SELECTED.replace(
                '        attachment = *(u8 **)(node + 0x48);\n', ''),
            missing_minus_one=screen.SELECTED.replace(' - 1.0f <=', ' <='),
            wrong_flag=screen.SELECTED.replace('0x8000', '0x4000'))
        for name, body in forms.items():
            self.assertNotEqual(body, screen.SELECTED)
            _, words = screen.compile_candidate(self.root, self.out, 'negative-'+name, body)
            memory = fixture(0 if name == 'cached_attachment' else 0x8000,
                0x40400000 if name == 'missing_minus_one' else 0, 0x40800000)
            mode = 1 if name == 'cached_attachment' else 0
            reference = ProgressReference(memory, mode=mode)
            expected = reference.run(NODE, 0)
            actual = ProgressOracle(words, memory, (NODE, 0), mode=mode).run()
            self.assertNotEqual((actual.r[2], actual.calls), (expected, reference.calls), name)
        self.receipt('negatives', dict(compiled_effective_negatives=list(forms), no_fault_used_as_difference=True))

    def test_native_32bit_actual_C_callback_mutations_and_binary32_boundaries(self):
        values = ','.join('0x%08X' % value for value in FLOATS)
        self.fixture = r'''typedef unsigned char u8;typedef unsigned short u16;typedef int s32;
typedef unsigned int u32;typedef float f32;
typedef union {u32 align;u8 bytes[0x60];} Storage;
typedef char pointer_width[(sizeof(void *)==4)?1:-1];
static Storage node,attached,alternate;static int mode,calls,error;static u32 last[6];
static u32 word(f32 f){union {f32 f;u32 u;} v;v.f=f;return v.u;}
static f32 number(u32 u){union {f32 f;u32 u;} v;v.u=u;return v.f;}
void func_1503F5B8(u8 *a,s32 b,s32 c,f32 d,f32 e,s32 f){
    if(a!=attached.bytes||b||c||word(d)!=0x3F800000||word(e)||f!=1)error=1;
    last[0]=(u32)a;last[1]=b;last[2]=c;last[3]=word(d);last[4]=word(e);last[5]=f;calls++;
    if(mode==1||mode==3)*(u8 **)(node.bytes+0x48)=alternate.bytes;
    if(mode==2||mode==3){*(f32 *)(a+8)=10.0f;*(f32 *)(a+0x18)=4.0f;}
}
static void init(u16 flags,u32 current,u32 end,int kind){int i;mode=kind;calls=error=0;
    for(i=0;i<0x60;i++){node.bytes[i]=0xA5;attached.bytes[i]=0xA5;alternate.bytes[i]=0xA5;}
    for(i=0;i<6;i++)last[i]=0xA5A5A5A5;
    *(u8 **)(node.bytes+0x48)=attached.bytes;*(u16 *)(attached.bytes+4)=flags;
    *(f32 *)(attached.bytes+8)=number(current);*(f32 *)(attached.bytes+0x18)=number(end);
    *(f32 *)(alternate.bytes+8)=10.0f;*(f32 *)(alternate.bytes+0x18)=4.0f;
}
static int reference(u8 *n){u8 *a=*(u8 **)(n+0x48);volatile f32 threshold;
    if(!a)return 0;
    if((*(u16 *)(a+4)&0x8000)!=0x8000){func_1503F5B8(a,0,0,1.0f,0.0f,1);a=*(u8 **)(n+0x48);}
    threshold=*(f32 *)(a+0x18)-1.0f;return threshold<=*(f32 *)(a+8);
}
''' + screen.SELECTED+'\nstatic u32 values[]={'+values+'};\n'
        self.run_host(r'''
int flag,current,end,kind,actor,i,expected,actual,expectedCalls;u32 expectedLast[6];Storage saved[3];
static u16 flags[6]={0,1,0x7FFF,0x8000,0x8001,0xFFFF};
for(flag=0;flag<6;flag++)for(current=0;current<25;current++)for(end=0;end<25;end++)
for(kind=0;kind<4;kind++)for(actor=0;actor<3;actor++){
    init(flags[flag],values[current],values[end],kind);expected=reference(node.bytes);expectedCalls=calls;
    saved[0]=node;saved[1]=attached;saved[2]=alternate;for(i=0;i<6;i++)expectedLast[i]=last[i];
    if(error)return 1;
    init(flags[flag],values[current],values[end],kind);
    actual=func_1503327C(node.bytes,actor==0?0:actor==1?node.bytes:(u8 *)0xFFFFFFFF);
    if(error||actual!=expected||calls!=expectedCalls)return 2;
    for(i=0;i<0x60;i++)if(node.bytes[i]!=saved[0].bytes[i]||attached.bytes[i]!=saved[1].bytes[i]
        ||alternate.bytes[i]!=saved[2].bytes[i])return 3;
    for(i=0;i<6;i++)if(last[i]!=expectedLast[i])return 4;
}
*(u8 **)(node.bytes+0x48)=0;calls=0;if(func_1503327C(node.bytes,(u8 *)0xFFFFFFFF)||calls)return 5;
''')
        self.receipt('native', dict(cases=6*25*25*4*3, lazy_cases=1, pointer_bytes=4,
            actual_complete_C=True, valid_storage=True, callback_ABI_and_public_mutations=True,
            NaN_infinity_zero_subnormal_and_rounding_boundaries=True,
            private_home_mutations_invalid_pointer_and_FCSR_state_not_claimed=True))

    def qualify_owner(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        if screen.SELECTED in source:
            self.assertEqual(source.count(screen.SELECTED), 1)
            source = source.replace(screen.SELECTED, STUB)
        self.assertEqual(source.count(STUB), 1)
        selected = source.replace(STUB, screen.SELECTED)
        if screen.DECLARATION not in selected:
            selected = selected.replace('#include <ultra64.h>\n',
                '#include <ultra64.h>\n'+screen.DECLARATION+'\n', 1)
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
            self.assertEqual(text[current['value']:current['value']+current['size']],
                old_text[previous['value']:previous['value']+previous['size']], name)
            self.assertEqual({o-current['value']: r for o, r in rel.items()
                if current['value'] <= o < current['value']+current['size']},
                {o-previous['value']: r for o, r in old_rel.items()
                if previous['value'] <= o < previous['value']+previous['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        isolated_text, isolated, isolated_rel = parse_object(self.out / 'selected.o')
        target = functions[screen.FUNCTION]
        self.assertEqual(target['size'], isolated[screen.FUNCTION]['size'])
        self.assertEqual(text[target['value']:target['value']+172], isolated_text[:172])
        self.assertEqual({o-target['value']: r for o, r in rel.items()
            if target['value'] <= o < target['value']+172}, isolated_rel)
        self.receipt('owner', dict(functions=len(functions), unchanged_neighbors=len(functions)-1,
            neighbors_pools_relocations_unchanged=True, target_isolated_equal=True, warnings=0))
        return objects[1]

    def test_copied_owner_neighbors_pools_relocations_and_warnings_unchanged(self):
        self.qualify_owner()

    def test_real_padder_complete_size_and_independent_function_setup_rebases(self):
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
        self.assertEqual(functions[screen.FUNCTION]['size'], 172)
        self.assertEqual(relocs, {88: [('R_MIPS_26', 'func_1503F5B8')]})
        for entry, setup in ((screen.ENTRY, screen.SETUP), (screen.ENTRY+0x01000004, screen.SETUP),
                (screen.ENTRY, screen.SETUP+0x01000004)):
            script = self.out / 'rebased.ld'
            script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
            elf = self.out / ('rebased-%X-%X.elf' % (entry, setup))
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', screen.FUNCTION,
                '--defsym=func_1503F5B8=0x%X' % setup, '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = self.words.copy()
            expected[22] = expected[22]&0xFC000000 | setup>>2&0x3FFFFFF
            self.assertEqual(list(struct.unpack_from('>43I', sections(elf)['.text'][1])), expected)
        self.receipt('padder', dict(body_bytes=172, slot_bytes=172, extra_padding_words=0,
            symbolic_setup_call=True, independent_entry_and_setup_rebased_links=True))

    def test_installed_slot_or_original_placeholder_explicit_and_guards_intact(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        installed = screen.SELECTED in source
        self.assertEqual(source.count(screen.SELECTED if installed else STUB), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        expected = self.words if installed else [0x00001025, 0x03E00008]+[0]*41
        self.assertEqual((addresses[screen.FUNCTION], functions[screen.FUNCTION]), (screen.ENTRY, expected))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed', dict(C_installed=installed, byte_exact=installed, guards_added=0,
            old_placeholder_not_mistaken_for_original_assembly=True))


if __name__ == '__main__':
    unittest.main()
