glabel func_150A44F0
    /* D19A0 150A44F0 1080013E */  beqz       $a0, .L150A49EC
    /* D19A4 150A44F4 00000000 */   nop
    /* D19A8 150A44F8 27BDFFA8 */  addiu      $sp, $sp, -0x58
    /* D19AC 150A44FC AFB00010 */  sw         $s0, 0x10($sp)
    /* D19B0 150A4500 AFB10014 */  sw         $s1, 0x14($sp)
    /* D19B4 150A4504 AFB20018 */  sw         $s2, 0x18($sp)
    /* D19B8 150A4508 AFB3001C */  sw         $s3, 0x1C($sp)
    /* D19BC 150A450C AFB40020 */  sw         $s4, 0x20($sp)
    /* D19C0 150A4510 AFB50024 */  sw         $s5, 0x24($sp)
    /* D19C4 150A4514 AFB60028 */  sw         $s6, 0x28($sp)
    /* D19C8 150A4518 AFB7002C */  sw         $s7, 0x2C($sp)
    /* D19CC 150A451C AFBE0030 */  sw         $fp, 0x30($sp)
    /* D19D0 150A4520 AFBC0034 */  sw         $gp, 0x34($sp)
    /* D19D4 150A4524 AFBF0038 */  sw         $ra, 0x38($sp)
    /* D19D8 150A4528 E7B4003C */  swc1       $f20, 0x3C($sp)
    /* D19DC 150A452C E7B50040 */  swc1       $f21, 0x40($sp)
    /* D19E0 150A4530 E7B60044 */  swc1       $f22, 0x44($sp)
    /* D19E4 150A4534 E7B70048 */  swc1       $f23, 0x48($sp)
    /* D19E8 150A4538 E7B8004C */  swc1       $f24, 0x4C($sp)
    /* D19EC 150A453C E7B90050 */  swc1       $f25, 0x50($sp)
    /* D19F0 150A4540 00C03825 */  or         $a3, $a2, $zero
    /* D19F4 150A4544 4487C000 */  mtc1       $a3, $f24
    /* D19F8 150A4548 00000000 */  nop
    /* D19FC 150A454C 00A08025 */  or         $s0, $a1, $zero
    /* D1A00 150A4550 00042040 */  sll        $a0, $a0, 1
    /* D1A04 150A4554 02048821 */  addu       $s1, $s0, $a0
    /* D1A08 150A4558 3C1C800C */  lui        $gp, (0x800C0000 >> 16)
    /* D1A0C 150A455C 939CE9C0 */  lbu        $gp, -0x1640($gp)
    /* D1A10 150A4560 2631FFFE */  addiu      $s1, $s1, -0x2
    /* D1A14 150A4564 001CE080 */  sll        $gp, $gp, 2
    /* D1A18 150A4568 3C14800E */  lui        $s4, %hi(D_800DBE40)
    /* D1A1C 150A456C 8E94BE40 */  lw         $s4, %lo(D_800DBE40)($s4)
    /* D1A20 150A4570 3C15800E */  lui        $s5, %hi(D_800DBE44)
    /* D1A24 150A4574 8EB5BE44 */  lw         $s5, %lo(D_800DBE44)($s5)
    /* D1A28 150A4578 3C16800E */  lui        $s6, %hi(D_800DBE3C)
    /* D1A2C 150A457C 8ED6BE3C */  lw         $s6, %lo(D_800DBE3C)($s6)
    /* D1A30 150A4580 3C17800E */  lui        $s7, %hi(D_800DBEF8)
    /* D1A34 150A4584 8EF7BEF8 */  lw         $s7, %lo(D_800DBEF8)($s7)
    /* D1A38 150A4588 3C1E800E */  lui        $fp, %hi(D_800DBEF4)
    /* D1A3C 150A458C 8FDEBEF4 */  lw         $fp, %lo(D_800DBEF4)($fp)
    /* D1A40 150A4590 3C08800E */  lui        $t0, %hi(D_800DBEFC)
    /* D1A44 150A4594 8D08BEFC */  lw         $t0, %lo(D_800DBEFC)($t0)
    /* D1A48 150A4598 4488B800 */  mtc1       $t0, $f23
    /* D1A4C 150A459C 00000000 */  nop
    /* D1A50 150A45A0 3C01800A */  lui        $at, %hi(D_8009F680)
    /* D1A54 150A45A4 C434F680 */  lwc1       $f20, %lo(D_8009F680)($at)
  .L150A45A8:
    /* D1A58 150A45A8 AFA00054 */  sw         $zero, 0x54($sp)
    /* D1A5C 150A45AC 96120000 */  lhu        $s2, 0x0($s0)
    /* D1A60 150A45B0 440AB800 */  mfc1       $t2, $f23
    /* D1A64 150A45B4 01525021 */  addu       $t2, $t2, $s2
    /* D1A68 150A45B8 00124080 */  sll        $t0, $s2, 2
    /* D1A6C 150A45BC 02E84821 */  addu       $t1, $s7, $t0
    /* D1A70 150A45C0 8D280000 */  lw         $t0, 0x0($t1)
    /* D1A74 150A45C4 240B0003 */  addiu      $t3, $zero, 0x3
    /* D1A78 150A45C8 150000EF */  bnez       $t0, .L150A4988
    /* D1A7C 150A45CC A14B0000 */   sb        $t3, 0x0($t2)
    /* D1A80 150A45D0 240800A0 */  addiu      $t0, $zero, 0xA0
    /* D1A84 150A45D4 01120018 */  mult       $t0, $s2
    /* D1A88 150A45D8 00009012 */  mflo       $s2
    /* D1A8C 150A45DC 4407C000 */  mfc1       $a3, $f24
    /* D1A90 150A45E0 14E00013 */  bnez       $a3, .L150A4630
    /* D1A94 150A45E4 025E9021 */   addu      $s2, $s2, $fp
    /* D1A98 150A45E8 924B0070 */  lbu        $t3, 0x70($s2)
    /* D1A9C 150A45EC 316B0001 */  andi       $t3, $t3, 0x1
    /* D1AA0 150A45F0 1160000F */  beqz       $t3, .L150A4630
    /* D1AA4 150A45F4 03925821 */   addu      $t3, $gp, $s2
    /* D1AA8 150A45F8 8D730020 */  lw         $s3, 0x20($t3)
    /* D1AAC 150A45FC 09429226 */  j          func_150A4898
    /* D1AB0 150A4600 AD330000 */   sw        $s3, 0x0($t1)
  .L150A4604:
    /* D1AB4 150A4604 96440016 */  lhu        $a0, 0x16($s2)
    /* D1AB8 150A4608 24050001 */  addiu      $a1, $zero, 0x1
    /* D1ABC 150A460C 24060000 */  addiu      $a2, $zero, 0x0
    /* D1AC0 150A4610 24070002 */  addiu      $a3, $zero, 0x2
    /* D1AC4 150A4614 00042100 */  sll        $a0, $a0, 4
    /* D1AC8 150A4618 0C000F10 */  jal        allocate_memory
    /* D1ACC 150A461C 00000000 */   nop
    /* D1AD0 150A4620 AFA20054 */  sw         $v0, 0x54($sp)
    /* D1AD4 150A4624 00409825 */  or         $s3, $v0, $zero
    /* D1AD8 150A4628 0942919C */  j          func_150A4670
    /* D1ADC 150A462C 00000000 */   nop
  .L150A4630:
    /* D1AE0 150A4630 14E0FFF4 */  bnez       $a3, .L150A4604
    /* D1AE4 150A4634 01209825 */   or        $s3, $t1, $zero
    /* D1AE8 150A4638 9244004E */  lbu        $a0, 0x4E($s2)
    /* D1AEC 150A463C 24010003 */  addiu      $at, $zero, 0x3
    /* D1AF0 150A4640 14810002 */  bne        $a0, $at, .L150A464C
    /* D1AF4 150A4644 8E650000 */   lw        $a1, 0x0($s3)
    /* D1AF8 150A4648 14A000CF */  bnez       $a1, .L150A4988
  .L150A464C:
    /* D1AFC 150A464C 96440016 */   lhu       $a0, 0x16($s2)
    /* D1B00 150A4650 24050001 */  addiu      $a1, $zero, 0x1
    /* D1B04 150A4654 00042100 */  sll        $a0, $a0, 4
    /* D1B08 150A4658 24060000 */  addiu      $a2, $zero, 0x0
    /* D1B0C 150A465C 0C000F10 */  jal        allocate_memory
    /* D1B10 150A4660 24070002 */   addiu     $a3, $zero, 0x2
    /* D1B14 150A4664 AE620000 */  sw         $v0, 0x0($s3)
    /* D1B18 150A4668 104000C7 */  beqz       $v0, .L150A4988
    /* D1B1C 150A466C 00409825 */   or        $s3, $v0, $zero
endlabel func_150A44F0
