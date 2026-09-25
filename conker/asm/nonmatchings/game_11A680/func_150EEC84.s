glabel func_150EEC84
    /* 11C134 150EEC84 27BDFFC8 */  addiu      $sp, $sp, -0x38
    /* 11C138 150EEC88 AFBF0024 */  sw         $ra, 0x24($sp)
    /* 11C13C 150EEC8C AFB00020 */  sw         $s0, 0x20($sp)
    /* 11C140 150EEC90 00803025 */  or         $a2, $a0, $zero
    /* 11C144 150EEC94 8CC20318 */  lw         $v0, 0x318($a2)
    /* 11C148 150EEC98 240E0003 */  addiu      $t6, $zero, 0x3
    /* 11C14C 150EEC9C 240F00FF */  addiu      $t7, $zero, 0xFF
    /* 11C150 150EECA0 A0CE0005 */  sb         $t6, 0x5($a2)
    /* 11C154 150EECA4 A4C000E4 */  sh         $zero, 0xE4($a2)
    /* 11C158 150EECA8 A0CF0125 */  sb         $t7, 0x125($a2)
    /* 11C15C 150EECAC 10400039 */  beqz       $v0, .L150EED94
    /* 11C160 150EECB0 A0C00328 */   sb        $zero, 0x328($a2)
    /* 11C164 150EECB4 9058023D */  lbu        $t8, 0x23D($v0)
    /* 11C168 150EECB8 24010003 */  addiu      $at, $zero, 0x3
    /* 11C16C 150EECBC 00408025 */  or         $s0, $v0, $zero
    /* 11C170 150EECC0 17010002 */  bne        $t8, $at, .L150EECCC
    /* 11C174 150EECC4 00002825 */   or        $a1, $zero, $zero
    /* 11C178 150EECC8 24050001 */  addiu      $a1, $zero, 0x1
  .L150EECCC:
    /* 11C17C 150EECCC 02002025 */  or         $a0, $s0, $zero
    /* 11C180 150EECD0 AFA5002C */  sw         $a1, 0x2C($sp)
    /* 11C184 150EECD4 0D44953D */  jal        func_151254F4
    /* 11C188 150EECD8 AFA60038 */   sw        $a2, 0x38($sp)
    /* 11C18C 150EECDC 8FA5002C */  lw         $a1, 0x2C($sp)
    /* 11C190 150EECE0 8FA60038 */  lw         $a2, 0x38($sp)
    /* 11C194 150EECE4 3C0A800C */  lui        $t2, %hi(D_800BE748)
    /* 11C198 150EECE8 00054880 */  sll        $t1, $a1, 2
    /* 11C19C 150EECEC 8CC8031C */  lw         $t0, 0x31C($a2)
    /* 11C1A0 150EECF0 00056880 */  sll        $t5, $a1, 2
    /* 11C1A4 150EECF4 01254823 */  subu       $t1, $t1, $a1
    /* 11C1A8 150EECF8 01A56823 */  subu       $t5, $t5, $a1
    /* 11C1AC 150EECFC 24190029 */  addiu      $t9, $zero, 0x29
    /* 11C1B0 150EED00 00094840 */  sll        $t1, $t1, 1
    /* 11C1B4 150EED04 254AE748 */  addiu      $t2, $t2, %lo(D_800BE748)
    /* 11C1B8 150EED08 000D6880 */  sll        $t5, $t5, 2
    /* 11C1BC 150EED0C 012A1021 */  addu       $v0, $t1, $t2
    /* 11C1C0 150EED10 01A56821 */  addu       $t5, $t5, $a1
    /* 11C1C4 150EED14 A1190078 */  sb         $t9, 0x78($t0)
    /* 11C1C8 150EED18 944B0000 */  lhu        $t3, 0x0($v0)
    /* 11C1CC 150EED1C 000D6880 */  sll        $t5, $t5, 2
    /* 11C1D0 150EED20 01A56823 */  subu       $t5, $t5, $a1
    /* 11C1D4 150EED24 000D6880 */  sll        $t5, $t5, 2
    /* 11C1D8 150EED28 3C0E800D */  lui        $t6, %hi(D_800CC2D0)
    /* 11C1DC 150EED2C 01A56823 */  subu       $t5, $t5, $a1
    /* 11C1E0 150EED30 316CFFEF */  andi       $t4, $t3, 0xFFEF
    /* 11C1E4 150EED34 A44C0000 */  sh         $t4, 0x0($v0)
    /* 11C1E8 150EED38 000D6880 */  sll        $t5, $t5, 2
    /* 11C1EC 150EED3C 25CEC2D0 */  addiu      $t6, $t6, %lo(D_800CC2D0)
    /* 11C1F0 150EED40 9218023D */  lbu        $t8, 0x23D($s0)
    /* 11C1F4 150EED44 01AE1821 */  addu       $v1, $t5, $t6
    /* 11C1F8 150EED48 906F02FC */  lbu        $t7, 0x2FC($v1)
    /* 11C1FC 150EED4C 906A010A */  lbu        $t2, 0x10A($v1)
    /* 11C200 150EED50 24190001 */  addiu      $t9, $zero, 0x1
    /* 11C204 150EED54 03194004 */  sllv       $t0, $t9, $t8
    /* 11C208 150EED58 01E84825 */  or         $t1, $t7, $t0
    /* 11C20C 150EED5C 1140000D */  beqz       $t2, .L150EED94
    /* 11C210 150EED60 A06902FC */   sb        $t1, 0x2FC($v1)
    /* 11C214 150EED64 240B0014 */  addiu      $t3, $zero, 0x14
    /* 11C218 150EED68 AFAB0010 */  sw         $t3, 0x10($sp)
    /* 11C21C 150EED6C 920C023D */  lbu        $t4, 0x23D($s0)
    /* 11C220 150EED70 AFA30028 */  sw         $v1, 0x28($sp)
    /* 11C224 150EED74 240400FF */  addiu      $a0, $zero, 0xFF
    /* 11C228 150EED78 00002825 */  or         $a1, $zero, $zero
    /* 11C22C 150EED7C 00003025 */  or         $a2, $zero, $zero
    /* 11C230 150EED80 240700B4 */  addiu      $a3, $zero, 0xB4
    /* 11C234 150EED84 0D45FD22 */  jal        func_1517F488
    /* 11C238 150EED88 AFAC0014 */   sw        $t4, 0x14($sp)
    /* 11C23C 150EED8C 8FA30028 */  lw         $v1, 0x28($sp)
    /* 11C240 150EED90 A060010A */  sb         $zero, 0x10A($v1)
  .L150EED94:
    /* 11C244 150EED94 8FBF0024 */  lw         $ra, 0x24($sp)
    /* 11C248 150EED98 8FB00020 */  lw         $s0, 0x20($sp)
    /* 11C24C 150EED9C 27BD0038 */  addiu      $sp, $sp, 0x38
    /* 11C250 150EEDA0 03E00008 */  jr         $ra
    /* 11C254 150EEDA4 00000000 */   nop
endlabel func_150EEC84
