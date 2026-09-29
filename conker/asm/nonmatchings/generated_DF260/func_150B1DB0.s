/* Handwritten function */
glabel func_150B1DB0
    /* DF260 150B1DB0 3C08A000 */  lui        $t0, %hi(D_A0000010)
    /* DF264 150B1DB4 01044025 */  or         $t0, $t0, $a0
    /* DF268 150B1DB8 3C09800A */  lui        $t1, %hi(D_8009F8D0)
    /* DF26C 150B1DBC DD29F8D0 */  ld         $t1, %lo(D_8009F8D0)($t1)
    /* DF270 150B1DC0 3C0E800A */  lui        $t6, %hi(D_8009F8D8)
    /* DF274 150B1DC4 DDCEF8D8 */  ld         $t6, %lo(D_8009F8D8)($t6)
  .L150B1DC8:
    /* DF278 150B1DC8 DC8A0000 */  ld         $t2, 0x0($a0)
    /* DF27C 150B1DCC DC8B0008 */  ld         $t3, 0x8($a0)
    /* DF280 150B1DD0 014E7824 */  and        $t7, $t2, $t6
    /* DF284 150B1DD4 01495024 */  and        $t2, $t2, $t1
    /* DF288 150B1DD8 000A6178 */  dsll       $t4, $t2, 5
    /* DF28C 150B1DDC 01EC6025 */  or         $t4, $t7, $t4
    /* DF290 150B1DE0 000A517A */  dsrl       $t2, $t2, 5
    /* DF294 150B1DE4 014C5025 */  or         $t2, $t2, $t4
    /* DF298 150B1DE8 FC8A0000 */  sd         $t2, 0x0($a0)
    /* DF29C 150B1DEC 016EC024 */  and        $t8, $t3, $t6
    /* DF2A0 150B1DF0 01695824 */  and        $t3, $t3, $t1
    /* DF2A4 150B1DF4 000B6978 */  dsll       $t5, $t3, 5
    /* DF2A8 150B1DF8 030D6825 */  or         $t5, $t8, $t5
    /* DF2AC 150B1DFC 000B597A */  dsrl       $t3, $t3, 5
    /* DF2B0 150B1E00 016D5825 */  or         $t3, $t3, $t5
    /* DF2B4 150B1E04 FC8B0008 */  sd         $t3, 0x8($a0)
    /* DF2B8 150B1E08 20840010 */  addi       $a0, $a0, 0x10 /* handwritten instruction */
    /* DF2BC 150B1E0C 0085082A */  slt        $at, $a0, $a1
    /* DF2C0 150B1E10 1420FFED */  bnez       $at, .L150B1DC8
    /* DF2C4 150B1E14 21080010 */   addi      $t0, $t0, %lo(D_A0000010) /* handwritten instruction */
    /* DF2C8 150B1E18 03E00008 */  jr         $ra
    /* DF2CC 150B1E1C 00000000 */   nop
endlabel func_150B1DB0
