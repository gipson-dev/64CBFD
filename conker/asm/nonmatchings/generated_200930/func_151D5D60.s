glabel func_151D5D60
    /* 203210 151D5D60 27BDFFD8 */  addiu      $sp, $sp, -0x28
    /* 203214 151D5D64 AFA5002C */  sw         $a1, 0x2C($sp)
    /* 203218 151D5D68 00057400 */  sll        $t6, $a1, 16
    /* 20321C 151D5D6C 000E2C03 */  sra        $a1, $t6, 16
    /* 203220 151D5D70 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 203224 151D5D74 AFA40028 */  sw         $a0, 0x28($sp)
    /* 203228 151D5D78 AFA60030 */  sw         $a2, 0x30($sp)
    /* 20322C 151D5D7C AFA70034 */  sw         $a3, 0x34($sp)
    /* 203230 151D5D80 8FB80038 */  lw         $t8, 0x38($sp)
    /* 203234 151D5D84 27B90027 */  addiu      $t9, $sp, 0x27
    /* 203238 151D5D88 24060002 */  addiu      $a2, $zero, 0x2
    /* 20323C 151D5D8C 17000002 */  bnez       $t8, .L151D5D98
    /* 203240 151D5D90 24070001 */   addiu     $a3, $zero, 0x1
    /* 203244 151D5D94 AFB90038 */  sw         $t9, 0x38($sp)
  .L151D5D98:
    /* 203248 151D5D98 8FA80038 */  lw         $t0, 0x38($sp)
    /* 20324C 151D5D9C 00055080 */  sll        $t2, $a1, 2
    /* 203250 151D5DA0 A1000000 */  sb         $zero, 0x0($t0)
    /* 203254 151D5DA4 8FA90028 */  lw         $t1, 0x28($sp)
    /* 203258 151D5DA8 012A1821 */  addu       $v1, $t1, $t2
    /* 20325C 151D5DAC 8C640000 */  lw         $a0, 0x0($v1)
    /* 203260 151D5DB0 14800011 */  bnez       $a0, .L151D5DF8
    /* 203264 151D5DB4 00000000 */   nop
    /* 203268 151D5DB8 8FA40030 */  lw         $a0, 0x30($sp)
    /* 20326C 151D5DBC 24050001 */  addiu      $a1, $zero, 0x1
    /* 203270 151D5DC0 AFA3001C */  sw         $v1, 0x1C($sp)
    /* 203274 151D5DC4 00045840 */  sll        $t3, $a0, 1
    /* 203278 151D5DC8 0C000F10 */  jal        allocate_memory
    /* 20327C 151D5DCC 01602025 */   or        $a0, $t3, $zero
    /* 203280 151D5DD0 8FA3001C */  lw         $v1, 0x1C($sp)
    /* 203284 151D5DD4 14400004 */  bnez       $v0, .L151D5DE8
    /* 203288 151D5DD8 AC620000 */   sw        $v0, 0x0($v1)
    /* 20328C 151D5DDC 8FAC0034 */  lw         $t4, 0x34($sp)
    /* 203290 151D5DE0 1000000F */  b          .L151D5E20
    /* 203294 151D5DE4 AD800000 */   sw        $zero, 0x0($t4)
  .L151D5DE8:
    /* 203298 151D5DE8 8FAE0038 */  lw         $t6, 0x38($sp)
    /* 20329C 151D5DEC 240D0001 */  addiu      $t5, $zero, 0x1
    /* 2032A0 151D5DF0 A1CD0000 */  sb         $t5, 0x0($t6)
    /* 2032A4 151D5DF4 8C640000 */  lw         $a0, 0x0($v1)
  .L151D5DF8:
    /* 2032A8 151D5DF8 3C0F800C */  lui        $t7, %hi(D_800BE9C0)
    /* 2032AC 151D5DFC 91EFE9C0 */  lbu        $t7, %lo(D_800BE9C0)($t7)
    /* 2032B0 151D5E00 8FB90034 */  lw         $t9, 0x34($sp)
    /* 2032B4 151D5E04 8FA20030 */  lw         $v0, 0x30($sp)
    /* 2032B8 151D5E08 11E00003 */  beqz       $t7, .L151D5E18
    /* 2032BC 151D5E0C 00000000 */   nop
    /* 2032C0 151D5E10 10000001 */  b          .L151D5E18
    /* 2032C4 151D5E14 00001025 */   or        $v0, $zero, $zero
  .L151D5E18:
    /* 2032C8 151D5E18 0044C021 */  addu       $t8, $v0, $a0
    /* 2032CC 151D5E1C AF380000 */  sw         $t8, 0x0($t9)
  .L151D5E20:
    /* 2032D0 151D5E20 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 2032D4 151D5E24 27BD0028 */  addiu      $sp, $sp, 0x28
    /* 2032D8 151D5E28 03E00008 */  jr         $ra
    /* 2032DC 151D5E2C 00000000 */   nop
endlabel func_151D5D60
