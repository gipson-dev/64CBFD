"""Actor-event byte ABI, repeated callback lookup, and live payload qualification."""

import csv
import hashlib
import itertools
import json
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_actor_event_dispatch_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_payload_copy_wrapper_match import SignedByteOracle, external, read
from tools.tests.test_game_actor_triangle_transform_match import put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

TABLE, CLEANUP = screen.SYMBOLS.values()
ACTOR, EVENT, ALTERNATE, OTHER_EVENT = 0x21000, 0x22000, 0x23000, 0x24000
CALLBACKS = (0x15500000, 0x15500004)
MASK = 0xFFFFFFFF


def field(actor, offset):
    return (actor+offset)&MASK


def memory_case(selector=7, command=0x24, enabled=1, match=True, alias=0, actor=ACTOR):
    memory = {STACK+i:0xA5 for i in range(-0x100,0x100)}
    for base, length in ((actor,0x1C0),(ALTERNATE,0x1C0),(EVENT,32),(OTHER_EVENT,32),(TABLE,1024)):
        memory.update({field(base,i):(i*13+7)&255 for i in range(length)})
    for i in range(256): put(memory,TABLE+i*4,0 if enabled==0 else CALLBACKS[(i+enabled-1)&1])
    put(memory,field(actor,0x168),selector,1)
    put(memory,ALTERNATE+0x168,selector,1)
    event = (EVENT,field(actor,0x168),field(actor,0x169),TABLE+selector*4+3)[alias]
    put(memory,event,selector if match else selector^255,1)
    put(memory,OTHER_EVENT,selector,1)
    # A table-byte alias must retain a valid callback target; use its actual byte for comparison.
    if alias==3:
        put(memory,TABLE+selector*4,CALLBACKS[(selector+enabled-1)&1] if enabled else 0)
    return memory,(actor,event,0x87654300|command)


def call_state(memory, target, args):
    actor,event,command = args
    return (target,actor,event,command,read(memory,field(actor,0x168),1),
            read(memory,field(actor,0x169),1))


def callback_actions(memory, actor, event, command, mutation):
    if mutation==1:
        put(memory,field(actor,0x168),(command+1)&255,1)
        put(memory,event,(command+1)&255,1)
        put(memory,field(actor,0x169),0x55,1)
    elif mutation==2:
        put(memory,field(actor,0x168),read(memory,field(actor,0x168),1)^255,1)
    elif mutation==3:
        put(memory,event,read(memory,field(actor,0x168),1)^255,1)
    elif mutation==4:
        put(memory,field(actor,0x169),0x81,1)
    elif mutation==5:
        put(memory,TABLE+read(memory,field(actor,0x168),1)*4,0)
        put(memory,field(actor,4),0xDEADBEEF)
    elif mutation==6:
        value = (read(memory,field(actor,0x168),1)+17)&255
        put(memory,field(actor,0x168),value,1); put(memory,event,value,1)
    elif mutation==7:
        put(memory,event,0,1)


def home_actions(memory, phase, homes):
    if homes&1: put(memory,STACK+phase,ALTERNATE)
    if homes&2: put(memory,STACK+phase+4,OTHER_EVENT)
    if homes&4: put(memory,STACK+phase+8,0xFEDCBA25)


def reference(memory, args, mutation=0, phase=0, homes=0, selector_actions=(), table_actions=()):
    memory = dict(memory)
    actor,event,command = args
    put(memory,STACK+phase+4,event); put(memory,STACK+phase+8,command)
    index = read(memory,field(actor,0x168),1)
    for address,value,size in selector_actions: put(memory,address,value,size)
    first = read(memory,TABLE+index*4)
    for address,value,size in table_actions: put(memory,address,value,size)
    calls = []
    if first:
        target = read(memory,TABLE+read(memory,field(actor,0x168),1)*4)
        assert target in CALLBACKS, ('invalid callback',target)
        event = read(memory,STACK+phase+4); command = read(memory,STACK+phase+11,1)
        calls.append(call_state(memory,target,(actor,event,command)))
        callback_actions(memory,actor,event,command,mutation)
        put(memory,STACK+phase,actor)
        home_actions(memory,phase,homes)
        actor = read(memory,STACK+phase)
    command = read(memory,STACK+phase+11,1)
    if command in (0x22,0x24,0x25):
        event = read(memory,STACK+phase+4)
        if read(memory,event,1)==read(memory,field(actor,0x168),1):
            if command==0x22:
                calls.append((CLEANUP,actor))
                put(memory,field(actor,4),0x12345678)
                put(memory,field(actor,0x169),0xE1,1)
            else: put(memory,field(actor,0x169),255 if command==0x24 else 2,1)
    return external(memory),calls


class EventOracle(SignedByteOracle):
    def __init__(self, words, memory, args, mutation=0, phase=0, homes=0,
                 selector_actions=(), table_actions=()):
        super().__init__(words,memory,entry=screen.ENTRY,arguments=args,phase=phase)
        self.actor,self.mutation,self.phase,self.homes = args[0],mutation,phase,homes
        self.selector_actions,self.table_actions = selector_actions,table_actions
        self.selector_reads,self.table_reads = 0,0

    def get(self, address, size):
        value = super().get(address,size)
        actions = ()
        if address==field(self.actor,0x168) and size==1:
            self.selector_reads += 1
            if self.selector_reads==1: actions = self.selector_actions
        if TABLE<=address<TABLE+1024 and size==4:
            self.table_reads += 1
            if self.table_reads==1: actions = self.table_actions
        for where,what,width in actions: put(self.memory,where,what,width)
        return value

    def record_call(self, target):
        if target==CLEANUP: call = (target,self.r[4])
        else:
            assert target in CALLBACKS, ('invalid callback',target)
            call = call_state(self.memory,target,tuple(self.r[4:7]))
        self.calls.append(call); self.events.append(('CALL',target,call[1:]))

    def hook(self, target):
        if target==CLEANUP:
            put(self.memory,field(self.r[4],4),0x12345678)
            put(self.memory,field(self.r[4],0x169),0xE1,1)
        else:
            callback_actions(self.memory,*self.r[4:7],self.mutation)
            home_actions(self.memory,self.phase,self.homes)
        for register in (1,2,3,*range(4,16),24,25): self.r[register] = 0xA5000000+register
        self.f[:20] = [0xA5000000+i for i in range(20)]


class GameActorEventDispatchMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root/'conker/build/game-actor-event-dispatch-test'; cls.output.mkdir(exist_ok=True)
        cls.record,cls.words = screen.compile_candidate(cls.root,cls.output,'selected')
        cls.retail = list(struct.unpack_from('>55I',(cls.root/'conker/conker.us.bin').read_bytes(),screen.ROM))
        cls.directory = tempfile.TemporaryDirectory(); cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.coverage = [set(),set()]; cls.cases = 0

    def models(self, memory, args, mutation=0, phase=0, homes=0, selector_actions=(), table_actions=()):
        wanted = reference(memory,args,mutation,phase,homes,selector_actions,table_actions)
        models = []
        for i,body in enumerate((self.words,self.retail)):
            model = EventOracle(body,memory,args,mutation,phase,homes,selector_actions,table_actions).run()
            self.assertEqual((external(model.memory),model.calls),wanted,(args,mutation,phase,homes))
            type(self).coverage[i].update(model.visits); models.append(model)
        self.assertEqual(models[0].events,models[1].events)
        self.assertEqual(models[0].r[2],models[1].r[2])
        type(self).cases += 1
        return models[0]

    def test_complete_direct_slot_actual_sdk_and_all_profiles(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],self.record['diagnostics']),
                         (55,24,0,''))
        self.assertEqual(self.words,self.retail)
        records = []
        for name,body in screen.candidates():
            for profile in screen.PROFILES:
                record,_ = screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile)
                self.assertEqual(record['diagnostics'],'')
                records.append(record)
        exact = [(r['name'],r['body_words'],r['frame']) for r in records if r['exact']]
        self.assertEqual(exact,[('selected-o2g3',55,24),('unsigned-hex-subtraction-o2g3',55,24)])
        (self.output/'controls.json').write_text(json.dumps(records,indent=2)+'\n')

    def test_guest_every_selector_byte_command_classes_and_full_storage(self):
        cases = 0
        for selector,command,enabled,match,phase in itertools.product(range(256),
                (0,0x21,0x22,0x23,0x24,0x25,0x26,0x80,255),range(3),(False,True),(0,8)):
            memory,args = memory_case(selector,command,enabled,match)
            self.models(memory,args,phase=phase); cases += 1
        self.assertEqual(cases,27648)

    def test_guest_every_command_byte_mutations_and_event_aliases(self):
        cases = 0
        for command,selector,mutation,alias in itertools.product(range(256),(0,127,128,255),range(8),range(4)):
            memory,args = memory_case(selector,command,1,True,alias)
            self.models(memory,args,mutation,8 if selector&1 else 0); cases += 1
        self.assertEqual(cases,32768)

    def test_fresh_selector_and_second_table_lookup_not_captured_callback(self):
        for command,phase,change_table in itertools.product((0x22,0x24,0x25,255),(0,8),(False,True)):
            memory,args = memory_case(7,command)
            put(memory,EVENT,8,1)
            selector = ((ACTOR+0x168,8,1),) if not change_table else ()
            table = ((TABLE+7*4,CALLBACKS[0],4),) if change_table else ()
            model = self.models(memory,args,phase=phase,selector_actions=selector,table_actions=table)
            self.assertEqual(model.calls[0][0],CALLBACKS[0])
            reads = [e for e in model.events if e[0]=='R' and (TABLE<=e[1]<TABLE+1024 or e[1]==ACTOR+0x168)]
            self.assertEqual(reads[:4], [('R',ACTOR+0x168,1,7),('R',TABLE+28,4,CALLBACKS[1]),
                ('R',ACTOR+0x168,1,7 if change_table else 8),
                ('R',TABLE+(28 if change_table else 32),4,CALLBACKS[0])])

    def test_saved_argument_homes_and_wrapping_guest_addresses(self):
        for command,homes,phase in itertools.product((0x22,0x24,0x25,255),range(8),(0,8)):
            memory,args = memory_case(7,command)
            self.models(memory,args,phase=phase,homes=homes)
        for actor,command,mutation,phase in itertools.product((ACTOR,0x7FFFFEF0,0xFFFFFEF0),
                (0x22,0x24,0x25,255),range(8),(0,8)):
            memory,args = memory_case(7,command,actor=actor)
            self.models(memory,args,mutation,phase)

    def test_noneligible_commands_never_dereference_the_event(self):
        for command,enabled,phase in itertools.product((0,0x21,0x23,0x26,128,255),range(3),(0,8)):
            memory,args = memory_case(7,command,enabled)
            args = (args[0],0,args[2])
            self.models(memory,args,phase=phase)
        for command,phase in itertools.product((0x22,0x24,0x25),(0,8)):
            memory,args = memory_case(7,command)
            changes = ((TABLE+28,0,4),)
            for body in (self.words,self.retail):
                with self.assertRaisesRegex(AssertionError,'invalid callback'):
                    EventOracle(body,memory,args,phase=phase,table_actions=changes).run()

    def test_compiled_semantic_negatives_have_real_state_call_or_access_failures(self):
        cached = screen.SELECTED.replace('    u8 *payload;', '    u8 *payload;\n    ActorEventCallback16DC80 callback;').replace(
            '    if (D_8008A02C[*(volatile u8 *)(actor + 0x168)] != NULL) {',
            '    callback = D_8008A02C[*(volatile u8 *)(actor + 0x168)];\n    if (callback != NULL) {').replace(
            'D_8008A02C[*(volatile u8 *)(actor + 0x168)](actor, event, command);','callback(actor, event, command);')
        negatives = [('stub','void func_151416E8(u8 *actor,u8 *event,u8 command) {}'),
            ('cleanup-command',screen.SELECTED.replace('command == 0x22','command == 0x21')),
            ('missing-event-gate',screen.SELECTED.replace('event[0] == payload[0x58]','1')),
            ('wrong-selector',screen.SELECTED.replace('payload[0x58]','payload[0x57]')),
            ('wrong-status-offset',screen.SELECTED.replace('payload + 0x59','payload + 0x5A')),
            ('wrong-stop-status',screen.SELECTED.replace('= -1','= 1')),
            ('wrong-start-status',screen.SELECTED.replace('= 2','= 3')),
            ('cached-callback',cached),
            ('word-command',screen.SELECTED.replace('u8 command','u32 command'))]
        cases = [(c,m,a,change) for c in (0x21,0x22,0x24,0x25,255) for m in (0,1,2)
                 for a in (0,1,2) for change in (False,True)]
        receipts = []
        for name,body in negatives:
            _,words = screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            failures = 0
            for command,mutation,alias,change in cases:
                memory,args = memory_case(7,command,1,False,alias)
                actions = ((ACTOR+0x168,8,1),(EVENT,8,1)) if change else ()
                wanted = reference(memory,args,mutation,selector_actions=actions)
                try:
                    model = EventOracle(words,memory,args,mutation,selector_actions=actions).run()
                    different = (external(model.memory),model.calls)!=wanted
                except AssertionError as error:
                    self.assertIn(error.args[0][0],('unmapped read','unmapped write','invalid callback'))
                    different = True
                failures += bool(different)
            self.assertGreater(failures,0,name); receipts.append((name,failures,len(cases)))
        (self.output/'negatives.json').write_text(json.dumps(receipts,indent=2)+'\n')

    def test_native_actual_source_every_byte_pair_and_live_aliases(self):
        source = self.root/'conker/src/game_16DC80.c'
        production = source.read_text()
        body = screen.SELECTED if screen.SELECTED not in production else production[production.index(screen.SELECTED):][:len(screen.SELECTED)]
        self.fixture = native_fixture()+body+'\n'
        self.run_host(r'''
int s,c,m,a,mode,match,i;static u8 wanted[0x1C0],wantedEvent[32],wantedTable[sizeof(D_8008A02C)];
static u32 wantedLog[18];int wantedCount;
if(sizeof(void *)!=4 || sizeof(u32)!=4 || sizeof(s8)!=1) return 40;
for(s=0;s<256;s++) for(c=0;c<256;c++) for(mode=0;mode<3;mode++) {
    initialize(s,c,mode,1,0,0);reference(actor,event,(u8)c);
    for(i=0;i<0x1C0;i++) wanted[i]=actor[i];
    for(i=0;i<32;i++) wantedEvent[i]=eventStorage[i];
    for(i=0;i<(int)sizeof(D_8008A02C);i++) wantedTable[i]=((u8 *)D_8008A02C)[i];
    for(i=0;i<18;i++) wantedLog[i]=((u32 *)log)[i];
    wantedCount=count;
    initialize(s,c,mode,1,0,0);func_151416E8(actor,event,(u8)(0x87654300u|c));
    if(count!=wantedCount) return 41;
    for(i=0;i<0x1C0;i++) if(wanted[i]!=actor[i]) return 42;
    for(i=0;i<32;i++) if(wantedEvent[i]!=eventStorage[i]) return 43;
    for(i=0;i<(int)sizeof(D_8008A02C);i++) if(wantedTable[i]!=((u8 *)D_8008A02C)[i]) return 44;
    for(i=0;i<18;i++) if(wantedLog[i]!=((u32 *)log)[i]) return 45;
}
for(s=0;s<4;s++) for(c=0;c<256;c++) for(m=0;m<8;m++) for(a=0;a<4;a++) for(match=0;match<2;match++) {
    initialize(s*85,c,1,match,a,m);reference(actor,event,(u8)c);
    for(i=0;i<0x1C0;i++) wanted[i]=actor[i];
    for(i=0;i<32;i++) wantedEvent[i]=eventStorage[i];
    for(i=0;i<(int)sizeof(D_8008A02C);i++) wantedTable[i]=((u8 *)D_8008A02C)[i];
    for(i=0;i<18;i++) wantedLog[i]=((u32 *)log)[i];
    wantedCount=count;
    initialize(s*85,c,1,match,a,m);func_151416E8(actor,event,(u8)(0xFEDCBA00u|c));
    if(count!=wantedCount) return 46;
    for(i=0;i<0x1C0;i++) if(wanted[i]!=actor[i]) return 47;
    for(i=0;i<32;i++) if(wantedEvent[i]!=eventStorage[i]) return 48;
    for(i=0;i<(int)sizeof(D_8008A02C);i++) if(wantedTable[i]!=((u8 *)D_8008A02C)[i]) return 49;
    for(i=0;i<18;i++) if(wantedLog[i]!=((u32 *)log)[i]) return 50;
}
''')

    def test_production_guard_free_source_complete_slot_and_relocations(self):
        self.assertIn(screen.SELECTED,(self.root/'conker/src/game_16DC80.c').read_text())
        self.assertIn('void func_151416E8(u8 *actor, u8 *event, u8 command);',
                      (self.root/'conker/src/game_16DC80.c').read_text())
        functions,_,addresses = load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')
        self.assertEqual(addresses['func_151416E8'],screen.ENTRY)
        self.assertEqual(functions['func_151416E8'],self.retail)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream: rows = list(csv.DictReader(stream))
        self.assertEqual(len(rows),10785)
        self.assertFalse([row for row in rows if row['function']=='func_151416E8'])
        relocations = subprocess.run(['mips-linux-gnu-objdump','-r',str(self.output/'selected.o')],
                                     check=True,capture_output=True,text=True).stdout
        self.assertIn('00000004 R_MIPS_HI16       D_8008A02C',relocations)
        self.assertIn('00000008 R_MIPS_LO16       D_8008A02C',relocations)
        self.assertIn('000000b0 R_MIPS_26         func_1516972C',relocations)

    @classmethod
    def tearDownClass(cls):
        receipt = dict(cases=cls.cases,bodies=2,covered_words=[len(v) for v in cls.coverage],
                       sha256=hashlib.sha256(struct.pack('>55I',*cls.words)).hexdigest())
        (cls.output/'behavior.json').write_text(json.dumps(receipt,indent=2)+'\n')
        print('actor-event dispatch:',receipt)


def native_fixture():
    return r'''
typedef unsigned char u8;typedef signed char s8;typedef unsigned int u32;
typedef struct struct102 struct102;
#define NULL ((void *)0)
typedef void (*ActorEventCallback16DC80)(u8 *,u8 *,u8);
static ActorEventCallback16DC80 D_8008A02C[256];
static union {u32 alignment;u8 bytes[0x1C0];} actorStorage;
static u8 eventStorage[32],*actor=actorStorage.bytes,*event;
static u32 log[3][6];static int count,mutation;
static void record(u32 target,u8 *a,u8 *e,u8 c) {
    int n=count++;log[n][0]=target;log[n][1]=(u32)a;log[n][2]=(u32)e;
    log[n][3]=c;log[n][4]=a[0x168];log[n][5]=a[0x169];
}
static void actions(u8 *a,u8 *e,u8 c) {
    if(mutation==1) {a[0x168]=(u8)(c+1);e[0]=(u8)(c+1);a[0x169]=0x55;}
    else if(mutation==2) a[0x168]^=255;
    else if(mutation==3) e[0]=a[0x168]^255;
    else if(mutation==4) a[0x169]=0x81;
    else if(mutation==5) {D_8008A02C[a[0x168]]=NULL;*(u32 *)(a+4)=0xDEADBEEF;}
    else if(mutation==6) {a[0x168]=(u8)(a[0x168]+17);e[0]=a[0x168];}
    else if(mutation==7) e[0]=0;
}
static void callbackA(u8 *a,u8 *e,u8 c) {record(1,a,e,c);actions(a,e,c);}
static void callbackB(u8 *a,u8 *e,u8 c) {record(2,a,e,c);actions(a,e,c);}
void func_1516972C(struct102 *p) {
    u8 *a=(u8 *)p;record(3,a,NULL,0);*(u32 *)(a+4)=0x12345678;a[0x169]=0xE1;
}
static void initialize(int s,int c,int enabled,int match,int alias,int mutate) {
    int i;(void)c;mutation=mutate;count=0;
    for(i=0;i<0x1C0;i++) actor[i]=(u8)(i*13+7);
    for(i=0;i<32;i++) eventStorage[i]=(u8)(i*13+7);
    for(i=0;i<18;i++) ((u32 *)log)[i]=0;
    for(i=0;i<256;i++) D_8008A02C[i]=enabled==0?NULL:((i+enabled-1)&1)?callbackB:callbackA;
    actor[0x168]=(u8)s;event=alias==1?actor+0x168:alias==2?actor+0x169:alias==3?(u8 *)(D_8008A02C+s)+3:eventStorage;
    if(alias!=3) event[0]=(u8)(match?s:s^255);
}
static void reference(u8 *a,u8 *e,u8 c) {
    ActorEventCallback16DC80 first=D_8008A02C[a[0x168]];
    if(first) {ActorEventCallback16DC80 second=D_8008A02C[a[0x168]];second(a,e,c);}
    if(c!=0x22 && c!=0x24 && c!=0x25) return;
    if(e[0]!=a[0x168]) return;
    if(c==0x22) func_1516972C((struct102 *)a);
    else a[0x169]=(u8)(c==0x24?255:2);
}
'''


if __name__ == '__main__':
    unittest.main()
