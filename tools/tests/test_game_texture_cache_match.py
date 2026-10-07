"""Cached submission, original resolver execution and live callback boundaries."""

import csv
import itertools
import json
import struct
import tempfile
import unittest
from pathlib import Path
from tools.tests.game_owner_pool import normalized_pools, assert_guard_history
from tools.experiments import game_texture_resolver_candidates as resolver

from tools.experiments import game_texture_cache_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_random_curve_record as native
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.game_animation_timeline_oracle import signed
from tools.tests.test_game_grid_channel_updater_match import STACK, external, put
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
import subprocess

RESOLVE, SUBMIT = 0x1514306C, 0x15094FE8
IMAGE, WIDTH, HEIGHT, VALUE, ATTACHMENT = 0x800DD1B0, 0x800DD208, 0x800DD20C, 0x800DD210, 0x800DD214
WORLD, OVERRIDE = 0x800BE9F0, 0x800BE616
OUTPUT, SYNC, SOURCE, OTHER, KEY = 0x20020, 0x21004, 0x24000, 0x27000, 0x87654321
WORLDS = (0, 0x18, 0x13, 6, 0x3B, 2, 0x80000018, 0xFFFFFFFF)


def read(memory, address, size=4):
    return int.from_bytes(bytes(memory[address + i] for i in range(size)), 'big')


def arguments(packed=0x0002AB00, alias=0):
    sync = (SYNC, OUTPUT + 3, WIDTH + 3)[alias]
    return (OUTPUT, SOURCE, packed, 0x1234, 0x87654321, 0xFFFFFFFF,
        3, 0xFFFF0006, 0x26000, sync, 0xCAFEBABE)


def memory_case(args, world=0, override=0, miss=0, sync=1, key=KEY):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x600, 0x100)}
    for base, size in ((OUTPUT - 16, 176), (SYNC - 4, 32), (SOURCE, 32),
            (0x26000, 32), (OTHER, 32), (IMAGE - 8, 24), (WIDTH - 8, 40),
            (WORLD - 4, 16), (OVERRIDE - 4, 16)):
        memory.update({base + i: (i * 31 + 7) & 255 for i in range(size)})
    for index, (address, value) in enumerate(zip((IMAGE, WIDTH, HEIGHT, VALUE, ATTACHMENT),
            (key, args[3], args[4], args[5], args[8]))):
        put(memory, address, value ^ (0x100 if miss == index + 1 else 0))
    put(memory, WORLD, world)
    put(memory, OVERRIDE, override, 1)
    put(memory, args[9], sync, 1)
    return memory


def actions(stage, mutate):
    if not mutate:
        return ()
    if stage == RESOLVE:
        return ((WORLD, 2, 4), (OVERRIDE, 0x80, 1), (WIDTH, 0x777, 4))
    return ((ATTACHMENT, 0xA1234560, 4), (IMAGE, 0, 4), (WIDTH, 0, 4),
        (HEIGHT, 0, 4), (VALUE, 0, 4))


def reference(memory, args, key=KEY, mutate=False, home=None):
    memory, current = dict(memory), list(args)
    calls, writes = [], []

    def store(address, value, size=4):
        put(memory, address, value, size)
        writes.append(('W', address, size, value & ((1 << (size * 8)) - 1)))

    def callback(target):
        for address, value, size in actions(target, mutate):
            store(address, value, size)
        if home is not None and home[0] == target:
            current[home[1]] = home[2]

    resolve_args = (args[1], args[6], signed(args[2]) >> 16 & 0xFFFFFFFF, args[7] & 255)
    calls.append((RESOLVE, resolve_args, external(memory)))
    callback(RESOLVE)
    cached = tuple(read(memory, address) for address in (IMAGE, WIDTH, HEIGHT, VALUE, ATTACHMENT))
    if cached == (key, current[3], current[4], current[5], current[8]):
        return external(memory), current[0], calls, writes
    if read(memory, current[9], 1) == 1:
        store(current[9], 0, 1)
    flags = 3 if read(memory, WORLD) in WORLDS[1:6] or read(memory, OVERRIDE, 1) != 0 else current[10]
    submit_args = (current[0], current[1], signed(current[2]) >> 8 & 0xFFFFFFFF,
        current[8], 0, 0, 0, current[3], current[4], current[5], flags)
    calls.append((SUBMIT, submit_args, external(memory)))
    store(current[0], 0xFD123456)
    store(current[0] + 4, flags)
    result = current[0] + 8
    callback(SUBMIT)
    for address, value in zip((IMAGE, WIDTH, HEIGHT, VALUE), (key, current[3], current[4], current[5])):
        store(address, value)
    store(ATTACHMENT, read(memory, ATTACHMENT))
    return external(memory), result, calls, writes


class TextureCacheOracle(TriangleOracle):
    def __init__(self, words, memory, args, phase=0, mutate=False, home=None, connected=None, key=KEY):
        super().__init__(words, memory, phase=phase, connected=connected,
            entry=screen.ENTRY, arguments=args)
        self.key, self.change, self.home, self.phase = key, mutate, home, phase

    def record_call(self, target):
        self.calls.append((target, self.arguments(4 if target == RESOLVE else 11), external(self.memory)))

    def hook(self, target):
        assert target in (RESOLVE, SUBMIT), hex(target)
        result = self.key
        if target == SUBMIT:
            args = self.arguments(11)
            self.put(args[0], 0xFD123456, 4)
            self.put(args[0] + 4, args[10], 4)
            result = args[0] + 8
        for address, value, size in actions(target, self.change):
            self.put(address, value, size)
        if self.home is not None and self.home[0] == target:
            self.put(STACK + self.phase + self.home[1] * 4, self.home[2], 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.r[2] = result


class GameTextureCacheMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-texture-cache-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>102I', cls.rom, screen.ROM))
        cls.resolver = list(struct.unpack_from('>50I', cls.rom, 0x17051C))
        address, data = screen.sections(cls.root / 'conker/build/conker.us.elf')['.game_data']
        cls.jump = struct.unpack_from('>6I', data, 0x800A562C - address)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, value):
        (self.output / (name + '.json')).write_text(json.dumps(value, indent=2) + '\n')

    def compare(self, memory, args, phase=0, mutate=False, home=None, connected=None, key=KEY):
        expected, result, calls, writes = reference(memory, args, key, mutate, home)
        models = []
        for words in (self.words, self.retail):
            model = TextureCacheOracle(words, memory, args, phase, mutate, home, connected, key).run()
            self.assertEqual(external(model.memory), expected)
            self.assertEqual(model.r[2], result)
            self.assertEqual(model.calls, calls)
            self.assertEqual([event for event in model.events if event[0] == 'W'
                and not STACK - 0x600 <= event[1] < STACK + 0x100], writes)
            models.append(model)
        self.assertEqual(models[0].events, models[1].events)
        self.assertEqual(models[0].memory, models[1].memory)
        return models

    def test_thirty_two_controls_and_direct_complete_slot(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (102, 0x40, 0))
        self.assertEqual(self.words, self.retail)
        controls = []
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                record, _ = screen.compile_candidate(self.root, self.output, name + '-' + profile, body, profile)
                controls.append(record)
        self.assertEqual(len(controls), 32)
        self.assertEqual(sum(record['differences'] == 0 for record in controls), 1)
        self.assertTrue(all(not record['diagnostics'] for record in controls))
        self.receipt('controls', controls)

    def test_guest_cache_hit_each_miss_signed_packed_fields_worlds_sync_aliases_mutations(self):
        count, coverage = 0, [set(), set()]
        for world, override, miss, sync, packed, phase in itertools.product(WORLDS,
                (0, 0x80), range(6), (0, 1, 2, 255), (0x0002AB00, 0xFFFFEFCD, 0x80000001), (0, 8)):
            args = arguments(packed, count % 3)
            memory = memory_case(args, world, override, miss, sync)
            for index, model in enumerate(self.compare(memory, args, phase, bool(count % 2))):
                coverage[index].update(model.visits)
            count += 1
        self.assertEqual(count, 2304)
        self.assertEqual([len(c) for c in coverage], [102, 102])
        self.receipt('guest', dict(cases=count, bodies=2, covered_words=[102, 102],
            full_traces=True, full_memory=True, helper_models=True, sync_aliases=3))

    def test_guest_only_live_argument_homes_at_both_helpers(self):
        count = 0
        for stage, index, phase, pattern in itertools.product((RESOLVE, SUBMIT), range(11), (0, 8), (0, 1)):
            args = arguments()
            replacement = ({0: OUTPUT + 32, 1: OTHER, 8: OTHER, 9: SYNC + 8}.get(index,
                (0x87654321, 0x12345678)[pattern]))
            memory = memory_case(args, miss=1)
            self.compare(memory, args, phase, home=(stage, index, replacement))
            count += 1
        self.assertEqual(count, 88)
        self.receipt('homes', dict(cases=count, native_private_home_claim=False))

    def test_original_fifty_word_resolver_all_switch_paths_and_threshold(self):
        self.assertEqual(self.jump, (0x151430B8, 0x151430C0, 0x151430AC, 0x151430A0, 0x151430D4, 0x151430DC))
        count, coverage = 0, [set(), set()]
        connected = {RESOLVE + i * 4: word for i, word in enumerate(self.resolver)}
        for kind, index, subindex, base, phase in itertools.product((0, 1, 2, 3, 4, 5, 6, 7, 255),
                (-2, 0, 2), (-2, 0, 2), (0x0FFFFFFF, 0x10000000, 0x80050000), (0, 8)):
            args = list(arguments())
            args[2], args[6], args[7] = (subindex << 16 | 0xAB00) & 0xFFFFFFFF, index & 0xFFFFFFFF, kind | 0xABCD0000
            memory = memory_case(tuple(args), world=WORLDS[count % 8],
                override=(count // 8) % 2, sync=count % 4)
            for address in (0x800915B0, 0x80091514, 0x80091564, 0x80090B60, 0x80060000, 0x10000000, 0x80050000):
                memory.update({address + i: 0xA5 for i in range(-32, 80)})
            for i, target in enumerate(self.jump):
                put(memory, 0x800A562C + i * 4, target)
            put(memory, 0x800915B0, 0x11223344)
            put(memory, 0x80091514, 0x55667788)
            put(memory, 0x80091564 + index * 4, 0x89ABCDEF)
            put(memory, 0x80090B60 + index * 12, 0x80060000)
            put(memory, 0x80060000 + subindex * 4, 0xABCDEF01)
            put(memory, SOURCE, base)
            if base >= 0x10000000:
                put(memory, base + subindex * 4, 0xDEADBEEF)
            key = {1: 0, 2: 0x89ABCDEF, 3: 0x55667788, 4: 0x11223344,
                5: index & 0xFFFFFFFF, 6: 0xDEADBEEF if base >= 0x10000000 else base}.get(kind, 0xABCDEF01)
            put(memory, IMAGE, key)
            miss = count % 6
            if miss:
                address = (IMAGE, WIDTH, HEIGHT, VALUE, ATTACHMENT)[miss - 1]
                put(memory, address, read(memory, address) ^ 0x100)
            for n, model in enumerate(self.compare(memory, tuple(args), phase, connected=connected, key=key)):
                coverage[n].update(model.visits)
            count += 1
        expected = set(range(screen.ENTRY, screen.ENTRY + 408, 4)) | set(range(RESOLVE, RESOLVE + 200, 4))
        self.assertEqual(count, 486)
        self.assertEqual(coverage, [expected, expected])
        self.receipt('resolver', dict(cases=count, main_words=102, resolver_words=50,
            all_words=True, submit='bounded model', table_from_exact_game_data=True))

    def test_mapped_memory_gates_and_hit_does_not_read_sync(self):
        args = arguments()
        memory = memory_case(args)
        del memory[args[9]]
        self.compare(memory, args)
        memory = memory_case(args, miss=1)
        del memory[args[9]]
        with self.assertRaisesRegex(AssertionError, 'unmapped'):
            TextureCacheOracle(self.words, memory, args).run()
        for address in (IMAGE, WIDTH, WORLD, OUTPUT):
            memory = memory_case(args, miss=1)
            del memory[address]
            with self.assertRaisesRegex(AssertionError, 'unmapped'):
                TextureCacheOracle(self.words, memory, args).run()

    def test_compiled_negatives_include_observable_same_value_store(self):
        source = screen.SELECTED
        forms = {
            'placeholder': screen.PROTOTYPE[:-1] + ' { return output; }',
            'unsigned-index': source.replace('packed >> 16', '(u32)packed >> 16'),
            'unsigned-packed': source.replace('packed >> 8', '(u32)packed >> 8'),
            'missing-resolver': source.replace('func_1514306C(source, index, packed >> 16, kind)', '0'),
            'missing-submit': source.replace('output = (Gfx *)func_15094FE8((s32)output, source, packed >> 8, attachment, 0, 0, 0,\n            width, height, value, flags);', ''),
            'wrong-hit-gate': source.replace('image != D_800DD1B0', 'image == D_800DD1B0'),
            'wrong-sync': source.replace('*sync == 1', '*sync != 0'),
            'wrong-flags': source.replace('flags = 3', 'flags = 2'),
            'write-attachment': source.replace('*(u8 *volatile *)&D_800DD214 = *(u8 *volatile *)&D_800DD214;', 'D_800DD214 = attachment;'),
            'missing-self-store': source.replace('*(u8 *volatile *)&D_800DD214 = *(u8 *volatile *)&D_800DD214;', '')}
        results = []
        args = arguments(0xFFFFEFCD)
        for name, body in forms.items():
            self.assertNotEqual(body, source)
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            changed = 0
            for miss, sync, mutate in itertools.product((0, 1), (1, 2), (False, True)):
                memory = memory_case(args, world=2, miss=miss, sync=sync)
                wanted, result, calls, writes = reference(memory, args, mutate=mutate)
                model = TextureCacheOracle(words, memory, args, mutate=mutate).run()
                actual_writes = [event for event in model.events if event[0] == 'W'
                    and not STACK - 0x600 <= event[1] < STACK + 0x100]
                changed += (external(model.memory), model.r[2], model.calls, actual_writes) != (wanted, result, calls, writes)
            self.assertGreater(changed, 0, name)
            results.append(dict(name=name, valid_mapped_cases=8, changes=changed))
        self.receipt('negatives', results)

    def test_actual_32_bit_native_typed_helpers_aliases_and_complete_external_storage(self):
        declarations = screen.DECLARATIONS.replace('s32 func_1514306C(GameTextureSource *source, s32 index, s32 subindex, u8 kind);\n', '')
        self.fixture = ('typedef unsigned char u8; typedef unsigned short u16; typedef int s32; typedef unsigned int u32;\n'
            'typedef struct { struct { u32 w0,w1; } words; } Gfx;\n' + declarations + r'''
s32 D_800DD1B0,D_800DD208,D_800DD20C,D_800DD210,D_800BE9F0;
u8 *D_800DD214; u8 D_800BE616;
static Gfx output[12],expected[12]; static GameTextureSource sourceRecord;
static u8 syncByte; static int mutation,resolveCalls,submitCalls;
static u32 resolved[4],submitted[11];
s32 func_1514306C(GameTextureSource *source,s32 index,s32 subindex,u8 kind) {
    resolveCalls++; resolved[0]=(u32)source; resolved[1]=(u32)index;
    resolved[2]=(u32)subindex; resolved[3]=kind;
    if(mutation) { D_800BE9F0=2; D_800BE616=0x80; D_800DD208=0x777; }
    return (s32)0x87654321u;
}
s32 func_15094FE8(s32 out,GameTextureSource *source,s32 packed,u8 *attachment,
    s32 zero0,s32 zero1,s32 zero2,s32 width,s32 height,s32 value,s32 flags) {
    u32 *words=(u32 *)out; submitCalls++;
    submitted[0]=(u32)out;submitted[1]=(u32)source;submitted[2]=(u32)packed;
    submitted[3]=(u32)attachment;submitted[4]=(u32)zero0;submitted[5]=(u32)zero1;
    submitted[6]=(u32)zero2;submitted[7]=(u32)width;submitted[8]=(u32)height;
    submitted[9]=(u32)value;submitted[10]=(u32)flags;
    words[0]=0xFD123456;words[1]=(u32)flags;
    if(mutation) { D_800DD214=(u8 *)0xA1234560u;D_800DD1B0=0;
        D_800DD208=0;D_800DD20C=0;D_800DD210=0; }
    return out+8;
}
''' + screen.SELECTED + '\n')
        self.run_host(r'''
static u32 worlds[]={0,0x18,0x13,6,0x3B,2,0x80000018u,0xFFFFFFFFu};
static u32 packedWords[]={0x0002AB00,0xFFFFEFCDu,0x80000001u};
static u8 syncValues[]={0,1,2,255};
int w,o,m,s,p,a,h,i,j,count=0,changed,special;u32 flags,oldAttachment;
u8 *sync;Gfx *result; s32 packed; u32 want[11],cache[5];
for(w=0;w<8;w++)for(o=0;o<2;o++)for(m=0;m<6;m++)for(s=0;s<4;s++)
for(p=0;p<3;p++)for(a=0;a<3;a++)for(h=0;h<2;h++) {
    for(i=0;i<12;i++) output[i].words.w0=output[i].words.w1=0xA5A5A5A5u;
    D_800DD1B0=(s32)(0x87654321u^(m==1?0x100u:0));
    D_800DD208=(s32)(0x1234u^(m==2?0x100u:0));
    D_800DD20C=(s32)(0x87654321u^(m==3?0x100u:0));
    D_800DD210=(s32)(0xFFFFFFFFu^(m==4?0x100u:0));
    D_800DD214=(u8 *)(0x26000u^(m==5?0x100u:0));
    D_800BE9F0=(s32)worlds[w];D_800BE616=o?0x80:0;mutation=h;
    resolveCalls=submitCalls=0;packed=(s32)packedWords[p];
    sync=a==0?&syncByte:a==1?(u8 *)&output[2]+3:(u8 *)&D_800DD208+3;
    *sync=syncValues[s];
    for(i=0;i<12;i++)expected[i]=output[i];
    cache[0]=(u32)D_800DD1B0;cache[1]=(u32)D_800DD208;cache[2]=(u32)D_800DD20C;
    cache[3]=(u32)D_800DD210;cache[4]=(u32)D_800DD214;
    if(h)cache[1]=0x777;
    changed=cache[0]!=0x87654321u || cache[1]!=0x1234u || cache[2]!=0x87654321u
        || cache[3]!=0xFFFFFFFFu || cache[4]!=0x26000u;
    special=h || o || worlds[w]==0x18 || worlds[w]==0x13 || worlds[w]==6
        || worlds[w]==0x3B || worlds[w]==2;
    flags=special?3:0xCAFEBABEu;oldAttachment=cache[4];
    if(changed) {
        if(a==1 && syncValues[s]==1)((u8 *)&expected[2])[3]=0;
        expected[2].words.w0=0xFD123456;expected[2].words.w1=flags;
    }
    result=func_15142E24(output+2,&sourceRecord,packed,0x1234,(s32)0x87654321u,
        -1,3,(u8)0xFFFF0006u,(u8 *)0x26000u,sync,(s32)0xCAFEBABEu);
    if(result!=output+2+(changed?1:0) || resolveCalls!=1 || submitCalls!=changed)return 1;
    if(resolved[0]!=(u32)&sourceRecord || resolved[1]!=3
        || resolved[2]!=(u32)(packed>>16) || resolved[3]!=6)return 2;
    if(changed) {
        want[0]=(u32)(output+2);want[1]=(u32)&sourceRecord;want[2]=(u32)(packed>>8);
        want[3]=0x26000;want[4]=want[5]=want[6]=0;want[7]=0x1234;
        want[8]=0x87654321u;want[9]=0xFFFFFFFFu;want[10]=flags;
        for(i=0;i<11;i++)if(submitted[i]!=want[i])return 3;
        cache[0]=0x87654321u;cache[1]=0x1234;cache[2]=0x87654321u;cache[3]=0xFFFFFFFFu;
        cache[4]=h?0xA1234560u:oldAttachment;
    }
    if((u32)D_800DD1B0!=cache[0] || (u32)D_800DD208!=cache[1]
        || (u32)D_800DD20C!=cache[2] || (u32)D_800DD210!=cache[3]
        || (u32)D_800DD214!=cache[4])return 4;
    if(a==0 && syncByte!=(changed && syncValues[s]==1?0:syncValues[s]))return 5;
    for(j=0;j<(int)sizeof(output);j++)if(((u8 *)output)[j]!=((u8 *)expected)[j])return 6;
    count++;
}
if(count!=6912 || sizeof(void *)!=4 || sizeof(GameTextureSource)!=12 || sizeof(Gfx)!=8)return 7;
''')
        self.receipt('native', dict(cases=6912, bits=32, actual_source=True, typed_helpers=True,
            external_storage=True, helpers='bounded models', private_home_claim=False))

    def test_actual_padder_preserves_slot_and_all_relocations(self):
        text, functions, relocations = parse_object(self.output / 'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['size'], 408)
        self.assertEqual(text[408:416], bytes(8))
        self.assertEqual(relocations[0x2C], [('R_MIPS_26', 'func_1514306C')])
        self.assertEqual(relocations[0x138], [('R_MIPS_26', 'func_15094FE8')])
        layout = self.output / 'layout.csv'
        layout.write_text('version,section,filename,function,address,end\n'
            'us,game,game_16EE20,func_15142E24,0x15142E24,0x15142FBC\n')
        assembly = self.output / 'padded.s'
        assembly.write_text(emit_padded_assembly(self.output / 'selected.o', layout, 'game_16EE20'))
        obj = self.output / 'padded.o'
        subprocess.run(['mips-linux-gnu-as', '-EB', '-march=vr4300', '-o', str(obj), str(assembly)], check=True, capture_output=True)
        padded, symbols, mapped = parse_object(obj)
        self.assertEqual(symbols[screen.FUNCTION]['size'], 408)
        self.assertEqual(padded[:408], text[:408])
        self.assertEqual(mapped, relocations)
        targets = dict(screen.SYMBOLS)
        targets['func_1514306C'] += 0x1000000
        targets['func_15094FE8'] += 0x1000000
        elf = self.output / 'padded.elf'
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(self.output / 'texture-cache.ld'), '-e', screen.FUNCTION,
            *['--defsym=%s=0x%X' % item for item in targets.items()], '-o', str(elf), str(obj)], check=True, capture_output=True)
        words = list(struct.unpack_from('>102I', screen.sections(elf)['.text'][1]))
        expected = list(self.retail)
        for offset, name in ((0x2C, 'func_1514306C'), (0x138, 'func_15094FE8')):
            expected[offset // 4] = 0x0C000000 | (targets[name] >> 2 & 0x3FFFFFF)
        self.assertEqual(words, expected)
        self.receipt('padding', dict(bytes=408, alignment_tail=8, retargeted_calls=2, guards=0))

    def test_copied_owner_retains_all_other_functions_pool_warnings_and_standalone(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        stub = 's32 func_15142E24() {\n    return 0;\n}'
        # The recovered resolver also needs this shared source-record type.
        declarations = screen.DECLARATIONS.replace(
            's32 func_1514306C(GameTextureSource *source, s32 index, s32 subindex, u8 kind);\n', '')
        if screen.SELECTED in source:
            baseline = source.replace(screen.SELECTED, stub).replace(screen.PROTOTYPE, 's32 func_15142E24();')
            if 's32 func_1514306C() {' in baseline:
                baseline = baseline.replace(declarations + '\n', '')
        else:
            baseline = source
        self.assertIn(stub, baseline)
        selected = baseline
        if declarations not in selected:
            selected = selected.replace('/* Generated placeholder declarations. */',
                declarations + '\n/* Generated placeholder declarations. */')
        selected = selected.replace(stub, screen.SELECTED).replace('s32 func_15142E24();', screen.PROTOTYPE)
        old, old_warnings = compile_owner(self.root, self.output, baseline, 'owner-baseline')
        new, warnings = compile_owner(self.root, self.output, selected, 'owner-selected')
        self.assertEqual(warnings, old_warnings)
        old_text, old_functions, old_relocations = parse_object(old)
        text, functions, relocations = parse_object(new)
        self.assertEqual(set(functions), set(old_functions))
        for name, meta in functions.items():
            if name == screen.FUNCTION:
                continue
            old_meta = old_functions[name]
            self.assertEqual(text[meta['value']:meta['value'] + meta['size']],
                old_text[old_meta['value']:old_meta['value'] + old_meta['size']], name)
            self.assertEqual({a - meta['value']: r for a, r in relocations.items() if meta['value'] <= a < meta['value'] + meta['size']},
                {a - old_meta['value']: r for a, r in old_relocations.items() if old_meta['value'] <= a < old_meta['value'] + old_meta['size']}, name)
        standalone, _, standalone_relocations = parse_object(self.output / 'selected.o')
        target = functions[screen.FUNCTION]
        self.assertEqual(target['size'], 408)
        self.assertEqual(text[target['value']:target['value'] + 408], standalone[:408])
        self.assertEqual({a - target['value']: r for a, r in relocations.items() if target['value'] <= a < target['value'] + 408},
            standalone_relocations)
        self.assertEqual(normalized_pools(old), normalized_pools(new))
        self.receipt('owner', dict(functions=len(functions), unchanged=len(functions) - 1,
            warnings=len(warnings), raw_target_standalone=True, resolver_raw_unchanged=True,
            pools='relocation-owned function-relative targets and exact other bytes'))

    def test_nine_original_caller_call_delay_pairs_preserve_argument_vector(self):
        sources = list((self.root / 'conker/asm/nonmatchings').rglob('*.s'))
        call_word = 0x0C000000 | (screen.ENTRY >> 2 & 0x3FFFFFF)
        pairs = []
        import re
        for source in sources:
            text = source.read_text()
            if 'jal        func_15142E24' not in text:
                continue
            instructions = [(int(a, 16), int(w, 16)) for a, w in re.findall(
                r'/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+([0-9A-Fa-f]{8})\s*\*/', text)]
            for i, (address, word) in enumerate(instructions):
                if word != call_word:
                    continue
                self.assertEqual(instructions[i + 1][0], address + 4)
                pairs.append((address, word, instructions[i + 1][1]))
        self.assertEqual(len(pairs), 9)
        count = 0
        for address, call, delay in pairs:
            args = arguments()
            memory = memory_case(args, miss=1)
            memory.update({STACK + i: 0xA5 for i in range(0x100, 0x120)})
            registers = {2: OUTPUT, 8: 0x11223344, 10: SYNC, 12: args[6]}
            forwarded, prepared = list(args), dict(memory)
            op, rs, rt, immediate = delay >> 26, delay >> 21 & 31, delay >> 16 & 31, delay & 65535
            # Independently decode the nine actual outgoing-argument/private-store delays.
            if op == 9:
                self.assertEqual((rs, rt, immediate), (0, 7, 2))
                forwarded[3] = 2
            else:
                self.assertEqual((op, rs), (43, 29))
                value = 0 if rt == 0 else registers[rt]
                put(prepared, STACK + immediate, value)
                if 0x10 <= immediate <= 0x28:
                    forwarded[immediate // 4] = value
            expected, result, calls, _ = reference(prepared, tuple(forwarded))
            # Only the original call/delay pair is retained; the return sentinel is synthetic.
            wrapper = [call, delay, 0x3C1FDEAD, 0x03E00008, 0]
            connected = {address + i * 4: word for i, word in enumerate(wrapper)}
            models = []
            for words in (self.words, self.retail):
                model = TextureCacheOracle(words, memory, args, connected=connected)
                model.entry = address
                for register, value in registers.items():
                    model.r[register] = value
                original_record = model.record_call
                model.record_call = lambda target: (setattr(model, 'forwarded', model.arguments(11))
                    if target == screen.ENTRY else original_record(target))
                model.run()
                self.assertEqual(model.forwarded, tuple(forwarded))
                self.assertEqual(external(model.memory), expected)
                self.assertEqual(model.r[2], result)
                self.assertEqual(model.calls, calls)
                self.assertTrue({address, address + 4}.issubset(model.visits))
                models.append(model)
            self.assertEqual(models[0].events, models[1].events)
            self.assertEqual(models[0].memory, models[1].memory)
            count += 1
        self.receipt('callers', dict(original_pairs=count, whole_callers=False,
            delay_words_executed=True, argument_vector_checked=True))

    def test_production_source_target_neighbors_and_unchanged_guards(self):
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.SELECTED, source)
        self.assertEqual(source.count(screen.PROTOTYPE), 1)
        self.assertIn(resolver.SELECTED, source)
        self.assertIn('s32 func_15142600() {\n    return 0;\n}', source)
        functions, _, addresses = load_elf_functions(str(self.root / 'conker/build/conker.us.elf'), 'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION], screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION], self.retail)
        neighbors = (('func_15141A7C', 0x16EF2C, 100), ('func_15141C0C', 0x16F0BC, 45),
            ('func_15141CC0', 0x16F170, 57), ('func_15141DA4', 0x16F254, 37),
            ('func_15141E38', 0x16F2E8, 80), ('func_15141F78', 0x16F428, 96),
            ('func_15142180', 0x16F630, 80), ('func_151424F4', 0x16F9A4, 67),
            ('func_15142838', 0x16FCE8, 55))
        for name, rom, count in neighbors:
            self.assertEqual(functions[name], list(struct.unpack_from('>%dI' % count, self.rom, rom)))
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards = list(csv.DictReader(stream))
        self.assertFalse(any(row['function'] == screen.FUNCTION for row in guards))
        digest = assert_guard_history(self, guards)
        self.receipt('production', dict(words=102, direct=True, guards=len(guards),
            guard_sha256=digest, exact_neighbors=len(neighbors), resolver_restored=True))


if __name__ == '__main__':
    unittest.main()
