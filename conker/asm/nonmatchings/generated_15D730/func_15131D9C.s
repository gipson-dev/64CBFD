glabel func_15131D9C
    /* 15F24C 15131D9C 27BDFFD8 */  addiu      $sp, $sp, -0x28
    /* 15F250 15131DA0 AFB00020 */  sw         $s0, 0x20($sp)
    /* 15F254 15131DA4 00808025 */  or         $s0, $a0, $zero
    /* 15F258 15131DA8 AFBF0024 */  sw         $ra, 0x24($sp)
    /* 15F25C 15131DAC AFA5002C */  sw         $a1, 0x2C($sp)
    /* 15F260 15131DB0 8E0600AC */  lw         $a2, 0xAC($s0)
    /* 15F264 15131DB4 260E0038 */  addiu      $t6, $s0, 0x38
    /* 15F268 15131DB8 260F003C */  addiu      $t7, $s0, 0x3C
    /* 15F26C 15131DBC AFAF0014 */  sw         $t7, 0x14($sp)
    /* 15F270 15131DC0 AFAE0010 */  sw         $t6, 0x10($sp)
    /* 15F274 15131DC4 260400A8 */  addiu      $a0, $s0, 0xA8
    /* 15F278 15131DC8 260500AA */  addiu      $a1, $s0, 0xAA
    /* 15F27C 15131DCC 0D44C721 */  jal        func_15131C84
    /* 15F280 15131DD0 260700B0 */   addiu     $a3, $s0, 0xB0
    /* 15F284 15131DD4 24020001 */  addiu      $v0, $zero, 0x1
    /* 15F288 15131DD8 8FBF0024 */  lw         $ra, 0x24($sp)
    /* 15F28C 15131DDC 8FB00020 */  lw         $s0, 0x20($sp)
    /* 15F290 15131DE0 27BD0028 */  addiu      $sp, $sp, 0x28
    /* 15F294 15131DE4 03E00008 */  jr         $ra
    /* 15F298 15131DE8 00000000 */   nop
endlabel func_15131D9C
