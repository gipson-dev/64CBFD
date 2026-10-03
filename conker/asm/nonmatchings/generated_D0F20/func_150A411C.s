  glabel func_150A411C
    /* D15CC 150A411C 00AA082A */  slt        $at, $a1, $t2
    /* D15D0 150A4120 142000A3 */  bnez       $at, .L150A43B0
    /* D15D4 150A4124 00000000 */   nop
    /* D15D8 150A4128 03D5082A */  slt        $at, $fp, $s5
    /* D15DC 150A412C 1020000A */  beqz       $at, .L150A4158
    /* D15E0 150A4130 00000000 */   nop
    /* D15E4 150A4134 01606825 */  or         $t5, $t3, $zero
    /* D15E8 150A4138 02A07025 */  or         $t6, $s5, $zero
    /* D15EC 150A413C 01807825 */  or         $t7, $t4, $zero
    /* D15F0 150A4140 02C05825 */  or         $t3, $s6, $zero
    /* D15F4 150A4144 03C0A825 */  or         $s5, $fp, $zero
    /* D15F8 150A4148 02E06025 */  or         $t4, $s7, $zero
    /* D15FC 150A414C 01A0B025 */  or         $s6, $t5, $zero
    /* D1600 150A4150 01C0F025 */  or         $fp, $t6, $zero
    /* D1604 150A4154 01E0B825 */  or         $s7, $t7, $zero
  .L150A4158:
    /* D1608 150A4158 03C5082A */  slt        $at, $fp, $a1
    /* D160C 150A415C 14200094 */  bnez       $at, .L150A43B0
    /* D1610 150A4160 00000000 */   nop
    /* D1614 150A4164 03CA7022 */  sub        $t6, $fp, $t2 /* handwritten instruction */
    /* D1618 150A4168 25CE0001 */  addiu      $t6, $t6, 0x1
    /* D161C 150A416C 02C87822 */  sub        $t7, $s6, $t0 /* handwritten instruction */
    /* D1620 150A4170 000F7A00 */  sll        $t7, $t7, 8
    /* D1624 150A4174 01EE001A */  div        $zero, $t7, $t6
    /* D1628 150A4178 00AA6822 */  sub        $t5, $a1, $t2 /* handwritten instruction */
    /* D162C 150A417C 448D5000 */  mtc1       $t5, $f10
    /* D1630 150A4180 00000000 */  nop
    /* D1634 150A4184 448E5800 */  mtc1       $t6, $f11
    /* D1638 150A4188 00000000 */  nop
    /* D163C 150A418C 00007812 */  mflo       $t7
    /* D1640 150A4190 00000000 */  nop
    /* D1644 150A4194 00000000 */  nop
    /* D1648 150A4198 01AF0018 */  mult       $t5, $t7
    /* D164C 150A419C 00006812 */  mflo       $t5
    /* D1650 150A41A0 00000000 */  nop
    /* D1654 150A41A4 00000000 */  nop
    /* D1658 150A41A8 000D6A03 */  sra        $t5, $t5, 8
    /* D165C 150A41AC 03D57022 */  sub        $t6, $fp, $s5 /* handwritten instruction */
    /* D1660 150A41B0 01A8F021 */  addu       $fp, $t5, $t0
    /* D1664 150A41B4 00B56822 */  sub        $t5, $a1, $s5 /* handwritten instruction */
    /* D1668 150A41B8 448D7000 */  mtc1       $t5, $f14
    /* D166C 150A41BC 00000000 */  nop
    /* D1670 150A41C0 05A10005 */  bgez       $t5, .L150A41D8
    /* D1674 150A41C4 00000000 */   nop
    /* D1678 150A41C8 02AA7022 */  sub        $t6, $s5, $t2 /* handwritten instruction */
    /* D167C 150A41CC 00AA6822 */  sub        $t5, $a1, $t2 /* handwritten instruction */
    /* D1680 150A41D0 0160B025 */  or         $s6, $t3, $zero
    /* D1684 150A41D4 01005825 */  or         $t3, $t0, $zero
  .L150A41D8:
    /* D1688 150A41D8 25CE0001 */  addiu      $t6, $t6, 0x1
    /* D168C 150A41DC 02CB7822 */  sub        $t7, $s6, $t3 /* handwritten instruction */
    /* D1690 150A41E0 000F7A00 */  sll        $t7, $t7, 8
    /* D1694 150A41E4 01EE001A */  div        $zero, $t7, $t6
    /* D1698 150A41E8 448D6000 */  mtc1       $t5, $f12
    /* D169C 150A41EC 00000000 */  nop
    /* D16A0 150A41F0 448E6800 */  mtc1       $t6, $f13
    /* D16A4 150A41F4 00000000 */  nop
    /* D16A8 150A41F8 00007812 */  mflo       $t7
    /* D16AC 150A41FC 00000000 */  nop
    /* D16B0 150A4200 00000000 */  nop
    /* D16B4 150A4204 01AF0018 */  mult       $t5, $t7
    /* D16B8 150A4208 00006812 */  mflo       $t5
    /* D16BC 150A420C 00000000 */  nop
    /* D16C0 150A4210 00000000 */  nop
    /* D16C4 150A4214 000D6A03 */  sra        $t5, $t5, 8
    /* D16C8 150A4218 01ABB021 */  addu       $s6, $t5, $t3
    /* D16CC 150A421C 02C47022 */  sub        $t6, $s6, $a0 /* handwritten instruction */
    /* D16D0 150A4220 03C47822 */  sub        $t7, $fp, $a0 /* handwritten instruction */
    /* D16D4 150A4224 01CF082A */  slt        $at, $t6, $t7
    /* D16D8 150A4228 240DFFFF */  addiu      $t5, $zero, -0x1
    /* D16DC 150A422C 54200001 */  bnel       $at, $zero, .L150A4234
    /* D16E0 150A4230 240D0001 */   addiu     $t5, $zero, 0x1
  .L150A4234:
    /* D16E4 150A4234 01CD7023 */  subu       $t6, $t6, $t5
    /* D16E8 150A4238 01ED7821 */  addu       $t7, $t7, $t5
    /* D16EC 150A423C 01EE6826 */  xor        $t5, $t7, $t6
    /* D16F0 150A4240 05A1005B */  bgez       $t5, .L150A43B0
    /* D16F4 150A4244 00000000 */   nop
    /* D16F8 150A4248 0120C825 */  or         $t9, $t1, $zero
    /* D16FC 150A424C 032C082A */  slt        $at, $t9, $t4
    /* D1700 150A4250 10200002 */  beqz       $at, .L150A425C
    /* D1704 150A4254 00000000 */   nop
    /* D1708 150A4258 0180C825 */  or         $t9, $t4, $zero
  .L150A425C:
    /* D170C 150A425C 0337082A */  slt        $at, $t9, $s7
    /* D1710 150A4260 10200002 */  beqz       $at, .L150A426C
    /* D1714 150A4264 00000000 */   nop
    /* D1718 150A4268 02E0C825 */  or         $t9, $s7, $zero
  .L150A426C:
    /* D171C 150A426C 0019CA00 */  sll        $t9, $t9, 8
    /* D1720 150A4270 02E97822 */  sub        $t7, $s7, $t1 /* handwritten instruction */
    /* D1724 150A4274 440E5800 */  mfc1       $t6, $f11
    /* D1728 150A4278 00000000 */  nop
    /* D172C 150A427C 000F7A00 */  sll        $t7, $t7, 8
    /* D1730 150A4280 01EE001A */  div        $zero, $t7, $t6
    /* D1734 150A4284 440D5000 */  mfc1       $t5, $f10
    /* D1738 150A4288 00000000 */  nop
    /* D173C 150A428C 0120C025 */  or         $t8, $t1, $zero
    /* D1740 150A4290 0198082A */  slt        $at, $t4, $t8
    /* D1744 150A4294 10200002 */  beqz       $at, .L150A42A0
    /* D1748 150A4298 00000000 */   nop
    /* D174C 150A429C 0180C025 */  or         $t8, $t4, $zero
  .L150A42A0:
    /* D1750 150A42A0 00007812 */  mflo       $t7
    /* D1754 150A42A4 00000000 */  nop
    /* D1758 150A42A8 00000000 */  nop
    /* D175C 150A42AC 01AF0018 */  mult       $t5, $t7
    /* D1760 150A42B0 02F8082A */  slt        $at, $s7, $t8
    /* D1764 150A42B4 10200002 */  beqz       $at, .L150A42C0
    /* D1768 150A42B8 00000000 */   nop
    /* D176C 150A42BC 02E0C025 */  or         $t8, $s7, $zero
  .L150A42C0:
    /* D1770 150A42C0 00006812 */  mflo       $t5
    /* D1774 150A42C4 00000000 */  nop
    /* D1778 150A42C8 00000000 */  nop
    /* D177C 150A42CC 00095A00 */  sll        $t3, $t1, 8
    /* D1780 150A42D0 016D5821 */  addu       $t3, $t3, $t5
    /* D1784 150A42D4 440E7000 */  mfc1       $t6, $f14
    /* D1788 150A42D8 00000000 */  nop
    /* D178C 150A42DC 05C10003 */  bgez       $t6, .L150A42EC
    /* D1790 150A42E0 00000000 */   nop
    /* D1794 150A42E4 0180B825 */  or         $s7, $t4, $zero
    /* D1798 150A42E8 01206025 */  or         $t4, $t1, $zero
  .L150A42EC:
    /* D179C 150A42EC 02EC7822 */  sub        $t7, $s7, $t4 /* handwritten instruction */
    /* D17A0 150A42F0 440E6800 */  mfc1       $t6, $f13
    /* D17A4 150A42F4 00000000 */  nop
    /* D17A8 150A42F8 000F7A00 */  sll        $t7, $t7, 8
    /* D17AC 150A42FC 01EE001A */  div        $zero, $t7, $t6
    /* D17B0 150A4300 440D6000 */  mfc1       $t5, $f12
    /* D17B4 150A4304 00000000 */  nop
    /* D17B8 150A4308 00007812 */  mflo       $t7
    /* D17BC 150A430C 00000000 */  nop
    /* D17C0 150A4310 00000000 */  nop
    /* D17C4 150A4314 01AF0018 */  mult       $t5, $t7
    /* D17C8 150A4318 0018C200 */  sll        $t8, $t8, 8
    /* D17CC 150A431C 00006812 */  mflo       $t5
    /* D17D0 150A4320 00000000 */  nop
    /* D17D4 150A4324 00000000 */  nop
    /* D17D8 150A4328 000C6200 */  sll        $t4, $t4, 8
    /* D17DC 150A432C 01ACA821 */  addu       $s5, $t5, $t4
    /* D17E0 150A4330 03D6F022 */  sub        $fp, $fp, $s6 /* handwritten instruction */
    /* D17E4 150A4334 01755822 */  sub        $t3, $t3, $s5 /* handwritten instruction */
    /* D17E8 150A4338 000B5A00 */  sll        $t3, $t3, 8
    /* D17EC 150A433C 017E001A */  div        $zero, $t3, $fp
    /* D17F0 150A4340 00964022 */  sub        $t0, $a0, $s6 /* handwritten instruction */
    /* D17F4 150A4344 0000F012 */  mflo       $fp
    /* D17F8 150A4348 00000000 */  nop
    /* D17FC 150A434C 00000000 */  nop
    /* D1800 150A4350 011E0018 */  mult       $t0, $fp
    /* D1804 150A4354 00004012 */  mflo       $t0
    /* D1808 150A4358 00000000 */  nop
    /* D180C 150A435C 00000000 */  nop
    /* D1810 150A4360 00084203 */  sra        $t0, $t0, 8
    /* D1814 150A4364 02A81021 */  addu       $v0, $s5, $t0
    /* D1818 150A4368 0322082A */  slt        $at, $t9, $v0
    /* D181C 150A436C 10200002 */  beqz       $at, .L150A4378
    /* D1820 150A4370 00000000 */   nop
    /* D1824 150A4374 03201025 */  or         $v0, $t9, $zero
  .L150A4378:
    /* D1828 150A4378 0058082A */  slt        $at, $v0, $t8
    /* D182C 150A437C 10200002 */  beqz       $at, .L150A4388
    /* D1830 150A4380 00000000 */   nop
    /* D1834 150A4384 03001025 */  or         $v0, $t8, $zero
  .L150A4388:
    /* D1838 150A4388 44825800 */  mtc1       $v0, $f11
    /* D183C 150A438C 00000000 */  nop
    /* D1840 150A4390 46805AE0 */  cvt.s.w    $f11, $f11
    /* D1844 150A4394 3C013B80 */  lui        $at, (0x3B800000 >> 16)
    /* D1848 150A4398 44815000 */  mtc1       $at, $f10
    /* D184C 150A439C 00000000 */  nop
    /* D1850 150A43A0 460B5282 */  mul.s      $f10, $f10, $f11
    /* D1854 150A43A4 00000000 */  nop
    /* D1858 150A43A8 8FA20010 */  lw         $v0, 0x10($sp)
    /* D185C 150A43AC E44A0000 */  swc1       $f10, 0x0($v0)
  .L150A43B0:
    /* D1860 150A43B0 44150800 */  mfc1       $s5, $f1
    /* D1864 150A43B4 00000000 */  nop
    /* D1868 150A43B8 44161000 */  mfc1       $s6, $f2
    /* D186C 150A43BC 00000000 */  nop
    /* D1870 150A43C0 44171800 */  mfc1       $s7, $f3
    /* D1874 150A43C4 00000000 */  nop
    /* D1878 150A43C8 441E2000 */  mfc1       $fp, $f4
    /* D187C 150A43CC 00000000 */  nop
    /* D1880 150A43D0 03E00008 */  jr         $ra
    /* D1884 150A43D4 00000000 */   nop
  .L150A43D8:
    /* D1888 150A43D8 03E00008 */  jr         $ra
    /* D188C 150A43DC 00000000 */   nop

endlabel func_150A411C
