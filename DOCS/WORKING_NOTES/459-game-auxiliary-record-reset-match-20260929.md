# Game auxiliary-record reset byte match

Date: 2026-09-29

## Scope

This pass completed `func_1511A7C0` in
`conker/src/game/generated_142560.c`. Its tracked retail slot spans 30 words
and 120 bytes at `0x1511A7C0..0x1511A838`.

## Recovered behavior

The routine reads the auxiliary record at owner offset `0x80`. It enables the
record through byte `0x1E`, zeroes float `0x10` and state byte `0x1C`, sets
state byte `0x1D` to seven, and initializes floats `0x14` and `0x18` to
`260.0f` and `100.0f`.

It then reads the owner's unsigned halfword count at offset `0x16`. For each
entry, it reloads the float-array base from auxiliary-record offset `0x4` and
stores zero at the current four-byte offset. Separate element-count and byte
offset locals preserve retail's post-incremented loop shape and place the
next array-base load in the branch-likely delay slot.

The corrected return type is `void`. The complete leaf routine emits directly
from semantic C; no expected-word guards or assembly fallback are required.

## Verification

- The focused compact object matches all 30 retail words, including the
  branch-likely loop and its delay slot.
- `wsl make -C conker NON_MATCHING=1 -j1` rebuilt and linked the complete ELF
  and binary successfully.
- The linked ELF and pristine retail 120-byte spans share SHA-256
  `5f44289b94c6d621b6172d793da5c279b95a7c0d83d380882901d219512b3654`.
- Fresh matcher totals are `2,961 / 5,465 (54.18%)` overall and
  `2,387 / 4,789 (49.84%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked Game queue with 29-word `func_1514DAA4`, at 28
real differences. Keep `func_15194320` and `func_15194394` parked behind
generated-slice jump-table and rodata ownership, `func_151F3D78` parked behind
audio-object layout drift, the tied Init SDK cache routines in their ownership
lane, and `func_10012588` parked on address drift.
