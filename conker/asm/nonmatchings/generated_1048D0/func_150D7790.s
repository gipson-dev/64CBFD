glabel func_150D7790
    /* 104C40 150D7790 27BDFFB0 */  addiu      $sp, $sp, -0x50
    /* 104C44 150D7794 AFBF0034 */  sw         $ra, 0x34($sp)
    /* 104C48 150D7798 AFA40050 */  sw         $a0, 0x50($sp)
    /* 104C4C 150D779C 8FAE0050 */  lw         $t6, 0x50($sp)
    /* 104C50 150D77A0 00004025 */  or         $t0, $zero, $zero
    /* 104C54 150D77A4 24010030 */  addiu      $at, $zero, 0x30
    /* 104C58 150D77A8 8DC2031C */  lw         $v0, 0x31C($t6)
    /* 104C5C 150D77AC 10400004 */  beqz       $v0, .L150D77C0
    /* 104C60 150D77B0 00000000 */   nop
    /* 104C64 150D77B4 804F01AE */  lb         $t7, 0x1AE($v0)
    /* 104C68 150D77B8 59E00058 */  blezl      $t7, .L150D791C
    /* 104C6C 150D77BC 8FBF0034 */   lw        $ra, 0x34($sp)
  .L150D77C0:
    /* 104C70 150D77C0 10A1000A */  beq        $a1, $at, .L150D77EC
    /* 104C74 150D77C4 24010031 */   addiu     $at, $zero, 0x31
    /* 104C78 150D77C8 10A10008 */  beq        $a1, $at, .L150D77EC
    /* 104C7C 150D77CC 24010032 */   addiu     $at, $zero, 0x32
    /* 104C80 150D77D0 10A10017 */  beq        $a1, $at, .L150D7830
    /* 104C84 150D77D4 8FAC0050 */   lw        $t4, 0x50($sp)
    /* 104C88 150D77D8 24010033 */  addiu      $at, $zero, 0x33
    /* 104C8C 150D77DC 10A10014 */  beq        $a1, $at, .L150D7830
    /* 104C90 150D77E0 24080001 */   addiu     $t0, $zero, 0x1
    /* 104C94 150D77E4 1000004D */  b          .L150D791C
    /* 104C98 150D77E8 8FBF0034 */   lw        $ra, 0x34($sp)
  .L150D77EC:
    /* 104C9C 150D77EC 1040004A */  beqz       $v0, .L150D7918
    /* 104CA0 150D77F0 24180078 */   addiu     $t8, $zero, 0x78
    /* 104CA4 150D77F4 A458012C */  sh         $t8, 0x12C($v0)
    /* 104CA8 150D77F8 8FB90050 */  lw         $t9, 0x50($sp)
    /* 104CAC 150D77FC 240B03E8 */  addiu      $t3, $zero, 0x3E8
    /* 104CB0 150D7800 24040628 */  addiu      $a0, $zero, 0x628
    /* 104CB4 150D7804 8F22031C */  lw         $v0, 0x31C($t9)
    /* 104CB8 150D7808 24067FFF */  addiu      $a2, $zero, 0x7FFF
    /* 104CBC 150D780C 240701F4 */  addiu      $a3, $zero, 0x1F4
    /* 104CC0 150D7810 804901AE */  lb         $t1, 0x1AE($v0)
    /* 104CC4 150D7814 252AFFFF */  addiu      $t2, $t1, -0x1
    /* 104CC8 150D7818 A04A01AE */  sb         $t2, 0x1AE($v0)
    /* 104CCC 150D781C AFAB0010 */  sw         $t3, 0x10($sp)
    /* 104CD0 150D7820 0C004055 */  jal        func_10010154
    /* 104CD4 150D7824 8FA50050 */   lw        $a1, 0x50($sp)
    /* 104CD8 150D7828 1000003C */  b          .L150D791C
    /* 104CDC 150D782C 8FBF0034 */   lw        $ra, 0x34($sp)
  .L150D7830:
    /* 104CE0 150D7830 C58C0040 */  lwc1       $f12, 0x40($t4)
    /* 104CE4 150D7834 44800000 */  mtc1       $zero, $f0
    /* 104CE8 150D7838 3C01439B */  lui        $at, (0x439B0000 >> 16)
    /* 104CEC 150D783C 44817000 */  mtc1       $at, $f14
    /* 104CF0 150D7840 00081900 */  sll        $v1, $t0, 4
    /* 104CF4 150D7844 00681823 */  subu       $v1, $v1, $t0
    /* 104CF8 150D7848 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 104CFC 150D784C 44812000 */  mtc1       $at, $f4
    /* 104D00 150D7850 00031840 */  sll        $v1, $v1, 1
    /* 104D04 150D7854 2463001E */  addiu      $v1, $v1, 0x1E
    /* 104D08 150D7858 240D000D */  addiu      $t5, $zero, 0xD
    /* 104D0C 150D785C 240E0001 */  addiu      $t6, $zero, 0x1
    /* 104D10 150D7860 2D0F0001 */  sltiu      $t7, $t0, 0x1
    /* 104D14 150D7864 44060000 */  mfc1       $a2, $f0
    /* 104D18 150D7868 44070000 */  mfc1       $a3, $f0
    /* 104D1C 150D786C AFAF0028 */  sw         $t7, 0x28($sp)
    /* 104D20 150D7870 AFAE0024 */  sw         $t6, 0x24($sp)
    /* 104D24 150D7874 AFAD0014 */  sw         $t5, 0x14($sp)
    /* 104D28 150D7878 AFA30010 */  sw         $v1, 0x10($sp)
    /* 104D2C 150D787C AFA30038 */  sw         $v1, 0x38($sp)
    /* 104D30 150D7880 AFA00020 */  sw         $zero, 0x20($sp)
    /* 104D34 150D7884 E7A00018 */  swc1       $f0, 0x18($sp)
    /* 104D38 150D7888 0D41B118 */  jal        func_1506C460
    /* 104D3C 150D788C E7A4001C */   swc1      $f4, 0x1C($sp)
    /* 104D40 150D7890 8FA30038 */  lw         $v1, 0x38($sp)
    /* 104D44 150D7894 10400005 */  beqz       $v0, .L150D78AC
    /* 104D48 150D7898 00402825 */   or        $a1, $v0, $zero
    /* 104D4C 150D789C 3C18800C */  lui        $t8, %hi(D_800C3E78)
    /* 104D50 150D78A0 93183E78 */  lbu        $t8, %lo(D_800C3E78)($t8)
    /* 104D54 150D78A4 27190001 */  addiu      $t9, $t8, 0x1
    /* 104D58 150D78A8 A0590124 */  sb         $t9, 0x124($v0)
  .L150D78AC:
    /* 104D5C 150D78AC 10400013 */  beqz       $v0, .L150D78FC
    /* 104D60 150D78B0 2401001E */   addiu     $at, $zero, 0x1E
    /* 104D64 150D78B4 10610011 */  beq        $v1, $at, .L150D78FC
    /* 104D68 150D78B8 2409FFFF */   addiu     $t1, $zero, -0x1
    /* 104D6C 150D78BC A0A90221 */  sb         $t1, 0x221($a1)
    /* 104D70 150D78C0 AFA50040 */  sw         $a1, 0x40($sp)
    /* 104D74 150D78C4 0D422157 */  jal        func_1508855C
    /* 104D78 150D78C8 8FA40050 */   lw        $a0, 0x50($sp)
    /* 104D7C 150D78CC 2401FFFF */  addiu      $at, $zero, -0x1
    /* 104D80 150D78D0 1041000A */  beq        $v0, $at, .L150D78FC
    /* 104D84 150D78D4 8FA50040 */   lw        $a1, 0x40($sp)
    /* 104D88 150D78D8 00A02025 */  or         $a0, $a1, $zero
    /* 104D8C 150D78DC 0D4221A3 */  jal        func_1508868C
    /* 104D90 150D78E0 AFA20048 */   sw        $v0, 0x48($sp)
    /* 104D94 150D78E4 2401FFFF */  addiu      $at, $zero, -0x1
    /* 104D98 150D78E8 8FA60048 */  lw         $a2, 0x48($sp)
    /* 104D9C 150D78EC 10410003 */  beq        $v0, $at, .L150D78FC
    /* 104DA0 150D78F0 00402825 */   or        $a1, $v0, $zero
    /* 104DA4 150D78F4 0D42217B */  jal        func_150885EC
    /* 104DA8 150D78F8 00C02025 */   or        $a0, $a2, $zero
  .L150D78FC:
    /* 104DAC 150D78FC 8FAA0050 */  lw         $t2, 0x50($sp)
    /* 104DB0 150D7900 8D42031C */  lw         $v0, 0x31C($t2)
    /* 104DB4 150D7904 50400005 */  beql       $v0, $zero, .L150D791C
    /* 104DB8 150D7908 8FBF0034 */   lw        $ra, 0x34($sp)
    /* 104DBC 150D790C 804B01AE */  lb         $t3, 0x1AE($v0)
    /* 104DC0 150D7910 256CFFFF */  addiu      $t4, $t3, -0x1
    /* 104DC4 150D7914 A04C01AE */  sb         $t4, 0x1AE($v0)
  .L150D7918:
    /* 104DC8 150D7918 8FBF0034 */  lw         $ra, 0x34($sp)
  .L150D791C:
    /* 104DCC 150D791C 27BD0050 */  addiu      $sp, $sp, 0x50
    /* 104DD0 150D7920 03E00008 */  jr         $ra
    /* 104DD4 150D7924 00000000 */   nop
endlabel func_150D7790
