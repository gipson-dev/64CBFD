glabel func_150ED578
    /* 11AA28 150ED578 8C82031C */  lw         $v0, 0x31C($a0)
    /* 11AA2C 150ED57C 1040002C */  beqz       $v0, .L150ED630
    /* 11AA30 150ED580 00000000 */   nop
    /* 11AA34 150ED584 904E0084 */  lbu        $t6, 0x84($v0)
    /* 11AA38 150ED588 3C0F800C */  lui        $t7, %hi(D_800BE616)
    /* 11AA3C 150ED58C 3C18800C */  lui        $t8, %hi(D_800BE728)
    /* 11AA40 150ED590 15C00027 */  bnez       $t6, .L150ED630
    /* 11AA44 150ED594 00000000 */   nop
    /* 11AA48 150ED598 91EFE616 */  lbu        $t7, %lo(D_800BE616)($t7)
    /* 11AA4C 150ED59C 3C0D800D */  lui        $t5, %hi(D_800CC2D0)
    /* 11AA50 150ED5A0 25ADC2D0 */  addiu      $t5, $t5, %lo(D_800CC2D0)
    /* 11AA54 150ED5A4 51E00004 */  beql       $t7, $zero, .L150ED5B8
    /* 11AA58 150ED5A8 90820124 */   lbu       $v0, 0x124($a0)
    /* 11AA5C 150ED5AC 10000002 */  b          .L150ED5B8
    /* 11AA60 150ED5B0 90820127 */   lbu       $v0, 0x127($a0)
    /* 11AA64 150ED5B4 90820124 */  lbu        $v0, 0x124($a0)
  .L150ED5B8:
    /* 11AA68 150ED5B8 8F18E728 */  lw         $t8, %lo(D_800BE728)($t8)
    /* 11AA6C 150ED5BC 0002C880 */  sll        $t9, $v0, 2
    /* 11AA70 150ED5C0 00026080 */  sll        $t4, $v0, 2
    /* 11AA74 150ED5C4 03194021 */  addu       $t0, $t8, $t9
    /* 11AA78 150ED5C8 8D090000 */  lw         $t1, 0x0($t0)
    /* 11AA7C 150ED5CC 01826023 */  subu       $t4, $t4, $v0
    /* 11AA80 150ED5D0 000C6080 */  sll        $t4, $t4, 2
    /* 11AA84 150ED5D4 952A0000 */  lhu        $t2, 0x0($t1)
    /* 11AA88 150ED5D8 01826021 */  addu       $t4, $t4, $v0
    /* 11AA8C 150ED5DC 000C6080 */  sll        $t4, $t4, 2
    /* 11AA90 150ED5E0 314B0010 */  andi       $t3, $t2, 0x10
    /* 11AA94 150ED5E4 11600012 */  beqz       $t3, .L150ED630
    /* 11AA98 150ED5E8 01826023 */   subu      $t4, $t4, $v0
    /* 11AA9C 150ED5EC 000C6080 */  sll        $t4, $t4, 2
    /* 11AAA0 150ED5F0 01826023 */  subu       $t4, $t4, $v0
    /* 11AAA4 150ED5F4 000C6080 */  sll        $t4, $t4, 2
    /* 11AAA8 150ED5F8 018D1821 */  addu       $v1, $t4, $t5
    /* 11AAAC 150ED5FC 8C6E031C */  lw         $t6, 0x31C($v1)
    /* 11AAB0 150ED600 91CF0197 */  lbu        $t7, 0x197($t6)
    /* 11AAB4 150ED604 11E0000A */  beqz       $t7, .L150ED630
    /* 11AAB8 150ED608 00000000 */   nop
    /* 11AABC 150ED60C 8C620318 */  lw         $v0, 0x318($v1)
    /* 11AAC0 150ED610 10400007 */  beqz       $v0, .L150ED630
    /* 11AAC4 150ED614 00000000 */   nop
    /* 11AAC8 150ED618 9059023D */  lbu        $t9, 0x23D($v0)
    /* 11AACC 150ED61C 909802FC */  lbu        $t8, 0x2FC($a0)
    /* 11AAD0 150ED620 24080001 */  addiu      $t0, $zero, 0x1
    /* 11AAD4 150ED624 03284804 */  sllv       $t1, $t0, $t9
    /* 11AAD8 150ED628 03095025 */  or         $t2, $t8, $t1
    /* 11AADC 150ED62C A08A02FC */  sb         $t2, 0x2FC($a0)
  .L150ED630:
    /* 11AAE0 150ED630 03E00008 */  jr         $ra
    /* 11AAE4 150ED634 00000000 */   nop
endlabel func_150ED578
