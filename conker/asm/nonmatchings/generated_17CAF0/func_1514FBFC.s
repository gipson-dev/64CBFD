glabel func_1514FBFC
    /* 17D0AC 1514FBFC 27BDFF98 */  addiu      $sp, $sp, -0x68
    /* 17D0B0 1514FC00 AFBF0024 */  sw         $ra, 0x24($sp)
    /* 17D0B4 1514FC04 AFA40068 */  sw         $a0, 0x68($sp)
    /* 17D0B8 1514FC08 AFA5006C */  sw         $a1, 0x6C($sp)
    /* 17D0BC 1514FC0C AFA60070 */  sw         $a2, 0x70($sp)
    /* 17D0C0 1514FC10 8FA40068 */  lw         $a0, 0x68($sp)
    /* 17D0C4 1514FC14 27A5005C */  addiu      $a1, $sp, 0x5C
    /* 17D0C8 1514FC18 27A60048 */  addiu      $a2, $sp, 0x48
    /* 17D0CC 1514FC1C 27A70034 */  addiu      $a3, $sp, 0x34
    /* 17D0D0 1514FC20 0D4513A0 */  jal        func_15144E80
    /* 17D0D4 1514FC24 2484000C */   addiu     $a0, $a0, 0xC
    /* 17D0D8 1514FC28 1040002B */  beqz       $v0, .L1514FCD8
    /* 17D0DC 1514FC2C 27A4005C */   addiu     $a0, $sp, 0x5C
    /* 17D0E0 1514FC30 00802825 */  or         $a1, $a0, $zero
    /* 17D0E4 1514FC34 27A60058 */  addiu      $a2, $sp, 0x58
    /* 17D0E8 1514FC38 0D45144A */  jal        func_15145128
    /* 17D0EC 1514FC3C 27A70054 */   addiu     $a3, $sp, 0x54
    /* 17D0F0 1514FC40 27A40048 */  addiu      $a0, $sp, 0x48
    /* 17D0F4 1514FC44 00802825 */  or         $a1, $a0, $zero
    /* 17D0F8 1514FC48 27A60044 */  addiu      $a2, $sp, 0x44
    /* 17D0FC 1514FC4C 0D45144A */  jal        func_15145128
    /* 17D100 1514FC50 27A70040 */   addiu     $a3, $sp, 0x40
    /* 17D104 1514FC54 27A40034 */  addiu      $a0, $sp, 0x34
    /* 17D108 1514FC58 00802825 */  or         $a1, $a0, $zero
    /* 17D10C 1514FC5C 27A60030 */  addiu      $a2, $sp, 0x30
    /* 17D110 1514FC60 0D45144A */  jal        func_15145128
    /* 17D114 1514FC64 27A7002C */   addiu     $a3, $sp, 0x2C
    /* 17D118 1514FC68 27A40034 */  addiu      $a0, $sp, 0x34
    /* 17D11C 1514FC6C 0D45129D */  jal        func_15144A74
    /* 17D120 1514FC70 8FA50068 */   lw        $a1, 0x68($sp)
    /* 17D124 1514FC74 44802000 */  mtc1       $zero, $f4
    /* 17D128 1514FC78 C7A60034 */  lwc1       $f6, 0x34($sp)
    /* 17D12C 1514FC7C 27A50034 */  addiu      $a1, $sp, 0x34
    /* 17D130 1514FC80 4604003C */  c.lt.s     $f0, $f4
    /* 17D134 1514FC84 27A6005C */  addiu      $a2, $sp, 0x5C
    /* 17D138 1514FC88 27A70048 */  addiu      $a3, $sp, 0x48
    /* 17D13C 1514FC8C 4502000A */  bc1fl      .L1514FCB8
    /* 17D140 1514FC90 8FAE0068 */   lw        $t6, 0x68($sp)
    /* 17D144 1514FC94 C7AA0038 */  lwc1       $f10, 0x38($sp)
    /* 17D148 1514FC98 C7B2003C */  lwc1       $f18, 0x3C($sp)
    /* 17D14C 1514FC9C 46003207 */  neg.s      $f8, $f6
    /* 17D150 1514FCA0 46005407 */  neg.s      $f16, $f10
    /* 17D154 1514FCA4 46009107 */  neg.s      $f4, $f18
    /* 17D158 1514FCA8 E7A80034 */  swc1       $f8, 0x34($sp)
    /* 17D15C 1514FCAC E7B00038 */  swc1       $f16, 0x38($sp)
    /* 17D160 1514FCB0 E7A4003C */  swc1       $f4, 0x3C($sp)
    /* 17D164 1514FCB4 8FAE0068 */  lw         $t6, 0x68($sp)
  .L1514FCB8:
    /* 17D168 1514FCB8 93AF006F */  lbu        $t7, 0x6F($sp)
    /* 17D16C 1514FCBC 8FB80070 */  lw         $t8, 0x70($sp)
    /* 17D170 1514FCC0 C5C60020 */  lwc1       $f6, 0x20($t6)
    /* 17D174 1514FCC4 25C40024 */  addiu      $a0, $t6, 0x24
    /* 17D178 1514FCC8 AFAF0014 */  sw         $t7, 0x14($sp)
    /* 17D17C 1514FCCC AFB80018 */  sw         $t8, 0x18($sp)
    /* 17D180 1514FCD0 0D453E3E */  jal        func_1514F8F8
    /* 17D184 1514FCD4 E7A60010 */   swc1      $f6, 0x10($sp)
  .L1514FCD8:
    /* 17D188 1514FCD8 8FBF0024 */  lw         $ra, 0x24($sp)
    /* 17D18C 1514FCDC 27BD0068 */  addiu      $sp, $sp, 0x68
    /* 17D190 1514FCE0 03E00008 */  jr         $ra
    /* 17D194 1514FCE4 00000000 */   nop
endlabel func_1514FBFC
