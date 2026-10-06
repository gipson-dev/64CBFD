"""Qualify the direct packet wrapper and its unchanged, exact retail callee."""

import csv
import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_effect_packet_wrapper_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native


ENTRY = screen.ENTRY
CALLEE, ALLOCATOR, COPY = 0x15134908, 0x15167A68, 0x10022EC0
POINTS, RECORD = 0x20000, 0x21000
PARAMETER0, PARAMETER1 = 0x800A0280, 0x800A0284
DELTAS = (0, 1, 0x7FFF, 0x8000, 0xFFFF, 0x12348001)
CHANNELS = (0, 1, 127, 128, 255, 256, -1, 0xA5ABCDEE)
CONTEXTS = (0, 1, -1, 0x80000000, 0x7FFFFFFF, 0x81002030)
POINTERS = ((POINTS, POINTS + 4, POINTS + 8), (POINTS, POINTS, POINTS),
            (0, 0, 0), (0xFFFFFFFF, 0x80000000, 0x12345678))


def memory_case(parameter0=0x4124CCCD, parameter1=0x3F003AFB):
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({POINTS + i: 0xA5 for i in range(16)})
    memory.update({RECORD + i: 0xA5 for i in range(0x60)})
    put(memory, PARAMETER0, parameter0)
    put(memory, PARAMETER1, parameter1)
    for i, value in enumerate((1.25, -2.5, 4.0)):
        put(memory, POINTS + i * 4, bits(value))
    return memory


def packet_bytes(pointers, delta, parameter0=0x4124CCCD, parameter1=0x3F003AFB):
    return struct.pack('>5IH4B', *[v & 0xFFFFFFFF for v in pointers], parameter0, parameter1,
                       delta & 65535, 5, 6, 3, 255)


def external(memory):
    return {a: v for a, v in memory.items() if not STACK - 0x600 <= a < STACK + 0x100}


class PacketOracle(TriangleOracle):
    def __init__(self, words, memory, pointers=POINTERS[0], delta=0, channel=0, context=0,
                 phase=0, result=0x81234560, mutation=False, callee=None):
        connected = {CALLEE + i * 4: w for i, w in enumerate(callee or [])}
        super().__init__(words, memory, entry=ENTRY, phase=phase, connected=connected,
                         arguments=(*pointers, delta & 0xFFFFFFFF, channel & 0xFFFFFFFF, context & 0xFFFFFFFF))
        self.result, self.mutation, self.context, self.channel = result, mutation, context, channel
        self.snapshot = None

    def record_call(self, target):
        if target == CALLEE:
            packet, reserved, channel, context = self.r[4:8]
            assert reserved == 0 and channel == self.channel & 255 and context == self.context & 0xFFFFFFFF
            assert packet == self.before[29] - 0x1C
            self.snapshot = bytes(self.memory[packet + i] for i in range(28))
            self.calls.append((target, self.snapshot, reserved, channel, context))
        elif target == ALLOCATOR:
            self.calls.append((target, *self.arguments(6)))
        else:
            assert target == COPY
            destination, source, size = self.r[4:7]
            assert size == 28 and source == self.before[29] - 0x1C
            self.calls.append((target, destination, 'private-packet', size))

    def hook(self, target):
        if target == COPY:
            destination, source, size = self.r[4:7]
            for i in range(size):
                self.put(destination + i, self.get(source + i, 1), 1)
            result = destination
        else:
            assert target in (CALLEE, ALLOCATOR)
            if self.mutation:
                self.put(PARAMETER0, bits(20.0), 4)
                self.put(PARAMETER1, bits(-3.0), 4)
                self.put(POINTS, bits(50.0), 4)
            result = self.result
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.r[2] = result


class GameEffectPacketWrapperMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-effect-packet-wrapper-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.other_record, cls.other = screen.compile_candidate(cls.root, cls.output, 'no-debug', profile='o2')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>37I', rom, screen.ROM))
        cls.callee = list(struct.unpack_from('>50I', rom, 0x161DB8))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = screen.TYPES + screen.PACKET + r'''
f32 D_800A0280,D_800A0284;
static f32 coordinates[3];
static int calls,error,mutate;
static s16 expectedDelta;
static u8 expectedChannel;
static s32 expectedContext;
static u32 parameter0,parameter1;
static u32 word(f32 value) {union {f32 f;u32 u;} v;v.f=value;return v.u;}
static f32 number(u32 value) {union {f32 f;u32 u;} v;v.u=value;return v.f;}
void *func_15134908(void *value,s32 reserved,u8 channel,s32 context) {
    PacketEF410 *p=value;
    calls++;
    if(p->x!=coordinates || p->y!=coordinates+1 || p->z!=coordinates+2) error=1;
    if(word(p->parameter0)!=parameter0 || word(p->parameter1)!=parameter1) error=2;
    if(p->delta!=expectedDelta || p->flags!=5 || p->byte17!=6 || p->byte18!=3 || p->sentinel!=-1) error=3;
    if(reserved || channel!=expectedChannel || context!=expectedContext) error=4;
    if(mutate) {
        D_800A0280=20;D_800A0284=-3;coordinates[0]=50;
        p->flags|=2;
    }
    return (void *)0x81234560;
}
''' + screen.SELECTED + '\n'

    def test_existing_profile_emits_complete_slot_directly(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['diagnostics']), (37, 0x38, 0, ''))
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.words[-4:], [0x8FBF0014, 0x27BD0038, 0x03E00008, 0])
        self.assertEqual((self.other_record['body_words'], self.other_record['differences']), (34, 24))

    def test_named_source_profile_controls_remain_bounded(self):
        self.assertEqual((len(screen.candidates()), len(dict(screen.candidates()))), (6, 6))
        expected = {'retained-order': ((37, 0), (34, 24), (37, 0), (37, 17)),
                    'field-order': ((37, 0), (34, 24), (37, 0), (37, 17)),
                    'flags-first': ((37, 16), (34, 32), (37, 16), (37, 29)),
                    'globals-first': ((37, 8), (34, 24), (37, 8), (37, 18)),
                    'wide-delta': ((37, 1), (33, 26), (37, 1), (37, 17)),
                    'pointer-return': ((37, 0), (34, 24), (37, 0), (37, 17))}
        for name, body in screen.candidates():
            for index, profile in enumerate(screen.PROFILES):
                record, _ = screen.compile_candidate(self.root, self.output, name + '-' + profile, body, profile)
                self.assertEqual((record['body_words'], record['differences']), expected[name][index])
                self.assertEqual(record['diagnostics'], '')

    def test_all_argument_widths_opaque_handoff_padding_and_return_register(self):
        coverage, cases = set(), 0
        for pointers, delta, channel, context, phase in itertools.product(POINTERS, DELTAS, CHANNELS, CONTEXTS, (0, 8)):
            memory = memory_case()
            wanted = packet_bytes(pointers, delta) + b'\xA5\xA5'
            for words in (self.retail, self.words, self.other):
                model = PacketOracle(words, memory, pointers, delta, channel, context, phase).run()
                self.assertEqual(model.calls, [(CALLEE, wanted, 0, channel & 255, context & 0xFFFFFFFF)])
                self.assertEqual(external(model.memory), external(memory))
                self.assertEqual(model.r[2], 0x81234560)
                if words is self.retail:
                    coverage.update(model.visits)
            cases += 1
        self.assertEqual(cases, 2304)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 148, 4)))
        (self.output / 'behavior.json').write_text(json.dumps(dict(cases=cases, models=3,
             wrapper_executed_words=len(coverage), untouched_padding_bytes=2), indent=2) + '\n')

    def test_float_anchor_bit_patterns_and_post_capture_mutations(self):
        patterns = (0, 0x80000000, 0x4124CCCD, 0x3F003AFB, 0x7F800000, 0xFF800000, 0x7FC12345, 0x7FA12345)
        for parameter0, parameter1, phase, result in itertools.product(patterns, patterns, (0, 8), (0, 0x81234560)):
            memory = memory_case(parameter0, parameter1)
            for words in (self.retail, self.words, self.other):
                model = PacketOracle(words, memory, delta=0xABCDFFFF, channel=-1, context=-1,
                                     phase=phase, result=result, mutation=True).run()
                self.assertEqual(model.snapshot, packet_bytes(POINTERS[0], -1, parameter0, parameter1) + b'\xA5\xA5')
                self.assertEqual(model.r[2], result)
                self.assertEqual(model.peek(PARAMETER0, 4), bits(20.0))
                self.assertEqual(model.peek(PARAMETER1, 4), bits(-3.0))
                self.assertEqual(model.peek(POINTS, 4), bits(50.0))

    def test_connected_retail_callee_allocation_copy_pointer_reads_and_null_path(self):
        coverage, cases = set(), 0
        for delta, channel, context, phase, result, mutation in itertools.product(
                (-32768, -1, 0, 32767), (0, 128, 255), (0, -1, 0x80000000), (0, 8), (0, RECORD), (False, True)):
            memory = memory_case()
            models = [PacketOracle(words, memory, delta=delta, channel=channel, context=context,
                                  phase=phase, result=result, mutation=mutation, callee=self.callee).run()
                      for words in (self.retail, self.words, self.other)]
            for model in models:
                self.assertEqual(model.calls[:2], [(CALLEE, packet_bytes(POINTERS[0], delta) + b'\xA5\xA5',
                                                   0, channel, context & 0xFFFFFFFF),
                                                  (ALLOCATOR, 42, context & 0xFFFFFFFF, 64, 1, channel, 1)])
                self.assertEqual(model.r[2], result)
                wanted = dict(memory)
                if mutation:
                    put(wanted, PARAMETER0, bits(20.0)); put(wanted, PARAMETER1, bits(-3.0)); put(wanted, POINTS, bits(50.0))
                if result:
                    payload = bytearray(packet_bytes(POINTERS[0], delta) + b'\xA5\xA5')
                    payload[22] |= 2
                    wanted.update({RECORD + 0x10 + i: b for i, b in enumerate(payload)})
                    for i in range(3):
                        value = int.from_bytes(bytes(wanted[POINTS + i * 4 + j] for j in range(4)), 'big')
                        put(wanted, RECORD + 0x2C + i * 4, value)
                    put(wanted, RECORD + 0x38, bits(1.0 / floating(bits(floating(0x4124CCCD) * 2.0))))
                    put(wanted, RECORD + 0x3C, 0)
                    self.assertEqual(model.calls[2:], [(COPY, RECORD + 0x10, 'private-packet', 28)])
                else:
                    self.assertEqual(len(model.calls), 2)
                self.assertEqual(external(model.memory), external(wanted))
                self.assertEqual(model.calls, models[0].calls)
            coverage.update(models[0].visits)
            cases += 1
        self.assertEqual(cases, 288)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY + 148, 4)) | set(range(CALLEE, CALLEE + 200, 4)))
        (self.output / 'connected.json').write_text(json.dumps(dict(cases=cases, wrapper_words=37,
             retail_callee_words=50, allocated_record_bytes=96, copied_bytes=28), indent=2) + '\n')

    def test_native_32bit_layout_and_initialized_packet_fields(self):
        self.run_host(r'''
static s32 deltas[]={0,1,32767,32768,65535,(s32)0x12348001};
static s32 channels[]={0,1,127,128,255,256,-1,(s32)0xA5ABCDEE};
static s32 contexts[]={0,1,-1,(s32)0x80000000,0x7FFFFFFF,(s32)0x81002030};
static u32 patterns[]={0,0x80000000,0x4124CCCD,0x3F003AFB,0x7FC12345};
int a,b,c,d,e,m;
PacketEF410 p;
if(sizeof(p)!=28 || (u8 *)&p.delta-(u8 *)&p!=20 || (u8 *)&p.flags-(u8 *)&p!=22
   || (u8 *)&p.sentinel-(u8 *)&p!=25 || sizeof(void *)!=4) return 1;
for(a=0;a<6;a++) for(b=0;b<8;b++) for(c=0;c<6;c++) for(d=0;d<5;d++) for(e=0;e<5;e++) for(m=0;m<2;m++) {
    expectedDelta=(s16)deltas[a];expectedChannel=(u8)channels[b];expectedContext=contexts[c];
    parameter0=patterns[d];parameter1=patterns[e];
    D_800A0280=number(parameter0);D_800A0284=number(parameter1);
    coordinates[0]=1.25f;coordinates[1]=-2.5f;coordinates[2]=4;calls=error=0;mutate=m;
    func_150C2804(coordinates,coordinates+1,coordinates+2,expectedDelta,expectedChannel,expectedContext);
    if(calls!=1 || error) return 2;
    if(m && (D_800A0280!=20 || D_800A0284!=-3 || coordinates[0]!=50)) return 3;
    if(!m && (word(D_800A0280)!=parameter0 || word(D_800A0284)!=parameter1 || coordinates[0]!=1.25f)) return 4;
    if(coordinates[1]!=-2.5f || coordinates[2]!=4) return 5;
}
''')

    def test_wrong_packet_flag_missing_dispatch_and_copied_coordinates_are_detected(self):
        for name, body, packet in (
                ('wrong-flag', screen.SELECTED.replace('packet.flags = 5;', 'packet.flags = 4;'), screen.PACKET),
                ('placeholder', 's32 func_150C2804(void) { return 0; }', screen.PACKET),
                ('copied-values', screen.SELECTED.replace('packet.x = x;', 'packet.x = *x;')
                 .replace('packet.y = y;', 'packet.y = *y;').replace('packet.z = z;', 'packet.z = *z;'),
                 screen.PACKET.replace('f32 *x;', 'f32 x;').replace('f32 *y;', 'f32 y;').replace('f32 *z;', 'f32 z;'))):
            _, words = screen.compile_candidate(self.root, self.output, name, body, packet=packet)
            try:
                model = PacketOracle(words, memory_case()).run()
            except (AssertionError, KeyError):
                continue
            self.assertNotEqual(model.calls, [(CALLEE, packet_bytes(POINTERS[0], 0) + b'\xA5\xA5', 0, 0, 0)])

    def test_production_source_slot_globals_and_no_guards(self):
        source = (self.root / 'conker/src/game_EF410.c').read_text()
        self.assertIn(screen.PACKET, source)
        self.assertEqual(re.search(r'void func_150C2804\([^;{]+\) \{\n.*?\n\}', source, re.S).group(), screen.SELECTED)
        functions = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        self.assertEqual(functions['func_150C2804'], self.retail)
        self.assertEqual(functions['func_15134908'], self.callee)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse(any(row['function'] == 'func_150C2804' for row in csv.DictReader(stream)))
        self.assertEqual(self.words[6:9], [0x3C01800A, 0xC4240280, 0x3C01800A])


if __name__ == '__main__':
    unittest.main()
