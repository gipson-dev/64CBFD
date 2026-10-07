"""Texture resolver semantics, original table ownership and checked relocation binding."""

import csv
import itertools
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_texture_resolver_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.patch_generated_slice_ld import load_game_data_layout
from tools.pad_generated_object import parse_object
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.experiments import game_output_mode_candidates as output_mode
from tools.experiments import game_secondary_output_candidates as secondary_output
from tools.tests import test_game_texture_cache_match as cache
from tools.tests import test_game_random_curve_record as native
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly

STACK, SOURCE, ROWS = cache.STACK, 0x24000, 0x80070000
B0, B14, B64, RECORDS = 0x800915B0, 0x80091514, 0x80091564, 0x80090B60
BASES = (0x0FFFFFFF, 0x10000000, 0x80050000)


def fixture(args, base, phase=0, pool=None):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x140)}
    for address, size in ((SOURCE, 32), (B0 - 4, 12), (B14 - 4, 12),
            (B64 - 32, 68), (RECORDS - 96, 204), (ROWS, 17 * 64)):
        memory.update({address + i: (i * 31 + 7) & 255 for i in range(size)})
    cache.put(memory, B0, 0x11223344)
    cache.put(memory, B14, 0x55667788)
    for index in range(-8, 9):
        cache.put(memory, B64 + index * 4, (0x89ABCDEF + index * 31) & 0xFFFFFFFF)
        row = ROWS + (index + 8) * 64 + 16
        cache.put(memory, RECORDS + index * 12, row)
        for subindex in range(-4, 5):
            cache.put(memory, row + subindex * 4, (0xABCDEF01 + index * 37 + subindex * 19) & 0xFFFFFFFF)
    cache.put(memory, SOURCE, base)
    if base >= 0x10000000:
        for index in range(-4, 5):
            address = (base + index * 4) & 0xFFFFFFFF
            memory.update({address + i: 0xA5 for i in range(4)})
            cache.put(memory, address, (0xDEADBEEF + index * 13) & 0xFFFFFFFF)
    if pool is not None:
        memory.update({screen.TABLE + i: value for i, value in enumerate(pool)})
    return memory


def expected(memory, args):
    source, index, subindex, kind = args
    index, subindex, kind = cache.signed(index), cache.signed(subindex), kind & 255
    reads = []

    def load(address):
        address &= 0xFFFFFFFF
        value = cache.read(memory, address)
        reads.append(('R', address, 4, value))
        return value

    if kind == 1: value = 0
    elif kind == 2: value = load(B64 + index * 4)
    elif kind == 3: value = load(B14)
    elif kind == 4: value = load(B0)
    elif kind == 5: value = index & 0xFFFFFFFF
    elif kind == 6:
        value = load(source)
        if value >= 0x10000000:
            value = load(value + subindex * 4)
    else:
        value = load(load(RECORDS + index * 12) + subindex * 4)
    return value, reads


def data_reads(model):
    return [e for e in model.events if e[0] == 'R' and not
        screen.TABLE <= e[1] < screen.TABLE + 64 and not STACK - 0x600 <= e[1] < STACK + 0x140]


class GameTextureResolverMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-texture-resolver-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words, cls.pool = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>50I', cls.rom, screen.ROM))
        address, data = screen.sections(cls.root / 'conker/build/conker.us.elf')['.game_data']
        cls.original = data[screen.TABLE - address:screen.TABLE - address + 24]
        start, vram, _, owners = load_game_data_layout(cls.root / 'conker')
        assert cls.original == cls.rom[start + screen.TABLE - vram:start + screen.TABLE - vram + 24]
        cls.owners = [o for o in owners if o['address'] < screen.TABLE + 24 and o['end'] > screen.TABLE]
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, report):
        (self.output / (name + '.json')).write_text(json.dumps(report, indent=2) + '\n')

    def model(self, words, memory, args, phase=0):
        return TriangleOracle(words, memory, phase=phase, entry=screen.ENTRY, arguments=args).run()

    def test_seventy_two_controls_direct_slot_and_original_table_targets(self):
        self.assertEqual((self.record['body_words'], self.record['differences'], self.record['frame']), (50, 0, 0))
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.pool[:24], self.original)
        self.assertEqual(self.pool[24:], bytes(8))
        self.assertEqual(struct.unpack('>6I', self.original),
            (0x151430B8, 0x151430C0, 0x151430AC, 0x151430A0, 0x151430D4, 0x151430DC))
        records = []
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                record, words, pool = screen.compile_candidate(self.root, self.output, name + '-' + profile, body, profile)
                records.append(record)
                if record['differences'] == 0:
                    self.assertEqual(words, self.retail)
                    self.assertEqual(pool[:24], self.original)
        self.assertEqual(len(records), 72)
        self.assertEqual(sum(r['differences'] == 0 for r in records), 2)
        self.receipt('controls', records)

    def test_guest_every_kind_signed_indices_threshold_full_storage_and_trace(self):
        count, coverage = 0, [set(), set()]
        for kind, index, subindex, base, phase in itertools.product(range(256), (-2, 0, 2), (-2, 0, 2), BASES, (0, 8)):
            args = (SOURCE, index & 0xFFFFFFFF, subindex & 0xFFFFFFFF, kind | 0xABCD0000)
            memory = fixture(args, base, phase, self.original)
            value, reads = expected(memory, args)
            after = dict(memory)
            cache.put(after, STACK + phase + 12, args[3])
            models = []
            for n, words in enumerate((self.words, self.retail)):
                model = self.model(words, memory, args, phase)
                self.assertEqual(model.r[2], value)
                self.assertEqual(model.memory, after)
                self.assertEqual(data_reads(model), reads)
                self.assertEqual([e for e in model.events if e[0] == 'W'], [('W', STACK + phase + 12, 4, args[3])])
                self.assertEqual(model.calls, [])
                models.append(model)
                coverage[n].update(model.visits)
            self.assertEqual(models[0].events, models[1].events)
            count += 1
        self.assertEqual(count, 13824)
        self.assertEqual([len(c) for c in coverage], [50, 50])
        self.receipt('guest', dict(cases=count, bodies=2, covered_words=[50, 50], full_memory=True, full_traces=True))

    def test_unused_source_and_mapped_memory_fail_closed(self):
        for kind in (0, 1, 2, 3, 4, 5, 7, 255):
            args = (0x12345678, 0, 0, kind)
            memory = fixture(args, BASES[0], pool=self.original)
            value, reads = expected(memory, args)
            model = self.model(self.words, memory, args)
            self.assertEqual(model.r[2], value)
            self.assertEqual(data_reads(model), reads)
        for kind, missing in ((6, SOURCE), (2, B64), (3, B14), (4, B0), (0, RECORDS),
                (6, 0x10000000), (0, ROWS + 8 * 64 + 16), (1, screen.TABLE)):
            args = (SOURCE, 0, 0, kind)
            memory = fixture(args, 0x10000000, pool=self.original)
            del memory[missing]
            with self.assertRaisesRegex(AssertionError, 'unmapped'):
                self.model(self.words, memory, args)

    def test_actual_native_32_bit_typed_caller_and_complete_readonly_inputs(self):
        self.fixture = ('typedef unsigned char u8;typedef unsigned short u16;typedef unsigned int u32;typedef int s32;\n'
            + screen.SOURCE_DECLARATION + screen.DECLARATIONS
            + 's32 D_800915B0,D_80091514,D_80091564[5];GameTextureSource D_80090B60[5];\n' + screen.SELECTED + '\n')
        self.run_host(r'''
s32 rows[5][5],saved[5][5],sourceRows[5],sourceSaved[5];
GameTextureSource sourceRecord,recordSaved[5];u8 sourceSavedBytes[12];
int kind,index,subindex,base,i,j,count=0;u32 word,want,answer;
for(i=0;i<5;i++)for(j=0;j<5;j++)rows[i][j]=(s32)(0xABCDEF01u+i*37u+j*19u);
for(i=0;i<5;i++)sourceRows[i]=(s32)(0xDEADBEEFu+i*13u);
for(i=0;i<5;i++)sourceSaved[i]=sourceRows[i];
for(i=0;i<5;i++)for(j=0;j<5;j++)saved[i][j]=rows[i][j];
D_800915B0=0x11223344;D_80091514=0x55667788;
for(i=0;i<5;i++) {
    D_80091564[i]=(s32)(0x89ABCDEFu+i*31u);
    for(j=0;j<12;j++)((u8 *)&D_80090B60[i])[j]=0xA5;
    D_80090B60[i].unk0=(u32)&rows[i][2];recordSaved[i]=D_80090B60[i];
}
for(i=0;i<12;i++)((u8 *)&sourceRecord)[i]=0x55;
for(kind=0;kind<256;kind++)for(index=0;index<5;index++)for(subindex=-2;subindex<3;subindex++)for(base=0;base<3;base++) {
    word=base==0?0u:base==1?0x0FFFFFFFu:(u32)&sourceRows[2];
    sourceRecord.unk0=word;
    for(i=0;i<12;i++)sourceSavedBytes[i]=((u8 *)&sourceRecord)[i];
    switch(kind) {
        case 1:want=0;break;case 2:want=(u32)D_80091564[index];break;
        case 3:want=0x55667788;break;case 4:want=0x11223344;break;
        case 5:want=(u32)index;break;
        case 6:want=base<2?word:(u32)sourceRows[subindex+2];break;
        default:want=(u32)rows[index][subindex+2];break;
    }
    answer=(u32)func_1514306C(&sourceRecord,index,subindex,(u8)(kind|0xABCD0000u));
    if(answer!=want)return 1;
    for(i=0;i<12;i++)if(((u8 *)&sourceRecord)[i]!=sourceSavedBytes[i])return 2;
    for(i=0;i<5;i++)for(j=0;j<12;j++)if(((u8 *)&D_80090B60[i])[j]!=((u8 *)&recordSaved[i])[j])return 3;
    for(i=0;i<5;i++)for(j=0;j<5;j++)if(rows[i][j]!=saved[i][j])return 4;
    for(i=0;i<5;i++)if(sourceRows[i]!=sourceSaved[i] || (u32)D_80091564[i]!=0x89ABCDEFu+i*31u)return 5;
    if(D_800915B0!=0x11223344 || D_80091514!=0x55667788)return 6;
    count++;
}
if(count!=19200 || sizeof(void *)!=4 || sizeof(GameTextureSource)!=12 || (u32)&sourceRows[2]<0x10000000u)return 7;
''')
        self.receipt('native', dict(cases=19200, bits=32, typed_caller=True, complete_readonly_inputs=True,
            negative_indices='guest only', threshold_edge='guest only'))

    def test_compiled_negatives_change_known_results_or_data_reads(self):
        forms = {
            'placeholder': screen.PROTOTYPE[:-1] + ' { return 0; }',
            'full-kind': screen.SELECTED.replace('u8 kind', 'u32 kind'),
            'signed-threshold': screen.SELECTED.replace('(u32)index >= 0x10000000U', 'index >= 0x10000000'),
            'shifted-threshold': screen.SELECTED.replace('0x10000000U', '0x10000004U'),
            'wrong-null': screen.SELECTED.replace('result = 0;', 'result = 1;'),
            'wrong-global': screen.SELECTED.replace('result = D_800915B0;', 'result = D_80091514;'),
            'wrong-table-index': screen.SELECTED.replace('D_80091564[index]', 'D_80091564[index + 1]'),
            'wrong-record-index': screen.SELECTED.replace('D_80090B60[index]', 'D_80090B60[index + 1]'),
            'wrong-subindex': screen.SELECTED.replace('[subindex]', '[subindex + 1]'),
            'wrong-passthrough': screen.SELECTED.replace('case 5:\n            result = index;', 'case 5:\n            result = -index;')}
        receipts = []
        for name, body in forms.items():
            self.assertNotEqual(body, screen.SELECTED)
            _, words, pool = screen.compile_candidate(self.root, self.output, name, body)
            changes = 0
            for kind, base in itertools.product((0, 1, 2, 3, 4, 5, 6, 255), BASES):
                args = (SOURCE, 2, 0xFFFFFFFE, kind | 0xABCD0000)
                memory = fixture(args, base, pool=pool)
                value, reads = expected(memory, args)
                model = self.model(words, memory, args)
                changes += (model.r[2], data_reads(model)) != (value, reads)
            self.assertGreater(changes, 0, name)
            receipts.append(dict(name=name, mapped_cases=24, changes=changes))
        self.receipt('negatives', receipts)

    def test_complete_original_cache_caller_and_both_resolvers(self):
        main = list(struct.unpack_from('>102I', self.rom, cache.screen.ROM))
        count, coverage = 0, [set(), set()]
        for kind, index, subindex, base, phase in itertools.product((0, 1, 2, 3, 4, 5, 6, 7, 255),
                (-2, 0, 2), (-2, 0, 2), BASES, (0, 8)):
            args = list(cache.arguments())
            args[2], args[6], args[7] = (subindex << 16 | 0xAB00) & 0xFFFFFFFF, index & 0xFFFFFFFF, kind | 0xABCD0000
            leaf_args = (args[1], args[6], subindex & 0xFFFFFFFF, args[7])
            memory = cache.memory_case(args, world=cache.WORLDS[count % 8], override=(count // 8) % 2, sync=count % 4)
            memory.update(fixture(leaf_args, base, phase, self.original))
            key = expected(memory, leaf_args)[0]
            for n, (address, value) in enumerate(zip((cache.IMAGE, cache.WIDTH, cache.HEIGHT, cache.VALUE, cache.ATTACHMENT),
                    (key, args[3], args[4], args[5], args[8]))):
                cache.put(memory, address, value ^ (0x100 if count % 6 == n + 1 else 0))
            wanted, result, calls, _ = cache.reference(memory, args, key=key)
            models = []
            for n, leaf in enumerate((self.words, self.retail)):
                connected = {screen.ENTRY + i * 4: w for i, w in enumerate(leaf)}
                model = cache.TextureCacheOracle(main, memory, args, phase, connected=connected, key=key).run()
                self.assertEqual(cache.external(model.memory), wanted)
                self.assertEqual(model.r[2], result)
                self.assertEqual(model.calls, calls)
                models.append(model)
                coverage[n].update(model.visits)
            self.assertEqual(models[0].events, models[1].events)
            self.assertEqual(models[0].memory, models[1].memory)
            count += 1
        self.assertEqual(count, 486)
        required = set(range(cache.screen.ENTRY, cache.screen.ENTRY + 408, 4)) | set(range(screen.ENTRY, screen.ENTRY + 200, 4))
        self.assertEqual([sorted(required - c) for c in coverage], [[], []])
        self.receipt('connected', dict(cases=count, caller_words=102, resolver_words=50,
            all_words=True, submit='bounded model', original_cache_caller=True))

    def test_standalone_actual_padder_preserves_slot_table_and_all_relocation_carries(self):
        text, functions, relocations = parse_object(self.output / 'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['size'], 200)
        self.assertEqual(text[200:208], bytes(8))
        self.assertEqual(relocations[0x20], [('R_MIPS_HI16', '.rodata')])
        self.assertEqual(relocations[0x28], [('R_MIPS_LO16', '.rodata')])
        layout = self.output / 'layout.csv'
        layout.write_text('version,section,filename,function,address,end\nus,game,game_16EE20,func_1514306C,0x1514306C,0x15143134\n')
        assembly = emit_padded_assembly(self.output / 'selected.o', layout, 'game_16EE20', rodata_symbol=screen.ANCHOR)
        self.link_padded(assembly, 'standalone')
        self.receipt('padding', dict(bytes=200, alignment_tail=8, table_bytes=24, relocation_pairs=5, word_guards=0))

    def link_padded(self, assembly, name):
        source, obj = (self.output / (name + suffix) for suffix in ('.s', '.o'))
        source.write_text(assembly)
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(source)], check=True, capture_output=True)
        _, functions, relocations = parse_object(obj)
        self.assertEqual(functions[screen.FUNCTION]['size'], 200)
        self.assertEqual(len(relocations), 10)
        for alternate in (False, True):
            targets = dict(screen.SYMBOLS, **{screen.ANCHOR: screen.TABLE})
            if alternate:
                targets = {name: 0x90018004 + i * 0x10000 for i, name in enumerate(screen.SYMBOLS)}
                targets[screen.ANCHOR] = 0x90007FFC
            elf = self.output / ('%s-%d.elf' % (name, alternate))
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output / 'resolver.ld'), '-e', screen.FUNCTION,
                *['--defsym=%s=0x%X' % item for item in targets.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
            words = list(struct.unpack_from('>50I', screen.sections(elf)['.text'][1]))
            expected_words = list(self.retail)
            for hi, lo, symbol in ((0x20, 0x28, screen.ANCHOR), (0x34, 0x3C, 'D_800915B0'),
                    (0x40, 0x48, 'D_80091514'), (0x58, 0x64, 'D_80091564'), (0xA4, 0xAC, 'D_80090B60')):
                address = targets[symbol]
                expected_words[hi // 4] = expected_words[hi // 4] & 0xFFFF0000 | ((address + 0x8000) >> 16 & 65535)
                expected_words[lo // 4] = expected_words[lo // 4] & 0xFFFF0000 | (address & 65535)
            self.assertEqual(words, expected_words)

    def copied_owner(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        stub = 's32 func_1514306C() {\n    return 0;\n}'
        baseline = source.replace(screen.SELECTED, stub).replace(screen.PROTOTYPE, 's32 func_1514306C();')
        baseline = baseline.replace(screen.DECLARATIONS + '\n', '')
        self.assertIn(stub, baseline)
        selected = baseline.replace('/* Generated placeholder declarations. */', screen.DECLARATIONS + '\n/* Generated placeholder declarations. */')
        selected = selected.replace(stub, screen.SELECTED).replace('s32 func_1514306C();', screen.PROTOTYPE)
        old, old_warnings = compile_owner(self.root, self.output, baseline, 'owner-baseline')
        new, warnings = compile_owner(self.root, self.output, selected, 'owner-selected')
        self.assertEqual(warnings, old_warnings)
        self.assertEqual(len(warnings), 2)
        return old, new

    def test_copied_owner_preserves_neighbors_and_existing_pool_then_appends_exact_table(self):
        old, new = self.copied_owner()
        old_text, old_functions, old_relocations = parse_object(old)
        text, functions, relocations = parse_object(new)
        self.assertEqual(set(functions), set(old_functions))
        for name, f in functions.items():
            if name == screen.FUNCTION: continue
            prior = old_functions[name]
            current = bytearray(text[f['value']:f['value'] + f['size']])
            previous = bytearray(old_text[prior['value']:prior['value'] + prior['size']])
            if name == output_mode.FUNCTION:
                self.assertEqual(struct.unpack_from('>I', previous, 0x20)[0], 0x8C2E0258)
                self.assertEqual(struct.unpack_from('>I', current, 0x20)[0], 0x8C2E0270)
                # Restoring this resolver inserts 24 bytes before the later output table.
                struct.pack_into('>I', previous, 0x20, 0x8C2E0000)
                struct.pack_into('>I', current, 0x20, 0x8C2E0000)
            elif name == secondary_output.FUNCTION:
                self.assertEqual(struct.unpack_from('>I', previous, 0x1C)[0], 0x8C2E026C)
                self.assertEqual(struct.unpack_from('>I', current, 0x1C)[0], 0x8C2E0284)
                struct.pack_into('>I', previous, 0x1C, 0x8C2E0000)
                struct.pack_into('>I', current, 0x1C, 0x8C2E0000)
            self.assertEqual(current, previous, name)
            self.assertEqual({o - f['value']: r for o, r in relocations.items() if f['value'] <= o < f['value'] + f['size']},
                {o - prior['value']: r for o, r in old_relocations.items() if prior['value'] <= o < prior['value'] + prior['size']}, name)
        old_pool, pool = screen.sections(old)['.rodata'][1], screen.sections(new)['.rodata'][1]
        self.assertEqual((len(old_pool), len(pool)), (688, 704))
        self.assertEqual(old_pool[:600], pool[:600])
        old_normal, new_normal = normalized_pools(old)['.rodata'], normalized_pools(new)['.rodata']
        self.assertEqual(old_normal[0][:600], new_normal[0][:600])
        self.assertEqual(old_normal[0][600:676], new_normal[0][624:700])
        self.assertEqual(old_pool[676:], bytes(12)); self.assertEqual(pool[700:], bytes(4))
        self.assertEqual(tuple((o + 24, n, r) for o, n, r in old_normal[1] if o >= 600),
            tuple(item for item in new_normal[1] if item[0] >= 624))
        self.assertEqual(tuple(item for item in old_normal[1] if item[0] < 600),
            tuple(item for item in new_normal[1] if item[0] < 600))
        target = functions[screen.FUNCTION]
        self.assertEqual(target['size'], 200)
        start = target['value']
        self.assertEqual([x - start + screen.ENTRY for x in struct.unpack_from('>6I', pool, 600)], list(struct.unpack('>6I', self.original)))
        adjusted = bytearray(text[start:start + 200])
        struct.pack_into('>I', adjusted, 0x28, struct.unpack_from('>I', adjusted, 0x28)[0] - 600)
        standalone, _, standalone_relocations = parse_object(self.output / 'selected.o')
        self.assertEqual(adjusted, standalone[:200])
        self.assertEqual({o - start: r for o, r in relocations.items() if start <= o < start + 200}, standalone_relocations)
        self.assertEqual(screen.sections(old).get('.data'), screen.sections(new).get('.data'))
        self.receipt('owner', dict(functions=len(functions), unchanged=len(functions) - 1, warnings=2,
            prior_pool=688, retained_payload=600, new_pool=704, table_addend=600,
            later_output_tables_retained=2,only_later_compact_table_addends_change=True,caller_raw_unchanged=True))

    def test_owner_padder_binds_original_table_and_stale_words_or_relocations_fail(self):
        _, owner = self.copied_owner()
        processed = self.output / 'owner-postprocessed.o'
        shutil.copyfile(owner, processed)
        subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
            str((self.output / 'owner-selected.c').relative_to(self.root / 'conker')), '--post-process',
            str(processed.relative_to(self.root / 'conker')), '--assembler',
            'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
            '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker',
            check=True, capture_output=True)
        owner = processed
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows = list(csv.DictReader(stream))
        rows = [r for r in rows if r['function'] != screen.FUNCTION] + screen.owner_guards()
        guards = self.output / 'owner-guards.csv'

        def write(items):
            with guards.open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=list(items[0]))
                writer.writeheader()
                writer.writerows(items)

        write(rows)
        assembly = emit_padded_assembly(owner, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
            rodata_symbol='jtbl_800A5218_game', word_patches_path=guards)
        begin = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), begin)
        end = assembly.index('\n', end)
        self.link_padded('.text\n.globl %s\n' % screen.FUNCTION + assembly[begin:end + 1], 'owner-padded-target')
        for field, value in (('expected', '0x8C2F025C'), ('expected_relocations', 'R_MIPS_LO16:D_800915B0')):
            altered = [dict(r) for r in rows]
            altered[-1][field] = value
            write(altered)
            with self.assertRaisesRegex(ValueError, 'stale'):
                emit_padded_assembly(owner, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
                    rodata_symbol='jtbl_800A5218_game', word_patches_path=guards)
        self.receipt('owner-padding', dict(bytes=200, guards=2, instruction_changes='only compact table addend',
            retail_table_binding=True, stale_word=True, stale_relocation=True, alternate_carries=True))

    def test_production_source_target_neighbors_original_table_owner_and_guard_history(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.SELECTED, source)
        self.assertEqual(source.count(screen.PROTOTYPE), 1)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        self.assertEqual(functions[cache.screen.FUNCTION], list(struct.unpack_from('>102I', self.rom, cache.screen.ROM)))
        address, data = screen.sections(self.root / 'conker/build/conker.us.elf')['.game_data']
        self.assertEqual(data[screen.TABLE - address:screen.TABLE - address + 24], self.original)
        self.assertEqual(len(self.owners), 1)
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        digest = assert_guard_history(self, guards)
        self.receipt('production', dict(words=50, table_guards=2, guards=len(guards), guard_sha256=digest,
            caller_words=102, table_owner=self.owners))


if __name__ == '__main__':
    unittest.main()
