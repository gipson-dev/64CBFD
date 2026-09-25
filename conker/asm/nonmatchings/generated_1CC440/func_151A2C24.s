glabel func_151A2C24
    /* 1D00D4 151A2C24 27BDFF00 */  addiu      $sp, $sp, -0x100
    /* 1D00D8 151A2C28 AFBF00A4 */  sw         $ra, 0xA4($sp)
    /* 1D00DC 151A2C2C AFBE00A0 */  sw         $fp, 0xA0($sp)
    /* 1D00E0 151A2C30 AFB7009C */  sw         $s7, 0x9C($sp)
    /* 1D00E4 151A2C34 AFB60098 */  sw         $s6, 0x98($sp)
    /* 1D00E8 151A2C38 AFB50094 */  sw         $s5, 0x94($sp)
    /* 1D00EC 151A2C3C AFB40090 */  sw         $s4, 0x90($sp)
    /* 1D00F0 151A2C40 AFB3008C */  sw         $s3, 0x8C($sp)
    /* 1D00F4 151A2C44 AFB20088 */  sw         $s2, 0x88($sp)
    /* 1D00F8 151A2C48 AFB10084 */  sw         $s1, 0x84($sp)
    /* 1D00FC 151A2C4C AFB00080 */  sw         $s0, 0x80($sp)
    /* 1D0100 151A2C50 F7BE0078 */  sdc1       $f30, 0x78($sp)
    /* 1D0104 151A2C54 F7BC0070 */  sdc1       $f28, 0x70($sp)
    /* 1D0108 151A2C58 F7BA0068 */  sdc1       $f26, 0x68($sp)
    /* 1D010C 151A2C5C F7B80060 */  sdc1       $f24, 0x60($sp)
    /* 1D0110 151A2C60 F7B60058 */  sdc1       $f22, 0x58($sp)
    /* 1D0114 151A2C64 F7B40050 */  sdc1       $f20, 0x50($sp)
    /* 1D0118 151A2C68 AFA40100 */  sw         $a0, 0x100($sp)
    /* 1D011C 151A2C6C AFA50104 */  sw         $a1, 0x104($sp)
    /* 1D0120 151A2C70 AFA60108 */  sw         $a2, 0x108($sp)
    /* 1D0124 151A2C74 AFA7010C */  sw         $a3, 0x10C($sp)
    /* 1D0128 151A2C78 93AE0157 */  lbu        $t6, 0x157($sp)
    /* 1D012C 151A2C7C 3C18151A */  lui        $t8, %hi(func_151A2BD0)
    /* 1D0130 151A2C80 3C0F151A */  lui        $t7, %hi(func_151A2B84)
    /* 1D0134 151A2C84 15C00004 */  bnez       $t6, .L151A2C98
    /* 1D0138 151A2C88 27182BD0 */   addiu     $t8, $t8, %lo(func_151A2BD0)
    /* 1D013C 151A2C8C 25EF2B84 */  addiu      $t7, $t7, %lo(func_151A2B84)
    /* 1D0140 151A2C90 10000002 */  b          .L151A2C9C
    /* 1D0144 151A2C94 AFAF00F0 */   sw        $t7, 0xF0($sp)
  .L151A2C98:
    /* 1D0148 151A2C98 AFB800F0 */  sw         $t8, 0xF0($sp)
  .L151A2C9C:
    /* 1D014C 151A2C9C 87A20142 */  lh         $v0, 0x142($sp)
    /* 1D0150 151A2CA0 87A30146 */  lh         $v1, 0x146($sp)
    /* 1D0154 151A2CA4 27B700C8 */  addiu      $s7, $sp, 0xC8
    /* 1D0158 151A2CA8 27B600D8 */  addiu      $s6, $sp, 0xD8
    /* 1D015C 151A2CAC 0043082A */  slt        $at, $v0, $v1
    /* 1D0160 151A2CB0 10200003 */  beqz       $at, .L151A2CC0
    /* 1D0164 151A2CB4 27B500E4 */   addiu     $s5, $sp, 0xE4
    /* 1D0168 151A2CB8 10000002 */  b          .L151A2CC4
    /* 1D016C 151A2CBC A7A200FE */   sh        $v0, 0xFE($sp)
  .L151A2CC0:
    /* 1D0170 151A2CC0 A7A300FE */  sh         $v1, 0xFE($sp)
  .L151A2CC4:
    /* 1D0174 151A2CC4 8FB3011C */  lw         $s3, 0x11C($sp)
    /* 1D0178 151A2CC8 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 1D017C 151A2CCC 44812000 */  mtc1       $at, $f4
    /* 1D0180 151A2CD0 44933000 */  mtc1       $s3, $f6
    /* 1D0184 151A2CD4 87BE0136 */  lh         $fp, 0x136($sp)
    /* 1D0188 151A2CD8 4480A000 */  mtc1       $zero, $f20
    /* 1D018C 151A2CDC 46803220 */  cvt.s.w    $f8, $f6
    /* 1D0190 151A2CE0 87B90132 */  lh         $t9, 0x132($sp)
    /* 1D0194 151A2CE4 27DE0001 */  addiu      $fp, $fp, 0x1
    /* 1D0198 151A2CE8 12600076 */  beqz       $s3, .L151A2EC4
    /* 1D019C 151A2CEC 46082603 */   div.s     $f24, $f4, $f8
    /* 1D01A0 151A2CF0 87A8013E */  lh         $t0, 0x13E($sp)
    /* 1D01A4 151A2CF4 87AA013A */  lh         $t2, 0x13A($sp)
    /* 1D01A8 151A2CF8 AFB900B0 */  sw         $t9, 0xB0($sp)
    /* 1D01AC 151A2CFC 25090001 */  addiu      $t1, $t0, 0x1
    /* 1D01B0 151A2D00 AFA900AC */  sw         $t1, 0xAC($sp)
    /* 1D01B4 151A2D04 C7BE0124 */  lwc1       $f30, 0x124($sp)
    /* 1D01B8 151A2D08 C7BC0110 */  lwc1       $f28, 0x110($sp)
    /* 1D01BC 151A2D0C C7BA0120 */  lwc1       $f26, 0x120($sp)
    /* 1D01C0 151A2D10 AFAA00A8 */  sw         $t2, 0xA8($sp)
  .L151A2D14:
    /* 1D01C4 151A2D14 0D42B688 */  jal        func_150ADA20
    /* 1D01C8 151A2D18 00000000 */   nop
    /* 1D01CC 151A2D1C 005E001B */  divu       $zero, $v0, $fp
    /* 1D01D0 151A2D20 8FAC00B0 */  lw         $t4, 0xB0($sp)
    /* 1D01D4 151A2D24 00005810 */  mfhi       $t3
    /* 1D01D8 151A2D28 016CA021 */  addu       $s4, $t3, $t4
    /* 1D01DC 151A2D2C 00146C00 */  sll        $t5, $s4, 16
    /* 1D01E0 151A2D30 17C00002 */  bnez       $fp, .L151A2D3C
    /* 1D01E4 151A2D34 00000000 */   nop
    /* 1D01E8 151A2D38 0007000D */  break      7
  .L151A2D3C:
    /* 1D01EC 151A2D3C 000DA403 */  sra        $s4, $t5, 16
    /* 1D01F0 151A2D40 0D42B688 */  jal        func_150ADA20
    /* 1D01F4 151A2D44 00000000 */   nop
    /* 1D01F8 151A2D48 0D42B688 */  jal        func_150ADA20
    /* 1D01FC 151A2D4C 00408825 */   or        $s1, $v0, $zero
    /* 1D0200 151A2D50 0D42B69A */  jal        func_150ADA68
    /* 1D0204 151A2D54 00408025 */   or        $s0, $v0, $zero
    /* 1D0208 151A2D58 461A0282 */  mul.s      $f10, $f0, $f26
    /* 1D020C 151A2D5C 322400FF */  andi       $a0, $s1, 0xFF
    /* 1D0210 151A2D60 320500FF */  andi       $a1, $s0, 0xFF
    /* 1D0214 151A2D64 0005CC00 */  sll        $t9, $a1, 16
    /* 1D0218 151A2D68 00047C00 */  sll        $t7, $a0, 16
    /* 1D021C 151A2D6C 000F2403 */  sra        $a0, $t7, 16
    /* 1D0220 151A2D70 00192C03 */  sra        $a1, $t9, 16
    /* 1D0224 151A2D74 44065000 */  mfc1       $a2, $f10
    /* 1D0228 151A2D78 0D450DE5 */  jal        func_15143794
    /* 1D022C 151A2D7C 02A03825 */   or        $a3, $s5, $zero
    /* 1D0230 151A2D80 8FB900F0 */  lw         $t9, 0xF0($sp)
    /* 1D0234 151A2D84 4407E000 */  mfc1       $a3, $f28
    /* 1D0238 151A2D88 8FA40104 */  lw         $a0, 0x104($sp)
    /* 1D023C 151A2D8C 87A5010A */  lh         $a1, 0x10A($sp)
    /* 1D0240 151A2D90 87A6010E */  lh         $a2, 0x10E($sp)
    /* 1D0244 151A2D94 E7B40010 */  swc1       $f20, 0x10($sp)
    /* 1D0248 151A2D98 0320F809 */  jalr       $t9
    /* 1D024C 151A2D9C AFB60014 */   sw        $s6, 0x14($sp)
    /* 1D0250 151A2DA0 3C098009 */  lui        $t1, %hi(D_8008F8E8)
    /* 1D0254 151A2DA4 2529F8E8 */  addiu      $t1, $t1, %lo(D_8008F8E8)
    /* 1D0258 151A2DA8 8D210000 */  lw         $at, 0x0($t1)
    /* 1D025C 151A2DAC AEE10000 */  sw         $at, 0x0($s7)
    /* 1D0260 151A2DB0 8D2C0004 */  lw         $t4, 0x4($t1)
    /* 1D0264 151A2DB4 AEEC0004 */  sw         $t4, 0x4($s7)
    /* 1D0268 151A2DB8 8D210008 */  lw         $at, 0x8($t1)
    /* 1D026C 151A2DBC 0D42B688 */  jal        func_150ADA20
    /* 1D0270 151A2DC0 AEE10008 */   sw        $at, 0x8($s7)
    /* 1D0274 151A2DC4 0D42B69A */  jal        func_150ADA68
    /* 1D0278 151A2DC8 30520003 */   andi      $s2, $v0, 0x3
    /* 1D027C 151A2DCC 0D42B688 */  jal        func_150ADA20
    /* 1D0280 151A2DD0 46000586 */   mov.s     $f22, $f0
    /* 1D0284 151A2DD4 0D42B69A */  jal        func_150ADA68
    /* 1D0288 151A2DD8 00408825 */   or        $s1, $v0, $zero
    /* 1D028C 151A2DDC 3C01800B */  lui        $at, %hi(D_800A8D2C)
    /* 1D0290 151A2DE0 C4308D2C */  lwc1       $f16, %lo(D_800A8D2C)($at)
    /* 1D0294 151A2DE4 C7B2012C */  lwc1       $f18, 0x12C($sp)
    /* 1D0298 151A2DE8 4407F000 */  mfc1       $a3, $f30
    /* 1D029C 151A2DEC 4610003C */  c.lt.s     $f0, $f16
    /* 1D02A0 151A2DF0 4612B182 */  mul.s      $f6, $f22, $f18
    /* 1D02A4 151A2DF4 8FA40100 */  lw         $a0, 0x100($sp)
    /* 1D02A8 151A2DF8 02A02825 */  or         $a1, $s5, $zero
    /* 1D02AC 151A2DFC 45000003 */  bc1f       .L151A2E0C
    /* 1D02B0 151A2E00 02C03025 */   or        $a2, $s6, $zero
    /* 1D02B4 151A2E04 10000002 */  b          .L151A2E10
    /* 1D02B8 151A2E08 24100019 */   addiu     $s0, $zero, 0x19
  .L151A2E0C:
    /* 1D02BC 151A2E0C 2410FFFF */  addiu      $s0, $zero, -0x1
  .L151A2E10:
    /* 1D02C0 151A2E10 8FAF00AC */  lw         $t7, 0xAC($sp)
    /* 1D02C4 151A2E14 C7AA0118 */  lwc1       $f10, 0x118($sp)
    /* 1D02C8 151A2E18 C7A40128 */  lwc1       $f4, 0x128($sp)
    /* 1D02CC 151A2E1C 022F001B */  divu       $zero, $s1, $t7
    /* 1D02D0 151A2E20 46145402 */  mul.s      $f16, $f10, $f20
    /* 1D02D4 151A2E24 C7B20114 */  lwc1       $f18, 0x114($sp)
    /* 1D02D8 151A2E28 46043200 */  add.s      $f8, $f6, $f4
    /* 1D02DC 151A2E2C 87AD00FE */  lh         $t5, 0xFE($sp)
    /* 1D02E0 151A2E30 8FA800A8 */  lw         $t0, 0xA8($sp)
    /* 1D02E4 151A2E34 87AB0142 */  lh         $t3, 0x142($sp)
    /* 1D02E8 151A2E38 87AA0146 */  lh         $t2, 0x146($sp)
    /* 1D02EC 151A2E3C 46128180 */  add.s      $f6, $f16, $f18
    /* 1D02F0 151A2E40 83A9014B */  lb         $t1, 0x14B($sp)
    /* 1D02F4 151A2E44 0000C010 */  mfhi       $t8
    /* 1D02F8 151A2E48 00126080 */  sll        $t4, $s2, 2
    /* 1D02FC 151A2E4C 01926023 */  subu       $t4, $t4, $s2
    /* 1D0300 151A2E50 028D7021 */  addu       $t6, $s4, $t5
    /* 1D0304 151A2E54 0308C821 */  addu       $t9, $t8, $t0
    /* 1D0308 151A2E58 AFB9001C */  sw         $t9, 0x1C($sp)
    /* 1D030C 151A2E5C AFAE0018 */  sw         $t6, 0x18($sp)
    /* 1D0310 151A2E60 02EC1021 */  addu       $v0, $s7, $t4
    /* 1D0314 151A2E64 E7A60014 */  swc1       $f6, 0x14($sp)
    /* 1D0318 151A2E68 E7A80010 */  swc1       $f8, 0x10($sp)
    /* 1D031C 151A2E6C AFB00028 */  sw         $s0, 0x28($sp)
    /* 1D0320 151A2E70 AFAB0020 */  sw         $t3, 0x20($sp)
    /* 1D0324 151A2E74 AFAA0024 */  sw         $t2, 0x24($sp)
    /* 1D0328 151A2E78 AFA9002C */  sw         $t1, 0x2C($sp)
    /* 1D032C 151A2E7C 904D0000 */  lbu        $t5, 0x0($v0)
    /* 1D0330 151A2E80 15E00002 */  bnez       $t7, .L151A2E8C
    /* 1D0334 151A2E84 00000000 */   nop
    /* 1D0338 151A2E88 0007000D */  break      7
  .L151A2E8C:
    /* 1D033C 151A2E8C AFAD0030 */  sw         $t5, 0x30($sp)
    /* 1D0340 151A2E90 904E0001 */  lbu        $t6, 0x1($v0)
    /* 1D0344 151A2E94 8FA80150 */  lw         $t0, 0x150($sp)
    /* 1D0348 151A2E98 93B8014F */  lbu        $t8, 0x14F($sp)
    /* 1D034C 151A2E9C AFAE0034 */  sw         $t6, 0x34($sp)
    /* 1D0350 151A2EA0 904F0002 */  lbu        $t7, 0x2($v0)
    /* 1D0354 151A2EA4 AFA80040 */  sw         $t0, 0x40($sp)
    /* 1D0358 151A2EA8 AFB8003C */  sw         $t8, 0x3C($sp)
    /* 1D035C 151A2EAC 0D4689BB */  jal        func_151A26EC
    /* 1D0360 151A2EB0 AFAF0038 */   sw        $t7, 0x38($sp)
    /* 1D0364 151A2EB4 4618A500 */  add.s      $f20, $f20, $f24
    /* 1D0368 151A2EB8 2673FFFF */  addiu      $s3, $s3, -0x1
    /* 1D036C 151A2EBC 1660FF95 */  bnez       $s3, .L151A2D14
    /* 1D0370 151A2EC0 00000000 */   nop
  .L151A2EC4:
    /* 1D0374 151A2EC4 8FBF00A4 */  lw         $ra, 0xA4($sp)
    /* 1D0378 151A2EC8 D7B40050 */  ldc1       $f20, 0x50($sp)
    /* 1D037C 151A2ECC D7B60058 */  ldc1       $f22, 0x58($sp)
    /* 1D0380 151A2ED0 D7B80060 */  ldc1       $f24, 0x60($sp)
    /* 1D0384 151A2ED4 D7BA0068 */  ldc1       $f26, 0x68($sp)
    /* 1D0388 151A2ED8 D7BC0070 */  ldc1       $f28, 0x70($sp)
    /* 1D038C 151A2EDC D7BE0078 */  ldc1       $f30, 0x78($sp)
    /* 1D0390 151A2EE0 8FB00080 */  lw         $s0, 0x80($sp)
    /* 1D0394 151A2EE4 8FB10084 */  lw         $s1, 0x84($sp)
    /* 1D0398 151A2EE8 8FB20088 */  lw         $s2, 0x88($sp)
    /* 1D039C 151A2EEC 8FB3008C */  lw         $s3, 0x8C($sp)
    /* 1D03A0 151A2EF0 8FB40090 */  lw         $s4, 0x90($sp)
    /* 1D03A4 151A2EF4 8FB50094 */  lw         $s5, 0x94($sp)
    /* 1D03A8 151A2EF8 8FB60098 */  lw         $s6, 0x98($sp)
    /* 1D03AC 151A2EFC 8FB7009C */  lw         $s7, 0x9C($sp)
    /* 1D03B0 151A2F00 8FBE00A0 */  lw         $fp, 0xA0($sp)
    /* 1D03B4 151A2F04 03E00008 */  jr         $ra
    /* 1D03B8 151A2F08 27BD0100 */   addiu     $sp, $sp, 0x100
endlabel func_151A2C24
