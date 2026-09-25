glabel func_150AD78C
    /* DAC3C 150AD78C 44086000 */  mfc1       $t0, $f12
    /* DAC40 150AD790 00084583 */  sra        $t0, $t0, 22
    /* DAC44 150AD794 310801FF */  andi       $t0, $t0, 0x1FF
    /* DAC48 150AD798 290100FF */  slti       $at, $t0, 0xFF
    /* DAC4C 150AD79C 10200018 */  beqz       $at, .L150AD800
    /* DAC50 150AD7A0 00000000 */   nop
    /* DAC54 150AD7A4 290100E6 */  slti       $at, $t0, 0xE6
    /* DAC58 150AD7A8 1420003C */  bnez       $at, func_150AD89C
    /* DAC5C 150AD7AC 46006006 */   mov.s     $f0, $f12
    /* DAC60 150AD7B0 460C6402 */  mul.s      $f16, $f12, $f12
    /* DAC64 150AD7B4 3C01800A */  lui        $at, %hi(D_8009F714)
    /* DAC68 150AD7B8 C432F714 */  lwc1       $f18, %lo(D_8009F714)($at)
    /* DAC6C 150AD7BC 46109482 */  mul.s      $f18, $f18, $f16
    /* DAC70 150AD7C0 3C01800A */  lui        $at, %hi(D_8009F718)
    /* DAC74 150AD7C4 C42AF718 */  lwc1       $f10, %lo(D_8009F718)($at)
    /* DAC78 150AD7C8 46125480 */  add.s      $f18, $f10, $f18
    /* DAC7C 150AD7CC 46109482 */  mul.s      $f18, $f18, $f16
    /* DAC80 150AD7D0 3C01800A */  lui        $at, %hi(D_8009F71C)
    /* DAC84 150AD7D4 C42AF71C */  lwc1       $f10, %lo(D_8009F71C)($at)
    /* DAC88 150AD7D8 46125480 */  add.s      $f18, $f10, $f18
    /* DAC8C 150AD7DC 46109482 */  mul.s      $f18, $f18, $f16
    /* DAC90 150AD7E0 3C01800A */  lui        $at, %hi(D_8009F720)
    /* DAC94 150AD7E4 C42AF720 */  lwc1       $f10, %lo(D_8009F720)($at)
    /* DAC98 150AD7E8 46125480 */  add.s      $f18, $f10, $f18
    /* DAC9C 150AD7EC 460C8282 */  mul.s      $f10, $f16, $f12
    /* DACA0 150AD7F0 00000000 */  nop
    /* DACA4 150AD7F4 460A9482 */  mul.s      $f18, $f18, $f10
    /* DACA8 150AD7F8 0942B627 */  j          func_150AD89C
    /* DACAC 150AD7FC 460C9000 */   add.s     $f0, $f18, $f12
  .L150AD800:
    /* DACB0 150AD800 29010136 */  slti       $at, $t0, 0x136
    /* DACB4 150AD804 50200025 */  beql       $at, $zero, func_150AD89C
    /* DACB8 150AD808 44800000 */   mtc1      $zero, $f0
    /* DACBC 150AD80C 3C01800A */  lui        $at, %hi(D_8009F724)
    /* DACC0 150AD810 C430F724 */  lwc1       $f16, %lo(D_8009F724)($at)
    /* DACC4 150AD814 460C8402 */  mul.s      $f16, $f16, $f12
    /* DACC8 150AD818 46008424 */  cvt.w.s    $f16, $f16
    /* DACCC 150AD81C 44098000 */  mfc1       $t1, $f16
    /* DACD0 150AD820 46808420 */  cvt.s.w    $f16, $f16
    /* DACD4 150AD824 3C01800A */  lui        $at, %hi(D_8009F728)
    /* DACD8 150AD828 C432F728 */  lwc1       $f18, %lo(D_8009F728)($at)
    /* DACDC 150AD82C 46109482 */  mul.s      $f18, $f18, $f16
    /* DACE0 150AD830 46126301 */  sub.s      $f12, $f12, $f18
    /* DACE4 150AD834 3C01800A */  lui        $at, %hi(D_8009F72C)
    /* DACE8 150AD838 C432F72C */  lwc1       $f18, %lo(D_8009F72C)($at)
    /* DACEC 150AD83C 46109482 */  mul.s      $f18, $f18, $f16
    /* DACF0 150AD840 46126301 */  sub.s      $f12, $f12, $f18
    /* DACF4 150AD844 460C6402 */  mul.s      $f16, $f12, $f12
    /* DACF8 150AD848 3C01800A */  lui        $at, %hi(D_8009F730)
    /* DACFC 150AD84C C432F730 */  lwc1       $f18, %lo(D_8009F730)($at)
    /* DAD00 150AD850 46109482 */  mul.s      $f18, $f18, $f16
    /* DAD04 150AD854 3C01800A */  lui        $at, %hi(D_8009F734)
    /* DAD08 150AD858 C42AF734 */  lwc1       $f10, %lo(D_8009F734)($at)
    /* DAD0C 150AD85C 46125480 */  add.s      $f18, $f10, $f18
    /* DAD10 150AD860 46109482 */  mul.s      $f18, $f18, $f16
    /* DAD14 150AD864 3C01800A */  lui        $at, %hi(D_8009F738)
    /* DAD18 150AD868 C42AF738 */  lwc1       $f10, %lo(D_8009F738)($at)
    /* DAD1C 150AD86C 46125480 */  add.s      $f18, $f10, $f18
    /* DAD20 150AD870 46109482 */  mul.s      $f18, $f18, $f16
    /* DAD24 150AD874 3C01800A */  lui        $at, %hi(D_8009F73C)
    /* DAD28 150AD878 C42AF73C */  lwc1       $f10, %lo(D_8009F73C)($at)
    /* DAD2C 150AD87C 46125480 */  add.s      $f18, $f10, $f18
    /* DAD30 150AD880 46109482 */  mul.s      $f18, $f18, $f16
    /* DAD34 150AD884 00000000 */  nop
    /* DAD38 150AD888 460C9482 */  mul.s      $f18, $f18, $f12
    /* DAD3C 150AD88C 460C9000 */  add.s      $f0, $f18, $f12
    /* DAD40 150AD890 31290001 */  andi       $t1, $t1, 0x1
    /* DAD44 150AD894 55200001 */  bnel       $t1, $zero, func_150AD89C
    /* DAD48 150AD898 46000007 */   neg.s     $f0, $f0
endlabel func_150AD78C
