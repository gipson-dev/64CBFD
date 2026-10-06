"""Bound the source effect packet, its opaque handoff, and retained consumer."""

import csv
import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_source_effect_packet_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

SOURCE, EFFECT, TABLE = 0x20000, 0x21000, screen.TABLE
HOLES = (6, 7, 0x4D, 0x4E, 0x4F)
ARGUMENTS = ((0, 0, 0), (1, 1, 1), (0xABCD7FFF, 0xFEDC8000, 0x12340080),
             (0xABCD8000, 0xFEDC7FFF, 0x123400FF), (0xABCDFFFF, 0xFEDCFFFF, 0x12340100),
             (0xFFFFFFFF, 0x80000000, 0xFFFFFFFF), (0x1234ABCD, 0x76543210, 0xABCDEFEE), (206, -53, 255))


def external(memory):
    return {a: v for a, v in memory.items() if not STACK-0x600 <= a < STACK+0x100}


def memory_case(pattern=0, padding=0xA5):
    memory = {STACK+i: padding for i in range(-0x600, 0x100)}
    for base in (SOURCE-0x180, EFFECT-16):
        memory.update({base+i: (i*17+13) & 255 for i in range(0x380)})
    memory.update({TABLE+i: 0xA5 for i in range(-16, 48)})
    values = ((1.25, -2.5, 4.0, 6.0, -8.0, 12.0, 100.0, -160.0),
              (-0.0, 0.0, -20.0, -6.0, 8.0, -12.0, -0.0, 0.0),
              (17.0, 31.0, -13.0, 0.0, -0.0, 1.0, 0.125, -0.25))[pattern]
    for i, value in enumerate(values):
        put(memory, SOURCE+i*4, bits(value))
    return memory


def word(memory, address):
    return int.from_bytes(bytes(memory[address+i] for i in range(4)), 'big')


def packet_bytes(memory, mode, lifetime, padding):
    packet = bytearray([padding]*88)
    def store(offset, value, size=4):
        packet[offset:offset+size] = (value & ((1 << (8*size))-1)).to_bytes(size, 'big')
    for offset, value in ((0, mode), (1, 0), (0x10, 255), (0x11, 255), (0x12, 255), (0x13, 255),
                          (0x44, 255), (0x45, 255), (0x46, 0), (0x47, 7), (0x4C, 255)):
        store(offset, value, 1)
    for offset, value in ((2, 0x3B03), (4, lifetime), (0x54, 1), (0x56, 255)):
        store(offset, value, 2)
    for offset, value in ((8, 0), (12, 0), (0x34, 0x3F800000), (0x38, 0x3F800000),
                          (0x3C, 0x3F800000), (0x40, 0x045C0081), (0x48, 0), (0x50, 0)):
        store(offset, value)
    for offset, source_offset in ((0x14, 0x18), (0x18, 0x1C)):
        store(offset, bits(floating(word(memory, SOURCE+source_offset))*10.0))
    packet[0x1C:0x34] = bytes(memory[SOURCE+i] for i in range(24))
    return bytes(packet)


class EffectPacketOracle(TriangleOracle):
    def __init__(self, words, memory, mode=0, lifetime=0, channel=0, context=0, phase=0,
                 result=EFFECT, mutation=False, connected=None):
        super().__init__(words, memory, entry=screen.ENTRY, phase=phase, connected=connected,
            arguments=(SOURCE, mode & 0xFFFFFFFF, lifetime & 0xFFFFFFFF, channel & 0xFFFFFFFF, context & 0xFFFFFFFF))
        self.result, self.mutation = result, mutation

    def record_call(self, target):
        if target == screen.CONSTRUCTOR:
            args = self.arguments(12)
            assert args[0] == self.before[29]-88
            snapshot = bytes(self.memory[args[0]+i] for i in range(88))
            call = (target, snapshot, *args[1:])
        else:
            assert target == screen.COPY
            destination, source, size = self.r[4:7]
            assert source == self.before[29]-92 and size == 4
            call = (target, destination, self.peek(source, 4), size)
        self.calls.append(call)
        self.events.append(('CALL', target, call[1:]))

    def hook(self, target):
        if target == screen.CONSTRUCTOR:
            if self.mutation:
                for address in (SOURCE, TABLE, self.r[4]+0x40):
                    self.put(address, 0x12345678, 4)
            result = self.result
        else:
            assert target == screen.COPY
            destination, source, size = self.r[4:7]
            for i in range(size):
                self.put(destination+i, self.get(source+i, 1), 1)
            result = destination
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]
        self.r[2] = result


class GameSourceEffectPacketMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-source-effect-packet-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.base_record, cls.baseline = screen.compile_candidate(cls.root, cls.output, 'field-order', screen.BASELINE)
        rom = (cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>96I', rom, screen.ROM))
        cls.production = load_elf_functions(str(cls.root/'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = ('''typedef unsigned char u8;typedef short s16;typedef unsigned short u16;
typedef int s32;typedef unsigned int u32;typedef float f32;
#define NULL ((void *)0)
''' + screen.LAYOUTS+'\n'+r'''
s32 D_800A4AA0;
static union {u32 align;u8 bytes[0x230];} storage;
static Source1CBE20 source;
static u32 sourceWords[8];
static s32 expectedContext;static u8 expectedMode,expectedChannel;static s16 expectedLifetime;
static int calls,copies,error,fail,mutation;
static u32 word(f32 f) {union {f32 f;u32 u;} v;v.f=f;return v.u;}
static f32 number(u32 u) {union {f32 f;u32 u;} v;v.u=u;return v.f;}
void *func_1513D2F0(void *data,s32 table,u8 kind,u8 a,u8 b,u8 c,u8 d,
                  s32 e,s32 f,s32 size,u8 channel,s32 context) {
    SourceEffect1CBE20 *p=data;calls++;
    if(table!=(s32)&D_800A4AA0 || kind!=39 || a || b || c!=23 || d || e!=3 || f!=255
       || size!=4 || channel!=expectedChannel || context!=expectedContext) error=1;
    if(p->mode!=expectedMode || p->field01 || p->field02!=0x3B03 || p->lifetime!=expectedLifetime
       || p->field08 || p->field0C || p->field10!=255 || p->field11!=255 || p->field12!=255 || p->field13!=255) error=2;
    if(word(p->width)!=word(number(sourceWords[6])*10.0f) || word(p->height)!=word(number(sourceWords[7])*10.0f)
       || word(p->position.x)!=sourceWords[0] || word(p->position.y)!=sourceWords[1] || word(p->position.z)!=sourceWords[2]
       || word(p->vector.x)!=sourceWords[3] || word(p->vector.y)!=sourceWords[4] || word(p->vector.z)!=sourceWords[5]) error=3;
    if(p->field34!=1 || p->field38!=1 || p->field3C!=1 || p->flags!=0x045C0081
       || p->field44!=255 || p->field45!=255 || p->field46 || p->field47!=7 || p->field48
       || p->field4C!=255 || p->field50 || p->field54!=1 || p->field56!=255) error=4;
    if(mutation) {source.position.x=number(0x12345678);D_800A4AA0=0x12345678;p->flags=0;}
    return fail?NULL:storage.bytes+16;
}
void *memcpy(void *destination,const void *input,u32 size) {
    const u8 *p=input;u32 i;copies++;
    if(destination!=storage.bytes+16+0x110 || size!=4 || *(Source1CBE20 *const *)input!=&source) error=5;
    for(i=0;i<size;i++) ((u8 *)destination)[i]=p[i];
    return destination;
}
''' + screen.SELECTED+'\n')

    def test_direct_body_fifty_two_profile_and_forty_six_order_controls(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['diagnostics']), (96, 0xA0, 0, ''))
        self.assertEqual(self.words, self.retail)
        expected = {
            'field-order': ((96,160,16),(94,160,94),(101,152,98),(101,152,98)),
            'header-order': ((96,160,0),(94,160,94),(102,152,99),(102,152,100)),
            'narrow-mode': ((96,160,16),(95,160,94),(101,152,98),(101,152,98)),
            'wide-lifetime': ((96,160,16),(93,160,91),(101,152,98),(101,152,98)),
            'wide-channel': ((96,160,17),(94,160,94),(101,152,98),(101,152,98)),
            'mode-first': ((97,160,66),(95,160,93),(101,152,98),(101,152,98)),
            'unit-first': ((96,160,57),(94,160,79),(101,152,100),(101,152,100)),
            'vector-copy': ((97,160,77),(95,160,94),(102,152,102),(102,152,102)),
            'position-copy': ((97,160,77),(95,160,94),(104,152,103),(104,152,103)),
            'captured-factor': ((96,168,50),(94,168,95),(101,160,95),(101,160,95)),
            'captured-unit': ((96,168,50),(94,168,95),(100,160,99),(100,160,99)),
            'dimensions-first': ((96,160,71),(94,160,91),(101,152,101),(101,152,101)),
            'pointer-first': ((96,160,43),(94,160,94),(101,152,98),(101,152,98))}
        self.assertEqual(len(screen.candidates()), 13)
        for name, body in screen.candidates():
            for index, profile in enumerate(screen.PROFILES):
                record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                self.assertEqual((record['body_words'], record['frame'], record['differences']), expected[name][index], (name,profile))
                self.assertEqual(record['diagnostics'], '')
        order_expected = [(97,66),(97,66),(97,70),(97,70),(97,70),(96,16),(97,72),(96,18),(96,16),(96,16),(96,30)]
        order_expected += [(97,68),(97,68),(97,70),(97,70),(97,70),(96,16),(97,72),(96,18),(96,16),(96,16),(96,30)]
        order_expected += [(97,72)]*3+[(96,18),(96,16),(96,18),(96,19),(96,20)]
        order_expected += [(96,n) for n in (25,23,22,20,19,18,16,18)]
        order_expected += [(97,73)]*3+[(96,n) for n in (21,20,19,18,16)]
        self.assertEqual(len(list(screen.ordering_candidates())), 46)
        for (name, body), wanted in zip(screen.ordering_candidates(), order_expected):
            record, _ = screen.compile_candidate(self.root, self.output, name, body)
            self.assertEqual((record['body_words'], record['differences']), wanted, name)
            self.assertEqual((record['frame'], record['diagnostics']), (160, ''))

    def test_guest_full_packet_padding_calls_aliases_traces_and_saved_lifetimes(self):
        cases, coverage = 0, set()
        for args, context, phase, padding, mutation, result, pattern in itertools.product(ARGUMENTS,
            (0,-1,0x80000000,0x7FFFFFFF),(0,8),(0,0xA5,0x5A),(False,True),(0,EFFECT,SOURCE-0x110),range(3)):
            mode, lifetime, channel = args
            memory = memory_case(pattern, padding)
            wanted = dict(memory)
            calls = [(screen.CONSTRUCTOR,packet_bytes(memory,mode,lifetime,padding),TABLE,39,0,0,23,0,3,255,4,
                      channel & 255,context & 0xFFFFFFFF)]
            if mutation:
                for address in (SOURCE,TABLE):
                    put(wanted,address,0x12345678)
            if result:
                calls.append((screen.COPY,result+0x110,SOURCE,4));put(wanted,result+0x110,SOURCE)
            traces = []
            for words in (self.baseline,self.words,self.retail):
                model = EffectPacketOracle(words,memory,mode,lifetime,channel,context,phase,result,mutation).run()
                self.assertEqual(model.calls,calls)
                self.assertEqual(external(model.memory),external(wanted))
                self.assertEqual(model.r[2],result+0x110 if result else 0)
                traces.append([e for e in model.events if e[0]=='CALL' or not STACK-0x600<=e[1]<STACK+0x100])
                if words is self.retail:
                    coverage.update(model.visits)
            self.assertEqual(traces[0],traces[1]);self.assertEqual(traces[1],traces[2])
            cases += 1
        self.assertEqual(cases,3456)
        self.assertEqual(coverage,set(range(screen.ENTRY,screen.ENTRY+384,4)))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases,bodies=3,words=len(coverage),holes=list(HOLES)),indent=2)+'\n')

    def test_all_halfwords_and_every_mode_channel_byte_with_high_incoming_bits(self):
        memory = memory_case()
        for value in range(65536):
            model = EffectPacketOracle(self.words,memory,mode=0xABCD0000 | value,lifetime=0xFEDC0000 | value,
                channel=0x12340000 | (value >> 8),context=0x80000000,phase=8*(value & 1)).run()
            self.assertEqual(model.calls,[(screen.CONSTRUCTOR,packet_bytes(memory,value,value,0xA5),TABLE,39,0,0,23,0,3,255,4,
                value >> 8,0x80000000),(screen.COPY,EFFECT+0x110,SOURCE,4)])
            wanted = dict(memory);put(wanted,EFFECT+0x110,SOURCE)
            self.assertEqual(external(model.memory),external(wanted))

    def test_float_dimension_boundaries_and_raw_coordinate_transport(self):
        sizes = (0,0x80000000,1,0x007FFFFF,0x00800000,0x3F800001,0x7F7FFFFF,0xFF7FFFFF)
        transported = (0x7FA12345,0x7FC54321,0x7F800000,0xFF800000,0x80000000,1,0x7F7FFFFF,0)
        cases = 0
        for width,height,phase in itertools.product(sizes,sizes,(0,8)):
            memory = memory_case()
            put(memory,SOURCE+24,width);put(memory,SOURCE+28,height)
            for i in range(6):
                put(memory,SOURCE+i*4,transported[(sizes.index(width)+i)%8])
            wanted = packet_bytes(memory,206,-53,0xA5)
            for words in (self.baseline,self.words,self.retail):
                model = EffectPacketOracle(words,memory,206,-53,255,0,phase).run()
                self.assertEqual(model.calls[0],(screen.CONSTRUCTOR,wanted,TABLE,39,0,0,23,0,3,255,4,255,0))
            cases += 1
        self.assertEqual(cases,128)

    def test_recovered_constructor_retail_slot_and_actual_connected_handoff(self):
        from tools.tests.test_game_source_effect_constructor_match import connected_wrapper_cases
        rom = (self.root/'conker/conker.us.bin').read_bytes()
        constructor = self.production['func_1513D2F0']
        self.assertEqual(constructor,list(struct.unpack_from('>114I',rom,0x16A7A0)))
        connected_wrapper_cases(self,self.words,constructor)

    def test_native_typed_layout_all_halfwords_byte_pairs_and_whole_footprint(self):
        self.run_host(r'''
u32 value;int f,i;u8 before[32];SourceEffect1CBE20 p;
if(sizeof(source)!=32 || sizeof(p)!=88 || sizeof(void *)!=4 || (u8 *)&p.lifetime-(u8 *)&p!=4
   || (u8 *)&p.width-(u8 *)&p!=20 || (u8 *)&p.position-(u8 *)&p!=28 || (u8 *)&p.vector-(u8 *)&p!=40
   || (u8 *)&p.flags-(u8 *)&p!=64 || (u8 *)&p.field50-(u8 *)&p!=80 || (u8 *)&p.field56-(u8 *)&p!=86) return 1;
for(value=0;value<65536;value++) for(f=0;f<2;f++) {
    for(i=0;i<8;i++) sourceWords[i]=word((f32)(i+1)*(value & 1?-2:3));
    for(i=0;i<32;i++) ((u8 *)&source)[i]=((u8 *)sourceWords)[i];
    for(i=0;i<32;i++) before[i]=((u8 *)&source)[i];
    for(i=0;i<0x230;i++) storage.bytes[i]=0xA5;
    expectedMode=value & 255;expectedLifetime=(s16)value;expectedChannel=value >> 8;
    expectedContext=value & 1?(s32)0x80000000:0x7FFFFFFF;
    D_800A4AA0=-123;fail=f;mutation=value & 1;calls=copies=error=0;
    func_1519ED84(&source,(s32)(0xABCD0000 | value),expectedLifetime,expectedChannel,expectedContext);
    if(calls!=1 || copies!=!f || error || D_800A4AA0!=(mutation?0x12345678:-123)) return 2;
    for(i=0;i<0x230;i++) {
        u8 expected=!f && i>=16+0x110 && i<16+0x114?((u8 *)&(Source1CBE20 *){&source})[i-16-0x110]:0xA5;
        if(storage.bytes[i]!=expected) return 3;
    }
    for(i=0;i<32;i++) {
        u8 expected=mutation && i<4?((u8 *)&(u32){0x12345678})[i]:before[i];
        if(((u8 *)&source)[i]!=expected) return 4;
    }
}
return 0;
''')

    def test_native_actual_source_consumer_after_pointer_publication(self):
        original = self.fixture
        source = (self.root/'conker/src/game/generated_1CBE20.c').read_text()
        consumer = re.search(r's32 func_1519EF04\([^;{}]+\) \{\n.*?\n\}',source,re.S).group(0)
        self.fixture += '\n'+consumer+'\n'
        try:
            self.run_host(r'''
int pattern,mode,life,channel,i,j;u8 expected[0x230];
for(pattern=0;pattern<4;pattern++) for(mode=0;mode<3;mode++) for(life=0;life<4;life++) for(channel=0;channel<4;channel++) {
    for(i=0;i<8;i++) sourceWords[i]=word((f32)(pattern+1)*(i+1)*(pattern & 1?-2:3));
    for(i=0;i<32;i++) ((u8 *)&source)[i]=((u8 *)sourceWords)[i];
    for(i=0;i<0x230;i++) storage.bytes[i]=expected[i]=0xA5;
    expectedMode=mode==0?0:mode==1?206:255;
    expectedLifetime=life==0?-32768:life==1?-1:life==2?0:32767;expectedChannel=channel*85;
    expectedContext=-123;D_800A4AA0=-7;fail=0;mutation=pattern & 1;calls=copies=error=0;
    func_1519ED84(&source,expectedMode,expectedLifetime,expectedChannel,expectedContext);
    if(error || calls!=1 || copies!=1) return 1;
    for(i=0;i<4;i++) expected[16+0x110+i]=((u8 *)&(Source1CBE20 *){&source})[i];
    source.position.x=number(0x80000000);source.vector.y=-35.0f;
    source.width=-0.125f;source.height=7.5f;
    if(func_1519EF04(storage.bytes+16)!=1) return 2;
    for(i=0;i<8;i++) {
        int offset=i==0?0x2C:i==1?0x30:i<5?0x34+(i-2)*4:0x40+(i-5)*4;
        f32 value=i==0?source.width*10.0f:i==1?source.height*10.0f:i==2?source.position.x:i==3?source.position.y:
                  i==4?source.position.z:i==5?source.vector.x:i==6?source.vector.y:source.vector.z;
        for(j=0;j<4;j++) expected[16+offset+j]=((u8 *)&value)[j];
    }
    for(i=0;i<0x230;i++) if(storage.bytes[i]!=expected[i]) return 3;
}
return 0;
''')
        finally:
            self.fixture = original

    def test_stub_wrong_flags_size_payload_channel_and_padding_are_detected(self):
        negatives = [('stub','void func_1519ED84(Source1CBE20 *s,s32 m,s16 l,u8 c,s32 x) {}'),
            ('flags',screen.SELECTED.replace('packet.flags = 0x045C0081','packet.flags = 0')),
            ('size',screen.SELECTED.replace('255, 4, channel','255, 0, channel')),
            ('pointer',screen.SELECTED.replace('&savedSource, sizeof(savedSource)','savedSource, sizeof(savedSource)')),
            ('channel',screen.SELECTED.replace('4, channel, context','4, channel + 1, context')),
            ('padding',screen.SELECTED.replace('    packet.field50 = 0;','    packet.field50 = 0;\n    packet.pad4D[0] = 0;'))]
        memory = memory_case()
        wanted = [(screen.CONSTRUCTOR,packet_bytes(memory,206,-53,0xA5),TABLE,39,0,0,23,0,3,255,4,255,0),
                  (screen.COPY,EFFECT+0x110,SOURCE,4)]
        for name,body in negatives:
            _,words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            try:
                model = EffectPacketOracle(words,memory,206,-53,255).run()
            except AssertionError:
                continue
            self.assertNotEqual(model.calls,wanted,name)

    def test_production_complete_direct_slot_source_no_guards_and_retained_consumer(self):
        self.assertEqual(self.production['func_1519ED84'],self.retail)
        source = (self.root/'conker/src/game/generated_1CBE20.c').read_text()
        self.assertIn(screen.SELECTED,source)
        self.assertIn(screen.LAYOUTS.split('typedef struct {\n    u8 mode;',1)[1],source)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        self.assertFalse([r for r in rows if r['function']=='func_1519ED84'])
        self.assertEqual(len(rows),10760)
        rom = (self.root/'conker/conker.us.bin').read_bytes()
        self.assertEqual(self.production['func_1519EF04'],list(struct.unpack_from('>27I',rom,0x1CC3B4)))
