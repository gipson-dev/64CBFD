glabel func_150D6730
    /* 103BE0 150D6730 27BDFEA8 */  addiu      $sp, $sp, -0x158
    /* 103BE4 150D6734 AFB40030 */  sw         $s4, 0x30($sp)
    /* 103BE8 150D6738 AFB3002C */  sw         $s3, 0x2C($sp)
    /* 103BEC 150D673C 30B300FF */  andi       $s3, $a1, 0xFF
    /* 103BF0 150D6740 00C0A025 */  or         $s4, $a2, $zero
    /* 103BF4 150D6744 AFBF0034 */  sw         $ra, 0x34($sp)
    /* 103BF8 150D6748 AFB20028 */  sw         $s2, 0x28($sp)
    /* 103BFC 150D674C AFB10024 */  sw         $s1, 0x24($sp)
    /* 103C00 150D6750 AFB00020 */  sw         $s0, 0x20($sp)
    /* 103C04 150D6754 AFA40158 */  sw         $a0, 0x158($sp)
    /* 103C08 150D6758 AFA5015C */  sw         $a1, 0x15C($sp)
    /* 103C0C 150D675C 0D42B688 */  jal        func_150ADA20
    /* 103C10 150D6760 00000000 */   nop
    /* 103C14 150D6764 2401000B */  addiu      $at, $zero, 0xB
    /* 103C18 150D6768 0041001B */  divu       $zero, $v0, $at
    /* 103C1C 150D676C 8FA40158 */  lw         $a0, 0x158($sp)
    /* 103C20 150D6770 3C01800A */  lui        $at, %hi(D_800A0ACC)
    /* 103C24 150D6774 240F006C */  addiu      $t7, $zero, 0x6C
    /* 103C28 150D6778 AFA400D8 */  sw         $a0, 0xD8($sp)
    /* 103C2C 150D677C 908E003B */  lbu        $t6, 0x3B($a0)
    /* 103C30 150D6780 C4240ACC */  lwc1       $f4, %lo(D_800A0ACC)($at)
    /* 103C34 150D6784 A3AF0101 */  sb         $t7, 0x101($sp)
    /* 103C38 150D6788 3C190020 */  lui        $t9, (0x200005 >> 16)
    /* 103C3C 150D678C A3AE00DC */  sb         $t6, 0xDC($sp)
    /* 103C40 150D6790 00009010 */  mfhi       $s2
    /* 103C44 150D6794 24185103 */  addiu      $t8, $zero, 0x5103
    /* 103C48 150D6798 37390005 */  ori        $t9, $t9, (0x200005 & 0xFFFF)
    /* 103C4C 150D679C 24080014 */  addiu      $t0, $zero, 0x14
    /* 103C50 150D67A0 24090014 */  addiu      $t1, $zero, 0x14
    /* 103C54 150D67A4 240A0014 */  addiu      $t2, $zero, 0x14
    /* 103C58 150D67A8 240B00FF */  addiu      $t3, $zero, 0xFF
    /* 103C5C 150D67AC 240C004B */  addiu      $t4, $zero, 0x4B
    /* 103C60 150D67B0 240D004B */  addiu      $t5, $zero, 0x4B
    /* 103C64 150D67B4 240E004B */  addiu      $t6, $zero, 0x4B
    /* 103C68 150D67B8 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 103C6C 150D67BC 2652000F */  addiu      $s2, $s2, 0xF
    /* 103C70 150D67C0 A7B800EC */  sh         $t8, 0xEC($sp)
    /* 103C74 150D67C4 AFB900E4 */  sw         $t9, 0xE4($sp)
    /* 103C78 150D67C8 AFA000E8 */  sw         $zero, 0xE8($sp)
    /* 103C7C 150D67CC AFA000F0 */  sw         $zero, 0xF0($sp)
    /* 103C80 150D67D0 AFA000F4 */  sw         $zero, 0xF4($sp)
    /* 103C84 150D67D4 A3A800FC */  sb         $t0, 0xFC($sp)
    /* 103C88 150D67D8 A3A900FD */  sb         $t1, 0xFD($sp)
    /* 103C8C 150D67DC A3AA00FE */  sb         $t2, 0xFE($sp)
    /* 103C90 150D67E0 A3AB00FB */  sb         $t3, 0xFB($sp)
    /* 103C94 150D67E4 A3AC00F8 */  sb         $t4, 0xF8($sp)
    /* 103C98 150D67E8 A3AD00F9 */  sb         $t5, 0xF9($sp)
    /* 103C9C 150D67EC A3AE00FA */  sb         $t6, 0xFA($sp)
    /* 103CA0 150D67F0 A3AF0100 */  sb         $t7, 0x100($sp)
    /* 103CA4 150D67F4 27A50114 */  addiu      $a1, $sp, 0x114
    /* 103CA8 150D67F8 0D435B26 */  jal        func_150D6C98
    /* 103CAC 150D67FC E7A400E0 */   swc1      $f4, 0xE0($sp)
    /* 103CB0 150D6800 44800000 */  mtc1       $zero, $f0
    /* 103CB4 150D6804 3C01800A */  lui        $at, %hi(D_800A0AD0)
    /* 103CB8 150D6808 C4260AD0 */  lwc1       $f6, %lo(D_800A0AD0)($at)
    /* 103CBC 150D680C 3C080084 */  lui        $t0, (0x84DE01 >> 16)
    /* 103CC0 150D6810 2418000F */  addiu      $t8, $zero, 0xF
    /* 103CC4 150D6814 24190011 */  addiu      $t9, $zero, 0x11
    /* 103CC8 150D6818 3508DE01 */  ori        $t0, $t0, (0x84DE01 & 0xFFFF)
    /* 103CCC 150D681C 24090008 */  addiu      $t1, $zero, 0x8
    /* 103CD0 150D6820 240A0006 */  addiu      $t2, $zero, 0x6
    /* 103CD4 150D6824 240B001E */  addiu      $t3, $zero, 0x1E
    /* 103CD8 150D6828 240CFFFF */  addiu      $t4, $zero, -0x1
    /* 103CDC 150D682C 240DFFFF */  addiu      $t5, $zero, -0x1
    /* 103CE0 150D6830 240E0008 */  addiu      $t6, $zero, 0x8
    /* 103CE4 150D6834 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 103CE8 150D6838 A7B80102 */  sh         $t8, 0x102($sp)
    /* 103CEC 150D683C A7B90104 */  sh         $t9, 0x104($sp)
    /* 103CF0 150D6840 AFA8013C */  sw         $t0, 0x13C($sp)
    /* 103CF4 150D6844 A3A90144 */  sb         $t1, 0x144($sp)
    /* 103CF8 150D6848 A3AA0145 */  sb         $t2, 0x145($sp)
    /* 103CFC 150D684C A3AB0146 */  sb         $t3, 0x146($sp)
    /* 103D00 150D6850 A3AC0147 */  sb         $t4, 0x147($sp)
    /* 103D04 150D6854 A3AD0148 */  sb         $t5, 0x148($sp)
    /* 103D08 150D6858 A3AE0149 */  sb         $t6, 0x149($sp)
    /* 103D0C 150D685C AFA00140 */  sw         $zero, 0x140($sp)
    /* 103D10 150D6860 A3AF014A */  sb         $t7, 0x14A($sp)
    /* 103D14 150D6864 E7A00120 */  swc1       $f0, 0x120($sp)
    /* 103D18 150D6868 E7A00124 */  swc1       $f0, 0x124($sp)
    /* 103D1C 150D686C E7A00128 */  swc1       $f0, 0x128($sp)
    /* 103D20 150D6870 E7A60108 */  swc1       $f6, 0x108($sp)
  .L150D6874:
    /* 103D24 150D6874 0D42B688 */  jal        func_150ADA20
    /* 103D28 150D6878 00000000 */   nop
    /* 103D2C 150D687C 2401009C */  addiu      $at, $zero, 0x9C
    /* 103D30 150D6880 0041001B */  divu       $zero, $v0, $at
    /* 103D34 150D6884 0000C010 */  mfhi       $t8
    /* 103D38 150D6888 27190064 */  addiu      $t9, $t8, 0x64
    /* 103D3C 150D688C 0D42B688 */  jal        func_150ADA20
    /* 103D40 150D6890 A3B900FF */   sb        $t9, 0xFF($sp)
    /* 103D44 150D6894 2401000E */  addiu      $at, $zero, 0xE
    /* 103D48 150D6898 0041001B */  divu       $zero, $v0, $at
    /* 103D4C 150D689C 00001810 */  mfhi       $v1
    /* 103D50 150D68A0 24690008 */  addiu      $t1, $v1, 0x8
    /* 103D54 150D68A4 A7A90106 */  sh         $t1, 0x106($sp)
    /* 103D58 150D68A8 0D42B69A */  jal        func_150ADA68
    /* 103D5C 150D68AC A7A900EE */   sh        $t1, 0xEE($sp)
    /* 103D60 150D68B0 3C01434F */  lui        $at, (0x434F0000 >> 16)
    /* 103D64 150D68B4 44814000 */  mtc1       $at, $f8
    /* 103D68 150D68B8 3C01436E */  lui        $at, (0x436E0000 >> 16)
    /* 103D6C 150D68BC 44818000 */  mtc1       $at, $f16
    /* 103D70 150D68C0 46080282 */  mul.s      $f10, $f0, $f8
    /* 103D74 150D68C4 46105080 */  add.s      $f2, $f10, $f16
    /* 103D78 150D68C8 E7A2010C */  swc1       $f2, 0x10C($sp)
    /* 103D7C 150D68CC 0D42B688 */  jal        func_150ADA20
    /* 103D80 150D68D0 E7A20110 */   swc1      $f2, 0x110($sp)
    /* 103D84 150D68D4 0D42B688 */  jal        func_150ADA20
    /* 103D88 150D68D8 00408825 */   or        $s1, $v0, $zero
    /* 103D8C 150D68DC 0D42B69A */  jal        func_150ADA68
    /* 103D90 150D68E0 00408025 */   or        $s0, $v0, $zero
    /* 103D94 150D68E4 24010024 */  addiu      $at, $zero, 0x24
    /* 103D98 150D68E8 0201001B */  divu       $zero, $s0, $at
    /* 103D9C 150D68EC 3C0141F0 */  lui        $at, (0x41F00000 >> 16)
    /* 103DA0 150D68F0 44819000 */  mtc1       $at, $f18
    /* 103DA4 150D68F4 3C0141C8 */  lui        $at, (0x41C80000 >> 16)
    /* 103DA8 150D68F8 44813000 */  mtc1       $at, $f6
    /* 103DAC 150D68FC 46120102 */  mul.s      $f4, $f0, $f18
    /* 103DB0 150D6900 00002810 */  mfhi       $a1
    /* 103DB4 150D6904 24A5FFE7 */  addiu      $a1, $a1, -0x19
    /* 103DB8 150D6908 322400FF */  andi       $a0, $s1, 0xFF
    /* 103DBC 150D690C 00045400 */  sll        $t2, $a0, 16
    /* 103DC0 150D6910 00056400 */  sll        $t4, $a1, 16
    /* 103DC4 150D6914 000C2C03 */  sra        $a1, $t4, 16
    /* 103DC8 150D6918 46062200 */  add.s      $f8, $f4, $f6
    /* 103DCC 150D691C 000A2403 */  sra        $a0, $t2, 16
    /* 103DD0 150D6920 27A7012C */  addiu      $a3, $sp, 0x12C
    /* 103DD4 150D6924 44064000 */  mfc1       $a2, $f8
    /* 103DD8 150D6928 0D450DE5 */  jal        func_15143794
    /* 103DDC 150D692C 00000000 */   nop
    /* 103DE0 150D6930 0D42B69A */  jal        func_150ADA68
    /* 103DE4 150D6934 00000000 */   nop
    /* 103DE8 150D6938 44805000 */  mtc1       $zero, $f10
    /* 103DEC 150D693C 8FAE013C */  lw         $t6, 0x13C($sp)
    /* 103DF0 150D6940 2401FF3F */  addiu      $at, $zero, -0xC1
    /* 103DF4 150D6944 460A0402 */  mul.s      $f16, $f0, $f10
    /* 103DF8 150D6948 01C17824 */  and        $t7, $t6, $at
    /* 103DFC 150D694C AFAF013C */  sw         $t7, 0x13C($sp)
    /* 103E00 150D6950 0D42B688 */  jal        func_150ADA20
    /* 103E04 150D6954 E7B00138 */   swc1      $f16, 0x138($sp)
    /* 103E08 150D6958 30580001 */  andi       $t8, $v0, 0x1
    /* 103E0C 150D695C 13000003 */  beqz       $t8, .L150D696C
    /* 103E10 150D6960 00008825 */   or        $s1, $zero, $zero
    /* 103E14 150D6964 10000001 */  b          .L150D696C
    /* 103E18 150D6968 24110080 */   addiu     $s1, $zero, 0x80
  .L150D696C:
    /* 103E1C 150D696C 0D42B688 */  jal        func_150ADA20
    /* 103E20 150D6970 00000000 */   nop
    /* 103E24 150D6974 30590001 */  andi       $t9, $v0, 0x1
    /* 103E28 150D6978 13200003 */  beqz       $t9, .L150D6988
    /* 103E2C 150D697C 8FA8013C */   lw        $t0, 0x13C($sp)
    /* 103E30 150D6980 10000002 */  b          .L150D698C
    /* 103E34 150D6984 24100040 */   addiu     $s0, $zero, 0x40
  .L150D6988:
    /* 103E38 150D6988 00008025 */  or         $s0, $zero, $zero
  .L150D698C:
    /* 103E3C 150D698C 02114825 */  or         $t1, $s0, $s1
    /* 103E40 150D6990 01095025 */  or         $t2, $t0, $t1
    /* 103E44 150D6994 AFAA013C */  sw         $t2, 0x13C($sp)
    /* 103E48 150D6998 27A400E4 */  addiu      $a0, $sp, 0xE4
    /* 103E4C 150D699C 24050001 */  addiu      $a1, $zero, 0x1
    /* 103E50 150D69A0 00003025 */  or         $a2, $zero, $zero
    /* 103E54 150D69A4 2407000C */  addiu      $a3, $zero, 0xC
    /* 103E58 150D69A8 AFB30010 */  sw         $s3, 0x10($sp)
    /* 103E5C 150D69AC 0D44C0A0 */  jal        func_15130280
    /* 103E60 150D69B0 AFB40014 */   sw        $s4, 0x14($sp)
    /* 103E64 150D69B4 10400004 */  beqz       $v0, .L150D69C8
    /* 103E68 150D69B8 244400A8 */   addiu     $a0, $v0, 0xA8
    /* 103E6C 150D69BC 27A500D8 */  addiu      $a1, $sp, 0xD8
    /* 103E70 150D69C0 0C008BB0 */  jal        memcpy
    /* 103E74 150D69C4 2406000C */   addiu     $a2, $zero, 0xC
  .L150D69C8:
    /* 103E78 150D69C8 2652FFFF */  addiu      $s2, $s2, -0x1
    /* 103E7C 150D69CC 1E40FFA9 */  bgtz       $s2, .L150D6874
    /* 103E80 150D69D0 00000000 */   nop
    /* 103E84 150D69D4 8FA20158 */  lw         $v0, 0x158($sp)
    /* 103E88 150D69D8 AFA20048 */  sw         $v0, 0x48($sp)
    /* 103E8C 150D69DC 3C01800A */  lui        $at, %hi(D_800A0AD4)
    /* 103E90 150D69E0 904B003B */  lbu        $t3, 0x3B($v0)
    /* 103E94 150D69E4 44809000 */  mtc1       $zero, $f18
    /* 103E98 150D69E8 C4240AD4 */  lwc1       $f4, %lo(D_800A0AD4)($at)
    /* 103E9C 150D69EC A3AB004C */  sb         $t3, 0x4C($sp)
    /* 103EA0 150D69F0 E7B20050 */  swc1       $f18, 0x50($sp)
    /* 103EA4 150D69F4 0D42B69A */  jal        func_150ADA68
    /* 103EA8 150D69F8 E7A40058 */   swc1      $f4, 0x58($sp)
    /* 103EAC 150D69FC 3C014040 */  lui        $at, (0x40400000 >> 16)
    /* 103EB0 150D6A00 44813000 */  mtc1       $at, $f6
    /* 103EB4 150D6A04 3C014110 */  lui        $at, (0x41100000 >> 16)
    /* 103EB8 150D6A08 44815000 */  mtc1       $at, $f10
    /* 103EBC 150D6A0C 46060202 */  mul.s      $f8, $f0, $f6
    /* 103EC0 150D6A10 460A4300 */  add.s      $f12, $f8, $f10
    /* 103EC4 150D6A14 0D42B69A */  jal        func_150ADA68
    /* 103EC8 150D6A18 E7AC0054 */   swc1      $f12, 0x54($sp)
    /* 103ECC 150D6A1C 3C0142A0 */  lui        $at, (0x42A00000 >> 16)
    /* 103ED0 150D6A20 44818000 */  mtc1       $at, $f16
    /* 103ED4 150D6A24 C7AC0054 */  lwc1       $f12, 0x54($sp)
    /* 103ED8 150D6A28 3C0142C8 */  lui        $at, (0x42C80000 >> 16)
    /* 103EDC 150D6A2C 46100482 */  mul.s      $f18, $f0, $f16
    /* 103EE0 150D6A30 44812000 */  mtc1       $at, $f4
    /* 103EE4 150D6A34 240D0001 */  addiu      $t5, $zero, 0x1
    /* 103EE8 150D6A38 460C6182 */  mul.s      $f6, $f12, $f12
    /* 103EEC 150D6A3C 3C180020 */  lui        $t8, (0x200005 >> 16)
    /* 103EF0 150D6A40 3C014F00 */  lui        $at, (0x4F000000 >> 16)
    /* 103EF4 150D6A44 240E0079 */  addiu      $t6, $zero, 0x79
    /* 103EF8 150D6A48 240F4403 */  addiu      $t7, $zero, 0x4403
    /* 103EFC 150D6A4C 46049080 */  add.s      $f2, $f18, $f4
    /* 103F00 150D6A50 37180005 */  ori        $t8, $t8, (0x200005 & 0xFFFF)
    /* 103F04 150D6A54 241900FF */  addiu      $t9, $zero, 0xFF
    /* 103F08 150D6A58 240800FF */  addiu      $t0, $zero, 0xFF
    /* 103F0C 150D6A5C 46061203 */  div.s      $f8, $f2, $f6
    /* 103F10 150D6A60 240900DF */  addiu      $t1, $zero, 0xDF
    /* 103F14 150D6A64 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 103F18 150D6A68 240B00FF */  addiu      $t3, $zero, 0xFF
    /* 103F1C 150D6A6C 27A50094 */  addiu      $a1, $sp, 0x94
    /* 103F20 150D6A70 444CF800 */  cfc1       $t4, $31
    /* 103F24 150D6A74 44CDF800 */  ctc1       $t5, $31
    /* 103F28 150D6A78 E7A80060 */  swc1       $f8, 0x60($sp)
    /* 103F2C 150D6A7C 460012A4 */  cvt.w.s    $f10, $f2
    /* 103F30 150D6A80 444DF800 */  cfc1       $t5, $31
    /* 103F34 150D6A84 00000000 */  nop
    /* 103F38 150D6A88 31AD0078 */  andi       $t5, $t5, 0x78
    /* 103F3C 150D6A8C 51A00013 */  beql       $t5, $zero, .L150D6ADC
    /* 103F40 150D6A90 440D5000 */   mfc1      $t5, $f10
    /* 103F44 150D6A94 44815000 */  mtc1       $at, $f10
    /* 103F48 150D6A98 240D0001 */  addiu      $t5, $zero, 0x1
    /* 103F4C 150D6A9C 460A1281 */  sub.s      $f10, $f2, $f10
    /* 103F50 150D6AA0 44CDF800 */  ctc1       $t5, $31
    /* 103F54 150D6AA4 00000000 */  nop
    /* 103F58 150D6AA8 460052A4 */  cvt.w.s    $f10, $f10
    /* 103F5C 150D6AAC 444DF800 */  cfc1       $t5, $31
    /* 103F60 150D6AB0 00000000 */  nop
    /* 103F64 150D6AB4 31AD0078 */  andi       $t5, $t5, 0x78
    /* 103F68 150D6AB8 15A00005 */  bnez       $t5, .L150D6AD0
    /* 103F6C 150D6ABC 00000000 */   nop
    /* 103F70 150D6AC0 440D5000 */  mfc1       $t5, $f10
    /* 103F74 150D6AC4 3C018000 */  lui        $at, (0x80000000 >> 16)
    /* 103F78 150D6AC8 10000007 */  b          .L150D6AE8
    /* 103F7C 150D6ACC 01A16825 */   or        $t5, $t5, $at
  .L150D6AD0:
    /* 103F80 150D6AD0 10000005 */  b          .L150D6AE8
    /* 103F84 150D6AD4 240DFFFF */   addiu     $t5, $zero, -0x1
    /* 103F88 150D6AD8 440D5000 */  mfc1       $t5, $f10
  .L150D6ADC:
    /* 103F8C 150D6ADC 00000000 */  nop
    /* 103F90 150D6AE0 05A0FFFB */  bltz       $t5, .L150D6AD0
    /* 103F94 150D6AE4 00000000 */   nop
  .L150D6AE8:
    /* 103F98 150D6AE8 44CCF800 */  ctc1       $t4, $31
    /* 103F9C 150D6AEC A3AD007F */  sb         $t5, 0x7F($sp)
    /* 103FA0 150D6AF0 A3AE0081 */  sb         $t6, 0x81($sp)
    /* 103FA4 150D6AF4 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 103FA8 150D6AF8 240D00FF */  addiu      $t5, $zero, 0xFF
    /* 103FAC 150D6AFC 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 103FB0 150D6B00 A7AF006C */  sh         $t7, 0x6C($sp)
    /* 103FB4 150D6B04 AFB80064 */  sw         $t8, 0x64($sp)
    /* 103FB8 150D6B08 AFA00068 */  sw         $zero, 0x68($sp)
    /* 103FBC 150D6B0C AFA00070 */  sw         $zero, 0x70($sp)
    /* 103FC0 150D6B10 AFA00074 */  sw         $zero, 0x74($sp)
    /* 103FC4 150D6B14 A3B9007C */  sb         $t9, 0x7C($sp)
    /* 103FC8 150D6B18 A3A8007D */  sb         $t0, 0x7D($sp)
    /* 103FCC 150D6B1C A3A9007E */  sb         $t1, 0x7E($sp)
    /* 103FD0 150D6B20 A3AA007B */  sb         $t2, 0x7B($sp)
    /* 103FD4 150D6B24 A3AB0078 */  sb         $t3, 0x78($sp)
    /* 103FD8 150D6B28 A3AC0079 */  sb         $t4, 0x79($sp)
    /* 103FDC 150D6B2C A3AD007A */  sb         $t5, 0x7A($sp)
    /* 103FE0 150D6B30 A3AE0080 */  sb         $t6, 0x80($sp)
    /* 103FE4 150D6B34 8FA40158 */  lw         $a0, 0x158($sp)
    /* 103FE8 150D6B38 0D435B26 */  jal        func_150D6C98
    /* 103FEC 150D6B3C E7A2005C */   swc1      $f2, 0x5C($sp)
    /* 103FF0 150D6B40 3C12800A */  lui        $s2, %hi(D_800A5480)
    /* 103FF4 150D6B44 26525480 */  addiu      $s2, $s2, %lo(D_800A5480)
    /* 103FF8 150D6B48 8E410000 */  lw         $at, 0x0($s2)
    /* 103FFC 150D6B4C 27AF00A0 */  addiu      $t7, $sp, 0xA0
    /* 104000 150D6B50 24090001 */  addiu      $t1, $zero, 0x1
    /* 104004 150D6B54 ADE10000 */  sw         $at, 0x0($t7)
    /* 104008 150D6B58 8E480004 */  lw         $t0, 0x4($s2)
    /* 10400C 150D6B5C 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 104010 150D6B60 240B0001 */  addiu      $t3, $zero, 0x1
    /* 104014 150D6B64 ADE80004 */  sw         $t0, 0x4($t7)
    /* 104018 150D6B68 8E410008 */  lw         $at, 0x8($s2)
    /* 10401C 150D6B6C ADE10008 */  sw         $at, 0x8($t7)
    /* 104020 150D6B70 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 104024 150D6B74 44818000 */  mtc1       $at, $f16
    /* 104028 150D6B78 A7A90082 */  sh         $t1, 0x82($sp)
    /* 10402C 150D6B7C A7AA0084 */  sh         $t2, 0x84($sp)
    /* 104030 150D6B80 A7AB0086 */  sh         $t3, 0x86($sp)
    /* 104034 150D6B84 0D42B688 */  jal        func_150ADA20
    /* 104038 150D6B88 E7B00088 */   swc1      $f16, 0x88($sp)
    /* 10403C 150D6B8C 304C0001 */  andi       $t4, $v0, 0x1
    /* 104040 150D6B90 11800003 */  beqz       $t4, .L150D6BA0
    /* 104044 150D6B94 00008825 */   or        $s1, $zero, $zero
    /* 104048 150D6B98 10000001 */  b          .L150D6BA0
    /* 10404C 150D6B9C 24110040 */   addiu     $s1, $zero, 0x40
  .L150D6BA0:
    /* 104050 150D6BA0 0D42B688 */  jal        func_150ADA20
    /* 104054 150D6BA4 00000000 */   nop
    /* 104058 150D6BA8 304D0001 */  andi       $t5, $v0, 0x1
    /* 10405C 150D6BAC 11A00003 */  beqz       $t5, .L150D6BBC
    /* 104060 150D6BB0 3C010004 */   lui       $at, (0x4C000 >> 16)
    /* 104064 150D6BB4 10000002 */  b          .L150D6BC0
    /* 104068 150D6BB8 24100080 */   addiu     $s0, $zero, 0x80
  .L150D6BBC:
    /* 10406C 150D6BBC 00008025 */  or         $s0, $zero, $zero
  .L150D6BC0:
    /* 104070 150D6BC0 3421C000 */  ori        $at, $at, (0x4C000 & 0xFFFF)
    /* 104074 150D6BC4 02017025 */  or         $t6, $s0, $at
    /* 104078 150D6BC8 8E410000 */  lw         $at, 0x0($s2)
    /* 10407C 150D6BCC 01D1C825 */  or         $t9, $t6, $s1
    /* 104080 150D6BD0 24180006 */  addiu      $t8, $zero, 0x6
    /* 104084 150D6BD4 240F0006 */  addiu      $t7, $zero, 0x6
    /* 104088 150D6BD8 2408001F */  addiu      $t0, $zero, 0x1F
    /* 10408C 150D6BDC 2409FFFF */  addiu      $t1, $zero, -0x1
    /* 104090 150D6BE0 240AFFFF */  addiu      $t2, $zero, -0x1
    /* 104094 150D6BE4 240B0009 */  addiu      $t3, $zero, 0x9
    /* 104098 150D6BE8 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 10409C 150D6BEC AFB900BC */  sw         $t9, 0xBC($sp)
    /* 1040A0 150D6BF0 A3B800C4 */  sb         $t8, 0xC4($sp)
    /* 1040A4 150D6BF4 A3AF00C5 */  sb         $t7, 0xC5($sp)
    /* 1040A8 150D6BF8 A3A800C6 */  sb         $t0, 0xC6($sp)
    /* 1040AC 150D6BFC A3A900C7 */  sb         $t1, 0xC7($sp)
    /* 1040B0 150D6C00 A3AA00C8 */  sb         $t2, 0xC8($sp)
    /* 1040B4 150D6C04 A3AB00C9 */  sb         $t3, 0xC9($sp)
    /* 1040B8 150D6C08 AFA000C0 */  sw         $zero, 0xC0($sp)
    /* 1040BC 150D6C0C A3AC00CA */  sb         $t4, 0xCA($sp)
    /* 1040C0 150D6C10 27AD00AC */  addiu      $t5, $sp, 0xAC
    /* 1040C4 150D6C14 ADA10000 */  sw         $at, 0x0($t5)
    /* 1040C8 150D6C18 8E580004 */  lw         $t8, 0x4($s2)
    /* 1040CC 150D6C1C 44809000 */  mtc1       $zero, $f18
    /* 1040D0 150D6C20 44802000 */  mtc1       $zero, $f4
    /* 1040D4 150D6C24 ADB80004 */  sw         $t8, 0x4($t5)
    /* 1040D8 150D6C28 8E410008 */  lw         $at, 0x8($s2)
    /* 1040DC 150D6C2C 44803000 */  mtc1       $zero, $f6
    /* 1040E0 150D6C30 240F012C */  addiu      $t7, $zero, 0x12C
    /* 1040E4 150D6C34 ADA10008 */  sw         $at, 0x8($t5)
    /* 1040E8 150D6C38 A7AF006E */  sh         $t7, 0x6E($sp)
    /* 1040EC 150D6C3C AFB40014 */  sw         $s4, 0x14($sp)
    /* 1040F0 150D6C40 AFB30010 */  sw         $s3, 0x10($sp)
    /* 1040F4 150D6C44 27A40064 */  addiu      $a0, $sp, 0x64
    /* 1040F8 150D6C48 24050001 */  addiu      $a1, $zero, 0x1
    /* 1040FC 150D6C4C 00003025 */  or         $a2, $zero, $zero
    /* 104100 150D6C50 2407001C */  addiu      $a3, $zero, 0x1C
    /* 104104 150D6C54 E7B20090 */  swc1       $f18, 0x90($sp)
    /* 104108 150D6C58 E7A4008C */  swc1       $f4, 0x8C($sp)
    /* 10410C 150D6C5C 0D44C0A0 */  jal        func_15130280
    /* 104110 150D6C60 E7A600B8 */   swc1      $f6, 0xB8($sp)
    /* 104114 150D6C64 10400004 */  beqz       $v0, .L150D6C78
    /* 104118 150D6C68 244400A8 */   addiu     $a0, $v0, 0xA8
    /* 10411C 150D6C6C 27A50048 */  addiu      $a1, $sp, 0x48
    /* 104120 150D6C70 0C008BB0 */  jal        memcpy
    /* 104124 150D6C74 2406001C */   addiu     $a2, $zero, 0x1C
  .L150D6C78:
    /* 104128 150D6C78 8FBF0034 */  lw         $ra, 0x34($sp)
    /* 10412C 150D6C7C 8FB00020 */  lw         $s0, 0x20($sp)
    /* 104130 150D6C80 8FB10024 */  lw         $s1, 0x24($sp)
    /* 104134 150D6C84 8FB20028 */  lw         $s2, 0x28($sp)
    /* 104138 150D6C88 8FB3002C */  lw         $s3, 0x2C($sp)
    /* 10413C 150D6C8C 8FB40030 */  lw         $s4, 0x30($sp)
    /* 104140 150D6C90 03E00008 */  jr         $ra
    /* 104144 150D6C94 27BD0158 */   addiu     $sp, $sp, 0x158
endlabel func_150D6730
