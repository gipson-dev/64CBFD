glabel func_151C0698
    /* 1EDB48 151C0698 27BDFCF8 */  addiu      $sp, $sp, -0x308
    /* 1EDB4C 151C069C AFB00040 */  sw         $s0, 0x40($sp)
    /* 1EDB50 151C06A0 00808025 */  or         $s0, $a0, $zero
    /* 1EDB54 151C06A4 AFBF0044 */  sw         $ra, 0x44($sp)
    /* 1EDB58 151C06A8 AFA5030C */  sw         $a1, 0x30C($sp)
    /* 1EDB5C 151C06AC AFA60310 */  sw         $a2, 0x310($sp)
    /* 1EDB60 151C06B0 AFA70314 */  sw         $a3, 0x314($sp)
    /* 1EDB64 151C06B4 3C0E800C */  lui        $t6, %hi(D_800BE616)
    /* 1EDB68 151C06B8 91CEE616 */  lbu        $t6, %lo(D_800BE616)($t6)
    /* 1EDB6C 151C06BC 44802000 */  mtc1       $zero, $f4
    /* 1EDB70 151C06C0 11C00013 */  beqz       $t6, .L151C0710
    /* 1EDB74 151C06C4 E7A402A0 */   swc1      $f4, 0x2A0($sp)
    /* 1EDB78 151C06C8 8E0F01D4 */  lw         $t7, 0x1D4($s0)
    /* 1EDB7C 151C06CC 02002025 */  or         $a0, $s0, $zero
    /* 1EDB80 151C06D0 51E00006 */  beql       $t7, $zero, .L151C06EC
    /* 1EDB84 151C06D4 C6060014 */   lwc1      $f6, 0x14($s0)
    /* 1EDB88 151C06D8 0D4705E6 */  jal        func_151C1798
    /* 1EDB8C 151C06DC 27A50260 */   addiu     $a1, $sp, 0x260
    /* 1EDB90 151C06E0 1000005F */  b          .L151C0860
    /* 1EDB94 151C06E4 8E02031C */   lw        $v0, 0x31C($s0)
    /* 1EDB98 151C06E8 C6060014 */  lwc1       $f6, 0x14($s0)
  .L151C06EC:
    /* 1EDB9C 151C06EC 3C014282 */  lui        $at, (0x42820000 >> 16)
    /* 1EDBA0 151C06F0 44815000 */  mtc1       $at, $f10
    /* 1EDBA4 151C06F4 E7A60260 */  swc1       $f6, 0x260($sp)
    /* 1EDBA8 151C06F8 C6080018 */  lwc1       $f8, 0x18($s0)
    /* 1EDBAC 151C06FC 460A4400 */  add.s      $f16, $f8, $f10
    /* 1EDBB0 151C0700 E7B00264 */  swc1       $f16, 0x264($sp)
    /* 1EDBB4 151C0704 C612001C */  lwc1       $f18, 0x1C($s0)
    /* 1EDBB8 151C0708 10000054 */  b          .L151C085C
    /* 1EDBBC 151C070C E7B20268 */   swc1      $f18, 0x268($sp)
  .L151C0710:
    /* 1EDBC0 151C0710 8E050318 */  lw         $a1, 0x318($s0)
    /* 1EDBC4 151C0714 8E02031C */  lw         $v0, 0x31C($s0)
    /* 1EDBC8 151C0718 10A0003F */  beqz       $a1, .L151C0818
    /* 1EDBCC 151C071C 2443013C */   addiu     $v1, $v0, 0x13C
    /* 1EDBD0 151C0720 92180065 */  lbu        $t8, 0x65($s0)
    /* 1EDBD4 151C0724 5300000C */  beql       $t8, $zero, .L151C0758
    /* 1EDBD8 151C0728 90590197 */   lbu       $t9, 0x197($v0)
    /* 1EDBDC 151C072C C4640000 */  lwc1       $f4, 0x0($v1)
    /* 1EDBE0 151C0730 3C01C150 */  lui        $at, (0xC1500000 >> 16)
    /* 1EDBE4 151C0734 44814000 */  mtc1       $at, $f8
    /* 1EDBE8 151C0738 E7A40260 */  swc1       $f4, 0x260($sp)
    /* 1EDBEC 151C073C C4660004 */  lwc1       $f6, 0x4($v1)
    /* 1EDBF0 151C0740 46083280 */  add.s      $f10, $f6, $f8
    /* 1EDBF4 151C0744 E7AA0264 */  swc1       $f10, 0x264($sp)
    /* 1EDBF8 151C0748 C4700008 */  lwc1       $f16, 0x8($v1)
    /* 1EDBFC 151C074C 10000043 */  b          .L151C085C
    /* 1EDC00 151C0750 E7B00268 */   swc1      $f16, 0x268($sp)
    /* 1EDC04 151C0754 90590197 */  lbu        $t9, 0x197($v0)
  .L151C0758:
    /* 1EDC08 151C0758 5320001E */  beql       $t9, $zero, .L151C07D4
    /* 1EDC0C 151C075C 8E0901D4 */   lw        $t1, 0x1D4($s0)
    /* 1EDC10 151C0760 90A4023D */  lbu        $a0, 0x23D($a1)
    /* 1EDC14 151C0764 0D4512AA */  jal        func_15144AA8
    /* 1EDC18 151C0768 AFA30234 */   sw        $v1, 0x234($sp)
    /* 1EDC1C 151C076C 3C01800B */  lui        $at, %hi(D_800AA99C)
    /* 1EDC20 151C0770 C432A99C */  lwc1       $f18, %lo(D_800AA99C)($at)
    /* 1EDC24 151C0774 46120302 */  mul.s      $f12, $f0, $f18
    /* 1EDC28 151C0778 0D411F00 */  jal        cosf
    /* 1EDC2C 151C077C E7AC022C */   swc1      $f12, 0x22C($sp)
    /* 1EDC30 151C0780 3C0141C8 */  lui        $at, (0x41C80000 >> 16)
    /* 1EDC34 151C0784 44812000 */  mtc1       $at, $f4
    /* 1EDC38 151C0788 8FA30234 */  lw         $v1, 0x234($sp)
    /* 1EDC3C 151C078C C7AC022C */  lwc1       $f12, 0x22C($sp)
    /* 1EDC40 151C0790 46040182 */  mul.s      $f6, $f0, $f4
    /* 1EDC44 151C0794 C4680000 */  lwc1       $f8, 0x0($v1)
    /* 1EDC48 151C0798 46083280 */  add.s      $f10, $f6, $f8
    /* 1EDC4C 151C079C E7AA0260 */  swc1       $f10, 0x260($sp)
    /* 1EDC50 151C07A0 C4700004 */  lwc1       $f16, 0x4($v1)
    /* 1EDC54 151C07A4 0D411F58 */  jal        sinf
    /* 1EDC58 151C07A8 E7B00264 */   swc1      $f16, 0x264($sp)
    /* 1EDC5C 151C07AC 3C0141C8 */  lui        $at, (0x41C80000 >> 16)
    /* 1EDC60 151C07B0 44812000 */  mtc1       $at, $f4
    /* 1EDC64 151C07B4 8FA30234 */  lw         $v1, 0x234($sp)
    /* 1EDC68 151C07B8 46040182 */  mul.s      $f6, $f0, $f4
    /* 1EDC6C 151C07BC C4720008 */  lwc1       $f18, 0x8($v1)
    /* 1EDC70 151C07C0 46069201 */  sub.s      $f8, $f18, $f6
    /* 1EDC74 151C07C4 E7A80268 */  swc1       $f8, 0x268($sp)
    /* 1EDC78 151C07C8 10000025 */  b          .L151C0860
    /* 1EDC7C 151C07CC 8E02031C */   lw        $v0, 0x31C($s0)
    /* 1EDC80 151C07D0 8E0901D4 */  lw         $t1, 0x1D4($s0)
  .L151C07D4:
    /* 1EDC84 151C07D4 02002025 */  or         $a0, $s0, $zero
    /* 1EDC88 151C07D8 51200006 */  beql       $t1, $zero, .L151C07F4
    /* 1EDC8C 151C07DC C60A0014 */   lwc1      $f10, 0x14($s0)
    /* 1EDC90 151C07E0 0D4705E6 */  jal        func_151C1798
    /* 1EDC94 151C07E4 27A50260 */   addiu     $a1, $sp, 0x260
    /* 1EDC98 151C07E8 1000001D */  b          .L151C0860
    /* 1EDC9C 151C07EC 8E02031C */   lw        $v0, 0x31C($s0)
    /* 1EDCA0 151C07F0 C60A0014 */  lwc1       $f10, 0x14($s0)
  .L151C07F4:
    /* 1EDCA4 151C07F4 3C014282 */  lui        $at, (0x42820000 >> 16)
    /* 1EDCA8 151C07F8 44812000 */  mtc1       $at, $f4
    /* 1EDCAC 151C07FC E7AA0260 */  swc1       $f10, 0x260($sp)
    /* 1EDCB0 151C0800 C6100018 */  lwc1       $f16, 0x18($s0)
    /* 1EDCB4 151C0804 46048480 */  add.s      $f18, $f16, $f4
    /* 1EDCB8 151C0808 E7B20264 */  swc1       $f18, 0x264($sp)
    /* 1EDCBC 151C080C C606001C */  lwc1       $f6, 0x1C($s0)
    /* 1EDCC0 151C0810 10000012 */  b          .L151C085C
    /* 1EDCC4 151C0814 E7A60268 */   swc1      $f6, 0x268($sp)
  .L151C0818:
    /* 1EDCC8 151C0818 8E0A01D4 */  lw         $t2, 0x1D4($s0)
    /* 1EDCCC 151C081C 02002025 */  or         $a0, $s0, $zero
    /* 1EDCD0 151C0820 51400006 */  beql       $t2, $zero, .L151C083C
    /* 1EDCD4 151C0824 C6080014 */   lwc1      $f8, 0x14($s0)
    /* 1EDCD8 151C0828 0D4705E6 */  jal        func_151C1798
    /* 1EDCDC 151C082C 27A50260 */   addiu     $a1, $sp, 0x260
    /* 1EDCE0 151C0830 1000000B */  b          .L151C0860
    /* 1EDCE4 151C0834 8E02031C */   lw        $v0, 0x31C($s0)
    /* 1EDCE8 151C0838 C6080014 */  lwc1       $f8, 0x14($s0)
  .L151C083C:
    /* 1EDCEC 151C083C 3C014282 */  lui        $at, (0x42820000 >> 16)
    /* 1EDCF0 151C0840 44818000 */  mtc1       $at, $f16
    /* 1EDCF4 151C0844 E7A80260 */  swc1       $f8, 0x260($sp)
    /* 1EDCF8 151C0848 C60A0018 */  lwc1       $f10, 0x18($s0)
    /* 1EDCFC 151C084C 46105100 */  add.s      $f4, $f10, $f16
    /* 1EDD00 151C0850 E7A40264 */  swc1       $f4, 0x264($sp)
    /* 1EDD04 151C0854 C612001C */  lwc1       $f18, 0x1C($s0)
    /* 1EDD08 151C0858 E7B20268 */  swc1       $f18, 0x268($sp)
  .L151C085C:
    /* 1EDD0C 151C085C 8E02031C */  lw         $v0, 0x31C($s0)
  .L151C0860:
    /* 1EDD10 151C0860 8FAC030C */  lw         $t4, 0x30C($sp)
    /* 1EDD14 151C0864 10400004 */  beqz       $v0, .L151C0878
    /* 1EDD18 151C0868 00000000 */   nop
    /* 1EDD1C 151C086C 904B0197 */  lbu        $t3, 0x197($v0)
    /* 1EDD20 151C0870 55600004 */  bnel       $t3, $zero, .L151C0884
    /* 1EDD24 151C0874 8FAD030C */   lw        $t5, 0x30C($sp)
  .L151C0878:
    /* 1EDD28 151C0878 1180001C */  beqz       $t4, .L151C08EC
    /* 1EDD2C 151C087C 02002025 */   or        $a0, $s0, $zero
    /* 1EDD30 151C0880 8FAD030C */  lw         $t5, 0x30C($sp)
  .L151C0884:
    /* 1EDD34 151C0884 02001025 */  or         $v0, $s0, $zero
    /* 1EDD38 151C0888 11A00003 */  beqz       $t5, .L151C0898
    /* 1EDD3C 151C088C 00000000 */   nop
    /* 1EDD40 151C0890 10000001 */  b          .L151C0898
    /* 1EDD44 151C0894 01A01025 */   or        $v0, $t5, $zero
  .L151C0898:
    /* 1EDD48 151C0898 8C43031C */  lw         $v1, 0x31C($v0)
    /* 1EDD4C 151C089C 27AE0248 */  addiu      $t6, $sp, 0x248
    /* 1EDD50 151C08A0 24080001 */  addiu      $t0, $zero, 0x1
    /* 1EDD54 151C08A4 8C61013C */  lw         $at, 0x13C($v1)
    /* 1EDD58 151C08A8 2463013C */  addiu      $v1, $v1, 0x13C
    /* 1EDD5C 151C08AC ADC10000 */  sw         $at, 0x0($t6)
    /* 1EDD60 151C08B0 8C780004 */  lw         $t8, 0x4($v1)
    /* 1EDD64 151C08B4 ADD80004 */  sw         $t8, 0x4($t6)
    /* 1EDD68 151C08B8 8C610008 */  lw         $at, 0x8($v1)
    /* 1EDD6C 151C08BC ADC10008 */  sw         $at, 0x8($t6)
    /* 1EDD70 151C08C0 8C59031C */  lw         $t9, 0x31C($v0)
    /* 1EDD74 151C08C4 C7260130 */  lwc1       $f6, 0x130($t9)
    /* 1EDD78 151C08C8 E7A6023C */  swc1       $f6, 0x23C($sp)
    /* 1EDD7C 151C08CC 8C49031C */  lw         $t1, 0x31C($v0)
    /* 1EDD80 151C08D0 C5280134 */  lwc1       $f8, 0x134($t1)
    /* 1EDD84 151C08D4 E7A80240 */  swc1       $f8, 0x240($sp)
    /* 1EDD88 151C08D8 8C4A031C */  lw         $t2, 0x31C($v0)
    /* 1EDD8C 151C08DC C54A0138 */  lwc1       $f10, 0x138($t2)
    /* 1EDD90 151C08E0 E7AA0244 */  swc1       $f10, 0x244($sp)
    /* 1EDD94 151C08E4 10000014 */  b          .L151C0938
    /* 1EDD98 151C08E8 00000000 */   nop
  .L151C08EC:
    /* 1EDD9C 151C08EC 44808000 */  mtc1       $zero, $f16
    /* 1EDDA0 151C08F0 27A50254 */  addiu      $a1, $sp, 0x254
    /* 1EDDA4 151C08F4 27A60218 */  addiu      $a2, $sp, 0x218
    /* 1EDDA8 151C08F8 00003825 */  or         $a3, $zero, $zero
    /* 1EDDAC 151C08FC 0D4515D0 */  jal        func_15145740
    /* 1EDDB0 151C0900 E7B00010 */   swc1      $f16, 0x10($sp)
    /* 1EDDB4 151C0904 3C01800B */  lui        $at, %hi(D_800AA9A0)
    /* 1EDDB8 151C0908 C420A9A0 */  lwc1       $f0, %lo(D_800AA9A0)($at)
    /* 1EDDBC 151C090C C7A40254 */  lwc1       $f4, 0x254($sp)
    /* 1EDDC0 151C0910 C7A60258 */  lwc1       $f6, 0x258($sp)
    /* 1EDDC4 151C0914 C7AA025C */  lwc1       $f10, 0x25C($sp)
    /* 1EDDC8 151C0918 46002482 */  mul.s      $f18, $f4, $f0
    /* 1EDDCC 151C091C 00004025 */  or         $t0, $zero, $zero
    /* 1EDDD0 151C0920 46003202 */  mul.s      $f8, $f6, $f0
    /* 1EDDD4 151C0924 00000000 */  nop
    /* 1EDDD8 151C0928 46005402 */  mul.s      $f16, $f10, $f0
    /* 1EDDDC 151C092C E7B20254 */  swc1       $f18, 0x254($sp)
    /* 1EDDE0 151C0930 E7A80258 */  swc1       $f8, 0x258($sp)
    /* 1EDDE4 151C0934 E7B0025C */  swc1       $f16, 0x25C($sp)
  .L151C0938:
    /* 1EDDE8 151C0938 3C0B800C */  lui        $t3, %hi(D_800BE9F0)
    /* 1EDDEC 151C093C 8D6BE9F0 */  lw         $t3, %lo(D_800BE9F0)($t3)
    /* 1EDDF0 151C0940 24010024 */  addiu      $at, $zero, 0x24
    /* 1EDDF4 151C0944 02003025 */  or         $a2, $s0, $zero
    /* 1EDDF8 151C0948 15610003 */  bne        $t3, $at, .L151C0958
    /* 1EDDFC 151C094C 24070003 */   addiu     $a3, $zero, 0x3
    /* 1EDE00 151C0950 10000015 */  b          .L151C09A8
    /* 1EDE04 151C0954 00001825 */   or        $v1, $zero, $zero
  .L151C0958:
    /* 1EDE08 151C0958 11000004 */  beqz       $t0, .L151C096C
    /* 1EDE0C 151C095C 27AD0260 */   addiu     $t5, $sp, 0x260
    /* 1EDE10 151C0960 27AC0248 */  addiu      $t4, $sp, 0x248
    /* 1EDE14 151C0964 10000002 */  b          .L151C0970
    /* 1EDE18 151C0968 AFAC0054 */   sw        $t4, 0x54($sp)
  .L151C096C:
    /* 1EDE1C 151C096C AFAD0054 */  sw         $t5, 0x54($sp)
  .L151C0970:
    /* 1EDE20 151C0970 11000004 */  beqz       $t0, .L151C0984
    /* 1EDE24 151C0974 27AE0254 */   addiu     $t6, $sp, 0x254
    /* 1EDE28 151C0978 27AF023C */  addiu      $t7, $sp, 0x23C
    /* 1EDE2C 151C097C 10000002 */  b          .L151C0988
    /* 1EDE30 151C0980 AFAF0058 */   sw        $t7, 0x58($sp)
  .L151C0984:
    /* 1EDE34 151C0984 AFAE0058 */  sw         $t6, 0x58($sp)
  .L151C0988:
    /* 1EDE38 151C0988 8FB80310 */  lw         $t8, 0x310($sp)
    /* 1EDE3C 151C098C 8FA40054 */  lw         $a0, 0x54($sp)
    /* 1EDE40 151C0990 8FA50058 */  lw         $a1, 0x58($sp)
    /* 1EDE44 151C0994 A3A8026F */  sb         $t0, 0x26F($sp)
    /* 1EDE48 151C0998 0D4756DB */  jal        func_151D5B6C
    /* 1EDE4C 151C099C AFB80010 */   sw        $t8, 0x10($sp)
    /* 1EDE50 151C09A0 93A8026F */  lbu        $t0, 0x26F($sp)
    /* 1EDE54 151C09A4 00401825 */  or         $v1, $v0, $zero
  .L151C09A8:
    /* 1EDE58 151C09A8 11000003 */  beqz       $t0, .L151C09B8
    /* 1EDE5C 151C09AC 27A402A4 */   addiu     $a0, $sp, 0x2A4
    /* 1EDE60 151C09B0 10000002 */  b          .L151C09BC
    /* 1EDE64 151C09B4 00003025 */   or        $a2, $zero, $zero
  .L151C09B8:
    /* 1EDE68 151C09B8 27A60254 */  addiu      $a2, $sp, 0x254
  .L151C09BC:
    /* 1EDE6C 151C09BC 11000004 */  beqz       $t0, .L151C09D0
    /* 1EDE70 151C09C0 27A50260 */   addiu     $a1, $sp, 0x260
    /* 1EDE74 151C09C4 27B90248 */  addiu      $t9, $sp, 0x248
    /* 1EDE78 151C09C8 10000002 */  b          .L151C09D4
    /* 1EDE7C 151C09CC AFB90054 */   sw        $t9, 0x54($sp)
  .L151C09D0:
    /* 1EDE80 151C09D0 AFA00054 */  sw         $zero, 0x54($sp)
  .L151C09D4:
    /* 1EDE84 151C09D4 11000004 */  beqz       $t0, .L151C09E8
    /* 1EDE88 151C09D8 27AC0294 */   addiu     $t4, $sp, 0x294
    /* 1EDE8C 151C09DC 27A9023C */  addiu      $t1, $sp, 0x23C
    /* 1EDE90 151C09E0 10000002 */  b          .L151C09EC
    /* 1EDE94 151C09E4 AFA90058 */   sw        $t1, 0x58($sp)
  .L151C09E8:
    /* 1EDE98 151C09E8 AFA00058 */  sw         $zero, 0x58($sp)
  .L151C09EC:
    /* 1EDE9C 151C09EC 8FAA0058 */  lw         $t2, 0x58($sp)
    /* 1EDEA0 151C09F0 8FAB0310 */  lw         $t3, 0x310($sp)
    /* 1EDEA4 151C09F4 27AD02A0 */  addiu      $t5, $sp, 0x2A0
    /* 1EDEA8 151C09F8 27AF0270 */  addiu      $t7, $sp, 0x270
    /* 1EDEAC 151C09FC AFAF0024 */  sw         $t7, 0x24($sp)
    /* 1EDEB0 151C0A00 AFAD0020 */  sw         $t5, 0x20($sp)
    /* 1EDEB4 151C0A04 8FA70054 */  lw         $a3, 0x54($sp)
    /* 1EDEB8 151C0A08 AFB00014 */  sw         $s0, 0x14($sp)
    /* 1EDEBC 151C0A0C AFAC001C */  sw         $t4, 0x1C($sp)
    /* 1EDEC0 151C0A10 AFA30028 */  sw         $v1, 0x28($sp)
    /* 1EDEC4 151C0A14 AFA30238 */  sw         $v1, 0x238($sp)
    /* 1EDEC8 151C0A18 AFAA0010 */  sw         $t2, 0x10($sp)
    /* 1EDECC 151C0A1C 0D47065B */  jal        func_151C196C
    /* 1EDED0 151C0A20 AFAB0018 */   sw        $t3, 0x18($sp)
    /* 1EDED4 151C0A24 104001B4 */  beqz       $v0, .L151C10F8
    /* 1EDED8 151C0A28 8FA30238 */   lw        $v1, 0x238($sp)
    /* 1EDEDC 151C0A2C 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 1EDEE0 151C0A30 44810000 */  mtc1       $at, $f0
    /* 1EDEE4 151C0A34 3C01800B */  lui        $at, %hi(D_800AA9A4)
    /* 1EDEE8 151C0A38 44806000 */  mtc1       $zero, $f12
    /* 1EDEEC 151C0A3C C422A9A4 */  lwc1       $f2, %lo(D_800AA9A4)($at)
    /* 1EDEF0 151C0A40 27B802A4 */  addiu      $t8, $sp, 0x2A4
    /* 1EDEF4 151C0A44 AFA30214 */  sw         $v1, 0x214($sp)
    /* 1EDEF8 151C0A48 AFA001C8 */  sw         $zero, 0x1C8($sp)
    /* 1EDEFC 151C0A4C 270A0060 */  addiu      $t2, $t8, 0x60
    /* 1EDF00 151C0A50 27AE0148 */  addiu      $t6, $sp, 0x148
  .L151C0A54:
    /* 1EDF04 151C0A54 8F010000 */  lw         $at, 0x0($t8)
    /* 1EDF08 151C0A58 2718000C */  addiu      $t8, $t8, 0xC
    /* 1EDF0C 151C0A5C 25CE000C */  addiu      $t6, $t6, 0xC
    /* 1EDF10 151C0A60 ADC1FFF4 */  sw         $at, -0xC($t6)
    /* 1EDF14 151C0A64 8F01FFF8 */  lw         $at, -0x8($t8)
    /* 1EDF18 151C0A68 ADC1FFF8 */  sw         $at, -0x8($t6)
    /* 1EDF1C 151C0A6C 8F01FFFC */  lw         $at, -0x4($t8)
    /* 1EDF20 151C0A70 170AFFF8 */  bne        $t8, $t2, .L151C0A54
    /* 1EDF24 151C0A74 ADC1FFFC */   sw        $at, -0x4($t6)
    /* 1EDF28 151C0A78 8F010000 */  lw         $at, 0x0($t8)
    /* 1EDF2C 151C0A7C 27AC0260 */  addiu      $t4, $sp, 0x260
    /* 1EDF30 151C0A80 27AB00F4 */  addiu      $t3, $sp, 0xF4
    /* 1EDF34 151C0A84 ADC10000 */  sw         $at, 0x0($t6)
    /* 1EDF38 151C0A88 AFA001CC */  sw         $zero, 0x1CC($sp)
    /* 1EDF3C 151C0A8C E7A000CC */  swc1       $f0, 0xCC($sp)
    /* 1EDF40 151C0A90 E7A000D0 */  swc1       $f0, 0xD0($sp)
    /* 1EDF44 151C0A94 E7A200D4 */  swc1       $f2, 0xD4($sp)
    /* 1EDF48 151C0A98 E7A200D8 */  swc1       $f2, 0xD8($sp)
    /* 1EDF4C 151C0A9C E7AC00DC */  swc1       $f12, 0xDC($sp)
    /* 1EDF50 151C0AA0 E7AC00E0 */  swc1       $f12, 0xE0($sp)
    /* 1EDF54 151C0AA4 E7AC00E4 */  swc1       $f12, 0xE4($sp)
    /* 1EDF58 151C0AA8 E7A000E8 */  swc1       $f0, 0xE8($sp)
    /* 1EDF5C 151C0AAC E7A000EC */  swc1       $f0, 0xEC($sp)
    /* 1EDF60 151C0AB0 E7A000F0 */  swc1       $f0, 0xF0($sp)
    /* 1EDF64 151C0AB4 8D810000 */  lw         $at, 0x0($t4)
    /* 1EDF68 151C0AB8 3C190050 */  lui        $t9, (0x500920 >> 16)
    /* 1EDF6C 151C0ABC 37390920 */  ori        $t9, $t9, (0x500920 & 0xFFFF)
    /* 1EDF70 151C0AC0 AD610000 */  sw         $at, 0x0($t3)
    /* 1EDF74 151C0AC4 8D890004 */  lw         $t1, 0x4($t4)
    /* 1EDF78 151C0AC8 240A012C */  addiu      $t2, $zero, 0x12C
    /* 1EDF7C 151C0ACC 2418002F */  addiu      $t8, $zero, 0x2F
    /* 1EDF80 151C0AD0 AD690004 */  sw         $t1, 0x4($t3)
    /* 1EDF84 151C0AD4 8D810008 */  lw         $at, 0x8($t4)
    /* 1EDF88 151C0AD8 240E0001 */  addiu      $t6, $zero, 0x1
    /* 1EDF8C 151C0ADC 27AF01B8 */  addiu      $t7, $sp, 0x1B8
    /* 1EDF90 151C0AE0 AD610008 */  sw         $at, 0x8($t3)
    /* 1EDF94 151C0AE4 8FAD0310 */  lw         $t5, 0x310($sp)
    /* 1EDF98 151C0AE8 E7AC0118 */  swc1       $f12, 0x118($sp)
    /* 1EDF9C 151C0AEC AFB9011C */  sw         $t9, 0x11C($sp)
    /* 1EDFA0 151C0AF0 A7AA0120 */  sh         $t2, 0x120($sp)
    /* 1EDFA4 151C0AF4 A7B80122 */  sh         $t8, 0x122($sp)
    /* 1EDFA8 151C0AF8 A3AE0124 */  sb         $t6, 0x124($sp)
    /* 1EDFAC 151C0AFC AFB001B4 */  sw         $s0, 0x1B4($sp)
    /* 1EDFB0 151C0B00 8DA10000 */  lw         $at, 0x0($t5)
    /* 1EDFB4 151C0B04 27AA0294 */  addiu      $t2, $sp, 0x294
    /* 1EDFB8 151C0B08 27B901E0 */  addiu      $t9, $sp, 0x1E0
    /* 1EDFBC 151C0B0C ADE10000 */  sw         $at, 0x0($t7)
    /* 1EDFC0 151C0B10 8DA90004 */  lw         $t1, 0x4($t5)
    /* 1EDFC4 151C0B14 44805000 */  mtc1       $zero, $f10
    /* 1EDFC8 151C0B18 240B0001 */  addiu      $t3, $zero, 0x1
    /* 1EDFCC 151C0B1C ADE90004 */  sw         $t1, 0x4($t7)
    /* 1EDFD0 151C0B20 8DA10008 */  lw         $at, 0x8($t5)
    /* 1EDFD4 151C0B24 ADE10008 */  sw         $at, 0x8($t7)
    /* 1EDFD8 151C0B28 8DA9000C */  lw         $t1, 0xC($t5)
    /* 1EDFDC 151C0B2C 3C01800B */  lui        $at, %hi(D_800AA9A8)
    /* 1EDFE0 151C0B30 27AD01EC */  addiu      $t5, $sp, 0x1EC
    /* 1EDFE4 151C0B34 ADE9000C */  sw         $t1, 0xC($t7)
    /* 1EDFE8 151C0B38 C7A402A0 */  lwc1       $f4, 0x2A0($sp)
    /* 1EDFEC 151C0B3C C432A9A8 */  lwc1       $f18, %lo(D_800AA9A8)($at)
    /* 1EDFF0 151C0B40 46122182 */  mul.s      $f6, $f4, $f18
    /* 1EDFF4 151C0B44 E7A601DC */  swc1       $f6, 0x1DC($sp)
    /* 1EDFF8 151C0B48 8D410000 */  lw         $at, 0x0($t2)
    /* 1EDFFC 151C0B4C AF210000 */  sw         $at, 0x0($t9)
    /* 1EE000 151C0B50 8D4C0004 */  lw         $t4, 0x4($t2)
    /* 1EE004 151C0B54 AF2C0004 */  sw         $t4, 0x4($t9)
    /* 1EE008 151C0B58 8D410008 */  lw         $at, 0x8($t2)
    /* 1EE00C 151C0B5C AF210008 */  sw         $at, 0x8($t9)
    /* 1EE010 151C0B60 C7A802A0 */  lwc1       $f8, 0x2A0($sp)
    /* 1EE014 151C0B64 3C014348 */  lui        $at, (0x43480000 >> 16)
    /* 1EE018 151C0B68 44810000 */  mtc1       $at, $f0
    /* 1EE01C 151C0B6C 460A4032 */  c.eq.s     $f8, $f10
    /* 1EE020 151C0B70 00000000 */  nop
    /* 1EE024 151C0B74 45030004 */  bc1tl      .L151C0B88
    /* 1EE028 151C0B78 AFA00058 */   sw        $zero, 0x58($sp)
    /* 1EE02C 151C0B7C 10000002 */  b          .L151C0B88
    /* 1EE030 151C0B80 AFAB0058 */   sw        $t3, 0x58($sp)
    /* 1EE034 151C0B84 AFA00058 */  sw         $zero, 0x58($sp)
  .L151C0B88:
    /* 1EE038 151C0B88 8FAF0058 */  lw         $t7, 0x58($sp)
    /* 1EE03C 151C0B8C 27A90270 */  addiu      $t1, $sp, 0x270
    /* 1EE040 151C0B90 25390024 */  addiu      $t9, $t1, 0x24
    /* 1EE044 151C0B94 A3AF0210 */  sb         $t7, 0x210($sp)
  .L151C0B98:
    /* 1EE048 151C0B98 8D210000 */  lw         $at, 0x0($t1)
    /* 1EE04C 151C0B9C 2529000C */  addiu      $t1, $t1, 0xC
    /* 1EE050 151C0BA0 25AD000C */  addiu      $t5, $t5, 0xC
    /* 1EE054 151C0BA4 ADA1FFF4 */  sw         $at, -0xC($t5)
    /* 1EE058 151C0BA8 8D21FFF8 */  lw         $at, -0x8($t1)
    /* 1EE05C 151C0BAC ADA1FFF8 */  sw         $at, -0x8($t5)
    /* 1EE060 151C0BB0 8D21FFFC */  lw         $at, -0x4($t1)
    /* 1EE064 151C0BB4 1539FFF8 */  bne        $t1, $t9, .L151C0B98
    /* 1EE068 151C0BB8 ADA1FFFC */   sw        $at, -0x4($t5)
    /* 1EE06C 151C0BBC C7B00180 */  lwc1       $f16, 0x180($sp)
    /* 1EE070 151C0BC0 C7B20184 */  lwc1       $f18, 0x184($sp)
    /* 1EE074 151C0BC4 C7A80188 */  lwc1       $f8, 0x188($sp)
    /* 1EE078 151C0BC8 46008102 */  mul.s      $f4, $f16, $f0
    /* 1EE07C 151C0BCC E7A001B0 */  swc1       $f0, 0x1B0($sp)
    /* 1EE080 151C0BD0 27A40100 */  addiu      $a0, $sp, 0x100
    /* 1EE084 151C0BD4 46009182 */  mul.s      $f6, $f18, $f0
    /* 1EE088 151C0BD8 27A500E0 */  addiu      $a1, $sp, 0xE0
    /* 1EE08C 151C0BDC 27A600DC */  addiu      $a2, $sp, 0xDC
    /* 1EE090 151C0BE0 46004282 */  mul.s      $f10, $f8, $f0
    /* 1EE094 151C0BE4 E7A40100 */  swc1       $f4, 0x100($sp)
    /* 1EE098 151C0BE8 E7A60104 */  swc1       $f6, 0x104($sp)
    /* 1EE09C 151C0BEC 0D45165D */  jal        func_15145974
    /* 1EE0A0 151C0BF0 E7AA0108 */   swc1      $f10, 0x108($sp)
    /* 1EE0A4 151C0BF4 44808000 */  mtc1       $zero, $f16
    /* 1EE0A8 151C0BF8 3C01800B */  lui        $at, %hi(D_800AA9AC)
    /* 1EE0AC 151C0BFC C42AA9AC */  lwc1       $f10, %lo(D_800AA9AC)($at)
    /* 1EE0B0 151C0C00 C7A8014C */  lwc1       $f8, 0x14C($sp)
    /* 1EE0B4 151C0C04 E7B000E4 */  swc1       $f16, 0xE4($sp)
    /* 1EE0B8 151C0C08 44802000 */  mtc1       $zero, $f4
    /* 1EE0BC 151C0C0C 460A4402 */  mul.s      $f16, $f8, $f10
    /* 1EE0C0 151C0C10 44809000 */  mtc1       $zero, $f18
    /* 1EE0C4 151C0C14 44803000 */  mtc1       $zero, $f6
    /* 1EE0C8 151C0C18 93AA0317 */  lbu        $t2, 0x317($sp)
    /* 1EE0CC 151C0C1C 93A9031B */  lbu        $t1, 0x31B($sp)
    /* 1EE0D0 151C0C20 8FAD031C */  lw         $t5, 0x31C($sp)
    /* 1EE0D4 151C0C24 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 1EE0D8 151C0C28 240B000A */  addiu      $t3, $zero, 0xA
    /* 1EE0DC 151C0C2C 240F0002 */  addiu      $t7, $zero, 0x2
    /* 1EE0E0 151C0C30 24180002 */  addiu      $t8, $zero, 0x2
    /* 1EE0E4 151C0C34 240E0001 */  addiu      $t6, $zero, 0x1
    /* 1EE0E8 151C0C38 241900FF */  addiu      $t9, $zero, 0xFF
    /* 1EE0EC 151C0C3C E7B001AC */  swc1       $f16, 0x1AC($sp)
    /* 1EE0F0 151C0C40 AFA00128 */  sw         $zero, 0x128($sp)
    /* 1EE0F4 151C0C44 A3AC012C */  sb         $t4, 0x12C($sp)
    /* 1EE0F8 151C0C48 A3AB012D */  sb         $t3, 0x12D($sp)
    /* 1EE0FC 151C0C4C A3A0012E */  sb         $zero, 0x12E($sp)
    /* 1EE100 151C0C50 A3A0012F */  sb         $zero, 0x12F($sp)
    /* 1EE104 151C0C54 A3A00130 */  sb         $zero, 0x130($sp)
    /* 1EE108 151C0C58 A3A00131 */  sb         $zero, 0x131($sp)
    /* 1EE10C 151C0C5C A3A00132 */  sb         $zero, 0x132($sp)
    /* 1EE110 151C0C60 A3A00133 */  sb         $zero, 0x133($sp)
    /* 1EE114 151C0C64 A3AF0134 */  sb         $t7, 0x134($sp)
    /* 1EE118 151C0C68 A3B80136 */  sb         $t8, 0x136($sp)
    /* 1EE11C 151C0C6C AFA00138 */  sw         $zero, 0x138($sp)
    /* 1EE120 151C0C70 A3A0013C */  sb         $zero, 0x13C($sp)
    /* 1EE124 151C0C74 A7AE013E */  sh         $t6, 0x13E($sp)
    /* 1EE128 151C0C78 A7B90140 */  sh         $t9, 0x140($sp)
    /* 1EE12C 151C0C7C 27A400CC */  addiu      $a0, $sp, 0xCC
    /* 1EE130 151C0C80 24050003 */  addiu      $a1, $zero, 0x3
    /* 1EE134 151C0C84 240600FF */  addiu      $a2, $zero, 0xFF
    /* 1EE138 151C0C88 240700D0 */  addiu      $a3, $zero, 0xD0
    /* 1EE13C 151C0C8C E7A4010C */  swc1       $f4, 0x10C($sp)
    /* 1EE140 151C0C90 E7B20110 */  swc1       $f18, 0x110($sp)
    /* 1EE144 151C0C94 E7A60114 */  swc1       $f6, 0x114($sp)
    /* 1EE148 151C0C98 A3AA01DA */  sb         $t2, 0x1DA($sp)
    /* 1EE14C 151C0C9C AFA90010 */  sw         $t1, 0x10($sp)
    /* 1EE150 151C0CA0 0D44CA93 */  jal        func_15132A4C
    /* 1EE154 151C0CA4 AFAD0014 */   sw        $t5, 0x14($sp)
    /* 1EE158 151C0CA8 10400072 */  beqz       $v0, .L151C0E74
    /* 1EE15C 151C0CAC 8FA401C8 */   lw        $a0, 0x1C8($sp)
    /* 1EE160 151C0CB0 24440170 */  addiu      $a0, $v0, 0x170
    /* 1EE164 151C0CB4 AFA40048 */  sw         $a0, 0x48($sp)
    /* 1EE168 151C0CB8 27A50148 */  addiu      $a1, $sp, 0x148
    /* 1EE16C 151C0CBC 240600D0 */  addiu      $a2, $zero, 0xD0
    /* 1EE170 151C0CC0 0C008BB0 */  jal        memcpy
    /* 1EE174 151C0CC4 AFA200C8 */   sw        $v0, 0xC8($sp)
    /* 1EE178 151C0CC8 C7A40260 */  lwc1       $f4, 0x260($sp)
    /* 1EE17C 151C0CCC C7A60264 */  lwc1       $f6, 0x264($sp)
    /* 1EE180 151C0CD0 C7AA0268 */  lwc1       $f10, 0x268($sp)
    /* 1EE184 151C0CD4 4600248D */  trunc.w.s  $f18, $f4
    /* 1EE188 151C0CD8 240A0002 */  addiu      $t2, $zero, 0x2
    /* 1EE18C 151C0CDC 240CFFFF */  addiu      $t4, $zero, -0x1
    /* 1EE190 151C0CE0 4600320D */  trunc.w.s  $f8, $f6
    /* 1EE194 151C0CE4 44189000 */  mfc1       $t8, $f18
    /* 1EE198 151C0CE8 240B012C */  addiu      $t3, $zero, 0x12C
    /* 1EE19C 151C0CEC 4600540D */  trunc.w.s  $f16, $f10
    /* 1EE1A0 151C0CF0 AFB800B0 */  sw         $t8, 0xB0($sp)
    /* 1EE1A4 151C0CF4 44194000 */  mfc1       $t9, $f8
    /* 1EE1A8 151C0CF8 8FB8031C */  lw         $t8, 0x31C($sp)
    /* 1EE1AC 151C0CFC 440D8000 */  mfc1       $t5, $f16
    /* 1EE1B0 151C0D00 93AF031B */  lbu        $t7, 0x31B($sp)
    /* 1EE1B4 151C0D04 A3AA00BC */  sb         $t2, 0xBC($sp)
    /* 1EE1B8 151C0D08 A3AC00BD */  sb         $t4, 0xBD($sp)
    /* 1EE1BC 151C0D0C A7AB00BE */  sh         $t3, 0xBE($sp)
    /* 1EE1C0 151C0D10 240B00FF */  addiu      $t3, $zero, 0xFF
    /* 1EE1C4 151C0D14 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 1EE1C8 151C0D18 240A00FF */  addiu      $t2, $zero, 0xFF
    /* 1EE1CC 151C0D1C A3A000C0 */  sb         $zero, 0xC0($sp)
    /* 1EE1D0 151C0D20 AFAA0010 */  sw         $t2, 0x10($sp)
    /* 1EE1D4 151C0D24 AFAC0014 */  sw         $t4, 0x14($sp)
    /* 1EE1D8 151C0D28 AFAB0018 */  sw         $t3, 0x18($sp)
    /* 1EE1DC 151C0D2C 27A400BC */  addiu      $a0, $sp, 0xBC
    /* 1EE1E0 151C0D30 27A500B0 */  addiu      $a1, $sp, 0xB0
    /* 1EE1E4 151C0D34 24060028 */  addiu      $a2, $zero, 0x28
    /* 1EE1E8 151C0D38 240700FF */  addiu      $a3, $zero, 0xFF
    /* 1EE1EC 151C0D3C AFA0001C */  sw         $zero, 0x1C($sp)
    /* 1EE1F0 151C0D40 AFA00020 */  sw         $zero, 0x20($sp)
    /* 1EE1F4 151C0D44 AFB900B4 */  sw         $t9, 0xB4($sp)
    /* 1EE1F8 151C0D48 AFB80028 */  sw         $t8, 0x28($sp)
    /* 1EE1FC 151C0D4C AFAD00B8 */  sw         $t5, 0xB8($sp)
    /* 1EE200 151C0D50 0D4580B0 */  jal        func_151602C0
    /* 1EE204 151C0D54 AFAF0024 */   sw        $t7, 0x24($sp)
    /* 1EE208 151C0D58 8FAE0048 */  lw         $t6, 0x48($sp)
    /* 1EE20C 151C0D5C ADC20080 */  sw         $v0, 0x80($t6)
    /* 1EE210 151C0D60 0D46E242 */  jal        func_151B8908
    /* 1EE214 151C0D64 8FA400C8 */   lw        $a0, 0xC8($sp)
    /* 1EE218 151C0D68 8FB90048 */  lw         $t9, 0x48($sp)
    /* 1EE21C 151C0D6C 0D42B688 */  jal        func_150ADA20
    /* 1EE220 151C0D70 AF220084 */   sw        $v0, 0x84($t9)
    /* 1EE224 151C0D74 24010003 */  addiu      $at, $zero, 0x3
    /* 1EE228 151C0D78 0041001B */  divu       $zero, $v0, $at
    /* 1EE22C 151C0D7C C7A60264 */  lwc1       $f6, 0x264($sp)
    /* 1EE230 151C0D80 C7A40260 */  lwc1       $f4, 0x260($sp)
    /* 1EE234 151C0D84 C7AA0268 */  lwc1       $f10, 0x268($sp)
    /* 1EE238 151C0D88 4600320D */  trunc.w.s  $f8, $f6
    /* 1EE23C 151C0D8C 00002010 */  mfhi       $a0
    /* 1EE240 151C0D90 248402EE */  addiu      $a0, $a0, 0x2EE
    /* 1EE244 151C0D94 4600248D */  trunc.w.s  $f18, $f4
    /* 1EE248 151C0D98 44064000 */  mfc1       $a2, $f8
    /* 1EE24C 151C0D9C 3C0B151C */  lui        $t3, %hi(func_151C110C)
    /* 1EE250 151C0DA0 4600540D */  trunc.w.s  $f16, $f10
    /* 1EE254 151C0DA4 44059000 */  mfc1       $a1, $f18
    /* 1EE258 151C0DA8 00067C00 */  sll        $t7, $a2, 16
    /* 1EE25C 151C0DAC 000F3403 */  sra        $a2, $t7, 16
    /* 1EE260 151C0DB0 44078000 */  mfc1       $a3, $f16
    /* 1EE264 151C0DB4 00055400 */  sll        $t2, $a1, 16
    /* 1EE268 151C0DB8 8FAF00C8 */  lw         $t7, 0xC8($sp)
    /* 1EE26C 151C0DBC 000A2C03 */  sra        $a1, $t2, 16
    /* 1EE270 151C0DC0 240A03E8 */  addiu      $t2, $zero, 0x3E8
    /* 1EE274 151C0DC4 256B110C */  addiu      $t3, $t3, %lo(func_151C110C)
    /* 1EE278 151C0DC8 3089FFFF */  andi       $t1, $a0, 0xFFFF
    /* 1EE27C 151C0DCC 240D7530 */  addiu      $t5, $zero, 0x7530
    /* 1EE280 151C0DD0 240C01F4 */  addiu      $t4, $zero, 0x1F4
    /* 1EE284 151C0DD4 24180004 */  addiu      $t8, $zero, 0x4
    /* 1EE288 151C0DD8 0007CC00 */  sll        $t9, $a3, 16
    /* 1EE28C 151C0DDC 00193C03 */  sra        $a3, $t9, 16
    /* 1EE290 151C0DE0 AFB80028 */  sw         $t8, 0x28($sp)
    /* 1EE294 151C0DE4 AFAC0018 */  sw         $t4, 0x18($sp)
    /* 1EE298 151C0DE8 AFAD0010 */  sw         $t5, 0x10($sp)
    /* 1EE29C 151C0DEC 01202025 */  or         $a0, $t1, $zero
    /* 1EE2A0 151C0DF0 AFAB001C */  sw         $t3, 0x1C($sp)
    /* 1EE2A4 151C0DF4 AFAA0014 */  sw         $t2, 0x14($sp)
    /* 1EE2A8 151C0DF8 AFA00024 */  sw         $zero, 0x24($sp)
    /* 1EE2AC 151C0DFC AFA0002C */  sw         $zero, 0x2C($sp)
    /* 1EE2B0 151C0E00 0C003E99 */  jal        func_1000FA64
    /* 1EE2B4 151C0E04 AFAF0020 */   sw        $t7, 0x20($sp)
    /* 1EE2B8 151C0E08 8FAE0048 */  lw         $t6, 0x48($sp)
    /* 1EE2BC 151C0E0C A5C20090 */  sh         $v0, 0x90($t6)
    /* 1EE2C0 151C0E10 0D46E100 */  jal        func_151B8400
    /* 1EE2C4 151C0E14 8FA400C8 */   lw        $a0, 0xC8($sp)
    /* 1EE2C8 151C0E18 8FB90048 */  lw         $t9, 0x48($sp)
    /* 1EE2CC 151C0E1C 3C098008 */  lui        $t1, %hi(D_80082FA0)
    /* 1EE2D0 151C0E20 3C0D8009 */  lui        $t5, %hi(D_8008FD8C)
    /* 1EE2D4 151C0E24 AF220088 */  sw         $v0, 0x88($t9)
    /* 1EE2D8 151C0E28 8D292FA0 */  lw         $t1, %lo(D_80082FA0)($t1)
    /* 1EE2DC 151C0E2C 8FAC0048 */  lw         $t4, 0x48($sp)
    /* 1EE2E0 151C0E30 29210002 */  slti       $at, $t1, 0x2
    /* 1EE2E4 151C0E34 5020000D */  beql       $at, $zero, .L151C0E6C
    /* 1EE2E8 151C0E38 AD80008C */   sw        $zero, 0x8C($t4)
    /* 1EE2EC 151C0E3C 81ADFD8C */  lb         $t5, %lo(D_8008FD8C)($t5)
    /* 1EE2F0 151C0E40 8FA400C8 */  lw         $a0, 0xC8($sp)
    /* 1EE2F4 151C0E44 93A5031B */  lbu        $a1, 0x31B($sp)
    /* 1EE2F8 151C0E48 29A10004 */  slti       $at, $t5, 0x4
    /* 1EE2FC 151C0E4C 50200007 */  beql       $at, $zero, .L151C0E6C
    /* 1EE300 151C0E50 AD80008C */   sw        $zero, 0x8C($t4)
    /* 1EE304 151C0E54 0D46E19A */  jal        func_151B8668
    /* 1EE308 151C0E58 8FA6031C */   lw        $a2, 0x31C($sp)
    /* 1EE30C 151C0E5C 8FAA0048 */  lw         $t2, 0x48($sp)
    /* 1EE310 151C0E60 1000000D */  b          .L151C0E98
    /* 1EE314 151C0E64 AD42008C */   sw        $v0, 0x8C($t2)
    /* 1EE318 151C0E68 AD80008C */  sw         $zero, 0x8C($t4)
  .L151C0E6C:
    /* 1EE31C 151C0E6C 1000000B */  b          .L151C0E9C
    /* 1EE320 151C0E70 8E0B01D4 */   lw        $t3, 0x1D4($s0)
  .L151C0E74:
    /* 1EE324 151C0E74 50800004 */  beql       $a0, $zero, .L151C0E88
    /* 1EE328 151C0E78 8FA401CC */   lw        $a0, 0x1CC($sp)
    /* 1EE32C 151C0E7C 0D45A5CB */  jal        func_1516972C
    /* 1EE330 151C0E80 00000000 */   nop
    /* 1EE334 151C0E84 8FA401CC */  lw         $a0, 0x1CC($sp)
  .L151C0E88:
    /* 1EE338 151C0E88 50800004 */  beql       $a0, $zero, .L151C0E9C
    /* 1EE33C 151C0E8C 8E0B01D4 */   lw        $t3, 0x1D4($s0)
    /* 1EE340 151C0E90 0D45A5CB */  jal        func_1516972C
    /* 1EE344 151C0E94 00000000 */   nop
  .L151C0E98:
    /* 1EE348 151C0E98 8E0B01D4 */  lw         $t3, 0x1D4($s0)
  .L151C0E9C:
    /* 1EE34C 151C0E9C 51600097 */  beql       $t3, $zero, .L151C10FC
    /* 1EE350 151C0EA0 8FBF0044 */   lw        $ra, 0x44($sp)
    /* 1EE354 151C0EA4 920F0074 */  lbu        $t7, 0x74($s0)
    /* 1EE358 151C0EA8 2401000F */  addiu      $at, $zero, 0xF
    /* 1EE35C 151C0EAC 31F8000F */  andi       $t8, $t7, 0xF
    /* 1EE360 151C0EB0 53010092 */  beql       $t8, $at, .L151C10FC
    /* 1EE364 151C0EB4 8FBF0044 */   lw        $ra, 0x44($sp)
    /* 1EE368 151C0EB8 92020004 */  lbu        $v0, 0x4($s0)
    /* 1EE36C 151C0EBC 24010077 */  addiu      $at, $zero, 0x77
    /* 1EE370 151C0EC0 1041008D */  beq        $v0, $at, .L151C10F8
    /* 1EE374 151C0EC4 24010028 */   addiu     $at, $zero, 0x28
    /* 1EE378 151C0EC8 1041008B */  beq        $v0, $at, .L151C10F8
    /* 1EE37C 151C0ECC 27AE00A4 */   addiu     $t6, $sp, 0xA4
    /* 1EE380 151C0ED0 3C19800B */  lui        $t9, %hi(D_800AA930)
    /* 1EE384 151C0ED4 2739A930 */  addiu      $t9, $t9, %lo(D_800AA930)
    /* 1EE388 151C0ED8 8F210000 */  lw         $at, 0x0($t9)
    /* 1EE38C 151C0EDC 8F2D0004 */  lw         $t5, 0x4($t9)
    /* 1EE390 151C0EE0 3C0C800B */  lui        $t4, %hi(D_800AA93C)
    /* 1EE394 151C0EE4 ADC10000 */  sw         $at, 0x0($t6)
    /* 1EE398 151C0EE8 8F210008 */  lw         $at, 0x8($t9)
    /* 1EE39C 151C0EEC 258CA93C */  addiu      $t4, $t4, %lo(D_800AA93C)
    /* 1EE3A0 151C0EF0 ADCD0004 */  sw         $t5, 0x4($t6)
    /* 1EE3A4 151C0EF4 ADC10008 */  sw         $at, 0x8($t6)
    /* 1EE3A8 151C0EF8 8D810000 */  lw         $at, 0x0($t4)
    /* 1EE3AC 151C0EFC 27AA0098 */  addiu      $t2, $sp, 0x98
    /* 1EE3B0 151C0F00 8D8F0004 */  lw         $t7, 0x4($t4)
    /* 1EE3B4 151C0F04 AD410000 */  sw         $at, 0x0($t2)
    /* 1EE3B8 151C0F08 8D810008 */  lw         $at, 0x8($t4)
    /* 1EE3BC 151C0F0C 3C09800B */  lui        $t1, %hi(D_800AA948)
    /* 1EE3C0 151C0F10 2529A948 */  addiu      $t1, $t1, %lo(D_800AA948)
    /* 1EE3C4 151C0F14 AD4F0004 */  sw         $t7, 0x4($t2)
    /* 1EE3C8 151C0F18 AD410008 */  sw         $at, 0x8($t2)
    /* 1EE3CC 151C0F1C 8D210000 */  lw         $at, 0x0($t1)
    /* 1EE3D0 151C0F20 27B8008C */  addiu      $t8, $sp, 0x8C
    /* 1EE3D4 151C0F24 8D390004 */  lw         $t9, 0x4($t1)
    /* 1EE3D8 151C0F28 AF010000 */  sw         $at, 0x0($t8)
    /* 1EE3DC 151C0F2C 8D210008 */  lw         $at, 0x8($t1)
    /* 1EE3E0 151C0F30 AF190004 */  sw         $t9, 0x4($t8)
    /* 1EE3E4 151C0F34 0D42B69A */  jal        func_150ADA68
    /* 1EE3E8 151C0F38 AF010008 */   sw        $at, 0x8($t8)
    /* 1EE3EC 151C0F3C 3C014120 */  lui        $at, (0x41200000 >> 16)
    /* 1EE3F0 151C0F40 44812000 */  mtc1       $at, $f4
    /* 1EE3F4 151C0F44 3C0141C8 */  lui        $at, (0x41C80000 >> 16)
    /* 1EE3F8 151C0F48 44813000 */  mtc1       $at, $f6
    /* 1EE3FC 151C0F4C 46040482 */  mul.s      $f18, $f0, $f4
    /* 1EE400 151C0F50 46069200 */  add.s      $f8, $f18, $f6
    /* 1EE404 151C0F54 0D42B69A */  jal        func_150ADA68
    /* 1EE408 151C0F58 E7A80084 */   swc1      $f8, 0x84($sp)
    /* 1EE40C 151C0F5C 3C01800B */  lui        $at, %hi(D_800AA9B0)
    /* 1EE410 151C0F60 C42AA9B0 */  lwc1       $f10, %lo(D_800AA9B0)($at)
    /* 1EE414 151C0F64 3C01800B */  lui        $at, %hi(D_800AA9B4)
    /* 1EE418 151C0F68 C424A9B4 */  lwc1       $f4, %lo(D_800AA9B4)($at)
    /* 1EE41C 151C0F6C 460A0402 */  mul.s      $f16, $f0, $f10
    /* 1EE420 151C0F70 27AD00A4 */  addiu      $t5, $sp, 0xA4
    /* 1EE424 151C0F74 27AB0098 */  addiu      $t3, $sp, 0x98
    /* 1EE428 151C0F78 27AA0078 */  addiu      $t2, $sp, 0x78
    /* 1EE42C 151C0F7C 27AC006C */  addiu      $t4, $sp, 0x6C
    /* 1EE430 151C0F80 AFAD0064 */  sw         $t5, 0x64($sp)
    /* 1EE434 151C0F84 AFAB0068 */  sw         $t3, 0x68($sp)
    /* 1EE438 151C0F88 46048480 */  add.s      $f18, $f16, $f4
    /* 1EE43C 151C0F8C AFAA005C */  sw         $t2, 0x5C($sp)
    /* 1EE440 151C0F90 AFAC0060 */  sw         $t4, 0x60($sp)
    /* 1EE444 151C0F94 27A40064 */  addiu      $a0, $sp, 0x64
    /* 1EE448 151C0F98 E7B20088 */  swc1       $f18, 0x88($sp)
    /* 1EE44C 151C0F9C 8E0601D4 */  lw         $a2, 0x1D4($s0)
    /* 1EE450 151C0FA0 27A5005C */  addiu      $a1, $sp, 0x5C
    /* 1EE454 151C0FA4 24070002 */  addiu      $a3, $zero, 0x2
    /* 1EE458 151C0FA8 0D4517A9 */  jal        func_15145EA4
    /* 1EE45C 151C0FAC 24C60240 */   addiu     $a2, $a2, 0x240
    /* 1EE460 151C0FB0 0D42B688 */  jal        func_150ADA20
    /* 1EE464 151C0FB4 00000000 */   nop
    /* 1EE468 151C0FB8 0D42B688 */  jal        func_150ADA20
    /* 1EE46C 151C0FBC AFA20054 */   sw        $v0, 0x54($sp)
    /* 1EE470 151C0FC0 0D42B69A */  jal        func_150ADA68
    /* 1EE474 151C0FC4 AFA20058 */   sw        $v0, 0x58($sp)
    /* 1EE478 151C0FC8 8FAE0054 */  lw         $t6, 0x54($sp)
    /* 1EE47C 151C0FCC 24010003 */  addiu      $at, $zero, 0x3
    /* 1EE480 151C0FD0 8FB90058 */  lw         $t9, 0x58($sp)
    /* 1EE484 151C0FD4 01C1001B */  divu       $zero, $t6, $at
    /* 1EE488 151C0FD8 24010038 */  addiu      $at, $zero, 0x38
    /* 1EE48C 151C0FDC 0000C010 */  mfhi       $t8
    /* 1EE490 151C0FE0 27090008 */  addiu      $t1, $t8, 0x8
    /* 1EE494 151C0FE4 27AF0084 */  addiu      $t7, $sp, 0x84
    /* 1EE498 151C0FE8 0321001B */  divu       $zero, $t9, $at
    /* 1EE49C 151C0FEC 3C01434C */  lui        $at, (0x434C0000 >> 16)
    /* 1EE4A0 151C0FF0 44813000 */  mtc1       $at, $f6
    /* 1EE4A4 151C0FF4 3C01800B */  lui        $at, %hi(D_800AA9B8)
    /* 1EE4A8 151C0FF8 C42AA9B8 */  lwc1       $f10, %lo(D_800AA9B8)($at)
    /* 1EE4AC 151C0FFC 46060202 */  mul.s      $f8, $f0, $f6
    /* 1EE4B0 151C1000 8FB8031C */  lw         $t8, 0x31C($sp)
    /* 1EE4B4 151C1004 93AE031B */  lbu        $t6, 0x31B($sp)
    /* 1EE4B8 151C1008 00006810 */  mfhi       $t5
    /* 1EE4BC 151C100C AFAF0010 */  sw         $t7, 0x10($sp)
    /* 1EE4C0 151C1010 240FFFFF */  addiu      $t7, $zero, -0x1
    /* 1EE4C4 151C1014 25AB00C8 */  addiu      $t3, $t5, 0xC8
    /* 1EE4C8 151C1018 460A4400 */  add.s      $f16, $f8, $f10
    /* 1EE4CC 151C101C 27AA0078 */  addiu      $t2, $sp, 0x78
    /* 1EE4D0 151C1020 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 1EE4D4 151C1024 AFAC0024 */  sw         $t4, 0x24($sp)
    /* 1EE4D8 151C1028 AFAA0020 */  sw         $t2, 0x20($sp)
    /* 1EE4DC 151C102C E7B0001C */  swc1       $f16, 0x1C($sp)
    /* 1EE4E0 151C1030 AFAB0018 */  sw         $t3, 0x18($sp)
    /* 1EE4E4 151C1034 AFAF002C */  sw         $t7, 0x2C($sp)
    /* 1EE4E8 151C1038 AFA90014 */  sw         $t1, 0x14($sp)
    /* 1EE4EC 151C103C 02002025 */  or         $a0, $s0, $zero
    /* 1EE4F0 151C1040 24050009 */  addiu      $a1, $zero, 0x9
    /* 1EE4F4 151C1044 27A600A4 */  addiu      $a2, $sp, 0xA4
    /* 1EE4F8 151C1048 27A7008C */  addiu      $a3, $sp, 0x8C
    /* 1EE4FC 151C104C AFA00028 */  sw         $zero, 0x28($sp)
    /* 1EE500 151C1050 AFB80034 */  sw         $t8, 0x34($sp)
    /* 1EE504 151C1054 0D440ACE */  jal        func_15102B38
    /* 1EE508 151C1058 AFAE0030 */   sw        $t6, 0x30($sp)
    /* 1EE50C 151C105C 0D42B688 */  jal        func_150ADA20
    /* 1EE510 151C1060 00000000 */   nop
    /* 1EE514 151C1064 0D42B688 */  jal        func_150ADA20
    /* 1EE518 151C1068 AFA20054 */   sw        $v0, 0x54($sp)
    /* 1EE51C 151C106C 0D42B69A */  jal        func_150ADA68
    /* 1EE520 151C1070 AFA20058 */   sw        $v0, 0x58($sp)
    /* 1EE524 151C1074 8FA40054 */  lw         $a0, 0x54($sp)
    /* 1EE528 151C1078 24010003 */  addiu      $at, $zero, 0x3
    /* 1EE52C 151C107C 8FA50058 */  lw         $a1, 0x58($sp)
    /* 1EE530 151C1080 0081001B */  divu       $zero, $a0, $at
    /* 1EE534 151C1084 24010038 */  addiu      $at, $zero, 0x38
    /* 1EE538 151C1088 00004810 */  mfhi       $t1
    /* 1EE53C 151C108C 93AF031B */  lbu        $t7, 0x31B($sp)
    /* 1EE540 151C1090 8FAE031C */  lw         $t6, 0x31C($sp)
    /* 1EE544 151C1094 00A1001B */  divu       $zero, $a1, $at
    /* 1EE548 151C1098 3C01434C */  lui        $at, (0x434C0000 >> 16)
    /* 1EE54C 151C109C 44812000 */  mtc1       $at, $f4
    /* 1EE550 151C10A0 3C01800B */  lui        $at, %hi(D_800AA9BC)
    /* 1EE554 151C10A4 C426A9BC */  lwc1       $f6, %lo(D_800AA9BC)($at)
    /* 1EE558 151C10A8 46040482 */  mul.s      $f18, $f0, $f4
    /* 1EE55C 151C10AC 00005810 */  mfhi       $t3
    /* 1EE560 151C10B0 256500C8 */  addiu      $a1, $t3, 0xC8
    /* 1EE564 151C10B4 25240008 */  addiu      $a0, $t1, 0x8
    /* 1EE568 151C10B8 0004CC00 */  sll        $t9, $a0, 16
    /* 1EE56C 151C10BC 30AA00FF */  andi       $t2, $a1, 0xFF
    /* 1EE570 151C10C0 240C00FF */  addiu      $t4, $zero, 0xFF
    /* 1EE574 151C10C4 46069200 */  add.s      $f8, $f18, $f6
    /* 1EE578 151C10C8 AFAC0010 */  sw         $t4, 0x10($sp)
    /* 1EE57C 151C10CC 01402825 */  or         $a1, $t2, $zero
    /* 1EE580 151C10D0 00192403 */  sra        $a0, $t9, 16
    /* 1EE584 151C10D4 44064000 */  mfc1       $a2, $f8
    /* 1EE588 151C10D8 27A7006C */  addiu      $a3, $sp, 0x6C
    /* 1EE58C 151C10DC AFAF0014 */  sw         $t7, 0x14($sp)
    /* 1EE590 151C10E0 0D440C95 */  jal        func_15103254
    /* 1EE594 151C10E4 AFAE0018 */   sw        $t6, 0x18($sp)
    /* 1EE598 151C10E8 27A4006C */  addiu      $a0, $sp, 0x6C
    /* 1EE59C 151C10EC 93A5031B */  lbu        $a1, 0x31B($sp)
    /* 1EE5A0 151C10F0 0D470618 */  jal        func_151C1860
    /* 1EE5A4 151C10F4 8FA6031C */   lw        $a2, 0x31C($sp)
  .L151C10F8:
    /* 1EE5A8 151C10F8 8FBF0044 */  lw         $ra, 0x44($sp)
  .L151C10FC:
    /* 1EE5AC 151C10FC 8FB00040 */  lw         $s0, 0x40($sp)
    /* 1EE5B0 151C1100 27BD0308 */  addiu      $sp, $sp, 0x308
    /* 1EE5B4 151C1104 03E00008 */  jr         $ra
    /* 1EE5B8 151C1108 00000000 */   nop
endlabel func_151C0698
