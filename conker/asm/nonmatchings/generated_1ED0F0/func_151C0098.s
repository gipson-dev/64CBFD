glabel func_151C0098
    /* 1ED548 151C0098 27BDFF40 */  addiu      $sp, $sp, -0xC0
    /* 1ED54C 151C009C AFB20020 */  sw         $s2, 0x20($sp)
    /* 1ED550 151C00A0 AFB1001C */  sw         $s1, 0x1C($sp)
    /* 1ED554 151C00A4 AFB00018 */  sw         $s0, 0x18($sp)
    /* 1ED558 151C00A8 00808025 */  or         $s0, $a0, $zero
    /* 1ED55C 151C00AC 30F100FF */  andi       $s1, $a3, 0xFF
    /* 1ED560 151C00B0 8FB200D0 */  lw         $s2, 0xD0($sp)
    /* 1ED564 151C00B4 AFBF0024 */  sw         $ra, 0x24($sp)
    /* 1ED568 151C00B8 AFA500C4 */  sw         $a1, 0xC4($sp)
    /* 1ED56C 151C00BC AFA600C8 */  sw         $a2, 0xC8($sp)
    /* 1ED570 151C00C0 AFA700CC */  sw         $a3, 0xCC($sp)
    /* 1ED574 151C00C4 02002025 */  or         $a0, $s0, $zero
    /* 1ED578 151C00C8 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED57C 151C00CC 0D470106 */  jal        func_151C0418
    /* 1ED580 151C00D0 02403025 */   or        $a2, $s2, $zero
    /* 1ED584 151C00D4 02002025 */  or         $a0, $s0, $zero
    /* 1ED588 151C00D8 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED58C 151C00DC 0D47013E */  jal        func_151C04F8
    /* 1ED590 151C00E0 02403025 */   or        $a2, $s2, $zero
    /* 1ED594 151C00E4 02002025 */  or         $a0, $s0, $zero
    /* 1ED598 151C00E8 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED59C 151C00EC 0D470169 */  jal        func_151C05A4
    /* 1ED5A0 151C00F0 02403025 */   or        $a2, $s2, $zero
    /* 1ED5A4 151C00F4 02002025 */  or         $a0, $s0, $zero
    /* 1ED5A8 151C00F8 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED5AC 151C00FC 0D47017C */  jal        func_151C05F0
    /* 1ED5B0 151C0100 02403025 */   or        $a2, $s2, $zero
    /* 1ED5B4 151C0104 93AE00CB */  lbu        $t6, 0xCB($sp)
    /* 1ED5B8 151C0108 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 1ED5BC 151C010C 2418FFC0 */  addiu      $t8, $zero, -0x40
    /* 1ED5C0 151C0110 11C00043 */  beqz       $t6, .L151C0220
    /* 1ED5C4 151C0114 24190047 */   addiu     $t9, $zero, 0x47
    /* 1ED5C8 151C0118 24080006 */  addiu      $t0, $zero, 0x6
    /* 1ED5CC 151C011C 24090004 */  addiu      $t1, $zero, 0x4
    /* 1ED5D0 151C0120 A7A00064 */  sh         $zero, 0x64($sp)
    /* 1ED5D4 151C0124 A7AF0066 */  sh         $t7, 0x66($sp)
    /* 1ED5D8 151C0128 A7B80068 */  sh         $t8, 0x68($sp)
    /* 1ED5DC 151C012C A7B9006A */  sh         $t9, 0x6A($sp)
    /* 1ED5E0 151C0130 AFA8006C */  sw         $t0, 0x6C($sp)
    /* 1ED5E4 151C0134 AFA90070 */  sw         $t1, 0x70($sp)
    /* 1ED5E8 151C0138 8E010000 */  lw         $at, 0x0($s0)
    /* 1ED5EC 151C013C 27AA0074 */  addiu      $t2, $sp, 0x74
    /* 1ED5F0 151C0140 240E0007 */  addiu      $t6, $zero, 0x7
    /* 1ED5F4 151C0144 AD410000 */  sw         $at, 0x0($t2)
    /* 1ED5F8 151C0148 8E0D0004 */  lw         $t5, 0x4($s0)
    /* 1ED5FC 151C014C 240F0003 */  addiu      $t7, $zero, 0x3
    /* 1ED600 151C0150 24180019 */  addiu      $t8, $zero, 0x19
    /* 1ED604 151C0154 AD4D0004 */  sw         $t5, 0x4($t2)
    /* 1ED608 151C0158 8E010008 */  lw         $at, 0x8($s0)
    /* 1ED60C 151C015C 2419000F */  addiu      $t9, $zero, 0xF
    /* 1ED610 151C0160 24080064 */  addiu      $t0, $zero, 0x64
    /* 1ED614 151C0164 AD410008 */  sw         $at, 0x8($t2)
    /* 1ED618 151C0168 3C0141B8 */  lui        $at, (0x41B80000 >> 16)
    /* 1ED61C 151C016C 44812000 */  mtc1       $at, $f4
    /* 1ED620 151C0170 3C0141F0 */  lui        $at, (0x41F00000 >> 16)
    /* 1ED624 151C0174 44813000 */  mtc1       $at, $f6
    /* 1ED628 151C0178 3C014234 */  lui        $at, (0x42340000 >> 16)
    /* 1ED62C 151C017C 44814000 */  mtc1       $at, $f8
    /* 1ED630 151C0180 3C014254 */  lui        $at, (0x42540000 >> 16)
    /* 1ED634 151C0184 44815000 */  mtc1       $at, $f10
    /* 1ED638 151C0188 3C01434B */  lui        $at, (0x434B0000 >> 16)
    /* 1ED63C 151C018C 44818000 */  mtc1       $at, $f16
    /* 1ED640 151C0190 3C0143CF */  lui        $at, (0x43CF0000 >> 16)
    /* 1ED644 151C0194 44819000 */  mtc1       $at, $f18
    /* 1ED648 151C0198 3C014170 */  lui        $at, (0x41700000 >> 16)
    /* 1ED64C 151C019C E7A40080 */  swc1       $f4, 0x80($sp)
    /* 1ED650 151C01A0 44812000 */  mtc1       $at, $f4
    /* 1ED654 151C01A4 3C01800B */  lui        $at, %hi(D_800AA990)
    /* 1ED658 151C01A8 E7A60084 */  swc1       $f6, 0x84($sp)
    /* 1ED65C 151C01AC C426A990 */  lwc1       $f6, %lo(D_800AA990)($at)
    /* 1ED660 151C01B0 3C01800B */  lui        $at, %hi(D_800AA994)
    /* 1ED664 151C01B4 E7A80088 */  swc1       $f8, 0x88($sp)
    /* 1ED668 151C01B8 C428A994 */  lwc1       $f8, %lo(D_800AA994)($at)
    /* 1ED66C 151C01BC 3C01800B */  lui        $at, %hi(D_800AA998)
    /* 1ED670 151C01C0 E7AA008C */  swc1       $f10, 0x8C($sp)
    /* 1ED674 151C01C4 C42AA998 */  lwc1       $f10, %lo(D_800AA998)($at)
    /* 1ED678 151C01C8 24090064 */  addiu      $t1, $zero, 0x64
    /* 1ED67C 151C01CC 240C000C */  addiu      $t4, $zero, 0xC
    /* 1ED680 151C01D0 240B0014 */  addiu      $t3, $zero, 0x14
    /* 1ED684 151C01D4 AFAE0098 */  sw         $t6, 0x98($sp)
    /* 1ED688 151C01D8 AFAF009C */  sw         $t7, 0x9C($sp)
    /* 1ED68C 151C01DC A7B800B0 */  sh         $t8, 0xB0($sp)
    /* 1ED690 151C01E0 A7B900B2 */  sh         $t9, 0xB2($sp)
    /* 1ED694 151C01E4 A7A800B4 */  sh         $t0, 0xB4($sp)
    /* 1ED698 151C01E8 A7A900B6 */  sh         $t1, 0xB6($sp)
    /* 1ED69C 151C01EC A7AC00B8 */  sh         $t4, 0xB8($sp)
    /* 1ED6A0 151C01F0 A7AB00BA */  sh         $t3, 0xBA($sp)
    /* 1ED6A4 151C01F4 A3A000BC */  sb         $zero, 0xBC($sp)
    /* 1ED6A8 151C01F8 27A40064 */  addiu      $a0, $sp, 0x64
    /* 1ED6AC 151C01FC 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED6B0 151C0200 02403025 */  or         $a2, $s2, $zero
    /* 1ED6B4 151C0204 E7B00090 */  swc1       $f16, 0x90($sp)
    /* 1ED6B8 151C0208 E7B20094 */  swc1       $f18, 0x94($sp)
    /* 1ED6BC 151C020C E7A400A0 */  swc1       $f4, 0xA0($sp)
    /* 1ED6C0 151C0210 E7A600A4 */  swc1       $f6, 0xA4($sp)
    /* 1ED6C4 151C0214 E7A800A8 */  swc1       $f8, 0xA8($sp)
    /* 1ED6C8 151C0218 0D453F3A */  jal        func_1514FCE8
    /* 1ED6CC 151C021C E7AA00AC */   swc1      $f10, 0xAC($sp)
  .L151C0220:
    /* 1ED6D0 151C0220 93AA00CB */  lbu        $t2, 0xCB($sp)
    /* 1ED6D4 151C0224 8FA500C4 */  lw         $a1, 0xC4($sp)
    /* 1ED6D8 151C0228 51400029 */  beql       $t2, $zero, .L151C02D0
    /* 1ED6DC 151C022C 8FBF0024 */   lw        $ra, 0x24($sp)
    /* 1ED6E0 151C0230 50A00027 */  beql       $a1, $zero, .L151C02D0
    /* 1ED6E4 151C0234 8FBF0024 */   lw        $ra, 0x24($sp)
    /* 1ED6E8 151C0238 C6100000 */  lwc1       $f16, 0x0($s0)
    /* 1ED6EC 151C023C 3C0142C8 */  lui        $at, (0x42C80000 >> 16)
    /* 1ED6F0 151C0240 44812000 */  mtc1       $at, $f4
    /* 1ED6F4 151C0244 E7B00058 */  swc1       $f16, 0x58($sp)
    /* 1ED6F8 151C0248 C6120004 */  lwc1       $f18, 0x4($s0)
    /* 1ED6FC 151C024C 27A40034 */  addiu      $a0, $sp, 0x34
    /* 1ED700 151C0250 46049180 */  add.s      $f6, $f18, $f4
    /* 1ED704 151C0254 E7A6005C */  swc1       $f6, 0x5C($sp)
    /* 1ED708 151C0258 C6080008 */  lwc1       $f8, 0x8($s0)
    /* 1ED70C 151C025C 0D411C57 */  jal        func_1504715C
    /* 1ED710 151C0260 E7A80060 */   swc1      $f8, 0x60($sp)
    /* 1ED714 151C0264 3C01447A */  lui        $at, (0x447A0000 >> 16)
    /* 1ED718 151C0268 44818000 */  mtc1       $at, $f16
    /* 1ED71C 151C026C C60A0004 */  lwc1       $f10, 0x4($s0)
    /* 1ED720 151C0270 27A40058 */  addiu      $a0, $sp, 0x58
    /* 1ED724 151C0274 00002825 */  or         $a1, $zero, $zero
    /* 1ED728 151C0278 46105481 */  sub.s      $f18, $f10, $f16
    /* 1ED72C 151C027C 27A70034 */  addiu      $a3, $sp, 0x34
    /* 1ED730 151C0280 44069000 */  mfc1       $a2, $f18
    /* 1ED734 151C0284 0D411B20 */  jal        func_15046C80
    /* 1ED738 151C0288 00000000 */   nop
    /* 1ED73C 151C028C 1040000F */  beqz       $v0, .L151C02CC
    /* 1ED740 151C0290 C7A40058 */   lwc1      $f4, 0x58($sp)
    /* 1ED744 151C0294 C7A60034 */  lwc1       $f6, 0x34($sp)
    /* 1ED748 151C0298 C7A80060 */  lwc1       $f8, 0x60($sp)
    /* 1ED74C 151C029C E7A40028 */  swc1       $f4, 0x28($sp)
    /* 1ED750 151C02A0 27A40038 */  addiu      $a0, $sp, 0x38
    /* 1ED754 151C02A4 27A50028 */  addiu      $a1, $sp, 0x28
    /* 1ED758 151C02A8 322600FF */  andi       $a2, $s1, 0xFF
    /* 1ED75C 151C02AC 02403825 */  or         $a3, $s2, $zero
    /* 1ED760 151C02B0 E7A6002C */  swc1       $f6, 0x2C($sp)
    /* 1ED764 151C02B4 0D4700D8 */  jal        func_151C0360
    /* 1ED768 151C02B8 E7A80030 */   swc1      $f8, 0x30($sp)
    /* 1ED76C 151C02BC 02002025 */  or         $a0, $s0, $zero
    /* 1ED770 151C02C0 322500FF */  andi       $a1, $s1, 0xFF
    /* 1ED774 151C02C4 0D470191 */  jal        func_151C0644
    /* 1ED778 151C02C8 02403025 */   or        $a2, $s2, $zero
  .L151C02CC:
    /* 1ED77C 151C02CC 8FBF0024 */  lw         $ra, 0x24($sp)
  .L151C02D0:
    /* 1ED780 151C02D0 8FB00018 */  lw         $s0, 0x18($sp)
    /* 1ED784 151C02D4 8FB1001C */  lw         $s1, 0x1C($sp)
    /* 1ED788 151C02D8 8FB20020 */  lw         $s2, 0x20($sp)
    /* 1ED78C 151C02DC 03E00008 */  jr         $ra
    /* 1ED790 151C02E0 27BD00C0 */   addiu     $sp, $sp, 0xC0
endlabel func_151C0098
