"""Actor/callback gates, untouched packet bytes and a closed opening schedule."""

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

from tools.experiments import game_actor_gated_packet_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests.game_animation_timeline_oracle import signed
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read
from tools.tests.test_game_queued_segment_writer import STACK
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests import test_game_random_curve_record as native

ACTORS, COUNT, INDEX, BASE = 0x800CC2D0, 0x80082FA0, 0x800BE9E8, 0x800DBFF0
CHECK, CONTEXT, RANDOM, SUBMIT = 0x150A29C8, 0x1512D748, 0x150ADA20, 0x151D8868
STUB = 's32 func_15143E94() {\n    return 0;\n}'


def fixture(count=3, health=0, ready=0, flags=0xABCD4022, command=5,
            random=(0xFFFFFFFF, 0x12345678), mutation=False, phase=0, submit=0):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x200, 0x140)}
    for address, value in ((COUNT, count), (INDEX, 2), (BASE, 0x25000)):
        memory.update({address + i: 0 for i in range(4)}); put(memory, address, value)
    for i in range(127):
        memory[ACTORS + i * 0x32C + 0x1CA] = 255 if i == health else 0
    return memory, dict(ready=ready, random=random, mutation=mutation, phase=phase,
        submit=submit, args=(command & 0xFFFFFFFF, flags & 0xFFFFFFFF))


def expected(memory, case):
    count = (read(memory, COUNT) + 1) & 255
    count = count if count < 128 else count - 256
    calls = []
    if count <= 0 or not any(memory[ACTORS + i * 0x32C + 0x1CA] for i in range(count)):
        return 0, calls
    for index in range(count):
        calls.append((CHECK, index, case['args'][1]))
        if index == case['ready']:
            context = 0x35000 if case['mutation'] else read(memory, BASE)
            slot = 1 if case['mutation'] else read(memory, INDEX)
            calls += [(CONTEXT, (context + slot * 0x9A0) & 0xFFFFFFFF, case['args'][0], 1),
                (RANDOM,), (RANDOM,)]
            packet = [memory[STACK + case['phase'] - 0x10 + i] for i in range(8)]
            duration = (case['random'][0] & 15) + 20
            packet[0], packet[2], packet[3] = 1, duration >> 8, duration & 255
            packet[4], packet[5], packet[6] = (case['random'][1] & 3) + 4, 1, 255
            calls.append((SUBMIT, tuple(packet), 0, 255, 0))
            return 1, calls
    return 0, calls


class PacketOracle(TriangleOracle):
    def __init__(self, words, memory, case, entry=screen.ENTRY, connected=None):
        super().__init__(words, memory, entry=entry, arguments=case['args'],
            phase=case['phase'], connected=connected)
        self.case, self.random_calls = case, 0

    def execute(self, word):
        if word >> 26 == 32:
            imm = word & 65535
            address = (self.r[word >> 21 & 31] + (imm if imm < 32768 else imm - 65536)) & 0xFFFFFFFF
            value = self.get(address, 1)
            self.r[word >> 16 & 31] = (value if value < 128 else value - 256) & 0xFFFFFFFF
            self.r[0] = 0
        elif word >> 26 == 0 and word & 63 == 3:
            self.r[word >> 11 & 31] = (signed(self.r[word >> 16 & 31]) >> (word >> 6 & 31)) & 0xFFFFFFFF
            self.r[0] = 0
        else:
            super().execute(word)

    def record_call(self, target):
        if target == screen.ENTRY:
            self.calls.append((target, *self.arguments(2)))
        elif target == CHECK:
            self.calls.append((target, *self.arguments(2)))
        elif target == CONTEXT:
            self.calls.append((target, *self.arguments(3)))
        elif target == RANDOM:
            self.calls.append((target,))
        else:
            assert target == SUBMIT
            pointer, a, b, c = self.arguments(4)
            self.calls.append((target, tuple(self.get(pointer + i, 1) for i in range(8)), a, b, c))
        self.events.append(('CALL', target, self.calls[-1][1:]))

    def hook(self, target):
        result = 0
        if target == CHECK:
            result = 0 if self.r[4] == self.case['ready'] else 0x80000001
            if self.case['mutation']:
                self.put(COUNT, 0xFFFFFFFF, 4); self.put(INDEX, 1, 4); self.put(BASE, 0x35000, 4)
        elif target == RANDOM:
            result = self.case['random'][self.random_calls]; self.random_calls += 1
        elif target == SUBMIT:
            result = self.case['submit']
        else:
            assert target == CONTEXT
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000 + register
        self.f[:20] = [0xA5000000 + i for i in range(20)]
        self.r[2] = result & 0xFFFFFFFF


class GameActorGatedPacketMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-actor-gated-packet-test'; cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>98I', cls.rom, screen.ROM))
        cls.directory = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, report):
        (self.output / (name + '.json')).write_text(json.dumps(report, indent=2) + '\n')

    def test_complete_frame_private_lifetimes_and_closed_schedule(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (98, 56, 11))
        self.assertEqual(self.record['diagnostics'], '')
        self.assertEqual(self.words[:8], self.retail[:8]); self.assertEqual(self.words[20:], self.retail[20:])
        self.assertEqual(screen.schedule_tokens(self.words), screen.schedule_tokens(self.retail))
        self.assertEqual(len(screen.owner_guards()), 11)
        # Snapshot count flows through the same add/shift/shift before the same branch target.
        self.assertEqual(self.words[12:15], self.retail[13:16])
        self.assertIn(('blez', 18, 0x15143F20), screen.schedule_tokens(self.words))
        self.assertEqual(self.words[10], self.retail[8])
        self.assertEqual(self.words[10], 0xA3A00037)
        _, functions, relocs = parse_object(self.output / 'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['size'], 392)
        self.assertEqual(len(relocs), 13)
        self.receipt('slot', dict(body_words=98, bytes=392, frame=56, direct_words=87,
            guards=11, schedule_window=[32,76], branch_target=0x15143F20, relocations=13,
            packet_offset=40, result_offset=55, unchanged_opcode_dependencies=True))

    def test_guest_all_count_bytes_gates_full_packet_memory_and_saved_state(self):
        coverage = [set(), set()]; cases = 0
        for count, health, ready, phase in itertools.product(range(256), (-1,0,3,126), (-1,0,3,126), (0,8)):
            memory, case = fixture(count, health, ready, phase=phase)
            result, calls = expected(memory, case)
            models = [PacketOracle(w, memory, case).run() for w in (self.words, self.retail)]
            for i, model in enumerate(models):
                self.assertEqual((model.r[2], model.calls), (result, calls)); coverage[i].update(model.visits)
                self.assertEqual({a:v for a,v in model.memory.items() if not STACK-0x200<=a<STACK+0x140},
                    {a:v for a,v in memory.items() if not STACK-0x200<=a<STACK+0x140})
            self.assertEqual(models[0].memory, models[1].memory)
            external = lambda m: [e for e in m.events if not STACK-0x200 <= e[1] < STACK+0x140]
            self.assertEqual(external(models[0]), external(models[1])); cases += 1
        # Duplicated increments are dead after branch-likely conversion.
        self.assertEqual([set(range(screen.ENTRY,screen.ENTRY+392,4))-c for c in coverage],
            [{0x15143F04,0x15143F4C}]*2)
        self.receipt('guest', dict(cases=cases, count_bytes=256, phases=2, reachable_words=96, dead_words=2,
            full_packet=True, untouched_bytes=[1,7], full_final_memory=True, external_order=True,
            external_calls_interleaved=True,
            private_opening_store_order_different=True, saved_state=True, synthetic_actor_bounds=127))

    def test_callback_mutation_snapshot_count_live_context_and_rng_ranges(self):
        cases = 0
        for count, ready, flags, command, mutation, submit in itertools.product(
                (0,3,25), (0,3,25), (0,0x4022,0xFFFF4022,0x80000000),
                (5,0xFFFFFFFF), (False,True), (0,0x80012345)):
            memory, case = fixture(count,0,ready,flags,command,mutation=mutation,submit=submit)
            result, calls = expected(memory, case)
            models = [PacketOracle(w,memory,case).run() for w in (self.words,self.retail)]
            for model in models:self.assertEqual((model.r[2],model.calls),(result,calls))
            self.assertEqual(models[0].memory,models[1].memory); cases += 1
        for a,b in itertools.product(range(16), range(4)):
            memory, case = fixture(random=(0xFFFFFFF0|a,0x80000000|b))
            model = PacketOracle(self.words,memory,case).run()
            self.assertEqual((model.r[2],model.calls),expected(memory,case)); cases += 1
        for count in (0x7FFFFFFF,0x80000000,0xFFFFFFFE,0xFFFFFFFF,0x12345603):
            memory,case=fixture(count,0,3)
            for words in (self.words,self.retail):
                model=PacketOracle(words,memory,case).run()
                self.assertEqual((model.r[2],model.calls),expected(memory,case));cases+=1
        self.receipt('callbacks',dict(cases=cases,full_word_arguments=True,count_snapshot=True,
            live_context=True,caller_saved_clobbered=True,two_random_calls=True,
            ignored_submission_result=True,unsigned_count_increment=True))

    def test_lazy_reads_unmapped_bounds_and_untouched_packet_bytes(self):
        for words in (self.words,self.retail):
            memory,case=fixture(0xFFFFFFFF)
            memory={a:v for a,v in memory.items() if a<0x80000000 or COUNT<=a<COUNT+4}
            self.assertEqual(PacketOracle(words,memory,case).run().calls,[])
            for health,ready in ((-1,0),(0,-1)):
                memory,case=fixture(3,health,ready)
                for address in (BASE,INDEX):
                    for i in range(4):del memory[address+i]
                self.assertEqual(PacketOracle(words,memory,case).run().r[2],0)
            for address in (COUNT,ACTORS+0x1CA,BASE,INDEX):
                memory,case=fixture();del memory[address]
                with self.assertRaisesRegex(AssertionError,'unmapped'):PacketOracle(words,memory,case).run()
            for first,last in itertools.product((0,1,127,255),repeat=2):
                memory,case=fixture()
                memory[STACK-15],memory[STACK-9]=first,last
                model=PacketOracle(words,memory,case).run()
                self.assertEqual((model.calls[-1][1][1],model.calls[-1][1][7]),(first,last))
        self.receipt('lazy',dict(nonpositive_no_actor_reads=True,failed_gates_no_context_reads=True,
            unmapped_required_reads_rejected=True,poisoned_padding_cases=32))

    def test_profiles_storage_controls_and_narrow_signature_regression(self):
        records=[]
        for profile in screen.PROFILES:
            record,words=screen.compile_candidate(self.root,self.output,'profile-'+profile,screen.SELECTED,profile)
            for health,ready in itertools.product((-1,0,3),(-1,0,3)):
                memory,case=fixture(3,health,ready)
                # Profiles have independent private placement; defined bytes and call contracts are compared.
                model=PacketOracle(words,memory,case).run()
                result,calls=expected(memory,case)
                strip=lambda cs:[(c[0], tuple(c[1][i] for i in (0,2,3,4,5,6)),*c[2:]) if c[0]==SUBMIT else c for c in cs]
                self.assertEqual((model.r[2],strip(model.calls)),(result,strip(calls)))
            records.append(record)
        self.assertEqual([r['frame'] for r in records],[56,56,40,40])
        controls=[]
        for name,body in screen.storage_candidates():
            record,words=screen.compile_candidate(self.root,self.output,name,body);controls.append(record)
            self.assertEqual(record['body_words'],98)
            for health,ready in itertools.product((-1,0),(-1,0,3)):
                memory,case=fixture(3,health,ready)
                model=PacketOracle(words,memory,case).run();result,calls=expected(memory,case)
                self.assertEqual((model.r[2],strip(model.calls)),(result,strip(calls)))
        self.assertEqual(min(r['differences'] for r in controls),11)
        narrow=screen.DECLARATIONS.replace('func_150A29C8(s32, s32)','func_150A29C8(u8, u16)')
        record,words=screen.compile_candidate(self.root,self.output,'narrow-signature',declarations=narrow)
        memory,case=fixture(flags=0xABCD4022)
        self.assertNotEqual(PacketOracle(words,memory,case).run().calls,expected(memory,case)[1])
        self.receipt('controls',dict(profiles=records,storage=controls,narrow_signature=record,
            narrowed_forwarded_flags_detected=True))

    def test_native_32_bit_packet_fields_counts_arguments_and_live_callbacks(self):
        self.fixture=('typedef unsigned char u8;typedef signed char s8;typedef short s16;'
            'typedef unsigned short u16;typedef int s32;typedef unsigned int u32;\n'+screen.DECLARATIONS+r'''
GameGatedActor D_800CC2D0[127];
static GameGatedContext contexts[4];
GameGatedContext *D_800DBFF0;
s32 D_80082FA0,D_800BE9E8;
static int ready,checker,randomCalls,contextCalls,packetCalls,error,mutate;
static s32 command,flags;
static u32 randomWords[2];
s32 func_150A29C8(s32 index,s32 value) {
    if(index!=checker++ || value!=flags) error=1;
    if(mutate) { D_80082FA0=-1; D_800BE9E8=1; D_800DBFF0=contexts+1; }
    return index==ready?0:(s32)0x80000001u;
}
void func_1512D748(GameGatedContext *context,s32 value,s32 one) {
    if(context!=contexts+2 || value!=command || one!=1 || contextCalls++) error=2;
}
s32 func_150ADA20(void) {
    if(contextCalls!=1 || randomCalls>=2) { error=3; return 0; }
    return (s32)randomWords[randomCalls++];
}
void *func_151D8868(void *data,s32 zero,s32 max,s32 another) {
    GameGatedPacket *p=data;
    if(randomCalls!=2 || packetCalls++ || zero || max!=255 || another || p->kind!=1
       || p->duration!=(s16)((randomWords[0]&15)+20) || p->count!=(randomWords[1]&3)+4
       || p->mode!=1 || p->index!=-1) error=4;
    return (void *)0;
}
''' + screen.SELECTED)
        self.run_host(r'''
int n,h,r,m,a,b,i,count,active,result,calls;
static s32 extremes[]={0x7FFFFFFF,(s32)0x80000000u,-2,-1,0x12345603};
command=(s32)0xFEDCBA98u;flags=(s32)0xABCD4022u;
for(n=0;n<261;n++) for(h=-1;h<5;h++) for(r=-1;r<5;r++) for(m=0;m<2;m++) {
    D_80082FA0=n<256?n:extremes[n-256];count=(s8)((u32)D_80082FA0+1);
    D_800BE9E8=2;D_800DBFF0=contexts;ready=r;mutate=m;
    checker=randomCalls=contextCalls=packetCalls=error=0;
    for(i=0;i<127;i++) D_800CC2D0[i].health=i==h?255:0;
    active=count>0 && h>=0 && h<count;
    result=active && r>=0 && r<count;
    calls=active?(result?r+1:count):0;
    randomWords[0]=0xFFFFFFFFu;randomWords[1]=0x12345678u;
    if(func_15143E94(command,flags)!=result || checker!=calls || contextCalls!=result
       || packetCalls!=result || randomCalls!=result*2 || error) return 1;
}
for(a=0;a<16;a++) for(b=0;b<4;b++) {
    D_80082FA0=0;D_800BE9E8=2;D_800DBFF0=contexts;ready=mutate=0;
    checker=randomCalls=contextCalls=packetCalls=error=0;D_800CC2D0[0].health=1;
    randomWords[0]=0xFFFFFFF0u|a;randomWords[1]=0x80000000u|b;
    if(func_15143E94(command,flags)!=1 || error || randomCalls!=2) return 2;
}
''')
        self.receipt('native',dict(cases=261*6*6*2+64,word_bits=32,
            defined_packet_fields=True,padding_values_not_claimed=True,full_arguments=True,
            unsigned_increment_extremes=True,live_mutations=True))

    def test_original_caller_call_and_delay_pairs_connected(self):
        cases=0
        for entry,rom,delay in ((0x150BAA8C,0xE7F3C,0x24054022),(0x150BACB8,0xE8168,0xE7B000C8)):
            fragment=list(struct.unpack_from('>2I',self.rom,rom));self.assertEqual(fragment,[0x0D450FA5,delay])
            fragment += [0x8FBF0010,0x03E00008,0]
            for phase,ready in itertools.product((0,8),(-1,0,3)):
                memory,case=fixture(3,0,ready,flags=0x4022,phase=phase)
                put(memory,STACK+phase+0x10,0xDEAD0000)
                connected={screen.ENTRY+i*4:w for i,w in enumerate(self.words)}
                model=PacketOracle(fragment,memory,case,entry=entry,connected=connected)
                model.f[16]=0xC1234567
                model.run();result,calls=expected(memory,case)
                self.assertEqual((model.r[2],model.calls),(result,[(screen.ENTRY,5,0x4022),*calls]))
                if delay==0xE7B000C8:self.assertIn(('W',STACK+phase+0xC8,4,0xC1234567),model.events)
                cases+=1
        self.receipt('callers',dict(cases=cases,original_pairs=2,delay_store=True,
            connected_target=True,caller_setup_seeded=True,whole_callers=False))

    def copied_owner(self):
        if hasattr(self.__class__,'owners'):return self.owners
        baseline=(self.root/'conker/src/game_16EE20.c').read_text()
        baseline=baseline.replace(screen.SELECTED,STUB).replace(screen.PROTOTYPE,'s32 func_15143E94();')
        baseline=baseline.replace(screen.OWNER_DECLARATIONS,'').replace(screen.OWNER_INCLUDE,'#include "functions.h"')
        selected=baseline.replace('#include "functions.h"',screen.OWNER_INCLUDE).replace(
            '/* Generated placeholder declarations. */',screen.OWNER_DECLARATIONS+'\n/* Generated placeholder declarations. */').replace(
            's32 func_15143E94();',screen.PROTOTYPE).replace(STUB,screen.SELECTED)
        result,warnings=[],[]
        for name,body in (('baseline',baseline),('selected',selected)):
            obj,warning=compile_owner(self.root,self.output,body,'owner-'+name);warnings.append(warning)
            processed=self.output/('owner-'+name+'-postprocessed.o');shutil.copyfile(obj,processed)
            subprocess.run([sys.executable,str(self.root/'tools/asm-processor/asm_processor.py'),'-O2','-g3',
                str((self.output/('owner-'+name+'.c')).relative_to(self.root/'conker')),'--post-process',
                str(processed.relative_to(self.root/'conker')),'--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude','include/asm_processor_prelude.inc'],cwd=self.root/'conker',check=True,capture_output=True)
            result.append(processed)
        self.assertEqual(warnings[0],warnings[1]);self.assertEqual(len(warnings[0]),2)
        self.__class__.owners=result;return result

    def test_copied_owner_neighbors_relocations_pool_and_guarded_padding(self):
        old,new=self.copied_owner();ot,of,orr=parse_object(old);text,functions,rel=parse_object(new)
        self.assertEqual(set(functions),set(of))
        for name,f in functions.items():
            if name==screen.FUNCTION:continue
            previous=of[name]
            self.assertEqual(text[f['value']:f['value']+f['size']],ot[previous['value']:previous['value']+previous['size']],name)
            self.assertEqual({o-f['value']:r for o,r in rel.items() if f['value']<=o<f['value']+f['size']},
                {o-previous['value']:r for o,r in orr.items() if previous['value']<=o<previous['value']+previous['size']},name)
        self.assertEqual(normalized_pools(old),normalized_pools(new))
        st,sf,sr=parse_object(self.output/'selected.o');f=functions[screen.FUNCTION];g=sf[screen.FUNCTION]
        self.assertEqual(text[f['value']:f['value']+392],st[g['value']:g['value']+392])
        self.assertEqual({o-f['value']:r for o,r in rel.items() if f['value']<=o<f['value']+392},sr)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:rows=list(csv.DictReader(stream))
        rows=[r for r in rows if r['function']!=screen.FUNCTION]+screen.owner_guards()
        guard_path=self.output/'owner-guards.csv'
        def emit(items):
            with guard_path.open('w',newline='') as stream:
                writer=csv.DictWriter(stream,fieldnames=list(items[0]));writer.writeheader();writer.writerows(items)
            return emit_padded_assembly(new,self.root/'conker/retail_layout.us.txt','game_16EE20',
                rodata_symbol='jtbl_800A5218_game',word_patches_path=guard_path)
        assembly=emit(rows);begin=assembly.index('.type %s, @function'%screen.FUNCTION)
        end=assembly.index('.size %s, . - %s'%(screen.FUNCTION,screen.FUNCTION),begin);end=assembly.index('\n',end)
        source,obj=(self.output/('padded'+suffix) for suffix in ('.s','.o'))
        source.write_text('.text\n.globl '+screen.FUNCTION+'\n'+assembly[begin:end+1])
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(obj),str(source)],check=True,capture_output=True)
        _,_,padded_rel=parse_object(obj)
        self.assertEqual(len(padded_rel),13)
        for alternate in (False,True):
            targets=screen.SYMBOLS if not alternate else {n:(0x15208004+i*0x10000 if n.startswith('func_')
                else 0x90018004+i*0x10000) for i,n in enumerate(screen.SYMBOLS)}
            elf=self.output/('padded-%d.elf'%alternate)
            subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'packet.ld'),'-e',screen.FUNCTION,
                *['--defsym=%s=0x%X'%item for item in targets.items()],'-o',str(elf),str(obj)],check=True,capture_output=True)
            words=list(struct.unpack_from('>98I',screen.sections(elf)['.text'][1]));wanted=self.retail.copy()
            for offset,values in padded_rel.items():
                self.assertEqual(len(values),1);kind,name=values[0];address=targets[name]
                if kind=='R_MIPS_26':wanted[offset//4]=wanted[offset//4]&0xFC000000|address>>2&0x3FFFFFF
                else:wanted[offset//4]=wanted[offset//4]&0xFFFF0000|((address+0x8000)>>16&65535 if kind=='R_MIPS_HI16' else address&65535)
            self.assertEqual(words,wanted)
        for field,value in (('expected','0x00000000'),('expected_relocations','R_MIPS_HI16:D_800BE9E8')):
            altered=[dict(r) for r in rows];altered[-11][field]=value
            with self.assertRaisesRegex(ValueError,'stale'):emit(altered)
        self.receipt('owner',dict(functions=len(functions),unchanged=len(functions)-1,warnings=2,
            pool_unchanged=True,target_raw_identical=True,relocations=13,padded_words=98,
            guards=11,alternate_carries=True,stale_word=True,stale_relocation=True))

    def test_compiled_negative_controls_change_contracts(self):
        forms={'ignore-health':screen.SELECTED.replace('D_800CC2D0[index].health != 0','1'),
            'reverse-ready':screen.SELECTED.replace('func_150A29C8(index, flags) == 0','func_150A29C8(index, flags) != 0'),
            'narrow-flags':screen.SELECTED.replace('func_150A29C8(index, flags)','func_150A29C8(index, flags & 0xFFFF)'),
            'wrong-rng-mask':screen.SELECTED.replace('& 0xF','& 7'),
            'zero-padding':screen.SELECTED.replace('packet.kind = 1;','packet.pad1 = 0; packet.pad7 = 0; packet.kind = 1;'),
            'submission-status':screen.SELECTED.replace('func_151D8868(&packet, 0, 255, 0);\n            result = 1;',
                'result = func_151D8868(&packet, 0, 255, 0) != 0;')}
        report={}
        for name,body in forms.items():
            _,words=screen.compile_candidate(self.root,self.output,name,body)
            detected=0
            for health,ready in itertools.product((-1,0,3),(-1,0,3)):
                memory,case=fixture(3,health,ready)
                model=PacketOracle(words,memory,case).run()
                detected+=(model.r[2],model.calls)!=expected(memory,case)
            self.assertGreater(detected,0,name);report[name]=detected
        self.receipt('negatives',report)

    def test_production_complete_source_slot_and_guard_history(self):
        self.assertIn(screen.SELECTED,(self.root/'conker/src/game_16EE20.c').read_text())
        functions,_,addresses=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY);self.assertEqual(functions[screen.FUNCTION],self.retail)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:guards=list(csv.DictReader(stream))
        digest=assert_guard_history(self,guards)
        self.assertEqual([r for r in guards if r['function']==screen.FUNCTION],screen.owner_guards())
        self.receipt('production',dict(words=98,byte_exact=True,guards=len(guards),new_guards=11,guard_sha256=digest))


if __name__=='__main__':unittest.main()
