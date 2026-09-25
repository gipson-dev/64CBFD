glabel func_151C1860
    /* 1EED10 151C1860 27BDFFB0 */  addiu      $sp, $sp, -0x50
    /* 1EED14 151C1864 AFBF0034 */  sw         $ra, 0x34($sp)
    /* 1EED18 151C1868 AFA50054 */  sw         $a1, 0x54($sp)
    /* 1EED1C 151C186C AFA60058 */  sw         $a2, 0x58($sp)
    /* 1EED20 151C1870 240E0003 */  addiu      $t6, $zero, 0x3
    /* 1EED24 151C1874 240FFFFF */  addiu      $t7, $zero, -0x1
    /* 1EED28 151C1878 A3AE0048 */  sb         $t6, 0x48($sp)
    /* 1EED2C 151C187C A3AF0049 */  sb         $t7, 0x49($sp)
    /* 1EED30 151C1880 0D42B688 */  jal        func_150ADA20
    /* 1EED34 151C1884 AFA40050 */   sw        $a0, 0x50($sp)
    /* 1EED38 151C1888 24010005 */  addiu      $at, $zero, 0x5
    /* 1EED3C 151C188C 0041001B */  divu       $zero, $v0, $at
    /* 1EED40 151C1890 8FA40050 */  lw         $a0, 0x50($sp)
    /* 1EED44 151C1894 0000C010 */  mfhi       $t8
    /* 1EED48 151C1898 27190005 */  addiu      $t9, $t8, 0x5
    /* 1EED4C 151C189C A7B9004A */  sh         $t9, 0x4A($sp)
    /* 1EED50 151C18A0 A3A0004C */  sb         $zero, 0x4C($sp)
    /* 1EED54 151C18A4 C4840000 */  lwc1       $f4, 0x0($a0)
    /* 1EED58 151C18A8 4600218D */  trunc.w.s  $f6, $f4
    /* 1EED5C 151C18AC 44093000 */  mfc1       $t1, $f6
    /* 1EED60 151C18B0 00000000 */  nop
    /* 1EED64 151C18B4 AFA9003C */  sw         $t1, 0x3C($sp)
    /* 1EED68 151C18B8 C4880004 */  lwc1       $f8, 0x4($a0)
    /* 1EED6C 151C18BC 4600428D */  trunc.w.s  $f10, $f8
    /* 1EED70 151C18C0 440B5000 */  mfc1       $t3, $f10
    /* 1EED74 151C18C4 00000000 */  nop
    /* 1EED78 151C18C8 AFAB0040 */  sw         $t3, 0x40($sp)
    /* 1EED7C 151C18CC C4900008 */  lwc1       $f16, 0x8($a0)
    /* 1EED80 151C18D0 4600848D */  trunc.w.s  $f18, $f16
    /* 1EED84 151C18D4 440D9000 */  mfc1       $t5, $f18
    /* 1EED88 151C18D8 0D42B688 */  jal        func_150ADA20
    /* 1EED8C 151C18DC AFAD0044 */   sw        $t5, 0x44($sp)
    /* 1EED90 151C18E0 2401000B */  addiu      $at, $zero, 0xB
    /* 1EED94 151C18E4 0041001B */  divu       $zero, $v0, $at
    /* 1EED98 151C18E8 93B90057 */  lbu        $t9, 0x57($sp)
    /* 1EED9C 151C18EC 8FA80058 */  lw         $t0, 0x58($sp)
    /* 1EEDA0 151C18F0 00003010 */  mfhi       $a2
    /* 1EEDA4 151C18F4 240E00FF */  addiu      $t6, $zero, 0xFF
    /* 1EEDA8 151C18F8 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 1EEDAC 151C18FC 241800FF */  addiu      $t8, $zero, 0xFF
    /* 1EEDB0 151C1900 AFB80018 */  sw         $t8, 0x18($sp)
    /* 1EEDB4 151C1904 AFAF0014 */  sw         $t7, 0x14($sp)
    /* 1EEDB8 151C1908 AFAE0010 */  sw         $t6, 0x10($sp)
    /* 1EEDBC 151C190C 24C60005 */  addiu      $a2, $a2, 0x5
    /* 1EEDC0 151C1910 27A40048 */  addiu      $a0, $sp, 0x48
    /* 1EEDC4 151C1914 27A5003C */  addiu      $a1, $sp, 0x3C
    /* 1EEDC8 151C1918 240700FF */  addiu      $a3, $zero, 0xFF
    /* 1EEDCC 151C191C AFA0001C */  sw         $zero, 0x1C($sp)
    /* 1EEDD0 151C1920 AFA00020 */  sw         $zero, 0x20($sp)
    /* 1EEDD4 151C1924 AFB90024 */  sw         $t9, 0x24($sp)
    /* 1EEDD8 151C1928 0D4580B0 */  jal        func_151602C0
    /* 1EEDDC 151C192C AFA80028 */   sw        $t0, 0x28($sp)
    /* 1EEDE0 151C1930 8FBF0034 */  lw         $ra, 0x34($sp)
    /* 1EEDE4 151C1934 27BD0050 */  addiu      $sp, $sp, 0x50
    /* 1EEDE8 151C1938 03E00008 */  jr         $ra
    /* 1EEDEC 151C193C 00000000 */   nop
endlabel func_151C1860
