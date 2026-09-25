glabel func_151D57F8
    /* 202CA8 151D57F8 27BDFF48 */  addiu      $sp, $sp, -0xB8
    /* 202CAC 151D57FC AFB00048 */  sw         $s0, 0x48($sp)
    /* 202CB0 151D5800 00808025 */  or         $s0, $a0, $zero
    /* 202CB4 151D5804 AFBF004C */  sw         $ra, 0x4C($sp)
    /* 202CB8 151D5808 AFA500BC */  sw         $a1, 0xBC($sp)
    /* 202CBC 151D580C 93A200BF */  lbu        $v0, 0xBF($sp)
    /* 202CC0 151D5810 3C188009 */  lui        $t8, %hi(D_8008FC8C)
    /* 202CC4 151D5814 3C198009 */  lui        $t9, %hi(D_8008FC94)
    /* 202CC8 151D5818 00027880 */  sll        $t7, $v0, 2
    /* 202CCC 151D581C 030FC021 */  addu       $t8, $t8, $t7
    /* 202CD0 151D5820 8F18FC8C */  lw         $t8, %lo(D_8008FC8C)($t8)
    /* 202CD4 151D5824 032FC821 */  addu       $t9, $t9, $t7
    /* 202CD8 151D5828 8F39FC94 */  lw         $t9, %lo(D_8008FC94)($t9)
    /* 202CDC 151D582C 27AE0088 */  addiu      $t6, $sp, 0x88
    /* 202CE0 151D5830 AFAE0010 */  sw         $t6, 0x10($sp)
    /* 202CE4 151D5834 AFB80014 */  sw         $t8, 0x14($sp)
    /* 202CE8 151D5838 93280000 */  lbu        $t0, 0x0($t9)
    /* 202CEC 151D583C 01E01025 */  or         $v0, $t7, $zero
    /* 202CF0 151D5840 02002025 */  or         $a0, $s0, $zero
    /* 202CF4 151D5844 27A500AC */  addiu      $a1, $sp, 0xAC
    /* 202CF8 151D5848 27A600A0 */  addiu      $a2, $sp, 0xA0
    /* 202CFC 151D584C 27A70094 */  addiu      $a3, $sp, 0x94
    /* 202D00 151D5850 0D475686 */  jal        func_151D5A18
    /* 202D04 151D5854 AFA80018 */   sw        $t0, 0x18($sp)
    /* 202D08 151D5858 27A90088 */  addiu      $t1, $sp, 0x88
    /* 202D0C 151D585C 27AA007C */  addiu      $t2, $sp, 0x7C
    /* 202D10 151D5860 27AB0070 */  addiu      $t3, $sp, 0x70
    /* 202D14 151D5864 27AC006C */  addiu      $t4, $sp, 0x6C
    /* 202D18 151D5868 27AD0068 */  addiu      $t5, $sp, 0x68
    /* 202D1C 151D586C AFAD0020 */  sw         $t5, 0x20($sp)
    /* 202D20 151D5870 AFAC001C */  sw         $t4, 0x1C($sp)
    /* 202D24 151D5874 AFAB0018 */  sw         $t3, 0x18($sp)
    /* 202D28 151D5878 AFAA0014 */  sw         $t2, 0x14($sp)
    /* 202D2C 151D587C AFA90010 */  sw         $t1, 0x10($sp)
    /* 202D30 151D5880 02002025 */  or         $a0, $s0, $zero
    /* 202D34 151D5884 27A500AC */  addiu      $a1, $sp, 0xAC
    /* 202D38 151D5888 27A600A0 */  addiu      $a2, $sp, 0xA0
    /* 202D3C 151D588C 27A70094 */  addiu      $a3, $sp, 0x94
    /* 202D40 151D5890 0D47545D */  jal        func_151D5174
    /* 202D44 151D5894 AFA00024 */   sw        $zero, 0x24($sp)
    /* 202D48 151D5898 8E0F031C */  lw         $t7, 0x31C($s0)
    /* 202D4C 151D589C 240E0001 */  addiu      $t6, $zero, 0x1
    /* 202D50 151D58A0 27B900AC */  addiu      $t9, $sp, 0xAC
    /* 202D54 151D58A4 A1EE0109 */  sb         $t6, 0x109($t7)
    /* 202D58 151D58A8 8FB8006C */  lw         $t8, 0x6C($sp)
    /* 202D5C 151D58AC 27A900A0 */  addiu      $t1, $sp, 0xA0
    /* 202D60 151D58B0 27A4005C */  addiu      $a0, $sp, 0x5C
    /* 202D64 151D58B4 57000003 */  bnel       $t8, $zero, .L151D58C4
    /* 202D68 151D58B8 8FA80068 */   lw        $t0, 0x68($sp)
    /* 202D6C 151D58BC AFB9006C */  sw         $t9, 0x6C($sp)
    /* 202D70 151D58C0 8FA80068 */  lw         $t0, 0x68($sp)
  .L151D58C4:
    /* 202D74 151D58C4 55000003 */  bnel       $t0, $zero, .L151D58D4
    /* 202D78 151D58C8 8FAB0068 */   lw        $t3, 0x68($sp)
    /* 202D7C 151D58CC AFA90068 */  sw         $t1, 0x68($sp)
    /* 202D80 151D58D0 8FAB0068 */  lw         $t3, 0x68($sp)
  .L151D58D4:
    /* 202D84 151D58D4 3C01800B */  lui        $at, %hi(D_800AB238)
    /* 202D88 151D58D8 C420B238 */  lwc1       $f0, %lo(D_800AB238)($at)
    /* 202D8C 151D58DC C5660000 */  lwc1       $f6, 0x0($t3)
    /* 202D90 151D58E0 8FAA006C */  lw         $t2, 0x6C($sp)
    /* 202D94 151D58E4 8E0C031C */  lw         $t4, 0x31C($s0)
    /* 202D98 151D58E8 46003202 */  mul.s      $f8, $f6, $f0
    /* 202D9C 151D58EC C5440000 */  lwc1       $f4, 0x0($t2)
    /* 202DA0 151D58F0 46082280 */  add.s      $f10, $f4, $f8
    /* 202DA4 151D58F4 E58A00B8 */  swc1       $f10, 0xB8($t4)
    /* 202DA8 151D58F8 8FAE0068 */  lw         $t6, 0x68($sp)
    /* 202DAC 151D58FC 8FAD006C */  lw         $t5, 0x6C($sp)
    /* 202DB0 151D5900 8E0F031C */  lw         $t7, 0x31C($s0)
    /* 202DB4 151D5904 C5D20004 */  lwc1       $f18, 0x4($t6)
    /* 202DB8 151D5908 C5B00004 */  lwc1       $f16, 0x4($t5)
    /* 202DBC 151D590C 46009182 */  mul.s      $f6, $f18, $f0
    /* 202DC0 151D5910 46068100 */  add.s      $f4, $f16, $f6
    /* 202DC4 151D5914 E5E400BC */  swc1       $f4, 0xBC($t7)
    /* 202DC8 151D5918 8FB90068 */  lw         $t9, 0x68($sp)
    /* 202DCC 151D591C 8FB8006C */  lw         $t8, 0x6C($sp)
    /* 202DD0 151D5920 8E08031C */  lw         $t0, 0x31C($s0)
    /* 202DD4 151D5924 C72A0008 */  lwc1       $f10, 0x8($t9)
    /* 202DD8 151D5928 C7080008 */  lwc1       $f8, 0x8($t8)
    /* 202DDC 151D592C 46005482 */  mul.s      $f18, $f10, $f0
    /* 202DE0 151D5930 46124400 */  add.s      $f16, $f8, $f18
    /* 202DE4 151D5934 E51000C0 */  swc1       $f16, 0xC0($t0)
    /* 202DE8 151D5938 8E02031C */  lw         $v0, 0x31C($s0)
    /* 202DEC 151D593C C7A400AC */  lwc1       $f4, 0xAC($sp)
    /* 202DF0 151D5940 90490109 */  lbu        $t1, 0x109($v0)
    /* 202DF4 151D5944 1120002D */  beqz       $t1, .L151D59FC
    /* 202DF8 151D5948 00000000 */   nop
    /* 202DFC 151D594C C44600B8 */  lwc1       $f6, 0xB8($v0)
    /* 202E00 151D5950 C7B200B0 */  lwc1       $f18, 0xB0($sp)
    /* 202E04 151D5954 00802825 */  or         $a1, $a0, $zero
    /* 202E08 151D5958 46043281 */  sub.s      $f10, $f6, $f4
    /* 202E0C 151D595C C7A400B4 */  lwc1       $f4, 0xB4($sp)
    /* 202E10 151D5960 27A60058 */  addiu      $a2, $sp, 0x58
    /* 202E14 151D5964 00003825 */  or         $a3, $zero, $zero
    /* 202E18 151D5968 E7AA005C */  swc1       $f10, 0x5C($sp)
    /* 202E1C 151D596C 8E0A031C */  lw         $t2, 0x31C($s0)
    /* 202E20 151D5970 C54800BC */  lwc1       $f8, 0xBC($t2)
    /* 202E24 151D5974 46124401 */  sub.s      $f16, $f8, $f18
    /* 202E28 151D5978 E7B00060 */  swc1       $f16, 0x60($sp)
    /* 202E2C 151D597C 8E0B031C */  lw         $t3, 0x31C($s0)
    /* 202E30 151D5980 C56600C0 */  lwc1       $f6, 0xC0($t3)
    /* 202E34 151D5984 46043281 */  sub.s      $f10, $f6, $f4
    /* 202E38 151D5988 0D45144A */  jal        func_15145128
    /* 202E3C 151D598C E7AA0064 */   swc1      $f10, 0x64($sp)
    /* 202E40 151D5990 1040001A */  beqz       $v0, .L151D59FC
    /* 202E44 151D5994 02002025 */   or        $a0, $s0, $zero
    /* 202E48 151D5998 C7A8005C */  lwc1       $f8, 0x5C($sp)
    /* 202E4C 151D599C C7B20060 */  lwc1       $f18, 0x60($sp)
    /* 202E50 151D59A0 C7B00064 */  lwc1       $f16, 0x64($sp)
    /* 202E54 151D59A4 3C01800B */  lui        $at, %hi(D_800AB23C)
    /* 202E58 151D59A8 C424B23C */  lwc1       $f4, %lo(D_800AB23C)($at)
    /* 202E5C 151D59AC C7A60058 */  lwc1       $f6, 0x58($sp)
    /* 202E60 151D59B0 E7A80010 */  swc1       $f8, 0x10($sp)
    /* 202E64 151D59B4 E7B20014 */  swc1       $f18, 0x14($sp)
    /* 202E68 151D59B8 E7B00018 */  swc1       $f16, 0x18($sp)
    /* 202E6C 151D59BC 8E0C031C */  lw         $t4, 0x31C($s0)
    /* 202E70 151D59C0 46043282 */  mul.s      $f10, $f6, $f4
    /* 202E74 151D59C4 240EFFFF */  addiu      $t6, $zero, -0x1
    /* 202E78 151D59C8 258D00B0 */  addiu      $t5, $t4, 0xB0
    /* 202E7C 151D59CC AFAD001C */  sw         $t5, 0x1C($sp)
    /* 202E80 151D59D0 AFAE0030 */  sw         $t6, 0x30($sp)
    /* 202E84 151D59D4 AFA00038 */  sw         $zero, 0x38($sp)
    /* 202E88 151D59D8 AFA00034 */  sw         $zero, 0x34($sp)
    /* 202E8C 151D59DC E7AA0020 */  swc1       $f10, 0x20($sp)
    /* 202E90 151D59E0 AFA0002C */  sw         $zero, 0x2C($sp)
    /* 202E94 151D59E4 AFA00028 */  sw         $zero, 0x28($sp)
    /* 202E98 151D59E8 AFA00024 */  sw         $zero, 0x24($sp)
    /* 202E9C 151D59EC 8FA500AC */  lw         $a1, 0xAC($sp)
    /* 202EA0 151D59F0 8FA600B0 */  lw         $a2, 0xB0($sp)
    /* 202EA4 151D59F4 0D4205A4 */  jal        func_15081690
    /* 202EA8 151D59F8 8FA700B4 */   lw        $a3, 0xB4($sp)
  .L151D59FC:
    /* 202EAC 151D59FC 0D418DA9 */  jal        func_150636A4
    /* 202EB0 151D5A00 02002025 */   or        $a0, $s0, $zero
    /* 202EB4 151D5A04 8FBF004C */  lw         $ra, 0x4C($sp)
    /* 202EB8 151D5A08 8FB00048 */  lw         $s0, 0x48($sp)
    /* 202EBC 151D5A0C 27BD00B8 */  addiu      $sp, $sp, 0xB8
    /* 202EC0 151D5A10 03E00008 */  jr         $ra
    /* 202EC4 151D5A14 00000000 */   nop
endlabel func_151D57F8
