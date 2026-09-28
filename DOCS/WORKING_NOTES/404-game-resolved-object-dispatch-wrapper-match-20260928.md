# Game resolved-object dispatch wrapper byte match

Date: 2026-09-28

## Scope

This pass replaced the empty placeholder for `func_1509F5F4` in
`conker/src/game/generated_CBDB0.c` with its semantic Game wrapper. The retail
slot spans 27 words and 108 bytes.

## Recovered behavior

The function resolves `arg2` through `func_1505EEF4`. A failed lookup returns
without dispatching. When an object is found, nonzero `arg5` bypasses the
`func_10010894` validation; otherwise dispatch proceeds only when that check
returns zero. The accepted object and the remaining narrowed arguments are
forwarded to `func_10010344`.

The short-circuit expression preserves retail's branch-likely validation
bypass. Keeping the resolved object in a local also reproduces its spill before
`func_10010894` and reload into `a1` afterward. The `u16` and `s16` parameter
types emit retail's incoming argument spills and narrow reloads. All 27 words
emit directly from C; no expected-word guards or compiler-profile changes are
required.

## Verification

- The focused `generated_CBDB0.c.o` build passed under the existing profile.
- Focused object disassembly matches all 27 retail instruction words and
  relocations.
- The full `wsl make -C conker NON_MATCHING=1` rebuild and relink passed.
- `match_progress.py` classifies `func_1509F5F4` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `9239aa6a6b4788f6821422b9ce5c85dce833dc9fb1bc102ab1e18ccad7a4e820`.
- Fresh matcher totals are `2,906 / 5,466 (53.17%)` overall and
  `2,332 / 4,790 (48.68%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_150A0264`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
