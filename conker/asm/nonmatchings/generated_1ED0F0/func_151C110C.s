glabel func_151C110C
    /* 1EE5BC 151C110C AFA50004 */  sw         $a1, 0x4($sp)
    /* 1EE5C0 151C1110 AFA7000C */  sw         $a3, 0xC($sp)
    /* 1EE5C4 151C1114 8C830018 */  lw         $v1, 0x18($a0)
    /* 1EE5C8 151C1118 8FAB0018 */  lw         $t3, 0x18($sp)
    /* 1EE5CC 151C111C 00001025 */  or         $v0, $zero, $zero
    /* 1EE5D0 151C1120 50600015 */  beql       $v1, $zero, .L151C1178
    /* 1EE5D4 151C1124 A5600000 */   sh        $zero, 0x0($t3)
    /* 1EE5D8 151C1128 8CCE0000 */  lw         $t6, 0x0($a2)
    /* 1EE5DC 151C112C 51C00012 */  beql       $t6, $zero, .L151C1178
    /* 1EE5E0 151C1130 A5600000 */   sh        $zero, 0x0($t3)
    /* 1EE5E4 151C1134 C4640038 */  lwc1       $f4, 0x38($v1)
    /* 1EE5E8 151C1138 00001025 */  or         $v0, $zero, $zero
    /* 1EE5EC 151C113C 4600218D */  trunc.w.s  $f6, $f4
    /* 1EE5F0 151C1140 44183000 */  mfc1       $t8, $f6
    /* 1EE5F4 151C1144 00000000 */  nop
    /* 1EE5F8 151C1148 A4980002 */  sh         $t8, 0x2($a0)
    /* 1EE5FC 151C114C C468003C */  lwc1       $f8, 0x3C($v1)
    /* 1EE600 151C1150 4600428D */  trunc.w.s  $f10, $f8
    /* 1EE604 151C1154 44085000 */  mfc1       $t0, $f10
    /* 1EE608 151C1158 00000000 */  nop
    /* 1EE60C 151C115C A4880004 */  sh         $t0, 0x4($a0)
    /* 1EE610 151C1160 C4700040 */  lwc1       $f16, 0x40($v1)
    /* 1EE614 151C1164 4600848D */  trunc.w.s  $f18, $f16
    /* 1EE618 151C1168 440A9000 */  mfc1       $t2, $f18
    /* 1EE61C 151C116C 03E00008 */  jr         $ra
    /* 1EE620 151C1170 A48A0006 */   sh        $t2, 0x6($a0)
    /* 1EE624 151C1174 A5600000 */  sh         $zero, 0x0($t3)
  .L151C1178:
    /* 1EE628 151C1178 03E00008 */  jr         $ra
    /* 1EE62C 151C117C 00000000 */   nop
endlabel func_151C110C
