/* Handwritten function */
glabel func_151F892C
    /* 225DDC 151F892C 88890000 */  lwl        $t1, 0x0($a0)
    /* 225DE0 151F8930 98890003 */  lwr        $t1, 0x3($a0)
    /* 225DE4 151F8934 310A0007 */  andi       $t2, $t0, 0x7
    /* 225DE8 151F8938 01515020 */  add        $t2, $t2, $s1
    /* 225DEC 151F893C 000A50C2 */  srl        $t2, $t2, 3
    /* 225DF0 151F8940 008A2020 */  add        $a0, $a0, $t2
    /* 225DF4 151F8944 310A0007 */  andi       $t2, $t0, 0x7
    /* 225DF8 151F8948 01494804 */  sllv       $t1, $t1, $t2
    /* 225DFC 151F894C 240A0020 */  addiu      $t2, $zero, 0x20
    /* 225E00 151F8950 01515022 */  sub        $t2, $t2, $s1
    /* 225E04 151F8954 01491006 */  srlv       $v0, $t1, $t2
    /* 225E08 151F8958 03E00008 */  jr         $ra
    /* 225E0C 151F895C 01114020 */   add       $t0, $t0, $s1
endlabel func_151F892C
