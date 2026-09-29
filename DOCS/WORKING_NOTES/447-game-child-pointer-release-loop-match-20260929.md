# Game child-pointer release loop byte match

Date: 2026-09-29

## Scope

This pass completed `func_151BFB2C` in
`conker/src/game/generated_1E73B0.c`. The retail slot spans 30 words and 120
bytes at `0x151BFB2C..0x151BFBA4`.

## Recovered behavior

The routine releases a non-null primary pointer at owner offset `0x28`, then
walks two child pointers at offsets `0x2C` and `0x30` and releases each
non-null entry through `func_1516972C`.

Retail keeps the owner in `a1` across the optional first call, retains
`owner + 0x28` in `s1`, and uses `s0` as the indexed child counter. Expressing
the counter as `s32` with `(i = (u8)i)` in the post-tested condition reproduces
retail's increment, `andi`, comparison, and branch-delay feedback. Writing the
child address as `base + 4 + i * 4` preserves retail's commutative `addu`
operand order. All 30 words and both `R_MIPS_26` call relocations emit directly
from C; no expected-word guards are required.

## Verification

- The focused `generated_1E73B0.c.o` build matches all 30 retail words and
  retains both relocations for `func_1516972C`.
- The incremental `wsl make -C conker NON_MATCHING=1 -j1` relink refreshed
  the ELF and binary successfully.
- The linked ELF and retail 120-byte spans share SHA-256
  `acd08cbda50fab15b1c03fdebaaa7f19e11a51276b5b6acf3021d19296910c95`.
- Fresh matcher totals are `2,948 / 5,465 (53.94%)` overall and
  `2,374 / 4,789 (49.57%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 30-word `func_151AE06C`, currently at
27 real differences. Its retail body calls `func_151ACB38` with a one-byte
stack output, reads a requested selector from the second argument at offset
`0x1B`, compares it with the current selector at
`(*(arg0 + 0x31C)) + 0x98`, and conditionally dispatches `func_151AE264`
before `func_151AE0E4`. Keep 29-word `func_15194320` and `func_15194394`
parked behind generated-slice jump-table/rodata ownership. Also keep
`func_151F3D78` parked behind audio-object layout drift, the tied Init SDK
cache routines in their ownership lane, and address-drift row
`func_10012588` parked.
