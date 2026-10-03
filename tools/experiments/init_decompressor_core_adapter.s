/* Experimental original a0/a1/a2 entry; extra stack ownership is unproven. */
.set noreorder
.set noat
.option pic0
.text
.globl init_decode_retail_core_adapter
.ent init_decode_retail_core_adapter
init_decode_retail_core_adapter:
    addiu $sp, $sp, -0xA88
    sw $s0, 0xA48($sp)
    sw $s1, 0xA4C($sp)
    sw $s2, 0xA50($sp)
    sw $s3, 0xA54($sp)
    sw $s4, 0xA58($sp)
    sw $s5, 0xA5C($sp)
    sw $s6, 0xA60($sp)
    sw $s7, 0xA64($sp)
    sw $fp, 0xA78($sp)
    sw $gp, 0xA7C($sp)
    sw $ra, 0xA80($sp)
    move $t0, $sp
    addiu $sp, $sp, -0x48
    sw $a2, 0x10($sp)
    sw $a0, 0x20($sp)
    sw $a1, 0x24($sp)
    sw $a2, 0x28($sp)
    sw $zero, 0x2C($sp)
    sw $zero, 0x30($sp)
    sw $zero, 0x34($sp)
    sw $zero, 0x38($sp)
    sw $zero, 0x3C($sp)
    sw $t0, 0x40($sp)
    sw $a2, 0x44($sp)
    move $a2, $a0
    move $a3, $a1
    lui $a1, 0x8004
    addiu $a1, $a1, -0x4170
    jal init_decode_core
     addiu $a0, $sp, 0x20
    lw $t0, 0x24($sp)
    mtc1 $t0, $f16
    lw $t0, 0x34($sp)
    mtc1 $t0, $f17
    lw $t0, 0x38($sp)
    mtc1 $t0, $f18
    lw $t0, 0x3C($sp)
    mtc1 $t0, $f19
    addiu $sp, $sp, 0x48
    lw $s0, 0xA48($sp)
    lw $s1, 0xA4C($sp)
    lw $s2, 0xA50($sp)
    lw $s3, 0xA54($sp)
    lw $s4, 0xA58($sp)
    lw $s5, 0xA5C($sp)
    lw $s6, 0xA60($sp)
    lw $s7, 0xA64($sp)
    lw $fp, 0xA78($sp)
    lw $gp, 0xA7C($sp)
    lw $ra, 0xA80($sp)
    jr $ra
     addiu $sp, $sp, 0xA88
.globl init_decode_retail_core_adapter_end
init_decode_retail_core_adapter_end:
.end init_decode_retail_core_adapter
