"""Actor-reference coordinate phase, fresh float bounds and five-argument calls."""

import csv
import itertools
import re
import shutil
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_actor_attachment_phase_candidates as screen
from tools.match_progress import load_elf_functions
from tools import pad_generated_object as pad
from tools.tests import test_game_actor_update_pass_match as actor_pass
from tools.tests import test_game_table_range_loader as table
from tools.tests.game_animation_timeline_oracle import bits, floating

ENTRY, TRANSFORM = 0x1502F3C8, 0x1502F490
ACTORS, STRIDE, STACK = actor_pass.ACTORS, actor_pass.STRIDE, table.STACK
FLOATS = (0xC0A00000, 0xBF800000, 0, 0x80000000, 0x3F800000,
          0x40A00000, 0x7F800000, 0xFF800000, 0x7FC12345)


def memory_case(active=1, reference=1, joint=0, bound=bits(3.5), slot=0):
    memory = actor_pass.memory_case()
    for i in range(26):
        for offset, value, size in ((0, active if i == slot else 0, 4),
                (0x274, reference if i == slot else 0, 1), (0x19E, joint, 2),
                (0x14, bits(1.25), 4), (0x18, bits(-2.5), 4),
                (0x1C, bits(4.75), 4), (0x180, bound, 4)):
            actor_pass.dispatch.put(memory, ACTORS + i * STRIDE + offset, value, size)
    return memory


def transform_hook(model):
    target, x, y, z, joint = model.arguments(5)
    assert x % STRIDE == (ACTORS + 0x14) % STRIDE and y == x + 4 and z == y + 4
    assert joint <= 65535
    slot = (x - ACTORS - 0x14) // STRIDE
    assert 0 <= slot < 25
    model.observed.append((slot, target, joint, model.peek(y, 4)))
    for address, value in ((x, bits(12.25)), (y, model.result), (z, bits(-14.75))):
        model.put(address, value, 4)
    if model.bound is not None:
        model.put(ACTORS + slot * STRIDE + 0x180, model.bound, 4)
    for address, value, size in model.actions.get((TRANSFORM, slot), ()):
        model.put(address, value, size)
    for register in (1, 2, 3, *range(4, 16), 24, 25):
        model.r[register] = 0xA5000000 + register
    model.f[:20] = [0xA5000000 + i for i in range(20)]


class PhaseOracle(table.RangeOracle):
    def __init__(self, words, memory, phase=0, result=bits(5.5), bound=None, actions=None, connected=None):
        super().__init__(words, memory, (), phase, connected=connected, entry=ENTRY)
        self.result, self.bound, self.actions = result, bound, actions or {}
        self.observed = []
        self.f[20:] = [0x3F800000 + i for i in range(20, 32)]
        self.saved_f = self.f[20:].copy()

    def execute(self, word):
        op, rs, rt = word >> 26, word >> 21 & 31, word >> 16 & 31
        if op in (53, 61):
            immediate = word & 65535
            address = (self.r[rs] + (immediate if immediate < 32768 else immediate - 65536)) & 0xFFFFFFFF
            assert rt % 2 == 0 and address % 8 == 0
            # FR=0 pairs put the odd register's high word first in big-endian memory.
            if op == 61:
                self.put(address, (self.f[rt + 1] << 32) | self.f[rt], 8)
            else:
                value = self.get(address, 8)
                self.f[rt], self.f[rt + 1] = value & 0xFFFFFFFF, value >> 32
        else:
            super().execute(word)

    def run(self):
        result = super().run()
        assert self.f[20:] == self.saved_f, 'saved floating registers'
        return result

    def record_call(self, target):
        assert target == TRANSFORM
        args = self.arguments(5)
        self.calls.append((target, *args))
        self.events.append(('CALL', target, args))

    def hook(self, target):
        assert target == TRANSFORM
        transform_hook(self)


class ConnectedPassOracle(actor_pass.PassOracle):
    def record_call(self, target):
        if target == TRANSFORM:
            args = self.arguments(5)
            self.calls.append((target, *args))
            self.events.append(('CALL', target, args))
        else:
            super().record_call(target)

    def hook(self, target):
        if target == TRANSFORM:
            transform_hook(self)
        else:
            super().hook(target)


class GameActorAttachmentPhaseMatchTests(unittest.TestCase):
    run_host = table.native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').exists() or any(shutil.which(n) is None
                for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-actor-attachment-phase-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected', screen.SELECTED)
        _, cls.baseline = screen.compile_candidate(cls.root, cls.output, 'baseline', screen.BASELINE)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>50I', rom, 0x5C878))
        cls.transform = list(struct.unpack_from('>302I', rom, 0x5C940))
        cls.caller = list(struct.unpack_from('>176I', rom, 0x59394))
        cls.dispatcher = list(struct.unpack_from('>88I', rom, 0x59234))
        cls.selector = list(struct.unpack_from('>35I', rom, 0x6CE14))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = ('''typedef unsigned char u8; typedef unsigned short u16;
typedef unsigned int u32; typedef int s32; typedef float f32;
''' + screen.DECLARATIONS + '''
ActorAttachment58F80 D_800CC2D0[26];
#define D_800D121C (D_800CC2D0 + 25)
typedef union {u32 word;f32 value;} FloatBits;
static int mode,logCount,error;
static u32 result,bound,log[25][4];
static f32 value(u32 word) {FloatBits b;b.word=word;return b.value;}
static u32 word(f32 v) {FloatBits b;b.value=v;return b.word;}
s32 func_1502F490(ActorAttachment58F80 *target,f32 *x,f32 *y,f32 *z,s32 joint) {
    int slot=(int)(((u8 *)x-(u8 *)D_800CC2D0-0x14)/0x32C);
    if(slot<0 || slot>=25 || joint<0 || joint>65535) error=1;
    log[logCount][0]=(u32)(target-D_800CC2D0);
    log[logCount][1]=(u32)slot;log[logCount][2]=(u32)joint;log[logCount++][3]=word(*y);
    *x=12.25f;*y=value(result);*z=-14.75f;
    if(mode&1) D_800CC2D0[slot].boundY=value(bound);
    if(mode&2 && slot==0) {D_800CC2D0[1].active=1;D_800CC2D0[1].reference=26;}
    return -1;
}
static void reset(int pattern) {
    int i;u8 *p=(u8 *)D_800CC2D0;
    for(i=0;i<(int)sizeof(D_800CC2D0);i++) p[i]=0xA5;
    for(i=0;i<26;i++) {
        D_800CC2D0[i].active=((pattern>>(i%8))&1)?-1:0;
        D_800CC2D0[i].reference=(u8)((pattern+i)%27);
        D_800CC2D0[i].joint=(u16)(pattern*65521+i*32769);
        D_800CC2D0[i].x=1.25f;D_800CC2D0[i].y=-2.5f;D_800CC2D0[i].z=4.75f;
        D_800CC2D0[i].boundY=value(bound);
    }
    if(mode&2) {D_800CC2D0[0].active=1;D_800CC2D0[0].reference=1;D_800CC2D0[1].active=0;}
    logCount=error=0;
}
static void reference(void) {
    int i;
    for(i=0;i<25;i++) if(D_800CC2D0[i].active && D_800CC2D0[i].reference) {
        ActorAttachment58F80 *p=D_800CC2D0+i;
        p->y=p->boundY;
        func_1502F490(D_800CC2D0+(p->reference-1),&p->x,&p->y,&p->z,p->joint);
        if(!(p->y<p->boundY)) p->boundY=p->y;
        else p->y=p->boundY;
    }
}
''' + screen.SELECTED + '\n')

    def models(self, memory, phase=0, result=bits(5.5), bound=None, actions=None, connected=None):
        models = [PhaseOracle(w, memory, phase, result, bound, actions, connected).run()
                  for w in (self.retail, self.words, self.baseline)]
        for model in models[1:]:
            self.assertEqual(actor_pass.external_memory(model.memory), actor_pass.external_memory(models[0].memory))
            self.assertEqual(actor_pass.external_events(model), actor_pass.external_events(models[0]))
        return models[0]

    def test_compiler_linked_slot_and_guarded_boundary(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']),
                         (50, 0x30, 16))
        self.assertEqual(self.record['diagnostics'], '')
        source = (self.root / 'conker/src/game/generated_58F80.c').read_text()
        body = re.search(r'void func_1502F3C8\(void\) \{\n.*?\n\}', source, re.S).group(0)
        self.assertEqual(body, screen.production_body())
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1502F3C8'], ENTRY)
        self.assertEqual(functions['func_1502F3C8'], self.retail)
        # Full semantic recovery is qualified separately; it is not byte-exact.
        from tools.experiments import game_actor_triangle_transform_candidates as transform
        _, recovered = transform.compile_candidate(self.root, self.output, 'recovered-transform', transform.SELECTED)
        self.assertEqual(functions['func_1502F490'], recovered)

    def test_word_and_relocation_guards_fail_closed(self):
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            reader = csv.DictReader(file)
            fields = reader.fieldnames
            rows = [r for r in reader if r['function'] == 'func_1502F3C8']
        self.assertEqual([int(r['offset'], 0) for r in rows], [d[0] for d in self.record['differences']])
        self.assertEqual(len(rows), 16)
        self.assertTrue(all(r['filename'] == 'generated_58F80' and r['omit'] == 'false'
                            and not r['insert_after'] and not r['insert_after_relocations'] for r in rows))
        assembly = (self.root / 'conker/asm/58F80.s').read_text().split('glabel func_1502F3C8\n')[1].split('endlabel func_1502F3C8')[0]
        retail = self.path / 'phase.s'
        retail.write_text('glabel func_1502F3C8\n' + assembly + 'endlabel func_1502F3C8\n')
        patches = self.path / 'phase.csv'

        def emit(values):
            with patches.open('w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(values)
            return pad.emit_padded_assembly(self.output / 'selected.o', retail,
                                            word_patches_path=patches, filename='generated_58F80')

        self.assertIn('func_1502F3C8', emit(rows))
        altered = [dict(r) for r in rows]
        altered[0]['expected'] = hex(int(altered[0]['expected'], 0) ^ 1)
        with self.assertRaisesRegex(ValueError, 'stale word patch'):
            emit(altered)
        altered = [dict(r) for r in rows]
        altered[2]['expected_relocations'] = 'R_MIPS_HI16:D_800D121C'
        with self.assertRaisesRegex(ValueError, 'stale relocations'):
            emit(altered)

    def test_all_reference_bytes_joint_extension_and_reserved_slot(self):
        count, coverage = 0, set()
        for reference, joint, phase in itertools.product(range(256), (0, 1, 0x8000, 65535), (0, 8)):
            model = self.models(memory_case(-1, reference, joint, slot=24), phase)
            expected = [] if reference == 0 else [(TRANSFORM, ACTORS + (reference - 1) * STRIDE,
                       ACTORS + 24 * STRIDE + 0x14, ACTORS + 24 * STRIDE + 0x18,
                       ACTORS + 24 * STRIDE + 0x1C, joint)]
            self.assertEqual(model.calls, expected)
            coverage.update(model.visits)
            count += 1
        self.assertEqual(count, 2048)
        self.assertEqual(set(range(ENTRY, ENTRY + 200, 4)) - coverage, {0x1502F45C, 0x1502F460, 0x1502F464})
        memory = memory_case(slot=25)
        self.assertEqual(self.models(memory).calls, [])
        self.assertEqual(actor_pass.external_memory(self.models(memory).memory), actor_pass.external_memory(memory))

    def test_float_order_nan_signed_zero_and_fresh_callback_bound(self):
        count, coverage = 0, set()
        for initial, result, bound, phase in itertools.product(FLOATS, FLOATS, FLOATS, (0, 8)):
            model = self.models(memory_case(bound=initial), phase, result, bound)
            expected_y, expected_bound = (bound, bound) if floating(result) < floating(bound) else (result, result)
            self.assertEqual(model.peek(ACTORS + 0x18, 4), expected_y)
            self.assertEqual(model.peek(ACTORS + 0x180, 4), expected_bound)
            self.assertEqual(model.observed, [(0, ACTORS, 0, initial)])
            coverage.update(model.visits)
            count += 1
        self.assertEqual(count, 1458)
        self.assertEqual(set(range(ENTRY, ENTRY + 200, 4)) - coverage, {0x1502F410, 0x1502F464})

    def test_live_next_actor_eligibility_after_transform(self):
        memory = memory_case()
        actions = {(TRANSFORM, 0): ((ACTORS + STRIDE, 1, 4),
                   (ACTORS + STRIDE + 0x274, 26, 1), (ACTORS + STRIDE + 0x19E, 65535, 2))}
        model = self.models(memory, actions=actions)
        self.assertEqual([c[1] for c in model.calls], [ACTORS, ACTORS + 25 * STRIDE])
        memory = memory_case()
        actor_pass.dispatch.put(memory, ACTORS + STRIDE, 1, 4)
        actor_pass.dispatch.put(memory, ACTORS + STRIDE + 0x274, 1, 1)
        model = self.models(memory, actions={(TRANSFORM, 0): ((ACTORS + STRIDE, 0, 4),)})
        self.assertEqual(len(model.calls), 1)

    def test_cached_bound_negative_control_fails_despite_retail_word_length(self):
        body = dict(screen.candidates())['cached-bound-negative-control']
        record, words = screen.compile_candidate(self.root, self.output, 'wrong-cached-bound', body)
        self.assertEqual(record['real_differences'], 39)
        memory = memory_case(bound=bits(1.0))
        correct = PhaseOracle(self.retail, memory, result=bits(2.0), bound=bits(3.0)).run()
        wrong = PhaseOracle(words, memory, result=bits(2.0), bound=bits(3.0)).run()
        self.assertNotEqual(actor_pass.external_memory(correct.memory), actor_pass.external_memory(wrong.memory))

    def test_omitted_joint_negative_control_reaches_real_callee_with_wrong_stack_word(self):
        body = dict(screen.candidates())['omitted-joint-negative-control']
        self.assertNotEqual(body, screen.BASELINE)
        _, words = screen.compile_candidate(self.root, self.output, 'wrong-omitted-joint', body)
        connection = {TRANSFORM + i * 4: w for i, w in enumerate(self.transform)}
        memory = memory_case(joint=65535)
        memory.update({0x800C6070 + i: 0 for i in range(256 * 4)})
        correct = PhaseOracle(self.retail, memory, connected=connection).run()
        wrong = PhaseOracle(words, memory, connected=connection).run()
        self.assertIn(0x1502F4D4, wrong.visits)
        self.assertEqual(correct.calls[0][-1], 65535)
        self.assertNotEqual(wrong.calls[0][-1], correct.calls[0][-1])
        self.assertNotEqual(wrong.calls, correct.calls)

    def test_actual_transform_zero_table_path_consumes_all_five_arguments(self):
        connection = {TRANSFORM + i * 4: w for i, w in enumerate(self.transform)}
        count = 0
        for reference, joint, phase in itertools.product((1, 2, 25, 26), (0, 1, 0x8000, 65535), (0, 8)):
            memory = memory_case(reference=reference, joint=joint)
            memory.update({0x800C6070 + i: 0 for i in range(256 * 4)})
            model = self.models(memory, phase, connected=connection)
            self.assertIn(0x1502F4D4, model.visits)
            self.assertIn((STACK + phase - 0x30 + 0x10, 4, joint), model.reads)
            self.assertEqual(model.peek(ACTORS + 0x18, 4), bits(3.5))
            count += 1
        self.assertEqual(count, 32)

    def test_actual_caller_selector_dispatcher_and_phase_connected(self):
        _, selected = actor_pass.screen.compile_candidate(self.root, self.output, 'caller', actor_pass.screen.SELECTED)
        _, baseline = actor_pass.screen.compile_candidate(self.root, self.output, 'caller-baseline', actor_pass.screen.BASELINE)
        count = 0
        for start, enabled, phase, result in itertools.product(range(25), (0, 1), (0, 8), FLOATS[:3]):
            memory = memory_case()
            for slot in (0, 1, 2):
                for offset, value, size in ((0, 1, 4), (0x65, slot, 1), (0x274, slot + 1, 1),
                                           (0xF8, 0, 4), (0x260, 0, 4), (0x1D4, 0, 4)):
                    actor_pass.dispatch.put(memory, ACTORS + slot * STRIDE + offset, value, size)
            actor_pass.dispatch.put(memory, actor_pass.CURRENT, start, 1)
            actor_pass.dispatch.put(memory, actor_pass.ENABLE, enabled, 1)
            models = []
            for caller, helper in ((self.caller, self.retail), (selected, self.words), (baseline, self.baseline)):
                connection = {ENTRY + i * 4: w for i, w in enumerate(helper)}
                connection.update({actor_pass.UPDATE + i * 4: w for i, w in enumerate(self.dispatcher)})
                connection.update({actor_pass.SELECTOR + i * 4: w for i, w in enumerate(self.selector)})
                model = ConnectedPassOracle(caller, memory, phase, connected=connection)
                model.result, model.bound, model.observed = result, bits(1.0), []
                models.append(model.run())
            for model in models[1:]:
                self.assertEqual(actor_pass.external_memory(model.memory), actor_pass.external_memory(models[0].memory))
                self.assertEqual(actor_pass.external_events(model), actor_pass.external_events(models[0]))
            self.assertEqual(len(models[0].observed), 3)
            count += 1
        self.assertEqual(count, 300)

    def test_native_reference_full_records_and_live_mutations(self):
        self.run_host('''
static ActorAttachment58F80 expected[26];static u32 expectedLog[25][4];
static const u32 values[]={0xC0A00000,0xBF800000,0,0x80000000,0x3F800000,0x40A00000,0x7F800000,0xFF800000,0x7FC12345};
int pattern,a,b,i,j,n,cases=0;u8 *left,*right;
if(sizeof(ActorAttachment58F80)!=0x32C || __builtin_offsetof(ActorAttachment58F80,y)!=0x18
   || __builtin_offsetof(ActorAttachment58F80,boundY)!=0x180
   || __builtin_offsetof(ActorAttachment58F80,joint)!=0x19E
   || __builtin_offsetof(ActorAttachment58F80,reference)!=0x274) return 1;
for(mode=0;mode<4;mode++) for(pattern=0;pattern<256;pattern++) for(a=0;a<9;a++) for(b=0;b<9;b++) {
    result=values[a];bound=values[b];reset(pattern);reference();n=logCount;
    for(i=0;i<n;i++) for(j=0;j<4;j++) expectedLog[i][j]=log[i][j];
    for(i=0;i<26;i++) expected[i]=D_800CC2D0[i];
    reset(pattern);func_1502F3C8();
    if(error || logCount!=n) return 2;
    for(i=0;i<n;i++) for(j=0;j<4;j++) if(expectedLog[i][j]!=log[i][j]) return 3;
    left=(u8 *)expected;right=(u8 *)D_800CC2D0;
    for(i=0;i<(int)sizeof(expected);i++) if(left[i]!=right[i]) return 4;
    cases++;
}
if(cases!=82944) return 5;
return 0;
''')


if __name__ == '__main__':
    unittest.main()
