"""Live XOR range ordering, signed limits and the original saved-pointer shape."""

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

from tools.experiments import game_range_clamp_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.pad_generated_object import parse_object
from tools.tests.game_owner_pool import normalized_pools
from tools.tests.game_owner_pool import assert_guard_history
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read
from tools.tests.test_game_queued_segment_writer import STACK
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests import test_game_random_curve_record as native

BUFFER = 0x24000
VALUES = (-2147483648, -1, 0, 1, 2147483647)


def fixture(a, b, low, high, alias=0, phase=0):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x100, 0x100)}
    memory.update({BUFFER + i: 0xA5 for i in range(32)})
    p, q = ((BUFFER, BUFFER + 4), (BUFFER, BUFFER), (STACK + phase + 0x20, STACK + phase + 0x24))[alias]
    put(memory, p, a); put(memory, q, b)
    return memory, (p, q, low & 0xFFFFFFFF, high & 0xFFFFFFFF)


class ClampOracle(TriangleOracle):
    def __init__(self, words, memory, args, phase=0):
        super().__init__(words, memory, arguments=args, phase=phase, entry=screen.ENTRY)

    def execute(self, word):
        if word >> 26 == 0 and word & 63 == 38:
            self.r[word >> 11 & 31] = self.r[word >> 21 & 31] ^ self.r[word >> 16 & 31]
            self.r[0] = 0
        else: super().execute(word)

    def record_call(self, target):
        assert target == screen.ENTRY
        self.forwarded = self.arguments(4)


def output_trace(model, args):
    return [e for e in model.events if e[0] in ('R', 'W') and e[1] in args[:2]]


class GameRangeClampMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-range-clamp-test'; cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>36I', cls.rom, screen.ROM))
        cls.directory = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, data):
        (self.output / (name + '.json')).write_text(json.dumps(data, indent=2) + '\n')

    def test_complete_slot_and_only_temporary_register_fields_differ(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (36, 16, 13))
        self.assertEqual(self.record['relocations'], {})
        changes = [i * 4 for i, (a, b) in enumerate(zip(self.words, self.retail)) if a != b]
        self.assertEqual(changes, [0x2C, 0x30, 0x34, 0x3C, 0x40, 0x48, 0x4C, 0x54, 0x58, 0x5C, 0x64, 0x6C, 0x70])
        for i, (a, b) in enumerate(zip(self.words, self.retail)):
            op = a >> 26
            mask = 0x03FFF800 if op == 0 else 0x001F0000 if op in (35, 43) else 0
            self.assertEqual(a & ~mask, b & ~mask, hex(i * 4))
            self.assertEqual(a >> 26, b >> 26)
        patched = self.words.copy()
        for row in screen.owner_guards():
            index = int(row['offset'], 16) // 4
            self.assertEqual(patched[index], int(row['expected'], 16))
            patched[index] = int(row['replacement'], 16)
        self.assertEqual(patched, self.retail)
        self.receipt('slot', dict(words=36, frame=16, guards=13, relocations=0,
            register_fields_only=True, branches_arithmetic_frame_stores_unchanged=True))

    def test_bounded_guest_signed_limits_aliases_caller_storage_and_all_words(self):
        count, coverage = 0, [set(), set()]
        for a, b, low, high, alias, phase in itertools.product(VALUES, VALUES, VALUES, VALUES, range(3), (0, 8)):
            memory, args = fixture(a, b, low, high, alias, phase)
            models = [ClampOracle(words, memory, args, phase).run() for words in (self.words, self.retail)]
            self.assertEqual(models[0].memory, models[1].memory)
            self.assertEqual(output_trace(models[0], args), output_trace(models[1], args))
            want0, want1 = sorted((a, b)) if alias != 1 else (b, b)
            lower, upper = sorted((low, high))
            if alias == 1:
                value = max(b, lower)
                want0 = want1 = min(value, upper)
            else:
                want0, want1 = max(want0, lower), min(want1, upper)
            self.assertEqual(read(models[0].memory, args[0]), want0 & 0xFFFFFFFF)
            self.assertEqual(read(models[0].memory, args[1]), want1 & 0xFFFFFFFF)
            for i, model in enumerate(models): coverage[i].update(model.visits)
            count += 1
        self.assertEqual([len(c) for c in coverage], [36, 36])
        self.receipt('guest', dict(cases=count, all_words=True, full_memory=True, ordered_output_reads_writes=True,
            aliases='distinct, identical, caller-owned stack storage', saved_state=True))

    def test_actual_native_32_bit_caller_signed_domain_and_aliases(self):
        self.fixture = 'typedef int s32;typedef unsigned int u32;\n' + screen.SELECTED + '\n'
        self.run_host('''static const s32 values[]={(-2147483647-1),-1,0,1,2147483647};
int i,j,k,l,alias; s32 storage[2],a,b,low,high,t,*p,*q;
if(sizeof(void *)!=4)return 1;
for(i=0;i<5;i++)for(j=0;j<5;j++)for(k=0;k<5;k++)for(l=0;l<5;l++)for(alias=0;alias<2;alias++) {
    p=storage;q=storage+(alias?0:1);*p=values[i];*q=values[j];a=*p;b=*q;
    low=values[k];high=values[l];if(high<low){t=low;low=high;high=t;}
    if(b<a){t=a;a=b;b=t;}if(a<low)a=low;
    if(alias)b=a;
    if(high<b)b=high;
    if(alias)a=b;
    func_15143D18(p,q,values[k],values[l]);
    if(*p!=a || *q!=b)return 2;
}
''')
        self.receipt('native', dict(cases=1250, bits=32, typed_caller=True, aliases=True, signed_extremes=True))

    def test_original_lookup_call_delay_pair_with_caller_argument_homes(self):
        address = 0x15143918
        pair = struct.unpack_from('>2I', self.rom, 0x170DC8)
        self.assertEqual(pair, (0x0D450F46, 0xAFA80058))
        count = 0
        for a, b, limit, phase in itertools.product(VALUES, VALUES, VALUES, (0, 8)):
            memory, _ = fixture(a,b,0,limit,phase=phase)
            args = (STACK+phase+0x60, STACK+phase+0x64, 0, limit & 0xFFFFFFFF)
            put(memory,args[0],a); put(memory,args[1],b)
            put(memory,STACK+phase+0x1C,0xDEAD0000)
            models=[]
            for words in (self.words,self.retail):
                model=ClampOracle(pair,memory,args,phase)
                model.entry=address
                model.code=dict(zip(range(address,address+20,4), (*pair,0x8FBF001C,0x03E00008,0)))
                model.code.update(zip(range(screen.ENTRY,screen.ENTRY+144,4),words))
                model.r[8]=0
                models.append(model.run())
            self.assertEqual(models[0].memory,models[1].memory)
            self.assertEqual(models[0].forwarded,args)
            self.assertEqual(read(models[0].memory,STACK+phase+0x58),0)
            count+=1
        self.receipt('caller-pair',dict(cases=count,original_call_delay=True,argument_homes=True,
            boundary='two original instructions, seeded context and synthetic return; not the whole lookup caller'))

    def test_baseline_and_profile_controls_preserve_behavior_not_slot_shape(self):
        report = []
        for name, body in (('baseline', screen.BASELINE), ('selected', screen.SELECTED)):
            for profile in screen.PROFILES:
                record, words = screen.compile_candidate(self.root, self.output, name + '-' + profile, body, profile)
                report.append(record)
                for a, b, low, high, alias in itertools.product((-1, 1), (-1, 1), (-1, 1), (-1, 1), (0, 1)):
                    memory, args = fixture(a, b, low, high, alias)
                    model = ClampOracle(words, memory, args).run()
                    original = ClampOracle(self.retail, memory, args).run()
                    self.assertEqual(output_trace(model, args), output_trace(original, args))
        self.assertEqual((report[0]['body_words'], report[0]['frame']), (29, 0))
        self.receipt('profiles', report)

    def copied_owner(self):
        if hasattr(self.__class__, 'owners'): return self.__class__.owners
        source = (self.root / 'conker/src/game_16EE20.c').read_text()
        self.assertTrue(screen.BASELINE in source or screen.SELECTED in source)
        baseline = source.replace(screen.SELECTED, screen.BASELINE)
        selected = baseline.replace(screen.BASELINE, screen.SELECTED)
        result, warnings = [], []
        for name, body in (('baseline', baseline), ('selected', selected)):
            obj, warning = compile_owner(self.root, self.output, body, 'owner-' + name)
            warnings.append(warning)
            processed = self.output / ('owner-' + name + '-postprocessed.o'); shutil.copyfile(obj, processed)
            subprocess.run([sys.executable, str(self.root / 'tools/asm-processor/asm_processor.py'), '-O2', '-g3',
                str((self.output / ('owner-' + name + '.c')).relative_to(self.root / 'conker')),
                '--post-process', str(processed.relative_to(self.root / 'conker')), '--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude', 'include/asm_processor_prelude.inc'], cwd=self.root / 'conker', check=True, capture_output=True)
            result.append(processed)
        self.assertEqual(warnings[0], warnings[1]); self.assertEqual(len(warnings[0]), 2)
        self.__class__.owners = result
        return result

    def test_copied_owner_neighbors_target_relocations_and_pools(self):
        old, new = self.copied_owner()
        old_text, old_functions, old_rel = parse_object(old)
        text, functions, rel = parse_object(new)
        self.assertEqual(set(functions), set(old_functions))
        for name, function in functions.items():
            if name == screen.FUNCTION: continue
            previous = old_functions[name]
            self.assertEqual(text[function['value']:function['value'] + function['size']],
                old_text[previous['value']:previous['value'] + previous['size']], name)
            self.assertEqual({o-function['value']:r for o,r in rel.items() if function['value']<=o<function['value']+function['size']},
                {o-previous['value']:r for o,r in old_rel.items() if previous['value']<=o<previous['value']+previous['size']},name)
        target = functions[screen.FUNCTION]
        self.assertEqual(struct.unpack_from('>36I', text, target['value']), tuple(self.words))
        self.assertFalse(any(target['value']<=o<target['value']+144 for o in rel))
        self.assertEqual(normalized_pools(old), normalized_pools(new))
        self.receipt('owner', dict(functions=len(functions), unchanged=len(functions)-1, warnings=2,
            target_identical=True, normalized_pools_equal=True))

    def test_actual_padder_complete_slot_and_stale_word_rejection(self):
        _, obj = self.copied_owner()
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream: rows = list(csv.DictReader(stream))
        rows = [r for r in rows if r['function'] != screen.FUNCTION] + screen.owner_guards()
        path = self.output / 'guards.csv'

        def emit(items):
            with path.open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=list(items[0])); writer.writeheader(); writer.writerows(items)
            return emit_padded_assembly(obj, self.root / 'conker/retail_layout.us.txt', 'game_16EE20',
                rodata_symbol='jtbl_800A5218_game', word_patches_path=path)

        assembly = emit(rows)
        begin = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION, screen.FUNCTION), begin)
        end = assembly.index('\n', end)
        source, padded = self.output / 'padded.s', self.output / 'padded.o'
        source.write_text('.text\n.globl %s\n' % screen.FUNCTION + assembly[begin:end+1])
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(padded),str(source)],check=True,capture_output=True)
        text, functions, relocs = parse_object(padded)
        self.assertEqual(functions[screen.FUNCTION]['size'],144)
        self.assertEqual(struct.unpack_from('>36I',text),tuple(self.retail)); self.assertEqual(relocs,{})
        broken = [dict(r) for r in rows]; broken[-1]['expected']='0x00000000'
        with self.assertRaisesRegex(ValueError,'stale'): emit(broken)
        self.receipt('padding', dict(words=36, guards=13, relocations=0, stale_rejected=True, no_insertions=True))

    def test_compiled_negatives_change_public_outputs(self):
        forms = {'no-swap':screen.SELECTED.replace('if (value1 < value0)', 'if (0)'),
            'wrong-low':screen.SELECTED.replace('if (value0 < arg2)', 'if (arg2 < value0)'),
            'wrong-high':screen.SELECTED.replace('if (arg3 < *arg1)', 'if (*arg1 < arg3)'),
            'unsigned':screen.SELECTED.replace('s32','u32')}
        detections = {}
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root, self.output, name, body)
            detected = 0
            for a,b,low,high in itertools.product((-1,1),repeat=4):
                memory,args=fixture(a,b,low,high)
                original=ClampOracle(self.retail,memory,args).run();model=ClampOracle(words,memory,args).run()
                detected += [read(original.memory,p) for p in args[:2]] != [read(model.memory,p) for p in args[:2]]
            self.assertGreater(detected,0,name);detections[name]=detected
        self.receipt('negatives',detections)

    def test_production_source_complete_slot_and_guard_suffix(self):
        self.assertIn(screen.SELECTED,(self.root/'conker/src/game_16EE20.c').read_text())
        functions,_,addresses=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION],self.retail)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:guards=list(csv.DictReader(stream))
        digest=assert_guard_history(self,guards)
        self.assertEqual(guards[10842:],screen.owner_guards())
        self.receipt('production',dict(words=36,guards=len(guards),guard_sha256=digest,byte_exact=True))


if __name__ == '__main__': unittest.main()
