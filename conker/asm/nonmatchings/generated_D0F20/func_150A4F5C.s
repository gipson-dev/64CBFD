  glabel func_150A4F5C
    /* D240C 150A4F5C 8E170264 */  lw         $s7, 0x264($s0)
    /* D2410 150A4F60 12E00003 */  beqz       $s7, .L150A4F70
    /* D2414 150A4F64 AE000264 */   sw        $zero, 0x264($s0)
    /* D2418 150A4F68 0C00101D */  jal        func_10004074
    /* D241C 150A4F6C 02E02025 */   or        $a0, $s7, $zero
  .L150A4F70:
    /* D2420 150A4F70 8E170268 */  lw         $s7, 0x268($s0)
    /* D2424 150A4F74 12E00003 */  beqz       $s7, .L150A4F84
    /* D2428 150A4F78 AE000268 */   sw        $zero, 0x268($s0)
    /* D242C 150A4F7C 0C00101D */  jal        func_10004074
    /* D2430 150A4F80 02E02025 */   or        $a0, $s7, $zero
  .L150A4F84:
    /* D2434 150A4F84 8E17026C */  lw         $s7, 0x26C($s0)
    /* D2438 150A4F88 12E00003 */  beqz       $s7, .L150A4F98
    /* D243C 150A4F8C AE00026C */   sw        $zero, 0x26C($s0)
    /* D2440 150A4F90 0C00101D */  jal        func_10004074
    /* D2444 150A4F94 02E02025 */   or        $a0, $s7, $zero
  .L150A4F98:
    /* D2448 150A4F98 094293BD */  j          func_150A4EF4
    /* D244C 150A4F9C 00000000 */   nop

endlabel func_150A4F5C
