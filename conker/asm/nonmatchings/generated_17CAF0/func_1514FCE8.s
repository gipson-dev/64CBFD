glabel func_1514FCE8
    /* 17D198 1514FCE8 27BDFF70 */  addiu      $sp, $sp, -0x90
    /* 17D19C 1514FCEC AFB60088 */  sw         $s6, 0x88($sp)
    /* 17D1A0 1514FCF0 AFB50084 */  sw         $s5, 0x84($sp)
    /* 17D1A4 1514FCF4 AFB00070 */  sw         $s0, 0x70($sp)
    /* 17D1A8 1514FCF8 00808025 */  or         $s0, $a0, $zero
    /* 17D1AC 1514FCFC 30B500FF */  andi       $s5, $a1, 0xFF
    /* 17D1B0 1514FD00 00C0B025 */  or         $s6, $a2, $zero
    /* 17D1B4 1514FD04 AFBF008C */  sw         $ra, 0x8C($sp)
    /* 17D1B8 1514FD08 AFB40080 */  sw         $s4, 0x80($sp)
    /* 17D1BC 1514FD0C AFB3007C */  sw         $s3, 0x7C($sp)
    /* 17D1C0 1514FD10 AFB20078 */  sw         $s2, 0x78($sp)
    /* 17D1C4 1514FD14 AFB10074 */  sw         $s1, 0x74($sp)
    /* 17D1C8 1514FD18 F7B80068 */  sdc1       $f24, 0x68($sp)
    /* 17D1CC 1514FD1C F7B60060 */  sdc1       $f22, 0x60($sp)
    /* 17D1D0 1514FD20 F7B40058 */  sdc1       $f20, 0x58($sp)
    /* 17D1D4 1514FD24 AFA50094 */  sw         $a1, 0x94($sp)
    /* 17D1D8 1514FD28 0D42B688 */  jal        func_150ADA20
    /* 17D1DC 1514FD2C 00000000 */   nop
    /* 17D1E0 1514FD30 8E0E000C */  lw         $t6, 0xC($s0)
    /* 17D1E4 1514FD34 8E190008 */  lw         $t9, 0x8($s0)
    /* 17D1E8 1514FD38 26140010 */  addiu      $s4, $s0, 0x10
    /* 17D1EC 1514FD3C 25CF0001 */  addiu      $t7, $t6, 0x1
    /* 17D1F0 1514FD40 004F001B */  divu       $zero, $v0, $t7
    /* 17D1F4 1514FD44 0000C010 */  mfhi       $t8
    /* 17D1F8 1514FD48 03199021 */  addu       $s2, $t8, $t9
    /* 17D1FC 1514FD4C 15E00002 */  bnez       $t7, .L1514FD58
    /* 17D200 1514FD50 00000000 */   nop
    /* 17D204 1514FD54 0007000D */  break      7
  .L1514FD58:
    /* 17D208 1514FD58 5240005C */  beql       $s2, $zero, .L1514FECC
    /* 17D20C 1514FD5C 8FBF008C */   lw        $ra, 0x8C($sp)
  .L1514FD60:
    /* 17D210 1514FD60 0D42B688 */  jal        func_150ADA20
    /* 17D214 1514FD64 00000000 */   nop
    /* 17D218 1514FD68 0D42B688 */  jal        func_150ADA20
    /* 17D21C 1514FD6C 00409825 */   or        $s3, $v0, $zero
    /* 17D220 1514FD70 0D42B69A */  jal        func_150ADA68
    /* 17D224 1514FD74 00408825 */   or        $s1, $v0, $zero
    /* 17D228 1514FD78 0D42B69A */  jal        func_150ADA68
    /* 17D22C 1514FD7C 46000506 */   mov.s     $f20, $f0
    /* 17D230 1514FD80 0D42B69A */  jal        func_150ADA68
    /* 17D234 1514FD84 46000586 */   mov.s     $f22, $f0
    /* 17D238 1514FD88 0D42B688 */  jal        func_150ADA20
    /* 17D23C 1514FD8C 46000606 */   mov.s     $f24, $f0
    /* 17D240 1514FD90 86080002 */  lh         $t0, 0x2($s0)
    /* 17D244 1514FD94 860E0006 */  lh         $t6, 0x6($s0)
    /* 17D248 1514FD98 C6040020 */  lwc1       $f4, 0x20($s0)
    /* 17D24C 1514FD9C 25090001 */  addiu      $t1, $t0, 0x1
    /* 17D250 1514FDA0 0269001B */  divu       $zero, $s3, $t1
    /* 17D254 1514FDA4 00005010 */  mfhi       $t2
    /* 17D258 1514FDA8 25CF0001 */  addiu      $t7, $t6, 0x1
    /* 17D25C 1514FDAC 4604A182 */  mul.s      $f6, $f20, $f4
    /* 17D260 1514FDB0 022F001B */  divu       $zero, $s1, $t7
    /* 17D264 1514FDB4 C6100028 */  lwc1       $f16, 0x28($s0)
    /* 17D268 1514FDB8 C608001C */  lwc1       $f8, 0x1C($s0)
    /* 17D26C 1514FDBC C6040024 */  lwc1       $f4, 0x24($s0)
    /* 17D270 1514FDC0 4610B482 */  mul.s      $f18, $f22, $f16
    /* 17D274 1514FDC4 46083280 */  add.s      $f10, $f6, $f8
    /* 17D278 1514FDC8 860B0000 */  lh         $t3, 0x0($s0)
    /* 17D27C 1514FDCC 86190004 */  lh         $t9, 0x4($s0)
    /* 17D280 1514FDD0 0000C010 */  mfhi       $t8
    /* 17D284 1514FDD4 44075000 */  mfc1       $a3, $f10
    /* 17D288 1514FDD8 014B2821 */  addu       $a1, $t2, $t3
    /* 17D28C 1514FDDC 46049180 */  add.s      $f6, $f18, $f4
    /* 17D290 1514FDE0 00056400 */  sll        $t4, $a1, 16
    /* 17D294 1514FDE4 000C6C03 */  sra        $t5, $t4, 16
    /* 17D298 1514FDE8 01A02825 */  or         $a1, $t5, $zero
    /* 17D29C 1514FDEC E7A60010 */  swc1       $f6, 0x10($sp)
    /* 17D2A0 1514FDF0 C6080030 */  lwc1       $f8, 0x30($s0)
    /* 17D2A4 1514FDF4 C610002C */  lwc1       $f16, 0x2C($s0)
    /* 17D2A8 1514FDF8 03193021 */  addu       $a2, $t8, $t9
    /* 17D2AC 1514FDFC 4608C282 */  mul.s      $f10, $f24, $f8
    /* 17D2B0 1514FE00 00064400 */  sll        $t0, $a2, 16
    /* 17D2B4 1514FE04 02802025 */  or         $a0, $s4, $zero
    /* 17D2B8 1514FE08 15200002 */  bnez       $t1, .L1514FE14
    /* 17D2BC 1514FE0C 00000000 */   nop
    /* 17D2C0 1514FE10 0007000D */  break      7
  .L1514FE14:
    /* 17D2C4 1514FE14 46105480 */  add.s      $f18, $f10, $f16
    /* 17D2C8 1514FE18 15E00002 */  bnez       $t7, .L1514FE24
    /* 17D2CC 1514FE1C 00000000 */   nop
    /* 17D2D0 1514FE20 0007000D */  break      7
  .L1514FE24:
    /* 17D2D4 1514FE24 E7B20014 */  swc1       $f18, 0x14($sp)
    /* 17D2D8 1514FE28 8E0A0038 */  lw         $t2, 0x38($s0)
    /* 17D2DC 1514FE2C 8E0D0034 */  lw         $t5, 0x34($s0)
    /* 17D2E0 1514FE30 00084C03 */  sra        $t1, $t0, 16
    /* 17D2E4 1514FE34 254B0001 */  addiu      $t3, $t2, 0x1
    /* 17D2E8 1514FE38 004B001B */  divu       $zero, $v0, $t3
    /* 17D2EC 1514FE3C 00006010 */  mfhi       $t4
    /* 17D2F0 1514FE40 018D7021 */  addu       $t6, $t4, $t5
    /* 17D2F4 1514FE44 AFAE0018 */  sw         $t6, 0x18($sp)
    /* 17D2F8 1514FE48 C604003C */  lwc1       $f4, 0x3C($s0)
    /* 17D2FC 1514FE4C 01203025 */  or         $a2, $t1, $zero
    /* 17D300 1514FE50 15600002 */  bnez       $t3, .L1514FE5C
    /* 17D304 1514FE54 00000000 */   nop
    /* 17D308 1514FE58 0007000D */  break      7
  .L1514FE5C:
    /* 17D30C 1514FE5C E7A4001C */  swc1       $f4, 0x1C($sp)
    /* 17D310 1514FE60 C6060040 */  lwc1       $f6, 0x40($s0)
    /* 17D314 1514FE64 E7A60020 */  swc1       $f6, 0x20($sp)
    /* 17D318 1514FE68 C6080044 */  lwc1       $f8, 0x44($s0)
    /* 17D31C 1514FE6C E7A80024 */  swc1       $f8, 0x24($sp)
    /* 17D320 1514FE70 C60A0048 */  lwc1       $f10, 0x48($s0)
    /* 17D324 1514FE74 E7AA0028 */  swc1       $f10, 0x28($sp)
    /* 17D328 1514FE78 860F004C */  lh         $t7, 0x4C($s0)
    /* 17D32C 1514FE7C AFAF002C */  sw         $t7, 0x2C($sp)
    /* 17D330 1514FE80 8618004E */  lh         $t8, 0x4E($s0)
    /* 17D334 1514FE84 AFB80030 */  sw         $t8, 0x30($sp)
    /* 17D338 1514FE88 86190050 */  lh         $t9, 0x50($s0)
    /* 17D33C 1514FE8C AFB90034 */  sw         $t9, 0x34($sp)
    /* 17D340 1514FE90 86080052 */  lh         $t0, 0x52($s0)
    /* 17D344 1514FE94 AFA80038 */  sw         $t0, 0x38($sp)
    /* 17D348 1514FE98 86090054 */  lh         $t1, 0x54($s0)
    /* 17D34C 1514FE9C AFA9003C */  sw         $t1, 0x3C($sp)
    /* 17D350 1514FEA0 860A0056 */  lh         $t2, 0x56($s0)
    /* 17D354 1514FEA4 AFAA0040 */  sw         $t2, 0x40($sp)
    /* 17D358 1514FEA8 820B0058 */  lb         $t3, 0x58($s0)
    /* 17D35C 1514FEAC AFB6004C */  sw         $s6, 0x4C($sp)
    /* 17D360 1514FEB0 AFB50048 */  sw         $s5, 0x48($sp)
    /* 17D364 1514FEB4 0D468A85 */  jal        func_151A2A14
    /* 17D368 1514FEB8 AFAB0044 */   sw        $t3, 0x44($sp)
    /* 17D36C 1514FEBC 2652FFFF */  addiu      $s2, $s2, -0x1
    /* 17D370 1514FEC0 1640FFA7 */  bnez       $s2, .L1514FD60
    /* 17D374 1514FEC4 00000000 */   nop
    /* 17D378 1514FEC8 8FBF008C */  lw         $ra, 0x8C($sp)
  .L1514FECC:
    /* 17D37C 1514FECC D7B40058 */  ldc1       $f20, 0x58($sp)
    /* 17D380 1514FED0 D7B60060 */  ldc1       $f22, 0x60($sp)
    /* 17D384 1514FED4 D7B80068 */  ldc1       $f24, 0x68($sp)
    /* 17D388 1514FED8 8FB00070 */  lw         $s0, 0x70($sp)
    /* 17D38C 1514FEDC 8FB10074 */  lw         $s1, 0x74($sp)
    /* 17D390 1514FEE0 8FB20078 */  lw         $s2, 0x78($sp)
    /* 17D394 1514FEE4 8FB3007C */  lw         $s3, 0x7C($sp)
    /* 17D398 1514FEE8 8FB40080 */  lw         $s4, 0x80($sp)
    /* 17D39C 1514FEEC 8FB50084 */  lw         $s5, 0x84($sp)
    /* 17D3A0 1514FEF0 8FB60088 */  lw         $s6, 0x88($sp)
    /* 17D3A4 1514FEF4 03E00008 */  jr         $ra
    /* 17D3A8 1514FEF8 27BD0090 */   addiu     $sp, $sp, 0x90
endlabel func_1514FCE8
