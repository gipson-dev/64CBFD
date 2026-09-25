glabel func_151C1D5C
    /* 1EF20C 151C1D5C 27BDFF58 */  addiu      $sp, $sp, -0xA8
    /* 1EF210 151C1D60 AFB20068 */  sw         $s2, 0x68($sp)
    /* 1EF214 151C1D64 AFB00060 */  sw         $s0, 0x60($sp)
    /* 1EF218 151C1D68 44800000 */  mtc1       $zero, $f0
    /* 1EF21C 151C1D6C 00E08025 */  or         $s0, $a3, $zero
    /* 1EF220 151C1D70 00C09025 */  or         $s2, $a2, $zero
    /* 1EF224 151C1D74 AFBF0084 */  sw         $ra, 0x84($sp)
    /* 1EF228 151C1D78 AFBE0080 */  sw         $fp, 0x80($sp)
    /* 1EF22C 151C1D7C AFB7007C */  sw         $s7, 0x7C($sp)
    /* 1EF230 151C1D80 AFB60078 */  sw         $s6, 0x78($sp)
    /* 1EF234 151C1D84 AFB50074 */  sw         $s5, 0x74($sp)
    /* 1EF238 151C1D88 AFB40070 */  sw         $s4, 0x70($sp)
    /* 1EF23C 151C1D8C AFB3006C */  sw         $s3, 0x6C($sp)
    /* 1EF240 151C1D90 AFB10064 */  sw         $s1, 0x64($sp)
    /* 1EF244 151C1D94 F7B80058 */  sdc1       $f24, 0x58($sp)
    /* 1EF248 151C1D98 F7B60050 */  sdc1       $f22, 0x50($sp)
    /* 1EF24C 151C1D9C F7B40048 */  sdc1       $f20, 0x48($sp)
    /* 1EF250 151C1DA0 AFA500AC */  sw         $a1, 0xAC($sp)
    /* 1EF254 151C1DA4 8FAE00D4 */  lw         $t6, 0xD4($sp)
    /* 1EF258 151C1DA8 27AF0098 */  addiu      $t7, $sp, 0x98
    /* 1EF25C 151C1DAC 46000586 */  mov.s      $f22, $f0
    /* 1EF260 151C1DB0 E5C00000 */  swc1       $f0, 0x0($t6)
    /* 1EF264 151C1DB4 8FB800AC */  lw         $t8, 0xAC($sp)
    /* 1EF268 151C1DB8 8F010000 */  lw         $at, 0x0($t8)
    /* 1EF26C 151C1DBC ADE10000 */  sw         $at, 0x0($t7)
    /* 1EF270 151C1DC0 8F080004 */  lw         $t0, 0x4($t8)
    /* 1EF274 151C1DC4 ADE80004 */  sw         $t0, 0x4($t7)
    /* 1EF278 151C1DC8 8F010008 */  lw         $at, 0x8($t8)
    /* 1EF27C 151C1DCC ADE10008 */  sw         $at, 0x8($t7)
    /* 1EF280 151C1DD0 3C01800B */  lui        $at, %hi(D_800AA9C4)
    /* 1EF284 151C1DD4 C434A9C4 */  lwc1       $f20, %lo(D_800AA9C4)($at)
    /* 1EF288 151C1DD8 8FB100D8 */  lw         $s1, 0xD8($sp)
    /* 1EF28C 151C1DDC 8FB300BC */  lw         $s3, 0xBC($sp)
    /* 1EF290 151C1DE0 8FB400C0 */  lw         $s4, 0xC0($sp)
    /* 1EF294 151C1DE4 8FB500C4 */  lw         $s5, 0xC4($sp)
    /* 1EF298 151C1DE8 83B600CB */  lb         $s6, 0xCB($sp)
    /* 1EF29C 151C1DEC 8FB700CC */  lw         $s7, 0xCC($sp)
    /* 1EF2A0 151C1DF0 8FBE00DC */  lw         $fp, 0xDC($sp)
    /* 1EF2A4 151C1DF4 C7B800B8 */  lwc1       $f24, 0xB8($sp)
    /* 1EF2A8 151C1DF8 AFA400A8 */  sw         $a0, 0xA8($sp)
    /* 1EF2AC 151C1DFC C6440000 */  lwc1       $f4, 0x0($s2)
  .L151C1E00:
    /* 1EF2B0 151C1E00 8FA400A8 */  lw         $a0, 0xA8($sp)
    /* 1EF2B4 151C1E04 8FA50098 */  lw         $a1, 0x98($sp)
    /* 1EF2B8 151C1E08 E7A40010 */  swc1       $f4, 0x10($sp)
    /* 1EF2BC 151C1E0C C6460004 */  lwc1       $f6, 0x4($s2)
    /* 1EF2C0 151C1E10 8FA6009C */  lw         $a2, 0x9C($sp)
    /* 1EF2C4 151C1E14 8FA700A0 */  lw         $a3, 0xA0($sp)
    /* 1EF2C8 151C1E18 E7A60014 */  swc1       $f6, 0x14($sp)
    /* 1EF2CC 151C1E1C C6480008 */  lwc1       $f8, 0x8($s2)
    /* 1EF2D0 151C1E20 AFBE0038 */  sw         $fp, 0x38($sp)
    /* 1EF2D4 151C1E24 AFB70034 */  sw         $s7, 0x34($sp)
    /* 1EF2D8 151C1E28 AFB60030 */  sw         $s6, 0x30($sp)
    /* 1EF2DC 151C1E2C AFB5002C */  sw         $s5, 0x2C($sp)
    /* 1EF2E0 151C1E30 AFB40028 */  sw         $s4, 0x28($sp)
    /* 1EF2E4 151C1E34 AFB30024 */  sw         $s3, 0x24($sp)
    /* 1EF2E8 151C1E38 E7B80020 */  swc1       $f24, 0x20($sp)
    /* 1EF2EC 151C1E3C AFB0001C */  sw         $s0, 0x1C($sp)
    /* 1EF2F0 151C1E40 0D4205A4 */  jal        func_15081690
    /* 1EF2F4 151C1E44 E7A80018 */   swc1      $f8, 0x18($sp)
    /* 1EF2F8 151C1E48 8E02005C */  lw         $v0, 0x5C($s0)
    /* 1EF2FC 151C1E4C C60A0004 */  lwc1       $f10, 0x4($s0)
    /* 1EF300 151C1E50 1040003F */  beqz       $v0, .L151C1F50
    /* 1EF304 151C1E54 460AB580 */   add.s     $f22, $f22, $f10
    /* 1EF308 151C1E58 9049004F */  lbu        $t1, 0x4F($v0)
    /* 1EF30C 151C1E5C 00401825 */  or         $v1, $v0, $zero
    /* 1EF310 151C1E60 24010040 */  addiu      $at, $zero, 0x40
    /* 1EF314 151C1E64 312A0060 */  andi       $t2, $t1, 0x60
    /* 1EF318 151C1E68 15410037 */  bne        $t2, $at, .L151C1F48
    /* 1EF31C 151C1E6C 00001025 */   or        $v0, $zero, $zero
    /* 1EF320 151C1E70 C6120038 */  lwc1       $f18, 0x38($s0)
    /* 1EF324 151C1E74 C6100008 */  lwc1       $f16, 0x8($s0)
    /* 1EF328 151C1E78 8FAB00D0 */  lw         $t3, 0xD0($sp)
    /* 1EF32C 151C1E7C 46149102 */  mul.s      $f4, $f18, $f20
    /* 1EF330 151C1E80 24090007 */  addiu      $t1, $zero, 0x7
    /* 1EF334 151C1E84 240A0003 */  addiu      $t2, $zero, 0x3
    /* 1EF338 151C1E88 24020001 */  addiu      $v0, $zero, 0x1
    /* 1EF33C 151C1E8C 46048180 */  add.s      $f6, $f16, $f4
    /* 1EF340 151C1E90 E7A60098 */  swc1       $f6, 0x98($sp)
    /* 1EF344 151C1E94 C60A003C */  lwc1       $f10, 0x3C($s0)
    /* 1EF348 151C1E98 C608000C */  lwc1       $f8, 0xC($s0)
    /* 1EF34C 151C1E9C 46145482 */  mul.s      $f18, $f10, $f20
    /* 1EF350 151C1EA0 46124400 */  add.s      $f16, $f8, $f18
    /* 1EF354 151C1EA4 E7B0009C */  swc1       $f16, 0x9C($sp)
    /* 1EF358 151C1EA8 C6060040 */  lwc1       $f6, 0x40($s0)
    /* 1EF35C 151C1EAC C6040010 */  lwc1       $f4, 0x10($s0)
    /* 1EF360 151C1EB0 46143282 */  mul.s      $f10, $f6, $f20
    /* 1EF364 151C1EB4 460A2200 */  add.s      $f8, $f4, $f10
    /* 1EF368 151C1EB8 E7A800A0 */  swc1       $f8, 0xA0($sp)
    /* 1EF36C 151C1EBC 8E010008 */  lw         $at, 0x8($s0)
    /* 1EF370 151C1EC0 AD610000 */  sw         $at, 0x0($t3)
    /* 1EF374 151C1EC4 8E0E000C */  lw         $t6, 0xC($s0)
    /* 1EF378 151C1EC8 AD6E0004 */  sw         $t6, 0x4($t3)
    /* 1EF37C 151C1ECC 8E010010 */  lw         $at, 0x10($s0)
    /* 1EF380 151C1ED0 AD610008 */  sw         $at, 0x8($t3)
    /* 1EF384 151C1ED4 8FB900D4 */  lw         $t9, 0xD4($sp)
    /* 1EF388 151C1ED8 E7360000 */  swc1       $f22, 0x0($t9)
    /* 1EF38C 151C1EDC C612000C */  lwc1       $f18, 0xC($s0)
    /* 1EF390 151C1EE0 4614B580 */  add.s      $f22, $f22, $f20
    /* 1EF394 151C1EE4 E6320000 */  swc1       $f18, 0x0($s1)
    /* 1EF398 151C1EE8 8A010044 */  lwl        $at, 0x44($s0)
    /* 1EF39C 151C1EEC 9A010047 */  lwr        $at, 0x47($s0)
    /* 1EF3A0 151C1EF0 AA210004 */  swl        $at, 0x4($s1)
    /* 1EF3A4 151C1EF4 BA210007 */  swr        $at, 0x7($s1)
    /* 1EF3A8 151C1EF8 8A180048 */  lwl        $t8, 0x48($s0)
    /* 1EF3AC 151C1EFC 9A18004B */  lwr        $t8, 0x4B($s0)
    /* 1EF3B0 151C1F00 AA380008 */  swl        $t8, 0x8($s1)
    /* 1EF3B4 151C1F04 BA38000B */  swr        $t8, 0xB($s1)
    /* 1EF3B8 151C1F08 8A01004C */  lwl        $at, 0x4C($s0)
    /* 1EF3BC 151C1F0C 9A01004F */  lwr        $at, 0x4F($s0)
    /* 1EF3C0 151C1F10 AA21000C */  swl        $at, 0xC($s1)
    /* 1EF3C4 151C1F14 BA21000F */  swr        $at, 0xF($s1)
    /* 1EF3C8 151C1F18 8A180050 */  lwl        $t8, 0x50($s0)
    /* 1EF3CC 151C1F1C 9A180053 */  lwr        $t8, 0x53($s0)
    /* 1EF3D0 151C1F20 AA380010 */  swl        $t8, 0x10($s1)
    /* 1EF3D4 151C1F24 BA380013 */  swr        $t8, 0x13($s1)
    /* 1EF3D8 151C1F28 96010054 */  lhu        $at, 0x54($s0)
    /* 1EF3DC 151C1F2C A6210014 */  sh         $at, 0x14($s1)
    /* 1EF3E0 151C1F30 8E080060 */  lw         $t0, 0x60($s0)
    /* 1EF3E4 151C1F34 A229001C */  sb         $t1, 0x1C($s1)
    /* 1EF3E8 151C1F38 A22A001D */  sb         $t2, 0x1D($s1)
    /* 1EF3EC 151C1F3C AE230020 */  sw         $v1, 0x20($s1)
    /* 1EF3F0 151C1F40 10000004 */  b          .L151C1F54
    /* 1EF3F4 151C1F44 AE280018 */   sw        $t0, 0x18($s1)
  .L151C1F48:
    /* 1EF3F8 151C1F48 10000002 */  b          .L151C1F54
    /* 1EF3FC 151C1F4C 00000000 */   nop
  .L151C1F50:
    /* 1EF400 151C1F50 00001025 */  or         $v0, $zero, $zero
  .L151C1F54:
    /* 1EF404 151C1F54 5440FFAA */  bnel       $v0, $zero, .L151C1E00
    /* 1EF408 151C1F58 C6440000 */   lwc1      $f4, 0x0($s2)
    /* 1EF40C 151C1F5C 8FAD00AC */  lw         $t5, 0xAC($sp)
    /* 1EF410 151C1F60 8DA10000 */  lw         $at, 0x0($t5)
    /* 1EF414 151C1F64 AE01002C */  sw         $at, 0x2C($s0)
    /* 1EF418 151C1F68 8DAB0004 */  lw         $t3, 0x4($t5)
    /* 1EF41C 151C1F6C AE0B0030 */  sw         $t3, 0x30($s0)
    /* 1EF420 151C1F70 8DA10008 */  lw         $at, 0x8($t5)
    /* 1EF424 151C1F74 E6160004 */  swc1       $f22, 0x4($s0)
    /* 1EF428 151C1F78 AE010034 */  sw         $at, 0x34($s0)
    /* 1EF42C 151C1F7C 8FBF0084 */  lw         $ra, 0x84($sp)
    /* 1EF430 151C1F80 D7B40048 */  ldc1       $f20, 0x48($sp)
    /* 1EF434 151C1F84 D7B60050 */  ldc1       $f22, 0x50($sp)
    /* 1EF438 151C1F88 D7B80058 */  ldc1       $f24, 0x58($sp)
    /* 1EF43C 151C1F8C 8FB00060 */  lw         $s0, 0x60($sp)
    /* 1EF440 151C1F90 8FB10064 */  lw         $s1, 0x64($sp)
    /* 1EF444 151C1F94 8FB20068 */  lw         $s2, 0x68($sp)
    /* 1EF448 151C1F98 8FB3006C */  lw         $s3, 0x6C($sp)
    /* 1EF44C 151C1F9C 8FB40070 */  lw         $s4, 0x70($sp)
    /* 1EF450 151C1FA0 8FB50074 */  lw         $s5, 0x74($sp)
    /* 1EF454 151C1FA4 8FB60078 */  lw         $s6, 0x78($sp)
    /* 1EF458 151C1FA8 8FB7007C */  lw         $s7, 0x7C($sp)
    /* 1EF45C 151C1FAC 8FBE0080 */  lw         $fp, 0x80($sp)
    /* 1EF460 151C1FB0 03E00008 */  jr         $ra
    /* 1EF464 151C1FB4 27BD00A8 */   addiu     $sp, $sp, 0xA8
endlabel func_151C1D5C
