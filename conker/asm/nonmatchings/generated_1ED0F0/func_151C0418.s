glabel func_151C0418
    /* 1ED8C8 151C0418 27BDFFB0 */  addiu      $sp, $sp, -0x50
    /* 1ED8CC 151C041C AFBF0034 */  sw         $ra, 0x34($sp)
    /* 1ED8D0 151C0420 AFA50054 */  sw         $a1, 0x54($sp)
    /* 1ED8D4 151C0424 AFA60058 */  sw         $a2, 0x58($sp)
    /* 1ED8D8 151C0428 240E0003 */  addiu      $t6, $zero, 0x3
    /* 1ED8DC 151C042C 240FFFFF */  addiu      $t7, $zero, -0x1
    /* 1ED8E0 151C0430 A3AE0048 */  sb         $t6, 0x48($sp)
    /* 1ED8E4 151C0434 A3AF0049 */  sb         $t7, 0x49($sp)
    /* 1ED8E8 151C0438 0D42B688 */  jal        func_150ADA20
    /* 1ED8EC 151C043C AFA40050 */   sw        $a0, 0x50($sp)
    /* 1ED8F0 151C0440 2401000B */  addiu      $at, $zero, 0xB
    /* 1ED8F4 151C0444 0041001B */  divu       $zero, $v0, $at
    /* 1ED8F8 151C0448 8FA40050 */  lw         $a0, 0x50($sp)
    /* 1ED8FC 151C044C 0000C010 */  mfhi       $t8
    /* 1ED900 151C0450 27190014 */  addiu      $t9, $t8, 0x14
    /* 1ED904 151C0454 A7B9004A */  sh         $t9, 0x4A($sp)
    /* 1ED908 151C0458 A3A0004C */  sb         $zero, 0x4C($sp)
    /* 1ED90C 151C045C C4840000 */  lwc1       $f4, 0x0($a0)
    /* 1ED910 151C0460 4600218D */  trunc.w.s  $f6, $f4
    /* 1ED914 151C0464 44093000 */  mfc1       $t1, $f6
    /* 1ED918 151C0468 00000000 */  nop
    /* 1ED91C 151C046C AFA9003C */  sw         $t1, 0x3C($sp)
    /* 1ED920 151C0470 C4880004 */  lwc1       $f8, 0x4($a0)
    /* 1ED924 151C0474 4600428D */  trunc.w.s  $f10, $f8
    /* 1ED928 151C0478 440B5000 */  mfc1       $t3, $f10
    /* 1ED92C 151C047C 00000000 */  nop
    /* 1ED930 151C0480 AFAB0040 */  sw         $t3, 0x40($sp)
    /* 1ED934 151C0484 C4900008 */  lwc1       $f16, 0x8($a0)
    /* 1ED938 151C0488 4600848D */  trunc.w.s  $f18, $f16
    /* 1ED93C 151C048C 440D9000 */  mfc1       $t5, $f18
    /* 1ED940 151C0490 0D42B688 */  jal        func_150ADA20
    /* 1ED944 151C0494 AFAD0044 */   sw        $t5, 0x44($sp)
    /* 1ED948 151C0498 24010079 */  addiu      $at, $zero, 0x79
    /* 1ED94C 151C049C 0041001B */  divu       $zero, $v0, $at
    /* 1ED950 151C04A0 93B90057 */  lbu        $t9, 0x57($sp)
    /* 1ED954 151C04A4 8FA80058 */  lw         $t0, 0x58($sp)
    /* 1ED958 151C04A8 00003010 */  mfhi       $a2
    /* 1ED95C 151C04AC 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 1ED960 151C04B0 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 1ED964 151C04B4 241800FF */  addiu      $t8, $zero, 0xFF
    /* 1ED968 151C04B8 AFB80018 */  sw         $t8, 0x18($sp)
    /* 1ED96C 151C04BC AFAF0014 */  sw         $t7, 0x14($sp)
    /* 1ED970 151C04C0 AFAE0010 */  sw         $t6, 0x10($sp)
    /* 1ED974 151C04C4 24C6003C */  addiu      $a2, $a2, 0x3C
    /* 1ED978 151C04C8 27A40048 */  addiu      $a0, $sp, 0x48
    /* 1ED97C 151C04CC 27A5003C */  addiu      $a1, $sp, 0x3C
    /* 1ED980 151C04D0 240700FF */  addiu      $a3, $zero, 0xFF
    /* 1ED984 151C04D4 AFA0001C */  sw         $zero, 0x1C($sp)
    /* 1ED988 151C04D8 AFA00020 */  sw         $zero, 0x20($sp)
    /* 1ED98C 151C04DC AFB90024 */  sw         $t9, 0x24($sp)
    /* 1ED990 151C04E0 0D4580B0 */  jal        func_151602C0
    /* 1ED994 151C04E4 AFA80028 */   sw        $t0, 0x28($sp)
    /* 1ED998 151C04E8 8FBF0034 */  lw         $ra, 0x34($sp)
    /* 1ED99C 151C04EC 27BD0050 */  addiu      $sp, $sp, 0x50
    /* 1ED9A0 151C04F0 03E00008 */  jr         $ra
    /* 1ED9A4 151C04F4 00000000 */   nop
endlabel func_151C0418
