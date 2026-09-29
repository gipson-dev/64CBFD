# Game packed-mask setter byte match

Date: 2026-09-29

## Scope and behavior

`func_1507A4D4` in `conker/src/game_A28B0.c` spans 21 words and 84 bytes. It
packs bytes `D_800D1890` through `D_800D1893` into one big-endian 32-bit mask
and sets those bits in the active object's word at offset `0x94`.

The recovered explicit `u32 mask` local mirrors the adjacent byte-exact
clear-mask routine `func_1507A47C`. It prevents the source from obscuring the
two-stage operation and gives both routines the same semantic ownership.

Five words emit directly from semantic C: the opening first-byte address, the
active-object address and pointer loads, and the return pair. Sixteen
fail-closed expected-word guards normalize IDO's packed-byte load order and
temporary-register allocation. This is the set-mask counterpart of
`func_1507A47C`'s existing 18 guarded words; every moved global access retains
an explicit expected and replacement relocation.

## Verification

- The focused padded object builds with all sixteen expected-word guards
  firing.
- The complete non-matching build and relink pass.
- Direct comparison passes all 84 linked bytes. Both spans share SHA-256
  `7b5a575d011936f80c735669b60c8a2a24d26c2cde4ca4a610ce057a70c219fe`.
- The authoritative matcher reports `2,976 / 5,465 (54.46%)` overall and
  `2,402 / 4,789 (50.16%)` in Game, with one address-drift row.

## Resume boundary

Continue with the next ordinary small Game candidate. Keep `func_151A8584`
and `func_151A85D4` parked at IDO's 21-word early-spill form versus retail's
20-word delay-slot spill. Keep `func_1506EF5C` parked at its broad 19-word
register-allocation mismatch; the m2c-style repeated-global form exceeds the
retail span. All experiments for those rows were removed and their focused
objects restored before this match was started.
