glabel func_151C1180
    /* 1EE630 151C1180 27BDFF18 */  addiu      $sp, $sp, -0xE8
    /* 1EE634 151C1184 AFB10048 */  sw         $s1, 0x48($sp)
    /* 1EE638 151C1188 3C03800C */  lui        $v1, %hi(D_800BE9A4)
    /* 1EE63C 151C118C 2463E9A4 */  addiu      $v1, $v1, %lo(D_800BE9A4)
    /* 1EE640 151C1190 00808825 */  or         $s1, $a0, $zero
    /* 1EE644 151C1194 AFBF004C */  sw         $ra, 0x4C($sp)
    /* 1EE648 151C1198 AFB00044 */  sw         $s0, 0x44($sp)
    /* 1EE64C 151C119C C4620000 */  lwc1       $f2, 0x0($v1)
    /* 1EE650 151C11A0 C62401D4 */  lwc1       $f4, 0x1D4($s1)
    /* 1EE654 151C11A4 26300170 */  addiu      $s0, $s1, 0x170
    /* 1EE658 151C11A8 26240038 */  addiu      $a0, $s1, 0x38
    /* 1EE65C 151C11AC 4602203C */  c.lt.s     $f4, $f2
    /* 1EE660 151C11B0 27A500D4 */  addiu      $a1, $sp, 0xD4
    /* 1EE664 151C11B4 27A600C8 */  addiu      $a2, $sp, 0xC8
    /* 1EE668 151C11B8 45020008 */  bc1fl      .L151C11DC
    /* 1EE66C 151C11BC C60A0068 */   lwc1      $f10, 0x68($s0)
    /* 1EE670 151C11C0 26300170 */  addiu      $s0, $s1, 0x170
    /* 1EE674 151C11C4 C6060068 */  lwc1       $f6, 0x68($s0)
    /* 1EE678 151C11C8 C6080064 */  lwc1       $f8, 0x64($s0)
    /* 1EE67C 151C11CC 46083002 */  mul.s      $f0, $f6, $f8
    /* 1EE680 151C11D0 10000005 */  b          .L151C11E8
    /* 1EE684 151C11D4 C6100038 */   lwc1      $f16, 0x38($s0)
    /* 1EE688 151C11D8 C60A0068 */  lwc1       $f10, 0x68($s0)
  .L151C11DC:
    /* 1EE68C 151C11DC 46025002 */  mul.s      $f0, $f10, $f2
    /* 1EE690 151C11E0 00000000 */  nop
    /* 1EE694 151C11E4 C6100038 */  lwc1       $f16, 0x38($s0)
  .L151C11E8:
    /* 1EE698 151C11E8 3C02800E */  lui        $v0, %hi(D_800E0930)
    /* 1EE69C 151C11EC 8C420930 */  lw         $v0, %lo(D_800E0930)($v0)
    /* 1EE6A0 151C11F0 46008482 */  mul.s      $f18, $f16, $f0
    /* 1EE6A4 151C11F4 E7B200D4 */  swc1       $f18, 0xD4($sp)
    /* 1EE6A8 151C11F8 C604003C */  lwc1       $f4, 0x3C($s0)
    /* 1EE6AC 151C11FC 46002182 */  mul.s      $f6, $f4, $f0
    /* 1EE6B0 151C1200 E7A600D8 */  swc1       $f6, 0xD8($sp)
    /* 1EE6B4 151C1204 C6080040 */  lwc1       $f8, 0x40($s0)
    /* 1EE6B8 151C1208 46004282 */  mul.s      $f10, $f8, $f0
    /* 1EE6BC 151C120C 10400020 */  beqz       $v0, .L151C1290
    /* 1EE6C0 151C1210 E7AA00DC */   swc1      $f10, 0xDC($sp)
    /* 1EE6C4 151C1214 0040F809 */  jalr       $v0
    /* 1EE6C8 151C1218 E7A000E0 */   swc1      $f0, 0xE0($sp)
    /* 1EE6CC 151C121C 3C03800C */  lui        $v1, %hi(D_800BE9A4)
    /* 1EE6D0 151C1220 2463E9A4 */  addiu      $v1, $v1, %lo(D_800BE9A4)
    /* 1EE6D4 151C1224 1040001A */  beqz       $v0, .L151C1290
    /* 1EE6D8 151C1228 C7A000E0 */   lwc1      $f0, 0xE0($sp)
    /* 1EE6DC 151C122C 00002025 */  or         $a0, $zero, $zero
    /* 1EE6E0 151C1230 8FA500C8 */  lw         $a1, 0xC8($sp)
    /* 1EE6E4 151C1234 8FA600CC */  lw         $a2, 0xCC($sp)
    /* 1EE6E8 151C1238 8FA700D0 */  lw         $a3, 0xD0($sp)
    /* 1EE6EC 151C123C 0D41568B */  jal        func_15055A2C
    /* 1EE6F0 151C1240 AFA00010 */   sw        $zero, 0x10($sp)
    /* 1EE6F4 151C1244 26050038 */  addiu      $a1, $s0, 0x38
    /* 1EE6F8 151C1248 8E06006C */  lw         $a2, 0x6C($s0)
    /* 1EE6FC 151C124C 92070092 */  lbu        $a3, 0x92($s0)
    /* 1EE700 151C1250 AFA50054 */  sw         $a1, 0x54($sp)
    /* 1EE704 151C1254 AFA00010 */  sw         $zero, 0x10($sp)
    /* 1EE708 151C1258 0D470595 */  jal        func_151C1654
    /* 1EE70C 151C125C 27A400C8 */   addiu     $a0, $sp, 0xC8
    /* 1EE710 151C1260 920200C8 */  lbu        $v0, 0xC8($s0)
    /* 1EE714 151C1264 92380001 */  lbu        $t8, 0x1($s1)
    /* 1EE718 151C1268 9227000C */  lbu        $a3, 0xC($s1)
    /* 1EE71C 151C126C 304E0001 */  andi       $t6, $v0, 0x1
    /* 1EE720 151C1270 2DCF0001 */  sltiu      $t7, $t6, 0x1
    /* 1EE724 151C1274 8FA50054 */  lw         $a1, 0x54($sp)
    /* 1EE728 151C1278 31E600FF */  andi       $a2, $t7, 0xFF
    /* 1EE72C 151C127C 27A400C8 */  addiu      $a0, $sp, 0xC8
    /* 1EE730 151C1280 0D46FF68 */  jal        func_151BFDA0
    /* 1EE734 151C1284 AFB80010 */   sw        $t8, 0x10($sp)
    /* 1EE738 151C1288 100000B4 */  b          .L151C155C
    /* 1EE73C 151C128C 00001025 */   or        $v0, $zero, $zero
  .L151C1290:
    /* 1EE740 151C1290 44808000 */  mtc1       $zero, $f16
    /* 1EE744 151C1294 00000000 */  nop
    /* 1EE748 151C1298 46100032 */  c.eq.s     $f0, $f16
    /* 1EE74C 151C129C 00000000 */  nop
    /* 1EE750 151C12A0 45030038 */  bc1tl      .L151C1384
    /* 1EE754 151C12A4 C6280044 */   lwc1      $f8, 0x44($s1)
    /* 1EE758 151C12A8 8E04006C */  lw         $a0, 0x6C($s0)
    /* 1EE75C 151C12AC 8E250038 */  lw         $a1, 0x38($s1)
    /* 1EE760 151C12B0 8E26003C */  lw         $a2, 0x3C($s1)
    /* 1EE764 151C12B4 8E270040 */  lw         $a3, 0x40($s1)
    /* 1EE768 151C12B8 C7B200D4 */  lwc1       $f18, 0xD4($sp)
    /* 1EE76C 151C12BC C7A400D8 */  lwc1       $f4, 0xD8($sp)
    /* 1EE770 151C12C0 C7A600DC */  lwc1       $f6, 0xDC($sp)
    /* 1EE774 151C12C4 27B90064 */  addiu      $t9, $sp, 0x64
    /* 1EE778 151C12C8 24080001 */  addiu      $t0, $zero, 0x1
    /* 1EE77C 151C12CC 24090001 */  addiu      $t1, $zero, 0x1
    /* 1EE780 151C12D0 240A0003 */  addiu      $t2, $zero, 0x3
    /* 1EE784 151C12D4 260B0070 */  addiu      $t3, $s0, 0x70
    /* 1EE788 151C12D8 AFAB0034 */  sw         $t3, 0x34($sp)
    /* 1EE78C 151C12DC AFAA0030 */  sw         $t2, 0x30($sp)
    /* 1EE790 151C12E0 AFA9002C */  sw         $t1, 0x2C($sp)
    /* 1EE794 151C12E4 AFA80024 */  sw         $t0, 0x24($sp)
    /* 1EE798 151C12E8 AFB9001C */  sw         $t9, 0x1C($sp)
    /* 1EE79C 151C12EC AFA00028 */  sw         $zero, 0x28($sp)
    /* 1EE7A0 151C12F0 E7A00020 */  swc1       $f0, 0x20($sp)
    /* 1EE7A4 151C12F4 E7B20010 */  swc1       $f18, 0x10($sp)
    /* 1EE7A8 151C12F8 E7A40014 */  swc1       $f4, 0x14($sp)
    /* 1EE7AC 151C12FC E7A60018 */  swc1       $f6, 0x18($sp)
    /* 1EE7B0 151C1300 8E0C00CC */  lw         $t4, 0xCC($s0)
    /* 1EE7B4 151C1304 0D4205A4 */  jal        func_15081690
    /* 1EE7B8 151C1308 AFAC0038 */   sw        $t4, 0x38($sp)
    /* 1EE7BC 151C130C 93AD00BD */  lbu        $t5, 0xBD($sp)
    /* 1EE7C0 151C1310 3C03800C */  lui        $v1, %hi(D_800BE9A4)
    /* 1EE7C4 151C1314 2463E9A4 */  addiu      $v1, $v1, %lo(D_800BE9A4)
    /* 1EE7C8 151C1318 29A10002 */  slti       $at, $t5, 0x2
    /* 1EE7CC 151C131C 14200018 */  bnez       $at, .L151C1380
    /* 1EE7D0 151C1320 24040001 */   addiu     $a0, $zero, 0x1
    /* 1EE7D4 151C1324 8FA5006C */  lw         $a1, 0x6C($sp)
    /* 1EE7D8 151C1328 8FA60070 */  lw         $a2, 0x70($sp)
    /* 1EE7DC 151C132C 8FA70074 */  lw         $a3, 0x74($sp)
    /* 1EE7E0 151C1330 0D41568B */  jal        func_15055A2C
    /* 1EE7E4 151C1334 AFA00010 */   sw        $zero, 0x10($sp)
    /* 1EE7E8 151C1338 8E06006C */  lw         $a2, 0x6C($s0)
    /* 1EE7EC 151C133C 92070092 */  lbu        $a3, 0x92($s0)
    /* 1EE7F0 151C1340 AFA00010 */  sw         $zero, 0x10($sp)
    /* 1EE7F4 151C1344 27A4006C */  addiu      $a0, $sp, 0x6C
    /* 1EE7F8 151C1348 0D470595 */  jal        func_151C1654
    /* 1EE7FC 151C134C 26050038 */   addiu     $a1, $s0, 0x38
    /* 1EE800 151C1350 920200C8 */  lbu        $v0, 0xC8($s0)
    /* 1EE804 151C1354 92380001 */  lbu        $t8, 0x1($s1)
    /* 1EE808 151C1358 9227000C */  lbu        $a3, 0xC($s1)
    /* 1EE80C 151C135C 304E0001 */  andi       $t6, $v0, 0x1
    /* 1EE810 151C1360 2DCF0001 */  sltiu      $t7, $t6, 0x1
    /* 1EE814 151C1364 31E600FF */  andi       $a2, $t7, 0xFF
    /* 1EE818 151C1368 27A4006C */  addiu      $a0, $sp, 0x6C
    /* 1EE81C 151C136C 8FA50064 */  lw         $a1, 0x64($sp)
    /* 1EE820 151C1370 0D470026 */  jal        func_151C0098
    /* 1EE824 151C1374 AFB80010 */   sw        $t8, 0x10($sp)
    /* 1EE828 151C1378 10000078 */  b          .L151C155C
    /* 1EE82C 151C137C 00001025 */   or        $v0, $zero, $zero
  .L151C1380:
    /* 1EE830 151C1380 C6280044 */  lwc1       $f8, 0x44($s1)
  .L151C1384:
    /* 1EE834 151C1384 C46A0000 */  lwc1       $f10, 0x0($v1)
    /* 1EE838 151C1388 C6320038 */  lwc1       $f18, 0x38($s1)
    /* 1EE83C 151C138C C6260048 */  lwc1       $f6, 0x48($s1)
    /* 1EE840 151C1390 460A4402 */  mul.s      $f16, $f8, $f10
    /* 1EE844 151C1394 46109100 */  add.s      $f4, $f18, $f16
    /* 1EE848 151C1398 C632003C */  lwc1       $f18, 0x3C($s1)
    /* 1EE84C 151C139C E6240038 */  swc1       $f4, 0x38($s1)
    /* 1EE850 151C13A0 C4680000 */  lwc1       $f8, 0x0($v1)
    /* 1EE854 151C13A4 C624004C */  lwc1       $f4, 0x4C($s1)
    /* 1EE858 151C13A8 46083282 */  mul.s      $f10, $f6, $f8
    /* 1EE85C 151C13AC 460A9400 */  add.s      $f16, $f18, $f10
    /* 1EE860 151C13B0 C6320040 */  lwc1       $f18, 0x40($s1)
    /* 1EE864 151C13B4 E630003C */  swc1       $f16, 0x3C($s1)
    /* 1EE868 151C13B8 C4660000 */  lwc1       $f6, 0x0($v1)
    /* 1EE86C 151C13BC 46062202 */  mul.s      $f8, $f4, $f6
    /* 1EE870 151C13C0 46089280 */  add.s      $f10, $f18, $f8
    /* 1EE874 151C13C4 E62A0040 */  swc1       $f10, 0x40($s1)
    /* 1EE878 151C13C8 921900C8 */  lbu        $t9, 0xC8($s0)
    /* 1EE87C 151C13CC 33280001 */  andi       $t0, $t9, 0x1
    /* 1EE880 151C13D0 51000019 */  beql       $t0, $zero, .L151C1438
    /* 1EE884 151C13D4 C6120064 */   lwc1      $f18, 0x64($s0)
    /* 1EE888 151C13D8 44801000 */  mtc1       $zero, $f2
    /* 1EE88C 151C13DC C6000094 */  lwc1       $f0, 0x94($s0)
    /* 1EE890 151C13E0 4600103C */  c.lt.s     $f2, $f0
    /* 1EE894 151C13E4 00000000 */  nop
    /* 1EE898 151C13E8 45020013 */  bc1fl      .L151C1438
    /* 1EE89C 151C13EC C6120064 */   lwc1      $f18, 0x64($s0)
    /* 1EE8A0 151C13F0 C4700000 */  lwc1       $f16, 0x0($v1)
    /* 1EE8A4 151C13F4 26040098 */  addiu      $a0, $s0, 0x98
    /* 1EE8A8 151C13F8 260500A4 */  addiu      $a1, $s0, 0xA4
    /* 1EE8AC 151C13FC 46100101 */  sub.s      $f4, $f0, $f16
    /* 1EE8B0 151C1400 24060002 */  addiu      $a2, $zero, 0x2
    /* 1EE8B4 151C1404 E6040094 */  swc1       $f4, 0x94($s0)
    /* 1EE8B8 151C1408 C6060094 */  lwc1       $f6, 0x94($s0)
    /* 1EE8BC 151C140C 4602303E */  c.le.s     $f6, $f2
    /* 1EE8C0 151C1410 00000000 */  nop
    /* 1EE8C4 151C1414 45020008 */  bc1fl      .L151C1438
    /* 1EE8C8 151C1418 C6120064 */   lwc1      $f18, 0x64($s0)
    /* 1EE8CC 151C141C 92290001 */  lbu        $t1, 0x1($s1)
    /* 1EE8D0 151C1420 9227000C */  lbu        $a3, 0xC($s1)
    /* 1EE8D4 151C1424 0D46AF90 */  jal        func_151ABE40
    /* 1EE8D8 151C1428 AFA90010 */   sw        $t1, 0x10($sp)
    /* 1EE8DC 151C142C 3C03800C */  lui        $v1, %hi(D_800BE9A4)
    /* 1EE8E0 151C1430 2463E9A4 */  addiu      $v1, $v1, %lo(D_800BE9A4)
    /* 1EE8E4 151C1434 C6120064 */  lwc1       $f18, 0x64($s0)
  .L151C1438:
    /* 1EE8E8 151C1438 C4680000 */  lwc1       $f8, 0x0($v1)
    /* 1EE8EC 151C143C 44801000 */  mtc1       $zero, $f2
    /* 1EE8F0 151C1440 46089281 */  sub.s      $f10, $f18, $f8
    /* 1EE8F4 151C1444 E60A0064 */  swc1       $f10, 0x64($s0)
    /* 1EE8F8 151C1448 C6100064 */  lwc1       $f16, 0x64($s0)
    /* 1EE8FC 151C144C 4602803E */  c.le.s     $f16, $f2
    /* 1EE900 151C1450 00000000 */  nop
    /* 1EE904 151C1454 45020023 */  bc1fl      .L151C14E4
    /* 1EE908 151C1458 8E030080 */   lw        $v1, 0x80($s0)
    /* 1EE90C 151C145C 920A0059 */  lbu        $t2, 0x59($s0)
    /* 1EE910 151C1460 24010001 */  addiu      $at, $zero, 0x1
    /* 1EE914 151C1464 00002025 */  or         $a0, $zero, $zero
    /* 1EE918 151C1468 1541001B */  bne        $t2, $at, .L151C14D8
    /* 1EE91C 151C146C 00000000 */   nop
    /* 1EE920 151C1470 8E050008 */  lw         $a1, 0x8($s0)
    /* 1EE924 151C1474 8E06000C */  lw         $a2, 0xC($s0)
    /* 1EE928 151C1478 8E070010 */  lw         $a3, 0x10($s0)
    /* 1EE92C 151C147C 0D41568B */  jal        func_15055A2C
    /* 1EE930 151C1480 AFA00010 */   sw        $zero, 0x10($sp)
    /* 1EE934 151C1484 8E06006C */  lw         $a2, 0x6C($s0)
    /* 1EE938 151C1488 92070092 */  lbu        $a3, 0x92($s0)
    /* 1EE93C 151C148C 26040008 */  addiu      $a0, $s0, 0x8
    /* 1EE940 151C1490 26020044 */  addiu      $v0, $s0, 0x44
    /* 1EE944 151C1494 AFA20010 */  sw         $v0, 0x10($sp)
    /* 1EE948 151C1498 AFA20054 */  sw         $v0, 0x54($sp)
    /* 1EE94C 151C149C AFA40050 */  sw         $a0, 0x50($sp)
    /* 1EE950 151C14A0 0D470595 */  jal        func_151C1654
    /* 1EE954 151C14A4 26050038 */   addiu     $a1, $s0, 0x38
    /* 1EE958 151C14A8 922D000C */  lbu        $t5, 0xC($s1)
    /* 1EE95C 151C14AC 920200C8 */  lbu        $v0, 0xC8($s0)
    /* 1EE960 151C14B0 8FA40054 */  lw         $a0, 0x54($sp)
    /* 1EE964 151C14B4 AFAD0010 */  sw         $t5, 0x10($sp)
    /* 1EE968 151C14B8 922E0001 */  lbu        $t6, 0x1($s1)
    /* 1EE96C 151C14BC 304B0001 */  andi       $t3, $v0, 0x1
    /* 1EE970 151C14C0 2D6C0001 */  sltiu      $t4, $t3, 0x1
    /* 1EE974 151C14C4 318700FF */  andi       $a3, $t4, 0xFF
    /* 1EE978 151C14C8 8FA50050 */  lw         $a1, 0x50($sp)
    /* 1EE97C 151C14CC 26260044 */  addiu      $a2, $s1, 0x44
    /* 1EE980 151C14D0 0D46FFA1 */  jal        func_151BFE84
    /* 1EE984 151C14D4 AFAE0014 */   sw        $t6, 0x14($sp)
  .L151C14D8:
    /* 1EE988 151C14D8 10000020 */  b          .L151C155C
    /* 1EE98C 151C14DC 00001025 */   or        $v0, $zero, $zero
    /* 1EE990 151C14E0 8E030080 */  lw         $v1, 0x80($s0)
  .L151C14E4:
    /* 1EE994 151C14E4 50600014 */  beql       $v1, $zero, .L151C1538
    /* 1EE998 151C14E8 8E020084 */   lw        $v0, 0x84($s0)
    /* 1EE99C 151C14EC C6240038 */  lwc1       $f4, 0x38($s1)
    /* 1EE9A0 151C14F0 8C790014 */  lw         $t9, 0x14($v1)
    /* 1EE9A4 151C14F4 4600218D */  trunc.w.s  $f6, $f4
    /* 1EE9A8 151C14F8 44183000 */  mfc1       $t8, $f6
    /* 1EE9AC 151C14FC 00000000 */  nop
    /* 1EE9B0 151C1500 A738000E */  sh         $t8, 0xE($t9)
    /* 1EE9B4 151C1504 C632003C */  lwc1       $f18, 0x3C($s1)
    /* 1EE9B8 151C1508 8C6A0014 */  lw         $t2, 0x14($v1)
    /* 1EE9BC 151C150C 4600920D */  trunc.w.s  $f8, $f18
    /* 1EE9C0 151C1510 44094000 */  mfc1       $t1, $f8
    /* 1EE9C4 151C1514 00000000 */  nop
    /* 1EE9C8 151C1518 A5490010 */  sh         $t1, 0x10($t2)
    /* 1EE9CC 151C151C C62A0040 */  lwc1       $f10, 0x40($s1)
    /* 1EE9D0 151C1520 8C6D0014 */  lw         $t5, 0x14($v1)
    /* 1EE9D4 151C1524 4600540D */  trunc.w.s  $f16, $f10
    /* 1EE9D8 151C1528 440C8000 */  mfc1       $t4, $f16
    /* 1EE9DC 151C152C 00000000 */  nop
    /* 1EE9E0 151C1530 A5AC0012 */  sh         $t4, 0x12($t5)
    /* 1EE9E4 151C1534 8E020084 */  lw         $v0, 0x84($s0)
  .L151C1538:
    /* 1EE9E8 151C1538 50400008 */  beql       $v0, $zero, .L151C155C
    /* 1EE9EC 151C153C 24020001 */   addiu     $v0, $zero, 0x1
    /* 1EE9F0 151C1540 8E210038 */  lw         $at, 0x38($s1)
    /* 1EE9F4 151C1544 AC410040 */  sw         $at, 0x40($v0)
    /* 1EE9F8 151C1548 8E2F003C */  lw         $t7, 0x3C($s1)
    /* 1EE9FC 151C154C AC4F0044 */  sw         $t7, 0x44($v0)
    /* 1EEA00 151C1550 8E210040 */  lw         $at, 0x40($s1)
    /* 1EEA04 151C1554 AC410048 */  sw         $at, 0x48($v0)
    /* 1EEA08 151C1558 24020001 */  addiu      $v0, $zero, 0x1
  .L151C155C:
    /* 1EEA0C 151C155C 8FBF004C */  lw         $ra, 0x4C($sp)
    /* 1EEA10 151C1560 8FB00044 */  lw         $s0, 0x44($sp)
    /* 1EEA14 151C1564 8FB10048 */  lw         $s1, 0x48($sp)
    /* 1EEA18 151C1568 03E00008 */  jr         $ra
    /* 1EEA1C 151C156C 27BD00E8 */   addiu     $sp, $sp, 0xE8
endlabel func_151C1180
