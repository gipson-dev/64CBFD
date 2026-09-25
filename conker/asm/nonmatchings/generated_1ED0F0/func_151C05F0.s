glabel func_151C05F0
    /* 1EDAA0 151C05F0 27BDFFD8 */  addiu      $sp, $sp, -0x28
    /* 1EDAA4 151C05F4 AFBF0024 */  sw         $ra, 0x24($sp)
    /* 1EDAA8 151C05F8 AFA5002C */  sw         $a1, 0x2C($sp)
    /* 1EDAAC 151C05FC AFA60030 */  sw         $a2, 0x30($sp)
    /* 1EDAB0 151C0600 93B8002F */  lbu        $t8, 0x2F($sp)
    /* 1EDAB4 151C0604 8FB90030 */  lw         $t9, 0x30($sp)
    /* 1EDAB8 151C0608 3C073A03 */  lui        $a3, (0x3A03126F >> 16)
    /* 1EDABC 151C060C 240E000F */  addiu      $t6, $zero, 0xF
    /* 1EDAC0 151C0610 240F0014 */  addiu      $t7, $zero, 0x14
    /* 1EDAC4 151C0614 AFAF0014 */  sw         $t7, 0x14($sp)
    /* 1EDAC8 151C0618 AFAE0010 */  sw         $t6, 0x10($sp)
    /* 1EDACC 151C061C 34E7126F */  ori        $a3, $a3, (0x3A03126F & 0xFFFF)
    /* 1EDAD0 151C0620 3C054448 */  lui        $a1, (0x44480000 >> 16)
    /* 1EDAD4 151C0624 3C0644FA */  lui        $a2, (0x44FA0000 >> 16)
    /* 1EDAD8 151C0628 AFB80018 */  sw         $t8, 0x18($sp)
    /* 1EDADC 151C062C 0D475501 */  jal        func_151D5404
    /* 1EDAE0 151C0630 AFB9001C */   sw        $t9, 0x1C($sp)
    /* 1EDAE4 151C0634 8FBF0024 */  lw         $ra, 0x24($sp)
    /* 1EDAE8 151C0638 27BD0028 */  addiu      $sp, $sp, 0x28
    /* 1EDAEC 151C063C 03E00008 */  jr         $ra
    /* 1EDAF0 151C0640 00000000 */   nop
endlabel func_151C05F0
