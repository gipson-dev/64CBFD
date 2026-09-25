glabel func_151B8400
    /* 1E58B0 151B8400 27BDFF50 */  addiu      $sp, $sp, -0xB0
    /* 1E58B4 151B8404 3C013E80 */  lui        $at, (0x3E800000 >> 16)
    /* 1E58B8 151B8408 AFB00038 */  sw         $s0, 0x38($sp)
    /* 1E58BC 151B840C 44810000 */  mtc1       $at, $f0
    /* 1E58C0 151B8410 00808025 */  or         $s0, $a0, $zero
    /* 1E58C4 151B8414 AFBF003C */  sw         $ra, 0x3C($sp)
    /* 1E58C8 151B8418 27A20044 */  addiu      $v0, $sp, 0x44
    /* 1E58CC 151B841C 3C014110 */  lui        $at, (0x41100000 >> 16)
    /* 1E58D0 151B8420 44812000 */  mtc1       $at, $f4
    /* 1E58D4 151B8424 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 1E58D8 151B8428 44813000 */  mtc1       $at, $f6
    /* 1E58DC 151B842C 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 1E58E0 151B8430 240F5901 */  addiu      $t7, $zero, 0x5901
    /* 1E58E4 151B8434 24180032 */  addiu      $t8, $zero, 0x32
    /* 1E58E8 151B8438 241900FF */  addiu      $t9, $zero, 0xFF
    /* 1E58EC 151B843C 240800E6 */  addiu      $t0, $zero, 0xE6
    /* 1E58F0 151B8440 240900B6 */  addiu      $t1, $zero, 0xB6
    /* 1E58F4 151B8444 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 1E58F8 151B8448 AFB000A8 */  sw         $s0, 0xA8($sp)
    /* 1E58FC 151B844C A3AE0050 */  sb         $t6, 0x50($sp)
    /* 1E5900 151B8450 A3A00051 */  sb         $zero, 0x51($sp)
    /* 1E5904 151B8454 A7AF0052 */  sh         $t7, 0x52($sp)
    /* 1E5908 151B8458 A7B80054 */  sh         $t8, 0x54($sp)
    /* 1E590C 151B845C AFA00058 */  sw         $zero, 0x58($sp)
    /* 1E5910 151B8460 AFA0005C */  sw         $zero, 0x5C($sp)
    /* 1E5914 151B8464 A3B90060 */  sb         $t9, 0x60($sp)
    /* 1E5918 151B8468 A3A80061 */  sb         $t0, 0x61($sp)
    /* 1E591C 151B846C A3A90062 */  sb         $t1, 0x62($sp)
    /* 1E5920 151B8470 A3AA0063 */  sb         $t2, 0x63($sp)
    /* 1E5924 151B8474 E7A40064 */  swc1       $f4, 0x64($sp)
    /* 1E5928 151B8478 E7A60068 */  swc1       $f6, 0x68($sp)
    /* 1E592C 151B847C 8E010038 */  lw         $at, 0x38($s0)
    /* 1E5930 151B8480 27AE0078 */  addiu      $t6, $sp, 0x78
    /* 1E5934 151B8484 27A8006C */  addiu      $t0, $sp, 0x6C
    /* 1E5938 151B8488 AC410000 */  sw         $at, 0x0($v0)
    /* 1E593C 151B848C 8E0D003C */  lw         $t5, 0x3C($s0)
    /* 1E5940 151B8490 3C0B0CCC */  lui        $t3, (0xCCC0000 >> 16)
    /* 1E5944 151B8494 241800FF */  addiu      $t8, $zero, 0xFF
    /* 1E5948 151B8498 AC4D0004 */  sw         $t5, 0x4($v0)
    /* 1E594C 151B849C 8E010040 */  lw         $at, 0x40($s0)
    /* 1E5950 151B84A0 240D00C8 */  addiu      $t5, $zero, 0xC8
    /* 1E5954 151B84A4 240F0006 */  addiu      $t7, $zero, 0x6
    /* 1E5958 151B84A8 AC410008 */  sw         $at, 0x8($v0)
    /* 1E595C 151B84AC 8C410000 */  lw         $at, 0x0($v0)
    /* 1E5960 151B84B0 240A0005 */  addiu      $t2, $zero, 0x5
    /* 1E5964 151B84B4 24090019 */  addiu      $t1, $zero, 0x19
    /* 1E5968 151B84B8 ADC10000 */  sw         $at, 0x0($t6)
    /* 1E596C 151B84BC 8C590004 */  lw         $t9, 0x4($v0)
    /* 1E5970 151B84C0 3C05800B */  lui        $a1, %hi(D_800AA490)
    /* 1E5974 151B84C4 24A5A490 */  addiu      $a1, $a1, %lo(D_800AA490)
    /* 1E5978 151B84C8 ADD90004 */  sw         $t9, 0x4($t6)
    /* 1E597C 151B84CC 8C410008 */  lw         $at, 0x8($v0)
    /* 1E5980 151B84D0 24190032 */  addiu      $t9, $zero, 0x32
    /* 1E5984 151B84D4 27A40050 */  addiu      $a0, $sp, 0x50
    /* 1E5988 151B84D8 ADC10008 */  sw         $at, 0x8($t6)
    /* 1E598C 151B84DC 8C410000 */  lw         $at, 0x0($v0)
    /* 1E5990 151B84E0 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 1E5994 151B84E4 2406001B */  addiu      $a2, $zero, 0x1B
    /* 1E5998 151B84E8 AD010000 */  sw         $at, 0x0($t0)
    /* 1E599C 151B84EC 8C4C0004 */  lw         $t4, 0x4($v0)
    /* 1E59A0 151B84F0 00003825 */  or         $a3, $zero, $zero
    /* 1E59A4 151B84F4 AD0C0004 */  sw         $t4, 0x4($t0)
    /* 1E59A8 151B84F8 8C410008 */  lw         $at, 0x8($v0)
    /* 1E59AC 151B84FC AD010008 */  sw         $at, 0x8($t0)
    /* 1E59B0 151B8500 C6080044 */  lwc1       $f8, 0x44($s0)
    /* 1E59B4 151B8504 24080004 */  addiu      $t0, $zero, 0x4
    /* 1E59B8 151B8508 46004282 */  mul.s      $f10, $f8, $f0
    /* 1E59BC 151B850C E7AA0084 */  swc1       $f10, 0x84($sp)
    /* 1E59C0 151B8510 C6100048 */  lwc1       $f16, 0x48($s0)
    /* 1E59C4 151B8514 46008482 */  mul.s      $f18, $f16, $f0
    /* 1E59C8 151B8518 E7B20088 */  swc1       $f18, 0x88($sp)
    /* 1E59CC 151B851C C604004C */  lwc1       $f4, 0x4C($s0)
    /* 1E59D0 151B8520 AFAB0090 */  sw         $t3, 0x90($sp)
    /* 1E59D4 151B8524 A3AD0094 */  sb         $t5, 0x94($sp)
    /* 1E59D8 151B8528 46002182 */  mul.s      $f6, $f4, $f0
    /* 1E59DC 151B852C A3B80095 */  sb         $t8, 0x95($sp)
    /* 1E59E0 151B8530 A3A00096 */  sb         $zero, 0x96($sp)
    /* 1E59E4 151B8534 A3AF0097 */  sb         $t7, 0x97($sp)
    /* 1E59E8 151B8538 AFA00098 */  sw         $zero, 0x98($sp)
    /* 1E59EC 151B853C A3AE009C */  sb         $t6, 0x9C($sp)
    /* 1E59F0 151B8540 AFA000A0 */  sw         $zero, 0xA0($sp)
    /* 1E59F4 151B8544 E7A6008C */  swc1       $f6, 0x8C($sp)
    /* 1E59F8 151B8548 A7B900A4 */  sh         $t9, 0xA4($sp)
    /* 1E59FC 151B854C A7AA00A6 */  sh         $t2, 0xA6($sp)
    /* 1E5A00 151B8550 AFA80024 */  sw         $t0, 0x24($sp)
    /* 1E5A04 151B8554 AFA00020 */  sw         $zero, 0x20($sp)
    /* 1E5A08 151B8558 AFA0001C */  sw         $zero, 0x1C($sp)
    /* 1E5A0C 151B855C AFA00018 */  sw         $zero, 0x18($sp)
    /* 1E5A10 151B8560 AFA90014 */  sw         $t1, 0x14($sp)
    /* 1E5A14 151B8564 AFA00010 */  sw         $zero, 0x10($sp)
    /* 1E5A18 151B8568 920C000C */  lbu        $t4, 0xC($s0)
    /* 1E5A1C 151B856C AFAC0028 */  sw         $t4, 0x28($sp)
    /* 1E5A20 151B8570 920B0001 */  lbu        $t3, 0x1($s0)
    /* 1E5A24 151B8574 0D44F4BC */  jal        func_1513D2F0
    /* 1E5A28 151B8578 AFAB002C */   sw        $t3, 0x2C($sp)
    /* 1E5A2C 151B857C 10400005 */  beqz       $v0, .L151B8594
    /* 1E5A30 151B8580 00408025 */   or        $s0, $v0, $zero
    /* 1E5A34 151B8584 24440110 */  addiu      $a0, $v0, 0x110
    /* 1E5A38 151B8588 27A500A8 */  addiu      $a1, $sp, 0xA8
    /* 1E5A3C 151B858C 0C008BB0 */  jal        memcpy
    /* 1E5A40 151B8590 24060004 */   addiu     $a2, $zero, 0x4
  .L151B8594:
    /* 1E5A44 151B8594 02001025 */  or         $v0, $s0, $zero
    /* 1E5A48 151B8598 8FBF003C */  lw         $ra, 0x3C($sp)
    /* 1E5A4C 151B859C 8FB00038 */  lw         $s0, 0x38($sp)
    /* 1E5A50 151B85A0 27BD00B0 */  addiu      $sp, $sp, 0xB0
    /* 1E5A54 151B85A4 03E00008 */  jr         $ra
    /* 1E5A58 151B85A8 00000000 */   nop
endlabel func_151B8400
