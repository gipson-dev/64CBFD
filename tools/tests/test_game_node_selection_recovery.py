"""Whole dispatcher recovery, original table keys and callback-induced rereads."""

import csv
import itertools
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_node_selection_candidates as screen
from tools.experiments.game_actor_classifier_candidates import sections
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_retail_slice
from tools.tests import test_game_matrix_pair_resolver_recovery as prior
from tools.tests import test_game_node_action_match as action
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.game_owner_pool import assert_guard_history
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_node_tile_match import TileOracle
from tools.tests.test_game_point_transform_match import put, read

NODE, ACTOR, SOURCE, ATTACHMENT, ALTERNATE = 0x10000, 0x20000, 0x30000, 0x60000, 0x70000
TABLES = ((0x800970E0, 35, 0x58), (0x8009716C, 43, 0), (0x80097218, 29, 0x83),
    (0x8009728C, 16, 0x14), (0x800972CC, 463, 0x17F), (0x80097A08, 78, 0x104), (0x80097B40, 10, 0x171))
SETUP, RESET = screen.SYMBOLS['func_1503F5B8'], screen.SYMBOLS['func_1505E060']


def public(events):
    return [e for e in prior.public(events) if not screen.TABLE <= e[1] < screen.TABLE+0xB00]


def external(memory):
    return {a:v for a,v in prior.external_memory(memory).items() if not screen.TABLE <= a < screen.TABLE+0xB00}


def fixture(model=0, node_action=0x8F, actor_type=0, flags=0, source=SOURCE, attached=ATTACHMENT):
    memory = {prior.STACK+i:0xA5 for i in range(-0x100, 0x100)}
    for base in (NODE, ACTOR, SOURCE, ATTACHMENT, ALTERNATE):
        memory.update({base+i:0xA5 for i in range(0x500)})
    for address, value, size in ((ACTOR+4, model, 1), (ACTOR+5, 0, 1), (NODE+1, node_action, 1),
        (ACTOR+0x84, actor_type, 2), (ACTOR+0x2D0, source, 4), (NODE+0x48, attached, 4),
        (ACTOR+0x2E8, 0, 4), (ACTOR+0x24, 0, 4), (ACTOR+0x3C, 0, 4),
        (ATTACHMENT+4, flags, 2), (SOURCE+8, bits(2.0), 4), (SOURCE+0x3A, 0x8001, 2),
        (SOURCE+0x3C, 0x3FF, 2), (0x800902D0, 0x80017FED, 4), (0x800902D4, 0x7FFF1234, 4)):
        put(memory, address, value, size)
    for base in (ATTACHMENT, ALTERNATE):
        put(memory, base+0x18, bits(4.0))
        put(memory, base+0x39, 1, 1)
        put(memory, base+0x215, 0, 1)
    return memory


def mutations(mode, ordinal, attached):
    if mode == 1:
        return [(NODE+0x48, ALTERNATE, 4)]
    if mode == 2:
        return [(SOURCE+8, bits(7.0+ordinal), 4), (SOURCE+0x3A, 0xFFFF, 2)]
    if mode == 3:
        return [(ACTOR+0x2D0, 0, 4)]
    if mode == 4:
        return [(attached+0x39, 0, 1), (attached+0x215, 1, 1)]
    if mode == 5:
        return [(attached+0x18, bits(1.5), 4), (attached+8, bits(99.0), 4)]
    if mode == 6:
        return [(NODE+0x48, 0, 4)]
    return []


class SelectionOracle(TileOracle):
    def __init__(self, words, memory, pool, args=(NODE, ACTOR), phase=0, mode=0):
        TriangleOracle.__init__(self, words, memory, entry=screen.ENTRY, arguments=args, phase=phase)
        self.memory.update({screen.TABLE+i:v for i,v in enumerate(pool)})
        self.mode = mode

    def record_call(self, target):
        assert target in (SETUP, RESET)
        args = self.arguments(6 if target == SETUP else 1)
        if target == SETUP:
            assert args[1] == 0 and args[3:] == (0, 0, 1), args
        self.calls.append((target, *args))

    def hook(self, target):
        for address, value, size in mutations(self.mode, len(self.calls), self.calls[-1][1]):
            self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]
        self.condition = True


class SelectionReference(action.ActionReference):
    def __init__(self, memory, maps, phase=0, mode=0):
        super().__init__(memory, phase, mode)
        self.maps = maps

    def call(self, target, attached, choice=None):
        self.calls.append((target, attached, 0, choice, 0, 0, 1) if target == SETUP else (target, attached))
        for address, value, size in mutations(self.mode, len(self.calls), attached):
            self.put(address, value, size)

    def run(self, node=NODE, actor=ACTOR):
        source = self.get(actor+0x2D0)
        initial = self.get(node+0x48)
        if not initial:
            return 0
        old_flags = self.get(initial+4, 2)&0x7FFF
        model = self.get(actor+4, 1)
        actor_type = self.get(actor+0x84, 2)
        choice, copy_state = -1, True
        if model == 0x58:
            if self.get(node+1, 1) == 0x9B:
                self.put(node+2, 0x12, 1)
            if actor_type in (2, 3, 0x27, 0x28):
                choice = {2:1, 3:0, 0x27:3, 0x28:4}[actor_type]
            else:
                choice = 3 if self.get(node+1, 1) == 0x9B else 0
        elif model == 0x5B:
            choice = 0
        elif model in (0x5A, 0x74, 0x7A):
            parameter = self.get(0x800902D4 if self.get(actor+0x2E8) else 0x800902D0)
            self.put(node+0x18, parameter, 2)
            choice = self.maps[1].get(actor_type, {0x50:19, 0x51:20}.get(actor_type, 6))
        else:
            command = self.get(node+1, 1)
            if command == 0x9E:
                self.put(node+2, 9, 1)
                self.put(node+0x1E, 0x41, 2)
                self.put(node+0x20, 1, 2)
                choice = {0x1D6:1, 0x1D7:2, 0x1D8:3, 0x257:4, 0x275:5}.get(actor_type, -1)
                if actor_type in (0x1D7, 0x257, 0x275):
                    self.put(node+2, 0x13, 1)
                copy_state = False
                if self.get(node+2, 1) == 0x13:
                    self.put(node+0x1E, 0, 2)
            elif command in (0x9B, 0x9D, 0x9F):
                choice = 0
                if self.get(actor+5, 1) == 5:
                    self.put(node+2, 0, 1)
                elif command in (0x9B, 0x9D) and model == 0x8B:
                    self.put(node+2, 6, 1)
                    choice = ({0xC:6, 0x13:7} if command == 0x9B else {0x13:4, 0x20:4, 0x22:3}).get(actor_type, 0)
                elif command == 0x9F and model == 0xB5:
                    self.put(node+2, 0x12, 1)
                    choice = {0x34:1, 0x35:2, 0x36:3, 0x37:4}.get(actor_type, 0)
                else:
                    self.put(node+2, 9, 1)
                    choice = ({0x1B7:1, 0x1B8:2, 0x22E:5} if command == 0x9B else
                        {0x21C:1, 0x241:2} if command == 0x9D else {}).get(actor_type, 0)
            elif command == 0x9C:
                choice = 8
            elif command == 0x9A:
                if model == 0x87:
                    self.put(node+2, 0x12, 1)
                    choice = {1:1, 5:2}.get(actor_type, 0)
                elif model == 0x99:
                    self.put(node+2, 0x15, 1)
                    choice = self.maps[3].get(actor_type, 0)
            elif command == 0x8D:
                choice = {0x323:1, 0x324:2}.get(actor_type, 0)
            elif command == 0x8E:
                choice = {0xB4:0, 0xB6:1, 0xB5:2, 0xDD:3, 0xDE:3}.get(actor_type, -1)
                if choice == -1:
                    return 1
            elif command in (0x8F, 0x90):
                choice = self.maps[4].get(actor_type, self.maps[5].get(actor_type,
                    {0xA8:95, 0xAE:2, 0xB9:1, 0xDA:3}.get(actor_type, 0)))
            elif command in (0x83, 0x87, 0x98):
                if command == 0x98 and model == 0x8B:
                    choice = 5
                    self.put(node+2, 6, 1)
                else:
                    choices = {0x5E:0, 0x5F:1, 0xFA:1, 0x60:2, 0xB3:3} if command == 0x83 else (
                        self.maps[6] if command == 0x87 else {0x12C:0, 0x12D:3, 0x142:4, 0x12E:2, 0x358:2, 0x2AA:6})
                    choice = choices.get(actor_type, -1)
                    if choice == -1:
                        return 1
            elif command == 0x85:
                choice = {0x13E:5, 0x13F:4, 0x7C:2}.get(actor_type)
                if choice is None:
                    choice = int(0.0 < floating(self.get(actor+0x3C)))
            elif command == 0x88:
                choice = {0x11:0, 0x26:1}.get(actor_type, 2)
            elif command == 0x89:
                if self.get(actor+5, 1) == 5:
                    choice = 3
                    self.put(node+2, 0, 1)
                else:
                    choice = {0x49:0, 0x47:1, 0x81:2}.get(actor_type, -1)
                    if choice == -1:
                        return 1
                    self.put(node+2, 0x13 if actor_type == 0x81 else 9, 1)
            elif command == 0x91:
                if self.get(actor+5, 1) == 5:
                    self.put(node+2, 0, 1)
                    choice = 3 if floating(self.get(actor+0x24)) == 0.0 else 0
                else:
                    self.put(node+2, 0xE, 1)
                    choice = {0x12:2, 0x10:1}.get(actor_type, 4)
        if choice != -1:
            self.call(SETUP, self.get(node+0x48), choice)
        if source:
            attached = self.get(node+0x48)
            if choice == old_flags and self.get(source+0x3C, 2) == 0x3FF:
                self.call(RESET, attached)
                attached = self.get(node+0x48)
            self.put(attached+8, self.get(source+8))
            attached = self.get(node+0x48)
            if copy_state and (self.get(attached+0x39, 1) != 0 or self.get(attached+0x215, 1) == 0):
                self.put(attached+0x3A, self.get(source+0x3A, 2), 2)
                progress = self.get(source+0x3C, 2)
                self.put(self.get(node+0x48)+0x3C, progress, 2)
                attached = self.get(node+0x48)
            end = floating(self.get(attached+0x18))
            current = floating(self.get(attached+8))
            limit = floating(bits(end-1.0))
            if limit <= current:
                self.put(attached+8, bits(limit))
        return 0


class GameNodeSelectionRecoveryTests(unittest.TestCase):
    run_host = prior.GameMatrixPairResolverRecoveryTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-node-selection-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words, cls.pool = screen.compile_candidate(cls.root, cls.out, 'selected')
        cls.retail = list(struct.unpack_from('>1148I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        base, data = sections(cls.root / 'conker/build/conker.us.elf')['.game_data']
        cls.retail_pool = data[screen.TABLE-base:screen.TABLE-base+2696]
        cls.maps, cls.targets = [], []
        for address, count, selector_base in TABLES:
            targets = struct.unpack_from('>%dI' % count, data, address-base)
            choices = {}
            for i, target in enumerate(targets):
                delay = cls.retail[(target-screen.ENTRY)//4+1]
                if delay & 0xFFFF0000 == 0x24060000 or delay == 0x3025:
                    choices[selector_base+i] = delay & 65535 if delay != 0x3025 else 0
            cls.maps.append(choices)
            cls.targets.append(targets)
        cls.coverage, cls.cases = set(), 0
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def compare(self, memory, args=(NODE, ACTOR), phase=0, mode=0, compiled=None, ordered=True):
        reference = SelectionReference(memory, self.maps, phase, mode)
        result = reference.run(*args)
        models = [SelectionOracle(words, memory, pool, args, phase, mode).run() for words,pool in
            (compiled or (self.words, self.pool), (self.retail, self.retail_pool))]
        for model in models:
            self.assertEqual((model.r[2], model.calls, external(model.memory)),
                (result, reference.calls, external(reference.memory)))
            if ordered:
                self.assertEqual(public(model.events), reference.events)
        self.coverage.update(models[1].visits)
        self.cases += 1
        return models

    def test_06_valid_object_aliases_and_store_induced_pointer_reload(self):
        cases = 0
        for node, source, attached in ((ACTOR, SOURCE, ATTACHMENT), (NODE, NODE, ATTACHMENT),
                (NODE, ACTOR, ATTACHMENT), (NODE, ATTACHMENT, ATTACHMENT), (NODE, SOURCE, NODE)):
            memory = fixture()
            put(memory, node+1, 0x8F, 1)
            put(memory, node+0x48, attached)
            put(memory, ACTOR+0x2D0, source)
            put(memory, source+8, bits(2.0))
            put(memory, source+0x3A, 0x8001, 2)
            put(memory, source+0x3C, 0x3FF, 2)
            put(memory, attached+4, 0, 2)
            put(memory, attached+0x18, bits(4.0))
            put(memory, attached+0x39, 1, 1)
            put(memory, attached+0x215, 0, 1)
            self.compare(memory, (node, ACTOR))
            cases += 1
        memory = fixture(node_action=0x84)
        put(memory, NODE+0x48, NODE+0xC)
        put(memory, NODE+0x10, 0, 2)
        put(memory, NODE+0x14, bits(0.0))
        put(memory, NODE+0x24, bits(4.0))
        put(memory, NODE+0x45, 1, 1)
        put(memory, SOURCE+0x3C, 6, 2)
        put(memory, ATTACHMENT+0xC+0x18, bits(2.0))
        put(memory, ATTACHMENT+0xC+8, bits(2.5))
        models = self.compare(memory)
        self.assertEqual(read(models[0].memory, NODE+0x48), ATTACHMENT+0xC)
        self.assertEqual(read(models[0].memory, ATTACHMENT+0xC+8), bits(1.0))
        self.receipt('aliases', dict(cases=cases+1, source_node_actor_attachment_aliases=True,
            halfword_store_changes_node_attachment_pointer=True, subsequent_clamp_uses_changed_pointer=True,
            arbitrary_private_stack_alias_not_claimed=True))

    def test_07_compiled_controls_and_effective_semantic_negatives(self):
        records = []
        for name, body in screen.candidates():
            record, words, pool = screen.compile_candidate(self.root, self.out, name, body)
            records.append(record)
            if name.startswith('negative-'):
                memory = fixture(actor_type=0x34D) if name == 'negative-missing-choice' else (
                    fixture(node_action=0x9E) if name == 'negative-always-copy-state' else fixture())
                if name == 'negative-strict-clamp':
                    put(memory, SOURCE+8, bits(3.0))
                mode = 1 if name == 'negative-no-postsetup-reload' else 0
                if name == 'negative-strict-clamp':
                    # Equal-value stores are observable even when bytes do not change.
                    with self.assertRaises(AssertionError):
                        self.compare(memory, mode=mode, compiled=(words, pool))
                else:
                    with self.assertRaises(AssertionError):
                        self.compare(memory, mode=mode, compiled=(words, pool), ordered=False)
            else:
                for model, command, actor_type in itertools.product((0, 0x58, 0x5A, 0x87, 0x8B, 0x99, 0xB5),
                        (0x8F, 0x9B, 0x9A, 0x9E), (0, 0x13, 0x34D)):
                    self.compare(fixture(model, command, actor_type), compiled=(words, pool), ordered=False)
        self.receipt('controls', dict(records=records, ordinary_control_executions=504, effective_negatives=5))

    def test_08_actual_native32_C_route_effects_callbacks_and_object_snapshots(self):
        specs = [(m, 0x9B, 0x13, 0, 0) for m in range(256)]
        specs += [(0, command, actor_type, 0, 0) for command,actor_type in itertools.product(range(256), (0, 0x13, 0xFFFF))]
        specs += [(0, 0x8F, key, 0, 0) for key,_ in screen.BROAD_CHOICES]
        specs += [(model, command, actor_type, mode_byte, mode) for model,command,actor_type,mode_byte,mode in itertools.product(
            (0, 0x58, 0x5A, 0x87, 0x8B, 0x99, 0xB5), (0x83, 0x85, 0x87, 0x89, 0x91, 0x98, 0x9A, 0x9B, 0x9D, 0x9E, 0x9F),
            (1, 5, 0x14, 0x26, 0x34, 0x47, 0x5F, 0x7C, 0x81, 0x171, 0x1D7, 0x358), (0, 5), (0, 1, 2, 3, 4, 5))]
        cases, stores, calls = [], [], []
        bases = (NODE, ACTOR, SOURCE, ATTACHMENT, ALTERNATE)
        for model, command, actor_type, mode_byte, mode in specs:
            memory = fixture(model, command, actor_type)
            put(memory, ACTOR+5, mode_byte, 1)
            put(memory, ACTOR+0x2E8, mode_byte)
            ref = SelectionReference(memory, self.maps, mode=mode)
            result = ref.run()
            first_store, first_call = len(stores), len(calls)
            for event, address, size, value in ref.events:
                if event != 'W':
                    continue
                region = next(i for i,base in enumerate(bases) if base <= address < base+0x500)
                pointer = address == NODE+0x48 and value == ALTERNATE
                stores.append((region, address-bases[region], size, value, int(pointer)))
            for call in ref.calls:
                calls.append((int(call[0] == RESET), bases.index(call[1]), call[3] if call[0] == SETUP else 0))
            cases.append((model, command, actor_type, mode_byte, mode, result, first_store, len(stores)-first_store,
                first_call, len(calls)-first_call))
        arrays = '\n'.join('static const u32 %s[][ %d ]={%s};' % (name, width, ','.join(
            '{'+','.join('0x%Xu' % v for v in row)+'}' for row in rows)) for name,width,rows in (
                ('cases', 10, cases), ('stores', 5, stores), ('calls', 3, calls)))
        self.fixture = '''typedef unsigned char u8; typedef signed char s8;
typedef short s16; typedef unsigned short u16; typedef int s32;
typedef unsigned int u32; typedef float f32;
static union {u32 alignment;u8 bytes[0x500];} storage[5], expected[5];
static u32 observed[2][3], count, bad, mode;
s32 D_800902D0=(s32)0x80017FEDu, D_800902D4=0x7FFF1234;
static void change(u8 *attached) {
    if(mode==1) *(u8 **)(storage[0].bytes+0x48)=storage[4].bytes;
    if(mode==2) {*(f32 *)(storage[2].bytes+8)=7.0f+(f32)count;*(u16 *)(storage[2].bytes+0x3A)=0xFFFF;}
    if(mode==3) *(u8 **)(storage[1].bytes+0x2D0)=0;
    if(mode==4) {attached[0x39]=0;attached[0x215]=1;}
    if(mode==5) {*(f32 *)(attached+0x18)=1.5f;*(f32 *)(attached+8)=99.0f;}
}
static void record(u32 reset,u8 *attached,u32 choice) {
    u32 region;
    for(region=0;region<5;region++) if(attached==storage[region].bytes) break;
    if(count>=2 || region==5) {bad=1;return;}
    observed[count][0]=reset;observed[count][1]=region;observed[count][2]=choice;
    count++;change(attached);
}
void func_1503F5B8(u8 *a,s32 b,s32 c,f32 d,f32 e,s32 f) {
    if(b!=0 || d!=0.0f || e!=0.0f || f!=1) bad=1;
    record(0,a,(u32)c);
}
void func_1505E060(u8 *attached) {record(1,attached,0);}
'''+screen.SELECTED+'\n'+arrays+'\n'
        self.run_host('''u32 c,i,j,k,region,offset,size,value,result;
if(sizeof(void *)!=4 || sizeof(f32)!=4 || sizeof(u16)!=2) return 1;
for(c=0;c<sizeof(cases)/sizeof(cases[0]);c++) {
    for(i=0;i<5;i++) for(j=0;j<0x500;j++) storage[i].bytes[j]=0xA5;
    storage[1].bytes[4]=(u8)cases[c][0];storage[0].bytes[1]=(u8)cases[c][1];
    *(u16 *)(storage[1].bytes+0x84)=(u16)cases[c][2];
    storage[1].bytes[5]=(u8)cases[c][3];*(u32 *)(storage[1].bytes+0x2E8)=cases[c][3];
    *(u8 **)(storage[1].bytes+0x2D0)=storage[2].bytes;
    *(u8 **)(storage[0].bytes+0x48)=storage[3].bytes;
    *(u16 *)(storage[3].bytes+4)=0;
    *(f32 *)(storage[1].bytes+0x24)=0.0f;*(f32 *)(storage[1].bytes+0x3C)=0.0f;
    *(f32 *)(storage[2].bytes+8)=2.0f;*(u16 *)(storage[2].bytes+0x3A)=0x8001;*(u16 *)(storage[2].bytes+0x3C)=0x3FF;
    for(i=3;i<5;i++) {*(f32 *)(storage[i].bytes+0x18)=4.0f;storage[i].bytes[0x39]=1;storage[i].bytes[0x215]=0;}
    for(i=0;i<5;i++) for(j=0;j<0x500;j++) expected[i].bytes[j]=storage[i].bytes[j];
    for(i=0;i<cases[c][7];i++) {
        k=cases[c][6]+i;region=stores[k][0];offset=stores[k][1];size=stores[k][2];value=stores[k][3];
        if(stores[k][4]) value=(u32)storage[4].bytes;
        if(size==4) *(u32 *)(expected[region].bytes+offset)=value;
        else if(size==2) *(u16 *)(expected[region].bytes+offset)=(u16)value;
        else expected[region].bytes[offset]=(u8)value;
    }
    count=bad=0;mode=cases[c][4];
    result=(u32)func_15031FC8(storage[0].bytes,storage[1].bytes);
    if(bad || result!=cases[c][5] || count!=cases[c][9]) return 2;
    for(i=0;i<count;i++) for(j=0;j<3;j++) if(observed[i][j]!=calls[cases[c][8]+i][j]) return 3;
    for(i=0;i<5;i++) for(j=0;j<0x500;j++) if(storage[i].bytes[j]!=expected[i].bytes[j]) return 4;
}
''')
        self.receipt('native', dict(cases=len(cases), actual_C_executed=True, models=256, actions=256,
            six_callback_modes=True, all_five_object_byte_snapshots=True, six_argument_setup_ABI_checked=True,
            little_endian_host_not_hardware_FCSR_or_private_frame_proof=True))

    def test_09_original_table_domains_and_retail_word_coverage(self):
        self.coverage.clear()
        cases = [(model, 0x84, 0) for model in range(256)]
        cases += [(0x5A, 0x84, t) for t in (*range(43), 0x50, 0x51, 0xFFFF)]
        cases += [(0, a, 0) for a in range(256)]
        cases += [(0x99, 0x9A, t) for t in range(0x13, 0x25)]
        cases += [(0, 0x8F, t) for t in (*range(0x104, 0x152), *range(0x17F, 0x34E), 0xA8, 0xAE, 0xB9, 0xDA)]
        cases += [(0, 0x87, t) for t in range(0x170, 0x17C)]
        cases += [(m, a, t) for m,a,t in itertools.product((0x58, 0x87, 0x8B, 0xB5),
            (0x83, 0x85, 0x88, 0x89, 0x8D, 0x8E, 0x91, 0x98, 0x9A, 0x9B, 0x9D, 0x9E, 0x9F),
            (1, 2, 3, 5, 0xC, 0x10, 0x11, 0x12, 0x13, 0x20, 0x22, 0x26, 0x27, 0x28,
             0x34, 0x35, 0x36, 0x37, 0x47, 0x49, 0x5E, 0x5F, 0x60, 0x7C, 0x81, 0xB3, 0xB4, 0xB5, 0xB6,
             0xDD, 0xDE, 0xFA, 0x12C, 0x12D, 0x12E, 0x13E, 0x13F, 0x142, 0x1B7, 0x1B8, 0x1D6, 0x1D7,
             0x1D8, 0x21C, 0x22E, 0x241, 0x257, 0x275, 0x2AA, 0x323, 0x324, 0x358))]
        for model, command, actor_type in cases:
            self.compare(fixture(model, command, actor_type))
        for source in (0, SOURCE):
            self.compare(fixture(attached=0, source=source))
        self.compare(fixture(source=0))
        for model in (0x5A, 0x74, 0x7A):
            memory = fixture(model=model)
            put(memory, ACTOR+0x2E8, 1)
            self.compare(memory)
        for current in (3.0, 5.0):
            memory = fixture()
            put(memory, SOURCE+8, bits(current))
            self.compare(memory)
        for command, state, active, progress, mode_byte in itertools.product((0x84, 0x85, 0x8F, 0x91, 0x9E),
                (0, 1), (0, 1), (0, 0x3FF), (0, 5)):
            memory = fixture(node_action=command)
            put(memory, ATTACHMENT+0x39, state, 1)
            put(memory, ATTACHMENT+0x215, active, 1)
            put(memory, SOURCE+0x3C, progress, 2)
            put(memory, ACTOR+5, mode_byte, 1)
            put(memory, ACTOR+0x3C, bits(2.0))
            self.compare(memory)
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+4592, 4))-self.coverage)
        self.assertGreaterEqual(len(self.coverage), 1120, missing)
        self.receipt('coverage', dict(cases=len(cases)+168, words_executed=len(self.coverage), total_words=1148,
            missing_word_indices=missing, all_674_original_table_keys_exercised=True,
            missing_words_not_a_byte_match_or_full_FCSR_claim=True))

    def test_01_table_case_values_independent_retail_targets_and_nonmatching_boundary(self):
        _, _, _, labels = parse_retail_slice(self.root / 'conker/asm/5D2C0.s')
        for targets in self.targets:
            self.assertTrue(all(screen.ENTRY <= pc < screen.ENTRY+4592 and pc in labels for pc in targets))
        self.assertEqual(sum(map(len, self.targets)), 674)
        for pairs, table, default in ((screen.MODEL_CHOICES, 1, 6), (screen.JOINT_CHOICES, 3, 0)):
            values = dict(pairs)
            self.assertEqual(len(values), len(pairs))
            self.assertEqual({key:values.get(key, default) for key in self.maps[table]}, self.maps[table])
        broad = dict(screen.BROAD_CHOICES)
        self.assertEqual(len(broad), len(screen.BROAD_CHOICES))
        for table in (4, 5):
            self.assertEqual({key:broad.get(key, 0) for key in self.maps[table]}, self.maps[table])
        self.assertNotEqual(self.words, self.retail)
        self.assertEqual(self.record['diagnostics'], '')
        self.receipt('slot', self.record)

    def test_02_all_unsigned_types_broad_route_and_every_model_action_byte(self):
        for actor_type in range(65536):
            self.compare(fixture(actor_type=actor_type, source=0))
        types = (0, 1, 2, 3, 5, 6, 0xC, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x19, 0x20, 0x22, 0x23,
            0x26, 0x27, 0x28, 0x2A, 0x34, 0x35, 0x36, 0x37, 0x47, 0x49, 0x50, 0x51, 0x5E, 0x5F, 0x60, 0x7C,
            0x81, 0xB3, 0xB4, 0xB5, 0xB6, 0xDD, 0xDE, 0xFA, 0x12C, 0x12D, 0x12E, 0x13E, 0x13F, 0x142,
            0x171, 0x172, 0x173, 0x174, 0x175, 0x17A, 0x1B7, 0x1B8, 0x1D6, 0x1D7, 0x1D8, 0x21C, 0x22E,
            0x241, 0x257, 0x275, 0x2AA, 0x323, 0x324, 0x358, 0xFFFF)
        for model in range(256):
            self.compare(fixture(model=model, actor_type=0x13, node_action=0x9B))
        for command in range(256):
            for actor_type in types:
                self.compare(fixture(node_action=command, actor_type=actor_type))
        for model, command, actor_type, mode_byte in itertools.product((0x58, 0x5A, 0x5B, 0x74, 0x7A, 0x87, 0x8B, 0x99, 0xB5),
                (0x9A, 0x9B, 0x9D, 0x9E, 0x9F, 0x98, 0x89, 0x91), types, (0, 5)):
            memory = fixture(model, command, actor_type)
            put(memory, ACTOR+5, mode_byte, 1)
            put(memory, ACTOR+0x2E8, mode_byte)
            self.compare(memory)
        missing = sorted((pc-screen.ENTRY)//4 for pc in set(range(screen.ENTRY, screen.ENTRY+4592, 4))-self.coverage)
        self.receipt('dispatch', dict(cases=self.cases, exhaustive_unsigned_types=65536, every_model_byte=True,
            every_action_byte=True, missing_retail_word_indices=missing, return_calls_memory_order_equal=True,
            FCSR_full_callees_hardware_not_claimed=True))

    def test_03_callback_mutations_state_gate_and_binary32_clamp(self):
        floats = (0, 0x80000000, bits(-1.0), bits(1.0), bits(3.0)-1, bits(3.0), bits(3.0)+1,
            bits(4.0), 1, 0x80000001, 0x7F7FFFFF, 0xFF7FFFFF, 0x7F800000, 0xFF800000, 0x7FC00001)
        cases = 0
        for command, flags, state, active, phase, mode in itertools.product((0x84, 0x8F, 0x9E),
                (0, 0x8000, 1, 0x7FFF, 0xFFFF), (0, 1, 0x80, 0xFF), (0, 1, 0xFF), (0, 8), range(6)):
            memory = fixture(node_action=command, flags=flags)
            put(memory, ATTACHMENT+0x39, state, 1)
            put(memory, ATTACHMENT+0x215, active, 1)
            self.compare(memory, phase=phase, mode=mode)
            cases += 1
        for current, end in itertools.product(floats, floats):
            memory = fixture(node_action=0x84)
            put(memory, SOURCE+8, current)
            put(memory, ATTACHMENT+0x18, end)
            self.compare(memory)
            cases += 1
        for command, value in itertools.product((0x85, 0x91), floats):
            memory = fixture(node_action=command)
            put(memory, ACTOR+5, 5, 1)
            put(memory, ACTOR+(0x3C if command == 0x85 else 0x24), value)
            self.compare(memory)
            cases += 1
        self.receipt('callbacks', dict(cases=cases, caller_saved_GP_FP_clobbered=True, initial_source_cached=True,
            attachment_reloads_checked=True, six_callback_modes=True, two_SP_phases=True,
            state_byte_patterns=4, active_byte_patterns=3, float_patterns=len(floats),
            private_home_layout_not_matching=True))

    def test_04_absent_attachment_lazy_reads_early_returns_and_required_fault_prefixes(self):
        memory = fixture(attached=0)
        for address in (ACTOR+4, ACTOR+0x84, ATTACHMENT+4, NODE+1):
            del memory[address]
        self.compare(memory)
        for command in (0x83, 0x87, 0x89, 0x8E, 0x98):
            memory = fixture(node_action=command, actor_type=0xFFFF)
            for address in (SOURCE+8, SOURCE+0x3A, SOURCE+0x3C, ATTACHMENT+0x18, ATTACHMENT+0x39):
                del memory[address]
            self.compare(memory)
        faults = [(fixture(attached=0), ACTOR+0x2D0, 0), (fixture(), NODE+0x48, 0),
            (fixture(), ATTACHMENT+4, 0), (fixture(), ACTOR+4, 0), (fixture(), ACTOR+0x84, 0),
            (fixture(), NODE+1, 0), (fixture(model=0x5A), 0x800902D0, 0),
            (fixture(), SOURCE+8, 0), (fixture(), SOURCE+0x3C, 0), (fixture(), ATTACHMENT+0x39, 0),
            (fixture(), SOURCE+0x3A, 0), (fixture(), ATTACHMENT+0x18, 0), (fixture(), None, 6)]
        for memory, missing, mode in faults:
            if missing is not None:
                del memory[missing]
            ref = SelectionReference(memory, self.maps, mode=mode)
            with self.assertRaises(AssertionError) as error:
                ref.run()
            for words, pool in ((self.words, self.pool), (self.retail, self.retail_pool)):
                oracle = SelectionOracle(words, memory, pool, mode=mode)
                with self.assertRaises(AssertionError) as actual:
                    oracle.run()
                self.assertEqual(actual.exception.args, error.exception.args)
                self.assertEqual((oracle.calls, public(oracle.events), external(oracle.memory)),
                    (ref.calls, ref.events, external(ref.memory)))
        self.receipt('gates', dict(required_faults=len(faults), early_return_routes=5, absent_attachment_source_still_required=True,
            exact_fault_public_prefixes=True, no_postcallback_null_gate=True))

    def test_05_copied_owner_neighbors_pool_gap_and_uninstalled_guard_history(self):
        record = screen.measure_owner(self.root, self.out)
        self.assertEqual((record['neighbors_unchanged'], record['strict_diagnostics'], record['old_useful_pool_preserved']), (39, 0, True))
        self.assertEqual(record['table_loads'][0]['pool_addend'], 412)
        self.assertEqual(record['original_first_table_owner_offset'], 416)
        self.assertEqual(len(record['new_pool_identities'])-len(record['old_pool_identities']), 674)
        self.receipt('owner', record)
        source = (self.root / 'conker/src/game/generated_5D2C0.c').read_text()
        self.assertEqual(source.count(screen.STUB), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual((addresses[screen.FUNCTION], functions[screen.FUNCTION]),
            (screen.ENTRY, [0x1025, 0x03E00008]+[0]*1146))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        self.receipt('installed', dict(C_installed=False, complete_candidate_only=True, guards_added=0,
            layout_gap_open=True, byte_exact_not_claimed=True))


if __name__ == '__main__':
    unittest.main()
