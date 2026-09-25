glabel func_151C36D8
    /* 1F0B88 151C36D8 27BDFEC0 */  addiu      $sp, $sp, -0x140
    /* 1F0B8C 151C36DC AFB00038 */  sw         $s0, 0x38($sp)
    /* 1F0B90 151C36E0 00808025 */  or         $s0, $a0, $zero
    /* 1F0B94 151C36E4 AFBF003C */  sw         $ra, 0x3C($sp)
    /* 1F0B98 151C36E8 AFA50144 */  sw         $a1, 0x144($sp)
    /* 1F0B9C 151C36EC AFA60148 */  sw         $a2, 0x148($sp)
    /* 1F0BA0 151C36F0 240E0008 */  addiu      $t6, $zero, 0x8
    /* 1F0BA4 151C36F4 240F0006 */  addiu      $t7, $zero, 0x6
    /* 1F0BA8 151C36F8 AFAE00CC */  sw         $t6, 0xCC($sp)
    /* 1F0BAC 151C36FC AFAF00D0 */  sw         $t7, 0xD0($sp)
    /* 1F0BB0 151C3700 8E010000 */  lw         $at, 0x0($s0)
    /* 1F0BB4 151C3704 27B800D4 */  addiu      $t8, $sp, 0xD4
    /* 1F0BB8 151C3708 240BFFC0 */  addiu      $t3, $zero, -0x40
    /* 1F0BBC 151C370C AF010000 */  sw         $at, 0x0($t8)
    /* 1F0BC0 151C3710 8E090004 */  lw         $t1, 0x4($s0)
    /* 1F0BC4 151C3714 240C0050 */  addiu      $t4, $zero, 0x50
    /* 1F0BC8 151C3718 240D0003 */  addiu      $t5, $zero, 0x3
    /* 1F0BCC 151C371C AF090004 */  sw         $t1, 0x4($t8)
    /* 1F0BD0 151C3720 8E010008 */  lw         $at, 0x8($s0)
    /* 1F0BD4 151C3724 240E000F */  addiu      $t6, $zero, 0xF
    /* 1F0BD8 151C3728 240F000A */  addiu      $t7, $zero, 0xA
    /* 1F0BDC 151C372C AF010008 */  sw         $at, 0x8($t8)
    /* 1F0BE0 151C3730 3C01800B */  lui        $at, %hi(D_800AAA54)
    /* 1F0BE4 151C3734 C424AA54 */  lwc1       $f4, %lo(D_800AAA54)($at)
    /* 1F0BE8 151C3738 3C01800B */  lui        $at, %hi(D_800AAA58)
    /* 1F0BEC 151C373C C426AA58 */  lwc1       $f6, %lo(D_800AAA58)($at)
    /* 1F0BF0 151C3740 3C01800B */  lui        $at, %hi(D_800AAA5C)
    /* 1F0BF4 151C3744 C428AA5C */  lwc1       $f8, %lo(D_800AAA5C)($at)
    /* 1F0BF8 151C3748 3C01800B */  lui        $at, %hi(D_800AAA60)
    /* 1F0BFC 151C374C C42AAA60 */  lwc1       $f10, %lo(D_800AAA60)($at)
    /* 1F0C00 151C3750 3C014120 */  lui        $at, (0x41200000 >> 16)
    /* 1F0C04 151C3754 44818000 */  mtc1       $at, $f16
    /* 1F0C08 151C3758 3C014100 */  lui        $at, (0x41000000 >> 16)
    /* 1F0C0C 151C375C A7AB00FC */  sh         $t3, 0xFC($sp)
    /* 1F0C10 151C3760 A7AC00FE */  sh         $t4, 0xFE($sp)
    /* 1F0C14 151C3764 24080001 */  addiu      $t0, $zero, 0x1
    /* 1F0C18 151C3768 24190004 */  addiu      $t9, $zero, 0x4
    /* 1F0C1C 151C376C 24180002 */  addiu      $t8, $zero, 0x2
    /* 1F0C20 151C3770 44819000 */  mtc1       $at, $f18
    /* 1F0C24 151C3774 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 1F0C28 151C3778 AFAD0100 */  sw         $t5, 0x100($sp)
    /* 1F0C2C 151C377C A7AE0108 */  sh         $t6, 0x108($sp)
    /* 1F0C30 151C3780 A7AF010A */  sh         $t7, 0x10A($sp)
    /* 1F0C34 151C3784 A7A8010C */  sh         $t0, 0x10C($sp)
    /* 1F0C38 151C3788 A3B9010E */  sb         $t9, 0x10E($sp)
    /* 1F0C3C 151C378C A3B8010F */  sb         $t8, 0x10F($sp)
    /* 1F0C40 151C3790 240B00FF */  addiu      $t3, $zero, 0xFF
    /* 1F0C44 151C3794 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 1F0C48 151C3798 A3AB0112 */  sb         $t3, 0x112($sp)
    /* 1F0C4C 151C379C A3AC0113 */  sb         $t4, 0x113($sp)
    /* 1F0C50 151C37A0 240D00FF */  addiu      $t5, $zero, 0xFF
    /* 1F0C54 151C37A4 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 1F0C58 151C37A8 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 1F0C5C 151C37AC 240800FF */  addiu      $t0, $zero, 0xFF
    /* 1F0C60 151C37B0 241900FF */  addiu      $t9, $zero, 0xFF
    /* 1F0C64 151C37B4 241800FF */  addiu      $t8, $zero, 0xFF
    /* 1F0C68 151C37B8 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 1F0C6C 151C37BC E7A400E0 */  swc1       $f4, 0xE0($sp)
    /* 1F0C70 151C37C0 44812000 */  mtc1       $at, $f4
    /* 1F0C74 151C37C4 A7AA00FA */  sh         $t2, 0xFA($sp)
    /* 1F0C78 151C37C8 A3AA0111 */  sb         $t2, 0x111($sp)
    /* 1F0C7C 151C37CC A3AD0114 */  sb         $t5, 0x114($sp)
    /* 1F0C80 151C37D0 A3AE0119 */  sb         $t6, 0x119($sp)
    /* 1F0C84 151C37D4 A3AF011A */  sb         $t7, 0x11A($sp)
    /* 1F0C88 151C37D8 A3A8011B */  sb         $t0, 0x11B($sp)
    /* 1F0C8C 151C37DC A3B9011C */  sb         $t9, 0x11C($sp)
    /* 1F0C90 151C37E0 A3B80121 */  sb         $t8, 0x121($sp)
    /* 1F0C94 151C37E4 3C0B0020 */  lui        $t3, (0x200005 >> 16)
    /* 1F0C98 151C37E8 3C0C0006 */  lui        $t4, (0x60600 >> 16)
    /* 1F0C9C 151C37EC 24090003 */  addiu      $t1, $zero, 0x3
    /* 1F0CA0 151C37F0 240A0024 */  addiu      $t2, $zero, 0x24
    /* 1F0CA4 151C37F4 356B0005 */  ori        $t3, $t3, (0x200005 & 0xFFFF)
    /* 1F0CA8 151C37F8 358C0600 */  ori        $t4, $t4, (0x60600 & 0xFFFF)
    /* 1F0CAC 151C37FC 240D0008 */  addiu      $t5, $zero, 0x8
    /* 1F0CB0 151C3800 240E001F */  addiu      $t6, $zero, 0x1F
    /* 1F0CB4 151C3804 240F0001 */  addiu      $t7, $zero, 0x1
    /* 1F0CB8 151C3808 2408FFFF */  addiu      $t0, $zero, -0x1
    /* 1F0CBC 151C380C 2419FFFF */  addiu      $t9, $zero, -0x1
    /* 1F0CC0 151C3810 2418FFFF */  addiu      $t8, $zero, -0x1
    /* 1F0CC4 151C3814 A7A000F8 */  sh         $zero, 0xF8($sp)
    /* 1F0CC8 151C3818 AFA00104 */  sw         $zero, 0x104($sp)
    /* 1F0CCC 151C381C A3A90110 */  sb         $t1, 0x110($sp)
    /* 1F0CD0 151C3820 A3A00115 */  sb         $zero, 0x115($sp)
    /* 1F0CD4 151C3824 A3A00116 */  sb         $zero, 0x116($sp)
    /* 1F0CD8 151C3828 A3A00117 */  sb         $zero, 0x117($sp)
    /* 1F0CDC 151C382C A3A00118 */  sb         $zero, 0x118($sp)
    /* 1F0CE0 151C3830 A3A0011D */  sb         $zero, 0x11D($sp)
    /* 1F0CE4 151C3834 A3A0011E */  sb         $zero, 0x11E($sp)
    /* 1F0CE8 151C3838 A3A0011F */  sb         $zero, 0x11F($sp)
    /* 1F0CEC 151C383C A3A00120 */  sb         $zero, 0x120($sp)
    /* 1F0CF0 151C3840 A3A00122 */  sb         $zero, 0x122($sp)
    /* 1F0CF4 151C3844 A3A90123 */  sb         $t1, 0x123($sp)
    /* 1F0CF8 151C3848 A3AA0124 */  sb         $t2, 0x124($sp)
    /* 1F0CFC 151C384C AFAB0128 */  sw         $t3, 0x128($sp)
    /* 1F0D00 151C3850 AFAC012C */  sw         $t4, 0x12C($sp)
    /* 1F0D04 151C3854 A7AD0130 */  sh         $t5, 0x130($sp)
    /* 1F0D08 151C3858 A7AE0132 */  sh         $t6, 0x132($sp)
    /* 1F0D0C 151C385C A7AF0134 */  sh         $t7, 0x134($sp)
    /* 1F0D10 151C3860 A3A00136 */  sb         $zero, 0x136($sp)
    /* 1F0D14 151C3864 A3A8013C */  sb         $t0, 0x13C($sp)
    /* 1F0D18 151C3868 A3A0013D */  sb         $zero, 0x13D($sp)
    /* 1F0D1C 151C386C A3B9013E */  sb         $t9, 0x13E($sp)
    /* 1F0D20 151C3870 A3B8013F */  sb         $t8, 0x13F($sp)
    /* 1F0D24 151C3874 8FA60148 */  lw         $a2, 0x148($sp)
    /* 1F0D28 151C3878 93A50147 */  lbu        $a1, 0x147($sp)
    /* 1F0D2C 151C387C 27A400CC */  addiu      $a0, $sp, 0xCC
    /* 1F0D30 151C3880 E7A600E4 */  swc1       $f6, 0xE4($sp)
    /* 1F0D34 151C3884 E7A800E8 */  swc1       $f8, 0xE8($sp)
    /* 1F0D38 151C3888 E7AA00EC */  swc1       $f10, 0xEC($sp)
    /* 1F0D3C 151C388C E7B000F0 */  swc1       $f16, 0xF0($sp)
    /* 1F0D40 151C3890 E7B200F4 */  swc1       $f18, 0xF4($sp)
    /* 1F0D44 151C3894 0D454ACE */  jal        func_15152B38
    /* 1F0D48 151C3898 E7A40138 */   swc1      $f4, 0x138($sp)
    /* 1F0D4C 151C389C 3C0B0020 */  lui        $t3, (0x200005 >> 16)
    /* 1F0D50 151C38A0 2409002B */  addiu      $t1, $zero, 0x2B
    /* 1F0D54 151C38A4 240A4403 */  addiu      $t2, $zero, 0x4403
    /* 1F0D58 151C38A8 356B0005 */  ori        $t3, $t3, (0x200005 & 0xFFFF)
    /* 1F0D5C 151C38AC 3C0C0002 */  lui        $t4, (0x20000 >> 16)
    /* 1F0D60 151C38B0 A3A90079 */  sb         $t1, 0x79($sp)
    /* 1F0D64 151C38B4 A7AA0064 */  sh         $t2, 0x64($sp)
    /* 1F0D68 151C38B8 AFAB005C */  sw         $t3, 0x5C($sp)
    /* 1F0D6C 151C38BC 0D42B688 */  jal        func_150ADA20
    /* 1F0D70 151C38C0 AFAC0060 */   sw        $t4, 0x60($sp)
    /* 1F0D74 151C38C4 24010005 */  addiu      $at, $zero, 0x5
    /* 1F0D78 151C38C8 0041001B */  divu       $zero, $v0, $at
    /* 1F0D7C 151C38CC 00006810 */  mfhi       $t5
    /* 1F0D80 151C38D0 25AE0004 */  addiu      $t6, $t5, 0x4
    /* 1F0D84 151C38D4 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 1F0D88 151C38D8 240800FF */  addiu      $t0, $zero, 0xFF
    /* 1F0D8C 151C38DC 241900FF */  addiu      $t9, $zero, 0xFF
    /* 1F0D90 151C38E0 241800FF */  addiu      $t8, $zero, 0xFF
    /* 1F0D94 151C38E4 240900FF */  addiu      $t1, $zero, 0xFF
    /* 1F0D98 151C38E8 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 1F0D9C 151C38EC 240B00FF */  addiu      $t3, $zero, 0xFF
    /* 1F0DA0 151C38F0 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 1F0DA4 151C38F4 240D00FF */  addiu      $t5, $zero, 0xFF
    /* 1F0DA8 151C38F8 A7AE0066 */  sh         $t6, 0x66($sp)
    /* 1F0DAC 151C38FC AFA00068 */  sw         $zero, 0x68($sp)
    /* 1F0DB0 151C3900 AFA0006C */  sw         $zero, 0x6C($sp)
    /* 1F0DB4 151C3904 A3AF0070 */  sb         $t7, 0x70($sp)
    /* 1F0DB8 151C3908 A3A80071 */  sb         $t0, 0x71($sp)
    /* 1F0DBC 151C390C A3B90072 */  sb         $t9, 0x72($sp)
    /* 1F0DC0 151C3910 A3B80073 */  sb         $t8, 0x73($sp)
    /* 1F0DC4 151C3914 A3A90074 */  sb         $t1, 0x74($sp)
    /* 1F0DC8 151C3918 A3AA0075 */  sb         $t2, 0x75($sp)
    /* 1F0DCC 151C391C A3AB0076 */  sb         $t3, 0x76($sp)
    /* 1F0DD0 151C3920 A3AC0077 */  sb         $t4, 0x77($sp)
    /* 1F0DD4 151C3924 0D42B69A */  jal        func_150ADA68
    /* 1F0DD8 151C3928 A3AD0078 */   sb        $t5, 0x78($sp)
    /* 1F0DDC 151C392C 3C014270 */  lui        $at, (0x42700000 >> 16)
    /* 1F0DE0 151C3930 44813000 */  mtc1       $at, $f6
    /* 1F0DE4 151C3934 3C0142A0 */  lui        $at, (0x42A00000 >> 16)
    /* 1F0DE8 151C3938 44815000 */  mtc1       $at, $f10
    /* 1F0DEC 151C393C 46060202 */  mul.s      $f8, $f0, $f6
    /* 1F0DF0 151C3940 27AE008C */  addiu      $t6, $sp, 0x8C
    /* 1F0DF4 151C3944 44801000 */  mtc1       $zero, $f2
    /* 1F0DF8 151C3948 24180002 */  addiu      $t8, $zero, 0x2
    /* 1F0DFC 151C394C 2409007F */  addiu      $t1, $zero, 0x7F
    /* 1F0E00 151C3950 240A0001 */  addiu      $t2, $zero, 0x1
    /* 1F0E04 151C3954 460A4400 */  add.s      $f16, $f8, $f10
    /* 1F0E08 151C3958 E7B00088 */  swc1       $f16, 0x88($sp)
    /* 1F0E0C 151C395C E7B00084 */  swc1       $f16, 0x84($sp)
    /* 1F0E10 151C3960 8E010000 */  lw         $at, 0x0($s0)
    /* 1F0E14 151C3964 ADC10000 */  sw         $at, 0x0($t6)
    /* 1F0E18 151C3968 8E190004 */  lw         $t9, 0x4($s0)
    /* 1F0E1C 151C396C ADD90004 */  sw         $t9, 0x4($t6)
    /* 1F0E20 151C3970 8E010008 */  lw         $at, 0x8($s0)
    /* 1F0E24 151C3974 ADC10008 */  sw         $at, 0x8($t6)
    /* 1F0E28 151C3978 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 1F0E2C 151C397C 44819000 */  mtc1       $at, $f18
    /* 1F0E30 151C3980 A7B8007A */  sh         $t8, 0x7A($sp)
    /* 1F0E34 151C3984 A7A9007C */  sh         $t1, 0x7C($sp)
    /* 1F0E38 151C3988 A7AA007E */  sh         $t2, 0x7E($sp)
    /* 1F0E3C 151C398C E7A20098 */  swc1       $f2, 0x98($sp)
    /* 1F0E40 151C3990 E7A2009C */  swc1       $f2, 0x9C($sp)
    /* 1F0E44 151C3994 E7A200A0 */  swc1       $f2, 0xA0($sp)
    /* 1F0E48 151C3998 E7A200A4 */  swc1       $f2, 0xA4($sp)
    /* 1F0E4C 151C399C E7A200A8 */  swc1       $f2, 0xA8($sp)
    /* 1F0E50 151C39A0 E7A200AC */  swc1       $f2, 0xAC($sp)
    /* 1F0E54 151C39A4 E7A200B0 */  swc1       $f2, 0xB0($sp)
    /* 1F0E58 151C39A8 0D42B688 */  jal        func_150ADA20
    /* 1F0E5C 151C39AC E7B20080 */   swc1      $f18, 0x80($sp)
    /* 1F0E60 151C39B0 304B0001 */  andi       $t3, $v0, 0x1
    /* 1F0E64 151C39B4 11600003 */  beqz       $t3, .L151C39C4
    /* 1F0E68 151C39B8 00001825 */   or        $v1, $zero, $zero
    /* 1F0E6C 151C39BC 10000001 */  b          .L151C39C4
    /* 1F0E70 151C39C0 24030040 */   addiu     $v1, $zero, 0x40
  .L151C39C4:
    /* 1F0E74 151C39C4 0D42B688 */  jal        func_150ADA20
    /* 1F0E78 151C39C8 AFA30040 */   sw        $v1, 0x40($sp)
    /* 1F0E7C 151C39CC 304C0001 */  andi       $t4, $v0, 0x1
    /* 1F0E80 151C39D0 11800003 */  beqz       $t4, .L151C39E0
    /* 1F0E84 151C39D4 8FA30040 */   lw        $v1, 0x40($sp)
    /* 1F0E88 151C39D8 10000002 */  b          .L151C39E4
    /* 1F0E8C 151C39DC 24020080 */   addiu     $v0, $zero, 0x80
  .L151C39E0:
    /* 1F0E90 151C39E0 00001025 */  or         $v0, $zero, $zero
  .L151C39E4:
    /* 1F0E94 151C39E4 344D0001 */  ori        $t5, $v0, 0x1
    /* 1F0E98 151C39E8 01A37025 */  or         $t6, $t5, $v1
    /* 1F0E9C 151C39EC 93A80147 */  lbu        $t0, 0x147($sp)
    /* 1F0EA0 151C39F0 8FAF0148 */  lw         $t7, 0x148($sp)
    /* 1F0EA4 151C39F4 35D9C200 */  ori        $t9, $t6, 0xC200
    /* 1F0EA8 151C39F8 24180006 */  addiu      $t8, $zero, 0x6
    /* 1F0EAC 151C39FC 24090006 */  addiu      $t1, $zero, 0x6
    /* 1F0EB0 151C3A00 240AFFFF */  addiu      $t2, $zero, -0x1
    /* 1F0EB4 151C3A04 240BFFFF */  addiu      $t3, $zero, -0x1
    /* 1F0EB8 151C3A08 240CFFFF */  addiu      $t4, $zero, -0x1
    /* 1F0EBC 151C3A0C 240D0004 */  addiu      $t5, $zero, 0x4
    /* 1F0EC0 151C3A10 AFB900B4 */  sw         $t9, 0xB4($sp)
    /* 1F0EC4 151C3A14 A3B800BC */  sb         $t8, 0xBC($sp)
    /* 1F0EC8 151C3A18 A3A900BD */  sb         $t1, 0xBD($sp)
    /* 1F0ECC 151C3A1C A3AA00BE */  sb         $t2, 0xBE($sp)
    /* 1F0ED0 151C3A20 A3AB00BF */  sb         $t3, 0xBF($sp)
    /* 1F0ED4 151C3A24 A3AC00C0 */  sb         $t4, 0xC0($sp)
    /* 1F0ED8 151C3A28 A3AD00C1 */  sb         $t5, 0xC1($sp)
    /* 1F0EDC 151C3A2C 27A4005C */  addiu      $a0, $sp, 0x5C
    /* 1F0EE0 151C3A30 24050001 */  addiu      $a1, $zero, 0x1
    /* 1F0EE4 151C3A34 00003025 */  or         $a2, $zero, $zero
    /* 1F0EE8 151C3A38 00003825 */  or         $a3, $zero, $zero
    /* 1F0EEC 151C3A3C AFA80010 */  sw         $t0, 0x10($sp)
    /* 1F0EF0 151C3A40 0D44C0A0 */  jal        func_15130280
    /* 1F0EF4 151C3A44 AFAF0014 */   sw        $t7, 0x14($sp)
    /* 1F0EF8 151C3A48 240E0003 */  addiu      $t6, $zero, 0x3
    /* 1F0EFC 151C3A4C 2419FFFF */  addiu      $t9, $zero, -0x1
    /* 1F0F00 151C3A50 A3AE0054 */  sb         $t6, 0x54($sp)
    /* 1F0F04 151C3A54 0D42B688 */  jal        func_150ADA20
    /* 1F0F08 151C3A58 A3B90055 */   sb        $t9, 0x55($sp)
    /* 1F0F0C 151C3A5C 24010007 */  addiu      $at, $zero, 0x7
    /* 1F0F10 151C3A60 0041001B */  divu       $zero, $v0, $at
    /* 1F0F14 151C3A64 0000C010 */  mfhi       $t8
    /* 1F0F18 151C3A68 27090006 */  addiu      $t1, $t8, 0x6
    /* 1F0F1C 151C3A6C A7A90056 */  sh         $t1, 0x56($sp)
    /* 1F0F20 151C3A70 A3A00058 */  sb         $zero, 0x58($sp)
    /* 1F0F24 151C3A74 C6040000 */  lwc1       $f4, 0x0($s0)
    /* 1F0F28 151C3A78 4600218D */  trunc.w.s  $f6, $f4
    /* 1F0F2C 151C3A7C 440B3000 */  mfc1       $t3, $f6
    /* 1F0F30 151C3A80 00000000 */  nop
    /* 1F0F34 151C3A84 AFAB0048 */  sw         $t3, 0x48($sp)
    /* 1F0F38 151C3A88 C6080004 */  lwc1       $f8, 0x4($s0)
    /* 1F0F3C 151C3A8C 4600428D */  trunc.w.s  $f10, $f8
    /* 1F0F40 151C3A90 440D5000 */  mfc1       $t5, $f10
    /* 1F0F44 151C3A94 00000000 */  nop
    /* 1F0F48 151C3A98 AFAD004C */  sw         $t5, 0x4C($sp)
    /* 1F0F4C 151C3A9C C6100008 */  lwc1       $f16, 0x8($s0)
    /* 1F0F50 151C3AA0 4600848D */  trunc.w.s  $f18, $f16
    /* 1F0F54 151C3AA4 440F9000 */  mfc1       $t7, $f18
    /* 1F0F58 151C3AA8 0D42B688 */  jal        func_150ADA20
    /* 1F0F5C 151C3AAC AFAF0050 */   sw        $t7, 0x50($sp)
    /* 1F0F60 151C3AB0 93A90147 */  lbu        $t1, 0x147($sp)
    /* 1F0F64 151C3AB4 8FAA0148 */  lw         $t2, 0x148($sp)
    /* 1F0F68 151C3AB8 30460001 */  andi       $a2, $v0, 0x1
    /* 1F0F6C 151C3ABC 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 1F0F70 151C3AC0 241900FF */  addiu      $t9, $zero, 0xFF
    /* 1F0F74 151C3AC4 241800FF */  addiu      $t8, $zero, 0xFF
    /* 1F0F78 151C3AC8 AFB80018 */  sw         $t8, 0x18($sp)
    /* 1F0F7C 151C3ACC AFB90014 */  sw         $t9, 0x14($sp)
    /* 1F0F80 151C3AD0 AFAE0010 */  sw         $t6, 0x10($sp)
    /* 1F0F84 151C3AD4 24C60005 */  addiu      $a2, $a2, 0x5
    /* 1F0F88 151C3AD8 27A40054 */  addiu      $a0, $sp, 0x54
    /* 1F0F8C 151C3ADC 27A50048 */  addiu      $a1, $sp, 0x48
    /* 1F0F90 151C3AE0 240700FF */  addiu      $a3, $zero, 0xFF
    /* 1F0F94 151C3AE4 AFA0001C */  sw         $zero, 0x1C($sp)
    /* 1F0F98 151C3AE8 AFA00020 */  sw         $zero, 0x20($sp)
    /* 1F0F9C 151C3AEC AFA90024 */  sw         $t1, 0x24($sp)
    /* 1F0FA0 151C3AF0 0D4580B0 */  jal        func_151602C0
    /* 1F0FA4 151C3AF4 AFAA0028 */   sw        $t2, 0x28($sp)
    /* 1F0FA8 151C3AF8 8FBF003C */  lw         $ra, 0x3C($sp)
    /* 1F0FAC 151C3AFC 8FB00038 */  lw         $s0, 0x38($sp)
    /* 1F0FB0 151C3B00 27BD0140 */  addiu      $sp, $sp, 0x140
    /* 1F0FB4 151C3B04 03E00008 */  jr         $ra
    /* 1F0FB8 151C3B08 00000000 */   nop
endlabel func_151C36D8
