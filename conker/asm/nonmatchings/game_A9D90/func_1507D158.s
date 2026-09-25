glabel func_1507D158
    /* AA608 1507D158 27BDFFE0 */  addiu      $sp, $sp, -0x20
    /* AA60C 1507D15C AFA60028 */  sw         $a2, 0x28($sp)
    /* AA610 1507D160 AFA7002C */  sw         $a3, 0x2C($sp)
    /* AA614 1507D164 8FA70028 */  lw         $a3, 0x28($sp)
    /* AA618 1507D168 00A03025 */  or         $a2, $a1, $zero
    /* AA61C 1507D16C AFBF001C */  sw         $ra, 0x1C($sp)
    /* AA620 1507D170 AFA40020 */  sw         $a0, 0x20($sp)
    /* AA624 1507D174 AFA50024 */  sw         $a1, 0x24($sp)
    /* AA628 1507D178 8FAE0020 */  lw         $t6, 0x20($sp)
    /* AA62C 1507D17C 3C02800D */  lui        $v0, %hi(D_800CC40F)
    /* AA630 1507D180 8FB8002C */  lw         $t8, 0x2C($sp)
    /* AA634 1507D184 000E7880 */  sll        $t7, $t6, 2
    /* AA638 1507D188 01EE7823 */  subu       $t7, $t7, $t6
    /* AA63C 1507D18C 000F7880 */  sll        $t7, $t7, 2
    /* AA640 1507D190 01EE7821 */  addu       $t7, $t7, $t6
    /* AA644 1507D194 000F7880 */  sll        $t7, $t7, 2
    /* AA648 1507D198 01EE7823 */  subu       $t7, $t7, $t6
    /* AA64C 1507D19C 000F7880 */  sll        $t7, $t7, 2
    /* AA650 1507D1A0 01EE7823 */  subu       $t7, $t7, $t6
    /* AA654 1507D1A4 000F7880 */  sll        $t7, $t7, 2
    /* AA658 1507D1A8 004F1021 */  addu       $v0, $v0, $t7
    /* AA65C 1507D1AC 9042C40F */  lbu        $v0, %lo(D_800CC40F)($v0)
    /* AA660 1507D1B0 8FB90030 */  lw         $t9, 0x30($sp)
    /* AA664 1507D1B4 24040003 */  addiu      $a0, $zero, 0x3
    /* AA668 1507D1B8 AFB80010 */  sw         $t8, 0x10($sp)
    /* AA66C 1507D1BC 34452000 */  ori        $a1, $v0, 0x2000
    /* AA670 1507D1C0 0D426FEC */  jal        func_1509BFB0
    /* AA674 1507D1C4 AFB90014 */   sw        $t9, 0x14($sp)
    /* AA678 1507D1C8 8FBF001C */  lw         $ra, 0x1C($sp)
    /* AA67C 1507D1CC 27BD0020 */  addiu      $sp, $sp, 0x20
    /* AA680 1507D1D0 03E00008 */  jr         $ra
    /* AA684 1507D1D4 00000000 */   nop
endlabel func_1507D158
