"""Bounded projection recovery, not production matching or hardware acceptance."""

import itertools
import shutil
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_projection_lifetime_candidates as screen
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, MATRIX, TAIL, CONTINUATION
from tools.tests.test_game_table_range_loader import native, STACK
from tools.tests.game_animation_timeline_oracle import bits, floating

ENTRY = screen.ENTRY
POINT, XY, OUTPUT, VIEW, ALTERNATE = 0x20000, 0x21000, 0x22000, 0x50000, 0x70000
BANK, VIEW_WORD, UPPER, LOWER = 0x800D9D10, 0x800BE628, 0x800A56B0, 0x800D9B20


def put(memory, address, value, size=4):
    for i, byte in enumerate((value & ((1 << (size * 8)) - 1)).to_bytes(size, 'big')):
        memory[address + i] = byte


def peek(memory, address, size=4):
    return int.from_bytes(bytes(memory[address + i] for i in range(size)), 'big')


def private(address):
    return STACK - 0x200 <= address < STACK + 0x100


def external(memory):
    return {a: v for a, v in memory.items() if not private(a)}


def fixture(index=0, mask=0, layout=0, depth=2.0, lower=0.0, phase=0, new_index=None):
    memory = {STACK + i: 0xA5 for i in range(-0x200, 0x100)}
    chosen = index if new_index is None else new_index
    for base, length in ((POINT, 32), (XY, 32), (OUTPUT, 32), (VIEW_WORD, 8),
                         (BANK + index * 64, 80), (UPPER, 4), (LOWER, 4),
                         (VIEW + chosen * 384, 384), (ALTERNATE + chosen * 384, 384)):
        memory.update({base + i: 0xA5 for i in range(length)})
    for i, value in enumerate((2.0, 3.0, 4.0)):
        put(memory, POINT + i * 4, bits(value))
    for i in range(16):
        value = 1.0 if i in (0, 5, 10) else depth if i == 15 else 0.0
        put(memory, BANK + index * 64 + i * 4, bits(value))
    for base in (VIEW, ALTERNATE):
        for offset, value in ((12, 2.0), (16, 3.0), (52, 11.0),
                              (56, 37.0 if base == VIEW else 71.0)):
            put(memory, base + chosen * 384 + offset, bits(value))
    put(memory, VIEW_WORD, VIEW)
    put(memory, UPPER, bits(6000.0))
    put(memory, LOWER, bits(lower))
    xy, z, w, inverse = XY, OUTPUT, OUTPUT + 4, OUTPUT + 8
    if layout == 1: inverse = xy
    if layout == 2: inverse = xy + 4
    if layout == 3: z = xy
    if layout == 4: w = xy + 4
    if layout == 5: z = w
    if layout == 6: xy = VIEW + chosen * 384 + 16
    if layout == 7: xy = BANK + index * 64 + 12
    if layout == 8: xy = POINT
    if layout == 9:
        xy = VIEW_WORD
        put(memory, VIEW + chosen * 384 + 12, bits(-5.0))
        put(memory, VIEW + chosen * 384 + 52, ALTERNATE)
    args = (POINT, xy, 0 if mask & 1 else z, 0 if mask & 2 else w,
            0 if mask & 4 else inverse, 0xA5AB0000 | index)
    actions = []
    if new_index is not None:
        actions.append((STACK + phase + 0x17, new_index, 1))
    if layout == 9:
        actions.append((VIEW_WORD, VIEW, 4))
    return memory, args, actions


class ProjectionOracle(TriangleOracle):
    def __init__(self, words, memory, arguments, connected, phase=0, actions=()):
        super().__init__(words, memory, phase=phase, entry=ENTRY,
                         arguments=arguments, connected=connected)
        self.boundary_actions = actions
        self.pending_boundary = False

    def record_call(self, target):
        assert target == TAIL
        self.calls.append((target, *self.arguments(8)))
        self.pending_boundary = True

    def execute(self, word):
        # Both measured wrappers resume with this W-pointer home load.
        if self.pending_boundary and word == 0x8FB80054:
            for address, value, size in self.boundary_actions:
                self.put(address, value, size)
            self.pending_boundary = False
        super().execute(word)

    def hook(self, target):
        raise AssertionError(('unconnected helper', target))


def reference(memory, args, actions=(), phase=0):
    memory = memory.copy()
    point, xy, z, w, inverse, index = args
    entry_sp = STACK + phase
    put(memory, entry_sp + 0x14, index)
    z, w, inverse = z or entry_sp - 4, w or entry_sp - 8, inverse or entry_sp - 12
    matrix = BANK + (index & 255) * 64
    xyz = [floating(peek(memory, point + i * 4)) for i in range(3)]
    calls = [(TAIL, matrix, *(bits(v) for v in xyz), xy, xy + 4, z, w)]
    writes = []

    def write(address, word, size=4):
        put(memory, address, word, size)
        if not private(address):
            writes.append(('W', address, size, word & ((1 << (size * 8)) - 1)))

    def f(address):
        return floating(peek(memory, address))

    def rnd(value):
        return floating(bits(value))

    def dot(axis):
        p = [rnd(f(matrix + (axis + i * 4) * 4) * xyz[i]) for i in range(3)]
        return rnd(rnd(p[0] + p[1]) + rnd(p[2] + f(matrix + (axis + 12) * 4)))

    values = [dot(axis) for axis in range(3)]
    for address, value in zip((xy, xy + 4, z), values):
        write(address, bits(value))
    write(w, bits(dot(3)))
    for address, value, size in actions:
        write(address, value, size)
    depth = f(w)
    if f(UPPER) <= depth or depth <= f(LOWER) or depth == 0.0:
        return memory, writes, calls, 0
    write(inverse, bits(1.0 / depth))
    index = peek(memory, entry_sp + 0x17, 1)
    offset = (index & 255) * 384
    view = peek(memory, VIEW_WORD) + offset
    xp = rnd(f(xy) * rnd(f(view + 12) + 5.0))
    yp = rnd(f(xy + 4) * rnd(f(view + 16) + 5.0))
    write(xy, bits(rnd(rnd(f(inverse) * xp) + f(view + 52))))
    view = peek(memory, VIEW_WORD) + offset
    write(xy + 4, bits(rnd(f(view + 56) - rnd(f(inverse) * yp))))
    return memory, writes, calls, 1


class GameProjectionLifetimeRecoveryTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or shutil.which('mips-linux-gnu-ld') is None:
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-projection-lifetime-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        wrong = screen.partial_body(1, 0, False, False, True)
        cls.wrong_record, cls.late_y = screen.compile_candidate(cls.root, cls.output, 'late-y', wrong)
        cached_inverse = screen.SELECTED.replace('    s32 offset;', '    s32 offset;\n    f32 savedInverse;')
        cached_inverse = cached_inverse.replace('    arg1[0] =', '    savedInverse = *arg4;\n    arg1[0] =')
        cached_inverse = cached_inverse.replace('view->unk38 - *arg4 * cachedDepth',
                                                'view->unk38 - savedInverse * cachedDepth')
        cached_view = screen.SELECTED
        line = '    view = (struct140 *)((u8 *)D_800BE628 + offset);\n'
        before, after = cached_view.rsplit(line, 1)
        cached_view = before + after
        cls.stale = {name: screen.compile_candidate(cls.root, cls.output, name, body)[1]
                     for name, body in (('cached-inverse', cached_inverse), ('cached-view', cached_view))}
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>101I', rom, screen.ROM))
        cls.connected = {}
        for address, position, count in ((MATRIX, 0xD4E10, 40), (TAIL, 0xD4EB0, 5),
                                         (CONTINUATION, 0xD4EC4, 13)):
            cls.connected.update(zip(range(address, address + count * 4, 4),
                                     struct.unpack_from('>%dI' % count, rom, position)))
        cls.coverage = set()
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = r'''
typedef unsigned char u8;typedef unsigned int u32;typedef int s32;typedef float f32;
#define NULL ((void *)0)
typedef struct {f32 unk0,unk4,unk8;u32 guard[5];} struct17;
typedef struct {u8 pad0[12];f32 unkC,unk10;u8 pad14[32];
    f32 unk34,unk38;u8 pad3C[324];} struct140;
typedef char check_view_size[sizeof(struct140)==384 ? 1 : -1];
typedef char check_pointer_size[sizeof(void *)==4 ? 1 : -1];
''' + screen.DECLARATIONS + r'''
s32 D_800D9D10[4096],D_800BE628;
f32 D_800A56B0=6000.0f,D_800D9B20;
static struct17 point;
static struct140 views[256];
static f32 xyStorage[8],outputs[8];
static u32 logWords[8],savedLog[8],snapshot[136];
static f32 *xy,*z,*w,*inverse;
static int activeIndex,activeMask,calls;
static u32 word(f32 value) {union {f32 f;u32 u;} b;b.f=value;return b.u;}
static f32 axis(f32 *m,int i,f32 x,f32 y,f32 z) {
    f32 a=m[i]*x,b=m[i+4]*y,c=m[i+8]*z;
    f32 ab=a+b,cd=c+m[i+12];return ab+cd;
}
void func_150A7A00(f32 matrix[4][4],f32 x,f32 y,f32 z,
                 f32 *outX,f32 *outY,f32 *outZ,f32 *outW) {
    f32 *m=&matrix[0][0],a=axis(m,0,x,y,z),b=axis(m,1,x,y,z),c=axis(m,2,x,y,z);
    logWords[0]=(u32)m;logWords[1]=word(x);logWords[2]=word(y);logWords[3]=word(z);
    logWords[4]=(u32)outX;logWords[5]=(u32)outY;logWords[6]=(u32)outZ;logWords[7]=(u32)outW;
    calls++;*outX=a;*outY=b;*outZ=c;*outW=axis(m,3,x,y,z);
}
static void reset(int index,int mask,int layout,int pattern) {
    int i;f32 *m=(f32 *)(D_800D9D10+index*16);
    struct140 *v=views+index;u32 *p=(u32 *)&point;
    activeIndex=index;activeMask=mask;calls=0;
    for(i=0;i<8;i++) {p[i]=0xA5A5A5A5;((u32 *)xyStorage)[i]=0xA5A5A5A5;((u32 *)outputs)[i]=0xA5A5A5A5;}
    for(i=0;i<96;i++) ((u32 *)v)[i]=0xA5A5A5A5;
    point.unk0=2.0f;point.unk4=3.0f;point.unk8=4.0f;
    for(i=0;i<16;i++) m[i]=(i==0 || i==5 || i==10)?1.0f:0.0f;
    m[15]=pattern==0?2.0f:pattern==1?6000.0f:pattern==2?-2.0f:pattern==3?0.0f:0.25f;
    D_800D9B20=pattern==3?-4.0f:0.0f;
    v->unkC=2.0f;v->unk10=3.0f;v->unk34=11.0f;v->unk38=37.0f;
    D_800BE628=(s32)views;
    xy=xyStorage;z=outputs;w=outputs+1;inverse=outputs+2;
    if(layout==1) inverse=xy;
    if(layout==2) inverse=xy+1;
    if(layout==3) z=xy;
    if(layout==4) w=xy+1;
    if(layout==5) z=w;
    if(layout==6) xy=&v->unk10;
    if(layout==7) xy=m+3;
    if(layout==8) xy=&point.unk0;
    if(mask&1) z=NULL;
    if(mask&2) w=NULL;
    if(mask&4) inverse=NULL;
}
static s32 reference(void) {
    f32 scratch[3],*outZ=z?z:scratch,*outW=w?w:scratch+1,*inv=inverse?inverse:scratch+2;
    f32 depth,oldX,oldY,sx,sy,offsetX,xp,yp,newX;
    struct140 *v;
    func_150A7A00((f32 (*)[4])(D_800D9D10+activeIndex*16),
        point.unk0,point.unk4,point.unk8,xy,xy+1,outZ,outW);
    depth=*outW;
    if(D_800A56B0<=depth) return 0;
    if(depth<=D_800D9B20) return 0;
    if(depth==0.0f) return 0;
    *inv=1.0f/depth;
    v=(struct140 *)((u8 *)D_800BE628+activeIndex*384);
    oldX=xy[0];oldY=xy[1];sx=v->unkC+5.0f;sy=v->unk10+5.0f;offsetX=v->unk34;
    xp=oldX*sx;yp=oldY*sy;newX=*inv*xp;newX=newX+offsetX;xy[0]=newX;
    v=(struct140 *)((u8 *)D_800BE628+activeIndex*384);
    xy[1]=v->unk38-*inv*yp;return 1;
}
static int capture(int compare) {
    u32 *parts[5]={(u32 *)&point,(u32 *)xyStorage,(u32 *)outputs,
        (u32 *)(D_800D9D10+activeIndex*16),(u32 *)(views+activeIndex)};
    int lengths[5]={8,8,8,16,96},i,j,k=0;
    for(i=0;i<5;i++) for(j=0;j<lengths[i];j++,k++) {
        if(compare && snapshot[k]!=parts[i][j]) return 1;
        if(!compare) snapshot[k]=parts[i][j];
    }
    for(i=0;i<8;i++) {
        if(i==6 && (activeMask&1)) continue;
        if(i==7 && (activeMask&2)) continue;
        if(compare && savedLog[i]!=logWords[i]) return 2;
        if(!compare) savedLog[i]=logWords[i];
    }
    return 0;
}
''' + screen.SELECTED + '\n'

    def pair(self, memory, args, actions=(), phase=0):
        expected, writes, calls, status = reference(memory, args, actions, phase)
        models = [ProjectionOracle(words, memory, args, self.connected, phase, actions).run()
                  for words in (self.retail, self.words)]
        for model in models:
            self.assertEqual(external(model.memory), external(expected))
            actual = [e for e in model.events if e[0] == 'W' and not private(e[1])]
            self.assertEqual(actual, writes)
            self.assertEqual(model.calls, calls)
            self.assertEqual(model.r[2], status)
        self.coverage.update(models[0].visits)
        return models

    def test_compiler_receipts_preserve_explicit_nonmatch(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']),
                         (102, 72, 46))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertFalse(self.record['exact'])
        self.assertEqual(self.words[:17], self.retail[:17])
        self.assertEqual(self.words[-5:], self.retail[-5:])
        self.assertEqual(len(list(screen.lifetime_candidates())), 140)
        self.assertEqual(len({n for n, _, _ in screen.lifetime_candidates()}), 140)

    def test_all_byte_indices_optional_outputs_and_aliases(self):
        cases = 0
        for index, mask, layout, phase in itertools.product(range(256), range(8), range(9), (0, 8)):
            memory, args, actions = fixture(index, mask, layout, phase=phase)
            self.pair(memory, args, actions, phase)
            cases += 1
        self.assertEqual(cases, 36864)

    def test_depth_limits_zero_and_lazy_views(self):
        for depth, lower, mask, phase in itertools.product(
                (-2.0, -0.0, 0.0, 0.25, 2.0, 5999.5, 6000.0, 6001.0),
                (-4.0, 0.0, 0.5), range(8), (0, 8)):
            memory, args, actions = fixture(mask=mask, depth=depth, lower=lower, phase=phase)
            rejected = 6000.0 <= depth or depth <= lower or depth == 0.0
            if rejected:
                for a in list(memory):
                    if VIEW <= a < VIEW + 384 or ALTERNATE <= a < ALTERNATE + 384 or a == VIEW_WORD:
                        del memory[a]
            if depth >= 6000.0:
                for a in range(LOWER, LOWER + 4):
                    del memory[a]
            self.pair(memory, args, actions, phase)
        self.assertEqual(len(self.coverage & set(self.connected)), 58)
        self.assertEqual(set(range(ENTRY, ENTRY + 404, 4)) - self.coverage, {ENTRY + 0xD8})
        self.assertEqual(self.retail[0xD8 // 4], 0x44804000)

    def test_post_helper_index_home_is_live_and_unsigned(self):
        for index, phase in itertools.product(range(256), (0, 8)):
            self.pair(*fixture(index=index, phase=phase, new_index=index ^ 255), phase=phase)

    def test_required_inputs_coefficients_bounds_and_outputs_fail_closed(self):
        required = (POINT, BANK, BANK + 12, UPPER, LOWER, VIEW_WORD,
                    VIEW + 12, VIEW + 16, VIEW + 52, VIEW + 56, XY, OUTPUT + 8)
        for address, words in itertools.product(required, (self.retail, self.words)):
            memory, args, actions = fixture()
            for a in range(address, address + 4):
                del memory[a]
            with self.assertRaises((AssertionError, KeyError), msg=hex(address)):
                ProjectionOracle(words, memory, args, self.connected, actions=actions).run()

    def test_live_view_base_and_inverse_reads_after_x_store(self):
        for phase, mask in itertools.product((0, 8), (0, 1, 2, 3)):
            self.pair(*fixture(mask=mask, layout=9, phase=phase), phase=phase)
        memory, args, actions = fixture(layout=1)
        models = self.pair(memory, args, actions)
        # X overwrites the reciprocal; the second coordinate must use that new value.
        self.assertEqual(floating(peek(models[0].memory, XY + 4)), 37.0 - 12.75 * 24.0)

    def test_late_y_scale_negative_has_real_output_failure(self):
        memory, args, actions = fixture(layout=6)
        retail, selected = self.pair(memory, args, actions)
        wrong = ProjectionOracle(self.late_y, memory, args, self.connected).run()
        self.assertEqual((self.wrong_record['body_words'], self.wrong_record['frame'],
                          self.wrong_record['differences']), (102, 72, 44))
        self.assertEqual(floating(peek(retail.memory, args[1] + 4)), 26.5)
        self.assertEqual(floating(peek(selected.memory, args[1] + 4)), 26.5)
        self.assertEqual(floating(peek(wrong.memory, args[1] + 4)), 2.5)
        self.assertNotEqual(external(retail.memory), external(wrong.memory))

    def test_matrix_xyz_stores_affect_w_continuation(self):
        memory, args, actions = fixture(layout=7)
        model, _ = self.pair(memory, args, actions)
        # X overwrites m[3], so W becomes 2*2+2 rather than the seeded 2.
        self.assertEqual(floating(peek(model.memory, OUTPUT + 4)), 6.0)
        self.assertEqual(model.calls[0][1], BANK)

    def test_compiled_cached_inverse_and_view_controls_fail_real_aliases(self):
        for name, layout in (('cached-inverse', 1), ('cached-view', 9)):
            memory, args, actions = fixture(layout=layout)
            retail, _ = self.pair(memory, args, actions)
            wrong = ProjectionOracle(self.stale[name], memory, args, self.connected, actions=actions).run()
            self.assertNotEqual(external(retail.memory), external(wrong.memory), name)
            self.assertNotEqual(peek(retail.memory, args[1] + 4), peek(wrong.memory, args[1] + 4), name)

    def test_actual_32bit_c_all_indices_outputs_aliases_and_depth_paths(self):
        self.run_host(r'''
int index,mask,layout,pattern,cases=0; s32 expected,actual;
for(index=0;index<256;index++) for(mask=0;mask<8;mask++)
for(layout=0;layout<9;layout++) for(pattern=0;pattern<5;pattern++) {
    reset(index,mask,layout,pattern);expected=reference();
    if(calls!=1 || capture(0)) return 1;
    reset(index,mask,layout,pattern);
    actual=func_15144CEC(&point,xy,z,w,inverse,(u8)index);
    if(actual!=expected || calls!=1 || capture(1) || D_800BE628!=(s32)views) return 2;
    cases++;
}
if(cases!=92160) return 3;
''')


if __name__ == '__main__':
    unittest.main()
