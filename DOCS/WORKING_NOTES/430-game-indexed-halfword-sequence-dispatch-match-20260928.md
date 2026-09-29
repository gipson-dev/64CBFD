# Game indexed halfword-sequence dispatcher byte match

Date: 2026-09-28

## Scope

This pass completed `func_15080784` in
`conker/src/game/generated_AD9B0.c`. The retail slot spans 28 words and 112
bytes at `0x15080784..0x150807F0`.

## Recovered behavior

The routine returns immediately when the halfword-sequence pointer in
`D_800D1998` is null or when current byte index `D_800D1994` equals end byte
index `D_800D1995`. Otherwise it reads the current unsigned halfword entry.

A nonzero entry is forwarded to `func_1001263C` with fixed arguments `0x7FFF`
and `0x40`. Zero entries skip that call. Both paths increment
`D_800D1994`; the call path deliberately reloads the current index afterward,
matching retail's treatment of the global as externally mutable.

Using an `s32` local for the zero-extended halfword preserves it directly in
the first call-argument register. Reversing the source comparison order
reproduces retail's commutative equality operand order. Together these choices
emit the frame, branch-likely exits, sequence addressing, optional call,
post-call reload, index increment, and epilogue directly from semantic C. No
expected-word guards or compiler-profile override are required.

## Verification

- The focused `generated_AD9B0.c.o` build passed under the existing
  `-O2 -g3` profile; all 28 words and the call relocation match retail.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`.
- `match_progress.py` classifies `func_15080784` as byte-exact.
- The linked ELF and retail 112-byte spans share SHA-256
  `f594c1f1cae3306800ce46b21fb1fccc6e04787a892f61d7011e3f63ee5f65b1`.
- Fresh matcher totals are `2,932 / 5,466 (53.64%)` overall and
  `2,358 / 4,790 (49.23%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_150B1DB0`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
