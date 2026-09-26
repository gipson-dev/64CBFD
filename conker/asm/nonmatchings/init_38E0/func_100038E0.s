/* Handwritten function */
glabel func_100038E0
    /* 38E0 100038E0 3C02BC00 */  lui        $v0, (0xBC000C02 >> 16)
    /* 38E4 100038E4 34420C02 */  ori        $v0, $v0, (0xBC000C02 & 0xFFFF)
    /* 38E8 100038E8 3C018004 */  lui        $at, %hi(D_80038070)
    /* 38EC 100038EC AC228070 */  sw         $v0, %lo(D_80038070)($at)
    /* 38F0 100038F0 3C018004 */  lui        $at, %hi(D_80038074)
    /* 38F4 100038F4 240E4040 */  addiu      $t6, $zero, 0x4040
    /* 38F8 100038F8 A42E8074 */  sh         $t6, %lo(D_80038074)($at)
    /* 38FC 100038FC 240F4040 */  addiu      $t7, $zero, 0x4040
    /* 3900 10003900 A44F0000 */  sh         $t7, 0x0($v0)
    /* 3904 10003904 03E00008 */  jr         $ra
    /* 3908 10003908 00000000 */   nop
endlabel func_100038E0
