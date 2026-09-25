glabel func_150D3360
    /* 100810 150D3360 27BDFDF8 */  addiu      $sp, $sp, -0x208
    /* 100814 150D3364 3C0141A0 */  lui        $at, (0x41A00000 >> 16)
    /* 100818 150D3368 44810000 */  mtc1       $at, $f0
    /* 10081C 150D336C AFBF003C */  sw         $ra, 0x3C($sp)
    /* 100820 150D3370 AFB00038 */  sw         $s0, 0x38($sp)
    /* 100824 150D3374 AFA5020C */  sw         $a1, 0x20C($sp)
    /* 100828 150D3378 AFA60210 */  sw         $a2, 0x210($sp)
    /* 10082C 150D337C 240E0019 */  addiu      $t6, $zero, 0x19
    /* 100830 150D3380 240F012C */  addiu      $t7, $zero, 0x12C
    /* 100834 150D3384 24180012 */  addiu      $t8, $zero, 0x12
    /* 100838 150D3388 2419000F */  addiu      $t9, $zero, 0xF
    /* 10083C 150D338C 24080001 */  addiu      $t0, $zero, 0x1
    /* 100840 150D3390 24090001 */  addiu      $t1, $zero, 0x1
    /* 100844 150D3394 A3AE0201 */  sb         $t6, 0x201($sp)
    /* 100848 150D3398 A7AF01F8 */  sh         $t7, 0x1F8($sp)
    /* 10084C 150D339C A7B801FA */  sh         $t8, 0x1FA($sp)
    /* 100850 150D33A0 AFB901FC */  sw         $t9, 0x1FC($sp)
    /* 100854 150D33A4 A3A80200 */  sb         $t0, 0x200($sp)
    /* 100858 150D33A8 E7A001E8 */  swc1       $f0, 0x1E8($sp)
    /* 10085C 150D33AC E7A001E4 */  swc1       $f0, 0x1E4($sp)
    /* 100860 150D33B0 A3A901D5 */  sb         $t1, 0x1D5($sp)
    /* 100864 150D33B4 AFA001DC */  sw         $zero, 0x1DC($sp)
    /* 100868 150D33B8 AFA001E0 */  sw         $zero, 0x1E0($sp)
    /* 10086C 150D33BC AFA401D0 */  sw         $a0, 0x1D0($sp)
    /* 100870 150D33C0 908A003B */  lbu        $t2, 0x3B($a0)
    /* 100874 150D33C4 24010048 */  addiu      $at, $zero, 0x48
    /* 100878 150D33C8 00003025 */  or         $a2, $zero, $zero
    /* 10087C 150D33CC A3AA01D4 */  sb         $t2, 0x1D4($sp)
    /* 100880 150D33D0 908B0004 */  lbu        $t3, 0x4($a0)
    /* 100884 150D33D4 24050079 */  addiu      $a1, $zero, 0x79
    /* 100888 150D33D8 15610003 */  bne        $t3, $at, .L150D33E8
    /* 10088C 150D33DC 00000000 */   nop
    /* 100890 150D33E0 10000001 */  b          .L150D33E8
    /* 100894 150D33E4 2405007A */   addiu     $a1, $zero, 0x7A
  .L150D33E8:
    /* 100898 150D33E8 0D40C657 */  jal        func_1503195C
    /* 10089C 150D33EC AFA40208 */   sw        $a0, 0x208($sp)
    /* 1008A0 150D33F0 10400198 */  beqz       $v0, .L150D3A54
    /* 1008A4 150D33F4 00403825 */   or        $a3, $v0, $zero
    /* 1008A8 150D33F8 27A401EC */  addiu      $a0, $sp, 0x1EC
    /* 1008AC 150D33FC 27A501C0 */  addiu      $a1, $sp, 0x1C0
    /* 1008B0 150D3400 8FA60208 */  lw         $a2, 0x208($sp)
    /* 1008B4 150D3404 0D4352B8 */  jal        func_150D4AE0
    /* 1008B8 150D3408 AFA201D8 */   sw        $v0, 0x1D8($sp)
    /* 1008BC 150D340C 10400005 */  beqz       $v0, .L150D3424
    /* 1008C0 150D3410 27A401EC */   addiu     $a0, $sp, 0x1EC
    /* 1008C4 150D3414 97AC01FA */  lhu        $t4, 0x1FA($sp)
    /* 1008C8 150D3418 358D0004 */  ori        $t5, $t4, 0x4
    /* 1008CC 150D341C 1000000A */  b          .L150D3448
    /* 1008D0 150D3420 A7AD01FA */   sh        $t5, 0x1FA($sp)
  .L150D3424:
    /* 1008D4 150D3424 44800000 */  mtc1       $zero, $f0
    /* 1008D8 150D3428 3C0143FA */  lui        $at, (0x43FA0000 >> 16)
    /* 1008DC 150D342C 44812000 */  mtc1       $at, $f4
    /* 1008E0 150D3430 E7A001EC */  swc1       $f0, 0x1EC($sp)
    /* 1008E4 150D3434 E7A001F0 */  swc1       $f0, 0x1F0($sp)
    /* 1008E8 150D3438 E7A001F4 */  swc1       $f0, 0x1F4($sp)
    /* 1008EC 150D343C E7A001C0 */  swc1       $f0, 0x1C0($sp)
    /* 1008F0 150D3440 E7A001C8 */  swc1       $f0, 0x1C8($sp)
    /* 1008F4 150D3444 E7A401C4 */  swc1       $f4, 0x1C4($sp)
  .L150D3448:
    /* 1008F8 150D3448 93B8020F */  lbu        $t8, 0x20F($sp)
    /* 1008FC 150D344C 8FB90210 */  lw         $t9, 0x210($sp)
    /* 100900 150D3450 240E000D */  addiu      $t6, $zero, 0xD
    /* 100904 150D3454 240F000D */  addiu      $t7, $zero, 0xD
    /* 100908 150D3458 AFAF0014 */  sw         $t7, 0x14($sp)
    /* 10090C 150D345C AFAE0010 */  sw         $t6, 0x10($sp)
    /* 100910 150D3460 24050020 */  addiu      $a1, $zero, 0x20
    /* 100914 150D3464 24060014 */  addiu      $a2, $zero, 0x14
    /* 100918 150D3468 00003825 */  or         $a3, $zero, $zero
    /* 10091C 150D346C AFA00018 */  sw         $zero, 0x18($sp)
    /* 100920 150D3470 AFA0001C */  sw         $zero, 0x1C($sp)
    /* 100924 150D3474 AFA00020 */  sw         $zero, 0x20($sp)
    /* 100928 150D3478 AFB80024 */  sw         $t8, 0x24($sp)
    /* 10092C 150D347C 0D451EA0 */  jal        func_15147A80
    /* 100930 150D3480 AFB90028 */   sw        $t9, 0x28($sp)
    /* 100934 150D3484 10400173 */  beqz       $v0, .L150D3A54
    /* 100938 150D3488 27A501D0 */   addiu     $a1, $sp, 0x1D0
    /* 10093C 150D348C 8C500098 */  lw         $s0, 0x98($v0)
    /* 100940 150D3490 2406001C */  addiu      $a2, $zero, 0x1C
    /* 100944 150D3494 0C008BB0 */  jal        memcpy
    /* 100948 150D3498 02002025 */   or        $a0, $s0, $zero
    /* 10094C 150D349C 3C088009 */  lui        $t0, %hi(D_8008FD8C)
    /* 100950 150D34A0 8108FD8C */  lb         $t0, %lo(D_8008FD8C)($t0)
    /* 100954 150D34A4 240405B3 */  addiu      $a0, $zero, 0x5B3
    /* 100958 150D34A8 240903E8 */  addiu      $t1, $zero, 0x3E8
    /* 10095C 150D34AC 29010005 */  slti       $at, $t0, 0x5
    /* 100960 150D34B0 1020001F */  beqz       $at, .L150D3530
    /* 100964 150D34B4 240803E8 */   addiu     $t0, $zero, 0x3E8
    /* 100968 150D34B8 8E020000 */  lw         $v0, 0x0($s0)
    /* 10096C 150D34BC 3C0B150D */  lui        $t3, %hi(func_150D5124)
    /* 100970 150D34C0 256B5124 */  addiu      $t3, $t3, %lo(func_150D5124)
    /* 100974 150D34C4 C4460014 */  lwc1       $f6, 0x14($v0)
    /* 100978 150D34C8 C44A0018 */  lwc1       $f10, 0x18($v0)
    /* 10097C 150D34CC C452001C */  lwc1       $f18, 0x1C($v0)
    /* 100980 150D34D0 4600320D */  trunc.w.s  $f8, $f6
    /* 100984 150D34D4 240C05B3 */  addiu      $t4, $zero, 0x5B3
    /* 100988 150D34D8 AFAC0024 */  sw         $t4, 0x24($sp)
    /* 10098C 150D34DC 4600540D */  trunc.w.s  $f16, $f10
    /* 100990 150D34E0 44054000 */  mfc1       $a1, $f8
    /* 100994 150D34E4 AFA0002C */  sw         $zero, 0x2C($sp)
    /* 100998 150D34E8 4600910D */  trunc.w.s  $f4, $f18
    /* 10099C 150D34EC 44068000 */  mfc1       $a2, $f16
    /* 1009A0 150D34F0 00055400 */  sll        $t2, $a1, 16
    /* 1009A4 150D34F4 000A2C03 */  sra        $a1, $t2, 16
    /* 1009A8 150D34F8 44072000 */  mfc1       $a3, $f4
    /* 1009AC 150D34FC 00066C00 */  sll        $t5, $a2, 16
    /* 1009B0 150D3500 000D3403 */  sra        $a2, $t5, 16
    /* 1009B4 150D3504 240D000C */  addiu      $t5, $zero, 0xC
    /* 1009B8 150D3508 240A00C8 */  addiu      $t2, $zero, 0xC8
    /* 1009BC 150D350C 0007C400 */  sll        $t8, $a3, 16
    /* 1009C0 150D3510 00183C03 */  sra        $a3, $t8, 16
    /* 1009C4 150D3514 AFAA0018 */  sw         $t2, 0x18($sp)
    /* 1009C8 150D3518 AFAD0028 */  sw         $t5, 0x28($sp)
    /* 1009CC 150D351C AFB00020 */  sw         $s0, 0x20($sp)
    /* 1009D0 150D3520 AFAB001C */  sw         $t3, 0x1C($sp)
    /* 1009D4 150D3524 AFA90014 */  sw         $t1, 0x14($sp)
    /* 1009D8 150D3528 0C003E99 */  jal        func_1000FA64
    /* 1009DC 150D352C AFA80010 */   sw        $t0, 0x10($sp)
  .L150D3530:
    /* 1009E0 150D3530 8E020000 */  lw         $v0, 0x0($s0)
    /* 1009E4 150D3534 3C03150D */  lui        $v1, %hi(func_150D5124)
    /* 1009E8 150D3538 24635124 */  addiu      $v1, $v1, %lo(func_150D5124)
    /* 1009EC 150D353C C4460014 */  lwc1       $f6, 0x14($v0)
    /* 1009F0 150D3540 C44A0018 */  lwc1       $f10, 0x18($v0)
    /* 1009F4 150D3544 C452001C */  lwc1       $f18, 0x1C($v0)
    /* 1009F8 150D3548 4600320D */  trunc.w.s  $f8, $f6
    /* 1009FC 150D354C 240D03E8 */  addiu      $t5, $zero, 0x3E8
    /* 100A00 150D3550 240E03E8 */  addiu      $t6, $zero, 0x3E8
    /* 100A04 150D3554 4600540D */  trunc.w.s  $f16, $f10
    /* 100A08 150D3558 44054000 */  mfc1       $a1, $f8
    /* 100A0C 150D355C 241805B4 */  addiu      $t8, $zero, 0x5B4
    /* 100A10 150D3560 4600910D */  trunc.w.s  $f4, $f18
    /* 100A14 150D3564 44068000 */  mfc1       $a2, $f16
    /* 100A18 150D3568 00057C00 */  sll        $t7, $a1, 16
    /* 100A1C 150D356C 000F2C03 */  sra        $a1, $t7, 16
    /* 100A20 150D3570 44072000 */  mfc1       $a3, $f4
    /* 100A24 150D3574 240F00C8 */  addiu      $t7, $zero, 0xC8
    /* 100A28 150D3578 2419000C */  addiu      $t9, $zero, 0xC
    /* 100A2C 150D357C 00064400 */  sll        $t0, $a2, 16
    /* 100A30 150D3580 00075C00 */  sll        $t3, $a3, 16
    /* 100A34 150D3584 000B3C03 */  sra        $a3, $t3, 16
    /* 100A38 150D3588 00083403 */  sra        $a2, $t0, 16
    /* 100A3C 150D358C AFB90028 */  sw         $t9, 0x28($sp)
    /* 100A40 150D3590 AFAF0018 */  sw         $t7, 0x18($sp)
    /* 100A44 150D3594 AFB80024 */  sw         $t8, 0x24($sp)
    /* 100A48 150D3598 AFAE0014 */  sw         $t6, 0x14($sp)
    /* 100A4C 150D359C AFAD0010 */  sw         $t5, 0x10($sp)
    /* 100A50 150D35A0 AFA30044 */  sw         $v1, 0x44($sp)
    /* 100A54 150D35A4 AFA0002C */  sw         $zero, 0x2C($sp)
    /* 100A58 150D35A8 AFB00020 */  sw         $s0, 0x20($sp)
    /* 100A5C 150D35AC AFA3001C */  sw         $v1, 0x1C($sp)
    /* 100A60 150D35B0 0C003E99 */  jal        func_1000FA64
    /* 100A64 150D35B4 240405B4 */   addiu     $a0, $zero, 0x5B4
    /* 100A68 150D35B8 3C088009 */  lui        $t0, %hi(D_8008FD8C)
    /* 100A6C 150D35BC 8108FD8C */  lb         $t0, %lo(D_8008FD8C)($t0)
    /* 100A70 150D35C0 8FA30044 */  lw         $v1, 0x44($sp)
    /* 100A74 150D35C4 8FA90208 */  lw         $t1, 0x208($sp)
    /* 100A78 150D35C8 29010007 */  slti       $at, $t0, 0x7
    /* 100A7C 150D35CC 14200004 */  bnez       $at, .L150D35E0
    /* 100A80 150D35D0 240405BC */   addiu     $a0, $zero, 0x5BC
    /* 100A84 150D35D4 8D2A0318 */  lw         $t2, 0x318($t1)
    /* 100A88 150D35D8 51400020 */  beql       $t2, $zero, .L150D365C
    /* 100A8C 150D35DC 3C013F80 */   lui       $at, (0x3F800000 >> 16)
  .L150D35E0:
    /* 100A90 150D35E0 8E020000 */  lw         $v0, 0x0($s0)
    /* 100A94 150D35E4 240A03E8 */  addiu      $t2, $zero, 0x3E8
    /* 100A98 150D35E8 240B03E8 */  addiu      $t3, $zero, 0x3E8
    /* 100A9C 150D35EC C4460014 */  lwc1       $f6, 0x14($v0)
    /* 100AA0 150D35F0 C44A0018 */  lwc1       $f10, 0x18($v0)
    /* 100AA4 150D35F4 C452001C */  lwc1       $f18, 0x1C($v0)
    /* 100AA8 150D35F8 4600320D */  trunc.w.s  $f8, $f6
    /* 100AAC 150D35FC 240D05BC */  addiu      $t5, $zero, 0x5BC
    /* 100AB0 150D3600 240E000C */  addiu      $t6, $zero, 0xC
    /* 100AB4 150D3604 4600540D */  trunc.w.s  $f16, $f10
    /* 100AB8 150D3608 44054000 */  mfc1       $a1, $f8
    /* 100ABC 150D360C AFAE0028 */  sw         $t6, 0x28($sp)
    /* 100AC0 150D3610 4600910D */  trunc.w.s  $f4, $f18
    /* 100AC4 150D3614 44068000 */  mfc1       $a2, $f16
    /* 100AC8 150D3618 00056400 */  sll        $t4, $a1, 16
    /* 100ACC 150D361C 000C2C03 */  sra        $a1, $t4, 16
    /* 100AD0 150D3620 44072000 */  mfc1       $a3, $f4
    /* 100AD4 150D3624 240C00C8 */  addiu      $t4, $zero, 0xC8
    /* 100AD8 150D3628 00067C00 */  sll        $t7, $a2, 16
    /* 100ADC 150D362C 00074400 */  sll        $t0, $a3, 16
    /* 100AE0 150D3630 00083C03 */  sra        $a3, $t0, 16
    /* 100AE4 150D3634 000F3403 */  sra        $a2, $t7, 16
    /* 100AE8 150D3638 AFAC0018 */  sw         $t4, 0x18($sp)
    /* 100AEC 150D363C AFAD0024 */  sw         $t5, 0x24($sp)
    /* 100AF0 150D3640 AFA0002C */  sw         $zero, 0x2C($sp)
    /* 100AF4 150D3644 AFB00020 */  sw         $s0, 0x20($sp)
    /* 100AF8 150D3648 AFA3001C */  sw         $v1, 0x1C($sp)
    /* 100AFC 150D364C AFAB0014 */  sw         $t3, 0x14($sp)
    /* 100B00 150D3650 0C003E99 */  jal        func_1000FA64
    /* 100B04 150D3654 AFAA0010 */   sw        $t2, 0x10($sp)
    /* 100B08 150D3658 3C013F80 */  lui        $at, (0x3F800000 >> 16)
  .L150D365C:
    /* 100B0C 150D365C 44810000 */  mtc1       $at, $f0
    /* 100B10 150D3660 3C014220 */  lui        $at, (0x42200000 >> 16)
    /* 100B14 150D3664 44811000 */  mtc1       $at, $f2
    /* 100B18 150D3668 3C01800A */  lui        $at, %hi(D_800A09E8)
    /* 100B1C 150D366C C42C09E8 */  lwc1       $f12, %lo(D_800A09E8)($at)
    /* 100B20 150D3670 3C0142C8 */  lui        $at, (0x42C80000 >> 16)
    /* 100B24 150D3674 44817000 */  mtc1       $at, $f14
    /* 100B28 150D3678 3C014348 */  lui        $at, (0x43480000 >> 16)
    /* 100B2C 150D367C 44813000 */  mtc1       $at, $f6
    /* 100B30 150D3680 3C01800A */  lui        $at, %hi(D_800A09EC)
    /* 100B34 150D3684 C42809EC */  lwc1       $f8, %lo(D_800A09EC)($at)
    /* 100B38 150D3688 3C01800A */  lui        $at, %hi(D_800A09F0)
    /* 100B3C 150D368C C42A09F0 */  lwc1       $f10, %lo(D_800A09F0)($at)
    /* 100B40 150D3690 3C01800A */  lui        $at, %hi(D_800A09F4)
    /* 100B44 150D3694 C43009F4 */  lwc1       $f16, %lo(D_800A09F4)($at)
    /* 100B48 150D3698 240FFFFF */  addiu      $t7, $zero, -0x1
    /* 100B4C 150D369C 2418FFFF */  addiu      $t8, $zero, -0x1
    /* 100B50 150D36A0 2419FFFF */  addiu      $t9, $zero, -0x1
    /* 100B54 150D36A4 2408FFFF */  addiu      $t0, $zero, -0x1
    /* 100B58 150D36A8 2409FFFF */  addiu      $t1, $zero, -0x1
    /* 100B5C 150D36AC 240AFFFF */  addiu      $t2, $zero, -0x1
    /* 100B60 150D36B0 240BFFFF */  addiu      $t3, $zero, -0x1
    /* 100B64 150D36B4 AFAF0184 */  sw         $t7, 0x184($sp)
    /* 100B68 150D36B8 AFB80194 */  sw         $t8, 0x194($sp)
    /* 100B6C 150D36BC AFB90188 */  sw         $t9, 0x188($sp)
    /* 100B70 150D36C0 AFA80198 */  sw         $t0, 0x198($sp)
    /* 100B74 150D36C4 AFA9018C */  sw         $t1, 0x18C($sp)
    /* 100B78 150D36C8 AFAA019C */  sw         $t2, 0x19C($sp)
    /* 100B7C 150D36CC AFAB0190 */  sw         $t3, 0x190($sp)
    /* 100B80 150D36D0 240DFFFF */  addiu      $t5, $zero, -0x1
    /* 100B84 150D36D4 240CFFFF */  addiu      $t4, $zero, -0x1
    /* 100B88 150D36D8 A3AD01B9 */  sb         $t5, 0x1B9($sp)
    /* 100B8C 150D36DC 240E0015 */  addiu      $t6, $zero, 0x15
    /* 100B90 150D36E0 240F0003 */  addiu      $t7, $zero, 0x3
    /* 100B94 150D36E4 24185503 */  addiu      $t8, $zero, 0x5503
    /* 100B98 150D36E8 2419012C */  addiu      $t9, $zero, 0x12C
    /* 100B9C 150D36EC 240800FF */  addiu      $t0, $zero, 0xFF
    /* 100BA0 150D36F0 240900FF */  addiu      $t1, $zero, 0xFF
    /* 100BA4 150D36F4 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 100BA8 150D36F8 240B00FF */  addiu      $t3, $zero, 0xFF
    /* 100BAC 150D36FC E7A20164 */  swc1       $f2, 0x164($sp)
    /* 100BB0 150D3700 E7A20168 */  swc1       $f2, 0x168($sp)
    /* 100BB4 150D3704 E7A2016C */  swc1       $f2, 0x16C($sp)
    /* 100BB8 150D3708 E7AC0170 */  swc1       $f12, 0x170($sp)
    /* 100BBC 150D370C E7AC0174 */  swc1       $f12, 0x174($sp)
    /* 100BC0 150D3710 AFAC01A0 */  sw         $t4, 0x1A0($sp)
    /* 100BC4 150D3714 AFA001A4 */  sw         $zero, 0x1A4($sp)
    /* 100BC8 150D3718 E7A001A8 */  swc1       $f0, 0x1A8($sp)
    /* 100BCC 150D371C A7A001AC */  sh         $zero, 0x1AC($sp)
    /* 100BD0 150D3720 A7A001AE */  sh         $zero, 0x1AE($sp)
    /* 100BD4 150D3724 A7A001B0 */  sh         $zero, 0x1B0($sp)
    /* 100BD8 150D3728 A7A001B2 */  sh         $zero, 0x1B2($sp)
    /* 100BDC 150D372C A3A001B4 */  sb         $zero, 0x1B4($sp)
    /* 100BE0 150D3730 A3A001B5 */  sb         $zero, 0x1B5($sp)
    /* 100BE4 150D3734 A3A001B6 */  sb         $zero, 0x1B6($sp)
    /* 100BE8 150D3738 A3A001B7 */  sb         $zero, 0x1B7($sp)
    /* 100BEC 150D373C A3A001B8 */  sb         $zero, 0x1B8($sp)
    /* 100BF0 150D3740 A3AE0108 */  sb         $t6, 0x108($sp)
    /* 100BF4 150D3744 A3AF0109 */  sb         $t7, 0x109($sp)
    /* 100BF8 150D3748 A7B8010A */  sh         $t8, 0x10A($sp)
    /* 100BFC 150D374C A7B9010C */  sh         $t9, 0x10C($sp)
    /* 100C00 150D3750 AFA00110 */  sw         $zero, 0x110($sp)
    /* 100C04 150D3754 AFA00114 */  sw         $zero, 0x114($sp)
    /* 100C08 150D3758 A3A80118 */  sb         $t0, 0x118($sp)
    /* 100C0C 150D375C A3A90119 */  sb         $t1, 0x119($sp)
    /* 100C10 150D3760 A3AA011A */  sb         $t2, 0x11A($sp)
    /* 100C14 150D3764 A3AB011B */  sb         $t3, 0x11B($sp)
    /* 100C18 150D3768 E7AE011C */  swc1       $f14, 0x11C($sp)
    /* 100C1C 150D376C E7AE0120 */  swc1       $f14, 0x120($sp)
    /* 100C20 150D3770 27AD01EC */  addiu      $t5, $sp, 0x1EC
    /* 100C24 150D3774 E7A60160 */  swc1       $f6, 0x160($sp)
    /* 100C28 150D3778 E7A80178 */  swc1       $f8, 0x178($sp)
    /* 100C2C 150D377C E7AA017C */  swc1       $f10, 0x17C($sp)
    /* 100C30 150D3780 E7B00180 */  swc1       $f16, 0x180($sp)
    /* 100C34 150D3784 8DA10000 */  lw         $at, 0x0($t5)
    /* 100C38 150D3788 27AC0124 */  addiu      $t4, $sp, 0x124
    /* 100C3C 150D378C 27A801C0 */  addiu      $t0, $sp, 0x1C0
    /* 100C40 150D3790 AD810000 */  sw         $at, 0x0($t4)
    /* 100C44 150D3794 8DB80004 */  lw         $t8, 0x4($t5)
    /* 100C48 150D3798 27B90130 */  addiu      $t9, $sp, 0x130
    /* 100C4C 150D379C 3C0F00CD */  lui        $t7, (0xCD2006 >> 16)
    /* 100C50 150D37A0 AD980004 */  sw         $t8, 0x4($t4)
    /* 100C54 150D37A4 8DA10008 */  lw         $at, 0x8($t5)
    /* 100C58 150D37A8 35EF2006 */  ori        $t7, $t7, (0xCD2006 & 0xFFFF)
    /* 100C5C 150D37AC 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 100C60 150D37B0 AD810008 */  sw         $at, 0x8($t4)
    /* 100C64 150D37B4 8D010000 */  lw         $at, 0x0($t0)
    /* 100C68 150D37B8 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 100C6C 150D37BC 240D0006 */  addiu      $t5, $zero, 0x6
    /* 100C70 150D37C0 AF210000 */  sw         $at, 0x0($t9)
    /* 100C74 150D37C4 8D0B0004 */  lw         $t3, 0x4($t0)
    /* 100C78 150D37C8 241800FF */  addiu      $t8, $zero, 0xFF
    /* 100C7C 150D37CC 240AFFFF */  addiu      $t2, $zero, -0x1
    /* 100C80 150D37D0 AF2B0004 */  sw         $t3, 0x4($t9)
    /* 100C84 150D37D4 8D010008 */  lw         $at, 0x8($t0)
    /* 100C88 150D37D8 27A40160 */  addiu      $a0, $sp, 0x160
    /* 100C8C 150D37DC 24050060 */  addiu      $a1, $zero, 0x60
    /* 100C90 150D37E0 AF210008 */  sw         $at, 0x8($t9)
    /* 100C94 150D37E4 8FB90210 */  lw         $t9, 0x210($sp)
    /* 100C98 150D37E8 93A9020F */  lbu        $t1, 0x20F($sp)
    /* 100C9C 150D37EC E7A0013C */  swc1       $f0, 0x13C($sp)
    /* 100CA0 150D37F0 E7A00140 */  swc1       $f0, 0x140($sp)
    /* 100CA4 150D37F4 E7A00144 */  swc1       $f0, 0x144($sp)
    /* 100CA8 150D37F8 AFAF0148 */  sw         $t7, 0x148($sp)
    /* 100CAC 150D37FC A3AE014C */  sb         $t6, 0x14C($sp)
    /* 100CB0 150D3800 A3AC014D */  sb         $t4, 0x14D($sp)
    /* 100CB4 150D3804 A3A0014E */  sb         $zero, 0x14E($sp)
    /* 100CB8 150D3808 A3AD014F */  sb         $t5, 0x14F($sp)
    /* 100CBC 150D380C AFA00150 */  sw         $zero, 0x150($sp)
    /* 100CC0 150D3810 A3B80154 */  sb         $t8, 0x154($sp)
    /* 100CC4 150D3814 AFAA001C */  sw         $t2, 0x1C($sp)
    /* 100CC8 150D3818 AFA00018 */  sw         $zero, 0x18($sp)
    /* 100CCC 150D381C AFA00014 */  sw         $zero, 0x14($sp)
    /* 100CD0 150D3820 AFA00010 */  sw         $zero, 0x10($sp)
    /* 100CD4 150D3824 27A60108 */  addiu      $a2, $sp, 0x108
    /* 100CD8 150D3828 00003825 */  or         $a3, $zero, $zero
    /* 100CDC 150D382C AFB90024 */  sw         $t9, 0x24($sp)
    /* 100CE0 150D3830 0D4501F4 */  jal        func_151407D0
    /* 100CE4 150D3834 AFA90020 */   sw        $t1, 0x20($sp)
    /* 100CE8 150D3838 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 100CEC 150D383C 44810000 */  mtc1       $at, $f0
    /* 100CF0 150D3840 3C014234 */  lui        $at, (0x42340000 >> 16)
    /* 100CF4 150D3844 44811000 */  mtc1       $at, $f2
    /* 100CF8 150D3848 3C0141CC */  lui        $at, (0x41CC0000 >> 16)
    /* 100CFC 150D384C 44816000 */  mtc1       $at, $f12
    /* 100D00 150D3850 3C01800A */  lui        $at, %hi(D_800A09F8)
    /* 100D04 150D3854 C42E09F8 */  lwc1       $f14, %lo(D_800A09F8)($at)
    /* 100D08 150D3858 AE02000C */  sw         $v0, 0xC($s0)
    /* 100D0C 150D385C 3C01800A */  lui        $at, %hi(D_800A09FC)
    /* 100D10 150D3860 C43209FC */  lwc1       $f18, %lo(D_800A09FC)($at)
    /* 100D14 150D3864 3C01800A */  lui        $at, %hi(D_800A0A00)
    /* 100D18 150D3868 C4240A00 */  lwc1       $f4, %lo(D_800A0A00)($at)
    /* 100D1C 150D386C 2408FFFF */  addiu      $t0, $zero, -0x1
    /* 100D20 150D3870 240BFFFF */  addiu      $t3, $zero, -0x1
    /* 100D24 150D3874 240FFFFF */  addiu      $t7, $zero, -0x1
    /* 100D28 150D3878 240EFFFF */  addiu      $t6, $zero, -0x1
    /* 100D2C 150D387C 240CFFFF */  addiu      $t4, $zero, -0x1
    /* 100D30 150D3880 240DFFFF */  addiu      $t5, $zero, -0x1
    /* 100D34 150D3884 2418FFFF */  addiu      $t8, $zero, -0x1
    /* 100D38 150D3888 240AFFFF */  addiu      $t2, $zero, -0x1
    /* 100D3C 150D388C 2409FFFF */  addiu      $t1, $zero, -0x1
    /* 100D40 150D3890 A7A0004C */  sh         $zero, 0x4C($sp)
    /* 100D44 150D3894 E7A00050 */  swc1       $f0, 0x50($sp)
    /* 100D48 150D3898 E7A200B0 */  swc1       $f2, 0xB0($sp)
    /* 100D4C 150D389C E7A200AC */  swc1       $f2, 0xAC($sp)
    /* 100D50 150D38A0 E7AC00B8 */  swc1       $f12, 0xB8($sp)
    /* 100D54 150D38A4 E7AC00B4 */  swc1       $f12, 0xB4($sp)
    /* 100D58 150D38A8 E7AE00BC */  swc1       $f14, 0xBC($sp)
    /* 100D5C 150D38AC E7AE00C0 */  swc1       $f14, 0xC0($sp)
    /* 100D60 150D38B0 E7A000C4 */  swc1       $f0, 0xC4($sp)
    /* 100D64 150D38B4 AFA800D0 */  sw         $t0, 0xD0($sp)
    /* 100D68 150D38B8 AFAB00E0 */  sw         $t3, 0xE0($sp)
    /* 100D6C 150D38BC AFAF00D4 */  sw         $t7, 0xD4($sp)
    /* 100D70 150D38C0 AFAE00E4 */  sw         $t6, 0xE4($sp)
    /* 100D74 150D38C4 AFAC00D8 */  sw         $t4, 0xD8($sp)
    /* 100D78 150D38C8 AFAD00E8 */  sw         $t5, 0xE8($sp)
    /* 100D7C 150D38CC AFB800DC */  sw         $t8, 0xDC($sp)
    /* 100D80 150D38D0 AFAA00EC */  sw         $t2, 0xEC($sp)
    /* 100D84 150D38D4 AFA000F0 */  sw         $zero, 0xF0($sp)
    /* 100D88 150D38D8 E7A000F4 */  swc1       $f0, 0xF4($sp)
    /* 100D8C 150D38DC A7A000F8 */  sh         $zero, 0xF8($sp)
    /* 100D90 150D38E0 A7A000FA */  sh         $zero, 0xFA($sp)
    /* 100D94 150D38E4 A7A000FC */  sh         $zero, 0xFC($sp)
    /* 100D98 150D38E8 A7A000FE */  sh         $zero, 0xFE($sp)
    /* 100D9C 150D38EC A3A00100 */  sb         $zero, 0x100($sp)
    /* 100DA0 150D38F0 A3A00101 */  sb         $zero, 0x101($sp)
    /* 100DA4 150D38F4 A3A00102 */  sb         $zero, 0x102($sp)
    /* 100DA8 150D38F8 A3A00103 */  sb         $zero, 0x103($sp)
    /* 100DAC 150D38FC A3A00104 */  sb         $zero, 0x104($sp)
    /* 100DB0 150D3900 A3A90105 */  sb         $t1, 0x105($sp)
    /* 100DB4 150D3904 E7B200C8 */  swc1       $f18, 0xC8($sp)
    /* 100DB8 150D3908 0D42B688 */  jal        func_150ADA20
    /* 100DBC 150D390C E7A400CC */   swc1      $f4, 0xCC($sp)
    /* 100DC0 150D3910 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 100DC4 150D3914 44810000 */  mtc1       $at, $f0
    /* 100DC8 150D3918 30590003 */  andi       $t9, $v0, 0x3
    /* 100DCC 150D391C 00194080 */  sll        $t0, $t9, 2
    /* 100DD0 150D3920 3C0142C8 */  lui        $at, (0x42C80000 >> 16)
    /* 100DD4 150D3924 3C0B800A */  lui        $t3, %hi(D_800A09C0)
    /* 100DD8 150D3928 44811000 */  mtc1       $at, $f2
    /* 100DDC 150D392C 01685821 */  addu       $t3, $t3, $t0
    /* 100DE0 150D3930 8D6B09C0 */  lw         $t3, %lo(D_800A09C0)($t3)
    /* 100DE4 150D3934 240F0003 */  addiu      $t7, $zero, 0x3
    /* 100DE8 150D3938 240E2203 */  addiu      $t6, $zero, 0x2203
    /* 100DEC 150D393C 240C012C */  addiu      $t4, $zero, 0x12C
    /* 100DF0 150D3940 240D00FF */  addiu      $t5, $zero, 0xFF
    /* 100DF4 150D3944 241800FF */  addiu      $t8, $zero, 0xFF
    /* 100DF8 150D3948 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 100DFC 150D394C 240900FF */  addiu      $t1, $zero, 0xFF
    /* 100E00 150D3950 A3AF0055 */  sb         $t7, 0x55($sp)
    /* 100E04 150D3954 A7AE0056 */  sh         $t6, 0x56($sp)
    /* 100E08 150D3958 A7AC0058 */  sh         $t4, 0x58($sp)
    /* 100E0C 150D395C AFA0005C */  sw         $zero, 0x5C($sp)
    /* 100E10 150D3960 AFA00060 */  sw         $zero, 0x60($sp)
    /* 100E14 150D3964 A3AD0064 */  sb         $t5, 0x64($sp)
    /* 100E18 150D3968 A3B80065 */  sb         $t8, 0x65($sp)
    /* 100E1C 150D396C A3AA0066 */  sb         $t2, 0x66($sp)
    /* 100E20 150D3970 A3A90067 */  sb         $t1, 0x67($sp)
    /* 100E24 150D3974 27A801EC */  addiu      $t0, $sp, 0x1EC
    /* 100E28 150D3978 E7A20068 */  swc1       $f2, 0x68($sp)
    /* 100E2C 150D397C E7A2006C */  swc1       $f2, 0x6C($sp)
    /* 100E30 150D3980 A3AB0054 */  sb         $t3, 0x54($sp)
    /* 100E34 150D3984 8D010000 */  lw         $at, 0x0($t0)
    /* 100E38 150D3988 27B90070 */  addiu      $t9, $sp, 0x70
    /* 100E3C 150D398C 27AD01C0 */  addiu      $t5, $sp, 0x1C0
    /* 100E40 150D3990 AF210000 */  sw         $at, 0x0($t9)
    /* 100E44 150D3994 8D0E0004 */  lw         $t6, 0x4($t0)
    /* 100E48 150D3998 27AC007C */  addiu      $t4, $sp, 0x7C
    /* 100E4C 150D399C 3C0F00CD */  lui        $t7, (0xCD2006 >> 16)
    /* 100E50 150D39A0 AF2E0004 */  sw         $t6, 0x4($t9)
    /* 100E54 150D39A4 8D010008 */  lw         $at, 0x8($t0)
    /* 100E58 150D39A8 35EF2006 */  ori        $t7, $t7, (0xCD2006 & 0xFFFF)
    /* 100E5C 150D39AC 240B00FF */  addiu      $t3, $zero, 0xFF
    /* 100E60 150D39B0 AF210008 */  sw         $at, 0x8($t9)
    /* 100E64 150D39B4 8DA10000 */  lw         $at, 0x0($t5)
    /* 100E68 150D39B8 241900FF */  addiu      $t9, $zero, 0xFF
    /* 100E6C 150D39BC 24080007 */  addiu      $t0, $zero, 0x7
    /* 100E70 150D39C0 AD810000 */  sw         $at, 0x0($t4)
    /* 100E74 150D39C4 8DA90004 */  lw         $t1, 0x4($t5)
    /* 100E78 150D39C8 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 100E7C 150D39CC 240A0027 */  addiu      $t2, $zero, 0x27
    /* 100E80 150D39D0 AD890004 */  sw         $t1, 0x4($t4)
    /* 100E84 150D39D4 8DA10008 */  lw         $at, 0x8($t5)
    /* 100E88 150D39D8 2418FFFF */  addiu      $t8, $zero, -0x1
    /* 100E8C 150D39DC 27A400AC */  addiu      $a0, $sp, 0xAC
    /* 100E90 150D39E0 AD810008 */  sw         $at, 0x8($t4)
    /* 100E94 150D39E4 8FAD0210 */  lw         $t5, 0x210($sp)
    /* 100E98 150D39E8 93AC020F */  lbu        $t4, 0x20F($sp)
    /* 100E9C 150D39EC AFAF0094 */  sw         $t7, 0x94($sp)
    /* 100EA0 150D39F0 A3AB0098 */  sb         $t3, 0x98($sp)
    /* 100EA4 150D39F4 A3B90099 */  sb         $t9, 0x99($sp)
    /* 100EA8 150D39F8 A3A0009A */  sb         $zero, 0x9A($sp)
    /* 100EAC 150D39FC A3A8009B */  sb         $t0, 0x9B($sp)
    /* 100EB0 150D3A00 AFA0009C */  sw         $zero, 0x9C($sp)
    /* 100EB4 150D3A04 A3AE00A0 */  sb         $t6, 0xA0($sp)
    /* 100EB8 150D3A08 AFB8001C */  sw         $t8, 0x1C($sp)
    /* 100EBC 150D3A0C AFA00018 */  sw         $zero, 0x18($sp)
    /* 100EC0 150D3A10 AFA00014 */  sw         $zero, 0x14($sp)
    /* 100EC4 150D3A14 AFAA0010 */  sw         $t2, 0x10($sp)
    /* 100EC8 150D3A18 24050068 */  addiu      $a1, $zero, 0x68
    /* 100ECC 150D3A1C 27A60054 */  addiu      $a2, $sp, 0x54
    /* 100ED0 150D3A20 00003825 */  or         $a3, $zero, $zero
    /* 100ED4 150D3A24 E7A00088 */  swc1       $f0, 0x88($sp)
    /* 100ED8 150D3A28 E7A0008C */  swc1       $f0, 0x8C($sp)
    /* 100EDC 150D3A2C E7A00090 */  swc1       $f0, 0x90($sp)
    /* 100EE0 150D3A30 AFAD0024 */  sw         $t5, 0x24($sp)
    /* 100EE4 150D3A34 0D4501F4 */  jal        func_151407D0
    /* 100EE8 150D3A38 AFAC0020 */   sw        $t4, 0x20($sp)
    /* 100EEC 150D3A3C 10400005 */  beqz       $v0, .L150D3A54
    /* 100EF0 150D3A40 AE020010 */   sw        $v0, 0x10($s0)
    /* 100EF4 150D3A44 24440170 */  addiu      $a0, $v0, 0x170
    /* 100EF8 150D3A48 27A5004C */  addiu      $a1, $sp, 0x4C
    /* 100EFC 150D3A4C 0C008BB0 */  jal        memcpy
    /* 100F00 150D3A50 24060008 */   addiu     $a2, $zero, 0x8
  .L150D3A54:
    /* 100F04 150D3A54 8FBF003C */  lw         $ra, 0x3C($sp)
    /* 100F08 150D3A58 8FB00038 */  lw         $s0, 0x38($sp)
    /* 100F0C 150D3A5C 27BD0208 */  addiu      $sp, $sp, 0x208
    /* 100F10 150D3A60 03E00008 */  jr         $ra
    /* 100F14 150D3A64 00000000 */   nop
endlabel func_150D3360
