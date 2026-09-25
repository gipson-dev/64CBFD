glabel func_151B8908
    /* 1E5DB8 151B8908 27BDFF50 */  addiu      $sp, $sp, -0xB0
    /* 1E5DBC 151B890C AFBF001C */  sw         $ra, 0x1C($sp)
    /* 1E5DC0 151B8910 AFA400B0 */  sw         $a0, 0xB0($sp)
    /* 1E5DC4 151B8914 3C0F800B */  lui        $t7, %hi(D_800AA4B8)
    /* 1E5DC8 151B8918 25EFA4B8 */  addiu      $t7, $t7, %lo(D_800AA4B8)
    /* 1E5DCC 151B891C 8DE10000 */  lw         $at, 0x0($t7)
    /* 1E5DD0 151B8920 8DE80004 */  lw         $t0, 0x4($t7)
    /* 1E5DD4 151B8924 27AE002C */  addiu      $t6, $sp, 0x2C
    /* 1E5DD8 151B8928 ADC10000 */  sw         $at, 0x0($t6)
    /* 1E5DDC 151B892C ADC80004 */  sw         $t0, 0x4($t6)
    /* 1E5DE0 151B8930 8DE8000C */  lw         $t0, 0xC($t7)
    /* 1E5DE4 151B8934 8DE10008 */  lw         $at, 0x8($t7)
    /* 1E5DE8 151B8938 ADC8000C */  sw         $t0, 0xC($t6)
    /* 1E5DEC 151B893C 0D42B688 */  jal        func_150ADA20
    /* 1E5DF0 151B8940 ADC10008 */   sw        $at, 0x8($t6)
    /* 1E5DF4 151B8944 30490003 */  andi       $t1, $v0, 0x3
    /* 1E5DF8 151B8948 00095080 */  sll        $t2, $t1, 2
    /* 1E5DFC 151B894C 03AA5821 */  addu       $t3, $sp, $t2
    /* 1E5E00 151B8950 8D6B002C */  lw         $t3, 0x2C($t3)
    /* 1E5E04 151B8954 3C0D0020 */  lui        $t5, (0x200005 >> 16)
    /* 1E5E08 151B8958 240C1303 */  addiu      $t4, $zero, 0x1303
    /* 1E5E0C 151B895C 35AD0005 */  ori        $t5, $t5, (0x200005 & 0xFFFF)
    /* 1E5E10 151B8960 A7AC0044 */  sh         $t4, 0x44($sp)
    /* 1E5E14 151B8964 AFAD003C */  sw         $t5, 0x3C($sp)
    /* 1E5E18 151B8968 A3AB0059 */  sb         $t3, 0x59($sp)
    /* 1E5E1C 151B896C 2419012C */  addiu      $t9, $zero, 0x12C
    /* 1E5E20 151B8970 241800FF */  addiu      $t8, $zero, 0xFF
    /* 1E5E24 151B8974 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 1E5E28 151B8978 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 1E5E2C 151B897C 240800FF */  addiu      $t0, $zero, 0xFF
    /* 1E5E30 151B8980 240900FF */  addiu      $t1, $zero, 0xFF
    /* 1E5E34 151B8984 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 1E5E38 151B8988 240B00FF */  addiu      $t3, $zero, 0xFF
    /* 1E5E3C 151B898C 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 1E5E40 151B8990 240D00FF */  addiu      $t5, $zero, 0xFF
    /* 1E5E44 151B8994 AFA00040 */  sw         $zero, 0x40($sp)
    /* 1E5E48 151B8998 A7B90046 */  sh         $t9, 0x46($sp)
    /* 1E5E4C 151B899C AFA00048 */  sw         $zero, 0x48($sp)
    /* 1E5E50 151B89A0 AFA0004C */  sw         $zero, 0x4C($sp)
    /* 1E5E54 151B89A4 A3B80050 */  sb         $t8, 0x50($sp)
    /* 1E5E58 151B89A8 A3AE0051 */  sb         $t6, 0x51($sp)
    /* 1E5E5C 151B89AC A3AF0052 */  sb         $t7, 0x52($sp)
    /* 1E5E60 151B89B0 A3A80053 */  sb         $t0, 0x53($sp)
    /* 1E5E64 151B89B4 A3A90054 */  sb         $t1, 0x54($sp)
    /* 1E5E68 151B89B8 A3AA0055 */  sb         $t2, 0x55($sp)
    /* 1E5E6C 151B89BC A3AB0056 */  sb         $t3, 0x56($sp)
    /* 1E5E70 151B89C0 A3AC0057 */  sb         $t4, 0x57($sp)
    /* 1E5E74 151B89C4 0D42B69A */  jal        func_150ADA68
    /* 1E5E78 151B89C8 A3AD0058 */   sb        $t5, 0x58($sp)
    /* 1E5E7C 151B89CC 3C0143FA */  lui        $at, (0x43FA0000 >> 16)
    /* 1E5E80 151B89D0 44812000 */  mtc1       $at, $f4
    /* 1E5E84 151B89D4 3C014461 */  lui        $at, (0x44610000 >> 16)
    /* 1E5E88 151B89D8 44814000 */  mtc1       $at, $f8
    /* 1E5E8C 151B89DC 46040182 */  mul.s      $f6, $f0, $f4
    /* 1E5E90 151B89E0 8FB800B0 */  lw         $t8, 0xB0($sp)
    /* 1E5E94 151B89E4 27B9006C */  addiu      $t9, $sp, 0x6C
    /* 1E5E98 151B89E8 3C02800A */  lui        $v0, %hi(D_800A5480)
    /* 1E5E9C 151B89EC 24425480 */  addiu      $v0, $v0, %lo(D_800A5480)
    /* 1E5EA0 151B89F0 27A90078 */  addiu      $t1, $sp, 0x78
    /* 1E5EA4 151B89F4 27AD0084 */  addiu      $t5, $sp, 0x84
    /* 1E5EA8 151B89F8 46083280 */  add.s      $f10, $f6, $f8
    /* 1E5EAC 151B89FC 44808000 */  mtc1       $zero, $f16
    /* 1E5EB0 151B8A00 240B0001 */  addiu      $t3, $zero, 0x1
    /* 1E5EB4 151B8A04 E7AA0068 */  swc1       $f10, 0x68($sp)
    /* 1E5EB8 151B8A08 E7AA0064 */  swc1       $f10, 0x64($sp)
    /* 1E5EBC 151B8A0C 8F010038 */  lw         $at, 0x38($t8)
    /* 1E5EC0 151B8A10 AF210000 */  sw         $at, 0x0($t9)
    /* 1E5EC4 151B8A14 8F08003C */  lw         $t0, 0x3C($t8)
    /* 1E5EC8 151B8A18 AF280004 */  sw         $t0, 0x4($t9)
    /* 1E5ECC 151B8A1C 8F010040 */  lw         $at, 0x40($t8)
    /* 1E5ED0 151B8A20 24180001 */  addiu      $t8, $zero, 0x1
    /* 1E5ED4 151B8A24 240800FF */  addiu      $t0, $zero, 0xFF
    /* 1E5ED8 151B8A28 AF210008 */  sw         $at, 0x8($t9)
    /* 1E5EDC 151B8A2C 8C410000 */  lw         $at, 0x0($v0)
    /* 1E5EE0 151B8A30 AD210000 */  sw         $at, 0x0($t1)
    /* 1E5EE4 151B8A34 8C4C0004 */  lw         $t4, 0x4($v0)
    /* 1E5EE8 151B8A38 AD2C0004 */  sw         $t4, 0x4($t1)
    /* 1E5EEC 151B8A3C 8C410008 */  lw         $at, 0x8($v0)
    /* 1E5EF0 151B8A40 AD210008 */  sw         $at, 0x8($t1)
    /* 1E5EF4 151B8A44 8C410000 */  lw         $at, 0x0($v0)
    /* 1E5EF8 151B8A48 ADA10000 */  sw         $at, 0x0($t5)
    /* 1E5EFC 151B8A4C 8C590004 */  lw         $t9, 0x4($v0)
    /* 1E5F00 151B8A50 ADB90004 */  sw         $t9, 0x4($t5)
    /* 1E5F04 151B8A54 8C410008 */  lw         $at, 0x8($v0)
    /* 1E5F08 151B8A58 ADA10008 */  sw         $at, 0x8($t5)
    /* 1E5F0C 151B8A5C 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 1E5F10 151B8A60 44819000 */  mtc1       $at, $f18
    /* 1E5F14 151B8A64 A7B8005A */  sh         $t8, 0x5A($sp)
    /* 1E5F18 151B8A68 A7A8005C */  sh         $t0, 0x5C($sp)
    /* 1E5F1C 151B8A6C A7AB005E */  sh         $t3, 0x5E($sp)
    /* 1E5F20 151B8A70 E7B00090 */  swc1       $f16, 0x90($sp)
    /* 1E5F24 151B8A74 0D42B688 */  jal        func_150ADA20
    /* 1E5F28 151B8A78 E7B20060 */   swc1      $f18, 0x60($sp)
    /* 1E5F2C 151B8A7C 304A0001 */  andi       $t2, $v0, 0x1
    /* 1E5F30 151B8A80 11400003 */  beqz       $t2, .L151B8A90
    /* 1E5F34 151B8A84 00001825 */   or        $v1, $zero, $zero
    /* 1E5F38 151B8A88 10000001 */  b          .L151B8A90
    /* 1E5F3C 151B8A8C 24030040 */   addiu     $v1, $zero, 0x40
  .L151B8A90:
    /* 1E5F40 151B8A90 0D42B688 */  jal        func_150ADA20
    /* 1E5F44 151B8A94 AFA30024 */   sw        $v1, 0x24($sp)
    /* 1E5F48 151B8A98 30490001 */  andi       $t1, $v0, 0x1
    /* 1E5F4C 151B8A9C 11200003 */  beqz       $t1, .L151B8AAC
    /* 1E5F50 151B8AA0 8FA30024 */   lw        $v1, 0x24($sp)
    /* 1E5F54 151B8AA4 10000002 */  b          .L151B8AB0
    /* 1E5F58 151B8AA8 24020080 */   addiu     $v0, $zero, 0x80
  .L151B8AAC:
    /* 1E5F5C 151B8AAC 00001025 */  or         $v0, $zero, $zero
  .L151B8AB0:
    /* 1E5F60 151B8AB0 00437025 */  or         $t6, $v0, $v1
    /* 1E5F64 151B8AB4 35CFC000 */  ori        $t7, $t6, 0xC000
    /* 1E5F68 151B8AB8 3C010004 */  lui        $at, (0x40000 >> 16)
    /* 1E5F6C 151B8ABC 01E16825 */  or         $t5, $t7, $at
    /* 1E5F70 151B8AC0 8FAE00B0 */  lw         $t6, 0xB0($sp)
    /* 1E5F74 151B8AC4 3C010080 */  lui        $at, (0x800000 >> 16)
    /* 1E5F78 151B8AC8 01A1C825 */  or         $t9, $t5, $at
    /* 1E5F7C 151B8ACC 24180006 */  addiu      $t8, $zero, 0x6
    /* 1E5F80 151B8AD0 24080005 */  addiu      $t0, $zero, 0x5
    /* 1E5F84 151B8AD4 240BFFFF */  addiu      $t3, $zero, -0x1
    /* 1E5F88 151B8AD8 240AFFFF */  addiu      $t2, $zero, -0x1
    /* 1E5F8C 151B8ADC 2409FFFF */  addiu      $t1, $zero, -0x1
    /* 1E5F90 151B8AE0 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 1E5F94 151B8AE4 AFB90094 */  sw         $t9, 0x94($sp)
    /* 1E5F98 151B8AE8 A3B8009C */  sb         $t8, 0x9C($sp)
    /* 1E5F9C 151B8AEC A3A8009D */  sb         $t0, 0x9D($sp)
    /* 1E5FA0 151B8AF0 A3AB009E */  sb         $t3, 0x9E($sp)
    /* 1E5FA4 151B8AF4 A3AA009F */  sb         $t2, 0x9F($sp)
    /* 1E5FA8 151B8AF8 A3A900A0 */  sb         $t1, 0xA0($sp)
    /* 1E5FAC 151B8AFC A3A000A1 */  sb         $zero, 0xA1($sp)
    /* 1E5FB0 151B8B00 AFA00098 */  sw         $zero, 0x98($sp)
    /* 1E5FB4 151B8B04 A3AC00A2 */  sb         $t4, 0xA2($sp)
    /* 1E5FB8 151B8B08 91CF000C */  lbu        $t7, 0xC($t6)
    /* 1E5FBC 151B8B0C 27A4003C */  addiu      $a0, $sp, 0x3C
    /* 1E5FC0 151B8B10 24050001 */  addiu      $a1, $zero, 0x1
    /* 1E5FC4 151B8B14 AFAF0010 */  sw         $t7, 0x10($sp)
    /* 1E5FC8 151B8B18 91CD0001 */  lbu        $t5, 0x1($t6)
    /* 1E5FCC 151B8B1C 00003025 */  or         $a2, $zero, $zero
    /* 1E5FD0 151B8B20 00003825 */  or         $a3, $zero, $zero
    /* 1E5FD4 151B8B24 0D44C0A0 */  jal        func_15130280
    /* 1E5FD8 151B8B28 AFAD0014 */   sw        $t5, 0x14($sp)
    /* 1E5FDC 151B8B2C 8FBF001C */  lw         $ra, 0x1C($sp)
    /* 1E5FE0 151B8B30 27BD00B0 */  addiu      $sp, $sp, 0xB0
    /* 1E5FE4 151B8B34 03E00008 */  jr         $ra
    /* 1E5FE8 151B8B38 00000000 */   nop
endlabel func_151B8908
    /* 1E5FEC 151B8B3C 00000000 */  nop
