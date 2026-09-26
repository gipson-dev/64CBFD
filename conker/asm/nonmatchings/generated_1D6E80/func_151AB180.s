glabel func_151AB180
    /* 1D8630 151AB180 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* 1D8634 151AB184 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 1D8638 151AB188 8C8200B0 */  lw         $v0, 0xB0($a0)
    /* 1D863C 151AB18C 00002825 */  or         $a1, $zero, $zero
    /* 1D8640 151AB190 00003025 */  or         $a2, $zero, $zero
    /* 1D8644 151AB194 AC400070 */  sw         $zero, 0x70($v0)
    /* 1D8648 151AB198 8C8E0018 */  lw         $t6, 0x18($a0)
    /* 1D864C 151AB19C AC8000B0 */  sw         $zero, 0xB0($a0)
    /* 1D8650 151AB1A0 24420058 */  addiu      $v0, $v0, 0x58
    /* 1D8654 151AB1A4 35CF0002 */  ori        $t7, $t6, 0x2
    /* 1D8658 151AB1A8 0D44FDB0 */  jal        func_1513F6C0
    /* 1D865C 151AB1AC AC8F0018 */   sw        $t7, 0x18($a0)
    /* 1D8660 151AB1B0 00001025 */  or         $v0, $zero, $zero
    /* 1D8664 151AB1B4 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 1D8668 151AB1B8 27BD0018 */  addiu      $sp, $sp, 0x18
    /* 1D866C 151AB1BC 03E00008 */  jr         $ra
    /* 1D8670 151AB1C0 00000000 */   nop
endlabel func_151AB180
