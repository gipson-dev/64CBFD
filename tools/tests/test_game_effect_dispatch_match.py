"""Live callback/list dispatch, closed scheduling and private cursor access."""

import csv
import itertools
import hashlib
import json
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_effect_dispatch_candidates as screen
from tools.match_progress import load_elf_functions
from tools.pad_generated_object import ELF_HEADER, SECTION_HEADER, read_c_string
from tools.tests.test_game_payload_copy_wrapper_match import SignedByteOracle, external, read
from tools.tests.test_game_actor_triangle_transform_match import put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pad_c_object import emit_padded_assembly
from pad_generated_object import parse_object

ACTOR, NODES, RECORDS = 0x21000, 0x25000, 0x26000
CLASSIFY, MASK, CATEGORY, POSITIVE, SEARCH = (screen.SYMBOLS[name] for name in
    ('func_15141C0C', 'func_1510F8CC', 'func_15141CC0', 'func_15141E38', 'func_1514ECE0'))
TABLE_A, TABLE_B, GATE, WORLD = 0x8008A084, 0x8008A0B4, 0x800BE616, 0x800BE9F0
CLASS_CALLBACK, EFFECT, ALT_EFFECT = 0x1A100000, 0x1A200000, 0x1A200100
ALT_CLASS = 0x1A100100
OFFSETS = (0x50,0x54,0x84,0x88,0x8C,0x90,0x94,0x9C,0xA4,0xA8,0xBC,0xC4,0xC8,0xCC,
           0xE4,0xE8,0xEC,0xF0,0xF4,0xF8,0x11C,0x13C,0x158,0x160,0x168)
PERMUTATION = {0xE4:0xF0,0xE8:0xEC,0xEC:0xE4,0xF0:0xE8,0xF4:0xF8,0xF8:0xF4}


def signed(value):
    return value if value < 0x80000000 else value - 0x100000000


def normalize(raw):
    assert len(raw) == 100
    result = list(raw)
    # The category lifetime is over; exchange only the cursor/table register phase.
    for offset in range(0x90,0x174,4):
        word = raw[offset//4]
        for shift in ((21,16,11) if word>>26 == 0 else (21,16)):
            reg = word>>shift&31
            if reg in (16,17): word = word&~(31<<shift) | (33-reg)<<shift
        result[offset//4] = word
    # V0 remains the selected index until the positive helper consumes it.
    for offset,expected,replacement in ((0x50,0x53200025,0x13200024),(0x54,0x8E4402F4,0),
            (0x84,0x00403825,0x2401FFFF),(0x88,0x2401FFFF,0x10410016),
            (0x8C,0x10410015,0x00403825),(0xC4,0x00E02825,0x00402825),
            (0xA4,0x51600010,0x1160000F),(0xA8,0x8E4402F4,0),
            (0xC8,0x10000007,0x10000006),(0xCC,0x8E4402F4,0)):
        assert raw[offset//4] == expected
        result[offset//4] = replacement
    before = list(result)
    for old,new in PERMUTATION.items(): result[new//4] = before[old//4]
    assert result[0x160//4] == 0xAE380000 and raw[0x168//4] == 0x8FA4003C
    result[0x160//4],result[0x168//4] = 0xAFB8003C,0x03002025
    return result


def normalized_relocations(relocations):
    return {PERMUTATION.get(offset,offset):list(items) for offset,items in relocations.items()}


def guard_rows(raw, relocations):
    replacement, moved = normalize(raw),normalized_relocations(relocations)
    def spec(items): return ';'.join(kind+':'+symbol for kind,symbol in items) or '-'
    return [dict(filename='game_16EE20',function=screen.FUNCTION,offset='0x%X'%offset,
        expected='0x%08X'%raw[offset//4],replacement='0x%08X'%replacement[offset//4],
        expected_relocations=spec(relocations.get(offset,[])),replacement_relocations=spec(moved.get(offset,[])),
        note='Normalize effect dispatch closed register schedule and private cursor operations',
        insert_after='',insert_after_relocations='',omit='false') for offset in OFFSETS]


def memory_case(category, selected, count, layout, gate):
    memory = {STACK+i:0xA5 for i in range(-0x600,0x100)}
    for base,size in ((ACTOR-16,0x440),(NODES-16,0x110),(RECORDS-16,0x140),
                      (TABLE_A-16,12*4+16),(TABLE_B,21*8+16),(GATE,1)):
        memory.update({base+i:(i*13+7)&255 for i in range(size)})
    put(memory,GATE,gate,1); put(memory,ACTOR+0x184,0xFFFFFFA5); put(memory,ACTOR+0x400,0)
    for i in range(12): put(memory,TABLE_A+i*4,0 if i==11 else CLASS_CALLBACK)
    for i in range(21):
        put(memory,TABLE_B+i*8,0 if i==20 else EFFECT)
        put(memory,TABLE_B+i*8+4,(count if i==selected else -1)&0xFFFFFFFF)
    for i,amount in enumerate((0x8000,0xFFFF,0,0x7FFF)):
        node,record = NODES+i*0x20,RECORDS+i*0x40
        put(memory,node+0x10,record); put(memory,node+0x14,node+0x20 if i<3 else 0)
        put(memory,node+0x1C,0x1A if layout!=2 or i%2 else 0x19,2)
        put(memory,record+0x28,(0,5,19,20)[i]); put(memory,record+0xE,amount,2)
    if layout==1: put(memory,NODES+0x14,0)
    put(memory,ACTOR+0x2F4,0 if layout==0 else NODES)
    return memory


def mutate(memory,target,mutation,selected,writer=put):
    if target==CLASS_CALLBACK:
        if mutation&2: writer(memory,ACTOR+0x2F4,NODES+0x20)
        if mutation&4 and selected>=0:
            writer(memory,TABLE_B+selected*8,ALT_EFFECT); writer(memory,TABLE_B+selected*8+4,0)
    if target in (EFFECT,ALT_EFFECT,POSITIVE):
        writer(memory,ACTOR+0x400,(read(memory,ACTOR+0x400)+1)&0xFFFFFFFF)
        if mutation&1: writer(memory,NODES+0x14,NODES+0x60)
        if mutation&8: writer(memory,RECORDS+0x40+0x28,19)


def reference(memory,category,selected,mutation,context,category_result=7):
    memory,calls = dict(memory),[]
    if read(memory,GATE,1): return external(memory),calls
    calls.append((CLASSIFY,ACTOR))
    if read(memory,TABLE_A+category*4):
        calls.extend(((MASK,read(memory,ACTOR+0x184)),(CATEGORY,read(memory,ACTOR+0x184)&31)))
        callback = read(memory,TABLE_A+category*4)
        calls.append((callback,category_result,ACTOR)); mutate(memory,callback,mutation,selected)
        if selected!=-1 and read(memory,TABLE_B+selected*8):
            if signed(read(memory,TABLE_B+selected*8+4))>0:
                target=POSITIVE; calls.append((target,ACTOR,selected))
            else:
                target=read(memory,TABLE_B+selected*8); calls.append((target,ACTOR,context,0))
            mutate(memory,target,mutation,selected)
    node = read(memory,ACTOR+0x2F4); cursor_moved=False
    for _ in range(8):
        calls.append((SEARCH,node,0x1A))
        while node and read(memory,node+0x1C,2)!=0x1A: node=read(memory,node+0x14)
        if not node: return external(memory),calls
        record=read(memory,node+0x10); index=read(memory,record+0x28)
        if read(memory,TABLE_B+index*8):
            index=read(memory,record+0x28); target=read(memory,TABLE_B+index*8)
            amount=read(memory,record+0xE,2)
            amount=(amount if amount<0x8000 else amount-0x10000)&0xFFFFFFFF
            calls.append((target,ACTOR,context,amount)); mutate(memory,target,mutation,selected)
            if mutation&32 and not cursor_moved: node=NODES+0x40; cursor_moved=True
        node=read(memory,node+0x14)
    raise AssertionError('reference loop budget')


class EffectOracle(SignedByteOracle):
    def __init__(self,words,memory,category,selected,mutation,context,phase,helpers,entry=screen.ENTRY,bind_cursor=True):
        super().__init__(words,memory,entry=entry,arguments=(ACTOR,context),phase=phase,connected=helpers)
        self.category,self.selected,self.mutation = category,selected,mutation
        self.cursor_reads,self.frame_sp = [],self.before[29]
        self.cursor_home,self.cursor_moved = None,False
        self.bind_cursor=bind_cursor

    def execute(self,word):
        index=len(self.events)
        super().execute(word)
        if self.bind_cursor and word==0x8FA4003C and self.code.get(screen.ENTRY+0x168)==word:
            event=self.events[index]
            assert event==('R',self.frame_sp-12,4,self.r[24]),('cursor register lifetime',event,self.r[24])
            self.cursor_reads.append(index)

    def comparable_events(self):
        return [event for index,event in enumerate(self.events) if index not in self.cursor_reads]

    def record_call(self,target):
        if target==screen.ENTRY: self.frame_sp=self.r[29]
        if target==SEARCH: self.cursor_home=self.r[6]
        if target in (CLASSIFY,MASK,CATEGORY): args=self.arguments(1)
        elif target in (SEARCH,POSITIVE,CLASS_CALLBACK,ALT_CLASS,screen.ENTRY): args=self.arguments(2)
        else:
            assert target in (EFFECT,ALT_EFFECT),('invalid target',target)
            args=self.arguments(3)
        self.calls.append((target,*args)); self.events.append(('CALL',target,*args))

    def hook(self,target):
        if target==CLASSIFY: result=self.category
        elif target==CATEGORY: result=7
        elif target in (CLASS_CALLBACK,ALT_CLASS): result=self.selected&0xFFFFFFFF
        else:
            assert target in (EFFECT,ALT_EFFECT,POSITIVE),('invalid target',target)
            result=0xA5000002
        mutate(self.memory,target,self.mutation,self.selected,
            writer=lambda memory,address,value:self.put(address,value,4))
        if self.mutation&32 and target in (EFFECT,ALT_EFFECT,POSITIVE) and self.cursor_home and not self.cursor_moved:
            self.put(self.cursor_home,NODES+0x40,4); self.cursor_moved=True
        for reg in (1,2,3,*range(4,16),24,25): self.r[reg]=0xA5000000+reg
        self.f[:20]=[0xA5000000+i for i in range(20)]; self.r[2]=result


class LookupOracle(EffectOracle):
    def hook(self,target):
        super().hook(target)
        if target==CATEGORY: self.put(TABLE_A+self.category*4,ALT_CLASS,4)


def game_data(elf):
    data=elf.read_bytes(); header=ELF_HEADER.unpack_from(data)
    sections=[SECTION_HEADER.unpack_from(data,header[6]+i*header[11]) for i in range(header[12])]
    names=sections[header[13]]; strings=data[names[4]:names[4]+names[5]]
    section=next(s for s in sections if read_c_string(strings,s[0])=='.game_data')
    return data[section[4]:section[4]+section[5]],section[3]


class GameEffectDispatchMatchTests(unittest.TestCase):
    run_host=native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        cls.output=cls.root/'conker/build/game-effect-dispatch-test'; cls.output.mkdir(exist_ok=True)
        cls.record,cls.raw=screen.compile_candidate(cls.root,cls.output,'selected')
        cls.normalized=normalize(cls.raw)
        cls.rom=(cls.root/'conker/conker.us.bin').read_bytes()
        cls.retail=list(struct.unpack_from('>100I',cls.rom,screen.ROM))
        cls.helpers,cls.connected={},{}
        for entry,offset,length in ((MASK,0x13CD7C,3),(SEARCH,0x17C190,23),
                (CLASSIFY,0x16F0BC,45),(CATEGORY,0x16F170,57)):
            cls.connected.update({entry+i*4:word for i,word in enumerate(struct.unpack_from('>%dI'%length,cls.rom,offset))})
        cls.helpers={pc:word for pc,word in cls.connected.items() if pc<MASK+12 and pc>=MASK or SEARCH<=pc<SEARCH+92}
        cls.data,cls.data_base=game_data(cls.root/'conker/build/conker.us.elf')
        cls.directory=tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path=Path(cls.directory.name)

    def models(self,memory,category,selected,mutation,context,phase=0,helpers=None,wanted=None):
        wanted=wanted or reference(memory,category,selected,mutation,context)
        models=[]
        for body in (self.raw,self.normalized,self.retail):
            model=EffectOracle(body,memory,category,selected,mutation,context,phase,helpers or self.helpers).run()
            self.assertEqual((external(model.memory),model.calls),wanted)
            models.append(model)
        self.assertEqual(models[0].comparable_events(),models[2].events)
        self.assertEqual(models[1].events,models[2].events)
        self.assertEqual(models[0].memory,models[2].memory)
        self.assertEqual(models[1].memory,models[2].memory)
        return models

    def test_compiler_controls_complete_closed_derivation_and_actual_sdk(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences']), (100,72,25))
        self.assertEqual(self.normalized,self.retail)
        self.assertEqual(tuple(i*4 for i,(a,b) in enumerate(zip(self.raw,self.retail)) if a!=b),OFFSETS)
        self.assertEqual(self.raw[:20],self.retail[:20]); self.assertEqual(self.raw[93:],self.retail[93:])
        records=[]
        for name,body in screen.candidates():
            for profile in screen.PROFILES:
                record,_=screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                self.assertEqual(record['diagnostics'],''); records.append(record)
        self.assertEqual([(r['name'],r['body_words'],r['frame'],r['differences']) for r in records
            if r['body_words']==100 and r['frame']==72 and r['differences']==25],
            [('shape-110-o2g3',100,72,25),('shape-111-o2g3',100,72,25)])
        (self.output/'controls.json').write_text(json.dumps(records,indent=2)+'\n')

    def test_actual_padder_relocation_movement_full_slot_and_stale_guards(self):
        text,functions,relocations=parse_object(self.output/'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['value'],0)
        raw=list(struct.unpack_from('>100I',text))
        rows=guard_rows(raw,relocations)
        fields=tuple(rows[0]); guards=self.output/'guards.csv'
        with guards.open('w',newline='') as stream:
            writer=csv.DictWriter(stream,fieldnames=fields); writer.writeheader(); writer.writerows(rows)
        layout=self.output/'layout.csv'
        layout.write_text('version,section,filename,function,address,end\nus,game,game_16EE20,func_15141A7C,0x15141A7C,0x15141C0C\n')
        assembly=emit_padded_assembly(self.output/'selected.o',layout,'game_16EE20',word_patches_path=guards)
        (self.output/'padded.s').write_text(assembly)
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(self.output/'padded.o'),
            str(self.output/'padded.s')],check=True,capture_output=True)
        _,padded,moved=parse_object(self.output/'padded.o')
        self.assertEqual(padded[screen.FUNCTION]['size'],400)
        self.assertEqual(moved,normalized_relocations(relocations))
        for alternate in (False,True):
            symbols=dict(screen.SYMBOLS)
            if alternate: symbols.update(D_8008A084=0x90007FFC,D_8008A0B4=0x90018008,D_800BE616=0x90028000)
            linked=[]
            for name in ('selected','padded'):
                elf=self.output/(name+('-alternate' if alternate else '-retail')+'.elf')
                subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(self.output/'effect-dispatch.ld'),
                    '-e',screen.FUNCTION,*['--defsym=%s=0x%X'%item for item in symbols.items()],
                    '-o',str(elf),str(self.output/(name+'.o'))],check=True,capture_output=True)
                words=load_elf_functions(str(elf),'mips-linux-gnu-objdump')[0][screen.FUNCTION]
                self.assertFalse(any(words[100:])); linked.append(words[:100])
            self.assertEqual(linked[1],normalize(linked[0]))
            if not alternate: self.assertEqual(linked[1],self.retail)
        for column,bad in (('expected','0x00000000'),('expected_relocations','R_MIPS_HI16:wrong_symbol')):
            changed=[dict(row) for row in rows]; changed[0][column]=bad
            with guards.open('w',newline='') as stream:
                writer=csv.DictWriter(stream,fieldnames=fields); writer.writeheader(); writer.writerows(changed)
            with self.assertRaisesRegex(ValueError,'stale word patch|stale relocations'):
                emit_padded_assembly(self.output/'selected.o',layout,'game_16EE20',word_patches_path=guards)
        with guards.open('w',newline='') as stream:
            writer=csv.DictWriter(stream,fieldnames=fields); writer.writeheader(); writer.writerows(rows)

    def test_guest_full_storage_live_mutations_all_words_and_one_private_read(self):
        coverage=[set(),set(),set()]; cases,reloads=0,0
        for category,selected,count,layout,gate,mutation,phase in itertools.product(range(12),(-1,0,5,20),
                (-1,0,1),range(4),(0,1),(0,1,2,4,8,15),(0,8)):
            memory=memory_case(category,selected,count,layout,gate)
            models=self.models(memory,category,selected,mutation,0x80000000+cases,phase)
            for i,model in enumerate(models): coverage[i].update(model.visits)
            reloads+=len(models[0].cursor_reads); cases+=1
        target=set(range(screen.ENTRY,screen.ENTRY+400,4))
        self.assertEqual([c&target for c in coverage],[target]*3)
        self.assertEqual((cases,reloads),(13824,13764))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases,bodies=3,
            covered_words=[len(c&target) for c in coverage],private_cursor_reads=reloads),indent=2)+'\n')

    def test_connected_retail_classifiers_switch_tables_mask_and_list_search(self):
        identity_values={0x15141C5C:10,0x15141C64:9,0x15141C6C:8,0x15141C74:0,
            0x15141C7C:1,0x15141C84:2,0x15141C8C:5,0x15141C94:6,0x15141C9C:7,
            0x15141CA4:3,0x15141CAC:4,0x15141CB4:11}
        def word(address): return struct.unpack_from('>I',self.data,address-self.data_base)[0]
        identity={i:identity_values[word(0x800A52CC+i*4)] for i in range(89)}
        identity.update({121+i:identity_values[word(0x800A5218+i*4)] for i in range(45)})
        targets=[word(0x800A5430+i*4) for i in range(16)]
        coverage=[set(),set(),set()]; cases,reloads=0,0
        for identity_byte,flags,world in itertools.product(range(256),(*range(32),0x80000000,0xFFFFFFA5),
                (0,2,20,25,39,47,66,0x80000000)):
            category=identity.get(identity_byte,11); selected=(-1,0,5,20)[identity_byte%4]
            mutation=(0,1,2,4,8,15)[identity_byte%6]
            memory=memory_case(category,selected,(-1,0,1)[flags%3],identity_byte%4,0)
            memory.update({0x800A5218+i:self.data[0x800A5218-self.data_base+i] for i in range(0x258)})
            memory.update({WORLD+i:0 for i in range(4)})
            put(memory,WORLD,world); put(memory,ACTOR+4,identity_byte,1); put(memory,ACTOR+0x184,flags)
            value=flags&31
            if world in (47,66,39,25): answer={47:6,66:7,39:8,25:5}[world]
            elif value>=16: answer=9
            elif targets[value]==0x15141D58: answer=7 if world==2 else 4
            elif targets[value]==0x15141D74: answer=5 if world==20 else 9
            else: answer={0x15141D38:0,0x15141D40:2,0x15141D48:1,0x15141D50:3,
                0x15141D90:9,0x15141D98:9}[targets[value]]
            context=0x80000000+cases
            wanted=reference(memory,category,selected,mutation,context,answer)
            models=self.models(memory,category,selected,mutation,context,(cases%2)*8,self.connected,wanted)
            for i,model in enumerate(models): coverage[i].update(model.visits)
            reloads+=len(models[0].cursor_reads); cases+=1
        self.assertEqual((cases,reloads),(69632,110976))
        self.assertEqual([len(c&set(self.connected)) for c in coverage],[122]*3)
        (self.output/'classifiers.json').write_text(json.dumps(dict(cases=cases,bodies=3,
            mapped_words=len(self.connected),reached_words=122,private_cursor_reads=reloads),indent=2)+'\n')

    def test_registered_cursor_alias_stays_live_after_callbacks(self):
        cases=0
        for category,selected,count,layout,mutation,phase in itertools.product((0,11),(-1,0,5),
                (-1,1),(2,3),(32,33,34,36,40,63),(0,8)):
            memory=memory_case(category,selected,count,layout,0)
            self.models(memory,category,selected,mutation,0xFFFFFFFF,phase); cases+=1
        self.assertEqual(cases,288)

    def test_native_actual_source_full_storage_live_aliases_cursor_and_signed_payloads(self):
        owner=(self.root/'conker/src/game_16EE20.c').read_text()
        body=screen.SELECTED if screen.SELECTED not in owner else owner[owner.index(screen.SELECTED):owner.index(screen.SELECTED)+len(screen.SELECTED)]
        self.fixture=native_fixture()+body+'\n'
        self.run_host(r'''
int category,selected,count,layout,gate,mode,context,alias,cases=0;
int selections[]={-1,0,5,20};s32 counts[]={-1,0,1,(s32)0x80000000u,0x7FFFFFFF};
int modes[]={0,1,2,4,8,15,16,31,32,63,64,127};s32 contexts[]={0,(s32)0x80000000u,-1};
if(sizeof(void *)!=4 || sizeof(GameEffectEntry)!=8) return 70;
for(category=0;category<12;category++) for(selected=0;selected<4;selected++)
for(count=0;count<5;count++) for(layout=0;layout<4;layout++) for(gate=0;gate<2;gate++)
for(mode=0;mode<12;mode++) for(context=0;context<3;context++) {
    initialize(category,selections[selected],counts[count],layout,gate,modes[mode],0);
    reference_native(actor,contexts[context]);remember();
    initialize(category,selections[selected],counts[count],layout,gate,modes[mode],0);
    func_15141A7C(actor,contexts[context]);if(compare()) return 71;cases++;
}
if(cases!=69120) return 72;
for(alias=1;alias<5;alias++) for(count=0;count<3;count++) for(layout=0;layout<4;layout++)
for(mode=0;mode<12;mode++) for(context=0;context<3;context++) {
    initialize(0,0,counts[count],layout,0,modes[mode],alias);
    reference_native(actor,contexts[context]);remember();
    initialize(0,0,counts[count],layout,0,modes[mode],alias);
    func_15141A7C(actor,contexts[context]);if(compare()) return 73;cases++;
}
if(cases!=70848) return 74;
''')
        (self.output/'native.json').write_text(json.dumps(dict(cases=70848,pointer_bytes=4,
            external_alias_modes=4,registered_private_cursor_alias=True,scalar_return=False),indent=2)+'\n')

    def test_connected_retail_caller_forwards_live_globals_and_void_native_wrapper(self):
        caller=list(struct.unpack_from('>11I',self.rom,0x9F278)); cases=0
        for category,selected,count,layout,gate,mutation,context,phase in itertools.product((0,11),(-1,0,20),
                (-1,1),(0,3),(0,1),(0,15,32),(0,0x80000000,0xFFFFFFFF),(0,8)):
            memory=memory_case(category,selected,count,layout,gate)
            memory.update({0x800D154C+i:0 for i in range(4)});memory.update({0x800D1580+i:0 for i in range(4)})
            put(memory,0x800D154C,ACTOR);put(memory,0x800D1580,context)
            storage,calls=reference(memory,category,selected,mutation,context)
            wanted=(storage,[(screen.ENTRY,ACTOR,context),*calls]); models=[]
            for body in (self.raw,self.normalized,self.retail):
                connected=dict(self.helpers);connected.update({screen.ENTRY+i*4:w for i,w in enumerate(body)})
                model=EffectOracle(caller,memory,category,selected,mutation,context,phase,connected,entry=0x15071DC8).run()
                self.assertEqual((external(model.memory),model.calls),wanted);models.append(model)
            self.assertEqual(models[0].comparable_events(),models[2].events)
            self.assertEqual(models[1].events,models[2].events);cases+=1
        self.assertEqual(cases,864)
        owner=(self.root/'conker/src/game_981E0.c').read_text()
        wrapper='void func_15071DC8(void) {\n    func_15141A7C(D_800D154C, D_800D1580);\n}'
        self.assertIn(wrapper,owner)
        self.fixture=native_fixture()+screen.SELECTED+'\nstatic u8 *D_800D154C;static s32 D_800D1580;\n'+wrapper+'\n'
        self.run_host(r'''
int a,k,m,c,cases=0;int modes[]={0,15,32,63};s32 contexts[]={0,(s32)0x80000000u,-1};
for(a=0;a<5;a++) for(k=0;k<4;k++) for(m=0;m<4;m++) for(c=0;c<3;c++) {
    initialize(0,0,k==0?1:-1,k,0,modes[m],a);reference_native(actor,contexts[c]);remember();
    initialize(0,0,k==0?1:-1,k,0,modes[m],a);D_800D154C=actor;D_800D1580=contexts[c];
    func_15071DC8();if(compare()) return 76;cases++;
}
if(cases!=240) return 77;
''')
        (self.output/'caller.json').write_text(json.dumps(dict(guest_cases=cases,bodies=3,native_cases=240,
            caller_words=11,scalar_return=False),indent=2)+'\n')

    def test_fresh_classifier_lookup_and_invalid_second_targets(self):
        cached=screen.SELECTED.replace('    s32 category;', '    GameEffectClassifier cached;\n    s32 category;').replace(
            '        if (((GameEffectClassifier *)D_8008A084)[category] != NULL)',
            '        cached = ((GameEffectClassifier *)D_8008A084)[category];\n        if (cached != NULL)').replace(
            'selected = ((GameEffectClassifier *)D_8008A084)[category](', 'selected = cached(')
        _,negative=screen.compile_candidate(self.root,self.output,'negative-cached-classifier',cached)
        for category,selected in itertools.product((0,5,10),(-1,0,20)):
            memory=memory_case(category,selected,-1,3,0)
            original=EffectOracle(self.retail,memory,category,selected,0,0xFFFFFFFF,0,self.helpers).run()
            expected_calls=[(ALT_CLASS,*call[1:]) if call[0]==CLASS_CALLBACK else call for call in original.calls]
            expected_memory=external(original.memory);put(expected_memory,TABLE_A+category*4,ALT_CLASS)
            for body in (self.raw,self.normalized,self.retail):
                model=LookupOracle(body,memory,category,selected,0,0xFFFFFFFF,0,self.helpers).run()
                self.assertEqual((external(model.memory),model.calls),(expected_memory,expected_calls))
            bad=LookupOracle(negative,memory,category,selected,0,0xFFFFFFFF,0,self.helpers,entry=0x1B000000,bind_cursor=False).run()
            self.assertNotEqual(bad.calls,expected_calls)
        class InvalidLookup(EffectOracle):
            def hook(self,target):
                super().hook(target)
                if target==CATEGORY: self.put(TABLE_A+self.category*4,0,4)
        for body in (self.raw,self.normalized,self.retail):
            with self.assertRaisesRegex(AssertionError,'invalid target'):
                InvalidLookup(body,memory_case(0,0,-1,3,0),0,0,0,0,0,self.helpers).run()

    def test_compiled_negatives_change_calls_storage_live_reads_or_mapped_accesses(self):
        stale=screen.SELECTED.replace('        while (func_1514ECE0(node, 0x1A, &node)) {',
            '        while (func_1514ECE0(node, 0x1A, &node)) {\n            u8 *before = node;').replace(
            '*(u8 **)(node + 0x14)', '*(u8 **)(before + 0x14)')
        controls={
            'placeholder':'void func_15141A7C(u8 *a,s32 context) {}',
            'inverted-gate':screen.SELECTED.replace('D_800BE616 == 0','D_800BE616 != 0'),
            'wrong-actor':screen.SELECTED.replace('func_15141C0C(actor)','func_15141C0C(actor + 1)'),
            'zero-flags':screen.SELECTED.replace('func_1510F8CC(*(s32 *)(actor + 0x184))','func_1510F8CC(0)'),
            'zero-count-positive':screen.SELECTED.replace('.count > 0','.count >= 0'),
            'wrong-key':screen.SELECTED.replace('0x1A, &node','0x19, &node'),
            'unsigned-payload':screen.SELECTED.replace('*(s16 *)(record + 0xE)','*(u16 *)(record + 0xE)'),
            'cached-selector':screen.SELECTED.replace('*(volatile s32 *)(record + 0x28)','*(s32 *)(record + 0x28)'),
            'stale-cursor':stale,
            'omit-list':screen.SELECTED.replace('        node = *(u8 **)(actor + 0x2F4);','        return;\n        node = *(u8 **)(actor + 0x2F4);')}
        receipts=[]
        def owner_events(model):
            return [event for event in model.events if event[0]=='CALL' or not STACK-0x600<=event[1]<STACK+0x100]
        for name,body in controls.items():
            _,words=screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            cases,different=0,0
            for category,selected,count,layout,gate,mutation in itertools.product((0,11),(-1,0,5,20),
                    (-1,0,1),(0,2,3),(0,1),(0,15,32)):
                memory=memory_case(category,selected,count,layout,gate)
                original=EffectOracle(self.retail,memory,category,selected,mutation,0xFFFFFFFF,0,self.helpers).run()
                try:
                    model=EffectOracle(words,memory,category,selected,mutation,0xFFFFFFFF,0,self.helpers,entry=0x1B000000,bind_cursor=False).run()
                    differs=(external(model.memory),model.calls,owner_events(model))!=(external(original.memory),original.calls,owner_events(original))
                except AssertionError as error:
                    self.assertIn(error.args[0][0],('unmapped read','unmapped write','unmapped store','invalid target'))
                    differs=True
                different+=bool(differs);cases+=1
            self.assertGreater(different,0,name);receipts.append(dict(name=name,cases=cases,differences=different))
        (self.output/'negatives.json').write_text(json.dumps(receipts,indent=2)+'\n')

    def test_guest_only_invalid_storage_and_cyclic_list_budget(self):
        for body in (self.raw,self.normalized,self.retail):
            missing=memory_case(0,0,-1,3,0)
            for address in range(ACTOR+0x184,ACTOR+0x188): del missing[address]
            with self.assertRaisesRegex(AssertionError,'unmapped read'):
                EffectOracle(body,missing,0,0,0,0,0,self.helpers).run()
            cycle=memory_case(11,-1,-1,1,0)
            put(cycle,NODES+0x14,NODES)
            with self.assertRaisesRegex(AssertionError,'instruction budget exhausted'):
                EffectOracle(body,cycle,11,-1,0,0,0,self.helpers).run()
            skipped=memory_case(0,0,-1,3,1)
            for address in range(ACTOR-16,ACTOR+0x430): skipped.pop(address,None)
            model=EffectOracle(body,skipped,0,0,0,0,0,self.helpers).run()
            self.assertEqual(model.calls,[])

    def test_production_source_full_slot_caller_and_closed_guard_prefix(self):
        owner=(self.root/'conker/src/game_16EE20.c').read_text()
        self.assertIn(screen.SELECTED,owner); self.assertIn(screen.PROTOTYPE,owner)
        self.assertIn(screen.LOCAL_DECLARATIONS,owner)
        functions,_,addresses=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),
            'mips-linux-gnu-objdump')
        self.assertEqual(addresses[screen.FUNCTION],screen.ENTRY)
        self.assertEqual(functions[screen.FUNCTION],self.retail)
        self.assertEqual(functions['func_15071DC8'],list(struct.unpack_from('>11I',self.rom,0x9F278)))
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:
            rows=list(csv.DictReader(stream))
        self.assertEqual(len(rows),10809)
        prefix=json.dumps(rows[:10760],sort_keys=True,separators=(',',':')).encode()
        self.assertEqual(hashlib.sha256(prefix).hexdigest(),
            '81681279410eb5b2409eed147dbe85366bb7a7bfb3a18c795940e15ec2a54e05')
        text,functions,relocations=parse_object(self.output/'selected.o')
        self.assertEqual(functions[screen.FUNCTION]['value'],0)
        self.assertEqual(rows[10760:10785],guard_rows(list(struct.unpack_from('>100I',text)),relocations))


def native_fixture():
    return r'''
typedef unsigned char u8;typedef unsigned short u16;typedef signed short s16;
typedef unsigned int u32;typedef signed int s32;
typedef struct {s32 unk0; s32 unk4;} struct32;
#define NULL ((void *)0)
static s32 D_8008A084[12];static struct32 D_8008A0B4[21];static u8 D_800BE616;
''' + screen.LOCAL_DECLARATIONS + r'''
typedef union {u32 align;u8 bytes[0x440];} ActorStorage;
typedef union {u32 align;u8 bytes[0x110];} NodeStorage;
typedef union {u32 align;u8 bytes[0x140];} RecordStorage;
static ActorStorage actorStorage,wantedActor;static NodeStorage nodeStorage,wantedNodes;
static RecordStorage recordStorage,wantedRecords;
static s32 wantedA[12];static struct32 wantedB[21];static u32 log[128],wantedLog[128];
static u8 *actor=actorStorage.bytes+16,*nodes[4],*records[4];static u8 **registeredCursor;
static int fixtureCategory,fixtureSelected,mutation,cursorMoved,wantedMoved,logCount,wantedLogCount;
static u16 payloads[]={0x8000,0xFFFF,0,0x7FFF};
static u32 load(const void *p) {return *(const u32 *)p;}
static void store(void *p,u32 value) {*(u32 *)p=value;}
static void append(u32 kind,u32 a,u32 b,u32 c) {
    int base=logCount*4;log[base]=kind;log[base+1]=a;log[base+2]=b;log[base+3]=c;logCount++;
}
static void effect_actions(void) {
    store(actor+0x400,load(actor+0x400)+1);
    if(mutation&1) *(u8 **)(nodes[0]+0x14)=nodes[3];
    if(mutation&8) store(records[1]+0x28,19);
    if((mutation&32) && registeredCursor!=NULL && !cursorMoved) {
        *registeredCursor=nodes[2];cursorMoved=1;
    }
}
static void effect(u8 *a,s32 context,s32 amount) {
    append(0x1A200000u,(u32)a,(u32)context,(u32)amount);effect_actions();
}
static void alternate(u8 *a,s32 context,s32 amount) {
    append(0x1A200100u,(u32)a,(u32)context,(u32)amount);effect_actions();
}
static s32 classify_actions(s32 category,u8 *a,u32 kind) {
    append(kind,(u32)category,(u32)a,0);
    if(mutation&2) *(u8 **)(actor+0x2F4)=nodes[1];
    if((mutation&4) && fixtureSelected>=0) {
        D_8008A0B4[fixtureSelected].unk0=(s32)alternate;D_8008A0B4[fixtureSelected].unk4=0;
    }
    return fixtureSelected;
}
static s32 classify_callback(s32 category,u8 *a) {return classify_actions(category,a,0x1A100000u);}
static s32 classify_alternate(s32 category,u8 *a) {return classify_actions(category,a,0x1A100100u);}
s32 func_15141C0C(u8 *a) {
    append(0x15141C0Cu,(u32)a,0,0);
    if(mutation&16) store(a+0x184,0x12345667u);
    return fixtureCategory;
}
s32 func_1510F8CC(s32 flags) {append(0x1510F8CCu,(u32)flags,0,0);return flags&31;}
s32 func_15141CC0(s32 value) {
    append(0x15141CC0u,(u32)value,0,0);
    if(mutation&64) D_8008A084[fixtureCategory]=(s32)classify_alternate;
    return 7;
}
void func_15141E38(u8 *a,s32 index) {
    append(0x15141E38u,(u32)a,(u32)index,0);effect_actions();
}
__attribute__((noinline)) s32 func_1514ECE0(u8 *node,s16 key,u8 **result) {
    append(0x1514ECE0u,(u32)node,(u32)(s32)key,0);
    while(node!=NULL && *(s16 *)(node+0x1C)!=key) node=*(u8 **)(node+0x14);
    *result=node;registeredCursor=node!=NULL?result:NULL;return node!=NULL;
}
static void initialize(int category,int selected,s32 count,int layout,int gate,int mode,int alias) {
    int i;fixtureCategory=category;fixtureSelected=selected;mutation=mode;
    cursorMoved=0;registeredCursor=NULL;logCount=0;D_800BE616=(u8)gate;
    for(i=0;i<128;i++) log[i]=0;
    for(i=0;i<(int)sizeof(actorStorage);i++) actorStorage.bytes[i]=(u8)(i*13+7);
    for(i=0;i<(int)sizeof(nodeStorage);i++) nodeStorage.bytes[i]=(u8)(i*13+7);
    for(i=0;i<(int)sizeof(recordStorage);i++) recordStorage.bytes[i]=(u8)(i*13+7);
    for(i=0;i<12;i++) D_8008A084[i]=i==11?0:(s32)classify_callback;
    for(i=0;i<21;i++) {
        D_8008A0B4[i].unk0=i==20?0:(s32)effect;
        D_8008A0B4[i].unk4=i==selected?count:-1;
    }
    for(i=0;i<4;i++) {nodes[i]=nodeStorage.bytes+16+i*0x20;records[i]=recordStorage.bytes+16+i*0x40;}
    if(alias==1) records[0]=actor+0x3D8;
    if(alias==2) nodes[0]=actor+0x390;
    if(alias==3) records[0]=(u8 *)D_8008A0B4+44;
    if(alias==4) records[0]=(u8 *)D_8008A084+4;
    store(actor+0x184,0xFFFFFFA5u);store(actor+0x400,0);
    for(i=0;i<4;i++) {
        *(u8 **)(nodes[i]+0x10)=records[i];*(u8 **)(nodes[i]+0x14)=i<3?nodes[i+1]:NULL;
        *(s16 *)(nodes[i]+0x1C)=(s16)((layout==2 && !(i&1))?0x19:0x1A);
        store(records[i]+0x28,(u32[]){0,5,19,20}[i]);*(s16 *)(records[i]+0xE)=(s16)payloads[i];
    }
    if(layout==1) *(u8 **)(nodes[0]+0x14)=NULL;
    *(u8 **)(actor+0x2F4)=layout==0?NULL:nodes[0];
}
static void reference_native(u8 *a,s32 context) {
    s32 category,selected,index;GameEffectClassifier classifier;GameEffectCallback callback;
    u8 *node,*record;
    if(D_800BE616) return;
    category=func_15141C0C(a);
    classifier=(GameEffectClassifier)D_8008A084[category];
    if(classifier!=NULL) {
        s32 flags=func_1510F8CC((s32)load(a+0x184));s32 answer=func_15141CC0(flags);
        classifier=(GameEffectClassifier)D_8008A084[category];selected=classifier(answer,a);
        if(selected!=-1 && D_8008A0B4[selected].unk0) {
            if(D_8008A0B4[selected].unk4>0) func_15141E38(a,selected);
            else {callback=(GameEffectCallback)D_8008A0B4[selected].unk0;callback(a,context,0);}
        }
    }
    node=*(u8 **)(a+0x2F4);
    while(func_1514ECE0(node,0x1A,&node)) {
        record=*(u8 **)(node+0x10);index=(s32)load(record+0x28);
        if(D_8008A0B4[index].unk0) {
            index=(s32)load(record+0x28);callback=(GameEffectCallback)D_8008A0B4[index].unk0;
            callback(a,context,(s32)*(s16 *)(record+0xE));
        }
        node=*(u8 **)(node+0x14);
    }
}
static void remember(void) {
    int i;wantedActor=actorStorage;wantedNodes=nodeStorage;wantedRecords=recordStorage;
    wantedMoved=cursorMoved;wantedLogCount=logCount;
    for(i=0;i<12;i++) wantedA[i]=D_8008A084[i];
    for(i=0;i<21;i++) wantedB[i]=D_8008A0B4[i];
    for(i=0;i<128;i++) wantedLog[i]=log[i];
}
static int compare(void) {
    int i;
    if(cursorMoved!=wantedMoved || logCount!=wantedLogCount) return 1;
    for(i=0;i<(int)sizeof(actorStorage);i++) if(actorStorage.bytes[i]!=wantedActor.bytes[i]) return 2;
    for(i=0;i<(int)sizeof(nodeStorage);i++) if(nodeStorage.bytes[i]!=wantedNodes.bytes[i]) return 3;
    for(i=0;i<(int)sizeof(recordStorage);i++) if(recordStorage.bytes[i]!=wantedRecords.bytes[i]) return 4;
    for(i=0;i<12;i++) if(D_8008A084[i]!=wantedA[i]) return 5;
    for(i=0;i<21;i++) if(D_8008A0B4[i].unk0!=wantedB[i].unk0 || D_8008A0B4[i].unk4!=wantedB[i].unk4) return 6;
    for(i=0;i<128;i++) if(log[i]!=wantedLog[i]) return 7;
    return 0;
}
'''


if __name__ == '__main__': unittest.main()
