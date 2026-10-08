"""Cached resource, setup ABI, copy-induced attachment reload and float clamp."""

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

from tools.experiments import game_attachment_copy_candidates as screen
from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.tests import test_game_attachment_progress_match as progress
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read

NODE, ALT_NODE, ATTACHMENT, ALT_ATTACHMENT = progress.NODE, progress.ALT_NODE, progress.ATTACHMENT, progress.ALT_ATTACHMENT
ACTOR, SOURCE, ALT_SOURCE = 0x30000, 0x22000, 0x23000
INDICES = (0, 1, 0xFE, 0xFF, 0x100, 0x123456FF, 0x80000001, 0xFFFFFFFF)
MODES = (0, 1, 2, 3, 4, 7)
STUB = 's32 func_150331B8() {\n    return 0;\n}'


def fixture(index=0, current=0, end=0x40800000, attached=ATTACHMENT, source=SOURCE):
    memory = progress.fixture(current=current, end=end, attached=attached)
    put(memory, ACTOR+0x2D0, source)
    put(memory, ACTOR+0x2E4, index)
    put(memory, SOURCE+8, current)
    put(memory, ALT_SOURCE+8, 0xBF800000)
    put(memory, NODE+0x48, attached)
    return memory


def actions(mode, stack):
    return {0: [], 1: [(NODE+0x48, ALT_ATTACHMENT)], 2: [(stack, ALT_NODE)],
        3: [(ACTOR+0x2D0, ALT_SOURCE)], 4: [(SOURCE+8, 0x41200000)],
        5: [(NODE+0x48, 0)], 6: [(stack, 0)],
        7: [(NODE+0x48, ALT_ATTACHMENT), (ACTOR+0x2D0, 0), (SOURCE+8, 0x41200000)]}[mode]


class CopyReference(progress.ProgressReference):
    def run(self, node, actor):
        self.put(self.stack, node)
        source = self.get(actor+0x2D0)
        attached = self.get(node+0x48)
        if not attached:
            return 0
        index = self.get(actor+0x2E4)&255
        if index != 255:
            self.calls.append((screen.SETUP, attached, 0, index, 0x3F800000, 0, 1))
            for address, value in actions(self.mode, self.stack):
                self.put(address, value)
        node = self.get(self.stack)
        if source:
            value = self.get(source+8)
            attached = self.get(node+0x48)
            self.put(attached+8, value)
            attached = self.get(node+0x48)
            end, current = self.get(attached+0x18), self.get(attached+8)
            if floating(end) <= floating(current):
                self.put(attached+8, bits(floating(end)-1.0))
        return 0


class CopyOracle(TriangleOracle):
    def __init__(self, words, memory, args=(NODE, ACTOR), phase=0, mode=0):
        super().__init__(words, memory, entry=screen.ENTRY, arguments=args, phase=phase)
        self.stack, self.mode = prior.STACK+phase, mode

    def record_call(self, target):
        assert target == screen.SETUP
        arguments = self.arguments(6)
        assert arguments[1] == 0 and arguments[3:] == (0x3F800000, 0, 1), arguments
        assert arguments[2] < 255
        self.calls.append((target, *arguments))

    def hook(self, target):
        assert target == screen.SETUP
        for address, value in actions(self.mode, self.stack):
            self.put(address, value, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]
        self.condition = True


class GameAttachmentCopyMatchTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-attachment-copy-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        cls.retail = list(struct.unpack_from('>49I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def compare(self, memory, args=(NODE, ACTOR), phase=0, mode=0):
        reference = CopyReference(memory, phase, mode)
        expected = reference.run(*args)
        models = [CopyOracle(body, memory, args, phase, mode).run() for body in (self.words, self.retail)]
        for model in models:
            self.assertEqual((model.r[2], model.calls, prior.public(model.events), prior.external_memory(model.memory)),
                (expected, reference.calls, prior.public(reference.events), prior.external_memory(reference.memory)))
            self.assertEqual(read(model.memory, prior.STACK+phase), read(reference.memory, prior.STACK+phase))
        self.assertEqual((models[0].r, models[0].f, models[0].events), (models[1].r, models[1].f, models[1].events))
        return models

    def test_complete_direct_slot_frame_relocation_and_standard_profile(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (49, 48, 0))
        self.assertEqual((self.record['diagnostics'], self.record['pool_bytes']), ('', 0))
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.record['relocations'], {92: [('R_MIPS_26', 'func_1503F5B8')]})
        self.receipt('slot', dict(body_words=49, slot_words=49, frame=48, direct_differences=0,
            guards_added=0, default_o2g3_profile=True, cached_source_spill_offset=44))

    def test_indices_float_boundaries_callback_mutations_and_complete_word_coverage(self):
        cases, seen = 0, set()
        for index, current, end, mode, phase in itertools.product(INDICES, progress.FLOATS,
                progress.FLOATS, MODES, (0, 8)):
            for model in self.compare(fixture(index, current, end), phase=phase, mode=mode):
                seen.update(model.visits)
            cases += 1
        for source, attached, phase in itertools.product((0, SOURCE), (0, ATTACHMENT), (0, 8)):
            for model in self.compare(fixture(source=source, attached=attached), phase=phase):
                seen.update(model.visits)
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+196, 4))-seen)
        self.assertEqual(missing, [11])
        self.receipt('guest', dict(cases=cases, lazy_coverage_cases=8, indices=len(INDICES),
            float_bit_patterns=len(progress.FLOATS), callback_modes=len(MODES), SP_phases=2,
            missing_word_indices=missing, unreachable_branch_likely_duplicate_only=True,
            cached_source_and_post_call_home_reload=True, ordered_public_memory_and_setup_ABI=True,
            FCSR_exceptions_and_full_setup_callee_not_claimed=True))

    def test_source_destination_and_copy_induced_pointer_aliases(self):
        cases = 0
        for source, attached, index, phase, mode in itertools.product((SOURCE, ATTACHMENT, NODE+0x40),
                (ATTACHMENT, NODE+0x40), (0, 0xFFFFFFFF), (0, 8), (0, 1, 2, 3)):
            memory = fixture(index, source=source, attached=attached)
            if attached == NODE+0x40:
                put(memory, attached+0x18, 0x40800000)
                if source != NODE+0x40:
                    put(memory, source+8, ALT_ATTACHMENT)
            if source == NODE+0x40:
                self.assertEqual(read(memory, source+8), attached)
            self.compare(memory, phase=phase, mode=mode)
            cases += 1
        # The copy overwrites node+0x48, so the following clamp uses the NEW pointer.
        memory = fixture(0xFF, ALT_ATTACHMENT, attached=NODE+0x40)
        put(memory, NODE+0x58, 0x7F800000)
        models = self.compare(memory)
        self.assertEqual(read(models[0].memory, NODE+0x48), ALT_ATTACHMENT)
        self.assertEqual(read(models[0].memory, ALT_ATTACHMENT+8), 0x40400000)
        self.receipt('aliases', dict(cases=cases+1, source_destination_and_node_field_aliases=True,
            copy_induced_attachment_reload_explicit=True, arbitrary_private_stack_aliases_not_claimed=True))

    def test_lazy_paths_required_read_store_faults_and_partial_effects(self):
        memory = fixture(attached=0)
        memory.pop(ACTOR+0x2E4)
        model = self.compare(memory)[0]
        self.assertEqual(prior.public(model.events), [('R', ACTOR+0x2D0, 4, SOURCE), ('R', NODE+0x48, 4, 0)])
        memory = fixture(source=0)
        memory.pop(ATTACHMENT+8)
        self.compare(memory)
        probes = [(fixture(attached=0), (NODE, 0), 0, None),
            (fixture(attached=0), (NODE, ACTOR), 0, ACTOR+0x2D0),
            (fixture(), (0, ACTOR), 0, None), (fixture(), (NODE, ACTOR), 0, NODE+0x48),
            (fixture(), (NODE, ACTOR), 0, ACTOR+0x2E4),
            (fixture(), (NODE, ACTOR), 0, SOURCE+8),
            (fixture(), (NODE, ACTOR), 0, ATTACHMENT+8),
            (fixture(), (NODE, ACTOR), 0, ATTACHMENT+0x18),
            (fixture(), (NODE, ACTOR), 1, ALT_ATTACHMENT+8),
            (fixture(), (NODE, ACTOR), 1, ALT_ATTACHMENT+0x18),
            (fixture(), (NODE, ACTOR), 2, ALT_NODE+0x48),
            (fixture(), (NODE, ACTOR), 5, None), (fixture(), (NODE, ACTOR), 6, None)]
        for memory, args, mode, missing in probes:
            if missing is not None:
                memory.pop(missing)
            reference = CopyReference(memory, mode=mode)
            with self.assertRaises(AssertionError) as failure:
                reference.run(*args)
            for words in (self.words, self.retail):
                model = CopyOracle(words, memory, args, mode=mode)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args, failure.exception.args)
                self.assertEqual((prior.public(model.events), model.calls, prior.external_memory(model.memory)),
                    (prior.public(reference.events), reference.calls, prior.external_memory(reference.memory)))
        self.receipt('gates', dict(lazy_cases=2, required_faults=len(probes),
            actor_source_required_before_absent_attachment_gate=True, source_null_skips_copy_not_setup=True,
            post_setup_null_not_hidden=True, partial_public_effects_preserved=True))

    def test_source_profile_controls_preserve_ordinary_results(self):
        forms = [(name, body, 'o2g3') for name, body in screen.candidates()]
        forms += [('profile-'+profile, screen.SELECTED, profile) for profile in PROFILES if profile != 'o2g3']
        records, executions = [], 0
        for name, body, profile in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile)
            for index, current, end, mode in itertools.product((0, 0xFF), (0, 0x41200000, 0x7FC00001),
                    (0x40800000, 0x7F800000), (0, 1, 3)):
                memory = fixture(index, current, end)
                reference = CopyReference(memory, mode=mode)
                expected = reference.run(NODE, ACTOR)
                model = CopyOracle(words, memory, mode=mode).run()
                self.assertEqual((model.r[2], model.calls, prior.external_memory(model.memory)),
                    (expected, reference.calls, prior.external_memory(reference.memory)), name)
                executions += 1
            records.append(record)
        self.assertEqual(sum(not r['differences'] for r in records), 8)
        self.receipt('controls', dict(forms=len(forms), ordinary_executions=executions, measurements=records,
            raw_exact_forms=8, all_control_homes_faults_read_order_private_not_claimed=True))

    def test_compiled_source_cache_clamp_and_setup_index_negatives(self):
        forms = dict(reread_source=screen.SELECTED.replace('    if (source != 0) {',
                '    source = *(u8 **)(actor + 0x2D0);\n    if (source != 0) {'),
            clamp_equal=screen.SELECTED.replace(' <= ', ' < '),
            omit_minus_one=screen.SELECTED.replace(' - 1.0f;', ';'),
            full_index=screen.SELECTED.replace(' & 0xFF;', ';'),
            cached_destination=screen.SELECTED.replace('        attachment = *(u8 **)(node + 0x48);\n', ''))
        for name, body in forms.items():
            record, words = screen.compile_candidate(self.root, self.out, 'negative-'+name, body)
            self.assertTrue(record['differences'])
            index = 0x123456FF if name == 'full_index' else 0
            memory = fixture(index, 0x40800000)
            mode = 3 if name == 'reread_source' else 0
            if name == 'cached_destination':
                memory = fixture(0xFF, ALT_ATTACHMENT, attached=NODE+0x40)
                put(memory, NODE+0x58, 0x7F800000)
            reference = CopyReference(memory, mode=mode)
            reference.run(NODE, ACTOR)
            if name == 'full_index':
                class PermissiveOracle(CopyOracle):
                    def record_call(self, target):
                        self.calls.append((target, *self.arguments(6)))
                oracle = PermissiveOracle
            else:
                oracle = CopyOracle
            model = oracle(words, memory, mode=mode).run()
            self.assertNotEqual((model.calls, prior.external_memory(model.memory)),
                (reference.calls, prior.external_memory(reference.memory)), name)
        self.receipt('negatives', dict(effective_compiled_negatives=list(forms), faults_not_accepted_as_success=True))

    def test_native_32bit_complete_C_public_mutations_float_boundaries_and_aliases(self):
        values = ','.join('0x%08X' % value for value in progress.FLOATS)
        self.fixture = r'''typedef unsigned char u8;typedef int s32;typedef unsigned int u32;typedef float f32;
typedef union {u32 align;u8 bytes[0x300];} Storage;
typedef char pointer_width[(sizeof(void *)==4)?1:-1];
static Storage node,actor,attached,alternate,source,other;static int mode,calls,error;static u32 last[6];
static u32 word(f32 f){union {f32 f;u32 u;} v;v.f=f;return v.u;}
static f32 number(u32 u){union {f32 f;u32 u;} v;v.u=u;return v.f;}
void func_1503F5B8(u8 *a,s32 b,s32 c,f32 d,f32 e,s32 f){
    if(a!=attached.bytes||b||c!=(int)(*(u32 *)(actor.bytes+0x2E4)&255)
        ||word(d)!=0x3F800000||word(e)||f!=1)error=1;
    last[0]=(u32)a;last[1]=b;last[2]=c;last[3]=word(d);last[4]=word(e);last[5]=f;calls++;
    if(mode==1||mode==4)*(u8 **)(node.bytes+0x48)=alternate.bytes;
    if(mode==2||mode==4)*(u8 **)(actor.bytes+0x2D0)=other.bytes;
    if(mode==3||mode==4)*(f32 *)(source.bytes+8)=10.0f;
}
static void init(u32 index,u32 current,u32 end,int kind,int alias){int i;mode=kind;calls=error=0;
    for(i=0;i<0x300;i++){node.bytes[i]=actor.bytes[i]=attached.bytes[i]=alternate.bytes[i]=source.bytes[i]=other.bytes[i]=0xA5;}
    for(i=0;i<6;i++)last[i]=0xA5A5A5A5;
    *(u8 **)(node.bytes+0x48)=attached.bytes;*(u32 *)(actor.bytes+0x2E4)=index;
    *(u8 **)(actor.bytes+0x2D0)=alias==1?attached.bytes:alias==2?0:source.bytes;
    *(f32 *)(source.bytes+8)=number(current);*(f32 *)(other.bytes+8)=-1.0f;
    *(f32 *)(attached.bytes+8)=number(current);*(f32 *)(attached.bytes+0x18)=number(end);
    *(f32 *)(alternate.bytes+8)=10.0f;*(f32 *)(alternate.bytes+0x18)=4.0f;
}
static int reference(u8 *n,u8 *a){u8 *s=*(u8 **)(a+0x2D0),*t=*(u8 **)(n+0x48);u32 index;volatile f32 threshold;
    if(!t)return 0;
    index=*(u32 *)(a+0x2E4)&255;
    if(index!=255)func_1503F5B8(t,0,index,1.0f,0.0f,1);
    if(s){*(f32 *)(*(u8 **)(n+0x48)+8)=*(f32 *)(s+8);t=*(u8 **)(n+0x48);
        if(*(f32 *)(t+0x18)<=*(f32 *)(t+8)){threshold=*(f32 *)(t+0x18)-1.0f;*(f32 *)(t+8)=threshold;}}
    return 0;
}
''' + screen.SELECTED+'\nstatic u32 values[]={'+values+'};\n'
        self.run_host(r'''
int index,current,end,kind,alias,i,j,expected,actual,expectedCalls;u32 expectedLast[6];Storage saved[6];
Storage *objects[6]={&node,&actor,&attached,&alternate,&source,&other};
static u32 indices[8]={0,1,0xFE,0xFF,0x100,0x123456FF,0x80000001,0xFFFFFFFF};
for(index=0;index<8;index++)for(current=0;current<25;current++)for(end=0;end<25;end++)
for(kind=0;kind<5;kind++)for(alias=0;alias<3;alias++){
    init(indices[index],values[current],values[end],kind,alias);expected=reference(node.bytes,actor.bytes);expectedCalls=calls;
    for(j=0;j<6;j++)saved[j]=*objects[j];
    for(i=0;i<6;i++)expectedLast[i]=last[i];
    if(error)return 1;
    init(indices[index],values[current],values[end],kind,alias);actual=func_150331B8(node.bytes,actor.bytes);
    if(error||actual!=expected||calls!=expectedCalls)return 2;
    for(j=0;j<6;j++)for(i=0;i<0x300;i++)if(objects[j]->bytes[i]!=saved[j].bytes[i])return 3;
    for(i=0;i<6;i++)if(last[i]!=expectedLast[i])return 4;
}
*(u8 **)(node.bytes+0x48)=0;calls=0;if(func_150331B8(node.bytes,actor.bytes)||calls)return 5;
''')
        self.receipt('native', dict(cases=8*25*25*5*3, lazy_cases=1, pointer_bytes=4, complete_actual_C=True,
            cached_resource_public_mutations_and_source_aliases=True, all_object_bytes_and_setup_ABI_checked=True,
            invalid_pointers_private_home_mutations_and_FCSR_not_claimed=True))

    def qualify_owner(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        if screen.SELECTED in source:
            self.assertEqual(source.count(screen.SELECTED), 1)
            source = source.replace(screen.SELECTED, STUB)
        self.assertEqual(source.count(STUB), 1)
        self.assertIn(screen.DECLARATION, source)
        objects = []
        for name, body in (('baseline', source), ('selected', source.replace(STUB, screen.SELECTED))):
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
        self.assertEqual(text[target['value']:target['value']+196], isolated_text[:196])
        self.assertEqual({o-target['value']: r for o, r in rel.items()
            if target['value'] <= o < target['value']+196}, isolated_rel)
        self.receipt('owner', dict(functions=len(functions), unchanged_neighbors=len(functions)-1,
            neighbors_pools_relocations_unchanged=True, target_isolated_equal=True, warnings=0))
        return objects[1]

    def test_owner_neighbors_pools_relocations_and_warnings(self):
        self.qualify_owner()

    def test_real_padder_body_slot_and_independent_setup_entry_rebases(self):
        assembly = emit_padded_assembly(self.qualify_owner(), self.root / 'conker/asm/5D2C0.s',
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
        self.assertEqual(functions[screen.FUNCTION]['size'], 196)
        self.assertEqual(relocs, {92: [('R_MIPS_26', 'func_1503F5B8')]})
        for entry, setup in ((screen.ENTRY, screen.SETUP), (screen.ENTRY+0x01000004, screen.SETUP),
                (screen.ENTRY, screen.SETUP+0x01000004)):
            script = self.out / 'rebased.ld'
            script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
            elf = self.out / ('rebased-%X-%X.elf' % (entry, setup))
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', screen.FUNCTION,
                '--defsym=func_1503F5B8=0x%X' % setup, '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = self.words.copy()
            expected[23] = expected[23]&0xFC000000 | setup>>2&0x3FFFFFF
            self.assertEqual(list(struct.unpack_from('>49I', sections(elf)['.text'][1])), expected)
        self.receipt('padder', dict(body_bytes=196, slot_bytes=196, extra_padding_words=0,
            symbolic_setup_call=True, independent_function_and_setup_rebases=True))

    def test_installed_slot_or_previous_placeholder_and_guard_history(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        installed = screen.SELECTED in source
        self.assertEqual(source.count(screen.SELECTED if installed else STUB), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        expected = self.words if installed else [0x00001025, 0x03E00008]+[0]*47
        self.assertEqual((addresses[screen.FUNCTION], functions[screen.FUNCTION]), (screen.ENTRY, expected))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed', dict(C_installed=installed, byte_exact=installed, guards_added=0))


if __name__ == '__main__':
    unittest.main()
