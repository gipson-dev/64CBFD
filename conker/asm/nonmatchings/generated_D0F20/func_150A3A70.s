glabel func_150A3A70
    /* D0F20 150A3A70 3C08800E */  lui        $t0, %hi(D_800DBE62)
    /* D0F24 150A3A74 8108BE62 */  lb         $t0, %lo(D_800DBE62)($t0)
    /* D0F28 150A3A78 11000406 */  beqz       $t0, func_150A49F4+0xA0
    /* D0F2C 150A3A7C 00000000 */   nop
    /* D0F30 150A3A80 3C01800D */  lui        $at, %hi(D_800D3584)
    /* D0F34 150A3A84 AC203584 */  sw         $zero, %lo(D_800D3584)($at)
    /* D0F38 150A3A88 44900000 */  mtc1       $s0, $f0
    /* D0F3C 150A3A8C 00000000 */  nop
    /* D0F40 150A3A90 44910800 */  mtc1       $s1, $f1
    /* D0F44 150A3A94 00000000 */  nop
    /* D0F48 150A3A98 44921000 */  mtc1       $s2, $f2
    /* D0F4C 150A3A9C 00000000 */  nop
    /* D0F50 150A3AA0 44931800 */  mtc1       $s3, $f3
    /* D0F54 150A3AA4 00000000 */  nop
    /* D0F58 150A3AA8 44942000 */  mtc1       $s4, $f4
    /* D0F5C 150A3AAC 00000000 */  nop
    /* D0F60 150A3AB0 44952800 */  mtc1       $s5, $f5
    /* D0F64 150A3AB4 00000000 */  nop
    /* D0F68 150A3AB8 44963000 */  mtc1       $s6, $f6
    /* D0F6C 150A3ABC 00000000 */  nop
    /* D0F70 150A3AC0 44973800 */  mtc1       $s7, $f7
    /* D0F74 150A3AC4 00000000 */  nop
    /* D0F78 150A3AC8 449E4000 */  mtc1       $fp, $f8
    /* D0F7C 150A3ACC 00000000 */  nop
    /* D0F80 150A3AD0 449C4800 */  mtc1       $gp, $f9
    /* D0F84 150A3AD4 00000000 */  nop
    /* D0F88 150A3AD8 449F7800 */  mtc1       $ra, $f15
    /* D0F8C 150A3ADC 00000000 */  nop
    /* D0F90 150A3AE0 0000E025 */  or         $gp, $zero, $zero
    /* D0F94 150A3AE4 3C08800E */  lui        $t0, %hi(D_800DBE4C)
    /* D0F98 150A3AE8 8D08BE4C */  lw         $t0, %lo(D_800DBE4C)($t0)
    /* D0F9C 150A3AEC 3C1F150A */  lui        $ra, %hi(D_150A3B88)
    /* D0FA0 150A3AF0 27FF3B88 */  addiu      $ra, $ra, %lo(D_150A3B88)
    /* D0FA4 150A3AF4 3C0A800D */  lui        $t2, %hi(D_800D3300)
    /* D0FA8 150A3AF8 254A3300 */  addiu      $t2, $t2, %lo(D_800D3300)
    /* D0FAC 150A3AFC 3C0B800E */  lui        $t3, %hi(D_800DBE3C)
    /* D0FB0 150A3B00 8D6BBE3C */  lw         $t3, %lo(D_800DBE3C)($t3)
    /* D0FB4 150A3B04 3C0C800E */  lui        $t4, %hi(D_800DBE40)
    /* D0FB8 150A3B08 8D8CBE40 */  lw         $t4, %lo(D_800DBE40)($t4)
    /* D0FBC 150A3B0C 240D000C */  addiu      $t5, $zero, 0xC
    /* D0FC0 150A3B10 00001025 */  or         $v0, $zero, $zero
    /* D0FC4 150A3B14 3C18800E */  lui        $t8, %hi(D_800DBE48)
    /* D0FC8 150A3B18 8F18BE48 */  lw         $t8, %lo(D_800DBE48)($t8)
    /* D0FCC 150A3B1C 00004025 */  or         $t0, $zero, $zero
endlabel func_150A3A70
