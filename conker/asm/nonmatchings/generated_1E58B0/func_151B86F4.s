glabel func_151B86F4
    /* 1E5BA4 151B86F4 27BDFF70 */  addiu      $sp, $sp, -0x90
    /* 1E5BA8 151B86F8 AFBF004C */  sw         $ra, 0x4C($sp)
    /* 1E5BAC 151B86FC AFA60098 */  sw         $a2, 0x98($sp)
    /* 1E5BB0 151B8700 AFA7009C */  sw         $a3, 0x9C($sp)
    /* 1E5BB4 151B8704 C7A40098 */  lwc1       $f4, 0x98($sp)
    /* 1E5BB8 151B8708 E7AC0084 */  swc1       $f12, 0x84($sp)
    /* 1E5BBC 151B870C E7AE0088 */  swc1       $f14, 0x88($sp)
    /* 1E5BC0 151B8710 0D42B688 */  jal        func_150ADA20
    /* 1E5BC4 151B8714 E7A4008C */   swc1      $f4, 0x8C($sp)
    /* 1E5BC8 151B8718 0D42B688 */  jal        func_150ADA20
    /* 1E5BCC 151B871C AFA2005C */   sw        $v0, 0x5C($sp)
    /* 1E5BD0 151B8720 0D42B69A */  jal        func_150ADA68
    /* 1E5BD4 151B8724 AFA20060 */   sw        $v0, 0x60($sp)
    /* 1E5BD8 151B8728 24010041 */  addiu      $at, $zero, 0x41
    /* 1E5BDC 151B872C 8FA50060 */  lw         $a1, 0x60($sp)
    /* 1E5BE0 151B8730 8FA4005C */  lw         $a0, 0x5C($sp)
    /* 1E5BE4 151B8734 27A70078 */  addiu      $a3, $sp, 0x78
    /* 1E5BE8 151B8738 00A1001B */  divu       $zero, $a1, $at
    /* 1E5BEC 151B873C 3C01800B */  lui        $at, %hi(D_800AA4CC)
    /* 1E5BF0 151B8740 C426A4CC */  lwc1       $f6, %lo(D_800AA4CC)($at)
    /* 1E5BF4 151B8744 3C01800B */  lui        $at, %hi(D_800AA4D0)
    /* 1E5BF8 151B8748 C42AA4D0 */  lwc1       $f10, %lo(D_800AA4D0)($at)
    /* 1E5BFC 151B874C 46060202 */  mul.s      $f8, $f0, $f6
    /* 1E5C00 151B8750 0000C810 */  mfhi       $t9
    /* 1E5C04 151B8754 2725FFE0 */  addiu      $a1, $t9, -0x20
    /* 1E5C08 151B8758 308E00FF */  andi       $t6, $a0, 0xFF
    /* 1E5C0C 151B875C 000E7C00 */  sll        $t7, $t6, 16
    /* 1E5C10 151B8760 00054400 */  sll        $t0, $a1, 16
    /* 1E5C14 151B8764 00082C03 */  sra        $a1, $t0, 16
    /* 1E5C18 151B8768 460A4402 */  mul.s      $f16, $f8, $f10
    /* 1E5C1C 151B876C 000F2403 */  sra        $a0, $t7, 16
    /* 1E5C20 151B8770 44068000 */  mfc1       $a2, $f16
    /* 1E5C24 151B8774 0D450DE5 */  jal        func_15143794
    /* 1E5C28 151B8778 00000000 */   nop
    /* 1E5C2C 151B877C 0D42B69A */  jal        func_150ADA68
    /* 1E5C30 151B8780 00000000 */   nop
    /* 1E5C34 151B8784 3C01800C */  lui        $at, %hi(D_800BE9A8)
    /* 1E5C38 151B8788 C42CE9A8 */  lwc1       $f12, %lo(D_800BE9A8)($at)
    /* 1E5C3C 151B878C 3C01431D */  lui        $at, (0x431D0000 >> 16)
    /* 1E5C40 151B8790 44819000 */  mtc1       $at, $f18
    /* 1E5C44 151B8794 3C014417 */  lui        $at, (0x44170000 >> 16)
    /* 1E5C48 151B8798 44813000 */  mtc1       $at, $f6
    /* 1E5C4C 151B879C 46120102 */  mul.s      $f4, $f0, $f18
    /* 1E5C50 151B87A0 3C01800B */  lui        $at, %hi(D_800AA4D4)
    /* 1E5C54 151B87A4 C42AA4D4 */  lwc1       $f10, %lo(D_800AA4D4)($at)
    /* 1E5C58 151B87A8 C7B2009C */  lwc1       $f18, 0x9C($sp)
    /* 1E5C5C 151B87AC C7B00078 */  lwc1       $f16, 0x78($sp)
    /* 1E5C60 151B87B0 44807000 */  mtc1       $zero, $f14
    /* 1E5C64 151B87B4 46062200 */  add.s      $f8, $f4, $f6
    /* 1E5C68 151B87B8 E7AE006C */  swc1       $f14, 0x6C($sp)
    /* 1E5C6C 151B87BC E7AE0070 */  swc1       $f14, 0x70($sp)
    /* 1E5C70 151B87C0 46009107 */  neg.s      $f4, $f18
    /* 1E5C74 151B87C4 460A4082 */  mul.s      $f2, $f8, $f10
    /* 1E5C78 151B87C8 C7B2007C */  lwc1       $f18, 0x7C($sp)
    /* 1E5C7C 151B87CC E7AE0074 */  swc1       $f14, 0x74($sp)
    /* 1E5C80 151B87D0 460C2182 */  mul.s      $f6, $f4, $f12
    /* 1E5C84 151B87D4 C7A400A0 */  lwc1       $f4, 0xA0($sp)
    /* 1E5C88 151B87D8 46023202 */  mul.s      $f8, $f6, $f2
    /* 1E5C8C 151B87DC 46002187 */  neg.s      $f6, $f4
    /* 1E5C90 151B87E0 C7A40080 */  lwc1       $f4, 0x80($sp)
    /* 1E5C94 151B87E4 46088280 */  add.s      $f10, $f16, $f8
    /* 1E5C98 151B87E8 460C3402 */  mul.s      $f16, $f6, $f12
    /* 1E5C9C 151B87EC C7A600A4 */  lwc1       $f6, 0xA4($sp)
    /* 1E5CA0 151B87F0 E7AA0078 */  swc1       $f10, 0x78($sp)
    /* 1E5CA4 151B87F4 46028202 */  mul.s      $f8, $f16, $f2
    /* 1E5CA8 151B87F8 46003407 */  neg.s      $f16, $f6
    /* 1E5CAC 151B87FC 46089280 */  add.s      $f10, $f18, $f8
    /* 1E5CB0 151B8800 460C8482 */  mul.s      $f18, $f16, $f12
    /* 1E5CB4 151B8804 E7AA007C */  swc1       $f10, 0x7C($sp)
    /* 1E5CB8 151B8808 46029202 */  mul.s      $f8, $f18, $f2
    /* 1E5CBC 151B880C 46082280 */  add.s      $f10, $f4, $f8
    /* 1E5CC0 151B8810 0D42B69A */  jal        func_150ADA68
    /* 1E5CC4 151B8814 E7AA0080 */   swc1      $f10, 0x80($sp)
    /* 1E5CC8 151B8818 0D42B69A */  jal        func_150ADA68
    /* 1E5CCC 151B881C E7A00058 */   swc1      $f0, 0x58($sp)
    /* 1E5CD0 151B8820 0D42B688 */  jal        func_150ADA20
    /* 1E5CD4 151B8824 E7A00064 */   swc1      $f0, 0x64($sp)
    /* 1E5CD8 151B8828 0D42B688 */  jal        func_150ADA20
    /* 1E5CDC 151B882C AFA2005C */   sw        $v0, 0x5C($sp)
    /* 1E5CE0 151B8830 3C01431D */  lui        $at, (0x431D0000 >> 16)
    /* 1E5CE4 151B8834 44818000 */  mtc1       $at, $f16
    /* 1E5CE8 151B8838 C7A60058 */  lwc1       $f6, 0x58($sp)
    /* 1E5CEC 151B883C 3C01C317 */  lui        $at, (0xC3170000 >> 16)
    /* 1E5CF0 151B8840 44812000 */  mtc1       $at, $f4
    /* 1E5CF4 151B8844 46103482 */  mul.s      $f18, $f6, $f16
    /* 1E5CF8 151B8848 3C01800B */  lui        $at, %hi(D_800AA4D8)
    /* 1E5CFC 151B884C C42AA4D8 */  lwc1       $f10, %lo(D_800AA4D8)($at)
    /* 1E5D00 151B8850 3C01425C */  lui        $at, (0x425C0000 >> 16)
    /* 1E5D04 151B8854 8FAA005C */  lw         $t2, 0x5C($sp)
    /* 1E5D08 151B8858 C7B00064 */  lwc1       $f16, 0x64($sp)
    /* 1E5D0C 151B885C 8FA300A8 */  lw         $v1, 0xA8($sp)
    /* 1E5D10 151B8860 46049200 */  add.s      $f8, $f18, $f4
    /* 1E5D14 151B8864 44819000 */  mtc1       $at, $f18
    /* 1E5D18 151B8868 3C014296 */  lui        $at, (0x42960000 >> 16)
    /* 1E5D1C 151B886C 240F000A */  addiu      $t7, $zero, 0xA
    /* 1E5D20 151B8870 460A4182 */  mul.s      $f6, $f8, $f10
    /* 1E5D24 151B8874 44814000 */  mtc1       $at, $f8
    /* 1E5D28 151B8878 2401001A */  addiu      $at, $zero, 0x1A
    /* 1E5D2C 151B887C 0141001B */  divu       $zero, $t2, $at
    /* 1E5D30 151B8880 00005810 */  mfhi       $t3
    /* 1E5D34 151B8884 24010065 */  addiu      $at, $zero, 0x65
    /* 1E5D38 151B8888 46128102 */  mul.s      $f4, $f16, $f18
    /* 1E5D3C 151B888C 0041001B */  divu       $zero, $v0, $at
    /* 1E5D40 151B8890 46082280 */  add.s      $f10, $f4, $f8
    /* 1E5D44 151B8894 00006810 */  mfhi       $t5
    /* 1E5D48 151B8898 25AE0064 */  addiu      $t6, $t5, 0x64
    /* 1E5D4C 151B889C 256C0019 */  addiu      $t4, $t3, 0x19
    /* 1E5D50 151B88A0 24180019 */  addiu      $t8, $zero, 0x19
    /* 1E5D54 151B88A4 2419FFFF */  addiu      $t9, $zero, -0x1
    /* 1E5D58 151B88A8 AFB9002C */  sw         $t9, 0x2C($sp)
    /* 1E5D5C 151B88AC AFB80024 */  sw         $t8, 0x24($sp)
    /* 1E5D60 151B88B0 AFAC0018 */  sw         $t4, 0x18($sp)
    /* 1E5D64 151B88B4 AFAE001C */  sw         $t6, 0x1C($sp)
    /* 1E5D68 151B88B8 E7AA0014 */  swc1       $f10, 0x14($sp)
    /* 1E5D6C 151B88BC E7A60010 */  swc1       $f6, 0x10($sp)
    /* 1E5D70 151B88C0 AFAF0020 */  sw         $t7, 0x20($sp)
    /* 1E5D74 151B88C4 AFA00028 */  sw         $zero, 0x28($sp)
    /* 1E5D78 151B88C8 AFA00030 */  sw         $zero, 0x30($sp)
    /* 1E5D7C 151B88CC AFA00034 */  sw         $zero, 0x34($sp)
    /* 1E5D80 151B88D0 AFA00038 */  sw         $zero, 0x38($sp)
    /* 1E5D84 151B88D4 9068000C */  lbu        $t0, 0xC($v1)
    /* 1E5D88 151B88D8 27A40084 */  addiu      $a0, $sp, 0x84
    /* 1E5D8C 151B88DC 27A5006C */  addiu      $a1, $sp, 0x6C
    /* 1E5D90 151B88E0 AFA8003C */  sw         $t0, 0x3C($sp)
    /* 1E5D94 151B88E4 90690001 */  lbu        $t1, 0x1($v1)
    /* 1E5D98 151B88E8 27A60078 */  addiu      $a2, $sp, 0x78
    /* 1E5D9C 151B88EC 3C073F80 */  lui        $a3, (0x3F800000 >> 16)
    /* 1E5DA0 151B88F0 0D4689BB */  jal        func_151A26EC
    /* 1E5DA4 151B88F4 AFA90040 */   sw        $t1, 0x40($sp)
    /* 1E5DA8 151B88F8 8FBF004C */  lw         $ra, 0x4C($sp)
    /* 1E5DAC 151B88FC 27BD0090 */  addiu      $sp, $sp, 0x90
    /* 1E5DB0 151B8900 03E00008 */  jr         $ra
    /* 1E5DB4 151B8904 00000000 */   nop
