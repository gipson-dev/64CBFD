glabel func_1509BFB0
    /* C9460 1509BFB0 27BDFFD0 */  addiu      $sp, $sp, -0x30
    /* C9464 1509BFB4 AFA40030 */  sw         $a0, 0x30($sp)
    /* C9468 1509BFB8 3C0B800D */  lui        $t3, %hi(D_800D3840)
    /* C946C 1509BFBC 256B3840 */  addiu      $t3, $t3, %lo(D_800D3840)
    /* C9470 1509BFC0 2404FFFC */  addiu      $a0, $zero, -0x4
    /* C9474 1509BFC4 AFBF0014 */  sw         $ra, 0x14($sp)
    /* C9478 1509BFC8 AFA50034 */  sw         $a1, 0x34($sp)
    /* C947C 1509BFCC AFA60038 */  sw         $a2, 0x38($sp)
    /* C9480 1509BFD0 AFA7003C */  sw         $a3, 0x3C($sp)
    /* C9484 1509BFD4 27AE0037 */  addiu      $t6, $sp, 0x37
    /* C9488 1509BFD8 01C41024 */  and        $v0, $t6, $a0
    /* C948C 1509BFDC 8C470000 */  lw         $a3, 0x0($v0)
    /* C9490 1509BFE0 24590007 */  addiu      $t9, $v0, 0x7
    /* C9494 1509BFE4 03243024 */  and        $a2, $t9, $a0
    /* C9498 1509BFE8 8CCC0000 */  lw         $t4, 0x0($a2)
    /* C949C 1509BFEC 8FAE0030 */  lw         $t6, 0x30($sp)
    /* C94A0 1509BFF0 30EAF000 */  andi       $t2, $a3, 0xF000
    /* C94A4 1509BFF4 8D690000 */  lw         $t1, 0x0($t3)
    /* C94A8 1509BFF8 000A7B03 */  sra        $t7, $t2, 12
    /* C94AC 1509BFFC 3C01800D */  lui        $at, %hi(D_800D2F60)
    /* C94B0 1509C000 30F80FFF */  andi       $t8, $a3, 0xFFF
    /* C94B4 1509C004 25EAFFFF */  addiu      $t2, $t7, -0x1
    /* C94B8 1509C008 03003825 */  or         $a3, $t8, $zero
    /* C94BC 1509C00C 24C30004 */  addiu      $v1, $a2, 0x4
    /* C94C0 1509C010 AC382F60 */  sw         $t8, %lo(D_800D2F60)($at)
    /* C94C4 1509C014 00002825 */  or         $a1, $zero, $zero
    /* C94C8 1509C018 AFAC0038 */  sw         $t4, 0x38($sp)
    /* C94CC 1509C01C 19C0002D */  blez       $t6, .L1509C0D4
    /* C94D0 1509C020 AC2C2F64 */   sw        $t4, %lo(D_800D2F64)($at)
    /* C94D4 1509C024 31C80003 */  andi       $t0, $t6, 0x3
    /* C94D8 1509C028 11000010 */  beqz       $t0, .L1509C06C
    /* C94DC 1509C02C 01003025 */   or        $a2, $t0, $zero
    /* C94E0 1509C030 3C18800D */  lui        $t8, %hi(D_800D2F60)
    /* C94E4 1509C034 27182F60 */  addiu      $t8, $t8, %lo(D_800D2F60)
    /* C94E8 1509C038 00007880 */  sll        $t7, $zero, 2
    /* C94EC 1509C03C 01F81021 */  addu       $v0, $t7, $t8
  .L1509C040:
    /* C94F0 1509C040 24790003 */  addiu      $t9, $v1, 0x3
    /* C94F4 1509C044 03241824 */  and        $v1, $t9, $a0
    /* C94F8 1509C048 8C6C0000 */  lw         $t4, 0x0($v1)
    /* C94FC 1509C04C 24A50001 */  addiu      $a1, $a1, 0x1
    /* C9500 1509C050 24630004 */  addiu      $v1, $v1, 0x4
    /* C9504 1509C054 24420004 */  addiu      $v0, $v0, 0x4
    /* C9508 1509C058 14C5FFF9 */  bne        $a2, $a1, .L1509C040
    /* C950C 1509C05C AC4C0004 */   sw        $t4, 0x4($v0)
    /* C9510 1509C060 8FAD0030 */  lw         $t5, 0x30($sp)
    /* C9514 1509C064 50AD001C */  beql       $a1, $t5, .L1509C0D8
    /* C9518 1509C068 8FAE0030 */   lw        $t6, 0x30($sp)
  .L1509C06C:
    /* C951C 1509C06C 8FB80030 */  lw         $t8, 0x30($sp)
    /* C9520 1509C070 3C0F800D */  lui        $t7, %hi(D_800D2F60)
    /* C9524 1509C074 25EF2F60 */  addiu      $t7, $t7, %lo(D_800D2F60)
    /* C9528 1509C078 00057080 */  sll        $t6, $a1, 2
    /* C952C 1509C07C 0018C880 */  sll        $t9, $t8, 2
    /* C9530 1509C080 032F3021 */  addu       $a2, $t9, $t7
    /* C9534 1509C084 01CF1021 */  addu       $v0, $t6, $t7
  .L1509C088:
    /* C9538 1509C088 246C0003 */  addiu      $t4, $v1, 0x3
    /* C953C 1509C08C 01841824 */  and        $v1, $t4, $a0
    /* C9540 1509C090 8C6D0000 */  lw         $t5, 0x0($v1)
    /* C9544 1509C094 246E0007 */  addiu      $t6, $v1, 0x7
    /* C9548 1509C098 01C41824 */  and        $v1, $t6, $a0
    /* C954C 1509C09C AC4D0008 */  sw         $t5, 0x8($v0)
    /* C9550 1509C0A0 8C780000 */  lw         $t8, 0x0($v1)
    /* C9554 1509C0A4 24790007 */  addiu      $t9, $v1, 0x7
    /* C9558 1509C0A8 03241824 */  and        $v1, $t9, $a0
    /* C955C 1509C0AC AC58000C */  sw         $t8, 0xC($v0)
    /* C9560 1509C0B0 8C6F0000 */  lw         $t7, 0x0($v1)
    /* C9564 1509C0B4 246C0007 */  addiu      $t4, $v1, 0x7
    /* C9568 1509C0B8 01841824 */  and        $v1, $t4, $a0
    /* C956C 1509C0BC AC4F0010 */  sw         $t7, 0x10($v0)
    /* C9570 1509C0C0 8C6D0000 */  lw         $t5, 0x0($v1)
    /* C9574 1509C0C4 24420010 */  addiu      $v0, $v0, 0x10
    /* C9578 1509C0C8 24630004 */  addiu      $v1, $v1, 0x4
    /* C957C 1509C0CC 1446FFEE */  bne        $v0, $a2, .L1509C088
    /* C9580 1509C0D0 AC4D0004 */   sw        $t5, 0x4($v0)
  .L1509C0D4:
    /* C9584 1509C0D4 8FAE0030 */  lw         $t6, 0x30($sp)
  .L1509C0D8:
    /* C9588 1509C0D8 000AC880 */  sll        $t9, $t2, 2
    /* C958C 1509C0DC 3C018009 */  lui        $at, %hi(D_800884D4)
    /* C9590 1509C0E0 25D80002 */  addiu      $t8, $t6, 0x2
    /* C9594 1509C0E4 AD780000 */  sw         $t8, 0x0($t3)
    /* C9598 1509C0E8 00390821 */  addu       $at, $at, $t9
    /* C959C 1509C0EC 8C3984D4 */  lw         $t9, %lo(D_800884D4)($at)
    /* C95A0 1509C0F0 3C06800D */  lui        $a2, %hi(D_800D2F60)
    /* C95A4 1509C0F4 24C62F60 */  addiu      $a2, $a2, %lo(D_800D2F60)
    /* C95A8 1509C0F8 00E02025 */  or         $a0, $a3, $zero
    /* C95AC 1509C0FC 8FA50038 */  lw         $a1, 0x38($sp)
    /* C95B0 1509C100 0320F809 */  jalr       $t9
    /* C95B4 1509C104 AFA9001C */   sw        $t1, 0x1C($sp)
    /* C95B8 1509C108 8FA9001C */  lw         $t1, 0x1C($sp)
    /* C95BC 1509C10C 3C01800D */  lui        $at, %hi(D_800D3840)
    /* C95C0 1509C110 8FBF0014 */  lw         $ra, 0x14($sp)
    /* C95C4 1509C114 AC293840 */  sw         $t1, %lo(D_800D3840)($at)
    /* C95C8 1509C118 03E00008 */  jr         $ra
    /* C95CC 1509C11C 27BD0030 */   addiu     $sp, $sp, 0x30
endlabel func_1509BFB0
