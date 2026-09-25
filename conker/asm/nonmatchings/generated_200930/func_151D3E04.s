glabel func_151D3E04
    /* 2012B4 151D3E04 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* 2012B8 151D3E08 AFA70024 */  sw         $a3, 0x24($sp)
    /* 2012BC 151D3E0C 30EE00FF */  andi       $t6, $a3, 0xFF
    /* 2012C0 151D3E10 01C03825 */  or         $a3, $t6, $zero
    /* 2012C4 151D3E14 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 2012C8 151D3E18 AFA60020 */  sw         $a2, 0x20($sp)
    /* 2012CC 151D3E1C 8C8201D4 */  lw         $v0, 0x1D4($a0)
    /* 2012D0 151D3E20 00077980 */  sll        $t7, $a3, 6
    /* 2012D4 151D3E24 10400005 */  beqz       $v0, .L151D3E3C
    /* 2012D8 151D3E28 004F3021 */   addu      $a2, $v0, $t7
    /* 2012DC 151D3E2C 0D450C4D */  jal        func_15143134
    /* 2012E0 151D3E30 8FA40020 */   lw        $a0, 0x20($sp)
    /* 2012E4 151D3E34 1000000A */  b          .L151D3E60
    /* 2012E8 151D3E38 8FBF0014 */   lw        $ra, 0x14($sp)
  .L151D3E3C:
    /* 2012EC 151D3E3C C4840014 */  lwc1       $f4, 0x14($a0)
    /* 2012F0 151D3E40 E4A40000 */  swc1       $f4, 0x0($a1)
    /* 2012F4 151D3E44 C7A80028 */  lwc1       $f8, 0x28($sp)
    /* 2012F8 151D3E48 C4860018 */  lwc1       $f6, 0x18($a0)
    /* 2012FC 151D3E4C 46083280 */  add.s      $f10, $f6, $f8
    /* 201300 151D3E50 E4AA0004 */  swc1       $f10, 0x4($a1)
    /* 201304 151D3E54 C490001C */  lwc1       $f16, 0x1C($a0)
    /* 201308 151D3E58 E4B00008 */  swc1       $f16, 0x8($a1)
    /* 20130C 151D3E5C 8FBF0014 */  lw         $ra, 0x14($sp)
  .L151D3E60:
    /* 201310 151D3E60 27BD0018 */  addiu      $sp, $sp, 0x18
    /* 201314 151D3E64 03E00008 */  jr         $ra
    /* 201318 151D3E68 00000000 */   nop
endlabel func_151D3E04
