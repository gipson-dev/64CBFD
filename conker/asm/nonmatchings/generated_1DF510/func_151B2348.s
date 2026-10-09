glabel func_151B2348
    /* 1DF7F8 151B2348 27BDFF58 */  addiu      $sp, $sp, -0xA8
    /* 1DF7FC 151B234C AFBF002C */  sw         $ra, 0x2C($sp)
    /* 1DF800 151B2350 AFB20028 */  sw         $s2, 0x28($sp)
    /* 1DF804 151B2354 AFB10024 */  sw         $s1, 0x24($sp)
    /* 1DF808 151B2358 AFB00020 */  sw         $s0, 0x20($sp)
    /* 1DF80C 151B235C AFA400A8 */  sw         $a0, 0xA8($sp)
    /* 1DF810 151B2360 8FAE00A8 */  lw         $t6, 0xA8($sp)
    /* 1DF814 151B2364 240F0002 */  addiu      $t7, $zero, 0x2
    /* 1DF818 151B2368 24190005 */  addiu      $t9, $zero, 0x5
    /* 1DF81C 151B236C 8DD00030 */  lw         $s0, 0x30($t6)
    /* 1DF820 151B2370 8DD10028 */  lw         $s1, 0x28($t6)
    /* 1DF824 151B2374 A3AF0060 */  sb         $t7, 0x60($sp)
    /* 1DF828 151B2378 AFAE005C */  sw         $t6, 0x5C($sp)
    /* 1DF82C 151B237C AFB00034 */  sw         $s0, 0x34($sp)
    /* 1DF830 151B2380 9218003B */  lbu        $t8, 0x3B($s0)
    /* 1DF834 151B2384 3C09800B */  lui        $t1, %hi(D_800AA350)
    /* 1DF838 151B2388 A3B90039 */  sb         $t9, 0x39($sp)
    /* 1DF83C 151B238C 2529A350 */  addiu      $t1, $t1, %lo(D_800AA350)
    /* 1DF840 151B2390 A3B80038 */  sb         $t8, 0x38($sp)
    /* 1DF844 151B2394 8D210000 */  lw         $at, 0x0($t1)
    /* 1DF848 151B2398 27A8003C */  addiu      $t0, $sp, 0x3C
    /* 1DF84C 151B239C 8D2C0004 */  lw         $t4, 0x4($t1)
    /* 1DF850 151B23A0 AD010000 */  sw         $at, 0x0($t0)
    /* 1DF854 151B23A4 8D210008 */  lw         $at, 0x8($t1)
    /* 1DF858 151B23A8 AD0C0004 */  sw         $t4, 0x4($t0)
    /* 1DF85C 151B23AC 240E000A */  addiu      $t6, $zero, 0xA
    /* 1DF860 151B23B0 AD010008 */  sw         $at, 0x8($t0)
    /* 1DF864 151B23B4 AFB00048 */  sw         $s0, 0x48($sp)
    /* 1DF868 151B23B8 920D003B */  lbu        $t5, 0x3B($s0)
    /* 1DF86C 151B23BC 3C18800B */  lui        $t8, %hi(D_800AA35C)
    /* 1DF870 151B23C0 A3AE004D */  sb         $t6, 0x4D($sp)
    /* 1DF874 151B23C4 2718A35C */  addiu      $t8, $t8, %lo(D_800AA35C)
    /* 1DF878 151B23C8 A3AD004C */  sb         $t5, 0x4C($sp)
    /* 1DF87C 151B23CC 8F010000 */  lw         $at, 0x0($t8)
    /* 1DF880 151B23D0 27AF0050 */  addiu      $t7, $sp, 0x50
    /* 1DF884 151B23D4 8F0A0004 */  lw         $t2, 0x4($t8)
    /* 1DF888 151B23D8 ADE10000 */  sw         $at, 0x0($t7)
    /* 1DF88C 151B23DC 8F010008 */  lw         $at, 0x8($t8)
    /* 1DF890 151B23E0 ADEA0004 */  sw         $t2, 0x4($t7)
    /* 1DF894 151B23E4 240803E8 */  addiu      $t0, $zero, 0x3E8
    /* 1DF898 151B23E8 ADE10008 */  sw         $at, 0x8($t7)
    /* 1DF89C 151B23EC A3A00098 */  sb         $zero, 0x98($sp)
    /* 1DF8A0 151B23F0 A3A00064 */  sb         $zero, 0x64($sp)
    /* 1DF8A4 151B23F4 A7A80066 */  sh         $t0, 0x66($sp)
    /* 1DF8A8 151B23F8 C6040014 */  lwc1       $f4, 0x14($s0)
    /* 1DF8AC 151B23FC 3C0140A0 */  lui        $at, (0x40A00000 >> 16)
    /* 1DF8B0 151B2400 24090001 */  addiu      $t1, $zero, 0x1
    /* 1DF8B4 151B2404 E7A40068 */  swc1       $f4, 0x68($sp)
    /* 1DF8B8 151B2408 C6060018 */  lwc1       $f6, 0x18($s0)
    /* 1DF8BC 151B240C 44812000 */  mtc1       $at, $f4
    /* 1DF8C0 151B2410 3C0142A0 */  lui        $at, (0x42A00000 >> 16)
    /* 1DF8C4 151B2414 E7A6006C */  swc1       $f6, 0x6C($sp)
    /* 1DF8C8 151B2418 C608001C */  lwc1       $f8, 0x1C($s0)
    /* 1DF8CC 151B241C 44813000 */  mtc1       $at, $f6
    /* 1DF8D0 151B2420 3C01800B */  lui        $at, %hi(D_800AA380)
    /* 1DF8D4 151B2424 E7A80070 */  swc1       $f8, 0x70($sp)
    /* 1DF8D8 151B2428 C60A0014 */  lwc1       $f10, 0x14($s0)
    /* 1DF8DC 151B242C C428A380 */  lwc1       $f8, %lo(D_800AA380)($at)
    /* 1DF8E0 151B2430 3C01800B */  lui        $at, %hi(D_800AA384)
    /* 1DF8E4 151B2434 E7AA0074 */  swc1       $f10, 0x74($sp)
    /* 1DF8E8 151B2438 C6100018 */  lwc1       $f16, 0x18($s0)
    /* 1DF8EC 151B243C C42AA384 */  lwc1       $f10, %lo(D_800AA384)($at)
    /* 1DF8F0 151B2440 240C0001 */  addiu      $t4, $zero, 0x1
    /* 1DF8F4 151B2444 E7B00078 */  swc1       $f16, 0x78($sp)
    /* 1DF8F8 151B2448 C612001C */  lwc1       $f18, 0x1C($s0)
    /* 1DF8FC 151B244C 240D0003 */  addiu      $t5, $zero, 0x3
    /* 1DF900 151B2450 3C053AC4 */  lui        $a1, (0x3AC49BA6 >> 16)
    /* 1DF904 151B2454 A3A90080 */  sb         $t1, 0x80($sp)
    /* 1DF908 151B2458 A3AC0081 */  sb         $t4, 0x81($sp)
    /* 1DF90C 151B245C A3A00082 */  sb         $zero, 0x82($sp)
    /* 1DF910 151B2460 A3AD0088 */  sb         $t5, 0x88($sp)
    /* 1DF914 151B2464 34A59BA6 */  ori        $a1, $a1, (0x3AC49BA6 & 0xFFFF)
    /* 1DF918 151B2468 AFA00010 */  sw         $zero, 0x10($sp)
    /* 1DF91C 151B246C 27A40064 */  addiu      $a0, $sp, 0x64
    /* 1DF920 151B2470 24060030 */  addiu      $a2, $zero, 0x30
    /* 1DF924 151B2474 240700FF */  addiu      $a3, $zero, 0xFF
    /* 1DF928 151B2478 E7A40084 */  swc1       $f4, 0x84($sp)
    /* 1DF92C 151B247C E7A6008C */  swc1       $f6, 0x8C($sp)
    /* 1DF930 151B2480 E7A80090 */  swc1       $f8, 0x90($sp)
    /* 1DF934 151B2484 E7AA0094 */  swc1       $f10, 0x94($sp)
    /* 1DF938 151B2488 0D46CC2C */  jal        func_151B30B0
    /* 1DF93C 151B248C E7B2007C */   swc1      $f18, 0x7C($sp)
    /* 1DF940 151B2490 8FB200A8 */  lw         $s2, 0xA8($sp)
    /* 1DF944 151B2494 24440150 */  addiu      $a0, $v0, 0x150
    /* 1DF948 151B2498 27A50034 */  addiu      $a1, $sp, 0x34
    /* 1DF94C 151B249C 26520028 */  addiu      $s2, $s2, 0x28
    /* 1DF950 151B24A0 10400003 */  beqz       $v0, .L151B24B0
    /* 1DF954 151B24A4 AE420018 */   sw        $v0, 0x18($s2)
    /* 1DF958 151B24A8 0C008BB0 */  jal        memcpy
    /* 1DF95C 151B24AC 24060030 */   addiu     $a2, $zero, 0x30
  .L151B24B0:
    /* 1DF960 151B24B0 240E0001 */  addiu      $t6, $zero, 0x1
    /* 1DF964 151B24B4 A3AE0060 */  sb         $t6, 0x60($sp)
    /* 1DF968 151B24B8 AFB10034 */  sw         $s1, 0x34($sp)
    /* 1DF96C 151B24BC 922B003B */  lbu        $t3, 0x3B($s1)
    /* 1DF970 151B24C0 24190005 */  addiu      $t9, $zero, 0x5
    /* 1DF974 151B24C4 3C18800B */  lui        $t8, %hi(D_800AA320)
    /* 1DF978 151B24C8 A3B90039 */  sb         $t9, 0x39($sp)
    /* 1DF97C 151B24CC 2718A320 */  addiu      $t8, $t8, %lo(D_800AA320)
    /* 1DF980 151B24D0 A3AB0038 */  sb         $t3, 0x38($sp)
    /* 1DF984 151B24D4 8F010000 */  lw         $at, 0x0($t8)
    /* 1DF988 151B24D8 27AF003C */  addiu      $t7, $sp, 0x3C
    /* 1DF98C 151B24DC 8F090004 */  lw         $t1, 0x4($t8)
    /* 1DF990 151B24E0 ADE10000 */  sw         $at, 0x0($t7)
    /* 1DF994 151B24E4 8F010008 */  lw         $at, 0x8($t8)
    /* 1DF998 151B24E8 ADE90004 */  sw         $t1, 0x4($t7)
    /* 1DF99C 151B24EC 240D0005 */  addiu      $t5, $zero, 0x5
    /* 1DF9A0 151B24F0 ADE10008 */  sw         $at, 0x8($t7)
    /* 1DF9A4 151B24F4 AFB00048 */  sw         $s0, 0x48($sp)
    /* 1DF9A8 151B24F8 920C003B */  lbu        $t4, 0x3B($s0)
    /* 1DF9AC 151B24FC 3C0B800B */  lui        $t3, %hi(D_800AA338)
    /* 1DF9B0 151B2500 A3AD004D */  sb         $t5, 0x4D($sp)
    /* 1DF9B4 151B2504 256BA338 */  addiu      $t3, $t3, %lo(D_800AA338)
    /* 1DF9B8 151B2508 A3AC004C */  sb         $t4, 0x4C($sp)
    /* 1DF9BC 151B250C 8D610000 */  lw         $at, 0x0($t3)
    /* 1DF9C0 151B2510 27AE0050 */  addiu      $t6, $sp, 0x50
    /* 1DF9C4 151B2514 8D6A0004 */  lw         $t2, 0x4($t3)
    /* 1DF9C8 151B2518 ADC10000 */  sw         $at, 0x0($t6)
    /* 1DF9CC 151B251C 8D610008 */  lw         $at, 0x8($t3)
    /* 1DF9D0 151B2520 ADCA0004 */  sw         $t2, 0x4($t6)
    /* 1DF9D4 151B2524 3C053AC4 */  lui        $a1, (0x3AC49BA6 >> 16)
    /* 1DF9D8 151B2528 ADC10008 */  sw         $at, 0x8($t6)
    /* 1DF9DC 151B252C C6300014 */  lwc1       $f16, 0x14($s1)
    /* 1DF9E0 151B2530 3C01432A */  lui        $at, (0x432A0000 >> 16)
    /* 1DF9E4 151B2534 34A59BA6 */  ori        $a1, $a1, (0x3AC49BA6 & 0xFFFF)
    /* 1DF9E8 151B2538 E7B00068 */  swc1       $f16, 0x68($sp)
    /* 1DF9EC 151B253C C6320018 */  lwc1       $f18, 0x18($s1)
    /* 1DF9F0 151B2540 44818000 */  mtc1       $at, $f16
    /* 1DF9F4 151B2544 27A40064 */  addiu      $a0, $sp, 0x64
    /* 1DF9F8 151B2548 E7B2006C */  swc1       $f18, 0x6C($sp)
    /* 1DF9FC 151B254C C624001C */  lwc1       $f4, 0x1C($s1)
    /* 1DFA00 151B2550 24060030 */  addiu      $a2, $zero, 0x30
    /* 1DFA04 151B2554 240700FF */  addiu      $a3, $zero, 0xFF
    /* 1DFA08 151B2558 E7A40070 */  swc1       $f4, 0x70($sp)
    /* 1DFA0C 151B255C C6060014 */  lwc1       $f6, 0x14($s0)
    /* 1DFA10 151B2560 E7A60074 */  swc1       $f6, 0x74($sp)
    /* 1DFA14 151B2564 C6080018 */  lwc1       $f8, 0x18($s0)
    /* 1DFA18 151B2568 E7A80078 */  swc1       $f8, 0x78($sp)
    /* 1DFA1C 151B256C C60A001C */  lwc1       $f10, 0x1C($s0)
    /* 1DFA20 151B2570 A3A00082 */  sb         $zero, 0x82($sp)
    /* 1DFA24 151B2574 AFA00010 */  sw         $zero, 0x10($sp)
    /* 1DFA28 151B2578 E7B0008C */  swc1       $f16, 0x8C($sp)
    /* 1DFA2C 151B257C 0D46CC2C */  jal        func_151B30B0
    /* 1DFA30 151B2580 E7AA007C */   swc1      $f10, 0x7C($sp)
    /* 1DFA34 151B2584 10400005 */  beqz       $v0, .L151B259C
    /* 1DFA38 151B2588 AE420014 */   sw        $v0, 0x14($s2)
    /* 1DFA3C 151B258C 24440150 */  addiu      $a0, $v0, 0x150
    /* 1DFA40 151B2590 27A50034 */  addiu      $a1, $sp, 0x34
    /* 1DFA44 151B2594 0C008BB0 */  jal        memcpy
    /* 1DFA48 151B2598 24060030 */   addiu     $a2, $zero, 0x30
  .L151B259C:
    /* 1DFA4C 151B259C A3A00060 */  sb         $zero, 0x60($sp)
    /* 1DFA50 151B25A0 AFB10034 */  sw         $s1, 0x34($sp)
    /* 1DFA54 151B25A4 922F003B */  lbu        $t7, 0x3B($s1)
    /* 1DFA58 151B25A8 24180005 */  addiu      $t8, $zero, 0x5
    /* 1DFA5C 151B25AC 3C0C800B */  lui        $t4, %hi(D_800AA32C)
    /* 1DFA60 151B25B0 A3B80039 */  sb         $t8, 0x39($sp)
    /* 1DFA64 151B25B4 258CA32C */  addiu      $t4, $t4, %lo(D_800AA32C)
    /* 1DFA68 151B25B8 A3AF0038 */  sb         $t7, 0x38($sp)
    /* 1DFA6C 151B25BC 8D810000 */  lw         $at, 0x0($t4)
    /* 1DFA70 151B25C0 27A9003C */  addiu      $t1, $sp, 0x3C
    /* 1DFA74 151B25C4 8D990004 */  lw         $t9, 0x4($t4)
    /* 1DFA78 151B25C8 AD210000 */  sw         $at, 0x0($t1)
    /* 1DFA7C 151B25CC 8D810008 */  lw         $at, 0x8($t4)
    /* 1DFA80 151B25D0 AD390004 */  sw         $t9, 0x4($t1)
    /* 1DFA84 151B25D4 240B000A */  addiu      $t3, $zero, 0xA
    /* 1DFA88 151B25D8 AD210008 */  sw         $at, 0x8($t1)
    /* 1DFA8C 151B25DC AFB00048 */  sw         $s0, 0x48($sp)
    /* 1DFA90 151B25E0 920E003B */  lbu        $t6, 0x3B($s0)
    /* 1DFA94 151B25E4 3C0F800B */  lui        $t7, %hi(D_800AA344)
    /* 1DFA98 151B25E8 A3AB004D */  sb         $t3, 0x4D($sp)
    /* 1DFA9C 151B25EC 25EFA344 */  addiu      $t7, $t7, %lo(D_800AA344)
    /* 1DFAA0 151B25F0 A3AE004C */  sb         $t6, 0x4C($sp)
    /* 1DFAA4 151B25F4 8DE10000 */  lw         $at, 0x0($t7)
    /* 1DFAA8 151B25F8 27AA0050 */  addiu      $t2, $sp, 0x50
    /* 1DFAAC 151B25FC 8DED0004 */  lw         $t5, 0x4($t7)
    /* 1DFAB0 151B2600 AD410000 */  sw         $at, 0x0($t2)
    /* 1DFAB4 151B2604 8DE10008 */  lw         $at, 0x8($t7)
    /* 1DFAB8 151B2608 AD4D0004 */  sw         $t5, 0x4($t2)
    /* 1DFABC 151B260C 3C053AC4 */  lui        $a1, (0x3AC49BA6 >> 16)
    /* 1DFAC0 151B2610 AD410008 */  sw         $at, 0x8($t2)
    /* 1DFAC4 151B2614 C6320014 */  lwc1       $f18, 0x14($s1)
    /* 1DFAC8 151B2618 34A59BA6 */  ori        $a1, $a1, (0x3AC49BA6 & 0xFFFF)
    /* 1DFACC 151B261C 27A40064 */  addiu      $a0, $sp, 0x64
    /* 1DFAD0 151B2620 E7B20068 */  swc1       $f18, 0x68($sp)
    /* 1DFAD4 151B2624 C6240018 */  lwc1       $f4, 0x18($s1)
    /* 1DFAD8 151B2628 24060030 */  addiu      $a2, $zero, 0x30
    /* 1DFADC 151B262C 240700FF */  addiu      $a3, $zero, 0xFF
    /* 1DFAE0 151B2630 E7A4006C */  swc1       $f4, 0x6C($sp)
    /* 1DFAE4 151B2634 C626001C */  lwc1       $f6, 0x1C($s1)
    /* 1DFAE8 151B2638 E7A60070 */  swc1       $f6, 0x70($sp)
    /* 1DFAEC 151B263C C6080014 */  lwc1       $f8, 0x14($s0)
    /* 1DFAF0 151B2640 E7A80074 */  swc1       $f8, 0x74($sp)
    /* 1DFAF4 151B2644 C60A0018 */  lwc1       $f10, 0x18($s0)
    /* 1DFAF8 151B2648 E7AA0078 */  swc1       $f10, 0x78($sp)
    /* 1DFAFC 151B264C C610001C */  lwc1       $f16, 0x1C($s0)
    /* 1DFB00 151B2650 A3A00082 */  sb         $zero, 0x82($sp)
    /* 1DFB04 151B2654 AFA00010 */  sw         $zero, 0x10($sp)
    /* 1DFB08 151B2658 0D46CC2C */  jal        func_151B30B0
    /* 1DFB0C 151B265C E7B0007C */   swc1      $f16, 0x7C($sp)
    /* 1DFB10 151B2660 10400005 */  beqz       $v0, .L151B2678
    /* 1DFB14 151B2664 AE420010 */   sw        $v0, 0x10($s2)
    /* 1DFB18 151B2668 24440150 */  addiu      $a0, $v0, 0x150
    /* 1DFB1C 151B266C 27A50034 */  addiu      $a1, $sp, 0x34
    /* 1DFB20 151B2670 0C008BB0 */  jal        memcpy
    /* 1DFB24 151B2674 24060030 */   addiu     $a2, $zero, 0x30
  .L151B2678:
    /* 1DFB28 151B2678 8FBF002C */  lw         $ra, 0x2C($sp)
    /* 1DFB2C 151B267C 8FB00020 */  lw         $s0, 0x20($sp)
    /* 1DFB30 151B2680 8FB10024 */  lw         $s1, 0x24($sp)
    /* 1DFB34 151B2684 8FB20028 */  lw         $s2, 0x28($sp)
    /* 1DFB38 151B2688 03E00008 */  jr         $ra
    /* 1DFB3C 151B268C 27BD00A8 */   addiu     $sp, $sp, 0xA8
