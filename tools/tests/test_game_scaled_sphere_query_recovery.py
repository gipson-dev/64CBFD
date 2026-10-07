"""Complete uninstalled scaled query and its real five-helper chain."""

import csv
import itertools
import json
import random
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_scaled_sphere_query_candidates as screen
from tools.experiments import game_scaled_sphere_query_schedule_candidates as scheduling
from tools.experiments import game_actor_dimensions_candidates as dimensions
from tools.experiments import game_sphere_callee_allocation_candidates as callee
from tools.experiments import game_sphere_wrapper_candidates as wrapper
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.pad_generated_object import parse_object
from tools.match_progress import load_elf_functions
from tools.tests import game_scaled_sphere_query_reference as reference
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests.test_game_sphere_wrapper_match import SphereOracle
from tools.tests.test_game_projection_lifetime_recovery import put, peek
from tools.tests.test_game_table_range_loader import native, STACK
from tools.tests.game_owner_pool import assert_guard_history
from tools.tests.game_owner_pool import normalized_pools
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly

ORIGIN, DIRECTION, ACTOR, POINTS, OPTIONAL = 0x20000, 0x21000, 0x22000, 0x24000, 0x28000
CENTERS = ((5.0, 0.0, 0.0), (-5.0, 0.0, 0.0), (1.0, 0.0, 0.0),
           (5.0, 1.0, 0.0), (5.0, 4.0, 0.0), (0.0, 0.0, 0.0))
SCALES = ((1.0, 1.0), (2.0, 0.5), (0.5, 2.0), (-1.0, -1.0))


def fixture(center=CENTERS[0], radius=1, height=2, scale=SCALES[0], identity=1,
            direction=(10.0, 0.0, 0.0), layout=0, mask=0, phase=0, vertical=0):
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
    for base, count in ((ORIGIN, 32), (DIRECTION, 32), (ACTOR, 0x440), (POINTS, 128), (OPTIONAL, 32)):
        memory.update({base + i: 0xA5 for i in range(count)})
    for base, values in ((ORIGIN, (0.0, 0.0, 0.0)), (DIRECTION, direction), (ACTOR + 0x14, center)):
        for i, value in enumerate(values):
            put(memory, base + i * 4, bits(value))
    put(memory, ACTOR + 4, identity, 1)
    for offset, value in ((0xD2, radius), (0xD4, height), (0xD6, vertical)):
        put(memory, ACTOR + offset, value, 2)
    for offset, value in zip((0xDC, 0xE0), scale):
        put(memory, ACTOR + offset, bits(value))
    for base in (0, 0x40800000, 0x40C00000):
        for i in range(4):
            put(memory, base + i * 4, bits(float(12 + i)))
    point0, point1 = POINTS, POINTS + 64
    if layout == 1: point1 = point0
    if layout == 2: point0 = ORIGIN
    if layout == 3: point1 = ORIGIN
    if layout == 4: point0 = DIRECTION
    if layout == 5: point1 = DIRECTION
    if layout == 6: point0 = ACTOR + 0x14
    if layout == 7: point1 = ACTOR + 0x14
    if layout == 8: point0 = ACTOR + 0xDC
    if layout == 9: point1 = ACTOR + 0xDC
    if layout == 10: point0 = point1 + 4
    if layout == 11: point0 = STACK + phase + 0xC
    args = (ORIGIN, DIRECTION, ACTOR, point0, point1,
            0 if mask & 1 else OPTIONAL, 0 if mask & 2 else OPTIONAL + 4,
            0 if mask & 4 else OPTIONAL + 8)
    return memory, args


class QueryOracle(SphereOracle):
    def __init__(self, words, memory, args, connected, phase=0):
        super().__init__(words, memory, args, connected, phase, entry=screen.ENTRY)
        self.caller_frame = STACK + phase - 0x88
        self.snapshots = []

    def record_call(self, target):
        count = {reference.DIMENSION: 4, reference.NORMALIZE: 4, reference.WRAPPER: 9,
                 reference.CALLEE: 8, reference.DOT: 2}[target]
        self.calls.append((target, *self.arguments(count)))
        if target in (reference.NORMALIZE, reference.WRAPPER):
            self.snapshots.append(reference.snapshot(self.memory, target, self.caller_frame))


class GameScaledSphereQueryRecoveryTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        if not (cls.root / 'ido/ido5.3_recomp/cc').is_file() or shutil.which('mips-linux-gnu-ld') is None:
            raise unittest.SkipTest('IDO/MIPS tools unavailable')
        cls.out = cls.root / 'conker/build/game-scaled-sphere-query-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.out, 'selected')
        (cls.out / 'selected-record.json').write_text(json.dumps(cls.record, indent=2) + '\n')
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>110I', rom, screen.ROM))
        cls.helpers = {}
        for name, entry, position, count in (('dimensions', reference.DIMENSION, 0x189650, 41),
                ('normalize', reference.NORMALIZE, 0x1725D8, 50),
                ('wrapper', reference.WRAPPER, wrapper.ROM, 53),
                ('callee', reference.CALLEE, callee.ROM, 126), ('dot', reference.DOT, wrapper.DOT_ROM, 13)):
            cls.helpers[name] = entry, list(struct.unpack_from('>%dI' % count, rom, position))
        cls.connected = {entry + i * 4: word for entry, words in cls.helpers.values() for i, word in enumerate(words)}
        cls.coverage = set()
        forms = dict(screen.negatives())
        assert all(body != screen.SELECTED for body in forms.values())
        cls.negative = {name: screen.compile_candidate(cls.root, cls.out, name, body)[1] for name, body in forms.items()}
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        header = (cls.root / 'conker/include/structs.h').read_text()
        actor = re.search(r'struct struct127 \{.*?(?=    s16 unkE4;)', header, re.S).group() + '};'
        normalize = (cls.root / 'conker/src/game_16EE20.c').read_text().split('s32 func_15145128(')[1].split('/* Note 1083:')[0]
        cls.fixture = '''typedef unsigned char u8;typedef signed char s8;typedef short s16;
typedef unsigned short u16;typedef int s32;typedef unsigned int u32;typedef float f32;
#define NULL ((void *)0)
typedef struct {f32 unk0,unk4,unk8;} struct17;
static u32 word(f32 f){union {f32 f;u32 u;} b;b.f=f;return b.u;}
static f32 number(u32 u){union {f32 f;u32 u;} b;b.u=u;return b.f;}
static f32 sqrtf(f32 v){f32 result;__asm__("sqrtss %1,%0":"=x"(result):"x"(v));return result;}
''' + actor + '\ntypedef struct struct127 struct127;\n' + screen.DECLARATIONS + dimensions.SELECTED + '\n' + (
            's32 func_15145128(' + normalize) + '''
f32 func_15144A74(f32 *a,f32 *b){return a[0]*b[0]+a[1]*b[1]+b[2]*a[2];}
''' + callee.SELECTED + '\n' + wrapper.SELECTED + '\n' + screen.SELECTED + '\n'
        cls.fixture += '''
static f32 mul(f32 a,f32 b){return a*b;}
static f32 add(f32 a,f32 b){return a+b;}
static int independent(u8 *bytes,int p,int q){
    f32 *m=(f32 *)bytes,o[3],d[3],c[3],delta[3],t[3],length,inv,scale;
    f32 radius,height,projection,perpendicular,root,first,second,rs,reciprocal;
    int i,special=bytes[4]<187;
    radius=special?(f32)*(s16 *)(bytes+0xD2):1.0f;
    height=special?(f32)*(s16 *)(bytes+0xD4):1.0f;
    c[0]=m[5];c[1]=special?add(m[6],(f32)*(s16 *)(bytes+0xD6)):m[6];c[2]=m[7];
    if(height==0 || radius==0)return 0;
    scale=m[0xDC/4];inv=m[0xE0/4];
    for(i=0;i<3;i++){o[i]=m[300+i];d[i]=m[308+i];}
    o[1]=mul(o[1],scale);d[1]=mul(d[1],scale);
    for(i=0;i<3;i++)t[i]=mul(d[i],d[i]);
    length=add(add(t[0],t[1]),t[2]);if(length==0)return 0;
    length=sqrtf(length);reciprocal=1.0f/length;
    for(i=0;i<3;i++)d[i]=mul(reciprocal,d[i]);
    c[1]=mul(c[1],scale);
    for(i=0;i<3;i++)delta[i]=c[i]-o[i];
    for(i=0;i<3;i++)t[i]=mul(delta[i],d[i]);
    projection=add(add(t[0],t[1]),t[2]);
    for(i=0;i<3;i++)t[i]=mul(delta[i],delta[i]);
    perpendicular=add(add(t[0],t[1]),t[2])-mul(projection,projection);
    rs=mul(radius,radius);if(rs<perpendicular)return 0;
    root=sqrtf(rs-perpendicular);if(projection<root)root=-root;
    first=projection-root;second=add(projection,root);
    for(i=0;i<3;i++)m[p+i]=add(mul(first,d[i]),o[i]);
    for(i=0;i<3;i++)m[q+i]=add(mul(second,d[i]),o[i]);
    for(i=0;i<3;i++)t[i]=mul(m[p+i]-o[i],d[i]);
    if(add(add(t[0],t[1]),t[2])<0)return 0;
    if(first<0 && second<0)return 0;
    if(!(first>=0 && second<0) && !(first<length))return 0;
    m[p+1]=mul(m[p+1],inv);m[q+1]=mul(m[q+1],inv);return 1;
}
'''

    @classmethod
    def tearDownClass(cls):
        (cls.out / 'coverage.json').write_text(json.dumps({name: dict(total=len(words), reached=sum(
            entry + i * 4 in cls.coverage for i in range(len(words)))) for name, (entry, words) in
            {'caller': (screen.ENTRY, cls.retail), **cls.helpers}.items()}, indent=2) + '\n')

    def check(self, memory, args, phase=0):
        snapshots = []
        expected, writes, status, calls = reference.reference(memory, args, phase, snapshots)
        models = []
        for words in (self.retail, self.words):
            model = QueryOracle(words, memory, args, self.connected, phase).run()
            self.assertEqual(model.r[2], status)
            self.assertEqual(reference.external(model.memory), reference.external(expected))
            self.assertEqual([e for e in model.events if e[0] == 'W' and not reference.private(e[1])], writes)
            self.assertEqual(model.calls, calls)
            self.assertEqual(model.snapshots, snapshots)
            if words is self.retail:
                self.coverage.update(model.visits)
            models.append(model)
        return models

    def test_complete_caller_finite_geometry_output_aliases_and_all_helpers(self):
        count = 0
        for center, radius, height, scale, direction, layout, phase in itertools.product(
                CENTERS, (0, 1, 2, -1), (0, 2), SCALES,
                ((10.0, 0.0, 0.0), (0.0, 10.0, 0.0), (0.0, 0.0, 0.0)), range(11), (0, 8)):
            memory, args = fixture(center, radius, height, scale, direction=direction, layout=layout, phase=phase)
            self.check(memory, args, phase)
            count += 1
        self.assertEqual(count, 12672)
        self.assertEqual(set(range(screen.ENTRY, screen.ENTRY + 440, 4)) - self.coverage,
            {screen.ENTRY + offset for offset in (0x28, 0x4C, 0x90)})

    def test_every_identity_byte_and_real_null_redirection_paths(self):
        count = 0
        for identity, mask, phase in itertools.product(range(256), range(8), (0, 8)):
            memory, args = fixture(identity=identity, mask=mask, phase=phase)
            original, raw = self.check(memory, args, phase)
            self.assertEqual(original.calls[0][2:], tuple(STACK + phase - 0x88 + offset if not mask & flag else 0
                for offset, flag in ((0x7C, 4), (0x78, 1), (0x74, 2))))
            count += 1
        self.assertEqual(count, 4096)

    def test_recovered_original_layout_and_uninstalled_oversized_fit(self):
        self.assertEqual((self.record['body_words'], self.record['frame']), (111, 136))
        self.assertFalse(self.record['exact'])
        self.assertEqual(self.record['diagnostics'], '')
        layout = screen.local_layout(self.out / 'selected.o')
        self.assertEqual(layout, dict(frame=136, entry_relative=dict(center=-12, radius=-16, height=-20,
            origin=-32, direction=-44, scaledCenter=-56, length=-60, first=-64, second=-68,
            scale=-72, inverse=-76, reciprocal=-80)))
        self.assertEqual(self.words[:34], self.retail[:34])
        self.assertEqual(self.record['differences'], 72)
        self.assertEqual(self.record['relocations'], {0x58: [('R_MIPS_26', 'func_1515C1A0')],
            0x100: [('R_MIPS_26', 'func_15145128')], 0x16C: [('R_MIPS_26', 'func_151451F0')]})

    def test_gate_storage_and_live_home_controls_do_not_fix_the_fit(self):
        expected = {}
        for left, right in itertools.product(range(3), repeat=2):
            expected['zero-left%d-right%d' % (left, right)] = (
                (112, 136, 79) if (left == 1) != (right == 1) else (111, 136, 72))
        expected.update({'nested-height0-radius0': (111, 136, 72),
            'nested-height0-radius1': (111, 136, 73), 'nested-height1-radius0': (111, 136, 77),
            'nested-height1-radius1': (112, 128, 109), 'scale-pair-union0': (111, 136, 72),
            'scale-pair-union1': (113, 136, 76),
            **{'array-' + name: (111, 136, 72) for name in ('origin', 'direction', 'scaledCenter')},
            **{'live-home%d' % index: values for index, values in enumerate((
                (114, 136, 80), (114, 136, 78), (114, 136, 95), (111, 144, 94),
                (111, 144, 92), (113, 136, 88), (113, 136, 99), (114, 128, 112)))},
            'shared-failure1': (111, 136, 77), 'shared-failure2': (111, 136, 73),
            'shared-failure3': (109, 136, 77), 'shared-failure15': (105, 136, 77)})
        records = []
        for name, body in scheduling.candidates():
            record, _ = screen.compile_candidate(self.root, self.out, name, body)
            self.assertEqual((record['body_words'], record['frame'], record['differences']), expected.pop(name))
            self.assertEqual(record['diagnostics'], '')
            self.assertFalse(record['exact'])
            record['layout'] = screen.local_layout(self.out / (name + '.o'))
            records.append(record)
        self.assertFalse(expected)
        self.assertEqual(len(records), 30)
        (self.out / 'schedule-records.json').write_text(json.dumps(records, indent=2) + '\n')

    def check_copied_owner(self, candidate=screen.SELECTED, return_owner=False):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        from tools.experiments import game_scaled_sphere_query_address_view_candidates as matching
        if matching.SELECTED in source:
            self.assertEqual(source.count(matching.SELECTED), 1)
            source = source.replace(matching.SELECTED, 's32 func_15145AD8() {\n    return 0;\n}').replace(
                matching.OWNER_DECLARATIONS + matching.PROTOTYPE, 's32 func_15145AD8();')
        selected = source.replace('s32 func_15145AD8();', screen.DECLARATIONS + screen.PROTOTYPE).replace(
            's32 func_15145AD8() {\n    return 0;\n}', candidate)
        self.assertEqual(selected.count(candidate), 1)
        objects, warnings = [], []
        for name, body in (('baseline', source), ('selected', selected)):
            obj, warning = compile_owner(self.root, self.out, body, 'owner-' + name)
            warnings.append(warning)
            processed = self.out / ('owner-' + name + '-processed.o')
            shutil.copyfile(obj, processed)
            subprocess.run(['python3', str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.out / ('owner-' + name + '.c')).relative_to(self.root / 'conker')),
                '--post-process', str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker',
                check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0], warnings[1])
        self.assertEqual(len(warnings[0]), 2)
        old_text, old_functions, old_rel = parse_object(objects[0])
        text, functions, rel = parse_object(objects[1])
        self.assertEqual(set(functions), set(old_functions))
        self.assertEqual(len(functions), 89)
        for name, meta in functions.items():
            if name == screen.FUNCTION:
                continue
            old = old_functions[name]
            self.assertEqual(text[meta['value']:meta['value'] + meta['size']],
                old_text[old['value']:old['value'] + old['size']], name)
            self.assertEqual({o - meta['value']: r for o, r in rel.items() if meta['value'] <= o < meta['value'] + meta['size']},
                {o - old['value']: r for o, r in old_rel.items() if old['value'] <= o < old['value'] + old['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        raw, standalone, standalone_rel = parse_object(self.out / 'selected.o')
        meta, isolated = functions[screen.FUNCTION], standalone[screen.FUNCTION]
        self.assertEqual(meta['size'], isolated['size'])
        self.assertEqual(text[meta['value']:meta['value'] + meta['size']],
            raw[isolated['value']:isolated['value'] + isolated['size']])
        self.assertEqual({o - meta['value']: r for o, r in rel.items() if meta['value'] <= o < meta['value'] + meta['size']},
            standalone_rel)
        if return_owner:
            return objects[1]
        assembly = emit_padded_assembly(objects[1], self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=self.root / 'conker/retail_word_patches.us.csv')
        overflow = '__retail_overflow_' + screen.FUNCTION
        body = assembly.split(screen.FUNCTION + ':\n', 1)[1].split('.size ' + screen.FUNCTION, 1)[0]
        self.assertEqual(re.findall(r'\.word 0x([0-9A-F]{8})', body), ['08000000'] + ['00000000'] * 109)
        self.assertIn('.reloc ., R_MIPS_26, ' + overflow, body)
        self.assertIn(overflow + ':\n', assembly)
        (self.out / 'owner-overflow.s').write_text(assembly)

    def test_copied_owner_preserves_neighbors_but_padder_uses_overflow(self):
        self.check_copied_owner()

    def test_natural_first_point_write_changes_both_late_output_pointer_homes(self):
        for phase in (0, 8):
            memory, args = fixture(scale=(2.0, 0.5), layout=11, phase=phase)
            for model in self.check(memory, args, phase):
                self.assertEqual(model.r[2], 1)
                self.assertEqual(peek(model.memory, STACK + phase + 0xC), bits(4.0))
                self.assertEqual(peek(model.memory, STACK + phase + 0x10), 0)
                self.assertEqual(peek(model.memory, 0x40800004), bits(6.5))
                self.assertEqual(peek(model.memory, 4), bits(6.5))

    def test_private_local_output_windows_remain_observable(self):
        count = 0
        for offset, output, center, phase in itertools.product(range(0x38, 0x80, 4), (0, 1),
                (CENTERS[0], CENTERS[1], CENTERS[3]), (0, 8)):
            memory, args = fixture(center=center, phase=phase)
            args = list(args); args[3 + output] = STACK + phase - 0x88 + offset
            self.check(memory, args, phase)
            count += 1
        self.assertEqual(count, 216)

    def test_varied_finite_vectors_dimensions_and_scales(self):
        rng = random.Random(screen.ENTRY)
        for _ in range(1024):
            memory, args = fixture(radius=rng.choice((-2, -1, 0, 1, 3)), height=rng.choice((-1, 0, 2)),
                scale=rng.choice(SCALES), layout=rng.randrange(11), identity=rng.randrange(256))
            for base in (ORIGIN, DIRECTION, ACTOR + 0x14):
                for i in range(3): put(memory, base + i * 4, bits(rng.randrange(-32, 33) / 8.0))
            self.check(memory, args)

    def test_signed_vertical_offsets_reach_the_real_geometry_chain(self):
        count = 0
        for vertical, identity, scale, center, direction, layout, phase in itertools.product(
                (-32768, -187, -2, -1, 0, 1, 187, 32767), (0, 186, 187, 255), SCALES,
                ((5.0, -1.0, 0.0), (5.0, 0.0, 0.0), (5.0, 1.0, 0.0)),
                ((10.0, 0.0, 0.0), (10.0, 10.0, 0.0), (0.0, 10.0, 0.0)), (0, 6, 8, 10), (0, 8)):
            memory, args = fixture(center=center, radius=2, identity=identity, scale=scale,
                direction=direction, layout=layout, phase=phase, vertical=vertical)
            models = self.check(memory, args, phase)
            adjusted = floating(bits(center[1] + vertical)) if identity < 187 else center[1]
            for model in models:
                self.assertEqual(model.snapshots[0][1][(0x80 - 0x38) // 4], bits(adjusted))
                self.assertEqual(model.snapshots[1][1][(0x54 - 0x38) // 4], bits(adjusted * scale[0]))
            count += 1
        self.assertEqual(count, 9216)

    def test_private_input_windows_preserve_call_boundary_values(self):
        count = 0
        for offset, input_index, vector, phase in itertools.product(range(0x38, 0x80, 4), (0, 1),
                ((1.0, 2.0, 3.0), (-1.0, -2.0, -3.0), (10.0, 10.0, 0.0)), (0, 8)):
            memory, args = fixture(scale=(2.0, 0.5), phase=phase, vertical=1)
            args = list(args)
            args[input_index] = STACK + phase - 0x88 + offset
            for axis, value in enumerate(vector):
                put(memory, args[input_index] + axis * 4, bits(value))
            self.check(memory, args, phase)
            count += 1
        self.assertEqual(count, 216)

    def test_required_fields_fail_closed_but_zero_dimensions_read_lazily(self):
        for mask in range(8):
            memory, args = fixture(mask=mask)
            if mask:
                for i in range(12): memory.pop(i, None)
                for words in (self.retail, self.words):
                    with self.assertRaisesRegex(AssertionError, 'unmapped'):
                        QueryOracle(words, memory, args, self.connected).run()
        memory, args = fixture(height=0)
        for base, size in ((ORIGIN, 12), (DIRECTION, 12), (ACTOR + 0xDC, 8), (POINTS, 128)):
            for i in range(size): memory.pop(base + i, None)
        self.check(memory, args)
        for base, size in ((ORIGIN, 12), (DIRECTION, 12), (ACTOR + 0xDC, 8)):
            memory, args = fixture()
            for i in range(size): memory.pop(base + i, None)
            for words in (self.retail, self.words):
                with self.assertRaisesRegex(AssertionError, 'unmapped'):
                    QueryOracle(words, memory, args, self.connected).run()

    def test_compiled_semantic_negatives_break_outputs(self):
        for name, (layout, direction) in {'ordinary-null-fallback': (0, (10.0, 0.0, 0.0)),
                'late-inverse': (8, (10.0, 10.0, 0.0)),
                'unscaled-direction': (0, (10.0, 10.0, 0.0)),
                'missing-output-unscale': (0, (10.0, 10.0, 0.0))}.items():
            memory, args = fixture(center=(5.0, 5.0, 0.0), radius=2, scale=(2.0, 0.5),
                direction=direction, layout=layout)
            good = QueryOracle(self.retail, memory, args, self.connected).run()
            bad = QueryOracle(self.negative[name], memory, args, self.connected).run()
            self.assertTrue((good.r[2], reference.external(good.memory)) !=
                (bad.r[2], reference.external(bad.memory)), name)

    def test_native_32bit_complete_caller_and_real_helpers_finite_aliases(self):
        self.run_host('''
static union {u32 words[480];u8 bytes[1920];} actual,expected;
static int ids[4]={0,186,187,255},radii[4]={0,1,2,-1},heights[2]={0,2};
static int verticals[5]={0,-32768,-1,1,32767};
static f32 scales[4][2]={{1,1},{2,0.5},{0.5,2},{-1,-1}};
static f32 centers[6][3]={{5,0,0},{-5,0,0},{1,0,0},{5,1,0},{5,4,0},{0,0,0}};
static f32 directions[3][3]={{10,0,0},{0,10,0},{0,0,0}};
int id,r,h,s,c,d,l,v,i,p,q,wanted,result,cases=0;
struct127 *actor=(struct127 *)actual.bytes;
if(sizeof(void *)!=4 || sizeof(struct17)!=12 || (u8 *)&actor->unkDC-actual.bytes!=0xDC
    || (u8 *)&actor->unkE0-actual.bytes!=0xE0 || (u8 *)&actor->unkD2-actual.bytes!=0xD2)return 1;
for(id=0;id<4;id++)for(r=0;r<4;r++)for(h=0;h<2;h++)for(s=0;s<4;s++)
for(c=0;c<6;c++)for(d=0;d<3;d++)for(l=0;l<11;l++)for(v=0;v<5;v++){
    for(i=0;i<1920;i++)actual.bytes[i]=0xA5;
    actor->id=ids[id];actor->unkD2=radii[r];actor->unkD4=heights[h];actor->unkD6=verticals[v];
    actor->unkDC=scales[s][0];actor->unkE0=scales[s][1];
    for(i=0;i<3;i++){actual.words[5+i]=word(centers[c][i]);
        actual.words[300+i]=word(0);actual.words[308+i]=word(directions[d][i]);}
    p=320;q=336;
    if(l==1){q=p;}if(l==2){p=300;}if(l==3){q=300;}if(l==4){p=308;}if(l==5){q=308;}
    if(l==6){p=5;}if(l==7){q=5;}if(l==8){p=0xDC/4;}if(l==9){q=0xDC/4;}if(l==10){p=q+1;}
    for(i=0;i<1920;i++)expected.bytes[i]=actual.bytes[i];
    wanted=independent(expected.bytes,p,q);
    result=func_15145AD8((struct17 *)(actual.words+300),(struct17 *)(actual.words+308),actor,
        (struct17 *)(actual.words+p),(struct17 *)(actual.words+q),
        (f32 *)(actual.words+400),(f32 *)(actual.words+401),(struct17 *)(actual.words+402));
    if(result!=wanted)return 2;
    for(i=0;i<1920;i++)if(actual.bytes[i]!=expected.bytes[i])return 3;
    cases++;
}
if(cases!=126720)return 4;
''')

    def test_uninstalled_source_and_original_helper_slots_are_bound(self):
        """Historical candidates stay uninstalled after the direct recovery lands."""
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        from tools.experiments import game_scaled_sphere_query_address_view_candidates as matching
        installed = matching.SELECTED in source
        if installed:
            self.assertEqual(source.count(matching.SELECTED), 1)
        else:
            self.assertIn('s32 func_15145AD8() {\n    return 0;\n}', source)
        self.assertNotIn(screen.SELECTED, source)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        if installed:
            self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
            self.assertEqual(functions[screen.FUNCTION], self.retail)
        for _, (entry, words) in self.helpers.items():
            name = next(name for name, address in addresses.items() if address == entry)
            self.assertEqual(functions[name], words)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        assert_guard_history(self, rows)
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in rows))


if __name__ == '__main__':
    unittest.main()
