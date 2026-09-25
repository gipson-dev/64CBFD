glabel func_151D3F14
    /* 2013C4 151D3F14 27BDFFB0 */  addiu      $sp, $sp, -0x50
    /* 2013C8 151D3F18 AFBF0034 */  sw         $ra, 0x34($sp)
    /* 2013CC 151D3F1C AFA50054 */  sw         $a1, 0x54($sp)
    /* 2013D0 151D3F20 AFA60058 */  sw         $a2, 0x58($sp)
    /* 2013D4 151D3F24 240E0003 */  addiu      $t6, $zero, 0x3
    /* 2013D8 151D3F28 240FFFFF */  addiu      $t7, $zero, -0x1
    /* 2013DC 151D3F2C A3AE0048 */  sb         $t6, 0x48($sp)
    /* 2013E0 151D3F30 A3AF0049 */  sb         $t7, 0x49($sp)
    /* 2013E4 151D3F34 0D42B688 */  jal        func_150ADA20
    /* 2013E8 151D3F38 AFA40050 */   sw        $a0, 0x50($sp)
    /* 2013EC 151D3F3C 24010003 */  addiu      $at, $zero, 0x3
    /* 2013F0 151D3F40 0041001B */  divu       $zero, $v0, $at
    /* 2013F4 151D3F44 8FA40050 */  lw         $a0, 0x50($sp)
    /* 2013F8 151D3F48 0000C010 */  mfhi       $t8
    /* 2013FC 151D3F4C 27190004 */  addiu      $t9, $t8, 0x4
    /* 201400 151D3F50 A7B9004A */  sh         $t9, 0x4A($sp)
    /* 201404 151D3F54 A3A0004C */  sb         $zero, 0x4C($sp)
    /* 201408 151D3F58 C4840000 */  lwc1       $f4, 0x0($a0)
    /* 20140C 151D3F5C 4600218D */  trunc.w.s  $f6, $f4
    /* 201410 151D3F60 44093000 */  mfc1       $t1, $f6
    /* 201414 151D3F64 00000000 */  nop
    /* 201418 151D3F68 AFA9003C */  sw         $t1, 0x3C($sp)
    /* 20141C 151D3F6C C4880004 */  lwc1       $f8, 0x4($a0)
    /* 201420 151D3F70 4600428D */  trunc.w.s  $f10, $f8
    /* 201424 151D3F74 440B5000 */  mfc1       $t3, $f10
    /* 201428 151D3F78 00000000 */  nop
    /* 20142C 151D3F7C AFAB0040 */  sw         $t3, 0x40($sp)
    /* 201430 151D3F80 C4900008 */  lwc1       $f16, 0x8($a0)
    /* 201434 151D3F84 4600848D */  trunc.w.s  $f18, $f16
    /* 201438 151D3F88 440D9000 */  mfc1       $t5, $f18
    /* 20143C 151D3F8C 0D42B688 */  jal        func_150ADA20
    /* 201440 151D3F90 AFAD0044 */   sw        $t5, 0x44($sp)
    /* 201444 151D3F94 2401000D */  addiu      $at, $zero, 0xD
    /* 201448 151D3F98 0041001B */  divu       $zero, $v0, $at
    /* 20144C 151D3F9C 93B90057 */  lbu        $t9, 0x57($sp)
    /* 201450 151D3FA0 8FA80058 */  lw         $t0, 0x58($sp)
    /* 201454 151D3FA4 00003010 */  mfhi       $a2
    /* 201458 151D3FA8 240E00E8 */  addiu      $t6, $zero, 0xE8
    /* 20145C 151D3FAC 240F00AB */  addiu      $t7, $zero, 0xAB
    /* 201460 151D3FB0 241800FF */  addiu      $t8, $zero, 0xFF
    /* 201464 151D3FB4 AFB80018 */  sw         $t8, 0x18($sp)
    /* 201468 151D3FB8 AFAF0014 */  sw         $t7, 0x14($sp)
    /* 20146C 151D3FBC AFAE0010 */  sw         $t6, 0x10($sp)
    /* 201470 151D3FC0 24C60014 */  addiu      $a2, $a2, 0x14
    /* 201474 151D3FC4 27A40048 */  addiu      $a0, $sp, 0x48
    /* 201478 151D3FC8 27A5003C */  addiu      $a1, $sp, 0x3C
    /* 20147C 151D3FCC 240700FF */  addiu      $a3, $zero, 0xFF
    /* 201480 151D3FD0 AFA0001C */  sw         $zero, 0x1C($sp)
    /* 201484 151D3FD4 AFA00020 */  sw         $zero, 0x20($sp)
    /* 201488 151D3FD8 AFB90024 */  sw         $t9, 0x24($sp)
    /* 20148C 151D3FDC 0D4580B0 */  jal        func_151602C0
    /* 201490 151D3FE0 AFA80028 */   sw        $t0, 0x28($sp)
    /* 201494 151D3FE4 8FBF0034 */  lw         $ra, 0x34($sp)
    /* 201498 151D3FE8 27BD0050 */  addiu      $sp, $sp, 0x50
    /* 20149C 151D3FEC 03E00008 */  jr         $ra
    /* 2014A0 151D3FF0 00000000 */   nop
endlabel func_151D3F14
