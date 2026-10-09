glabel func_151B2690
    /* 1DFB40 151B2690 27BDFF28 */  addiu      $sp, $sp, -0xD8
    /* 1DFB44 151B2694 AFB10030 */  sw         $s1, 0x30($sp)
    /* 1DFB48 151B2698 00808825 */  or         $s1, $a0, $zero
    /* 1DFB4C 151B269C AFBF0034 */  sw         $ra, 0x34($sp)
    /* 1DFB50 151B26A0 AFB0002C */  sw         $s0, 0x2C($sp)
    /* 1DFB54 151B26A4 8E300028 */  lw         $s0, 0x28($s1)
    /* 1DFB58 151B26A8 240E0001 */  addiu      $t6, $zero, 0x1
    /* 1DFB5C 151B26AC AFB10090 */  sw         $s1, 0x90($sp)
    /* 1DFB60 151B26B0 A3AE0094 */  sb         $t6, 0x94($sp)
    /* 1DFB64 151B26B4 AFB00068 */  sw         $s0, 0x68($sp)
    /* 1DFB68 151B26B8 920F003B */  lbu        $t7, 0x3B($s0)
    /* 1DFB6C 151B26BC 24180005 */  addiu      $t8, $zero, 0x5
    /* 1DFB70 151B26C0 3C08800B */  lui        $t0, %hi(D_800AA320)
    /* 1DFB74 151B26C4 A3B8006D */  sb         $t8, 0x6D($sp)
    /* 1DFB78 151B26C8 2508A320 */  addiu      $t0, $t0, %lo(D_800AA320)
    /* 1DFB7C 151B26CC A3AF006C */  sb         $t7, 0x6C($sp)
    /* 1DFB80 151B26D0 8D010000 */  lw         $at, 0x0($t0)
    /* 1DFB84 151B26D4 27B90070 */  addiu      $t9, $sp, 0x70
    /* 1DFB88 151B26D8 8D0B0004 */  lw         $t3, 0x4($t0)
    /* 1DFB8C 151B26DC AF210000 */  sw         $at, 0x0($t9)
    /* 1DFB90 151B26E0 8D010008 */  lw         $at, 0x8($t0)
    /* 1DFB94 151B26E4 AF2B0004 */  sw         $t3, 0x4($t9)
    /* 1DFB98 151B26E8 240D0002 */  addiu      $t5, $zero, 0x2
    /* 1DFB9C 151B26EC AF210008 */  sw         $at, 0x8($t9)
    /* 1DFBA0 151B26F0 AFB0007C */  sw         $s0, 0x7C($sp)
    /* 1DFBA4 151B26F4 920C003B */  lbu        $t4, 0x3B($s0)
    /* 1DFBA8 151B26F8 3C0F800B */  lui        $t7, %hi(D_800AA368)
    /* 1DFBAC 151B26FC A3AD0081 */  sb         $t5, 0x81($sp)
    /* 1DFBB0 151B2700 25EFA368 */  addiu      $t7, $t7, %lo(D_800AA368)
    /* 1DFBB4 151B2704 A3AC0080 */  sb         $t4, 0x80($sp)
    /* 1DFBB8 151B2708 8DE10000 */  lw         $at, 0x0($t7)
    /* 1DFBBC 151B270C 27AE0084 */  addiu      $t6, $sp, 0x84
    /* 1DFBC0 151B2710 8DE90004 */  lw         $t1, 0x4($t7)
    /* 1DFBC4 151B2714 ADC10000 */  sw         $at, 0x0($t6)
    /* 1DFBC8 151B2718 8DE10008 */  lw         $at, 0x8($t7)
    /* 1DFBCC 151B271C ADC90004 */  sw         $t1, 0x4($t6)
    /* 1DFBD0 151B2720 24190064 */  addiu      $t9, $zero, 0x64
    /* 1DFBD4 151B2724 ADC10008 */  sw         $at, 0x8($t6)
    /* 1DFBD8 151B2728 A3A000CC */  sb         $zero, 0xCC($sp)
    /* 1DFBDC 151B272C A3A00098 */  sb         $zero, 0x98($sp)
    /* 1DFBE0 151B2730 A7B9009A */  sh         $t9, 0x9A($sp)
    /* 1DFBE4 151B2734 C6040014 */  lwc1       $f4, 0x14($s0)
    /* 1DFBE8 151B2738 3C0140A0 */  lui        $at, (0x40A00000 >> 16)
    /* 1DFBEC 151B273C 24080001 */  addiu      $t0, $zero, 0x1
    /* 1DFBF0 151B2740 E7A4009C */  swc1       $f4, 0x9C($sp)
    /* 1DFBF4 151B2744 C6060018 */  lwc1       $f6, 0x18($s0)
    /* 1DFBF8 151B2748 44812000 */  mtc1       $at, $f4
    /* 1DFBFC 151B274C 3C014334 */  lui        $at, (0x43340000 >> 16)
    /* 1DFC00 151B2750 E7A600A0 */  swc1       $f6, 0xA0($sp)
    /* 1DFC04 151B2754 C608001C */  lwc1       $f8, 0x1C($s0)
    /* 1DFC08 151B2758 44813000 */  mtc1       $at, $f6
    /* 1DFC0C 151B275C 3C01800B */  lui        $at, %hi(D_800AA388)
    /* 1DFC10 151B2760 E7A800A4 */  swc1       $f8, 0xA4($sp)
    /* 1DFC14 151B2764 C60A0014 */  lwc1       $f10, 0x14($s0)
    /* 1DFC18 151B2768 C428A388 */  lwc1       $f8, %lo(D_800AA388)($at)
    /* 1DFC1C 151B276C 3C01800B */  lui        $at, %hi(D_800AA38C)
    /* 1DFC20 151B2770 E7AA00A8 */  swc1       $f10, 0xA8($sp)
    /* 1DFC24 151B2774 C6100018 */  lwc1       $f16, 0x18($s0)
    /* 1DFC28 151B2778 C42AA38C */  lwc1       $f10, %lo(D_800AA38C)($at)
    /* 1DFC2C 151B277C 240B0001 */  addiu      $t3, $zero, 0x1
    /* 1DFC30 151B2780 E7B000AC */  swc1       $f16, 0xAC($sp)
    /* 1DFC34 151B2784 C612001C */  lwc1       $f18, 0x1C($s0)
    /* 1DFC38 151B2788 240C0001 */  addiu      $t4, $zero, 0x1
    /* 1DFC3C 151B278C 240D0003 */  addiu      $t5, $zero, 0x3
    /* 1DFC40 151B2790 3C053AC4 */  lui        $a1, (0x3AC49BA6 >> 16)
    /* 1DFC44 151B2794 A3A800B4 */  sb         $t0, 0xB4($sp)
    /* 1DFC48 151B2798 A3AB00B5 */  sb         $t3, 0xB5($sp)
    /* 1DFC4C 151B279C A3AC00B6 */  sb         $t4, 0xB6($sp)
    /* 1DFC50 151B27A0 A3AD00BC */  sb         $t5, 0xBC($sp)
    /* 1DFC54 151B27A4 34A59BA6 */  ori        $a1, $a1, (0x3AC49BA6 & 0xFFFF)
    /* 1DFC58 151B27A8 AFB100D8 */  sw         $s1, 0xD8($sp)
    /* 1DFC5C 151B27AC AFA00010 */  sw         $zero, 0x10($sp)
    /* 1DFC60 151B27B0 27A40098 */  addiu      $a0, $sp, 0x98
    /* 1DFC64 151B27B4 24060030 */  addiu      $a2, $zero, 0x30
    /* 1DFC68 151B27B8 240700FF */  addiu      $a3, $zero, 0xFF
    /* 1DFC6C 151B27BC E7A400B8 */  swc1       $f4, 0xB8($sp)
    /* 1DFC70 151B27C0 E7A600C0 */  swc1       $f6, 0xC0($sp)
    /* 1DFC74 151B27C4 E7A800C4 */  swc1       $f8, 0xC4($sp)
    /* 1DFC78 151B27C8 E7AA00C8 */  swc1       $f10, 0xC8($sp)
    /* 1DFC7C 151B27CC 0D46CC2C */  jal        func_151B30B0
    /* 1DFC80 151B27D0 E7B200B0 */   swc1      $f18, 0xB0($sp)
    /* 1DFC84 151B27D4 8FB100D8 */  lw         $s1, 0xD8($sp)
    /* 1DFC88 151B27D8 24440150 */  addiu      $a0, $v0, 0x150
    /* 1DFC8C 151B27DC 27A50068 */  addiu      $a1, $sp, 0x68
    /* 1DFC90 151B27E0 26310028 */  addiu      $s1, $s1, 0x28
    /* 1DFC94 151B27E4 10400003 */  beqz       $v0, .L151B27F4
    /* 1DFC98 151B27E8 AE220014 */   sw        $v0, 0x14($s1)
    /* 1DFC9C 151B27EC 0C008BB0 */  jal        memcpy
    /* 1DFCA0 151B27F0 24060030 */   addiu     $a2, $zero, 0x30
  .L151B27F4:
    /* 1DFCA4 151B27F4 3C18800B */  lui        $t8, %hi(D_800AA32C)
    /* 1DFCA8 151B27F8 A3A00094 */  sb         $zero, 0x94($sp)
    /* 1DFCAC 151B27FC 2718A32C */  addiu      $t8, $t8, %lo(D_800AA32C)
    /* 1DFCB0 151B2800 8F010000 */  lw         $at, 0x0($t8)
    /* 1DFCB4 151B2804 27AA0070 */  addiu      $t2, $sp, 0x70
    /* 1DFCB8 151B2808 8F090004 */  lw         $t1, 0x4($t8)
    /* 1DFCBC 151B280C AD410000 */  sw         $at, 0x0($t2)
    /* 1DFCC0 151B2810 8F010008 */  lw         $at, 0x8($t8)
    /* 1DFCC4 151B2814 3C08800B */  lui        $t0, %hi(D_800AA374)
    /* 1DFCC8 151B2818 2508A374 */  addiu      $t0, $t0, %lo(D_800AA374)
    /* 1DFCCC 151B281C AD490004 */  sw         $t1, 0x4($t2)
    /* 1DFCD0 151B2820 AD410008 */  sw         $at, 0x8($t2)
    /* 1DFCD4 151B2824 8D010000 */  lw         $at, 0x0($t0)
    /* 1DFCD8 151B2828 27B90084 */  addiu      $t9, $sp, 0x84
    /* 1DFCDC 151B282C 8D0D0004 */  lw         $t5, 0x4($t0)
    /* 1DFCE0 151B2830 AF210000 */  sw         $at, 0x0($t9)
    /* 1DFCE4 151B2834 8D010008 */  lw         $at, 0x8($t0)
    /* 1DFCE8 151B2838 240F0001 */  addiu      $t7, $zero, 0x1
    /* 1DFCEC 151B283C 3C053AC4 */  lui        $a1, (0x3AC49BA6 >> 16)
    /* 1DFCF0 151B2840 AF2D0004 */  sw         $t5, 0x4($t9)
    /* 1DFCF4 151B2844 AF210008 */  sw         $at, 0x8($t9)
    /* 1DFCF8 151B2848 A3AF00B6 */  sb         $t7, 0xB6($sp)
    /* 1DFCFC 151B284C AFA00010 */  sw         $zero, 0x10($sp)
    /* 1DFD00 151B2850 34A59BA6 */  ori        $a1, $a1, (0x3AC49BA6 & 0xFFFF)
    /* 1DFD04 151B2854 27A40098 */  addiu      $a0, $sp, 0x98
    /* 1DFD08 151B2858 24060030 */  addiu      $a2, $zero, 0x30
    /* 1DFD0C 151B285C 0D46CC2C */  jal        func_151B30B0
    /* 1DFD10 151B2860 240700FF */   addiu     $a3, $zero, 0xFF
    /* 1DFD14 151B2864 10400005 */  beqz       $v0, .L151B287C
    /* 1DFD18 151B2868 AE220010 */   sw        $v0, 0x10($s1)
    /* 1DFD1C 151B286C 24440150 */  addiu      $a0, $v0, 0x150
    /* 1DFD20 151B2870 27A50068 */  addiu      $a1, $sp, 0x68
    /* 1DFD24 151B2874 0C008BB0 */  jal        memcpy
    /* 1DFD28 151B2878 24060030 */   addiu     $a2, $zero, 0x30
  .L151B287C:
    /* 1DFD2C 151B287C AFB00040 */  sw         $s0, 0x40($sp)
    /* 1DFD30 151B2880 920E003B */  lbu        $t6, 0x3B($s0)
    /* 1DFD34 151B2884 240A0002 */  addiu      $t2, $zero, 0x2
    /* 1DFD38 151B2888 3C09800B */  lui        $t1, %hi(D_800AA368)
    /* 1DFD3C 151B288C A3AA0045 */  sb         $t2, 0x45($sp)
    /* 1DFD40 151B2890 2529A368 */  addiu      $t1, $t1, %lo(D_800AA368)
    /* 1DFD44 151B2894 A3AE0044 */  sb         $t6, 0x44($sp)
    /* 1DFD48 151B2898 8D210000 */  lw         $at, 0x0($t1)
    /* 1DFD4C 151B289C 27B80048 */  addiu      $t8, $sp, 0x48
    /* 1DFD50 151B28A0 8D390004 */  lw         $t9, 0x4($t1)
    /* 1DFD54 151B28A4 AF010000 */  sw         $at, 0x0($t8)
    /* 1DFD58 151B28A8 8D210008 */  lw         $at, 0x8($t1)
    /* 1DFD5C 151B28AC 3C0D800B */  lui        $t5, %hi(D_800AA374)
    /* 1DFD60 151B28B0 25ADA374 */  addiu      $t5, $t5, %lo(D_800AA374)
    /* 1DFD64 151B28B4 AF190004 */  sw         $t9, 0x4($t8)
    /* 1DFD68 151B28B8 AF010008 */  sw         $at, 0x8($t8)
    /* 1DFD6C 151B28BC 8DA10000 */  lw         $at, 0x0($t5)
    /* 1DFD70 151B28C0 27A80054 */  addiu      $t0, $sp, 0x54
    /* 1DFD74 151B28C4 8DAA0004 */  lw         $t2, 0x4($t5)
    /* 1DFD78 151B28C8 AD010000 */  sw         $at, 0x0($t0)
    /* 1DFD7C 151B28CC 8DA10008 */  lw         $at, 0x8($t5)
    /* 1DFD80 151B28D0 AD0A0004 */  sw         $t2, 0x4($t0)
    /* 1DFD84 151B28D4 24180028 */  addiu      $t8, $zero, 0x28
    /* 1DFD88 151B28D8 AD010008 */  sw         $at, 0x8($t0)
    /* 1DFD8C 151B28DC 3C0140A0 */  lui        $at, (0x40A00000 >> 16)
    /* 1DFD90 151B28E0 44818000 */  mtc1       $at, $f16
    /* 1DFD94 151B28E4 8FAB00D8 */  lw         $t3, 0xD8($sp)
    /* 1DFD98 151B28E8 24190001 */  addiu      $t9, $zero, 0x1
    /* 1DFD9C 151B28EC 240900FF */  addiu      $t1, $zero, 0xFF
    /* 1DFDA0 151B28F0 240C0013 */  addiu      $t4, $zero, 0x13
    /* 1DFDA4 151B28F4 AFAC0014 */  sw         $t4, 0x14($sp)
    /* 1DFDA8 151B28F8 AFA9001C */  sw         $t1, 0x1C($sp)
    /* 1DFDAC 151B28FC AFB90020 */  sw         $t9, 0x20($sp)
    /* 1DFDB0 151B2900 AFB80018 */  sw         $t8, 0x18($sp)
    /* 1DFDB4 151B2904 AFA00010 */  sw         $zero, 0x10($sp)
    /* 1DFDB8 151B2908 2404012C */  addiu      $a0, $zero, 0x12C
    /* 1DFDBC 151B290C 2405FFFF */  addiu      $a1, $zero, -0x1
    /* 1DFDC0 151B2910 2406FFFF */  addiu      $a2, $zero, -0x1
    /* 1DFDC4 151B2914 00003825 */  or         $a3, $zero, $zero
    /* 1DFDC8 151B2918 E7B00060 */  swc1       $f16, 0x60($sp)
    /* 1DFDCC 151B291C 0D45244C */  jal        func_15149130
    /* 1DFDD0 151B2920 AFAB0064 */   sw        $t3, 0x64($sp)
    /* 1DFDD4 151B2924 10400005 */  beqz       $v0, .L151B293C
    /* 1DFDD8 151B2928 AE22001C */   sw        $v0, 0x1C($s1)
    /* 1DFDDC 151B292C 24440028 */  addiu      $a0, $v0, 0x28
    /* 1DFDE0 151B2930 27A50040 */  addiu      $a1, $sp, 0x40
    /* 1DFDE4 151B2934 0C008BB0 */  jal        memcpy
    /* 1DFDE8 151B2938 24060028 */   addiu     $a2, $zero, 0x28
  .L151B293C:
    /* 1DFDEC 151B293C 8FBF0034 */  lw         $ra, 0x34($sp)
    /* 1DFDF0 151B2940 8FB0002C */  lw         $s0, 0x2C($sp)
    /* 1DFDF4 151B2944 8FB10030 */  lw         $s1, 0x30($sp)
    /* 1DFDF8 151B2948 03E00008 */  jr         $ra
    /* 1DFDFC 151B294C 27BD00D8 */   addiu     $sp, $sp, 0xD8
