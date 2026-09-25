glabel func_150D4CC4
    /* 102174 150D4CC4 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* 102178 150D4CC8 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 10217C 150D4CCC 3C0F800C */  lui        $t7, %hi(D_800BE9E4)
    /* 102180 150D4CD0 8DEFE9E4 */  lw         $t7, %lo(D_800BE9E4)($t7)
    /* 102184 150D4CD4 848E0170 */  lh         $t6, 0x170($a0)
    /* 102188 150D4CD8 01CFC023 */  subu       $t8, $t6, $t7
    /* 10218C 150D4CDC A4980170 */  sh         $t8, 0x170($a0)
    /* 102190 150D4CE0 84990170 */  lh         $t9, 0x170($a0)
    /* 102194 150D4CE4 07230010 */  bgezl      $t9, .L150D4D28
    /* 102198 150D4CE8 24830110 */   addiu     $v1, $a0, 0x110
    /* 10219C 150D4CEC 0D42B688 */  jal        func_150ADA20
    /* 1021A0 150D4CF0 AFA40018 */   sw        $a0, 0x18($sp)
    /* 1021A4 150D4CF4 30480003 */  andi       $t0, $v0, 0x3
    /* 1021A8 150D4CF8 00084880 */  sll        $t1, $t0, 2
    /* 1021AC 150D4CFC 3C0A800A */  lui        $t2, %hi(D_800A09C0)
    /* 1021B0 150D4D00 01495021 */  addu       $t2, $t2, $t1
    /* 1021B4 150D4D04 8D4A09C0 */  lw         $t2, %lo(D_800A09C0)($t2)
    /* 1021B8 150D4D08 8FA40018 */  lw         $a0, 0x18($sp)
    /* 1021BC 150D4D0C 0D42B688 */  jal        func_150ADA20
    /* 1021C0 150D4D10 A08A0018 */   sb        $t2, 0x18($a0)
    /* 1021C4 150D4D14 8FA40018 */  lw         $a0, 0x18($sp)
    /* 1021C8 150D4D18 304B0007 */  andi       $t3, $v0, 0x7
    /* 1021CC 150D4D1C 256C0003 */  addiu      $t4, $t3, 0x3
    /* 1021D0 150D4D20 A48C0170 */  sh         $t4, 0x170($a0)
    /* 1021D4 150D4D24 24830110 */  addiu      $v1, $a0, 0x110
  .L150D4D28:
    /* 1021D8 150D4D28 C4600048 */  lwc1       $f0, 0x48($v1)
    /* 1021DC 150D4D2C C4840174 */  lwc1       $f4, 0x174($a0)
    /* 1021E0 150D4D30 3C01800A */  lui        $at, %hi(D_800A0A14)
    /* 1021E4 150D4D34 C4280A14 */  lwc1       $f8, %lo(D_800A0A14)($at)
    /* 1021E8 150D4D38 46002181 */  sub.s      $f6, $f4, $f0
    /* 1021EC 150D4D3C 24020001 */  addiu      $v0, $zero, 0x1
    /* 1021F0 150D4D40 46083282 */  mul.s      $f10, $f6, $f8
    /* 1021F4 150D4D44 460A0400 */  add.s      $f16, $f0, $f10
    /* 1021F8 150D4D48 E4700048 */  swc1       $f16, 0x48($v1)
    /* 1021FC 150D4D4C 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 102200 150D4D50 03E00008 */  jr         $ra
    /* 102204 150D4D54 27BD0018 */   addiu     $sp, $sp, 0x18
endlabel func_150D4CC4
