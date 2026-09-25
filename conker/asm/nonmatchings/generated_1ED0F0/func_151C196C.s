glabel func_151C196C
    /* 1EEE1C 151C196C 27BDFFA8 */  addiu      $sp, $sp, -0x58
    /* 1EEE20 151C1970 AFB10040 */  sw         $s1, 0x40($sp)
    /* 1EEE24 151C1974 AFB0003C */  sw         $s0, 0x3C($sp)
    /* 1EEE28 151C1978 00808025 */  or         $s0, $a0, $zero
    /* 1EEE2C 151C197C 00A08825 */  or         $s1, $a1, $zero
    /* 1EEE30 151C1980 AFBF004C */  sw         $ra, 0x4C($sp)
    /* 1EEE34 151C1984 AFB30048 */  sw         $s3, 0x48($sp)
    /* 1EEE38 151C1988 AFB20044 */  sw         $s2, 0x44($sp)
    /* 1EEE3C 151C198C AFA60060 */  sw         $a2, 0x60($sp)
    /* 1EEE40 151C1990 AFA70064 */  sw         $a3, 0x64($sp)
    /* 1EEE44 151C1994 8FAE0064 */  lw         $t6, 0x64($sp)
    /* 1EEE48 151C1998 24030001 */  addiu      $v1, $zero, 0x1
    /* 1EEE4C 151C199C A3A00056 */  sb         $zero, 0x56($sp)
    /* 1EEE50 151C19A0 11C0007E */  beqz       $t6, .L151C1B9C
    /* 1EEE54 151C19A4 8FAF0068 */   lw        $t7, 0x68($sp)
    /* 1EEE58 151C19A8 51E0007D */  beql       $t7, $zero, .L151C1BA0
    /* 1EEE5C 151C19AC 8E210000 */   lw        $at, 0x0($s1)
    /* 1EEE60 151C19B0 8DC10000 */  lw         $at, 0x0($t6)
    /* 1EEE64 151C19B4 2612002C */  addiu      $s2, $s0, 0x2C
    /* 1EEE68 151C19B8 26130038 */  addiu      $s3, $s0, 0x38
    /* 1EEE6C 151C19BC AE410000 */  sw         $at, 0x0($s2)
    /* 1EEE70 151C19C0 8DD90004 */  lw         $t9, 0x4($t6)
    /* 1EEE74 151C19C4 44802000 */  mtc1       $zero, $f4
    /* 1EEE78 151C19C8 240B0001 */  addiu      $t3, $zero, 0x1
    /* 1EEE7C 151C19CC AE590004 */  sw         $t9, 0x4($s2)
    /* 1EEE80 151C19D0 8DC10008 */  lw         $at, 0x8($t6)
    /* 1EEE84 151C19D4 240C0003 */  addiu      $t4, $zero, 0x3
    /* 1EEE88 151C19D8 02603025 */  or         $a2, $s3, $zero
    /* 1EEE8C 151C19DC AE410008 */  sw         $at, 0x8($s2)
    /* 1EEE90 151C19E0 8FA80068 */  lw         $t0, 0x68($sp)
    /* 1EEE94 151C19E4 02402825 */  or         $a1, $s2, $zero
    /* 1EEE98 151C19E8 02003825 */  or         $a3, $s0, $zero
    /* 1EEE9C 151C19EC 8D010000 */  lw         $at, 0x0($t0)
    /* 1EEEA0 151C19F0 AE610000 */  sw         $at, 0x0($s3)
    /* 1EEEA4 151C19F4 8D0A0004 */  lw         $t2, 0x4($t0)
    /* 1EEEA8 151C19F8 AE6A0004 */  sw         $t2, 0x4($s3)
    /* 1EEEAC 151C19FC 8D010008 */  lw         $at, 0x8($t0)
    /* 1EEEB0 151C1A00 AE610008 */  sw         $at, 0x8($s3)
    /* 1EEEB4 151C1A04 8FB90080 */  lw         $t9, 0x80($sp)
    /* 1EEEB8 151C1A08 8FAE007C */  lw         $t6, 0x7C($sp)
    /* 1EEEBC 151C1A0C 8FB80078 */  lw         $t8, 0x78($sp)
    /* 1EEEC0 151C1A10 8FAF0074 */  lw         $t7, 0x74($sp)
    /* 1EEEC4 151C1A14 8FAD0070 */  lw         $t5, 0x70($sp)
    /* 1EEEC8 151C1A18 A3A30057 */  sb         $v1, 0x57($sp)
    /* 1EEECC 151C1A1C AFAC0020 */  sw         $t4, 0x20($sp)
    /* 1EEED0 151C1A20 AFAB001C */  sw         $t3, 0x1C($sp)
    /* 1EEED4 151C1A24 AFA00018 */  sw         $zero, 0x18($sp)
    /* 1EEED8 151C1A28 AFA00014 */  sw         $zero, 0x14($sp)
    /* 1EEEDC 151C1A2C 8FA4006C */  lw         $a0, 0x6C($sp)
    /* 1EEEE0 151C1A30 E7A40010 */  swc1       $f4, 0x10($sp)
    /* 1EEEE4 151C1A34 AFB90034 */  sw         $t9, 0x34($sp)
    /* 1EEEE8 151C1A38 AFAE0030 */  sw         $t6, 0x30($sp)
    /* 1EEEEC 151C1A3C AFB8002C */  sw         $t8, 0x2C($sp)
    /* 1EEEF0 151C1A40 AFAF0028 */  sw         $t7, 0x28($sp)
    /* 1EEEF4 151C1A44 0D470757 */  jal        func_151C1D5C
    /* 1EEEF8 151C1A48 AFAD0024 */   sw        $t5, 0x24($sp)
    /* 1EEEFC 151C1A4C 92090059 */  lbu        $t1, 0x59($s0)
    /* 1EEF00 151C1A50 93A30057 */  lbu        $v1, 0x57($sp)
    /* 1EEF04 151C1A54 55200024 */  bnel       $t1, $zero, .L151C1AE8
    /* 1EEF08 151C1A58 C606002C */   lwc1      $f6, 0x2C($s0)
    /* 1EEF0C 151C1A5C C606002C */  lwc1       $f6, 0x2C($s0)
    /* 1EEF10 151C1A60 C6280000 */  lwc1       $f8, 0x0($s1)
    /* 1EEF14 151C1A64 46083032 */  c.eq.s     $f6, $f8
    /* 1EEF18 151C1A68 00000000 */  nop
    /* 1EEF1C 151C1A6C 4502000E */  bc1fl      .L151C1AA8
    /* 1EEF20 151C1A70 8E210000 */   lw        $at, 0x0($s1)
    /* 1EEF24 151C1A74 C60A0030 */  lwc1       $f10, 0x30($s0)
    /* 1EEF28 151C1A78 C6300004 */  lwc1       $f16, 0x4($s1)
    /* 1EEF2C 151C1A7C 46105032 */  c.eq.s     $f10, $f16
    /* 1EEF30 151C1A80 00000000 */  nop
    /* 1EEF34 151C1A84 45020008 */  bc1fl      .L151C1AA8
    /* 1EEF38 151C1A88 8E210000 */   lw        $at, 0x0($s1)
    /* 1EEF3C 151C1A8C C6120034 */  lwc1       $f18, 0x34($s0)
    /* 1EEF40 151C1A90 C6240008 */  lwc1       $f4, 0x8($s1)
    /* 1EEF44 151C1A94 46049032 */  c.eq.s     $f18, $f4
    /* 1EEF48 151C1A98 00000000 */  nop
    /* 1EEF4C 151C1A9C 4501000F */  bc1t       .L151C1ADC
    /* 1EEF50 151C1AA0 00000000 */   nop
    /* 1EEF54 151C1AA4 8E210000 */  lw         $at, 0x0($s1)
  .L151C1AA8:
    /* 1EEF58 151C1AA8 AE410000 */  sw         $at, 0x0($s2)
    /* 1EEF5C 151C1AAC 8E2A0004 */  lw         $t2, 0x4($s1)
    /* 1EEF60 151C1AB0 AE4A0004 */  sw         $t2, 0x4($s2)
    /* 1EEF64 151C1AB4 8E210008 */  lw         $at, 0x8($s1)
    /* 1EEF68 151C1AB8 AE410008 */  sw         $at, 0x8($s2)
    /* 1EEF6C 151C1ABC 8FAB0068 */  lw         $t3, 0x68($sp)
    /* 1EEF70 151C1AC0 8D610000 */  lw         $at, 0x0($t3)
    /* 1EEF74 151C1AC4 AE610000 */  sw         $at, 0x0($s3)
    /* 1EEF78 151C1AC8 8D6D0004 */  lw         $t5, 0x4($t3)
    /* 1EEF7C 151C1ACC AE6D0004 */  sw         $t5, 0x4($s3)
    /* 1EEF80 151C1AD0 8D610008 */  lw         $at, 0x8($t3)
    /* 1EEF84 151C1AD4 10000040 */  b          .L151C1BD8
    /* 1EEF88 151C1AD8 AE610008 */   sw        $at, 0x8($s3)
  .L151C1ADC:
    /* 1EEF8C 151C1ADC 1000003E */  b          .L151C1BD8
    /* 1EEF90 151C1AE0 00001825 */   or        $v1, $zero, $zero
    /* 1EEF94 151C1AE4 C606002C */  lwc1       $f6, 0x2C($s0)
  .L151C1AE8:
    /* 1EEF98 151C1AE8 C6280000 */  lwc1       $f8, 0x0($s1)
    /* 1EEF9C 151C1AEC 46083032 */  c.eq.s     $f6, $f8
    /* 1EEFA0 151C1AF0 00000000 */  nop
    /* 1EEFA4 151C1AF4 4502000E */  bc1fl      .L151C1B30
    /* 1EEFA8 151C1AF8 8E210000 */   lw        $at, 0x0($s1)
    /* 1EEFAC 151C1AFC C60A0030 */  lwc1       $f10, 0x30($s0)
    /* 1EEFB0 151C1B00 C6300004 */  lwc1       $f16, 0x4($s1)
    /* 1EEFB4 151C1B04 46105032 */  c.eq.s     $f10, $f16
    /* 1EEFB8 151C1B08 00000000 */  nop
    /* 1EEFBC 151C1B0C 45020008 */  bc1fl      .L151C1B30
    /* 1EEFC0 151C1B10 8E210000 */   lw        $at, 0x0($s1)
    /* 1EEFC4 151C1B14 C6120034 */  lwc1       $f18, 0x34($s0)
    /* 1EEFC8 151C1B18 C6240008 */  lwc1       $f4, 0x8($s1)
    /* 1EEFCC 151C1B1C 46049032 */  c.eq.s     $f18, $f4
    /* 1EEFD0 151C1B20 00000000 */  nop
    /* 1EEFD4 151C1B24 4501002C */  bc1t       .L151C1BD8
    /* 1EEFD8 151C1B28 00000000 */   nop
    /* 1EEFDC 151C1B2C 8E210000 */  lw         $at, 0x0($s1)
  .L151C1B30:
    /* 1EEFE0 151C1B30 02602025 */  or         $a0, $s3, $zero
    /* 1EEFE4 151C1B34 02602825 */  or         $a1, $s3, $zero
    /* 1EEFE8 151C1B38 AE410000 */  sw         $at, 0x0($s2)
    /* 1EEFEC 151C1B3C 8E380004 */  lw         $t8, 0x4($s1)
    /* 1EEFF0 151C1B40 26060004 */  addiu      $a2, $s0, 0x4
    /* 1EEFF4 151C1B44 00003825 */  or         $a3, $zero, $zero
    /* 1EEFF8 151C1B48 AE580004 */  sw         $t8, 0x4($s2)
    /* 1EEFFC 151C1B4C 8E210008 */  lw         $at, 0x8($s1)
    /* 1EF000 151C1B50 AE410008 */  sw         $at, 0x8($s2)
    /* 1EF004 151C1B54 C6280000 */  lwc1       $f8, 0x0($s1)
    /* 1EF008 151C1B58 C6060008 */  lwc1       $f6, 0x8($s0)
    /* 1EF00C 151C1B5C C610000C */  lwc1       $f16, 0xC($s0)
    /* 1EF010 151C1B60 46083281 */  sub.s      $f10, $f6, $f8
    /* 1EF014 151C1B64 C6060010 */  lwc1       $f6, 0x10($s0)
    /* 1EF018 151C1B68 E60A0038 */  swc1       $f10, 0x38($s0)
    /* 1EF01C 151C1B6C C6320004 */  lwc1       $f18, 0x4($s1)
    /* 1EF020 151C1B70 46128101 */  sub.s      $f4, $f16, $f18
    /* 1EF024 151C1B74 E604003C */  swc1       $f4, 0x3C($s0)
    /* 1EF028 151C1B78 C6280008 */  lwc1       $f8, 0x8($s1)
    /* 1EF02C 151C1B7C 46083281 */  sub.s      $f10, $f6, $f8
    /* 1EF030 151C1B80 E60A0040 */  swc1       $f10, 0x40($s0)
    /* 1EF034 151C1B84 0D45144A */  jal        func_15145128
    /* 1EF038 151C1B88 A3A30057 */   sb        $v1, 0x57($sp)
    /* 1EF03C 151C1B8C 14400012 */  bnez       $v0, .L151C1BD8
    /* 1EF040 151C1B90 93A30057 */   lbu       $v1, 0x57($sp)
    /* 1EF044 151C1B94 1000006A */  b          .L151C1D40
    /* 1EF048 151C1B98 00001025 */   or        $v0, $zero, $zero
  .L151C1B9C:
    /* 1EF04C 151C1B9C 8E210000 */  lw         $at, 0x0($s1)
  .L151C1BA0:
    /* 1EF050 151C1BA0 2612002C */  addiu      $s2, $s0, 0x2C
    /* 1EF054 151C1BA4 26130038 */  addiu      $s3, $s0, 0x38
    /* 1EF058 151C1BA8 AE410000 */  sw         $at, 0x0($s2)
    /* 1EF05C 151C1BAC 8E390004 */  lw         $t9, 0x4($s1)
    /* 1EF060 151C1BB0 AE590004 */  sw         $t9, 0x4($s2)
    /* 1EF064 151C1BB4 8E210008 */  lw         $at, 0x8($s1)
    /* 1EF068 151C1BB8 AE410008 */  sw         $at, 0x8($s2)
    /* 1EF06C 151C1BBC 8FA90060 */  lw         $t1, 0x60($sp)
    /* 1EF070 151C1BC0 8D210000 */  lw         $at, 0x0($t1)
    /* 1EF074 151C1BC4 AE610000 */  sw         $at, 0x0($s3)
    /* 1EF078 151C1BC8 8D2A0004 */  lw         $t2, 0x4($t1)
    /* 1EF07C 151C1BCC AE6A0004 */  sw         $t2, 0x4($s3)
    /* 1EF080 151C1BD0 8D210008 */  lw         $at, 0x8($t1)
    /* 1EF084 151C1BD4 AE610008 */  sw         $at, 0x8($s3)
  .L151C1BD8:
    /* 1EF088 151C1BD8 1060001D */  beqz       $v1, .L151C1C50
    /* 1EF08C 151C1BDC 8FA4006C */   lw        $a0, 0x6C($sp)
    /* 1EF090 151C1BE0 44808000 */  mtc1       $zero, $f16
    /* 1EF094 151C1BE4 8FAF0070 */  lw         $t7, 0x70($sp)
    /* 1EF098 151C1BE8 8FB80074 */  lw         $t8, 0x74($sp)
    /* 1EF09C 151C1BEC 8FAE0078 */  lw         $t6, 0x78($sp)
    /* 1EF0A0 151C1BF0 8FB9007C */  lw         $t9, 0x7C($sp)
    /* 1EF0A4 151C1BF4 8FA80080 */  lw         $t0, 0x80($sp)
    /* 1EF0A8 151C1BF8 240C0001 */  addiu      $t4, $zero, 0x1
    /* 1EF0AC 151C1BFC 240B0001 */  addiu      $t3, $zero, 0x1
    /* 1EF0B0 151C1C00 240D0003 */  addiu      $t5, $zero, 0x3
    /* 1EF0B4 151C1C04 AFAD0020 */  sw         $t5, 0x20($sp)
    /* 1EF0B8 151C1C08 AFAB001C */  sw         $t3, 0x1C($sp)
    /* 1EF0BC 151C1C0C AFAC0018 */  sw         $t4, 0x18($sp)
    /* 1EF0C0 151C1C10 02402825 */  or         $a1, $s2, $zero
    /* 1EF0C4 151C1C14 02603025 */  or         $a2, $s3, $zero
    /* 1EF0C8 151C1C18 02003825 */  or         $a3, $s0, $zero
    /* 1EF0CC 151C1C1C AFA00014 */  sw         $zero, 0x14($sp)
    /* 1EF0D0 151C1C20 AFAF0024 */  sw         $t7, 0x24($sp)
    /* 1EF0D4 151C1C24 E7B00010 */  swc1       $f16, 0x10($sp)
    /* 1EF0D8 151C1C28 AFB80028 */  sw         $t8, 0x28($sp)
    /* 1EF0DC 151C1C2C AFAE002C */  sw         $t6, 0x2C($sp)
    /* 1EF0E0 151C1C30 AFB90030 */  sw         $t9, 0x30($sp)
    /* 1EF0E4 151C1C34 0D470757 */  jal        func_151C1D5C
    /* 1EF0E8 151C1C38 AFA80034 */   sw        $t0, 0x34($sp)
    /* 1EF0EC 151C1C3C 92090059 */  lbu        $t1, 0x59($s0)
    /* 1EF0F0 151C1C40 240A0001 */  addiu      $t2, $zero, 0x1
    /* 1EF0F4 151C1C44 51200003 */  beql       $t1, $zero, .L151C1C54
    /* 1EF0F8 151C1C48 93AC0056 */   lbu       $t4, 0x56($sp)
    /* 1EF0FC 151C1C4C A3AA0056 */  sb         $t2, 0x56($sp)
  .L151C1C50:
    /* 1EF100 151C1C50 93AC0056 */  lbu        $t4, 0x56($sp)
  .L151C1C54:
    /* 1EF104 151C1C54 3C01800B */  lui        $at, %hi(D_800AA9C0)
    /* 1EF108 151C1C58 55800039 */  bnel       $t4, $zero, .L151C1D40
    /* 1EF10C 151C1C5C 24020001 */   addiu     $v0, $zero, 0x1
    /* 1EF110 151C1C60 C420A9C0 */  lwc1       $f0, %lo(D_800AA9C0)($at)
    /* 1EF114 151C1C64 AE000000 */  sw         $zero, 0x0($s0)
    /* 1EF118 151C1C68 E6000004 */  swc1       $f0, 0x4($s0)
    /* 1EF11C 151C1C6C 8E210000 */  lw         $at, 0x0($s1)
    /* 1EF120 151C1C70 AE410000 */  sw         $at, 0x0($s2)
    /* 1EF124 151C1C74 8E2D0004 */  lw         $t5, 0x4($s1)
    /* 1EF128 151C1C78 AE4D0004 */  sw         $t5, 0x4($s2)
    /* 1EF12C 151C1C7C 8E210008 */  lw         $at, 0x8($s1)
    /* 1EF130 151C1C80 AE410008 */  sw         $at, 0x8($s2)
    /* 1EF134 151C1C84 8FAF0068 */  lw         $t7, 0x68($sp)
    /* 1EF138 151C1C88 8FA30060 */  lw         $v1, 0x60($sp)
    /* 1EF13C 151C1C8C 11E00003 */  beqz       $t7, .L151C1C9C
    /* 1EF140 151C1C90 00000000 */   nop
    /* 1EF144 151C1C94 10000001 */  b          .L151C1C9C
    /* 1EF148 151C1C98 01E01825 */   or        $v1, $t7, $zero
  .L151C1C9C:
    /* 1EF14C 151C1C9C 8C610000 */  lw         $at, 0x0($v1)
    /* 1EF150 151C1CA0 26020008 */  addiu      $v0, $s0, 0x8
    /* 1EF154 151C1CA4 AE610000 */  sw         $at, 0x0($s3)
    /* 1EF158 151C1CA8 8C6E0004 */  lw         $t6, 0x4($v1)
    /* 1EF15C 151C1CAC AE6E0004 */  sw         $t6, 0x4($s3)
    /* 1EF160 151C1CB0 8C610008 */  lw         $at, 0x8($v1)
    /* 1EF164 151C1CB4 AE610008 */  sw         $at, 0x8($s3)
    /* 1EF168 151C1CB8 C6040038 */  lwc1       $f4, 0x38($s0)
    /* 1EF16C 151C1CBC C612002C */  lwc1       $f18, 0x2C($s0)
    /* 1EF170 151C1CC0 C610003C */  lwc1       $f16, 0x3C($s0)
    /* 1EF174 151C1CC4 46002182 */  mul.s      $f6, $f4, $f0
    /* 1EF178 151C1CC8 C60A0030 */  lwc1       $f10, 0x30($s0)
    /* 1EF17C 151C1CCC 46008102 */  mul.s      $f4, $f16, $f0
    /* 1EF180 151C1CD0 46069200 */  add.s      $f8, $f18, $f6
    /* 1EF184 151C1CD4 C6060034 */  lwc1       $f6, 0x34($s0)
    /* 1EF188 151C1CD8 46045480 */  add.s      $f18, $f10, $f4
    /* 1EF18C 151C1CDC E6080008 */  swc1       $f8, 0x8($s0)
    /* 1EF190 151C1CE0 C6080040 */  lwc1       $f8, 0x40($s0)
    /* 1EF194 151C1CE4 E612000C */  swc1       $f18, 0xC($s0)
    /* 1EF198 151C1CE8 46004402 */  mul.s      $f16, $f8, $f0
    /* 1EF19C 151C1CEC 46103280 */  add.s      $f10, $f6, $f16
    /* 1EF1A0 151C1CF0 E60A0010 */  swc1       $f10, 0x10($s0)
    /* 1EF1A4 151C1CF4 8C410000 */  lw         $at, 0x0($v0)
    /* 1EF1A8 151C1CF8 AE010014 */  sw         $at, 0x14($s0)
    /* 1EF1AC 151C1CFC 8C480004 */  lw         $t0, 0x4($v0)
    /* 1EF1B0 151C1D00 AE080018 */  sw         $t0, 0x18($s0)
    /* 1EF1B4 151C1D04 8C410008 */  lw         $at, 0x8($v0)
    /* 1EF1B8 151C1D08 AE01001C */  sw         $at, 0x1C($s0)
    /* 1EF1BC 151C1D0C 8C410000 */  lw         $at, 0x0($v0)
    /* 1EF1C0 151C1D10 AE010020 */  sw         $at, 0x20($s0)
    /* 1EF1C4 151C1D14 8C4A0004 */  lw         $t2, 0x4($v0)
    /* 1EF1C8 151C1D18 AE0A0024 */  sw         $t2, 0x24($s0)
    /* 1EF1CC 151C1D1C 8C410008 */  lw         $at, 0x8($v0)
    /* 1EF1D0 151C1D20 A6000056 */  sh         $zero, 0x56($s0)
    /* 1EF1D4 151C1D24 A2000058 */  sb         $zero, 0x58($s0)
    /* 1EF1D8 151C1D28 A2000059 */  sb         $zero, 0x59($s0)
    /* 1EF1DC 151C1D2C A200005A */  sb         $zero, 0x5A($s0)
    /* 1EF1E0 151C1D30 AE00005C */  sw         $zero, 0x5C($s0)
    /* 1EF1E4 151C1D34 AE000060 */  sw         $zero, 0x60($s0)
    /* 1EF1E8 151C1D38 AE010028 */  sw         $at, 0x28($s0)
    /* 1EF1EC 151C1D3C 24020001 */  addiu      $v0, $zero, 0x1
  .L151C1D40:
    /* 1EF1F0 151C1D40 8FBF004C */  lw         $ra, 0x4C($sp)
    /* 1EF1F4 151C1D44 8FB0003C */  lw         $s0, 0x3C($sp)
    /* 1EF1F8 151C1D48 8FB10040 */  lw         $s1, 0x40($sp)
    /* 1EF1FC 151C1D4C 8FB20044 */  lw         $s2, 0x44($sp)
    /* 1EF200 151C1D50 8FB30048 */  lw         $s3, 0x48($sp)
    /* 1EF204 151C1D54 03E00008 */  jr         $ra
    /* 1EF208 151C1D58 27BD0058 */   addiu     $sp, $sp, 0x58
endlabel func_151C196C
