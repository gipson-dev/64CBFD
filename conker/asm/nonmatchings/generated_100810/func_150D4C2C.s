glabel func_150D4C2C
    /* 1020DC 150D4C2C 27BDFFD8 */  addiu      $sp, $sp, -0x28
    /* 1020E0 150D4C30 AFBF001C */  sw         $ra, 0x1C($sp)
    /* 1020E4 150D4C34 AFB00018 */  sw         $s0, 0x18($sp)
    /* 1020E8 150D4C38 3C0E8009 */  lui        $t6, %hi(D_8008FD8C)
    /* 1020EC 150D4C3C 81CEFD8C */  lb         $t6, %lo(D_8008FD8C)($t6)
    /* 1020F0 150D4C40 8C900098 */  lw         $s0, 0x98($a0)
    /* 1020F4 150D4C44 3C04150D */  lui        $a0, %hi(func_150D5124)
    /* 1020F8 150D4C48 29C10005 */  slti       $at, $t6, 0x5
    /* 1020FC 150D4C4C 10200004 */  beqz       $at, .L150D4C60
    /* 102100 150D4C50 24845124 */   addiu     $a0, $a0, %lo(func_150D5124)
    /* 102104 150D4C54 02002825 */  or         $a1, $s0, $zero
    /* 102108 150D4C58 0C003F4E */  jal        func_1000FD38
    /* 10210C 150D4C5C 240605B3 */   addiu     $a2, $zero, 0x5B3
  .L150D4C60:
    /* 102110 150D4C60 3C04150D */  lui        $a0, %hi(func_150D5124)
    /* 102114 150D4C64 24845124 */  addiu      $a0, $a0, %lo(func_150D5124)
    /* 102118 150D4C68 AFA40020 */  sw         $a0, 0x20($sp)
    /* 10211C 150D4C6C 02002825 */  or         $a1, $s0, $zero
    /* 102120 150D4C70 0C003F4E */  jal        func_1000FD38
    /* 102124 150D4C74 240605B4 */   addiu     $a2, $zero, 0x5B4
    /* 102128 150D4C78 8FA40020 */  lw         $a0, 0x20($sp)
    /* 10212C 150D4C7C 02002825 */  or         $a1, $s0, $zero
    /* 102130 150D4C80 0C003F4E */  jal        func_1000FD38
    /* 102134 150D4C84 240605BC */   addiu     $a2, $zero, 0x5BC
    /* 102138 150D4C88 8E04000C */  lw         $a0, 0xC($s0)
    /* 10213C 150D4C8C 50800004 */  beql       $a0, $zero, .L150D4CA0
    /* 102140 150D4C90 8E040010 */   lw        $a0, 0x10($s0)
    /* 102144 150D4C94 0D45A5CB */  jal        func_1516972C
    /* 102148 150D4C98 00000000 */   nop
    /* 10214C 150D4C9C 8E040010 */  lw         $a0, 0x10($s0)
  .L150D4CA0:
    /* 102150 150D4CA0 50800004 */  beql       $a0, $zero, .L150D4CB4
    /* 102154 150D4CA4 8FBF001C */   lw        $ra, 0x1C($sp)
    /* 102158 150D4CA8 0D45A5CB */  jal        func_1516972C
    /* 10215C 150D4CAC 00000000 */   nop
    /* 102160 150D4CB0 8FBF001C */  lw         $ra, 0x1C($sp)
  .L150D4CB4:
    /* 102164 150D4CB4 8FB00018 */  lw         $s0, 0x18($sp)
    /* 102168 150D4CB8 27BD0028 */  addiu      $sp, $sp, 0x28
    /* 10216C 150D4CBC 03E00008 */  jr         $ra
    /* 102170 150D4CC0 00000000 */   nop
endlabel func_150D4C2C
