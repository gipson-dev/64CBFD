  glabel D_150A3B88
    /* D1038 150A3B88 930D0000 */  lbu        $t5, 0x0($t8)
    /* D103C 150A3B8C 11A000F3 */  beqz       $t5, func_150A3F5C
    /* D1040 150A3B90 31B0007F */   andi      $s0, $t5, 0x7F
    /* D1044 150A3B94 51B00005 */  beql       $t5, $s0, func_150A3BAC
    /* D1048 150A3B98 02038021 */   addu      $s0, $s0, $v1
    /* D104C 150A3B9C 93120001 */  lbu        $s2, 0x1($t8)
    /* D1050 150A3BA0 27180001 */  addiu      $t8, $t8, 0x1
    /* D1054 150A3BA4 00108200 */  sll        $s0, $s0, 8
    /* D1058 150A3BA8 02128025 */  or         $s0, $s0, $s2
endlabel D_150A3B88
