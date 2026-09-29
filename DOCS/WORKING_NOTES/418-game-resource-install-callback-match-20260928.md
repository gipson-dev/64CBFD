# Game resource-install callback byte match

Date: 2026-09-28

## Scope

This pass completed `func_15166F6C` in
`conker/src/game/generated_193E50.c`. The retail slot spans 27 words and 108
bytes at `0x15166F6C..0x15166FD8`.

## Recovered behavior

The callback installs the resource at `D_8009054C` into global pointer
`D_800DD228`, then calls `func_15094F70`. The setup call receives the original
first callback argument, the installed resource pointer, `D_800DD220`, the
address of `D_800DD230`, three zero arguments, `D_800DD224`, and constant `3`.
The callback itself has four fixed incoming arguments and returns `void`.

The fixed callback signature reproduces retail's `0x30` frame and homes
incoming `a1`, `a2`, and `a3` at `sp+0x34`, `sp+0x38`, and `sp+0x3C`.
Forwarding `D_800DD228` after assigning it makes IDO retain the global's
address in `v0`, matching retail's opening load/store schedule and all later
argument registers. All 27 words emit directly from semantic C. No
expected-word guards or compiler-profile override are required.

## Verification

- The focused `generated_193E50.c.o` build passed under the existing
  `-O2 -g3` profile; all 27 words and eleven relocations match retail.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_15166F6C` as byte-exact.
- The linked ELF and retail 108-byte spans share SHA-256
  `1d8be5028b0b03a7fc525437b36e570682ceaee7ffb91eef469a9f4951f6ce44`.
- Fresh matcher totals are `2,920 / 5,466 (53.42%)` overall and
  `2,346 / 4,790 (48.98%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_15173C90`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
