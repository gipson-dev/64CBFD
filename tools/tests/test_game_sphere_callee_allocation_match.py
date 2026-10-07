"""Retail private layout, closed guard inputs and copied-owner installation gates."""

import csv
import itertools
import random
import shutil
import struct
import subprocess
import tempfile
from pathlib import Path

from tools.experiments import game_sphere_callee_allocation_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.experiments.game_actor_classifier_candidates import sections
from tools.pad_generated_object import parse_object
from tools.tests import game_sphere_frame_reference as frame_reference
from tools.tests import test_game_sphere_callee_frame_recovery as recovery
from tools.tests.test_game_sphere_wrapper_match import CENTERS, POINTS, STACK, SphereOracle, bits, external, fixture, floating, peek, put
from tools.tests.test_game_projection_schedule_match import guarded
from tools.tests.test_game_owner_pool import normalized_pools
from tools.tests.game_owner_pool import assert_guard_history
from tools.match_progress import load_elf_functions
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests.test_game_table_range_loader import native


class OperandCode(dict):
    def __init__(self, model, remap=False):
        super().__init__(model.code)
        self.model, self.remap, self.trace = model, remap, {}

    def __getitem__(self, pc):
        word = super().__getitem__(pc)
        m = self.model
        op, rs, rt, rd, fd, fn = word >> 26, word >> 21 & 31, word >> 16 & 31, word >> 11 & 31, word >> 6 & 31, word & 63
        imm = word & 65535
        signed_imm = imm if imm < 32768 else imm - 65536
        if op == 0:
            identity = (op, fn)
            inputs = (m.r[rt], fd) if fn == 0 else (m.r[rs],) if fn == 8 else tuple(sorted((m.r[rs], m.r[rt])))
            assert fn in (0, 8, 37)
        elif op in (35, 43, 49, 57):
            address = (m.r[rs] + signed_imm) & 0xFFFFFFFF
            value = m.f[rt] if op == 57 else m.r[rt] if op == 43 else peek(m.memory, address)
            identity, inputs = (op,), (address, 4, value)
        elif op == 17:
            identity = (op, rs, fn if rs == 16 else None)
            if rs == 4: inputs = (m.r[rt],)
            elif rs == 8: inputs = (m.condition, rt, imm)
            elif rs == 16:
                inputs = (m.f[rd],) if fn in (4, 6, 7) else (m.f[rd], m.f[rt])
                if fn in (0, 2): inputs = tuple(sorted(inputs))
            else: raise AssertionError(hex(word))
        elif op in (2, 3):
            identity, inputs = (op,), (((pc + 4) & 0xF0000000) | ((word & 0x3FFFFFF) << 2),)
        elif op == 4: identity, inputs = (op,), (*sorted((m.r[rs], m.r[rt])), imm)
        elif op == 9: identity, inputs = (op,), (m.r[rs], signed_imm)
        elif op == 15: identity, inputs = (op,), (imm,)
        else: raise AssertionError(hex(word))
        mapped = pc
        if self.remap and screen.ENTRY <= pc < screen.ENTRY + 504:
            mapped = screen.ENTRY + screen.SCHEDULE.get(pc - screen.ENTRY, pc - screen.ENTRY)
        assert mapped not in self.trace
        self.trace[mapped] = identity, inputs
        return word


class GameSphereCalleeAllocationMatchTests(recovery.GameSphereCalleeFrameRecoveryTests):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.out = cls.root / 'conker/build/game-sphere-callee-allocation-test'
        cls.out.mkdir(exist_ok=True)
        cls.record, cls.trial = screen.compile_candidate(cls.root, cls.out, 'selected')
        cls.rows = screen.owner_guards()
        cls.normalized = guarded(cls.trial, cls.rows)
        cls.coverage = set()
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = '''typedef unsigned int u32;typedef int s32;typedef float f32;
typedef struct {f32 unk0,unk4,unk8;} struct17;
typedef char pointer_size[sizeof(void *)==4?1:-1];
typedef char vector_size[sizeof(struct17)==12?1:-1];
static u32 word(f32 f){union {f32 f;u32 u;} b;b.f=f;return b.u;}
static f32 number(u32 u){union {f32 f;u32 u;} b;b.u=u;return b.f;}
static f32 sqrtf(f32 v){f32 result;__asm__("sqrtss %1,%0":"=x"(result):"x"(v));return result;}
f32 func_15144A74(f32 *a,f32 *b){return a[0]*b[0]+a[1]*b[1]+b[2]*a[2];}
''' + screen.SELECTED + '''
static f32 product(f32 a,f32 b){return a*b;}
static f32 sum(f32 a,f32 b){return a+b;}
static int expected(f32 *m,int p,int q,int x,int y,f32 radius){
    f32 o[3],d[3],v[3],r[3],t[3],projection,perpendicular,root,first,second,rs;
    int i;
    for(i=0;i<3;i++){o[i]=m[i];d[i]=m[8+i];v[i]=m[16+i]-o[i];}
    for(i=0;i<3;i++)t[i]=product(v[i],d[i]);
    projection=sum(sum(t[0],t[1]),t[2]);
    for(i=0;i<3;i++)t[i]=product(v[i],v[i]);
    perpendicular=sum(sum(t[0],t[1]),t[2])-product(projection,projection);
    rs=product(radius,radius);if(rs<perpendicular)return 0;
    root=sqrtf(rs-perpendicular);if(projection<root)root=-root;
    first=projection-root;second=sum(projection,root);
    for(i=0;i<3;i++){m[p+i]=sum(product(first,d[i]),o[i]);}m[x]=first;
    for(i=0;i<3;i++){m[q+i]=sum(product(second,d[i]),o[i]);}m[y]=second;
    for(i=0;i<3;i++)r[i]=m[p+i]-m[i];
    for(i=0;i<3;i++)t[i]=product(r[i],m[8+i]);
    return !(sum(sum(t[0],t[1]),t[2])<0);
}
'''

    def check(self, memory, args, phase=0):
        expected, writes, status, dot = frame_reference.reference(memory, args, phase)
        models = []
        for raw, words in ((False, self.retail), (True, self.trial), (False, self.normalized)):
            model = SphereOracle(words, memory, args, self.connected, phase, entry=screen.ENTRY)
            model.code = OperandCode(model, raw)
            model.run()
            self.assertEqual(model.memory, expected)
            self.assertEqual(model.r[2], status)
            self.assertEqual([e for e in model.events if e[0] == 'W'], writes)
            self.assertEqual(model.calls, [] if dot is None else [(screen.DOT, *dot)])
            self.coverage.update(model.visits)
            models.append(model)
        self.assertEqual(models[0].code.trace, models[1].code.trace)
        self.assertEqual(models[0].events, models[2].events)
        self.assertEqual(models[0].r, models[2].r)
        self.assertEqual(models[0].f, models[2].f)
        return models[:2]

    def test_original_counterexample_is_explained_by_live_private_copy_reads(self):
        memory, wrapper_args = fixture()
        args = list((*wrapper_args[:4], *wrapper_args[5:]))
        args[4] = STACK - 0x70 + 0x58
        original, raw = self.check(memory, args)
        self.assertEqual(floating(peek(original.memory, POINTS + 64)), 24.0)
        self.assertEqual(raw.memory, original.memory)

    def test_private_output_windows_and_incoming_homes_have_layout_specific_results(self):
        offsets = (*range(0x1C, 0x70, 4), 0x70, 0x7C, 0x80, 0x84, 0x88, 0x8C)
        count = 0
        for offset, output, center, radius, phase in itertools.product(
                offsets, range(4), (CENTERS[0], CENTERS[1], CENTERS[5]), (1.0, 2.0), (0, 8)):
            memory, wrapper_args = fixture(center, radius, phase=phase)
            for number in (0.0, *range(3, 8), *range(-7, -2)):
                memory.update({bits(number) + i: 0xA5 for i in range(16)})
            args = list((*wrapper_args[:4], *wrapper_args[5:]))
            args[4 + output] = STACK + phase - 0x70 + offset
            original, raw = self.check(memory, args, phase)
            self.assertEqual(original.memory, raw.memory)
            count += 1
        self.assertEqual(count, 1296)

    def test_missing_private_snapshot_and_late_scalar_target_fail_closed(self):
        for words in (self.retail, self.trial, self.normalized):
            for address in (STACK - 0x70 + 0x58, STACK + 0x18):
                memory, wrapper_args = fixture()
                args = list((*wrapper_args[:4], *wrapper_args[5:]))
                if address == STACK + 0x18:
                    args[4] = address
                    address = bits(4.0)
                    memory.update({i: 0xA5 for i in range(16)})
                for i in range(4): memory.pop(address + i, None)
                with self.assertRaisesRegex(AssertionError, 'unmapped'):
                    SphereOracle(words, memory, args, self.connected, entry=screen.ENTRY).run()

    def test_closed_fit_and_guard_boundaries(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (126, 112, 53))
        self.assertEqual(self.normalized, self.retail)
        self.assertEqual(len(self.rows), 53)
        self.assertEqual(self.record['relocations'], {0x1C0: [('R_MIPS_26', 'func_15144A74')]})
        self.assertTrue(all(r['omit'] == 'false' and r['insert_after'] == '' for r in self.rows))
        self.assertEqual(self.trial[:35], self.retail[:35])
        self.assertEqual(self.trial[-9:], self.retail[-9:])
        layout = screen.local_layout(self.out / 'selected.o')
        self.assertEqual(layout['frame'], 112)
        self.assertEqual(layout['entry_relative'], dict(x=-4, y=-8, z=-12, direction=-24, origin=-36,
            projection=-40, radiusSquared=-44, perpendicularSquared=-48, root=-52, first=-56, second=-60, relative=-72))

    def test_varied_finite_origins_directions_and_external_aliases(self):
        rng = random.Random(screen.ENTRY)
        from tools.tests.test_game_sphere_wrapper_match import ORIGIN, DIRECTION, CENTER
        for _ in range(1024):
            memory, wrapper_args = fixture(radius=rng.choice((0.0, 0.25, 1.0, -1.0, 2.0, 8.0)), layout=rng.randrange(13))
            for base in (ORIGIN, DIRECTION, CENTER):
                for i in range(3): put(memory, base + i * 4, bits(rng.randrange(-32, 33) / 8.0))
            self.check(memory, (*wrapper_args[:4], *wrapper_args[5:]))
        self.assertTrue(set(range(screen.ENTRY, screen.ENTRY + 504, 4)).issubset(self.coverage))
        self.assertTrue(set(range(screen.DOT, screen.DOT + 52, 4)).issubset(self.coverage))

    def copied_owner(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        baseline = source.replace(screen.SELECTED, screen.ASSEMBLY)
        selected = baseline.replace(screen.ASSEMBLY, screen.SELECTED)
        objects, warnings = [], []
        for name, body in (('baseline', baseline), ('selected', selected)):
            obj, warning = compile_owner(self.root, self.out, body, 'owner-' + name)
            warnings.append(warning)
            processed = self.out / ('owner-' + name + '-processed.o')
            shutil.copyfile(obj, processed)
            subprocess.run(['python3', str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.out / ('owner-' + name + '.c')).relative_to(self.root / 'conker')),
                '--post-process', str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker', check=True, capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0], warnings[1])
        self.assertEqual(len(warnings[0]), 2)
        old_text, old_functions, old_rel = parse_object(objects[0])
        text, functions, rel = parse_object(objects[1])
        self.assertEqual(set(functions), set(old_functions))
        self.assertEqual(len(functions), 89)
        for name, meta in functions.items():
            if name == screen.FUNCTION: continue
            old = old_functions[name]
            self.assertEqual(text[meta['value']:meta['value'] + meta['size']], old_text[old['value']:old['value'] + old['size']], name)
            self.assertEqual({o - meta['value']: r for o, r in rel.items() if meta['value'] <= o < meta['value'] + meta['size']},
                {o - old['value']: r for o, r in old_rel.items() if old['value'] <= o < old['value'] + old['size']}, name)
        self.assertEqual(normalized_pools(objects[0]), normalized_pools(objects[1]))
        raw, standalone, standalone_rel = parse_object(self.out / 'selected.o')
        meta = functions[screen.FUNCTION]
        self.assertEqual(text[meta['value']:meta['value'] + 504], raw[standalone[screen.FUNCTION]['value']:standalone[screen.FUNCTION]['value'] + 504])
        self.assertEqual({o - meta['value']: r for o, r in rel.items() if meta['value'] <= o < meta['value'] + 504}, standalone_rel)
        return objects[1]

    def test_copied_owner_and_actual_padder_with_alternate_helper_and_stale_guard(self):
        obj = self.copied_owner()
        patch_path = self.out / 'guards.csv'
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            reader = csv.DictReader(stream)
            fields, rows = reader.fieldnames, list(reader)
        rows = [r for r in rows if r['function'] != screen.FUNCTION] + [dict(row) for row in self.rows]
        with patch_path.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fields); writer.writeheader(); writer.writerows(rows)
        assembly = emit_padded_assembly(obj, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=patch_path)
        begin = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), begin)
        end = assembly.index('\n', end)
        asm, padded, elf = (self.out / ('padded' + suffix) for suffix in ('.s', '.o', '.elf'))
        asm.write_text('.text\n.globl ' + screen.FUNCTION + '\n' + assembly[begin:end + 1])
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(padded), str(asm)], check=True, capture_output=True)
        _, functions, rel = parse_object(padded)
        self.assertEqual(functions[screen.FUNCTION]['size'], 504)
        self.assertEqual(rel, self.record['relocations'])
        for target in (screen.DOT, screen.DOT + 0x100000):
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.out / 'selected.ld'),
                '-e', screen.FUNCTION, '--defsym=func_15144A74=0x%X' % target, '-o', str(elf), str(padded)], check=True, capture_output=True)
            expected = self.retail.copy(); expected[0x1C0 // 4] = 0x0C000000 | (target >> 2 & 0x3FFFFFF)
            self.assertEqual(list(struct.unpack_from('>126I', sections(elf)['.text'][1])), expected)
        rows[-1]['expected'] = '0x00000000'
        with patch_path.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fields); writer.writeheader(); writer.writerows(rows)
        with self.assertRaisesRegex(ValueError, 'stale'):
            emit_padded_assembly(obj, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
                rodata_symbol='jtbl_800A5218_game', word_patches_path=patch_path)

    def test_native_32bit_finite_geometry_external_aliases_and_full_storage(self):
        self.run_host('''
static f32 centers[9][3]={{5,0,0},{-5,0,0},{0,0,0},{1,0,0},{5,1,0},
    {5,2,0},{0.25,0.5,-0.25},{5,0.25,0.5},{-0.5,-0.25,0.5}};
static f32 radii[6]={0,0.25,1,-1,2,8};
static f32 origins[3][3]={{0,0,0},{1,-2,0.5},{-0.25,0.5,-1}};
static f32 directions[3][3]={{1,0,0},{0,1,0},{0.5,-0.5,0.5}};
static f32 a[128],b[128];int o,d,c,r,l,i,p,q,x,y,wanted,result,cases=0;
for(o=0;o<3;o++)for(d=0;d<3;d++)for(c=0;c<9;c++)for(r=0;r<6;r++)for(l=0;l<13;l++){
    for(i=0;i<128;i++)a[i]=b[i]=number(0xA5A5A5A5);
    for(i=0;i<3;i++){a[i]=b[i]=origins[o][i];a[8+i]=b[8+i]=directions[d][i];a[16+i]=b[16+i]=centers[c][i];}
    p=32;q=64;x=96;y=97;
    if(l==1){q=p;}if(l==2){p=0;}if(l==3){q=0;}if(l==4){p=8;}if(l==5){q=8;}if(l==6){p=16;}
    if(l==7){x=p;}if(l==8){y=p+1;}if(l==9){y=x;}if(l==10){p=q+1;}if(l==11){x=8;}if(l==12){y=2;}
    wanted=expected(b,p,q,x,y,radii[r]);
    result=func_151452C4((struct17 *)a,(struct17 *)(a+8),(struct17 *)(a+16),radii[r],
        (struct17 *)(a+p),(struct17 *)(a+q),a+x,a+y);
    if(result!=wanted)return 1;
    for(i=0;i<128;i++)if(word(a[i])!=word(b[i]))return 2;
    cases++;
}
if(cases!=6318)return 3;
''')

    def test_production_source_slot_and_complete_historical_guards(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.SELECTED, source)
        self.assertNotIn(screen.ASSEMBLY, source)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        assert_guard_history(self, guards)
        self.assertEqual([row for row in guards if row['function'] == screen.FUNCTION], self.rows)


if __name__ == '__main__':
    import unittest
    unittest.main()
