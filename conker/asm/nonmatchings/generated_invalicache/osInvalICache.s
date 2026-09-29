glabel osInvalICache
    /* 22C90 10022C90 18A00011 */  blez       $a1, .L10022CD8
    /* 22C94 10022C94 00000000 */   nop
    /* 22C98 10022C98 240B4000 */  addiu      $t3, $zero, 0x4000
    /* 22C9C 10022C9C 00AB082B */  sltu       $at, $a1, $t3
    /* 22CA0 10022CA0 1020000F */  beqz       $at, .L10022CE0
    /* 22CA4 10022CA4 00000000 */   nop
    /* 22CA8 10022CA8 00804025 */  or         $t0, $a0, $zero
    /* 22CAC 10022CAC 00854821 */  addu       $t1, $a0, $a1
    /* 22CB0 10022CB0 0109082B */  sltu       $at, $t0, $t1
    /* 22CB4 10022CB4 10200008 */  beqz       $at, .L10022CD8
    /* 22CB8 10022CB8 00000000 */   nop
    /* 22CBC 10022CBC 310A001F */  andi       $t2, $t0, 0x1F
    /* 22CC0 10022CC0 2529FFE0 */  addiu      $t1, $t1, -0x20
    /* 22CC4 10022CC4 010A4023 */  subu       $t0, $t0, $t2
  .L10022CC8:
    /* 22CC8 10022CC8 BD100000 */  cache      0x10, 0x0($t0)
    /* 22CCC 10022CCC 0109082B */  sltu       $at, $t0, $t1
    /* 22CD0 10022CD0 1420FFFD */  bnez       $at, .L10022CC8
    /* 22CD4 10022CD4 25080020 */   addiu     $t0, $t0, 0x20
  .L10022CD8:
    /* 22CD8 10022CD8 03E00008 */  jr         $ra
    /* 22CDC 10022CDC 00000000 */   nop
  .L10022CE0:
    /* 22CE0 10022CE0 3C088000 */  lui        $t0, 0x8000
    /* 22CE4 10022CE4 010B4821 */  addu       $t1, $t0, $t3
    /* 22CE8 10022CE8 2529FFE0 */  addiu      $t1, $t1, -0x20
  .L10022CEC:
    /* 22CEC 10022CEC BD000000 */  cache      0x00, 0x0($t0)
    /* 22CF0 10022CF0 0109082B */  sltu       $at, $t0, $t1
    /* 22CF4 10022CF4 1420FFFD */  bnez       $at, .L10022CEC
    /* 22CF8 10022CF8 25080020 */   addiu     $t0, $t0, (0x80000020 & 0xFFFF)
    /* 22CFC 10022CFC 03E00008 */  jr         $ra
    /* 22D00 10022D00 00000000 */   nop
endlabel osInvalICache
    /* 22D04 10022D04 00000000 */  nop
    /* 22D08 10022D08 00000000 */  nop
    /* 22D0C 10022D0C 00000000 */  nop
