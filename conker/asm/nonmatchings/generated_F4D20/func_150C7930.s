glabel func_150C7930
    /* F4DE0 150C7930 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* F4DE4 150C7934 AFBF0014 */  sw         $ra, 0x14($sp)
    /* F4DE8 150C7938 3C02800E */  lui        $v0, %hi(D_800DBEF4)
    /* F4DEC 150C793C 8C42BEF4 */  lw         $v0, %lo(D_800DBEF4)($v0)
    /* F4DF0 150C7940 3C01FFFF */  lui        $at, (0xFFFF0000 >> 16)
    /* F4DF4 150C7944 8C4E021C */  lw         $t6, 0x21C($v0)
    /* F4DF8 150C7948 244201E0 */  addiu      $v0, $v0, 0x1E0
    /* F4DFC 150C794C 01C17824 */  and        $t7, $t6, $at
    /* F4E00 150C7950 0D44542F */  jal        func_151150BC
    /* F4E04 150C7954 AC8F003C */   sw        $t7, 0x3C($a0)
    /* F4E08 150C7958 8FBF0014 */  lw         $ra, 0x14($sp)
    /* F4E0C 150C795C 27BD0018 */  addiu      $sp, $sp, 0x18
    /* F4E10 150C7960 03E00008 */  jr         $ra
    /* F4E14 150C7964 00000000 */   nop
endlabel func_150C7930
