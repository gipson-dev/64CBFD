"""Direct shape-measure matching, signed/wrapped dimensions and ordered float work."""

import itertools
import json
import re
import struct
import tempfile
import unittest
from pathlib import Path

from tools.check_game_data_layout import load_section
from tools.experiments import game_shape_volume_candidates as screen
from tools.match_progress import load_elf_functions
from tools.tests.game_animation_timeline_oracle import bits, floating, signed
from tools.tests.test_game_actor_triangle_transform_match import TriangleOracle, put
from tools.tests.test_game_table_range_loader import STACK
from tools.tests import test_game_random_curve_record as native

DESCRIPTOR = 0x20000
VALUES = (-32768, -32767, -100, -1, 0, 1, 100, 32767)
FLAGS = (0, 1, 2, 3, 252, 253, 254, 255)
SYNTHETIC = ((0x3F000000, 0xC0000000), (0, 0x80000000),
             (0xBF000000, 0x4B000000), (0x3F800000, 0x3F800000), (0x40490FDA, 0x40860A92))


def memory_case(width, height, depth, flags, coefficients):
    memory = {STACK + i: 0xA5 for i in range(-0x600, 0x100)}
    memory.update({DESCRIPTOR + i: 0xA5 for i in range(-8, 48)})
    for offset, value in ((6, width), (8, height), (10, depth)):
        put(memory, DESCRIPTOR + offset, value & 65535, 2)
    put(memory, DESCRIPTOR + 21, flags, 1)
    for address, value in zip(screen.SYMBOLS.values(), coefficients):
        put(memory, address, value)
    return memory


def reference(width, height, depth, flags, coefficients):
    kind = flags & 3
    reads = [('R', DESCRIPTOR + 21, 1, flags)]
    def dimension(offset, value):
        reads.append(('R', DESCRIPTOR + offset, 2, value & 65535))
    if kind == 2:
        for offset, value in ((6, width), (8, height), (10, depth)):
            dimension(offset, value)
        value = bits(float(signed((width * height * depth) & 0xFFFFFFFF)))
    elif kind == 0:
        dimension(6, width)
        dimension(8, height)
        reads.append(('R', 0x800A5698, 4, coefficients[0]))
        square = floating(bits(float(width * width)))
        scaled = floating(bits(square * floating(coefficients[0])))
        value = bits(scaled * float(height))
    elif kind == 1:
        dimension(6, width)
        reads.append(('R', 0x800A569C, 4, coefficients[1]))
        scaled = floating(bits(float(width) * floating(coefficients[1])))
        square = floating(bits(scaled * float(width)))
        value = bits(square * float(width))
    else:
        value = 0x3F800000
    return value, reads


class VolumeOracle(TriangleOracle):
    def __init__(self, words, memory, phase=0):
        super().__init__(words, memory, phase=phase, entry=screen.ENTRY, arguments=(DESCRIPTOR,))

    def record_call(self, target):
        raise AssertionError('shape measure unexpectedly calls a helper')


class GameShapeVolumeMatchTests(unittest.TestCase):
    run_host = native.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.output = cls.root / 'conker/build/game-shape-volume-test'
        cls.output.mkdir(exist_ok=True)
        cls.record, cls.words = screen.compile_candidate(cls.root, cls.output, 'selected')
        cls.alternate_body = dict(screen.candidates())['box-6-8-0xA-cylinder-right']
        _, cls.alternate = screen.compile_candidate(cls.root, cls.output, 'alternate', cls.alternate_body)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = list(struct.unpack_from('>56I', rom, screen.ROM))
        cls.coefficients = struct.unpack_from('>2I', rom, 0x2275E0 + 0x800A5698 - 0x80082B20)
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.descriptor = re.search(r'typedef struct \{[^{}]*\} struct134;',
                                  (cls.root / 'conker/include/structs.h').read_text()).group()
        cls.fixture = ('typedef unsigned char u8;typedef short s16;typedef unsigned short u16;'
                       'typedef int s32;typedef unsigned int u32;typedef float f32;\n' + cls.descriptor + '\n'
                       'f32 D_800A5698,D_800A569C;\n' + screen.SELECTED + r'''
static u32 word(f32 f) {union {u32 u;f32 f;} v;v.f=f;return v.u;}
static f32 number(u32 u) {union {u32 u;f32 f;} v;v.u=u;return v.f;}
static f32 expected(s32 w,s32 h,s32 d,u8 flags) {
    volatile f32 first,second;
    u32 product;
    switch(flags&3) {
        case 2: product=(u32)w*(u32)h;product*=(u32)d;return (f32)(s32)product;
        case 0: first=(f32)(w*w)*D_800A5698;return first*(f32)h;
        case 1: first=(f32)w*D_800A569C;second=first*(f32)w;return second*(f32)w;
        default:return 1.0f;
    }
}
static int verify(s32 w,s32 h,s32 d,u8 flags,u32 c0,u32 c1) {
    struct134 descriptor;
    u8 before[sizeof(descriptor)],*bytes=(u8 *)&descriptor;
    u32 i,got,wanted;
    for(i=0;i<sizeof(descriptor);i++) bytes[i]=0xA5;
    descriptor.unk6=(u16)w;descriptor.unk8=(u16)h;descriptor.unkA=(u16)d;bytes[21]=flags;
    for(i=0;i<sizeof(descriptor);i++) before[i]=bytes[i];
    D_800A5698=number(c0);D_800A569C=number(c1);
    wanted=word(expected(w,h,d,flags));got=word(func_1514462C(&descriptor));
    if(got!=wanted) return 1;
    for(i=0;i<sizeof(descriptor);i++) if(bytes[i]!=before[i]) return 2;
    return 0;
}
''')

    def test_direct_compiler_identity_and_bounded_inventory(self):
        self.assertEqual(self.words, self.retail)
        self.assertEqual((self.record['body_words'], self.record['frame'], self.record['differences'],
                          self.record['diagnostics']), (56, 0, 0, ''))
        forms = screen.candidates()
        self.assertEqual((len(forms), len(dict(forms))), (12, 12))
        exact = []
        for name, body in forms:
            record, words = screen.compile_candidate(self.root, self.output, name, body)
            self.assertEqual((record['body_words'], record['frame'], record['diagnostics']), (56, 0, ''))
            if record['exact']:
                exact.append(name)
                self.assertEqual(words, self.retail)
        self.assertEqual(exact, ['box-8-0xA-6-cylinder-left'])

    def test_retail_coefficients_and_real_descriptor_layout(self):
        address, data = load_section(self.root / 'conker/build/conker.us.elf', '.game_data')
        self.assertEqual(struct.unpack_from('>2I', data, 0x800A5698 - address), self.coefficients)
        self.assertTrue(all(0 < floating(c) < 5 for c in self.coefficients))
        self.run_host(r'''
if(sizeof(struct134)!=40 || __builtin_offsetof(struct134,unk6)!=6
   || __builtin_offsetof(struct134,unk8)!=8 || __builtin_offsetof(struct134,unkA)!=10
   || __builtin_offsetof(struct134,unk14)!=20) return 1;
''')

    def test_guest_values_reads_footprints_flags_and_reachable_coverage(self):
        cases, alternate_trace_differences, coverage = 0, 0, set()
        corpora = (
            ((w,h,d,f,self.coefficients) for w,h,d,f in itertools.product(VALUES,VALUES,VALUES,FLAGS)),
            ((w,h,d,f,self.coefficients) for f,w,(h,d) in
             itertools.product(range(256),VALUES,((1,32767),(-32768,-1)))),
            ((w,h,d,f,c) for c,w,h,d,f in
             itertools.product(SYNTHETIC,VALUES,(-32768,-1,0,32767),(-32768,-1,0,32767),range(4))))
        for w,h,d,flags,coefficients in itertools.chain(*corpora):
            memory = memory_case(w,h,d,flags,coefficients)
            wanted, trace = reference(w,h,d,flags,coefficients)
            for phase in (0,8):
                for words in (self.retail,self.words,self.alternate):
                    model = VolumeOracle(words,memory,phase).run()
                    self.assertEqual(model.f[0],wanted)
                    self.assertEqual(model.memory,memory)
                    self.assertEqual(model.calls,[])
                    if words is self.alternate:
                        alternate_trace_differences += model.events != trace
                    else:
                        self.assertEqual(model.events,trace)
                    if words is self.retail:
                        coverage.update(model.visits)
                cases += 1
        self.assertEqual(cases,21504)
        self.assertEqual(alternate_trace_differences,5376)
        unreachable = screen.ENTRY + 24*4
        self.assertEqual(coverage,set(range(screen.ENTRY,screen.ENTRY+224,4))-{unreachable})
        self.assertEqual(self.retail[24],0x84820006)
        self.assertEqual(self.retail[3],0x51C00015)
        self.assertEqual(self.retail[22],0x1000001E)
        (self.output/'behavior.json').write_text(json.dumps(dict(cases=cases,models=3,
            reachable_words=len(coverage),unreachable_word=hex(unreachable),
            alternate_trace_differences=alternate_trace_differences,coefficients=self.coefficients),indent=2)+'\n')

    def test_native_actual_c_full_storage_and_ordered_float_math(self):
        pairs = [self.coefficients,*SYNTHETIC]
        self.run_host('static u32 coefficients[6][2]={' + ','.join('{0x%Xu,0x%Xu}' % p for p in pairs) + r'''};
static s32 values[]={-32768,-32767,-100,-1,0,1,100,32767};
static u8 flags[]={0,1,2,3,252,253,254,255};
static s32 shortValues[]={-32768,-1,0,32767};
int w,h,d,f,c,k,cases=0;
for(w=0;w<8;w++) for(h=0;h<8;h++) for(d=0;d<8;d++) for(f=0;f<8;f++) {
    if(verify(values[w],values[h],values[d],flags[f],coefficients[0][0],coefficients[0][1])) return 1;
    cases++;
}
for(f=0;f<256;f++) for(w=0;w<8;w++) for(k=0;k<2;k++) {
    if(verify(values[w],k?-32768:1,k?-1:32767,(u8)f,coefficients[0][0],coefficients[0][1])) return 2;
    cases++;
}
for(c=1;c<6;c++) for(w=0;w<8;w++) for(h=0;h<4;h++) for(d=0;d<4;d++) for(f=0;f<4;f++) {
    if(verify(values[w],shortValues[h],shortValues[d],(u8)f,coefficients[c][0],coefficients[c][1])) return 3;
    cases++;
}
if(cases!=10752) return 4;
''')

    def test_false_stub_unsigned_dimensions_unmasked_flags_and_float_box_are_detected(self):
        box = '(s32)((u32)*(s16 *)(record + 8) * (u32)*(s16 *)(record + 0xA) * (u32)*(s16 *)(record + 6))'
        negatives = (
            ('float-box',screen.SELECTED.replace(box,'(f32)*(s16 *)(record + 6) * *(s16 *)(record + 8) * *(s16 *)(record + 0xA)'),(32767,32767,32767,2)),
            ('unsigned-dimensions',screen.SELECTED.replace('*(s16 *)','*(u16 *)'),(-1,100,100,1)),
            ('unmasked-flags',screen.SELECTED.replace('record[0x15] & 3','record[0x15]'),(100,100,100,252)),
            ('zero-stub','f32 func_1514462C(struct134 *arg0) { return 0.0f; }',(1,1,1,3)))
        for name,body,case in negatives:
            _,words=screen.compile_candidate(self.root,self.output,name,body)
            memory=memory_case(*case,self.coefficients)
            wanted,_=reference(*case,self.coefficients)
            self.assertNotEqual(VolumeOracle(words,memory).run().f[0],wanted,name)

    def test_production_slot_source_header_and_no_guards(self):
        source=(self.root/'conker/src/game_16EE20.c').read_text()
        self.assertEqual(re.search(r'^f32 func_1514462C\([^;{]+\) \{\n.*?\n\}',source,re.M|re.S).group(),screen.SELECTED)
        self.assertIn('f32  func_1514462C(struct134 *arg0);',(self.root/'conker/include/functions.h').read_text())
        variables = (self.root / 'conker/include/variables.h').read_text()
        self.assertIn('extern f32 D_800A5698;', variables)
        self.assertIn('extern f32 D_800A569C;', variables)
        self.assertNotIn(',func_1514462C,',(self.root/'conker/retail_word_patches.us.csv').read_text())
        functions=load_elf_functions(str(self.root/'conker/build/conker.us.elf'),'mips-linux-gnu-objdump')[0]
        self.assertEqual(functions['func_1514462C'],self.retail)


if __name__=='__main__':
    unittest.main()
