# Game mapped three-byte-row dispatch byte match

Date: 2026-09-28

## Scope

This pass completed `func_1517F3A0` in
`conker/src/game/generated_1AC2F0.c`. The retail slot spans 27 words and 108
bytes at `0x1517F3A0..0x1517F408`.

## Recovered behavior

The routine passes its selector argument to `func_1517EF00`. A zero mapping
returns the original first argument unchanged. A nonzero mapping selects the
three-byte row at `D_800DDDA0 + selector * 3`, then calls `func_1517F08C` with
the original first argument, mapped value, the row's three unsigned bytes, and
the original selector as the sixth argument.

Writing the zero-map path as an early return is part of the recovered source
shape. It makes IDO emit retail's `bnez` into the dispatch path followed by an
ordinary branch whose delay slot copies the passthrough result. Nesting the
dispatch under a nonzero test emits an extra post-call branch and overruns the
retail slot by one word. The accepted form emits all 27 words directly from
semantic C; no expected-word guards or compiler-profile override are needed.

## Verification

- The focused `generated_1AC2F0.c.o` build passed under the existing
  `-O2 -g3` profile; all 27 words and four relocations match retail.
- The full `wsl make NON_MATCHING=1` relink passed from `conker`.
- `match_progress.py` classifies `func_1517F3A0` as byte-exact.
- The linked ELF and retail 108-byte spans share SHA-256
  `bca8c2263f7d6ccb6f2a7572fc5ed850bef668670172b0d7be811a287aff4595`.
- Fresh matcher totals are `2,923 / 5,466 (53.48%)` overall and
  `2,349 / 4,790 (49.04%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_15190550`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
