# Game actor-slot selector byte match

Date: 2026-09-29

## Scope and behavior

`func_1503F964` in `conker/src/game/generated_6CCB0.c` occupies 35 words and
140 bytes at `0x1503F964..0x1503F9F0`. When `D_800C67F0` is enabled, it starts
after the cursor in `D_800C67F1`, wraps across 25 actor slots, and selects the
first `D_800CC2D0` entry whose `unkF8` field has bit `0x00800000` set. A full
cycle leaves the saved cursor unchanged.

## Source recovery

The previous implementation was a false zero-return placeholder. The recovered
body restores the enable gate, wrapped cursor scan, 812-byte actor stride,
selection-bit test, and selected-index store. The return type is `void`, which
matches the retail routine's lack of a defined return value and its known
caller's ignored result.

IDO reproduces the complete control flow, instruction count, branch-delay
updates, constants, and relocations. One closed compiler-allocation cycle
remains: retail keeps the scan index in `a0` and the actor-table base in `v1`,
while the recovered C chooses those registers in reverse. Fourteen
stale-checked guards normalize only that cycle, including the relocation-aware
`D_800CC2D0` address pair. No words are inserted or omitted.

## Verification

- The focused `generated_6CCB0` object emits the complete 35-word retail
  instruction stream after the 14 expected-word guards are applied.
- A full guard-table rebuild reaches the linked ELF without a stale-guard
  failure.
- The authoritative linked matcher reports `3,006 / 5,463 (55.02%)` overall
  and `2,428 / 4,789 (50.70%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 140 bytes.
- Both spans share SHA-256
  `2a29585ac9a143e8d168f4be74450d0b0bd8d0342407f438c8ed303bb2f53260`.
- `make tools-check`, all 10 tests under `tools/tests`,
  `make -C conker replace NON_MATCHING=1 -j4`, and the outer
  `make NON_MATCHING=1 -j4` build pass.

## Resume boundary

Inspect `func_15022640` as the next ordinary 29-difference Game candidate.
Keep `func_15015F40` parked behind its unresolved indirect-table ownership,
`func_150A76F0` in the handwritten-assembly queue, and Init `func_1000FF90`
parked at its measured compiler-allocation boundary.
