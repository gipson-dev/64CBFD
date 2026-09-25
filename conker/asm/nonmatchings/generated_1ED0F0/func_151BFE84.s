glabel func_151BFE84
    /* 1ED334 151BFE84 27BDFEE0 */  addiu      $sp, $sp, -0x120
    /* 1ED338 151BFE88 AFB00018 */  sw         $s0, 0x18($sp)
    /* 1ED33C 151BFE8C 00A08025 */  or         $s0, $a1, $zero
    /* 1ED340 151BFE90 AFBF001C */  sw         $ra, 0x1C($sp)
    /* 1ED344 151BFE94 AFA40120 */  sw         $a0, 0x120($sp)
    /* 1ED348 151BFE98 AFA60128 */  sw         $a2, 0x128($sp)
    /* 1ED34C 151BFE9C AFA7012C */  sw         $a3, 0x12C($sp)
    /* 1ED350 151BFEA0 02002025 */  or         $a0, $s0, $zero
    /* 1ED354 151BFEA4 93A50133 */  lbu        $a1, 0x133($sp)
    /* 1ED358 151BFEA8 0D470106 */  jal        func_151C0418
    /* 1ED35C 151BFEAC 8FA60134 */   lw        $a2, 0x134($sp)
    /* 1ED360 151BFEB0 02002025 */  or         $a0, $s0, $zero
    /* 1ED364 151BFEB4 93A50133 */  lbu        $a1, 0x133($sp)
    /* 1ED368 151BFEB8 0D47013E */  jal        func_151C04F8
    /* 1ED36C 151BFEBC 8FA60134 */   lw        $a2, 0x134($sp)
    /* 1ED370 151BFEC0 02002025 */  or         $a0, $s0, $zero
    /* 1ED374 151BFEC4 93A50133 */  lbu        $a1, 0x133($sp)
    /* 1ED378 151BFEC8 0D470169 */  jal        func_151C05A4
    /* 1ED37C 151BFECC 8FA60134 */   lw        $a2, 0x134($sp)
    /* 1ED380 151BFED0 02002025 */  or         $a0, $s0, $zero
    /* 1ED384 151BFED4 93A50133 */  lbu        $a1, 0x133($sp)
    /* 1ED388 151BFED8 0D47017C */  jal        func_151C05F0
    /* 1ED38C 151BFEDC 8FA60134 */   lw        $a2, 0x134($sp)
    /* 1ED390 151BFEE0 8FAE0120 */  lw         $t6, 0x120($sp)
    /* 1ED394 151BFEE4 93AF012F */  lbu        $t7, 0x12F($sp)
    /* 1ED398 151BFEE8 51C00013 */  beql       $t6, $zero, .L151BFF38
    /* 1ED39C 151BFEEC 8FB80120 */   lw        $t8, 0x120($sp)
    /* 1ED3A0 151BFEF0 11E00010 */  beqz       $t7, .L151BFF34
    /* 1ED3A4 151BFEF4 01C02025 */   or        $a0, $t6, $zero
    /* 1ED3A8 151BFEF8 27A50114 */  addiu      $a1, $sp, 0x114
    /* 1ED3AC 151BFEFC 27A60108 */  addiu      $a2, $sp, 0x108
    /* 1ED3B0 151BFF00 0D4513A0 */  jal        func_15144E80
    /* 1ED3B4 151BFF04 27A700FC */   addiu     $a3, $sp, 0xFC
    /* 1ED3B8 151BFF08 1040000A */  beqz       $v0, .L151BFF34
    /* 1ED3BC 151BFF0C C7A40100 */   lwc1      $f4, 0x100($sp)
    /* 1ED3C0 151BFF10 44803000 */  mtc1       $zero, $f6
    /* 1ED3C4 151BFF14 02002025 */  or         $a0, $s0, $zero
    /* 1ED3C8 151BFF18 93A50133 */  lbu        $a1, 0x133($sp)
    /* 1ED3CC 151BFF1C 4606203C */  c.lt.s     $f4, $f6
    /* 1ED3D0 151BFF20 00000000 */  nop
    /* 1ED3D4 151BFF24 45020004 */  bc1fl      .L151BFF38
    /* 1ED3D8 151BFF28 8FB80120 */   lw        $t8, 0x120($sp)
    /* 1ED3DC 151BFF2C 0D470191 */  jal        func_151C0644
    /* 1ED3E0 151BFF30 8FA60134 */   lw        $a2, 0x134($sp)
  .L151BFF34:
    /* 1ED3E4 151BFF34 8FB80120 */  lw         $t8, 0x120($sp)
  .L151BFF38:
    /* 1ED3E8 151BFF38 93B9012F */  lbu        $t9, 0x12F($sp)
    /* 1ED3EC 151BFF3C 53000008 */  beql       $t8, $zero, .L151BFF60
    /* 1ED3F0 151BFF40 93A8012F */   lbu       $t0, 0x12F($sp)
    /* 1ED3F4 151BFF44 13200005 */  beqz       $t9, .L151BFF5C
    /* 1ED3F8 151BFF48 03002025 */   or        $a0, $t8, $zero
    /* 1ED3FC 151BFF4C 02002825 */  or         $a1, $s0, $zero
    /* 1ED400 151BFF50 93A60133 */  lbu        $a2, 0x133($sp)
    /* 1ED404 151BFF54 0D4700D8 */  jal        func_151C0360
    /* 1ED408 151BFF58 8FA70134 */   lw        $a3, 0x134($sp)
  .L151BFF5C:
    /* 1ED40C 151BFF5C 93A8012F */  lbu        $t0, 0x12F($sp)
  .L151BFF60:
    /* 1ED410 151BFF60 8FA90120 */  lw         $t1, 0x120($sp)
    /* 1ED414 151BFF64 51000048 */  beql       $t0, $zero, .L151C0088
    /* 1ED418 151BFF68 8FBF001C */   lw        $ra, 0x1C($sp)
    /* 1ED41C 151BFF6C 1120002E */  beqz       $t1, .L151C0028
    /* 1ED420 151BFF70 8FA20128 */   lw        $v0, 0x128($sp)
    /* 1ED424 151BFF74 8FA20128 */  lw         $v0, 0x128($sp)
    /* 1ED428 151BFF78 C4480000 */  lwc1       $f8, 0x0($v0)
    /* 1ED42C 151BFF7C 27AA0090 */  addiu      $t2, $sp, 0x90
    /* 1ED430 151BFF80 27AF00B0 */  addiu      $t7, $sp, 0xB0
    /* 1ED434 151BFF84 46004287 */  neg.s      $f10, $f8
    /* 1ED438 151BFF88 27A400A8 */  addiu      $a0, $sp, 0xA8
    /* 1ED43C 151BFF8C E7AA0084 */  swc1       $f10, 0x84($sp)
    /* 1ED440 151BFF90 C4500004 */  lwc1       $f16, 0x4($v0)
    /* 1ED444 151BFF94 27A500A4 */  addiu      $a1, $sp, 0xA4
    /* 1ED448 151BFF98 46008487 */  neg.s      $f18, $f16
    /* 1ED44C 151BFF9C E7B20088 */  swc1       $f18, 0x88($sp)
    /* 1ED450 151BFFA0 C4440008 */  lwc1       $f4, 0x8($v0)
    /* 1ED454 151BFFA4 46002187 */  neg.s      $f6, $f4
    /* 1ED458 151BFFA8 E7A6008C */  swc1       $f6, 0x8C($sp)
    /* 1ED45C 151BFFAC 89210000 */  lwl        $at, 0x0($t1)
    /* 1ED460 151BFFB0 99210003 */  lwr        $at, 0x3($t1)
    /* 1ED464 151BFFB4 A9410000 */  swl        $at, 0x0($t2)
    /* 1ED468 151BFFB8 B9410003 */  swr        $at, 0x3($t2)
    /* 1ED46C 151BFFBC 892D0004 */  lwl        $t5, 0x4($t1)
    /* 1ED470 151BFFC0 992D0007 */  lwr        $t5, 0x7($t1)
    /* 1ED474 151BFFC4 A94D0004 */  swl        $t5, 0x4($t2)
    /* 1ED478 151BFFC8 B94D0007 */  swr        $t5, 0x7($t2)
    /* 1ED47C 151BFFCC 89210008 */  lwl        $at, 0x8($t1)
    /* 1ED480 151BFFD0 9921000B */  lwr        $at, 0xB($t1)
    /* 1ED484 151BFFD4 A9410008 */  swl        $at, 0x8($t2)
    /* 1ED488 151BFFD8 B941000B */  swr        $at, 0xB($t2)
    /* 1ED48C 151BFFDC 892D000C */  lwl        $t5, 0xC($t1)
    /* 1ED490 151BFFE0 992D000F */  lwr        $t5, 0xF($t1)
    /* 1ED494 151BFFE4 A94D000C */  swl        $t5, 0xC($t2)
    /* 1ED498 151BFFE8 B94D000F */  swr        $t5, 0xF($t2)
    /* 1ED49C 151BFFEC 95210010 */  lhu        $at, 0x10($t1)
    /* 1ED4A0 151BFFF0 A5410010 */  sh         $at, 0x10($t2)
    /* 1ED4A4 151BFFF4 8E010000 */  lw         $at, 0x0($s0)
    /* 1ED4A8 151BFFF8 ADE10000 */  sw         $at, 0x0($t7)
    /* 1ED4AC 151BFFFC 8E180004 */  lw         $t8, 0x4($s0)
    /* 1ED4B0 151C0000 ADF80004 */  sw         $t8, 0x4($t7)
    /* 1ED4B4 151C0004 8E010008 */  lw         $at, 0x8($s0)
    /* 1ED4B8 151C0008 0D46FF10 */  jal        func_151BFC40
    /* 1ED4BC 151C000C ADE10008 */   sw        $at, 0x8($t7)
    /* 1ED4C0 151C0010 27A40084 */  addiu      $a0, $sp, 0x84
    /* 1ED4C4 151C0014 93A50133 */  lbu        $a1, 0x133($sp)
    /* 1ED4C8 151C0018 0D453EFF */  jal        func_1514FBFC
    /* 1ED4CC 151C001C 8FA60134 */   lw        $a2, 0x134($sp)
    /* 1ED4D0 151C0020 10000019 */  b          .L151C0088
    /* 1ED4D4 151C0024 8FBF001C */   lw        $ra, 0x1C($sp)
  .L151C0028:
    /* 1ED4D8 151C0028 C4480000 */  lwc1       $f8, 0x0($v0)
    /* 1ED4DC 151C002C 27A40030 */  addiu      $a0, $sp, 0x30
    /* 1ED4E0 151C0030 27A5002C */  addiu      $a1, $sp, 0x2C
    /* 1ED4E4 151C0034 46004287 */  neg.s      $f10, $f8
    /* 1ED4E8 151C0038 E7AA0020 */  swc1       $f10, 0x20($sp)
    /* 1ED4EC 151C003C C4500004 */  lwc1       $f16, 0x4($v0)
    /* 1ED4F0 151C0040 46008487 */  neg.s      $f18, $f16
    /* 1ED4F4 151C0044 E7B20024 */  swc1       $f18, 0x24($sp)
    /* 1ED4F8 151C0048 C4440008 */  lwc1       $f4, 0x8($v0)
    /* 1ED4FC 151C004C 46002187 */  neg.s      $f6, $f4
    /* 1ED500 151C0050 0D46FF10 */  jal        func_151BFC40
    /* 1ED504 151C0054 E7A60028 */   swc1      $f6, 0x28($sp)
    /* 1ED508 151C0058 8E010000 */  lw         $at, 0x0($s0)
    /* 1ED50C 151C005C 27A80038 */  addiu      $t0, $sp, 0x38
    /* 1ED510 151C0060 27A40020 */  addiu      $a0, $sp, 0x20
    /* 1ED514 151C0064 AD010000 */  sw         $at, 0x0($t0)
    /* 1ED518 151C0068 8E0A0004 */  lw         $t2, 0x4($s0)
    /* 1ED51C 151C006C AD0A0004 */  sw         $t2, 0x4($t0)
    /* 1ED520 151C0070 8E010008 */  lw         $at, 0x8($s0)
    /* 1ED524 151C0074 AD010008 */  sw         $at, 0x8($t0)
    /* 1ED528 151C0078 8FA60134 */  lw         $a2, 0x134($sp)
    /* 1ED52C 151C007C 0D453EE6 */  jal        func_1514FB98
    /* 1ED530 151C0080 93A50133 */   lbu       $a1, 0x133($sp)
    /* 1ED534 151C0084 8FBF001C */  lw         $ra, 0x1C($sp)
  .L151C0088:
    /* 1ED538 151C0088 8FB00018 */  lw         $s0, 0x18($sp)
    /* 1ED53C 151C008C 27BD0120 */  addiu      $sp, $sp, 0x120
    /* 1ED540 151C0090 03E00008 */  jr         $ra
    /* 1ED544 151C0094 00000000 */   nop
endlabel func_151BFE84
