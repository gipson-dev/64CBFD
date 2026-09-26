glabel func_150C5EFC
    /* F33AC 150C5EFC 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* F33B0 150C5F00 AFBF0014 */  sw         $ra, 0x14($sp)
    /* F33B4 150C5F04 8C8200B0 */  lw         $v0, 0xB0($a0)
    /* F33B8 150C5F08 00002825 */  or         $a1, $zero, $zero
    /* F33BC 150C5F0C 00003025 */  or         $a2, $zero, $zero
    /* F33C0 150C5F10 AC400058 */  sw         $zero, 0x58($v0)
    /* F33C4 150C5F14 8C8E0018 */  lw         $t6, 0x18($a0)
    /* F33C8 150C5F18 AC8000B0 */  sw         $zero, 0xB0($a0)
    /* F33CC 150C5F1C 24420058 */  addiu      $v0, $v0, 0x58
    /* F33D0 150C5F20 35CF0002 */  ori        $t7, $t6, 0x2
    /* F33D4 150C5F24 0D44FDB0 */  jal        func_1513F6C0
    /* F33D8 150C5F28 AC8F0018 */   sw        $t7, 0x18($a0)
    /* F33DC 150C5F2C 00001025 */  or         $v0, $zero, $zero
    /* F33E0 150C5F30 8FBF0014 */  lw         $ra, 0x14($sp)
    /* F33E4 150C5F34 27BD0018 */  addiu      $sp, $sp, 0x18
    /* F33E8 150C5F38 03E00008 */  jr         $ra
    /* F33EC 150C5F3C 00000000 */   nop
endlabel func_150C5EFC
