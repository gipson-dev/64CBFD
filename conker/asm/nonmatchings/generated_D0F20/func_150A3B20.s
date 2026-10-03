  glabel func_150A3B20
    /* D0FD0 150A3B20 97140006 */  lhu        $s4, 0x6($t8)
    /* D0FD4 150A3B24 87100008 */  lh         $s0, 0x8($t8)
    /* D0FD8 150A3B28 00906823 */  subu       $t5, $a0, $s0
    /* D0FDC 150A3B2C 1DA00002 */  bgtz       $t5, .L150A3B38
    /* D0FE0 150A3B30 8711000A */   lh        $s1, 0xA($t8)
    /* D0FE4 150A3B34 000D6823 */  negu       $t5, $t5
  .L150A3B38:
    /* D0FE8 150A3B38 028D082A */  slt        $at, $s4, $t5
    /* D0FEC 150A3B3C 1420000A */  bnez       $at, .L150A3B68
    /* D0FF0 150A3B40 00B17023 */   subu      $t6, $a1, $s1
    /* D0FF4 150A3B44 05C20001 */  bltzl      $t6, .L150A3B4C
    /* D0FF8 150A3B48 000E7023 */   negu      $t6, $t6
  .L150A3B4C:
    /* D0FFC 150A3B4C 028E082A */  slt        $at, $s4, $t6
    /* D1000 150A3B50 14200005 */  bnez       $at, .L150A3B68
    /* D1004 150A3B54 870D000C */   lh        $t5, 0xC($t8)
    /* D1008 150A3B58 11A0000A */  beqz       $t5, .L150A3B84
    /* D100C 150A3B5C 00000000 */   nop
    /* D1010 150A3B60 09428EC8 */  j          func_150A3B20
    /* D1014 150A3B64 030DC021 */   addu      $t8, $t8, $t5
  .L150A3B68:
    /* D1018 150A3B68 870D0004 */  lh         $t5, 0x4($t8)
    /* D101C 150A3B6C 15A00003 */  bnez       $t5, .L150A3B7C
    /* D1020 150A3B70 00000000 */   nop
    /* D1024 150A3B74 09428FD7 */  j          func_150A3F5C
    /* D1028 150A3B78 00000000 */   nop
  .L150A3B7C:
    /* D102C 150A3B7C 09428EC8 */  j          func_150A3B20
    /* D1030 150A3B80 030DC021 */   addu      $t8, $t8, $t5
  .L150A3B84:
    /* D1034 150A3B84 2718000E */  addiu      $t8, $t8, 0xE
endlabel func_150A3B20
