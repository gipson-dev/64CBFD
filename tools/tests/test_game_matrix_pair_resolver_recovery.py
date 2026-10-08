"""Complete recursive routes, store-induced rereads and incoming-home lifetime."""

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

from tools.experiments import game_matrix_pair_resolver_candidates as screen
from tools.experiments.game_actor_classifier_candidates import PROFILES
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.tests import test_game_matrix_route_recovery as route
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read, external_memory
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools

NODE, ACTOR, PAGE, STACK = route.DESCRIPTOR, route.ACTOR, route.PAGE, route.STACK
PRIMARY, SECONDARY, ALT_ACTOR, ALT_OUTPUT = 0x50004, 0x50010, 0x51000, 0x52004
LOOKUP = screen.SYMBOLS['func_1503195C']


def fixture(kind=0, page=0, slot=2, offset=1):
    source = (0, 3, 1, 4, 0, 6, 7, 1)[kind]
    memory, _ = route.fixture(source, count=2, page=page)
    for base, size in ((PRIMARY-4, 32), (ALT_ACTOR, 0x200), (ALT_OUTPUT-4, 32)):
        memory.update({base+i: 0xA5 for i in range(size)})
    put(memory, NODE+2, slot, 1)
    put(memory, NODE+0x20, offset, 2)
    put(memory, ALT_ACTOR+0x3B, 3, 1)
    put(memory, ALT_ACTOR+0x1D4, route.SECONDARY)
    if kind == 4:
        put(memory, route.ATTACHMENT+0x3F6, 0, 1)
    if kind == 7:
        nodes = [route.NODE, 0x14000, 0x15000, 0x16000]
        for i, node in enumerate(nodes):
            memory.update({node+j: 0 for j in range(0x60)})
            for delta, value, size in ((0, 3, 1), (2, slot, 1), (6, 37+i, 1),
                    (0x1E, 38+i if i != 3 else 0, 2), (0x20, offset, 2),
                    (0x54, nodes[i+1] if i != 3 else 0, 4)):
                put(memory, node+delta, value, size)
    for bank in (route.BANK, route.BANK+64):
        for p in range(2):
            put(memory, bank+0x3E0+p*4, route.SECONDARY+128+p*64)
        put(memory, bank+0x1D4, route.SECONDARY+192)
    memory.update({PAGE+i: memory.get(PAGE+i, 0xA5) for i in range(4)})
    return memory, (NODE, ACTOR, PRIMARY, SECONDARY)


class PairReference:
    def __init__(self, memory, phase=0, home=0):
        self.memory, self.events, self.calls = dict(memory), [], []
        self.phase, self.home, self.lookups = phase, home, 0

    def get(self, address, size=4):
        address &= 0xFFFFFFFF
        assert all(address+i in self.memory for i in range(size)), ('unmapped read', address, size)
        value = read(self.memory, address, size)
        self.events.append(('R', address, size, value))
        return value

    def put(self, address, value):
        self.events.append(('W', address, 4, value & 0xFFFFFFFF))
        assert all(address+i in self.memory for i in range(4)), ('unmapped store', address, 4)
        put(self.memory, address, value & 0xFFFFFFFF)

    def run(self, node, actor, primary, secondary, stack=None, depth=0):
        assert depth < 8, 'acyclic fixture bound, not a production recursion limit'
        stack = STACK+self.phase if stack is None else stack
        self.put(stack+4, actor)
        attachment = self.get(node+0x48)
        if attachment:
            if not self.get(attachment+0x3F6, 1):
                return 0
            page = self.get(PAGE, 1)
            value = self.get(attachment+0x3E8+page*4)
            self.put(primary, value)
            page = self.get(PAGE, 1)
            attachment = self.get(node+0x48)
            self.put(secondary, self.get(attachment+0x3E0+page*4))
        else:
            bank = self.get(node+0x34)
            if bank:
                self.put(primary, bank+self.get(PAGE, 1)*64)
                actor = self.get(stack+4)
                slot = self.get(node+2, 1)
                bank = self.get(actor+0x1D4)
                self.put(secondary, bank+slot*64)
            else:
                key = self.get(node+0x1E, 2)
                if key:
                    actor = self.get(stack+4)
                    self.put(stack+12, secondary)
                    self.calls.append((LOOKUP, actor, key, 0))
                    parent = route.lookup(self.memory, actor, key, 0)
                    self.lookups += 1
                    if self.lookups == 1:
                        if self.home & 1:
                            self.put(stack+4, ALT_ACTOR)
                        if self.home & 2:
                            self.put(stack+12, ALT_OUTPUT)
                    secondary = self.get(stack+12)
                    if not parent:
                        return 0
                    actor = self.get(stack+4)
                    self.calls.append((screen.ENTRY, parent, actor, primary, secondary))
                    if not self.run(parent, actor, primary, secondary, stack-32, depth+1):
                        return 0
                    offset = self.get(node+0x20, 2)
                    self.put(primary, self.get(primary)+offset*64)
                    return 1
                actor = self.get(stack+4)
                bank = self.get(actor+0x1D4)
                self.put(primary, bank)
                slot = self.get(node+2, 1)
                value = bank+slot*64
                self.put(primary, value)
                self.put(secondary, value)
        return 1


class PairOracle(TriangleOracle):
    def __init__(self, words, memory, args, phase=0, home=0, connected=None):
        super().__init__(words, memory, phase=phase, connected=connected,
            entry=screen.ENTRY, arguments=args)
        self.home, self.lookups = home, 0

    def record_call(self, target):
        assert target in (screen.ENTRY, LOOKUP)
        self.calls.append((target, *self.arguments(3 if target == LOOKUP else 4)))

    def hook(self, target):
        assert target == LOOKUP
        result = route.lookup(self.memory, *self.arguments(3))
        self.lookups += 1
        if self.lookups == 1:
            if self.home & 1:
                self.put(self.r[29]+0x24, ALT_ACTOR, 4)
            if self.home & 2:
                self.put(self.r[29]+0x2C, ALT_OUTPUT, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.r[2] = result


def public(events):
    return [event for event in events if not STACK-0x600 <= event[1] < STACK+0x140]


class GameMatrixPairResolverRecoveryTests(unittest.TestCase):
    run_host = route.GameMatrixRouteRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-matrix-pair-resolver-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected', screen.SELECTED)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>85I', rom, screen.ROM))
        cls.lookup = dict(zip(range(LOOKUP, LOOKUP+28*4, 4), struct.unpack_from('>28I', rom, 0x5EE0C)))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def compare(self, memory, args, phase=0, home=0, connected=False, words=None):
        reference = PairReference(memory, phase, home)
        expected = reference.run(*args)
        models = [PairOracle(body, memory, args, phase, home, self.lookup if connected else None).run()
            for body in (words or self.words, self.retail)]
        for model in models:
            self.assertEqual((external_memory(model.memory), model.calls, model.r[2]),
                (external_memory(reference.memory), reference.calls, expected))
            if not connected:
                self.assertEqual(public(model.events), public(reference.events))
            for address in args[2:]:
                if all(address+i in memory for i in range(4)):
                    self.assertEqual(read(model.memory, address), read(reference.memory, address))
        self.assertEqual(public(models[0].events), public(models[1].events))
        return models

    def test_complete_nonmatching_body_and_retail_frame(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (84, 32, 44))
        self.assertEqual((self.record['diagnostics'], self.record['pool_bytes']), ('', 0))
        self.assertEqual(self.words[:15], self.retail[:15])
        self.assertEqual(self.words[-5:], self.retail[-5:])
        self.receipt('slot', dict(body_words=84, slot_words=85, frame=32, differences=44,
            complete_semantic_C=True, alignment_nop_not_counted=True, guards_added=0))

    def test_all_routes_full_returns_public_reads_writes_and_recursion_coverage(self):
        coverage = [set(), set()]
        cases = 0
        for kind, page, slot, offset, phase in itertools.product(range(8), range(2),
                (0, 1, 2, 255), (0, 1, 2, 255, 65535), (0, 8)):
            memory, args = fixture(kind, page, slot, offset)
            models = self.compare(memory, args, phase)
            for seen, model in zip(coverage, models):
                seen.update(model.visits)
            cases += 1
        missing = [sorted((address-screen.ENTRY)//4 for address in
            set(range(screen.ENTRY, screen.ENTRY+length*4, 4))-seen)
            for length, seen in zip((84, 85), coverage)]
        self.assertEqual(missing, [[17, 29, 63, 70], [17, 29, 64, 71]])
        self.receipt('guest', dict(cases=cases, missing_word_indices=missing,
            missing_only_unreachable_branch_likely_duplicates=True,
            saved_registers_SP_RA_checked=True, all_four_routes=True, bounded_acyclic_recursion=True))

    def test_output_aliases_fields_page_and_each_other_preserve_store_order(self):
        cases = 0
        for kind, page, phase in itertools.product(range(8), range(2), (0, 8)):
            memory, args = fixture(kind, page)
            addresses = (PRIMARY, SECONDARY, NODE, NODE+0x1C, NODE+0x20,
                NODE+0x34, NODE+0x48, ACTOR+0x1D4, PAGE)
            for primary, secondary in itertools.product(addresses, repeat=2):
                self.compare(memory, (args[0], args[1], primary, secondary), phase)
                cases += 1
        self.receipt('aliases', dict(cases=cases, ordered_public_trace=True,
            rereads_after_primary_store=True, default_intermediate_store=True))

    def test_original_lookup_connection_and_incoming_actor_secondary_home_mutations(self):
        cases, homes = 0, 0
        for kind, page, phase in itertools.product(range(8), range(2), (0, 8)):
            memory, args = fixture(kind, page)
            self.compare(memory, args, phase, connected=True)
            cases += 1
            for home in range(1, 4):
                self.compare(memory, args, phase, home)
                homes += 1
        self.receipt('connected', dict(cases=cases, homes=homes, original_lookup_28_words=True,
            full_lookup_path_coverage_not_claimed=True, caller_saved_GP_clobbered=True))

    def test_lazy_failed_routes_required_storage_and_unclamped_word_address_wrap(self):
        lazy = 0
        for kind in (4, 5, 6):
            memory, args = fixture(kind)
            memory.pop(PAGE)
            self.compare(memory, (args[0], 0 if kind == 4 else args[1], 0, 0))
            lazy += 1
        probes = [(0, NODE+0x48), (0, route.ATTACHMENT+0x3F6), (0, PAGE),
            (0, route.ATTACHMENT+0x3E8), (0, route.ATTACHMENT+0x3E0),
            (1, NODE+0x34), (1, ACTOR+0x1D4), (1, NODE+2),
            (2, NODE+0x1E), (2, route.NODE+0x48), (3, ACTOR+0x1D4), (3, NODE+2)]
        faults = 0
        for kind, missing in probes:
            memory, args = fixture(kind)
            memory.pop(missing)
            models = [PairReference(memory), PairOracle(self.words, memory, args), PairOracle(self.retail, memory, args)]
            errors = []
            for model in models:
                try:
                    model.run(*args) if isinstance(model, PairReference) else model.run()
                except (KeyError, AssertionError) as error:
                    errors.append((type(error).__name__, error.args))
                else:
                    self.fail(('required access did not fault', kind, missing))
            self.assertEqual(errors, [errors[0]]*3)
            for model in models[1:]:
                self.assertEqual(external_memory(model.memory), external_memory(models[0].memory))
                self.assertEqual(public(model.events), public(models[0].events))
            faults += 1
        for kind in (0, 1, 3):
            memory, args = fixture(kind)
            models = [PairReference(memory), PairOracle(self.words, memory, (args[0], args[1], 0, args[3])),
                PairOracle(self.retail, memory, (args[0], args[1], 0, args[3]))]
            for model in models:
                with self.assertRaisesRegex(AssertionError, 'unmapped store'):
                    model.run(args[0], args[1], 0, args[3]) if isinstance(model, PairReference) else model.run()
            faults += 1
        wraps = 0
        for kind, bank in itertools.product((1, 3), (0, 0xFFFFFFC0, 0x80000000)):
            memory, args = fixture(kind, slot=255)
            put(memory, ACTOR+0x1D4, bank)
            self.compare(memory, args)
            wraps += 1
        self.receipt('gates', dict(lazy=lazy, required_faults=faults,
            guest_word_wrap_cases=wraps, no_new_null_or_bounds_gate=True))

    def test_sixty_nine_source_profile_controls_and_effective_reread_negatives(self):
        forms = [(name, body, 'o2g3') for group in (screen.candidates, screen.lifetime_candidates,
            screen.branch_candidates, screen.flow_candidates) for name, body in group()]
        forms += [('profile-'+profile, screen.BASELINE, profile) for profile in PROFILES]
        self.assertEqual(len(forms), 69)
        records, executions = [], 0
        for name, body, profile in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile)
            self.assertGreater(record['differences'], 0)
            for kind, page in itertools.product(range(8), range(2)):
                memory, args = fixture(kind, page)
                ref = PairReference(memory)
                expected = ref.run(*args)
                model = PairOracle(words, memory, args).run()
                self.assertEqual((external_memory(model.memory), model.calls, model.r[2]),
                    (external_memory(ref.memory), ref.calls, expected), name)
                executions += 1
            records.append(record)
        negatives = dict(cached_attachment=screen.SELECTED.replace('*(u8 **)(node + 0x48) + 0x3E0',
                'attachment + 0x3E0'),
            cached_page=screen.SELECTED.replace('    u8 *parent;', '    u8 *parent;\n    u8 page;').replace(
                '*primary = ((Mtx **)(attachment + 0x3E8))[D_800BE9C0];',
                'page = D_800BE9C0;\n        *primary = ((Mtx **)(attachment + 0x3E8))[page];').replace(
                '+ 0x3E0))[D_800BE9C0]', '+ 0x3E0))[page]'),
            omitted_first_fallback_store=screen.SELECTED.replace(
                '*primary = *(Mtx **)(actor + 0x1D4);\n        *primary += node[2];',
                '*primary = *(Mtx **)(actor + 0x1D4) + node[2];'),
            wrong_offset=screen.SELECTED.replace('*primary += *(u16 *)(node + 0x20);', '*primary += 0;'))
        differences = {}
        for name, body in negatives.items():
            self.assertNotEqual(body, screen.SELECTED)
            _, words = screen.compile_candidate(self.root, self.out, 'negative-'+name, body)
            kind = 3 if name == 'omitted_first_fallback_store' else 2 if name == 'wrong_offset' else 0
            memory, args = fixture(kind, 1)
            primary = NODE+0x48 if name == 'cached_attachment' else PAGE if name == 'cached_page' else NODE if kind == 3 else PRIMARY
            args = (args[0], args[1], primary, args[3])
            ref = PairReference(memory)
            ref.run(*args)
            model = PairOracle(words, memory, args).run()
            self.assertNotEqual(external_memory(model.memory), external_memory(ref.memory), name)
            differences[name] = True
        self.receipt('controls', dict(forms=69, ordinary_executions=executions, exact=0,
            measurements=records, four_effective_public_output_negatives=differences,
            aliases_homes_and_faults_not_claimed_for_all_controls=True))

    def test_native_32bit_complete_recursive_C_valid_objects_and_output_aliases(self):
        self.fixture = r'''typedef unsigned char u8;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;
typedef union {u32 words[16];unsigned long long alignment;} Mtx;
typedef union {unsigned long long alignment;u8 bytes[0x60];} Node;
typedef union {unsigned long long alignment;u8 bytes[0x410];} Storage;
typedef char pointer_width[(sizeof(void *)==4)?1:-1];
u8 D_800BE9C0;
static Node nodes[5];static Storage actor,attachment,outputs;
static Mtx banks[3][2048];
static u8 saved[sizeof(nodes)+3*sizeof(Storage)];
static int calls,error;
static u8 *lookup(u8 *a,s32 key,s32 ordinal){
    int i;if(a!=actor.bytes||ordinal)error=1;
    calls++;for(i=1;i<5;i++)if(nodes[i].bytes[6]==key)return nodes[i].bytes;
    return 0;
}
s32 func_1503195C(u8 *a,s32 key,s32 ordinal){return (s32)lookup(a,key,ordinal);}
static int reference(u8 *node,u8 *a,Mtx **primary,Mtx **secondary){
    u8 *attachment=*(u8 **)(node+0x48),*parent;Mtx *bank;u16 key;
    if(attachment){
        if(!attachment[0x3F6])return 0;
        *primary=*(Mtx **)(attachment+0x3E8+D_800BE9C0*4);
        *secondary=*(Mtx **)(*(u8 **)(node+0x48)+0x3E0+D_800BE9C0*4);
        return 1;
    }
    bank=*(Mtx **)(node+0x34);
    if(bank){
        *primary=bank+D_800BE9C0;
        *secondary=*(Mtx **)(a+0x1D4)+node[2];return 1;
    }
    key=*(u16 *)(node+0x1E);
    if(key){
        parent=lookup(a,key,0);
        if(!parent||!reference(parent,a,primary,secondary))return 0;
        *primary=*primary+*(u16 *)(node+0x20);return 1;
    }
    bank=*(Mtx **)(a+0x1D4);*primary=bank;
    *primary=bank+node[2];*secondary=*primary;return 1;
}
static void init(int kind,int page,int slot,int offset,int pattern){
    int i,j;u8 *node=nodes[0].bytes;
    for(i=0;i<(int)sizeof(nodes);i++)((u8 *)nodes)[i]=0;
    for(i=0;i<(int)sizeof(Storage);i++){
        actor.bytes[i]=0;attachment.bytes[i]=0;outputs.bytes[i]=(u8)(i*17+pattern);
    }
    calls=error=0;D_800BE9C0=page;*(Mtx **)(actor.bytes+0x1D4)=banks[0];
    for(i=0;i<5;i++){
        nodes[i].bytes[2]=slot;nodes[i].bytes[6]=i?36+i:0;
        *(u16 *)(nodes[i].bytes+0x20)=offset;
    }
    attachment.bytes[0x3F6]=kind!=4&&kind!=6;
    for(i=0;i<2;i++){
        *(Mtx **)(attachment.bytes+0x3E8+i*4)=banks[0]+i;
        *(Mtx **)(attachment.bytes+0x3E0+i*4)=banks[1]+i;
        for(j=0;j<2;j++)*(Mtx **)((u8 *)(banks[0]+j)+0x3E0+i*4)=banks[1]+2+i;
    }
    if(kind==0||kind==4)*(u8 **)(node+0x48)=attachment.bytes;
    else if(kind==1)*(Mtx **)(node+0x34)=banks[2];
    else if(kind==2||kind==5||kind==6||kind==7){
        *(u16 *)(node+0x1E)=kind==5?99:37;
        if(kind!=7)*(u8 **)(nodes[1].bytes+0x48)=attachment.bytes;
        else for(i=1;i<4;i++)*(u16 *)(nodes[i].bytes+0x1E)=37+i;
    }
}
static void snapshot(int compare){
    int i,j=0;u8 *parts[4]={(u8 *)nodes,actor.bytes,attachment.bytes,outputs.bytes};
    int sizes[4]={sizeof(nodes),sizeof(Storage),sizeof(Storage),sizeof(Storage)};
    for(i=0;i<4;i++){int k;for(k=0;k<sizes[i];k++,j++){
        if(compare){if(saved[j]!=parts[i][k])error=2;}else saved[j]=parts[i][k];
    }}
}
static void arguments(int alias,Mtx ***primary,Mtx ***secondary){
    *primary=(Mtx **)(outputs.bytes+4);*secondary=(Mtx **)(outputs.bytes+16);
    if(alias==1)*secondary=*primary;
    if(alias==2)*primary=(Mtx **)(nodes[0].bytes+0x48);
    if(alias==3)*primary=(Mtx **)(actor.bytes+0x1D4);
}
''' + screen.SELECTED + '\n'
        self.run_host(r'''
int kind,page,s,o,alias,pattern,want,expectedCalls,actual;Mtx **primary,**secondary;
static int slots[4]={0,1,2,255},offsets[3]={0,1,127};
for(kind=0;kind<8;kind++)for(page=0;page<2;page++)for(s=0;s<4;s++)
for(o=0;o<3;o++)for(alias=0;alias<4;alias++)for(pattern=0;pattern<3;pattern++){
    init(kind,page,slots[s],offsets[o],pattern);arguments(alias,&primary,&secondary);
    want=reference(nodes[0].bytes,actor.bytes,primary,secondary);expectedCalls=calls;
    if(error)return 1;
    snapshot(0);
    init(kind,page,slots[s],offsets[o],pattern);arguments(alias,&primary,&secondary);
    actual=func_15031070(nodes[0].bytes,actor.bytes,primary,secondary);snapshot(1);
    if(error||actual!=want||calls!=expectedCalls)return 2;
}
init(4,0,2,1,0);
if(func_15031070(nodes[0].bytes,0,0,0)||calls||error)return 3;
init(5,0,2,1,0);
if(func_15031070(nodes[0].bytes,actor.bytes,0,0)||calls!=1||error)return 4;
init(6,0,2,1,0);
if(func_15031070(nodes[0].bytes,actor.bytes,0,0)||calls!=1||error)return 5;
''')
        self.receipt('native', dict(cases=8*2*4*3*4*3, lazy_cases=3, pointer_bytes=4,
            actual_complete_recursive_C=True, four_output_aliases=True,
            valid_matrix_objects=True, lookup='bounded validating native callback',
            guest_wrapping_and_private_home_mutations_not_claimed=True))

    def qualify_owner(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        stub = 's32 func_15031070() {\n    return 0;\n}'
        if stub not in source:
            self.assertEqual(source.count(screen.SELECTED), 1)
            source = source.replace(screen.SELECTED, stub).replace('extern u8 D_800BE9C0;\n', '', 1)
        self.assertEqual(source.count(stub), 1)
        selected = source.replace(stub, screen.SELECTED).replace('#include <ultra64.h>\n',
            '#include <ultra64.h>\nextern u8 D_800BE9C0;\n', 1)
        objects, warnings = [], []
        for name, body in (('baseline', source), ('selected', selected)):
            obj, diagnostic = compile_owner(self.root, self.out, body, 'owner-'+name)
            warnings.append([(item[0], item[2]) for item in diagnostic])
            processed = self.out / ('owner-'+name+'-postprocessed.o')
            shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.out / ('owner-'+name+'.c')).relative_to(self.root / 'conker')), '--post-process',
                str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker',
                check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0], warnings[1])
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
        standalone, isolated_functions, isolated_rel = parse_object(self.out / 'selected.o')
        target, size = functions[screen.FUNCTION], isolated_functions[screen.FUNCTION]['size']
        self.assertEqual(target['size'], size)
        self.assertEqual(text[target['value']:target['value']+size], standalone[:size])
        self.assertEqual({o-target['value']: r for o, r in rel.items()
            if target['value'] <= o < target['value']+size}, isolated_rel)
        self.receipt('owner', dict(functions=len(functions), unchanged_neighbors=len(functions)-1,
            warnings=len(warnings[0]), normalized_pools_equal=True, target_matches_isolated=True,
            object_words=size//4, meaningful_body_words=84, no_production_edit_by_test=True))
        return objects[1]

    def test_copied_owner_neighbors_relocations_pools_and_warning_statements_unchanged(self):
        self.qualify_owner()

    def test_real_padder_preserves_complete_body_and_self_call_symbol_relocations(self):
        owner = self.qualify_owner()
        assembly = emit_padded_assembly(owner, self.root / 'conker/asm/5D2C0.s',
            word_patches_path=self.root / 'conker/retail_word_patches.us.csv', filename='generated_5D2C0')
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        end = assembly.index('\n', end)+1
        next_function = assembly.index('.globl ', end)
        self.assertEqual(assembly[end:next_function].strip(), '.space 0x4, 0')
        asm, obj = self.out / 'padded.s', self.out / 'padded.o'
        asm.write_text('.text\n.globl %s\n' % screen.FUNCTION+assembly[start:next_function])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(asm)],
            check=True, capture_output=True)
        _, functions, relocs = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'], 336)
        self.assertEqual(relocs, parse_object(self.out / 'selected.o')[2])
        self.assertTrue(any(('R_MIPS_26', screen.FUNCTION) in entries for entries in relocs.values()))
        for rebased in (None, *screen.SYMBOLS, screen.FUNCTION):
            targets = dict(screen.SYMBOLS, **{screen.FUNCTION: screen.ENTRY})
            if rebased:
                targets[rebased] += 0x01008004
            script, elf = self.out / 'padded.ld', self.out / ('rebased-%s.elf' % rebased)
            script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % targets[screen.FUNCTION])
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X' % item for item in targets.items() if item[0] != screen.FUNCTION],
                '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = self.words+[0]
            for offset, entries in relocs.items():
                kind, name = entries[0]
                address = targets[name]
                expected[offset//4] = (expected[offset//4] & 0xFC000000 | address >> 2 & 0x3FFFFFF) if kind == 'R_MIPS_26' else (
                    expected[offset//4] & 0xFFFF0000 | ((address+0x8000) >> 16 & 65535
                        if kind == 'R_MIPS_HI16' else address & 65535))
            self.assertEqual(list(struct.unpack_from('>85I', route.screen.sections(elf)['.text'][1])), expected)
        self.receipt('padder', dict(body_words=84, slot_words=85, relocations=len(relocs),
            rebased_symbols=3, guards_added=0, insertions=0, tail_padding_words=1,
            self_call_retained_as_symbol=True, preserves_raw_nonmatching_body=True))

    def test_actual_matrix_wrapper_connection_and_recursive_resolver_paths(self):
        from tools.experiments import game_matrix_route_layout_candidates as fit
        _, wrapper = route.screen.compile_candidate(self.root, self.out, 'caller-selected', fit.SELECTED)
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        original_wrapper = list(struct.unpack_from('>120I', rom, route.screen.ROM))
        helpers = dict(self.lookup)
        for entry, offset, length in ((route.CONVERT, 0x21D368, 46), (route.POINT, 0xD4E10, 40),
                (route.LIST, 0x173354, 117), (route.matrix_list.TRANSLATE, 0x16F7C4, 49)):
            helpers.update(zip(range(entry, entry+length*4, 4), struct.unpack_from('>%dI' % length, rom, offset)))
        cases, recursive, visited = 0, 0, set()
        for kind, count, page, alias, phase, zero in itertools.product(range(8), (-1, 0, 2),
                range(2), range(3), (0, 8), (False, True)):
            memory, args = route.fixture(kind, count, page, alias=alias)
            if zero:
                for axis in range(3):
                    put(memory, route.SOURCES+axis*4, 0)
            for chained in (False, True) if kind == 2 else (False,):
                if chained:
                    parent = route.NODE+0x80
                    memory.update({parent+i: 0 for i in range(0x60)})
                    put(memory, route.NODE+0x34, 0)
                    put(memory, route.NODE+0x1E, 38, 2)
                    put(memory, route.NODE+0x54, parent)
                    put(memory, parent, 3, 1)
                    put(memory, parent+6, 38, 1)
                    put(memory, parent+0x34, route.DESCRIPTOR_BANK)
                models = []
                for caller in (wrapper, original_wrapper):
                    for resolver in (self.words, self.retail):
                        connected = dict(helpers)
                        connected.update(zip(range(screen.ENTRY, screen.ENTRY+len(resolver)*4, 4), resolver))
                        model = route.MatrixRouteOracle(caller, memory, args, phase=phase, connected=connected).run()
                        models.append(model)
                        visited.update(model.visits)
                expected, _, result = route.reference(memory, args, phase=phase)
                for model in models:
                    self.assertEqual((external_memory(model.memory), model.r[2]), (external_memory(expected), result))
                    self.assertEqual((model.calls, model.private_outputs, model.private_matrices),
                        (models[0].calls, models[0].private_outputs, models[0].private_matrices))
                    self.assertEqual(public(model.events), public(models[0].events))
                recursive += chained
                cases += 1
        helpers_seen = {hex(entry): sum(entry <= pc < entry+length*4 for pc in visited)
            for entry, length in ((LOOKUP, 28), (screen.ENTRY, 85), (route.CONVERT, 45),
                (route.POINT, 40), (route.LIST, 117), (route.matrix_list.TRANSLATE, 49))}
        self.assertTrue(all(helpers_seen.values()), helpers_seen)
        self.receipt('caller', dict(cases=cases, recursive=recursive, executions=cases*4,
            actual_wrapper_C_and_retail=True, actual_helpers=True, helper_words_visited=helpers_seen,
            private_argument_addresses_equal=True, public_traces_equal=True,
            full_helper_coverage_and_full_stack_equivalence_not_claimed=True))

    def test_installed_slot_or_placeholder_explicit_and_guard_history_unchanged(self):
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'),
            'mips-linux-gnu-objdump')
        installed = screen.SELECTED in source
        self.assertEqual(source.count(screen.SELECTED), int(installed))
        expected = self.words+[0] if installed else [0x00001025, 0x03E00008, 0]+[0]*82
        self.assertEqual((addresses[screen.FUNCTION], functions[screen.FUNCTION]), (screen.ENTRY, expected))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed', dict(installed_complete_C=installed, slot_words=85,
            body_words=84 if installed else 3, differences=sum(a != b for a, b in zip(expected, self.retail)),
            frame=32 if installed else 0, byte_exact=False, guards_added=0))
