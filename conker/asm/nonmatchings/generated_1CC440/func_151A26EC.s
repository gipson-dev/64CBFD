glabel func_151A26EC
    /* 1CFB9C 151A26EC 27BDFF58 */  addiu      $sp, $sp, -0xA8
    /* 1CFBA0 151A26F0 44876000 */  mtc1       $a3, $f12
    /* 1CFBA4 151A26F4 87A700CA */  lh         $a3, 0xCA($sp)
    /* 1CFBA8 151A26F8 AFBF001C */  sw         $ra, 0x1C($sp)
    /* 1CFBAC 151A26FC 1CE00002 */  bgtz       $a3, .L151A2708
    /* 1CFBB0 151A2700 87A200CE */   lh        $v0, 0xCE($sp)
    /* 1CFBB4 151A2704 24070001 */  addiu      $a3, $zero, 0x1
  .L151A2708:
    /* 1CFBB8 151A2708 1C400002 */  bgtz       $v0, .L151A2714
    /* 1CFBBC 151A270C 240300FF */   addiu     $v1, $zero, 0xFF
    /* 1CFBC0 151A2710 24020001 */  addiu      $v0, $zero, 0x1
  .L151A2714:
    /* 1CFBC4 151A2714 0062001A */  div        $zero, $v1, $v0
    /* 1CFBC8 151A2718 00007012 */  mflo       $t6
    /* 1CFBCC 151A271C 87B800D2 */  lh         $t8, 0xD2($sp)
    /* 1CFBD0 151A2720 83B900D7 */  lb         $t9, 0xD7($sp)
    /* 1CFBD4 151A2724 0067001A */  div        $zero, $v1, $a3
    /* 1CFBD8 151A2728 24095203 */  addiu      $t1, $zero, 0x5203
    /* 1CFBDC 151A272C C7A000BC */  lwc1       $f0, 0xBC($sp)
    /* 1CFBE0 151A2730 A7AE00A2 */  sh         $t6, 0xA2($sp)
    /* 1CFBE4 151A2734 A7A90030 */  sh         $t1, 0x30($sp)
    /* 1CFBE8 151A2738 3C0A0020 */  lui        $t2, (0x200005 >> 16)
    /* 1CFBEC 151A273C 87AB00C2 */  lh         $t3, 0xC2($sp)
    /* 1CFBF0 151A2740 93AC00DB */  lbu        $t4, 0xDB($sp)
    /* 1CFBF4 151A2744 93AD00DF */  lbu        $t5, 0xDF($sp)
    /* 1CFBF8 151A2748 93AE00E3 */  lbu        $t6, 0xE3($sp)
    /* 1CFBFC 151A274C 93A900C7 */  lbu        $t1, 0xC7($sp)
    /* 1CFC00 151A2750 00007812 */  mflo       $t7
    /* 1CFC04 151A2754 24080027 */  addiu      $t0, $zero, 0x27
    /* 1CFC08 151A2758 354A0005 */  ori        $t2, $t2, (0x200005 & 0xFFFF)
    /* 1CFC0C 151A275C A7AF0048 */  sh         $t7, 0x48($sp)
    /* 1CFC10 151A2760 A3A80045 */  sb         $t0, 0x45($sp)
    /* 1CFC14 151A2764 AFAA0028 */  sw         $t2, 0x28($sp)
    /* 1CFC18 151A2768 A7B800A4 */  sh         $t8, 0xA4($sp)
    /* 1CFC1C 151A276C A3B900A6 */  sb         $t9, 0xA6($sp)
    /* 1CFC20 151A2770 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 1CFC24 151A2774 241800FF */  addiu      $t8, $zero, 0xFF
    /* 1CFC28 151A2778 241900FF */  addiu      $t9, $zero, 0xFF
    /* 1CFC2C 151A277C 240800FF */  addiu      $t0, $zero, 0xFF
    /* 1CFC30 151A2780 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 1CFC34 151A2784 E7AC009C */  swc1       $f12, 0x9C($sp)
    /* 1CFC38 151A2788 A7A200A0 */  sh         $v0, 0xA0($sp)
    /* 1CFC3C 151A278C 14400002 */  bnez       $v0, .L151A2798
    /* 1CFC40 151A2790 00000000 */   nop
    /* 1CFC44 151A2794 0007000D */  break      7
  .L151A2798:
    /* 1CFC48 151A2798 2401FFFF */  addiu      $at, $zero, -0x1
    /* 1CFC4C 151A279C 14410004 */  bne        $v0, $at, .L151A27B0
    /* 1CFC50 151A27A0 3C018000 */   lui       $at, (0x80000000 >> 16)
    /* 1CFC54 151A27A4 14610002 */  bne        $v1, $at, .L151A27B0
    /* 1CFC58 151A27A8 00000000 */   nop
    /* 1CFC5C 151A27AC 0006000D */  break      6
  .L151A27B0:
    /* 1CFC60 151A27B0 A7A70046 */  sh         $a3, 0x46($sp)
    /* 1CFC64 151A27B4 14E00002 */  bnez       $a3, .L151A27C0
    /* 1CFC68 151A27B8 00000000 */   nop
    /* 1CFC6C 151A27BC 0007000D */  break      7
  .L151A27C0:
    /* 1CFC70 151A27C0 2401FFFF */  addiu      $at, $zero, -0x1
    /* 1CFC74 151A27C4 14E10004 */  bne        $a3, $at, .L151A27D8
    /* 1CFC78 151A27C8 3C018000 */   lui       $at, (0x80000000 >> 16)
    /* 1CFC7C 151A27CC 14610002 */  bne        $v1, $at, .L151A27D8
    /* 1CFC80 151A27D0 00000000 */   nop
    /* 1CFC84 151A27D4 0006000D */  break      6
  .L151A27D8:
    /* 1CFC88 151A27D8 AFA0002C */  sw         $zero, 0x2C($sp)
    /* 1CFC8C 151A27DC AFA00034 */  sw         $zero, 0x34($sp)
    /* 1CFC90 151A27E0 AFA00038 */  sw         $zero, 0x38($sp)
    /* 1CFC94 151A27E4 A3AF003F */  sb         $t7, 0x3F($sp)
    /* 1CFC98 151A27E8 A3B80040 */  sb         $t8, 0x40($sp)
    /* 1CFC9C 151A27EC A3B90041 */  sb         $t9, 0x41($sp)
    /* 1CFCA0 151A27F0 A3A80042 */  sb         $t0, 0x42($sp)
    /* 1CFCA4 151A27F4 A3AA0044 */  sb         $t2, 0x44($sp)
    /* 1CFCA8 151A27F8 E7A00054 */  swc1       $f0, 0x54($sp)
    /* 1CFCAC 151A27FC E7A00050 */  swc1       $f0, 0x50($sp)
    /* 1CFCB0 151A2800 A7AB0032 */  sh         $t3, 0x32($sp)
    /* 1CFCB4 151A2804 A3AC003C */  sb         $t4, 0x3C($sp)
    /* 1CFCB8 151A2808 A3AD003D */  sb         $t5, 0x3D($sp)
    /* 1CFCBC 151A280C A3AE003E */  sb         $t6, 0x3E($sp)
    /* 1CFCC0 151A2810 A3A90043 */  sb         $t1, 0x43($sp)
    /* 1CFCC4 151A2814 8C810000 */  lw         $at, 0x0($a0)
    /* 1CFCC8 151A2818 27AB0058 */  addiu      $t3, $sp, 0x58
    /* 1CFCCC 151A281C 27AF0064 */  addiu      $t7, $sp, 0x64
    /* 1CFCD0 151A2820 AD610000 */  sw         $at, 0x0($t3)
    /* 1CFCD4 151A2824 8C8E0004 */  lw         $t6, 0x4($a0)
    /* 1CFCD8 151A2828 27A90070 */  addiu      $t1, $sp, 0x70
    /* 1CFCDC 151A282C AD6E0004 */  sw         $t6, 0x4($t3)
    /* 1CFCE0 151A2830 8C810008 */  lw         $at, 0x8($a0)
    /* 1CFCE4 151A2834 AD610008 */  sw         $at, 0x8($t3)
    /* 1CFCE8 151A2838 8CA10000 */  lw         $at, 0x0($a1)
    /* 1CFCEC 151A283C 240B0001 */  addiu      $t3, $zero, 0x1
    /* 1CFCF0 151A2840 ADE10000 */  sw         $at, 0x0($t7)
    /* 1CFCF4 151A2844 8CA80004 */  lw         $t0, 0x4($a1)
    /* 1CFCF8 151A2848 ADE80004 */  sw         $t0, 0x4($t7)
    /* 1CFCFC 151A284C 8CA10008 */  lw         $at, 0x8($a1)
    /* 1CFD00 151A2850 ADE10008 */  sw         $at, 0x8($t7)
    /* 1CFD04 151A2854 8CC10000 */  lw         $at, 0x0($a2)
    /* 1CFD08 151A2858 AD210000 */  sw         $at, 0x0($t1)
    /* 1CFD0C 151A285C 8CCC0004 */  lw         $t4, 0x4($a2)
    /* 1CFD10 151A2860 AD2C0004 */  sw         $t4, 0x4($t1)
    /* 1CFD14 151A2864 8CC10008 */  lw         $at, 0x8($a2)
    /* 1CFD18 151A2868 AD210008 */  sw         $at, 0x8($t1)
    /* 1CFD1C 151A286C 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 1CFD20 151A2870 C7A400B8 */  lwc1       $f4, 0xB8($sp)
    /* 1CFD24 151A2874 44813000 */  mtc1       $at, $f6
    /* 1CFD28 151A2878 A7AB004A */  sh         $t3, 0x4A($sp)
    /* 1CFD2C 151A287C E7A4007C */  swc1       $f4, 0x7C($sp)
    /* 1CFD30 151A2880 0D42B688 */  jal        func_150ADA20
    /* 1CFD34 151A2884 E7A6004C */   swc1      $f6, 0x4C($sp)
    /* 1CFD38 151A2888 304E0001 */  andi       $t6, $v0, 0x1
    /* 1CFD3C 151A288C 11C00003 */  beqz       $t6, .L151A289C
    /* 1CFD40 151A2890 00001825 */   or        $v1, $zero, $zero
    /* 1CFD44 151A2894 10000001 */  b          .L151A289C
    /* 1CFD48 151A2898 24030040 */   addiu     $v1, $zero, 0x40
  .L151A289C:
    /* 1CFD4C 151A289C 0D42B688 */  jal        func_150ADA20
    /* 1CFD50 151A28A0 AFA30020 */   sw        $v1, 0x20($sp)
    /* 1CFD54 151A28A4 30590001 */  andi       $t9, $v0, 0x1
    /* 1CFD58 151A28A8 13200003 */  beqz       $t9, .L151A28B8
    /* 1CFD5C 151A28AC 8FA30020 */   lw        $v1, 0x20($sp)
    /* 1CFD60 151A28B0 10000002 */  b          .L151A28BC
    /* 1CFD64 151A28B4 24020080 */   addiu     $v0, $zero, 0x80
  .L151A28B8:
    /* 1CFD68 151A28B8 00001025 */  or         $v0, $zero, $zero
  .L151A28BC:
    /* 1CFD6C 151A28BC 34580007 */  ori        $t8, $v0, 0x7
    /* 1CFD70 151A28C0 03035025 */  or         $t2, $t8, $v1
    /* 1CFD74 151A28C4 8FAD00E8 */  lw         $t5, 0xE8($sp)
    /* 1CFD78 151A28C8 3549D200 */  ori        $t1, $t2, 0xD200
    /* 1CFD7C 151A28CC 3C010080 */  lui        $at, (0x800000 >> 16)
    /* 1CFD80 151A28D0 01216025 */  or         $t4, $t1, $at
    /* 1CFD84 151A28D4 240B0007 */  addiu      $t3, $zero, 0x7
    /* 1CFD88 151A28D8 240E0002 */  addiu      $t6, $zero, 0x2
    /* 1CFD8C 151A28DC 24190011 */  addiu      $t9, $zero, 0x11
    /* 1CFD90 151A28E0 2418FFFF */  addiu      $t8, $zero, -0x1
    /* 1CFD94 151A28E4 240FFFFF */  addiu      $t7, $zero, -0x1
    /* 1CFD98 151A28E8 24080002 */  addiu      $t0, $zero, 0x2
    /* 1CFD9C 151A28EC AFAC0080 */  sw         $t4, 0x80($sp)
    /* 1CFDA0 151A28F0 A3AB0088 */  sb         $t3, 0x88($sp)
    /* 1CFDA4 151A28F4 A3AE0089 */  sb         $t6, 0x89($sp)
    /* 1CFDA8 151A28F8 A3B9008A */  sb         $t9, 0x8A($sp)
    /* 1CFDAC 151A28FC A3B8008B */  sb         $t8, 0x8B($sp)
    /* 1CFDB0 151A2900 A3AF008C */  sb         $t7, 0x8C($sp)
    /* 1CFDB4 151A2904 A3A8008D */  sb         $t0, 0x8D($sp)
    /* 1CFDB8 151A2908 27A40028 */  addiu      $a0, $sp, 0x28
    /* 1CFDBC 151A290C 24050001 */  addiu      $a1, $zero, 0x1
    /* 1CFDC0 151A2910 24060010 */  addiu      $a2, $zero, 0x10
    /* 1CFDC4 151A2914 93A700E7 */  lbu        $a3, 0xE7($sp)
    /* 1CFDC8 151A2918 0D44C0DD */  jal        func_15130374
    /* 1CFDCC 151A291C AFAD0010 */   sw        $t5, 0x10($sp)
    /* 1CFDD0 151A2920 1040000A */  beqz       $v0, .L151A294C
    /* 1CFDD4 151A2924 244400A8 */   addiu     $a0, $v0, 0xA8
    /* 1CFDD8 151A2928 27A5009C */  addiu      $a1, $sp, 0x9C
    /* 1CFDDC 151A292C 24060008 */  addiu      $a2, $zero, 0x8
    /* 1CFDE0 151A2930 0C008BB0 */  jal        memcpy
    /* 1CFDE4 151A2934 AFA20098 */   sw        $v0, 0x98($sp)
    /* 1CFDE8 151A2938 8FA30098 */  lw         $v1, 0x98($sp)
    /* 1CFDEC 151A293C 27A500A0 */  addiu      $a1, $sp, 0xA0
    /* 1CFDF0 151A2940 24060008 */  addiu      $a2, $zero, 0x8
    /* 1CFDF4 151A2944 0C008BB0 */  jal        memcpy
    /* 1CFDF8 151A2948 246400B0 */   addiu     $a0, $v1, 0xB0
  .L151A294C:
    /* 1CFDFC 151A294C 00001025 */  or         $v0, $zero, $zero
    /* 1CFE00 151A2950 8FBF001C */  lw         $ra, 0x1C($sp)
    /* 1CFE04 151A2954 27BD00A8 */  addiu      $sp, $sp, 0xA8
    /* 1CFE08 151A2958 03E00008 */  jr         $ra
    /* 1CFE0C 151A295C 00000000 */   nop
endlabel func_151A26EC
