glabel func_151C05A4
    /* 1EDA54 151C05A4 27BDFFD8 */  addiu      $sp, $sp, -0x28
    /* 1EDA58 151C05A8 AFBF0024 */  sw         $ra, 0x24($sp)
    /* 1EDA5C 151C05AC AFA5002C */  sw         $a1, 0x2C($sp)
    /* 1EDA60 151C05B0 AFA60030 */  sw         $a2, 0x30($sp)
    /* 1EDA64 151C05B4 93AF002F */  lbu        $t7, 0x2F($sp)
    /* 1EDA68 151C05B8 8FB80030 */  lw         $t8, 0x30($sp)
    /* 1EDA6C 151C05BC 3C073A03 */  lui        $a3, (0x3A03126F >> 16)
    /* 1EDA70 151C05C0 240E0005 */  addiu      $t6, $zero, 0x5
    /* 1EDA74 151C05C4 AFAE0010 */  sw         $t6, 0x10($sp)
    /* 1EDA78 151C05C8 34E7126F */  ori        $a3, $a3, (0x3A03126F & 0xFFFF)
    /* 1EDA7C 151C05CC 3C054448 */  lui        $a1, (0x44480000 >> 16)
    /* 1EDA80 151C05D0 3C0644FA */  lui        $a2, (0x44FA0000 >> 16)
    /* 1EDA84 151C05D4 AFAF0014 */  sw         $t7, 0x14($sp)
    /* 1EDA88 151C05D8 0D4754CD */  jal        func_151D5334
    /* 1EDA8C 151C05DC AFB80018 */   sw        $t8, 0x18($sp)
    /* 1EDA90 151C05E0 8FBF0024 */  lw         $ra, 0x24($sp)
    /* 1EDA94 151C05E4 27BD0028 */  addiu      $sp, $sp, 0x28
    /* 1EDA98 151C05E8 03E00008 */  jr         $ra
    /* 1EDA9C 151C05EC 00000000 */   nop
endlabel func_151C05A4
