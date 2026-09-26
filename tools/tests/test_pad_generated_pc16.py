"""Cross-body branches must follow retail padding rather than compact offsets."""
from pathlib import Path
import shutil, struct, subprocess, sys, tempfile, unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from pad_generated_object import emit_padded_assembly, parse_object

class PaddedPc16Tests(unittest.TestCase):
    def test_branch_target_moves_with_padded_function(self):
        for tool in ('mips-linux-gnu-as','mips-linux-gnu-ld','mips-linux-gnu-objcopy'):
            if not shutil.which(tool):self.skipTest(tool+' required')
        with tempfile.TemporaryDirectory() as tmp:
            work=Path(tmp)
            (work/'compact.s').write_text('''
.section .text,"ax"
.set noreorder
.globl first
.type first,@function
first:
.reloc .,R_MIPS_PC16,second
.word 0x1000ffff
nop
.size first,.-first
.globl second
.type second,@function
second:
jr $ra
nop
.size second,.-second
''')
            (work/'retail.s').write_text('''
glabel first
/* 000000 15000000 1000000F */ b second
/* 000004 15000004 00000000 */ nop
glabel second
/* 000040 15000040 03E00008 */ jr $ra
/* 000044 15000044 00000000 */ nop
''')
            def run(*args):subprocess.run(args,cwd=work,check=True,capture_output=True)
            run('mips-linux-gnu-as','-EB','-march=vr4300','-o','compact.o','compact.s')
            (work/'padded.s').write_text(emit_padded_assembly(work/'compact.o',work/'retail.s'))
            run('mips-linux-gnu-as','-EB','-march=vr4300','-o','padded.o','padded.s')
            run('mips-linux-gnu-ld','-Ttext','0x15000000','-e','first','-o','linked.elf','padded.o')
            run('mips-linux-gnu-objcopy','-O','binary','-j','.text','linked.elf','text.bin')
            text=(work/'text.bin').read_bytes()
            self.assertEqual(struct.unpack_from('>I',text)[0],0x1000000f)
            self.assertEqual(struct.unpack_from('>I',text,0x40)[0],0x03e00008)

    def test_guarded_word_replacement(self):
        if not shutil.which('mips-linux-gnu-as'):
            self.skipTest('mips-linux-gnu-as required')
        with tempfile.TemporaryDirectory() as tmp:
            work=Path(tmp)
            (work/'compact.s').write_text('''
.section .text,"ax"
.set noreorder
.globl sample
.type sample,@function
sample:
.word 0x00851021
jr $ra
nop
.size sample,.-sample
''')
            (work/'retail.s').write_text('''
glabel sample
/* 000000 15000000 00A41021 */ addu $v0,$a1,$a0
/* 000004 15000004 03E00008 */ jr $ra
/* 000008 15000008 00000000 */ nop
''')
            (work/'patches.csv').write_text(
                'filename,function,offset,expected,replacement,'
                'expected_relocations,replacement_relocations,note,insert_after\n'
                'fixture,sample,0x0,0x00851021,0x00A41021,-,-,swap operands,\n'
            )
            subprocess.run(
                ['mips-linux-gnu-as','-EB','-march=vr4300','-o','compact.o','compact.s'],
                cwd=work,check=True,capture_output=True
            )
            padded=emit_padded_assembly(
                work/'compact.o',work/'retail.s',
                word_patches_path=work/'patches.csv',filename='fixture'
            )
            self.assertIn('.word 0x00A41021',padded)
            (work/'patches.csv').write_text(
                'filename,function,offset,expected,replacement,'
                'expected_relocations,replacement_relocations,note,insert_after\n'
                'fixture,sample,0x0,0x00000000,0x00A41021,-,-,stale guard,\n'
            )
            with self.assertRaisesRegex(ValueError, 'stale word patch'):
                emit_padded_assembly(
                    work/'compact.o',work/'retail.s',
                    word_patches_path=work/'patches.csv',filename='fixture'
                )

    def test_guarded_word_insertion(self):
        if not shutil.which('mips-linux-gnu-as'):
            self.skipTest('mips-linux-gnu-as required')
        with tempfile.TemporaryDirectory() as tmp:
            work=Path(tmp)
            (work/'compact.s').write_text('''
.section .text,"ax"
.set noreorder
.globl sample
.type sample,@function
sample:
addiu $a0,$a0,1
jr $ra
nop
.size sample,.-sample
.globl next_sample
.type next_sample,@function
next_sample:
jr $ra
nop
.size next_sample,.-next_sample
''')
            (work/'retail.s').write_text('''
glabel sample
/* 000000 15000000 24840001 */ addiu $a0,$a0,1
jlabel inserted_label
/* 000004 15000004 00801025 */ move $v0,$a0
/* 000008 15000008 03E00008 */ jr $ra
/* 00000C 1500000C 00000000 */ nop
glabel next_sample
/* 000010 15000010 03E00008 */ jr $ra
/* 000014 15000014 00000000 */ nop
''')
            (work/'patches.csv').write_text(
                'filename,function,offset,expected,replacement,'
                'expected_relocations,replacement_relocations,note,insert_after\n'
                'fixture,sample,0x0,0x24840001,0x24840001,-,-,'
                'retain result pointer,0x00801025\n'
            )
            subprocess.run(
                ['mips-linux-gnu-as','-EB','-march=vr4300','-o','compact.o','compact.s'],
                cwd=work,check=True,capture_output=True
            )
            padded=emit_padded_assembly(
                work/'compact.o',work/'retail.s',
                word_patches_path=work/'patches.csv',filename='fixture'
            )
            self.assertLess(
                padded.index('inserted_label:'),
                padded.index('.word 0x00801025')
            )
            (work/'padded.s').write_text(padded)
            subprocess.run(
                ['mips-linux-gnu-as','-EB','-march=vr4300','-o','padded.o','padded.s'],
                cwd=work,check=True,capture_output=True
            )
            text,functions,_=parse_object(work/'padded.o')
            start=functions['sample']['value']
            self.assertEqual(functions['sample']['size'],0x10)
            self.assertEqual(struct.unpack_from('>I',text,start+4)[0],0x00801025)
            self.assertEqual(functions['next_sample']['value'],start+0x10)

            (work/'retail-tight.s').write_text('''
glabel sample
/* 000000 15000000 24840001 */ addiu $a0,$a0,1
/* 000004 15000004 03E00008 */ jr $ra
/* 000008 15000008 00000000 */ nop
glabel next_sample
/* 00000C 1500000C 03E00008 */ jr $ra
/* 000010 15000010 00000000 */ nop
''')
            with self.assertRaisesRegex(ValueError, 'patched sample is 0x10'):
                emit_padded_assembly(
                    work/'compact.o',work/'retail-tight.s',
                    word_patches_path=work/'patches.csv',filename='fixture'
                )

if __name__=='__main__':unittest.main()
