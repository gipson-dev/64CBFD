/* Handwritten function */
glabel osWritebackDCacheAll
    /* 24F10 10024F10 3C088000 */  lui        $t0, 0x8000
    /* 24F14 10024F14 240A2000 */  addiu      $t2, $zero, 0x2000
    /* 24F18 10024F18 010A4821 */  addu       $t1, $t0, $t2
    /* 24F1C 10024F1C 2529FFF0 */  addiu      $t1, $t1, -0x10
  .L10024F20:
    /* 24F20 10024F20 BD010000 */  cache      0x01, 0x0($t0) /* handwritten instruction */
    /* 24F24 10024F24 0109082B */  sltu       $at, $t0, $t1
    /* 24F28 10024F28 1420FFFD */  bnez       $at, .L10024F20
    /* 24F2C 10024F2C 25080010 */   addiu     $t0, $t0, 0x10
    /* 24F30 10024F30 03E00008 */  jr         $ra
    /* 24F34 10024F34 00000000 */   nop
endlabel osWritebackDCacheAll
    /* 24F38 10024F38 00000000 */  nop
    /* 24F3C 10024F3C 00000000 */  nop
