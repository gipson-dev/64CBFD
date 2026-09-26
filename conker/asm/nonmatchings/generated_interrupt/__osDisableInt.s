/* Handwritten function */
glabel __osDisableInt
    /* 22DC0 10022DC0 40086000 */  mfc0       $t0, $12
    /* 22DC4 10022DC4 2401FFFE */  addiu      $at, $zero, -0x2
    /* 22DC8 10022DC8 01014824 */  and        $t1, $t0, $at
    /* 22DCC 10022DCC 40896000 */  mtc0       $t1, $12
    /* 22DD0 10022DD0 31020001 */  andi       $v0, $t0, 0x1
    /* 22DD4 10022DD4 00000000 */  nop
    /* 22DD8 10022DD8 03E00008 */  jr         $ra
    /* 22DDC 10022DDC 00000000 */   nop
