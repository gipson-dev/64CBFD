glabel func_150AD780
    /* DAC30 150AD780 3C01800A */  lui        $at, %hi(D_8009F710)
    /* DAC34 150AD784 C42AF710 */  lwc1       $f10, %lo(D_8009F710)($at)
    /* DAC38 150AD788 460A6300 */  add.s      $f12, $f12, $f10
endlabel func_150AD780
