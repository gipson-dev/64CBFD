# Game object-record cleanup byte match

Date: 2026-09-29

## Scope

This pass completed `func_1518E308` in
`conker/src/game/generated_1BA1D0.c`. Its tracked retail slot spans 29 words
and 116 bytes at `0x1518E308..0x1518E37C`.

## Recovered behavior

The former zero-return placeholder now clears the owner's word at offset
`0x28` and float at offset `0x24`. It then walks 100 records beginning at
offset `0x48`, each with a `0x18`-byte stride. A nonnull pointer in the first
word of a record is passed to `func_1516972C` for release.

After the release pass, the routine calls `bzero` on the retained array base
for `0x960` bytes, exactly covering all 100 records. The recovered function is
`void`, consistent with every caller and retail's lack of a synthesized return
value.

The direct bounded-loop C shape naturally reproduces retail's `0x38`-byte
frame, saved `s0` through `s2` lifetimes, branch-likely null path, pointer
stride in the loop delay slot, retained base spill, and final `bzero` call. No
expected-word guards are needed.

## Verification

- The focused generated object reproduces all 29 retail instructions directly
  from C.
- `wsl make -C conker NON_MATCHING=1 -j1` relinked the complete ELF and binary
  successfully.
- Direct linked-span comparison passes all 116 bytes. The linked and pristine
  retail spans share SHA-256
  `a062376721760a70f62df07a70915d1a422edc96387ff8ec416e4248dc20dcf6`.
- Fresh matcher totals are `2,965 / 5,465 (54.25%)` overall and
  `2,391 / 4,789 (49.93%)` in Game, with one address-drift row.

## Resume boundary

Resume ordinary Game matching with 29-word `func_151B8BE0`, at 28 real
differences. Keep the lower-difference compiler-scheduling cases and the
generated-slice jump-table/rodata cases at their documented parked boundaries.
Keep the tied Init SDK cache routines in their ownership lane and
`func_10012588` parked on address drift.
