glabel func_150D66A4
    /* 103B54 150D66A4 27BDFFD0 */  addiu      $sp, $sp, -0x30
    /* 103B58 150D66A8 AFBF0024 */  sw         $ra, 0x24($sp)
    /* 103B5C 150D66AC AFA40030 */  sw         $a0, 0x30($sp)
    /* 103B60 150D66B0 AFA50034 */  sw         $a1, 0x34($sp)
    /* 103B64 150D66B4 AFA60038 */  sw         $a2, 0x38($sp)
    /* 103B68 150D66B8 0D42B688 */  jal        func_150ADA20
    /* 103B6C 150D66BC 00000000 */   nop
    /* 103B70 150D66C0 0D42B688 */  jal        func_150ADA20
    /* 103B74 150D66C4 AFA20028 */   sw        $v0, 0x28($sp)
    /* 103B78 150D66C8 8FA70028 */  lw         $a3, 0x28($sp)
    /* 103B7C 150D66CC 24010038 */  addiu      $at, $zero, 0x38
    /* 103B80 150D66D0 93A80033 */  lbu        $t0, 0x33($sp)
    /* 103B84 150D66D4 00E1001B */  divu       $zero, $a3, $at
    /* 103B88 150D66D8 00007010 */  mfhi       $t6
    /* 103B8C 150D66DC 24010006 */  addiu      $at, $zero, 0x6
    /* 103B90 150D66E0 93A90037 */  lbu        $t1, 0x37($sp)
    /* 103B94 150D66E4 0041001B */  divu       $zero, $v0, $at
    /* 103B98 150D66E8 8FAA0038 */  lw         $t2, 0x38($sp)
    /* 103B9C 150D66EC 0000C010 */  mfhi       $t8
    /* 103BA0 150D66F0 25C700C8 */  addiu      $a3, $t6, 0xC8
    /* 103BA4 150D66F4 30EF00FF */  andi       $t7, $a3, 0xFF
    /* 103BA8 150D66F8 27190019 */  addiu      $t9, $t8, 0x19
    /* 103BAC 150D66FC AFB90010 */  sw         $t9, 0x10($sp)
    /* 103BB0 150D6700 01E03825 */  or         $a3, $t7, $zero
    /* 103BB4 150D6704 240400FF */  addiu      $a0, $zero, 0xFF
    /* 103BB8 150D6708 240500FF */  addiu      $a1, $zero, 0xFF
    /* 103BBC 150D670C 240600FF */  addiu      $a2, $zero, 0xFF
    /* 103BC0 150D6710 AFA80014 */  sw         $t0, 0x14($sp)
    /* 103BC4 150D6714 AFA90018 */  sw         $t1, 0x18($sp)
    /* 103BC8 150D6718 0D46099C */  jal        func_15182670
    /* 103BCC 150D671C AFAA001C */   sw        $t2, 0x1C($sp)
    /* 103BD0 150D6720 8FBF0024 */  lw         $ra, 0x24($sp)
    /* 103BD4 150D6724 27BD0030 */  addiu      $sp, $sp, 0x30
    /* 103BD8 150D6728 03E00008 */  jr         $ra
    /* 103BDC 150D672C 00000000 */   nop
endlabel func_150D66A4
