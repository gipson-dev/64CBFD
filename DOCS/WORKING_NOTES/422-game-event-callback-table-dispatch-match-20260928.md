# Game event callback-table dispatch byte match

Date: 2026-09-28

## Scope

This pass completed `func_15190550` in
`conker/src/game/generated_1BA1D0.c`. The retail slot spans 27 words and 108
bytes at `0x15190550..0x151905B8`.

## Recovered behavior

The routine receives an object, an opaque context, and an event byte. Event
`0x2A` first calls `func_151D33FC(object, context)`. It then reads the callback
index from object offset `0x8A`, loads that entry from `D_8008D684`, and, when
the entry is non-null, invokes it with the original object, context, and event
byte.

The third formal is `u8`, reproducing retail's incoming stack home and byte
canonicalization. The compiler preserves the context across the optional
pre-handler and saves/restores the event byte only on that path. A typed
three-argument function-pointer table naturally emits retail's branch-likely
null gate and `jalr` delay-slot reload. All 27 words emit directly from
semantic C; no expected-word guards or compiler-profile override are needed.

## Verification

- The focused `generated_1BA1D0.c.o` build passed under the existing
  `-O2 -g3` profile; all 27 words and three relocations match retail.
- The full `wsl make NON_MATCHING=1` relink passed from `conker`.
- `match_progress.py` classifies `func_15190550` as byte-exact.
- The linked ELF and retail 108-byte spans share SHA-256
  `9193a39a64e3fed0ea5f093cf70ce6e95b41bc79c21f38a34ca894441df6fe66`.
- Fresh matcher totals are `2,924 / 5,466 (53.49%)` overall and
  `2,350 / 4,790 (49.06%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_151B222C`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
