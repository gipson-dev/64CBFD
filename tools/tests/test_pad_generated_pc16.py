"""Cross-body branches must follow retail padding rather than compact offsets."""
from pathlib import Path
import shutil, struct, subprocess, sys, tempfile, unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from pad_generated_object import emit_padded_assembly

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

if __name__=='__main__':unittest.main()
