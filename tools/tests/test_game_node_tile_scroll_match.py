"""Fourth-command scrolling, one-step wrap boundaries and fixed owner preservation."""

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

from tools.experiments import game_node_tile_scroll_candidates as screen
from tools.experiments.game_actor_classifier_candidates import PROFILES, sections
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.tests import test_game_node_action_match as action
from tools.tests import test_game_node_tile_match as tile
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read

NODE, ACTOR, CONTAINER, COMMANDS = tile.NODE, tile.ACTOR, tile.CONTAINER, tile.COMMANDS
COORDS = (0, 1, 2, 3, 99, 100, 101, 127, 255, 256, 1023, 2047, 2048, 3995, 4094, 4095)
ENDS = (0, 1, 2, 62, 98, 99, 100, 4094, 4095)


def wrapped(value, span):
    if value >= span:
        value -= span
    if value < 0:
        value += span
    return value


def encoded(first, last):
    s = wrapped(((first >> 12) & 4095)-100, ((last >> 12) & 4095)+2)
    t = wrapped(first & 4095, (last & 4095)+2)
    return 0xF2000000 | (s & 4095) << 12 | (t & 4095)


def fixture(selector=0x37, s=100, t=64, end_s=62, end_t=62, layout=tile.LAYOUTS[0]):
    memory = {prior.STACK+i: 0xA5 for i in range(-0x100, 0x100)}
    for base, size in ((NODE, 0x40), (CONTAINER, 8), (COMMANDS, 40*8)):
        memory.update({base+i: 0xA5 for i in range(size)})
    put(memory, NODE+1, selector, 1)
    put(memory, NODE+0x24, CONTAINER)
    put(memory, CONTAINER, COMMANDS)
    for index in range(40):
        opcode = (0, 0x7F, 0x80, 0xF1, 0xF3, 0xFF)[index % 6]
        put(memory, COMMANDS+index*8, opcode << 24 | 0x123400 | index)
        put(memory, COMMANDS+index*8+4, 0xABCD0000 | index)
    for index in (*layout, 36):
        put(memory, COMMANDS+index*8, 0xF2123400 | index)
    put(memory, COMMANDS+layout[3]*8, 0xF2000000 | s << 12 | t)
    put(memory, COMMANDS+layout[3]*8+4, 0xAB000000 | end_s << 12 | end_t)
    return memory


class ScrollReference(action.ActionReference):
    def run(self, node=NODE, actor=ACTOR):
        self.put(self.stack+4, actor)
        if self.get(node+1, 1) != 0x37:
            return 0
        commands = self.get(self.get(node+0x24))
        if commands == 0:
            return 0
        index = 0
        for match in range(4):
            while self.get(commands+index*8, 1) != 0xF2:
                index += 1
            if match != 3:
                index += 1
        address = commands+index*8
        first = self.get(address)
        last = self.get(address+4)
        self.put(address, encoded(first, last))
        return 0


class ScrollOracle(tile.TileOracle):
    def __init__(self, words, memory, args=(NODE, ACTOR), phase=0):
        TriangleOracle.__init__(self, words, memory, entry=screen.ENTRY, arguments=args, phase=phase)


class GameNodeTileScrollMatchTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-node-tile-scroll-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        cls.retail = list(struct.unpack_from('>68I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def compare(self, memory, args=(NODE, ACTOR), phase=0):
        reference = ScrollReference(memory, phase)
        expected = reference.run(*args)
        models = [ScrollOracle(words, memory, args, phase).run() for words in (self.words, self.retail)]
        for model in models:
            self.assertEqual((model.r[2], model.calls, model.events, model.memory),
                (expected, [], reference.events, reference.memory))
        self.assertEqual((models[0].r, models[0].f), (models[1].r, models[1].f))
        return models

    def test_all_words_direct_no_frame_relocations_or_generated_pool(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
            self.record['pool_bytes'], self.record['relocations']), (68, 0, 0, 0, {}))
        self.assertEqual(self.words, self.retail)
        self.receipt('slot', dict(body_words=68, slot_words=68, frame=0, raw_differences=0,
            padding_words=0, guards_added=0, calls=0, relocations=0, generated_data_bytes=0))

    def test_selector_bytes_boundaries_all_coordinate_values_and_word_coverage(self):
        seen, selectors, boundaries, exhaustive = set(), 0, 0, 0
        for selector, actor, phase in itertools.product(range(256), (0, 0xDEADBEEF), (0, 8)):
            memory = fixture(selector)
            if selector != 0x37:
                for base, size in ((NODE+0x24, 4), (CONTAINER, 8), (COMMANDS, 320)):
                    for address in range(base, base+size):
                        del memory[address]
            for model in self.compare(memory, (NODE, actor), phase):
                seen.update(model.visits)
            selectors += 1
        for s, end_s, t, end_t, layout, phase in itertools.product(
                COORDS, ENDS, COORDS, (0, 62, 4095), tile.LAYOUTS[:2], (0, 8)):
            memory = fixture(s=s, t=t, end_s=end_s, end_t=end_t, layout=layout)
            target = COMMANDS+layout[3]*8
            expected = encoded(read(memory, target), read(memory, target+4))
            for model in self.compare(memory, phase=phase):
                seen.update(model.visits)
                self.assertEqual(read(model.memory, target), expected)
                changed = {a for a in memory if memory[a] != model.memory[a]}
                self.assertTrue(changed <= set(range(target, target+4)) | set(range(prior.STACK+phase+4, prior.STACK+phase+8)))
            boundaries += 1
        for axis, value, end in itertools.product(('s', 't'), range(4096), (0, 4095)):
            arguments = dict(s=137, t=91, end_s=62, end_t=62)
            arguments[axis], arguments['end_'+axis] = value, end
            for model in self.compare(fixture(**arguments)):
                seen.update(model.visits)
            exhaustive += 1
        for layout in tile.LAYOUTS:
            for model in self.compare(fixture(layout=layout)):
                seen.update(model.visits)
        null = fixture()
        put(null, CONTAINER, 0)
        for model in self.compare(null):
            seen.update(model.visits)
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+272, 4))-seen)
        self.assertEqual(missing, [59])
        self.receipt('guest', dict(selector_cases=selectors, boundary_cases=boundaries,
            exhaustive_axis_cases=exhaustive, additional_layouts=6, null_commands=1,
            cases=selectors+boundaries+exhaustive+7, selector_bytes=256, each_axis_values=4096,
            SP_phases=2, missing_word_indices=missing, missing_only_masked_T_negative_add=True,
            raw_V0_all_GP_FP_full_trace_and_memory_equal=True, no_actor_reads=True,
            only_fourth_first_word_and_unused_actor_home_written=True, hardware_or_renderer_not_claimed=True))

    def test_required_storage_faults_scan_prefixes_null_gate_and_valid_aliases(self):
        lazy = fixture()
        put(lazy, CONTAINER, 0)
        for address in range(COMMANDS, COMMANDS+320):
            del lazy[address]
        self.compare(lazy, (NODE, 0))
        aliases = []
        memory = fixture()
        put(memory, NODE+0x24, NODE)
        put(memory, NODE, COMMANDS)
        aliases.append((memory, (NODE, ACTOR)))
        memory = fixture()
        aliases.append((memory, (NODE, NODE)))
        memory = fixture()
        put(memory, NODE+0x24, COMMANDS+4)
        put(memory, COMMANDS+4, COMMANDS)
        aliases.append((memory, (NODE, COMMANDS)))
        memory = fixture()
        put(memory, NODE+0x24, prior.STACK+4)
        aliases.append((memory, (NODE, COMMANDS)))
        memory = fixture()
        home_node = prior.STACK+3
        put(memory, home_node+0x24, CONTAINER)
        aliases.append((memory, (home_node, 0x37000000)))
        for memory, args in aliases:
            self.compare(memory, args)
        faults = []
        for missing in (prior.STACK+4, NODE+1, NODE+0x24, CONTAINER, COMMANDS,
                COMMANDS+24+1, COMMANDS+24+4):
            memory = fixture()
            del memory[missing]
            faults.append((memory, (NODE, ACTOR)))
        for missing_match in range(4):
            memory = fixture()
            for index in range(missing_match, 40):
                put(memory, COMMANDS+index*8, 0xFF000000)
            faults.append((memory, (NODE, ACTOR)))
        memory = fixture()
        put(memory, NODE+0x24, 0)
        faults.append((memory, (NODE, ACTOR)))
        faults.append((fixture(), (0, ACTOR)))
        for memory, args in faults:
            reference = ScrollReference(memory)
            with self.assertRaises(AssertionError) as failure:
                reference.run(*args)
            for words in (self.words, self.retail):
                model = ScrollOracle(words, memory, args)
                with self.assertRaises(AssertionError) as actual:
                    model.run()
                self.assertEqual(actual.exception.args, failure.exception.args)
                self.assertEqual((model.events, model.memory), (reference.events, reference.memory))
        self.receipt('gates', dict(lazy_cases=1, valid_aliases=len(aliases), fault_cases=len(faults),
            ordered_fault_prefixes_and_partial_home_effects_equal=True,
            no_new_container_null_gate_or_scan_bound=True, caller_home_aliases=2))

    def test_source_profile_controls_and_effective_semantic_negatives(self):
        records, executions, negatives = [], 0, 0
        memories = [fixture(s=s, t=t, end_s=es, end_t=et) for s,t,es,et in (
            (0, 0, 0, 0), (100, 64, 62, 62), (164, 64, 62, 62), (4095, 4095, 0, 0), (4095, 4095, 4095, 4095))]
        forms = [(n,b,'o2g3') for n,b in screen.candidates()]
        forms += [('profile-'+p,screen.SELECTED,p) for p in PROFILES if p != 'o2g3']
        for name, body, profile in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile)
            if name.startswith('negative-'):
                caught = False
                for memory in memories:
                    reference = ScrollReference(memory)
                    expected = reference.run()
                    try:
                        model = ScrollOracle(words, memory).run()
                        caught |= (model.r[2], prior.external_memory(model.memory)) != (
                            expected, prior.external_memory(reference.memory))
                    except AssertionError as failure:
                        self.assertEqual(name, 'negative-signed-opcode', failure.args)
                        self.assertEqual(failure.args[0][0], 'unmapped read')
                        caught = True
                self.assertTrue(caught, name)
                negatives += 1
            else:
                for memory in memories:
                    reference = ScrollReference(memory)
                    expected = reference.run()
                    model = ScrollOracle(words, memory).run()
                    self.assertEqual((model.r[2], prior.external_memory(model.memory)),
                        (expected, prior.external_memory(reference.memory)), name)
                    executions += 1
            records.append(record)
        self.receipt('controls', dict(forms=len(forms), ordinary_executions=executions,
            effective_semantic_negatives=negatives, measurements=records,
            exact_control_forms=sum(r['differences'] == 0 for r in records),
            all_control_GP_FP_or_read_schedule_not_claimed=True))

    def test_native32_complete_C_signed_opcode_scans_and_all_input_canaries(self):
        self.fixture = r'''typedef unsigned char u8;typedef signed char s8;typedef int s32;typedef unsigned int u32;
typedef union __attribute__((aligned(8))) {struct {u32 w0,w1;} words;unsigned long long align;} Gfx;
#define G_SETTILESIZE 0xF2
#define _SHIFTL(v,s,w) ((u32)(((u32)(v)&((1U<<(w))-1U))<<(s)))
typedef union __attribute__((aligned(8))) {u32 align;u8 b[0x40];} Storage;
typedef char widths[(sizeof(void *)==4&&sizeof(Gfx)==8)?1:-1];
static Storage node,container;static Gfx commands[40];
''' + screen.SELECTED
        self.run_host(r'''
static int layouts[6][4]={{0,1,2,3},{1,3,5,7},{0,4,9,15},{4,7,12,16},{2,6,10,20},{0,1,8,32}};
static u8 opcodes[6]={0,0x7F,0x80,0xF1,0xF3,0xFF};
Storage old_node,old_container;Gfx old[40];int k,l,i,j,n,axis,v,e,s,t,ss,tt;u32 expected;
for(axis=0;axis<2;axis++)for(v=0;v<4096;v++)for(e=0;e<2;e++){
    l=v%6;k=v%5;n=v%3;
    for(i=0;i<0x40;i++)node.b[i]=container.b[i]=0xA5;
    node.b[1]=k==0?0x37:(k==1?0:k==2?0x36:k==3?0x38:0xFF);
    *(Gfx **)container.b=n==1?0:commands;*(u8 **)(node.b+0x24)=container.b;
    for(i=0;i<40;i++){commands[i].words.w0=0x12340000+i;commands[i].words.w1=0xABCD0000+i;
        ((u8 *)&commands[i])[0]=opcodes[i%6];}
    for(i=0;i<4;i++)((u8 *)&commands[layouts[l][i]])[0]=0xF2;
    ((u8 *)&commands[36])[0]=0xF2;
    i=layouts[l][3];s=axis==0?v:137;t=axis==1?v:91;
    commands[i].words.w0=0xF2000000|s<<12|t;
    commands[i].words.w1=0xAB000000|(axis==0?(e?4095:0):62)<<12|(axis==1?(e?4095:0):62);
    ((u8 *)&commands[i])[0]=0xF2;
    old_node=node;old_container=container;for(j=0;j<40;j++)old[j]=commands[j];
    s=((old[i].words.w0>>12)&4095)-100;t=old[i].words.w0&4095;
    ss=((old[i].words.w1>>12)&4095)+2;tt=(old[i].words.w1&4095)+2;
    if(s>=ss)s-=ss;
    if(s<0)s+=ss;
    if(t>=tt)t-=tt;
    if(t<0)t+=tt;
    expected=0xF2000000|(s&4095)<<12|(t&4095);
    if(func_150334B8(node.b,0)!=0)return 1;
    for(j=0;j<40;j++)if(commands[j].words.w0!=(node.b[1]==0x37&&n!=1&&j==i?expected:old[j].words.w0)||
        commands[j].words.w1!=old[j].words.w1)return 2;
    for(j=0;j<0x40;j++)if(node.b[j]!=old_node.b[j]||container.b[j]!=old_container.b[j])return 3;
}
''')
        self.receipt('native', dict(cases=16384, pointer_bytes=4, Gfx_bytes=8,
            actual_complete_C=True, all_command_words_and_input_canaries_checked=True,
            opcode_first_bytes_seeded_for_host_endian=True, expectation_uses_actual_seeded_words=True,
            host_opcode_byte_overlaps_low_T_byte=True, big_endian_axis_coverage_is_guest_test=True,
            N64_hardware_or_renderer_not_claimed=True))

    def qualify_owner(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        if screen.SELECTED in source:
            source = source.replace(screen.SELECTED, screen.STUB)
        self.assertEqual(source.count(screen.STUB), 1)
        objects = []
        for name, body in (('baseline', source), ('selected', source.replace(screen.STUB, screen.SELECTED))):
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
            self.assertEqual({o-current['value']:r for o,r in rel.items() if current['value'] <= o < current['value']+current['size']},
                {o-previous['value']:r for o,r in old_rel.items() if previous['value'] <= o < previous['value']+previous['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        isolated, _, isolated_rel = parse_object(self.out / 'selected.o')
        target = functions[screen.FUNCTION]
        self.assertEqual(text[target['value']:target['value']+272], isolated[:272])
        self.assertFalse(isolated_rel)
        self.receipt('owner', dict(functions=len(functions), unchanged_neighbors=len(functions)-1,
            pools_and_relative_relocations_unchanged=True, strict_diagnostics=0))
        return objects[1]

    def test_copied_owner_real_padder_and_independent_entry_rebases(self):
        assembly = emit_padded_assembly(self.qualify_owner(), self.root / 'conker/asm/5D2C0.s',
            word_patches_path=self.root / 'conker/retail_word_patches.us.csv', filename='generated_5D2C0', rodata_symbol=action.ANCHOR)
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        end = assembly.index('\n', end)+1
        self.assertNotIn('.space', assembly[end:assembly.index('.type ', end)])
        asm, obj = self.out / 'padded.s', self.out / 'padded.o'
        asm.write_text('.text\n.set noreorder\n.globl %s\n' % screen.FUNCTION+assembly[start:end])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(asm)], check=True, capture_output=True)
        text, functions, relocs = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'], 272)
        self.assertEqual(relocs, {})
        self.assertNotIn('.rodata', sections(obj))
        for entry in (screen.ENTRY, screen.ENTRY+0x01000004, 0x90008004):
            script, elf = self.out / 'padded.ld', self.out / ('rebased-%X.elf' % entry)
            script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', screen.FUNCTION,
                '-o', str(elf), str(obj)], check=True, capture_output=True)
            self.assertEqual(list(struct.unpack_from('>68I', sections(elf)['.text'][1])), self.words)
        self.receipt('padder', dict(body_bytes=272, slot_bytes=272, padding_words=0,
            unchanged_under_three_entry_bases=True, generated_data_absent=True))

    def test_installed_slot_or_previous_stub_and_guard_history(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        installed = screen.SELECTED in source
        self.assertEqual(source.count(screen.SELECTED if installed else screen.STUB), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        expected = self.words if installed else [0x00001025, 0x03E00008]+[0]*66
        self.assertEqual((addresses[screen.FUNCTION], functions[screen.FUNCTION]), (screen.ENTRY, expected))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed', dict(C_installed=installed, byte_exact=installed, guards_added=0))


if __name__ == '__main__':
    unittest.main()
