glabel func_151A2AD4
    /* 1CFF84 151A2AD4 27BDFFA0 */  addiu      $sp, $sp, -0x60
    /* 1CFF88 151A2AD8 44866000 */  mtc1       $a2, $f12
    /* 1CFF8C 151A2ADC 44877000 */  mtc1       $a3, $f14
    /* 1CFF90 151A2AE0 AFBF005C */  sw         $ra, 0x5C($sp)
    /* 1CFF94 151A2AE4 44802000 */  mtc1       $zero, $f4
    /* 1CFF98 151A2AE8 8FAE0070 */  lw         $t6, 0x70($sp)
    /* 1CFF9C 151A2AEC C7A60074 */  lwc1       $f6, 0x74($sp)
    /* 1CFFA0 151A2AF0 C7A80078 */  lwc1       $f8, 0x78($sp)
    /* 1CFFA4 151A2AF4 C7AA007C */  lwc1       $f10, 0x7C($sp)
    /* 1CFFA8 151A2AF8 C7B00080 */  lwc1       $f16, 0x80($sp)
    /* 1CFFAC 151A2AFC 87AF0086 */  lh         $t7, 0x86($sp)
    /* 1CFFB0 151A2B00 87B8008A */  lh         $t8, 0x8A($sp)
    /* 1CFFB4 151A2B04 87B9008E */  lh         $t9, 0x8E($sp)
    /* 1CFFB8 151A2B08 87A80092 */  lh         $t0, 0x92($sp)
    /* 1CFFBC 151A2B0C 87A90096 */  lh         $t1, 0x96($sp)
    /* 1CFFC0 151A2B10 87AA009A */  lh         $t2, 0x9A($sp)
    /* 1CFFC4 151A2B14 83AB009F */  lb         $t3, 0x9F($sp)
    /* 1CFFC8 151A2B18 93AC00A3 */  lbu        $t4, 0xA3($sp)
    /* 1CFFCC 151A2B1C 8FAD00A4 */  lw         $t5, 0xA4($sp)
    /* 1CFFD0 151A2B20 00003025 */  or         $a2, $zero, $zero
    /* 1CFFD4 151A2B24 00003825 */  or         $a3, $zero, $zero
    /* 1CFFD8 151A2B28 E7AC0014 */  swc1       $f12, 0x14($sp)
    /* 1CFFDC 151A2B2C E7AE0018 */  swc1       $f14, 0x18($sp)
    /* 1CFFE0 151A2B30 AFA00054 */  sw         $zero, 0x54($sp)
    /* 1CFFE4 151A2B34 AFAE001C */  sw         $t6, 0x1C($sp)
    /* 1CFFE8 151A2B38 E7A40010 */  swc1       $f4, 0x10($sp)
    /* 1CFFEC 151A2B3C E7A60020 */  swc1       $f6, 0x20($sp)
    /* 1CFFF0 151A2B40 E7A80024 */  swc1       $f8, 0x24($sp)
    /* 1CFFF4 151A2B44 E7AA0028 */  swc1       $f10, 0x28($sp)
    /* 1CFFF8 151A2B48 E7B0002C */  swc1       $f16, 0x2C($sp)
    /* 1CFFFC 151A2B4C AFAF0030 */  sw         $t7, 0x30($sp)
    /* 1D0000 151A2B50 AFB80034 */  sw         $t8, 0x34($sp)
    /* 1D0004 151A2B54 AFB90038 */  sw         $t9, 0x38($sp)
    /* 1D0008 151A2B58 AFA8003C */  sw         $t0, 0x3C($sp)
    /* 1D000C 151A2B5C AFA90040 */  sw         $t1, 0x40($sp)
    /* 1D0010 151A2B60 AFAA0044 */  sw         $t2, 0x44($sp)
    /* 1D0014 151A2B64 AFAB0048 */  sw         $t3, 0x48($sp)
    /* 1D0018 151A2B68 AFAC004C */  sw         $t4, 0x4C($sp)
    /* 1D001C 151A2B6C 0D468B09 */  jal        func_151A2C24
    /* 1D0020 151A2B70 AFAD0050 */   sw        $t5, 0x50($sp)
    /* 1D0024 151A2B74 8FBF005C */  lw         $ra, 0x5C($sp)
    /* 1D0028 151A2B78 27BD0060 */  addiu      $sp, $sp, 0x60
    /* 1D002C 151A2B7C 03E00008 */  jr         $ra
    /* 1D0030 151A2B80 00000000 */   nop
endlabel func_151A2AD4
