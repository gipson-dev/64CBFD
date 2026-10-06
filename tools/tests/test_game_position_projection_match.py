"""Projection aliases, float-bit ABI and bounded connected SDK instruction paths."""

import csv
import hashlib
import itertools
import json
import math
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_position_projection_candidates as screen
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import ELF_HEADER, SECTION_HEADER, read_c_string
from tools.tests.test_game_payload_copy_wrapper_match import SignedByteOracle, external, read
from tools.tests.test_game_actor_triangle_transform_match import put, MATRIX, TAIL, CONTINUATION
from tools.tests.test_game_table_range_loader import STACK
from tools.tests.game_animation_timeline_oracle import bits, floating
from tools.tests import test_game_random_curve_record as native

ROTATION = screen.SYMBOLS['func_150A8050']
ACTOR, ORIGIN, COEFFICIENTS, ANGLES = 0x21000, 0x22000, 0x23000, 0x24000
TRIG_A, TRIG_B, UNIT = 0x150AD780, 0x150AD78C, 0x8009F6C0
ALIASES = (None,0x34,0x38,0x3C,0x40,0x44,0x48,0x4C)
SPECIAL = (0,0x80000000,1,0x007FFFFF,0x00800000,0x7F7FFFFF,0xFF7FFFFF,
           0x7F800000,0xFF800000,0x7FC00001,0x7FA00001,0xFFA12345)


def number(value):
    return floating(bits(value))


def equal_arithmetic_nan_memory(test, actual, expected):
    actual,expected = dict(actual),dict(expected)
    for offset in (0x34,0x38,0x3C,0x40,0x44,0x48):
        address = ACTOR+offset
        if math.isnan(floating(read(actual,address))) or math.isnan(floating(read(expected,address))):
            test.assertTrue(math.isnan(floating(read(actual,address))) and math.isnan(floating(read(expected,address))))
            put(actual,address,0); put(expected,address,0)
    test.assertEqual(actual,expected)


def matrix_case(mode):
    result = [0.0]*16
    for i in (0,5,10,15): result[i] = 1.0
    if mode==1: result[1],result[4],result[5],result[9] = 2.0,-0.5,0.25,-3.0
    if mode==2: result[0],result[5],result[10],result[6] = -1.0,-2.0,0.0,1.5
    if mode==3: result[4],result[5],result[6],result[0],result[9] = 0.125,3.0,-0.25,2.0,-0.75
    return list(map(bits,result))


def memory_case(alias=None, mode=0):
    memory = {STACK+i:0xA5 for i in range(-0x600,0x100)}
    for base,length in ((ACTOR-16,0x240),(ORIGIN-16,80),(COEFFICIENTS-16,96),(ANGLES-16,64),(UNIT,4)):
        memory.update({base+i:(i*13+7)&255 for i in range(length)})
    for i in range(20): put(memory,ACTOR+0x30+i*4,bits(float(i+1)))
    for i,value in enumerate((10.0,20.0,30.0)): put(memory,ORIGIN+i*4,bits(value))
    for i,value in enumerate(matrix_case(mode)): put(memory,COEFFICIENTS+i*4,value)
    put(memory,ACTOR+0x178,ANGLES)
    for i,value in enumerate((0.125,1.0,-0.75)): put(memory,ANGLES+i*4,bits(value))
    return memory,ORIGIN if alias is None else ACTOR+alias


def actions(memory, stage, actor, origin, mutation, phase=0, writer=None):
    write = writer or (lambda address,value,size=4: put(memory,address,value,size))
    if stage==ROTATION:
        if mutation&1:
            for i,value in enumerate((3.0,-4.0,5.0)): write(actor+0x34+i*4,bits(value))
        if mutation&2:
            for i,value in enumerate((-11.0,7.0,0.125)): write(origin+i*4,bits(value))
        if mutation&4:
            write(STACK+phase+8,bits(-2.5)); write(STACK+phase+12,bits(0.75))
    else:
        if mutation&8:
            for i,value in enumerate((9.0,-3.5,1.25)): write(origin+i*4,bits(value))
        if mutation&16:
            for i,value in enumerate((0.125,-2.0,7.0)): write(actor+0x34+i*4,bits(value))


def transform(matrix, coordinate):
    matrix = list(map(floating,matrix)); x,y,z = map(floating,coordinate)
    output = []
    for axis in range(3):
        first = number(number(matrix[axis]*x)+number(matrix[axis+4]*y))
        second = number(number(matrix[axis+8]*z)+matrix[axis+12])
        output.append(bits(first+second))
    return output


def reference(memory, args, mutation=0, phase=0, coefficients=None):
    memory = dict(memory)
    actor,origin,height,scale,angle_x,angle_z = args
    put(memory,STACK+phase+8,height); put(memory,STACK+phase+12,scale)
    calls = [(ROTATION,angle_x,0,angle_z)]
    matrix = [read(memory,COEFFICIENTS+i*4) for i in range(16)] if coefficients is None else list(coefficients)
    actions(memory,ROTATION,actor,origin,mutation,phase)
    for axis in range(3): matrix[12+axis] = read(memory,origin+axis*4)
    height = read(memory,STACK+phase+8)
    calls.append((MATRIX,tuple(matrix),0,height,0,actor+0x34,actor+0x38,actor+0x3C))
    for axis,value in enumerate(transform(matrix,(0,height,0))): put(memory,actor+0x34+axis*4,value)
    actions(memory,MATRIX,actor,origin,mutation,phase)
    positions = [read(memory,actor+0x34+i*4) for i in range(3)]
    sources = [read(memory,origin+i*4) for i in range(3)]
    scale = floating(read(memory,STACK+phase+12))
    products = [number(number(floating(p)-floating(s))*scale) for p,s in zip(positions,sources)]
    for axis,(position,product) in enumerate(zip(positions,products)):
        put(memory,actor+0x40+axis*4,bits(floating(position)+number(product*500.0)))
    return external(memory),calls,positions[0]


class ProjectionOracle(SignedByteOracle):
    def __init__(self, words, memory, args, mutation=0, phase=0, connected=None, entry=screen.ENTRY):
        super().__init__(words,memory,entry=entry,arguments=args,phase=phase,connected=connected)
        self.actor,self.origin,self.mutation,self.phase = args[0],args[1],mutation,phase

    def record_call(self, target):
        if target==screen.ENTRY:
            args = self.arguments(6)
            self.actor,self.origin = args[:2]
            self.phase = self.r[29]-STACK
            call = (target,*args)
        elif target==ROTATION:
            call = (target,*self.arguments(4)[1:])
        else:
            assert target==MATRIX
            matrix,x,y,z,*outputs = self.arguments(7)
            snapshot = tuple(read(self.memory,matrix+i*4) for i in range(16))
            call = (target,snapshot,x,y,z,*outputs)
        self.calls.append(call); self.events.append(('CALL',target,call[1:]))

    def hook(self, target):
        if target==ROTATION:
            matrix = self.r[4]
            for i in range(16): self.put(matrix+i*4,read(self.memory,COEFFICIENTS+i*4),4)
        else:
            assert target==MATRIX
            matrix,x,y,z,*outputs = self.arguments(7)
            values = [read(self.memory,matrix+i*4) for i in range(16)]
            for destination,value in zip(outputs,transform(values,(x,y,z))): self.put(destination,value,4)
        actions(self.memory,target,self.actor,self.origin,self.mutation,self.phase,
                writer=lambda a,v,s=4:self.put(a,v,s))
        for register in (1,2,3,*range(4,16),24,25): self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]


def sdk_matrix(values):
    a,b,c,d,e,f = values
    bd,ad = number(b*d),number(a*d)
    return list(map(bits,(number(c*e),number(c*f),-d,0.0,
        number(number(bd*e)-number(a*f)),number(number(bd*f)+number(a*e)),number(b*c),0.0,
        number(number(ad*e)+number(b*f)),number(number(ad*f)-number(b*e)),number(a*c),0.0,
        0.0,0.0,0.0,1.0)))


class SdkProjectionOracle(ProjectionOracle):
    def __init__(self, words, memory, args, connected, responses, phase=0):
        super().__init__(words,memory,args,phase=phase,connected=connected)
        self.responses,self.trig_calls = responses,0

    def execute(self, word):
        if word>>26==17 and word>>21&31==16 and word&63==7:
            self.f[word>>6&31] = self.f[word>>11&31]^0x80000000
        else: super().execute(word)

    def record_call(self, target):
        if target in (TRIG_A,TRIG_B):
            call = (target,self.f[12]); self.calls.append(call); self.events.append(('CALL',target,call[1:]))
        else: super().record_call(target)

    def hook(self, target):
        assert target in (TRIG_A,TRIG_B)
        result = self.responses[self.trig_calls]; self.trig_calls += 1
        for register in (1,2,3,*range(4,16),24,25): self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]; self.f[0] = bits(result)


class GamePositionProjectionMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-position-projection-test'; cls.output.mkdir(exist_ok=True)
        cls.record,cls.words = screen.compile_candidate(cls.root,cls.output,'selected')
        cls.caller_record,cls.caller = screen.compile_candidate(cls.root,cls.output,'caller',screen.CALLER,caller=True)
        rom = (cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>63I',rom,screen.ROM))
        cls.retail_caller = list(struct.unpack_from('>18I',rom,screen.CALLER_ROM))
        cls.sdk = {}
        for entry,offset,length in ((ROTATION,0xD5500,83),(MATRIX,0xD4E10,40),
                                    (TAIL,0xD4EB0,5),(CONTINUATION,0xD4EC4,13)):
            cls.sdk.update({entry+i*4:word for i,word in enumerate(struct.unpack_from('>%dI'%length,rom,offset))})
        data = (cls.root/'conker/build/conker.us.elf').read_bytes()
        header = ELF_HEADER.unpack_from(data)
        sections = [SECTION_HEADER.unpack_from(data,header[6]+i*header[11]) for i in range(header[12])]
        names = sections[header[13]]; strings = data[names[4]:names[4]+names[5]]
        section = next(s for s in sections if read_c_string(strings,s[0])=='.game_data')
        cls.unit = struct.unpack_from('>I',data,section[4]+UNIT-section[3])[0]
        cls.directory = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name); cls.coverage = [set(),set()]; cls.cases = 0

    def models(self, memory, args, mutation=0, phase=0):
        wanted = reference(memory,args,mutation,phase)
        models = []
        for index,body in enumerate((self.words,self.retail)):
            model = ProjectionOracle(body,memory,args,mutation,phase).run()
            self.assertEqual((external(model.memory),model.calls,model.f[0]),wanted)
            type(self).coverage[index].update(model.visits); models.append(model)
        self.assertEqual(models[0].events,models[1].events)
        type(self).cases += 1
        return models[0]

    def test_direct_full_slot_caller_abi_and_thirty_six_controls(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences']), (63,128,0))
        self.assertEqual(self.words,self.retail)
        self.assertEqual((self.caller_record['body_words'],self.caller_record['slot_words'],self.caller_record['frame'],
                          self.caller_record['differences']),(16,18,32,0))
        self.assertEqual(self.caller,self.retail_caller)
        records = []
        for name,body in screen.candidates():
            for profile in screen.PROFILES:
                record,_ = screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                self.assertEqual(record['diagnostics'],''); records.append(record)
        for profile in screen.PROFILES:
            record,_ = screen.compile_candidate(self.root,self.output,'caller-'+profile,screen.CALLER,profile,caller=True)
            self.assertEqual(record['diagnostics'],''); records.append(record)
        self.assertEqual([r['name'] for r in records if r['exact']],
                         ['shape-000-o2g3','shape-001-o2g3','shape-100-o2g3','shape-101-o2g3','caller-o2g3'])
        (self.output/'controls.json').write_text(json.dumps(records,indent=2)+'\n')

    def test_guest_full_storage_aliases_mutations_and_rounding(self):
        cases = 0
        for alias,mode,height,scale,mutation,phase in itertools.product(ALIASES,range(4),
                (-3.0,-0.0,0.0,1.25,7.0),(-2.0,-0.0,0.0,0.00025,0.25,1.5),
                (0,1,2,3,8,16,24,31),(0,8)):
            memory,origin = memory_case(alias,mode)
            args = (ACTOR,origin,bits(height),bits(scale),bits(0.125),bits(-0.75))
            self.models(memory,args,mutation,phase); cases += 1
        self.assertEqual(cases,15360)
        self.assertEqual(self.coverage,[set(range(screen.ENTRY,screen.ENTRY+252,4))]*2)

    def test_saved_float_argument_homes_are_guest_only_live_reads(self):
        for alias,mutation,phase in itertools.product(ALIASES,(4,5,6,7,12,20,28,31),(0,8)):
            memory,origin = memory_case(alias,3)
            self.models(memory,(ACTOR,origin,bits(1.25),bits(0.125),bits(-0.0),bits(2.0)),mutation,phase)

    def test_connected_retail_rotation_and_coordinate_instructions(self):
        cases,coverage = 0,set()
        responses = ((1.0,0.0,1.0,0.0,1.0,0.0),(0.5,-0.25,-0.75,0.125,2.0,-1.0),
                     (-1.0,0.5,0.25,-0.5,-0.25,0.75))
        for alias,values,height,phase in itertools.product(ALIASES,responses,(-2.0,0.0,3.0),(0,8)):
            memory,origin = memory_case(alias)
            put(memory,UNIT,self.unit)
            args = (ACTOR,origin,bits(height),bits(0.125),bits(0.75),bits(-2.0))
            expected,calls,x = reference(memory,args,phase=phase,coefficients=sdk_matrix(values))
            angles = (number(0.75*floating(self.unit)),number(0.0*floating(self.unit)),number(-2.0*floating(self.unit)))
            trig = [(target,bits(angle)) for angle in angles for target in (TRIG_A,TRIG_B)]
            wanted_calls = [calls[0],*trig,calls[1]]
            models = []
            for body in (self.words,self.retail):
                model = SdkProjectionOracle(body,memory,args,self.sdk,values,phase).run()
                self.assertEqual((external(model.memory),model.calls,model.f[0]),(expected,wanted_calls,x))
                self.assertEqual(model.trig_calls,6); coverage.update(model.visits&set(self.sdk)); models.append(model)
            self.assertEqual(models[0].events,models[1].events); cases += 1
        self.assertEqual((cases,len(coverage)),(144,123))
        (self.output/'sdk.json').write_text(json.dumps(dict(cases=cases,mapped_words=141,reached_words=123,
            rotation_words=83,coordinate_words=40,trig='bounded finite providers',unit=hex(self.unit)),indent=2)+'\n')

    def test_connected_caller_float_bits_aliases_and_return_one(self):
        cases,coverage = 0,set()
        for mode,height,scale,mutation,phase in itertools.product(range(4),(-0.0,0.125,2.0),
                (-2.0,0.0,0.25),(0,2,8,16,31),(0,8)):
            memory,origin = memory_case(0x17C,mode)
            for axis,value in enumerate((2.0,-3.0,4.0)): put(memory,origin+axis*4,bits(value))
            put(memory,ACTOR+0x170,bits(height)); put(memory,ACTOR+0x174,bits(scale))
            args = (ACTOR,origin,bits(height),bits(scale),read(memory,ANGLES),read(memory,ANGLES+8))
            wanted,calls,x = reference(memory,args,mutation,phase-32)
            models = []
            for caller,body in ((self.caller,self.words),(self.retail_caller,self.retail)):
                connected = {screen.ENTRY+i*4:word for i,word in enumerate(body)}
                model = ProjectionOracle(caller,memory,(ACTOR,origin),mutation,phase,connected,screen.CALLER_ENTRY).run()
                self.assertEqual((external(model.memory),model.calls,model.r[2],model.f[0]),
                                 (wanted,[(screen.ENTRY,*args),*calls],1,x))
                coverage.update(model.visits); models.append(model)
            self.assertEqual(models[0].events,models[1].events); cases += 1
        self.assertEqual(cases,360)
        self.assertEqual(len(coverage&set(range(screen.CALLER_ENTRY,screen.CALLER_ENTRY+64,4))),16)

    def test_compiled_negatives_change_state_calls_or_mapped_accesses(self):
        interleaved = screen.SELECTED.replace('    dx = (*(f32 *)(actor + 0x34) - origin[0]) * scale;\n','').replace(
            '    dy = (*(f32 *)(actor + 0x38) - origin[1]) * scale;\n','').replace(
            '    dz = (*(f32 *)(actor + 0x3C) - origin[2]) * scale;\n','').replace('    f32 dx, dy, dz;\n','')
        for axis,index in zip(('x','y','z'),range(3)):
            interleaved = interleaved.replace('d'+axis+' * 500.0f',
                '(*(f32 *)(actor + 0x%X) - origin[%d]) * scale * 500.0f'%(0x34+index*4,index))
        stale = screen.SELECTED.replace('    f32 matrix[4][4];','    f32 matrix[4][4];\n    f32 sourceX,sourceY,sourceZ;').replace(
            '    func_150A8050(', '    sourceX = origin[0]; sourceY = origin[1]; sourceZ = origin[2];\n    func_150A8050(',1)
        for index,axis in enumerate(('X','Y','Z')): stale = stale.replace('matrix[3][%d] = origin[%d]'%(index,index),'matrix[3][%d] = source%s'%(index,axis))
        reassociated = screen.SELECTED
        for axis,index in zip(('x','y','z'),range(3)):
            reassociated = reassociated.replace('origin[%d]) * scale;'%index,'origin[%d]) * (scale * 500.0f);'%index).replace('d'+axis+' * 500.0f','d'+axis)
        negatives = [('stub','void func_1514182C(u8 *a,f32 *p,f32 h,f32 s,f32 x,f32 z) {}'),
            ('wrong-angle',screen.SELECTED.replace('matrix, angleX, 0.0f, angleZ','matrix, angleZ, 0.0f, angleX')),
            ('wrong-translation',screen.SELECTED.replace('matrix[3][1] = origin[1]','matrix[3][1] = origin[0]')),
            ('integer-height',screen.SELECTED.replace('f32 height','s32 height')),
            ('zero-height',screen.SELECTED.replace('0.0f, height, 0.0f','0.0f, 0.0f, 0.0f')),
            ('wrong-scale',screen.SELECTED.replace(') * scale;',') * 2.0f;')),
            ('wrong-output',screen.SELECTED.replace('*(f32 *)(actor + 0x48) =','*(f32 *)(actor + 0x4C) =')),
            ('stale-origin',stale),('interleaved-origin',interleaved),('reassociated-scale',reassociated)]
        receipts = []
        for name,body in negatives:
            _,words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            differences,cases = 0,0
            for alias,mode,height,scale,mutation in itertools.product((None,0x38,0x40),(1,3),
                    (0.001,0.125,1.001,7.0),(0.1,0.00025,0.3333333432674408,1.5),(0,2,8)):
                memory,origin = memory_case(alias,mode)
                args = (ACTOR,origin,bits(height),bits(scale),bits(0.125),bits(-0.75))
                wanted = reference(memory,args,mutation)
                try:
                    model = ProjectionOracle(words,memory,args,mutation).run()
                    different = (external(model.memory),model.calls)!=wanted[:2]
                except AssertionError as error:
                    self.assertIn(error.args[0][0],('unmapped read','unmapped write','unmapped store'))
                    different = True
                differences += bool(different); cases += 1
            self.assertGreater(differences,0,name)
            receipts.append(dict(name=name,cases=cases,differences=differences))
        (self.output/'negatives.json').write_text(json.dumps(receipts,indent=2)+'\n')

    def test_native_actual_source_full_footprint_aliases_and_typed_caller(self):
        self.fixture = native_fixture()+self.native_source()+'\n'
        self.run_host(r'''
int a,m,h,s,k,call,i;int modes[]={0,1,2,3,8,16,24,27};
float heights[]={-3.0f,-0.0f,0.0f,1.25f,7.0f};
float scales[]={-2.0f,-0.0f,0.0f,0.00025f,0.25f,1.5f};
static u8 wantedActor[sizeof(actorStorage)],wantedOrigin[sizeof(originStorage)],wantedCoef[sizeof(coefficientStorage)];
static u32 wantedLog[64];
if(sizeof(void *)!=4 || sizeof(float)!=4) return 50;
for(a=0;a<8;a++) for(m=0;m<4;m++) for(h=0;h<5;h++) for(s=0;s<6;s++) for(k=0;k<8;k++) {
    initialize(a,m,modes[k],heights[h],scales[s]);reference(actor,origin,heights[h],scales[s],0.125f,-0.75f);
    for(i=0;i<(int)sizeof(actorStorage);i++) wantedActor[i]=actorStorage.bytes[i];
    for(i=0;i<(int)sizeof(originStorage);i++) wantedOrigin[i]=originStorage.bytes[i];
    for(i=0;i<(int)sizeof(coefficientStorage);i++) wantedCoef[i]=coefficientStorage.bytes[i];
    for(i=0;i<64;i++) wantedLog[i]=log[i];
    initialize(a,m,modes[k],heights[h],scales[s]);func_1514182C(actor,origin,heights[h],scales[s],0.125f,-0.75f);
    if(count!=2) return 51;
    for(i=0;i<(int)sizeof(actorStorage);i++) if(wantedActor[i]!=actorStorage.bytes[i]) return 52;
    for(i=0;i<(int)sizeof(originStorage);i++) if(wantedOrigin[i]!=originStorage.bytes[i]) return 53;
    for(i=0;i<(int)sizeof(coefficientStorage);i++) if(wantedCoef[i]!=coefficientStorage.bytes[i]) return 54;
    for(i=0;i<64;i++) if(wantedLog[i]!=log[i]) return 55;
}
for(m=0;m<4;m++) for(h=0;h<5;h++) for(s=0;s<6;s++) for(k=0;k<8;k++) for(call=0;call<2;call++) {
    initialize(8,m,modes[k],heights[h],scales[s]);reference(actor,origin,heights[h],scales[s],0.125f,-0.75f);
    for(i=0;i<(int)sizeof(actorStorage);i++) wantedActor[i]=actorStorage.bytes[i];
    for(i=0;i<64;i++) wantedLog[i]=log[i];
    initialize(8,m,modes[k],heights[h],scales[s]);
    if(call) {if(func_15141928(actor)!=1) return 56;}
    else func_1514182C(actor,origin,heights[h],scales[s],0.125f,-0.75f);
    for(i=0;i<(int)sizeof(actorStorage);i++) if(wantedActor[i]!=actorStorage.bytes[i]) return 57;
    for(i=0;i<64;i++) if(wantedLog[i]!=log[i]) return 58;
}
''')

    def native_source(self):
        owner = (self.root/'conker/src/game_16DC80.c').read_text()
        if screen.SELECTED in owner and screen.CALLER in owner:
            start = owner.index(screen.SELECTED); caller = owner.index(screen.CALLER)
            return owner[start:start+len(screen.SELECTED)]+'\n'+owner[caller:caller+len(screen.CALLER)]
        return screen.SELECTED+'\n'+screen.CALLER

    def test_special_float_guest_and_native_direct_bits_vs_arithmetic_nan_class(self):
        cases = 0
        for field,encoding,alias,mutation in itertools.product(range(10),SPECIAL,(None,0x38,0x40),(0,8)):
            memory,origin = memory_case(alias,3)
            args = [ACTOR,origin,bits(1.25),bits(0.125),bits(0.25),bits(-0.75)]
            if field<3: put(memory,origin+field*4,encoding)
            elif field<7: args[(2,3,4,5)[field-3]] = encoding
            else: put(memory,COEFFICIENTS+(0,5,9)[field-7]*4,encoding)
            wanted,calls,x = reference(memory,args,mutation)
            models = []
            for body in (self.words,self.retail):
                model = ProjectionOracle(body,memory,args,mutation).run()
                equal_arithmetic_nan_memory(self,external(model.memory),wanted)
                self.assertEqual(model.calls,calls)
                if math.isnan(floating(x)):
                    self.assertTrue(math.isnan(floating(model.f[0])))
                else: self.assertEqual(model.f[0],x)
                models.append(model)
            self.assertEqual(models[0].memory,models[1].memory)
            self.assertEqual(models[0].events,models[1].events); cases += 1
        self.assertEqual(cases,720)
        self.fixture = native_fixture()+self.native_source()+r'''
static u32 special[]={0,0x80000000u,1,0x007FFFFFu,0x00800000u,0x7F7FFFFFu,0xFF7FFFFFu,
    0x7F800000u,0xFF800000u,0x7FC00001u,0x7FA00001u,0xFFA12345u};
static f32 specialHeight,specialScale,specialX,specialZ;
static void prepare_special(int field,int encoding,int alias,int mutate) {
    u32 input=special[encoding];int aliases[]={0,2,4},indices[]={0,5,9};
    initialize(aliases[alias],3,mutate,1.25f,0.125f);
    specialHeight=1.25f;specialScale=0.125f;specialX=0.25f;specialZ=-0.75f;
    if(field<3) ((u32 *)origin)[field]=input;
    else if(field==3) specialHeight=value(input);
    else if(field==4) specialScale=value(input);
    else if(field==5) specialX=value(input);
    else if(field==6) specialZ=value(input);
    else ((u32 *)(coefficientStorage.bytes+16))[indices[field-7]]=input;
}
static int is_nan(u32 word) {return (word&0x7F800000u)==0x7F800000u && (word&0x7FFFFFu)!=0;}
'''
        self.run_host(r'''
int f,e,a,m,i,j;static u8 wa[sizeof(actorStorage)],wo[sizeof(originStorage)],wc[sizeof(coefficientStorage)];
static u32 wl[64];int offsets[]={0x34,0x38,0x3C,0x40,0x44,0x48};
for(f=0;f<10;f++) for(e=0;e<12;e++) for(a=0;a<3;a++) for(m=0;m<2;m++) {
    prepare_special(f,e,a,m?8:0);reference(actor,origin,specialHeight,specialScale,specialX,specialZ);
    for(i=0;i<(int)sizeof(actorStorage);i++) wa[i]=actorStorage.bytes[i];
    for(i=0;i<(int)sizeof(originStorage);i++) wo[i]=originStorage.bytes[i];
    for(i=0;i<(int)sizeof(coefficientStorage);i++) wc[i]=coefficientStorage.bytes[i];
    for(i=0;i<64;i++) wl[i]=log[i];
    prepare_special(f,e,a,m?8:0);func_1514182C(actor,origin,specialHeight,specialScale,specialX,specialZ);
    for(j=0;j<6;j++) {
        u32 *expected=(u32 *)(wa+16+offsets[j]),*actual=(u32 *)(actor+offsets[j]);
        if(is_nan(*expected) || is_nan(*actual)) {
            if(!is_nan(*expected) || !is_nan(*actual)) return 60;
            *expected=*actual=0;
        }
    }
    for(i=0;i<(int)sizeof(actorStorage);i++) if(wa[i]!=actorStorage.bytes[i]) return 61;
    for(i=0;i<(int)sizeof(originStorage);i++) if(wo[i]!=originStorage.bytes[i]) return 62;
    for(i=0;i<(int)sizeof(coefficientStorage);i++) if(wc[i]!=coefficientStorage.bytes[i]) return 63;
    for(i=0;i<64;i++) if(wl[i]!=log[i]) return 64;
}
''')
        (self.output/'special.json').write_text(json.dumps(dict(cases=cases,guest_bodies=2,native_cases=720,
            encodings=[hex(v) for v in SPECIAL],nan='arithmetic classification only',direct_bits='exact'),indent=2)+'\n')

    def test_production_direct_source_caller_slots_relocations_and_no_guards(self):
        owner = (self.root/'conker/src/game_16DC80.c').read_text()
        self.assertIn(screen.SELECTED,owner); self.assertIn(screen.CALLER,owner); self.assertIn(screen.PROTOTYPE,owner)
        self.assertNotIn('f32 func_1514182C(',owner)
        functions,_,addresses = load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_1514182C'],screen.ENTRY)
        self.assertEqual(addresses['func_15141928'],screen.CALLER_ENTRY)
        self.assertEqual(functions['func_1514182C'],self.retail)
        self.assertEqual(functions['func_15141928'],self.retail_caller)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream: rows = list(csv.DictReader(stream))
        self.assertEqual(len(rows),10809)
        self.assertFalse([row for row in rows if row['function'] in ('func_1514182C','func_15141928')])
        actual = subprocess.run(['mips-linux-gnu-objdump','-r',str(self.output/'selected.o')],
                                check=True,capture_output=True,text=True).stdout
        self.assertIn('0000002c R_MIPS_26         func_150A8050',actual)
        self.assertIn('00000074 R_MIPS_26         func_150A7960',actual)
        caller = subprocess.run(['mips-linux-gnu-objdump','-r',str(self.output/'caller.o')],
                                check=True,capture_output=True,text=True).stdout
        self.assertIn('00000024 R_MIPS_26         func_1514182C',caller)

    @classmethod
    def tearDownClass(cls):
        report = dict(cases=cls.cases,bodies=2,covered_words=[len(v) for v in cls.coverage],
                      sha256=hashlib.sha256(struct.pack('>63I',*cls.words)).hexdigest())
        (cls.output/'behavior.json').write_text(json.dumps(report,indent=2)+'\n'); print('position projection:',report)


def native_fixture():
    return r'''
typedef unsigned char u8;typedef unsigned int u32;typedef int s32;typedef float f32;
typedef union {u32 align;u8 bytes[0x240];} ActorStorage;
typedef union {u32 align;u8 bytes[80];} OriginStorage;
typedef union {u32 align;u8 bytes[96];} CoefficientStorage;
static ActorStorage actorStorage;static OriginStorage originStorage;static CoefficientStorage coefficientStorage;
static u8 *actor=actorStorage.bytes+16;static f32 *origin;
static f32 angles[3];static u32 log[64];static int count,mutation;
static u32 word(f32 f) {union {f32 f;u32 u;} v;v.f=f;return v.u;}
static f32 value(u32 u) {union {f32 f;u32 u;} v;v.u=u;return v.f;}
static f32 get(const void *p) {return value(*(const u32 *)p);}
static void set(void *p,f32 f) {*(u32 *)p=word(f);}
static f32 rounded(f32 f) {volatile f32 v=f;return v;}
static void actions(int stage,u8 *a,f32 *o) {
    if(stage==0) {
        if(mutation&1) {set(a+0x34,3.0f);set(a+0x38,-4.0f);set(a+0x3C,5.0f);}
        if(mutation&2) {set(o,-11.0f);set(o+1,7.0f);set(o+2,0.125f);}
    } else {
        if(mutation&8) {set(o,9.0f);set(o+1,-3.5f);set(o+2,1.25f);}
        if(mutation&16) {set(a+0x34,0.125f);set(a+0x38,-2.0f);set(a+0x3C,7.0f);}
    }
}
void func_150A8050(f32 m[4][4],f32 x,f32 y,f32 z) {
    int i;log[0]=word(x);log[1]=word(y);log[2]=word(z);count++;
    for(i=0;i<16;i++) ((u32 *)m)[i]=((u32 *)(coefficientStorage.bytes+16))[i];
    actions(0,actor,origin);
}
void func_150A7960(f32 *m,f32 x,f32 y,f32 z,f32 *ox,f32 *oy,f32 *oz) {
    int i;f32 result[3];f32 *outputs[3]={ox,oy,oz};
    log[3]=word(x);log[4]=word(y);log[5]=word(z);
    log[6]=(u32)ox;log[7]=(u32)oy;log[8]=(u32)oz;
    for(i=0;i<16;i++) log[9+i]=word(m[i]);
    for(i=0;i<3;i++) {
        f32 first=rounded(rounded(m[i]*x)+rounded(m[i+4]*y));
        f32 second=rounded(rounded(m[i+8]*z)+m[i+12]);
        result[i]=rounded(first+second);
    }
    for(i=0;i<3;i++) set(outputs[i],result[i]);
    count++;actions(1,actor,origin);
}
static void initialize(int alias,int mode,int mutate,f32 height,f32 scale) {
    int i;static int offsets[]={-1,0x34,0x38,0x3C,0x40,0x44,0x48,0x4C,0x17C};
    mutation=mutate;count=0;for(i=0;i<64;i++) log[i]=0;
    for(i=0;i<(int)sizeof(actorStorage);i++) actorStorage.bytes[i]=(u8)(i*13+7);
    for(i=0;i<(int)sizeof(originStorage);i++) originStorage.bytes[i]=(u8)(i*13+7);
    for(i=0;i<(int)sizeof(coefficientStorage);i++) coefficientStorage.bytes[i]=(u8)(i*13+7);
    for(i=0;i<20;i++) set(actor+0x30+i*4,(f32)(i+1));
    for(i=0;i<16;i++) set(coefficientStorage.bytes+16+i*4,(i==0||i==5||i==10||i==15)?1.0f:0.0f);
    if(mode==1) {set(coefficientStorage.bytes+20,2);set(coefficientStorage.bytes+32,-0.5f);
        set(coefficientStorage.bytes+36,0.25f);set(coefficientStorage.bytes+52,-3);}
    if(mode==2) {set(coefficientStorage.bytes+16,-1);set(coefficientStorage.bytes+36,-2);
        set(coefficientStorage.bytes+56,0);set(coefficientStorage.bytes+40,1.5f);}
    if(mode==3) {set(coefficientStorage.bytes+32,0.125f);set(coefficientStorage.bytes+36,3);
        set(coefficientStorage.bytes+40,-0.25f);set(coefficientStorage.bytes+16,2);set(coefficientStorage.bytes+52,-0.75f);}
    origin=(f32 *)(alias==0?originStorage.bytes+16:actor+offsets[alias]);
    if(alias==0) {set(origin,10);set(origin+1,20);set(origin+2,30);}
    if(alias==8) {set(origin,2);set(origin+1,-3);set(origin+2,4);}
    set(actor+0x170,height);set(actor+0x174,scale);*(f32 **)(actor+0x178)=angles;
    angles[0]=0.125f;angles[1]=1;angles[2]=-0.75f;
}
static void reference(u8 *a,f32 *o,f32 height,f32 scale,f32 ax,f32 az) {
    f32 matrix[4][4];f32 positions[3],sources[3],products[3];int i;
    func_150A8050(matrix,ax,0.0f,az);
    for(i=0;i<3;i++) ((u32 *)matrix)[12+i]=word(o[i]);
    func_150A7960((f32 *)matrix,0.0f,height,0.0f,(f32 *)(a+0x34),(f32 *)(a+0x38),(f32 *)(a+0x3C));
    for(i=0;i<3;i++) {positions[i]=get(a+0x34+i*4);sources[i]=o[i];}
    for(i=0;i<3;i++) products[i]=rounded(rounded(positions[i]-sources[i])*scale);
    for(i=0;i<3;i++) set(a+0x40+i*4,rounded(positions[i]+rounded(products[i]*500.0f)));
}
'''


if __name__=='__main__': unittest.main()
