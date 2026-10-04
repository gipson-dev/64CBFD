import re
import shutil
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.tests import test_game_positioned_emitter_descriptor as positioned
from tools.tests import test_game_random_dispatch as dispatch


class GameRandomEdgeEmitterTests(unittest.TestCase):
    run_host = positioned.GamePositionedEmitterDescriptorTests.run_host

    @classmethod
    def setUpClass(cls):
        positioned.GamePositionedEmitterDescriptorTests.setUpClass()
        cls.addClassCleanup(positioned.GamePositionedEmitterDescriptorTests.doClassCleanups)
        base = positioned.GamePositionedEmitterDescriptorTests
        cls.root, cls.types, cls.layouts = base.root, base.types, base.layouts
        cls.positioned_body = base.body
        cls.directory = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.directory.cleanup)
        cls.path = Path(cls.directory.name)
        source = (cls.root / 'conker/src/game/generated_113D60.c').read_text()
        cls.body = re.search(r's32 func_150E76D0\([^;{}]+\) \{\n.*?\n\}', source, re.S).group(0)
        cls.fixture = base.fixture.replace(base.body, cls.body).replace('captured.kind==4', 'captured.kind==5')
        callbacks = r'''
s32 D_80088A68[3],D_80088A74[3];
static u32 randoms[2];
static f32 fraction;
static int integerCalls,floatCalls,changeTables,error;
s32 func_150ADA20(void) {
    int i=integerCalls++;
    if(i>=2) { error=1; return 0; }
    if(changeTables==1 && i==1) {
        D_80088A68[0]=D_80088A68[1]=D_80088A68[2]=0xEE;
        D_80088A74[0]=D_80088A74[1]=D_80088A74[2]=0xDD;
    }
    return (s32)randoms[i];
}
f32 func_150ADA68(void) {
    floatCalls++;
    if(integerCalls!=2 || floatCalls!=1) error=2;
    if(changeTables==2) {
        D_80088A68[0]=D_80088A68[1]=D_80088A68[2]=0xCC;
        D_80088A74[0]=D_80088A74[1]=D_80088A74[2]=0xBB;
    }
    return fraction;
}
'''
        cls.fixture = cls.fixture.replace('u8 D_80088A64;', 'u8 D_80088A64;\n' + callbacks, 1)
        cls.fixture = cls.fixture.replace('calls=mutate=0; result=123;', r'''
calls=mutate=0; result=123;
D_80088A68[0]=72; D_80088A68[1]=73; D_80088A68[2]=74;
D_80088A74[0]=69; D_80088A74[1]=70; D_80088A74[2]=71;
randoms[0]=randoms[1]=0; fraction=0.25f;
integerCalls=floatCalls=changeTables=error=0;
''')

    def test_four_variants_unsigned_selection_and_positions(self):
        self.run_host(r'''
static u32 selectors[]={0,1,2,0x80000000,0xFFFFFFFE,0xFFFFFFFF};
static f32 fractions[]={0,0.25f,0.5f,0.75f,1,-1,2};
int v,j,k;
for(v=0;v<4;v++) for(j=0;j<6;j++) for(k=0;k<7;k++) {
    f32 x,y;
    initialize(); randoms[0]=0xFFFFFFFCu|v; randoms[1]=selectors[j]; fraction=fractions[k];
    if(func_150E76D0(2.5f,-123,0xFF,0xAB,0x156,0x18001,0xFFFF,pair,-7,0xCD,(s32)0x87654321)!=123) return 1;
    if(error || integerCalls!=2 || floatCalls!=1 || calls!=1 || !constants_match()) return 2;
    x=v<2 ? (v==0 ? 142.5f : -142.5f) : fractions[k]*260-130;
    y=v<2 ? fractions[k]*160-80 : (v==2 ? 107.5f : -107.5f);
    if(captured.position.x!=x || captured.position.y!=y || captured.scale[0]!=2.5f || captured.scale[1]!=2.5f) return 3;
    if(captured.tag!=(u8)((v<2?72:69)+selectors[j]%3) || captured.flags!=(0xF9|(v==0?2:v==2?4:0))) return 4;
    if(captured.id!=-123 || captured.duration!=0xAB || captured.opacity!=0x56
       || captured.size0!=(s16)0x8001 || captured.size1!=-1 || capturedPair!=pair) return 5;
    if(args[0] || args[1]!=-7 || args[2] || args[3]!=0xCD || args[4]!=(s32)0x87654321) return 6;
}
''')

    def test_snapshot_before_rng_and_tag_before_float_callback(self):
        self.run_host(r'''
int v,m;
for(v=0;v<4;v++) for(m=1;m<=2;m++) {
    initialize(); randoms[0]=v; randoms[1]=2; changeTables=m;
    func_150E76D0(3,500,9,100,255,64,3,pair,2,7,8);
    if(error || captured.tag!=(v<2?74:71) || captured.scale[0]!=3 || captured.scale[1]!=3) return 1;
    if(integerCalls!=2 || floatCalls!=1 || calls!=1) return 2;
}
''')

    def test_return_handles_narrowing_and_null_pair(self):
        self.run_host(r'''
static s32 results[]={0,1,-1,(s32)0x80000000};
static s32 values[]={0,-1,255,256,32767,32768,65535,65536};
int i,j;
for(i=0;i<4;i++) for(j=0;j<8;j++) {
    initialize(); result=results[i]; randoms[0]=1;
    if(func_150E76D0(-0.5f,(s16)values[j],(u8)values[j],(u8)values[j],values[j],values[j],values[j],0,0,0,0)!=result) return 1;
    if(captured.id!=(s16)values[j] || captured.flags!=((u8)values[j]&0xF9)
       || captured.duration!=(u8)values[j] || captured.opacity!=(u8)values[j]
       || captured.size0!=(s16)values[j] || captured.size1!=(s16)values[j]
       || capturedPair || !constants_match() || calls!=1) return 2;
}
''')

    def test_dispatcher_both_paths_use_actual_helpers(self):
        case = dispatch.GameRandomDispatchTests
        case.setUpClass()
        try:
            test = case('test_positioned_path_all_flags_unsigned_remainders_and_tail')
            fixture = re.sub(r's32 func_150E76D0\([^;{}]+\) \{.*?\n\}', self.body,
                             test.fixture, count=1, flags=re.S)
            self.assertNotEqual(fixture, test.fixture)
            fixture = re.sub(r's32 func_150E75A0\([^;{}]+\) \{.*?\n\}', self.positioned_body,
                             fixture, count=1, flags=re.S)
            self.assertIn(self.positioned_body, fixture)
            declarations = ('extern s32 D_80088A68[3],D_80088A74[3]; extern u8 D_80088A64;\n'
                            's32 func_1515548C(void *,s32,s32 *,s32,s32,u8,s32);\n')
            submit = r'''
s32 D_80088A68[3]={72,73,74},D_80088A74[3]={69,70,71};
u8 D_80088A64;
static u8 capturedTag;
s32 func_1515548C(void *data,s32 arg1,s32 *choices,s32 mode,s32 arg4,u8 slot,s32 context) {
    EmitterDescriptor113D60 *d=data;
    if(d->kind==4) { push('P'); positionCalls++; }
    else { push('A'); alternateCalls++; }
    capturedScale=d->scale[0]; capturedTag=d->tag;
    capturedPosition[0]=d->position.x; capturedPosition[1]=d->position.y;
    if(arg1 || arg4 || (d->kind!=4 && d->kind!=5) || d->scale[1]!=capturedScale) error=7;
    capture(d->id,(u8)d->flags,d->duration,d->opacity,d->size0,d->size1,choices,mode,slot,context);
    return -1;
}
'''
            test.fixture = test.types + self.layouts + '\n' + declarations + fixture[len(test.types):] + submit
            test.run_host(r'''
int v;
for(v=0;v<4;v++) {
    initialize(); samples[1]=0.875f; words[2]=v; words[3]=2;
    func_150E7290(0x23,0xAB,(s32)0x87654321);
    if(check_common(4) || alternateCalls!=1 || positionCalls || integers!=6 || floats!=4) return 1;
    if(capturedScale!=350 || captured[1]!=(9|(v==0?2:v==2?4:0)) || captured[2]!=(s32)(words[1]%26+100)) return 2;
    if(!trace_equals("FFFIIIIFASEIIT")) return 3;
    if(capturedTag!=(v<2?74:71)) return 4;
}
initialize(); D_80088A64=0xA7;
func_150E7290(0x23,0xAB,(s32)0x87654321);
if(check_common(4) || positionCalls!=1 || alternateCalls || captured[1]!=(9|2|0x40)) return 5;
if(capturedScale!=550 || capturedTag!=0xA7 || !trace_equals("FFFFFIIIIPSEIIT")) return 6;
''')
        finally:
            case.doClassCleanups()

    def test_independent_ido_body_and_call_targets(self):
        compiler = self.root / 'ido/ido5.3_recomp/cc'
        if not compiler.is_file():
            self.skipTest('IDO is unavailable')
        for tool in ('mips-linux-gnu-ld', 'mips-linux-gnu-objcopy'):
            if shutil.which(tool) is None:
                self.skipTest(tool + ' is unavailable')
        source, obj = self.path / 'edge.c', self.path / 'edge.o'
        source.write_text(self.types + self.layouts + '\n'
            'extern s32 D_80088A68[3],D_80088A74[3]; s32 func_150ADA20(void); f32 func_150ADA68(void);\n'
            's32 func_1515548C(void *,s32,s32 *,s32,s32,u8,s32);\n' + self.body + '\n')
        result = subprocess.run([str(compiler), '-c', '-32', '-G', '0', '-Xfullwarn',
            '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared', '-Wab,-r4300_mul',
            '-mips2', '-o32', '-O2', '-g3', '-o', str(obj), str(source)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout + result.stderr, '')
        elf, binary, script = (self.path / ('edge' + suffix) for suffix in ('.elf', '.bin', '.ld'))
        script.write_text('SECTIONS { .text 0x150E76D0 : SUBALIGN(4) { *(.text) } }\n')
        subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip', '-T', str(script), '-e', 'func_150E76D0',
            '--defsym=D_80088A68=0x80088A68', '--defsym=D_80088A74=0x80088A74',
            '--defsym=func_150ADA20=0x150ADA20', '--defsym=func_150ADA68=0x150ADA68',
            '--defsym=func_1515548C=0x1515548C', '-o', str(elf), str(obj)], check=True, capture_output=True)
        subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary', '-j', '.text', str(elf), str(binary)],
                       check=True, capture_output=True)
        words = list(struct.unpack('>' + 'I' * (binary.stat().st_size // 4), binary.read_bytes()))
        end = max(i for i, word in enumerate(words) if word == 0x03E00008) + 2
        self.assertLessEqual(end, 177)
        targets = [0x10000000 | ((word & 0x3FFFFFF) << 2) for word in words[:end] if word >> 26 == 3]
        self.assertEqual(targets.count(0x150ADA20), 3)
        self.assertEqual(targets.count(0x150ADA68), 2)
        self.assertEqual(targets.count(0x1515548C), 1)
        self.assertEqual(len(targets), 6)


if __name__ == '__main__':
    unittest.main()
