glabel func_150AD8B0
    /* DAD60 150AD8B0 C4800000 */  lwc1       $f0, 0x0($a0)
    /* DAD64 150AD8B4 C4820004 */  lwc1       $f2, 0x4($a0)
    /* DAD68 150AD8B8 C4A40000 */  lwc1       $f4, 0x0($a1)
    /* DAD6C 150AD8BC C4A60004 */  lwc1       $f6, 0x4($a1)
    /* DAD70 150AD8C0 46041402 */  mul.s      $f16, $f2, $f4
    /* DAD74 150AD8C4 C4A80008 */  lwc1       $f8, 0x8($a1)
    /* DAD78 150AD8C8 46060482 */  mul.s      $f18, $f0, $f6
    /* DAD7C 150AD8CC C48A0008 */  lwc1       $f10, 0x8($a0)
    /* DAD80 150AD8D0 46081302 */  mul.s      $f12, $f2, $f8
    /* DAD84 150AD8D4 46109401 */  sub.s      $f16, $f18, $f16
    /* DAD88 150AD8D8 46065382 */  mul.s      $f14, $f10, $f6
    /* DAD8C 150AD8DC E4D00008 */  swc1       $f16, 0x8($a2)
    /* DAD90 150AD8E0 46045402 */  mul.s      $f16, $f10, $f4
    /* DAD94 150AD8E4 460E6301 */  sub.s      $f12, $f12, $f14
    /* DAD98 150AD8E8 46080482 */  mul.s      $f18, $f0, $f8
    /* DAD9C 150AD8EC E4CC0000 */  swc1       $f12, 0x0($a2)
    /* DADA0 150AD8F0 46128401 */  sub.s      $f16, $f16, $f18
    /* DADA4 150AD8F4 03E00008 */  jr         $ra
    /* DADA8 150AD8F8 E4D00004 */   swc1      $f16, 0x4($a2)
endlabel func_150AD8B0
