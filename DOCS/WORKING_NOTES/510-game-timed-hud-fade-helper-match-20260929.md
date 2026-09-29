# Game timed HUD fade helper byte match

Date: 2026-09-29

## Scope and behavior

`func_151EC178` in `conker/src/game/generated_215960.c` occupies 30 words and
120 bytes at `0x151EC178..0x151EC1F0`. It returns the incoming display-list
pointer unchanged. Once `D_800E0A90` reaches `0x5DD`, it computes an alpha of
`(timer - 0x5DC) << 3`, saturates values at `0xFF`, applies white modulation
through `func_1504332C`, and draws `D_800E0BD8[0x74]` at `(0xDC, 0x130)`.

## Source recovery

The previous body was a false zero-return placeholder. The recovered C caches
the timer once, preserves separate delta, scaled, and alpha lifetimes, narrows
the color alpha to a byte, performs the two calls, and returns the original
display-list pointer.

IDO still coalesces the scaled and result lifetimes, producing a semantically
equivalent 29-word body followed by one padding word. Nineteen relocation-aware
stale checks restore retail's explicit merge move and shift the closed call and
epilogue tail by one word. Both call relocations remain symbolic, the tracked
slot stays 30 words, and no neighboring function moves.

## Verification

- The focused `generated_215960` object accepts all 19 stale checks.
- The full guard-table rebuild, replacement build, outer non-matching build,
  and ELF relink pass.
- The authoritative matcher reports `3,014 / 5,463 (55.17%)` overall and
  `2,436 / 4,789 (50.87%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 120 linked bytes.
- Both spans share SHA-256
  `3d94d64b056ac0c8f9b14949c3456faa92bfe86305e718365922d0f7e438a47b`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_15080BE8` as the next ordinary 31-word Game candidate. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten-assembly queue.
