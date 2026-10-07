"""Complete record-query instructions, typed callers and live field-read contracts."""

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

from tools.experiments import game_record_query_candidates as screen
from tools.experiments import game_range_clamp_candidates as clamp
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests.game_animation_timeline_oracle import floating, signed
from tools.tests.game_owner_pool import assert_guard_history, normalized_pools
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle
from tools.tests.test_game_point_transform_match import put, read
from tools.tests.test_game_queued_segment_writer import STACK
from tools.tests.test_game_range_clamp_match import ClampOracle
from tools.tests.test_game_scaled_matrix_match import emit_padded_assembly
from tools.tests import test_game_random_curve_record as native

QUERY, RECORDS, COUNT, TABLE = 0x24000, 0x25000, 0x800D3094, 0x800D3098
GROUPS = (((0, 2), (2, 2), (4, 2)), ((6, 2), (8, 2), (10, 2)),
    ((12, 4),), ((16, 4),), ((20, 1),), ((21, 1),), ((22, 1),), ((23, 1),),
    ((24, 4),), ((28, 4),), ((32, 4),))
PATTERNS = ((0, 0, 0, 0), (0x7FF, 0x7FF, 0x7FF, 0x7FF), (0x555, 0x2AA, 0, 0x555))
STUB = 's32 func_151438D8() {\n    return 0;\n}'


def fixture(pattern=2, start=0, end=4, flags=0x7FF, count=4, alias=False):
    memory = {STACK + i: (i * 17 + 13) & 255 for i in range(-0x180, 0x100)}
    for address, size in ((QUERY, 52), (RECORDS - 104, 7 * 52), (COUNT - 4, 16)):
        memory.update({address + i: 0xA5 for i in range(size)})
    values = (0x8000, 7, 0x7FFF, 0xFFFF, 2, 0x8000, 0x3FA00000, 0xBF400000,
        255, 37, 128, 0, 0x80000000, 0xFFFFFFFF, 0x7FFFFFFF)
    for (offset, size), value in zip([field for group in GROUPS for field in group], values):
        put(memory, QUERY + offset, value, size)
    for i, matches in enumerate(PATTERNS[pattern]):
        memory.update({RECORDS + i * 52 + j: memory[QUERY + j] for j in range(52)})
        put(memory, RECORDS + i * 52 + 21, 37 * 4 + 3, 1)
        for bit, group in enumerate(GROUPS):
            if not matches & 1 << bit:
                offset, size = group[0]
                address = RECORDS + i * 52 + offset
                put(memory, address, read(memory, address, size) ^ (4 if bit == 5 else 1), size)
    put(memory, COUNT, count); put(memory, TABLE, RECORDS)
    return memory, (start & 0xFFFFFFFF, end & 0xFFFFFFFF, flags & 0xFFFFFFFF,
        RECORDS if alias else QUERY)


def expected(memory, args):
    start, end, flags, query = args
    if not query: return 0
    start, end = sorted((signed(start), signed(end)))
    low, high = sorted((0, signed(read(memory, COUNT))))
    start, end = max(start, low), min(end, high)
    result = 0
    for i in range(start, end):
        record = read(memory, TABLE) + i * 52
        matches = []
        for bit, group in enumerate(GROUPS):
            checks = []
            for offset, size in group:
                a, b = read(memory, query + offset, size), read(memory, record + offset, size)
                if bit in (2, 3): a, b = floating(a), floating(b)
                if bit == 5: b >>= 2
                checks.append(a == b)
            matches.append(all(checks))
        selected = [matches[b] for b in range(11) if flags & 1 << b]
        if (all(selected) if flags & 0x1000 else any(selected)): result = record
    return result


class QueryOracle(ClampOracle):
    def __init__(self, words, memory, args, helper, phase=0):
        helper_address = clamp.ENTRY if len(words)<=272 else 0x15150000
        words = [((3<<26)|((helper_address>>2)&0x3FFFFFF)) if w==0x0D450F46 else w for w in words]
        connected = {helper_address + i * 4: w for i, w in enumerate(helper)}
        self.helper_address = helper_address
        TriangleOracle.__init__(self, words, memory, arguments=args, phase=phase, entry=screen.ENTRY, connected=connected)

    def execute(self, word):
        if word >> 26 == 0 and word & 63 == 3:
            self.r[word >> 11 & 31] = (signed(self.r[word >> 16 & 31]) >> (word >> 6 & 31)) & 0xFFFFFFFF
            self.r[0] = 0
        else: ClampOracle.execute(self, word)

    def record_call(self, target):
        assert target == self.helper_address
        self.calls.append((target, *self.arguments(4)))


class GameRecordQueryMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-record-query-test'; cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>272I', cls.rom, screen.ROM))
        cls.helper = list(struct.unpack_from('>36I', cls.rom, clamp.ROM))
        cls.directory = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def receipt(self, name, report):
        (self.output / (name + '.json')).write_text(json.dumps(report, indent=2) + '\n')

    def model(self, words, memory, args, phase=0, helper=None):
        return QueryOracle(words, memory, args, helper or self.helper, phase).run()

    def test_direct_complete_slot_frame_and_relocation_targets(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences']), (272, 96, 0))
        self.assertEqual(self.words, self.retail)
        self.assertEqual(self.record['diagnostics'], '')
        _, functions, relocs = parse_object(self.output / 'selected.o')
        target = functions[screen.FUNCTION]
        self.assertEqual({o-target['value']:r for o,r in relocs.items()}, {
            0x2C: [('R_MIPS_HI16','D_800D3094')], 0x30: [('R_MIPS_LO16','D_800D3094')],
            0x40: [('R_MIPS_26','func_15143D18')], 0x84: [('R_MIPS_HI16','D_800D3098')],
            0x88: [('R_MIPS_LO16','D_800D3098')]})
        self.receipt('slot', dict(words=272, bytes=1088, frame=96, differences=0, guards=0, relocations=5))

    def test_profiles_and_declaration_order_controls(self):
        report=[]
        for profile in screen.PROFILES:
            record,words=screen.compile_candidate(self.root,self.output,'profile-'+profile,screen.SELECTED,profile)
            report.append(record)
            for pattern,flags in itertools.product(range(3),(0,1,0x20,0x7FF,0x1000,0x17FF)):
                memory,args=fixture(pattern,flags=flags)
                self.assertEqual(self.model(words,memory,args).r[2],expected(memory,args))
        self.assertEqual(report[0]['differences'],0)
        controls=[]
        for name,body in screen.storage_candidates():
            record,words=screen.compile_candidate(self.root,self.output,name,body)
            controls.append(record)
            for pattern,flags in itertools.product(range(3),(0,0x7FF,0x1000,0x17FF)):
                memory,args=fixture(pattern,flags=flags)
                self.assertEqual(self.model(words,memory,args).r[2],expected(memory,args))
        self.assertEqual([r['name'] for r in controls if r['differences']==0],['decl-06','decl-07','decl-16','decl-22'])
        self.receipt('controls',dict(profiles=report,storage=controls,bounded_behavior=True))

    def test_guest_all_field_masks_both_modes_read_traces_memory_and_last_match(self):
        count, coverage = 0, [set(), set()]
        for mask, mode, pattern in itertools.product(range(2048), (0, 0x1000), range(3)):
            phase = (mask & 1) * 8
            memory, args = fixture(pattern, flags=mask | mode | 0xABCD8800)
            models = [self.model(words, memory, args, phase) for words in (self.words, self.retail)]
            self.assertEqual(models[0].r[2], expected(memory, args))
            self.assertEqual(models[0].r[2], models[1].r[2])
            self.assertEqual(models[0].memory, models[1].memory)
            self.assertEqual(models[0].events, models[1].events)
            self.assertEqual(models[0].calls, [(clamp.ENTRY, STACK+phase, STACK+phase+4, 0, 4)])
            for i, model in enumerate(models): coverage[i].update(model.visits)
            self.assertEqual({a:v for a,v in models[0].memory.items() if not STACK-0x180 <= a < STACK+0x100},
                {a:v for a,v in memory.items() if not STACK-0x180 <= a < STACK+0x100})
            count += 1
        for i, words in enumerate((self.words,self.retail)):
            memory,args=fixture();args=(*args[:3],0)
            coverage[i].update(self.model(words,memory,args).visits)
        # Five duplicated else assignments are dead after branch-likely conversion.
        self.assertEqual([set(range(screen.ENTRY, screen.ENTRY+1088, 4))-c for c in coverage],
            [{0x15143B94,0x15143BD8,0x15143C1C,0x15143C60,0x15143CA4}]*2)
        self.receipt('guest', dict(cases=count, field_masks=2048, modes=2, patterns=3,
            reachable_words=267, dead_else_words=5, full_memory=True, ordered_reads_writes=True,
            connected_retail_helper=True, last_match=True, saved_state=True))

    def test_signed_ranges_null_query_short_circuits_and_raw_c_helper(self):
        _, raw_helper = clamp.compile_candidate(self.root,self.output,'raw-helper')
        count = 0
        values = (-2147483648,-1,0,1,4,5,2147483647)
        for start,end,limit,flags,phase in itertools.product(values,values,(-2,0,4),(0,1,0x7FF,0x1000,0x17FF),(0,8)):
            memory,args=fixture(start=start,end=end,count=limit,flags=flags)
            models=[self.model(self.words,memory,args,phase,h) for h in (self.helper,raw_helper)]
            for model in models: self.assertEqual(model.r[2],expected(memory,args))
            self.assertEqual(models[0].memory,models[1].memory)
            count += 1
        for phase in (0,8):
            memory,args=fixture(); args=(*args[:3],0)
            memory={a:v for a,v in memory.items() if STACK-0x180<=a<STACK+0x100}
            model=self.model(self.words,memory,args,phase)
            self.assertEqual(model.r[2],0);self.assertEqual(model.calls,[])
        memory,args=fixture(flags=0x1000)
        memory={a:v for a,v in memory.items() if not QUERY<=a<QUERY+52}
        self.assertEqual(self.model(self.words,memory,args).r[2],RECORDS+3*52)
        for flags in (0,1,0x20,0x7FF,0x1000,0x17FF):
            memory,args=fixture(alias=True,flags=flags)
            self.assertEqual(self.model(self.words,memory,args).r[2],expected(memory,args))
        for flags,address in ((1,QUERY),(2,QUERY+8),(4,QUERY+12),(0x400,QUERY+32),(1,TABLE)):
            memory,args=fixture(1,flags=flags);del memory[address]
            with self.assertRaisesRegex(AssertionError,'unmapped'):self.model(self.words,memory,args)
        self.receipt('ranges',dict(cases=count,null_no_reads=True,unselected_query_unread=True,
            signed_extremes=True,raw_c_helper_connected=True,unmapped_rejected=True))

    def test_original_caller_setup_and_delay_store_with_connected_query(self):
        entry=0x15011E34
        fragment=list(struct.unpack_from('>9I',self.rom,0x3F2E4))
        self.assertEqual(fragment[-2:], [0x0D450E36,0xAFB90064])
        # Only the return scaffolding is synthetic; setup/call/delay words are retail.
        fragment += [0x8FBF0010,0x03E00008,0]
        connected={screen.ENTRY+i*4:w for i,w in enumerate(self.words)}
        connected.update({clamp.ENTRY+i*4:w for i,w in enumerate(self.helper)})

        class PairOracle(QueryOracle):
            def __init__(self,memory,phase,key):
                TriangleOracle.__init__(self,fragment,memory,arguments=(),phase=phase,entry=entry,connected=connected)
                self.r[15],self.r[24],self.r[25]=3,21,key

            def record_call(self,target):
                assert target in (screen.ENTRY,clamp.ENTRY)
                self.calls.append((target,*self.arguments(4)))

        count=0
        for key,phase in itertools.product(range(16),(0,8)):
            memory,_=fixture(1);query=STACK+phase+0x4C
            memory.update({query+i:memory[QUERY+i] for i in range(52)})
            put(memory,STACK+phase+0x10,0xDEAD0000)
            for i in range(4):
                put(memory,RECORDS+i*52+21,15,1);put(memory,RECORDS+i*52+23,21,1)
                put(memory,RECORDS+i*52+24,i%2)
            after=memory.copy();put(after,query+21,3,1);put(after,query+23,21,1);put(after,query+24,key)
            model=PairOracle(memory,phase,key).run()
            self.assertEqual(model.calls[0],(screen.ENTRY,0,4,0x11A0,query))
            self.assertEqual(model.r[2],expected(after,(0,4,0x11A0,query)))
            self.assertIn(('W',query+24,4,key),model.events)
            count+=1
        self.receipt('caller',dict(cases=count,original_words=9,caller='func_15011D60',
            delay_store=True,stack_query=True,connected_query_and_helper=True,whole_caller=False))

    def test_float_equality_triplet_short_circuit_and_shifted_byte(self):
        count=0
        float_values=(0,0x80000000,0x3FA00000,0x7F800000,0xFF800000,0x7FC00001)
        for bit,a,b in itertools.product((2,3),float_values,float_values):
            memory,args=fixture(1,flags=1<<bit)
            offset=GROUPS[bit][0][0];put(memory,QUERY+offset,a)
            for i in range(4):put(memory,RECORDS+i*52+offset,b)
            model=self.model(self.words,memory,args)
            self.assertEqual(model.r[2],expected(memory,args));count+=1
        for bit in (0,1):
            for offset,size in GROUPS[bit]:
                memory,args=fixture(1,flags=1<<bit)
                for i in range(4):
                    address=RECORDS+i*52+offset;put(memory,address,read(memory,address,size)^1,size)
                model=self.model(self.words,memory,args);self.assertEqual(model.r[2],0);count+=1
        for q,r in itertools.product((0,37,63,64,127,255),(0,1,3,148,151,252,255)):
            memory,args=fixture(1,flags=0x20);put(memory,QUERY+21,q,1)
            for i in range(4):put(memory,RECORDS+i*52+21,r,1)
            self.assertEqual(self.model(self.words,memory,args).r[2],expected(memory,args));count+=1
        self.receipt('fields',dict(cases=count,nan_unordered=True,signed_zero=True,infinities=True,
            triplets=True,unsigned_shifted_byte=True,fcsr_hardware_unqualified=True))

    def test_native_32_bit_typed_callers_all_u16_flags_and_readonly_inputs(self):
        self.fixture = ('typedef unsigned char u8;typedef short s16;typedef unsigned short u16;'
            'typedef int s32;typedef float f32;\n#define NULL ((void *)0)\n'+screen.DECLARATIONS+
            's32 D_800D3094;GameQueryRecord *D_800D3098;\n'+clamp.SELECTED+'\n'+screen.SELECTED+'\n')
        self.run_host(r'''
static GameQueryRecord records[4];GameQueryRecord saved[4],q,qs,*want,*got;int flags,p,i,b,count=0;
static const unsigned masks[3][4]={{0,0,0,0},{2047,2047,2047,2047},{1365,682,0,1365}};
if(sizeof(void *)!=4 || sizeof(GameQueryRecord)!=52)return 1;
if(__builtin_offsetof(GameQueryRecord,flags)!=21 || __builtin_offsetof(GameQueryRecord,word20)!=32)return 2;
D_800D3094=4;D_800D3098=records;
q.x=-32768;q.y=7;q.z=32767;q.radius=-1;q.height=2;q.width=-32768;
q.valueC=1.25f;q.value10=-0.75f;q.value14=255;q.flags=37;q.value16=128;q.value17=0;
q.word18=(-2147483647-1);q.word1C=-1;q.word20=2147483647;
for(i=0;i<16;i++)q.pad24[i]=(u8)(i*19);
qs=q;
for(p=0;p<3;p++) {
    for(i=0;i<4;i++) {
        records[i]=q;records[i].flags=151;
        if(!(masks[p][i]&1))records[i].x++;
        if(!(masks[p][i]&2))records[i].radius++;
        if(!(masks[p][i]&4))records[i].valueC=2.0f;
        if(!(masks[p][i]&8))records[i].value10=2.0f;
        if(!(masks[p][i]&16))records[i].value14=0;
        if(!(masks[p][i]&32))records[i].flags=155;
        if(!(masks[p][i]&64))records[i].value16=0;
        if(!(masks[p][i]&128))records[i].value17=1;
        if(!(masks[p][i]&256))records[i].word18=0;
        if(!(masks[p][i]&512))records[i].word1C=0;
        if(!(masks[p][i]&1024))records[i].word20=0;
        saved[i]=records[i];
    }
    for(flags=0;flags<65536;flags++) {
        want=NULL;
        for(i=0;i<4;i++) {
            unsigned selected=(unsigned)flags&2047u;
            int matches=(flags&4096)?(masks[p][i]&selected)==selected:(masks[p][i]&selected)!=0;
            if(matches)want=records+i;
        }
        got=func_151438D8(4,0,(u16)flags,&q);
        if(got!=want)return 3;
        count++;
    }
    for(i=0;i<4*52;i++)if(((u8 *)records)[i]!=((u8 *)saved)[i])return 4;
    for(b=0;b<52;b++)if(((u8 *)&q)[b]!=((u8 *)&qs)[b])return 5;
}
if(count!=196608)return 6;
D_800D3098=NULL;
if(func_151438D8(0,4,65535,NULL)!=NULL)return 7;
''')
        self.receipt('native',dict(cases=196608,bits=32,all_u16_flags=True,typed_pointer_return=True,
            stride=52,readonly=True,reversed_bounds=True,null_gate=True))

    def copied_owner(self):
        if hasattr(self.__class__,'owners'):return self.__class__.owners
        source=(self.root/'conker/src/game_16EE20.c').read_text()
        baseline=source.replace(screen.SELECTED,STUB).replace(screen.PROTOTYPE,'s32 func_151438D8();')
        baseline=baseline.replace(screen.OWNER_DECLARATIONS,'')
        baseline=baseline.replace(screen.OWNER_INCLUDE,'#include "variables.h"')
        selected=baseline.replace('#include "variables.h"',screen.OWNER_INCLUDE).replace('/* Generated placeholder declarations. */',
            screen.OWNER_DECLARATIONS+'\n/* Generated placeholder declarations. */').replace(
            's32 func_151438D8();',screen.PROTOTYPE).replace(STUB,screen.SELECTED)
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
        self.__class__.owners=result
        return result

    def test_copied_owner_neighbors_relocations_pool_and_actual_padding(self):
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
        self.assertEqual(text[f['value']:f['value']+1088],st[g['value']:g['value']+1088])
        self.assertEqual({o-f['value']:r for o,r in rel.items() if f['value']<=o<f['value']+1088},sr)
        assembly=emit_padded_assembly(new,self.root/'conker/retail_layout.us.txt','game_16EE20',
            rodata_symbol='jtbl_800A5218_game',word_patches_path=self.root/'conker/retail_word_patches.us.csv')
        begin=assembly.index('.type %s, @function'%screen.FUNCTION)
        end=assembly.index('.size %s, . - %s'%(screen.FUNCTION,screen.FUNCTION),begin)
        end=assembly.index('\n',end)
        source,obj,elf=(self.output/('padded'+suffix) for suffix in ('.s','.o','.elf'))
        source.write_text('.text\n.globl '+screen.FUNCTION+'\n'+assembly[begin:end+1])
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(obj),str(source)],check=True,capture_output=True)
        subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'query.ld'),'-e',screen.FUNCTION,
            *['--defsym=%s=0x%X'%item for item in screen.SYMBOLS.items()],'-o',str(elf),str(obj)],check=True,capture_output=True)
        address,data=screen.sections(elf)['.text'];self.assertEqual(address,screen.ENTRY)
        self.assertEqual(list(struct.unpack_from('>272I',data)),self.retail)
        self.receipt('owner',dict(functions=len(functions),unchanged=len(functions)-1,warnings=2,
            pool_unchanged=True,target_raw_identical=True,relocations=5,padded_words=272,guards=0))

    def test_compiled_negative_controls_change_returned_records(self):
        forms={'first-match':screen.SELECTED.replace('result = &D_800D3098[index];','return &D_800D3098[index];'),
            'no-byte-shift':screen.SELECTED.replace('(D_800D3098[index].flags >> 2)','D_800D3098[index].flags'),
            'all-for-any':screen.SELECTED.replace('else if (match != 0)','else if (pass == 0x7FF)'),
            'any-for-all':screen.SELECTED.replace('if (pass == 0x7FF)','if (match != 0)')}
        report={}
        for name,body in forms.items():
            _,words=screen.compile_candidate(self.root,self.output,name,body)
            detected=0
            for pattern,flags in itertools.product(range(3),(0,1,0x20,0x7FF,0x1000,0x1001,0x17FF)):
                memory,args=fixture(pattern,flags=flags)
                detected+=self.model(words,memory,args).r[2]!=expected(memory,args)
            self.assertGreater(detected,0,name);report[name]=detected
        self.receipt('negatives',report)

    def test_production_complete_source_slot_and_unchanged_guard_history(self):
        self.assertIn(screen.SELECTED,(self.root/'conker/src/game_16EE20.c').read_text())
        functions,_,addresses=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY);self.assertEqual(functions[screen.FUNCTION],self.retail)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:guards=list(csv.DictReader(stream))
        digest=assert_guard_history(self,guards)
        self.assertFalse(any(r['function']==screen.FUNCTION for r in guards))
        self.receipt('production',dict(words=272,byte_exact=True,guards=len(guards),new_guards=0,guard_sha256=digest))


if __name__=='__main__':unittest.main()
