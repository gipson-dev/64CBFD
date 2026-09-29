# Game selector-transition dispatch byte match

Date: 2026-09-29

## Scope

This pass completed `func_151AE06C` in
`conker/src/game/generated_1D92F0.c`. The retail slot spans 30 words and 120
bytes at `0x151AE06C..0x151AE0E4`.

## Recovered behavior

The routine first asks `func_151ACB38` to admit the operation, passing a
one-byte stack output. If admitted, it reads the requested selector from the
second argument at offset `0x1B` and the current selector from offset `0x98`
of the object referenced by owner field `0x31C`.

When the current selector is zero, the routine installs the requested selector
directly through `func_151AE0E4`. When the selector is already equal, it
returns without work. Otherwise it calls `func_151AE264` to remove the old
state and then installs the requested selector through `func_151AE0E4`.

Typed byte-selector declarations for both transition helpers reproduce
retail's byte spill at stack offset `0x1E` and reload across the first call.
Declaring the admission byte before the requested selector gives the retail
`0x20` frame and places the admission output at `0x1F`. Loading the requested
selector before the current selector reproduces retail's `t6`/`t7` allocation.
Twenty-nine words and all four `R_MIPS_26` relocations emit directly from C.
One expected-word guard changes only the commutative equality branch from
`beql v0,a1` to retail's `beql a1,v0`.

## Verification

- The focused `generated_1D92F0.c.o` build matches all 30 retail words and
  retains relocations for `func_151ACB38`, `func_151AE264`, and both calls to
  `func_151AE0E4`.
- The guard-table change triggered a complete serial rebuild; the full
  `wsl make -C conker NON_MATCHING=1 -j1` relink completed successfully.
- The linked ELF and retail 120-byte spans share SHA-256
  `540db7d8ff6e8ae46dac27e83c1fdf131ce6275da182665eb858b303353d595c`.
- Fresh matcher totals are `2,949 / 5,465 (53.96%)` overall and
  `2,375 / 4,789 (49.59%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 32-word `func_15174920`, currently at
27 real differences. Its retail body caps byte `0x3F` at 200, subtracts the
unsigned product of `D_800BE9E4` and owner word `0x18`, clears halfword `0x38`
if the result is negative, and otherwise updates halfwords `0x34` and `0x36`
from signed word `0x14` before storing the remaining byte. Keep 29-word
`func_15194320` and `func_15194394` parked behind generated-slice jump-table
and rodata ownership. Also keep `func_151F3D78` parked behind audio-object
layout drift, the tied Init SDK cache routines in their ownership lane, and
address-drift row `func_10012588` parked.
