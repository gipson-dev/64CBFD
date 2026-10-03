glabel func_150A4FA0
    /* D2450 150A4FA0 44900000 */  mtc1       $s0, $f0
    /* D2454 150A4FA4 44910800 */  mtc1       $s1, $f1
    /* D2458 150A4FA8 44921000 */  mtc1       $s2, $f2
    /* D245C 150A4FAC 44931800 */  mtc1       $s3, $f3
    /* D2460 150A4FB0 44942000 */  mtc1       $s4, $f4
    /* D2464 150A4FB4 44952800 */  mtc1       $s5, $f5
    /* D2468 150A4FB8 44963000 */  mtc1       $s6, $f6
    /* D246C 150A4FBC 44973800 */  mtc1       $s7, $f7
    /* D2470 150A4FC0 449E4000 */  mtc1       $fp, $f8
    /* D2474 150A4FC4 449C4800 */  mtc1       $gp, $f9
    /* D2478 150A4FC8 449F7800 */  mtc1       $ra, $f15
    /* D247C 150A4FCC 3C1F150A */  lui        $ra, %hi(D_150A5070)
    /* D2480 150A4FD0 27FF5070 */  addiu      $ra, $ra, %lo(D_150A5070)
    /* D2484 150A4FD4 3C0A800D */  lui        $t2, %hi(D_800D3300)
    /* D2488 150A4FD8 254A3300 */  addiu      $t2, $t2, %lo(D_800D3300)
    /* D248C 150A4FDC 3C06800D */  lui        $a2, %hi(D_800CC2D0)
    /* D2490 150A4FE0 24C6C2D0 */  addiu      $a2, $a2, %lo(D_800CC2D0)
    /* D2494 150A4FE4 24C74F4C */  addiu      $a3, $a2, 0x4F4C
    /* D2498 150A4FE8 00001025 */  or         $v0, $zero, $zero
    /* D249C 150A4FEC 241CFFFF */  addiu      $gp, $zero, -0x1
    /* D24A0 150A4FF0 3C19800D */  lui        $t9, %hi(D_800D35DC)
    /* D24A4 150A4FF4 933935DC */  lbu        $t9, %lo(D_800D35DC)($t9)
    /* D24A8 150A4FF8 2739FFFF */  addiu      $t9, $t9, -0x1
    /* D24AC 150A4FFC 44998000 */  mtc1       $t9, $f16
  .L150A5000:
    /* D24B0 150A5000 279C0001 */  addiu      $gp, $gp, 0x1
    /* D24B4 150A5004 10E6001E */  beq        $a3, $a2, .L150A5080
    /* D24B8 150A5008 44198000 */   mfc1      $t9, $f16
    /* D24BC 150A500C 1399FFFC */  beq        $gp, $t9, .L150A5000
    /* D24C0 150A5010 24C6032C */   addiu     $a2, $a2, 0x32C
    /* D24C4 150A5014 8CD9FCD4 */  lw         $t9, -0x32C($a2)
    /* D24C8 150A5018 1320FFF9 */  beqz       $t9, .L150A5000
    /* D24CC 150A501C 00000000 */   nop
    /* D24D0 150A5020 8CD9FDCC */  lw         $t9, -0x234($a2)
    /* D24D4 150A5024 8CC8FF38 */  lw         $t0, -0xC8($a2)
    /* D24D8 150A5028 33394000 */  andi       $t9, $t9, 0x4000
    /* D24DC 150A502C 1320FFF4 */  beqz       $t9, .L150A5000
    /* D24E0 150A5030 8CCCFF3C */   lw        $t4, -0xC4($a2)
    /* D24E4 150A5034 90D8FCD8 */  lbu        $t8, -0x328($a2)
    /* D24E8 150A5038 1100FFF1 */  beqz       $t0, .L150A5000
    /* D24EC 150A503C 3C19800C */   lui       $t9, %hi(D_800C5918)
    /* D24F0 150A5040 27395918 */  addiu      $t9, $t9, %lo(D_800C5918)
    /* D24F4 150A5044 00184840 */  sll        $t1, $t8, 1
    /* D24F8 150A5048 01394821 */  addu       $t1, $t1, $t9
    /* D24FC 150A504C 95290000 */  lhu        $t1, 0x0($t1)
    /* D2500 150A5050 3C0B800C */  lui        $t3, %hi(D_800C6070)
    /* D2504 150A5054 256B6070 */  addiu      $t3, $t3, %lo(D_800C6070)
    /* D2508 150A5058 0018C880 */  sll        $t9, $t8, 2
    /* D250C 150A505C 01795821 */  addu       $t3, $t3, $t9
    /* D2510 150A5060 8D6B0000 */  lw         $t3, 0x0($t3)
    /* D2514 150A5064 0000C025 */  or         $t8, $zero, $zero
    /* D2518 150A5068 1180FFE5 */  beqz       $t4, .L150A5000
    /* D251C 150A506C 00000000 */   nop
endlabel func_150A4FA0
