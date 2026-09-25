glabel func_1514F8F8
    /* 17CDA8 1514F8F8 27BDFF40 */  addiu      $sp, $sp, -0xC0
    /* 17CDAC 1514F8FC 3C01447A */  lui        $at, (0x447A0000 >> 16)
    /* 17CDB0 1514F900 AFB5007C */  sw         $s5, 0x7C($sp)
    /* 17CDB4 1514F904 AFB40078 */  sw         $s4, 0x78($sp)
    /* 17CDB8 1514F908 AFB20070 */  sw         $s2, 0x70($sp)
    /* 17CDBC 1514F90C AFB00068 */  sw         $s0, 0x68($sp)
    /* 17CDC0 1514F910 44810000 */  mtc1       $at, $f0
    /* 17CDC4 1514F914 00808025 */  or         $s0, $a0, $zero
    /* 17CDC8 1514F918 00A09025 */  or         $s2, $a1, $zero
    /* 17CDCC 1514F91C 00C0A025 */  or         $s4, $a2, $zero
    /* 17CDD0 1514F920 00E0A825 */  or         $s5, $a3, $zero
    /* 17CDD4 1514F924 AFBF008C */  sw         $ra, 0x8C($sp)
    /* 17CDD8 1514F928 AFBE0088 */  sw         $fp, 0x88($sp)
    /* 17CDDC 1514F92C AFB70084 */  sw         $s7, 0x84($sp)
    /* 17CDE0 1514F930 AFB60080 */  sw         $s6, 0x80($sp)
    /* 17CDE4 1514F934 AFB30074 */  sw         $s3, 0x74($sp)
    /* 17CDE8 1514F938 AFB1006C */  sw         $s1, 0x6C($sp)
    /* 17CDEC 1514F93C F7B80060 */  sdc1       $f24, 0x60($sp)
    /* 17CDF0 1514F940 F7B60058 */  sdc1       $f22, 0x58($sp)
    /* 17CDF4 1514F944 F7B40050 */  sdc1       $f20, 0x50($sp)
    /* 17CDF8 1514F948 C6440000 */  lwc1       $f4, 0x0($s2)
    /* 17CDFC 1514F94C C6480004 */  lwc1       $f8, 0x4($s2)
    /* 17CE00 1514F950 C6500008 */  lwc1       $f16, 0x8($s2)
    /* 17CE04 1514F954 46002182 */  mul.s      $f6, $f4, $f0
    /* 17CE08 1514F958 00000000 */  nop
    /* 17CE0C 1514F95C 46004282 */  mul.s      $f10, $f8, $f0
    /* 17CE10 1514F960 00000000 */  nop
    /* 17CE14 1514F964 46008482 */  mul.s      $f18, $f16, $f0
    /* 17CE18 1514F968 E6460000 */  swc1       $f6, 0x0($s2)
    /* 17CE1C 1514F96C E64A0004 */  swc1       $f10, 0x4($s2)
    /* 17CE20 1514F970 0D42B688 */  jal        func_150ADA20
    /* 17CE24 1514F974 E6520008 */   swc1      $f18, 0x8($s2)
    /* 17CE28 1514F978 8E0E0004 */  lw         $t6, 0x4($s0)
    /* 17CE2C 1514F97C 8E190000 */  lw         $t9, 0x0($s0)
    /* 17CE30 1514F980 26080008 */  addiu      $t0, $s0, 0x8
    /* 17CE34 1514F984 25CF0001 */  addiu      $t7, $t6, 0x1
    /* 17CE38 1514F988 004F001B */  divu       $zero, $v0, $t7
    /* 17CE3C 1514F98C 0000C010 */  mfhi       $t8
    /* 17CE40 1514F990 03199821 */  addu       $s3, $t8, $t9
    /* 17CE44 1514F994 15E00002 */  bnez       $t7, .L1514F9A0
    /* 17CE48 1514F998 00000000 */   nop
    /* 17CE4C 1514F99C 0007000D */  break      7
  .L1514F9A0:
    /* 17CE50 1514F9A0 27BE00A8 */  addiu      $fp, $sp, 0xA8
    /* 17CE54 1514F9A4 5260006E */  beql       $s3, $zero, .L1514FB60
    /* 17CE58 1514F9A8 8FBF008C */   lw        $ra, 0x8C($sp)
    /* 17CE5C 1514F9AC AFA80094 */  sw         $t0, 0x94($sp)
    /* 17CE60 1514F9B0 C7B800D0 */  lwc1       $f24, 0xD0($sp)
    /* 17CE64 1514F9B4 8FB700D8 */  lw         $s7, 0xD8($sp)
    /* 17CE68 1514F9B8 93B600D7 */  lbu        $s6, 0xD7($sp)
  .L1514F9BC:
    /* 17CE6C 1514F9BC 0D42B69A */  jal        func_150ADA68
    /* 17CE70 1514F9C0 00000000 */   nop
    /* 17CE74 1514F9C4 C6040018 */  lwc1       $f4, 0x18($s0)
    /* 17CE78 1514F9C8 C6080014 */  lwc1       $f8, 0x14($s0)
    /* 17CE7C 1514F9CC 46040182 */  mul.s      $f6, $f0, $f4
    /* 17CE80 1514F9D0 0D42B688 */  jal        func_150ADA20
    /* 17CE84 1514F9D4 46083500 */   add.s     $f20, $f6, $f8
    /* 17CE88 1514F9D8 0D42B69A */  jal        func_150ADA68
    /* 17CE8C 1514F9DC 00408825 */   or        $s1, $v0, $zero
    /* 17CE90 1514F9E0 46180282 */  mul.s      $f10, $f0, $f24
    /* 17CE94 1514F9E4 322400FF */  andi       $a0, $s1, 0xFF
    /* 17CE98 1514F9E8 00044C00 */  sll        $t1, $a0, 16
    /* 17CE9C 1514F9EC 00092403 */  sra        $a0, $t1, 16
    /* 17CEA0 1514F9F0 03C03025 */  or         $a2, $fp, $zero
    /* 17CEA4 1514F9F4 27A700AC */  addiu      $a3, $sp, 0xAC
    /* 17CEA8 1514F9F8 44055000 */  mfc1       $a1, $f10
    /* 17CEAC 1514F9FC 0D450E1D */  jal        func_15143874
    /* 17CEB0 1514FA00 00000000 */   nop
    /* 17CEB4 1514FA04 C6900000 */  lwc1       $f16, 0x0($s4)
    /* 17CEB8 1514FA08 C7B200A8 */  lwc1       $f18, 0xA8($sp)
    /* 17CEBC 1514FA0C C6A60000 */  lwc1       $f6, 0x0($s5)
    /* 17CEC0 1514FA10 C7A800AC */  lwc1       $f8, 0xAC($sp)
    /* 17CEC4 1514FA14 46128102 */  mul.s      $f4, $f16, $f18
    /* 17CEC8 1514FA18 00000000 */  nop
    /* 17CECC 1514FA1C 46083282 */  mul.s      $f10, $f6, $f8
    /* 17CED0 1514FA20 C6460000 */  lwc1       $f6, 0x0($s2)
    /* 17CED4 1514FA24 460A2400 */  add.s      $f16, $f4, $f10
    /* 17CED8 1514FA28 46068100 */  add.s      $f4, $f16, $f6
    /* 17CEDC 1514FA2C 46142282 */  mul.s      $f10, $f4, $f20
    /* 17CEE0 1514FA30 E7AA00B0 */  swc1       $f10, 0xB0($sp)
    /* 17CEE4 1514FA34 C6900004 */  lwc1       $f16, 0x4($s4)
    /* 17CEE8 1514FA38 C6A40004 */  lwc1       $f4, 0x4($s5)
    /* 17CEEC 1514FA3C 46128182 */  mul.s      $f6, $f16, $f18
    /* 17CEF0 1514FA40 00000000 */  nop
    /* 17CEF4 1514FA44 46082282 */  mul.s      $f10, $f4, $f8
    /* 17CEF8 1514FA48 C6440004 */  lwc1       $f4, 0x4($s2)
    /* 17CEFC 1514FA4C 460A3400 */  add.s      $f16, $f6, $f10
    /* 17CF00 1514FA50 46048180 */  add.s      $f6, $f16, $f4
    /* 17CF04 1514FA54 46143282 */  mul.s      $f10, $f6, $f20
    /* 17CF08 1514FA58 E7AA00B4 */  swc1       $f10, 0xB4($sp)
    /* 17CF0C 1514FA5C C6900008 */  lwc1       $f16, 0x8($s4)
    /* 17CF10 1514FA60 C6A60008 */  lwc1       $f6, 0x8($s5)
    /* 17CF14 1514FA64 46128102 */  mul.s      $f4, $f16, $f18
    /* 17CF18 1514FA68 C6520008 */  lwc1       $f18, 0x8($s2)
    /* 17CF1C 1514FA6C 46083282 */  mul.s      $f10, $f6, $f8
    /* 17CF20 1514FA70 460A2400 */  add.s      $f16, $f4, $f10
    /* 17CF24 1514FA74 46128180 */  add.s      $f6, $f16, $f18
    /* 17CF28 1514FA78 46143202 */  mul.s      $f8, $f6, $f20
    /* 17CF2C 1514FA7C 0D42B69A */  jal        func_150ADA68
    /* 17CF30 1514FA80 E7A800B8 */   swc1      $f8, 0xB8($sp)
    /* 17CF34 1514FA84 0D42B69A */  jal        func_150ADA68
    /* 17CF38 1514FA88 46000586 */   mov.s     $f22, $f0
    /* 17CF3C 1514FA8C 0D42B688 */  jal        func_150ADA20
    /* 17CF40 1514FA90 46000506 */   mov.s     $f20, $f0
    /* 17CF44 1514FA94 8E0B0030 */  lw         $t3, 0x30($s0)
    /* 17CF48 1514FA98 C6040020 */  lwc1       $f4, 0x20($s0)
    /* 17CF4C 1514FA9C C610001C */  lwc1       $f16, 0x1C($s0)
    /* 17CF50 1514FAA0 256C0001 */  addiu      $t4, $t3, 0x1
    /* 17CF54 1514FAA4 004C001B */  divu       $zero, $v0, $t4
    /* 17CF58 1514FAA8 4604B282 */  mul.s      $f10, $f22, $f4
    /* 17CF5C 1514FAAC 8E0E002C */  lw         $t6, 0x2C($s0)
    /* 17CF60 1514FAB0 00006810 */  mfhi       $t5
    /* 17CF64 1514FAB4 C6040024 */  lwc1       $f4, 0x24($s0)
    /* 17CF68 1514FAB8 C6060028 */  lwc1       $f6, 0x28($s0)
    /* 17CF6C 1514FABC 01AE7821 */  addu       $t7, $t5, $t6
    /* 17CF70 1514FAC0 AFAF0010 */  sw         $t7, 0x10($sp)
    /* 17CF74 1514FAC4 46105480 */  add.s      $f18, $f10, $f16
    /* 17CF78 1514FAC8 C6100034 */  lwc1       $f16, 0x34($s0)
    /* 17CF7C 1514FACC 4606A202 */  mul.s      $f8, $f20, $f6
    /* 17CF80 1514FAD0 8FA40094 */  lw         $a0, 0x94($sp)
    /* 17CF84 1514FAD4 44069000 */  mfc1       $a2, $f18
    /* 17CF88 1514FAD8 E7B00014 */  swc1       $f16, 0x14($sp)
    /* 17CF8C 1514FADC C6120038 */  lwc1       $f18, 0x38($s0)
    /* 17CF90 1514FAE0 27A500B0 */  addiu      $a1, $sp, 0xB0
    /* 17CF94 1514FAE4 E7B20018 */  swc1       $f18, 0x18($sp)
    /* 17CF98 1514FAE8 C606003C */  lwc1       $f6, 0x3C($s0)
    /* 17CF9C 1514FAEC 46044280 */  add.s      $f10, $f8, $f4
    /* 17CFA0 1514FAF0 E7A6001C */  swc1       $f6, 0x1C($sp)
    /* 17CFA4 1514FAF4 C6080040 */  lwc1       $f8, 0x40($s0)
    /* 17CFA8 1514FAF8 44075000 */  mfc1       $a3, $f10
    /* 17CFAC 1514FAFC 15800002 */  bnez       $t4, .L1514FB08
    /* 17CFB0 1514FB00 00000000 */   nop
    /* 17CFB4 1514FB04 0007000D */  break      7
  .L1514FB08:
    /* 17CFB8 1514FB08 E7A80020 */  swc1       $f8, 0x20($sp)
    /* 17CFBC 1514FB0C 86180044 */  lh         $t8, 0x44($s0)
    /* 17CFC0 1514FB10 AFB80024 */  sw         $t8, 0x24($sp)
    /* 17CFC4 1514FB14 86190046 */  lh         $t9, 0x46($s0)
    /* 17CFC8 1514FB18 AFB90028 */  sw         $t9, 0x28($sp)
    /* 17CFCC 1514FB1C 86080048 */  lh         $t0, 0x48($s0)
    /* 17CFD0 1514FB20 AFA8002C */  sw         $t0, 0x2C($sp)
    /* 17CFD4 1514FB24 8609004A */  lh         $t1, 0x4A($s0)
    /* 17CFD8 1514FB28 AFA90030 */  sw         $t1, 0x30($sp)
    /* 17CFDC 1514FB2C 860A004C */  lh         $t2, 0x4C($s0)
    /* 17CFE0 1514FB30 AFAA0034 */  sw         $t2, 0x34($sp)
    /* 17CFE4 1514FB34 860B004E */  lh         $t3, 0x4E($s0)
    /* 17CFE8 1514FB38 AFAB0038 */  sw         $t3, 0x38($sp)
    /* 17CFEC 1514FB3C 820C0050 */  lb         $t4, 0x50($s0)
    /* 17CFF0 1514FB40 AFB70044 */  sw         $s7, 0x44($sp)
    /* 17CFF4 1514FB44 AFB60040 */  sw         $s6, 0x40($sp)
    /* 17CFF8 1514FB48 0D468AB5 */  jal        func_151A2AD4
    /* 17CFFC 1514FB4C AFAC003C */   sw        $t4, 0x3C($sp)
    /* 17D000 1514FB50 2673FFFF */  addiu      $s3, $s3, -0x1
    /* 17D004 1514FB54 1660FF99 */  bnez       $s3, .L1514F9BC
    /* 17D008 1514FB58 00000000 */   nop
    /* 17D00C 1514FB5C 8FBF008C */  lw         $ra, 0x8C($sp)
  .L1514FB60:
    /* 17D010 1514FB60 D7B40050 */  ldc1       $f20, 0x50($sp)
    /* 17D014 1514FB64 D7B60058 */  ldc1       $f22, 0x58($sp)
    /* 17D018 1514FB68 D7B80060 */  ldc1       $f24, 0x60($sp)
    /* 17D01C 1514FB6C 8FB00068 */  lw         $s0, 0x68($sp)
    /* 17D020 1514FB70 8FB1006C */  lw         $s1, 0x6C($sp)
    /* 17D024 1514FB74 8FB20070 */  lw         $s2, 0x70($sp)
    /* 17D028 1514FB78 8FB30074 */  lw         $s3, 0x74($sp)
    /* 17D02C 1514FB7C 8FB40078 */  lw         $s4, 0x78($sp)
    /* 17D030 1514FB80 8FB5007C */  lw         $s5, 0x7C($sp)
    /* 17D034 1514FB84 8FB60080 */  lw         $s6, 0x80($sp)
    /* 17D038 1514FB88 8FB70084 */  lw         $s7, 0x84($sp)
    /* 17D03C 1514FB8C 8FBE0088 */  lw         $fp, 0x88($sp)
    /* 17D040 1514FB90 03E00008 */  jr         $ra
    /* 17D044 1514FB94 27BD00C0 */   addiu     $sp, $sp, 0xC0
endlabel func_1514F8F8
