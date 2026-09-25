glabel func_151C04F8
    /* 1ED9A8 151C04F8 27BDFFD0 */  addiu      $sp, $sp, -0x30
    /* 1ED9AC 151C04FC AFBF0024 */  sw         $ra, 0x24($sp)
    /* 1ED9B0 151C0500 AFA40030 */  sw         $a0, 0x30($sp)
    /* 1ED9B4 151C0504 AFA50034 */  sw         $a1, 0x34($sp)
    /* 1ED9B8 151C0508 AFA60038 */  sw         $a2, 0x38($sp)
    /* 1ED9BC 151C050C 0D42B69A */  jal        func_150ADA68
    /* 1ED9C0 151C0510 00000000 */   nop
    /* 1ED9C4 151C0514 0D42B688 */  jal        func_150ADA20
    /* 1ED9C8 151C0518 E7A00028 */   swc1      $f0, 0x28($sp)
    /* 1ED9CC 151C051C C7B00028 */  lwc1       $f16, 0x28($sp)
    /* 1ED9D0 151C0520 3C014080 */  lui        $at, (0x40800000 >> 16)
    /* 1ED9D4 151C0524 44817000 */  mtc1       $at, $f14
    /* 1ED9D8 151C0528 3C014160 */  lui        $at, (0x41600000 >> 16)
    /* 1ED9DC 151C052C 44816000 */  mtc1       $at, $f12
    /* 1ED9E0 151C0530 460E8382 */  mul.s      $f14, $f16, $f14
    /* 1ED9E4 151C0534 24010038 */  addiu      $at, $zero, 0x38
    /* 1ED9E8 151C0538 0041001B */  divu       $zero, $v0, $at
    /* 1ED9EC 151C053C 460C7300 */  add.s      $f12, $f14, $f12
    /* 1ED9F0 151C0540 00007010 */  mfhi       $t6
    /* 1ED9F4 151C0544 25CF00C8 */  addiu      $t7, $t6, 0xC8
    /* 1ED9F8 151C0548 448F9000 */  mtc1       $t7, $f18
    /* 1ED9FC 151C054C 44056000 */  mfc1       $a1, $f12
    /* 1EDA00 151C0550 3C063F97 */  lui        $a2, (0x3F974EB9 >> 16)
    /* 1EDA04 151C0554 468094A0 */  cvt.s.w    $f18, $f18
    /* 1EDA08 151C0558 8FA40030 */  lw         $a0, 0x30($sp)
    /* 1EDA0C 151C055C 05E10005 */  bgez       $t7, .L151C0574
    /* 1EDA10 151C0560 34C64EB9 */   ori       $a2, $a2, (0x3F974EB9 & 0xFFFF)
    /* 1EDA14 151C0564 3C014F80 */  lui        $at, (0x4F800000 >> 16)
    /* 1EDA18 151C0568 44812000 */  mtc1       $at, $f4
    /* 1EDA1C 151C056C 00000000 */  nop
    /* 1EDA20 151C0570 46049480 */  add.s      $f18, $f18, $f4
  .L151C0574:
    /* 1EDA24 151C0574 44803000 */  mtc1       $zero, $f6
    /* 1EDA28 151C0578 93B80037 */  lbu        $t8, 0x37($sp)
    /* 1EDA2C 151C057C 8FB90038 */  lw         $t9, 0x38($sp)
    /* 1EDA30 151C0580 44079000 */  mfc1       $a3, $f18
    /* 1EDA34 151C0584 AFB80014 */  sw         $t8, 0x14($sp)
    /* 1EDA38 151C0588 E7A60010 */  swc1       $f6, 0x10($sp)
    /* 1EDA3C 151C058C 0D45506E */  jal        func_151541B8
    /* 1EDA40 151C0590 AFB90018 */   sw        $t9, 0x18($sp)
    /* 1EDA44 151C0594 8FBF0024 */  lw         $ra, 0x24($sp)
    /* 1EDA48 151C0598 27BD0030 */  addiu      $sp, $sp, 0x30
    /* 1EDA4C 151C059C 03E00008 */  jr         $ra
    /* 1EDA50 151C05A0 00000000 */   nop
endlabel func_151C04F8
