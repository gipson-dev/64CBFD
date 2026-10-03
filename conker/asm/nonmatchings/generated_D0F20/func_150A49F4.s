  glabel func_150A49F4
    /* D1EA4 150A49F4 00044080 */  sll        $t0, $a0, 2
    /* D1EA8 150A49F8 3C09800E */  lui        $t1, %hi(D_800DBDD8)
    /* D1EAC 150A49FC 2529BDD8 */  addiu      $t1, $t1, %lo(D_800DBDD8)
    /* D1EB0 150A4A00 01284821 */  addu       $t1, $t1, $t0
    /* D1EB4 150A4A04 8D2A0000 */  lw         $t2, 0x0($t1)
    /* D1EB8 150A4A08 3C0B800E */  lui        $t3, %hi(D_800DBE3C)
    /* D1EBC 150A4A0C 256BBE3C */  addiu      $t3, $t3, %lo(D_800DBE3C)
    /* D1EC0 150A4A10 AD6A0000 */  sw         $t2, 0x0($t3)
    /* D1EC4 150A4A14 3C09800E */  lui        $t1, %hi(D_800DBDE8)
    /* D1EC8 150A4A18 2529BDE8 */  addiu      $t1, $t1, %lo(D_800DBDE8)
    /* D1ECC 150A4A1C 01284821 */  addu       $t1, $t1, $t0
    /* D1ED0 150A4A20 8D2A0000 */  lw         $t2, 0x0($t1)
    /* D1ED4 150A4A24 3C0B800E */  lui        $t3, %hi(D_800DBE40)
    /* D1ED8 150A4A28 256BBE40 */  addiu      $t3, $t3, %lo(D_800DBE40)
    /* D1EDC 150A4A2C AD6A0000 */  sw         $t2, 0x0($t3)
    /* D1EE0 150A4A30 3C09800E */  lui        $t1, %hi(D_800DBDF8)
    /* D1EE4 150A4A34 2529BDF8 */  addiu      $t1, $t1, %lo(D_800DBDF8)
    /* D1EE8 150A4A38 01284821 */  addu       $t1, $t1, $t0
    /* D1EEC 150A4A3C 8D2A0000 */  lw         $t2, 0x0($t1)
    /* D1EF0 150A4A40 3C0B800E */  lui        $t3, %hi(D_800DBE44)
    /* D1EF4 150A4A44 256BBE44 */  addiu      $t3, $t3, %lo(D_800DBE44)
    /* D1EF8 150A4A48 AD6A0000 */  sw         $t2, 0x0($t3)
    /* D1EFC 150A4A4C 3C09800E */  lui        $t1, %hi(D_800DBE08)
    /* D1F00 150A4A50 2529BE08 */  addiu      $t1, $t1, %lo(D_800DBE08)
    /* D1F04 150A4A54 01284821 */  addu       $t1, $t1, $t0
    /* D1F08 150A4A58 8D2A0000 */  lw         $t2, 0x0($t1)
    /* D1F0C 150A4A5C 3C0B800E */  lui        $t3, %hi(D_800DBE48)
    /* D1F10 150A4A60 256BBE48 */  addiu      $t3, $t3, %lo(D_800DBE48)
    /* D1F14 150A4A64 AD6A0000 */  sw         $t2, 0x0($t3)
    /* D1F18 150A4A68 3C09800E */  lui        $t1, %hi(D_800DBE18)
    /* D1F1C 150A4A6C 2529BE18 */  addiu      $t1, $t1, %lo(D_800DBE18)
    /* D1F20 150A4A70 01284821 */  addu       $t1, $t1, $t0
    /* D1F24 150A4A74 8D2A0000 */  lw         $t2, 0x0($t1)
    /* D1F28 150A4A78 3C0B800E */  lui        $t3, %hi(D_800DBE4C)
    /* D1F2C 150A4A7C 256BBE4C */  addiu      $t3, $t3, %lo(D_800DBE4C)
    /* D1F30 150A4A80 AD6A0000 */  sw         $t2, 0x0($t3)
    /* D1F34 150A4A84 3C08800E */  lui        $t0, %hi(D_800DBE50)
    /* D1F38 150A4A88 2508BE50 */  addiu      $t0, $t0, %lo(D_800DBE50)
    /* D1F3C 150A4A8C 03E00008 */  jr         $ra
    /* D1F40 150A4A90 AD040000 */   sw        $a0, 0x0($t0)
  .L150A4A94:
    /* D1F44 150A4A94 44900000 */  mtc1       $s0, $f0
    /* D1F48 150A4A98 44910800 */  mtc1       $s1, $f1
    /* D1F4C 150A4A9C 44921000 */  mtc1       $s2, $f2
    /* D1F50 150A4AA0 44931800 */  mtc1       $s3, $f3
    /* D1F54 150A4AA4 44942000 */  mtc1       $s4, $f4
    /* D1F58 150A4AA8 44952800 */  mtc1       $s5, $f5
    /* D1F5C 150A4AAC 44963000 */  mtc1       $s6, $f6
    /* D1F60 150A4AB0 44973800 */  mtc1       $s7, $f7
    /* D1F64 150A4AB4 449E4000 */  mtc1       $fp, $f8
    /* D1F68 150A4AB8 449C4800 */  mtc1       $gp, $f9
    /* D1F6C 150A4ABC 449F7800 */  mtc1       $ra, $f15
    /* D1F70 150A4AC0 3C1F150A */  lui        $ra, %hi(D_150A4AF4)
    /* D1F74 150A4AC4 27FF4AF4 */  addiu      $ra, $ra, %lo(D_150A4AF4)
    /* D1F78 150A4AC8 3C0A800D */  lui        $t2, %hi(D_800D3300)
    /* D1F7C 150A4ACC 254A3300 */  addiu      $t2, $t2, %lo(D_800D3300)
    /* D1F80 150A4AD0 00001025 */  or         $v0, $zero, $zero
    /* D1F84 150A4AD4 3C0C800E */  lui        $t4, %hi(D_800DBE40)
    /* D1F88 150A4AD8 8D8CBE40 */  lw         $t4, %lo(D_800DBE40)($t4)
    /* D1F8C 150A4ADC 3C0B800E */  lui        $t3, %hi(D_800DBE3C)
    /* D1F90 150A4AE0 8D6BBE3C */  lw         $t3, %lo(D_800DBE3C)($t3)
    /* D1F94 150A4AE4 3C09800E */  lui        $t1, %hi(D_800DBE4C)
    /* D1F98 150A4AE8 8D29BE4C */  lw         $t1, %lo(D_800DBE4C)($t1)
    /* D1F9C 150A4AEC 0000C025 */  or         $t8, $zero, $zero
    /* D1FA0 150A4AF0 00004025 */  or         $t0, $zero, $zero
endlabel func_150A49F4
