glabel func_150A4B04
    /* D1FB4 150A4B04 27BDFF90 */  addiu      $sp, $sp, -0x70
    /* D1FB8 150A4B08 AFB00010 */  sw         $s0, 0x10($sp)
    /* D1FBC 150A4B0C AFB10014 */  sw         $s1, 0x14($sp)
    /* D1FC0 150A4B10 AFB20018 */  sw         $s2, 0x18($sp)
    /* D1FC4 150A4B14 AFB3001C */  sw         $s3, 0x1C($sp)
    /* D1FC8 150A4B18 AFB40020 */  sw         $s4, 0x20($sp)
    /* D1FCC 150A4B1C AFB50024 */  sw         $s5, 0x24($sp)
    /* D1FD0 150A4B20 AFB60028 */  sw         $s6, 0x28($sp)
    /* D1FD4 150A4B24 AFB7002C */  sw         $s7, 0x2C($sp)
    /* D1FD8 150A4B28 AFBE0030 */  sw         $fp, 0x30($sp)
    /* D1FDC 150A4B2C AFBC0034 */  sw         $gp, 0x34($sp)
    /* D1FE0 150A4B30 E7B40038 */  swc1       $f20, 0x38($sp)
    /* D1FE4 150A4B34 E7B5003C */  swc1       $f21, 0x3C($sp)
    /* D1FE8 150A4B38 E7B60040 */  swc1       $f22, 0x40($sp)
    /* D1FEC 150A4B3C E7B70044 */  swc1       $f23, 0x44($sp)
    /* D1FF0 150A4B40 E7B80048 */  swc1       $f24, 0x48($sp)
    /* D1FF4 150A4B44 E7B9004C */  swc1       $f25, 0x4C($sp)
    /* D1FF8 150A4B48 E7BA0050 */  swc1       $f26, 0x50($sp)
    /* D1FFC 150A4B4C E7BB0054 */  swc1       $f27, 0x54($sp)
    /* D2000 150A4B50 E7BC0058 */  swc1       $f28, 0x58($sp)
    /* D2004 150A4B54 E7BD005C */  swc1       $f29, 0x5C($sp)
    /* D2008 150A4B58 E7BE0060 */  swc1       $f30, 0x60($sp)
    /* D200C 150A4B5C E7BF0064 */  swc1       $f31, 0x64($sp)
    /* D2010 150A4B60 AFBF0068 */  sw         $ra, 0x68($sp)
    /* D2014 150A4B64 00808025 */  or         $s0, $a0, $zero
    /* D2018 150A4B68 8E170000 */  lw         $s7, 0x0($s0)
    /* D201C 150A4B6C 12E000FB */  beqz       $s7, func_150A4F5C
    /* D2020 150A4B70 8E1701D4 */   lw        $s7, 0x1D4($s0)
    /* D2024 150A4B74 12E000F9 */  beqz       $s7, func_150A4F5C
    /* D2028 150A4B78 8E1700F8 */   lw        $s7, 0xF8($s0)
    /* D202C 150A4B7C 32F74000 */  andi       $s7, $s7, 0x4000
    /* D2030 150A4B80 12E000F6 */  beqz       $s7, func_150A4F5C
    /* D2034 150A4B84 3C12800C */   lui       $s2, %hi(D_800C5C08)
    /* D2038 150A4B88 26525C08 */  addiu      $s2, $s2, %lo(D_800C5C08)
    /* D203C 150A4B8C 92110004 */  lbu        $s1, 0x4($s0)
    /* D2040 150A4B90 0011F080 */  sll        $fp, $s1, 2
    /* D2044 150A4B94 025E9021 */  addu       $s2, $s2, $fp
    /* D2048 150A4B98 8E520000 */  lw         $s2, 0x0($s2)
    /* D204C 150A4B9C 124000EF */  beqz       $s2, func_150A4F5C
    /* D2050 150A4BA0 3C08800D */   lui       $t0, %hi(D_800CC2D0)
    /* D2054 150A4BA4 2508C2D0 */  addiu      $t0, $t0, %lo(D_800CC2D0)
    /* D2058 150A4BA8 25094F4C */  addiu      $t1, $t0, 0x4F4C
    /* D205C 150A4BAC C60C0014 */  lwc1       $f12, 0x14($s0)
    /* D2060 150A4BB0 C60D0018 */  lwc1       $f13, 0x18($s0)
    /* D2064 150A4BB4 C60E001C */  lwc1       $f14, 0x1C($s0)
    /* D2068 150A4BB8 C6030270 */  lwc1       $f3, 0x270($s0)
    /* D206C 150A4BBC 460318C2 */  mul.s      $f3, $f3, $f3
  .L150A4BC0:
    /* D2070 150A4BC0 1208000D */  beq        $s0, $t0, .L150A4BF8
    /* D2074 150A4BC4 8D170000 */   lw        $s7, 0x0($t0)
    /* D2078 150A4BC8 12E0000B */  beqz       $s7, .L150A4BF8
    /* D207C 150A4BCC 00000000 */   nop
    /* D2080 150A4BD0 C5000014 */  lwc1       $f0, 0x14($t0)
    /* D2084 150A4BD4 C502001C */  lwc1       $f2, 0x1C($t0)
    /* D2088 150A4BD8 460C0001 */  sub.s      $f0, $f0, $f12
    /* D208C 150A4BDC 460E1081 */  sub.s      $f2, $f2, $f14
    /* D2090 150A4BE0 46000002 */  mul.s      $f0, $f0, $f0
    /* D2094 150A4BE4 00000000 */  nop
    /* D2098 150A4BE8 46021082 */  mul.s      $f2, $f2, $f2
    /* D209C 150A4BEC 46020000 */  add.s      $f0, $f0, $f2
    /* D20A0 150A4BF0 46030036 */  c.ole.s    $f0, $f3
    /* D20A4 150A4BF4 45010004 */  bc1t       .L150A4C08
  .L150A4BF8:
    /* D20A8 150A4BF8 2508032C */   addiu     $t0, $t0, 0x32C
    /* D20AC 150A4BFC 1509FFF0 */  bne        $t0, $t1, .L150A4BC0
    /* D20B0 150A4C00 00000000 */   nop
    /* D20B4 150A4C04 094293D7 */  j          func_150A4F5C
  .L150A4C08:
    /* D20B8 150A4C08 3C13800C */   lui       $s3, (0x800C0000 >> 16)
    /* D20BC 150A4C0C 26735EF8 */  addiu      $s3, $s3, 0x5EF8
    /* D20C0 150A4C10 0011B840 */  sll        $s7, $s1, 1
    /* D20C4 150A4C14 02779821 */  addu       $s3, $s3, $s7
    /* D20C8 150A4C18 96730000 */  lhu        $s3, 0x0($s3)
    /* D20CC 150A4C1C 2673FFFF */  addiu      $s3, $s3, -0x1
    /* D20D0 150A4C20 3C1E800C */  lui        $fp, %hi(D_800C57A0)
    /* D20D4 150A4C24 27DE57A0 */  addiu      $fp, $fp, %lo(D_800C57A0)
    /* D20D8 150A4C28 03D7F021 */  addu       $fp, $fp, $s7
    /* D20DC 150A4C2C 97DE0000 */  lhu        $fp, 0x0($fp)
    /* D20E0 150A4C30 8E150264 */  lw         $s5, 0x264($s0)
    /* D20E4 150A4C34 001E2100 */  sll        $a0, $fp, 4
    /* D20E8 150A4C38 16A00007 */  bnez       $s5, .L150A4C58
    /* D20EC 150A4C3C 24050001 */   addiu     $a1, $zero, 0x1
    /* D20F0 150A4C40 24060001 */  addiu      $a2, $zero, 0x1
    /* D20F4 150A4C44 0C000F10 */  jal        allocate_memory
    /* D20F8 150A4C48 24070002 */   addiu     $a3, $zero, 0x2
    /* D20FC 150A4C4C 104000C3 */  beqz       $v0, func_150A4F5C
    /* D2100 150A4C50 0040A825 */   or        $s5, $v0, $zero
    /* D2104 150A4C54 AE020264 */  sw         $v0, 0x264($s0)
  .L150A4C58:
    /* D2108 150A4C58 4495F800 */  mtc1       $s5, $f31
    /* D210C 150A4C5C 3C1E800C */  lui        $fp, %hi(D_800C5918)
    /* D2110 150A4C60 27DE5918 */  addiu      $fp, $fp, %lo(D_800C5918)
    /* D2114 150A4C64 03D7F021 */  addu       $fp, $fp, $s7
    /* D2118 150A4C68 97DE0000 */  lhu        $fp, 0x0($fp)
    /* D211C 150A4C6C 8E160268 */  lw         $s6, 0x268($s0)
    /* D2120 150A4C70 001E20C0 */  sll        $a0, $fp, 3
    /* D2124 150A4C74 16C00007 */  bnez       $s6, .L150A4C94
    /* D2128 150A4C78 24050001 */   addiu     $a1, $zero, 0x1
    /* D212C 150A4C7C 24060001 */  addiu      $a2, $zero, 0x1
    /* D2130 150A4C80 0C000F10 */  jal        allocate_memory
    /* D2134 150A4C84 24070002 */   addiu     $a3, $zero, 0x2
    /* D2138 150A4C88 104000B4 */  beqz       $v0, func_150A4F5C
    /* D213C 150A4C8C 0040B025 */   or        $s6, $v0, $zero
    /* D2140 150A4C90 AE020268 */  sw         $v0, 0x268($s0)
  .L150A4C94:
    /* D2144 150A4C94 8E07026C */  lw         $a3, 0x26C($s0)
    /* D2148 150A4C98 001E2080 */  sll        $a0, $fp, 2
    /* D214C 150A4C9C 14E00007 */  bnez       $a3, .L150A4CBC
    /* D2150 150A4CA0 24050001 */   addiu     $a1, $zero, 0x1
    /* D2154 150A4CA4 24060001 */  addiu      $a2, $zero, 0x1
    /* D2158 150A4CA8 0C000F10 */  jal        allocate_memory
    /* D215C 150A4CAC 24070002 */   addiu     $a3, $zero, 0x2
    /* D2160 150A4CB0 104000AA */  beqz       $v0, func_150A4F5C
    /* D2164 150A4CB4 00403825 */   or        $a3, $v0, $zero
    /* D2168 150A4CB8 AE02026C */  sw         $v0, 0x26C($s0)
  .L150A4CBC:
    /* D216C 150A4CBC 8E4C0000 */  lw         $t4, 0x0($s2)
    /* D2170 150A4CC0 8E540004 */  lw         $s4, 0x4($s2)
    /* D2174 150A4CC4 8E4B0008 */  lw         $t3, 0x8($s2)
    /* D2178 150A4CC8 8E1701D4 */  lw         $s7, 0x1D4($s0)
    /* D217C 150A4CCC 000B5980 */  sll        $t3, $t3, 6
    /* D2180 150A4CD0 01775821 */  addu       $t3, $t3, $s7
    /* D2184 150A4CD4 2652000C */  addiu      $s2, $s2, 0xC
    /* D2188 150A4CD8 12800035 */  beqz       $s4, .L150A4DB0
    /* D218C 150A4CDC 2694FFFF */   addiu     $s4, $s4, -0x1
    /* D2190 150A4CE0 C5600000 */  lwc1       $f0, 0x0($t3)
    /* D2194 150A4CE4 C5610004 */  lwc1       $f1, 0x4($t3)
    /* D2198 150A4CE8 C5620008 */  lwc1       $f2, 0x8($t3)
    /* D219C 150A4CEC C5630010 */  lwc1       $f3, 0x10($t3)
    /* D21A0 150A4CF0 C5640014 */  lwc1       $f4, 0x14($t3)
    /* D21A4 150A4CF4 C5650018 */  lwc1       $f5, 0x18($t3)
    /* D21A8 150A4CF8 C5660020 */  lwc1       $f6, 0x20($t3)
    /* D21AC 150A4CFC C5670024 */  lwc1       $f7, 0x24($t3)
    /* D21B0 150A4D00 C5680028 */  lwc1       $f8, 0x28($t3)
    /* D21B4 150A4D04 C5690030 */  lwc1       $f9, 0x30($t3)
    /* D21B8 150A4D08 C56A0034 */  lwc1       $f10, 0x34($t3)
    /* D21BC 150A4D0C C56B0038 */  lwc1       $f11, 0x38($t3)
  .L150A4D10:
    /* D21C0 150A4D10 85880000 */  lh         $t0, 0x0($t4)
    /* D21C4 150A4D14 85890002 */  lh         $t1, 0x2($t4)
    /* D21C8 150A4D18 44886000 */  mtc1       $t0, $f12
    /* D21CC 150A4D1C 44896800 */  mtc1       $t1, $f13
    /* D21D0 150A4D20 46806320 */  cvt.s.w    $f12, $f12
    /* D21D4 150A4D24 46806B60 */  cvt.s.w    $f13, $f13
    /* D21D8 150A4D28 858A0004 */  lh         $t2, 0x4($t4)
    /* D21DC 150A4D2C 460C03C2 */  mul.s      $f15, $f0, $f12
    /* D21E0 150A4D30 448A7000 */  mtc1       $t2, $f14
    /* D21E4 150A4D34 460D1C02 */  mul.s      $f16, $f3, $f13
    /* D21E8 150A4D38 468073A0 */  cvt.s.w    $f14, $f14
    /* D21EC 150A4D3C 46107BC0 */  add.s      $f15, $f15, $f16
    /* D21F0 150A4D40 460E3502 */  mul.s      $f20, $f6, $f14
    /* D21F4 150A4D44 4609A500 */  add.s      $f20, $f20, $f9
    /* D21F8 150A4D48 460C0D42 */  mul.s      $f21, $f1, $f12
    /* D21FC 150A4D4C 46147C40 */  add.s      $f17, $f15, $f20
    /* D2200 150A4D50 460D2582 */  mul.s      $f22, $f4, $f13
    /* D2204 150A4D54 46008C64 */  cvt.w.s    $f17, $f17
    /* D2208 150A4D58 460E3DC2 */  mul.s      $f23, $f7, $f14
    /* D220C 150A4D5C 4616AD40 */  add.s      $f21, $f21, $f22
    /* D2210 150A4D60 460C13C2 */  mul.s      $f15, $f2, $f12
    /* D2214 150A4D64 460ABDC0 */  add.s      $f23, $f23, $f10
    /* D2218 150A4D68 460D2C02 */  mul.s      $f16, $f5, $f13
    /* D221C 150A4D6C 4617AC80 */  add.s      $f18, $f21, $f23
    /* D2220 150A4D70 460E4502 */  mul.s      $f20, $f8, $f14
    /* D2224 150A4D74 46107BC0 */  add.s      $f15, $f15, $f16
    /* D2228 150A4D78 460BA500 */  add.s      $f20, $f20, $f11
    /* D222C 150A4D7C 460094A4 */  cvt.w.s    $f18, $f18
    /* D2230 150A4D80 46147CC0 */  add.s      $f19, $f15, $f20
    /* D2234 150A4D84 44088800 */  mfc1       $t0, $f17
    /* D2238 150A4D88 46009CE4 */  cvt.w.s    $f19, $f19
    /* D223C 150A4D8C A6A80000 */  sh         $t0, 0x0($s5)
    /* D2240 150A4D90 44099000 */  mfc1       $t1, $f18
    /* D2244 150A4D94 440A9800 */  mfc1       $t2, $f19
    /* D2248 150A4D98 A6A90002 */  sh         $t1, 0x2($s5)
    /* D224C 150A4D9C 258C0010 */  addiu      $t4, $t4, 0x10
    /* D2250 150A4DA0 A6AA0004 */  sh         $t2, 0x4($s5)
    /* D2254 150A4DA4 26B50010 */  addiu      $s5, $s5, 0x10
    /* D2258 150A4DA8 1680FFD9 */  bnez       $s4, .L150A4D10
    /* D225C 150A4DAC 2694FFFF */   addiu     $s4, $s4, -0x1
  .L150A4DB0:
    /* D2260 150A4DB0 1660FFC2 */  bnez       $s3, .L150A4CBC
    /* D2264 150A4DB4 2673FFFF */   addiu     $s3, $s3, -0x1
    /* D2268 150A4DB8 3C19800C */  lui        $t9, %hi(D_800C6070)
    /* D226C 150A4DBC 27396070 */  addiu      $t9, $t9, %lo(D_800C6070)
    /* D2270 150A4DC0 0011B880 */  sll        $s7, $s1, 2
    /* D2274 150A4DC4 0337C821 */  addu       $t9, $t9, $s7
    /* D2278 150A4DC8 8F390000 */  lw         $t9, 0x0($t9)
    /* D227C 150A4DCC 3C03800C */  lui        $v1, %hi(D_800C5918)
    /* D2280 150A4DD0 24635918 */  addiu      $v1, $v1, %lo(D_800C5918)
    /* D2284 150A4DD4 0011B840 */  sll        $s7, $s1, 1
    /* D2288 150A4DD8 00771821 */  addu       $v1, $v1, $s7
    /* D228C 150A4DDC 94630000 */  lhu        $v1, 0x0($v1)
    /* D2290 150A4DE0 0003B8C0 */  sll        $s7, $v1, 3
    /* D2294 150A4DE4 00031880 */  sll        $v1, $v1, 2
    /* D2298 150A4DE8 00771821 */  addu       $v1, $v1, $s7
    /* D229C 150A4DEC 00791821 */  addu       $v1, $v1, $t9
    /* D22A0 150A4DF0 4415F800 */  mfc1       $s5, $f31
  .L150A4DF4:
    /* D22A4 150A4DF4 8F2C0000 */  lw         $t4, 0x0($t9)
    /* D22A8 150A4DF8 8F310004 */  lw         $s1, 0x4($t9)
    /* D22AC 150A4DFC 8F320008 */  lw         $s2, 0x8($t9)
    /* D22B0 150A4E00 01956021 */  addu       $t4, $t4, $s5
    /* D22B4 150A4E04 858D0000 */  lh         $t5, 0x0($t4)
    /* D22B8 150A4E08 85850002 */  lh         $a1, 0x2($t4)
    /* D22BC 150A4E0C 858F0004 */  lh         $t7, 0x4($t4)
    /* D22C0 150A4E10 01A07025 */  or         $t6, $t5, $zero
    /* D22C4 150A4E14 00A03025 */  or         $a2, $a1, $zero
    /* D22C8 150A4E18 01E0C025 */  or         $t8, $t7, $zero
    /* D22CC 150A4E1C 02358821 */  addu       $s1, $s1, $s5
    /* D22D0 150A4E20 86280000 */  lh         $t0, 0x0($s1)
    /* D22D4 150A4E24 86290002 */  lh         $t1, 0x2($s1)
    /* D22D8 150A4E28 862A0004 */  lh         $t2, 0x4($s1)
    /* D22DC 150A4E2C 010D082A */  slt        $at, $t0, $t5
    /* D22E0 150A4E30 54200004 */  bnel       $at, $zero, .L150A4E44
    /* D22E4 150A4E34 01006825 */   or        $t5, $t0, $zero
    /* D22E8 150A4E38 01C8082A */  slt        $at, $t6, $t0
    /* D22EC 150A4E3C 54200001 */  bnel       $at, $zero, .L150A4E44
    /* D22F0 150A4E40 01007025 */   or        $t6, $t0, $zero
  .L150A4E44:
    /* D22F4 150A4E44 0125082A */  slt        $at, $t1, $a1
    /* D22F8 150A4E48 54200004 */  bnel       $at, $zero, .L150A4E5C
    /* D22FC 150A4E4C 01202825 */   or        $a1, $t1, $zero
    /* D2300 150A4E50 00C9082A */  slt        $at, $a2, $t1
    /* D2304 150A4E54 54200001 */  bnel       $at, $zero, .L150A4E5C
    /* D2308 150A4E58 01203025 */   or        $a2, $t1, $zero
  .L150A4E5C:
    /* D230C 150A4E5C 014F082A */  slt        $at, $t2, $t7
    /* D2310 150A4E60 54200004 */  bnel       $at, $zero, .L150A4E74
    /* D2314 150A4E64 01407825 */   or        $t7, $t2, $zero
    /* D2318 150A4E68 030A082A */  slt        $at, $t8, $t2
    /* D231C 150A4E6C 54200001 */  bnel       $at, $zero, .L150A4E74
    /* D2320 150A4E70 0140C025 */   or        $t8, $t2, $zero
  .L150A4E74:
    /* D2324 150A4E74 02559021 */  addu       $s2, $s2, $s5
    /* D2328 150A4E78 86480000 */  lh         $t0, 0x0($s2)
    /* D232C 150A4E7C 86490002 */  lh         $t1, 0x2($s2)
    /* D2330 150A4E80 864A0004 */  lh         $t2, 0x4($s2)
    /* D2334 150A4E84 010D082A */  slt        $at, $t0, $t5
    /* D2338 150A4E88 54200004 */  bnel       $at, $zero, .L150A4E9C
    /* D233C 150A4E8C 01006825 */   or        $t5, $t0, $zero
    /* D2340 150A4E90 01C8082A */  slt        $at, $t6, $t0
    /* D2344 150A4E94 54200001 */  bnel       $at, $zero, .L150A4E9C
    /* D2348 150A4E98 01007025 */   or        $t6, $t0, $zero
  .L150A4E9C:
    /* D234C 150A4E9C A6CD0000 */  sh         $t5, 0x0($s6)
    /* D2350 150A4EA0 014F082A */  slt        $at, $t2, $t7
    /* D2354 150A4EA4 54200004 */  bnel       $at, $zero, .L150A4EB8
    /* D2358 150A4EA8 01407825 */   or        $t7, $t2, $zero
    /* D235C 150A4EAC 030A082A */  slt        $at, $t8, $t2
    /* D2360 150A4EB0 54200001 */  bnel       $at, $zero, .L150A4EB8
    /* D2364 150A4EB4 0140C025 */   or        $t8, $t2, $zero
  .L150A4EB8:
    /* D2368 150A4EB8 A6CE0004 */  sh         $t6, 0x4($s6)
    /* D236C 150A4EBC 0125082A */  slt        $at, $t1, $a1
    /* D2370 150A4EC0 54200004 */  bnel       $at, $zero, .L150A4ED4
    /* D2374 150A4EC4 01202825 */   or        $a1, $t1, $zero
    /* D2378 150A4EC8 00C9082A */  slt        $at, $a2, $t1
    /* D237C 150A4ECC 54200001 */  bnel       $at, $zero, .L150A4ED4
    /* D2380 150A4ED0 01203025 */   or        $a2, $t1, $zero
  .L150A4ED4:
    /* D2384 150A4ED4 A6CF0002 */  sh         $t7, 0x2($s6)
    /* D2388 150A4ED8 A6D80006 */  sh         $t8, 0x6($s6)
    /* D238C 150A4EDC 2739000C */  addiu      $t9, $t9, 0xC
    /* D2390 150A4EE0 A4E50000 */  sh         $a1, 0x0($a3)
    /* D2394 150A4EE4 A4E60002 */  sh         $a2, 0x2($a3)
    /* D2398 150A4EE8 24E70004 */  addiu      $a3, $a3, 0x4
    /* D239C 150A4EEC 1723FFC1 */  bne        $t9, $v1, .L150A4DF4
    /* D23A0 150A4EF0 26D60008 */   addiu     $s6, $s6, 0x8
endlabel func_150A4B04
