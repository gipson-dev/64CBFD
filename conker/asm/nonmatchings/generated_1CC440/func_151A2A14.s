glabel func_151A2A14
    /* 1CFEC4 151A2A14 27BDFFA0 */  addiu      $sp, $sp, -0x60
    /* 1CFEC8 151A2A18 AFA60068 */  sw         $a2, 0x68($sp)
    /* 1CFECC 151A2A1C AFA50064 */  sw         $a1, 0x64($sp)
    /* 1CFED0 151A2A20 44876000 */  mtc1       $a3, $f12
    /* 1CFED4 151A2A24 87A7006A */  lh         $a3, 0x6A($sp)
    /* 1CFED8 151A2A28 87A60066 */  lh         $a2, 0x66($sp)
    /* 1CFEDC 151A2A2C AFBF005C */  sw         $ra, 0x5C($sp)
    /* 1CFEE0 151A2A30 8FAE0078 */  lw         $t6, 0x78($sp)
    /* 1CFEE4 151A2A34 C7A40070 */  lwc1       $f4, 0x70($sp)
    /* 1CFEE8 151A2A38 C7A60074 */  lwc1       $f6, 0x74($sp)
    /* 1CFEEC 151A2A3C C7A8007C */  lwc1       $f8, 0x7C($sp)
    /* 1CFEF0 151A2A40 C7AA0080 */  lwc1       $f10, 0x80($sp)
    /* 1CFEF4 151A2A44 C7B00084 */  lwc1       $f16, 0x84($sp)
    /* 1CFEF8 151A2A48 C7B20088 */  lwc1       $f18, 0x88($sp)
    /* 1CFEFC 151A2A4C 87AF008E */  lh         $t7, 0x8E($sp)
    /* 1CFF00 151A2A50 87B80092 */  lh         $t8, 0x92($sp)
    /* 1CFF04 151A2A54 87B90096 */  lh         $t9, 0x96($sp)
    /* 1CFF08 151A2A58 87A8009A */  lh         $t0, 0x9A($sp)
    /* 1CFF0C 151A2A5C 87A9009E */  lh         $t1, 0x9E($sp)
    /* 1CFF10 151A2A60 87AA00A2 */  lh         $t2, 0xA2($sp)
    /* 1CFF14 151A2A64 83AB00A7 */  lb         $t3, 0xA7($sp)
    /* 1CFF18 151A2A68 93AC00AB */  lbu        $t4, 0xAB($sp)
    /* 1CFF1C 151A2A6C 8FAD00AC */  lw         $t5, 0xAC($sp)
    /* 1CFF20 151A2A70 AFAE001C */  sw         $t6, 0x1C($sp)
    /* 1CFF24 151A2A74 240E0001 */  addiu      $t6, $zero, 0x1
    /* 1CFF28 151A2A78 AFAE0054 */  sw         $t6, 0x54($sp)
    /* 1CFF2C 151A2A7C 00002825 */  or         $a1, $zero, $zero
    /* 1CFF30 151A2A80 E7AC0010 */  swc1       $f12, 0x10($sp)
    /* 1CFF34 151A2A84 E7A40014 */  swc1       $f4, 0x14($sp)
    /* 1CFF38 151A2A88 E7A60018 */  swc1       $f6, 0x18($sp)
    /* 1CFF3C 151A2A8C E7A80020 */  swc1       $f8, 0x20($sp)
    /* 1CFF40 151A2A90 E7AA0024 */  swc1       $f10, 0x24($sp)
    /* 1CFF44 151A2A94 E7B00028 */  swc1       $f16, 0x28($sp)
    /* 1CFF48 151A2A98 E7B2002C */  swc1       $f18, 0x2C($sp)
    /* 1CFF4C 151A2A9C AFAF0030 */  sw         $t7, 0x30($sp)
    /* 1CFF50 151A2AA0 AFB80034 */  sw         $t8, 0x34($sp)
    /* 1CFF54 151A2AA4 AFB90038 */  sw         $t9, 0x38($sp)
    /* 1CFF58 151A2AA8 AFA8003C */  sw         $t0, 0x3C($sp)
    /* 1CFF5C 151A2AAC AFA90040 */  sw         $t1, 0x40($sp)
    /* 1CFF60 151A2AB0 AFAA0044 */  sw         $t2, 0x44($sp)
    /* 1CFF64 151A2AB4 AFAB0048 */  sw         $t3, 0x48($sp)
    /* 1CFF68 151A2AB8 AFAC004C */  sw         $t4, 0x4C($sp)
    /* 1CFF6C 151A2ABC 0D468B09 */  jal        func_151A2C24
    /* 1CFF70 151A2AC0 AFAD0050 */   sw        $t5, 0x50($sp)
    /* 1CFF74 151A2AC4 8FBF005C */  lw         $ra, 0x5C($sp)
    /* 1CFF78 151A2AC8 27BD0060 */  addiu      $sp, $sp, 0x60
    /* 1CFF7C 151A2ACC 03E00008 */  jr         $ra
    /* 1CFF80 151A2AD0 00000000 */   nop
endlabel func_151A2A14
