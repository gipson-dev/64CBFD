glabel func_150DA67C
    /* 107B2C 150DA67C 27BDFE38 */  addiu      $sp, $sp, -0x1C8
    /* 107B30 150DA680 AFB40058 */  sw         $s4, 0x58($sp)
    /* 107B34 150DA684 AFB30054 */  sw         $s3, 0x54($sp)
    /* 107B38 150DA688 00809825 */  or         $s3, $a0, $zero
    /* 107B3C 150DA68C 00C0A025 */  or         $s4, $a2, $zero
    /* 107B40 150DA690 AFBF005C */  sw         $ra, 0x5C($sp)
    /* 107B44 150DA694 AFB20050 */  sw         $s2, 0x50($sp)
    /* 107B48 150DA698 AFB1004C */  sw         $s1, 0x4C($sp)
    /* 107B4C 150DA69C AFB00048 */  sw         $s0, 0x48($sp)
    /* 107B50 150DA6A0 F7B60040 */  sdc1       $f22, 0x40($sp)
    /* 107B54 150DA6A4 F7B40038 */  sdc1       $f20, 0x38($sp)
    /* 107B58 150DA6A8 AFA501CC */  sw         $a1, 0x1CC($sp)
    /* 107B5C 150DA6AC 8FAE01CC */  lw         $t6, 0x1CC($sp)
    /* 107B60 150DA6B0 8E710098 */  lw         $s1, 0x98($s3)
    /* 107B64 150DA6B4 91C20059 */  lbu        $v0, 0x59($t6)
    /* 107B68 150DA6B8 8DC30000 */  lw         $v1, 0x0($t6)
    /* 107B6C 150DA6BC 104001E1 */  beqz       $v0, .L150DAE44
    /* 107B70 150DA6C0 28410002 */   slti      $at, $v0, 0x2
    /* 107B74 150DA6C4 142000D6 */  bnez       $at, .L150DAA20
    /* 107B78 150DA6C8 00000000 */   nop
    /* 107B7C 150DA6CC 90620004 */  lbu        $v0, 0x4($v1)
    /* 107B80 150DA6D0 24010033 */  addiu      $at, $zero, 0x33
    /* 107B84 150DA6D4 10410003 */  beq        $v0, $at, .L150DA6E4
    /* 107B88 150DA6D8 2401003A */   addiu     $at, $zero, 0x3A
    /* 107B8C 150DA6DC 144100D0 */  bne        $v0, $at, .L150DAA20
    /* 107B90 150DA6E0 00000000 */   nop
  .L150DA6E4:
    /* 107B94 150DA6E4 0D42B69A */  jal        func_150ADA68
    /* 107B98 150DA6E8 00000000 */   nop
    /* 107B9C 150DA6EC 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 107BA0 150DA6F0 4481B000 */  mtc1       $at, $f22
    /* 107BA4 150DA6F4 3C01800A */  lui        $at, %hi(D_800A0BA0)
    /* 107BA8 150DA6F8 C4240BA0 */  lwc1       $f4, %lo(D_800A0BA0)($at)
    /* 107BAC 150DA6FC 3C01800A */  lui        $at, %hi(D_800A0BA4)
    /* 107BB0 150DA700 C4260BA4 */  lwc1       $f6, %lo(D_800A0BA4)($at)
    /* 107BB4 150DA704 3C01800C */  lui        $at, %hi(D_800BE9A4)
    /* 107BB8 150DA708 C430E9A4 */  lwc1       $f16, %lo(D_800BE9A4)($at)
    /* 107BBC 150DA70C 46060202 */  mul.s      $f8, $f0, $f6
    /* 107BC0 150DA710 C6260048 */  lwc1       $f6, 0x48($s1)
    /* 107BC4 150DA714 3C190020 */  lui        $t9, (0x200005 >> 16)
    /* 107BC8 150DA718 3C0A0090 */  lui        $t2, (0x90DE07 >> 16)
    /* 107BCC 150DA71C 3C01800A */  lui        $at, %hi(D_800A0BA8)
    /* 107BD0 150DA720 240F006C */  addiu      $t7, $zero, 0x6C
    /* 107BD4 150DA724 24185103 */  addiu      $t8, $zero, 0x5103
    /* 107BD8 150DA728 46082280 */  add.s      $f10, $f4, $f8
    /* 107BDC 150DA72C 37390005 */  ori        $t9, $t9, (0x200005 & 0xFFFF)
    /* 107BE0 150DA730 2408002E */  addiu      $t0, $zero, 0x2E
    /* 107BE4 150DA734 24090005 */  addiu      $t1, $zero, 0x5
    /* 107BE8 150DA738 46105482 */  mul.s      $f18, $f10, $f16
    /* 107BEC 150DA73C 354ADE07 */  ori        $t2, $t2, (0x90DE07 & 0xFFFF)
    /* 107BF0 150DA740 240B0008 */  addiu      $t3, $zero, 0x8
    /* 107BF4 150DA744 240C0006 */  addiu      $t4, $zero, 0x6
    /* 107BF8 150DA748 240D0024 */  addiu      $t5, $zero, 0x24
    /* 107BFC 150DA74C 240EFFFF */  addiu      $t6, $zero, -0x1
    /* 107C00 150DA750 46123100 */  add.s      $f4, $f6, $f18
    /* 107C04 150DA754 E6240048 */  swc1       $f4, 0x48($s1)
    /* 107C08 150DA758 C6280048 */  lwc1       $f8, 0x48($s1)
    /* 107C0C 150DA75C 4608B03C */  c.lt.s     $f22, $f8
    /* 107C10 150DA760 00000000 */  nop
    /* 107C14 150DA764 450000AC */  bc1f       .L150DAA18
    /* 107C18 150DA768 00000000 */   nop
    /* 107C1C 150DA76C 44800000 */  mtc1       $zero, $f0
    /* 107C20 150DA770 00000000 */  nop
    /* 107C24 150DA774 C42A0BA8 */  lwc1       $f10, %lo(D_800A0BA8)($at)
    /* 107C28 150DA778 A7B80158 */  sh         $t8, 0x158($sp)
    /* 107C2C 150DA77C 2418002E */  addiu      $t8, $zero, 0x2E
    /* 107C30 150DA780 3C01800A */  lui        $at, %hi(D_800A0BAC)
    /* 107C34 150DA784 C4300BAC */  lwc1       $f16, %lo(D_800A0BAC)($at)
    /* 107C38 150DA788 A7B80172 */  sh         $t8, 0x172($sp)
    /* 107C3C 150DA78C 8FB801CC */  lw         $t8, 0x1CC($sp)
    /* 107C40 150DA790 A3AF016D */  sb         $t7, 0x16D($sp)
    /* 107C44 150DA794 AFB90150 */  sw         $t9, 0x150($sp)
    /* 107C48 150DA798 A7A8016E */  sh         $t0, 0x16E($sp)
    /* 107C4C 150DA79C A7A90170 */  sh         $t1, 0x170($sp)
    /* 107C50 150DA7A0 AFAA01A8 */  sw         $t2, 0x1A8($sp)
    /* 107C54 150DA7A4 A3AB01B0 */  sb         $t3, 0x1B0($sp)
    /* 107C58 150DA7A8 A3AC01B1 */  sb         $t4, 0x1B1($sp)
    /* 107C5C 150DA7AC A3AD01B2 */  sb         $t5, 0x1B2($sp)
    /* 107C60 150DA7B0 A3AE01B3 */  sb         $t6, 0x1B3($sp)
    /* 107C64 150DA7B4 240FFFFF */  addiu      $t7, $zero, -0x1
    /* 107C68 150DA7B8 241900DD */  addiu      $t9, $zero, 0xDD
    /* 107C6C 150DA7BC 240800D3 */  addiu      $t0, $zero, 0xD3
    /* 107C70 150DA7C0 240900CD */  addiu      $t1, $zero, 0xCD
    /* 107C74 150DA7C4 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 107C78 150DA7C8 240B0057 */  addiu      $t3, $zero, 0x57
    /* 107C7C 150DA7CC 240C0055 */  addiu      $t4, $zero, 0x55
    /* 107C80 150DA7D0 240D005A */  addiu      $t5, $zero, 0x5A
    /* 107C84 150DA7D4 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 107C88 150DA7D8 AFA00154 */  sw         $zero, 0x154($sp)
    /* 107C8C 150DA7DC AFA0015C */  sw         $zero, 0x15C($sp)
    /* 107C90 150DA7E0 AFA00160 */  sw         $zero, 0x160($sp)
    /* 107C94 150DA7E4 A3AF01B4 */  sb         $t7, 0x1B4($sp)
    /* 107C98 150DA7E8 A3A001B5 */  sb         $zero, 0x1B5($sp)
    /* 107C9C 150DA7EC A3B90164 */  sb         $t9, 0x164($sp)
    /* 107CA0 150DA7F0 A3A80165 */  sb         $t0, 0x165($sp)
    /* 107CA4 150DA7F4 A3A90166 */  sb         $t1, 0x166($sp)
    /* 107CA8 150DA7F8 A3AA0167 */  sb         $t2, 0x167($sp)
    /* 107CAC 150DA7FC A3AB0168 */  sb         $t3, 0x168($sp)
    /* 107CB0 150DA800 A3AC0169 */  sb         $t4, 0x169($sp)
    /* 107CB4 150DA804 A3AD016A */  sb         $t5, 0x16A($sp)
    /* 107CB8 150DA808 A3AE016C */  sb         $t6, 0x16C($sp)
    /* 107CBC 150DA80C E7A0018C */  swc1       $f0, 0x18C($sp)
    /* 107CC0 150DA810 E7A00190 */  swc1       $f0, 0x190($sp)
    /* 107CC4 150DA814 E7A00194 */  swc1       $f0, 0x194($sp)
    /* 107CC8 150DA818 E7AA014C */  swc1       $f10, 0x14C($sp)
    /* 107CCC 150DA81C E7B00174 */  swc1       $f16, 0x174($sp)
    /* 107CD0 150DA820 8F010008 */  lw         $at, 0x8($t8)
    /* 107CD4 150DA824 27AF0180 */  addiu      $t7, $sp, 0x180
    /* 107CD8 150DA828 3C0B800A */  lui        $t3, %hi(D_800A5480)
    /* 107CDC 150DA82C ADE10000 */  sw         $at, 0x0($t7)
    /* 107CE0 150DA830 8F09000C */  lw         $t1, 0xC($t8)
    /* 107CE4 150DA834 256B5480 */  addiu      $t3, $t3, %lo(D_800A5480)
    /* 107CE8 150DA838 27AA0198 */  addiu      $t2, $sp, 0x198
    /* 107CEC 150DA83C ADE90004 */  sw         $t1, 0x4($t7)
    /* 107CF0 150DA840 8F010010 */  lw         $at, 0x10($t8)
    /* 107CF4 150DA844 24140065 */  addiu      $s4, $zero, 0x65
    /* 107CF8 150DA848 24120005 */  addiu      $s2, $zero, 0x5
    /* 107CFC 150DA84C ADE10008 */  sw         $at, 0x8($t7)
    /* 107D00 150DA850 8D610000 */  lw         $at, 0x0($t3)
    /* 107D04 150DA854 8D6E0004 */  lw         $t6, 0x4($t3)
    /* 107D08 150DA858 AD410000 */  sw         $at, 0x0($t2)
    /* 107D0C 150DA85C 8D610008 */  lw         $at, 0x8($t3)
    /* 107D10 150DA860 AD4E0004 */  sw         $t6, 0x4($t2)
    /* 107D14 150DA864 AD410008 */  sw         $at, 0x8($t2)
    /* 107D18 150DA868 3C014120 */  lui        $at, (0x41200000 >> 16)
    /* 107D1C 150DA86C 4481A000 */  mtc1       $at, $f20
    /* 107D20 150DA870 00000000 */  nop
  .L150DA874:
    /* 107D24 150DA874 0D42B688 */  jal        func_150ADA20
    /* 107D28 150DA878 00000000 */   nop
    /* 107D2C 150DA87C 0D42B688 */  jal        func_150ADA20
    /* 107D30 150DA880 A3A20140 */   sb        $v0, 0x140($sp)
    /* 107D34 150DA884 0040C825 */  or         $t9, $v0, $zero
    /* 107D38 150DA888 0D42B688 */  jal        func_150ADA20
    /* 107D3C 150DA88C A3B90141 */   sb        $t9, 0x141($sp)
    /* 107D40 150DA890 0052001B */  divu       $zero, $v0, $s2
    /* 107D44 150DA894 00007810 */  mfhi       $t7
    /* 107D48 150DA898 25F80004 */  addiu      $t8, $t7, 0x4
    /* 107D4C 150DA89C 16400002 */  bnez       $s2, .L150DA8A8
    /* 107D50 150DA8A0 00000000 */   nop
    /* 107D54 150DA8A4 0007000D */  break      7
  .L150DA8A8:
    /* 107D58 150DA8A8 A3B80142 */  sb         $t8, 0x142($sp)
    /* 107D5C 150DA8AC 0D42B688 */  jal        func_150ADA20
    /* 107D60 150DA8B0 00000000 */   nop
    /* 107D64 150DA8B4 0052001B */  divu       $zero, $v0, $s2
    /* 107D68 150DA8B8 00004810 */  mfhi       $t1
    /* 107D6C 150DA8BC 252D0004 */  addiu      $t5, $t1, 0x4
    /* 107D70 150DA8C0 16400002 */  bnez       $s2, .L150DA8CC
    /* 107D74 150DA8C4 00000000 */   nop
    /* 107D78 150DA8C8 0007000D */  break      7
  .L150DA8CC:
    /* 107D7C 150DA8CC A3AD0143 */  sb         $t5, 0x143($sp)
    /* 107D80 150DA8D0 0D42B69A */  jal        func_150ADA68
    /* 107D84 150DA8D4 00000000 */   nop
    /* 107D88 150DA8D8 46140182 */  mul.s      $f6, $f0, $f20
    /* 107D8C 150DA8DC 0D42B69A */  jal        func_150ADA68
    /* 107D90 150DA8E0 E7A60144 */   swc1      $f6, 0x144($sp)
    /* 107D94 150DA8E4 46140482 */  mul.s      $f18, $f0, $f20
    /* 107D98 150DA8E8 0D42B69A */  jal        func_150ADA68
    /* 107D9C 150DA8EC E7B20148 */   swc1      $f18, 0x148($sp)
    /* 107DA0 150DA8F0 3C01800A */  lui        $at, %hi(D_800A0BB0)
    /* 107DA4 150DA8F4 C4240BB0 */  lwc1       $f4, %lo(D_800A0BB0)($at)
    /* 107DA8 150DA8F8 3C01800A */  lui        $at, %hi(D_800A0BB4)
    /* 107DAC 150DA8FC C42A0BB4 */  lwc1       $f10, %lo(D_800A0BB4)($at)
    /* 107DB0 150DA900 46040202 */  mul.s      $f8, $f0, $f4
    /* 107DB4 150DA904 8FAC01A8 */  lw         $t4, 0x1A8($sp)
    /* 107DB8 150DA908 2401FF3F */  addiu      $at, $zero, -0xC1
    /* 107DBC 150DA90C 01815024 */  and        $t2, $t4, $at
    /* 107DC0 150DA910 AFAA01A8 */  sw         $t2, 0x1A8($sp)
    /* 107DC4 150DA914 460A4400 */  add.s      $f16, $f8, $f10
    /* 107DC8 150DA918 0D42B688 */  jal        func_150ADA20
    /* 107DCC 150DA91C E7B001A4 */   swc1      $f16, 0x1A4($sp)
    /* 107DD0 150DA920 304B0001 */  andi       $t3, $v0, 0x1
    /* 107DD4 150DA924 11600003 */  beqz       $t3, .L150DA934
    /* 107DD8 150DA928 00008025 */   or        $s0, $zero, $zero
    /* 107DDC 150DA92C 10000001 */  b          .L150DA934
    /* 107DE0 150DA930 24100080 */   addiu     $s0, $zero, 0x80
  .L150DA934:
    /* 107DE4 150DA934 0D42B688 */  jal        func_150ADA20
    /* 107DE8 150DA938 00000000 */   nop
    /* 107DEC 150DA93C 304E0001 */  andi       $t6, $v0, 0x1
    /* 107DF0 150DA940 11C00003 */  beqz       $t6, .L150DA950
    /* 107DF4 150DA944 8FA801A8 */   lw        $t0, 0x1A8($sp)
    /* 107DF8 150DA948 10000002 */  b          .L150DA954
    /* 107DFC 150DA94C 24020040 */   addiu     $v0, $zero, 0x40
  .L150DA950:
    /* 107E00 150DA950 00001025 */  or         $v0, $zero, $zero
  .L150DA954:
    /* 107E04 150DA954 0050C825 */  or         $t9, $v0, $s0
    /* 107E08 150DA958 01197825 */  or         $t7, $t0, $t9
    /* 107E0C 150DA95C 0D42B688 */  jal        func_150ADA20
    /* 107E10 150DA960 AFAF01A8 */   sw        $t7, 0x1A8($sp)
    /* 107E14 150DA964 0054001B */  divu       $zero, $v0, $s4
    /* 107E18 150DA968 0000C010 */  mfhi       $t8
    /* 107E1C 150DA96C 27090064 */  addiu      $t1, $t8, 0x64
    /* 107E20 150DA970 16800002 */  bnez       $s4, .L150DA97C
    /* 107E24 150DA974 00000000 */   nop
    /* 107E28 150DA978 0007000D */  break      7
  .L150DA97C:
    /* 107E2C 150DA97C A3A9016B */  sb         $t1, 0x16B($sp)
    /* 107E30 150DA980 0D42B688 */  jal        func_150ADA20
    /* 107E34 150DA984 00000000 */   nop
    /* 107E38 150DA988 2401000B */  addiu      $at, $zero, 0xB
    /* 107E3C 150DA98C 0041001B */  divu       $zero, $v0, $at
    /* 107E40 150DA990 00006810 */  mfhi       $t5
    /* 107E44 150DA994 25AC0046 */  addiu      $t4, $t5, 0x46
    /* 107E48 150DA998 0D42B69A */  jal        func_150ADA68
    /* 107E4C 150DA99C A7AC015A */   sh        $t4, 0x15A($sp)
    /* 107E50 150DA9A0 3C0142E8 */  lui        $at, (0x42E80000 >> 16)
    /* 107E54 150DA9A4 44813000 */  mtc1       $at, $f6
    /* 107E58 150DA9A8 3C014303 */  lui        $at, (0x43030000 >> 16)
    /* 107E5C 150DA9AC 44812000 */  mtc1       $at, $f4
    /* 107E60 150DA9B0 46060482 */  mul.s      $f18, $f0, $f6
    /* 107E64 150DA9B4 27A40150 */  addiu      $a0, $sp, 0x150
    /* 107E68 150DA9B8 24050001 */  addiu      $a1, $zero, 0x1
    /* 107E6C 150DA9BC 00003025 */  or         $a2, $zero, $zero
    /* 107E70 150DA9C0 24070010 */  addiu      $a3, $zero, 0x10
    /* 107E74 150DA9C4 46049200 */  add.s      $f8, $f18, $f4
    /* 107E78 150DA9C8 E7A8017C */  swc1       $f8, 0x17C($sp)
    /* 107E7C 150DA9CC E7A80178 */  swc1       $f8, 0x178($sp)
    /* 107E80 150DA9D0 926A000C */  lbu        $t2, 0xC($s3)
    /* 107E84 150DA9D4 AFAA0010 */  sw         $t2, 0x10($sp)
    /* 107E88 150DA9D8 926B0001 */  lbu        $t3, 0x1($s3)
    /* 107E8C 150DA9DC 0D44C0A0 */  jal        func_15130280
    /* 107E90 150DA9E0 AFAB0014 */   sw        $t3, 0x14($sp)
    /* 107E94 150DA9E4 10400004 */  beqz       $v0, .L150DA9F8
    /* 107E98 150DA9E8 244400A8 */   addiu     $a0, $v0, 0xA8
    /* 107E9C 150DA9EC 27A50140 */  addiu      $a1, $sp, 0x140
    /* 107EA0 150DA9F0 0C008BB0 */  jal        memcpy
    /* 107EA4 150DA9F4 24060010 */   addiu     $a2, $zero, 0x10
  .L150DA9F8:
    /* 107EA8 150DA9F8 C62A0048 */  lwc1       $f10, 0x48($s1)
    /* 107EAC 150DA9FC 46165401 */  sub.s      $f16, $f10, $f22
    /* 107EB0 150DAA00 E6300048 */  swc1       $f16, 0x48($s1)
    /* 107EB4 150DAA04 C6260048 */  lwc1       $f6, 0x48($s1)
    /* 107EB8 150DAA08 4606B03C */  c.lt.s     $f22, $f6
    /* 107EBC 150DAA0C 00000000 */  nop
    /* 107EC0 150DAA10 4501FF98 */  bc1t       .L150DA874
    /* 107EC4 150DAA14 00000000 */   nop
  .L150DAA18:
    /* 107EC8 150DAA18 100000B9 */  b          .L150DAD00
    /* 107ECC 150DAA1C 8FAD01CC */   lw        $t5, 0x1CC($sp)
  .L150DAA20:
    /* 107ED0 150DAA20 0D42B69A */  jal        func_150ADA68
    /* 107ED4 150DAA24 00000000 */   nop
    /* 107ED8 150DAA28 3C01800A */  lui        $at, %hi(D_800A0BB8)
    /* 107EDC 150DAA2C C4220BB8 */  lwc1       $f2, %lo(D_800A0BB8)($at)
    /* 107EE0 150DAA30 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 107EE4 150DAA34 4481B000 */  mtc1       $at, $f22
    /* 107EE8 150DAA38 46020482 */  mul.s      $f18, $f0, $f2
    /* 107EEC 150DAA3C 3C01800C */  lui        $at, %hi(D_800BE9A4)
    /* 107EF0 150DAA40 C428E9A4 */  lwc1       $f8, %lo(D_800BE9A4)($at)
    /* 107EF4 150DAA44 C6300044 */  lwc1       $f16, 0x44($s1)
    /* 107EF8 150DAA48 27B000D4 */  addiu      $s0, $sp, 0xD4
    /* 107EFC 150DAA4C 02002025 */  or         $a0, $s0, $zero
    /* 107F00 150DAA50 46121100 */  add.s      $f4, $f2, $f18
    /* 107F04 150DAA54 46082282 */  mul.s      $f10, $f4, $f8
    /* 107F08 150DAA58 460A8180 */  add.s      $f6, $f16, $f10
    /* 107F0C 150DAA5C E6260044 */  swc1       $f6, 0x44($s1)
    /* 107F10 150DAA60 C6320044 */  lwc1       $f18, 0x44($s1)
    /* 107F14 150DAA64 4612B03C */  c.lt.s     $f22, $f18
    /* 107F18 150DAA68 00000000 */  nop
    /* 107F1C 150DAA6C 450200A4 */  bc1fl      .L150DAD00
    /* 107F20 150DAA70 8FAD01CC */   lw        $t5, 0x1CC($sp)
    /* 107F24 150DAA74 0D411CB0 */  jal        func_150472C0
    /* 107F28 150DAA78 8FA501CC */   lw        $a1, 0x1CC($sp)
    /* 107F2C 150DAA7C 8FAE01CC */  lw         $t6, 0x1CC($sp)
    /* 107F30 150DAA80 27B200F8 */  addiu      $s2, $sp, 0xF8
    /* 107F34 150DAA84 24180002 */  addiu      $t8, $zero, 0x2
    /* 107F38 150DAA88 8DC10008 */  lw         $at, 0x8($t6)
    /* 107F3C 150DAA8C 240F0001 */  addiu      $t7, $zero, 0x1
    /* 107F40 150DAA90 24090003 */  addiu      $t1, $zero, 0x3
    /* 107F44 150DAA94 AE410000 */  sw         $at, 0x0($s2)
    /* 107F48 150DAA98 8DD9000C */  lw         $t9, 0xC($t6)
    /* 107F4C 150DAA9C 240D0001 */  addiu      $t5, $zero, 0x1
    /* 107F50 150DAAA0 240C0014 */  addiu      $t4, $zero, 0x14
    /* 107F54 150DAAA4 AE590004 */  sw         $t9, 0x4($s2)
    /* 107F58 150DAAA8 8DC10010 */  lw         $at, 0x10($t6)
    /* 107F5C 150DAAAC 240A000A */  addiu      $t2, $zero, 0xA
    /* 107F60 150DAAB0 240B00C8 */  addiu      $t3, $zero, 0xC8
    /* 107F64 150DAAB4 AE410008 */  sw         $at, 0x8($s2)
    /* 107F68 150DAAB8 3C01800A */  lui        $at, %hi(D_800A0BBC)
    /* 107F6C 150DAABC C4240BBC */  lwc1       $f4, %lo(D_800A0BBC)($at)
    /* 107F70 150DAAC0 3C01800A */  lui        $at, %hi(D_800A0BC0)
    /* 107F74 150DAAC4 C4280BC0 */  lwc1       $f8, %lo(D_800A0BC0)($at)
    /* 107F78 150DAAC8 3C01800A */  lui        $at, %hi(D_800A0BC4)
    /* 107F7C 150DAACC C4300BC4 */  lwc1       $f16, %lo(D_800A0BC4)($at)
    /* 107F80 150DAAD0 3C01800A */  lui        $at, %hi(D_800A0BC8)
    /* 107F84 150DAAD4 C42A0BC8 */  lwc1       $f10, %lo(D_800A0BC8)($at)
    /* 107F88 150DAAD8 3C01800A */  lui        $at, %hi(D_800A0BCC)
    /* 107F8C 150DAADC C4260BCC */  lwc1       $f6, %lo(D_800A0BCC)($at)
    /* 107F90 150DAAE0 3C01800A */  lui        $at, %hi(D_800A0BD0)
    /* 107F94 150DAAE4 C4320BD0 */  lwc1       $f18, %lo(D_800A0BD0)($at)
    /* 107F98 150DAAE8 3C01800A */  lui        $at, %hi(D_800A0BD4)
    /* 107F9C 150DAAEC E7A40104 */  swc1       $f4, 0x104($sp)
    /* 107FA0 150DAAF0 C4240BD4 */  lwc1       $f4, %lo(D_800A0BD4)($at)
    /* 107FA4 150DAAF4 A7B8011E */  sh         $t8, 0x11E($sp)
    /* 107FA8 150DAAF8 8FB801CC */  lw         $t8, 0x1CC($sp)
    /* 107FAC 150DAAFC A7AF011C */  sh         $t7, 0x11C($sp)
    /* 107FB0 150DAB00 24080037 */  addiu      $t0, $zero, 0x37
    /* 107FB4 150DAB04 240E0010 */  addiu      $t6, $zero, 0x10
    /* 107FB8 150DAB08 2419000F */  addiu      $t9, $zero, 0xF
    /* 107FBC 150DAB0C 240F0003 */  addiu      $t7, $zero, 0x3
    /* 107FC0 150DAB10 A7A90120 */  sh         $t1, 0x120($sp)
    /* 107FC4 150DAB14 A7AD0122 */  sh         $t5, 0x122($sp)
    /* 107FC8 150DAB18 A7AC0124 */  sh         $t4, 0x124($sp)
    /* 107FCC 150DAB1C A7AA0126 */  sh         $t2, 0x126($sp)
    /* 107FD0 150DAB20 A7AB0128 */  sh         $t3, 0x128($sp)
    /* 107FD4 150DAB24 A7A8012A */  sh         $t0, 0x12A($sp)
    /* 107FD8 150DAB28 A7AE0134 */  sh         $t6, 0x134($sp)
    /* 107FDC 150DAB2C A7B90136 */  sh         $t9, 0x136($sp)
    /* 107FE0 150DAB30 AFA00138 */  sw         $zero, 0x138($sp)
    /* 107FE4 150DAB34 A3AF012C */  sb         $t7, 0x12C($sp)
    /* 107FE8 150DAB38 E7A80108 */  swc1       $f8, 0x108($sp)
    /* 107FEC 150DAB3C E7B0010C */  swc1       $f16, 0x10C($sp)
    /* 107FF0 150DAB40 E7AA0110 */  swc1       $f10, 0x110($sp)
    /* 107FF4 150DAB44 E7A60114 */  swc1       $f6, 0x114($sp)
    /* 107FF8 150DAB48 E7B20118 */  swc1       $f18, 0x118($sp)
    /* 107FFC 150DAB4C E7A40130 */  swc1       $f4, 0x130($sp)
    /* 108000 150DAB50 93090059 */  lbu        $t1, 0x59($t8)
    /* 108004 150DAB54 27A2006C */  addiu      $v0, $sp, 0x6C
    /* 108008 150DAB58 240D0001 */  addiu      $t5, $zero, 0x1
    /* 10800C 150DAB5C 29210002 */  slti       $at, $t1, 0x2
    /* 108010 150DAB60 54200037 */  bnel       $at, $zero, .L150DAC40
    /* 108014 150DAB64 C6920000 */   lwc1      $f18, 0x0($s4)
    /* 108018 150DAB68 A3AD00A8 */  sb         $t5, 0xA8($sp)
    /* 10801C 150DAB6C C6880000 */  lwc1       $f8, 0x0($s4)
    /* 108020 150DAB70 3C0C800A */  lui        $t4, %hi(D_800A5480)
    /* 108024 150DAB74 258C5480 */  addiu      $t4, $t4, %lo(D_800A5480)
    /* 108028 150DAB78 46004407 */  neg.s      $f16, $f8
    /* 10802C 150DAB7C 27AE00C4 */  addiu      $t6, $sp, 0xC4
    /* 108030 150DAB80 E7B000AC */  swc1       $f16, 0xAC($sp)
    /* 108034 150DAB84 C68A0004 */  lwc1       $f10, 0x4($s4)
    /* 108038 150DAB88 27A900B8 */  addiu      $t1, $sp, 0xB8
    /* 10803C 150DAB8C 46005187 */  neg.s      $f6, $f10
    /* 108040 150DAB90 E7A600B0 */  swc1       $f6, 0xB0($sp)
    /* 108044 150DAB94 C6920008 */  lwc1       $f18, 0x8($s4)
    /* 108048 150DAB98 46009107 */  neg.s      $f4, $f18
    /* 10804C 150DAB9C E7A400B4 */  swc1       $f4, 0xB4($sp)
    /* 108050 150DABA0 8D810000 */  lw         $at, 0x0($t4)
    /* 108054 150DABA4 AC410000 */  sw         $at, 0x0($v0)
    /* 108058 150DABA8 8D880004 */  lw         $t0, 0x4($t4)
    /* 10805C 150DABAC AC480004 */  sw         $t0, 0x4($v0)
    /* 108060 150DABB0 8D810008 */  lw         $at, 0x8($t4)
    /* 108064 150DABB4 AC410008 */  sw         $at, 0x8($v0)
    /* 108068 150DABB8 8C410000 */  lw         $at, 0x0($v0)
    /* 10806C 150DABBC ADC10000 */  sw         $at, 0x0($t6)
    /* 108070 150DABC0 8C580004 */  lw         $t8, 0x4($v0)
    /* 108074 150DABC4 ADD80004 */  sw         $t8, 0x4($t6)
    /* 108078 150DABC8 8C410008 */  lw         $at, 0x8($v0)
    /* 10807C 150DABCC ADC10008 */  sw         $at, 0x8($t6)
    /* 108080 150DABD0 8C410000 */  lw         $at, 0x0($v0)
    /* 108084 150DABD4 AD210000 */  sw         $at, 0x0($t1)
    /* 108088 150DABD8 8C4A0004 */  lw         $t2, 0x4($v0)
    /* 10808C 150DABDC AD2A0004 */  sw         $t2, 0x4($t1)
    /* 108090 150DABE0 8C410008 */  lw         $at, 0x8($v0)
    /* 108094 150DABE4 AD210008 */  sw         $at, 0x8($t1)
    /* 108098 150DABE8 3C014396 */  lui        $at, (0x43960000 >> 16)
    /* 10809C 150DABEC 44814000 */  mtc1       $at, $f8
    /* 1080A0 150DABF0 00000000 */  nop
    /* 1080A4 150DABF4 E7A800D0 */  swc1       $f8, 0xD0($sp)
    /* 1080A8 150DABF8 926C0001 */  lbu        $t4, 0x1($s3)
  .L150DABFC:
    /* 1080AC 150DABFC 9267000C */  lbu        $a3, 0xC($s3)
    /* 1080B0 150DAC00 27A400A8 */  addiu      $a0, $sp, 0xA8
    /* 1080B4 150DAC04 02402825 */  or         $a1, $s2, $zero
    /* 1080B8 150DAC08 02003025 */  or         $a2, $s0, $zero
    /* 1080BC 150DAC0C 0D454F33 */  jal        func_15153CCC
    /* 1080C0 150DAC10 AFAC0010 */   sw        $t4, 0x10($sp)
    /* 1080C4 150DAC14 C6300044 */  lwc1       $f16, 0x44($s1)
    /* 1080C8 150DAC18 46168281 */  sub.s      $f10, $f16, $f22
    /* 1080CC 150DAC1C E62A0044 */  swc1       $f10, 0x44($s1)
    /* 1080D0 150DAC20 C6260044 */  lwc1       $f6, 0x44($s1)
    /* 1080D4 150DAC24 4606B03C */  c.lt.s     $f22, $f6
    /* 1080D8 150DAC28 00000000 */  nop
    /* 1080DC 150DAC2C 4503FFF3 */  bc1tl      .L150DABFC
    /* 1080E0 150DAC30 926C0001 */   lbu       $t4, 0x1($s3)
    /* 1080E4 150DAC34 10000032 */  b          .L150DAD00
    /* 1080E8 150DAC38 8FAD01CC */   lw        $t5, 0x1CC($sp)
    /* 1080EC 150DAC3C C6920000 */  lwc1       $f18, 0x0($s4)
  .L150DAC40:
    /* 1080F0 150DAC40 8FAF01CC */  lw         $t7, 0x1CC($sp)
    /* 1080F4 150DAC44 27A80090 */  addiu      $t0, $sp, 0x90
    /* 1080F8 150DAC48 46009107 */  neg.s      $f4, $f18
    /* 1080FC 150DAC4C E7A40084 */  swc1       $f4, 0x84($sp)
    /* 108100 150DAC50 C6880004 */  lwc1       $f8, 0x4($s4)
    /* 108104 150DAC54 46004407 */  neg.s      $f16, $f8
    /* 108108 150DAC58 E7B00088 */  swc1       $f16, 0x88($sp)
    /* 10810C 150DAC5C C68A0008 */  lwc1       $f10, 0x8($s4)
    /* 108110 150DAC60 46005187 */  neg.s      $f6, $f10
    /* 108114 150DAC64 E7A6008C */  swc1       $f6, 0x8C($sp)
    /* 108118 150DAC68 89E10044 */  lwl        $at, 0x44($t7)
    /* 10811C 150DAC6C 99E10047 */  lwr        $at, 0x47($t7)
    /* 108120 150DAC70 A9010000 */  swl        $at, 0x0($t0)
    /* 108124 150DAC74 B9010003 */  swr        $at, 0x3($t0)
    /* 108128 150DAC78 89F80048 */  lwl        $t8, 0x48($t7)
    /* 10812C 150DAC7C 99F8004B */  lwr        $t8, 0x4B($t7)
    /* 108130 150DAC80 A9180004 */  swl        $t8, 0x4($t0)
    /* 108134 150DAC84 B9180007 */  swr        $t8, 0x7($t0)
    /* 108138 150DAC88 89E1004C */  lwl        $at, 0x4C($t7)
    /* 10813C 150DAC8C 99E1004F */  lwr        $at, 0x4F($t7)
    /* 108140 150DAC90 A9010008 */  swl        $at, 0x8($t0)
    /* 108144 150DAC94 B901000B */  swr        $at, 0xB($t0)
    /* 108148 150DAC98 89F80050 */  lwl        $t8, 0x50($t7)
    /* 10814C 150DAC9C 99F80053 */  lwr        $t8, 0x53($t7)
    /* 108150 150DACA0 A918000C */  swl        $t8, 0xC($t0)
    /* 108154 150DACA4 B918000F */  swr        $t8, 0xF($t0)
    /* 108158 150DACA8 95E10054 */  lhu        $at, 0x54($t7)
    /* 10815C 150DACAC A5010010 */  sh         $at, 0x10($t0)
    /* 108160 150DACB0 3C014396 */  lui        $at, (0x43960000 >> 16)
    /* 108164 150DACB4 44819000 */  mtc1       $at, $f18
    /* 108168 150DACB8 00000000 */  nop
    /* 10816C 150DACBC E7B200A4 */  swc1       $f18, 0xA4($sp)
    /* 108170 150DACC0 926B0001 */  lbu        $t3, 0x1($s3)
  .L150DACC4:
    /* 108174 150DACC4 9267000C */  lbu        $a3, 0xC($s3)
    /* 108178 150DACC8 27A40084 */  addiu      $a0, $sp, 0x84
    /* 10817C 150DACCC 02402825 */  or         $a1, $s2, $zero
    /* 108180 150DACD0 02003025 */  or         $a2, $s0, $zero
    /* 108184 150DACD4 0D454F21 */  jal        func_15153C84
    /* 108188 150DACD8 AFAB0010 */   sw        $t3, 0x10($sp)
    /* 10818C 150DACDC C6240044 */  lwc1       $f4, 0x44($s1)
    /* 108190 150DACE0 46162201 */  sub.s      $f8, $f4, $f22
    /* 108194 150DACE4 E6280044 */  swc1       $f8, 0x44($s1)
    /* 108198 150DACE8 C6300044 */  lwc1       $f16, 0x44($s1)
    /* 10819C 150DACEC 4610B03C */  c.lt.s     $f22, $f16
    /* 1081A0 150DACF0 00000000 */  nop
    /* 1081A4 150DACF4 4503FFF3 */  bc1tl      .L150DACC4
    /* 1081A8 150DACF8 926B0001 */   lbu       $t3, 0x1($s3)
    /* 1081AC 150DACFC 8FAD01CC */  lw         $t5, 0x1CC($sp)
  .L150DAD00:
    /* 1081B0 150DAD00 24010001 */  addiu      $at, $zero, 0x1
    /* 1081B4 150DAD04 24140065 */  addiu      $s4, $zero, 0x65
    /* 1081B8 150DAD08 91A90059 */  lbu        $t1, 0x59($t5)
    /* 1081BC 150DAD0C 5521004E */  bnel       $t1, $at, .L150DAE48
    /* 1081C0 150DAD10 8FBF005C */   lw        $ra, 0x5C($sp)
    /* 1081C4 150DAD14 0D42B69A */  jal        func_150ADA68
    /* 1081C8 150DAD18 00000000 */   nop
    /* 1081CC 150DAD1C 3C01800A */  lui        $at, %hi(D_800A0BD8)
    /* 1081D0 150DAD20 C42A0BD8 */  lwc1       $f10, %lo(D_800A0BD8)($at)
    /* 1081D4 150DAD24 3C01800A */  lui        $at, %hi(D_800A0BDC)
    /* 1081D8 150DAD28 C4260BDC */  lwc1       $f6, %lo(D_800A0BDC)($at)
    /* 1081DC 150DAD2C 3C01800C */  lui        $at, %hi(D_800BE9A4)
    /* 1081E0 150DAD30 C428E9A4 */  lwc1       $f8, %lo(D_800BE9A4)($at)
    /* 1081E4 150DAD34 46060482 */  mul.s      $f18, $f0, $f6
    /* 1081E8 150DAD38 C6260040 */  lwc1       $f6, 0x40($s1)
    /* 1081EC 150DAD3C 24120051 */  addiu      $s2, $zero, 0x51
    /* 1081F0 150DAD40 46125100 */  add.s      $f4, $f10, $f18
    /* 1081F4 150DAD44 46082402 */  mul.s      $f16, $f4, $f8
    /* 1081F8 150DAD48 46103280 */  add.s      $f10, $f6, $f16
    /* 1081FC 150DAD4C E62A0040 */  swc1       $f10, 0x40($s1)
    /* 108200 150DAD50 C6320040 */  lwc1       $f18, 0x40($s1)
    /* 108204 150DAD54 8FAA01CC */  lw         $t2, 0x1CC($sp)
    /* 108208 150DAD58 4612B03C */  c.lt.s     $f22, $f18
    /* 10820C 150DAD5C 254C0008 */  addiu      $t4, $t2, 0x8
    /* 108210 150DAD60 254E0044 */  addiu      $t6, $t2, 0x44
    /* 108214 150DAD64 45020038 */  bc1fl      .L150DAE48
    /* 108218 150DAD68 8FBF005C */   lw        $ra, 0x5C($sp)
    /* 10821C 150DAD6C AFAC0068 */  sw         $t4, 0x68($sp)
    /* 108220 150DAD70 AFAE0064 */  sw         $t6, 0x64($sp)
  .L150DAD74:
    /* 108224 150DAD74 0D42B69A */  jal        func_150ADA68
    /* 108228 150DAD78 00000000 */   nop
    /* 10822C 150DAD7C 0D42B688 */  jal        func_150ADA20
    /* 108230 150DAD80 46000506 */   mov.s     $f20, $f0
    /* 108234 150DAD84 0D42B688 */  jal        func_150ADA20
    /* 108238 150DAD88 00408025 */   or        $s0, $v0, $zero
    /* 10823C 150DAD8C 0214001B */  divu       $zero, $s0, $s4
    /* 108240 150DAD90 00003010 */  mfhi       $a2
    /* 108244 150DAD94 3C0141F0 */  lui        $at, (0x41F00000 >> 16)
    /* 108248 150DAD98 44812000 */  mtc1       $at, $f4
    /* 10824C 150DAD9C 0052001B */  divu       $zero, $v0, $s2
    /* 108250 150DADA0 4604A202 */  mul.s      $f8, $f20, $f4
    /* 108254 150DADA4 8FA80068 */  lw         $t0, 0x68($sp)
    /* 108258 150DADA8 00007810 */  mfhi       $t7
    /* 10825C 150DADAC 3C014170 */  lui        $at, (0x41700000 >> 16)
    /* 108260 150DADB0 44813000 */  mtc1       $at, $f6
    /* 108264 150DADB4 25F8003C */  addiu      $t8, $t7, 0x3C
    /* 108268 150DADB8 240B0001 */  addiu      $t3, $zero, 0x1
    /* 10826C 150DADBC 240D0001 */  addiu      $t5, $zero, 0x1
    /* 108270 150DADC0 24090001 */  addiu      $t1, $zero, 0x1
    /* 108274 150DADC4 AFA90020 */  sw         $t1, 0x20($sp)
    /* 108278 150DADC8 AFAD001C */  sw         $t5, 0x1C($sp)
    /* 10827C 150DADCC AFAB0018 */  sw         $t3, 0x18($sp)
    /* 108280 150DADD0 AFB80014 */  sw         $t8, 0x14($sp)
    /* 108284 150DADD4 AFA80010 */  sw         $t0, 0x10($sp)
    /* 108288 150DADD8 926C000C */  lbu        $t4, 0xC($s3)
    /* 10828C 150DADDC 46064400 */  add.s      $f16, $f8, $f6
    /* 108290 150DADE0 24C60064 */  addiu      $a2, $a2, 0x64
    /* 108294 150DADE4 AFAC0024 */  sw         $t4, 0x24($sp)
    /* 108298 150DADE8 926A0001 */  lbu        $t2, 0x1($s3)
    /* 10829C 150DADEC 30D900FF */  andi       $t9, $a2, 0xFF
    /* 1082A0 150DADF0 44058000 */  mfc1       $a1, $f16
    /* 1082A4 150DADF4 03203025 */  or         $a2, $t9, $zero
    /* 1082A8 150DADF8 24040003 */  addiu      $a0, $zero, 0x3
    /* 1082AC 150DADFC 16800002 */  bnez       $s4, .L150DAE08
    /* 1082B0 150DAE00 00000000 */   nop
    /* 1082B4 150DAE04 0007000D */  break      7
  .L150DAE08:
    /* 1082B8 150DAE08 8FA70064 */  lw         $a3, 0x64($sp)
    /* 1082BC 150DAE0C 16400002 */  bnez       $s2, .L150DAE18
    /* 1082C0 150DAE10 00000000 */   nop
    /* 1082C4 150DAE14 0007000D */  break      7
  .L150DAE18:
    /* 1082C8 150DAE18 AFAA0028 */  sw         $t2, 0x28($sp)
    /* 1082CC 150DAE1C 0D4766E3 */  jal        func_151D9B8C
    /* 1082D0 150DAE20 00000000 */   nop
    /* 1082D4 150DAE24 C62A0040 */  lwc1       $f10, 0x40($s1)
    /* 1082D8 150DAE28 46165481 */  sub.s      $f18, $f10, $f22
    /* 1082DC 150DAE2C E6320040 */  swc1       $f18, 0x40($s1)
    /* 1082E0 150DAE30 C6240040 */  lwc1       $f4, 0x40($s1)
    /* 1082E4 150DAE34 4604B03C */  c.lt.s     $f22, $f4
    /* 1082E8 150DAE38 00000000 */  nop
    /* 1082EC 150DAE3C 4501FFCD */  bc1t       .L150DAD74
    /* 1082F0 150DAE40 00000000 */   nop
  .L150DAE44:
    /* 1082F4 150DAE44 8FBF005C */  lw         $ra, 0x5C($sp)
  .L150DAE48:
    /* 1082F8 150DAE48 D7B40038 */  ldc1       $f20, 0x38($sp)
    /* 1082FC 150DAE4C D7B60040 */  ldc1       $f22, 0x40($sp)
    /* 108300 150DAE50 8FB00048 */  lw         $s0, 0x48($sp)
    /* 108304 150DAE54 8FB1004C */  lw         $s1, 0x4C($sp)
    /* 108308 150DAE58 8FB20050 */  lw         $s2, 0x50($sp)
    /* 10830C 150DAE5C 8FB30054 */  lw         $s3, 0x54($sp)
    /* 108310 150DAE60 8FB40058 */  lw         $s4, 0x58($sp)
    /* 108314 150DAE64 03E00008 */  jr         $ra
    /* 108318 150DAE68 27BD01C8 */   addiu     $sp, $sp, 0x1C8
    /* 10831C 150DAE6C 00000000 */  nop
endlabel func_150DA67C
