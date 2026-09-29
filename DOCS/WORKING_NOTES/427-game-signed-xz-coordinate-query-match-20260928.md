# Game signed XZ coordinate query byte match

Date: 2026-09-28

## Scope

This pass completed `func_15045714` in
`conker/src/game/generated_71820.c`. The retail slot spans 27 words and 108
bytes at `0x15045714..0x1504577C`.

## Recovered behavior

The routine selects query mode `2` through `func_1510F800`, then reads the X
and Z floats at position offsets `0` and `8`. Each coordinate is truncated to
an integer and narrowed to signed 16 bits before being passed to
`func_150A6500` with the full-width context and unsigned 16-bit selector. The
returned query handle is stored through the caller's output pointer.

The typed four-argument body reproduces retail's argument homes, selector
halfword reload, paired float conversions, narrowing sequence, calls, and
result store. IDO selects `v1` for the position-pointer reload where retail
uses `v0`; explicit scalar locals produce the same allocation. Three guarded
words normalize that closed pointer register cycle. The other 24 words emit
directly from semantic C, and no compiler-profile override is required.

## Verification

- The focused `generated_71820.c.o` build passed under the existing
  `-O2 -g3` profile; all 27 words and both call relocations match retail after
  the three guarded register-allocation words.
- The full `wsl make NON_MATCHING=1` rebuild and relink passed from `conker`.
- `match_progress.py` classifies `func_15045714` as byte-exact.
- The linked ELF and retail 108-byte spans share SHA-256
  `84efd8a61af7f41170600c4e2a234589aa9723e0da7953b036a48ac0b383bb43`.
- Fresh matcher totals are `2,929 / 5,466 (53.59%)` overall and
  `2,355 / 4,790 (49.16%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 30-word `func_15049C40`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
