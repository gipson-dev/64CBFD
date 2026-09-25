glabel func_151B8668
    /* 1E5B18 151B8668 27BDFFC8 */  addiu      $sp, $sp, -0x38
    /* 1E5B1C 151B866C AFA5003C */  sw         $a1, 0x3C($sp)
    /* 1E5B20 151B8670 00C03825 */  or         $a3, $a2, $zero
    /* 1E5B24 151B8674 93A6003F */  lbu        $a2, 0x3F($sp)
    /* 1E5B28 151B8678 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 1E5B2C 151B867C AFA40038 */  sw         $a0, 0x38($sp)
    /* 1E5B30 151B8680 3C014120 */  lui        $at, (0x41200000 >> 16)
    /* 1E5B34 151B8684 44812000 */  mtc1       $at, $f4
    /* 1E5B38 151B8688 3C01800B */  lui        $at, %hi(D_800AA4C8)
    /* 1E5B3C 151B868C C426A4C8 */  lwc1       $f6, %lo(D_800AA4C8)($at)
    /* 1E5B40 151B8690 3C01800E */  lui        $at, %hi(D_800DCA24)
    /* 1E5B44 151B8694 C428CA24 */  lwc1       $f8, %lo(D_800DCA24)($at)
    /* 1E5B48 151B8698 8FAE0038 */  lw         $t6, 0x38($sp)
    /* 1E5B4C 151B869C 2408012C */  addiu      $t0, $zero, 0x12C
    /* 1E5B50 151B86A0 46083282 */  mul.s      $f10, $f6, $f8
    /* 1E5B54 151B86A4 24090003 */  addiu      $t1, $zero, 0x3
    /* 1E5B58 151B86A8 25CF0038 */  addiu      $t7, $t6, 0x38
    /* 1E5B5C 151B86AC 25D8003C */  addiu      $t8, $t6, 0x3C
    /* 1E5B60 151B86B0 25D90040 */  addiu      $t9, $t6, 0x40
    /* 1E5B64 151B86B4 AFAF0018 */  sw         $t7, 0x18($sp)
    /* 1E5B68 151B86B8 AFB8001C */  sw         $t8, 0x1C($sp)
    /* 1E5B6C 151B86BC AFB90020 */  sw         $t9, 0x20($sp)
    /* 1E5B70 151B86C0 E7AA0028 */  swc1       $f10, 0x28($sp)
    /* 1E5B74 151B86C4 A7A8002C */  sh         $t0, 0x2C($sp)
    /* 1E5B78 151B86C8 A3A0002E */  sb         $zero, 0x2E($sp)
    /* 1E5B7C 151B86CC A3A9002F */  sb         $t1, 0x2F($sp)
    /* 1E5B80 151B86D0 A3A00030 */  sb         $zero, 0x30($sp)
    /* 1E5B84 151B86D4 27A40018 */  addiu      $a0, $sp, 0x18
    /* 1E5B88 151B86D8 00002825 */  or         $a1, $zero, $zero
    /* 1E5B8C 151B86DC 0D44D242 */  jal        func_15134908
    /* 1E5B90 151B86E0 E7A40024 */   swc1      $f4, 0x24($sp)
    /* 1E5B94 151B86E4 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 1E5B98 151B86E8 27BD0038 */  addiu      $sp, $sp, 0x38
    /* 1E5B9C 151B86EC 03E00008 */  jr         $ra
    /* 1E5BA0 151B86F0 00000000 */   nop
endlabel func_151B8668
