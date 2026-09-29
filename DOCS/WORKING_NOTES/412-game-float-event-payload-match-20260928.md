# Game float event-payload wrapper byte match

Date: 2026-09-28

## Scope

This pass completed `func_150E8854` in
`conker/src/game/generated_113D60.c`. The retail slot spans 27 words and 108
bytes.

## Recovered behavior

The wrapper prepares a `10.0f` payload and calls `func_15149130` with event
identifier `0x12C`, subtype `0x35`, a four-byte payload size, and the remaining
retail mode and sentinel arguments. If allocation succeeds, it copies the
four-byte payload into offset `0x28` of the returned record.

Recovering the allocator's pointer return and narrow argument types reproduces
the retail call convention, frame, branch, and `memcpy` call. IDO places the
four-byte scalar at `sp+0x34`, while retail uses the equivalent lower local
word at `sp+0x30`. Alternative array, structure, and extra-local source shapes
either retained `sp+0x34` or enlarged the frame to `0x40`.

Semantic C therefore emits 25 of the 27 words directly. Two expected-word
guards change only the scalar store and matching `memcpy` source address from
`sp+0x34` to `sp+0x30`; no control flow, data value, call target, or register
lifetime is replaced.

## Verification

- The focused `generated_113D60.c.o` build passed under the existing
  `-O2 -g3` profile.
- Post-guard object disassembly matches all 27 retail instruction words and
  both call relocations.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_150E8854` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `1e7751de0c93b1888850f728df5f0b90a89bcaa36e83dbabbfbaa07772aa5503`.
- Fresh matcher totals are `2,914 / 5,466 (53.31%)` overall and
  `2,340 / 4,790 (48.85%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with adjacent 28-word `func_150E88C0`,
currently at 26 real differences. Keep the documented lower-difference
compiler cases parked. Also keep `func_151F3D78` parked behind the pre-existing
audio-object layout drift, keep the tied Init SDK cache routines in their
ownership lane, and keep address-drift row `func_10012588` parked.
