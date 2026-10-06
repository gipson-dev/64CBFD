"""Payload copying, live counter/selector lifetimes and the real constructor."""

import csv
import itertools
import json
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_payload_copy_wrapper_candidates as screen
from tools.match_progress import load_elf_functions
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly
from pad_generated_object import parse_object
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_source_effect_constructor_match as constructor
from tools.tests import test_game_random_curve_record as native

ALLOC, COPY = screen.WRAPPER_ENTRY, screen.SYMBOLS['memcpy']
SOURCE, DESCRIPTOR, ACTOR, COUNTER = 0x20000, 0x22000, 0x21000, 0x800DC9F0
HI = 'R_MIPS_HI16:D_800DC9F0'
GUARDS = (
    (0x06C,0x1040000C,0x1040000D,'-','-'),
    (0x08C,0x8FA3003C,0x83AD005F,'-','-'),
    (0x090,0xAC800044,0x8FA3003C,'-','-'),
    (0x094,0x83AD005F,0xAC800044,'-','-'),
    (0x098,0x10000003,0xA08D0059,'-','-'),
    (0x09C,0xA08D0059,0x10000003,'-','-'),
    (0x0A0,0x10000008,0x3C020000,'-',HI),
    (0x0A4,0x00001025,0x10000007,'-','-'),
    (0x0A8,0x10600005,0x00001025,'-','-'),
    (0x0AC,0x3C020000,0x10600004,HI,'-'))


def read(memory, address, size=4):
    return int.from_bytes(bytes(memory[address+i] for i in range(size)), 'big')


def external(memory):
    return {a:v for a,v in memory.items() if not STACK-0x600<=a<STACK+0x100}


def memory_case(alias=0, flags=0, counter=0xFFFFFFFE):
    source, descriptor, actor = SOURCE, DESCRIPTOR, ACTOR
    if alias == 1: source = descriptor
    if alias == 2: descriptor = actor+0x110
    if alias == 3: actor = COUNTER-0x154
    if alias == 4: source = COUNTER
    if alias == 5: source = actor
    memory = {STACK+i:0xA5 for i in range(-0x600,0x100)}
    for base,length in ((source-16,288),(descriptor-16,128),(actor-16,0x230),(COUNTER-16,288)):
        memory.update({base+i:(i*13+7)&255 for i in range(length)})
    put(memory,descriptor+0x40,flags); put(memory,COUNTER,counter)
    return memory,source,descriptor,actor


def actions(memory, stage, source, descriptor, mutation, phase):
    if not mutation: return
    if stage == 'allocate':
        put(memory,descriptor+1,0xE7,1); put(memory,descriptor+0x40,0xDEADBEEF)
        put(memory,source,0xB3,1); put(memory,COUNTER,0x80000000)
    else:
        put(memory,COUNTER,0xFFFFFFFF); put(memory,STACK+phase+0x1C,0x876543FE)


def reference(memory, args, actor, fail=False, mutation=False, phase=0):
    memory = dict(memory)
    source,size,desc,kind,mode,first,variant,selector,channel,context = args
    put(memory,desc+1,3,1); put(memory,desc+0x40,read(memory,desc+0x40)|0x40400000)
    calls = [(ALLOC,bytes(memory[desc+i] for i in range(88)),kind&255,mode&255,first&255,
              1,variant&255,size&0xFFFFFFFF,channel&255,context&0xFFFFFFFF)]
    actions(memory,'allocate',source,desc,mutation,phase)
    if fail: return external(memory),calls,0
    copied = bytes(memory[source+i] for i in range(size))
    calls.append((COPY,actor+0x110,copied,size))
    for i,value in enumerate(copied): put(memory,actor+0x110+i,value,1)
    actions(memory,'copy',source,desc,mutation,phase)
    put(memory,actor+0x154,0); put(memory,actor+0x169,0xFE if mutation else selector&255,1)
    put(memory,COUNTER,(read(memory,COUNTER)+1)&0xFFFFFFFF)
    return external(memory),calls,actor


class SignedByteOracle(TriangleOracle):
    def get(self, address, size):
        assert all(address+i in self.memory for i in range(size)), ('unmapped read',address,size)
        return super().get(address,size)

    def put(self, address, value, size):
        if self.recording:
            assert all(address+i in self.memory for i in range(size)), ('unmapped write',address,size)
        super().put(address,value,size)

    def execute(self, word):
        if word>>26 == 32:
            rs,rt,imm = word>>21&31,word>>16&31,word&65535
            if imm&0x8000: imm -= 0x10000
            value = self.get((self.r[rs]+imm)&0xFFFFFFFF,1)
            self.r[rt] = (value if value<128 else value-256)&0xFFFFFFFF; self.r[0] = 0
        else: super().execute(word)


class PayloadOracle(SignedByteOracle):
    def __init__(self, words, memory, args, actor, fail=False, mutation=False, phase=0, copy_actions=()):
        super().__init__(words,memory,entry=screen.ENTRY,arguments=args,phase=phase)
        self.actor,self.fail,self.mutation,self.phase = actor,fail,mutation,phase
        self.source,self.descriptor,self.copy_actions = args[0],args[2],copy_actions

    def record_call(self, target):
        if target == ALLOC:
            args = self.arguments(9); desc = args[0]
            call = (target,bytes(self.memory[desc+i] for i in range(88)),*args[1:])
        else:
            assert target == COPY
            destination,source,size = self.r[4:7]
            call = (target,destination,bytes(self.memory[source+i] for i in range(size)),size)
        self.calls.append(call); self.events.append(('CALL',target,call[1:]))

    def hook(self, target):
        if target == ALLOC:
            stage,result = 'allocate',0 if self.fail else self.actor
        else:
            assert target == COPY
            destination,source,size = self.r[4:7]
            copied = bytes(self.memory[source+i] for i in range(size))
            for i,value in enumerate(copied): self.put(destination+i,value,1)
            stage,result = 'copy',0xBAD00000
            for address,value,width in self.copy_actions: self.put(address,value,width)
        actions(self.memory,stage,self.source,self.descriptor,self.mutation,self.phase)
        for register in (1,2,3,*range(4,16),24,25): self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]; self.r[2] = result


class ConnectedOracle(constructor.ConstructorOracle, SignedByteOracle):
    def __init__(self, words, memory, args, fail, mutation, phase, connected):
        super().__init__(words,memory,args,fail,actions=connected_actions(mutation),connected=connected,
                         entry=screen.ENTRY,phase=phase)
        self.payload_mutation,self.phase = mutation,phase

    def record_call(self, target):
        if target == ALLOC:
            args = self.arguments(9); desc = args[0]
            call = (target,bytes(self.memory[desc+i] for i in range(88)),*args[1:])
            self.calls.append(call); self.events.append(('CALL',target,call[1:]))
        elif target == COPY and self.r[4] == ACTOR+0x110:
            destination,source,size = self.r[4:7]
            call = (target,destination,bytes(self.memory[source+i] for i in range(size)),size)
            self.calls.append(call); self.events.append(('CALL',target,call[1:]))
        else: super().record_call(target)

    def hook(self, target):
        if target == COPY and self.r[4] == ACTOR+0x110:
            destination,source,size = self.r[4:7]
            for i,value in enumerate(bytes(self.memory[source+i] for i in range(size))): self.put(destination+i,value,1)
            if self.payload_mutation: self.put(COUNTER,0xFFFFFFFF,4)
            for register in (1,2,3,*range(4,16),24,25): self.r[register] = 0xA5000000+register
            self.f[:20] = [0xA5000000+i for i in range(20)]; self.r[2] = 0xBAD00000
        else: super().hook(target)


def connected_actions(mutation):
    result = constructor.actions_for(mutation)
    if mutation: result['allocate'] += ((COUNTER,0x80000000,4),)
    return result


def connected_reference(memory, args, fail, mutation):
    source,size,desc,kind,mode,first,variant,selector,channel,context = args
    memory = dict(memory)
    put(memory,desc+1,3,1); put(memory,desc+0x40,read(memory,desc+0x40)|0x40400000)
    description = bytes(memory[desc+i] for i in range(88))
    inner = (desc,constructor.packet.TABLE,kind&255,mode&255,first&255,1,variant&255,0,0,size,channel&255,context)
    wanted,calls,result = constructor.reference(memory,inner,fail,actions=connected_actions(mutation))
    prefix = [(ALLOC,description,*inner[2:7],size,channel&255,context&0xFFFFFFFF),
              (constructor.screen.ENTRY,description,*inner[1:])]
    if result:
        copied = bytes(wanted[source+i] for i in range(size)); calls.append((COPY,ACTOR+0x110,copied,size))
        for i,value in enumerate(copied): put(wanted,ACTOR+0x110+i,value,1)
        if mutation: put(wanted,COUNTER,0xFFFFFFFF)
        put(wanted,ACTOR+0x154,0); put(wanted,ACTOR+0x169,selector&255,1)
        put(wanted,COUNTER,(read(wanted,COUNTER)+1)&0xFFFFFFFF)
    return wanted,[*prefix,*calls],result


class GamePayloadCopyWrapperMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-payload-copy-wrapper-test'; cls.output.mkdir(exist_ok=True)
        cls.record,cls.words = screen.compile_candidate(cls.root,cls.output,'selected')
        cls.wrapper_record,cls.wrapper = screen.compile_candidate(cls.root,cls.output,'wrapper',screen.WRAPPER,
            declarations=screen.WRAPPER_DECLARATIONS,wrapper=True)
        cls.ctor_record,cls.ctor = constructor.screen.compile_candidate(cls.root,cls.output,'constructor')
        rom = (cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>53I',rom,screen.ROM))
        cls.wrapper_retail = list(struct.unpack_from('>28I',rom,screen.WRAPPER_ROM))
        cls.directory = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)

    def test_complete_closed_schedule_branches_delay_slots_and_relocation(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],self.record['diagnostics']),
                         (53,64,10,''))
        movement = {35:36,36:37,37:35,38:39,39:38,40:41,41:42,42:43,43:40}
        normalized = list(self.words)
        for old,word in enumerate(self.words):
            new = movement.get(old,old)
            if word>>26 in (4,5):
                offset = word&65535; offset = offset if offset<32768 else offset-65536
                target = old+1+offset
                word = word&0xFFFF0000 | ((movement.get(target,target)-new-1)&65535)
            normalized[new] = word
        self.assertEqual(normalized,self.retail)
        self.assertEqual(sum(a==b for a,b in zip(self.words,self.retail)),43)
        text,functions,relocations = parse_object(self.output/'selected.o')
        start = functions['func_151407D0']['value']
        self.assertEqual(relocations[start+0xAC],[('R_MIPS_HI16','D_800DC9F0')])
        self.assertEqual(relocations[start+0xB0],[('R_MIPS_LO16','D_800DC9F0')])
        with (self.output/'guards.csv').open('w',newline='') as stream:
            writer = csv.writer(stream)
            writer.writerow(('filename','function','offset','expected','replacement','expected_relocations',
                             'replacement_relocations','note','insert_after','insert_after_relocations','omit'))
            for offset,expected,replacement,old,new in GUARDS:
                self.assertEqual(struct.unpack_from('>I',text,start+offset)[0],expected)
                writer.writerow(('game_16DC80','func_151407D0',hex(offset),hex(expected),hex(replacement),old,new,
                                 'closed success schedule','','','false'))
        layout = self.output/'layout.csv'
        layout.write_text('version,section,filename,function,address,end\nus,game,game_16DC80,func_151407D0,0x151407D0,0x151408A4\n')
        assembly = emit_padded_assembly(self.output/'selected.o',layout,'game_16DC80',word_patches_path=self.output/'guards.csv')
        (self.output/'padded.s').write_text(assembly)
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(self.output/'padded.o'),
                        str(self.output/'padded.s')],check=True,capture_output=True)
        _,padded_functions,padded_relocations = parse_object(self.output/'padded.o')
        start = padded_functions['func_151407D0']['value']
        self.assertEqual(padded_functions['func_151407D0']['size'],212)
        self.assertNotIn(start+0xAC,padded_relocations)
        self.assertEqual(padded_relocations[start+0xA0],[('R_MIPS_HI16','D_800DC9F0')])
        self.assertEqual(padded_relocations[start+0xB0],[('R_MIPS_LO16','D_800DC9F0')])
        subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'func_151407D0.ld'),
            '-e','func_151407D0',*['--defsym=%s=0x%X'%item for item in screen.SYMBOLS.items()],
            '-o',str(self.output/'padded.elf'),str(self.output/'padded.o')],check=True,capture_output=True)
        linked = load_elf_functions(str(self.output/'padded.elf'),'mips-linux-gnu-objdump')[0]['func_151407D0']
        self.assertEqual(linked[:53],self.retail); self.assertFalse(any(linked[53:]))

    def test_guest_full_storage_aliases_failure_callbacks_and_all_words(self):
        cases,coverage = 0,[set(),set()]
        for size,flags,alias,fail,mutation,phase,selector in itertools.product(
                (0,1,4,16,64,96,128),(0,0x80000000,0x02000000,0xFFFFFFFF),range(6),
                (False,True),(False,True),(0,8),(0,127,128,255)):
            memory,source,descriptor,actor = memory_case(alias,flags)
            args = (source,size,descriptor,0x12340000|selector,0xBEEF0000|(selector^255),
                    0xA5000000|((selector+7)&255),0x87650000|((selector*13)&255),
                    0x56780000|selector,0xDEAD0000|((selector*17)&255),0x80000000)
            wanted = reference(memory,args,actor,fail,mutation,phase)
            traces = []
            for index,body in enumerate((self.words,self.retail)):
                model = PayloadOracle(body,memory,args,actor,fail,mutation,phase).run()
                self.assertEqual((external(model.memory),model.calls,model.r[2]),wanted,(cases,index))
                coverage[index].update(model.visits)
                traces.append([event for event in model.events if not STACK-0x600<=event[1]<STACK+0x100])
            self.assertEqual(*traces); cases += 1
        self.assertEqual((cases,*map(len,coverage)),(5376,53,53))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases,bodies=2,covered_words=53),indent=2)+'\n')

    def test_all_selector_byte_pairs_and_opaque_failure_size_boundaries(self):
        cases = 0
        for kind,mode in itertools.product(range(256),range(256)):
            memory,source,descriptor,actor = memory_case()
            byte = (kind*17+mode)&255
            args = (source,4,descriptor,0x12340000|kind,0x56780000|mode,
                    0xA5000000|((kind+mode)&255),0xBEEF0000|((kind^mode)&255),
                    0xFACE0000|byte,0xDEAD0000|((kind-mode)&255),0xFFFFFFFF)
            wanted = reference(memory,args,actor)
            for body in (self.words,self.retail):
                model = PayloadOracle(body,memory,args,actor).run()
                self.assertEqual((external(model.memory),model.calls,model.r[2]),wanted)
            cases += 1
        self.assertEqual(cases,65536)
        for size,phase in itertools.product((0,0xFFFFFFFF,0x80000000,0x7FFFFEEF,0x7FFFFFFF),(0,8)):
            memory,source,descriptor,actor = memory_case()
            args = (source,size,descriptor,255,255,255,255,255,255,0x80000000)
            wanted = reference(memory,args,actor,fail=True)
            for body in (self.words,self.retail):
                model = PayloadOracle(body,memory,args,actor,fail=True,phase=phase).run()
                self.assertEqual((external(model.memory),model.calls,model.r[2]),wanted)

    def test_post_copy_saved_result_selector_and_live_counter_join(self):
        for result,selector,counter,phase in itertools.product((0,ACTOR,ACTOR+16),(0,127,128,255),
                                                               (0,0x7FFFFFFF,0xFFFFFFFF),(0,8)):
            memory,source,descriptor,actor = memory_case(counter=counter)
            args = (source,4,descriptor,39,0,0,0,7,255,1)
            writes = ((STACK+phase-4,result,4),(STACK+phase+0x1C,selector,4),(COUNTER,counter,4))
            wanted,calls,_ = reference(memory,args,actor)
            put(wanted,actor+0x169,selector,1); put(wanted,COUNTER,(counter+(result!=0))&0xFFFFFFFF)
            traces = []
            for body in (self.words,self.retail):
                model = PayloadOracle(body,memory,args,actor,phase=phase,copy_actions=writes).run()
                self.assertEqual((external(model.memory),model.calls,model.r[2]),(wanted,calls,result))
                traces.append([e for e in model.events if not STACK-0x600<=e[1]<STACK+0x100])
            self.assertEqual(*traces)

    def test_forty_compiler_and_pointer_return_controls(self):
        expected = {'success-join':((53,64,10),(54,64,31),(60,56,59),(60,56,60)),
            'structured':((54,64,19),(54,64,31),(60,56,59),(60,56,60)),
            'early-null':((53,64,17),(53,64,29),(60,56,59),(60,56,60)),
            'capture-selector':((53,64,12),(54,64,33),(62,64,56),(62,64,61)),
            'typed-payload':((53,64,10),(54,64,31),(60,56,59),(60,56,60)),
            'volatile-counter':((53,64,10),(54,64,31),(60,56,59),(60,56,60))}
        for name,body,declarations in screen.candidates():
            for index,profile in enumerate(screen.PROFILES):
                record,_ = screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile,declarations)
                self.assertEqual((record['body_words'],record['frame'],record['differences']),expected[name][index],(name,profile))
                self.assertEqual(record['diagnostics'],'')
        for name,body in screen.wrapper_candidates():
            for index,profile in enumerate(screen.PROFILES):
                record,words = screen.compile_candidate(self.root,self.output,'wrapper-'+name+'-'+profile,body,profile,
                                                        screen.WRAPPER_DECLARATIONS,True)
                self.assertEqual((record['body_words'],record['frame'],record['differences']),
                                 ((28,56,0),(28,56,13),(30,56,29),(30,56,29))[index])
                self.assertEqual(record['diagnostics'],'')
                if profile == 'o2g3': self.assertEqual(words,self.wrapper_retail)

    def test_actual_wrapper_constructor_chain_and_source_aliases(self):
        self.assertEqual(self.wrapper,self.wrapper_retail)
        self.assertEqual(self.ctor,list(struct.unpack_from('>114I',
            (self.root/'conker/conker.us.bin').read_bytes(),constructor.screen.ROM)))
        connected = {entry+i*4:word for entry,body in ((ALLOC,self.wrapper),(constructor.screen.ENTRY,self.ctor))
                     for i,word in enumerate(body)}
        cases = 0
        for flags,source,size,fail,mutation,phase,selector in itertools.product(
                (0,0x80000000,0x02000000,0x82800000),(SOURCE,DESCRIPTOR,ACTOR),
                (0,4,64,88,128),(False,True),(False,True),(0,8),(0,128,255)):
            memory = constructor.memory_case(flags)
            for i in range(288): memory.setdefault(DESCRIPTOR-16+i,(i*13+7)&255)
            for base,length in ((SOURCE,256),(COUNTER-16,36)):
                memory.update({base+i:(i*13+7)&255 for i in range(length)})
            put(memory,COUNTER,0xFFFFFFFE)
            args = (source,size,DESCRIPTOR,39,128,255,206,selector,255,0x80000000)
            wanted = connected_reference(memory,args,fail,mutation)
            traces = []
            for body in (self.words,self.retail):
                model = ConnectedOracle(body,memory,args,fail,mutation,phase,connected).run()
                self.assertEqual((external(model.memory),model.calls,model.r[2]),wanted,(cases,source,size))
                traces.append([e for e in model.events if e[0]=='CALL' or not STACK-0x600<=e[1]<STACK+0x100])
            self.assertEqual(*traces); cases += 1
        self.assertEqual(cases,1440)

    def test_ten_compiled_negatives_change_storage_calls_or_return(self):
        stub = '''u8 *func_151407D0(void *s,s32 n,u8 *d,u8 k,u8 m,u8 f,u8 v,s8 b,u8 h,s32 c) {return NULL;}'''
        early = screen.SELECTED.replace('        memcpy(payload, source, size);',
            '        *(u32 *)&D_800DC9F0 += 1;\n        memcpy(payload, source, size);').replace(
            '    if (result != NULL) {\n        *(u32 *)&D_800DC9F0 += 1;\n    }\n','')
        negatives = [('stub',stub),('descriptor-byte',screen.SELECTED.replace('descriptor[1] = 3','descriptor[1] = 2')),
            ('flags',screen.SELECTED.replace('0x40400000','0x40000000')),
            ('setup',screen.SELECTED.replace('first, 1, variant','first, 0, variant')),
            ('payload-offset',screen.SELECTED.replace('result + 0x110','result + 0x114')),
            ('copy-size',screen.SELECTED.replace('memcpy(payload, source, size)','memcpy(payload, source, size - 1)')),
            ('zero-offset',screen.SELECTED.replace('payload + 0x44','payload + 0x40')),
            ('selector-offset',screen.SELECTED.replace('payload[0x59]','payload[0x58]')),
            ('early-counter',early),('payload-return',screen.SELECTED.replace('return result','return result + 0x110'))]
        for name,body in negatives:
            _,words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            memory,source,descriptor,actor = memory_case()
            args = (source,64,descriptor,39,128,255,206,0xFF,255,0x80000000)
            wanted = reference(memory,args,actor,mutation=True)
            model = PayloadOracle(words,memory,args,actor,mutation=True).run()
            self.assertNotEqual((external(model.memory),model.calls,model.r[2]),wanted,name)

    def test_native_actual_constructor_copy_whole_footprint_and_byte_pairs(self):
        self.fixture = native_fixture()+constructor.screen.SELECTED+'\n'+screen.WRAPPER+'\n'+screen.SELECTED+'\n'
        self.run_host(r'''
static s32 sizes[]={0,1,4,16,64,88,96,128};
u32 a,b,alias,n,f,m,cases=0;u8 *result;
if(sizeof(void *)!=4 || sizeof(s8)!=1) return 30;
for(a=0;a<8;a++) for(alias=0;alias<5;alias++) for(n=0;n<8;n++) for(f=0;f<2;f++) for(m=0;m<2;m++) {
    prepare(f,m,alias,sizes[n],a*37,a*43,a*17,a*19,a*29,a*31);
    result=func_151407D0(payloadInput,payloadSize,descriptor,expectedKind,expectedMode,expectedFirst,
                         expectedVariant,payloadSelector,expectedChannel,expectedContext);
    if(result!=(f?NULL:actor) || verify_payload()) return 31;
    cases++;
}
if(cases!=1280) return 32;
for(a=0;a<256;a++) for(b=0;b<256;b++) for(f=0;f<2;f++) {
    prepare(f,(a^b)&1,(a+b)%5,sizes[(a+b)%8],a,b,a+b,a^b,a*17+b,a-b);
    result=func_151407D0(payloadInput,payloadSize,descriptor,expectedKind,expectedMode,expectedFirst,
                         expectedVariant,payloadSelector,expectedChannel,expectedContext);
    if(result!=(f?NULL:actor) || verify_payload()) return 33;
}
''')

    def test_production_body_abi_complete_slot_and_exact_guards(self):
        source = (self.root/'conker/src/game_16DC80.c').read_text()
        self.assertIn(screen.SELECTED,source)
        self.assertIn(screen.WRAPPER,(self.root/'conker/src/game_169510.c').read_text())
        self.assertIn('void *func_1513D524(void *descriptor, u8 kind, u8 mode, u8 first, u8 setup,',
                      (self.root/'conker/include/functions.h').read_text())
        production = load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        self.assertEqual(production['func_151407D0'],self.retail)
        self.assertEqual(production['func_1513D524'],self.wrapper_retail)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream: rows = list(csv.DictReader(stream))
        guards = [row for row in rows if row['function']=='func_151407D0']
        self.assertEqual((len(rows),len(guards)),(10738,10))
        for row,(offset,expected,replacement,old,new) in zip(guards,GUARDS):
            self.assertEqual(row['filename'],'game_16DC80')
            self.assertEqual(tuple(int(row[k],16) for k in ('offset','expected','replacement')),(offset,expected,replacement))
            self.assertEqual((row['expected_relocations'],row['replacement_relocations']),(old,new))
            self.assertEqual((row['insert_after'],row['insert_after_relocations'],row['omit']),('','','false'))
        self.assertFalse([row for row in rows if row['function']=='func_1513D524'])


def native_fixture():
    fixture = constructor.native_fixture().replace('typedef unsigned char u8;', 'typedef signed char s8;typedef unsigned char u8;')
    fixture = fixture.replace('static Source1CBE20 source;','')
    declarations = r'''
static union {u32 align;u8 bytes[160];} counterStorage;
static u8 counterExpected[160],payloadBytes[160],payloadBefore[160];
static u8 *payloadInput;static s32 payloadSize;static s8 payloadSelector;
static u32 *counterPointer;static u32 expectedCounter;static int payloadAlias,outerCopies;
#define D_800DC9F0 (*(s32 *)counterPointer)
'''
    fixture = fixture.replace('static u32 expectedFlags;', declarations+'\nstatic u32 expectedFlags;')
    fixture = fixture.replace('    return fail?NULL:actor;',
        '    if(mutation) D_800DC9F0=(s32)0x80000000;\n    return fail?NULL:actor;')
    start = fixture.index('void *memcpy('); end = fixture.index('\nvoid bzero(',start)
    fixture = fixture[:start]+r'''
void *memcpy(void *out,const void *in,u32 length) {
    if(out==actor+0x18) {
        if(stage++!=1 || length!=88 || in!=descriptor) error=2;
        copy_bytes(copied,in,88);copy_bytes(out,in,length);return out;
    }
    if(out!=actor+0x110 || in!=payloadInput || length!=(u32)payloadSize || fail || stage!=5 || outerCopies++) error=3;
    copy_bytes(out,in,length);if(mutation) D_800DC9F0=-1;return NULL;
}
'''+fixture[end:]
    fixture = fixture.replace('static int verify(void)', 'static int verify_constructor(void)')
    fixture = fixture.replace('        if(connected) {if(published!=1) return 4;store(e+0x110,(u32)&source);}',r'''
        for(i=0;i<88;i++) if(copied[i]!=descriptorBefore[16+i]) return 8;
        if(payloadAlias==1) copy_bytes(e+0x110,descriptorBefore+16,payloadSize);
        else if(payloadAlias==2) copy_bytes(e+0x110,e,payloadSize);
        else if(payloadAlias==4) {
            store(counterExpected+16,mutation?0x80000000u:0xFFFFFFFEu);
            copy_bytes(e+0x110,counterExpected+16,payloadSize);
        } else copy_bytes(e+0x110,payloadBefore,payloadSize);
        store(e+0x154,0);e[0x169]=(u8)payloadSelector;
        if(payloadAlias==3) store(e+0x154,1);
''')
    fixture += r'''
static void prepare(int failure,int mutate,int alias,s32 length,u8 kind,u8 mode,u8 first,u8 variant,u8 selector,u8 channel) {
    int i;initialize(failure,mutate,0);payloadAlias=alias;payloadSize=length;payloadSelector=(s8)selector;outerCopies=0;
    for(i=0;i<160;i++) {payloadBytes[i]=(u8)(i*11+7);counterStorage.bytes[i]=(u8)(i*13+7);}
    counterPointer=(u32 *)(alias==3?actor+0x154:counterStorage.bytes+16);
    D_800DC9F0=-2;copy_bytes(expected,storage.bytes,0x230);copy_bytes(counterExpected,counterStorage.bytes,160);
    copy_bytes(payloadBefore,payloadBytes,160);
    payloadInput=alias==1?descriptor:alias==2?actor:alias==4?counterStorage.bytes+16:payloadBytes;
    expectedKind=kind;expectedMode=mode;expectedFirst=first;expectedSetup=1;expectedVariant=variant;expectedChannel=channel;
    expectedResource=expectedExtra=0;expectedPayload=length;expectedContext=(s32)0x87654321;
    expectedTable=(s32)&D_800A4AA0;expectedFlags=0x045C0081|((kind&1)?0x800000:0)|((kind&2)?0x2000000:0)|((kind&4)?0x80000000:0);
    store(descriptor+0x40,expectedFlags);expectedFlags|=0x40400000;
    descriptorBefore[17]=3;
    expectedCounter=failure?(mutate?0x80000000u:0xFFFFFFFEu):alias==3?1:mutate?0:0xFFFFFFFFu;
    if(failure && alias==3) store(expected+16+0x154,expectedCounter);
}
static int verify_payload(void) {
    int i,result=verify_constructor();if(result) return result;
    if(outerCopies!=(fail?0:1) || (u32)D_800DC9F0!=expectedCounter) return 9;
    if(payloadAlias!=3) store(counterExpected+16,expectedCounter);
    for(i=0;i<160;i++) if(counterStorage.bytes[i]!=counterExpected[i] || payloadBytes[i]!=payloadBefore[i]) return 10;
    return 0;
}
'''
    return fixture


if __name__ == '__main__':
    unittest.main()
