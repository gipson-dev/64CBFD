"""Complete triangle remapping and the matrix helper's nonstandard tail contract."""

import math
import csv
import re
import shutil
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_actor_triangle_transform_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests import test_game_actor_update_pass_match as actor_pass
from tools.tests import test_game_table_range_loader as table
from tools.tests.game_animation_timeline_oracle import bits, floating, signed

ENTRY, MATRIX, TAIL, CONTINUATION = 0x1502F490, 0x150A7960, 0x150A7A00, 0x150A7A14
ACTOR, OUTPUT, VERTICES, OFFSETS, RANGES = actor_pass.ACTORS, 0x20000, 0x80280000, 0x21000, 0x22000
BUFFER, SOURCE, ALTERNATE = 0x24000, 0x25000, 0x26000
OFFSET_TABLE, BASE_TABLE, COUNT_TABLE, RANGE_TABLE = 0x800C6070, 0x800D19A0, 0x800C5EF8, 0x800C5C08


def put(memory, address, value, size=4):
    actor_pass.dispatch.put(memory, address, value, size)


def memory_case(identity=7, joint=0, vertices=((0, 0, 0), (4, 2, 0), (0, 3, 4)),
                coordinate=(1.0, 5.5, 1.0), translations=((0, 0, 0), (10, 20, 30), (-3, -4, -5))):
    memory = actor_pass.memory_case()
    for base, length in ((OUTPUT, 64), (VERTICES, 256), (OFFSETS, 256), (RANGES, 128),
                         (BUFFER, 256), (SOURCE, 256), (ALTERNATE, 256),
                         (OFFSET_TABLE, 1024), (BASE_TABLE, 1024), (COUNT_TABLE, 512), (RANGE_TABLE, 1024)):
        memory.update({base + i: 0xA5 for i in range(length)})
    memory.update({table.STACK + i: 0xA5 for i in range(-0x600, 0x100)})
    for address, value, size in ((ACTOR + 4, identity, 1), (ACTOR + 0x1D8, BUFFER, 4),
            (ACTOR + 0x1D4, SOURCE, 4), (OFFSET_TABLE + identity * 4, OFFSETS, 4),
            (BASE_TABLE + identity * 4, VERTICES, 4), (COUNT_TABLE + identity * 2, 3, 2),
            (RANGE_TABLE + identity * 4, RANGES, 4)):
        put(memory, address, value, size)
    for i, point in enumerate(vertices):
        put(memory, OFFSETS + (joint * 3 + i) * 4, i * 16)
        for axis, value in enumerate(point):
            put(memory, VERTICES + i * 16 + axis * 2, value, 2)
        for offset, value in ((0, VERTICES + i * 16), (4, 1), (8, i)):
            put(memory, RANGES + i * 12 + offset, value)
    for i, value in enumerate(coordinate):
        put(memory, OUTPUT + i * 4, bits(value))
    for base, translation in zip((BUFFER, SOURCE, ALTERNATE), translations):
        for matrix in range(4):
            for index in range(16):
                value = 1.0 if index in (0, 5, 10, 15) else 0.0
                if index in (12, 13, 14):
                    value = translation[index - 12]
                put(memory, base + matrix * 64 + index * 4, bits(value))
    return memory


class TriangleOracle(table.RangeOracle):
    def __init__(self, words, memory, phase=0, joint=0, actions=None, connected=None,
                 outputs=None, entry=ENTRY, arguments=None, tail=False):
        outputs = outputs or (OUTPUT, OUTPUT + 4, OUTPUT + 8)
        args = (ACTOR, *outputs, joint) if arguments is None else arguments
        super().__init__(words, memory, args, phase, connected=connected, entry=entry)
        self.actions, self.tail = actions or {}, tail
        self.condition = False
        self.f[20:] = [0x3F800000 + i for i in range(20, 32)]
        self.saved_f = self.f[20:].copy()
        self.matrix_calls = 0

    def execute(self, word):
        op, rs, rt, rd, shift, fn = word >> 26, word >> 21 & 31, word >> 16 & 31, word >> 11 & 31, word >> 6 & 31, word & 63
        if op in (53, 61):
            imm = word & 65535
            address = (self.r[rs] + (imm if imm < 32768 else imm - 65536)) & 0xFFFFFFFF
            assert rt % 2 == 0 and address % 8 == 0
            if op == 61:
                self.put(address, self.f[rt + 1] << 32 | self.f[rt], 8)
            else:
                value = self.get(address, 8)
                self.f[rt], self.f[rt + 1] = value & 0xFFFFFFFF, value >> 32
        elif op == 17 and rs == 20 and fn == 32:
            self.f[shift] = bits(float(signed(self.f[rd])))
        elif op == 17 and rs == 16 and fn == 3:
            left, right = floating(self.f[rd]), floating(self.f[rt])
            self.f[shift] = bits(left / right if right else
                                (math.nan if not left else math.copysign(math.inf, left * math.copysign(1.0, right))))
        else:
            super().execute(word)

    def record_call(self, target):
        if target == ENTRY:
            self.calls.append((target, *self.arguments(5)))
            return
        assert target == MATRIX
        args = self.arguments(7)
        assert args[5] == args[4] + 4 and args[6] == args[4] + 8
        assert all(table.STACK - 0x600 <= a < table.STACK for a in args[4:])
        self.calls.append((target, *args[:4], ('private-point', self.matrix_calls)))
        self.matrix_calls += 1

    def hook(self, target):
        assert target == MATRIX
        matrix, x, y, z, out_x, out_y, out_z = self.arguments(7)
        x, y, z = map(floating, (x, y, z))
        values = [floating(self.get(matrix + i * 4, 4)) for i in range(16)]
        result = [bits(floating(bits(floating(bits(values[i] * x)) + floating(bits(values[i + 4] * y))))
                       + floating(bits(floating(bits(values[i + 8] * z)) + values[i + 12]))) for i in range(3)]
        for address, value in zip((out_x, out_y, out_z), result):
            self.put(address, value, 4)
        for address, value, size in self.actions.get(self.matrix_calls - 1, ()):
            self.put(address, value, size)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]

    def run(self):
        pc = self.entry
        for _ in range(50000):
            self.visits.add(pc)
            word = self.code[pc]
            op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
            if op == 17 and rs == 8:
                take, likely = self.condition == bool(rt & 1), bool(rt & 2)
            elif op in (1, 4, 5, 6, 7, 20, 21):
                if op == 1:
                    assert rt in (0, 1, 2, 3)
                    take, likely = signed(self.r[rs]) >= 0 if rt & 1 else signed(self.r[rs]) < 0, bool(rt & 2)
                else:
                    take = signed(self.r[rs]) <= 0 if op == 6 else signed(self.r[rs]) > 0 if op == 7 else self.r[rs] == self.r[rt]
                    if op in (5, 21):
                        take = not take
                    likely = op in (20, 21)
            else:
                take = None
            if take is not None:
                imm = word & 65535
                offset = imm if imm < 32768 else imm - 65536
                if take or not likely:
                    self.visits.add(pc + 4)
                    self.execute(self.code[pc + 4])
                pc = pc + 4 + offset * 4 if take else pc + 8
            elif op in (2, 3):
                target = (pc + 4 & 0xF0000000) | ((word & 0x3FFFFFF) << 2)
                if op == 3:
                    self.r[31] = pc + 8
                self.visits.add(pc + 4)
                self.execute(self.code[pc + 4])
                if op == 3:
                    self.record_call(target)
                if target in self.code:
                    pc = target
                else:
                    assert op == 3
                    self.hook(target)
                    pc += 8
            elif op == 0 and word & 63 == 8:
                target = self.r[rs]
                self.visits.add(pc + 4)
                self.execute(self.code[pc + 4])
                if target == 0xDEAD0000:
                    for register in (*range(16, 24), 28, 29, 30, *((31,) if not self.tail else ())):
                        assert self.r[register] == self.before[register], ('saved register', register)
                    assert self.f[20:] == self.saved_f
                    return self
                assert target in self.code, ('unowned jump', target)
                pc = target
            else:
                self.execute(word)
                pc += 4
        raise AssertionError('triangle instruction budget exhausted')


def external_writes(model):
    return [event for event in model.events if event[0] == 'W' and not
            table.STACK - 0x600 <= event[1] < table.STACK + 0x100]


class GameActorTriangleTransformMatchTests(unittest.TestCase):
    run_host = table.native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').exists() or any(shutil.which(n) is None
                for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-actor-triangle-transform-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        _, cls.baseline = screen.compile_candidate(cls.root, cls.output, 'baseline', screen.BASELINE)
        cls.negative = {n: screen.compile_candidate(cls.root, cls.output, n, b)[1]
                        for n, b in screen.candidates() if 'negative-control' in n}
        cls.matrix_record, cls.matrix_control = screen.compile_candidate(cls.root, cls.output, 'matrix-control', screen.MATRIX_BODY, 'func_150A7960')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>302I', rom, 0x5C940))
        cls.matrix = list(struct.unpack_from('>40I', rom, 0xD4E10))
        cls.tail = list(struct.unpack_from('>5I', rom, 0xD4EB0))
        cls.continuation = list(struct.unpack_from('>13I', rom, 0xD4EC4))
        cls.production = load_elf_functions(str(cls.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')[0]
        cls.connected = {MATRIX + i * 4: w for i, w in enumerate(cls.matrix)}
        cls.connected.update({CONTINUATION + i * 4: w for i, w in enumerate(cls.continuation)})
        cls.coverage, cls.sdk_coverage, cls.cases = set(), set(), 0
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = ('''typedef unsigned char u8;typedef short s16;typedef unsigned short u16;
typedef unsigned int u32;typedef int s32;typedef float f32;
#define NULL ((void *)0)
''' + screen.DECLARATIONS + r'''
u32 *D_800C6070[256];u8 *D_800D19A0[256];u16 D_800C5EF8[256];
ActorRange58F80 *D_800C5C08[256];
static ActorCopy58F80 actor;
static ActorVertex58F80 records[16];
static ActorRange58F80 ranges[8];
static u32 offsets[24],log[6][4];
static f32 banks[3][4][16],coordinates[3];
static int logCount,error,mutation;
static u32 word(f32 v) {union {f32 f;u32 u;} b;b.f=v;return b.u;}
static void reset(int id,int pattern,int mode) {
    int i,j,k;u8 *p=(u8 *)&actor;
    for(i=0;i<(int)sizeof(actor);i++) p[i]=0xA5;
    for(i=0;i<(int)sizeof(records);i++) ((u8 *)records)[i]=0xA5;
    for(i=0;i<256;i++) {D_800C6070[i]=NULL;D_800D19A0[i]=NULL;D_800C5EF8[i]=0;D_800C5C08[i]=NULL;}
    for(i=0;i<8;i++) {ranges[i].start=(u32)(records+i);ranges[i].count=1;ranges[i].matrix=(u32)(i%4);}
    for(i=0;i<24;i++) offsets[i]=(u32)(i%3)*16;
    records[0].x=records[0].y=records[0].z=0;
    records[1].x=4;records[1].y=2;records[1].z=0;
    records[2].x=0;records[2].y=3;records[2].z=4;
    for(i=0;i<3;i++) for(j=0;j<4;j++) for(k=0;k<16;k++) {
        banks[i][j][k]=(k==0 || k==5 || k==10 || k==15)?1.0f:0.0f;
        if(k>=12 && k<15) banks[i][j][k]=i==1?(f32)((k-11)*10):i==2?(f32)(-k+9):0.0f;
    }
    actor.id=(u8)id;actor.source=banks[1];actor.buffer=banks[0];
    D_800C6070[id]=offsets;D_800D19A0[id]=(u8 *)records;
    D_800C5EF8[id]=3;D_800C5C08[id]=ranges;
    coordinates[0]=1.0f;coordinates[1]=5.5f;coordinates[2]=1.0f;
    if(pattern==1) D_800C6070[id]=NULL;
    if(pattern==2) D_800C5EF8[id]=0;
    if(pattern==3) D_800C5EF8[id]=2;
    if(pattern==4) actor.buffer=NULL;
    if(pattern==5) actor.source=NULL;
    if(pattern==6) ranges[0].count=0;
    if(pattern==7) {coordinates[0]=3.0f;coordinates[2]=3.0f;}
    if(pattern==8) coordinates[0]=-1.0f;
    if(pattern==9) coordinates[2]=5.0f;
    if(pattern==10) records[2].z=0;
    if(pattern==11) {records[1].x=0;records[1].z=4;records[2].x=4;records[2].z=0;}
    if(pattern==12) {records[0].x=records[0].z=-32768;records[1].x=32767;
        records[1].z=-32768;records[2].x=-32768;records[2].z=32767;records[2].y=-32768;}
    if(pattern==13) {coordinates[0]=4.0f;coordinates[2]=4.0f;}
    if(pattern==14) D_800C5EF8[id]=65535;
    if(pattern==15) {records[1].x=32;coordinates[0]=100000008.0f;
        for(j=0;j<4;j++) banks[0][j][12]=100000000.0f;}
    if(pattern==16) {ranges[0].count=2;ranges[0].matrix=0;
        ranges[1].count=2;ranges[1].matrix=2;}
    if(pattern==17) {ranges[1].start=(u32)records;ranges[1].count=3;ranges[1].matrix=1;}
    logCount=error=0;mutation=mode;
    for(i=0;i<24;i++) ((u32 *)log)[i]=0;
}
''' + screen.MATRIX_BODY.replace('void func_150A7960(', 'static void matrixReference(') + r'''
void func_150A7960(f32 *matrix,f32 x,f32 y,f32 z,f32 *outX,f32 *outY,f32 *outZ) {
    int call=logCount;
    if(call>=6 || outY!=outX+1 || outZ!=outY+1) {error=1;return;}
    log[call][0]=(u32)matrix;log[call][1]=word(x);log[call][2]=word(y);log[call][3]=word(z);
    logCount++;matrixReference(matrix,x,y,z,outX,outY,outZ);
    if(call==0) {
        if(mutation&1) actor.id^=255;
        if(mutation&2) actor.buffer=banks[2];
        if(mutation&4) actor.source=banks[2];
        if(mutation&16) {records[1].x=8;records[1].y=-32768;}
        if(mutation&64) {D_800C5EF8[actor.id]=0;offsets[1]=32;}
    }
    if(call==3 && (mutation&8)) actor.source=banks[2];
    if(call==5 && (mutation&32)) {coordinates[0]=3;coordinates[1]=-4.5f;coordinates[2]=3;}
}
static void reference(f32 *x,f32 *y,f32 *z,int joint) {
    ActorVertex58F80 *v[3];u32 selected[3];int id=actor.id,i,j,found,pass,axis;
    f32 p[2][3][3],a[2][3],b[2][3],delta[3],wa,wb,den,newBlend,oldBlend;
    f32 *outputs[3]={x,y,z};u8 *matrixBase;
    if(!D_800C6070[id]) return;
    for(j=0;j<3;j++) v[j]=(ActorVertex58F80 *)(D_800D19A0[id]+D_800C6070[id][joint*3+j]);
    for(j=0;j<3;j++) {
        found=0;
        for(i=0;i<D_800C5EF8[id];i++) {
            ActorRange58F80 *r=D_800C5C08[id]+i;
            if((u32)v[j]>=r->start && (u32)v[j]<r->start+(r->count<<4)) {
                selected[j]=r->matrix;found=1;break;
            }
        }
        if(!found) return;
    }
    matrixBase=actor.buffer;if(!matrixBase || !actor.source) return;
    for(pass=0;pass<2;pass++) {
        if(pass) matrixBase=actor.source;
        for(j=0;j<3;j++) func_150A7960((f32 *)(matrixBase+(selected[j]<<6)),
            (f32)v[j]->x,(f32)v[j]->y,(f32)v[j]->z,p[pass][j],p[pass][j]+1,p[pass][j]+2);
    }
    for(pass=0;pass<2;pass++) for(axis=0;axis<3;axis++) {
        a[pass][axis]=p[pass][1][axis]-p[pass][0][axis];
        b[pass][axis]=p[pass][2][axis]-p[pass][0][axis];
    }
    for(axis=0;axis<3;axis++) delta[axis]=*outputs[axis]-p[0][0][axis];
    den=a[0][0]*b[0][2]-b[0][0]*a[0][2];
    wa=den==0?-100.0f:(delta[0]*b[0][2]-b[0][0]*delta[2])/den;
    if(wa<0 || wa>1) return;
    wb=b[0][2]==0?-100.0f:(delta[2]-wa*a[0][2])/b[0][2];
    if(wb<0 || wb>1) return;
    for(axis=0;axis<3;axis++) {
        newBlend=b[1][axis]*wb+wa*a[1][axis];
        oldBlend=axis==1?b[0][1]*wb+wa*a[0][1]:delta[axis];
        *outputs[axis]=*outputs[axis]+(((newBlend+p[1][0][axis])-oldBlend)-p[0][0][axis]);
    }
}
''' + screen.SELECTED + '\n')

    def models(self, memory, phase=0, joint=0, actions=None, connected=None, outputs=None):
        models = [TriangleOracle(words, memory, phase, joint, actions, connected, outputs).run()
                  for words in (self.retail, self.words, self.baseline)]
        first = models[0]
        for model in models[1:]:
            self.assertEqual(actor_pass.external_memory(model.memory), actor_pass.external_memory(first.memory))
            self.assertEqual(external_writes(model), external_writes(first))
            self.assertEqual(model.calls, first.calls)
        type(self).cases += 1
        type(self).coverage.update(first.visits)
        type(self).sdk_coverage.update(first.visits & set(self.connected))
        return first

    def test_full_body_fits_without_guards(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (298, 0x160, 273))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(len(self.words), 302)
        source = (self.root / 'conker/src/game/generated_58F80.c').read_text()
        self.assertEqual(re.search(r'void func_1502F490\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(), screen.SELECTED)
        self.assertEqual(self.production['func_1502F490'], self.words)
        self.assertEqual(self.production['func_150A7960'], self.matrix)
        self.assertEqual(self.production['func_150A7A00'], self.tail)
        self.assertEqual(self.production['func_150A7A14'], self.continuation)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            self.assertFalse(any(r['function'] in ('func_1502F490', 'func_150A7960') for r in csv.DictReader(stream)))

    def test_connected_coordinate_phase_uses_complete_transform(self):
        phase_entry = 0x1502F3C8
        phase_words = self.production['func_1502F3C8']
        for identity in (0, 1, 127, 187, 255):
            for joint in (0, 7):
                for stack_phase in (0, 8):
                    for translation in (20, -4):
                        memory = memory_case(identity, joint, translations=((0, 0, 0), (10, translation, 30), (-3, -4, -5)))
                        for offset, value, size in ((0, 1, 4), (0x274, 1, 1), (0x19E, joint, 2),
                                (0x14, bits(1.0), 4), (0x18, bits(-2.0), 4), (0x1C, bits(1.0), 4), (0x180, bits(3.5), 4)):
                            put(memory, ACTOR + offset, value, size)
                        models = []
                        for body in (self.retail, self.words, self.baseline):
                            connected = dict(self.connected)
                            connected.update({ENTRY + i * 4: w for i, w in enumerate(body)})
                            models.append(TriangleOracle(phase_words, memory, stack_phase, connected=connected,
                                                         entry=phase_entry, arguments=()).run())
                        for model in models[1:]:
                            self.assertEqual(actor_pass.external_memory(model.memory), actor_pass.external_memory(models[0].memory))
                            self.assertEqual(external_writes(model), external_writes(models[0]))
                            self.assertEqual(model.calls, models[0].calls)
                        expected_y = 23.5 if translation == 20 else 3.5
                        self.assertEqual([models[0].peek(ACTOR + offset, 4) for offset in (0x14, 0x18, 0x1C, 0x180)],
                                         list(map(bits, (11.0, expected_y, 31.0, expected_y))))
                        self.assertEqual(models[0].calls[0], (ENTRY, ACTOR, ACTOR + 0x14, ACTOR + 0x18, ACTOR + 0x1C, joint))
                        self.assertEqual(len(models[0].calls), 7)
                        type(self).cases += 1
                        type(self).coverage.update(models[0].visits)

    def test_all_identity_bytes_and_joint_rows_use_the_seven_argument_abi(self):
        for identity in range(256):
            for joint in (0, 1, 7):
                for phase in (0, 8):
                    model = self.models(memory_case(identity, joint), phase, joint)
                    self.assertEqual(len(model.calls), 6)
                    self.assertEqual([c[1] for c in model.calls], [BUFFER + i * 64 for i in range(3)] + [SOURCE + i * 64 for i in range(3)])
                    self.assertEqual([model.peek(OUTPUT + i * 4, 4) for i in range(3)], list(map(bits, (11.0, 25.5, 31.0))))

    def test_ordered_early_returns_and_unsigned_interval_edges(self):
        for mode in range(10):
            memory = memory_case()
            if mode == 0:
                put(memory, OFFSET_TABLE + 28, 0)
                for i in range(4):
                    del memory[ACTOR + 0x1D8 + i]
            elif mode == 1:
                put(memory, COUNT_TABLE + 14, 0, 2)
                for i in range(4):
                    del memory[ACTOR + 0x1D8 + i]
            elif mode == 2:
                put(memory, COUNT_TABLE + 14, 2, 2)
            elif mode == 3:
                put(memory, ACTOR + 0x1D8, 0)
                for i in range(4):
                    del memory[ACTOR + 0x1D4 + i]
            elif mode == 4:
                put(memory, ACTOR + 0x1D4, 0)
            elif mode == 5:
                put(memory, RANGES + 4, 0)
            elif mode == 6:
                put(memory, RANGES, VERTICES + 16)
            elif mode == 7:
                put(memory, RANGES, VERTICES - 16)
            elif mode == 8:
                put(memory, RANGES, 0xFFFFFFF0)
                put(memory, RANGES + 4, 2)
            else:
                put(memory, RANGES + 4, 0x10000000)
            self.assertFalse(self.models(memory).calls, mode)
        for count in (0x8000, 0xFFFF):
            memory = memory_case()
            put(memory, COUNT_TABLE + 14, count, 2)
            self.assertEqual(len(self.models(memory).calls), 6)

    def test_connected_real_matrix_helper_and_independent_weight_acceptance(self):
        for x in (-1.0, -0.0, 0.0, 1.0, 3.0, 4.0, 5.0):
            for z in (-1.0, -0.0, 0.0, 1.0, 3.0, 4.0, 5.0):
                for phase in (0, 8):
                    model = self.models(memory_case(coordinate=(x, 5.5, z)), phase, connected=self.connected)
                    accepted = 0 <= x <= 4 and 0 <= z <= 4
                    self.assertEqual(len(model.calls), 6)
                    self.assertEqual(bool(external_writes(model)), accepted)
                    expected = (x + 10, 25.5, z + 30) if accepted else (x, 5.5, z)
                    self.assertEqual([model.peek(OUTPUT + i * 4, 4) for i in range(3)], list(map(bits, expected)))

    def test_overlapping_ranges_keep_first_match_and_stop_before_third_range(self):
        wrong_body = screen.BASELINE.replace('if ((mask & bit) == 0)', 'if (1)')
        _, wrong_words = screen.compile_candidate(self.root, self.output, 'last-match-negative-control', wrong_body)
        for variant, expected in ((0, (0, 0, 2)), (1, (0, 1, 1))):
            memory = memory_case()
            if variant == 0:
                put(memory, RANGES + 4, 2)
                put(memory, RANGES + 8, 0)
                put(memory, RANGES + 16, 2)
                put(memory, RANGES + 20, 2)
            else:
                put(memory, RANGES + 12, VERTICES)
                put(memory, RANGES + 16, 3)
                put(memory, RANGES + 20, 1)
            for offset in range(24, 36):
                del memory[RANGES + offset]
            for phase in (0, 8):
                model = self.models(memory, phase)
                self.assertEqual([c[1] for c in model.calls],
                                 [base + index * 64 for base in (BUFFER, SOURCE) for index in expected])
                wrong = TriangleOracle(wrong_words, memory, phase).run()
                self.assertNotEqual(model.calls, wrong.calls)

    def test_final_coordinate_update_retains_single_precision_rounding(self):
        memory = memory_case(vertices=((0, 0, 0), (32, 2, 0), (0, 3, 4)),
                             coordinate=(100000008.0, 5.5, 1.0),
                             translations=((100000000.0, 0, 0), (10, 20, 30), (-3, -4, -5)))
        model = self.models(memory, connected=self.connected)
        self.assertEqual(model.peek(OUTPUT, 4), bits(16.0))
        wrong = TriangleOracle(self.negative['direct-x-negative-control'], memory, connected=self.connected).run()
        self.assertEqual(wrong.peek(OUTPUT, 4), bits(18.0))

    def test_high_unsigned_joint_rows_keep_full_fifth_argument(self):
        for joint in (0x8000, 0xFFFF):
            for phase in (0, 8):
                self.assertEqual(len(self.models(memory_case(joint=joint), phase, joint).calls), 6)

    def test_live_mutations_cached_buffers_vertices_and_fresh_inputs(self):
        modes = ({0: ((ACTOR + 0x1D8, ALTERNATE, 4),)},
                 {0: ((ACTOR + 0x1D4, ALTERNATE, 4),)},
                 {0: ((ACTOR + 4, 99, 1), (COUNT_TABLE + 14, 0, 2))},
                 {0: ((VERTICES + 16, 8, 2), (VERTICES + 18, -32768, 2))},
                 {2: ((ACTOR + 0x1D4, ALTERNATE, 4),)},
                 {3: ((ACTOR + 0x1D4, ALTERNATE, 4),)},
                 {5: ((OUTPUT, bits(3.0), 4), (OUTPUT + 4, bits(-4.5), 4))})
        for actions in modes:
            for phase in (0, 8):
                self.assertEqual(len(self.models(memory_case(), phase, actions=actions).calls), 6)

    def test_degenerate_triangles_signed_coordinates_and_output_aliases(self):
        for vertices in (((0, 0, 0), (4, 2, 0), (8, 3, 0)),
                         ((0, 0, 0), (0, 2, 4), (4, 3, 0)),
                         ((-32768, -1, -32768), (32767, 32767, -32768), (-32768, -32768, 32767))):
            for phase in (0, 8):
                self.models(memory_case(vertices=vertices), phase, connected=self.connected)
        for offsets in ((0, 0, 0), (0, 0, 8), (0, 4, 0), (0, 4, 4)):
            self.models(memory_case(), outputs=tuple(OUTPUT + o for o in offsets), connected=self.connected)

    def test_wrong_semantic_controls_are_detected(self):
        cases = [('closed-end-negative-control', {0: ((RANGES, VERTICES - 16, 4),)}, None),
                 ('cached-source-negative-control', {}, {0: ((ACTOR + 0x1D4, ALTERNATE, 4),)}),
                 ('sum-weight-negative-control', {}, None), ('wrong-y-negative-control', {}, None)]
        for name, changes, actions in cases:
            memory = memory_case(coordinate=(3.0, 5.5, 3.0) if name.startswith('sum') else (1.0, 5.5, 1.0))
            for address, value, size in changes.get(0, ()):
                put(memory, address, value, size)
            actual = TriangleOracle(self.retail, memory, actions=actions).run()
            wrong = TriangleOracle(self.negative[name], memory, actions=actions).run()
            self.assertNotEqual((actual.calls, actor_pass.external_memory(actual.memory)),
                                (wrong.calls, actor_pass.external_memory(wrong.memory)), name)

    def test_matrix_tail_entry_preserves_live_register_contract(self):
        for phase in (0, 8):
            memory = memory_case()
            arguments = (BUFFER, bits(2.0), bits(-3.0), bits(4.0), OUTPUT, OUTPUT + 4, OUTPUT + 8, OUTPUT + 12)
            tail = TriangleOracle(self.tail, memory, phase, connected=self.connected, entry=TAIL, arguments=arguments, tail=True).run()
            self.assertEqual([tail.peek(OUTPUT + i * 4, 4) for i in range(4)], list(map(bits, (2.0, -3.0, 4.0, 1.0))))
            self.assertEqual((tail.r[4], tail.r[25], tail.f[0], tail.f[2], tail.f[4]),
                             (BUFFER, 0xDEAD0000, bits(2.0), bits(-3.0), bits(4.0)))
            self.assertEqual(tail.visits & set(range(MATRIX, CONTINUATION + 52, 4)), set(range(MATRIX, CONTINUATION + 52, 4)))
            type(self).sdk_coverage.update(tail.visits & set(self.connected))
            original = TriangleOracle(self.matrix, memory, phase, entry=MATRIX, arguments=arguments).run()
            ordinary = TriangleOracle(self.matrix_control, memory, phase, entry=MATRIX, arguments=arguments).run()
            self.assertNotEqual((ordinary.f[0], ordinary.f[2], ordinary.f[4]), (original.f[0], original.f[2], original.f[4]))
        self.assertGreater(self.matrix_record['body_words'], 40)

    def test_native_independent_reference_full_state_and_callback_log(self):
        self.run_host(r'''
static int modes[]={0,1,2,4,8,16,32,64,3,7,15,31,63,127};
static u8 savedActor[0x32C],savedRecords[sizeof(records)],savedBanks[sizeof(banks)];
static u32 savedOffsets[24],savedLog[6][4],savedCoordinates[3];
static u16 savedCounts[256];int id,pattern,m,i,j,n,savedCount;
for(id=0;id<256;id++) for(pattern=0;pattern<18;pattern++) for(m=0;m<14;m++) {
    reset(id,pattern,modes[m]);reference(coordinates,coordinates+1,coordinates+2,pattern%8);
    if(error) return 1;
    savedCount=logCount;
    for(i=0;i<0x32C;i++) savedActor[i]=((u8 *)&actor)[i];
    for(i=0;i<(int)sizeof(records);i++) savedRecords[i]=((u8 *)records)[i];
    for(i=0;i<(int)sizeof(banks);i++) savedBanks[i]=((u8 *)banks)[i];
    for(i=0;i<24;i++) {savedOffsets[i]=offsets[i];((u32 *)savedLog)[i]=((u32 *)log)[i];}
    for(i=0;i<256;i++) savedCounts[i]=D_800C5EF8[i];
    for(i=0;i<3;i++) savedCoordinates[i]=word(coordinates[i]);
    reset(id,pattern,modes[m]);func_1502F490(&actor,coordinates,coordinates+1,coordinates+2,pattern%8);
    if(error || savedCount!=logCount) return 2;
    for(i=0;i<0x32C;i++) if(savedActor[i]!=((u8 *)&actor)[i]) return 3;
    for(i=0;i<(int)sizeof(records);i++) if(savedRecords[i]!=((u8 *)records)[i]) return 4;
    for(i=0;i<(int)sizeof(banks);i++) if(savedBanks[i]!=((u8 *)banks)[i]) return 5;
    for(i=0;i<24;i++) if(savedOffsets[i]!=offsets[i] || ((u32 *)savedLog)[i]!=((u32 *)log)[i]) return 6;
    for(i=0;i<256;i++) if(savedCounts[i]!=D_800C5EF8[i]) return 7;
    for(i=0;i<3;i++) if(savedCoordinates[i]!=word(coordinates[i])) return 8;
}
for(j=0;j<4;j++) for(n=0;n<8;n++) {
    f32 *x,*y,*z;u32 expected[3];
    reset(7,0,0);x=coordinates;y=(j&1)?x:coordinates+1;z=(j&2)?x:coordinates+2;
    reference(x,y,z,n);for(i=0;i<3;i++) expected[i]=word(coordinates[i]);
    reset(7,0,0);x=coordinates;y=(j&1)?x:coordinates+1;z=(j&2)?x:coordinates+2;
    func_1502F490(&actor,x,y,z,n);
    for(i=0;i<3;i++) if(expected[i]!=word(coordinates[i])) return 9;
}
reset(7,0,0);func_1502F490(&actor,coordinates,coordinates,coordinates,0);
if(word(coordinates[0])!=word(61.0f)) return 10;
''')

    @classmethod
    def tearDownClass(cls):
        print('triangle transform:', cls.cases, 'three-way cases;',
              len(cls.coverage & set(range(ENTRY, ENTRY + 1208, 4))), '/302 retail words;',
              len(cls.sdk_coverage), '/53 connected matrix/continuation words')


if __name__ == '__main__':
    unittest.main()
