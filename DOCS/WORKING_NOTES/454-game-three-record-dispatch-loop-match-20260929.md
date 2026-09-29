# Game three-record dispatch loop byte match

Date: 2026-09-29

## Scope

This pass completed `func_15096D08` in
`conker/src/game/generated_C3E20.c`. The tracked retail slot spans 28 words
and 112 bytes at `0x15096D08..0x15096D78`.

## Recovered behavior

The routine first reads the global mode byte `D_800C35EA`. Mode one skips the
update entirely. In every other mode, it scans the three records beginning at
`D_800D2DC0`, each separated by `0x24` bytes. Empty records, identified by a
zero first byte, are skipped. Every nonempty record invokes
`func_15096A68(index)`, and a nonzero result stops the scan immediately.

The retail routine does not return a value, so the false `s32` placeholder was
corrected to `void`. Giving `func_15096A68` its proven signed-index parameter
also records the call ABI used by this loop. A zero-based `while (i != 3)`
with an explicit entry pointer reproduces retail's `s0`, `s1`, and `s2`
lifetimes, the branch-likely empty-record increment, the successful-call exit,
and the `0x24` loop-delay update. No expected-word guards are required.

## Verification

- The focused `generated_C3E20.c.o` comparison matches all 28 retail words,
  both global `HI16`/`LO16` pairs, and the `R_MIPS_26` relocation for
  `func_15096A68`.
- `wsl make -C conker NON_MATCHING=1 -j1` rebuilt and relinked the ELF and
  binary successfully.
- The linked ELF and retail 112-byte spans share SHA-256
  `15e463f0914a3cd4f1ecc2d323f812dbe8bd443b83acd89e6e0859cccc283a0c`.
- Fresh matcher totals are `2,955 / 5,465 (54.07%)` overall and
  `2,381 / 4,789 (49.72%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked Game queue with 32-word `func_15084C30`,
currently at 28 real differences. It is a zero-return placeholder in
`conker/src/game/generated_AEB40.c`; recover its behavior from the retail
`AEB40` assembly slice before attempting compiler normalization. Keep
`func_15194320` and `func_15194394` parked behind generated-slice jump-table
and rodata ownership, `func_151F3D78` parked behind audio-object layout drift,
the tied Init SDK cache routines in their ownership lane, and
`func_10012588` parked on address drift.
