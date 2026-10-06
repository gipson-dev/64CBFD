"""Post-cleanup gate, allocation publication and stack-packet byte provenance."""

import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_conditional_packet_allocator_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_indexed_state_save_match import external, events
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

BYTE_WRAPPER, DISPATCH, CONSTRUCTOR, BACKEND, ZERO = 0x1519CF70, 0x15147D64, 0x15149130, 0x15167A68, 0x100226F0
OBJECT, RECORD, ALTERNATE = 0x20000, 0x21000, 0x22000
ARGUMENTS = (OBJECT, RECORD, RECORD+0x28, screen.SLOT-0x3B)
RESULTS = (0, RECORD, ALTERNATE, screen.SLOT-0x28)
ALLOC_ARGS = (300, 0xFFFFFFFF, 9, 0, 4, 12, 255, 0)
CTOR_ARGS = (300, 0xFFFFFFFF, 9, 0xFFFFFFFF, 0, 4, 12, 255, 0)


def memory_case(slot, code, pattern, argument):
    memory = {STACK+i: (i*29+pattern*73)&255 for i in range(-0x600, 0x100)}
    for base, size in ((OBJECT, 64), (RECORD, 128), (ALTERNATE, 128), (screen.SLOT-32, 64)):
        memory.update({base+i: (i*17+pattern*83)&255 for i in range(size)})
    put(memory, screen.SLOT, slot)
    # A slot-byte source intentionally changes the initial slot's top byte.
    put(memory, argument+0x3B, code, 1)
    return memory


def changes(stage, mode, argument):
    if not mode:
        return []
    slots = ((0, 0, 0), (RECORD, 0, ALTERNATE), (0, ALTERNATE, 0))[mode-1]
    return [(screen.SLOT, slots[stage], 4), (argument+0x3B, 0xA0+mode*16+stage, 1)]


def snapshot(memory):
    return bytes(value for _, value in sorted(external(memory).items()))


def reference(memory, argument, result, cleanup_mode, allocation_mutation, connected, phase):
    memory, trace, calls = dict(memory), [], []
    residue = 0x81234567
    packet_address = STACK+phase-12
    def read(address, size):
        value = int.from_bytes(bytes(memory[address+i] for i in range(size)), 'big')
        if not STACK-0x600 <= address < STACK+0x100:
            trace.append(('R', address, size, value))
        return value
    def write(address, value, size):
        put(memory, address, value, size)
        if not STACK-0x600 <= address < STACK+0x100:
            trace.append(('W', address, size, value&((1 << (size*8))-1)))
    def call(target, args=(), packet=None):
        calls.append((target, *args, packet, snapshot(memory)))
        trace.append(('CALL', target, *args))
    call(screen.CLEANUP)
    if connected:
        for stage in range(3):
            if stage < 2:
                call(BYTE_WRAPPER, (stage+3,))
            call(DISPATCH, (('private-byte', stage+3), 6) if stage < 2 else (0, 9))
            for address, value, size in changes(stage, cleanup_mode, argument):
                write(address, value, size)
    else:
        for stage in range(3):
            for address, value, size in changes(stage, cleanup_mode, argument):
                write(address, value, size)
    if read(screen.SLOT, 4):
        return external(memory), trace, calls, argument
    write(packet_address+8, 0, 4)
    write(packet_address, argument, 4)
    write(packet_address+4, read(argument+0x3B, 1), 1)
    packet = bytes(memory[packet_address+i] for i in range(12))
    call(screen.ALLOCATOR, ALLOC_ARGS, packet)
    if connected == 2:
        call(CONSTRUCTOR, CTOR_ARGS)
        call(BACKEND, (35, 0, 52, 1, 255, 1))
    if allocation_mutation:
        write(screen.SLOT, ALTERNATE, 4)
        write(argument+0x3B, 0xEE, 1)
    if result and connected == 2:
        for offset, value, size in ((14, 300, 2), (16, 255, 1), (17, 9, 1), (18, 255, 1), (13, 0, 1), (19, 4, 1)):
            write(result+offset, value, size)
        call(ZERO, (result+20, 16))
        for i in range(16):
            write(result+20+i, 0, 1)
    write(screen.SLOT, result, 4)
    if result:
        call(screen.COPY, (result+0x28, 'private-packet', 12), packet)
        for i, byte in enumerate(packet):
            write(result+0x28+i, byte, 1)
        residue = result+0x28
    else:
        residue = 0
    return external(memory), trace, calls, residue


class AllocatorOracle(TriangleOracle):
    def __init__(self, words, memory, argument, result, cleanup_mode=0, allocation_mutation=0,
                 connected=0, phase=0, helpers=None):
        code = {}
        if connected:
            for target in (screen.CLEANUP, BYTE_WRAPPER):
                code.update({target+i*4: word for i, word in enumerate(helpers[target])})
        if connected == 2:
            for target in (screen.ALLOCATOR, CONSTRUCTOR):
                code.update({target+i*4: word for i, word in enumerate(helpers[target])})
        super().__init__(words, memory, entry=screen.ENTRY, arguments=(argument,), phase=phase, connected=code)
        self.argument, self.result = argument, result
        self.cleanup_mode, self.allocation_mutation, self.stage = cleanup_mode, allocation_mutation, 0

    def execute(self, word):
        if word >> 26 == 32:
            rs, rt, immediate = word >> 21 & 31, word >> 16 & 31, word & 65535
            address = (self.r[rs]+(immediate if immediate < 32768 else immediate-65536))&0xFFFFFFFF
            value = self.get(address, 1)
            self.r[rt] = value if value < 128 else value | 0xFFFFFF00
        else:
            super().execute(word)

    def record_call(self, target):
        packet, args = None, ()
        if target == screen.ALLOCATOR:
            args = self.arguments(8)
            pointer = self.before[29]-12
            packet = bytes(self.memory[pointer+i] for i in range(12))
        elif target == CONSTRUCTOR:
            args = self.arguments(9)
        elif target == BACKEND:
            args = self.arguments(6)
        elif target == BYTE_WRAPPER:
            args = (self.r[4],)
        elif target == DISPATCH:
            pointer, command = self.arguments(2)
            args = (('private-byte', self.peek(pointer, 1)), command) if command == 6 else (pointer, command)
        elif target == ZERO:
            args = self.arguments(2)
        elif target == screen.COPY:
            destination, pointer, size = self.arguments(3)
            assert pointer == self.before[29]-12 and size == 12
            args = (destination, 'private-packet', size)
            packet = bytes(self.memory[pointer+i] for i in range(12))
        else:
            assert target == screen.CLEANUP
        self.calls.append((target, *args, packet, snapshot(self.memory)))
        self.events.append(('CALL', target, *args))

    def hook(self, target):
        value = 0x81234567
        if target in (screen.CLEANUP, DISPATCH):
            for stage in (range(3) if target == screen.CLEANUP else (self.stage,)):
                for address, word, size in changes(stage, self.cleanup_mode, self.argument):
                    self.put(address, word, size)
            self.stage += 1
        elif target in (screen.ALLOCATOR, BACKEND):
            if self.allocation_mutation:
                self.put(screen.SLOT, ALTERNATE, 4)
                self.put(self.argument+0x3B, 0xEE, 1)
            value = self.result
        elif target == ZERO:
            destination, size = self.arguments(2)
            for i in range(size):
                self.put(destination+i, 0, 1)
        else:
            assert target == screen.COPY
            destination, source, size = self.arguments(3)
            for i in range(size):
                self.put(destination+i, self.get(source+i, 1), 1)
            value = destination
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.r[2] = value
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameConditionalPacketAllocatorMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-conditional-packet-allocator-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>38I', rom, screen.ROM))
        cls.helpers = {target: list(struct.unpack_from('>%dI'%count, rom, offset)) for target, count, offset in (
            (screen.CLEANUP, 13, 0x1CBB38), (BYTE_WRAPPER, 12, 0x1CA420),
            (screen.ALLOCATOR, 28, 0x1766A4), (CONSTRUCTOR, 49, 0x1765E0))}
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        owner = (cls.root / 'conker/src/game/generated_1CA420.c').read_text()
        helpers = '\n'.join(re.search(r'void '+name+r'\([^;{}]+\) \{.*?\n\}', owner, re.S).group()
                            for name in ('func_1519CF70', 'func_1519E688'))
        cls.fixture = '''typedef unsigned char u8;typedef signed char s8;typedef short s16;
typedef int s32;typedef unsigned int u32;typedef struct {u8 b[128];} struct260;
#define NULL ((void *)0)
''' + screen.PACKET + r'''
static struct260 records[2];static u8 object[64],expected[2][128],expectedObject[64];
u8 *D_800E0920;
static u8 *wantedSlot,*allocationResult;static int mode,mutate,calls,error;
static u8 expectedCode;static void *expectedObjectPointer;
static int events[8],count;
void func_15147D64(void *p,u8 command) {
    int stage=count++;events[stage]=command==6?*(u8 *)p:9;
    if((stage<2 && (command!=6 || *(u8 *)p!=stage+3)) || (stage==2 && (p || command!=9))) error=1;
    if(mode) {
        u8 *slots[3][3]={{NULL,NULL,NULL},{(u8 *)&records[0],NULL,(u8 *)&records[1]},
                        {NULL,(u8 *)&records[1],NULL}};
        D_800E0920=slots[mode-1][stage];object[0x3B]=(u8)(0xA0+mode*16+stage);
    }
}
''' + helpers + r'''
struct260 *func_151491F4(s16 a,s8 b,s8 c,u8 d,u8 e,s32 f,u8 g,s32 h) {
    calls++;if(a!=300 || b!=-1 || c!=9 || d || e!=4 || f!=12 || g!=255 || h) error=2;
    if(mutate) {D_800E0920=(u8 *)&records[1];object[0x3B]=0xEE;}
    return (struct260 *)allocationResult;
}
void *memcpy(void *d,const void *s,u32 n) {
    const Packet1CA420 *p=s;u8 *out=d;const u8 *in=s;u32 i;
    if(n!=12 || d!=allocationResult+0x28 || p->object!=expectedObjectPointer || p->code!=expectedCode || p->reserved) error=3;
    if(D_800E0920!=allocationResult) error=4;
    /* Padding is intentionally unspecified natively; compare its transport, not a value. */
    for(i=0;i<n;i++) out[i]=in[i];
    for(i=0;i<n;i++) if(out[i]!=in[i]) error=5;
    return d;
}
''' + screen.SELECTED + '\n'

    def test_direct_body_and_twenty_four_compiler_controls(self):
        self.assertEqual(self.words, self.retail)
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (38, 56, 0))
        expected = {'reserved-first': ((38,56,0),(37,56,35),(40,56,32),(39,56,37)),
                    'field-order': ((38,56,6),(37,56,35),(40,56,32),(39,56,37)),
                    'allocation-local': ((36,56,32),(35,56,35),(39,56,31),(38,56,29)),
                    'unused-local': ((38,64,8),(37,64,36),(40,56,32),(39,56,37)),
                    'early-return': ((38,56,0),(37,56,35),(40,56,32),(39,56,37)),
                    'explicit-copy-size': ((38,56,0),(37,56,35),(40,56,32),(39,56,37))}
        for name, body in screen.candidates():
            for i, profile in enumerate(screen.PROFILES):
                record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                self.assertEqual((record['body_words'], record['frame'], record['differences']), expected[name][i])
                self.assertEqual(record['diagnostics'], '')

    def test_opaque_connected_cleanup_and_allocator_order_padding_and_aliases(self):
        for connected in range(3):
            cases, coverage = 0, set()
            for slot, code, argument, result, mode, mutation, phase in itertools.product(
                    (0, RECORD, 0xFFFFFFFF), (0, 127, 128, 255), ARGUMENTS, RESULTS, range(4), (0, 1), (0, 8)):
                memory = memory_case(slot, code, cases%3, argument)
                wanted = reference(memory, argument, result, mode, mutation, connected, phase)
                for words in (self.retail, self.words):
                    model = AllocatorOracle(words, memory, argument, result, mode, mutation, connected, phase, self.helpers).run()
                    self.assertEqual((external(model.memory), events(model), model.calls, model.r[2]), wanted)
                    coverage.update(model.visits)
                cases += 1
            self.assertEqual(cases, 3072)
            wanted_words = set(range(screen.ENTRY, screen.ENTRY+152, 4))
            if connected:
                wanted_words.update(range(screen.CLEANUP, screen.CLEANUP+52, 4))
                wanted_words.update(range(BYTE_WRAPPER, BYTE_WRAPPER+48, 4))
            if connected == 2:
                wanted_words.update(range(screen.ALLOCATOR, screen.ALLOCATOR+112, 4))
                wanted_words.update(range(CONSTRUCTOR, CONSTRUCTOR+196, 4))
                wanted_words.difference_update((CONSTRUCTOR+0x34, CONSTRUCTOR+0x38))
            self.assertEqual(coverage, wanted_words)
            (self.output / ('mode%d.json'%connected)).write_text(json.dumps(dict(cases=cases, models=2,
                reachable_words=len(coverage), packet_padding_bytes=3), indent=2)+'\n')

    def test_all_code_bytes_and_three_padding_patterns(self):
        for code, pattern, phase in itertools.product(range(256), range(3), (0, 8)):
            memory = memory_case(0, code, pattern, OBJECT)
            wanted = reference(memory, OBJECT, RECORD, 0, 0, 2, phase)
            model = AllocatorOracle(self.words, memory, OBJECT, RECORD, connected=2, phase=phase, helpers=self.helpers).run()
            self.assertEqual((external(model.memory), events(model), model.calls, model.r[2]), wanted)

    def test_native_actual_cleanup_and_wrapper_initialized_fields_and_footprints(self):
        self.run_host(r'''
int slot,code,m,r,k,i,j,n=0;Packet1CA420 layout;
if(sizeof(void *)!=4 || sizeof(layout)!=12 || (u8 *)&layout.code-(u8 *)&layout!=4
   || (u8 *)&layout.reserved-(u8 *)&layout!=8) return 1;
for(slot=0;slot<3;slot++) for(code=0;code<256;code++) for(m=0;m<4;m++) for(r=0;r<3;r++) for(k=0;k<2;k++) {
    for(i=0;i<2;i++) for(j=0;j<128;j++) records[i].b[j]=expected[i][j]=(u8)(j*17+code);
    for(i=0;i<64;i++) object[i]=expectedObject[i]=(u8)(i*29+code);
    object[0x3B]=expectedObject[0x3B]=(u8)code;
    D_800E0920=slot?(u8 *)&records[slot-1]:NULL;mode=m;mutate=k;count=calls=error=0;
    allocationResult=r?(u8 *)&records[r-1]:NULL;
    wantedSlot=m==1 || m==3?NULL:m==2?(u8 *)&records[1]:D_800E0920;
    expectedCode=m?(u8)(0xA0+m*16+2):(u8)code;expectedObjectPointer=object;
    if(m) expectedObject[0x3B]=expectedCode;
    if(!wantedSlot) {
        wantedSlot=allocationResult;
        if(k) expectedObject[0x3B]=0xEE;
        if(r) {
            *(void **)(expected[r-1]+0x28)=object;expected[r-1][0x2C]=expectedCode;
            *(s32 *)(expected[r-1]+0x30)=0;
        }
    }
    func_1519E6BC(object);
    if(error || count!=3 || events[0]!=3 || events[1]!=4 || events[2]!=9 || D_800E0920!=wantedSlot) return 2;
    if(calls!=((m==1 || m==3 || (!m && !slot))?1:0)) return 3;
    for(i=0;i<64;i++) if(object[i]!=expectedObject[i]) return 4;
    for(i=0;i<2;i++) for(j=0;j<128;j++) {
        if(calls && r && i==r-1 && j>=0x2D && j<0x30) continue;
        if(records[i].b[j]!=expected[i][j]) return 5;
    }
    n++;
}
if(n!=18432) return 6;
''')

    def test_wrong_gate_capture_publication_size_and_zero_padding_are_detected(self):
        forms = {'stub': 'void func_1519E6BC(u8 *p) {}',
                 'early-gate': screen.SELECTED.replace('    func_1519E688();\n', '').replace(
                     '    if (D_800E0920 == NULL) {', '    if (D_800E0920 == NULL) {\n        func_1519E688();'),
                 'early-code': screen.SELECTED.replace('    Packet1CA420 packet;', '    Packet1CA420 packet;\n    u8 code = arg0[0x3B];').replace('packet.code = arg0[0x3B];', 'packet.code = code;'),
                 'copy-size': screen.SELECTED.replace('sizeof(packet)', '8'),
                 'late-publish': screen.SELECTED.replace('    Packet1CA420 packet;', '    Packet1CA420 packet;\n    u8 *result;').replace(
                     'D_800E0920 = (u8 *)', 'result = (u8 *)').replace('if (D_800E0920 != NULL)', 'if (result != NULL)').replace(
                     'memcpy(D_800E0920 +', 'memcpy(result +').replace('            memcpy(', '            D_800E0920 = result;\n            memcpy('),
                 'zero-padding': screen.SELECTED.replace('        packet.reserved = 0;', '        ((u8 *)&packet)[5] = 0;\n        ((u8 *)&packet)[6] = 0;\n        ((u8 *)&packet)[7] = 0;\n        packet.reserved = 0;')}
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root, self.output, 'wrong-'+name, body)
            different = False
            for slot, result, mode in ((RECORD, RECORD, 3), (0, 0, 0), (0, RECORD, 1)):
                memory = memory_case(slot, 127, 1, OBJECT)
                wanted = reference(memory, OBJECT, result, mode, 1, 0, 0)
                try:
                    model = AllocatorOracle(words, memory, OBJECT, result, mode, 1).run()
                    different |= (external(model.memory), events(model), model.calls, model.r[2]) != wanted
                except (AssertionError, KeyError):
                    different = True
            self.assertTrue(different, name)

    def test_production_direct_slot_and_unchanged_complete_helpers(self):
        linked, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1519E6BC'], screen.ENTRY)
        self.assertEqual(linked['func_1519E6BC'], self.retail)
        for target, words in self.helpers.items():
            self.assertEqual(linked['func_%08X'%target], words)
        source = (self.root / 'conker/src/game/generated_1CA420.c').read_text()
        self.assertIn(screen.PACKET, source)
        self.assertIn(screen.SELECTED, source)
        self.assertNotIn('func_1519E6BC', (self.root / 'conker/retail_word_patches.us.csv').read_text())


if __name__ == '__main__':
    unittest.main()
