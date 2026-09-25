glabel func_151D469C
    /* 201B4C 151D469C 27BDFFA8 */  addiu      $sp, $sp, -0x58
    /* 201B50 151D46A0 AFBF002C */  sw         $ra, 0x2C($sp)
    /* 201B54 151D46A4 AFA5005C */  sw         $a1, 0x5C($sp)
    /* 201B58 151D46A8 AFA60060 */  sw         $a2, 0x60($sp)
    /* 201B5C 151D46AC AFA70064 */  sw         $a3, 0x64($sp)
    /* 201B60 151D46B0 AFA40038 */  sw         $a0, 0x38($sp)
    /* 201B64 151D46B4 908E003B */  lbu        $t6, 0x3B($a0)
    /* 201B68 151D46B8 93AF005F */  lbu        $t7, 0x5F($sp)
    /* 201B6C 151D46BC 44802000 */  mtc1       $zero, $f4
    /* 201B70 151D46C0 2418FFFF */  addiu      $t8, $zero, -0x1
    /* 201B74 151D46C4 24010006 */  addiu      $at, $zero, 0x6
    /* 201B78 151D46C8 A7B8003E */  sh         $t8, 0x3E($sp)
    /* 201B7C 151D46CC A3A00048 */  sb         $zero, 0x48($sp)
    /* 201B80 151D46D0 A3AE003C */  sb         $t6, 0x3C($sp)
    /* 201B84 151D46D4 A3AF0040 */  sb         $t7, 0x40($sp)
    /* 201B88 151D46D8 15E10003 */  bne        $t7, $at, .L151D46E8
    /* 201B8C 151D46DC E7A40044 */   swc1      $f4, 0x44($sp)
    /* 201B90 151D46E0 24190082 */  addiu      $t9, $zero, 0x82
    /* 201B94 151D46E4 A7B9003E */  sh         $t9, 0x3E($sp)
  .L151D46E8:
    /* 201B98 151D46E8 8C8801D4 */  lw         $t0, 0x1D4($a0)
    /* 201B9C 151D46EC 51000012 */  beql       $t0, $zero, .L151D4738
    /* 201BA0 151D46F0 93A90067 */   lbu       $t1, 0x67($sp)
    /* 201BA4 151D46F4 90890074 */  lbu        $t1, 0x74($a0)
    /* 201BA8 151D46F8 93AB005F */  lbu        $t3, 0x5F($sp)
    /* 201BAC 151D46FC 2401000F */  addiu      $at, $zero, 0xF
    /* 201BB0 151D4700 312A000F */  andi       $t2, $t1, 0xF
    /* 201BB4 151D4704 1141000B */  beq        $t2, $at, .L151D4734
    /* 201BB8 151D4708 000B6080 */   sll       $t4, $t3, 2
    /* 201BBC 151D470C 3C198009 */  lui        $t9, %hi(D_8008FC70)
    /* 201BC0 151D4710 032CC821 */  addu       $t9, $t9, $t4
    /* 201BC4 151D4714 8F39FC70 */  lw         $t9, %lo(D_8008FC70)($t9)
    /* 201BC8 151D4718 87A5003E */  lh         $a1, 0x3E($sp)
    /* 201BCC 151D471C 27A6004C */  addiu      $a2, $sp, 0x4C
    /* 201BD0 151D4720 0320F809 */  jalr       $t9
    /* 201BD4 151D4724 00000000 */   nop
    /* 201BD8 151D4728 93AD0048 */  lbu        $t5, 0x48($sp)
    /* 201BDC 151D472C 35AE0001 */  ori        $t6, $t5, 0x1
    /* 201BE0 151D4730 A3AE0048 */  sb         $t6, 0x48($sp)
  .L151D4734:
    /* 201BE4 151D4734 93A90067 */  lbu        $t1, 0x67($sp)
  .L151D4738:
    /* 201BE8 151D4738 8FAA0068 */  lw         $t2, 0x68($sp)
    /* 201BEC 151D473C 24180001 */  addiu      $t8, $zero, 0x1
    /* 201BF0 151D4740 240F0035 */  addiu      $t7, $zero, 0x35
    /* 201BF4 151D4744 24080020 */  addiu      $t0, $zero, 0x20
    /* 201BF8 151D4748 AFA80018 */  sw         $t0, 0x18($sp)
    /* 201BFC 151D474C AFAF0014 */  sw         $t7, 0x14($sp)
    /* 201C00 151D4750 AFB80010 */  sw         $t8, 0x10($sp)
    /* 201C04 151D4754 87A40062 */  lh         $a0, 0x62($sp)
    /* 201C08 151D4758 2405FFFF */  addiu      $a1, $zero, -0x1
    /* 201C0C 151D475C 24060041 */  addiu      $a2, $zero, 0x41
    /* 201C10 151D4760 2407FFFF */  addiu      $a3, $zero, -0x1
    /* 201C14 151D4764 AFA9001C */  sw         $t1, 0x1C($sp)
    /* 201C18 151D4768 0D45244C */  jal        func_15149130
    /* 201C1C 151D476C AFAA0020 */   sw        $t2, 0x20($sp)
    /* 201C20 151D4770 10400004 */  beqz       $v0, .L151D4784
    /* 201C24 151D4774 24440028 */   addiu     $a0, $v0, 0x28
    /* 201C28 151D4778 27A50038 */  addiu      $a1, $sp, 0x38
    /* 201C2C 151D477C 0C008BB0 */  jal        memcpy
    /* 201C30 151D4780 24060020 */   addiu     $a2, $zero, 0x20
  .L151D4784:
    /* 201C34 151D4784 8FBF002C */  lw         $ra, 0x2C($sp)
    /* 201C38 151D4788 27BD0058 */  addiu      $sp, $sp, 0x58
    /* 201C3C 151D478C 03E00008 */  jr         $ra
    /* 201C40 151D4790 00000000 */   nop
endlabel func_151D469C
