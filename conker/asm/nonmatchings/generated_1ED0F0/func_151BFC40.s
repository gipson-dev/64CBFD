glabel func_151BFC40
    /* 1ED0F0 151BFC40 3C038008 */  lui        $v1, %hi(D_80082FA0)
    /* 1ED0F4 151BFC44 24632FA0 */  addiu      $v1, $v1, %lo(D_80082FA0)
    /* 1ED0F8 151BFC48 240E0003 */  addiu      $t6, $zero, 0x3
    /* 1ED0FC 151BFC4C AC8E0000 */  sw         $t6, 0x0($a0)
    /* 1ED100 151BFC50 8C6F0000 */  lw         $t7, 0x0($v1)
    /* 1ED104 151BFC54 24180004 */  addiu      $t8, $zero, 0x4
    /* 1ED108 151BFC58 240B0003 */  addiu      $t3, $zero, 0x3
    /* 1ED10C 151BFC5C 29E10002 */  slti       $at, $t7, 0x2
    /* 1ED110 151BFC60 14200003 */  bnez       $at, .L151BFC70
    /* 1ED114 151BFC64 240D0019 */   addiu     $t5, $zero, 0x19
    /* 1ED118 151BFC68 10000002 */  b          .L151BFC74
    /* 1ED11C 151BFC6C 24020001 */   addiu     $v0, $zero, 0x1
  .L151BFC70:
    /* 1ED120 151BFC70 00001025 */  or         $v0, $zero, $zero
  .L151BFC74:
    /* 1ED124 151BFC74 3C0143F7 */  lui        $at, (0x43F70000 >> 16)
    /* 1ED128 151BFC78 44812000 */  mtc1       $at, $f4
    /* 1ED12C 151BFC7C 0058C807 */  srav       $t9, $t8, $v0
    /* 1ED130 151BFC80 AC990004 */  sw         $t9, 0x4($a0)
    /* 1ED134 151BFC84 3C01800B */  lui        $at, %hi(D_800AA97C)
    /* 1ED138 151BFC88 E4A40000 */  swc1       $f4, 0x0($a1)
    /* 1ED13C 151BFC8C C426A97C */  lwc1       $f6, %lo(D_800AA97C)($at)
    /* 1ED140 151BFC90 3C01800B */  lui        $at, %hi(D_800AA980)
    /* 1ED144 151BFC94 24080007 */  addiu      $t0, $zero, 0x7
    /* 1ED148 151BFC98 E4860014 */  swc1       $f6, 0x14($a0)
    /* 1ED14C 151BFC9C C428A980 */  lwc1       $f8, %lo(D_800AA980)($at)
    /* 1ED150 151BFCA0 3C014234 */  lui        $at, (0x42340000 >> 16)
    /* 1ED154 151BFCA4 44815000 */  mtc1       $at, $f10
    /* 1ED158 151BFCA8 3C014254 */  lui        $at, (0x42540000 >> 16)
    /* 1ED15C 151BFCAC 44818000 */  mtc1       $at, $f16
    /* 1ED160 151BFCB0 3C01434B */  lui        $at, (0x434B0000 >> 16)
    /* 1ED164 151BFCB4 44819000 */  mtc1       $at, $f18
    /* 1ED168 151BFCB8 3C0143CF */  lui        $at, (0x43CF0000 >> 16)
    /* 1ED16C 151BFCBC 44812000 */  mtc1       $at, $f4
    /* 1ED170 151BFCC0 AC88002C */  sw         $t0, 0x2C($a0)
    /* 1ED174 151BFCC4 E4880018 */  swc1       $f8, 0x18($a0)
    /* 1ED178 151BFCC8 E48A001C */  swc1       $f10, 0x1C($a0)
    /* 1ED17C 151BFCCC E4900020 */  swc1       $f16, 0x20($a0)
    /* 1ED180 151BFCD0 E4920024 */  swc1       $f18, 0x24($a0)
    /* 1ED184 151BFCD4 E4840028 */  swc1       $f4, 0x28($a0)
    /* 1ED188 151BFCD8 8C690000 */  lw         $t1, 0x0($v1)
    /* 1ED18C 151BFCDC 24050064 */  addiu      $a1, $zero, 0x64
    /* 1ED190 151BFCE0 3C0A8009 */  lui        $t2, %hi(D_8008FD8C)
    /* 1ED194 151BFCE4 29210002 */  slti       $at, $t1, 0x2
    /* 1ED198 151BFCE8 10200006 */  beqz       $at, .L151BFD04
    /* 1ED19C 151BFCEC 240E000F */   addiu     $t6, $zero, 0xF
    /* 1ED1A0 151BFCF0 814AFD8C */  lb         $t2, %lo(D_8008FD8C)($t2)
    /* 1ED1A4 151BFCF4 00001025 */  or         $v0, $zero, $zero
    /* 1ED1A8 151BFCF8 29410008 */  slti       $at, $t2, 0x8
    /* 1ED1AC 151BFCFC 14200003 */  bnez       $at, .L151BFD0C
    /* 1ED1B0 151BFD00 00000000 */   nop
  .L151BFD04:
    /* 1ED1B4 151BFD04 10000001 */  b          .L151BFD0C
    /* 1ED1B8 151BFD08 24020001 */   addiu     $v0, $zero, 0x1
  .L151BFD0C:
    /* 1ED1BC 151BFD0C 3C014170 */  lui        $at, (0x41700000 >> 16)
    /* 1ED1C0 151BFD10 44813000 */  mtc1       $at, $f6
    /* 1ED1C4 151BFD14 004B6007 */  srav       $t4, $t3, $v0
    /* 1ED1C8 151BFD18 AC8C0030 */  sw         $t4, 0x30($a0)
    /* 1ED1CC 151BFD1C 3C01800B */  lui        $at, %hi(D_800AA984)
    /* 1ED1D0 151BFD20 E4860034 */  swc1       $f6, 0x34($a0)
    /* 1ED1D4 151BFD24 C428A984 */  lwc1       $f8, %lo(D_800AA984)($at)
    /* 1ED1D8 151BFD28 3C01800B */  lui        $at, %hi(D_800AA988)
    /* 1ED1DC 151BFD2C 240F000C */  addiu      $t7, $zero, 0xC
    /* 1ED1E0 151BFD30 E4880038 */  swc1       $f8, 0x38($a0)
    /* 1ED1E4 151BFD34 C42AA988 */  lwc1       $f10, %lo(D_800AA988)($at)
    /* 1ED1E8 151BFD38 3C01800B */  lui        $at, %hi(D_800AA98C)
    /* 1ED1EC 151BFD3C 24180014 */  addiu      $t8, $zero, 0x14
    /* 1ED1F0 151BFD40 E48A003C */  swc1       $f10, 0x3C($a0)
    /* 1ED1F4 151BFD44 C430A98C */  lwc1       $f16, %lo(D_800AA98C)($at)
    /* 1ED1F8 151BFD48 A48D0044 */  sh         $t5, 0x44($a0)
    /* 1ED1FC 151BFD4C A48E0046 */  sh         $t6, 0x46($a0)
    /* 1ED200 151BFD50 A4850048 */  sh         $a1, 0x48($a0)
    /* 1ED204 151BFD54 A485004A */  sh         $a1, 0x4A($a0)
    /* 1ED208 151BFD58 A48F004C */  sh         $t7, 0x4C($a0)
    /* 1ED20C 151BFD5C A498004E */  sh         $t8, 0x4E($a0)
    /* 1ED210 151BFD60 E4900040 */  swc1       $f16, 0x40($a0)
    /* 1ED214 151BFD64 8C790000 */  lw         $t9, 0x0($v1)
    /* 1ED218 151BFD68 3C088009 */  lui        $t0, %hi(D_8008FD8C)
    /* 1ED21C 151BFD6C 2409FFFF */  addiu      $t1, $zero, -0x1
    /* 1ED220 151BFD70 2B210002 */  slti       $at, $t9, 0x2
    /* 1ED224 151BFD74 10200005 */  beqz       $at, .L151BFD8C
    /* 1ED228 151BFD78 00000000 */   nop
    /* 1ED22C 151BFD7C 8108FD8C */  lb         $t0, %lo(D_8008FD8C)($t0)
    /* 1ED230 151BFD80 29010008 */  slti       $at, $t0, 0x8
    /* 1ED234 151BFD84 54200004 */  bnel       $at, $zero, .L151BFD98
    /* 1ED238 151BFD88 A0800050 */   sb        $zero, 0x50($a0)
  .L151BFD8C:
    /* 1ED23C 151BFD8C 03E00008 */  jr         $ra
    /* 1ED240 151BFD90 A0890050 */   sb        $t1, 0x50($a0)
    /* 1ED244 151BFD94 A0800050 */  sb         $zero, 0x50($a0)
  .L151BFD98:
    /* 1ED248 151BFD98 03E00008 */  jr         $ra
    /* 1ED24C 151BFD9C 00000000 */   nop
endlabel func_151BFC40
