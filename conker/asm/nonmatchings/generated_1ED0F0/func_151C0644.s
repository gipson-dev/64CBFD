glabel func_151C0644
    /* 1EDAF4 151C0644 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* 1EDAF8 151C0648 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 1EDAFC 151C064C AFA40018 */  sw         $a0, 0x18($sp)
    /* 1EDB00 151C0650 AFA5001C */  sw         $a1, 0x1C($sp)
    /* 1EDB04 151C0654 AFA60020 */  sw         $a2, 0x20($sp)
    /* 1EDB08 151C0658 0D42B688 */  jal        func_150ADA20
    /* 1EDB0C 151C065C 00000000 */   nop
    /* 1EDB10 151C0660 2401003E */  addiu      $at, $zero, 0x3E
    /* 1EDB14 151C0664 0041001B */  divu       $zero, $v0, $at
    /* 1EDB18 151C0668 00002810 */  mfhi       $a1
    /* 1EDB1C 151C066C 24A50078 */  addiu      $a1, $a1, 0x78
    /* 1EDB20 151C0670 00057400 */  sll        $t6, $a1, 16
    /* 1EDB24 151C0674 000E2C03 */  sra        $a1, $t6, 16
    /* 1EDB28 151C0678 8FA40018 */  lw         $a0, 0x18($sp)
    /* 1EDB2C 151C067C 93A6001F */  lbu        $a2, 0x1F($sp)
    /* 1EDB30 151C0680 0D43A0EB */  jal        func_150E83AC
    /* 1EDB34 151C0684 8FA70020 */   lw        $a3, 0x20($sp)
    /* 1EDB38 151C0688 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 1EDB3C 151C068C 27BD0018 */  addiu      $sp, $sp, 0x18
    /* 1EDB40 151C0690 03E00008 */  jr         $ra
    /* 1EDB44 151C0694 00000000 */   nop
endlabel func_151C0644
