glabel func_151C1570
    /* 1EEA20 151C1570 27BDFFD8 */  addiu      $sp, $sp, -0x28
    /* 1EEA24 151C1574 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 1EEA28 151C1578 AFA40028 */  sw         $a0, 0x28($sp)
    /* 1EEA2C 151C157C 8FAE0028 */  lw         $t6, 0x28($sp)
    /* 1EEA30 151C1580 8DCF01F0 */  lw         $t7, 0x1F0($t6)
    /* 1EEA34 151C1584 51E00004 */  beql       $t7, $zero, .L151C1598
    /* 1EEA38 151C1588 8FA50028 */   lw        $a1, 0x28($sp)
    /* 1EEA3C 151C158C 0D45A5CB */  jal        func_1516972C
    /* 1EEA40 151C1590 01E02025 */   or        $a0, $t7, $zero
    /* 1EEA44 151C1594 8FA50028 */  lw         $a1, 0x28($sp)
  .L151C1598:
    /* 1EEA48 151C1598 8CA401F4 */  lw         $a0, 0x1F4($a1)
    /* 1EEA4C 151C159C 24A50170 */  addiu      $a1, $a1, 0x170
    /* 1EEA50 151C15A0 50800005 */  beql       $a0, $zero, .L151C15B8
    /* 1EEA54 151C15A4 8CA30088 */   lw        $v1, 0x88($a1)
    /* 1EEA58 151C15A8 0D45A5CB */  jal        func_1516972C
    /* 1EEA5C 151C15AC AFA5001C */   sw        $a1, 0x1C($sp)
    /* 1EEA60 151C15B0 8FA5001C */  lw         $a1, 0x1C($sp)
    /* 1EEA64 151C15B4 8CA30088 */  lw         $v1, 0x88($a1)
  .L151C15B8:
    /* 1EEA68 151C15B8 10600002 */  beqz       $v1, .L151C15C4
    /* 1EEA6C 151C15BC 24620110 */   addiu     $v0, $v1, 0x110
    /* 1EEA70 151C15C0 AC400000 */  sw         $zero, 0x0($v0)
  .L151C15C4:
    /* 1EEA74 151C15C4 8CA4008C */  lw         $a0, 0x8C($a1)
    /* 1EEA78 151C15C8 10800003 */  beqz       $a0, .L151C15D8
    /* 1EEA7C 151C15CC 00000000 */   nop
    /* 1EEA80 151C15D0 0D45A5CB */  jal        func_1516972C
    /* 1EEA84 151C15D4 00000000 */   nop
  .L151C15D8:
    /* 1EEA88 151C15D8 3C04151C */  lui        $a0, %hi(func_151C110C)
    /* 1EEA8C 151C15DC 2484110C */  addiu      $a0, $a0, %lo(func_151C110C)
    /* 1EEA90 151C15E0 8FA50028 */  lw         $a1, 0x28($sp)
    /* 1EEA94 151C15E4 0C003F4E */  jal        func_1000FD38
    /* 1EEA98 151C15E8 00003025 */   or        $a2, $zero, $zero
    /* 1EEA9C 151C15EC 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 1EEAA0 151C15F0 27BD0028 */  addiu      $sp, $sp, 0x28
    /* 1EEAA4 151C15F4 03E00008 */  jr         $ra
    /* 1EEAA8 151C15F8 00000000 */   nop
endlabel func_151C1570
