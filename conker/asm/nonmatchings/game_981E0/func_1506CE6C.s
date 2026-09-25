glabel func_1506CE6C
    /* 9A31C 1506CE6C 27BDFF60 */  addiu      $sp, $sp, -0xA0
    /* 9A320 1506CE70 44800000 */  mtc1       $zero, $f0
    /* 9A324 1506CE74 AFBF0034 */  sw         $ra, 0x34($sp)
    /* 9A328 1506CE78 3C014234 */  lui        $at, (0x42340000 >> 16)
    /* 9A32C 1506CE7C 44812000 */  mtc1       $at, $f4
    /* 9A330 1506CE80 3C01800A */  lui        $at, %hi(D_80099CD8)
    /* 9A334 1506CE84 C4269CD8 */  lwc1       $f6, %lo(D_80099CD8)($at)
    /* 9A338 1506CE88 3C013F00 */  lui        $at, (0x3F000000 >> 16)
    /* 9A33C 1506CE8C 44814000 */  mtc1       $at, $f8
    /* 9A340 1506CE90 3C04800D */  lui        $a0, %hi(D_800D154C)
    /* 9A344 1506CE94 8C84154C */  lw         $a0, %lo(D_800D154C)($a0)
    /* 9A348 1506CE98 AFA00054 */  sw         $zero, 0x54($sp)
    /* 9A34C 1506CE9C E7A00088 */  swc1       $f0, 0x88($sp)
    /* 9A350 1506CEA0 E7A40094 */  swc1       $f4, 0x94($sp)
    /* 9A354 1506CEA4 E7A6008C */  swc1       $f6, 0x8C($sp)
    /* 9A358 1506CEA8 E7A8007C */  swc1       $f8, 0x7C($sp)
    /* 9A35C 1506CEAC 948E007A */  lhu        $t6, 0x7A($a0)
    /* 9A360 1506CEB0 3C013BB4 */  lui        $at, (0x3BB40000 >> 16)
    /* 9A364 1506CEB4 44813000 */  mtc1       $at, $f6
    /* 9A368 1506CEB8 25CF4000 */  addiu      $t7, $t6, 0x4000
    /* 9A36C 1506CEBC 448F5000 */  mtc1       $t7, $f10
    /* 9A370 1506CEC0 3C0A800D */  lui        $t2, %hi(D_800D1580)
    /* 9A374 1506CEC4 8D4A1580 */  lw         $t2, %lo(D_800D1580)($t2)
    /* 9A378 1506CEC8 46805120 */  cvt.s.w    $f4, $f10
    /* 9A37C 1506CECC 24010005 */  addiu      $at, $zero, 0x5
    /* 9A380 1506CED0 2408FFFF */  addiu      $t0, $zero, -0x1
    /* 9A384 1506CED4 00004825 */  or         $t1, $zero, $zero
    /* 9A388 1506CED8 AFA00050 */  sw         $zero, 0x50($sp)
    /* 9A38C 1506CEDC 46062202 */  mul.s      $f8, $f4, $f6
    /* 9A390 1506CEE0 11410006 */  beq        $t2, $at, .L1506CEFC
    /* 9A394 1506CEE4 E7A80090 */   swc1      $f8, 0x90($sp)
    /* 9A398 1506CEE8 24010009 */  addiu      $at, $zero, 0x9
    /* 9A39C 1506CEEC 11410003 */  beq        $t2, $at, .L1506CEFC
    /* 9A3A0 1506CEF0 2401000A */   addiu     $at, $zero, 0xA
    /* 9A3A4 1506CEF4 55410003 */  bnel       $t2, $at, .L1506CF04
    /* 9A3A8 1506CEF8 2401FFFF */   addiu     $at, $zero, -0x1
  .L1506CEFC:
    /* 9A3AC 1506CEFC 24080003 */  addiu      $t0, $zero, 0x3
    /* 9A3B0 1506CF00 2401FFFF */  addiu      $at, $zero, -0x1
  .L1506CF04:
    /* 9A3B4 1506CF04 51010048 */  beql       $t0, $at, .L1506D028
    /* 9A3B8 1506CF08 8C820318 */   lw        $v0, 0x318($a0)
    /* 9A3BC 1506CF0C 8C8301D4 */  lw         $v1, 0x1D4($a0)
    /* 9A3C0 1506CF10 0008C180 */  sll        $t8, $t0, 6
    /* 9A3C4 1506CF14 3C073F80 */  lui        $a3, (0x3F800000 >> 16)
    /* 9A3C8 1506CF18 10600040 */  beqz       $v1, .L1506D01C
    /* 9A3CC 1506CF1C 00782021 */   addu      $a0, $v1, $t8
    /* 9A3D0 1506CF20 44050000 */  mfc1       $a1, $f0
    /* 9A3D4 1506CF24 44060000 */  mfc1       $a2, $f0
    /* 9A3D8 1506CF28 27B90070 */  addiu      $t9, $sp, 0x70
    /* 9A3DC 1506CF2C 27AB006C */  addiu      $t3, $sp, 0x6C
    /* 9A3E0 1506CF30 27AC0068 */  addiu      $t4, $sp, 0x68
    /* 9A3E4 1506CF34 AFAC0018 */  sw         $t4, 0x18($sp)
    /* 9A3E8 1506CF38 AFAB0014 */  sw         $t3, 0x14($sp)
    /* 9A3EC 1506CF3C AFB90010 */  sw         $t9, 0x10($sp)
    /* 9A3F0 1506CF40 AFA4003C */  sw         $a0, 0x3C($sp)
    /* 9A3F4 1506CF44 AFA90058 */  sw         $t1, 0x58($sp)
    /* 9A3F8 1506CF48 0D429E58 */  jal        func_150A7960
    /* 9A3FC 1506CF4C AFAA0098 */   sw        $t2, 0x98($sp)
    /* 9A400 1506CF50 8FA4003C */  lw         $a0, 0x3C($sp)
    /* 9A404 1506CF54 C7AA0070 */  lwc1       $f10, 0x70($sp)
    /* 9A408 1506CF58 C7A8006C */  lwc1       $f8, 0x6C($sp)
    /* 9A40C 1506CF5C C4840030 */  lwc1       $f4, 0x30($a0)
    /* 9A410 1506CF60 46045301 */  sub.s      $f12, $f10, $f4
    /* 9A414 1506CF64 E7AC0070 */  swc1       $f12, 0x70($sp)
    /* 9A418 1506CF68 C48A0034 */  lwc1       $f10, 0x34($a0)
    /* 9A41C 1506CF6C 460A4101 */  sub.s      $f4, $f8, $f10
    /* 9A420 1506CF70 C7A80068 */  lwc1       $f8, 0x68($sp)
    /* 9A424 1506CF74 E7A4006C */  swc1       $f4, 0x6C($sp)
    /* 9A428 1506CF78 C48A0038 */  lwc1       $f10, 0x38($a0)
    /* 9A42C 1506CF7C 460A4381 */  sub.s      $f14, $f8, $f10
    /* 9A430 1506CF80 0D412128 */  jal        func_150484A0
    /* 9A434 1506CF84 E7AE0068 */   swc1      $f14, 0x68($sp)
    /* 9A438 1506CF88 C7B00070 */  lwc1       $f16, 0x70($sp)
    /* 9A43C 1506CF8C C7B20068 */  lwc1       $f18, 0x68($sp)
    /* 9A440 1506CF90 46000086 */  mov.s      $f2, $f0
    /* 9A444 1506CF94 46108202 */  mul.s      $f8, $f16, $f16
    /* 9A448 1506CF98 E7A20064 */  swc1       $f2, 0x64($sp)
    /* 9A44C 1506CF9C C7AC006C */  lwc1       $f12, 0x6C($sp)
    /* 9A450 1506CFA0 46129282 */  mul.s      $f10, $f18, $f18
    /* 9A454 1506CFA4 460A4000 */  add.s      $f0, $f8, $f10
    /* 9A458 1506CFA8 0D412128 */  jal        func_150484A0
    /* 9A45C 1506CFAC 46000384 */   sqrt.s    $f14, $f0
    /* 9A460 1506CFB0 3C01800A */  lui        $at, %hi(D_80099CDC)
    /* 9A464 1506CFB4 C4309CDC */  lwc1       $f16, %lo(D_80099CDC)($at)
    /* 9A468 1506CFB8 C7A20064 */  lwc1       $f2, 0x64($sp)
    /* 9A46C 1506CFBC 3C014334 */  lui        $at, (0x43340000 >> 16)
    /* 9A470 1506CFC0 44819000 */  mtc1       $at, $f18
    /* 9A474 1506CFC4 46101082 */  mul.s      $f2, $f2, $f16
    /* 9A478 1506CFC8 8FA90058 */  lw         $t1, 0x58($sp)
    /* 9A47C 1506CFCC 8FAA0098 */  lw         $t2, 0x98($sp)
    /* 9A480 1506CFD0 46100302 */  mul.s      $f12, $f0, $f16
    /* 9A484 1506CFD4 44800000 */  mtc1       $zero, $f0
    /* 9A488 1506CFD8 3C0143B4 */  lui        $at, (0x43B40000 >> 16)
    /* 9A48C 1506CFDC 4602903C */  c.lt.s     $f18, $f2
    /* 9A490 1506CFE0 46006386 */  mov.s      $f14, $f12
    /* 9A494 1506CFE4 45020005 */  bc1fl      .L1506CFFC
    /* 9A498 1506CFE8 460C903C */   c.lt.s    $f18, $f12
    /* 9A49C 1506CFEC 44813000 */  mtc1       $at, $f6
    /* 9A4A0 1506CFF0 00000000 */  nop
    /* 9A4A4 1506CFF4 46061081 */  sub.s      $f2, $f2, $f6
    /* 9A4A8 1506CFF8 460C903C */  c.lt.s     $f18, $f12
  .L1506CFFC:
    /* 9A4AC 1506CFFC 3C0143B4 */  lui        $at, (0x43B40000 >> 16)
    /* 9A4B0 1506D000 45020005 */  bc1fl      .L1506D018
    /* 9A4B4 1506D004 E7A20090 */   swc1      $f2, 0x90($sp)
    /* 9A4B8 1506D008 44812000 */  mtc1       $at, $f4
    /* 9A4BC 1506D00C 00000000 */  nop
    /* 9A4C0 1506D010 46046381 */  sub.s      $f14, $f12, $f4
    /* 9A4C4 1506D014 E7A20090 */  swc1       $f2, 0x90($sp)
  .L1506D018:
    /* 9A4C8 1506D018 E7AE0094 */  swc1       $f14, 0x94($sp)
  .L1506D01C:
    /* 9A4CC 1506D01C 10000033 */  b          .L1506D0EC
    /* 9A4D0 1506D020 2558FFFF */   addiu     $t8, $t2, -0x1
    /* 9A4D4 1506D024 8C820318 */  lw         $v0, 0x318($a0)
  .L1506D028:
    /* 9A4D8 1506D028 5040002A */  beql       $v0, $zero, .L1506D0D4
    /* 9A4DC 1506D02C 808E01D1 */   lb        $t6, 0x1D1($a0)
    /* 9A4E0 1506D030 8C4D002C */  lw         $t5, 0x2C($v0)
    /* 9A4E4 1506D034 24010100 */  addiu      $at, $zero, 0x100
    /* 9A4E8 1506D038 55A10026 */  bnel       $t5, $at, .L1506D0D4
    /* 9A4EC 1506D03C 808E01D1 */   lb        $t6, 0x1D1($a0)
    /* 9A4F0 1506D040 C4480780 */  lwc1       $f8, 0x780($v0)
    /* 9A4F4 1506D044 3C014270 */  lui        $at, (0x42700000 >> 16)
    /* 9A4F8 1506D048 E7A80094 */  swc1       $f8, 0x94($sp)
    /* 9A4FC 1506D04C C7AA0094 */  lwc1       $f10, 0x94($sp)
    /* 9A500 1506D050 C7AC0094 */  lwc1       $f12, 0x94($sp)
    /* 9A504 1506D054 4600503C */  c.lt.s     $f10, $f0
    /* 9A508 1506D058 00000000 */  nop
    /* 9A50C 1506D05C 4502000D */  bc1fl      .L1506D094
    /* 9A510 1506D060 44812000 */   mtc1      $at, $f4
    /* 9A514 1506D064 3C01BF00 */  lui        $at, (0xBF000000 >> 16)
    /* 9A518 1506D068 44813000 */  mtc1       $at, $f6
    /* 9A51C 1506D06C 3C01800A */  lui        $at, %hi(D_80099CE0)
    /* 9A520 1506D070 C4289CE0 */  lwc1       $f8, %lo(D_80099CE0)($at)
    /* 9A524 1506D074 46065102 */  mul.s      $f4, $f10, $f6
    /* 9A528 1506D078 3C0140E0 */  lui        $at, (0x40E00000 >> 16)
    /* 9A52C 1506D07C 46085282 */  mul.s      $f10, $f10, $f8
    /* 9A530 1506D080 44814000 */  mtc1       $at, $f8
    /* 9A534 1506D084 460A2180 */  add.s      $f6, $f4, $f10
    /* 9A538 1506D088 1000000B */  b          .L1506D0B8
    /* 9A53C 1506D08C 46083300 */   add.s     $f12, $f6, $f8
    /* 9A540 1506D090 44812000 */  mtc1       $at, $f4
  .L1506D094:
    /* 9A544 1506D094 3C01800A */  lui        $at, %hi(D_80099CE4)
    /* 9A548 1506D098 C4269CE4 */  lwc1       $f6, %lo(D_80099CE4)($at)
    /* 9A54C 1506D09C 460C2281 */  sub.s      $f10, $f4, $f12
    /* 9A550 1506D0A0 3C01BF00 */  lui        $at, (0xBF000000 >> 16)
    /* 9A554 1506D0A4 44812000 */  mtc1       $at, $f4
    /* 9A558 1506D0A8 46065202 */  mul.s      $f8, $f10, $f6
    /* 9A55C 1506D0AC 00000000 */  nop
    /* 9A560 1506D0B0 46046282 */  mul.s      $f10, $f12, $f4
    /* 9A564 1506D0B4 46085300 */  add.s      $f12, $f10, $f8
  .L1506D0B8:
    /* 9A568 1506D0B8 3C013FB4 */  lui        $at, (0x3FB40000 >> 16)
    /* 9A56C 1506D0BC 44813000 */  mtc1       $at, $f6
    /* 9A570 1506D0C0 00000000 */  nop
    /* 9A574 1506D0C4 46066302 */  mul.s      $f12, $f12, $f6
    /* 9A578 1506D0C8 10000007 */  b          .L1506D0E8
    /* 9A57C 1506D0CC E7AC0094 */   swc1      $f12, 0x94($sp)
    /* 9A580 1506D0D0 808E01D1 */  lb         $t6, 0x1D1($a0)
  .L1506D0D4:
    /* 9A584 1506D0D4 000E7823 */  negu       $t7, $t6
    /* 9A588 1506D0D8 448F2000 */  mtc1       $t7, $f4
    /* 9A58C 1506D0DC 00000000 */  nop
    /* 9A590 1506D0E0 468022A0 */  cvt.s.w    $f10, $f4
    /* 9A594 1506D0E4 E7AA0094 */  swc1       $f10, 0x94($sp)
  .L1506D0E8:
    /* 9A598 1506D0E8 2558FFFF */  addiu      $t8, $t2, -0x1
  .L1506D0EC:
    /* 9A59C 1506D0EC 2F010012 */  sltiu      $at, $t8, 0x12
    /* 9A5A0 1506D0F0 10200052 */  beqz       $at, .L1506D23C
    /* 9A5A4 1506D0F4 C7AC0094 */   lwc1      $f12, 0x94($sp)
    /* 9A5A8 1506D0F8 0018C080 */  sll        $t8, $t8, 2
    /* 9A5AC 1506D0FC 3C01800A */  lui        $at, %hi(jtbl_80099CE8_game)
    /* 9A5B0 1506D100 00380821 */  addu       $at, $at, $t8
    /* 9A5B4 1506D104 8C389CE8 */  lw         $t8, %lo(jtbl_80099CE8_game)($at)
    /* 9A5B8 1506D108 03000008 */  jr         $t8
    /* 9A5BC 1506D10C 00000000 */   nop
    /* 9A5C0 1506D110 24090001 */  addiu      $t1, $zero, 0x1
    /* 9A5C4 1506D114 10000049 */  b          .L1506D23C
    /* 9A5C8 1506D118 E7AC0094 */   swc1      $f12, 0x94($sp)
    /* 9A5CC 1506D11C 3C01800A */  lui        $at, %hi(D_80099D30)
    /* 9A5D0 1506D120 C4289D30 */  lwc1       $f8, %lo(D_80099D30)($at)
    /* 9A5D4 1506D124 3C0140E0 */  lui        $at, (0x40E00000 >> 16)
    /* 9A5D8 1506D128 44813000 */  mtc1       $at, $f6
    /* 9A5DC 1506D12C 46086302 */  mul.s      $f12, $f12, $f8
    /* 9A5E0 1506D130 3C01800A */  lui        $at, %hi(D_80099D34)
    /* 9A5E4 1506D134 C4249D34 */  lwc1       $f4, %lo(D_80099D34)($at)
    /* 9A5E8 1506D138 E7A40088 */  swc1       $f4, 0x88($sp)
    /* 9A5EC 1506D13C 46066300 */  add.s      $f12, $f12, $f6
    /* 9A5F0 1506D140 1000003E */  b          .L1506D23C
    /* 9A5F4 1506D144 E7AC0094 */   swc1      $f12, 0x94($sp)
    /* 9A5F8 1506D148 3C01800A */  lui        $at, %hi(D_80099D38)
    /* 9A5FC 1506D14C C42A9D38 */  lwc1       $f10, %lo(D_80099D38)($at)
    /* 9A600 1506D150 E7AC0094 */  swc1       $f12, 0x94($sp)
    /* 9A604 1506D154 10000039 */  b          .L1506D23C
    /* 9A608 1506D158 E7AA0088 */   swc1      $f10, 0x88($sp)
    /* 9A60C 1506D15C 3C0143FA */  lui        $at, (0x43FA0000 >> 16)
    /* 9A610 1506D160 3C04800D */  lui        $a0, %hi(D_800CC5EC)
    /* 9A614 1506D164 44814000 */  mtc1       $at, $f8
    /* 9A618 1506D168 8C84C5EC */  lw         $a0, %lo(D_800CC5EC)($a0)
    /* 9A61C 1506D16C 27A50090 */  addiu      $a1, $sp, 0x90
    /* 9A620 1506D170 27A60094 */  addiu      $a2, $sp, 0x94
    /* 9A624 1506D174 AFAA0098 */  sw         $t2, 0x98($sp)
    /* 9A628 1506D178 E7A8008C */  swc1       $f8, 0x8C($sp)
    /* 9A62C 1506D17C 0D45165D */  jal        func_15145974
    /* 9A630 1506D180 248400E8 */   addiu     $a0, $a0, 0xE8
    /* 9A634 1506D184 3C02800D */  lui        $v0, %hi(D_800CC5EC)
    /* 9A638 1506D188 8C42C5EC */  lw         $v0, %lo(D_800CC5EC)($v0)
    /* 9A63C 1506D18C C7A80094 */  lwc1       $f8, 0x94($sp)
    /* 9A640 1506D190 27B90044 */  addiu      $t9, $sp, 0x44
    /* 9A644 1506D194 C44600DC */  lwc1       $f6, 0xDC($v0)
    /* 9A648 1506D198 44800000 */  mtc1       $zero, $f0
    /* 9A64C 1506D19C 8FAA0098 */  lw         $t2, 0x98($sp)
    /* 9A650 1506D1A0 E7A60044 */  swc1       $f6, 0x44($sp)
    /* 9A654 1506D1A4 C44400E0 */  lwc1       $f4, 0xE0($v0)
    /* 9A658 1506D1A8 46004187 */  neg.s      $f6, $f8
    /* 9A65C 1506D1AC 24090001 */  addiu      $t1, $zero, 0x1
    /* 9A660 1506D1B0 E7A40048 */  swc1       $f4, 0x48($sp)
    /* 9A664 1506D1B4 C44A00E4 */  lwc1       $f10, 0xE4($v0)
    /* 9A668 1506D1B8 AFB90050 */  sw         $t9, 0x50($sp)
    /* 9A66C 1506D1BC E7A60094 */  swc1       $f6, 0x94($sp)
    /* 9A670 1506D1C0 1000001E */  b          .L1506D23C
    /* 9A674 1506D1C4 E7AA004C */   swc1      $f10, 0x4C($sp)
    /* 9A678 1506D1C8 3C0143FA */  lui        $at, (0x43FA0000 >> 16)
    /* 9A67C 1506D1CC 44812000 */  mtc1       $at, $f4
    /* 9A680 1506D1D0 24090001 */  addiu      $t1, $zero, 0x1
    /* 9A684 1506D1D4 E7A00094 */  swc1       $f0, 0x94($sp)
    /* 9A688 1506D1D8 10000018 */  b          .L1506D23C
    /* 9A68C 1506D1DC E7A4008C */   swc1      $f4, 0x8C($sp)
    /* 9A690 1506D1E0 3C014316 */  lui        $at, (0x43160000 >> 16)
    /* 9A694 1506D1E4 44815000 */  mtc1       $at, $f10
    /* 9A698 1506D1E8 240B0030 */  addiu      $t3, $zero, 0x30
    /* 9A69C 1506D1EC AFAB0054 */  sw         $t3, 0x54($sp)
    /* 9A6A0 1506D1F0 E7A00094 */  swc1       $f0, 0x94($sp)
    /* 9A6A4 1506D1F4 10000011 */  b          .L1506D23C
    /* 9A6A8 1506D1F8 E7AA008C */   swc1      $f10, 0x8C($sp)
    /* 9A6AC 1506D1FC 3C01437A */  lui        $at, (0x437A0000 >> 16)
    /* 9A6B0 1506D200 44814000 */  mtc1       $at, $f8
    /* 9A6B4 1506D204 E7AC0094 */  swc1       $f12, 0x94($sp)
    /* 9A6B8 1506D208 1000000C */  b          .L1506D23C
    /* 9A6BC 1506D20C E7A8008C */   swc1      $f8, 0x8C($sp)
    /* 9A6C0 1506D210 3C0140A0 */  lui        $at, (0x40A00000 >> 16)
    /* 9A6C4 1506D214 44813000 */  mtc1       $at, $f6
    /* 9A6C8 1506D218 3C01800A */  lui        $at, %hi(D_80099D3C)
    /* 9A6CC 1506D21C C4249D3C */  lwc1       $f4, %lo(D_80099D3C)($at)
    /* 9A6D0 1506D220 3C013FC0 */  lui        $at, (0x3FC00000 >> 16)
    /* 9A6D4 1506D224 44815000 */  mtc1       $at, $f10
    /* 9A6D8 1506D228 24090001 */  addiu      $t1, $zero, 0x1
    /* 9A6DC 1506D22C E7AC0094 */  swc1       $f12, 0x94($sp)
    /* 9A6E0 1506D230 E7A60088 */  swc1       $f6, 0x88($sp)
    /* 9A6E4 1506D234 E7A4008C */  swc1       $f4, 0x8C($sp)
    /* 9A6E8 1506D238 E7AA007C */  swc1       $f10, 0x7C($sp)
  .L1506D23C:
    /* 9A6EC 1506D23C 3C01800A */  lui        $at, %hi(D_80099D40)
    /* 9A6F0 1506D240 C7AC0094 */  lwc1       $f12, 0x94($sp)
    /* 9A6F4 1506D244 C4289D40 */  lwc1       $f8, %lo(D_80099D40)($at)
    /* 9A6F8 1506D248 44060000 */  mfc1       $a2, $f0
    /* 9A6FC 1506D24C 27B80080 */  addiu      $t8, $sp, 0x80
    /* 9A700 1506D250 46086182 */  mul.s      $f6, $f12, $f8
    /* 9A704 1506D254 27B90078 */  addiu      $t9, $sp, 0x78
    /* 9A708 1506D258 AFB90014 */  sw         $t9, 0x14($sp)
    /* 9A70C 1506D25C AFB80010 */  sw         $t8, 0x10($sp)
    /* 9A710 1506D260 8FA5008C */  lw         $a1, 0x8C($sp)
    /* 9A714 1506D264 27A70084 */  addiu      $a3, $sp, 0x84
    /* 9A718 1506D268 AFA90058 */  sw         $t1, 0x58($sp)
    /* 9A71C 1506D26C 4600310D */  trunc.w.s  $f4, $f6
    /* 9A720 1506D270 AFAA0098 */  sw         $t2, 0x98($sp)
    /* 9A724 1506D274 440E2000 */  mfc1       $t6, $f4
    /* 9A728 1506D278 0D416861 */  jal        func_1505A184
    /* 9A72C 1506D27C 31C4FFFF */   andi      $a0, $t6, 0xFFFF
    /* 9A730 1506D280 C7A00080 */  lwc1       $f0, 0x80($sp)
    /* 9A734 1506D284 8FA90058 */  lw         $t1, 0x58($sp)
    /* 9A738 1506D288 8FAA0098 */  lw         $t2, 0x98($sp)
    /* 9A73C 1506D28C 46000007 */  neg.s      $f0, $f0
    /* 9A740 1506D290 44805000 */  mtc1       $zero, $f10
    /* 9A744 1506D294 C7A8007C */  lwc1       $f8, 0x7C($sp)
    /* 9A748 1506D298 8FAC0050 */  lw         $t4, 0x50($sp)
    /* 9A74C 1506D29C 8FAD0054 */  lw         $t5, 0x54($sp)
    /* 9A750 1506D2A0 44060000 */  mfc1       $a2, $f0
    /* 9A754 1506D2A4 240B0064 */  addiu      $t3, $zero, 0x64
    /* 9A758 1506D2A8 AFAB0010 */  sw         $t3, 0x10($sp)
    /* 9A75C 1506D2AC E7A00080 */  swc1       $f0, 0x80($sp)
    /* 9A760 1506D2B0 C7AC0090 */  lwc1       $f12, 0x90($sp)
    /* 9A764 1506D2B4 C7AE0084 */  lwc1       $f14, 0x84($sp)
    /* 9A768 1506D2B8 8FA70088 */  lw         $a3, 0x88($sp)
    /* 9A76C 1506D2BC AFA90028 */  sw         $t1, 0x28($sp)
    /* 9A770 1506D2C0 AFAA0014 */  sw         $t2, 0x14($sp)
    /* 9A774 1506D2C4 E7A8001C */  swc1       $f8, 0x1C($sp)
    /* 9A778 1506D2C8 E7AA0018 */  swc1       $f10, 0x18($sp)
    /* 9A77C 1506D2CC AFAC0020 */  sw         $t4, 0x20($sp)
    /* 9A780 1506D2D0 0D41B118 */  jal        func_1506C460
    /* 9A784 1506D2D4 AFAD0024 */   sw        $t5, 0x24($sp)
    /* 9A788 1506D2D8 8FBF0034 */  lw         $ra, 0x34($sp)
    /* 9A78C 1506D2DC 27BD00A0 */  addiu      $sp, $sp, 0xA0
    /* 9A790 1506D2E0 03E00008 */  jr         $ra
    /* 9A794 1506D2E4 00000000 */   nop
endlabel func_1506CE6C
