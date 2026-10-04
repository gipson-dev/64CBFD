.set noat
.set noreorder
.section .text.glyph_adapter,"ax"
.globl init_glyph_writer_adapter
init_glyph_writer_adapter:
    addiu $sp, $sp, -56
    sw $v0, 16($sp)
    sw $v1, 20($sp)
    sw $a0, 24($sp)
    sw $a1, 28($sp)
    sw $t0, 32($sp)
    sw $t2, 36($sp)
    sw $t4, 40($sp)
    sw $t9, 44($sp)
    sw $ra, 48($sp)
    or $a0, $t1, $zero
    or $a1, $t2, $zero
    or $a2, $t3, $zero
    or $a3, $t4, $zero
    jal init_glyph_writer
    nop
    or $t1, $v0, $zero
    or $a2, $zero, $zero
    or $a3, $zero, $zero
    lw $v0, 16($sp)
    lw $v1, 20($sp)
    lw $a0, 24($sp)
    lw $a1, 28($sp)
    lw $t0, 32($sp)
    lw $t2, 36($sp)
    lw $t4, 40($sp)
    lw $t9, 44($sp)
    lw $ra, 48($sp)
    jr $ra
    addiu $sp, $sp, 56
