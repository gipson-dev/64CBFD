"""Seven-argument narrowing, actual allocator/list linking and ordered record stores."""

import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_address_record_allocator_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_indexed_state_save_match import external, events
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

HEAP, INSERT, TABLE = 0x10003C6C, 0x15168A4C, 0x800DCE50
SOURCE, RECORD, ALTERNATE, HEAD = 0x20000, 0x21000, 0x22000, 0x23000
CONTEXTS = (0, 1, 0xFFFFFFFF, 0x80000000, 0x7FFFFFFF, 0x12345601)
LIFETIMES = (0, 1, 0x7FFF, 0x8000, 0xFFFF, 0xABCD8001, 0xFFFFFFFF, 0x80000000)
POINTERS = ((SOURCE, SOURCE+4, SOURCE+8), (0, 0, 0), (HEAD, RECORD, ALTERNATE),
            (0xFFFFFFFF, 0x80000000, 0x12345678), (SOURCE+8, SOURCE+4, SOURCE),
            (RECORD+16, RECORD+16, RECORD+16), (1, 3, 0xFFFFFFFC), (SOURCE, SOURCE, SOURCE))


def slot(context):
    return TABLE+(context&255)*0x1A0+38*4


def memory_case(context, head, pattern):
    memory = {STACK+i: 0xA5 for i in range(-0x600, 0x100)}
    for base, size in ((SOURCE, 64), (RECORD, 128), (ALTERNATE, 128), (HEAD, 128), (slot(context)-8, 20)):
        memory.update({base+i: (i*17+pattern*83)&255 for i in range(size)})
    put(memory, slot(context), head)
    return memory


def mutation_writes(context, result, mutation):
    if not mutation:
        return []
    return [(SOURCE, 0xE7, 1), (slot(context), HEAD, 4)] + (
        [(result+0x10, 0xDEADBEEF, 4), (result+0x28, 0xEE, 1)] if result else [])


def snapshot(memory):
    return bytes(v for _, v in sorted(external(memory).items()))


def reference(memory, arguments, result, mutation, connected):
    memory, trace, calls = dict(memory), [], []
    lifetime, owner, mode, first, second, channel, context = arguments
    def read(address, size):
        value = int.from_bytes(bytes(memory[address+i] for i in range(size)), 'big')
        trace.append(('R', address, size, value))
        return value
    def write(address, value, size):
        put(memory, address, value, size)
        trace.append(('W', address, size, value&((1 << (size*8))-1)))
    def call(target, args):
        calls.append((target, *args, snapshot(memory)))
        trace.append(('CALL', target, *args))
    call(screen.ALLOCATOR, (38, context, 44, 1, channel&255, 1))
    if connected:
        call(HEAP, (44, 1, 1, 0, 1))
    for address, value, size in mutation_writes(context, result, mutation):
        write(address, value, size)
    if not result:
        return external(memory), trace, calls, 0
    if connected:
        write(result+1, context, 1)
        call(INSERT, (result, 38))
        location = TABLE+read(result+1, 1)*0x1A0+38*4
        head = read(location, 4)
        write(result+8, head, 4)
        if head:
            write(head+4, result, 4)
        write(result, 38, 1)
        write(result+4, 0, 4)
        write(location, result, 4)
        write(result+12, channel, 1)
    for offset, value, size in ((24, first, 4), (28, second, 4), (32, lifetime, 2),
                               (40, mode, 1), (16, 1, 4), (20, 0, 4), (36, owner, 4)):
        write(result+offset, value, size)
    return external(memory), trace, calls, result


class RecordOracle(TriangleOracle):
    def __init__(self, words, memory, arguments, result, mutation=0, connected=0, phase=0, allocator=(), insert=()):
        code = {screen.ALLOCATOR+i*4: word for i, word in enumerate(allocator if connected else ())}
        code.update({INSERT+i*4: word for i, word in enumerate(insert if connected == 2 else ())})
        super().__init__(words, memory, entry=screen.ENTRY, arguments=arguments, phase=phase, connected=code)
        self.context, self.result, self.mutation = arguments[6], result, mutation

    def record_call(self, target):
        assert target in (screen.ALLOCATOR, HEAP, INSERT)
        args = self.arguments(6 if target == screen.ALLOCATOR else 5 if target == HEAP else 2)
        self.calls.append((target, *args, snapshot(self.memory)))
        self.events.append(('CALL', target, *args))

    def hook(self, target):
        if target == INSERT:
            node, kind = self.arguments(2)
            row = self.get(node+1, 1)
            location = TABLE+row*0x1A0+kind*4
            head = self.get(location, 4)
            self.put(node+8, head, 4)
            if head:
                self.put(head+4, node, 4)
            self.put(node, kind, 1)
            self.put(node+4, 0, 4)
            self.put(location, node, 4)
            value = 0x81234567
        else:
            assert target in (screen.ALLOCATOR, HEAP)
            for address, word, size in mutation_writes(self.context, self.result, self.mutation):
                self.put(address, word, size)
            value = self.result
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.r[2] = value
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameAddressRecordAllocatorMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-address-record-allocator-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>37I', rom, screen.ROM))
        cls.allocator = list(struct.unpack_from('>28I', rom, 0x194F18))
        cls.insert = list(struct.unpack_from('>20I', rom, 0x195EFC))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        source = (cls.root / 'conker/src/game_1944C0.c').read_text()
        list_node = re.search(r'typedef struct ListNode \{.*?\n\} ListNode;', source, re.S).group()
        allocator = re.search(r'void \*func_15167A68\([^;{}]+\) \{.*?\n\}', source, re.S).group()
        insert = re.search(r'void func_15168A4C\([^;{}]+\) \{.*?\n\}', source, re.S).group()
        cls.fixture = '''typedef unsigned char u8;typedef short s16;typedef int s32;typedef unsigned int u32;
#define NULL ((void *)0)
''' + screen.RECORD + '\n' + list_node + r'''
static u32 records[2][32],oldHead[32],table[208];static u8 source[64];
static u32 expectedRecords[2][32],expectedHead[32],expectedTable[208];static u8 expectedSource[64];
#define D_800DCE50 ((u8 *)table)
static u8 *allocationResult;static s32 contextValue;static int mutation,calls,error;
void func_15168A4C(void *,s32);
s32 func_10003C6C(s32 size,s32 mode,s32 policy,s32 zero,s32 pool) {
    u8 *p=allocationResult;
    calls++;if(size!=44 || mode!=1 || policy!=1 || zero || pool!=1) error=1;
    if(mutation) {
        source[0]=0xE7;*(void **)(D_800DCE50+(contextValue&255)*416+152)=oldHead;
        if(p) {*(u32 *)(p+16)=0xDEADBEEF;p[40]=0xEE;}
    }
    return (s32)p;
}
''' + allocator.replace('ret = func_10003C6C(', 'ret = (u8 *)func_10003C6C(') + '\n' + insert + '\n' + screen.SELECTED + '\n'

    def compare(self, memory, arguments, result, mutation=0, connected=0, phase=0):
        wanted = reference(memory, arguments, result, mutation, connected)
        coverage = set()
        for words in (self.retail, self.words):
            model = RecordOracle(words, memory, arguments, result, mutation, connected, phase, self.allocator, self.insert).run()
            self.assertEqual((external(model.memory), events(model), model.calls, model.r[2]), wanted)
            coverage.update(model.visits)
        return coverage

    def test_direct_body_and_forty_eight_compiler_controls(self):
        self.assertEqual(self.words, self.retail)
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (37, 32, 0))
        expected = {'early-null': ((37,32,6),(37,32,16),(46,40,38),(46,40,42)),
                    'nested-success': ((35,32,20),(35,32,30),(43,40,35),(43,40,39)),
                    'flags-first': ((37,32,14),(37,32,24),(46,40,38),(46,40,42)),
                    'wide-lifetime': ((37,32,7),(37,32,17),(46,40,38),(46,40,42)),
                    'wide-mode': ((37,32,7),(37,32,17),(46,40,38),(46,40,42)),
                    'wide-channel': ((37,32,7),(37,32,16),(46,40,38),(46,40,42)),
                    'explicit-size': ((37,32,6),(37,32,16),(46,40,38),(46,40,42)),
                    'register-result': ((37,32,6),(37,32,16),(40,48,40),(40,48,38)),
                    'owner-before-flags': ((37,32,0),(37,32,10),(46,40,38),(46,40,42)),
                    'byte-view-mode': ((37,32,6),(37,32,16),(46,40,38),(46,40,42)),
                    'owner-first-byte-view': ((37,32,0),(37,32,10),(46,40,38),(46,40,42)),
                    'raw-fields': ((37,32,6),(37,32,16),(46,40,38),(46,40,42))}
        for name, body in screen.candidates():
            for i, profile in enumerate(screen.PROFILES):
                record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                self.assertEqual((record['body_words'], record['frame'], record['differences']), expected[name][i])
                self.assertEqual(record['diagnostics'], '')

    def test_opaque_connected_allocator_and_actual_list_linking_full_traces(self):
        for connected in range(3):
            cases, coverage = 0, set()
            for pattern, context, result, head, mutation, phase in itertools.product(
                    range(8), CONTEXTS, (0, RECORD), (0, HEAD, RECORD), (0, 1), (0, 8)):
                owner, first, second = POINTERS[pattern]
                arguments = (LIFETIMES[pattern], owner, (0xFEDC0000+pattern*37)&0xFFFFFFFF,
                             first, second, (0xABCDFF00+pattern*53)&0xFFFFFFFF, context)
                coverage.update(self.compare(memory_case(context, head, pattern), arguments, result, mutation, connected, phase))
                cases += 1
            self.assertEqual(cases, 1152)
            wanted = set(range(screen.ENTRY, screen.ENTRY+148, 4))
            if connected:
                wanted.update(range(screen.ALLOCATOR, screen.ALLOCATOR+112, 4))
            if connected == 2:
                wanted.update(range(INSERT, INSERT+80, 4))
            self.assertEqual(coverage, wanted)
            (self.output / ('mode%d.json'%connected)).write_text(json.dumps(dict(cases=cases, models=2,
                reachable_words=len(coverage), all_words_reachable=True), indent=2)+'\n')

    def test_all_halfwords_and_all_mode_channel_byte_pairs_with_high_bits(self):
        for value in range(65536):
            context, phase = value>>7&1, 8 if value&0x8000 else 0
            owner, first, second = POINTERS[value%8]
            arguments = (0xABCD0000|value, owner, 0xFEDC0000|(value&255), first, second,
                         0x12340000|(value>>8), context)
            memory = memory_case(context, HEAD if value&4 else 0, value%3)
            wanted = reference(memory, arguments, RECORD, value&1, 2)
            model = RecordOracle(self.words, memory, arguments, RECORD, value&1, 2, phase, self.allocator, self.insert).run()
            self.assertEqual((external(model.memory), events(model), model.calls, model.r[2]), wanted)
        (self.output / 'width-sweep.json').write_text(json.dumps(dict(cases=65536, models=1,
            all_halfwords=True, all_mode_channel_pairs=True), indent=2)+'\n')

    def test_native_actual_wrapper_allocator_and_list_insert_full_footprints(self):
        self.run_host(r'''
int value,failed,head,m,i,j,n=0;AddressRecord1CBE20 layout;
if(sizeof(void *)!=4 || sizeof(layout)!=44 || (u8 *)&layout.flags-(u8 *)&layout!=16
 || (u8 *)&layout.first-(u8 *)&layout!=24 || (u8 *)&layout.lifetime-(u8 *)&layout!=32
 || (u8 *)&layout.owner-(u8 *)&layout!=36 || (u8 *)&layout.mode-(u8 *)&layout!=40 || sizeof(ListNode)!=12) return 1;
for(value=0;value<65536;value++) for(failed=0;failed<2;failed++) {
    s32 life=(s32)(0xABCD0000U|(u32)value);u8 mode=(u8)value,channel=(u8)(value>>8);
    u8 *owner=(value&8)?source:NULL,*first=(value&16)?source+8:source+16,*second=(value&32)?first:source+24;
    u8 *p=(u8 *)records[0],*copy=(u8 *)expectedRecords[0],*old=(u8 *)oldHead;
    void *current;AddressRecord1CBE20 *result;
    contextValue=(value&128)?(s32)0x80000001:(s32)0x12345600;
    head=value%3;mutation=m=value&1;
    for(i=0;i<2;i++) for(j=0;j<128;j++) ((u8 *)records[i])[j]=(u8)(j*17+value);
    for(i=0;i<128;i++) ((u8 *)oldHead)[i]=(u8)(i*29+value);
    for(i=0;i<832;i++) ((u8 *)table)[i]=0xA5;
    for(i=0;i<64;i++) source[i]=(u8)(i*31+value);
    current=head==0?NULL:head==1?(void *)old:(void *)p;
    *(void **)(D_800DCE50+(contextValue&255)*416+152)=current;
    for(i=0;i<2;i++) for(j=0;j<128;j++) ((u8 *)expectedRecords[i])[j]=((u8 *)records[i])[j];
    for(i=0;i<128;i++) ((u8 *)expectedHead)[i]=((u8 *)oldHead)[i];
    for(i=0;i<832;i++) ((u8 *)expectedTable)[i]=((u8 *)table)[i];
    for(i=0;i<64;i++) expectedSource[i]=source[i];
    allocationResult=failed?NULL:p;calls=error=0;
    if(m) {
        expectedSource[0]=0xE7;current=old;
        *(void **)((u8 *)expectedTable+(contextValue&255)*416+152)=old;
        if(!failed) {*(u32 *)(copy+16)=0xDEADBEEF;copy[40]=0xEE;}
    }
    if(!failed) {
        copy[1]=(u8)contextValue;*(void **)(copy+8)=current;
        if(current==old) *(void **)((u8 *)expectedHead+4)=p;
        if(current==p) *(void **)(copy+4)=p;
        copy[0]=38;*(void **)(copy+4)=NULL;
        *(void **)((u8 *)expectedTable+(contextValue&255)*416+152)=p;copy[12]=channel;
        *(void **)(copy+24)=first;*(void **)(copy+28)=second;*(s16 *)(copy+32)=(s16)life;
        copy[40]=mode;*(u32 *)(copy+16)=1;*(s32 *)(copy+20)=0;*(void **)(copy+36)=owner;
    }
    result=func_1519E970((s16)life,owner,mode,first,second,channel,contextValue);
    if(error || calls!=1 || result!=(AddressRecord1CBE20 *)allocationResult) return 2;
    for(i=0;i<2;i++) for(j=0;j<128;j++) if(((u8 *)records[i])[j]!=((u8 *)expectedRecords[i])[j]) return 3;
    for(i=0;i<128;i++) if(((u8 *)oldHead)[i]!=((u8 *)expectedHead)[i]) return 4;
    for(i=0;i<832;i++) if(((u8 *)table)[i]!=((u8 *)expectedTable)[i]) return 5;
    for(i=0;i<64;i++) if(source[i]!=expectedSource[i]) return 6;
    n++;
}
if(n!=131072) return 7;
''')

    def test_stub_wrong_size_flags_pointer_and_narrowing_are_detected(self):
        forms = {'stub': 'AddressRecord1CBE20 *func_1519E970(s16 a,u8 *b,u8 c,u8 *d,u8 *e,u8 f,s32 g) {return NULL;}',
                 'size': screen.SELECTED.replace('sizeof(AddressRecord1CBE20)', '0x28'),
                 'flags': screen.SELECTED.replace('record->flags = 1;', 'record->flags = 0;'),
                 'pointer': screen.SELECTED.replace('record->second = second;', 'record->second = first;'),
                 'lifetime': screen.SELECTED.replace('record->lifetime = lifetime;', 'record->lifetime = lifetime + 1;'),
                 'channel': screen.SELECTED.replace(', 1, channel, 1)', ', 1, channel + 1, 1)')}
        arguments = (0xABCD8001, SOURCE, 0xFEDC0080, SOURCE+4, SOURCE+8, 0x123400FF, 0)
        memory = memory_case(0, HEAD, 1)
        wanted = reference(memory, arguments, RECORD, 1, 2)
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root, self.output, 'wrong-'+name, body)
            model = RecordOracle(words, memory, arguments, RECORD, 1, 2, allocator=self.allocator, insert=self.insert).run()
            self.assertNotEqual((external(model.memory), events(model), model.calls, model.r[2]), wanted, name)

    def test_production_direct_slot_retained_helpers_and_no_guards(self):
        linked, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1519E970'], screen.ENTRY)
        self.assertEqual(linked['func_1519E970'], self.retail)
        self.assertEqual(linked['func_15167A68'], self.allocator)
        self.assertEqual(linked['func_15168A4C'], self.insert)
        source = (self.root / 'conker/src/game/generated_1CBE20.c').read_text()
        self.assertIn(screen.RECORD, source)
        self.assertIn(screen.SELECTED, source)
        self.assertNotIn('func_1519E970', (self.root / 'conker/retail_word_patches.us.csv').read_text())


if __name__ == '__main__':
    unittest.main()
