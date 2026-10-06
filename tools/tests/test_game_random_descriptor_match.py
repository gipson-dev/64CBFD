"""Direct descriptor construction, live RNG providers and the complete submit ABI."""

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

from tools.experiments import game_random_descriptor_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests.test_game_timed_interpolation_match import InterpolationOracle, rounded_bits
from tools.tests.test_game_grid_channel_updater_match import STACK, external, put, read
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests import test_game_random_curve_record as native

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly

INTEGER, FLOAT, SUBMIT = 0x150ADA20, 0x150ADA68, 0x1513C650
SOURCE, POSITION, OUTPUT, ALTERNATE = 0x20000, 0x21000, 0x22000, 0x23000
TAIL = (33, 38, 39)
PATTERNS = (0, 0x80000000, 1, 0x80000001, 0x007FFFFF, 0x00800000,
            0x7F7FFFFF, 0xFF7FFFFF, 0x7F800000, 0xFF800000, 0x7FC12345, 0x7F812345)


def memory_case(alias=0):
    memory = {STACK+i: (i*17+13)&255 for i in range(-0x600, 0x100)}
    for base in (SOURCE, POSITION, OUTPUT, ALTERNATE):
        memory.update({base+i: (i*31+7)&255 for i in range(-16, 192)})
    position = (POSITION, SOURCE, SOURCE+4)[alias]
    for base in (SOURCE, ALTERNATE):
        for offset, value in ((0, 2.5), (4, -17), (8, 9), (24, 43)):
            put(memory, base+offset, bits(value) if offset != 24 else value)
    for offset, value in ((0, 11), (4, -3), (8, 23)):
        put(memory, position+offset, bits(value))
    return memory, position


def mutate(memory, source, position, stage, mask):
    if mask & (1 << (stage-1)):
        put(memory, source, bits(1.25*stage))
        put(memory, source+24, 0x12340000+stage)
        put(memory, position, bits(-2.5*stage))
        put(memory, position+8, bits(3.75*stage))


def descriptor(memory, base, slot, first, second, source_word):
    for offset, value, size in ((0, 0x6F701, 4), (4, first%61+100, 2),
        (6, slot&255, 1), (7, 0, 1), (8, 0, 4), (12, 0, 4), (16, (second&127)+128, 1),
        (17, 255, 1), (18, 255, 1), (19, 255, 1), (20, 255, 1), (21, 255, 1),
        (22, 0, 1), (23, 7, 1), (24, 0x3B0002, 4), (28, source_word, 4),
        (32, 255, 1), (34, 40, 2), (36, 6, 2)):
        put(memory, base+offset, value, size)


def reference(memory, args, integers, sample, mask, phase=0, redirect=False):
    memory = dict(memory)
    slot, source, scale, tag, position, mode = args
    calls = []
    for stage, target in ((1, INTEGER), (2, INTEGER), (3, FLOAT)):
        if stage == 3:
            source_word = read(memory, source+24)
        calls.append((target, external(memory)))
        mutate(memory, source, position, stage, mask)
    if redirect:
        source, scale, tag, position, mode = ALTERNATE, bits(-2), 0xAB00007F, SOURCE+4, 0xFFFF0102
    product = rounded_bits(floating(sample)*5)
    shifted = rounded_bits(floating(product)+10)
    radius = rounded_bits(floating(shifted)*floating(scale))
    base = STACK+phase-0x78+0x50
    descriptor(memory, base, slot, integers[0], integers[1], source_word)
    payload = bytes(memory[base+i] for i in range(40))
    submit = (source+4, read(memory, position), read(memory, source), read(memory, position+8),
              radius, radius, tag&255, int(mode&255 == 2), 3, 1, 0, 255, 1)
    calls.append((SUBMIT, payload, submit, external(memory)))
    for i, value in enumerate(payload):
        memory[OUTPUT+i] = value
    for i, value in enumerate(submit):
        put(memory, OUTPUT+40+i*4, value)
    return external(memory), calls


class DescriptorOracle(InterpolationOracle):
    def __init__(self, words, memory, args, integers, sample, mask=0, phase=0, redirect=False):
        super().__init__(words, memory, SOURCE, (), 0, phase=phase)
        self.entry = screen.ENTRY
        self.code = {screen.ENTRY+i*4: word for i, word in enumerate(words)}
        self.r[4:8] = args[:4]
        self.before[4:8] = args[:4]
        for i, value in enumerate(args[4:]):
            put(self.memory, STACK+phase+16+i*4, value)
        self.args, self.integers, self.sample = args, integers, sample
        self.mask, self.redirect, self.initial_sp = mask, redirect, STACK+phase
        self.stage = 0

    def execute(self, word):
        if word >> 26 == 0 and word&63 in (26,27):
            left, right = self.r[word>>21&31], self.r[word>>16&31]
            assert right
            if word&63 == 26:
                left = left if left<0x80000000 else left-0x100000000
                right = right if right<0x80000000 else right-0x100000000
                quotient = abs(left)//abs(right)*(-1 if (left<0)!=(right<0) else 1)
                self.lo,self.hi = quotient&0xFFFFFFFF,(left-quotient*right)&0xFFFFFFFF
            else:
                self.lo, self.hi = left//right, left%right
        elif word >> 26 == 0 and word&63 == 16:
            self.r[word>>11&31] = self.hi
        else:
            super().execute(word)

    def record_call(self, target):
        if target == screen.ENTRY:
            self.forwarded = self.arguments(6)
            return
        if target in (INTEGER, FLOAT):
            self.calls.append((target, external(self.memory)))
        else:
            assert target == SUBMIT
            args = self.arguments(16)
            assert args[1:3] == (0, 0)
            payload = bytes(self.get(args[0]+i, 1) for i in range(40))
            self.calls.append((target, payload, args[3:], external(self.memory)))
        self.events.append(('CALL', target, self.calls[-1]))

    def hook(self, target):
        if target == SUBMIT:
            _, payload, args, _ = self.calls[-1]
            for i, value in enumerate(payload):
                self.put(OUTPUT+i, value, 1)
            for i, value in enumerate(args):
                self.put(OUTPUT+40+i*4, value, 4)
        else:
            self.stage += 1
            mutate(self.memory, self.args[1], self.args[4], self.stage, self.mask)
            if target == FLOAT and self.redirect:
                for offset, value in ((4, ALTERNATE), (8, bits(-2)), (12, 0xAB00007F),
                                      (16, SOURCE+4), (20, 0xFFFF0102)):
                    self.put(self.initial_sp+offset, value, 4)
        for register in (1, 2, 3, *range(4, 16), 24, 25):
            self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]
        if target == INTEGER:
            self.r[2] = self.integers[self.stage-1]
        elif target == FLOAT:
            self.f[0] = self.sample


def native_fixture():
    return '''typedef unsigned char u8; typedef unsigned int u32; typedef int s32;
typedef short s16; typedef float f32; typedef struct { s32 unused; } struct210;
'''+screen.DECLARATIONS+r'''
static u8 storage[256] __attribute__((aligned(4))), output[160], expected[160], before[256];
static u8 *source; static f32 *position;
static u32 randomWords[2],sampleWord,scaleWord,expectedSourceWord;
static int mask,stage,error,modeValue,tagValue,slotValue;
static u32 word(f32 v) {union {u32 u;f32 f;} w;w.f=v;return w.u;}
static f32 number(u32 v) {union {u32 u;f32 f;} w;w.u=v;return w.f;}
static u32 load(u8 *p) {return *(u32 *)p;}
static void save(u8 *p,u32 v) {*(u32 *)p=v;}
static int nanWord(u32 v) {return (v&0x7FFFFFFF)>0x7F800000;}
static int equalFloat(u32 a,u32 b) {return a==b || (nanWord(a)&&nanWord(b));}
static void change(int n) {
    if(mask&(1<<(n-1))) {
        save(source,word(1.25f*n));save(source+24,0x12340000u+n);
        save((u8 *)position,word(-2.5f*n));save((u8 *)(position+2),word(3.75f*n));
    }
}
static void step(int n) {
    int i;
    if(stage!=n-1) error=1;
    for(i=0;i<256;i++) if(storage[i]!=before[i]) error=2;
    change(n);
    for(i=0;i<256;i++) before[i]=storage[i];
    stage=n;
}
__attribute__((noinline)) s32 func_150ADA20(void) {
    int n=stage;step(n+1);return (s32)randomWords[n];
}
__attribute__((noinline)) f32 func_150ADA68(void) {step(3);return number(sampleWord);}
__attribute__((noinline)) struct210 *func_1513C650(s32 a0,u8 a1,u8 a2,s32 a3,
    f32 a4,f32 a5,f32 a6,f32 a7,f32 a8,u8 a9,u8 aA,s32 aB,s32 aC,s32 aD,u8 aE,s32 aF) {
    GameRandomDescriptor *d=(GameRandomDescriptor *)a0;
    volatile f32 product,shifted,radius;
    u32 args[13];int i;
    if(stage!=3 || a1 || a2) error=3;
    if(d->flags!=0x6F701 || (u32)d->lifetime!=randomWords[0]%61+100 || d->slot!=(u8)slotValue
       || d->kind || d->zero8 || d->zeroC || d->random!=((randomWords[1]&127)+128)
       || d->value11!=255 || d->value12!=255 || d->value13!=255 || d->value14!=255
       || d->value15!=255 || d->zero16 || d->seven!=7 || d->effect!=0x3B0002
       || d->value20!=255 || d->size!=40 || d->count!=6) error=4;
    if((u32)d->sourceWord!=expectedSourceWord) error=5;
    product=number(sampleWord)*5.0f;shifted=product+10.0f;radius=shifted*number(scaleWord);
    if(a3!=(s32)(source+4) || word(a4)!=word(position[0]) || word(a5)!=load(source)
       || word(a6)!=word(position[2]) || !equalFloat(word(a7),word(radius))
       || !equalFloat(word(a8),word(radius)) || a9!=(u8)tagValue || aA!=((u8)modeValue==2)
       || aB!=3 || aC!=1 || aD || aE!=255 || aF!=1) error=6;
    args[0]=(u32)a3;args[1]=word(a4);args[2]=word(a5);args[3]=word(a6);
    args[4]=word(a7);args[5]=word(a8);args[6]=a9;args[7]=aA;
    args[8]=aB;args[9]=aC;args[10]=aD;args[11]=aE;args[12]=aF;
    for(i=0;i<40;i++) output[i]=((u8 *)d)[i];
    for(i=0;i<13;i++) save(output+40+i*4,args[i]);
    stage=4;return (struct210 *)0x12345678;
}
static void initialize(int alias,int mutation) {
    int i;u32 sourceWord;
    source=storage+16;position=(f32 *)(alias==0?storage+112:alias==1?source:source+4);
    for(i=0;i<256;i++) storage[i]=(u8)(i*31+7);
    save(source,word(2.5f));save(source+4,word(-17));save(source+8,word(9));save(source+24,43);
    position[0]=11;position[1]=-3;position[2]=23;
    for(i=0;i<160;i++) output[i]=expected[i]=(u8)(i*17+13);
    mask=mutation;change(1);change(2);sourceWord=load(source+24);change(3);
    for(i=0;i<256;i++) before[i]=storage[i];
    expectedSourceWord=sourceWord;
    /* Restore initial storage after computing the captured source word. */
    for(i=0;i<256;i++) storage[i]=(u8)(i*31+7);
    save(source,word(2.5f));save(source+4,word(-17));save(source+8,word(9));save(source+24,43);
    position[0]=11;position[1]=-3;position[2]=23;
    for(i=0;i<256;i++) before[i]=storage[i];
    stage=error=0;
}
'''+screen.SELECTED+'\n'


class GameRandomDescriptorMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-random-descriptor-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.rom = (cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>96I', cls.rom, screen.ROM))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.fixture = native_fixture()

    def receipt(self, name, report):
        (self.output/(name+'.json')).write_text(json.dumps(report, indent=2)+'\n')

    def compare(self, memory, args, integers, sample, mask=0, phase=0, redirect=False, body=None):
        wanted, calls = reference(memory, args, integers, sample, mask, phase, redirect)
        models = [DescriptorOracle(words, memory, args, integers, sample, mask, phase, redirect).run()
                  for words in (self.words if body is None else body, self.retail)]
        for model in models:
            self.assertEqual(external(model.memory), wanted)
            self.assertEqual(model.calls, calls)
            pointer = STACK+phase-0x28
            for offset in TAIL:
                self.assertEqual(model.memory[pointer+offset], memory[pointer+offset])
                self.assertFalse([event for event in model.events if event[0]=='W' and
                    event[1] <= pointer+offset < event[1]+event[2]])
        if body is None:
            self.assertEqual(models[0].events, models[1].events)
            self.assertEqual(models[0].memory, models[1].memory)
        return models

    def test_sixty_four_controls_direct_complete_slot_and_byte_signedness(self):
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['diagnostics']), (96, 0x78, 0, ''))
        self.assertEqual(self.words, self.retail)
        records = []
        for name, body in screen.candidates():
            for profile in screen.PROFILES:
                record, words = screen.compile_candidate(self.root, self.output, name+'-'+profile, body, profile)
                records.append(record)
                if name=='shape-1000' and profile=='o2g3':
                    self.assertEqual(words, self.retail)
        self.assertEqual(len(records),64)
        self.assertEqual(sum(record['differences']==0 for record in records),2)
        signed, words = screen.compile_candidate(self.root, self.output, 'signed', screen.SIGNED)
        self.assertEqual((signed['body_words'], signed['frame'], signed['differences']), (96, 120, 6))
        offsets = [i*4 for i,(a,b) in enumerate(zip(words,self.retail)) if a!=b]
        self.assertEqual(offsets, [0x68,0x6C,0x70,0x74,0x78,0x84])
        for offset in offsets:
            self.assertEqual(words[offset//4]&0xFFFF,0xFFFF)
            self.assertEqual(self.retail[offset//4]&0xFFFF,255)
        self.receipt('controls', dict(controls=len(records), selected=self.record, signed_control=signed))

    def test_actual_padder_complete_slot_and_unchanged_call_relocations(self):
        text,functions,relocations = parse_object(self.output/'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['value'],0)
        self.assertEqual(relocations,{0x30:[('R_MIPS_26','func_150ADA20')],
            0x50:[('R_MIPS_26','func_150ADA20')],0xC4:[('R_MIPS_26','func_150ADA68')],
            0x168:[('R_MIPS_26','func_1513C650')]})
        layout=self.output/'layout.csv'
        layout.write_text('version,section,filename,function,address,end\n'
            'us,game,game_16EE20,func_15141F78,0x15141F78,0x151420F8\n')
        assembly=emit_padded_assembly(self.output/'selected.o',layout,'game_16EE20')
        (self.output/'padded.s').write_text(assembly)
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(self.output/'padded.o'),
            str(self.output/'padded.s')],check=True,capture_output=True)
        padded,symbols,mapped=parse_object(self.output/'padded.o')
        self.assertEqual(symbols[screen.FUNCTION]['size'],384)
        self.assertEqual(padded,text)
        self.assertEqual(mapped,relocations)
        for delta in (0,0x10000):
            elf=self.output/('padded-%X.elf'%delta)
            symbols={key:value+delta for key,value in screen.SYMBOLS.items()}
            subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'descriptor.ld'),
                '-e',screen.FUNCTION,*['--defsym=%s=0x%X'%item for item in symbols.items()],
                '-o',str(elf),str(self.output/'padded.o')],check=True,capture_output=True)
            words=list(struct.unpack_from('>96I',screen.sections(elf)['.text'][1]))
            if not delta:self.assertEqual(words,self.retail)
            for offset,items in relocations.items():
                self.assertEqual(words[offset//4]&0x3FFFFFF,(symbols[items[0][1]]>>2)&0x3FFFFFF)
        self.receipt('padding',dict(bytes=384,guards=0,relocations=relocations,alternate_calls=True))

    def test_guest_ordered_rng_live_reads_aliases_padding_and_full_submit_abi(self):
        coverage = [set(), set()]
        cases = 0
        for first, second, sample, scale, mode, alias, mask, phase in itertools.product(
            (0,60,61,0x80000000,0xFFFFFFFE,0xFFFFFFFF), (0,127,128,0xFFFFFFFF),
            (bits(0),bits(0.5),bits(1)), (bits(0.5),bits(-2)), (0,2,255),
            (0,2), (0,2,4,7), (0,8)):
            memory, position = memory_case(alias)
            args = (0xAB000081,SOURCE,scale,0xCD0000FF,position,0xEF000000|mode)
            for i, model in enumerate(self.compare(memory,args,(first,second),sample,mask,phase)):
                coverage[i].update(model.visits)
            cases += 1
        self.assertEqual(cases,6912)
        self.assertEqual([len(c) for c in coverage], [96,96])
        self.receipt('guest',dict(cases=cases,bodies=2,covered_words=[len(c) for c in coverage],
            full_traces=True,full_storage=True,untouched_padding=list(TAIL)))

    def test_guest_every_byte_high_aliases_and_single_precision_special_values(self):
        cases = 0
        for byte, phase in itertools.product(range(256),(0,8)):
            memory, position = memory_case(1)
            args = (0x12340000|byte,SOURCE,bits(1),0x56780000|byte,position,0x9ABC0000|byte)
            self.compare(memory,args,(0xFFFFFFFF,0x80000000),bits(0.5),7,phase)
            cases += 1
        for sample, scale, alias in itertools.product(PATTERNS,PATTERNS,range(3)):
            memory, position = memory_case(alias)
            self.compare(memory,(127,SOURCE,scale,128,position,2),(61,127),sample)
            cases += 1
        self.receipt('edges',dict(cases=cases,full_byte_aliases=512,special_float_pairs=432,
            floating_scope='binary32 values; no hardware FCSR or NaN payload claim'))

    def test_guest_only_parameter_home_reload_after_float_provider(self):
        cases = 0
        for phase, mask, slot in itertools.product((0,8),range(8),(0,127,255)):
            memory, position = memory_case()
            self.compare(memory,(slot,SOURCE,bits(1),255,position,0),(60,127),bits(0.5),mask,phase,True)
            cases += 1
        self.receipt('home',dict(cases=cases,native_private_alias_claim=False))

    def test_eight_original_callsite_delay_slots_forward_all_six_arguments(self):
        sites=((0x150EB19C,0x11864C),(0x150BEBE8,0xEC098),(0x150BEE68,0xEC318),
            (0x15146D1C,0x1741CC),(0x15146E6C,0x17431C),(0x15147460,0x174910),
            (0x15147594,0x174A44),(0x151476F4,0x174BA4))
        cases=0
        for (entry,rom),alias,phase,mode in itertools.product(sites,range(3),(0,8),(0,2,255)):
            call,delay=struct.unpack_from('>2I',self.rom,rom)
            self.assertEqual(call,0x0D4507DE)
            self.assertEqual(delay>>26,43)
            self.assertEqual(delay>>21&31,29)
            self.assertEqual(delay&65535,20)
            memory,position=memory_case(alias)
            args=(0xAB000081,SOURCE,bits(-2),0xCD0000FF,position,0xEF000000|mode)
            wanted,calls=reference(memory,args,(0xFFFFFFFF,127),bits(0.5),7,phase)
            for words in (self.words,self.retail):
                model=DescriptorOracle(words,memory,args,(0xFFFFFFFF,127),bits(0.5),7,phase)
                # Only the real jal/delay pair is connected; this epilogue is a bounded wrapper.
                model.code.update({entry:call,entry+4:delay,entry+8:0x02E0F825,
                    entry+12:0x03E00008,entry+16:0})
                model.entry=entry
                model.r[23]=model.before[23]=0xDEAD0000
                model.r[delay>>16&31]=args[5]
                put(model.memory,STACK+phase+20,0x12345678)
                model.run()
                self.assertEqual(model.forwarded,args)
                self.assertEqual(model.calls,calls)
                self.assertEqual(external(model.memory),wanted)
            cases+=1
        self.assertEqual(cases,144)
        self.receipt('callsites',dict(cases=cases,sites=sites,bodies=2,original_call_delay_words=16,
            complete_original_caller_execution=False,bounded_wrapper=True))

    def test_actual_native_source_layout_all_rng_edges_and_provider_mutations(self):
        self.run_host(r'''
static u32 integers[]={0,60,61,0x80000000u,0xFFFFFFFEu,0xFFFFFFFFu};
static u32 second[]={0,127,128,0xFFFFFFFFu};
static u32 samples[]={0,0x3F000000,0x3F800000,0x7F800000,0x7FC12345};
static u32 scales[]={0,0x80000000u,0x3F000000,0xC0000000,0x7F7FFFFF};
int a,b,c,d,e,f,g,i,cases=0;
if(sizeof(GameRandomDescriptor)!=40 || __builtin_offsetof(GameRandomDescriptor,slot)!=6
   || __builtin_offsetof(GameRandomDescriptor,sourceWord)!=28
   || __builtin_offsetof(GameRandomDescriptor,pad21)!=33
   || __builtin_offsetof(GameRandomDescriptor,size)!=34
   || __builtin_offsetof(GameRandomDescriptor,count)!=36) return 20;
for(a=0;a<6;a++) for(b=0;b<4;b++) for(c=0;c<5;c++) for(d=0;d<5;d++)
for(e=0;e<4;e++) for(f=0;f<3;f++) for(g=0;g<8;g++) {
    randomWords[0]=integers[a];randomWords[1]=second[b];sampleWord=samples[c];scaleWord=scales[d];
    slotValue=129;tagValue=255;modeValue=e==3?255:e;initialize(f,g);
    func_15141F78((u8)slotValue,source,number(scaleWord),(u8)tagValue,position,(u8)modeValue);
    if(error || stage!=4) return 21+error;
    for(i=92;i<160;i++) if(output[i]!=expected[i]) return 30;
    for(i=0;i<256;i++) if(storage[i]!=before[i]) return 31;
    cases++;
}
if(cases!=57600) return 32;
for(i=0;i<256;i++) {
    randomWords[0]=0xFFFFFFFF;randomWords[1]=0x80000000;sampleWord=0x3F000000;scaleWord=0x3F800000;
    slotValue=tagValue=modeValue=i;initialize(i%3,7);
    func_15141F78((u8)slotValue,source,number(scaleWord),(u8)tagValue,position,(u8)modeValue);
    if(error || stage!=4) return 33+error;
}
''')
        self.receipt('native',dict(cases=57856,actual_source=True,bits=32,padding_excluded=list(TAIL),
            helper='bounded submit model; original helper not executed',nan_payload_exact=False))

    def test_missing_guest_storage_fails_strict_mapped_gates(self):
        memory, position = memory_case()
        for address in (SOURCE+24,position,position+8,OUTPUT):
            missing = dict(memory);del missing[address]
            with self.assertRaises(AssertionError):
                DescriptorOracle(self.words,missing,(7,SOURCE,bits(1),9,position,2),(60,127),bits(0.5)).run()

    def test_compiled_semantic_negatives_change_known_payload_calls_or_live_reads(self):
        forms = {
            'placeholder':screen.PROTOTYPE[:-1]+' { }',
            'missing-submit':screen.SELECTED[:screen.SELECTED.index('    func_1513C650(')]+'}',
            'dereferenced-source-address':screen.SELECTED.replace('(s32)(source + 4)','*(s32 *)(source + 4)'),
            'signed-remainder':screen.SELECTED.replace('(u32)func_150ADA20() % 61U','func_150ADA20() % 61'),
            'wrong-mask':screen.SELECTED.replace('& 0x7F','& 0x3F'),
            'wrong-mode':screen.SELECTED.replace('mode == 2','mode == 1'),
            'wrong-position':screen.SELECTED.replace('position[2]','position[1]'),
            'wrong-slot':screen.SELECTED.replace('descriptor.slot = slot','descriptor.slot = 0'),
            'wrong-lifetime':screen.SELECTED.replace('% 61U + 100','% 61U + 99'),
            'wrong-flag':screen.SELECTED.replace('descriptor.effect = 0x3B0002','descriptor.effect = 0x3B0003'),
            'wrong-scale-order':screen.SELECTED.replace('(func_150ADA68() * 5.0f + 10.0f) * scale',
                'func_150ADA68() * (5.0f * scale) + 10.0f'),
            'cached-source-word':screen.SELECTED.replace('    s32 enabled;',
                '    s32 enabled;\n    s32 cached = *(s32 *)(source + 0x18);').replace(
                'descriptor.sourceWord = *(s32 *)(source + 0x18);','descriptor.sourceWord = cached;'),
        }
        report = []
        for name, body in forms.items():
            _, words = screen.compile_candidate(self.root,self.output,name,body)
            memory, position = memory_case()
            args = (129,SOURCE,bits(-2),255,position,2)
            wanted, calls = reference(memory,args,(0xFFFFFFFF,127),bits(0.5),7)
            model = DescriptorOracle(words,memory,args,(0xFFFFFFFF,127),bits(0.5),7).run()
            known = lambda output: {a:v for a,v in output.items() if a not in {OUTPUT+i for i in TAIL}}
            different = known(external(model.memory)) != known(wanted) or [
                call[0] for call in model.calls] != [call[0] for call in calls]
            self.assertTrue(different,name)
            report.append(dict(name=name,known_storage_difference=different))
        self.receipt('negatives',report)

    def test_copied_sdk_owner_changes_only_target_and_preserves_pool(self):
        baseline = (self.root/'conker/src/game_16EE20.c').read_text()
        if screen.SELECTED in baseline:
            baseline=baseline.replace(screen.SELECTED,'s32 func_15141F78() {\n    return 0;\n}')
            baseline=baseline.replace(screen.PROTOTYPE,'s32 func_15141F78();')
            baseline=baseline.replace(screen.DECLARATIONS+'\n','',1)
        placeholder = re.search(r's32 func_15141F78\(\) \{\n.*?\n\}',baseline,re.S)
        self.assertIsNotNone(placeholder)
        selected = baseline.replace('s32 func_15141F78();',screen.PROTOTYPE)
        selected = selected.replace(placeholder.group(0),screen.SELECTED)
        selected = selected.replace('typedef struct { s32 index;',screen.DECLARATIONS+'\ntypedef struct { s32 index;',1)
        old, warnings = compile_owner(self.root,self.output,baseline,'owner-baseline')
        new, new_warnings = compile_owner(self.root,self.output,selected,'owner-selected')
        self.assertEqual(warnings,new_warnings)
        self.assertEqual(len(warnings),2)
        old_text,old_functions,old_relocs = parse_object(old)
        text,functions,relocs = parse_object(new)
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
        selected_text,selected_functions,selected_relocs=parse_object(self.output/'selected.o')
        self.assertEqual(text[start:start+384],selected_text[:384])
        self.assertEqual({a-start:r for a,r in relocs.items() if start<=a<start+384},selected_relocs)
        self.assertEqual(screen.sections(old)['.rodata'][1],screen.sections(new)['.rodata'][1])
        self.receipt('owner',dict(functions=len(functions),unchanged=len(functions)-1,warnings=len(warnings),
            original_pool_unchanged=True))

    def test_production_source_complete_slot_typed_abi_and_unchanged_guards(self):
        owner=(self.root/'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.DECLARATIONS,owner)
        self.assertIn(screen.SELECTED,owner)
        self.assertEqual(owner.count(screen.PROTOTYPE),1)
        self.assertNotIn('// --- matching to here ---',owner)
        self.assertNotIn('//     func_1513C650(&tmp',owner)
        functions,_,addresses=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION],self.retail)
        for name,offset,count in (('func_15141A7C',0x16EF2C,100),('func_15141C0C',0x16F0BC,45),
            ('func_15141CC0',0x16F170,57),('func_15141DA4',0x16F254,37),('func_15141E38',0x16F2E8,80)):
            self.assertEqual(functions[name],list(struct.unpack_from('>%dI'%count,self.rom,offset)))
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows=list(csv.DictReader(stream))
        self.assertEqual(len(rows),10809)
        self.assertFalse([row for row in rows if row['function']==screen.FUNCTION])
        self.assertEqual(hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
            'e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a')


if __name__ == '__main__':
    unittest.main()
