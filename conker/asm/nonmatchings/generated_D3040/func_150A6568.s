glabel func_150A6568
    /* D3A18 150A6568 00001025 */  or         $v0, $zero, $zero
    /* D3A1C 150A656C ACC00000 */  sw         $zero, 0x0($a2)
    /* D3A20 150A6570 3C0E800E */  lui        $t6, %hi(D_800DBEF0)
    /* D3A24 150A6574 8DCEBEF0 */  lw         $t6, %lo(D_800DBEF0)($t6)
    /* D3A28 150A6578 11C0FFD1 */  beqz       $t6, func_150A64B8+0x8
    /* D3A2C 150A657C 00000000 */   nop
    /* D3A30 150A6580 44900000 */  mtc1       $s0, $f0
    /* D3A34 150A6584 00000000 */  nop
    /* D3A38 150A6588 44910800 */  mtc1       $s1, $f1
    /* D3A3C 150A658C 00000000 */  nop
    /* D3A40 150A6590 44921000 */  mtc1       $s2, $f2
    /* D3A44 150A6594 00000000 */  nop
    /* D3A48 150A6598 44931800 */  mtc1       $s3, $f3
    /* D3A4C 150A659C 00000000 */  nop
    /* D3A50 150A65A0 44942000 */  mtc1       $s4, $f4
    /* D3A54 150A65A4 00000000 */  nop
    /* D3A58 150A65A8 44952800 */  mtc1       $s5, $f5
    /* D3A5C 150A65AC 00000000 */  nop
    /* D3A60 150A65B0 44963000 */  mtc1       $s6, $f6
    /* D3A64 150A65B4 00000000 */  nop
    /* D3A68 150A65B8 44973800 */  mtc1       $s7, $f7
    /* D3A6C 150A65BC 00000000 */  nop
    /* D3A70 150A65C0 449E4000 */  mtc1       $fp, $f8
    /* D3A74 150A65C4 00000000 */  nop
    /* D3A78 150A65C8 8FB50010 */  lw         $s5, 0x10($sp)
    /* D3A7C 150A65CC 8FB60014 */  lw         $s6, 0x14($sp)
    /* D3A80 150A65D0 24120060 */  addiu      $s2, $zero, 0x60
    /* D3A84 150A65D4 24130020 */  addiu      $s3, $zero, 0x20
    /* D3A88 150A65D8 3C19800D */  lui        $t9, %hi(D_800D37E0)
    /* D3A8C 150A65DC 273937E0 */  addiu      $t9, $t9, %lo(D_800D37E0)
    /* D3A90 150A65E0 3C03800D */  lui        $v1, %hi(D_800D3830)
    /* D3A94 150A65E4 24633830 */  addiu      $v1, $v1, %lo(D_800D3830)
    /* D3A98 150A65E8 24F1FFFF */  addiu      $s1, $a3, -0x1
    /* D3A9C 150A65EC 02C0C025 */  or         $t8, $s6, $zero
    /* D3AA0 150A65F0 00A07825 */  or         $t7, $a1, $zero
    /* D3AA4 150A65F4 02A02825 */  or         $a1, $s5, $zero
    /* D3AA8 150A65F8 8FB50018 */  lw         $s5, 0x18($sp)
    /* D3AAC 150A65FC 8FB6001C */  lw         $s6, 0x1C($sp)
    /* D3AB0 150A6600 00005825 */  or         $t3, $zero, $zero
    /* D3AB4 150A6604 240D00A0 */  addiu      $t5, $zero, 0xA0
    /* D3AB8 150A6608 01AE0018 */  mult       $t5, $t6
    /* D3ABC 150A660C 3C0C800E */  lui        $t4, %hi(D_800DBEF4)
    /* D3AC0 150A6610 8D8CBEF4 */  lw         $t4, %lo(D_800DBEF4)($t4)
    /* D3AC4 150A6614 00007012 */  mflo       $t6
    /* D3AC8 150A6618 00000000 */  nop
    /* D3ACC 150A661C 00000000 */  nop
    /* D3AD0 150A6620 01CC7021 */  addu       $t6, $t6, $t4
    /* D3AD4 150A6624 00008025 */  or         $s0, $zero, $zero
  .L150A6628:
    /* D3AD8 150A6628 9194006E */  lbu        $s4, 0x6E($t4)
    /* D3ADC 150A662C 16800033 */  bnez       $s4, func_150A66FC
    /* D3AE0 150A6630 00000000 */   nop
    /* D3AE4 150A6634 9194004F */  lbu        $s4, 0x4F($t4)
    /* D3AE8 150A6638 32940060 */  andi       $s4, $s4, 0x60
    /* D3AEC 150A663C 1293002F */  beq        $s4, $s3, func_150A66FC
    /* D3AF0 150A6640 00000000 */   nop
    /* D3AF4 150A6644 95890050 */  lhu        $t1, 0x50($t4)
    /* D3AF8 150A6648 85880010 */  lh         $t0, 0x10($t4)
    /* D3AFC 150A664C 01095023 */  subu       $t2, $t0, $t1
    /* D3B00 150A6650 0145082A */  slt        $at, $t2, $a1
    /* D3B04 150A6654 10200029 */  beqz       $at, func_150A66FC
    /* D3B08 150A6658 00000000 */   nop
    /* D3B0C 150A665C 01095021 */  addu       $t2, $t0, $t1
    /* D3B10 150A6660 008A082A */  slt        $at, $a0, $t2
    /* D3B14 150A6664 10200025 */  beqz       $at, func_150A66FC
    /* D3B18 150A6668 00000000 */   nop
    /* D3B1C 150A666C 85880014 */  lh         $t0, 0x14($t4)
    /* D3B20 150A6670 01095023 */  subu       $t2, $t0, $t1
    /* D3B24 150A6674 0158082A */  slt        $at, $t2, $t8
    /* D3B28 150A6678 10200020 */  beqz       $at, func_150A66FC
    /* D3B2C 150A667C 00000000 */   nop
    /* D3B30 150A6680 01095021 */  addu       $t2, $t0, $t1
    /* D3B34 150A6684 01EA082A */  slt        $at, $t7, $t2
    /* D3B38 150A6688 1020001C */  beqz       $at, func_150A66FC
    /* D3B3C 150A668C 00000000 */   nop
    /* D3B40 150A6690 9188004F */  lbu        $t0, 0x4F($t4)
    /* D3B44 150A6694 24090040 */  addiu      $t1, $zero, 0x40
    /* D3B48 150A6698 01094024 */  and        $t0, $t0, $t1
    /* D3B4C 150A669C 1109000B */  beq        $t0, $t1, .L150A66CC
    /* D3B50 150A66A0 00000000 */   nop
    /* D3B54 150A66A4 95890052 */  lhu        $t1, 0x52($t4)
    /* D3B58 150A66A8 85880012 */  lh         $t0, 0x12($t4)
    /* D3B5C 150A66AC 01095023 */  subu       $t2, $t0, $t1
    /* D3B60 150A66B0 0156082A */  slt        $at, $t2, $s6
    /* D3B64 150A66B4 10200011 */  beqz       $at, func_150A66FC
    /* D3B68 150A66B8 00000000 */   nop
    /* D3B6C 150A66BC 01095021 */  addu       $t2, $t0, $t1
    /* D3B70 150A66C0 02AA082A */  slt        $at, $s5, $t2
    /* D3B74 150A66C4 1020000D */  beqz       $at, func_150A66FC
    /* D3B78 150A66C8 00000000 */   nop
  .L150A66CC:
    /* D3B7C 150A66CC 1171000B */  beq        $t3, $s1, func_150A66FC
    /* D3B80 150A66D0 00000000 */   nop
    /* D3B84 150A66D4 12800006 */  beqz       $s4, .L150A66F0
    /* D3B88 150A66D8 00000000 */   nop
    /* D3B8C 150A66DC 26100001 */  addiu      $s0, $s0, 0x1
    /* D3B90 150A66E0 A46B0000 */  sh         $t3, 0x0($v1)
    /* D3B94 150A66E4 24630002 */  addiu      $v1, $v1, 0x2
    /* D3B98 150A66E8 094299BF */  j          func_150A66FC
    /* D3B9C 150A66EC 00000000 */   nop
  .L150A66F0:
    /* D3BA0 150A66F0 24420001 */  addiu      $v0, $v0, 0x1
    /* D3BA4 150A66F4 A72B0000 */  sh         $t3, 0x0($t9)
    /* D3BA8 150A66F8 27390002 */  addiu      $t9, $t9, 0x2
endlabel func_150A6568
