glabel func_151A2960
    /* 1CFE10 151A2960 27BDFFE0 */  addiu      $sp, $sp, -0x20
    /* 1CFE14 151A2964 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 1CFE18 151A2968 AFA50024 */  sw         $a1, 0x24($sp)
    /* 1CFE1C 151A296C 8486001A */  lh         $a2, 0x1A($a0)
    /* 1CFE20 151A2970 848E00B0 */  lh         $t6, 0xB0($a0)
    /* 1CFE24 151A2974 3C19800C */  lui        $t9, %hi(D_800BE616)
    /* 1CFE28 151A2978 248200B0 */  addiu      $v0, $a0, 0xB0
    /* 1CFE2C 151A297C 00CE082A */  slt        $at, $a2, $t6
    /* 1CFE30 151A2980 10200006 */  beqz       $at, .L151A299C
    /* 1CFE34 151A2984 00000000 */   nop
    /* 1CFE38 151A2988 848F00B2 */  lh         $t7, 0xB2($a0)
    /* 1CFE3C 151A298C 00CF0019 */  multu      $a2, $t7
    /* 1CFE40 151A2990 0000C012 */  mflo       $t8
    /* 1CFE44 151A2994 A098002C */  sb         $t8, 0x2C($a0)
    /* 1CFE48 151A2998 00000000 */  nop
  .L151A299C:
    /* 1CFE4C 151A299C 9339E616 */  lbu        $t9, %lo(D_800BE616)($t9)
    /* 1CFE50 151A29A0 17200016 */  bnez       $t9, .L151A29FC
    /* 1CFE54 151A29A4 00000000 */   nop
    /* 1CFE58 151A29A8 84450004 */  lh         $a1, 0x4($v0)
    /* 1CFE5C 151A29AC 2407FFFF */  addiu      $a3, $zero, -0x1
    /* 1CFE60 151A29B0 10E50012 */  beq        $a3, $a1, .L151A29FC
    /* 1CFE64 151A29B4 00000000 */   nop
    /* 1CFE68 151A29B8 80430006 */  lb         $v1, 0x6($v0)
    /* 1CFE6C 151A29BC 00A6082A */  slt        $at, $a1, $a2
    /* 1CFE70 151A29C0 10E3000E */  beq        $a3, $v1, .L151A29FC
    /* 1CFE74 151A29C4 00000000 */   nop
    /* 1CFE78 151A29C8 1420000C */  bnez       $at, .L151A29FC
    /* 1CFE7C 151A29CC 00034080 */   sll       $t0, $v1, 2
    /* 1CFE80 151A29D0 3C198009 */  lui        $t9, %hi(D_8008F8E0)
    /* 1CFE84 151A29D4 0328C821 */  addu       $t9, $t9, $t0
    /* 1CFE88 151A29D8 8F39F8E0 */  lw         $t9, %lo(D_8008F8E0)($t9)
    /* 1CFE8C 151A29DC AFA20018 */  sw         $v0, 0x18($sp)
    /* 1CFE90 151A29E0 AFA40020 */  sw         $a0, 0x20($sp)
    /* 1CFE94 151A29E4 0320F809 */  jalr       $t9
    /* 1CFE98 151A29E8 00000000 */   nop
    /* 1CFE9C 151A29EC 8FA20018 */  lw         $v0, 0x18($sp)
    /* 1CFEA0 151A29F0 8FA40020 */  lw         $a0, 0x20($sp)
    /* 1CFEA4 151A29F4 2407FFFF */  addiu      $a3, $zero, -0x1
    /* 1CFEA8 151A29F8 A4470004 */  sh         $a3, 0x4($v0)
  .L151A29FC:
    /* 1CFEAC 151A29FC 0D44C5C3 */  jal        func_1513170C
    /* 1CFEB0 151A2A00 8FA50024 */   lw        $a1, 0x24($sp)
    /* 1CFEB4 151A2A04 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 1CFEB8 151A2A08 27BD0020 */  addiu      $sp, $sp, 0x20
    /* 1CFEBC 151A2A0C 03E00008 */  jr         $ra
    /* 1CFEC0 151A2A10 00000000 */   nop
endlabel func_151A2960
