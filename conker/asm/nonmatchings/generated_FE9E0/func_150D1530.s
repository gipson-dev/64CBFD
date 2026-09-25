glabel func_150D1530
    /* FE9E0 150D1530 27BDFFC8 */  addiu      $sp, $sp, -0x38
    /* FE9E4 150D1534 AFB00028 */  sw         $s0, 0x28($sp)
    /* FE9E8 150D1538 00808025 */  or         $s0, $a0, $zero
    /* FE9EC 150D153C AFBF002C */  sw         $ra, 0x2C($sp)
    /* FE9F0 150D1540 8E0E002C */  lw         $t6, 0x2C($s0)
    /* FE9F4 150D1544 24010040 */  addiu      $at, $zero, 0x40
    /* FE9F8 150D1548 51C100AC */  beql       $t6, $at, .L150D17FC
    /* FE9FC 150D154C 8FBF002C */   lw        $ra, 0x2C($sp)
    /* FEA00 150D1550 8E0F05F0 */  lw         $t7, 0x5F0($s0)
    /* FEA04 150D1554 02002025 */  or         $a0, $s0, $zero
    /* FEA08 150D1558 31F80080 */  andi       $t8, $t7, 0x80
    /* FEA0C 150D155C 1300008A */  beqz       $t8, .L150D1788
    /* FEA10 150D1560 00000000 */   nop
    /* FEA14 150D1564 44800000 */  mtc1       $zero, $f0
    /* FEA18 150D1568 3C01432A */  lui        $at, (0x432A0000 >> 16)
    /* FEA1C 150D156C 8E1903D0 */  lw         $t9, 0x3D0($s0)
    /* FEA20 150D1570 C722003C */  lwc1       $f2, 0x3C($t9)
    /* FEA24 150D1574 4600103C */  c.lt.s     $f2, $f0
    /* FEA28 150D1578 00000000 */  nop
    /* FEA2C 150D157C 45020004 */  bc1fl      .L150D1590
    /* FEA30 150D1580 44816000 */   mtc1      $at, $f12
    /* FEA34 150D1584 1000000B */  b          .L150D15B4
    /* FEA38 150D1588 46000086 */   mov.s     $f2, $f0
    /* FEA3C 150D158C 44816000 */  mtc1       $at, $f12
  .L150D1590:
    /* FEA40 150D1590 00000000 */  nop
    /* FEA44 150D1594 4602603C */  c.lt.s     $f12, $f2
    /* FEA48 150D1598 00000000 */  nop
    /* FEA4C 150D159C 45020004 */  bc1fl      .L150D15B0
    /* FEA50 150D15A0 46001006 */   mov.s     $f0, $f2
    /* FEA54 150D15A4 10000002 */  b          .L150D15B0
    /* FEA58 150D15A8 46006006 */   mov.s     $f0, $f12
    /* FEA5C 150D15AC 46001006 */  mov.s      $f0, $f2
  .L150D15B0:
    /* FEA60 150D15B0 46000086 */  mov.s      $f2, $f0
  .L150D15B4:
    /* FEA64 150D15B4 3C01800A */  lui        $at, %hi(D_800A08D0)
    /* FEA68 150D15B8 C42408D0 */  lwc1       $f4, %lo(D_800A08D0)($at)
    /* FEA6C 150D15BC 8E070134 */  lw         $a3, 0x134($s0)
    /* FEA70 150D15C0 24080003 */  addiu      $t0, $zero, 0x3
    /* FEA74 150D15C4 46041082 */  mul.s      $f2, $f2, $f4
    /* FEA78 150D15C8 AFA80010 */  sw         $t0, 0x10($sp)
    /* FEA7C 150D15CC 02002025 */  or         $a0, $s0, $zero
    /* FEA80 150D15D0 24050008 */  addiu      $a1, $zero, 0x8
    /* FEA84 150D15D4 00003025 */  or         $a2, $zero, $zero
    /* FEA88 150D15D8 0D448E4D */  jal        func_15123934
    /* FEA8C 150D15DC E7A20034 */   swc1      $f2, 0x34($sp)
    /* FEA90 150D15E0 1040000D */  beqz       $v0, .L150D1618
    /* FEA94 150D15E4 C7A20034 */   lwc1      $f2, 0x34($sp)
    /* FEA98 150D15E8 8E090084 */  lw         $t1, 0x84($s0)
    /* FEA9C 150D15EC 3C010130 */  lui        $at, (0x1300080 >> 16)
    /* FEAA0 150D15F0 34210080 */  ori        $at, $at, (0x1300080 & 0xFFFF)
    /* FEAA4 150D15F4 01215025 */  or         $t2, $t1, $at
    /* FEAA8 150D15F8 2401FFF9 */  addiu      $at, $zero, -0x7
    /* FEAAC 150D15FC AE0A0084 */  sw         $t2, 0x84($s0)
    /* FEAB0 150D1600 01416024 */  and        $t4, $t2, $at
    /* FEAB4 150D1604 240D0001 */  addiu      $t5, $zero, 0x1
    /* FEAB8 150D1608 240E0002 */  addiu      $t6, $zero, 0x2
    /* FEABC 150D160C AE0C0084 */  sw         $t4, 0x84($s0)
    /* FEAC0 150D1610 A60D01B4 */  sh         $t5, 0x1B4($s0)
    /* FEAC4 150D1614 A60E01E0 */  sh         $t6, 0x1E0($s0)
  .L150D1618:
    /* FEAC8 150D1618 3C01C342 */  lui        $at, (0xC3420000 >> 16)
    /* FEACC 150D161C 44813000 */  mtc1       $at, $f6
    /* FEAD0 150D1620 3C01438C */  lui        $at, (0x438C0000 >> 16)
    /* FEAD4 150D1624 44815000 */  mtc1       $at, $f10
    /* FEAD8 150D1628 3C014208 */  lui        $at, (0x42080000 >> 16)
    /* FEADC 150D162C 46023202 */  mul.s      $f8, $f6, $f2
    /* FEAE0 150D1630 44819000 */  mtc1       $at, $f18
    /* FEAE4 150D1634 3C014296 */  lui        $at, (0x42960000 >> 16)
    /* FEAE8 150D1638 44813000 */  mtc1       $at, $f6
    /* FEAEC 150D163C 46029102 */  mul.s      $f4, $f18, $f2
    /* FEAF0 150D1640 3C0F800C */  lui        $t7, %hi(D_800BE9F0)
    /* FEAF4 150D1644 24010032 */  addiu      $at, $zero, 0x32
    /* FEAF8 150D1648 24194035 */  addiu      $t9, $zero, 0x4035
    /* FEAFC 150D164C 24084036 */  addiu      $t0, $zero, 0x4036
    /* FEB00 150D1650 460A4400 */  add.s      $f16, $f8, $f10
    /* FEB04 150D1654 24040005 */  addiu      $a0, $zero, 0x5
    /* FEB08 150D1658 240600AC */  addiu      $a2, $zero, 0xAC
    /* FEB0C 150D165C 46062000 */  add.s      $f0, $f4, $f6
    /* FEB10 150D1660 E6100374 */  swc1       $f16, 0x374($s0)
    /* FEB14 150D1664 2407400A */  addiu      $a3, $zero, 0x400A
    /* FEB18 150D1668 240B400B */  addiu      $t3, $zero, 0x400B
    /* FEB1C 150D166C E6000348 */  swc1       $f0, 0x348($s0)
    /* FEB20 150D1670 E600034C */  swc1       $f0, 0x34C($s0)
    /* FEB24 150D1674 8DEFE9F0 */  lw         $t7, %lo(D_800BE9F0)($t7)
    /* FEB28 150D1678 240C400C */  addiu      $t4, $zero, 0x400C
    /* FEB2C 150D167C 240D400D */  addiu      $t5, $zero, 0x400D
    /* FEB30 150D1680 15E1000F */  bne        $t7, $at, .L150D16C0
    /* FEB34 150D1684 240E400E */   addiu     $t6, $zero, 0x400E
    /* FEB38 150D1688 9205023D */  lbu        $a1, 0x23D($s0)
    /* FEB3C 150D168C 24094037 */  addiu      $t1, $zero, 0x4037
    /* FEB40 150D1690 AFA90018 */  sw         $t1, 0x18($sp)
    /* FEB44 150D1694 34B82000 */  ori        $t8, $a1, 0x2000
    /* FEB48 150D1698 03002825 */  or         $a1, $t8, $zero
    /* FEB4C 150D169C E7A20034 */  swc1       $f2, 0x34($sp)
    /* FEB50 150D16A0 AFA80014 */  sw         $t0, 0x14($sp)
    /* FEB54 150D16A4 AFB90010 */  sw         $t9, 0x10($sp)
    /* FEB58 150D16A8 24040004 */  addiu      $a0, $zero, 0x4
    /* FEB5C 150D16AC 240600AC */  addiu      $a2, $zero, 0xAC
    /* FEB60 150D16B0 0D426F90 */  jal        func_1509BE40
    /* FEB64 150D16B4 24074027 */   addiu     $a3, $zero, 0x4027
    /* FEB68 150D16B8 1000000B */  b          .L150D16E8
    /* FEB6C 150D16BC C7A20034 */   lwc1      $f2, 0x34($sp)
  .L150D16C0:
    /* FEB70 150D16C0 9205023D */  lbu        $a1, 0x23D($s0)
    /* FEB74 150D16C4 E7A20034 */  swc1       $f2, 0x34($sp)
    /* FEB78 150D16C8 AFAE001C */  sw         $t6, 0x1C($sp)
    /* FEB7C 150D16CC 34AA2000 */  ori        $t2, $a1, 0x2000
    /* FEB80 150D16D0 01402825 */  or         $a1, $t2, $zero
    /* FEB84 150D16D4 AFAD0018 */  sw         $t5, 0x18($sp)
    /* FEB88 150D16D8 AFAC0014 */  sw         $t4, 0x14($sp)
    /* FEB8C 150D16DC 0D426F90 */  jal        func_1509BE40
    /* FEB90 150D16E0 AFAB0010 */   sw        $t3, 0x10($sp)
    /* FEB94 150D16E4 C7A20034 */  lwc1       $f2, 0x34($sp)
  .L150D16E8:
    /* FEB98 150D16E8 50400007 */  beql       $v0, $zero, .L150D1708
    /* FEB9C 150D16EC 8E1903D0 */   lw        $t9, 0x3D0($s0)
    /* FEBA0 150D16F0 8E0F0084 */  lw         $t7, 0x84($s0)
    /* FEBA4 150D16F4 3C011000 */  lui        $at, (0x10000000 >> 16)
    /* FEBA8 150D16F8 01E1C025 */  or         $t8, $t7, $at
    /* FEBAC 150D16FC 10000012 */  b          .L150D1748
    /* FEBB0 150D1700 AE180084 */   sw        $t8, 0x84($s0)
    /* FEBB4 150D1704 8E1903D0 */  lw         $t9, 0x3D0($s0)
  .L150D1708:
    /* FEBB8 150D1708 3C0142F6 */  lui        $at, (0x42F60000 >> 16)
    /* FEBBC 150D170C 93280081 */  lbu        $t0, 0x81($t9)
    /* FEBC0 150D1710 51000006 */  beql       $t0, $zero, .L150D172C
    /* FEBC4 150D1714 44815000 */   mtc1      $at, $f10
    /* FEBC8 150D1718 3C01C1F0 */  lui        $at, (0xC1F00000 >> 16)
    /* FEBCC 150D171C 44814000 */  mtc1       $at, $f8
    /* FEBD0 150D1720 10000004 */  b          .L150D1734
    /* FEBD4 150D1724 E6080190 */   swc1      $f8, 0x190($s0)
    /* FEBD8 150D1728 44815000 */  mtc1       $at, $f10
  .L150D172C:
    /* FEBDC 150D172C 00000000 */  nop
    /* FEBE0 150D1730 E60A0190 */  swc1       $f10, 0x190($s0)
  .L150D1734:
    /* FEBE4 150D1734 8E090084 */  lw         $t1, 0x84($s0)
    /* FEBE8 150D1738 3C01EFFF */  lui        $at, (0xEFFFFFFF >> 16)
    /* FEBEC 150D173C 3421FFFF */  ori        $at, $at, (0xEFFFFFFF & 0xFFFF)
    /* FEBF0 150D1740 01215024 */  and        $t2, $t1, $at
    /* FEBF4 150D1744 AE0A0084 */  sw         $t2, 0x84($s0)
  .L150D1748:
    /* FEBF8 150D1748 3C01800A */  lui        $at, %hi(D_800A08D4)
    /* FEBFC 150D174C C43008D4 */  lwc1       $f16, %lo(D_800A08D4)($at)
    /* FEC00 150D1750 3C014120 */  lui        $at, (0x41200000 >> 16)
    /* FEC04 150D1754 44812000 */  mtc1       $at, $f4
    /* FEC08 150D1758 46028482 */  mul.s      $f18, $f16, $f2
    /* FEC0C 150D175C 920B023C */  lbu        $t3, 0x23C($s0)
    /* FEC10 150D1760 46049000 */  add.s      $f0, $f18, $f4
    /* FEC14 150D1764 E60001A8 */  swc1       $f0, 0x1A8($s0)
    /* FEC18 150D1768 11600010 */  beqz       $t3, .L150D17AC
    /* FEC1C 150D176C E60001A4 */   swc1      $f0, 0x1A4($s0)
    /* FEC20 150D1770 C60601A4 */  lwc1       $f6, 0x1A4($s0)
    /* FEC24 150D1774 C60801A8 */  lwc1       $f8, 0x1A8($s0)
    /* FEC28 150D1778 E60601A4 */  swc1       $f6, 0x1A4($s0)
    /* FEC2C 150D177C E60801A8 */  swc1       $f8, 0x1A8($s0)
    /* FEC30 150D1780 1000000A */  b          .L150D17AC
    /* FEC34 150D1784 00000000 */   nop
  .L150D1788:
    /* FEC38 150D1788 0D448E73 */  jal        func_151239CC
    /* FEC3C 150D178C 24050003 */   addiu     $a1, $zero, 0x3
    /* FEC40 150D1790 10400006 */  beqz       $v0, .L150D17AC
    /* FEC44 150D1794 00000000 */   nop
    /* FEC48 150D1798 44800000 */  mtc1       $zero, $f0
    /* FEC4C 150D179C 00000000 */  nop
    /* FEC50 150D17A0 E60001A8 */  swc1       $f0, 0x1A8($s0)
    /* FEC54 150D17A4 E60001A4 */  swc1       $f0, 0x1A4($s0)
    /* FEC58 150D17A8 E6000190 */  swc1       $f0, 0x190($s0)
  .L150D17AC:
    /* FEC5C 150D17AC 3C0C800C */  lui        $t4, %hi(D_800BE9F0)
    /* FEC60 150D17B0 8D8CE9F0 */  lw         $t4, %lo(D_800BE9F0)($t4)
    /* FEC64 150D17B4 24010032 */  addiu      $at, $zero, 0x32
    /* FEC68 150D17B8 24040001 */  addiu      $a0, $zero, 0x1
    /* FEC6C 150D17BC 1581000E */  bne        $t4, $at, .L150D17F8
    /* FEC70 150D17C0 24054039 */   addiu     $a1, $zero, 0x4039
    /* FEC74 150D17C4 24060006 */  addiu      $a2, $zero, 0x6
    /* FEC78 150D17C8 0D426F90 */  jal        func_1509BE40
    /* FEC7C 150D17CC 34079000 */   ori       $a3, $zero, 0x9000
    /* FEC80 150D17D0 50400006 */  beql       $v0, $zero, .L150D17EC
    /* FEC84 150D17D4 8E0F0084 */   lw        $t7, 0x84($s0)
    /* FEC88 150D17D8 8E0D0084 */  lw         $t5, 0x84($s0)
    /* FEC8C 150D17DC 35AE1000 */  ori        $t6, $t5, 0x1000
    /* FEC90 150D17E0 10000005 */  b          .L150D17F8
    /* FEC94 150D17E4 AE0E0084 */   sw        $t6, 0x84($s0)
    /* FEC98 150D17E8 8E0F0084 */  lw         $t7, 0x84($s0)
  .L150D17EC:
    /* FEC9C 150D17EC 2401EFFF */  addiu      $at, $zero, -0x1001
    /* FECA0 150D17F0 01E1C024 */  and        $t8, $t7, $at
    /* FECA4 150D17F4 AE180084 */  sw         $t8, 0x84($s0)
  .L150D17F8:
    /* FECA8 150D17F8 8FBF002C */  lw         $ra, 0x2C($sp)
  .L150D17FC:
    /* FECAC 150D17FC 8FB00028 */  lw         $s0, 0x28($sp)
    /* FECB0 150D1800 27BD0038 */  addiu      $sp, $sp, 0x38
    /* FECB4 150D1804 03E00008 */  jr         $ra
    /* FECB8 150D1808 00000000 */   nop
endlabel func_150D1530
    /* FECBC 150D180C 00000000 */  nop
