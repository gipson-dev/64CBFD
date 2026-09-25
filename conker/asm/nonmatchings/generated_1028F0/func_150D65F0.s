glabel func_150D65F0
    /* 103AA0 150D65F0 27BDFFC0 */  addiu      $sp, $sp, -0x40
    /* 103AA4 150D65F4 AFBF002C */  sw         $ra, 0x2C($sp)
    /* 103AA8 150D65F8 AFA40040 */  sw         $a0, 0x40($sp)
    /* 103AAC 150D65FC AFA50044 */  sw         $a1, 0x44($sp)
    /* 103AB0 150D6600 AFA60048 */  sw         $a2, 0x48($sp)
    /* 103AB4 150D6604 AFA7004C */  sw         $a3, 0x4C($sp)
    /* 103AB8 150D6608 0D42B69A */  jal        func_150ADA68
    /* 103ABC 150D660C 00000000 */   nop
    /* 103AC0 150D6610 0D42B688 */  jal        func_150ADA20
    /* 103AC4 150D6614 E7A00034 */   swc1      $f0, 0x34($sp)
    /* 103AC8 150D6618 0D42B688 */  jal        func_150ADA20
    /* 103ACC 150D661C AFA20038 */   sw        $v0, 0x38($sp)
    /* 103AD0 150D6620 3C0142C8 */  lui        $at, (0x42C80000 >> 16)
    /* 103AD4 150D6624 44813000 */  mtc1       $at, $f6
    /* 103AD8 150D6628 8FA50038 */  lw         $a1, 0x38($sp)
    /* 103ADC 150D662C 3C014316 */  lui        $at, (0x43160000 >> 16)
    /* 103AE0 150D6630 44815000 */  mtc1       $at, $f10
    /* 103AE4 150D6634 24010047 */  addiu      $at, $zero, 0x47
    /* 103AE8 150D6638 00A1001B */  divu       $zero, $a1, $at
    /* 103AEC 150D663C 00007010 */  mfhi       $t6
    /* 103AF0 150D6640 2401001F */  addiu      $at, $zero, 0x1F
    /* 103AF4 150D6644 C7A40034 */  lwc1       $f4, 0x34($sp)
    /* 103AF8 150D6648 0041001B */  divu       $zero, $v0, $at
    /* 103AFC 150D664C 46062202 */  mul.s      $f8, $f4, $f6
    /* 103B00 150D6650 93A9004B */  lbu        $t1, 0x4B($sp)
    /* 103B04 150D6654 8FAA004C */  lw         $t2, 0x4C($sp)
    /* 103B08 150D6658 0000C010 */  mfhi       $t8
    /* 103B0C 150D665C 25C50082 */  addiu      $a1, $t6, 0x82
    /* 103B10 150D6660 30AF00FF */  andi       $t7, $a1, 0xFF
    /* 103B14 150D6664 27190032 */  addiu      $t9, $t8, 0x32
    /* 103B18 150D6668 24080001 */  addiu      $t0, $zero, 0x1
    /* 103B1C 150D666C AFA80018 */  sw         $t0, 0x18($sp)
    /* 103B20 150D6670 AFB90010 */  sw         $t9, 0x10($sp)
    /* 103B24 150D6674 01E02825 */  or         $a1, $t7, $zero
    /* 103B28 150D6678 8FA60040 */  lw         $a2, 0x40($sp)
    /* 103B2C 150D667C 8FA70044 */  lw         $a3, 0x44($sp)
    /* 103B30 150D6680 AFA00014 */  sw         $zero, 0x14($sp)
    /* 103B34 150D6684 460A4300 */  add.s      $f12, $f8, $f10
    /* 103B38 150D6688 AFA9001C */  sw         $t1, 0x1C($sp)
    /* 103B3C 150D668C 0D469756 */  jal        func_151A5D58
    /* 103B40 150D6690 AFAA0020 */   sw        $t2, 0x20($sp)
    /* 103B44 150D6694 8FBF002C */  lw         $ra, 0x2C($sp)
    /* 103B48 150D6698 27BD0040 */  addiu      $sp, $sp, 0x40
    /* 103B4C 150D669C 03E00008 */  jr         $ra
    /* 103B50 150D66A0 00000000 */   nop
endlabel func_150D65F0
