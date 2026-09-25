glabel func_150DA50C
    /* 1079BC 150DA50C 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* 1079C0 150DA510 AFA60020 */  sw         $a2, 0x20($sp)
    /* 1079C4 150DA514 30CE00FF */  andi       $t6, $a2, 0xFF
    /* 1079C8 150DA518 01C03025 */  or         $a2, $t6, $zero
    /* 1079CC 150DA51C AFBF0014 */  sw         $ra, 0x14($sp)
    /* 1079D0 150DA520 24010044 */  addiu      $at, $zero, 0x44
    /* 1079D4 150DA524 8C820098 */  lw         $v0, 0x98($a0)
    /* 1079D8 150DA528 14C1000D */  bne        $a2, $at, .L150DA560
    /* 1079DC 150DA52C 00C01825 */   or        $v1, $a2, $zero
    /* 1079E0 150DA530 8C4F0000 */  lw         $t7, 0x0($v0)
    /* 1079E4 150DA534 8CB80000 */  lw         $t8, 0x0($a1)
    /* 1079E8 150DA538 51F80006 */  beql       $t7, $t8, .L150DA554
    /* 1079EC 150DA53C C4A40008 */   lwc1      $f4, 0x8($a1)
    /* 1079F0 150DA540 90590004 */  lbu        $t9, 0x4($v0)
    /* 1079F4 150DA544 90A80004 */  lbu        $t0, 0x4($a1)
    /* 1079F8 150DA548 57280025 */  bnel       $t9, $t0, .L150DA5E0
    /* 1079FC 150DA54C 8FBF0014 */   lw        $ra, 0x14($sp)
    /* 107A00 150DA550 C4A40008 */  lwc1       $f4, 0x8($a1)
  .L150DA554:
    /* 107A04 150DA554 E444003C */  swc1       $f4, 0x3C($v0)
    /* 107A08 150DA558 10000021 */  b          .L150DA5E0
    /* 107A0C 150DA55C 8FBF0014 */   lw        $ra, 0x14($sp)
  .L150DA560:
    /* 107A10 150DA560 1460000D */  bnez       $v1, .L150DA598
    /* 107A14 150DA564 2401002D */   addiu     $at, $zero, 0x2D
    /* 107A18 150DA568 8CA30000 */  lw         $v1, 0x0($a1)
    /* 107A1C 150DA56C 8C490000 */  lw         $t1, 0x0($v0)
    /* 107A20 150DA570 10690005 */  beq        $v1, $t1, .L150DA588
    /* 107A24 150DA574 00000000 */   nop
    /* 107A28 150DA578 90AA0004 */  lbu        $t2, 0x4($a1)
    /* 107A2C 150DA57C 904B0004 */  lbu        $t3, 0x4($v0)
    /* 107A30 150DA580 554B0017 */  bnel       $t2, $t3, .L150DA5E0
    /* 107A34 150DA584 8FBF0014 */   lw        $ra, 0x14($sp)
  .L150DA588:
    /* 107A38 150DA588 0D45A5CB */  jal        func_1516972C
    /* 107A3C 150DA58C 00000000 */   nop
    /* 107A40 150DA590 10000013 */  b          .L150DA5E0
    /* 107A44 150DA594 8FBF0014 */   lw        $ra, 0x14($sp)
  .L150DA598:
    /* 107A48 150DA598 54610011 */  bnel       $v1, $at, .L150DA5E0
    /* 107A4C 150DA59C 8FBF0014 */   lw        $ra, 0x14($sp)
    /* 107A50 150DA5A0 8CA40000 */  lw         $a0, 0x0($a1)
    /* 107A54 150DA5A4 8C430000 */  lw         $v1, 0x0($v0)
    /* 107A58 150DA5A8 54830007 */  bnel       $a0, $v1, .L150DA5C8
    /* 107A5C 150DA5AC 8CAE0004 */   lw        $t6, 0x4($a1)
    /* 107A60 150DA5B0 8CAC0004 */  lw         $t4, 0x4($a1)
    /* 107A64 150DA5B4 AC4C0000 */  sw         $t4, 0x0($v0)
    /* 107A68 150DA5B8 90AD0009 */  lbu        $t5, 0x9($a1)
    /* 107A6C 150DA5BC 10000007 */  b          .L150DA5DC
    /* 107A70 150DA5C0 A04D0004 */   sb        $t5, 0x4($v0)
    /* 107A74 150DA5C4 8CAE0004 */  lw         $t6, 0x4($a1)
  .L150DA5C8:
    /* 107A78 150DA5C8 55C30005 */  bnel       $t6, $v1, .L150DA5E0
    /* 107A7C 150DA5CC 8FBF0014 */   lw        $ra, 0x14($sp)
    /* 107A80 150DA5D0 AC440000 */  sw         $a0, 0x0($v0)
    /* 107A84 150DA5D4 90AF0008 */  lbu        $t7, 0x8($a1)
    /* 107A88 150DA5D8 A04F0004 */  sb         $t7, 0x4($v0)
  .L150DA5DC:
    /* 107A8C 150DA5DC 8FBF0014 */  lw         $ra, 0x14($sp)
  .L150DA5E0:
    /* 107A90 150DA5E0 27BD0018 */  addiu      $sp, $sp, 0x18
    /* 107A94 150DA5E4 03E00008 */  jr         $ra
    /* 107A98 150DA5E8 00000000 */   nop
endlabel func_150DA50C
