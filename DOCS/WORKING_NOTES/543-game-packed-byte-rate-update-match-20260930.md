# Game packed-byte rate updater byte match

Date: 2026-09-30

`func_15077404` occupies 44 words and 176 bytes at
`0x15077404..0x150774B4`. When the update mode is active, it combines
`D_800D1891` and `D_800D1892` into a signed 16-bit rate, multiplies that rate
by `D_800BE9E4`, adds it to the packed value in object bytes `0x246` and
`0x249`, truncates the result to signed 16 bits, and clamps negative results
to zero. It writes the high five bits with flag `0x80` to byte `0x246` and the
low byte to `0x249`. In fallback mode it copies `D_800D1890` to byte `0x246`.

The prior source kept the sum in `s32`, so it missed retail's signed 16-bit
truncation before the negative test. The recovered C also exposes the packed
rate temporary, uses addition for the two rate bytes, and returns after the
active-path stores. IDO preserves the recovered behavior but chooses a closed
register-allocation and instruction-scheduling cycle. Thirty-three guarded
source words normalize that cycle, and the offset-`0x090` row inserts retail's
`jr $ra` so offset `0x094` can restore the empty delay slot.

The fresh matcher advances by exactly this one row and reports
`3,047 / 5,463 (55.78%)` overall and `2,468 / 4,789 (51.53%)` in Game with no
address drift. The linked ELF span has SHA-256
`85f549020a856aac2adf5142775d97f1ce8016b59dfb5ed4f796b58c50a802e9`, and
its disassembly matches all 44 words in the retail listing beginning at ROM
annotation `0xA48B4`. The cartridge Game payload is compressed, so a direct
hash of pristine `baserom.us.z64` at that annotation is not a valid
uncompressed-code comparison.

The replacement payload build, outer non-matching ROM build, project tool
checks, and all 10 tool unit tests pass.

Keep Game `func_15015F40`, `func_150A76F0`, `func_15106E78`, and
`func_150413FC`, plus Init `func_1000FF90`, parked at their documented
ownership or compiler boundaries. Resume with 34-word Game `func_1509CDDC`,
the next ordinary matcher row.
