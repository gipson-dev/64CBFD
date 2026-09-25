glabel func_151C1654
    /* 1EEB04 151C1654 27BDFFD0 */  addiu      $sp, $sp, -0x30
    /* 1EEB08 151C1658 AFB00028 */  sw         $s0, 0x28($sp)
    /* 1EEB0C 151C165C 00808025 */  or         $s0, $a0, $zero
    /* 1EEB10 151C1660 AFBF002C */  sw         $ra, 0x2C($sp)
    /* 1EEB14 151C1664 AFA50034 */  sw         $a1, 0x34($sp)
    /* 1EEB18 151C1668 AFA60038 */  sw         $a2, 0x38($sp)
    /* 1EEB1C 151C166C AFA7003C */  sw         $a3, 0x3C($sp)
    /* 1EEB20 151C1670 3C02800E */  lui        $v0, %hi(D_800E0934)
    /* 1EEB24 151C1674 8C420934 */  lw         $v0, %lo(D_800E0934)($v0)
    /* 1EEB28 151C1678 5040000D */  beql       $v0, $zero, .L151C16B0
    /* 1EEB2C 151C167C 93A2003F */   lbu       $v0, 0x3F($sp)
    /* 1EEB30 151C1680 C6040000 */  lwc1       $f4, 0x0($s0)
    /* 1EEB34 151C1684 C6080004 */  lwc1       $f8, 0x4($s0)
    /* 1EEB38 151C1688 C6100008 */  lwc1       $f16, 0x8($s0)
    /* 1EEB3C 151C168C 4600218D */  trunc.w.s  $f6, $f4
    /* 1EEB40 151C1690 4600428D */  trunc.w.s  $f10, $f8
    /* 1EEB44 151C1694 44043000 */  mfc1       $a0, $f6
    /* 1EEB48 151C1698 4600848D */  trunc.w.s  $f18, $f16
    /* 1EEB4C 151C169C 44055000 */  mfc1       $a1, $f10
    /* 1EEB50 151C16A0 44069000 */  mfc1       $a2, $f18
    /* 1EEB54 151C16A4 0040F809 */  jalr       $v0
    /* 1EEB58 151C16A8 00000000 */   nop
    /* 1EEB5C 151C16AC 93A2003F */  lbu        $v0, 0x3F($sp)
  .L151C16B0:
    /* 1EEB60 151C16B0 24010001 */  addiu      $at, $zero, 0x1
    /* 1EEB64 151C16B4 02002025 */  or         $a0, $s0, $zero
    /* 1EEB68 151C16B8 10400028 */  beqz       $v0, .L151C175C
    /* 1EEB6C 151C16BC 8FA50034 */   lw        $a1, 0x34($sp)
    /* 1EEB70 151C16C0 10410009 */  beq        $v0, $at, .L151C16E8
    /* 1EEB74 151C16C4 8FA60038 */   lw        $a2, 0x38($sp)
    /* 1EEB78 151C16C8 24010002 */  addiu      $at, $zero, 0x2
    /* 1EEB7C 151C16CC 1041000E */  beq        $v0, $at, .L151C1708
    /* 1EEB80 151C16D0 8FA60038 */   lw        $a2, 0x38($sp)
    /* 1EEB84 151C16D4 24010003 */  addiu      $at, $zero, 0x3
    /* 1EEB88 151C16D8 10410013 */  beq        $v0, $at, .L151C1728
    /* 1EEB8C 151C16DC 8FA60038 */   lw        $a2, 0x38($sp)
    /* 1EEB90 151C16E0 1000001F */  b          .L151C1760
    /* 1EEB94 151C16E4 8FAC0040 */   lw        $t4, 0x40($sp)
  .L151C16E8:
    /* 1EEB98 151C16E8 24190024 */  addiu      $t9, $zero, 0x24
    /* 1EEB9C 151C16EC AFB90010 */  sw         $t9, 0x10($sp)
    /* 1EEBA0 151C16F0 02002025 */  or         $a0, $s0, $zero
    /* 1EEBA4 151C16F4 8FA50034 */  lw         $a1, 0x34($sp)
    /* 1EEBA8 151C16F8 0D4750BA */  jal        func_151D42E8
    /* 1EEBAC 151C16FC 8FA70040 */   lw        $a3, 0x40($sp)
    /* 1EEBB0 151C1700 10000021 */  b          .L151C1788
    /* 1EEBB4 151C1704 8FBF002C */   lw        $ra, 0x2C($sp)
  .L151C1708:
    /* 1EEBB8 151C1708 24080025 */  addiu      $t0, $zero, 0x25
    /* 1EEBBC 151C170C AFA80010 */  sw         $t0, 0x10($sp)
    /* 1EEBC0 151C1710 02002025 */  or         $a0, $s0, $zero
    /* 1EEBC4 151C1714 8FA50034 */  lw         $a1, 0x34($sp)
    /* 1EEBC8 151C1718 0D4750BA */  jal        func_151D42E8
    /* 1EEBCC 151C171C 8FA70040 */   lw        $a3, 0x40($sp)
    /* 1EEBD0 151C1720 10000019 */  b          .L151C1788
    /* 1EEBD4 151C1724 8FBF002C */   lw        $ra, 0x2C($sp)
  .L151C1728:
    /* 1EEBD8 151C1728 8FA90040 */  lw         $t1, 0x40($sp)
    /* 1EEBDC 151C172C 240A0016 */  addiu      $t2, $zero, 0x16
    /* 1EEBE0 151C1730 240B0026 */  addiu      $t3, $zero, 0x26
    /* 1EEBE4 151C1734 AFAB0018 */  sw         $t3, 0x18($sp)
    /* 1EEBE8 151C1738 AFAA0014 */  sw         $t2, 0x14($sp)
    /* 1EEBEC 151C173C 02002025 */  or         $a0, $s0, $zero
    /* 1EEBF0 151C1740 8FA50034 */  lw         $a1, 0x34($sp)
    /* 1EEBF4 151C1744 00003825 */  or         $a3, $zero, $zero
    /* 1EEBF8 151C1748 AFA0001C */  sw         $zero, 0x1C($sp)
    /* 1EEBFC 151C174C 0D475035 */  jal        func_151D40D4
    /* 1EEC00 151C1750 AFA90010 */   sw        $t1, 0x10($sp)
    /* 1EEC04 151C1754 1000000C */  b          .L151C1788
    /* 1EEC08 151C1758 8FBF002C */   lw        $ra, 0x2C($sp)
  .L151C175C:
    /* 1EEC0C 151C175C 8FAC0040 */  lw         $t4, 0x40($sp)
  .L151C1760:
    /* 1EEC10 151C1760 240D0016 */  addiu      $t5, $zero, 0x16
    /* 1EEC14 151C1764 240E0015 */  addiu      $t6, $zero, 0x15
    /* 1EEC18 151C1768 AFAE0018 */  sw         $t6, 0x18($sp)
    /* 1EEC1C 151C176C AFAD0014 */  sw         $t5, 0x14($sp)
    /* 1EEC20 151C1770 8FA60038 */  lw         $a2, 0x38($sp)
    /* 1EEC24 151C1774 00003825 */  or         $a3, $zero, $zero
    /* 1EEC28 151C1778 AFA0001C */  sw         $zero, 0x1C($sp)
    /* 1EEC2C 151C177C 0D475035 */  jal        func_151D40D4
    /* 1EEC30 151C1780 AFAC0010 */   sw        $t4, 0x10($sp)
    /* 1EEC34 151C1784 8FBF002C */  lw         $ra, 0x2C($sp)
  .L151C1788:
    /* 1EEC38 151C1788 8FB00028 */  lw         $s0, 0x28($sp)
    /* 1EEC3C 151C178C 27BD0030 */  addiu      $sp, $sp, 0x30
    /* 1EEC40 151C1790 03E00008 */  jr         $ra
    /* 1EEC44 151C1794 00000000 */   nop
endlabel func_151C1654
