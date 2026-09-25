glabel func_151D3FF4
    /* 2014A4 151D3FF4 27BDFFB0 */  addiu      $sp, $sp, -0x50
    /* 2014A8 151D3FF8 AFBF0034 */  sw         $ra, 0x34($sp)
    /* 2014AC 151D3FFC AFA50054 */  sw         $a1, 0x54($sp)
    /* 2014B0 151D4000 AFA60058 */  sw         $a2, 0x58($sp)
    /* 2014B4 151D4004 240E0003 */  addiu      $t6, $zero, 0x3
    /* 2014B8 151D4008 240FFFFF */  addiu      $t7, $zero, -0x1
    /* 2014BC 151D400C A3AE0048 */  sb         $t6, 0x48($sp)
    /* 2014C0 151D4010 A3AF0049 */  sb         $t7, 0x49($sp)
    /* 2014C4 151D4014 0D42B688 */  jal        func_150ADA20
    /* 2014C8 151D4018 AFA40050 */   sw        $a0, 0x50($sp)
    /* 2014CC 151D401C 2401000B */  addiu      $at, $zero, 0xB
    /* 2014D0 151D4020 0041001B */  divu       $zero, $v0, $at
    /* 2014D4 151D4024 8FA40050 */  lw         $a0, 0x50($sp)
    /* 2014D8 151D4028 0000C010 */  mfhi       $t8
    /* 2014DC 151D402C 27190014 */  addiu      $t9, $t8, 0x14
    /* 2014E0 151D4030 A7B9004A */  sh         $t9, 0x4A($sp)
    /* 2014E4 151D4034 A3A0004C */  sb         $zero, 0x4C($sp)
    /* 2014E8 151D4038 C4840000 */  lwc1       $f4, 0x0($a0)
    /* 2014EC 151D403C 4600218D */  trunc.w.s  $f6, $f4
    /* 2014F0 151D4040 44093000 */  mfc1       $t1, $f6
    /* 2014F4 151D4044 00000000 */  nop
    /* 2014F8 151D4048 AFA9003C */  sw         $t1, 0x3C($sp)
    /* 2014FC 151D404C C4880004 */  lwc1       $f8, 0x4($a0)
    /* 201500 151D4050 4600428D */  trunc.w.s  $f10, $f8
    /* 201504 151D4054 440B5000 */  mfc1       $t3, $f10
    /* 201508 151D4058 00000000 */  nop
    /* 20150C 151D405C AFAB0040 */  sw         $t3, 0x40($sp)
    /* 201510 151D4060 C4900008 */  lwc1       $f16, 0x8($a0)
    /* 201514 151D4064 4600848D */  trunc.w.s  $f18, $f16
    /* 201518 151D4068 440D9000 */  mfc1       $t5, $f18
    /* 20151C 151D406C 0D42B688 */  jal        func_150ADA20
    /* 201520 151D4070 AFAD0044 */   sw        $t5, 0x44($sp)
    /* 201524 151D4074 24010018 */  addiu      $at, $zero, 0x18
    /* 201528 151D4078 0041001B */  divu       $zero, $v0, $at
    /* 20152C 151D407C 93B90057 */  lbu        $t9, 0x57($sp)
    /* 201530 151D4080 8FA80058 */  lw         $t0, 0x58($sp)
    /* 201534 151D4084 00003010 */  mfhi       $a2
    /* 201538 151D4088 240E00A1 */  addiu      $t6, $zero, 0xA1
    /* 20153C 151D408C 240F00A2 */  addiu      $t7, $zero, 0xA2
    /* 201540 151D4090 241800FF */  addiu      $t8, $zero, 0xFF
    /* 201544 151D4094 AFB80018 */  sw         $t8, 0x18($sp)
    /* 201548 151D4098 AFAF0014 */  sw         $t7, 0x14($sp)
    /* 20154C 151D409C AFAE0010 */  sw         $t6, 0x10($sp)
    /* 201550 151D40A0 24C60022 */  addiu      $a2, $a2, 0x22
    /* 201554 151D40A4 27A40048 */  addiu      $a0, $sp, 0x48
    /* 201558 151D40A8 27A5003C */  addiu      $a1, $sp, 0x3C
    /* 20155C 151D40AC 240700FF */  addiu      $a3, $zero, 0xFF
    /* 201560 151D40B0 AFA0001C */  sw         $zero, 0x1C($sp)
    /* 201564 151D40B4 AFA00020 */  sw         $zero, 0x20($sp)
    /* 201568 151D40B8 AFB90024 */  sw         $t9, 0x24($sp)
    /* 20156C 151D40BC 0D4580B0 */  jal        func_151602C0
    /* 201570 151D40C0 AFA80028 */   sw        $t0, 0x28($sp)
    /* 201574 151D40C4 8FBF0034 */  lw         $ra, 0x34($sp)
    /* 201578 151D40C8 27BD0050 */  addiu      $sp, $sp, 0x50
    /* 20157C 151D40CC 03E00008 */  jr         $ra
    /* 201580 151D40D0 00000000 */   nop
endlabel func_151D3FF4
