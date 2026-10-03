  glabel func_150A66FC
    /* D3BAC 150A66FC 018D6021 */  addu       $t4, $t4, $t5
    /* D3BB0 150A6700 256B0001 */  addiu      $t3, $t3, 0x1
    /* D3BB4 150A6704 158EFFC8 */  bne        $t4, $t6, func_150A6568+0xC0
    /* D3BB8 150A6708 00000000 */   nop
    /* D3BBC 150A670C ACD00000 */  sw         $s0, 0x0($a2)
    /* D3BC0 150A6710 44100000 */  mfc1       $s0, $f0
    /* D3BC4 150A6714 00000000 */  nop
    /* D3BC8 150A6718 44110800 */  mfc1       $s1, $f1
    /* D3BCC 150A671C 00000000 */  nop
    /* D3BD0 150A6720 44121000 */  mfc1       $s2, $f2
    /* D3BD4 150A6724 00000000 */  nop
    /* D3BD8 150A6728 44131800 */  mfc1       $s3, $f3
    /* D3BDC 150A672C 00000000 */  nop
    /* D3BE0 150A6730 44142000 */  mfc1       $s4, $f4
    /* D3BE4 150A6734 00000000 */  nop
    /* D3BE8 150A6738 44152800 */  mfc1       $s5, $f5
    /* D3BEC 150A673C 00000000 */  nop
    /* D3BF0 150A6740 44163000 */  mfc1       $s6, $f6
    /* D3BF4 150A6744 00000000 */  nop
    /* D3BF8 150A6748 44173800 */  mfc1       $s7, $f7
    /* D3BFC 150A674C 00000000 */  nop
    /* D3C00 150A6750 441E4000 */  mfc1       $fp, $f8
    /* D3C04 150A6754 00000000 */  nop
    /* D3C08 150A6758 03E00008 */  jr         $ra
    /* D3C0C 150A675C 00000000 */   nop
endlabel func_150A66FC
