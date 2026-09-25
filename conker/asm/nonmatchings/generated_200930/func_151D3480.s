glabel func_151D3480
    /* 200930 151D3480 27BDFE40 */  addiu      $sp, $sp, -0x1C0
    /* 200934 151D3484 AFA701CC */  sw         $a3, 0x1CC($sp)
    /* 200938 151D3488 30EE00FF */  andi       $t6, $a3, 0xFF
    /* 20093C 151D348C 01C03825 */  or         $a3, $t6, $zero
    /* 200940 151D3490 AFBF0044 */  sw         $ra, 0x44($sp)
    /* 200944 151D3494 AFA401C0 */  sw         $a0, 0x1C0($sp)
    /* 200948 151D3498 AFA501C4 */  sw         $a1, 0x1C4($sp)
    /* 20094C 151D349C 28E10006 */  slti       $at, $a3, 0x6
    /* 200950 151D34A0 10200227 */  beqz       $at, .L151D3D40
    /* 200954 151D34A4 00E01825 */   or        $v1, $a3, $zero
    /* 200958 151D34A8 2CE10006 */  sltiu      $at, $a3, 0x6
    /* 20095C 151D34AC 10200015 */  beqz       $at, .L151D3504
    /* 200960 151D34B0 00077880 */   sll       $t7, $a3, 2
    /* 200964 151D34B4 3C01800B */  lui        $at, %hi(jtbl_800AB170_game)
    /* 200968 151D34B8 002F0821 */  addu       $at, $at, $t7
    /* 20096C 151D34BC 8C2FB170 */  lw         $t7, %lo(jtbl_800AB170_game)($at)
    /* 200970 151D34C0 01E00008 */  jr         $t7
    /* 200974 151D34C4 00000000 */   nop
  jlabel .L151D34C8_game_data
    /* 200978 151D34C8 2418000C */  addiu      $t8, $zero, 0xC
    /* 20097C 151D34CC 1000000E */  b          .L151D3508
    /* 200980 151D34D0 AFB80190 */   sw        $t8, 0x190($sp)
  jlabel .L151D34D4_game_data
    /* 200984 151D34D4 24190057 */  addiu      $t9, $zero, 0x57
    /* 200988 151D34D8 1000000B */  b          .L151D3508
    /* 20098C 151D34DC AFB90190 */   sw        $t9, 0x190($sp)
  jlabel .L151D34E0_game_data
    /* 200990 151D34E0 24080058 */  addiu      $t0, $zero, 0x58
    /* 200994 151D34E4 10000008 */  b          .L151D3508
    /* 200998 151D34E8 AFA80190 */   sw        $t0, 0x190($sp)
  jlabel .L151D34EC_game_data
    /* 20099C 151D34EC 24090034 */  addiu      $t1, $zero, 0x34
    /* 2009A0 151D34F0 10000005 */  b          .L151D3508
    /* 2009A4 151D34F4 AFA90190 */   sw        $t1, 0x190($sp)
  jlabel .L151D34F8_game_data
    /* 2009A8 151D34F8 240A004D */  addiu      $t2, $zero, 0x4D
    /* 2009AC 151D34FC 10000002 */  b          .L151D3508
    /* 2009B0 151D3500 AFAA0190 */   sw        $t2, 0x190($sp)
  jlabel .L151D3504
    /* 2009B4 151D3504 AFA00190 */  sw         $zero, 0x190($sp)
  .L151D3508:
    /* 2009B8 151D3508 14C0002C */  bnez       $a2, .L151D35BC
    /* 2009BC 151D350C 8FAB01C4 */   lw        $t3, 0x1C4($sp)
    /* 2009C0 151D3510 8FAC01C0 */  lw         $t4, 0x1C0($sp)
    /* 2009C4 151D3514 C5600000 */  lwc1       $f0, 0x0($t3)
    /* 2009C8 151D3518 C5620004 */  lwc1       $f2, 0x4($t3)
    /* 2009CC 151D351C C5920000 */  lwc1       $f18, 0x0($t4)
    /* 2009D0 151D3520 C58A0004 */  lwc1       $f10, 0x4($t4)
    /* 2009D4 151D3524 C5700008 */  lwc1       $f16, 0x8($t3)
    /* 2009D8 151D3528 C5880008 */  lwc1       $f8, 0x8($t4)
    /* 2009DC 151D352C 46009301 */  sub.s      $f12, $f18, $f0
    /* 2009E0 151D3530 44070000 */  mfc1       $a3, $f0
    /* 2009E4 151D3534 44809000 */  mtc1       $zero, $f18
    /* 2009E8 151D3538 46104201 */  sub.s      $f8, $f8, $f16
    /* 2009EC 151D353C 27AD0188 */  addiu      $t5, $sp, 0x188
    /* 2009F0 151D3540 27AE01A0 */  addiu      $t6, $sp, 0x1A0
    /* 2009F4 151D3544 46025381 */  sub.s      $f14, $f10, $f2
    /* 2009F8 151D3548 44064000 */  mfc1       $a2, $f8
    /* 2009FC 151D354C 27AF01B4 */  addiu      $t7, $sp, 0x1B4
    /* 200A00 151D3550 27B801B8 */  addiu      $t8, $sp, 0x1B8
    /* 200A04 151D3554 27B901BC */  addiu      $t9, $sp, 0x1BC
    /* 200A08 151D3558 27A80184 */  addiu      $t0, $sp, 0x184
    /* 200A0C 151D355C 27A90198 */  addiu      $t1, $sp, 0x198
    /* 200A10 151D3560 E7A20010 */  swc1       $f2, 0x10($sp)
    /* 200A14 151D3564 E7B00014 */  swc1       $f16, 0x14($sp)
    /* 200A18 151D3568 AFAD0018 */  sw         $t5, 0x18($sp)
    /* 200A1C 151D356C AFAE001C */  sw         $t6, 0x1C($sp)
    /* 200A20 151D3570 AFAF0020 */  sw         $t7, 0x20($sp)
    /* 200A24 151D3574 AFB80024 */  sw         $t8, 0x24($sp)
    /* 200A28 151D3578 AFB90028 */  sw         $t9, 0x28($sp)
    /* 200A2C 151D357C AFA8002C */  sw         $t0, 0x2C($sp)
    /* 200A30 151D3580 AFA90030 */  sw         $t1, 0x30($sp)
    /* 200A34 151D3584 AFA00034 */  sw         $zero, 0x34($sp)
    /* 200A38 151D3588 E7B20038 */  swc1       $f18, 0x38($sp)
    /* 200A3C 151D358C 0D42B270 */  jal        func_150AC9C0
    /* 200A40 151D3590 AFA30058 */   sw        $v1, 0x58($sp)
    /* 200A44 151D3594 10400004 */  beqz       $v0, .L151D35A8
    /* 200A48 151D3598 8FA30058 */   lw        $v1, 0x58($sp)
    /* 200A4C 151D359C 240A0001 */  addiu      $t2, $zero, 0x1
    /* 200A50 151D35A0 10000021 */  b          .L151D3628
    /* 200A54 151D35A4 A3AA019F */   sb        $t2, 0x19F($sp)
  .L151D35A8:
    /* 200A58 151D35A8 240BFFFF */  addiu      $t3, $zero, -0x1
    /* 200A5C 151D35AC A3A0019F */  sb         $zero, 0x19F($sp)
    /* 200A60 151D35B0 AFAB0198 */  sw         $t3, 0x198($sp)
    /* 200A64 151D35B4 1000001D */  b          .L151D362C
    /* 200A68 151D35B8 8FA40198 */   lw        $a0, 0x198($sp)
  .L151D35BC:
    /* 200A6C 151D35BC 8FAE01C0 */  lw         $t6, 0x1C0($sp)
    /* 200A70 151D35C0 240CFFFF */  addiu      $t4, $zero, -0x1
    /* 200A74 151D35C4 AFAC0198 */  sw         $t4, 0x198($sp)
    /* 200A78 151D35C8 8DC10000 */  lw         $at, 0x0($t6)
    /* 200A7C 151D35CC 27AD01B4 */  addiu      $t5, $sp, 0x1B4
    /* 200A80 151D35D0 27A801A0 */  addiu      $t0, $sp, 0x1A0
    /* 200A84 151D35D4 ADA10000 */  sw         $at, 0x0($t5)
    /* 200A88 151D35D8 8DD90004 */  lw         $t9, 0x4($t6)
    /* 200A8C 151D35DC 240C0001 */  addiu      $t4, $zero, 0x1
    /* 200A90 151D35E0 ADB90004 */  sw         $t9, 0x4($t5)
    /* 200A94 151D35E4 8DC10008 */  lw         $at, 0x8($t6)
    /* 200A98 151D35E8 ADA10008 */  sw         $at, 0x8($t5)
    /* 200A9C 151D35EC 88C10000 */  lwl        $at, 0x0($a2)
    /* 200AA0 151D35F0 98C10003 */  lwr        $at, 0x3($a2)
    /* 200AA4 151D35F4 AD010000 */  sw         $at, 0x0($t0)
    /* 200AA8 151D35F8 88CB0004 */  lwl        $t3, 0x4($a2)
    /* 200AAC 151D35FC 98CB0007 */  lwr        $t3, 0x7($a2)
    /* 200AB0 151D3600 AD0B0004 */  sw         $t3, 0x4($t0)
    /* 200AB4 151D3604 88C10008 */  lwl        $at, 0x8($a2)
    /* 200AB8 151D3608 98C1000B */  lwr        $at, 0xB($a2)
    /* 200ABC 151D360C AD010008 */  sw         $at, 0x8($t0)
    /* 200AC0 151D3610 88CB000C */  lwl        $t3, 0xC($a2)
    /* 200AC4 151D3614 98CB000F */  lwr        $t3, 0xF($a2)
    /* 200AC8 151D3618 AD0B000C */  sw         $t3, 0xC($t0)
    /* 200ACC 151D361C 94C10010 */  lhu        $at, 0x10($a2)
    /* 200AD0 151D3620 A5010010 */  sh         $at, 0x10($t0)
    /* 200AD4 151D3624 A3AC019F */  sb         $t4, 0x19F($sp)
  .L151D3628:
    /* 200AD8 151D3628 8FA40198 */  lw         $a0, 0x198($sp)
  .L151D362C:
    /* 200ADC 151D362C 0D451724 */  jal        func_15145C90
    /* 200AE0 151D3630 AFA30058 */   sw        $v1, 0x58($sp)
    /* 200AE4 151D3634 0D42B688 */  jal        func_150ADA20
    /* 200AE8 151D3638 A3A20197 */   sb        $v0, 0x197($sp)
    /* 200AEC 151D363C 30580001 */  andi       $t8, $v0, 0x1
    /* 200AF0 151D3640 17000003 */  bnez       $t8, .L151D3650
    /* 200AF4 151D3644 8FA30058 */   lw        $v1, 0x58($sp)
    /* 200AF8 151D3648 93AF0197 */  lbu        $t7, 0x197($sp)
    /* 200AFC 151D364C 15E00003 */  bnez       $t7, .L151D365C
  .L151D3650:
    /* 200B00 151D3650 240D0001 */   addiu     $t5, $zero, 0x1
    /* 200B04 151D3654 10000002 */  b          .L151D3660
    /* 200B08 151D3658 AFAD018C */   sw        $t5, 0x18C($sp)
  .L151D365C:
    /* 200B0C 151D365C AFA0018C */  sw         $zero, 0x18C($sp)
  .L151D3660:
    /* 200B10 151D3660 24010001 */  addiu      $at, $zero, 0x1
    /* 200B14 151D3664 14610051 */  bne        $v1, $at, .L151D37AC
    /* 200B18 151D3668 8FAE018C */   lw        $t6, 0x18C($sp)
    /* 200B1C 151D366C 11C0002E */  beqz       $t6, .L151D3728
    /* 200B20 151D3670 240D00B0 */   addiu     $t5, $zero, 0xB0
    /* 200B24 151D3674 0D42B688 */  jal        func_150ADA20
    /* 200B28 151D3678 00000000 */   nop
    /* 200B2C 151D367C 24010003 */  addiu      $at, $zero, 0x3
    /* 200B30 151D3680 0041001B */  divu       $zero, $v0, $at
    /* 200B34 151D3684 3C098008 */  lui        $t1, %hi(D_80082FA0)
    /* 200B38 151D3688 8D292FA0 */  lw         $t1, %lo(D_80082FA0)($t1)
    /* 200B3C 151D368C 0000C810 */  mfhi       $t9
    /* 200B40 151D3690 272A0459 */  addiu      $t2, $t9, 0x459
    /* 200B44 151D3694 15200025 */  bnez       $t1, .L151D372C
    /* 200B48 151D3698 AFAA0180 */   sw        $t2, 0x180($sp)
    /* 200B4C 151D369C 8FA201C0 */  lw         $v0, 0x1C0($sp)
    /* 200B50 151D36A0 3C0C1001 */  lui        $t4, %hi(func_1000EC24)
    /* 200B54 151D36A4 258CEC24 */  addiu      $t4, $t4, %lo(func_1000EC24)
    /* 200B58 151D36A8 C4440000 */  lwc1       $f4, 0x0($v0)
    /* 200B5C 151D36AC C4480004 */  lwc1       $f8, 0x4($v0)
    /* 200B60 151D36B0 C4520008 */  lwc1       $f18, 0x8($v0)
    /* 200B64 151D36B4 4600218D */  trunc.w.s  $f6, $f4
    /* 200B68 151D36B8 24094000 */  addiu      $t1, $zero, 0x4000
    /* 200B6C 151D36BC 240804B0 */  addiu      $t0, $zero, 0x4B0
    /* 200B70 151D36C0 4600428D */  trunc.w.s  $f10, $f8
    /* 200B74 151D36C4 44053000 */  mfc1       $a1, $f6
    /* 200B78 151D36C8 24180028 */  addiu      $t8, $zero, 0x28
    /* 200B7C 151D36CC 4600910D */  trunc.w.s  $f4, $f18
    /* 200B80 151D36D0 44065000 */  mfc1       $a2, $f10
    /* 200B84 151D36D4 00055C00 */  sll        $t3, $a1, 16
    /* 200B88 151D36D8 000B2C03 */  sra        $a1, $t3, 16
    /* 200B8C 151D36DC 44072000 */  mfc1       $a3, $f4
    /* 200B90 151D36E0 240B0320 */  addiu      $t3, $zero, 0x320
    /* 200B94 151D36E4 00067C00 */  sll        $t7, $a2, 16
    /* 200B98 151D36E8 0007CC00 */  sll        $t9, $a3, 16
    /* 200B9C 151D36EC 00193C03 */  sra        $a3, $t9, 16
    /* 200BA0 151D36F0 000F3403 */  sra        $a2, $t7, 16
    /* 200BA4 151D36F4 AFAB0018 */  sw         $t3, 0x18($sp)
    /* 200BA8 151D36F8 AFB80020 */  sw         $t8, 0x20($sp)
    /* 200BAC 151D36FC AFA80014 */  sw         $t0, 0x14($sp)
    /* 200BB0 151D3700 AFA90010 */  sw         $t1, 0x10($sp)
    /* 200BB4 151D3704 AFA0002C */  sw         $zero, 0x2C($sp)
    /* 200BB8 151D3708 AFA00028 */  sw         $zero, 0x28($sp)
    /* 200BBC 151D370C AFA00024 */  sw         $zero, 0x24($sp)
    /* 200BC0 151D3710 AFAC001C */  sw         $t4, 0x1C($sp)
    /* 200BC4 151D3714 0C003E99 */  jal        func_1000FA64
    /* 200BC8 151D3718 97A40182 */   lhu       $a0, 0x182($sp)
    /* 200BCC 151D371C 240F0106 */  addiu      $t7, $zero, 0x106
    /* 200BD0 151D3720 10000002 */  b          .L151D372C
    /* 200BD4 151D3724 AFAF0180 */   sw        $t7, 0x180($sp)
  .L151D3728:
    /* 200BD8 151D3728 AFAD0180 */  sw         $t5, 0x180($sp)
  .L151D372C:
    /* 200BDC 151D372C 0D42B688 */  jal        func_150ADA20
    /* 200BE0 151D3730 00000000 */   nop
    /* 200BE4 151D3734 240101F4 */  addiu      $at, $zero, 0x1F4
    /* 200BE8 151D3738 0041001B */  divu       $zero, $v0, $at
    /* 200BEC 151D373C 8FA301C0 */  lw         $v1, 0x1C0($sp)
    /* 200BF0 151D3740 AFA00010 */  sw         $zero, 0x10($sp)
    /* 200BF4 151D3744 AFA00014 */  sw         $zero, 0x14($sp)
    /* 200BF8 151D3748 C4660000 */  lwc1       $f6, 0x0($v1)
    /* 200BFC 151D374C 00003810 */  mfhi       $a3
    /* 200C00 151D3750 24E7FF06 */  addiu      $a3, $a3, -0xFA
    /* 200C04 151D3754 4600320D */  trunc.w.s  $f8, $f6
    /* 200C08 151D3758 00077400 */  sll        $t6, $a3, 16
    /* 200C0C 151D375C 240F01F4 */  addiu      $t7, $zero, 0x1F4
    /* 200C10 151D3760 240D0320 */  addiu      $t5, $zero, 0x320
    /* 200C14 151D3764 44094000 */  mfc1       $t1, $f8
    /* 200C18 151D3768 000E3C03 */  sra        $a3, $t6, 16
    /* 200C1C 151D376C 00002025 */  or         $a0, $zero, $zero
    /* 200C20 151D3770 AFA90018 */  sw         $t1, 0x18($sp)
    /* 200C24 151D3774 C46A0004 */  lwc1       $f10, 0x4($v1)
    /* 200C28 151D3778 8FA50180 */  lw         $a1, 0x180($sp)
    /* 200C2C 151D377C 24066590 */  addiu      $a2, $zero, 0x6590
    /* 200C30 151D3780 4600548D */  trunc.w.s  $f18, $f10
    /* 200C34 151D3784 440B9000 */  mfc1       $t3, $f18
    /* 200C38 151D3788 00000000 */  nop
    /* 200C3C 151D378C AFAB001C */  sw         $t3, 0x1C($sp)
    /* 200C40 151D3790 C4640008 */  lwc1       $f4, 0x8($v1)
    /* 200C44 151D3794 AFAD0028 */  sw         $t5, 0x28($sp)
    /* 200C48 151D3798 AFAF0024 */  sw         $t7, 0x24($sp)
    /* 200C4C 151D379C 4600218D */  trunc.w.s  $f6, $f4
    /* 200C50 151D37A0 44183000 */  mfc1       $t8, $f6
    /* 200C54 151D37A4 0C00439E */  jal        func_10010E78
    /* 200C58 151D37A8 AFB80020 */   sw        $t8, 0x20($sp)
  .L151D37AC:
    /* 200C5C 151D37AC 0D42B69A */  jal        func_150ADA68
    /* 200C60 151D37B0 00000000 */   nop
    /* 200C64 151D37B4 3C01800E */  lui        $at, %hi(D_800DCA24)
    /* 200C68 151D37B8 C428CA24 */  lwc1       $f8, %lo(D_800DCA24)($at)
    /* 200C6C 151D37BC 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 200C70 151D37C0 3C02800E */  lui        $v0, %hi(D_800DCA20)
    /* 200C74 151D37C4 4608003C */  c.lt.s     $f0, $f8
    /* 200C78 151D37C8 240E0005 */  addiu      $t6, $zero, 0x5
    /* 200C7C 151D37CC 240A0004 */  addiu      $t2, $zero, 0x4
    /* 200C80 151D37D0 27A80114 */  addiu      $t0, $sp, 0x114
    /* 200C84 151D37D4 4500006B */  bc1f       .L151D3984
    /* 200C88 151D37D8 240D00FF */   addiu     $t5, $zero, 0xFF
    /* 200C8C 151D37DC 44810000 */  mtc1       $at, $f0
    /* 200C90 151D37E0 44801000 */  mtc1       $zero, $f2
    /* 200C94 151D37E4 2418000C */  addiu      $t8, $zero, 0xC
    /* 200C98 151D37E8 9042CA20 */  lbu        $v0, %lo(D_800DCA20)($v0)
    /* 200C9C 151D37EC 8FAB01C0 */  lw         $t3, 0x1C0($sp)
    /* 200CA0 151D37F0 240C000A */  addiu      $t4, $zero, 0xA
    /* 200CA4 151D37F4 004EC807 */  srav       $t9, $t6, $v0
    /* 200CA8 151D37F8 004A4807 */  srav       $t1, $t2, $v0
    /* 200CAC 151D37FC AFB9010C */  sw         $t9, 0x10C($sp)
    /* 200CB0 151D3800 AFA90110 */  sw         $t1, 0x110($sp)
    /* 200CB4 151D3804 8D610000 */  lw         $at, 0x0($t3)
    /* 200CB8 151D3808 24190050 */  addiu      $t9, $zero, 0x50
    /* 200CBC 151D380C 240A0003 */  addiu      $t2, $zero, 0x3
    /* 200CC0 151D3810 AD010000 */  sw         $at, 0x0($t0)
    /* 200CC4 151D3814 8D6F0004 */  lw         $t7, 0x4($t3)
    /* 200CC8 151D3818 240EFFC3 */  addiu      $t6, $zero, -0x3D
    /* 200CCC 151D381C 24090001 */  addiu      $t1, $zero, 0x1
    /* 200CD0 151D3820 AD0F0004 */  sw         $t7, 0x4($t0)
    /* 200CD4 151D3824 8D610008 */  lw         $at, 0x8($t3)
    /* 200CD8 151D3828 240B0004 */  addiu      $t3, $zero, 0x4
    /* 200CDC 151D382C 240F0002 */  addiu      $t7, $zero, 0x2
    /* 200CE0 151D3830 AD010008 */  sw         $at, 0x8($t0)
    /* 200CE4 151D3834 3C014104 */  lui        $at, (0x41040000 >> 16)
    /* 200CE8 151D3838 44815000 */  mtc1       $at, $f10
    /* 200CEC 151D383C 3C01800B */  lui        $at, %hi(D_800AB188)
    /* 200CF0 151D3840 C432B188 */  lwc1       $f18, %lo(D_800AB188)($at)
    /* 200CF4 151D3844 3C0140E0 */  lui        $at, (0x40E00000 >> 16)
    /* 200CF8 151D3848 A7B9013E */  sh         $t9, 0x13E($sp)
    /* 200CFC 151D384C AFAA0140 */  sw         $t2, 0x140($sp)
    /* 200D00 151D3850 24080001 */  addiu      $t0, $zero, 0x1
    /* 200D04 151D3854 44812000 */  mtc1       $at, $f4
    /* 200D08 151D3858 A7AD013A */  sh         $t5, 0x13A($sp)
    /* 200D0C 151D385C A7AE013C */  sh         $t6, 0x13C($sp)
    /* 200D10 151D3860 AFA90144 */  sw         $t1, 0x144($sp)
    /* 200D14 151D3864 A7B80148 */  sh         $t8, 0x148($sp)
    /* 200D18 151D3868 A7AC014A */  sh         $t4, 0x14A($sp)
    /* 200D1C 151D386C A7A8014C */  sh         $t0, 0x14C($sp)
    /* 200D20 151D3870 A3AB014E */  sb         $t3, 0x14E($sp)
    /* 200D24 151D3874 A3AF014F */  sb         $t7, 0x14F($sp)
    /* 200D28 151D3878 241900FF */  addiu      $t9, $zero, 0xFF
    /* 200D2C 151D387C 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 200D30 151D3880 3C014180 */  lui        $at, (0x41800000 >> 16)
    /* 200D34 151D3884 240D0003 */  addiu      $t5, $zero, 0x3
    /* 200D38 151D3888 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 200D3C 151D388C A3B90152 */  sb         $t9, 0x152($sp)
    /* 200D40 151D3890 A3AA0153 */  sb         $t2, 0x153($sp)
    /* 200D44 151D3894 240900FF */  addiu      $t1, $zero, 0xFF
    /* 200D48 151D3898 241800FF */  addiu      $t8, $zero, 0xFF
    /* 200D4C 151D389C 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 200D50 151D38A0 240800FF */  addiu      $t0, $zero, 0xFF
    /* 200D54 151D38A4 240B00FF */  addiu      $t3, $zero, 0xFF
    /* 200D58 151D38A8 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 200D5C 151D38AC 44813000 */  mtc1       $at, $f6
    /* 200D60 151D38B0 A3AD0150 */  sb         $t5, 0x150($sp)
    /* 200D64 151D38B4 A3AE0151 */  sb         $t6, 0x151($sp)
    /* 200D68 151D38B8 A3A90154 */  sb         $t1, 0x154($sp)
    /* 200D6C 151D38BC A3B80159 */  sb         $t8, 0x159($sp)
    /* 200D70 151D38C0 A3AC015A */  sb         $t4, 0x15A($sp)
    /* 200D74 151D38C4 A3A8015B */  sb         $t0, 0x15B($sp)
    /* 200D78 151D38C8 A3AB015C */  sb         $t3, 0x15C($sp)
    /* 200D7C 151D38CC A3AF0161 */  sb         $t7, 0x161($sp)
    /* 200D80 151D38D0 3C190020 */  lui        $t9, (0x200005 >> 16)
    /* 200D84 151D38D4 3C0A0006 */  lui        $t2, (0x60600 >> 16)
    /* 200D88 151D38D8 240D0001 */  addiu      $t5, $zero, 0x1
    /* 200D8C 151D38DC 240E0024 */  addiu      $t6, $zero, 0x24
    /* 200D90 151D38E0 37390005 */  ori        $t9, $t9, (0x200005 & 0xFFFF)
    /* 200D94 151D38E4 354A0600 */  ori        $t2, $t2, (0x60600 & 0xFFFF)
    /* 200D98 151D38E8 2409000A */  addiu      $t1, $zero, 0xA
    /* 200D9C 151D38EC 24180019 */  addiu      $t8, $zero, 0x19
    /* 200DA0 151D38F0 240C0001 */  addiu      $t4, $zero, 0x1
    /* 200DA4 151D38F4 2408FFFF */  addiu      $t0, $zero, -0x1
    /* 200DA8 151D38F8 240BFFFF */  addiu      $t3, $zero, -0x1
    /* 200DAC 151D38FC 240FFFFF */  addiu      $t7, $zero, -0x1
    /* 200DB0 151D3900 E7A20128 */  swc1       $f2, 0x128($sp)
    /* 200DB4 151D3904 E7A2012C */  swc1       $f2, 0x12C($sp)
    /* 200DB8 151D3908 A7A00138 */  sh         $zero, 0x138($sp)
    /* 200DBC 151D390C A3A00155 */  sb         $zero, 0x155($sp)
    /* 200DC0 151D3910 A3A00156 */  sb         $zero, 0x156($sp)
    /* 200DC4 151D3914 A3A00157 */  sb         $zero, 0x157($sp)
    /* 200DC8 151D3918 A3A00158 */  sb         $zero, 0x158($sp)
    /* 200DCC 151D391C A3A0015D */  sb         $zero, 0x15D($sp)
    /* 200DD0 151D3920 A3A0015E */  sb         $zero, 0x15E($sp)
    /* 200DD4 151D3924 A3A0015F */  sb         $zero, 0x15F($sp)
    /* 200DD8 151D3928 A3A00160 */  sb         $zero, 0x160($sp)
    /* 200DDC 151D392C A3A00162 */  sb         $zero, 0x162($sp)
    /* 200DE0 151D3930 A3AD0163 */  sb         $t5, 0x163($sp)
    /* 200DE4 151D3934 A3AE0164 */  sb         $t6, 0x164($sp)
    /* 200DE8 151D3938 AFB90168 */  sw         $t9, 0x168($sp)
    /* 200DEC 151D393C AFAA016C */  sw         $t2, 0x16C($sp)
    /* 200DF0 151D3940 A7A90170 */  sh         $t1, 0x170($sp)
    /* 200DF4 151D3944 A7B80172 */  sh         $t8, 0x172($sp)
    /* 200DF8 151D3948 A7AC0174 */  sh         $t4, 0x174($sp)
    /* 200DFC 151D394C A3A00176 */  sb         $zero, 0x176($sp)
    /* 200E00 151D3950 E7A00178 */  swc1       $f0, 0x178($sp)
    /* 200E04 151D3954 A3A8017C */  sb         $t0, 0x17C($sp)
    /* 200E08 151D3958 A3A0017D */  sb         $zero, 0x17D($sp)
    /* 200E0C 151D395C A3AB017E */  sb         $t3, 0x17E($sp)
    /* 200E10 151D3960 A3AF017F */  sb         $t7, 0x17F($sp)
    /* 200E14 151D3964 8FA601D4 */  lw         $a2, 0x1D4($sp)
    /* 200E18 151D3968 93A501D3 */  lbu        $a1, 0x1D3($sp)
    /* 200E1C 151D396C 27A4010C */  addiu      $a0, $sp, 0x10C
    /* 200E20 151D3970 E7AA0120 */  swc1       $f10, 0x120($sp)
    /* 200E24 151D3974 E7B20124 */  swc1       $f18, 0x124($sp)
    /* 200E28 151D3978 E7A40130 */  swc1       $f4, 0x130($sp)
    /* 200E2C 151D397C 0D454ACE */  jal        func_15152B38
    /* 200E30 151D3980 E7A60134 */   swc1      $f6, 0x134($sp)
  .L151D3984:
    /* 200E34 151D3984 8FAD0190 */  lw         $t5, 0x190($sp)
    /* 200E38 151D3988 3C0E8008 */  lui        $t6, %hi(D_80082FA0)
    /* 200E3C 151D398C 51A000D0 */  beql       $t5, $zero, .L151D3CD0
    /* 200E40 151D3990 93AD019F */   lbu       $t5, 0x19F($sp)
    /* 200E44 151D3994 8DCE2FA0 */  lw         $t6, %lo(D_80082FA0)($t6)
    /* 200E48 151D3998 8FAA01C0 */  lw         $t2, 0x1C0($sp)
    /* 200E4C 151D399C 29C10002 */  slti       $at, $t6, 0x2
    /* 200E50 151D39A0 502000CB */  beql       $at, $zero, .L151D3CD0
    /* 200E54 151D39A4 93AD019F */   lbu       $t5, 0x19F($sp)
    /* 200E58 151D39A8 8D410000 */  lw         $at, 0x0($t2)
    /* 200E5C 151D39AC 27B900B8 */  addiu      $t9, $sp, 0xB8
    /* 200E60 151D39B0 27A500A4 */  addiu      $a1, $sp, 0xA4
    /* 200E64 151D39B4 AF210000 */  sw         $at, 0x0($t9)
    /* 200E68 151D39B8 8D580004 */  lw         $t8, 0x4($t2)
    /* 200E6C 151D39BC 27A600A0 */  addiu      $a2, $sp, 0xA0
    /* 200E70 151D39C0 AF380004 */  sw         $t8, 0x4($t9)
    /* 200E74 151D39C4 8D410008 */  lw         $at, 0x8($t2)
    /* 200E78 151D39C8 AF210008 */  sw         $at, 0x8($t9)
    /* 200E7C 151D39CC 0D45165D */  jal        func_15145974
    /* 200E80 151D39D0 8FA401C4 */   lw        $a0, 0x1C4($sp)
    /* 200E84 151D39D4 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 200E88 151D39D8 44810000 */  mtc1       $at, $f0
    /* 200E8C 151D39DC 3C01800B */  lui        $at, %hi(D_800AB18C)
    /* 200E90 151D39E0 C422B18C */  lwc1       $f2, %lo(D_800AB18C)($at)
    /* 200E94 151D39E4 8FAE018C */  lw         $t6, 0x18C($sp)
    /* 200E98 151D39E8 44804000 */  mtc1       $zero, $f8
    /* 200E9C 151D39EC 8FAC0190 */  lw         $t4, 0x190($sp)
    /* 200EA0 151D39F0 240800FF */  addiu      $t0, $zero, 0xFF
    /* 200EA4 151D39F4 240B0002 */  addiu      $t3, $zero, 0x2
    /* 200EA8 151D39F8 240F000C */  addiu      $t7, $zero, 0xC
    /* 200EAC 151D39FC 240D0015 */  addiu      $t5, $zero, 0x15
    /* 200EB0 151D3A00 A3A000E8 */  sb         $zero, 0xE8($sp)
    /* 200EB4 151D3A04 AFA000EC */  sw         $zero, 0xEC($sp)
    /* 200EB8 151D3A08 A3A800F0 */  sb         $t0, 0xF0($sp)
    /* 200EBC 151D3A0C A3A000F2 */  sb         $zero, 0xF2($sp)
    /* 200EC0 151D3A10 A3A000F3 */  sb         $zero, 0xF3($sp)
    /* 200EC4 151D3A14 A3A000F4 */  sb         $zero, 0xF4($sp)
    /* 200EC8 151D3A18 A3A000F5 */  sb         $zero, 0xF5($sp)
    /* 200ECC 151D3A1C A3A000F6 */  sb         $zero, 0xF6($sp)
    /* 200ED0 151D3A20 A3A000F7 */  sb         $zero, 0xF7($sp)
    /* 200ED4 151D3A24 A3AB00F8 */  sb         $t3, 0xF8($sp)
    /* 200ED8 151D3A28 A3A000FA */  sb         $zero, 0xFA($sp)
    /* 200EDC 151D3A2C AFA000FC */  sw         $zero, 0xFC($sp)
    /* 200EE0 151D3A30 A3A00100 */  sb         $zero, 0x100($sp)
    /* 200EE4 151D3A34 A7AF0102 */  sh         $t7, 0x102($sp)
    /* 200EE8 151D3A38 A7AD0104 */  sh         $t5, 0x104($sp)
    /* 200EEC 151D3A3C E7A00090 */  swc1       $f0, 0x90($sp)
    /* 200EF0 151D3A40 E7A00094 */  swc1       $f0, 0x94($sp)
    /* 200EF4 151D3A44 E7A000AC */  swc1       $f0, 0xAC($sp)
    /* 200EF8 151D3A48 E7A000B0 */  swc1       $f0, 0xB0($sp)
    /* 200EFC 151D3A4C E7A000B4 */  swc1       $f0, 0xB4($sp)
    /* 200F00 151D3A50 E7A2009C */  swc1       $f2, 0x9C($sp)
    /* 200F04 151D3A54 E7A20098 */  swc1       $f2, 0x98($sp)
    /* 200F08 151D3A58 E7A800A8 */  swc1       $f8, 0xA8($sp)
    /* 200F0C 151D3A5C 11C0005F */  beqz       $t6, .L151D3BDC
    /* 200F10 151D3A60 A7AC00E6 */   sh        $t4, 0xE6($sp)
    /* 200F14 151D3A64 8FA401C4 */  lw         $a0, 0x1C4($sp)
    /* 200F18 151D3A68 27A50084 */  addiu      $a1, $sp, 0x84
    /* 200F1C 151D3A6C 27A60080 */  addiu      $a2, $sp, 0x80
    /* 200F20 151D3A70 0D45144A */  jal        func_15145128
    /* 200F24 151D3A74 27A7007C */   addiu     $a3, $sp, 0x7C
    /* 200F28 151D3A78 50400095 */  beql       $v0, $zero, .L151D3CD0
    /* 200F2C 151D3A7C 93AD019F */   lbu       $t5, 0x19F($sp)
    /* 200F30 151D3A80 0D42B69A */  jal        func_150ADA68
    /* 200F34 151D3A84 00000000 */   nop
    /* 200F38 151D3A88 3C014140 */  lui        $at, (0x41400000 >> 16)
    /* 200F3C 151D3A8C 44815000 */  mtc1       $at, $f10
    /* 200F40 151D3A90 3C014040 */  lui        $at, (0x40400000 >> 16)
    /* 200F44 151D3A94 44812000 */  mtc1       $at, $f4
    /* 200F48 151D3A98 460A0482 */  mul.s      $f18, $f0, $f10
    /* 200F4C 151D3A9C 46049080 */  add.s      $f2, $f18, $f4
    /* 200F50 151D3AA0 0D42B688 */  jal        func_150ADA20
    /* 200F54 151D3AA4 E7A20078 */   swc1      $f2, 0x78($sp)
    /* 200F58 151D3AA8 2401000B */  addiu      $at, $zero, 0xB
    /* 200F5C 151D3AAC 0041001B */  divu       $zero, $v0, $at
    /* 200F60 151D3AB0 C7A60084 */  lwc1       $f6, 0x84($sp)
    /* 200F64 151D3AB4 C7A20078 */  lwc1       $f2, 0x78($sp)
    /* 200F68 151D3AB8 C7B20088 */  lwc1       $f18, 0x88($sp)
    /* 200F6C 151D3ABC 46003207 */  neg.s      $f8, $f6
    /* 200F70 151D3AC0 00004810 */  mfhi       $t1
    /* 200F74 151D3AC4 46024282 */  mul.s      $f10, $f8, $f2
    /* 200F78 151D3AC8 C7A8008C */  lwc1       $f8, 0x8C($sp)
    /* 200F7C 151D3ACC 46009107 */  neg.s      $f4, $f18
    /* 200F80 151D3AD0 2539001E */  addiu      $t9, $t1, 0x1E
    /* 200F84 151D3AD4 46022182 */  mul.s      $f6, $f4, $f2
    /* 200F88 151D3AD8 A7B900E4 */  sh         $t9, 0xE4($sp)
    /* 200F8C 151D3ADC E7AA00C4 */  swc1       $f10, 0xC4($sp)
    /* 200F90 151D3AE0 46004287 */  neg.s      $f10, $f8
    /* 200F94 151D3AE4 46025482 */  mul.s      $f18, $f10, $f2
    /* 200F98 151D3AE8 E7A600C8 */  swc1       $f6, 0xC8($sp)
    /* 200F9C 151D3AEC 0D42B69A */  jal        func_150ADA68
    /* 200FA0 151D3AF0 E7B200CC */   swc1      $f18, 0xCC($sp)
    /* 200FA4 151D3AF4 3C01800B */  lui        $at, %hi(D_800AB190)
    /* 200FA8 151D3AF8 C424B190 */  lwc1       $f4, %lo(D_800AB190)($at)
    /* 200FAC 151D3AFC 3C01800B */  lui        $at, %hi(D_800AB194)
    /* 200FB0 151D3B00 C428B194 */  lwc1       $f8, %lo(D_800AB194)($at)
    /* 200FB4 151D3B04 46040182 */  mul.s      $f6, $f0, $f4
    /* 200FB8 151D3B08 3C01800B */  lui        $at, %hi(D_800AB198)
    /* 200FBC 151D3B0C C432B198 */  lwc1       $f18, %lo(D_800AB198)($at)
    /* 200FC0 151D3B10 46083280 */  add.s      $f10, $f6, $f8
    /* 200FC4 151D3B14 46125102 */  mul.s      $f4, $f10, $f18
    /* 200FC8 151D3B18 0D42B69A */  jal        func_150ADA68
    /* 200FCC 151D3B1C E7A400D0 */   swc1      $f4, 0xD0($sp)
    /* 200FD0 151D3B20 3C01800B */  lui        $at, %hi(D_800AB19C)
    /* 200FD4 151D3B24 C426B19C */  lwc1       $f6, %lo(D_800AB19C)($at)
    /* 200FD8 151D3B28 3C01800B */  lui        $at, %hi(D_800AB1A0)
    /* 200FDC 151D3B2C C42AB1A0 */  lwc1       $f10, %lo(D_800AB1A0)($at)
    /* 200FE0 151D3B30 46060202 */  mul.s      $f8, $f0, $f6
    /* 200FE4 151D3B34 3C01800B */  lui        $at, %hi(D_800AB1A4)
    /* 200FE8 151D3B38 C424B1A4 */  lwc1       $f4, %lo(D_800AB1A4)($at)
    /* 200FEC 151D3B3C 460A4480 */  add.s      $f18, $f8, $f10
    /* 200FF0 151D3B40 46049182 */  mul.s      $f6, $f18, $f4
    /* 200FF4 151D3B44 0D42B69A */  jal        func_150ADA68
    /* 200FF8 151D3B48 E7A600D4 */   swc1      $f6, 0xD4($sp)
    /* 200FFC 151D3B4C 3C01800B */  lui        $at, %hi(D_800AB1A8)
    /* 201000 151D3B50 C428B1A8 */  lwc1       $f8, %lo(D_800AB1A8)($at)
    /* 201004 151D3B54 3C01800B */  lui        $at, %hi(D_800AB1AC)
    /* 201008 151D3B58 C432B1AC */  lwc1       $f18, %lo(D_800AB1AC)($at)
    /* 20100C 151D3B5C 46080282 */  mul.s      $f10, $f0, $f8
    /* 201010 151D3B60 3C01800B */  lui        $at, %hi(D_800AB1B0)
    /* 201014 151D3B64 C426B1B0 */  lwc1       $f6, %lo(D_800AB1B0)($at)
    /* 201018 151D3B68 46125100 */  add.s      $f4, $f10, $f18
    /* 20101C 151D3B6C 46062202 */  mul.s      $f8, $f4, $f6
    /* 201020 151D3B70 0D42B69A */  jal        func_150ADA68
    /* 201024 151D3B74 E7A800D8 */   swc1      $f8, 0xD8($sp)
    /* 201028 151D3B78 3C01800B */  lui        $at, %hi(D_800AB1B4)
    /* 20102C 151D3B7C C42AB1B4 */  lwc1       $f10, %lo(D_800AB1B4)($at)
    /* 201030 151D3B80 3C01C43A */  lui        $at, (0xC43A0000 >> 16)
    /* 201034 151D3B84 44812000 */  mtc1       $at, $f4
    /* 201038 151D3B88 460A0482 */  mul.s      $f18, $f0, $f10
    /* 20103C 151D3B8C 3C01800B */  lui        $at, %hi(D_800AB1B8)
    /* 201040 151D3B90 C428B1B8 */  lwc1       $f8, %lo(D_800AB1B8)($at)
    /* 201044 151D3B94 93AC01D3 */  lbu        $t4, 0x1D3($sp)
    /* 201048 151D3B98 8FA801D4 */  lw         $t0, 0x1D4($sp)
    /* 20104C 151D3B9C 240A39E8 */  addiu      $t2, $zero, 0x39E8
    /* 201050 151D3BA0 24180008 */  addiu      $t8, $zero, 0x8
    /* 201054 151D3BA4 46049180 */  add.s      $f6, $f18, $f4
    /* 201058 151D3BA8 AFAA00E0 */  sw         $t2, 0xE0($sp)
    /* 20105C 151D3BAC A3B800F1 */  sb         $t8, 0xF1($sp)
    /* 201060 151D3BB0 27A40090 */  addiu      $a0, $sp, 0x90
    /* 201064 151D3BB4 46083282 */  mul.s      $f10, $f6, $f8
    /* 201068 151D3BB8 24050003 */  addiu      $a1, $zero, 0x3
    /* 20106C 151D3BBC 240600FF */  addiu      $a2, $zero, 0xFF
    /* 201070 151D3BC0 00003825 */  or         $a3, $zero, $zero
    /* 201074 151D3BC4 AFAC0010 */  sw         $t4, 0x10($sp)
    /* 201078 151D3BC8 AFA80014 */  sw         $t0, 0x14($sp)
    /* 20107C 151D3BCC 0D44CA93 */  jal        func_15132A4C
    /* 201080 151D3BD0 E7AA00DC */   swc1      $f10, 0xDC($sp)
    /* 201084 151D3BD4 1000003E */  b          .L151D3CD0
    /* 201088 151D3BD8 93AD019F */   lbu       $t5, 0x19F($sp)
  .L151D3BDC:
    /* 20108C 151D3BDC 0D42B688 */  jal        func_150ADA20
    /* 201090 151D3BE0 00000000 */   nop
    /* 201094 151D3BE4 44809000 */  mtc1       $zero, $f18
    /* 201098 151D3BE8 304B000F */  andi       $t3, $v0, 0xF
    /* 20109C 151D3BEC 256F0014 */  addiu      $t7, $t3, 0x14
    /* 2010A0 151D3BF0 A7AF0068 */  sh         $t7, 0x68($sp)
    /* 2010A4 151D3BF4 0D42B69A */  jal        func_150ADA68
    /* 2010A8 151D3BF8 E7B2006C */   swc1      $f18, 0x6C($sp)
    /* 2010AC 151D3BFC 3C01800B */  lui        $at, %hi(D_800AB1BC)
    /* 2010B0 151D3C00 C422B1BC */  lwc1       $f2, %lo(D_800AB1BC)($at)
    /* 2010B4 151D3C04 3C01800B */  lui        $at, %hi(D_800AB1C0)
    /* 2010B8 151D3C08 C428B1C0 */  lwc1       $f8, %lo(D_800AB1C0)($at)
    /* 2010BC 151D3C0C 46020102 */  mul.s      $f4, $f0, $f2
    /* 2010C0 151D3C10 46022180 */  add.s      $f6, $f4, $f2
    /* 2010C4 151D3C14 46083282 */  mul.s      $f10, $f6, $f8
    /* 2010C8 151D3C18 0D42B69A */  jal        func_150ADA68
    /* 2010CC 151D3C1C E7AA0070 */   swc1      $f10, 0x70($sp)
    /* 2010D0 151D3C20 3C01800B */  lui        $at, %hi(D_800AB1C4)
    /* 2010D4 151D3C24 C432B1C4 */  lwc1       $f18, %lo(D_800AB1C4)($at)
    /* 2010D8 151D3C28 3C01457A */  lui        $at, (0x457A0000 >> 16)
    /* 2010DC 151D3C2C 44813000 */  mtc1       $at, $f6
    /* 2010E0 151D3C30 46120102 */  mul.s      $f4, $f0, $f18
    /* 2010E4 151D3C34 3C01800B */  lui        $at, %hi(D_800AB1C8)
    /* 2010E8 151D3C38 C42AB1C8 */  lwc1       $f10, %lo(D_800AB1C8)($at)
    /* 2010EC 151D3C3C 44801000 */  mtc1       $zero, $f2
    /* 2010F0 151D3C40 240D012C */  addiu      $t5, $zero, 0x12C
    /* 2010F4 151D3C44 A7AD00E4 */  sh         $t5, 0xE4($sp)
    /* 2010F8 151D3C48 27A900A0 */  addiu      $t1, $sp, 0xA0
    /* 2010FC 151D3C4C 46062200 */  add.s      $f8, $f4, $f6
    /* 201100 151D3C50 E7A200C4 */  swc1       $f2, 0xC4($sp)
    /* 201104 151D3C54 E7A200C8 */  swc1       $f2, 0xC8($sp)
    /* 201108 151D3C58 E7A200CC */  swc1       $f2, 0xCC($sp)
    /* 20110C 151D3C5C 460A4482 */  mul.s      $f18, $f8, $f10
    /* 201110 151D3C60 27AE00D0 */  addiu      $t6, $sp, 0xD0
    /* 201114 151D3C64 240C3980 */  addiu      $t4, $zero, 0x3980
    /* 201118 151D3C68 2408000C */  addiu      $t0, $zero, 0xC
    /* 20111C 151D3C6C 27A40090 */  addiu      $a0, $sp, 0x90
    /* 201120 151D3C70 24050003 */  addiu      $a1, $zero, 0x3
    /* 201124 151D3C74 240600FF */  addiu      $a2, $zero, 0xFF
    /* 201128 151D3C78 E7B20074 */  swc1       $f18, 0x74($sp)
    /* 20112C 151D3C7C 8D210000 */  lw         $at, 0x0($t1)
    /* 201130 151D3C80 24070010 */  addiu      $a3, $zero, 0x10
    /* 201134 151D3C84 ADC10000 */  sw         $at, 0x0($t6)
    /* 201138 151D3C88 8D380004 */  lw         $t8, 0x4($t1)
    /* 20113C 151D3C8C ADD80004 */  sw         $t8, 0x4($t6)
    /* 201140 151D3C90 8D210008 */  lw         $at, 0x8($t1)
    /* 201144 151D3C94 ADC10008 */  sw         $at, 0x8($t6)
    /* 201148 151D3C98 8FAF01D4 */  lw         $t7, 0x1D4($sp)
    /* 20114C 151D3C9C 93AB01D3 */  lbu        $t3, 0x1D3($sp)
    /* 201150 151D3CA0 AFAC00E0 */  sw         $t4, 0xE0($sp)
    /* 201154 151D3CA4 A3A800F1 */  sb         $t0, 0xF1($sp)
    /* 201158 151D3CA8 E7A200DC */  swc1       $f2, 0xDC($sp)
    /* 20115C 151D3CAC AFAF0014 */  sw         $t7, 0x14($sp)
    /* 201160 151D3CB0 0D44CA93 */  jal        func_15132A4C
    /* 201164 151D3CB4 AFAB0010 */   sw        $t3, 0x10($sp)
    /* 201168 151D3CB8 10400004 */  beqz       $v0, .L151D3CCC
    /* 20116C 151D3CBC 24440170 */   addiu     $a0, $v0, 0x170
    /* 201170 151D3CC0 27A50068 */  addiu      $a1, $sp, 0x68
    /* 201174 151D3CC4 0C008BB0 */  jal        memcpy
    /* 201178 151D3CC8 24060010 */   addiu     $a2, $zero, 0x10
  .L151D3CCC:
    /* 20117C 151D3CCC 93AD019F */  lbu        $t5, 0x19F($sp)
  .L151D3CD0:
    /* 201180 151D3CD0 93AA0197 */  lbu        $t2, 0x197($sp)
    /* 201184 151D3CD4 51A0001B */  beql       $t5, $zero, .L151D3D44
    /* 201188 151D3CD8 8FBF0044 */   lw        $ra, 0x44($sp)
    /* 20118C 151D3CDC 51400019 */  beql       $t2, $zero, .L151D3D44
    /* 201190 151D3CE0 8FBF0044 */   lw        $ra, 0x44($sp)
    /* 201194 151D3CE4 0D42B69A */  jal        func_150ADA68
    /* 201198 151D3CE8 00000000 */   nop
    /* 20119C 151D3CEC 3C0141A0 */  lui        $at, (0x41A00000 >> 16)
    /* 2011A0 151D3CF0 44812000 */  mtc1       $at, $f4
    /* 2011A4 151D3CF4 3C014170 */  lui        $at, (0x41700000 >> 16)
    /* 2011A8 151D3CF8 44814000 */  mtc1       $at, $f8
    /* 2011AC 151D3CFC 46040182 */  mul.s      $f6, $f0, $f4
    /* 2011B0 151D3D00 93B801D3 */  lbu        $t8, 0x1D3($sp)
    /* 2011B4 151D3D04 8FAC01D4 */  lw         $t4, 0x1D4($sp)
    /* 2011B8 151D3D08 2419012C */  addiu      $t9, $zero, 0x12C
    /* 2011BC 151D3D0C 240E0001 */  addiu      $t6, $zero, 0x1
    /* 2011C0 151D3D10 24090001 */  addiu      $t1, $zero, 0x1
    /* 2011C4 151D3D14 AFA90018 */  sw         $t1, 0x18($sp)
    /* 2011C8 151D3D18 AFAE0014 */  sw         $t6, 0x14($sp)
    /* 2011CC 151D3D1C AFB90010 */  sw         $t9, 0x10($sp)
    /* 2011D0 151D3D20 240500FF */  addiu      $a1, $zero, 0xFF
    /* 2011D4 151D3D24 27A601A0 */  addiu      $a2, $sp, 0x1A0
    /* 2011D8 151D3D28 27A701B4 */  addiu      $a3, $sp, 0x1B4
    /* 2011DC 151D3D2C AFA0001C */  sw         $zero, 0x1C($sp)
    /* 2011E0 151D3D30 46083300 */  add.s      $f12, $f6, $f8
    /* 2011E4 151D3D34 AFB80020 */  sw         $t8, 0x20($sp)
    /* 2011E8 151D3D38 0D440A48 */  jal        func_15102920
    /* 2011EC 151D3D3C AFAC0024 */   sw        $t4, 0x24($sp)
  .L151D3D40:
    /* 2011F0 151D3D40 8FBF0044 */  lw         $ra, 0x44($sp)
  .L151D3D44:
    /* 2011F4 151D3D44 27BD01C0 */  addiu      $sp, $sp, 0x1C0
    /* 2011F8 151D3D48 03E00008 */  jr         $ra
    /* 2011FC 151D3D4C 00000000 */   nop
endlabel func_151D3480
