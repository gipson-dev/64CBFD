glabel __osSetFpcCsr
    /* 22A50 10022A50 4442F800 */  cfc1       $v0, $31
    /* 22A54 10022A54 44C4F800 */  ctc1       $a0, $31
    /* 22A58 10022A58 03E00008 */  jr         $ra
    /* 22A5C 10022A5C 00000000 */   nop
