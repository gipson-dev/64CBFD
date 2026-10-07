"""Position-copy bit provenance, scaled fields and the header/subrecord ABI."""

import csv
import hashlib
import itertools
import json
import re
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_scaled_descriptor_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_random_curve_record as native
from tools.tests.test_game_timed_interpolation_match import InterpolationOracle, rounded_bits
from tools.tests.test_game_grid_channel_updater_match import STACK, external, put, read
from tools.tests.game_animation_timeline_oracle import bits, floating

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly

SOURCE, OUTPUT = 0x20000, 0x22000
FIRST, SECOND, SUBMIT = 0x800A5470, 0x800A5474, 0x15153F18
TAIL = (61,62,63)
PATTERNS = (0,0x80000000,1,0x80000001,0x007FFFFF,0x00800000,
            0x7F7FFFFF,0xFF7FFFFF,0x7F800000,0xFF800000,0x7FC12345,0x7F812345)
CONSTANTS = ((0x3DDD2F1B,0x3E51EB86),(0,0x80000000),
             (0x00800000,0x7F7FFFFF),(0x7FC12345,0x7F812345))


def memory_case(alias=0,constants=0,output_alias=0,poison=0):
    memory={STACK+i:(i*17+13+poison)&255 for i in range(-0x600,0x100)}
    for base in (SOURCE,OUTPUT,FIRST):
        memory.update({base+i:(i*31+7)&255 for i in range(-16,192)})
    source=(SOURCE,FIRST-4,FIRST)[alias]
    for offset,value in ((0,bits(11)),(4,bits(-3)),(8,bits(23))):
        put(memory,source+offset,value)
    for address,value in zip((FIRST,SECOND),CONSTANTS[constants]):
        put(memory,address,value)
    output=(OUTPUT,source,source+4)[output_alias]
    return memory,source,output


def reference(memory,args,output=OUTPUT,phase=0):
    memory=dict(memory)
    slot,source,word,width,height=args
    base=STACK+phase-0x4C
    for offset,value in ((0,slot),(4,source),(8,word),(16,height)):
        put(memory,STACK+phase+offset,value)
    # Retail copies three words in read/store order, including guest-only partial overlap.
    for offset in (0,4,8):
        put(memory,base+8+offset,read(memory,source+offset))
    values=((20,rounded_bits(2.5*floating(width))),
        (24,rounded_bits(2*floating(width))),(28,read(memory,FIRST)),(32,read(memory,SECOND)),
        (36,rounded_bits(3*floating(height))),(40,rounded_bits(3.5*floating(height))),
        (64,0),(72,word))
    for offset,value in values:
        put(memory,base+offset,value)
    for offset,value in ((0,0),(2,255),(4,0xFFE7),(6,10),(44,3),(46,3),(48,3),
        (50,1),(52,9),(54,15),(56,180),(58,75),(68,12),(70,21)):
        put(memory,base+offset,value,2)
    put(memory,base+60,slot&255,1)
    payload=bytes(memory[base+i] for i in range(76))
    call=(SUBMIT,payload,(8,0,255,1),external(memory))
    for i,value in enumerate(payload):
        memory[output+i]=value
    for i,value in enumerate((8,0,255,1)):
        put(memory,output+76+i*4,value)
    return external(memory),[call]


class ScaledOracle(InterpolationOracle):
    def __init__(self,words,memory,args,output=OUTPUT,phase=0):
        super().__init__(words,memory,SOURCE,(),0,phase=phase)
        self.entry=screen.ENTRY
        self.code={screen.ENTRY+i*4:word for i,word in enumerate(words)}
        self.r[4:8]=args[:4]
        self.before[4:8]=args[:4]
        put(self.memory,STACK+phase+16,args[4])
        self.output=output

    def record_call(self,target):
        if target==screen.ENTRY:
            self.forwarded=self.arguments(5)
            return
        assert target==SUBMIT
        args=self.arguments(5)
        payload=bytes(self.get(args[0]+i,1) for i in range(76))
        self.calls.append((target,payload,(args[1]-args[0],*args[2:]),external(self.memory)))
        self.events.append(('CALL',target,self.calls[-1]))

    def hook(self,target):
        assert target==SUBMIT
        _,payload,args,_=self.calls[-1]
        for i,value in enumerate(payload):
            self.put(self.output+i,value,1)
        for i,value in enumerate(args):
            self.put(self.output+76+i*4,value,4)
        for register in (1,2,3,*range(4,16),24,25):
            self.r[register]=0xA5000000+register
        self.f[:20]=[0xA5000000+i for i in range(20)]


def native_fixture():
    return '''typedef unsigned char u8;typedef unsigned int u32;typedef int s32;
typedef short s16;typedef float f32;typedef struct {f32 unk0,unk4,unk8;} struct17;
'''+screen.LAYOUT+r'''
typedef union {u32 align;u8 bytes[256];} Bank;
static Bank data,constants,wantedData,wantedConstants;
static struct17 *source;
static u8 *output;
static u8 *expectedOutput;
static GameScaledDescriptor wanted;
static int error,calls;
#define D_800A5470 (*(f32 *)(constants.bytes+16))
#define D_800A5474 (*(f32 *)(constants.bytes+20))
static u32 word(f32 v) {union {u32 u;f32 f;} w;w.f=v;return w.u;}
static f32 number(u32 v) {union {u32 u;f32 f;} w;w.u=v;return w.f;}
static u32 load(u8 *p) {return *(u32 *)p;}
static void save(u8 *p,u32 v) {*(u32 *)p=v;}
static int nanWord(u32 v) {return (v&0x7FFFFFFF)>0x7F800000;}
static int equalFloat(u32 a,u32 b) {return a==b || (nanWord(a)&&nanWord(b));}
static int unknown(int offset) {return offset>=61 && offset<=63;}
static int arithmetic(int offset) {return offset==20 || offset==24 || offset==36 || offset==40;}
static void initialize(int alias,int outputAlias,int pattern) {
    static u32 values[4][2]={{0x3DDD2F1B,0x3E51EB86},{0,0x80000000u},
        {0x00800000,0x7F7FFFFF},{0x7FC12345,0x7F812345}};
    int i;
    for(i=0;i<256;i++) data.bytes[i]=constants.bytes[i]=(u8)(i*31+7);
    source=(struct17 *)(alias==0?data.bytes+16:constants.bytes+(alias==1?12:16));
    source->unk0=11;source->unk4=-3;source->unk8=23;
    save(constants.bytes+16,values[pattern][0]);save(constants.bytes+20,values[pattern][1]);
    output=outputAlias==0?data.bytes+128:outputAlias==1?(u8 *)source:(u8 *)source+4;
    expectedOutput=alias!=0 && outputAlias!=0?
        wantedConstants.bytes+(alias==1?12:16)+(outputAlias==2?4:0):
        wantedData.bytes+(outputAlias==0?128:16)+(outputAlias==2?4:0);
    error=calls=0;
}
static void reference_native(u8 slot,s32 opaque,f32 width,f32 height) {
    int i;volatile f32 a,b,c,d;
    for(i=0;i<76;i++) ((u8 *)&wanted)[i]=0xA5;
    wanted.point=*source;
    a=2.5f*width;b=2.0f*width;c=3.0f*height;d=3.5f*height;
    wanted.value14=a;wanted.value18=b;wanted.value1C=D_800A5470;wanted.value20=D_800A5474;
    wanted.value24=c;wanted.value28=d;wanted.value0=0;wanted.value2=255;
    wanted.value4=-25;wanted.value6=10;wanted.value2C=3;wanted.value2E=3;wanted.value30=3;
    wanted.value32=1;wanted.value34=9;wanted.value36=15;wanted.value38=180;wanted.value3A=75;
    wanted.slot=slot;wanted.value40=0;wanted.value44=12;wanted.value46=21;wanted.word48=opaque;
    for(i=0;i<256;i++) {wantedData.bytes[i]=data.bytes[i];wantedConstants.bytes[i]=constants.bytes[i];}
}
__attribute__((noinline)) void func_15153F18(GameScaledDescriptor *d,struct17 *point,s32 zero,u8 value,s32 one) {
    int i;u8 *expected=expectedOutput;
    calls++;
    if(point!=&d->point || zero || value!=255 || one!=1) error=1;
    for(i=0;i<76;i++) {
        if(unknown(i)) continue;
        if(arithmetic(i)) {
            if(!equalFloat(load((u8 *)d+i),load((u8 *)&wanted+i))) error=2;
            i+=3;
        } else if(((u8 *)d)[i]!=((u8 *)&wanted)[i]) error=3;
    }
    for(i=0;i<76;i++) {
        output[i]=((u8 *)d)[i];
        if(!unknown(i)) expected[i]=((u8 *)&wanted)[i];
    }
    save(output+76,8);save(output+80,0);save(output+84,255);save(output+88,1);
    save(expected+76,8);save(expected+80,0);save(expected+84,255);save(expected+88,1);
}
static int check(void) {
    int i,offset;u8 *current,*expected;
    if(error || calls!=1) return 1;
    for(i=0;i<512;i++) {
        current=i<256?data.bytes+i:constants.bytes+i-256;
        expected=i<256?wantedData.bytes+i:wantedConstants.bytes+i-256;
        offset=(s32)current-(s32)output;
        if(unknown(offset)) continue;
        if(arithmetic(offset)) {
            if(!equalFloat(load(current),load(expected))) return 2;
            i+=3;
        } else if(*current!=*expected) return 3;
    }
    return 0;
}
'''+screen.SELECTED+'\n'


class GameScaledDescriptorMatchTests(unittest.TestCase):
    run_host=native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        cls.output=cls.root/'conker/build/game-scaled-descriptor-test'
        cls.output.mkdir(exist_ok=True)
        cls.record,cls.words=screen.compile_candidate(cls.root,cls.output,'selected')
        cls.rom=(cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail=list(struct.unpack_from('>80I',cls.rom,screen.ROM))
        cls.directory=tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path=Path(cls.directory.name)
        cls.fixture=native_fixture()

    def receipt(self,name,report):
        (self.output/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')

    def compare(self,memory,args,output=OUTPUT,phase=0):
        wanted,calls=reference(memory,args,output,phase)
        models=[ScaledOracle(words,memory,args,output,phase).run() for words in (self.words,self.retail)]
        for model in models:
            self.assertEqual(external(model.memory),wanted)
            self.assertEqual(model.calls,calls)
            base=STACK+phase-0x4C
            for offset in TAIL:
                self.assertEqual(model.memory[base+offset],memory[base+offset])
                self.assertFalse([e for e in model.events if e[0]=='W' and e[1]<=base+offset<e[1]+e[2]])
        self.assertEqual(models[0].events,models[1].events)
        self.assertEqual(models[0].memory,models[1].memory)
        return models

    def test_sixty_four_controls_original_integer_literal_and_store_order(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],
                          self.record['diagnostics']),(80,0x70,0,''))
        self.assertEqual(self.words,self.retail)
        records=[]
        for name,body in screen.candidates():
            for profile in screen.PROFILES:
                record,words=screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                records.append(record)
                if record['differences']==0:self.assertEqual(words,self.retail)
        self.assertEqual(len(records),64)
        self.assertEqual(sum(r['differences']==0 for r in records),1)
        self.receipt('controls',dict(controls=records,selected=self.record))

    def test_guest_live_constants_full_width_words_and_aliased_source_output(self):
        coverage=[set(),set()];cases=0
        for opaque,width,height,alias,output_alias,slot,phase in itertools.product(
            (0,1,0xFFFFFFFF,0x80000000,0x3F800000,0x7FC12345),
            (bits(0),bits(-0.0),bits(0.5),bits(1),bits(-2)),
            (bits(0),bits(-0.0),bits(0.5),bits(1),bits(-2)),
            range(3),range(3),(0,127,128,255),(0,8)):
            memory,source,output=memory_case(alias,output_alias=output_alias)
            args=(0xAB000000|slot,source,opaque,width,height)
            for i,model in enumerate(self.compare(memory,args,output,phase)):coverage[i].update(model.visits)
            cases+=1
        self.assertEqual(cases,10800)
        self.assertEqual([len(c) for c in coverage],[80,80])
        self.receipt('guest',dict(cases=cases,bodies=2,covered_words=[len(c) for c in coverage],
            full_traces=True,full_storage=True,untouched_padding=list(TAIL)))

    def test_guest_every_byte_float_patterns_and_live_constant_bit_patterns(self):
        cases=0
        for slot,phase in itertools.product(range(256),(0,8)):
            memory,source,output=memory_case(slot%3,slot%4,slot%3)
            self.compare(memory,(0xFFFF0000|slot,source,0x7FC12345,bits(-2),bits(0.5)),output,phase)
            cases+=1
        for width,height,constants,alias in itertools.product(PATTERNS,PATTERNS,range(4),range(3)):
            memory,source,output=memory_case(alias,constants)
            self.compare(memory,(255,source,0x80000000,width,height),output)
            cases+=1
        self.receipt('edges',dict(cases=cases,byte_aliases=512,float_and_constant_patterns=1728,
            hardware_fcsr=False,nan_payload_arithmetic_claim=False))

    def test_guest_only_parameter_homes_and_partial_private_position_overlap(self):
        cases=0
        for phase,offset,poison in itertools.product((0,8),(0,4,16,-0x4C,-0x48,-0x44,-0x40),(0,61)):
            memory,_,output=memory_case(poison=poison)
            source=STACK+phase+offset
            self.compare(memory,(0xAB000081,source,0x12345678,bits(-2),bits(0.5)),output,phase)
            cases+=1
        self.receipt('private',dict(cases=cases,interleaved_read_store_copy=True,
            native_private_or_partial_overlap_claim=False))

    def test_actual_native_source_layout_opaque_words_constants_and_output_aliases(self):
        self.run_host(r'''
static u32 opaque[]={0,0xFFFFFFFFu,0x80000000u,0x7FC12345};
static u32 values[]={0,0x80000000u,0x3F000000,0xC0000000,0x7F7FFFFF,0x7FC12345};
int a,b,c,d,e,f,g,i,cases=0;u8 slot;
if(sizeof(struct17)!=12 || sizeof(GameScaledDescriptor)!=76
   || __builtin_offsetof(GameScaledDescriptor,point)!=8
   || __builtin_offsetof(GameScaledDescriptor,value14)!=20
   || __builtin_offsetof(GameScaledDescriptor,value2C)!=44
   || __builtin_offsetof(GameScaledDescriptor,slot)!=60
   || __builtin_offsetof(GameScaledDescriptor,value40)!=64
   || __builtin_offsetof(GameScaledDescriptor,word48)!=72) return 20;
for(a=0;a<4;a++) for(b=0;b<6;b++) for(c=0;c<6;c++) for(d=0;d<4;d++)
for(e=0;e<3;e++) for(f=0;f<3;f++) for(g=0;g<4;g++) {
    slot=(u8)(g==3?255:g==2?128:g==1?127:0);initialize(e,f,d);
    reference_native(slot,(s32)opaque[a],number(values[b]),number(values[c]));
    func_15142180(slot,source,(s32)opaque[a],number(values[b]),number(values[c]));
    if(check()) return 21+error;
    cases++;
}
if(cases!=20736) return 30;
for(i=0;i<256;i++) {
    initialize(i%3,i%3,i%4);reference_native((u8)i,0x12345678,-2,0.5f);
    func_15142180((u8)i,source,0x12345678,-2,0.5f);
    if(check()) return 31+error;
}
''')
        self.receipt('native',dict(cases=20992,bits=32,actual_source=True,
            padding_excluded=list(TAIL),arithmetic_nan_classification=True,submit='bounded model'))

    def test_actual_padder_complete_slot_and_alternate_constant_relocations(self):
        text,functions,relocations=parse_object(self.output/'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['value'],0)
        self.assertEqual(relocations,{0x70:[('R_MIPS_HI16','D_800A5470')],
            0x74:[('R_MIPS_LO16','D_800A5470')],0x78:[('R_MIPS_HI16','D_800A5474')],
            0x80:[('R_MIPS_LO16','D_800A5474')],0x128:[('R_MIPS_26','func_15153F18')]})
        layout=self.output/'layout.csv'
        layout.write_text('version,section,filename,function,address,end\n'
            'us,game,game_16EE20,func_15142180,0x15142180,0x151422C0\n')
        (self.output/'padded.s').write_text(emit_padded_assembly(self.output/'selected.o',layout,'game_16EE20'))
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(self.output/'padded.o'),
            str(self.output/'padded.s')],check=True,capture_output=True)
        padded,symbols,mapped=parse_object(self.output/'padded.o')
        self.assertEqual(symbols[screen.FUNCTION]['size'],320)
        self.assertEqual(padded,text)
        self.assertEqual(mapped,relocations)
        for first in (FIRST,0x90018004):
            targets=dict(screen.SYMBOLS,D_800A5470=first,D_800A5474=first+4)
            elf=self.output/('padded-%X.elf'%first)
            subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'descriptor.ld'),
                '-e',screen.FUNCTION,*['--defsym=%s=0x%X'%item for item in targets.items()],
                '-o',str(elf),str(self.output/'padded.o')],check=True,capture_output=True)
            words=list(struct.unpack_from('>80I',screen.sections(elf)['.text'][1]))
            if first==FIRST:self.assertEqual(words,self.retail)
            for hi,lo,address in ((0x70,0x74,first),(0x78,0x80,first+4)):
                self.assertEqual(words[hi//4]&65535,((address+0x8000)>>16)&65535)
                self.assertEqual(words[lo//4]&65535,address&65535)
        self.receipt('padding',dict(bytes=320,guards=0,relocations=relocations,alternate_constant_carries=True))

    def test_seven_original_call_delay_pairs_forward_five_arguments(self):
        sites=((0x15146D48,0x1741F8),(0x15146EF4,0x1743A4),(0x15147378,0x174828),
            (0x151475C0,0x174A70),(0x15147720,0x174BD0),(0x150BEC18,0xEC0C8),(0x150BEE98,0xEC348))
        cases=0
        for (entry,rom),alias,phase in itertools.product(sites,range(3),(0,8)):
            call,delay=struct.unpack_from('>2I',self.rom,rom)
            self.assertEqual(call,0x0D450860)
            self.assertEqual(delay>>26,57)
            self.assertEqual(delay>>21&31,29)
            self.assertEqual(delay&65535,16)
            memory,source,output=memory_case(alias)
            args=(0xAB000081,source,0x12345678,bits(-2),bits(0.5))
            wanted,calls=reference(memory,args,output,phase)
            for words in (self.words,self.retail):
                model=ScaledOracle(words,memory,args,output,phase)
                model.code.update({entry:call,entry+4:delay,entry+8:0x02E0F825,
                    entry+12:0x03E00008,entry+16:0})
                model.entry=entry
                model.r[23]=model.before[23]=0xDEAD0000
                model.f[delay>>16&31]=args[4]
                put(model.memory,STACK+phase+16,0x12345678)
                model.run()
                self.assertEqual(model.forwarded,args)
                self.assertEqual(model.calls,calls)
                self.assertEqual(external(model.memory),wanted)
            cases+=1
        self.assertEqual(cases,42)
        self.receipt('callsites',dict(cases=cases,sites=sites,original_call_delay_words=14,
            complete_original_caller_execution=False,bounded_wrapper=True))

    def test_missing_guest_source_constants_or_output_fail_strict_memory_gates(self):
        memory,source,output=memory_case()
        for address in (source,source+8,FIRST,SECOND,output):
            missing=dict(memory);del missing[address]
            with self.assertRaises(AssertionError):
                ScaledOracle(self.words,missing,(7,source,0x12345678,bits(-2),bits(0.5)),output).run()

    def test_compiled_negatives_change_known_payload_or_submit_arguments(self):
        forms={'placeholder':screen.PROTOTYPE[:-1]+' { }',
            'missing-submit':screen.SELECTED.replace('    func_15153F18(&descriptor, &descriptor.point, 0, 255, 1);',''),
            'wrong-copy':screen.SELECTED.replace('descriptor.point = *source;',
                'descriptor.point.unk0 = 0; descriptor.point.unk4 = 0; descriptor.point.unk8 = 0;'),
            'wrong-opaque-width':screen.SELECTED.replace('descriptor.word48 = word;','descriptor.word48 = word & 0xFFFF;'),
            'wrong-slot':screen.SELECTED.replace('descriptor.slot = slot;','descriptor.slot = 0;'),
            'wrong-width':screen.SELECTED.replace('2.5f * width','2.0f * width'),
            'wrong-height':screen.SELECTED.replace('3.5f * height','3.0f * height'),
            'wrong-constant':screen.SELECTED.replace('descriptor.value1C = D_800A5470;','descriptor.value1C = D_800A5474;'),
            'wrong-signed-header':screen.SELECTED.replace('descriptor.value4 = -25;','descriptor.value4 = 25;'),
            'wrong-halfword':screen.SELECTED.replace('descriptor.value38 = 180;','descriptor.value38 = 179;'),
            'wrong-subrecord':screen.SELECTED.replace('&descriptor.point, 0, 255, 1',
                '(struct17 *)((u8 *)&descriptor + 4), 0, 255, 1'),
            'wrong-submit-flag':screen.SELECTED.replace('&descriptor.point, 0, 255, 1','&descriptor.point, 0, 254, 1')}
        receipts=[]
        for name,body in forms.items():
            _,words=screen.compile_candidate(self.root,self.output,name,body)
            memory,source,output=memory_case()
            args=(129,source,0x12345678,bits(-2),bits(0.5))
            wanted,calls=reference(memory,args,output)
            model=ScaledOracle(words,memory,args,output).run()
            known=lambda storage:{a:v for a,v in storage.items() if a not in {output+i for i in TAIL}}
            changed=known(external(model.memory))!=known(wanted) or len(model.calls)!=len(calls)
            self.assertTrue(changed,name)
            receipts.append(dict(name=name,known_storage_or_call_difference=changed))
        self.receipt('negatives',receipts)

    def test_copied_owner_raw_neighbors_original_pool_and_unchanged_warnings(self):
        baseline=(self.root/'conker/src/game_16EE20.c').read_text()
        if screen.SELECTED in baseline:
            baseline=baseline.replace(screen.SELECTED,'s32 func_15142180() {\n    return 0;\n}')
            baseline=baseline.replace(screen.PROTOTYPE,'s32 func_15142180();')
            baseline=baseline.replace(screen.LOCAL_DECLARATIONS+'\n','',1)
        placeholder=re.search(r's32 func_15142180\(\) \{\n.*?\n\}',baseline,re.S)
        self.assertIsNotNone(placeholder)
        selected=baseline.replace('s32 func_15142180();',screen.PROTOTYPE)
        selected=selected.replace(placeholder.group(0),screen.SELECTED)
        selected=selected.replace('typedef struct { s32 index;',
            screen.LOCAL_DECLARATIONS+'\ntypedef struct { s32 index;',1)
        old,warnings=compile_owner(self.root,self.output,baseline,'owner-baseline')
        new,new_warnings=compile_owner(self.root,self.output,selected,'owner-selected')
        self.assertEqual(warnings,new_warnings)
        self.assertEqual(len(warnings),2)
        old_text,old_functions,old_relocs=parse_object(old)
        text,functions,relocs=parse_object(new)
        self.assertEqual(set(functions),set(old_functions))
        for name,meta in functions.items():
            if name==screen.FUNCTION:continue
            prior=old_functions[name]
            self.assertEqual(text[meta['value']:meta['value']+meta['size']],
                old_text[prior['value']:prior['value']+prior['size']],name)
            old_rel={a-prior['value']:r for a,r in old_relocs.items() if prior['value']<=a<prior['value']+prior['size']}
            new_rel={a-meta['value']:r for a,r in relocs.items() if meta['value']<=a<meta['value']+meta['size']}
            self.assertEqual(old_rel,new_rel,name)
        start=functions[screen.FUNCTION]['value']
        selected_text,_,selected_relocs=parse_object(self.output/'selected.o')
        self.assertEqual(text[start:start+320],selected_text[:320])
        self.assertEqual({a-start:r for a,r in relocs.items() if start<=a<start+320},selected_relocs)
        self.assertEqual(screen.sections(old)['.rodata'][1],screen.sections(new)['.rodata'][1])
        self.receipt('owner',dict(functions=len(functions),unchanged=len(functions)-1,warnings=len(warnings),
            original_pool_unchanged=True))

    def test_production_linked_slot_original_data_and_guard_manifest(self):
        source=(self.root/'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.LOCAL_DECLARATIONS,source)
        self.assertIn(screen.SELECTED,source)
        self.assertEqual(source.count(screen.PROTOTYPE),1)
        functions,_,addresses=load_elf_functions(
            str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION],self.retail)
        for name,rom,count in (
            ('func_15141A7C',0x16EF2C,100),('func_15141C0C',0x16F0BC,45),
            ('func_15141CC0',0x16F170,57),('func_15141DA4',0x16F254,37),
            ('func_15141E38',0x16F2E8,80),('func_15141F78',0x16F428,96)):
            self.assertEqual(functions[name],list(struct.unpack_from('>%dI'%count,self.rom,rom)))
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards=list(csv.DictReader(stream))
        self.assertEqual(len(guards),10809)
        digest=hashlib.sha256(json.dumps(guards,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        self.assertEqual(digest,'e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a')
        data=screen.sections(self.root/'conker/build/conker.us.elf')['.game_data']
        self.assertEqual(data[1][FIRST-data[0]:SECOND-data[0]+4],self.rom[0x249F30:0x249F38])
        self.receipt('production',dict(words=80,direct=True,guards=len(guards),
            guard_sha256=digest,original_constants=True,exact_neighbors=6))


if __name__=='__main__':
    unittest.main()
