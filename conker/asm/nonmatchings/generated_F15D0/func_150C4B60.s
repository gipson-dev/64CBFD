glabel func_150C4B60
    /* F2010 150C4B60 27BDFFE0 */  addiu      $sp, $sp, -0x20
    /* F2014 150C4B64 AFBF001C */  sw         $ra, 0x1C($sp)
    /* F2018 150C4B68 AFA40020 */  sw         $a0, 0x20($sp)
    /* F201C 150C4B6C AFA50024 */  sw         $a1, 0x24($sp)
    /* F2020 150C4B70 AFA60028 */  sw         $a2, 0x28($sp)
    /* F2024 150C4B74 93A2002B */  lbu        $v0, 0x2B($sp)
    /* F2028 150C4B78 24010055 */  addiu      $at, $zero, 0x55
    /* F202C 150C4B7C 8FA60020 */  lw         $a2, 0x20($sp)
    /* F2030 150C4B80 54410007 */  bnel       $v0, $at, .L150C4BA0
    /* F2034 150C4B84 24010056 */   addiu     $at, $zero, 0x56
    /* F2038 150C4B88 90CE003E */  lbu        $t6, 0x3E($a2)
    /* F203C 150C4B8C 24C60028 */  addiu      $a2, $a2, 0x28
    /* F2040 150C4B90 31CFFFFD */  andi       $t7, $t6, 0xFFFD
    /* F2044 150C4B94 10000010 */  b          .L150C4BD8
    /* F2048 150C4B98 A0CF0016 */   sb        $t7, 0x16($a2)
    /* F204C 150C4B9C 24010056 */  addiu      $at, $zero, 0x56
  .L150C4BA0:
    /* F2050 150C4BA0 14410007 */  bne        $v0, $at, .L150C4BC0
    /* F2054 150C4BA4 8FA80020 */   lw        $t0, 0x20($sp)
    /* F2058 150C4BA8 8FA60020 */  lw         $a2, 0x20($sp)
    /* F205C 150C4BAC 90D8003E */  lbu        $t8, 0x3E($a2)
    /* F2060 150C4BB0 24C60028 */  addiu      $a2, $a2, 0x28
    /* F2064 150C4BB4 37190002 */  ori        $t9, $t8, 0x2
    /* F2068 150C4BB8 10000007 */  b          .L150C4BD8
    /* F206C 150C4BBC A0D90016 */   sb        $t9, 0x16($a2)
  .L150C4BC0:
    /* F2070 150C4BC0 25060028 */  addiu      $a2, $t0, 0x28
    /* F2074 150C4BC4 24C70004 */  addiu      $a3, $a2, 0x4
    /* F2078 150C4BC8 8FA40024 */  lw         $a0, 0x24($sp)
    /* F207C 150C4BCC 93A5002B */  lbu        $a1, 0x2B($sp)
    /* F2080 150C4BD0 0D452545 */  jal        func_15149514
    /* F2084 150C4BD4 AFA80010 */   sw        $t0, 0x10($sp)
  .L150C4BD8:
    /* F2088 150C4BD8 8FBF001C */  lw         $ra, 0x1C($sp)
    /* F208C 150C4BDC 27BD0020 */  addiu      $sp, $sp, 0x20
    /* F2090 150C4BE0 03E00008 */  jr         $ra
    /* F2094 150C4BE4 00000000 */   nop
endlabel func_150C4B60
    /* F2098 150C4BE8 00000000 */  nop
    /* F209C 150C4BEC 00000000 */  nop
