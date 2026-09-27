glabel func_150A6538
    addiu      $sp, $sp, -0x20
    addiu      $t0, $zero, -0x2710
    addiu      $t1, $zero, 0x4E20
    sw         $ra, 0x20($sp)
    sw         $t0, 0x18($sp)
    sw         $t1, 0x1C($sp)
    jal        func_150A6568
     nop
    lw         $ra, 0x20($sp)
    addiu      $sp, $sp, 0x20
    jr         $ra
     nop
