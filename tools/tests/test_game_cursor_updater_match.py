"""Cursor wrap/reflect modes, live pointer aliases and closed register roles."""

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

from tools.experiments import game_cursor_updater_candidates as screen
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

BUFFER, TABLE, TICKS = 0x24000, 0x80090B64, 0x800BE9E4
STUB = 's32 func_1514401C() {\n    return 0;\n}'


class DivisionTrap(Exception):
    def __init__(self, code):self.code=code


def fixture(count=2, value=0, velocity=3, ticks=1, flags=0, index=5, alias=0, phase=0):
    memory={STACK+i:(i*17+13)&255 for i in range(-0x80,0x100)}
    for address in (BUFFER,BUFFER+4,TICKS,TABLE+(index&255)*12):
        memory.update({address+i:0xA5 for i in range(4)})
    p,q=BUFFER,BUFFER+4
    if alias==1:p=q=BUFFER
    elif alias==2:p=TICKS
    elif alias==3:p,q=STACK+phase+0x20,STACK+phase+0x24
    put(memory,TICKS,ticks);put(memory,p,velocity);put(memory,q,value)
    put(memory,TABLE+(index&255)*12,count,1)
    return memory,(index&0xFFFFFFFF,p,q,flags&0xFFFFFFFF)


def reference(memory,args,phase=0):
    after=memory.copy();trace=[]
    def get(address,size=4):
        value=read(after,address,size);trace.append(('R',address,size,value));return value
    def store(address,value,size=4):
        put(after,address,value,size);trace.append(('W',address,size,value&((1<<(size*8))-1)))
    index,velocity,position,flags=args
    put(after,STACK+phase,index);put(after,STACK+phase+12,flags)
    flags &=255
    ticks=get(TICKS);speed=get(velocity)
    limit=(get(TABLE+(index&255)*12,1)<<16)-1
    value=signed((get(position)+speed*ticks)&0xFFFFFFFF)
    store(position,value);result=0;trap=None
    def remainder(numerator):
        if numerator==-2147483648 and limit==-1:return 0,6
        quotient=abs(numerator)//abs(limit)
        if (numerator<0)!=(limit<0):quotient=-quotient
        return numerator-quotient*limit,None
    if value>limit:
        if flags&1:result=1
        elif flags&2:store(velocity,0);store(position,limit)
        elif flags&4:
            rest,trap=remainder(value);store(position,limit-rest)
            speed=get(velocity)
            if trap is None:store(velocity,-speed)
        else:
            for _ in range(1000):
                value=signed((value-limit)&0xFFFFFFFF);store(position,value)
                if value<=limit:break
            else:raise AssertionError('unbounded fixture')
    elif value<0 and not flags&8:
        if flags&16:store(velocity,0);store(position,0)
        elif flags&4:
            rest,trap=remainder(signed((-value)&0xFFFFFFFF));store(position,rest)
            speed=get(velocity)
            if trap is None:store(velocity,-speed)
        else:
            for _ in range(1000):
                value=signed((value+limit)&0xFFFFFFFF);store(position,value)
                if value>=0:break
            else:raise AssertionError('unbounded fixture')
    return result,after,trace,trap


class CursorOracle(TriangleOracle):
    def __init__(self,words,memory,args,phase=0,entry=screen.ENTRY,connected=None):
        super().__init__(words,memory,arguments=args,phase=phase,entry=entry,connected=connected)
        self.hi=0

    def execute(self,word):
        if word>>26==0 and word&63==26:
            a,b=signed(self.r[word>>21&31]),signed(self.r[word>>16&31])
            assert b!=0,'zero divisor outside valid table domain'
            quotient=(abs(a)//abs(b))*(-1 if (a<0)!=(b<0) else 1)
            self.lo=quotient&0xFFFFFFFF;self.hi=(a-quotient*b)&0xFFFFFFFF
        elif word>>26==0 and word&63==16:
            self.r[word>>11&31]=self.hi;self.r[0]=0
        elif word>>26==0 and word&63==13:
            raise DivisionTrap(word>>16&1023)
        else:super().execute(word)

    def record_call(self,target):
        assert target==screen.ENTRY
        self.calls.append((target,*self.arguments(4)))

    def outcome(self):
        try:self.run();return self.r[2],None
        except DivisionTrap as trap:return None,trap.code


def public_trace(model,phase=0):
    return [e for e in model.events if e[1] not in (STACK+phase,STACK+phase+12)]


class OperandCode(dict):
    """Observe operands before execution, including branch and annulled delay rules."""
    def __init__(self, model):
        super().__init__(model.code); self.model = model; self.trace = []

    def __getitem__(self, pc):
        word = super().__getitem__(pc)
        m = self.model
        op, rs, rt, shift, fn = word >> 26, word >> 21 & 31, word >> 16 & 31, word >> 6 & 31, word & 63
        imm = word & 65535
        a, b = m.r[rs], m.r[rt]
        if op == 0:
            if fn == 0: inputs = (b, shift)
            elif fn in (33, 37, 25): inputs = tuple(sorted((a, b)))
            elif fn in (35, 42, 26): inputs = (a, b)
            elif fn == 16: inputs = (m.hi,)
            elif fn == 18: inputs = (m.lo,)
            elif fn == 8: inputs = (a,)
            elif fn == 13: inputs = (word >> 16 & 1023,)
            else: raise AssertionError(('unsupported operand trace', hex(word)))
        elif op in (35, 36, 43):
            address = (a + (imm if imm < 32768 else imm - 65536)) & 0xFFFFFFFF
            size = 1 if op == 36 else 4
            inputs = (address, size, b if op == 43 else read(m.memory, address, size))
        elif op in (4, 5, 20): inputs = (*sorted((a, b)), imm)
        elif op == 1: inputs = (a, rt, imm)
        elif op in (9, 12): inputs = (a, imm)
        elif op == 15: inputs = (imm,)
        else: raise AssertionError(('unsupported operand trace', hex(word)))
        self.trace.append((pc, op, fn if op == 0 else None, inputs))
        return word


class GameCursorUpdaterMatchTests(unittest.TestCase):
    run_host=native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        cls.output=cls.root/'conker/build/game-cursor-updater-test';cls.output.mkdir(exist_ok=True)
        cls.record,cls.words=screen.compile_candidate(cls.root,cls.output,'selected')
        cls.rom=(cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail=list(struct.unpack_from('>98I',cls.rom,screen.ROM))
        cls.directory=tempfile.TemporaryDirectory();cls.addClassCleanup(cls.directory.cleanup);cls.path=Path(cls.directory.name)

    def receipt(self,name,report):(self.output/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')

    def test_complete_retail_slot_and_only_register_fields_differ(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences']),(98,0,46))
        self.assertEqual(self.words[:8],self.retail[:8]);self.assertEqual(self.record['diagnostics'],'')
        self.assertEqual(len(self.record['relocations']),4)
        self.assertEqual(self.retail[-6:],[0xACCD0000,0x05A0FFFD,0x01A04825,0x00601025,0x03E00008,0])
        self.assertEqual(self.words[-6:],[0xACC40000,0x0480FFFD,0x00804025,0x00601025,0x03E00008,0])
        self.assertEqual(self.words.count(0x0007000D),2);self.assertEqual(self.words.count(0x0006000D),2)
        patched=self.words.copy()
        for i,(a,b) in enumerate(zip(self.words,self.retail)):
            self.assertEqual(a & ~screen.register_mask(a),b & ~screen.register_mask(a),hex(i*4))
        for row in screen.owner_guards():
            i=int(row['offset'],16)//4
            self.assertEqual(patched[i],int(row['expected'],16));patched[i]=int(row['replacement'],16)
        self.assertEqual(patched,self.retail)
        self.receipt('slot',dict(retail_words=98,candidate_words=98,frame=0,differences=46,
            relocations=4,register_fields_only=True,guards=46,no_insertions_or_omissions=True))

    def test_paired_instruction_operands_and_closed_register_lifetimes(self):
        cases=0;coverage=set()
        fixtures=[]
        for count,point,flags,alias in itertools.product((1,2,255),range(7),range(256),(0,1)):
            limit=(count<<16)-1
            value=(-limit,-1,0,limit-1,limit,limit+1,2*limit+1)[point]
            fixtures.append(fixture(count,value,0,1,flags,alias=alias))
        for value,flags,alias in itertools.product((0x80000000,0x7FFFFFFF),range(256),(0,1)):
            fixtures.append(fixture(0,value,0,0,flags,alias=alias))
        for memory,args in fixtures:
            traces=[]
            for words in (self.words,self.retail):
                model=CursorOracle(words,memory,args);model.code=OperandCode(model)
                model.outcome();traces.append(model.code.trace);coverage.update(model.visits)
            self.assertEqual(traces[0],traces[1]);cases+=1
        self.assertEqual(len(coverage),95)
        # The single commutative add is normalized by the operand observer, not by ignoring values.
        self.assertEqual(self.words[0x58//4],0x016C6821);self.assertEqual(self.retail[0x58//4],0x018B6821)
        self.receipt('operands',dict(cases=cases,retail_reachable_words=95,paired_instruction_inputs=True,
            load_store_addresses_values_and_branch_inputs=True,commutative_add_order_checked=True,
            physical_register_names_not_part_of_semantic_trace=True))

    def test_guest_every_mode_byte_limits_indices_aliases_trace_and_memory(self):
        cases=0;coverage=[set(),set()]
        for count,point,alias,flags in itertools.product((1,2,7,255),range(9),(0,1),range(256)):
            limit=(count<<16)-1
            values=(-2*limit,-limit,-1,0,1,limit-1,limit,limit+1,2*limit+1)
            phase=(flags&1)*8;index=0xABCD0000|((flags*17+count)&255)
            memory,args=fixture(count,values[point],(-3,0,3)[point%3],(-1,0,1)[point%3],0xABCD0000|flags,index,alias,phase)
            result,after,trace,trap=reference(memory,args,phase);self.assertIsNone(trap)
            for i,words in enumerate((self.words,self.retail)):
                model=CursorOracle(words,memory,args,phase);self.assertEqual(model.outcome(),(result,None))
                self.assertEqual(model.memory,after);self.assertEqual(public_trace(model,phase),trace)
                coverage[i].update(model.visits)
            cases+=1
        for value,flags in itertools.product((0x80000000,0x7FFFFFFF),range(256)):
            memory,args=fixture(0,value,0,0,flags)
            result,after,trace,trap=reference(memory,args)
            for i,words in enumerate((self.words,self.retail)):
                model=CursorOracle(words,memory,args)
                self.assertEqual(model.outcome(),(None,trap) if trap else (result,None))
                self.assertEqual(model.memory,after);self.assertEqual(public_trace(model),trace)
                coverage[i].update(model.visits)
            cases+=1
        dead=set(range(screen.ENTRY,screen.ENTRY+392,4))-coverage[1]
        self.assertEqual(dead,{0x151440D4,0x151440EC,0x15144160})
        self.receipt('guest',dict(cases=cases,mode_bytes=256,index_low_bytes=256,stack_phases=2,
            full_memory=True,ordered_public_reads_writes=True,saved_state_on_return=True,retail_reachable_words=95,
            unreachable_division_guards=[hex(a) for a in sorted(dead)],synthetic_table_bounds=256))

    def test_modular_extremes_global_and_caller_stack_aliases(self):
        cases=0
        for value,velocity,ticks,flags,alias in itertools.product(
                (0x80000000,0x7FFFFFFF,0xFFFFFFFF,0,1),(0x80000000,0x7FFFFFFF,-1,0,1),(-2,-1,0,1,2),
                (0,1,2,4,8,16,31),(0,1,2,3)):
            memory,args=fixture(255,value,velocity,ticks,flags,alias=alias)
            result,after,trace,trap=reference(memory,args)
            for words in (self.words,self.retail):
                model=CursorOracle(words,memory,args);self.assertEqual(model.outcome(),(result,trap))
                self.assertEqual(model.memory,after);self.assertEqual(public_trace(model),trace)
            cases+=1
        self.receipt('extremes',dict(cases=cases,modular_product_add_sub_negation=True,
            velocity_cursor_tick_and_caller_stack_aliases=True,full_memory=True,ordered_trace=True))

    def test_zero_count_natural_overflow_trap_and_unreachable_zero_divisor(self):
        cases=traps=0
        self.assertTrue(all(((count<<16)-1)!=0 for count in range(256)))
        for value,flags,alias in itertools.product((0x80000000,0x7FFFFFFF),range(256),(0,1)):
            memory,args=fixture(0,value,0,0,flags,alias=alias)
            result,after,trace,trap=reference(memory,args)
            for words in (self.words,self.retail):
                model=CursorOracle(words,memory,args)
                self.assertEqual(model.outcome(),(None,trap) if trap else (result,None))
                self.assertEqual(model.memory,after);self.assertEqual(public_trace(model),trace)
            cases+=1;traps+=trap is not None
        self.receipt('traps',dict(cases=cases,overflow_traps=traps,break_code=6,
            write_and_velocity_read_before_trap=True,zero_divisor_unreachable_for_all_256_counts=True,
            overflow_hi_zero_bounded_model=True,hardware_div_hi_unqualified=True,
            zero_count_long_wraps_not_repaired_or_executed=True))

    def test_lazy_single_byte_table_reads_and_unmapped_required_inputs(self):
        memory,args=fixture(index=0xFFFFFFFF,flags=1)
        address=TABLE+255*12
        for i in range(1,4):del memory[address+i]
        for words in (self.words,self.retail):self.assertEqual(CursorOracle(words,memory,args).outcome()[1],None)
        for address in (TICKS,args[1],args[2],TABLE+255*12):
            broken=memory.copy();del broken[address]
            for words in (self.words,self.retail):
                with self.assertRaisesRegex(AssertionError,'unmapped'):CursorOracle(words,broken,args).run()
        for offset in (0,4):
            memory,args=fixture(flags=1)
            pointer=TABLE+(args[0]&255)*12+offset
            memory.update({pointer+i:0 for i in range(4)});put(memory,pointer,0x02000000)
            args=(args[0],args[1],pointer,args[3]);result,after,trace,trap=reference(memory,args)
            for words in (self.words,self.retail):
                model=CursorOracle(words,memory,args);self.assertEqual(model.outcome(),(result,trap))
                self.assertEqual(model.memory,after);self.assertEqual(public_trace(model),trace)
        self.receipt('reads',dict(single_selected_byte=True,null_unmapped_not_silently_accepted=True,
            table_cursor_aliases=True,upper_input_bits_ignored=True))

    def test_native_32_bit_all_modes_aliases_and_unsigned_overflow(self):
        self.fixture=('typedef unsigned char u8;typedef signed char s8;typedef short s16;typedef int s32;'
            'typedef unsigned int u32;\n'+screen.DECLARATIONS+r'''
GameCursorLimit D_80090B64[256];s32 D_800BE9E4;
static s32 words[2],copy[2];
static s32 wrap(u32 value) { return (s32)value; }
static s32 expected(s32 *v,s32 *p,u8 count,u8 flags,s32 ticks) {
    s32 limit=((s32)count<<16)-1;
    s32 value=wrap((u32)*p+(u32)*v*(u32)ticks);
    *p=value;
    if(value>limit) {
        if(flags&1) return 1;
        if(flags&2) { *v=0;*p=limit; }
        else if(flags&4) { *p=limit-value%limit;*v=wrap(0U-(u32)*v); }
        else { while(value>limit) { value=wrap((u32)value-(u32)limit);*p=value; } }
    } else if(value<0 && !(flags&8)) {
        if(flags&16) { *v=0;*p=0; }
        else if(flags&4) { *p=wrap(0U-(u32)value)%limit;*v=wrap(0U-(u32)*v); }
        else { while(value<0) { value=wrap((u32)value+(u32)limit);*p=value; } }
    }
    return 0;
}
''' + screen.SELECTED)
        self.run_host(r'''
int c,p,a,f,i,r,limit,v,t; s32 tick; s32 values[9];
static u8 counts[]={1,2,7,255};static s32 speed[]={-3,0,3};
static s32 edges[]={(s32)0x80000000u,0x7FFFFFFF,-1,0,1};
static s32 ticks[]={-2,-1,0,1,2};static u8 modes[]={0,1,2,4,8,16,31};
for(c=0;c<4;c++) {
    limit=((s32)counts[c]<<16)-1;
    values[0]=-2*limit;values[1]=-limit;values[2]=-1;values[3]=0;values[4]=1;
    values[5]=limit-1;values[6]=limit;values[7]=limit+1;values[8]=2*limit+1;
    for(p=0;p<9;p++) for(a=0;a<2;a++) for(f=0;f<256;f++) {
        i=(f*17+counts[c])&255;D_80090B64[i].count=counts[c];tick=p%3-1;D_800BE9E4=tick;
        words[0]=copy[0]=a?values[p]:speed[p%3];words[1]=copy[1]=values[p];
        r=expected(copy,copy+(a?0:1),counts[c],f,tick);
        if(func_1514401C(i,words,words+(a?0:1),f)!=r || words[0]!=copy[0] || words[1]!=copy[1]) return 1;
    }
}
for(p=0;p<5;p++) for(v=0;v<5;v++) for(t=0;t<5;t++) for(f=0;f<7;f++) for(a=0;a<2;a++) {
    D_80090B64[5].count=255;D_800BE9E4=ticks[t];
    words[0]=copy[0]=a?edges[p]:edges[v];words[1]=copy[1]=edges[p];
    r=expected(copy,copy+(a?0:1),255,modes[f],ticks[t]);
    if(func_1514401C(5,words,words+(a?0:1),modes[f])!=r || words[0]!=copy[0] || words[1]!=copy[1]) return 2;
}
''')
        self.receipt('native',dict(cases=20182,word_bits=32,all_mode_bytes=True,
            full_pointer_aliases=True,unsigned_modular_arithmetic=True,invalid_division_excluded=True))

    def test_original_caller_setup_call_delay_and_status_mask(self):
        entry=0x1515BB68
        fragment=list(struct.unpack_from('>9I',self.rom,0x189018))
        self.assertEqual(fragment[-3:],[0x0D451007,0x92070012,0x304300FF])
        fragment += [0x8FBF0010,0x03E00008,0]
        cases=0
        for flags,point,phase in itertools.product(range(32),(-65536,65535,65536),(0,8)):
            memory,args=fixture(1,point,3,1,flags,index=5,phase=phase)
            memory.update({BUFFER+i:0xA5 for i in range(64)})
            put(memory,BUFFER+0x10,5,1);put(memory,BUFFER+0x12,flags,1)
            put(memory,BUFFER+0x18,point);put(memory,BUFFER+0x1C,3)
            put(memory,STACK+phase+0x10,0xDEAD0000)
            args=(5,BUFFER+0x1C,BUFFER+0x18,flags)
            result,after,trace,trap=reference(memory,args,phase)
            expected_trace=[('R',BUFFER+0x1C,4,3),('R',BUFFER+0x10,1,5),
                ('R',BUFFER+0x12,1,flags),*trace,('R',STACK+phase+0x10,4,0xDEAD0000)]
            for words in (self.words,self.retail):
                connected={screen.ENTRY+i*4:w for i,w in enumerate(words)}
                model=CursorOracle(fragment,memory,(),phase,entry,connected)
                model.r[16]=model.before[16]=BUFFER
                self.assertEqual(model.outcome(),(result,trap));self.assertEqual(model.r[3],result)
                self.assertEqual(model.calls,[(screen.ENTRY,*args)])
                self.assertEqual(model.memory,after);self.assertEqual(public_trace(model,phase),expected_trace)
            cases+=1
        self.receipt('caller',dict(cases=cases,original_words=9,original_setup_call_delay_mask=True,
            connected_candidate_and_retail=True,full_memory_and_ordered_trace=True,
            earlier_context_and_return_seeded=True,whole_caller=False))

    def test_copied_owner_neighbors_relocations_pool_and_guarded_padding(self):
        baseline=(self.root/'conker/src/game_16EE20.c').read_text().replace(screen.SELECTED,STUB).replace(
            screen.DECLARATIONS+'\n','').replace(screen.PROTOTYPE,'s32 func_1514401C();')
        selected=baseline.replace('/* Generated placeholder declarations. */',screen.DECLARATIONS+
            '\n/* Generated placeholder declarations. */').replace('s32 func_1514401C();',screen.PROTOTYPE).replace(STUB,screen.SELECTED)
        objects=[];warnings=[]
        for name,body in (('baseline',baseline),('selected',selected)):
            obj,warning=compile_owner(self.root,self.output,body,'owner-'+name);warnings.append(warning)
            processed=self.output/('owner-'+name+'-postprocessed.o');shutil.copyfile(obj,processed)
            subprocess.run([sys.executable,str(self.root/'tools/asm-processor/asm_processor.py'),'-O2','-g3',
                str((self.output/('owner-'+name+'.c')).relative_to(self.root/'conker')),'--post-process',
                str(processed.relative_to(self.root/'conker')),'--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude','include/asm_processor_prelude.inc'],cwd=self.root/'conker',check=True,capture_output=True)
            objects.append(processed)
        self.assertEqual(warnings[0],warnings[1]);self.assertEqual(len(warnings[0]),2)
        old,new=objects;ot,of,orr=parse_object(old);text,functions,rel=parse_object(new)
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
        path=self.output/'guards.csv'
        def emit(items):
            with path.open('w',newline='') as stream:
                writer=csv.DictWriter(stream,fieldnames=list(items[0]));writer.writeheader();writer.writerows(items)
            return emit_padded_assembly(new,self.root/'conker/retail_layout.us.txt','game_16EE20',
                rodata_symbol='jtbl_800A5218_game',word_patches_path=path)
        assembly=emit(rows)
        begin=assembly.index('.type %s, @function'%screen.FUNCTION)
        end=assembly.index('.size %s, . - %s'%(screen.FUNCTION,screen.FUNCTION),begin);end=assembly.index('\n',end)
        source,obj,elf=(self.output/('padded'+suffix) for suffix in ('.s','.o','.elf'))
        source.write_text('.text\n.globl '+screen.FUNCTION+'\n'+assembly[begin:end+1])
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(obj),str(source)],check=True,capture_output=True)
        subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'cursor.ld'),'-e',screen.FUNCTION,
            *['--defsym=%s=0x%X'%item for item in screen.SYMBOLS.items()],'-o',str(elf),str(obj)],check=True,capture_output=True)
        words=list(struct.unpack_from('>98I',screen.sections(elf)['.text'][1]))
        self.assertEqual(words,self.retail)
        _,padded_functions,padded_relocs=parse_object(obj)
        self.assertEqual(padded_functions[screen.FUNCTION]['size'],392)
        self.assertEqual(padded_relocs,self.record['relocations'])
        alternate=dict(D_800BE9E4=0x8123FFF0,D_80090B64=0x82348004)
        subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'cursor.ld'),'-e',screen.FUNCTION,
            *['--defsym=%s=0x%X'%item for item in alternate.items()],'-o',str(elf),str(obj)],check=True,capture_output=True)
        alt_words=list(struct.unpack_from('>98I',screen.sections(elf)['.text'][1]))
        expected=self.retail.copy()
        for hi,lo,name in ((0x18,0x1C,'D_800BE9E4'),(0x34,0x3C,'D_80090B64')):
            expected[hi//4]=expected[hi//4]&0xFFFF0000|((alternate[name]+0x8000)>>16)&65535
            expected[lo//4]=expected[lo//4]&0xFFFF0000|alternate[name]&65535
        self.assertEqual(alt_words,expected)
        broken=[dict(r) for r in rows];broken[-1]['expected']='0x00000000'
        with self.assertRaisesRegex(ValueError,'stale'):emit(broken)
        broken=[dict(r) for r in rows];broken[-1]['expected_relocations']='R_MIPS_LO16:D_800BE9E4'
        with self.assertRaisesRegex(ValueError,'stale relocations'):emit(broken)
        self.receipt('owner',dict(functions=89,neighbors_unchanged=88,
            pool_bytes=len(normalized_pools(new)['.rodata'][0]),pools_equal=True,
            warnings=2,new_warnings=0,raw_target_identical=True,relocations=4,padded_words=98,
            byte_exact=True,guards=46,stale_words_and_relocations_rejected=True,alternate_hi_lo_carry_link=True))

    def test_profiles_and_compiled_semantic_negatives(self):
        records=[]
        for profile in screen.PROFILES:
            record,words=screen.compile_candidate(self.root,self.output,'profile-'+profile,screen.SELECTED,profile);records.append(record)
            for flags,value,alias in itertools.product(range(32),(-65536,0,65535,65536),(0,1)):
                memory,args=fixture(1,value,3,1,flags,alias=alias)
                result,after,_,trap=reference(memory,args)
                model=CursorOracle(words,memory,args);self.assertEqual(model.outcome(),(result,trap))
                self.assertEqual({a:v for a,v in model.memory.items() if not STACK-0x80<=a<STACK+0x100},
                    {a:v for a,v in after.items() if not STACK-0x80<=a<STACK+0x100})
        forms={'no-tick-scale':screen.SELECTED.replace('* (u32)D_800BE9E4','* 1U'),
            'inclusive-upper':screen.SELECTED.replace('if (value > limit)','if (value >= limit)'),
            'wrong-upper-reflection':screen.SELECTED.replace('limit - value % limit','value % limit'),
            'stop-before-status':screen.SELECTED.replace('if (flags & 1)','if (flags & 2)').replace('else if (flags & 2)','else if (flags & 1)'),
            'cached-velocity':screen.SELECTED.replace('    s32 limit;','    s32 initialSpeed = *velocity;\n    s32 limit;').replace(
                '0U - (u32)*velocity','0U - (u32)initialSpeed'),
            'wrong-lower-stop':screen.SELECTED.replace('flags & 16','flags & 2')}
        negatives={}
        for name,body in forms.items():
            _,words=screen.compile_candidate(self.root,self.output,name,body);detected=0
            for flags,value,alias in itertools.product(range(32),(-65536,0,21845,65529,65535,65536),(0,1)):
                memory,args=fixture(1,value,3,2,flags,alias=alias)
                result,after,_,trap=reference(memory,args)
                model=CursorOracle(words,memory,args)
                detected+=(model.outcome()!=(result,trap) or any(model.memory[a]!=v for a,v in after.items()
                    if not STACK-0x80<=a<STACK+0x100))
            self.assertGreater(detected,0,name);negatives[name]=detected
        self.receipt('controls',dict(profiles=records,negative_detections=negatives))

    def test_production_complete_slot_and_prior_guard_history_unchanged(self):
        source=(self.root/'conker/src/game_16EE20.c').read_text();self.assertNotIn(STUB,source);self.assertIn(screen.SELECTED,source)
        functions,_,addresses=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        words=functions[screen.FUNCTION]
        self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY);self.assertEqual(len(words),98)
        self.assertEqual(words,self.retail)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:guards=list(csv.DictReader(stream))
        digest=assert_guard_history(self,guards);self.assertEqual(guards[10866:10912],screen.owner_guards())
        self.receipt('production',dict(installed=True,byte_exact=True,words=98,new_guards=46,
            guards=len(guards),guard_sha256=digest))


if __name__=='__main__':unittest.main()
