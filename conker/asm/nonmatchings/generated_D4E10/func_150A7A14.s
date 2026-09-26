glabel func_150A7A14
    /* D4EC4 150A7A14 C486000C */  lwc1       $f6, 0xC($a0)
    /* D4EC8 150A7A18 C488001C */  lwc1       $f8, 0x1C($a0)
    /* D4ECC 150A7A1C 46003182 */  mul.s      $f6, $f6, $f0
    /* D4ED0 150A7A20 C48A002C */  lwc1       $f10, 0x2C($a0)
    /* D4ED4 150A7A24 46024202 */  mul.s      $f8, $f8, $f2
    /* D4ED8 150A7A28 C48C003C */  lwc1       $f12, 0x3C($a0)
    /* D4EDC 150A7A2C 46045282 */  mul.s      $f10, $f10, $f4
    /* D4EE0 150A7A30 46083180 */  add.s      $f6, $f6, $f8
    /* D4EE4 150A7A34 460C5280 */  add.s      $f10, $f10, $f12
    /* D4EE8 150A7A38 8FAA001C */  lw         $t2, 0x1C($sp)
    /* D4EEC 150A7A3C 460A3480 */  add.s      $f18, $f6, $f10
    /* D4EF0 150A7A40 03200008 */  jr         $t9
    /* D4EF4 150A7A44 E5520000 */   swc1      $f18, 0x0($t2)
endlabel func_150A7A14
