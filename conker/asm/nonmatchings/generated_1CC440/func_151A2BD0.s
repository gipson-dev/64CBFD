glabel func_151A2BD0
    /* 1D0080 151A2BD0 27BDFFE8 */  addiu      $sp, $sp, -0x18
    /* 1D0084 151A2BD4 44876000 */  mtc1       $a3, $f12
    /* 1D0088 151A2BD8 AFBF0014 */  sw         $ra, 0x14($sp)
    /* 1D008C 151A2BDC AFA40018 */  sw         $a0, 0x18($sp)
    /* 1D0090 151A2BE0 AFA5001C */  sw         $a1, 0x1C($sp)
    /* 1D0094 151A2BE4 AFA60020 */  sw         $a2, 0x20($sp)
    /* 1D0098 151A2BE8 3C013F80 */  lui        $at, (0x3F800000 >> 16)
    /* 1D009C 151A2BEC 44812000 */  mtc1       $at, $f4
    /* 1D00A0 151A2BF0 C7A60028 */  lwc1       $f6, 0x28($sp)
    /* 1D00A4 151A2BF4 87A4001E */  lh         $a0, 0x1E($sp)
    /* 1D00A8 151A2BF8 87A50022 */  lh         $a1, 0x22($sp)
    /* 1D00AC 151A2BFC 46062201 */  sub.s      $f8, $f4, $f6
    /* 1D00B0 151A2C00 8FA7002C */  lw         $a3, 0x2C($sp)
    /* 1D00B4 151A2C04 460C4282 */  mul.s      $f10, $f8, $f12
    /* 1D00B8 151A2C08 44065000 */  mfc1       $a2, $f10
    /* 1D00BC 151A2C0C 0D450DE5 */  jal        func_15143794
    /* 1D00C0 151A2C10 00000000 */   nop
    /* 1D00C4 151A2C14 8FBF0014 */  lw         $ra, 0x14($sp)
    /* 1D00C8 151A2C18 27BD0018 */  addiu      $sp, $sp, 0x18
    /* 1D00CC 151A2C1C 03E00008 */  jr         $ra
    /* 1D00D0 151A2C20 00000000 */   nop
endlabel func_151A2BD0
