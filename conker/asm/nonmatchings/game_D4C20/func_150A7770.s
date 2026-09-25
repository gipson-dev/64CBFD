/* Handwritten function */
glabel func_150A7770
    /* D4C20 150A7770 A0850000 */  sb         $a1, 0x0($a0)
  .L150A7774:
    /* D4C24 150A7774 20C6FFFF */  addi       $a2, $a2, -0x1 /* handwritten instruction */
    /* D4C28 150A7778 20840001 */  addi       $a0, $a0, 0x1 /* handwritten instruction */
    /* D4C2C 150A777C 54C0FFFD */  bnel       $a2, $zero, .L150A7774
    /* D4C30 150A7780 A0850000 */   sb        $a1, 0x0($a0)
    /* D4C34 150A7784 03E00008 */  jr         $ra
    /* D4C38 150A7788 00000000 */   nop
endlabel func_150A7770
    /* D4C3C 150A778C 00000000 */  nop
