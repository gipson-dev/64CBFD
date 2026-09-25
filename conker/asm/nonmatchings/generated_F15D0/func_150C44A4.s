glabel func_150C44A4
    /* F1954 150C44A4 27BDFEF0 */  addiu      $sp, $sp, -0x110
    /* F1958 150C44A8 AFB40074 */  sw         $s4, 0x74($sp)
    /* F195C 150C44AC 0080A025 */  or         $s4, $a0, $zero
    /* F1960 150C44B0 AFBF007C */  sw         $ra, 0x7C($sp)
    /* F1964 150C44B4 AFB50078 */  sw         $s5, 0x78($sp)
    /* F1968 150C44B8 AFB30070 */  sw         $s3, 0x70($sp)
    /* F196C 150C44BC AFB2006C */  sw         $s2, 0x6C($sp)
    /* F1970 150C44C0 AFB10068 */  sw         $s1, 0x68($sp)
    /* F1974 150C44C4 AFB00064 */  sw         $s0, 0x64($sp)
    /* F1978 150C44C8 F7BA0058 */  sdc1       $f26, 0x58($sp)
    /* F197C 150C44CC F7B80050 */  sdc1       $f24, 0x50($sp)
    /* F1980 150C44D0 F7B60048 */  sdc1       $f22, 0x48($sp)
    /* F1984 150C44D4 F7B40040 */  sdc1       $f20, 0x40($sp)
    /* F1988 150C44D8 8E900028 */  lw         $s0, 0x28($s4)
    /* F198C 150C44DC 26930028 */  addiu      $s3, $s4, 0x28
    /* F1990 150C44E0 2419FFFF */  addiu      $t9, $zero, -0x1
    /* F1994 150C44E4 8E0E0000 */  lw         $t6, 0x0($s0)
    /* F1998 150C44E8 11C00005 */  beqz       $t6, .L150C4500
    /* F199C 150C44EC 00000000 */   nop
    /* F19A0 150C44F0 926F0004 */  lbu        $t7, 0x4($s3)
    /* F19A4 150C44F4 9218003B */  lbu        $t8, 0x3B($s0)
    /* F19A8 150C44F8 51F80004 */  beql       $t7, $t8, .L150C450C
    /* F19AC 150C44FC 8E0801D4 */   lw        $t0, 0x1D4($s0)
  .L150C4500:
    /* F19B0 150C4500 10000168 */  b          .L150C4AA4
    /* F19B4 150C4504 A699000E */   sh        $t9, 0xE($s4)
    /* F19B8 150C4508 8E0801D4 */  lw         $t0, 0x1D4($s0)
  .L150C450C:
    /* F19BC 150C450C 51000007 */  beql       $t0, $zero, .L150C452C
    /* F19C0 150C4510 8E62000C */   lw        $v0, 0xC($s3)
    /* F19C4 150C4514 92690016 */  lbu        $t1, 0x16($s3)
    /* F19C8 150C4518 27A400C0 */  addiu      $a0, $sp, 0xC0
    /* F19CC 150C451C 312A0002 */  andi       $t2, $t1, 0x2
    /* F19D0 150C4520 11400007 */  beqz       $t2, .L150C4540
    /* F19D4 150C4524 00000000 */   nop
    /* F19D8 150C4528 8E62000C */  lw         $v0, 0xC($s3)
  .L150C452C:
    /* F19DC 150C452C 240B0003 */  addiu      $t3, $zero, 0x3
    /* F19E0 150C4530 5040015D */  beql       $v0, $zero, .L150C4AA8
    /* F19E4 150C4534 8FBF007C */   lw        $ra, 0x7C($sp)
    /* F19E8 150C4538 1000015A */  b          .L150C4AA4
    /* F19EC 150C453C A04B0074 */   sb        $t3, 0x74($v0)
  .L150C4540:
    /* F19F0 150C4540 0D411C57 */  jal        func_1504715C
    /* F19F4 150C4544 02002825 */   or        $a1, $s0, $zero
    /* F19F8 150C4548 8E6C0018 */  lw         $t4, 0x18($s3)
    /* F19FC 150C454C 24040096 */  addiu      $a0, $zero, 0x96
    /* F1A00 150C4550 02002825 */  or         $a1, $s0, $zero
    /* F1A04 150C4554 15800006 */  bnez       $t4, .L150C4570
    /* F1A08 150C4558 240636B0 */   addiu     $a2, $zero, 0x36B0
    /* F1A0C 150C455C 240D4268 */  addiu      $t5, $zero, 0x4268
    /* F1A10 150C4560 AFAD0010 */  sw         $t5, 0x10($sp)
    /* F1A14 150C4564 0C004055 */  jal        func_10010154
    /* F1A18 150C4568 24070190 */   addiu     $a3, $zero, 0x190
    /* F1A1C 150C456C AE620018 */  sw         $v0, 0x18($s3)
  .L150C4570:
    /* F1A20 150C4570 926E0016 */  lbu        $t6, 0x16($s3)
    /* F1A24 150C4574 02002025 */  or         $a0, $s0, $zero
    /* F1A28 150C4578 00003025 */  or         $a2, $zero, $zero
    /* F1A2C 150C457C 31CF0001 */  andi       $t7, $t6, 0x1
    /* F1A30 150C4580 51E0004E */  beql       $t7, $zero, .L150C46BC
    /* F1A34 150C4584 8E0202E8 */   lw        $v0, 0x2E8($s0)
    /* F1A38 150C4588 0D40C657 */  jal        func_1503195C
    /* F1A3C 150C458C 86650014 */   lh        $a1, 0x14($s3)
    /* F1A40 150C4590 10400144 */  beqz       $v0, .L150C4AA4
    /* F1A44 150C4594 00402825 */   or        $a1, $v0, $zero
    /* F1A48 150C4598 8E1802EC */  lw         $t8, 0x2EC($s0)
    /* F1A4C 150C459C 3C014080 */  lui        $at, (0x40800000 >> 16)
    /* F1A50 150C45A0 44816000 */  mtc1       $at, $f12
    /* F1A54 150C45A4 53000007 */  beql       $t8, $zero, .L150C45C4
    /* F1A58 150C45A8 44801000 */   mtc1      $zero, $f2
    /* F1A5C 150C45AC C60402DC */  lwc1       $f4, 0x2DC($s0)
    /* F1A60 150C45B0 C60602D8 */  lwc1       $f6, 0x2D8($s0)
    /* F1A64 150C45B4 46062082 */  mul.s      $f2, $f4, $f6
    /* F1A68 150C45B8 10000003 */  b          .L150C45C8
    /* F1A6C 150C45BC 00000000 */   nop
    /* F1A70 150C45C0 44801000 */  mtc1       $zero, $f2
  .L150C45C4:
    /* F1A74 150C45C4 00000000 */  nop
  .L150C45C8:
    /* F1A78 150C45C8 460C1202 */  mul.s      $f8, $f2, $f12
    /* F1A7C 150C45CC 4600428D */  trunc.w.s  $f10, $f8
    /* F1A80 150C45D0 44035000 */  mfc1       $v1, $f10
    /* F1A84 150C45D4 00000000 */  nop
    /* F1A88 150C45D8 28610004 */  slti       $at, $v1, 0x4
    /* F1A8C 150C45DC 54200003 */  bnel       $at, $zero, .L150C45EC
    /* F1A90 150C45E0 44838000 */   mtc1      $v1, $f16
    /* F1A94 150C45E4 24030003 */  addiu      $v1, $zero, 0x3
    /* F1A98 150C45E8 44838000 */  mtc1       $v1, $f16
  .L150C45EC:
    /* F1A9C 150C45EC 3C013E80 */  lui        $at, (0x3E800000 >> 16)
    /* F1AA0 150C45F0 44812000 */  mtc1       $at, $f4
    /* F1AA4 150C45F4 468084A0 */  cvt.s.w    $f18, $f16
    /* F1AA8 150C45F8 00034080 */  sll        $t0, $v1, 2
    /* F1AAC 150C45FC 01034023 */  subu       $t0, $t0, $v1
    /* F1AB0 150C4600 3C09800A */  lui        $t1, %hi(D_800A0378)
    /* F1AB4 150C4604 25290378 */  addiu      $t1, $t1, %lo(D_800A0378)
    /* F1AB8 150C4608 00084080 */  sll        $t0, $t0, 2
    /* F1ABC 150C460C 46049182 */  mul.s      $f6, $f18, $f4
    /* F1AC0 150C4610 01091021 */  addu       $v0, $t0, $t1
    /* F1AC4 150C4614 C44A0000 */  lwc1       $f10, 0x0($v0)
    /* F1AC8 150C4618 C4520004 */  lwc1       $f18, 0x4($v0)
    /* F1ACC 150C461C 3C06800A */  lui        $a2, %hi(D_800A03A8)
    /* F1AD0 150C4620 27B500FC */  addiu      $s5, $sp, 0xFC
    /* F1AD4 150C4624 27AA00F0 */  addiu      $t2, $sp, 0xF0
    /* F1AD8 150C4628 46061201 */  sub.s      $f8, $f2, $f6
    /* F1ADC 150C462C C4460008 */  lwc1       $f6, 0x8($v0)
    /* F1AE0 150C4630 00C33021 */  addu       $a2, $a2, $v1
    /* F1AE4 150C4634 27AB00B8 */  addiu      $t3, $sp, 0xB8
    /* F1AE8 150C4638 460C4002 */  mul.s      $f0, $f8, $f12
    /* F1AEC 150C463C 240C0001 */  addiu      $t4, $zero, 0x1
    /* F1AF0 150C4640 AFAA00BC */  sw         $t2, 0xBC($sp)
    /* F1AF4 150C4644 AFB500B8 */  sw         $s5, 0xB8($sp)
    /* F1AF8 150C4648 AFAC0014 */  sw         $t4, 0x14($sp)
    /* F1AFC 150C464C AFAB0010 */  sw         $t3, 0x10($sp)
    /* F1B00 150C4650 90C603A8 */  lbu        $a2, %lo(D_800A03A8)($a2)
    /* F1B04 150C4654 46005402 */  mul.s      $f16, $f10, $f0
    /* F1B08 150C4658 02002025 */  or         $a0, $s0, $zero
    /* F1B0C 150C465C 27A700BC */  addiu      $a3, $sp, 0xBC
    /* F1B10 150C4660 46009102 */  mul.s      $f4, $f18, $f0
    /* F1B14 150C4664 00000000 */  nop
    /* F1B18 150C4668 46003202 */  mul.s      $f8, $f6, $f0
    /* F1B1C 150C466C E7B000F0 */  swc1       $f16, 0xF0($sp)
    /* F1B20 150C4670 E7A400F4 */  swc1       $f4, 0xF4($sp)
    /* F1B24 150C4674 0D451953 */  jal        func_1514654C
    /* F1B28 150C4678 E7A800F8 */   swc1      $f8, 0xF8($sp)
    /* F1B2C 150C467C 5440000B */  bnel       $v0, $zero, .L150C46AC
    /* F1B30 150C4680 3C013F80 */   lui       $at, (0x3F800000 >> 16)
    /* F1B34 150C4684 C60A0014 */  lwc1       $f10, 0x14($s0)
    /* F1B38 150C4688 3C014448 */  lui        $at, (0x44480000 >> 16)
    /* F1B3C 150C468C 44819000 */  mtc1       $at, $f18
    /* F1B40 150C4690 E7AA00FC */  swc1       $f10, 0xFC($sp)
    /* F1B44 150C4694 C6100018 */  lwc1       $f16, 0x18($s0)
    /* F1B48 150C4698 46128100 */  add.s      $f4, $f16, $f18
    /* F1B4C 150C469C E7A40100 */  swc1       $f4, 0x100($sp)
    /* F1B50 150C46A0 C606001C */  lwc1       $f6, 0x1C($s0)
    /* F1B54 150C46A4 E7A60104 */  swc1       $f6, 0x104($sp)
    /* F1B58 150C46A8 3C013F80 */  lui        $at, (0x3F800000 >> 16)
  .L150C46AC:
    /* F1B5C 150C46AC 4481C000 */  mtc1       $at, $f24
    /* F1B60 150C46B0 1000003F */  b          .L150C47B0
    /* F1B64 150C46B4 8E62000C */   lw        $v0, 0xC($s3)
    /* F1B68 150C46B8 8E0202E8 */  lw         $v0, 0x2E8($s0)
  .L150C46BC:
    /* F1B6C 150C46BC 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* F1B70 150C46C0 5040000B */  beql       $v0, $zero, .L150C46F0
    /* F1B74 150C46C4 4481C000 */   mtc1      $at, $f24
    /* F1B78 150C46C8 8E0D02E4 */  lw         $t5, 0x2E4($s0)
    /* F1B7C 150C46CC 44828000 */  mtc1       $v0, $f16
    /* F1B80 150C46D0 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* F1B84 150C46D4 448D4000 */  mtc1       $t5, $f8
    /* F1B88 150C46D8 468084A0 */  cvt.s.w    $f18, $f16
    /* F1B8C 150C46DC 4481C000 */  mtc1       $at, $f24
    /* F1B90 150C46E0 468042A0 */  cvt.s.w    $f10, $f8
    /* F1B94 150C46E4 10000004 */  b          .L150C46F8
    /* F1B98 150C46E8 46125083 */   div.s     $f2, $f10, $f18
    /* F1B9C 150C46EC 4481C000 */  mtc1       $at, $f24
  .L150C46F0:
    /* F1BA0 150C46F0 00000000 */  nop
    /* F1BA4 150C46F4 4600C086 */  mov.s      $f2, $f24
  .L150C46F8:
    /* F1BA8 150C46F8 3C014040 */  lui        $at, (0x40400000 >> 16)
    /* F1BAC 150C46FC 44816000 */  mtc1       $at, $f12
    /* F1BB0 150C4700 00000000 */  nop
    /* F1BB4 150C4704 460C1102 */  mul.s      $f4, $f2, $f12
    /* F1BB8 150C4708 4600218D */  trunc.w.s  $f6, $f4
    /* F1BBC 150C470C 44033000 */  mfc1       $v1, $f6
    /* F1BC0 150C4710 00000000 */  nop
    /* F1BC4 150C4714 28610003 */  slti       $at, $v1, 0x3
    /* F1BC8 150C4718 54200003 */  bnel       $at, $zero, .L150C4728
    /* F1BCC 150C471C 44834000 */   mtc1      $v1, $f8
    /* F1BD0 150C4720 24030002 */  addiu      $v1, $zero, 0x2
    /* F1BD4 150C4724 44834000 */  mtc1       $v1, $f8
  .L150C4728:
    /* F1BD8 150C4728 3C01800A */  lui        $at, %hi(D_800A03B8)
    /* F1BDC 150C472C C42A03B8 */  lwc1       $f10, %lo(D_800A03B8)($at)
    /* F1BE0 150C4730 46804420 */  cvt.s.w    $f16, $f8
    /* F1BE4 150C4734 00037880 */  sll        $t7, $v1, 2
    /* F1BE8 150C4738 01E37823 */  subu       $t7, $t7, $v1
    /* F1BEC 150C473C 3C18800A */  lui        $t8, %hi(D_800A0350)
    /* F1BF0 150C4740 27180350 */  addiu      $t8, $t8, %lo(D_800A0350)
    /* F1BF4 150C4744 000F7880 */  sll        $t7, $t7, 2
    /* F1BF8 150C4748 460A8482 */  mul.s      $f18, $f16, $f10
    /* F1BFC 150C474C 01F81021 */  addu       $v0, $t7, $t8
    /* F1C00 150C4750 C4460000 */  lwc1       $f6, 0x0($v0)
    /* F1C04 150C4754 C4500004 */  lwc1       $f16, 0x4($v0)
    /* F1C08 150C4758 3C19800A */  lui        $t9, %hi(D_800A0374)
    /* F1C0C 150C475C 0323C821 */  addu       $t9, $t9, $v1
    /* F1C10 150C4760 93390374 */  lbu        $t9, %lo(D_800A0374)($t9)
    /* F1C14 150C4764 46121101 */  sub.s      $f4, $f2, $f18
    /* F1C18 150C4768 C4520008 */  lwc1       $f18, 0x8($v0)
    /* F1C1C 150C476C 27B500FC */  addiu      $s5, $sp, 0xFC
    /* F1C20 150C4770 00194180 */  sll        $t0, $t9, 6
    /* F1C24 150C4774 460C2002 */  mul.s      $f0, $f4, $f12
    /* F1C28 150C4778 02A02825 */  or         $a1, $s5, $zero
    /* F1C2C 150C477C 27A400F0 */  addiu      $a0, $sp, 0xF0
    /* F1C30 150C4780 46003202 */  mul.s      $f8, $f6, $f0
    /* F1C34 150C4784 00000000 */  nop
    /* F1C38 150C4788 46008282 */  mul.s      $f10, $f16, $f0
    /* F1C3C 150C478C 00000000 */  nop
    /* F1C40 150C4790 46009102 */  mul.s      $f4, $f18, $f0
    /* F1C44 150C4794 E7A800F0 */  swc1       $f8, 0xF0($sp)
    /* F1C48 150C4798 E7AA00F4 */  swc1       $f10, 0xF4($sp)
    /* F1C4C 150C479C E7A400F8 */  swc1       $f4, 0xF8($sp)
    /* F1C50 150C47A0 8E0901D4 */  lw         $t1, 0x1D4($s0)
    /* F1C54 150C47A4 0D450C4D */  jal        func_15143134
    /* F1C58 150C47A8 01093021 */   addu      $a2, $t0, $t1
    /* F1C5C 150C47AC 8E62000C */  lw         $v0, 0xC($s3)
  .L150C47B0:
    /* F1C60 150C47B0 240AFFFF */  addiu      $t2, $zero, -0x1
    /* F1C64 150C47B4 3C0E800C */  lui        $t6, %hi(D_800BE9F0)
    /* F1C68 150C47B8 10400009 */  beqz       $v0, .L150C47E0
    /* F1C6C 150C47BC 3C0F800D */   lui       $t7, %hi(D_800CC2D0)
    /* F1C70 150C47C0 A04A0074 */  sb         $t2, 0x74($v0)
    /* F1C74 150C47C4 8EA10000 */  lw         $at, 0x0($s5)
    /* F1C78 150C47C8 8E6B000C */  lw         $t3, 0xC($s3)
    /* F1C7C 150C47CC AD610040 */  sw         $at, 0x40($t3)
    /* F1C80 150C47D0 8EAD0004 */  lw         $t5, 0x4($s5)
    /* F1C84 150C47D4 AD6D0044 */  sw         $t5, 0x44($t3)
    /* F1C88 150C47D8 8EA10008 */  lw         $at, 0x8($s5)
    /* F1C8C 150C47DC AD610048 */  sw         $at, 0x48($t3)
  .L150C47E0:
    /* F1C90 150C47E0 8DCEE9F0 */  lw         $t6, %lo(D_800BE9F0)($t6)
    /* F1C94 150C47E4 24010002 */  addiu      $at, $zero, 0x2
    /* F1C98 150C47E8 24110001 */  addiu      $s1, $zero, 0x1
    /* F1C9C 150C47EC 15C1000B */  bne        $t6, $at, .L150C481C
    /* F1CA0 150C47F0 25EFC2D0 */   addiu     $t7, $t7, %lo(D_800CC2D0)
    /* F1CA4 150C47F4 020F2023 */  subu       $a0, $s0, $t7
    /* F1CA8 150C47F8 2401032C */  addiu      $at, $zero, 0x32C
    /* F1CAC 150C47FC 0081001A */  div        $zero, $a0, $at
    /* F1CB0 150C4800 00002012 */  mflo       $a0
    /* F1CB4 150C4804 24054065 */  addiu      $a1, $zero, 0x4065
    /* F1CB8 150C4808 0D428A72 */  jal        func_150A29C8
    /* F1CBC 150C480C 00000000 */   nop
    /* F1CC0 150C4810 14400002 */  bnez       $v0, .L150C481C
    /* F1CC4 150C4814 00000000 */   nop
    /* F1CC8 150C4818 00008825 */  or         $s1, $zero, $zero
  .L150C481C:
    /* F1CCC 150C481C 1220001F */  beqz       $s1, .L150C489C
    /* F1CD0 150C4820 00000000 */   nop
    /* F1CD4 150C4824 0D42B69A */  jal        func_150ADA68
    /* F1CD8 150C4828 00000000 */   nop
    /* F1CDC 150C482C 3C01800A */  lui        $at, %hi(D_800A03BC)
    /* F1CE0 150C4830 C42603BC */  lwc1       $f6, %lo(D_800A03BC)($at)
    /* F1CE4 150C4834 3C01800A */  lui        $at, %hi(D_800A03C0)
    /* F1CE8 150C4838 C42803C0 */  lwc1       $f8, %lo(D_800A03C0)($at)
    /* F1CEC 150C483C 3C01800C */  lui        $at, %hi(D_800BE9A4)
    /* F1CF0 150C4840 C432E9A4 */  lwc1       $f18, %lo(D_800BE9A4)($at)
    /* F1CF4 150C4844 46080402 */  mul.s      $f16, $f0, $f8
    /* F1CF8 150C4848 C6680008 */  lwc1       $f8, 0x8($s3)
    /* F1CFC 150C484C 46103280 */  add.s      $f10, $f6, $f16
    /* F1D00 150C4850 46125102 */  mul.s      $f4, $f10, $f18
    /* F1D04 150C4854 46044180 */  add.s      $f6, $f8, $f4
    /* F1D08 150C4858 E6660008 */  swc1       $f6, 0x8($s3)
    /* F1D0C 150C485C C6700008 */  lwc1       $f16, 0x8($s3)
    /* F1D10 150C4860 4610C03C */  c.lt.s     $f24, $f16
    /* F1D14 150C4864 00000000 */  nop
    /* F1D18 150C4868 4500000C */  bc1f       .L150C489C
    /* F1D1C 150C486C 02A02025 */   or        $a0, $s5, $zero
  .L150C4870:
    /* F1D20 150C4870 9285000C */  lbu        $a1, 0xC($s4)
    /* F1D24 150C4874 0D470DB6 */  jal        func_151C36D8
    /* F1D28 150C4878 92860001 */   lbu       $a2, 0x1($s4)
    /* F1D2C 150C487C C66A0008 */  lwc1       $f10, 0x8($s3)
    /* F1D30 150C4880 46185481 */  sub.s      $f18, $f10, $f24
    /* F1D34 150C4884 E6720008 */  swc1       $f18, 0x8($s3)
    /* F1D38 150C4888 C6680008 */  lwc1       $f8, 0x8($s3)
    /* F1D3C 150C488C 4608C03C */  c.lt.s     $f24, $f8
    /* F1D40 150C4890 00000000 */  nop
    /* F1D44 150C4894 4503FFF6 */  bc1tl      .L150C4870
    /* F1D48 150C4898 02A02025 */   or        $a0, $s5, $zero
  .L150C489C:
    /* F1D4C 150C489C 0D42B69A */  jal        func_150ADA68
    /* F1D50 150C48A0 00000000 */   nop
    /* F1D54 150C48A4 3C01800A */  lui        $at, %hi(D_800A03C4)
    /* F1D58 150C48A8 C42403C4 */  lwc1       $f4, %lo(D_800A03C4)($at)
    /* F1D5C 150C48AC 3C01800A */  lui        $at, %hi(D_800A03C8)
    /* F1D60 150C48B0 C42603C8 */  lwc1       $f6, %lo(D_800A03C8)($at)
    /* F1D64 150C48B4 3C01800C */  lui        $at, %hi(D_800BE9A4)
    /* F1D68 150C48B8 C432E9A4 */  lwc1       $f18, %lo(D_800BE9A4)($at)
    /* F1D6C 150C48BC 46060402 */  mul.s      $f16, $f0, $f6
    /* F1D70 150C48C0 C6660010 */  lwc1       $f6, 0x10($s3)
    /* F1D74 150C48C4 02002025 */  or         $a0, $s0, $zero
    /* F1D78 150C48C8 46102280 */  add.s      $f10, $f4, $f16
    /* F1D7C 150C48CC 46125202 */  mul.s      $f8, $f10, $f18
    /* F1D80 150C48D0 46083100 */  add.s      $f4, $f6, $f8
    /* F1D84 150C48D4 E6640010 */  swc1       $f4, 0x10($s3)
    /* F1D88 150C48D8 C6700010 */  lwc1       $f16, 0x10($s3)
    /* F1D8C 150C48DC 4610C03C */  c.lt.s     $f24, $f16
    /* F1D90 150C48E0 00000000 */  nop
    /* F1D94 150C48E4 45020070 */  bc1fl      .L150C4AA8
    /* F1D98 150C48E8 8FBF007C */   lw        $ra, 0x7C($sp)
    /* F1D9C 150C48EC 0D45703E */  jal        func_1515C0F8
    /* F1DA0 150C48F0 27A500AC */   addiu     $a1, $sp, 0xAC
    /* F1DA4 150C48F4 14400004 */  bnez       $v0, .L150C4908
    /* F1DA8 150C48F8 3C01800A */   lui       $at, %hi(D_800A03CC)
    /* F1DAC 150C48FC 3C19800A */  lui        $t9, %hi(D_800A5480)
    /* F1DB0 150C4900 27395480 */  addiu      $t9, $t9, %lo(D_800A5480)
    /* F1DB4 150C4904 AFB900AC */  sw         $t9, 0xAC($sp)
  .L150C4908:
    /* F1DB8 150C4908 C43A03CC */  lwc1       $f26, %lo(D_800A03CC)($at)
    /* F1DBC 150C490C 27B200A0 */  addiu      $s2, $sp, 0xA0
  .L150C4910:
    /* F1DC0 150C4910 0D42B688 */  jal        func_150ADA20
    /* F1DC4 150C4914 00000000 */   nop
    /* F1DC8 150C4918 0D42B688 */  jal        func_150ADA20
    /* F1DCC 150C491C 00408825 */   or        $s1, $v0, $zero
    /* F1DD0 150C4920 0D42B69A */  jal        func_150ADA68
    /* F1DD4 150C4924 00408025 */   or        $s0, $v0, $zero
    /* F1DD8 150C4928 24010019 */  addiu      $at, $zero, 0x19
    /* F1DDC 150C492C 0201001B */  divu       $zero, $s0, $at
    /* F1DE0 150C4930 3C01800A */  lui        $at, %hi(D_800A03D0)
    /* F1DE4 150C4934 C42A03D0 */  lwc1       $f10, %lo(D_800A03D0)($at)
    /* F1DE8 150C4938 3C01800A */  lui        $at, %hi(D_800A03D4)
    /* F1DEC 150C493C C42603D4 */  lwc1       $f6, %lo(D_800A03D4)($at)
    /* F1DF0 150C4940 460A0482 */  mul.s      $f18, $f0, $f10
    /* F1DF4 150C4944 00002810 */  mfhi       $a1
    /* F1DF8 150C4948 24A5FFC0 */  addiu      $a1, $a1, -0x40
    /* F1DFC 150C494C 322400FF */  andi       $a0, $s1, 0xFF
    /* F1E00 150C4950 00044400 */  sll        $t0, $a0, 16
    /* F1E04 150C4954 00055400 */  sll        $t2, $a1, 16
    /* F1E08 150C4958 000A2C03 */  sra        $a1, $t2, 16
    /* F1E0C 150C495C 46069200 */  add.s      $f8, $f18, $f6
    /* F1E10 150C4960 00082403 */  sra        $a0, $t0, 16
    /* F1E14 150C4964 02403825 */  or         $a3, $s2, $zero
    /* F1E18 150C4968 44064000 */  mfc1       $a2, $f8
    /* F1E1C 150C496C 0D450DE5 */  jal        func_15143794
    /* F1E20 150C4970 00000000 */   nop
    /* F1E24 150C4974 8FAB00AC */  lw         $t3, 0xAC($sp)
    /* F1E28 150C4978 C7A400A0 */  lwc1       $f4, 0xA0($sp)
    /* F1E2C 150C497C C7A600A8 */  lwc1       $f6, 0xA8($sp)
    /* F1E30 150C4980 C5700000 */  lwc1       $f16, 0x0($t3)
    /* F1E34 150C4984 461A8282 */  mul.s      $f10, $f16, $f26
    /* F1E38 150C4988 460A2481 */  sub.s      $f18, $f4, $f10
    /* F1E3C 150C498C E7B200A0 */  swc1       $f18, 0xA0($sp)
    /* F1E40 150C4990 C5680008 */  lwc1       $f8, 0x8($t3)
    /* F1E44 150C4994 461A4402 */  mul.s      $f16, $f8, $f26
    /* F1E48 150C4998 46103101 */  sub.s      $f4, $f6, $f16
    /* F1E4C 150C499C 0D42B69A */  jal        func_150ADA68
    /* F1E50 150C49A0 E7A400A8 */   swc1      $f4, 0xA8($sp)
    /* F1E54 150C49A4 0D42B688 */  jal        func_150ADA20
    /* F1E58 150C49A8 46000506 */   mov.s     $f20, $f0
    /* F1E5C 150C49AC 0D42B688 */  jal        func_150ADA20
    /* F1E60 150C49B0 00408825 */   or        $s1, $v0, $zero
    /* F1E64 150C49B4 0D42B69A */  jal        func_150ADA68
    /* F1E68 150C49B8 00408025 */   or        $s0, $v0, $zero
    /* F1E6C 150C49BC 0D42B69A */  jal        func_150ADA68
    /* F1E70 150C49C0 46000586 */   mov.s     $f22, $f0
    /* F1E74 150C49C4 3C01800A */  lui        $at, %hi(D_800A03D8)
    /* F1E78 150C49C8 C42A03D8 */  lwc1       $f10, %lo(D_800A03D8)($at)
    /* F1E7C 150C49CC 3C01800A */  lui        $at, %hi(D_800A03DC)
    /* F1E80 150C49D0 C42803DC */  lwc1       $f8, %lo(D_800A03DC)($at)
    /* F1E84 150C49D4 24010029 */  addiu      $at, $zero, 0x29
    /* F1E88 150C49D8 0221001B */  divu       $zero, $s1, $at
    /* F1E8C 150C49DC 24010038 */  addiu      $at, $zero, 0x38
    /* F1E90 150C49E0 00006810 */  mfhi       $t5
    /* F1E94 150C49E4 460AA482 */  mul.s      $f18, $f20, $f10
    /* F1E98 150C49E8 25AE003C */  addiu      $t6, $t5, 0x3C
    /* F1E9C 150C49EC 0201001B */  divu       $zero, $s0, $at
    /* F1EA0 150C49F0 3C014320 */  lui        $at, (0x43200000 >> 16)
    /* F1EA4 150C49F4 44818000 */  mtc1       $at, $f16
    /* F1EA8 150C49F8 3C0142F2 */  lui        $at, (0x42F20000 >> 16)
    /* F1EAC 150C49FC 44815000 */  mtc1       $at, $f10
    /* F1EB0 150C4A00 4610B102 */  mul.s      $f4, $f22, $f16
    /* F1EB4 150C4A04 46089180 */  add.s      $f6, $f18, $f8
    /* F1EB8 150C4A08 3C01800A */  lui        $at, %hi(D_800A03E0)
    /* F1EBC 150C4A0C C42803E0 */  lwc1       $f8, %lo(D_800A03E0)($at)
    /* F1EC0 150C4A10 00007810 */  mfhi       $t7
    /* F1EC4 150C4A14 25F800C8 */  addiu      $t8, $t7, 0xC8
    /* F1EC8 150C4A18 4608003C */  c.lt.s     $f0, $f8
    /* F1ECC 150C4A1C 44073000 */  mfc1       $a3, $f6
    /* F1ED0 150C4A20 460A2480 */  add.s      $f18, $f4, $f10
    /* F1ED4 150C4A24 AFB80014 */  sw         $t8, 0x14($sp)
    /* F1ED8 150C4A28 AFAE0010 */  sw         $t6, 0x10($sp)
    /* F1EDC 150C4A2C 02A02025 */  or         $a0, $s5, $zero
    /* F1EE0 150C4A30 E7B20018 */  swc1       $f18, 0x18($sp)
    /* F1EE4 150C4A34 02402825 */  or         $a1, $s2, $zero
    /* F1EE8 150C4A38 2406000C */  addiu      $a2, $zero, 0xC
    /* F1EEC 150C4A3C 45000002 */  bc1f       .L150C4A48
    /* F1EF0 150C4A40 0000C825 */   or        $t9, $zero, $zero
    /* F1EF4 150C4A44 24190001 */  addiu      $t9, $zero, 0x1
  .L150C4A48:
    /* F1EF8 150C4A48 27A800C0 */  addiu      $t0, $sp, 0xC0
    /* F1EFC 150C4A4C 24090001 */  addiu      $t1, $zero, 0x1
    /* F1F00 150C4A50 240A0001 */  addiu      $t2, $zero, 0x1
    /* F1F04 150C4A54 AFAA0034 */  sw         $t2, 0x34($sp)
    /* F1F08 150C4A58 AFA90030 */  sw         $t1, 0x30($sp)
    /* F1F0C 150C4A5C AFA8002C */  sw         $t0, 0x2C($sp)
    /* F1F10 150C4A60 AFB9001C */  sw         $t9, 0x1C($sp)
    /* F1F14 150C4A64 E7B80020 */  swc1       $f24, 0x20($sp)
    /* F1F18 150C4A68 E7B80024 */  swc1       $f24, 0x24($sp)
    /* F1F1C 150C4A6C AFA00028 */  sw         $zero, 0x28($sp)
    /* F1F20 150C4A70 928C000C */  lbu        $t4, 0xC($s4)
    /* F1F24 150C4A74 AFAC0038 */  sw         $t4, 0x38($sp)
    /* F1F28 150C4A78 928B0001 */  lbu        $t3, 0x1($s4)
    /* F1F2C 150C4A7C 0D476405 */  jal        func_151D9014
    /* F1F30 150C4A80 AFAB003C */   sw        $t3, 0x3C($sp)
    /* F1F34 150C4A84 C6660010 */  lwc1       $f6, 0x10($s3)
    /* F1F38 150C4A88 46183401 */  sub.s      $f16, $f6, $f24
    /* F1F3C 150C4A8C E6700010 */  swc1       $f16, 0x10($s3)
    /* F1F40 150C4A90 C6640010 */  lwc1       $f4, 0x10($s3)
    /* F1F44 150C4A94 4604C03C */  c.lt.s     $f24, $f4
    /* F1F48 150C4A98 00000000 */  nop
    /* F1F4C 150C4A9C 4501FF9C */  bc1t       .L150C4910
    /* F1F50 150C4AA0 00000000 */   nop
  .L150C4AA4:
    /* F1F54 150C4AA4 8FBF007C */  lw         $ra, 0x7C($sp)
  .L150C4AA8:
    /* F1F58 150C4AA8 D7B40040 */  ldc1       $f20, 0x40($sp)
    /* F1F5C 150C4AAC D7B60048 */  ldc1       $f22, 0x48($sp)
    /* F1F60 150C4AB0 D7B80050 */  ldc1       $f24, 0x50($sp)
    /* F1F64 150C4AB4 D7BA0058 */  ldc1       $f26, 0x58($sp)
    /* F1F68 150C4AB8 8FB00064 */  lw         $s0, 0x64($sp)
    /* F1F6C 150C4ABC 8FB10068 */  lw         $s1, 0x68($sp)
    /* F1F70 150C4AC0 8FB2006C */  lw         $s2, 0x6C($sp)
    /* F1F74 150C4AC4 8FB30070 */  lw         $s3, 0x70($sp)
    /* F1F78 150C4AC8 8FB40074 */  lw         $s4, 0x74($sp)
    /* F1F7C 150C4ACC 8FB50078 */  lw         $s5, 0x78($sp)
    /* F1F80 150C4AD0 03E00008 */  jr         $ra
    /* F1F84 150C4AD4 27BD0110 */   addiu     $sp, $sp, 0x110
endlabel func_150C44A4
