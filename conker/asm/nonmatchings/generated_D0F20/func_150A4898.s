  glabel func_150A4898
    /* D1D48 150A4898 4407C000 */  mfc1       $a3, $f24
    /* D1D4C 150A489C 14E00004 */  bnez       $a3, .L150A48B0
    /* D1D50 150A48A0 96490056 */   lhu       $t1, 0x56($s2)
    /* D1D54 150A48A4 9248006F */  lbu        $t0, 0x6F($s2)
    /* D1D58 150A48A8 31080080 */  andi       $t0, $t0, 0x80
    /* D1D5C 150A48AC 15000036 */  bnez       $t0, .L150A4988
  .L150A48B0:
    /* D1D60 150A48B0 96480058 */   lhu       $t0, 0x58($s2)
    /* D1D64 150A48B4 000840C0 */  sll        $t0, $t0, 3
    /* D1D68 150A48B8 02885021 */  addu       $t2, $s4, $t0
    /* D1D6C 150A48BC 02C8C821 */  addu       $t9, $s6, $t0
    /* D1D70 150A48C0 00084042 */  srl        $t0, $t0, 1
    /* D1D74 150A48C4 02A85821 */  addu       $t3, $s5, $t0
    /* D1D78 150A48C8 0328C821 */  addu       $t9, $t9, $t0
    /* D1D7C 150A48CC 000948C0 */  sll        $t1, $t1, 3
    /* D1D80 150A48D0 012A4821 */  addu       $t1, $t1, $t2
  .L150A48D4:
    /* D1D84 150A48D4 8F2E0000 */  lw         $t6, 0x0($t9)
    /* D1D88 150A48D8 8F240004 */  lw         $a0, 0x4($t9)
    /* D1D8C 150A48DC 8F260008 */  lw         $a2, 0x8($t9)
    /* D1D90 150A48E0 01D37020 */  add        $t6, $t6, $s3 /* handwritten instruction */
    /* D1D94 150A48E4 85CC0000 */  lh         $t4, 0x0($t6)
    /* D1D98 150A48E8 85CD0002 */  lh         $t5, 0x2($t6)
    /* D1D9C 150A48EC 85CE0004 */  lh         $t6, 0x4($t6)
    /* D1DA0 150A48F0 01807825 */  or         $t7, $t4, $zero
    /* D1DA4 150A48F4 01A0C025 */  or         $t8, $t5, $zero
    /* D1DA8 150A48F8 01C04025 */  or         $t0, $t6, $zero
    /* D1DAC 150A48FC 00932020 */  add        $a0, $a0, $s3 /* handwritten instruction */
    /* D1DB0 150A4900 00D33020 */  add        $a2, $a2, $s3 /* handwritten instruction */
  .L150A4904:
    /* D1DB4 150A4904 84850000 */  lh         $a1, 0x0($a0)
    /* D1DB8 150A4908 84920002 */  lh         $s2, 0x2($a0)
    /* D1DBC 150A490C 84820004 */  lh         $v0, 0x4($a0)
    /* D1DC0 150A4910 00AC082A */  slt        $at, $a1, $t4
    /* D1DC4 150A4914 54200004 */  bnel       $at, $zero, .L150A4928
    /* D1DC8 150A4918 00A06025 */   or        $t4, $a1, $zero
    /* D1DCC 150A491C 01E5082A */  slt        $at, $t7, $a1
    /* D1DD0 150A4920 54200001 */  bnel       $at, $zero, .L150A4928
    /* D1DD4 150A4924 00A07825 */   or        $t7, $a1, $zero
  .L150A4928:
    /* D1DD8 150A4928 024D082A */  slt        $at, $s2, $t5
    /* D1DDC 150A492C 54200004 */  bnel       $at, $zero, .L150A4940
    /* D1DE0 150A4930 02406825 */   or        $t5, $s2, $zero
    /* D1DE4 150A4934 0312082A */  slt        $at, $t8, $s2
    /* D1DE8 150A4938 54200001 */  bnel       $at, $zero, .L150A4940
    /* D1DEC 150A493C 0240C025 */   or        $t8, $s2, $zero
  .L150A4940:
    /* D1DF0 150A4940 004E082A */  slt        $at, $v0, $t6
    /* D1DF4 150A4944 54200004 */  bnel       $at, $zero, .L150A4958
    /* D1DF8 150A4948 00407025 */   or        $t6, $v0, $zero
    /* D1DFC 150A494C 0102082A */  slt        $at, $t0, $v0
    /* D1E00 150A4950 54200001 */  bnel       $at, $zero, .L150A4958
    /* D1E04 150A4954 00404025 */   or        $t0, $v0, $zero
  .L150A4958:
    /* D1E08 150A4958 1486FFEA */  bne        $a0, $a2, .L150A4904
    /* D1E0C 150A495C 00C02025 */   or        $a0, $a2, $zero
    /* D1E10 150A4960 A54C0000 */  sh         $t4, 0x0($t2)
    /* D1E14 150A4964 A54F0004 */  sh         $t7, 0x4($t2)
    /* D1E18 150A4968 A54E0002 */  sh         $t6, 0x2($t2)
    /* D1E1C 150A496C A5480006 */  sh         $t0, 0x6($t2)
    /* D1E20 150A4970 254A0008 */  addiu      $t2, $t2, 0x8
    /* D1E24 150A4974 A56D0000 */  sh         $t5, 0x0($t3)
    /* D1E28 150A4978 256B0004 */  addiu      $t3, $t3, 0x4
    /* D1E2C 150A497C A578FFFE */  sh         $t8, -0x2($t3)
    /* D1E30 150A4980 1549FFD4 */  bne        $t2, $t1, .L150A48D4
    /* D1E34 150A4984 2739000C */   addiu     $t9, $t9, 0xC
  .L150A4988:
    /* D1E38 150A4988 8FB30054 */  lw         $s3, 0x54($sp)
    /* D1E3C 150A498C 12600003 */  beqz       $s3, .L150A499C
    /* D1E40 150A4990 02602025 */   or        $a0, $s3, $zero
    /* D1E44 150A4994 0C00101D */  jal        func_10004074
    /* D1E48 150A4998 00000000 */   nop
  .L150A499C:
    /* D1E4C 150A499C 1611FF02 */  bne        $s0, $s1, .L150A45A8
    /* D1E50 150A49A0 26100002 */   addiu     $s0, $s0, 0x2
    /* D1E54 150A49A4 8FB00010 */  lw         $s0, 0x10($sp)
    /* D1E58 150A49A8 8FB10014 */  lw         $s1, 0x14($sp)
    /* D1E5C 150A49AC 8FB20018 */  lw         $s2, 0x18($sp)
    /* D1E60 150A49B0 8FB3001C */  lw         $s3, 0x1C($sp)
    /* D1E64 150A49B4 8FB40020 */  lw         $s4, 0x20($sp)
    /* D1E68 150A49B8 8FB50024 */  lw         $s5, 0x24($sp)
    /* D1E6C 150A49BC 8FB60028 */  lw         $s6, 0x28($sp)
    /* D1E70 150A49C0 8FB7002C */  lw         $s7, 0x2C($sp)
    /* D1E74 150A49C4 8FBE0030 */  lw         $fp, 0x30($sp)
    /* D1E78 150A49C8 8FBC0034 */  lw         $gp, 0x34($sp)
    /* D1E7C 150A49CC 8FBF0038 */  lw         $ra, 0x38($sp)
    /* D1E80 150A49D0 C7B4003C */  lwc1       $f20, 0x3C($sp)
    /* D1E84 150A49D4 C7B50040 */  lwc1       $f21, 0x40($sp)
    /* D1E88 150A49D8 C7B60044 */  lwc1       $f22, 0x44($sp)
    /* D1E8C 150A49DC C7B70048 */  lwc1       $f23, 0x48($sp)
    /* D1E90 150A49E0 C7B8004C */  lwc1       $f24, 0x4C($sp)
    /* D1E94 150A49E4 C7B90050 */  lwc1       $f25, 0x50($sp)
    /* D1E98 150A49E8 27BD0058 */  addiu      $sp, $sp, 0x58
  .L150A49EC:
    /* D1E9C 150A49EC 03E00008 */  jr         $ra
    /* D1EA0 150A49F0 00000000 */   nop
endlabel func_150A4898
