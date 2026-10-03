  glabel func_150A3BAC
    /* D105C 150A3BAC 02001825 */  or         $v1, $s0, $zero
    /* D1060 150A3BB0 001080C0 */  sll        $s0, $s0, 3
    /* D1064 150A3BB4 020CC821 */  addu       $t9, $s0, $t4
    /* D1068 150A3BB8 872D0000 */  lh         $t5, 0x0($t9)
    /* D106C 150A3BBC 87320002 */  lh         $s2, 0x2($t9)
    /* D1070 150A3BC0 25ADFFFE */  addiu      $t5, $t5, -0x2
    /* D1074 150A3BC4 008D082A */  slt        $at, $a0, $t5
    /* D1078 150A3BC8 142000E1 */  bnez       $at, .L150A3F50
    /* D107C 150A3BCC 2652FFFE */   addiu     $s2, $s2, -0x2
    /* D1080 150A3BD0 00B2082A */  slt        $at, $a1, $s2
    /* D1084 150A3BD4 142000DE */  bnez       $at, .L150A3F50
    /* D1088 150A3BD8 87350004 */   lh        $s5, 0x4($t9)
    /* D108C 150A3BDC 873E0006 */  lh         $fp, 0x6($t9)
    /* D1090 150A3BE0 26B50002 */  addiu      $s5, $s5, 0x2
    /* D1094 150A3BE4 02A4082A */  slt        $at, $s5, $a0
    /* D1098 150A3BE8 142000D9 */  bnez       $at, .L150A3F50
    /* D109C 150A3BEC 27DE0002 */   addiu     $fp, $fp, 0x2
    /* D10A0 150A3BF0 03C5082A */  slt        $at, $fp, $a1
    /* D10A4 150A3BF4 142000D6 */  bnez       $at, .L150A3F50
    /* D10A8 150A3BF8 020BC821 */   addu      $t9, $s0, $t3
    /* D10AC 150A3BFC 00108042 */  srl        $s0, $s0, 1
    /* D10B0 150A3C00 0330C821 */  addu       $t9, $t9, $s0
    /* D10B4 150A3C04 8F320000 */  lw         $s2, 0x0($t9)
    /* D10B8 150A3C08 8F350004 */  lw         $s5, 0x4($t9)
    /* D10BC 150A3C0C 8F3E0008 */  lw         $fp, 0x8($t9)
    /* D10C0 150A3C10 02489021 */  addu       $s2, $s2, $t0
    /* D10C4 150A3C14 02A8A821 */  addu       $s5, $s5, $t0
    /* D10C8 150A3C18 03C8F021 */  addu       $fp, $fp, $t0
    /* D10CC 150A3C1C 86500000 */  lh         $s0, 0x0($s2)
    /* D10D0 150A3C20 86510002 */  lh         $s1, 0x2($s2)
    /* D10D4 150A3C24 86520004 */  lh         $s2, 0x4($s2)
    /* D10D8 150A3C28 86B30000 */  lh         $s3, 0x0($s5)
    /* D10DC 150A3C2C 86B40002 */  lh         $s4, 0x2($s5)
    /* D10E0 150A3C30 86B50004 */  lh         $s5, 0x4($s5)
    /* D10E4 150A3C34 87D60000 */  lh         $s6, 0x0($fp)
    /* D10E8 150A3C38 87D70002 */  lh         $s7, 0x2($fp)
    /* D10EC 150A3C3C 87DE0004 */  lh         $fp, 0x4($fp)
    /* D10F0 150A3C40 0255082A */  slt        $at, $s2, $s5
    /* D10F4 150A3C44 1020000F */  beqz       $at, .L150A3C84
    /* D10F8 150A3C48 00000000 */   nop
    /* D10FC 150A3C4C 03D2082A */  slt        $at, $fp, $s2
    /* D1100 150A3C50 1020001A */  beqz       $at, func_150A3CBC
    /* D1104 150A3C54 00000000 */   nop
  .L150A3C58:
    /* D1108 150A3C58 02C06825 */  or         $t5, $s6, $zero
    /* D110C 150A3C5C 03C07025 */  or         $t6, $fp, $zero
    /* D1110 150A3C60 02E07825 */  or         $t7, $s7, $zero
    /* D1114 150A3C64 0200B025 */  or         $s6, $s0, $zero
    /* D1118 150A3C68 0240F025 */  or         $fp, $s2, $zero
    /* D111C 150A3C6C 0220B825 */  or         $s7, $s1, $zero
    /* D1120 150A3C70 01A08025 */  or         $s0, $t5, $zero
    /* D1124 150A3C74 01C09025 */  or         $s2, $t6, $zero
    /* D1128 150A3C78 01E08825 */  or         $s1, $t7, $zero
    /* D112C 150A3C7C 09428F2F */  j          func_150A3CBC
    /* D1130 150A3C80 00000000 */   nop
  .L150A3C84:
    /* D1134 150A3C84 02BE082A */  slt        $at, $s5, $fp
    /* D1138 150A3C88 1020FFF3 */  beqz       $at, .L150A3C58
    /* D113C 150A3C8C 00000000 */   nop
    /* D1140 150A3C90 02606825 */  or         $t5, $s3, $zero
    /* D1144 150A3C94 02A07025 */  or         $t6, $s5, $zero
    /* D1148 150A3C98 02807825 */  or         $t7, $s4, $zero
    /* D114C 150A3C9C 02009825 */  or         $s3, $s0, $zero
    /* D1150 150A3CA0 0240A825 */  or         $s5, $s2, $zero
    /* D1154 150A3CA4 0220A025 */  or         $s4, $s1, $zero
    /* D1158 150A3CA8 01A08025 */  or         $s0, $t5, $zero
    /* D115C 150A3CAC 01C09025 */  or         $s2, $t6, $zero
    /* D1160 150A3CB0 01E08825 */  or         $s1, $t7, $zero
    /* D1164 150A3CB4 09428F2F */  j          func_150A3CBC
    /* D1168 150A3CB8 00000000 */   nop
endlabel func_150A3BAC
