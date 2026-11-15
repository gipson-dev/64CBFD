/* Handwritten function */
glabel func_151F8870
    /* 225D20 151F8870 310C0007 */  andi       $t4, $t0, 0x7
    /* 225D24 151F8874 240B0008 */  addiu      $t3, $zero, 0x8
    /* 225D28 151F8878 908D0000 */  lbu        $t5, 0x0($a0)
    /* 225D2C 151F887C 908A0001 */  lbu        $t2, 0x1($a0)
    /* 225D30 151F8880 000D4A00 */  sll        $t1, $t5, 8
    /* 225D34 151F8884 012A4825 */  or         $t1, $t1, $t2
    /* 225D38 151F8888 016C5822 */  sub        $t3, $t3, $t4 /* handwritten instruction */
    /* 225D3C 151F888C 01694806 */  srlv       $t1, $t1, $t3
    /* 225D40 151F8890 312900FF */  andi       $t1, $t1, 0xFF
    /* 225D44 151F8894 00065A00 */  sll        $t3, $a2, 8
    /* 225D48 151F8898 01695820 */  add        $t3, $t3, $t1 /* handwritten instruction */
    /* 225D4C 151F889C 22AA2200 */  addi       $t2, $s5, 0x2200 /* handwritten instruction */
    /* 225D50 151F88A0 016A5020 */  add        $t2, $t3, $t2 /* handwritten instruction */
    /* 225D54 151F88A4 914A0000 */  lbu        $t2, 0x0($t2)
    /* 225D58 151F88A8 1140000A */  beqz       $t2, .L151F88D4
    /* 225D5C 151F88AC 00000000 */   nop
    /* 225D60 151F88B0 010A4020 */  add        $t0, $t0, $t2 /* handwritten instruction */
    /* 225D64 151F88B4 018A6020 */  add        $t4, $t4, $t2 /* handwritten instruction */
    /* 225D68 151F88B8 000C60C2 */  srl        $t4, $t4, 3
    /* 225D6C 151F88BC 008C2020 */  add        $a0, $a0, $t4 /* handwritten instruction */
    /* 225D70 151F88C0 01755020 */  add        $t2, $t3, $s5 /* handwritten instruction */
    /* 225D74 151F88C4 914A0000 */  lbu        $t2, 0x0($t2)
    /* 225D78 151F88C8 000A4902 */  srl        $t1, $t2, 4
    /* 225D7C 151F88CC 03E00008 */  jr         $ra
    /* 225D80 151F88D0 3142000F */   andi      $v0, $t2, 0xF
  .L151F88D4:
    /* 225D84 151F88D4 00107820 */  add        $t7, $zero, $s0 /* handwritten instruction */
    /* 225D88 151F88D8 31090007 */  andi       $t1, $t0, 0x7
    /* 225D8C 151F88DC 240A0080 */  addiu      $t2, $zero, 0x80
    /* 225D90 151F88E0 012A5006 */  srlv       $t2, $t2, $t1
    /* 225D94 151F88E4 240EFFFF */  addiu      $t6, $zero, -0x1
  .L151F88E8:
    /* 225D98 151F88E8 01AA6024 */  and        $t4, $t5, $t2
    /* 225D9C 151F88EC 51800002 */  beql       $t4, $zero, .L151F88F8
    /* 225DA0 151F88F0 91EC0000 */   lbu       $t4, 0x0($t7)
    /* 225DA4 151F88F4 91EC0001 */  lbu        $t4, 0x1($t7)
  .L151F88F8:
    /* 225DA8 151F88F8 000A5042 */  srl        $t2, $t2, 1
    /* 225DAC 151F88FC 000C6080 */  sll        $t4, $t4, 2
    /* 225DB0 151F8900 15400004 */  bnez       $t2, .L151F8914
    /* 225DB4 151F8904 01EC7820 */   add       $t7, $t7, $t4 /* handwritten instruction */
    /* 225DB8 151F8908 240A0080 */  addiu      $t2, $zero, 0x80
    /* 225DBC 151F890C 20840001 */  addi       $a0, $a0, 0x1 /* handwritten instruction */
    /* 225DC0 151F8910 908D0000 */  lbu        $t5, 0x0($a0)
  .L151F8914:
    /* 225DC4 151F8914 81E90002 */  lb         $t1, 0x2($t7)
    /* 225DC8 151F8918 112EFFF3 */  beq        $t1, $t6, .L151F88E8
    /* 225DCC 151F891C 21080001 */   addi      $t0, $t0, 0x1 /* handwritten instruction */
    /* 225DD0 151F8920 00091020 */  add        $v0, $zero, $t1 /* handwritten instruction */
    /* 225DD4 151F8924 03E00008 */  jr         $ra
    /* 225DD8 151F8928 81E90003 */   lb        $t1, 0x3($t7)
endlabel func_151F8870
