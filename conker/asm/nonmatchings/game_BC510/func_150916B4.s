glabel func_150916B4
    /* BEB64 150916B4 27BDFFB8 */  addiu      $sp, $sp, -0x48
    /* BEB68 150916B8 AFB20028 */  sw         $s2, 0x28($sp)
    /* BEB6C 150916BC AFB10024 */  sw         $s1, 0x24($sp)
    /* BEB70 150916C0 3C020005 */  lui        $v0, (0x57030 >> 16)
    /* BEB74 150916C4 34427030 */  ori        $v0, $v0, (0x57030 & 0xFFFF)
    /* BEB78 150916C8 00808825 */  or         $s1, $a0, $zero
    /* BEB7C 150916CC 00A09025 */  or         $s2, $a1, $zero
    /* BEB80 150916D0 AFBF002C */  sw         $ra, 0x2C($sp)
    /* BEB84 150916D4 AFB00020 */  sw         $s0, 0x20($sp)
    /* BEB88 150916D8 AFA70054 */  sw         $a3, 0x54($sp)
    /* BEB8C 150916DC 00C2082A */  slt        $at, $a2, $v0
    /* BEB90 150916E0 14200002 */  bnez       $at, .L150916EC
    /* BEB94 150916E4 2409003C */   addiu     $t1, $zero, 0x3C
    /* BEB98 150916E8 00403025 */  or         $a2, $v0, $zero
  .L150916EC:
    /* BEB9C 150916EC 00C9001A */  div        $zero, $a2, $t1
    /* BEBA0 150916F0 00007010 */  mfhi       $t6
    /* BEBA4 150916F4 000E7880 */  sll        $t7, $t6, 2
    /* BEBA8 150916F8 01EE7823 */  subu       $t7, $t7, $t6
    /* BEBAC 150916FC 000F78C0 */  sll        $t7, $t7, 3
    /* BEBB0 15091700 01EE7821 */  addu       $t7, $t7, $t6
    /* BEBB4 15091704 000F7880 */  sll        $t7, $t7, 2
    /* BEBB8 15091708 01E9001A */  div        $zero, $t7, $t1
    /* BEBBC 1509170C 15200002 */  bnez       $t1, .L15091718
    /* BEBC0 15091710 00000000 */   nop
    /* BEBC4 15091714 0007000D */  break      7
  .L15091718:
    /* BEBC8 15091718 2401FFFF */  addiu      $at, $zero, -0x1
    /* BEBCC 1509171C 15210004 */  bne        $t1, $at, .L15091730
    /* BEBD0 15091720 3C018000 */   lui       $at, (0x80000000 >> 16)
    /* BEBD4 15091724 14C10002 */  bne        $a2, $at, .L15091730
    /* BEBD8 15091728 00000000 */   nop
    /* BEBDC 1509172C 0006000D */  break      6
  .L15091730:
    /* BEBE0 15091730 00001012 */  mflo       $v0
    /* BEBE4 15091734 00405025 */  or         $t2, $v0, $zero
    /* BEBE8 15091738 15200002 */  bnez       $t1, .L15091744
    /* BEBEC 1509173C 00000000 */   nop
    /* BEBF0 15091740 0007000D */  break      7
  .L15091744:
    /* BEBF4 15091744 2401FFFF */  addiu      $at, $zero, -0x1
    /* BEBF8 15091748 15210004 */  bne        $t1, $at, .L1509175C
    /* BEBFC 1509174C 3C018000 */   lui       $at, (0x80000000 >> 16)
    /* BEC00 15091750 15E10002 */  bne        $t7, $at, .L1509175C
    /* BEC04 15091754 00000000 */   nop
    /* BEC08 15091758 0006000D */  break      6
  .L1509175C:
    /* BEC0C 1509175C 28410064 */  slti       $at, $v0, 0x64
    /* BEC10 15091760 14200002 */  bnez       $at, .L1509176C
    /* BEC14 15091764 02402825 */   or        $a1, $s2, $zero
    /* BEC18 15091768 240A0063 */  addiu      $t2, $zero, 0x63
  .L1509176C:
    /* BEC1C 1509176C 04C00046 */  bltz       $a2, .L15091888
    /* BEC20 15091770 2631FFF8 */   addiu     $s1, $s1, -0x8
    /* BEC24 15091774 00C9001A */  div        $zero, $a2, $t1
    /* BEC28 15091778 00001012 */  mflo       $v0
    /* BEC2C 1509177C 93B00057 */  lbu        $s0, 0x57($sp)
    /* BEC30 15091780 15200002 */  bnez       $t1, .L1509178C
    /* BEC34 15091784 00000000 */   nop
    /* BEC38 15091788 0007000D */  break      7
  .L1509178C:
    /* BEC3C 1509178C 2401FFFF */  addiu      $at, $zero, -0x1
    /* BEC40 15091790 15210004 */  bne        $t1, $at, .L150917A4
    /* BEC44 15091794 3C018000 */   lui       $at, (0x80000000 >> 16)
    /* BEC48 15091798 14C10002 */  bne        $a2, $at, .L150917A4
    /* BEC4C 1509179C 00000000 */   nop
    /* BEC50 150917A0 0006000D */  break      6
  .L150917A4:
    /* BEC54 150917A4 0049001A */  div        $zero, $v0, $t1
    /* BEC58 150917A8 15200002 */  bnez       $t1, .L150917B4
    /* BEC5C 150917AC 00000000 */   nop
    /* BEC60 150917B0 0007000D */  break      7
  .L150917B4:
    /* BEC64 150917B4 2401FFFF */  addiu      $at, $zero, -0x1
    /* BEC68 150917B8 15210004 */  bne        $t1, $at, .L150917CC
    /* BEC6C 150917BC 3C018000 */   lui       $at, (0x80000000 >> 16)
    /* BEC70 150917C0 14410002 */  bne        $v0, $at, .L150917CC
    /* BEC74 150917C4 00000000 */   nop
    /* BEC78 150917C8 0006000D */  break      6
  .L150917CC:
    /* BEC7C 150917CC 00001812 */  mflo       $v1
    /* BEC80 150917D0 2861000A */  slti       $at, $v1, 0xA
    /* BEC84 150917D4 14200003 */  bnez       $at, .L150917E4
    /* BEC88 150917D8 02003025 */   or        $a2, $s0, $zero
    /* BEC8C 150917DC 10000002 */  b          .L150917E8
    /* BEC90 150917E0 24080005 */   addiu     $t0, $zero, 0x5
  .L150917E4:
    /* BEC94 150917E4 00004025 */  or         $t0, $zero, $zero
  .L150917E8:
    /* BEC98 150917E8 02282023 */  subu       $a0, $s1, $t0
    /* BEC9C 150917EC 3C07800A */  lui        $a3, %hi(D_8009DCC0)
    /* BECA0 150917F0 24E7DCC0 */  addiu      $a3, $a3, %lo(D_8009DCC0)
    /* BECA4 150917F4 2484FFF8 */  addiu      $a0, $a0, -0x8
    /* BECA8 150917F8 AFA30010 */  sw         $v1, 0x10($sp)
    /* BECAC 150917FC AFA20030 */  sw         $v0, 0x30($sp)
    /* BECB0 15091800 0D410B65 */  jal        func_15042D94
    /* BECB4 15091804 AFAA0038 */   sw        $t2, 0x38($sp)
    /* BECB8 15091808 8FA20030 */  lw         $v0, 0x30($sp)
    /* BECBC 1509180C 2409003C */  addiu      $t1, $zero, 0x3C
    /* BECC0 15091810 3C07800A */  lui        $a3, %hi(D_8009DCC4)
    /* BECC4 15091814 0049001A */  div        $zero, $v0, $t1
    /* BECC8 15091818 0000C010 */  mfhi       $t8
    /* BECCC 1509181C 8FAA0038 */  lw         $t2, 0x38($sp)
    /* BECD0 15091820 AFB80010 */  sw         $t8, 0x10($sp)
    /* BECD4 15091824 24E7DCC4 */  addiu      $a3, $a3, %lo(D_8009DCC4)
    /* BECD8 15091828 02202025 */  or         $a0, $s1, $zero
    /* BECDC 1509182C 02402825 */  or         $a1, $s2, $zero
    /* BECE0 15091830 320600FF */  andi       $a2, $s0, 0xFF
    /* BECE4 15091834 15200002 */  bnez       $t1, .L15091840
    /* BECE8 15091838 00000000 */   nop
    /* BECEC 1509183C 0007000D */  break      7
  .L15091840:
    /* BECF0 15091840 2401FFFF */  addiu      $at, $zero, -0x1
    /* BECF4 15091844 15210004 */  bne        $t1, $at, .L15091858
    /* BECF8 15091848 3C018000 */   lui       $at, (0x80000000 >> 16)
    /* BECFC 1509184C 14410002 */  bne        $v0, $at, .L15091858
    /* BED00 15091850 00000000 */   nop
    /* BED04 15091854 0006000D */  break      6
  .L15091858:
    /* BED08 15091858 0D410B65 */  jal        func_15042D94
    /* BED0C 1509185C 00000000 */   nop
    /* BED10 15091860 8FAA0038 */  lw         $t2, 0x38($sp)
    /* BED14 15091864 3C07800A */  lui        $a3, %hi(D_8009DCCC)
    /* BED18 15091868 24E7DCCC */  addiu      $a3, $a3, %lo(D_8009DCCC)
    /* BED1C 1509186C 26240010 */  addiu      $a0, $s1, 0x10
    /* BED20 15091870 02402825 */  or         $a1, $s2, $zero
    /* BED24 15091874 320600FF */  andi       $a2, $s0, 0xFF
    /* BED28 15091878 0D410B65 */  jal        func_15042D94
    /* BED2C 1509187C AFAA0010 */   sw        $t2, 0x10($sp)
    /* BED30 15091880 10000015 */  b          .L150918D8
    /* BED34 15091884 8FBF002C */   lw        $ra, 0x2C($sp)
  .L15091888:
    /* BED38 15091888 93B00057 */  lbu        $s0, 0x57($sp)
    /* BED3C 1509188C 3C07800A */  lui        $a3, %hi(D_8009DCD4)
    /* BED40 15091890 24E7DCD4 */  addiu      $a3, $a3, %lo(D_8009DCD4)
    /* BED44 15091894 2624FFF8 */  addiu      $a0, $s1, -0x8
    /* BED48 15091898 02402825 */  or         $a1, $s2, $zero
    /* BED4C 1509189C 0D410B65 */  jal        func_15042D94
    /* BED50 150918A0 02003025 */   or        $a2, $s0, $zero
    /* BED54 150918A4 3C07800A */  lui        $a3, %hi(D_8009DCD8)
    /* BED58 150918A8 24E7DCD8 */  addiu      $a3, $a3, %lo(D_8009DCD8)
    /* BED5C 150918AC 02202025 */  or         $a0, $s1, $zero
    /* BED60 150918B0 02402825 */  or         $a1, $s2, $zero
    /* BED64 150918B4 0D410B65 */  jal        func_15042D94
    /* BED68 150918B8 320600FF */   andi      $a2, $s0, 0xFF
    /* BED6C 150918BC 3C07800A */  lui        $a3, %hi(D_8009DCE0)
    /* BED70 150918C0 24E7DCE0 */  addiu      $a3, $a3, %lo(D_8009DCE0)
    /* BED74 150918C4 26240010 */  addiu      $a0, $s1, 0x10
    /* BED78 150918C8 02402825 */  or         $a1, $s2, $zero
    /* BED7C 150918CC 0D410B65 */  jal        func_15042D94
    /* BED80 150918D0 320600FF */   andi      $a2, $s0, 0xFF
    /* BED84 150918D4 8FBF002C */  lw         $ra, 0x2C($sp)
  .L150918D8:
    /* BED88 150918D8 8FB00020 */  lw         $s0, 0x20($sp)
    /* BED8C 150918DC 8FB10024 */  lw         $s1, 0x24($sp)
    /* BED90 150918E0 8FB20028 */  lw         $s2, 0x28($sp)
    /* BED94 150918E4 03E00008 */  jr         $ra
    /* BED98 150918E8 27BD0048 */   addiu     $sp, $sp, 0x48
endlabel func_150916B4
