glabel func_151D4408
    /* 2018B8 151D4408 27BDFF30 */  addiu      $sp, $sp, -0xD0
    /* 2018BC 151D440C AFBF002C */  sw         $ra, 0x2C($sp)
    /* 2018C0 151D4410 AFA400D0 */  sw         $a0, 0xD0($sp)
    /* 2018C4 151D4414 AFA500D4 */  sw         $a1, 0xD4($sp)
    /* 2018C8 151D4418 AFA600D8 */  sw         $a2, 0xD8($sp)
    /* 2018CC 151D441C AFA700DC */  sw         $a3, 0xDC($sp)
    /* 2018D0 151D4420 27AE0064 */  addiu      $t6, $sp, 0x64
    /* 2018D4 151D4424 27AF0068 */  addiu      $t7, $sp, 0x68
    /* 2018D8 151D4428 27B8006C */  addiu      $t8, $sp, 0x6C
    /* 2018DC 151D442C 27B90038 */  addiu      $t9, $sp, 0x38
    /* 2018E0 151D4430 27A8003C */  addiu      $t0, $sp, 0x3C
    /* 2018E4 151D4434 27A90040 */  addiu      $t1, $sp, 0x40
    /* 2018E8 151D4438 AFA90024 */  sw         $t1, 0x24($sp)
    /* 2018EC 151D443C AFA80020 */  sw         $t0, 0x20($sp)
    /* 2018F0 151D4440 AFB9001C */  sw         $t9, 0x1C($sp)
    /* 2018F4 151D4444 AFB80018 */  sw         $t8, 0x18($sp)
    /* 2018F8 151D4448 AFAF0014 */  sw         $t7, 0x14($sp)
    /* 2018FC 151D444C AFAE0010 */  sw         $t6, 0x10($sp)
    /* 201900 151D4450 8FA400D8 */  lw         $a0, 0xD8($sp)
    /* 201904 151D4454 27A50044 */  addiu      $a1, $sp, 0x44
    /* 201908 151D4458 27A60048 */  addiu      $a2, $sp, 0x48
    /* 20190C 151D445C 0D40FD01 */  jal        func_1503F404
    /* 201910 151D4460 27A7004C */   addiu     $a3, $sp, 0x4C
    /* 201914 151D4464 3C014334 */  lui        $at, (0x43340000 >> 16)
    /* 201918 151D4468 44813000 */  mtc1       $at, $f6
    /* 20191C 151D446C C7A40064 */  lwc1       $f4, 0x64($sp)
    /* 201920 151D4470 46062200 */  add.s      $f8, $f4, $f6
    /* 201924 151D4474 E7A80064 */  swc1       $f8, 0x64($sp)
    /* 201928 151D4478 0D42B69A */  jal        func_150ADA68
    /* 20192C 151D447C 00000000 */   nop
    /* 201930 151D4480 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 201934 151D4484 44816000 */  mtc1       $at, $f12
    /* 201938 151D4488 3C01800B */  lui        $at, %hi(D_800AB1D4)
    /* 20193C 151D448C C42AB1D4 */  lwc1       $f10, %lo(D_800AB1D4)($at)
    /* 201940 151D4490 C7B000E0 */  lwc1       $f16, 0xE0($sp)
    /* 201944 151D4494 8FAB00D0 */  lw         $t3, 0xD0($sp)
    /* 201948 151D4498 E7AC0054 */  swc1       $f12, 0x54($sp)
    /* 20194C 151D449C 46105482 */  mul.s      $f18, $f10, $f16
    /* 201950 151D44A0 E7AC0058 */  swc1       $f12, 0x58($sp)
    /* 201954 151D44A4 E7AC0070 */  swc1       $f12, 0x70($sp)
    /* 201958 151D44A8 E7AC0074 */  swc1       $f12, 0x74($sp)
    /* 20195C 151D44AC E7AC0078 */  swc1       $f12, 0x78($sp)
    /* 201960 151D44B0 8FA200D4 */  lw         $v0, 0xD4($sp)
    /* 201964 151D44B4 27AA007C */  addiu      $t2, $sp, 0x7C
    /* 201968 151D44B8 E7B20060 */  swc1       $f18, 0x60($sp)
    /* 20196C 151D44BC E7B2005C */  swc1       $f18, 0x5C($sp)
    /* 201970 151D44C0 8D610000 */  lw         $at, 0x0($t3)
    /* 201974 151D44C4 AD410000 */  sw         $at, 0x0($t2)
    /* 201978 151D44C8 8D6E0004 */  lw         $t6, 0x4($t3)
    /* 20197C 151D44CC AD4E0004 */  sw         $t6, 0x4($t2)
    /* 201980 151D44D0 8D610008 */  lw         $at, 0x8($t3)
    /* 201984 151D44D4 AD410008 */  sw         $at, 0x8($t2)
    /* 201988 151D44D8 3C0142D2 */  lui        $at, (0x42D20000 >> 16)
    /* 20198C 151D44DC 44812000 */  mtc1       $at, $f4
    /* 201990 151D44E0 3C014347 */  lui        $at, (0x43470000 >> 16)
    /* 201994 151D44E4 44814000 */  mtc1       $at, $f8
    /* 201998 151D44E8 46040182 */  mul.s      $f6, $f0, $f4
    /* 20199C 151D44EC 3C01800B */  lui        $at, %hi(D_800AB1D8)
    /* 2019A0 151D44F0 C430B1D8 */  lwc1       $f16, %lo(D_800AB1D8)($at)
    /* 2019A4 151D44F4 C4520000 */  lwc1       $f18, 0x0($v0)
    /* 2019A8 151D44F8 46083280 */  add.s      $f10, $f6, $f8
    /* 2019AC 151D44FC 46105082 */  mul.s      $f2, $f10, $f16
    /* 2019B0 151D4500 00000000 */  nop
    /* 2019B4 151D4504 46029102 */  mul.s      $f4, $f18, $f2
    /* 2019B8 151D4508 E7A40088 */  swc1       $f4, 0x88($sp)
    /* 2019BC 151D450C C4460004 */  lwc1       $f6, 0x4($v0)
    /* 2019C0 151D4510 46023202 */  mul.s      $f8, $f6, $f2
    /* 2019C4 151D4514 E7A8008C */  swc1       $f8, 0x8C($sp)
    /* 2019C8 151D4518 C44A0008 */  lwc1       $f10, 0x8($v0)
    /* 2019CC 151D451C 46025402 */  mul.s      $f16, $f10, $f2
    /* 2019D0 151D4520 0D42B69A */  jal        func_150ADA68
    /* 2019D4 151D4524 E7B00090 */   swc1      $f16, 0x90($sp)
    /* 2019D8 151D4528 3C01800B */  lui        $at, %hi(D_800AB1DC)
    /* 2019DC 151D452C C432B1DC */  lwc1       $f18, %lo(D_800AB1DC)($at)
    /* 2019E0 151D4530 3C01800B */  lui        $at, %hi(D_800AB1E0)
    /* 2019E4 151D4534 C426B1E0 */  lwc1       $f6, %lo(D_800AB1E0)($at)
    /* 2019E8 151D4538 46120102 */  mul.s      $f4, $f0, $f18
    /* 2019EC 151D453C 3C01800B */  lui        $at, %hi(D_800AB1E4)
    /* 2019F0 151D4540 C42AB1E4 */  lwc1       $f10, %lo(D_800AB1E4)($at)
    /* 2019F4 151D4544 44809000 */  mtc1       $zero, $f18
    /* 2019F8 151D4548 00000000 */  nop
    /* 2019FC 151D454C E7B20098 */  swc1       $f18, 0x98($sp)
    /* 201A00 151D4550 46062200 */  add.s      $f8, $f4, $f6
    /* 201A04 151D4554 460A4402 */  mul.s      $f16, $f8, $f10
    /* 201A08 151D4558 0D42B69A */  jal        func_150ADA68
    /* 201A0C 151D455C E7B00094 */   swc1      $f16, 0x94($sp)
    /* 201A10 151D4560 3C01800B */  lui        $at, %hi(D_800AB1E8)
    /* 201A14 151D4564 C424B1E8 */  lwc1       $f4, %lo(D_800AB1E8)($at)
    /* 201A18 151D4568 3C01800B */  lui        $at, %hi(D_800AB1EC)
    /* 201A1C 151D456C C428B1EC */  lwc1       $f8, %lo(D_800AB1EC)($at)
    /* 201A20 151D4570 46040182 */  mul.s      $f6, $f0, $f4
    /* 201A24 151D4574 3C01800B */  lui        $at, %hi(D_800AB1F0)
    /* 201A28 151D4578 C430B1F0 */  lwc1       $f16, %lo(D_800AB1F0)($at)
    /* 201A2C 151D457C 46083280 */  add.s      $f10, $f6, $f8
    /* 201A30 151D4580 46105482 */  mul.s      $f18, $f10, $f16
    /* 201A34 151D4584 0D42B69A */  jal        func_150ADA68
    /* 201A38 151D4588 E7B2009C */   swc1      $f18, 0x9C($sp)
    /* 201A3C 151D458C 3C0143A0 */  lui        $at, (0x43A00000 >> 16)
    /* 201A40 151D4590 44812000 */  mtc1       $at, $f4
    /* 201A44 151D4594 3C01800B */  lui        $at, %hi(D_800AB1F4)
    /* 201A48 151D4598 C428B1F4 */  lwc1       $f8, %lo(D_800AB1F4)($at)
    /* 201A4C 151D459C 46040182 */  mul.s      $f6, $f0, $f4
    /* 201A50 151D45A0 3C01800B */  lui        $at, %hi(D_800AB1F8)
    /* 201A54 151D45A4 C430B1F8 */  lwc1       $f16, %lo(D_800AB1F8)($at)
    /* 201A58 151D45A8 240F29E8 */  addiu      $t7, $zero, 0x29E8
    /* 201A5C 151D45AC AFAF00A4 */  sw         $t7, 0xA4($sp)
    /* 201A60 151D45B0 46083280 */  add.s      $f10, $f6, $f8
    /* 201A64 151D45B4 46105482 */  mul.s      $f18, $f10, $f16
    /* 201A68 151D45B8 0D42B688 */  jal        func_150ADA20
    /* 201A6C 151D45BC E7B200A0 */   swc1      $f18, 0xA0($sp)
    /* 201A70 151D45C0 8FA300DC */  lw         $v1, 0xDC($sp)
    /* 201A74 151D45C4 30580007 */  andi       $t8, $v0, 0x7
    /* 201A78 151D45C8 2719001C */  addiu      $t9, $t8, 0x1C
    /* 201A7C 151D45CC 24080025 */  addiu      $t0, $zero, 0x25
    /* 201A80 151D45D0 240900FF */  addiu      $t1, $zero, 0xFF
    /* 201A84 151D45D4 240D0008 */  addiu      $t5, $zero, 0x8
    /* 201A88 151D45D8 240C0002 */  addiu      $t4, $zero, 0x2
    /* 201A8C 151D45DC 240A0001 */  addiu      $t2, $zero, 0x1
    /* 201A90 151D45E0 A7B900A8 */  sh         $t9, 0xA8($sp)
    /* 201A94 151D45E4 A7A800AA */  sh         $t0, 0xAA($sp)
    /* 201A98 151D45E8 A3A000AC */  sb         $zero, 0xAC($sp)
    /* 201A9C 151D45EC AFA000B0 */  sw         $zero, 0xB0($sp)
    /* 201AA0 151D45F0 A3A900B4 */  sb         $t1, 0xB4($sp)
    /* 201AA4 151D45F4 A3AD00B5 */  sb         $t5, 0xB5($sp)
    /* 201AA8 151D45F8 A3A000B6 */  sb         $zero, 0xB6($sp)
    /* 201AAC 151D45FC A3A000B7 */  sb         $zero, 0xB7($sp)
    /* 201AB0 151D4600 A3A000B8 */  sb         $zero, 0xB8($sp)
    /* 201AB4 151D4604 A3A000B9 */  sb         $zero, 0xB9($sp)
    /* 201AB8 151D4608 A3A000BA */  sb         $zero, 0xBA($sp)
    /* 201ABC 151D460C A3A000BB */  sb         $zero, 0xBB($sp)
    /* 201AC0 151D4610 A3AC00BC */  sb         $t4, 0xBC($sp)
    /* 201AC4 151D4614 A3AA00BE */  sb         $t2, 0xBE($sp)
    /* 201AC8 151D4618 AFA300C0 */  sw         $v1, 0xC0($sp)
    /* 201ACC 151D461C 906B003B */  lbu        $t3, 0x3B($v1)
    /* 201AD0 151D4620 8FB900E8 */  lw         $t9, 0xE8($sp)
    /* 201AD4 151D4624 93B800E7 */  lbu        $t8, 0xE7($sp)
    /* 201AD8 151D4628 240E0006 */  addiu      $t6, $zero, 0x6
    /* 201ADC 151D462C 240F002A */  addiu      $t7, $zero, 0x2A
    /* 201AE0 151D4630 A7AE00C6 */  sh         $t6, 0xC6($sp)
    /* 201AE4 151D4634 A7AF00C8 */  sh         $t7, 0xC8($sp)
    /* 201AE8 151D4638 27A40054 */  addiu      $a0, $sp, 0x54
    /* 201AEC 151D463C 24050003 */  addiu      $a1, $zero, 0x3
    /* 201AF0 151D4640 240600FF */  addiu      $a2, $zero, 0xFF
    /* 201AF4 151D4644 00003825 */  or         $a3, $zero, $zero
    /* 201AF8 151D4648 A3AB00C4 */  sb         $t3, 0xC4($sp)
    /* 201AFC 151D464C AFB90014 */  sw         $t9, 0x14($sp)
    /* 201B00 151D4650 0D44CA93 */  jal        func_15132A4C
    /* 201B04 151D4654 AFB80010 */   sw        $t8, 0x10($sp)
    /* 201B08 151D4658 8FBF002C */  lw         $ra, 0x2C($sp)
    /* 201B0C 151D465C 27BD00D0 */  addiu      $sp, $sp, 0xD0
    /* 201B10 151D4660 03E00008 */  jr         $ra
    /* 201B14 151D4664 00000000 */   nop
endlabel func_151D4408
