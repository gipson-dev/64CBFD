glabel func_151BFDA0
    /* 1ED250 151BFDA0 27BDFF78 */  addiu      $sp, $sp, -0x88
    /* 1ED254 151BFDA4 AFB10018 */  sw         $s1, 0x18($sp)
    /* 1ED258 151BFDA8 AFB00014 */  sw         $s0, 0x14($sp)
    /* 1ED25C 151BFDAC 00808025 */  or         $s0, $a0, $zero
    /* 1ED260 151BFDB0 30F100FF */  andi       $s1, $a3, 0xFF
    /* 1ED264 151BFDB4 AFBF001C */  sw         $ra, 0x1C($sp)
    /* 1ED268 151BFDB8 AFA5008C */  sw         $a1, 0x8C($sp)
    /* 1ED26C 151BFDBC AFA60090 */  sw         $a2, 0x90($sp)
    /* 1ED270 151BFDC0 AFA70094 */  sw         $a3, 0x94($sp)
    /* 1ED274 151BFDC4 02002025 */  or         $a0, $s0, $zero
    /* 1ED278 151BFDC8 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED27C 151BFDCC 0D470106 */  jal        func_151C0418
    /* 1ED280 151BFDD0 8FA60098 */   lw        $a2, 0x98($sp)
    /* 1ED284 151BFDD4 02002025 */  or         $a0, $s0, $zero
    /* 1ED288 151BFDD8 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED28C 151BFDDC 0D47013E */  jal        func_151C04F8
    /* 1ED290 151BFDE0 8FA60098 */   lw        $a2, 0x98($sp)
    /* 1ED294 151BFDE4 02002025 */  or         $a0, $s0, $zero
    /* 1ED298 151BFDE8 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED29C 151BFDEC 0D470169 */  jal        func_151C05A4
    /* 1ED2A0 151BFDF0 8FA60098 */   lw        $a2, 0x98($sp)
    /* 1ED2A4 151BFDF4 02002025 */  or         $a0, $s0, $zero
    /* 1ED2A8 151BFDF8 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED2AC 151BFDFC 0D47017C */  jal        func_151C05F0
    /* 1ED2B0 151BFE00 8FA60098 */   lw        $a2, 0x98($sp)
    /* 1ED2B4 151BFE04 93AE0093 */  lbu        $t6, 0x93($sp)
    /* 1ED2B8 151BFE08 8FA2008C */  lw         $v0, 0x8C($sp)
    /* 1ED2BC 151BFE0C 51C00019 */  beql       $t6, $zero, .L151BFE74
    /* 1ED2C0 151BFE10 8FBF001C */   lw        $ra, 0x1C($sp)
    /* 1ED2C4 151BFE14 C4440000 */  lwc1       $f4, 0x0($v0)
    /* 1ED2C8 151BFE18 27A40034 */  addiu      $a0, $sp, 0x34
    /* 1ED2CC 151BFE1C 27A50030 */  addiu      $a1, $sp, 0x30
    /* 1ED2D0 151BFE20 46002187 */  neg.s      $f6, $f4
    /* 1ED2D4 151BFE24 E7A60024 */  swc1       $f6, 0x24($sp)
    /* 1ED2D8 151BFE28 C4480004 */  lwc1       $f8, 0x4($v0)
    /* 1ED2DC 151BFE2C 46004287 */  neg.s      $f10, $f8
    /* 1ED2E0 151BFE30 E7AA0028 */  swc1       $f10, 0x28($sp)
    /* 1ED2E4 151BFE34 C4500008 */  lwc1       $f16, 0x8($v0)
    /* 1ED2E8 151BFE38 46008487 */  neg.s      $f18, $f16
    /* 1ED2EC 151BFE3C 0D46FF10 */  jal        func_151BFC40
    /* 1ED2F0 151BFE40 E7B2002C */   swc1      $f18, 0x2C($sp)
    /* 1ED2F4 151BFE44 8E010000 */  lw         $at, 0x0($s0)
    /* 1ED2F8 151BFE48 27AF003C */  addiu      $t7, $sp, 0x3C
    /* 1ED2FC 151BFE4C 27A40024 */  addiu      $a0, $sp, 0x24
    /* 1ED300 151BFE50 ADE10000 */  sw         $at, 0x0($t7)
    /* 1ED304 151BFE54 8E080004 */  lw         $t0, 0x4($s0)
    /* 1ED308 151BFE58 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED30C 151BFE5C ADE80004 */  sw         $t0, 0x4($t7)
    /* 1ED310 151BFE60 8E010008 */  lw         $at, 0x8($s0)
    /* 1ED314 151BFE64 ADE10008 */  sw         $at, 0x8($t7)
    /* 1ED318 151BFE68 0D453EE6 */  jal        func_1514FB98
    /* 1ED31C 151BFE6C 8FA60098 */   lw        $a2, 0x98($sp)
    /* 1ED320 151BFE70 8FBF001C */  lw         $ra, 0x1C($sp)
  .L151BFE74:
    /* 1ED324 151BFE74 8FB00014 */  lw         $s0, 0x14($sp)
    /* 1ED328 151BFE78 8FB10018 */  lw         $s1, 0x18($sp)
    /* 1ED32C 151BFE7C 03E00008 */  jr         $ra
    /* 1ED330 151BFE80 27BD0088 */   addiu     $sp, $sp, 0x88
endlabel func_151BFDA0
