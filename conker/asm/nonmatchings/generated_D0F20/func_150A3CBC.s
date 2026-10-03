  glabel func_150A3CBC
    /* D116C 150A3CBC 00B2082A */  slt        $at, $a1, $s2
    /* D1170 150A3CC0 142000A3 */  bnez       $at, .L150A3F50
    /* D1174 150A3CC4 00000000 */   nop
    /* D1178 150A3CC8 03D5082A */  slt        $at, $fp, $s5
    /* D117C 150A3CCC 1020000A */  beqz       $at, .L150A3CF8
    /* D1180 150A3CD0 00000000 */   nop
    /* D1184 150A3CD4 02606825 */  or         $t5, $s3, $zero
    /* D1188 150A3CD8 02A07025 */  or         $t6, $s5, $zero
    /* D118C 150A3CDC 02807825 */  or         $t7, $s4, $zero
    /* D1190 150A3CE0 02C09825 */  or         $s3, $s6, $zero
    /* D1194 150A3CE4 03C0A825 */  or         $s5, $fp, $zero
    /* D1198 150A3CE8 02E0A025 */  or         $s4, $s7, $zero
    /* D119C 150A3CEC 01A0B025 */  or         $s6, $t5, $zero
    /* D11A0 150A3CF0 01C0F025 */  or         $fp, $t6, $zero
    /* D11A4 150A3CF4 01E0B825 */  or         $s7, $t7, $zero
  .L150A3CF8:
    /* D11A8 150A3CF8 03C5082A */  slt        $at, $fp, $a1
    /* D11AC 150A3CFC 14200094 */  bnez       $at, .L150A3F50
    /* D11B0 150A3D00 00000000 */   nop
    /* D11B4 150A3D04 03D27022 */  sub        $t6, $fp, $s2 /* handwritten instruction */
    /* D11B8 150A3D08 25CE0001 */  addiu      $t6, $t6, 0x1
    /* D11BC 150A3D0C 02D07822 */  sub        $t7, $s6, $s0 /* handwritten instruction */
    /* D11C0 150A3D10 000F7A00 */  sll        $t7, $t7, 8
    /* D11C4 150A3D14 01EE001A */  div        $zero, $t7, $t6
    /* D11C8 150A3D18 00B26822 */  sub        $t5, $a1, $s2 /* handwritten instruction */
    /* D11CC 150A3D1C 448D5000 */  mtc1       $t5, $f10
    /* D11D0 150A3D20 00000000 */  nop
    /* D11D4 150A3D24 448E5800 */  mtc1       $t6, $f11
    /* D11D8 150A3D28 00000000 */  nop
    /* D11DC 150A3D2C 00007812 */  mflo       $t7
    /* D11E0 150A3D30 00000000 */  nop
    /* D11E4 150A3D34 00000000 */  nop
    /* D11E8 150A3D38 01AF0018 */  mult       $t5, $t7
    /* D11EC 150A3D3C 00006812 */  mflo       $t5
    /* D11F0 150A3D40 00000000 */  nop
    /* D11F4 150A3D44 00000000 */  nop
    /* D11F8 150A3D48 000D6A03 */  sra        $t5, $t5, 8
    /* D11FC 150A3D4C 03D57022 */  sub        $t6, $fp, $s5 /* handwritten instruction */
    /* D1200 150A3D50 01B0F021 */  addu       $fp, $t5, $s0
    /* D1204 150A3D54 00B56822 */  sub        $t5, $a1, $s5 /* handwritten instruction */
    /* D1208 150A3D58 448D7000 */  mtc1       $t5, $f14
    /* D120C 150A3D5C 00000000 */  nop
    /* D1210 150A3D60 05A10005 */  bgez       $t5, .L150A3D78
    /* D1214 150A3D64 00000000 */   nop
    /* D1218 150A3D68 02B27022 */  sub        $t6, $s5, $s2 /* handwritten instruction */
    /* D121C 150A3D6C 00B26822 */  sub        $t5, $a1, $s2 /* handwritten instruction */
    /* D1220 150A3D70 0260B025 */  or         $s6, $s3, $zero
    /* D1224 150A3D74 02009825 */  or         $s3, $s0, $zero
  .L150A3D78:
    /* D1228 150A3D78 25CE0001 */  addiu      $t6, $t6, 0x1
    /* D122C 150A3D7C 02D37822 */  sub        $t7, $s6, $s3 /* handwritten instruction */
    /* D1230 150A3D80 000F7A00 */  sll        $t7, $t7, 8
    /* D1234 150A3D84 01EE001A */  div        $zero, $t7, $t6
    /* D1238 150A3D88 448D6000 */  mtc1       $t5, $f12
    /* D123C 150A3D8C 00000000 */  nop
    /* D1240 150A3D90 448E6800 */  mtc1       $t6, $f13
    /* D1244 150A3D94 00000000 */  nop
    /* D1248 150A3D98 00007812 */  mflo       $t7
    /* D124C 150A3D9C 00000000 */  nop
    /* D1250 150A3DA0 00000000 */  nop
    /* D1254 150A3DA4 01AF0018 */  mult       $t5, $t7
    /* D1258 150A3DA8 00006812 */  mflo       $t5
    /* D125C 150A3DAC 00000000 */  nop
    /* D1260 150A3DB0 00000000 */  nop
    /* D1264 150A3DB4 000D6A03 */  sra        $t5, $t5, 8
    /* D1268 150A3DB8 01B3B021 */  addu       $s6, $t5, $s3
    /* D126C 150A3DBC 02C47022 */  sub        $t6, $s6, $a0 /* handwritten instruction */
    /* D1270 150A3DC0 03C47822 */  sub        $t7, $fp, $a0 /* handwritten instruction */
    /* D1274 150A3DC4 01CF082A */  slt        $at, $t6, $t7
    /* D1278 150A3DC8 240DFFFF */  addiu      $t5, $zero, -0x1
    /* D127C 150A3DCC 54200001 */  bnel       $at, $zero, .L150A3DD4
    /* D1280 150A3DD0 240D0001 */   addiu     $t5, $zero, 0x1
  .L150A3DD4:
    /* D1284 150A3DD4 01CD7023 */  subu       $t6, $t6, $t5
    /* D1288 150A3DD8 01ED7821 */  addu       $t7, $t7, $t5
    /* D128C 150A3DDC 01EE6826 */  xor        $t5, $t7, $t6
    /* D1290 150A3DE0 05A1005B */  bgez       $t5, .L150A3F50
    /* D1294 150A3DE4 00000000 */   nop
    /* D1298 150A3DE8 AD590004 */  sw         $t9, 0x4($t2)
    /* D129C 150A3DEC 0220C825 */  or         $t9, $s1, $zero
    /* D12A0 150A3DF0 0334082A */  slt        $at, $t9, $s4
    /* D12A4 150A3DF4 10200002 */  beqz       $at, .L150A3E00
    /* D12A8 150A3DF8 00000000 */   nop
    /* D12AC 150A3DFC 0280C825 */  or         $t9, $s4, $zero
  .L150A3E00:
    /* D12B0 150A3E00 0337082A */  slt        $at, $t9, $s7
    /* D12B4 150A3E04 10200002 */  beqz       $at, .L150A3E10
    /* D12B8 150A3E08 00000000 */   nop
    /* D12BC 150A3E0C 02E0C825 */  or         $t9, $s7, $zero
  .L150A3E10:
    /* D12C0 150A3E10 0019CA00 */  sll        $t9, $t9, 8
    /* D12C4 150A3E14 02F17822 */  sub        $t7, $s7, $s1 /* handwritten instruction */
    /* D12C8 150A3E18 440E5800 */  mfc1       $t6, $f11
    /* D12CC 150A3E1C 00000000 */  nop
    /* D12D0 150A3E20 000F7A00 */  sll        $t7, $t7, 8
    /* D12D4 150A3E24 01EE001A */  div        $zero, $t7, $t6
    /* D12D8 150A3E28 440D5000 */  mfc1       $t5, $f10
    /* D12DC 150A3E2C 00000000 */  nop
    /* D12E0 150A3E30 02209825 */  or         $s3, $s1, $zero
    /* D12E4 150A3E34 0293082A */  slt        $at, $s4, $s3
    /* D12E8 150A3E38 10200002 */  beqz       $at, .L150A3E44
    /* D12EC 150A3E3C 00000000 */   nop
    /* D12F0 150A3E40 02809825 */  or         $s3, $s4, $zero
  .L150A3E44:
    /* D12F4 150A3E44 00007812 */  mflo       $t7
    /* D12F8 150A3E48 00000000 */  nop
    /* D12FC 150A3E4C 00000000 */  nop
    /* D1300 150A3E50 01AF0018 */  mult       $t5, $t7
    /* D1304 150A3E54 02607825 */  or         $t7, $s3, $zero
    /* D1308 150A3E58 02EF082A */  slt        $at, $s7, $t7
    /* D130C 150A3E5C 10200002 */  beqz       $at, .L150A3E68
    /* D1310 150A3E60 00000000 */   nop
    /* D1314 150A3E64 02E07825 */  or         $t7, $s7, $zero
  .L150A3E68:
    /* D1318 150A3E68 00006812 */  mflo       $t5
    /* D131C 150A3E6C 00000000 */  nop
    /* D1320 150A3E70 00000000 */  nop
    /* D1324 150A3E74 00119A00 */  sll        $s3, $s1, 8
    /* D1328 150A3E78 026D9821 */  addu       $s3, $s3, $t5
    /* D132C 150A3E7C 440E7000 */  mfc1       $t6, $f14
    /* D1330 150A3E80 00000000 */  nop
    /* D1334 150A3E84 05C10003 */  bgez       $t6, .L150A3E94
    /* D1338 150A3E88 00000000 */   nop
    /* D133C 150A3E8C 0280B825 */  or         $s7, $s4, $zero
    /* D1340 150A3E90 0220A025 */  or         $s4, $s1, $zero
  .L150A3E94:
    /* D1344 150A3E94 000F8A00 */  sll        $s1, $t7, 8
    /* D1348 150A3E98 02F47822 */  sub        $t7, $s7, $s4 /* handwritten instruction */
    /* D134C 150A3E9C 440E6800 */  mfc1       $t6, $f13
    /* D1350 150A3EA0 00000000 */  nop
    /* D1354 150A3EA4 000F7A00 */  sll        $t7, $t7, 8
    /* D1358 150A3EA8 01EE001A */  div        $zero, $t7, $t6
    /* D135C 150A3EAC 440D6000 */  mfc1       $t5, $f12
    /* D1360 150A3EB0 00000000 */  nop
    /* D1364 150A3EB4 00007812 */  mflo       $t7
    /* D1368 150A3EB8 00000000 */  nop
    /* D136C 150A3EBC 00000000 */  nop
    /* D1370 150A3EC0 01AF0018 */  mult       $t5, $t7
    /* D1374 150A3EC4 00006812 */  mflo       $t5
    /* D1378 150A3EC8 00000000 */  nop
    /* D137C 150A3ECC 00000000 */  nop
    /* D1380 150A3ED0 0014A200 */  sll        $s4, $s4, 8
    /* D1384 150A3ED4 01B4A821 */  addu       $s5, $t5, $s4
    /* D1388 150A3ED8 03D6F022 */  sub        $fp, $fp, $s6 /* handwritten instruction */
    /* D138C 150A3EDC 02759822 */  sub        $s3, $s3, $s5 /* handwritten instruction */
    /* D1390 150A3EE0 00139A00 */  sll        $s3, $s3, 8
    /* D1394 150A3EE4 027E001A */  div        $zero, $s3, $fp
    /* D1398 150A3EE8 00968022 */  sub        $s0, $a0, $s6 /* handwritten instruction */
    /* D139C 150A3EEC 0000F012 */  mflo       $fp
    /* D13A0 150A3EF0 00000000 */  nop
    /* D13A4 150A3EF4 00000000 */  nop
    /* D13A8 150A3EF8 021E0018 */  mult       $s0, $fp
    /* D13AC 150A3EFC 00008012 */  mflo       $s0
    /* D13B0 150A3F00 00000000 */  nop
    /* D13B4 150A3F04 00000000 */  nop
    /* D13B8 150A3F08 00108203 */  sra        $s0, $s0, 8
    /* D13BC 150A3F0C 02B0A821 */  addu       $s5, $s5, $s0
    /* D13C0 150A3F10 0335082A */  slt        $at, $t9, $s5
    /* D13C4 150A3F14 10200002 */  beqz       $at, .L150A3F20
    /* D13C8 150A3F18 00000000 */   nop
    /* D13CC 150A3F1C 0320A825 */  or         $s5, $t9, $zero
  .L150A3F20:
    /* D13D0 150A3F20 02B1082A */  slt        $at, $s5, $s1
    /* D13D4 150A3F24 10200002 */  beqz       $at, .L150A3F30
    /* D13D8 150A3F28 00000000 */   nop
    /* D13DC 150A3F2C 0220A825 */  or         $s5, $s1, $zero
  .L150A3F30:
    /* D13E0 150A3F30 AD550000 */  sw         $s5, 0x0($t2)
    /* D13E4 150A3F34 AD480008 */  sw         $t0, 0x8($t2)
    /* D13E8 150A3F38 AD5C000C */  sw         $gp, 0xC($t2)
    /* D13EC 150A3F3C 24010027 */  addiu      $at, $zero, 0x27
    /* D13F0 150A3F40 10410003 */  beq        $v0, $at, .L150A3F50
    /* D13F4 150A3F44 00000000 */   nop
    /* D13F8 150A3F48 24420001 */  addiu      $v0, $v0, 0x1
    /* D13FC 150A3F4C 254A0010 */  addiu      $t2, $t2, 0x10
  .L150A3F50:
    /* D1400 150A3F50 27180001 */  addiu      $t8, $t8, 0x1
    /* D1404 150A3F54 03E00008 */  jr         $ra
    /* D1408 150A3F58 00000000 */   nop
endlabel func_150A3CBC
