glabel func_151C1798
    /* 1EEC48 151C1798 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* 1EEC4C 151C179C AFBF0014 */  sw         $ra, 0x14($sp)
    /* 1EEC50 151C17A0 00803825 */  or         $a3, $a0, $zero
    /* 1EEC54 151C17A4 90E20004 */  lbu        $v0, 0x4($a3)
    /* 1EEC58 151C17A8 24010028 */  addiu      $at, $zero, 0x28
    /* 1EEC5C 151C17AC 3C0F800B */  lui        $t7, %hi(D_800AA958)
    /* 1EEC60 151C17B0 10410008 */  beq        $v0, $at, .L151C17D4
    /* 1EEC64 151C17B4 25EFA958 */   addiu     $t7, $t7, %lo(D_800AA958)
    /* 1EEC68 151C17B8 24010077 */  addiu      $at, $zero, 0x77
    /* 1EEC6C 151C17BC 10410003 */  beq        $v0, $at, .L151C17CC
    /* 1EEC70 151C17C0 00000000 */   nop
    /* 1EEC74 151C17C4 10000004 */  b          .L151C17D8
    /* 1EEC78 151C17C8 00001025 */   or        $v0, $zero, $zero
  .L151C17CC:
    /* 1EEC7C 151C17CC 10000002 */  b          .L151C17D8
    /* 1EEC80 151C17D0 24020001 */   addiu     $v0, $zero, 0x1
  .L151C17D4:
    /* 1EEC84 151C17D4 24020002 */  addiu      $v0, $zero, 0x2
  .L151C17D8:
    /* 1EEC88 151C17D8 3C18800B */  lui        $t8, %hi(D_800AA954)
    /* 1EEC8C 151C17DC 0302C021 */  addu       $t8, $t8, $v0
    /* 1EEC90 151C17E0 9318A954 */  lbu        $t8, %lo(D_800AA954)($t8)
    /* 1EEC94 151C17E4 00027080 */  sll        $t6, $v0, 2
    /* 1EEC98 151C17E8 8CE801D4 */  lw         $t0, 0x1D4($a3)
    /* 1EEC9C 151C17EC 01C27023 */  subu       $t6, $t6, $v0
    /* 1EECA0 151C17F0 000E7080 */  sll        $t6, $t6, 2
    /* 1EECA4 151C17F4 0018C980 */  sll        $t9, $t8, 6
    /* 1EECA8 151C17F8 01CF2021 */  addu       $a0, $t6, $t7
    /* 1EECAC 151C17FC 0D450C4D */  jal        func_15143134
    /* 1EECB0 151C1800 03283021 */   addu      $a2, $t9, $t0
    /* 1EECB4 151C1804 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 1EECB8 151C1808 27BD0018 */  addiu      $sp, $sp, 0x18
    /* 1EECBC 151C180C 03E00008 */  jr         $ra
    /* 1EECC0 151C1810 00000000 */   nop
endlabel func_151C1798
