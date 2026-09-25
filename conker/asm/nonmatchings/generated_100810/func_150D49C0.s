glabel func_150D49C0
    /* 101E70 150D49C0 27BDFFE0 */  addiu      $sp, $sp, -0x20
    /* 101E74 150D49C4 AFA60028 */  sw         $a2, 0x28($sp)
    /* 101E78 150D49C8 30CE00FF */  andi       $t6, $a2, 0xFF
    /* 101E7C 150D49CC 01C03025 */  or         $a2, $t6, $zero
    /* 101E80 150D49D0 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 101E84 150D49D4 8C830098 */  lw         $v1, 0x98($a0)
    /* 101E88 150D49D8 10C00006 */  beqz       $a2, .L150D49F4
    /* 101E8C 150D49DC 00C01025 */   or        $v0, $a2, $zero
    /* 101E90 150D49E0 2401002E */  addiu      $at, $zero, 0x2E
    /* 101E94 150D49E4 10C10003 */  beq        $a2, $at, .L150D49F4
    /* 101E98 150D49E8 24010003 */   addiu     $at, $zero, 0x3
    /* 101E9C 150D49EC 54C1000E */  bnel       $a2, $at, .L150D4A28
    /* 101EA0 150D49F0 2401002D */   addiu     $at, $zero, 0x2D
  .L150D49F4:
    /* 101EA4 150D49F4 8CA20000 */  lw         $v0, 0x0($a1)
    /* 101EA8 150D49F8 8C6F0000 */  lw         $t7, 0x0($v1)
    /* 101EAC 150D49FC 104F0005 */  beq        $v0, $t7, .L150D4A14
    /* 101EB0 150D4A00 00000000 */   nop
    /* 101EB4 150D4A04 90780004 */  lbu        $t8, 0x4($v1)
    /* 101EB8 150D4A08 90B90004 */  lbu        $t9, 0x4($a1)
    /* 101EBC 150D4A0C 57190031 */  bnel       $t8, $t9, .L150D4AD4
    /* 101EC0 150D4A10 8FBF0014 */   lw        $ra, 0x14($sp)
  .L150D4A14:
    /* 101EC4 150D4A14 0D45A5CB */  jal        func_1516972C
    /* 101EC8 150D4A18 00000000 */   nop
    /* 101ECC 150D4A1C 1000002D */  b          .L150D4AD4
    /* 101ED0 150D4A20 8FBF0014 */   lw        $ra, 0x14($sp)
    /* 101ED4 150D4A24 2401002D */  addiu      $at, $zero, 0x2D
  .L150D4A28:
    /* 101ED8 150D4A28 5441002A */  bnel       $v0, $at, .L150D4AD4
    /* 101EDC 150D4A2C 8FBF0014 */   lw        $ra, 0x14($sp)
    /* 101EE0 150D4A30 8CA20000 */  lw         $v0, 0x0($a1)
    /* 101EE4 150D4A34 8C640000 */  lw         $a0, 0x0($v1)
    /* 101EE8 150D4A38 00003025 */  or         $a2, $zero, $zero
    /* 101EEC 150D4A3C 54440012 */  bnel       $v0, $a0, .L150D4A88
    /* 101EF0 150D4A40 8CAB0004 */   lw        $t3, 0x4($a1)
    /* 101EF4 150D4A44 8CA40004 */  lw         $a0, 0x4($a1)
    /* 101EF8 150D4A48 24010048 */  addiu      $at, $zero, 0x48
    /* 101EFC 150D4A4C AC640000 */  sw         $a0, 0x0($v1)
    /* 101F00 150D4A50 90A90009 */  lbu        $t1, 0x9($a1)
    /* 101F04 150D4A54 24050079 */  addiu      $a1, $zero, 0x79
    /* 101F08 150D4A58 A0690004 */  sb         $t1, 0x4($v1)
    /* 101F0C 150D4A5C 908A0004 */  lbu        $t2, 0x4($a0)
    /* 101F10 150D4A60 15410003 */  bne        $t2, $at, .L150D4A70
    /* 101F14 150D4A64 00000000 */   nop
    /* 101F18 150D4A68 10000001 */  b          .L150D4A70
    /* 101F1C 150D4A6C 2405007A */   addiu     $a1, $zero, 0x7A
  .L150D4A70:
    /* 101F20 150D4A70 0D40C657 */  jal        func_1503195C
    /* 101F24 150D4A74 AFA3001C */   sw        $v1, 0x1C($sp)
    /* 101F28 150D4A78 8FA3001C */  lw         $v1, 0x1C($sp)
    /* 101F2C 150D4A7C 10000014 */  b          .L150D4AD0
    /* 101F30 150D4A80 AC620008 */   sw        $v0, 0x8($v1)
    /* 101F34 150D4A84 8CAB0004 */  lw         $t3, 0x4($a1)
  .L150D4A88:
    /* 101F38 150D4A88 00003025 */  or         $a2, $zero, $zero
    /* 101F3C 150D4A8C 55640011 */  bnel       $t3, $a0, .L150D4AD4
    /* 101F40 150D4A90 8FBF0014 */   lw        $ra, 0x14($sp)
    /* 101F44 150D4A94 AC620000 */  sw         $v0, 0x0($v1)
    /* 101F48 150D4A98 90AC0008 */  lbu        $t4, 0x8($a1)
    /* 101F4C 150D4A9C 24010048 */  addiu      $at, $zero, 0x48
    /* 101F50 150D4AA0 24050079 */  addiu      $a1, $zero, 0x79
    /* 101F54 150D4AA4 A06C0004 */  sb         $t4, 0x4($v1)
    /* 101F58 150D4AA8 904D0004 */  lbu        $t5, 0x4($v0)
    /* 101F5C 150D4AAC 00402025 */  or         $a0, $v0, $zero
    /* 101F60 150D4AB0 15A10003 */  bne        $t5, $at, .L150D4AC0
    /* 101F64 150D4AB4 00000000 */   nop
    /* 101F68 150D4AB8 10000001 */  b          .L150D4AC0
    /* 101F6C 150D4ABC 2405007A */   addiu     $a1, $zero, 0x7A
  .L150D4AC0:
    /* 101F70 150D4AC0 0D40C657 */  jal        func_1503195C
    /* 101F74 150D4AC4 AFA3001C */   sw        $v1, 0x1C($sp)
    /* 101F78 150D4AC8 8FA3001C */  lw         $v1, 0x1C($sp)
    /* 101F7C 150D4ACC AC620008 */  sw         $v0, 0x8($v1)
  .L150D4AD0:
    /* 101F80 150D4AD0 8FBF0014 */  lw         $ra, 0x14($sp)
  .L150D4AD4:
    /* 101F84 150D4AD4 27BD0020 */  addiu      $sp, $sp, 0x20
    /* 101F88 150D4AD8 03E00008 */  jr         $ra
    /* 101F8C 150D4ADC 00000000 */   nop
endlabel func_150D49C0
