glabel func_1515FB70
    /* 18D020 1515FB70 908E003B */  lbu        $t6, 0x3B($a0)
    /* 18D024 1515FB74 24010001 */  addiu      $at, $zero, 0x1
    /* 18D028 1515FB78 15C10004 */  bne        $t6, $at, .L1515FB8C
    /* 18D02C 1515FB7C 00000000 */   nop
    /* 18D030 1515FB80 8CA2001C */  lw         $v0, 0x1C($a1)
    /* 18D034 1515FB84 04400001 */  bltz       $v0, .L1515FB8C
    /* 18D038 1515FB88 00000000 */   nop
  .L1515FB8C:
    /* 18D03C 1515FB8C 03E00008 */  jr         $ra
    /* 18D040 1515FB90 00000000 */   nop
endlabel func_1515FB70
