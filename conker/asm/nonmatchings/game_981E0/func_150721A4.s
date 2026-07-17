glabel func_150721A4
    /* 9F754 150721A4 27BDFFE0 */  addiu      $sp, $sp, -0x20
    /* 9F758 150721A8 AFBF001C */  sw         $ra, 0x1C($sp)
    /* 9F75C 150721AC 3C02800D */  lui        $v0, %hi(D_800D1580)
    /* 9F760 150721B0 8C431580 */  lw         $v1, %lo(D_800D1580)($v0)
    /* 9F764 150721B4 3C04800D */  lui        $a0, %hi(D_800D154C)
    /* 9F768 150721B8 8C84154C */  lw         $a0, %lo(D_800D154C)($a0)
    /* 9F76C 150721BC 00037203 */  sra        $t6, $v1, 0x8
    /* 9F770 150721C0 00037C03 */  sra        $t7, $v1, 0x10
    /* 9F774 150721C4 31E500FF */  andi       $a1, $t7, 0xFF
    /* 9F778 150721C8 31C700FF */  andi       $a3, $t6, 0xFF
    /* 9F77C 150721CC AFA00010 */  sw         $zero, 0x10($sp)
    /* 9F780 150721D0 0D418583 */  jal        func_1506160C
    /* 9F784 150721D4 306600FF */   andi      $a2, $v1, 0xFF
    /* 9F788 150721D8 8FBF001C */  lw         $ra, 0x1C($sp)
    /* 9F78C 150721DC 27BD0020 */  addiu      $sp, $sp, 0x20
    /* 9F790 150721E0 03E00008 */  jr         $ra
    /* 9F794 150721E4 00000000 */   nop
