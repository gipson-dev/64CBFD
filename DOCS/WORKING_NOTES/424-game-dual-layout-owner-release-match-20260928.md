# Game dual-layout owner release byte match

Date: 2026-09-28

## Scope

This pass completed `func_151CB49C` in
`conker/src/game/generated_1F4650.c`. The retail slot spans 29 words and 116
bytes at `0x151CB49C..0x151CB50C`.

## Recovered behavior

The routine receives an object, a pointer-bearing event context, and an event
byte. For event `0x21`, it compares the object word at offset `0x18` directly
with the first word of the context. For event zero, it follows the first
context pointer and compares the same object word with that referenced
object's word at offset `0x318`. Either equality match passes the input object
to `func_1516972C`; mismatches and all other event values return unchanged.

The third formal is `u8`, reproducing retail's incoming stack home and byte
canonicalization. Naming the event-zero referenced object as an explicit local
makes IDO retain it in `v0` and use `t0` for the nested owner word, matching
retail's allocation. All 29 words emit directly from semantic C. No
expected-word guards or compiler-profile override are required.

## Verification

- The focused `generated_1F4650.c.o` build passed under the existing
  `-O2 -g3` profile; all 29 words and two call relocations match retail.
- The full `wsl make NON_MATCHING=1` relink passed from `conker`.
- `match_progress.py` classifies `func_151CB49C` as byte-exact.
- The linked ELF and retail 116-byte spans share SHA-256
  `3232754db39e3f954bcc006026de28587b62ebe879fe65f461b4b3b2f1c4b870`.
- Fresh matcher totals are `2,926 / 5,466 (53.53%)` overall and
  `2,352 / 4,790 (49.10%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_15034340`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
