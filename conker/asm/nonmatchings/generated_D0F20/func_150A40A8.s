  glabel func_150A40A8
    /* D1558 150A40A8 0155082A */  slt        $at, $t2, $s5
    /* D155C 150A40AC 1020000F */  beqz       $at, .L150A40EC
    /* D1560 150A40B0 00000000 */   nop
    /* D1564 150A40B4 03CA082A */  slt        $at, $fp, $t2
    /* D1568 150A40B8 10200018 */  beqz       $at, func_150A411C
    /* D156C 150A40BC 00000000 */   nop
  .L150A40C0:
    /* D1570 150A40C0 02C06825 */  or         $t5, $s6, $zero
    /* D1574 150A40C4 03C07025 */  or         $t6, $fp, $zero
    /* D1578 150A40C8 02E07825 */  or         $t7, $s7, $zero
    /* D157C 150A40CC 0100B025 */  or         $s6, $t0, $zero
    /* D1580 150A40D0 0140F025 */  or         $fp, $t2, $zero
    /* D1584 150A40D4 0120B825 */  or         $s7, $t1, $zero
    /* D1588 150A40D8 01A04025 */  or         $t0, $t5, $zero
    /* D158C 150A40DC 01C05025 */  or         $t2, $t6, $zero
    /* D1590 150A40E0 01E04825 */  or         $t1, $t7, $zero
    /* D1594 150A40E4 09429047 */  j          func_150A411C
    /* D1598 150A40E8 00000000 */   nop
  .L150A40EC:
    /* D159C 150A40EC 02BE082A */  slt        $at, $s5, $fp
    /* D15A0 150A40F0 1020FFF3 */  beqz       $at, .L150A40C0
    /* D15A4 150A40F4 00000000 */   nop
    /* D15A8 150A40F8 01606825 */  or         $t5, $t3, $zero
    /* D15AC 150A40FC 02A07025 */  or         $t6, $s5, $zero
    /* D15B0 150A4100 01807825 */  or         $t7, $t4, $zero
    /* D15B4 150A4104 01005825 */  or         $t3, $t0, $zero
    /* D15B8 150A4108 0140A825 */  or         $s5, $t2, $zero
    /* D15BC 150A410C 01206025 */  or         $t4, $t1, $zero
    /* D15C0 150A4110 01A04025 */  or         $t0, $t5, $zero
    /* D15C4 150A4114 01C05025 */  or         $t2, $t6, $zero
    /* D15C8 150A4118 01E04825 */  or         $t1, $t7, $zero
endlabel func_150A40A8
