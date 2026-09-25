glabel func_151C0360
    /* 1ED810 151C0360 27BDFFB8 */  addiu      $sp, $sp, -0x48
    /* 1ED814 151C0364 AFBF0034 */  sw         $ra, 0x34($sp)
    /* 1ED818 151C0368 AFA40048 */  sw         $a0, 0x48($sp)
    /* 1ED81C 151C036C AFA5004C */  sw         $a1, 0x4C($sp)
    /* 1ED820 151C0370 AFA60050 */  sw         $a2, 0x50($sp)
    /* 1ED824 151C0374 AFA70054 */  sw         $a3, 0x54($sp)
    /* 1ED828 151C0378 0D42B69A */  jal        func_150ADA68
    /* 1ED82C 151C037C 00000000 */   nop
    /* 1ED830 151C0380 0D42B688 */  jal        func_150ADA20
    /* 1ED834 151C0384 E7A0003C */   swc1      $f0, 0x3C($sp)
    /* 1ED838 151C0388 0D42B688 */  jal        func_150ADA20
    /* 1ED83C 151C038C AFA20040 */   sw        $v0, 0x40($sp)
    /* 1ED840 151C0390 8FA50040 */  lw         $a1, 0x40($sp)
    /* 1ED844 151C0394 3C014296 */  lui        $at, (0x42960000 >> 16)
    /* 1ED848 151C0398 44810000 */  mtc1       $at, $f0
    /* 1ED84C 151C039C 24010038 */  addiu      $at, $zero, 0x38
    /* 1ED850 151C03A0 00A1001B */  divu       $zero, $a1, $at
    /* 1ED854 151C03A4 00007010 */  mfhi       $t6
    /* 1ED858 151C03A8 240100CD */  addiu      $at, $zero, 0xCD
    /* 1ED85C 151C03AC C7A4003C */  lwc1       $f4, 0x3C($sp)
    /* 1ED860 151C03B0 0041001B */  divu       $zero, $v0, $at
    /* 1ED864 151C03B4 46002182 */  mul.s      $f6, $f4, $f0
    /* 1ED868 151C03B8 93AA0053 */  lbu        $t2, 0x53($sp)
    /* 1ED86C 151C03BC 0000C010 */  mfhi       $t8
    /* 1ED870 151C03C0 25C500C8 */  addiu      $a1, $t6, 0xC8
    /* 1ED874 151C03C4 30AF00FF */  andi       $t7, $a1, 0xFF
    /* 1ED878 151C03C8 2719012B */  addiu      $t9, $t8, 0x12B
    /* 1ED87C 151C03CC 24080001 */  addiu      $t0, $zero, 0x1
    /* 1ED880 151C03D0 24090001 */  addiu      $t1, $zero, 0x1
    /* 1ED884 151C03D4 AFA90018 */  sw         $t1, 0x18($sp)
    /* 1ED888 151C03D8 AFA80014 */  sw         $t0, 0x14($sp)
    /* 1ED88C 151C03DC AFB90010 */  sw         $t9, 0x10($sp)
    /* 1ED890 151C03E0 01E02825 */  or         $a1, $t7, $zero
    /* 1ED894 151C03E4 8FA60048 */  lw         $a2, 0x48($sp)
    /* 1ED898 151C03E8 8FA7004C */  lw         $a3, 0x4C($sp)
    /* 1ED89C 151C03EC AFA0001C */  sw         $zero, 0x1C($sp)
    /* 1ED8A0 151C03F0 AFA00020 */  sw         $zero, 0x20($sp)
    /* 1ED8A4 151C03F4 AFA00024 */  sw         $zero, 0x24($sp)
    /* 1ED8A8 151C03F8 AFA0002C */  sw         $zero, 0x2C($sp)
    /* 1ED8AC 151C03FC 46003300 */  add.s      $f12, $f6, $f0
    /* 1ED8B0 151C0400 0D439FFB */  jal        func_150E7FEC
    /* 1ED8B4 151C0404 AFAA0028 */   sw        $t2, 0x28($sp)
    /* 1ED8B8 151C0408 8FBF0034 */  lw         $ra, 0x34($sp)
    /* 1ED8BC 151C040C 27BD0048 */  addiu      $sp, $sp, 0x48
    /* 1ED8C0 151C0410 03E00008 */  jr         $ra
    /* 1ED8C4 151C0414 00000000 */   nop
endlabel func_151C0360
