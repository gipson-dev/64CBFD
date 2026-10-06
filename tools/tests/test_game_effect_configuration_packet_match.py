"""Bound the complete configuration packet handoff, not its unrecovered callee."""

import csv
import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_effect_configuration_packet_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

ENTRY, CALLEE, SOURCE = screen.ENTRY, screen.CALLEE, 0x20000
GLOBALS = (0x800A8CC0, 0x800A8CC4, 0x800A8CC8, 0x800A8CCC, 0x800A8CD0)
ANCHORS = (0xBFA978D6, 0x3F3E76C9, 0x3F19999A, 0x3F4CCCCD, 0x41D174BD)
PATTERNS = (0, 0x80000000, 1, 0x007FFFFF, 0x3F800000, 0x7F7FFFFF,
            0x7F800000, 0xFF800000, 0x7FC12345, 0x7FA12345)


def external(memory):
    return {a: v for a, v in memory.items() if not STACK - 0x600 <= a < STACK + 0x100}


def memory_case(pattern=0):
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({SOURCE + i: (i * 17 + 13) & 255 for i in range(64)})
    memory.update({GLOBALS[0] + i: 0xA5 for i in range(-16, 36)})
    for i, address in enumerate(GLOBALS):
        put(memory, address, ANCHORS[i] if pattern == 0 else PATTERNS[(pattern + i) % len(PATTERNS)])
    for i in range(3):
        put(memory, SOURCE + i * 4, PATTERNS[(pattern + i + 2) % len(PATTERNS)])
    return memory


def packet_bytes(memory, source):
    point = bytes(memory[source + i] for i in range(12))
    anchors = [bytes(memory[a + i] for i in range(4)) for a in GLOBALS]
    return (struct.pack('>2I', 10, 7) + point + struct.pack('>4h2I', 0, 255, -53, 24,
            0x41200000, 0x41000000) + b''.join(anchors[:2]) + struct.pack('>2h', 50, 20)
            + b''.join(anchors[2:]))


class ConfigurationOracle(TriangleOracle):
    def __init__(self, words, memory, source=SOURCE, selector=0, scale=0, channel=0,
                 context=0, phase=0, mutation=False, result=0x81234560):
        super().__init__(words, memory, entry=ENTRY, phase=phase,
            arguments=(source, selector & 0xFFFFFFFF, scale, channel & 0xFFFFFFFF, context & 0xFFFFFFFF))
        self.mutation, self.result = mutation, result

    def record_call(self, target):
        assert target == CALLEE
        packet, selector, scale, count, zero, mode, channel, context = self.arguments(8)
        assert (packet, selector, scale) == (self.before[29] - 60, self.before[29] - 64, self.before[29] - 68)
        snapshot = (bytes(self.memory[packet + i] for i in range(60)),
                    self.peek(selector, 4), self.peek(scale, 4), count, zero, mode, channel, context)
        self.calls.append((target, *snapshot))
        self.events.append(('CALL', target, snapshot))

    def hook(self, target):
        assert target == CALLEE
        if self.mutation:
            for address in (SOURCE, *GLOBALS, *self.r[4:7]):
                self.put(address, 0xFEDC1234, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.r[2] = self.result


class GameEffectConfigurationPacketMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-effect-configuration-packet-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.retail = list(struct.unpack_from('>69I', (cls.root / 'conker/conker.us.bin').read_bytes(), screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = ('''typedef unsigned char u8;typedef unsigned short u16;typedef short s16;
typedef int s32;typedef unsigned int u32;typedef float f32;
''' + screen.PACKET + '\n' + r'''
f32 D_800A8CC0,D_800A8CC4,D_800A8CC8,D_800A8CCC,D_800A8CD0;
static Position1CBE20 point;
static u32 input[3],anchor[5],scaleBits;
static s32 expectedSelector,expectedContext;
static u8 expectedChannel;
static int calls,error,mutation;
static u32 word(f32 f) {union {f32 f;u32 u;} v;v.f=f;return v.u;}
static f32 number(u32 u) {union {f32 f;u32 u;} v;v.u=u;return v.f;}
void func_15152190(Configuration1CBE20 *p,s32 *selector,f32 *scale,s32 count,f32 zero,u8 mode,u8 channel,s32 context) {
    calls++;
    if(p->count!=10 || p->countRange!=7 || word(p->position.x)!=input[0]
       || word(p->position.y)!=input[1] || word(p->position.z)!=input[2]) error=1;
    if(p->angle || p->angleRange!=255 || p->pitch!=-53 || p->pitchRange!=24
       || word(p->speed)!=0x41200000 || word(p->speedRange)!=0x41000000
       || p->lifetime!=50 || p->lifetimeRange!=20) error=2;
    if(word(p->vertical)!=anchor[0] || word(p->verticalRange)!=anchor[1]
       || word(p->scale)!=anchor[2] || word(p->scaleRange)!=anchor[3]
       || word(p->spread)!=anchor[4]) error=3;
    if(*selector!=expectedSelector || word(*scale)!=scaleBits || count!=1 || word(zero)
       || mode || channel!=expectedChannel || context!=expectedContext) error=4;
    if(scale==&D_800A8CC0 || (void *)scale==(void *)&point) error=5;
    if(mutation) {
        point.x=number(0xFEDC1234);D_800A8CC0=number(0xFEDC1234);
        D_800A8CC4=number(0xFEDC1234);D_800A8CC8=number(0xFEDC1234);
        D_800A8CCC=number(0xFEDC1234);D_800A8CD0=number(0xFEDC1234);
        p->count=0;*selector=-1;*scale=0;
    }
}
''' + screen.SELECTED + '\n')

    def test_direct_body_and_thirty_two_compiler_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['diagnostics']), (69, 0x70, 0, ''))
        self.assertEqual(self.words, self.retail)
        common = ((68, 104, 40), (67, 104, 68), (68, 104, 43), (68, 104, 45))
        expected = {'field-order': common, 'local-order': common, 'wide-selector': common, 'wide-channel': common,
            'selector-first': ((68,104,62),(67,104,67),(68,104,62),(68,104,63)),
            'scalar-position': ((67,104,65),(66,104,68),(67,104,65),(67,104,67)),
            'local-scale': ((69,112,0),(68,112,62),(70,112,35),(70,112,38)),
            'local-scale-first': ((69,112,41),(68,112,29),(70,112,63),(70,112,63))}
        self.assertEqual(len(screen.candidates()), 8)
        for name, body in screen.candidates():
            for i, profile in enumerate(screen.PROFILES):
                record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                self.assertEqual((record['body_words'], record['frame'], record['differences']), expected[name][i])
                self.assertEqual(record['diagnostics'], '')

    def test_complete_packet_arguments_external_traces_and_saved_lifetimes(self):
        cases, coverage = 0, set()
        for pattern, source, selector, channel, context, phase, mutation, result in itertools.product(
            range(3), (SOURCE, GLOBALS[0]), (0, 0xABCDFFFF, 0x12348000), (0, 0x12340080, -1),
            (0, 0x80000000, 0x7FFFFFFF), (0,8), (False,True), (0,0x81234560)):
            memory = memory_case(pattern)
            wanted = dict(memory)
            if mutation:
                for address in (SOURCE, *GLOBALS):
                    put(wanted, address, 0xFEDC1234)
            models = [ConfigurationOracle(words, memory, source, selector, PATTERNS[pattern], channel,
                       context, phase, mutation, result).run() for words in (self.retail, self.words)]
            for model in models:
                self.assertEqual(model.calls, [(CALLEE, packet_bytes(memory, source), selector & 65535,
                    PATTERNS[pattern], 1, 0, 0, channel & 255, context & 0xFFFFFFFF)])
                self.assertEqual(external(model.memory), external(wanted))
                self.assertEqual(model.r[2], result)
                trace = [e for e in model.events if e[0]=='CALL' or not STACK-0x600 <= e[1] < STACK+0x100]
                self.assertEqual(trace, [e for e in models[0].events if e[0]=='CALL' or
                    not STACK-0x600 <= e[1] < STACK+0x100])
            coverage.update(models[0].visits)
            cases += 1
        self.assertEqual(cases, 1296)
        self.assertEqual(coverage, set(range(ENTRY, ENTRY+276, 4)))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases, bodies=2, words=len(coverage)),indent=2)+'\n')

    def test_all_selector_halfwords_channel_bytes_and_raw_float_transport(self):
        memory = memory_case()
        wanted = packet_bytes(memory, SOURCE)
        for value in range(65536):
            scale = PATTERNS[value % len(PATTERNS)]
            model = ConfigurationOracle(self.words, memory, selector=0xABCD0000|value, scale=scale,
                channel=0xFEDC0000|(value&255), context=0x80000000, phase=8*(value&1)).run()
            self.assertEqual(model.calls, [(CALLEE,wanted,value,scale,1,0,0,value&255,0x80000000)])
            self.assertEqual(external(model.memory),external(memory))
        for pattern, scale in itertools.product(range(len(PATTERNS)), PATTERNS):
            memory = memory_case(pattern+1)
            for words in (self.words,self.retail):
                model = ConfigurationOracle(words,memory,scale=scale).run()
                self.assertEqual(model.calls[0][1:4], (packet_bytes(memory,SOURCE),0,scale))

    def test_native_typed_packet_layout_all_halfwords_and_full_source_footprint(self):
        self.run_host(r'''
static u32 patterns[]={0,0x80000000,0x3F800000,0xBF800000,0x7FC12345};
u32 value;int i,m;u8 before[12];Configuration1CBE20 p;
if(sizeof(p)!=60 || sizeof(point)!=12 || sizeof(void *)!=4
   || (u8 *)&p.position-(u8 *)&p!=8 || (u8 *)&p.angle-(u8 *)&p!=20
   || (u8 *)&p.speed-(u8 *)&p!=28 || (u8 *)&p.lifetime-(u8 *)&p!=44
   || (u8 *)&p.scale-(u8 *)&p!=48 || (u8 *)&p.spread-(u8 *)&p!=56) return 1;
for(value=0;value<65536;value++) for(m=0;m<2;m++) {
    for(i=0;i<3;i++) input[i]=patterns[(value+i)%5];
    for(i=0;i<5;i++) anchor[i]=patterns[(value+i+2)%5];
    point.x=number(input[0]);point.y=number(input[1]);point.z=number(input[2]);
    for(i=0;i<12;i++) before[i]=((u8 *)&point)[i];
    D_800A8CC0=number(anchor[0]);D_800A8CC4=number(anchor[1]);D_800A8CC8=number(anchor[2]);
    D_800A8CCC=number(anchor[3]);D_800A8CD0=number(anchor[4]);
    expectedSelector=value;expectedChannel=value&255;expectedContext=value&1?(s32)0x80000000:0x7FFFFFFF;
    scaleBits=patterns[(value+4)%5];calls=error=0;mutation=m;
    func_1519EA78(&point,(u16)value,number(scaleBits),expectedChannel,expectedContext);
    if(calls!=1 || error) return 2;
    for(i=0;i<12;i++) {
        u8 wanted=m && i<4?((u8 *)&(u32){0xFEDC1234})[i]:before[i];
        if(((u8 *)&point)[i]!=wanted) return 3;
    }
    if(word(D_800A8CC0)!=(m?0xFEDC1234:anchor[0]) || word(D_800A8CC4)!=(m?0xFEDC1234:anchor[1])
       || word(D_800A8CC8)!=(m?0xFEDC1234:anchor[2]) || word(D_800A8CCC)!=(m?0xFEDC1234:anchor[3])
       || word(D_800A8CD0)!=(m?0xFEDC1234:anchor[4])) return 4;
}
return 0;
''')

    def test_stub_wrong_constant_selector_width_channel_and_scale_are_detected(self):
        negatives = [('stub','void func_1519EA78(Position1CBE20 *p,u16 s,f32 f,u8 c,s32 x) {}'),
            ('count',screen.SELECTED.replace('packet.count = 10','packet.count = 9')),
            ('selector',screen.SELECTED.replace('selected = selector','selected = (s16)selector')),
            ('channel',screen.SELECTED.replace('0, channel, context','0, channel + 1, context')),
            ('scale',screen.SELECTED.replace('selectedScale = scale','selectedScale = 0.0f'))]
        memory = memory_case()
        wanted = (CALLEE,packet_bytes(memory,SOURCE),65535,0x3F800000,1,0,0,255,0x80000000)
        for name,body in negatives:
            _, words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            model = ConfigurationOracle(words,memory,selector=0xABCDFFFF,scale=0x3F800000,
                        channel=255,context=0x80000000).run()
            self.assertNotEqual(model.calls,[wanted],name)

    def test_production_direct_slot_source_no_guards_and_callee_still_explicit(self):
        functions = load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        self.assertEqual(functions['func_1519EA78'],self.retail)
        source = (self.root/'conker/src/game/generated_1CBE20.c').read_text()
        self.assertIn(screen.PACKET,source)
        self.assertIn(screen.SELECTED,source)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse([r for r in csv.DictReader(stream) if r['function']=='func_1519EA78'])
        helper = (self.root/'conker/src/game/generated_17CAF0.c').read_text()
        self.assertRegex(helper,r's32 func_15152190\(\)\s*\{\s*return 0;\s*\}')
