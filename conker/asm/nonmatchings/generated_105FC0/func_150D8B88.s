glabel func_150D8B88
    /* 106038 150D8B88 27BDFF38 */  addiu      $sp, $sp, -0xC8
    /* 10603C 150D8B8C AFB00038 */  sw         $s0, 0x38($sp)
    /* 106040 150D8B90 00808025 */  or         $s0, $a0, $zero
    /* 106044 150D8B94 AFBF003C */  sw         $ra, 0x3C($sp)
    /* 106048 150D8B98 8E0E031C */  lw         $t6, 0x31C($s0)
    /* 10604C 150D8B9C 3C0F800C */  lui        $t7, %hi(D_800BE9F0)
    /* 106050 150D8BA0 51C00074 */  beql       $t6, $zero, .L150D8D74
    /* 106054 150D8BA4 8FBF003C */   lw        $ra, 0x3C($sp)
    /* 106058 150D8BA8 8DEFE9F0 */  lw         $t7, %lo(D_800BE9F0)($t7)
    /* 10605C 150D8BAC 2401000A */  addiu      $at, $zero, 0xA
    /* 106060 150D8BB0 2404000A */  addiu      $a0, $zero, 0xA
    /* 106064 150D8BB4 15E10003 */  bne        $t7, $at, .L150D8BC4
    /* 106068 150D8BB8 24050037 */   addiu     $a1, $zero, 0x37
    /* 10606C 150D8BBC 0C00365B */  jal        func_1000D96C
    /* 106070 150D8BC0 00003025 */   or        $a2, $zero, $zero
  .L150D8BC4:
    /* 106074 150D8BC4 02002025 */  or         $a0, $s0, $zero
    /* 106078 150D8BC8 0D4362C4 */  jal        func_150D8B10
    /* 10607C 150D8BCC 27A500AC */   addiu     $a1, $sp, 0xAC
    /* 106080 150D8BD0 24180001 */  addiu      $t8, $zero, 0x1
    /* 106084 150D8BD4 A3A000A5 */  sb         $zero, 0xA5($sp)
    /* 106088 150D8BD8 A3B800A4 */  sb         $t8, 0xA4($sp)
    /* 10608C 150D8BDC AFB00058 */  sw         $s0, 0x58($sp)
    /* 106090 150D8BE0 9219003B */  lbu        $t9, 0x3B($s0)
    /* 106094 150D8BE4 27A800AC */  addiu      $t0, $sp, 0xAC
    /* 106098 150D8BE8 27A2004C */  addiu      $v0, $sp, 0x4C
    /* 10609C 150D8BEC A3B9005C */  sb         $t9, 0x5C($sp)
    /* 1060A0 150D8BF0 8D010000 */  lw         $at, 0x0($t0)
    /* 1060A4 150D8BF4 27AC0060 */  addiu      $t4, $sp, 0x60
    /* 1060A8 150D8BF8 27B8006C */  addiu      $t8, $sp, 0x6C
    /* 1060AC 150D8BFC AC410000 */  sw         $at, 0x0($v0)
    /* 1060B0 150D8C00 8D0B0004 */  lw         $t3, 0x4($t0)
    /* 1060B4 150D8C04 02002025 */  or         $a0, $s0, $zero
    /* 1060B8 150D8C08 27A50078 */  addiu      $a1, $sp, 0x78
    /* 1060BC 150D8C0C AC4B0004 */  sw         $t3, 0x4($v0)
    /* 1060C0 150D8C10 8D010008 */  lw         $at, 0x8($t0)
    /* 1060C4 150D8C14 AC410008 */  sw         $at, 0x8($v0)
    /* 1060C8 150D8C18 8C410000 */  lw         $at, 0x0($v0)
    /* 1060CC 150D8C1C AD810000 */  sw         $at, 0x0($t4)
    /* 1060D0 150D8C20 8C4F0004 */  lw         $t7, 0x4($v0)
    /* 1060D4 150D8C24 AD8F0004 */  sw         $t7, 0x4($t4)
    /* 1060D8 150D8C28 8C410008 */  lw         $at, 0x8($v0)
    /* 1060DC 150D8C2C AD810008 */  sw         $at, 0x8($t4)
    /* 1060E0 150D8C30 8C410000 */  lw         $at, 0x0($v0)
    /* 1060E4 150D8C34 AF010000 */  sw         $at, 0x0($t8)
    /* 1060E8 150D8C38 8C490004 */  lw         $t1, 0x4($v0)
    /* 1060EC 150D8C3C AF090004 */  sw         $t1, 0x4($t8)
    /* 1060F0 150D8C40 8C410008 */  lw         $at, 0x8($v0)
    /* 1060F4 150D8C44 0D4362CF */  jal        func_150D8B3C
    /* 1060F8 150D8C48 AF010008 */   sw        $at, 0x8($t8)
    /* 1060FC 150D8C4C 3C01800A */  lui        $at, %hi(D_800A0B48)
    /* 106100 150D8C50 C4240B48 */  lwc1       $f4, %lo(D_800A0B48)($at)
    /* 106104 150D8C54 0D47BD84 */  jal        func_151EF610
    /* 106108 150D8C58 E7A40094 */   swc1      $f4, 0x94($sp)
    /* 10610C 150D8C5C 04410004 */  bgez       $v0, .L150D8C70
    /* 106110 150D8C60 30440001 */   andi      $a0, $v0, 0x1
    /* 106114 150D8C64 10800002 */  beqz       $a0, .L150D8C70
    /* 106118 150D8C68 00000000 */   nop
    /* 10611C 150D8C6C 2484FFFE */  addiu      $a0, $a0, -0x2
  .L150D8C70:
    /* 106120 150D8C70 240801F4 */  addiu      $t0, $zero, 0x1F4
    /* 106124 150D8C74 240B1388 */  addiu      $t3, $zero, 0x1388
    /* 106128 150D8C78 AFAB0024 */  sw         $t3, 0x24($sp)
    /* 10612C 150D8C7C AFA80020 */  sw         $t0, 0x20($sp)
    /* 106130 150D8C80 248401B6 */  addiu      $a0, $a0, 0x1B6
    /* 106134 150D8C84 24057FFF */  addiu      $a1, $zero, 0x7FFF
    /* 106138 150D8C88 00003025 */  or         $a2, $zero, $zero
    /* 10613C 150D8C8C 00003825 */  or         $a3, $zero, $zero
    /* 106140 150D8C90 AFA00010 */  sw         $zero, 0x10($sp)
    /* 106144 150D8C94 AFA00014 */  sw         $zero, 0x14($sp)
    /* 106148 150D8C98 AFA00018 */  sw         $zero, 0x18($sp)
    /* 10614C 150D8C9C 0C0043E2 */  jal        func_10010F88
    /* 106150 150D8CA0 AFA0001C */   sw        $zero, 0x1C($sp)
    /* 106154 150D8CA4 44800000 */  mtc1       $zero, $f0
    /* 106158 150D8CA8 3C01C680 */  lui        $at, (0xC6800000 >> 16)
    /* 10615C 150D8CAC 44813000 */  mtc1       $at, $f6
    /* 106160 150D8CB0 A7A20088 */  sh         $v0, 0x88($sp)
    /* 106164 150D8CB4 E7A0008C */  swc1       $f0, 0x8C($sp)
    /* 106168 150D8CB8 E7A00084 */  swc1       $f0, 0x84($sp)
    /* 10616C 150D8CBC E7A00098 */  swc1       $f0, 0x98($sp)
    /* 106170 150D8CC0 E7A0009C */  swc1       $f0, 0x9C($sp)
    /* 106174 150D8CC4 E7A000A0 */  swc1       $f0, 0xA0($sp)
    /* 106178 150D8CC8 E7A60090 */  swc1       $f6, 0x90($sp)
    /* 10617C 150D8CCC 8E03031C */  lw         $v1, 0x31C($s0)
    /* 106180 150D8CD0 240F0032 */  addiu      $t7, $zero, 0x32
    /* 106184 150D8CD4 240A012C */  addiu      $t2, $zero, 0x12C
    /* 106188 150D8CD8 10600006 */  beqz       $v1, .L150D8CF4
    /* 10618C 150D8CDC 24190036 */   addiu     $t9, $zero, 0x36
    /* 106190 150D8CE0 906E0084 */  lbu        $t6, 0x84($v1)
    /* 106194 150D8CE4 93AD00A4 */  lbu        $t5, 0xA4($sp)
    /* 106198 150D8CE8 11C00002 */  beqz       $t6, .L150D8CF4
    /* 10619C 150D8CEC 31ACFFFE */   andi      $t4, $t5, 0xFFFE
    /* 1061A0 150D8CF0 A3AC00A4 */  sb         $t4, 0xA4($sp)
  .L150D8CF4:
    /* 1061A4 150D8CF4 A3AF00C1 */  sb         $t7, 0xC1($sp)
    /* 1061A8 150D8CF8 24180002 */  addiu      $t8, $zero, 0x2
    /* 1061AC 150D8CFC 24090005 */  addiu      $t1, $zero, 0x5
    /* 1061B0 150D8D00 240F0001 */  addiu      $t7, $zero, 0x1
    /* 1061B4 150D8D04 24080001 */  addiu      $t0, $zero, 0x1
    /* 1061B8 150D8D08 240B0011 */  addiu      $t3, $zero, 0x11
    /* 1061BC 150D8D0C 240E0003 */  addiu      $t6, $zero, 0x3
    /* 1061C0 150D8D10 240D00FF */  addiu      $t5, $zero, 0xFF
    /* 1061C4 150D8D14 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 1061C8 150D8D18 A7AA00B8 */  sh         $t2, 0xB8($sp)
    /* 1061CC 150D8D1C A7B900BA */  sh         $t9, 0xBA($sp)
    /* 1061D0 150D8D20 AFB800BC */  sw         $t8, 0xBC($sp)
    /* 1061D4 150D8D24 A3A900C0 */  sb         $t1, 0xC0($sp)
    /* 1061D8 150D8D28 AFA000C4 */  sw         $zero, 0xC4($sp)
    /* 1061DC 150D8D2C AFAC0024 */  sw         $t4, 0x24($sp)
    /* 1061E0 150D8D30 AFAD001C */  sw         $t5, 0x1C($sp)
    /* 1061E4 150D8D34 AFAE0018 */  sw         $t6, 0x18($sp)
    /* 1061E8 150D8D38 AFAB0014 */  sw         $t3, 0x14($sp)
    /* 1061EC 150D8D3C AFA80010 */  sw         $t0, 0x10($sp)
    /* 1061F0 150D8D40 AFAF0028 */  sw         $t7, 0x28($sp)
    /* 1061F4 150D8D44 27A400AC */  addiu      $a0, $sp, 0xAC
    /* 1061F8 150D8D48 24050050 */  addiu      $a1, $zero, 0x50
    /* 1061FC 150D8D4C 24060024 */  addiu      $a2, $zero, 0x24
    /* 106200 150D8D50 2407000E */  addiu      $a3, $zero, 0xE
    /* 106204 150D8D54 0D451EA0 */  jal        func_15147A80
    /* 106208 150D8D58 AFA00020 */   sw        $zero, 0x20($sp)
    /* 10620C 150D8D5C 10400004 */  beqz       $v0, .L150D8D70
    /* 106210 150D8D60 27A50058 */   addiu     $a1, $sp, 0x58
    /* 106214 150D8D64 8C440098 */  lw         $a0, 0x98($v0)
    /* 106218 150D8D68 0C008BB0 */  jal        memcpy
    /* 10621C 150D8D6C 24060050 */   addiu     $a2, $zero, 0x50
  .L150D8D70:
    /* 106220 150D8D70 8FBF003C */  lw         $ra, 0x3C($sp)
  .L150D8D74:
    /* 106224 150D8D74 8FB00038 */  lw         $s0, 0x38($sp)
    /* 106228 150D8D78 27BD00C8 */  addiu      $sp, $sp, 0xC8
    /* 10622C 150D8D7C 03E00008 */  jr         $ra
    /* 106230 150D8D80 00000000 */   nop
endlabel func_150D8B88
