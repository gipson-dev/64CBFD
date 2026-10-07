"""Full-width context classification and the shared original switch-table owner."""

import csv
import itertools
import json
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from tools.tests.game_owner_pool import assert_guard_history
from tools.experiments import game_texture_resolver_candidates as resolver
from tools.experiments import game_output_mode_candidates as output_mode
from tools.experiments import game_secondary_output_candidates as secondary_output

from tools.experiments import game_context_classifier_candidates as screen
from tools.experiments import game_actor_classifier_candidates as actor_screen
from tools.match_progress import load_elf_functions
from tools.patch_generated_slice_ld import load_game_data_layout
from tools.pad_generated_object import parse_object
from tools.tests.test_game_effect_dispatch_match import game_data
from tools.tests.test_game_payload_copy_wrapper_match import SignedByteOracle
from tools.tests.test_game_table_range_loader import STACK
from tools.tests.test_game_actor_triangle_transform_match import put
from tools.tests import test_game_random_curve_record as native

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly

WORLDS = (0, 1, 2, 19, 20, 21, 24, 25, 26, 38, 39, 40, 46, 47, 48, 65, 66, 67,
          0xFFFFFFFF, 0x80000000, 0x7FFFFFFF, 0x10002, 0x10014, 0x10019, 0x10027, 0x1002F, 0x10042)
CONTEXTS = (*range(256), 0xFFFFFFFF, 0xFFFFFFF0, 0xFFFF8000, 0x80000000, 0x7FFFFFFF,
            *range(0x10000, 0x10010), *range(0x80000000, 0x80000010))


def answer(world, context):
    if world in (47, 66, 39, 25): return {47: 6, 66: 7, 39: 8, 25: 5}[world]
    if context in (2, 8, 12): return 7 if world == 2 else 4
    if context == 5: return 5 if world == 20 else 9
    return {10: 0, 7: 2, 11: 1, 15: 3}.get(context, 9)


class GameContextClassifierMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-context-classifier-test'; cls.output.mkdir(exist_ok=True)
        cls.record, cls.words, cls.pool = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>57I', cls.rom, screen.ROM))
        data, base = game_data(cls.root / 'conker/build/conker.us.elf')
        start, vram, _, owners = load_game_data_layout(cls.root / 'conker')
        cls.original = data[screen.TABLE-base:screen.TABLE-base+64]
        assert cls.original == cls.rom[start+screen.TABLE-vram:start+screen.TABLE-vram+64]
        cls.owners = [owner for owner in owners if owner['address'] < screen.TABLE+64 and owner['end'] > screen.TABLE]
        cls.directory = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def memory(self, world, poison=0xA5, pool=None):
        memory = {STACK+i: poison for i in range(-0x600, 0x100)}
        memory.update({screen.WORLD+i: poison for i in range(-16, 32)})
        put(memory, screen.WORLD, world)
        memory.update({screen.TABLE+i: value for i, value in enumerate(self.original if pool is None else pool)})
        return memory

    def model(self, words, memory, context, phase=0):
        return SignedByteOracle(words, memory, entry=screen.ENTRY, arguments=(context,), phase=phase).run()

    def test_sixteen_controls_complete_direct_slot_and_table_targets(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (57, 0, 0))
        self.assertEqual(self.words, self.retail); self.assertEqual(self.pool, self.original)
        targets = (0x15141D90, 0x15141D98, 0x15141D58, 0x15141D98, 0x15141D98, 0x15141D74,
                   0x15141D98, 0x15141D40, 0x15141D58, 0x15141D98, 0x15141D38, 0x15141D48,
                   0x15141D58, 0x15141D98, 0x15141D98, 0x15141D50)
        self.assertEqual(struct.unpack('>16I', self.original), targets)
        records = []
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                record, words, pool = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                self.assertEqual(record['diagnostics'], ''); records.append(record)
                if record['differences'] == 0:
                    self.assertEqual(words, self.retail); self.assertEqual(pool, self.original)
        self.assertEqual(sum(record['differences'] == 0 for record in records), 8)
        (self.output / 'controls.json').write_text(json.dumps(records, indent=2)+'\n')

    def test_actual_padding_normal_and_alternate_world_and_pool_carries(self):
        text, functions, relocations = parse_object(self.output / 'selected.o')
        self.assertEqual(relocations, {0: [('R_MIPS_HI16', 'D_800BE9F0')], 4: [('R_MIPS_LO16', 'D_800BE9F0')],
            0x64: [('R_MIPS_HI16', '.rodata')], 0x6C: [('R_MIPS_LO16', '.rodata')]})
        layout = self.output / 'layout.csv'
        layout.write_text('version,section,filename,function,address,end\nus,game,game_16EE20,func_15141CC0,0x15141CC0,0x15141DA4\n')
        assembly = emit_padded_assembly(self.output / 'selected.o', layout, 'game_16EE20', rodata_symbol=screen.ANCHOR)
        (self.output / 'padded.s').write_text(assembly)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(self.output/'padded.o'),
            str(self.output/'padded.s')], check=True, capture_output=True)
        padded, symbols, mapped = parse_object(self.output/'padded.o')
        self.assertEqual(symbols[screen.FUNCTION]['size'], 228); self.assertEqual(padded[:228], text[:228])
        self.assertNotIn('.rodata', screen.sections(self.output/'padded.o'))
        self.assertEqual(mapped, {offset: [(kind, screen.ANCHOR if symbol == '.rodata' else symbol)
            for kind, symbol in items] for offset, items in relocations.items()})
        for table, world in ((screen.TABLE, screen.WORLD), (0x90007FFC, 0x90018004)):
            elf = self.output / ('padded-%X.elf' % table)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output/'classifier.ld'),
                '-e', screen.FUNCTION, '--defsym=%s=0x%X' % (screen.ANCHOR, table),
                '--defsym=D_800BE9F0=0x%X' % world, '-o', str(elf), str(self.output/'padded.o')], check=True, capture_output=True)
            words = list(struct.unpack_from('>57I', screen.sections(elf)['.text'][1]))
            for hi, lo, address in ((0, 4, world), (0x64, 0x6C, table)):
                self.assertEqual(words[hi//4]&65535, ((address+0x8000)>>16)&65535)
                self.assertEqual(words[lo//4]&65535, address&65535)
            if table == screen.TABLE: self.assertEqual(words, self.retail)

    def test_guest_full_width_edges_world_overrides_storage_and_single_read(self):
        coverage = [set(), set()]; cases = 0
        for world, context, phase in itertools.product(WORLDS, CONTEXTS, (0, 8)):
            memory = self.memory(world, (world+context)&255); models = []
            for index, words in enumerate((self.words, self.retail)):
                model = self.model(words, memory, context, phase); models.append(model)
                self.assertEqual(model.r[2], answer(world, context)); self.assertEqual(model.memory, memory)
                self.assertEqual(model.calls, []); coverage[index].update(model.visits)
                self.assertEqual(model.events[0], ('R', screen.WORLD, 4, world))
                reads = [event for event in model.events if event[1] == screen.WORLD]
                self.assertEqual(reads, [('R', screen.WORLD, 4, world)])
                self.assertFalse([event for event in model.events if event[0] == 'W'])
            self.assertEqual(models[0].events, models[1].events); cases += 1
        # Repeated comparison constants on annulled paths are unreachable, not coverage failures.
        unreachable = {screen.ENTRY+offset for offset in (0x1C, 0x30, 0x44, 0x58)}
        self.assertEqual(coverage, [set(range(screen.ENTRY, screen.ENTRY+228, 4))-unreachable]*2)
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases, bodies=2,
            covered_words=list(map(len, coverage)), unreachable_words=sorted(unreachable)), indent=2)+'\n')

    def test_native_actual_source_every_low_half_and_high_width_aliases(self):
        self.fixture = 'typedef int s32;static s32 D_800BE9F0;\n'+screen.SELECTED+r'''
static int expected(unsigned world, unsigned context) {
    if(world==47) return 6;
    if(world==66) return 7;
    if(world==39) return 8;
    if(world==25) return 5;
    if(context==2 || context==8 || context==12) return world==2 ? 7 : 4;
    if(context==5) return world==20 ? 5 : 9;
    if(context==10) return 0;
    if(context==7) return 2;
    if(context==11) return 1;
    if(context==15) return 3;
    return 9;
}
'''
        self.run_host('unsigned worlds[]={'+','.join(str(x)+'U' for x in WORLDS)+r'''};
unsigned edges[]={0xFFFFFFFFU,0xFFFFFFF0U,0xFFFF8000U,0x80000000U,0x7FFFFFFFU};
unsigned w,c,i,context,cases=0,before;
if(sizeof(void *)!=4 || sizeof(s32)!=4) return 80;
for(w=0;w<sizeof(worlds)/sizeof(worlds[0]);w++) {
    D_800BE9F0=(s32)worlds[w];before=(unsigned)D_800BE9F0;
    for(c=0;c<65536;c++) for(i=0;i<3;i++) {
        context=c | (i==0 ? 0 : i==1 ? 0x10000U : 0x80000000U);
        if(func_15141CC0((s32)context)!=expected(worlds[w],context)) return 81;
        if((unsigned)D_800BE9F0!=before) return 82;
        cases++;
    }
    for(i=0;i<sizeof(edges)/sizeof(edges[0]);i++) {
        if(func_15141CC0((s32)edges[i])!=expected(worlds[w],edges[i])) return 83;
        if((unsigned)D_800BE9F0!=before) return 84;
        cases++;
    }
}
if(cases!='''+str(len(WORLDS)*(65536*3+5))+r'''U) return 85;
''')
        (self.output/'native.json').write_text(json.dumps(dict(cases=len(WORLDS)*(65536*3+5),
            pointer_bytes=4, full_world_storage=True), indent=2)+'\n')

    def test_guest_minimal_world_storage_override_and_range_gates(self):
        for words in (self.words, self.retail):
            for world, context in itertools.product(WORLDS, (0, 2, 5, 15, 16, 0xFFFFFFFF)):
                memory = {}; put(memory, screen.WORLD, world)
                if world not in (47, 66, 39, 25) and context < 16:
                    memory.update({screen.TABLE+i: value for i, value in enumerate(self.original)})
                self.assertEqual(self.model(words, memory, context).r[2], answer(world, context))
            with self.assertRaisesRegex(AssertionError, 'unmapped read'): self.model(words, {}, 2)
            memory = self.memory(0); put(memory, screen.TABLE+2*4, 0x1BAD0000)
            with self.assertRaisesRegex(AssertionError, 'unowned jump'): self.model(words, memory, 2)

    def test_compiled_semantic_negatives_not_just_binary_differences(self):
        negatives = {'placeholder': 's32 func_15141CC0(s32 context) { return 0; }',
            'missing-override': screen.SELECTED.replace('world == 47', 'world == 48'),
            'wrong-override': screen.SELECTED.replace('return 8;', 'return 7;'),
            'byte-context': screen.SELECTED.replace('switch (context)', 'switch ((u8)context)'),
            'short-world': screen.SELECTED.replace('s32 world =', 's16 world ='),
            'wrong-default': screen.SELECTED.replace('    return 9;\n}', '    return 8;\n}'),
            'missing-world-two': screen.SELECTED.replace('world == 2)', 'world == 3)'),
            'missing-world-twenty': screen.SELECTED.replace('world == 20)', 'world == 21)')}
        receipts = []
        for name, body in negatives.items():
            _, words, pool = screen.compile_candidate(self.root, self.output, 'negative-'+name, body)
            differences = 0
            for world, context in itertools.product(WORLDS, (*range(32), 0x10002, 0x1000F, 0xFFFFFFFF)):
                model = self.model(words, self.memory(world, pool=pool), context)
                differences += model.r[2] != answer(world, context)
            self.assertGreater(differences, 0, name); receipts.append(dict(name=name, differences=differences))
        (self.output/'negatives.json').write_text(json.dumps(receipts, indent=2)+'\n')

    def test_connected_dispatcher_with_both_compiled_classifiers_and_live_world(self):
        from tools.tests.test_game_effect_dispatch_match import EffectOracle, memory_case, reference, CLASSIFY, MASK, CATEGORY, SEARCH, ACTOR
        _, actor_words, actor_pool = actor_screen.compile_candidate(self.root, self.output, 'actor-selected')
        dispatcher = list(struct.unpack_from('>100I', self.rom, 0x16EF2C)); helpers = {}
        for entry, words in ((CLASSIFY, actor_words), (CATEGORY, self.words),
            (MASK, struct.unpack_from('>3I', self.rom, 0x13CD7C)), (SEARCH, struct.unpack_from('>23I', self.rom, 0x17C190))):
            helpers.update({entry+i*4: word for i, word in enumerate(words)})
        answers = {identity: value for value, identities in actor_screen.GROUPS.items() for identity in identities}
        cases = 0
        for identity, world, flags, layout, mutation in itertools.product((0, 33, 121, 123, 150, 165, 255),
            (0, 2, 20, 25, 39, 47, 66, 0x1002F), (2, 5, 7, 10, 11, 15, 16, 0xFFFFFFE8), (0, 3), (0, 15, 32)):
            category = answers.get(identity, 11); selected = 0
            memory = memory_case(category, selected, -1, layout, 0)
            memory.update({actor_screen.TABLE+i: value for i, value in enumerate(actor_pool[:536]+self.pool)})
            put(memory, screen.WORLD, world); put(memory, ACTOR+4, identity, 1); put(memory, ACTOR+0x184, flags)
            wanted = reference(memory, category, selected, mutation, 0xFFFFFFFF, answer(world, flags&31))
            model = EffectOracle(dispatcher, memory, category, selected, mutation, 0xFFFFFFFF, 0, helpers).run()
            self.assertEqual((model.calls, {a: v for a, v in model.memory.items() if not STACK-0x600 <= a < STACK+0x100}),
                (wanted[1], wanted[0])); cases += 1
        self.assertEqual(cases, 2688)
        (self.output/'caller.json').write_text(json.dumps(dict(cases=cases, actor_words=45, context_words=57,
            dispatcher_words=100), indent=2)+'\n')

    def test_full_owner_pool_addends_prototypes_slots_and_unchanged_guards(self):
        owner = (self.root/'conker/src/game_16EE20.c').read_text()
        placeholder = 's32 func_15141CC0() {\n    return 0;\n}'
        baseline = owner.replace(screen.SELECTED, placeholder).replace(screen.PROTOTYPE, 's32 func_15141CC0();')
        selected = baseline.replace(placeholder, screen.SELECTED).replace('s32 func_15141CC0();', screen.PROTOTYPE)
        self.assertNotEqual(baseline, selected)
        old, old_warnings = screen.compile_owner(self.root, self.output, baseline, 'owner-baseline')
        new, new_warnings = screen.compile_owner(self.root, self.output, selected, 'owner-selected')
        self.assertEqual(old_warnings, new_warnings); self.assertEqual(len(new_warnings), 2)
        old_text, old_functions, old_relocations = parse_object(old)
        text, functions, relocations = parse_object(new)
        for name in ('func_15141A7C', 'func_15141C0C'):
            a, b = old_functions[name], functions[name]
            size = 400 if name == 'func_15141A7C' else 180
            self.assertEqual(text[b['value']:b['value']+size], old_text[a['value']:a['value']+size])
            self.assertEqual({o-b['value']: v for o, v in relocations.items() if b['value'] <= o < b['value']+size},
                {o-a['value']: v for o, v in old_relocations.items() if a['value'] <= o < a['value']+size})
        start = functions[screen.FUNCTION]['value']
        self.assertEqual(struct.unpack_from('>I', text, start+0x6C)[0]&65535, screen.POOL_OFFSET)
        standalone, _, standalone_relocations = parse_object(self.output/'selected.o')
        adjusted = bytearray(text[start:start+228])
        struct.pack_into('>I', adjusted, 0x6C, struct.unpack_from('>I', adjusted, 0x6C)[0]-screen.POOL_OFFSET)
        self.assertEqual(adjusted, standalone[:228])
        self.assertEqual({offset-start: value for offset, value in relocations.items() if start <= offset < start+228},
                         standalone_relocations)
        pool_references = {offset: items for offset, items in relocations.items()
                           if any(symbol == '.rodata' for _, symbol in items)}
        expected_pool_offsets = {functions[actor_screen.FUNCTION]['value']+offset for offset in (0x1C, 0x24, 0x3C, 0x44)}
        resolver_start = functions[resolver.FUNCTION]['value']
        output_start = functions[output_mode.FUNCTION]['value']
        secondary_start = functions[secondary_output.FUNCTION]['value']
        self.assertEqual(set(pool_references), expected_pool_offsets | {start+0x64, start+0x6C,
            resolver_start+0x20, resolver_start+0x28, output_start+0x18, output_start+0x20,
            secondary_start+0x14, secondary_start+0x1C})
        pool = screen.sections(new)['.rodata'][1]
        self.assertEqual(len(pool), 704)
        for offset, count, name, entry in ((0, 134, actor_screen.FUNCTION, actor_screen.ENTRY),
                                         (536, 16, screen.FUNCTION, screen.ENTRY)):
            # Unlinked pool targets are offsets in the owner's text, not absolute standalone addresses.
            linked = self.rom[0x249CC0+24+offset:0x249CC0+24+offset+count*4]
            expected = struct.unpack('>%dI' % count, linked)
            self.assertEqual([target-functions[name]['value']+entry for target in struct.unpack_from('>%dI' % count, pool, offset)],
                             list(expected))
        self.assertEqual([target-resolver_start+resolver.ENTRY for target in struct.unpack_from('>6I',pool,600)],
            [0x151430B8,0x151430C0,0x151430AC,0x151430A0,0x151430D4,0x151430DC])
        self.assertEqual([target-output_start+output_mode.ENTRY for target in struct.unpack_from('>5I',pool,624)],
            [0x151441F4,0x1514420C,0x151441D0,0x15144228,0x15144270])
        self.assertEqual([target-secondary_start+secondary_output.ENTRY for target in struct.unpack_from('>14I',pool,644)],
            list(secondary_output.TARGETS))
        self.assertEqual(pool[700:], bytes(4))
        (self.output/'owner.json').write_text(json.dumps(dict(warnings=len(new_warnings), pool_bytes=len(pool),
            context_addend=screen.POOL_OFFSET, resolver_addend=600, output_addend=624,
            secondary_addend=644, table_targets=175), indent=2)+'\n')
        self.assertIn(screen.SELECTED, owner); self.assertEqual(owner.count(screen.PROTOTYPE), 2)
        elf = self.root/'conker/build/conker.us.elf'
        linked, _, addresses = load_elf_functions(str(elf), 'mips-linux-gnu-objdump')
        for name, entry, offset, count in ((screen.FUNCTION, screen.ENTRY, screen.ROM, 57),
            (actor_screen.FUNCTION, actor_screen.ENTRY, actor_screen.ROM, 45), ('func_15141A7C', 0x15141A7C, 0x16EF2C, 100)):
            self.assertEqual(addresses[name], entry); self.assertEqual(linked[name], list(struct.unpack_from('>%dI' % count, self.rom, offset)))
        self.assertEqual(self.owners, [dict(rom=0x249CC0, address=0x800A5200, end=0x800A5480,
            section='.data', input='build/assets/249CC0.bin.o(.data)')])
        data, base = game_data(elf)
        self.assertEqual(data[0x800A5200-base:0x800A5480-base], self.rom[0x249CC0:0x249F40])
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream: rows = list(csv.DictReader(stream))
        assert_guard_history(self,rows); self.assertFalse([row for row in rows if row['function'] == screen.FUNCTION])


if __name__ == '__main__': unittest.main()
