# Game group-value deduplicating append byte match

Date: 2026-09-29

## Scope and behavior

`func_15022640` in `conker/src/game/generated_49D30.c` occupies 31 words and
124 bytes at `0x15022640..0x150226BC`. It searches the populated prefix of a
30-byte `D_800C3550[group]` row for an incoming value. A duplicate returns
without changing state; a new value is appended at the byte count held in
`D_800C354A[group]`, and that count is incremented.

## Source recovery

The previous implementation was a false zero-return placeholder. The recovered
body expresses `D_800C3550` as 30-byte rows, retains a pointer to the selected
count byte, snapshots that count as an `s32`, and uses a separate signed loop
bound. Those lifetimes reproduce retail's count pointer in `v1`, count in
`a2`, loop bound in `a3`, index in `v0`, and row cursor in `t0`.

The incoming value must be an `s32`. Declaring it as `u8` makes IDO spill and
truncate `a0`, adding three instructions that retail does not have; retail
instead relies on the caller's byte load. With the corrected ABI and explicit
loop-bound lifetime, the complete routine emits directly from C with no
expected-word guards.

## Verification

- The focused `generated_49D30` object matches all 31 retail words, including
  both global relocation pairs and the signed `slt`/`bnez` loop test.
- The authoritative linked matcher reports `3,007 / 5,463 (55.04%)` overall
  and `2,429 / 4,789 (50.72%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 124 bytes.
- Both spans share SHA-256
  `6a43dab9f135f13b92604ed942ab52b6b38913b931457760c0544a753e3cbc88`.
- `make tools-check`, all 10 tests under `tools/tests`,
  `make -C conker replace NON_MATCHING=1 -j4`, and the outer
  `make NON_MATCHING=1 -j4` build pass.

## Resume boundary

Inspect `func_15168F08` as the next ordinary 29-difference Game candidate.
Keep `func_15015F40` parked behind its unresolved indirect-table ownership,
`func_150A76F0` in the handwritten-assembly queue, and Init `func_1000FF90`
parked at its measured compiler-allocation boundary.
