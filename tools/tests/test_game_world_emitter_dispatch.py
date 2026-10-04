import hashlib
import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests import test_game_random_curve_record as curve


class GameWorldEmitterDispatchTests(unittest.TestCase):
    run_host = curve.GameRandomCurveRecordTests.run_host

    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        source = (cls.root / 'conker/src/game/generated_113D60.c').read_text()
        cls.body = re.search(r'void func_150E81A8\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.layouts = '\n'.join(re.search(r'typedef struct ' + name + r' \{.*?\} ' + name + ';',
            source, re.S).group(0) for name in
            ('WorldPosition113D60', 'WorldEmitterDescriptor113D60', 'RandomPacket113D60'))
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        cls.types = ('typedef signed char s8; typedef unsigned char u8; typedef short s16; '
                     'typedef int s32; typedef unsigned int u32; typedef float f32;\n')
        cls.declarations = '''
extern WorldPosition113D60 D_800A1290[8];
extern f32 D_800A1354, D_800A1358, D_800A135C, D_800A1360, D_800A1364;
void func_151D3FF4(WorldPosition113D60 *, u8, s32);
void func_1514FCE8(WorldEmitterDescriptor113D60 *, u8, s32);
s32 func_150ADA20(void);
s32 func_151D8868(void *, s32, s32, s32);
'''
        rom = (cls.root / 'conker/conker.us.bin').read_bytes()
        cls.retail = rom[0x115658:0x11585C]
        cls.position_words = struct.unpack('>24I', rom[0x245D50:0x245DB0])
        values = ','.join('0x%08XU' % word for word in cls.position_words)
        cls.fixture = cls.types + cls.layouts + cls.declarations + (
            'static const u32 positions[24] = {' + values + '};\n') + r'''
WorldPosition113D60 D_800A1290[8];
f32 D_800A1354, D_800A1358, D_800A135C, D_800A1360, D_800A1364;
static WorldPosition113D60 expected, seen;
static u32 randomWord;
static u8 expectedSlot;
static s32 expectedContext;
static int stage, error, mutate, integerCalls;
static u32 bits(f32 value) { union { f32 f; u32 u; } w; w.f=value; return w.u; }
static f32 number(u32 value) { union { f32 f; u32 u; } w; w.u=value; return w.f; }
void func_151D3FF4(WorldPosition113D60 *p, u8 slot, s32 context) {
    if(stage!=0 || slot!=expectedSlot || context!=expectedContext
       || bits(p->x)!=bits(expected.x) || bits(p->y)!=bits(expected.y)
       || bits(p->z)!=bits(expected.z)) error=1;
    if(mutate) {
        p->x=13.5f; p->y=-87.25f; p->z=2000.0f;
        D_800A1290[4].x=999; D_800A1290[5].y=999;
        D_800A1290[6].z=999; D_800A1290[7].x=999;
        D_800A1354=123; D_800A1358=456;
        D_800A135C=-0.25f; D_800A1360=0.5f; D_800A1364=-0.75f;
    }
    seen=*p;
    stage=1;
}
void func_1514FCE8(WorldEmitterDescriptor113D60 *d, u8 slot, s32 context) {
    if(stage!=1 || slot!=expectedSlot || context!=expectedContext
       || d->field00!=0 || d->field02!=255 || d->field04!=-64 || d->field06!=77
       || d->field08!=10 || d->field0C!=5
       || bits(d->position.x)!=bits(seen.x) || bits(d->position.y)!=bits(seen.y)
       || bits(d->position.z)!=bits(seen.z)
       || d->field1C!=252 || d->field20!=117 || d->field24!=308 || d->field28!=256
       || bits(d->field2C)!=bits(D_800A1354) || bits(d->field30)!=bits(D_800A1358)
       || d->field34!=4 || d->field38!=7 || d->field3C!=27
       || bits(d->field40)!=bits(D_800A135C) || bits(d->field44)!=bits(D_800A1360)
       || bits(d->field48)!=bits(D_800A1364)
       || d->field4C!=25 || d->field4E!=15 || d->field50!=100 || d->field52!=100
       || d->field54!=12 || d->field56!=20 || d->field58!=0) error=2;
    stage=2;
}
s32 func_150ADA20(void) {
    if(stage!=2 || integerCalls) error=3;
    integerCalls++;
    stage=3;
    return (s32)randomWord;
}
s32 func_151D8868(void *data, s32 a, s32 b, s32 c) {
    RandomPacket113D60 *p=data;
    if(stage!=3 || integerCalls!=1 || a || b!=255 || c
       || p->kind!=1 || p->duration!=(s16)(randomWord%11+30)
       || p->count!=8 || p->mode!=1 || p->index!=-1) error=4;
    stage=4;
    return -123;
}
static void initialize(u8 index, u8 slot, s32 context, u32 word) {
    int i;
    for(i=0;i<8;i++) {
        D_800A1290[i].x=number(positions[i*3]);
        D_800A1290[i].y=number(positions[i*3+1]);
        D_800A1290[i].z=number(positions[i*3+2]);
    }
    if(index<8) { expected=D_800A1290[index]; expected.y+=200; }
    D_800A1354=number(0x442EC000); D_800A1358=number(0x43FF8000);
    D_800A135C=number(0x3F483128); D_800A1360=number(0xBF6E147C);
    D_800A1364=number(0x3F3AE148);
    randomWord=word; expectedSlot=slot; expectedContext=context;
    stage=error=mutate=integerCalls=0;
}
''' + cls.body + '\n'

    def test_all_selector_bytes_and_argument_truncation(self):
        self.run_host(r'''
int i, slot=0x1A5;
for(i=0;i<1024;i++) {
    u8 index=(u8)i;
    initialize(index,0xA5,(s32)0xFEDCBA98,0xFFFFFFFFU);
    func_150E81A8(i,slot,(s32)0xFEDCBA98);
    if(error || stage!=((index>=4 && index<=7)?4:0)
       || integerCalls!=((index>=4 && index<=7)?1:0)) return 1;
}
''')

    def test_unsigned_random_remainders_and_full_context(self):
        self.run_host(r'''
static u32 words[]={0,1,9,10,11,12,21,22,0x7FFFFFFF,0x80000000,0x80000001,0xFFFFFFFE,0xFFFFFFFF};
static s32 contexts[]={0,1,-1,(s32)0x80000000,0x7FFFFFFF};
int index,i,c;
for(index=4;index<8;index++) for(i=0;i<13;i++) for(c=0;c<5;c++) {
    initialize(index,0xFF,contexts[c],words[i]);
    func_150E81A8(index,0xFF,contexts[c]);
    if(error || stage!=4 || integerCalls!=1) return 1;
}
''')

    def test_position_snapshot_and_post_helper_constant_loads(self):
        self.run_host(r'''
int index;
for(index=4;index<8;index++) {
    initialize(index,0xD5,(s32)0xAABBCCDD,0x80000001); mutate=1;
    func_150E81A8(index,0xD5,(s32)0xAABBCCDD);
    if(error || stage!=4 || integerCalls!=1) return 1;
}
''')

    def test_layout_offsets_and_consumer_extent(self):
        self.run_host(r'''
#define OFFSET(type,field) ((u32)&((type *)0)->field)
if(sizeof(WorldPosition113D60)!=12 || sizeof(WorldEmitterDescriptor113D60)!=0x5C
   || OFFSET(WorldEmitterDescriptor113D60,position)!=0x10
   || OFFSET(WorldEmitterDescriptor113D60,field2C)!=0x2C
   || OFFSET(WorldEmitterDescriptor113D60,field4C)!=0x4C
   || OFFSET(WorldEmitterDescriptor113D60,field58)!=0x58
   || OFFSET(WorldEmitterDescriptor113D60,pad59)!=0x59
   || sizeof(RandomPacket113D60)!=8) return 1;
''')
        source = (self.root / 'conker/asm/17CAF0.s').read_text()
        body = source.split('glabel func_1514FCE8\n', 1)[1].split('endlabel func_1514FCE8', 1)[0]
        self.assertIn('lb         $t3, 0x58($s0)', body)
        self.assertNotRegex(body, r'(?:lb|lbu|lh|lw|lwc1)\s+\$\w+, 0x(?:59|5A|5B)\(\$s0\)')

    def test_retail_slot_call_sequence_and_discarded_return(self):
        self.assertEqual(hashlib.sha256(self.retail).hexdigest(),
                         'b0e576afb054d463f65658487256ecaf1f667576948aa0d7906745b150e01a02')
        calls = [((0x150E81A8+i*4+4)&0xF0000000)|((word&0x3FFFFFF)<<2)
                 for i, (word,) in enumerate(struct.iter_unpack('>I', self.retail)) if word>>26==3]
        self.assertEqual(calls, [0x151D3FF4, 0x1514FCE8, 0x150ADA20, 0x151D8868])
        rom = (self.root / 'conker/conker.us.bin').read_bytes()
        self.assertEqual(struct.unpack_from('>4I', rom, 0xCAB88),
                         (0x0D43A06A, 0x24060001, 0x10000022, 0x8FA200C4))
        self.assertNotIn('descriptor.pad59', self.body)
        self.assertNotIn('packet.pad1', self.body)
        self.assertNotIn('packet.pad7', self.body)

    def test_ido_complete_slot_direct_match(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file() or shutil.which('mips-linux-gnu-ld') is None:
            self.skipTest('IDO/MIPS tools are unavailable')
        source, obj, elf, binary, script = (self.path / ('dispatch' + suffix)
                                          for suffix in ('.c', '.o', '.elf', '.bin', '.ld'))
        source.write_text(self.types + self.layouts + self.declarations + self.body + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn', '-Xcpluscomm',
            '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul', '-mips2', '-o32', '-O2', '-g3',
            '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        targets = {'D_800A1290':0x800A1290, 'func_151D3FF4':0x151D3FF4,
                   'func_1514FCE8':0x1514FCE8, 'func_150ADA20':0x150ADA20,
                   'func_151D8868':0x151D8868, **{name:int(name[2:],16) for name in
                   ('D_800A1354','D_800A1358','D_800A135C','D_800A1360','D_800A1364')}}
        script.write_text('SECTIONS { .text 0x150E81A8 : SUBALIGN(4) { *(.text) } }\n')
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script),
            '-e', 'func_150E81A8', *(f'--defsym={name}=0x{address:X}' for name,address in targets.items()),
            '-o', str(elf), str(obj)], check=True, capture_output=True)
        subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', '.text', str(elf), str(binary)],
                       check=True, capture_output=True)
        words = list(struct.unpack('>'+'I'*(binary.stat().st_size//4), binary.read_bytes()))
        end = max(i for i,word in enumerate(words) if word==0x03E00008)+2
        retail = list(struct.unpack('>129I', self.retail))
        differences = sum(a!=b for a,b in zip(words[:end],retail))+abs(end-len(retail))
        print('world emitter slot:', {'words':end, 'retail_words':129, 'different_positions':differences})
        self.assertEqual(end,129)
        self.assertEqual(words[:end],retail)


if __name__ == '__main__':
    unittest.main()
