/* Handwritten function */
glabel __osRestoreInt
    /* 22DE0 10022DE0 40086000 */  mfc0       $t0, $12
    /* 22DE4 10022DE4 01044025 */  or         $t0, $t0, $a0
    /* 22DE8 10022DE8 40886000 */  mtc0       $t0, $12
    /* 22DEC 10022DEC 00000000 */  nop
    /* 22DF0 10022DF0 00000000 */  nop
    /* 22DF4 10022DF4 03E00008 */  jr         $ra
    /* 22DF8 10022DF8 00000000 */   nop
    /* 22DFC 10022DFC 00000000 */  nop
