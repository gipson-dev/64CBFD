"""Actor scan C and retail instructions; renderer callbacks are opaque fixtures."""

import csv
import hashlib
import itertools
import random
import re
import shutil
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_actor_display_scan_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests import test_game_table_range_loader as table
from tools.tests.test_game_dual_matrix_emitter import sdk_macro
from tools.tests.game_animation_timeline_oracle import signed


ENTRY, ACTORS, STRIDE, DIAG = 0x1502BAD0, 0x800CC2D0, 0x32C, 0x8003C8E0
ALPHA, SPECIAL, GENERIC, FOLLOWUP, FINAL = 0x1506196C, 0x1502C408, 0x1502C974, 0x150368C4, 0x15030E08
OUTPUT, OTHER, STACK = table.BUFFER, table.BUFFER + 0x2000, table.STACK
COUNTS = {ALPHA: 2, SPECIAL: 2, GENERIC: 5, FOLLOWUP: 3, FINAL: 3}
MODES = (-1, 0, 1, 2, 3, 4, 5, 6, 7)
VIEWS = (0, 1, -1, 0x7FFF, 0x8000, 0xFFFF, 0x12340001, 0x5678FFFF)
ALPHAS = (-0x80000000, -1, 0, 254, 255, 256, 0x7FFFFFFF)
GUARDS = {
    0x070: (0x24170007, 0x24170001), 0x074: (0x24160001, 0x24160007),
    0x0BC: (0x54540006, 0x56820006), 0x0E8: (0x5057002C, 0x52C2002C),
    0x11C: (0x1676000E, 0x1677000E), 0x124: (0x50570031, 0x52C20031),
    0x12C: (0x5056002F, 0x52E2002F), 0x160: (0x5054000E, 0x5282000E),
    0x168: (0x50570020, 0x52C20020), 0x178: (0x5456001C, 0x56E2001C),
    0x204: (0x16760007, 0x16770007),
}


def source_body():
    return dict(screen.candidates())['selected-active-state']


def guarded(words, omitted=None):
    words = words[:]
    for offset, (expected, replacement) in GUARDS.items():
        assert words[offset // 4] == expected, ('stale actor-scan guard', offset)
        if offset != omitted:
            words[offset // 4] = replacement
    return words


def actor_put(memory, slot, active=1, state=0, identity=0, flags=0x200):
    address = ACTORS + slot * STRIDE
    table.lookup.put_word(memory, address, active)
    memory[address + 4], memory[address + 5] = identity, state
    table.lookup.put_word(memory, address + 0x184, flags)


def memory_case(rows=()):
    memory = {STACK + i: 0xA5 for i in range(-0x100, 0x80)}
    memory.update({ACTORS + i: 0xA5 for i in range(-16, 26 * STRIDE + 16)})
    memory.update({DIAG + i: 0xA5 for i in range(-8, 12)})
    for base in (OUTPUT, OTHER):
        memory.update({base + i: 0xA5 for i in range(-16, 0x1010)})
    for i in range(26):
        actor_put(memory, i, active=0)
    for i, row in enumerate(rows):
        actor_put(memory, i, **row)
    # The 26th table entry is deliberately active and must not be visited.
    actor_put(memory, 25, active=-1, state=7)
    return memory


def visible(active, state, identity, flags, mode, alpha):
    """Independent predicate, including the asymmetric signed alpha tests."""
    if not active or state in (3, 5):
        return False
    if state == 2:
        return mode == 2
    if identity == 255:
        return False
    if mode == 0:
        return bool(flags & 0x200)
    if mode == 6:
        return state == 7
    if mode == 1:
        return state not in (1, 7) and (state != 0 or alpha >= 255)
    if mode == 2:
        return state in (0, 1) and (state != 0 or alpha != 255)
    return True


class ActorOracle(table.RangeOracle):
    def __init__(self, words, memory, mode=0, view=0, phase=0, alpha=255,
                 mutation=0, advance=8, redirect=False):
        super().__init__(words, memory, (OUTPUT, mode, view), phase, entry=ENTRY)
        self.alpha, self.mutation = alpha, mutation
        self.advance, self.redirect = advance, redirect
        self.receipts = []

    def record_call(self, target):
        args = self.arguments(COUNTS[target])
        self.calls.append((target, *args))
        self.events.append(('CALL', target, args, self.peek(DIAG, 4)))
        self.receipts.append((target, args, self.peek(DIAG, 4)))

    def hook(self, target):
        args = self.arguments(COUNTS[target])
        if target == ALPHA:
            slot = (args[0] - ACTORS) // STRIDE
            assert args[0] == ACTORS + slot * STRIDE and 0 <= slot < 25
            if self.mutation in (1, 2):
                self.put(args[0], 0, 4)
                self.put(args[0] + 4, 255, 1)
                self.put(args[0] + 5, 2 if self.mutation == 1 else 7, 1)
                self.put(args[0] + 0x184, 0, 4)
            if self.mutation == 3 and slot == 0:
                self.put(ACTORS + STRIDE, 0xFFFFFFFF, 4)
                self.put(ACTORS + STRIDE + 5, 1, 1)
            result = self.alpha
        else:
            destination = args[0]
            for i in range(self.advance // 8):
                self.put(destination + i * 8, target, 4)
                self.put(destination + i * 8 + 4, 0xCA110000 | i, 4)
            result = OTHER if self.redirect and target == GENERIC and args[1] == 0 else destination + self.advance
            if self.mutation == 4 and target == GENERIC and args[1] == 0:
                self.put(ACTORS + 5, 2, 1)
                self.put(ACTORS + STRIDE, 1, 4)
                self.put(ACTORS + STRIDE + 5, 7, 1)
            if self.mutation == 5:
                self.put(DIAG, 0xDEADBEEF, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result & 0xFFFFFFFF


class GameActorDisplayScanMatchTests(unittest.TestCase):
    run_host = table.native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or any(shutil.which(n) is None
                for n in ('mips-linux-gnu-ld', 'mips-linux-gnu-objdump')):
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.output = cls.root / 'conker/build/game-actor-display-scan-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.raw = screen.compile_candidate(cls.root, cls.output, 'selected', source_body())
        cls.words = guarded(cls.raw)
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>173I', cls.rom, 0x58F80))
        cls.coverage, cls.cases = set(), 0
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        types = ('typedef unsigned char u8; typedef short s16; typedef int s32; typedef unsigned int u32;\n'
                 'typedef struct { struct { u32 w0,w1; } words; } Gfx;\n')
        gbi = (cls.root / 'conker/include/2.0L/PR/gbi.h').read_text()
        mbi = (cls.root / 'conker/include/2.0L/PR/mbi.h').read_text()
        macros = sdk_macro(mbi, '_SHIFTL')
        for name in ('G_DL', 'G_DL_PUSH', 'gDma1p', 'gSPDisplayList'):
            macros += sdk_macro(gbi, name)
        cls.fixture = types + macros + screen.DECLARATIONS + r'''
ActorDisplay58F80 D_800CC2D0[26];
Gfx D_80084160[1],D_80084190[1];s32 D_8003C8E0;
static Gfx output[256],alternate[256],*cursor;
static s32 alphaValue,expectedView,expectedMode;
static int alphaCalls,specialCalls,genericCalls,followups,finals,error,mutation,step,redirect;
static int expectAlpha,expectSpecial,expectGeneric,expectFollowup,expectFinal;
static void reset(void) {
    int i;u8 *bytes=(u8 *)D_800CC2D0;
    for(i=0;i<(int)sizeof(D_800CC2D0);i++) bytes[i]=0xA5;
    for(i=0;i<26;i++) {D_800CC2D0[i].active=0;D_800CC2D0[i].id=0;D_800CC2D0[i].state=0;D_800CC2D0[i].flags=0x200;}
    D_800CC2D0[25].active=-1;D_800CC2D0[25].state=7;
    for(i=0;i<256;i++) {output[i].words.w0=output[i].words.w1=0xA5A5A5A5;alternate[i]=output[i];}
    alphaCalls=specialCalls=genericCalls=followups=finals=error=mutation=redirect=0;
    expectAlpha=expectSpecial=expectGeneric=expectFollowup=expectFinal=0;
    step=1;cursor=output+2;D_8003C8E0=-123;
}
static void checkView(s32 view) {if(view!=expectedView) error=1;}
static Gfx *packet(Gfx *commands,int target) {
    int i;if(commands!=cursor) error=2;
    for(i=0;i<step;i++) {commands[i].words.w0=(u32)target;commands[i].words.w1=0xCA110000+(u32)i;}
    cursor=commands+step;return cursor;
}
s32 func_1506196C(ActorDisplay58F80 *actor,s32 view) {
    int slot=(int)(actor-D_800CC2D0);checkView(view);alphaCalls++;
    if(slot<0 || slot>=25 || D_8003C8E0!=(0x1000000|slot)) error=3;
    if(mutation==1 || mutation==2) {actor->active=0;actor->id=255;actor->state=mutation==1?2:7;actor->flags=0;}
    if(mutation==3 && slot==0) {D_800CC2D0[1].active=-1;D_800CC2D0[1].state=1;}
    return alphaValue;
}
Gfx *func_1502C408(Gfx *commands,s32 slot) {
    specialCalls++;if(slot<0 || slot>=25 || D_8003C8E0!=(0x1000000|slot)) error=4;
    return packet(commands,0x1502C408);
}
Gfx *func_1502C974(Gfx *commands,s32 slot,s32 view,s32 mode,s32 zero) {
    checkView(view);genericCalls++;
    if(slot<0 || slot>=25 || D_8003C8E0!=(0x1000000|slot) || mode!=expectedMode || zero) error=5;
    packet(commands,0x1502C974);
    if(mutation==4 && slot==0) {D_800CC2D0[0].state=2;D_800CC2D0[1].active=1;D_800CC2D0[1].state=7;}
    if(redirect && slot==0) cursor=alternate+1;
    return cursor;
}
Gfx *func_150368C4(Gfx *commands,s32 slot,s32 view) {
    followups++;checkView(view);if(slot || D_8003C8E0!=0x1000000) error=6;
    return packet(commands,0x150368C4);
}
Gfx *func_15030E08(Gfx *commands,s32 view,s32 mode) {
    finals++;checkView(view);
    if(D_8003C8E0!=0x1FFFFFF || mode!=(expectedMode==1?0:expectedMode==2?1:2)) error=7;
    return packet(commands,0x15030E08);
}
static int admitted(ActorDisplay58F80 *a,s32 mode) {
    int st=a->state;
    if(!a->active || st==3 || st==5) return 0;
    if(st==2) return mode==2;
    if(a->id==255) return 0;
    switch(mode) {
        case 0:return (a->flags&0x200)!=0;
        case 6:return st==7;
        case 1:return st!=1 && st!=7 && (st!=0 || alphaValue>=255);
        case 2:return (st==0 || st==1) && (st!=0 || alphaValue!=255);
        default:return 1;
    }
}
static void predict(void) {
    int i;
    for(i=0;i<25;i++) {
        ActorDisplay58F80 *a=D_800CC2D0+i;
        if(a->active && a->id!=255 && a->state==0 && (expectedMode==1 || expectedMode==2)) expectAlpha++;
        if(admitted(a,expectedMode)) {
            if(a->state==2) expectSpecial++;
            else {expectGeneric++;if(i==0) expectFollowup++;}
        }
    }
    expectFinal=expectedMode==1 || expectedMode==2 || expectedMode==6;
}
''' + source_body() + r'''
static int check(s32 rawView) {
    Gfx *result;int count;
    expectedView=(s16)rawView;
    result=func_1502BAD0(output+1,expectedMode,(s16)rawView);
    if(error || result!=cursor+1 || D_8003C8E0 || alphaCalls!=expectAlpha || specialCalls!=expectSpecial
        || genericCalls!=expectGeneric || followups!=expectFollowup || finals!=expectFinal) return 1;
    if(output[1].words.w0!=0xDE000000 || output[1].words.w1!=(u32)D_80084160
        || cursor->words.w0!=0xDE000000 || cursor->words.w1!=(u32)D_80084190) return 2;
    if(output[0].words.w0!=0xA5A5A5A5 || output[0].words.w1!=0xA5A5A5A5) return 3;
    if(!redirect) {
        count=expectSpecial+expectGeneric+expectFollowup+expectFinal;
        if(result!=output+3+step*count || result->words.w0!=0xA5A5A5A5 || result->words.w1!=0xA5A5A5A5) return 4;
    }
    if(D_800CC2D0[25].active!=-1 || D_800CC2D0[25].state!=7) return 5;
    return 0;
}
'''

    def models(self, memory, **case):
        models = [ActorOracle(words, memory, **case).run() for words in (self.retail, self.raw, self.words)]
        for model in models[1:]:
            for field in ('memory', 'calls', 'events', 'reads', 'stores'):
                self.assertEqual(getattr(model, field), getattr(models[0], field), field)
            self.assertEqual(model.r[2], models[0].r[2])
        self.coverage.update(models[0].visits)
        type(self).cases += 1
        return models[0]

    def test_body_frame_guard_manifest_and_production_identity(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['real_differences']), (173, 0x48, 11))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words, self.retail)
        self.assertEqual(hashlib.sha256(struct.pack('>173I', *self.words)).hexdigest(),
                         '8a278075c83a3a64eeb495537f79a15a7fb32672d7f8881766e26a0f639b1060')
        self.assertEqual(len(screen.candidates()), 28)
        production = (self.root / 'conker/src/game/generated_58F80.c').read_text()
        body = re.search(r'Gfx \*func_1502BAD0\([^;{}]+\) \{\n.*?\n\}', production, re.S).group(0)
        body = re.sub(r'(?m)^ +/\*[^\n]+\*/\n', '', body)
        self.assertEqual(body, source_body())
        self.assertIn(screen.DECLARATIONS.strip(), production)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(functions['func_1502BAD0'], self.retail)
        self.assertEqual(addresses['func_1502BAD0'], ENTRY)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as file:
            rows = [r for r in csv.DictReader(file) if r['function'] == 'func_1502BAD0']
        self.assertEqual({int(r['offset'], 0): (int(r['expected'], 0), int(r['replacement'], 0)) for r in rows}, GUARDS)
        self.assertEqual(len(rows), 11)
        for r in rows:
            self.assertEqual(r['filename'], 'generated_58F80')
            self.assertEqual((r['expected_relocations'], r['replacement_relocations'], r['insert_after'], r['omit']), ('-', '-', '', 'false'))

    def test_closed_register_cycle_and_commutative_branches_only(self):
        self.assertEqual(self.raw[0x70 // 4:0x78 // 4], [0x24170007, 0x24160001])
        self.assertEqual(self.retail[0x70 // 4:0x78 // 4], [0x24170001, 0x24160007])
        for offset, (current, retail) in GUARDS.items():
            if offset in (0x70, 0x74):
                continue
            self.assertEqual(current >> 26, retail >> 26)
            self.assertIn(current >> 26, (4, 5, 20, 21))
            self.assertEqual(current & 65535, retail & 65535)
            rs, rt = current >> 21 & 31, current >> 16 & 31
            rs, rt = ({22: 23, 23: 22}.get(rs, rs), {22: 23, 23: 22}.get(rt, rt))
            expected = (retail >> 21 & 31, retail >> 16 & 31)
            self.assertIn(expected, ((rs, rt), (rt, rs)))
        # All uses of the two allocated constants, up to the epilogue, are accounted for.
        uses = set()
        for i in range(0x78 // 4, 0x280 // 4):
            word = self.raw[i]
            if word >> 26 in (4, 5, 20, 21) and {word >> 21 & 31, word >> 16 & 31} & {22, 23}:
                uses.add(i * 4)
        self.assertEqual(uses, {0xE8, 0x11C, 0x124, 0x12C, 0x168, 0x178, 0x204})

    def test_retained_placeholder_helpers_and_original_caller_slots_unchanged(self):
        functions, _, _ = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        for name, count, digest in (
                ('func_150195A0', 215, '7a5b146a4f6dcffaf14ac7cbb06f70a1cad7ca6d1c977bbe1253c2e39bebf3ae'),
                ('func_15019CC8', 102, '5c14b4747a1d12564ca7e4ead73a6e711a80b39ac27a026a341c2a8c7b3742b8'),
                ('func_1502C408', 128, 'facd7fdcd3492d98c4f0b25da438e5de8db734ac6ef3cc05af5a031a5157244b'),
                ('func_1502C974', 176, '0fec5b32d47b6d2b7a1045ba46ba1333914fddc792e91fab482c1dca76bab842')):
            words = functions[name]
            self.assertEqual(len(words), count, name)
            self.assertEqual(hashlib.sha256(struct.pack('>' + str(count) + 'I', *words)).hexdigest(), digest, name)
            self.assertEqual(words[:3], [0x00001025, 0x03E00008, 0])

    def test_shape_controls(self):
        for name, expected in (('baseline', (174, 0x48, 136)), ('signed-state', (173, 0x48, 35)),
                               ('placeholder', (3, 0, 169)), ('selected-one-first', (173, 0x48, 11)),
                               ('selected-mode-one-first', (172, 0x48, 160))):
            record, _ = screen.compile_candidate(self.root, self.output, name, dict(screen.candidates())[name])
            self.assertEqual((record['body_words'], record['frame'], record['real_differences']), expected, name)
            self.assertEqual(record['diagnostics'], '')

    def test_target_gate_matrix_with_independent_predicate(self):
        count = 0
        for mode, state, identity, flags, active, alpha in itertools.product(
                MODES, (0, 1, 2, 3, 4, 5, 6, 7, 255), (0, 255), (0, 0xFFFFFFFF), (0, -1), ALPHAS):
            row = dict(active=active, state=state, identity=identity, flags=flags)
            model = self.models(memory_case((row,)), mode=mode, alpha=alpha, view=0x5678FFFF)
            expected = []
            if active and state == 0 and identity != 255 and mode in (1, 2):
                expected.append((ALPHA, ACTORS, 0xFFFFFFFF))
            if visible(active, state, identity, flags, mode, alpha):
                expected.append((SPECIAL, OUTPUT + 8, 0) if state == 2 else (GENERIC, OUTPUT + 8, 0, 0xFFFFFFFF, mode & 0xFFFFFFFF, 0))
                if state != 2:
                    expected.append((FOLLOWUP, OUTPUT + 16, 0, 0xFFFFFFFF))
            cursor = OUTPUT + 8 + 8 * sum(c[0] != ALPHA for c in expected)
            if mode in (1, 2, 6):
                expected.append((FINAL, cursor, 0xFFFFFFFF, {1: 0, 2: 1, 6: 2}[mode]))
                cursor += 8
            self.assertEqual(model.calls, expected)
            self.assertEqual(model.r[2], cursor + 8)
            self.assertEqual([s[2] for s in model.stores if s[0] == DIAG], [0x1000000 | i for i in range(25)] + [0x1FFFFFF, 0])
            self.assertFalse(any(ACTORS + 25 * STRIDE <= a < ACTORS + 26 * STRIDE for a, _, _ in model.reads))
            count += 1
        self.assertEqual(count, 4536)

    def test_target_signed_view_frame_phase_and_all_slot_lifetimes(self):
        for mode, view, phase in itertools.product(MODES, VIEWS, (0, 8)):
            rows = [dict(active=-1, state=(0, 1, 2, 4, 7)[i % 5]) for i in range(25)]
            model = self.models(memory_case(rows), mode=mode, view=view, phase=phase, alpha=256)
            canonical = (view & 65535) - (65536 if view & 32768 else 0)
            for target, *args in model.calls:
                if target == ALPHA:
                    self.assertEqual(args[1], canonical & 0xFFFFFFFF)
                elif target != SPECIAL:
                    self.assertEqual(args[1 if target == FINAL else 2], canonical & 0xFFFFFFFF)
                if target == GENERIC:
                    self.assertEqual(args[-1], 0)
            for offset in (0x20, 0x24, 0x28, 0x2C, 0x30, 0x34, 0x38, 0x3C, 0x40, 0x44):
                address = STACK + phase - 0x48 + offset
                self.assertEqual(sum(a == address and size == 4 for a, size, _ in model.stores), 1)

    def test_target_callback_mutations_fresh_state_next_actor_and_retained_followup(self):
        for mode, mutation, alpha in itertools.product((1, 2), range(1, 5), (254, 255, 256)):
            model = self.models(memory_case((dict(state=0),)), mode=mode, alpha=alpha, mutation=mutation)
            passed = alpha >= 255 if mode == 1 else alpha != 255
            rendered = [c[0] for c in model.calls if c[0] not in (ALPHA, FINAL)]
            expected = []
            if passed:
                expected = [SPECIAL] if mutation == 1 else [GENERIC, FOLLOWUP]
            if mutation == 3 and mode == 2:
                expected.append(GENERIC)
            self.assertEqual(rendered, expected)
        model = self.models(memory_case((dict(state=7),)), mode=6, mutation=4)
        self.assertEqual([c[0] for c in model.calls], [GENERIC, FOLLOWUP, GENERIC, FINAL])
        model = self.models(memory_case((dict(state=4),)), mode=3, mutation=5)
        self.assertEqual(model.receipts[1][2], 0xDEADBEEF)
        self.assertEqual(model.peek(DIAG, 4), 0)

    def test_target_returned_cursor_zero_double_and_redirected_packets(self):
        for advance, redirect, mode in itertools.product((0, 8, 16), (False, True), MODES):
            model = self.models(memory_case([dict(state=7 if mode == 6 else 1 if mode == 2 else 4)] * 25),
                                mode=mode, advance=advance, redirect=redirect)
            cursor = OUTPUT + 8
            for target, *args in model.calls:
                if target == ALPHA:
                    continue
                self.assertEqual(args[0], cursor)
                cursor = OTHER if redirect and target == GENERIC and args[1] == 0 else cursor + advance
            self.assertEqual(model.r[2], cursor + 8)
            self.assertIn((cursor, 4, 0xDE000000), model.stores)
            self.assertIn((cursor + 4, 4, 0x80084190), model.stores)

    def test_target_mixed_full_table_sparse_slots_and_complete_coverage(self):
        rng = random.Random(0x1502BAD0)
        for mode, seed in itertools.product(MODES, range(12)):
            rows = [dict(active=rng.choice((0, 1, -1, 0x80000000)), state=rng.randrange(256),
                         identity=rng.choice((0, 17, 255)), flags=rng.getrandbits(32)) for _ in range(25)]
            rows[seed % 25] = dict(active=1, state=0, flags=0x200)
            alpha = ALPHAS[seed % len(ALPHAS)]
            model = self.models(memory_case(rows), mode=mode, alpha=alpha)
            slots = [c[2] for c in model.calls if c[0] in (SPECIAL, GENERIC)]
            expected = [i for i, row in enumerate(rows) if visible(row['active'], row['state'], row.get('identity', 0), row['flags'], mode, alpha)]
            self.assertEqual(slots, expected)
        # Retail retains an unreachable duplicate id load after an unconditional branch.
        self.assertEqual(self.coverage, set(range(ENTRY, ENTRY + 173 * 4, 4)) - {0x1502BBA4})

    def test_retained_unreachable_id_load_has_no_control_flow_predecessor(self):
        self.assertEqual(self.words[0xD4 // 4], 0x92090004)
        self.assertEqual(self.words[0xCC // 4], 0x10000047)
        for i, word in enumerate(self.words):
            if word >> 26 in (4, 5, 20, 21):
                offset = (word & 65535) - (65536 if word & 32768 else 0)
                self.assertNotEqual(ENTRY + i * 4 + 4 + offset * 4, 0x1502BBA4)
            if word >> 26 in (2, 3):
                self.assertNotEqual(((ENTRY + i * 4 + 4) & 0xF0000000) | (word & 0x3FFFFFF) << 2, 0x1502BBA4)

    def test_guards_reject_stale_words_and_omissions_do_not_claim_exactness(self):
        for offset in GUARDS:
            changed = self.raw[:]
            changed[offset // 4] ^= 1
            with self.assertRaisesRegex(AssertionError, 'stale actor-scan guard'):
                guarded(changed)
            self.assertNotEqual(guarded(self.raw, omitted=offset), self.retail)
        # Every register-renaming use must move with its two constant definitions.
        for offset in (0x70, 0x74, 0xE8, 0x11C, 0x124, 0x12C, 0x168, 0x178, 0x204):
            words = guarded(self.raw, omitted=offset)
            found = False
            for mode, state in itertools.product((1, 2, 6), (0, 1, 7)):
                memory = memory_case((dict(state=state),))
                original = ActorOracle(self.retail, memory, mode=mode).run()
                altered = ActorOracle(words, memory, mode=mode).run()
                found |= original.calls != altered.calls
            self.assertTrue(found, hex(offset))

    def test_native_all_state_bytes_gates_alpha_boundaries_and_sdk_packets(self):
        self.run_host(r'''
static s32 modes[]={-1,0,1,2,3,4,5,6,7};
static s32 alphas[]={(-2147483647-1),-1,0,254,255,256,2147483647};
static s32 actives[]={0,1,-1};int m,st,id,flag,act,a,cases=0;
for(m=0;m<9;m++) for(st=0;st<256;st++) for(id=0;id<2;id++) for(flag=0;flag<2;flag++)
for(act=0;act<3;act++) for(a=0;a<7;a++) {
    reset();expectedMode=modes[m];alphaValue=alphas[a];
    D_800CC2D0[0].active=actives[act];D_800CC2D0[0].state=(u8)st;
    D_800CC2D0[0].id=id?255:0;D_800CC2D0[0].flags=flag?0xFFFFFFFF:0;
    predict();if(check(0x5678FFFF)) return 1;cases++;
}
if(cases!=193536) return 2;
''')

    def test_native_all_slots_views_packets_callback_mutations_and_redirect(self):
        self.run_host(r'''
static s32 modes[]={-1,0,1,2,3,4,5,6,7};
static s32 views[]={0,1,-1,32767,32768,65535,0x12340001,0x5678FFFF};
int m,v,st,i,mut,cases=0;
for(m=0;m<9;m++) for(v=0;v<8;v++) for(st=0;st<8;st++) {
    reset();expectedMode=modes[m];alphaValue=256;step=2;
    for(i=0;i<25;i++) {D_800CC2D0[i].active=(i&1)?-1:1;D_800CC2D0[i].state=(u8)((i+st)&7);}
    predict();if(check(views[v])) return 1;cases++;
}
for(m=1;m<=2;m++) for(mut=1;mut<=4;mut++) {
    reset();expectedMode=m;alphaValue=256;mutation=mut;D_800CC2D0[0].active=1;
    expectAlpha=1;expectFinal=1;
    if(mut==1) expectSpecial=1;else {expectGeneric=expectFollowup=1;}
    if(mut==3 && m==2) expectGeneric++;
    if(check(32768)) return 2;
    cases++;
}
for(m=0;m<3;m++) {
    reset();expectedMode=6;alphaValue=255;step=m;redirect=1;mutation=4;
    D_800CC2D0[0].active=1;D_800CC2D0[0].state=7;
    expectGeneric=2;expectFollowup=expectFinal=1;
    if(check(-1)) return 3;
    if(alternate[0].words.w0!=0xA5A5A5A5 || (cursor+1)->words.w0!=0xA5A5A5A5) return 4;
    cases++;
}
if(cases!=587) return 5;
''')


if __name__ == '__main__':
    unittest.main()
