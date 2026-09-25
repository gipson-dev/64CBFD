glabel func_151C1FB8
    /* 1EF468 151C1FB8 27BDFFE0 */  addiu      $sp, $sp, -0x20
    /* 1EF46C 151C1FBC AFBF0014 */  sw         $ra, 0x14($sp)
    /* 1EF470 151C1FC0 8C8E0318 */  lw         $t6, 0x318($a0)
    /* 1EF474 151C1FC4 240F0001 */  addiu      $t7, $zero, 0x1
    /* 1EF478 151C1FC8 51C0001B */  beql       $t6, $zero, .L151C2038
    /* 1EF47C 151C1FCC 8FBF0014 */   lw        $ra, 0x14($sp)
    /* 1EF480 151C1FD0 A3AF0018 */  sb         $t7, 0x18($sp)
    /* 1EF484 151C1FD4 0D42B688 */  jal        func_150ADA20
    /* 1EF488 151C1FD8 AFA40020 */   sw        $a0, 0x20($sp)
    /* 1EF48C 151C1FDC 8FA40020 */  lw         $a0, 0x20($sp)
    /* 1EF490 151C1FE0 30580007 */  andi       $t8, $v0, 0x7
    /* 1EF494 151C1FE4 2719000D */  addiu      $t9, $t8, 0xD
    /* 1EF498 151C1FE8 A7B9001A */  sh         $t9, 0x1A($sp)
    /* 1EF49C 151C1FEC 8C880318 */  lw         $t0, 0x318($a0)
    /* 1EF4A0 151C1FF0 240A0001 */  addiu      $t2, $zero, 0x1
    /* 1EF4A4 151C1FF4 9109023D */  lbu        $t1, 0x23D($t0)
    /* 1EF4A8 151C1FF8 012A5804 */  sllv       $t3, $t2, $t1
    /* 1EF4AC 151C1FFC 0D42B688 */  jal        func_150ADA20
    /* 1EF4B0 151C2000 A3AB001D */   sb        $t3, 0x1D($sp)
    /* 1EF4B4 151C2004 24010003 */  addiu      $at, $zero, 0x3
    /* 1EF4B8 151C2008 0041001B */  divu       $zero, $v0, $at
    /* 1EF4BC 151C200C 00006010 */  mfhi       $t4
    /* 1EF4C0 151C2010 258D0006 */  addiu      $t5, $t4, 0x6
    /* 1EF4C4 151C2014 240EFFFF */  addiu      $t6, $zero, -0x1
    /* 1EF4C8 151C2018 A3AD001C */  sb         $t5, 0x1C($sp)
    /* 1EF4CC 151C201C A3AE001E */  sb         $t6, 0x1E($sp)
    /* 1EF4D0 151C2020 27A40018 */  addiu      $a0, $sp, 0x18
    /* 1EF4D4 151C2024 00002825 */  or         $a1, $zero, $zero
    /* 1EF4D8 151C2028 240600FF */  addiu      $a2, $zero, 0xFF
    /* 1EF4DC 151C202C 0D47621A */  jal        func_151D8868
    /* 1EF4E0 151C2030 24070001 */   addiu     $a3, $zero, 0x1
    /* 1EF4E4 151C2034 8FBF0014 */  lw         $ra, 0x14($sp)
  .L151C2038:
    /* 1EF4E8 151C2038 27BD0020 */  addiu      $sp, $sp, 0x20
    /* 1EF4EC 151C203C 03E00008 */  jr         $ra
    /* 1EF4F0 151C2040 00000000 */   nop
endlabel func_151C1FB8
    /* 1EF4F4 151C2044 00000000 */  nop
    /* 1EF4F8 151C2048 00000000 */  nop
    /* 1EF4FC 151C204C 00000000 */  nop
