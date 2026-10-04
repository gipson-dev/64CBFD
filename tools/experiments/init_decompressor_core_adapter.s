/* Experimental original a0/a1/a2 entry; extra stack ownership is unproven. */
.set noreorder
.set noat
.option pic0
.ifdef INIT_DECODE_TIGHT_ADAPTER
.ifndef INIT_DECODE_ABI_FPR_SHADOW
.error "tight adapter requires ABI FPR shadow"
.endif
.ifndef INIT_DECODE_CORE_PRESERVES_CALLEE
.error "tight adapter requires callee-preserving core"
.endif
.section .text.init_decode_adapter,"ax",@progbits
.balign 4
.else
.text
.endif
.macro publish_fpr reg, offset
.ifdef INIT_DECODE_DIRECT_FPR_LOADS
    lwc1 \reg, \offset($sp)
.else
    lw $t0, \offset($sp)
    mtc1 $t0, \reg
.endif
.endm
.ifdef INIT_DECODE_ABI_FPR_SHADOW
.equ ADAPTER_EXTRA, 0x98
.else
.equ ADAPTER_EXTRA, 0x48
.endif
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
    addiu $sp, $sp, -ADAPTER_EXTRA
    sw $a2, 0x10($sp)
    sw $a0, 0x20($sp)
    sw $a1, 0x24($sp)
    sw $a2, 0x28($sp)
.ifndef INIT_DECODE_CORE_OWNS_STATE
    sw $zero, 0x2C($sp)
    sw $zero, 0x30($sp)
    sw $zero, 0x34($sp)
    sw $zero, 0x38($sp)
    sw $zero, 0x3C($sp)
.endif
    sw $t0, 0x40($sp)
.ifndef INIT_DECODE_CORE_OWNS_STATE
    sw $a2, 0x44($sp)
.endif
    move $a2, $a0
    move $a3, $a1
    lui $a1, 0x8004
    addiu $a1, $a1, -0x4170
    jal init_decode_core
     addiu $a0, $sp, 0x20
.ifdef INIT_DECODE_ABI_FPR_SHADOW
    lw $t0, 0x90($sp)
    beq $t0, $zero, .Labi_no_fpr_snapshot
.ifdef INIT_DECODE_TIGHT_ADAPTER
     lw $ra, 0xA80+ADAPTER_EXTRA($sp)
.else
     nop
.endif
    publish_fpr $f0, 0x60
    publish_fpr $f1, 0x64
    publish_fpr $f2, 0x68
    publish_fpr $f3, 0x6C
    publish_fpr $f4, 0x70
    publish_fpr $f5, 0x74
    publish_fpr $f6, 0x78
    publish_fpr $f7, 0x7C
    publish_fpr $f8, 0x80
    publish_fpr $f9, 0x84
    publish_fpr $f10, 0x88
    publish_fpr $f11, 0x8C
.Labi_no_fpr_snapshot:
.endif
    publish_fpr $f16, 0x24
    publish_fpr $f17, 0x34
    publish_fpr $f18, 0x38
    publish_fpr $f19, 0x3C
.ifndef INIT_DECODE_TIGHT_ADAPTER
    addiu $sp, $sp, ADAPTER_EXTRA
.endif
.ifndef INIT_DECODE_CORE_PRESERVES_CALLEE
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
.endif
.ifdef INIT_DECODE_TIGHT_ADAPTER
    jr $ra
     addiu $sp, $sp, 0xA88+ADAPTER_EXTRA
.else
    lw $ra, 0xA80($sp)
    jr $ra
     addiu $sp, $sp, 0xA88
.endif
.globl init_decode_retail_core_adapter_end
init_decode_retail_core_adapter_end:
.end init_decode_retail_core_adapter
