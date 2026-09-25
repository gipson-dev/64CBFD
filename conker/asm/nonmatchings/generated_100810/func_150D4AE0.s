glabel func_150D4AE0
    /* 101F90 150D4AE0 27BDFFC8 */  addiu      $sp, $sp, -0x38
    /* 101F94 150D4AE4 AFB00020 */  sw         $s0, 0x20($sp)
    /* 101F98 150D4AE8 00C08025 */  or         $s0, $a2, $zero
    /* 101F9C 150D4AEC AFBF0024 */  sw         $ra, 0x24($sp)
    /* 101FA0 150D4AF0 AFA40038 */  sw         $a0, 0x38($sp)
    /* 101FA4 150D4AF4 AFA5003C */  sw         $a1, 0x3C($sp)
    /* 101FA8 150D4AF8 AFA70044 */  sw         $a3, 0x44($sp)
    /* 101FAC 150D4AFC 8E0E01D4 */  lw         $t6, 0x1D4($s0)
    /* 101FB0 150D4B00 3C0F800A */  lui        $t7, %hi(D_800A09D0)
    /* 101FB4 150D4B04 25EF09D0 */  addiu      $t7, $t7, %lo(D_800A09D0)
    /* 101FB8 150D4B08 11C00018 */  beqz       $t6, .L150D4B6C
    /* 101FBC 150D4B0C 8FAB0038 */   lw        $t3, 0x38($sp)
    /* 101FC0 150D4B10 8FB90038 */  lw         $t9, 0x38($sp)
    /* 101FC4 150D4B14 8FA8003C */  lw         $t0, 0x3C($sp)
    /* 101FC8 150D4B18 3C18800A */  lui        $t8, %hi(D_800A09DC)
    /* 101FCC 150D4B1C 271809DC */  addiu      $t8, $t8, %lo(D_800A09DC)
    /* 101FD0 150D4B20 27A90028 */  addiu      $t1, $sp, 0x28
    /* 101FD4 150D4B24 240A0002 */  addiu      $t2, $zero, 0x2
    /* 101FD8 150D4B28 AFAF0030 */  sw         $t7, 0x30($sp)
    /* 101FDC 150D4B2C AFB80034 */  sw         $t8, 0x34($sp)
    /* 101FE0 150D4B30 AFAA0014 */  sw         $t2, 0x14($sp)
    /* 101FE4 150D4B34 AFA90010 */  sw         $t1, 0x10($sp)
    /* 101FE8 150D4B38 02002025 */  or         $a0, $s0, $zero
    /* 101FEC 150D4B3C 8FA50044 */  lw         $a1, 0x44($sp)
    /* 101FF0 150D4B40 00003025 */  or         $a2, $zero, $zero
    /* 101FF4 150D4B44 27A70030 */  addiu      $a3, $sp, 0x30
    /* 101FF8 150D4B48 AFB90028 */  sw         $t9, 0x28($sp)
    /* 101FFC 150D4B4C 0D451953 */  jal        func_1514654C
    /* 102000 150D4B50 AFA8002C */   sw        $t0, 0x2C($sp)
    /* 102004 150D4B54 10400003 */  beqz       $v0, .L150D4B64
    /* 102008 150D4B58 00000000 */   nop
    /* 10200C 150D4B5C 10000018 */  b          .L150D4BC0
    /* 102010 150D4B60 24020001 */   addiu     $v0, $zero, 0x1
  .L150D4B64:
    /* 102014 150D4B64 10000016 */  b          .L150D4BC0
    /* 102018 150D4B68 00001025 */   or        $v0, $zero, $zero
  .L150D4B6C:
    /* 10201C 150D4B6C C6040014 */  lwc1       $f4, 0x14($s0)
    /* 102020 150D4B70 3C0142C8 */  lui        $at, (0x42C80000 >> 16)
    /* 102024 150D4B74 44810000 */  mtc1       $at, $f0
    /* 102028 150D4B78 E5640000 */  swc1       $f4, 0x0($t3)
    /* 10202C 150D4B7C C6060018 */  lwc1       $f6, 0x18($s0)
    /* 102030 150D4B80 3C0143FA */  lui        $at, (0x43FA0000 >> 16)
    /* 102034 150D4B84 24020002 */  addiu      $v0, $zero, 0x2
    /* 102038 150D4B88 46003200 */  add.s      $f8, $f6, $f0
    /* 10203C 150D4B8C 44813000 */  mtc1       $at, $f6
    /* 102040 150D4B90 E5680004 */  swc1       $f8, 0x4($t3)
    /* 102044 150D4B94 C60A001C */  lwc1       $f10, 0x1C($s0)
    /* 102048 150D4B98 E56A0008 */  swc1       $f10, 0x8($t3)
    /* 10204C 150D4B9C 8FAC003C */  lw         $t4, 0x3C($sp)
    /* 102050 150D4BA0 C6100014 */  lwc1       $f16, 0x14($s0)
    /* 102054 150D4BA4 E5900000 */  swc1       $f16, 0x0($t4)
    /* 102058 150D4BA8 C6120018 */  lwc1       $f18, 0x18($s0)
    /* 10205C 150D4BAC 46009100 */  add.s      $f4, $f18, $f0
    /* 102060 150D4BB0 46062200 */  add.s      $f8, $f4, $f6
    /* 102064 150D4BB4 E5880004 */  swc1       $f8, 0x4($t4)
    /* 102068 150D4BB8 C60A001C */  lwc1       $f10, 0x1C($s0)
    /* 10206C 150D4BBC E58A0008 */  swc1       $f10, 0x8($t4)
  .L150D4BC0:
    /* 102070 150D4BC0 8FBF0024 */  lw         $ra, 0x24($sp)
    /* 102074 150D4BC4 8FB00020 */  lw         $s0, 0x20($sp)
    /* 102078 150D4BC8 27BD0038 */  addiu      $sp, $sp, 0x38
    /* 10207C 150D4BCC 03E00008 */  jr         $ra
    /* 102080 150D4BD0 00000000 */   nop
endlabel func_150D4AE0
