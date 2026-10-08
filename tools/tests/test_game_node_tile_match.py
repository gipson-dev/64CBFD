"""Fourth tile-size update, ordered scans, binary32 boundaries and fixed owners."""

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

from tools.experiments import game_node_tile_candidates as screen
from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.tests import test_game_node_action_match as action
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read

NODE, ACTOR, SOURCE, CONTAINER, COMMANDS = 0x10000, 0x20000, 0x24000, 0x25000, 0x30000
TYPES = (0, 0x54, 0x55, 0x56, 0x57, 0xFF, 0x8000, 0xFFFF)
LAYOUTS = ((0, 1, 2, 3), (1, 3, 5, 7), (0, 4, 9, 15), (4, 7, 12, 16), (2, 6, 10, 20), (0, 1, 8, 32))
FLOATS = sorted(set((0, 0x80000000, 1, 0x80000001, 0x00800000, 0x80800000,
    0xBF800000, 0x3F800000, 0x7F7FFFFF, 0xFF7FFFFF, 0x7F800000, 0xFF800000,
    0x7FC00001, 0xFFC12345, bits(120.0)-1, bits(120.0), bits(120.0)+1,
    *[bits((27-coordinate)*4.8)+offset for coordinate in range(3, 27) for offset in range(-2, 3)])))
STUB = 's32 func_15031E7C() {\n    return 0;\n}'


def coordinate(actor_type, progress):
    if actor_type == 0x55:
        factor = 1.0
    elif actor_type == 0x56:
        factor = 0.0
    else:
        value = floating(progress)
        factor = floating(bits(1.0-floating(bits(value*floating(0x3C088889))))) if 0.0 <= value <= 120.0 else 0.0
    return int(floating(bits(floating(bits(25.0*factor))+2.0))) & 0xFFF


def fixture(actor_type=0, progress=0, layout=LAYOUTS[0]):
    memory = {prior.STACK+i: 0xA5 for i in range(-0x100, 0x100)}
    put(memory, NODE+0x24, CONTAINER)
    put(memory, CONTAINER, COMMANDS)
    put(memory, ACTOR+0x2D0, SOURCE)
    put(memory, ACTOR+0x84, actor_type, 2)
    put(memory, SOURCE+8, progress)
    put(memory, screen.SCALE, 0x3C088889)
    for index in range(40):
        opcode = (0, 0x7F, 0x80, 0xF1, 0xF3, 0xFF)[index % 6]
        put(memory, COMMANDS+index*8, opcode<<24 | 0x00123400 | index)
        put(memory, COMMANDS+index*8+4, 0xABCD0000 | index)
    for index in (*layout, 36):
        put(memory, COMMANDS+index*8, 0xF2123400 | index)
    return memory


class TileReference(action.ActionReference):
    def run(self, node=NODE, actor=ACTOR):
        source = self.get(actor+0x2D0)
        if source == 0:
            return 0
        commands = self.get(self.get(node+0x24))
        if commands == 0:
            return 0
        actor_type = self.get(actor+0x84, 2)
        if actor_type == 0x55:
            factor = 1.0
        elif actor_type == 0x56:
            factor = 0.0
        else:
            progress = floating(self.get(source+8))
            if 0.0 <= progress <= 120.0:
                scale = floating(self.get(screen.SCALE))
                factor = floating(bits(1.0-floating(bits(progress*scale))))
            else:
                factor = 0.0
        index = 0
        for match in range(4):
            while self.get(commands+index*8, 1) != 0xF2:
                index += 1
            if match != 3:
                index += 1
        result = int(floating(bits(floating(bits(25.0*factor))+2.0))) & 0xFFF
        self.put(commands+index*8, 0xF2002000 | result)
        return 0


class TileOracle(TriangleOracle):
    def __init__(self, words, memory, args=(NODE, ACTOR), phase=0):
        super().__init__(words, memory, entry=screen.ENTRY, arguments=args, phase=phase)

    def execute(self, word):
        if word >> 26 == 32:
            rs, rt = word >> 21 & 31, word >> 16 & 31
            offset = word & 65535
            address = (self.r[rs]+(offset if offset < 32768 else offset-65536)) & 0xFFFFFFFF
            value = self.get(address, 1)
            self.r[rt] = (value if value < 128 else value-256) & 0xFFFFFFFF
            self.r[0] = 0
        else:
            super().execute(word)

    def record_call(self, target):
        raise AssertionError(('unexpected call', target))


class GameNodeTileMatchTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-node-tile-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        cls.retail = list(struct.unpack_from('>83I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def compare(self, memory, args=(NODE, ACTOR), phase=0):
        reference = TileReference(memory, phase)
        expected = reference.run(*args)
        models = [TileOracle(words, memory, args, phase).run() for words in (self.words, self.retail)]
        for model in models:
            self.assertEqual((model.r[2], model.calls, model.events, model.memory),
                (expected, [], reference.events, reference.memory))
        self.assertEqual((models[0].r, models[0].f), (models[1].r, models[1].f))
        return models

    def test_all_words_direct_frame_and_no_generated_pool(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'], self.record['pool_bytes']), (83, 0, 0, 0))
        self.assertEqual(self.words, self.retail)
        self.receipt('slot', dict(body_words=83, slot_words=83, frame=0, raw_differences=0,
            padding_words=0, guards_added=0, SDK_Gfx_opcode_and_word_macros=True))

    def test_types_float_boundaries_scan_layouts_complete_word_coverage_and_untouched_words(self):
        seen, cases = set(), 0
        for actor_type, progress, layout, phase in itertools.product(TYPES, FLOATS, LAYOUTS, (0, 8)):
            memory = fixture(actor_type, progress, layout)
            for model in self.compare(memory, phase=phase):
                seen.update(model.visits)
                self.assertEqual(read(model.memory, COMMANDS+layout[3]*8), 0xF2002000 | coordinate(actor_type, progress))
                changed = sorted(a for a in memory if model.memory[a] != memory[a])
                self.assertTrue(set(changed) <= set(range(COMMANDS+layout[3]*8, COMMANDS+layout[3]*8+4)))
            cases += 1
        for null in (ACTOR+0x2D0, CONTAINER):
            memory = fixture()
            put(memory, null, 0)
            for model in self.compare(memory):
                seen.update(model.visits)
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+332, 4))-seen)
        self.assertEqual(missing, [5, 11, 25, 44])
        self.receipt('guest', dict(cases=cases, actor_types=len(TYPES), float_patterns=len(FLOATS), layouts=len(LAYOUTS),
            SP_phases=2, missing_word_indices=missing, missing_only_unreachable_branch_likely_duplicates=True,
            complete_return_GP_FP_trace_memory_equal=True, only_fourth_command_first_word_written=True,
            full_FCSR_hardware_or_renderer_acceptance_not_claimed=True))

    def test_lazy_override_null_gates_required_storage_and_malformed_scan_fault_prefixes(self):
        lazy = []
        memory = fixture()
        put(memory, ACTOR+0x2D0, 0)
        for address in (NODE+0x24, ACTOR+0x84, SOURCE+8, screen.SCALE):
            del memory[address]
        lazy.append(memory)
        memory = fixture()
        put(memory, CONTAINER, 0)
        for address in (ACTOR+0x84, SOURCE+8, screen.SCALE):
            del memory[address]
        lazy.append(memory)
        for kind in (0x55, 0x56):
            memory = fixture(kind)
            del memory[SOURCE+8], memory[screen.SCALE]
            lazy.append(memory)
        memory = fixture(progress=bits(-1.0))
        del memory[screen.SCALE]
        lazy.append(memory)
        for memory in lazy:
            self.compare(memory)
        aliases = []
        memory = fixture(progress=bits(60.0))
        put(memory, ACTOR+0x24, CONTAINER)
        aliases.append((memory, (ACTOR, ACTOR)))
        memory = fixture(progress=bits(60.0))
        put(memory, NODE+0x24, NODE)
        put(memory, NODE, COMMANDS)
        aliases.append((memory, (NODE, ACTOR)))
        for source in (NODE, ACTOR):
            memory = fixture()
            put(memory, ACTOR+0x2D0, source)
            put(memory, source+8, bits(60.0))
            aliases.append((memory, (NODE, ACTOR)))
        memory = fixture()
        put(memory, ACTOR+0x2D0, COMMANDS+16)
        aliases.append((memory, (NODE, ACTOR)))
        for memory, args in aliases:
            self.compare(memory, args)
        faults = [fixture() for _ in range(9)]
        for memory, missing in zip(faults, (ACTOR+0x2D0, NODE+0x24, CONTAINER, ACTOR+0x84,
                SOURCE+8, screen.SCALE, COMMANDS, COMMANDS+24, COMMANDS+25)):
            del memory[missing]
        for null in (NODE+0x24,):
            memory = fixture()
            put(memory, null, 0)
            faults.append(memory)
        for missing_match in range(4):
            memory = fixture()
            for index in range(missing_match, 40):
                put(memory, COMMANDS+index*8, 0xFF000000)
            faults.append(memory)
        for memory in faults:
            reference = TileReference(memory)
            with self.assertRaises(AssertionError) as failure:
                reference.run()
            for words in (self.words, self.retail):
                model = TileOracle(words, memory)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args, failure.exception.args)
                self.assertEqual((model.events, model.memory), (reference.events, reference.memory))
        self.receipt('gates', dict(lazy_cases=len(lazy), required_faults=10, missing_sentinel_faults=4,
            valid_aliases=len(aliases), no_new_scan_bound_or_container_null_gate=True,
            ordered_prefixes_and_partial_effects_equal=True))

    def test_source_profile_controls_and_effective_semantic_negatives(self):
        forms = [(n, b, 'o2g3') for n, b in screen.candidates()]
        forms += [('profile-'+p, screen.SELECTED, p) for p in PROFILES if p != 'o2g3']
        records, executions = [], 0
        for name, body, profile in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile)
            for kind, value, layout in itertools.product(TYPES, (0, bits(120.0), bits(120.0)+1, bits(4.8)+1, 0x7FC00001), LAYOUTS[:2]):
                memory = fixture(kind, value, layout)
                ref = TileReference(memory)
                expected = ref.run()
                model = TileOracle(words, memory).run()
                self.assertEqual((model.r[2], prior.external_memory(model.memory)),
                    (expected, prior.external_memory(ref.memory)), name)
                executions += 1
            records.append(record)
        negatives = (
            ('third-command', screen.SELECTED.replace('remaining = 4;', 'remaining = 3;'), 0, 0),
            ('wrong-default-factor', screen.SELECTED.replace('factor = 0.0f;', 'factor = 1.0f;'), 0x56, 0),
            ('wrong-factor-direction', screen.SELECTED.replace('factor = 1.0f - factor;', 'factor = factor;'), 0, 0),
            ('wrong-coordinate-scale', screen.SELECTED.replace('25.0f * factor', '24.0f * factor'), 0x55, 0),
        )
        for name, body, kind, value in negatives:
            _, words = screen.compile_candidate(self.root, self.out, name, body)
            memory = fixture(kind, value)
            reference = TileReference(memory)
            reference.run()
            model = TileOracle(words, memory).run()
            self.assertNotEqual(prior.external_memory(model.memory), prior.external_memory(reference.memory), name)
        self.receipt('controls', dict(forms=len(forms), ordinary_executions=executions,
            raw_exact_forms=sum(r['differences'] == 0 for r in records), measurements=records,
            effective_public_output_negatives=len(negatives), all_control_read_order_GP_FP_not_claimed=True))

    def test_native32_complete_C_opcode_bytes_word_encoding_and_all_canaries(self):
        expected = ','.join('0x%X' % v for v in FLOATS)
        coordinates = ','.join(str(coordinate(kind, value)) for kind in TYPES for value in FLOATS)
        self.fixture = r'''typedef unsigned char u8;typedef signed char s8;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;typedef float f32;
typedef union __attribute__((aligned(8))) {struct {u32 w0,w1;} words;unsigned long long align;} Gfx;
#define G_SETTILESIZE 0xF2
#define _SHIFTL(v,s,w) ((u32)(((u32)(v)&((1U<<(w))-1U))<<(s)))
typedef union __attribute__((aligned(8))) {u32 align;u8 b[0x340];} Storage;
typedef char widths[(sizeof(void *)==4&&sizeof(Gfx)==8&&sizeof(f32)==4)?1:-1];
static Storage node,actor,source,container;static Gfx commands[40];f32 D_800970DC;
static union {u32 u;f32 f;} scale;
''' + screen.SELECTED
        self.run_host('static u32 values[]={'+expected+'};\nstatic int expected[]={'+coordinates+'};\n'+r'''
static int types[8]={0,0x54,0x55,0x56,0x57,0xFF,0x8000,0xFFFF};
static int layouts[6][4]={{0,1,2,3},{1,3,5,7},{0,4,9,15},{4,7,12,16},{2,6,10,20},{0,1,8,32}};
static u8 opcodes[6]={0,0x7F,0x80,0xF1,0xF3,0xFF};
Storage saved[4];Gfx old[40];int k,p,l,n,i,j;
for(k=0;k<8;k++)for(p=0;p<(int)(sizeof(values)/sizeof(values[0]));p++)for(l=0;l<6;l++)for(n=0;n<3;n++){
    for(i=0;i<0x340;i++)node.b[i]=actor.b[i]=source.b[i]=container.b[i]=0xA5;
    for(i=0;i<40;i++){commands[i].words.w0=0x12340000+i;commands[i].words.w1=0xABCD0000+i;
        ((u8 *)&commands[i])[0]=opcodes[i%6];}
    for(i=0;i<4;i++)((u8 *)&commands[layouts[l][i]])[0]=0xF2;
    ((u8 *)&commands[36])[0]=0xF2;
    *(u8 **)(actor.b+0x2D0)=n==1?0:source.b;*(u16 *)(actor.b+0x84)=types[k];
    *(Gfx **)container.b=n==2?0:commands;*(u8 **)(node.b+0x24)=container.b;
    *(u32 *)(source.b+8)=values[p];scale.u=0x3C088889;D_800970DC=scale.f;
    saved[0]=node;saved[1]=actor;saved[2]=source;saved[3]=container;
    for(i=0;i<40;i++)old[i]=commands[i];
    if(func_15031E7C(node.b,actor.b)!=0)return 1;
    for(i=0;i<40;i++){
        u32 word=n==0&&i==layouts[l][3]?0xF2002000|expected[k*(sizeof(values)/sizeof(values[0]))+p]:old[i].words.w0;
        if(commands[i].words.w0!=word||commands[i].words.w1!=old[i].words.w1)return 2;
    }
    for(j=0;j<0x340;j++)if(node.b[j]!=saved[0].b[j]||actor.b[j]!=saved[1].b[j]||
        source.b[j]!=saved[2].b[j]||container.b[j]!=saved[3].b[j])return 3;
    if(D_800970DC!=scale.f)return 4;
}
''')
        self.receipt('native', dict(cases=8*len(FLOATS)*6*3, pointer_bytes=4, Gfx_bytes=8, return_zero=True,
            actual_complete_C=True, independently_precomputed_binary32_results=True,
            all_command_words_and_input_bytes_checked=True, first_byte_opcodes_seeded_for_host_endian=True,
            big_endian_graphics_runtime_and_FCSR_not_claimed=True))

    def qualify_owner(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
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
            self.assertEqual(text[current['value']:current['value']+current['size']], old_text[previous['value']:previous['value']+previous['size']], name)
            self.assertEqual({o-current['value']: r for o, r in rel.items() if current['value'] <= o < current['value']+current['size']},
                {o-previous['value']: r for o, r in old_rel.items() if previous['value'] <= o < previous['value']+previous['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        isolated_text, _, isolated_rel = parse_object(self.out / 'selected.o')
        target = functions[screen.FUNCTION]
        self.assertEqual(text[target['value']:target['value']+332], isolated_text[:332])
        self.assertEqual({o-target['value']: r for o, r in rel.items() if target['value'] <= o < target['value']+332}, isolated_rel)
        self.receipt('owner', dict(functions=len(functions), unchanged_neighbors=len(functions)-1,
            pools_and_relocations_unchanged=True, strict_diagnostics=0))
        return objects[1]

    def test_copied_owner_real_padder_and_independent_scale_entry_rebases(self):
        assembly = emit_padded_assembly(self.qualify_owner(), self.root / 'conker/asm/5D2C0.s',
            word_patches_path=self.root / 'conker/retail_word_patches.us.csv', filename='generated_5D2C0', rodata_symbol=action.ANCHOR)
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        end = assembly.index('\n', end)+1
        self.assertNotIn('.space', assembly[end:assembly.index('.type ', end)])
        asm, obj = self.out / 'padded.s', self.out / 'padded.o'
        asm.write_text('.text\n.globl %s\n' % screen.FUNCTION+assembly[start:end])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(asm)], check=True, capture_output=True)
        text, functions, relocs = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'], 332)
        self.assertNotIn('.rodata', sections(obj))
        self.assertEqual(relocs, {132: [('R_MIPS_HI16', 'D_800970DC')], 152: [('R_MIPS_LO16', 'D_800970DC')]})
        for entry, scale in ((screen.ENTRY, screen.SCALE), (screen.ENTRY+0x01000004, screen.SCALE), (screen.ENTRY, 0x90008004)):
            script, elf = self.out / 'padded.ld', self.out / ('rebased-%X-%X.elf' % (entry, scale))
            script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', screen.FUNCTION,
                '--defsym=D_800970DC=0x%X' % scale, '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = self.words.copy()
            expected[33] = expected[33]&0xFFFF0000 | ((scale+0x8000)>>16)&65535
            expected[38] = expected[38]&0xFFFF0000 | scale&65535
            self.assertEqual(list(struct.unpack_from('>83I', sections(elf)['.text'][1])), expected)
        self.receipt('padder', dict(body_bytes=332, slot_bytes=332, padding_words=0,
            original_scale_HI_LO_symbolic=True, independent_entry_and_carry_rebase=True, generated_data_absent=True))

    def test_installed_slot_or_previous_stub_and_guard_history(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        installed = screen.SELECTED in source
        self.assertEqual(source.count(screen.SELECTED if installed else STUB), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        expected = self.words if installed else [0x00001025, 0x03E00008]+[0]*81
        self.assertEqual((addresses[screen.FUNCTION], functions[screen.FUNCTION]), (screen.ENTRY, expected))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed', dict(C_installed=installed, byte_exact=installed, guards_added=0))


if __name__ == '__main__':
    unittest.main()
