# Game audio DMA prefetch wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_151F3D78` in `conker/src/libultra/audio/game_21FC90.c` spans 26 words
and 104 bytes at `0x151F3D78..0x151F3DE0`. It asks `n_syn->dma` for the active
DMA procedure and state, then requests an `0x810`-byte transfer from
`D_800E0D80 + D_800E0DE4` with a zero final argument.

The recovered body compiles instruction-for-instruction from semantic C. No
expected-word guards or assembly replacement are needed.

## Object layout correction

`game_21FC90.c` previously bypassed retail padding, so expanding the false
two-word placeholder shifted the following object even though the recovered
function matched in isolation. The object now uses the established retail
padding path. Its `.text` is exactly `0x1480` bytes and places
`func_151F3D78` at relative offset `0x1418`, matching its retail address.

Two layout rows that incorrectly assigned standalone sources
`func_151F27E0.c` and `func_151F2890.c` to `game_21FC90` now name their actual
owners. The padding tool adds hidden address-named functions
`func_151F2DFC` and `func_151F3C1C` from their compiled symbols. Existing
oversized `func_151F2E88` remains behavior-preserved through the established
`.game_overflow` trampoline; this object contributes `0xB8C` bytes there.

## Verification

- The complete non-matching build and ELF link pass.
- The linked map places `game_21FC90` at `0x151F2960..0x151F3DE0`, with the
  following function beginning at `0x151F3DE0`.
- Direct comparison passes all 104 linked bytes. Both spans share SHA-256
  `3a57cd163b38e4edc9e3beea97a3bbb961bff87fc574ec20cb1f18e5e8d135b7`.
- The authoritative matcher reports `2,979 / 5,465 (54.51%)` overall and
  `2,404 / 4,789 (50.20%)` in Game, with zero address-drift rows.
- The clean full regeneration independently moves unchanged 17-word Init
  routine `func_10012588` from address drift to exact. This is a stale-build
  reclassification, not a second source recovery in this change.

## Resume boundary

Continue with the next ordinary small Game candidate. Keep `func_151A8584`
and `func_151A85D4` parked at their early-spill boundary, and keep
`func_1506EF5C` parked at its broad register-allocation mismatch. The
`game_21FC90` layout blocker and the final Init address-drift row are closed.
