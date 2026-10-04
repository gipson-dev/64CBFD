import csv
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools import match_progress
from tools.patch_generated_slice_ld import load_game_data_layout
from tools.tests import test_game_random_curve_record as curve


class GameDescriptorPositionWriterTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game_16EE20.c').read_text()
        def body(name, result):
            return re.search(result + r' ' + name + r'\([^;{}]+\) \{\n.*?\n\}',
                             source, re.S).group(0)
        cls.body = body('func_1514470C', 'void')
        cls.lookup = body('func_151423D8', 'f32')
        cls.spherical = body('func_151436B4', 'void')
        cls.types = ('typedef unsigned char u8; typedef short s16; typedef signed char s8; '
                     'typedef int s32; typedef unsigned int u32; typedef float f32;\n'
                     'typedef struct { f32 x,y,z; } vertex;\n#define NULL ((void *)0)\n')
        cls.declarations = '''
extern f32 D_800A56A0;
f32 func_150ADA68(void);
s32 func_150ADA20(void);
f32 func_151423D8(u8);
void func_151436B4(f32, f32, f32, vertex *);
'''
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        first, address, _, _ = load_game_data_layout(cls.root / 'conker')
        cls.period_word, = struct.unpack_from('>I', rom, first + 0x800A56A0 - address)
        table = struct.unpack_from('>65I', rom, first + 0x8009A220 - address)
        cls.common = cls.types + 'static const u32 tableBits[65]={' + ','.join(
            '0x%08Xu' % word for word in table) + '};\n' + r'''
f32 D_800A56A0, D_8009A220[65];
static union { u32 alignment; u8 bytes[0x40]; } descriptor;
static u32 outputWords[5];
static f32 samples[16], mathArguments[4];
static u32 integers[8];
static int floatCalls, integerCalls, lookupCalls, mathCalls, error;
static int mutateDescriptor, mutatePeriod, mutateMath;
static u8 angles[2];
static char trace[64];
static int traceLength;
static u32 bits(f32 value) { union { f32 f; u32 u; } v; v.f=value; return v.u; }
static f32 number(u32 value) { union { f32 f; u32 u; } v; v.u=value; return v.f; }
static void push(char c) { if(traceLength<63) trace[traceLength++]=c; else error=1; }
static int trace_is(const char *s) {
    int i=0;
    while(s[i]) { if(i>=traceLength || trace[i]!=s[i]) return 0; i++; }
    return i==traceLength;
}
static void put_center(s16 x,s16 y,s16 z) {
    *(s16 *)(descriptor.bytes+0)=x; *(s16 *)(descriptor.bytes+2)=y;
    *(s16 *)(descriptor.bytes+4)=z;
}
static void put_dimensions(s16 x,s16 y,s16 z) {
    *(s16 *)(descriptor.bytes+6)=x; *(s16 *)(descriptor.bytes+8)=y;
    *(s16 *)(descriptor.bytes+10)=z;
}
static void put_coefficients(f32 a,f32 b,f32 c,f32 d) {
    *(f32 *)(descriptor.bytes+0x24)=a; *(f32 *)(descriptor.bytes+0x28)=b;
    *(f32 *)(descriptor.bytes+0x2C)=c; *(f32 *)(descriptor.bytes+0x30)=d;
}
static void initialize(u8 flags) {
    int i;
    for(i=0;i<64;i++) descriptor.bytes[i]=0xA5;
    for(i=0;i<65;i++) D_8009A220[i]=number(tableBits[i]);
    for(i=0;i<5;i++) outputWords[i]=0xA5A5A5A5;
    for(i=0;i<16;i++) samples[i]=0;
    for(i=0;i<8;i++) integers[i]=0;
    samples[0]=0.25f; samples[1]=0.5f; samples[2]=0.75f;
    floatCalls=integerCalls=lookupCalls=mathCalls=error=traceLength=0;
    mutateDescriptor=mutatePeriod=mutateMath=0;
    D_800A56A0=number(0x40C90FDB);
    put_center(-100,200,-300); put_dimensions(8,12,4);
    put_coefficients(0,1,0,1); descriptor.bytes[0x15]=flags;
}
f32 func_150ADA68(void) {
    int i=floatCalls++;
    push('F');
    if(i>=16) { error=2; return 0; }
    if(mutateDescriptor && !i) {
        put_center(10,20,30); put_dimensions(100,100,100);
        put_coefficients(99,99,99,99); descriptor.bytes[0x15]=3;
    }
    if(mutatePeriod && i==2) D_800A56A0=8;
    return samples[i];
}
s32 func_150ADA20(void) {
    int i=integerCalls++;
    push('I');
    if(i>=8) { error=3; return 0; }
    return (s32)integers[i];
}
f32 cosf(f32 value) {
    int i=mathCalls++;
    push('C');
    if(i>=4 || (i!=0 && i!=2)) { error=4; return 0; }
    mathArguments[i]=value;
    if(mutateMath && !i) D_800A56A0=99;
    return i==0?2:5;
}
f32 sinf(f32 value) {
    int i=mathCalls++;
    push('S');
    if(i>=4 || (i!=1 && i!=3)) { error=5; return 0; }
    mathArguments[i]=value;
    return i==1?3:7;
}
static int output_is(f32 x,f32 y,f32 z) {
    return outputWords[0]==0xA5A5A5A5 && outputWords[4]==0xA5A5A5A5
        && outputWords[1]==bits(x) && outputWords[2]==bits(y) && outputWords[3]==bits(z);
}
static int nan_word(u32 word) { return (word&0x7F800000)==0x7F800000 && (word&0x7FFFFF)!=0; }
''' + cls.lookup.replace('f32 func_151423D8(u8 arg0) {',
            '''f32 func_151423D8(u8 arg0) {
    if(lookupCalls<2) angles[lookupCalls]=arg0; else error=6;
    lookupCalls++;
    push('L');''') + '\n' + cls.spherical + '\n' + cls.body + '\n'
        cls.fixture = cls.common

    def test_all_mode_and_flag_bytes_initialize_three_coordinates(self):
        self.run_host(r'''
int flags;
for(flags=0;flags<256;flags++) {
    initialize((u8)flags);
    func_1514470C(descriptor.bytes,outputWords+1);
    switch(flags&3) {
        case 0:
            if(!output_is(-100,206,-298) || floatCalls!=2 || integerCalls!=1
               || lookupCalls!=2 || mathCalls || angles[0]!=192 || angles[1]!=0
               || !trace_is("FILFL")) return 1;
            break;
        case 1:
            if(!output_is(-10,158,-240) || floatCalls!=3 || integerCalls || lookupCalls
               || mathCalls!=4 || !trace_is("FFFCSCS")) return 2;
            break;
        case 2:
            if(!output_is(-104,206,-298) || floatCalls!=3 || integerCalls || lookupCalls
               || mathCalls || !trace_is("FFF")) return 3;
            break;
        default:
            if(!output_is(-100,200,-300) || floatCalls || integerCalls || lookupCalls
               || mathCalls || traceLength) return 4;
    }
    if(error || descriptor.bytes[0x14]!=0xA5 || descriptor.bytes[0x16]!=0xA5) return 5;
}
''')

    def test_angular_byte_narrowing_and_quadrants_use_actual_lookup(self):
        self.run_host(r'''
static u32 words[]={0,64,128,192,256,320,384,448,0x80000000,0xFFFFFFC0};
static f32 x[]={-100,-98,-100,-102,-100,-98,-100,-102,-100,-102};
static f32 z[]={-298,-300,-302,-300,-298,-300,-302,-300,-298,-300};
int i;
for(i=0;i<10;i++) {
    initialize(0); integers[0]=words[i];
    func_1514470C(descriptor.bytes,outputWords+1);
    if(error || !output_is(x[i],206,z[i]) || angles[0]!=(u8)(words[i]-64)
       || angles[1]!=(u8)words[i] || !trace_is("FILFL")) return 1;
}
''')

    def test_signed_dimensions_negative_and_out_of_range_samples_are_not_clamped(self):
        self.run_host(r'''
initialize(2); put_dimensions(-32768,-123,-32768);
func_1514470C(descriptor.bytes,outputWords+1);
if(error || !output_is(16284,138.5f,-16684)) return 1;
initialize(2); samples[0]=-1; samples[1]=-2; samples[2]=1.5f;
func_1514470C(descriptor.bytes,outputWords+1);
if(error || !output_is(-124,176,-292)) return 2;
initialize(3); put_center(-32768,32767,-1);
func_1514470C(descriptor.bytes,outputWords+1);
if(error || !output_is(-32768,32767,-1) || traceLength) return 3;
''')

    def test_rotated_arithmetic_grouping_for_rectangular_and_radial_modes(self):
        self.run_host(r'''
initialize(2); put_coefficients(0.5f,-0.75f,1.5f,-0.25f);
func_1514470C(descriptor.bytes,outputWords+1);
if(error || !output_is(-96.75f,194.5f,-294.375f)) return 1;
initialize(0); put_coefficients(0.5f,-0.75f,1.5f,-0.25f); integers[0]=64;
func_1514470C(descriptor.bytes,outputWords+1);
if(error || !output_is(-96,195.5f,-303.75f)) return 2;
''')

    def test_dimensions_and_coefficients_snapshot_before_callbacks_bases_reload_after(self):
        self.run_host(r'''
initialize(2); mutateDescriptor=1;
func_1514470C(descriptor.bytes,outputWords+1);
if(error || !output_is(6,26,32) || !trace_is("FFF")) return 1;
initialize(0); mutateDescriptor=1;
func_1514470C(descriptor.bytes,outputWords+1);
if(error || !output_is(10,26,32) || !trace_is("FILFL")) return 2;
''')

    def test_spherical_period_load_is_after_third_sample_and_helper_is_actual_c(self):
        self.run_host(r'''
initialize(1); mutateDescriptor=mutatePeriod=mutateMath=1;
func_1514470C(descriptor.bytes,outputWords+1);
if(error || !output_is(100,-22,90) || !trace_is("FFFCSCS")
   || mathCalls!=4 || bits(mathArguments[0])!=bits(2) || bits(mathArguments[1])!=bits(2)
   || bits(mathArguments[2])!=bits(4) || bits(mathArguments[3])!=bits(4)
   || D_800A56A0!=99) return 1;
''')

    def test_nonfinite_samples_propagate_without_added_guards(self):
        self.run_host(r'''
initialize(2); samples[0]=number(0x7F800000);
func_1514470C(descriptor.bytes,outputWords+1);
if(error || outputWords[1]!=0x7F800000 || outputWords[2]!=bits(206)
   || !nan_word(outputWords[3]) || !trace_is("FFF")) return 1;
initialize(2); samples[0]=number(0x7FC12345);
func_1514470C(descriptor.bytes,outputWords+1);
if(error || !nan_word(outputWords[1]) || outputWords[2]!=bits(206)
   || !nan_word(outputWords[3]) || !trace_is("FFF")) return 2;
initialize(3); put_coefficients(number(0x7F800000),number(0x7FC12345),0,1);
func_1514470C(descriptor.bytes,outputWords+1);
if(error || !output_is(-100,200,-300) || traceLength) return 3;
''')

    def test_actual_weighted_emitter_position_chain_all_modes_failure_and_culling(self):
        source = (self.root / 'conker/src/game/generated_113D60.c').read_text()
        weighted = re.search(r'void func_150E8B1C\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';',
            source, re.S).group(0) for name in ('EventPayload113D60', 'WorldPosition113D60',
                                              'EventPositionPayload113D60', 'EventWeightNode113D60'))
        connection = layouts + r'''
f32 D_800BE9A4,D_800DCD90,D_800A1384,D_800A1388,D_800A138C;
s32 D_800BE9E8;
u8 *D_800DCDC4;
static union { u32 alignment; u8 bytes[80]; } parent,child;
static EventWeightNode113D60 node;
static f32 origin[3];
static int originCalls,allocations,copies,fail;
f32 *func_15144B34(s32 index) {
    push('O'); originCalls++;
    if(index!=7 || floatCalls) error=7;
    return origin;
}
void *func_15149130(s16 duration,s8 index,s8 kind,s8 source,u8 active,u8 mode,
                    s32 size,u8 slot,s32 context) {
    u32 last=integers[integerCalls-1];
    push('A'); allocations++;
    if(duration!=(s16)(last%13+5) || index!=-1 || kind!=0x34 || source!=-1
       || active!=1 || mode || size!=24 || slot!=0xC7 || context!=0x81) error=8;
    return fail?NULL:child.bytes;
}
void *memcpy(void *dst,const void *src,u32 size) {
    u8 *d=dst; const u8 *s=src; u32 i;
    push('M'); copies++;
    if(dst!=child.bytes+0x28 || size!=24) error=9;
    for(i=0;i<size;i++) d[i]=s[i];
    return dst;
}
''' + weighted + '\n'
        original = self.fixture
        try:
            self.fixture = self.common + connection
            self.run_host(r'''
static f32 x[]={-100,-10,-104,-100}, y[]={206,158,206,200}, z[]={-298,-240,-298,-300};
static int draws[]={4,5,5,2}, ints[]={2,1,1,1};
static const char *traces[]={"OFFFILFLIAM","OFFFFFCSCSIAM","OFFFFFIAM","OFFIAM"};
int mode,failed,i;
for(mode=0;mode<4;mode++) for(failed=0;failed<3;failed++) {
    EventPayload113D60 *state=(EventPayload113D60 *)(parent.bytes+0x28);
    EventPositionPayload113D60 *p=(EventPositionPayload113D60 *)(child.bytes+0x28);
    initialize((u8)mode); fail=failed==1; originCalls=allocations=copies=0;
    for(i=0;i<80;i++) parent.bytes[i]=child.bytes[i]=0xA5;
    state->field00=state->field04=0; state->field08=1.125f;
    parent.bytes[0xC]=0xC7; parent.bytes[1]=0x81;
    origin[0]=origin[1]=origin[2]=0; D_800BE9E8=7;
    D_800BE9A4=D_800DCD90=1;
    D_800A1384=number(0x3F85F40A); D_800A1388=number(0x3EA25D8D);
    D_800A138C=failed==2?1:3240000;
    node.descriptor=descriptor.bytes; node.weight=1; node.next=NULL;
    D_800DCDC4=(u8 *)&node;
    samples[0]=samples[1]=0; samples[2]=0.25f; samples[3]=0.5f; samples[4]=0.75f;
    integers[0]=mode==0?0x80000000:0xFFFFFFFF; integers[1]=0xFFFFFFFF;
    func_150E8B1C(parent.bytes);
    if(error || originCalls!=1 || allocations!=(failed!=2) || copies!=!failed
       || floatCalls!=draws[mode] || integerCalls!=ints[mode]-(failed==2)
       || bits(state->field08)!=bits(0.125f)) return 1;
    if(!failed) {
        if(!trace_is(traces[mode]) || bits(p->position.x)!=bits(x[mode])
           || bits(p->position.y)!=bits(y[mode]) || bits(p->position.z)!=bits(z[mode])
           || bits(p->parameters.field00)!=0x3EA25D8D
           || bits(p->parameters.field04)!=0x3F85F40A || bits(p->parameters.field08)) return 2;
    }
    for(i=0;i<80;i++) if((failed || i<0x28 || i>=0x40) && child.bytes[i]!=0xA5) return 3;
}
''')
        finally:
            self.fixture = original

    def test_retail_slot_helpers_and_no_new_instruction_guards(self):
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        words = struct.unpack('>218I', rom[0x171BBC:0x171F24])
        self.assertEqual((words[0], words[-2:]), (0x27BDFF68, (0x03E00008, 0x27BD0098)))
        self.assertEqual(self.period_word, 0x40C90FDB)
        self.assertIn('void func_1514470C(void *descriptor, void *position);',
                      (self.root / 'conker/src/game/generated_113D60.c').read_text())
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as source:
            self.assertFalse(any(row['function'] == 'func_1514470C'
                                 for row in csv.DictReader(source)))

    def test_existing_linked_helpers_and_selected_neighbors_are_raw_exact(self):
        production = self.root / 'conker/build/conker.us.elf'
        if not production.is_file() or not shutil.which('mips-linux-gnu-objdump'):
            self.skipTest('production ELF/objdump is required for existing-artifact audit')
        linked, _, addresses = match_progress.load_elf_functions(
            str(production), 'mips-linux-gnu-objdump')
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        for name, count in (('func_150E6ED8', 16), ('func_151423D8', 27),
                            ('func_151436B4', 34), ('func_15144598', 37),
                            ('func_15144A74', 13), ('func_15144AA8', 35),
                            ('func_15144B34', 13)):
            with self.subTest(function=name):
                self.assertEqual(len(linked[name]), count)
                first = 0x2D4B0 + addresses[name] - 0x15000000
                self.assertEqual(struct.pack('>' + str(count) + 'I', *linked[name]),
                                 rom[first:first + count * 4])

    def test_ido_semantic_body_fits_complete_retail_allocation(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or any(shutil.which(n) is None for n in
                ('mips-linux-gnu-ld', 'mips-linux-gnu-objcopy')):
            self.skipTest('IDO/MIPS tools are unavailable')
        source, obj, elf, binary, script = (self.path / ('position' + suffix)
                                           for suffix in ('.c', '.o', '.elf', '.bin', '.ld'))
        source.write_text(self.types + self.declarations + self.body + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
            '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3',
            '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        script.write_text('SECTIONS { .text 0x1514470C : SUBALIGN(4) { *(.text) } }\n')
        targets = {'D_800A56A0': 0x800A56A0, 'func_150ADA68': 0x150ADA68,
                   'func_150ADA20': 0x150ADA20, 'func_151423D8': 0x151423D8,
                   'func_151436B4': 0x151436B4}
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_1514470C',
            *(f'--defsym={name}=0x{value:X}' for name, value in targets.items()),
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', '.text', str(elf), str(binary)],
                       check=True, capture_output=True)
        data = binary.read_bytes()
        words = struct.unpack('>' + 'I' * (len(data) // 4), data)
        count = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        self.assertEqual(count, 179)
        self.assertEqual(data[count * 4:], bytes(len(data) - count * 4))
        frame = 0x10000 - (words[0] & 0xFFFF)
        self.assertEqual(frame, 0x78)
        retail = struct.unpack('>218I', (self.root / 'conker/conker.us.bin').read_bytes()[0x171BBC:0x171F24])
        padded = words[:count] + (0,) * (218 - count)
        differences = sum(a != b for a, b in zip(padded, retail))
        self.assertEqual(differences, 196)
        production = self.root / 'conker/build/conker.us.elf'
        if production.is_file() and shutil.which('mips-linux-gnu-objdump'):
            linked, _, addresses = match_progress.load_elf_functions(
                str(production), 'mips-linux-gnu-objdump')
            self.assertEqual(addresses['func_1514470C'], 0x1514470C)
            self.assertEqual(tuple(linked['func_1514470C']), padded)
        print('descriptor position writer slot:', {'body_words': count, 'slot_words': 218,
              'frame_bytes': frame, 'different_words': differences})


if __name__ == '__main__':
    unittest.main()
