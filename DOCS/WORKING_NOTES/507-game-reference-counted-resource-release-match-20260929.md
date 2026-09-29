# Game reference-counted resource release byte match

Date: 2026-09-29

## Scope and behavior

`func_1518CA04` in `conker/src/game/generated_1B9DB0.c` occupies a 31-word,
124-byte tracked slot at `0x1518CA04..0x1518CA80`. Index `0x1E4` is reserved
and returns immediately. Every other index addresses a byte counter in
`D_800DF7D0`; a nonzero counter is decremented, and only a transition to zero
releases the corresponding allocation from `D_800DF9B8` and retags the
payload from `D_800E0148` with type four.

## Source recovery

The previous body was a false zero-return placeholder. The recovered
declarations identify `D_800DF9B8` as an array of `s16 *` allocations accepted
by `func_1510D630` and `D_800E0148` as an array of `s32 *` payload pointers
accepted by `func_100043B4`.

An initial explicit pointer/value implementation recovered the behavior but
reversed retail's `v0`/`v1` allocation and produced a `0x28` frame. Expressing
the update as a short-circuit nonzero check with prefix decrement restores
retail's `v0` counter pointer, `v1` byte value, decrement delay slots, `0x20`
frame, scaled-index spill, and both cleanup calls. All executable words and
the trailing tracked padding word emit directly with no guards.

## Verification

- The focused `generated_1B9DB0` object reproduces the complete tracked slot.
- The full replacement build and outer non-matching ROM build pass.
- The authoritative linked matcher reports `3,011 / 5,463 (55.12%)` overall
  and `2,433 / 4,789 (50.80%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 124 bytes.
- Both spans share SHA-256
  `dfa0b48be60169a821895ce7a48189eff8755b2d682a1497651eaec3aa1b925a`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_15194794` as the next ordinary 29-difference Game candidate.
Keep `func_15015F40` parked behind its unresolved indirect-table ownership,
`func_150A76F0` in the handwritten-assembly queue, and Init `func_1000FF90`
parked at its measured compiler-allocation boundary.
