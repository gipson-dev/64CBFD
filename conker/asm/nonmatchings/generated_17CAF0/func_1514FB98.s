glabel func_1514FB98
    /* 17D048 1514FB98 27BDFFC0 */  addiu      $sp, $sp, -0x40
    /* 17D04C 1514FB9C AFBF0024 */  sw         $ra, 0x24($sp)
    /* 17D050 1514FBA0 AFA40040 */  sw         $a0, 0x40($sp)
    /* 17D054 1514FBA4 AFA50044 */  sw         $a1, 0x44($sp)
    /* 17D058 1514FBA8 AFA60048 */  sw         $a2, 0x48($sp)
    /* 17D05C 1514FBAC 8FA40040 */  lw         $a0, 0x40($sp)
    /* 17D060 1514FBB0 27A50034 */  addiu      $a1, $sp, 0x34
    /* 17D064 1514FBB4 0D45181E */  jal        func_15146078
    /* 17D068 1514FBB8 27A60028 */   addiu     $a2, $sp, 0x28
    /* 17D06C 1514FBBC 1040000B */  beqz       $v0, .L1514FBEC
    /* 17D070 1514FBC0 8FA50040 */   lw        $a1, 0x40($sp)
    /* 17D074 1514FBC4 C4A4000C */  lwc1       $f4, 0xC($a1)
    /* 17D078 1514FBC8 93AE0047 */  lbu        $t6, 0x47($sp)
    /* 17D07C 1514FBCC 8FAF0048 */  lw         $t7, 0x48($sp)
    /* 17D080 1514FBD0 24A40010 */  addiu      $a0, $a1, 0x10
    /* 17D084 1514FBD4 27A60034 */  addiu      $a2, $sp, 0x34
    /* 17D088 1514FBD8 27A70028 */  addiu      $a3, $sp, 0x28
    /* 17D08C 1514FBDC E7A40010 */  swc1       $f4, 0x10($sp)
    /* 17D090 1514FBE0 AFAE0014 */  sw         $t6, 0x14($sp)
    /* 17D094 1514FBE4 0D453E3E */  jal        func_1514F8F8
    /* 17D098 1514FBE8 AFAF0018 */   sw        $t7, 0x18($sp)
  .L1514FBEC:
    /* 17D09C 1514FBEC 8FBF0024 */  lw         $ra, 0x24($sp)
    /* 17D0A0 1514FBF0 27BD0040 */  addiu      $sp, $sp, 0x40
    /* 17D0A4 1514FBF4 03E00008 */  jr         $ra
    /* 17D0A8 1514FBF8 00000000 */   nop
endlabel func_1514FB98
