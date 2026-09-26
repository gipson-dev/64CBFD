/* Handwritten function */
glabel func_10001420
    /* 1420 10001420 3C0E8004 */  lui        $t6, %hi(D_80043B40)
    /* 1424 10001424 25C53B40 */  addiu      $a1, $t6, %lo(D_80043B40)
    /* 1428 10001428 24A40FE0 */  addiu      $a0, $a1, 0xFE0
  .L1000142C:
    /* 142C 1000142C 24A50004 */  addiu      $a1, $a1, 0x4
    /* 1430 10001430 00A4082B */  sltu       $at, $a1, $a0
    /* 1434 10001434 1420FFFD */  bnez       $at, .L1000142C
    /* 1438 10001438 ACA0FFFC */   sw        $zero, -0x4($a1)
    /* 143C 1000143C 03E00008 */  jr         $ra
    /* 1440 10001440 00000000 */   nop
endlabel func_10001420
