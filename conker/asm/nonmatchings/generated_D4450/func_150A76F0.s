glabel func_150A76F0
    /* D4BA0 150A76F0 318C00FF */  andi       $t4, $t4, 0xFF
    /* D4BA4 150A76F4 29810041 */  slti       $at, $t4, 0x41
    /* D4BA8 150A76F8 14200015 */  bnez       $at, .L150A7750
    /* D4BAC 150A76FC 29810081 */   slti      $at, $t4, 0x81
    /* D4BB0 150A7700 1420000D */  bnez       $at, .L150A7738
    /* D4BB4 150A7704 298100C1 */   slti      $at, $t4, 0xC1
    /* D4BB8 150A7708 14200005 */  bnez       $at, .L150A7720
    /* D4BBC 150A770C 032C1822 */   sub       $v1, $t9, $t4 /* handwritten instruction */
    /* D4BC0 150A7710 00031880 */  sll        $v1, $v1, 2
    /* D4BC4 150A7714 00761820 */  add        $v1, $v1, $s6 /* handwritten instruction */
    /* D4BC8 150A7718 00400008 */  jr         $v0
    /* D4BCC 150A771C C4680000 */   lwc1      $f8, 0x0($v1)
  .L150A7720:
    /* D4BD0 150A7720 2183FF80 */  addi       $v1, $t4, -0x80 /* handwritten instruction */
    /* D4BD4 150A7724 00031880 */  sll        $v1, $v1, 2
    /* D4BD8 150A7728 00761820 */  add        $v1, $v1, $s6 /* handwritten instruction */
    /* D4BDC 150A772C C4680000 */  lwc1       $f8, 0x0($v1)
    /* D4BE0 150A7730 00400008 */  jr         $v0
    /* D4BE4 150A7734 46004207 */   neg.s     $f8, $f8
  .L150A7738:
    /* D4BE8 150A7738 02EC1822 */  sub        $v1, $s7, $t4 /* handwritten instruction */
    /* D4BEC 150A773C 00031880 */  sll        $v1, $v1, 2
    /* D4BF0 150A7740 00761820 */  add        $v1, $v1, $s6 /* handwritten instruction */
    /* D4BF4 150A7744 C4680000 */  lwc1       $f8, 0x0($v1)
    /* D4BF8 150A7748 00400008 */  jr         $v0
    /* D4BFC 150A774C 46004207 */   neg.s     $f8, $f8
  .L150A7750:
    /* D4C00 150A7750 000C1880 */  sll        $v1, $t4, 2
    /* D4C04 150A7754 00761820 */  add        $v1, $v1, $s6 /* handwritten instruction */
    /* D4C08 150A7758 8C630000 */  lw         $v1, 0x0($v1)
    /* D4C0C 150A775C 00400008 */  jr         $v0
    /* D4C10 150A7760 44834000 */   mtc1      $v1, $f8
endlabel func_150A76F0
