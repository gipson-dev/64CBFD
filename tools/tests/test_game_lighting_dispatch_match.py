"""Qualify the complete dispatcher; rendering callees remain bounded ABI hooks."""

import csv
import itertools
import json
import math
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_lighting_dispatch_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.game_owner_pool import normalized_pools, assert_guard_history
from tools.tests import test_game_random_curve_record as native
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read, external_memory
from tools.tests.test_game_queued_segment_writer import STACK
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly

DIRECT, POSITIONAL = screen.SYMBOLS['func_1515E544'], screen.SYMBOLS['func_1515D914']
COMMANDS, DESCRIPTOR, ACTOR, POINT = 0x20000, 0x21000, 0x22000, 0x23000
LIGHTS, AMBIENT, ACTOR_LIGHTS = 0x24000, 0x25000, 0x26000
OLD = '''/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151462C8.s. */
s32 func_151462C8() {
    return 0;
}'''


def fixture(mode=0, actor_case=1, index=0, flags=0, page=0, gate=0):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x100)}
    for base, size in ((COMMANDS, 48), (DESCRIPTOR, 48), (ACTOR, 0x330), (POINT, 32),
            (LIGHTS, 64), (AMBIENT, 16), (ACTOR_LIGHTS, 64)):
        memory.update({base + i: 0xA5 for i in range(-16, size)})
    put(memory, DESCRIPTOR, 0xFFFFFFF9)
    put(memory, DESCRIPTOR + 4, 0x79, 1)
    put(memory, DESCRIPTOR + 0x18, 0 if gate == 2 else AMBIENT)
    put(memory, DESCRIPTOR + 0x1C, 0x80000003)
    for i in range(4):
        put(memory, DESCRIPTOR + 8 + i * 4, LIGHTS + i * 8)
        put(memory, ACTOR + 0x304 + i * 4, 0xABCDEF10 + i)
        put(memory, screen.SYMBOLS['D_800D9E10'] + i * 4, 0x87654320 + i)
    put(memory, DESCRIPTOR + 8 + index * 4, 0 if gate == 1 else LIGHTS)
    put(memory, screen.SYMBOLS['D_800BE9C0'], page, 1)
    put(memory, screen.SYMBOLS['D_800D9E20'], 0xE3, 1)
    put(memory, screen.SYMBOLS['D_800D9E21'], 0x81, 1)
    put(memory, ACTOR, 0 if actor_case == 2 else 1)
    put(memory, ACTOR + 0x3B, 0x78 if actor_case == 3 else 0x79, 1)
    put(memory, ACTOR + 4, 255 if actor_case == 4 else 7, 1)
    put(memory, ACTOR + 0x301, 0xF1, 1)
    put(memory, ACTOR + 0x302, 0 if actor_case == 5 else 0x82, 1)
    put(memory, ACTOR + 0x314, ACTOR_LIGHTS)
    for axis, value in enumerate((-3.75, 4.5, -0.0)):
        put(memory, POINT + axis * 4, bits(value))
    args = (COMMANDS, DESCRIPTOR, 0xA5123400 | mode, 0 if actor_case == 0 else ACTOR,
        0xF1234579, 0xCAFE0000 | (index & 65535), POINT, 0xACDC0000 | flags, 0xFEDCBA98)
    return memory, args


def reference(memory, args):
    commands, descriptor, mode, actor, slot, index, position, flags, extra = args
    mode, slot, flags = mode & 255, slot & 255, flags & 255
    index = index & 65535
    index = index if index < 32768 else index - 65536
    lights = read(memory, descriptor + 8 + index * 4)
    if not lights:
        return None
    ambient = read(memory, descriptor + 0x18)
    if not ambient:
        return None
    if mode == 1:
        if not actor:
            mode = 0
        elif (not read(memory, actor) or read(memory, actor + 0x3B, 1) != slot
                or read(memory, actor + 4, 1) == 255 or not read(memory, actor + 0x302, 1)):
            mode = 2
    if mode == 1:
        return DIRECT, (commands, read(memory, actor + 0x304 + index * 4),
            read(memory, actor + 0x301, 1), read(memory, actor + 0x302, 1), read(memory, actor + 0x314))
    if mode == 2:
        return DIRECT, (commands, read(memory, screen.SYMBOLS['D_800D9E10'] + index * 4),
            read(memory, screen.SYMBOLS['D_800D9E20'], 1), read(memory, screen.SYMBOLS['D_800D9E21'], 1),
            screen.SYMBOLS['D_800D9BD0'] + index * 16 + read(memory, screen.SYMBOLS['D_800BE9C0'], 1) * 8)
    xyz = tuple(math.trunc(floating(read(memory, position + axis * 4))) & 0xFFFFFFFF for axis in range(3))
    return POSITIONAL, (commands, index & 0xFFFFFFFF, *xyz, extra, lights, read(memory, descriptor),
        ambient, descriptor + 4, read(memory, descriptor + 0x1C), 0,
        8 | (2 if flags & 1 else 0) | (16 if flags & 2 else 0), 0)


def actions(call, mutate):
    if call is None:
        return ()
    target, args = call
    stores = [(args[0], 0x11223344, 4), (args[0] + 4, 0x55667788, 4)]
    if target == POSITIONAL:
        stores.append((args[9], 0xE7, 1))
    if mutate:
        stores += [(DESCRIPTOR, 0x13579BDF, 4), (ACTOR, 0x2468ACE0, 4), (POINT, bits(12), 4)]
    return stores


class LightingOracle(TriangleOracle):
    def __init__(self, words, memory, args, phase=0, result=COMMANDS + 8, mutate=False):
        super().__init__(words, memory, arguments=args, phase=phase, entry=screen.ENTRY)
        self.result, self.mutate = result, mutate

    def record_call(self, target):
        assert target in (DIRECT, POSITIONAL)
        call = (target, self.arguments(5 if target == DIRECT else 14))
        self.calls.append(call)
        self.events.append(('CALL', *call))

    def hook(self, target):
        for address, value, size in actions(self.calls[-1], self.mutate):
            self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.r[2] = self.result


class GameLightingDispatchMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-lighting-dispatch-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected', screen.SELECTED)
        cls.retail = list(struct.unpack_from('>124I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.normalized = screen.normalize(cls.words)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, data):
        (self.out / (name + '.json')).write_text(json.dumps(data, indent=2) + '\n')

    def check_case(self, memory, args, phase=0, result=COMMANDS + 8, mutate=False):
        call = reference(memory, args)
        expected = dict(memory)
        for address, value, size in actions(call, mutate):
            put(expected, address, value, size)
        models = [LightingOracle(words, memory, args, phase, result, mutate).run()
            for words in (self.words, self.normalized, self.retail)]
        traces = []
        for model in models:
            self.assertEqual((model.calls, model.r[2], external_memory(model.memory)),
                ([call] if call else [], result if call else args[0], external_memory(expected)))
            traces.append([e for e in model.events if not STACK - 0x600 <= e[1] < STACK + 0x100])
        self.assertEqual(traces[0], traces[1])
        self.assertEqual(traces[1], traces[2])
        self.assertEqual(models[0].memory, models[1].memory)
        self.assertEqual(models[1].memory, models[2].memory)
        return models

    def test_full_slot_two_independent_words_and_thirteen_relocations(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
            self.record['pool_bytes'], self.record['diagnostics']), (124, 0x48, 2, 0, ''))
        self.assertEqual(self.normalized, self.retail)
        changed = [i * 4 for i, (a, b) in enumerate(zip(self.words, self.retail)) if a != b]
        self.assertEqual(changed, [0x138, 0x13C])
        self.assertEqual(self.words[78:80], [0x00004025, 0x87A5005E])
        text, functions, rel = parse_object(self.out / 'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['size'], 496)
        self.assertEqual(len(rel), 13)
        self.assertEqual(sum(r == [('R_MIPS_26', 'func_1515E544')] for r in rel.values()), 2)
        self.assertEqual(rel[0x1CC], [('R_MIPS_26', 'func_1515D914')])
        for row in screen.owner_guards():
            offset = int(row['offset'], 16)
            self.assertNotIn(offset, rel)
            self.assertEqual(struct.unpack_from('>I', text, offset)[0], int(row['expected'], 16))
            self.assertEqual((row['insert_after'], row['omit']), ('', 'false'))
        self.receipt('slot', dict(words=124, bytes=496, frame=72, guards=2, relocations=13,
            insertions=0, omissions=0, changed_control_flow=False, raw_differences=2))

    def test_modes_actor_fallbacks_flags_narrowing_and_all_executable_words(self):
        coverage = [set(), set(), set()]
        cases = 0
        forms = itertools.chain(itertools.product(range(256), range(6), range(4), (0,)),
            itertools.product((0, 1, 2, 255), range(6), range(4), range(256)))
        for mode, actor, index, flags in forms:
            memory, args = fixture(mode, actor, index, flags, cases % 2)
            models = self.check_case(memory, args, (cases % 2) * 8,
                result=0 if cases % 3 == 0 else COMMANDS + 8, mutate=bool(cases % 2))
            for visited, model in zip(coverage, models):
                visited.update(model.visits)
            cases += 1
        for gate in (1, 2):
            memory, args = fixture(gate=gate)
            for visited, model in zip(coverage, self.check_case(memory, args)):
                visited.update(model.visits)
            cases += 1
        self.assertEqual(cases, 30722)
        wanted = set(range(screen.ENTRY, screen.ENTRY + 496, 4))
        excluded = {screen.ENTRY + offset for offset in (0xA0, 0x134)}
        self.assertEqual([wanted - c for c in coverage], [excluded] * 3)
        self.receipt('guest', dict(cases=cases, executable_words=122, excluded_offsets=[160, 308],
            all_modes_and_flags=True, actor_states=6, index_values=4, stack_phases=2,
            full_memory=True, public_traces=True, clobbered_GP_FP=True, callees='bounded ABI hooks'))

    def test_finite_binary32_truncation_and_all_slot_bytes(self):
        patterns = (0, 0x80000000, 1, 0x80000001, 0x007FFFFF, 0x807FFFFF,
            bits(0.5), bits(-0.5), bits(3.75), bits(-3.75), bits(2147483520.0), bits(-2147483648.0))
        count = 0
        for axis, pattern, flags, phase in itertools.product(range(3), patterns, (0, 1, 2, 3, 255), (0, 8)):
            memory, args = fixture(flags=flags)
            put(memory, POINT + axis * 4, pattern)
            self.check_case(memory, args, phase)
            count += 1
        for slot, phase in itertools.product(range(256), (0, 8)):
            memory, args = fixture(1)
            args = (*args[:4], 0xACDC0000 | slot, *args[5:])
            self.check_case(memory, args, phase)
            count += 1
        self.receipt('floats', dict(cases=count, finite_binary32_patterns=12, all_slot_bytes=True,
            truncation='toward zero, finite signed-int32 range only', FCSR_exceptions_and_NaNs=False))

    def test_lazy_resource_gates_and_unused_actor_position_storage(self):
        cases = 0
        for gate, mode, actor, index, phase in itertools.product((1, 2), (0, 1, 2, 255), range(6), range(4), (0, 8)):
            memory, args = fixture(mode, actor, index, 255, gate=gate)
            for address in list(memory):
                if ACTOR - 16 <= address < POINT + 32 or address in screen.SYMBOLS.values():
                    del memory[address]
            if gate == 1:
                for address in range(DESCRIPTOR + 0x18, DESCRIPTOR + 0x1C):
                    del memory[address]
            self.check_case(memory, args, phase)
            cases += 1
        for mode, actor, index in itertools.product((1, 2), range(1, 6), range(4)):
            memory, args = fixture(mode, actor, index)
            for address in range(POINT - 16, POINT + 32):
                del memory[address]
            self.check_case(memory, (*args[:6], 0, *args[7:]))
            cases += 1
        for mode, index in itertools.product((0, 2, 255), range(4)):
            memory, args = fixture(mode, 1, index)
            for address in range(ACTOR - 16, ACTOR + 0x330):
                del memory[address]
            self.check_case(memory, args)
            cases += 1
        required = 0
        for address, mode in ((DESCRIPTOR + 8, 0), (DESCRIPTOR + 0x18, 0), (POINT, 0),
                (ACTOR, 1), (ACTOR + 0x3B, 1), (ACTOR + 4, 1), (ACTOR + 0x302, 1)):
            memory, args = fixture(mode)
            del memory[address]
            for words in (self.words, self.normalized, self.retail):
                with self.assertRaisesRegex(AssertionError, 'unmapped read'):
                    LightingOracle(words, memory, args).run()
            required += 1
        for index in (-32768, -1, 4, 32767):
            memory, args = fixture(0, 0, index)
            self.check_case(memory, args)
        self.receipt('gates', dict(lazy_cases=cases, required_storage_cases=required,
            guest_only_signed_index_cases=4, no_new_bounds_check=True))

    def test_source_controls_profiles_and_semantic_negatives(self):
        groups = (screen.candidates, screen.lifetime_candidates, screen.dispatch_candidates,
            screen.guard_candidates, screen.shape_candidates, screen.sharing_candidates)
        forms = [(n, b, 'o2g3') for group in groups for n, b in group()]
        forms += [('profile-' + p, screen.BASELINE, p) for p in screen.PROFILES]
        self.assertEqual(len(forms), 244)
        records, executions = [], 0
        for name, body, profile in forms:
            record, words = screen.compile_candidate(self.root, self.out, name, body, profile)
            self.assertGreater(record['differences'], 0)
            self.assertEqual(record['diagnostics'], '')
            for mode, actor in itertools.product((0, 1, 2, 255), (0, 1, 2, 3, 4, 5)):
                memory, args = fixture(mode, actor, 3, 255, 1)
                model = LightingOracle(words, memory, args).run()
                self.assertEqual(model.calls, [reference(memory, args)], name)
                self.assertEqual(model.r[2], COMMANDS + 8, name)
                executions += 1
            records.append(record)
        negatives = dict(null_actor_global=screen.SELECTED.replace('selected = 0;', 'selected = 2;'),
            invalid_actor_position=screen.SELECTED.replace('selected = 2;', 'selected = 0;'),
            wrong_slot=screen.SELECTED.replace('actor[0x3B] != slot', 'actor[0x3B] == slot'),
            wrong_flags=screen.SELECTED.replace('environment | 8 | direction', 'environment | 4 | direction'),
            wrong_global_page=screen.SELECTED.replace('[D_800BE9C0]', '[0]'),
            placeholder='s32 func_151462C8() { return 0; }')
        detections = {}
        for name, body in negatives.items():
            _, words = screen.compile_candidate(self.root, self.out, 'negative-' + name, body)
            count = 0
            for mode, actor, page in itertools.product((0, 1, 2, 255), range(6), (0, 1)):
                memory, args = fixture(mode, actor, 3, 255, page)
                model = LightingOracle(words, memory, args).run()
                count += (model.calls, model.r[2]) != ([reference(memory, args)], COMMANDS + 8)
            self.assertGreater(count, 0, name)
            detections[name] = count
        self.receipt('controls', dict(forms=244, executions=executions, measurements=records,
            raw_exact=0, negatives=detections, faults_not_counted_as_detections=True))

    def test_native_32bit_nine_input_words_and_complete_helper_arguments(self):
        self.fixture = r'''typedef unsigned char u8; typedef short s16; typedef int s32;
typedef unsigned int u32; typedef float f32;
typedef struct { u32 words[2]; } Gfx;
typedef struct { f32 unk0, unk4, unk8; } struct17;
''' + screen.DECLARATIONS + r'''
u8 D_800BE9C0, D_800D9E20, D_800D9E21, D_800D9BD0[4][2][8];
s32 D_800D9E10[4];
static GameLightingDescriptor descriptor;
static union { u32 align; u8 bytes[0x330]; } actor;
static struct17 position;
static Gfx commands[4];
static u8 lights[64],ambient[16],actorLights[64];
static u32 wanted[14];
static int expectedKind, calls, error, fail;
typedef char layout_size[sizeof(GameLightingDescriptor)==32?1:-1];
typedef char layout_count[__builtin_offsetof(GameLightingDescriptor,count)==4?1:-1];
typedef char layout_ambient[__builtin_offsetof(GameLightingDescriptor,ambient)==24?1:-1];
static Gfx *callback(int kind,u32 *args,int count) {
    int i;
    calls++;
    if(kind!=expectedKind || calls!=1)error=1;
    for(i=0;i<count;i++)if(args[i]!=wanted[i])error=2;
    ((Gfx *)args[0])->words[0]=0x11223344;
    ((Gfx *)args[0])->words[1]=0x55667788;
    if(kind==2)*(u8 *)args[9]=0xE7;
    descriptor.capacity=0x13579BDF;
    *(s32 *)actor.bytes=0x2468ACE0;
    position.unk0=12.0f;
    return fail?(Gfx *)0:commands+2;
}
Gfx *func_1515E544(Gfx *out,s32 word,u8 a,u8 b,u8 *data) {
    u32 args[5]={(u32)out,(u32)word,a,b,(u32)data};
    return callback(1,args,5);
}
Gfx *func_1515D914(Gfx *out,s32 index,s32 x,s32 y,s32 z,s32 extra,u8 *data,
    s32 capacity,u8 *ambientData,u8 *count,s32 channels,u8 *history,s32 flags,u8 **nodes) {
    u32 args[14]={(u32)out,(u32)index,(u32)x,(u32)y,(u32)z,(u32)extra,(u32)data,
        (u32)capacity,(u32)ambientData,(u32)count,(u32)channels,(u32)history,(u32)flags,(u32)nodes};
    return callback(2,args,14);
}
static void initialize(int mode,int state,int index,int flags,int gate,int page) {
    int i,route=mode;
    for(i=0;i<8;i++)((u32 *)commands)[i]=0xA5A5A5A5;
    for(i=0;i<(int)sizeof(actor.bytes);i++)actor.bytes[i]=0xA5;
    for(i=0;i<4;i++) {
        descriptor.lights[i]=lights+i*8;
        ((s32 *)(actor.bytes+0x304))[i]=(s32)(0xABCDEF10U+i);
        D_800D9E10[i]=(s32)(0x87654320U+i);
    }
    descriptor.lights[index]=gate==1?(u8 *)0:lights;
    descriptor.ambient=gate==2?(u8 *)0:ambient;
    descriptor.capacity=-7;descriptor.count=0x79;descriptor.channels=(s32)0x80000003U;
    actor.bytes[4]=state==4?255:7;
    actor.bytes[0x3B]=state==3?0x78:0x79;
    *(s32 *)actor.bytes=state==2?0:1;
    actor.bytes[0x301]=0xF1;actor.bytes[0x302]=state==5?0:0x82;
    *(u8 **)(actor.bytes+0x314)=actorLights;
    position.unk0=-3.75f;position.unk4=4.5f;position.unk8=-0.0f;
    D_800BE9C0=page;D_800D9E20=0xE3;D_800D9E21=0x81;
    calls=error=0;fail=(mode+flags+state)&1;
    if(mode==1)route=state==0?0:state==1?1:2;
    expectedKind=gate?0:(route==1||route==2?1:2);
    wanted[0]=(u32)(commands+1);
    if(route==1) {
        wanted[1]=0xABCDEF10U+index;wanted[2]=0xF1;wanted[3]=0x82;wanted[4]=(u32)actorLights;
    } else if(route==2) {
        wanted[1]=0x87654320U+index;wanted[2]=0xE3;wanted[3]=0x81;wanted[4]=(u32)&D_800D9BD0[index][page][0];
    } else {
        wanted[1]=index;wanted[2]=(u32)-3;wanted[3]=4;wanted[4]=0;wanted[5]=0xFEDCBA98;
        wanted[6]=(u32)lights;wanted[7]=(u32)-7;wanted[8]=(u32)ambient;
        wanted[9]=(u32)&descriptor.count;wanted[10]=0x80000003;wanted[11]=0;
        wanted[12]=8|((flags&1)?2:0)|((flags&2)?16:0);wanted[13]=0;
    }
}
''' + screen.SELECTED + r'''
static int exercise(int mode,int state,int index,int flags,int gate,int page) {
    Gfx *result;
    u8 *inputActor;
    struct17 *inputPosition;
    int i;
    initialize(mode,state,index,flags,gate,page);
    inputActor=state==0?(u8 *)0:actor.bytes;
    inputPosition=expectedKind==2?&position:(struct17 *)0;
    if(gate)inputActor=(u8 *)0;
    result=func_151462C8(commands+1,&descriptor,(u8)(0xA5123400U+mode),inputActor,
        (u8)0xF1234579U,(s16)(0xCAFE0000U+index),inputPosition,
        (u8)(0xACDC0000U+flags),(s32)0xFEDCBA98U);
    if(error || calls!=(gate?0:1))return 1;
    if(result!=(gate?commands+1:fail?(Gfx *)0:commands+2))return 2;
    for(i=0;i<8;i++) {
        u32 expected=(!gate && i==2)?0x11223344:(!gate && i==3)?0x55667788:0xA5A5A5A5;
        if(((u32 *)commands)[i]!=expected)return 3;
    }
    if(descriptor.count!=(expectedKind==2?0xE7:0x79))return 4;
    return 0;
}
'''
        self.run_host(r'''
int mode,state,index,flags,gate,error;
for(mode=0;mode<256;mode++)for(state=0;state<6;state++)for(index=0;index<4;index++) {
    error=exercise(mode,state,index,(mode*17)&255,0,(mode+state)&1);
    if(error)return error;
}
for(mode=0;mode<4;mode++)for(flags=0;flags<256;flags++)for(state=0;state<6;state++)for(index=0;index<4;index++) {
    error=exercise(mode==3?255:mode,state,index,flags,0,flags&1);
    if(error)return error;
}
for(gate=1;gate<3;gate++)for(mode=0;mode<256;mode++)for(index=0;index<4;index++) {
    error=exercise(mode,1,index,255,gate,mode&1);
    if(error)return error;
}
''')
        self.receipt('native', dict(cases=32768, bits=32, warnings_as_errors=True,
            actual_dispatcher_C=True, descriptor_layout=True, all_nine_incoming_arguments=True,
            five_and_fourteen_helper_arguments=True, callbacks='bounded validating hooks',
            no_64bit_port_or_hardware_rendering_claim=True))

    def test_copied_owner_padder_neighbors_pools_and_independent_relocations(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        if screen.SELECTED in source:
            source = source.replace(screen.SELECTED, OLD).replace(screen.PROTOTYPE, 's32 func_151462C8();')
            source = source.replace(screen.DECLARATIONS, '')
        self.assertIn(OLD, source)
        selected = source.replace(OLD, screen.SELECTED).replace('s32 func_151462C8();', screen.PROTOTYPE)
        selected = selected.replace('/* Generated placeholder declarations. */', screen.DECLARATIONS + '\n/* Generated placeholder declarations. */')
        objects, warnings = [], []
        for name, body in (('baseline', source), ('selected', selected)):
            obj, warning = compile_owner(self.root, self.out, body, 'owner-' + name)
            warnings.append([(code, statement) for code, _, statement in warning])
            processed = self.out / ('owner-' + name + '-postprocessed.o')
            shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.out / ('owner-' + name + '.c')).relative_to(self.root / 'conker')), '--post-process',
                str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker', check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0], warnings[1])
        self.assertEqual(len(warnings[0]), 2)
        old_text, old_functions, old_rel = parse_object(objects[0])
        text, functions, rel = parse_object(objects[1])
        self.assertEqual(set(functions), set(old_functions))
        self.assertEqual(len(functions), 89)
        for name, current in functions.items():
            if name == screen.FUNCTION:
                continue
            previous = old_functions[name]
            self.assertEqual(text[current['value']:current['value'] + current['size']],
                old_text[previous['value']:previous['value'] + previous['size']], name)
            self.assertEqual({o - current['value']: r for o, r in rel.items() if current['value'] <= o < current['value'] + current['size']},
                {o - previous['value']: r for o, r in old_rel.items() if previous['value'] <= o < previous['value'] + previous['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        standalone, _, relocs = parse_object(self.out / 'selected.o')
        target = functions[screen.FUNCTION]
        self.assertEqual(text[target['value']:target['value'] + 496], standalone[:496])
        self.assertEqual({o - target['value']: r for o, r in rel.items() if target['value'] <= o < target['value'] + 496}, relocs)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = [row for row in csv.DictReader(stream) if row['function'] != screen.FUNCTION]
        guards += screen.owner_guards()
        guard_path = self.out / 'guards.csv'
        with guard_path.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(guards[0]))
            writer.writeheader()
            writer.writerows(guards)
        assembly = emit_padded_assembly(objects[1], self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=guard_path)
        bad_guards = [dict(row) for row in guards]
        bad_guards[-2]['expected'] = '0x00004024'
        bad_path = self.out / 'stale-guards.csv'
        with bad_path.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(bad_guards[0]))
            writer.writeheader()
            writer.writerows(bad_guards)
        with self.assertRaisesRegex(ValueError, 'stale.*word patch'):
            emit_padded_assembly(objects[1], self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
                rodata_symbol='jtbl_800A5218_game', word_patches_path=bad_path)
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), start)
        end = assembly.index('\n', end) + 1
        asm, obj = self.out / 'padded.s', self.out / 'padded.o'
        asm.write_text('.text\n.globl %s\n' % screen.FUNCTION + assembly[start:end])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(asm)], check=True, capture_output=True)
        _, padded_functions, padded_relocs = parse_object(obj)
        self.assertEqual(padded_functions[screen.FUNCTION]['size'], 496)
        self.assertEqual(padded_relocs, relocs)
        for rebased in (None, *screen.SYMBOLS):
            targets = dict(screen.SYMBOLS)
            if rebased:
                targets[rebased] += 0x01008004
            elf = self.out / ('rebased-%s.elf' % rebased)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'lighting.ld'),
                '-e', screen.FUNCTION, *['--defsym=%s=0x%X' % item for item in targets.items()],
                '-o', str(elf), str(obj)], check=True, capture_output=True)
            expected = list(self.retail)
            for offset, relocations in relocs.items():
                kind, name = relocations[0]
                address = targets[name]
                expected[offset // 4] = (expected[offset // 4] & 0xFC000000 | address >> 2 & 0x3FFFFFF) if kind == 'R_MIPS_26' else (
                    expected[offset // 4] & 0xFFFF0000 | ((address + 0x8000) >> 16 & 65535 if kind == 'R_MIPS_HI16' else address & 65535))
            self.assertEqual(list(struct.unpack_from('>124I', screen.sections(elf)['.text'][1])), expected)
        self.receipt('owner', dict(functions=89, unchanged_neighbors=88, warnings=2, new_warnings=0,
            normalized_pools_equal=True, actual_padder_words=124, independently_rebased_symbols=7,
            relocations=13, stale_word_guard_rejected=True))

    def test_installed_complete_slot_and_guard_history(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.SELECTED, source)
        self.assertEqual(source.count(screen.PROTOTYPE), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual((addresses[screen.FUNCTION], functions[screen.FUNCTION]), (screen.ENTRY, self.retail))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertEqual(guards[11061:], screen.owner_guards())


if __name__ == '__main__':
    unittest.main()
