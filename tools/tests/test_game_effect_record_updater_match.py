"""Live effect refresh, private request bytes and bounded constructor/link calls."""

import csv
import hashlib
import itertools
import json
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_effect_record_updater_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests.test_game_payload_copy_wrapper_match import SignedByteOracle, read, external
from tools.tests.test_game_actor_triangle_transform_match import put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly

TABLE, SEARCH, ALLOC, COPY, LINK = (screen.SYMBOLS[name] for name in
    ('D_8008A0B4', 'func_1514ECE0', 'func_15149130', 'memcpy', 'func_1514EC1C'))
ACTOR, NODES, RECORDS, CREATED, ALT_ACTOR = 0x21000, 0x25000, 0x26000, 0x27000, 0x22000
COUNTS = (0, 1, 0x7FFF, 0x8000, 0xFFFF, 0x10000, 0x10001, 0x80000000, 0x7FFFFFFF, 0xFFFFFFFF)


def native_fixture():
    return r'''
typedef unsigned char u8; typedef signed char s8; typedef short s16;
typedef int s32; typedef unsigned int u32;
typedef struct { u8 unused; } struct37;
typedef struct { s32 unk0,unk4; } struct32;
#define NULL ((void *)0)
static struct32 D_8008A0B4[21],wanted_table[21];
static union { u32 alignment; u8 bytes[0x1600]; } store;
static u8 wanted[0x1600];
#define arena store.bytes
static u8 *actor=arena+16,*nodes=arena+0x500,*records=arena+0x700,*created;
static int mode,fail,index,sequence,call_count,copy_count;
typedef struct { u32 kind,args[9]; u8 prefix[9]; } Call;
static Call calls[16],wanted_calls[16];
static int wanted_call_count,wanted_copy_count;
static u32 get32(u8 *p) { return *(u32 *)p; }
static void set32(u8 *p,u32 value) { *(u32 *)p=value; }
static u8 *pointer(u8 *p) { return *(u8 **)p; }
static Call *call(u32 kind) {
    Call *result=&calls[call_count++];int i;
    result->kind=kind;
    for(i=0;i<9;i++) { result->args[i]=0;result->prefix[i]=0; }
    return result;
}
s32 func_1514ECE0(u8 *node,s16 key,u8 **out) {
    Call *receipt=call(10);receipt->args[0]=(u32)node;receipt->args[1]=(u32)(s32)key;
    sequence++;
    if(mode&1) D_8008A0B4[index].unk4=(s32)((u32)D_8008A0B4[index].unk4+0x10003U);
    if(mode&2) actor[0x3B]=(u8)(0xE7+sequence*7);
    if((mode&4) && sequence==1 && node) *(u8 **)(node+0x14)=nodes+0x60;
    while(node && *(s16 *)(node+0x1C)!=key) node=pointer(node+0x14);
    *out=node;
    return node!=NULL;
}
u8 *func_15149130(s16 first,s8 a,s8 b,s8 c,u8 flag,u8 duration,struct37 *size,u8 slot,s32 context) {
    Call *receipt=call(20);
    receipt->args[0]=(u32)(s32)first;receipt->args[1]=(u32)(s32)a;receipt->args[2]=(u32)(s32)b;
    receipt->args[3]=(u32)(s32)c;receipt->args[4]=flag;receipt->args[5]=duration;
    receipt->args[6]=(u32)size;receipt->args[7]=slot;receipt->args[8]=(u32)context;
    if(mode&8) { actor[0x3B]=0x11;D_8008A0B4[index].unk4=(s32)0x87654321U; }
    return fail?NULL:created;
}
void *memcpy(void *destination,const void *source,u32 length) {
    Call *receipt=call(30);u32 i;
    receipt->args[0]=(u32)destination;receipt->args[1]=length;
    for(i=0;i<9;i++) receipt->prefix[i]=((const u8 *)source)[i];
    for(i=0;i<length;i++) ((u8 *)destination)[i]=((const u8 *)source)[i];
    copy_count++;
    return destination;
}
s32 func_1514EC1C(s32 record,s32 owner,s32 key) {
    Call *receipt=call(40);u8 *object=(u8 *)owner;
    receipt->args[0]=(u32)record;receipt->args[1]=(u32)owner;receipt->args[2]=(u32)key;
    set32(object+0x3F0,get32(object+0x3F0)+1U);
    return -1;
}
static void initialize(int idx,u32 count,int shape,int failed,int mutation,int alias) {
    int i;index=idx;fail=failed;mode=mutation;sequence=call_count=copy_count=0;
    for(i=0;i<(int)sizeof(arena);i++) arena[i]=(u8)(i*13+7);
    for(i=0;i<21;i++) { D_8008A0B4[i].unk0=0x1A100000+i*4;D_8008A0B4[i].unk4=(s32)(i==index?count:0xBEEF0000U+(u32)i); }
    set32(actor+0x3F0,0);actor[0x3B]=0xE7;*(u8 **)(actor+0x2F4)=shape?nodes:NULL;
    for(i=0;i<4;i++) {
        u8 *node=nodes+i*0x20,*record=shape==7?records:records+i*0x40;
        int match=(shape==2 && i==0)||(shape==3 && i==3)||shape==4||shape==7||(shape==5 && (i==0 || i==2));
        *(u8 **)(node+0x10)=record;*(u8 **)(node+0x14)=i<3?node+0x20:NULL;
        *(s16 *)(node+0x1C)=(shape==6 || (shape==5 && i%2))?0x13:0x1A;
        set32(record+0x28,(u32)(match?index:index^1));*(s16 *)(record+0xE)=(s16)(0x8001+i);
    }
    created=alias==0?arena+0xA00:alias==1?actor+0x100:records;
}
static void reference_native(void) {
    u8 *node=pointer(actor+0x2F4);int found=0;
    while(func_1514ECE0(node,0x1A,&node)) {
        u8 *record=pointer(node+0x10);
        if(get32(record+0x28)==(u32)index) { *(s16 *)(record+0xE)=(s16)D_8008A0B4[index].unk4;found=1; }
        node=pointer(node+0x14);
    }
    if(!found) {
        union { u32 alignment; u8 bytes[12]; } packet;
        u8 *result;
        set32(packet.bytes,(u32)index);*(u8 **)(packet.bytes+4)=actor;packet.bytes[8]=actor[0x3B];
        result=func_15149130((s16)D_8008A0B4[index].unk4,-1,-1,-1,1,50,(struct37 *)12,255,1);
        if(result) { memcpy(result+0x28,packet.bytes,12);func_1514EC1C((s32)result,(s32)actor,0x1A); }
    }
}
static void remember(void) {
    int i;wanted_call_count=call_count;wanted_copy_count=copy_count;
    for(i=0;i<(int)sizeof(arena);i++) wanted[i]=arena[i];
    for(i=0;i<21;i++) wanted_table[i]=D_8008A0B4[i];
    for(i=0;i<call_count;i++) wanted_calls[i]=calls[i];
}
static int compare(void) {
    int i,j;u32 unknown=(u32)created+0x31;
    if(call_count!=wanted_call_count || copy_count!=wanted_copy_count) return 1;
    for(i=0;i<call_count;i++) {
        if(calls[i].kind!=wanted_calls[i].kind) return 2;
        for(j=0;j<9;j++) if(calls[i].args[j]!=wanted_calls[i].args[j] || calls[i].prefix[j]!=wanted_calls[i].prefix[j]) return 3;
    }
    for(i=0;i<(int)sizeof(arena);i++) {
        u32 address=(u32)(arena+i);
        if(copy_count && address>=unknown && address<unknown+3) continue;
        if(arena[i]!=wanted[i]) return 4;
    }
    for(i=0;i<21;i++) if(D_8008A0B4[i].unk0!=wanted_table[i].unk0 || D_8008A0B4[i].unk4!=wanted_table[i].unk4) return 5;
    return 0;
}
'''+screen.LOCAL_DECLARATIONS+screen.SELECTED+'\n'


def signed16(value):
    return (value&65535 if value&65535 < 32768 else (value&65535)-65536)&0xFFFFFFFF


def count_address(index):
    return (TABLE+index*8+4)&0xFFFFFFFF


def memory_case(index=0, count=1, shape=0, poison=0, output_alias=0):
    memory = {STACK+i: ((i*17+0xA5)&255 if poison else 0xA5) for i in range(-0x600, 0x100)}
    for base, size in ((ACTOR-16, 0x440), (ALT_ACTOR-16, 0x440), (NODES-16, 0x120),
                       (RECORDS-16, 0x120), (CREATED-16, 0x100), (TABLE-16, 21*8+32)):
        memory.update({base+i: (i*13+7)&255 for i in range(size)})
    for i in range(21):
        put(memory, TABLE+i*8, 0x1A100000+i*4); put(memory, TABLE+i*8+4, count if i==index else 0xBEEF0000+i)
    for actor in (ACTOR, ALT_ACTOR): put(memory, actor+0x3F0, 0)
    put(memory, ACTOR+0x2F4, 0 if shape==0 else NODES); put(memory, ACTOR+0x3B, 0xE7, 1)
    for i in range(4):
        node, record = NODES+i*0x20, RECORDS+i*0x40
        if shape==7: record = RECORDS
        put(memory, node+0x10, record); put(memory, node+0x14, node+0x20 if i<3 else 0)
        put(memory, node+0x1C, 0x13 if shape==6 or shape==5 and i%2 else 0x1A, 2)
        match = shape==2 and i==0 or shape==3 and i==3 or shape in (4, 7) or shape==5 and i in (0, 2)
        put(memory, record+0x28, index if match else index^1)
        put(memory, record+0xE, 0x8001+i, 2)
    destination = (CREATED, ACTOR+0x100, RECORDS)[output_alias]
    return memory, destination


def search_reference(memory, node, index, mode, sequence):
    if mode&1: put(memory, count_address(index), (read(memory, count_address(index))+0x10003)&0xFFFFFFFF)
    if mode&2: put(memory, ACTOR+0x3B, (0xE7+sequence*7)&255, 1)
    if mode&4 and sequence==1 and node: put(memory, node+0x14, NODES+0x60)
    for _ in range(8):
        if not node or read(memory, node+0x1C, 2)==0x1A: return node
        node = read(memory, node+0x14)
    raise AssertionError('search reference budget')


def reference(memory, index, destination, fail=0, mode=0):
    memory = dict(memory); calls = []; node = read(memory, ACTOR+0x2F4); matched = 0; sequence = 0
    for _ in range(8):
        sequence += 1; calls.append((SEARCH, node, 0x1A))
        node = search_reference(memory, node, index, mode, sequence)
        if not node: break
        record = read(memory, node+0x10)
        if read(memory, record+0x28)==index:
            matched = node; put(memory, record+0xE, read(memory, count_address(index)), 2)
        node = read(memory, node+0x14)
    else: raise AssertionError('updater reference budget')
    unknown = set()
    if not matched:
        prefix = index.to_bytes(4, 'big')+ACTOR.to_bytes(4, 'big')+bytes((read(memory, ACTOR+0x3B, 1),))
        calls.append((ALLOC, signed16(read(memory, count_address(index))), 0xFFFFFFFF, 0xFFFFFFFF,
            0xFFFFFFFF, 1, 50, 12, 255, 1))
        if mode&8:
            put(memory, ACTOR+0x3B, 0x11, 1); put(memory, count_address(index), 0x87654321)
        if not fail:
            calls.append((COPY, destination+0x28, prefix, 12))
            for i, value in enumerate(prefix): put(memory, destination+0x28+i, value, 1)
            unknown = set(range(destination+0x31, destination+0x34))
            actor = ALT_ACTOR if mode&16 else ACTOR
            calls.append((LINK, destination, actor, 0x1A))
            put(memory, actor+0x3F0, read(memory, actor+0x3F0)+1)
    return external(memory), calls, unknown


class UpdaterOracle(SignedByteOracle):
    def __init__(self, words, memory, index, destination, fail=0, mode=0, phase=0, connected=None, bind=True,
                 entry=screen.ENTRY, arguments=None):
        super().__init__(words, memory, entry=entry, arguments=(ACTOR, index) if arguments is None else arguments,
            phase=phase, connected=connected)
        self.index, self.destination, self.fail, self.mode = index, destination, fail, mode
        self.sequence, self.cursor_reads, self.copies = 0, [], []
        self.initial_sp, self.bind = self.before[29], bind

    def execute(self, word):
        position = len(self.events)
        super().execute(word)
        if self.bind and word==0x8FA40058 and self.code.get(screen.ENTRY+0x8C)==word:
            self.assert_cursor(position)

    def assert_cursor(self, position):
        event = self.events[position]
        assert event == ('R', self.initial_sp-8, 4, self.r[12]), ('cursor reload', event, self.r[12])
        self.cursor_reads.append(position)

    def record_call(self, target):
        if target==screen.ENTRY:
            self.initial_sp = self.r[29]
            call = (target, *self.arguments(2))
        elif target==SEARCH:
            node, key, result = self.arguments(3); self.sequence += 1
            assert key==0x1A
            if self.bind: assert result==self.initial_sp-8
            else: assert self.initial_sp-0x600 <= result < self.initial_sp
            call = (target, node, key)
        elif target==ALLOC: call = (target, *self.arguments(9))
        elif target==COPY:
            destination, source, size = self.arguments(3)
            payload = bytes(self.memory[source+i] for i in range(size))
            self.copies.append((source, payload)); call = (target, destination, payload[:9], size)
        else:
            assert target==LINK, ('invalid target', target)
            call = (target, *self.arguments(3))
        self.calls.append(call); self.events.append(('CALL', target, call[1:]))

    def hook(self, target):
        if target==SEARCH:
            node, _, result = self.arguments(3)
            before = dict(self.memory)
            node = search_reference(before, node, self.index, self.mode, self.sequence)
            for address, value in before.items():
                if self.memory[address]!=value: self.put(address, value, 1)
            self.put(result, node, 4); returned = int(node!=0)
        elif target==ALLOC:
            if self.mode&8:
                self.put(ACTOR+0x3B, 0x11, 1); self.put(count_address(self.index), 0x87654321, 4)
            returned = 0 if self.fail else self.destination
        elif target==COPY:
            destination, source, size = self.arguments(3)
            copied = bytes(self.get(source+i, 1) for i in range(size))
            for i, value in enumerate(copied): self.put(destination+i, value, 1)
            if self.mode&16: self.put(self.initial_sp, ALT_ACTOR, 4)
            returned = 0xBAD00000
        else:
            assert target==LINK
            record, actor, key = self.arguments(3)
            assert record==self.destination and key==0x1A
            self.put(actor+0x3F0, self.get(actor+0x3F0, 4)+1, 4); returned = 0xBAD00000
        for register in (1, 2, 3, *range(4, 16), 24, 25): self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]; self.r[2] = returned


class GameEffectRecordUpdaterMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-effect-record-updater-test'; cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.normalized = screen.normalize(cls.raw)
        cls.rom = (cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>80I', cls.rom, screen.ROM))
        cls.search = {SEARCH+i*4: word for i, word in enumerate(struct.unpack_from('>23I', cls.rom, 0x17C190))}
        cls.directory = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def models(self, memory, index, destination, fail=0, mode=0, phase=0, connected=None):
        wanted, calls, unknown = reference(memory, index, destination, fail, mode); models = []
        for words in (self.raw, self.normalized, self.retail):
            model = UpdaterOracle(words, memory, index, destination, fail, mode, phase, connected).run()
            self.assertEqual(model.calls, calls)
            self.assertEqual({a: v for a, v in external(model.memory).items() if a not in unknown},
                             {a: v for a, v in wanted.items() if a not in unknown})
            if model.copies:
                source, payload = model.copies[0]
                expected_offset = 0x44 if words is self.raw else 0x40
                self.assertEqual(source, model.initial_sp-0x60+expected_offset)
                self.assertEqual(payload[9:], bytes(memory[source+i] for i in range(9, 12)))
                before_copy = model.events[:next(i for i, event in enumerate(model.events) if event[0]=='CALL' and event[1]==COPY)]
                self.assertFalse([event for event in before_copy if event[0]=='W' and
                    any(event[1]<=source+i<event[1]+event[2] for i in range(9, 12))])
            models.append(model)
        self.assertEqual(models[1].events, models[2].events)
        self.assertEqual(models[1].memory, models[2].memory)
        return models

    def test_controls_complete_closed_derivation_and_actual_padding(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'], self.record['diagnostics']), (80, 96, 24, ''))
        self.assertEqual(self.normalized, self.retail)
        records = []
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                record, _ = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                records.append(record); self.assertEqual(record['diagnostics'], '')
        (self.output/'controls.json').write_text(json.dumps(records, indent=2)+'\n')
        _, _, relocations = parse_object(self.output/'selected.o')
        guards = screen.guard_rows(self.raw, relocations); self.assertEqual(len(guards), 24)
        self.assertTrue(all(row['omit']=='false' and not row['insert_after'] for row in guards))
        csv_path = self.output/'guards.csv'
        with csv_path.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(guards[0])); writer.writeheader(); writer.writerows(guards)
        layout = self.output/'layout.csv'
        layout.write_text('version,section,filename,function,address,end\nus,game,game_16EE20,func_15141E38,0x15141E38,0x15141F78\n')
        assembly = emit_padded_assembly(self.output/'selected.o', layout, 'game_16EE20', word_patches_path=csv_path)
        (self.output/'padded.s').write_text(assembly)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(self.output/'padded.o'), str(self.output/'padded.s')], check=True, capture_output=True)
        _, symbols, mapped = parse_object(self.output/'padded.o')
        self.assertEqual(symbols[screen.FUNCTION]['size'], 320); self.assertEqual(mapped, relocations)
        for table in (TABLE, 0x90018004):
            elf = self.output/('padded-%X.elf'%table); values = dict(screen.SYMBOLS, D_8008A0B4=table)
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output/'updater.ld'), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X'%item for item in values.items()], '-o', str(elf), str(self.output/'padded.o')], check=True, capture_output=True)
            words = list(struct.unpack_from('>80I', screen.sections(elf)['.text'][1]))
            if table==TABLE: self.assertEqual(words, self.retail)
            for hi, lo in ((0x44, 0x48), (0x98, 0xA0)):
                self.assertEqual(words[hi//4]&65535, ((table+0x8000)>>16)&65535)
                self.assertEqual(words[lo//4]&65535, table&65535)
        stale = self.output/'stale.csv'; damaged = list(guards); damaged[0] = dict(damaged[0], expected='0x00000000')
        with stale.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(guards[0])); writer.writeheader(); writer.writerows(damaged)
        with self.assertRaisesRegex(ValueError, 'expected|mismatch'):
            emit_padded_assembly(self.output/'selected.o', layout, 'game_16EE20', word_patches_path=stale)

    def test_guest_refresh_every_matching_record_live_counts_and_constructor_paths(self):
        cases, reloads = 0, 0; coverage = [set(), set(), set()]
        for index, count, shape, fail, mode, phase in itertools.product((0, 5, 19, 20), COUNTS, range(8), (0, 1), (0, 1, 2, 4, 8, 15), (0, 8)):
            memory, destination = memory_case(index, count, shape, cases%2)
            models = self.models(memory, index, destination, fail, mode, phase)
            for i, model in enumerate(models): coverage[i].update(model.visits)
            reloads += len(models[0].cursor_reads); cases += 1
        self.assertEqual(cases, 7680)
        self.assertEqual([len(visits) for visits in coverage], [80, 80, 80])
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases, bodies=3,
            covered_words=[80, 80, 80], bound_cursor_reads=reloads,
            raw_unknown_copy_bytes=3, normalized_full_trace=True), indent=2)+'\n')

    def test_connected_original_search_and_aliased_destination_storage(self):
        # Real search does not contain the model's mutation hook; mutate allocation only here.
        cases = 0
        for index, count, shape, fail, mode, alias, phase in itertools.product((0, 19, 20), (0x8000, 0x10001, 0xFFFFFFFF), range(8), (0, 1), (0, 8), range(3), (0, 8)):
            memory, destination = memory_case(index, count, shape, cases%2, alias)
            self.models(memory, index, destination, fail, mode, phase, self.search); cases += 1
        self.assertEqual(cases, 1728)
        (self.output/'search.json').write_text(json.dumps(dict(cases=cases, bodies=3, search_words=23,
            output_aliases=3), indent=2)+'\n')

    def test_guest_home_reload_after_copy_and_nonuniform_unknown_padding(self):
        cases = 0; padding_differences = 0
        for index, count, mode, phase in itertools.product((0, 19, 20), (0, 0x8000, 0x10001), (16, 24), (0, 8)):
            memory, destination = memory_case(index, count, 0, 1)
            models = self.models(memory, index, destination, 0, mode, phase)
            self.assertEqual(models[0].calls[-1], (LINK, destination, ALT_ACTOR, 0x1A))
            self.assertNotEqual(models[0].copies[0][1][9:], models[2].copies[0][1][9:]); padding_differences += 1; cases += 1
        self.assertEqual((cases, padding_differences), (36, 36))
        (self.output/'private.json').write_text(json.dumps(dict(guest_actor_home_cases=cases,
            raw_vs_retail_padding_differences=padding_differences, normalized_padding_exact=True,
            native_actor_home_alias_claim=False), indent=2)+'\n')

    def test_native_actual_source_live_refresh_allocation_failure_and_known_storage(self):
        self.fixture = native_fixture()
        self.run_host('u32 counts[]={'+','.join(str(value)+'U' for value in COUNTS)+r'''};
int indices[]={0,5,19,20},modes[]={0,1,8,15};
int i,c,shape,failed,mutation,alias,cases=0;
if(sizeof(void *)!=4 || sizeof(GameEffectRefreshRequest)!=12 || sizeof(struct32)!=8) return 70;
if(__builtin_offsetof(GameEffectRefreshRequest,index)!=0 || __builtin_offsetof(GameEffectRefreshRequest,actor)!=4
   || __builtin_offsetof(GameEffectRefreshRequest,identity)!=8) return 71;
for(i=0;i<4;i++) for(c=0;c<10;c++) for(shape=0;shape<8;shape++) for(failed=0;failed<2;failed++)
for(mutation=0;mutation<4;mutation++) for(alias=0;alias<3;alias++) {
    initialize(indices[i],counts[c],shape,failed,modes[mutation],alias);reference_native();remember();
    initialize(indices[i],counts[c],shape,failed,modes[mutation],alias);func_15141E38(actor,indices[i]);
    if(compare()) return 72;
    cases++;
}
if(cases!=7680) return 73;
''')
        (self.output/'native.json').write_text(json.dumps(dict(cases=7680, pointer_bytes=4,
            known_request_bytes=9, indeterminate_tail_bytes=3, full_other_storage=True,
            actor_home_alias_claim=False, scalar_return=False), indent=2)+'\n')

    def test_guest_full_width_selectors_and_no_new_index_range_gate(self):
        cases = 0
        for index, selector, mode in itertools.product((0, 5, 19, 20), (0x10000, 0x80000000, 0xFFFF0000), (0, 1)):
            memory, destination = memory_case(index, 0xFFFFFFFF, 4)
            for i in range(4): put(memory, RECORDS+i*0x40+0x28, selector|index)
            self.models(memory, index, destination, 0, mode); cases += 1
        # Bounded guest-only invalid-array indices: native C cannot claim valid out-of-array access.
        for index in (-1, 21):
            memory, destination = memory_case(0, 1, 0)
            put(memory, TABLE+index*8+4, 0x1234FFFF)
            self.models(memory, index&0xFFFFFFFF, destination); cases += 1
        self.assertEqual(cases, 26)

    def test_connected_original_checked_caller_and_actual_native_wrapper(self):
        caller = list(struct.unpack_from('>37I', self.rom, 0x16F254)); entry = 0x15141DA4
        gate, classifiers = 0x800BE616, 0x8008A084
        cases = 0
        for category, selected, disabled, count, classifier, callback, shape, failed, phase in itertools.product(
            (0xFFFFFFFF, 0, 11, 12), (0xFFFFFFFF, 0, 19, 20), (0, 1), (0xFFFFFFFF, 0, 1),
            (0, 1), (0, 1), (0, 4), (0, 1), (0, 8)):
            index = 19 if selected==19 else 0
            memory, destination = memory_case(index, count, shape, cases%2)
            memory.update({classifiers+i: 0 for i in range(12*4)}); put(memory, gate, disabled, 1)
            for i in range(12): put(memory, classifiers+i*4, 0x1A100000 if classifier else 0)
            put(memory, TABLE+index*8, 0x1A200000 if callback else 0)
            enabled = category<12 and selected<20 and not disabled and classifier and callback and count==1
            if enabled:
                wanted, calls, unknown = reference(memory, index, destination, failed)
                calls = [(screen.ENTRY, ACTOR, selected), *calls]
            else: wanted, calls, unknown = external(memory), [], set()
            models = []
            for words in (self.raw, self.normalized, self.retail):
                helpers = dict(self.search); helpers.update({screen.ENTRY+i*4: word for i, word in enumerate(words)})
                model = UpdaterOracle(caller, memory, index, destination, failed, phase=phase, connected=helpers,
                    entry=entry, arguments=(ACTOR, category, selected)).run()
                self.assertEqual(model.calls, calls)
                self.assertEqual({a: v for a, v in external(model.memory).items() if a not in unknown},
                    {a: v for a, v in wanted.items() if a not in unknown})
                models.append(model)
            self.assertEqual(models[1].events, models[2].events)
            self.assertEqual(models[1].memory, models[2].memory); cases += 1
        self.assertEqual(cases, 3072)
        owner = (self.root/'conker/src/game_16EE20.c').read_text()
        start = owner.index('void func_15141DA4('); end = owner.index('\n}', start)+2
        wrapper = owner[start:end]
        self.fixture = native_fixture()+'\nstatic s32 D_8008A084[12];static u8 D_800BE616;\n'+wrapper+'\n'
        self.run_host(r'''
int categories[]={-1,0,11,12},selections[]={-1,0,19,20},counts[]={-1,0,1};
int c,s,g,k,a,b,shape,f,i,valid,idx,cases=0;
for(c=0;c<4;c++) for(s=0;s<4;s++) for(g=0;g<2;g++) for(k=0;k<3;k++)
for(a=0;a<2;a++) for(b=0;b<2;b++) for(shape=0;shape<2;shape++) for(f=0;f<2;f++) {
    idx=selections[s]==19?19:0;
    initialize(idx,(u32)counts[k],shape?4:0,f,0,0);
    for(i=0;i<12;i++) D_8008A084[i]=a;
    D_800BE616=(u8)g;D_8008A0B4[idx].unk0=b;
    valid=categories[c]>=0 && categories[c]<12 && selections[s]>=0 && selections[s]<20
        && !g && a && b && counts[k]>0;
    if(valid) reference_native();
    remember();
    initialize(idx,(u32)counts[k],shape?4:0,f,0,0);
    for(i=0;i<12;i++) D_8008A084[i]=a;
    D_800BE616=(u8)g;D_8008A0B4[idx].unk0=b;
    func_15141DA4(actor,categories[c],selections[s]);
    if(compare()) return 75;
    cases++;
}
if(cases!=1536) return 76;
''')
        (self.output/'caller.json').write_text(json.dumps(dict(guest_cases=cases, bodies=3, caller_words=37,
            connected_search_words=23, native_cases=1536, scalar_return=False), indent=2)+'\n')

    def test_invalid_guest_storage_and_cycles_fail_strict_gates(self):
        for words in (self.raw, self.normalized, self.retail):
            memory, destination = memory_case(0, 1, 4)
            del memory[ACTOR+0x2F4]
            with self.assertRaisesRegex(AssertionError, 'unmapped read'):
                UpdaterOracle(words, memory, 0, destination).run()
            memory, destination = memory_case(0, 1, 4)
            put(memory, NODES+3*0x20+0x14, NODES)
            with self.assertRaisesRegex(AssertionError, 'instruction budget'):
                UpdaterOracle(words, memory, 0, destination, connected=self.search).run()

    def test_compiled_negatives_change_valid_calls_or_known_storage(self):
        negatives = {'placeholder': 'void func_15141E38(u8 *actor, s32 index) { }',
            'first-match-only': screen.SELECTED.replace('            matched = node;', '            matched = node;').replace(
                '            *(s16 *)(record + 0xE) = D_8008A0B4[index].unk4;', '            *(s16 *)(record + 0xE) = D_8008A0B4[index].unk4;\n            return;'),
            'wrong-selector': screen.SELECTED.replace('record + 0x28', 'record + 0x24'),
            'wrong-store-width': screen.SELECTED.replace('*(s16 *)(record + 0xE)', '*(s32 *)(record + 0xC)'),
            'wrong-count': screen.SELECTED.replace('= D_8008A0B4[index].unk4;', '= D_8008A0B4[index].unk0;'),
            'cached-count': screen.SELECTED.replace('    u8 *created;', '    s32 cached = D_8008A0B4[index].unk4;\n    u8 *created;').replace('= D_8008A0B4[index].unk4;', '= cached;'),
            'wrong-flag': screen.SELECTED.replace('-1, -1, -1, 1, 50,', '-1, -1, -1, 2, 50,'),
            'wrong-duration': screen.SELECTED.replace('1, 50, (struct37 *)12', '1, 49, (struct37 *)12'),
            'short-copy': screen.SELECTED.replace('&request, 12', '&request, 9'),
            'skip-link': screen.SELECTED.replace('            func_1514EC1C((s32)created, (s32)actor, 0x1A);\n', '')}
        receipts = []
        for name, body in negatives.items():
            if name=='cached-count': body = body.replace('s32 cached = cached;', 's32 cached = D_8008A0B4[index].unk4;')
            record, words = screen.compile_candidate(self.root, self.output, 'negative-'+name, body)
            differences = 0
            for index, shape, mode in itertools.product((0, 19), (0, 1, 4, 5), (0, 1, 15)):
                memory, destination = memory_case(index, 0x12348001, shape)
                wanted, calls, unknown = reference(memory, index, destination, 0, mode)
                model = UpdaterOracle(words, memory, index, destination, mode=mode, bind=False).run()
                changed = model.calls != calls or any(model.memory[a]!=value for a, value in wanted.items() if a not in unknown)
                differences += bool(changed)
            self.assertGreater(differences, 0, name); receipts.append(dict(name=name, differences=differences, words=record['body_words']))
        (self.output/'negatives.json').write_text(json.dumps(receipts, indent=2)+'\n')

    def test_production_source_slot_callers_and_unchanged_guard_prefix(self):
        owner = (self.root/'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.SELECTED, owner); self.assertEqual(owner.count(screen.PROTOTYPE), 2)
        functions, _, addresses = load_elf_functions(str(self.root/'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual((addresses[screen.FUNCTION], len(functions[screen.FUNCTION])), (screen.ENTRY, 80))
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        for name, offset, count in (('func_15141A7C', 0x16EF2C, 100), ('func_15141C0C', 0x16F0BC, 45),
                                   ('func_15141CC0', 0x16F170, 57), ('func_15141DA4', 0x16F254, 37)):
            self.assertEqual(functions[name], list(struct.unpack_from('>%dI'%count, self.rom, offset)))
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream: rows = list(csv.DictReader(stream))
        self.assertEqual(len(rows), 10809)
        prefix = json.dumps(rows[:10785], sort_keys=True, separators=(',', ':')).encode()
        self.assertEqual(hashlib.sha256(prefix).hexdigest(), '3dab8eceb937516ba0c03ffcef9a1bcd29f8dd9dd6e4cf62790ed3e903cbe077')
        _, _, relocations = parse_object(self.output/'selected.o')
        self.assertEqual(rows[10785:], screen.guard_rows(self.raw, relocations))

    def test_copied_owner_typed_abi_raw_slot_neighbors_and_existing_pool(self):
        owner = (self.root/'conker/src/game_16EE20.c').read_text()
        old_owner = owner.replace(screen.SELECTED, 's32 func_15141E38(s32 arg0, s32 arg1) {\n    return 0;\n}')
        old_owner = old_owner.replace(screen.PROTOTYPE, 's32 func_15141E38(s32, s32);')
        old_owner = old_owner.replace('func_15141E38(actor, selected);', 'func_15141E38((s32)actor, selected);')
        baseline, old_warnings = compile_owner(self.root, self.output, old_owner, 'owner-baseline')
        candidate, warnings = compile_owner(self.root, self.output, owner, 'owner-selected')
        old_text, old_functions, old_relocations = parse_object(baseline)
        text, functions, relocations = parse_object(candidate)
        self.assertEqual(set(functions), set(old_functions))
        for name, old in old_functions.items():
            if name==screen.FUNCTION: continue
            current = functions[name]
            self.assertEqual(current['size'], old['size'], name)
            self.assertEqual(text[current['value']:current['value']+current['size']],
                old_text[old['value']:old['value']+old['size']], name)
            self.assertEqual({offset-current['value']: items for offset, items in relocations.items()
                if current['value'] <= offset < current['value']+current['size']},
                {offset-old['value']: items for offset, items in old_relocations.items()
                if old['value'] <= offset < old['value']+old['size']}, name)
        current = functions[screen.FUNCTION]
        standalone, _, standalone_relocations = parse_object(self.output/'selected.o')
        self.assertEqual(current['size'], 320)
        self.assertEqual(text[current['value']:current['value']+320], standalone[:320])
        self.assertEqual({offset-current['value']: items for offset, items in relocations.items()
            if current['value'] <= offset < current['value']+320}, standalone_relocations)
        self.assertEqual(screen.sections(candidate)['.rodata'][1], screen.sections(baseline)['.rodata'][1])
        self.assertEqual(len(old_warnings), 3); self.assertEqual(len(warnings), 2)
        self.assertTrue(all(warning in old_warnings for warning in warnings))
        (self.output/'owner.json').write_text(json.dumps(dict(functions=len(functions),
            changed_functions=[screen.FUNCTION], warning_counts=[3, 2], pool_unchanged=True,
            dispatcher_raw_words_unchanged=True), indent=2)+'\n')


if __name__=='__main__': unittest.main()
