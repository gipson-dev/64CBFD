"""Scaled float-matrix fields, twelve-input ABI and bounded fixed conversion."""

import csv
import hashlib
import itertools
import json
import math
import re
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_scaled_matrix_candidates as screen
from tools.experiments.game_context_classifier_candidates import compile_owner
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import parse_object
from tools.tests import test_game_random_curve_record as native
from tools.tests.test_game_timed_interpolation_match import InterpolationOracle, rounded_bits
from tools.tests.test_game_grid_channel_updater_match import STACK, external, put, read
from tools.tests.game_animation_timeline_oracle import bits, floating

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly

ROTATE, CONVERT, CALLER = 0x150A8050, 0x150A7790, 0x15133510
ACTOR, OUTPUT, ALTERNATE = 0x20000, 0x24000, 0x26000
PATTERNS = (0,0x80000000,1,0x80000001,0x007FFFFF,0x00800000,
    0x7F7FFFFF,0xFF7FFFFF,0x7F800000,0xFF800000,0x7FC12345,0x7F812345)
ROWS0 = (0,-0.0,0.5,1,-2)
ROWS1 = (0,0.25,2,-3)
COLUMNS = ((2,-0.5,3),(-2,0,0.25),(0,0,0))
TRANSLATIONS = ((7,-9,11),(-0.0,2.5,-3.5),(0,0,0))


def provider(pattern):
    values=([0.25*(i+1) for i in range(16)],
            [(-1 if i&1 else 1)*0.5*(i%5+1) for i in range(16)],
            [1e20,1e-20,-3,7,0.125,-2,3.5,11,-0.0,0.75,-9,13,17,19,23,29])[pattern]
    return tuple(bits(v) for v in values)


def arguments(row0=1,row1=2,column=0,translation=0,alias=0):
    output=(OUTPUT,ACTOR+0x18,ACTOR+0x20)[alias]
    return (output,*map(bits,(row0,row1,0.125,-0.25,0.5,*COLUMNS[column],*TRANSLATIONS[translation])))


def memory_case(args):
    memory={STACK+i:(i*17+13)&255 for i in range(-0x600,0x100)}
    for base in (ACTOR,OUTPUT,ALTERNATE):
        memory.update({base+i:(i*31+7)&255 for i in range(-16,256)})
    for i,value in enumerate(args[1:]):put(memory,ACTOR+0x18+i*4,value)
    return memory


def mutation_actions(args,change):
    if not change:return ()
    return tuple((ACTOR+0x18+i*4,0xA5000000+i) for i in range(11))+((args[0]+8,0x12345678),)


def result_matrix(args,pattern):
    values=list(provider(pattern))
    for row in range(3):
        for col in range(3):
            factor=rounded_bits(floating(args[6+col])*floating(args[2 if row==1 else 1]))
            values[row*4+col]=rounded_bits(floating(values[row*4+col])*floating(factor))
    values[12:15]=args[9:12]
    return tuple(values)


def fixed_payload(values):
    scaled=[floating(rounded_bits(floating(v)*65536)) for v in values]
    assert all(math.isfinite(v) and v==int(v) and -0x80000000<=v<=0x7FFFFFFF for v in scaled)
    integers=[int(v)&0xFFFFFFFF for v in scaled]
    return struct.pack('>32H',*[v>>16 for v in integers],*[v&65535 for v in integers])


def reference(memory,args,pattern=0,change=False,home=None,fixed=False):
    memory=dict(memory)
    calls=[(ROTATE,args[3:6],external(memory))]
    for address,value in mutation_actions(args,change):put(memory,address,value)
    updated=list(args)
    if home is not None and home[0] not in (3,4,5):updated[home[0]]=home[1]
    values=result_matrix(updated,pattern)
    calls.append((CONVERT,values,updated[0],external(memory)))
    payload=fixed_payload(values) if fixed else struct.pack('>16I',*values)
    for i,value in enumerate(payload):memory[updated[0]+i]=value
    return external(memory),calls


class MatrixOracle(InterpolationOracle):
    def __init__(self,words,memory,args,pattern=0,change=False,phase=0,home=None,connected=None):
        super().__init__(words,memory,ACTOR,(),0,phase=phase)
        self.entry=screen.ENTRY
        self.code={screen.ENTRY+i*4:w for i,w in enumerate(words)}
        self.code.update(connected or {})
        self.r[4:8]=args[:4]
        self.before[4:8]=args[:4]
        for i,value in enumerate(args[4:]):put(self.memory,STACK+phase+16+i*4,value)
        self.args,self.pattern,self.change,self.home=args,pattern,change,home
        self.phase=phase

    def execute(self,word):
        if word>>26==17 and word>>21&31==16 and word&63==36:
            value=floating(self.f[word>>11&31])
            assert math.isfinite(value) and value==int(value) and -0x80000000<=value<=0x7FFFFFFF
            self.f[word>>6&31]=int(value)&0xFFFFFFFF
        else:super().execute(word)

    def record_call(self,target):
        if target==screen.ENTRY:
            self.forwarded=self.arguments(12)
            return
        assert target in (ROTATE,CONVERT)
        if target==ROTATE:
            args=self.arguments(4)
            self.matrix=args[0]
            call=(target,args[1:],external(self.memory))
        else:
            matrix,output=self.arguments(2)
            values=tuple(self.get(matrix+i*4,4) for i in range(16))
            call=(target,values,output,external(self.memory))
        self.calls.append(call)
        self.events.append(('CALL',target,call[1:]))

    def hook(self,target):
        if target==ROTATE:
            for i,value in enumerate(provider(self.pattern)):self.put(self.matrix+i*4,value,4)
            for address,value in mutation_actions(self.args,self.change):self.put(address,value,4)
            if self.home is not None:
                self.put(STACK+self.phase+self.home[0]*4,self.home[1],4)
        else:
            assert target==CONVERT
            _,values,output,_=self.calls[-1]
            for i,value in enumerate(values):self.put(output+i*4,value,4)
        for register in (1,2,3,*range(4,16),24,25):self.r[register]=0xA5000000+register
        self.f[:20]=[0xA5000000+i for i in range(20)]


def native_fixture():
    return r'''typedef unsigned char u8;typedef unsigned int u32;typedef int s32;typedef float f32;
typedef struct {u32 words[16];} Mtx;
typedef union {u32 align;u8 bytes[384];} Bank;
static Bank live,wanted;
static u8 *source;
static Mtx *output;
static u32 input[11],matrixWords[16],expected[16];
static int pattern,change,stage,error;
static u32 word(f32 value) {union {u32 u;f32 f;} w;w.f=value;return w.u;}
static f32 number(u32 value) {union {u32 u;f32 f;} w;w.u=value;return w.f;}
static int nanWord(u32 value) {return (value&0x7FFFFFFF)>0x7F800000;}
static int equalFloat(u32 a,u32 b) {return a==b || (nanWord(a)&&nanWord(b));}
static void mutate(Bank *bank) {
    int i,offset=(u8 *)output-live.bytes;
    if(!change)return;
    for(i=0;i<11;i++) *(u32 *)(bank->bytes+40+i*4)=0xA5000000u+i;
    *(u32 *)(bank->bytes+offset+8)=0x12345678;
}
static void initialize(int p,int m,int alias) {
    static f32 special[16]={1e20f,1e-20f,-3,7,0.125f,-2,3.5f,11,-0.0f,0.75f,-9,13,17,19,23,29};
    int i,offset;
    source=live.bytes+16;pattern=p;change=m;stage=error=0;
    output=(Mtx *)(live.bytes+(alias==0?192:alias==1?40:48));
    for(i=0;i<384;i++) live.bytes[i]=(u8)(i*31+7);
    for(i=0;i<11;i++) *(u32 *)(source+0x18+i*4)=input[i];
    for(i=0;i<16;i++) matrixWords[i]=word(pattern==0?0.25f*(i+1):
        pattern==1?(i&1?-1.0f:1.0f)*0.5f*(i%5+1):special[i]);
    for(i=0;i<384;i++) wanted.bytes[i]=live.bytes[i];
    for(i=0;i<16;i++) expected[i]=matrixWords[i];
    for(i=0;i<12;i++) if(i%4!=3) {
        volatile f32 factor=number(input[5+i%4])*number(input[i/4==1?1:0]);
        volatile f32 value=number(matrixWords[i])*factor;
        expected[i]=word(value);
    }
    for(i=0;i<3;i++) expected[12+i]=input[8+i];
    mutate(&wanted);
    offset=(u8 *)output-live.bytes;
    for(i=0;i<16;i++) *(u32 *)(wanted.bytes+offset+i*4)=expected[i];
}
__attribute__((noinline)) void func_150A8050(f32 matrix[4][4],f32 rx,f32 ry,f32 rz) {
    int i;
    if(stage++!=0 || word(rx)!=input[2] || word(ry)!=input[3] || word(rz)!=input[4]) error=1;
    for(i=0;i<16;i++) ((u32 *)matrix)[i]=matrixWords[i];
    mutate(&live);
}
__attribute__((noinline)) void guMtxF2L(f32 matrix[4][4],Mtx *destination) {
    int i;
    if(stage++!=1 || destination!=output) error=2;
    for(i=0;i<16;i++) {
        if(i<12 && i%4!=3) {
            if(!equalFloat(word(((f32 *)matrix)[i]),expected[i])) error=3;
        } else if(word(((f32 *)matrix)[i])!=expected[i]) error=4;
        destination->words[i]=word(((f32 *)matrix)[i]);
    }
}
static int check(void) {
    int i,offset;
    if(error || stage!=2)return 1;
    offset=(u8 *)output-live.bytes;
    for(i=0;i<384;i++) {
        if(i>=offset && i<offset+48 && (i-offset)%16<12 && (i-offset)%4==0) {
            if(!equalFloat(*(u32 *)(live.bytes+i),*(u32 *)(wanted.bytes+i)))return 2;
            i+=3;
        } else if(live.bytes[i]!=wanted.bytes[i])return 3;
    }
    return 0;
}
'''+screen.SELECTED+'\n'+screen.CALLER+'\n'


class GameScaledMatrixMatchTests(unittest.TestCase):
    run_host=native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        cls.output=cls.root/'conker/build/game-scaled-matrix-test'
        cls.output.mkdir(exist_ok=True)
        cls.record,cls.words=screen.compile_candidate(cls.root,cls.output,'selected')
        cls.rom=(cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail=list(struct.unpack_from('>67I',cls.rom,screen.ROM))
        cls.caller=list(struct.unpack_from('>30I',cls.rom,0x1609C0))
        cls.converter=list(struct.unpack_from('>115I',cls.rom,0xD4C40))
        cls.directory=tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path=Path(cls.directory.name)
        cls.fixture=native_fixture()

    def receipt(self,name,report):
        (self.output/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')

    def compare(self,args,pattern=0,change=False,phase=0,home=None,caller=False,fixed=False):
        memory=memory_case(args)
        wanted,calls=reference(memory,args,pattern,change,home,fixed)
        connected={}
        if caller:connected.update({CALLER+i*4:w for i,w in enumerate(self.caller)})
        if fixed:connected.update({CONVERT+i*4:w for i,w in enumerate(self.converter)})
        models=[]
        for words in (self.words,self.retail):
            model=MatrixOracle(words,memory,args,pattern,change,phase,home,connected)
            if caller:
                model.entry=CALLER
                model.r[4:8]=model.before[4:8]=[args[0],ACTOR,0,0]
            model.run()
            self.assertEqual(external(model.memory),wanted)
            self.assertEqual(model.calls,calls)
            if caller:
                self.assertEqual(model.forwarded,args)
                self.assertEqual(model.r[2],1)
            models.append(model)
        self.assertEqual(models[0].events,models[1].events)
        self.assertEqual(models[0].memory,models[1].memory)
        return models

    def test_sixteen_controls_direct_full_slot_frame_and_source_order(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],
            self.record['diagnostics']),(67,0x68,0,''))
        self.assertEqual(self.words,self.retail)
        controls=[]
        for name,body in screen.candidates():
            for profile in screen.PROFILES:
                record,_=screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                controls.append(record)
        self.assertEqual(len(controls),16)
        self.assertEqual(sum(r['differences']==0 for r in controls),1)
        self.receipt('controls',dict(selected=self.record,controls=controls))

    def test_guest_row_column_translation_provider_mutations_and_output_aliases(self):
        cases=0;coverage=[set(),set()]
        for row0,row1,column,translation,pattern,alias,change,phase in itertools.product(
            ROWS0,ROWS1,range(3),range(3),range(3),range(3),(False,True),(0,8)):
            args=arguments(row0,row1,column,translation,alias)
            for i,model in enumerate(self.compare(args,pattern,change,phase)):coverage[i].update(model.visits)
            cases+=1
        self.assertEqual(cases,6480)
        self.assertEqual([len(c) for c in coverage],[67,67])
        self.receipt('guest',dict(cases=cases,bodies=2,covered_words=[len(c) for c in coverage],
            full_traces=True,full_storage=True,helpers='bounded matrix/capture models'))

    def test_guest_all_float_input_bits_signed_zero_and_two_step_rounding_edges(self):
        cases=0
        for index,value,phase in itertools.product(range(1,12),PATTERNS,(0,8)):
            args=list(arguments(alias=index%3));args[index]=value
            self.compare(tuple(args),index%3,True,phase);cases+=1
        for row,column,pattern in itertools.product(PATTERNS,PATTERNS,range(3)):
            args=list(arguments());args[1],args[6]=row,column
            self.compare(tuple(args),pattern);cases+=1
        self.assertEqual(cases,696)
        self.receipt('edges',dict(cases=cases,all_eleven_float_inputs=True,hardware_fcsr=False,
            native_nan_payload=False))

    def test_guest_only_live_parameter_homes_after_rotation_provider(self):
        cases=0
        for index,phase,value in itertools.product(range(12),(0,8),(bits(-0.5),bits(3))):
            home=(index,ALTERNATE if index==0 else value)
            self.compare(arguments(),1,True,phase,home);cases+=1
        self.assertEqual(cases,48)
        self.receipt('private',dict(cases=cases,output_scale_translation_homes=True,
            rotation_arguments_already_captured=True,native_private_access_claim=False))

    def test_complete_original_thirty_word_caller_and_fixed_converter(self):
        coverage=[set(),set()];cases=0
        for row0,row1,column,translation,alias,change,phase in itertools.product(
            (0.5,-2),(0.25,2),range(3),range(3),range(3),(False,True),(0,8)):
            args=arguments(row0,row1,column,translation,alias)
            for i,model in enumerate(self.compare(args,1,change,phase,caller=True,fixed=True)):
                coverage[i].update(model.visits)
            cases+=1
        self.assertEqual(cases,432)
        expected=set(range(CALLER,CALLER+120,4))|set(range(CONVERT,CONVERT+460,4))|set(range(screen.ENTRY,screen.ENTRY+268,4))
        self.assertEqual(coverage,[expected,expected])
        self.receipt('connected',dict(cases=cases,caller_words=30,converter_words=115,builder_words=67,
            all_words_covered=True,provider='bounded model',conversion='finite exact integral domain',
            hardware_fcsr=False,complete_original_rotation_provider=False))

    def test_actual_native_typed_caller_all_fields_aliases_and_float_inputs(self):
        self.run_host(r'''
static f32 row0[]={0,-0.0f,0.5f,1,-2},row1[]={0,0.25f,2,-3};
static f32 columns[3][3]={{2,-0.5f,3},{-2,0,0.25f},{0,0,0}};
static f32 translations[3][3]={{7,-9,11},{-0.0f,2.5f,-3.5f},{0,0,0}};
static u32 patterns[]={0,0x80000000u,1,0x80000001u,0x007FFFFF,0x00800000,
    0x7F7FFFFF,0xFF7FFFFFu,0x7F800000,0xFF800000u,0x7FC12345,0x7F812345};
int a,b,c,d,e,f,g,i,j,cases=0;
if(sizeof(Mtx)!=64 || sizeof(f32)!=4)return 20;
for(a=0;a<5;a++) for(b=0;b<4;b++) for(c=0;c<3;c++) for(d=0;d<3;d++)
for(e=0;e<3;e++) for(f=0;f<3;f++) for(g=0;g<2;g++) {
    input[0]=word(row0[a]);input[1]=word(row1[b]);input[2]=word(0.125f);
    input[3]=word(-0.25f);input[4]=word(0.5f);
    for(i=0;i<3;i++) {input[5+i]=word(columns[c][i]);input[8+i]=word(translations[d][i]);}
    initialize(e,g,f);
    if(func_15133510(output,source)!=1 || check())return 21+error;
    cases++;
}
if(cases!=3240)return 30;
for(i=0;i<11;i++) for(j=0;j<12;j++) {
    for(a=0;a<11;a++)input[a]=word((a+1)*0.25f);
    input[i]=patterns[j];initialize(i%3,1,i%3);
    if(func_15133510(output,source)!=1 || check())return 31+error;
    cases++;
}
if(cases!=3372)return 40;
''')
        self.receipt('native',dict(cases=3372,bits=32,actual_source=True,typed_caller=True,
            all_external_storage=True,arithmetic_nan_classification=True,helpers='bounded models'))

    def test_actual_padder_preserves_symbol_extent_and_retargets_calls(self):
        text,functions,relocations=parse_object(self.output/'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['value'],0)
        self.assertEqual(functions[screen.FUNCTION]['size'],268)
        self.assertEqual(text[268:272],bytes(4))
        self.assertEqual(relocations,{0x28:[('R_MIPS_26','func_150A8050')],0xF4:[('R_MIPS_26','guMtxF2L')]})
        layout=self.output/'layout.csv'
        layout.write_text('version,section,filename,function,address,end\n'
            'us,game,game_16EE20,func_151424F4,0x151424F4,0x15142600\n')
        (self.output/'padded.s').write_text(emit_padded_assembly(self.output/'selected.o',layout,'game_16EE20'))
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(self.output/'padded.o'),
            str(self.output/'padded.s')],check=True,capture_output=True)
        padded,symbols,mapped=parse_object(self.output/'padded.o')
        self.assertEqual(symbols[screen.FUNCTION]['size'],268)
        self.assertEqual(padded[:268],text[:268])
        self.assertEqual(mapped,relocations)
        for alternate in (False,True):
            targets={name:address+(0x1000000 if alternate else 0) for name,address in screen.SYMBOLS.items()}
            elf=self.output/('padded-%d.elf'%alternate)
            subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'matrix.ld'),
                '-e',screen.FUNCTION,*['--defsym=%s=0x%X'%item for item in targets.items()],
                '-o',str(elf),str(self.output/'padded.o')],check=True,capture_output=True)
            words=list(struct.unpack_from('>67I',screen.sections(elf)['.text'][1]))
            if not alternate:self.assertEqual(words,self.retail)
            for offset,name in ((0x28,'func_150A8050'),(0xF4,'guMtxF2L')):
                self.assertEqual(words[offset//4],0x0C000000|(targets[name]>>2&0x3FFFFFF))
        self.receipt('padding',dict(bytes=268,section_alignment_tail=4,guards=0,retargeted_calls=2))

    def test_native_negative_integer_loads_must_not_convert_float_bit_words(self):
        caller=screen.CALLER
        for offset in ('0x18','0x1C','0x20'):
            caller=caller.replace('*(f32 *)(source + '+offset+')','*(s32 *)(source + '+offset+')')
        original=self.fixture
        self.fixture=original.replace(screen.CALLER,caller)
        try:
            self.run_host(r'''
int i,changed=0;
for(i=0;i<11;i++)input[i]=word((i+1)*0.25f);
initialize(1,1,1);
if(func_15133510(output,source)!=1 || stage!=2 || !error)return 41;
for(i=0;i<16;i++)changed+=output->words[i]!=expected[i];
if(!changed)return 42;
''')
        finally:self.fixture=original
        self.receipt('caller-negative',dict(actual_native=True,mapped_storage=True,
            known_argument_and_output_difference=True,numeric_conversion_rejected=True))

    def test_missing_source_matrix_or_output_fails_strict_guest_memory_gates(self):
        args=arguments()
        for address,caller in ((ACTOR+0x18,True),(ACTOR+0x40,True),(OUTPUT,False),(STACK-64,False)):
            memory=memory_case(args);del memory[address]
            connected={CALLER+i*4:w for i,w in enumerate(self.caller)} if caller else {}
            model=MatrixOracle(self.words,memory,args,connected=connected)
            if caller:
                model.entry=CALLER
                model.r[4:8]=model.before[4:8]=[OUTPUT,ACTOR,0,0]
            with self.assertRaisesRegex(AssertionError,'unmapped'):
                model.run()

    def test_compiled_negatives_change_known_output_or_call_sequence(self):
        translations='    matrix[3][0] = tx;\n    matrix[3][1] = ty;\n    matrix[3][2] = tz;\n'
        forms={'placeholder':screen.PROTOTYPE[:-1]+' { }',
            'missing-provider':screen.SELECTED.replace('    func_150A8050(matrix, rx, ry, rz);',''),
            'missing-converter':screen.SELECTED.replace('    guMtxF2L(matrix, output);',''),
            'wrong-row':screen.SELECTED.replace('cy * row1','cy * row0'),
            'wrong-column':screen.SELECTED.replace('matrix[2][0] *= cx','matrix[2][0] *= cy'),
            'wrong-translation':screen.SELECTED.replace('matrix[3][2] = tz','matrix[3][2] = tx'),
            'wrong-provider-args':screen.SELECTED.replace('matrix, rx, ry, rz','matrix, rz, ry, rx'),
            'wrong-output':screen.SELECTED.replace('matrix, output);','matrix, (Mtx *)((u8 *)output + 4));'),
            'premature-translation':screen.SELECTED.replace(translations,'').replace(
                '    func_150A8050(',translations+'    func_150A8050('),
            'reassociated-product':screen.SELECTED.replace('matrix[0][0] *= cx * row0;',
                'matrix[0][0] = (matrix[0][0] * cx) * row0;')}
        controls=[]
        for name,body in forms.items():
            _,words=screen.compile_candidate(self.root,self.output,name,body)
            differences=0
            for pattern in range(3):
                args=list(arguments(-2,0.25))
                if name=='reassociated-product':args[1],args[6]=bits(1e-20),bits(1e20)
                args=tuple(args);memory=memory_case(args)
                wanted,calls=reference(memory,args,pattern,True)
                model=MatrixOracle(words,memory,args,pattern,True).run()
                differences+=external(model.memory)!=wanted or model.calls!=calls
            self.assertGreater(differences,0,name)
            controls.append(dict(name=name,valid_mapped_cases=3,semantic_differences=differences))
        self.receipt('negatives',controls)

    def test_copied_owners_raw_neighbors_pools_warnings_and_typed_caller(self):
        source=(self.root/'conker/src/game_16EE20.c').read_text()
        baseline=source.replace(screen.SELECTED,'s32 func_151424F4() {\n    return 0;\n}').replace(
            screen.PROTOTYPE,'s32 func_151424F4();')
        stub=re.search(r's32 func_151424F4\(\) \{\n.*?\n\}',baseline,re.S)
        self.assertIsNotNone(stub)
        selected=baseline.replace(stub.group(0),screen.SELECTED).replace('s32 func_151424F4();',screen.PROTOTYPE)
        caller_source=(self.root/'conker/src/game/generated_15F680.c').read_text()
        caller_baseline=caller_source.replace(screen.CALLER,screen.OLD_CALLER).replace(
            screen.PROTOTYPE,screen.OLD_CALLER_PROTOTYPE)
        self.assertIn(screen.OLD_CALLER,caller_baseline)
        caller_selected=caller_baseline.replace(screen.OLD_CALLER,screen.CALLER).replace(
            screen.OLD_CALLER_PROTOTYPE,screen.PROTOTYPE)
        receipts=[]
        for prefix,old_source,new_source,target in (
            ('builder',baseline,selected,screen.FUNCTION),
            ('caller',caller_baseline,caller_selected,None)):
            old,old_warnings=compile_owner(self.root,self.output,old_source,prefix+'-baseline')
            new,warnings=compile_owner(self.root,self.output,new_source,prefix+'-selected')
            self.assertEqual(warnings,old_warnings)
            old_text,old_functions,old_relocs=parse_object(old)
            text,functions,relocs=parse_object(new)
            self.assertEqual(set(functions),set(old_functions))
            for name,meta in functions.items():
                prior=old_functions[name]
                if name==target:continue
                self.assertEqual(text[meta['value']:meta['value']+meta['size']],
                    old_text[prior['value']:prior['value']+prior['size']],name)
                old_rel={a-prior['value']:r for a,r in old_relocs.items() if prior['value']<=a<prior['value']+prior['size']}
                new_rel={a-meta['value']:r for a,r in relocs.items() if meta['value']<=a<meta['value']+meta['size']}
                self.assertEqual(old_rel,new_rel,name)
            if target:
                start=functions[target]['value']
                selected_text,_,selected_relocs=parse_object(self.output/'selected.o')
                self.assertEqual(text[start:start+268],selected_text[:268])
                self.assertEqual({a-start:r for a,r in relocs.items() if start<=a<start+268},selected_relocs)
            old_sections,new_sections=screen.sections(old),screen.sections(new)
            for section in ('.rodata','.data'):
                self.assertEqual(old_sections.get(section),new_sections.get(section))
            receipts.append(dict(owner=prefix,functions=len(functions),warnings=len(warnings),
                unchanged=len(functions)-(1 if target else 0),raw_caller_unchanged=target is None))
        self.receipt('owners',receipts)

    def test_production_typed_builder_caller_neighbors_data_and_unchanged_guards(self):
        owner=(self.root/'conker/src/game_16EE20.c').read_text()
        caller=(self.root/'conker/src/game/generated_15F680.c').read_text()
        self.assertIn(screen.SELECTED,owner)
        self.assertIn(screen.CALLER,caller)
        self.assertEqual(owner.count(screen.PROTOTYPE),1)
        self.assertEqual(caller.count(screen.PROTOTYPE),1)
        self.assertNotIn(screen.OLD_CALLER_PROTOTYPE,caller)
        functions,_,addresses=load_elf_functions(
            str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION],self.retail)
        self.assertEqual(functions['func_15133510'],self.caller)
        for name,rom,count in (
            ('func_15141A7C',0x16EF2C,100),('func_15141C0C',0x16F0BC,45),
            ('func_15141CC0',0x16F170,57),('func_15141DA4',0x16F254,37),
            ('func_15141E38',0x16F2E8,80),('func_15141F78',0x16F428,96),
            ('func_15142180',0x16F630,80)):
            self.assertEqual(functions[name],list(struct.unpack_from('>%dI'%count,self.rom,rom)))
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            guards=list(csv.DictReader(stream))
        self.assertEqual(len(guards),10809)
        self.assertFalse([row for row in guards if row['function']==screen.FUNCTION])
        digest=hashlib.sha256(json.dumps(guards,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        self.assertEqual(digest,'e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a')
        self.receipt('production',dict(words=67,direct=True,caller_words=30,guards=len(guards),
            guard_sha256=digest,exact_neighbors=7))


if __name__=='__main__':
    unittest.main()
