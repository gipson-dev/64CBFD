glabel func_150C4120
    /* F15D0 150C4120 27BDFF10 */  addiu      $sp, $sp, -0xF0
    /* F15D4 150C4124 AFA500F4 */  sw         $a1, 0xF4($sp)
    /* F15D8 150C4128 00057400 */  sll        $t6, $a1, 16
    /* F15DC 150C412C 44800000 */  mtc1       $zero, $f0
    /* F15E0 150C4130 000E2C03 */  sra        $a1, $t6, 16
    /* F15E4 150C4134 AFBF002C */  sw         $ra, 0x2C($sp)
    /* F15E8 150C4138 AFA600F8 */  sw         $a2, 0xF8($sp)
    /* F15EC 150C413C AFA700FC */  sw         $a3, 0xFC($sp)
    /* F15F0 150C4140 AFA400D4 */  sw         $a0, 0xD4($sp)
    /* F15F4 150C4144 9098003B */  lbu        $t8, 0x3B($a0)
    /* F15F8 150C4148 2419FFFF */  addiu      $t9, $zero, -0x1
    /* F15FC 150C414C E7A000DC */  swc1       $f0, 0xDC($sp)
    /* F1600 150C4150 AFA000E0 */  sw         $zero, 0xE0($sp)
    /* F1604 150C4154 E7A000E4 */  swc1       $f0, 0xE4($sp)
    /* F1608 150C4158 A7B900E8 */  sh         $t9, 0xE8($sp)
    /* F160C 150C415C A3A000EA */  sb         $zero, 0xEA($sp)
    /* F1610 150C4160 AFA000EC */  sw         $zero, 0xEC($sp)
    /* F1614 150C4164 A3B800D8 */  sb         $t8, 0xD8($sp)
    /* F1618 150C4168 90880004 */  lbu        $t0, 0x4($a0)
    /* F161C 150C416C 24010034 */  addiu      $at, $zero, 0x34
    /* F1620 150C4170 2402FFFF */  addiu      $v0, $zero, -0x1
    /* F1624 150C4174 15010005 */  bne        $t0, $at, .L150C418C
    /* F1628 150C4178 24060053 */   addiu     $a2, $zero, 0x53
    /* F162C 150C417C 24090054 */  addiu      $t1, $zero, 0x54
    /* F1630 150C4180 240A0001 */  addiu      $t2, $zero, 0x1
    /* F1634 150C4184 A7A900E8 */  sh         $t1, 0xE8($sp)
    /* F1638 150C4188 A3AA00EA */  sb         $t2, 0xEA($sp)
  .L150C418C:
    /* F163C 150C418C 14A20003 */  bne        $a1, $v0, .L150C419C
    /* F1640 150C4190 2407FFFF */   addiu     $a3, $zero, -0x1
    /* F1644 150C4194 10000002 */  b          .L150C41A0
    /* F1648 150C4198 2403012C */   addiu     $v1, $zero, 0x12C
  .L150C419C:
    /* F164C 150C419C 00A01825 */  or         $v1, $a1, $zero
  .L150C41A0:
    /* F1650 150C41A0 14A20003 */  bne        $a1, $v0, .L150C41B0
    /* F1654 150C41A4 00032400 */   sll       $a0, $v1, 16
    /* F1658 150C41A8 10000002 */  b          .L150C41B4
    /* F165C 150C41AC 00001025 */   or        $v0, $zero, $zero
  .L150C41B0:
    /* F1660 150C41B0 24020001 */  addiu      $v0, $zero, 0x1
  .L150C41B4:
    /* F1664 150C41B4 93AE00FB */  lbu        $t6, 0xFB($sp)
    /* F1668 150C41B8 8FAF00FC */  lw         $t7, 0xFC($sp)
    /* F166C 150C41BC 00045C03 */  sra        $t3, $a0, 16
    /* F1670 150C41C0 240C0040 */  addiu      $t4, $zero, 0x40
    /* F1674 150C41C4 240D001C */  addiu      $t5, $zero, 0x1C
    /* F1678 150C41C8 AFAD0018 */  sw         $t5, 0x18($sp)
    /* F167C 150C41CC AFAC0014 */  sw         $t4, 0x14($sp)
    /* F1680 150C41D0 01602025 */  or         $a0, $t3, $zero
    /* F1684 150C41D4 2405FFFF */  addiu      $a1, $zero, -0x1
    /* F1688 150C41D8 AFA20010 */  sw         $v0, 0x10($sp)
    /* F168C 150C41DC AFAE001C */  sw         $t6, 0x1C($sp)
    /* F1690 150C41E0 0D45244C */  jal        func_15149130
    /* F1694 150C41E4 AFAF0020 */   sw        $t7, 0x20($sp)
    /* F1698 150C41E8 104000AA */  beqz       $v0, .L150C4494
    /* F169C 150C41EC 24440028 */   addiu     $a0, $v0, 0x28
    /* F16A0 150C41F0 27A500D4 */  addiu      $a1, $sp, 0xD4
    /* F16A4 150C41F4 2406001C */  addiu      $a2, $zero, 0x1C
    /* F16A8 150C41F8 0C008BB0 */  jal        memcpy
    /* F16AC 150C41FC AFA40030 */   sw        $a0, 0x30($sp)
    /* F16B0 150C4200 3C19800A */  lui        $t9, %hi(D_800A0340)
    /* F16B4 150C4204 27390340 */  addiu      $t9, $t9, %lo(D_800A0340)
    /* F16B8 150C4208 8F210000 */  lw         $at, 0x0($t9)
    /* F16BC 150C420C 8F2A0004 */  lw         $t2, 0x4($t9)
    /* F16C0 150C4210 27B8003C */  addiu      $t8, $sp, 0x3C
    /* F16C4 150C4214 AF010000 */  sw         $at, 0x0($t8)
    /* F16C8 150C4218 AF0A0004 */  sw         $t2, 0x4($t8)
    /* F16CC 150C421C 8F2A000C */  lw         $t2, 0xC($t9)
    /* F16D0 150C4220 8F210008 */  lw         $at, 0x8($t9)
    /* F16D4 150C4224 AF0A000C */  sw         $t2, 0xC($t8)
    /* F16D8 150C4228 0D42B688 */  jal        func_150ADA20
    /* F16DC 150C422C AF010008 */   sw        $at, 0x8($t8)
    /* F16E0 150C4230 0D42B688 */  jal        func_150ADA20
    /* F16E4 150C4234 A3A2004C */   sb        $v0, 0x4C($sp)
    /* F16E8 150C4238 3C01442F */  lui        $at, (0x442F0000 >> 16)
    /* F16EC 150C423C 44810000 */  mtc1       $at, $f0
    /* F16F0 150C4240 A3A2004D */  sb         $v0, 0x4D($sp)
    /* F16F4 150C4244 E7A00088 */  swc1       $f0, 0x88($sp)
    /* F16F8 150C4248 E7A00084 */  swc1       $f0, 0x84($sp)
    /* F16FC 150C424C 0D42B688 */  jal        func_150ADA20
    /* F1700 150C4250 E7A00050 */   swc1      $f0, 0x50($sp)
    /* F1704 150C4254 24010006 */  addiu      $at, $zero, 0x6
    /* F1708 150C4258 0041001B */  divu       $zero, $v0, $at
    /* F170C 150C425C 00006810 */  mfhi       $t5
    /* F1710 150C4260 25AE0005 */  addiu      $t6, $t5, 0x5
    /* F1714 150C4264 0D42B688 */  jal        func_150ADA20
    /* F1718 150C4268 A3AE004E */   sb        $t6, 0x4E($sp)
    /* F171C 150C426C 24010006 */  addiu      $at, $zero, 0x6
    /* F1720 150C4270 0041001B */  divu       $zero, $v0, $at
    /* F1724 150C4274 00007810 */  mfhi       $t7
    /* F1728 150C4278 25E90005 */  addiu      $t1, $t7, 0x5
    /* F172C 150C427C 0D42B69A */  jal        func_150ADA68
    /* F1730 150C4280 A3A9004F */   sb        $t1, 0x4F($sp)
    /* F1734 150C4284 3C013E80 */  lui        $at, (0x3E800000 >> 16)
    /* F1738 150C4288 44812000 */  mtc1       $at, $f4
    /* F173C 150C428C 3C01800A */  lui        $at, %hi(D_800A03AC)
    /* F1740 150C4290 C42803AC */  lwc1       $f8, %lo(D_800A03AC)($at)
    /* F1744 150C4294 46040182 */  mul.s      $f6, $f0, $f4
    /* F1748 150C4298 C7B00050 */  lwc1       $f16, 0x50($sp)
    /* F174C 150C429C 46083280 */  add.s      $f10, $f6, $f8
    /* F1750 150C42A0 46105482 */  mul.s      $f18, $f10, $f16
    /* F1754 150C42A4 0D42B69A */  jal        func_150ADA68
    /* F1758 150C42A8 E7B20054 */   swc1      $f18, 0x54($sp)
    /* F175C 150C42AC 3C013E80 */  lui        $at, (0x3E800000 >> 16)
    /* F1760 150C42B0 44812000 */  mtc1       $at, $f4
    /* F1764 150C42B4 3C01800A */  lui        $at, %hi(D_800A03B0)
    /* F1768 150C42B8 C42803B0 */  lwc1       $f8, %lo(D_800A03B0)($at)
    /* F176C 150C42BC 46040182 */  mul.s      $f6, $f0, $f4
    /* F1770 150C42C0 C7B00050 */  lwc1       $f16, 0x50($sp)
    /* F1774 150C42C4 46083280 */  add.s      $f10, $f6, $f8
    /* F1778 150C42C8 46105482 */  mul.s      $f18, $f10, $f16
    /* F177C 150C42CC 0D42B688 */  jal        func_150ADA20
    /* F1780 150C42D0 E7B20058 */   swc1      $f18, 0x58($sp)
    /* F1784 150C42D4 30480003 */  andi       $t0, $v0, 0x3
    /* F1788 150C42D8 0008C080 */  sll        $t8, $t0, 2
    /* F178C 150C42DC 03B8C821 */  addu       $t9, $sp, $t8
    /* F1790 150C42E0 8F39003C */  lw         $t9, 0x3C($t9)
    /* F1794 150C42E4 3C03800A */  lui        $v1, %hi(D_800A5480)
    /* F1798 150C42E8 24635480 */  addiu      $v1, $v1, %lo(D_800A5480)
    /* F179C 150C42EC 8C610000 */  lw         $at, 0x0($v1)
    /* F17A0 150C42F0 3C0B0020 */  lui        $t3, (0x200005 >> 16)
    /* F17A4 150C42F4 240A2203 */  addiu      $t2, $zero, 0x2203
    /* F17A8 150C42F8 356B0005 */  ori        $t3, $t3, (0x200005 & 0xFFFF)
    /* F17AC 150C42FC 240C00FF */  addiu      $t4, $zero, 0xFF
    /* F17B0 150C4300 240D00FF */  addiu      $t5, $zero, 0xFF
    /* F17B4 150C4304 240E00FF */  addiu      $t6, $zero, 0xFF
    /* F17B8 150C4308 A7AA0064 */  sh         $t2, 0x64($sp)
    /* F17BC 150C430C AFAB005C */  sw         $t3, 0x5C($sp)
    /* F17C0 150C4310 AFA00060 */  sw         $zero, 0x60($sp)
    /* F17C4 150C4314 AFA00068 */  sw         $zero, 0x68($sp)
    /* F17C8 150C4318 AFA0006C */  sw         $zero, 0x6C($sp)
    /* F17CC 150C431C A3A00070 */  sb         $zero, 0x70($sp)
    /* F17D0 150C4320 A3A00071 */  sb         $zero, 0x71($sp)
    /* F17D4 150C4324 A3A00072 */  sb         $zero, 0x72($sp)
    /* F17D8 150C4328 A3AC0073 */  sb         $t4, 0x73($sp)
    /* F17DC 150C432C A3A00074 */  sb         $zero, 0x74($sp)
    /* F17E0 150C4330 A3A00075 */  sb         $zero, 0x75($sp)
    /* F17E4 150C4334 A3A00076 */  sb         $zero, 0x76($sp)
    /* F17E8 150C4338 A3AD0077 */  sb         $t5, 0x77($sp)
    /* F17EC 150C433C A3AE0078 */  sb         $t6, 0x78($sp)
    /* F17F0 150C4340 27AF008C */  addiu      $t7, $sp, 0x8C
    /* F17F4 150C4344 A3B90079 */  sb         $t9, 0x79($sp)
    /* F17F8 150C4348 ADE10000 */  sw         $at, 0x0($t7)
    /* F17FC 150C434C 8C780004 */  lw         $t8, 0x4($v1)
    /* F1800 150C4350 27B90098 */  addiu      $t9, $sp, 0x98
    /* F1804 150C4354 27AD00A4 */  addiu      $t5, $sp, 0xA4
    /* F1808 150C4358 ADF80004 */  sw         $t8, 0x4($t7)
    /* F180C 150C435C 8C610008 */  lw         $at, 0x8($v1)
    /* F1810 150C4360 44802000 */  mtc1       $zero, $f4
    /* F1814 150C4364 ADE10008 */  sw         $at, 0x8($t7)
    /* F1818 150C4368 8C610000 */  lw         $at, 0x0($v1)
    /* F181C 150C436C 240F0001 */  addiu      $t7, $zero, 0x1
    /* F1820 150C4370 AF210000 */  sw         $at, 0x0($t9)
    /* F1824 150C4374 8C6C0004 */  lw         $t4, 0x4($v1)
    /* F1828 150C4378 AF2C0004 */  sw         $t4, 0x4($t9)
    /* F182C 150C437C 8C610008 */  lw         $at, 0x8($v1)
    /* F1830 150C4380 AF210008 */  sw         $at, 0x8($t9)
    /* F1834 150C4384 8C610000 */  lw         $at, 0x0($v1)
    /* F1838 150C4388 ADA10000 */  sw         $at, 0x0($t5)
    /* F183C 150C438C 8C690004 */  lw         $t1, 0x4($v1)
    /* F1840 150C4390 ADA90004 */  sw         $t1, 0x4($t5)
    /* F1844 150C4394 8C610008 */  lw         $at, 0x8($v1)
    /* F1848 150C4398 ADA10008 */  sw         $at, 0x8($t5)
    /* F184C 150C439C 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* F1850 150C43A0 44813000 */  mtc1       $at, $f6
    /* F1854 150C43A4 A7AF007E */  sh         $t7, 0x7E($sp)
    /* F1858 150C43A8 E7A400B0 */  swc1       $f4, 0xB0($sp)
    /* F185C 150C43AC 0D42B688 */  jal        func_150ADA20
    /* F1860 150C43B0 E7A60080 */   swc1      $f6, 0x80($sp)
    /* F1864 150C43B4 30580001 */  andi       $t8, $v0, 0x1
    /* F1868 150C43B8 13000003 */  beqz       $t8, .L150C43C8
    /* F186C 150C43BC 00001825 */   or        $v1, $zero, $zero
    /* F1870 150C43C0 10000001 */  b          .L150C43C8
    /* F1874 150C43C4 24030040 */   addiu     $v1, $zero, 0x40
  .L150C43C8:
    /* F1878 150C43C8 0D42B688 */  jal        func_150ADA20
    /* F187C 150C43CC AFA30034 */   sw        $v1, 0x34($sp)
    /* F1880 150C43D0 304B0001 */  andi       $t3, $v0, 0x1
    /* F1884 150C43D4 11600003 */  beqz       $t3, .L150C43E4
    /* F1888 150C43D8 8FA30034 */   lw        $v1, 0x34($sp)
    /* F188C 150C43DC 10000002 */  b          .L150C43E8
    /* F1890 150C43E0 24020080 */   addiu     $v0, $zero, 0x80
  .L150C43E4:
    /* F1894 150C43E4 00001025 */  or         $v0, $zero, $zero
  .L150C43E8:
    /* F1898 150C43E8 0043C825 */  or         $t9, $v0, $v1
    /* F189C 150C43EC 372CC000 */  ori        $t4, $t9, 0xC000
    /* F18A0 150C43F0 2408012C */  addiu      $t0, $zero, 0x12C
    /* F18A4 150C43F4 AFAC00B4 */  sw         $t4, 0xB4($sp)
    /* F18A8 150C43F8 A7A80066 */  sh         $t0, 0x66($sp)
    /* F18AC 150C43FC 3C01800A */  lui        $at, %hi(D_800A03B4)
    /* F18B0 150C4400 C42803B4 */  lwc1       $f8, %lo(D_800A03B4)($at)
    /* F18B4 150C4404 8FA800FC */  lw         $t0, 0xFC($sp)
    /* F18B8 150C4408 93AC00FB */  lbu        $t4, 0xFB($sp)
    /* F18BC 150C440C 240E0001 */  addiu      $t6, $zero, 0x1
    /* F18C0 150C4410 240D00FF */  addiu      $t5, $zero, 0xFF
    /* F18C4 150C4414 24090006 */  addiu      $t1, $zero, 0x6
    /* F18C8 150C4418 240F0008 */  addiu      $t7, $zero, 0x8
    /* F18CC 150C441C 2418FFFF */  addiu      $t8, $zero, -0x1
    /* F18D0 150C4420 240B0026 */  addiu      $t3, $zero, 0x26
    /* F18D4 150C4424 240AFFFF */  addiu      $t2, $zero, -0x1
    /* F18D8 150C4428 241900FF */  addiu      $t9, $zero, 0xFF
    /* F18DC 150C442C A7AE007A */  sh         $t6, 0x7A($sp)
    /* F18E0 150C4430 A7AD007C */  sh         $t5, 0x7C($sp)
    /* F18E4 150C4434 A3A900BC */  sb         $t1, 0xBC($sp)
    /* F18E8 150C4438 A3AF00BD */  sb         $t7, 0xBD($sp)
    /* F18EC 150C443C A3B800C0 */  sb         $t8, 0xC0($sp)
    /* F18F0 150C4440 A3AB00BE */  sb         $t3, 0xBE($sp)
    /* F18F4 150C4444 A3AA00BF */  sb         $t2, 0xBF($sp)
    /* F18F8 150C4448 A3A000C1 */  sb         $zero, 0xC1($sp)
    /* F18FC 150C444C AFA000B8 */  sw         $zero, 0xB8($sp)
    /* F1900 150C4450 A3B900C2 */  sb         $t9, 0xC2($sp)
    /* F1904 150C4454 A7A000C4 */  sh         $zero, 0xC4($sp)
    /* F1908 150C4458 27A4005C */  addiu      $a0, $sp, 0x5C
    /* F190C 150C445C 24050001 */  addiu      $a1, $zero, 0x1
    /* F1910 150C4460 00003025 */  or         $a2, $zero, $zero
    /* F1914 150C4464 24070010 */  addiu      $a3, $zero, 0x10
    /* F1918 150C4468 E7A800C8 */  swc1       $f8, 0xC8($sp)
    /* F191C 150C446C AFA80014 */  sw         $t0, 0x14($sp)
    /* F1920 150C4470 0D44C0A0 */  jal        func_15130280
    /* F1924 150C4474 AFAC0010 */   sw        $t4, 0x10($sp)
    /* F1928 150C4478 8FA30030 */  lw         $v1, 0x30($sp)
    /* F192C 150C447C 244400A8 */  addiu      $a0, $v0, 0xA8
    /* F1930 150C4480 10400004 */  beqz       $v0, .L150C4494
    /* F1934 150C4484 AC62000C */   sw        $v0, 0xC($v1)
    /* F1938 150C4488 27A5004C */  addiu      $a1, $sp, 0x4C
    /* F193C 150C448C 0C008BB0 */  jal        memcpy
    /* F1940 150C4490 24060010 */   addiu     $a2, $zero, 0x10
  .L150C4494:
    /* F1944 150C4494 8FBF002C */  lw         $ra, 0x2C($sp)
    /* F1948 150C4498 27BD00F0 */  addiu      $sp, $sp, 0xF0
    /* F194C 150C449C 03E00008 */  jr         $ra
    /* F1950 150C44A0 00000000 */   nop
endlabel func_150C4120
