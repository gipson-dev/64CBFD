glabel func_151D4794
    /* 201C44 151D4794 27BDFEF0 */  addiu      $sp, $sp, -0x110
    /* 201C48 151D4798 AFB20048 */  sw         $s2, 0x48($sp)
    /* 201C4C 151D479C 00809025 */  or         $s2, $a0, $zero
    /* 201C50 151D47A0 AFBF004C */  sw         $ra, 0x4C($sp)
    /* 201C54 151D47A4 AFB10044 */  sw         $s1, 0x44($sp)
    /* 201C58 151D47A8 AFB00040 */  sw         $s0, 0x40($sp)
    /* 201C5C 151D47AC F7BA0038 */  sdc1       $f26, 0x38($sp)
    /* 201C60 151D47B0 F7B80030 */  sdc1       $f24, 0x30($sp)
    /* 201C64 151D47B4 F7B60028 */  sdc1       $f22, 0x28($sp)
    /* 201C68 151D47B8 F7B40020 */  sdc1       $f20, 0x20($sp)
    /* 201C6C 151D47BC 8E41003C */  lw         $at, 0x3C($s2)
    /* 201C70 151D47C0 8E470028 */  lw         $a3, 0x28($s2)
    /* 201C74 151D47C4 27AE00FC */  addiu      $t6, $sp, 0xFC
    /* 201C78 151D47C8 ADC10000 */  sw         $at, 0x0($t6)
    /* 201C7C 151D47CC 8E590040 */  lw         $t9, 0x40($s2)
    /* 201C80 151D47D0 26500028 */  addiu      $s0, $s2, 0x28
    /* 201C84 151D47D4 240DFFFF */  addiu      $t5, $zero, -0x1
    /* 201C88 151D47D8 ADD90004 */  sw         $t9, 0x4($t6)
    /* 201C8C 151D47DC 8E410044 */  lw         $at, 0x44($s2)
    /* 201C90 151D47E0 ADC10008 */  sw         $at, 0x8($t6)
    /* 201C94 151D47E4 8CEA0000 */  lw         $t2, 0x0($a3)
    /* 201C98 151D47E8 92480038 */  lbu        $t0, 0x38($s2)
    /* 201C9C 151D47EC 11400005 */  beqz       $t2, .L151D4804
    /* 201CA0 151D47F0 31110001 */   andi      $s1, $t0, 0x1
    /* 201CA4 151D47F4 920B0004 */  lbu        $t3, 0x4($s0)
    /* 201CA8 151D47F8 90EC003B */  lbu        $t4, 0x3B($a3)
    /* 201CAC 151D47FC 516C0004 */  beql       $t3, $t4, .L151D4810
    /* 201CB0 151D4800 8CF801D4 */   lw        $t8, 0x1D4($a3)
  .L151D4804:
    /* 201CB4 151D4804 10000102 */  b          .L151D4C10
    /* 201CB8 151D4808 A64D000E */   sh        $t5, 0xE($s2)
    /* 201CBC 151D480C 8CF801D4 */  lw         $t8, 0x1D4($a3)
  .L151D4810:
    /* 201CC0 151D4810 13000013 */  beqz       $t8, .L151D4860
    /* 201CC4 151D4814 00000000 */   nop
    /* 201CC8 151D4818 90EF0074 */  lbu        $t7, 0x74($a3)
    /* 201CCC 151D481C 2401000F */  addiu      $at, $zero, 0xF
    /* 201CD0 151D4820 31EE000F */  andi       $t6, $t7, 0xF
    /* 201CD4 151D4824 11C1000E */  beq        $t6, $at, .L151D4860
    /* 201CD8 151D4828 00000000 */   nop
    /* 201CDC 151D482C 92190008 */  lbu        $t9, 0x8($s0)
    /* 201CE0 151D4830 00E02025 */  or         $a0, $a3, $zero
    /* 201CE4 151D4834 86050006 */  lh         $a1, 0x6($s0)
    /* 201CE8 151D4838 00194080 */  sll        $t0, $t9, 2
    /* 201CEC 151D483C 3C198009 */  lui        $t9, %hi(D_8008FC70)
    /* 201CF0 151D4840 0328C821 */  addu       $t9, $t9, $t0
    /* 201CF4 151D4844 8F39FC70 */  lw         $t9, %lo(D_8008FC70)($t9)
    /* 201CF8 151D4848 26060014 */  addiu      $a2, $s0, 0x14
    /* 201CFC 151D484C 0320F809 */  jalr       $t9
    /* 201D00 151D4850 00000000 */   nop
    /* 201D04 151D4854 92090010 */  lbu        $t1, 0x10($s0)
    /* 201D08 151D4858 352A0001 */  ori        $t2, $t1, 0x1
    /* 201D0C 151D485C A20A0010 */  sb         $t2, 0x10($s0)
  .L151D4860:
    /* 201D10 151D4860 122000EB */  beqz       $s1, .L151D4C10
    /* 201D14 151D4864 C7A600FC */   lwc1      $f6, 0xFC($sp)
    /* 201D18 151D4868 C6040014 */  lwc1       $f4, 0x14($s0)
    /* 201D1C 151D486C C7B20100 */  lwc1       $f18, 0x100($sp)
    /* 201D20 151D4870 27A400EC */  addiu      $a0, $sp, 0xEC
    /* 201D24 151D4874 46062201 */  sub.s      $f8, $f4, $f6
    /* 201D28 151D4878 E7A800EC */  swc1       $f8, 0xEC($sp)
    /* 201D2C 151D487C C60A0018 */  lwc1       $f10, 0x18($s0)
    /* 201D30 151D4880 C7A80104 */  lwc1       $f8, 0x104($sp)
    /* 201D34 151D4884 46125101 */  sub.s      $f4, $f10, $f18
    /* 201D38 151D4888 E7A400F0 */  swc1       $f4, 0xF0($sp)
    /* 201D3C 151D488C C606001C */  lwc1       $f6, 0x1C($s0)
    /* 201D40 151D4890 46083281 */  sub.s      $f10, $f6, $f8
    /* 201D44 151D4894 0D450F99 */  jal        func_15143E64
    /* 201D48 151D4898 E7AA00F4 */   swc1      $f10, 0xF4($sp)
    /* 201D4C 151D489C 3C0140A0 */  lui        $at, (0x40A00000 >> 16)
    /* 201D50 151D48A0 44819000 */  mtc1       $at, $f18
    /* 201D54 151D48A4 00000000 */  nop
    /* 201D58 151D48A8 4600903C */  c.lt.s     $f18, $f0
    /* 201D5C 151D48AC 00000000 */  nop
    /* 201D60 151D48B0 450300D8 */  bc1tl      .L151D4C14
    /* 201D64 151D48B4 8FBF004C */   lw        $ra, 0x4C($sp)
    /* 201D68 151D48B8 0D42B69A */  jal        func_150ADA68
    /* 201D6C 151D48BC 00000000 */   nop
    /* 201D70 151D48C0 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 201D74 151D48C4 4481D000 */  mtc1       $at, $f26
    /* 201D78 151D48C8 3C01800B */  lui        $at, %hi(D_800AB1FC)
    /* 201D7C 151D48CC C424B1FC */  lwc1       $f4, %lo(D_800AB1FC)($at)
    /* 201D80 151D48D0 3C01800B */  lui        $at, %hi(D_800AB200)
    /* 201D84 151D48D4 C426B200 */  lwc1       $f6, %lo(D_800AB200)($at)
    /* 201D88 151D48D8 3C01800C */  lui        $at, %hi(D_800BE9A4)
    /* 201D8C 151D48DC C432E9A4 */  lwc1       $f18, %lo(D_800BE9A4)($at)
    /* 201D90 151D48E0 46060202 */  mul.s      $f8, $f0, $f6
    /* 201D94 151D48E4 3C0D0020 */  lui        $t5, (0x200005 >> 16)
    /* 201D98 151D48E8 3C0E0090 */  lui        $t6, (0x90DE07 >> 16)
    /* 201D9C 151D48EC 3C01800B */  lui        $at, %hi(D_800AB204)
    /* 201DA0 151D48F0 240B006C */  addiu      $t3, $zero, 0x6C
    /* 201DA4 151D48F4 240C5103 */  addiu      $t4, $zero, 0x5103
    /* 201DA8 151D48F8 35AD0005 */  ori        $t5, $t5, (0x200005 & 0xFFFF)
    /* 201DAC 151D48FC 46082280 */  add.s      $f10, $f4, $f8
    /* 201DB0 151D4900 C604000C */  lwc1       $f4, 0xC($s0)
    /* 201DB4 151D4904 24180046 */  addiu      $t8, $zero, 0x46
    /* 201DB8 151D4908 240F0003 */  addiu      $t7, $zero, 0x3
    /* 201DBC 151D490C 46125182 */  mul.s      $f6, $f10, $f18
    /* 201DC0 151D4910 35CEDE07 */  ori        $t6, $t6, (0x90DE07 & 0xFFFF)
    /* 201DC4 151D4914 24080008 */  addiu      $t0, $zero, 0x8
    /* 201DC8 151D4918 24190006 */  addiu      $t9, $zero, 0x6
    /* 201DCC 151D491C 24090020 */  addiu      $t1, $zero, 0x20
    /* 201DD0 151D4920 240AFFFF */  addiu      $t2, $zero, -0x1
    /* 201DD4 151D4924 24110005 */  addiu      $s1, $zero, 0x5
    /* 201DD8 151D4928 46062200 */  add.s      $f8, $f4, $f6
    /* 201DDC 151D492C E608000C */  swc1       $f8, 0xC($s0)
    /* 201DE0 151D4930 C60A000C */  lwc1       $f10, 0xC($s0)
    /* 201DE4 151D4934 460AD03C */  c.lt.s     $f26, $f10
    /* 201DE8 151D4938 00000000 */  nop
    /* 201DEC 151D493C 450200B5 */  bc1fl      .L151D4C14
    /* 201DF0 151D4940 8FBF004C */   lw        $ra, 0x4C($sp)
    /* 201DF4 151D4944 44800000 */  mtc1       $zero, $f0
    /* 201DF8 151D4948 00000000 */  nop
    /* 201DFC 151D494C C432B204 */  lwc1       $f18, %lo(D_800AB204)($at)
    /* 201E00 151D4950 3C01800B */  lui        $at, %hi(D_800AB208)
    /* 201E04 151D4954 C424B208 */  lwc1       $f4, %lo(D_800AB208)($at)
    /* 201E08 151D4958 3C014220 */  lui        $at, (0x42200000 >> 16)
    /* 201E0C 151D495C 4481C000 */  mtc1       $at, $f24
    /* 201E10 151D4960 3C0140C0 */  lui        $at, (0x40C00000 >> 16)
    /* 201E14 151D4964 A3AB0099 */  sb         $t3, 0x99($sp)
    /* 201E18 151D4968 A7AC0084 */  sh         $t4, 0x84($sp)
    /* 201E1C 151D496C AFAD007C */  sw         $t5, 0x7C($sp)
    /* 201E20 151D4970 A7B8009A */  sh         $t8, 0x9A($sp)
    /* 201E24 151D4974 A7AF009C */  sh         $t7, 0x9C($sp)
    /* 201E28 151D4978 AFAE00D4 */  sw         $t6, 0xD4($sp)
    /* 201E2C 151D497C A3A800DC */  sb         $t0, 0xDC($sp)
    /* 201E30 151D4980 A3B900DD */  sb         $t9, 0xDD($sp)
    /* 201E34 151D4984 A3A900DE */  sb         $t1, 0xDE($sp)
    /* 201E38 151D4988 A3AA00DF */  sb         $t2, 0xDF($sp)
    /* 201E3C 151D498C 4481B000 */  mtc1       $at, $f22
    /* 201E40 151D4990 240BFFFF */  addiu      $t3, $zero, -0x1
    /* 201E44 151D4994 240C0046 */  addiu      $t4, $zero, 0x46
    /* 201E48 151D4998 240D00DD */  addiu      $t5, $zero, 0xDD
    /* 201E4C 151D499C 241800D3 */  addiu      $t8, $zero, 0xD3
    /* 201E50 151D49A0 240F00CD */  addiu      $t7, $zero, 0xCD
    /* 201E54 151D49A4 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 201E58 151D49A8 24080057 */  addiu      $t0, $zero, 0x57
    /* 201E5C 151D49AC 24190055 */  addiu      $t9, $zero, 0x55
    /* 201E60 151D49B0 2409005A */  addiu      $t1, $zero, 0x5A
    /* 201E64 151D49B4 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 201E68 151D49B8 3C01800B */  lui        $at, %hi(D_800AB20C)
    /* 201E6C 151D49BC AFA00080 */  sw         $zero, 0x80($sp)
    /* 201E70 151D49C0 AFA00088 */  sw         $zero, 0x88($sp)
    /* 201E74 151D49C4 AFA0008C */  sw         $zero, 0x8C($sp)
    /* 201E78 151D49C8 A3AB00E0 */  sb         $t3, 0xE0($sp)
    /* 201E7C 151D49CC A3A000E1 */  sb         $zero, 0xE1($sp)
    /* 201E80 151D49D0 A7AC009E */  sh         $t4, 0x9E($sp)
    /* 201E84 151D49D4 A3AD0090 */  sb         $t5, 0x90($sp)
    /* 201E88 151D49D8 A3B80091 */  sb         $t8, 0x91($sp)
    /* 201E8C 151D49DC A3AF0092 */  sb         $t7, 0x92($sp)
    /* 201E90 151D49E0 A3AE0093 */  sb         $t6, 0x93($sp)
    /* 201E94 151D49E4 A3A80094 */  sb         $t0, 0x94($sp)
    /* 201E98 151D49E8 A3B90095 */  sb         $t9, 0x95($sp)
    /* 201E9C 151D49EC A3A90096 */  sb         $t1, 0x96($sp)
    /* 201EA0 151D49F0 A3AA0098 */  sb         $t2, 0x98($sp)
    /* 201EA4 151D49F4 E7A000B8 */  swc1       $f0, 0xB8($sp)
    /* 201EA8 151D49F8 E7A000BC */  swc1       $f0, 0xBC($sp)
    /* 201EAC 151D49FC E7A000C0 */  swc1       $f0, 0xC0($sp)
    /* 201EB0 151D4A00 C434B20C */  lwc1       $f20, %lo(D_800AB20C)($at)
    /* 201EB4 151D4A04 E7B20078 */  swc1       $f18, 0x78($sp)
    /* 201EB8 151D4A08 E7A400A0 */  swc1       $f4, 0xA0($sp)
  .L151D4A0C:
    /* 201EBC 151D4A0C 0D42B69A */  jal        func_150ADA68
    /* 201EC0 151D4A10 00000000 */   nop
    /* 201EC4 151D4A14 C7AC00EC */  lwc1       $f12, 0xEC($sp)
    /* 201EC8 151D4A18 C7AE00F0 */  lwc1       $f14, 0xF0($sp)
    /* 201ECC 151D4A1C C7A800FC */  lwc1       $f8, 0xFC($sp)
    /* 201ED0 151D4A20 46006182 */  mul.s      $f6, $f12, $f0
    /* 201ED4 151D4A24 C7B000F4 */  lwc1       $f16, 0xF4($sp)
    /* 201ED8 151D4A28 C7A40100 */  lwc1       $f4, 0x100($sp)
    /* 201EDC 151D4A2C 46007482 */  mul.s      $f18, $f14, $f0
    /* 201EE0 151D4A30 3C01800C */  lui        $at, %hi(D_800BE9A8)
    /* 201EE4 151D4A34 46083280 */  add.s      $f10, $f6, $f8
    /* 201EE8 151D4A38 46008202 */  mul.s      $f8, $f16, $f0
    /* 201EEC 151D4A3C 46049180 */  add.s      $f6, $f18, $f4
    /* 201EF0 151D4A40 E7AA00AC */  swc1       $f10, 0xAC($sp)
    /* 201EF4 151D4A44 C7AA0104 */  lwc1       $f10, 0x104($sp)
    /* 201EF8 151D4A48 E7A600B0 */  swc1       $f6, 0xB0($sp)
    /* 201EFC 151D4A4C 460A4480 */  add.s      $f18, $f8, $f10
    /* 201F00 151D4A50 E7B200B4 */  swc1       $f18, 0xB4($sp)
    /* 201F04 151D4A54 C422E9A8 */  lwc1       $f2, %lo(D_800BE9A8)($at)
    /* 201F08 151D4A58 46026102 */  mul.s      $f4, $f12, $f2
    /* 201F0C 151D4A5C 00000000 */  nop
    /* 201F10 151D4A60 46142182 */  mul.s      $f6, $f4, $f20
    /* 201F14 151D4A64 00000000 */  nop
    /* 201F18 151D4A68 46027202 */  mul.s      $f8, $f14, $f2
    /* 201F1C 151D4A6C E7A600C4 */  swc1       $f6, 0xC4($sp)
    /* 201F20 151D4A70 46144282 */  mul.s      $f10, $f8, $f20
    /* 201F24 151D4A74 00000000 */  nop
    /* 201F28 151D4A78 46028482 */  mul.s      $f18, $f16, $f2
    /* 201F2C 151D4A7C E7AA00C8 */  swc1       $f10, 0xC8($sp)
    /* 201F30 151D4A80 46149102 */  mul.s      $f4, $f18, $f20
    /* 201F34 151D4A84 0D42B688 */  jal        func_150ADA20
    /* 201F38 151D4A88 E7A400CC */   swc1      $f4, 0xCC($sp)
    /* 201F3C 151D4A8C 0D42B688 */  jal        func_150ADA20
    /* 201F40 151D4A90 A3A2006C */   sb        $v0, 0x6C($sp)
    /* 201F44 151D4A94 00406025 */  or         $t4, $v0, $zero
    /* 201F48 151D4A98 0D42B688 */  jal        func_150ADA20
    /* 201F4C 151D4A9C A3AC006D */   sb        $t4, 0x6D($sp)
    /* 201F50 151D4AA0 0051001B */  divu       $zero, $v0, $s1
    /* 201F54 151D4AA4 00006810 */  mfhi       $t5
    /* 201F58 151D4AA8 25B80004 */  addiu      $t8, $t5, 0x4
    /* 201F5C 151D4AAC 16200002 */  bnez       $s1, .L151D4AB8
    /* 201F60 151D4AB0 00000000 */   nop
    /* 201F64 151D4AB4 0007000D */  break      7
  .L151D4AB8:
    /* 201F68 151D4AB8 A3B8006E */  sb         $t8, 0x6E($sp)
    /* 201F6C 151D4ABC 0D42B688 */  jal        func_150ADA20
    /* 201F70 151D4AC0 00000000 */   nop
    /* 201F74 151D4AC4 0051001B */  divu       $zero, $v0, $s1
    /* 201F78 151D4AC8 00007810 */  mfhi       $t7
    /* 201F7C 151D4ACC 25EE0004 */  addiu      $t6, $t7, 0x4
    /* 201F80 151D4AD0 16200002 */  bnez       $s1, .L151D4ADC
    /* 201F84 151D4AD4 00000000 */   nop
    /* 201F88 151D4AD8 0007000D */  break      7
  .L151D4ADC:
    /* 201F8C 151D4ADC A3AE006F */  sb         $t6, 0x6F($sp)
    /* 201F90 151D4AE0 0D42B69A */  jal        func_150ADA68
    /* 201F94 151D4AE4 00000000 */   nop
    /* 201F98 151D4AE8 46160182 */  mul.s      $f6, $f0, $f22
    /* 201F9C 151D4AEC 0D42B69A */  jal        func_150ADA68
    /* 201FA0 151D4AF0 E7A60070 */   swc1      $f6, 0x70($sp)
    /* 201FA4 151D4AF4 46160202 */  mul.s      $f8, $f0, $f22
    /* 201FA8 151D4AF8 0D42B69A */  jal        func_150ADA68
    /* 201FAC 151D4AFC E7A80074 */   swc1      $f8, 0x74($sp)
    /* 201FB0 151D4B00 3C01800B */  lui        $at, %hi(D_800AB210)
    /* 201FB4 151D4B04 C42AB210 */  lwc1       $f10, %lo(D_800AB210)($at)
    /* 201FB8 151D4B08 3C01800B */  lui        $at, %hi(D_800AB214)
    /* 201FBC 151D4B0C C424B214 */  lwc1       $f4, %lo(D_800AB214)($at)
    /* 201FC0 151D4B10 460A0482 */  mul.s      $f18, $f0, $f10
    /* 201FC4 151D4B14 8FA800D4 */  lw         $t0, 0xD4($sp)
    /* 201FC8 151D4B18 2401FF3F */  addiu      $at, $zero, -0xC1
    /* 201FCC 151D4B1C 0101C824 */  and        $t9, $t0, $at
    /* 201FD0 151D4B20 AFB900D4 */  sw         $t9, 0xD4($sp)
    /* 201FD4 151D4B24 46049180 */  add.s      $f6, $f18, $f4
    /* 201FD8 151D4B28 0D42B688 */  jal        func_150ADA20
    /* 201FDC 151D4B2C E7A600D0 */   swc1      $f6, 0xD0($sp)
    /* 201FE0 151D4B30 30490001 */  andi       $t1, $v0, 0x1
    /* 201FE4 151D4B34 11200003 */  beqz       $t1, .L151D4B44
    /* 201FE8 151D4B38 00001825 */   or        $v1, $zero, $zero
    /* 201FEC 151D4B3C 10000001 */  b          .L151D4B44
    /* 201FF0 151D4B40 24030080 */   addiu     $v1, $zero, 0x80
  .L151D4B44:
    /* 201FF4 151D4B44 0D42B688 */  jal        func_150ADA20
    /* 201FF8 151D4B48 AFA30058 */   sw        $v1, 0x58($sp)
    /* 201FFC 151D4B4C 304A0001 */  andi       $t2, $v0, 0x1
    /* 202000 151D4B50 11400003 */  beqz       $t2, .L151D4B60
    /* 202004 151D4B54 8FA30058 */   lw        $v1, 0x58($sp)
    /* 202008 151D4B58 10000002 */  b          .L151D4B64
    /* 20200C 151D4B5C 24020040 */   addiu     $v0, $zero, 0x40
  .L151D4B60:
    /* 202010 151D4B60 00001025 */  or         $v0, $zero, $zero
  .L151D4B64:
    /* 202014 151D4B64 8FAB00D4 */  lw         $t3, 0xD4($sp)
    /* 202018 151D4B68 00436025 */  or         $t4, $v0, $v1
    /* 20201C 151D4B6C 016C6825 */  or         $t5, $t3, $t4
    /* 202020 151D4B70 0D42B688 */  jal        func_150ADA20
    /* 202024 151D4B74 AFAD00D4 */   sw        $t5, 0xD4($sp)
    /* 202028 151D4B78 2401003D */  addiu      $at, $zero, 0x3D
    /* 20202C 151D4B7C 0041001B */  divu       $zero, $v0, $at
    /* 202030 151D4B80 0000C010 */  mfhi       $t8
    /* 202034 151D4B84 270F003C */  addiu      $t7, $t8, 0x3C
    /* 202038 151D4B88 0D42B688 */  jal        func_150ADA20
    /* 20203C 151D4B8C A3AF0097 */   sb        $t7, 0x97($sp)
    /* 202040 151D4B90 2401000B */  addiu      $at, $zero, 0xB
    /* 202044 151D4B94 0041001B */  divu       $zero, $v0, $at
    /* 202048 151D4B98 00007010 */  mfhi       $t6
    /* 20204C 151D4B9C 25C80046 */  addiu      $t0, $t6, 0x46
    /* 202050 151D4BA0 0D42B69A */  jal        func_150ADA68
    /* 202054 151D4BA4 A7A80086 */   sh        $t0, 0x86($sp)
    /* 202058 151D4BA8 46180202 */  mul.s      $f8, $f0, $f24
    /* 20205C 151D4BAC 27A4007C */  addiu      $a0, $sp, 0x7C
    /* 202060 151D4BB0 24050001 */  addiu      $a1, $zero, 0x1
    /* 202064 151D4BB4 00003025 */  or         $a2, $zero, $zero
    /* 202068 151D4BB8 24070010 */  addiu      $a3, $zero, 0x10
    /* 20206C 151D4BBC 46184280 */  add.s      $f10, $f8, $f24
    /* 202070 151D4BC0 E7AA00A8 */  swc1       $f10, 0xA8($sp)
    /* 202074 151D4BC4 E7AA00A4 */  swc1       $f10, 0xA4($sp)
    /* 202078 151D4BC8 9259000C */  lbu        $t9, 0xC($s2)
    /* 20207C 151D4BCC AFB90010 */  sw         $t9, 0x10($sp)
    /* 202080 151D4BD0 92490001 */  lbu        $t1, 0x1($s2)
    /* 202084 151D4BD4 0D44C0A0 */  jal        func_15130280
    /* 202088 151D4BD8 AFA90014 */   sw        $t1, 0x14($sp)
    /* 20208C 151D4BDC 10400004 */  beqz       $v0, .L151D4BF0
    /* 202090 151D4BE0 244400A8 */   addiu     $a0, $v0, 0xA8
    /* 202094 151D4BE4 27A5006C */  addiu      $a1, $sp, 0x6C
    /* 202098 151D4BE8 0C008BB0 */  jal        memcpy
    /* 20209C 151D4BEC 24060010 */   addiu     $a2, $zero, 0x10
  .L151D4BF0:
    /* 2020A0 151D4BF0 C612000C */  lwc1       $f18, 0xC($s0)
    /* 2020A4 151D4BF4 461A9101 */  sub.s      $f4, $f18, $f26
    /* 2020A8 151D4BF8 E604000C */  swc1       $f4, 0xC($s0)
    /* 2020AC 151D4BFC C606000C */  lwc1       $f6, 0xC($s0)
    /* 2020B0 151D4C00 4606D03C */  c.lt.s     $f26, $f6
    /* 2020B4 151D4C04 00000000 */  nop
    /* 2020B8 151D4C08 4501FF80 */  bc1t       .L151D4A0C
    /* 2020BC 151D4C0C 00000000 */   nop
  .L151D4C10:
    /* 2020C0 151D4C10 8FBF004C */  lw         $ra, 0x4C($sp)
  .L151D4C14:
    /* 2020C4 151D4C14 D7B40020 */  ldc1       $f20, 0x20($sp)
    /* 2020C8 151D4C18 D7B60028 */  ldc1       $f22, 0x28($sp)
    /* 2020CC 151D4C1C D7B80030 */  ldc1       $f24, 0x30($sp)
    /* 2020D0 151D4C20 D7BA0038 */  ldc1       $f26, 0x38($sp)
    /* 2020D4 151D4C24 8FB00040 */  lw         $s0, 0x40($sp)
    /* 2020D8 151D4C28 8FB10044 */  lw         $s1, 0x44($sp)
    /* 2020DC 151D4C2C 8FB20048 */  lw         $s2, 0x48($sp)
    /* 2020E0 151D4C30 03E00008 */  jr         $ra
    /* 2020E4 151D4C34 27BD0110 */   addiu     $sp, $sp, 0x110
endlabel func_151D4794
