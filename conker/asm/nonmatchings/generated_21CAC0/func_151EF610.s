glabel func_151EF610
    /* 21CAC0 151EF610 3C048009 */  lui        $a0, %hi(D_80091970)
    /* 21CAC4 151EF614 8C841970 */  lw         $a0, %lo(D_80091970)($a0)
    /* 21CAC8 151EF618 3C018009 */  lui        $at, %hi(D_80091970)
    /* 21CACC 151EF61C 00047080 */  sll        $t6, $a0, 2
    /* 21CAD0 151EF620 25CF0002 */  addiu      $t7, $t6, 2
    /* 21CAD4 151EF624 25D80003 */  addiu      $t8, $t6, 3
    /* 21CAD8 151EF628 01F80019 */  multu      $t7, $t8
    /* 21CADC 151EF62C 00002812 */  mflo       $a1
    /* 21CAE0 151EF630 00051082 */  srl        $v0, $a1, 2
    /* 21CAE4 151EF634 03E00008 */  jr         $ra
    /* 21CAE8 151EF638 AC221970 */   sw        $v0, %lo(D_80091970)($at)
endlabel func_151EF610
