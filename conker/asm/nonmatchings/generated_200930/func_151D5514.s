glabel func_151D5514
    /* 2029C4 151D5514 27BDFF88 */  addiu      $sp, $sp, -0x78
    /* 2029C8 151D5518 AFA5007C */  sw         $a1, 0x7C($sp)
    /* 2029CC 151D551C 30AE00FF */  andi       $t6, $a1, 0xFF
    /* 2029D0 151D5520 01C02825 */  or         $a1, $t6, $zero
    /* 2029D4 151D5524 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 2029D8 151D5528 00803825 */  or         $a3, $a0, $zero
    /* 2029DC 151D552C 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 2029E0 151D5530 2418FFC0 */  addiu      $t8, $zero, -0x40
    /* 2029E4 151D5534 2419004A */  addiu      $t9, $zero, 0x4A
    /* 2029E8 151D5538 24080009 */  addiu      $t0, $zero, 0x9
    /* 2029EC 151D553C 24090003 */  addiu      $t1, $zero, 0x3
    /* 2029F0 151D5540 A7A0001C */  sh         $zero, 0x1C($sp)
    /* 2029F4 151D5544 A7AF001E */  sh         $t7, 0x1E($sp)
    /* 2029F8 151D5548 A7B80020 */  sh         $t8, 0x20($sp)
    /* 2029FC 151D554C A7B90022 */  sh         $t9, 0x22($sp)
    /* 202A00 151D5550 AFA80024 */  sw         $t0, 0x24($sp)
    /* 202A04 151D5554 AFA90028 */  sw         $t1, 0x28($sp)
    /* 202A08 151D5558 8CE10000 */  lw         $at, 0x0($a3)
    /* 202A0C 151D555C 27AA002C */  addiu      $t2, $sp, 0x2C
    /* 202A10 151D5560 240E0007 */  addiu      $t6, $zero, 0x7
    /* 202A14 151D5564 AD410000 */  sw         $at, 0x0($t2)
    /* 202A18 151D5568 8CED0004 */  lw         $t5, 0x4($a3)
    /* 202A1C 151D556C 240F0003 */  addiu      $t7, $zero, 0x3
    /* 202A20 151D5570 2418000F */  addiu      $t8, $zero, 0xF
    /* 202A24 151D5574 AD4D0004 */  sw         $t5, 0x4($t2)
    /* 202A28 151D5578 8CE10008 */  lw         $at, 0x8($a3)
    /* 202A2C 151D557C 2419000F */  addiu      $t9, $zero, 0xF
    /* 202A30 151D5580 24080064 */  addiu      $t0, $zero, 0x64
    /* 202A34 151D5584 AD410008 */  sw         $at, 0x8($t2)
    /* 202A38 151D5588 3C01800B */  lui        $at, %hi(D_800AB21C)
    /* 202A3C 151D558C C424B21C */  lwc1       $f4, %lo(D_800AB21C)($at)
    /* 202A40 151D5590 3C014356 */  lui        $at, (0x43560000 >> 16)
    /* 202A44 151D5594 44813000 */  mtc1       $at, $f6
    /* 202A48 151D5598 3C01434B */  lui        $at, (0x434B0000 >> 16)
    /* 202A4C 151D559C 44814000 */  mtc1       $at, $f8
    /* 202A50 151D55A0 3C01800B */  lui        $at, %hi(D_800AB220)
    /* 202A54 151D55A4 C42AB220 */  lwc1       $f10, %lo(D_800AB220)($at)
    /* 202A58 151D55A8 3C01800B */  lui        $at, %hi(D_800AB224)
    /* 202A5C 151D55AC C430B224 */  lwc1       $f16, %lo(D_800AB224)($at)
    /* 202A60 151D55B0 3C01800B */  lui        $at, %hi(D_800AB228)
    /* 202A64 151D55B4 C432B228 */  lwc1       $f18, %lo(D_800AB228)($at)
    /* 202A68 151D55B8 3C014234 */  lui        $at, (0x42340000 >> 16)
    /* 202A6C 151D55BC E7A40038 */  swc1       $f4, 0x38($sp)
    /* 202A70 151D55C0 44812000 */  mtc1       $at, $f4
    /* 202A74 151D55C4 3C01800B */  lui        $at, %hi(D_800AB22C)
    /* 202A78 151D55C8 E7A6003C */  swc1       $f6, 0x3C($sp)
    /* 202A7C 151D55CC C426B22C */  lwc1       $f6, %lo(D_800AB22C)($at)
    /* 202A80 151D55D0 3C01800B */  lui        $at, %hi(D_800AB230)
    /* 202A84 151D55D4 E7A80040 */  swc1       $f8, 0x40($sp)
    /* 202A88 151D55D8 C428B230 */  lwc1       $f8, %lo(D_800AB230)($at)
    /* 202A8C 151D55DC 3C01800B */  lui        $at, %hi(D_800AB234)
    /* 202A90 151D55E0 E7AA0044 */  swc1       $f10, 0x44($sp)
    /* 202A94 151D55E4 C42AB234 */  lwc1       $f10, %lo(D_800AB234)($at)
    /* 202A98 151D55E8 24090064 */  addiu      $t1, $zero, 0x64
    /* 202A9C 151D55EC 240C000C */  addiu      $t4, $zero, 0xC
    /* 202AA0 151D55F0 240B0014 */  addiu      $t3, $zero, 0x14
    /* 202AA4 151D55F4 AFAE0050 */  sw         $t6, 0x50($sp)
    /* 202AA8 151D55F8 AFAF0054 */  sw         $t7, 0x54($sp)
    /* 202AAC 151D55FC A7B80068 */  sh         $t8, 0x68($sp)
    /* 202AB0 151D5600 A7B9006A */  sh         $t9, 0x6A($sp)
    /* 202AB4 151D5604 A7A8006C */  sh         $t0, 0x6C($sp)
    /* 202AB8 151D5608 A7A9006E */  sh         $t1, 0x6E($sp)
    /* 202ABC 151D560C A7AC0070 */  sh         $t4, 0x70($sp)
    /* 202AC0 151D5610 A7AB0072 */  sh         $t3, 0x72($sp)
    /* 202AC4 151D5614 A3A00074 */  sb         $zero, 0x74($sp)
    /* 202AC8 151D5618 27A4001C */  addiu      $a0, $sp, 0x1C
    /* 202ACC 151D561C E7B00048 */  swc1       $f16, 0x48($sp)
    /* 202AD0 151D5620 E7B2004C */  swc1       $f18, 0x4C($sp)
    /* 202AD4 151D5624 E7A40058 */  swc1       $f4, 0x58($sp)
    /* 202AD8 151D5628 E7A6005C */  swc1       $f6, 0x5C($sp)
    /* 202ADC 151D562C E7A80060 */  swc1       $f8, 0x60($sp)
    /* 202AE0 151D5630 0D453F3A */  jal        func_1514FCE8
    /* 202AE4 151D5634 E7AA0064 */   swc1      $f10, 0x64($sp)
    /* 202AE8 151D5638 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 202AEC 151D563C 27BD0078 */  addiu      $sp, $sp, 0x78
    /* 202AF0 151D5640 03E00008 */  jr         $ra
    /* 202AF4 151D5644 00000000 */   nop
endlabel func_151D5514
