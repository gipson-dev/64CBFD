# Game byte-selected coefficient clamp byte match

Date: 2026-09-29

## Scope and behavior

`func_15182F58` in `conker/src/game/generated_1AFC80.c` occupies 33 words and
132 bytes at `0x15182F58..0x15182FDC`. It uses `D_800DDE54[arg1]` to select a
24-byte row at `D_8008D058`, reads the row's leading floating coefficient,
and multiplies it by the integer expression `arg0 * 40`. The result is
clamped to the inclusive range `0.0f..39.0f` and returned.

## Source recovery

The previous body was a false zero-return placeholder. A narrow row type
captures only the proven leading coefficient and 24-byte stride. Keeping the
scale as integer arithmetic before conversion reproduces retail's shift/add
sequence and single `cvt.s.w` rather than introducing floating multiplication
by a constant.

The clamp is mutually exclusive: a negative result takes the lower-bound
exit, while only a nonnegative result is tested against the upper bound.
Writing this as `if` followed by `else if` restores retail's unconditional
lower-bound branch and complete 33-word extent. IDO emits the entire routine
directly from C with no expected-word guards.

## Verification

- The focused `generated_1AFC80` object emits all 33 retail words directly.
- The full replacement build and outer non-matching ROM build pass.
- The authoritative linked matcher reports `3,010 / 5,463 (55.10%)` overall
  and `2,432 / 4,789 (50.78%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 132 bytes.
- Both spans share SHA-256
  `0873fbb7ea8b86165e60c1c6cdb73f6cb692d345f177b80efa4b6165f1847db2`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_1518CA04` as the next ordinary 29-difference Game candidate.
Keep `func_15015F40` parked behind its unresolved indirect-table ownership,
`func_150A76F0` in the handwritten-assembly queue, and Init `func_1000FF90`
parked at its measured compiler-allocation boundary.
