glabel func_150EEDA8
    /* 11C258 150EEDA8 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* 11C25C 150EEDAC AFBF0014 */  sw         $ra, 0x14($sp)
    /* 11C260 150EEDB0 908E0005 */  lbu        $t6, 0x5($a0)
    /* 11C264 150EEDB4 24010003 */  addiu      $at, $zero, 0x3
    /* 11C268 150EEDB8 2405000F */  addiu      $a1, $zero, 0xF
    /* 11C26C 150EEDBC 11C10009 */  beq        $t6, $at, .L150EEDE4
    /* 11C270 150EEDC0 3C06437A */   lui       $a2, (0x437A0000 >> 16)
    /* 11C274 150EEDC4 0D441178 */  jal        func_151045E0
    /* 11C278 150EEDC8 AFA40018 */   sw        $a0, 0x18($sp)
    /* 11C27C 150EEDCC 8FA40018 */  lw         $a0, 0x18($sp)
    /* 11C280 150EEDD0 240F0003 */  addiu      $t7, $zero, 0x3
    /* 11C284 150EEDD4 241800FF */  addiu      $t8, $zero, 0xFF
    /* 11C288 150EEDD8 A08F0005 */  sb         $t7, 0x5($a0)
    /* 11C28C 150EEDDC A48000E4 */  sh         $zero, 0xE4($a0)
    /* 11C290 150EEDE0 A0980125 */  sb         $t8, 0x125($a0)
  .L150EEDE4:
    /* 11C294 150EEDE4 0D414964 */  jal        func_15052590
    /* 11C298 150EEDE8 00000000 */   nop
    /* 11C29C 150EEDEC 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 11C2A0 150EEDF0 27BD0018 */  addiu      $sp, $sp, 0x18
    /* 11C2A4 150EEDF4 03E00008 */  jr         $ra
    /* 11C2A8 150EEDF8 00000000 */   nop
endlabel func_150EEDA8
    /* 11C2AC 150EEDFC 00000000 */  nop
