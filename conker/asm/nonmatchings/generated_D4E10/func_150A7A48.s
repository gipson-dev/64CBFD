/* Original cached-right-operand matrix product; preserve row-wise read/write order. */
glabel func_150A7A48
    /* D4EF8 150A7A48 E7B4FFE0 */  swc1       $f20, -0x20($sp)
    /* D4EFC 150A7A4C 27BDFFE0 */  addiu      $sp, $sp, -0x20
    /* D4F00 150A7A50 E7B50004 */  swc1       $f21, 0x4($sp)
    /* D4F04 150A7A54 24080004 */  addiu      $t0, $zero, 0x4
    /* D4F08 150A7A58 E7B60008 */  swc1       $f22, 0x8($sp)
    /* D4F0C 150A7A5C E7B7000C */  swc1       $f23, 0xC($sp)
    /* D4F10 150A7A60 E7B80010 */  swc1       $f24, 0x10($sp)
    /* D4F14 150A7A64 E7B90014 */  swc1       $f25, 0x14($sp)
    /* D4F18 150A7A68 E7BA0018 */  swc1       $f26, 0x18($sp)
    /* D4F1C 150A7A6C E7BB001C */  swc1       $f27, 0x1C($sp)
    /* D4F20 150A7A70 C4A00000 */  lwc1       $f0, 0x0($a1)
    /* D4F24 150A7A74 C4A10004 */  lwc1       $f1, 0x4($a1)
    /* D4F28 150A7A78 C4A20008 */  lwc1       $f2, 0x8($a1)
    /* D4F2C 150A7A7C C4A3000C */  lwc1       $f3, 0xC($a1)
    /* D4F30 150A7A80 C4A40010 */  lwc1       $f4, 0x10($a1)
    /* D4F34 150A7A84 C4A50014 */  lwc1       $f5, 0x14($a1)
    /* D4F38 150A7A88 C4A60018 */  lwc1       $f6, 0x18($a1)
    /* D4F3C 150A7A8C C4A7001C */  lwc1       $f7, 0x1C($a1)
    /* D4F40 150A7A90 C4A80020 */  lwc1       $f8, 0x20($a1)
    /* D4F44 150A7A94 C4A90024 */  lwc1       $f9, 0x24($a1)
    /* D4F48 150A7A98 C4AA0028 */  lwc1       $f10, 0x28($a1)
    /* D4F4C 150A7A9C C4AB002C */  lwc1       $f11, 0x2C($a1)
    /* D4F50 150A7AA0 C4AC0030 */  lwc1       $f12, 0x30($a1)
    /* D4F54 150A7AA4 C4AD0034 */  lwc1       $f13, 0x34($a1)
    /* D4F58 150A7AA8 C4AE0038 */  lwc1       $f14, 0x38($a1)
    /* D4F5C 150A7AAC C4AF003C */  lwc1       $f15, 0x3C($a1)
  .L150A7AB0:
    /* D4F60 150A7AB0 24840010 */  addiu      $a0, $a0, 0x10
    /* D4F64 150A7AB4 C490FFF0 */  lwc1       $f16, -0x10($a0)
    /* D4F68 150A7AB8 C491FFF4 */  lwc1       $f17, -0xC($a0)
    /* D4F6C 150A7ABC 46008502 */  mul.s      $f20, $f16, $f0
    /* D4F70 150A7AC0 C492FFF8 */  lwc1       $f18, -0x8($a0)
    /* D4F74 150A7AC4 46018582 */  mul.s      $f22, $f16, $f1
    /* D4F78 150A7AC8 C493FFFC */  lwc1       $f19, -0x4($a0)
    /* D4F7C 150A7ACC 46048D42 */  mul.s      $f21, $f17, $f4
    /* D4F80 150A7AD0 2508FFFF */  addiu      $t0, $t0, -0x1
    /* D4F84 150A7AD4 46058DC2 */  mul.s      $f23, $f17, $f5
    /* D4F88 150A7AD8 4615A500 */  add.s      $f20, $f20, $f21
    /* D4F8C 150A7ADC 46089542 */  mul.s      $f21, $f18, $f8
    /* D4F90 150A7AE0 4617B580 */  add.s      $f22, $f22, $f23
    /* D4F94 150A7AE4 460995C2 */  mul.s      $f23, $f18, $f9
    /* D4F98 150A7AE8 4615A500 */  add.s      $f20, $f20, $f21
    /* D4F9C 150A7AEC 46028602 */  mul.s      $f24, $f16, $f2
    /* D4FA0 150A7AF0 4617B580 */  add.s      $f22, $f22, $f23
    /* D4FA4 150A7AF4 460C9D42 */  mul.s      $f21, $f19, $f12
    /* D4FA8 150A7AF8 24C60010 */  addiu      $a2, $a2, 0x10
    /* D4FAC 150A7AFC 4615A500 */  add.s      $f20, $f20, $f21
    /* D4FB0 150A7B00 460D9DC2 */  mul.s      $f23, $f19, $f13
    /* D4FB4 150A7B04 E4D4FFF0 */  swc1       $f20, -0x10($a2)
    /* D4FB8 150A7B08 46038682 */  mul.s      $f26, $f16, $f3
    /* D4FBC 150A7B0C 4617B580 */  add.s      $f22, $f22, $f23
    /* D4FC0 150A7B10 46068E42 */  mul.s      $f25, $f17, $f6
    /* D4FC4 150A7B14 E4D6FFF4 */  swc1       $f22, -0xC($a2)
    /* D4FC8 150A7B18 46078EC2 */  mul.s      $f27, $f17, $f7
    /* D4FCC 150A7B1C 4619C600 */  add.s      $f24, $f24, $f25
    /* D4FD0 150A7B20 460A9642 */  mul.s      $f25, $f18, $f10
    /* D4FD4 150A7B24 461BD680 */  add.s      $f26, $f26, $f27
    /* D4FD8 150A7B28 460B96C2 */  mul.s      $f27, $f18, $f11
    /* D4FDC 150A7B2C 4619C600 */  add.s      $f24, $f24, $f25
    /* D4FE0 150A7B30 460E9E42 */  mul.s      $f25, $f19, $f14
    /* D4FE4 150A7B34 461BD680 */  add.s      $f26, $f26, $f27
    /* D4FE8 150A7B38 460F9EC2 */  mul.s      $f27, $f19, $f15
    /* D4FEC 150A7B3C 4619C600 */  add.s      $f24, $f24, $f25
    /* D4FF0 150A7B40 461BD680 */  add.s      $f26, $f26, $f27
    /* D4FF4 150A7B44 E4D8FFF8 */  swc1       $f24, -0x8($a2)
    /* D4FF8 150A7B48 1500FFD9 */  bnez       $t0, .L150A7AB0
    /* D4FFC 150A7B4C E4DAFFFC */   swc1      $f26, -0x4($a2)
    /* D5000 150A7B50 C7B40000 */  lwc1       $f20, 0x0($sp)
    /* D5004 150A7B54 C7B50004 */  lwc1       $f21, 0x4($sp)
    /* D5008 150A7B58 C7B60008 */  lwc1       $f22, 0x8($sp)
    /* D500C 150A7B5C C7B7000C */  lwc1       $f23, 0xC($sp)
    /* D5010 150A7B60 C7B80010 */  lwc1       $f24, 0x10($sp)
    /* D5014 150A7B64 C7B90014 */  lwc1       $f25, 0x14($sp)
    /* D5018 150A7B68 C7BA0018 */  lwc1       $f26, 0x18($sp)
    /* D501C 150A7B6C C7BB001C */  lwc1       $f27, 0x1C($sp)
    /* D5020 150A7B70 03E00008 */  jr         $ra
    /* D5024 150A7B74 27BD0020 */   addiu     $sp, $sp, 0x20
    /* D5028 150A7B78 00000000 */  nop
    /* D502C 150A7B7C 00000000 */  nop
endlabel func_150A7A48
