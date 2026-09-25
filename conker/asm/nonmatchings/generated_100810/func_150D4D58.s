glabel func_150D4D58
    /* 102208 150D4D58 27BDFEF8 */  addiu      $sp, $sp, -0x108
    /* 10220C 150D4D5C F7B40020 */  sdc1       $f20, 0x20($sp)
    /* 102210 150D4D60 AFB3005C */  sw         $s3, 0x5C($sp)
    /* 102214 150D4D64 AFB00050 */  sw         $s0, 0x50($sp)
    /* 102218 150D4D68 4486A000 */  mtc1       $a2, $f20
    /* 10221C 150D4D6C 00808025 */  or         $s0, $a0, $zero
    /* 102220 150D4D70 00A09825 */  or         $s3, $a1, $zero
    /* 102224 150D4D74 AFBF0074 */  sw         $ra, 0x74($sp)
    /* 102228 150D4D78 AFBE0070 */  sw         $fp, 0x70($sp)
    /* 10222C 150D4D7C AFB7006C */  sw         $s7, 0x6C($sp)
    /* 102230 150D4D80 AFB60068 */  sw         $s6, 0x68($sp)
    /* 102234 150D4D84 AFB50064 */  sw         $s5, 0x64($sp)
    /* 102238 150D4D88 AFB40060 */  sw         $s4, 0x60($sp)
    /* 10223C 150D4D8C AFB20058 */  sw         $s2, 0x58($sp)
    /* 102240 150D4D90 AFB10054 */  sw         $s1, 0x54($sp)
    /* 102244 150D4D94 F7BE0048 */  sdc1       $f30, 0x48($sp)
    /* 102248 150D4D98 F7BC0040 */  sdc1       $f28, 0x40($sp)
    /* 10224C 150D4D9C F7BA0038 */  sdc1       $f26, 0x38($sp)
    /* 102250 150D4DA0 F7B80030 */  sdc1       $f24, 0x30($sp)
    /* 102254 150D4DA4 F7B60028 */  sdc1       $f22, 0x28($sp)
    /* 102258 150D4DA8 AFA70114 */  sw         $a3, 0x114($sp)
    /* 10225C 150D4DAC 0D42B688 */  jal        func_150ADA20
    /* 102260 150D4DB0 00000000 */   nop
    /* 102264 150D4DB4 2401000B */  addiu      $at, $zero, 0xB
    /* 102268 150D4DB8 0041001B */  divu       $zero, $v0, $at
    /* 10226C 150D4DBC 3C0F0020 */  lui        $t7, (0x200005 >> 16)
    /* 102270 150D4DC0 240E2203 */  addiu      $t6, $zero, 0x2203
    /* 102274 150D4DC4 35EF0005 */  ori        $t7, $t7, (0x200005 & 0xFFFF)
    /* 102278 150D4DC8 241800FF */  addiu      $t8, $zero, 0xFF
    /* 10227C 150D4DCC 241900FF */  addiu      $t9, $zero, 0xFF
    /* 102280 150D4DD0 240800FF */  addiu      $t0, $zero, 0xFF
    /* 102284 150D4DD4 240900FF */  addiu      $t1, $zero, 0xFF
    /* 102288 150D4DD8 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 10228C 150D4DDC 240B00FF */  addiu      $t3, $zero, 0xFF
    /* 102290 150D4DE0 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 102294 150D4DE4 240D00FF */  addiu      $t5, $zero, 0xFF
    /* 102298 150D4DE8 A7AE00A0 */  sh         $t6, 0xA0($sp)
    /* 10229C 150D4DEC AFAF0098 */  sw         $t7, 0x98($sp)
    /* 1022A0 150D4DF0 AFA0009C */  sw         $zero, 0x9C($sp)
    /* 1022A4 150D4DF4 AFA000A4 */  sw         $zero, 0xA4($sp)
    /* 1022A8 150D4DF8 AFA000A8 */  sw         $zero, 0xA8($sp)
    /* 1022AC 150D4DFC A3B800AC */  sb         $t8, 0xAC($sp)
    /* 1022B0 150D4E00 A3B900AD */  sb         $t9, 0xAD($sp)
    /* 1022B4 150D4E04 A3A800AE */  sb         $t0, 0xAE($sp)
    /* 1022B8 150D4E08 A3A900AF */  sb         $t1, 0xAF($sp)
    /* 1022BC 150D4E0C A3AA00B0 */  sb         $t2, 0xB0($sp)
    /* 1022C0 150D4E10 A3AB00B1 */  sb         $t3, 0xB1($sp)
    /* 1022C4 150D4E14 A3AC00B2 */  sb         $t4, 0xB2($sp)
    /* 1022C8 150D4E18 A3AD00B4 */  sb         $t5, 0xB4($sp)
    /* 1022CC 150D4E1C 8E010000 */  lw         $at, 0x0($s0)
    /* 1022D0 150D4E20 27AE00C8 */  addiu      $t6, $sp, 0xC8
    /* 1022D4 150D4E24 3C09800A */  lui        $t1, %hi(D_800A5480)
    /* 1022D8 150D4E28 ADC10000 */  sw         $at, 0x0($t6)
    /* 1022DC 150D4E2C 8E190004 */  lw         $t9, 0x4($s0)
    /* 1022E0 150D4E30 25295480 */  addiu      $t1, $t1, %lo(D_800A5480)
    /* 1022E4 150D4E34 27A800D4 */  addiu      $t0, $sp, 0xD4
    /* 1022E8 150D4E38 ADD90004 */  sw         $t9, 0x4($t6)
    /* 1022EC 150D4E3C 8E010008 */  lw         $at, 0x8($s0)
    /* 1022F0 150D4E40 240D000A */  addiu      $t5, $zero, 0xA
    /* 1022F4 150D4E44 24180019 */  addiu      $t8, $zero, 0x19
    /* 1022F8 150D4E48 ADC10008 */  sw         $at, 0x8($t6)
    /* 1022FC 150D4E4C 8D210000 */  lw         $at, 0x0($t1)
    /* 102300 150D4E50 8D2C0004 */  lw         $t4, 0x4($t1)
    /* 102304 150D4E54 24190007 */  addiu      $t9, $zero, 0x7
    /* 102308 150D4E58 AD010000 */  sw         $at, 0x0($t0)
    /* 10230C 150D4E5C 8D210008 */  lw         $at, 0x8($t1)
    /* 102310 150D4E60 AD0C0004 */  sw         $t4, 0x4($t0)
    /* 102314 150D4E64 240BFFFF */  addiu      $t3, $zero, -0x1
    /* 102318 150D4E68 AD010008 */  sw         $at, 0x8($t0)
    /* 10231C 150D4E6C 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 102320 150D4E70 44812000 */  mtc1       $at, $f4
    /* 102324 150D4E74 3C01800A */  lui        $at, %hi(D_800A0A18)
    /* 102328 150D4E78 C4260A18 */  lwc1       $f6, %lo(D_800A0A18)($at)
    /* 10232C 150D4E7C 3C014120 */  lui        $at, (0x41200000 >> 16)
    /* 102330 150D4E80 4481F000 */  mtc1       $at, $f30
    /* 102334 150D4E84 4606A202 */  mul.s      $f8, $f20, $f6
    /* 102338 150D4E88 3C014347 */  lui        $at, (0x43470000 >> 16)
    /* 10233C 150D4E8C A7AD00B6 */  sh         $t5, 0xB6($sp)
    /* 102340 150D4E90 4481E000 */  mtc1       $at, $f28
    /* 102344 150D4E94 A7B800B8 */  sh         $t8, 0xB8($sp)
    /* 102348 150D4E98 3C014369 */  lui        $at, (0x43690000 >> 16)
    /* 10234C 150D4E9C A3B900F9 */  sb         $t9, 0xF9($sp)
    /* 102350 150D4EA0 4600428D */  trunc.w.s  $f10, $f8
    /* 102354 150D4EA4 4481D000 */  mtc1       $at, $f26
    /* 102358 150D4EA8 3C01800A */  lui        $at, %hi(D_800A0A1C)
    /* 10235C 150D4EAC 00009010 */  mfhi       $s2
    /* 102360 150D4EB0 44145000 */  mfc1       $s4, $f10
    /* 102364 150D4EB4 3C0E0004 */  lui        $t6, (0x4C207 >> 16)
    /* 102368 150D4EB8 A3AB00FA */  sb         $t3, 0xFA($sp)
    /* 10236C 150D4EBC 00146C00 */  sll        $t5, $s4, 16
    /* 102370 150D4EC0 000DC403 */  sra        $t8, $t5, 16
    /* 102374 150D4EC4 0018CA03 */  sra        $t9, $t8, 8
    /* 102378 150D4EC8 27340040 */  addiu      $s4, $t9, 0x40
    /* 10237C 150D4ECC C4380A1C */  lwc1       $f24, %lo(D_800A0A1C)($at)
    /* 102380 150D4ED0 240F0001 */  addiu      $t7, $zero, 0x1
    /* 102384 150D4ED4 35CEC207 */  ori        $t6, $t6, (0x4C207 & 0xFFFF)
    /* 102388 150D4ED8 240AFFFF */  addiu      $t2, $zero, -0x1
    /* 10238C 150D4EDC 2408FFFF */  addiu      $t0, $zero, -0x1
    /* 102390 150D4EE0 240900FF */  addiu      $t1, $zero, 0xFF
    /* 102394 150D4EE4 3C01800A */  lui        $at, %hi(D_800A0A20)
    /* 102398 150D4EE8 00145C00 */  sll        $t3, $s4, 16
    /* 10239C 150D4EEC 3C16800A */  lui        $s6, %hi(D_800A09C0)
    /* 1023A0 150D4EF0 2652000A */  addiu      $s2, $s2, 0xA
    /* 1023A4 150D4EF4 A7AF00BA */  sh         $t7, 0xBA($sp)
    /* 1023A8 150D4EF8 AFAE00F0 */  sw         $t6, 0xF0($sp)
    /* 1023AC 150D4EFC A3A000F8 */  sb         $zero, 0xF8($sp)
    /* 1023B0 150D4F00 A3AA00FB */  sb         $t2, 0xFB($sp)
    /* 1023B4 150D4F04 A3A800FC */  sb         $t0, 0xFC($sp)
    /* 1023B8 150D4F08 A3A000FD */  sb         $zero, 0xFD($sp)
    /* 1023BC 150D4F0C AFA000F4 */  sw         $zero, 0xF4($sp)
    /* 1023C0 150D4F10 A3A900FE */  sb         $t1, 0xFE($sp)
    /* 1023C4 150D4F14 26D609C0 */  addiu      $s6, $s6, %lo(D_800A09C0)
    /* 1023C8 150D4F18 000BA403 */  sra        $s4, $t3, 16
    /* 1023CC 150D4F1C C4360A20 */  lwc1       $f22, %lo(D_800A0A20)($at)
    /* 1023D0 150D4F20 8FB50118 */  lw         $s5, 0x118($sp)
    /* 1023D4 150D4F24 241E009C */  addiu      $fp, $zero, 0x9C
    /* 1023D8 150D4F28 24170012 */  addiu      $s7, $zero, 0x12
    /* 1023DC 150D4F2C E7A400BC */  swc1       $f4, 0xBC($sp)
  .L150D4F30:
    /* 1023E0 150D4F30 0D42B69A */  jal        func_150ADA68
    /* 1023E4 150D4F34 00000000 */   nop
    /* 1023E8 150D4F38 46160402 */  mul.s      $f16, $f0, $f22
    /* 1023EC 150D4F3C 0D42B688 */  jal        func_150ADA20
    /* 1023F0 150D4F40 46188500 */   add.s     $f20, $f16, $f24
    /* 1023F4 150D4F44 30480003 */  andi       $t0, $v0, 0x3
    /* 1023F8 150D4F48 00084880 */  sll        $t1, $t0, 2
    /* 1023FC 150D4F4C 02C96021 */  addu       $t4, $s6, $t1
    /* 102400 150D4F50 8D8D0000 */  lw         $t5, 0x0($t4)
    /* 102404 150D4F54 0D42B688 */  jal        func_150ADA20
    /* 102408 150D4F58 A3AD00B5 */   sb        $t5, 0xB5($sp)
    /* 10240C 150D4F5C 0057001B */  divu       $zero, $v0, $s7
    /* 102410 150D4F60 0000C010 */  mfhi       $t8
    /* 102414 150D4F64 270F001B */  addiu      $t7, $t8, 0x1B
    /* 102418 150D4F68 16E00002 */  bnez       $s7, .L150D4F74
    /* 10241C 150D4F6C 00000000 */   nop
    /* 102420 150D4F70 0007000D */  break      7
  .L150D4F74:
    /* 102424 150D4F74 A7AF00A2 */  sh         $t7, 0xA2($sp)
    /* 102428 150D4F78 0D42B688 */  jal        func_150ADA20
    /* 10242C 150D4F7C 00000000 */   nop
    /* 102430 150D4F80 005E001B */  divu       $zero, $v0, $fp
    /* 102434 150D4F84 00007010 */  mfhi       $t6
    /* 102438 150D4F88 25D90064 */  addiu      $t9, $t6, 0x64
    /* 10243C 150D4F8C 17C00002 */  bnez       $fp, .L150D4F98
    /* 102440 150D4F90 00000000 */   nop
    /* 102444 150D4F94 0007000D */  break      7
  .L150D4F98:
    /* 102448 150D4F98 A3B900B3 */  sb         $t9, 0xB3($sp)
    /* 10244C 150D4F9C 0D42B69A */  jal        func_150ADA68
    /* 102450 150D4FA0 00000000 */   nop
    /* 102454 150D4FA4 461A0482 */  mul.s      $f18, $f0, $f26
    /* 102458 150D4FA8 461C9080 */  add.s      $f2, $f18, $f28
    /* 10245C 150D4FAC E7A200C0 */  swc1       $f2, 0xC0($sp)
    /* 102460 150D4FB0 0D42B688 */  jal        func_150ADA20
    /* 102464 150D4FB4 E7A200C4 */   swc1      $f2, 0xC4($sp)
    /* 102468 150D4FB8 0D42B688 */  jal        func_150ADA20
    /* 10246C 150D4FBC 00408825 */   or        $s1, $v0, $zero
    /* 102470 150D4FC0 0D42B69A */  jal        func_150ADA68
    /* 102474 150D4FC4 00408025 */   or        $s0, $v0, $zero
    /* 102478 150D4FC8 24010082 */  addiu      $at, $zero, 0x82
    /* 10247C 150D4FCC 0221001B */  divu       $zero, $s1, $at
    /* 102480 150D4FD0 24010051 */  addiu      $at, $zero, 0x51
    /* 102484 150D4FD4 00005810 */  mfhi       $t3
    /* 102488 150D4FD8 461E0102 */  mul.s      $f4, $f0, $f30
    /* 10248C 150D4FDC 01742021 */  addu       $a0, $t3, $s4
    /* 102490 150D4FE0 0201001B */  divu       $zero, $s0, $at
    /* 102494 150D4FE4 3C0140A0 */  lui        $at, (0x40A00000 >> 16)
    /* 102498 150D4FE8 44813000 */  mtc1       $at, $f6
    /* 10249C 150D4FEC 00002810 */  mfhi       $a1
    /* 1024A0 150D4FF0 24A5FFC0 */  addiu      $a1, $a1, -0x40
    /* 1024A4 150D4FF4 46062200 */  add.s      $f8, $f4, $f6
    /* 1024A8 150D4FF8 00054C00 */  sll        $t1, $a1, 16
    /* 1024AC 150D4FFC 00045400 */  sll        $t2, $a0, 16
    /* 1024B0 150D5000 000A2403 */  sra        $a0, $t2, 16
    /* 1024B4 150D5004 44064000 */  mfc1       $a2, $f8
    /* 1024B8 150D5008 00092C03 */  sra        $a1, $t1, 16
    /* 1024BC 150D500C 0D450DE5 */  jal        func_15143794
    /* 1024C0 150D5010 27A700E0 */   addiu     $a3, $sp, 0xE0
    /* 1024C4 150D5014 C6700000 */  lwc1       $f16, 0x0($s3)
    /* 1024C8 150D5018 C7AA00E0 */  lwc1       $f10, 0xE0($sp)
    /* 1024CC 150D501C C7A600E8 */  lwc1       $f6, 0xE8($sp)
    /* 1024D0 150D5020 46148482 */  mul.s      $f18, $f16, $f20
    /* 1024D4 150D5024 46125101 */  sub.s      $f4, $f10, $f18
    /* 1024D8 150D5028 E7A400E0 */  swc1       $f4, 0xE0($sp)
    /* 1024DC 150D502C C6680008 */  lwc1       $f8, 0x8($s3)
    /* 1024E0 150D5030 46144402 */  mul.s      $f16, $f8, $f20
    /* 1024E4 150D5034 46103281 */  sub.s      $f10, $f6, $f16
    /* 1024E8 150D5038 0D42B69A */  jal        func_150ADA68
    /* 1024EC 150D503C E7AA00E8 */   swc1      $f10, 0xE8($sp)
    /* 1024F0 150D5040 3C01800A */  lui        $at, %hi(D_800A0A24)
    /* 1024F4 150D5044 C4320A24 */  lwc1       $f18, %lo(D_800A0A24)($at)
    /* 1024F8 150D5048 3C01800A */  lui        $at, %hi(D_800A0A28)
    /* 1024FC 150D504C C4280A28 */  lwc1       $f8, %lo(D_800A0A28)($at)
    /* 102500 150D5050 46120102 */  mul.s      $f4, $f0, $f18
    /* 102504 150D5054 8FAD00F0 */  lw         $t5, 0xF0($sp)
    /* 102508 150D5058 2401FF3F */  addiu      $at, $zero, -0xC1
    /* 10250C 150D505C 01A1C024 */  and        $t8, $t5, $at
    /* 102510 150D5060 AFB800F0 */  sw         $t8, 0xF0($sp)
    /* 102514 150D5064 46082180 */  add.s      $f6, $f4, $f8
    /* 102518 150D5068 0D42B688 */  jal        func_150ADA20
    /* 10251C 150D506C E7A600EC */   swc1      $f6, 0xEC($sp)
    /* 102520 150D5070 304F0001 */  andi       $t7, $v0, 0x1
    /* 102524 150D5074 11E00003 */  beqz       $t7, .L150D5084
    /* 102528 150D5078 00008825 */   or        $s1, $zero, $zero
    /* 10252C 150D507C 10000001 */  b          .L150D5084
    /* 102530 150D5080 24110080 */   addiu     $s1, $zero, 0x80
  .L150D5084:
    /* 102534 150D5084 0D42B688 */  jal        func_150ADA20
    /* 102538 150D5088 00000000 */   nop
    /* 10253C 150D508C 304E0001 */  andi       $t6, $v0, 0x1
    /* 102540 150D5090 11C00003 */  beqz       $t6, .L150D50A0
    /* 102544 150D5094 8FB900F0 */   lw        $t9, 0xF0($sp)
    /* 102548 150D5098 10000002 */  b          .L150D50A4
    /* 10254C 150D509C 24100040 */   addiu     $s0, $zero, 0x40
  .L150D50A0:
    /* 102550 150D50A0 00008025 */  or         $s0, $zero, $zero
  .L150D50A4:
    /* 102554 150D50A4 93A80117 */  lbu        $t0, 0x117($sp)
    /* 102558 150D50A8 02115825 */  or         $t3, $s0, $s1
    /* 10255C 150D50AC 032B5025 */  or         $t2, $t9, $t3
    /* 102560 150D50B0 AFAA00F0 */  sw         $t2, 0xF0($sp)
    /* 102564 150D50B4 27A40098 */  addiu      $a0, $sp, 0x98
    /* 102568 150D50B8 24050001 */  addiu      $a1, $zero, 0x1
    /* 10256C 150D50BC 00003025 */  or         $a2, $zero, $zero
    /* 102570 150D50C0 00003825 */  or         $a3, $zero, $zero
    /* 102574 150D50C4 AFB50014 */  sw         $s5, 0x14($sp)
    /* 102578 150D50C8 0D44C0A0 */  jal        func_15130280
    /* 10257C 150D50CC AFA80010 */   sw        $t0, 0x10($sp)
    /* 102580 150D50D0 2652FFFF */  addiu      $s2, $s2, -0x1
    /* 102584 150D50D4 1E40FF96 */  bgtz       $s2, .L150D4F30
    /* 102588 150D50D8 00000000 */   nop
    /* 10258C 150D50DC 8FBF0074 */  lw         $ra, 0x74($sp)
    /* 102590 150D50E0 D7B40020 */  ldc1       $f20, 0x20($sp)
    /* 102594 150D50E4 D7B60028 */  ldc1       $f22, 0x28($sp)
    /* 102598 150D50E8 D7B80030 */  ldc1       $f24, 0x30($sp)
    /* 10259C 150D50EC D7BA0038 */  ldc1       $f26, 0x38($sp)
    /* 1025A0 150D50F0 D7BC0040 */  ldc1       $f28, 0x40($sp)
    /* 1025A4 150D50F4 D7BE0048 */  ldc1       $f30, 0x48($sp)
    /* 1025A8 150D50F8 8FB00050 */  lw         $s0, 0x50($sp)
    /* 1025AC 150D50FC 8FB10054 */  lw         $s1, 0x54($sp)
    /* 1025B0 150D5100 8FB20058 */  lw         $s2, 0x58($sp)
    /* 1025B4 150D5104 8FB3005C */  lw         $s3, 0x5C($sp)
    /* 1025B8 150D5108 8FB40060 */  lw         $s4, 0x60($sp)
    /* 1025BC 150D510C 8FB50064 */  lw         $s5, 0x64($sp)
    /* 1025C0 150D5110 8FB60068 */  lw         $s6, 0x68($sp)
    /* 1025C4 150D5114 8FB7006C */  lw         $s7, 0x6C($sp)
    /* 1025C8 150D5118 8FBE0070 */  lw         $fp, 0x70($sp)
    /* 1025CC 150D511C 03E00008 */  jr         $ra
    /* 1025D0 150D5120 27BD0108 */   addiu     $sp, $sp, 0x108
endlabel func_150D4D58
