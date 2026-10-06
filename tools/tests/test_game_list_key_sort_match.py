"""Stable linked sorting, captured links, bounded preconditions and word guards."""

import csv
import itertools
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.experiments import game_list_key_sort_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

GUARDS = (
    (0x068,0x8FAF0030,0x8FB90030),(0x078,0x8CA70008,0x8CA80008),
    (0x090,0x00E04025,0x01003825),(0x0BC,0xACC70008,0xACC80008),
    (0x0C0,0x8CA70008,0x8CA80008),(0x0C4,0x50E00004,0x51000004),
    (0x0C8,0x8C470008,0x8C4F0008),(0x0D0,0xACF80004,0xAD180004),
    (0x0D4,0x8C470008,0x8C4F0008),(0x0D8,0x10E00002,0x11E00002),
    (0x0DC,0xACA70008,0xACAF0008),(0x0E0,0xACE50004,0xADE50004),
    (0x0FC,0x1500FFDB,0x14E0FFDB),(0x100,0x01002825,0x00E02825),
    (0x104,0x8FAF0030,0x8FB90030),(0x108,0x8FB90030,0x8FAB0030),
    (0x110,0xAC6F0000,0xAC790000),(0x114,0xAF200004,0xAD600004))


def read(memory,address,size=4):
    return int.from_bytes(bytes(memory[address+i] for i in range(size)),'big')


def key(kind,value):
    return (kind<<8)+((value if value<0x80000000 else value-0x100000000)>>16)


def fields(index,length,pattern):
    halves=(index,length-index,index%3,0,(index*37)%7,(index*32769+32768)&65535,
            (index*7919)&32767,(index%2)*256)
    kinds=(0,0,0,0,0,128,(index*43)&255,1-index%2)
    return kinds[pattern],(halves[pattern]<<16)|((index*11+9)&65535)


def memory_case(length,pattern,column,row):
    memory={STACK+i:0xA5 for i in range(-0x600,0x100)}
    memory.update({screen.TABLE+i:(i*13+7)&255 for i in range(0x340)})
    nodes=[0x20000+i*0x120 for i in range(length)]
    for index,node in enumerate(nodes):
        memory.update({node+i:(index*29+i*13+7)&255 for i in range(0x120)})
        kind,value=fields(index,length,pattern)
        put(memory,node+4,nodes[index-1] if index else 0)
        put(memory,node+8,nodes[index+1] if index+1<length else 0)
        put(memory,node+0x18,kind,1);put(memory,node+0x20,value)
    slot=screen.TABLE+row*0x1A0+column*4
    put(memory,slot,nodes[0])
    return memory,nodes,slot


def reference(memory,nodes,slot):
    wanted=dict(memory)
    values={node:key(read(memory,node+0x18,1),read(memory,node+0x20)) for node in nodes}
    assert all(value>=0 for value in values.values())
    ordered=sorted(nodes,key=values.__getitem__)
    put(wanted,slot,ordered[0])
    for index,node in enumerate(ordered):
        put(wanted,node+4,ordered[index-1] if index else 0)
        put(wanted,node+8,ordered[index+1] if index+1<len(ordered) else 0)
    return wanted


def external(memory):
    return {a:v for a,v in memory.items() if not STACK-0x600<=a<STACK+0x100}


class Fault(Exception):
    pass


class SortOracle(TriangleOracle):
    def get(self,address,size):
        if any(address+i not in self.memory for i in range(size)):
            raise Fault('read',address,size)
        return super().get(address,size)

    def put(self,address,value,size):
        if self.recording and any(address+i not in self.memory for i in range(size)):
            raise Fault('write',address,size)
        super().put(address,value,size)


class GameListKeySortMatchTests(unittest.TestCase):
    run_host=native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root=Path(__file__).resolve().parents[2]
        cls.output=cls.root/'conker/build/game-list-key-sort-test';cls.output.mkdir(exist_ok=True)
        cls.record,cls.words=screen.compile_candidate(cls.root,cls.output,'selected')
        cls.retail=list(struct.unpack_from('>73I',(cls.root/'conker/conker.us.bin').read_bytes(),screen.ROM))
        cls.directory=tempfile.TemporaryDirectory();cls.addClassCleanup(cls.directory.cleanup)
        cls.path=Path(cls.directory.name)

    def test_complete_shape_and_closed_register_lifetimes(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences'],self.record['diagnostics']),
                         (72,0x138,18,''))
        normalized=self.words+[0]
        for offset,expected,replacement in GUARDS:
            self.assertEqual(self.words[offset//4],expected)
            self.assertEqual(self.retail[offset//4],replacement)
            mapping=({15:25} if offset in (0x68,0x104,0x110) else {25:11} if offset in (0x108,0x114)
                     else {7:15} if offset in (0xC8,0xD4,0xD8,0xDC,0xE0) else {7:8,8:7})
            rewritten=expected
            for shift in (21,16,11) if expected>>26==0 else (21,16):
                register=expected>>shift&31
                rewritten=(rewritten&~(31<<shift))|(mapping.get(register,register)<<shift)
            self.assertEqual(rewritten,replacement,(hex(offset),mapping))
            normalized[offset//4]=replacement
        self.assertEqual(normalized,self.retail)
        self.assertEqual(sum(a==b for a,b in zip(self.words+[0],self.retail)),55)

    def test_full_guest_storage_stability_keys_tables_tokens_and_traces(self):
        count,coverage=0,set()
        for length,pattern,column,row,token,phase in itertools.product(
                range(1,13),range(8),(0,27,28,86,103),(0,1),(0,0x12345678,0xFFFFFFFF),(0,8)):
            memory,nodes,slot=memory_case(length,pattern,column,row)
            wanted=reference(memory,nodes,slot)
            models=[SortOracle(body,memory,entry=screen.ENTRY,arguments=(token,column,row,0x12340000),phase=phase).run()
                    for body in (self.words,self.retail)]
            for model in models:
                self.assertEqual(external(model.memory),external(wanted),(count,length,pattern))
                self.assertEqual(model.r[2],token);self.assertEqual(model.calls,[])
                coverage.update(model.visits)
            traces=[[event for event in model.events if not STACK-0x600<=event[1]<STACK+0x100] for model in models]
            self.assertEqual(*traces)
            count+=1
        self.assertEqual((count,len(coverage)),(5760,69))
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=count,bodies=2,covered_words=len(coverage)),indent=2)+'\n')

    def test_all_nonzero_bypass_halfwords_no_external_access(self):
        coverage=set()
        for bypass in range(1,65536):
            memory={STACK+i:0xA5 for i in range(-0x140,0x20)}
            for body in (self.words,self.retail):
                model=SortOracle(body,memory,entry=screen.ENTRY,
                    arguments=(0x12345678,0xFFFFFFFF,0x80000000,0x12340000|bypass),phase=bypass&8).run()
                self.assertEqual(model.r[2],0x12345678)
                self.assertFalse([e for e in model.events if not STACK-0x600<=e[1]<STACK+0x100])
                coverage.update(model.visits)
        self.assertEqual(len(coverage),10)

    def test_retail_preconditions_empty_head_and_negative_sentinel_walk(self):
        memory,nodes,slot=memory_case(2,0,28,0)
        empty=dict(memory);put(empty,slot,0)
        for body in (self.words,self.retail):
            with self.assertRaises(Fault) as caught:
                SortOracle(body,empty,entry=screen.ENTRY,arguments=(7,28,0,0)).run()
            self.assertEqual(caught.exception.args,('write',4,4))
        negative=dict(memory);put(negative,nodes[0]+0x20,1<<16);put(negative,nodes[1]+0x20,0xFFFF0000)
        for body in (self.words,self.retail):
            with self.assertRaises(Fault) as caught:
                SortOracle(body,negative,entry=screen.ENTRY,arguments=(7,28,0,0)).run()
            self.assertEqual(caught.exception.args,('read',0xA5A5A5BD,1))

    def test_twenty_four_compiler_controls(self):
        expected={'selected':((72,312,18),(72,312,26),(102,304,102),(101,304,100)),
            'inner-for':((72,312,18),(72,312,26),(100,304,100),(99,304,98)),
            'outer-for':((72,312,18),(72,312,26),(100,304,100),(99,304,98)),
            'loop-local':((73,312,27),(72,312,26),(102,304,102),(101,304,100)),
            'next-local':((73,312,27),(72,312,26),(102,304,102),(101,304,100)),
            'small-node':((72,88,21),(72,88,27),(102,80,102),(101,80,100))}
        for name,body,declarations in screen.candidates():
            for index,profile in enumerate(screen.PROFILES):
                record,_=screen.compile_candidate(self.root,self.output,name+'-'+profile,body,profile,declarations)
                self.assertEqual((record['body_words'],record['frame'],record['differences']),expected[name][index])
                self.assertEqual(record['diagnostics'],'')

    def test_eight_compiled_negatives_change_real_storage_or_return(self):
        negatives=[('stub','s32 func_151406AC(s32 token,u32 column,u32 row,s16 bypass) { return 0; }'),
            ('descending',screen.SELECTED.replace('key >= otherKey','key <= otherKey')),
            ('unstable',screen.SELECTED.replace('key >= otherKey','key > otherKey')),
            ('unsigned-value',screen.SELECTED.replace('current->value >> 16','(u32)current->value >> 16').replace(
                                                   'head->value >> 16','(u32)head->value >> 16')),
            ('head-prev',screen.SELECTED.replace('    dummy.next->prev = NULL;\n','')),
            ('successor-prev',screen.SELECTED.replace('                            temporary->prev = current->prev;\n','')),
            ('row-stride',screen.SELECTED.replace('row * 0x1A0','row * 0x19C')),
            ('word-bypass',screen.SELECTED.replace('s16 bypass','s32 bypass'))]
        for name,body in negatives:
            _,words=screen.compile_candidate(self.root,self.output,'negative-'+name,body)
            found=False
            for pattern,row in itertools.product((7,1,5,0,2,3,4,6),(0,1)):
                memory,nodes,slot=memory_case(6,pattern,28,row)
                if name=='row-stride':put(memory,slot-4,nodes[0])
                wanted=reference(memory,nodes,slot)
                try:model=SortOracle(words,memory,entry=screen.ENTRY,arguments=(0x12345678,28,row,0x12340000)).run()
                except Fault as error:
                    if name=='descending':
                        self.assertEqual(error.args,('read',0xA5A5A5BD,1));found=True
                    else:raise
                else:found=external(model.memory)!=external(wanted) or model.r[2]!=0x12345678
                if found:break
            self.assertTrue(found,name)

    def test_native_full_storage_halfword_value_sweep_and_bypass(self):
        self.fixture='''typedef unsigned char u8;typedef short s16;typedef int s32;typedef unsigned int u32;
#define NULL ((void *)0)
'''+screen.DECLARATIONS+screen.SELECTED+r'''
u8 D_800DCE50[0x340] __attribute__((aligned(4)));
static union {u32 align;u8 bytes[12*0x120];} storage;
static u8 wanted[12*0x120],tableWanted[0x340];
static u32 order[12],count,slotOffset;
static void word(u8 *p,u32 value) {*(u32 *)p=value;}
static u32 get(u8 *p) {return *(u32 *)p;}
static s32 value_key(u8 *p) {return ((s32)p[0x18]<<8)+((s32)get(p+0x20)>>16);}
static void initialize(u32 n,u32 pattern,u32 column,u32 row) {
    u32 i,j,halves[8],kinds[8];count=n;slotOffset=row*0x1A0+column*4;
    for(i=0;i<sizeof(storage.bytes);i++) storage.bytes[i]=(u8)(i*13+7);
    for(i=0;i<sizeof(D_800DCE50);i++) D_800DCE50[i]=(u8)(i*13+7);
    for(i=0;i<n;i++) {
        u8 *node=storage.bytes+i*0x120;
        halves[0]=i;halves[1]=n-i;halves[2]=i%3;halves[3]=0;halves[4]=(i*37)%7;
        halves[5]=(i*32769+32768)&65535;halves[6]=(i*7919)&32767;halves[7]=(i%2)*256;
        for(j=0;j<8;j++) kinds[j]=0;
        kinds[5]=128;kinds[6]=(i*43)&255;kinds[7]=1-i%2;
        word(node+4,i?(u32)(node-0x120):0);word(node+8,i+1<n?(u32)(node+0x120):0);
        node[0x18]=(u8)kinds[pattern];word(node+0x20,(halves[pattern]<<16)|((i*11+9)&65535));
    }
    word(D_800DCE50+slotOffset,(u32)storage.bytes);
}
static void compute_reference(void) {
    u32 i,j,best,tmp;
    for(i=0;i<sizeof(wanted);i++) wanted[i]=storage.bytes[i];
    for(i=0;i<sizeof(tableWanted);i++) tableWanted[i]=D_800DCE50[i];
    for(i=0;i<count;i++) order[i]=i;
    for(i=0;i<count;i++) {
        best=i;
        for(j=i+1;j<count;j++) {
            s32 left=value_key(wanted+order[j]*0x120),right=value_key(wanted+order[best]*0x120);
            if(left<right || (left==right && order[j]<order[best])) best=j;
        }
        tmp=order[i];order[i]=order[best];order[best]=tmp;
    }
    word(tableWanted+slotOffset,(u32)(storage.bytes+order[0]*0x120));
    for(i=0;i<count;i++) {
        u8 *node=wanted+order[i]*0x120;
        word(node+4,i?(u32)(storage.bytes+order[i-1]*0x120):0);
        word(node+8,i+1<count?(u32)(storage.bytes+order[i+1]*0x120):0);
    }
}
static int verify(void) {
    u32 i;for(i=0;i<sizeof(wanted);i++) if(wanted[i]!=storage.bytes[i]) return 1;
    for(i=0;i<sizeof(tableWanted);i++) if(tableWanted[i]!=D_800DCE50[i]) return 2;
    return 0;
}
'''
        self.run_host(r'''
u32 n,p,c,r,v,token,cases=0;static u32 columns[]={0,27,28,86,103};
if(sizeof(void *)!=4 || sizeof(s16)!=2 || sizeof(SortNode169510)!=0x110) return 20;
if((u32)&((SortNode169510 *)storage.bytes)->kind-(u32)storage.bytes!=0x18) return 21;
if((u32)&((SortNode169510 *)storage.bytes)->value-(u32)storage.bytes!=0x20) return 22;
for(n=1;n<=12;n++) for(p=0;p<8;p++) for(c=0;c<5;c++) for(r=0;r<2;r++) {
    initialize(n,p,columns[c],r);compute_reference();token=0x80000000u+n+p+c+r;
    if((u32)func_151406AC((s32)token,columns[c],r,0)!=token || verify()) return 23;
    cases++;
}
if(cases!=960) return 24;
for(v=0;v<65536;v++) {
    initialize(2,0,28,0);storage.bytes[0x18]=storage.bytes[0x120+0x18]=128;
    word(storage.bytes+0x20,0);word(storage.bytes+0x120+0x20,(v<<16)|((v*13+7)&65535));
    compute_reference();if(func_151406AC(7,28,0,0)!=7 || verify()) return 25;
}
initialize(2,1,28,0);
for(c=0;c<sizeof(wanted);c++) wanted[c]=storage.bytes[c];
for(c=0;c<sizeof(tableWanted);c++) tableWanted[c]=D_800DCE50[c];
for(v=1;v<65536;v++) {
    token=0x80000000u+v;
    if((u32)func_151406AC((s32)token,0xFFFFFFFF,0x80000000,(s16)v)!=token || verify()) return 26;
}
''')

    def test_production_source_complete_slot_guards_and_callback_tables(self):
        source=(self.root/'conker/src/game_169510.c').read_text()
        self.assertIn(screen.SELECTED,source)
        self.assertIn(screen.DECLARATIONS.split('extern')[0].strip(),source)
        self.assertIn('s32 func_151406AC(s32 token, u32 column, u32 row, s16 bypass);',source)
        production=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        self.assertEqual(production['func_151406AC'],self.retail)
        with (self.root/'conker/retail_word_patches.us.csv').open(newline='') as stream:rows=list(csv.DictReader(stream))
        guards=[r for r in rows if r['function']=='func_151406AC']
        self.assertEqual((len(rows),len(guards)),(10738,18))
        for guard,(offset,expected,replacement) in zip(guards,GUARDS):
            self.assertEqual(guard['filename'],'game_169510')
            self.assertEqual(tuple(int(guard[k],16) for k in ('offset','expected','replacement')),(offset,expected,replacement))
            self.assertEqual((guard['expected_relocations'],guard['replacement_relocations'],guard['omit']),('-','-','false'))
            self.assertEqual((guard['insert_after'],guard['insert_after_relocations']),('',''))
        rom=(self.root/'conker/conker.us.bin').read_bytes()
        self.assertEqual(struct.unpack_from('>I',rom,0x23052C)[0],screen.ENTRY)
        self.assertEqual(struct.unpack_from('>I',rom,0x2310F4)[0],screen.ENTRY)
        self.assertEqual(tuple((a-0x8008B4A8)//0x34 for a in (0x8008BA6C,0x8008C634)),(28,86))


if __name__=='__main__':
    unittest.main()
