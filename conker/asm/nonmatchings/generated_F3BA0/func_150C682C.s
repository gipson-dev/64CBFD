glabel func_150C682C
    /* F3CDC 150C682C 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* F3CE0 150C6830 AFBF0014 */  sw         $ra, 0x14($sp)
    /* F3CE4 150C6834 8C8200B0 */  lw         $v0, 0xB0($a0)
    /* F3CE8 150C6838 00002825 */  or         $a1, $zero, $zero
    /* F3CEC 150C683C 00003025 */  or         $a2, $zero, $zero
    /* F3CF0 150C6840 AC40006C */  sw         $zero, 0x6C($v0)
    /* F3CF4 150C6844 8C8E0018 */  lw         $t6, 0x18($a0)
    /* F3CF8 150C6848 AC8000B0 */  sw         $zero, 0xB0($a0)
    /* F3CFC 150C684C 24420058 */  addiu      $v0, $v0, 0x58
    /* F3D00 150C6850 35CF0002 */  ori        $t7, $t6, 0x2
    /* F3D04 150C6854 0D44FDB0 */  jal        func_1513F6C0
    /* F3D08 150C6858 AC8F0018 */   sw        $t7, 0x18($a0)
    /* F3D0C 150C685C 00001025 */  or         $v0, $zero, $zero
    /* F3D10 150C6860 8FBF0014 */  lw         $ra, 0x14($sp)
    /* F3D14 150C6864 27BD0018 */  addiu      $sp, $sp, 0x18
    /* F3D18 150C6868 03E00008 */  jr         $ra
    /* F3D1C 150C686C 00000000 */   nop
endlabel func_150C682C
